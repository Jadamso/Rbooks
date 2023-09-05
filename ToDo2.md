

## Competitive Market Equilibrium

You may already be familiar with the term "simultaneity bias", which arises when two variables simultaneously affect one another. Although there are many ways this simultaneity can happen, economic theorists have made great strides in analyzing the simultaneity problem as it arises from market relationships. In fact, the 2SLS statistical approach arose to understand the equilibrium of a single competitive market, which has three structural equations: (1) market supply is the sum of quantities supplied by individual firms, (2) market demand is the sum of quantities demanded by individual people, (3) market supply equals market demand.
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


It becomes clear that even in the linear model that all effects are conditional: *The* effect of a cost change on quantity or price depends on the demand curve. A change in costs affects quantity supplied but not quantity demanded (which then affects equilibrium price) but the demand side of the market still matters! The change in price from a change in costs depends on the elasticity of demand. (Likewise for changes in demand parameters.) 


```{r}
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


```{r}
N <- 1000 ## Number of Simulations

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

## Analyze Market Data
dat1 <- data.frame(t(EQ1), cost='1')
reg1 <- lm(Q~P, data=dat1)
summary(reg1)
```




## Two Stage Least Squares (2SLS)

You can simply run a regression of one variable on another, but you will need much luck to correctly interrupt the resulting number. Consider regressing quantity on price;
\begin{eqnarray}
Q &=& \alpha^{Q} + \beta^{Q} P + \epsilon^{Q} = \alpha^{Q} + \beta^{Q} [\alpha^{P} + \beta^{P} Q + \epsilon^{P}] + \epsilon^{Q} \\
&=& \frac{[\alpha^{Q} +  \epsilon^{Q}] + \beta^{Q} [\alpha^{P} + \epsilon^{P}]}{1-\beta^{P}}
\end{eqnarray}
We can see $Q$ is a function of $\epsilon^{P}$, thus biasing the estimate of $\beta^{P}$. If you were to instead regress $Q$ on $P$, you would similarly get a number that is hard to interpret meaningfully. This simple derivation has a profound insight: price-quantity data does not generally tell you how price affects quantity supplied or demanded (and vice-versa).


If you have exogeneous variation on one side of the market, ``shocks'', you can get information on the other. Experimental manipulation of $A^{S}$ would, for example, allow you to trace out part of a demand curve: 
\begin{eqnarray}
\frac{\partial P^{*}}{\partial A^{S}} = \frac{-1}{B^{D}+B^{S}}, \\
\frac{\partial Q^{*}}{\partial A^{S}} = \frac{B^{D}}{B^{D}+B^{S}}.
\end{eqnarray}
With two equations and two unknowns, we can thus estimate $B^{D}$ and $B^{S}$, which was the original idea behind 2SLS. Substituting the equilibrium condition into the structural demand equation, we can rewrite them as
\begin{eqnarray}
\label{eqn:linear_demand_iv}
P(Q) &=& -\frac{A^{D}}{{B^{D}}} + \frac{Q^{s}}{B^{D}} - \frac{\epsilon^{D}}{B^{D}}  = \alpha^{P} + \beta^{P} Q + \epsilon^{P}\\
\label{eqn:linear_supply_iv}
Q(P) &=&  A^{S}  + \epsilon^{S} +  B^{S} P .
\end{eqnarray}

```{r}
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

plot.new()
plot.window(xlim=c(0,2), ylim=plm)
points(dat2$Q, dat2$P, col=as.numeric(dat2$cost))
axis(1)
axis(2)
mtext('Quantity',1, line=2)
mtext('Price',2, line=2)


## Not exact, at least right sign
reg2 <- lm(Q~P, data=dat2)
summary(reg2)

## FE
library(fixest)
reg2_alt <- feols(Q~1|P~cost, data=dat2)
summary(reg2_alt)

#library(ivreg)
#reg2_alt2 <- ivreg(Q~P|cost, data=dat2)
#summary(reg2_alt2)
```



With multiple linear regression, note that simultaneity bias is not just a problem your main variable. Suppose your interested in how $x_{1}$ affects $y$, conditional on $x_{2}$. Letting $X=[x_{1}, x_{2}]$, you estimate 
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

Note that the coefficient interpretation still rests on many assumptions

* do you know both supply and demand are linear?
* do you know only supply was affected, and it was only an intercept shift?
* is the shock large enough to be picked up statistically

If we had multiple alleged supply shifts and recorded their magnitudes, then we could recover more information about demand. One common diagnostic tool is simply to report the reduced form results, but we could use a nonparametric estimator to diagnose linearity at the same time. 
```{r, eval=F, results='hide'}
#reg2_alt_fs <- lm(Q~cost, data=dat2)
#summary(reg2_alt_fs)
#lo2_alt_fs <- loess(Q~cost, data=dat2)
```

Other tools are used to help address some of the other assumptions.







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




<!--Cleveland, W.S. (1993) Visualizing data, Hobart Press-->
<!--Tufte, E.R. (1983) The visual display of quantitative information, Graphics Press-->


<!-- ## COMPILE FROM CLI
    Rscript -e "rmarkdown::render('RandRstudio.Rmd')"
-->


