
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
* *confidence interval* range your statistic varies across different samples.
* *p-value* the probability you would see something as extreme as your statistic when sampling from the null distribution.
* *null distribution*: the sampling distribution of the statistic under the null hypothesis (assuming your null hypothesis was true).

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
## [1] 0.6090226
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
<div class="plotly html-widget html-fill-item-overflow-hidden html-fill-item" id="htmlwidget-f1bb3ac3c86a3faa4542" style="width:672px;height:480px;"></div>
<script type="application/json" data-for="htmlwidget-f1bb3ac3c86a3faa4542">{"x":{"visdat":{"166e189569ca":["function () ","plotlyVisDat"]},"cur_data":"166e189569ca","attrs":{"166e189569ca":{"x":{},"y":{},"text":{},"mode":"markers","hoverinfo":"text","showlegend":false,"marker":{"size":{},"opacity":0.5,"showscale":true,"colorbar":{"title":"Murder Arrests (per 100,000)"}},"color":{},"alpha_stroke":1,"sizes":[10,100],"spans":[1,20],"type":"scatter"}},"layout":{"margin":{"b":40,"l":60,"t":25,"r":10},"title":"Crime and Urbanization in America 1975","xaxis":{"domain":[0,1],"automargin":true,"title":"Percent of People in an Urban Area"},"yaxis":{"domain":[0,1],"automargin":true,"title":"Assault Arrests per 100,000 People"},"hovermode":"closest","showlegend":false},"source":"A","config":{"modeBarButtonsToAdd":["hoverclosest","hovercompare"],"showSendToCloud":false},"data":[{"x":[58,48,80,50,91,78,77,72,80,60,83,54,83,65,57,66,52,66,51,67,85,74,66,44,70,53,62,81,56,89,70,86,45,44,75,68,67,72,87,48,45,59,80,80,32,63,73,39,66,60],"y":[236,263,294,190,276,204,110,238,335,211,46,120,249,113,56,115,109,249,83,300,149,255,72,259,178,109,102,252,57,159,285,254,337,45,120,151,159,106,174,279,86,188,201,120,48,156,145,81,53,161],"text":["<b> Alabama <\/b> <br>Urban  : 58 <br>Assault: 236 <br>Murder : 13.2","<b> Alaska <\/b> <br>Urban  : 48 <br>Assault: 263 <br>Murder : 10","<b> Arizona <\/b> <br>Urban  : 80 <br>Assault: 294 <br>Murder : 8.1","<b> Arkansas <\/b> <br>Urban  : 50 <br>Assault: 190 <br>Murder : 8.8","<b> California <\/b> <br>Urban  : 91 <br>Assault: 276 <br>Murder : 9","<b> Colorado <\/b> <br>Urban  : 78 <br>Assault: 204 <br>Murder : 7.9","<b> Connecticut <\/b> <br>Urban  : 77 <br>Assault: 110 <br>Murder : 3.3","<b> Delaware <\/b> <br>Urban  : 72 <br>Assault: 238 <br>Murder : 5.9","<b> Florida <\/b> <br>Urban  : 80 <br>Assault: 335 <br>Murder : 15.4","<b> Georgia <\/b> <br>Urban  : 60 <br>Assault: 211 <br>Murder : 17.4","<b> Hawaii <\/b> <br>Urban  : 83 <br>Assault: 46 <br>Murder : 5.3","<b> Idaho <\/b> <br>Urban  : 54 <br>Assault: 120 <br>Murder : 2.6","<b> Illinois <\/b> <br>Urban  : 83 <br>Assault: 249 <br>Murder : 10.4","<b> Indiana <\/b> <br>Urban  : 65 <br>Assault: 113 <br>Murder : 7.2","<b> Iowa <\/b> <br>Urban  : 57 <br>Assault: 56 <br>Murder : 2.2","<b> Kansas <\/b> <br>Urban  : 66 <br>Assault: 115 <br>Murder : 6","<b> Kentucky <\/b> <br>Urban  : 52 <br>Assault: 109 <br>Murder : 9.7","<b> Louisiana <\/b> <br>Urban  : 66 <br>Assault: 249 <br>Murder : 15.4","<b> Maine <\/b> <br>Urban  : 51 <br>Assault: 83 <br>Murder : 2.1","<b> Maryland <\/b> <br>Urban  : 67 <br>Assault: 300 <br>Murder : 11.3","<b> Massachusetts <\/b> <br>Urban  : 85 <br>Assault: 149 <br>Murder : 4.4","<b> Michigan <\/b> <br>Urban  : 74 <br>Assault: 255 <br>Murder : 12.1","<b> Minnesota <\/b> <br>Urban  : 66 <br>Assault: 72 <br>Murder : 2.7","<b> Mississippi <\/b> <br>Urban  : 44 <br>Assault: 259 <br>Murder : 16.1","<b> Missouri <\/b> <br>Urban  : 70 <br>Assault: 178 <br>Murder : 9","<b> Montana <\/b> <br>Urban  : 53 <br>Assault: 109 <br>Murder : 6","<b> Nebraska <\/b> <br>Urban  : 62 <br>Assault: 102 <br>Murder : 4.3","<b> Nevada <\/b> <br>Urban  : 81 <br>Assault: 252 <br>Murder : 12.2","<b> New Hampshire <\/b> <br>Urban  : 56 <br>Assault: 57 <br>Murder : 2.1","<b> New Jersey <\/b> <br>Urban  : 89 <br>Assault: 159 <br>Murder : 7.4","<b> New Mexico <\/b> <br>Urban  : 70 <br>Assault: 285 <br>Murder : 11.4","<b> New York <\/b> <br>Urban  : 86 <br>Assault: 254 <br>Murder : 11.1","<b> North Carolina <\/b> <br>Urban  : 45 <br>Assault: 337 <br>Murder : 13","<b> North Dakota <\/b> <br>Urban  : 44 <br>Assault: 45 <br>Murder : 0.8","<b> Ohio <\/b> <br>Urban  : 75 <br>Assault: 120 <br>Murder : 7.3","<b> Oklahoma <\/b> <br>Urban  : 68 <br>Assault: 151 <br>Murder : 6.6","<b> Oregon <\/b> <br>Urban  : 67 <br>Assault: 159 <br>Murder : 4.9","<b> Pennsylvania <\/b> <br>Urban  : 72 <br>Assault: 106 <br>Murder : 6.3","<b> Rhode Island <\/b> <br>Urban  : 87 <br>Assault: 174 <br>Murder : 3.4","<b> South Carolina <\/b> <br>Urban  : 48 <br>Assault: 279 <br>Murder : 14.4","<b> South Dakota <\/b> <br>Urban  : 45 <br>Assault: 86 <br>Murder : 3.8","<b> Tennessee <\/b> <br>Urban  : 59 <br>Assault: 188 <br>Murder : 13.2","<b> Texas <\/b> <br>Urban  : 80 <br>Assault: 201 <br>Murder : 12.7","<b> Utah <\/b> <br>Urban  : 80 <br>Assault: 120 <br>Murder : 3.2","<b> Vermont <\/b> <br>Urban  : 32 <br>Assault: 48 <br>Murder : 2.2","<b> Virginia <\/b> <br>Urban  : 63 <br>Assault: 156 <br>Murder : 8.5","<b> Washington <\/b> <br>Urban  : 73 <br>Assault: 145 <br>Murder : 4","<b> West Virginia <\/b> <br>Urban  : 39 <br>Assault: 81 <br>Murder : 5.7","<b> Wisconsin <\/b> <br>Urban  : 66 <br>Assault: 53 <br>Murder : 2.6","<b> Wyoming <\/b> <br>Urban  : 60 <br>Assault: 161 <br>Murder : 6.8"],"mode":"markers","hoverinfo":["text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text"],"showlegend":false,"marker":{"colorbar":{"title":"Murder Arrests (per 100,000)","ticklen":2},"cmin":0.80000000000000004,"cmax":17.399999999999999,"colorscale":[["0","rgba(68,1,84,1)"],["0.0416666666666667","rgba(70,19,97,1)"],["0.0833333333333333","rgba(72,32,111,1)"],["0.125","rgba(71,45,122,1)"],["0.166666666666667","rgba(68,58,128,1)"],["0.208333333333333","rgba(64,70,135,1)"],["0.25","rgba(60,82,138,1)"],["0.291666666666667","rgba(56,93,140,1)"],["0.333333333333333","rgba(49,104,142,1)"],["0.375","rgba(46,114,142,1)"],["0.416666666666667","rgba(42,123,142,1)"],["0.458333333333333","rgba(38,133,141,1)"],["0.5","rgba(37,144,140,1)"],["0.541666666666667","rgba(33,154,138,1)"],["0.583333333333333","rgba(39,164,133,1)"],["0.625","rgba(47,174,127,1)"],["0.666666666666667","rgba(53,183,121,1)"],["0.708333333333333","rgba(79,191,110,1)"],["0.75","rgba(98,199,98,1)"],["0.791666666666667","rgba(119,207,85,1)"],["0.833333333333333","rgba(147,214,70,1)"],["0.875","rgba(172,220,52,1)"],["0.916666666666667","rgba(199,225,42,1)"],["0.958333333333333","rgba(226,228,40,1)"],["1","rgba(253,231,37,1)"]],"showscale":true,"color":[13.199999999999999,10,8.0999999999999996,8.8000000000000007,9,7.9000000000000004,3.2999999999999998,5.9000000000000004,15.4,17.399999999999999,5.2999999999999998,2.6000000000000001,10.4,7.2000000000000002,2.2000000000000002,6,9.6999999999999993,15.4,2.1000000000000001,11.300000000000001,4.4000000000000004,12.1,2.7000000000000002,16.100000000000001,9,6,4.2999999999999998,12.199999999999999,2.1000000000000001,7.4000000000000004,11.4,11.1,13,0.80000000000000004,7.2999999999999998,6.5999999999999996,4.9000000000000004,6.2999999999999998,3.3999999999999999,14.4,3.7999999999999998,13.199999999999999,12.699999999999999,3.2000000000000002,2.2000000000000002,8.5,4,5.7000000000000002,2.6000000000000001,6.7999999999999998],"size":[13.199999999999999,10,8.0999999999999996,8.8000000000000007,9,7.9000000000000004,3.2999999999999998,5.9000000000000004,15.4,17.399999999999999,5.2999999999999998,2.6000000000000001,10.4,7.2000000000000002,2.2000000000000002,6,9.6999999999999993,15.4,2.1000000000000001,11.300000000000001,4.4000000000000004,12.1,2.7000000000000002,16.100000000000001,9,6,4.2999999999999998,12.199999999999999,2.1000000000000001,7.4000000000000004,11.4,11.1,13,0.80000000000000004,7.2999999999999998,6.5999999999999996,4.9000000000000004,6.2999999999999998,3.3999999999999999,14.4,3.7999999999999998,13.199999999999999,12.699999999999999,3.2000000000000002,2.2000000000000002,8.5,4,5.7000000000000002,2.6000000000000001,6.7999999999999998],"opacity":0.5,"line":{"colorbar":{"title":"","ticklen":2},"cmin":0.80000000000000004,"cmax":17.399999999999999,"colorscale":[["0","rgba(68,1,84,1)"],["0.0416666666666667","rgba(70,19,97,1)"],["0.0833333333333333","rgba(72,32,111,1)"],["0.125","rgba(71,45,122,1)"],["0.166666666666667","rgba(68,58,128,1)"],["0.208333333333333","rgba(64,70,135,1)"],["0.25","rgba(60,82,138,1)"],["0.291666666666667","rgba(56,93,140,1)"],["0.333333333333333","rgba(49,104,142,1)"],["0.375","rgba(46,114,142,1)"],["0.416666666666667","rgba(42,123,142,1)"],["0.458333333333333","rgba(38,133,141,1)"],["0.5","rgba(37,144,140,1)"],["0.541666666666667","rgba(33,154,138,1)"],["0.583333333333333","rgba(39,164,133,1)"],["0.625","rgba(47,174,127,1)"],["0.666666666666667","rgba(53,183,121,1)"],["0.708333333333333","rgba(79,191,110,1)"],["0.75","rgba(98,199,98,1)"],["0.791666666666667","rgba(119,207,85,1)"],["0.833333333333333","rgba(147,214,70,1)"],["0.875","rgba(172,220,52,1)"],["0.916666666666667","rgba(199,225,42,1)"],["0.958333333333333","rgba(226,228,40,1)"],["1","rgba(253,231,37,1)"]],"showscale":false,"color":[13.199999999999999,10,8.0999999999999996,8.8000000000000007,9,7.9000000000000004,3.2999999999999998,5.9000000000000004,15.4,17.399999999999999,5.2999999999999998,2.6000000000000001,10.4,7.2000000000000002,2.2000000000000002,6,9.6999999999999993,15.4,2.1000000000000001,11.300000000000001,4.4000000000000004,12.1,2.7000000000000002,16.100000000000001,9,6,4.2999999999999998,12.199999999999999,2.1000000000000001,7.4000000000000004,11.4,11.1,13,0.80000000000000004,7.2999999999999998,6.5999999999999996,4.9000000000000004,6.2999999999999998,3.3999999999999999,14.4,3.7999999999999998,13.199999999999999,12.699999999999999,3.2000000000000002,2.2000000000000002,8.5,4,5.7000000000000002,2.6000000000000001,6.7999999999999998]}},"type":"scatter","xaxis":"x","yaxis":"y","frame":null},{"x":[32,91],"y":[45,337],"type":"scatter","mode":"markers","opacity":0,"hoverinfo":"none","showlegend":false,"marker":{"colorbar":{"title":"Murder","ticklen":2},"cmin":0.80000000000000004,"cmax":17.399999999999999,"colorscale":[["0","rgba(68,1,84,1)"],["0.0416666666666667","rgba(70,19,97,1)"],["0.0833333333333333","rgba(72,32,111,1)"],["0.125","rgba(71,45,122,1)"],["0.166666666666667","rgba(68,58,128,1)"],["0.208333333333333","rgba(64,70,135,1)"],["0.25","rgba(60,82,138,1)"],["0.291666666666667","rgba(56,93,140,1)"],["0.333333333333333","rgba(49,104,142,1)"],["0.375","rgba(46,114,142,1)"],["0.416666666666667","rgba(42,123,142,1)"],["0.458333333333333","rgba(38,133,141,1)"],["0.5","rgba(37,144,140,1)"],["0.541666666666667","rgba(33,154,138,1)"],["0.583333333333333","rgba(39,164,133,1)"],["0.625","rgba(47,174,127,1)"],["0.666666666666667","rgba(53,183,121,1)"],["0.708333333333333","rgba(79,191,110,1)"],["0.75","rgba(98,199,98,1)"],["0.791666666666667","rgba(119,207,85,1)"],["0.833333333333333","rgba(147,214,70,1)"],["0.875","rgba(172,220,52,1)"],["0.916666666666667","rgba(199,225,42,1)"],["0.958333333333333","rgba(226,228,40,1)"],["1","rgba(253,231,37,1)"]],"showscale":true,"color":[0.80000000000000004,17.399999999999999],"line":{"color":"rgba(255,127,14,1)"}},"xaxis":"x","yaxis":"y","frame":null}],"highlight":{"on":"plotly_click","persistent":false,"dynamic":false,"selectize":false,"opacityDim":0.20000000000000001,"selected":{"opacity":1},"debounce":0},"shinyEvents":["plotly_hover","plotly_click","plotly_selected","plotly_relayout","plotly_brushed","plotly_brushing","plotly_clickannotation","plotly_doubleclick","plotly_deselect","plotly_afterplot","plotly_sunburstclick"],"base_url":"https://plot.ly"},"evals":[],"jsHooks":[]}</script>
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
<div class="plotly html-widget html-fill-item-overflow-hidden html-fill-item" id="htmlwidget-452038ce696f762f9006" style="width:672px;height:480px;"></div>
<script type="application/json" data-for="htmlwidget-452038ce696f762f9006">{"x":{"visdat":{"166e14f62772":["function () ","plotlyVisDat"]},"cur_data":"166e14f62772","attrs":{"166e14f62772":{"x":[0.036374125294464377,0.05937738989163778,0.043421271757990092,0.034458562789098007,0.047732902396673708,0.047049621293000637,0.049707354250934435,0.04085259866509975,0.048407210656299583,0.043480210555636549,0.038076590805490564,0.037331183748303881,0.04102833979447898,0.045283756944924751,0.047066876917625095,0.04466915304452998,0.038777472947774665,0.045650811838404332,0.05045845669733439,0.044770634101758321,0.041728310182986124,0.03941050039080593,0.045123783034318431,0.049559086564209681,0.053463526852195707,0.039115765409370874,0.049613071036205894,0.048781229853758386,0.035257006665861568,0.044410016513913339,0.043422326736750422,0.043349149268922325,0.052939579145141656,0.049778540215340707,0.041037603121519398,0.048423413474945706,0.040834779003135285,0.045848754397280297,0.042759612680836674,0.038010898785440853,0.042015535404790923,0.046309868020371701,0.050392552915659486,0.044476055269184078,0.034909073460702995,0.041547760869294383,0.038976272651047444,0.042353061185649882,0.044576510068571426,0.040624087353999132,0.050559740003489749,0.04645598804672469,0.038939056998183813,0.044525287042565392,0.042825802269603239,0.04164798894098265,0.049800817033796144,0.045979980610034901,0.041987247879247097,0.041736993941604836,0.046763113796463036,0.045361079893269915,0.040532851765054445,0.04545510181850293,0.042438570032909427,0.044235021019209377,0.044866087903944252,0.042256157639344559,0.048768575309219929,0.05413764124458921,0.037290633714676641,0.041704070005232532,0.039973929899296608,0.051595904802295582,0.045079860634002919,0.046524606766993104,0.050901682957176925,0.044738234304219304,0.045692240831408458,0.040823030836589384,0.044532718914366672,0.049800369316124297,0.042720146701159055,0.035969400837507375,0.041571761009847052,0.049931023877569342,0.043800750346641902,0.045766927636230234,0.043599503712505358,0.044953458452060037,0.043180254168203924,0.041107616215872222,0.043744651227696441,0.047561771505460669,0.040885565893308155,0.036781937749890491,0.050431902047083615,0.042978262759426997,0.051927067051829763,0.04017489173993135,0.047577127288735199,0.04663409569931834,0.054655861346510758,0.04170417585857418,0.053926009664076735,0.051627755361378237,0.044849297136403704,0.038363144713828866,0.039233209922572954,0.039308152879853793,0.047360448455732174,0.047438897814282767,0.044085744795305012,0.046853762037801644,0.040274505692622316,0.038260172057873812,0.042905405108922566,0.040524985333614733,0.040689159734348085,0.039954351928041788,0.051758081005468061,0.046383099847341333,0.043293354997263708,0.048413033443603329,0.046895492132541947,0.040662008124357753,0.035336152143226864,0.042530219837044178,0.055329132245294475,0.041913879509354192,0.044216150500482408,0.041809669718116373,0.037569849143870959,0.054474913455187172,0.040325861732411539,0.044845049052946603,0.048347684351069592,0.041716411051807449,0.037998702927842139,0.040396452552603455,0.040399696348065756,0.035021875218482081,0.053665523159927453,0.04575417482427066,0.049575631340121218,0.048566156550726249,0.056142619472894284,0.03206960326033987,0.04375663006706438,0.04494932247614758,0.035975841021419805,0.040569947660723638,0.042518131127028562,0.043091921638374581,0.045852271270150964,0.042697495440663216,0.048924340132764581,0.044566398970205402,0.04242107860855273,0.037579741927571471,0.039569756939375922,0.040835230254191571,0.038631334136178058,0.043168585449857994,0.044788600660114128,0.041881178441644851,0.043879291420729521,0.043934447090667683,0.044562253248922996,0.043916090200396711,0.044839586441559415,0.040734737239864788,0.047854748274168621,0.037401992921252708,0.036925933336961543,0.041525843189981544,0.040386720894182715,0.037416541788119151,0.045196724454283584,0.046990372105316029,0.040749999117430435,0.051530217366609447,0.052492575338041747,0.045105472192842784,0.042674840299217066,0.042132346643121314,0.042462652377984245,0.040718082231196447,0.046205982979297497,0.043931874638227127,0.041768598341992813,0.049195055192375339,0.048565014813389207,0.047419594712918622,0.045022383106003094,0.043533306369456223,0.041281995872696937,0.046323422909814685,0.046595394105974297,0.046288767156562549,0.041529109526097965,0.045300065789126334,0.034616502109011543,0.048654234205862727,0.049266932558353599,0.035578954724659155,0.045970089614363656,0.040185775162427183,0.04818116495046168,0.042807882056701302,0.051457947451950349,0.047755761884365915,0.039106321813901508,0.041762514707991034,0.0381931597291039,0.043075625289671501,0.046521076177750212,0.048452278960266423,0.044971012719133632,0.043691315653687335,0.041867976256453401,0.044532438813187594,0.046981997318723455,0.051710880425446679,0.048097432117928482,0.044787198556658407,0.040722455049736823,0.050875277951098967,0.038288192388966732,0.044089055957261265,0.049423630494974391,0.037991149409664589,0.04714395342317116,0.04693817245486076,0.045915623259695823,0.045366699211953569,0.043188576784025531,0.044876910700155537,0.045685064163612385,0.035198460694652448,0.046483977758377024,0.046550746729041102,0.054967661454381041,0.04397817281078404,0.041084563676436175,0.040714844479336626,0.046323441817469141,0.036728369411275864,0.040451617805852873,0.04556280444338813,0.030209865923424749,0.04610637961352558,0.039043096101068403,0.038310927787538411,0.043558188326135838,0.039043189520706047,0.05032634015372156,0.048994069245739902,0.040960316836610035,0.042992796801969303,0.042472641803199901,0.04887187570419789,0.047780055613439724,0.041632947070303662,0.044520281047491082,0.034886996993720013,0.047384575162280639,0.043338471779854573,0.044262753883040573,0.042484285082528009,0.048719779155507237,0.049364903700060386,0.043378276506655142,0.03821899581721503,0.043488346360401352,0.051593664829382692,0.050329761921207944,0.040339330017542918,0.040720019478402279,0.04266456530884722,0.039560402617696236,0.04816201687217031,0.042322498947399208,0.039272651651489139,0.048099289203164974,0.044148516574055191,0.04222492692077405,0.04646666493144587,0.037841818453670809,0.04291989383253992,0.040672627541236128,0.05181653054715428,0.053865932491341612,0.041429469029061909,0.045308226060742016,0.042577017541613506,0.043055331017320279,0.065703961259289956,0.04128526997171926,0.045514059965372271,0.050404061524103504,0.040519576134044853,0.04193684955337184,0.051608816533440127,0.050334995073846533,0.041820829517704737,0.049412709601613994,0.043643211227561561,0.043394705510731602,0.045273092179760853,0.039536260510507328,0.039419375626177776,0.042840356854789957,0.038225494145475818,0.045193948864592576,0.043258316226283629,0.049312395528461332,0.048131320675466112,0.040839473359495115,0.043611489799861132,0.044294958221384309,0.042818644053038139,0.049707787073924883,0.040009443684506624,0.052450609415334373,0.039031800804887898,0.043666173420135131,0.047182825319455779,0.04103941630359733,0.049663059111638305,0.043435222497420843,0.038616049312007551,0.040500271245546532,0.046810260450860522,0.047540662824415422,0.043001069954269444,0.052872482808097886,0.046680214721076863,0.048153636400458402,0.044335685217403581,0.049925503419515724,0.032989832755624594,0.046580839165731927,0.040279020667815045,0.03938696300612763,0.043561061228646683,0.050031833088792478,0.04866703948843748,0.037787146621358805,0.040914001878752979,0.049059156391776715,0.046411405309851182,0.041625243906867858,0.044971056148628751,0.039176963659352297,0.043433171295336082,0.037869928351271821,0.043368710848885932,0.043951412415103183,0.039642733576478288,0.045536831099806163,0.041559202490872228,0.042523776783533834,0.048378453640010158,0.03903244433327617,0.046802758790726498,0.047079593115982234,0.052548557608871567,0.049578192604848616,0.048832835759766116,0.063061313890713594,0.041421792506255418,0.04353333422202136,0.044762547078554434,0.050866144638596705,0.038070614287124188,0.058898680054890989,0.048180743497936468,0.041022750722897856,0.03965611022187681,0.045656691990997526,0.045907645235542978,0.040006082460541305,0.051008932196364772,0.046521956414174379,0.038895081775766831,0.049066987509744697,0.039257444103741587,0.043020098744962654,0.033790253322316825,0.04186699258394682,0.043089857600990711,0.055632473000696667,0.036062801947775246,0.043036937944224474,0.042439871639401154,0.043642698527633215,0.048481985754648765,0.045998830707383483],"y":[-0.039299599745572532,-0.071996804268810832,-0.015548083189427152,-0.083032242634594175,-0.091303786746573232,-0.041421740477244201,-0.064805988442676946,-0.0022708134117925922,-0.087511538423846222,-0.014948113769213265,-0.079536249730669681,-0.021858387422623551,-0.051993653886561256,-0.040676185767035723,-0.051249732607560869,-0.038250196903166535,-0.029591915010991295,-0.041109995685041013,-0.074356238283874665,-0.044162766144303874,-0.065053122880667738,-0.017052437656875304,-0.064687837922936989,-0.063443060974883586,-0.064959041348139596,-0.073263479504555987,-0.050091496916352174,-0.043280956580029964,-0.068262123613977987,-0.047674093693037316,-0.032350716181056796,-0.033226044344194239,-0.069388318093722035,-0.089450225387431803,-0.06492871162166626,-0.019015054603128766,-0.023554322537726231,-0.038980364464760969,-0.024474871828868351,-0.045516693647736965,-0.024094013225193032,-0.032919692769989177,-0.08305098899098462,-0.014309231785526955,-0.031835347318327573,-0.05977670854256583,-0.028266565018935659,-0.06006615175235009,-0.036465480881086441,-0.023390211725257921,-0.10049401220115463,-0.048564503004778672,-0.073922384397168431,-0.082398632055741744,-0.055291185362142406,-0.066162889765779928,-0.057423280766434721,-0.048799559044779242,-0.022534808982311492,-0.052336761602067003,-0.033317924004995697,-0.028503113886206105,-0.048544973377472357,-0.077416900586397885,-0.052739861242934907,-0.025379260739785765,-0.061168977390553235,-0.025480609649649717,-0.075860900280976806,-0.047743058547612696,-0.022629332675709841,-0.03364909147235156,-0.010574570876863247,-0.067311855003897289,-0.073915660766134553,-0.11268702062009751,-0.021177657631941925,-0.049135262139873646,-0.020008415493337147,0.0085668781963946783,-0.042346936313228972,-0.068104319819772122,-0.061726143511240721,0.0045270284281021577,-0.073257891349461077,-0.026966109545183432,-0.050839376841390151,-0.045024830042461349,0.006481800133079787,-0.038592291713662977,-0.031749273051868414,-0.033201011445940919,-0.071321343356811701,-0.052527692711604616,-0.0079819258888840401,-0.010525447399124662,-0.064080321339723995,-0.062209679744471655,-0.053246470770465237,-0.0079846376993637416,-0.058369900312638598,-0.038261703195982114,-0.06996470997023807,-0.088768135808512588,-0.10192134523519232,-0.070953365680517702,-0.013440081772782364,-0.045639462793405625,-0.036561971172669738,-0.028290360492078219,-0.07568102750654189,-0.077037106991275014,-0.01964392958342405,-0.039811742979677357,-0.057004734984362336,-0.031686981598999978,-0.10698594200457656,-0.041434759480592748,-0.048978387243190778,-0.041087196597328818,-0.021605585088176324,-0.068942059032313457,-0.027021050116952969,-0.031164612963760926,-0.042031493246932942,-0.08555486272745659,-0.080759425696831921,-0.050703591446379842,-0.077479537642192328,-0.018494706277526737,-0.013683305395230601,-0.0083978271540427248,-0.018175954373148999,-0.063158477256355788,-0.013521187206256053,-0.049394725006529014,-0.00048722834680202241,-0.040231892022197124,-0.025401916887077349,-0.01017215703654493,-0.035701651866409355,-0.04636468383094737,-0.093004750227158109,-0.021927458252540256,-0.042430585656940023,-0.01490014016489662,-0.022037668048786815,-0.035108200453877747,-0.070241335016561712,-0.062036432332645795,-0.026403524392480299,-0.038493071904581511,-0.039531924207354074,-0.086320902620265288,-0.05207359438858962,-0.062407472296045492,-0.060834798536234629,0.019308529005566455,-0.04626578674901681,-0.029152064729485182,-0.018060074525955417,-0.015036310832046514,-0.048391152674677911,-0.074329621642248822,-0.056171316336758488,-0.0089021025451643445,-0.064811886085434686,-0.041254013203543181,-0.038324115016604765,-0.045533585295085784,-0.015731494125795879,-0.068698581480860443,-0.078127422446125888,-0.021768884228808894,-0.063139317197050834,-0.041456414568233901,-0.031926674190691569,-0.02404700735554012,-0.087536316510335235,-0.046362300781015033,-0.038357792718259315,-0.10298295164507425,-0.064469590772599325,-0.029185570581670588,-0.041211535232824774,-0.053727107881090613,-0.055799571551599356,-0.02977800757360502,-0.058885255453579956,-0.032581432505992748,-0.055211512663922942,-0.024071592024103954,-0.072415103407248674,-0.048534667193720987,-0.044840598411775089,-0.010063759939478811,-0.0093848519099842716,-0.055669988427341291,-0.044658622582116926,-0.051402780632578471,-0.048328241509169589,-0.042921574659450817,-0.047735060765611029,-0.0045566853395859058,-0.088890870236496625,-0.0043864556348728019,-0.068773061619465392,-0.0061069479873017349,-0.033640597891941459,-0.066762477300916723,-0.032119134104528262,-0.057318439834688324,-0.041423319314352516,-0.041797250478897222,-0.059882479621472209,-0.022127449500735918,-0.047269444678090279,-0.02254475822188284,-0.032887971088204196,-0.017147531282171877,-0.041205487387278313,-0.014693966234775861,-0.060930255325082408,-0.094309365883746499,-0.068829299146465725,-0.011392858675346751,-0.084199291064148016,-0.088402752870318888,-0.045989723307609011,-0.057597220521871641,-0.063926664916578252,-0.020632066817241657,-0.067772300858310236,-0.049448275321966419,-0.060893092813232026,-0.0093871029173724849,-0.0012651450351101074,-0.080745645793193613,-0.025106885269264159,-0.024652823222933926,-0.046681872719904108,-0.044216347593607784,-0.099399017446161947,-0.0067501789153863534,-0.035069551661483025,-0.034925992749754171,-0.032366479576622781,-0.02374399781510363,-0.06747726277044333,-0.0079589678050147241,-0.029015235131976787,-0.12325729096409403,-0.048612209545655906,-0.014786063062285474,-0.046003622592449028,-0.081427291526761689,-0.055319131517597556,-0.054700407503679396,-0.051745907793286028,-0.026156536683915686,-0.019636489579734073,-0.085727024693304454,-0.055114661089475811,-0.056491656485987272,-0.059194743759408003,0.045075043339403389,-0.071830024569235096,-0.0063419429093640014,-0.059652237987976336,-0.0065931093816853489,-0.031507662091138415,-0.035533868934184622,-0.020768362989490776,-0.040262522316358081,-0.050702549381521772,-0.050961838116399358,-0.040026316559488406,-0.023249351023281965,-0.037992513599398946,-0.0040249338773024586,-0.04340761491965852,-0.05654778274447668,-0.039381923652384111,-0.010767363234688711,-0.068766616890701085,-0.061191540829350945,-0.084168569160721254,-0.01704644808307831,-0.032396467260872454,0.0030984540833157619,-0.038810490989967944,-0.062003664577157433,-0.082754182594347817,-0.051827275573920265,-0.051578356720760825,-0.0023591694497533322,-0.019003848400143405,-0.12084642991798103,-0.03591271867080708,-0.019643726958160919,-0.06423220267377322,0.00012119498108175443,-0.097700337022663591,-0.068705301869948318,-0.064615028659646551,-0.026415823188803055,-0.038473855105265124,-0.085245496889489542,-0.042750965877845923,-0.030457113373292894,-0.034098256295635079,-0.017906970184035347,-0.03706075374902381,-0.061023452430163924,-0.025409181762145027,-0.058450752130671128,-0.02528731061971172,-0.049950674623678644,-0.069569723544593523,-0.038411051408075388,-0.046765610503475732,-0.030204716750590232,-0.06467874935977351,-0.015026969509770598,-0.07361033408849868,-0.036141658411833637,-0.037574481944790371,-0.10972301291750608,-0.034277647075606377,-0.064895520200650772,-0.045754315506869175,-0.029295498545971251,-0.018676471445078179,-0.03461244588231794,-0.051209054368728364,-0.040636843514089117,-0.063159439345971471,-0.064117089677999145,-0.053286011652361881,-0.067292305127078664,-0.037581840397349596,0.039627475560087409,-0.043076144445929575,-0.049744082738657512,-0.051009198653855323,-0.054403539381572233,-0.052700367258547764,-0.079966537514454469,-0.038098457296524835,-0.035710422269090075,-0.05349369141389998,-0.076966304689893836,-0.020461594107834064,-0.064543668617217317,0.0028502801491356294,-0.014631401300668855,-0.001722267825737955,-0.037656877436692819,-0.051948292341288754,-0.019536291594624319,-0.06367885120544077,-0.048527280655448153,-0.10318500466340928,-0.039132862629543776,-0.083708440213426688,-0.047468936288128691,-0.053118792949450204,-0.062933897216933252,-0.081966688394358861,-0.053904254990345839,-0.14092929737097598,-0.035002016915291208,-0.023884900858022643,-0.030637022111679065,-0.089846207206691786,-0.0062868254967957619,-0.13384062055059454,-0.068865546695526386,-0.021774274598987925,-0.011139791923139956,-0.048986656824893504,-0.065865316828721029,-0.03563371473204649,-0.035948782447012245,-0.063970723892676357,-0.010200341311613119,-0.019590883644031765,-0.054057247762111266,-0.035937241887864853,-0.055888940849475044,-0.063812641732039599,0.029502373969897185,-0.069849583955775521,-0.027891155410391808,-0.050772522064501259,-0.059796075852838845,-0.03339608530804359,-0.0097946009208092055,-0.034406354758898423],"alpha_stroke":1,"sizes":[10,100],"spans":[1,20],"type":"histogram2d","nbinsx":20,"nbinsy":20,"inherit":true}},"layout":{"margin":{"b":40,"l":60,"t":25,"r":10},"xaxis":{"domain":[0,1],"automargin":true,"title":[]},"yaxis":{"domain":[0,1],"automargin":true,"title":[]},"hovermode":"closest","showlegend":false,"legend":{"yanchor":"top","y":0.5}},"source":"A","config":{"modeBarButtonsToAdd":["hoverclosest","hovercompare"],"showSendToCloud":false},"data":[{"colorbar":{"title":"","ticklen":2,"len":0.5,"lenmode":"fraction","y":1,"yanchor":"top"},"colorscale":[["0","rgba(68,1,84,1)"],["0.0416666666666667","rgba(70,19,97,1)"],["0.0833333333333333","rgba(72,32,111,1)"],["0.125","rgba(71,45,122,1)"],["0.166666666666667","rgba(68,58,128,1)"],["0.208333333333333","rgba(64,70,135,1)"],["0.25","rgba(60,82,138,1)"],["0.291666666666667","rgba(56,93,140,1)"],["0.333333333333333","rgba(49,104,142,1)"],["0.375","rgba(46,114,142,1)"],["0.416666666666667","rgba(42,123,142,1)"],["0.458333333333333","rgba(38,133,141,1)"],["0.5","rgba(37,144,140,1)"],["0.541666666666667","rgba(33,154,138,1)"],["0.583333333333333","rgba(39,164,133,1)"],["0.625","rgba(47,174,127,1)"],["0.666666666666667","rgba(53,183,121,1)"],["0.708333333333333","rgba(79,191,110,1)"],["0.75","rgba(98,199,98,1)"],["0.791666666666667","rgba(119,207,85,1)"],["0.833333333333333","rgba(147,214,70,1)"],["0.875","rgba(172,220,52,1)"],["0.916666666666667","rgba(199,225,42,1)"],["0.958333333333333","rgba(226,228,40,1)"],["1","rgba(253,231,37,1)"]],"showscale":true,"x":[0.036374125294464377,0.05937738989163778,0.043421271757990092,0.034458562789098007,0.047732902396673708,0.047049621293000637,0.049707354250934435,0.04085259866509975,0.048407210656299583,0.043480210555636549,0.038076590805490564,0.037331183748303881,0.04102833979447898,0.045283756944924751,0.047066876917625095,0.04466915304452998,0.038777472947774665,0.045650811838404332,0.05045845669733439,0.044770634101758321,0.041728310182986124,0.03941050039080593,0.045123783034318431,0.049559086564209681,0.053463526852195707,0.039115765409370874,0.049613071036205894,0.048781229853758386,0.035257006665861568,0.044410016513913339,0.043422326736750422,0.043349149268922325,0.052939579145141656,0.049778540215340707,0.041037603121519398,0.048423413474945706,0.040834779003135285,0.045848754397280297,0.042759612680836674,0.038010898785440853,0.042015535404790923,0.046309868020371701,0.050392552915659486,0.044476055269184078,0.034909073460702995,0.041547760869294383,0.038976272651047444,0.042353061185649882,0.044576510068571426,0.040624087353999132,0.050559740003489749,0.04645598804672469,0.038939056998183813,0.044525287042565392,0.042825802269603239,0.04164798894098265,0.049800817033796144,0.045979980610034901,0.041987247879247097,0.041736993941604836,0.046763113796463036,0.045361079893269915,0.040532851765054445,0.04545510181850293,0.042438570032909427,0.044235021019209377,0.044866087903944252,0.042256157639344559,0.048768575309219929,0.05413764124458921,0.037290633714676641,0.041704070005232532,0.039973929899296608,0.051595904802295582,0.045079860634002919,0.046524606766993104,0.050901682957176925,0.044738234304219304,0.045692240831408458,0.040823030836589384,0.044532718914366672,0.049800369316124297,0.042720146701159055,0.035969400837507375,0.041571761009847052,0.049931023877569342,0.043800750346641902,0.045766927636230234,0.043599503712505358,0.044953458452060037,0.043180254168203924,0.041107616215872222,0.043744651227696441,0.047561771505460669,0.040885565893308155,0.036781937749890491,0.050431902047083615,0.042978262759426997,0.051927067051829763,0.04017489173993135,0.047577127288735199,0.04663409569931834,0.054655861346510758,0.04170417585857418,0.053926009664076735,0.051627755361378237,0.044849297136403704,0.038363144713828866,0.039233209922572954,0.039308152879853793,0.047360448455732174,0.047438897814282767,0.044085744795305012,0.046853762037801644,0.040274505692622316,0.038260172057873812,0.042905405108922566,0.040524985333614733,0.040689159734348085,0.039954351928041788,0.051758081005468061,0.046383099847341333,0.043293354997263708,0.048413033443603329,0.046895492132541947,0.040662008124357753,0.035336152143226864,0.042530219837044178,0.055329132245294475,0.041913879509354192,0.044216150500482408,0.041809669718116373,0.037569849143870959,0.054474913455187172,0.040325861732411539,0.044845049052946603,0.048347684351069592,0.041716411051807449,0.037998702927842139,0.040396452552603455,0.040399696348065756,0.035021875218482081,0.053665523159927453,0.04575417482427066,0.049575631340121218,0.048566156550726249,0.056142619472894284,0.03206960326033987,0.04375663006706438,0.04494932247614758,0.035975841021419805,0.040569947660723638,0.042518131127028562,0.043091921638374581,0.045852271270150964,0.042697495440663216,0.048924340132764581,0.044566398970205402,0.04242107860855273,0.037579741927571471,0.039569756939375922,0.040835230254191571,0.038631334136178058,0.043168585449857994,0.044788600660114128,0.041881178441644851,0.043879291420729521,0.043934447090667683,0.044562253248922996,0.043916090200396711,0.044839586441559415,0.040734737239864788,0.047854748274168621,0.037401992921252708,0.036925933336961543,0.041525843189981544,0.040386720894182715,0.037416541788119151,0.045196724454283584,0.046990372105316029,0.040749999117430435,0.051530217366609447,0.052492575338041747,0.045105472192842784,0.042674840299217066,0.042132346643121314,0.042462652377984245,0.040718082231196447,0.046205982979297497,0.043931874638227127,0.041768598341992813,0.049195055192375339,0.048565014813389207,0.047419594712918622,0.045022383106003094,0.043533306369456223,0.041281995872696937,0.046323422909814685,0.046595394105974297,0.046288767156562549,0.041529109526097965,0.045300065789126334,0.034616502109011543,0.048654234205862727,0.049266932558353599,0.035578954724659155,0.045970089614363656,0.040185775162427183,0.04818116495046168,0.042807882056701302,0.051457947451950349,0.047755761884365915,0.039106321813901508,0.041762514707991034,0.0381931597291039,0.043075625289671501,0.046521076177750212,0.048452278960266423,0.044971012719133632,0.043691315653687335,0.041867976256453401,0.044532438813187594,0.046981997318723455,0.051710880425446679,0.048097432117928482,0.044787198556658407,0.040722455049736823,0.050875277951098967,0.038288192388966732,0.044089055957261265,0.049423630494974391,0.037991149409664589,0.04714395342317116,0.04693817245486076,0.045915623259695823,0.045366699211953569,0.043188576784025531,0.044876910700155537,0.045685064163612385,0.035198460694652448,0.046483977758377024,0.046550746729041102,0.054967661454381041,0.04397817281078404,0.041084563676436175,0.040714844479336626,0.046323441817469141,0.036728369411275864,0.040451617805852873,0.04556280444338813,0.030209865923424749,0.04610637961352558,0.039043096101068403,0.038310927787538411,0.043558188326135838,0.039043189520706047,0.05032634015372156,0.048994069245739902,0.040960316836610035,0.042992796801969303,0.042472641803199901,0.04887187570419789,0.047780055613439724,0.041632947070303662,0.044520281047491082,0.034886996993720013,0.047384575162280639,0.043338471779854573,0.044262753883040573,0.042484285082528009,0.048719779155507237,0.049364903700060386,0.043378276506655142,0.03821899581721503,0.043488346360401352,0.051593664829382692,0.050329761921207944,0.040339330017542918,0.040720019478402279,0.04266456530884722,0.039560402617696236,0.04816201687217031,0.042322498947399208,0.039272651651489139,0.048099289203164974,0.044148516574055191,0.04222492692077405,0.04646666493144587,0.037841818453670809,0.04291989383253992,0.040672627541236128,0.05181653054715428,0.053865932491341612,0.041429469029061909,0.045308226060742016,0.042577017541613506,0.043055331017320279,0.065703961259289956,0.04128526997171926,0.045514059965372271,0.050404061524103504,0.040519576134044853,0.04193684955337184,0.051608816533440127,0.050334995073846533,0.041820829517704737,0.049412709601613994,0.043643211227561561,0.043394705510731602,0.045273092179760853,0.039536260510507328,0.039419375626177776,0.042840356854789957,0.038225494145475818,0.045193948864592576,0.043258316226283629,0.049312395528461332,0.048131320675466112,0.040839473359495115,0.043611489799861132,0.044294958221384309,0.042818644053038139,0.049707787073924883,0.040009443684506624,0.052450609415334373,0.039031800804887898,0.043666173420135131,0.047182825319455779,0.04103941630359733,0.049663059111638305,0.043435222497420843,0.038616049312007551,0.040500271245546532,0.046810260450860522,0.047540662824415422,0.043001069954269444,0.052872482808097886,0.046680214721076863,0.048153636400458402,0.044335685217403581,0.049925503419515724,0.032989832755624594,0.046580839165731927,0.040279020667815045,0.03938696300612763,0.043561061228646683,0.050031833088792478,0.04866703948843748,0.037787146621358805,0.040914001878752979,0.049059156391776715,0.046411405309851182,0.041625243906867858,0.044971056148628751,0.039176963659352297,0.043433171295336082,0.037869928351271821,0.043368710848885932,0.043951412415103183,0.039642733576478288,0.045536831099806163,0.041559202490872228,0.042523776783533834,0.048378453640010158,0.03903244433327617,0.046802758790726498,0.047079593115982234,0.052548557608871567,0.049578192604848616,0.048832835759766116,0.063061313890713594,0.041421792506255418,0.04353333422202136,0.044762547078554434,0.050866144638596705,0.038070614287124188,0.058898680054890989,0.048180743497936468,0.041022750722897856,0.03965611022187681,0.045656691990997526,0.045907645235542978,0.040006082460541305,0.051008932196364772,0.046521956414174379,0.038895081775766831,0.049066987509744697,0.039257444103741587,0.043020098744962654,0.033790253322316825,0.04186699258394682,0.043089857600990711,0.055632473000696667,0.036062801947775246,0.043036937944224474,0.042439871639401154,0.043642698527633215,0.048481985754648765,0.045998830707383483],"y":[-0.039299599745572532,-0.071996804268810832,-0.015548083189427152,-0.083032242634594175,-0.091303786746573232,-0.041421740477244201,-0.064805988442676946,-0.0022708134117925922,-0.087511538423846222,-0.014948113769213265,-0.079536249730669681,-0.021858387422623551,-0.051993653886561256,-0.040676185767035723,-0.051249732607560869,-0.038250196903166535,-0.029591915010991295,-0.041109995685041013,-0.074356238283874665,-0.044162766144303874,-0.065053122880667738,-0.017052437656875304,-0.064687837922936989,-0.063443060974883586,-0.064959041348139596,-0.073263479504555987,-0.050091496916352174,-0.043280956580029964,-0.068262123613977987,-0.047674093693037316,-0.032350716181056796,-0.033226044344194239,-0.069388318093722035,-0.089450225387431803,-0.06492871162166626,-0.019015054603128766,-0.023554322537726231,-0.038980364464760969,-0.024474871828868351,-0.045516693647736965,-0.024094013225193032,-0.032919692769989177,-0.08305098899098462,-0.014309231785526955,-0.031835347318327573,-0.05977670854256583,-0.028266565018935659,-0.06006615175235009,-0.036465480881086441,-0.023390211725257921,-0.10049401220115463,-0.048564503004778672,-0.073922384397168431,-0.082398632055741744,-0.055291185362142406,-0.066162889765779928,-0.057423280766434721,-0.048799559044779242,-0.022534808982311492,-0.052336761602067003,-0.033317924004995697,-0.028503113886206105,-0.048544973377472357,-0.077416900586397885,-0.052739861242934907,-0.025379260739785765,-0.061168977390553235,-0.025480609649649717,-0.075860900280976806,-0.047743058547612696,-0.022629332675709841,-0.03364909147235156,-0.010574570876863247,-0.067311855003897289,-0.073915660766134553,-0.11268702062009751,-0.021177657631941925,-0.049135262139873646,-0.020008415493337147,0.0085668781963946783,-0.042346936313228972,-0.068104319819772122,-0.061726143511240721,0.0045270284281021577,-0.073257891349461077,-0.026966109545183432,-0.050839376841390151,-0.045024830042461349,0.006481800133079787,-0.038592291713662977,-0.031749273051868414,-0.033201011445940919,-0.071321343356811701,-0.052527692711604616,-0.0079819258888840401,-0.010525447399124662,-0.064080321339723995,-0.062209679744471655,-0.053246470770465237,-0.0079846376993637416,-0.058369900312638598,-0.038261703195982114,-0.06996470997023807,-0.088768135808512588,-0.10192134523519232,-0.070953365680517702,-0.013440081772782364,-0.045639462793405625,-0.036561971172669738,-0.028290360492078219,-0.07568102750654189,-0.077037106991275014,-0.01964392958342405,-0.039811742979677357,-0.057004734984362336,-0.031686981598999978,-0.10698594200457656,-0.041434759480592748,-0.048978387243190778,-0.041087196597328818,-0.021605585088176324,-0.068942059032313457,-0.027021050116952969,-0.031164612963760926,-0.042031493246932942,-0.08555486272745659,-0.080759425696831921,-0.050703591446379842,-0.077479537642192328,-0.018494706277526737,-0.013683305395230601,-0.0083978271540427248,-0.018175954373148999,-0.063158477256355788,-0.013521187206256053,-0.049394725006529014,-0.00048722834680202241,-0.040231892022197124,-0.025401916887077349,-0.01017215703654493,-0.035701651866409355,-0.04636468383094737,-0.093004750227158109,-0.021927458252540256,-0.042430585656940023,-0.01490014016489662,-0.022037668048786815,-0.035108200453877747,-0.070241335016561712,-0.062036432332645795,-0.026403524392480299,-0.038493071904581511,-0.039531924207354074,-0.086320902620265288,-0.05207359438858962,-0.062407472296045492,-0.060834798536234629,0.019308529005566455,-0.04626578674901681,-0.029152064729485182,-0.018060074525955417,-0.015036310832046514,-0.048391152674677911,-0.074329621642248822,-0.056171316336758488,-0.0089021025451643445,-0.064811886085434686,-0.041254013203543181,-0.038324115016604765,-0.045533585295085784,-0.015731494125795879,-0.068698581480860443,-0.078127422446125888,-0.021768884228808894,-0.063139317197050834,-0.041456414568233901,-0.031926674190691569,-0.02404700735554012,-0.087536316510335235,-0.046362300781015033,-0.038357792718259315,-0.10298295164507425,-0.064469590772599325,-0.029185570581670588,-0.041211535232824774,-0.053727107881090613,-0.055799571551599356,-0.02977800757360502,-0.058885255453579956,-0.032581432505992748,-0.055211512663922942,-0.024071592024103954,-0.072415103407248674,-0.048534667193720987,-0.044840598411775089,-0.010063759939478811,-0.0093848519099842716,-0.055669988427341291,-0.044658622582116926,-0.051402780632578471,-0.048328241509169589,-0.042921574659450817,-0.047735060765611029,-0.0045566853395859058,-0.088890870236496625,-0.0043864556348728019,-0.068773061619465392,-0.0061069479873017349,-0.033640597891941459,-0.066762477300916723,-0.032119134104528262,-0.057318439834688324,-0.041423319314352516,-0.041797250478897222,-0.059882479621472209,-0.022127449500735918,-0.047269444678090279,-0.02254475822188284,-0.032887971088204196,-0.017147531282171877,-0.041205487387278313,-0.014693966234775861,-0.060930255325082408,-0.094309365883746499,-0.068829299146465725,-0.011392858675346751,-0.084199291064148016,-0.088402752870318888,-0.045989723307609011,-0.057597220521871641,-0.063926664916578252,-0.020632066817241657,-0.067772300858310236,-0.049448275321966419,-0.060893092813232026,-0.0093871029173724849,-0.0012651450351101074,-0.080745645793193613,-0.025106885269264159,-0.024652823222933926,-0.046681872719904108,-0.044216347593607784,-0.099399017446161947,-0.0067501789153863534,-0.035069551661483025,-0.034925992749754171,-0.032366479576622781,-0.02374399781510363,-0.06747726277044333,-0.0079589678050147241,-0.029015235131976787,-0.12325729096409403,-0.048612209545655906,-0.014786063062285474,-0.046003622592449028,-0.081427291526761689,-0.055319131517597556,-0.054700407503679396,-0.051745907793286028,-0.026156536683915686,-0.019636489579734073,-0.085727024693304454,-0.055114661089475811,-0.056491656485987272,-0.059194743759408003,0.045075043339403389,-0.071830024569235096,-0.0063419429093640014,-0.059652237987976336,-0.0065931093816853489,-0.031507662091138415,-0.035533868934184622,-0.020768362989490776,-0.040262522316358081,-0.050702549381521772,-0.050961838116399358,-0.040026316559488406,-0.023249351023281965,-0.037992513599398946,-0.0040249338773024586,-0.04340761491965852,-0.05654778274447668,-0.039381923652384111,-0.010767363234688711,-0.068766616890701085,-0.061191540829350945,-0.084168569160721254,-0.01704644808307831,-0.032396467260872454,0.0030984540833157619,-0.038810490989967944,-0.062003664577157433,-0.082754182594347817,-0.051827275573920265,-0.051578356720760825,-0.0023591694497533322,-0.019003848400143405,-0.12084642991798103,-0.03591271867080708,-0.019643726958160919,-0.06423220267377322,0.00012119498108175443,-0.097700337022663591,-0.068705301869948318,-0.064615028659646551,-0.026415823188803055,-0.038473855105265124,-0.085245496889489542,-0.042750965877845923,-0.030457113373292894,-0.034098256295635079,-0.017906970184035347,-0.03706075374902381,-0.061023452430163924,-0.025409181762145027,-0.058450752130671128,-0.02528731061971172,-0.049950674623678644,-0.069569723544593523,-0.038411051408075388,-0.046765610503475732,-0.030204716750590232,-0.06467874935977351,-0.015026969509770598,-0.07361033408849868,-0.036141658411833637,-0.037574481944790371,-0.10972301291750608,-0.034277647075606377,-0.064895520200650772,-0.045754315506869175,-0.029295498545971251,-0.018676471445078179,-0.03461244588231794,-0.051209054368728364,-0.040636843514089117,-0.063159439345971471,-0.064117089677999145,-0.053286011652361881,-0.067292305127078664,-0.037581840397349596,0.039627475560087409,-0.043076144445929575,-0.049744082738657512,-0.051009198653855323,-0.054403539381572233,-0.052700367258547764,-0.079966537514454469,-0.038098457296524835,-0.035710422269090075,-0.05349369141389998,-0.076966304689893836,-0.020461594107834064,-0.064543668617217317,0.0028502801491356294,-0.014631401300668855,-0.001722267825737955,-0.037656877436692819,-0.051948292341288754,-0.019536291594624319,-0.06367885120544077,-0.048527280655448153,-0.10318500466340928,-0.039132862629543776,-0.083708440213426688,-0.047468936288128691,-0.053118792949450204,-0.062933897216933252,-0.081966688394358861,-0.053904254990345839,-0.14092929737097598,-0.035002016915291208,-0.023884900858022643,-0.030637022111679065,-0.089846207206691786,-0.0062868254967957619,-0.13384062055059454,-0.068865546695526386,-0.021774274598987925,-0.011139791923139956,-0.048986656824893504,-0.065865316828721029,-0.03563371473204649,-0.035948782447012245,-0.063970723892676357,-0.010200341311613119,-0.019590883644031765,-0.054057247762111266,-0.035937241887864853,-0.055888940849475044,-0.063812641732039599,0.029502373969897185,-0.069849583955775521,-0.027891155410391808,-0.050772522064501259,-0.059796075852838845,-0.03339608530804359,-0.0097946009208092055,-0.034406354758898423],"type":"histogram2d","nbinsx":20,"nbinsy":20,"marker":{"line":{"color":"rgba(31,119,180,1)"}},"xaxis":"x","yaxis":"y","frame":null}],"highlight":{"on":"plotly_click","persistent":false,"dynamic":false,"selectize":false,"opacityDim":0.20000000000000001,"selected":{"opacity":1},"debounce":0},"shinyEvents":["plotly_hover","plotly_click","plotly_selected","plotly_relayout","plotly_brushed","plotly_brushing","plotly_clickannotation","plotly_doubleclick","plotly_deselect","plotly_afterplot","plotly_sunburstclick"],"base_url":"https://plot.ly"},"evals":[],"jsHooks":[]}</script>
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
##  9.68736293  1.69845451 -0.03151014
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
## -30.809  -5.367  -0.459   5.409  43.269 
## 
## Coefficients:
##              Estimate Std. Error t value Pr(>|t|)    
## (Intercept)  18.65615    1.09387  17.055  < 2e-16 ***
## x             1.31939    0.18369   7.183 1.34e-12 ***
## fo.L         23.63918    1.08786  21.730  < 2e-16 ***
## fo.Q          9.90788    0.94980  10.432  < 2e-16 ***
## fo.C          0.19220    0.71498   0.269    0.788    
## fo^4          0.08386    0.51936   0.161    0.872    
## fuB         -22.86445    0.54232 -42.161  < 2e-16 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 8.538 on 993 degrees of freedom
## Multiple R-squared:  0.7272,	Adjusted R-squared:  0.7256 
## F-statistic: 441.3 on 6 and 993 DF,  p-value: < 2.2e-16
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
## x  1.31939   0.564055 2.33911 0.079456 .  
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## RMSE: 8.50795     Adj. R2: 0.725594
##                 Within R2: 0.049388
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
## x  1.12284   0.500696 2.24255 0.051628 .  
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## RMSE: 3.38275     Adj. R2: 0.956445
##                 Within R2: 0.190387
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
## -8.2495 -1.5251 -0.0278  1.4477 10.2947 
## 
## Coefficients:
##               Estimate Std. Error t value Pr(>|t|)    
## (Intercept)  1.376e+01  6.521e-01  21.092  < 2e-16 ***
## x            2.676e+00  1.227e-01  21.810  < 2e-16 ***
## fo.L         2.262e+01  1.906e+00  11.867  < 2e-16 ***
## fo.Q         7.245e+00  1.656e+00   4.374 1.35e-05 ***
## fo.C         1.037e+00  1.193e+00   0.869  0.38510    
## fo^4         1.152e-01  8.393e-01   0.137  0.89086    
## fuB         -1.400e+01  8.866e-01 -15.794  < 2e-16 ***
## x:fo.L       5.386e+00  3.617e-01  14.891  < 2e-16 ***
## x:fo.Q       2.095e+00  3.135e-01   6.684 3.91e-11 ***
## x:fo.C       5.598e-01  2.211e-01   2.532  0.01149 *  
## x:fo^4       6.849e-04  1.520e-01   0.005  0.99641    
## x:fuB       -2.617e+00  1.620e-01 -16.151  < 2e-16 ***
## fo.L:fuB    -2.283e+01  2.561e+00  -8.912  < 2e-16 ***
## fo.Q:fuB    -6.077e+00  2.231e+00  -2.724  0.00657 ** 
## fo.C:fuB    -1.613e-01  1.660e+00  -0.097  0.92261    
## fo^4:fuB     1.116e+00  1.195e+00   0.934  0.35063    
## x:fo.L:fuB  -5.296e+00  4.698e-01 -11.271  < 2e-16 ***
## x:fo.Q:fuB  -2.295e+00  4.084e-01  -5.620 2.49e-08 ***
## x:fo.C:fuB  -6.765e-01  3.023e-01  -2.238  0.02544 *  
## x:fo^4:fuB  -2.482e-01  2.146e-01  -1.157  0.24761    
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 2.56 on 980 degrees of freedom
## Multiple R-squared:  0.9758,	Adjusted R-squared:  0.9753 
## F-statistic:  2079 on 19 and 980 DF,  p-value: < 2.2e-16
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

