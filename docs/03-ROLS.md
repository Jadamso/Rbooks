
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
## Example 1 (Theoretical)

## Generate Dataset
n <- 300
z <- rbinom(n,1,.5)
xy <- sapply(z, function(zi){
    y <- rnorm(1,zi,1)
    x <- rnorm(1,zi*2,1)
    c(x,y)
})
xy <- data.frame(x=xy[1,],y=xy[2,])

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
##      0.2209       0.2169
```

```r
## Add Predictions to Plot
abline(reg, col='orange')
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-1-1.png" width="672" />


Sums of Squared Errors
$$
\underbrace{\sum\nolimits_{i}(y_i-\bar{y})^2}_\text{TSS}=\underbrace{\sum\nolimits_{i}(\hat{y}_i-\bar{y})^2}_\text{RSS}+\underbrace{\sum\nolimits_{i}\hat{\epsilon}^2}_\text{ESS}\\
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

## Check R2
summary(reg)$r.squared
```

```
## [1] 0.07597341
```

### Variability Estimates

A regression coefficient is a statistic. And, just like all statistics, we can calculate 

* *standard deviation*: variability within a single sample.
* *standard error*: variability across different samples.
* *confidence interval* range of variability across different samples.
* *p-value* the probability you would see something as extreme as your statistic under the null (assuming your null hypothesis was true).
* null distribution*: the distribution of the statistic under the null hypothesis.

The classic estimates for variability are the Standard Error of the Regression $\hat{\sigma}$, and Standard Error of the Coefficient Estimates $\hat{\sigma}_{\hat{\alpha}}$ and $\hat{\sigma}_{\hat{\alpha}}$ --- or simply Standard Errors.
$$
\hat{\sigma}^2 = \frac{1}{n-2}\sum_{i}\hat{\epsilon_{i}}^2\\
\hat{\sigma}^2_{\hat{\alpha}}=\hat{\sigma}^2\left[\frac{1}{n}+\frac{\bar{x}^2}{\sum_{i}(x_i-\bar{x})^2}\right]\\
\hat{\sigma}^2_{\hat{\beta}}=\frac{\hat{\sigma}^2}{\sum_{i}(x_i-\bar{x})^2}.
$$
These equations are motivated by particular data generating proceses, which you can read more about this at https://www.econometrics-with-r.org/4-lrwor.html. We can also estimate variabilty using *data-driven* methods that assume much less. See, e.g., https://www.sagepub.com/sites/default/files/upm-binaries/21122_Chapter_21.pdf

We first consider the simplest, the jackknife, where we loop through each row of the dataset. In each iteration of the loop, we drop that observation from the dataset and reestimate the statistic of interest. We then calculate the standard deviation of the statistic across all ``resamples''.


```r
## Example 1 Continued

## Point Estimates
reg <- lm(y~x, dat=xy)
coefX <- coef(reg)['x']

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
    main=paste0('SE est.=', round(jack_se,4)),
    xlab=expression(beta[-i]))
abline(v=jack_mean, col="red", lwd=2)
abline(v=jack_ci_percentile, col="red", lty=2)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-3-1.png" width="672" />

```r
## Plot Full-Sample Estimate
## abline(v=coefX, lty=1, col='blue', lwd=2)

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
    main=paste0('SE est.=', round(boot_se,4)),
    xlab=expression(beta[b]))
abline(v=boot_mean, col="red", lwd=2)
abline(v=boot_ci_percentile, col="red", lty=2)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-4-1.png" width="672" />

```r
## Normal Approximation
## boot_ci_normal <- boot_mean+c(-1.96, +1.96)*boot
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
    main=paste0('SE est.=', round(boot_se,4)),
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
    xlim=range(c(boot_coefs0, coefX)))
abline(v=boot_ci_percentile0, lty=2)
abline(v=coefX, col="red", lwd=2)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-6-1.png" width="672" />

Regardless of how we calculate standard errors, we can use them to conduct a t-test. We also compute the distribution of t-values under the null hypothesis, and compare how extreme the oberved value is.
$$ \hat{t} = \frac{\hat{\beta} - \beta_{0} }{\hat{\sigma}_{\hat{\beta}}} $$


```r
## T Test
B0 <- 0
boot_t  <- (coefX-B0)/boot_se

## Compute Bootstrap T-Values (without refinement)
boot_t_boot0 <- sapply(boot_regs0, function(reg_b){
    beta_b <- coef(reg_b)[['x']]
    t_hat_b <- (beta_b)/boot_se
    return(t_hat_b)
})
hist(boot_t_boot0, breaks=100,
    xlim=range(c(boot_t_boot0, boot_t)) )
abline(v=boot_t, lwd=2, col='red')
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-7-1.png" width="672" />

From this, we can calculate a *p-value*: the probability you would see something as extreme as your statistic under the null (assuming your null hypothesis was true).  Note that the $p$ reported by your computer does not necessarily satisfy this definition! We can always calcuate a p-value from an explicit null distribution.

```r
## One Sided Test for P(t > boot_t | Null)=1- P(t < boot_t | Null)
That_NullDist1 <- ecdf(boot_t_boot0)
Phat1  <- 1-That_NullDist1(boot_t)
## Two Sided Test for P(t > jack_t or  t < -jack_t | Null)
That_NullDist2 <- ecdf(abs(boot_t_boot0))
Phat2  <-  1-That_NullDist2(boot_t)
```
Under some assumptions, the null distribution is distributed $t_{n-2}$. (For more on theory based regression t-testing, see https://www.econometrics-with-r.org/4-lrwor.html.) 


### Prediction Intervals [Under Construction]

In addition to confidence intervales, we can also compute a *prediction interval* which estimates the range of variability across different samples for the outcomes. These intervals also take into account the residuals--- the variability of individuals around the mean. 

For a nice overview of different types of intervals, see https://www.jstor.org/stable/2685212
For an indepth view, see "Statistical Intervals: A Guide for Practitioners and Researchers" or "Statistical Tolerance Regions: Theory, Applications, and Computation". 
See https://robjhyndman.com/hyndsight/intervals/ for constructing intervals for future observations in a time-series context



```r
## Bootstrap Prediction Interval
boot_resids <- lapply(boot_regs, function(reg_b){
    e_b <- resid(reg_b)
    x_b <- reg_b$model$x
    res_b <- cbind(e_b, x_b)
})
boot_resids <- as.data.frame(do.call(rbind, boot_resids))
## Estimate Residual Quantiles using data around X points
x <- data.frame(x=quantile(xy$x,probs=seq(0,1,by=.1)))
boot_resid_list <- split(boot_resids,
    cut(boot_resids$x_b, x$x) )
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
boot_x <- x$x[-1] - diff(x$x)/2
boot_pmean <- boot_mean*boot_x
boot_pi <-  boot_pmean + boot_resid_est

## Plot Bootstrap PI
plot(y~x, dat=xy, pch=16)
polygon( c(boot_x, rev(boot_x)), c(boot_pi[,1], rev(boot_pi[,2])),
    col=grey(0,.2), border=0)

## Parametric PI (For Comparison)
pi <- predict(reg, interval='prediction', newdata=x)
lines( x$x, pi[,'lwr'], lty=2)
lines( x$x, pi[,'upr'], lty=2)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-9-1.png" width="672" />

```r
## Parametric CI
## x <- data.frame(x=quantile(xy$x,probs=seq(0,1,by=.1)))
## ci <- predict(reg, interval='confidence', newdata=x)
## polygon( c(x$x, rev(x$x)), c(ci[,'lwr'], rev(ci[,'upr'])), col=grey(0,.2), border=0)
```

