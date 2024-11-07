# (PART) Linear Regression in R {-} 

This section is a quick overview of linear regression models from the perspective that ``all models are wrong, but some are useful''. All models are estimated via  Ordinary Least Squares (OLS). For more in-depth introductions, which typically begin by assuming the true data generating process is linear, see https://jadamso.github.io/Rbooks/ordinary-least-squares.html#more-literature. 


``` r
knitr::opts_chunk$set(echo=TRUE, message=FALSE, warning=FALSE)
```

# Bivariate Data
***

Given some data

``` r
# Bivariate Data from USArrests
xy <- USArrests[,c('Murder','UrbanPop')]
colnames(xy) <- c('y','x')
```
first inspect it, as in Part I.

``` r
# Inspect Dataset
# head(xy)
# summary(xy)
plot(y~x, xy, col=grey(.5,.5), pch=16)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-3-1.png" width="672" />

## Simple Linear Regression
Simple Linear Regression refers to fitting a linear model to bivariate data. Specifically, the model is 
$$
y_i=\alpha+\beta x_i+\epsilon_{i}
$$
and objective function is
$$
min_{\alpha, \beta} \sum_{i=1}^{n} \left( \epsilon_{i} \right)^2 =  min_{\alpha, \beta} \sum_{i=1}^{n} \left( y_i - [\alpha+\beta x_i] \right).
$$
Minimizing the squared errors yields point estimates
$$
\hat{\alpha}=\bar{y}-\hat{\beta}\bar{x} = \widehat{\mathbb{E}}[Y] - \hat{\beta} \widehat{\mathbb{E}}[X] \\
\hat{\beta}=\frac{\sum_{i}^{}(x_i-\bar{x})(y_i-\bar{y})}{\sum_{i}^{}(x_i-\bar{x})^2} = \frac{\widehat{Cov}[X,Y]}{\widehat{\mathbb{V}}[X]}
$$
and predictions
$$
\hat{y}_i=\hat{\alpha}+\hat{\beta}x_i\\
\hat{\epsilon}_i=y_i-\hat{y}_i
$$



``` r
# Estimate Regression Coefficients
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

``` r
# Point Estimates
coef(reg)
```

```
## (Intercept)           x 
##  6.41594246  0.02093466
```

To qualitatively analyze the ''Goodness of fit'', we plot our predictions.

``` r
# Plot Data and Predictions
library(plotly)
xy$ID <- rownames(USArrests)
xy$pred <- predict(reg)
xy$resid <- resid(reg)
fig <- plotly::plot_ly(
  xy, x=~x, y=~y,
  mode='markers',
  type='scatter',
  hoverinfo='text',
  marker=list(color=grey(0,.25), size=10),
  text=~paste('<b>', ID, '</b>',
              '<br>Urban  :', x,
              '<br>Murder :', y,
              '<br>Predicted Murder :', round(pred,2),
              '<br>Residual :', round(resid,2)))              
# Add Legend
fig <- plotly::layout(fig,
          showlegend=F,
          title='Crime and Urbanization in America 1975',
          xaxis = list(title='Percent of People in an Urban Area'),
          yaxis = list(title='Homicide Arrests per 100,000 People'))
# Plot Model Predictions
add_trace(fig, x=~x, y=~pred,
    inherit=F, hoverinfo='none',
    mode='lines+markers', type='scatter',
    color=I('black'),
    line=list(width=1/2),
    marker=list(symbol=134, size=5))
```

```{=html}
<div class="plotly html-widget html-fill-item" id="htmlwidget-f2da295cea093e7a3ceb" style="width:672px;height:480px;"></div>
<script type="application/json" data-for="htmlwidget-f2da295cea093e7a3ceb">{"x":{"visdat":{"cdeb4abbf5b2":["function () ","plotlyVisDat"]},"cur_data":"cdeb4abbf5b2","attrs":{"cdeb4abbf5b2":{"x":{},"y":{},"mode":"markers","hoverinfo":"text","marker":{"color":"#00000040","size":10},"text":{},"alpha_stroke":1,"sizes":[10,100],"spans":[1,20],"type":"scatter"},"cdeb4abbf5b2.1":{"x":{},"y":{},"hoverinfo":"none","mode":"lines+markers","type":"scatter","color":["black"],"line":{"width":0.5},"marker":{"symbol":134,"size":5},"inherit":false}},"layout":{"margin":{"b":40,"l":60,"t":25,"r":10},"showlegend":false,"title":"Crime and Urbanization in America 1975","xaxis":{"domain":[0,1],"automargin":true,"title":"Percent of People in an Urban Area"},"yaxis":{"domain":[0,1],"automargin":true,"title":"Homicide Arrests per 100,000 People"},"hovermode":"closest"},"source":"A","config":{"modeBarButtonsToAdd":["hoverclosest","hovercompare"],"showSendToCloud":false},"data":[{"x":[58,48,80,50,91,78,77,72,80,60,83,54,83,65,57,66,52,66,51,67,85,74,66,44,70,53,62,81,56,89,70,86,45,44,75,68,67,72,87,48,45,59,80,80,32,63,73,39,66,60],"y":[13.199999999999999,10,8.0999999999999996,8.8000000000000007,9,7.9000000000000004,3.2999999999999998,5.9000000000000004,15.4,17.399999999999999,5.2999999999999998,2.6000000000000001,10.4,7.2000000000000002,2.2000000000000002,6,9.6999999999999993,15.4,2.1000000000000001,11.300000000000001,4.4000000000000004,12.1,2.7000000000000002,16.100000000000001,9,6,4.2999999999999998,12.199999999999999,2.1000000000000001,7.4000000000000004,11.4,11.1,13,0.80000000000000004,7.2999999999999998,6.5999999999999996,4.9000000000000004,6.2999999999999998,3.3999999999999999,14.4,3.7999999999999998,13.199999999999999,12.699999999999999,3.2000000000000002,2.2000000000000002,8.5,4,5.7000000000000002,2.6000000000000001,6.7999999999999998],"mode":"markers","hoverinfo":["text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text"],"marker":{"color":"#00000040","size":10,"line":{"color":"rgba(31,119,180,1)"}},"text":["<b> Alabama <\/b> <br>Urban  : 58 <br>Murder : 13.2 <br>Predicted Murder : 7.63 <br>Residual : 5.57","<b> Alaska <\/b> <br>Urban  : 48 <br>Murder : 10 <br>Predicted Murder : 7.42 <br>Residual : 2.58","<b> Arizona <\/b> <br>Urban  : 80 <br>Murder : 8.1 <br>Predicted Murder : 8.09 <br>Residual : 0.01","<b> Arkansas <\/b> <br>Urban  : 50 <br>Murder : 8.8 <br>Predicted Murder : 7.46 <br>Residual : 1.34","<b> California <\/b> <br>Urban  : 91 <br>Murder : 9 <br>Predicted Murder : 8.32 <br>Residual : 0.68","<b> Colorado <\/b> <br>Urban  : 78 <br>Murder : 7.9 <br>Predicted Murder : 8.05 <br>Residual : -0.15","<b> Connecticut <\/b> <br>Urban  : 77 <br>Murder : 3.3 <br>Predicted Murder : 8.03 <br>Residual : -4.73","<b> Delaware <\/b> <br>Urban  : 72 <br>Murder : 5.9 <br>Predicted Murder : 7.92 <br>Residual : -2.02","<b> Florida <\/b> <br>Urban  : 80 <br>Murder : 15.4 <br>Predicted Murder : 8.09 <br>Residual : 7.31","<b> Georgia <\/b> <br>Urban  : 60 <br>Murder : 17.4 <br>Predicted Murder : 7.67 <br>Residual : 9.73","<b> Hawaii <\/b> <br>Urban  : 83 <br>Murder : 5.3 <br>Predicted Murder : 8.15 <br>Residual : -2.85","<b> Idaho <\/b> <br>Urban  : 54 <br>Murder : 2.6 <br>Predicted Murder : 7.55 <br>Residual : -4.95","<b> Illinois <\/b> <br>Urban  : 83 <br>Murder : 10.4 <br>Predicted Murder : 8.15 <br>Residual : 2.25","<b> Indiana <\/b> <br>Urban  : 65 <br>Murder : 7.2 <br>Predicted Murder : 7.78 <br>Residual : -0.58","<b> Iowa <\/b> <br>Urban  : 57 <br>Murder : 2.2 <br>Predicted Murder : 7.61 <br>Residual : -5.41","<b> Kansas <\/b> <br>Urban  : 66 <br>Murder : 6 <br>Predicted Murder : 7.8 <br>Residual : -1.8","<b> Kentucky <\/b> <br>Urban  : 52 <br>Murder : 9.7 <br>Predicted Murder : 7.5 <br>Residual : 2.2","<b> Louisiana <\/b> <br>Urban  : 66 <br>Murder : 15.4 <br>Predicted Murder : 7.8 <br>Residual : 7.6","<b> Maine <\/b> <br>Urban  : 51 <br>Murder : 2.1 <br>Predicted Murder : 7.48 <br>Residual : -5.38","<b> Maryland <\/b> <br>Urban  : 67 <br>Murder : 11.3 <br>Predicted Murder : 7.82 <br>Residual : 3.48","<b> Massachusetts <\/b> <br>Urban  : 85 <br>Murder : 4.4 <br>Predicted Murder : 8.2 <br>Residual : -3.8","<b> Michigan <\/b> <br>Urban  : 74 <br>Murder : 12.1 <br>Predicted Murder : 7.97 <br>Residual : 4.13","<b> Minnesota <\/b> <br>Urban  : 66 <br>Murder : 2.7 <br>Predicted Murder : 7.8 <br>Residual : -5.1","<b> Mississippi <\/b> <br>Urban  : 44 <br>Murder : 16.1 <br>Predicted Murder : 7.34 <br>Residual : 8.76","<b> Missouri <\/b> <br>Urban  : 70 <br>Murder : 9 <br>Predicted Murder : 7.88 <br>Residual : 1.12","<b> Montana <\/b> <br>Urban  : 53 <br>Murder : 6 <br>Predicted Murder : 7.53 <br>Residual : -1.53","<b> Nebraska <\/b> <br>Urban  : 62 <br>Murder : 4.3 <br>Predicted Murder : 7.71 <br>Residual : -3.41","<b> Nevada <\/b> <br>Urban  : 81 <br>Murder : 12.2 <br>Predicted Murder : 8.11 <br>Residual : 4.09","<b> New Hampshire <\/b> <br>Urban  : 56 <br>Murder : 2.1 <br>Predicted Murder : 7.59 <br>Residual : -5.49","<b> New Jersey <\/b> <br>Urban  : 89 <br>Murder : 7.4 <br>Predicted Murder : 8.28 <br>Residual : -0.88","<b> New Mexico <\/b> <br>Urban  : 70 <br>Murder : 11.4 <br>Predicted Murder : 7.88 <br>Residual : 3.52","<b> New York <\/b> <br>Urban  : 86 <br>Murder : 11.1 <br>Predicted Murder : 8.22 <br>Residual : 2.88","<b> North Carolina <\/b> <br>Urban  : 45 <br>Murder : 13 <br>Predicted Murder : 7.36 <br>Residual : 5.64","<b> North Dakota <\/b> <br>Urban  : 44 <br>Murder : 0.8 <br>Predicted Murder : 7.34 <br>Residual : -6.54","<b> Ohio <\/b> <br>Urban  : 75 <br>Murder : 7.3 <br>Predicted Murder : 7.99 <br>Residual : -0.69","<b> Oklahoma <\/b> <br>Urban  : 68 <br>Murder : 6.6 <br>Predicted Murder : 7.84 <br>Residual : -1.24","<b> Oregon <\/b> <br>Urban  : 67 <br>Murder : 4.9 <br>Predicted Murder : 7.82 <br>Residual : -2.92","<b> Pennsylvania <\/b> <br>Urban  : 72 <br>Murder : 6.3 <br>Predicted Murder : 7.92 <br>Residual : -1.62","<b> Rhode Island <\/b> <br>Urban  : 87 <br>Murder : 3.4 <br>Predicted Murder : 8.24 <br>Residual : -4.84","<b> South Carolina <\/b> <br>Urban  : 48 <br>Murder : 14.4 <br>Predicted Murder : 7.42 <br>Residual : 6.98","<b> South Dakota <\/b> <br>Urban  : 45 <br>Murder : 3.8 <br>Predicted Murder : 7.36 <br>Residual : -3.56","<b> Tennessee <\/b> <br>Urban  : 59 <br>Murder : 13.2 <br>Predicted Murder : 7.65 <br>Residual : 5.55","<b> Texas <\/b> <br>Urban  : 80 <br>Murder : 12.7 <br>Predicted Murder : 8.09 <br>Residual : 4.61","<b> Utah <\/b> <br>Urban  : 80 <br>Murder : 3.2 <br>Predicted Murder : 8.09 <br>Residual : -4.89","<b> Vermont <\/b> <br>Urban  : 32 <br>Murder : 2.2 <br>Predicted Murder : 7.09 <br>Residual : -4.89","<b> Virginia <\/b> <br>Urban  : 63 <br>Murder : 8.5 <br>Predicted Murder : 7.73 <br>Residual : 0.77","<b> Washington <\/b> <br>Urban  : 73 <br>Murder : 4 <br>Predicted Murder : 7.94 <br>Residual : -3.94","<b> West Virginia <\/b> <br>Urban  : 39 <br>Murder : 5.7 <br>Predicted Murder : 7.23 <br>Residual : -1.53","<b> Wisconsin <\/b> <br>Urban  : 66 <br>Murder : 2.6 <br>Predicted Murder : 7.8 <br>Residual : -5.2","<b> Wyoming <\/b> <br>Urban  : 60 <br>Murder : 6.8 <br>Predicted Murder : 7.67 <br>Residual : -0.87"],"type":"scatter","error_y":{"color":"rgba(31,119,180,1)"},"error_x":{"color":"rgba(31,119,180,1)"},"line":{"color":"rgba(31,119,180,1)"},"xaxis":"x","yaxis":"y","frame":null},{"x":[58,48,80,50,91,78,77,72,80,60,83,54,83,65,57,66,52,66,51,67,85,74,66,44,70,53,62,81,56,89,70,86,45,44,75,68,67,72,87,48,45,59,80,80,32,63,73,39,66,60],"y":[7.630152672499273,7.4208060843020238,8.0907151665332222,7.4626754019414738,8.3209964135501959,8.0488458488937713,8.0279111900740467,7.9232378959754222,8.0907151665332222,7.672021990138723,8.1535191429923959,7.546414037220373,8.1535191429923959,7.7766952842373476,7.6092180136795484,7.7976299430570721,7.5045447195809238,7.7976299430570721,7.4836100607611984,7.8185646018767976,8.1953884606318468,7.9651072136148722,7.7976299430570721,7.3370674490231238,7.8813685783359722,7.5254793784006484,7.713891307778173,8.1116498253529468,7.588283354859823,8.279127095910745,7.8813685783359722,8.2163231194515713,7.3580021078428492,7.3370674490231238,7.9860418724345967,7.8394992606965221,7.8185646018767976,7.9232378959754222,8.2372577782712959,7.4208060843020238,7.3580021078428492,7.6510873313189975,8.0907151665332222,8.0907151665332222,7.0858515431864246,7.7348259665978976,7.9441725547951467,7.2323941549244992,7.7976299430570721,7.672021990138723],"hoverinfo":["none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none"],"mode":"lines+markers","type":"scatter","line":{"color":"rgba(0,0,0,1)","width":0.5},"marker":{"color":"rgba(0,0,0,1)","symbol":134,"size":5,"line":{"color":"rgba(0,0,0,1)"}},"textfont":{"color":"rgba(0,0,0,1)"},"error_y":{"color":"rgba(0,0,0,1)"},"error_x":{"color":"rgba(0,0,0,1)"},"xaxis":"x","yaxis":"y","frame":null}],"highlight":{"on":"plotly_click","persistent":false,"dynamic":false,"selectize":false,"opacityDim":0.20000000000000001,"selected":{"opacity":1},"debounce":0},"shinyEvents":["plotly_hover","plotly_click","plotly_selected","plotly_relayout","plotly_brushed","plotly_brushing","plotly_clickannotation","plotly_doubleclick","plotly_deselect","plotly_afterplot","plotly_sunburstclick"],"base_url":"https://plot.ly"},"evals":[],"jsHooks":[]}</script>
```
To quantitatively analyze GoF, we compute $R^2$ using the sums of squared errors (Total, Explained, and Residual)
$$
\underbrace{\sum_{i}(y_i-\bar{y})^2}_\text{TSS}=\underbrace{\sum_{i}(\hat{y}_i-\bar{y})^2}_\text{ESS}+\underbrace{\sum_{i}\hat{\epsilon_{i}}^2}_\text{RSS}\\
R^2 = \frac{ESS}{TSS}=1-\frac{RSS}{TSS}
$$
Note that $R^2$ is also called the coefficient of determination.

``` r
# Manually Compute Goodness of Fit
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

``` r
# Check R2
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

