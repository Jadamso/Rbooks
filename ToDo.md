# To Do

## Big Picture 

Style 

* Transfer to quarto and allow student annotation
* Make R code use "cache" 
* Add student callouts
* Provide simple numerical examples for each mathematical expression
* Each chapter ends with 3 questions.
* Update the writing, as well as references/bibliography
* Clean up all figures (axes, titles, legends, ...)


Content

* More introduction to R in Chapter 1
* Add a little math about probabality distributions to the first part of section 4, plus a little sampling theory and real-world applications to 4.3
* Add some theory about adjusted R2 and F-test to 11.4, also introduce J-test
* Complete 12.4 (Regressograms) 
* Complete 14.1 (Experimental Design)
* Add semi-formal treatment of "Multiple Hypothesis Testing" to 15.1
* Complete 16 Misc Topics.


## Quarto/Bookdown (Specifics)

Add Annotation (quarto)
https://web.hypothes.is/hypothesis-for-faculty-instructors/


Callouts

* ::: {.callout-tip, icon=false, collapse="true"}
* ::: {.callout-note, icon=false, collapse="true"}
* ::: {.callout-warning, icon=false, collapse="true"}
* ::: {.callout-important, icon=false, collapse="true"}


Notes (custom code)

* ::: {.aside}
* ::: {.tip}
* ::: {.background}


See also 

https://bookdown.org/yihui/bookdown/markdown-extensions-by-bookdown.html
https://bookdown.org/yihui/bookdown/web-pages-and-shiny-apps.html
https://bookdown.org/yihui/rmarkdown-cookbook/cache-path.html
https://quarto.org/docs/output-formats/html-basics.html
https://quarto.org/docs/dashboards/interactivity/observable.html

knitr::include_url("https://sites.google.com/view/jordan-adamson/")

<!--
The compilation instructions are in 'index.Rmd' 
To Create from scratch, use a template ``bookdown::create_gitbook('index.Rmd')``
-->

* https://github.com/bvkrauth/is4e/, https://bookdown.org/bkrauth/IS4E/
* https://github.com/Camilo-Mora/GEO380
* https://github.com/rstudio/bookdown
* https://bookdown.org/pkaldunn/SRM-Textbook/

Note that Github repos must be public to deploy!
https://bookdown.org/yihui/bookdown/github.html


## Introduction to Data Analysis (Specifics)

? Coefficient of colligation

Weighted means, quantiles, and variance
```{r}
 wt <- c(5,  5,  4,  1)
 x <- c(3.7,3.3,3.5,2.8)
 xm <- sum(wt*x)/sum(wt)
 v <- sum(wt * (x - xm)^2)/sum(wt)
 
weighted.mean
spatstat.univar::weighted.quantile
    oo <- order(x)
    x <- x[oo]
    w <- w[oo]
    Fx <- cumsum(w)/sum(w)
    med_id <- max(which(Fx <= .5))+1
    x[med_id]
    
```
https://seismo.berkeley.edu/~kirchner/Toolkits/Toolkit_12.pdf
https://www.bookdown.org/rwnahhas/RMPH/survey-desc.html



#### Data Analysis

https://onlinelibrary.wiley.com/doi/10.1002/%28SICI%291099-1255%28199709/10%2912%3A5%3C533%3A%3AAID-JAE454%3E3.0.CO%3B2-V

Add styling to interactive plots

Data clean/merge
 * by, with, subset, stack, switch
 * do.call, reduce
 * data.table, ...



## Introduction to Linear Regression (Specifics)

Add interactive plots via https://plotly-r.com/

**Interpretation**
https://easystats.github.io/report/


#### Adjusted R2 (add to 10.4)
https://davegiles.blogspot.com/2013/10/in-what-sense-is-adjusted-r-squared.html
https://stats.stackexchange.com/questions/130069/what-is-the-distribution-of-r2-in-linear-regression-under-the-null-hypothesis
Rencher, A. C., & Schaalje, G. B. (2008). Linear Models in Statistics (2nd ed.). Wiley. Chapter 5 (“The General Linear Model”), Section 5.6.2 (“Distribution of R2 under the Null Hypothesis”), which shows that under the null (all slopes zero) and Gaussian errors,

