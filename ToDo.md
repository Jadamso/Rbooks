# To Do

## Quarto/Bookdown
***

#### Big Picture Tasks

1. Increase Depth
 * Provide simple numerical examples for every mathematical expression
 * Add more integrated examples, especially business related
 * Each chapter ends with 3 questions
2. Ease Digestion
 * Add "definition" callouts to Univariate Data. Definitions are in italics, not quotes or bold, and capitalized.
 * Add callouts to other parts
 * Add code annotation in first chapter.
3. Add supplementary materials
 * Create slides
 * Create exam questions, TA review questions
4. Writing
 * Update the writing
 * Update references/bibliography
 * Hyperlinks are valid
 * Clean up all figures (axes, titles, legends, ...)
 * Consistent chapter/section title, subsection, paragraph style.
5. Refine the core content
 * Add content (another chapter to the last part)
6. Workflow optimization?
 * Publish using `gh-pages` branch to resolve compilation warning related to YAML file (output-dir: ../docs)



#### Timeline

Target 1: 4 Months (December)
    * Setup Rbooks-companion github repo
    * Add numerical examples, integrated questions, and slides for Part I.
    * Additional practice questions for weekly tutorials

Target 2: 8 Months (April)
    * Refine existing materials on Rbooks-companion
    * Add new materials to Rbooks-companion Part I
    * Add content to Part II.

Target 3: 12 months
    * Refine existing companion materials and start refining the textbook itself
    * Ensure consistent style for definitions, italics, etc. for all Parts.
    * Harmonize R code across the book.
    * Create a draft bank of exam questions

Target 4: 16 Months
    * Check and update references/bibliography for Parts I–II.
    * Add student handout and exercises for coding and other materials

Target 5+: 36 Months
    * Work shifts to shaping the textbook itself (new chapters, full integration)
    * Refine the ToDo list together and complete it


#### Markdown/Github (Specifics)


Better integrate students with https://web.hypothes.is/hypothesis-for-faculty-instructors/

Callouts

* Must Know ::: {.callout-tip icon=false collapse="true"}
* Test Yourself ::: {.callout-note icon=false collapse="true"}

* ::: {.callout-warning icon=false collapse="true"}
* ::: {.callout-important, icon=false collapse="true"}


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



#### Add Other Datasets in StatsII:

* builtin "datasets" package: USPersonalExpenditure, LifeCycleSavings, EuStockMarkets, JohnsonJohnson, freeny, longley, occupationalStatus, uspop
* use additional package like "AER", "Ecdat", "wooldridge", "causaldata" "np".
* API's from the UScensus or worldbank, especially for sampling examples
* See the list by https://vincentarelbundock.github.io/Rdatasets/datasets.html
* https://pages.stern.nyu.edu/~wgreene/Text/Edition7/tablelist8new.htm
* https://www.ssc.wisc.edu/~bhansen/econometrics/Econometrics%20Data.zip










## Univariate Data
***
(Formerly part of Introduction to Data Analysis)

* Highlight definitions via markdown, alongside italics
* Add sampling distributions for proportions 
* Update one-sided intervals
* Update notation? Estimator/estimate $X_{i}/x_{i}, \bar{X}/\bar{x}$ 

#### Ch 0.
Syllabus, Refresher (Highschool Background, on your own time)

#### Ch 2. Programming and Math
* Define what functions are and provide examples (numerical and visual)
    - https://r02pro.github.io/functions.html
* New 2.2 with logic (and, or) and counting (choose). Both concrete and computational examples.
    - Suppose license plates use the format AB1 23C, where each of the first two digits can be any one of 26 letters and each of the next three digits can be one of 10 numbers, and the last digit can be one of 26 letters. How many possible license plate numbers can be generated if no letter or number can be used twice?
    - Suppose that, from a population of 20 bank accounts, we want to take a random sample of three accounts in order to learn about the population. In this case, the order of selection doesn’t matter. How many different random samples of three accounts are possible? 
    - The HR committee is about to have a busy day. In the morning, the committee plans to choose 2 employees (out of a set of 25 employees) for promotion. The first person they select will become a manager, and the second person they choose will become an assistant manager. Moving on to the afternoon, the HR committee intends to make a separate decision by choosing 5 employees (out of a set of 23 employees) for termination. Note that the decisions made in the morning and afternoon are independent of one another. How many possible outcomes are there for the HR committee’s overall decisions throughout the day?

#### Ch 4. Numerical Statistics
* https://www.khanacademy.org/math/mappers/statistics-and-probability-220-223

#### Ch 6. Random Variables
* https://www.khanacademy.org/math/mappers/statistics-and-probability-192-202
* Further show how F(x) comes from f(x), and vice versa.

#### Ch 7. Statistical Theory

* Bootstrap Jackknife theory (iid)
* Value of new data for Bootstrap?


1. A fitness tracker manufacturer claims that users take more than 8,000 steps per day on average. 
A sample of 25 users has mean = 8,492 steps, and a standard deviation = 1,200 steps. Test at the 5% level, using theory-based intervals and showing your work.
a) state the Hypotheses
b) Calculate the test statistic 
c) Do you reject the null Hypothesis?
d) Fully state your conclusion

