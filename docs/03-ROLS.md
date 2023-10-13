
# (PART) Linear Regression in R {-} 

This section is a quick overview of linear regression models from the perspective that ``all models are wrong, but some are useful''. For more in-depth introductions, which typically begin by assuming the true data generating process is linear, see https://jadamso.github.io/Rbooks/ordinary-least-squares.html#more-literature. 



# Ordinary Least Squares
***

## Simple OLS (linear regression)
Model and objective
$$
y_i=\alpha+\beta x_i+\epsilon_{i} \\
\epsilon_{i} = y_i - [\alpha+\beta x_i]\\
min_{\beta} \sum_{i=1}^{n} (\epsilon_{i})^2
$$


Point Estimates
$$
\hat{\alpha}=\bar{y}-\hat{\beta}\bar{x} = \widehat{\mathbb{E}}[Y] - \hat{\beta} \widehat{\mathbb{E}}[X] \\
\hat{\beta}=\frac{\sum_{i}^{}(x_i-\bar{x})(y_i-\bar{y})}{\sum_{i}^{}(x_i-\bar{x})^2} = \frac{\widehat{Cov}[X,Y]}{\widehat{\mathbb{V}}[X]}\\
\hat{y}_i=\hat{\alpha}+\hat{\beta}x_i\\
\hat{\epsilon}_i=y_i-\hat{y}_i\\
$$


```r
## Generate Dataset
xy <- USArrests[,c('Murder','UrbanPop')]
colnames(xy) <- c('y','x')

## Plot Data
plot(y~x, xy, col=grey(.5,.5), pch=16)

## Estimate Regression Coefficeints
reg <- lm(y~x, dat=xy)
reg 
```

```
## 
## Call:
## lm(formula = y ~ x, data = xy)
## 
## Coefficients:
## (Intercept)            x  
##     6.41594      0.02093
```

```r
## Point Estimates
coef(reg)
```

```
## (Intercept)           x 
##  6.41594246  0.02093466
```

```r
## Add Predictions to Plot
abline(reg, col='orange')
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-1-1.png" width="672" />

To measure the ''Goodness of fit'', we analyze sums of squared errors
$$
\underbrace{\sum_{i}(y_i-\bar{y})^2}_\text{TSS}=\underbrace{\sum_{i}(\hat{y}_i-\bar{y})^2}_\text{RSS}+\underbrace{\sum_{i}\hat{\epsilon_{i}}^2}_\text{ESS}\\
R^2 = \frac{RSS}{TSS}=1-\frac{ESS}{TSS}
$$
Note that $R^2$ is also called the coefficient of determination.


```r
## Manually Compute Goodness of Fit
Ehat <- resid(reg)
ESS  <- sum(Ehat^2)
Y <- xy$y
TSS  <- sum((Y-mean(Y))^2)
R2 <- 1 - ESS/TSS
R2
```

```
## [1] 0.00484035
```

```r
## Check R2
summary(reg)$r.squared
```

```
## [1] 0.00484035
```

### Variability Estimates

A regression coefficient is a statistic. And, just like all statistics, we can calculate 

* *standard deviation*: variability within a single sample.
* *standard error*: variability across different samples.
* *confidence interval* range of variability across different samples.
* *p-value* the probability you would see something as extreme as your statistic under the null (assuming your null hypothesis was true).
* null distribution*: the distribution of the statistic under the null hypothesis.

The classic estimates for variability are the Standard Error of the Regression $\hat{\sigma}$, and Standard Error of the Coefficient Estimates $\hat{\sigma}_{\hat{\alpha}}$ and $\hat{\sigma}_{\hat{\alpha}}~~$ (or simply Standard Errors).
$$
\hat{\sigma}^2 = \frac{1}{n-2}\sum_{i}\hat{\epsilon_{i}}^2\\
\hat{\sigma}^2_{\hat{\alpha}}=\hat{\sigma}^2\left[\frac{1}{n}+\frac{\bar{x}^2}{\sum_{i}(x_i-\bar{x})^2}\right]\\
\hat{\sigma}^2_{\hat{\beta}}=\frac{\hat{\sigma}^2}{\sum_{i}(x_i-\bar{x})^2}.
$$
These equations are motivated by particular data generating proceses, which you can read more about this at https://www.econometrics-with-r.org/4-lrwor.html. We can also estimate variabilty using *data-driven* methods that assume much less. See, e.g., https://www.sagepub.com/sites/default/files/upm-binaries/21122_Chapter_21.pdf

We first consider the simplest, the jackknife, where we loop through each row of the dataset. In each iteration of the loop, we drop that observation from the dataset and reestimate the statistic of interest. We then calculate the standard deviation of the statistic across all ``resamples''.


```r
## Example 1 Continued

## Jackknife Standard Errors for Beta
jack_regs <- lapply(1:nrow(xy), function(i){
    xy_i <- xy[-i,]
    reg_i <- lm(y~x, dat=xy_i)
})
jack_coefs <- sapply(jack_regs, coef)['x',]
jack_mean <- mean(jack_coefs)
jack_se <- sd(jack_coefs)

## Jackknife Confidence Intervals
jack_ci_percentile <- quantile(jack_coefs, probs=c(.025,.975))
hist(jack_coefs, breaks=25,
    main=paste0('SE est. = ', round(jack_se,4)),
    xlab=expression(beta[-i]))
abline(v=jack_mean, col="red", lwd=2)
abline(v=jack_ci_percentile, col="red", lty=2)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-3-1.png" width="672" />

```r
## Plot Full-Sample Estimate
## abline(v=coef(reg)['x'], lty=1, col='blue', lwd=2)

## Plot Normal Approximation
## jack_ci_normal <- jack_mean+c(-1.96, +1.96)*jack_se
## abline(v=jack_ci_normal, col="red", lty=3)
```

There are several other resampling techniques. We consider the other main one, the bootstrap, which resamples with *replacement* for an *arbitrary* number of iterations. For a dataset with $n$ observations, you now randomly resamples all $n$ rows in your data set $B$ times. 

| | Sample Size per Iteration | Number of Iterations | Resample |
| -------- | ------- | ------- | ------- |
Bootstrap | $n$     | $B$  | With Replacement |
Jackknife | $n-1$   | $n$  | Without Replacement |


```r
## Bootstrap Standard Errors for Beta
boots <- 1:399
boot_regs <- lapply(boots, function(b){
    b_id <- sample( nrow(xy), replace=T)
    xy_b <- xy[b_id,]
    reg_b <- lm(y~x, dat=xy_b)
})
boot_coefs <- sapply(boot_regs, coef)['x',]
boot_mean <- mean(boot_coefs)
boot_se <- sd(boot_coefs)

## Bootstrap Confidence Intervals
boot_ci_percentile <- quantile(boot_coefs, probs=c(.025,.975))
hist(boot_coefs, breaks=25,
    main=paste0('SE est. = ', round(boot_se,4)),
    xlab=expression(beta[b]))
abline(v=boot_mean, col="red", lwd=2)
abline(v=boot_ci_percentile, col="red", lty=2)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-4-1.png" width="672" />

```r
## Normal Approximation
## boot_ci_normal <- boot_mean+c(-1.96, +1.96)*boot

## Parametric CI
## x <- data.frame(x=quantile(xy$x,probs=seq(0,1,by=.1)))
## ci <- predict(reg, interval='confidence', newdata=data.frame(x))
## polygon( c(x, rev(x)), c(ci[,'lwr'], rev(ci[,'upr'])), col=grey(0,.2), border=0)
```

We can also bootstrap other statistics, such as a t-statistic or $R^2$. We do such things to test a null hypothesis, which is often ``no relationship''. We are rarely interested in computing standard errrors and conducting hypothesis tests for two variables. However, we work through the ideas in the two-variable case to better understand the multi-variable case.

### Hypothesis Tests

There are two main ways to conduct a hypothesis test.
 
**Invert a CI**
One main way to conduct hypothesis tests is to examine whether a confidence interval contains a hypothesized value. Often, this is $0$.

```r
## Example 1 Continued Yet Again

## Bootstrap Distribution
boot_ci_percentile <- quantile(boot_coefs, probs=c(.025,.975))
hist(boot_coefs, breaks=25,
    main=paste0('SE est. = ', round(boot_se,4)),
    xlab=expression(beta[b]), 
    xlim=range(c(0, boot_coefs)) )
abline(v=boot_ci_percentile, lty=2)
abline(v=0, col="red", lwd=2)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-5-1.png" width="672" />


**Impose the Null**
We can also compute a null distribution using *data-driven* methods that assume much less about the data generating process. We focus on the simplest, the bootstrap, where loop through a large number of simulations. In each iteration of the loop, we drop impose the null hypothesis and reestimate the statistic of interest. We then calculate the standard deviation of the statistic across all ``resamples''.


```r
## Example 1 Continued Again

## Null Distribution for Beta
boots <- 1:399
boot_regs0 <- lapply(boots, function(b){
    xy_b <- xy
    xy_b$y <- sample( xy_b$y, replace=T)
    reg_b <- lm(y~x, dat=xy_b)
})
boot_coefs0 <- sapply(boot_regs0, coef)['x',]

## Null Bootstrap Distribution
boot_ci_percentile0 <- quantile(boot_coefs0, probs=c(.025,.975))
hist(boot_coefs0, breaks=25, main='',
    xlab=expression(beta[b]),
    xlim=range(c(boot_coefs0, coef(reg)['x'])))
abline(v=boot_ci_percentile0, lty=2)
abline(v=coef(reg)['x'], col="red", lwd=2)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-6-1.png" width="672" />

Regardless of how we calculate standard errors, we can use them to conduct a t-test. We also compute the distribution of t-values under the null hypothesis, and compare how extreme the oberved value is.
$$ \hat{t} = \frac{\hat{\beta} - \beta_{0} }{\hat{\sigma}_{\hat{\beta}}} $$


```r
## T Test
B0 <- 0
boot_t  <- (coef(reg)['x']-B0)/boot_se

## Compute Bootstrap T-Values (without refinement)
boot_t_boot0 <- sapply(boot_regs0, function(reg_b){
    beta_b <- coef(reg_b)[['x']]
    t_hat_b <- (beta_b)/boot_se
    return(t_hat_b)
})
hist(boot_t_boot0, breaks=100,
    main='Bootstrapped t values', xlab='t',
    xlim=range(c(boot_t_boot0, boot_t)) )
abline(v=boot_t, lwd=2, col='red')
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-7-1.png" width="672" />

From this, we can calculate a *p-value*: the probability you would see something as extreme as your statistic under the null (assuming your null hypothesis was true). Note that the $p$ reported by your computer does not necessarily satisfy this definition. We can always calcuate a p-value from an explicit null distribution.

```r
## One Sided Test for P(t > boot_t | Null)=1- P(t < boot_t | Null)
That_NullDist1 <- ecdf(boot_t_boot0)
Phat1  <- 1-That_NullDist1(boot_t)

## Two Sided Test for P(t > jack_t or  t < -jack_t | Null)
That_NullDist2 <- ecdf(abs(boot_t_boot0))
plot(That_NullDist2, xlim=range(boot_t_boot0, boot_t))
abline(v=quantile(That_NullDist2,probs=.95), lty=3)
abline(v=boot_t, col='red')
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-8-1.png" width="672" />

```r
Phat2  <-  1-That_NullDist2(boot_t)
Phat2
```

```
## [1] 0.5989975
```
Under some assumptions, the null distribution is distributed $t_{n-2}$. (For more on parametric t-testing based on statistical theory, see https://www.econometrics-with-r.org/4-lrwor.html.)


### Prediction Intervals

In addition to confidence intervales, we can also compute a *prediction interval* which estimates the range of variability across different samples for the outcomes. These intervals also take into account the residuals--- the variability of individuals around the mean. 



```r
## Bootstrap Prediction Interval
boot_resids <- lapply(boot_regs, function(reg_b){
    e_b <- resid(reg_b)
    x_b <- reg_b$model$x
    res_b <- cbind(e_b, x_b)
})
boot_resids <- as.data.frame(do.call(rbind, boot_resids))
## Homoskedastic
ehat <- quantile(boot_resids$e_b, probs=c(.025, .975))
x <- quantile(xy$x,probs=seq(0,1,by=.1))
boot_pi <- coef(reg)[1] + x*coef(reg)['x']
boot_pi <- cbind(boot_pi + ehat[1], boot_pi + ehat[2])

## Plot Bootstrap PI
plot(y~x, dat=xy, pch=16, main='Prediction Intervals',
ylim=c(-5,20))
polygon( c(x, rev(x)), c(boot_pi[,1], rev(boot_pi[,2])),
    col=grey(0,.2), border=NA)

## Parametric PI (For Comparison)
pi <- predict(reg, interval='prediction', newdata=data.frame(x))
lines( x, pi[,'lwr'], lty=2)
lines( x, pi[,'upr'], lty=2)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-9-1.png" width="672" />

There are many ways to improve upon the prediction intervals you just created. Probably the most basic way is to allow the residuals to be heteroskedastic. 


```r
## Estimate Residual Quantiles seperately around X points
boot_resid_list <- split(boot_resids,
    cut(boot_resids$x_b, x) )
boot_resid_est <- lapply(boot_resid_list, function(res_b) {
    if( nrow(res_b)==0){ ## If Empty, Return Nothing
        ehat <- c(NA,NA)
    } else{ ## Estimate Quantiles of Residuals
        ehat <- quantile(res_b$e_b, probs=c(.025, .975))
    }
    return(ehat)
    })
boot_resid_est <- do.call(rbind, boot_resid_est)
## Construct PI at x points
boot_x <- x[-1] - diff(x)/2
boot_pi <- coef(reg)[1] + boot_x*coef(reg)['x']
boot_pi <- cbind(boot_pi + boot_resid_est[,1], boot_pi + boot_resid_est[,2])

plot(y~x, dat=xy, pch=16, main='Heteroskedastic P.I.')
polygon( c(boot_x, rev(boot_x)), c(boot_pi[,1], rev(boot_pi[,2])),
    col=grey(0,.2), border=NA)
rug(boot_x)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-10-1.png" width="672" />


For a nice overview of different types of intervals, see https://www.jstor.org/stable/2685212. For an indepth view, see "Statistical Intervals: A Guide for Practitioners and Researchers" or "Statistical Tolerance Regions: Theory, Applications, and Computation". See https://robjhyndman.com/hyndsight/intervals/ for constructing intervals for future observations in a time-series context. See Davison and Hinkley, chapters 5 and 6 (also Efron and Tibshirani, or Wehrens et al.)


## OLS (multiple linear regression)

Model and objective
$$
y_i=\beta_0+\beta_1x_{i1}+\beta_2x_{i2}+\ldots+\beta_kx_{ik}+\epsilon_i = X_{i}\beta +\epsilon_i \\
min_{\beta} \sum_{i=1}^{n} (\epsilon_i)^2
$$
Can be written in matrix form
$$
y=\textbf{X}\beta+\epsilon\\
min_{\beta} (\epsilon' \epsilon)
$$
Point Estimates 
$$
\hat{\beta}=(\textbf{X}'\textbf{X})^{-1}\textbf{X}'y
$$


```r
## Example 2 (Empirical)
## Inspect Dataset on police arrests for the USA in 1973
head(USArrests)
```

```
##            Murder Assault UrbanPop Rape
## Alabama      13.2     236       58 21.2
## Alaska       10.0     263       48 44.5
## Arizona       8.1     294       80 31.0
## Arkansas      8.8     190       50 19.5
## California    9.0     276       91 40.6
## Colorado      7.9     204       78 38.7
```

```r
## Simple Plot
#plot(Assault~UrbanPop, USArrests, col=grey(0,.5), pch=16,
#    cex=USArrests$Murder/diff(range(USArrests$Murder))*2,
#    main='US Murder arrests (per 100,000)')

