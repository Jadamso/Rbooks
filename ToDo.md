# To Do

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


## R Programming

Make plots interactive via https://plotly-r.com/


#### Statistics 

```{r}
twosam <- function(y1, y2){
    n1  <- length(y1)
    n2  <- length(y2)
    yb1 <- mean(y1)
    yb2 <- mean(y2)
    s1  <- var(y1)
    s2  <- var(y2)
    s   <- ((n1-1)*s1 + (n2-1)*s2)/(n1+n2-2)
    tst <- (yb1-yb2)/sqrt(s*(1/n1+1/n2))
    return(tst)
}
 
tstat <- twosam(data$male, data$female); tstat
```



#### Data Analysis

Add styling to interactive plots


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





## Linear Regression


library(AER)
data(CASchools)
CASchools$score <- (CASchools$read + CASchools$math) / 2)
reg <- lm(score ~ income, data = CASchools)
hvec <- lm.influence(reg)$hat
iplot <- car::influencePlot(reg)
CASchools[rownames(iplot),]


Section 7: Derive Simple OLS

* "Introduction to Econometrics with R" by Hanck, Arnold, Gerber, and Schmelzer, https://www.econometrics-with-r.org/
(taking seriously Greene's "Model Building--A General to Simple Strategy")


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



## Intermediate R

For and while loops


showDot = function(...){
  dots = list(...)
  print(dots)
}
showDot(arg1 = 1:5, "test stuff", 
        b = "another", list(test_still = 2))
        
Add Fortran Code, https://masuday.github.io/fortran_tutorial/r.html

Update packages after new install, 
    for loop checks for old packages and installs if not already installed. not from source

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

<!--for more dimesniosn-->

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



