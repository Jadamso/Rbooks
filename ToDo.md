# To Do


## Bookdown

Add title page

knitr::include_url("https://sites.google.com/view/jordan-adamson/")

<!--
The compilation instructions are in 'index.Rmd' 
To Create from scratch, use a template ``bookdown::create_gitbook('index.Rmd')``
-->

* https://github.com/bvkrauth/is4e/, https://bookdown.org/bkrauth/IS4E/
* https://github.com/Camilo-Mora/GEO380
* https://github.com/rstudio/bookdown
* https://bookdown.org/pkaldunn/SRM-Textbook/

Github repos must be public to deploy!
https://bookdown.org/yihui/bookdown/github.html


## Basic Statistics

Make plots interactive via https://plotly-r.com/

**Interpretation**
https://easystats.github.io/report/

**Github**
* https://happygitwithr.com/classroom-overview.html
* https://aeturrell.github.io/coding-for-economists/intro.html

Coefficient of colligation



#### Hypothesis Tests 

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


```{r}
t_2sample <- function(x1, x2){
    # Differences between means
    m1 <- mean(x1)
    m2 <- mean(x2)
    d <- (m1-m2)
    
    # SE estimate
    n1  <- length(x1)
    n2  <- length(x2)
    s1  <- var(x1)
    s2  <- var(x2)
    s   <- ((n1-1)*s1 + (n2-1)*s2)/(n1+n2-2)
    d_se <- sqrt(s*(1/n1+1/n2))
    
    # t stat
    t_stat <- d/d_se
    return(t_stat)
}
 
tstat <- twosam(data$male, data$female)
tstat
```




#### Endogeneity

```{r}
## Theoretical Relationship
x <- c(-1,1)/2
y <- c(0,0)
plot.new()
plot(x,y, type='n', axes=F, ann=F, xlim=c(-1,1))
s <- seq(length(x)-1)
arrows(x[1], y[1], x[2], y[2], code=2, lwd=2)
text(c(-1,1), y, c("X","Y"), cex=2)
```

```{r}
### Reverse Causation
x <- c(-1,1)/2
y <- c(0,0)
plot(x,y, type='n', axes=F, ann=F, xlim=c(-1,1))
arrows(x[1], y[1], x[2], y[2], code=1, lwd=2)
text(c(-1,1), y, c("X","Y"), cex=2)
```

```{r}
### Lurking/Confounding Variable
x <- c(-1,0,1)/2
y <- c(0,-1,0)/2
plot(x,y, type='n', axes=F, ann=F, xlim=c(-1,1), ylim=c(-1,.2))
arrows(x[1], y[1], x[2], y[2], code=1, lwd=2)
arrows(x[3], y[3], x[2], y[2], code=1, lwd=2)
text(c(-2/3,0,2/3), c(1/5,-2/3,1/5), c("X","Z","Y"), cex=2)
```

*Example 1:* Suppose you want to know how taxes affect economic prosperity.
What are the issue with interpreting an empirical finding that higher $Taxes$ do not affect $GDP$ with data from Canada and Germany? Or across all countries for that matter?

```{r}
x <- c(-1,0,1)/2
y <- c(0,-1,0)/2
plot(x,y, type='n', axes=F, ann=F, xlim=c(-1,1), ylim=c(-1,.25))
arrows(x[1], y[1], x[2]-.1, y[2], code=3, lwd=2)
arrows(x[3], y[3], x[2]+.1, y[2], code=3, lwd=2)
arrows(x[3], y[3]+.2, x[1], y[1]+.2, code=3, lwd=2)
text(c(-2/3,0,2/3), c(1/5,-2/3,1/5), 
    c("Taxes","Culture, Laws, Record Keeping","GDP"), cex=1.3)
```