# Superior Plot
USArrests$ID <- rownames(USArrests)
fig <- plotly::plot_ly(
  USArrests, x = ~UrbanPop, y = ~Assault,
  text = ~paste('<b>', ID, '</b>',
    "<br>Urban  :", UrbanPop,
    "<br>Assault:", Assault,
    "<br>Murder :", Murder),
  mode='markers',
  type='scatter',
  hoverinfo='text',
  color=~Murder,
  showlegend=F,
  marker=list(
    size=~Murder,
    opacity=0.5,
    showscale=T,  
    colorbar = list(title='Murder Arrests (per 100,000)')))
fig <- plotly::layout(fig,
  title='Crime and Urbanization in America 1975',
  xaxis = list(title = 'Percent of People in an Urban Area'),
  yaxis = list(title = 'Assault Arrests per 100,000 People'))
fig
```

```{=html}
<div class="plotly html-widget html-fill-item-overflow-hidden html-fill-item" id="htmlwidget-1b7934e8482e5d840dc3" style="width:672px;height:480px;"></div>
<script type="application/json" data-for="htmlwidget-1b7934e8482e5d840dc3">{"x":{"visdat":{"446e5c208712":["function () ","plotlyVisDat"]},"cur_data":"446e5c208712","attrs":{"446e5c208712":{"x":{},"y":{},"text":{},"mode":"markers","hoverinfo":"text","showlegend":false,"marker":{"size":{},"opacity":0.5,"showscale":true,"colorbar":{"title":"Murder Arrests (per 100,000)"}},"color":{},"alpha_stroke":1,"sizes":[10,100],"spans":[1,20],"type":"scatter"}},"layout":{"margin":{"b":40,"l":60,"t":25,"r":10},"title":"Crime and Urbanization in America 1975","xaxis":{"domain":[0,1],"automargin":true,"title":"Percent of People in an Urban Area"},"yaxis":{"domain":[0,1],"automargin":true,"title":"Assault Arrests per 100,000 People"},"hovermode":"closest","showlegend":false},"source":"A","config":{"modeBarButtonsToAdd":["hoverclosest","hovercompare"],"showSendToCloud":false},"data":[{"x":[58,48,80,50,91,78,77,72,80,60,83,54,83,65,57,66,52,66,51,67,85,74,66,44,70,53,62,81,56,89,70,86,45,44,75,68,67,72,87,48,45,59,80,80,32,63,73,39,66,60],"y":[236,263,294,190,276,204,110,238,335,211,46,120,249,113,56,115,109,249,83,300,149,255,72,259,178,109,102,252,57,159,285,254,337,45,120,151,159,106,174,279,86,188,201,120,48,156,145,81,53,161],"text":["<b> Alabama <\/b> <br>Urban  : 58 <br>Assault: 236 <br>Murder : 13.2","<b> Alaska <\/b> <br>Urban  : 48 <br>Assault: 263 <br>Murder : 10","<b> Arizona <\/b> <br>Urban  : 80 <br>Assault: 294 <br>Murder : 8.1","<b> Arkansas <\/b> <br>Urban  : 50 <br>Assault: 190 <br>Murder : 8.8","<b> California <\/b> <br>Urban  : 91 <br>Assault: 276 <br>Murder : 9","<b> Colorado <\/b> <br>Urban  : 78 <br>Assault: 204 <br>Murder : 7.9","<b> Connecticut <\/b> <br>Urban  : 77 <br>Assault: 110 <br>Murder : 3.3","<b> Delaware <\/b> <br>Urban  : 72 <br>Assault: 238 <br>Murder : 5.9","<b> Florida <\/b> <br>Urban  : 80 <br>Assault: 335 <br>Murder : 15.4","<b> Georgia <\/b> <br>Urban  : 60 <br>Assault: 211 <br>Murder : 17.4","<b> Hawaii <\/b> <br>Urban  : 83 <br>Assault: 46 <br>Murder : 5.3","<b> Idaho <\/b> <br>Urban  : 54 <br>Assault: 120 <br>Murder : 2.6","<b> Illinois <\/b> <br>Urban  : 83 <br>Assault: 249 <br>Murder : 10.4","<b> Indiana <\/b> <br>Urban  : 65 <br>Assault: 113 <br>Murder : 7.2","<b> Iowa <\/b> <br>Urban  : 57 <br>Assault: 56 <br>Murder : 2.2","<b> Kansas <\/b> <br>Urban  : 66 <br>Assault: 115 <br>Murder : 6","<b> Kentucky <\/b> <br>Urban  : 52 <br>Assault: 109 <br>Murder : 9.7","<b> Louisiana <\/b> <br>Urban  : 66 <br>Assault: 249 <br>Murder : 15.4","<b> Maine <\/b> <br>Urban  : 51 <br>Assault: 83 <br>Murder : 2.1","<b> Maryland <\/b> <br>Urban  : 67 <br>Assault: 300 <br>Murder : 11.3","<b> Massachusetts <\/b> <br>Urban  : 85 <br>Assault: 149 <br>Murder : 4.4","<b> Michigan <\/b> <br>Urban  : 74 <br>Assault: 255 <br>Murder : 12.1","<b> Minnesota <\/b> <br>Urban  : 66 <br>Assault: 72 <br>Murder : 2.7","<b> Mississippi <\/b> <br>Urban  : 44 <br>Assault: 259 <br>Murder : 16.1","<b> Missouri <\/b> <br>Urban  : 70 <br>Assault: 178 <br>Murder : 9","<b> Montana <\/b> <br>Urban  : 53 <br>Assault: 109 <br>Murder : 6","<b> Nebraska <\/b> <br>Urban  : 62 <br>Assault: 102 <br>Murder : 4.3","<b> Nevada <\/b> <br>Urban  : 81 <br>Assault: 252 <br>Murder : 12.2","<b> New Hampshire <\/b> <br>Urban  : 56 <br>Assault: 57 <br>Murder : 2.1","<b> New Jersey <\/b> <br>Urban  : 89 <br>Assault: 159 <br>Murder : 7.4","<b> New Mexico <\/b> <br>Urban  : 70 <br>Assault: 285 <br>Murder : 11.4","<b> New York <\/b> <br>Urban  : 86 <br>Assault: 254 <br>Murder : 11.1","<b> North Carolina <\/b> <br>Urban  : 45 <br>Assault: 337 <br>Murder : 13","<b> North Dakota <\/b> <br>Urban  : 44 <br>Assault: 45 <br>Murder : 0.8","<b> Ohio <\/b> <br>Urban  : 75 <br>Assault: 120 <br>Murder : 7.3","<b> Oklahoma <\/b> <br>Urban  : 68 <br>Assault: 151 <br>Murder : 6.6","<b> Oregon <\/b> <br>Urban  : 67 <br>Assault: 159 <br>Murder : 4.9","<b> Pennsylvania <\/b> <br>Urban  : 72 <br>Assault: 106 <br>Murder : 6.3","<b> Rhode Island <\/b> <br>Urban  : 87 <br>Assault: 174 <br>Murder : 3.4","<b> South Carolina <\/b> <br>Urban  : 48 <br>Assault: 279 <br>Murder : 14.4","<b> South Dakota <\/b> <br>Urban  : 45 <br>Assault: 86 <br>Murder : 3.8","<b> Tennessee <\/b> <br>Urban  : 59 <br>Assault: 188 <br>Murder : 13.2","<b> Texas <\/b> <br>Urban  : 80 <br>Assault: 201 <br>Murder : 12.7","<b> Utah <\/b> <br>Urban  : 80 <br>Assault: 120 <br>Murder : 3.2","<b> Vermont <\/b> <br>Urban  : 32 <br>Assault: 48 <br>Murder : 2.2","<b> Virginia <\/b> <br>Urban  : 63 <br>Assault: 156 <br>Murder : 8.5","<b> Washington <\/b> <br>Urban  : 73 <br>Assault: 145 <br>Murder : 4","<b> West Virginia <\/b> <br>Urban  : 39 <br>Assault: 81 <br>Murder : 5.7","<b> Wisconsin <\/b> <br>Urban  : 66 <br>Assault: 53 <br>Murder : 2.6","<b> Wyoming <\/b> <br>Urban  : 60 <br>Assault: 161 <br>Murder : 6.8"],"mode":"markers","hoverinfo":["text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text"],"showlegend":false,"marker":{"colorbar":{"title":"Murder Arrests (per 100,000)","ticklen":2},"cmin":0.80000000000000004,"cmax":17.399999999999999,"colorscale":[["0","rgba(68,1,84,1)"],["0.0416666666666667","rgba(70,19,97,1)"],["0.0833333333333333","rgba(72,32,111,1)"],["0.125","rgba(71,45,122,1)"],["0.166666666666667","rgba(68,58,128,1)"],["0.208333333333333","rgba(64,70,135,1)"],["0.25","rgba(60,82,138,1)"],["0.291666666666667","rgba(56,93,140,1)"],["0.333333333333333","rgba(49,104,142,1)"],["0.375","rgba(46,114,142,1)"],["0.416666666666667","rgba(42,123,142,1)"],["0.458333333333333","rgba(38,133,141,1)"],["0.5","rgba(37,144,140,1)"],["0.541666666666667","rgba(33,154,138,1)"],["0.583333333333333","rgba(39,164,133,1)"],["0.625","rgba(47,174,127,1)"],["0.666666666666667","rgba(53,183,121,1)"],["0.708333333333333","rgba(79,191,110,1)"],["0.75","rgba(98,199,98,1)"],["0.791666666666667","rgba(119,207,85,1)"],["0.833333333333333","rgba(147,214,70,1)"],["0.875","rgba(172,220,52,1)"],["0.916666666666667","rgba(199,225,42,1)"],["0.958333333333333","rgba(226,228,40,1)"],["1","rgba(253,231,37,1)"]],"showscale":true,"color":[13.199999999999999,10,8.0999999999999996,8.8000000000000007,9,7.9000000000000004,3.2999999999999998,5.9000000000000004,15.4,17.399999999999999,5.2999999999999998,2.6000000000000001,10.4,7.2000000000000002,2.2000000000000002,6,9.6999999999999993,15.4,2.1000000000000001,11.300000000000001,4.4000000000000004,12.1,2.7000000000000002,16.100000000000001,9,6,4.2999999999999998,12.199999999999999,2.1000000000000001,7.4000000000000004,11.4,11.1,13,0.80000000000000004,7.2999999999999998,6.5999999999999996,4.9000000000000004,6.2999999999999998,3.3999999999999999,14.4,3.7999999999999998,13.199999999999999,12.699999999999999,3.2000000000000002,2.2000000000000002,8.5,4,5.7000000000000002,2.6000000000000001,6.7999999999999998],"size":[13.199999999999999,10,8.0999999999999996,8.8000000000000007,9,7.9000000000000004,3.2999999999999998,5.9000000000000004,15.4,17.399999999999999,5.2999999999999998,2.6000000000000001,10.4,7.2000000000000002,2.2000000000000002,6,9.6999999999999993,15.4,2.1000000000000001,11.300000000000001,4.4000000000000004,12.1,2.7000000000000002,16.100000000000001,9,6,4.2999999999999998,12.199999999999999,2.1000000000000001,7.4000000000000004,11.4,11.1,13,0.80000000000000004,7.2999999999999998,6.5999999999999996,4.9000000000000004,6.2999999999999998,3.3999999999999999,14.4,3.7999999999999998,13.199999999999999,12.699999999999999,3.2000000000000002,2.2000000000000002,8.5,4,5.7000000000000002,2.6000000000000001,6.7999999999999998],"opacity":0.5,"line":{"colorbar":{"title":"","ticklen":2},"cmin":0.80000000000000004,"cmax":17.399999999999999,"colorscale":[["0","rgba(68,1,84,1)"],["0.0416666666666667","rgba(70,19,97,1)"],["0.0833333333333333","rgba(72,32,111,1)"],["0.125","rgba(71,45,122,1)"],["0.166666666666667","rgba(68,58,128,1)"],["0.208333333333333","rgba(64,70,135,1)"],["0.25","rgba(60,82,138,1)"],["0.291666666666667","rgba(56,93,140,1)"],["0.333333333333333","rgba(49,104,142,1)"],["0.375","rgba(46,114,142,1)"],["0.416666666666667","rgba(42,123,142,1)"],["0.458333333333333","rgba(38,133,141,1)"],["0.5","rgba(37,144,140,1)"],["0.541666666666667","rgba(33,154,138,1)"],["0.583333333333333","rgba(39,164,133,1)"],["0.625","rgba(47,174,127,1)"],["0.666666666666667","rgba(53,183,121,1)"],["0.708333333333333","rgba(79,191,110,1)"],["0.75","rgba(98,199,98,1)"],["0.791666666666667","rgba(119,207,85,1)"],["0.833333333333333","rgba(147,214,70,1)"],["0.875","rgba(172,220,52,1)"],["0.916666666666667","rgba(199,225,42,1)"],["0.958333333333333","rgba(226,228,40,1)"],["1","rgba(253,231,37,1)"]],"showscale":false,"color":[13.199999999999999,10,8.0999999999999996,8.8000000000000007,9,7.9000000000000004,3.2999999999999998,5.9000000000000004,15.4,17.399999999999999,5.2999999999999998,2.6000000000000001,10.4,7.2000000000000002,2.2000000000000002,6,9.6999999999999993,15.4,2.1000000000000001,11.300000000000001,4.4000000000000004,12.1,2.7000000000000002,16.100000000000001,9,6,4.2999999999999998,12.199999999999999,2.1000000000000001,7.4000000000000004,11.4,11.1,13,0.80000000000000004,7.2999999999999998,6.5999999999999996,4.9000000000000004,6.2999999999999998,3.3999999999999999,14.4,3.7999999999999998,13.199999999999999,12.699999999999999,3.2000000000000002,2.2000000000000002,8.5,4,5.7000000000000002,2.6000000000000001,6.7999999999999998]}},"type":"scatter","xaxis":"x","yaxis":"y","frame":null},{"x":[32,91],"y":[45,337],"type":"scatter","mode":"markers","opacity":0,"hoverinfo":"none","showlegend":false,"marker":{"colorbar":{"title":"Murder","ticklen":2},"cmin":0.80000000000000004,"cmax":17.399999999999999,"colorscale":[["0","rgba(68,1,84,1)"],["0.0416666666666667","rgba(70,19,97,1)"],["0.0833333333333333","rgba(72,32,111,1)"],["0.125","rgba(71,45,122,1)"],["0.166666666666667","rgba(68,58,128,1)"],["0.208333333333333","rgba(64,70,135,1)"],["0.25","rgba(60,82,138,1)"],["0.291666666666667","rgba(56,93,140,1)"],["0.333333333333333","rgba(49,104,142,1)"],["0.375","rgba(46,114,142,1)"],["0.416666666666667","rgba(42,123,142,1)"],["0.458333333333333","rgba(38,133,141,1)"],["0.5","rgba(37,144,140,1)"],["0.541666666666667","rgba(33,154,138,1)"],["0.583333333333333","rgba(39,164,133,1)"],["0.625","rgba(47,174,127,1)"],["0.666666666666667","rgba(53,183,121,1)"],["0.708333333333333","rgba(79,191,110,1)"],["0.75","rgba(98,199,98,1)"],["0.791666666666667","rgba(119,207,85,1)"],["0.833333333333333","rgba(147,214,70,1)"],["0.875","rgba(172,220,52,1)"],["0.916666666666667","rgba(199,225,42,1)"],["0.958333333333333","rgba(226,228,40,1)"],["1","rgba(253,231,37,1)"]],"showscale":true,"color":[0.80000000000000004,17.399999999999999],"line":{"color":"rgba(255,127,14,1)"}},"xaxis":"x","yaxis":"y","frame":null}],"highlight":{"on":"plotly_click","persistent":false,"dynamic":false,"selectize":false,"opacityDim":0.20000000000000001,"selected":{"opacity":1},"debounce":0},"shinyEvents":["plotly_hover","plotly_click","plotly_selected","plotly_relayout","plotly_brushed","plotly_brushing","plotly_clickannotation","plotly_doubleclick","plotly_deselect","plotly_afterplot","plotly_sunburstclick"],"base_url":"https://plot.ly"},"evals":[],"jsHooks":[]}</script>
```

```r
## For further exploratory plotting,
## see https://plotly.com/r/bubble-charts/
```


```r
## Manually Compute
Y <- USArrests[,'Murder']
X <- USArrests[,c('Assault','UrbanPop')]
X <- as.matrix(cbind(1,X))