There are many ways to improve upon the prediction intervals you just created. Again, this is just an introduction. For more, see Davison and Hinkley, chapters 5 and 6 (also (Efron and Tibshirani, or Wehrens et al.)




## OLS (multiple linear regression)

Model and objective
$$
y_i=\beta_0+\beta_1x_{i1}+\beta_2x_{i2}+\ldots+\beta_kx_{ik}+\epsilon_i = X_{i}\beta + +\epsilon_i \\
min_{\beta} \sum_{i=1}^{n} (\epsilon_i)^2
$$

Point Estimates in matrix form
$$
y=\textbf{X}\beta+\epsilon\\
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
plotly::plot_ly(
  USArrests, x = ~UrbanPop, y = ~Assault,
  text = ~paste('State: ', ID, "<br>Murder Arrests:", Murder),
  color = ~Murder,
  marker = list(size = ~Murder, opacity = 0.5),
  title = 'Murder arrests (per 100,000)')
```

```{=html}
<div class="plotly html-widget html-fill-item-overflow-hidden html-fill-item" id="htmlwidget-3675438f9f778c094c45" style="width:672px;height:480px;"></div>
<script type="application/json" data-for="htmlwidget-3675438f9f778c094c45">{"x":{"visdat":{"2f726d2879c2":["function () ","plotlyVisDat"]},"cur_data":"2f726d2879c2","attrs":{"2f726d2879c2":{"x":{},"y":{},"text":{},"marker":{"size":{},"opacity":0.5},"title":"Murder arrests (per 100,000)","color":{},"alpha_stroke":1,"sizes":[10,100],"spans":[1,20]}},"layout":{"margin":{"b":40,"l":60,"t":25,"r":10},"xaxis":{"domain":[0,1],"automargin":true,"title":"UrbanPop"},"yaxis":{"domain":[0,1],"automargin":true,"title":"Assault"},"hovermode":"closest","showlegend":false,"legend":{"yanchor":"top","y":0.5}},"source":"A","config":{"modeBarButtonsToAdd":["hoverclosest","hovercompare"],"showSendToCloud":false},"data":[{"x":[58,48,80,50,91,78,77,72,80,60,83,54,83,65,57,66,52,66,51,67,85,74,66,44,70,53,62,81,56,89,70,86,45,44,75,68,67,72,87,48,45,59,80,80,32,63,73,39,66,60],"y":[236,263,294,190,276,204,110,238,335,211,46,120,249,113,56,115,109,249,83,300,149,255,72,259,178,109,102,252,57,159,285,254,337,45,120,151,159,106,174,279,86,188,201,120,48,156,145,81,53,161],"text":["State:  Alabama <br>Murder Arrests: 13.2","State:  Alaska <br>Murder Arrests: 10","State:  Arizona <br>Murder Arrests: 8.1","State:  Arkansas <br>Murder Arrests: 8.8","State:  California <br>Murder Arrests: 9","State:  Colorado <br>Murder Arrests: 7.9","State:  Connecticut <br>Murder Arrests: 3.3","State:  Delaware <br>Murder Arrests: 5.9","State:  Florida <br>Murder Arrests: 15.4","State:  Georgia <br>Murder Arrests: 17.4","State:  Hawaii <br>Murder Arrests: 5.3","State:  Idaho <br>Murder Arrests: 2.6","State:  Illinois <br>Murder Arrests: 10.4","State:  Indiana <br>Murder Arrests: 7.2","State:  Iowa <br>Murder Arrests: 2.2","State:  Kansas <br>Murder Arrests: 6","State:  Kentucky <br>Murder Arrests: 9.7","State:  Louisiana <br>Murder Arrests: 15.4","State:  Maine <br>Murder Arrests: 2.1","State:  Maryland <br>Murder Arrests: 11.3","State:  Massachusetts <br>Murder Arrests: 4.4","State:  Michigan <br>Murder Arrests: 12.1","State:  Minnesota <br>Murder Arrests: 2.7","State:  Mississippi <br>Murder Arrests: 16.1","State:  Missouri <br>Murder Arrests: 9","State:  Montana <br>Murder Arrests: 6","State:  Nebraska <br>Murder Arrests: 4.3","State:  Nevada <br>Murder Arrests: 12.2","State:  New Hampshire <br>Murder Arrests: 2.1","State:  New Jersey <br>Murder Arrests: 7.4","State:  New Mexico <br>Murder Arrests: 11.4","State:  New York <br>Murder Arrests: 11.1","State:  North Carolina <br>Murder Arrests: 13","State:  North Dakota <br>Murder Arrests: 0.8","State:  Ohio <br>Murder Arrests: 7.3","State:  Oklahoma <br>Murder Arrests: 6.6","State:  Oregon <br>Murder Arrests: 4.9","State:  Pennsylvania <br>Murder Arrests: 6.3","State:  Rhode Island <br>Murder Arrests: 3.4","State:  South Carolina <br>Murder Arrests: 14.4","State:  South Dakota <br>Murder Arrests: 3.8","State:  Tennessee <br>Murder Arrests: 13.2","State:  Texas <br>Murder Arrests: 12.7","State:  Utah <br>Murder Arrests: 3.2","State:  Vermont <br>Murder Arrests: 2.2","State:  Virginia <br>Murder Arrests: 8.5","State:  Washington <br>Murder Arrests: 4","State:  West Virginia <br>Murder Arrests: 5.7","State:  Wisconsin <br>Murder Arrests: 2.6","State:  Wyoming <br>Murder Arrests: 6.8"],"marker":{"colorbar":{"title":"Murder","ticklen":2},"cmin":0.80000000000000004,"cmax":17.399999999999999,"colorscale":[["0","rgba(68,1,84,1)"],["0.0416666666666667","rgba(70,19,97,1)"],["0.0833333333333333","rgba(72,32,111,1)"],["0.125","rgba(71,45,122,1)"],["0.166666666666667","rgba(68,58,128,1)"],["0.208333333333333","rgba(64,70,135,1)"],["0.25","rgba(60,82,138,1)"],["0.291666666666667","rgba(56,93,140,1)"],["0.333333333333333","rgba(49,104,142,1)"],["0.375","rgba(46,114,142,1)"],["0.416666666666667","rgba(42,123,142,1)"],["0.458333333333333","rgba(38,133,141,1)"],["0.5","rgba(37,144,140,1)"],["0.541666666666667","rgba(33,154,138,1)"],["0.583333333333333","rgba(39,164,133,1)"],["0.625","rgba(47,174,127,1)"],["0.666666666666667","rgba(53,183,121,1)"],["0.708333333333333","rgba(79,191,110,1)"],["0.75","rgba(98,199,98,1)"],["0.791666666666667","rgba(119,207,85,1)"],["0.833333333333333","rgba(147,214,70,1)"],["0.875","rgba(172,220,52,1)"],["0.916666666666667","rgba(199,225,42,1)"],["0.958333333333333","rgba(226,228,40,1)"],["1","rgba(253,231,37,1)"]],"showscale":false,"color":[13.199999999999999,10,8.0999999999999996,8.8000000000000007,9,7.9000000000000004,3.2999999999999998,5.9000000000000004,15.4,17.399999999999999,5.2999999999999998,2.6000000000000001,10.4,7.2000000000000002,2.2000000000000002,6,9.6999999999999993,15.4,2.1000000000000001,11.300000000000001,4.4000000000000004,12.1,2.7000000000000002,16.100000000000001,9,6,4.2999999999999998,12.199999999999999,2.1000000000000001,7.4000000000000004,11.4,11.1,13,0.80000000000000004,7.2999999999999998,6.5999999999999996,4.9000000000000004,6.2999999999999998,3.3999999999999999,14.4,3.7999999999999998,13.199999999999999,12.699999999999999,3.2000000000000002,2.2000000000000002,8.5,4,5.7000000000000002,2.6000000000000001,6.7999999999999998],"size":[13.199999999999999,10,8.0999999999999996,8.8000000000000007,9,7.9000000000000004,3.2999999999999998,5.9000000000000004,15.4,17.399999999999999,5.2999999999999998,2.6000000000000001,10.4,7.2000000000000002,2.2000000000000002,6,9.6999999999999993,15.4,2.1000000000000001,11.300000000000001,4.4000000000000004,12.1,2.7000000000000002,16.100000000000001,9,6,4.2999999999999998,12.199999999999999,2.1000000000000001,7.4000000000000004,11.4,11.1,13,0.80000000000000004,7.2999999999999998,6.5999999999999996,4.9000000000000004,6.2999999999999998,3.3999999999999999,14.4,3.7999999999999998,13.199999999999999,12.699999999999999,3.2000000000000002,2.2000000000000002,8.5,4,5.7000000000000002,2.6000000000000001,6.7999999999999998],"opacity":0.5,"line":{"colorbar":{"title":"","ticklen":2},"cmin":0.80000000000000004,"cmax":17.399999999999999,"colorscale":[["0","rgba(68,1,84,1)"],["0.0416666666666667","rgba(70,19,97,1)"],["0.0833333333333333","rgba(72,32,111,1)"],["0.125","rgba(71,45,122,1)"],["0.166666666666667","rgba(68,58,128,1)"],["0.208333333333333","rgba(64,70,135,1)"],["0.25","rgba(60,82,138,1)"],["0.291666666666667","rgba(56,93,140,1)"],["0.333333333333333","rgba(49,104,142,1)"],["0.375","rgba(46,114,142,1)"],["0.416666666666667","rgba(42,123,142,1)"],["0.458333333333333","rgba(38,133,141,1)"],["0.5","rgba(37,144,140,1)"],["0.541666666666667","rgba(33,154,138,1)"],["0.583333333333333","rgba(39,164,133,1)"],["0.625","rgba(47,174,127,1)"],["0.666666666666667","rgba(53,183,121,1)"],["0.708333333333333","rgba(79,191,110,1)"],["0.75","rgba(98,199,98,1)"],["0.791666666666667","rgba(119,207,85,1)"],["0.833333333333333","rgba(147,214,70,1)"],["0.875","rgba(172,220,52,1)"],["0.916666666666667","rgba(199,225,42,1)"],["0.958333333333333","rgba(226,228,40,1)"],["1","rgba(253,231,37,1)"]],"showscale":false,"color":[13.199999999999999,10,8.0999999999999996,8.8000000000000007,9,7.9000000000000004,3.2999999999999998,5.9000000000000004,15.4,17.399999999999999,5.2999999999999998,2.6000000000000001,10.4,7.2000000000000002,2.2000000000000002,6,9.6999999999999993,15.4,2.1000000000000001,11.300000000000001,4.4000000000000004,12.1,2.7000000000000002,16.100000000000001,9,6,4.2999999999999998,12.199999999999999,2.1000000000000001,7.4000000000000004,11.4,11.1,13,0.80000000000000004,7.2999999999999998,6.5999999999999996,4.9000000000000004,6.2999999999999998,3.3999999999999999,14.4,3.7999999999999998,13.199999999999999,12.699999999999999,3.2000000000000002,2.2000000000000002,8.5,4,5.7000000000000002,2.6000000000000001,6.7999999999999998]}},"title":"Murder arrests (per 100,000)","type":"scatter","mode":"markers","xaxis":"x","yaxis":"y","frame":null},{"x":[32,91],"y":[45,337],"type":"scatter","mode":"markers","opacity":0,"hoverinfo":"none","showlegend":false,"marker":{"colorbar":{"title":"Murder","ticklen":2,"len":0.5,"lenmode":"fraction","y":1,"yanchor":"top"},"cmin":0.80000000000000004,"cmax":17.399999999999999,"colorscale":[["0","rgba(68,1,84,1)"],["0.0416666666666667","rgba(70,19,97,1)"],["0.0833333333333333","rgba(72,32,111,1)"],["0.125","rgba(71,45,122,1)"],["0.166666666666667","rgba(68,58,128,1)"],["0.208333333333333","rgba(64,70,135,1)"],["0.25","rgba(60,82,138,1)"],["0.291666666666667","rgba(56,93,140,1)"],["0.333333333333333","rgba(49,104,142,1)"],["0.375","rgba(46,114,142,1)"],["0.416666666666667","rgba(42,123,142,1)"],["0.458333333333333","rgba(38,133,141,1)"],["0.5","rgba(37,144,140,1)"],["0.541666666666667","rgba(33,154,138,1)"],["0.583333333333333","rgba(39,164,133,1)"],["0.625","rgba(47,174,127,1)"],["0.666666666666667","rgba(53,183,121,1)"],["0.708333333333333","rgba(79,191,110,1)"],["0.75","rgba(98,199,98,1)"],["0.791666666666667","rgba(119,207,85,1)"],["0.833333333333333","rgba(147,214,70,1)"],["0.875","rgba(172,220,52,1)"],["0.916666666666667","rgba(199,225,42,1)"],["0.958333333333333","rgba(226,228,40,1)"],["1","rgba(253,231,37,1)"]],"showscale":true,"color":[0.80000000000000004,17.399999999999999],"line":{"color":"rgba(255,127,14,1)"}},"xaxis":"x","yaxis":"y","frame":null}],"highlight":{"on":"plotly_click","persistent":false,"dynamic":false,"selectize":false,"opacityDim":0.20000000000000001,"selected":{"opacity":1},"debounce":0},"shinyEvents":["plotly_hover","plotly_click","plotly_selected","plotly_relayout","plotly_brushed","plotly_brushing","plotly_clickannotation","plotly_doubleclick","plotly_deselect","plotly_afterplot","plotly_sunburstclick"],"base_url":"https://plot.ly"},"evals":[],"jsHooks":[]}</script>
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


Sums of Squared Errors
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

<img src="03-ROLS_files/figure-html/unnamed-chunk-12-1.png" width="672" />


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
<div class="plotly html-widget html-fill-item-overflow-hidden html-fill-item" id="htmlwidget-2957ddbdcd88d652cbd0" style="width:672px;height:480px;"></div>
<script type="application/json" data-for="htmlwidget-2957ddbdcd88d652cbd0">{"x":{"visdat":{"2f722fb4eceb":["function () ","plotlyVisDat"]},"cur_data":"2f722fb4eceb","attrs":{"2f722fb4eceb":{"x":[0.052642997962285845,0.040801478469323457,0.040935602728793749,0.043017968750892484,0.036938841032154078,0.044804260373237467,0.042964962949070415,0.049214687474997708,0.047986829406784746,0.044251999196216897,0.044568406016771367,0.054955514289893211,0.041016373833306773,0.044221773314322005,0.044697022492597951,0.031250984326667015,0.039234221844662624,0.046714589552645597,0.040940290888041783,0.045546566867141258,0.046536061460558865,0.042491826660883615,0.04046246355616441,0.042643601847090602,0.043618931955011798,0.04689081607203531,0.047121945711399812,0.043922755724643603,0.053528484905738527,0.04032871086012893,0.038547781422523769,0.042878088709822036,0.04887152217552275,0.044950552305783049,0.040993741995647454,0.041512596992188219,0.037693624446867878,0.043460035465790872,0.04516705608469674,0.043281054218148679,0.044045108305718207,0.044478615721400772,0.040947349366127053,0.044497992454377994,0.045489081062407934,0.044886732656467913,0.045644824138284273,0.042387646823234572,0.048065838640807511,0.042590703256042826,0.050024864337711993,0.036995022858481642,0.040814685156124429,0.049106229173394508,0.053024976940854382,0.039744602660325999,0.049207589217279864,0.04531909245359924,0.044147991278847422,0.042520173737643316,0.040647021368851302,0.041512765144039898,0.039657474200505936,0.040140943869352338,0.03463515767563298,0.047417906568894296,0.051050294632165018,0.043130046049612895,0.03924870401246093,0.042800433720487703,0.043836811034702973,0.049838771297971284,0.037679237118763281,0.039539987041964736,0.040639707974942624,0.039769956687837935,0.039171243248986749,0.04637832705000159,0.044687998623867325,0.041810967830884851,0.042152968132249911,0.04016973404847194,0.041294923702333772,0.048071026662161224,0.039956766649328637,0.043545317663182447,0.047631670683441929,0.04158254729110622,0.046451076367572307,0.048961900892495032,0.043706526399311663,0.043067754697055503,0.039449163915634113,0.037757596063774997,0.046371873961154102,0.04032363286212505,0.04630177925377453,0.051425348344363214,0.04846006995900351,0.046892381167221213,0.049972574546039893,0.040786586990038537,0.04206253570525894,0.044540334493680826,0.043410653661739261,0.04611480373492044,0.044353432077843098,0.042546923463874869,0.050148963499000838,0.043518590025664362,0.044186593795437996,0.04391796959290515,0.04461823840295355,0.039380701904586521,0.05310449213138483,0.037507229395484287,0.051587628134919884,0.039142769494928419,0.048450460102657425,0.049529626400196827,0.042926805137821392,0.040784767362386391,0.045553343313159224,0.049155849971137186,0.04347323829918525,0.045930701325088849,0.036191974329128226,0.047057603756285558,0.035668182841776412,0.040975003246540992,0.040874901414922976,0.033492551636873195,0.044269353913742641,0.049119049502449379,0.047868919531647958,0.043002638660592056,0.042596389441307128,0.038886687462070781,0.045414168197072093,0.046290072804638101,0.04130077441457667,0.044353930599613497,0.043459777012720011,0.041278312674083405,0.032786843800355618,0.045395624050333122,0.041984373060481694,0.050377125676396517,0.042583954488185381,0.035097084737095378,0.043684888268690769,0.043691179087374112,0.035181941375112068,0.042858338925853702,0.037730702180605397,0.047063878552827107,0.050059826469496707,0.04505624870576469,0.040189353331436702,0.044250785338746226,0.042556795482672584,0.046735055592570206,0.04068483981423366,0.037541725855276181,0.043910527897424334,0.051639383183537758,0.042150891122565079,0.040562345952967004,0.042012311455076327,0.046350170194907885,0.042955411274895605,0.043153324225435143,0.040128613442963909,0.040585766540960168,0.042753527529916298,0.050435178850202864,0.041055264557576784,0.047855313381664058,0.042318317468654922,0.043426249106045152,0.046569474362258563,0.039861483781457416,0.043471181236001306,0.031972154111555476,0.041576370957471451,0.043560523635171114,0.051779621132945923,0.037071044769188294,0.04195495452211806,0.035205733402664474,0.049718134361177398,0.043272563905217838,0.055258185407516917,0.048715967969121768,0.054538337416947934,0.048127618001743977,0.044700587563308067,0.039667620876519712,0.042804496013825064,0.045113705071974451,0.045645795972642601,0.041044854624810681,0.049273746547925087,0.042081746682427382,0.040199366848288724,0.045885426718059008,0.049056828325833503,0.045769815239671205,0.04157636245946586,0.041841375120786888,0.043144071366415661,0.04835528463458276,0.043270224562617199,0.049418971185384755,0.046074698261823116,0.047960134946642759,0.0404423990634908,0.03854912938507888,0.044463809643332131,0.043632097954187946,0.04810177401481508,0.036525116249416165,0.043284554601615066,0.05099118897175358,0.034146230849352074,0.040963685631192091,0.044840660412508344,0.054088746746191442,0.041456947347054393,0.04991823201264,0.044056002006982613,0.047711449562615471,0.039620138355828699,0.041453035227122306,0.04060398505555797,0.04192633661088626,0.045892328832703964,0.046630869315975786,0.043495538062289237,0.04232038698776338,0.046582987768100215,0.049227330680475204,0.044030347988495401,0.046089835998371395,0.048176476349826906,0.043082372348715384,0.040125484660635702,0.039189777900832286,0.035484830016157161,0.034246174015158781,0.041608147895020035,0.037658440118250959,0.041194527064402089,0.052234249032057929,0.040748936702174762,0.039391554467317749,0.044747972806029303,0.045642050732009054,0.041746011494908676,0.047597691022876448,0.048226473273767612,0.041346434180731535,0.048907659247721967,0.039437587099375615,0.040761427799869548,0.042159092501182452,0.051400976384052915,0.041387915845171847,0.052566578392838917,0.047277401247747666,0.042508899617494794,0.048643526486218114,0.052993568327748146,0.048202575072901939,0.043153324000704825,0.038376919541906883,0.053329064699070519,0.045842556360133645,0.038384592707149473,0.059821088888475496,0.040185666064052439,0.038072975999677475,0.048901073347294099,0.040497327727968865,0.044444656747313502,0.038824764887663114,0.045619423542406161,0.047152184747737698,0.048091311370690594,0.047791074329830104,0.042938515135590383,0.04460928256761329,0.044318046395719436,0.056361163599344274,0.047069088233744713,0.045720735900304836,0.044171528327372804,0.037521486392144469,0.044789842329014694,0.049207252121526233,0.043457443164675348,0.050783424290122545,0.045908696769920251,0.051560854271516625,0.039285576887219023,0.03775449623653665,0.040491967713629173,0.045196553295756683,0.0422355025188745,0.043354401372751011,0.036084490935141683,0.043641122683428332,0.049997518938142742,0.040207185581910776,0.055057784669710674,0.046388355184570476,0.044157841096460718,0.049936390649873333,0.050697589828567771,0.042024558098327114,0.041234256872764823,0.038804539459156434,0.044054946703714862,0.03998565566705483,0.042838690537834255,0.043872297963614519,0.051333093364569267,0.043540173036866935,0.040891345859966996,0.042910833453610589,0.037279246715490752,0.040501899845872706,0.048906435334844962,0.048022073127577204,0.049208844190833552,0.050143464526732684,0.04767767370050853,0.046362248055944195,0.036478171795185137,0.033940371521434809,0.044785024080196301,0.040563583841763694,0.043680258422818793,0.042734808931608879,0.046009872932469817,0.044158645046193622,0.044107857495954007,0.041032819322338918,0.045380424017597412,0.04631337596199208,0.047984323228913953,0.042256925091231481,0.047456709214840145,0.041233897596510694,0.042371374773839857,0.050315965381483883,0.042040643292777569,0.038071617968391563,0.044396675893626197,0.046852137710091279,0.040628182029901719,0.041467514275190215,0.045985908209610425,0.04707879516246493,0.045695568700397184,0.048449261564360607,0.03664620011861467,0.042371202081975673,0.051020980726704919,0.037439759839624366,0.050311959924504025,0.040596123352859045,0.032985303048273164,0.048974783015852529,0.059442866881126967,0.047388521136617366,0.042469090340169192,0.037005819370821792,0.041667311097019676,0.043936306168463002,0.047348316640399311,0.048593352712730263,0.04427629197792099,0.036203023446674629,0.040186172865141569,0.039604969194878541,0.047180824278878347,0.044713255974241958,0.041226867747447854,0.040504103849978407,0.038796868595592671,0.032939954497624074,0.049699575555851021,0.04203910334174564,0.047918969096703873,0.046009672312034344,0.047960013418345979,0.03891629752082508,0.042193193917246942],"y":[-0.081903451165601701,-0.077495672911755395,-0.047385460844986849,-0.027067281588523999,-0.032664667065250293,-0.026067968036116756,-0.021402639699820491,-0.057931770632811873,-0.092026543116480439,-0.052779077347680434,-0.089104034467508544,-0.072476418104293103,-0.037377519571034509,-0.031617838210040376,-0.037000137939184198,-0.066202992199197855,-0.03556500488506651,-0.028536678583704393,-0.049377192479347291,-0.04921843440868888,-0.047934504505556759,-0.032056469246700983,-0.064613783015435342,-0.046838912187379227,-0.075247065494002743,-0.017446219664640009,-0.066338778888815786,-0.034784861119667693,-0.08247413353200557,0.031326592132210763,-0.02724202367898116,-0.11503771270635904,-0.086041759139925109,-0.079375191458983863,0.0099035006374742027,-0.039718618937564301,-0.040609919644254838,-0.055810983591337383,-0.041542183279589043,-0.076559178433139641,-0.039784704194300406,-0.071484042116996827,-0.0030061501697152587,-0.043443773355493577,-0.02978788605546134,-0.017518948402771264,-0.070246648299006453,-0.04811485618218328,-0.070899134461649291,-0.031342696816578419,-0.077521707386032479,-0.046839221675028943,-0.051093736589274942,-0.03897606607273206,-0.06779280116893413,-0.071964524963469612,-0.0464659414429415,-0.042791786386356528,-0.012862398793173925,-0.055710546928876607,-0.06454278306632695,-0.018454914669368827,-0.063267477683203288,-0.065516726143442089,-0.016634167658077573,-0.071261382015116684,-0.060286468573132058,-0.028670075459046662,-0.0048713638774021831,-0.015633460279525564,-0.019014907055733263,-0.062357896978345144,-0.034538003439997765,-0.020599262588826703,-0.069615857484749119,-0.029565700948984693,-0.036858261255474298,-0.026583967384274175,-0.0056422927276350721,-0.029299346293705918,-0.045427879574413389,-0.0065414594761519689,-0.054412574874046812,-0.043060318925756069,-0.046809873700164081,-0.033593692443156256,-0.056223882758745715,-0.080274534750416904,-0.070373184883739476,-0.048113837510789986,-0.063538299498343165,-0.037872952821833686,-0.039618120218359754,-0.044818600494436471,-0.051638940103808144,-0.024023654640416715,-0.027775757782167371,-0.075434170676583284,-0.012734860203653102,-0.067906296957078269,-0.048012628488583821,-0.0062787971581788251,-0.072471890348559137,-0.056019032786510707,-0.042867933661485273,-0.058392600773076168,-0.023000331812767592,-0.0040555054776090461,-0.043181508161705004,-0.028165052863427603,-0.026857680640229739,-0.055747404697452083,-0.041615927053252302,-0.016772411214410886,-0.12959594822126982,-0.062512363496033632,-0.061620779324139036,-0.081145031381763294,-0.082250996018186098,-0.063736334358158633,-0.038741512002944796,-0.024650354292022423,-0.017939611653649042,-0.081395463759484435,-0.048167379839893824,-0.016774382735707846,0.014011397786164522,-0.021638673439556159,0.0056976458317746391,-0.054008658606205531,-0.05524191575364374,-0.01298658859005886,-0.035409294787482837,-0.071001609030053064,-0.038413142488607749,-0.088722448669018392,-0.0086237046502362497,-0.023505058097984012,-0.072236674175036375,-0.047253132715974644,-0.017281432408477678,-0.044326545021727615,-0.020330714030718497,-0.042531483635779833,-0.010365404694293321,-0.046067629675957379,-0.025385137038208459,-0.054934811182074758,-0.060599490375551568,-0.063813437494003325,-0.051059822446890175,-0.059614004504177164,-0.059174597211034297,-0.057594311202839345,-0.052622020149263649,-0.043904115902992431,-0.087742546726883794,-0.048639159059006391,-0.045674176598184832,-0.020787590911159677,-0.028356545263687485,-0.06794336698656997,-0.037783392792528972,-0.024118600425410825,-0.062960144280188923,-0.031294742971456971,-0.039429680401915447,-0.072227759765143423,-0.031354677481922742,-0.082076128020059605,-0.0015008634762965966,-0.018632381791148917,-0.03616101255012065,-0.020536198734698266,-0.027772944458851131,-0.085795057485342288,-0.078504801267684443,-0.064511133054784911,-0.027596378745388853,-0.017274930912723186,-0.047216467807980757,-0.041926045151895269,-0.038423526247442975,-0.031898828901158582,-0.050055620148816114,-0.048595608744219525,-0.071762808377249021,-0.009609044827906716,-0.04499251516122374,-0.036361241048692733,-0.047623301237012375,-0.0033792256590043793,-0.072961866273522705,-0.05102414407880547,-0.089288911882215993,-0.042865549254576779,-0.040784079026465185,-0.0049723541192267734,-0.040477943485843611,-0.092774771498764827,-0.058337230384742748,-0.0092136348782453931,-0.050560329339644106,-0.0045756612343351415,-0.012014135946277751,-0.030948925639670846,-0.091509957289623037,-0.041308317707072231,-0.05113124946338226,-0.051651400632237159,-0.0895312114233284,-0.026132042685286499,-0.011233600792001275,-0.064692709110077296,-0.038184498959253341,-0.059316103185503434,-0.038262160667887748,-0.049513799693641121,-0.041005602935264958,-0.058123803786037542,-0.024484219039390184,-0.024992795080385776,-0.0099097287224914361,-0.068419509562294381,-0.031621589882182152,-0.037618570253361898,-0.089425100585127426,-0.073175628989357436,-0.0052146769241850754,-0.083788058945967595,-0.025237235151095029,-0.052801379248252088,-0.051402644263781751,-0.037520022115962039,-0.049188798507089168,-0.061648692791066925,-0.016852479472977081,-0.037605725752548655,-0.07476306399858805,-0.066748109586128326,-0.083544662061771233,-0.044529048353716946,-0.057753785956827883,-0.075978786136420423,-0.054829369127478059,-0.017173737695027735,-0.046668090931480326,-0.028175718758905764,0.0034805145090774504,-0.035002969458879471,-0.010224180142731049,-0.025777534275599673,-0.051327078831487856,-0.095924747756486253,-0.037269744682031702,-0.055683973021805,-0.11235510070819013,-0.041355999874432531,-0.060527719326749108,-0.0692378135847974,-0.080632550486664095,0.0059107817204400127,-0.044108288609566684,-0.064763723012573271,0.014969104740271022,-0.036164913211784305,-0.10901785344595363,-0.069584123134967021,-0.080315398988395459,-0.084208448909847439,-0.045452878678807533,-0.084858007779085282,-0.051477382938856293,-0.094203732490758238,-0.043570056963173599,0.014663709505303981,-0.065367506409766213,-0.031680323588558532,-0.10157951995539874,-0.1161932836898268,-0.042715980013983135,-0.005071058409733032,-0.057485030365446638,-0.01539990894615015,-0.0080209923150562495,-0.037174409699898422,-0.055539526811853528,-0.02978748597819773,-0.044875882596797499,-0.013061698192473546,-0.054048709415279013,-0.062152036917824956,-0.066112470391113509,-0.096907935909493342,-0.040824236217912542,-0.015498782553125569,-0.0040695107301233231,-0.0078528786260042959,-0.066738678800044526,-0.096229688750022857,-0.079964169406396557,-0.058994221836592531,-0.032802381363871799,-0.057249308792291939,-0.01968556907720773,-0.041294791565097591,-0.019189552800767094,-0.041179065923050172,-0.036819199403001247,-0.021976566180714724,-0.017647813157866246,-0.076383302619172561,-0.082759957473615142,-0.061571407203665288,-0.13831644086362413,-0.060864740059138403,-0.050755736104456245,-0.058067949161440952,-0.082324614910308971,-0.070033164186094329,-0.017184884497500805,-0.063389076944187966,-0.065102563152614437,-0.04269401264856592,-0.05724705018315613,-0.0011774937990925484,-0.028233243987107887,-0.085822086834290615,-0.048037432725468704,-0.032449703496725685,-0.042964459822022863,-0.048550525329425012,-0.061411496202944942,-0.064078914375952853,-0.06080699106355094,-0.075733358840474052,-0.055514278224782089,-0.026007863387374385,-0.0038309087909662496,-0.025326123375252547,-0.08831761348625107,-0.026105900497968872,-0.043315870315062378,-0.013034569615116908,-0.064525451073255288,-0.092290381801014093,-0.067877550809394407,-0.0074688004960390287,-0.071475597261052348,-0.003238217245113749,-0.029221180116512698,-0.038074187236780903,-0.032183311263791564,-0.059661990377419406,-0.01745243036972877,-0.047247973054695906,-0.018008182312839745,-0.070864701545322997,-0.066927043566413297,-0.063320259543241386,-0.02616138525550981,-0.042330303290041199,-0.042363792499824811,-0.02568393076716197,-0.04170840774359489,-0.044154557440109488,-0.046032780874251798,-0.03850922068514661,-0.055245462424224422,-0.046454876835975323,-0.070669332879459174,-0.038950590007478941,-0.029680165821683951,-0.060916531999044593,-0.10172090009361044,-0.055200818642906622,-0.036137066487297698,-0.017142737510590245,-0.015733621075578828,-0.035256684964240413,-0.040384191217214857,-0.041615401389595491,-0.045624815291493447,-0.0097699879698969899,0.010918588566359083,-0.040731236998668145,-0.048841898122088508,-0.043017124263799639,-0.027002552946293838,-0.045539798292360094,-0.035172955223464801,-0.021128793934253588,-0.051768712179352604,-0.051311672778627068,-0.031162274861655043,-0.056937637375574807,-0.043294379325133761,-0.0071061982308987907,-0.010899402003809421],"alpha_stroke":1,"sizes":[10,100],"spans":[1,20],"type":"histogram2d","nbinsx":20,"nbinsy":20,"inherit":true}},"layout":{"margin":{"b":40,"l":60,"t":25,"r":10},"xaxis":{"domain":[0,1],"automargin":true,"title":[]},"yaxis":{"domain":[0,1],"automargin":true,"title":[]},"hovermode":"closest","showlegend":false,"legend":{"yanchor":"top","y":0.5}},"source":"A","config":{"modeBarButtonsToAdd":["hoverclosest","hovercompare"],"showSendToCloud":false},"data":[{"colorbar":{"title":"","ticklen":2,"len":0.5,"lenmode":"fraction","y":1,"yanchor":"top"},"colorscale":[["0","rgba(68,1,84,1)"],["0.0416666666666667","rgba(70,19,97,1)"],["0.0833333333333333","rgba(72,32,111,1)"],["0.125","rgba(71,45,122,1)"],["0.166666666666667","rgba(68,58,128,1)"],["0.208333333333333","rgba(64,70,135,1)"],["0.25","rgba(60,82,138,1)"],["0.291666666666667","rgba(56,93,140,1)"],["0.333333333333333","rgba(49,104,142,1)"],["0.375","rgba(46,114,142,1)"],["0.416666666666667","rgba(42,123,142,1)"],["0.458333333333333","rgba(38,133,141,1)"],["0.5","rgba(37,144,140,1)"],["0.541666666666667","rgba(33,154,138,1)"],["0.583333333333333","rgba(39,164,133,1)"],["0.625","rgba(47,174,127,1)"],["0.666666666666667","rgba(53,183,121,1)"],["0.708333333333333","rgba(79,191,110,1)"],["0.75","rgba(98,199,98,1)"],["0.791666666666667","rgba(119,207,85,1)"],["0.833333333333333","rgba(147,214,70,1)"],["0.875","rgba(172,220,52,1)"],["0.916666666666667","rgba(199,225,42,1)"],["0.958333333333333","rgba(226,228,40,1)"],["1","rgba(253,231,37,1)"]],"showscale":true,"x":[0.052642997962285845,0.040801478469323457,0.040935602728793749,0.043017968750892484,0.036938841032154078,0.044804260373237467,0.042964962949070415,0.049214687474997708,0.047986829406784746,0.044251999196216897,0.044568406016771367,0.054955514289893211,0.041016373833306773,0.044221773314322005,0.044697022492597951,0.031250984326667015,0.039234221844662624,0.046714589552645597,0.040940290888041783,0.045546566867141258,0.046536061460558865,0.042491826660883615,0.04046246355616441,0.042643601847090602,0.043618931955011798,0.04689081607203531,0.047121945711399812,0.043922755724643603,0.053528484905738527,0.04032871086012893,0.038547781422523769,0.042878088709822036,0.04887152217552275,0.044950552305783049,0.040993741995647454,0.041512596992188219,0.037693624446867878,0.043460035465790872,0.04516705608469674,0.043281054218148679,0.044045108305718207,0.044478615721400772,0.040947349366127053,0.044497992454377994,0.045489081062407934,0.044886732656467913,0.045644824138284273,0.042387646823234572,0.048065838640807511,0.042590703256042826,0.050024864337711993,0.036995022858481642,0.040814685156124429,0.049106229173394508,0.053024976940854382,0.039744602660325999,0.049207589217279864,0.04531909245359924,0.044147991278847422,0.042520173737643316,0.040647021368851302,0.041512765144039898,0.039657474200505936,0.040140943869352338,0.03463515767563298,0.047417906568894296,0.051050294632165018,0.043130046049612895,0.03924870401246093,0.042800433720487703,0.043836811034702973,0.049838771297971284,0.037679237118763281,0.039539987041964736,0.040639707974942624,0.039769956687837935,0.039171243248986749,0.04637832705000159,0.044687998623867325,0.041810967830884851,0.042152968132249911,0.04016973404847194,0.041294923702333772,0.048071026662161224,0.039956766649328637,0.043545317663182447,0.047631670683441929,0.04158254729110622,0.046451076367572307,0.048961900892495032,0.043706526399311663,0.043067754697055503,0.039449163915634113,0.037757596063774997,0.046371873961154102,0.04032363286212505,0.04630177925377453,0.051425348344363214,0.04846006995900351,0.046892381167221213,0.049972574546039893,0.040786586990038537,0.04206253570525894,0.044540334493680826,0.043410653661739261,0.04611480373492044,0.044353432077843098,0.042546923463874869,0.050148963499000838,0.043518590025664362,0.044186593795437996,0.04391796959290515,0.04461823840295355,0.039380701904586521,0.05310449213138483,0.037507229395484287,0.051587628134919884,0.039142769494928419,0.048450460102657425,0.049529626400196827,0.042926805137821392,0.040784767362386391,0.045553343313159224,0.049155849971137186,0.04347323829918525,0.045930701325088849,0.036191974329128226,0.047057603756285558,0.035668182841776412,0.040975003246540992,0.040874901414922976,0.033492551636873195,0.044269353913742641,0.049119049502449379,0.047868919531647958,0.043002638660592056,0.042596389441307128,0.038886687462070781,0.045414168197072093,0.046290072804638101,0.04130077441457667,0.044353930599613497,0.043459777012720011,0.041278312674083405,0.032786843800355618,0.045395624050333122,0.041984373060481694,0.050377125676396517,0.042583954488185381,0.035097084737095378,0.043684888268690769,0.043691179087374112,0.035181941375112068,0.042858338925853702,0.037730702180605397,0.047063878552827107,0.050059826469496707,0.04505624870576469,0.040189353331436702,0.044250785338746226,0.042556795482672584,0.046735055592570206,0.04068483981423366,0.037541725855276181,0.043910527897424334,0.051639383183537758,0.042150891122565079,0.040562345952967004,0.042012311455076327,0.046350170194907885,0.042955411274895605,0.043153324225435143,0.040128613442963909,0.040585766540960168,0.042753527529916298,0.050435178850202864,0.041055264557576784,0.047855313381664058,0.042318317468654922,0.043426249106045152,0.046569474362258563,0.039861483781457416,0.043471181236001306,0.031972154111555476,0.041576370957471451,0.043560523635171114,0.051779621132945923,0.037071044769188294,0.04195495452211806,0.035205733402664474,0.049718134361177398,0.043272563905217838,0.055258185407516917,0.048715967969121768,0.054538337416947934,0.048127618001743977,0.044700587563308067,0.039667620876519712,0.042804496013825064,0.045113705071974451,0.045645795972642601,0.041044854624810681,0.049273746547925087,0.042081746682427382,0.040199366848288724,0.045885426718059008,0.049056828325833503,0.045769815239671205,0.04157636245946586,0.041841375120786888,0.043144071366415661,0.04835528463458276,0.043270224562617199,0.049418971185384755,0.046074698261823116,0.047960134946642759,0.0404423990634908,0.03854912938507888,0.044463809643332131,0.043632097954187946,0.04810177401481508,0.036525116249416165,0.043284554601615066,0.05099118897175358,0.034146230849352074,0.040963685631192091,0.044840660412508344,0.054088746746191442,0.041456947347054393,0.04991823201264,0.044056002006982613,0.047711449562615471,0.039620138355828699,0.041453035227122306,0.04060398505555797,0.04192633661088626,0.045892328832703964,0.046630869315975786,0.043495538062289237,0.04232038698776338,0.046582987768100215,0.049227330680475204,0.044030347988495401,0.046089835998371395,0.048176476349826906,0.043082372348715384,0.040125484660635702,0.039189777900832286,0.035484830016157161,0.034246174015158781,0.041608147895020035,0.037658440118250959,0.041194527064402089,0.052234249032057929,0.040748936702174762,0.039391554467317749,0.044747972806029303,0.045642050732009054,0.041746011494908676,0.047597691022876448,0.048226473273767612,0.041346434180731535,0.048907659247721967,0.039437587099375615,0.040761427799869548,0.042159092501182452,0.051400976384052915,0.041387915845171847,0.052566578392838917,0.047277401247747666,0.042508899617494794,0.048643526486218114,0.052993568327748146,0.048202575072901939,0.043153324000704825,0.038376919541906883,0.053329064699070519,0.045842556360133645,0.038384592707149473,0.059821088888475496,0.040185666064052439,0.038072975999677475,0.048901073347294099,0.040497327727968865,0.044444656747313502,0.038824764887663114,0.045619423542406161,0.047152184747737698,0.048091311370690594,0.047791074329830104,0.042938515135590383,0.04460928256761329,0.044318046395719436,0.056361163599344274,0.047069088233744713,0.045720735900304836,0.044171528327372804,0.037521486392144469,0.044789842329014694,0.049207252121526233,0.043457443164675348,0.050783424290122545,0.045908696769920251,0.051560854271516625,0.039285576887219023,0.03775449623653665,0.040491967713629173,0.045196553295756683,0.0422355025188745,0.043354401372751011,0.036084490935141683,0.043641122683428332,0.049997518938142742,0.040207185581910776,0.055057784669710674,0.046388355184570476,0.044157841096460718,0.049936390649873333,0.050697589828567771,0.042024558098327114,0.041234256872764823,0.038804539459156434,0.044054946703714862,0.03998565566705483,0.042838690537834255,0.043872297963614519,0.051333093364569267,0.043540173036866935,0.040891345859966996,0.042910833453610589,0.037279246715490752,0.040501899845872706,0.048906435334844962,0.048022073127577204,0.049208844190833552,0.050143464526732684,0.04767767370050853,0.046362248055944195,0.036478171795185137,0.033940371521434809,0.044785024080196301,0.040563583841763694,0.043680258422818793,0.042734808931608879,0.046009872932469817,0.044158645046193622,0.044107857495954007,0.041032819322338918,0.045380424017597412,0.04631337596199208,0.047984323228913953,0.042256925091231481,0.047456709214840145,0.041233897596510694,0.042371374773839857,0.050315965381483883,0.042040643292777569,0.038071617968391563,0.044396675893626197,0.046852137710091279,0.040628182029901719,0.041467514275190215,0.045985908209610425,0.04707879516246493,0.045695568700397184,0.048449261564360607,0.03664620011861467,0.042371202081975673,0.051020980726704919,0.037439759839624366,0.050311959924504025,0.040596123352859045,0.032985303048273164,0.048974783015852529,0.059442866881126967,0.047388521136617366,0.042469090340169192,0.037005819370821792,0.041667311097019676,0.043936306168463002,0.047348316640399311,0.048593352712730263,0.04427629197792099,0.036203023446674629,0.040186172865141569,0.039604969194878541,0.047180824278878347,0.044713255974241958,0.041226867747447854,0.040504103849978407,0.038796868595592671,0.032939954497624074,0.049699575555851021,0.04203910334174564,0.047918969096703873,0.046009672312034344,0.047960013418345979,0.03891629752082508,0.042193193917246942],"y":[-0.081903451165601701,-0.077495672911755395,-0.047385460844986849,-0.027067281588523999,-0.032664667065250293,-0.026067968036116756,-0.021402639699820491,-0.057931770632811873,-0.092026543116480439,-0.052779077347680434,-0.089104034467508544,-0.072476418104293103,-0.037377519571034509,-0.031617838210040376,-0.037000137939184198,-0.066202992199197855,-0.03556500488506651,-0.028536678583704393,-0.049377192479347291,-0.04921843440868888,-0.047934504505556759,-0.032056469246700983,-0.064613783015435342,-0.046838912187379227,-0.075247065494002743,-0.017446219664640009,-0.066338778888815786,-0.034784861119667693,-0.08247413353200557,0.031326592132210763,-0.02724202367898116,-0.11503771270635904,-0.086041759139925109,-0.079375191458983863,0.0099035006374742027,-0.039718618937564301,-0.040609919644254838,-0.055810983591337383,-0.041542183279589043,-0.076559178433139641,-0.039784704194300406,-0.071484042116996827,-0.0030061501697152587,-0.043443773355493577,-0.02978788605546134,-0.017518948402771264,-0.070246648299006453,-0.04811485618218328,-0.070899134461649291,-0.031342696816578419,-0.077521707386032479,-0.046839221675028943,-0.051093736589274942,-0.03897606607273206,-0.06779280116893413,-0.071964524963469612,-0.0464659414429415,-0.042791786386356528,-0.012862398793173925,-0.055710546928876607,-0.06454278306632695,-0.018454914669368827,-0.063267477683203288,-0.065516726143442089,-0.016634167658077573,-0.071261382015116684,-0.060286468573132058,-0.028670075459046662,-0.0048713638774021831,-0.015633460279525564,-0.019014907055733263,-0.062357896978345144,-0.034538003439997765,-0.020599262588826703,-0.069615857484749119,-0.029565700948984693,-0.036858261255474298,-0.026583967384274175,-0.0056422927276350721,-0.029299346293705918,-0.045427879574413389,-0.0065414594761519689,-0.054412574874046812,-0.043060318925756069,-0.046809873700164081,-0.033593692443156256,-0.056223882758745715,-0.080274534750416904,-0.070373184883739476,-0.048113837510789986,-0.063538299498343165,-0.037872952821833686,-0.039618120218359754,-0.044818600494436471,-0.051638940103808144,-0.024023654640416715,-0.027775757782167371,-0.075434170676583284,-0.012734860203653102,-0.067906296957078269,-0.048012628488583821,-0.0062787971581788251,-0.072471890348559137,-0.056019032786510707,-0.042867933661485273,-0.058392600773076168,-0.023000331812767592,-0.0040555054776090461,-0.043181508161705004,-0.028165052863427603,-0.026857680640229739,-0.055747404697452083,-0.041615927053252302,-0.016772411214410886,-0.12959594822126982,-0.062512363496033632,-0.061620779324139036,-0.081145031381763294,-0.082250996018186098,-0.063736334358158633,-0.038741512002944796,-0.024650354292022423,-0.017939611653649042,-0.081395463759484435,-0.048167379839893824,-0.016774382735707846,0.014011397786164522,-0.021638673439556159,0.0056976458317746391,-0.054008658606205531,-0.05524191575364374,-0.01298658859005886,-0.035409294787482837,-0.071001609030053064,-0.038413142488607749,-0.088722448669018392,-0.0086237046502362497,-0.023505058097984012,-0.072236674175036375,-0.047253132715974644,-0.017281432408477678,-0.044326545021727615,-0.020330714030718497,-0.042531483635779833,-0.010365404694293321,-0.046067629675957379,-0.025385137038208459,-0.054934811182074758,-0.060599490375551568,-0.063813437494003325,-0.051059822446890175,-0.059614004504177164,-0.059174597211034297,-0.057594311202839345,-0.052622020149263649,-0.043904115902992431,-0.087742546726883794,-0.048639159059006391,-0.045674176598184832,-0.020787590911159677,-0.028356545263687485,-0.06794336698656997,-0.037783392792528972,-0.024118600425410825,-0.062960144280188923,-0.031294742971456971,-0.039429680401915447,-0.072227759765143423,-0.031354677481922742,-0.082076128020059605,-0.0015008634762965966,-0.018632381791148917,-0.03616101255012065,-0.020536198734698266,-0.027772944458851131,-0.085795057485342288,-0.078504801267684443,-0.064511133054784911,-0.027596378745388853,-0.017274930912723186,-0.047216467807980757,-0.041926045151895269,-0.038423526247442975,-0.031898828901158582,-0.050055620148816114,-0.048595608744219525,-0.071762808377249021,-0.009609044827906716,-0.04499251516122374,-0.036361241048692733,-0.047623301237012375,-0.0033792256590043793,-0.072961866273522705,-0.05102414407880547,-0.089288911882215993,-0.042865549254576779,-0.040784079026465185,-0.0049723541192267734,-0.040477943485843611,-0.092774771498764827,-0.058337230384742748,-0.0092136348782453931,-0.050560329339644106,-0.0045756612343351415,-0.012014135946277751,-0.030948925639670846,-0.091509957289623037,-0.041308317707072231,-0.05113124946338226,-0.051651400632237159,-0.0895312114233284,-0.026132042685286499,-0.011233600792001275,-0.064692709110077296,-0.038184498959253341,-0.059316103185503434,-0.038262160667887748,-0.049513799693641121,-0.041005602935264958,-0.058123803786037542,-0.024484219039390184,-0.024992795080385776,-0.0099097287224914361,-0.068419509562294381,-0.031621589882182152,-0.037618570253361898,-0.089425100585127426,-0.073175628989357436,-0.0052146769241850754,-0.083788058945967595,-0.025237235151095029,-0.052801379248252088,-0.051402644263781751,-0.037520022115962039,-0.049188798507089168,-0.061648692791066925,-0.016852479472977081,-0.037605725752548655,-0.07476306399858805,-0.066748109586128326,-0.083544662061771233,-0.044529048353716946,-0.057753785956827883,-0.075978786136420423,-0.054829369127478059,-0.017173737695027735,-0.046668090931480326,-0.028175718758905764,0.0034805145090774504,-0.035002969458879471,-0.010224180142731049,-0.025777534275599673,-0.051327078831487856,-0.095924747756486253,-0.037269744682031702,-0.055683973021805,-0.11235510070819013,-0.041355999874432531,-0.060527719326749108,-0.0692378135847974,-0.080632550486664095,0.0059107817204400127,-0.044108288609566684,-0.064763723012573271,0.014969104740271022,-0.036164913211784305,-0.10901785344595363,-0.069584123134967021,-0.080315398988395459,-0.084208448909847439,-0.045452878678807533,-0.084858007779085282,-0.051477382938856293,-0.094203732490758238,-0.043570056963173599,0.014663709505303981,-0.065367506409766213,-0.031680323588558532,-0.10157951995539874,-0.1161932836898268,-0.042715980013983135,-0.005071058409733032,-0.057485030365446638,-0.01539990894615015,-0.0080209923150562495,-0.037174409699898422,-0.055539526811853528,-0.02978748597819773,-0.044875882596797499,-0.013061698192473546,-0.054048709415279013,-0.062152036917824956,-0.066112470391113509,-0.096907935909493342,-0.040824236217912542,-0.015498782553125569,-0.0040695107301233231,-0.0078528786260042959,-0.066738678800044526,-0.096229688750022857,-0.079964169406396557,-0.058994221836592531,-0.032802381363871799,-0.057249308792291939,-0.01968556907720773,-0.041294791565097591,-0.019189552800767094,-0.041179065923050172,-0.036819199403001247,-0.021976566180714724,-0.017647813157866246,-0.076383302619172561,-0.082759957473615142,-0.061571407203665288,-0.13831644086362413,-0.060864740059138403,-0.050755736104456245,-0.058067949161440952,-0.082324614910308971,-0.070033164186094329,-0.017184884497500805,-0.063389076944187966,-0.065102563152614437,-0.04269401264856592,-0.05724705018315613,-0.0011774937990925484,-0.028233243987107887,-0.085822086834290615,-0.048037432725468704,-0.032449703496725685,-0.042964459822022863,-0.048550525329425012,-0.061411496202944942,-0.064078914375952853,-0.06080699106355094,-0.075733358840474052,-0.055514278224782089,-0.026007863387374385,-0.0038309087909662496,-0.025326123375252547,-0.08831761348625107,-0.026105900497968872,-0.043315870315062378,-0.013034569615116908,-0.064525451073255288,-0.092290381801014093,-0.067877550809394407,-0.0074688004960390287,-0.071475597261052348,-0.003238217245113749,-0.029221180116512698,-0.038074187236780903,-0.032183311263791564,-0.059661990377419406,-0.01745243036972877,-0.047247973054695906,-0.018008182312839745,-0.070864701545322997,-0.066927043566413297,-0.063320259543241386,-0.02616138525550981,-0.042330303290041199,-0.042363792499824811,-0.02568393076716197,-0.04170840774359489,-0.044154557440109488,-0.046032780874251798,-0.03850922068514661,-0.055245462424224422,-0.046454876835975323,-0.070669332879459174,-0.038950590007478941,-0.029680165821683951,-0.060916531999044593,-0.10172090009361044,-0.055200818642906622,-0.036137066487297698,-0.017142737510590245,-0.015733621075578828,-0.035256684964240413,-0.040384191217214857,-0.041615401389595491,-0.045624815291493447,-0.0097699879698969899,0.010918588566359083,-0.040731236998668145,-0.048841898122088508,-0.043017124263799639,-0.027002552946293838,-0.045539798292360094,-0.035172955223464801,-0.021128793934253588,-0.051768712179352604,-0.051311672778627068,-0.031162274861655043,-0.056937637375574807,-0.043294379325133761,-0.0071061982308987907,-0.010899402003809421],"type":"histogram2d","nbinsx":20,"nbinsy":20,"marker":{"line":{"color":"rgba(31,119,180,1)"}},"xaxis":"x","yaxis":"y","frame":null}],"highlight":{"on":"plotly_click","persistent":false,"dynamic":false,"selectize":false,"opacityDim":0.20000000000000001,"selected":{"opacity":1},"debounce":0},"shinyEvents":["plotly_hover","plotly_click","plotly_selected","plotly_relayout","plotly_brushed","plotly_brushing","plotly_clickannotation","plotly_doubleclick","plotly_deselect","plotly_afterplot","plotly_sunburstclick"],"base_url":"https://plot.ly"},"evals":[],"jsHooks":[]}</script>
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

<img src="03-ROLS_files/figure-html/unnamed-chunk-16-1.png" width="672" />

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


Generate a simulated dataset with 30 observations and two exogenous variables. Assume the following relationship: $yi = \beta_0 + \beta_1 x_{1,i} + \beta_2 x_{2,i} + \epsilon_i$ where the variables and the error term are realizations of the following data generating processes (DGP):

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
##    9.128378    2.087306   -1.243350
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

<img src="03-ROLS_files/figure-html/unnamed-chunk-18-1.png" width="672" />


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

<img src="03-ROLS_files/figure-html/unnamed-chunk-19-1.png" width="672" />

## Factor Variables

So far, we have discussed cardinal data where the difference between units always means the same thing: e.g., $4 -3=3-2$. There are also factor variables

* Ordered: The difference between units means something, but not always the same thing. E.g., $1st - 2nd \neq 2nd - 3rd$.
* Unordered: The difference between units does not mean something $B-A =??$

Sometimes Ordinal and Categorical data are called Ordinal and Categorical variables. 

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
## -31.749  -6.491  -0.166   5.952  41.151 
## 
## Coefficients:
##             Estimate Std. Error t value Pr(>|t|)    
## (Intercept)  20.4211     1.2423  16.438  < 2e-16 ***
## x             1.0452     0.2071   5.047 5.34e-07 ***
## fo.L         26.2420     1.0737  24.441  < 2e-16 ***
## fo.Q          8.4317     0.9454   8.919  < 2e-16 ***
## fo.C          1.9211     0.7477   2.569   0.0103 *  
## fo^4         -0.3942     0.5757  -0.685   0.4937    
## fuB         -24.4561     0.6012 -40.677  < 2e-16 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 9.499 on 993 degrees of freedom
## Multiple R-squared:  0.7153,	Adjusted R-squared:  0.7136 
## F-statistic: 415.9 on 6 and 993 DF,  p-value: < 2.2e-16
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
## x  1.04517   0.414008 2.52452 0.065043 .  
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## RMSE: 9.46541     Adj. R2: 0.713607
##                 Within R2: 0.025011
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
## x  1.02533   0.502079 2.04217 0.071514 .  
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## RMSE: 3.33598     Adj. R2: 0.964282
##                 Within R2: 0.165442
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
## -9.9527 -1.4995 -0.1032  1.5492 10.8650 
## 
## Coefficients:
##              Estimate Std. Error t value Pr(>|t|)    
## (Intercept)  15.85889    0.59083  26.842  < 2e-16 ***
## x             2.36432    0.10219  23.137  < 2e-16 ***
## fo.L         29.73451    1.66417  17.868  < 2e-16 ***
## fo.Q         12.08475    1.46143   8.269 4.36e-16 ***
## fo.C          4.08007    1.14814   3.554 0.000398 ***
## fo^4          1.28348    0.87070   1.474 0.140779    
## fuB         -15.59240    0.83872 -18.591  < 2e-16 ***
## x:fo.L        4.27380    0.28660  14.912  < 2e-16 ***
## x:fo.Q        1.44516    0.25213   5.732 1.32e-08 ***
## x:fo.C        0.07966    0.19955   0.399 0.689841    
## x:fo^4       -0.18291    0.15273  -1.198 0.231349    
## x:fuB        -2.44360    0.14740 -16.578  < 2e-16 ***
## fo.L:fuB    -27.97796    2.36129 -11.849  < 2e-16 ***
## fo.Q:fuB    -11.67964    2.07548  -5.627 2.39e-08 ***
## fo.C:fuB     -2.35275    1.62752  -1.446 0.148608    
## fo^4:fuB     -0.82052    1.23976  -0.662 0.508231    
## x:fo.L:fuB   -4.64681    0.41477 -11.203  < 2e-16 ***
## x:fo.Q:fuB   -1.58208    0.36443  -4.341 1.56e-05 ***
## x:fo.C:fuB   -0.42091    0.28667  -1.468 0.142357    
## x:fo^4:fuB    0.07381    0.21797   0.339 0.734953    
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 2.599 on 980 degrees of freedom
## Multiple R-squared:  0.979,	Adjusted R-squared:  0.9786 
## F-statistic:  2400 on 19 and 980 DF,  p-value: < 2.2e-16
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

<img src="03-ROLS_files/figure-html/unnamed-chunk-24-1.png" width="672" />
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

<img src="03-ROLS_files/figure-html/unnamed-chunk-25-1.png" width="672" />

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

<img src="03-ROLS_files/figure-html/unnamed-chunk-26-1.png" width="672" />

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
## 21 
## 21
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

<img src="03-ROLS_files/figure-html/unnamed-chunk-28-1.png" width="672" />

```
##       StudRes        Hat      CookD
## 1  -1.7254560 0.84307284 7.60179245
## 8   2.1929731 0.02852086 0.06416205
## 21  2.8564028 0.02833577 0.10010752
## 40 -0.6877953 0.04147049 0.01037735
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
##         dfb.1_         dfb.x        dffit     cov.r       cook.d        hat
## 1  3.088084020 -3.939588e+00 -3.999331289 5.7576383 7.601792e+00 0.84307284
## 2  0.044064881  2.019585e-02  0.126647593 1.0477661 8.103134e-03 0.02565231
## 3 -0.002541388  1.524401e-03 -0.002898103 1.0925319 4.312973e-06 0.03456264
## 4  0.002377938 -7.255395e-05  0.004696091 1.0817866 1.132439e-05 0.02500597
## 5 -0.037968687 -1.480231e-02 -0.104198967 1.0585418 5.513640e-03 0.02551490
## 6  0.303668767 -1.887792e-01  0.340033343 0.9324281 5.480598e-02 0.03613882
```


## Assessing Normality and Collinearity

The second plot examines whether the residuals are normally distributed. OLS point estimates do not depend on the normality of the residuals. (Good thing, because there's no reason the residuals of economic phenomena should be so well behaved.) Many hypothesis tests of the regression estimates are, however, affected by the distribution of the residuals. For these reasons, you may be interested in assessing normality 

```r
par(mfrow=c(1,2))
hist(resid(reg), main='Histogram of Residuals')

qqnorm(resid(reg), main="Normal Q-Q Plot of Residuals", col="darkgrey")
qqline(resid(reg), col="dodgerblue", lwd=2)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-32-1.png" width="672" />

```r
shapiro.test(resid(reg))
```

```
## 
## 	Shapiro-Wilk normality test
## 
## data:  resid(reg)
## W = 0.89132, p-value = 0.001079
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
## BP = 0.021162, df = 1, p-value = 0.8843
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

<img src="03-ROLS_files/figure-html/unnamed-chunk-35-1.png" width="672" />

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

<img src="03-ROLS_files/figure-html/unnamed-chunk-35-2.png" width="672" />

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

These endogeneity issues imply $X$ and $\epsilon$ are correlated, which is a barrier to interpreting OLS as a causal model. Three statistical tools: 2SLS, RDD, and DID, are designed to address endogeneity issues. The elementary versions of these tools are linear regression. Because there are many textbooks and online notebooks that explain these methods at both high and low levels of technical detail, they are not covered extensively in this notebook. You are directed to the following resources which discuss these statistical models in more general terms and how they can be applied across many social sciences.

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

<img src="03-ROLS_files/figure-html/unnamed-chunk-39-1.png" width="672" />



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

<img src="03-ROLS_files/figure-html/unnamed-chunk-40-1.png" width="672" />




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

<img src="03-ROLS_files/figure-html/unnamed-chunk-43-1.png" width="672" />


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

<img src="03-ROLS_files/figure-html/unnamed-chunk-44-1.png" width="672" />


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

<img src="03-ROLS_files/figure-html/unnamed-chunk-45-1.png" width="672" />


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

<img src="03-ROLS_files/figure-html/unnamed-chunk-47-1.png" width="672" />


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