*Example 2:* What do you think about this plot from (https://ourworldindata.org/grapher/share-of-population-with-cancer-vs-gdp)? Is money the root of all evil; our focus on wealth literally a cancer to society?

*Example 3:* This map of cocaine (https://www.unodc.org/wdr2016/field/1.2.3._Prevalence_cocaine.pdf) usage looks a lot like GDP. Could it be that cocaine causes people to become rich, or rather that people in richer countries use more cocaine?

#### Power Analysis

```{r, eval=F}
# Two-Sided Test, based on theory
# Symmetric Null Distribution: p_upper = 1 - p_upper
# pt( -abs(jack_t), n-1) = 1-pt( abs(jack_t), n-1)
# p <- 2*(1-pt(abs(jack_t), n-1) )
```

https://osf.io/zqphw/download
The Essential Guide to Effect Sizes: Statistical Power, Meta-Analysis, and the Interpretation of Research Results
https://online.stat.psu.edu/statprogram/reviews/statistical-concepts/power-analysis
https://bookdown.org/MathiasHarrer/Doing_Meta_Analysis_in_R/power.html
https://peopleanalytics-regression-book.org/power-tests.html

https://aaroncaldwell.us/SuperpowerBook/



Parametric P values and Power Analysis
```{r}
xy <- USArrests[,c("Murder","UrbanPop")]
colnames(xy) <- c("y","x")

reg <- lm(y~x, dat=xy)

## T-values
b <- coef(reg)
se_b <- sqrt(diag(vcov(reg)))
t_b <- b/se_b

## P-values
k <- reg$df.residual
p <- (1-pt(abs(t_b), k))*2
p <- pt(-t_b, k) + (1-pt(t_b, k))

#PT_r <- pwrss::power.t.test(T_r, df=k, plot=FALSE, alpha=0.05)
PT_r <- 1 -
    pt( qt(alpha/2, df=k), df=k, ncp=abs(T_r), lower.tail=F) +
    pt( qt(alpha/2, df=k, lower.tail=F), df=k, ncp=abs(T_r), lower.tail=F)
1 - pt( qt(1-alpha/2, df=k)-abs(T_r), df=k) + pt( qt(alpha/2, df=k)-abs(T_r), df=k)
```



#### Data Analysis

https://onlinelibrary.wiley.com/doi/10.1002/%28SICI%291099-1255%28199709/10%2912%3A5%3C533%3A%3AAID-JAE454%3E3.0.CO%3B2-V

Add styling to interactive plots

Data clean/merge
 * by, with, subset, stack, switch
 * do.call, reduce
 * data.table, ...



## Multivariate Data


#### GoF
https://statmodeling.stat.columbia.edu/2024/06/17/this-well-known-paradox-of-r-squared-is-still-buggin-me-can-you-help-me-out/


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

Note that we can compute classic estimates for variability: denoting the Standard Error of the Regression as $\hat{\sigma}$, and the Standard Error of the Coefficient Estimates as $\hat{\sigma}_{\hat{\alpha}}$ and $\hat{\sigma}_{\hat{\beta}}~~$ (or simply Standard Errors).
$$
\hat{\sigma}^2 = \frac{1}{n-2}\sum_{i}\hat{\epsilon_{i}}^2\\
\hat{\sigma}^2_{\hat{\alpha}}=\hat{\sigma}^2\left[\frac{1}{n}+\frac{\bar{x}^2}{\sum_{i}(x_i-\bar{x})^2}\right]\\
\hat{\sigma}^2_{\hat{\beta}}=\frac{\hat{\sigma}^2}{\sum_{i}(x_i-\bar{x})^2}.
$$
These equations are motivated by particular data generating proceses, which you can read more about this at https://www.econometrics-with-r.org/4-lrwor.html.]




#### Parametric Variability Estimates and Hypothesis Tests [Under Construction]

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
$$
\hat{P}=X(X'X)^{-1}X'\\
\hat{\epsilon}=y-X\hat{\beta}=y-X(X'X)^{-1}X'y=y-\hat{P}y\\
\hat{P}y=X(X'X)^{-1}X'y=y-(y-X(X'X)^{-1}X'y)=y-\hat{\epsilon}=\hat{y}\\
$$
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




## Intermediate R

For and while loops

```{r}
add2 = function(x, ...){
  y <- x+2
  dots = list(...)
  print(dots)
  return(y)
}
add2(1:4,
    arg1=1:5,
    "test stuff",
    b="another", list(test_still=2))
```

Update packages after new install, 
    for loop checks for old packages and installs if not already installed. not from source


#### Rcpp
https://teuder.github.io/rcpp4everyone_en/
http://adv-r.had.co.nz/Rcpp.html
http://dirk.eddelbuettel.com/code/rcpp.examples.html (https://gallery.rcpp.org/)

```{r}
library(Rcpp)
cppFunction('int add(int x, int y, int z) {
  int sum = x + y + z;
  return sum;
}')
add(1, 2, 3)
```

```{r}
library(Rcpp)
cppFunction('
double rcpp_sum(NumericVector v){
    double sum = 0;
    for(int i=0; i<v.length(); ++i){
        sum += v[i];
    }
    return(sum);
}
')
rcpp_sum(1:3)
```


Random Numbers
https://teuder.github.io/rcpp4everyone_en/220_dpqr_functions.html
https://en.cppreference.com/w/cpp/numeric/random

Particle Filter
https://dirk.eddelbuettel.com/code/rcpp.kalman.html
https://dirk.eddelbuettel.com/code/rcpp.smc.html



#### RReproducible

- fill in /DataScientism_Poster
- default /DataScientism_Slides to `output: ioslides_presentation`
- remove dependance on "reshape2" package in all files
- update links [RandRstudio](https://jadamso.github.io/Rbooks/01-RandRstudio.md)

Add 
 - Screenshot of Rmarkdown
 - How to execute
 
Add Tikz Pictures
https://community.rstudio.com/t/tikz-in-r-markdown-with-html-output/54260/2

```{r}
#install.packages("magick")
#install.packages("pdftools")
```

```{tikz, fig.cap = "Funky tikz", fig.ext = 'png'}
\usetikzlibrary{positioning}
\usetikzlibrary{arrows}
\usetikzlibrary{shapes}

\begin{tikzpicture}[box/.style={draw,rounded corners,text width=2.5cm,align=center}]
\node[box] (a) {Data Folder};
\node[left=of a.170,font=\bfseries] (aux1) {Data Source 1};
\node[left=of a.190,font=\bfseries] (aux2) {Data Source 2};
\node[below=0cm of aux2]{ $\vdots$};
\node[ellipse, below=of a, fill=lightgray, x radius=3.75cm, align=center,  y radius=2cm] (b) { Data Work \\ \{Clean, Analyze, ...\}} ;
\node[box, below=of b, text width=4cm] (c) {Output Folder \\ \{Figures, Tables, ...\} };
\node[right=of c,font=\bfseries] (d) {Final Document};
\draw[->] (aux1) -- (a.170);
\draw[->] (aux2) -- (a.190);
\draw[->] (a) -- (b);
\draw[->] (b) -- (c);
\draw[->] (c) -- (d);
\end{tikzpicture}
```


<!--```{r, error=TRUE}-->
<!--https://cran.r-project.org/web/views/NumericalMathematics.html-->
<!--https://cran.r-project.org/web/views/Optimization.html-->

<!--    integrate() finds the area under the curve defined by f()-->
<!--    uniroot() finds where f() hits zero-->
<!--    optimise() finds the location of the lowest (or highest) value of f()-->

<!--f <- function(x) x^2-->
<!--f1 <- Deriv::Deriv(f)-->

<!--optim-->
<!--```-->




<!--
###  Quantitative Analysis of Almost Any Type of Data} 

E.g., plotting galactic superclusters
\vspace{.5\baselineskip}
\includegraphics[scale=0.25, trim=0 5cm 0 5cm, clip=true]{./Figures/shapley.pdf}
\vspace{-2\baselineskip}

\begin{Rcode}{basicstyle=\tiny\ttfamily}
library(spatstat)
data(shapley)
plot(shapley, pch=16, main="", cols=rgb(0,0,0,.1), cex=.4, use.marks=F)
\end{Rcode}
<<echo=TRUE, cache=FALSE, fig=TRUE, eval=TRUE>>=
library(spatstat)
data(shapley)
plot(shapley, pch=16, main="", cols=rgb(0,0,0,.1), cex=.4, use.marks=F)
@
\vspace{-.5\baselineskip}

\textbf{Physics and Chemistry:}
Particle Simulations, DNA Sequences, Protein Folding\\
\textbf{Biology:} 
Human Brain Morphology, Insect Trajectories  \\
{\footnotesize \texttt{bio3d:} 
\url{http://thegrantlab.org/bio3d/tutorials/structure-analysis} \\
\url{https://ecomorph.wordpress.com/2015/08/05/retinal-topography-maps-in-r/}} \\
\textbf{Astronomy:} Map the Brightness of Galaxy Locations 
{\footnotesize \url{https://asaip.psu.edu/resources/datasets}}
\bash
Rscript -e 'library(spatstat); data(shapley);  pdf("./shapley.pdf"); plot(unmark(shapley), pch=16, main = "", cols=rgb(0,0,0,.1), cex=.4 )'
\END

###  ... To Large Scale Observational Data ...}
{\footnotesize \url{https://cran.r-project.org/web/views/MedicalImaging.html}}
data(brains)
shapes3d(brains$x[,,], type="dots", axes3=T)  ## 24 markers (x,y,z) for 59 people $

\textbf{Social and Historical:} Income, Population, Crime, ... \\
i.e. \footnotesize{\url{http://www.census.gov/did/www/saipe/data/statecounty/maps/iy2014/Tot_Pct_Poor2014.pdf}} \\
i.e. \footnotesize{\url{http://lincolnmullen.com/projects/slavery/}}\\~\\

\textbf{Ecology:} Global Temperatures, Soil Attributes, Land Use, ...\\
https://benborgy.wordpress.com/
i.e. \footnotesize{\url{https://benborgy.files.wordpress.com/2014/08/spatializemap_2.jpg}} \\
i.e. \footnotesize{\url{http://esdac.jrc.ec.europa.eu/themes/global-data-other-initiatives}} \\
-->
