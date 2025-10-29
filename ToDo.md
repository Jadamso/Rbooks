# To Do

## Quarto/Bookdown
***

#### Big Picture Tasks

1. Increase Depth
 * Provide simple numerical examples for every mathematical expression
 * Add integrated questions 
 * Each chapter ends with 3 questions
2. Ease coding
 * Add student callouts 
 * Add code annotation in first chapter.
3. Add supplementary materials
 * Create slides
 * Create exam questions, TA review questions
 * Handout for students to use hypothesis.is (examples and nonexamples)
4. Writing
 * Update the writing
 * Update references/bibliography
 * Hyperlinks are valid
 * Clean up all figures (axes, titles, legends, ...)
 * Definitions are in italics, not quotes or bold, and capitalized. (Maybe they should be colored, or in a callout box?)
 * Chapter/section title, subsection, paragraph style.
5. Refine the core content
 * Split into three parts: univariate, bivariate, multivariate.
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
    * Ensure consistent style for definitions, italics, etc. for both Parts I + II.
    * Create a draft bank of exam questions
    
Target 4: 16 Months
    * Check and update references/bibliography for Parts I–II.
    * Add code annotations in the first coding chapter and harmonize R code across the book.
    * Add student handout and exercises for coding and other materials (e.g., using Hypothesis.is.)

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

#### Ch 0.
Syllabus, Refresher (Highschool Background, on your own time)

#### Ch 2.
* Define what functions are and provide examples (numerical and visual)
    - https://r02pro.github.io/functions.html
* New 2.2 with logic (and, or) and counting (choose). Both concrete and computational examples.
    - Suppose license plates use the format AB1 23C, where each of the first two digits can be any one of 26 letters and each of the next three digits can be one of 10 numbers, and the last digit can be one of 26 letters.  How many possible license plate numbers can be generated if no letter or number can be used twice?
    - Suppose that, from a population of 20 bank accounts, we want to take a random sample of three accounts in order to learn about the population. In this case, the order of selection doesn’t matter. How many different random samples of three accounts are possible? 
    - The HR committee is about to have a busy day. In the morning, the committee plans to choose 2 employees (out of a set of 25 employees) for promotion. The first person they select will become a manager, and the second person they choose will become an assistant manager. Moving on to the afternoon, the HR committee intends to make a separate decision by choosing 5 employees (out of a set of 23 employees) for termination. Note that the decisions made in the morning and afternoon are independent of one another. How many possible outcomes are there for the HR committee’s overall decisions throughout the day?

#### Ch 4. Random Variables
* https://www.khanacademy.org/math/mappers/statistics-and-probability-192-202
* Further show how F(x) comes from f(x), and vice versa.


#### Ch 5. Mean and Standard Deviation
* https://www.khanacademy.org/math/mappers/statistics-and-probability-220-223

#### Ch 6. (Re)Sampling
* Bootstrap Jacknife theory (iid)
* Value of new data for Bootstrap?


#### Ch 7. Hypothesis Tests
* permutation sampling and H-testing

* ?Fail to reject the null. Example with multiple hypothesis: can't rule out A, also can't rule out B.


#### Ch.8 Misc Univariate Topics

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
* add empirical example of table with joint and marginal distributions


Suppose you read that Honda Civic is the most commonly stolen car. Does this mean that Honda Civic cars have a higher probability to be stolen compared to other cars?


#### Ch 11. Bivariate Statistics
* other examples from Microeconometrics (Simpsons paradox)
* 10.4 Hypothesis Tests
* Two Sample test tests


#### Ch.12. Hypothesis Testing 
* https://www.tandfonline.com/doi/abs/10.1198/000313008X332421
* Advanced probability theory?
* Type I vs II errors. Power analysis




When we test a hypothesis, we start with a claim called the null hypothesis $H_0$ and an alternative claim $H_A$. Because we base conclusions on sample data, which has variability, mistakes are possible. There are two types of errors:

* *Type I Error*: Rejecting a true null hypothesis. (False Positive). 
* *Type II Error*: Failing to reject a false null hypothesis (False Negative). 

| **True Situation** | **Decision: Fail to Reject $H_0$** | **Decision: Reject $H_0$** |
|---|---|---|
| $H_0$ is true |  Correct (no detection)  |  **Type I Error** (false positive) |
| $H_0$ is false |  **Type II Error** (false negative; missed detection) | Correct (effect detected) |