## Outliers

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
## 32 
## 32
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
## 1  -1.1536326 0.83109271 3.245944057
## 15 -2.3029328 0.02543524 0.062167730
## 23 -0.2812283 0.03961187 0.001671557
## 32  3.3447818 0.02530815 0.114537400
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
##        dfb.1_        dfb.x       dffit    cov.r      cook.d        hat
## 1  1.93842622 -2.520204616 -2.55898678 5.818640 3.245944057 0.83109271
## 2 -0.00261081 -0.029541331 -0.06218703 1.083178 0.001979672 0.03228569
## 3 -0.01011337 -0.038190112 -0.09219668 1.071723 0.004332992 0.03017800
## 4 -0.19354074  0.118436690 -0.21496871 1.024192 0.022960061 0.03589604
## 5 -0.09418448  0.061225379 -0.10175462 1.082894 0.005280689 0.03918731
## 6  0.04342717  0.007346746  0.09750787 1.060746 0.004834211 0.02514273
```


## Normality

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
## W = 0.97803, p-value = 0.6169
```

```r
# car::qqPlot(reg)
```

Heterskedasticity may also matters for variance estimates. This is not shown in the plot, but you can run a simple test

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
## BP = 0.32679, df = 1, p-value = 0.5676
```

## Collinearity

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

With multiple linear regression, note that endogeneity biases are not just a problem your main variable. Suppose your interested in how $x_{1}$ affects $y$, conditional on $x_{2}$. Letting $X=[x_{1}, x_{2}]$, you estimate 
\begin{eqnarray}
\hat{\beta}_{OLS} = [X'X]^{-1}X'y
\end{eqnarray}
You paid special attention in your research design to find a case where $x_{1}$ is truly exogenous. Unfortunately, $x_{2}$ is correlated with the error term. (How unfair, I know, especially after all that work). Nonetheless,
\begin{eqnarray}
\mathbb{E}[X'\epsilon] = 
\begin{bmatrix}
0 \\ \rho
\end{bmatrix}\\
\mathbb{E}[ \hat{\beta}_{OLS} - \beta] = [X'X]^{-1} \begin{bmatrix}
0 \\ \rho
\end{bmatrix} = 
\begin{bmatrix}
\rho_{1} \\ \rho_{2}
\end{bmatrix}
\end{eqnarray}
The magnitude of the bias for $x_{1}$ thus depends on the correlations between $x_{1}$ and $x_{2}$ as well as $x_{2}$ and $\epsilon$.


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


There are many "Applied Statistics" approaches to 2SLS, and I encourage you to read up on them here

* https://www.econometrics-with-r.org/12-ivr.html
* https://bookdown.org/paul/applied-causal-analysis/estimation-2.html
* https://mixtape.scunning.com/07-instrumental_variables
* https://theeffectbook.net/ch-InstrumentalVariables.html
* http://www.urfie.net/read/index.html#page/247

I will focus on the seminal case in economics, which is complementary and hopefully provides much intuition

### Competitive Market Equilibrium

Although there are many ways this simultaneity can happen, economic theorists have made great strides in analyzing the simultaneity problem as it arises from market relationships. In fact, the 2SLS statistical approach arose to understand the equilibrium of a single competitive market, which has three structural equations: (1) market supply is the sum of quantities supplied by individual firms, (2) market demand is the sum of quantities demanded by individual people, (3) market supply equals market demand.
\begin{eqnarray}
Q^{D}(P) &=& \sum_{i} q^{D}_{i}(P)  \\
Q^{S}(P) &=& \sum_{i} q^{S}_{i}(P) \\
Q^{D} &=& Q^{S} = Q.
\end{eqnarray}
This last equation implies a simultaneous "reduced form" relationship where both the price and the quantity are outcomes. If there is a linear parametric structure to these equations, then you can examine how a change in parameters affects both price and quantity. Specifically, if
\begin{eqnarray}
\label{eqn:linear_demand}
Q^{D}(P) &=& A^{D} - B^{D} P + \epsilon^{D},\\
\label{eqn:linear_supply}
Q^{S}(P) &=& A^{S} + B^{S} P + \epsilon^{S},
\end{eqnarray}
then equilibrium yields reduced form equations that collapse into intercept and residual terms;
\begin{eqnarray}
P^{*} &=& \frac{A^{D}-A^{S}}{B^{D}+B^{S}} + \frac{\epsilon^{D} - \epsilon^{S}}{B^{D}+B^{S}} = \alpha^{P} + \nu^{P}, \\
Q^{*} &=& \frac{A^{S}B^{D}+ A^{D}B^{S}}{B^{D}+B^{S}} + \frac{\epsilon^{S}B^{D}+ \epsilon^{D}B^{S}}{B^{D}+B^{S}}= \alpha^{Q} + \nu^{Q}.
\end{eqnarray}



```r
# Competitive Market Process

