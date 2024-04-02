
# (PART) Linear Regression in R {-} 

This section is a quick overview of linear regression models from the perspective that ``all models are wrong, but some are useful''. All models are estimated via  Ordinary Least Squares (OLS). For more in-depth introductions, which typically begin by assuming the true data generating process is linear, see https://jadamso.github.io/Rbooks/ordinary-least-squares.html#more-literature. 


# Simple OLS
***
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


Before fitting the model to your data, explore your data (as in Part I)

```r
## Inspect Dataset
xy <- USArrests[,c('Murder','UrbanPop')]
colnames(xy) <- c('y','x')
## head(xy)
## Plot Data
plot(y~x, xy, col=grey(.5,.5), pch=16)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-1-1.png" width="672" />



```r
## Estimate Regression Coefficients
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


To measure the ''Goodness of fit'', we analyze sums of squared errors (Total, Explained, and Residual) as
$$
\underbrace{\sum_{i}(y_i-\bar{y})^2}_\text{TSS}=\underbrace{\sum_{i}(\hat{y}_i-\bar{y})^2}_\text{ESS}+\underbrace{\sum_{i}\hat{\epsilon_{i}}^2}_\text{RSS}\\
R^2 = \frac{ESS}{TSS}=1-\frac{RSS}{TSS}
$$
Note that $R^2$ is also called the coefficient of determination.


```r
## Manually Compute Goodness of Fit
Ehat <- resid(reg)
RSS  <- sum(Ehat^2)
Y <- xy$y
TSS  <- sum((Y-mean(Y))^2)
R2 <- 1 - RSS/TSS
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




## Variability Estimates

A regression coefficient is a statistic. And, just like all statistics, we can calculate 

* *standard deviation*: variability within a single sample.
* *standard error*: variability across different samples.
* *confidence interval:* range your statistic varies across different samples.
* *null distribution*: the sampling distribution of the statistic under the null hypothesis (assuming your null hypothesis was true).
* *p-value* the probability you would see something as extreme as your statistic when sampling from the null distribution.

To calculate these variability statistics, we will estimate variabilty using *data-driven* methods.^[For some technical background, see, e.g., https://www.sagepub.com/sites/default/files/upm-binaries/21122_Chapter_21.pdf. Also note that we can compute  classic estimates for variability: denoting the Standard Error of the Regression as $\hat{\sigma}$, and the Standard Error of the Coefficient Estimates as $\hat{\sigma}_{\hat{\alpha}}$ and $\hat{\sigma}_{\hat{\beta}}~~$ (or simply Standard Errors).
$$
\hat{\sigma}^2 = \frac{1}{n-2}\sum_{i}\hat{\epsilon_{i}}^2\\
\hat{\sigma}^2_{\hat{\alpha}}=\hat{\sigma}^2\left[\frac{1}{n}+\frac{\bar{x}^2}{\sum_{i}(x_i-\bar{x})^2}\right]\\
\hat{\sigma}^2_{\hat{\beta}}=\frac{\hat{\sigma}^2}{\sum_{i}(x_i-\bar{x})^2}.
$$
These equations are motivated by particular data generating proceses, which you can read more about this at https://www.econometrics-with-r.org/4-lrwor.html.]

We first consider the simplest, the jackknife. In this procedure, we loop through each row of the dataset. And, in each iteration of the loop, we drop that observation from the dataset and reestimate the statistic of interest. We then calculate the standard deviation of the statistic across all ``resamples''.


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

<img src="03-ROLS_files/figure-html/unnamed-chunk-4-1.png" width="672" />

```r
## Plot Full-Sample Estimate
## abline(v=coef(reg)['x'], lty=1, col='blue', lwd=2)

## Plot Normal Approximation
## jack_ci_normal <- jack_mean+c(-1.96, +1.96)*jack_se
## abline(v=jack_ci_normal, col="red", lty=3)
```

There are several other resampling techniques. We consider the other main one, the bootstrap, which resamples with *replacement* for an *arbitrary* number of iterations. When bootstrapping a dataset with $n$ observations, you randomly resample all $n$ rows in your data set $B$ times. 

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

<img src="03-ROLS_files/figure-html/unnamed-chunk-5-1.png" width="672" />

```r
## Normal Approximation
## boot_ci_normal <- boot_mean+c(-1.96, +1.96)*boot

## Parametric CI
## x <- data.frame(x=quantile(xy$x,probs=seq(0,1,by=.1)))
## ci <- predict(reg, interval='confidence', newdata=data.frame(x))
## polygon( c(x, rev(x)), c(ci[,'lwr'], rev(ci[,'upr'])), col=grey(0,.2), border=0)
```

We can also bootstrap other statistics, such as a t-statistic or $R^2$. We do such things to test a null hypothesis, which is often ``no relationship''. We are rarely interested in computing standard errrors and conducting hypothesis tests for two variables. However, we work through the ideas in the two-variable case to better understand the multi-variable case.

## Hypothesis Tests

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
abline(v=boot_ci_percentile, lty=2, col="red")
abline(v=0, col="red", lwd=2)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-6-1.png" width="672" />

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
abline(v=boot_ci_percentile0, col="red", lty=2)
abline(v=coef(reg)['x'], col="red", lwd=2)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-7-1.png" width="672" />

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

<img src="03-ROLS_files/figure-html/unnamed-chunk-8-1.png" width="672" />

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

<img src="03-ROLS_files/figure-html/unnamed-chunk-9-1.png" width="672" />

```r
Phat2  <-  1-That_NullDist2(boot_t)
Phat2
```

```
## [1] 0.6240602
```
Under some assumptions, the null distribution is distributed $t_{n-2}$. (For more on parametric t-testing based on statistical theory, see https://www.econometrics-with-r.org/4-lrwor.html.)


## Prediction Intervals

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

<img src="03-ROLS_files/figure-html/unnamed-chunk-10-1.png" width="672" />

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

<img src="03-ROLS_files/figure-html/unnamed-chunk-11-1.png" width="672" />


For a nice overview of different types of intervals, see https://www.jstor.org/stable/2685212. For an indepth view, see "Statistical Intervals: A Guide for Practitioners and Researchers" or "Statistical Tolerance Regions: Theory, Applications, and Computation". See https://robjhyndman.com/hyndsight/intervals/ for constructing intervals for future observations in a time-series context. See Davison and Hinkley, chapters 5 and 6 (also Efron and Tibshirani, or Wehrens et al.)


## Value of More Data

Just as before, there are diminishing returns to larger sample sizes with simple OLS.


```r
B <- 300
Nseq <- seq(3,100, by=1)
SE <- sapply(Nseq, function(n){
    sample_statistics <- sapply(1:B, function(b){
        x <- rnorm(n)
        e <- rnorm(n)        
        y <- x*2 + e
        reg <- lm(y~x)
        coef(reg)
        #se <- sqrt(diag(vcov(vcov)))
    })
    sd(sample_statistics)
})

par(mfrow=c(1,2))
plot(Nseq, SE, pch=16, col=grey(0,.5), main='Absolute Gain',
    ylab='standard error', xlab='sample size')
plot(Nseq[-1], abs(diff(SE)), pch=16, col=grey(0,.5), main='Marginal Gain', 
    ylab='decrease in standard error', xlab='sample size')
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-12-1.png" width="672" />

## Locally Linear


Segmented/piecewise regression

```r
library(AER)
```

```
## Loading required package: car
```

```
## Loading required package: carData
```

```
## Loading required package: lmtest
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

```
## Loading required package: sandwich
```

```
## Loading required package: survival
```

```r
data(CASchools)
CASchools$score <- (CASchools$read + CASchools$math) / 2
reg <- lm(score ~ income, data = CASchools)
plot( CASchools$income, resid(reg), pch=16, col=grey(0,.5))
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-13-1.png" width="672" />

```r
## Add Piecewise Term
CASchools$IncomeCut <- cut(CASchools$income,2)
reg2 <- lm(score ~ income*IncomeCut, data=CASchools)
summary(reg2)
```

```
## 
## Call:
## lm(formula = score ~ income * IncomeCut, data = CASchools)
## 
## Residuals:
##     Min      1Q  Median      3Q     Max 
## -44.710  -8.897   0.730   8.210  32.445 
## 
## Coefficients:
##                             Estimate Std. Error t value Pr(>|t|)    
## (Intercept)                 617.4010     2.1013 293.821  < 2e-16 ***
## income                        2.4732     0.1426  17.338  < 2e-16 ***
## IncomeCut(30.3,55.4]         59.6336    16.9170   3.525  0.00047 ***
## income:IncomeCut(30.3,55.4]  -2.0904     0.4499  -4.646 4.55e-06 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 12.88 on 416 degrees of freedom
## Multiple R-squared:  0.5462,	Adjusted R-squared:  0.5429 
## F-statistic: 166.9 on 3 and 416 DF,  p-value: < 2.2e-16
```

```r
## F Test for Break
anova(reg, reg2)
```

```
## Analysis of Variance Table
## 
## Model 1: score ~ income
## Model 2: score ~ income * IncomeCut
##   Res.Df   RSS Df Sum of Sq      F    Pr(>F)    
## 1    418 74905                                  
## 2    416 69033  2    5871.7 17.692 4.226e-08 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
```

```r
## Chow Test for Break
data_splits <- split(CASchools, CASchools$IncomeCut)
resids <- sapply(data_splits, function(dat){
    reg <- lm(score ~ income, data=dat)
    sum( resid(reg)^2)
})
Ns <-  sapply(data_splits, function(dat){ nrow(dat)})
Rt <- (sum(resid(reg)^2) - sum(resids))/sum(resids)
Rb <- (sum(Ns)-2*reg$rank)/reg$rank
Ft <- Rt*Rb
pf(Ft,reg$rank, sum(Ns)-2*reg$rank,lower.tail=F)
```

```
## [1] 4.225896e-08
```


Multiple Breaks

```r
CASchools$IncomeCut2 <- cut(CASchools$income, seq(0,60,by=20)) ## Finer Bins
reg3 <- lm(score ~ income*IncomeCut2, data=CASchools)
summary(reg3)
```

```
## 
## Call:
## lm(formula = score ~ income * IncomeCut2, data = CASchools)
## 
## Residuals:
##     Min      1Q  Median      3Q     Max 
## -42.323  -9.048   0.258   8.279  31.702 
## 
## Coefficients:
##                          Estimate Std. Error t value Pr(>|t|)    
## (Intercept)              612.0820     2.7523 222.386  < 2e-16 ***
## income                     2.9200     0.2073  14.089  < 2e-16 ***
## IncomeCut2(20,40]         23.0794     8.7824   2.628 0.008910 ** 
## IncomeCut2(40,60]         89.1941    37.6356   2.370 0.018249 *  
## income:IncomeCut2(20,40]  -1.3601     0.3805  -3.574 0.000393 ***
## income:IncomeCut2(40,60]  -3.0429     0.8525  -3.570 0.000400 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 12.78 on 414 degrees of freedom
## Multiple R-squared:  0.5553,	Adjusted R-squared:  0.5499 
## F-statistic: 103.4 on 5 and 414 DF,  p-value: < 2.2e-16
```

```r
## Make Predictions
income <- seq(min(CASchools$income), max(CASchools$income), length.out=1001)
newdata <- data.frame(income,
    IncomeCut=cut(income,2),
    IncomeCut2=cut(income,seq(0,60,by=20)))
pred1 <- predict(reg, newdata=newdata)
pred2 <- predict(reg2, newdata=newdata)
pred3 <- predict(reg3,newdata=newdata)

## Compare Predictions
plot(score ~ income, pch=16, col=grey(0,.5), dat=CASchools)
lines(income, pred1, lwd=2, col=2)
lines(income, pred2, lwd=2, col=4)
lines(income, pred3, lwd=2, col=3)
legend('topleft',
    legend=c('OLS','Peicewise Linear (2)','Peicewise Linear (3)'),
    lty=1, col=c(2,4,3), cex=.8)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-14-1.png" width="672" />


```r
## To Test for Any Break
## strucchange::sctest(score ~ income, data=CASchools, type="Chow", point=.5)
## strucchange::Fstats(score ~ income, data=CASchools)