Here is a Courtroom Analogy. Someone at trial is either guilty or not (a Bernoulli random variable), and you hypothesize that they are innocent.

| **Reality** | **Court’s Decision** | **Interpretation** |
|---|---|---|
| Innocent | Convicted | **Type I Error** (false positive) |
| Guilty   | Freed     | **Type II Error** (false negative) |


The probability of Type I Error is called *significance level* and denoted by $Prob(\text{Type I Error}) = \alpha$. The probability of correctly rejecting a false null is called *power* and denoted by $\text{Power} = 1 - \beta = 1 -  Prob(\text{Type II Error})$. 

Significance is often chosen by statistical analysts to be $ \alpha = 0.05 $.
Power is less often chosen, instead following from a decision about power. There is an important Trade-off for fixed sample sizes: Increasing significance (fewer false positive) often lowers power (more false negatives). Generally, power depends on the effect size and sample size: bigger true effects and larger $n$ make it easier to detect real differences (higher power, lower $\beta$).

:::
The code below runs a small simulation for a two-sided z-test of a mean with known $\sigma$. It shows how power increases when the effect size $(\mu - \mu_0)/\sigma$ or sample size $n$ increases.

```{r power-sim}
#"Power vs. Sample Size and Effect Size"
set.seed(1)

power_sim <- function(n = 25, mu = 0.2, mu0 = 0, sigma = 1, alpha = 0.05, reps = 5000){
    zcrit <- qnorm(1 - alpha/2)
    rejections <- vector(length=1000)
    for(i in 1:length(rejections)) {
        xbar <- mean(rnorm(n, mean = mu, sd = sigma))
        z <- sqrt(n) * (xbar - mu0) / sigma
        rejections[i] <- abs(z) > zcrit
    }
    mean(rejections)
}

grid <- expand.grid(n = c(20, 50, 100),
                    effect = c(0.1, 0.2, 0.4))  # effect = (mu - mu0)/sigma
grid$power <- mapply(function(n, eff) power_sim(n = n, mu = eff, mu0 = 0, sigma = 1),
                     grid$n, grid$effect)

grid
```
:::



#### Ch 13. Data Analysis
* Incorporate insights from "Statistics for Public Policy: A Practical Guide to Being Mostly Right (or at Least Respectably Wrong)" 

Add styling to interactive plots

Data clean/merge
 * by, with, subset, stack, switch
 * do.call, reduce

* https://onlinelibrary.wiley.com/doi/10.1002/%28SICI%291099-1255%28199709/10%2912%3A5%3C533%3A%3AAID-JAE454%3E3.0.CO%3B2-V





## Multivariate Data (Econometrics)
***
(Formerly Introduction to Linear Regression)


#### Big Picture

Main gaps are Experimental Design Basics (15.1) and Statistical Decision Theory (17.3)

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





#### Derive Simple OLS

* "Introduction to Econometrics with R" by Hanck, Arnold, Gerber, and Schmelzer, https://www.econometrics-with-r.org/
(taking seriously Greene's "Model Building--A General to Simple Strategy")





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



#### Adjusted R2 (add to 10.4)
https://davegiles.blogspot.com/2013/10/in-what-sense-is-adjusted-r-squared.html
https://stats.stackexchange.com/questions/130069/what-is-the-distribution-of-r2-in-linear-regression-under-the-null-hypothesis
Rencher, A. C., & Schaalje, G. B. (2008). Linear Models in Statistics (2nd ed.). Wiley. Chapter 5 (“The General Linear Model”), Section 5.6.2 (“Distribution of R2 under the Null Hypothesis”), which shows that under the null (all slopes zero) and Gaussian errors,

https://statmodeling.stat.columbia.edu/2024/06/17/this-well-known-paradox-of-r-squared-is-still-buggin-me-can-you-help-me-out/


**Interpretation**
https://easystats.github.io/report/




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

#### Data Transformation

Correction for Bias Introduced by a Transformation of Variables
https://www.explainxkcd.com/wiki/index.php/2048:_Curve-Fitting
Measurement Error
Smearing?

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



Assume the tail part of a plane has the same surface area as the wings. During WWII, the designers of planes needed to know which parts of  a plane to reinforce.  They could not reinforce the entire plane, or it would become heavy and slow.  They looked at planes that returned from the battle with bullet damage, and noticed that most of these planes had bullet holes in the tail part of the plane. Does this mean that the tail part of the plane should be reinforced?