## Parameters
plm <- c(5,10) ## Price Range
P <- seq(plm[1],plm[2],by=.01) ## Price to Consider

## Demand Curve Simulator
qd_fun <- function(p, Ad=8, Bd=-.8, Ed_sigma=.25){
    Qd <- Ad + Bd*p + rnorm(1,0,Ed_sigma)
}

## Supply Curve Simulator
qs_fun <- function(p, As=-8, Bs=1, Es_sigma=.25){
    Qs <- As + Bs*p + rnorm(1,0,Es_sigma)
}
```



```r
N <- 300 ## Number of Simulations

## Generate Equilibrium Data
## Plot Underlying Process
plot.new()
plot.window(xlim=c(0,2), ylim=plm)
EQ1 <- sapply(1:N, function(n){

    ## Market Mechanisms
    demand <- qd_fun(P)
    supply <- qs_fun(P)

    ## Compute EQ (what we observe)
    eq_id <- which.min( abs(demand-supply) )
    eq <- c(P=P[eq_id], Q=demand[eq_id]) 
    
    ## Plot Theoretical Supply and Demand behind EQ
	lines(demand, P, col=grey(0,.01))
	lines(supply, P, col=grey(0,.01))
    points(eq[2], eq[1], col=grey(0,.05), pch=16)

    ## Return Equilibrium Observations
    return(eq)
})
axis(1)
axis(2)
mtext('Quantity',1, line=2)
mtext('Price',2, line=2)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-39-1.png" width="672" />


