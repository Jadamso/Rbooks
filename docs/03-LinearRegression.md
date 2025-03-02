# (PART) Linear Regression in R {-}



This section overviews linear regression models from the perspective that ``all models are wrong, but some are useful''. All linear models are estimated via Ordinary Least Squares (OLS). For more in-depth introductions, which typically begin by assuming a linear data generating process, see https://jadamso.github.io/Rbooks/ordinary-least-squares.html#more-literature. 

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
plot(y~x, xy, col=grey(0,.5), pch=16)
```

<img src="03-LinearRegression_files/figure-html/unnamed-chunk-3-1.png" width="672" />

## Linear Correlation

To quantitatively describe the relationship between $Y$ and $X$, you can compute the covariance:
$$
\widehat{Cov}(X,Y) =  \sum_{i} [X_i - \bar{x}] [Y_i - \bar{y}]
$$

``` r
cov(xy)
```

```
##           y          x
## y 18.970465   4.386204
## x  4.386204 209.518776
```
Note that $\widehat{Cov}(X,X)=\widehat{Var}(X)$.
For ease of interpretation, we rescale this statistic to always lay between $-1$ and $1$ 
$$
\widehat{Cor}(X,Y) = \frac{\widehat{Cov}(X,Y) }{ \sqrt{\widehat{Cov}(X,X)} \sqrt{\widehat{Cov}(Y,Y)}}
$$

``` r
cor(xy)
```

```
##            y          x
## y 1.00000000 0.06957262
## x 0.06957262 1.00000000
```

## Simple Linear Regression
Simple Linear Regression refers to fitting a linear model to bivariate data. Specifically, the model is 
$$
y_i=\beta_{0}+\beta_{1} x_i+\epsilon_{i}
$$
and our objective function is
$$
min_{\beta_{0}, \beta_{1}} \sum_{i=1}^{N} \left( \epsilon_{i} \right)^2 =  min_{\beta_{0}, \beta_{1}} \sum_{i=1} \left( y_i - [\beta_{0}+\beta_{1} x_i] \right).
$$
Minimizing the sum of squared errors yields parameter estimates
$$
\hat{\beta_{0}}=\bar{y}-\hat{\beta_{1}}\bar{x} = \widehat{\mathbb{E}}[Y] - \hat{\beta_{1}} \widehat{\mathbb{E}}[X] \\
\hat{\beta_{1}}=\frac{\sum_{i}^{}(x_i-\bar{x})(y_i-\bar{y})}{\sum_{i}^{}(x_i-\bar{x})^2} = \frac{\widehat{Cov}[X,Y]}{\widehat{Var}[X]}
$$
and predictions
$$
\hat{y}_i=\hat{\beta_{0}}+\hat{\beta}x_i\\
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
# Coefficient Estimates
coef(reg)
```

```
## (Intercept)           x 
##  6.41594246  0.02093466
```

To qualitatively analyze the ''Goodness of fit'' of our model, we plot our predictions.

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
<div class="plotly html-widget html-fill-item" id="htmlwidget-e5eef9f1a2ab21fb87a1" style="width:672px;height:480px;"></div>
<script type="application/json" data-for="htmlwidget-e5eef9f1a2ab21fb87a1">{"x":{"visdat":{"2a0a5cae89dc":["function () ","plotlyVisDat"]},"cur_data":"2a0a5cae89dc","attrs":{"2a0a5cae89dc":{"x":{},"y":{},"mode":"markers","hoverinfo":"text","marker":{"color":"#00000040","size":10},"text":{},"alpha_stroke":1,"sizes":[10,100],"spans":[1,20],"type":"scatter"},"2a0a5cae89dc.1":{"x":{},"y":{},"hoverinfo":"none","mode":"lines+markers","type":"scatter","color":["black"],"line":{"width":0.5},"marker":{"symbol":134,"size":5},"inherit":false}},"layout":{"margin":{"b":40,"l":60,"t":25,"r":10},"showlegend":false,"title":"Crime and Urbanization in America 1975","xaxis":{"domain":[0,1],"automargin":true,"title":"Percent of People in an Urban Area"},"yaxis":{"domain":[0,1],"automargin":true,"title":"Homicide Arrests per 100,000 People"},"hovermode":"closest"},"source":"A","config":{"modeBarButtonsToAdd":["hoverclosest","hovercompare"],"showSendToCloud":false},"data":[{"x":[58,48,80,50,91,78,77,72,80,60,83,54,83,65,57,66,52,66,51,67,85,74,66,44,70,53,62,81,56,89,70,86,45,44,75,68,67,72,87,48,45,59,80,80,32,63,73,39,66,60],"y":[13.199999999999999,10,8.0999999999999996,8.8000000000000007,9,7.9000000000000004,3.2999999999999998,5.9000000000000004,15.4,17.399999999999999,5.2999999999999998,2.6000000000000001,10.4,7.2000000000000002,2.2000000000000002,6,9.6999999999999993,15.4,2.1000000000000001,11.300000000000001,4.4000000000000004,12.1,2.7000000000000002,16.100000000000001,9,6,4.2999999999999998,12.199999999999999,2.1000000000000001,7.4000000000000004,11.4,11.1,13,0.80000000000000004,7.2999999999999998,6.5999999999999996,4.9000000000000004,6.2999999999999998,3.3999999999999999,14.4,3.7999999999999998,13.199999999999999,12.699999999999999,3.2000000000000002,2.2000000000000002,8.5,4,5.7000000000000002,2.6000000000000001,6.7999999999999998],"mode":"markers","hoverinfo":["text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text"],"marker":{"color":"#00000040","size":10,"line":{"color":"rgba(31,119,180,1)"}},"text":["<b> Alabama <\/b> <br>Urban  : 58 <br>Murder : 13.2 <br>Predicted Murder : 7.63 <br>Residual : 5.57","<b> Alaska <\/b> <br>Urban  : 48 <br>Murder : 10 <br>Predicted Murder : 7.42 <br>Residual : 2.58","<b> Arizona <\/b> <br>Urban  : 80 <br>Murder : 8.1 <br>Predicted Murder : 8.09 <br>Residual : 0.01","<b> Arkansas <\/b> <br>Urban  : 50 <br>Murder : 8.8 <br>Predicted Murder : 7.46 <br>Residual : 1.34","<b> California <\/b> <br>Urban  : 91 <br>Murder : 9 <br>Predicted Murder : 8.32 <br>Residual : 0.68","<b> Colorado <\/b> <br>Urban  : 78 <br>Murder : 7.9 <br>Predicted Murder : 8.05 <br>Residual : -0.15","<b> Connecticut <\/b> <br>Urban  : 77 <br>Murder : 3.3 <br>Predicted Murder : 8.03 <br>Residual : -4.73","<b> Delaware <\/b> <br>Urban  : 72 <br>Murder : 5.9 <br>Predicted Murder : 7.92 <br>Residual : -2.02","<b> Florida <\/b> <br>Urban  : 80 <br>Murder : 15.4 <br>Predicted Murder : 8.09 <br>Residual : 7.31","<b> Georgia <\/b> <br>Urban  : 60 <br>Murder : 17.4 <br>Predicted Murder : 7.67 <br>Residual : 9.73","<b> Hawaii <\/b> <br>Urban  : 83 <br>Murder : 5.3 <br>Predicted Murder : 8.15 <br>Residual : -2.85","<b> Idaho <\/b> <br>Urban  : 54 <br>Murder : 2.6 <br>Predicted Murder : 7.55 <br>Residual : -4.95","<b> Illinois <\/b> <br>Urban  : 83 <br>Murder : 10.4 <br>Predicted Murder : 8.15 <br>Residual : 2.25","<b> Indiana <\/b> <br>Urban  : 65 <br>Murder : 7.2 <br>Predicted Murder : 7.78 <br>Residual : -0.58","<b> Iowa <\/b> <br>Urban  : 57 <br>Murder : 2.2 <br>Predicted Murder : 7.61 <br>Residual : -5.41","<b> Kansas <\/b> <br>Urban  : 66 <br>Murder : 6 <br>Predicted Murder : 7.8 <br>Residual : -1.8","<b> Kentucky <\/b> <br>Urban  : 52 <br>Murder : 9.7 <br>Predicted Murder : 7.5 <br>Residual : 2.2","<b> Louisiana <\/b> <br>Urban  : 66 <br>Murder : 15.4 <br>Predicted Murder : 7.8 <br>Residual : 7.6","<b> Maine <\/b> <br>Urban  : 51 <br>Murder : 2.1 <br>Predicted Murder : 7.48 <br>Residual : -5.38","<b> Maryland <\/b> <br>Urban  : 67 <br>Murder : 11.3 <br>Predicted Murder : 7.82 <br>Residual : 3.48","<b> Massachusetts <\/b> <br>Urban  : 85 <br>Murder : 4.4 <br>Predicted Murder : 8.2 <br>Residual : -3.8","<b> Michigan <\/b> <br>Urban  : 74 <br>Murder : 12.1 <br>Predicted Murder : 7.97 <br>Residual : 4.13","<b> Minnesota <\/b> <br>Urban  : 66 <br>Murder : 2.7 <br>Predicted Murder : 7.8 <br>Residual : -5.1","<b> Mississippi <\/b> <br>Urban  : 44 <br>Murder : 16.1 <br>Predicted Murder : 7.34 <br>Residual : 8.76","<b> Missouri <\/b> <br>Urban  : 70 <br>Murder : 9 <br>Predicted Murder : 7.88 <br>Residual : 1.12","<b> Montana <\/b> <br>Urban  : 53 <br>Murder : 6 <br>Predicted Murder : 7.53 <br>Residual : -1.53","<b> Nebraska <\/b> <br>Urban  : 62 <br>Murder : 4.3 <br>Predicted Murder : 7.71 <br>Residual : -3.41","<b> Nevada <\/b> <br>Urban  : 81 <br>Murder : 12.2 <br>Predicted Murder : 8.11 <br>Residual : 4.09","<b> New Hampshire <\/b> <br>Urban  : 56 <br>Murder : 2.1 <br>Predicted Murder : 7.59 <br>Residual : -5.49","<b> New Jersey <\/b> <br>Urban  : 89 <br>Murder : 7.4 <br>Predicted Murder : 8.28 <br>Residual : -0.88","<b> New Mexico <\/b> <br>Urban  : 70 <br>Murder : 11.4 <br>Predicted Murder : 7.88 <br>Residual : 3.52","<b> New York <\/b> <br>Urban  : 86 <br>Murder : 11.1 <br>Predicted Murder : 8.22 <br>Residual : 2.88","<b> North Carolina <\/b> <br>Urban  : 45 <br>Murder : 13 <br>Predicted Murder : 7.36 <br>Residual : 5.64","<b> North Dakota <\/b> <br>Urban  : 44 <br>Murder : 0.8 <br>Predicted Murder : 7.34 <br>Residual : -6.54","<b> Ohio <\/b> <br>Urban  : 75 <br>Murder : 7.3 <br>Predicted Murder : 7.99 <br>Residual : -0.69","<b> Oklahoma <\/b> <br>Urban  : 68 <br>Murder : 6.6 <br>Predicted Murder : 7.84 <br>Residual : -1.24","<b> Oregon <\/b> <br>Urban  : 67 <br>Murder : 4.9 <br>Predicted Murder : 7.82 <br>Residual : -2.92","<b> Pennsylvania <\/b> <br>Urban  : 72 <br>Murder : 6.3 <br>Predicted Murder : 7.92 <br>Residual : -1.62","<b> Rhode Island <\/b> <br>Urban  : 87 <br>Murder : 3.4 <br>Predicted Murder : 8.24 <br>Residual : -4.84","<b> South Carolina <\/b> <br>Urban  : 48 <br>Murder : 14.4 <br>Predicted Murder : 7.42 <br>Residual : 6.98","<b> South Dakota <\/b> <br>Urban  : 45 <br>Murder : 3.8 <br>Predicted Murder : 7.36 <br>Residual : -3.56","<b> Tennessee <\/b> <br>Urban  : 59 <br>Murder : 13.2 <br>Predicted Murder : 7.65 <br>Residual : 5.55","<b> Texas <\/b> <br>Urban  : 80 <br>Murder : 12.7 <br>Predicted Murder : 8.09 <br>Residual : 4.61","<b> Utah <\/b> <br>Urban  : 80 <br>Murder : 3.2 <br>Predicted Murder : 8.09 <br>Residual : -4.89","<b> Vermont <\/b> <br>Urban  : 32 <br>Murder : 2.2 <br>Predicted Murder : 7.09 <br>Residual : -4.89","<b> Virginia <\/b> <br>Urban  : 63 <br>Murder : 8.5 <br>Predicted Murder : 7.73 <br>Residual : 0.77","<b> Washington <\/b> <br>Urban  : 73 <br>Murder : 4 <br>Predicted Murder : 7.94 <br>Residual : -3.94","<b> West Virginia <\/b> <br>Urban  : 39 <br>Murder : 5.7 <br>Predicted Murder : 7.23 <br>Residual : -1.53","<b> Wisconsin <\/b> <br>Urban  : 66 <br>Murder : 2.6 <br>Predicted Murder : 7.8 <br>Residual : -5.2","<b> Wyoming <\/b> <br>Urban  : 60 <br>Murder : 6.8 <br>Predicted Murder : 7.67 <br>Residual : -0.87"],"type":"scatter","error_y":{"color":"rgba(31,119,180,1)"},"error_x":{"color":"rgba(31,119,180,1)"},"line":{"color":"rgba(31,119,180,1)"},"xaxis":"x","yaxis":"y","frame":null},{"x":[58,48,80,50,91,78,77,72,80,60,83,54,83,65,57,66,52,66,51,67,85,74,66,44,70,53,62,81,56,89,70,86,45,44,75,68,67,72,87,48,45,59,80,80,32,63,73,39,66,60],"y":[7.630152672499273,7.4208060843020238,8.0907151665332222,7.4626754019414738,8.3209964135501959,8.0488458488937713,8.0279111900740467,7.9232378959754222,8.0907151665332222,7.672021990138723,8.1535191429923959,7.546414037220373,8.1535191429923959,7.7766952842373476,7.6092180136795484,7.7976299430570721,7.5045447195809238,7.7976299430570721,7.4836100607611984,7.8185646018767976,8.1953884606318468,7.9651072136148722,7.7976299430570721,7.3370674490231238,7.8813685783359722,7.5254793784006484,7.713891307778173,8.1116498253529468,7.588283354859823,8.279127095910745,7.8813685783359722,8.2163231194515713,7.3580021078428492,7.3370674490231238,7.9860418724345967,7.8394992606965221,7.8185646018767976,7.9232378959754222,8.2372577782712959,7.4208060843020238,7.3580021078428492,7.6510873313189975,8.0907151665332222,8.0907151665332222,7.0858515431864246,7.7348259665978976,7.9441725547951467,7.2323941549244992,7.7976299430570721,7.672021990138723],"hoverinfo":["none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none"],"mode":"lines+markers","type":"scatter","line":{"color":"rgba(0,0,0,1)","width":0.5},"marker":{"color":"rgba(0,0,0,1)","symbol":134,"size":5,"line":{"color":"rgba(0,0,0,1)"}},"textfont":{"color":"rgba(0,0,0,1)"},"error_y":{"color":"rgba(0,0,0,1)"},"error_x":{"color":"rgba(0,0,0,1)"},"xaxis":"x","yaxis":"y","frame":null}],"highlight":{"on":"plotly_click","persistent":false,"dynamic":false,"selectize":false,"opacityDim":0.20000000000000001,"selected":{"opacity":1},"debounce":0},"shinyEvents":["plotly_hover","plotly_click","plotly_selected","plotly_relayout","plotly_brushed","plotly_brushing","plotly_clickannotation","plotly_doubleclick","plotly_deselect","plotly_afterplot","plotly_sunburstclick"],"base_url":"https://plot.ly"},"evals":[],"jsHooks":[]}</script>
```
To quantitatively analyze Goodness of Fit, we can intuitively compute the linear correlation between the predictions and the data 
$$
R = Cor( \hat{y}_i, y)
$$
With linear models, we typically compute $R^2$, known as the "coefficient of determination", using the sums of squared errors (Total, Explained, and Residual)
$$
\underbrace{\sum_{i}(y_i-\bar{y})^2}_\text{TSS}=\underbrace{\sum_{i}(\hat{y}_i-\bar{y})^2}_\text{ESS}+\underbrace{\sum_{i}\hat{\epsilon_{i}}^2}_\text{RSS}\\
R^2 = \frac{ESS}{TSS}=1-\frac{RSS}{TSS}
$$

``` r
# Manually Compute R2
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