Note that values reported by your computer do not necessarily satisfy this definition. To calculate these statistics, we will estimate variability using *data-driven* methods. (For some theoretical background, see, e.g., https://www.sagepub.com/sites/default/files/upm-binaries/21122_Chapter_21.pdf.)


We first consider the simplest, the jackknife. In this procedure, we loop through each row of the dataset. And, in each iteration of the loop, we drop that observation from the dataset and reestimate the statistic of interest. We then calculate the standard deviation of the statistic across all ``subsamples''.


``` r
# Jackknife Standard Errors for OLS Coefficient
jack_regs <- lapply(1:nrow(xy), function(i){
    xy_i <- xy[-i,]
    reg_i <- lm(y~x, dat=xy_i)
})
jack_coefs <- sapply(jack_regs, coef)['x',]
jack_se <- sd(jack_coefs)
# classic_se <- sqrt(diag(vcov(reg)))[['x']]


# Jackknife Sampling Distribution
hist(jack_coefs, breaks=25,
    main=paste0('SE est. = ', round(jack_se,4)),
    font.main=1, border=NA,
    xlab=expression(beta[-i]))
# Original Estimate
abline(v=coef(reg)['x'], lwd=2)
# Jackknife Confidence Intervals
jack_ci_percentile <- quantile(jack_coefs, probs=c(.025,.975))
abline(v=jack_ci_percentile, lty=2)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-7-1.png" width="672" />

``` r
# Plot Normal Approximation
# jack_ci_normal <- jack_mean+c(-1.96, +1.96)*jack_se
# abline(v=jack_ci_normal, col="red", lty=3)
```

There are several resampling techniques. The other main one is the bootstrap, which resamples with *replacement* for an *arbitrary* number of iterations. When bootstrapping a dataset with $n$ observations, you randomly resample all $n$ rows in your data set $B$ times. Random subsampling is one of many hybrid approaches that tries to combine the best of both worlds.

| | Sample Size per Iteration | Number of Iterations | Resample |
| -------- | ------- | ------- | ------- |
Bootstrap | $n$     | $B$  | With Replacement |
Jackknife | $n-1$   | $n$  | Without Replacement |
Random Subsample | $m < n$ | $B$  | Without Replacement |


``` r
# Bootstrap
boot_regs <- lapply(1:399, function(b){
    b_id <- sample( nrow(xy), replace=T)
    xy_b <- xy[b_id,]
    reg_b <- lm(y~x, dat=xy_b)
})
boot_coefs <- sapply(boot_regs, coef)['x',]
boot_se <- sd(boot_coefs)

hist(boot_coefs, breaks=25,
    main=paste0('SE est. = ', round(boot_se,4)),
    font.main=1, border=NA,
    xlab=expression(beta[b]))
boot_ci_percentile <- quantile(boot_coefs, probs=c(.025,.975))
abline(v=boot_ci_percentile, lty=2)
abline(v=coef(reg)['x'], lwd=2)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-8-1.png" width="672" />


``` r
# Random Subsamples
rs_regs <- lapply(1:399, function(b){
    b_id <- sample( nrow(xy), nrow(xy)-10, replace=F)
    xy_b <- xy[b_id,]
    reg_b <- lm(y~x, dat=xy_b)
})
rs_coefs <- sapply(rs_regs, coef)['x',]
rs_se <- sd(rs_coefs)

hist(rs_coefs, breaks=25,
    main=paste0('SE est. = ', round(rs_se,4)),
    font.main=1, border=NA,
    xlab=expression(beta[b]))
abline(v=coef(reg)['x'], lwd=2)
rs_ci_percentile <- quantile(rs_coefs, probs=c(.025,.975))
abline(v=rs_ci_percentile, lty=2)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-9-1.png" width="672" />

We can also bootstrap other statistics, such as a t-statistic or $R^2$. We do such things to test a null hypothesis, which is often ``no relationship''. We are rarely interested in computing standard errors and conducting hypothesis tests for two variables. However, we work through the ideas in the two-variable case to better understand the multi-variable case.

## Hypothesis Tests

There are two main ways to conduct a hypothesis test. We do this using *data-driven* methods that assume much less about the data generating process.

**Invert a CI**
One main way to conduct hypothesis tests is to examine whether a confidence interval contains a hypothesized value. Does the slope coefficient equal $0$? For reasons we won't go into in this class, we typically normalize the coefficient by its standard error: $$ \hat{t} = \frac{\hat{\beta}}{\hat{\sigma}_{\hat{\beta}}} $$

``` r
tvalue <- coef(reg)['x']/jack_se

jack_t <- sapply(jack_regs, function(reg_b){
    # Data
    xy_b <- reg_b$model
    # Coefficient
    beta_b <- coef(reg_b)[['x']]
    t_hat_b <- beta_b/jack_se
    return(t_hat_b)
})

hist(jack_t, breaks=25,
    main='Jackknife t Density',
    font.main=1, border=NA,
    xlab=expression(hat(t)[b]), 
    xlim=range(c(0, jack_t)) )
abline(v=quantile(jack_t, probs=c(.025,.975)), lty=2)
abline(v=0, col="red", lwd=2)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-10-1.png" width="672" />

**Impose the Null**
We can also compute a null distribution. We focus on the simplest, the bootstrap, where loop through a large number of simulations. In each iteration of the loop, we drop impose the null hypothesis and reestimate the statistic of interest. We then calculate the standard deviation of the statistic across all ``resamples''. Specifically, we compute the distribution of t-values on data with randomly reshuffled outcomes (imposing the null), and compare how extreme the observed value is.

``` r
# Null Distribution for Beta
boot_t0 <- sapply( 1:399, function(b){
    xy_b <- xy
    xy_b$y <- sample( xy_b$y, replace=T)
    reg_b <- lm(y~x, dat=xy_b)
    beta_b <- coef(reg_b)[['x']]
    t_hat_b <- beta_b/jack_se
    return(t_hat_b)
})

# Null Bootstrap Distribution
boot_ci_percentile0 <- quantile(boot_t0, probs=c(.025,.975))
hist(boot_t0, breaks=25,
    main='Null Bootstrap Density',
    font.main=1, border=NA,
    xlab=expression(hat(t)[b]),
    xlim=range(boot_t0))
abline(v=boot_ci_percentile0, lty=2)
abline(v=tvalue, col="red", lwd=2)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-11-1.png" width="672" />

Alternatively, you can impose the null by recentering the sampling distribution around the theoretical value; $$ \hat{t} = \frac{\hat{\beta} - \beta_{0} }{\hat{\sigma}_{\hat{\beta}}} $$. Under some assumptions, the null distribution is t-distributed; $\sim t_{n-2}$. (For more on parametric t-testing based on statistical theory, see https://www.econometrics-with-r.org/4-lrwor.html.)


In any case, we can calculate a *p-value*: the probability you would see something as extreme as your statistic under the null (assuming your null hypothesis was true). We can always calculate a p-value from an explicit null distribution.

``` r
# One Sided Test for P(t > boot_t | Null)=1- P(t < boot_t | Null)
That_NullDist1 <- ecdf(boot_t0)
Phat1  <- 1-That_NullDist1(jack_t)

# Two Sided Test for P(t > jack_t or  t < -jack_t | Null)
That_NullDist2 <- ecdf(abs(boot_t0))
plot(That_NullDist2, xlim=range(boot_t0, jack_t),
    xlab=expression( abs(hat(t)[b]) ),
    main='Null Bootstrap Distribution', font.main=1)
abline(v=tvalue, col='red')
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-12-1.png" width="672" />

``` r
Phat2  <-  1-That_NullDist2( abs(tvalue))
Phat2
```

```
## [1] 0.6090226
```


## Prediction Intervals

In addition to confidence intervals, we can also compute a *prediction interval* which estimates the range of variability across different samples for the outcomes. These intervals also take into account the residuals--- the variability of individuals around the mean. 



``` r
# Bootstrap Prediction Interval
boot_resids <- lapply(boot_regs, function(reg_b){
    e_b <- resid(reg_b)
    x_b <- reg_b$model$x
    res_b <- cbind(e_b, x_b)
})
boot_resids <- as.data.frame(do.call(rbind, boot_resids))
# Homoskedastic
ehat <- quantile(boot_resids$e_b, probs=c(.025, .975))
x <- quantile(xy$x,probs=seq(0,1,by=.1))
boot_pi <- coef(reg)[1] + x*coef(reg)['x']
boot_pi <- cbind(boot_pi + ehat[1], boot_pi + ehat[2])

# Plot Bootstrap PI
plot(y~x, dat=xy, pch=16, main='Prediction Intervals',
    ylim=c(-5,20), font.main=1)
polygon( c(x, rev(x)), c(boot_pi[,1], rev(boot_pi[,2])),
    col=grey(0,.2), border=NA)

# Parametric PI (For Comparison)
pi <- predict(reg, interval='prediction', newdata=data.frame(x))
lines( x, pi[,'lwr'], lty=2)
lines( x, pi[,'upr'], lty=2)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-13-1.png" width="672" />


For a nice overview of different types of intervals, see https://www.jstor.org/stable/2685212. For an in-depth view, see "Statistical Intervals: A Guide for Practitioners and Researchers" or "Statistical Tolerance Regions: Theory, Applications, and Computation". See https://robjhyndman.com/hyndsight/intervals/ for constructing intervals for future observations in a time-series context. See Davison and Hinkley, chapters 5 and 6 (also Efron and Tibshirani, or Wehrens et al.)


## Locally Linear

Segmented/piecewise regressions

``` r
# Globally Linear
reg <- lm(y~x, data=xy)

# Diagnose Fit
#plot( fitted(reg), resid(reg), pch=16, col=grey(0,.5))
#plot( xy$x, resid(reg), pch=16, col=grey(0,.5))

# Linear in 2 Pieces (subsets)
xcut2 <- cut(xy$x,2)
xy_list2 <- split(xy, xcut2)
regs2 <- lapply(xy_list2, function(xy_s){
    lm(y~x, data=xy_s)
})
sapply(regs2, coef)
```

```
##             (31.9,61.5] (61.5,91.1]
## (Intercept)  -0.2836303  4.15337509
## x             0.1628157  0.04760783
```

``` r
# Linear in 3 Pieces (subsets or bins)
xcut3 <- cut(xy$x, seq(32,92,by=20)) # Finer Bins
xy_list3 <- split(xy, xcut3)
regs3 <- lapply(xy_list3, function(xy_s){
    lm(y~x, data=xy_s)
})
sapply(regs3, coef)
```

```
##                (32,52]    (52,72]      (72,92]
## (Intercept) 4.60313390 2.36291848  8.653829140
## x           0.08233618 0.08132841 -0.007174454
```

Compare Predictions

``` r
pred1 <- data.frame(yhat=predict(reg), x=reg$model$x)
pred1 <- pred1[order(pred1$x),]

pred2 <- lapply(regs2, function(reg){
    data.frame(yhat=predict(reg), x=reg$model$x)
})
pred2 <- do.call(rbind,pred2)
pred2 <- pred2[order(pred2$x),]

pred3 <- lapply(regs3, function(reg){
    data.frame(yhat=predict(reg), x=reg$model$x)
})
pred3 <- do.call(rbind,pred3)
pred3 <- pred3[order(pred3$x),]

# Compare Predictions
plot(y ~ x, pch=16, col=grey(0,.5), dat=xy)
lines(yhat~x, pred1, lwd=2, col=2)
lines(yhat~x, pred2, lwd=2, col=4)
lines(yhat~x, pred3, lwd=2, col=3)
legend('topleft',
    legend=c('Globally Linear', 'Peicewise Linear (2)','Peicewise Linear (3)'),
    lty=1, col=c(2,4,3), cex=.8)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-15-1.png" width="672" />


Local linear regressions conduct a linear regresssion for each data point using a subsample of data around it. 

``` r
# ``Naive" Smoother
pred_fun <- function(x0, h, xy){
    # Assign equal weight to observations within h distance to x0
    # 0 weight for all other observations
    ki   <- dunif(xy$x, x0-h, x0+h) 
    llls <- lm(y~x, data=xy, weights=ki)
    yhat_i <- predict(llls, newdata=data.frame(x=x0))
}

X0 <- sort(unique(xy$x))
pred_lo1 <- sapply(X0, pred_fun, h=2, xy=xy)
pred_lo2 <- sapply(X0, pred_fun, h=20, xy=xy)

plot(y~x, pch=16, data=xy, col=grey(.5,.5),
    ylab='Murder Rate', xlab='Population Density')
cols <- c(rgb(.8,0,0,.5), rgb(0,0,.8,.5))
lines(X0, pred_lo1, col=cols[1], lwd=1, type='o')
lines(X0, pred_lo2, col=cols[2], lwd=1, type='o')
legend('topleft', title='Locally Linear',
    legend=c('h=2 ', 'h=20'),
    lty=1, col=cols, cex=.8)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-16-1.png" width="672" />
See https://shinyserv.es/shiny/kreg/ for a nice illustration. Also note that you can use adaptive bandwidths to have a similar number of data points in each subsample (especially useful when $X$ is not uniform.)


``` r
# Adaptive-width subsamples with non-uniform weights
xy0 <- xy[order(xy$x),]
plot(y~x, pch=16, col=grey(0,.5), dat=xy0)

reg_lo4 <- loess(y~x, data=xy0, span=.4)
reg_lo8 <- loess(y~x, data=xy0, span=.8)

cols <- hcl.colors(3,alpha=.75)[-3]
lines(xy0$x, predict(reg_lo4),
    col=cols[1], type='o', pch=2)
lines(xy0$x, predict(reg_lo8),
    col=cols[2], type='o', pch=2)

legend('topleft', title='Loess',
    legend=c('span=.4 ', 'span=.8'),
    lty=1, col=cols, cex=.8)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-17-1.png" width="672" />

The smoothed predicted values estimate the local means. So we can also construct confidence bands

``` r
# Loess
xy0 <- xy[order(xy$x),]
X0 <- unique(xy0$x)
reg_lo <- loess(y~x, data=xy0, span=.8)

# Jackknife CI
jack_lo <- sapply(1:nrow(xy), function(i){
    xy_i <- xy[-i,]
    reg_i <- loess(y~x, dat=xy_i, span=.8)
    predict(reg_i, newdata=data.frame(x=X0))
})
jack_cb <- apply(jack_lo,1, quantile,
    probs=c(.025,.975), na.rm=T)

# Plot
plot(y~x, pch=16, col=grey(0,.5), dat=xy0)
preds_lo <- predict(reg_lo, newdata=data.frame(x=X0))
lines(X0, preds_lo,
    col=hcl.colors(3,alpha=.75)[2],
    type='o', pch=2)
# Plot CI
polygon(
    c(X0, rev(X0)),
    c(jack_cb[1,], rev(jack_cb[2,])),
    col=hcl.colors(3,alpha=.25)[2],
    border=NA)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-18-1.png" width="672" />


You can also construct prediction bands

``` r
plot(y~x, pch=16, col=grey(0,.5),
    dat=xy0, ylim=c(0, 20))
lines(X0, preds_lo,
    col=hcl.colors(3,alpha=.75)[2],
    type='o', pch=2)

# Estimate Residuals CI at design points
res_lo <- sapply(1:nrow(xy), function(i){
    y_i <- xy[i,'y']
    preds_i <- jack_lo[,i]
    resids_i <- y_i - preds_i
})
res_cb <- apply(res_lo, 1, quantile,
    probs=c(.025,.975), na.rm=T)

# Plot
lines( X0, preds_lo +res_cb[1,],
    col=hcl.colors(3,alpha=.75)[2], lt=2)
lines( X0, preds_lo +res_cb[2,],
    col=hcl.colors(3,alpha=.75)[2], lty=2)



# Smooth estimates 
res_lo <- lapply(1:nrow(xy), function(i){
    y_i <- xy[i,'y']
    x_i <- xy[i,'x']
    preds_i <- jack_lo[,i]
    resids_i <- y_i - preds_i
    cbind(e=resids_i, x=x_i)
})
res_lo <- as.data.frame(do.call(rbind, res_lo))

res_fun <- function(x0, h, res_lo){
    # Assign equal weight to observations within h distance to x0
    # 0 weight for all other observations
    ki <- dunif(res_lo$x, x0-h, x0+h) 
    ei <- res_lo[ki!=0,'e']
    res_i <- quantile(ei, probs=c(.025,.975), na.rm=T)
}
X0 <- sort(unique(xy$x))
res_lo2 <- sapply(X0, res_fun, h=15, res_lo=res_lo)

lines( X0, preds_lo +res_lo2[1,],
    col=hcl.colors(3,alpha=.75)[2], lty=1, lwd=2)
lines( X0, preds_lo +res_lo2[2,],
    col=hcl.colors(3,alpha=.75)[2], lty=1, lwd=2)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-19-1.png" width="672" />


# Multivariate Data
***

Given a dataset, you can summarize it using the previous tools.


``` r
# Inspect Dataset on police arrests for the USA in 1973
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

``` r
library(psych)
pairs.panels( USArrests[,c('Murder','Assault','UrbanPop')],
    hist.col=grey(0,.25), breaks=30, density=F, hist.border=NA, # Diagonal
    ellipses=F, rug=F, smoother=F, pch=16, col=grey(0,.5) # Lower Triangle
    )
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-20-1.png" width="672" />


## Multiple Linear Regression
Model and objective
$$
y_i=\beta_0+\beta_1x_{i1}+\beta_2x_{i2}+\ldots+\beta_kx_{ik}+\epsilon_i = X_{i}\beta +\epsilon_i \\
min_{\beta} \sum_{i=1}^{n} (\epsilon_i)^2
$$
Letting $y$ denote the vector $[y_{1},...y_{N}]$, we can also write the model and objective in matrix form
$$
y=\textbf{X}\beta+\epsilon\\
min_{\beta} (\epsilon' \epsilon)
$$

Minimizing the squared errors yields point estimates yields point estimates 
$$
\hat{\beta}=(\textbf{X}'\textbf{X})^{-1}\textbf{X}'y
$$
and predictions 
$$
\hat{y}=\textbf{X} \hat{\beta} \\
\hat{\epsilon}=y - \hat{y} \\
$$


``` r
# Manually Compute
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

``` r
# Check
reg <- lm(Murder~Assault+UrbanPop, data=USArrests)
coef(reg)
```

```
## (Intercept)     Assault    UrbanPop 
##  3.20715340  0.04390995 -0.04451047
```

To measure the ``Goodness of fit'' of the model, we can again plot our predictions

``` r
plot(USArrests$Murder, predict(reg), pch=16, col=grey(0,.5))
abline(a=0,b=1, lty=2)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-22-1.png" width="672" />
and compute sums of squared errors. Adding random data may sometimes improve the fit, however, so we adjust the $R^2$ by the number of covariates $K$.
$$
R^2 = \frac{ESS}{TSS}=1-\frac{RSS}{TSS}\\
R^2_{\text{adj.}} = 1-\frac{n-1}{n-K}(1-R^2)
$$


``` r
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

<img src="03-ROLS_files/figure-html/unnamed-chunk-23-1.png" width="672" />


## Variability and Hypothesis Tests

To estimate the variability of our estimates, we can use the same *data-driven* methods introduced in the last section.


``` r
# Bootstrap SE's
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
As before, we can conduct independent hypothesis tests using t-values. We can also conduct joint tests, such as whether two coefficients are equal, by looking at the their joint distribution.

``` r
boot_coef_df <- as.data.frame(cbind(ID=boots, t(boot_coefs)))
fig <- plotly::plot_ly(boot_coef_df,
    type = 'scatter', mode = 'markers',
    x = ~UrbanPop, y = ~Assault,
    text = ~paste('<b> bootstrap dataset: ', ID, '</b>',
            '<br>Coef. Urban  :', round(UrbanPop,3),
            '<br>Coef. Murder :', round(Assault,3),
            '<br>Coef. Intercept :', round(`(Intercept)`,3)),
    hoverinfo='text',
    showlegend=F,
    marker=list( color='rgba(0, 0, 0, 0.5)'))
fig <- plotly::layout(fig,
    showlegend=F,
    title='Joint Distribution of Coefficients',
    xaxis = list(title='UrbanPop Coefficient'),
    yaxis = list(title='Assualt Coefficient'))
fig
```

```{=html}
<div class="plotly html-widget html-fill-item" id="htmlwidget-1b0b56eb38915e2c9bb2" style="width:672px;height:480px;"></div>
<script type="application/json" data-for="htmlwidget-1b0b56eb38915e2c9bb2">{"x":{"visdat":{"cdeb7bff346b":["function () ","plotlyVisDat"]},"cur_data":"cdeb7bff346b","attrs":{"cdeb7bff346b":{"mode":"markers","x":{},"y":{},"text":{},"hoverinfo":"text","showlegend":false,"marker":{"color":"rgba(0, 0, 0, 0.5)"},"alpha_stroke":1,"sizes":[10,100],"spans":[1,20],"type":"scatter"}},"layout":{"margin":{"b":40,"l":60,"t":25,"r":10},"showlegend":false,"title":"Joint Distribution of Coefficients","xaxis":{"domain":[0,1],"automargin":true,"title":"UrbanPop Coefficient"},"yaxis":{"domain":[0,1],"automargin":true,"title":"Assualt Coefficient"},"hovermode":"closest"},"source":"A","config":{"modeBarButtonsToAdd":["hoverclosest","hovercompare"],"showSendToCloud":false},"data":[{"mode":"markers","x":[-0.039374562695332398,-0.04904825586642101,0.017882730873385214,-0.074767228767679217,-0.022949350689868565,-0.038724075045680158,-0.001472217406553576,-0.059427861980064625,-0.032051729854757578,-0.032867865668951946,-0.026725955699225493,-0.053156513020024894,-0.020499763610913491,-0.047136994747207166,-0.059188093000670419,-0.014531319447266456,-0.044301676673078785,-0.033454974746757848,-0.031491878549334731,-0.073184720588670552,-0.012368063512436203,-0.067422122931917849,-0.040744267354927088,-0.074632494765671575,-0.012739525656397393,-0.035765430968445727,-0.03812133404905358,-0.044149482132981199,-0.043112066030037116,-0.006386970356542644,-0.020702119587388657,-0.03028591365047778,-0.035289493074751828,-0.030710984109053357,-0.069100760280966567,-0.054508224585217514,-0.030274256083650478,-0.038816259197534002,-0.081080763433135652,-0.096917196711685263,-0.071116870986120073,-0.014266441725445618,-0.041132908088150948,-0.023781484421227198,-0.051963883139152824,-0.069432503366293086,-0.061674788494233593,-0.055232951562058291,-0.069085965841388805,-0.025920063174718296,-0.027245848127306026,-0.060819891490860339,0.0059123081945991517,-0.079154859644272837,-0.085951923906203972,-0.021521316456513916,-0.029138818836442971,-0.052111193706626813,-0.044129040598764109,-0.035691148176874771,-0.09301217125978227,-0.068959075422280913,-0.049508943856899842,-0.0068740242801018743,-0.054313783216367963,-0.05302213809148594,-0.074175926881684048,-0.030888701524740197,-0.006400076737286293,-0.10483554357796231,-0.016098412645789349,-0.068201902925866642,-0.051351720491813947,-0.084828441260757156,-0.025967049876757922,-0.07277802340015295,-0.018096885059668385,-0.06009391197807349,-0.028572555435058756,-0.062052475094709861,-0.0014685771841099924,-0.056543813291264691,-0.03363277983459971,-0.038185601457187135,-0.056511886590298183,-0.077244302266213288,-0.03950202467783287,-0.020259922411323066,-0.022606969685906673,-0.097347961197511337,-0.057574002397079146,-0.054369500494593263,-0.054518656517670398,-0.020500597248645953,-0.041761364859141198,-0.057383919053847571,-0.029746053154424027,-0.023739268748847936,-0.04553458597315365,-0.055851471903644583,-0.0019628144599925972,-0.059331535079036671,-0.026135124007615296,-0.049003347671964688,-0.073591753549864691,-0.053261148553955723,-0.0094555921554970602,-0.025355387436422728,-0.038224886947831133,-0.088400309439574443,-0.090785148639576041,-0.071802216998179208,-0.030435342765232968,-0.049978883967007531,-0.032950775843559543,-0.073369302352694968,-0.057634516888955746,-0.039100510635100567,-0.055899067290346903,-0.036051737462004178,-0.069448051634323382,-0.054913479572820514,-0.03859265817095673,-0.031004723169754275,-0.0093980635461211048,-0.025702791016664901,-0.085723806059532198,-0.041597045973520874,-0.028771002318599928,-0.025677797862926233,-0.04499103937483577,-0.070454203317139474,-0.0019510719420162174,-0.065690546868079638,-0.06632810084307976,-0.056634694895955642,-0.035893126774595115,-0.073048553448414544,-0.061387069454163168,-0.11311686442861564,0.0099274094354628115,-0.053914974451664793,-0.05922726422654663,-0.065320851804591309,-0.057746480322607416,-0.030201005093395138,-0.017638521644507375,-0.040032208734543898,-0.027141535652039729,-0.035683727747196504,-0.084705185754865325,-0.029223335442461668,-0.096096035866166801,-0.068441600686076298,-0.055625564266772877,-0.035464234280385643,-0.041730068386432367,-0.046920026206236511,-0.061494751385640978,-0.038028381589958818,-0.049786524223731338,-0.080806095521346058,-0.00029450905871022736,-0.063122499131938944,-0.031857895801378419,-0.024209204066546676,-0.072901106456623677,-0.085460381361677884,-0.04913304515298271,-0.029972359580206668,-0.040999287908032013,-0.04840532002651679,-0.069060065980576554,-0.03695152232978019,-0.018735763141142173,-0.030408865132473643,-0.0417204272679568,-0.03537616918928476,-0.0042039110582690357,-0.088957318960760534,-0.038847335661801742,-0.0043480654137961023,-0.036851253213727404,-0.084702415412899051,-0.036887907074582997,-0.033042167704191307,-0.065702926070243903,-0.039525603778603445,-0.012303553837021202,-0.068123319254661419,-0.029849623753563297,-0.03181966380666882,-0.034127877565776892,-0.042516035047287834,-0.013849854874163047,-0.039646654299795518,-0.044516851579575606,-0.0039468936695171699,-0.056850538527895282,-0.059878179589603772,-0.058119127411215554,-0.054709791482159306,-0.033722868733659303,-0.065427664302778368,-0.040228997819624024,-0.05407694215790948,-0.062306889482070145,-0.079266975558807989,-0.021168990274213553,-0.0099975524429685159,-0.025602100453759203,-0.038452035661552052,-0.04108275617992075,-0.034548207748015314,-0.074908237185107474,-0.044292131649276263,-0.060049456234124429,-0.055787490394088327,-0.025783615903823741,-0.072723913083808475,-0.028439062138720338,-0.054810996495001929,-0.0091334196630427494,-0.057720867411695367,-0.044527710150157558,-0.032807398186790994,-0.061408764040793457,-0.035643660538660561,-0.087493279349776243,-0.026540056879077682,-0.03428842138937295,-0.024382454272136075,-0.054666035416750206,-0.051953056639613256,-0.022884690968499235,-0.072145618055359198,-0.017012730251136185,-0.038742508199360842,-0.041012292020671498,-0.048301174834185903,-0.080085935037642775,-0.079763215337253279,-0.044034650484019486,-0.036074172748074652,-0.022405468307758632,-0.065051782816905754,-0.054919448649015608,-0.077846678608041855,-0.028623311705671357,-0.042430443022224325,-0.027519345099561724,-0.082594331751106254,-0.04502681385277061,-0.051500416638339361,0.0045491142715193833,-0.049182560564760357,-0.065426623670109749,-0.050478111370768373,-0.063148392442467491,-0.037350420344839014,-0.062897071609813712,-0.04602227016519523,-0.020698297911397615,-0.022059841480614142,-0.072366042840949815,-0.038700077837262814,-0.07370676907523023,-0.016137060529997301,-0.078972161689336545,-0.063959397706135526,-0.059116085327130662,-0.055006290533862676,-0.061164741382333722,-0.11925102366773442,-0.053840595231399536,0.016781742077745326,-0.02917895009419862,-0.056937472240085413,-0.028319949816533175,-0.052653295080140085,0.0056279838116233315,-0.060113325973109519,-0.038541373738816165,-0.031455283934229548,-0.04434763798814003,-0.04543555027293851,-0.063610405069654111,-0.082167874998341328,-0.071758226257052804,-0.063080361603324961,-0.12338959955364408,0.0062567012043690824,-0.042937191776486951,-0.054260999168659313,-0.054695017327035418,-0.068763625786788074,-0.05329599097755134,-0.015600630455241623,-0.059921479691404322,-0.0052559537557002852,-0.015462704397885859,-0.051839383499714412,-0.04660100686249783,-0.075072613715439496,-0.058844167949710577,-0.056979427008720267,-0.092323781360901497,-0.049101775661605659,-0.031293381878115818,-0.10508659424739021,-0.037070445457073796,-0.055856550095003274,-0.061343984661708963,-0.08255519407915346,-0.11744285407132413,-0.077973459775206658,-0.048366251446221038,-0.051307077780547258,-0.040701932875143093,-0.08181945594938278,-0.070911206262170443,-0.036197377233378895,-0.032909887211792041,-0.077174970440687399,-0.02948460904042826,-0.034877377561253135,-0.048394891396637198,-0.018754852299142179,-0.037369775584629956,-0.039476166562144012,-0.074329017950203025,-0.023217012358456902,-0.021858680891678039,-0.033770231200170538,-0.085967696174050812,-0.011898399773860605,-0.042516791966414551,-0.0277737849064544,-0.058845818191862839,-0.068230612354270456,-0.02217411743469171,-0.071287670399188194,-0.038136604839502465,-0.028141097327946805,0.0098334413268344658,-0.036722065253641974,-0.073442993030364806,-0.061202792598275657,-0.027277286627158649,-0.075158638272300682,-0.062634280553427651,-0.050234306260515491,-0.04639978378007277,-0.049543256318763558,-0.025402456311755733,-0.056161447502631807,-0.025261740611578595,-0.0079717627514454183,-0.037332025759472996,-0.036180948486272145,-0.043998876743216439,-0.040107336938337554,-0.037161414749385162,-0.059762956446904811,-0.034994567852509179,-0.0011602317806697854,-0.054117538365917171,-0.034896730258444184,-0.01643864643041959,-0.058111148068739404,0.019982216438112849,-0.082825709214482249,-0.05710845922665013,-0.025551120689213218,-0.083301296542779693,-0.06932418032595572,-0.038240083219308246,0.0020929861733668849,-0.091261179875100337,-0.052752314525126201,-0.028327765098153126,-0.024174723838466302,-0.069884573329160912,-0.082913144539367045,-0.042940673017895892,-0.036380989370019302,-0.060269119546944444,-0.029975691388925692,-0.06057477691390574,-0.038537931457842789,-0.046537653408649883,-0.048180387011249874,-0.014164975220977132,-0.079781618551066663,-0.05720430033729073,-0.080007985233362527,-0.043817428888565518,-0.069676503482751964,-0.032213683586120694],"y":[0.042082897810095214,0.044209415399921514,0.037865996936757594,0.04598002831578054,0.038353278861395661,0.039854721355746692,0.034396100191922761,0.048216084521616381,0.041371555683747174,0.034931990207765662,0.040848300678066128,0.041679397189539669,0.040742632397442496,0.047231606208665927,0.041091695580122212,0.038170773495546234,0.03529161842648372,0.045919605574454125,0.043108313064841842,0.051884613542109714,0.047195379963518413,0.042047181057230945,0.04215704151655842,0.046331667701718739,0.044636913785052849,0.043945164298409264,0.045917455867546225,0.042719450362916897,0.04111012139205486,0.04252984779023148,0.041859898612939671,0.046165608924817518,0.046185113308266058,0.032836049964391475,0.046682542787790736,0.039301783858882833,0.037279424338749166,0.036875657933365807,0.045253192873236821,0.038733404439512925,0.041893636914686873,0.038196786163177371,0.045654950497451961,0.040363742906893672,0.042729318383802832,0.044446054404957962,0.038696839058226386,0.047366838395021781,0.049991521103519496,0.039650374025512101,0.038711987916959088,0.047159284536173143,0.040671379001472857,0.041693951711561685,0.053682457889784319,0.044104457675658446,0.047301625481128283,0.047751123157345823,0.044765516294724784,0.040420607325814033,0.048084308069699072,0.041259438094740607,0.045379905018180532,0.040987072170425062,0.043985393087528225,0.042985677899070228,0.050508182965647748,0.041748041975910317,0.041433732900231113,0.061411162563737083,0.037306521014773726,0.045270403054767532,0.040653725597212809,0.0456731367730955,0.039594999856318987,0.039869987956542466,0.044512704321849929,0.039330305873161622,0.042447354269141438,0.043796936462894488,0.042995138587540456,0.044568401650022266,0.035664655681754337,0.044251987587193516,0.044070670882061985,0.049231099639921963,0.040784397153379566,0.044277687089402579,0.040372211485483693,0.047383811156655062,0.043176576751728132,0.04104894524485965,0.040280278543788163,0.049319081882990445,0.048468671872036621,0.036826784408583398,0.050317188423245354,0.043049876585175749,0.046904720833415368,0.043904051092773615,0.043919243769575858,0.04779226277555651,0.041971423367913117,0.048541656733682832,0.0439679084890146,0.042191044875091163,0.036269586390543965,0.042354110136083645,0.037081235006238313,0.045274764075448885,0.041770006267094623,0.037287763808683948,0.04578143377722424,0.040707219368015919,0.04485893934349415,0.047355562818620356,0.048707135756507793,0.045138521254428778,0.050183580085821508,0.045110747820680065,0.046560110022726052,0.045813091333472396,0.040679105266072102,0.04824212708277633,0.03666135708652165,0.046160394397023574,0.047897194447318228,0.048740178202467101,0.042799389326993044,0.043484330982330649,0.038654082982941519,0.040758450589152173,0.041187683218227439,0.044883688860337355,0.050013505844813413,0.052314469146693639,0.039199700672453361,0.052577250015650057,0.044106368166520603,0.050393174761491341,0.040500552594583211,0.042323613249938455,0.049844125218588345,0.049703148151184068,0.040660561551678076,0.04259977313552208,0.032109741293584952,0.044533886955318749,0.037337155623698812,0.046115310818101364,0.05179024627626351,0.048575117168231936,0.054468010655394652,0.046977501653318474,0.035927129974626687,0.044769027782128587,0.047269442436187463,0.04430936076144059,0.045463799053303888,0.041745533815479727,0.041405155781516177,0.050671400382521749,0.044404024665058231,0.044388740867658164,0.037194429823829818,0.043336609858009897,0.059420717225591724,0.043516626167890558,0.048954926675465596,0.044875132610311008,0.043640579575832984,0.048008670392284812,0.043442329167662899,0.040906662886948456,0.041324818220811528,0.038491882159182388,0.043692577336913556,0.041643084608994123,0.042672532548641867,0.047866351651995709,0.040840827476917925,0.041744376646037099,0.045221313941415951,0.057636441076223718,0.040858826809273122,0.039209436431746347,0.042187082137232997,0.042919926482949865,0.040780540527621999,0.044279699051282748,0.042894005973598243,0.046113991661546255,0.042430209700162515,0.046419791859106184,0.040988818223076942,0.050631417383722531,0.042989848643267346,0.039274250178345654,0.046367040549209849,0.044301907552980101,0.047586026796875874,0.045974479864004977,0.042782172353431722,0.033947591463947026,0.043270991012768774,0.046044691057926732,0.043585439309444252,0.043297137959177626,0.046649271913765798,0.03930428790058535,0.042176035022725905,0.044784730134148333,0.044599509085946065,0.045191430728915627,0.048185869066795818,0.048210207482272713,0.048667937841798591,0.045371343882296966,0.038759255604619659,0.045111936696050334,0.039775484084563967,0.047284984061096748,0.035030006596406434,0.048678018620981922,0.044435380378252613,0.043172214021453763,0.048090659257905365,0.041552719901836614,0.046958375886895672,0.041371713530757283,0.039552831626888767,0.048016772753675781,0.042514807003867859,0.046824353829135849,0.041378952152088491,0.044658251348543856,0.04343306562178504,0.043131699401843228,0.042055526237679795,0.041307537976132985,0.042367919947878599,0.05066603450943976,0.036968873415404453,0.040206210718304859,0.031398992198788042,0.048891811981577785,0.046184328390557826,0.03970574323310698,0.04425008352804613,0.03745919802075743,0.044273753175859493,0.051471759490420231,0.039380755891550455,0.045480204257454381,0.040516697101349884,0.042998790799544009,0.044067370481962832,0.035013492862613807,0.057101614020807184,0.04669939223921081,0.050630434864070387,0.052758182441203803,0.042360572760948359,0.045714895641438276,0.038074140344748646,0.045040211974503988,0.04641055067998423,0.042239062050969015,0.046277248623064482,0.045148515405246531,0.048274323879151343,0.031045301918665613,0.04565926645693405,0.056427693392530738,0.04616171284095584,0.040495295610999793,0.039295791885498921,0.038434409751724886,0.043023127891854238,0.043027102990211369,0.04372619214247097,0.044893024322570876,0.04353404506562835,0.046025492563565237,0.04139753213584399,0.043543811845463284,0.043624127668129412,0.052394779043883767,0.050178530351005335,0.040845188123052691,0.058252698343167951,0.043360787857871813,0.034112261997718732,0.050234742133648973,0.041579198292965185,0.041352832409097991,0.041139456680142121,0.044051905037764745,0.045127049190569049,0.045529411194531487,0.041433206479587842,0.045156907386716273,0.045997631095319604,0.047786953421589395,0.044725744627409796,0.04542189195683486,0.050979230603739781,0.040321953497579131,0.047740839184977513,0.049836088002072787,0.043275838302569515,0.040344660067658092,0.040160563004398901,0.048307333627130696,0.052034281688956366,0.044069369973267672,0.040794015760386465,0.038871352891255546,0.042734092110882554,0.043026557696715269,0.049338491611842408,0.03678954446764187,0.03916054213173998,0.047764620466428521,0.03932941753039744,0.044778539417811229,0.04254417201545295,0.040908316529070739,0.040810430049738652,0.043773055796476494,0.048895328538094085,0.049295909506026934,0.040336226629072963,0.046499758078213535,0.044862657176160031,0.035174692877060869,0.045157771017799948,0.033808958623964304,0.045117788480282438,0.042378655194029509,0.039165317180438357,0.048077398063919974,0.047198457268284255,0.040978884660069166,0.039955930171156416,0.037639700960340222,0.037659992511871229,0.046286725471859351,0.040470643080780397,0.046563845856586163,0.047271584799445855,0.043964379529440607,0.047993899206970773,0.050192098065850781,0.037694405510146509,0.042300342448046098,0.045852076479486678,0.045791723142063701,0.032865563212730903,0.0385100737374066,0.044255394420565052,0.043714023235777541,0.042494877520020131,0.047529903803213466,0.052109604336820853,0.045317677799054053,0.040374414014078673,0.040584469993194865,0.042867471523938279,0.047775100401078352,0.036680311471751048,0.041248281819035074,0.042924128857963005,0.045037582144616624,0.045041398706636253,0.045099907642916763,0.035810524189114658,0.044219595969740434,0.049761160417891991,0.050996702743940352,0.045657367239068131,0.04467862948269459,0.041474429088302879,0.046449695281920576,0.045615686222987652,0.042005152973552756,0.038799263741904448,0.042530252844312187,0.044433370814591776,0.045840978931484651,0.037801564859785121,0.039118738965858317,0.045195071072174665,0.042966455553115346,0.046234697969339662,0.043155718288105681,0.043314873378935907,0.047177070112734219,0.038646440119699171],"text":["<b> bootstrap dataset:  1 <\/b> <br>Coef. Urban  : -0.039 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 2.886","<b> bootstrap dataset:  2 <\/b> <br>Coef. Urban  : -0.049 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 3.499","<b> bootstrap dataset:  3 <\/b> <br>Coef. Urban  : 0.018 <br>Coef. Murder : 0.038 <br>Coef. Intercept : -0.077","<b> bootstrap dataset:  4 <\/b> <br>Coef. Urban  : -0.075 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 5.487","<b> bootstrap dataset:  5 <\/b> <br>Coef. Urban  : -0.023 <br>Coef. Murder : 0.038 <br>Coef. Intercept : 2.886","<b> bootstrap dataset:  6 <\/b> <br>Coef. Urban  : -0.039 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 3.173","<b> bootstrap dataset:  7 <\/b> <br>Coef. Urban  : -0.001 <br>Coef. Murder : 0.034 <br>Coef. Intercept : 2.019","<b> bootstrap dataset:  8 <\/b> <br>Coef. Urban  : -0.059 <br>Coef. Murder : 0.048 <br>Coef. Intercept : 2.958","<b> bootstrap dataset:  9 <\/b> <br>Coef. Urban  : -0.032 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 2.626","<b> bootstrap dataset:  10 <\/b> <br>Coef. Urban  : -0.033 <br>Coef. Murder : 0.035 <br>Coef. Intercept : 3.814","<b> bootstrap dataset:  11 <\/b> <br>Coef. Urban  : -0.027 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 2.797","<b> bootstrap dataset:  12 <\/b> <br>Coef. Urban  : -0.053 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 4.094","<b> bootstrap dataset:  13 <\/b> <br>Coef. Urban  : -0.02 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 2.091","<b> bootstrap dataset:  14 <\/b> <br>Coef. Urban  : -0.047 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 2.91","<b> bootstrap dataset:  15 <\/b> <br>Coef. Urban  : -0.059 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 4.769","<b> bootstrap dataset:  16 <\/b> <br>Coef. Urban  : -0.015 <br>Coef. Murder : 0.038 <br>Coef. Intercept : 1.383","<b> bootstrap dataset:  17 <\/b> <br>Coef. Urban  : -0.044 <br>Coef. Murder : 0.035 <br>Coef. Intercept : 4.657","<b> bootstrap dataset:  18 <\/b> <br>Coef. Urban  : -0.033 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 2.536","<b> bootstrap dataset:  19 <\/b> <br>Coef. Urban  : -0.031 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 2.849","<b> bootstrap dataset:  20 <\/b> <br>Coef. Urban  : -0.073 <br>Coef. Murder : 0.052 <br>Coef. Intercept : 3.781","<b> bootstrap dataset:  21 <\/b> <br>Coef. Urban  : -0.012 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 0.708","<b> bootstrap dataset:  22 <\/b> <br>Coef. Urban  : -0.067 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 5.48","<b> bootstrap dataset:  23 <\/b> <br>Coef. Urban  : -0.041 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 3.066","<b> bootstrap dataset:  24 <\/b> <br>Coef. Urban  : -0.075 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 4.997","<b> bootstrap dataset:  25 <\/b> <br>Coef. Urban  : -0.013 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 1.092","<b> bootstrap dataset:  26 <\/b> <br>Coef. Urban  : -0.036 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 2.737","<b> bootstrap dataset:  27 <\/b> <br>Coef. Urban  : -0.038 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 2.829","<b> bootstrap dataset:  28 <\/b> <br>Coef. Urban  : -0.044 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 3.021","<b> bootstrap dataset:  29 <\/b> <br>Coef. Urban  : -0.043 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 3.672","<b> bootstrap dataset:  30 <\/b> <br>Coef. Urban  : -0.006 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 1.402","<b> bootstrap dataset:  31 <\/b> <br>Coef. Urban  : -0.021 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 1.699","<b> bootstrap dataset:  32 <\/b> <br>Coef. Urban  : -0.03 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 2.375","<b> bootstrap dataset:  33 <\/b> <br>Coef. Urban  : -0.035 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 2.47","<b> bootstrap dataset:  34 <\/b> <br>Coef. Urban  : -0.031 <br>Coef. Murder : 0.033 <br>Coef. Intercept : 3.693","<b> bootstrap dataset:  35 <\/b> <br>Coef. Urban  : -0.069 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 4.124","<b> bootstrap dataset:  36 <\/b> <br>Coef. Urban  : -0.055 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 4.813","<b> bootstrap dataset:  37 <\/b> <br>Coef. Urban  : -0.03 <br>Coef. Murder : 0.037 <br>Coef. Intercept : 3.266","<b> bootstrap dataset:  38 <\/b> <br>Coef. Urban  : -0.039 <br>Coef. Murder : 0.037 <br>Coef. Intercept : 3.801","<b> bootstrap dataset:  39 <\/b> <br>Coef. Urban  : -0.081 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 5.66","<b> bootstrap dataset:  40 <\/b> <br>Coef. Urban  : -0.097 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 8.029","<b> bootstrap dataset:  41 <\/b> <br>Coef. Urban  : -0.071 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 4.93","<b> bootstrap dataset:  42 <\/b> <br>Coef. Urban  : -0.014 <br>Coef. Murder : 0.038 <br>Coef. Intercept : 1.769","<b> bootstrap dataset:  43 <\/b> <br>Coef. Urban  : -0.041 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 2.659","<b> bootstrap dataset:  44 <\/b> <br>Coef. Urban  : -0.024 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 2.401","<b> bootstrap dataset:  45 <\/b> <br>Coef. Urban  : -0.052 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 3.548","<b> bootstrap dataset:  46 <\/b> <br>Coef. Urban  : -0.069 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 4.722","<b> bootstrap dataset:  47 <\/b> <br>Coef. Urban  : -0.062 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 5.172","<b> bootstrap dataset:  48 <\/b> <br>Coef. Urban  : -0.055 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 3.528","<b> bootstrap dataset:  49 <\/b> <br>Coef. Urban  : -0.069 <br>Coef. Murder : 0.05 <br>Coef. Intercept : 3.66","<b> bootstrap dataset:  50 <\/b> <br>Coef. Urban  : -0.026 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 2.796","<b> bootstrap dataset:  51 <\/b> <br>Coef. Urban  : -0.027 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 3.08","<b> bootstrap dataset:  52 <\/b> <br>Coef. Urban  : -0.061 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 3.901","<b> bootstrap dataset:  53 <\/b> <br>Coef. Urban  : 0.006 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 0.253","<b> bootstrap dataset:  54 <\/b> <br>Coef. Urban  : -0.079 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 6.595","<b> bootstrap dataset:  55 <\/b> <br>Coef. Urban  : -0.086 <br>Coef. Murder : 0.054 <br>Coef. Intercept : 4.512","<b> bootstrap dataset:  56 <\/b> <br>Coef. Urban  : -0.022 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 1.573","<b> bootstrap dataset:  57 <\/b> <br>Coef. Urban  : -0.029 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 1.756","<b> bootstrap dataset:  58 <\/b> <br>Coef. Urban  : -0.052 <br>Coef. Murder : 0.048 <br>Coef. Intercept : 2.563","<b> bootstrap dataset:  59 <\/b> <br>Coef. Urban  : -0.044 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 2.639","<b> bootstrap dataset:  60 <\/b> <br>Coef. Urban  : -0.036 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 3.199","<b> bootstrap dataset:  61 <\/b> <br>Coef. Urban  : -0.093 <br>Coef. Murder : 0.048 <br>Coef. Intercept : 5.851","<b> bootstrap dataset:  62 <\/b> <br>Coef. Urban  : -0.069 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 5.465","<b> bootstrap dataset:  63 <\/b> <br>Coef. Urban  : -0.05 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 3.648","<b> bootstrap dataset:  64 <\/b> <br>Coef. Urban  : -0.007 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 0.919","<b> bootstrap dataset:  65 <\/b> <br>Coef. Urban  : -0.054 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 3.564","<b> bootstrap dataset:  66 <\/b> <br>Coef. Urban  : -0.053 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 4.802","<b> bootstrap dataset:  67 <\/b> <br>Coef. Urban  : -0.074 <br>Coef. Murder : 0.051 <br>Coef. Intercept : 3.966","<b> bootstrap dataset:  68 <\/b> <br>Coef. Urban  : -0.031 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 3.894","<b> bootstrap dataset:  69 <\/b> <br>Coef. Urban  : -0.006 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 1.394","<b> bootstrap dataset:  70 <\/b> <br>Coef. Urban  : -0.105 <br>Coef. Murder : 0.061 <br>Coef. Intercept : 4.053","<b> bootstrap dataset:  71 <\/b> <br>Coef. Urban  : -0.016 <br>Coef. Murder : 0.037 <br>Coef. Intercept : 2.31","<b> bootstrap dataset:  72 <\/b> <br>Coef. Urban  : -0.068 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 4.985","<b> bootstrap dataset:  73 <\/b> <br>Coef. Urban  : -0.051 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 4.187","<b> bootstrap dataset:  74 <\/b> <br>Coef. Urban  : -0.085 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 5.891","<b> bootstrap dataset:  75 <\/b> <br>Coef. Urban  : -0.026 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 2.731","<b> bootstrap dataset:  76 <\/b> <br>Coef. Urban  : -0.073 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 6.165","<b> bootstrap dataset:  77 <\/b> <br>Coef. Urban  : -0.018 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 1.086","<b> bootstrap dataset:  78 <\/b> <br>Coef. Urban  : -0.06 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 4.724","<b> bootstrap dataset:  79 <\/b> <br>Coef. Urban  : -0.029 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 2.323","<b> bootstrap dataset:  80 <\/b> <br>Coef. Urban  : -0.062 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 3.963","<b> bootstrap dataset:  81 <\/b> <br>Coef. Urban  : -0.001 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 0.722","<b> bootstrap dataset:  82 <\/b> <br>Coef. Urban  : -0.057 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 4.073","<b> bootstrap dataset:  83 <\/b> <br>Coef. Urban  : -0.034 <br>Coef. Murder : 0.036 <br>Coef. Intercept : 4.352","<b> bootstrap dataset:  84 <\/b> <br>Coef. Urban  : -0.038 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 3.31","<b> bootstrap dataset:  85 <\/b> <br>Coef. Urban  : -0.057 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 3.679","<b> bootstrap dataset:  86 <\/b> <br>Coef. Urban  : -0.077 <br>Coef. Murder : 0.049 <br>Coef. Intercept : 4.871","<b> bootstrap dataset:  87 <\/b> <br>Coef. Urban  : -0.04 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 2.816","<b> bootstrap dataset:  88 <\/b> <br>Coef. Urban  : -0.02 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 1.407","<b> bootstrap dataset:  89 <\/b> <br>Coef. Urban  : -0.023 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 1.685","<b> bootstrap dataset:  90 <\/b> <br>Coef. Urban  : -0.097 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 6.081","<b> bootstrap dataset:  91 <\/b> <br>Coef. Urban  : -0.058 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 4.56","<b> bootstrap dataset:  92 <\/b> <br>Coef. Urban  : -0.054 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 4.492","<b> bootstrap dataset:  93 <\/b> <br>Coef. Urban  : -0.055 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 4.282","<b> bootstrap dataset:  94 <\/b> <br>Coef. Urban  : -0.021 <br>Coef. Murder : 0.049 <br>Coef. Intercept : 1.38","<b> bootstrap dataset:  95 <\/b> <br>Coef. Urban  : -0.042 <br>Coef. Murder : 0.048 <br>Coef. Intercept : 2.459","<b> bootstrap dataset:  96 <\/b> <br>Coef. Urban  : -0.057 <br>Coef. Murder : 0.037 <br>Coef. Intercept : 4.607","<b> bootstrap dataset:  97 <\/b> <br>Coef. Urban  : -0.03 <br>Coef. Murder : 0.05 <br>Coef. Intercept : 0.919","<b> bootstrap dataset:  98 <\/b> <br>Coef. Urban  : -0.024 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 1.831","<b> bootstrap dataset:  99 <\/b> <br>Coef. Urban  : -0.046 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 3.136","<b> bootstrap dataset:  100 <\/b> <br>Coef. Urban  : -0.056 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 3.758","<b> bootstrap dataset:  101 <\/b> <br>Coef. Urban  : -0.002 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 0.812","<b> bootstrap dataset:  102 <\/b> <br>Coef. Urban  : -0.059 <br>Coef. Murder : 0.048 <br>Coef. Intercept : 3.684","<b> bootstrap dataset:  103 <\/b> <br>Coef. Urban  : -0.026 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 2.469","<b> bootstrap dataset:  104 <\/b> <br>Coef. Urban  : -0.049 <br>Coef. Murder : 0.049 <br>Coef. Intercept : 2.974","<b> bootstrap dataset:  105 <\/b> <br>Coef. Urban  : -0.074 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 5.193","<b> bootstrap dataset:  106 <\/b> <br>Coef. Urban  : -0.053 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 3.869","<b> bootstrap dataset:  107 <\/b> <br>Coef. Urban  : -0.009 <br>Coef. Murder : 0.036 <br>Coef. Intercept : 1.706","<b> bootstrap dataset:  108 <\/b> <br>Coef. Urban  : -0.025 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 1.996","<b> bootstrap dataset:  109 <\/b> <br>Coef. Urban  : -0.038 <br>Coef. Murder : 0.037 <br>Coef. Intercept : 3.528","<b> bootstrap dataset:  110 <\/b> <br>Coef. Urban  : -0.088 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 5.298","<b> bootstrap dataset:  111 <\/b> <br>Coef. Urban  : -0.091 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 6.892","<b> bootstrap dataset:  112 <\/b> <br>Coef. Urban  : -0.072 <br>Coef. Murder : 0.037 <br>Coef. Intercept : 5.443","<b> bootstrap dataset:  113 <\/b> <br>Coef. Urban  : -0.03 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 1.658","<b> bootstrap dataset:  114 <\/b> <br>Coef. Urban  : -0.05 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 3.91","<b> bootstrap dataset:  115 <\/b> <br>Coef. Urban  : -0.033 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 2.802","<b> bootstrap dataset:  116 <\/b> <br>Coef. Urban  : -0.073 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 4.381","<b> bootstrap dataset:  117 <\/b> <br>Coef. Urban  : -0.058 <br>Coef. Murder : 0.049 <br>Coef. Intercept : 3.414","<b> bootstrap dataset:  118 <\/b> <br>Coef. Urban  : -0.039 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 3.127","<b> bootstrap dataset:  119 <\/b> <br>Coef. Urban  : -0.056 <br>Coef. Murder : 0.05 <br>Coef. Intercept : 2.837","<b> bootstrap dataset:  120 <\/b> <br>Coef. Urban  : -0.036 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 2.557","<b> bootstrap dataset:  121 <\/b> <br>Coef. Urban  : -0.069 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 4.569","<b> bootstrap dataset:  122 <\/b> <br>Coef. Urban  : -0.055 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 3.497","<b> bootstrap dataset:  123 <\/b> <br>Coef. Urban  : -0.039 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 3.379","<b> bootstrap dataset:  124 <\/b> <br>Coef. Urban  : -0.031 <br>Coef. Murder : 0.048 <br>Coef. Intercept : 2.016","<b> bootstrap dataset:  125 <\/b> <br>Coef. Urban  : -0.009 <br>Coef. Murder : 0.037 <br>Coef. Intercept : 2.239","<b> bootstrap dataset:  126 <\/b> <br>Coef. Urban  : -0.026 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 1.728","<b> bootstrap dataset:  127 <\/b> <br>Coef. Urban  : -0.086 <br>Coef. Murder : 0.048 <br>Coef. Intercept : 5.106","<b> bootstrap dataset:  128 <\/b> <br>Coef. Urban  : -0.042 <br>Coef. Murder : 0.049 <br>Coef. Intercept : 1.647","<b> bootstrap dataset:  129 <\/b> <br>Coef. Urban  : -0.029 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 2.45","<b> bootstrap dataset:  130 <\/b> <br>Coef. Urban  : -0.026 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 2.503","<b> bootstrap dataset:  131 <\/b> <br>Coef. Urban  : -0.045 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 4.21","<b> bootstrap dataset:  132 <\/b> <br>Coef. Urban  : -0.07 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 5.328","<b> bootstrap dataset:  133 <\/b> <br>Coef. Urban  : -0.002 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 0.47","<b> bootstrap dataset:  134 <\/b> <br>Coef. Urban  : -0.066 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 3.685","<b> bootstrap dataset:  135 <\/b> <br>Coef. Urban  : -0.066 <br>Coef. Murder : 0.05 <br>Coef. Intercept : 3.462","<b> bootstrap dataset:  136 <\/b> <br>Coef. Urban  : -0.057 <br>Coef. Murder : 0.052 <br>Coef. Intercept : 3.172","<b> bootstrap dataset:  137 <\/b> <br>Coef. Urban  : -0.036 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 3.572","<b> bootstrap dataset:  138 <\/b> <br>Coef. Urban  : -0.073 <br>Coef. Murder : 0.053 <br>Coef. Intercept : 3.789","<b> bootstrap dataset:  139 <\/b> <br>Coef. Urban  : -0.061 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 4.677","<b> bootstrap dataset:  140 <\/b> <br>Coef. Urban  : -0.113 <br>Coef. Murder : 0.05 <br>Coef. Intercept : 6.711","<b> bootstrap dataset:  141 <\/b> <br>Coef. Urban  : 0.01 <br>Coef. Murder : 0.041 <br>Coef. Intercept : -0.12","<b> bootstrap dataset:  142 <\/b> <br>Coef. Urban  : -0.054 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 3.605","<b> bootstrap dataset:  143 <\/b> <br>Coef. Urban  : -0.059 <br>Coef. Murder : 0.05 <br>Coef. Intercept : 3.632","<b> bootstrap dataset:  144 <\/b> <br>Coef. Urban  : -0.065 <br>Coef. Murder : 0.05 <br>Coef. Intercept : 3.507","<b> bootstrap dataset:  145 <\/b> <br>Coef. Urban  : -0.058 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 4.499","<b> bootstrap dataset:  146 <\/b> <br>Coef. Urban  : -0.03 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 2.742","<b> bootstrap dataset:  147 <\/b> <br>Coef. Urban  : -0.018 <br>Coef. Murder : 0.032 <br>Coef. Intercept : 3.653","<b> bootstrap dataset:  148 <\/b> <br>Coef. Urban  : -0.04 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 2.436","<b> bootstrap dataset:  149 <\/b> <br>Coef. Urban  : -0.027 <br>Coef. Murder : 0.037 <br>Coef. Intercept : 3.244","<b> bootstrap dataset:  150 <\/b> <br>Coef. Urban  : -0.036 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 2.675","<b> bootstrap dataset:  151 <\/b> <br>Coef. Urban  : -0.085 <br>Coef. Murder : 0.052 <br>Coef. Intercept : 4.624","<b> bootstrap dataset:  152 <\/b> <br>Coef. Urban  : -0.029 <br>Coef. Murder : 0.049 <br>Coef. Intercept : 1.713","<b> bootstrap dataset:  153 <\/b> <br>Coef. Urban  : -0.096 <br>Coef. Murder : 0.054 <br>Coef. Intercept : 4.478","<b> bootstrap dataset:  154 <\/b> <br>Coef. Urban  : -0.068 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 4.49","<b> bootstrap dataset:  155 <\/b> <br>Coef. Urban  : -0.056 <br>Coef. Murder : 0.036 <br>Coef. Intercept : 5.62","<b> bootstrap dataset:  156 <\/b> <br>Coef. Urban  : -0.035 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 2.436","<b> bootstrap dataset:  157 <\/b> <br>Coef. Urban  : -0.042 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 2.216","<b> bootstrap dataset:  158 <\/b> <br>Coef. Urban  : -0.047 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 3.336","<b> bootstrap dataset:  159 <\/b> <br>Coef. Urban  : -0.061 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 3.82","<b> bootstrap dataset:  160 <\/b> <br>Coef. Urban  : -0.038 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 3.717","<b> bootstrap dataset:  161 <\/b> <br>Coef. Urban  : -0.05 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 3.537","<b> bootstrap dataset:  162 <\/b> <br>Coef. Urban  : -0.081 <br>Coef. Murder : 0.051 <br>Coef. Intercept : 4.02","<b> bootstrap dataset:  163 <\/b> <br>Coef. Urban  : 0 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 0.072","<b> bootstrap dataset:  164 <\/b> <br>Coef. Urban  : -0.063 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 4.206","<b> bootstrap dataset:  165 <\/b> <br>Coef. Urban  : -0.032 <br>Coef. Murder : 0.037 <br>Coef. Intercept : 3.039","<b> bootstrap dataset:  166 <\/b> <br>Coef. Urban  : -0.024 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 2.204","<b> bootstrap dataset:  167 <\/b> <br>Coef. Urban  : -0.073 <br>Coef. Murder : 0.059 <br>Coef. Intercept : 2.89","<b> bootstrap dataset:  168 <\/b> <br>Coef. Urban  : -0.085 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 5.965","<b> bootstrap dataset:  169 <\/b> <br>Coef. Urban  : -0.049 <br>Coef. Murder : 0.049 <br>Coef. Intercept : 2.438","<b> bootstrap dataset:  170 <\/b> <br>Coef. Urban  : -0.03 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 2.113","<b> bootstrap dataset:  171 <\/b> <br>Coef. Urban  : -0.041 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 2.84","<b> bootstrap dataset:  172 <\/b> <br>Coef. Urban  : -0.048 <br>Coef. Murder : 0.048 <br>Coef. Intercept : 3.085","<b> bootstrap dataset:  173 <\/b> <br>Coef. Urban  : -0.069 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 4.015","<b> bootstrap dataset:  174 <\/b> <br>Coef. Urban  : -0.037 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 2.583","<b> bootstrap dataset:  175 <\/b> <br>Coef. Urban  : -0.019 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 2.138","<b> bootstrap dataset:  176 <\/b> <br>Coef. Urban  : -0.03 <br>Coef. Murder : 0.038 <br>Coef. Intercept : 2.826","<b> bootstrap dataset:  177 <\/b> <br>Coef. Urban  : -0.042 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 3.34","<b> bootstrap dataset:  178 <\/b> <br>Coef. Urban  : -0.035 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 2.559","<b> bootstrap dataset:  179 <\/b> <br>Coef. Urban  : -0.004 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 0.801","<b> bootstrap dataset:  180 <\/b> <br>Coef. Urban  : -0.089 <br>Coef. Murder : 0.048 <br>Coef. Intercept : 5.408","<b> bootstrap dataset:  181 <\/b> <br>Coef. Urban  : -0.039 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 2.324","<b> bootstrap dataset:  182 <\/b> <br>Coef. Urban  : -0.004 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 0.783","<b> bootstrap dataset:  183 <\/b> <br>Coef. Urban  : -0.037 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 2.555","<b> bootstrap dataset:  184 <\/b> <br>Coef. Urban  : -0.085 <br>Coef. Murder : 0.058 <br>Coef. Intercept : 3.967","<b> bootstrap dataset:  185 <\/b> <br>Coef. Urban  : -0.037 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 2.668","<b> bootstrap dataset:  186 <\/b> <br>Coef. Urban  : -0.033 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 3.222","<b> bootstrap dataset:  187 <\/b> <br>Coef. Urban  : -0.066 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 5.001","<b> bootstrap dataset:  188 <\/b> <br>Coef. Urban  : -0.04 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 3.579","<b> bootstrap dataset:  189 <\/b> <br>Coef. Urban  : -0.012 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 1.941","<b> bootstrap dataset:  190 <\/b> <br>Coef. Urban  : -0.068 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 4.41","<b> bootstrap dataset:  191 <\/b> <br>Coef. Urban  : -0.03 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 2.744","<b> bootstrap dataset:  192 <\/b> <br>Coef. Urban  : -0.032 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 1.871","<b> bootstrap dataset:  193 <\/b> <br>Coef. Urban  : -0.034 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 2.863","<b> bootstrap dataset:  194 <\/b> <br>Coef. Urban  : -0.043 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 2.505","<b> bootstrap dataset:  195 <\/b> <br>Coef. Urban  : -0.014 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 1.807","<b> bootstrap dataset:  196 <\/b> <br>Coef. Urban  : -0.04 <br>Coef. Murder : 0.051 <br>Coef. Intercept : 2.599","<b> bootstrap dataset:  197 <\/b> <br>Coef. Urban  : -0.045 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 3.179","<b> bootstrap dataset:  198 <\/b> <br>Coef. Urban  : -0.004 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 1.413","<b> bootstrap dataset:  199 <\/b> <br>Coef. Urban  : -0.057 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 3.349","<b> bootstrap dataset:  200 <\/b> <br>Coef. Urban  : -0.06 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 4.627","<b> bootstrap dataset:  201 <\/b> <br>Coef. Urban  : -0.058 <br>Coef. Murder : 0.048 <br>Coef. Intercept : 3.369","<b> bootstrap dataset:  202 <\/b> <br>Coef. Urban  : -0.055 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 3.741","<b> bootstrap dataset:  203 <\/b> <br>Coef. Urban  : -0.034 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 2.75","<b> bootstrap dataset:  204 <\/b> <br>Coef. Urban  : -0.065 <br>Coef. Murder : 0.034 <br>Coef. Intercept : 6.924","<b> bootstrap dataset:  205 <\/b> <br>Coef. Urban  : -0.04 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 2.77","<b> bootstrap dataset:  206 <\/b> <br>Coef. Urban  : -0.054 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 3.643","<b> bootstrap dataset:  207 <\/b> <br>Coef. Urban  : -0.062 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 4.633","<b> bootstrap dataset:  208 <\/b> <br>Coef. Urban  : -0.079 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 5.225","<b> bootstrap dataset:  209 <\/b> <br>Coef. Urban  : -0.021 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 1.345","<b> bootstrap dataset:  210 <\/b> <br>Coef. Urban  : -0.01 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 1.832","<b> bootstrap dataset:  211 <\/b> <br>Coef. Urban  : -0.026 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 2.46","<b> bootstrap dataset:  212 <\/b> <br>Coef. Urban  : -0.038 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 2.155","<b> bootstrap dataset:  213 <\/b> <br>Coef. Urban  : -0.041 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 3.054","<b> bootstrap dataset:  214 <\/b> <br>Coef. Urban  : -0.035 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 2.102","<b> bootstrap dataset:  215 <\/b> <br>Coef. Urban  : -0.075 <br>Coef. Murder : 0.048 <br>Coef. Intercept : 4.642","<b> bootstrap dataset:  216 <\/b> <br>Coef. Urban  : -0.044 <br>Coef. Murder : 0.048 <br>Coef. Intercept : 3.178","<b> bootstrap dataset:  217 <\/b> <br>Coef. Urban  : -0.06 <br>Coef. Murder : 0.049 <br>Coef. Intercept : 3.297","<b> bootstrap dataset:  218 <\/b> <br>Coef. Urban  : -0.056 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 3.813","<b> bootstrap dataset:  219 <\/b> <br>Coef. Urban  : -0.026 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 2.407","<b> bootstrap dataset:  220 <\/b> <br>Coef. Urban  : -0.073 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 4.783","<b> bootstrap dataset:  221 <\/b> <br>Coef. Urban  : -0.028 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 3.118","<b> bootstrap dataset:  222 <\/b> <br>Coef. Urban  : -0.055 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 3.406","<b> bootstrap dataset:  223 <\/b> <br>Coef. Urban  : -0.009 <br>Coef. Murder : 0.035 <br>Coef. Intercept : 1.846","<b> bootstrap dataset:  224 <\/b> <br>Coef. Urban  : -0.058 <br>Coef. Murder : 0.049 <br>Coef. Intercept : 3.155","<b> bootstrap dataset:  225 <\/b> <br>Coef. Urban  : -0.045 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 3.242","<b> bootstrap dataset:  226 <\/b> <br>Coef. Urban  : -0.033 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 2.643","<b> bootstrap dataset:  227 <\/b> <br>Coef. Urban  : -0.061 <br>Coef. Murder : 0.048 <br>Coef. Intercept : 3.785","<b> bootstrap dataset:  228 <\/b> <br>Coef. Urban  : -0.036 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 3.392","<b> bootstrap dataset:  229 <\/b> <br>Coef. Urban  : -0.087 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 5.418","<b> bootstrap dataset:  230 <\/b> <br>Coef. Urban  : -0.027 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 2.18","<b> bootstrap dataset:  231 <\/b> <br>Coef. Urban  : -0.034 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 3.084","<b> bootstrap dataset:  232 <\/b> <br>Coef. Urban  : -0.024 <br>Coef. Murder : 0.048 <br>Coef. Intercept : 1.661","<b> bootstrap dataset:  233 <\/b> <br>Coef. Urban  : -0.055 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 4.399","<b> bootstrap dataset:  234 <\/b> <br>Coef. Urban  : -0.052 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 3.307","<b> bootstrap dataset:  235 <\/b> <br>Coef. Urban  : -0.023 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 1.731","<b> bootstrap dataset:  236 <\/b> <br>Coef. Urban  : -0.072 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 4.535","<b> bootstrap dataset:  237 <\/b> <br>Coef. Urban  : -0.017 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 1.346","<b> bootstrap dataset:  238 <\/b> <br>Coef. Urban  : -0.039 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 2.573","<b> bootstrap dataset:  239 <\/b> <br>Coef. Urban  : -0.041 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 2.992","<b> bootstrap dataset:  240 <\/b> <br>Coef. Urban  : -0.048 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 3.283","<b> bootstrap dataset:  241 <\/b> <br>Coef. Urban  : -0.08 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 6.165","<b> bootstrap dataset:  242 <\/b> <br>Coef. Urban  : -0.08 <br>Coef. Murder : 0.051 <br>Coef. Intercept : 4.141","<b> bootstrap dataset:  243 <\/b> <br>Coef. Urban  : -0.044 <br>Coef. Murder : 0.037 <br>Coef. Intercept : 4.312","<b> bootstrap dataset:  244 <\/b> <br>Coef. Urban  : -0.036 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 3.18","<b> bootstrap dataset:  245 <\/b> <br>Coef. Urban  : -0.022 <br>Coef. Murder : 0.031 <br>Coef. Intercept : 3.381","<b> bootstrap dataset:  246 <\/b> <br>Coef. Urban  : -0.065 <br>Coef. Murder : 0.049 <br>Coef. Intercept : 3.84","<b> bootstrap dataset:  247 <\/b> <br>Coef. Urban  : -0.055 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 3.598","<b> bootstrap dataset:  248 <\/b> <br>Coef. Urban  : -0.078 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 5.724","<b> bootstrap dataset:  249 <\/b> <br>Coef. Urban  : -0.029 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 1.846","<b> bootstrap dataset:  250 <\/b> <br>Coef. Urban  : -0.042 <br>Coef. Murder : 0.037 <br>Coef. Intercept : 4.385","<b> bootstrap dataset:  251 <\/b> <br>Coef. Urban  : -0.028 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 1.902","<b> bootstrap dataset:  252 <\/b> <br>Coef. Urban  : -0.083 <br>Coef. Murder : 0.051 <br>Coef. Intercept : 4.914","<b> bootstrap dataset:  253 <\/b> <br>Coef. Urban  : -0.045 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 3.731","<b> bootstrap dataset:  254 <\/b> <br>Coef. Urban  : -0.052 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 4.04","<b> bootstrap dataset:  255 <\/b> <br>Coef. Urban  : 0.005 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 0.155","<b> bootstrap dataset:  256 <\/b> <br>Coef. Urban  : -0.049 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 3.468","<b> bootstrap dataset:  257 <\/b> <br>Coef. Urban  : -0.065 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 4.298","<b> bootstrap dataset:  258 <\/b> <br>Coef. Urban  : -0.05 <br>Coef. Murder : 0.035 <br>Coef. Intercept : 5.517","<b> bootstrap dataset:  259 <\/b> <br>Coef. Urban  : -0.063 <br>Coef. Murder : 0.057 <br>Coef. Intercept : 2.293","<b> bootstrap dataset:  260 <\/b> <br>Coef. Urban  : -0.037 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 2.291","<b> bootstrap dataset:  261 <\/b> <br>Coef. Urban  : -0.063 <br>Coef. Murder : 0.051 <br>Coef. Intercept : 2.809","<b> bootstrap dataset:  262 <\/b> <br>Coef. Urban  : -0.046 <br>Coef. Murder : 0.053 <br>Coef. Intercept : 1.563","<b> bootstrap dataset:  263 <\/b> <br>Coef. Urban  : -0.021 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 2.285","<b> bootstrap dataset:  264 <\/b> <br>Coef. Urban  : -0.022 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 1.323","<b> bootstrap dataset:  265 <\/b> <br>Coef. Urban  : -0.072 <br>Coef. Murder : 0.038 <br>Coef. Intercept : 6.083","<b> bootstrap dataset:  266 <\/b> <br>Coef. Urban  : -0.039 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 2.384","<b> bootstrap dataset:  267 <\/b> <br>Coef. Urban  : -0.074 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 5.577","<b> bootstrap dataset:  268 <\/b> <br>Coef. Urban  : -0.016 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 1.719","<b> bootstrap dataset:  269 <\/b> <br>Coef. Urban  : -0.079 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 5.37","<b> bootstrap dataset:  270 <\/b> <br>Coef. Urban  : -0.064 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 4.08","<b> bootstrap dataset:  271 <\/b> <br>Coef. Urban  : -0.059 <br>Coef. Murder : 0.048 <br>Coef. Intercept : 3.669","<b> bootstrap dataset:  272 <\/b> <br>Coef. Urban  : -0.055 <br>Coef. Murder : 0.031 <br>Coef. Intercept : 5.818","<b> bootstrap dataset:  273 <\/b> <br>Coef. Urban  : -0.061 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 3.736","<b> bootstrap dataset:  274 <\/b> <br>Coef. Urban  : -0.119 <br>Coef. Murder : 0.056 <br>Coef. Intercept : 6.17","<b> bootstrap dataset:  275 <\/b> <br>Coef. Urban  : -0.054 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 3.802","<b> bootstrap dataset:  276 <\/b> <br>Coef. Urban  : 0.017 <br>Coef. Murder : 0.04 <br>Coef. Intercept : -0.674","<b> bootstrap dataset:  277 <\/b> <br>Coef. Urban  : -0.029 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 3.094","<b> bootstrap dataset:  278 <\/b> <br>Coef. Urban  : -0.057 <br>Coef. Murder : 0.038 <br>Coef. Intercept : 5.783","<b> bootstrap dataset:  279 <\/b> <br>Coef. Urban  : -0.028 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 2.055","<b> bootstrap dataset:  280 <\/b> <br>Coef. Urban  : -0.053 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 3.766","<b> bootstrap dataset:  281 <\/b> <br>Coef. Urban  : 0.006 <br>Coef. Murder : 0.044 <br>Coef. Intercept : -0.039","<b> bootstrap dataset:  282 <\/b> <br>Coef. Urban  : -0.06 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 3.998","<b> bootstrap dataset:  283 <\/b> <br>Coef. Urban  : -0.039 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 3.163","<b> bootstrap dataset:  284 <\/b> <br>Coef. Urban  : -0.031 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 2.54","<b> bootstrap dataset:  285 <\/b> <br>Coef. Urban  : -0.044 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 3.075","<b> bootstrap dataset:  286 <\/b> <br>Coef. Urban  : -0.045 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 2.941","<b> bootstrap dataset:  287 <\/b> <br>Coef. Urban  : -0.064 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 3.961","<b> bootstrap dataset:  288 <\/b> <br>Coef. Urban  : -0.082 <br>Coef. Murder : 0.052 <br>Coef. Intercept : 4.9","<b> bootstrap dataset:  289 <\/b> <br>Coef. Urban  : -0.072 <br>Coef. Murder : 0.05 <br>Coef. Intercept : 4.014","<b> bootstrap dataset:  290 <\/b> <br>Coef. Urban  : -0.063 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 4.917","<b> bootstrap dataset:  291 <\/b> <br>Coef. Urban  : -0.123 <br>Coef. Murder : 0.058 <br>Coef. Intercept : 6.329","<b> bootstrap dataset:  292 <\/b> <br>Coef. Urban  : 0.006 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 0.444","<b> bootstrap dataset:  293 <\/b> <br>Coef. Urban  : -0.043 <br>Coef. Murder : 0.034 <br>Coef. Intercept : 4.88","<b> bootstrap dataset:  294 <\/b> <br>Coef. Urban  : -0.054 <br>Coef. Murder : 0.05 <br>Coef. Intercept : 2.769","<b> bootstrap dataset:  295 <\/b> <br>Coef. Urban  : -0.055 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 4.281","<b> bootstrap dataset:  296 <\/b> <br>Coef. Urban  : -0.069 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 5.334","<b> bootstrap dataset:  297 <\/b> <br>Coef. Urban  : -0.053 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 4.684","<b> bootstrap dataset:  298 <\/b> <br>Coef. Urban  : -0.016 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 1.721","<b> bootstrap dataset:  299 <\/b> <br>Coef. Urban  : -0.06 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 3.874","<b> bootstrap dataset:  300 <\/b> <br>Coef. Urban  : -0.005 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 0.59","<b> bootstrap dataset:  301 <\/b> <br>Coef. Urban  : -0.015 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 1.344","<b> bootstrap dataset:  302 <\/b> <br>Coef. Urban  : -0.052 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 3.431","<b> bootstrap dataset:  303 <\/b> <br>Coef. Urban  : -0.047 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 2.7","<b> bootstrap dataset:  304 <\/b> <br>Coef. Urban  : -0.075 <br>Coef. Murder : 0.048 <br>Coef. Intercept : 4.133","<b> bootstrap dataset:  305 <\/b> <br>Coef. Urban  : -0.059 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 4.495","<b> bootstrap dataset:  306 <\/b> <br>Coef. Urban  : -0.057 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 4.01","<b> bootstrap dataset:  307 <\/b> <br>Coef. Urban  : -0.092 <br>Coef. Murder : 0.051 <br>Coef. Intercept : 5.078","<b> bootstrap dataset:  308 <\/b> <br>Coef. Urban  : -0.049 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 4.133","<b> bootstrap dataset:  309 <\/b> <br>Coef. Urban  : -0.031 <br>Coef. Murder : 0.048 <br>Coef. Intercept : 1.869","<b> bootstrap dataset:  310 <\/b> <br>Coef. Urban  : -0.105 <br>Coef. Murder : 0.05 <br>Coef. Intercept : 6.403","<b> bootstrap dataset:  311 <\/b> <br>Coef. Urban  : -0.037 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 3.043","<b> bootstrap dataset:  312 <\/b> <br>Coef. Urban  : -0.056 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 4.496","<b> bootstrap dataset:  313 <\/b> <br>Coef. Urban  : -0.061 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 4.911","<b> bootstrap dataset:  314 <\/b> <br>Coef. Urban  : -0.083 <br>Coef. Murder : 0.048 <br>Coef. Intercept : 6.032","<b> bootstrap dataset:  315 <\/b> <br>Coef. Urban  : -0.117 <br>Coef. Murder : 0.052 <br>Coef. Intercept : 7","<b> bootstrap dataset:  316 <\/b> <br>Coef. Urban  : -0.078 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 5.292","<b> bootstrap dataset:  317 <\/b> <br>Coef. Urban  : -0.048 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 4.251","<b> bootstrap dataset:  318 <\/b> <br>Coef. Urban  : -0.051 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 4.004","<b> bootstrap dataset:  319 <\/b> <br>Coef. Urban  : -0.041 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 3.304","<b> bootstrap dataset:  320 <\/b> <br>Coef. Urban  : -0.082 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 5.223","<b> bootstrap dataset:  321 <\/b> <br>Coef. Urban  : -0.071 <br>Coef. Murder : 0.049 <br>Coef. Intercept : 3.67","<b> bootstrap dataset:  322 <\/b> <br>Coef. Urban  : -0.036 <br>Coef. Murder : 0.037 <br>Coef. Intercept : 3.648","<b> bootstrap dataset:  323 <\/b> <br>Coef. Urban  : -0.033 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 2.969","<b> bootstrap dataset:  324 <\/b> <br>Coef. Urban  : -0.077 <br>Coef. Murder : 0.048 <br>Coef. Intercept : 5.054","<b> bootstrap dataset:  325 <\/b> <br>Coef. Urban  : -0.029 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 3.241","<b> bootstrap dataset:  326 <\/b> <br>Coef. Urban  : -0.035 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 2.608","<b> bootstrap dataset:  327 <\/b> <br>Coef. Urban  : -0.048 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 3.317","<b> bootstrap dataset:  328 <\/b> <br>Coef. Urban  : -0.019 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 2.157","<b> bootstrap dataset:  329 <\/b> <br>Coef. Urban  : -0.037 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 3.009","<b> bootstrap dataset:  330 <\/b> <br>Coef. Urban  : -0.039 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 2.517","<b> bootstrap dataset:  331 <\/b> <br>Coef. Urban  : -0.074 <br>Coef. Murder : 0.049 <br>Coef. Intercept : 4.355","<b> bootstrap dataset:  332 <\/b> <br>Coef. Urban  : -0.023 <br>Coef. Murder : 0.049 <br>Coef. Intercept : 1.129","<b> bootstrap dataset:  333 <\/b> <br>Coef. Urban  : -0.022 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 2.392","<b> bootstrap dataset:  334 <\/b> <br>Coef. Urban  : -0.034 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 2.258","<b> bootstrap dataset:  335 <\/b> <br>Coef. Urban  : -0.086 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 6.722","<b> bootstrap dataset:  336 <\/b> <br>Coef. Urban  : -0.012 <br>Coef. Murder : 0.035 <br>Coef. Intercept : 2.604","<b> bootstrap dataset:  337 <\/b> <br>Coef. Urban  : -0.043 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 2.85","<b> bootstrap dataset:  338 <\/b> <br>Coef. Urban  : -0.028 <br>Coef. Murder : 0.034 <br>Coef. Intercept : 4.119","<b> bootstrap dataset:  339 <\/b> <br>Coef. Urban  : -0.059 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 4.509","<b> bootstrap dataset:  340 <\/b> <br>Coef. Urban  : -0.068 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 4.952","<b> bootstrap dataset:  341 <\/b> <br>Coef. Urban  : -0.022 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 3.083","<b> bootstrap dataset:  342 <\/b> <br>Coef. Urban  : -0.071 <br>Coef. Murder : 0.048 <br>Coef. Intercept : 5.224","<b> bootstrap dataset:  343 <\/b> <br>Coef. Urban  : -0.038 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 2.073","<b> bootstrap dataset:  344 <\/b> <br>Coef. Urban  : -0.028 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 2.691","<b> bootstrap dataset:  345 <\/b> <br>Coef. Urban  : 0.01 <br>Coef. Murder : 0.04 <br>Coef. Intercept : -0.019","<b> bootstrap dataset:  346 <\/b> <br>Coef. Urban  : -0.037 <br>Coef. Murder : 0.038 <br>Coef. Intercept : 4.275","<b> bootstrap dataset:  347 <\/b> <br>Coef. Urban  : -0.073 <br>Coef. Murder : 0.038 <br>Coef. Intercept : 6.088","<b> bootstrap dataset:  348 <\/b> <br>Coef. Urban  : -0.061 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 3.891","<b> bootstrap dataset:  349 <\/b> <br>Coef. Urban  : -0.027 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 2.693","<b> bootstrap dataset:  350 <\/b> <br>Coef. Urban  : -0.075 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 5.13","<b> bootstrap dataset:  351 <\/b> <br>Coef. Urban  : -0.063 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 3.665","<b> bootstrap dataset:  352 <\/b> <br>Coef. Urban  : -0.05 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 4.311","<b> bootstrap dataset:  353 <\/b> <br>Coef. Urban  : -0.046 <br>Coef. Murder : 0.048 <br>Coef. Intercept : 2.859","<b> bootstrap dataset:  354 <\/b> <br>Coef. Urban  : -0.05 <br>Coef. Murder : 0.05 <br>Coef. Intercept : 2.925","<b> bootstrap dataset:  355 <\/b> <br>Coef. Urban  : -0.025 <br>Coef. Murder : 0.038 <br>Coef. Intercept : 3.164","<b> bootstrap dataset:  356 <\/b> <br>Coef. Urban  : -0.056 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 3.731","<b> bootstrap dataset:  357 <\/b> <br>Coef. Urban  : -0.025 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 1.949","<b> bootstrap dataset:  358 <\/b> <br>Coef. Urban  : -0.008 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 1.111","<b> bootstrap dataset:  359 <\/b> <br>Coef. Urban  : -0.037 <br>Coef. Murder : 0.033 <br>Coef. Intercept : 4.409","<b> bootstrap dataset:  360 <\/b> <br>Coef. Urban  : -0.036 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 3.407","<b> bootstrap dataset:  361 <\/b> <br>Coef. Urban  : -0.044 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 3.081","<b> bootstrap dataset:  362 <\/b> <br>Coef. Urban  : -0.04 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 2.625","<b> bootstrap dataset:  363 <\/b> <br>Coef. Urban  : -0.037 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 3.182","<b> bootstrap dataset:  364 <\/b> <br>Coef. Urban  : -0.06 <br>Coef. Murder : 0.048 <br>Coef. Intercept : 3.783","<b> bootstrap dataset:  365 <\/b> <br>Coef. Urban  : -0.035 <br>Coef. Murder : 0.052 <br>Coef. Intercept : 1.707","<b> bootstrap dataset:  366 <\/b> <br>Coef. Urban  : -0.001 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 0.465","<b> bootstrap dataset:  367 <\/b> <br>Coef. Urban  : -0.054 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 4.101","<b> bootstrap dataset:  368 <\/b> <br>Coef. Urban  : -0.035 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 3.423","<b> bootstrap dataset:  369 <\/b> <br>Coef. Urban  : -0.016 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 1.668","<b> bootstrap dataset:  370 <\/b> <br>Coef. Urban  : -0.058 <br>Coef. Murder : 0.048 <br>Coef. Intercept : 3.168","<b> bootstrap dataset:  371 <\/b> <br>Coef. Urban  : 0.02 <br>Coef. Murder : 0.037 <br>Coef. Intercept : 0.085","<b> bootstrap dataset:  372 <\/b> <br>Coef. Urban  : -0.083 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 6.51","<b> bootstrap dataset:  373 <\/b> <br>Coef. Urban  : -0.057 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 3.792","<b> bootstrap dataset:  374 <\/b> <br>Coef. Urban  : -0.026 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 1.446","<b> bootstrap dataset:  375 <\/b> <br>Coef. Urban  : -0.083 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 5.704","<b> bootstrap dataset:  376 <\/b> <br>Coef. Urban  : -0.069 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 4.559","<b> bootstrap dataset:  377 <\/b> <br>Coef. Urban  : -0.038 <br>Coef. Murder : 0.036 <br>Coef. Intercept : 3.7","<b> bootstrap dataset:  378 <\/b> <br>Coef. Urban  : 0.002 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 0.028","<b> bootstrap dataset:  379 <\/b> <br>Coef. Urban  : -0.091 <br>Coef. Murder : 0.05 <br>Coef. Intercept : 5.071","<b> bootstrap dataset:  380 <\/b> <br>Coef. Urban  : -0.053 <br>Coef. Murder : 0.051 <br>Coef. Intercept : 2.742","<b> bootstrap dataset:  381 <\/b> <br>Coef. Urban  : -0.028 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 1.838","<b> bootstrap dataset:  382 <\/b> <br>Coef. Urban  : -0.024 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 2.129","<b> bootstrap dataset:  383 <\/b> <br>Coef. Urban  : -0.07 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 4.997","<b> bootstrap dataset:  384 <\/b> <br>Coef. Urban  : -0.083 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 5.48","<b> bootstrap dataset:  385 <\/b> <br>Coef. Urban  : -0.043 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 2.803","<b> bootstrap dataset:  386 <\/b> <br>Coef. Urban  : -0.036 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 3.482","<b> bootstrap dataset:  387 <\/b> <br>Coef. Urban  : -0.06 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 4.708","<b> bootstrap dataset:  388 <\/b> <br>Coef. Urban  : -0.03 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 2.26","<b> bootstrap dataset:  389 <\/b> <br>Coef. Urban  : -0.061 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 3.308","<b> bootstrap dataset:  390 <\/b> <br>Coef. Urban  : -0.039 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 2.708","<b> bootstrap dataset:  391 <\/b> <br>Coef. Urban  : -0.047 <br>Coef. Murder : 0.038 <br>Coef. Intercept : 4.011","<b> bootstrap dataset:  392 <\/b> <br>Coef. Urban  : -0.048 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 3.755","<b> bootstrap dataset:  393 <\/b> <br>Coef. Urban  : -0.014 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 0.776","<b> bootstrap dataset:  394 <\/b> <br>Coef. Urban  : -0.08 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 6.179","<b> bootstrap dataset:  395 <\/b> <br>Coef. Urban  : -0.057 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 3.31","<b> bootstrap dataset:  396 <\/b> <br>Coef. Urban  : -0.08 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 5.059","<b> bootstrap dataset:  397 <\/b> <br>Coef. Urban  : -0.044 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 3.276","<b> bootstrap dataset:  398 <\/b> <br>Coef. Urban  : -0.07 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 3.803","<b> bootstrap dataset:  399 <\/b> <br>Coef. Urban  : -0.032 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 3.329"],"hoverinfo":["text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text"],"showlegend":false,"marker":{"color":"rgba(0, 0, 0, 0.5)","line":{"color":"rgba(31,119,180,1)"}},"type":"scatter","error_y":{"color":"rgba(31,119,180,1)"},"error_x":{"color":"rgba(31,119,180,1)"},"line":{"color":"rgba(31,119,180,1)"},"xaxis":"x","yaxis":"y","frame":null}],"highlight":{"on":"plotly_click","persistent":false,"dynamic":false,"selectize":false,"opacityDim":0.20000000000000001,"selected":{"opacity":1},"debounce":0},"shinyEvents":["plotly_hover","plotly_click","plotly_selected","plotly_relayout","plotly_brushed","plotly_brushing","plotly_clickannotation","plotly_doubleclick","plotly_deselect","plotly_afterplot","plotly_sunburstclick"],"base_url":"https://plot.ly"},"evals":[],"jsHooks":[]}</script>
```

**Hypothesis Testing**
We can also use an $F$ test for any $q$ hypotheses. Specifically, when $q$ hypotheses *restrict* a model, the degrees of freedom drop from $k_{u}$ to $k_{r}$ and the residual sum of squares $RSS=\sum_{i}(y_{i}-\widehat{y}_{i})^2$ typically increases. We compute the statistic
$$
F_{q} = \frac{(RSS_{r}-RSS_{u})/(k_{u}-k_{r})}{RSS_{u}/(N-k_{u})}.
$$
When the restricted model is a simple intercept, $F_{q}$ can also be written in terms of $R^2$ or adjusted $R^2$. For some intuition on hypothesis testing, we examine how the $R^2$ statistic varies with bootstrap samples. Specifically, compute a null $R^2$ distribution by randomly reshuffling the outcomes and compare it to the observed $R^2$.

``` r
# Bootstrap NULL
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

hist(R2adj_sim0, xlim=c(-.1,1), breaks=25, border=NA,
    main='', xlab=expression('adj.'~R[b]^2))
abline(v=summary(reg)$adj.r.squared, lwd=2, col=2)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-26-1.png" width="672" />

Under some additional assumptions $F_{q}$ follows an F-distribution. Note that *hypothesis testing is not to be done routinely*, as complications arise when testing multiple hypothesis sequentially.

For more about F-testing, see https://online.stat.psu.edu/stat501/lesson/6/6.2 and https://www.econometrics.blog/post/understanding-the-f-statistic/

## Factor Variables

So far, we have discussed cardinal data where the difference between units always means the same thing: e.g., $4-3=2-1$. There are also factor variables

* Ordered: refers to Ordinal data. The difference between units means something, but not always the same thing. For example, $4th - 3rd \neq 2nd - 1st$.
* Unordered: refers to Categorical data. The difference between units is meaningless. For example, $B-A=?$

To analyze either factor, we often convert them into indicator variables or dummies; $D_{c}=\mathbf{1}( Factor = c)$. One common case is if you have observations of individuals over time periods, then you may have two factor variables. An unordered factor that indicates who an individual is; for example $D_{i}=\mathbf{1}( Individual = i)$, and an order factor that indicates the time period; for example $D_{t}=\mathbf{1}( Time \in [month~ t, month~ t+1) )$. There are many other cases you see factor variables, including spatial ID's in purely cross sectional data.

Be careful not to handle categorical data as if they were cardinal. E.g., generate city data with Leipzig=1, Lausanne=2, LosAngeles=3, ... and then include city as if it were a cardinal number (that's a big no-no). The same applied to ordinal data; PopulationLeipzig=2, PopulationLausanne=3, PopulationLosAngeles=1.


``` r
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
y_{it} = x_{it} \beta_{x} + d_{t}\beta_{t}
$$
When, as commonly done, the factors are modeled as being additively seperable, they are modeled "fixed effects".^[There are also *random effects*: the factor variable comes from a distribution that is uncorrelated with the regressors. This is rarely used in economics today, however, and are mostly included for historical reasons and special cases where fixed effects cannot be estimated due to data limitations.]
Simply including the factors into the OLS regression yields a "dummy variable" fixed effects estimator.
**Hansen Econometrics, Theorem 17.1:** The fixed effects estimator of $\beta$ algebraically equals the dummy variable estimator of $\beta$. The two estimators have the same residuals.
<!--
In fact, if the fixed effect is ``fully unstructured then the only way to consistently estimate the coefficient $\beta$ is by an estimator which is invariant'' (Hansen Econometrics, p). 
-->

``` r
library(fixest)
fe_reg1 <- feols(y~x|fo+fu, dat_f)
coef(fe_reg1)
```

```
##         x 
## 0.7231942
```

``` r
fixef(fe_reg1)[1:2]
```

```
## $fo
##        0        1        2        3        4 
## 10.85695 12.30108 16.92056 25.31370 43.68604 
## 
## $fu
##         A         B 
##   0.00000 -23.26345
```

``` r
# Compare Coefficients
fe_reg0 <- lm(y~-1+x+fo+fu, dat_f)
coef( fe_reg0 )
```

```
##           x         fo0         fo1         fo2         fo3         fo4 
##   0.7231942  10.8569549  12.3010794  16.9205577  25.3136951  43.6860361 
##         fuB 
## -23.2634455
```

With fixed effects, we can also compute averages for each group and construct a *between estimator*: $\overline{y}_i = \alpha + \overline{x}_i \beta$. Or we can subtract the average from each group to construct a *within estimator*: $(y_{it} - \overline{y}_i) = (x_{it}-\overline{x}_i)\beta$. 

But note that many factors are not additively separable. This is easy to check with an F-test;

``` r
reg0 <- lm(y~-1+x+fo+fu, dat_f)
reg1 <- lm(y~-1+x+fo*fu, dat_f)
reg2 <- lm(y~-1+x*fo*fu, dat_f)

anova(reg0, reg2)
```

```
## Analysis of Variance Table
## 
## Model 1: y ~ -1 + x + fo + fu
## Model 2: y ~ -1 + x * fo * fu
##   Res.Df   RSS Df Sum of Sq      F    Pr(>F)    
## 1    993 84973                                  
## 2    980  6340 13     78634 935.04 < 2.2e-16 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
```

``` r
anova(reg0, reg1, reg2)
```

```
## Analysis of Variance Table
## 
## Model 1: y ~ -1 + x + fo + fu
## Model 2: y ~ -1 + x + fo * fu
## Model 3: y ~ -1 + x * fo * fu
##   Res.Df   RSS Df Sum of Sq        F    Pr(>F)    
## 1    993 84973                                    
## 2    989 11875  4     73099 2824.963 < 2.2e-16 ***
## 3    980  6340  9      5535   95.072 < 2.2e-16 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
```




<!-- 
> The labels "random effects" and "fixed effects" are misleading. These are labels which arose in the early literature and we are stuck with these labels today. In a previous era regressors were viewed as "fixed". Viewing the individual effect as an unobserved regressor leads to the label of the individual effect as "fixed". Today, we rarely refer to regressors as "fixed" when dealing with observational data. We view all variables as random. Consequently describing u i as "fixed" does not make much sense and it is hardly a contrast with the "random effect" label since under either assumption u i is treated as random. Once again, the labels are unfortunate but the key difference is whether u i is correlated with the regressors.
-->


**Break Points**
Kinks and Discontinuities in $X$ can also be modeled using factor variables. As such, $F$-tests can be used to examine whether a breaks is statistically significant.

``` r
library(AER); data(CASchools)
CASchools$score <- (CASchools$read + CASchools$math) / 2
reg <- lm(score~income, data=CASchools)

# F Test for Break
reg2 <- lm(score ~ income*I(income>15), data=CASchools)
anova(reg, reg2)

# Chow Test for Break
data_splits <- split(CASchools, CASchools$income <= 15)
resids <- sapply(data_splits, function(dat){
    reg <- lm(score ~ income, data=dat)
    sum( resid(reg)^2)
})
Ns <-  sapply(data_splits, function(dat){ nrow(dat)})
Rt <- (sum(resid(reg)^2) - sum(resids))/sum(resids)
Rb <- (sum(Ns)-2*reg$rank)/reg$rank
Ft <- Rt*Rb
pf(Ft,reg$rank, sum(Ns)-2*reg$rank,lower.tail=F)

# See also
# strucchange::sctest(y~x, data=xy, type="Chow", point=.5)
# strucchange::Fstats(y~x, data=xy)

# To Find Changes
# segmented::segmented(reg)
```


## Coefficient Interpretation

Notice that we have gotten pretty far without actually trying to meaningfully interpret regression coefficients. That is because the above procedure will always give us number, regardless as to whether the true data generating process is linear or not. So, to be cautious, we have been interpreting the regression outputs while being agnostic as to how the data are generated. We now consider a special situation where we know the data are generated according to a linear process and are only uncertain about the parameter values.

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

``` r
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
##  10.2626877   1.7491886  -0.3389693
```

Simulate the distribution of coefficients under a correctly specified model. Interpret the average.

``` r
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
    hist(Coefs[i,], xlab=bquote(beta[.(i)]), main='', border=NA)
    abline(v=mean(Coefs[i,]), lwd=2)
    abline(v=B[i], col=rgb(1,0,0))
}
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-32-1.png" width="672" />


Many economic phenomena are nonlinear, even when including potential transforms of $Y$ and $X$. Sometimes the linear model may still be a good or even great approximation. But sometimes not, and it is hard to know ex-ante. Examine the distribution of coefficients under this mispecified model and try to interpret the average.

``` r
N <- 30

Coefs <- sapply(1:600, function(sim){
    x2 <- runif(N, 0, 5)
    x3 <- rbinom(N,1,.7)
    e <- rnorm(N,0,3)
    Y <- 10*x3 + 2*log(x2)^x3 + e
    dat <- data.frame(Y,x2,x3)
    coef(lm(Y~x2+x3, data=dat))
})

par(mfrow=c(1,2))
for(i in 2:3){
    hist(Coefs[i,],  xlab=bquote(beta[.(i)]), main='', border=NA)
    abline(v=mean(Coefs[i,]), col=1, lwd=2)
}
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-33-1.png" width="672" />
In general, you can interpret your regression coefficients as "conditional correlations". If further hypothesis testing suggests the relationships are actually additively separable and linear, then you also have the structural interpretation of "marginal effect".


## Transformations

Transforming variables can often improve your model fit while still allowing it estimated via OLS. This is because OLS only requires the model to be linear in the parameters. Under the assumptions of the model is correctly specified, the following table is how we can interpret the coefficients of the transformed data. (Note for small changes, $\Delta ln(x) \approx \Delta x / x = \Delta x \% \cdot 100$.)

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
[ \widehat{y}_{i}^{(\lambda)} \cdot \lambda ]^{1/\lambda} -1 & \lambda  \neq 0 \\
exp( \widehat{y}_{i}^{(\lambda)}) -1 &  \lambda=0
\end{cases}.
$$


It is easiest to optimize parameters in a 2-step procedure called  `concentrated optimization'. We first solve for $\widehat{\beta}(\rho,\lambda)$ and compute the mean squared error $MSE(\rho,\lambda)$. We then find the $(\rho,\lambda)$ which minimizes $MSE$.

``` r
# Box-Cox Transformation Function
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

# Which Variables
reg <- lm(Murder~Assault+UrbanPop, data=USArrests)
X <- USArrests[,c('Assault','UrbanPop')]
Y <- USArrests[,'Murder']

# Simple Grid Search over potential (Rho,Lambda) 
rl_df <- expand.grid(rho=seq(-2,2,by=.5),lambda=seq(-2,2,by=.5))

# Compute Mean Squared Error
# from OLS on Transformed Data
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

# Want Small MSE and Interpretable
layout(matrix(1:2,ncol=2), width=c(3,1), height=c(1,1))
par(mar=c(4,4,2,0))
plot(lambda~rho,rl_df, cex=8, pch=15,
    xlab=expression(rho),
    ylab=expression(lambda),
    col=hcl.colors(25)[cut(1/rl_df$mse,25)])
# Which min
rl0 <- rl_df[which.min(rl_df$mse),c('rho','lambda')]
points(rl0$rho, rl0$lambda, pch=0, col=1, cex=8, lwd=2)
# Legend
plot(c(0,2),c(0,1), type='n', axes=F,
    xlab='',ylab='', cex.main=.8,
    main=expression(frac(1,'Mean Square Error')))
rasterImage(as.raster(matrix(hcl.colors(25), ncol=1)), 0, 0, 1,1)
text(x=1.5, y=seq(1,0,l=10), cex=.5,
    labels=levels(cut(1/rl_df$mse,10)))
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-34-1.png" width="960" style="display: block; margin: auto;" />

The parameters $-1,0,1,2$ are easy to interpret and might be selected instead if there is only a small loss in fit. (In the above example, we might choose $\lambda=0$ instead of the $\lambda$ which minimized the mean square error). You can also plot the specific predictions to better understand the effect of data  transformation beyond mean squared error.


``` r
# Plot for Specific Comparisons
Xr <- bxcx(X,rl0[[1]])
Yr <- bxcx(Y,rl0[[2]])
Datr <- cbind(Murder=Yr,Xr)
Regr <- lm(Murder~Assault+UrbanPop, data=Datr)
Predr <- bxcx_inv(predict(Regr),rl0[[2]])

cols <- c(rgb(1,0,0,.5), col=rgb(0,0,1,.5))
plot(Y, Predr, pch=16, col=cols[1], ylab='Prediction', 
    ylim=range(Y,Predr))
points(Y, predict(reg), pch=16, col=cols[2])
legend('topleft', pch=c(16), col=cols,
    title=expression(rho~', '~lambda),
    legend=c(  paste0(rl0, collapse=', '),'1, 1') )
abline(a=0,b=1, lty=2)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-35-1.png" width="672" />

When explicitly transforming data according to $\lambda$ and $\rho$, these parameters increase the degrees of freedom by two. The default hypothesis testing procedures do not account for you trying out different transformations, and should be adjusted by the increased degrees of freedom. Specification searches deflate standard errors and are a major source for false discoveries.

##  Diagnostics

There's little sense in getting great standard errors for a terrible model. Plotting your regression object a simple and easy step to help diagnose whether your model is in some way bad. We next go through what each of these figures show.

``` r
reg <- lm(Murder~Assault+UrbanPop, data=USArrests)
par(mfrow=c(2,2))
plot(reg, pch=16, col=grey(0,.5))
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-36-1.png" width="960" style="display: block; margin: auto;" />



**Outliers** 
The first diagnostic plot examines outliers in terms the outcome $y_i$ being far from its prediction $\hat{y}_i$. You may be interested in such outliers because they can (but do not have to) unduly influence your estimates. 

The third diagnostic plot examines another type of outlier, where an observation with the explanatory variable $x_i$ is far from the center of mass of the other $x$'s. A point has high *leverage* if the estimates change dramatically when you estimate the model without that data point.

``` r
N <- 40
x <- c(25, runif(N-1,3,8))
e <- rnorm(N,0,0.4)
y <- 3 + 0.6*sqrt(x) + e
plot(y~x, pch=16, col=grey(.5,.5))
points(x[1],y[1], pch=16, col=rgb(1,0,0,.5))

abline(lm(y~x), col=2, lty=2)
abline(lm(y[-1]~x[-1]))
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-37-1.png" width="672" />

See [AEJ-leverage](https://www.rwi-essen.de/fileadmin/user_upload/RWI/Publikationen/I4R_Discussion_Paper_Series/032_I4R_Haddad_Kattan_Wochner-updateJune28.pdf) for an example of leverage in economics.

Standardized residuals are
$$
r_i=\frac{\hat{\epsilon}_i}{s_{[i]}\sqrt{1-h_i}},
$$
where $s_{[i]}$ is the root mean squared error of a regression with the $i$th observation removed and $h_i$ is the leverage of residual $\hat{\epsilon_i}$. 

``` r
which.max(hatvalues(reg))
which.max(rstandard(reg))
```

(See https://www.r-bloggers.com/2016/06/leverage-and-influence-in-a-nutshell/ for a good interactive explanation, and https://online.stat.psu.edu/stat462/node/87/ for detail.)

The fourth plot further assesses outlier $X$ using *Cook's Distance*, which sums of all prediction changes when observation i is removed and scales proportionally to the mean square error $s^2 = \frac{\sum_{i} (e_{i})^2 }{n-K}.
$$
D_{i} = \frac{\sum_{j} \left( \hat{y_j} - \hat{y_j}_{[i]} \right)^2 }{ p s^2 }
= \frac{[e_{i}]^2}{p s^2 } \frac{h_i}{(1-h_i)^2}$$

``` r
which.max(cooks.distance(reg))
car::influencePlot(reg)
```


**Normality**
The second plot examines whether the residuals are normally distributed. OLS point estimates do not depend on the normality of the residuals. (Good thing, because there's no reason the residuals of economic phenomena should be so well behaved.) Many hypothesis tests are, however, affected by the distribution of the residuals. For these reasons, you may be interested in assessing normality 

``` r
par(mfrow=c(1,2))
hist(resid(reg), main='Histogram of Residuals',
    font.main=1, border=NA)

qqnorm(resid(reg), main="Normal Q-Q Plot of Residuals",
    font.main=1, col=grey(0,.5), pch=16)
qqline(resid(reg), col=1, lty=2)

#shapiro.test(resid(reg))
```

Heterskedasticity may also matters for variability estimates. This is not shown in the plot, but you can conduct a simple test

``` r
library(lmtest)
lmtest::bptest(reg)
```

**Collinearity**
This is when one explanatory variable in a multiple linear regression model can be linearly predicted from the others with a substantial degree of accuracy. Coefficient estimates may change erratically in response to small changes in the model or the data. (In the extreme case where there are more variables than observations $K>N$, the inverse of $X'X$ has an infinite number of solutions.) To diagnose collinearity, we can use the *Variance Inflation Factor*
$$
VIF_{k}=\frac{1}{1-R^2_k},
$$
where $R^2_k$ is the $R^2$ for the regression of $X_k$ on the other covariates $X_{-k}$ (a regression that does not involve the response variable Y)

``` r
car::vif(reg) 
sqrt(car::vif(reg)) > 2 # problem?
```



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


To derive OLS coefficients in Matrix form, see

* https://jrnold.github.io/intro-methods-notes/ols-in-matrix-form.html
* https://www.fsb.miamioh.edu/lij14/411_note_matrix.pdf
* https://web.stanford.edu/~mrosenfe/soc_meth_proj3/matrix_OLS_NYU_notes.pdf


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


``` r
# Simulate data with an endogeneity issue
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



``` r
# Demand Curve Simulator
qd_fun <- function(p, Ad=8, Bd=-.8, Ed_sigma=.25){
    Qd <- Ad + Bd*p + rnorm(1,0,Ed_sigma)
    return(Qd)
}

# Supply Curve Simulator
qs_fun <- function(p, As=-8, Bs=1, Es_sigma=.25){
    Qs <- As + Bs*p + rnorm(1,0,Es_sigma)
    return(Qs)
}

# Quantity Supplied and Demanded at 3 Prices
cbind(P=8:10, D=qd_fun(8:10), S=qs_fun(8:10))
```

```
##       P          D          S
## [1,]  8  1.3988226 -0.0257466
## [2,]  9  0.5988226  0.9742534
## [3,] 10 -0.2011774  1.9742534
```

``` r
# Market Equilibrium Finder
eq_fun <- function(demand, supply, P){
    # Compute EQ (what we observe)
    eq_id <- which.min( abs(demand-supply) )
    eq <- c(P=P[eq_id], Q=demand[eq_id]) 
    return(eq)
}
```



``` r
# Simulations Parameters
N <- 300 # Number of Market Interactions
P <- seq(5,10,by=.01) # Price Range to Consider

# Generate Data from Competitive Market  
# Plot Underlying Process
plot.new()
plot.window(xlim=c(0,2), ylim=range(P))
EQ1 <- sapply(1:N, function(n){
    # Market Data Generating Process
    demand <- qd_fun(P)
    supply <- qs_fun(P)
    eq <- eq_fun(demand, supply, P)    
    # Plot Theoretical Supply and Demand
	lines(demand, P, col=grey(0,.01))
	lines(supply, P, col=grey(0,.01))
    points(eq[2], eq[1], col=grey(0,.05), pch=16)
    # Save Data
    return(eq)
})
axis(1)
axis(2)
mtext('Quantity',1, line=2)
mtext('Price',2, line=2)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-45-1.png" width="672" />

Now regress quantity ("Y") on price ("X"): $\widehat{\beta}_{OLS} = Cov(Q^{*}, P^{*}) / Var(P^{*})$. You get a number back, but it is hard to interpret meaningfully. 

``` r
# Analyze Market Data
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
## -0.50100 -0.11444 -0.00497  0.13328  0.48994 
## 
## Coefficients:
##             Estimate Std. Error t value Pr(>|t|)
## (Intercept)  0.15596    0.52923   0.295    0.768
## P            0.08450    0.05943   1.422    0.156
## 
## Residual standard error: 0.1848 on 298 degrees of freedom
## Multiple R-squared:  0.006738,	Adjusted R-squared:  0.003405 
## F-statistic: 2.022 on 1 and 298 DF,  p-value: 0.1561
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


``` r
# New Observations After Cost Change
EQ2 <- sapply(1:N, function(n){
    demand <- qd_fun(P)
    supply2 <- qs_fun(P, As=-6.5) # More Supplied at Given Price
    eq <- eq_fun(demand, supply2, P)
    return(eq)
	# lines(supply2, P, col=rgb(0,0,1,.01))
    #points(eq[2], eq[1], col=rgb(0,0,1,.05), pch=16)	
})
dat2 <- data.frame(t(EQ2), cost='2')

# Plot Market Data
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

``` r
# Not exactly right, but at least right sign
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
## -0.67340 -0.15008 -0.01075  0.15479  0.62500 
## 
## Coefficients:
##             Estimate Std. Error t value Pr(>|t|)    
## (Intercept)  6.49925    0.16810   38.66   <2e-16 ***
## P           -0.62184    0.01982  -31.38   <2e-16 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 0.2289 on 598 degrees of freedom
## Multiple R-squared:  0.6221,	Adjusted R-squared:  0.6215 
## F-statistic: 984.5 on 1 and 598 DF,  p-value: < 2.2e-16
```
Although the individual observations are noisy, we can compute the change in the expected values $d \mathbb{E}[Q^{*}] / d \mathbb{E}[P^{*}] =-B_{D}$. Empirically, this is estimated via the change in average value.

``` r
# Wald (1940) Estimate
dat_mean <- rbind(
    colMeans(dat2[dat2$cost==1,1:2]),
    colMeans(dat2[dat2$cost==2,1:2]))
dat_mean
```

```
##             P         Q
## [1,] 8.903567 0.9082715
## [2,] 8.034167 1.5577434
```

``` r
B_est <- diff(dat_mean[,2])/diff(dat_mean[,1])
round(B_est, 2)
```

```
## [1] -0.75
```
We can also seperately recover $d \mathbb{E}[Q^{*}] / d \mathbb{E}[A_{S}]$ and $d \mathbb{E}[P^{*}] / d \mathbb{E}[A_{S}]$ from seperate regressions

``` r
# Heckman (2000, p.58) Estimate
ols_1 <- lm(P~cost, data=dat2)
ols_2 <- lm(Q~cost, data=dat2)
B_est2 <- coef(ols_2)/coef(ols_1)
round(B_est2[[2]],2)
```

```
## [1] -0.75
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


``` r
# Two Stage Least Squares Estimate
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
## -0.49792 -0.11576 -0.01055  0.13228  0.46429 
## 
## Coefficients:
##             Estimate Std. Error t value Pr(>|t|)    
## (Intercept)  7.55954    0.14447   52.33   <2e-16 ***
## Phat        -0.74703    0.01704  -43.85   <2e-16 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 0.1814 on 598 degrees of freedom
## Multiple R-squared:  0.7628,	Adjusted R-squared:  0.7624 
## F-statistic:  1923 on 1 and 598 DF,  p-value: < 2.2e-16
```

``` r
# One Stage Instrumental Variables Estimate
library(fixest)
reg2_iv <- feols(Q~1|P~cost, data=dat2)
summary(reg2_iv)
```

```
## TSLS estimation - Dep. Var.: Q
##                   Endo.    : P
##                   Instr.   : cost
## Second stage: Dep. Var.: Q
## Observations: 600
## Standard-errors: IID 
##              Estimate Std. Error  t value  Pr(>|t|)    
## (Intercept)  7.559544   0.188321  40.1418 < 2.2e-16 ***
## fit_P       -0.747035   0.022208 -33.6386 < 2.2e-16 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## RMSE: 0.236071   Adj. R2: 0.596219
## F-test (1st stage), P: stat = 3,377.2, p < 2.2e-16, on 1 and 598 DoF.
##            Wu-Hausman: stat =   361.1, p < 2.2e-16, on 1 and 597 DoF.
```

**Within Group Variance**
You can experiment with the effect of different variances on both OLS and IV in the code below. And note that if we had multiple supply shifts and recorded their magnitudes, then we could recover more information about demand, perhaps tracing it out entirely.

``` r
# Examine
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
## Ed_sigma.0.25           -0.61         -0.62      -0.74
## Ed_sigma.1               0.38          0.35      -0.05
## 
## [[2]]
##                Es_sigma.0.001 Es_sigma.0.25 Es_sigma.1
## Ed_sigma.0.001          -0.80         -0.80      -0.80
## Ed_sigma.0.25           -0.78         -0.79      -0.81
## Ed_sigma.1              -0.78         -0.79      -0.77
```




**Caveats** 
Regression analysis with instrumental variables can be very insightful and is applied to many different areas. But I also want to stress some caveats about using IV in practice.

We always get coefficients back when running `feols`, and sometimes the computed p-values are very small. The interpretation of those numbers rests on many assumptions:

* only supply was affected (Instrument exogeneity)
* the shock is large enough to be picked up statistically (Instrument relevance)
* supply and demand are linear and additively seperable (Functional form)
* we were not cycling through different IV's (Multiple hypotheses)

We are rarely sure that all of these assumptions hold, and this is one reason why researchers often also report their OLS results.

In practice, it is hard to find a good instrument. For example, suppose we asked "what is the effect of wages on police demanded?" and examined a policy which lowered the educational requirements from 4 years to 2 to become an officer. This increases the labour supply, but it also affects the demand curve through "general equilibrium": as some of the new officers were potentially criminals. With fewer criminals, the demand for likely police shifts down.

In practice, it is also easy to find a bad instrument. Paradoxically, IV's are something you are supposed to find but never search for. As you search for good instruments, sometimes random noise will appear like a good instrument (Spurious instruments). Worse, if you search for a good instrument for too long, you can also be led astray from important questions.






## Regression Discontinuities/Kink (RD/RK)

The basic idea here is to examine how a variable changes in response to an exogenous shock. The Regression Discontinuities estimate of the cost shock is the difference in the outcome variable just before and just after the shock. We now turn to our canonical competitive market example. The RD estimate is the difference between the lines at $T=300$.


``` r
dat2$T <- 1:nrow(dat2)

plot(P~T, dat2, main='Effect of Cost Shock on Price', 
    font.main=1, pch=16, col=grey(0,.25))
regP1 <- lm(P~T, dat2[dat2$cost==1,]) 
lines(regP1$model$T, predict(regP1), col=2)
regP2 <- lm(P~T, dat2[dat2$cost==2,]) 
lines(regP2$model$T, predict(regP2), col=4)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-54-1.png" width="672" />

``` r
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
## -0.52661 -0.11675 -0.00173  0.12361  0.56931 
## 
## Coefficients:
##               Estimate Std. Error t value Pr(>|t|)    
## (Intercept)  8.923e+00  2.118e-02 421.327   <2e-16 ***
## T           -1.295e-04  1.220e-04  -1.062    0.289    
## cost2       -7.993e-01  5.983e-02 -13.360   <2e-16 ***
## T:cost2     -6.934e-05  1.725e-04  -0.402    0.688    
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 0.183 on 596 degrees of freedom
## Multiple R-squared:  0.8505,	Adjusted R-squared:  0.8498 
## F-statistic:  1130 on 3 and 596 DF,  p-value: < 2.2e-16
```


``` r
plot(Q~T, dat2, main='Effect of Cost Shock on Quantity',
    font.main=1, pch=16, col=grey(0,.15))
regQ1 <- lm(Q~T, dat2[dat2$cost==1,]) 
lines(regQ1$model$T, predict(regQ1), col=2)
regQ2 <- lm(Q~T, dat2[dat2$cost==2,]) 
lines(regQ2$model$T, predict(regQ2), col=4)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-55-1.png" width="672" />

``` r
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
## -0.51266 -0.11610 -0.01001  0.12799  0.47197 
## 
## Coefficients:
##               Estimate Std. Error t value Pr(>|t|)    
## (Intercept)  0.8919619  0.0209527  42.570   <2e-16 ***
## T            0.0001084  0.0001207   0.898    0.370    
## cost2        0.7720946  0.0591893  13.044   <2e-16 ***
## T:cost2     -0.0003444  0.0001707  -2.018    0.044 *  
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 0.181 on 596 degrees of freedom
## Multiple R-squared:  0.7646,	Adjusted R-squared:  0.7634 
## F-statistic: 645.3 on 3 and 596 DF,  p-value: < 2.2e-16
```

Remember that this is effect is *local*: different magnitudes of the cost shock or different demand curves generally yeild different estimates.

## Difference in Differences (DID)

The basic idea here is to examine how a variable changes in response to an exogenous shock, *compared to a control group*. 


``` r
EQ3 <- sapply(1:(2*N), function(n){

    # Market Mechanisms
    demand <- qd_fun(P)
    supply <- qs_fun(P)

    # Compute EQ (what we observe)
    eq_id <- which.min( abs(demand-supply) )
    eq <- c(P=P[eq_id], Q=demand[eq_id]) 

    # Return Equilibrium Observations
    return(eq)
})
dat3 <- data.frame(t(EQ3), cost='1', T=1:ncol(EQ3))


par(mfrow=c(1,2))
plot(P~T, dat2, main='Effect of Cost Shock on Price',
    font.main=1, pch=17,col=rgb(0,0,1,.25))
points(P~T, dat3, pch=16, col=rgb(1,0,0,.25))

plot(Q~T, dat2, main='Effect of Cost Shock on Quantity',
    font.main=1, pch=17,col=rgb(0,0,1,.25))
points(Q~T, dat3, pch=16, col=rgb(1,0,0,.25))
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-56-1.png" width="672" />

``` r
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
## -0.57218 -0.12977 -0.00373  0.12379  0.57565 
## 
## Coefficients:
##               Estimate Std. Error t value Pr(>|t|)    
## (Intercept)  8.900e+00  1.133e-02 785.357   <2e-16 ***
## T           -3.569e-05  3.772e-05  -0.946    0.344    
## cost2       -7.761e-01  5.850e-02 -13.266   <2e-16 ***
## T:cost2     -1.632e-04  1.307e-04  -1.249    0.212    
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 0.1877 on 1196 degrees of freedom
## Multiple R-squared:  0.7969,	Adjusted R-squared:  0.7964 
## F-statistic:  1564 on 3 and 1196 DF,  p-value: < 2.2e-16
```

``` r
regQ <- lm(Q~T*cost, dat)
summary(regQ)
```

```
## 
## Call:
## lm(formula = Q ~ T * cost, data = dat)
## 
## Residuals:
##     Min      1Q  Median      3Q     Max 
## -0.5077 -0.1251 -0.0032  0.1284  0.5505 
## 
## Coefficients:
##               Estimate Std. Error t value Pr(>|t|)    
## (Intercept)  9.053e-01  1.088e-02  83.177   <2e-16 ***
## T           -1.276e-05  3.623e-05  -0.352   0.7247    
## cost2        7.588e-01  5.619e-02  13.504   <2e-16 ***
## T:cost2     -2.232e-04  1.255e-04  -1.779   0.0755 .  
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 0.1802 on 1196 degrees of freedom
## Multiple R-squared:  0.7137,	Adjusted R-squared:  0.713 
## F-statistic: 993.8 on 3 and 1196 DF,  p-value: < 2.2e-16
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

<!---
''torture the data (to) confess'' (Coase,  Essays on economics and economists.  1995, p. 27)
--->

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

``` r
set.seed(123)
n <- 50
X1 <- runif(n)

# Regression Machine:
# repeatedly finds covariate, runs regression
# stops when statistically significant at .1%

p <- 1
i <- 0
while(p >= .001){ 
    # Get Random Covariate
    X2 <-  runif(n)
    # Merge and `Analyze'
    dat_i <- data.frame(X1,X2)
    reg_i <- lm(X1~X2, data=dat_i)
    # update results in global environment
    p <- summary(reg_i)$coefficients[2,4]
    i <- i+1
}

plot(X1~X2, data=dat_i,
    pch=16, col=grey(.5,.5), font.main=1,
    main=paste0('Random Dataset ', i,":   p=",
        formatC(p,digits=2, format='fg')))
abline(reg_i)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-57-1.png" width="672" />

``` r
#summary(reg_i)
```



``` r
# P-hacking 2SLS
library(fixest)
p <- 1
ii <- 0
set.seed(123)
while(p >= .05){
    # Get Random Covariates
    X2 <-  runif(n)    
    X3 <-  runif(n)
    # Create Treatment Variable based on Cutoff
    cutoffs <- seq(0,1,length.out=11)[-c(1,11)]
    for(tau in cutoffs){
        T3 <- 1*(X3 > tau)
        # Merge and `Analyze'
        dat_i <- data.frame(X1,X2,T3)
        ivreg_i <- feols(X1~1|X2~T3, data=dat_i)
        # Update results in global environment
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
## TSLS estimation - Dep. Var.: X1
##                   Endo.    : X2
##                   Instr.   : T3
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

``` r
# Your data is not made up in the computer (hopefully!)
vigen_csv <- read.csv( paste0(
'https://raw.githubusercontent.com/the-mad-statter/',
'whysospurious/master/data-raw/tylervigen.csv') ) 
class(vigen_csv)
```

```
## [1] "data.frame"
```

``` r
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

``` r
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

``` r
# similar `apply' functions
lapply(vigen_csv[,1:5], class) # like apply, but for lists
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

``` r
sapply(vigen_csv[,1:5], class) # lapply, formatted to a vector
```

```
##                year    science_spending    hanging_suicides pool_fall_drownings 
##           "integer"           "integer"           "integer"           "integer" 
##          cage_films 
##           "integer"
```

The US government spending on science is ruining cinema
(p<.001)!?


``` r
# Drop Data before 1999
vigen_csv <- vigen_csv[vigen_csv$year >= 1999,] 

# Run OLS Regression
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


``` r
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

Some other great examples

``` r
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


``` r
# Include an intercept to regression 1
#reg2 <-  lm(cage_films ~ science_spending, data=vigen_csv)
#suppressMessages(library(stargazer))
#stargazer(reg1, reg2, type='html')
```

**The same principles apply to regression-based approaches to endogeneity issues**
For example, we now run IV regressions for different variable combinations in the dataset of spurious relationships

``` r
knames <- names(vigen_csv)[2:11] # First 10 Variables
#knames <- names(vigen_csv)[-1] # Try All Variables
p <- 1
ii <- 1
ivreg_list <- vector("list", factorial(length(knames))/factorial(length(knames)-3))

# Choose 3 variable
for( k1 in knames){
for( k2 in setdiff(knames,k1)){
for( k3 in setdiff(knames,c(k1,k2)) ){   
    X1 <- vigen_csv[,k1]
    X2 <- vigen_csv[,k2]
    X3 <- vigen_csv[,k3]
    # Merge and `Analyze'        
    dat_i <- na.omit(data.frame(X1,X2,X3))
    ivreg_i <- feols(X1~1|X2~X3, data=dat_i)
    ivreg_list[[ii]] <- list(ivreg_i, c(k1,k2,k3))
    ii <- ii+1
}}}
pvals <- sapply(ivreg_list, function(ivreg_i){ivreg_i[[1]]$coeftable[2,4]})

plot(ecdf(pvals), xlab='p-value', ylab='CDF', font.main=1,
    main='Frequency IV is Statistically Significant')
abline(v=c(.01,.05), col=c(2,4))
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-64-1.png" width="672" />

``` r
# Most Significant Spurious Combinations
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



``` r
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

``` r
# "Find" "valid" ingredients
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
## TSLS estimation - Dep. Var.: X1
##                   Endo.    : X2
##                   Instr.   : X3
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

``` r
# After experimenting with different instruments
# you can find even stronger results!
```


**RDD**
Second, find a large discrete change in the data that you can associate with a policy. You can use this as an instrument too, also providing a causal estimate of $X_{2}$ on $X_{1}$.



``` r
# Let the data take shape
# (around the large differences before and after)
n1 <- 290
wind1 <- c(n1-300,n1+300)
dat1 <- data.frame(t=n_index, y=random_walk1, d=1*(n_index > n1))
dat1_sub <- dat1[ n_index>wind1[1] & n_index < wind1[2],]

# Then find your big break
reg0 <- lm(y~t, data=dat1_sub[dat1_sub$d==0,])
reg1 <- lm(y~t, data=dat1_sub[dat1_sub$d==1,])

# The evidence should show openly (it's just science)
plot(random_walk1, pch=16, col=rgb(0,0,1,.25),
    xlim=wind1, xlab='Time', ylab='Random Value')
abline(v=n1, lty=2)
lines(reg0$model$t, reg0$fitted.values, col=1)
lines(reg1$model$t, reg1$fitted.values, col=1)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-67-1.png" width="672" />


``` r
# Dress with some statistics for added credibility
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


``` r
# Find a reversal of fortune
# (A good story always goes well with a nice pre-trend)
n2 <- 318
wind2 <- c(n2-20,n2+20)
plot(random_walk2, pch=16, col=rgb(0,0,1,.5),
    xlim=wind2, ylim=c(-15,15), xlab='Time', ylab='Random Value')
points(random_walk1, pch=16, col=rgb(1,0,0,.5))
abline(v=n2, lty=2)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-69-1.png" width="672" />


``` r
# Knead out any effects that are non-causal (aka correlation)
dat2A <- data.frame(t=n_index, y=random_walk1, d=1*(n_index > n2), RWid=1)
dat2B <- data.frame(t=n_index, y=random_walk2, d=0, RWid=2)
dat2  <- rbind(dat2A, dat2B)
dat2$RWid <- as.factor(dat2$RWid)
dat2$tid <- as.factor(dat2$t)
dat2_sub <- dat2[ dat2$t>wind2[1] & dat2$t < wind2[2],]

# Report the stars for all to enjoy
# (what about the intercept?)
# (stable coefficients are the good ones?)
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