You can simply run a regression of one variable on another, but you will need much luck to correctly interrupt the resulting number. Consider regressing quantity on price;
\begin{eqnarray}
Q &=& \alpha^{Q} + \beta^{Q} P + \epsilon^{Q} = \alpha^{Q} + \beta^{Q} [\alpha^{P} + \beta^{P} Q + \epsilon^{P}] + \epsilon^{Q} \\
&=& \frac{[\alpha^{Q} +  \epsilon^{Q}] + \beta^{Q} [\alpha^{P} + \epsilon^{P}]}{1-\beta^{P}}
\end{eqnarray}
We can see $Q$ is a function of $\epsilon^{P}$, thus biasing the estimate of $\beta^{P}$. If you were to instead regress $Q$ on $P$, you would similarly get a number that is hard to interpret meaningfully. This simple derivation has a profound insight: price-quantity data does not generally tell you how price affects quantity supplied or demanded (and vice-versa).

```r
## Analyze Market Data
dat1 <- data.frame(t(EQ1), cost='1')
reg1 <- lm(Q~P, data=dat1)
summary(reg1)
```

```
## 
## Call:
## lm(formula = Q ~ P, data = dat1)
## 
## Residuals:
##      Min       1Q   Median       3Q      Max 
## -0.49098 -0.10768 -0.01032  0.12138  0.54524 
## 
## Coefficients:
##             Estimate Std. Error t value Pr(>|t|)  
## (Intercept) -0.31192    0.46821  -0.666   0.5058  
## P            0.13356    0.05256   2.541   0.0116 *
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 0.1676 on 298 degrees of freedom
## Multiple R-squared:  0.0212,	Adjusted R-squared:  0.01792 
## F-statistic: 6.456 on 1 and 298 DF,  p-value: 0.01157
```