``` r
# Double Check R2
R <- cor(xy$y, predict(reg))
R^2
```

```
## [1] 0.00484035
```


## Variability Estimates

A regression coefficient is a statistic. And, just like all statistics, we can calculate 

* *standard deviation*: variability within a single sample.
* *standard error*: variability across different samples.
* *confidence interval:* range your statistic varies across different samples.


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

<img src="03-LinearRegression_files/figure-html/unnamed-chunk-9-1.png" width="672" />

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

<img src="03-LinearRegression_files/figure-html/unnamed-chunk-10-1.png" width="672" />


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

<img src="03-LinearRegression_files/figure-html/unnamed-chunk-11-1.png" width="672" />

We can also bootstrap other statistics, such as a t-statistic or $R^2$. We do such things to test a null hypothesis, which is often ``no relationship''. We are rarely interested in computing standard errors and conducting hypothesis tests for two variables. However, we work through the ideas in the two-variable case to better understand the multi-variable case.

## Hypothesis Tests

**Invert a CI**.
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

<img src="03-LinearRegression_files/figure-html/unnamed-chunk-12-1.png" width="672" />

**Impose the Null**.
We can also compute a null distribution. We focus on the simplest: bootstrap simulations that each impose the null hypothesis and re-estimate the statistic of interest. Specifically, we compute the distribution of t-values on data with randomly reshuffled outcomes (imposing the null), and compare how extreme the observed value is.

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

<img src="03-LinearRegression_files/figure-html/unnamed-chunk-13-1.png" width="672" />