XtXi <- solve(t(X)%*%X)
Bhat <- XtXi %*% (t(X)%*%Y)
c(Bhat)
```

```
## [1]  3.20715340  0.04390995 -0.04451047
```

```r
## Check
reg <- lm(Murder~Assault+UrbanPop, data=USArrests)
coef(reg)
```

```
## (Intercept)     Assault    UrbanPop 
##  3.20715340  0.04390995 -0.04451047
```

To measure the ``Goodness of fit'', we can compute various sums of squared srrors
$$
R^2 = \frac{RSS}{TSS}=1-\frac{ESS}{TSS}\\
R^2_{\text{adj.}} = 1-\frac{n-1}{n-K}(1-R^2)
$$
With multiple variables, sometimes random data may improve the fit. So we adjust the $R^2$ by the number of covariates $K$.

```r
ksims <- 1:30
for(k in ksims){ 
    USArrests[,paste0('R',k)] <- runif(nrow(USArrests),0,20)
}
reg_sim <- lapply(ksims, function(k){
    rvars <- c('Assault','UrbanPop', paste0('R',1:k))
    rvars2 <- paste0(rvars, collapse='+')
    reg_k <- lm( paste0('Murder~',rvars2), data=USArrests)
})
R2_sim <- sapply(reg_sim, function(reg_k){  summary(reg_k)$r.squared })
R2adj_sim <- sapply(reg_sim, function(reg_k){  summary(reg_k)$adj.r.squared })

plot.new()
plot.window(xlim=c(0,30), ylim=c(0,1))
points(ksims, R2_sim)
points(ksims, R2adj_sim, pch=16)
axis(1)
axis(2)
mtext(expression(R^2),2, line=3)
mtext('Additional Random Covariates', 1, line=3)
legend('topleft', horiz=T,
    legend=c('Undjusted', 'Adjusted'), pch=c(1,16))
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-13-1.png" width="672" />


### Variability Estimates and Hypothesis Tests

We can use the same *data-driven* methods to estimate the variability of the estimated parameters.


```r
## Bootstrap SE's
boots <- 1:399
boot_regs <- lapply(boots, function(b){
    b_id <- sample( nrow(USArrests), replace=T)
    xy_b <- USArrests[b_id,]
    reg_b <- lm(Murder~Assault+UrbanPop, dat=xy_b)
})
boot_coefs <- sapply(boot_regs, coef)
boot_mean <- apply(boot_coefs,1, mean)
boot_se <- apply(boot_coefs,1, sd)
```

Also as before, we can conduct independant hypothesis tests using t-values 
$$\hat{t}_{j} = \frac{\hat{\beta}_j - \beta_{0} }{\hat{\sigma}_{\hat{\beta}_j}}$$
and, under some additional assumptions $\hat{t}_{j} \sim t_{n-K}$. But note that *Hypothesis Testing is not to be done routinely*, and some additional complications arise when examining multiple variables.

We can conduct joint tests, such as whether two coefficients are equal, by looking at the their joint distribution.

```r
fig <- plotly::plot_ly(x=boot_coefs[2,], y=boot_coefs[3,]) 
plotly::add_histogram2d(fig, nbinsx=20, nbinsy=20)
```