If you have exogeneous variation on one side of the market, ``shocks'', you can get information on the other. Experimental manipulation of $A^{S}$ would, for example, allow you to trace out part of a demand curve: 
\begin{eqnarray}
\frac{\partial P^{*}}{\partial A^{S}} = \frac{-1}{B^{D}+B^{S}}, \\
\frac{\partial Q^{*}}{\partial A^{S}} = \frac{B^{D}}{B^{D}+B^{S}}.
\end{eqnarray}
Notice that even in this linear model, all effects are conditional: *The* effect of a cost change on quantity or price depends on the demand curve. A change in costs affects quantity supplied but not quantity demanded (which then affects equilibrium price) but the demand side of the market still matters! The change in price from a change in costs depends on the elasticity of demand. (Likewise for changes in demand parameters.) 

With two equations and two unknowns, we can estimate $B^{D}$ and $B^{S}$, which was the original idea behind 2SLS. Substituting the equilibrium condition into the structural demand equation, we can rewrite them as
\begin{eqnarray}
\label{eqn:linear_demand_iv}
P(Q) &=& -\frac{A^{D}}{{B^{D}}} + \frac{Q^{s}}{B^{D}} - \frac{\epsilon^{D}}{B^{D}}  = \alpha^{P} + \beta^{P} Q + \epsilon^{P}\\
\label{eqn:linear_supply_iv}
Q(P) &=&  A^{S}  + \epsilon^{S} +  B^{S} P .
\end{eqnarray}


