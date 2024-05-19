# (PART) Linear Regression in R {-} 

This section is a quick overview of linear regression models from the perspective that ``all models are wrong, but some are useful''. All models are estimated via  Ordinary Least Squares (OLS). For more in-depth introductions, which typically begin by assuming the true data generating process is linear, see https://jadamso.github.io/Rbooks/ordinary-least-squares.html#more-literature. 


``` r
knitr::opts_chunk$set(echo=TRUE, message=FALSE, warning=FALSE)
```

# Bivariate Data
***

Given some data

``` r
## Bivariate Data from USArrests
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

``` r
## Point Estimates
coef(reg)
```

```
## (Intercept)           x 
##  6.41594246  0.02093466
```

To qualitatively analyze the ''Goodness of fit'', we plot our predictions.

``` r
## Plot Data and Predictions
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
## Add Legend
fig <- plotly::layout(fig,
          showlegend=F,
          title='Crime and Urbanization in America 1975',
          xaxis = list(title='Percent of People in an Urban Area'),
          yaxis = list(title='Homicide Arrests per 100,000 People'))
## Plot Model Predictions
add_trace(fig, x=~x, y=~pred,
    inherit=F, hoverinfo='none',
    mode='lines+markers', type='scatter',
    color=I('black'),
    line=list(width=1/2),
    marker=list(symbol=134, size=5))
```

```{=html}
<div class="plotly html-widget html-fill-item" id="htmlwidget-46f1dfd8fd88dfe6c27e" style="width:672px;height:480px;"></div>
<script type="application/json" data-for="htmlwidget-46f1dfd8fd88dfe6c27e">{"x":{"visdat":{"94704918b360":["function () ","plotlyVisDat"]},"cur_data":"94704918b360","attrs":{"94704918b360":{"x":{},"y":{},"mode":"markers","hoverinfo":"text","marker":{"color":"#00000040","size":10},"text":{},"alpha_stroke":1,"sizes":[10,100],"spans":[1,20],"type":"scatter"},"94704918b360.1":{"x":{},"y":{},"hoverinfo":"none","mode":"lines+markers","type":"scatter","color":["black"],"line":{"width":0.5},"marker":{"symbol":134,"size":5},"inherit":false}},"layout":{"margin":{"b":40,"l":60,"t":25,"r":10},"showlegend":false,"title":"Crime and Urbanization in America 1975","xaxis":{"domain":[0,1],"automargin":true,"title":"Percent of People in an Urban Area"},"yaxis":{"domain":[0,1],"automargin":true,"title":"Homicide Arrests per 100,000 People"},"hovermode":"closest"},"source":"A","config":{"modeBarButtonsToAdd":["hoverclosest","hovercompare"],"showSendToCloud":false},"data":[{"x":[58,48,80,50,91,78,77,72,80,60,83,54,83,65,57,66,52,66,51,67,85,74,66,44,70,53,62,81,56,89,70,86,45,44,75,68,67,72,87,48,45,59,80,80,32,63,73,39,66,60],"y":[13.199999999999999,10,8.0999999999999996,8.8000000000000007,9,7.9000000000000004,3.2999999999999998,5.9000000000000004,15.4,17.399999999999999,5.2999999999999998,2.6000000000000001,10.4,7.2000000000000002,2.2000000000000002,6,9.6999999999999993,15.4,2.1000000000000001,11.300000000000001,4.4000000000000004,12.1,2.7000000000000002,16.100000000000001,9,6,4.2999999999999998,12.199999999999999,2.1000000000000001,7.4000000000000004,11.4,11.1,13,0.80000000000000004,7.2999999999999998,6.5999999999999996,4.9000000000000004,6.2999999999999998,3.3999999999999999,14.4,3.7999999999999998,13.199999999999999,12.699999999999999,3.2000000000000002,2.2000000000000002,8.5,4,5.7000000000000002,2.6000000000000001,6.7999999999999998],"mode":"markers","hoverinfo":["text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text"],"marker":{"color":"#00000040","size":10,"line":{"color":"rgba(31,119,180,1)"}},"text":["<b> Alabama <\/b> <br>Urban  : 58 <br>Murder : 13.2 <br>Predicted Murder : 7.63 <br>Residual : 5.57","<b> Alaska <\/b> <br>Urban  : 48 <br>Murder : 10 <br>Predicted Murder : 7.42 <br>Residual : 2.58","<b> Arizona <\/b> <br>Urban  : 80 <br>Murder : 8.1 <br>Predicted Murder : 8.09 <br>Residual : 0.01","<b> Arkansas <\/b> <br>Urban  : 50 <br>Murder : 8.8 <br>Predicted Murder : 7.46 <br>Residual : 1.34","<b> California <\/b> <br>Urban  : 91 <br>Murder : 9 <br>Predicted Murder : 8.32 <br>Residual : 0.68","<b> Colorado <\/b> <br>Urban  : 78 <br>Murder : 7.9 <br>Predicted Murder : 8.05 <br>Residual : -0.15","<b> Connecticut <\/b> <br>Urban  : 77 <br>Murder : 3.3 <br>Predicted Murder : 8.03 <br>Residual : -4.73","<b> Delaware <\/b> <br>Urban  : 72 <br>Murder : 5.9 <br>Predicted Murder : 7.92 <br>Residual : -2.02","<b> Florida <\/b> <br>Urban  : 80 <br>Murder : 15.4 <br>Predicted Murder : 8.09 <br>Residual : 7.31","<b> Georgia <\/b> <br>Urban  : 60 <br>Murder : 17.4 <br>Predicted Murder : 7.67 <br>Residual : 9.73","<b> Hawaii <\/b> <br>Urban  : 83 <br>Murder : 5.3 <br>Predicted Murder : 8.15 <br>Residual : -2.85","<b> Idaho <\/b> <br>Urban  : 54 <br>Murder : 2.6 <br>Predicted Murder : 7.55 <br>Residual : -4.95","<b> Illinois <\/b> <br>Urban  : 83 <br>Murder : 10.4 <br>Predicted Murder : 8.15 <br>Residual : 2.25","<b> Indiana <\/b> <br>Urban  : 65 <br>Murder : 7.2 <br>Predicted Murder : 7.78 <br>Residual : -0.58","<b> Iowa <\/b> <br>Urban  : 57 <br>Murder : 2.2 <br>Predicted Murder : 7.61 <br>Residual : -5.41","<b> Kansas <\/b> <br>Urban  : 66 <br>Murder : 6 <br>Predicted Murder : 7.8 <br>Residual : -1.8","<b> Kentucky <\/b> <br>Urban  : 52 <br>Murder : 9.7 <br>Predicted Murder : 7.5 <br>Residual : 2.2","<b> Louisiana <\/b> <br>Urban  : 66 <br>Murder : 15.4 <br>Predicted Murder : 7.8 <br>Residual : 7.6","<b> Maine <\/b> <br>Urban  : 51 <br>Murder : 2.1 <br>Predicted Murder : 7.48 <br>Residual : -5.38","<b> Maryland <\/b> <br>Urban  : 67 <br>Murder : 11.3 <br>Predicted Murder : 7.82 <br>Residual : 3.48","<b> Massachusetts <\/b> <br>Urban  : 85 <br>Murder : 4.4 <br>Predicted Murder : 8.2 <br>Residual : -3.8","<b> Michigan <\/b> <br>Urban  : 74 <br>Murder : 12.1 <br>Predicted Murder : 7.97 <br>Residual : 4.13","<b> Minnesota <\/b> <br>Urban  : 66 <br>Murder : 2.7 <br>Predicted Murder : 7.8 <br>Residual : -5.1","<b> Mississippi <\/b> <br>Urban  : 44 <br>Murder : 16.1 <br>Predicted Murder : 7.34 <br>Residual : 8.76","<b> Missouri <\/b> <br>Urban  : 70 <br>Murder : 9 <br>Predicted Murder : 7.88 <br>Residual : 1.12","<b> Montana <\/b> <br>Urban  : 53 <br>Murder : 6 <br>Predicted Murder : 7.53 <br>Residual : -1.53","<b> Nebraska <\/b> <br>Urban  : 62 <br>Murder : 4.3 <br>Predicted Murder : 7.71 <br>Residual : -3.41","<b> Nevada <\/b> <br>Urban  : 81 <br>Murder : 12.2 <br>Predicted Murder : 8.11 <br>Residual : 4.09","<b> New Hampshire <\/b> <br>Urban  : 56 <br>Murder : 2.1 <br>Predicted Murder : 7.59 <br>Residual : -5.49","<b> New Jersey <\/b> <br>Urban  : 89 <br>Murder : 7.4 <br>Predicted Murder : 8.28 <br>Residual : -0.88","<b> New Mexico <\/b> <br>Urban  : 70 <br>Murder : 11.4 <br>Predicted Murder : 7.88 <br>Residual : 3.52","<b> New York <\/b> <br>Urban  : 86 <br>Murder : 11.1 <br>Predicted Murder : 8.22 <br>Residual : 2.88","<b> North Carolina <\/b> <br>Urban  : 45 <br>Murder : 13 <br>Predicted Murder : 7.36 <br>Residual : 5.64","<b> North Dakota <\/b> <br>Urban  : 44 <br>Murder : 0.8 <br>Predicted Murder : 7.34 <br>Residual : -6.54","<b> Ohio <\/b> <br>Urban  : 75 <br>Murder : 7.3 <br>Predicted Murder : 7.99 <br>Residual : -0.69","<b> Oklahoma <\/b> <br>Urban  : 68 <br>Murder : 6.6 <br>Predicted Murder : 7.84 <br>Residual : -1.24","<b> Oregon <\/b> <br>Urban  : 67 <br>Murder : 4.9 <br>Predicted Murder : 7.82 <br>Residual : -2.92","<b> Pennsylvania <\/b> <br>Urban  : 72 <br>Murder : 6.3 <br>Predicted Murder : 7.92 <br>Residual : -1.62","<b> Rhode Island <\/b> <br>Urban  : 87 <br>Murder : 3.4 <br>Predicted Murder : 8.24 <br>Residual : -4.84","<b> South Carolina <\/b> <br>Urban  : 48 <br>Murder : 14.4 <br>Predicted Murder : 7.42 <br>Residual : 6.98","<b> South Dakota <\/b> <br>Urban  : 45 <br>Murder : 3.8 <br>Predicted Murder : 7.36 <br>Residual : -3.56","<b> Tennessee <\/b> <br>Urban  : 59 <br>Murder : 13.2 <br>Predicted Murder : 7.65 <br>Residual : 5.55","<b> Texas <\/b> <br>Urban  : 80 <br>Murder : 12.7 <br>Predicted Murder : 8.09 <br>Residual : 4.61","<b> Utah <\/b> <br>Urban  : 80 <br>Murder : 3.2 <br>Predicted Murder : 8.09 <br>Residual : -4.89","<b> Vermont <\/b> <br>Urban  : 32 <br>Murder : 2.2 <br>Predicted Murder : 7.09 <br>Residual : -4.89","<b> Virginia <\/b> <br>Urban  : 63 <br>Murder : 8.5 <br>Predicted Murder : 7.73 <br>Residual : 0.77","<b> Washington <\/b> <br>Urban  : 73 <br>Murder : 4 <br>Predicted Murder : 7.94 <br>Residual : -3.94","<b> West Virginia <\/b> <br>Urban  : 39 <br>Murder : 5.7 <br>Predicted Murder : 7.23 <br>Residual : -1.53","<b> Wisconsin <\/b> <br>Urban  : 66 <br>Murder : 2.6 <br>Predicted Murder : 7.8 <br>Residual : -5.2","<b> Wyoming <\/b> <br>Urban  : 60 <br>Murder : 6.8 <br>Predicted Murder : 7.67 <br>Residual : -0.87"],"type":"scatter","error_y":{"color":"rgba(31,119,180,1)"},"error_x":{"color":"rgba(31,119,180,1)"},"line":{"color":"rgba(31,119,180,1)"},"xaxis":"x","yaxis":"y","frame":null},{"x":[58,48,80,50,91,78,77,72,80,60,83,54,83,65,57,66,52,66,51,67,85,74,66,44,70,53,62,81,56,89,70,86,45,44,75,68,67,72,87,48,45,59,80,80,32,63,73,39,66,60],"y":[7.630152672499273,7.4208060843020238,8.0907151665332222,7.4626754019414738,8.3209964135501959,8.0488458488937713,8.0279111900740467,7.9232378959754222,8.0907151665332222,7.672021990138723,8.1535191429923959,7.546414037220373,8.1535191429923959,7.7766952842373476,7.6092180136795484,7.7976299430570721,7.5045447195809238,7.7976299430570721,7.4836100607611984,7.8185646018767976,8.1953884606318468,7.9651072136148722,7.7976299430570721,7.3370674490231238,7.8813685783359722,7.5254793784006484,7.713891307778173,8.1116498253529468,7.588283354859823,8.279127095910745,7.8813685783359722,8.2163231194515713,7.3580021078428492,7.3370674490231238,7.9860418724345967,7.8394992606965221,7.8185646018767976,7.9232378959754222,8.2372577782712959,7.4208060843020238,7.3580021078428492,7.6510873313189975,8.0907151665332222,8.0907151665332222,7.0858515431864246,7.7348259665978976,7.9441725547951467,7.2323941549244992,7.7976299430570721,7.672021990138723],"hoverinfo":["none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none"],"mode":"lines+markers","type":"scatter","line":{"color":"rgba(0,0,0,1)","width":0.5},"marker":{"color":"rgba(0,0,0,1)","symbol":134,"size":5,"line":{"color":"rgba(0,0,0,1)"}},"textfont":{"color":"rgba(0,0,0,1)"},"error_y":{"color":"rgba(0,0,0,1)"},"error_x":{"color":"rgba(0,0,0,1)"},"xaxis":"x","yaxis":"y","frame":null}],"highlight":{"on":"plotly_click","persistent":false,"dynamic":false,"selectize":false,"opacityDim":0.20000000000000001,"selected":{"opacity":1},"debounce":0},"shinyEvents":["plotly_hover","plotly_click","plotly_selected","plotly_relayout","plotly_brushed","plotly_brushing","plotly_clickannotation","plotly_doubleclick","plotly_deselect","plotly_afterplot","plotly_sunburstclick"],"base_url":"https://plot.ly"},"evals":[],"jsHooks":[]}</script>
```
To quantitatively analyze GoF, we compute $R^2$ using the sums of squared errors (Total, Explained, and Residual)
$$
\underbrace{\sum_{i}(y_i-\bar{y})^2}_\text{TSS}=\underbrace{\sum_{i}(\hat{y}_i-\bar{y})^2}_\text{ESS}+\underbrace{\sum_{i}\hat{\epsilon_{i}}^2}_\text{RSS}\\
R^2 = \frac{ESS}{TSS}=1-\frac{RSS}{TSS}
$$
Note that $R^2$ is also called the coefficient of determination.

``` r
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