https://statmodeling.stat.columbia.edu/2024/06/17/this-well-known-paradox-of-r-squared-is-still-buggin-me-can-you-help-me-out/

#### F-Test (add to 10.4)
ANOVA

```{r}
model0 <- lm(sr ~ 1, data = LifeCycleSavings) ## Null restricted model
model1 <- lm(sr ~ 1 + pop15 , data = LifeCycleSavings) ## Alternative unrestricted model
anova(model0, model1, test = "F")

# Manual F-test
rss0 <- sum(resid(model0)^2)
rss1 <- sum(resid(model1)^2)
df0  <- df.residual(model0)
df1  <- df.residual(model1)
F    <- ((rss0 - rss1)/(df0-df1)) / (rss1/df1)
p    <- 1-pf(F, df0-df1, df1)
cbind(F, p)
```

#### J-Test (add to 10.4)
* https://bookdown.org/mike/data_analysis/non-nested-model-tests.html#sec-davidson--mackinnon-j-test



#### Diminishing Returns
Value of More Data: Just as before, there are diminishing returns to larger sample sizes with simple OLS.

```{r}
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


#### Derive Simple OLS

* "Introduction to Econometrics with R" by Hanck, Arnold, Gerber, and Schmelzer, https://www.econometrics-with-r.org/
(taking seriously Greene's "Model Building--A General to Simple Strategy")




#### Parametric Variability Estimates and Hypothesis Tests [Under Construction]


First note that we can compute classic estimates for variability: denoting the Standard Error of the Regression as $\hat{\sigma}$, and the Standard Error of the Coefficient Estimates as $\hat{\sigma}_{\hat{\alpha}}$ and $\hat{\sigma}_{\hat{\beta}}~~$ (or simply Standard Errors).
$$
\hat{\sigma}^2 = \frac{1}{n-2}\sum_{i}\hat{\epsilon_{i}}^2\\
\hat{\sigma}^2_{\hat{\alpha}}=\hat{\sigma}^2\left[\frac{1}{n}+\frac{\bar{x}^2}{\sum_{i}(x_i-\bar{x})^2}\right]\\
\hat{\sigma}^2_{\hat{\beta}}=\frac{\hat{\sigma}^2}{\sum_{i}(x_i-\bar{x})^2}.
$$
These equations are motivated by particular data generating proceses, which you can read more about this at https://www.econometrics-with-r.org/4-lrwor.html.]


In general, note that the linear model has
$$
\hat{\Sigma}_{\beta} = (X'X)^{-1} X' \widehat{\Omega} X (X'X)^{-1}.\\
\widehat{\Omega} = \begin{pmatrix}
\hat{\sigma}_{1,1} & ... & \hat{\sigma}_{1,n}\\
& ... &  \\
\hat{\sigma}_{n,1} & ... & \hat{\sigma}_{n,n}
\end{pmatrix}
$$
Standard Errors are the diagonal: $diag( \hat{\Sigma}_{\beta}  )$


**Classical Linear Model (CLM)**
Independance: $\hat{\sigma_{i,j}}=0$
Homoskedasticity: 
$$
diag( \widehat{\Omega} ) = [\hat{\sigma}^2, \hat{\sigma}^2, ..., \hat{\sigma}^2] \\
\hat{\sigma}^2=\frac{1}{n-K}\sum_{i}\hat{\epsilon}_i^2\\
$$
IID Variability Estimates
$$
\hat{\Sigma}_{\beta} = \hat{\sigma}^2 (X'X)^{-1}\\
$$

```{r}
n <- nrow(X)
K <- ncol(X)
s <- sum( Ehat^2 )/(n-K)
Vhat <- s * XtXi