```r
## Supply Shifter
EQ2 <- sapply(1:N, function(n){
    ## New Demand, but same par's
    demand <- qd_fun(P)
    ## New Supply Curves
    supply2 <- qs_fun(P, As=-6.5)
	## lines(supply2, P, col=rgb(0,0,1,.01))
    ## Compute New EQ
    eq_id <- which.min( abs(demand-supply2) )
    eq <- c(P=P[eq_id], Q=demand[eq_id]) 
    #points(eq[2], eq[1], col=rgb(0,0,1,.05), pch=16)
    return(eq)
})

## Market Data w/ Supply Shift
dat2 <- data.frame(t(EQ2), cost='2')
dat2 <- rbind(dat1, dat2)


## Plot Market Data  w/ Supply Shift
cols <- ifelse(as.numeric(dat2$cost)==2, rgb(0,0,1,.2), rgb(0,0,0,.2))
plot.new()
plot.window(xlim=c(0,2), ylim=plm)
points(dat2$Q, dat2$P, col=cols, pch=16)
axis(1)
axis(2)
mtext('Quantity',1, line=2)
mtext('Price',2, line=2)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-41-1.png" width="672" />



```r
## Not exact, at least right sign
reg2 <- lm(Q~P, data=dat2)
summary(reg2)
```

```
## 
## Call:
## lm(formula = Q ~ P, data = dat2)
## 
## Residuals:
##      Min       1Q   Median       3Q      Max 
## -0.67572 -0.16129 -0.01454  0.16013  0.75910 
## 
## Coefficients:
##             Estimate Std. Error t value Pr(>|t|)    
## (Intercept)  6.70490    0.17515   38.28   <2e-16 ***
## P           -0.64725    0.02062  -31.39   <2e-16 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 0.2332 on 598 degrees of freedom
## Multiple R-squared:  0.6224,	Adjusted R-squared:  0.6217 
## F-statistic: 985.6 on 1 and 598 DF,  p-value: < 2.2e-16
```

```r
## Instrumental Variables Estimates
library(fixest)
reg2_iv <- feols(Q~1|P~cost, data=dat2)
summary(reg2_iv)
```

```
## TSLS estimation, Dep. Var.: Q, Endo.: P, Instr.: cost
## Second stage: Dep. Var.: Q
## Observations: 600 
## Standard-errors: IID 
##              Estimate Std. Error  t value  Pr(>|t|)    
## (Intercept)  7.976259   0.199704  39.9405 < 2.2e-16 ***
## fit_P       -0.797123   0.023512 -33.9021 < 2.2e-16 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## RMSE: 0.242927   Adj. R2: 0.588324
## F-test (1st stage), P: stat = 3,066.2, p < 2.2e-16, on 1 and 598 DoF.
##            Wu-Hausman: stat =   494.6, p < 2.2e-16, on 1 and 597 DoF.
```

```r
## Many alternative packages can do IV
## library(ivreg)
## summary( ivreg(Q~P|cost, data=dat2) )
```

If we had multiple alleged supply shifts and recorded their magnitudes, then we could recover more information about demand. 

**Caveat** The coefficient interpretation rests on many assumptions. We have implicitly assumed

* both supply and demand are linear and additively seperable in covariates.
* only supply was affected, and it was only an intercept shift.
* the shock large enough to be picked up statistically.

We always get coefficients back when fitting `feols` but are rarely confident that all these assumptions hold. This is one reason why researchers often also report their OLS results.






## Regression Discontinuities/Kink (RD/RK)

The basic idea here is to examine how a variable changes in response to an exogenous shock. Again, there is a large "Applied Statistics" literature I direct you to first

* https://bookdown.org/paul/applied-causal-analysis/rdd-regression-discontinuity-design.html
* https://mixtape.scunning.com/06-regression_discontinuity
* https://theeffectbook.net/ch-RegressionDiscontinuity.html

The Regression Discontinuities estimate of the cost shock is the difference in the outcome variable just before and just after the shock. We now turn to our canonical competitive market example. The RD estimate is the difference between the red and blue lines at $T=300$.


```r
dat2$T <- 1:nrow(dat2)