Alternatively, you can impose the null by recentering the sampling distribution around the theoretical value; $$\hat{t} = \frac{\hat{\beta} - \beta_{0} }{\hat{\sigma}_{\hat{\beta}}}.$$ Under some assumptions, the null distribution follows a t-distribution. (For more on parametric t-testing based on statistical theory, see https://www.econometrics-with-r.org/4-lrwor.html.)


In any case, we can calculate a *p-value*: the probability you would see something as extreme as your statistic under the null (assuming your null hypothesis was true). We can always calculate a p-value from an explicit null distribution.

``` r
# One Sided Test for P(t > boot_t | Null) = 1 - P(t < boot_t | Null)
That_NullDist1 <- ecdf(boot_t0)
Phat1  <- 1-That_NullDist1(jack_t)

# Two Sided Test for P(t > jack_t or t < -jack_t | Null)
That_NullDist2 <- ecdf(abs(boot_t0))
plot(That_NullDist2, xlim=range(boot_t0, jack_t),
    xlab=expression( abs(hat(t)[b]) ),
    main='Null Bootstrap Distribution', font.main=1)
abline(v=tvalue, col='red')
```

<img src="03-LinearRegression_files/figure-html/unnamed-chunk-14-1.png" width="672" />

``` r
Phat2  <-  1-That_NullDist2( abs(tvalue))
Phat2
```

```
## [1] 0.5789474
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

<img src="03-LinearRegression_files/figure-html/unnamed-chunk-15-1.png" width="672" />


For a nice overview of different types of intervals, see https://www.jstor.org/stable/2685212. For an in-depth view, see "Statistical Intervals: A Guide for Practitioners and Researchers" or "Statistical Tolerance Regions: Theory, Applications, and Computation". See https://robjhyndman.com/hyndsight/intervals/ for constructing intervals for future observations in a time-series context. See Davison and Hinkley, chapters 5 and 6 (also Efron and Tibshirani, or Wehrens et al.)


## Locally Linear

It is generally safe to assume that you could be analyzing data with nonlinear relationships. Here, our model can be represented as
\begin{eqnarray}
y_{i} = m(x_{i}) + e_{i},
\end{eqnarray}
with $m$ being some unknown but smooth function. In such cases, linear regressions can still be useful.

The simplest case is **segmented/piecewise regression**

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

<img src="03-LinearRegression_files/figure-html/unnamed-chunk-17-1.png" width="672" />

A less simple case is a **local linear regression** which conducts a linear regression for each data point using a subsample of data around it. 

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

plot(y~x, pch=16, data=xy, col=grey(0,.5),
    ylab='Murder Rate', xlab='Population Density')
cols <- c(rgb(.8,0,0,.5), rgb(0,0,.8,.5))
lines(X0, pred_lo1, col=cols[1], lwd=1, type='o')
lines(X0, pred_lo2, col=cols[2], lwd=1, type='o')
legend('topleft', title='Locally Linear',
    legend=c('h=2 ', 'h=20'),
    lty=1, col=cols, cex=.8)
```

<img src="03-LinearRegression_files/figure-html/unnamed-chunk-18-1.png" width="672" />
Note that there are more complex versions of local linear regressions (see https://shinyserv.es/shiny/kreg/ for a nice illustration.) An even more complex (and more powerful) version is **loess**, which uses adaptive bandwidths in order to have a similar number of data points in each subsample (especially useful when $X$ is not uniform.)


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

<img src="03-LinearRegression_files/figure-html/unnamed-chunk-19-1.png" width="672" />

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

<img src="03-LinearRegression_files/figure-html/unnamed-chunk-20-1.png" width="672" />

You can also construct prediction bands, which estimate the variability of new data rather than a statistic (a range for $y_{i}(x)$ rather than for $m(x)$).


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

<img src="03-LinearRegression_files/figure-html/unnamed-chunk-21-1.png" width="672" />


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
    ellipses=F, rug=F, smoother=F, pch=16, col='red' # Lower Triangle
    )
```

<img src="03-LinearRegression_files/figure-html/unnamed-chunk-22-1.png" width="672" />


## Multiple Linear Regression
With $K$ variables, the linear model is
$$
y_i=\beta_0+\beta_1 x_{i1}+\beta_2 x_{i2}+\ldots+\beta_K x_{iK}+\epsilon_i = [1~~  x_{i1} ~~...~~ x_{iK}] \beta + \epsilon_i
$$
and our objective is
$$
min_{\beta} \sum_{i=1}^{N} (\epsilon_i)^2.
$$

Denoting 
$$
y= \begin{pmatrix} 
y_{1} \\ \vdots \\ y_{N}
\end{pmatrix} \quad
\textbf{X} = \begin{pmatrix} 
1 & x_{11} & ... & x_{1K} \\
& \vdots & & \\
1 & x_{N1} & ... & x_{NK} 
\end{pmatrix},
$$
we can also write the model and objective in matrix form
$$
y=\textbf{X}\beta+\epsilon\\
min_{\beta} (\epsilon' \epsilon)
$$

Minimizing the squared errors yields coefficient estimates
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

<img src="03-LinearRegression_files/figure-html/unnamed-chunk-24-1.png" width="672" />
and compute sums of squared errors. Adding random data may sometimes improve the fit, however, so we adjust the $R^2$ by the number of covariates $K$.
$$
R^2 = \frac{ESS}{TSS}=1-\frac{RSS}{TSS}\\
R^2_{\text{adj.}} = 1-\frac{N-1}{N-K}(1-R^2)
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

<img src="03-LinearRegression_files/figure-html/unnamed-chunk-25-1.png" width="672" />


## Variability and Hypothesis Tests

To estimate the variability of our estimates, we can use the same *data-driven* methods introduced in the last section. As before, we can conduct independent hypothesis tests using t-values.

We can also conduct *joint* tests that account for interdependancies in our estimates. For example, to test whether two coefficients both equal $0$, we bootstrap the *joint* distribution of coefficients.


``` r
# Bootstrap SE's
boots <- 1:399
boot_regs <- lapply(boots, function(b){
    b_id <- sample( nrow(USArrests), replace=T)
    xy_b <- USArrests[b_id,]
    reg_b <- lm(Murder~Assault+UrbanPop, dat=xy_b)
})
boot_coefs <- sapply(boot_regs, coef)

# Recenter at 0 to impose the null
#boot_means <- rowMeans(boot_coefs)
#boot_coefs0 <- sweep(boot_coefs, MARGIN=1, STATS=boot_means)
```


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
    title='Joint Distribution of Coefficients (under the null)',
    xaxis = list(title='UrbanPop Coefficient'),
    yaxis = list(title='Assualt Coefficient'))
fig
```

```{=html}
<div class="plotly html-widget html-fill-item" id="htmlwidget-afb51333443283ec208c" style="width:672px;height:480px;"></div>
<script type="application/json" data-for="htmlwidget-afb51333443283ec208c">{"x":{"visdat":{"2a0a791a70fe":["function () ","plotlyVisDat"]},"cur_data":"2a0a791a70fe","attrs":{"2a0a791a70fe":{"mode":"markers","x":{},"y":{},"text":{},"hoverinfo":"text","showlegend":false,"marker":{"color":"rgba(0, 0, 0, 0.5)"},"alpha_stroke":1,"sizes":[10,100],"spans":[1,20],"type":"scatter"}},"layout":{"margin":{"b":40,"l":60,"t":25,"r":10},"showlegend":false,"title":"Joint Distribution of Coefficients (under the null)","xaxis":{"domain":[0,1],"automargin":true,"title":"UrbanPop Coefficient"},"yaxis":{"domain":[0,1],"automargin":true,"title":"Assualt Coefficient"},"hovermode":"closest"},"source":"A","config":{"modeBarButtonsToAdd":["hoverclosest","hovercompare"],"showSendToCloud":false},"data":[{"mode":"markers","x":[-0.025623688390704925,-0.077572433020417109,-0.052333444518829722,0.030559454730898137,-0.058499060784952851,-0.030632218451502307,-0.04526969895896274,-0.045980636165424915,-0.03057895481865756,-0.056924872529121116,-0.061291754283345518,-0.039745761947612077,-0.017840567941064721,-0.052657608997400011,-0.058727593356742568,-0.0057573697516746635,-0.0041740574323235156,-0.097667643393145431,-0.045081302396730819,-0.066437738840702476,-0.035536469330141894,-0.030466705079861125,-0.021462272062131051,-0.034144497829837174,-0.03029128176774247,-0.068056696483247345,-0.086527734390575581,-0.013941272876114973,-0.05283159159672194,-0.057326310242469959,-0.0419372020980373,-0.058416046625980669,-0.046713766724932763,-0.012989674998825454,-0.055818048645027374,-0.052930995007462928,-0.012050404144288285,-0.073994795884373271,-0.066425463270531573,-0.04335796962123508,-0.063096766776663996,-0.093821650297471013,-0.070757690445514485,-0.078059661503210087,-0.0888788081409118,-0.05067872069357502,-0.064110196266119135,-0.030806903730226824,-0.042548000515194195,-0.074955274702758978,0.02160760951986258,-0.052162832878458111,-0.075441142428659624,-0.058523110599755006,-0.0069074477678650603,-0.075771191025205797,-0.064754079711073526,-0.02495327356951613,-0.052804714172540783,-0.096522531578114315,-0.10384758573999904,-0.099697743505146139,-0.077155890461806223,-0.046716446152907508,-0.029249908775637923,-0.025119244289803919,-0.036702971735877866,-0.086512589109464078,-0.073999422923059791,-0.043741287252413212,-0.037523529869627939,-0.038950033378781487,-0.067695479109096374,-0.041480669000774788,-0.058429719526146617,-0.039933024085185176,-0.047803608226236673,-0.021015017732314897,-0.026494880488890517,-0.067106878658730038,-0.052729582035108351,-0.030933483840449669,-0.13771145869689502,-0.04305287677700232,-0.030434806131879277,-0.062154924381470016,-0.059885457192581051,-0.021187966959770262,-0.073460634205900113,-0.073529973452699751,-0.036807035437992415,-0.034161454804876125,-0.054572443669015813,-0.041346158296224254,-0.0182466094558917,-0.053381719670512411,-0.058669195024085789,-0.032257549376702457,-0.050628137382292888,-0.036445325853666326,-0.022884013786695207,-0.058532715739941017,-0.046980529326754977,-0.087230511028913188,-0.042275778388011366,-0.045432698341381812,-0.082774661874021022,-0.044097842916094483,-0.062453255215982849,-0.085963388668252663,-0.04739325583452058,-0.040650434701506526,-0.042147267838549232,-0.021577431008324623,-0.058816053497674402,-0.041916500716124239,-0.012169581144949849,-0.02460362902811174,-0.031420767247281975,0.030336310601589502,-0.054261482440872193,-0.049757791729909927,-0.026984305408796632,-0.028319792735303845,-0.028588703535811218,-0.029784032661063397,-0.065556563632194045,-0.040482627400588521,-0.068260302625088934,-0.019465997454799728,-0.047814576720180975,-0.059287860822812725,-0.027944487890615533,-0.045672561692472011,-0.018768663841064705,-0.07746508967019311,-0.10172397786927796,-0.053377868582739178,-0.06669946574277473,-0.035848832235627369,-0.070809403190572953,-8.7011022888281965e-05,-0.039834424676357331,-0.037282825251251817,-0.063158962369302032,-0.030067781180101949,-0.039472981761589435,-0.028452209254698973,-0.057314448124257213,-0.048944553123568206,-0.053364217665352959,-0.051259961622584609,-0.056021163229307024,-0.052183674956133928,-0.068763264725606371,-0.092976268977437243,0.0027116683371991609,-0.019565960643923692,-0.047631698767223667,-0.04602147156111687,-0.080940792196967287,-0.024181602566536526,-0.058137061476663206,-0.041636240410233095,-0.053026867307174194,-0.016547851050100856,-0.053619628350519775,-0.049159652480418869,-0.049288593589749095,-0.066010348040840966,-0.05617427048801469,-0.032685527167167681,-0.028941307048643138,-0.02791746109011238,-0.05089369199702206,-0.080530855450087646,-0.062318787247853981,-0.067048558271251113,-0.027540883686428236,-0.019991300118203801,-0.063175586843951373,-0.070449420608480626,-0.095507130171567062,-0.051539735971161543,-0.059368084387275963,-0.051603400072072453,-0.043387169119546681,-0.028781030950292802,-0.08015823237633192,-0.01327743709730147,-0.015050109425806573,-0.034838302747126466,-0.046004046439835335,-0.041672776171876216,-0.097345333007086171,-0.089145859219915372,-0.025167585834420643,-0.011109996573611485,-0.078313482167853249,-0.0073374299913155968,-0.040092279396145729,-0.016485316289597644,-0.0047223470684784842,-0.058395054517745217,-0.11272516523473389,-0.033828147132436648,-0.050620928071102786,-0.016880617715445689,-0.071252098314661477,-0.028409300191075851,-0.063822399448303258,-0.049988420877086444,-0.05597121597762357,-0.074302470712753352,-0.029502967204197282,-0.04514783175450636,-0.032120752641270921,0.0042715016013637336,-0.076283032786478175,-0.075353400124448966,-0.042527300585703261,-0.019955231581144452,-0.029472690842966463,-0.086894911350821655,-0.025679472869897985,-0.047721178684197514,-0.054245500232177495,-0.039483157861469331,-0.087824631801913522,-0.017202751032925453,-0.070155387559565824,-0.02063270079788692,-0.041078267350647735,-0.089151685651232049,-0.0082431530375926335,-0.098075722903797374,-0.069076791392512132,-0.01892396624128884,-0.04198270580580702,-0.023067182245441398,-0.05352477591605706,-0.02669816093150627,-0.049960483079680144,-0.050091848532099428,-0.024353004424315757,-0.072223826153760828,-0.069792241300934796,-0.05370485423022435,-0.040874005135900303,-0.048248423920749323,-0.016785606857683294,-0.015907932692756734,-0.080308022981698146,-0.055454960605139152,-0.00076221833388504727,0.012769745740343143,-0.032647473509381658,-0.064425599285279911,-0.042162132556715567,-0.016284008971821747,-0.087328444437727012,-0.14122928394718554,-0.090359739794757477,-0.082734286919402669,-0.037569405003675407,0.015796339270126625,-0.030298293948804716,-0.067764801965242136,-0.031923561243638363,-0.074773994784862019,-0.034096306551695953,-0.075091576745536112,-0.0057342008010022195,0.0030871549286071694,-0.05323448258141493,-0.0082336598350341728,-0.029812558610244167,-0.034990138510378216,-0.046629964561955381,-0.036814025161774989,-0.065215739960222244,-0.034052427577227228,0.0095641332709656725,-0.039584548837511967,-0.022894652521957791,-0.078325053536759059,-0.017209278766662776,-0.016746613977854149,-0.054978359881446316,-0.072464665248158019,-0.064013040731418946,-0.060089578270959371,-0.064521185235221892,-0.045282426834771662,-0.027060282517573184,-0.059108744553002537,-0.055179317457853067,-0.077737537218324188,-0.026811276126155838,-0.061422952341120267,-0.067360676014877233,-0.042876105988785052,-0.074955099980109061,-0.098726869999400529,-0.063747231909370969,-0.070974252923984044,-0.0071645563591526224,-0.054172546634217209,-0.00099668708763200366,-0.030100644470950694,-0.013631246413226827,-0.091331481943235163,-0.078132399049136533,-0.10326599869384359,-0.037235825702126746,-0.019387228079111866,-0.081662709522152044,-0.02701428961534277,-0.060360678538254754,-0.084169778529307376,-0.057814748729069408,-0.019171359847670405,-0.033626855411144047,-0.043346018450034655,-0.083054140467962043,-0.073028186674044607,-0.036917459519627507,-0.054212363749217146,-0.093841375851622,-0.094315034620207516,-0.06141740293044521,-0.049519505958686573,-0.06734804719673583,-0.016678687833100427,-0.048488764595544048,-0.019645063863930806,-0.028054930078627749,-0.031669267286645771,-0.052611590268467526,-0.054597156758515786,-0.05337042521466874,-0.063760366007102831,-0.049892879059057683,-0.044653173220038984,-0.038362986785836217,-0.05988477239754128,-0.051343575831067446,-0.05722200140683998,-0.055570759903326314,-0.020788696702211864,-0.025256884350827267,-0.0048845070559291187,-0.026796747565268886,-0.039736222930351985,-0.047181023650296881,-0.049949350525547574,-0.068023059466171598,-0.056848227197800721,-0.048648505887809376,-0.044135798638927408,-0.022993705876047307,-0.0050609864395980463,-0.051592448305677517,-0.065157802647144644,-0.10643693244671674,-0.074161474130918156,-0.044626052059709945,-0.018642736905732614,-0.05640209616085836,-0.059326818550711855,-0.080733561894980155,0.045989032165901958,-0.049386240172527074,-0.067163759946906432,-0.046694143897566584,-0.067702064333857295,-0.04121866221477128,-0.081253425372966107,-0.071769276630926554,-0.055423577912160536,-0.033973019663859093,-0.018535544807175949,-0.063743617084425885,-0.075211558524331729,-0.034548753067483513,-0.051642175911715972,-0.068949931801951803,-0.033373755188583008,-0.06165814646723683,-0.091421485397442936,-0.12141395834296234,-0.051703022672645933,-0.011888670979398447,-0.098609300267536518,-0.035500269327046564,-0.038455625568156418,-0.061756021480005259,-0.035484052180829458,-0.07984777802258694],"y":[0.045180506939046849,0.053434976417066044,0.045287497138363643,0.035936976880023022,0.03776768558501141,0.042444032058229345,0.047067221453599511,0.040732351374890993,0.048896391485987283,0.036322046221550927,0.044574175333761304,0.036258237310480154,0.041859814093208172,0.043538493037946976,0.047851566498657058,0.038317358398140391,0.043048074763239734,0.045073060075336867,0.044949054368610776,0.04440075763268593,0.044085517108610868,0.037414159604202211,0.038722598952109631,0.044440588194761987,0.039993476977545392,0.043076073591620009,0.047185522537575991,0.047325374204432738,0.040677379418922639,0.042101522714142338,0.045909780386597841,0.049850939048594271,0.043703544035846247,0.042446086000954272,0.050204723734946957,0.033751894727736369,0.046081094027615642,0.042470602147464516,0.046821090602376707,0.049137128269303339,0.044442369653673111,0.054176652045461147,0.048552967209848488,0.050474402162733981,0.051434977572757508,0.047186544096807656,0.04226532558639632,0.039472969762854485,0.04130386418880972,0.041575564243239868,0.035178077304379926,0.045720881466788682,0.045347486414683225,0.044990675960146692,0.040057618671419132,0.044118567484805735,0.04785160451235812,0.037625478628315251,0.044509716646327906,0.049139503167542245,0.045816934284067912,0.047629909780590243,0.044567120551574649,0.038045160239539154,0.039446830577998339,0.03433439356026053,0.038217619380678143,0.052072806370588275,0.04219892539321126,0.039025285991391517,0.041486878501672056,0.044031787277395033,0.042878801311915696,0.050011138313799657,0.049331157616127233,0.046118410272021668,0.050526194637361285,0.03709700542158495,0.043942507031614279,0.039403039382341881,0.05097191850969373,0.037534638046480398,0.053850417538662945,0.04385164840581228,0.044149615590054231,0.045311846799302564,0.044113874119847622,0.04450106976133214,0.042554408722056167,0.037671377981603464,0.043227009063352473,0.048322969658472568,0.048848414337364407,0.043779580854862665,0.047492229860423466,0.043126650313736289,0.04853708041187553,0.049287116018234364,0.047288849480810365,0.044227210516169138,0.045682339416734712,0.045682382508086643,0.046381955808143492,0.043881968524010294,0.045505233762163401,0.038033408177390052,0.049746469255657906,0.044533138997767854,0.042559772010982141,0.048973168742944773,0.045524082918302733,0.043979645772149141,0.043844626413369524,0.039402592927108779,0.04367306952616308,0.04049849941099929,0.042358294981464845,0.045913270226144234,0.039143191903072361,0.051012345792453194,0.047628521461649309,0.044889861563429334,0.041244720383256765,0.045569887030921172,0.042311002812045945,0.042013591218673846,0.040700357804763498,0.048244957413843013,0.048641016335297278,0.050227285408064058,0.046369304437745527,0.047593517297088481,0.039921994935367341,0.046048246279157184,0.039277244638888244,0.048587764239276909,0.042575760077165549,0.037191658820179316,0.043731700911910219,0.045757567555985493,0.042147182248733532,0.036952377757606701,0.049744221078287833,0.043969786462089246,0.048131138667777483,0.040151702306174319,0.038595623027131744,0.039878755303102024,0.040936038525211604,0.043786453142628301,0.041011853947294813,0.03608819616587413,0.045232449519164206,0.050802004296261881,0.056761566152275796,0.04732535585182112,0.039037012365355325,0.041765486823970792,0.043433003577290567,0.047505100958638129,0.050210431942008298,0.039050918624590994,0.049055769488044097,0.049115761062713759,0.045517633374325586,0.041139714177441493,0.040949787314079583,0.045174942125129978,0.047493847089468653,0.036625440266080958,0.042537711959764371,0.041893053781870443,0.044451447949815981,0.043188345863556118,0.039904524574350612,0.044237601168187576,0.049064491085234072,0.047345302028569659,0.046612872612146028,0.039539772428493956,0.05059518335375035,0.044367026553554581,0.045644451040203975,0.044310415999689233,0.043402318337930353,0.04539255717774715,0.034119853731309366,0.040424392104035256,0.051990081270602485,0.042240086847841182,0.046117022748490888,0.042938522158602686,0.043802097168870444,0.046551805205569979,0.049480170460217285,0.045879654089719037,0.036885941012174593,0.042653359571177184,0.048160348838066303,0.042779546247257015,0.038830913282352324,0.038026217453277812,0.040629917099110409,0.04455626185741815,0.050771789687965883,0.04561538076055429,0.043056643860784713,0.039552392093077947,0.053910965025317739,0.042083534782785231,0.037279608180839349,0.048752005978871527,0.045115399263087677,0.054008376472745943,0.047422802573866336,0.043963340230675309,0.042402483764417777,0.041428767643320819,0.048900543248320251,0.050434657621444869,0.044961963865979566,0.043003113524128271,0.042783638634604625,0.040142139688565968,0.04045579553213477,0.044803589240432339,0.049151856659456566,0.045327475184725526,0.053816153354120919,0.042762401287459652,0.047459769530451938,0.041004571356779609,0.044803457283221042,0.05461911613647491,0.035439202232672995,0.048131311968412235,0.046572164753184264,0.04418941096891589,0.042778278589849963,0.038577512168268727,0.042324805184535554,0.03612582980057373,0.040076491552227526,0.043108535704196503,0.040746959914630738,0.042463808454628951,0.044495811890916413,0.040170176845693489,0.04262585776841693,0.049630657997330213,0.035859378434947534,0.048600421613956633,0.047480879179036845,0.037060523077405108,0.043208569474483038,0.038786990225592427,0.045819295636388813,0.044034783046104323,0.046277354888041619,0.041515287822715866,0.044030353790984036,0.056364445287406396,0.044153470727926927,0.045980304283392455,0.041635399893345325,0.043207954198458014,0.039811927809500651,0.050278166180799506,0.044793821343700538,0.045449835364263273,0.042382797996850928,0.045994532553405125,0.038015726913443251,0.044819301445436652,0.044171661380057008,0.046343154817051549,0.035520570237179049,0.044396730917094951,0.046444889302664945,0.040173222132244911,0.043570402677499676,0.040968304724612235,0.040039889356759596,0.045747318468975909,0.041462958648131668,0.044377063643075587,0.04559514875292689,0.04465006607121666,0.040511527136082463,0.044472111463133748,0.047026534299615036,0.041697562714563013,0.035818514662919548,0.044500417256587148,0.042932861952922792,0.049311310349510681,0.046822329928415576,0.045818209265371494,0.041706544720959304,0.049899592225621028,0.041791613473604043,0.042417327957342807,0.043269106723153858,0.042126618145827778,0.046343571570510812,0.046881886387686346,0.041542101638003613,0.036871968072463852,0.038705505123689483,0.046767684310699893,0.043684390384586498,0.046755865758032845,0.047032861753618919,0.047212094688621371,0.041842997270503855,0.039296325977223066,0.048079500616799845,0.044225246503464509,0.039765589677771343,0.055733594841191662,0.043763960625919578,0.045051938673143582,0.03655739787666016,0.050599471012930088,0.04695385606124259,0.044026069622333769,0.041071810081958482,0.049666457130378532,0.043070872577717058,0.050408379887596194,0.044123133185515966,0.04310531233707459,0.039088391117829066,0.044553105325078238,0.044636066000310684,0.041868431992484238,0.038833578369400851,0.038783915436320968,0.038212146507049669,0.038752140964076476,0.04713472996218606,0.042862051304670024,0.046736358557135274,0.045699973258207099,0.04508869795054566,0.050597833077936125,0.044069485367968959,0.043080267390299333,0.049054139385422961,0.039293594446812588,0.045929515480326297,0.046027982760206101,0.049045968752396696,0.045041877014725347,0.04036889559127043,0.048281231912278316,0.039837771776880186,0.045604428770202238,0.043050442883726996,0.040204688624940144,0.040969434270296486,0.041509231012989506,0.046604931202072541,0.039981589144210884,0.057958792651824291,0.060046718756092889,0.044135997267320357,0.048269170329627097,0.051864566462137336,0.046818244077298503,0.04538401770846312,0.038027548350080348,0.042508747586929435,0.047480661077294359,0.042890516754801107,0.049433235140649276,0.038441412529419627,0.044905516486026933,0.041844297350612271,0.049791694780729111,0.044315760463424787,0.042505545353196686,0.048808473951743904,0.046278270460312,0.046225223067811551,0.054259807641469614,0.044476028451754843,0.046013677788711335,0.048847082232792015,0.050454712493037832,0.047946820067637778,0.048678054691738887,0.038814551958582993,0.048162164174675531,0.042929761727757053,0.039180762417351446,0.042805500596397761,0.04358098983998019,0.050501949684452561],"text":["<b> bootstrap dataset:  1 <\/b> <br>Coef. Urban  : -0.026 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 1.926","<b> bootstrap dataset:  2 <\/b> <br>Coef. Urban  : -0.078 <br>Coef. Murder : 0.053 <br>Coef. Intercept : 4.214","<b> bootstrap dataset:  3 <\/b> <br>Coef. Urban  : -0.052 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 3.66","<b> bootstrap dataset:  4 <\/b> <br>Coef. Urban  : 0.031 <br>Coef. Murder : 0.036 <br>Coef. Intercept : -1.276","<b> bootstrap dataset:  5 <\/b> <br>Coef. Urban  : -0.058 <br>Coef. Murder : 0.038 <br>Coef. Intercept : 4.787","<b> bootstrap dataset:  6 <\/b> <br>Coef. Urban  : -0.031 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 2.442","<b> bootstrap dataset:  7 <\/b> <br>Coef. Urban  : -0.045 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 2.662","<b> bootstrap dataset:  8 <\/b> <br>Coef. Urban  : -0.046 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 3.624","<b> bootstrap dataset:  9 <\/b> <br>Coef. Urban  : -0.031 <br>Coef. Murder : 0.049 <br>Coef. Intercept : 2.022","<b> bootstrap dataset:  10 <\/b> <br>Coef. Urban  : -0.057 <br>Coef. Murder : 0.036 <br>Coef. Intercept : 5.123","<b> bootstrap dataset:  11 <\/b> <br>Coef. Urban  : -0.061 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 3.985","<b> bootstrap dataset:  12 <\/b> <br>Coef. Urban  : -0.04 <br>Coef. Murder : 0.036 <br>Coef. Intercept : 4.178","<b> bootstrap dataset:  13 <\/b> <br>Coef. Urban  : -0.018 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 1.892","<b> bootstrap dataset:  14 <\/b> <br>Coef. Urban  : -0.053 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 3.619","<b> bootstrap dataset:  15 <\/b> <br>Coef. Urban  : -0.059 <br>Coef. Murder : 0.048 <br>Coef. Intercept : 3.591","<b> bootstrap dataset:  16 <\/b> <br>Coef. Urban  : -0.006 <br>Coef. Murder : 0.038 <br>Coef. Intercept : 1.258","<b> bootstrap dataset:  17 <\/b> <br>Coef. Urban  : -0.004 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 0.878","<b> bootstrap dataset:  18 <\/b> <br>Coef. Urban  : -0.098 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 6.585","<b> bootstrap dataset:  19 <\/b> <br>Coef. Urban  : -0.045 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 2.587","<b> bootstrap dataset:  20 <\/b> <br>Coef. Urban  : -0.066 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 4.403","<b> bootstrap dataset:  21 <\/b> <br>Coef. Urban  : -0.036 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 2.71","<b> bootstrap dataset:  22 <\/b> <br>Coef. Urban  : -0.03 <br>Coef. Murder : 0.037 <br>Coef. Intercept : 3.341","<b> bootstrap dataset:  23 <\/b> <br>Coef. Urban  : -0.021 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 2.488","<b> bootstrap dataset:  24 <\/b> <br>Coef. Urban  : -0.034 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 2.491","<b> bootstrap dataset:  25 <\/b> <br>Coef. Urban  : -0.03 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 2.421","<b> bootstrap dataset:  26 <\/b> <br>Coef. Urban  : -0.068 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 4.452","<b> bootstrap dataset:  27 <\/b> <br>Coef. Urban  : -0.087 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 5.118","<b> bootstrap dataset:  28 <\/b> <br>Coef. Urban  : -0.014 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 0.859","<b> bootstrap dataset:  29 <\/b> <br>Coef. Urban  : -0.053 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 3.943","<b> bootstrap dataset:  30 <\/b> <br>Coef. Urban  : -0.057 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 4.313","<b> bootstrap dataset:  31 <\/b> <br>Coef. Urban  : -0.042 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 2.114","<b> bootstrap dataset:  32 <\/b> <br>Coef. Urban  : -0.058 <br>Coef. Murder : 0.05 <br>Coef. Intercept : 3.529","<b> bootstrap dataset:  33 <\/b> <br>Coef. Urban  : -0.047 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 3.491","<b> bootstrap dataset:  34 <\/b> <br>Coef. Urban  : -0.013 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 1.601","<b> bootstrap dataset:  35 <\/b> <br>Coef. Urban  : -0.056 <br>Coef. Murder : 0.05 <br>Coef. Intercept : 2.569","<b> bootstrap dataset:  36 <\/b> <br>Coef. Urban  : -0.053 <br>Coef. Murder : 0.034 <br>Coef. Intercept : 5.678","<b> bootstrap dataset:  37 <\/b> <br>Coef. Urban  : -0.012 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 1.164","<b> bootstrap dataset:  38 <\/b> <br>Coef. Urban  : -0.074 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 5.861","<b> bootstrap dataset:  39 <\/b> <br>Coef. Urban  : -0.066 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 3.938","<b> bootstrap dataset:  40 <\/b> <br>Coef. Urban  : -0.043 <br>Coef. Murder : 0.049 <br>Coef. Intercept : 3.036","<b> bootstrap dataset:  41 <\/b> <br>Coef. Urban  : -0.063 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 4.202","<b> bootstrap dataset:  42 <\/b> <br>Coef. Urban  : -0.094 <br>Coef. Murder : 0.054 <br>Coef. Intercept : 4.491","<b> bootstrap dataset:  43 <\/b> <br>Coef. Urban  : -0.071 <br>Coef. Murder : 0.049 <br>Coef. Intercept : 4.298","<b> bootstrap dataset:  44 <\/b> <br>Coef. Urban  : -0.078 <br>Coef. Murder : 0.05 <br>Coef. Intercept : 5.043","<b> bootstrap dataset:  45 <\/b> <br>Coef. Urban  : -0.089 <br>Coef. Murder : 0.051 <br>Coef. Intercept : 4.752","<b> bootstrap dataset:  46 <\/b> <br>Coef. Urban  : -0.051 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 3.597","<b> bootstrap dataset:  47 <\/b> <br>Coef. Urban  : -0.064 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 4.539","<b> bootstrap dataset:  48 <\/b> <br>Coef. Urban  : -0.031 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 2.886","<b> bootstrap dataset:  49 <\/b> <br>Coef. Urban  : -0.043 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 2.964","<b> bootstrap dataset:  50 <\/b> <br>Coef. Urban  : -0.075 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 5.381","<b> bootstrap dataset:  51 <\/b> <br>Coef. Urban  : 0.022 <br>Coef. Murder : 0.035 <br>Coef. Intercept : 0.028","<b> bootstrap dataset:  52 <\/b> <br>Coef. Urban  : -0.052 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 3.724","<b> bootstrap dataset:  53 <\/b> <br>Coef. Urban  : -0.075 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 5.408","<b> bootstrap dataset:  54 <\/b> <br>Coef. Urban  : -0.059 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 4.132","<b> bootstrap dataset:  55 <\/b> <br>Coef. Urban  : -0.007 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 1.173","<b> bootstrap dataset:  56 <\/b> <br>Coef. Urban  : -0.076 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 4.435","<b> bootstrap dataset:  57 <\/b> <br>Coef. Urban  : -0.065 <br>Coef. Murder : 0.048 <br>Coef. Intercept : 3.404","<b> bootstrap dataset:  58 <\/b> <br>Coef. Urban  : -0.025 <br>Coef. Murder : 0.038 <br>Coef. Intercept : 2.638","<b> bootstrap dataset:  59 <\/b> <br>Coef. Urban  : -0.053 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 3.63","<b> bootstrap dataset:  60 <\/b> <br>Coef. Urban  : -0.097 <br>Coef. Murder : 0.049 <br>Coef. Intercept : 6.088","<b> bootstrap dataset:  61 <\/b> <br>Coef. Urban  : -0.104 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 6.556","<b> bootstrap dataset:  62 <\/b> <br>Coef. Urban  : -0.1 <br>Coef. Murder : 0.048 <br>Coef. Intercept : 6.678","<b> bootstrap dataset:  63 <\/b> <br>Coef. Urban  : -0.077 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 4.876","<b> bootstrap dataset:  64 <\/b> <br>Coef. Urban  : -0.047 <br>Coef. Murder : 0.038 <br>Coef. Intercept : 4.983","<b> bootstrap dataset:  65 <\/b> <br>Coef. Urban  : -0.029 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 2.986","<b> bootstrap dataset:  66 <\/b> <br>Coef. Urban  : -0.025 <br>Coef. Murder : 0.034 <br>Coef. Intercept : 3.943","<b> bootstrap dataset:  67 <\/b> <br>Coef. Urban  : -0.037 <br>Coef. Murder : 0.038 <br>Coef. Intercept : 4.075","<b> bootstrap dataset:  68 <\/b> <br>Coef. Urban  : -0.087 <br>Coef. Murder : 0.052 <br>Coef. Intercept : 4.774","<b> bootstrap dataset:  69 <\/b> <br>Coef. Urban  : -0.074 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 5.289","<b> bootstrap dataset:  70 <\/b> <br>Coef. Urban  : -0.044 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 3.661","<b> bootstrap dataset:  71 <\/b> <br>Coef. Urban  : -0.038 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 3.12","<b> bootstrap dataset:  72 <\/b> <br>Coef. Urban  : -0.039 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 2.551","<b> bootstrap dataset:  73 <\/b> <br>Coef. Urban  : -0.068 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 4.895","<b> bootstrap dataset:  74 <\/b> <br>Coef. Urban  : -0.041 <br>Coef. Murder : 0.05 <br>Coef. Intercept : 1.568","<b> bootstrap dataset:  75 <\/b> <br>Coef. Urban  : -0.058 <br>Coef. Murder : 0.049 <br>Coef. Intercept : 2.851","<b> bootstrap dataset:  76 <\/b> <br>Coef. Urban  : -0.04 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 2.474","<b> bootstrap dataset:  77 <\/b> <br>Coef. Urban  : -0.048 <br>Coef. Murder : 0.051 <br>Coef. Intercept : 2.504","<b> bootstrap dataset:  78 <\/b> <br>Coef. Urban  : -0.021 <br>Coef. Murder : 0.037 <br>Coef. Intercept : 2.664","<b> bootstrap dataset:  79 <\/b> <br>Coef. Urban  : -0.026 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 2.761","<b> bootstrap dataset:  80 <\/b> <br>Coef. Urban  : -0.067 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 5.331","<b> bootstrap dataset:  81 <\/b> <br>Coef. Urban  : -0.053 <br>Coef. Murder : 0.051 <br>Coef. Intercept : 2.936","<b> bootstrap dataset:  82 <\/b> <br>Coef. Urban  : -0.031 <br>Coef. Murder : 0.038 <br>Coef. Intercept : 3.186","<b> bootstrap dataset:  83 <\/b> <br>Coef. Urban  : -0.138 <br>Coef. Murder : 0.054 <br>Coef. Intercept : 7.492","<b> bootstrap dataset:  84 <\/b> <br>Coef. Urban  : -0.043 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 3.57","<b> bootstrap dataset:  85 <\/b> <br>Coef. Urban  : -0.03 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 2.776","<b> bootstrap dataset:  86 <\/b> <br>Coef. Urban  : -0.062 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 4.304","<b> bootstrap dataset:  87 <\/b> <br>Coef. Urban  : -0.06 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 4.159","<b> bootstrap dataset:  88 <\/b> <br>Coef. Urban  : -0.021 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 1.476","<b> bootstrap dataset:  89 <\/b> <br>Coef. Urban  : -0.073 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 5.743","<b> bootstrap dataset:  90 <\/b> <br>Coef. Urban  : -0.074 <br>Coef. Murder : 0.038 <br>Coef. Intercept : 6.701","<b> bootstrap dataset:  91 <\/b> <br>Coef. Urban  : -0.037 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 2.518","<b> bootstrap dataset:  92 <\/b> <br>Coef. Urban  : -0.034 <br>Coef. Murder : 0.048 <br>Coef. Intercept : 2.502","<b> bootstrap dataset:  93 <\/b> <br>Coef. Urban  : -0.055 <br>Coef. Murder : 0.049 <br>Coef. Intercept : 3.203","<b> bootstrap dataset:  94 <\/b> <br>Coef. Urban  : -0.041 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 2.788","<b> bootstrap dataset:  95 <\/b> <br>Coef. Urban  : -0.018 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 0.74","<b> bootstrap dataset:  96 <\/b> <br>Coef. Urban  : -0.053 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 3.242","<b> bootstrap dataset:  97 <\/b> <br>Coef. Urban  : -0.059 <br>Coef. Murder : 0.049 <br>Coef. Intercept : 3.03","<b> bootstrap dataset:  98 <\/b> <br>Coef. Urban  : -0.032 <br>Coef. Murder : 0.049 <br>Coef. Intercept : 1.517","<b> bootstrap dataset:  99 <\/b> <br>Coef. Urban  : -0.051 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 3.504","<b> bootstrap dataset:  100 <\/b> <br>Coef. Urban  : -0.036 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 2.113","<b> bootstrap dataset:  101 <\/b> <br>Coef. Urban  : -0.023 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 2.091","<b> bootstrap dataset:  102 <\/b> <br>Coef. Urban  : -0.059 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 4.305","<b> bootstrap dataset:  103 <\/b> <br>Coef. Urban  : -0.047 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 3.211","<b> bootstrap dataset:  104 <\/b> <br>Coef. Urban  : -0.087 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 5.729","<b> bootstrap dataset:  105 <\/b> <br>Coef. Urban  : -0.042 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 2.677","<b> bootstrap dataset:  106 <\/b> <br>Coef. Urban  : -0.045 <br>Coef. Murder : 0.038 <br>Coef. Intercept : 3.74","<b> bootstrap dataset:  107 <\/b> <br>Coef. Urban  : -0.083 <br>Coef. Murder : 0.05 <br>Coef. Intercept : 4.771","<b> bootstrap dataset:  108 <\/b> <br>Coef. Urban  : -0.044 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 3.367","<b> bootstrap dataset:  109 <\/b> <br>Coef. Urban  : -0.062 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 4.423","<b> bootstrap dataset:  110 <\/b> <br>Coef. Urban  : -0.086 <br>Coef. Murder : 0.049 <br>Coef. Intercept : 5.088","<b> bootstrap dataset:  111 <\/b> <br>Coef. Urban  : -0.047 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 3.505","<b> bootstrap dataset:  112 <\/b> <br>Coef. Urban  : -0.041 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 3.224","<b> bootstrap dataset:  113 <\/b> <br>Coef. Urban  : -0.042 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 3.742","<b> bootstrap dataset:  114 <\/b> <br>Coef. Urban  : -0.022 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 2.35","<b> bootstrap dataset:  115 <\/b> <br>Coef. Urban  : -0.059 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 3.858","<b> bootstrap dataset:  116 <\/b> <br>Coef. Urban  : -0.042 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 3.47","<b> bootstrap dataset:  117 <\/b> <br>Coef. Urban  : -0.012 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 1.508","<b> bootstrap dataset:  118 <\/b> <br>Coef. Urban  : -0.025 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 1.763","<b> bootstrap dataset:  119 <\/b> <br>Coef. Urban  : -0.031 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 3.327","<b> bootstrap dataset:  120 <\/b> <br>Coef. Urban  : 0.03 <br>Coef. Murder : 0.051 <br>Coef. Intercept : -2.251","<b> bootstrap dataset:  121 <\/b> <br>Coef. Urban  : -0.054 <br>Coef. Murder : 0.048 <br>Coef. Intercept : 3.018","<b> bootstrap dataset:  122 <\/b> <br>Coef. Urban  : -0.05 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 3.238","<b> bootstrap dataset:  123 <\/b> <br>Coef. Urban  : -0.027 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 1.781","<b> bootstrap dataset:  124 <\/b> <br>Coef. Urban  : -0.028 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 1.855","<b> bootstrap dataset:  125 <\/b> <br>Coef. Urban  : -0.029 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 2.296","<b> bootstrap dataset:  126 <\/b> <br>Coef. Urban  : -0.03 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 2.989","<b> bootstrap dataset:  127 <\/b> <br>Coef. Urban  : -0.066 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 5.084","<b> bootstrap dataset:  128 <\/b> <br>Coef. Urban  : -0.04 <br>Coef. Murder : 0.048 <br>Coef. Intercept : 2.797","<b> bootstrap dataset:  129 <\/b> <br>Coef. Urban  : -0.068 <br>Coef. Murder : 0.049 <br>Coef. Intercept : 3.404","<b> bootstrap dataset:  130 <\/b> <br>Coef. Urban  : -0.019 <br>Coef. Murder : 0.05 <br>Coef. Intercept : 0.451","<b> bootstrap dataset:  131 <\/b> <br>Coef. Urban  : -0.048 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 2.86","<b> bootstrap dataset:  132 <\/b> <br>Coef. Urban  : -0.059 <br>Coef. Murder : 0.048 <br>Coef. Intercept : 3.497","<b> bootstrap dataset:  133 <\/b> <br>Coef. Urban  : -0.028 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 2.2","<b> bootstrap dataset:  134 <\/b> <br>Coef. Urban  : -0.046 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 2.918","<b> bootstrap dataset:  135 <\/b> <br>Coef. Urban  : -0.019 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 2.399","<b> bootstrap dataset:  136 <\/b> <br>Coef. Urban  : -0.077 <br>Coef. Murder : 0.049 <br>Coef. Intercept : 4.987","<b> bootstrap dataset:  137 <\/b> <br>Coef. Urban  : -0.102 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 6.219","<b> bootstrap dataset:  138 <\/b> <br>Coef. Urban  : -0.053 <br>Coef. Murder : 0.037 <br>Coef. Intercept : 5.251","<b> bootstrap dataset:  139 <\/b> <br>Coef. Urban  : -0.067 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 4.224","<b> bootstrap dataset:  140 <\/b> <br>Coef. Urban  : -0.036 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 2.241","<b> bootstrap dataset:  141 <\/b> <br>Coef. Urban  : -0.071 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 5.669","<b> bootstrap dataset:  142 <\/b> <br>Coef. Urban  : 0 <br>Coef. Murder : 0.037 <br>Coef. Intercept : 1.029","<b> bootstrap dataset:  143 <\/b> <br>Coef. Urban  : -0.04 <br>Coef. Murder : 0.05 <br>Coef. Intercept : 1.648","<b> bootstrap dataset:  144 <\/b> <br>Coef. Urban  : -0.037 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 3.182","<b> bootstrap dataset:  145 <\/b> <br>Coef. Urban  : -0.063 <br>Coef. Murder : 0.048 <br>Coef. Intercept : 3.848","<b> bootstrap dataset:  146 <\/b> <br>Coef. Urban  : -0.03 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 3","<b> bootstrap dataset:  147 <\/b> <br>Coef. Urban  : -0.039 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 3.714","<b> bootstrap dataset:  148 <\/b> <br>Coef. Urban  : -0.028 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 2.249","<b> bootstrap dataset:  149 <\/b> <br>Coef. Urban  : -0.057 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 4.046","<b> bootstrap dataset:  150 <\/b> <br>Coef. Urban  : -0.049 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 3.373","<b> bootstrap dataset:  151 <\/b> <br>Coef. Urban  : -0.053 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 4.054","<b> bootstrap dataset:  152 <\/b> <br>Coef. Urban  : -0.051 <br>Coef. Murder : 0.036 <br>Coef. Intercept : 4.546","<b> bootstrap dataset:  153 <\/b> <br>Coef. Urban  : -0.056 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 3.662","<b> bootstrap dataset:  154 <\/b> <br>Coef. Urban  : -0.052 <br>Coef. Murder : 0.051 <br>Coef. Intercept : 2.442","<b> bootstrap dataset:  155 <\/b> <br>Coef. Urban  : -0.069 <br>Coef. Murder : 0.057 <br>Coef. Intercept : 3.116","<b> bootstrap dataset:  156 <\/b> <br>Coef. Urban  : -0.093 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 6.291","<b> bootstrap dataset:  157 <\/b> <br>Coef. Urban  : 0.003 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 0.503","<b> bootstrap dataset:  158 <\/b> <br>Coef. Urban  : -0.02 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 1.59","<b> bootstrap dataset:  159 <\/b> <br>Coef. Urban  : -0.048 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 2.909","<b> bootstrap dataset:  160 <\/b> <br>Coef. Urban  : -0.046 <br>Coef. Murder : 0.048 <br>Coef. Intercept : 2.829","<b> bootstrap dataset:  161 <\/b> <br>Coef. Urban  : -0.081 <br>Coef. Murder : 0.05 <br>Coef. Intercept : 4.579","<b> bootstrap dataset:  162 <\/b> <br>Coef. Urban  : -0.024 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 2.806","<b> bootstrap dataset:  163 <\/b> <br>Coef. Urban  : -0.058 <br>Coef. Murder : 0.049 <br>Coef. Intercept : 3.749","<b> bootstrap dataset:  164 <\/b> <br>Coef. Urban  : -0.042 <br>Coef. Murder : 0.049 <br>Coef. Intercept : 2.387","<b> bootstrap dataset:  165 <\/b> <br>Coef. Urban  : -0.053 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 3.485","<b> bootstrap dataset:  166 <\/b> <br>Coef. Urban  : -0.017 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 1.717","<b> bootstrap dataset:  167 <\/b> <br>Coef. Urban  : -0.054 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 3.906","<b> bootstrap dataset:  168 <\/b> <br>Coef. Urban  : -0.049 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 3.12","<b> bootstrap dataset:  169 <\/b> <br>Coef. Urban  : -0.049 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 3.134","<b> bootstrap dataset:  170 <\/b> <br>Coef. Urban  : -0.066 <br>Coef. Murder : 0.037 <br>Coef. Intercept : 5.422","<b> bootstrap dataset:  171 <\/b> <br>Coef. Urban  : -0.056 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 4.293","<b> bootstrap dataset:  172 <\/b> <br>Coef. Urban  : -0.033 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 2.595","<b> bootstrap dataset:  173 <\/b> <br>Coef. Urban  : -0.029 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 2.246","<b> bootstrap dataset:  174 <\/b> <br>Coef. Urban  : -0.028 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 2.196","<b> bootstrap dataset:  175 <\/b> <br>Coef. Urban  : -0.051 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 4.17","<b> bootstrap dataset:  176 <\/b> <br>Coef. Urban  : -0.081 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 5.683","<b> bootstrap dataset:  177 <\/b> <br>Coef. Urban  : -0.062 <br>Coef. Murder : 0.049 <br>Coef. Intercept : 3.552","<b> bootstrap dataset:  178 <\/b> <br>Coef. Urban  : -0.067 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 4.185","<b> bootstrap dataset:  179 <\/b> <br>Coef. Urban  : -0.028 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 0.683","<b> bootstrap dataset:  180 <\/b> <br>Coef. Urban  : -0.02 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 2.347","<b> bootstrap dataset:  181 <\/b> <br>Coef. Urban  : -0.063 <br>Coef. Murder : 0.051 <br>Coef. Intercept : 3.623","<b> bootstrap dataset:  182 <\/b> <br>Coef. Urban  : -0.07 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 5.485","<b> bootstrap dataset:  183 <\/b> <br>Coef. Urban  : -0.096 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 6.375","<b> bootstrap dataset:  184 <\/b> <br>Coef. Urban  : -0.052 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 3.422","<b> bootstrap dataset:  185 <\/b> <br>Coef. Urban  : -0.059 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 4.268","<b> bootstrap dataset:  186 <\/b> <br>Coef. Urban  : -0.052 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 3.121","<b> bootstrap dataset:  187 <\/b> <br>Coef. Urban  : -0.043 <br>Coef. Murder : 0.034 <br>Coef. Intercept : 4.868","<b> bootstrap dataset:  188 <\/b> <br>Coef. Urban  : -0.029 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 2.591","<b> bootstrap dataset:  189 <\/b> <br>Coef. Urban  : -0.08 <br>Coef. Murder : 0.052 <br>Coef. Intercept : 4.071","<b> bootstrap dataset:  190 <\/b> <br>Coef. Urban  : -0.013 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 1.696","<b> bootstrap dataset:  191 <\/b> <br>Coef. Urban  : -0.015 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 1.255","<b> bootstrap dataset:  192 <\/b> <br>Coef. Urban  : -0.035 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 2.698","<b> bootstrap dataset:  193 <\/b> <br>Coef. Urban  : -0.046 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 2.852","<b> bootstrap dataset:  194 <\/b> <br>Coef. Urban  : -0.042 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 2.487","<b> bootstrap dataset:  195 <\/b> <br>Coef. Urban  : -0.097 <br>Coef. Murder : 0.049 <br>Coef. Intercept : 6.521","<b> bootstrap dataset:  196 <\/b> <br>Coef. Urban  : -0.089 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 5.47","<b> bootstrap dataset:  197 <\/b> <br>Coef. Urban  : -0.025 <br>Coef. Murder : 0.037 <br>Coef. Intercept : 3.163","<b> bootstrap dataset:  198 <\/b> <br>Coef. Urban  : -0.011 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 0.937","<b> bootstrap dataset:  199 <\/b> <br>Coef. Urban  : -0.078 <br>Coef. Murder : 0.048 <br>Coef. Intercept : 4.164","<b> bootstrap dataset:  200 <\/b> <br>Coef. Urban  : -0.007 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 1.342","<b> bootstrap dataset:  201 <\/b> <br>Coef. Urban  : -0.04 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 3.42","<b> bootstrap dataset:  202 <\/b> <br>Coef. Urban  : -0.016 <br>Coef. Murder : 0.038 <br>Coef. Intercept : 1.992","<b> bootstrap dataset:  203 <\/b> <br>Coef. Urban  : -0.005 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 1.047","<b> bootstrap dataset:  204 <\/b> <br>Coef. Urban  : -0.058 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 4.242","<b> bootstrap dataset:  205 <\/b> <br>Coef. Urban  : -0.113 <br>Coef. Murder : 0.051 <br>Coef. Intercept : 6.583","<b> bootstrap dataset:  206 <\/b> <br>Coef. Urban  : -0.034 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 2.748","<b> bootstrap dataset:  207 <\/b> <br>Coef. Urban  : -0.051 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 3.238","<b> bootstrap dataset:  208 <\/b> <br>Coef. Urban  : -0.017 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 1.9","<b> bootstrap dataset:  209 <\/b> <br>Coef. Urban  : -0.071 <br>Coef. Murder : 0.054 <br>Coef. Intercept : 3.683","<b> bootstrap dataset:  210 <\/b> <br>Coef. Urban  : -0.028 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 2.413","<b> bootstrap dataset:  211 <\/b> <br>Coef. Urban  : -0.064 <br>Coef. Murder : 0.037 <br>Coef. Intercept : 5.75","<b> bootstrap dataset:  212 <\/b> <br>Coef. Urban  : -0.05 <br>Coef. Murder : 0.049 <br>Coef. Intercept : 3.098","<b> bootstrap dataset:  213 <\/b> <br>Coef. Urban  : -0.056 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 3.353","<b> bootstrap dataset:  214 <\/b> <br>Coef. Urban  : -0.074 <br>Coef. Murder : 0.054 <br>Coef. Intercept : 3.843","<b> bootstrap dataset:  215 <\/b> <br>Coef. Urban  : -0.03 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 2.345","<b> bootstrap dataset:  216 <\/b> <br>Coef. Urban  : -0.045 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 3.12","<b> bootstrap dataset:  217 <\/b> <br>Coef. Urban  : -0.032 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 2.539","<b> bootstrap dataset:  218 <\/b> <br>Coef. Urban  : 0.004 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 0.779","<b> bootstrap dataset:  219 <\/b> <br>Coef. Urban  : -0.076 <br>Coef. Murder : 0.049 <br>Coef. Intercept : 4.072","<b> bootstrap dataset:  220 <\/b> <br>Coef. Urban  : -0.075 <br>Coef. Murder : 0.05 <br>Coef. Intercept : 4.097","<b> bootstrap dataset:  221 <\/b> <br>Coef. Urban  : -0.043 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 2.912","<b> bootstrap dataset:  222 <\/b> <br>Coef. Urban  : -0.02 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 2.074","<b> bootstrap dataset:  223 <\/b> <br>Coef. Urban  : -0.029 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 2.315","<b> bootstrap dataset:  224 <\/b> <br>Coef. Urban  : -0.087 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 6.774","<b> bootstrap dataset:  225 <\/b> <br>Coef. Urban  : -0.026 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 2.163","<b> bootstrap dataset:  226 <\/b> <br>Coef. Urban  : -0.048 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 3.753","<b> bootstrap dataset:  227 <\/b> <br>Coef. Urban  : -0.054 <br>Coef. Murder : 0.049 <br>Coef. Intercept : 2.739","<b> bootstrap dataset:  228 <\/b> <br>Coef. Urban  : -0.039 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 2.692","<b> bootstrap dataset:  229 <\/b> <br>Coef. Urban  : -0.088 <br>Coef. Murder : 0.054 <br>Coef. Intercept : 4.432","<b> bootstrap dataset:  230 <\/b> <br>Coef. Urban  : -0.017 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 1.962","<b> bootstrap dataset:  231 <\/b> <br>Coef. Urban  : -0.07 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 4.409","<b> bootstrap dataset:  232 <\/b> <br>Coef. Urban  : -0.021 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 2.303","<b> bootstrap dataset:  233 <\/b> <br>Coef. Urban  : -0.041 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 2.942","<b> bootstrap dataset:  234 <\/b> <br>Coef. Urban  : -0.089 <br>Coef. Murder : 0.055 <br>Coef. Intercept : 5.1","<b> bootstrap dataset:  235 <\/b> <br>Coef. Urban  : -0.008 <br>Coef. Murder : 0.035 <br>Coef. Intercept : 2.17","<b> bootstrap dataset:  236 <\/b> <br>Coef. Urban  : -0.098 <br>Coef. Murder : 0.048 <br>Coef. Intercept : 6.094","<b> bootstrap dataset:  237 <\/b> <br>Coef. Urban  : -0.069 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 4.702","<b> bootstrap dataset:  238 <\/b> <br>Coef. Urban  : -0.019 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 1.851","<b> bootstrap dataset:  239 <\/b> <br>Coef. Urban  : -0.042 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 3.101","<b> bootstrap dataset:  240 <\/b> <br>Coef. Urban  : -0.023 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 2.481","<b> bootstrap dataset:  241 <\/b> <br>Coef. Urban  : -0.054 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 4.133","<b> bootstrap dataset:  242 <\/b> <br>Coef. Urban  : -0.027 <br>Coef. Murder : 0.036 <br>Coef. Intercept : 2.431","<b> bootstrap dataset:  243 <\/b> <br>Coef. Urban  : -0.05 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 3.966","<b> bootstrap dataset:  244 <\/b> <br>Coef. Urban  : -0.05 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 3.276","<b> bootstrap dataset:  245 <\/b> <br>Coef. Urban  : -0.024 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 2.617","<b> bootstrap dataset:  246 <\/b> <br>Coef. Urban  : -0.072 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 5.5","<b> bootstrap dataset:  247 <\/b> <br>Coef. Urban  : -0.07 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 4.898","<b> bootstrap dataset:  248 <\/b> <br>Coef. Urban  : -0.054 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 4.331","<b> bootstrap dataset:  249 <\/b> <br>Coef. Urban  : -0.041 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 2.998","<b> bootstrap dataset:  250 <\/b> <br>Coef. Urban  : -0.048 <br>Coef. Murder : 0.05 <br>Coef. Intercept : 2.745","<b> bootstrap dataset:  251 <\/b> <br>Coef. Urban  : -0.017 <br>Coef. Murder : 0.036 <br>Coef. Intercept : 2.161","<b> bootstrap dataset:  252 <\/b> <br>Coef. Urban  : -0.016 <br>Coef. Murder : 0.049 <br>Coef. Intercept : 1.064","<b> bootstrap dataset:  253 <\/b> <br>Coef. Urban  : -0.08 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 5.508","<b> bootstrap dataset:  254 <\/b> <br>Coef. Urban  : -0.055 <br>Coef. Murder : 0.037 <br>Coef. Intercept : 5.8","<b> bootstrap dataset:  255 <\/b> <br>Coef. Urban  : -0.001 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 0.846","<b> bootstrap dataset:  256 <\/b> <br>Coef. Urban  : 0.013 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 0.195","<b> bootstrap dataset:  257 <\/b> <br>Coef. Urban  : -0.033 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 2.74","<b> bootstrap dataset:  258 <\/b> <br>Coef. Urban  : -0.064 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 4.307","<b> bootstrap dataset:  259 <\/b> <br>Coef. Urban  : -0.042 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 2.863","<b> bootstrap dataset:  260 <\/b> <br>Coef. Urban  : -0.016 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 1.587","<b> bootstrap dataset:  261 <\/b> <br>Coef. Urban  : -0.087 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 6.083","<b> bootstrap dataset:  262 <\/b> <br>Coef. Urban  : -0.141 <br>Coef. Murder : 0.056 <br>Coef. Intercept : 7.902","<b> bootstrap dataset:  263 <\/b> <br>Coef. Urban  : -0.09 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 5.794","<b> bootstrap dataset:  264 <\/b> <br>Coef. Urban  : -0.083 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 5.452","<b> bootstrap dataset:  265 <\/b> <br>Coef. Urban  : -0.038 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 2.58","<b> bootstrap dataset:  266 <\/b> <br>Coef. Urban  : 0.016 <br>Coef. Murder : 0.043 <br>Coef. Intercept : -0.09","<b> bootstrap dataset:  267 <\/b> <br>Coef. Urban  : -0.03 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 2.812","<b> bootstrap dataset:  268 <\/b> <br>Coef. Urban  : -0.068 <br>Coef. Murder : 0.05 <br>Coef. Intercept : 3.213","<b> bootstrap dataset:  269 <\/b> <br>Coef. Urban  : -0.032 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 1.909","<b> bootstrap dataset:  270 <\/b> <br>Coef. Urban  : -0.075 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 5.273","<b> bootstrap dataset:  271 <\/b> <br>Coef. Urban  : -0.034 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 2.706","<b> bootstrap dataset:  272 <\/b> <br>Coef. Urban  : -0.075 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 4.973","<b> bootstrap dataset:  273 <\/b> <br>Coef. Urban  : -0.006 <br>Coef. Murder : 0.038 <br>Coef. Intercept : 1.746","<b> bootstrap dataset:  274 <\/b> <br>Coef. Urban  : 0.003 <br>Coef. Murder : 0.045 <br>Coef. Intercept : -0.088","<b> bootstrap dataset:  275 <\/b> <br>Coef. Urban  : -0.053 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 3.404","<b> bootstrap dataset:  276 <\/b> <br>Coef. Urban  : -0.008 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 0.503","<b> bootstrap dataset:  277 <\/b> <br>Coef. Urban  : -0.03 <br>Coef. Murder : 0.036 <br>Coef. Intercept : 3.013","<b> bootstrap dataset:  278 <\/b> <br>Coef. Urban  : -0.035 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 2.029","<b> bootstrap dataset:  279 <\/b> <br>Coef. Urban  : -0.047 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 3.595","<b> bootstrap dataset:  280 <\/b> <br>Coef. Urban  : -0.037 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 2.92","<b> bootstrap dataset:  281 <\/b> <br>Coef. Urban  : -0.065 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 4.142","<b> bootstrap dataset:  282 <\/b> <br>Coef. Urban  : -0.034 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 2.758","<b> bootstrap dataset:  283 <\/b> <br>Coef. Urban  : 0.01 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 0.347","<b> bootstrap dataset:  284 <\/b> <br>Coef. Urban  : -0.04 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 2.862","<b> bootstrap dataset:  285 <\/b> <br>Coef. Urban  : -0.023 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 2.809","<b> bootstrap dataset:  286 <\/b> <br>Coef. Urban  : -0.078 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 5.647","<b> bootstrap dataset:  287 <\/b> <br>Coef. Urban  : -0.017 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 1.246","<b> bootstrap dataset:  288 <\/b> <br>Coef. Urban  : -0.017 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 2.052","<b> bootstrap dataset:  289 <\/b> <br>Coef. Urban  : -0.055 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 4.307","<b> bootstrap dataset:  290 <\/b> <br>Coef. Urban  : -0.072 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 5.106","<b> bootstrap dataset:  291 <\/b> <br>Coef. Urban  : -0.064 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 4.285","<b> bootstrap dataset:  292 <\/b> <br>Coef. Urban  : -0.06 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 5.237","<b> bootstrap dataset:  293 <\/b> <br>Coef. Urban  : -0.065 <br>Coef. Murder : 0.036 <br>Coef. Intercept : 5.507","<b> bootstrap dataset:  294 <\/b> <br>Coef. Urban  : -0.045 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 3.236","<b> bootstrap dataset:  295 <\/b> <br>Coef. Urban  : -0.027 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 1.804","<b> bootstrap dataset:  296 <\/b> <br>Coef. Urban  : -0.059 <br>Coef. Murder : 0.049 <br>Coef. Intercept : 3.238","<b> bootstrap dataset:  297 <\/b> <br>Coef. Urban  : -0.055 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 3.31","<b> bootstrap dataset:  298 <\/b> <br>Coef. Urban  : -0.078 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 4.975","<b> bootstrap dataset:  299 <\/b> <br>Coef. Urban  : -0.027 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 2.081","<b> bootstrap dataset:  300 <\/b> <br>Coef. Urban  : -0.061 <br>Coef. Murder : 0.05 <br>Coef. Intercept : 3.063","<b> bootstrap dataset:  301 <\/b> <br>Coef. Urban  : -0.067 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 4.968","<b> bootstrap dataset:  302 <\/b> <br>Coef. Urban  : -0.043 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 3.561","<b> bootstrap dataset:  303 <\/b> <br>Coef. Urban  : -0.075 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 5.302","<b> bootstrap dataset:  304 <\/b> <br>Coef. Urban  : -0.099 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 7.191","<b> bootstrap dataset:  305 <\/b> <br>Coef. Urban  : -0.064 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 4.021","<b> bootstrap dataset:  306 <\/b> <br>Coef. Urban  : -0.071 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 4.145","<b> bootstrap dataset:  307 <\/b> <br>Coef. Urban  : -0.007 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 1.373","<b> bootstrap dataset:  308 <\/b> <br>Coef. Urban  : -0.054 <br>Coef. Murder : 0.037 <br>Coef. Intercept : 5.121","<b> bootstrap dataset:  309 <\/b> <br>Coef. Urban  : -0.001 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 1.192","<b> bootstrap dataset:  310 <\/b> <br>Coef. Urban  : -0.03 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 1.763","<b> bootstrap dataset:  311 <\/b> <br>Coef. Urban  : -0.014 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 1.652","<b> bootstrap dataset:  312 <\/b> <br>Coef. Urban  : -0.091 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 6.076","<b> bootstrap dataset:  313 <\/b> <br>Coef. Urban  : -0.078 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 4.721","<b> bootstrap dataset:  314 <\/b> <br>Coef. Urban  : -0.103 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 6.308","<b> bootstrap dataset:  315 <\/b> <br>Coef. Urban  : -0.037 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 3.168","<b> bootstrap dataset:  316 <\/b> <br>Coef. Urban  : -0.019 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 2.066","<b> bootstrap dataset:  317 <\/b> <br>Coef. Urban  : -0.082 <br>Coef. Murder : 0.048 <br>Coef. Intercept : 5.243","<b> bootstrap dataset:  318 <\/b> <br>Coef. Urban  : -0.027 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 2.007","<b> bootstrap dataset:  319 <\/b> <br>Coef. Urban  : -0.06 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 5.044","<b> bootstrap dataset:  320 <\/b> <br>Coef. Urban  : -0.084 <br>Coef. Murder : 0.056 <br>Coef. Intercept : 3.648","<b> bootstrap dataset:  321 <\/b> <br>Coef. Urban  : -0.058 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 3.87","<b> bootstrap dataset:  322 <\/b> <br>Coef. Urban  : -0.019 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 1.114","<b> bootstrap dataset:  323 <\/b> <br>Coef. Urban  : -0.034 <br>Coef. Murder : 0.037 <br>Coef. Intercept : 3.071","<b> bootstrap dataset:  324 <\/b> <br>Coef. Urban  : -0.043 <br>Coef. Murder : 0.051 <br>Coef. Intercept : 1.949","<b> bootstrap dataset:  325 <\/b> <br>Coef. Urban  : -0.083 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 5.514","<b> bootstrap dataset:  326 <\/b> <br>Coef. Urban  : -0.073 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 5.377","<b> bootstrap dataset:  327 <\/b> <br>Coef. Urban  : -0.037 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 3.381","<b> bootstrap dataset:  328 <\/b> <br>Coef. Urban  : -0.054 <br>Coef. Murder : 0.05 <br>Coef. Intercept : 3.179","<b> bootstrap dataset:  329 <\/b> <br>Coef. Urban  : -0.094 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 6.652","<b> bootstrap dataset:  330 <\/b> <br>Coef. Urban  : -0.094 <br>Coef. Murder : 0.05 <br>Coef. Intercept : 5.02","<b> bootstrap dataset:  331 <\/b> <br>Coef. Urban  : -0.061 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 4.32","<b> bootstrap dataset:  332 <\/b> <br>Coef. Urban  : -0.05 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 3.799","<b> bootstrap dataset:  333 <\/b> <br>Coef. Urban  : -0.067 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 5.728","<b> bootstrap dataset:  334 <\/b> <br>Coef. Urban  : -0.017 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 1.334","<b> bootstrap dataset:  335 <\/b> <br>Coef. Urban  : -0.048 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 3.83","<b> bootstrap dataset:  336 <\/b> <br>Coef. Urban  : -0.02 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 1.291","<b> bootstrap dataset:  337 <\/b> <br>Coef. Urban  : -0.028 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 2.545","<b> bootstrap dataset:  338 <\/b> <br>Coef. Urban  : -0.032 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 3.937","<b> bootstrap dataset:  339 <\/b> <br>Coef. Urban  : -0.053 <br>Coef. Murder : 0.038 <br>Coef. Intercept : 4.684","<b> bootstrap dataset:  340 <\/b> <br>Coef. Urban  : -0.055 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 4.356","<b> bootstrap dataset:  341 <\/b> <br>Coef. Urban  : -0.053 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 3.14","<b> bootstrap dataset:  342 <\/b> <br>Coef. Urban  : -0.064 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 4.381","<b> bootstrap dataset:  343 <\/b> <br>Coef. Urban  : -0.05 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 3.465","<b> bootstrap dataset:  344 <\/b> <br>Coef. Urban  : -0.045 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 2.641","<b> bootstrap dataset:  345 <\/b> <br>Coef. Urban  : -0.038 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 2.504","<b> bootstrap dataset:  346 <\/b> <br>Coef. Urban  : -0.06 <br>Coef. Murder : 0.051 <br>Coef. Intercept : 3.323","<b> bootstrap dataset:  347 <\/b> <br>Coef. Urban  : -0.051 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 3.935","<b> bootstrap dataset:  348 <\/b> <br>Coef. Urban  : -0.057 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 4.065","<b> bootstrap dataset:  349 <\/b> <br>Coef. Urban  : -0.056 <br>Coef. Murder : 0.049 <br>Coef. Intercept : 2.987","<b> bootstrap dataset:  350 <\/b> <br>Coef. Urban  : -0.021 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 2.716","<b> bootstrap dataset:  351 <\/b> <br>Coef. Urban  : -0.025 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 1.45","<b> bootstrap dataset:  352 <\/b> <br>Coef. Urban  : -0.005 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 0.162","<b> bootstrap dataset:  353 <\/b> <br>Coef. Urban  : -0.027 <br>Coef. Murder : 0.049 <br>Coef. Intercept : 1.371","<b> bootstrap dataset:  354 <\/b> <br>Coef. Urban  : -0.04 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 2.587","<b> bootstrap dataset:  355 <\/b> <br>Coef. Urban  : -0.047 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 2.817","<b> bootstrap dataset:  356 <\/b> <br>Coef. Urban  : -0.05 <br>Coef. Murder : 0.048 <br>Coef. Intercept : 3.102","<b> bootstrap dataset:  357 <\/b> <br>Coef. Urban  : -0.068 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 5.543","<b> bootstrap dataset:  358 <\/b> <br>Coef. Urban  : -0.057 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 4.004","<b> bootstrap dataset:  359 <\/b> <br>Coef. Urban  : -0.049 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 3.625","<b> bootstrap dataset:  360 <\/b> <br>Coef. Urban  : -0.044 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 3.794","<b> bootstrap dataset:  361 <\/b> <br>Coef. Urban  : -0.023 <br>Coef. Murder : 0.041 <br>Coef. Intercept : 2.743","<b> bootstrap dataset:  362 <\/b> <br>Coef. Urban  : -0.005 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 0.474","<b> bootstrap dataset:  363 <\/b> <br>Coef. Urban  : -0.052 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 2.734","<b> bootstrap dataset:  364 <\/b> <br>Coef. Urban  : -0.065 <br>Coef. Murder : 0.04 <br>Coef. Intercept : 5.399","<b> bootstrap dataset:  365 <\/b> <br>Coef. Urban  : -0.106 <br>Coef. Murder : 0.058 <br>Coef. Intercept : 5.157","<b> bootstrap dataset:  366 <\/b> <br>Coef. Urban  : -0.074 <br>Coef. Murder : 0.06 <br>Coef. Intercept : 2.714","<b> bootstrap dataset:  367 <\/b> <br>Coef. Urban  : -0.045 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 3.292","<b> bootstrap dataset:  368 <\/b> <br>Coef. Urban  : -0.019 <br>Coef. Murder : 0.048 <br>Coef. Intercept : 1.207","<b> bootstrap dataset:  369 <\/b> <br>Coef. Urban  : -0.056 <br>Coef. Murder : 0.052 <br>Coef. Intercept : 2.768","<b> bootstrap dataset:  370 <\/b> <br>Coef. Urban  : -0.059 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 3.452","<b> bootstrap dataset:  371 <\/b> <br>Coef. Urban  : -0.081 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 5.52","<b> bootstrap dataset:  372 <\/b> <br>Coef. Urban  : 0.046 <br>Coef. Murder : 0.038 <br>Coef. Intercept : -2.392","<b> bootstrap dataset:  373 <\/b> <br>Coef. Urban  : -0.049 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 3.803","<b> bootstrap dataset:  374 <\/b> <br>Coef. Urban  : -0.067 <br>Coef. Murder : 0.047 <br>Coef. Intercept : 3.843","<b> bootstrap dataset:  375 <\/b> <br>Coef. Urban  : -0.047 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 3.342","<b> bootstrap dataset:  376 <\/b> <br>Coef. Urban  : -0.068 <br>Coef. Murder : 0.049 <br>Coef. Intercept : 4.339","<b> bootstrap dataset:  377 <\/b> <br>Coef. Urban  : -0.041 <br>Coef. Murder : 0.038 <br>Coef. Intercept : 3.458","<b> bootstrap dataset:  378 <\/b> <br>Coef. Urban  : -0.081 <br>Coef. Murder : 0.045 <br>Coef. Intercept : 5.508","<b> bootstrap dataset:  379 <\/b> <br>Coef. Urban  : -0.072 <br>Coef. Murder : 0.042 <br>Coef. Intercept : 5.502","<b> bootstrap dataset:  380 <\/b> <br>Coef. Urban  : -0.055 <br>Coef. Murder : 0.05 <br>Coef. Intercept : 3.155","<b> bootstrap dataset:  381 <\/b> <br>Coef. Urban  : -0.034 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 2.07","<b> bootstrap dataset:  382 <\/b> <br>Coef. Urban  : -0.019 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 2.134","<b> bootstrap dataset:  383 <\/b> <br>Coef. Urban  : -0.064 <br>Coef. Murder : 0.049 <br>Coef. Intercept : 3.36","<b> bootstrap dataset:  384 <\/b> <br>Coef. Urban  : -0.075 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 5.04","<b> bootstrap dataset:  385 <\/b> <br>Coef. Urban  : -0.035 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 2.42","<b> bootstrap dataset:  386 <\/b> <br>Coef. Urban  : -0.052 <br>Coef. Murder : 0.054 <br>Coef. Intercept : 1.776","<b> bootstrap dataset:  387 <\/b> <br>Coef. Urban  : -0.069 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 4.334","<b> bootstrap dataset:  388 <\/b> <br>Coef. Urban  : -0.033 <br>Coef. Murder : 0.046 <br>Coef. Intercept : 2.226","<b> bootstrap dataset:  389 <\/b> <br>Coef. Urban  : -0.062 <br>Coef. Murder : 0.049 <br>Coef. Intercept : 3.482","<b> bootstrap dataset:  390 <\/b> <br>Coef. Urban  : -0.091 <br>Coef. Murder : 0.05 <br>Coef. Intercept : 5.199","<b> bootstrap dataset:  391 <\/b> <br>Coef. Urban  : -0.121 <br>Coef. Murder : 0.048 <br>Coef. Intercept : 7.913","<b> bootstrap dataset:  392 <\/b> <br>Coef. Urban  : -0.052 <br>Coef. Murder : 0.049 <br>Coef. Intercept : 3.096","<b> bootstrap dataset:  393 <\/b> <br>Coef. Urban  : -0.012 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 2.028","<b> bootstrap dataset:  394 <\/b> <br>Coef. Urban  : -0.099 <br>Coef. Murder : 0.048 <br>Coef. Intercept : 6.625","<b> bootstrap dataset:  395 <\/b> <br>Coef. Urban  : -0.036 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 3.061","<b> bootstrap dataset:  396 <\/b> <br>Coef. Urban  : -0.038 <br>Coef. Murder : 0.039 <br>Coef. Intercept : 3.394","<b> bootstrap dataset:  397 <\/b> <br>Coef. Urban  : -0.062 <br>Coef. Murder : 0.043 <br>Coef. Intercept : 3.873","<b> bootstrap dataset:  398 <\/b> <br>Coef. Urban  : -0.035 <br>Coef. Murder : 0.044 <br>Coef. Intercept : 3.645","<b> bootstrap dataset:  399 <\/b> <br>Coef. Urban  : -0.08 <br>Coef. Murder : 0.051 <br>Coef. Intercept : 4.785"],"hoverinfo":["text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text"],"showlegend":false,"marker":{"color":"rgba(0, 0, 0, 0.5)","line":{"color":"rgba(31,119,180,1)"}},"type":"scatter","error_y":{"color":"rgba(31,119,180,1)"},"error_x":{"color":"rgba(31,119,180,1)"},"line":{"color":"rgba(31,119,180,1)"},"xaxis":"x","yaxis":"y","frame":null}],"highlight":{"on":"plotly_click","persistent":false,"dynamic":false,"selectize":false,"opacityDim":0.20000000000000001,"selected":{"opacity":1},"debounce":0},"shinyEvents":["plotly_hover","plotly_click","plotly_selected","plotly_relayout","plotly_brushed","plotly_brushing","plotly_clickannotation","plotly_doubleclick","plotly_deselect","plotly_afterplot","plotly_sunburstclick"],"base_url":"https://plot.ly"},"evals":[],"jsHooks":[]}</script>
```


**F-statistic**.

We can also use an $F$ test for any $q$ hypotheses. Specifically, when $q$ hypotheses *restrict* a model, the degrees of freedom drop from $k_{u}$ to $k_{r}$ and the residual sum of squares $RSS=\sum_{i}(y_{i}-\widehat{y}_{i})^2$ typically increases. We compute the statistic
$$
F_{q} = \frac{(RSS_{r}-RSS_{u})/(k_{u}-k_{r})}{RSS_{u}/(N-k_{u})}
$$

If you test whether all $K$ variables are significant, the restricted model is a simple intercept and $RSS_{r}=TSS$, and $F_{q}$ can be written in terms of $R^2$: $F_{K} = \frac{R^2}{1-R^2} \frac{N-K}{K-1}$. The first fraction is the relative goodness of fit, and the second fraction is an adjustment for degrees of freedom (similar to how we  adjusted the $R^2$ term before). 

To conduct a hypothesis test, first compute a null distribution by randomly reshuffling the outcomes and recompute the $F$ statistic, and then compare how often random data give something as extreme as your initial statistic. For some intuition on this F test, examine how the adjusted $R^2$ statistic varies with bootstrap samples. 

``` r
# Bootstrap under the null
boots <- 1:399
boot_regs0 <- lapply(boots, function(b){
  # Generate bootstrap sample
  xy_b <- USArrests
  b_id <- sample( nrow(USArrests), replace=T)
  # Impose the null
  xy_b$Murder <-  xy_b$Murder[b_id]
  # Run regression
  reg_b <- lm(Murder~Assault+UrbanPop, dat=xy_b)
})
# Get null distribution for adjusted R2
R2adj_sim0 <- sapply(boot_regs0, function(reg_k){
    summary(reg_k)$adj.r.squared })
hist(R2adj_sim0, xlim=c(-.1,1), breaks=25, border=NA,
    main='', xlab=expression('adj.'~R[b]^2))

# Compare to initial statistic
abline(v=summary(reg)$adj.r.squared, lwd=2, col=2)
```

<img src="03-LinearRegression_files/figure-html/unnamed-chunk-28-1.png" width="672" />

Note that *hypothesis testing is not to be done routinely*, as additional complications arise when testing multiple hypothesis sequentially.

Under some additional assumptions $F_{q}$ follows an F-distribution. For more about F-testing, see https://online.stat.psu.edu/stat501/lesson/6/6.2 and https://www.econometrics.blog/post/understanding-the-f-statistic/

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
**Hansen Econometrics, Theorem 17.1:** *The fixed effects estimator of $\beta$ algebraically equals the dummy variable estimator of $\beta$. The two estimators have the same residuals.*
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
## 0.9111437
```

``` r
fixef(fe_reg1)[1:2]
```

```
## $fo
##         0         1         2         3         4 
##  7.399687 10.668256 15.217952 23.255949 39.571446 
## 
## $fu
##         A         B 
##   0.00000 -22.30994
```

``` r
# Compare Coefficients
fe_reg0 <- lm(y~-1+x+fo+fu, dat_f)
coef( fe_reg0 )
```

```
##           x         fo0         fo1         fo2         fo3         fo4 
##   0.9111437   7.3996867  10.6682556  15.2179522  23.2559486  39.5714459 
##         fuB 
## -22.3099421
```

With fixed effects, we can also compute averages for each group and construct a *between estimator*: $\bar{y}_i = \alpha + \bar{x}_i \beta$. Or we can subtract the average from each group to construct a *within estimator*: $(y_{it} - \bar{y}_i) = (x_{it}-\bar{x}_i)\beta$. 

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
## 1    993 69756                                  
## 2    980  5897 13     63859 816.33 < 2.2e-16 ***
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
## 1    993 69756                                    
## 2    989 10374  4     59382 2467.082 < 2.2e-16 ***
## 3    980  5897  9      4477   82.661 < 2.2e-16 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
```




<!-- 
> The labels "random effects" and "fixed effects" are misleading. These are labels which arose in the early literature and we are stuck with these labels today. In a previous era regressors were viewed as "fixed". Viewing the individual effect as an unobserved regressor leads to the label of the individual effect as "fixed". Today, we rarely refer to regressors as "fixed" when dealing with observational data. We view all variables as random. Consequently describing u i as "fixed" does not make much sense and it is hardly a contrast with the "random effect" label since under either assumption u i is treated as random. Once again, the labels are unfortunate but the key difference is whether u i is correlated with the regressors.
-->


**Break Points**.
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


Generate a simulated dataset with 30 observations and two exogenous variables. Assume the following relationship: $y_{i} = \beta_0 + \beta_1 x_{i1} + \beta_2 x_{i2} + \epsilon_i$ where the variables and the error term are realizations of the following data generating processes (DGP):

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
##   8.3731118   1.5616432   0.6425633
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

<img src="03-LinearRegression_files/figure-html/unnamed-chunk-34-1.png" width="672" />


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

<img src="03-LinearRegression_files/figure-html/unnamed-chunk-35-1.png" width="672" />

In general, you can interpret your regression coefficients as "adjusted correlations". There are (many) tests for whether the relationships in your dataset are actually additively separable and linear.


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
y^{(\lambda)}_{i} = \sum_{k=1}^{K}\beta_{k} x^{(\rho)}_{ik} + \epsilon_{i}\\
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

<img src="03-LinearRegression_files/figure-html/unnamed-chunk-36-1.png" width="960" style="display: block; margin: auto;" />

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

<img src="03-LinearRegression_files/figure-html/unnamed-chunk-37-1.png" width="672" />

When explicitly transforming data according to $\lambda$ and $\rho$, these parameters increase the degrees of freedom by two. The default hypothesis testing procedures do not account for you trying out different transformations, and should be adjusted by the increased degrees of freedom. Specification searches deflate standard errors and are a major source for false discoveries.

##  Diagnostics

There's little sense in getting great standard errors for a terrible model. Plotting your regression object a simple and easy step to help diagnose whether your model is in some way bad. We next go through what each of these figures show.

``` r
reg <- lm(Murder~Assault+UrbanPop, data=USArrests)
par(mfrow=c(2,2))
plot(reg, pch=16, col=grey(0,.5))
```

<img src="03-LinearRegression_files/figure-html/unnamed-chunk-38-1.png" width="960" style="display: block; margin: auto;" />



**Outliers**.
The first diagnostic plot examines outliers in terms the outcome $y_i$ being far from its prediction $\hat{y}_i$. You may be interested in such outliers because they can (but do not have to) unduly influence your estimates. 

The third diagnostic plot examines another type of outlier, where an observation with the explanatory variable $x_i$ is far from the center of mass of the other $x$'s. A point has high *leverage* if the estimates change dramatically when you estimate the model without that data point.

``` r
N <- 40
x <- c(25, runif(N-1,3,8))
e <- rnorm(N,0,0.4)
y <- 3 + 0.6*sqrt(x) + e
plot(y~x, pch=16, col=grey(0,.5))
points(x[1],y[1], pch=16, col=rgb(1,0,0,.5))

abline(lm(y~x), col=2, lty=2)
abline(lm(y[-1]~x[-1]))
```

<img src="03-LinearRegression_files/figure-html/unnamed-chunk-39-1.png" width="672" />

See [AEJ-leverage](https://www.rwi-essen.de/fileadmin/user_upload/RWI/Publikationen/I4R_Discussion_Paper_Series/032_I4R_Haddad_Kattan_Wochner-updateJune28.pdf) and [NBER-leverage](https://statmodeling.stat.columbia.edu/2025/02/28/the-r-squared-on-this-is-kinda-low-no/) for examples of leverage in economics.

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


**Normality**.
The second plot examines whether the residuals are normally distributed. Your OLS coefficient estimates do not depend on the normality of the residuals. (Good thing, because there's no reason the residuals of economic phenomena should be so well behaved.) Many hypothesis tests are, however, affected by the distribution of the residuals. For these reasons, you may be interested in assessing normality 

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

**Collinearity**.
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
plot(y~x, data=xy, pch=16, col=grey(0,.5))
abline(lm(y~x,data=xy))
```

<img src="03-LinearRegression_files/figure-html/unnamed-chunk-45-1.png" width="672" />

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


Three statistical tools: 2SLS, RDD, and DID, are designed to address endogeneity issues. The elementary versions of these tools are linear regression. Because there are many textbooks and online notebooks that explain these methods at both high and low levels of technical detail, they are not covered extensively in this notebook. Instead, I will focus on the seminal economic example to provide some intuition.


**Competitive Market Equilibrium**. This model has three structural relationships: (1) market supply is the sum of quantities supplied by individual firms at a given price, (2) market demand is the sum of quantities demanded by individual people at a given price, and (3) market supply equals market demand in equilibrium. Assuming market supply and demand are linear, we can write these three relationships as
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
##       P           D          S
## [1,]  8  1.55901913 0.07846755
## [2,]  9  0.75901913 1.07846755
## [3,] 10 -0.04098087 2.07846755
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

<img src="03-LinearRegression_files/figure-html/unnamed-chunk-47-1.png" width="672" />

Suppose we ask "what is the effect of price on quantity?" You can simply run a regression of quantity ("Y") on price ("X"): $\widehat{\beta}_{OLS} = Cov(Q^{*}, P^{*}) / Var(P^{*})$. You get a number back, but it is hard to interpret meaningfully. 

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
## -0.54232 -0.13835 -0.01141  0.11155  0.54348 
## 
## Coefficients:
##             Estimate Std. Error t value Pr(>|t|)    
## (Intercept) -1.01522    0.48490  -2.094   0.0371 *  
## P            0.21510    0.05447   3.949  9.8e-05 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 0.186 on 298 degrees of freedom
## Multiple R-squared:  0.04973,	Adjusted R-squared:  0.04654 
## F-statistic: 15.59 on 1 and 298 DF,  p-value: 9.8e-05
```
This simple derivation has a profound insight: price-quantity data does not generally tell you how price affects quantity (or vice-versa). The reason is simultaneity: price and quantity mutually cause one another in markets.^[Although there are many ways this simultaneity can happen, economic theorists have made great strides in analyzing the simultaneity problem as it arises from equilibrium market relationships. In fact, 2SLS arose to understand agricultural markets.]

Moreover, this example also clarifies that our initial question "what is the effect of price on quantity?" is misguided. We could more sensibly ask  "what is the effect of price on quantity supplied?" or "what is the effect of price on quantity demanded?"


## Two Stage Least Squares (2SLS)

If you have exogenous variation on one side of the market, "shocks", you can get information on the other. For example, lower costs shift out supply (more is produced at given price), allowing you to trace out part of a demand curve.
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

<img src="03-LinearRegression_files/figure-html/unnamed-chunk-49-1.png" width="672" />

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
## -0.88312 -0.16634 -0.01646  0.17131  0.76705 
## 
## Coefficients:
##             Estimate Std. Error t value Pr(>|t|)    
## (Intercept)  6.62308    0.19097   34.68   <2e-16 ***
## P           -0.63484    0.02245  -28.28   <2e-16 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 0.2492 on 598 degrees of freedom
## Multiple R-squared:  0.5721,	Adjusted R-squared:  0.5714 
## F-statistic: 799.6 on 1 and 598 DF,  p-value: < 2.2e-16
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
## [1,] 8.899933 0.8991567
## [2,] 8.088433 1.5620318
```

``` r
B_est <- diff(dat_mean[,2])/diff(dat_mean[,1])
round(B_est, 2)
```

```
## [1] -0.82
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
## -0.52725 -0.13309 -0.01224  0.11673  0.58651 
## 
## Coefficients:
##             Estimate Std. Error t value Pr(>|t|)    
## (Intercept)  8.16908    0.15996   51.07   <2e-16 ***
## Phat        -0.81685    0.01881  -43.42   <2e-16 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 0.187 on 598 degrees of freedom
## Multiple R-squared:  0.7592,	Adjusted R-squared:  0.7588 
## F-statistic:  1886 on 1 and 598 DF,  p-value: < 2.2e-16
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
## (Intercept)  8.169081   0.224656  36.3626 < 2.2e-16 ***
## fit_P       -0.816852   0.026418 -30.9202 < 2.2e-16 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## RMSE: 0.262126   Adj. R2: 0.524317
## F-test (1st stage), P: stat = 2,415.1, p < 2.2e-16, on 1 and 598 DoF.
##            Wu-Hausman: stat =   476.5, p < 2.2e-16, on 1 and 597 DoF.
```

**Within Group Variance**.
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
## Ed_sigma.0.25           -0.62         -0.61      -0.72
## Ed_sigma.1               0.33          0.30      -0.14
## 
## [[2]]
##                Es_sigma.0.001 Es_sigma.0.25 Es_sigma.1
## Ed_sigma.0.001          -0.80         -0.80      -0.80
## Ed_sigma.0.25           -0.80         -0.77      -0.80
## Ed_sigma.1              -0.78         -0.81      -0.79
```




**Caveats**.
Regression analysis with instrumental variables can be very insightful and is applied to many different areas. But I also want to stress some caveats about using IV in practice.

We always get coefficients back when running `feols`, and sometimes the computed p-values are very small. The interpretation of those numbers rests on many assumptions:

* only supply was affected (Instrument exogeneity)
* the shock is large enough to be picked up statistically (Instrument relevance)
* supply and demand are linear and additively separable (Functional form)
* we were not cycling through different IV's (Multiple hypotheses)

We are rarely sure that all of these assumptions hold, and this is one reason why researchers often also report their OLS results.






## Regression Discontinuities/Kink (RD/RK)

The basic idea here is to examine how a variable changes in response to an exogenous shock. The Regression Discontinuities estimate of the cost shock is the difference in the outcome variable just before and just after the shock. We now turn to our canonical competitive market example. The RD estimate is the difference between the lines at $T=300$.


``` r
dat2$T <- 1:nrow(dat2)
cols <- ifelse(as.numeric(dat2$cost)==2, rgb(0,0,1,.5), rgb(0,0,0,.5))

plot(P~T, dat2, main='Effect of Cost Shock on Price', 
    font.main=1, pch=16, col=cols)
regP1 <- lm(P~T, dat2[dat2$cost==1,]) 
lines(regP1$model$T, predict(regP1), col=rgb(0,0,0), lwd=2)
regP2 <- lm(P~T, dat2[dat2$cost==2,]) 
lines(regP2$model$T, predict(regP2), col=rgb(0,0,1), lwd=2)
```

<img src="03-LinearRegression_files/figure-html/unnamed-chunk-56-1.png" width="672" />

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
## -0.54802 -0.14230 -0.00139  0.13478  0.59313 
## 
## Coefficients:
##               Estimate Std. Error t value Pr(>|t|)    
## (Intercept)  8.887e+00  2.342e-02 379.483   <2e-16 ***
## T            8.499e-05  1.349e-04   0.630    0.529    
## cost2       -8.651e-01  6.616e-02 -13.076   <2e-16 ***
## T:cost2      6.227e-05  1.907e-04   0.326    0.744    
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 0.2023 on 596 degrees of freedom
## Multiple R-squared:  0.8021,	Adjusted R-squared:  0.8011 
## F-statistic:   805 on 3 and 596 DF,  p-value: < 2.2e-16
```


``` r
plot(Q~T, dat2, main='Effect of Cost Shock on Quantity',
    font.main=1, pch=16, col=cols)
regQ1 <- lm(Q~T, dat2[dat2$cost==1,]) 
lines(regQ1$model$T, predict(regQ1), col=rgb(0,0,0), lwd=2)
regQ2 <- lm(Q~T, dat2[dat2$cost==2,]) 
lines(regQ2$model$T, predict(regQ2), col=rgb(0,0,1), lwd=2)
```

<img src="03-LinearRegression_files/figure-html/unnamed-chunk-57-1.png" width="672" />

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
## -0.51970 -0.12984 -0.01395  0.11936  0.59884 
## 
## Coefficients:
##               Estimate Std. Error t value Pr(>|t|)    
## (Intercept)  0.8766667  0.0214883  40.797  < 2e-16 ***
## T            0.0001494  0.0001238   1.208  0.22771    
## cost2        0.8537494  0.0607023  14.065  < 2e-16 ***
## T:cost2     -0.0005232  0.0001750  -2.990  0.00291 ** 
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 0.1856 on 596 degrees of freedom
## Multiple R-squared:  0.7634,	Adjusted R-squared:  0.7622 
## F-statistic: 641.1 on 3 and 596 DF,  p-value: < 2.2e-16
```

Remember that this is effect is *local*: different magnitudes of the cost shock or different demand curves generally yield different estimates.

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
dat3$Pre <- dat3$T < N # Size of first treatment group

# Plot Price Data
par(mfrow=c(1,2))
plot(P~T, dat2, main='Effect of Cost Shock on Price', 
    font.main=1, pch=16, col=cols, cex=.5)
lines(regP1$model$T, predict(regP1), col=rgb(0,0,0), lwd=2)
lines(regP2$model$T, predict(regP2), col=rgb(0,0,1), lwd=2)
# W/ Control group
points(P~T, dat3, pch=16, col=rgb(1,0,0,.5), cex=.5)
regP3a <- lm(P~T, dat3[dat3$Pre,]) 
lines(regP3a$model$T, predict(regP3a), col=rgb(1,0,0), lwd=2)
regP3b <- lm(P~T, dat3[!dat3$Pre,]) 
lines(regP3b$model$T, predict(regP3b), col=rgb(1,0,0), lwd=2)


# Plot Quantity Data
plot(Q~T, dat2, main='Effect of Cost Shock on Quantity',
    font.main=1, pch=17, col=cols, cex=.5)
lines(regQ1$model$T, predict(regQ1), col=rgb(0,0,0), lwd=2)
lines(regQ2$model$T, predict(regQ2), col=rgb(0,0,1), lwd=2)
# W/ Control group
points(Q~T, dat3, pch=16, col=rgb(1,0,0,.5), cex=.5)
regQ3a <- lm(Q~T, dat3[dat3$Pre,]) 
lines(regQ3a$model$T, predict(regQ3a), col=rgb(1,0,0), lwd=2)
regQ3b <- lm(Q~T, dat3[!dat3$Pre,]) 
lines(regQ3b$model$T, predict(regQ3b), col=rgb(1,0,0), lwd=2)
```

<img src="03-LinearRegression_files/figure-html/unnamed-chunk-58-1.png" width="672" />

``` r
# Single Regression Estimates
# Pool Data
dat2$Pre <- dat2$T < N # Size of first treatment group
dat2$EverTreat <- 1
dat3$EverTreat <- 0
dat <- rbind(dat2, dat3)
# Estimate Intercept Shifts
regP <- lm(P~Pre*EverTreat, dat)
summary(regP)
```

```
## 
## Call:
## lm(formula = P ~ Pre * EverTreat, data = dat)
## 
## Residuals:
##      Min       1Q   Median       3Q      Max 
## -0.54957 -0.14013  0.00043  0.13850  0.91850 
## 
## Coefficients:
##                    Estimate Std. Error t value Pr(>|t|)    
## (Intercept)        8.883821   0.011531 770.432   <2e-16 ***
## PreTRUE            0.006313   0.016334   0.386    0.699    
## EverTreat         -0.792326   0.016307 -48.587   <2e-16 ***
## PreTRUE:EverTreat  0.801757   0.023100  34.707   <2e-16 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 0.2001 on 1196 degrees of freedom
## Multiple R-squared:  0.7508,	Adjusted R-squared:  0.7502 
## F-statistic:  1201 on 3 and 1196 DF,  p-value: < 2.2e-16
```

``` r
regQ <- lm(Q~Pre*EverTreat, dat)
summary(regQ)
```

```
## 
## Call:
## lm(formula = Q ~ Pre * EverTreat, data = dat)
## 
## Residuals:
##      Min       1Q   Median       3Q      Max 
## -0.66400 -0.12737 -0.00314  0.12137  0.58782 
## 
## Coefficients:
##                   Estimate Std. Error t value Pr(>|t|)    
## (Intercept)        0.89897    0.01045  86.019   <2e-16 ***
## PreTRUE           -0.01138    0.01480  -0.769    0.442    
## EverTreat          0.66216    0.01478  44.802   <2e-16 ***
## PreTRUE:EverTreat -0.65191    0.02094 -31.137   <2e-16 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 0.1813 on 1196 degrees of freedom
## Multiple R-squared:  0.7181,	Adjusted R-squared:  0.7174 
## F-statistic:  1015 on 3 and 1196 DF,  p-value: < 2.2e-16
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

In practice, it is hard to find a good natural experiment. For example, suppose we asked "what is the effect of wages on police demanded?" and examined a policy which lowered the educational requirements from 4 years to 2 to become an officer. This increases the labour supply, but it also affects the demand curve through "general equilibrium": as some of the new officers were potentially criminals and, with fewer criminals, the demand for police shifts down.

In practice, it is also easy to find a bad instrument. Paradoxically, natural experiments are something you are supposed to find but never search for. As you search for good instruments, for example, sometimes random noise will appear like a good instrument (spurious instruments). In this age of big data, we are getting increasingly more data and, perhaps surprisingly, this makes it easier to make false discoveries. 

We will consider three classical ways for false discoveries to arise. After that, there are examples with the latest and greatest empirical recipes---we don't have so many theoretical results yet but I think you can understand the issue with the numerical example. Although it is difficult to express numerically, you must also know that if you search for a good natural experiment for too long, you can also be led astray from important questions. There are good reasons to be excited about empirical social science, but we would be wise to recall some earlier wisdom from economists on the matter.

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
    pch=16, col=grey(0,.5), font.main=1,
    main=paste0('Random Dataset ', i,":   p=",
        formatC(p,digits=2, format='fg')))
abline(reg_i)
```

<img src="03-LinearRegression_files/figure-html/unnamed-chunk-59-1.png" width="672" />

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

<img src="03-LinearRegression_files/figure-html/unnamed-chunk-63-1.png" width="672" />

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

<img src="03-LinearRegression_files/figure-html/unnamed-chunk-64-1.png" width="672" />


``` r
# Include an intercept to regression 1
#reg2 <-  lm(cage_films ~ science_spending, data=vigen_csv)
#suppressMessages(library(stargazer))
#stargazer(reg1, reg2, type='html')
```

**The same principles apply to regression-based approaches to endogeneity issues**. For example, we now run IV regressions for different variable combinations in the dataset of spurious relationships

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

<img src="03-LinearRegression_files/figure-html/unnamed-chunk-66-1.png" width="672" />

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

In practice, it is hard to find a good natural experiment. For example, suppose we asked "what is the effect of wages on police demanded?" and examined a policy which lowered the educational requirements from 4 years to 2 to become an officer. This increases the labour supply, but it also affects the demand curve through "general equilibrium": as some of the new officers were potentially criminals. With fewer criminals, the demand for likely police shifts down.

In practice, it is surprisingly easy to find a bad instrument. Paradoxically, natural experiments are something you are supposed to find but never search for. As you search for good instruments, for example, sometimes random noise will appear like a good instrument (Spurious instruments). Worse, if you search for a good instrument for too long, you can also be led astray from important questions.


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

<img src="03-LinearRegression_files/figure-html/unnamed-chunk-67-1.png" width="672" />


**IV**.
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


**RDD**.
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

<img src="03-LinearRegression_files/figure-html/unnamed-chunk-69-1.png" width="672" />


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


**DID**.
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

<img src="03-LinearRegression_files/figure-html/unnamed-chunk-71-1.png" width="672" />


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