vcov(reg)
```

**Reality**
There are common violations to the iid case. 
Heteroskedasticity:
$$
diag( \widehat{\Omega} ) = [\widehat{\sigma^2_{1}}, \widehat{\sigma^2_{1}}, ..., \widehat{\sigma^2_{n}}]\\
\widehat{\sigma^2_{i}} = \hat{\epsilon_{i}}^2
$$

Autocorrelation Dependence: $\sigma_{i,j}=f( dist(i,j) )$.

Cluster Dependence: 
$$\sigma_{i,j}=
\begin{cases}
\hat{\sigma}_{group1} & i,j \in \text{group } 1\\
...\\
\hat{\sigma}_{groupG} & i,j \in \text{group } G \\
0 & \text{otherwise} \\ 
\end{cases}
$$


This is for a later course. (See https://cran.r-project.org/web/packages/sandwich/vignettes/sandwich.pdf and then https://cran.r-project.org/web/packages/sandwich/vignettes/sandwich-CL.pdf)


```{r, eval=F, results='hide'}
## Seperate tests each coef is 0
## Calculate standard errors, t–statistics, p-values
SEhat <- sqrt(diag(Vhat))
That  <- Bhat/SEhat

## One Sided Test for P(t > That | Null)
Phat1  <- pt(That, n-K)
## Two Sided Test for P(t > That or  t < -That | Null)
Phat2  <- 1-pt( abs(That), n-K) + pt(-abs(That), n-K)

Phat2
summary(reg)


## Joint test all 3 coefs are 0
Fhat <- (TSS - ESS)/ESS * (n-K)/3
1-pf(Fhat, 3, n-K)

summary(reg)$fstatistic

summary(reg)
```


#### Diagnostics 

Note that we can also calculate the leverage vector $H = [h_{1}, h_{2}, ...., h_{N}]$  directly from our OLS projection matrix $\hat{P}$, since $H=diag(\hat{P})$ and
$\hat{P}=X(X'X)^{-1}X'$
$\hat{\epsilon}=y-X\hat{\beta}=y-X(X'X)^{-1}X'y=y-\hat{P}y$
$\hat{P}y=X(X'X)^{-1}X'y=y-(y-X(X'X)^{-1}X'y)=y-\hat{\epsilon}=\hat{y}$
```{r}
Ehat <- Y - X%*% Bhat
## Ehat
## resid(reg)

Pmat <- X%*%XtXi%*%t(X)
Yhat <- Pmat%*%Y
## Yhat
## predict(reg)
```

```{r}
# Sall, J. (1990) Leverage plots for general linear hypotheses. American Statistician *44*, 308-315.
# car::leveragePlots(reg)
```

(Welsch and Kuh. 1977; Belsley, Kuh, and Welsch. 1980) attempt to summarize the information in the leverage versus residual-squared plot into one DFITS statistic where $DFITS > 2\sqrt{{k}/{n}}$ should be examined. 
$$
\text{DFITS}_i=r_i\sqrt{\frac{h_i}{1-h_i}}\\
$$

See also "dfbetas" and "covratio"
```{r}
#dfbetas(reg)
#dffits(reg)
#covratio(reg)
#hatvalues(reg)
head(influence.measures(reg)$infmat)
```

#### Data Scientism

Measurement Error

https://www.aeaweb.org/articles?id=10.1257/aer.p20171031

https://www.r-bloggers.com/2024/09/stepwise-selection-of-variables-in-regression-is-evil-by-ellis2013nz/

https://www.tandfonline.com/doi/full/10.1080/26939169.2023.2276446#d1e1498

Statistics for Public Policy: A Practical Guide to Being Mostly Right (or at Least Respectably Wrong)


Local Moran’s I maps "hot spots" and "cold spots" --- areas with strong positive or negative spatial correlation. High positive/negative values mean similar values cluster/anti-cluster.
```{r}
# Local Autocorrelation
rast_moran <- autocor(luxembourg_elevation_raster, method='moran', global=F)
colmap <- colorRampPalette(colors = c("darkblue", "lightgrey", "darkred"), bias=2.5)
plot(rast_moran,col=colmap(100))
```