plot(P~T, dat2, main='Effect of Cost Shock on Price', pch=16, col=grey(0,.5))
regP1 <- lm(P~T, dat2[dat2$cost==1,]) 
lines(regP1$model$T, predict(regP1), col=2)
regP2 <- lm(P~T, dat2[dat2$cost==2,]) 
lines(regP2$model$T, predict(regP2), col=4)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-44-1.png" width="672" />

```r
regP <- lm(P~T*cost, dat2)
summary(regP)
```

```
## 
## Call:
## lm(formula = P ~ T * cost, data = dat2)
## 
## Residuals:
##      Min       1Q   Median       3Q      Max 
## -0.54170 -0.12108 -0.01032  0.12872  0.59876 
## 
## Coefficients:
##               Estimate Std. Error t value Pr(>|t|)    
## (Intercept)  8.915e+00  2.167e-02 411.452   <2e-16 ***
## T           -6.201e-05  1.248e-04  -0.497    0.619    
## cost2       -8.504e-01  6.121e-02 -13.894   <2e-16 ***
## T:cost2      5.334e-05  1.765e-04   0.302    0.763    
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 0.1872 on 596 degrees of freedom
## Multiple R-squared:  0.8369,	Adjusted R-squared:  0.836 
## F-statistic:  1019 on 3 and 596 DF,  p-value: < 2.2e-16
```


