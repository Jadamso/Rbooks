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
* Show how F(x) comes from f(x), and vice versa.


#### Ch 5. Mean and Standard Deviation
* https://www.khanacademy.org/math/mappers/statistics-and-probability-220-223


#### Ch 6. (Re)Sampling
* Bootstrap Jacknife theory (iid)
* Value of new data for Bootstrap?

#### Ch 7. Hypothesis Tests
* permutation sampling and H-testing

#### Ch 8. Data Analysis
* Incorporate insights from "Statistics for Public Policy: A Practical Guide to Being Mostly Right (or at Least Respectably Wrong)" 

Add styling to interactive plots

Data clean/merge
 * by, with, subset, stack, switch
 * do.call, reduce

* https://onlinelibrary.wiley.com/doi/10.1002/%28SICI%291099-1255%28199709/10%2912%3A5%3C533%3A%3AAID-JAE454%3E3.0.CO%3B2-V

#### Ch.9 Misc Univariate Topics

* [The Box-Cox Transformation Technique: A Review](https://www.jstor.org/stable/2348250)
* ?Fail to reject the null. Example with multiple hypothesis: can't rule out A, also can't rule out B.

* Probability Integral Transform
- https://blogs.sas.com/content/iml/2024/05/13/p-values-under-null.html


* ?Advanced and Compound probability? 
    - Events A: the number on the die is greater than 2. B: the number on the die is even
        a) Find P(A U B) and P(A ∩ B)
        b) Are events A and B independent events? Explain.  
        c) Are events A and B mutually exclusive events?  Explain. 
        d) Find P(A | B)
    -Find the probability of rolling a six-sided die and obtaining an even number less than 5. Use a computer simulation to suggest an answer and then provide the math.
    -Find the probability of rolling a six-sided die and obtaining an odd number or a number less than 5. 
    -Suppose that we have five equally likely experimental outcomes: 1, 2, 3, 4, 5. Find $Prob(X_{i} \in  \{1, 2, 5\}  or X_{i} \in \{1, 3\})$. Find $Prob(X_{i} \in  \{1, 2, 5\} and X_{i} \in \{1, 3\})$.
* Binomial Distribution
* Binomial Limit Theorem
    - The unemployment rate is 10%. Suppose that 100 employable people are selected randomly. What is the probability that this sample contains between 9 and 12 unemployed people. Use the normal approximation to binomial probabilities (parameters mu=100, sigma=9.49).
    - Suppose that employees at a company are 70% female and 30% male. If we select a random sample of eight employees, what is the probability that more than 2 in the sample are female?
* Bates Distribution

* Poisson Limit Theorem
    - use the Poisson approximation to binomial probabilities.



## Bivariate Data (Stats II)
***
(Formerly part of Introduction to Data Analysis)

#### Ch 10. Bivariate Data
* add empirical example of table with joint and marginal distributions

#### Ch 11. Bivariate Statistics
* other examples from Microeconometrics (Simpsons paradox)
* 10.4 Hypothesis Tests
* Two Sample test tests


#### Ch.12. Hypothesis Testing 
* https://www.tandfonline.com/doi/abs/10.1198/000313008X332421
* Advanced probability theory?
* Type I vs II errors. Power analysis











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
 * Description vs. Inference vs. Prediction
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