## To Find Changes
## segmented::segmented(reg)
```


Smoothing (Linear Regression using subsample around each data point)

```r
plot(score ~ income, pch=16, col=grey(0,.5), dat=CASchools)

## design points
CASchoolsO <- CASchools[order(CASchools$income),]

## Loess (adaptive subsamples)
reg_lo <- loess(score ~ income, data=CASchoolsO, 
    span=.8)
lines(CASchoolsO$income, predict(reg_lo),
    col='orange', type='o', pch=8)

## llls (fixed width subsamples)
library(np)
```

```
## Nonparametric Kernel Methods for Mixed Datatypes (version 0.60-17)
## [vignette("np_faq",package="np") provides answers to frequently asked questions]
## [vignette("np",package="np") an overview]
## [vignette("entropy_np",package="np") an overview of entropy-based methods]
```

```r
reg_np <- npreg(score ~ income, data=CASchoolsO,
    bws=2, bandwidth.compute=F)
lines(CASchoolsO$income, predict(reg_np), 
    col='purple', type='o', pch=12)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-16-1.png" width="672" />


# OLS (multiple linear regression)
***

Model and objective
$$
y_i=\beta_0+\beta_1x_{i1}+\beta_2x_{i2}+\ldots+\beta_kx_{ik}+\epsilon_i = X_{i}\beta +\epsilon_i \\
min_{\beta} \sum_{i=1}^{n} (\epsilon_i)^2
$$
Can also be written in matrix form
$$
y=\textbf{X}\beta+\epsilon\\
min_{\beta} (\epsilon' \epsilon)
$$

Point Estimates 
$$
\hat{\beta}=(\textbf{X}'\textbf{X})^{-1}\textbf{X}'y
$$

^[
To derive OLS coefficients in Matrix form, see
* https://jrnold.github.io/intro-methods-notes/ols-in-matrix-form.html
* https://www.fsb.miamioh.edu/lij14/411_note_matrix.pdf
* https://web.stanford.edu/~mrosenfe/soc_meth_proj3/matrix_OLS_NYU_notes.pdf
]

Before fitting the model, summarize your data (as in Part I)


```r
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
library(psych)
```

```
## 
## Attaching package: 'psych'
```

```
## The following object is masked from 'package:car':
## 
##     logit
```

```r
pairs.panels( USArrests[,c('Murder','Assault','UrbanPop')],
    hist.col=grey(0,.25), breaks=30, density=F, ## Diagonal
    ellipses=F, rug=F, smoother=F, pch=16, col=grey(0,.5) ## Lower Triangle
    )
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-17-1.png" width="672" />

Now we fit the model to the data 

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

To measure the ``Goodness of fit'' of the model, we can again compute sums of squared srrors. Adding random data may sometimes improve the fit, however, so we adjust the $R^2$ by the number of covariates $K$.
$$
R^2 = \frac{ESS}{TSS}=1-\frac{RSS}{TSS}\\
R^2_{\text{adj.}} = 1-\frac{n-1}{n-K}(1-R^2)
$$


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

<img src="03-ROLS_files/figure-html/unnamed-chunk-19-1.png" width="672" />


## Variability Estimates and Hypothesis Tests

To estimate the variability of our estimates, we can use the same *data-driven* methods introduced with simple OLS.


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

Also as before, we can conduct independant hypothesis tests.^[This is done using t-values $$\hat{t}_{j} = \frac{\hat{\beta}_j - \beta_{0} }{\hat{\sigma}_{\hat{\beta}_j}}$$. Under some additional assumptions $\hat{t}_{j} \sim t_{n-K}$.] We can conduct joint tests, such as whether two coefficients are equal, by looking at the their joint distribution.

```r
boot_coef_df <- as.data.frame(cbind(ID=boots, t(boot_coefs)))
fig <- plotly::plot_ly(boot_coef_df,
    type = 'scatter', mode = 'markers',
    x = ~UrbanPop, y = ~Assault,
    text = ~paste('<b> boot: ', ID, '</b>'),
    hoverinfo='text',
    showlegend=F,
    marker=list( color='rgba(0, 0, 0, 0.5)'))
fig
```

```{=html}
<div class="plotly html-widget html-fill-item" id="htmlwidget-847b312d4fceb36fe41c" style="width:672px;height:480px;"></div>
<script type="application/json" data-for="htmlwidget-847b312d4fceb36fe41c">{"x":{"visdat":{"136d4f8dca81":["function () ","plotlyVisDat"]},"cur_data":"136d4f8dca81","attrs":{"136d4f8dca81":{"mode":"markers","x":{},"y":{},"text":{},"hoverinfo":"text","showlegend":false,"marker":{"color":"rgba(0, 0, 0, 0.5)"},"alpha_stroke":1,"sizes":[10,100],"spans":[1,20],"type":"scatter"}},"layout":{"margin":{"b":40,"l":60,"t":25,"r":10},"xaxis":{"domain":[0,1],"automargin":true,"title":"UrbanPop"},"yaxis":{"domain":[0,1],"automargin":true,"title":"Assault"},"hovermode":"closest","showlegend":false},"source":"A","config":{"modeBarButtonsToAdd":["hoverclosest","hovercompare"],"showSendToCloud":false},"data":[{"mode":"markers","x":[-0.082844101044341117,-0.062632940561418035,-0.041295536210013833,-0.04564426850920815,0.01583239360459493,-0.061685471795675205,-0.092558380149812866,-0.052012255527347374,-0.068809331386941841,-0.0053114432053432588,7.039677890901584e-05,-0.049514575024836943,-0.032469903778247718,-0.014631572352562379,-0.033896213674058706,-0.037566189963308155,-0.068193738491678604,-0.063790229380802144,-0.018154573500018485,-0.0106942606542092,-0.011726673719635984,-0.03251874236172192,-0.049979747644706772,-0.10885936003243529,-0.024852493156743188,-0.06538282109940316,-0.068707698022462335,-0.040724532977718275,-0.014403166396505624,0.008630152342915743,-0.0081730112136343732,-0.053075881974951437,-0.0045757343459782223,-0.029190265080953799,-0.039023658828070837,-0.079744286657330327,-0.036563951999548296,-0.033896603918806369,-0.047969208226042302,-0.043716453872732396,-0.10355731192670442,-0.079256197267701375,-0.037990854318016215,-0.073191138080588095,-0.059605451944184609,-0.078420429175214773,-0.097630581068575695,-0.076548747695952948,-0.056565849549028012,-0.00053775751388286316,-0.081603531868572568,-0.069382142069698435,-0.019830908297062157,-0.044072126328071656,0.012758867453381248,-0.072732955282949846,-0.055200358670116523,-0.018972737491271839,-0.016333476540956529,-0.048115924432166876,-0.057196740248028045,-0.10161227707958921,-0.017283285298892184,-0.0042957742533013352,-0.066584487776066861,-0.052956555816296172,-0.028104246239244429,-0.11295428859677036,-0.063282714786212335,-0.041377002700461324,-0.022209068181247554,-0.018258597000439837,0.010431215468747619,-0.046400549922992147,-0.063744587294707972,-0.064734136743385198,-0.040950955112702032,-0.055930901028566127,-0.068916063729913407,0.0047792968643849184,-0.024111722421621636,-0.044832361005507179,-0.040819983515353792,-0.041551181113896239,-0.062785420664061287,-0.053064276066791871,-0.039427641005428039,-0.049721701910897219,-0.027034742400074117,-0.037288292230308363,-0.053513489849589715,-0.025408867625192837,-0.03807247045287989,-0.09762785686480302,-0.0086511339648359248,-0.030249101306409044,-0.026710991044253521,-0.045977931291627305,-0.040587058135654684,-0.049351105646147565,-0.071099504648485065,-0.074451491383848156,-0.04960532895649844,-0.07027406105929182,-0.082710916440335638,-0.061195273651492417,-0.067269113265875133,-0.077856377548255987,-0.028488761368669718,-0.016966595954948122,-0.086148291241572111,-0.051574666785555105,-0.084447306789996748,-0.082654079597859517,-0.031216417424200168,-0.017830065807059155,-0.090546691014624064,-0.093202723695729656,-0.019075083735476474,0.027625402740293736,-0.079869234190801747,-0.072621375656079012,-0.065143615245283157,-0.06446054058406897,0.024749485388675198,-0.02973736797941991,-0.038123734214032631,-0.026929586930825096,-0.054944607190003145,-0.10865317186355668,-0.07652703378346494,-0.032115085771721251,-0.040718593105855252,-0.059157685910136655,-0.093238994120085003,-0.038017369927260326,-0.049936813212218267,-0.064784503486353048,0.0022710744186071894,-0.028462842456108202,-0.064381289956802937,-0.079655116174177171,-0.056951995809641456,-0.018073822915851682,-0.049799759172562373,-0.063483151364405854,-0.071007033078384296,-0.0564677634264674,-0.066703620388974372,-0.050118647355720199,-0.066345226929224246,-0.036270140546016537,-0.039238294127656066,-0.040697769316905281,-0.048975479574439186,-0.031385804810680075,-0.081147781102701114,-0.018253470836309873,-0.015899499947381535,-0.034978048688721675,-0.045018694259443062,-0.053638081791961049,-0.028899895683701798,-0.014395549582355593,-0.091086138159712782,-0.046728940555972515,-0.062054553345551065,-0.059158959050115548,-0.109840673795198,-0.036718577839029924,-0.050869578566957764,-0.077666825446130863,-0.074187321945086912,-0.023060042799231607,-0.036841963197317626,-0.073549500590715328,-0.028986412345205267,-0.041403317647619141,-0.050424871153919408,-0.043491411500754959,-0.067318687706778305,-0.040430023960009692,-0.026859068745295162,-0.035849099468010862,-0.066968570485574141,-0.067360756802671853,-0.039097530907493072,-0.05053853572385672,-0.05599946653960719,-0.026301068778712133,-0.020767941285368463,-0.049633248664208096,-0.040212577486415498,0.0011290265198146735,-0.056491758657878186,-0.032846096422507645,-0.029106522353330309,-0.047357878176084743,-0.059250324006140831,-0.059891290648907129,-0.079065399506544301,-0.020896781474865376,-0.031077130893688663,-0.047892341815674609,-0.033224756747609219,-0.043838528801204077,-0.020650308938171807,-0.050541929070786307,-0.049032975434565598,-0.014478215174279298,-0.055289937498284716,-0.046141720297818489,-0.061460701819034007,-0.038405688451800958,-0.048475629480701693,-0.060622080869323899,-0.014624185031457805,-0.013848487631001436,-0.04205936861529757,-0.017085180080216148,-0.043788326090080869,-0.009841117975248042,-0.031695099431815317,-0.074555447603255609,-0.079992103380954652,-0.05543257840561467,-0.038936356097839561,-0.059622529589421921,-0.068878428998406183,-0.083752913658642458,-0.037790308187985767,-0.089838090737658735,-0.019860274030508315,-0.090412543088514513,-0.052455616874269112,-0.029648044595091256,-0.080803700572638582,-0.012971385040721945,-0.014740554790948284,-0.043964114941071997,0.0012239156360568846,-0.069044221895354821,-0.0052611192744426933,-0.063000467528662951,-0.03462345231990227,-0.047750947200771804,-0.073288608164068209,-0.052750170767296975,-0.038514288977134804,-0.049954711637138112,-0.051603548565336631,-0.046493179992049903,-0.054400255207596046,-0.035801605439013957,-0.062937360309411758,-0.012442314964583211,-0.024457670320500505,-0.0435541803398539,-0.0087109326523468495,-0.033888815709147209,-0.055821062866586398,-0.011554809447569184,-0.030613726384945052,-0.051740925250761384,-0.042073889913178661,-0.042775931834560729,-0.037816589089920097,-0.03473289068918415,-0.054631027276240959,-0.06952569897210438,-0.011984071439424442,-0.039823411759295213,0.0045494783958771158,-0.013788642192362886,-0.034961731277506111,-0.018130773435513108,-0.058690114249862389,-0.033782044016367287,-0.035539528762845461,-0.034698375899742194,-0.0095276003228693812,-0.064354365487675563,0.0026345197485797226,-0.083214822111950082,-0.049520466768791641,-0.083828412165153535,-0.085145755924530581,-0.053670189671977626,-0.059886382030894546,-0.025453459249518952,-0.039688046372572394,-0.051848995511599702,-0.072487292494443162,-0.017889337227485237,-0.048036168285794052,-0.044774252856781709,-0.067412116082786133,-0.0034146943685376273,-0.02854491207891751,-0.043551194020510491,-0.07911019443691053,-0.049932725864844325,0.0020355209164293693,-0.073844349550553592,-0.036236814588555669,-0.095698490233782574,-0.086301206975297945,-0.055981042150787773,-0.019068197503519683,-0.061409729916645867,-0.062037929773760443,-0.061448785606032771,-0.1059844069538554,-0.064134327171128894,-0.02301344410854711,-0.046728838957558701,-0.023981576792539306,-0.024712543108647202,-0.060283754688479366,-0.011028945320724043,-0.077120614863457032,-0.05997249974881249,-0.019469327683255468,-0.065720053051092756,-0.027631639672492356,-0.044849963744834367,-0.069794845528884181,-0.067821810655679896,-0.06239722866424819,-0.040509358333323364,-0.10403133974599976,-0.012653119305349363,-0.012920637940355027,-0.024196838676708989,-0.045582850360062377,-0.038069866648591973,-0.073286551757747689,-0.046803877879077048,-0.057206222131055869,-0.011165394644223088,-0.018926797865067443,-0.044055914914003604,-0.050609669159140745,-0.054888645288342794,-0.064441421562298359,-0.063094858249056474,-0.021265787113049987,0.0044467421541467336,-0.019785205256659041,-0.015085969626741233,-0.05937660838031552,-0.051213021196561855,-0.049057354186234033,-0.095493911548844804,-0.012469578068300178,-0.059909804831288403,-0.072311098928155904,-0.042141360810944155,-0.082915550480852487,-0.026828367703817614,-0.019732925442710589,-0.074375617887898149,0.0023394580994833504,-0.037276536990064113,-0.064329854152799099,-0.036488527756253178,-0.095895988211555275,0.038030960545586009,-0.039341596483153322,-0.029421686963222154,-0.047807673770414338,-0.035702520262161315,-0.051968336723128568,-0.047707634560445564,-0.073005941371839231,-0.082989593119753638,-0.032378914297674248,-0.034679764696557307,-0.059164659669715056,-0.053497856307435226,-0.031926617612729989,-0.049130590818300478,-0.032684140618316683,-0.075111522538674133,0.0075646027077540048,-0.045429448645034287,-0.038251765796832926,-0.049237340751746655,-0.033260389120659622,-0.068431143951091566,-0.022495520467711104,-0.011209639468052006,-0.070237184936472338,-0.036216260953119327,-0.011826966782727129,-0.073716457376967984,-0.023793053205685876,-0.070829391181377294,0.0053092657864974978],"y":[0.050310556729631299,0.042790371428303664,0.048392159449245131,0.046691288723640333,0.044881223101905558,0.044589992072425096,0.04279465829192499,0.039034753959615712,0.04931288167048456,0.044432635502422706,0.049573245559784089,0.048796516247060828,0.035786092338515305,0.039309028139892156,0.04129099113519661,0.03367253477039623,0.046141658621704232,0.042507682240588887,0.051255030061760715,0.042584560989406127,0.036599410201457218,0.042074255491396706,0.039153590537467919,0.055719906264628,0.040854300350332239,0.049265732287920402,0.045900870796400275,0.046675333281090678,0.04447294512996508,0.030502994531023783,0.040025965088564146,0.045411317024724847,0.041776255356614535,0.044210065533685249,0.051094411203138783,0.044188376822928248,0.042741862131383666,0.051970609208533886,0.043494318067832376,0.047328334457689095,0.040276186293909555,0.048194735803004082,0.044129383971211932,0.046206832113521071,0.044437280730743066,0.040837560799079596,0.043581961139635028,0.048159377723709471,0.04665520656562349,0.035872987883823031,0.04815098351705098,0.050321713210057517,0.043818067329361735,0.036544007807522844,0.040713039115275296,0.038999825149799348,0.037515058929630744,0.038951556974584363,0.04300281683897262,0.048565331428696137,0.038320525378014066,0.052468169945460524,0.040080177840111093,0.037462084598957349,0.051424133738085,0.045215122077578843,0.041989481503945908,0.037824023608148523,0.034303599917297693,0.039913901559856454,0.040793999707900437,0.038005277119593804,0.03858361050239692,0.039975594082417742,0.044857731391124485,0.041648337106903251,0.039258502647036231,0.042441178558953192,0.044176853085965188,0.043029055647167476,0.039624131667008164,0.041364520790866978,0.0422656780638603,0.050010167886219183,0.042769517378071192,0.043804448415396158,0.035818872635930539,0.046433309198714662,0.044696249915559143,0.043295436033021856,0.038354915114553599,0.048017206521333171,0.049591654137446053,0.047348456886164132,0.042983885183859746,0.044971076200930965,0.043026692753857974,0.042444521018136561,0.047610498853977827,0.042059203635912437,0.046331359792516846,0.047423655915524963,0.041341735404260192,0.046545555761486321,0.052727050096026094,0.04351314929753957,0.046976031274052789,0.038199145957639881,0.043047161748949993,0.0449278667850323,0.049718420472425945,0.051428558876100795,0.047032427772005142,0.051837009845675727,0.044725311726400971,0.045540629536052542,0.049333243140640942,0.044008649487693612,0.041614187324615907,0.038152718578689925,0.044471227205067583,0.051940834912791604,0.041515534284527943,0.045024044449941611,0.041315823233833177,0.045641807567970524,0.041703069100728782,0.043654868558188717,0.040985275374141247,0.047081621155001842,0.040690967544778966,0.042797791086149728,0.043947435954425462,0.041885239874631136,0.040732205037465295,0.044836507956596723,0.041387167747813848,0.04826877502459586,0.03598143459670218,0.045974423682119549,0.048071415635161985,0.046241496557994054,0.039465736526266115,0.040007412857561403,0.046698791499576196,0.04599391734445054,0.048400633380903328,0.045928868872463481,0.044357096763975465,0.044107533580688099,0.055002290984669994,0.045705008877878407,0.036156910300169549,0.044256879192618177,0.042698908219191291,0.046922833320659808,0.036900924372304716,0.041961931163334354,0.042465236272372725,0.037437620091436023,0.040854345370767507,0.043913640193417973,0.037992530889961261,0.040395933194525918,0.043188633244111367,0.043473621161659468,0.042930035855356416,0.040427612862217972,0.04714294753895347,0.041654030773029566,0.043424671665012599,0.045390632488378761,0.047557178656009162,0.03685257045713234,0.044094511525473397,0.046878049353714174,0.04324054513492883,0.040554186643302223,0.039466664083040247,0.042703868653324963,0.040659103268311549,0.044695582604023884,0.041085776024662013,0.042787332531436191,0.042357814198125766,0.049961717228981323,0.046651330081198844,0.050973664156562987,0.048976096861026205,0.042986882132431785,0.037873057405414592,0.044319472210775458,0.042236004202411484,0.042795448285688792,0.042012248235117476,0.04365362910773897,0.044459280749431063,0.04043228715426303,0.040346437450617861,0.048003282632501858,0.047799559448110582,0.041171265675200977,0.041255840268116649,0.042443174403243765,0.043547939525689243,0.041312102558393397,0.044990365837117005,0.05247323088595203,0.03687498784859488,0.046257235127460376,0.045780110123075209,0.048048653199429588,0.043629386511119368,0.041277140154529261,0.04089328904690083,0.049149930061039522,0.043147971899271227,0.041809311953074003,0.044083869866588458,0.047178819045802331,0.043171183673114705,0.038767997996863091,0.038764113701104955,0.047545160816566838,0.049593799607698275,0.041421046285719236,0.041695091907671511,0.050088189085740392,0.042674161804513257,0.046339987428583369,0.047470549801443045,0.047364071506031412,0.045707001581104974,0.049671560959513909,0.041363022853936414,0.044187772738072603,0.05372551666118075,0.043986771652509651,0.042700824324239703,0.042140296243908311,0.040839475931451118,0.042625574558649994,0.044342255888630555,0.049348011066952517,0.04480478868818235,0.039309179423175133,0.049186687307017606,0.040521756740768647,0.044428995292183034,0.040917687528013287,0.046030438949189297,0.046433941414255234,0.042058244727598164,0.047862916780900232,0.042359714939401619,0.04216622702317608,0.043008831343557555,0.048585887927695234,0.043410094150924464,0.041186310154289855,0.043406945525448881,0.037348251395683749,0.049032897529990301,0.036603968742290445,0.049759763232454755,0.048920638821058765,0.037701241982533329,0.045567874554814883,0.049865315242448811,0.049534186496222515,0.03821943554220554,0.053866622130673128,0.041590196878076371,0.045124063911977777,0.040937316001906379,0.046405126293970485,0.038818437989585987,0.045053813534368693,0.040053509222980337,0.043226853053522453,0.043171300509585599,0.047142900071044963,0.041791379688083101,0.040073690932540373,0.047736012859364511,0.04667525360635652,0.039585016664629678,0.048070019690814418,0.038005220484997958,0.041932438444191693,0.04575751027265184,0.045697345708823223,0.042063987082364723,0.045556620620686841,0.04467729129243956,0.042349251337974798,0.050594998308568825,0.041448707280049985,0.04041336545560785,0.044839179655353209,0.046459815407430903,0.046500933904796531,0.040956428700579986,0.053883292264722688,0.044964760107299787,0.050461474083676738,0.049175732884362493,0.057460692374809635,0.046874456594522045,0.044434839239599254,0.04437270397552287,0.044838105774952924,0.044039775751615794,0.04553598847280952,0.036415305849241242,0.037068553771185807,0.043630349826587547,0.046242716324053586,0.050759962299145721,0.043181019235821169,0.050100728089450923,0.04550743009734573,0.037849956262718178,0.045723523946360749,0.045507561886290529,0.038643772763408281,0.048900482568796255,0.038041790579625603,0.049193065542316325,0.045090375154988295,0.047142090819968063,0.04045894847450289,0.039425693785259057,0.041234739959062752,0.042615435926820648,0.040329878685859417,0.048109332827856066,0.03718960706688898,0.044765762954837793,0.045299286766425549,0.040080054288981405,0.045688653087549567,0.038941769821061033,0.047386336430697749,0.048822704758344174,0.04319078946987228,0.045187510429211812,0.042934619355664803,0.042053501210116813,0.044728537519563225,0.04163112134864011,0.047031783607438087,0.040604265588423727,0.046632455879466669,0.044892034317830121,0.043183576021252786,0.037063832631836706,0.040416549597310975,0.044081591428349186,0.050647574634290225,0.034114051927292471,0.049551579142579689,0.037892640810966223,0.04991370402366925,0.05059440640541836,0.041950995197595091,0.048898487862384397,0.037245087324480078,0.02976457481124407,0.049427063116701912,0.038512909188413484,0.046805192054678396,0.035671971525929456,0.043881626561428466,0.04316366129253954,0.034709462750386604,0.043515197556283858,0.035933032406419235,0.044155296190974906,0.049121040131789001,0.046532280769367933,0.048266238318189533,0.046804766795989362,0.040552566683592473,0.043851812166037986,0.039212575726640483,0.03929241110245351,0.045151983979134766,0.045697086996012957,0.045549189434857328,0.049347732939254131,0.039961015425110824,0.0505492256038962,0.04481058702228561,0.048826087611426927,0.048631723604240569,0.034921273738833858,0.044525683060482192,0.04173131903732312],"text":["<b> boot:  1 <\/b>","<b> boot:  2 <\/b>","<b> boot:  3 <\/b>","<b> boot:  4 <\/b>","<b> boot:  5 <\/b>","<b> boot:  6 <\/b>","<b> boot:  7 <\/b>","<b> boot:  8 <\/b>","<b> boot:  9 <\/b>","<b> boot:  10 <\/b>","<b> boot:  11 <\/b>","<b> boot:  12 <\/b>","<b> boot:  13 <\/b>","<b> boot:  14 <\/b>","<b> boot:  15 <\/b>","<b> boot:  16 <\/b>","<b> boot:  17 <\/b>","<b> boot:  18 <\/b>","<b> boot:  19 <\/b>","<b> boot:  20 <\/b>","<b> boot:  21 <\/b>","<b> boot:  22 <\/b>","<b> boot:  23 <\/b>","<b> boot:  24 <\/b>","<b> boot:  25 <\/b>","<b> boot:  26 <\/b>","<b> boot:  27 <\/b>","<b> boot:  28 <\/b>","<b> boot:  29 <\/b>","<b> boot:  30 <\/b>","<b> boot:  31 <\/b>","<b> boot:  32 <\/b>","<b> boot:  33 <\/b>","<b> boot:  34 <\/b>","<b> boot:  35 <\/b>","<b> boot:  36 <\/b>","<b> boot:  37 <\/b>","<b> boot:  38 <\/b>","<b> boot:  39 <\/b>","<b> boot:  40 <\/b>","<b> boot:  41 <\/b>","<b> boot:  42 <\/b>","<b> boot:  43 <\/b>","<b> boot:  44 <\/b>","<b> boot:  45 <\/b>","<b> boot:  46 <\/b>","<b> boot:  47 <\/b>","<b> boot:  48 <\/b>","<b> boot:  49 <\/b>","<b> boot:  50 <\/b>","<b> boot:  51 <\/b>","<b> boot:  52 <\/b>","<b> boot:  53 <\/b>","<b> boot:  54 <\/b>","<b> boot:  55 <\/b>","<b> boot:  56 <\/b>","<b> boot:  57 <\/b>","<b> boot:  58 <\/b>","<b> boot:  59 <\/b>","<b> boot:  60 <\/b>","<b> boot:  61 <\/b>","<b> boot:  62 <\/b>","<b> boot:  63 <\/b>","<b> boot:  64 <\/b>","<b> boot:  65 <\/b>","<b> boot:  66 <\/b>","<b> boot:  67 <\/b>","<b> boot:  68 <\/b>","<b> boot:  69 <\/b>","<b> boot:  70 <\/b>","<b> boot:  71 <\/b>","<b> boot:  72 <\/b>","<b> boot:  73 <\/b>","<b> boot:  74 <\/b>","<b> boot:  75 <\/b>","<b> boot:  76 <\/b>","<b> boot:  77 <\/b>","<b> boot:  78 <\/b>","<b> boot:  79 <\/b>","<b> boot:  80 <\/b>","<b> boot:  81 <\/b>","<b> boot:  82 <\/b>","<b> boot:  83 <\/b>","<b> boot:  84 <\/b>","<b> boot:  85 <\/b>","<b> boot:  86 <\/b>","<b> boot:  87 <\/b>","<b> boot:  88 <\/b>","<b> boot:  89 <\/b>","<b> boot:  90 <\/b>","<b> boot:  91 <\/b>","<b> boot:  92 <\/b>","<b> boot:  93 <\/b>","<b> boot:  94 <\/b>","<b> boot:  95 <\/b>","<b> boot:  96 <\/b>","<b> boot:  97 <\/b>","<b> boot:  98 <\/b>","<b> boot:  99 <\/b>","<b> boot:  100 <\/b>","<b> boot:  101 <\/b>","<b> boot:  102 <\/b>","<b> boot:  103 <\/b>","<b> boot:  104 <\/b>","<b> boot:  105 <\/b>","<b> boot:  106 <\/b>","<b> boot:  107 <\/b>","<b> boot:  108 <\/b>","<b> boot:  109 <\/b>","<b> boot:  110 <\/b>","<b> boot:  111 <\/b>","<b> boot:  112 <\/b>","<b> boot:  113 <\/b>","<b> boot:  114 <\/b>","<b> boot:  115 <\/b>","<b> boot:  116 <\/b>","<b> boot:  117 <\/b>","<b> boot:  118 <\/b>","<b> boot:  119 <\/b>","<b> boot:  120 <\/b>","<b> boot:  121 <\/b>","<b> boot:  122 <\/b>","<b> boot:  123 <\/b>","<b> boot:  124 <\/b>","<b> boot:  125 <\/b>","<b> boot:  126 <\/b>","<b> boot:  127 <\/b>","<b> boot:  128 <\/b>","<b> boot:  129 <\/b>","<b> boot:  130 <\/b>","<b> boot:  131 <\/b>","<b> boot:  132 <\/b>","<b> boot:  133 <\/b>","<b> boot:  134 <\/b>","<b> boot:  135 <\/b>","<b> boot:  136 <\/b>","<b> boot:  137 <\/b>","<b> boot:  138 <\/b>","<b> boot:  139 <\/b>","<b> boot:  140 <\/b>","<b> boot:  141 <\/b>","<b> boot:  142 <\/b>","<b> boot:  143 <\/b>","<b> boot:  144 <\/b>","<b> boot:  145 <\/b>","<b> boot:  146 <\/b>","<b> boot:  147 <\/b>","<b> boot:  148 <\/b>","<b> boot:  149 <\/b>","<b> boot:  150 <\/b>","<b> boot:  151 <\/b>","<b> boot:  152 <\/b>","<b> boot:  153 <\/b>","<b> boot:  154 <\/b>","<b> boot:  155 <\/b>","<b> boot:  156 <\/b>","<b> boot:  157 <\/b>","<b> boot:  158 <\/b>","<b> boot:  159 <\/b>","<b> boot:  160 <\/b>","<b> boot:  161 <\/b>","<b> boot:  162 <\/b>","<b> boot:  163 <\/b>","<b> boot:  164 <\/b>","<b> boot:  165 <\/b>","<b> boot:  166 <\/b>","<b> boot:  167 <\/b>","<b> boot:  168 <\/b>","<b> boot:  169 <\/b>","<b> boot:  170 <\/b>","<b> boot:  171 <\/b>","<b> boot:  172 <\/b>","<b> boot:  173 <\/b>","<b> boot:  174 <\/b>","<b> boot:  175 <\/b>","<b> boot:  176 <\/b>","<b> boot:  177 <\/b>","<b> boot:  178 <\/b>","<b> boot:  179 <\/b>","<b> boot:  180 <\/b>","<b> boot:  181 <\/b>","<b> boot:  182 <\/b>","<b> boot:  183 <\/b>","<b> boot:  184 <\/b>","<b> boot:  185 <\/b>","<b> boot:  186 <\/b>","<b> boot:  187 <\/b>","<b> boot:  188 <\/b>","<b> boot:  189 <\/b>","<b> boot:  190 <\/b>","<b> boot:  191 <\/b>","<b> boot:  192 <\/b>","<b> boot:  193 <\/b>","<b> boot:  194 <\/b>","<b> boot:  195 <\/b>","<b> boot:  196 <\/b>","<b> boot:  197 <\/b>","<b> boot:  198 <\/b>","<b> boot:  199 <\/b>","<b> boot:  200 <\/b>","<b> boot:  201 <\/b>","<b> boot:  202 <\/b>","<b> boot:  203 <\/b>","<b> boot:  204 <\/b>","<b> boot:  205 <\/b>","<b> boot:  206 <\/b>","<b> boot:  207 <\/b>","<b> boot:  208 <\/b>","<b> boot:  209 <\/b>","<b> boot:  210 <\/b>","<b> boot:  211 <\/b>","<b> boot:  212 <\/b>","<b> boot:  213 <\/b>","<b> boot:  214 <\/b>","<b> boot:  215 <\/b>","<b> boot:  216 <\/b>","<b> boot:  217 <\/b>","<b> boot:  218 <\/b>","<b> boot:  219 <\/b>","<b> boot:  220 <\/b>","<b> boot:  221 <\/b>","<b> boot:  222 <\/b>","<b> boot:  223 <\/b>","<b> boot:  224 <\/b>","<b> boot:  225 <\/b>","<b> boot:  226 <\/b>","<b> boot:  227 <\/b>","<b> boot:  228 <\/b>","<b> boot:  229 <\/b>","<b> boot:  230 <\/b>","<b> boot:  231 <\/b>","<b> boot:  232 <\/b>","<b> boot:  233 <\/b>","<b> boot:  234 <\/b>","<b> boot:  235 <\/b>","<b> boot:  236 <\/b>","<b> boot:  237 <\/b>","<b> boot:  238 <\/b>","<b> boot:  239 <\/b>","<b> boot:  240 <\/b>","<b> boot:  241 <\/b>","<b> boot:  242 <\/b>","<b> boot:  243 <\/b>","<b> boot:  244 <\/b>","<b> boot:  245 <\/b>","<b> boot:  246 <\/b>","<b> boot:  247 <\/b>","<b> boot:  248 <\/b>","<b> boot:  249 <\/b>","<b> boot:  250 <\/b>","<b> boot:  251 <\/b>","<b> boot:  252 <\/b>","<b> boot:  253 <\/b>","<b> boot:  254 <\/b>","<b> boot:  255 <\/b>","<b> boot:  256 <\/b>","<b> boot:  257 <\/b>","<b> boot:  258 <\/b>","<b> boot:  259 <\/b>","<b> boot:  260 <\/b>","<b> boot:  261 <\/b>","<b> boot:  262 <\/b>","<b> boot:  263 <\/b>","<b> boot:  264 <\/b>","<b> boot:  265 <\/b>","<b> boot:  266 <\/b>","<b> boot:  267 <\/b>","<b> boot:  268 <\/b>","<b> boot:  269 <\/b>","<b> boot:  270 <\/b>","<b> boot:  271 <\/b>","<b> boot:  272 <\/b>","<b> boot:  273 <\/b>","<b> boot:  274 <\/b>","<b> boot:  275 <\/b>","<b> boot:  276 <\/b>","<b> boot:  277 <\/b>","<b> boot:  278 <\/b>","<b> boot:  279 <\/b>","<b> boot:  280 <\/b>","<b> boot:  281 <\/b>","<b> boot:  282 <\/b>","<b> boot:  283 <\/b>","<b> boot:  284 <\/b>","<b> boot:  285 <\/b>","<b> boot:  286 <\/b>","<b> boot:  287 <\/b>","<b> boot:  288 <\/b>","<b> boot:  289 <\/b>","<b> boot:  290 <\/b>","<b> boot:  291 <\/b>","<b> boot:  292 <\/b>","<b> boot:  293 <\/b>","<b> boot:  294 <\/b>","<b> boot:  295 <\/b>","<b> boot:  296 <\/b>","<b> boot:  297 <\/b>","<b> boot:  298 <\/b>","<b> boot:  299 <\/b>","<b> boot:  300 <\/b>","<b> boot:  301 <\/b>","<b> boot:  302 <\/b>","<b> boot:  303 <\/b>","<b> boot:  304 <\/b>","<b> boot:  305 <\/b>","<b> boot:  306 <\/b>","<b> boot:  307 <\/b>","<b> boot:  308 <\/b>","<b> boot:  309 <\/b>","<b> boot:  310 <\/b>","<b> boot:  311 <\/b>","<b> boot:  312 <\/b>","<b> boot:  313 <\/b>","<b> boot:  314 <\/b>","<b> boot:  315 <\/b>","<b> boot:  316 <\/b>","<b> boot:  317 <\/b>","<b> boot:  318 <\/b>","<b> boot:  319 <\/b>","<b> boot:  320 <\/b>","<b> boot:  321 <\/b>","<b> boot:  322 <\/b>","<b> boot:  323 <\/b>","<b> boot:  324 <\/b>","<b> boot:  325 <\/b>","<b> boot:  326 <\/b>","<b> boot:  327 <\/b>","<b> boot:  328 <\/b>","<b> boot:  329 <\/b>","<b> boot:  330 <\/b>","<b> boot:  331 <\/b>","<b> boot:  332 <\/b>","<b> boot:  333 <\/b>","<b> boot:  334 <\/b>","<b> boot:  335 <\/b>","<b> boot:  336 <\/b>","<b> boot:  337 <\/b>","<b> boot:  338 <\/b>","<b> boot:  339 <\/b>","<b> boot:  340 <\/b>","<b> boot:  341 <\/b>","<b> boot:  342 <\/b>","<b> boot:  343 <\/b>","<b> boot:  344 <\/b>","<b> boot:  345 <\/b>","<b> boot:  346 <\/b>","<b> boot:  347 <\/b>","<b> boot:  348 <\/b>","<b> boot:  349 <\/b>","<b> boot:  350 <\/b>","<b> boot:  351 <\/b>","<b> boot:  352 <\/b>","<b> boot:  353 <\/b>","<b> boot:  354 <\/b>","<b> boot:  355 <\/b>","<b> boot:  356 <\/b>","<b> boot:  357 <\/b>","<b> boot:  358 <\/b>","<b> boot:  359 <\/b>","<b> boot:  360 <\/b>","<b> boot:  361 <\/b>","<b> boot:  362 <\/b>","<b> boot:  363 <\/b>","<b> boot:  364 <\/b>","<b> boot:  365 <\/b>","<b> boot:  366 <\/b>","<b> boot:  367 <\/b>","<b> boot:  368 <\/b>","<b> boot:  369 <\/b>","<b> boot:  370 <\/b>","<b> boot:  371 <\/b>","<b> boot:  372 <\/b>","<b> boot:  373 <\/b>","<b> boot:  374 <\/b>","<b> boot:  375 <\/b>","<b> boot:  376 <\/b>","<b> boot:  377 <\/b>","<b> boot:  378 <\/b>","<b> boot:  379 <\/b>","<b> boot:  380 <\/b>","<b> boot:  381 <\/b>","<b> boot:  382 <\/b>","<b> boot:  383 <\/b>","<b> boot:  384 <\/b>","<b> boot:  385 <\/b>","<b> boot:  386 <\/b>","<b> boot:  387 <\/b>","<b> boot:  388 <\/b>","<b> boot:  389 <\/b>","<b> boot:  390 <\/b>","<b> boot:  391 <\/b>","<b> boot:  392 <\/b>","<b> boot:  393 <\/b>","<b> boot:  394 <\/b>","<b> boot:  395 <\/b>","<b> boot:  396 <\/b>","<b> boot:  397 <\/b>","<b> boot:  398 <\/b>","<b> boot:  399 <\/b>"],"hoverinfo":["text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text"],"showlegend":false,"marker":{"color":"rgba(0, 0, 0, 0.5)","line":{"color":"rgba(31,119,180,1)"}},"type":"scatter","error_y":{"color":"rgba(31,119,180,1)"},"error_x":{"color":"rgba(31,119,180,1)"},"line":{"color":"rgba(31,119,180,1)"},"xaxis":"x","yaxis":"y","frame":null}],"highlight":{"on":"plotly_click","persistent":false,"dynamic":false,"selectize":false,"opacityDim":0.20000000000000001,"selected":{"opacity":1},"debounce":0},"shinyEvents":["plotly_hover","plotly_click","plotly_selected","plotly_relayout","plotly_brushed","plotly_brushing","plotly_clickannotation","plotly_doubleclick","plotly_deselect","plotly_afterplot","plotly_sunburstclick"],"base_url":"https://plot.ly"},"evals":[],"jsHooks":[]}</script>
```

```r
## Show Histogram of Coefficients
## plotly::add_histogram2d(fig, nbinsx=20, nbinsy=20)

## Show 95% Contour
## plotly::add_histogram2dcontour(fig)
## fig <- layout(fig,
##    yaxis = list(title=expression(beta[3])),
##    xaxis = list(title=expression(beta[2])))
```



We can also use an $F$ test for $q$ hypotheses;
$$
\hat{F}_{q} = \frac{(ESS_{restricted}-ESS_{unrestricted})/q}{ESS_{unrestricted}/(n-K)},
$$
and $\hat{F}$ can be written in terms of unrestricted and restricted $R^2$. Under some additional assumptions $\hat{F}_{q}  \sim F_{q,n-K}$. For some inuition, we will examine how the $R^2$ statistic varies with bootstrap samples. Specifically, compute a null $R^2$ distribution by randomly reshuffling the outcomes and compare it to the observed $R^2$.

```r
## Bootstrap NULL
boots <- 1:399
boot_regs0 <- lapply(boots, function(b){
  xy_b <- USArrests
  b_id <- sample( nrow(USArrests), replace=T)
  xy_b$Murder <-  xy_b$Murder[b_id]
  reg_b <- lm(Murder~Assault+UrbanPop, dat=xy_b)
})

boot_coefs0 <- sapply(boot_regs0, function(reg_k){
    coef(reg_k) })
R2_sim0 <- sapply(boot_regs0, function(reg_k){
    summary(reg_k)$r.squared })
R2adj_sim0 <- sapply(boot_regs0, function(reg_k){
    summary(reg_k)$adj.r.squared })

hist(R2adj_sim0, xlim=c(0,1), breaks=25,
    main='', xlab=expression('adj.'~R[b]^2))
abline(v=summary(reg)$adj.r.squared, col="red", lwd=2)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-23-1.png" width="672" />

*Hypothesis Testing is not to be done routinely* and additional complications arise when testing multiple hypothesis.



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
## -39.266  -5.762   0.161   5.903  34.834 
## 
## Coefficients:
##             Estimate Std. Error t value Pr(>|t|)    
## (Intercept)  22.6976     1.2053  18.832  < 2e-16 ***
## x             0.9137     0.1991   4.590 5.01e-06 ***
## fo.L         30.4562     1.0966  27.773  < 2e-16 ***
## fo.Q         14.4263     0.9618  15.000  < 2e-16 ***
## fo.C          4.8210     0.7479   6.446 1.78e-10 ***
## fo^4          1.4428     0.5619   2.568   0.0104 *  
## fuB         -23.6404     0.5891 -40.126  < 2e-16 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 9.271 on 993 degrees of freedom
## Multiple R-squared:  0.7477,	Adjusted R-squared:  0.7461 
## F-statistic: 490.3 on 6 and 993 DF,  p-value: < 2.2e-16
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
```

```
## 
## Attaching package: 'fixest'
```

```
## The following object is masked from 'package:np':
## 
##     se
```

```r
fe_reg1 <- feols(y~x|fo+fu, dat_f)
summary(fe_reg1)
```

```
## OLS estimation, Dep. Var.: y
## Observations: 1,000 
## Fixed-effects: fo: 5,  fu: 2
## Standard-errors: Clustered (fo) 
##   Estimate Std. Error t value Pr(>|t|)    
## x 0.913706    0.27842 3.28175  0.03045 *  
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## RMSE: 9.23823     Adj. R2: 0.746126
##                 Within R2: 0.020772
```

```r
## Compare Coefficients
coef( lm(y~-1+x+fo+fu, dat_f) )
```

```
##           x         fo0         fo1         fo2         fo3         fo4 
##   0.9137058   9.7945102  11.5702042  16.0210372  24.7341968  51.3679374 
##         fuB 
## -23.6403531
```

```r
fixef(fe_reg1)
```

```
## $fo
##        0        1        2        3        4 
##  9.79451 11.57020 16.02104 24.73420 51.36794 
## 
## $fu
##         A         B 
##   0.00000 -23.64035 
## 
## attr(,"class")
## [1] "fixest.fixef" "list"        
## attr(,"references")
## fo fu 
##  0  1 
## attr(,"exponential")
## [1] FALSE
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
## x  1.03138   0.510805 2.01913 0.074226 .  
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## RMSE: 3.42866     Adj. R2: 0.964889
##                 Within R2: 0.163794
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
## -9.6185 -1.5506 -0.0306  1.3451  8.3707 
## 
## Coefficients:
##              Estimate Std. Error t value Pr(>|t|)    
## (Intercept)  15.35419    0.59451  25.827  < 2e-16 ***
## x             2.48293    0.10271  24.175  < 2e-16 ***
## fo.L         27.50539    1.70617  16.121  < 2e-16 ***
## fo.Q          9.30430    1.48435   6.268 5.46e-10 ***
## fo.C          1.98641    1.13576   1.749   0.0806 .  
## fo^4         -1.03778    0.81517  -1.273   0.2033    
## fuB         -15.23195    0.87766 -17.355  < 2e-16 ***
## x:fo.L        4.66923    0.29335  15.917  < 2e-16 ***
## x:fo.Q        2.02712    0.25565   7.929 5.98e-15 ***
## x:fo.C        0.48973    0.19748   2.480   0.0133 *  
## x:fo^4        0.27254    0.14341   1.900   0.0577 .  
## x:fuB        -2.47465    0.14923 -16.583  < 2e-16 ***
## fo.L:fuB    -27.09116    2.53818 -10.673  < 2e-16 ***
## fo.Q:fuB    -11.04996    2.20272  -5.017 6.25e-07 ***
## fo.C:fuB     -4.23465    1.65776  -2.554   0.0108 *  
## fo^4:fuB      0.49632    1.16753   0.425   0.6709    
## x:fo.L:fuB   -4.67916    0.42929 -10.900  < 2e-16 ***
## x:fo.Q:fuB   -1.73116    0.37352  -4.635 4.06e-06 ***
## x:fo.C:fuB   -0.06135    0.28335  -0.217   0.8286    
## x:fo^4:fuB   -0.19264    0.20321  -0.948   0.3434    
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 2.438 on 980 degrees of freedom
## Multiple R-squared:  0.9828,	Adjusted R-squared:  0.9824 
## F-statistic:  2944 on 19 and 980 DF,  p-value: < 2.2e-16
```

```r
#reg2 <- feols(y~x*fo*fu|fo^fu, dat_f)
```


With *Random Effects*, the factor variable is modelled as coming from a distribution that is uncorrelated with the regressors. This is rarely used in economics today, and mostly included for historical reasons and a few cases where fixed effects cannot be estimates.

<!-- 
> The labels "random effects" and "fixed effects" are misleading. These are labels which arose in the early literature and we are stuck with these labels today. In a previous era regressors were viewed as "fixed". Viewing the individual effect as an unobserved regressor leads to the label of the individual effect as "fixed". Today, we rarely refer to regressors as "fixed" when dealing with observational data. We view all variables as random. Consequently describing u i as "fixed" does not make much sense and it is hardly a contrast with the "random effect" label since under either assumption u i is treated as random. Once again, the labels are unfortunate but the key difference is whether u i is correlated with the regressors.
-->


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
##  10.9934900   1.6503856  -0.3715245
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

<img src="03-ROLS_files/figure-html/unnamed-chunk-29-1.png" width="672" />


Many economic phenomena are nonlinear, even when including potential transforms of $Y$ and $X$. Sometimes the linear model may still be a good or even great approximation (how good depends on the research question). In any case, you are safe to interpret your OLS coefficients as "conditional correlations". For example, examine the distribution of coefficients under this mispecified model. Interpret the average.

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

<img src="03-ROLS_files/figure-html/unnamed-chunk-30-1.png" width="672" />


##  Diagnostics

There's little sense in getting great standard errors for a terrible model. Plotting your regression object a simple and easy step to help diagnose whether your model is in some way bad.

```r
reg <- lm(Murder~Assault+UrbanPop, data=USArrests)
par(mfrow=c(2,2))
plot(reg)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-31-1.png" width="672" />
We now go through what these figures show, and then some additional

**Outliers** The first plot examines outlier $Y$ and $\hat{Y}$.

>``In our $y_i = a + b x_i + e_i$ regression, the residuals are, of course, $e_i$ -- they reveal how much our fitted value $\hat{y}_i = a + b x_i$ differs from the observed $y_i$. A point $(x_i ,y_i)$ with a corresponding large residual is called an *outlier*. Say that you are interested in outliers because you somehow think that such points will exert undue *influence* on your estimates. Your feelings are generally right, but there are exceptions. A point might have a huge residual and yet not affect the estimated $b$ at all''
>Stata Press (2015) Base Reference Manual, Release 14, p. 2138.



```r
plot(fitted(reg), resid(reg),col = "grey", pch = 20,
     xlab = "Fitted", ylab = "Residual",
     main = "Fitted versus Residuals")
abline(h = 0, col = "darkorange", lwd = 2)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-32-1.png" width="672" />

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

<img src="03-ROLS_files/figure-html/unnamed-chunk-33-1.png" width="672" />

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
## 37 
## 37
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

<img src="03-ROLS_files/figure-html/unnamed-chunk-35-1.png" width="672" />

```
##      StudRes        Hat       CookD
## 1  -3.528709 0.82508224 22.56662371
## 37  2.937407 0.02711964  0.10015471
## 40 -1.474646 0.04279714  0.04715585
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
##         dfb.1_        dfb.x        dffit    cov.r       cook.d        hat
## 1  5.895593376 -7.546857967 -7.663858558 3.375743 2.256662e+01 0.82508224
## 2 -0.054160385 -0.044130894 -0.191911003 1.008004 1.824283e-02 0.02639579
## 3  0.023873568  0.009686202  0.065910396 1.072814 2.220851e-03 0.02555185
## 4  0.005799585 -0.001646485  0.008974371 1.082620 4.135465e-05 0.02587080
## 5  0.007365469  0.018880718  0.051571358 1.080907 1.362449e-03 0.02886954
## 6  0.017180030 -0.011682579  0.018385232 1.100488 1.735400e-04 0.04193046
```

**Normality**

The second plot examines whether the residuals are normally distributed. OLS point estimates do not depend on the normality of the residuals. (Good thing, because there's no reason the residuals of economic phenomena should be so well behaved.) Many hypothesis tests of the regression estimates are, however, affected by the distribution of the residuals. For these reasons, you may be interested in assessing normality 

```r
par(mfrow=c(1,2))
hist(resid(reg), main='Histogram of Residuals', border=NA)

qqnorm(resid(reg), main="Normal Q-Q Plot of Residuals", col="darkgrey")
qqline(resid(reg), col="dodgerblue", lwd=2)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-39-1.png" width="672" />

```r
shapiro.test(resid(reg))
```

```
## 
## 	Shapiro-Wilk normality test
## 
## data:  resid(reg)
## W = 0.95995, p-value = 0.1668
```

```r
# car::qqPlot(reg)
```

Heterskedasticity may also matters for variance estimates. This is not shown in the plot, but you can run a simple test

```r
library(lmtest)
lmtest::bptest(reg)
```

```
## 
## 	studentized Breusch-Pagan test
## 
## data:  reg
## BP = 0.29693, df = 1, p-value = 0.5858
```

**Collinearity**
This is when one explanatory variable in a multiple linear regression model can be linearly predicted from the others with a substantial degree of accuracy. Coefficient estimates may change erratically in response to small changes in the model or the data. (In the extreme case where there are more variables than observations $K>\geq N$, $X'X$ has an infinite number of solutions and is not invertible.)

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


Data transformations can often improve model fit and still be estimated via OLS. This is because OLS only requires the model to be linear in the parameters. Under the assumptions of the model is correctly specified, the following table is how we can interpret the coefficients of the transformed data. (Note for small changes, $\Delta ln(x) \approx \Delta x / x = \Delta x \% \cdot 100$.)

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
```

```
## 
## Attaching package: 'ggplot2'
```

```
## The following objects are masked from 'package:psych':
## 
##     %+%, alpha
```

```r
ggplot(rl_df, aes(rho, lambda, fill=log(mse) )) +
    geom_tile() + ggtitle('Mean Squared Error') 
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-42-1.png" width="672" />

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

<img src="03-ROLS_files/figure-html/unnamed-chunk-42-2.png" width="672" />

Note that the default hypothesis testing procedures do not account for you trying out different transformations. Specification searches deflate standard errors and are a major source for false discoveries.




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

Diagnostics

* https://book.stat420.org/model-diagnostics.html#leverage
* https://socialsciences.mcmaster.ca/jfox/Books/RegressionDiagnostics/index.html
* https://bookdown.org/ripberjt/labbook/diagnosing-and-addressing-problems-in-linear-regression.html
* Belsley, D. A., Kuh, E., and Welsch, R. E. (1980). Regression Diagnostics: Identifying influential data and sources of collinearity. Wiley. https://doi.org/10.1002/0471725153
* Fox, J. D. (2020). Regression diagnostics: An introduction (2nd ed.). SAGE. https://dx.doi.org/10.4135/9781071878651



# Endogeneity Issues
***

Just like many economic relationships are nonlinear, many economic variables are endogenous. By this we typically mean that $X$ is an outcome determined (or caused: $\to$) by some other variable.

 * If $Y \to X$, then we have reverse causality
 * If $Y \to X$ and $X \to Y$, then we have simultaneity
 * If $Z\to Y$ and either $Z\to X$ or $X \to Z$, then we have omitted a potentially important variable

These endogeneity issues imply $X$ and $\epsilon$ are correlated, which is a barrier to interpreting OLS estimates causally. ($X$ and $\epsilon$ may be correlated for other reasons too, such as when $X$ is measured with error.)


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

<img src="03-ROLS_files/figure-html/unnamed-chunk-43-1.png" width="672" />

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


Three statistical tools: 2SLS, RDD, and DID, are designed to address endogeneity issues. The elementary versions of these tools are linear regression. Because there are many textbooks and online notebooks that explain these methods at both high and low levels of technical detail, they are not covered extensively in this notebook. 


## Two Stage Least Squares (2SLS)

There are many approaches to 2SLS, but I will focus on the seminal example in economics. Suppose we ask "what is the effect of price on quantity?" You can simply run a regression of one variable on another, but you will need much luck to correctly intepret the resulting coefficient. The reason is simultaneity: price and quantity mutually cause one another in markets.^[Although there are many ways this simultaneity can happen, economic theorists have made great strides in analyzing the simultaneity problem as it arises from market relationships. In fact, the 2SLS statistical approach arose to understand the equilibrium of competitive agricultural markets.]

**Competitive Market Equilibrium** has three structural relationships: (1) market supply is the sum of quantities supplied by individual firms at a given price, (2) market demand is the sum of quantities demanded by individual people at a given price, and (3) market supply equals market demand in equilibrium. Assuming market supply and demand are linear, we can write these three "structural equations" as
\begin{eqnarray}
Q_{S}(P) &=& A_{S} + B_{S} P + E_{S},\\
Q_{D}(P) &=& A_{D} - B_{D} P + E_{D},\\
Q_{D} &=& Q_{S} = Q.
%%  $Q_{D}(P) = \sum_{i} q_{D}_{i}(P)$, 
\end{eqnarray}
This last equation implies a simultaneous "reduced form" relationship where both the price and the quantity are outcomes. With a linear parametric structure to these equations, we can use algebra to solve for the equilibrium price and quantity analytically as
\begin{eqnarray}
P^{*} &=& \frac{A_{D}-A_{S}}{B_{D}+B_{S}} + \frac{E_{D} - E_{S}}{B_{D}+B_{S}}, \\
Q^{*} &=& \frac{A_{S}B_{D}+ A_{D}B_{S}}{B_{D}+B_{S}} + \frac{E_{S}B_{D}+ E_{D}B_{S}}{B_{D}+B_{S}}.
\end{eqnarray}



```r
## Demand Curve Simulator
qd_fun <- function(p, Ad=8, Bd=-.8, Ed_sigma=.25){
    Qd <- Ad + Bd*p + rnorm(1,0,Ed_sigma)
    return(Qd)
}

## Supply Curve Simulator
qs_fun <- function(p, As=-8, Bs=1, Es_sigma=.25){
    Qs <- As + Bs*p + rnorm(1,0,Es_sigma)
    return(Qs)
}

## Quantity Supplied and Demanded at 3 Prices
cbind(P=8:10, D=qd_fun(8:10), S=qs_fun(8:10))
```

```
##       P          D           S
## [1,]  8  1.4258219 -0.07388062
## [2,]  9  0.6258219  0.92611938
## [3,] 10 -0.1741781  1.92611938
```

```r
## Market Equilibrium Finder
eq_fun <- function(demand, supply, P){
    ## Compute EQ (what we observe)
    eq_id <- which.min( abs(demand-supply) )
    eq <- c(P=P[eq_id], Q=demand[eq_id]) 
    return(eq)
}
```



```r
## Simulations Parameters
N <- 300 ## Number of Market Interactions
P <- seq(5,10,by=.01) ## Price Range to Consider

## Generate Data from Competitive Market  
## Plot Underlying Process
plot.new()
plot.window(xlim=c(0,2), ylim=range(P))
EQ1 <- sapply(1:N, function(n){
    ## Market Data Generating Process
    demand <- qd_fun(P)
    supply <- qs_fun(P)
    eq <- eq_fun(demand, supply, P)    
    ## Plot Theoretical Supply and Demand
	lines(demand, P, col=grey(0,.01))
	lines(supply, P, col=grey(0,.01))
    points(eq[2], eq[1], col=grey(0,.05), pch=16)
    ## Save Data
    return(eq)
})
axis(1)
axis(2)
mtext('Quantity',1, line=2)
mtext('Price',2, line=2)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-45-1.png" width="672" />

Now regress quantity ("Y") on price ("X"): $\widehat{\beta}_{OLS} = Cov(Q^{*}, P^{*}) / Var(P^{*})$. You get a number back, but it is hard to interpret meaningfully. 

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
##     Min      1Q  Median      3Q     Max 
## -0.5782 -0.1367 -0.0132  0.1216  0.5108 
## 
## Coefficients:
##             Estimate Std. Error t value Pr(>|t|)
## (Intercept)  0.10465    0.48444   0.216    0.829
## P            0.08830    0.05447   1.621    0.106
## 
## Residual standard error: 0.188 on 298 degrees of freedom
## Multiple R-squared:  0.00874,	Adjusted R-squared:  0.005414 
## F-statistic: 2.628 on 1 and 298 DF,  p-value: 0.1061
```
This simple derivation has a profound insight: price-quantity data does not generally tell you how price affects quantity (or vice-versa). Moreover, it also clarifies that our initial question "what is the effect of price on quantity?" is misguided. We could more sensibly ask  "what is the effect of price on quantity supplied?" or "what is the effect of price on quantity demanded?"


If you have exogeneous variation on one side of the market, "shocks", you can get information on the other. For example, lower costs shift out supply (more is produced at given price), allowing you to trace out part of a demand curve.
Experimental manipulation of $A_{S}$ leads to 
\begin{eqnarray}
\label{eqn:comp_market_statics}
\frac{d P^{*}}{d A_{S}} = \frac{-1}{B_{D}+B_{S}}, \\
\frac{d Q^{*}}{d A_{S}} = \frac{B_{D}}{B_{D}+B_{S}}.
\end{eqnarray}
So, absent any other changes, we could recover $-B_{D}=d Q^{*}/d P^{*}$. In this case, the supply shock has identified the demand slope.^[Notice that even in this linear model, however, all effects are conditional: *The* effect of a cost change on quantity or price depends on the demand curve. A change in costs affects quantity supplied but not quantity demanded (which then affects equilibrium price) but the demand side of the market still matters! The change in price from a change in costs depends on the elasticity of demand.]


```r
## New Observations After Cost Change
EQ2 <- sapply(1:N, function(n){
    demand <- qd_fun(P)
    supply2 <- qs_fun(P, As=-6.5) ## More Supplied at Given Price
    eq <- eq_fun(demand, supply2, P)
    return(eq)
	## lines(supply2, P, col=rgb(0,0,1,.01))
    #points(eq[2], eq[1], col=rgb(0,0,1,.05), pch=16)	
})
dat2 <- data.frame(t(EQ2), cost='2')

## Plot Market Data 
dat2 <- rbind(dat1, dat2)
cols <- ifelse(as.numeric(dat2$cost)==2, rgb(0,0,1,.2), rgb(0,0,0,.2))
plot.new()
plot.window(xlim=c(0,2), ylim=range(P))
points(dat2$Q, dat2$P, col=cols, pch=16)
axis(1)
axis(2)
mtext('Quantity',1, line=2)
mtext('Price',2, line=2)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-47-1.png" width="672" />

We are not quite done yet, however. We have pooled two datasets that are seperately problematic, and the noisiness of the process within each group affects our OLS estimate: $\widehat{\beta}_{OLS}=Cov(Q^{*}, P^{*}) / Var(P^{*})$.

```r
## Not exactly right, but at least right sign
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
## -0.73060 -0.17541 -0.00829  0.17068  0.74994 
## 
## Coefficients:
##             Estimate Std. Error t value Pr(>|t|)    
## (Intercept)  6.67257    0.19204   34.75   <2e-16 ***
## P           -0.64218    0.02261  -28.41   <2e-16 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 0.2507 on 598 degrees of freedom
## Multiple R-squared:  0.5744,	Adjusted R-squared:  0.5737 
## F-statistic:   807 on 1 and 598 DF,  p-value: < 2.2e-16
```
Although the individual observations are noisy, we can compute the change in the expected values $d \mathbb{E}[Q^{*}] / d \mathbb{E}[P^{*}] =-B_{D}$. Empirically, this is estimated via the change in average value.

```r
## Wald (1940) Estimate
dat_mean <- rbind(
    colMeans(dat2[dat2$cost==1,1:2]),
    colMeans(dat2[dat2$cost==2,1:2]))
dat_mean
```

```
##             P         Q
## [1,] 8.891167 0.8897032
## [2,] 8.074800 1.5602511
```

```r
B_est <- diff(dat_mean[,2])/diff(dat_mean[,1])
round(B_est, 2)
```

```
## [1] -0.82
```
We can also seperately recover $d \mathbb{E}[Q^{*}] / d \mathbb{E}[A_{S}]$ and $d \mathbb{E}[P^{*}] / d \mathbb{E}[A_{S}]$ from seperate regressions

```r
## Heckman (2000, p.58) Estimate
ols_1 <- lm(P~cost, data=dat2)
ols_2 <- lm(Q~cost, data=dat2)
B_est2 <- coef(ols_2)/coef(ols_1)
round(B_est2[[2]],2)
```

```
## [1] -0.82
```
Mathematically, we can also do this in a single step by exploiting linear algebra: 
\begin{eqnarray}
\frac{\frac{ Cov(Q^{*},A_{S})}{ V(A_{S}) } }{\frac{ Cov(P^{*},A_{S})}{ V(A_{S}) }}
&=& \frac{Cov(Q^{*},A_{S} )}{ Cov(P^{*},A_{S})}.
\end{eqnarray}


Alternatively, we can recover the same estimate using an instrumental variables regression that has two equations:
\begin{eqnarray}
P &=& \alpha_{1} + A_{S} \beta_{1} + \epsilon_{1} \\
Q &=& \alpha_{2} + \hat{P} \beta_{2} + \epsilon_{2}.
\end{eqnarray}
In the first regression, we estimate the average effect of the cost shock on prices. In the second equation, we estimate how the average effect of prices *which are exogenous to demand* affect quantity demanded. To see this, first substitute the equilibrium condition into the supply equation: $Q_{D}=Q_{S}=A_{S}+B_{S} P + E_{S}$, lets us rewrite $P$ as a function of $Q_{D}$. This yields two theoretical equations
\begin{eqnarray}
\label{eqn:linear_supply_iv}
P &=& -\frac{A_{S}}{{B_{S}}} + \frac{Q_{D}}{B_{S}} - \frac{E_{S}}{B_{S}} \\
\label{eqn:linear_demand_iv}
Q_{D} &=&  A_{D} + B_{D} P  + E_{D}.
\end{eqnarray}


```r
## Two Stage Least Squares Estimate
ols_1 <- lm(P~cost, data=dat2)
dat2_new  <- cbind(dat2, Phat=predict(ols_1))
reg_2sls <- lm(Q~Phat, data=dat2_new)
summary(reg_2sls)
```

```
## 
## Call:
## lm(formula = Q ~ Phat, data = dat2_new)
## 
## Residuals:
##      Min       1Q   Median       3Q      Max 
## -0.57568 -0.12985 -0.00523  0.12429  0.55144 
## 
## Coefficients:
##             Estimate Std. Error t value Pr(>|t|)    
## (Intercept)  8.19274    0.15868   51.63   <2e-16 ***
## Phat        -0.82138    0.01868  -43.96   <2e-16 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 0.1868 on 598 degrees of freedom
## Multiple R-squared:  0.7637,	Adjusted R-squared:  0.7633 
## F-statistic:  1933 on 1 and 598 DF,  p-value: < 2.2e-16
```

```r
## One Stage Instrumental Variables Estimate
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
## (Intercept)  8.192736    0.22387  36.5960 < 2.2e-16 ***
## fit_P       -0.821381    0.02636 -31.1602 < 2.2e-16 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## RMSE: 0.263118   Adj. R2: 0.52886
## F-test (1st stage), P: stat = 2,595.4, p < 2.2e-16, on 1 and 598 DoF.
##            Wu-Hausman: stat =   500.6, p < 2.2e-16, on 1 and 597 DoF.
```

**Within Group Variance**
You can experiment with the effect of different variances on both OLS and IV in the code below. And note that if we had multiple supply shifts and recorded their magnitudes, then we could recover more information about demand, perhaps tracing it out entirely.

```r
## Examine
Egrid <- expand.grid(Ed_sigma=c(.001, .25, 1), Es_sigma=c(.001, .25, 1))

Egrid_regs <- lapply(1:nrow(Egrid), function(i){
    Ed_sigma <- Egrid[i,1]
    Es_sigma <- Egrid[i,2]    
    EQ1 <- sapply(1:N, function(n){
        demand <- qd_fun(P, Ed_sigma=Ed_sigma)
        supply <- qs_fun(P, Es_sigma=Es_sigma)
        return(eq_fun(demand, supply, P))
    })
    EQ2 <- sapply(1:N, function(n){
        demand <- qd_fun(P,Ed_sigma=Ed_sigma)
        supply2 <- qs_fun(P, As=-6.5,Es_sigma=Es_sigma)
        return(eq_fun(demand, supply2, P))
    })
    dat <- rbind(
        data.frame(t(EQ1), cost='1'),
        data.frame(t(EQ2), cost='2'))
    return(dat)
})
Egrid_OLS <- sapply(Egrid_regs, function(dat) coef( lm(Q~P, data=dat)))
Egrid_IV <- sapply(Egrid_regs, function(dat) coef( feols(Q~1|P~cost, data=dat)))

#cbind(Egrid, coef_OLS=t(Egrid_OLS)[,2], coef_IV=t(Egrid_IV)[,2])
lapply( list(Egrid_OLS, Egrid_IV), function(ei){
    Emat <- matrix(ei[2,],3,3)
    rownames(Emat) <- paste0('Ed_sigma.',c(.001, .25, 1))
    colnames(Emat) <- paste0('Es_sigma.',c(.001, .25, 1))
    return( round(Emat,2))
})
```

```
## [[1]]
##                Es_sigma.0.001 Es_sigma.0.25 Es_sigma.1
## Ed_sigma.0.001          -0.80         -0.80      -0.80
## Ed_sigma.0.25           -0.61         -0.64      -0.71
## Ed_sigma.1               0.30          0.32      -0.09
## 
## [[2]]
##                Es_sigma.0.001 Es_sigma.0.25 Es_sigma.1
## Ed_sigma.0.001          -0.80         -0.80      -0.80
## Ed_sigma.0.25           -0.79         -0.80      -0.77
## Ed_sigma.1              -0.61         -0.82      -0.72
```




**Caveats** 
Regression analysis with instrumental variables can be very insightful and is applied to many different areas. But I also want to stress some caveats about using IV in practice.

We always get coefficients back when running `feols`, and sometimes the computed p-values are very small. The interpretation of those numbers rests on many assumptions:

* only supply was affected. (Instrument exogeneity)
* the shock is large enough to be picked up statistically. (Instrument relevance)
* supply and demand are linear and additively seperable. (Functional form)
* we were not cycling through different IV's. (Multiple hypotheses)

We are rarely sure that all of these assumptions hold, and this is one reason why researchers often also report their OLS results. In practice, it is hard to find a good instrument. For example, suppose we asked "what is the effect of wages on police demanded?" and examined a policy which lowered the educational requirements from 4 years to 2 to become an officer. This increases the labour supply, but it also affects the demand curve through ``general equilibrium'': as some of the new officers were potentially criminals. With fewer criminals, the demand for likely police shifts down.

In practice, it is also easy to find a bad instrument. As you search for good instruments, sometimes random noise will appear like a good instrument (Spurious Instruments). Worse, if you search for a good instrument for too long, you can also be led astray from important questions (Spurious Research).






## Regression Discontinuities/Kink (RD/RK)

The basic idea here is to examine how a variable changes in response to an exogenous shock. The Regression Discontinuities estimate of the cost shock is the difference in the outcome variable just before and just after the shock. We now turn to our canonical competitive market example. The RD estimate is the difference between the lines at $T=300$.


```r
dat2$T <- 1:nrow(dat2)

plot(P~T, dat2, main='Effect of Cost Shock on Price', pch=16, col=grey(0,.5))
regP1 <- lm(P~T, dat2[dat2$cost==1,]) 
lines(regP1$model$T, predict(regP1), col=2)
regP2 <- lm(P~T, dat2[dat2$cost==2,]) 
lines(regP2$model$T, predict(regP2), col=4)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-54-1.png" width="672" />

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
##     Min      1Q  Median      3Q     Max 
## -0.5312 -0.1370  0.0052  0.1345  0.5963 
## 
## Coefficients:
##               Estimate Std. Error t value Pr(>|t|)    
## (Intercept)  8.883e+00  2.275e-02 390.491   <2e-16 ***
## T            5.379e-05  1.310e-04   0.411    0.682    
## cost2       -7.776e-01  6.426e-02 -12.100   <2e-16 ***
## T:cost2     -1.220e-04  1.853e-04  -0.658    0.511    
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 0.1965 on 596 degrees of freedom
## Multiple R-squared:  0.8129,	Adjusted R-squared:  0.8119 
## F-statistic:   863 on 3 and 596 DF,  p-value: < 2.2e-16
```


```r
plot(Q~T, dat2, main='Effect of Cost Shock on Quantity', pch=16, col=grey(0,.5))
regQ1 <- lm(Q~T, dat2[dat2$cost==1,]) 
lines(regQ1$model$T, predict(regQ1), col=2)
regQ2 <- lm(Q~T, dat2[dat2$cost==2,]) 
lines(regQ2$model$T, predict(regQ2), col=4)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-55-1.png" width="672" />

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
## -0.57599 -0.12996 -0.00584  0.12462  0.55278 
## 
## Coefficients:
##               Estimate Std. Error t value Pr(>|t|)    
## (Intercept)  8.905e-01  2.166e-02  41.109   <2e-16 ***
## T           -5.007e-06  1.247e-04  -0.040    0.968    
## cost2        6.640e-01  6.119e-02  10.852   <2e-16 ***
## T:cost2      1.780e-05  1.764e-04   0.101    0.920    
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 0.1871 on 596 degrees of freedom
## Multiple R-squared:  0.7637,	Adjusted R-squared:  0.7625 
## F-statistic: 642.1 on 3 and 596 DF,  p-value: < 2.2e-16
```

Remember that this is effect is *local*: different magnitudes of the cost shock or different demand curves generally yeild different estimates.

## Difference in Differences (DID)

The basic idea here is to examine how a variable changes in response to an exogenous shock, *compared to a control group*. 


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

<img src="03-ROLS_files/figure-html/unnamed-chunk-56-1.png" width="672" />

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
## -0.54065 -0.13001  0.01023  0.13147  0.60107 
## 
## Coefficients:
##               Estimate Std. Error t value Pr(>|t|)    
## (Intercept)  8.888e+00  1.185e-02 749.736   <2e-16 ***
## T            4.605e-06  3.946e-05   0.117    0.907    
## cost2       -7.825e-01  6.120e-02 -12.786   <2e-16 ***
## T:cost2     -7.279e-05  1.367e-04  -0.532    0.594    
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 0.1963 on 1196 degrees of freedom
## Multiple R-squared:  0.764,	Adjusted R-squared:  0.7634 
## F-statistic:  1291 on 3 and 1196 DF,  p-value: < 2.2e-16
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
## -0.57328 -0.12445 -0.00129  0.12419  0.55278 
## 
## Coefficients:
##               Estimate Std. Error t value Pr(>|t|)    
## (Intercept)  8.883e-01  1.110e-02  80.025   <2e-16 ***
## T           -1.140e-05  3.695e-05  -0.308    0.758    
## cost2        6.662e-01  5.731e-02  11.625   <2e-16 ***
## T:cost2      2.419e-05  1.280e-04   0.189    0.850    
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 0.1838 on 1196 degrees of freedom
## Multiple R-squared:  0.7171,	Adjusted R-squared:  0.7164 
## F-statistic:  1011 on 3 and 1196 DF,  p-value: < 2.2e-16
```


## More Literature

You are directed to the following resources which discusses endogeneity in more detail and how it applies generally.

* Causal Inference for Statistics, Social, and Biomedical Sciences: An Introduction
* https://www.mostlyharmlesseconometrics.com/
* https://www.econometrics-with-r.org
* https://bookdown.org/paul/applied-causal-analysis/
* https://mixtape.scunning.com/
* https://theeffectbook.net/
* https://www.r-causal.org/
* https://matheusfacure.github.io/python-causality-handbook/landing-page.html

For IV, 

* https://cameron.econ.ucdavis.edu/e240a/ch04iv.pdf
* https://mru.org/courses/mastering-econometrics/introduction-instrumental-variables-part-one
* https://www.econometrics-with-r.org/12-ivr.html
* https://bookdown.org/paul/applied-causal-analysis/estimation-2.html
* https://mixtape.scunning.com/07-instrumental_variables
* https://theeffectbook.net/ch-InstrumentalVariables.html
* http://www.urfie.net/read/index.html#page/247

For RDD and DID, 

* https://bookdown.org/paul/applied-causal-analysis/rdd-regression-discontinuity-design.html
* https://mixtape.scunning.com/06-regression_discontinuity
* https://theeffectbook.net/ch-RegressionDiscontinuity.html
* https://mixtape.scunning.com/09-difference_in_differences
* https://theeffectbook.net/ch-DifferenceinDifference.html
* http://www.urfie.net/read/index.html#page/226
    

# Data Scientism
***

There is currently a boom in empirical research centered around linear regression analysis. This is not for the first boom in empirical research, and we'd be wise to recall some earlier wisdom from economists on the matter.

> The most reckless and treacherous of all theorists is he who professes to let facts and figures speak for themselves, who keeps in the background the part he has played, perhaps unconsciously, in selecting and grouping them
>
> ---  Alfred Marshall, 1885 


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



In this age of big data, we are getting more and more data. Perhaps surprisingly, this makes it easier to make false discoveries. We consider three main ways for these to arise. After that, there are examples of scientism with the ''latest and greatest'' empirical recipes---we don't have so many theoretical results yet but I think you can understand the issue with the numerical example. 

## Data Errors

A huge amount of data normally means a huge amount of data cleaning/merging/aggregating. This avoids many copy-paste errors, which are a recipe for [disaster](https://blog.hurree.co/8-of-the-biggest-excel-mistakes-of-all-time), but may also introduce other types of errors. Some spurious results are driven by honest errors in data cleaning. According to one [estimate](https://www.pnas.org/doi/10.1073/pnas.1212247109), this is responsible for around one fifth of all medical science retractions (there is even a whole [book](https://www.amazon.de/Much-Cost-Coding-Errors-Implementation/dp/1543772994) about this!). Although there are not similar meta-analysis in economics, there are some high-profile examples. This includes papers that are highly influential, like [Lott, Levitt](https://scienceblogs.com/deltoid/2005/12/02/lott-levitt-and-coding-errors) and [Reinhart and Rogoff](https://blogs.lse.ac.uk/impactofsocialsciences/2013/04/24/reinhart-rogoff-revisited-why-we-need-open-data-in-economics/) as well as others the top economics journals, like the [RESTUD](https://academic.oup.com/restud/article/90/2/1009/6982752) and [AER](https://www.aeaweb.org/articles?id=10.1257/aer.113.7.2053). There are some reasons to think such errors are more widespread across the social sciences; e.g., in [Census data](https://www2.census.gov/ces/tp/tp-2002-17.pdf) and [Aid data](https://www.sciencedirect.com/science/article/abs/pii/S0305750X11001951). So be careful!

Note: one reason to plot your data is to help spot such errors.


## P-Hacking

Another class of errors pertains to P-hacking (and it's various synonyms: data drudging, star mining,....). While there are cases of fraudulent data manipulation (which can be considered as a dishonest data error), P-hacking is a much more [pernicious](https://elephantinthelab.org/a-replication-crisis-in-the-making/) and [widespread](https://www.americanscientist.org/article/the-statistical-crisis-in-science)

```r
set.seed(123)
n <- 50
X1 <- runif(n)

## Regression Machine:
## repeatedly finds covariate, runs regression
## stops when statistically significant at .1\% 

p <- 1
i <- 0
while(p >= .001){ 
    ## Get Random Covariate
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
    main=paste0('Random Dataset ', i,":   p=", formatC(p,digits=2, format='fg')))
abline(reg_i)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-57-1.png" width="672" />

```r
#summary(reg_i)
```



```r
## P-hacking 2SLS
library(fixest)
p <- 1
ii <- 0
set.seed(123)
while(p >= .05){
    ## Get Random Covariates
    X2 <-  runif(n)    
    X3 <-  runif(n)
    ## Create Treatment Variable based on Cutoff
    cutoffs <- seq(0,1,length.out=11)[-c(1,11)]
    for(tau in cutoffs){
        T3 <- 1*(X3 > tau)
        ## Merge and `Analyze'
        dat_i <- data.frame(X1,X2,T3)
        ivreg_i <- feols(X1~1|X2~T3, data=dat_i)
        ## Update results in global environment
        ptab <- summary(ivreg_i)$coeftable
        if( nrow(ptab)==2){
            p <- ptab[2,4]
            ii <- ii+1
        }
    }
}
summary(ivreg_i)
```

```
## TSLS estimation, Dep. Var.: X1, Endo.: X2, Instr.: T3
## Second stage: Dep. Var.: X1
## Observations: 50 
## Standard-errors: IID 
##              Estimate Std. Error       t value  Pr(>|t|)    
## (Intercept) -9.95e-14   1.28e-13 -7.750700e-01    0.4421    
## fit_X2       1.00e+00   2.46e-13  4.060978e+12 < 2.2e-16 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## RMSE: 5.81e-14   Adj. R2: 1
## F-test (1st stage), X2: stat = 0.664884, p = 0.418869, on 1 and 48 DoF.
##             Wu-Hausman: stat = 0.232185, p = 0.632145, on 1 and 47 DoF.
```

## Spurious Regression 
 
Even without any coding errors or p-hacking, you can sometimes make a false discovery. We begin with a motivating empirical example of "US Gov't Spending on Science".


First, get and inspect some data from https://tylervigen.com/spurious-correlations

```r
## Your data is not made up in the computer (hopefully!)
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
reg1 <-  lm(cage_films ~ -1 + science_spending, data=vigen_csv)
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

<img src="03-ROLS_files/figure-html/unnamed-chunk-61-1.png" width="672" />



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

<img src="03-ROLS_files/figure-html/unnamed-chunk-62-1.png" width="672" />



```r
## Include an intercept to regression 1
#reg2 <-  lm(cage_films ~ science_spending, data=vigen_csv)
#suppressMessages(library(stargazer))
#stargazer(reg1, reg2, type='html')
```


We now run IV regressions for different variable combinations in the dataset

```r
knames <- names(vigen_csv)[2:11] ## First 10 Variables
#knames <- names(vigen_csv)[-1] ## All Variables
p <- 1
ii <- 1
ivreg_list <- vector("list", factorial(length(knames))/factorial(length(knames)-3))

## Choose 3 variable
for( k1 in knames){
for( k2 in setdiff(knames,k1)){
for( k3 in setdiff(knames,c(k1,k2)) ){   
    X1 <- vigen_csv[,k1]
    X2 <- vigen_csv[,k2]
    X3 <- vigen_csv[,k3]
    ## Merge and `Analyze'        
    dat_i <- na.omit(data.frame(X1,X2,X3))
    ivreg_i <- feols(X1~1|X2~X3, data=dat_i)
    ivreg_list[[ii]] <- list(ivreg_i, c(k1,k2,k3))
    ii <- ii+1
}}}
pvals <- sapply(ivreg_list, function(ivreg_i){ivreg_i[[1]]$coeftable[2,4]})

plot(ecdf(pvals), xlab='p-value', ylab='CDF', main='Frequency IV is Statistically Significant')
abline(v=c(.01,.05), col=c(2,4))
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-64-1.png" width="672" />

```r
## Most Significant Spurious Combinations
pvars <- sapply(ivreg_list, function(ivreg_i){ivreg_i[[2]]})
pdat <- data.frame(t(pvars), pvals)
pdat <- pdat[order(pdat$pvals),]
head(pdat)
```

```
##                     X1                 X2            X3        pvals
## 4     science_spending   hanging_suicides    bed_deaths 3.049883e-08
## 76    hanging_suicides   science_spending    bed_deaths 3.049883e-08
## 3     science_spending   hanging_suicides cheese_percap 3.344890e-08
## 75    hanging_suicides   science_spending cheese_percap 3.344890e-08
## 485 maine_divorce_rate   margarine_percap cheese_percap 3.997738e-08
## 557   margarine_percap maine_divorce_rate cheese_percap 3.997738e-08
```

For more intuition on spurious correlations, try http://shiny.calpoly.sh/Corr_Reg_Game/


## Spurious Causal Impacts

We apply the three major credible methods (IV, RDD, DID) to random walks. Each time, we find a result that fits mold and add various extensions that make it appear robust. One could tell a story about how $X_{2}$ affects $X_{1}$ but $X_{1}$ might also affect $X_{2}$, and how they discovered an instrument $X_{3}$ to provide the first causal estimate of $X_{2}$ on $X_{1}$. The analysis looks scientific and the story sounds plausible, so you could probably be convinced *if it were not just random noise.*



```r
n <- 1000
n_index <- seq(n)

set.seed(1)
random_walk1 <- cumsum(runif(n,-1,1))

set.seed(2)
random_walk2 <- cumsum(runif(n,-1,1))

par(mfrow=c(1,2))
plot(random_walk1, pch=16, col=rgb(1,0,0,.25),
    xlab='Time', ylab='Random Value')
plot(random_walk2, pch=16, col=rgb(0,0,1,.25),
    xlab='Time', ylab='Random Value')
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-65-1.png" width="672" />


**IV**
First, find an instrument that satisfy various statistical criterion to provide a causal estimate of $X_{2}$ on $X_{1}$.

```r
## "Find" "valid" ingredients
library(fixest)
random_walk3 <- cumsum(runif(n,-1,1))
dat_i <- data.frame(
    X1=random_walk1,
    X2=random_walk2,
    X3=random_walk3)
ivreg_i <- feols(X1~1|X2~X3, data=dat_i)
summary(ivreg_i)
```

```
## TSLS estimation, Dep. Var.: X1, Endo.: X2, Instr.: X3
## Second stage: Dep. Var.: X1
## Observations: 1,000 
## Standard-errors: IID 
##             Estimate Std. Error t value   Pr(>|t|)    
## (Intercept)  8.53309   1.644285 5.18954 2.5533e-07 ***
## fit_X2       1.79901   0.472285 3.80916 1.4796e-04 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## RMSE: 6.25733   Adj. R2: -1.29152
## F-test (1st stage), X2: stat = 10.8, p = 0.001048, on 1 and 998 DoF.
##             Wu-Hausman: stat = 23.4, p = 1.518e-6, on 1 and 997 DoF.
```

```r
## After experimenting with different instruments
## you can find even stronger results!
```


**RDD**
Second, find a large discrete change in the data that you can associate with a policy. You can use this as an instrument too, also providing a causal estimate of $X_{2}$ on $X_{1}$.



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
plot(random_walk1, pch=16, col=rgb(0,0,1,.25),
    xlim=wind1, xlab='Time', ylab='Random Value')
abline(v=n1, lty=2)
lines(reg0$model$t, reg0$fitted.values, col=1)
lines(reg1$model$t, reg1$fitted.values, col=1)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-67-1.png" width="672" />


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


**DID**
Third, find a change in the data that you can associate with a policy where the control group has parallel trends. This also provides a causal estimate of $X_{2}$ on $X_{1}$.


```r
## Find a reversal of fortune
## (A good story always goes well with a nice pre-trend)
n2 <- 318
wind2 <- c(n2-20,n2+20)
plot(random_walk2, pch=16, col=rgb(0,0,1,.5),
    xlim=wind2, ylim=c(-15,15), xlab='Time', ylab='Random Value')
points(random_walk1, pch=16, col=rgb(1,0,0,.5))
abline(v=n2, lty=2)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-69-1.png" width="672" />


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
## (what about the intercept?)
## (stable coefficients are the good ones?)
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