```{=html}
<div class="plotly html-widget html-fill-item-overflow-hidden html-fill-item" id="htmlwidget-7dfbde572b7492e7f290" style="width:672px;height:480px;"></div>
<script type="application/json" data-for="htmlwidget-7dfbde572b7492e7f290">{"x":{"visdat":{"446e12a4a165":["function () ","plotlyVisDat"]},"cur_data":"446e12a4a165","attrs":{"446e12a4a165":{"x":[0.040561095499747596,0.041938368187497667,0.048148508148214461,0.034494577915526008,0.045367596479324444,0.034325300687929779,0.043702997183622576,0.055298649389121442,0.046956511259385533,0.043583829156873338,0.045008545240930398,0.042012485920126859,0.042235433336443876,0.04156717438550335,0.041420840817531196,0.045708819044591856,0.039013895102954693,0.03957042688085869,0.039850311411970915,0.048124777324044521,0.04324636260841782,0.039766538402627026,0.048744566513923455,0.04091952117407742,0.042303651286569446,0.043918077113088448,0.045741190619172326,0.0409782875816996,0.045207957190009695,0.044553402436169773,0.039685064182472751,0.038476714975078964,0.039803609069646688,0.040957095345608631,0.047246323626668314,0.042680697623014442,0.044238094765556027,0.04645855759108268,0.039740438258023071,0.039478600842938472,0.049692603203770169,0.041722878023708596,0.054497187566703374,0.044103891354072965,0.052179113906141709,0.044296371117787614,0.052071129169376125,0.044066526876193016,0.044321771238545492,0.043049294018183727,0.042110425409638365,0.041911797636494642,0.03764701235033404,0.041156217201248083,0.039375571213918242,0.040048303163068268,0.043992086347360675,0.04670007103545723,0.046182793952217298,0.052749297829928973,0.047535804044430745,0.038684191555140135,0.041978288575893766,0.040495080184013744,0.038652996282625141,0.040874357247695205,0.045763129528601079,0.05647432386388012,0.044640172617157504,0.041382342141327882,0.036449076757324721,0.059128796902146855,0.044358395217399156,0.0479898505233479,0.042536307391582248,0.036890768816775818,0.045563713836755934,0.045691501096377339,0.049544324299342177,0.044326131417409653,0.037954647275418731,0.045087808340589966,0.039173367060612099,0.051033637512413209,0.045783019407210544,0.041301706784998733,0.044595134361668169,0.048104021543994124,0.03622405273675755,0.045072585907362045,0.044067841702805075,0.039560867364671889,0.047660197178468498,0.037303685332457467,0.038140759274548956,0.044814079008092235,0.044951608060943074,0.044646912784842376,0.047129330208013735,0.043014314824240611,0.03884056289878407,0.04565040472694197,0.039843378766438932,0.043853108860878801,0.040143645858150896,0.037984412031271182,0.044094768669595559,0.050030705773438634,0.045600375207138798,0.041344049308323375,0.044789611232860238,0.044036963391725831,0.038010809015989015,0.045578032495297308,0.047096839443180168,0.046093982453354193,0.044021416348547567,0.041265715253206173,0.049206787475848099,0.042942318907303031,0.042326830595569923,0.049208224506214072,0.05065916219891848,0.040992222898925977,0.04972928008646392,0.041148913445416095,0.033449318759509815,0.038217268821004138,0.042365632786837797,0.062444001555800009,0.04763698817869904,0.043740534448319615,0.040634529221819059,0.047315537037525654,0.039909369313859799,0.041365025621329758,0.037731118804038788,0.041270829431029998,0.03817054710534791,0.038565074847755398,0.040196940018970298,0.042146854461504256,0.04389349451071993,0.049289643487195459,0.049035806196025607,0.048332011429498181,0.052632817134035885,0.048920625027620415,0.043977187836011754,0.040787041125200561,0.048426938738676553,0.046694385673852229,0.038768082623787961,0.040797349369864094,0.039475340880905006,0.053379360599122613,0.046229295027967542,0.041650064791689492,0.047090287473707339,0.041129540903358006,0.043977923703633501,0.038634023970751823,0.036169764956769886,0.043636143265890444,0.040226846010969958,0.039834092859099023,0.051867270884504102,0.042145983281062324,0.040622241556426818,0.042767416944450742,0.037265256144948591,0.039355429442664618,0.03887559099385958,0.037726566650863311,0.057325652873862418,0.040909659242150231,0.041635713447048119,0.04080186715476717,0.047871502774082544,0.044192146064853818,0.051210701177217093,0.043750080234764642,0.047322292991917397,0.041963639884453334,0.039286002949242053,0.043895338953518145,0.042658531678173385,0.04253021796008815,0.040829990440781311,0.043499696521405437,0.045074252636012065,0.043343950975981357,0.049495259945658551,0.042467174550639183,0.038711421590976673,0.042035792316083918,0.041292660457527761,0.047732606803375856,0.04358233285810529,0.043297693782181727,0.050664925703605319,0.044416047526790313,0.040268249091130311,0.039987912657155816,0.038985349846724068,0.048587634882312797,0.045784957309604683,0.046282375155957574,0.036468035366383128,0.045248637453310717,0.045126422546417758,0.047809571451128817,0.035668554433354885,0.045830407806456738,0.039621148189426247,0.044189128579100678,0.046353883513273381,0.03403776986291656,0.041384842609808112,0.046583522088378695,0.04022797162471551,0.046360978551073552,0.04695036598411375,0.045077466670964413,0.052435987997664822,0.040799139514390105,0.049846062947749251,0.03774128911113124,0.054867668563644459,0.039346251747315326,0.043332138473531283,0.038068123006481019,0.053718182347180801,0.04195049696834699,0.046943701556710925,0.049359776877600126,0.039758202182735965,0.038902306750183489,0.044365439130578756,0.046459747367250198,0.045687896730596804,0.042079409279903966,0.04203116141040155,0.047220814743143526,0.049826213728576645,0.042532534067328931,0.04670868995702341,0.044228626351741865,0.038075838360676829,0.038751052478496632,0.0400142565717716,0.043160544582185975,0.033014040813920453,0.042946868541027673,0.040812559910809502,0.056650297093242943,0.039336432540174354,0.04544631801806738,0.054803074556478239,0.04613063711926825,0.050996298590138919,0.042555574617090142,0.047211888366348799,0.038388418697401963,0.040031765286461039,0.051889953025915446,0.038140408528102375,0.047730269842191551,0.055392641561074464,0.043473188458181732,0.039524090875691968,0.042500723679540463,0.032917827920723453,0.042253950416248721,0.04042930690029968,0.046541221957011464,0.043785438994996935,0.03956249169257512,0.049528284438426606,0.037413215504233953,0.049405193575592497,0.038655790866674998,0.037194881553842915,0.045249694766023127,0.040666985198179989,0.037841509427711646,0.050692321362327153,0.04788176605484902,0.040906110335776513,0.045069426764045475,0.042863722747979623,0.046550323342642419,0.043707574009183604,0.044440119404429615,0.042753026973715635,0.042663072653452115,0.046299098307265425,0.043613699870629546,0.048434067462702152,0.039038383475368553,0.043708011781650284,0.045305118060674256,0.048377899426351054,0.046717089686619299,0.044021734764190516,0.042999138964103498,0.041891047690972259,0.040899943908473915,0.044097044499146761,0.042675674059894073,0.046359007252840714,0.042083598097596826,0.042171898339062666,0.036669851873306535,0.042336425663525662,0.049275989504441606,0.045746797647998716,0.039053503179783497,0.042288997479192535,0.044349060033221498,0.037192789523226862,0.036559534230021479,0.041647348459434783,0.039455538697652691,0.045490434076817569,0.047406048783572401,0.035523835478780019,0.049538250958167086,0.051292457978621676,0.042857411985557411,0.043036022751175886,0.050952024491864888,0.04464114040013064,0.040773479067767252,0.044504783538270455,0.043636972637671537,0.041201385074963133,0.038253742160989673,0.043904710361139604,0.04629411535045088,0.043437786112566726,0.038500967603413136,0.043745522705125002,0.03557214107946511,0.056445903507137067,0.04519251300053688,0.050248102292526096,0.047761242669360444,0.041181949015977319,0.038159096221574221,0.04703450071348201,0.038138763334304389,0.048963839971701346,0.049167006513344755,0.055392765094252047,0.03778642920535117,0.05446974074211533,0.047282418764844458,0.043103067952636812,0.045192967635122476,0.041629092119754969,0.038707477709985567,0.038520788959182817,0.044444775593467004,0.038568476015242284,0.040914029210052376,0.042689111222239652,0.040609674703896724,0.051164669528350762,0.044063857173005552,0.044382980713423725,0.041321636619342003,0.043162459005204094,0.051919262594911246,0.039272365507708247,0.035455515130619356,0.046717334718874494,0.046222485559935661,0.03763855107611587,0.04418796241372891,0.04700986406498283,0.046166865661805945,0.044027155337215192,0.050321521842337728,0.038359896883362381,0.039280042425294356,0.047167622766121534,0.039626719836848602,0.053754329439206591,0.043445049924637158,0.04589101429598668,0.040086800180707018,0.047782518077720069,0.041254116965517576,0.04676537777555375,0.036883187777624706,0.039763697635256279,0.0381028280247101,0.040774039299557217],"y":[-0.021486002685721622,-0.0046145257771850988,-0.052484608484121717,-0.0757214017772323,-0.092052157744157176,-0.032878766535674113,-0.050201594198953585,-0.08257691021169758,-0.089381281818677896,-0.08862192930233001,-0.058855503612395464,-0.019562619616540267,-0.031651177561435498,-0.059957931791270305,-0.030299709190241358,-0.043145022504713401,-0.030121603885246703,-0.047722546632326203,-0.015248988108052596,-0.052756081341627674,-0.058492633149643557,-0.058129920755929723,-0.076584307815436486,0.010403700604972033,-0.036001553896935892,-0.057830237069308982,-0.055675397263515503,-0.02796077615365674,-0.047259121099106134,0.0054206701896809184,-0.026825675042174542,-0.059303662175466627,-0.027336201133332749,-0.0088456844283903192,-0.091474714700756757,-0.036137985362677899,-0.022372225597843399,-0.051667327995607318,-0.019899722297873554,-0.015576251340659283,-0.041129037535957612,-0.0092546549075714184,-0.065903649443291037,-0.057388060777814498,-0.092330230594186102,-0.054143284541460737,-0.040096248548594289,-0.029960182930924749,-0.072198449990336214,-0.046579593824521232,-0.041501715183497344,-0.033108498674681311,-0.054829231574690981,-0.027862188144862323,-0.047470374651336376,-0.057562337022018892,-0.05550410422631688,-0.071978763251889677,-0.027252105552402144,-0.061274467150221168,-0.073476911019505292,-0.017721303511039191,-0.00082161265583111554,-0.00050060515201706863,-0.058439375398571636,-0.0064997278717346596,-0.10688714596274393,-0.055114345314348098,-0.076312826525984895,0.012611427104756165,-0.050259263469120262,-0.071752796855790613,-0.06133156340176478,-0.076963784379023015,-0.063290512564663198,-0.0042999665654485748,-0.0958887577306793,-0.012678594672884836,-0.034029641380567202,-0.055363650530823053,-0.037926407098667111,-0.039657599673024957,-0.066598362782386872,-0.060037460473079209,-0.044854428872768637,-0.012073811587926487,-0.021040326550146898,-0.061074764301517669,-0.05505159924679498,-0.031976300546248088,0.0092508114316274398,-0.043215091873383189,-0.046307789061492854,-0.073772822685868961,-0.059246656108934245,-0.025505140701637743,-0.049902397225728867,-0.032317641057144256,-0.066549130559838521,-0.048524462604792054,-0.044605398880632328,-0.0042316526420017563,-0.02229356426638926,-0.054259021032177585,-0.049453786802138439,-0.00071932797947594606,-0.077216239877705914,-0.047010213819939584,-0.093183467724852809,-0.019401973463347513,-0.020998582606223025,-0.043144101754446475,-0.042363701026252427,-0.10443594703331809,-0.032040870068855122,-0.051805500802957039,-0.061807474070957387,-0.069228653936959469,-0.089029366314387404,-0.033401903653154888,-0.04382841573362016,-0.040241090444150578,-0.064393818510792386,0.022656413993686064,-0.072586827089155384,-0.073672143020757239,-0.04442664979461948,-0.028372243536253283,-0.0096582178111410816,-0.09267438012766395,-0.05713289342390749,-0.038020940885945202,-0.018016827064612616,-0.041753509267433209,-0.04538094453238796,-0.040738412613887609,-0.077898052513242888,0.0097231617291171635,-0.045926669694083731,-0.017735301706025625,-0.036339119862559617,-0.04027075903897024,-0.061058248758896684,-0.087388855682227401,-0.059877386528863825,-0.077132438069174691,-0.10904666305104288,-0.047101387763360959,-0.026353753516858692,-0.00039188959038800181,-0.050360657963831185,-0.057671952674839738,-0.031395397916217364,-0.013425214049105129,-0.035856385471272879,-0.076045464832126028,-0.051990318976964434,-0.073552393745196329,-0.056182721136563384,-0.020199234431741292,-0.044326055621239847,-0.057846937068652876,-0.057385057640505117,-0.05851276511385417,-0.038837814416191982,-0.048049415892477486,-0.063026424009048218,-0.023659950687029137,0.014437860641145066,-0.059926134289448797,-0.010193469206754945,-0.038289802104416001,-0.0084134315064559005,-0.025037618804470991,-0.07568483692857815,-0.012766576601277132,-0.068531888499429428,-0.064340043595571259,-0.051681985224014605,-0.051930631601982906,-0.11855467947935414,-0.0098181957123330971,-0.070017644122193912,-0.045345950082350726,-0.032422965316338523,-0.057382545748661945,-0.035444817344547089,-0.021278403049395839,-0.05708217662938616,-0.043905879885943376,-0.056161969366722166,-0.070714198751281057,-0.093862485068617274,0.00065153711552640256,-0.038411640026049527,-0.044703146885146441,-0.024889176381820467,-0.071543565394628611,-0.054669645122161943,-0.03463683501244319,-0.059201433824501236,-0.052557249118388827,-0.0040251281952873811,-0.061674835802329749,-0.063749240401064722,-0.061790670864625752,-0.034351570338750276,-0.023749716861129973,-0.038328339168710576,-0.070033979839366614,-0.032534890809814407,-0.022479368132326222,-0.013170633708743747,-0.049726690663763326,-0.021480517200235701,-0.079494494332523744,-0.031458964287383699,-0.058995009880354943,-0.047561488433620916,-0.067460728667934039,-0.057757894479373538,-0.059445846156961128,-0.045348644669638942,-0.034475559954447198,-0.041747561824040644,-0.064808134281510124,-0.008656302222233056,-0.028063291633010475,-0.064905238109399216,-0.00063648871308099588,-0.040906308149708095,0.012082947482950364,-0.058208942334143227,-0.060450084754330134,-0.068834278400918547,-0.031091215859051901,-0.087156058563847519,-0.071495674568684275,-0.096704355245538137,-0.030209001361722547,-0.013857117139822029,-0.072612545710726686,-0.075411572387071149,-0.053348418783891696,-0.0479829730390759,-0.05419030960232521,-0.017433992856125898,-0.050058575036122412,-0.053013900139284309,-0.015933201428897096,-0.08269216053563884,-0.045732610182499127,-0.019324663667524205,-0.033635615190479431,-0.032013464043243553,-0.096872902934243943,-0.029687980208331615,-0.049635528436821716,-0.061472394501421466,-0.06829560472934193,-0.020287614756463797,-0.029325632876427865,-0.017603400183123889,0.0031098297692312626,-0.043493551169570689,-0.10143048634296969,0.016312274617040701,-0.068410580558066675,-0.07167113775702931,0.028409170174288238,-0.054689307218803614,-0.075396781181817502,-0.040139957856556122,-0.059727894663603891,0.004271814949164102,-0.048507307818721743,0.0024898619041638479,-0.029042825706412492,-0.021331971722211299,-0.047369650896170276,-0.067405029190581778,-0.06048248058820653,-0.022100418064635207,-0.047500751948522602,-0.060904533162084287,-0.016458525152865822,-0.072168008560544394,-0.071426016136504303,-0.017224153457132338,-0.070852685976639518,-0.061197834460762872,-0.050552119805877552,-0.059866739727402793,-0.074098716038111412,-0.030084437342325184,-0.034322779706077514,-0.05405761082013389,-0.016344414863769998,-0.052637300894317673,-0.022110563005362845,-0.010951342825572958,-0.0037841135746985838,-0.016846039511366553,-0.021788034142027419,-0.058490475405749066,-0.011472086843523337,-0.04190918621690521,-0.052777516936142105,-0.038954638511748074,-0.061392503664964224,-0.049022454924485183,-0.021369229108847622,-0.034500871780870385,-0.0071058472517475622,-0.035624953396375461,-0.030607503850735907,-0.060321306677979525,-0.058117892292428211,0.0084089984455226925,-0.035652827244573325,-0.0079745826625333277,-0.042782444243836988,-0.035221172177004996,-0.062300603181362657,-0.040297213490050547,-0.086389083348276163,-0.027217612000244262,-0.074933919848567579,-0.11186664381984357,-0.022104293535204728,-0.03620270282887969,-0.059591531282641087,-0.090781149437518638,-0.018476546352606055,-0.00081330614103075074,-0.0066673566530856153,-0.024850964147536576,-0.020640947830949906,-0.040038379080083002,-0.068770288487094128,-0.084594830304914256,-0.034867429619441975,-0.026573716613931538,-0.04149858146598534,-0.089829443395656378,-0.062313137858433239,-0.062579406266360965,-0.024882543843922505,-0.0030165169329302143,-0.015134040884833956,-0.046293950857568801,4.8894355373005596e-05,-0.020900735842969746,-0.014591094229030349,-0.10646420779056515,-0.034556613829021844,-0.046193848115282495,-0.048594337487652746,-0.063054480025119375,-0.063164579024411735,-0.05690550046138361,-0.033860034601355574,0.0089109151847340824,-0.047770427627076291,-0.04058386724874824,-0.044808436765296847,-0.086587549913542505,-0.044514211680204689,-0.091505612967161809,-0.0428115235182598,-0.039925430656736031,-0.043251084271121711,-0.038561785234047401,-0.051507833823042207,-0.064129410552229912,-0.047157124354832075,-0.066867311687074965,-0.03942624026848654,-0.051317814150660057,-0.056582362605509778,-0.055702363450034757,-0.079430386863231922,-0.038613613393028406,-0.097634032328018802,-0.049770422794154348,-0.013009427561970167,-0.05756768866356346,-0.027788792231603247,-0.071915097494820057,-0.0481599237098609,-0.050194952681045076,-0.0052815772357259691,-0.061005780167132574,-0.026826036777999607,-0.062131625017071757,-0.035070006401444462,-0.011433234695490388,-0.058041514921918502,-0.03636267844709961],"alpha_stroke":1,"sizes":[10,100],"spans":[1,20],"type":"histogram2d","nbinsx":20,"nbinsy":20,"inherit":true}},"layout":{"margin":{"b":40,"l":60,"t":25,"r":10},"xaxis":{"domain":[0,1],"automargin":true,"title":[]},"yaxis":{"domain":[0,1],"automargin":true,"title":[]},"hovermode":"closest","showlegend":false,"legend":{"yanchor":"top","y":0.5}},"source":"A","config":{"modeBarButtonsToAdd":["hoverclosest","hovercompare"],"showSendToCloud":false},"data":[{"colorbar":{"title":"","ticklen":2,"len":0.5,"lenmode":"fraction","y":1,"yanchor":"top"},"colorscale":[["0","rgba(68,1,84,1)"],["0.0416666666666667","rgba(70,19,97,1)"],["0.0833333333333333","rgba(72,32,111,1)"],["0.125","rgba(71,45,122,1)"],["0.166666666666667","rgba(68,58,128,1)"],["0.208333333333333","rgba(64,70,135,1)"],["0.25","rgba(60,82,138,1)"],["0.291666666666667","rgba(56,93,140,1)"],["0.333333333333333","rgba(49,104,142,1)"],["0.375","rgba(46,114,142,1)"],["0.416666666666667","rgba(42,123,142,1)"],["0.458333333333333","rgba(38,133,141,1)"],["0.5","rgba(37,144,140,1)"],["0.541666666666667","rgba(33,154,138,1)"],["0.583333333333333","rgba(39,164,133,1)"],["0.625","rgba(47,174,127,1)"],["0.666666666666667","rgba(53,183,121,1)"],["0.708333333333333","rgba(79,191,110,1)"],["0.75","rgba(98,199,98,1)"],["0.791666666666667","rgba(119,207,85,1)"],["0.833333333333333","rgba(147,214,70,1)"],["0.875","rgba(172,220,52,1)"],["0.916666666666667","rgba(199,225,42,1)"],["0.958333333333333","rgba(226,228,40,1)"],["1","rgba(253,231,37,1)"]],"showscale":true,"x":[0.040561095499747596,0.041938368187497667,0.048148508148214461,0.034494577915526008,0.045367596479324444,0.034325300687929779,0.043702997183622576,0.055298649389121442,0.046956511259385533,0.043583829156873338,0.045008545240930398,0.042012485920126859,0.042235433336443876,0.04156717438550335,0.041420840817531196,0.045708819044591856,0.039013895102954693,0.03957042688085869,0.039850311411970915,0.048124777324044521,0.04324636260841782,0.039766538402627026,0.048744566513923455,0.04091952117407742,0.042303651286569446,0.043918077113088448,0.045741190619172326,0.0409782875816996,0.045207957190009695,0.044553402436169773,0.039685064182472751,0.038476714975078964,0.039803609069646688,0.040957095345608631,0.047246323626668314,0.042680697623014442,0.044238094765556027,0.04645855759108268,0.039740438258023071,0.039478600842938472,0.049692603203770169,0.041722878023708596,0.054497187566703374,0.044103891354072965,0.052179113906141709,0.044296371117787614,0.052071129169376125,0.044066526876193016,0.044321771238545492,0.043049294018183727,0.042110425409638365,0.041911797636494642,0.03764701235033404,0.041156217201248083,0.039375571213918242,0.040048303163068268,0.043992086347360675,0.04670007103545723,0.046182793952217298,0.052749297829928973,0.047535804044430745,0.038684191555140135,0.041978288575893766,0.040495080184013744,0.038652996282625141,0.040874357247695205,0.045763129528601079,0.05647432386388012,0.044640172617157504,0.041382342141327882,0.036449076757324721,0.059128796902146855,0.044358395217399156,0.0479898505233479,0.042536307391582248,0.036890768816775818,0.045563713836755934,0.045691501096377339,0.049544324299342177,0.044326131417409653,0.037954647275418731,0.045087808340589966,0.039173367060612099,0.051033637512413209,0.045783019407210544,0.041301706784998733,0.044595134361668169,0.048104021543994124,0.03622405273675755,0.045072585907362045,0.044067841702805075,0.039560867364671889,0.047660197178468498,0.037303685332457467,0.038140759274548956,0.044814079008092235,0.044951608060943074,0.044646912784842376,0.047129330208013735,0.043014314824240611,0.03884056289878407,0.04565040472694197,0.039843378766438932,0.043853108860878801,0.040143645858150896,0.037984412031271182,0.044094768669595559,0.050030705773438634,0.045600375207138798,0.041344049308323375,0.044789611232860238,0.044036963391725831,0.038010809015989015,0.045578032495297308,0.047096839443180168,0.046093982453354193,0.044021416348547567,0.041265715253206173,0.049206787475848099,0.042942318907303031,0.042326830595569923,0.049208224506214072,0.05065916219891848,0.040992222898925977,0.04972928008646392,0.041148913445416095,0.033449318759509815,0.038217268821004138,0.042365632786837797,0.062444001555800009,0.04763698817869904,0.043740534448319615,0.040634529221819059,0.047315537037525654,0.039909369313859799,0.041365025621329758,0.037731118804038788,0.041270829431029998,0.03817054710534791,0.038565074847755398,0.040196940018970298,0.042146854461504256,0.04389349451071993,0.049289643487195459,0.049035806196025607,0.048332011429498181,0.052632817134035885,0.048920625027620415,0.043977187836011754,0.040787041125200561,0.048426938738676553,0.046694385673852229,0.038768082623787961,0.040797349369864094,0.039475340880905006,0.053379360599122613,0.046229295027967542,0.041650064791689492,0.047090287473707339,0.041129540903358006,0.043977923703633501,0.038634023970751823,0.036169764956769886,0.043636143265890444,0.040226846010969958,0.039834092859099023,0.051867270884504102,0.042145983281062324,0.040622241556426818,0.042767416944450742,0.037265256144948591,0.039355429442664618,0.03887559099385958,0.037726566650863311,0.057325652873862418,0.040909659242150231,0.041635713447048119,0.04080186715476717,0.047871502774082544,0.044192146064853818,0.051210701177217093,0.043750080234764642,0.047322292991917397,0.041963639884453334,0.039286002949242053,0.043895338953518145,0.042658531678173385,0.04253021796008815,0.040829990440781311,0.043499696521405437,0.045074252636012065,0.043343950975981357,0.049495259945658551,0.042467174550639183,0.038711421590976673,0.042035792316083918,0.041292660457527761,0.047732606803375856,0.04358233285810529,0.043297693782181727,0.050664925703605319,0.044416047526790313,0.040268249091130311,0.039987912657155816,0.038985349846724068,0.048587634882312797,0.045784957309604683,0.046282375155957574,0.036468035366383128,0.045248637453310717,0.045126422546417758,0.047809571451128817,0.035668554433354885,0.045830407806456738,0.039621148189426247,0.044189128579100678,0.046353883513273381,0.03403776986291656,0.041384842609808112,0.046583522088378695,0.04022797162471551,0.046360978551073552,0.04695036598411375,0.045077466670964413,0.052435987997664822,0.040799139514390105,0.049846062947749251,0.03774128911113124,0.054867668563644459,0.039346251747315326,0.043332138473531283,0.038068123006481019,0.053718182347180801,0.04195049696834699,0.046943701556710925,0.049359776877600126,0.039758202182735965,0.038902306750183489,0.044365439130578756,0.046459747367250198,0.045687896730596804,0.042079409279903966,0.04203116141040155,0.047220814743143526,0.049826213728576645,0.042532534067328931,0.04670868995702341,0.044228626351741865,0.038075838360676829,0.038751052478496632,0.0400142565717716,0.043160544582185975,0.033014040813920453,0.042946868541027673,0.040812559910809502,0.056650297093242943,0.039336432540174354,0.04544631801806738,0.054803074556478239,0.04613063711926825,0.050996298590138919,0.042555574617090142,0.047211888366348799,0.038388418697401963,0.040031765286461039,0.051889953025915446,0.038140408528102375,0.047730269842191551,0.055392641561074464,0.043473188458181732,0.039524090875691968,0.042500723679540463,0.032917827920723453,0.042253950416248721,0.04042930690029968,0.046541221957011464,0.043785438994996935,0.03956249169257512,0.049528284438426606,0.037413215504233953,0.049405193575592497,0.038655790866674998,0.037194881553842915,0.045249694766023127,0.040666985198179989,0.037841509427711646,0.050692321362327153,0.04788176605484902,0.040906110335776513,0.045069426764045475,0.042863722747979623,0.046550323342642419,0.043707574009183604,0.044440119404429615,0.042753026973715635,0.042663072653452115,0.046299098307265425,0.043613699870629546,0.048434067462702152,0.039038383475368553,0.043708011781650284,0.045305118060674256,0.048377899426351054,0.046717089686619299,0.044021734764190516,0.042999138964103498,0.041891047690972259,0.040899943908473915,0.044097044499146761,0.042675674059894073,0.046359007252840714,0.042083598097596826,0.042171898339062666,0.036669851873306535,0.042336425663525662,0.049275989504441606,0.045746797647998716,0.039053503179783497,0.042288997479192535,0.044349060033221498,0.037192789523226862,0.036559534230021479,0.041647348459434783,0.039455538697652691,0.045490434076817569,0.047406048783572401,0.035523835478780019,0.049538250958167086,0.051292457978621676,0.042857411985557411,0.043036022751175886,0.050952024491864888,0.04464114040013064,0.040773479067767252,0.044504783538270455,0.043636972637671537,0.041201385074963133,0.038253742160989673,0.043904710361139604,0.04629411535045088,0.043437786112566726,0.038500967603413136,0.043745522705125002,0.03557214107946511,0.056445903507137067,0.04519251300053688,0.050248102292526096,0.047761242669360444,0.041181949015977319,0.038159096221574221,0.04703450071348201,0.038138763334304389,0.048963839971701346,0.049167006513344755,0.055392765094252047,0.03778642920535117,0.05446974074211533,0.047282418764844458,0.043103067952636812,0.045192967635122476,0.041629092119754969,0.038707477709985567,0.038520788959182817,0.044444775593467004,0.038568476015242284,0.040914029210052376,0.042689111222239652,0.040609674703896724,0.051164669528350762,0.044063857173005552,0.044382980713423725,0.041321636619342003,0.043162459005204094,0.051919262594911246,0.039272365507708247,0.035455515130619356,0.046717334718874494,0.046222485559935661,0.03763855107611587,0.04418796241372891,0.04700986406498283,0.046166865661805945,0.044027155337215192,0.050321521842337728,0.038359896883362381,0.039280042425294356,0.047167622766121534,0.039626719836848602,0.053754329439206591,0.043445049924637158,0.04589101429598668,0.040086800180707018,0.047782518077720069,0.041254116965517576,0.04676537777555375,0.036883187777624706,0.039763697635256279,0.0381028280247101,0.040774039299557217],"y":[-0.021486002685721622,-0.0046145257771850988,-0.052484608484121717,-0.0757214017772323,-0.092052157744157176,-0.032878766535674113,-0.050201594198953585,-0.08257691021169758,-0.089381281818677896,-0.08862192930233001,-0.058855503612395464,-0.019562619616540267,-0.031651177561435498,-0.059957931791270305,-0.030299709190241358,-0.043145022504713401,-0.030121603885246703,-0.047722546632326203,-0.015248988108052596,-0.052756081341627674,-0.058492633149643557,-0.058129920755929723,-0.076584307815436486,0.010403700604972033,-0.036001553896935892,-0.057830237069308982,-0.055675397263515503,-0.02796077615365674,-0.047259121099106134,0.0054206701896809184,-0.026825675042174542,-0.059303662175466627,-0.027336201133332749,-0.0088456844283903192,-0.091474714700756757,-0.036137985362677899,-0.022372225597843399,-0.051667327995607318,-0.019899722297873554,-0.015576251340659283,-0.041129037535957612,-0.0092546549075714184,-0.065903649443291037,-0.057388060777814498,-0.092330230594186102,-0.054143284541460737,-0.040096248548594289,-0.029960182930924749,-0.072198449990336214,-0.046579593824521232,-0.041501715183497344,-0.033108498674681311,-0.054829231574690981,-0.027862188144862323,-0.047470374651336376,-0.057562337022018892,-0.05550410422631688,-0.071978763251889677,-0.027252105552402144,-0.061274467150221168,-0.073476911019505292,-0.017721303511039191,-0.00082161265583111554,-0.00050060515201706863,-0.058439375398571636,-0.0064997278717346596,-0.10688714596274393,-0.055114345314348098,-0.076312826525984895,0.012611427104756165,-0.050259263469120262,-0.071752796855790613,-0.06133156340176478,-0.076963784379023015,-0.063290512564663198,-0.0042999665654485748,-0.0958887577306793,-0.012678594672884836,-0.034029641380567202,-0.055363650530823053,-0.037926407098667111,-0.039657599673024957,-0.066598362782386872,-0.060037460473079209,-0.044854428872768637,-0.012073811587926487,-0.021040326550146898,-0.061074764301517669,-0.05505159924679498,-0.031976300546248088,0.0092508114316274398,-0.043215091873383189,-0.046307789061492854,-0.073772822685868961,-0.059246656108934245,-0.025505140701637743,-0.049902397225728867,-0.032317641057144256,-0.066549130559838521,-0.048524462604792054,-0.044605398880632328,-0.0042316526420017563,-0.02229356426638926,-0.054259021032177585,-0.049453786802138439,-0.00071932797947594606,-0.077216239877705914,-0.047010213819939584,-0.093183467724852809,-0.019401973463347513,-0.020998582606223025,-0.043144101754446475,-0.042363701026252427,-0.10443594703331809,-0.032040870068855122,-0.051805500802957039,-0.061807474070957387,-0.069228653936959469,-0.089029366314387404,-0.033401903653154888,-0.04382841573362016,-0.040241090444150578,-0.064393818510792386,0.022656413993686064,-0.072586827089155384,-0.073672143020757239,-0.04442664979461948,-0.028372243536253283,-0.0096582178111410816,-0.09267438012766395,-0.05713289342390749,-0.038020940885945202,-0.018016827064612616,-0.041753509267433209,-0.04538094453238796,-0.040738412613887609,-0.077898052513242888,0.0097231617291171635,-0.045926669694083731,-0.017735301706025625,-0.036339119862559617,-0.04027075903897024,-0.061058248758896684,-0.087388855682227401,-0.059877386528863825,-0.077132438069174691,-0.10904666305104288,-0.047101387763360959,-0.026353753516858692,-0.00039188959038800181,-0.050360657963831185,-0.057671952674839738,-0.031395397916217364,-0.013425214049105129,-0.035856385471272879,-0.076045464832126028,-0.051990318976964434,-0.073552393745196329,-0.056182721136563384,-0.020199234431741292,-0.044326055621239847,-0.057846937068652876,-0.057385057640505117,-0.05851276511385417,-0.038837814416191982,-0.048049415892477486,-0.063026424009048218,-0.023659950687029137,0.014437860641145066,-0.059926134289448797,-0.010193469206754945,-0.038289802104416001,-0.0084134315064559005,-0.025037618804470991,-0.07568483692857815,-0.012766576601277132,-0.068531888499429428,-0.064340043595571259,-0.051681985224014605,-0.051930631601982906,-0.11855467947935414,-0.0098181957123330971,-0.070017644122193912,-0.045345950082350726,-0.032422965316338523,-0.057382545748661945,-0.035444817344547089,-0.021278403049395839,-0.05708217662938616,-0.043905879885943376,-0.056161969366722166,-0.070714198751281057,-0.093862485068617274,0.00065153711552640256,-0.038411640026049527,-0.044703146885146441,-0.024889176381820467,-0.071543565394628611,-0.054669645122161943,-0.03463683501244319,-0.059201433824501236,-0.052557249118388827,-0.0040251281952873811,-0.061674835802329749,-0.063749240401064722,-0.061790670864625752,-0.034351570338750276,-0.023749716861129973,-0.038328339168710576,-0.070033979839366614,-0.032534890809814407,-0.022479368132326222,-0.013170633708743747,-0.049726690663763326,-0.021480517200235701,-0.079494494332523744,-0.031458964287383699,-0.058995009880354943,-0.047561488433620916,-0.067460728667934039,-0.057757894479373538,-0.059445846156961128,-0.045348644669638942,-0.034475559954447198,-0.041747561824040644,-0.064808134281510124,-0.008656302222233056,-0.028063291633010475,-0.064905238109399216,-0.00063648871308099588,-0.040906308149708095,0.012082947482950364,-0.058208942334143227,-0.060450084754330134,-0.068834278400918547,-0.031091215859051901,-0.087156058563847519,-0.071495674568684275,-0.096704355245538137,-0.030209001361722547,-0.013857117139822029,-0.072612545710726686,-0.075411572387071149,-0.053348418783891696,-0.0479829730390759,-0.05419030960232521,-0.017433992856125898,-0.050058575036122412,-0.053013900139284309,-0.015933201428897096,-0.08269216053563884,-0.045732610182499127,-0.019324663667524205,-0.033635615190479431,-0.032013464043243553,-0.096872902934243943,-0.029687980208331615,-0.049635528436821716,-0.061472394501421466,-0.06829560472934193,-0.020287614756463797,-0.029325632876427865,-0.017603400183123889,0.0031098297692312626,-0.043493551169570689,-0.10143048634296969,0.016312274617040701,-0.068410580558066675,-0.07167113775702931,0.028409170174288238,-0.054689307218803614,-0.075396781181817502,-0.040139957856556122,-0.059727894663603891,0.004271814949164102,-0.048507307818721743,0.0024898619041638479,-0.029042825706412492,-0.021331971722211299,-0.047369650896170276,-0.067405029190581778,-0.06048248058820653,-0.022100418064635207,-0.047500751948522602,-0.060904533162084287,-0.016458525152865822,-0.072168008560544394,-0.071426016136504303,-0.017224153457132338,-0.070852685976639518,-0.061197834460762872,-0.050552119805877552,-0.059866739727402793,-0.074098716038111412,-0.030084437342325184,-0.034322779706077514,-0.05405761082013389,-0.016344414863769998,-0.052637300894317673,-0.022110563005362845,-0.010951342825572958,-0.0037841135746985838,-0.016846039511366553,-0.021788034142027419,-0.058490475405749066,-0.011472086843523337,-0.04190918621690521,-0.052777516936142105,-0.038954638511748074,-0.061392503664964224,-0.049022454924485183,-0.021369229108847622,-0.034500871780870385,-0.0071058472517475622,-0.035624953396375461,-0.030607503850735907,-0.060321306677979525,-0.058117892292428211,0.0084089984455226925,-0.035652827244573325,-0.0079745826625333277,-0.042782444243836988,-0.035221172177004996,-0.062300603181362657,-0.040297213490050547,-0.086389083348276163,-0.027217612000244262,-0.074933919848567579,-0.11186664381984357,-0.022104293535204728,-0.03620270282887969,-0.059591531282641087,-0.090781149437518638,-0.018476546352606055,-0.00081330614103075074,-0.0066673566530856153,-0.024850964147536576,-0.020640947830949906,-0.040038379080083002,-0.068770288487094128,-0.084594830304914256,-0.034867429619441975,-0.026573716613931538,-0.04149858146598534,-0.089829443395656378,-0.062313137858433239,-0.062579406266360965,-0.024882543843922505,-0.0030165169329302143,-0.015134040884833956,-0.046293950857568801,4.8894355373005596e-05,-0.020900735842969746,-0.014591094229030349,-0.10646420779056515,-0.034556613829021844,-0.046193848115282495,-0.048594337487652746,-0.063054480025119375,-0.063164579024411735,-0.05690550046138361,-0.033860034601355574,0.0089109151847340824,-0.047770427627076291,-0.04058386724874824,-0.044808436765296847,-0.086587549913542505,-0.044514211680204689,-0.091505612967161809,-0.0428115235182598,-0.039925430656736031,-0.043251084271121711,-0.038561785234047401,-0.051507833823042207,-0.064129410552229912,-0.047157124354832075,-0.066867311687074965,-0.03942624026848654,-0.051317814150660057,-0.056582362605509778,-0.055702363450034757,-0.079430386863231922,-0.038613613393028406,-0.097634032328018802,-0.049770422794154348,-0.013009427561970167,-0.05756768866356346,-0.027788792231603247,-0.071915097494820057,-0.0481599237098609,-0.050194952681045076,-0.0052815772357259691,-0.061005780167132574,-0.026826036777999607,-0.062131625017071757,-0.035070006401444462,-0.011433234695490388,-0.058041514921918502,-0.03636267844709961],"type":"histogram2d","nbinsx":20,"nbinsy":20,"marker":{"line":{"color":"rgba(31,119,180,1)"}},"xaxis":"x","yaxis":"y","frame":null}],"highlight":{"on":"plotly_click","persistent":false,"dynamic":false,"selectize":false,"opacityDim":0.20000000000000001,"selected":{"opacity":1},"debounce":0},"shinyEvents":["plotly_hover","plotly_click","plotly_selected","plotly_relayout","plotly_brushed","plotly_brushing","plotly_clickannotation","plotly_doubleclick","plotly_deselect","plotly_afterplot","plotly_sunburstclick"],"base_url":"https://plot.ly"},"evals":[],"jsHooks":[]}</script>
```

