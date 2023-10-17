
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
## [1] 0.6390977
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
<div class="plotly html-widget html-fill-item-overflow-hidden html-fill-item" id="htmlwidget-b93ea5e5009acebc4b84" style="width:672px;height:480px;"></div>
<script type="application/json" data-for="htmlwidget-b93ea5e5009acebc4b84">{"x":{"visdat":{"665616ec6eee":["function () ","plotlyVisDat"]},"cur_data":"665616ec6eee","attrs":{"665616ec6eee":{"x":{},"y":{},"text":{},"mode":"markers","hoverinfo":"text","showlegend":false,"marker":{"size":{},"opacity":0.5,"showscale":true,"colorbar":{"title":"Murder Arrests (per 100,000)"}},"color":{},"alpha_stroke":1,"sizes":[10,100],"spans":[1,20],"type":"scatter"}},"layout":{"margin":{"b":40,"l":60,"t":25,"r":10},"title":"Crime and Urbanization in America 1975","xaxis":{"domain":[0,1],"automargin":true,"title":"Percent of People in an Urban Area"},"yaxis":{"domain":[0,1],"automargin":true,"title":"Assault Arrests per 100,000 People"},"hovermode":"closest","showlegend":false},"source":"A","config":{"modeBarButtonsToAdd":["hoverclosest","hovercompare"],"showSendToCloud":false},"data":[{"x":[58,48,80,50,91,78,77,72,80,60,83,54,83,65,57,66,52,66,51,67,85,74,66,44,70,53,62,81,56,89,70,86,45,44,75,68,67,72,87,48,45,59,80,80,32,63,73,39,66,60],"y":[236,263,294,190,276,204,110,238,335,211,46,120,249,113,56,115,109,249,83,300,149,255,72,259,178,109,102,252,57,159,285,254,337,45,120,151,159,106,174,279,86,188,201,120,48,156,145,81,53,161],"text":["<b> Alabama <\/b> <br>Urban  : 58 <br>Assault: 236 <br>Murder : 13.2","<b> Alaska <\/b> <br>Urban  : 48 <br>Assault: 263 <br>Murder : 10","<b> Arizona <\/b> <br>Urban  : 80 <br>Assault: 294 <br>Murder : 8.1","<b> Arkansas <\/b> <br>Urban  : 50 <br>Assault: 190 <br>Murder : 8.8","<b> California <\/b> <br>Urban  : 91 <br>Assault: 276 <br>Murder : 9","<b> Colorado <\/b> <br>Urban  : 78 <br>Assault: 204 <br>Murder : 7.9","<b> Connecticut <\/b> <br>Urban  : 77 <br>Assault: 110 <br>Murder : 3.3","<b> Delaware <\/b> <br>Urban  : 72 <br>Assault: 238 <br>Murder : 5.9","<b> Florida <\/b> <br>Urban  : 80 <br>Assault: 335 <br>Murder : 15.4","<b> Georgia <\/b> <br>Urban  : 60 <br>Assault: 211 <br>Murder : 17.4","<b> Hawaii <\/b> <br>Urban  : 83 <br>Assault: 46 <br>Murder : 5.3","<b> Idaho <\/b> <br>Urban  : 54 <br>Assault: 120 <br>Murder : 2.6","<b> Illinois <\/b> <br>Urban  : 83 <br>Assault: 249 <br>Murder : 10.4","<b> Indiana <\/b> <br>Urban  : 65 <br>Assault: 113 <br>Murder : 7.2","<b> Iowa <\/b> <br>Urban  : 57 <br>Assault: 56 <br>Murder : 2.2","<b> Kansas <\/b> <br>Urban  : 66 <br>Assault: 115 <br>Murder : 6","<b> Kentucky <\/b> <br>Urban  : 52 <br>Assault: 109 <br>Murder : 9.7","<b> Louisiana <\/b> <br>Urban  : 66 <br>Assault: 249 <br>Murder : 15.4","<b> Maine <\/b> <br>Urban  : 51 <br>Assault: 83 <br>Murder : 2.1","<b> Maryland <\/b> <br>Urban  : 67 <br>Assault: 300 <br>Murder : 11.3","<b> Massachusetts <\/b> <br>Urban  : 85 <br>Assault: 149 <br>Murder : 4.4","<b> Michigan <\/b> <br>Urban  : 74 <br>Assault: 255 <br>Murder : 12.1","<b> Minnesota <\/b> <br>Urban  : 66 <br>Assault: 72 <br>Murder : 2.7","<b> Mississippi <\/b> <br>Urban  : 44 <br>Assault: 259 <br>Murder : 16.1","<b> Missouri <\/b> <br>Urban  : 70 <br>Assault: 178 <br>Murder : 9","<b> Montana <\/b> <br>Urban  : 53 <br>Assault: 109 <br>Murder : 6","<b> Nebraska <\/b> <br>Urban  : 62 <br>Assault: 102 <br>Murder : 4.3","<b> Nevada <\/b> <br>Urban  : 81 <br>Assault: 252 <br>Murder : 12.2","<b> New Hampshire <\/b> <br>Urban  : 56 <br>Assault: 57 <br>Murder : 2.1","<b> New Jersey <\/b> <br>Urban  : 89 <br>Assault: 159 <br>Murder : 7.4","<b> New Mexico <\/b> <br>Urban  : 70 <br>Assault: 285 <br>Murder : 11.4","<b> New York <\/b> <br>Urban  : 86 <br>Assault: 254 <br>Murder : 11.1","<b> North Carolina <\/b> <br>Urban  : 45 <br>Assault: 337 <br>Murder : 13","<b> North Dakota <\/b> <br>Urban  : 44 <br>Assault: 45 <br>Murder : 0.8","<b> Ohio <\/b> <br>Urban  : 75 <br>Assault: 120 <br>Murder : 7.3","<b> Oklahoma <\/b> <br>Urban  : 68 <br>Assault: 151 <br>Murder : 6.6","<b> Oregon <\/b> <br>Urban  : 67 <br>Assault: 159 <br>Murder : 4.9","<b> Pennsylvania <\/b> <br>Urban  : 72 <br>Assault: 106 <br>Murder : 6.3","<b> Rhode Island <\/b> <br>Urban  : 87 <br>Assault: 174 <br>Murder : 3.4","<b> South Carolina <\/b> <br>Urban  : 48 <br>Assault: 279 <br>Murder : 14.4","<b> South Dakota <\/b> <br>Urban  : 45 <br>Assault: 86 <br>Murder : 3.8","<b> Tennessee <\/b> <br>Urban  : 59 <br>Assault: 188 <br>Murder : 13.2","<b> Texas <\/b> <br>Urban  : 80 <br>Assault: 201 <br>Murder : 12.7","<b> Utah <\/b> <br>Urban  : 80 <br>Assault: 120 <br>Murder : 3.2","<b> Vermont <\/b> <br>Urban  : 32 <br>Assault: 48 <br>Murder : 2.2","<b> Virginia <\/b> <br>Urban  : 63 <br>Assault: 156 <br>Murder : 8.5","<b> Washington <\/b> <br>Urban  : 73 <br>Assault: 145 <br>Murder : 4","<b> West Virginia <\/b> <br>Urban  : 39 <br>Assault: 81 <br>Murder : 5.7","<b> Wisconsin <\/b> <br>Urban  : 66 <br>Assault: 53 <br>Murder : 2.6","<b> Wyoming <\/b> <br>Urban  : 60 <br>Assault: 161 <br>Murder : 6.8"],"mode":"markers","hoverinfo":["text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text"],"showlegend":false,"marker":{"colorbar":{"title":"Murder Arrests (per 100,000)","ticklen":2},"cmin":0.80000000000000004,"cmax":17.399999999999999,"colorscale":[["0","rgba(68,1,84,1)"],["0.0416666666666667","rgba(70,19,97,1)"],["0.0833333333333333","rgba(72,32,111,1)"],["0.125","rgba(71,45,122,1)"],["0.166666666666667","rgba(68,58,128,1)"],["0.208333333333333","rgba(64,70,135,1)"],["0.25","rgba(60,82,138,1)"],["0.291666666666667","rgba(56,93,140,1)"],["0.333333333333333","rgba(49,104,142,1)"],["0.375","rgba(46,114,142,1)"],["0.416666666666667","rgba(42,123,142,1)"],["0.458333333333333","rgba(38,133,141,1)"],["0.5","rgba(37,144,140,1)"],["0.541666666666667","rgba(33,154,138,1)"],["0.583333333333333","rgba(39,164,133,1)"],["0.625","rgba(47,174,127,1)"],["0.666666666666667","rgba(53,183,121,1)"],["0.708333333333333","rgba(79,191,110,1)"],["0.75","rgba(98,199,98,1)"],["0.791666666666667","rgba(119,207,85,1)"],["0.833333333333333","rgba(147,214,70,1)"],["0.875","rgba(172,220,52,1)"],["0.916666666666667","rgba(199,225,42,1)"],["0.958333333333333","rgba(226,228,40,1)"],["1","rgba(253,231,37,1)"]],"showscale":true,"color":[13.199999999999999,10,8.0999999999999996,8.8000000000000007,9,7.9000000000000004,3.2999999999999998,5.9000000000000004,15.4,17.399999999999999,5.2999999999999998,2.6000000000000001,10.4,7.2000000000000002,2.2000000000000002,6,9.6999999999999993,15.4,2.1000000000000001,11.300000000000001,4.4000000000000004,12.1,2.7000000000000002,16.100000000000001,9,6,4.2999999999999998,12.199999999999999,2.1000000000000001,7.4000000000000004,11.4,11.1,13,0.80000000000000004,7.2999999999999998,6.5999999999999996,4.9000000000000004,6.2999999999999998,3.3999999999999999,14.4,3.7999999999999998,13.199999999999999,12.699999999999999,3.2000000000000002,2.2000000000000002,8.5,4,5.7000000000000002,2.6000000000000001,6.7999999999999998],"size":[13.199999999999999,10,8.0999999999999996,8.8000000000000007,9,7.9000000000000004,3.2999999999999998,5.9000000000000004,15.4,17.399999999999999,5.2999999999999998,2.6000000000000001,10.4,7.2000000000000002,2.2000000000000002,6,9.6999999999999993,15.4,2.1000000000000001,11.300000000000001,4.4000000000000004,12.1,2.7000000000000002,16.100000000000001,9,6,4.2999999999999998,12.199999999999999,2.1000000000000001,7.4000000000000004,11.4,11.1,13,0.80000000000000004,7.2999999999999998,6.5999999999999996,4.9000000000000004,6.2999999999999998,3.3999999999999999,14.4,3.7999999999999998,13.199999999999999,12.699999999999999,3.2000000000000002,2.2000000000000002,8.5,4,5.7000000000000002,2.6000000000000001,6.7999999999999998],"opacity":0.5,"line":{"colorbar":{"title":"","ticklen":2},"cmin":0.80000000000000004,"cmax":17.399999999999999,"colorscale":[["0","rgba(68,1,84,1)"],["0.0416666666666667","rgba(70,19,97,1)"],["0.0833333333333333","rgba(72,32,111,1)"],["0.125","rgba(71,45,122,1)"],["0.166666666666667","rgba(68,58,128,1)"],["0.208333333333333","rgba(64,70,135,1)"],["0.25","rgba(60,82,138,1)"],["0.291666666666667","rgba(56,93,140,1)"],["0.333333333333333","rgba(49,104,142,1)"],["0.375","rgba(46,114,142,1)"],["0.416666666666667","rgba(42,123,142,1)"],["0.458333333333333","rgba(38,133,141,1)"],["0.5","rgba(37,144,140,1)"],["0.541666666666667","rgba(33,154,138,1)"],["0.583333333333333","rgba(39,164,133,1)"],["0.625","rgba(47,174,127,1)"],["0.666666666666667","rgba(53,183,121,1)"],["0.708333333333333","rgba(79,191,110,1)"],["0.75","rgba(98,199,98,1)"],["0.791666666666667","rgba(119,207,85,1)"],["0.833333333333333","rgba(147,214,70,1)"],["0.875","rgba(172,220,52,1)"],["0.916666666666667","rgba(199,225,42,1)"],["0.958333333333333","rgba(226,228,40,1)"],["1","rgba(253,231,37,1)"]],"showscale":false,"color":[13.199999999999999,10,8.0999999999999996,8.8000000000000007,9,7.9000000000000004,3.2999999999999998,5.9000000000000004,15.4,17.399999999999999,5.2999999999999998,2.6000000000000001,10.4,7.2000000000000002,2.2000000000000002,6,9.6999999999999993,15.4,2.1000000000000001,11.300000000000001,4.4000000000000004,12.1,2.7000000000000002,16.100000000000001,9,6,4.2999999999999998,12.199999999999999,2.1000000000000001,7.4000000000000004,11.4,11.1,13,0.80000000000000004,7.2999999999999998,6.5999999999999996,4.9000000000000004,6.2999999999999998,3.3999999999999999,14.4,3.7999999999999998,13.199999999999999,12.699999999999999,3.2000000000000002,2.2000000000000002,8.5,4,5.7000000000000002,2.6000000000000001,6.7999999999999998]}},"type":"scatter","xaxis":"x","yaxis":"y","frame":null},{"x":[32,91],"y":[45,337],"type":"scatter","mode":"markers","opacity":0,"hoverinfo":"none","showlegend":false,"marker":{"colorbar":{"title":"Murder","ticklen":2},"cmin":0.80000000000000004,"cmax":17.399999999999999,"colorscale":[["0","rgba(68,1,84,1)"],["0.0416666666666667","rgba(70,19,97,1)"],["0.0833333333333333","rgba(72,32,111,1)"],["0.125","rgba(71,45,122,1)"],["0.166666666666667","rgba(68,58,128,1)"],["0.208333333333333","rgba(64,70,135,1)"],["0.25","rgba(60,82,138,1)"],["0.291666666666667","rgba(56,93,140,1)"],["0.333333333333333","rgba(49,104,142,1)"],["0.375","rgba(46,114,142,1)"],["0.416666666666667","rgba(42,123,142,1)"],["0.458333333333333","rgba(38,133,141,1)"],["0.5","rgba(37,144,140,1)"],["0.541666666666667","rgba(33,154,138,1)"],["0.583333333333333","rgba(39,164,133,1)"],["0.625","rgba(47,174,127,1)"],["0.666666666666667","rgba(53,183,121,1)"],["0.708333333333333","rgba(79,191,110,1)"],["0.75","rgba(98,199,98,1)"],["0.791666666666667","rgba(119,207,85,1)"],["0.833333333333333","rgba(147,214,70,1)"],["0.875","rgba(172,220,52,1)"],["0.916666666666667","rgba(199,225,42,1)"],["0.958333333333333","rgba(226,228,40,1)"],["1","rgba(253,231,37,1)"]],"showscale":true,"color":[0.80000000000000004,17.399999999999999],"line":{"color":"rgba(255,127,14,1)"}},"xaxis":"x","yaxis":"y","frame":null}],"highlight":{"on":"plotly_click","persistent":false,"dynamic":false,"selectize":false,"opacityDim":0.20000000000000001,"selected":{"opacity":1},"debounce":0},"shinyEvents":["plotly_hover","plotly_click","plotly_selected","plotly_relayout","plotly_brushed","plotly_brushing","plotly_clickannotation","plotly_doubleclick","plotly_deselect","plotly_afterplot","plotly_sunburstclick"],"base_url":"https://plot.ly"},"evals":[],"jsHooks":[]}</script>
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
<div class="plotly html-widget html-fill-item-overflow-hidden html-fill-item" id="htmlwidget-9018ebb5ac39a098f253" style="width:672px;height:480px;"></div>
<script type="application/json" data-for="htmlwidget-9018ebb5ac39a098f253">{"x":{"visdat":{"66566e6850ff":["function () ","plotlyVisDat"]},"cur_data":"66566e6850ff","attrs":{"66566e6850ff":{"x":[0.041695496811456019,0.042991428447120915,0.036830638001819328,0.041366356726772531,0.057127700260600212,0.051192539727764212,0.046668719823247537,0.041152112584075765,0.040746169786845893,0.044721286967665197,0.042207167665102553,0.04287036484245272,0.052669797276323004,0.04788026105513412,0.041746188197121073,0.034334282114581317,0.038467389092149668,0.040090643173285256,0.049170088752841942,0.044103710194456969,0.050593385546273927,0.046646968384492622,0.047554004613418334,0.044361730191329329,0.042118001869161183,0.046685698053117695,0.039130478702576028,0.049127093897098149,0.039781668036006926,0.038238774223237175,0.039792166155599037,0.047155990289240522,0.042844424427895912,0.045952529333238526,0.041745913234276427,0.040122294517187539,0.040704136268256946,0.038680195192030233,0.041353400542255121,0.042205703614083941,0.043672391175763721,0.039957689898917535,0.045475452337423693,0.050526806042397225,0.045313809622957106,0.051021436829797533,0.045045338240590177,0.043071230243381824,0.04724107500267373,0.036864843788194962,0.044396546685539523,0.036419270644063861,0.041588618471032852,0.044458794725948721,0.056999969136904367,0.040220846399066895,0.040083241549195195,0.042282717888524786,0.040141578418393151,0.048642787804544556,0.042904104048155332,0.044323174109382905,0.038029721018496124,0.054672182956618874,0.040359349262979502,0.046986431305813127,0.042980742850445987,0.04997363786597845,0.05275229471424165,0.056664803394598666,0.045420502327209962,0.046968844533816695,0.039811004262963363,0.049255078059990846,0.043689984873431106,0.042681235577533214,0.047911407426537989,0.036041164728239962,0.03944947087178928,0.049309545698767908,0.043989977799000934,0.049117097616013024,0.045626046535221593,0.046598537905109184,0.041967610968074345,0.039562663376340262,0.051701910710333476,0.043177619512200775,0.040570962590180185,0.046505625405905152,0.038182833053281684,0.040625890853293559,0.04407145085818337,0.041750848817591973,0.038914081097907789,0.049427565701194755,0.050078088320844712,0.044949842143450366,0.042765518144935059,0.052660180624981678,0.051578590149373979,0.049099258616692704,0.041645014516633265,0.047503251524889094,0.051551620232907318,0.05449362775263953,0.049121375458857808,0.041611954713280851,0.043582094973359436,0.03807637592651561,0.042412229245980905,0.043980712900708249,0.044232736574306625,0.042974984725858159,0.046723405882494899,0.045467556602871967,0.036950998521244935,0.04490799736356562,0.039690687379648884,0.038029361552196363,0.054152572632326292,0.04805004033548322,0.053093326354088907,0.042833221232733441,0.058671535404702789,0.046650776999756186,0.049002322372119399,0.05371845396676482,0.038884293621555252,0.050938139285039256,0.044389352280776,0.042481095812558774,0.041532253065329656,0.059594906464713826,0.041217950783379032,0.040990200022644939,0.041486145409862223,0.035316832663426702,0.043938618408098346,0.044322866012371641,0.04217532604249119,0.049747197948974628,0.044359843312890564,0.048950360171311956,0.042523675247828546,0.040910610100407717,0.05089917349876906,0.048230032313835498,0.045987487332390088,0.048628374400239552,0.042480018337978084,0.036236992794688332,0.049363894513252071,0.042643805588181802,0.041646455484624444,0.048406635702531037,0.046486627995477106,0.053463343691139677,0.03738659757131154,0.044240490595360081,0.03696217287556848,0.040500304719117003,0.036699230220550778,0.038137060179276358,0.040663293813244038,0.048006564969861353,0.043476753508356399,0.047562904480044965,0.037625500828581314,0.040780128129064452,0.040645213251201781,0.038455148658774793,0.050813153569259029,0.0413784928992387,0.041202800440491454,0.047812458024678962,0.049918708613639923,0.041214429146783436,0.036667413696727817,0.041785932329833131,0.046765127559534152,0.038663156002348133,0.047727064737509504,0.045899149880055307,0.040163505408114281,0.056910402283218448,0.036405644939151646,0.0380861094948639,0.049598794036110276,0.041483331447895955,0.041880193627144312,0.041082571058371785,0.039797487775085565,0.04000299965349853,0.039724678304337104,0.041072996429153963,0.047834604232009005,0.044247718577352699,0.040175037593301509,0.040249894964139665,0.041665546892569967,0.037284226693049725,0.045229214162626069,0.046017631078740504,0.043855866047801985,0.03775581335717941,0.034644534062899489,0.048032258033120126,0.049823382378191852,0.046425912975904898,0.057206797575910753,0.039597820843377922,0.049414727265002997,0.05099372907863417,0.04932621332192566,0.044863047421403818,0.041122086249698306,0.04296602001077942,0.051190975595461465,0.039066964591964536,0.042054232699055838,0.036265217261234439,0.044037904710491051,0.041797636685056747,0.037211121620848976,0.044303617607792278,0.042754139802299092,0.039175949789051277,0.049066053733806514,0.037505433851330587,0.038994547319690098,0.042611494575449459,0.040922664887302646,0.048455695722748521,0.044914877348255951,0.041780735923660765,0.036102780411476756,0.047322233812257843,0.040007530264185326,0.038159673073556777,0.044844864491849178,0.038643324815555116,0.041753294438360476,0.048655068953726871,0.0441135616438093,0.050014686232534376,0.043377351673518458,0.050048373664571336,0.044862376205163701,0.037432645982175675,0.041833979179321655,0.042486998650513731,0.043643427689792541,0.037575580079842331,0.039600426432789125,0.04520434395127871,0.040424365375697907,0.0439148797675517,0.0357407596137298,0.039763006072909245,0.04266024842243616,0.039597673675087638,0.045878120382729211,0.041169285324154731,0.038980833120502587,0.043189936881445928,0.039765975599556247,0.045459244210686679,0.04839519463585705,0.041722729622105569,0.04519704099807767,0.047135099216818417,0.043140455211506737,0.038435228540090842,0.038500541147582661,0.043765903731868491,0.044480783197550326,0.040960151156406881,0.042869386104610677,0.048798282754878512,0.046350372412818364,0.042804916156914431,0.038273089171036591,0.053883997555534566,0.052708234933516548,0.041087194217541416,0.051537445801483561,0.045225351614754189,0.044343354137856693,0.038983666731892005,0.042515836683484215,0.042812738161312647,0.045702918712862813,0.044018825892148769,0.043379129420772641,0.035418793481078188,0.042198190374147182,0.044490393451918006,0.045552281778591691,0.04296929069235654,0.05191851554710103,0.044872250702726608,0.050776235731371834,0.04200343309309431,0.057467618919488372,0.038308914899738623,0.049228731160574316,0.043163735581699898,0.039730798569782504,0.0444158413521182,0.050899415597819853,0.046541069868608329,0.048932802046286972,0.039249048076844054,0.040189607457801681,0.044760062145475121,0.041749103728097203,0.045368700006754498,0.041464692488126169,0.045971906209448611,0.039009366791895046,0.039883525323545242,0.043654865454529901,0.034327872699175199,0.046895327612831716,0.054714817029254216,0.04844276523336296,0.043658474204564909,0.042417861791852751,0.042463472984139161,0.044874441693375157,0.047142967835027222,0.052283871112450732,0.044887349575842742,0.040288577362944736,0.044772369548994884,0.05437504083035475,0.044758990708968889,0.048003290440077021,0.042161683238815501,0.045963280631681556,0.034395981326438244,0.040915788383716518,0.038976107709138813,0.047952648893506658,0.044720192744942891,0.045098568711134247,0.042827544716931926,0.047171574457592187,0.040949156313125949,0.03208756296729607,0.040555318409090005,0.040253468629131969,0.044804455056378645,0.050387321155206374,0.033376356861904391,0.034231656480574142,0.04627109058032304,0.048210003666392463,0.056370641091303519,0.041979441065205278,0.040624567726358314,0.042706326667670116,0.04802990755295259,0.039447634858230669,0.041959678051817315,0.039451025834659134,0.040816586157344639,0.038237434590893501,0.041459250849117377,0.035400469140466906,0.047780462380164208,0.037468755342465916,0.050557730087222211,0.050864021950302832,0.047611537483323502,0.045592606941317976,0.040346961628708919,0.041271537312439419,0.041912452263273954,0.0373792403309407,0.046487249909467294,0.044376345531502215,0.047734925309832629,0.04196152453234267,0.047433359000379254,0.040100922208039812,0.03731918848805417,0.036699680280162246,0.042550095611671127,0.040446916411711907,0.049658494508139174,0.051422005914395816,0.040115572628286494,0.039891994020528065,0.051988986807815739,0.042870581304278406,0.038220629290606732,0.043313462381787848],"y":[-0.0062769433130810161,-0.040349428028889231,-0.051135691963471779,-0.052746875006987042,-0.098125006846753432,-0.072125655484103365,-0.026852165718946074,-0.022641044079366571,-0.018747202116795376,-0.033017421860588071,-0.054753650792870576,-0.0052484056648222314,-0.11408256347316437,-0.077846440495202368,-0.0281425906073513,-0.036494725976359332,-0.014605999512472583,-0.021060970978517377,-0.050097627857879121,-0.075441098375378282,-0.049524031860801773,-0.044391903926744199,-0.058361239042675483,-0.050801241080187513,-0.072410386540984556,-0.042696902438182201,-0.042523133357830853,-0.075336517843522535,-0.038058316085050066,-0.016820936126807351,-0.051410810945638201,-0.076075222932706008,-0.014034610713710259,-0.056056577485325339,-0.013805278314419234,-0.0017067568930151525,-0.062552945237118102,-0.044525797843772398,-0.0080940273743650322,-0.02161479443499556,-0.0284694494618924,-0.024043621239012315,-0.027940370214298151,-0.064584459811716607,-0.017563791212607763,-0.11632986085268304,-0.059264165248785382,-0.024039890026536826,-0.051280679743219884,-0.010756314198540631,-0.063537918942106211,0.023292611797866444,-0.0074216508724456081,-0.11073090744340529,-0.072366059479171199,0.016902834895891471,-0.046367682001245178,-0.014442251457926441,-0.02918116638356591,-0.08080295745447845,-0.050439295587392297,-0.031328273124680207,0.0045366532712741905,-0.08028724560702491,-0.064788206178079344,-0.046535412441121832,-0.0071703095163352416,-0.060383804358355019,-0.090446191251128794,-0.1298302741982553,-0.077512929770279904,-0.084151771108837189,-0.011932209007720617,-0.092883937802275524,-0.018353692325844845,-0.051209914929087851,-0.072302997080965992,-0.026237509332832885,-0.046254129699859807,-0.043062083587237211,-0.048400776659845955,-0.058186441786442569,-0.079144370794505398,-0.052769709286102098,-0.05693408533200129,-0.081300882757134249,-0.049291856157707779,-0.075691660187929374,-0.034920326513734681,-0.037499087440138218,-0.043904670787047975,-0.016060483371282026,-0.05071665697818941,-0.038504276460241023,-0.025201969290848406,-0.054371141685409359,-0.062881225428327317,-0.0060338631731843657,-0.036622633989213609,-0.058797722172155717,-0.11037361297434926,-0.054671438779831133,-0.020702267790603076,-0.043859675064863698,-0.086903171457631892,-0.060254272218155505,-0.080586725098361719,0.014983819089178519,-0.014300310557012259,-0.054704589830627426,-0.01514802124832808,-0.038936688204571752,-0.048596024339145463,-0.071658598264693327,-0.06570368697079719,-0.028819713574896995,-0.023035591662585536,-0.087342422733960076,-0.043050758288893591,-0.071282873542698508,-0.09743503482262364,-0.098057445282730943,-0.079214600113386019,-0.022957825013315149,-0.063487533957400505,-0.053359361457402478,-0.080993623740640772,-0.057125562610049398,-0.030241037707913612,-0.065794013557202935,-0.0735631291386806,-0.091201297065997639,-0.018548134726842486,-0.039689337251261558,-0.095011582783161241,-0.014992423452831036,-0.012467720726184531,-0.050973901581569871,-0.028090768366906264,-0.064824404780178632,0.0015608438808885044,-0.052201233234048419,-0.021115027288316213,-0.063500136026929055,-0.0075238939865589546,-0.0058945636761283653,-0.037570346532092187,-0.057718893492597886,-0.081999052318134494,-0.049186782728465647,-0.052789167639087989,-0.06312799318738313,-0.0623853194684411,-0.037453580510497929,-0.029580610990079824,-0.11623246515508645,-0.076237139946906132,-0.070731125795655519,-0.043069620945847965,-0.039000888756782447,-0.0022659765431985277,0.0078067740427996031,-0.0084231933749185292,-0.037669246974731355,-0.050753660237652612,-0.04202996874855968,-0.031922492269295187,-0.022089335443727178,-0.024277551227228328,-0.039125982971302757,-0.035797200461141078,-0.044109480134467714,-0.047249356833457594,-0.0080362966936473861,-0.046037030051876406,-0.050277218670384143,-0.062773392341344075,-0.049525255202108792,-0.019764690700705925,-0.036083626829251918,-0.062387978019506574,0.021219169440622857,-0.082570842840681891,-0.013116454493912454,-0.03066620856683798,-0.073961837287759902,-0.047461441777250882,0.012687346518006034,-0.031149722723219989,-0.04196532895476833,-0.032470473071546463,-0.058298696456156214,-0.070544038957651031,-0.035473982194469664,-0.005234561497768543,-0.054493980828122589,-0.088092256700105939,-0.084670270157750055,-0.084682450092761291,-0.033750440559869824,-0.061665255320814301,0.021775792683367039,-0.045316907756612859,-0.050075128121911019,-0.027704878998410499,-0.022971683106963972,-0.001299195896867009,-0.093521283217787604,-0.069296129686756136,-0.016095539080242267,-0.090102290594433337,-0.078804543921699263,-0.054841074976504575,-0.05902312523644767,-0.042454993912189598,-0.018533038732109226,-0.041606537706499427,-0.044645602332831456,-0.070580467701933769,-0.075836584505089122,-0.045848995608924442,-0.00061217531382141781,-0.025078134326778075,-0.071368053196378858,-0.080263298624167007,-0.033448871691169391,-0.02317935617323159,-0.026562070941778853,-0.00077499819265819034,-0.036469102855878809,-0.017249844238659575,-0.039819179250854896,-0.016656595280190055,-0.021948986921968908,-0.023505199497491521,-0.035073914960062111,0.022351284569053505,-0.075081066923817996,-0.040275159815092609,-0.06827534831085412,-0.053816450818962032,-0.049806124850809583,-0.022160769049349376,-0.053910449595866265,-0.066023294391290885,-0.041344121870825999,-0.078933589899862863,-0.074479572281830136,-0.046199892393191638,-0.023517504673924057,-0.037402605337965446,-0.061005110240625826,-0.041230305690524292,-0.032573318216190354,-0.0026464790392490213,-0.048766395062636102,-0.046268356171977519,-0.038285302912220813,-0.072100505578182691,-0.052152484883452706,-0.087669583149915173,-0.033206878757052999,-0.11505474999526681,-0.010654574313446689,-0.043576036848103905,-0.064023981639225278,-0.016346302232590981,-0.065591692406559085,-0.087440770927024888,-0.031232847266340055,0.005378389652159022,-0.083830685739939556,-0.029417717589731003,-0.024718592387294069,-0.042163818946875362,-0.040170584506195477,-0.070999003039061231,-0.018314060385922079,-0.032026620707994384,-0.078244527517425361,-0.012471187784941679,-0.071776887152966165,-0.018300795244027886,-0.040894531819897502,-0.050581718687949799,-0.026058563134145382,-0.055751142948865948,-0.11190543224046921,-0.03262149504934473,-0.024429957925361238,-0.040530335397529392,-0.045478803871755846,-0.054306027731577569,-0.052200110304777773,-0.041508076513607543,-0.047308029782469535,-0.017583323951468798,-0.089361559121001244,0.0086619053803876165,-0.054618730297762236,-0.047293311080623839,-0.096355024697599934,-0.028837416912091397,-0.02926605539981204,-0.067192382501927522,-0.056032517815576291,-0.068089896050342005,-0.040220825145482628,-0.055468490772458981,-0.074937020845775651,-0.054099534382049952,-0.045886983309355388,-0.042958929091544001,0.008291497701644758,-0.035515434037977751,-0.028232969350227476,-0.024053641344934415,-0.037917133395184453,-0.081041692165589319,-0.048883612805482937,-0.025488121772017796,-0.068439300419238486,-0.018442681469482192,-0.05297376726266826,-0.04614296165584527,-0.15920341987424821,-0.072567835089919291,-0.049302965146176804,-0.023058586079882485,-0.038817089888986828,-0.05894251058484358,-0.1028034280606159,-0.068331017038246691,-0.02482536794546986,-0.035306928345870618,-0.043503845840359046,-0.045054157806076467,-0.024314131855818391,-0.028287177433178094,-0.031267478063412638,-0.042841978422324178,-0.013180981816749227,-0.038595327387763584,-0.054035259280179666,-0.065684494562522969,-0.041915789199643172,-0.053248823495599708,-0.0083938285429181227,-0.088200510004350058,-0.016083373391441513,-0.014096380950297383,-0.045324324576528206,-0.040776234193301682,-0.10237785147760491,-0.027684906600435554,-0.058193687119548511,-0.049634606125798238,-0.050200663139789679,-0.030093467529000231,-0.061700017533593041,-0.069583935762580179,-0.038043944609381382,0.044068350415775011,-0.034147220119419668,-0.027654460600752596,-0.079846911481775806,-0.05564648606912255,-0.015537232920554126,-0.026047379039938152,0.035137643747594885,0.0052388922355110935,-0.045272138600712879,0.019229725006775489,-0.054535152349314345,-0.080194383631478752,-0.036410404940785415,-0.031471214379422872,-0.0092745176254972229,-0.038733198489199705,0.0059656995705880721,-0.049600579077074582,-0.01321754389499292,-0.09433098356075835,-0.025826808003635043,-0.10791337383011318,-0.039865304153929131,-0.037883904841860751,-0.074813424798353165,-0.066726824252205788,-0.047108752496950748,-0.071464531045596191,-0.03533651500557649,-0.047503967368351115,-0.038287129528267121,-0.052443432541230753,-0.052544757879863666,-0.068010534716447343,-0.039641316094430404,-0.064076048816131465],"alpha_stroke":1,"sizes":[10,100],"spans":[1,20],"type":"histogram2d","nbinsx":20,"nbinsy":20,"inherit":true}},"layout":{"margin":{"b":40,"l":60,"t":25,"r":10},"xaxis":{"domain":[0,1],"automargin":true,"title":[]},"yaxis":{"domain":[0,1],"automargin":true,"title":[]},"hovermode":"closest","showlegend":false,"legend":{"yanchor":"top","y":0.5}},"source":"A","config":{"modeBarButtonsToAdd":["hoverclosest","hovercompare"],"showSendToCloud":false},"data":[{"colorbar":{"title":"","ticklen":2,"len":0.5,"lenmode":"fraction","y":1,"yanchor":"top"},"colorscale":[["0","rgba(68,1,84,1)"],["0.0416666666666667","rgba(70,19,97,1)"],["0.0833333333333333","rgba(72,32,111,1)"],["0.125","rgba(71,45,122,1)"],["0.166666666666667","rgba(68,58,128,1)"],["0.208333333333333","rgba(64,70,135,1)"],["0.25","rgba(60,82,138,1)"],["0.291666666666667","rgba(56,93,140,1)"],["0.333333333333333","rgba(49,104,142,1)"],["0.375","rgba(46,114,142,1)"],["0.416666666666667","rgba(42,123,142,1)"],["0.458333333333333","rgba(38,133,141,1)"],["0.5","rgba(37,144,140,1)"],["0.541666666666667","rgba(33,154,138,1)"],["0.583333333333333","rgba(39,164,133,1)"],["0.625","rgba(47,174,127,1)"],["0.666666666666667","rgba(53,183,121,1)"],["0.708333333333333","rgba(79,191,110,1)"],["0.75","rgba(98,199,98,1)"],["0.791666666666667","rgba(119,207,85,1)"],["0.833333333333333","rgba(147,214,70,1)"],["0.875","rgba(172,220,52,1)"],["0.916666666666667","rgba(199,225,42,1)"],["0.958333333333333","rgba(226,228,40,1)"],["1","rgba(253,231,37,1)"]],"showscale":true,"x":[0.041695496811456019,0.042991428447120915,0.036830638001819328,0.041366356726772531,0.057127700260600212,0.051192539727764212,0.046668719823247537,0.041152112584075765,0.040746169786845893,0.044721286967665197,0.042207167665102553,0.04287036484245272,0.052669797276323004,0.04788026105513412,0.041746188197121073,0.034334282114581317,0.038467389092149668,0.040090643173285256,0.049170088752841942,0.044103710194456969,0.050593385546273927,0.046646968384492622,0.047554004613418334,0.044361730191329329,0.042118001869161183,0.046685698053117695,0.039130478702576028,0.049127093897098149,0.039781668036006926,0.038238774223237175,0.039792166155599037,0.047155990289240522,0.042844424427895912,0.045952529333238526,0.041745913234276427,0.040122294517187539,0.040704136268256946,0.038680195192030233,0.041353400542255121,0.042205703614083941,0.043672391175763721,0.039957689898917535,0.045475452337423693,0.050526806042397225,0.045313809622957106,0.051021436829797533,0.045045338240590177,0.043071230243381824,0.04724107500267373,0.036864843788194962,0.044396546685539523,0.036419270644063861,0.041588618471032852,0.044458794725948721,0.056999969136904367,0.040220846399066895,0.040083241549195195,0.042282717888524786,0.040141578418393151,0.048642787804544556,0.042904104048155332,0.044323174109382905,0.038029721018496124,0.054672182956618874,0.040359349262979502,0.046986431305813127,0.042980742850445987,0.04997363786597845,0.05275229471424165,0.056664803394598666,0.045420502327209962,0.046968844533816695,0.039811004262963363,0.049255078059990846,0.043689984873431106,0.042681235577533214,0.047911407426537989,0.036041164728239962,0.03944947087178928,0.049309545698767908,0.043989977799000934,0.049117097616013024,0.045626046535221593,0.046598537905109184,0.041967610968074345,0.039562663376340262,0.051701910710333476,0.043177619512200775,0.040570962590180185,0.046505625405905152,0.038182833053281684,0.040625890853293559,0.04407145085818337,0.041750848817591973,0.038914081097907789,0.049427565701194755,0.050078088320844712,0.044949842143450366,0.042765518144935059,0.052660180624981678,0.051578590149373979,0.049099258616692704,0.041645014516633265,0.047503251524889094,0.051551620232907318,0.05449362775263953,0.049121375458857808,0.041611954713280851,0.043582094973359436,0.03807637592651561,0.042412229245980905,0.043980712900708249,0.044232736574306625,0.042974984725858159,0.046723405882494899,0.045467556602871967,0.036950998521244935,0.04490799736356562,0.039690687379648884,0.038029361552196363,0.054152572632326292,0.04805004033548322,0.053093326354088907,0.042833221232733441,0.058671535404702789,0.046650776999756186,0.049002322372119399,0.05371845396676482,0.038884293621555252,0.050938139285039256,0.044389352280776,0.042481095812558774,0.041532253065329656,0.059594906464713826,0.041217950783379032,0.040990200022644939,0.041486145409862223,0.035316832663426702,0.043938618408098346,0.044322866012371641,0.04217532604249119,0.049747197948974628,0.044359843312890564,0.048950360171311956,0.042523675247828546,0.040910610100407717,0.05089917349876906,0.048230032313835498,0.045987487332390088,0.048628374400239552,0.042480018337978084,0.036236992794688332,0.049363894513252071,0.042643805588181802,0.041646455484624444,0.048406635702531037,0.046486627995477106,0.053463343691139677,0.03738659757131154,0.044240490595360081,0.03696217287556848,0.040500304719117003,0.036699230220550778,0.038137060179276358,0.040663293813244038,0.048006564969861353,0.043476753508356399,0.047562904480044965,0.037625500828581314,0.040780128129064452,0.040645213251201781,0.038455148658774793,0.050813153569259029,0.0413784928992387,0.041202800440491454,0.047812458024678962,0.049918708613639923,0.041214429146783436,0.036667413696727817,0.041785932329833131,0.046765127559534152,0.038663156002348133,0.047727064737509504,0.045899149880055307,0.040163505408114281,0.056910402283218448,0.036405644939151646,0.0380861094948639,0.049598794036110276,0.041483331447895955,0.041880193627144312,0.041082571058371785,0.039797487775085565,0.04000299965349853,0.039724678304337104,0.041072996429153963,0.047834604232009005,0.044247718577352699,0.040175037593301509,0.040249894964139665,0.041665546892569967,0.037284226693049725,0.045229214162626069,0.046017631078740504,0.043855866047801985,0.03775581335717941,0.034644534062899489,0.048032258033120126,0.049823382378191852,0.046425912975904898,0.057206797575910753,0.039597820843377922,0.049414727265002997,0.05099372907863417,0.04932621332192566,0.044863047421403818,0.041122086249698306,0.04296602001077942,0.051190975595461465,0.039066964591964536,0.042054232699055838,0.036265217261234439,0.044037904710491051,0.041797636685056747,0.037211121620848976,0.044303617607792278,0.042754139802299092,0.039175949789051277,0.049066053733806514,0.037505433851330587,0.038994547319690098,0.042611494575449459,0.040922664887302646,0.048455695722748521,0.044914877348255951,0.041780735923660765,0.036102780411476756,0.047322233812257843,0.040007530264185326,0.038159673073556777,0.044844864491849178,0.038643324815555116,0.041753294438360476,0.048655068953726871,0.0441135616438093,0.050014686232534376,0.043377351673518458,0.050048373664571336,0.044862376205163701,0.037432645982175675,0.041833979179321655,0.042486998650513731,0.043643427689792541,0.037575580079842331,0.039600426432789125,0.04520434395127871,0.040424365375697907,0.0439148797675517,0.0357407596137298,0.039763006072909245,0.04266024842243616,0.039597673675087638,0.045878120382729211,0.041169285324154731,0.038980833120502587,0.043189936881445928,0.039765975599556247,0.045459244210686679,0.04839519463585705,0.041722729622105569,0.04519704099807767,0.047135099216818417,0.043140455211506737,0.038435228540090842,0.038500541147582661,0.043765903731868491,0.044480783197550326,0.040960151156406881,0.042869386104610677,0.048798282754878512,0.046350372412818364,0.042804916156914431,0.038273089171036591,0.053883997555534566,0.052708234933516548,0.041087194217541416,0.051537445801483561,0.045225351614754189,0.044343354137856693,0.038983666731892005,0.042515836683484215,0.042812738161312647,0.045702918712862813,0.044018825892148769,0.043379129420772641,0.035418793481078188,0.042198190374147182,0.044490393451918006,0.045552281778591691,0.04296929069235654,0.05191851554710103,0.044872250702726608,0.050776235731371834,0.04200343309309431,0.057467618919488372,0.038308914899738623,0.049228731160574316,0.043163735581699898,0.039730798569782504,0.0444158413521182,0.050899415597819853,0.046541069868608329,0.048932802046286972,0.039249048076844054,0.040189607457801681,0.044760062145475121,0.041749103728097203,0.045368700006754498,0.041464692488126169,0.045971906209448611,0.039009366791895046,0.039883525323545242,0.043654865454529901,0.034327872699175199,0.046895327612831716,0.054714817029254216,0.04844276523336296,0.043658474204564909,0.042417861791852751,0.042463472984139161,0.044874441693375157,0.047142967835027222,0.052283871112450732,0.044887349575842742,0.040288577362944736,0.044772369548994884,0.05437504083035475,0.044758990708968889,0.048003290440077021,0.042161683238815501,0.045963280631681556,0.034395981326438244,0.040915788383716518,0.038976107709138813,0.047952648893506658,0.044720192744942891,0.045098568711134247,0.042827544716931926,0.047171574457592187,0.040949156313125949,0.03208756296729607,0.040555318409090005,0.040253468629131969,0.044804455056378645,0.050387321155206374,0.033376356861904391,0.034231656480574142,0.04627109058032304,0.048210003666392463,0.056370641091303519,0.041979441065205278,0.040624567726358314,0.042706326667670116,0.04802990755295259,0.039447634858230669,0.041959678051817315,0.039451025834659134,0.040816586157344639,0.038237434590893501,0.041459250849117377,0.035400469140466906,0.047780462380164208,0.037468755342465916,0.050557730087222211,0.050864021950302832,0.047611537483323502,0.045592606941317976,0.040346961628708919,0.041271537312439419,0.041912452263273954,0.0373792403309407,0.046487249909467294,0.044376345531502215,0.047734925309832629,0.04196152453234267,0.047433359000379254,0.040100922208039812,0.03731918848805417,0.036699680280162246,0.042550095611671127,0.040446916411711907,0.049658494508139174,0.051422005914395816,0.040115572628286494,0.039891994020528065,0.051988986807815739,0.042870581304278406,0.038220629290606732,0.043313462381787848],"y":[-0.0062769433130810161,-0.040349428028889231,-0.051135691963471779,-0.052746875006987042,-0.098125006846753432,-0.072125655484103365,-0.026852165718946074,-0.022641044079366571,-0.018747202116795376,-0.033017421860588071,-0.054753650792870576,-0.0052484056648222314,-0.11408256347316437,-0.077846440495202368,-0.0281425906073513,-0.036494725976359332,-0.014605999512472583,-0.021060970978517377,-0.050097627857879121,-0.075441098375378282,-0.049524031860801773,-0.044391903926744199,-0.058361239042675483,-0.050801241080187513,-0.072410386540984556,-0.042696902438182201,-0.042523133357830853,-0.075336517843522535,-0.038058316085050066,-0.016820936126807351,-0.051410810945638201,-0.076075222932706008,-0.014034610713710259,-0.056056577485325339,-0.013805278314419234,-0.0017067568930151525,-0.062552945237118102,-0.044525797843772398,-0.0080940273743650322,-0.02161479443499556,-0.0284694494618924,-0.024043621239012315,-0.027940370214298151,-0.064584459811716607,-0.017563791212607763,-0.11632986085268304,-0.059264165248785382,-0.024039890026536826,-0.051280679743219884,-0.010756314198540631,-0.063537918942106211,0.023292611797866444,-0.0074216508724456081,-0.11073090744340529,-0.072366059479171199,0.016902834895891471,-0.046367682001245178,-0.014442251457926441,-0.02918116638356591,-0.08080295745447845,-0.050439295587392297,-0.031328273124680207,0.0045366532712741905,-0.08028724560702491,-0.064788206178079344,-0.046535412441121832,-0.0071703095163352416,-0.060383804358355019,-0.090446191251128794,-0.1298302741982553,-0.077512929770279904,-0.084151771108837189,-0.011932209007720617,-0.092883937802275524,-0.018353692325844845,-0.051209914929087851,-0.072302997080965992,-0.026237509332832885,-0.046254129699859807,-0.043062083587237211,-0.048400776659845955,-0.058186441786442569,-0.079144370794505398,-0.052769709286102098,-0.05693408533200129,-0.081300882757134249,-0.049291856157707779,-0.075691660187929374,-0.034920326513734681,-0.037499087440138218,-0.043904670787047975,-0.016060483371282026,-0.05071665697818941,-0.038504276460241023,-0.025201969290848406,-0.054371141685409359,-0.062881225428327317,-0.0060338631731843657,-0.036622633989213609,-0.058797722172155717,-0.11037361297434926,-0.054671438779831133,-0.020702267790603076,-0.043859675064863698,-0.086903171457631892,-0.060254272218155505,-0.080586725098361719,0.014983819089178519,-0.014300310557012259,-0.054704589830627426,-0.01514802124832808,-0.038936688204571752,-0.048596024339145463,-0.071658598264693327,-0.06570368697079719,-0.028819713574896995,-0.023035591662585536,-0.087342422733960076,-0.043050758288893591,-0.071282873542698508,-0.09743503482262364,-0.098057445282730943,-0.079214600113386019,-0.022957825013315149,-0.063487533957400505,-0.053359361457402478,-0.080993623740640772,-0.057125562610049398,-0.030241037707913612,-0.065794013557202935,-0.0735631291386806,-0.091201297065997639,-0.018548134726842486,-0.039689337251261558,-0.095011582783161241,-0.014992423452831036,-0.012467720726184531,-0.050973901581569871,-0.028090768366906264,-0.064824404780178632,0.0015608438808885044,-0.052201233234048419,-0.021115027288316213,-0.063500136026929055,-0.0075238939865589546,-0.0058945636761283653,-0.037570346532092187,-0.057718893492597886,-0.081999052318134494,-0.049186782728465647,-0.052789167639087989,-0.06312799318738313,-0.0623853194684411,-0.037453580510497929,-0.029580610990079824,-0.11623246515508645,-0.076237139946906132,-0.070731125795655519,-0.043069620945847965,-0.039000888756782447,-0.0022659765431985277,0.0078067740427996031,-0.0084231933749185292,-0.037669246974731355,-0.050753660237652612,-0.04202996874855968,-0.031922492269295187,-0.022089335443727178,-0.024277551227228328,-0.039125982971302757,-0.035797200461141078,-0.044109480134467714,-0.047249356833457594,-0.0080362966936473861,-0.046037030051876406,-0.050277218670384143,-0.062773392341344075,-0.049525255202108792,-0.019764690700705925,-0.036083626829251918,-0.062387978019506574,0.021219169440622857,-0.082570842840681891,-0.013116454493912454,-0.03066620856683798,-0.073961837287759902,-0.047461441777250882,0.012687346518006034,-0.031149722723219989,-0.04196532895476833,-0.032470473071546463,-0.058298696456156214,-0.070544038957651031,-0.035473982194469664,-0.005234561497768543,-0.054493980828122589,-0.088092256700105939,-0.084670270157750055,-0.084682450092761291,-0.033750440559869824,-0.061665255320814301,0.021775792683367039,-0.045316907756612859,-0.050075128121911019,-0.027704878998410499,-0.022971683106963972,-0.001299195896867009,-0.093521283217787604,-0.069296129686756136,-0.016095539080242267,-0.090102290594433337,-0.078804543921699263,-0.054841074976504575,-0.05902312523644767,-0.042454993912189598,-0.018533038732109226,-0.041606537706499427,-0.044645602332831456,-0.070580467701933769,-0.075836584505089122,-0.045848995608924442,-0.00061217531382141781,-0.025078134326778075,-0.071368053196378858,-0.080263298624167007,-0.033448871691169391,-0.02317935617323159,-0.026562070941778853,-0.00077499819265819034,-0.036469102855878809,-0.017249844238659575,-0.039819179250854896,-0.016656595280190055,-0.021948986921968908,-0.023505199497491521,-0.035073914960062111,0.022351284569053505,-0.075081066923817996,-0.040275159815092609,-0.06827534831085412,-0.053816450818962032,-0.049806124850809583,-0.022160769049349376,-0.053910449595866265,-0.066023294391290885,-0.041344121870825999,-0.078933589899862863,-0.074479572281830136,-0.046199892393191638,-0.023517504673924057,-0.037402605337965446,-0.061005110240625826,-0.041230305690524292,-0.032573318216190354,-0.0026464790392490213,-0.048766395062636102,-0.046268356171977519,-0.038285302912220813,-0.072100505578182691,-0.052152484883452706,-0.087669583149915173,-0.033206878757052999,-0.11505474999526681,-0.010654574313446689,-0.043576036848103905,-0.064023981639225278,-0.016346302232590981,-0.065591692406559085,-0.087440770927024888,-0.031232847266340055,0.005378389652159022,-0.083830685739939556,-0.029417717589731003,-0.024718592387294069,-0.042163818946875362,-0.040170584506195477,-0.070999003039061231,-0.018314060385922079,-0.032026620707994384,-0.078244527517425361,-0.012471187784941679,-0.071776887152966165,-0.018300795244027886,-0.040894531819897502,-0.050581718687949799,-0.026058563134145382,-0.055751142948865948,-0.11190543224046921,-0.03262149504934473,-0.024429957925361238,-0.040530335397529392,-0.045478803871755846,-0.054306027731577569,-0.052200110304777773,-0.041508076513607543,-0.047308029782469535,-0.017583323951468798,-0.089361559121001244,0.0086619053803876165,-0.054618730297762236,-0.047293311080623839,-0.096355024697599934,-0.028837416912091397,-0.02926605539981204,-0.067192382501927522,-0.056032517815576291,-0.068089896050342005,-0.040220825145482628,-0.055468490772458981,-0.074937020845775651,-0.054099534382049952,-0.045886983309355388,-0.042958929091544001,0.008291497701644758,-0.035515434037977751,-0.028232969350227476,-0.024053641344934415,-0.037917133395184453,-0.081041692165589319,-0.048883612805482937,-0.025488121772017796,-0.068439300419238486,-0.018442681469482192,-0.05297376726266826,-0.04614296165584527,-0.15920341987424821,-0.072567835089919291,-0.049302965146176804,-0.023058586079882485,-0.038817089888986828,-0.05894251058484358,-0.1028034280606159,-0.068331017038246691,-0.02482536794546986,-0.035306928345870618,-0.043503845840359046,-0.045054157806076467,-0.024314131855818391,-0.028287177433178094,-0.031267478063412638,-0.042841978422324178,-0.013180981816749227,-0.038595327387763584,-0.054035259280179666,-0.065684494562522969,-0.041915789199643172,-0.053248823495599708,-0.0083938285429181227,-0.088200510004350058,-0.016083373391441513,-0.014096380950297383,-0.045324324576528206,-0.040776234193301682,-0.10237785147760491,-0.027684906600435554,-0.058193687119548511,-0.049634606125798238,-0.050200663139789679,-0.030093467529000231,-0.061700017533593041,-0.069583935762580179,-0.038043944609381382,0.044068350415775011,-0.034147220119419668,-0.027654460600752596,-0.079846911481775806,-0.05564648606912255,-0.015537232920554126,-0.026047379039938152,0.035137643747594885,0.0052388922355110935,-0.045272138600712879,0.019229725006775489,-0.054535152349314345,-0.080194383631478752,-0.036410404940785415,-0.031471214379422872,-0.0092745176254972229,-0.038733198489199705,0.0059656995705880721,-0.049600579077074582,-0.01321754389499292,-0.09433098356075835,-0.025826808003635043,-0.10791337383011318,-0.039865304153929131,-0.037883904841860751,-0.074813424798353165,-0.066726824252205788,-0.047108752496950748,-0.071464531045596191,-0.03533651500557649,-0.047503967368351115,-0.038287129528267121,-0.052443432541230753,-0.052544757879863666,-0.068010534716447343,-0.039641316094430404,-0.064076048816131465],"type":"histogram2d","nbinsx":20,"nbinsy":20,"marker":{"line":{"color":"rgba(31,119,180,1)"}},"xaxis":"x","yaxis":"y","frame":null}],"highlight":{"on":"plotly_click","persistent":false,"dynamic":false,"selectize":false,"opacityDim":0.20000000000000001,"selected":{"opacity":1},"debounce":0},"shinyEvents":["plotly_hover","plotly_click","plotly_selected","plotly_relayout","plotly_brushed","plotly_brushing","plotly_clickannotation","plotly_doubleclick","plotly_deselect","plotly_afterplot","plotly_sunburstclick"],"base_url":"https://plot.ly"},"evals":[],"jsHooks":[]}</script>
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
##  11.1560459   1.2913759  -0.2972869
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
## -32.718  -6.118  -0.932   6.279  50.014 
## 
## Coefficients:
##               Estimate Std. Error t value Pr(>|t|)    
## (Intercept)  20.951357   1.269468  16.504  < 2e-16 ***
## x             0.846534   0.210726   4.017 6.33e-05 ***
## fo.L         22.470988   1.129778  19.890  < 2e-16 ***
## fo.Q          8.201696   0.992588   8.263 4.51e-16 ***
## fo.C          0.118699   0.773430   0.153    0.878    
## fo^4         -0.003264   0.586849  -0.006    0.996    
## fuB         -24.435367   0.615260 -39.716  < 2e-16 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 9.687 on 993 degrees of freedom
## Multiple R-squared:  0.6814,	Adjusted R-squared:  0.6794 
## F-statistic: 353.9 on 6 and 993 DF,  p-value: < 2.2e-16
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
## x 0.846534   0.382845 2.21116 0.091507 .  
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## RMSE: 9.65331     Adj. R2: 0.67943 
##                 Within R2: 0.015992
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
## x  1.13255   0.512179 2.21124 0.054335 .  
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## RMSE: 3.53169     Adj. R2: 0.956919
##                 Within R2: 0.177645
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
## -9.9123 -1.4925  0.0287  1.4580 12.5826 
## 
## Coefficients:
##             Estimate Std. Error t value Pr(>|t|)    
## (Intercept)  13.4107     0.6420  20.889  < 2e-16 ***
## x             2.8274     0.1158  24.410  < 2e-16 ***
## fo.L         23.9468     1.8537  12.918  < 2e-16 ***
## fo.Q          8.7687     1.6106   5.444 6.57e-08 ***
## fo.C          0.9625     1.2131   0.793  0.42771    
## fo^4         -0.6306     0.8611  -0.732  0.46415    
## fuB         -13.0088     0.8625 -15.082  < 2e-16 ***
## x:fo.L        5.3645     0.3371  15.914  < 2e-16 ***
## x:fo.Q        2.0703     0.2926   7.076 2.82e-12 ***
## x:fo.C        0.5996     0.2152   2.786  0.00544 ** 
## x:fo^4        0.2486     0.1510   1.646  0.10002    
## x:fuB        -2.9502     0.1536 -19.206  < 2e-16 ***
## fo.L:fuB    -23.9449     2.4499  -9.774  < 2e-16 ***
## fo.Q:fuB     -8.7832     2.1449  -4.095 4.57e-05 ***
## fo.C:fuB     -0.8791     1.6578  -0.530  0.59602    
## fo^4:fuB     -0.4161     1.2360  -0.337  0.73643    
## x:fo.L:fuB   -5.5354     0.4379 -12.642  < 2e-16 ***
## x:fo.Q:fuB   -2.1918     0.3830  -5.723 1.39e-08 ***
## x:fo.C:fuB   -0.6876     0.2935  -2.342  0.01936 *  
## x:fo^4:fuB   -0.1209     0.2176  -0.556  0.57865    
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 2.576 on 980 degrees of freedom
## Multiple R-squared:  0.9778,	Adjusted R-squared:  0.9773 
## F-statistic:  2267 on 19 and 980 DF,  p-value: < 2.2e-16
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
## 20 
## 20
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
##       StudRes        Hat        CookD
## 1  -2.5048936 0.82384364 12.883879330
## 4  -2.9361508 0.02665791  0.098334593
## 24 -2.5914729 0.02502822  0.074928507
## 36  0.4589864 0.04036630  0.004524797
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
##         dfb.1_       dfb.x       dffit     cov.r       cook.d        hat
## 1  4.085520801 -5.33422102 -5.41704586 4.3772859 1.288388e+01 0.82384364
## 2  0.025109927 -0.01009170  0.03350458 1.0822810 5.758302e-04 0.02749439
## 3  0.002750354  0.02631325  0.05571417 1.0843738 1.589969e-03 0.03217743
## 4 -0.346302280  0.12117874 -0.48591317 0.7128078 9.833459e-02 0.02665791
## 5 -0.159455918  0.09600708 -0.17791167 1.0439234 1.588239e-02 0.03527109
## 6 -0.049170678  0.03099982 -0.05371612 1.0914861 1.478742e-03 0.03748405
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
## W = 0.94704, p-value = 0.05999
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
## BP = 0.061378, df = 1, p-value = 0.8043
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
## -0.42284 -0.10994 -0.01107  0.11088  0.46110 
## 
## Coefficients:
##             Estimate Std. Error t value Pr(>|t|)
## (Intercept)  0.37361    0.43538   0.858    0.392
## P            0.05915    0.04893   1.209    0.228
## 
## Residual standard error: 0.17 on 298 degrees of freedom
## Multiple R-squared:  0.004879,	Adjusted R-squared:  0.00154 
## F-statistic: 1.461 on 1 and 298 DF,  p-value: 0.2277
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
## -0.65659 -0.15165 -0.01287  0.16192  0.75008 
## 
## Coefficients:
##             Estimate Std. Error t value Pr(>|t|)    
## (Intercept)  6.41768    0.16868   38.05   <2e-16 ***
## P           -0.61315    0.01988  -30.84   <2e-16 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 0.2266 on 598 degrees of freedom
## Multiple R-squared:  0.614,	Adjusted R-squared:  0.6133 
## F-statistic: 951.1 on 1 and 598 DF,  p-value: < 2.2e-16
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
## (Intercept)  7.694259   0.193788  39.7045 < 2.2e-16 ***
## fit_P       -0.763845   0.022847 -33.4323 < 2.2e-16 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## RMSE: 0.236848   Adj. R2: 0.576168
## F-test (1st stage), P: stat = 2,919.7, p < 2.2e-16, on 1 and 598 DoF.
##            Wu-Hausman: stat =   527.4, p < 2.2e-16, on 1 and 597 DoF.
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
## -0.59401 -0.12242  0.00072  0.12890  0.58382 
## 
## Coefficients:
##               Estimate Std. Error t value Pr(>|t|)    
## (Intercept)  8.884e+00  2.227e-02 399.005   <2e-16 ***
## T            7.235e-05  1.282e-04   0.564    0.573    
## cost2       -8.810e-01  6.290e-02 -14.007   <2e-16 ***
## T:cost2      2.546e-05  1.813e-04   0.140    0.888    
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 0.1923 on 596 degrees of freedom
## Multiple R-squared:  0.8303,	Adjusted R-squared:  0.8294 
## F-statistic: 971.7 on 3 and 596 DF,  p-value: < 2.2e-16
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
## -0.50134 -0.11077 -0.00193  0.10843  0.50361 
## 
## Coefficients:
##               Estimate Std. Error t value Pr(>|t|)    
## (Intercept)  8.860e-01  1.932e-02  45.868   <2e-16 ***
## T            9.142e-05  1.112e-04   0.822    0.412    
## cost2        7.064e-01  5.457e-02  12.946   <2e-16 ***
## T:cost2     -1.914e-04  1.573e-04  -1.216    0.224    
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 0.1669 on 596 degrees of freedom
## Multiple R-squared:  0.7914,	Adjusted R-squared:  0.7903 
## F-statistic: 753.6 on 3 and 596 DF,  p-value: < 2.2e-16
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
## -0.71663 -0.12708  0.00283  0.12344  0.60309 
## 
## Coefficients:
##               Estimate Std. Error t value Pr(>|t|)    
## (Intercept)  8.897e+00  1.153e-02 771.470   <2e-16 ***
## T            2.340e-06  3.839e-05   0.061    0.951    
## cost2       -8.933e-01  5.953e-02 -15.005   <2e-16 ***
## T:cost2      9.548e-05  1.330e-04   0.718    0.473    
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 0.191 on 1196 degrees of freedom
## Multiple R-squared:  0.7884,	Adjusted R-squared:  0.7879 
## F-statistic:  1485 on 3 and 1196 DF,  p-value: < 2.2e-16
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
## -0.54677 -0.11268  0.00178  0.11578  0.60742 
## 
## Coefficients:
##               Estimate Std. Error t value Pr(>|t|)    
## (Intercept)  9.071e-01  1.040e-02  87.244   <2e-16 ***
## T           -6.609e-05  3.461e-05  -1.910   0.0564 .  
## cost2        6.854e-01  5.367e-02  12.769   <2e-16 ***
## T:cost2     -3.387e-05  1.199e-04  -0.283   0.7776    
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 0.1722 on 1196 degrees of freedom
## Multiple R-squared:  0.7328,	Adjusted R-squared:  0.7321 
## F-statistic:  1093 on 3 and 1196 DF,  p-value: < 2.2e-16
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



