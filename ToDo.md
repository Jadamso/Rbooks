# To Do

Add title page

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

## OLS

Predictions and Projection Matrix
$$
\hat{\epsilon}=y-X\hat{\beta}=y-X(X'X)^{-1}X'y\\
\hat{P}=X(X'X)^{-1}X'\\
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


For OLS, we calculate a Leverage Vector: Distance within explanatory variables
$$
H = diag(\hat{P}) = [h_{1}, h_{2}, ...., h_{N}]\\
\hat{P} = X(X'X)^{-1}X'
$$
$h_i$ is the leverage of residual $\hat{\epsilon_i}$

Studentized residuals
$$
r_i=\frac{\hat{\epsilon}_i}{s_{[i]}\sqrt{1-h_i}}
$$
and $s_{(i)}$ the root mean squared error of a regression with the $i$th observation removed.
Cook's Distance is defined as the sum of all the changes in the regression model when observation i is removed from.
$$
D_{i} = \frac{\sum_{j} \left( \hat{y_j} - \hat{y_j}_{[i]} \right)^2 }{ p s^2 }
= \frac{[e_{i}]^2}{p s^2 } \frac{h_i}{(1-h_i)^2}\\
s^2 = \frac{\sum_{i} (e_{i})^2 }{n-K}
$$

<<application_OLS, echo=FALSE, cache=FALSE, fig.keep='none', eval=FALSE>>=
library(AER)
data(CASchools)
CASchools$score <- (CASchools$read + CASchools$math) / 2)
reg <- lm(score ~ income, data = CASchools)
hvec <- lm.influence(reg)$hat
iplot <- car::influencePlot(reg)
CASchools[rownames(iplot),]
@




### Parametric Variability Estimates and Hypothesis Tests [Under Construction]

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

Autocorrelation Dependance: $\sigma_{i,j}=f( dist(i,j) )$.

Cluster Dependance: 
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



## Intro R
The & and | operators
    always evaluate left and right
    vectorised
The && and || operators
    they evaluate the right side only if needed (i.e. conditionally)
    they accept only scalars on both sides!
x <- 1:3
if(length(x) >= 5 & x[5] > 12) print("ok")
if(length(x) >= 5& & x[5] > 12) print("ok")
https://meek-parfait-60672c.netlify.app/docs/m1_r-intro_01#103

Data clean/merge
 * by, with, subset, split, aggregate, stack, switch, do.call, reduce
 * data.table, ...

Strings. https://meek-parfait-60672c.netlify.app/docs/M1_R-intro_03_text.html, https://raw.githubusercontent.com/rstudio/cheatsheets/main/regex.pdf
kingText = "The king infringes the law on playing curling."
gsub(pattern = "ing", replacement = "", x = kingText)
gsub("[aeiouy]", "_", kingText)
gsub("([[:alpha:]]{3,})ing\\b", "\\1", kingText) 

For and while loops


## Intermediate R


showDot = function(...){
  dots = list(...)
  print(dots)
}
showDot(arg1 = 1:5, "test stuff", 
        b = "another", list(test_still = 2))
        
Add Fortran Code, https://masuday.github.io/fortran_tutorial/r.html

Update packages after new install, 
    for loop checks for old packages and installs if not already installed. not from source

## RReproducible

- edit /DataScientism_Poster
- links [RandRstudio](https://jadamso.github.io/Rbooks/01-RandRstudio.md)

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

<!--for more dimesniosn-->

<!--optim-->
<!--```-->