```r
## plotly::add_histogram2dcontour(fig)
## fig <- layout(fig,
##    yaxis = list(title=expression(beta[3])),
##    xaxis = list(title=expression(beta[2])))
```


```r
## fBjoint <- ks::histde( t(boot_coefs[2:3,]))
## ks::plot(fBjoint, xlab=expression(beta[2]), ylab=expression(beta[3]))
```

We can use an $F$ test for $q$ hypotheses;
$$
\hat{F}_{q} = \frac{(ESS_{restricted}-ESS_{unrestricted})/q}{ESS_{unrestricted}/(n-K)},
$$
and $\hat{F}$ can be written in terms of unrestricted and restricted $R^2$. Under some additional assumptions $\hat{F}_{q}  \sim F_{q,n-K}$. For some inuition, see how the $R^2$ statistic varies with bootstrap samples. Then compute a null $R^2$ distribution by randomly reshuffling the outcomes, and compare that to the observed $R^2$.

```r
## Bootstrap Distribution for R2
boot_R2s <- sapply(boot_regs, function(reg_b){
    summary(reg_b)$r.squared
})
hist(boot_R2s, breaks=25, main='', xlab=expression(R[b]^2), xlim=c(0,1))
abline(v=summary(reg)$r.squared, col="red", lwd=2)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-17-1.png" width="672" />

```r
## NULL Bootstrap Distribution for R2 ???
```



## Coefficient Interpretation

Notice that we have gotten pretty far without actually trying to meaningfully interpret regression coefficients. That is because the above procedure will always give us number, regardless as to whether the true data generating process is linear or not. So, to be cautious, we have been interpretting the regression outputs while being agnostic as to how the data are generated. We now consider a special situation where we know the data are generated according to a linear process and are only uncertain about the parameter values.

*If* the data generating process is 
$$
y=X\beta + \epsilon\\
\mathbb{E}[\epsilon | X]=0,
$$
then we have a famous result that lets us attach a simple interpretation of OLS coefficients as unbiased estimates of the effect of X:
$$
\hat{\beta} = (X'X)^{-1}X'y = (X'X)^{-1}X'(X\beta + \epsilon) = \beta + (X'X)^{-1}X'\epsilon\\
\mathbb{E}\left[ \hat{\beta} \right] = \mathbb{E}\left[ (X'X)^{-1}X'y \right] = \beta + (X'X)^{-1}\mathbb{E}\left[ X'\epsilon \right] = \beta
$$


Generate a simulated dataset with 30 observations and two exogenous variables. Assume the following relationship: $y_{i} = \beta_0 + \beta_1 x_{1,i} + \beta_2 x_{2,i} + \epsilon_i$ where the variables and the error term are realizations of the following data generating processes (DGP):

```r
N <- 30
B <- c(10, 2, -1)

x1 <- runif(N, 0, 5)
x2 <- rbinom(N,1,.7)
X <- cbind(1,x1,x2)
e <- rnorm(N,0,3)
Y <- X%*%B + e
dat <- data.frame(Y,X)
coef(lm(Y~x1+x2, data=dat))
```

```
## (Intercept)          x1          x2 
##   11.992660    1.855650   -1.566301
```

Simulate the distribution of coefficients under a correctly specified model. Interpret the average.

```r
N <- 30
B <- c(10, 2, -1)

Coefs <- sapply(1:400, function(sim){
    x1 <- runif(N, 0, 5)
    x2 <- rbinom(N,1,.7)
    X <- cbind(1,x1,x2)
    e <- rnorm(N,0,3)
    Y <- X%*%B + e
    dat <- data.frame(Y,x1,x2)
    coef(lm(Y~x1+x2, data=dat))
})

par(mfrow=c(1,2))
for(i in 2:3){
    hist(Coefs[i,], xlab=bquote(beta[.(i)]), main='')
    abline(v=mean(Coefs[i,]), col=1, lty=2)
    abline(v=B[i], col=2)
}
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-19-1.png" width="672" />


Many economic phenomena are nonlinear, even when including potential transforms of $Y$ and $X$. Sometimes the OLS model may still be a good or even great approximation (how good depends on the research question). In any case, you are safe to interpret your OLS coefficients as "conditional correlations". For example, examine the distribution of coefficients under this mispecified model. Interpret the average.

