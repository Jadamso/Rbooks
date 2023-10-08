
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
## [1] 0.5889724
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
<div class="plotly html-widget html-fill-item-overflow-hidden html-fill-item" id="htmlwidget-f145034e777aef9affb3" style="width:672px;height:480px;"></div>
<script type="application/json" data-for="htmlwidget-f145034e777aef9affb3">{"x":{"visdat":{"20a177e1b6ae":["function () ","plotlyVisDat"]},"cur_data":"20a177e1b6ae","attrs":{"20a177e1b6ae":{"x":{},"y":{},"text":{},"mode":"markers","hoverinfo":"text","showlegend":false,"marker":{"size":{},"opacity":0.5,"showscale":true,"colorbar":{"title":"Murder Arrests (per 100,000)"}},"color":{},"alpha_stroke":1,"sizes":[10,100],"spans":[1,20],"type":"scatter"}},"layout":{"margin":{"b":40,"l":60,"t":25,"r":10},"title":"Crime and Urbanization in America 1975","xaxis":{"domain":[0,1],"automargin":true,"title":"Percent of People in an Urban Area"},"yaxis":{"domain":[0,1],"automargin":true,"title":"Assault Arrests per 100,000 People"},"hovermode":"closest","showlegend":false},"source":"A","config":{"modeBarButtonsToAdd":["hoverclosest","hovercompare"],"showSendToCloud":false},"data":[{"x":[58,48,80,50,91,78,77,72,80,60,83,54,83,65,57,66,52,66,51,67,85,74,66,44,70,53,62,81,56,89,70,86,45,44,75,68,67,72,87,48,45,59,80,80,32,63,73,39,66,60],"y":[236,263,294,190,276,204,110,238,335,211,46,120,249,113,56,115,109,249,83,300,149,255,72,259,178,109,102,252,57,159,285,254,337,45,120,151,159,106,174,279,86,188,201,120,48,156,145,81,53,161],"text":["<b> Alabama <\/b> <br>Urban  : 58 <br>Assault: 236 <br>Murder : 13.2","<b> Alaska <\/b> <br>Urban  : 48 <br>Assault: 263 <br>Murder : 10","<b> Arizona <\/b> <br>Urban  : 80 <br>Assault: 294 <br>Murder : 8.1","<b> Arkansas <\/b> <br>Urban  : 50 <br>Assault: 190 <br>Murder : 8.8","<b> California <\/b> <br>Urban  : 91 <br>Assault: 276 <br>Murder : 9","<b> Colorado <\/b> <br>Urban  : 78 <br>Assault: 204 <br>Murder : 7.9","<b> Connecticut <\/b> <br>Urban  : 77 <br>Assault: 110 <br>Murder : 3.3","<b> Delaware <\/b> <br>Urban  : 72 <br>Assault: 238 <br>Murder : 5.9","<b> Florida <\/b> <br>Urban  : 80 <br>Assault: 335 <br>Murder : 15.4","<b> Georgia <\/b> <br>Urban  : 60 <br>Assault: 211 <br>Murder : 17.4","<b> Hawaii <\/b> <br>Urban  : 83 <br>Assault: 46 <br>Murder : 5.3","<b> Idaho <\/b> <br>Urban  : 54 <br>Assault: 120 <br>Murder : 2.6","<b> Illinois <\/b> <br>Urban  : 83 <br>Assault: 249 <br>Murder : 10.4","<b> Indiana <\/b> <br>Urban  : 65 <br>Assault: 113 <br>Murder : 7.2","<b> Iowa <\/b> <br>Urban  : 57 <br>Assault: 56 <br>Murder : 2.2","<b> Kansas <\/b> <br>Urban  : 66 <br>Assault: 115 <br>Murder : 6","<b> Kentucky <\/b> <br>Urban  : 52 <br>Assault: 109 <br>Murder : 9.7","<b> Louisiana <\/b> <br>Urban  : 66 <br>Assault: 249 <br>Murder : 15.4","<b> Maine <\/b> <br>Urban  : 51 <br>Assault: 83 <br>Murder : 2.1","<b> Maryland <\/b> <br>Urban  : 67 <br>Assault: 300 <br>Murder : 11.3","<b> Massachusetts <\/b> <br>Urban  : 85 <br>Assault: 149 <br>Murder : 4.4","<b> Michigan <\/b> <br>Urban  : 74 <br>Assault: 255 <br>Murder : 12.1","<b> Minnesota <\/b> <br>Urban  : 66 <br>Assault: 72 <br>Murder : 2.7","<b> Mississippi <\/b> <br>Urban  : 44 <br>Assault: 259 <br>Murder : 16.1","<b> Missouri <\/b> <br>Urban  : 70 <br>Assault: 178 <br>Murder : 9","<b> Montana <\/b> <br>Urban  : 53 <br>Assault: 109 <br>Murder : 6","<b> Nebraska <\/b> <br>Urban  : 62 <br>Assault: 102 <br>Murder : 4.3","<b> Nevada <\/b> <br>Urban  : 81 <br>Assault: 252 <br>Murder : 12.2","<b> New Hampshire <\/b> <br>Urban  : 56 <br>Assault: 57 <br>Murder : 2.1","<b> New Jersey <\/b> <br>Urban  : 89 <br>Assault: 159 <br>Murder : 7.4","<b> New Mexico <\/b> <br>Urban  : 70 <br>Assault: 285 <br>Murder : 11.4","<b> New York <\/b> <br>Urban  : 86 <br>Assault: 254 <br>Murder : 11.1","<b> North Carolina <\/b> <br>Urban  : 45 <br>Assault: 337 <br>Murder : 13","<b> North Dakota <\/b> <br>Urban  : 44 <br>Assault: 45 <br>Murder : 0.8","<b> Ohio <\/b> <br>Urban  : 75 <br>Assault: 120 <br>Murder : 7.3","<b> Oklahoma <\/b> <br>Urban  : 68 <br>Assault: 151 <br>Murder : 6.6","<b> Oregon <\/b> <br>Urban  : 67 <br>Assault: 159 <br>Murder : 4.9","<b> Pennsylvania <\/b> <br>Urban  : 72 <br>Assault: 106 <br>Murder : 6.3","<b> Rhode Island <\/b> <br>Urban  : 87 <br>Assault: 174 <br>Murder : 3.4","<b> South Carolina <\/b> <br>Urban  : 48 <br>Assault: 279 <br>Murder : 14.4","<b> South Dakota <\/b> <br>Urban  : 45 <br>Assault: 86 <br>Murder : 3.8","<b> Tennessee <\/b> <br>Urban  : 59 <br>Assault: 188 <br>Murder : 13.2","<b> Texas <\/b> <br>Urban  : 80 <br>Assault: 201 <br>Murder : 12.7","<b> Utah <\/b> <br>Urban  : 80 <br>Assault: 120 <br>Murder : 3.2","<b> Vermont <\/b> <br>Urban  : 32 <br>Assault: 48 <br>Murder : 2.2","<b> Virginia <\/b> <br>Urban  : 63 <br>Assault: 156 <br>Murder : 8.5","<b> Washington <\/b> <br>Urban  : 73 <br>Assault: 145 <br>Murder : 4","<b> West Virginia <\/b> <br>Urban  : 39 <br>Assault: 81 <br>Murder : 5.7","<b> Wisconsin <\/b> <br>Urban  : 66 <br>Assault: 53 <br>Murder : 2.6","<b> Wyoming <\/b> <br>Urban  : 60 <br>Assault: 161 <br>Murder : 6.8"],"mode":"markers","hoverinfo":["text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text"],"showlegend":false,"marker":{"colorbar":{"title":"Murder Arrests (per 100,000)","ticklen":2},"cmin":0.80000000000000004,"cmax":17.399999999999999,"colorscale":[["0","rgba(68,1,84,1)"],["0.0416666666666667","rgba(70,19,97,1)"],["0.0833333333333333","rgba(72,32,111,1)"],["0.125","rgba(71,45,122,1)"],["0.166666666666667","rgba(68,58,128,1)"],["0.208333333333333","rgba(64,70,135,1)"],["0.25","rgba(60,82,138,1)"],["0.291666666666667","rgba(56,93,140,1)"],["0.333333333333333","rgba(49,104,142,1)"],["0.375","rgba(46,114,142,1)"],["0.416666666666667","rgba(42,123,142,1)"],["0.458333333333333","rgba(38,133,141,1)"],["0.5","rgba(37,144,140,1)"],["0.541666666666667","rgba(33,154,138,1)"],["0.583333333333333","rgba(39,164,133,1)"],["0.625","rgba(47,174,127,1)"],["0.666666666666667","rgba(53,183,121,1)"],["0.708333333333333","rgba(79,191,110,1)"],["0.75","rgba(98,199,98,1)"],["0.791666666666667","rgba(119,207,85,1)"],["0.833333333333333","rgba(147,214,70,1)"],["0.875","rgba(172,220,52,1)"],["0.916666666666667","rgba(199,225,42,1)"],["0.958333333333333","rgba(226,228,40,1)"],["1","rgba(253,231,37,1)"]],"showscale":true,"color":[13.199999999999999,10,8.0999999999999996,8.8000000000000007,9,7.9000000000000004,3.2999999999999998,5.9000000000000004,15.4,17.399999999999999,5.2999999999999998,2.6000000000000001,10.4,7.2000000000000002,2.2000000000000002,6,9.6999999999999993,15.4,2.1000000000000001,11.300000000000001,4.4000000000000004,12.1,2.7000000000000002,16.100000000000001,9,6,4.2999999999999998,12.199999999999999,2.1000000000000001,7.4000000000000004,11.4,11.1,13,0.80000000000000004,7.2999999999999998,6.5999999999999996,4.9000000000000004,6.2999999999999998,3.3999999999999999,14.4,3.7999999999999998,13.199999999999999,12.699999999999999,3.2000000000000002,2.2000000000000002,8.5,4,5.7000000000000002,2.6000000000000001,6.7999999999999998],"size":[13.199999999999999,10,8.0999999999999996,8.8000000000000007,9,7.9000000000000004,3.2999999999999998,5.9000000000000004,15.4,17.399999999999999,5.2999999999999998,2.6000000000000001,10.4,7.2000000000000002,2.2000000000000002,6,9.6999999999999993,15.4,2.1000000000000001,11.300000000000001,4.4000000000000004,12.1,2.7000000000000002,16.100000000000001,9,6,4.2999999999999998,12.199999999999999,2.1000000000000001,7.4000000000000004,11.4,11.1,13,0.80000000000000004,7.2999999999999998,6.5999999999999996,4.9000000000000004,6.2999999999999998,3.3999999999999999,14.4,3.7999999999999998,13.199999999999999,12.699999999999999,3.2000000000000002,2.2000000000000002,8.5,4,5.7000000000000002,2.6000000000000001,6.7999999999999998],"opacity":0.5,"line":{"colorbar":{"title":"","ticklen":2},"cmin":0.80000000000000004,"cmax":17.399999999999999,"colorscale":[["0","rgba(68,1,84,1)"],["0.0416666666666667","rgba(70,19,97,1)"],["0.0833333333333333","rgba(72,32,111,1)"],["0.125","rgba(71,45,122,1)"],["0.166666666666667","rgba(68,58,128,1)"],["0.208333333333333","rgba(64,70,135,1)"],["0.25","rgba(60,82,138,1)"],["0.291666666666667","rgba(56,93,140,1)"],["0.333333333333333","rgba(49,104,142,1)"],["0.375","rgba(46,114,142,1)"],["0.416666666666667","rgba(42,123,142,1)"],["0.458333333333333","rgba(38,133,141,1)"],["0.5","rgba(37,144,140,1)"],["0.541666666666667","rgba(33,154,138,1)"],["0.583333333333333","rgba(39,164,133,1)"],["0.625","rgba(47,174,127,1)"],["0.666666666666667","rgba(53,183,121,1)"],["0.708333333333333","rgba(79,191,110,1)"],["0.75","rgba(98,199,98,1)"],["0.791666666666667","rgba(119,207,85,1)"],["0.833333333333333","rgba(147,214,70,1)"],["0.875","rgba(172,220,52,1)"],["0.916666666666667","rgba(199,225,42,1)"],["0.958333333333333","rgba(226,228,40,1)"],["1","rgba(253,231,37,1)"]],"showscale":false,"color":[13.199999999999999,10,8.0999999999999996,8.8000000000000007,9,7.9000000000000004,3.2999999999999998,5.9000000000000004,15.4,17.399999999999999,5.2999999999999998,2.6000000000000001,10.4,7.2000000000000002,2.2000000000000002,6,9.6999999999999993,15.4,2.1000000000000001,11.300000000000001,4.4000000000000004,12.1,2.7000000000000002,16.100000000000001,9,6,4.2999999999999998,12.199999999999999,2.1000000000000001,7.4000000000000004,11.4,11.1,13,0.80000000000000004,7.2999999999999998,6.5999999999999996,4.9000000000000004,6.2999999999999998,3.3999999999999999,14.4,3.7999999999999998,13.199999999999999,12.699999999999999,3.2000000000000002,2.2000000000000002,8.5,4,5.7000000000000002,2.6000000000000001,6.7999999999999998]}},"type":"scatter","xaxis":"x","yaxis":"y","frame":null},{"x":[32,91],"y":[45,337],"type":"scatter","mode":"markers","opacity":0,"hoverinfo":"none","showlegend":false,"marker":{"colorbar":{"title":"Murder","ticklen":2},"cmin":0.80000000000000004,"cmax":17.399999999999999,"colorscale":[["0","rgba(68,1,84,1)"],["0.0416666666666667","rgba(70,19,97,1)"],["0.0833333333333333","rgba(72,32,111,1)"],["0.125","rgba(71,45,122,1)"],["0.166666666666667","rgba(68,58,128,1)"],["0.208333333333333","rgba(64,70,135,1)"],["0.25","rgba(60,82,138,1)"],["0.291666666666667","rgba(56,93,140,1)"],["0.333333333333333","rgba(49,104,142,1)"],["0.375","rgba(46,114,142,1)"],["0.416666666666667","rgba(42,123,142,1)"],["0.458333333333333","rgba(38,133,141,1)"],["0.5","rgba(37,144,140,1)"],["0.541666666666667","rgba(33,154,138,1)"],["0.583333333333333","rgba(39,164,133,1)"],["0.625","rgba(47,174,127,1)"],["0.666666666666667","rgba(53,183,121,1)"],["0.708333333333333","rgba(79,191,110,1)"],["0.75","rgba(98,199,98,1)"],["0.791666666666667","rgba(119,207,85,1)"],["0.833333333333333","rgba(147,214,70,1)"],["0.875","rgba(172,220,52,1)"],["0.916666666666667","rgba(199,225,42,1)"],["0.958333333333333","rgba(226,228,40,1)"],["1","rgba(253,231,37,1)"]],"showscale":true,"color":[0.80000000000000004,17.399999999999999],"line":{"color":"rgba(255,127,14,1)"}},"xaxis":"x","yaxis":"y","frame":null}],"highlight":{"on":"plotly_click","persistent":false,"dynamic":false,"selectize":false,"opacityDim":0.20000000000000001,"selected":{"opacity":1},"debounce":0},"shinyEvents":["plotly_hover","plotly_click","plotly_selected","plotly_relayout","plotly_brushed","plotly_brushing","plotly_clickannotation","plotly_doubleclick","plotly_deselect","plotly_afterplot","plotly_sunburstclick"],"base_url":"https://plot.ly"},"evals":[],"jsHooks":[]}</script>
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
<div class="plotly html-widget html-fill-item-overflow-hidden html-fill-item" id="htmlwidget-0b6fb29e7719bcda6c75" style="width:672px;height:480px;"></div>
<script type="application/json" data-for="htmlwidget-0b6fb29e7719bcda6c75">{"x":{"visdat":{"20a16e4a46d5":["function () ","plotlyVisDat"]},"cur_data":"20a16e4a46d5","attrs":{"20a16e4a46d5":{"x":[0.048002447704248503,0.044134504049139635,0.038789291332079208,0.05091769718015856,0.0421760656888545,0.045034005378413407,0.045319096154077546,0.046825505706604424,0.0452537111101175,0.043275198795438771,0.041982807775398465,0.040004630828155585,0.051628462528751078,0.04277095655575628,0.046472592427275958,0.044040072457783595,0.04877748850092653,0.03862889356440953,0.042239173473875839,0.052514764942726187,0.043900920526198567,0.045611989855136162,0.039557506026634916,0.043242668874779802,0.044081177955709205,0.044676232676453549,0.038378761254818629,0.048458709300923129,0.03508048337250038,0.044581019108345034,0.039950773255827528,0.044462114799659017,0.05868284731366321,0.040582752707334427,0.046533296855412097,0.05104246262013299,0.051925909726019646,0.04417206866946187,0.046800351821926309,0.044848284338934924,0.044619259414540147,0.042829163938637532,0.046097295887102985,0.044523869357944522,0.044903007190389574,0.046324578300315486,0.044730538450090798,0.041717392337051254,0.033766829509669624,0.045102401352946533,0.039011121252404773,0.041876059094326235,0.038485236497549147,0.040165333322903653,0.0396217721491815,0.041149183869529628,0.04073831350562044,0.048662073573897818,0.041083896258982872,0.047933043807635245,0.043065461612392615,0.043471321663635737,0.044766855771756035,0.044339312326355511,0.044671007400215346,0.045148767639666812,0.042529717727873353,0.051737177777223219,0.049638832327007741,0.045208821935939329,0.052153083668580874,0.052195890584302747,0.043071162516664978,0.04301575732570332,0.047828417180780521,0.039100081503923197,0.046204254245340748,0.042256592352634757,0.046000939262963683,0.050046877135323291,0.040280611409138703,0.046683829817079969,0.04505327612696812,0.042425745882058823,0.043379319177843184,0.044890450337050934,0.048007501459111757,0.040099714107844568,0.041667836193063634,0.050476313483103337,0.041749898309871886,0.040838696731967161,0.039091703497942464,0.045749917762435394,0.042804522702432776,0.056613161262432078,0.047280082871769921,0.045059235995254909,0.044233654133539774,0.04700313323269633,0.050317355734745134,0.063572427764438971,0.043459401166659584,0.035786629811412611,0.052054688161449245,0.04121430303125697,0.050416612039256646,0.050123838435236032,0.037619603900338743,0.04452833176644224,0.039535196442007856,0.048679096132680164,0.046763013327638152,0.039929864957013908,0.038939206376531962,0.043166436256285405,0.047736030817694411,0.033345763627071971,0.0456015231356297,0.043060852755514155,0.045348649709519455,0.043637523133155533,0.040095063156556462,0.045282335911118257,0.050090666616800082,0.043505187549527854,0.049540247224055416,0.043135692295237504,0.037840118911058825,0.046608697464842502,0.045018705015519148,0.050784512870383929,0.045345352812028054,0.049743319559244485,0.05078217635767826,0.041757880237813357,0.040139719005603099,0.038638506858906796,0.044634204194219866,0.037625695707404566,0.045182812675666185,0.047027517551421073,0.039545003025763949,0.042299740206154922,0.034151705132189632,0.044143183522675218,0.050949802758157831,0.040348012615290467,0.048060413973515473,0.040512806583724005,0.047165328965291679,0.048749368752773359,0.052317630856733431,0.043455701855212622,0.045505187966301257,0.049186065239325456,0.049987248354110385,0.045401524369827792,0.052611257657355852,0.044128148844788689,0.046691530666822322,0.037422497233614731,0.049033246867612228,0.04726416122672774,0.035009824850810542,0.037683747471251333,0.054762051674440544,0.039940683464949521,0.035217366967403053,0.044052835558025423,0.046978211315325244,0.045642583234461451,0.050167147269807116,0.043272590292133352,0.045879828541006203,0.043987869478465183,0.043960473578738342,0.04418306827226539,0.040047121078528793,0.044059431254717653,0.053811961466855435,0.061407127214139191,0.047170583727097218,0.041462354272411295,0.037023475869896363,0.042743856586505403,0.051641672070808456,0.039304846580480807,0.039595864742292756,0.038474950594502733,0.053466223055857541,0.046103882307705811,0.040152183924087974,0.040312342793800533,0.053535208116869591,0.047239640095033342,0.050073819594946577,0.052847206945582814,0.038949268265323987,0.042600168368098774,0.036136194596127283,0.037394880420109598,0.046837221936181207,0.042648227173004538,0.048292362924330035,0.053300512458494209,0.046550582839038755,0.046582754996639511,0.04285648630766719,0.045254969531337494,0.036706871130970209,0.040745241665273213,0.039607963441056715,0.040392069886903741,0.052001345124495925,0.038774050060548231,0.042569206802616132,0.043276743326629161,0.041582432025823041,0.047821689561735957,0.041167758852229931,0.056715788239092846,0.051121058805069973,0.040129010477510427,0.041181463314838483,0.041262870798064989,0.058171080021191,0.041254494723294739,0.049036399641932849,0.046527174244513157,0.042064435937152693,0.051240297608155135,0.037890739441293973,0.042036539452414111,0.047033809914153575,0.043893854319396658,0.04282338031772797,0.043047326471283835,0.042123754256888947,0.044672176717496868,0.044811550294698528,0.041721200253256756,0.039923258320874587,0.044206412824398487,0.045039947630062888,0.04995783599810432,0.056293675880199436,0.042269215760945777,0.04355739620240541,0.043023765715451641,0.040653585642783492,0.041131706199979419,0.043719067033362292,0.040390161099722516,0.045329405920270432,0.041325901278819792,0.048264186649607993,0.045676249912410156,0.050836611329280919,0.043667258331162764,0.043790119480234549,0.042960534630127452,0.053968434257446338,0.038431148991888972,0.037597593918602117,0.039281441622939853,0.051140941684370479,0.044958577903756416,0.041058525129713717,0.040422691882759827,0.043729181906737011,0.043446615966908034,0.039110629950947134,0.043463278961530814,0.037948361489181959,0.044658579916771128,0.045294865435542189,0.040076992029629319,0.050386882715540454,0.048944621049341379,0.045772727833589058,0.041103187701723991,0.036453818366523408,0.050483567757758543,0.041646805165527073,0.04096950003476596,0.046728883523496578,0.035802330126585472,0.044375610238708944,0.040055990251262864,0.038182675915959398,0.038286752380280245,0.050553912900481716,0.053220819924285484,0.053172611212619847,0.048824271634451237,0.043362241038404518,0.050495279141397953,0.044559089873132729,0.04180009112194974,0.050323731197277996,0.049004328383191562,0.047023070130478399,0.045727672585450324,0.046004895988771069,0.048218231833893281,0.051518943403945472,0.036142087823172672,0.047712621054752179,0.044947060514309529,0.047455461891221587,0.053570722611875538,0.042804224884183173,0.039295827199076809,0.037808654924567982,0.04710076661450787,0.050126686356761423,0.043087509670203902,0.045318895809953089,0.039318999605330592,0.037634781096723822,0.047507097681124807,0.04930748825955026,0.038193224866758552,0.046189925918979823,0.048644057906808411,0.048889781084686744,0.044818888612935072,0.0492072984563987,0.039673786085296522,0.044748487646115095,0.044670110613524674,0.04915314102496187,0.040087580717822056,0.037848427927023476,0.042234799975142283,0.049731608848157756,0.050985422425644883,0.042873127143141974,0.040195909503168752,0.042248669701893386,0.04264552306376683,0.041277648776772966,0.042935785586597906,0.040542134038055684,0.050499447194051895,0.033902880769151877,0.043093614579251913,0.048379606846361459,0.049183447502702773,0.045770909830660955,0.045228528964574743,0.041539089918403826,0.047767771994734781,0.039470373989851246,0.043234612170869026,0.042535908780052145,0.047556253483478549,0.051428081497467817,0.045382674794870584,0.041954379703617782,0.04592475901133812,0.04126153855843865,0.047505857382679345,0.039392419855469867,0.044851141426700672,0.039285389089299433,0.051284205771928784,0.049341082534417054,0.048213125862789183,0.048398748313715378,0.041928147219481467,0.042178512068215893,0.042228567836539735,0.046334742806326726,0.039467544732936698,0.049937556297675309,0.049535058421468998,0.037805159438672069,0.046316492133978551,0.040359558565689867,0.051934516837827474,0.040294077086457818,0.050534505611993283,0.044559108428810557,0.043954240573637456,0.042217300400278837,0.0442099897918714,0.048464712364699118,0.047525008200232401,0.041952467050179403,0.051693087891597433,0.053853852577904773,0.040198919087246363,0.046147205765591677,0.042038682572105114,0.038126776105922772,0.043810213914896777,0.046197385287180343],"y":[-0.040299562103735524,-0.088230334283796299,-0.039500624823700432,-0.057031890164134603,-0.049328824114834614,-0.04151746667265397,-0.067928673753379049,-0.044826899457047958,-0.034424376114587325,-0.0094739693178192627,-0.053302476953742024,-0.034608280508379129,-0.10835959116471548,-0.013240736387677072,-0.08828052249725532,-0.070732264546847126,-0.10236266443744127,-0.020826708851989211,-0.0092047884648305822,-0.066673680122288165,-0.011960562055818911,-0.079916148848546711,-0.032761361349051041,-0.084339625707645083,-0.0086077467748118495,-0.04045762463437591,-0.00022429551845793707,-0.091318282936248732,-0.020108204341057225,-0.04102890207744718,-0.0086732919615090456,-0.038965679496203651,-0.090745061427136217,-0.038918927395989962,-0.071779240250964368,-0.026072189792532272,-0.058815049714847668,-0.020900320495787616,-0.067406238880285532,-0.011472026440148199,-0.03774292231648424,-0.03184727638399304,-0.048007282569805285,-0.019374993623139394,0.0051788678775668024,-0.056042362254313791,-0.033069590585096412,-0.03340013077723316,-0.012976876116509549,-0.045188806566604497,-0.039966038119770009,-0.055913952174814777,-0.02366857793154142,-0.062387306844919055,-0.068587535959009974,-0.051903525005644269,-0.0672104558509488,-0.029289958606582046,-0.021984150356063169,-0.044368657996655216,-0.041407211530199585,-0.04479428221335674,-0.0055344051108216575,-0.074264108613462443,-0.029740731462724979,-0.054871166293712477,-0.022170059957024577,-0.04092400659385171,-0.065173096591683924,-0.090234749735704056,-0.11169347873019744,-0.071039887157990006,-0.038357441342829028,-0.060939647993056262,-0.055085540267339271,-0.029681991046214731,-0.052184291474396807,-0.019025538447659154,-0.014253067000942175,-0.034983728746662467,-0.037739833645360071,-0.06482760443087901,-0.03617297442210686,-0.035224100029391817,-0.0061640129932066879,-0.021934409858445303,-0.052074027377318047,-0.052129026418441061,-0.00034240865665184791,-0.058988094884154824,-0.062136070901960078,-0.042409980280444216,-0.033704878941016606,-0.058577876290718298,-0.026234905527885457,-0.070910804058930549,-0.049250222789756923,-0.040169405280323055,-0.045382877850045529,-0.043452983215285686,-0.059931908729604973,-0.075074517683840089,-0.018617107536836548,-0.040892178367138612,-0.093852304945178336,-0.041782753260860894,-0.080925821734675343,-0.015785578825374735,-0.032168494469769507,-0.043571959074909669,0.0058609406444976942,-0.049436054620878765,-0.068271726275245651,-0.019032979215061599,0.010291578980259088,-0.030809364933935511,-0.05774615996201575,-0.040970619486109354,-0.047282392345948367,-0.047664598970508024,-0.027428547649620393,-0.096679919674137194,-0.034164680049251342,-0.10116251899136748,-0.057639244394745263,0.0015528556487139987,-0.066607590315037976,-0.025704362387536921,-0.0039429131626173763,-0.041054690779021297,-0.026388660088784287,-0.045618778425739255,-0.037009612067355514,-0.053566938989154704,-0.065047235474962037,-0.018371794752595018,-0.036972448515559392,-0.072468816712229864,-0.055021104571165456,-0.014737415563475402,-0.10681253276225866,-0.050791103385014892,-0.053590760283314567,-0.041429833727732193,-0.039186898277736935,-0.041672406817567356,-0.03954300693985513,-0.095341874637765611,-0.065722211297552,-0.04001522715240894,-0.070390008051165048,-0.044054434923147735,-0.05901371799610388,-0.054171661678783893,-0.052878518298604432,-0.050767424338463207,-0.08314830428707061,0.0011132231898234009,-0.062002517079784797,-0.067908896355172818,-0.07626736253721314,-0.019245458733231424,-0.10761527350785159,-0.052997744118038738,-0.061578521045428797,-0.063646958052385086,-0.013687853759316042,0.017758606899758042,-0.034439051358689181,-0.073889124033446552,-0.066298454831254183,-0.038233879907880831,-0.054287618688009201,-0.052590322310880476,-0.10133349865076657,-0.007363846331948103,-0.052385335811221394,-0.036925729475847338,-0.027446621639555635,-0.059728576845234999,-0.094432397541754795,-0.076215565260114623,-0.061807819866242987,-0.045328681099319305,-0.039801457069294763,-0.042973571268833242,-0.091265628630190318,-0.046721378828597483,-0.080404613987457643,-0.010573190722466753,-0.097652303737288088,-0.053437661626531505,-0.049119556741830543,-0.03943465386178336,-0.019540289795115556,-0.045570929583795883,-0.034646360770414178,-0.027602765307468614,-0.040823157022749239,-0.049205660243297103,-0.053681352289599978,-0.018842055853504486,-0.047238959186788297,-0.049050363519961469,-0.094613904768481694,-0.06605678226452931,-0.023196010544330785,-0.027826552757274563,-0.015093998823705913,-0.039926056402240083,-0.025807766561871521,0.0060016145806473676,0.0071573886321371349,-0.043702104395649713,-0.085964826466628494,-0.027228060965217463,-0.027061957611489912,-0.058609889903928056,-0.023197829747732445,-0.067537407600936211,-0.041482528405386965,-0.083879501734195477,-0.0925083721991206,-0.063947192806665679,-0.036750963120386081,-0.032036455290422032,-0.090607281765684194,-0.033781784048095238,-0.056676604834448904,-0.062431337085282666,-0.023844822408397161,-0.045250943015373656,-0.029632910250469369,-0.095701130224465858,-0.062685181936831952,-0.052643213038320875,-0.032604177559801953,-0.056813250843097365,-0.070706755868230178,-0.052480097935289981,-0.03926211968765745,0.0030563154335810803,-0.0076398839618791641,-0.016018580165078011,-0.056358438956037614,-0.052284923826670326,-0.079091183136820717,-0.03623681510142665,-0.029806810258513713,-0.040223558135678683,-0.01742621742636968,-0.037227933201354806,-0.079430212493670341,-0.053229119590031279,-0.04055078290115146,-0.038366847791338712,-0.039229904950951335,-0.064523828381425896,-0.06740591078115156,-0.03693604734480236,-0.053699340527905016,-0.068154481871255349,-0.04813880182765206,-0.061799199389308584,-0.06060449628505258,-0.048578836307491886,-0.084630519951840233,-0.027603059673495283,0.010147866280479007,-0.0047513481280726591,-0.040728012641342945,-0.054670503316114442,-0.040204201579505862,-0.055302672828390499,0.0085463235652791097,-0.058373449556208136,-0.07163614509374247,-0.043161156225982454,-0.094100565056731797,-0.051474703488979812,-0.080661919952056821,-0.03597876296980887,0.0019139640652373188,-0.066316190107010897,-0.0044074046435818685,0.0049932147951690124,-0.055150789529731438,-0.021639490243246969,-0.012692599013573114,-0.019784697766269423,-0.015799149310372584,-0.023088378786800944,-0.039732299014541422,-0.062813878896209929,-0.10177656366690607,-0.05451946144458255,-0.057130316639634894,-0.032360540155097324,-0.052245002505775441,-0.052913996928272561,-0.06688388932961134,-0.019184000738688044,-0.054575827530392709,-0.057321797798467328,-0.077561561876206317,-0.052914380944870602,-0.084668334488605557,-0.045800167779708016,-0.057638305775082666,-0.025180452550849736,-0.051707837724050278,-0.082583067782189531,-0.058596084190394873,-0.054181127304092719,-0.02497729210136251,-0.058108617748493588,-0.038949111623097402,-0.062950256534102939,-0.033882195893763956,-0.03072147960800433,-0.028645451920396147,-0.04883232756816986,-0.086586208985344804,0.010705754356962137,-0.092683767531139424,-0.051103870729153955,-0.12351458217640454,-0.063873643917108897,-0.030590723277847238,-0.05429766566505051,-0.065661214846073096,-0.050857267187254758,-0.027743604458506044,-0.037635074126151066,-0.062033213401217299,-0.022650296618833207,-0.06727766657690494,-0.062746666730704892,-0.076185660687040496,-0.063819104080355682,-0.046909257074236904,-0.049686196090563559,-0.047901223435507991,-0.011531242950984774,-0.055685807577074246,-0.067828195880091216,-0.057526003772604743,-0.04952469740128071,-0.075825806710839577,-0.032980755735044213,-0.022435645120642864,-0.03075938280780913,-0.046704838113163616,-0.041058163585462722,-0.051697754191844122,-0.021937261919957905,-0.03296699625388632,-0.098752819947914405,-0.0068467971677475589,-0.044447223227802111,-0.028711583986370026,-0.089093649168794795,-0.069027215373040074,-0.074094492261603404,-0.044316046205428318,-0.041971500607498075,-0.07656974406002387,-0.073628180842955207,-0.067364863495135013,-0.055472120896591592,-0.061529871649546854,-0.021415384864267927,-0.049719318774303932,-0.06298835461109889,-0.061588559077310416,-0.05500466414922122,-0.055401669126102525,-0.069237270831914319,-0.036208273469838501,-0.056692446353992905,-0.038002779344492962,-0.070136431293547075,-0.055620721868181143,-0.080325681743375982,-0.037098866671567345,-0.0408204427706629,-0.064058559806687496,-0.074248821662154824,-0.089449642059827958,-0.066139163173791066,-0.059845826855879192,-0.097797233593953717,-0.079907359590885282,-0.061428039327539166,-0.031571616972474764,-0.032911953888416931,-0.039248337322649776,-0.057527676315227698,-0.029257148666375951],"alpha_stroke":1,"sizes":[10,100],"spans":[1,20],"type":"histogram2d","nbinsx":20,"nbinsy":20,"inherit":true}},"layout":{"margin":{"b":40,"l":60,"t":25,"r":10},"xaxis":{"domain":[0,1],"automargin":true,"title":[]},"yaxis":{"domain":[0,1],"automargin":true,"title":[]},"hovermode":"closest","showlegend":false,"legend":{"yanchor":"top","y":0.5}},"source":"A","config":{"modeBarButtonsToAdd":["hoverclosest","hovercompare"],"showSendToCloud":false},"data":[{"colorbar":{"title":"","ticklen":2,"len":0.5,"lenmode":"fraction","y":1,"yanchor":"top"},"colorscale":[["0","rgba(68,1,84,1)"],["0.0416666666666667","rgba(70,19,97,1)"],["0.0833333333333333","rgba(72,32,111,1)"],["0.125","rgba(71,45,122,1)"],["0.166666666666667","rgba(68,58,128,1)"],["0.208333333333333","rgba(64,70,135,1)"],["0.25","rgba(60,82,138,1)"],["0.291666666666667","rgba(56,93,140,1)"],["0.333333333333333","rgba(49,104,142,1)"],["0.375","rgba(46,114,142,1)"],["0.416666666666667","rgba(42,123,142,1)"],["0.458333333333333","rgba(38,133,141,1)"],["0.5","rgba(37,144,140,1)"],["0.541666666666667","rgba(33,154,138,1)"],["0.583333333333333","rgba(39,164,133,1)"],["0.625","rgba(47,174,127,1)"],["0.666666666666667","rgba(53,183,121,1)"],["0.708333333333333","rgba(79,191,110,1)"],["0.75","rgba(98,199,98,1)"],["0.791666666666667","rgba(119,207,85,1)"],["0.833333333333333","rgba(147,214,70,1)"],["0.875","rgba(172,220,52,1)"],["0.916666666666667","rgba(199,225,42,1)"],["0.958333333333333","rgba(226,228,40,1)"],["1","rgba(253,231,37,1)"]],"showscale":true,"x":[0.048002447704248503,0.044134504049139635,0.038789291332079208,0.05091769718015856,0.0421760656888545,0.045034005378413407,0.045319096154077546,0.046825505706604424,0.0452537111101175,0.043275198795438771,0.041982807775398465,0.040004630828155585,0.051628462528751078,0.04277095655575628,0.046472592427275958,0.044040072457783595,0.04877748850092653,0.03862889356440953,0.042239173473875839,0.052514764942726187,0.043900920526198567,0.045611989855136162,0.039557506026634916,0.043242668874779802,0.044081177955709205,0.044676232676453549,0.038378761254818629,0.048458709300923129,0.03508048337250038,0.044581019108345034,0.039950773255827528,0.044462114799659017,0.05868284731366321,0.040582752707334427,0.046533296855412097,0.05104246262013299,0.051925909726019646,0.04417206866946187,0.046800351821926309,0.044848284338934924,0.044619259414540147,0.042829163938637532,0.046097295887102985,0.044523869357944522,0.044903007190389574,0.046324578300315486,0.044730538450090798,0.041717392337051254,0.033766829509669624,0.045102401352946533,0.039011121252404773,0.041876059094326235,0.038485236497549147,0.040165333322903653,0.0396217721491815,0.041149183869529628,0.04073831350562044,0.048662073573897818,0.041083896258982872,0.047933043807635245,0.043065461612392615,0.043471321663635737,0.044766855771756035,0.044339312326355511,0.044671007400215346,0.045148767639666812,0.042529717727873353,0.051737177777223219,0.049638832327007741,0.045208821935939329,0.052153083668580874,0.052195890584302747,0.043071162516664978,0.04301575732570332,0.047828417180780521,0.039100081503923197,0.046204254245340748,0.042256592352634757,0.046000939262963683,0.050046877135323291,0.040280611409138703,0.046683829817079969,0.04505327612696812,0.042425745882058823,0.043379319177843184,0.044890450337050934,0.048007501459111757,0.040099714107844568,0.041667836193063634,0.050476313483103337,0.041749898309871886,0.040838696731967161,0.039091703497942464,0.045749917762435394,0.042804522702432776,0.056613161262432078,0.047280082871769921,0.045059235995254909,0.044233654133539774,0.04700313323269633,0.050317355734745134,0.063572427764438971,0.043459401166659584,0.035786629811412611,0.052054688161449245,0.04121430303125697,0.050416612039256646,0.050123838435236032,0.037619603900338743,0.04452833176644224,0.039535196442007856,0.048679096132680164,0.046763013327638152,0.039929864957013908,0.038939206376531962,0.043166436256285405,0.047736030817694411,0.033345763627071971,0.0456015231356297,0.043060852755514155,0.045348649709519455,0.043637523133155533,0.040095063156556462,0.045282335911118257,0.050090666616800082,0.043505187549527854,0.049540247224055416,0.043135692295237504,0.037840118911058825,0.046608697464842502,0.045018705015519148,0.050784512870383929,0.045345352812028054,0.049743319559244485,0.05078217635767826,0.041757880237813357,0.040139719005603099,0.038638506858906796,0.044634204194219866,0.037625695707404566,0.045182812675666185,0.047027517551421073,0.039545003025763949,0.042299740206154922,0.034151705132189632,0.044143183522675218,0.050949802758157831,0.040348012615290467,0.048060413973515473,0.040512806583724005,0.047165328965291679,0.048749368752773359,0.052317630856733431,0.043455701855212622,0.045505187966301257,0.049186065239325456,0.049987248354110385,0.045401524369827792,0.052611257657355852,0.044128148844788689,0.046691530666822322,0.037422497233614731,0.049033246867612228,0.04726416122672774,0.035009824850810542,0.037683747471251333,0.054762051674440544,0.039940683464949521,0.035217366967403053,0.044052835558025423,0.046978211315325244,0.045642583234461451,0.050167147269807116,0.043272590292133352,0.045879828541006203,0.043987869478465183,0.043960473578738342,0.04418306827226539,0.040047121078528793,0.044059431254717653,0.053811961466855435,0.061407127214139191,0.047170583727097218,0.041462354272411295,0.037023475869896363,0.042743856586505403,0.051641672070808456,0.039304846580480807,0.039595864742292756,0.038474950594502733,0.053466223055857541,0.046103882307705811,0.040152183924087974,0.040312342793800533,0.053535208116869591,0.047239640095033342,0.050073819594946577,0.052847206945582814,0.038949268265323987,0.042600168368098774,0.036136194596127283,0.037394880420109598,0.046837221936181207,0.042648227173004538,0.048292362924330035,0.053300512458494209,0.046550582839038755,0.046582754996639511,0.04285648630766719,0.045254969531337494,0.036706871130970209,0.040745241665273213,0.039607963441056715,0.040392069886903741,0.052001345124495925,0.038774050060548231,0.042569206802616132,0.043276743326629161,0.041582432025823041,0.047821689561735957,0.041167758852229931,0.056715788239092846,0.051121058805069973,0.040129010477510427,0.041181463314838483,0.041262870798064989,0.058171080021191,0.041254494723294739,0.049036399641932849,0.046527174244513157,0.042064435937152693,0.051240297608155135,0.037890739441293973,0.042036539452414111,0.047033809914153575,0.043893854319396658,0.04282338031772797,0.043047326471283835,0.042123754256888947,0.044672176717496868,0.044811550294698528,0.041721200253256756,0.039923258320874587,0.044206412824398487,0.045039947630062888,0.04995783599810432,0.056293675880199436,0.042269215760945777,0.04355739620240541,0.043023765715451641,0.040653585642783492,0.041131706199979419,0.043719067033362292,0.040390161099722516,0.045329405920270432,0.041325901278819792,0.048264186649607993,0.045676249912410156,0.050836611329280919,0.043667258331162764,0.043790119480234549,0.042960534630127452,0.053968434257446338,0.038431148991888972,0.037597593918602117,0.039281441622939853,0.051140941684370479,0.044958577903756416,0.041058525129713717,0.040422691882759827,0.043729181906737011,0.043446615966908034,0.039110629950947134,0.043463278961530814,0.037948361489181959,0.044658579916771128,0.045294865435542189,0.040076992029629319,0.050386882715540454,0.048944621049341379,0.045772727833589058,0.041103187701723991,0.036453818366523408,0.050483567757758543,0.041646805165527073,0.04096950003476596,0.046728883523496578,0.035802330126585472,0.044375610238708944,0.040055990251262864,0.038182675915959398,0.038286752380280245,0.050553912900481716,0.053220819924285484,0.053172611212619847,0.048824271634451237,0.043362241038404518,0.050495279141397953,0.044559089873132729,0.04180009112194974,0.050323731197277996,0.049004328383191562,0.047023070130478399,0.045727672585450324,0.046004895988771069,0.048218231833893281,0.051518943403945472,0.036142087823172672,0.047712621054752179,0.044947060514309529,0.047455461891221587,0.053570722611875538,0.042804224884183173,0.039295827199076809,0.037808654924567982,0.04710076661450787,0.050126686356761423,0.043087509670203902,0.045318895809953089,0.039318999605330592,0.037634781096723822,0.047507097681124807,0.04930748825955026,0.038193224866758552,0.046189925918979823,0.048644057906808411,0.048889781084686744,0.044818888612935072,0.0492072984563987,0.039673786085296522,0.044748487646115095,0.044670110613524674,0.04915314102496187,0.040087580717822056,0.037848427927023476,0.042234799975142283,0.049731608848157756,0.050985422425644883,0.042873127143141974,0.040195909503168752,0.042248669701893386,0.04264552306376683,0.041277648776772966,0.042935785586597906,0.040542134038055684,0.050499447194051895,0.033902880769151877,0.043093614579251913,0.048379606846361459,0.049183447502702773,0.045770909830660955,0.045228528964574743,0.041539089918403826,0.047767771994734781,0.039470373989851246,0.043234612170869026,0.042535908780052145,0.047556253483478549,0.051428081497467817,0.045382674794870584,0.041954379703617782,0.04592475901133812,0.04126153855843865,0.047505857382679345,0.039392419855469867,0.044851141426700672,0.039285389089299433,0.051284205771928784,0.049341082534417054,0.048213125862789183,0.048398748313715378,0.041928147219481467,0.042178512068215893,0.042228567836539735,0.046334742806326726,0.039467544732936698,0.049937556297675309,0.049535058421468998,0.037805159438672069,0.046316492133978551,0.040359558565689867,0.051934516837827474,0.040294077086457818,0.050534505611993283,0.044559108428810557,0.043954240573637456,0.042217300400278837,0.0442099897918714,0.048464712364699118,0.047525008200232401,0.041952467050179403,0.051693087891597433,0.053853852577904773,0.040198919087246363,0.046147205765591677,0.042038682572105114,0.038126776105922772,0.043810213914896777,0.046197385287180343],"y":[-0.040299562103735524,-0.088230334283796299,-0.039500624823700432,-0.057031890164134603,-0.049328824114834614,-0.04151746667265397,-0.067928673753379049,-0.044826899457047958,-0.034424376114587325,-0.0094739693178192627,-0.053302476953742024,-0.034608280508379129,-0.10835959116471548,-0.013240736387677072,-0.08828052249725532,-0.070732264546847126,-0.10236266443744127,-0.020826708851989211,-0.0092047884648305822,-0.066673680122288165,-0.011960562055818911,-0.079916148848546711,-0.032761361349051041,-0.084339625707645083,-0.0086077467748118495,-0.04045762463437591,-0.00022429551845793707,-0.091318282936248732,-0.020108204341057225,-0.04102890207744718,-0.0086732919615090456,-0.038965679496203651,-0.090745061427136217,-0.038918927395989962,-0.071779240250964368,-0.026072189792532272,-0.058815049714847668,-0.020900320495787616,-0.067406238880285532,-0.011472026440148199,-0.03774292231648424,-0.03184727638399304,-0.048007282569805285,-0.019374993623139394,0.0051788678775668024,-0.056042362254313791,-0.033069590585096412,-0.03340013077723316,-0.012976876116509549,-0.045188806566604497,-0.039966038119770009,-0.055913952174814777,-0.02366857793154142,-0.062387306844919055,-0.068587535959009974,-0.051903525005644269,-0.0672104558509488,-0.029289958606582046,-0.021984150356063169,-0.044368657996655216,-0.041407211530199585,-0.04479428221335674,-0.0055344051108216575,-0.074264108613462443,-0.029740731462724979,-0.054871166293712477,-0.022170059957024577,-0.04092400659385171,-0.065173096591683924,-0.090234749735704056,-0.11169347873019744,-0.071039887157990006,-0.038357441342829028,-0.060939647993056262,-0.055085540267339271,-0.029681991046214731,-0.052184291474396807,-0.019025538447659154,-0.014253067000942175,-0.034983728746662467,-0.037739833645360071,-0.06482760443087901,-0.03617297442210686,-0.035224100029391817,-0.0061640129932066879,-0.021934409858445303,-0.052074027377318047,-0.052129026418441061,-0.00034240865665184791,-0.058988094884154824,-0.062136070901960078,-0.042409980280444216,-0.033704878941016606,-0.058577876290718298,-0.026234905527885457,-0.070910804058930549,-0.049250222789756923,-0.040169405280323055,-0.045382877850045529,-0.043452983215285686,-0.059931908729604973,-0.075074517683840089,-0.018617107536836548,-0.040892178367138612,-0.093852304945178336,-0.041782753260860894,-0.080925821734675343,-0.015785578825374735,-0.032168494469769507,-0.043571959074909669,0.0058609406444976942,-0.049436054620878765,-0.068271726275245651,-0.019032979215061599,0.010291578980259088,-0.030809364933935511,-0.05774615996201575,-0.040970619486109354,-0.047282392345948367,-0.047664598970508024,-0.027428547649620393,-0.096679919674137194,-0.034164680049251342,-0.10116251899136748,-0.057639244394745263,0.0015528556487139987,-0.066607590315037976,-0.025704362387536921,-0.0039429131626173763,-0.041054690779021297,-0.026388660088784287,-0.045618778425739255,-0.037009612067355514,-0.053566938989154704,-0.065047235474962037,-0.018371794752595018,-0.036972448515559392,-0.072468816712229864,-0.055021104571165456,-0.014737415563475402,-0.10681253276225866,-0.050791103385014892,-0.053590760283314567,-0.041429833727732193,-0.039186898277736935,-0.041672406817567356,-0.03954300693985513,-0.095341874637765611,-0.065722211297552,-0.04001522715240894,-0.070390008051165048,-0.044054434923147735,-0.05901371799610388,-0.054171661678783893,-0.052878518298604432,-0.050767424338463207,-0.08314830428707061,0.0011132231898234009,-0.062002517079784797,-0.067908896355172818,-0.07626736253721314,-0.019245458733231424,-0.10761527350785159,-0.052997744118038738,-0.061578521045428797,-0.063646958052385086,-0.013687853759316042,0.017758606899758042,-0.034439051358689181,-0.073889124033446552,-0.066298454831254183,-0.038233879907880831,-0.054287618688009201,-0.052590322310880476,-0.10133349865076657,-0.007363846331948103,-0.052385335811221394,-0.036925729475847338,-0.027446621639555635,-0.059728576845234999,-0.094432397541754795,-0.076215565260114623,-0.061807819866242987,-0.045328681099319305,-0.039801457069294763,-0.042973571268833242,-0.091265628630190318,-0.046721378828597483,-0.080404613987457643,-0.010573190722466753,-0.097652303737288088,-0.053437661626531505,-0.049119556741830543,-0.03943465386178336,-0.019540289795115556,-0.045570929583795883,-0.034646360770414178,-0.027602765307468614,-0.040823157022749239,-0.049205660243297103,-0.053681352289599978,-0.018842055853504486,-0.047238959186788297,-0.049050363519961469,-0.094613904768481694,-0.06605678226452931,-0.023196010544330785,-0.027826552757274563,-0.015093998823705913,-0.039926056402240083,-0.025807766561871521,0.0060016145806473676,0.0071573886321371349,-0.043702104395649713,-0.085964826466628494,-0.027228060965217463,-0.027061957611489912,-0.058609889903928056,-0.023197829747732445,-0.067537407600936211,-0.041482528405386965,-0.083879501734195477,-0.0925083721991206,-0.063947192806665679,-0.036750963120386081,-0.032036455290422032,-0.090607281765684194,-0.033781784048095238,-0.056676604834448904,-0.062431337085282666,-0.023844822408397161,-0.045250943015373656,-0.029632910250469369,-0.095701130224465858,-0.062685181936831952,-0.052643213038320875,-0.032604177559801953,-0.056813250843097365,-0.070706755868230178,-0.052480097935289981,-0.03926211968765745,0.0030563154335810803,-0.0076398839618791641,-0.016018580165078011,-0.056358438956037614,-0.052284923826670326,-0.079091183136820717,-0.03623681510142665,-0.029806810258513713,-0.040223558135678683,-0.01742621742636968,-0.037227933201354806,-0.079430212493670341,-0.053229119590031279,-0.04055078290115146,-0.038366847791338712,-0.039229904950951335,-0.064523828381425896,-0.06740591078115156,-0.03693604734480236,-0.053699340527905016,-0.068154481871255349,-0.04813880182765206,-0.061799199389308584,-0.06060449628505258,-0.048578836307491886,-0.084630519951840233,-0.027603059673495283,0.010147866280479007,-0.0047513481280726591,-0.040728012641342945,-0.054670503316114442,-0.040204201579505862,-0.055302672828390499,0.0085463235652791097,-0.058373449556208136,-0.07163614509374247,-0.043161156225982454,-0.094100565056731797,-0.051474703488979812,-0.080661919952056821,-0.03597876296980887,0.0019139640652373188,-0.066316190107010897,-0.0044074046435818685,0.0049932147951690124,-0.055150789529731438,-0.021639490243246969,-0.012692599013573114,-0.019784697766269423,-0.015799149310372584,-0.023088378786800944,-0.039732299014541422,-0.062813878896209929,-0.10177656366690607,-0.05451946144458255,-0.057130316639634894,-0.032360540155097324,-0.052245002505775441,-0.052913996928272561,-0.06688388932961134,-0.019184000738688044,-0.054575827530392709,-0.057321797798467328,-0.077561561876206317,-0.052914380944870602,-0.084668334488605557,-0.045800167779708016,-0.057638305775082666,-0.025180452550849736,-0.051707837724050278,-0.082583067782189531,-0.058596084190394873,-0.054181127304092719,-0.02497729210136251,-0.058108617748493588,-0.038949111623097402,-0.062950256534102939,-0.033882195893763956,-0.03072147960800433,-0.028645451920396147,-0.04883232756816986,-0.086586208985344804,0.010705754356962137,-0.092683767531139424,-0.051103870729153955,-0.12351458217640454,-0.063873643917108897,-0.030590723277847238,-0.05429766566505051,-0.065661214846073096,-0.050857267187254758,-0.027743604458506044,-0.037635074126151066,-0.062033213401217299,-0.022650296618833207,-0.06727766657690494,-0.062746666730704892,-0.076185660687040496,-0.063819104080355682,-0.046909257074236904,-0.049686196090563559,-0.047901223435507991,-0.011531242950984774,-0.055685807577074246,-0.067828195880091216,-0.057526003772604743,-0.04952469740128071,-0.075825806710839577,-0.032980755735044213,-0.022435645120642864,-0.03075938280780913,-0.046704838113163616,-0.041058163585462722,-0.051697754191844122,-0.021937261919957905,-0.03296699625388632,-0.098752819947914405,-0.0068467971677475589,-0.044447223227802111,-0.028711583986370026,-0.089093649168794795,-0.069027215373040074,-0.074094492261603404,-0.044316046205428318,-0.041971500607498075,-0.07656974406002387,-0.073628180842955207,-0.067364863495135013,-0.055472120896591592,-0.061529871649546854,-0.021415384864267927,-0.049719318774303932,-0.06298835461109889,-0.061588559077310416,-0.05500466414922122,-0.055401669126102525,-0.069237270831914319,-0.036208273469838501,-0.056692446353992905,-0.038002779344492962,-0.070136431293547075,-0.055620721868181143,-0.080325681743375982,-0.037098866671567345,-0.0408204427706629,-0.064058559806687496,-0.074248821662154824,-0.089449642059827958,-0.066139163173791066,-0.059845826855879192,-0.097797233593953717,-0.079907359590885282,-0.061428039327539166,-0.031571616972474764,-0.032911953888416931,-0.039248337322649776,-0.057527676315227698,-0.029257148666375951],"type":"histogram2d","nbinsx":20,"nbinsy":20,"marker":{"line":{"color":"rgba(31,119,180,1)"}},"xaxis":"x","yaxis":"y","frame":null}],"highlight":{"on":"plotly_click","persistent":false,"dynamic":false,"selectize":false,"opacityDim":0.20000000000000001,"selected":{"opacity":1},"debounce":0},"shinyEvents":["plotly_hover","plotly_click","plotly_selected","plotly_relayout","plotly_brushed","plotly_brushing","plotly_clickannotation","plotly_doubleclick","plotly_deselect","plotly_afterplot","plotly_sunburstclick"],"base_url":"https://plot.ly"},"evals":[],"jsHooks":[]}</script>
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
##   10.887805    2.181328   -3.322781
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
## -28.606  -5.866  -0.684   6.033  46.496 
## 
## Coefficients:
##              Estimate Std. Error t value Pr(>|t|)    
## (Intercept)  18.79371    1.22136  15.387  < 2e-16 ***
## x             1.27897    0.20418   6.264 5.59e-10 ***
## fo.L         23.10034    1.06631  21.664  < 2e-16 ***
## fo.Q          7.88356    0.94164   8.372  < 2e-16 ***
## fo.C         -0.07374    0.73117  -0.101    0.920    
## fo^4          0.08209    0.56711   0.145    0.885    
## fuB         -24.30839    0.59121 -41.116  < 2e-16 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 9.322 on 993 degrees of freedom
## Multiple R-squared:  0.7091,	Adjusted R-squared:  0.7074 
## F-statistic: 403.5 on 6 and 993 DF,  p-value: < 2.2e-16
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
##   Estimate Std. Error t value Pr(>|t|)    
## x  1.27897   0.400706 3.19179  0.03316 *  
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## RMSE: 9.28967     Adj. R2: 0.707384
##                 Within R2: 0.03801
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
## x  1.02792   0.570424 1.80204  0.10505 
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## RMSE: 3.5052     Adj. R2: 0.958171
##                Within R2: 0.151641
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
## -8.6528 -1.4293  0.0413  1.5571 10.9282 
## 
## Coefficients:
##              Estimate Std. Error t value Pr(>|t|)    
## (Intercept)  14.06324    0.62628  22.455  < 2e-16 ***
## x             2.67169    0.11102  24.065  < 2e-16 ***
## fo.L         26.61764    1.77554  14.991  < 2e-16 ***
## fo.Q         10.83497    1.56621   6.918 8.26e-12 ***
## fo.C          3.75762    1.18245   3.178  0.00153 ** 
## fo^4          0.84591    0.91694   0.923  0.35647    
## fuB         -13.11239    0.83905 -15.628  < 2e-16 ***
## x:fo.L        4.78362    0.31550  15.162  < 2e-16 ***
## x:fo.Q        1.66583    0.27794   5.993 2.88e-09 ***
## x:fo.C        0.17324    0.20921   0.828  0.40783    
## x:fo^4       -0.02364    0.16111  -0.147  0.88336    
## x:fuB        -2.86196    0.14848 -19.275  < 2e-16 ***
## fo.L:fuB    -25.47630    2.35067 -10.838  < 2e-16 ***
## fo.Q:fuB    -10.35221    2.07860  -4.980 7.50e-07 ***
## fo.C:fuB     -3.01887    1.61877  -1.865  0.06249 .  
## fo^4:fuB     -0.17002    1.27017  -0.134  0.89354    
## x:fo.L:fuB   -5.09252    0.41742 -12.200  < 2e-16 ***
## x:fo.Q:fuB   -1.81497    0.36864  -4.923 9.97e-07 ***
## x:fo.C:fuB   -0.32208    0.28518  -1.129  0.25901    
## x:fo^4:fuB   -0.06217    0.22242  -0.280  0.77992    
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 2.625 on 980 degrees of freedom
## Multiple R-squared:  0.9772,	Adjusted R-squared:  0.9768 
## F-statistic:  2215 on 19 and 980 DF,  p-value: < 2.2e-16
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
## 23 
## 23
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
## 1  -1.0553986 0.79313265 2.128911072
## 5  -3.4563211 0.03168028 0.151716723
## 15  0.2423741 0.04497063 0.001418233
## 23  2.0255414 0.02829720 0.055229894
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
##        dfb.1_       dfb.x       dffit     cov.r      cook.d        hat
## 1  1.59997737 -2.03370830 -2.06653832 4.8051752 2.128911072 0.79313265
## 2  0.04649812 -0.03278573  0.04924212 1.1013071 0.001243428 0.04490737
## 3 -0.14604380  0.08626803 -0.16914400 1.0449519 0.014373654 0.03378961
## 4 -0.04336266  0.02609955 -0.04972464 1.0884084 0.001267313 0.03450659
## 5 -0.52055985  0.28707946 -0.62517157 0.6224597 0.151716723 0.03168028
## 6  0.02211689  0.08676102  0.21969778 0.9997028 0.023769928 0.02961926
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
## W = 0.97074, p-value = 0.3797
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
## BP = 0.2643, df = 1, p-value = 0.6072
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