``` r
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

Note that values reported by your computer do not necessarily satisfy this definition. To calculate these statistics, we will estimate variability using *data-driven* methods. (For some theoretical background, see, e.g., https://www.sagepub.com/sites/default/files/upm-binaries/21122_Chapter_21.pdf.)


We first consider the simplest, the jackknife. In this procedure, we loop through each row of the dataset. And, in each iteration of the loop, we drop that observation from the dataset and reestimate the statistic of interest. We then calculate the standard deviation of the statistic across all ``subsamples''.


``` r
## Jackknife Standard Errors for OLS Coefficient
jack_regs <- lapply(1:nrow(xy), function(i){
    xy_i <- xy[-i,]
    reg_i <- lm(y~x, dat=xy_i)
})
jack_coefs <- sapply(jack_regs, coef)['x',]
jack_se <- sd(jack_coefs)
### classic_se <- sqrt(diag(vcov(reg)))[['x']]


## Jackknife Sampling Distribution
hist(jack_coefs, breaks=25,
    main=paste0('SE est. = ', round(jack_se,4)),
    font.main=1, border=NA,
    xlab=expression(beta[-i]))
## Original Estimate
abline(v=coef(reg)['x'], lwd=2)
## Jackknife Confidence Intervals
jack_ci_percentile <- quantile(jack_coefs, probs=c(.025,.975))
abline(v=jack_ci_percentile, lty=2)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-7-1.png" width="672" />

``` r
## Plot Normal Approximation
## jack_ci_normal <- jack_mean+c(-1.96, +1.96)*jack_se
## abline(v=jack_ci_normal, col="red", lty=3)
```

There are several resampling techniques. The other main one is the bootstrap, which resamples with *replacement* for an *arbitrary* number of iterations. When bootstrapping a dataset with $n$ observations, you randomly resample all $n$ rows in your data set $B$ times. Random subsampling is one of many hybrid approaches that tries to combine the best of both worlds.

| | Sample Size per Iteration | Number of Iterations | Resample |
| -------- | ------- | ------- | ------- |
Bootstrap | $n$     | $B$  | With Replacement |
Jackknife | $n-1$   | $n$  | Without Replacement |
Random Subsample | $m < n$ | $B$  | Without Replacement |


``` r
## Bootstrap
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
## Random Subsamples
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
    ## Data
    xy_b <- reg_b$model
    ## Coefficient
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
## Null Distribution for Beta
boot_t0 <- sapply( 1:399, function(b){
    xy_b <- xy
    xy_b$y <- sample( xy_b$y, replace=T)
    reg_b <- lm(y~x, dat=xy_b)
    beta_b <- coef(reg_b)[['x']]
    t_hat_b <- beta_b/jack_se
    return(t_hat_b)
})

## Null Bootstrap Distribution
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
## One Sided Test for P(t > boot_t | Null)=1- P(t < boot_t | Null)
That_NullDist1 <- ecdf(boot_t0)
Phat1  <- 1-That_NullDist1(jack_t)

## Two Sided Test for P(t > jack_t or  t < -jack_t | Null)
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
## [1] 0.6641604
```


## Prediction Intervals

In addition to confidence intervals, we can also compute a *prediction interval* which estimates the range of variability across different samples for the outcomes. These intervals also take into account the residuals--- the variability of individuals around the mean. 



``` r
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
    ylim=c(-5,20), font.main=1)
polygon( c(x, rev(x)), c(boot_pi[,1], rev(boot_pi[,2])),
    col=grey(0,.2), border=NA)

## Parametric PI (For Comparison)
pi <- predict(reg, interval='prediction', newdata=data.frame(x))
lines( x, pi[,'lwr'], lty=2)
lines( x, pi[,'upr'], lty=2)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-13-1.png" width="672" />


For a nice overview of different types of intervals, see https://www.jstor.org/stable/2685212. For an in-depth view, see "Statistical Intervals: A Guide for Practitioners and Researchers" or "Statistical Tolerance Regions: Theory, Applications, and Computation". See https://robjhyndman.com/hyndsight/intervals/ for constructing intervals for future observations in a time-series context. See Davison and Hinkley, chapters 5 and 6 (also Efron and Tibshirani, or Wehrens et al.)


## Locally Linear

Segmented/piecewise regressions

``` r
## Globally Linear
reg <- lm(y~x, data=xy)

# Diagnose Fit
#plot( fitted(reg), resid(reg), pch=16, col=grey(0,.5))
#plot( xy$x, resid(reg), pch=16, col=grey(0,.5))

## Linear in 2 Pieces (subsets)
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
## Linear in 3 Pieces (subsets)
xcut3 <- cut(xy$x, seq(32,92,by=20)) ## Finer Bins
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