```r
N <- 30

Coefs <- sapply(1:600, function(sim){
    x1 <- runif(N, 0, 5)
    x2 <- rbinom(N,1,.7)
    e <- rnorm(N,0,3)
    Y <- 10*x2 + 2*log(x1)^x2 + e
    dat <- data.frame(Y,x1,x2)
    coef(lm(Y~x1+x2, data=dat))
})

par(mfrow=c(1,2))
for(i in 2:3){
    hist(Coefs[i,],  xlab=bquote(beta[.(i)]), main='')
    abline(v=mean(Coefs[i,]), col=1, lty=2)
}
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-20-1.png" width="672" />

## Factor Variables

So far, we have discussed cardinal data where the difference between units always means the same thing: e.g., $4-3=2-1$. There are also factor variables

* Ordered: refers to Ordinal data. The difference between units means something, but not always the same thing. For example, $4th - 3rd \neq 2nd - 1st$.
* Unordered: refers to Categorical data. The difference between units is meaningless. For example, $B-A=?$


To analyze either factor, we often convert them into indicator variables or dummies; $D_{c}=\mathbf{1}( Factor = c)$. One common case is if you have observations of individuals over time periods, then you may have two factor variables. An unordered factor that indicates who an individual is; for example $D_{i}=\mathbf{1}( Individual = i)$, and an order factor that indicates the time period; for example $D_{t}=\mathbf{1}( Time \in [month~ t, month~ t+1) )$. There are many other cases you see factor variables, including spatial ID's in purely cross sectional data.

Be careful not to handle categorical data as if they were cardinal. E.g., generate city data with Leipzig=1, Lausanne=2, LosAngeles=3, ... and then include city as if it were a cardinal number (that's a big no-no). The same applied to ordinal data; PopulationLeipzig=2, PopulationLausanne=3, PopulationLosAngeles=1.  


```r
N <- 1000
x <- runif(N,3,8)
e <- rnorm(N,0,0.4)
fo <- factor(rbinom(N,4,.5), ordered=T)
fu <- factor(rep(c('A','B'),N/2), ordered=F)
dA <- 1*(fu=='A')
y <- (2^as.integer(fo)*dA )*sqrt(x)+ 2*as.integer(fo)*e
dat_f <- data.frame(y,x,fo,fu)
```


With factors, you can still include them in the design matrix of an OLS regression
$$
y_{it} = x_{it} \beta_{x} + d_{c}\beta_{c}
$$
When, as commonly done, the factors are modeled as being additively seperable, they are modelled as either "fixed" or "random" effects.

Simply including the factors into the OLS regression yields a "dummy variable" fixed effects estimator.

```r
fe_reg0 <- lm(y~x+fo+fu, dat_f)
summary(fe_reg0)
```

```
## 
## Call:
## lm(formula = y ~ x + fo + fu, data = dat_f)
## 
## Residuals:
##     Min      1Q  Median      3Q     Max 
## -35.202  -5.940   0.115   5.588  42.875 
## 
## Coefficients:
##             Estimate Std. Error t value Pr(>|t|)    
## (Intercept)  22.2978     1.2078  18.461  < 2e-16 ***
## x             0.6946     0.1990   3.490 0.000505 ***
## fo.L         27.2732     1.0717  25.448  < 2e-16 ***
## fo.Q         10.0139     0.9378  10.678  < 2e-16 ***
## fo.C          2.0443     0.7269   2.812 0.005015 ** 
## fo^4          0.2163     0.5409   0.400 0.689349    
## fuB         -23.1501     0.5645 -41.007  < 2e-16 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 8.921 on 993 degrees of freedom
## Multiple R-squared:  0.7269,	Adjusted R-squared:  0.7252 
## F-statistic: 440.4 on 6 and 993 DF,  p-value: < 2.2e-16
```
We can also compute averages for each group and construct a "between estimator"
$$
\overline{y}_i = \alpha + \overline{x}_i \beta
$$
Or we can subtract the average from each group to construct a "within estimator", 
$$
(y_{it} - \overline{y}_i) = (x_{it}-\overline{x}_i)\beta\\
$$
that tends to be more computationally efficient, has corrections for standard errors, and has additional summary statistics.

```r
library(fixest)
fe_reg1 <- feols(y~x|fo+fu, dat_f)
summary(fe_reg1)
```

```
## OLS estimation, Dep. Var.: y
## Observations: 1,000 
## Fixed-effects: fo: 5,  fu: 2
## Standard-errors: Clustered (fo) 
##   Estimate Std. Error t value  Pr(>|t|)    
## x 0.694565   0.123034  5.6453 0.0048485 ** 
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## RMSE: 8.88986     Adj. R2: 0.725211
##                 Within R2: 0.012116
```

**Hansen Econometrics, Theorem 17.1:** The fixed effects estimator of $\beta$ algebraically equals the dummy
variable estimator of $\beta$. The two estimators have the same residuals.
<!--
In fact, if the fixed effect is ``fully unstructured then the only way to consistently estimate the coefficient $\beta$ is by an estimator which is invariant'' (Hansen Econometrics, p). 
-->

Consistency is a great property, but only if the data generating process does in fact match the model. Many factor variables have effects that are not additively seperable.

```r
reg1 <- feols(y~x|fo^fu, dat_f)
summary(reg1)
```

```
## OLS estimation, Dep. Var.: y
## Observations: 1,000 
## Fixed-effects: fo^fu: 10
## Standard-errors: Clustered (fo^fu) 
##   Estimate Std. Error t value Pr(>|t|)    
## x  1.00253   0.457022 2.19361  0.05592 .  
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## RMSE: 3.31133     Adj. R2: 0.96172 
##                 Within R2: 0.154397
```

```r
reg2 <- lm(y~x*fo*fu, dat_f)
summary(reg2)
```

```
## 
## Call:
## lm(formula = y ~ x * fo * fu, data = dat_f)
## 
## Residuals:
##     Min      1Q  Median      3Q     Max 
## -9.4458 -1.5123 -0.0014  1.3625 12.6298 
## 
## Coefficients:
##             Estimate Std. Error t value Pr(>|t|)    
## (Intercept)  13.3936     0.6297  21.269  < 2e-16 ***
## x             2.8134     0.1095  25.683  < 2e-16 ***
## fo.L         23.8948     1.7881  13.363  < 2e-16 ***
## fo.Q          6.7611     1.5598   4.334 1.61e-05 ***
## fo.C         -0.8705     1.2241  -0.711   0.4771    
## fo^4         -1.0590     0.8958  -1.182   0.2374    
## fuB         -12.3701     0.9423 -13.127  < 2e-16 ***
## x:fo.L        5.3231     0.3107  17.134  < 2e-16 ***
## x:fo.Q        2.4056     0.2710   8.878  < 2e-16 ***
## x:fo.C        0.8980     0.2136   4.204 2.87e-05 ***
## x:fo^4        0.3176     0.1562   2.033   0.0423 *  
## x:fuB        -2.9777     0.1637 -18.193  < 2e-16 ***
## fo.L:fuB    -22.3617     2.7162  -8.233 5.80e-16 ***
## fo.Q:fuB     -4.3095     2.3577  -1.828   0.0679 .  
## fo.C:fuB      3.0354     1.7935   1.692   0.0909 .  
## fo^4:fuB      1.2683     1.2678   1.000   0.3174    
## x:fo.L:fuB   -5.5469     0.4716 -11.762  < 2e-16 ***
## x:fo.Q:fuB   -2.7675     0.4099  -6.752 2.50e-11 ***
## x:fo.C:fuB   -1.3170     0.3105  -4.241 2.44e-05 ***
## x:fo^4:fuB   -0.4176     0.2212  -1.888   0.0593 .  
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 2.555 on 980 degrees of freedom
## Multiple R-squared:  0.9779,	Adjusted R-squared:  0.9775 
## F-statistic:  2281 on 19 and 980 DF,  p-value: < 2.2e-16
```

```r
#reg2 <- feols(y~x*fo*fu|fo^fu, dat_f)
```


With *Random Effects*, the factor variable is modelled as coming from a distribution that is uncorrelated with the regressors. This is rarely used in economics today, and mostly included for historical reasons and a few cases where fixed effects cannot be estimates.

<!-- 
> The labels "random effects" and "fixed effects" are misleading. These are labels which arose in the early literature and we are stuck with these labels today. In a previous era regressors were viewed as "fixed". Viewing the individual effect as an unobserved regressor leads to the label of the individual effect as "fixed". Today, we rarely refer to regressors as "fixed" when dealing with observational data. We view all variables as random. Consequently describing u i as "fixed" does not make much sense and it is hardly a contrast with the "random effect" label since under either assumption u i is treated as random. Once again, the labels are unfortunate but the key difference is whether u i is correlated with the regressors.
-->


## More Literature

For OLS, see

* https://bookdown.org/josiesmith/qrmbook/linear-estimation-and-minimizing-error.html
* https://www.econometrics-with-r.org/4-lrwor.html
* https://www.econometrics-with-r.org/6-rmwmr.html
* https://www.econometrics-with-r.org/7-htaciimr.html
* https://bookdown.org/ripberjt/labbook/bivariate-linear-regression.html
* https://bookdown.org/ripberjt/labbook/multivariable-linear-regression.html
* https://online.stat.psu.edu/stat462/node/137/
* https://book.stat420.org/
* Hill, Griffiths & Lim (2007), Principles of Econometrics, 3rd ed., Wiley, S. 86f.
* Verbeek (2004), A Guide to Modern Econometrics, 2nd ed., Wiley, S. 51ff.
* Asteriou & Hall (2011), Applied Econometrics, 2nd ed., Palgrave MacMillan, S. 177ff.
* https://online.stat.psu.edu/stat485/lesson/11/


For fixed effects, see

* https://www.econometrics-with-r.org/10-rwpd.html
* https://bookdown.org/josiesmith/qrmbook/topics-in-multiple-regression.html
* https://bookdown.org/ripberjt/labbook/multivariable-linear-regression.html
* https://www.princeton.edu/~otorres/Panel101.pdf
* https://www.stata.com/manuals13/xtxtreg.pdf


# OLS Diagnostics
***

There's little sense in getting great standard errors for a bad model. Plotting your regression object a simple and easy step to help diagnose whether your model is in some way bad.

```r
reg <- lm(Murder~Assault+UrbanPop, data=USArrests)
par(mfrow=c(2,2))
plot(reg)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-25-1.png" width="672" />
We now go through what these figures show, and then some additional

## Assessing Outliers

The first plot examines outlier $Y$ and $\hat{Y}$.

>``In our $y_i = a + b x_i + e_i$ regression, the residuals are, of course, $e_i$ -- they reveal how much our fitted value $\hat{y}_i = a + b x_i$ differs from the observed $y_i$. A point $(x_i ,y_i)$ with a corresponding large residual is called an *outlier*. Say that you are interested in outliers because you somehow think that such points will exert undue *influence* on your estimates. Your feelings are generally right, but there are exceptions. A point might have a huge residual and yet not affect the estimated $b$ at all''
>Stata Press (2015) Base Reference Manual, Release 14, p. 2138.



```r
plot(fitted(reg), resid(reg),col = "grey", pch = 20,
     xlab = "Fitted", ylab = "Residual",
     main = "Fitted versus Residuals")
abline(h = 0, col = "darkorange", lwd = 2)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-26-1.png" width="672" />

```r
# car::outlierTest(reg)
```


The third plot examines outlier $X$ via ``leverage''

>"$(x_i ,y_i)$ can be an outlier in another way -- just as $y_i$ can be far from $\hat{y}_i$, $x_i$ can be far from the center of mass of the other $x$'s. Such an `outlier' should interest you just as much as the more traditional outliers. Picture a scatterplot of $y$ against $x$ with thousands of points in some sort of mass at the lower left of the graph and one point at the upper right of the graph. Now run a regression line through the points—the regression line will come close to the point at the upper right of the graph and may in fact, go through it. That is, this isolated point will not appear as an outlier as measured by residuals because its residual will be small. Yet this point might have a dramatic effect on our resulting estimates in the sense that, were you to delete the point, the estimates would change markedly. Such a point is said to have high *leverage*''
Stata Press (2015) Base Reference Manual, Release 14, pp. 2138-39.



```r
N <- 40
x <- c(25, runif(N-1,3,8))
e <- rnorm(N,0,0.4)
y <- 3 + 0.6*sqrt(x) + e
plot(y~x, pch=16, col=grey(.5,.5))
points(x[1],y[1], pch=16, col=rgb(1,0,0,.5))

abline(lm(y~x), col=2, lty=2)
abline(lm(y[-1]~x[-1]))
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-27-1.png" width="672" />

See https://www.r-bloggers.com/2016/06/leverage-and-influence-in-a-nutshell/ for a good interactive explaination.


Leverage Vector: Distance within explanatory variables
$$
H = [h_{1}, h_{2}, ...., h_{N}]
$$
$h_i$ is the leverage of residual $\hat{\epsilon_i}$. 


Studentized residuals
$$
r_i=\frac{\hat{\epsilon}_i}{s_{[i]}\sqrt{1-h_i}}
$$
and $s_{(i)}$ the root mean squared error of a regression with the $i$th observation removed.


```r
reg <- lm(y~x)
which.max(hatvalues(reg))
```

```
## 1 
## 1
```

```r
which.max(rstandard(reg))
```

```
## 27 
## 27
```


The fourth plot further assesses outlier $X$ using "Cook's Distance". Cook's Distance is defined as the sum of all the changes in the regression model when observation i is removed from.
$$
D_{i} = \frac{\sum_{j} \left( \hat{y_j} - \hat{y_j}_{[i]} \right)^2 }{ p s^2 }
= \frac{[e_{i}]^2}{p s^2 } \frac{h_i}{(1-h_i)^2}\\
s^2 = \frac{\sum_{i} (e_{i})^2 }{n-K}
$$

```r
which.max(cooks.distance(reg))
```

```
## 1 
## 1
```

```r
car::influencePlot(reg)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-29-1.png" width="672" />

```
##       StudRes        Hat       CookD
## 1  -0.7080720 0.83356849 1.272234319
## 8   2.4551532 0.04739966 0.132442189
## 27  3.4031443 0.03014455 0.140781669
## 32 -0.2052746 0.04868956 0.001106221
```