```r
plot(Q~T, dat2, main='Effect of Cost Shock on Quantity', pch=16, col=grey(0,.5))
regQ1 <- lm(Q~T, dat2[dat2$cost==1,]) 
lines(regQ1$model$T, predict(regQ1), col=2)
regQ2 <- lm(Q~T, dat2[dat2$cost==2,]) 
lines(regQ2$model$T, predict(regQ2), col=4)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-45-1.png" width="672" />

```r
regQ <- lm(Q~T*cost, dat2)
summary(regQ)
```

```
## 
## Call:
## lm(formula = Q ~ T * cost, data = dat2)
## 
## Residuals:
##      Min       1Q   Median       3Q      Max 
## -0.51459 -0.11936 -0.00235  0.12210  0.62111 
## 
## Coefficients:
##              Estimate Std. Error t value Pr(>|t|)    
## (Intercept) 8.607e-01  2.014e-02  42.736   <2e-16 ***
## T           1.112e-04  1.160e-04   0.959    0.338    
## cost2       6.394e-01  5.690e-02  11.238   <2e-16 ***
## T:cost2     1.766e-06  1.640e-04   0.011    0.991    
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 0.174 on 596 degrees of freedom
## Multiple R-squared:  0.7906,	Adjusted R-squared:  0.7895 
## F-statistic:   750 on 3 and 596 DF,  p-value: < 2.2e-16
```

Remember that this is effect is *local*: different magnitudes of the cost shock or different demand curves generally yeild different estimates.

## Difference in Differences (DID)

The basic idea here is to examine how a variable changes in response to an exogenous shock, *compared to a control group*. Again, there is a large "Applied Statistics" literature I direct you to first

* https://mixtape.scunning.com/09-difference_in_differences
* https://theeffectbook.net/ch-DifferenceinDifference.html
* http://www.urfie.net/read/index.html#page/226


```r
EQ3 <- sapply(1:(2*N), function(n){

    ## Market Mechanisms
    demand <- qd_fun(P)
    supply <- qs_fun(P)

    ## Compute EQ (what we observe)
    eq_id <- which.min( abs(demand-supply) )
    eq <- c(P=P[eq_id], Q=demand[eq_id]) 

    ## Return Equilibrium Observations
    return(eq)
})
dat3 <- data.frame(t(EQ3), cost='1', T=1:ncol(EQ3))


par(mfrow=c(1,2))
plot(P~T, dat2, main='Effect of Cost Shock on Price', pch=17,col=rgb(0,0,1,.25))
points(P~T, dat3, pch=16, col=rgb(1,0,0,.25))

plot(Q~T, dat2, main='Effect of Cost Shock on Quantity', pch=17,col=rgb(0,0,1,.25))
points(Q~T, dat3, pch=16, col=rgb(1,0,0,.25))
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-46-1.png" width="672" />

```r
dat <- rbind(dat2, dat3)
regP <- lm(P~T*cost, dat)
summary(regP)
```

```
## 
## Call:
## lm(formula = P ~ T * cost, data = dat)
## 
## Residuals:
##      Min       1Q   Median       3Q      Max 
## -0.68520 -0.12570 -0.00517  0.12472  0.61503 
## 
## Coefficients:
##               Estimate Std. Error t value Pr(>|t|)    
## (Intercept)  8.895e+00  1.166e-02 762.736   <2e-16 ***
## T            5.289e-06  3.882e-05   0.136    0.892    
## cost2       -8.303e-01  6.020e-02 -13.791   <2e-16 ***
## T:cost2     -1.396e-05  1.345e-04  -0.104    0.917    
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 0.1931 on 1196 degrees of freedom
## Multiple R-squared:  0.7788,	Adjusted R-squared:  0.7783 
## F-statistic:  1404 on 3 and 1196 DF,  p-value: < 2.2e-16
```

```r
regQ <- lm(Q~T*cost, dat)
summary(regQ)
```

```
## 
## Call:
## lm(formula = Q ~ T * cost, data = dat)
## 
## Residuals:
##      Min       1Q   Median       3Q      Max 
## -0.56863 -0.12055 -0.00401  0.12048  0.62748 
## 
## Coefficients:
##              Estimate Std. Error t value Pr(>|t|)    
## (Intercept) 8.829e-01  1.054e-02  83.737   <2e-16 ***
## T           1.516e-05  3.510e-05   0.432    0.666    
## cost2       6.173e-01  5.443e-02  11.341   <2e-16 ***
## T:cost2     9.779e-05  1.216e-04   0.804    0.421    
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 0.1746 on 1196 degrees of freedom
## Multiple R-squared:  0.7315,	Adjusted R-squared:  0.7308 
## F-statistic:  1086 on 3 and 1196 DF,  p-value: < 2.2e-16
```

Again, the effects are local. 

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

<img src="03-ROLS_files/figure-html/unnamed-chunk-49-1.png" width="672" />



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

<img src="03-ROLS_files/figure-html/unnamed-chunk-50-1.png" width="672" />




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

<img src="03-ROLS_files/figure-html/unnamed-chunk-53-1.png" width="672" />


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

<img src="03-ROLS_files/figure-html/unnamed-chunk-54-1.png" width="672" />


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

<img src="03-ROLS_files/figure-html/unnamed-chunk-55-1.png" width="672" />


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

<img src="03-ROLS_files/figure-html/unnamed-chunk-57-1.png" width="672" />


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