#### Ch 8. Intervals
* Fail to reject the null. Examples with multiple hypothesis: can't rule out A, also can't rule out B.

#### Ch.9 p-values
* 8.2. h-tests for mode?

#### Ch.10 Misc Univariate Topics

* [The Box-Cox Transformation Technique: A Review](https://www.jstor.org/stable/2348250)

* Probability Integral Transform
- https://blogs.sas.com/content/iml/2024/05/13/p-values-under-null.html

Inequalities
* 68–95–99.7_rule
* Samuelsons_inequality
* Chebyshevs_inequality


## Bivariate Data (Stats II)
***
(Formerly part of Introduction to Data Analysis)

#### Ch 10. Bivariate Distributions
More examples
* Suppose you read that Honda Civic is the most commonly stolen car. Does this mean that Honda Civic cars have a higher probability to be stolen compared to other cars?
* other examples from Microeconometrics (Simpsons paradox)



#### Ch 11. Bivariate Statistics

#### Ch 12. 

* Eliminate twosamples package dependency


#### Ch 13. Simple Regression

* Add a manual calculation of regression coefficient as callout-note
* Add manual calculation of R squared as callout-note
* P-value as callout-tip 

* "Introduction to Econometrics with R" by Hanck, Arnold, Gerber, and Schmelzer, https://www.econometrics-with-r.org/
(taking seriously Greene's "Model Building--A General to Simple Strategy")

https://openstax.org/books/introductory-statistics-2e/pages/12-1-linear-equations


#### Ch 14. Local Regression
Use wage-education example repeatedly
Others go as callout-tip examples.

#### Ch 15. Data Analysis
* Incorporate insights from "Statistics for Public Policy: A Practical Guide to Being Mostly Right (or at Least Respectably Wrong)" 

Add styling to interactive plots

Data clean/merge
 * by, with, subset, stack, switch
 * do.call, reduce

* https://onlinelibrary.wiley.com/doi/10.1002/%28SICI%291099-1255%28199709/10%2912%3A5%3C533%3A%3AAID-JAE454%3E3.0.CO%3B2-V


https://statmodeling.stat.columbia.edu/2025/10/21/reanalysis-of-that-nobel-prizewinning-study-of-patents-and-innovation/


#### Ch.16. Misc Topics
* https://www.tandfonline.com/doi/abs/10.1198/000313008X332421
* Advanced probability theory?
* Type I vs II errors. Power analysis
Measurement Error

Data Transformation
    Correction for Bias Introduced by a Transformation of Variables
    https://www.explainxkcd.com/wiki/index.php/2048:_Curve-Fitting
    Measurement Error
    Smearing?



## Multivariate Data (Econometrics)
***
(Formerly Introduction to Linear Regression)

## 17 Multivariate Regs I
ANOVA
    https://bookdown.org/mike/data_analysis/sec-experimental-design.html
    https://rpubs.com/odenipinedo/experimental-design-in-R
    https://bookdown.org/gerhard_krennrich/doe_and_optimization/doe2.html
    https://michael-franke.github.io/intro-data-analysis/Chap-02-01-data-exp-design.html
    https://bookdown.org/jgscott/DSGI/experiments.html
    https://designexptr.org/


Adjusted R2 (add to 10.4)
    https://davegiles.blogspot.com/2013/10/in-what-sense-is-adjusted-r-squared.html
    https://stats.stackexchange.com/questions/130069/what-is-the-distribution-of-r2-in-linear-regression-under-the-null-hypothesis
    Rencher, A. C., & Schaalje, G. B. (2008). Linear Models in Statistics (2nd ed.). Wiley. Chapter 5 (“The General Linear Model”), Section 5.6.2 (“Distribution of R2 under the Null Hypothesis”), which shows that under the null (all slopes zero) and Gaussian errors,

    https://statmodeling.stat.columbia.edu/2024/06/17/this-well-known-paradox-of-r-squared-is-still-buggin-me-can-you-help-me-out/


## 18. Multivariate Regs II
12.5 Diagnostics
    https://book.stat420.org/model-diagnostics.html
12.6 Transformations
12.7 Regressograms
12.8 Locally Linear
12.9 Gradient Summaries, GoF

## 19: Observational Data
13.1 Temporal Interdependence
    Plots
        https://plotly.com/r/time-series/#time-series-with-range-slider
        (https://rstudio.github.io/dygraphs/)
        https://vlyubchich.github.io/tsar/l02_tsintro.html
        https://vlyubchich.github.io/tsar/l03_smoothing.html
        https://otexts.com/fpp3/graphics.html
        https://otexts.com/fpp3/expsmooth.html
    Stationary vs. Nonstationary
    Measures of temporal association: ACF, CCF
13.2 Spatial Interdependence
    Plots
    Stationary vs. Nonstationary
    Measures of spatial association: ACF, CCF
13.3 Endogeneity Issues Overview
13.4 Historical Event Studies
    Caution! Causal interpretation rests on many assumptions. Often including spatial and temporal Independence.

https://www.tandfonline.com/doi/full/10.1080/10618600.2022.2104290#d1e315

## 20 Laboratory Experiments

14.1 Experimental Designs
    Completely Randomized Designs
    Factorial Design
    Randomized Block Design 
    Crossover Design
 
14.2 Sampling
    Simple Random Sampling
    Balanced Sampling
    Stratified Sampling
    Cluster Sampling
    Convenience Sampling
    Poisson Sampling

## 22. Misc Topics
16.4 Decision Theory
16.5 Quality Control
16.6 Optimal Designs

**Interpretation**
https://easystats.github.io/report/






----------------
#### Big Picture

* Add some theory about adjusted R2 and F-test to 11.4
* Ch.12 https://plotly.com/r/splom/
* Complete 15.1 (Experimental Design)
* Add semi-formal treatment of "Multiple Hypothesis Testing" to 16.1
* Complete Misc Topics. On the page and also
 * Description vs. Inference vs. Prediction -  See also <https://online.stat.psu.edu/stat200/lesson/4/4.4/4.4.2>.
 * ?CLT breaks down with strong dependence?
 * Differences in Quantiles, Quantiles of Differences
 * Model Selection, J test, Model Combination
* Add interactive plots via https://plotly-r.com/


* update CCFS in "Observational Data" to use `npSDA`

https://www.tandfonline.com/doi/pdf/10.1080/01621459.2021.1938081


find . -maxdepth 1 -type f -exec grep '[A-Za-z0-9]\$[A-Za-z0-9]' {} +


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


**Quantile Results**.{-}

#### Data Scientism

https://www.aeaweb.org/conference/2017/preliminary/paper/2BhG4nbH
https://en.wikipedia.org/wiki/Multiple_comparisons_problem
https://peerj.com/preprints/26605v1/
https://www.nature.com/articles/nmeth.3741
https://www.tandfonline.com/doi/abs/10.1198/000313006X152649

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


#### Misc Topics 
* J-Test, https://bookdown.org/mike/data_analysis/non-nested-model-tests.html#sec-davidson--mackinnon-j-test


This differs from a *pointwise inclusion frequency interval*
```{r}
# Frequency each point was in an interval
bks <- seq(0,1,by=.01)
xcovr <- vector(length=length(bks))
for(b in seq(xcovr)){
    bl <- b >= xq[1,]
    bu <- b <= xq[2,]
    xcovr[b] <- mean( bl & bu )
}
# 50\% Coverage
c_ul <- range(bks[xcovr>=.5])
c_ul # 50% confidence interval

plot.new()
plot.window(xlim=c(0,1), ylim=c(0,1))
polygon( c(bks, rev(bks)), c(xcovr, xcovr*0), col=grey(.5,.5), border=NA)
mtext('Frequency each value was in an interval',2, line=2.5)
axis(1)
axis(2)
abline(h=.5, lwd=2)
segments(c_ul,0,c_ul,.5, lty=2)
```



Assume the tail part of a plane has the same surface area as the wings. During WWII, the designers of planes needed to know which parts of a plane to reinforce. They could not reinforce the entire plane, or it would become heavy and slow. They looked at planes that returned from the battle with bullet damage, and noticed that most of these planes had bullet holes in the tail part of the plane. Does this mean that the tail part of the plane should be reinforced?























<details>
<summary> Advanced and Optional </summary>
A right tail test that "imposes the null" uses the interval $(-\infty, q_{0.95}]$, where $q_{0.95}$ is the $95^{\text{th}}$ percentile of the null bootstrap distribution: If the observed value falls inside that interval, then we fail to reject the null (at the $5\%$ level), otherwise we reject the null (it seems extremely unlikely that we would find such a small value). A left tail test that "imposes the null" uses the interval $[q_{0.05}, \infty)$, where $q_{0.05}$ is the $5^{\text{th}}$ percentile of the null bootstrap distribution. Referring to the hypothetical value generally as $\mu_0$ instead of the particular number $9$, we can summarize the one-sided decision rules as

| | Tail | Reject when | Fail to reject when |
| --- | --- | --- | --- |
| **Impose the Null**<br>(shifted/bootstrap-null) | *Right-tail*<br> $H_A: \mu > \mu_0$ | $\hat{M} > q^{\text{null}}_{0.95}$ | $\hat{M} \le q^{\text{null}}_{0.95}$ |
|                                                                  | *Left-tail*<br>$H_A: \mu < \mu_0$   | $\hat{M} < q^{\text{null}}_{0.05}$ | $\hat{M} \ge q^{\text{null}}_{0.05}$ |
| **Invert a CI**<br>(percentile CI)               | *Right-tail*<br>$H_A: \mu > \mu_0$  | $\mu_0 < q^{\text{boot}}_{0.05}$   | $\mu_0 \ge q^{\text{boot}}_{0.05}$   |
|                                                                  | *Left-tail*<br> $H_A: \mu < \mu_0$  | $\mu_0 > q^{\text{boot}}_{0.95}$   | $\mu_0 \le q^{\text{boot}}_{0.95}$  |
  </p>
</details>