Note that we can also calculate $H$ directly from our OLS projection matrix $\hat{P}$, since $H=diag(\hat{P})$ and
$$
\hat{P}=X(X'X)^{-1}X'\\
\hat{\epsilon}=y-X\hat{\beta}=y-X(X'X)^{-1}X'y=y-\hat{P}y\\
\hat{P}y=X(X'X)^{-1}X'y=y-(y-X(X'X)^{-1}X'y)=y-\hat{\epsilon}=\hat{y}\\
$$

```r
Ehat <- Y - X%*% Bhat
## Ehat
## resid(reg)

Pmat <- X%*%XtXi%*%t(X)
Yhat <- Pmat%*%Y
## Yhat
## predict(reg)
```



There are many other diagnostics (which can often be written in terms of Cooks Distance or Vice Versa). 

```r
# Sall, J. (1990) Leverage plots for general linear hypotheses. American Statistician *44*, 308-315.
# car::leveragePlots(reg)
```

(Welsch and Kuh. 1977; Belsley, Kuh, and Welsch. 1980) attempt to summarize the information in the leverage versus residual-squared plot into one DFITS statistic where $DFITS > 2\sqrt{{k}/{n}}$ should be examined. 
$$
\text{DFITS}_i=r_i\sqrt{\frac{h_i}{1-h_i}}\\
$$

See also "dfbetas" and "covratio"

```r
#dfbetas(reg)
#dffits(reg)
#covratio(reg)
#hatvalues(reg)
head(influence.measures(reg)$infmat)
```

```
##         dfb.1_        dfb.x        dffit     cov.r       cook.d        hat
## 1  1.249434096 -1.560695069 -1.584638840 6.1693222 1.272234e+00 0.83356849
## 2 -0.002959483  0.001035131 -0.004480183 1.0833535 1.030706e-05 0.02640982
## 3  0.021582718 -0.002507510  0.041352452 1.0780575 8.765471e-04 0.02509226
## 4 -0.020355789  0.012936732 -0.023014630 1.0939712 2.718917e-04 0.03654792
## 5 -0.098167101 -0.048745853 -0.304864306 0.9022108 4.357058e-02 0.02565592
## 6 -0.268700686  0.145953800 -0.331785204 0.9111659 5.171838e-02 0.03099875
```


## Assessing Normality and Collinearity

The second plot examines whether the residuals are normally distributed. OLS point estimates do not depend on the normality of the residuals. (Good thing, because there's no reason the residuals of economic phenomena should be so well behaved.) Many hypothesis tests of the regression estimates are, however, affected by the distribution of the residuals. For these reasons, you may be interested in assessing normality 

```r
par(mfrow=c(1,2))
hist(resid(reg), main='Histogram of Residuals')

qqnorm(resid(reg), main="Normal Q-Q Plot of Residuals", col="darkgrey")
qqline(resid(reg), col="dodgerblue", lwd=2)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-33-1.png" width="672" />

```r
shapiro.test(resid(reg))
```

```
## 
## 	Shapiro-Wilk normality test
## 
## data:  resid(reg)
## W = 0.95128, p-value = 0.08392
```

```r
# car::qqPlot(reg)
```

Assessing Heterskedasticity may also matters for variance estimates. This is not shown in the plot, but you can run a simple test

```r
library(lmtest)
```

```
## Loading required package: zoo
```

```
## 
## Attaching package: 'zoo'
```

```
## The following objects are masked from 'package:base':
## 
##     as.Date, as.Date.numeric
```

```r
lmtest::bptest(reg)
```

```
## 
## 	studentized Breusch-Pagan test
## 
## data:  reg
## BP = 0.043936, df = 1, p-value = 0.834
```


This is when one explanatory variable in a multiple regression model can be linearly predicted from the others with a substantial degree of accuracy. Coefficient estimates may change erratically in response to small changes in the model or the data. (In the extreme case where there are more variables than observations $K>\geq N$, $X'X$ has an infinite number of solutions and is not invertible.)

To diagnose this, we can use the Variance Inflation Factor
$$
VIF_{k}=\frac{1}{1-R^2_k},
$$
where $R^2_k$ is the $R^2$ for the regression of $X_k$ on the other covariates $X_{-k}$ (a regression that does not involve the response variable Y)

```r
car::vif(reg) 
sqrt(car::vif(reg)) > 2 # problem?
```


## Linear in Parameters


Data transformations can often improve model fit and still be estimated via OLS. This is because OLS is only required to be linear in the parameters. Under the assumptions of the model is correctly specified, this is how we can interpret the coefficients of the transformed data. (Note for small changes, $\Delta ln(x) \approx \Delta x / x = \Delta x \% \cdot 100$.)

| *Specification* | *Regressand* | *Regressor* | *Derivative* | *Interpretation (If True)* |
| --- | --- | --- | --- | --- |
| linear--linear | $y$          | $x$   | $\Delta y = \beta_1\cdot\Delta x$ | Change $x$ by one unit $\rightarrow$ change $y$ by $\beta_1$ units.|
| log--linear | $ln(y)$ | $x$ | $\Delta y \% \cdot 100 \approx \beta_1 \cdot \Delta x$ | Change $x$ by one unit $\rightarrow$ change $y$ by $100 \cdot \beta_1$ percent. |
| linear--log | $y$ | $ln(x)$ | $\Delta y \approx  \frac{\beta_1}{100}\cdot \Delta x \%$ | Change $x$ by one percent $\rightarrow$ change $y$ by $\frac{\beta_1}{100}$ units |
| log--log | $ln(y)$ | $ln(x)$ | $\Delta y \% \approx \beta_1\cdot \Delta x \%$ | Change $x$ by one percent $\rightarrow$ change $y$ by $\beta_1$ percent|

Now recall from micro theory that an additively seperable and linear production function is referred to as ``perfect substitutes''. With a linear model and untranformed data, you have implicitly modelled the different regressors $X$ as perfect substitutes. Further recall that the ''perfect substitutes'' model is a special case of the constant elasticity of substitution production function. Here, we will build on http://dx.doi.org/10.2139/ssrn.3917397, and consider box-cox transforming both $X$ and $y$. Specifically, apply the box-cox transform of $y$ using parameter $\lambda$ and apply another box-cox transform to each $x$ using the same parameter $\rho$ so that
$$
y^{(\lambda)}_{i} = \sum_{k}\beta_{k} x^{(\rho)}_{k,i} + \epsilon_{i}\\
y^{(\lambda)}_{i} =
\begin{cases}
\lambda^{-1}[ (y_i+1)^{\lambda}- 1] & \lambda \neq 0 \\
log(y_i+1) &  \lambda=0
\end{cases}.\\
x^{(\rho)}_{i} =
\begin{cases}
\rho^{-1}[ (x_i)^{\rho}- 1] & \rho \neq 0 \\
log(x_{i}+1) &  \rho=0
\end{cases}.
$$

Notice that this nests:

 * linear-linear $(\rho=\lambda=1)$.
 * linear-log $(\rho=1, \lambda=0)$.
 * log-linear $(\rho=0, \lambda=1)$.
 * log-log  $(\rho=\lambda=0)$.


If $\rho=\lambda$, we get the CES production function. This nests the ''perfect substitutes'' linear-linear model ($\rho=\lambda=1$) , the ''cobb-douglas''  log-log model  ($\rho=\lambda=0$), and many others. We can define $\lambda=\rho/\lambda'$ to be clear that this is indeed a CES-type transformation where

* $\rho \in (-\infty,1]$ controls the "substitutability" of explanatory variables. E.g., $\rho <0$ is ''complementary''.
* $\lambda$ determines ''returns to scale''. E.g., $\lambda<1$ is ''decreasing returns''.


We compute the mean squared error in the original scale by inverting the predictions;
$$
\widehat{y}_{i} =
\begin{cases}
[ \widehat{y^{(\lambda)}}_{i} \cdot \lambda ]^{1/\lambda} -1 & \lambda  \neq 0 \\
exp( \widehat{y^{(\lambda)}}_{i}) -1 &  \lambda=0
\end{cases}.
$$


It is easiest to optimize parameters in a 2-step procedure called  `concentrated optimization'. We first solve for $\widehat{\beta}(\rho,\lambda)$ and compute the mean squared error $MSE(\rho,\lambda)$. We then find the $(\rho,\lambda)$ which minimizes $MSE$.

```r
## Box-Cox Transformation Function
bxcx <- function( xy, rho){
    if (rho == 0L) {
      log(xy+1)
    } else if(rho == 1L){
      xy
    } else {
      ((xy+1)^rho - 1)/rho
    }
}
bxcx_inv <- function( xy, rho){
    if (rho == 0L) {
      exp(xy) - 1
    } else if(rho == 1L){
      xy
    } else {
     (xy * rho + 1)^(1/rho) - 1
    }
}

## Which Variables
reg <- lm(Murder~Assault+UrbanPop, data=USArrests)
X <- USArrests[,c('Assault','UrbanPop')]
Y <- USArrests[,'Murder']

## Simple Grid Search
## Which potential (Rho,Lambda) 
rl_df <- expand.grid(rho=seq(-2,2,by=.5),lambda=seq(-2,2,by=.5))

## Compute Mean Squared Error
## from OLS on Transformed Data
errors <- apply(rl_df,1,function(rl){
    Xr <- bxcx(X,rl[[1]])
    Yr <- bxcx(Y,rl[[2]])
    Datr <- cbind(Murder=Yr,Xr)
    Regr <- lm(Murder~Assault+UrbanPop, data=Datr)
    Predr <- bxcx_inv(predict(Regr),rl[[2]])
    Resr  <- (Y - Predr)
    return(Resr)
})
rl_df$mse <- colMeans(errors^2)

## Want Small MSE and Interpretable
## (-1,0,1,2 are Easy to interpretable)
library(ggplot2)
ggplot(rl_df, aes(rho, lambda, fill=mse )) +
    geom_tile() + ggtitle('Mean Squared Error') 
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-36-1.png" width="672" />

```r
## Which min
rl0 <- rl_df[which.min(rl_df$mse),c('rho','lambda')]

## Which give NA?
## which(is.na(errors), arr.ind=T)

## Plot
Xr <- bxcx(X,rl0[[1]])
Yr <- bxcx(Y,rl0[[2]])
Datr <- cbind(Murder=Yr,Xr)
Regr <- lm(Murder~Assault+UrbanPop, data=Datr)
Predr <- bxcx_inv(predict(Regr),rl0[[2]])

cols <- c(rgb(1,0,0,.5), col=rgb(0,0,1,.5))
plot(Y, Predr, pch=16, col=cols[1], ylab='Prediction')
points(Y, predict(reg), pch=16, col=cols[2])
legend('topleft', pch=c(16), col=cols, title='Rho,Lambda',
    legend=c(  paste0(rl0, collapse=','),'1,1') )
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-36-2.png" width="672" />

Note that the default hypothesis testing procedures do not account for you trying out different transformations. Specification searches deflate standard errors and are a major source for false discoveries.


## More Literature


* https://book.stat420.org/model-diagnostics.html#leverage
* https://socialsciences.mcmaster.ca/jfox/Books/RegressionDiagnostics/index.html
* https://bookdown.org/ripberjt/labbook/diagnosing-and-addressing-problems-in-linear-regression.html
* Belsley, D. A., Kuh, E., and Welsch, R. E. (1980). Regression Diagnostics: Identifying influential data and sources of collinearity. Wiley. https://doi.org/10.1002/0471725153
* Fox, J. D. (2020). Regression diagnostics: An introduction (2nd ed.). SAGE. https://dx.doi.org/10.4135/9781071878651



# OLS and Endogeneity
***

Just like many economic relationships are nonlinear, many economic variables are endogenous. By this we typically mean that $X$ is an outcome determined (or caused: $\to$) by some other variable.

 * If $Y \to X$, then we have reverse causality
 * If $Y \to X$ and $X \to Y$, then we have simultaneity
 * If $Z\to Y$ and either $Z\to X$ or $X \to Z$, then we have omitted a potentially important variable

These endogeneity issues imply $X$ and $\epsilon$ are correlated, which is a barrier to interpreting OLS as a causal model.


```r
## Simulate data with an endogeneity issue
n <- 300
z <- rbinom(n,1,.5)
xy <- sapply(z, function(zi){
    y <- rnorm(1,zi,1)
    x <- rnorm(1,zi*2,1)
    c(x,y)
})
xy <- data.frame(x=xy[1,],y=xy[2,])
plot(y~x, data=xy, pch=16, col=grey(.5,.5))
abline(lm(y~x,data=xy))
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-37-1.png" width="672" />

Three statistical tools: 2SLS, RDD, and DID, are designed to address endogeneity issues. The elementary versions of these tools are linear regression. Because there are many textbooks and online notebooks that explain these methods at both high and low levels of technical detail, they are not covered extensively in this notebook. You are directed to the following resources which discuss these statistical models in more general terms and how they can be applied across many social sciences.

* Causal Inference for Statistics, Social, and Biomedical Sciences: An Introduction
* https://www.mostlyharmlesseconometrics.com/
* https://www.econometrics-with-r.org
* https://bookdown.org/paul/applied-causal-analysis/
* https://mixtape.scunning.com/
* https://theeffectbook.net/
* https://www.r-causal.org/
* https://matheusfacure.github.io/python-causality-handbook/landing-page.html


## Two Stage Least Squares (2SLS)

* https://www.econometrics-with-r.org/12-ivr.html
* https://bookdown.org/paul/applied-causal-analysis/estimation-2.html
* https://mixtape.scunning.com/07-instrumental_variables
* https://theeffectbook.net/ch-InstrumentalVariables.html
* http://www.urfie.net/read/index.html#page/247

Note that the coefficient interpretation still rests on many assumptions. Taking the classic case of supply shock in a market setting (the situation the method was originally developed for) we are implicitly assuming

* both supply and demand are linear (and additively seperable in covariates).
* only supply was affected, and it was only an intercept shift.
* the shock large enough to be picked up statistically.

If we had multiple alleged supply shifts and recorded their magnitudes, then we could recover more information about demand. One common diagnostic tool is simply to report the reduced form results. We could also use a nonparametric estimator to diagnose linearity at each stage.

```r
#reg2_alt_fs <- lm(Q~cost, data=dat2)
#summary(reg2_alt_fs)
#lo2_alt_fs <- loess(Q~cost, data=dat2)
```

Other tools are used to help address some of the other assumptions.

## Regression Discontinuities/Kink (RD/RK)

* https://bookdown.org/paul/applied-causal-analysis/rdd-regression-discontinuity-design.html
* https://mixtape.scunning.com/06-regression_discontinuity
* https://theeffectbook.net/ch-RegressionDiscontinuity.html

## Difference in Differences (DID)

* https://mixtape.scunning.com/09-difference_in_differences
* https://theeffectbook.net/ch-DifferenceinDifference.html
* http://www.urfie.net/read/index.html#page/226


# Data Scientism
***

There is currently a boom in empirical research centered around linear regression analysis. This is not for the first boom in empirical research, and we'd be wise to recall some earlier wisdom from economists on the matter.

> The blind transfer of the striving for quantitative measurements to a field where the specific conditions are not present which give it its basic importance in the natural sciences is the result of an entirely unfounded prejudice. It is probably responsible for the worst aberrations and absurdities produced by scientism in the social sciences. It not only leads frequently to the selection for study of the most irrelevant aspects of the phenomena because they happen to be measurable, but also to "measurements" and assignments of numerical values which are absolutely meaningless. What a distinguished philosopher recently wrote about psychology is at least equally true of the social sciences, namely that it is only too easy "to rush off to measure something without considering what it is we are measuring, or what measurement means. In this respect some recent measurements are of the same logical type as Plato's determination that a just ruler is 729 times as happy as an unjust one."
>
> --- F.A. Hayek, 1943

> if you torture the data long enough, it will confess
>
> --- R. Coase (Source Unknown)


> the definition of a causal parameter is not always clearly stated, and formal statements of identifying conditions in terms of well-specified economic models are rarely presented. Moreover, the absence of explicit structural frameworks makes it difficult to cumulate knowledge across studies conducted within this framework. Many studies produced by this research program have a `stand alone' feature and neither inform nor are influenced by the general body of empirical knowledge in economics.
>
> --- J.J. Heckman, 2000


> without explicit prior consideration of the effect of the instrument choice on the parameter being estimated, such a procedure is effectively the opposite of standard statistical practice in which a parameter of interest is defined first, followed by an estimator that delivers that parameter. Instead, we have a procedure in which the choice of the instrument, which is guided by criteria designed for a situation in which there is no heterogeneity, is implicitly allowed to determine the parameter of interest. This goes beyond the old story of looking for an object where the light is strong enough to see; rather, we have at least some control over the light but choose to let it fall where it may and then proclaim that whatever it illuminates is what we were looking for all along.
>
> --- A. Deaton, 2010




The OLS examples are familiar are subject to current research. At the end are two simple examples of scientism with the ''latest and greatest'' empirical recipes---we don't have many theoretical results yet but I think you can understand the issue with the numerical example. 

## OLS in the age of big data

We begin with a motivating empirical example and then an simulation excercise.

### US Gov't Spending on Science

Get and inspect some data from https://tylervigen.com/spurious-correlations


```r
## Your data is not made up in the computer (hopefully!)
## will normally be an address on your PC
vigen_csv <- read.csv( paste0(
'https://raw.githubusercontent.com/the-mad-statter/',
'whysospurious/master/data-raw/tylervigen.csv') ) 
class(vigen_csv)
```

```
## [1] "data.frame"
```

```r
names(vigen_csv)
```

```
##  [1] "year"                         "science_spending"            
##  [3] "hanging_suicides"             "pool_fall_drownings"         
##  [5] "cage_films"                   "cheese_percap"               
##  [7] "bed_deaths"                   "maine_divorce_rate"          
##  [9] "margarine_percap"             "miss_usa_age"                
## [11] "steam_murders"                "arcade_revenue"              
## [13] "computer_science_doctorates"  "noncom_space_launches"       
## [15] "sociology_doctorates"         "mozzarella_percap"           
## [17] "civil_engineering_doctorates" "fishing_drownings"           
## [19] "kentucky_marriage_rate"       "oil_imports_norway"          
## [21] "chicken_percap"               "train_collision_deaths"      
## [23] "oil_imports_total"            "pool_drownings"              
## [25] "nuclear_power"                "japanese_cars_sold"          
## [27] "motor_vehicle_suicides"       "spelling_bee_word_length"    
## [29] "spider_deaths"                "math_doctorates"             
## [31] "uranium"
```

```r
vigen_csv[1:5,1:5]
```

```
##   year science_spending hanging_suicides pool_fall_drownings cage_films
## 1 1996               NA               NA                  NA         NA
## 2 1997               NA               NA                  NA         NA
## 3 1998               NA               NA                  NA         NA
## 4 1999            18079             5427                 109          2
## 5 2000            18594             5688                 102          2
```

```r
## similar `apply' functions
lapply(vigen_csv[,1:5], class) ## like apply, but for lists
```

```
## $year
## [1] "integer"
## 
## $science_spending
## [1] "integer"
## 
## $hanging_suicides
## [1] "integer"
## 
## $pool_fall_drownings
## [1] "integer"
## 
## $cage_films
## [1] "integer"
```

```r
sapply(vigen_csv[,1:5], class) ## lapply, formatted to a vector
```

```
##                year    science_spending    hanging_suicides pool_fall_drownings 
##           "integer"           "integer"           "integer"           "integer" 
##          cage_films 
##           "integer"
```

The US government spending on science is ruining cinema
(p<.001)!?


```r
## Drop Data before 1999
vigen_csv <- vigen_csv[vigen_csv$year >= 1999,] 

## Run OLS Regression $
reg1 <-  lm(cage_films ~ -1 + science_spending,
    data=vigen_csv)
summary(reg1)
```

```
## 
## Call:
## lm(formula = cage_films ~ -1 + science_spending, data = vigen_csv)
## 
## Residuals:
##     Min      1Q  Median      3Q     Max 
## -1.7670 -0.7165  0.1447  0.7890  1.4531 
## 
## Coefficients:
##                   Estimate Std. Error t value Pr(>|t|)    
## science_spending 9.978e-05  1.350e-05    7.39 2.34e-05 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 1.033 on 10 degrees of freedom
##   (1 observation deleted due to missingness)
## Multiple R-squared:  0.8452,	Adjusted R-squared:  0.8297 
## F-statistic: 54.61 on 1 and 10 DF,  p-value: 2.343e-05
```


It's not all bad, people in maine stay married longer?


```r
plot.new()
plot.window(xlim=c(1999, 2009), ylim=c(7,9))
lines(log(maine_divorce_rate*1000)~year, data=vigen_csv)
lines(log(science_spending/10)~year, data=vigen_csv, lty=2)
axis(1)
axis(2)
legend('topright', lty=c(1,2), legend=c(
    'log(maine_divorce_rate*1000)',
    'log(science_spending/10)'))
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-41-1.png" width="672" />



```r
par(mfrow=c(1,2), mar=c(2,2,2,1))
plot.new()
plot.window(xlim=c(1999, 2009), ylim=c(5,9)*1000)
lines(science_spending/3~year, data=vigen_csv, lty=1, col=2, pch=16)
text(2003, 8200, 'US spending on science, space, technology (USD/3)', col=2, cex=.6, srt=30)
lines(hanging_suicides~year, data=vigen_csv, lty=1, col=4, pch=16)
text(2004, 6500, 'US Suicides by hanging, strangulation, suffocation (Deaths)', col=4, cex=.6, srt=30)
axis(1)
axis(2)


plot.new()
plot.window(xlim=c(2002, 2009), ylim=c(0,5))
lines(cage_films~year, data=vigen_csv[vigen_csv$year>=2002,], lty=1, col=2, pch=16)
text(2006, 0.5, 'Number of films with Nicolas Cage (Films)', col=2, cex=.6, srt=0)
lines(pool_fall_drownings/25~year, data=vigen_csv[vigen_csv$year>=2002,], lty=1, col=4, pch=16)
text(2006, 4.5, 'Number of drownings by falling into pool (US Deaths/25)', col=4, cex=.6, srt=0)
axis(1)
axis(2)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-42-1.png" width="672" />




```r
## Include an intercept to regression 1
#reg2 <-  lm(cage_films ~ science_spending, data=vigen_csv)
#suppressMessages(library(stargazer))
#stargazer(reg1, reg2, type='html')
```




### False Positives arise from errors

A huge amount of data normally means a huge amount of data cleaning/merging/aggregating. Some spurious results are driven by errors in this process, so be careful.


```r
## Function to Create Sample Datasets
make_noisy_data <- function(n, b=0){
    x <- seq(1,10, length.out=n)
    e <- rnorm(length(x), mean=0, sd=10)
    y <- b*x + e
    xy_mat <- data.frame(ID=seq(x), x=x, y=y)
    return(xy_mat)
}

## Two sample datasets
dat1 <- make_noisy_data(6)
dat2 <- make_noisy_data(6)

## Merging data in wide format
dat_merged_wide <- merge(dat1, dat2,
    by='ID', suffixes=c('.1','.2'))

## merging data in long format and reshaping to wide
dat_merged_long <- rbind( cbind(dat1,DF=1),cbind(dat2,DF=2))
library(reshape2)
dat_melted <- melt(dat_merged_long, id.vars=c('ID', 'DF'))
dat_merged_wide2 <- dcast(dat_melted, ID~DF+variable)

## CHECK they are the same.
dat_merged_wide == dat_merged_wide2
```

```
##        ID  x.1  y.1  x.2  y.2
## [1,] TRUE TRUE TRUE TRUE TRUE
## [2,] TRUE TRUE TRUE TRUE TRUE
## [3,] TRUE TRUE TRUE TRUE TRUE
## [4,] TRUE TRUE TRUE TRUE TRUE
## [5,] TRUE TRUE TRUE TRUE TRUE
## [6,] TRUE TRUE TRUE TRUE TRUE
```

Nevertheless, data transformation is often necessary before regression analysis. For downloading tips, see https://raw.githubusercontent.com/rstudio/cheatsheets/main/data-import.pdf
<!--\url{https://github.com/rstudio/cheatsheets/raw/master/data-transformation.pdf}-->

### False Positives arise from Regression Machines

Another class of errors pertains to P-hacking (and it's various synonyms) 


```r
n <- 50
p <- 1
i <- 0
X1 <- runif(n)

## P-hacking
while(p >= .001){ ## stops when p < .001
    ## Get Random Covariate
    set.seed(i)
    X2 <-  runif(n)
    ## Merge and `Analyze'
    dat_i <- data.frame(X1,X2)
    reg_i <- lm(X1~X2, data=dat_i)
    ## update results in global environment
    p <- summary(reg_i)$coefficients[2,4]
    i <- i+1
}

plot(X1~X2, data=dat_i,
    pch=16, col=grey(.5,.5),
    main=paste0('Random Dataset ', i))
abline(reg_i)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-45-1.png" width="672" />


For more intuition on spurious correlations, try http://shiny.calpoly.sh/Corr_Reg_Game/


## Causal effects *sans theory*

We simply apply ``credible methods'' to a couple of random walks; finding a treatment that fits mold and adding various robustness checks that make the treatment appear robust. The analysis sounds scientific, and you could probably be convinced if it were not just random noise. 


### RDD


```r
n <- 1000
n_index <- seq(n)

set.seed(1)
random_walk1 <- cumsum(runif(n,-1,1))

set.seed(2)
random_walk2 <- cumsum(runif(n,-1,1))

par(mfrow=c(1,2))
plot(random_walk1, pch=16, col=grey(.5,.5))
plot(random_walk2, pch=16, col=grey(.5,.5))
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-46-1.png" width="672" />


```r
## Let the data take shape
## (around the large differences before and after)
n1 <- 290
wind1 <- c(n1-300,n1+300)
dat1 <- data.frame(t=n_index, y=random_walk1, d=1*(n_index > n1))
dat1_sub <- dat1[ n_index>wind1[1] & n_index < wind1[2],]

## Then find your big break
reg0 <- lm(y~t, data=dat1_sub[dat1_sub$d==0,])
reg1 <- lm(y~t, data=dat1_sub[dat1_sub$d==1,])

## The evidence should show openly (it's just science)
plot(random_walk1, pch=16, col=grey(.5,.5), xlim=wind1)
abline(v=n1, lty=2)
lines(reg0$model$t, reg0$fitted.values, col=2)
lines(reg1$model$t, reg1$fitted.values, col=4)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-47-1.png" width="672" />


```r
## Dress with some statistics for added credibility
rdd_sub <- lm(y~d+t+d*t, data=dat1_sub)
rdd_full <- lm(y~d+t+d*t, data=dat1)
stargazer::stargazer(rdd_sub, rdd_full, 
    type='html',
    title='Recipe RDD',
    header=F,
    omit=c('Constant'),
    notes=c('First column uses a dataset around the discontinuity.',
    'Smaller windows are more causal, and where the effect is bigger.'))
```


<table style="text-align:center"><caption><strong>Recipe RDD</strong></caption>
<tr><td colspan="3" style="border-bottom: 1px solid black"></td></tr><tr><td style="text-align:left"></td><td colspan="2"><em>Dependent variable:</em></td></tr>
<tr><td></td><td colspan="2" style="border-bottom: 1px solid black"></td></tr>
<tr><td style="text-align:left"></td><td colspan="2">y</td></tr>
<tr><td style="text-align:left"></td><td>(1)</td><td>(2)</td></tr>
<tr><td colspan="3" style="border-bottom: 1px solid black"></td></tr><tr><td style="text-align:left">d</td><td>-13.169<sup>***</sup></td><td>-9.639<sup>***</sup></td></tr>
<tr><td style="text-align:left"></td><td>(0.569)</td><td>(0.527)</td></tr>
<tr><td style="text-align:left"></td><td></td><td></td></tr>
<tr><td style="text-align:left">t</td><td>0.011<sup>***</sup></td><td>0.011<sup>***</sup></td></tr>
<tr><td style="text-align:left"></td><td>(0.001)</td><td>(0.002)</td></tr>
<tr><td style="text-align:left"></td><td></td><td></td></tr>
<tr><td style="text-align:left">d:t</td><td>0.009<sup>***</sup></td><td>0.004<sup>*</sup></td></tr>
<tr><td style="text-align:left"></td><td>(0.002)</td><td>(0.002)</td></tr>
<tr><td style="text-align:left"></td><td></td><td></td></tr>
<tr><td colspan="3" style="border-bottom: 1px solid black"></td></tr><tr><td style="text-align:left">Observations</td><td>589</td><td>1,000</td></tr>
<tr><td style="text-align:left">R<sup>2</sup></td><td>0.771</td><td>0.447</td></tr>
<tr><td style="text-align:left">Adjusted R<sup>2</sup></td><td>0.770</td><td>0.446</td></tr>
<tr><td style="text-align:left">Residual Std. Error</td><td>1.764 (df = 585)</td><td>3.081 (df = 996)</td></tr>
<tr><td style="text-align:left">F Statistic</td><td>658.281<sup>***</sup> (df = 3; 585)</td><td>268.763<sup>***</sup> (df = 3; 996)</td></tr>
<tr><td colspan="3" style="border-bottom: 1px solid black"></td></tr><tr><td style="text-align:left"><em>Note:</em></td><td colspan="2" style="text-align:right"><sup>*</sup>p<0.1; <sup>**</sup>p<0.05; <sup>***</sup>p<0.01</td></tr>
<tr><td style="text-align:left"></td><td colspan="2" style="text-align:right">First column uses a dataset around the discontinuity.</td></tr>
<tr><td style="text-align:left"></td><td colspan="2" style="text-align:right">Smaller windows are more causal, and where the effect is bigger.</td></tr>
</table>


### DID


```r
## Find a reversal of fortune
## (A good story always goes well with a nice pre-trend)
n2 <- 318
wind2 <- c(n2-20,n2+20)
plot(random_walk2, pch=16, col=4, xlim=wind2, ylim=c(-15,15))
points(random_walk1, pch=16, col=2)
abline(v=n2, lty=2)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-49-1.png" width="672" />


```r
## Knead out any effects that are non-causal 
## (or even just correlation)
dat2A <- data.frame(t=n_index, y=random_walk1, d=1*(n_index > n2), RWid=1)
dat2B <- data.frame(t=n_index, y=random_walk2, d=0, RWid=2)
dat2  <- rbind(dat2A, dat2B)
dat2$RWid <- as.factor(dat2$RWid)
dat2$tid <- as.factor(dat2$t)
dat2_sub <- dat2[ dat2$t>wind2[1] & dat2$t < wind2[2],]

## Report the stars for all to enjoy
## (and remind that stable coefficients are the good ones)
did_fe1 <- lm(y~d+tid, data=dat2_sub)
did_fe2 <- lm(y~d+RWid, data=dat2_sub)
did_fe3 <- lm(y~d*RWid+tid, data=dat2_sub)
stargazer::stargazer(did_fe1, did_fe2, did_fe3,
    type='html',
    title='Recipe DID',
    header=F,
    omit=c('tid','RWid', 'Constant'),
    notes=c(
     'Fixed effects for time in column 1, for id in column 2, and both in column 3.',
     'Fixed effects control for most of your concerns.',
     'Anything else creates a bias in the opposite direction.'))
```


<table style="text-align:center"><caption><strong>Recipe DID</strong></caption>
<tr><td colspan="4" style="border-bottom: 1px solid black"></td></tr><tr><td style="text-align:left"></td><td colspan="3"><em>Dependent variable:</em></td></tr>
<tr><td></td><td colspan="3" style="border-bottom: 1px solid black"></td></tr>
<tr><td style="text-align:left"></td><td colspan="3">y</td></tr>
<tr><td style="text-align:left"></td><td>(1)</td><td>(2)</td><td>(3)</td></tr>
<tr><td colspan="4" style="border-bottom: 1px solid black"></td></tr><tr><td style="text-align:left">d</td><td>1.804<sup>*</sup></td><td>1.847<sup>***</sup></td><td>5.851<sup>***</sup></td></tr>
<tr><td style="text-align:left"></td><td>(0.892)</td><td>(0.652)</td><td>(0.828)</td></tr>
<tr><td style="text-align:left"></td><td></td><td></td><td></td></tr>
<tr><td colspan="4" style="border-bottom: 1px solid black"></td></tr><tr><td style="text-align:left">Observations</td><td>78</td><td>78</td><td>78</td></tr>
<tr><td style="text-align:left">R<sup>2</sup></td><td>0.227</td><td>0.164</td><td>0.668</td></tr>
<tr><td style="text-align:left">Adjusted R<sup>2</sup></td><td>-0.566</td><td>0.142</td><td>0.309</td></tr>
<tr><td style="text-align:left">Residual Std. Error</td><td>2.750 (df = 38)</td><td>2.035 (df = 75)</td><td>1.827 (df = 37)</td></tr>
<tr><td style="text-align:left">F Statistic</td><td>0.287 (df = 39; 38)</td><td>7.379<sup>***</sup> (df = 2; 75)</td><td>1.860<sup>**</sup> (df = 40; 37)</td></tr>
<tr><td colspan="4" style="border-bottom: 1px solid black"></td></tr><tr><td style="text-align:left"><em>Note:</em></td><td colspan="3" style="text-align:right"><sup>*</sup>p<0.1; <sup>**</sup>p<0.05; <sup>***</sup>p<0.01</td></tr>
<tr><td style="text-align:left"></td><td colspan="3" style="text-align:right">Fixed effects for time in column 1, for id in column 2, and both in column 3.</td></tr>
<tr><td style="text-align:left"></td><td colspan="3" style="text-align:right">Fixed effects control for most of your concerns.</td></tr>
<tr><td style="text-align:left"></td><td colspan="3" style="text-align:right">Anything else creates a bias in the opposite direction.</td></tr>
</table>