## Compare Predictions
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
## ``Naive" Smoother
pred_fun <- function(x0, h, xy){
    ## Assign equal weight to observations within h distance to x0
    ## 0 weight for all other observations
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
## Adaptive-width subsamples with non-uniform weights
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
## Loess
xy0 <- xy[order(xy$x),]
X0 <- unique(xy0$x)
reg_lo <- loess(y~x, data=xy0, span=.8)

## Jackknife CI
jack_lo <- sapply(1:nrow(xy), function(i){
    xy_i <- xy[-i,]
    reg_i <- loess(y~x, dat=xy_i, span=.8)
    predict(reg_i, newdata=data.frame(x=X0))
})
jack_cb <- apply(jack_lo,1, quantile,
    probs=c(.025,.975), na.rm=T)

## Plot
plot(y~x, pch=16, col=grey(0,.5), dat=xy0)
preds_lo <- predict(reg_lo, newdata=data.frame(x=X0))
lines(X0, preds_lo,
    col=hcl.colors(3,alpha=.75)[2],
    type='o', pch=2)
## Plot CI
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

## Estimate Residuals CI at design points
res_lo <- sapply(1:nrow(xy), function(i){
    y_i <- xy[i,'y']
    preds_i <- jack_lo[,i]
    resids_i <- y_i - preds_i
})
res_cb <- apply(res_lo, 1, quantile,
    probs=c(.025,.975), na.rm=T)
## Plot
lines( X0, preds_lo +res_cb[1,],
    col=hcl.colors(3,alpha=.75)[2], lt=2)
lines( X0, preds_lo +res_cb[2,],
    col=hcl.colors(3,alpha=.75)[2], lty=2)




## Smooth estimates 
res_lo <- lapply(1:nrow(xy), function(i){
    y_i <- xy[i,'y']
    x_i <- xy[i,'x']
    preds_i <- jack_lo[,i]
    resids_i <- y_i - preds_i
    cbind(e=resids_i, x=x_i)
})
res_lo <- as.data.frame(do.call(rbind, res_lo))

res_fun <- function(x0, h, res_lo){
    ## Assign equal weight to observations within h distance to x0
    ## 0 weight for all other observations
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

``` r
library(psych)
pairs.panels( USArrests[,c('Murder','Assault','UrbanPop')],
    hist.col=grey(0,.25), breaks=30, density=F, hist.border=NA, ## Diagonal
    ellipses=F, rug=F, smoother=F, pch=16, col=grey(0,.5) ## Lower Triangle
    )
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-20-1.png" width="672" />


## Multiple Linear Regression
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

Point estimates 
$$
\hat{\beta}=(\textbf{X}'\textbf{X})^{-1}\textbf{X}'y
$$


``` r
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

``` r
## Check
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
<div class="plotly html-widget html-fill-item" id="htmlwidget-e5f9fc7b0e3f7b9b5db7" style="width:672px;height:480px;"></div>
<script type="application/json" data-for="htmlwidget-e5f9fc7b0e3f7b9b5db7">{"x":{"visdat":{"947079470370":["function () ","plotlyVisDat"]},"cur_data":"947079470370","attrs":{"947079470370":{"mode":"markers","x":{},"y":{},"text":{},"hoverinfo":"text","showlegend":false,"marker":{"color":"rgba(0, 0, 0, 0.5)"},"alpha_stroke":1,"sizes":[10,100],"spans":[1,20],"type":"scatter"}},"layout":{"margin":{"b":40,"l":60,"t":25,"r":10},"showlegend":false,"title":"Joint Distribution of Coefficients","xaxis":{"domain":[0,1],"automargin":true,"title":"UrbanPop Coefficient"},"yaxis":{"domain":[0,1],"automargin":true,"title":"Assualt Coefficient"},"hovermode":"closest"},"source":"A","config":{"modeBarButtonsToAdd":["hoverclosest","hovercompare"],"showSendToCloud":false},"data":[{"mode":"markers","x":[-0.063130296674725903,0.0050404843699919672,-0.046789014238759051,-0.094541931108383201,-0.036104663822894678,-0.010335517606006593,-0.033588153032380497,-0.019100013009570396,-0.058099579093503093,-0.05437224478291898,-0.046352711451702361,-0.029285580349734323,-0.047785251045663023,-0.02929959922122137,-0.073195786830080073,-0.085684881608951477,-0.034495621629866705,-0.015810654610590641,-0.038370407048179039,0.013649277295414651,-0.01966554254408415,-0.063148368359774359,0.0052277397453867648,-0.035050330515034034,-0.048959633535054746,-0.036888406041231073,-0.088643950519559672,-0.024149874722646042,-0.062488007958127381,0.0055750875898641361,-0.0031893885656458019,-0.0109264281867945,-0.046609179098099564,-0.037062498071477518,-0.09595550810271844,-0.044518254979911229,-0.012364261519608085,-0.022432343883536786,-0.074046888079856682,-0.052078170325964075,-0.036412506528408287,-0.054532642359788663,-0.048735129673674188,-0.026372773787119122,-0.03784907932671578,-0.055342977784253615,-0.049818052008526716,-0.017558286352361809,-0.057627272652065256,-0.042455671146072203,-0.032327926931529638,-0.074935495712137631,-0.067208141833517407,-0.028627902084978646,-0.077734073760599126,-0.066047514593922871,-0.10978592532702827,-0.073775432643580857,-0.057943804903565259,-0.0332574127056183,-0.056472305619578229,-0.05436900249822655,-0.079347051491676521,-0.0055330766388281046,-0.047748112856563427,-0.05735128112118025,-0.062173222024769381,-0.011904858850772068,-0.049350814829689692,-0.099985880185121667,-0.055292045107661898,-0.072073961430924149,-0.058230808703650071,-0.043321904855114578,-0.043792840694001557,-0.0063061243660120512,-0.048127354181485511,-0.053442589966235118,-0.024129300585707916,-0.054835551689890537,-0.054885906617976009,-0.060129094462276135,-0.13949722208940188,-0.024465048582957311,-0.050944378691442097,-0.042877253363378456,-0.05148636379053214,-0.059500147558094664,-0.059757365166178376,-0.035207446542572969,-0.041970365578068193,-0.035623616135891843,-0.031459038277279042,-0.073327537686719485,-0.026595084917471416,-0.061649614836267866,-0.071450154604491362,-0.04452499410938493,-0.037121598360626486,-0.091783171666202104,-0.069504869572176567,-0.010573650765565476,-0.042482672462567581,-0.053506965136070755,-0.089160765943622239,-0.037578707335888833,-0.0255476709973937,-0.051314057957231672,-0.046393377583705479,-0.035244683588217224,-0.045851525262929016,-0.061637526001309922,-0.00078474915390739481,-0.0070554548704968674,-0.043187938694686234,0.014834221974382302,-0.046529062845115897,-0.098603486442710886,-0.019293203883342467,-0.054141168772900906,-0.032695731791066149,0.0221517938093778,-0.074341733759592507,0.0034252174029938335,-0.073777374067257581,-0.051355431160975448,-0.046498152684854063,-0.026603768821146099,-0.033111946572315233,-0.063752423672278138,-0.038322802709532873,-0.026674185429039876,-0.029657452155187281,0.016074417856024044,-0.10842464044740639,-0.07213624671137589,-0.045875279387783817,-0.059791154738731013,-0.024844553543526032,-0.056407916738127728,-0.040514634382228062,-0.094221147044100714,-0.036613379626471459,-0.053025950142938073,-0.0025989269486884738,-0.059382013207309167,-0.061307421689865527,-0.048355888727933262,-0.046171786772787084,-0.0350644152717711,-0.028774041928542823,-0.045141029130795846,-0.089323135091998421,-0.039746332798468932,-0.0077240991815177417,-0.037452284573241887,-0.058501390518556268,-0.019569982961683663,-0.059943058342086776,-0.045597516126704665,-0.022698934426491568,-0.035552086068646016,-0.034786181959905745,-0.07381181334099364,-0.049968004833770396,-0.041644778615388268,-0.060066849303968571,0.0032437210269557369,-0.05248345992157006,-0.059921537624210007,-0.018419406646280587,-0.080095780705781175,-0.066756890233168914,-0.052699186312091612,0.0083014531109792487,-0.066654671464909471,-0.09729559576230401,-0.033464621516213405,-0.061176582576040084,-0.030261843902050979,-0.050279271066498772,-0.046413773415320742,-0.015895665257200393,-0.058338634278761098,-0.098208083660053652,-0.062482694264599618,-0.016002169757393516,-0.030943483280270453,-0.046836191247155309,-0.12445876405731207,-0.032184779431255368,-0.046395314369451844,-0.014703075752098048,-0.042096868963115174,-0.029388642465233514,-0.016939566215413329,-0.010093530924818506,-0.051026712204036741,-0.0086662728773900938,-0.067693891658680699,-0.049475610211030426,-0.057162369876943148,-0.049233518529263554,-0.042781026731981683,-0.055103053609401841,-0.036036543427656234,-0.03499719858541378,-0.0040450063145867346,-0.01017842281855454,0.012990742423785241,-0.035745955617487356,-0.018919295875893544,-0.037505424359202989,-0.0090864022199720774,-0.014412781690369077,-0.033190102678949278,-0.032405463925759784,-0.028988933580659595,-0.065374873882140916,-0.068332864280603714,-0.030901751912715977,-0.01397030781240719,-0.077878596240995746,-0.05267164341508547,-0.0507965525425529,-0.031288207318957165,-0.040231613468588744,-0.04282587754508508,-0.052989211654128288,-0.045279619240237427,-0.049293111923387131,-0.015132383319830321,-0.020543279567912836,-0.11866799543700096,-0.065063752283415974,-0.029257914180862019,-0.035532227267113595,-0.022181987853072491,-0.02073978384039208,-0.098724927867558043,-0.0094507594097516714,-0.048823604666712074,-0.028506864905272791,-0.012784870734233327,-0.040483858138575551,-0.020263123844474339,-0.049118645610859518,-0.061313934840581862,-0.10515967693016226,-0.12593025453737869,-0.031473864290179988,-0.074531341477402577,-0.068395680961423302,-0.060087281348944109,-0.040071108064446817,-0.036534853497621922,-0.050259680024438314,-0.053567910313082757,-0.090248567588390657,-0.095712003255214562,-0.025756454508684905,-0.092350273528810228,-0.065117863726241135,-0.020734027687277917,-0.032659263923709166,-0.092818342014891517,-0.055614532342250209,-0.060222209494244477,-0.053751987134547985,-0.04469870248391869,-0.069745036771375279,-0.066423092659688945,-0.032727121760109786,-0.040913984626375702,-0.039400381742873351,-0.068058809091319214,-0.013668605958144125,-0.021213083517407194,-0.083880601059233395,-0.043784710128913745,-0.031452221809244091,-0.066705728371389036,-0.098444880712481683,-0.025947422302107538,-0.011527942530583892,-0.025523827299366517,-0.056605887836463191,-0.052541542776762935,-0.037949840587162768,-0.033994405177493553,-0.069259750667797687,-0.050048306410820947,-0.016632933810229438,-0.0014748090480355639,-0.037782096661809435,-0.08007529699105255,-0.036698062903973004,-0.064435927318200914,-0.021059042420947739,-0.037287154291280877,-0.050735360270372579,-0.052027640505121153,-0.074891935043355909,-0.037356749837125412,-0.068373287804009947,-0.062764174565816483,-0.063047150001206836,-0.014251878807510302,-0.035059719684335758,-0.038408602417327409,-0.10738573844574574,-0.016561314401071555,-0.054294484109673635,-0.038508240340617429,-0.077303811905355721,-0.046982663507260838,-0.021584585135031253,-0.042353045432326389,-0.029524473011744618,-0.067290865650236245,-0.015911140782154262,-0.088022741369402482,-0.042253752894664785,-0.04154019084131623,-0.056727596809878655,-0.085323305389312279,-0.10079488119784043,-0.075423591733241924,-0.0057405659529929376,-0.036076179206495362,-0.091201713789507477,-0.028146370046073364,-0.060664245819566531,-0.023450626840143547,-0.04614294382493541,-0.056788051483554709,-0.092323788020530137,-0.048568942952656083,-0.010915866715110693,-0.06557039127612603,-0.025909659236658666,-0.047164600978491962,-0.053398216313252395,-0.0524430697030734,-0.038604740611209047,-0.0097596355663800271,-0.042143732934254899,-0.071080581066814974,-0.03328856190153158,-0.011891504976103317,0.0078577321794874727,-0.055774212189349782,-0.062373629881121641,0.0021443568142803676,-0.026498123857134598,-0.018353821099647328,-0.052694738030324817,-0.10920070641833769,-0.067346110892777172,-0.042021231266928333,-0.021356118009258962,-0.061305054999661317,-0.011863280986327444,-0.035180182516389692,-0.06597299322602343,-0.026145647284438165,-0.015025095037099185,-0.033603927855324303,-0.055209507188218619,-0.019549321175229895,-0.068774644134025772,-0.016457222514850999,-0.068193263243961133,-0.045381844295451189,-0.068233804790328381,-0.044960808743084064,-0.056656610428873815,-0.067671994058465468,-0.083854205978655033,-0.012330388868707708,-0.067063664650600457,-0.0068097760636334275,-0.062727879596499503,-0.059695582739226781,-0.010128664028402982,-0.062530426544103165,-0.03960993435703529,-0.067277531168389595,-0.053495451068373237,-0.03601841305469531,-0.056522911164676358,-0.028513506307523591,-0.053507468093055656,0.0084320873607060132,-0.014042739786258461,0.0036682606085600036,-0.030479470285668119,-0.028493752751853701,-0.031238806951682675],"y":[0.042783659685044599,0.043587684522159616,0.047910904901233155,0.048513291810031688,0.045336144296378042,0.038822159480123776,0.037314108238743662,0.034489418894089456,0.042350830892657294,0.038860544362997303,0.04137018469020242,0.035968429348607153,0.047504073965477546,0.047674381903088182,0.064300469898846649,0.040886231902928338,0.045266597641847019,0.037469177578945703,0.04312325198316963,0.03968062491586543,0.040323811337838043,0.04623805123846321,0.039058595594379603,0.047972624577641544,0.047668554711972531,0.045008462677312351,0.051754938378547985,0.044502815571105227,0.038217003801528593,0.041517135314247076,0.045462817353102689,0.043891512750252819,0.044822789246587072,0.043822130492260476,0.05804493501733881,0.039245200625984515,0.039360571735446825,0.04121272010941146,0.047840299927911861,0.045305779890302836,0.044731824961077159,0.048331447795467948,0.043417876434444114,0.036264371731331423,0.04574102767879859,0.041665177210236652,0.038877654000079809,0.035824065379915331,0.038494478703033845,0.052608394362397219,0.04568669043206143,0.057032774027170746,0.043516302212625604,0.043821918583050998,0.04984119776518478,0.050055395755578498,0.054960640179376755,0.041282851729104342,0.049392814942253664,0.043748520218643824,0.043599685564114012,0.043715189527337571,0.046727112597641722,0.044116900797962773,0.038751910237187145,0.042236118013369503,0.047926678790635814,0.039168741789108966,0.04230334162438535,0.058147183369764328,0.047327205263458051,0.047007242610381202,0.038349413956367907,0.047289732644342101,0.033264705420851366,0.047784408969000526,0.051990418829794091,0.048731344567721435,0.04913443680454186,0.045988067404841702,0.056172556244409755,0.046812758638423338,0.053261539284621282,0.04605159340275411,0.045090426999369937,0.046285648682393279,0.045536700884824491,0.044405621816986547,0.047075520927409069,0.03918979773272066,0.044299331686615151,0.040638067500566116,0.04517042480103365,0.052932120190026327,0.041422430634683864,0.041855134169391371,0.050383520373513548,0.047291049983575341,0.045232398058548284,0.043634545811708947,0.044650508385621367,0.042703498555922287,0.041838828440285886,0.045718562839127008,0.048445373791921133,0.03920069288102538,0.042631915725323266,0.046920656833325726,0.049382179814046821,0.046603309520355025,0.051148560672367269,0.037870208401484022,0.040550227143121689,0.03492891061689702,0.045411267677858101,0.037498418667794881,0.033782236268735048,0.051951900425464062,0.039790681101805725,0.041659522771969423,0.03728989656760031,0.039758040861900372,0.047749700683395582,0.043146319370635046,0.042571763937505697,0.043710546938338375,0.044572933391926348,0.042277871499024823,0.046793169807746449,0.05099564842023304,0.038612759233877733,0.033185107849562946,0.045524073390090639,0.038068499014040622,0.045522946360488592,0.051437550424274413,0.048480139155719172,0.047655745538517161,0.041886999896382227,0.039965956630470562,0.044836510363025252,0.048578257352225034,0.037467072762213595,0.050551506242756269,0.040339531308068693,0.048681909661034702,0.046183291082021329,0.037830059698279496,0.040365524890784973,0.046148858270410813,0.042577494339452467,0.04471693426244807,0.053878843767449988,0.044245664473617767,0.03743516763001855,0.043652787860999534,0.03820633695476406,0.043012539381156262,0.04326825400867431,0.043080286550281156,0.039757455876496588,0.045498983898973902,0.039823629208506836,0.038743728209927275,0.041047780814736264,0.044842851558855749,0.053533529219173703,0.049325789438373478,0.050450060464615094,0.046731474080350562,0.05079983541059728,0.048095935274074603,0.047756756097803929,0.044567620619125052,0.039923207829608218,0.043703109659491021,0.048655932538650304,0.046733923955462033,0.043779837156490711,0.037844905053611488,0.044469066479975845,0.038516997055735053,0.038873443123489955,0.041947984363105817,0.048879004747033092,0.051235138409422259,0.039208254586746913,0.048913382540172128,0.04112305633440802,0.044407797998125602,0.048177995970622743,0.055846707838082654,0.045083770799924906,0.045126023519783273,0.036593405276330482,0.046494314890849646,0.045499824984786219,0.043625724606266403,0.038371192100363757,0.04326558822974963,0.046489843574428327,0.049162985038588798,0.041628462179570981,0.044417899465815092,0.045737963486099882,0.043369046377497472,0.046270132267446321,0.044716545123187179,0.041806556167047031,0.043701646840656458,0.04397721806387251,0.044023078949226052,0.047242420617342573,0.038076587530364164,0.035844399573741262,0.03995609327019934,0.03961031840516397,0.048296245622245569,0.048728372057661083,0.040298026302876599,0.040374781102944388,0.051335459114793258,0.047224787928873344,0.041516542858673844,0.047914592334838739,0.039979456892924925,0.04620662032503111,0.044577971885579361,0.040648762362243865,0.046080325523376119,0.046354486179815996,0.038232283788215186,0.043291744246650443,0.049914634746130081,0.041007149572221867,0.043209986215527969,0.048182949333212918,0.03577628827867798,0.042929714521320946,0.04570738900172637,0.038019023418841294,0.050777710217227094,0.04973421459739643,0.03822270700880067,0.053950270544628136,0.039736756537713282,0.05690070554779586,0.041381633387068621,0.050440285570407487,0.050291596845815772,0.043275354156749657,0.047601554538016795,0.061968407105388271,0.042948567101912,0.038530448283546515,0.040078260915136728,0.039810004951469156,0.039752663878333039,0.0524721820575113,0.044515752288525189,0.039366170982198412,0.052014262932840873,0.038876342069957798,0.044545947130280886,0.041107933990924751,0.043257766947701913,0.042599333889295786,0.058178957775560494,0.047332538691558956,0.04048674649699778,0.052062365324295458,0.046309249974987657,0.038051397096870873,0.05506196185627775,0.047172387970999444,0.050540506602256896,0.040153139294078384,0.039599098359640705,0.04004557438465503,0.045540197203511663,0.040446748624838387,0.046673360249443713,0.050641727332721612,0.040363033918835771,0.038197013137113829,0.038973470147380548,0.041006358068157722,0.051571249823267544,0.03427279529804584,0.043343147375811908,0.048165190415764669,0.044867962222141108,0.039316529731338028,0.036804995086614382,0.04316395282198731,0.043187595650423308,0.046474462557036744,0.047879487163983159,0.045201924292606145,0.041287851746199748,0.04351906030559137,0.047565956151273035,0.044097028196843038,0.045101749369622315,0.054480902766490154,0.052009268777603548,0.043256852058125586,0.037989286491149223,0.054142665821480564,0.041478617819043891,0.045775822853838084,0.037878704675115116,0.045287833833597253,0.046455809733881755,0.048592744552828311,0.040084641004782193,0.040897268017298836,0.042474488068815652,0.046282821849705065,0.041741680805970093,0.03518564735404494,0.049912520567488711,0.051202599874080656,0.042762546006013973,0.042479982402472381,0.040407708283171279,0.062580396040608249,0.04127439702290861,0.041749236302131419,0.044083992691215317,0.046131182426509119,0.040390836056190822,0.038515298411098062,0.041694774532187208,0.044826077959664458,0.044614779956866843,0.047468224274783616,0.046282731309633597,0.037593674044691119,0.047150893123519631,0.04386101110230408,0.045629834319054742,0.049221255186161973,0.04639236520913978,0.049764148686547688,0.046321474032514638,0.048259832751470472,0.043646572982025574,0.046397533675276464,0.05067566982441804,0.044731364892763463,0.046163062786774303,0.047279980682231076,0.040140671172221851,0.04020180155708649,0.044483195137584093,0.036439995392886199,0.045160199114883511,0.048665321347289521,0.047043021233258611,0.040930552937481685,0.041504128498788345,0.044534953255436875,0.041064568890280796,0.046984619388666563,0.042749078515306613,0.047869957998199174,0.043135751899353252,0.048886035999915534,0.042930314436975099,0.041981877444069317,0.041583243295138919,0.044633712774001515,0.040163473664528611,0.049293329748316121,0.049888010386092758,0.046952088597410666,0.043060365353878333,0.03969489419546407,0.044235942749862249,0.049639880784562378,0.04154098449657586,0.042769930080564678,0.046489053696046938,0.040196808167846605,0.041487288271121206,0.045198705684516796,0.049494733014272256,0.042807775727883614,0.044218936625586493,0.041874223076110398,0.044319660427953531,0.048023992153541278,0.048585880095437725,0.045768493039374969,0.038239199515062487,0.043422141671804936,0.049286360143699484,0.038707089597623021],"text":["<b> bootstrap dataset:  1 <\/b> <br>Coef. Urban  : -0.063 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 5.438","<b> bootstrap dataset:  2 <\/b> <br>Coef. Urban  : 0.005 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 0.422","<b> bootstrap dataset:  3 <\/b> <br>Coef. Urban  : -0.047 <br>Coef. Murder : 0.048 <br>Coef. Intercept : 2.802","<b> bootstrap dataset:  4 <\/b> <br>Coef. Urban  : -0.095 <br>Coef. Murder : 0.049 <br>Coef. Intercept : 5.696","<b> bootstrap dataset:  5 <\/b> <br>Coef. Urban  : -0.036 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 2.571","<b> bootstrap dataset:  6 <\/b> <br>Coef. Urban  : -0.01 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 2.281","<b> bootstrap dataset:  7 <\/b> <br>Coef. Urban  : -0.034 <br>Coef. Murder : 0.037 <br>Coef. Intercept : 3.2","<b> bootstrap dataset:  8 <\/b> <br>Coef. Urban  : -0.019 <br>Coef. Murder : 0.034 <br>Coef. Intercept : 3.251","<b> bootstrap dataset:  9 <\/b> <br>Coef. Urban  : -0.058 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 3.792","<b> bootstrap dataset:  10 <\/b> <br>Coef. Urban  : -0.054 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 3.859","<b> bootstrap dataset:  11 <\/b> <br>Coef. Urban  : -0.046 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 3.566","<b> bootstrap dataset:  12 <\/b> <br>Coef. Urban  : -0.029 <br>Coef. Murder : 0.036 <br>Coef. Intercept : 3.567","<b> bootstrap dataset:  13 <\/b> <br>Coef. Urban  : -0.048 <br>Coef. Murder : 0.048 <br>Coef. Intercept : 2.391","<b> bootstrap dataset:  14 <\/b> <br>Coef. Urban  : -0.029 <br>Coef. Murder : 0.048 <br>Coef. Intercept : 1.336","<b> bootstrap dataset:  15 <\/b> <br>Coef. Urban  : -0.073 <br>Coef. Murder : 0.064 <br>Coef. Intercept : 2.318","<b> bootstrap dataset:  16 <\/b> <br>Coef. Urban  : -0.086 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 6.516","<b> bootstrap dataset:  17 <\/b> <br>Coef. Urban  : -0.034 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 2.682","<b> bootstrap dataset:  18 <\/b> <br>Coef. Urban  : -0.016 <br>Coef. Murder : 0.037 <br>Coef. Intercept : 1.925","<b> bootstrap dataset:  19 <\/b> <br>Coef. Urban  : -0.038 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 3","<b> bootstrap dataset:  20 <\/b> <br>Coef. Urban  : 0.014 <br>Coef. Murder : 0.04 <br>Coef. Intercept : -0.204","<b> bootstrap dataset:  21 <\/b> <br>Coef. Urban  : -0.02 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 1.485","<b> bootstrap dataset:  22 <\/b> <br>Coef. Urban  : -0.063 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 4.009","<b> bootstrap dataset:  23 <\/b> <br>Coef. Urban  : 0.005 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 0.869","<b> bootstrap dataset:  24 <\/b> <br>Coef. Urban  : -0.035 <br>Coef. Murder : 0.048 <br>Coef. Intercept : 2.382","<b> bootstrap dataset:  25 <\/b> <br>Coef. Urban  : -0.049 <br>Coef. Murder : 0.048 <br>Coef. Intercept : 2.984","<b> bootstrap dataset:  26 <\/b> <br>Coef. Urban  : -0.037 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 2.744","<b> bootstrap dataset:  27 <\/b> <br>Coef. Urban  : -0.089 <br>Coef. Murder : 0.052 <br>Coef. Intercept : 4.459","<b> bootstrap dataset:  28 <\/b> <br>Coef. Urban  : -0.024 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 1.777","<b> bootstrap dataset:  29 <\/b> <br>Coef. Urban  : -0.062 <br>Coef. Murder : 0.038 <br>Coef. Intercept : 5.488","<b> bootstrap dataset:  30 <\/b> <br>Coef. Urban  : 0.006 <br>Coef. Murder : 0.042 <br>Coef. Intercept : -0.117","<b> bootstrap dataset:  31 <\/b> <br>Coef. Urban  : -0.003 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 0.835","<b> bootstrap dataset:  32 <\/b> <br>Coef. Urban  : -0.011 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 1.589","<b> bootstrap dataset:  33 <\/b> <br>Coef. Urban  : -0.047 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 3.444","<b> bootstrap dataset:  34 <\/b> <br>Coef. Urban  : -0.037 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 2.763","<b> bootstrap dataset:  35 <\/b> <br>Coef. Urban  : -0.096 <br>Coef. Murder : 0.058 <br>Coef. Intercept : 4.525","<b> bootstrap dataset:  36 <\/b> <br>Coef. Urban  : -0.045 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 3.722","<b> bootstrap dataset:  37 <\/b> <br>Coef. Urban  : -0.012 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 1.826","<b> bootstrap dataset:  38 <\/b> <br>Coef. Urban  : -0.022 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 1.975","<b> bootstrap dataset:  39 <\/b> <br>Coef. Urban  : -0.074 <br>Coef. Murder : 0.048 <br>Coef. Intercept : 4.501","<b> bootstrap dataset:  40 <\/b> <br>Coef. Urban  : -0.052 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 3.858","<b> bootstrap dataset:  41 <\/b> <br>Coef. Urban  : -0.036 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 2.093","<b> bootstrap dataset:  42 <\/b> <br>Coef. Urban  : -0.055 <br>Coef. Murder : 0.048 <br>Coef. Intercept : 2.662","<b> bootstrap dataset:  43 <\/b> <br>Coef. Urban  : -0.049 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 3.753","<b> bootstrap dataset:  44 <\/b> <br>Coef. Urban  : -0.026 <br>Coef. Murder : 0.036 <br>Coef. Intercept : 3.036","<b> bootstrap dataset:  45 <\/b> <br>Coef. Urban  : -0.038 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 3.354","<b> bootstrap dataset:  46 <\/b> <br>Coef. Urban  : -0.055 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 4.236","<b> bootstrap dataset:  47 <\/b> <br>Coef. Urban  : -0.05 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 4.028","<b> bootstrap dataset:  48 <\/b> <br>Coef. Urban  : -0.018 <br>Coef. Murder : 0.036 <br>Coef. Intercept : 2.362","<b> bootstrap dataset:  49 <\/b> <br>Coef. Urban  : -0.058 <br>Coef. Murder : 0.038 <br>Coef. Intercept : 5.182","<b> bootstrap dataset:  50 <\/b> <br>Coef. Urban  : -0.042 <br>Coef. Murder : 0.053 <br>Coef. Intercept : 2.319","<b> bootstrap dataset:  51 <\/b> <br>Coef. Urban  : -0.032 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 2.007","<b> bootstrap dataset:  52 <\/b> <br>Coef. Urban  : -0.075 <br>Coef. Murder : 0.057 <br>Coef. Intercept : 3.289","<b> bootstrap dataset:  53 <\/b> <br>Coef. Urban  : -0.067 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 5.047","<b> bootstrap dataset:  54 <\/b> <br>Coef. Urban  : -0.029 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 2.384","<b> bootstrap dataset:  55 <\/b> <br>Coef. Urban  : -0.078 <br>Coef. Murder : 0.05 <br>Coef. Intercept : 4.377","<b> bootstrap dataset:  56 <\/b> <br>Coef. Urban  : -0.066 <br>Coef. Murder : 0.05 <br>Coef. Intercept : 3.482","<b> bootstrap dataset:  57 <\/b> <br>Coef. Urban  : -0.11 <br>Coef. Murder : 0.055 <br>Coef. Intercept : 5.692","<b> bootstrap dataset:  58 <\/b> <br>Coef. Urban  : -0.074 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 5.37","<b> bootstrap dataset:  59 <\/b> <br>Coef. Urban  : -0.058 <br>Coef. Murder : 0.049 <br>Coef. Intercept : 3.36","<b> bootstrap dataset:  60 <\/b> <br>Coef. Urban  : -0.033 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 2.894","<b> bootstrap dataset:  61 <\/b> <br>Coef. Urban  : -0.056 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 3.821","<b> bootstrap dataset:  62 <\/b> <br>Coef. Urban  : -0.054 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 3.651","<b> bootstrap dataset:  63 <\/b> <br>Coef. Urban  : -0.079 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 5.31","<b> bootstrap dataset:  64 <\/b> <br>Coef. Urban  : -0.006 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 0.097","<b> bootstrap dataset:  65 <\/b> <br>Coef. Urban  : -0.048 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 4.489","<b> bootstrap dataset:  66 <\/b> <br>Coef. Urban  : -0.057 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 4.38","<b> bootstrap dataset:  67 <\/b> <br>Coef. Urban  : -0.062 <br>Coef. Murder : 0.048 <br>Coef. Intercept : 3.786","<b> bootstrap dataset:  68 <\/b> <br>Coef. Urban  : -0.012 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 2.003","<b> bootstrap dataset:  69 <\/b> <br>Coef. Urban  : -0.049 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 3.526","<b> bootstrap dataset:  70 <\/b> <br>Coef. Urban  : -0.1 <br>Coef. Murder : 0.058 <br>Coef. Intercept : 4.368","<b> bootstrap dataset:  71 <\/b> <br>Coef. Urban  : -0.055 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 3.208","<b> bootstrap dataset:  72 <\/b> <br>Coef. Urban  : -0.072 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 4.432","<b> bootstrap dataset:  73 <\/b> <br>Coef. Urban  : -0.058 <br>Coef. Murder : 0.038 <br>Coef. Intercept : 4.788","<b> bootstrap dataset:  74 <\/b> <br>Coef. Urban  : -0.043 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 3.049","<b> bootstrap dataset:  75 <\/b> <br>Coef. Urban  : -0.044 <br>Coef. Murder : 0.033 <br>Coef. Intercept : 5.022","<b> bootstrap dataset:  76 <\/b> <br>Coef. Urban  : -0.006 <br>Coef. Murder : 0.048 <br>Coef. Intercept : 0.3","<b> bootstrap dataset:  77 <\/b> <br>Coef. Urban  : -0.048 <br>Coef. Murder : 0.052 <br>Coef. Intercept : 2.63","<b> bootstrap dataset:  78 <\/b> <br>Coef. Urban  : -0.053 <br>Coef. Murder : 0.049 <br>Coef. Intercept : 3.041","<b> bootstrap dataset:  79 <\/b> <br>Coef. Urban  : -0.024 <br>Coef. Murder : 0.049 <br>Coef. Intercept : 1.37","<b> bootstrap dataset:  80 <\/b> <br>Coef. Urban  : -0.055 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 3.846","<b> bootstrap dataset:  81 <\/b> <br>Coef. Urban  : -0.055 <br>Coef. Murder : 0.056 <br>Coef. Intercept : 1.939","<b> bootstrap dataset:  82 <\/b> <br>Coef. Urban  : -0.06 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 4.346","<b> bootstrap dataset:  83 <\/b> <br>Coef. Urban  : -0.139 <br>Coef. Murder : 0.053 <br>Coef. Intercept : 8.273","<b> bootstrap dataset:  84 <\/b> <br>Coef. Urban  : -0.024 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 0.868","<b> bootstrap dataset:  85 <\/b> <br>Coef. Urban  : -0.051 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 3.861","<b> bootstrap dataset:  86 <\/b> <br>Coef. Urban  : -0.043 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 2.322","<b> bootstrap dataset:  87 <\/b> <br>Coef. Urban  : -0.051 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 3.472","<b> bootstrap dataset:  88 <\/b> <br>Coef. Urban  : -0.06 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 4.351","<b> bootstrap dataset:  89 <\/b> <br>Coef. Urban  : -0.06 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 4.311","<b> bootstrap dataset:  90 <\/b> <br>Coef. Urban  : -0.035 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 3.697","<b> bootstrap dataset:  91 <\/b> <br>Coef. Urban  : -0.042 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 2.981","<b> bootstrap dataset:  92 <\/b> <br>Coef. Urban  : -0.036 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 3.468","<b> bootstrap dataset:  93 <\/b> <br>Coef. Urban  : -0.031 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 2.343","<b> bootstrap dataset:  94 <\/b> <br>Coef. Urban  : -0.073 <br>Coef. Murder : 0.053 <br>Coef. Intercept : 3.074","<b> bootstrap dataset:  95 <\/b> <br>Coef. Urban  : -0.027 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 2.959","<b> bootstrap dataset:  96 <\/b> <br>Coef. Urban  : -0.062 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 5.034","<b> bootstrap dataset:  97 <\/b> <br>Coef. Urban  : -0.071 <br>Coef. Murder : 0.05 <br>Coef. Intercept : 4.03","<b> bootstrap dataset:  98 <\/b> <br>Coef. Urban  : -0.045 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 2.681","<b> bootstrap dataset:  99 <\/b> <br>Coef. Urban  : -0.037 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 2.721","<b> bootstrap dataset:  100 <\/b> <br>Coef. Urban  : -0.092 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 6.573","<b> bootstrap dataset:  101 <\/b> <br>Coef. Urban  : -0.07 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 4.805","<b> bootstrap dataset:  102 <\/b> <br>Coef. Urban  : -0.011 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 0.686","<b> bootstrap dataset:  103 <\/b> <br>Coef. Urban  : -0.042 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 3.398","<b> bootstrap dataset:  104 <\/b> <br>Coef. Urban  : -0.054 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 3.868","<b> bootstrap dataset:  105 <\/b> <br>Coef. Urban  : -0.089 <br>Coef. Murder : 0.048 <br>Coef. Intercept : 5.526","<b> bootstrap dataset:  106 <\/b> <br>Coef. Urban  : -0.038 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 3.227","<b> bootstrap dataset:  107 <\/b> <br>Coef. Urban  : -0.026 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 1.658","<b> bootstrap dataset:  108 <\/b> <br>Coef. Urban  : -0.051 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 3.801","<b> bootstrap dataset:  109 <\/b> <br>Coef. Urban  : -0.046 <br>Coef. Murder : 0.049 <br>Coef. Intercept : 2.163","<b> bootstrap dataset:  110 <\/b> <br>Coef. Urban  : -0.035 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 1.908","<b> bootstrap dataset:  111 <\/b> <br>Coef. Urban  : -0.046 <br>Coef. Murder : 0.051 <br>Coef. Intercept : 1.488","<b> bootstrap dataset:  112 <\/b> <br>Coef. Urban  : -0.062 <br>Coef. Murder : 0.038 <br>Coef. Intercept : 5.329","<b> bootstrap dataset:  113 <\/b> <br>Coef. Urban  : -0.001 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 1.03","<b> bootstrap dataset:  114 <\/b> <br>Coef. Urban  : -0.007 <br>Coef. Murder : 0.035 <br>Coef. Intercept : 1.786","<b> bootstrap dataset:  115 <\/b> <br>Coef. Urban  : -0.043 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 3.009","<b> bootstrap dataset:  116 <\/b> <br>Coef. Urban  : 0.015 <br>Coef. Murder : 0.037 <br>Coef. Intercept : -0.429","<b> bootstrap dataset:  117 <\/b> <br>Coef. Urban  : -0.047 <br>Coef. Murder : 0.034 <br>Coef. Intercept : 5.049","<b> bootstrap dataset:  118 <\/b> <br>Coef. Urban  : -0.099 <br>Coef. Murder : 0.052 <br>Coef. Intercept : 6.105","<b> bootstrap dataset:  119 <\/b> <br>Coef. Urban  : -0.019 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 2.205","<b> bootstrap dataset:  120 <\/b> <br>Coef. Urban  : -0.054 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 4.623","<b> bootstrap dataset:  121 <\/b> <br>Coef. Urban  : -0.033 <br>Coef. Murder : 0.037 <br>Coef. Intercept : 3.116","<b> bootstrap dataset:  122 <\/b> <br>Coef. Urban  : 0.022 <br>Coef. Murder : 0.04 <br>Coef. Intercept : -0.855","<b> bootstrap dataset:  123 <\/b> <br>Coef. Urban  : -0.074 <br>Coef. Murder : 0.048 <br>Coef. Intercept : 4.542","<b> bootstrap dataset:  124 <\/b> <br>Coef. Urban  : 0.003 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 0.376","<b> bootstrap dataset:  125 <\/b> <br>Coef. Urban  : -0.074 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 5.575","<b> bootstrap dataset:  126 <\/b> <br>Coef. Urban  : -0.051 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 3.875","<b> bootstrap dataset:  127 <\/b> <br>Coef. Urban  : -0.046 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 2.902","<b> bootstrap dataset:  128 <\/b> <br>Coef. Urban  : -0.027 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 2.807","<b> bootstrap dataset:  129 <\/b> <br>Coef. Urban  : -0.033 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 2.031","<b> bootstrap dataset:  130 <\/b> <br>Coef. Urban  : -0.064 <br>Coef. Murder : 0.051 <br>Coef. Intercept : 3.139","<b> bootstrap dataset:  131 <\/b> <br>Coef. Urban  : -0.038 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 3.744","<b> bootstrap dataset:  132 <\/b> <br>Coef. Urban  : -0.027 <br>Coef. Murder : 0.033 <br>Coef. Intercept : 3.749","<b> bootstrap dataset:  133 <\/b> <br>Coef. Urban  : -0.03 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 2.292","<b> bootstrap dataset:  134 <\/b> <br>Coef. Urban  : 0.016 <br>Coef. Murder : 0.038 <br>Coef. Intercept : 0.122","<b> bootstrap dataset:  135 <\/b> <br>Coef. Urban  : -0.108 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 6.746","<b> bootstrap dataset:  136 <\/b> <br>Coef. Urban  : -0.072 <br>Coef. Murder : 0.051 <br>Coef. Intercept : 3.986","<b> bootstrap dataset:  137 <\/b> <br>Coef. Urban  : -0.046 <br>Coef. Murder : 0.048 <br>Coef. Intercept : 2.801","<b> bootstrap dataset:  138 <\/b> <br>Coef. Urban  : -0.06 <br>Coef. Murder : 0.048 <br>Coef. Intercept : 3.113","<b> bootstrap dataset:  139 <\/b> <br>Coef. Urban  : -0.025 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 2.403","<b> bootstrap dataset:  140 <\/b> <br>Coef. Urban  : -0.056 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 4.895","<b> bootstrap dataset:  141 <\/b> <br>Coef. Urban  : -0.041 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 2.365","<b> bootstrap dataset:  142 <\/b> <br>Coef. Urban  : -0.094 <br>Coef. Murder : 0.049 <br>Coef. Intercept : 6.351","<b> bootstrap dataset:  143 <\/b> <br>Coef. Urban  : -0.037 <br>Coef. Murder : 0.037 <br>Coef. Intercept : 2.694","<b> bootstrap dataset:  144 <\/b> <br>Coef. Urban  : -0.053 <br>Coef. Murder : 0.051 <br>Coef. Intercept : 2.815","<b> bootstrap dataset:  145 <\/b> <br>Coef. Urban  : -0.003 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 0.842","<b> bootstrap dataset:  146 <\/b> <br>Coef. Urban  : -0.059 <br>Coef. Murder : 0.049 <br>Coef. Intercept : 3.546","<b> bootstrap dataset:  147 <\/b> <br>Coef. Urban  : -0.061 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 4.177","<b> bootstrap dataset:  148 <\/b> <br>Coef. Urban  : -0.048 <br>Coef. Murder : 0.038 <br>Coef. Intercept : 4.572","<b> bootstrap dataset:  149 <\/b> <br>Coef. Urban  : -0.046 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 3.836","<b> bootstrap dataset:  150 <\/b> <br>Coef. Urban  : -0.035 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 2.476","<b> bootstrap dataset:  151 <\/b> <br>Coef. Urban  : -0.029 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 2.567","<b> bootstrap dataset:  152 <\/b> <br>Coef. Urban  : -0.045 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 3.293","<b> bootstrap dataset:  153 <\/b> <br>Coef. Urban  : -0.089 <br>Coef. Murder : 0.054 <br>Coef. Intercept : 4.339","<b> bootstrap dataset:  154 <\/b> <br>Coef. Urban  : -0.04 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 2.743","<b> bootstrap dataset:  155 <\/b> <br>Coef. Urban  : -0.008 <br>Coef. Murder : 0.037 <br>Coef. Intercept : 2.241","<b> bootstrap dataset:  156 <\/b> <br>Coef. Urban  : -0.037 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 2.062","<b> bootstrap dataset:  157 <\/b> <br>Coef. Urban  : -0.059 <br>Coef. Murder : 0.038 <br>Coef. Intercept : 5.39","<b> bootstrap dataset:  158 <\/b> <br>Coef. Urban  : -0.02 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 1.589","<b> bootstrap dataset:  159 <\/b> <br>Coef. Urban  : -0.06 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 3.999","<b> bootstrap dataset:  160 <\/b> <br>Coef. Urban  : -0.046 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 3.516","<b> bootstrap dataset:  161 <\/b> <br>Coef. Urban  : -0.023 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 2.459","<b> bootstrap dataset:  162 <\/b> <br>Coef. Urban  : -0.036 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 2.269","<b> bootstrap dataset:  163 <\/b> <br>Coef. Urban  : -0.035 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 3.133","<b> bootstrap dataset:  164 <\/b> <br>Coef. Urban  : -0.074 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 6.196","<b> bootstrap dataset:  165 <\/b> <br>Coef. Urban  : -0.05 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 4.72","<b> bootstrap dataset:  166 <\/b> <br>Coef. Urban  : -0.042 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 3.315","<b> bootstrap dataset:  167 <\/b> <br>Coef. Urban  : -0.06 <br>Coef. Murder : 0.054 <br>Coef. Intercept : 3.041","<b> bootstrap dataset:  168 <\/b> <br>Coef. Urban  : 0.003 <br>Coef. Murder : 0.049 <br>Coef. Intercept : -0.843","<b> bootstrap dataset:  169 <\/b> <br>Coef. Urban  : -0.052 <br>Coef. Murder : 0.05 <br>Coef. Intercept : 2.939","<b> bootstrap dataset:  170 <\/b> <br>Coef. Urban  : -0.06 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 3.457","<b> bootstrap dataset:  171 <\/b> <br>Coef. Urban  : -0.018 <br>Coef. Murder : 0.051 <br>Coef. Intercept : 0.454","<b> bootstrap dataset:  172 <\/b> <br>Coef. Urban  : -0.08 <br>Coef. Murder : 0.048 <br>Coef. Intercept : 4.97","<b> bootstrap dataset:  173 <\/b> <br>Coef. Urban  : -0.067 <br>Coef. Murder : 0.048 <br>Coef. Intercept : 3.812","<b> bootstrap dataset:  174 <\/b> <br>Coef. Urban  : -0.053 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 4.029","<b> bootstrap dataset:  175 <\/b> <br>Coef. Urban  : 0.008 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 0.321","<b> bootstrap dataset:  176 <\/b> <br>Coef. Urban  : -0.067 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 4.947","<b> bootstrap dataset:  177 <\/b> <br>Coef. Urban  : -0.097 <br>Coef. Murder : 0.049 <br>Coef. Intercept : 5.785","<b> bootstrap dataset:  178 <\/b> <br>Coef. Urban  : -0.033 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 2.284","<b> bootstrap dataset:  179 <\/b> <br>Coef. Urban  : -0.061 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 4.593","<b> bootstrap dataset:  180 <\/b> <br>Coef. Urban  : -0.03 <br>Coef. Murder : 0.038 <br>Coef. Intercept : 2.462","<b> bootstrap dataset:  181 <\/b> <br>Coef. Urban  : -0.05 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 3.137","<b> bootstrap dataset:  182 <\/b> <br>Coef. Urban  : -0.046 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 3.647","<b> bootstrap dataset:  183 <\/b> <br>Coef. Urban  : -0.016 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 2.657","<b> bootstrap dataset:  184 <\/b> <br>Coef. Urban  : -0.058 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 3.886","<b> bootstrap dataset:  185 <\/b> <br>Coef. Urban  : -0.098 <br>Coef. Murder : 0.049 <br>Coef. Intercept : 6.099","<b> bootstrap dataset:  186 <\/b> <br>Coef. Urban  : -0.062 <br>Coef. Murder : 0.051 <br>Coef. Intercept : 3.568","<b> bootstrap dataset:  187 <\/b> <br>Coef. Urban  : -0.016 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 2.021","<b> bootstrap dataset:  188 <\/b> <br>Coef. Urban  : -0.031 <br>Coef. Murder : 0.049 <br>Coef. Intercept : 1.876","<b> bootstrap dataset:  189 <\/b> <br>Coef. Urban  : -0.047 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 3.999","<b> bootstrap dataset:  190 <\/b> <br>Coef. Urban  : -0.124 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 9.141","<b> bootstrap dataset:  191 <\/b> <br>Coef. Urban  : -0.032 <br>Coef. Murder : 0.048 <br>Coef. Intercept : 1.729","<b> bootstrap dataset:  192 <\/b> <br>Coef. Urban  : -0.046 <br>Coef. Murder : 0.056 <br>Coef. Intercept : 1.518","<b> bootstrap dataset:  193 <\/b> <br>Coef. Urban  : -0.015 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 0.938","<b> bootstrap dataset:  194 <\/b> <br>Coef. Urban  : -0.042 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 2.926","<b> bootstrap dataset:  195 <\/b> <br>Coef. Urban  : -0.029 <br>Coef. Murder : 0.037 <br>Coef. Intercept : 3.449","<b> bootstrap dataset:  196 <\/b> <br>Coef. Urban  : -0.017 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 0.934","<b> bootstrap dataset:  197 <\/b> <br>Coef. Urban  : -0.01 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 0.817","<b> bootstrap dataset:  198 <\/b> <br>Coef. Urban  : -0.051 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 3.431","<b> bootstrap dataset:  199 <\/b> <br>Coef. Urban  : -0.009 <br>Coef. Murder : 0.038 <br>Coef. Intercept : 1.909","<b> bootstrap dataset:  200 <\/b> <br>Coef. Urban  : -0.068 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 4.586","<b> bootstrap dataset:  201 <\/b> <br>Coef. Urban  : -0.049 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 2.884","<b> bootstrap dataset:  202 <\/b> <br>Coef. Urban  : -0.057 <br>Coef. Murder : 0.049 <br>Coef. Intercept : 3.404","<b> bootstrap dataset:  203 <\/b> <br>Coef. Urban  : -0.049 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 3.645","<b> bootstrap dataset:  204 <\/b> <br>Coef. Urban  : -0.043 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 3.161","<b> bootstrap dataset:  205 <\/b> <br>Coef. Urban  : -0.055 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 3.725","<b> bootstrap dataset:  206 <\/b> <br>Coef. Urban  : -0.036 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 2.415","<b> bootstrap dataset:  207 <\/b> <br>Coef. Urban  : -0.035 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 2.673","<b> bootstrap dataset:  208 <\/b> <br>Coef. Urban  : -0.004 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 1.124","<b> bootstrap dataset:  209 <\/b> <br>Coef. Urban  : -0.01 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 0.691","<b> bootstrap dataset:  210 <\/b> <br>Coef. Urban  : 0.013 <br>Coef. Murder : 0.044 <br>Coef. Intercept : -1.027","<b> bootstrap dataset:  211 <\/b> <br>Coef. Urban  : -0.036 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 2.635","<b> bootstrap dataset:  212 <\/b> <br>Coef. Urban  : -0.019 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 1.337","<b> bootstrap dataset:  213 <\/b> <br>Coef. Urban  : -0.038 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 2.191","<b> bootstrap dataset:  214 <\/b> <br>Coef. Urban  : -0.009 <br>Coef. Murder : 0.038 <br>Coef. Intercept : 1.644","<b> bootstrap dataset:  215 <\/b> <br>Coef. Urban  : -0.014 <br>Coef. Murder : 0.036 <br>Coef. Intercept : 3.517","<b> bootstrap dataset:  216 <\/b> <br>Coef. Urban  : -0.033 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 3.006","<b> bootstrap dataset:  217 <\/b> <br>Coef. Urban  : -0.032 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 3.423","<b> bootstrap dataset:  218 <\/b> <br>Coef. Urban  : -0.029 <br>Coef. Murder : 0.048 <br>Coef. Intercept : 1.172","<b> bootstrap dataset:  219 <\/b> <br>Coef. Urban  : -0.065 <br>Coef. Murder : 0.049 <br>Coef. Intercept : 4.001","<b> bootstrap dataset:  220 <\/b> <br>Coef. Urban  : -0.068 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 5.491","<b> bootstrap dataset:  221 <\/b> <br>Coef. Urban  : -0.031 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 2.557","<b> bootstrap dataset:  222 <\/b> <br>Coef. Urban  : -0.014 <br>Coef. Murder : 0.051 <br>Coef. Intercept : -0.453","<b> bootstrap dataset:  223 <\/b> <br>Coef. Urban  : -0.078 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 5.277","<b> bootstrap dataset:  224 <\/b> <br>Coef. Urban  : -0.053 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 3.942","<b> bootstrap dataset:  225 <\/b> <br>Coef. Urban  : -0.051 <br>Coef. Murder : 0.048 <br>Coef. Intercept : 3.093","<b> bootstrap dataset:  226 <\/b> <br>Coef. Urban  : -0.031 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 2.724","<b> bootstrap dataset:  227 <\/b> <br>Coef. Urban  : -0.04 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 2.658","<b> bootstrap dataset:  228 <\/b> <br>Coef. Urban  : -0.043 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 2.396","<b> bootstrap dataset:  229 <\/b> <br>Coef. Urban  : -0.053 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 3.658","<b> bootstrap dataset:  230 <\/b> <br>Coef. Urban  : -0.045 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 2.061","<b> bootstrap dataset:  231 <\/b> <br>Coef. Urban  : -0.049 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 2.938","<b> bootstrap dataset:  232 <\/b> <br>Coef. Urban  : -0.015 <br>Coef. Murder : 0.038 <br>Coef. Intercept : 2.061","<b> bootstrap dataset:  233 <\/b> <br>Coef. Urban  : -0.021 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 1.184","<b> bootstrap dataset:  234 <\/b> <br>Coef. Urban  : -0.119 <br>Coef. Murder : 0.05 <br>Coef. Intercept : 7.053","<b> bootstrap dataset:  235 <\/b> <br>Coef. Urban  : -0.065 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 6.118","<b> bootstrap dataset:  236 <\/b> <br>Coef. Urban  : -0.029 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 3.281","<b> bootstrap dataset:  237 <\/b> <br>Coef. Urban  : -0.036 <br>Coef. Murder : 0.048 <br>Coef. Intercept : 1.589","<b> bootstrap dataset:  238 <\/b> <br>Coef. Urban  : -0.022 <br>Coef. Murder : 0.036 <br>Coef. Intercept : 2.495","<b> bootstrap dataset:  239 <\/b> <br>Coef. Urban  : -0.021 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 2.284","<b> bootstrap dataset:  240 <\/b> <br>Coef. Urban  : -0.099 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 6.524","<b> bootstrap dataset:  241 <\/b> <br>Coef. Urban  : -0.009 <br>Coef. Murder : 0.038 <br>Coef. Intercept : 1.213","<b> bootstrap dataset:  242 <\/b> <br>Coef. Urban  : -0.049 <br>Coef. Murder : 0.051 <br>Coef. Intercept : 2.189","<b> bootstrap dataset:  243 <\/b> <br>Coef. Urban  : -0.029 <br>Coef. Murder : 0.05 <br>Coef. Intercept : 1.401","<b> bootstrap dataset:  244 <\/b> <br>Coef. Urban  : -0.013 <br>Coef. Murder : 0.038 <br>Coef. Intercept : 1.575","<b> bootstrap dataset:  245 <\/b> <br>Coef. Urban  : -0.04 <br>Coef. Murder : 0.054 <br>Coef. Intercept : 1.712","<b> bootstrap dataset:  246 <\/b> <br>Coef. Urban  : -0.02 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 1.778","<b> bootstrap dataset:  247 <\/b> <br>Coef. Urban  : -0.049 <br>Coef. Murder : 0.057 <br>Coef. Intercept : 2.44","<b> bootstrap dataset:  248 <\/b> <br>Coef. Urban  : -0.061 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 4.201","<b> bootstrap dataset:  249 <\/b> <br>Coef. Urban  : -0.105 <br>Coef. Murder : 0.05 <br>Coef. Intercept : 6.175","<b> bootstrap dataset:  250 <\/b> <br>Coef. Urban  : -0.126 <br>Coef. Murder : 0.05 <br>Coef. Intercept : 7.394","<b> bootstrap dataset:  251 <\/b> <br>Coef. Urban  : -0.031 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 1.814","<b> bootstrap dataset:  252 <\/b> <br>Coef. Urban  : -0.075 <br>Coef. Murder : 0.048 <br>Coef. Intercept : 5.045","<b> bootstrap dataset:  253 <\/b> <br>Coef. Urban  : -0.068 <br>Coef. Murder : 0.062 <br>Coef. Intercept : 2.699","<b> bootstrap dataset:  254 <\/b> <br>Coef. Urban  : -0.06 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 4.581","<b> bootstrap dataset:  255 <\/b> <br>Coef. Urban  : -0.04 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 3.342","<b> bootstrap dataset:  256 <\/b> <br>Coef. Urban  : -0.037 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 3.241","<b> bootstrap dataset:  257 <\/b> <br>Coef. Urban  : -0.05 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 3.406","<b> bootstrap dataset:  258 <\/b> <br>Coef. Urban  : -0.054 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 5.017","<b> bootstrap dataset:  259 <\/b> <br>Coef. Urban  : -0.09 <br>Coef. Murder : 0.052 <br>Coef. Intercept : 5.142","<b> bootstrap dataset:  260 <\/b> <br>Coef. Urban  : -0.096 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 6.333","<b> bootstrap dataset:  261 <\/b> <br>Coef. Urban  : -0.026 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 2.643","<b> bootstrap dataset:  262 <\/b> <br>Coef. Urban  : -0.092 <br>Coef. Murder : 0.052 <br>Coef. Intercept : 4.922","<b> bootstrap dataset:  263 <\/b> <br>Coef. Urban  : -0.065 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 5.036","<b> bootstrap dataset:  264 <\/b> <br>Coef. Urban  : -0.021 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 1.978","<b> bootstrap dataset:  265 <\/b> <br>Coef. Urban  : -0.033 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 2.22","<b> bootstrap dataset:  266 <\/b> <br>Coef. Urban  : -0.093 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 6.653","<b> bootstrap dataset:  267 <\/b> <br>Coef. Urban  : -0.056 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 3.327","<b> bootstrap dataset:  268 <\/b> <br>Coef. Urban  : -0.06 <br>Coef. Murder : 0.058 <br>Coef. Intercept : 2.897","<b> bootstrap dataset:  269 <\/b> <br>Coef. Urban  : -0.054 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 4.244","<b> bootstrap dataset:  270 <\/b> <br>Coef. Urban  : -0.045 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 3.941","<b> bootstrap dataset:  271 <\/b> <br>Coef. Urban  : -0.07 <br>Coef. Murder : 0.052 <br>Coef. Intercept : 3.42","<b> bootstrap dataset:  272 <\/b> <br>Coef. Urban  : -0.066 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 4.891","<b> bootstrap dataset:  273 <\/b> <br>Coef. Urban  : -0.033 <br>Coef. Murder : 0.038 <br>Coef. Intercept : 3.556","<b> bootstrap dataset:  274 <\/b> <br>Coef. Urban  : -0.041 <br>Coef. Murder : 0.055 <br>Coef. Intercept : 1.235","<b> bootstrap dataset:  275 <\/b> <br>Coef. Urban  : -0.039 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 2.322","<b> bootstrap dataset:  276 <\/b> <br>Coef. Urban  : -0.068 <br>Coef. Murder : 0.051 <br>Coef. Intercept : 4.117","<b> bootstrap dataset:  277 <\/b> <br>Coef. Urban  : -0.014 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 2.371","<b> bootstrap dataset:  278 <\/b> <br>Coef. Urban  : -0.021 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 2.299","<b> bootstrap dataset:  279 <\/b> <br>Coef. Urban  : -0.084 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 5.829","<b> bootstrap dataset:  280 <\/b> <br>Coef. Urban  : -0.044 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 2.965","<b> bootstrap dataset:  281 <\/b> <br>Coef. Urban  : -0.031 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 2.768","<b> bootstrap dataset:  282 <\/b> <br>Coef. Urban  : -0.067 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 4.112","<b> bootstrap dataset:  283 <\/b> <br>Coef. Urban  : -0.098 <br>Coef. Murder : 0.051 <br>Coef. Intercept : 5.386","<b> bootstrap dataset:  284 <\/b> <br>Coef. Urban  : -0.026 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 2.18","<b> bootstrap dataset:  285 <\/b> <br>Coef. Urban  : -0.012 <br>Coef. Murder : 0.038 <br>Coef. Intercept : 1.527","<b> bootstrap dataset:  286 <\/b> <br>Coef. Urban  : -0.026 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 2.852","<b> bootstrap dataset:  287 <\/b> <br>Coef. Urban  : -0.057 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 4.67","<b> bootstrap dataset:  288 <\/b> <br>Coef. Urban  : -0.053 <br>Coef. Murder : 0.052 <br>Coef. Intercept : 2.303","<b> bootstrap dataset:  289 <\/b> <br>Coef. Urban  : -0.038 <br>Coef. Murder : 0.034 <br>Coef. Intercept : 4.424","<b> bootstrap dataset:  290 <\/b> <br>Coef. Urban  : -0.034 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 2.66","<b> bootstrap dataset:  291 <\/b> <br>Coef. Urban  : -0.069 <br>Coef. Murder : 0.048 <br>Coef. Intercept : 4.211","<b> bootstrap dataset:  292 <\/b> <br>Coef. Urban  : -0.05 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 3.167","<b> bootstrap dataset:  293 <\/b> <br>Coef. Urban  : -0.017 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 1.814","<b> bootstrap dataset:  294 <\/b> <br>Coef. Urban  : -0.001 <br>Coef. Murder : 0.037 <br>Coef. Intercept : 1.603","<b> bootstrap dataset:  295 <\/b> <br>Coef. Urban  : -0.038 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 3.069","<b> bootstrap dataset:  296 <\/b> <br>Coef. Urban  : -0.08 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 5.458","<b> bootstrap dataset:  297 <\/b> <br>Coef. Urban  : -0.037 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 2.173","<b> bootstrap dataset:  298 <\/b> <br>Coef. Urban  : -0.064 <br>Coef. Murder : 0.048 <br>Coef. Intercept : 3.776","<b> bootstrap dataset:  299 <\/b> <br>Coef. Urban  : -0.021 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 1.912","<b> bootstrap dataset:  300 <\/b> <br>Coef. Urban  : -0.037 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 3.428","<b> bootstrap dataset:  301 <\/b> <br>Coef. Urban  : -0.051 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 3.781","<b> bootstrap dataset:  302 <\/b> <br>Coef. Urban  : -0.052 <br>Coef. Murder : 0.048 <br>Coef. Intercept : 2.999","<b> bootstrap dataset:  303 <\/b> <br>Coef. Urban  : -0.075 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 5.498","<b> bootstrap dataset:  304 <\/b> <br>Coef. Urban  : -0.037 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 2.349","<b> bootstrap dataset:  305 <\/b> <br>Coef. Urban  : -0.068 <br>Coef. Murder : 0.054 <br>Coef. Intercept : 3.055","<b> bootstrap dataset:  306 <\/b> <br>Coef. Urban  : -0.063 <br>Coef. Murder : 0.052 <br>Coef. Intercept : 2.708","<b> bootstrap dataset:  307 <\/b> <br>Coef. Urban  : -0.063 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 4.884","<b> bootstrap dataset:  308 <\/b> <br>Coef. Urban  : -0.014 <br>Coef. Murder : 0.038 <br>Coef. Intercept : 2.768","<b> bootstrap dataset:  309 <\/b> <br>Coef. Urban  : -0.035 <br>Coef. Murder : 0.054 <br>Coef. Intercept : 1.534","<b> bootstrap dataset:  310 <\/b> <br>Coef. Urban  : -0.038 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 2.927","<b> bootstrap dataset:  311 <\/b> <br>Coef. Urban  : -0.107 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 6.973","<b> bootstrap dataset:  312 <\/b> <br>Coef. Urban  : -0.017 <br>Coef. Murder : 0.038 <br>Coef. Intercept : 2.223","<b> bootstrap dataset:  313 <\/b> <br>Coef. Urban  : -0.054 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 3.179","<b> bootstrap dataset:  314 <\/b> <br>Coef. Urban  : -0.039 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 1.756","<b> bootstrap dataset:  315 <\/b> <br>Coef. Urban  : -0.077 <br>Coef. Murder : 0.049 <br>Coef. Intercept : 3.885","<b> bootstrap dataset:  316 <\/b> <br>Coef. Urban  : -0.047 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 4.309","<b> bootstrap dataset:  317 <\/b> <br>Coef. Urban  : -0.022 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 2.327","<b> bootstrap dataset:  318 <\/b> <br>Coef. Urban  : -0.042 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 3.341","<b> bootstrap dataset:  319 <\/b> <br>Coef. Urban  : -0.03 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 2.068","<b> bootstrap dataset:  320 <\/b> <br>Coef. Urban  : -0.067 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 4.984","<b> bootstrap dataset:  321 <\/b> <br>Coef. Urban  : -0.016 <br>Coef. Murder : 0.035 <br>Coef. Intercept : 2.617","<b> bootstrap dataset:  322 <\/b> <br>Coef. Urban  : -0.088 <br>Coef. Murder : 0.05 <br>Coef. Intercept : 5.115","<b> bootstrap dataset:  323 <\/b> <br>Coef. Urban  : -0.042 <br>Coef. Murder : 0.051 <br>Coef. Intercept : 2.673","<b> bootstrap dataset:  324 <\/b> <br>Coef. Urban  : -0.042 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 3.292","<b> bootstrap dataset:  325 <\/b> <br>Coef. Urban  : -0.057 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 4.75","<b> bootstrap dataset:  326 <\/b> <br>Coef. Urban  : -0.085 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 6.376","<b> bootstrap dataset:  327 <\/b> <br>Coef. Urban  : -0.101 <br>Coef. Murder : 0.063 <br>Coef. Intercept : 4.505","<b> bootstrap dataset:  328 <\/b> <br>Coef. Urban  : -0.075 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 6","<b> bootstrap dataset:  329 <\/b> <br>Coef. Urban  : -0.006 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 1.064","<b> bootstrap dataset:  330 <\/b> <br>Coef. Urban  : -0.036 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 2.391","<b> bootstrap dataset:  331 <\/b> <br>Coef. Urban  : -0.091 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 5.32","<b> bootstrap dataset:  332 <\/b> <br>Coef. Urban  : -0.028 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 3.008","<b> bootstrap dataset:  333 <\/b> <br>Coef. Urban  : -0.061 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 5.573","<b> bootstrap dataset:  334 <\/b> <br>Coef. Urban  : -0.023 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 2.21","<b> bootstrap dataset:  335 <\/b> <br>Coef. Urban  : -0.046 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 3.074","<b> bootstrap dataset:  336 <\/b> <br>Coef. Urban  : -0.057 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 3.274","<b> bootstrap dataset:  337 <\/b> <br>Coef. Urban  : -0.092 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 5.632","<b> bootstrap dataset:  338 <\/b> <br>Coef. Urban  : -0.049 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 2.606","<b> bootstrap dataset:  339 <\/b> <br>Coef. Urban  : -0.011 <br>Coef. Murder : 0.038 <br>Coef. Intercept : 2.248","<b> bootstrap dataset:  340 <\/b> <br>Coef. Urban  : -0.066 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 3.738","<b> bootstrap dataset:  341 <\/b> <br>Coef. Urban  : -0.026 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 1.791","<b> bootstrap dataset:  342 <\/b> <br>Coef. Urban  : -0.047 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 3.072","<b> bootstrap dataset:  343 <\/b> <br>Coef. Urban  : -0.053 <br>Coef. Murder : 0.049 <br>Coef. Intercept : 3.578","<b> bootstrap dataset:  344 <\/b> <br>Coef. Urban  : -0.052 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 3.38","<b> bootstrap dataset:  345 <\/b> <br>Coef. Urban  : -0.039 <br>Coef. Murder : 0.05 <br>Coef. Intercept : 2.23","<b> bootstrap dataset:  346 <\/b> <br>Coef. Urban  : -0.01 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 0.65","<b> bootstrap dataset:  347 <\/b> <br>Coef. Urban  : -0.042 <br>Coef. Murder : 0.048 <br>Coef. Intercept : 2.129","<b> bootstrap dataset:  348 <\/b> <br>Coef. Urban  : -0.071 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 4.888","<b> bootstrap dataset:  349 <\/b> <br>Coef. Urban  : -0.033 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 2.95","<b> bootstrap dataset:  350 <\/b> <br>Coef. Urban  : -0.012 <br>Coef. Murder : 0.051 <br>Coef. Intercept : 0.497","<b> bootstrap dataset:  351 <\/b> <br>Coef. Urban  : 0.008 <br>Coef. Murder : 0.045 <br>Coef. Intercept : -0.795","<b> bootstrap dataset:  352 <\/b> <br>Coef. Urban  : -0.056 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 3.844","<b> bootstrap dataset:  353 <\/b> <br>Coef. Urban  : -0.062 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 3.586","<b> bootstrap dataset:  354 <\/b> <br>Coef. Urban  : 0.002 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 0.541","<b> bootstrap dataset:  355 <\/b> <br>Coef. Urban  : -0.026 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 2.364","<b> bootstrap dataset:  356 <\/b> <br>Coef. Urban  : -0.018 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 1.578","<b> bootstrap dataset:  357 <\/b> <br>Coef. Urban  : -0.053 <br>Coef. Murder : 0.036 <br>Coef. Intercept : 5.471","<b> bootstrap dataset:  358 <\/b> <br>Coef. Urban  : -0.109 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 7.271","<b> bootstrap dataset:  359 <\/b> <br>Coef. Urban  : -0.067 <br>Coef. Murder : 0.049 <br>Coef. Intercept : 4.087","<b> bootstrap dataset:  360 <\/b> <br>Coef. Urban  : -0.042 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 2.347","<b> bootstrap dataset:  361 <\/b> <br>Coef. Urban  : -0.021 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 2.477","<b> bootstrap dataset:  362 <\/b> <br>Coef. Urban  : -0.061 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 4.866","<b> bootstrap dataset:  363 <\/b> <br>Coef. Urban  : -0.012 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 1.455","<b> bootstrap dataset:  364 <\/b> <br>Coef. Urban  : -0.035 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 2.987","<b> bootstrap dataset:  365 <\/b> <br>Coef. Urban  : -0.066 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 3.848","<b> bootstrap dataset:  366 <\/b> <br>Coef. Urban  : -0.026 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 2.241","<b> bootstrap dataset:  367 <\/b> <br>Coef. Urban  : -0.015 <br>Coef. Murder : 0.048 <br>Coef. Intercept : 0.958","<b> bootstrap dataset:  368 <\/b> <br>Coef. Urban  : -0.034 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 2.082","<b> bootstrap dataset:  369 <\/b> <br>Coef. Urban  : -0.055 <br>Coef. Murder : 0.049 <br>Coef. Intercept : 3.021","<b> bootstrap dataset:  370 <\/b> <br>Coef. Urban  : -0.02 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 1.842","<b> bootstrap dataset:  371 <\/b> <br>Coef. Urban  : -0.069 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 4.5","<b> bootstrap dataset:  372 <\/b> <br>Coef. Urban  : -0.016 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 1.401","<b> bootstrap dataset:  373 <\/b> <br>Coef. Urban  : -0.068 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 5.023","<b> bootstrap dataset:  374 <\/b> <br>Coef. Urban  : -0.045 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 4.346","<b> bootstrap dataset:  375 <\/b> <br>Coef. Urban  : -0.068 <br>Coef. Murder : 0.049 <br>Coef. Intercept : 3.75","<b> bootstrap dataset:  376 <\/b> <br>Coef. Urban  : -0.045 <br>Coef. Murder : 0.05 <br>Coef. Intercept : 2.207","<b> bootstrap dataset:  377 <\/b> <br>Coef. Urban  : -0.057 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 3.047","<b> bootstrap dataset:  378 <\/b> <br>Coef. Urban  : -0.068 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 5.258","<b> bootstrap dataset:  379 <\/b> <br>Coef. Urban  : -0.084 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 6.106","<b> bootstrap dataset:  380 <\/b> <br>Coef. Urban  : -0.012 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 0.693","<b> bootstrap dataset:  381 <\/b> <br>Coef. Urban  : -0.067 <br>Coef. Murder : 0.05 <br>Coef. Intercept : 4.343","<b> bootstrap dataset:  382 <\/b> <br>Coef. Urban  : -0.007 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 1.272","<b> bootstrap dataset:  383 <\/b> <br>Coef. Urban  : -0.063 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 3.838","<b> bootstrap dataset:  384 <\/b> <br>Coef. Urban  : -0.06 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 3.702","<b> bootstrap dataset:  385 <\/b> <br>Coef. Urban  : -0.01 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 1.77","<b> bootstrap dataset:  386 <\/b> <br>Coef. Urban  : -0.063 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 4.212","<b> bootstrap dataset:  387 <\/b> <br>Coef. Urban  : -0.04 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 2.611","<b> bootstrap dataset:  388 <\/b> <br>Coef. Urban  : -0.067 <br>Coef. Murder : 0.049 <br>Coef. Intercept : 3.794","<b> bootstrap dataset:  389 <\/b> <br>Coef. Urban  : -0.053 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 4.228","<b> bootstrap dataset:  390 <\/b> <br>Coef. Urban  : -0.036 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 2.298","<b> bootstrap dataset:  391 <\/b> <br>Coef. Urban  : -0.057 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 4.239","<b> bootstrap dataset:  392 <\/b> <br>Coef. Urban  : -0.029 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 2.382","<b> bootstrap dataset:  393 <\/b> <br>Coef. Urban  : -0.054 <br>Coef. Murder : 0.048 <br>Coef. Intercept : 2.889","<b> bootstrap dataset:  394 <\/b> <br>Coef. Urban  : 0.008 <br>Coef. Murder : 0.049 <br>Coef. Intercept : -0.336","<b> bootstrap dataset:  395 <\/b> <br>Coef. Urban  : -0.014 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 0.815","<b> bootstrap dataset:  396 <\/b> <br>Coef. Urban  : 0.004 <br>Coef. Murder : 0.038 <br>Coef. Intercept : 0.947","<b> bootstrap dataset:  397 <\/b> <br>Coef. Urban  : -0.03 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 2.108","<b> bootstrap dataset:  398 <\/b> <br>Coef. Urban  : -0.028 <br>Coef. Murder : 0.049 <br>Coef. Intercept : 1.302","<b> bootstrap dataset:  399 <\/b> <br>Coef. Urban  : -0.031 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 3.377"],"hoverinfo":["text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text"],"showlegend":false,"marker":{"color":"rgba(0, 0, 0, 0.5)","line":{"color":"rgba(31,119,180,1)"}},"type":"scatter","error_y":{"color":"rgba(31,119,180,1)"},"error_x":{"color":"rgba(31,119,180,1)"},"line":{"color":"rgba(31,119,180,1)"},"xaxis":"x","yaxis":"y","frame":null}],"highlight":{"on":"plotly_click","persistent":false,"dynamic":false,"selectize":false,"opacityDim":0.20000000000000001,"selected":{"opacity":1},"debounce":0},"shinyEvents":["plotly_hover","plotly_click","plotly_selected","plotly_relayout","plotly_brushed","plotly_brushing","plotly_clickannotation","plotly_doubleclick","plotly_deselect","plotly_afterplot","plotly_sunburstclick"],"base_url":"https://plot.ly"},"evals":[],"jsHooks":[]}</script>
```

**Hypothesis Testing**
We can also use an $F$ test for any $q$ hypotheses. Specifically, when $q$ hypotheses *restrict* a model, the degrees of freedom drop from $k_{u}$ to $k_{r}$ and the residual sum of squares $RSS=\sum_{i}(y_{i}-\widehat{y}_{i})^2$ typically increases. We compute the statistic
$$
F_{q} = \frac{(RSS_{r}-RSS_{u})/(k_{u}-k_{r})}{RSS_{u}/(N-k_{u})}.
$$
When the restricted model is a simple intercept, $F_{q}$ can also be written in terms of $R^2$ or adjusted $R^2$. For some intuition on hypothesis testing, we examine how the $R^2$ statistic varies with bootstrap samples. Specifically, compute a null $R^2$ distribution by randomly reshuffling the outcomes and compare it to the observed $R^2$.

``` r
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

hist(R2adj_sim0, xlim=c(-.1,1), breaks=25, border=NA,
    main='', xlab=expression('adj.'~R[b]^2))
abline(v=summary(reg)$adj.r.squared, lwd=2, col=2)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-26-1.png" width="672" />

Under some additional assumptions $F_{q}$ follows an F-distribution. Note that *hypothesis testing is not to be done routinely*, as complications arise when testing multiple hypothesis sequentially. See https://online.stat.psu.edu/stat501/lesson/6/6.2

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
When, as commonly done, the factors are modeled as being additively seperable, they are modeled as either "fixed" or "random" effects.

Simply including the factors into the OLS regression yields a "dummy variable" fixed effects estimator.

``` r
fe_reg0 <- lm(y~x+fo+fu, dat_f)
```
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
##        x 
## 1.094665
```

``` r
fixef(fe_reg1)[1:2]
```

```
## $fo
##         0         1         2         3         4 
##  7.431314 10.108692 14.842376 23.437463 43.811157 
## 
## $fu
##         A         B 
##   0.00000 -22.99464
```

``` r
## Compare Coefficients
coef( lm(y~-1+x+fo+fu, dat_f) )
```

```
##          x        fo0        fo1        fo2        fo3        fo4        fuB 
##   1.094665   7.431314  10.108692  14.842376  23.437463  43.811157 -22.994641
```

With fixed effects, we can also compute averages for each group and construct a "between estimator" $\overline{y}_i = \alpha + \overline{x}_i \beta$. Or we can subtract the average from each group to construct a "within estimator", $(y_{it} - \overline{y}_i) = (x_{it}-\overline{x}_i)\beta$. 

But note that many factors are not additively separable. This is easy to check with an F-test;

``` r
reg1 <- lm(y~-1+x+fo*fu, dat_f)
reg2 <- lm(y~-1+x*fo*fu, dat_f)
anova(reg1, reg2)
```

```
## Analysis of Variance Table
## 
## Model 1: y ~ -1 + x + fo * fu
## Model 2: y ~ -1 + x * fo * fu
##   Res.Df     RSS Df Sum of Sq      F    Pr(>F)    
## 1    989 10151.6                                  
## 2    980  6305.8  9    3845.8 66.409 < 2.2e-16 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
```


With *Random Effects*, the factor variable is modeled as coming from a distribution that is uncorrelated with the regressors. This is rarely used in economics today, and mostly included for historical reasons and a few cases where fixed effects cannot be estimates.

<!-- 
> The labels "random effects" and "fixed effects" are misleading. These are labels which arose in the early literature and we are stuck with these labels today. In a previous era regressors were viewed as "fixed". Viewing the individual effect as an unobserved regressor leads to the label of the individual effect as "fixed". Today, we rarely refer to regressors as "fixed" when dealing with observational data. We view all variables as random. Consequently describing u i as "fixed" does not make much sense and it is hardly a contrast with the "random effect" label since under either assumption u i is treated as random. Once again, the labels are unfortunate but the key difference is whether u i is correlated with the regressors.
-->


**Test for Break Points**


``` r
library(AER); data(CASchools)
CASchools$score <- (CASchools$read + CASchools$math) / 2
reg <- lm(score~income, data=CASchools)

## F Test for Break
reg2 <- lm(score ~ income*I(income>15), data=CASchools)
anova(reg, reg2)

## Chow Test for Break
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

## See also
## strucchange::sctest(y~x, data=xy, type="Chow", point=.5)
## strucchange::Fstats(y~x, data=xy)

## To Find Changes
## segmented::segmented(reg)
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
##    7.621302    2.255451    1.106616
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

<img src="03-ROLS_files/figure-html/unnamed-chunk-33-1.png" width="672" />


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
    abline(v=mean(Coefs[i,]), col=1)
}
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-34-1.png" width="672" />
In general, you can interpret your OLS coefficients as "conditional correlations". If further hypothesis testing suggests the relationships are actually additively separable and linear, then you also have the structural interpretation of "marginal effect".


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
[ \widehat{y^{(\lambda)}}_{i} \cdot \lambda ]^{1/\lambda} -1 & \lambda  \neq 0 \\
exp( \widehat{y^{(\lambda)}}_{i}) -1 &  \lambda=0
\end{cases}.
$$


It is easiest to optimize parameters in a 2-step procedure called  `concentrated optimization'. We first solve for $\widehat{\beta}(\rho,\lambda)$ and compute the mean squared error $MSE(\rho,\lambda)$. We then find the $(\rho,\lambda)$ which minimizes $MSE$.

``` r
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
layout(matrix(1:2,ncol=2), width=c(3,1), height=c(1,1))
par(mar=c(4,4,2,0))
plot(lambda~rho,rl_df, cex=8, pch=15,
    xlab=expression(rho),
    ylab=expression(lambda),
    col=hcl.colors(25)[cut(1/rl_df$mse,25)])
## Which min
rl0 <- rl_df[which.min(rl_df$mse),c('rho','lambda')]
points(rl0$rho, rl0$lambda, pch=0, col=1, cex=8, lwd=2)
## Legend
plot(c(0,2),c(0,1), type='n', axes=F,
    xlab='',ylab='', cex.main=.8,
    main=expression(frac(1,'Mean Square Error')))
rasterImage(as.raster(matrix(hcl.colors(25), ncol=1)), 0, 0, 1,1)
text(x=1.5, y=seq(0,1,l=10), cex=.5,
    labels=levels(cut(1/rl_df$mse,10, right=F)))
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-35-1.png" width="960" style="display: block; margin: auto;" />



``` r
## Plot for Specific Comparisons
Xr <- bxcx(X,rl0[[1]])
Yr <- bxcx(Y,rl0[[2]])
Datr <- cbind(Murder=Yr,Xr)
Regr <- lm(Murder~Assault+UrbanPop, data=Datr)
Predr <- bxcx_inv(predict(Regr),rl0[[2]])

cols <- c(rgb(1,0,0,.5), col=rgb(0,0,1,.5))
plot(Y, Predr, pch=16, col=cols[1], ylab='Prediction')
points(Y, predict(reg), pch=16, col=cols[2])
legend('topleft', pch=c(16), col=cols,
    title=expression(rho~', '~lambda),
    legend=c(  paste0(rl0, collapse=', '),'1, 1') )
abline(a=0,b=1, lty=2)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-36-1.png" width="672" />

Note that the default hypothesis testing procedures do not account for you trying out different transformations. Specification searches deflate standard errors and are a major source for false discoveries.

##  Diagnostics

There's little sense in getting great standard errors for a terrible model. Plotting your regression object a simple and easy step to help diagnose whether your model is in some way bad.

``` r
#reg <- lm(Murder~Assault+UrbanPop, data=USArrests)
par(mfrow=c(2,2))
plot(reg)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-37-1.png" width="672" />
We now go through what these figures show, and then some additional

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

<img src="03-ROLS_files/figure-html/unnamed-chunk-38-1.png" width="672" />
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
This is when one explanatory variable in a multiple linear regression model can be linearly predicted from the others with a substantial degree of accuracy. Coefficient estimates may change erratically in response to small changes in the model or the data. (In the extreme case where there are more variables than observations $K>\geq N$, $X'X$ has an infinite number of solutions and is not invertible.) To diagnose this, we can use the Variance Inflation Factor
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

<img src="03-ROLS_files/figure-html/unnamed-chunk-44-1.png" width="672" />

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
##       P           D        S
## [1,]  8  1.51844954 0.254882
## [2,]  9  0.71844954 1.254882
## [3,] 10 -0.08155046 2.254882
```

``` r
## Market Equilibrium Finder
eq_fun <- function(demand, supply, P){
    ## Compute EQ (what we observe)
    eq_id <- which.min( abs(demand-supply) )
    eq <- c(P=P[eq_id], Q=demand[eq_id]) 
    return(eq)
}
```



``` r
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

<img src="03-ROLS_files/figure-html/unnamed-chunk-46-1.png" width="672" />

Now regress quantity ("Y") on price ("X"): $\widehat{\beta}_{OLS} = Cov(Q^{*}, P^{*}) / Var(P^{*})$. You get a number back, but it is hard to interpret meaningfully. 

``` r
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
## -0.47598 -0.12771  0.00999  0.12593  0.51622 
## 
## Coefficients:
##             Estimate Std. Error t value Pr(>|t|)
## (Intercept)  0.31875    0.46982   0.678    0.498
## P            0.06226    0.05281   1.179    0.239
## 
## Residual standard error: 0.175 on 298 degrees of freedom
## Multiple R-squared:  0.004642,	Adjusted R-squared:  0.001302 
## F-statistic:  1.39 on 1 and 298 DF,  p-value: 0.2394
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

<img src="03-ROLS_files/figure-html/unnamed-chunk-48-1.png" width="672" />

We are not quite done yet, however. We have pooled two datasets that are seperately problematic, and the noisiness of the process within each group affects our OLS estimate: $\widehat{\beta}_{OLS}=Cov(Q^{*}, P^{*}) / Var(P^{*})$.

``` r
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
## -0.65576 -0.15985  0.00242  0.15741  0.78770 
## 
## Coefficients:
##             Estimate Std. Error t value Pr(>|t|)    
## (Intercept)  6.60725    0.17631   37.48   <2e-16 ***
## P           -0.63705    0.02077  -30.67   <2e-16 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 0.2355 on 598 degrees of freedom
## Multiple R-squared:  0.6114,	Adjusted R-squared:  0.6107 
## F-statistic: 940.7 on 1 and 598 DF,  p-value: < 2.2e-16
```
Although the individual observations are noisy, we can compute the change in the expected values $d \mathbb{E}[Q^{*}] / d \mathbb{E}[P^{*}] =-B_{D}$. Empirically, this is estimated via the change in average value.

``` r
## Wald (1940) Estimate
dat_mean <- rbind(
    colMeans(dat2[dat2$cost==1,1:2]),
    colMeans(dat2[dat2$cost==2,1:2]))
dat_mean
```

```
##             P         Q
## [1,] 8.894567 0.8725129
## [2,] 8.057467 1.5426295
```

``` r
B_est <- diff(dat_mean[,2])/diff(dat_mean[,1])
round(B_est, 2)
```

```
## [1] -0.8
```
We can also seperately recover $d \mathbb{E}[Q^{*}] / d \mathbb{E}[A_{S}]$ and $d \mathbb{E}[P^{*}] / d \mathbb{E}[A_{S}]$ from seperate regressions

``` r
## Heckman (2000, p.58) Estimate
ols_1 <- lm(P~cost, data=dat2)
ols_2 <- lm(Q~cost, data=dat2)
B_est2 <- coef(ols_2)/coef(ols_1)
round(B_est2[[2]],2)
```

```
## [1] -0.8
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
## -0.52640 -0.11388  0.00834  0.11960  0.51531 
## 
## Coefficients:
##             Estimate Std. Error t value Pr(>|t|)    
## (Intercept)  7.99281    0.14355   55.68   <2e-16 ***
## Phat        -0.80052    0.01692  -47.32   <2e-16 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 0.1734 on 598 degrees of freedom
## Multiple R-squared:  0.7893,	Adjusted R-squared:  0.7889 
## F-statistic:  2240 on 1 and 598 DF,  p-value: < 2.2e-16
```

``` r
## One Stage Instrumental Variables Estimate
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
## (Intercept)  7.992805   0.204789  39.0296 < 2.2e-16 ***
## fit_P       -0.800522   0.024132 -33.1732 < 2.2e-16 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## RMSE: 0.246992   Adj. R2: 0.570394
## F-test (1st stage), P: stat = 2,680.0, p < 2.2e-16, on 1 and 598 DoF.
##            Wu-Hausman: stat =   517.2, p < 2.2e-16, on 1 and 597 DoF.
```

**Within Group Variance**
You can experiment with the effect of different variances on both OLS and IV in the code below. And note that if we had multiple supply shifts and recorded their magnitudes, then we could recover more information about demand, perhaps tracing it out entirely.

``` r
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
## Ed_sigma.0.25           -0.64         -0.63      -0.74
## Ed_sigma.1               0.34          0.39      -0.08
## 
## [[2]]
##                Es_sigma.0.001 Es_sigma.0.25 Es_sigma.1
## Ed_sigma.0.001          -0.80         -0.80      -0.80
## Ed_sigma.0.25           -0.81         -0.82      -0.81
## Ed_sigma.1              -0.75         -0.85      -0.82
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


``` r
dat2$T <- 1:nrow(dat2)

plot(P~T, dat2, main='Effect of Cost Shock on Price', 
    font.main=1, pch=16, col=grey(0,.25))
regP1 <- lm(P~T, dat2[dat2$cost==1,]) 
lines(regP1$model$T, predict(regP1), col=2)
regP2 <- lm(P~T, dat2[dat2$cost==2,]) 
lines(regP2$model$T, predict(regP2), col=4)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-55-1.png" width="672" />

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
## -0.72985 -0.12878 -0.00566  0.13415  0.54335 
## 
## Coefficients:
##               Estimate Std. Error t value Pr(>|t|)    
## (Intercept)  8.888e+00  2.295e-02 387.246   <2e-16 ***
## T            4.199e-05  1.322e-04   0.318    0.751    
## cost2       -8.723e-01  6.484e-02 -13.453   <2e-16 ***
## T:cost2      5.008e-05  1.869e-04   0.268    0.789    
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 0.1983 on 596 degrees of freedom
## Multiple R-squared:  0.8177,	Adjusted R-squared:  0.8168 
## F-statistic: 891.4 on 3 and 596 DF,  p-value: < 2.2e-16
```


``` r
plot(Q~T, dat2, main='Effect of Cost Shock on Quantity',
    font.main=1, pch=16, col=grey(0,.15))
regQ1 <- lm(Q~T, dat2[dat2$cost==1,]) 
lines(regQ1$model$T, predict(regQ1), col=2)
regQ2 <- lm(Q~T, dat2[dat2$cost==2,]) 
lines(regQ2$model$T, predict(regQ2), col=4)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-56-1.png" width="672" />

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
## -0.52762 -0.11690  0.00717  0.11822  0.51617 
## 
## Coefficients:
##              Estimate Std. Error t value Pr(>|t|)    
## (Intercept) 8.715e-01  2.010e-02  43.353   <2e-16 ***
## T           6.737e-06  1.158e-04   0.058    0.954    
## cost2       6.377e-01  5.679e-02  11.230   <2e-16 ***
## T:cost2     6.740e-05  1.637e-04   0.412    0.681    
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 0.1737 on 596 degrees of freedom
## Multiple R-squared:  0.7894,	Adjusted R-squared:  0.7883 
## F-statistic: 744.7 on 3 and 596 DF,  p-value: < 2.2e-16
```

Remember that this is effect is *local*: different magnitudes of the cost shock or different demand curves generally yeild different estimates.

## Difference in Differences (DID)

The basic idea here is to examine how a variable changes in response to an exogenous shock, *compared to a control group*. 


``` r
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
plot(P~T, dat2, main='Effect of Cost Shock on Price',
    font.main=1, pch=17,col=rgb(0,0,1,.25))
points(P~T, dat3, pch=16, col=rgb(1,0,0,.25))

plot(Q~T, dat2, main='Effect of Cost Shock on Quantity',
    font.main=1, pch=17,col=rgb(0,0,1,.25))
points(Q~T, dat3, pch=16, col=rgb(1,0,0,.25))
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-57-1.png" width="672" />

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
## -0.72985 -0.13572  0.00478  0.13477  0.54335 
## 
## Coefficients:
##               Estimate Std. Error t value Pr(>|t|)    
## (Intercept)  8.896e+00  1.207e-02 737.086   <2e-16 ***
## T           -5.354e-05  4.018e-05  -1.333    0.183    
## cost2       -8.805e-01  6.231e-02 -14.130   <2e-16 ***
## T:cost2      1.456e-04  1.392e-04   1.046    0.296    
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 0.1999 on 1196 degrees of freedom
## Multiple R-squared:  0.7625,	Adjusted R-squared:  0.762 
## F-statistic:  1280 on 3 and 1196 DF,  p-value: < 2.2e-16
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
##      Min       1Q   Median       3Q      Max 
## -0.58969 -0.11421  0.00362  0.11478  0.58059 
## 
## Coefficients:
##              Estimate Std. Error t value Pr(>|t|)    
## (Intercept) 8.784e-01  1.059e-02  82.961   <2e-16 ***
## T           5.139e-05  3.524e-05   1.458    0.145    
## cost2       6.308e-01  5.466e-02  11.541   <2e-16 ***
## T:cost2     2.275e-05  1.221e-04   0.186    0.852    
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 0.1753 on 1196 degrees of freedom
## Multiple R-squared:  0.7221,	Adjusted R-squared:  0.7214 
## F-statistic:  1036 on 3 and 1196 DF,  p-value: < 2.2e-16
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

``` r
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
    pch=16, col=grey(.5,.5), font.main=1,
    main=paste0('Random Dataset ', i,":   p=",
        formatC(p,digits=2, format='fg')))
abline(reg_i)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-58-1.png" width="672" />

``` r
#summary(reg_i)
```



``` r
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
## Your data is not made up in the computer (hopefully!)
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

``` r
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


``` r
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

<img src="03-ROLS_files/figure-html/unnamed-chunk-62-1.png" width="672" />



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

<img src="03-ROLS_files/figure-html/unnamed-chunk-63-1.png" width="672" />



``` r
## Include an intercept to regression 1
#reg2 <-  lm(cage_films ~ science_spending, data=vigen_csv)
#suppressMessages(library(stargazer))
#stargazer(reg1, reg2, type='html')
```


We now run IV regressions for different variable combinations in the dataset

``` r
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

plot(ecdf(pvals), xlab='p-value', ylab='CDF', font.main=1,
    main='Frequency IV is Statistically Significant')
abline(v=c(.01,.05), col=c(2,4))
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-65-1.png" width="672" />

``` r
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

<img src="03-ROLS_files/figure-html/unnamed-chunk-66-1.png" width="672" />


**IV**
First, find an instrument that satisfy various statistical criterion to provide a causal estimate of $X_{2}$ on $X_{1}$.

``` r
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
## After experimenting with different instruments
## you can find even stronger results!
```


**RDD**
Second, find a large discrete change in the data that you can associate with a policy. You can use this as an instrument too, also providing a causal estimate of $X_{2}$ on $X_{1}$.



``` r
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

<img src="03-ROLS_files/figure-html/unnamed-chunk-68-1.png" width="672" />


``` r
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


``` r
## Find a reversal of fortune
## (A good story always goes well with a nice pre-trend)
n2 <- 318
wind2 <- c(n2-20,n2+20)
plot(random_walk2, pch=16, col=rgb(0,0,1,.5),
    xlim=wind2, ylim=c(-15,15), xlab='Time', ylab='Random Value')
points(random_walk1, pch=16, col=rgb(1,0,0,.5))
abline(v=n2, lty=2)
```

<img src="03-ROLS_files/figure-html/unnamed-chunk-70-1.png" width="672" />


``` r
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

