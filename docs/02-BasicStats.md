# (PART) Data Analysis in R {-}



# First Steps
***

## Why Program in R?

You should program your statistical analysis, and we will cover some of the basics of how to do this in R. You also want your work to be replicable

* *Replicable*: someone collecting new data comes to the same results.
* *Reproducibile*: someone reusing your data comes to the same results.

You can read more about the distinction in many places, including

* https://www.annualreviews.org/doi/10.1146/annurev-psych-020821-114157
* https://nceas.github.io/sasap-training/materials/reproducible_research_in_r_fairbanks/

We focus on R because it is good for complex stats, concise figures, and coherent organization. It is built and developed by applied statisticians for statistics, and used by many in academia and industry. For students, think about labor demand and what may be good for getting a job. Do some of your own research to best understand how much to invest.


My main sell to you is that being reproducible is in your own self-interest.

#### **An example workflow**. {-}

**First Steps...**

*Step 1:* Some ideas and data about how variable $X_{1}$ affects $Y_{1}$

* You copy some data into a spreadsheet, manually aggregate
* do some calculations and tables the same spreadsheet
* some other analysis from here and there, using this software and that.

*Step 2:* Pursuing the lead for a week or two

* you extend your dataset with more observations
* copy in a spreadsheet data, manually aggregate
* do some more calculations and tables, same as before

**A Little Way Down the Road ...**

*1 month later*, someone asks about another factor: $X_{2}$

* you download some other type of data
* You repeat <u>Step 2</u> with some data on $X_{2}$.
* The details from your "point and click" method are a bit fuzzy.
* It takes a little time, but you successfully redo the analysis.

*4 months later*, someone asks about another factor: $X_{3}\to Y_{1}$

* You again repeat <u>Step 2</u> with some data on $X_{3}$.
* You're pretty sure none of tables your tried messed up the order of the rows or columns.
* It takes more time and effort. The data processing was not transparent, but you eventually redo the analysis.

*6 months later*, you want to explore: $X_{2} \to Y_{2}$.

* You found out Excel had some bugs in it's statistical calculations (see e.g., https://biostat.app.vumc.org/wiki/pub/Main/TheresaScott/StatsInExcel.TAScot.handout.pdf). You now use a new version of the spreadsheet
* You're not sure you merged everything correctly. After much time and effort, most (but not all) of the numbers match exactly.
 

*2 years later*, your boss wants you to replicate: $\{ X_{1}, X_{2}, X_{3} \} \to Y_{1}$

* A rival has proposed something new. Their idea doesn't actually make any sense, but their figures and statistics look better.
* You don't even use that computer anymore and a collaborator who handled the data on $X_{2}$ has moved on.


#### **An alternative workflow**. {-}

Suppose you decided to code what you did beginning with Step 2.

*It does not take much time to update or replicate your results*.

* Your computer runs for 2 hours and reproduces the figures and tables.
* You also rewrote your big calculations to use multiple cores, this took two hours to do but saved 6 hours *each time* you rerun your code.
* You add some more data. It adds almost no time to see whether much has changed.

*Your results are transparent and easier to build on*.

* You see the exact steps you took and found an error
  * glad you found it before sending it out! See https://retractionwatch.com/ and https://econjwatch.org/
  * Google "worst excell errors" and note the frequency they arise from copy/paste via the "point-and-click" approach. Future economists should also read https://core.ac.uk/download/pdf/300464894.pdf.
* You try out a new plot you found in *The Visual Display of Quantitative Information*, by Edward Tufte.
  * It's not a standard plot, but google answers most of your questions.
  * Tutorials help avoid bad practices, such as plotting 2D data as a 3D object (see e.g., https://clauswilke.com/dataviz/no-3d.html).
* You try out an obscure statistical approach that's hot in your field.
  * it doesn't make the report, but you have some confidence that candidate issue isn't a big problem


## First Steps

#### Install R {-}

First Install [R](https://cloud.r-project.org/).
Then Install [Rstudio](https://www.rstudio.com/products/rstudio/download/).

For help setting up, see any of the following links

* https://learnr-examples.shinyapps.io/ex-setup-r/
* https://rstudio-education.github.io/hopr/starting.html
* https://a-little-book-of-r-for-bioinformatics.readthedocs.io/en/latest/src/installr.html
* https://cran.r-project.org/doc/manuals/R-admin.html
* https://courses.edx.org/courses/UTAustinX/UT.7.01x/3T2014/56c5437b88fa43cf828bff5371c6a924/
* https://owi.usgs.gov/R/training-curriculum/installr/
* https://www.earthdatascience.org/courses/earth-analytics/document-your-science/setup-r-rstudio/

For Fedora users, note that you need to first enable the repo and then install


``` bash
sudo dnf install 'dnf-command(copr)'
sudo dnf copr enable iucar/rstudio
sudo dnf install rstudio-desktop
```


*Make sure you have the latest version of R and Rstudio for class.* If not, then reinstall. 

#### Interfacing with R {-}

Rstudio is easiest to get going with. (There are other GUI's.) There are 4 panes. The top left is where you write and save code

 * Create and save a new `R Script` file *My_First_Script.R*
 * could also use a plain .txt file.

![](./Figures_Manual/Rstudio.svg)<!-- -->

The pane below is where your code is executed. For all following examples, make sure to both execute and store your code.

Note that the coded examples generally have objects, functions, and comments.


## Further Reading

There are many good and free programming materials online.

The most common tasks can be found https://github.com/rstudio/cheatsheets/blob/main/rstudio-ide.pdf

Some of my programming examples originally come from https://r4ds.had.co.nz/ and I recommend https://intro2r.com. I have also used online material from many places over the years, including

* https://cran.r-project.org/doc/manuals/R-intro.html
* R Graphics Cookbook, 2nd edition. Winston Chang. 2021. https://r-graphics.org/
* R for Data Science. H. Wickham and G. Grolemund. 2017. https://r4ds.had.co.nz/index.html
* An Introduction to R. W. N. Venables, D. M. Smith, R Core Team. 2017. https://colinfay.me/intro-to-r/
* Introduction to R for Econometrics. Kieran Marray. https://bookdown.org/kieranmarray/intro_to_r_for_econometrics/
* Wollschläger, D. (2020). Grundlagen der Datenanalyse mit R: eine anwendungsorientierte Einführung. http://www.dwoll.de/rexrepos/
* Spatial Data Science with R: Introduction to R. Robert J. Hijmans. 2021. https://rspatial.org/intr/index.html

What we cover in this primer should be enough to get you going. But there are also many good yet free-online tutorials and courses. 

* https://www.econometrics-with-r.org/1.2-a-very-short-introduction-to-r-and-rstudio.html
* https://rafalab.github.io/dsbook/
* https://moderndive.com/foreword.html
* https://rstudio.cloud/learn/primers/1.2
* https://cran.r-project.org/manuals.html
* https://stats.idre.ucla.edu/stat/data/intro_r/intro_r_interactive_flat.html
* https://cswr.nrhstat.org/app-r


For more on why to program in R, see

* http://www.r-bloggers.com/the-reproducibility-crisis-in-science-and-prospects-for-r/
* http://fmwww.bc.edu/GStat/docs/pointclick.html
* https://github.com/qinwf/awesome-R\#reproducible-research
* A Guide to Reproducible Code in Ecology and Evolution
* https://biostat.app.vumc.org/wiki/pub/Main/TheresaScott/ReproducibleResearch.TAScott.handout.pdf



# Mathematics
***


## Objects

Vectors are probably your most common mathematical objects, which nest scalars as a special case. 

#### **Scalars**. {-}

Make your first scalar

``` r
xs <- 2 # Make your first scalar
xs  # Print the scalar
## [1] 2
```

Perform simple calculations

``` r
(xs+1)^2 # Perform and print a simple calculation
## [1] 9
xs + NA # often used for missing values
## [1] NA
xs*2
## [1] 4
```

#### **Vectors**. {-}

Make Your First Vector

``` r
x <- c(0,1,3,10,6) # Your First Vector
x # Print the vector
## [1]  0  1  3 10  6
x[2] # Print the 2nd Element; 1
## [1] 1
x+2 # Print simple calculation; 2,3,5,8,12
## [1]  2  3  5 12  8
x*2
## [1]  0  2  6 20 12
x^2
## [1]   0   1   9 100  36
```

Apply Mathematical calculations "elementwise"

``` r
x+x
## [1]  0  2  6 20 12
x*x
## [1]   0   1   9 100  36
x^x
## [1] 1.0000e+00 1.0000e+00 2.7000e+01 1.0000e+10 4.6656e+04
```

See that scalars are vectors

``` r
c(1)
## [1] 1

1:7
## [1] 1 2 3 4 5 6 7
seq(0,1,by=.1)
##  [1] 0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0
```


#### **Matrices**. {-}

Matrices are also common objects

``` r
x1 <- c(1,4,9)
x2 <- c(3,0,2)
x_mat <- rbind(x1, x2)

x_mat       # Print full matrix
##    [,1] [,2] [,3]
## x1    1    4    9
## x2    3    0    2
x_mat[2,]   # Print Second Row
## [1] 3 0 2
x_mat[,2]   # Print Second Column
## x1 x2 
##  4  0
x_mat[2,2]  # Print Element in Second Column and Second Row
## x2 
##  0
```

There are elementwise calculations

``` r
x_mat+2
##    [,1] [,2] [,3]
## x1    3    6   11
## x2    5    2    4
x_mat*2
##    [,1] [,2] [,3]
## x1    2    8   18
## x2    6    0    4
x_mat^2
##    [,1] [,2] [,3]
## x1    1   16   81
## x2    9    0    4

x_mat + x_mat
##    [,1] [,2] [,3]
## x1    2    8   18
## x2    6    0    4
x_mat*x_mat
##    [,1] [,2] [,3]
## x1    1   16   81
## x2    9    0    4
x_mat^x_mat
##    [,1] [,2]      [,3]
## x1    1  256 387420489
## x2   27    1         4
```

And you can also use matrix algebra

``` r
x_mat1 <- matrix(2:7,2,3)
x_mat1
##      [,1] [,2] [,3]
## [1,]    2    4    6
## [2,]    3    5    7

x_mat2 <- matrix(4:-1,2,3)
x_mat2
##      [,1] [,2] [,3]
## [1,]    4    2    0
## [2,]    3    1   -1

tcrossprod(x_mat1, x_mat2) #x_mat1 %*% t(x_mat2)
##      [,1] [,2]
## [1,]   16    4
## [2,]   22    7

crossprod(x_mat1, x_mat2)
##      [,1] [,2] [,3]
## [1,]   17    7   -3
## [2,]   31   13   -5
## [3,]   45   19   -7
# x_mat1 * x_mat2
```


##  Functions

Functions are applied to objects

``` r
# Define a function that adds two to any vector
add_2 <- function(input_vector) {
    output_vector <- input_vector + 2 # new object defined locally 
    return(output_vector) # return new object 
}
# Apply that function to a vector
x <- c(0,1,3,10,6)
add_2(x)
## [1]  2  3  5 12  8

# notice 'output_vector' is not available here
```

There are many many generalizations

``` r
add_vec <- function(input_vector1, input_vector2) {
    output_vector <- input_vector1 + input_vector2
    return(output_vector)
}
add_vec(x,3)
## [1]  3  4  6 13  9
add_vec(x,x)
## [1]  0  2  6 20 12

sum_squared <- function(x1, x2) {
    y <- (x1 + x2)^2
    return(y)
}

sum_squared(1, 3)
## [1] 16
sum_squared(x, 2)
## [1]   4   9  25 144  64
sum_squared(x, NA) 
## [1] NA NA NA NA NA
sum_squared(x, x)
## [1]   0   4  36 400 144
sum_squared(x, 2*x)
## [1]   0   9  81 900 324
```

Functions can take functions as arguments

``` r
fun_of_seq <- function(f){
    x <- seq(1,3, length.out=12)
    y <- f(x)
    return(y)
}

fun_of_seq(mean)
## [1] 2

fun_of_seq(sd)
## [1] 0.6555548
```

You can apply functions to matrices

``` r
sum_squared(x_mat, x_mat)
##    [,1] [,2] [,3]
## x1    4   64  324
## x2   36    0   16

# Apply function to each matrix row
y <- apply(x_mat, 1, sum)^2 
# ?apply  #checks the function details
y - sum_squared(x, x) # tests if there are any differences
## [1]  196   21  160 -375   52
```

There are many possible functions you can apply

``` r
# Return Y-value with minimum absolute difference from 3
abs_diff_y <- abs( y - 3 ) 
abs_diff_y # is this the luckiest number?
##  x1  x2 
## 193  22

#min(abs_diff_y)
#which.min(abs_diff_y)
y[ which.min(abs_diff_y) ]
## x2 
## 25
```

There are also some useful built in functions

``` r
m <- matrix(c(1:3,2*(1:3)),byrow=TRUE,ncol=3)
m
##      [,1] [,2] [,3]
## [1,]    1    2    3
## [2,]    2    4    6

# normalize rows
m/rowSums(m)
##           [,1]      [,2] [,3]
## [1,] 0.1666667 0.3333333  0.5
## [2,] 0.1666667 0.3333333  0.5

# normalize columns
t(t(m)/colSums(m))
##           [,1]      [,2]      [,3]
## [1,] 0.3333333 0.3333333 0.3333333
## [2,] 0.6666667 0.6666667 0.6666667

# de-mean rows
sweep(m,1,rowMeans(m), '-')
##      [,1] [,2] [,3]
## [1,]   -1    0    1
## [2,]   -2    0    2

# de-mean columns
sweep(m,2,colMeans(m), '-')
##      [,1] [,2] [,3]
## [1,] -0.5   -1 -1.5
## [2,]  0.5    1  1.5
```


#### **Loops**. {-}

Applying the same function over and over again

``` r
exp_vector <- vector(length=3)
for(i in 1:3){
    exp_vector[i] <- exp(i)
}

# Compare
exp_vector
## [1]  2.718282  7.389056 20.085537
c( exp(1), exp(2), exp(3))
## [1]  2.718282  7.389056 20.085537
```

store complicated example

``` r
complicate_fun <- function(i, j=0){
    x <- i^(i-1)
    y <- x + mean( j:i )
    z <- log(y)/i
    return(z)
}
complicated_vector <- vector(length=10)
for(i in 1:10){
    complicated_vector[i] <- complicate_fun(i)
}
```

recursive loop

``` r
x <- vector(length=4)
x[1] <- 1
for(i in 2:4){
    x[i] <- (x[i-1]+1)^2
}
x
## [1]   1   4  25 676
```

<!---



``` r
# for loop in a function
r_fun <- function(n){
    x <- rep(1,n)
    for(i in 2:length(x) ){
        x[i] <- (x[i-1]+1)^2
    }
    return(x)
}
r_fun(5)
## [1]      1      4     25    676 458329
```
--->


#### **Logic**. {-}

Basic Logic


``` r
x <- c(1,2,3,NA)
x > 2
## [1] FALSE FALSE  TRUE    NA
x==2
## [1] FALSE  TRUE FALSE    NA

any(x==2)
## [1] TRUE
all(x==2)
## [1] FALSE
2 %in% x
## [1] TRUE

is.numeric(x)
## [1] TRUE
is.na(x)
## [1] FALSE FALSE FALSE  TRUE
```

The "&" and "|" commands are logical calculations that compare vectors to the left and right.

``` r
x <- 1:3
is.numeric(x) & (x < 2)
## [1]  TRUE FALSE FALSE
is.numeric(x) | (x < 2)
## [1] TRUE TRUE TRUE

if(length(x) >= 5 & x[5] > 12) print("ok")
```

Advanced Logic.


``` r
x <- 1:10
cut(x, 4)
##  [1] (0.991,3.25] (0.991,3.25] (0.991,3.25] (3.25,5.5]   (3.25,5.5]  
##  [6] (5.5,7.75]   (5.5,7.75]   (7.75,10]    (7.75,10]    (7.75,10]   
## Levels: (0.991,3.25] (3.25,5.5] (5.5,7.75] (7.75,10]
split(x, cut(x, 4))
## $`(0.991,3.25]`
## [1] 1 2 3
## 
## $`(3.25,5.5]`
## [1] 4 5
## 
## $`(5.5,7.75]`
## [1] 6 7
## 
## $`(7.75,10]`
## [1]  8  9 10
```


``` r
xs <- split(x, cut(x, 4))
sapply(xs, mean)
## (0.991,3.25]   (3.25,5.5]   (5.5,7.75]    (7.75,10] 
##          2.0          4.5          6.5          9.0

# shortcut
aggregate(x, list(cut(x,4)), mean)
##        Group.1   x
## 1 (0.991,3.25] 2.0
## 2   (3.25,5.5] 4.5
## 3   (5.5,7.75] 6.5
## 4    (7.75,10] 9.0
```

see https://bookdown.org/rwnahhas/IntroToR/logical.html


## Arrays

Arrays are generalization of matrices. They are often used in spatial econometrics, and are a very efficient way to store numeric data with the same dimensions.


``` r
a <- array(data = 1:24, dim = c(2, 3, 4))
```


``` r
a

a[1, , , drop = FALSE]  # Row 1
#a[, 1, , drop = FALSE]  # Column 1
#a[, , 1, drop = FALSE]  # Layer 1

a[ 1, 1,  ]  # Row 1, column 1
#a[ 1,  , 1]  # Row 1, "layer" 1
#a[  , 1, 1]  # Column 1, "layer" 1
a[1 , 1, 1]  # Row 1, column 1, "layer" 1
```

Apply extends to arrays

``` r
apply(a, 1, mean)    # Row means
## [1] 12 13
apply(a, 2, mean)    # Column means
## [1] 10.5 12.5 14.5
apply(a, 3, mean)    # "Layer" means
## [1]  3.5  9.5 15.5 21.5
apply(a, 1:2, mean)  # Row/Column combination 
##      [,1] [,2] [,3]
## [1,]   10   12   14
## [2,]   11   13   15
```

Outer products yield arrays

``` r
x <- c(1,2,3)
x_mat1 <- outer(x, x) # x %o% x
x_mat1
##      [,1] [,2] [,3]
## [1,]    1    2    3
## [2,]    2    4    6
## [3,]    3    6    9
is.array(x_mat) # Matrices are arrays
## [1] TRUE

x_mat2 <- matrix(6:1,2,3)
outer(x_mat2, x)
## , , 1
## 
##      [,1] [,2] [,3]
## [1,]    6    4    2
## [2,]    5    3    1
## 
## , , 2
## 
##      [,1] [,2] [,3]
## [1,]   12    8    4
## [2,]   10    6    2
## 
## , , 3
## 
##      [,1] [,2] [,3]
## [1,]   18   12    6
## [2,]   15    9    3
# outer(x_mat2, matrix(x))
# outer(x_mat2, t(x))
# outer(x_mat1, x_mat2)
```

# Data
***

## Types

#### **Basic Types**. {-}
The two basic types of data are *cardinal* and *factor* data. We can further distinguish between whether cardinal data are discrete or continuous. We can also further distinguish between whether factor data are ordered or not

* *cardinal*: the difference between elements always mean the same thing. 
    * discrete: E.g., 2-1=3-2.
    * continuous: E.g., 2.11-1.4444=3.11-2.4444
* *factor*: the difference between elements does not always mean the same thing.
    * ordered: E.g., First place - Second place ?? Second place - Third place.
    * unordered (categorical): E.g., A - B ????


Here are some examples

``` r
d1d <- 1:3 # Cardinal data (Discrete)
d1d
## [1] 1 2 3
#class(d1d)

d1c <- c(1.1, 2/3, 3) # Cardinal data (Continuous)
d1c
## [1] 1.1000000 0.6666667 3.0000000
#class(d1c)

d2o <- factor(c('A','B','C'), ordered=T) # Factor data (Ordinal)
d2o
## [1] A B C
## Levels: A < B < C
#class(d2o)

d2c <- factor(c('Leipzig','Los Angeles','Logan'), ordered=F) # Factor data (Categorical)
d2c
## [1] Leipzig     Los Angeles Logan      
## Levels: Leipzig Logan Los Angeles
#class(d2c)
```

#### **Other Types**. {-} 
R also allows for more unstructured data types, such as *strings* and *lists*. You often combine all of the different data types into a single dataset called a *data.frame*

``` r
c('hello world', 'hi mom')  # character strings
## [1] "hello world" "hi mom"

list(d1c, d2c)  # lists
## [[1]]
## [1] 1.1000000 0.6666667 3.0000000
## 
## [[2]]
## [1] Leipzig     Los Angeles Logan      
## Levels: Leipzig Logan Los Angeles

# data.frames: your most common data type
    # matrix of different data-types
    # well-ordered lists
d0 <- data.frame(y=d1c, x=d2c)
d0
##           y           x
## 1 1.1000000     Leipzig
## 2 0.6666667 Los Angeles
## 3 3.0000000       Logan
```

Note that strings are encounter in a variety of settings, and you often have to format them after reading them into R.^[We will not cover the statistical analysis of text in this course, but strings are amenable to statistical analysis.]

``` r
# Strings
paste( 'hi', 'mom')
## [1] "hi mom"
paste( c('hi', 'mom'), collapse='--')
## [1] "hi--mom"

list(d1c, c('hello world'),
    list(d1d, list('...inception...'))) # lists
## [[1]]
## [1] 1.1000000 0.6666667 3.0000000
## 
## [[2]]
## [1] "hello world"
## 
## [[3]]
## [[3]][[1]]
## [1] 1 2 3
## 
## [[3]][[2]]
## [[3]][[2]][[1]]
## [1] "...inception..."

kingText <- "The king infringes the law on playing curling."
gsub(pattern="ing", replacement="", kingText)
## [1] "The k infres the law on play curl."
# advanced usage
#gsub("[aeiouy]", "_", kingText)
#gsub("([[:alpha:]]{3})ing\\b", "\\1", kingText) 
```
See 

* https://meek-parfait-60672c.netlify.app/docs/M1_R-intro_03_text.html
* https://raw.githubusercontent.com/rstudio/cheatsheets/main/regex.pdf




## Empirical Distributions

#### **Initial Inspection**. {-}
Regardless of the data types you have, you typically begin by inspecting your data by examining the first few observations.
 
Consider, for example, historical data on crime in the US.


``` r
head(USArrests)
##            Murder Assault UrbanPop Rape
## Alabama      13.2     236       58 21.2
## Alaska       10.0     263       48 44.5
## Arizona       8.1     294       80 31.0
## Arkansas      8.8     190       50 19.5
## California    9.0     276       91 40.6
## Colorado      7.9     204       78 38.7

# Check NA values
sum(is.na(x))
## [1] 0
```

To further examine a particular variable, we look at its distribution. In what follows, we will denote the data for a single variable as $\{X_{i}\}_{i=1}^{N}$, where there are $N$ observations and $X_{i}$ is the value of the $i$th one.

#### **Histogram**. {-}
The histogram divides the range of $\{X_{i}\}_{i=1}^{N}$ into $L$ exclusive bins of equal-width $h=[\text{max}(X_{i}) - \text{min}(X_{i})]/L$, and counts the number of observations within each bin. We often scale the counts to interpret the numbers as a density. Mathematically, for an exclusive bin with midpoint $x$, we compute
\begin{eqnarray}
\widehat{f}_{HIST}(x) &=& \frac{  \sum_{i}^{N} \mathbf{1}\left( X_{i} \in \left[x-\frac{h}{2}, x+\frac{h}{2} \right) \right) }{N h}.
\end{eqnarray}
We compute $\widehat{f}_{HIST}(x)$ for each $x \in \left\{ \frac{\ell h}{2} + \text{min}(X) \right\}_{\ell=1}^{L}$.

``` r
hist(USArrests$Murder, freq=F,
    border=NA, main='', xlab='Murder Arrests')
# Raw Observations
rug(USArrests$Murder, col=grey(0,.5))
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-35-1.png" width="672" />


Note that if you your data is discrete, you can directly plot the counts.

``` r
x <- floor(USArrests$Murder) #Discretized
plot(table(x), xlab='Murder Rate (Discrete)', ylab='Count')
```

#### **Empirical *Cumulative* Distribution Function**. {-}
The ECDF counts the proportion of observations whose values $X_{i}$ are less than $x$; 
\begin{eqnarray}
\widehat{F}_{ECDF}(x) = \frac{1}{N} \sum_{i}^{N} \mathbf{1}(X_{i} \leq x) 
\end{eqnarray}
for each unique value of $x$ in the dataset.


``` r
F_murder <- ecdf(USArrests$Murder)
# proportion of murders < 10
F_murder(10)
## [1] 0.7
# proportion of murders < x, for all x
plot(F_murder, main='', xlab='Murder Arrests',
    pch=16, col=grey(0,.5))
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-37-1.png" width="672" />

#### **Boxplots**. {-}
Boxplots summarize the distribution of data using *quantiles*: the $q$th quantile is the value where $q$ percent of the data are below and ($1-q$) percent are above.

* The "median" is the point where half of the data has lower values and the other half has higher values.
* The "lower quartile" is the point where 25% of the data has lower values and the other 75% has higher values.
* The "min" is the smallest value (or largest negative value if there are any) where 0% of the data has lower values.


``` r
x <- USArrests$Murder

# quantiles
median(x)
## [1] 7.25
range(x)
## [1]  0.8 17.4
quantile(x, probs=c(0,.25,.5))
##    0%   25%   50% 
## 0.800 4.075 7.250

# deciles are quantiles
quantile(x, probs=seq(0,1, by=.1))
##    0%   10%   20%   30%   40%   50%   60%   70%   80%   90%  100% 
##  0.80  2.56  3.38  4.75  6.00  7.25  8.62 10.12 12.12 13.32 17.40
```

To compute quantiles, we sort the observations from smallest to largest as $X_{(1)}, X_{(2)},... X_{(N)}$, and then compute quantiles as $X_{ (q*N) }$. Note that $(q*N)$ is rounded and there are different ways to break ties.

``` r
xo <- sort(x)
xo
##  [1]  0.8  2.1  2.1  2.2  2.2  2.6  2.6  2.7  3.2  3.3  3.4  3.8  4.0  4.3  4.4
## [16]  4.9  5.3  5.7  5.9  6.0  6.0  6.3  6.6  6.8  7.2  7.3  7.4  7.9  8.1  8.5
## [31]  8.8  9.0  9.0  9.7 10.0 10.4 11.1 11.3 11.4 12.1 12.2 12.7 13.0 13.2 13.2
## [46] 14.4 15.4 15.4 16.1 17.4

# median
xo[length(xo)*.5]
## [1] 7.2
quantile(x, probs=.5, type=4)
## 50% 
## 7.2

# min
xo[1]
## [1] 0.8
min(xo)
## [1] 0.8
quantile(xo,probs=0)
##  0% 
## 0.8
```

The boxplot shows the median (solid black line) and interquartile range ($IQR=$ upper quartile $-$ lower quartile; filled box),^[Technically, the upper and lower ``hinges'' use two different versions of the first and third quartile. See https://stackoverflow.com/questions/40634693/lower-and-upper-quartiles-in-boxplot-in-r] as well extreme values as outliers beyond the $1.5\times IQR$ (points beyond whiskers).


``` r
boxplot(USArrests$Murder, main='', ylab='Murder Arrests')
# Raw Observations
stripchart(USArrests$Murder,
    pch='-', col=grey(0,.5), cex=2,
    vert=T, add=T)
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-40-1.png" width="672" />

## Joint Distributions

Scatterplots are used frequently to summarize the joint relationship between two variables. They can be enhanced in several ways. As a default, use semi-transparent points so as not to hide any points (and perhaps see if your observations are concentrated anywhere).

You can also add regression lines (and confidence intervals), although I will defer this until later.


``` r
plot(Murder~UrbanPop, USArrests, pch=16, col=grey(0.,.5))
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-41-1.png" width="672" />

``` r

# Add the line of best fit for pooled data
#reg <- lm(Murder~UrbanPop, data=USArrests)
#abline(reg, lty=2)
```

#### **Marginal Distributions**.{-}
You can also show the distributions of each variable along each axis.


``` r
# Setup Plot
layout( matrix(c(2,0,1,3), ncol=2, byrow=TRUE),
    widths=c(9/10,1/10), heights=c(1/10,9/10))

# Scatterplot
par(mar=c(4,4,1,1))
plot(Murder~UrbanPop, USArrests, pch=16, col=rgb(0,0,0,.5))

# Add Marginals
par(mar=c(0,4,1,1))
xhist <- hist(USArrests$UrbanPop, plot=FALSE)
barplot(xhist$counts, axes=FALSE, space=0, border=NA)

par(mar=c(4,0,1,1))
yhist <- hist(USArrests$Murder, plot=FALSE)
barplot(yhist$counts, axes=FALSE, space=0, horiz=TRUE, border=NA)
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-42-1.png" width="672" />


## Conditional Distributions

It is easy to show how distributions change according to a third variable using data splits. E.g., 


``` r
# Tailored Histogram 
ylim <- c(0,8)
xbks <-  seq(min(USArrests$Murder)-1, max(USArrests$Murder)+1, by=1)

# Also show more information
# Split Data by Urban Population above/below mean
pop_mean <- mean(USArrests$UrbanPop)
murder_lowpop <- USArrests[USArrests$UrbanPop< pop_mean,'Murder']
murder_highpop <- USArrests[USArrests$UrbanPop>= pop_mean,'Murder']
cols <- c(low=rgb(0,0,1,.75), high=rgb(1,0,0,.75))

par(mfrow=c(1,2))
hist(murder_lowpop,
    breaks=xbks, col=cols[1],
    main='Urban Pop >= Mean', font.main=1,
    xlab='Murder Arrests',
    border=NA, ylim=ylim)

hist(murder_highpop,
    breaks=xbks, col=cols[2],
    main='Urban Pop < Mean', font.main=1,
    xlab='Murder Arrests',
    border=NA, ylim=ylim)
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-43-1.png" width="672" />

It is sometimes it is preferable to show the ECDF instead. And you can glue various combinations together to convey more information all at once


``` r
par(mfrow=c(1,2))
# Full Sample Density
hist(USArrests$Murder, 
    main='Density Function Estimate', font.main=1,
    xlab='Murder Arrests',
    breaks=xbks, freq=F, border=NA)

# Split Sample Distribution Comparison
F_lowpop <- ecdf(murder_lowpop)
plot(F_lowpop, col=cols[1],
    pch=16, xlab='Murder Arrests',
    main='Distribution Function Estimates',
    font.main=1, bty='n')
F_highpop <- ecdf(murder_highpop)
plot(F_highpop, add=T, col=cols[2], pch=16)

legend('bottomright', col=cols,
    pch=16, bty='n', inset=c(0,.1),
    title='% Urban Pop.',
    legend=c('Low (<= Mean)','High (>= Mean)'))
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-44-1.png" width="672" />


You can also split data into grouped boxplots in the same way

``` r
layout( t(c(1,2,2)))
boxplot(USArrests$Murder, main='',
    xlab='All Data', ylab='Murder Arrests')

# K Groups with even spacing
K <- 3
USArrests$UrbanPop_Kcut <- cut(USArrests$UrbanPop,K)
Kcols <- hcl.colors(K,alpha=.5)
boxplot(Murder~UrbanPop_Kcut, USArrests,
    main='', col=Kcols,
    xlab='Urban Population', ylab='')
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-45-1.png" width="672" />

``` r

# 4 Groups with equal numbers of observations
#Qcuts <- c(
#    '0%'=min(USArrests$UrbanPop)-10*.Machine$double.eps,
#    quantile(USArrests$UrbanPop, probs=c(.25,.5,.75,1)))
#USArrests$UrbanPop_cut <- cut(USArrests$UrbanPop, Qcuts)
#boxplot(Murder~UrbanPop_cut, USArrests, col=hcl.colors(4,alpha=.5))
```

You can also use size, color, and shape to further distinguish different conditional relationships.

``` r
# High Assault Areas
assault_high <- USArrests$Assault > median(USArrests$Assault)
cols <- ifelse(assault_high, rgb(1,0,0,.5), rgb(0,0,1,.5))

# Scatterplot
# Show High Assault Areas via 'cex=' or 'pch='
# Could further add regression lines for each data split
plot(Murder~UrbanPop, USArrests, pch=16, col=cols)
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-46-1.png" width="672" />



## Random Variables

Random variables are vectors that are generated from a probabilistic process. 

* The *sample space* of a random variable refers to the set of all possible outcomes.
* The *probability* of a particular set of outcomes is the proportion that those outcomes occur in the long run.

There are two basic types of sample spaces: discrete and random, which lead to two types of random variables.

#### **Discrete Random Variables**. {-}
The random variable can take one of several discrete values.  E.g., any number in $\{1,2,3,...\}$.

Bernoulli (Coin Flip: Heads=1 Tails=0)

``` r
rbinom(1, 1, 0.5) # 1 draw
## [1] 0
rbinom(4, 1, 0.5) # 4 draws
## [1] 0 0 0 0
x0 <- rbinom(600, 1, 0.5)

# Setup Plot
layout(matrix(c(1, 2), nrow = 1), widths = c(4, 1))

# Plot Cumulative Averages
x0_t <- seq_len(length(x0))
x0_mt <- cumsum(x0)/x0_t
par(mar=c(4,4,1,4))
plot(x0_t, x0_mt, type='l',
    ylab='Cumulative Average',
    xlab='Flip #', 
    ylim=c(0,1), 
    lwd=2)
points(x0_t, x0, col=grey(0,.5),
    pch=16, cex=.2)

# Plot Long run proportions
par(mar=c(4,4,1,1))
x_hist <- hist(x0, breaks=50, plot=F)
barplot(x_hist$count, axes=FALSE,
    space=0, horiz=TRUE, border=NA)
axis(1)
axis(2)
mtext('Overall Count', 2, line=2.5)
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-47-1.png" width="672" />

Try an Unfair Coin Flip

``` r
x0 <- rbinom(2000, 1, 0.2)
hist(x0, breaks=50, border=NA, main=NA, freq=T)
```

Discrete Uniform (numbers 1,...4)

``` r
# sample(1:4, 1, replace=T, prob=rep(1/4,4) ) # 1 draw, equal probabilities
x1 <- sample(1:4, 2000, replace=T, prob=rep(1/4,4))
hist(x1, breaks=50, border=NA, main=NA, freq=T)
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-49-1.png" width="672" />

Multinoulli (aka Categorical)

``` r
x1 <- sample(1:4, 2000, replace=T, prob=c(3,4,1,2)/10) # unequal probabilities
hist(x1, breaks=50, border=NA, main=NA, freq=T)
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-50-1.png" width="672" />

#### **Continuous Random Variables**. {-}
The random variable can take one value out of an uncountably infinite number. E.g., any number between $[0,1]$ allowing for any number of decimal points.


Continuous Uniform

``` r
runif(3) # 3 draws
## [1] 0.5294525 0.8117577 0.7800693
x2 <- runif(2000)
hist(x2, breaks=20, border=NA, main=NA, freq=F)
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-51-1.png" width="672" />

Normal (Gaussian)

``` r
rnorm(3) # 3 draws
## [1] 0.05664424 1.30552460 0.33014971
x3 <- rnorm(2000)
hist(x3, breaks=20, border=NA, main=NA, freq=F)
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-52-1.png" width="672" />

We might further distinguish types of random variables based on whether their maximum value is theoretically finite or infinite.

#### **Probability distributions**. {-}
Random variables are drawn from [probability distributions](https://en.wikipedia.org/wiki/List_of_probability_distributions). The most common ones are [easily accessible](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/Distributions.html).

All random variables have an associated theoretical Cumulative Distribution Function: $F_{X}(x) =$ Probability$(X_{i} \leq x)$. Continuous random variables have an associated density function: $f_{X}$, as well as a quantile function: $Q_{X}(p)$, which is the inverse of the CDF: the $x$ value where $p$ percent of the data fall below it. (Recall that the median is the value $x$ where $50\%$ of the data fall below $x$, for example.)

Here is an example of the [Beta](https://en.wikipedia.org/wiki/Beta_distribution) probability distribution

``` r
pars <- expand.grid( c(.5,1,2), c(.5,1,2) )
par(mfrow=c(3,3))
apply(pars, 1, function(p){
    x <- seq(0,1,by=.01)
    fx <- dbeta( x,p[1], p[2])
    plot(x, fx, type='l', xlim=c(0,1), ylim=c(0,4), lwd=2)
    #hist(rbeta(2000, p[1], p[2]), breaks=50, border=NA, main=NA, freq=F)
})
title('Beta densities', outer=T, line=-1)
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-53-1.png" width="672" />

Here is a more in-depth example of drawing random variables from the [Dagum distribution](https://en.wikipedia.org/wiki/Dagum_distribution)


``` r
# Quantile Function (VGAM::qdagum)
qdagum <- function(p, scale=1, shape1.a, shape2.p) {
  # Quantile function (theoretically derived from the CDF)
  ans <- scale * (expm1(-log(p) / shape2.p))^(-1 / shape1.a)
  # Special known cases
  ans[p == 0] <- 0
  ans[p == 1] <- Inf
  # Checks
  ans[p < 0] <- NaN
  ans[p > 1] <- NaN
  if(scale <= 0 | shape1.a <= 0 | shape2.p <= 0){ ans <- ans*NaN }
  # Return
  return(ans)
}

# Generate Random Variables (VGAM::rdagum)
rdagum <-function(n, scale=1, shape1.a, shape2.p){
    p <- runif(n) # generate random quantile probabilities
    x <- qdagum(p, scale=scale, shape1.a=shape1.a, shape2.p=shape2.p) #find the inverses
    return(x)
}

# Example
set.seed(123)
x <- rdagum(3000,1,3,1)

# Empirical Distribution
Fx_hat <- ecdf(x)
plot(Fx_hat, lwd=2, xlim=c(0,5), main='')

# Two Examples of generating a random variable
p <- c(.25, .9)
cols <- c(2,4)
Qx_hat <- quantile(x, p)
segments(Qx_hat,p,-10,p, col=cols)
segments(Qx_hat,p,Qx_hat,0, col=cols)
mtext( round(Qx_hat,2), 1, at=Qx_hat, col=cols)
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-54-1.png" width="672" />

We will return to the theory behind probability distributions in a later chapter.

## Further Reading 

For plotting histograms and marginals, see 

* https://www.r-bloggers.com/2011/06/example-8-41-scatterplot-with-marginal-histograms/
* https://r-graph-gallery.com/histogram.html
* https://r-graph-gallery.com/74-margin-and-oma-cheatsheet.html 
* https://jtr13.github.io/cc21fall2/tutorial-for-scatter-plot-with-marginal-distribution.html.


# Statistics
***

We often summarize distributions with *statistics*: functions of data. The most basic way to do this is with `summary`, whose values can all be calculated individually. (E.g., the "mean" computes the [sum of all values] divided by [number of values].) There are *many* other statistics.


``` r
summary( runif(1000))
##      Min.   1st Qu.    Median      Mean   3rd Qu.      Max. 
## 6.534e-05 2.434e-01 5.054e-01 5.040e-01 7.685e-01 9.995e-01
summary( rnorm(1000) )
##     Min.  1st Qu.   Median     Mean  3rd Qu.     Max. 
## -2.84855 -0.65619 -0.05057 -0.02011  0.64258  3.42109
```

## Mean and Variance

The most basic statistics summarize the center of a distribution and how far apart the values are spread.

#### **Mean**. {-}
Perhaps the most common statistic is the mean;
$$\overline{X}=\frac{\sum_{i=1}^{N}X_{i}}{N},$$ where $X_{i}$ denotes the value of the $i$th observation.


``` r
# compute the mean of a random sample
x <- runif(100)
hist(x, border=NA, main=NA)
m <- mean(x)  #sum(x)/length(x)
abline(v=m, col=2, lwd=2)
title(paste0('mean= ', round(m,2)), font.main=1)
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-56-1.png" width="672" />

``` r
# is m close to it's true value (1-0)/2=.5?
```

#### **Variance**.{-}
Perhaps the second most common statistic is the variance: the average squared deviation from the mean
$$V_{X} =\frac{\sum_{i=1}^{N} [X_{i} - \overline{X}]^2}{N}.$$
The standard deviation is simply $s_{X} = \sqrt{V_{X}}$.



``` r
s <- sd(x) # sqrt(var(x))
hist(x, border=NA, main=NA, freq=F)
s_lh <- c(m - s,  m + s)
abline(v=s_lh, col=4)
text(s_lh, -.02,
    c( expression(bar(X)-s[X]), expression(bar(X)+s[X])),
    col=4, adj=0)
title(paste0('sd= ', round(s,2)), font.main=1)
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-57-1.png" width="672" />

Note that a "corrected version" is used by R and many statisticians: $V_{X} =\frac{\sum_{i=1}^{N} [X_{i} - \overline{X}]^2}{N-1}$.

``` r
var(x)
## [1] 0.08561227
mean( (x - mean(x))^2 )
## [1] 0.08475614
```

Together, these statistics summarize the central tendency and dispersion of a distribution. In some special cases, such as with the normal distribution, they completely describe the distribution. Other distributions are easier to describe with other statistics.


## Other Center/Spread Statistics

#### **Absolute Deviations**. {-}
We can use the *Median* as a "robust alternative" to means. Recall that the $q$th quantile is the value where $q$ percent of the data are below and ($1-q$) percent are above. The median ($q=.5$) is the point where half of the data is lower values and the other half is higher.


We can also use the *Interquartile Range* or *Median Absolute Deviation* as an alternative to variance. The first and third quartiles ($q=.25$ and $q=.75$) together measure is the middle 50 percent of the data. The size of that range (interquartile range: the difference between the quartiles) represents "spread" or "dispersion" of the data. The median absolute deviation also measures spread
$$
\tilde{X} = Med(X_{i}) \\
MAD_{X} = Med\left( | X_{i} - \tilde{X} | \right).
$$


``` r
x <- rgeom(50, .4)
x
##  [1]  2  0  5  0  2  0  0  2  4  3  3  0  0  1  0  3  4  1  2  0  0  6  1  0  1
## [26]  0  1  0  0  0  0  0  3  0  0 11  1  7  2  1  0  8  4  0  2  5  2  0  0  0

plot(table(x))
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-59-1.png" width="672" />

``` r

#mean(x)
median(x)
## [1] 1

#sd(x)
#IQR(x) # diff( quantile(x, probs=c(.25,.75)))
mad(x, constant=1) # median( abs(x - median(x)) )
## [1] 1
```

Note that there other absolute deviations:

``` r
mean( abs(x - mean(x)) )
mean( abs(x - median(x)) )
median( abs(x - mean(x)) )
```

#### **Mode and Share Concentration**. {-}
Sometimes, none of the above work well. With categorical data, for example, distributions are easier to describe with other statistics. The mode is the most common observation: the value with the highest observed frequency. We can also measure the spread/dispersion of the frequencies, or compare the highest frequency to the average frequency to measure concentration at the mode.


``` r
# Draw 3 Random Letters
K <- length(LETTERS)
x_id <- rmultinom(3, 1, prob=rep(1/K,K))
x_id
##       [,1] [,2] [,3]
##  [1,]    0    0    0
##  [2,]    0    0    0
##  [3,]    0    0    0
##  [4,]    0    0    0
##  [5,]    0    0    0
##  [6,]    0    0    0
##  [7,]    0    0    0
##  [8,]    0    0    0
##  [9,]    0    0    1
## [10,]    0    0    0
## [11,]    0    0    0
## [12,]    0    0    0
## [13,]    0    0    0
## [14,]    0    0    0
## [15,]    0    0    0
## [16,]    0    0    0
## [17,]    0    0    0
## [18,]    0    0    0
## [19,]    0    0    0
## [20,]    0    1    0
## [21,]    0    0    0
## [22,]    0    0    0
## [23,]    0    0    0
## [24,]    0    0    0
## [25,]    0    0    0
## [26,]    1    0    0

# Draw Random Letters 100 Times
x_id <- rowSums(rmultinom(100, 1, prob=rep(1/K,K)))
x <- lapply(1:K, function(k){
    rep(LETTERS[k], x_id[k])
})
x <- factor(unlist(x), levels=LETTERS)

plot(x)
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-61-1.png" width="672" />

``` r

tx <- table(x)
# mode(s)
names(tx)[tx==max(tx)]
## [1] "Z"

# freq. spread
sx <- tx/sum(tx)
sd(sx) # mad(sx)
## [1] 0.01953301

# freq. concentration 
max(tx)/mean(tx)
## [1] 2.08
```

## Shape Statistics

Central tendency and dispersion are often insufficient to describe a distribution. To further describe shape, we can compute the "standard moments" skew and kurtosis, as well as other statistics.


#### **Skewness**. {-}
This captures how symmetric the distribution is.
$$Skew_{X} =\frac{\sum_{i=1}^{N} [X_{i} - \overline{X}]^3 / N}{ [s_{X}]^3 }$$



``` r
x <- rweibull(1000, shape=1)
hist(x, border=NA, main=NA, freq=F, breaks=20)
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-62-1.png" width="672" />

``` r

skewness <-  function(x) {
 x_bar <- mean(x)
 m3 <- mean((x - x_bar)^3)
 skew <- m3/(sd(x)^3)
 return(skew)
}

skewness( rweibull(1000, shape=1))
## [1] 2.271089
skewness( rweibull(1000, shape=10) )
## [1] -0.5094236
```

#### **Kurtosis**. {-}
This captures how many "outliers" there are.
$$Kurt_{X} =\frac{\sum_{i=1}^{N} [X_{i} - \overline{X}]^4 / N}{ [s_{X}]^4 }.$$


``` r
x <- rweibull(1000, shape=1)
boxplot(x, main=NA)
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-63-1.png" width="672" />

``` r

kurtosis <- function(x) {  
 x_bar <- mean(x)
 m4 <- mean((x - x_bar)^4) 
 kurt <- m4/(sd(x)^4) - 3  
 return(kurt)
}

kurtosis( rweibull(1000, shape=1))
## [1] 5.471682
kurtosis( rweibull(1000, shape=10) )
## [1] 0.5462298
```

#### **Clusters/Gaps**. {-}
You can also describe distributions in terms of how clustered the values are. Remember: *a picture is worth a thousand words*.


``` r
# Number of Modes
x <- rbeta(1000, .6, .6)
hist(x, border=NA, main=NA, freq=F, breaks=20)
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-64-1.png" width="672" />

``` r

# Random Number Generator 
r_ugly1 <- function(n, theta1=c(-8,-1), theta2=c(-2,2), rho=.25){
    omega   <- rbinom(n, size=1, rho)
    epsilon <- omega * runif(n, theta1[1], theta2[1]) +
        (1-omega) * rnorm(n, theta1[2], theta2[2])
    return(epsilon)
}
# Large Sample
par(mfrow=c(1,1))
X <- seq(-12,6,by=.001)
rx <- r_ugly1(1000000)
hist(rx, breaks=1000,  freq=F, border=NA,
    xlab="x", main='')
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-64-2.png" width="672" />


``` r
# Show True Density
d_ugly1 <- function(x, theta1=c(-8,-1), theta2=c(-2,2), rho=.25){
    rho     * dunif(x, theta1[1], theta2[1]) +
    (1-rho) * dnorm(x, theta1[2], theta2[2]) }
dx <- d_ugly1(X)
lines(X, dx, col=1)
```

## Associations

There are several ways to quantitatively describe the relationship between two variables, $Y$ and $X$. The major differences surround whether the variables are cardinal, ordinal, or categorical.

#### **Correlation**. {-}
**Pearson (Linear) Correlation**.
Suppose $X$ and $Y$ are both cardinal data. As such, you can compute the most famous measure of association, the covariance:
$$
C_{XY} =  \sum_{i} [X_i - \overline{X}] [Y_i - \overline{Y}] / N
$$

``` r
# Bivariate Data from USArrests
xy <- USArrests[,c('Murder','UrbanPop')]
#plot(xy, pch=16, col=grey(0,.25))
cov(xy)
##             Murder   UrbanPop
## Murder   18.970465   4.386204
## UrbanPop  4.386204 209.518776
```
Note that $C_{XX}=V_{X}$.
For ease of interpretation, we rescale this statistic to always lay between $-1$ and $1$ 
$$
r_{XY} = \frac{ C_{XY} }{ \sqrt{V_X} \sqrt{V_Y}}
$$

``` r
cor(xy)[2]
## [1] 0.06957262
```

**Falk Codeviance**.
The Codeviance is a robust alternative to Covariance. Instead of relying on means (which can be sensitive to outliers), it uses medians ($\tilde{X}$) to capture the central tendency.^[See also *Theil-Sen Estimator*, which may be seen as a precursor.] We can also scale the Codeviance by the median absolute deviation to compute the median correlation.
\[
\text{CoDev}(X,Y) = \text{Med}\left\{ |X_i - \tilde{X}| |Y_i - \tilde{Y}| \right\} \\
\tilde{r}_{XY} = \frac{ \text{CoDev}(X,Y) }{ \text{MAD}(X) \text{MAD}(Y) }.
\]

``` r
cor_m <- function(xy) {
  # Compute medians for each column
  med <- apply(xy, 2, median)
  # Subtract the medians from each column
  xm <- sweep(xy, 2, med, "-")
  # Compute CoDev
  CoDev <- median(xm[, 1] * xm[, 2])
  # Compute the medians of absolute deviation
  MadProd <- prod( apply(abs(xm), 2, median) )
  # Return the robust correlation measure
  return( CoDev / MadProd)
}
cor_m(xy)
## [1] 0.005707763
```

#### **Kendall's Tau**. {-}
Suppose $X$ and $Y$ are both *ordered* variables. Kendall's Tau measures the strength and direction of association by counting the number of concordant pairs (where the ranks agree) versus discordant pairs (where the ranks disagree). A value of \(\tau = 1\) implies perfect agreement in rankings, \(\tau = -1\) indicates perfect disagreement, and \(\tau = 0\) suggests no association in the ordering.
\[
\tau = \frac{2}{n(n-1)} \sum_{i} \sum_{j > i} \text{sgn} \Bigl( (X_i - X_j)(Y_i - Y_j) \Bigr),
\]
where the sign function is:
$$
\text{sgn}(z) = 
\begin{cases}
+1 & \text{if } z > 0\\
0  & \text{if } z = 0 \\
-1 & \text{if} z < 0 
\end{cases}.
$$

``` r
xy <- USArrests[,c('Murder','UrbanPop')]
xy[,1] <- rank(xy[,1] )
xy[,2] <- rank(xy[,2] )
# plot(xy, pch=16, col=grey(0,.25))
tau <- cor(xy[, 1], xy[, 2], method = "kendall")
round(tau, 3)
## [1] 0.074
```

#### **Cramer's V**. {-}
Suppose $X$ and $Y$ are both *categorical* variables; the value of $X$ is one of $1...r$ categories and the value of $Y$ is one of $1...k$ categories. Cramer's V quantifies the strength of association by adjusting a "chi-squared" statistic to provide a measure that ranges from 0 to 1; 0 indicates no association while a value closer to 1 signifies a strong association. 

First, consider a contingency table for $X$ and $Y$ with \(r\) rows and \(k\) columns. The chi-square statistic is then defined as:

\[
\chi^2 = \sum_{i=1}^{r} \sum_{j=1}^{k} \frac{(O_{ij} - E_{ij})^2}{E_{ij}}.
\]

where

- \(O_{ij}\) denote the observed frequency in cell \((i, j)\),
- \(E_{ij} = \frac{R_i \cdot C_j}{n}\) is the expected frequency for each cell if $X$ and $Y$ are independent
- \(R_i\) denote the total frequency for row \(i\) (i.e., \(R_i = \sum_{j=1}^{k} O_{ij}\)),
- \(C_j\) denote the total frequency for column \(j\) (i.e., \(C_j = \sum_{i=1}^{r} O_{ij}\)),
- \(n\) be the grand total of observations, so that \(n = \sum_{i=1}^{r} \sum_{j=1}^{k} O_{ij}\).


Second, normalize the chi-square statistic with the sample size and the degrees of freedom to compute Cramer's V. 

\[
V = \sqrt{\frac{\chi^2 / n}{\min(k - 1, \, r - 1)}},
\]

where:

- \(n\) is the total sample size,
- \(k\) is the number of categories for one variable,
- \(r\) is the number of categories for the other variable.



``` r
xy <- USArrests[,c('Murder','UrbanPop')]
xy[,1] <- cut(xy[,1],3)
xy[,2] <- cut(xy[,2],4)
table(xy)
##               UrbanPop
## Murder         (31.9,46.8] (46.8,61.5] (61.5,76.2] (76.2,91.1]
##   (0.783,6.33]           4           5           8           5
##   (6.33,11.9]            0           4           7           6
##   (11.9,17.4]            2           4           2           3

cor_v <- function(xy){
    # Create a contingency table from the categorical variables
    tbl <- table(xy)
    # Compute the chi-square statistic (without Yates' continuity correction)
    chi2 <- chisq.test(tbl, correct=FALSE)$statistic
    # Total sample size
    n <- sum(tbl)
    # Compute the minimum degrees of freedom (min(rows-1, columns-1))
    df_min <- min(nrow(tbl) - 1, ncol(tbl) - 1)
    # Calculate Cramer's V
    V <- sqrt((chi2 / n) / df_min)
    return(V)
}
cor_v(xy)
## X-squared 
## 0.2307071

# DescTools::CramerV( table(xy) )
```


## Beyond Basics

Use expansion "packages" for less common procedures and more functionality

#### **CRAN**. {-}
Most packages can be found on CRAN and can be easily installed

``` r
# commonly used packages
install.packages("stargazer")
install.packages("data.table")
install.packages("plotly")
# other statistical packages
install.packages("extraDistr")
install.packages("twosamples")
# install.packages("purrr")
# install.packages("reshape2")
```

The most common tasks also have [cheatsheets](https://www.rstudio.com/resources/cheatsheets/) you can use. 

For example, to generate 'exotic' probability distributions


``` r
library(extraDistr)

par(mfrow=c(1,2))
for(p in c(-.5,0)){
    x <- rgev(2000, mu=0, sigma=1, xi=p)
    hist(x, breaks=50, border=NA, main=NA, freq=F)
}
title('GEV densities', outer=T, line=-1)
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-72-1.png" width="672" />


``` r
library(extraDistr)

par(mfrow=c(1,3))
for(p in c(-1, 0,2)){
    x <- rtlambda(2000, p)
    hist(x, breaks=100, border=NA, main=NA, freq=F)
}
title('Tukey-Lambda densities', outer=T, line=-1)
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-73-1.png" width="672" />

#### **Github**.  {-}
Sometimes you will want to install a package from GitHub. For this, you can use [devtools](https://devtools.r-lib.org/) or its light-weight version [remotes](https://remotes.r-lib.org/)

``` r
install.packages("devtools")
install.packages("remotes")
```

Note that to install `devtools`, you also need to have developer tools installed on your computer.

* Windows: [Rtools](https://cran.r-project.org/bin/windows/Rtools/rtools42/rtools.html)
* Mac: [Xcode](https://apps.apple.com/us/app/xcode/id497799835?mt=12)

To color terminal output on Linux systems, you can use the colorout package

``` r
library(remotes)
# Install https://github.com/jalvesaq/colorout
# to .libPaths()[1]
install_github('jalvesaq/colorout')
library(colorout)
```

#### **Base**. {-}
While additional packages can make your code faster, they also create dependancies that can lead to problems. So learn base R well before becoming dependant on other packages

* https://bitsofanalytics.org/posts/base-vs-tidy/
* https://jtr13.github.io/cc21fall2/comparison-among-base-r-tidyverse-and-datatable.html






## Further Reading

Many random variables are related to each other

* https://en.wikipedia.org/wiki/Relationships_among_probability_distributions
* https://www.math.wm.edu/~leemis/chart/UDR/UDR.html
* https://qiangbo-workspace.oss-cn-shanghai.aliyuncs.com/2018-11-11-common-probability-distributions/distab.pdf

Note that numbers randomly generated on your computer cannot be truly random, they are "Pseudorandom".


# (Re)Sampling 
***



## Sample Distributions

The *sampling distribution* of a statistic shows us how much a statistic varies from sample to sample.

For example, see how the mean varies from sample to sample to sample.


``` r
# Three Sample Example
par(mfrow=c(1,3))
for(i in 1:3){
    x <- runif(100) 
    m <-  mean(x)
    hist(x,
        breaks=seq(0,1,by=.1), #for comparability
        main=NA, border=NA)
    abline(v=m, col=2, lwd=2)
    title(paste0('mean= ', round(m,2)),  font.main=1)
}
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-76-1.png" width="672" />

Examine the sampling distribution of the mean

``` r
sample_means <- sapply(1:1000, function(i){
    m <- mean(runif(100))
    return(m)
})
hist(sample_means, breaks=50, border=NA,
    col=2, font.main=1,
    main='Sampling Distribution of the mean')
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-77-1.png" width="672" />

In this figure, you see two the most profound results known in statistics

* *Law of Large Numbers*: the sample mean is centered around the true mean.
* *Central Limit Theorem*: the sampling distribution of the mean is approximately standard normal.

#### **Central Limit Theorem**. {-}
There are actually many different variants of the central limit theorem, as it applies more generally: the sampling distribution of many statistics are standard normal. For example, examine the sampling distribution of the standard deviation.

``` r
three_sds <- c(  sd(runif(100)),  sd(runif(100)),  sd(runif(100))  )
three_sds
## [1] 0.3013933 0.3024440 0.2870721

sample_sds <- sapply(1:1000, function(i){
    s <- sd(runif(100))
    return(s)
})
hist(sample_sds, breaks=50, border=NA,
    col=4, font.main=1,
    main='Sampling Distribution of the sd')
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-78-1.png" width="672" />

It is beyond this class to prove this result, but you should know that not all sampling distributions are standard normal. For example, examine the sampling distribution of the three main "order statistics"

``` r
# Create 300 samples, each with 1000 random uniform variables
x <- sapply(1:300, function(i) runif(1000) )
# Each row is a new sample
length(x[1,])
## [1] 300

# Median looks normal, Maximum and Minumum do not!
xmin <- apply(x,1,quantile, probs=0)
xmed <- apply(x,1,quantile, probs=.5)
xmax <- apply(x,1,quantile, probs=1)
par(mfrow=c(1,3))
hist(xmin, breaks=100, border=NA, main='Min', font.main=1)
hist(xmed, breaks=100, border=NA, main='Med', font.main=1)
hist(xmax, breaks=100, border=NA, main='Max', font.main=1)
title('Sampling Distributions', outer=T, line=-1)
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-79-1.png" width="672" />


``` r
# To explore, try any function!
fun_of_rv <- function(f, n=100){
  x <- runif(n)
  y <- f(x)
  return(y)
}

fun_of_rv( f=mean )
## [1] 0.4550786

fun_of_rv( f=function(i){ diff(range(exp(i))) } )
## [1] 1.715702
```


## Intervals

Using either the bootstrap or jackknife distribution, we can calculate 

* *confidence interval:* range your statistic varies across different samples.
* *standard error*: variance of your statistic across different samples.



``` r
sample_means <- apply(x,1,mean)
# standard error
sd(sample_means)
## [1] 0.01675757
```

Note that in some cases, you can estimate the standard error to get a confidence interval.

``` r
x00 <- x[1,]
# standard error
s00 <- sd(x00)/sqrt(length(x00))
ci <- mean(x00) + c(1.96, -1.96)*s00
```

#### **Confidence Interval**.  {-}
Compute the upper and lower quantiles of the sampling distribution.

*Sample Mean*. We simulate the sampling distribution of the sample mean and construct a 90% confidence interval by taking the 5th and 95th percentiles of the simulated means. This gives an empirical estimate of the interval within which the true mean is expected to lie with 90% confidence, assuming repeated sampling.

``` r
# Middle 90%
mq <- quantile(sample_means, probs=c(.05,.95))
paste0('we are 90% confident that the mean is between ', 
    round(mq[1],2), ' and ', round(mq[2],2) )
## [1] "we are 90% confident that the mean is between 0.47 and 0.53"

bks <- seq(.4,.6,by=.001)
hist(sample_means, breaks=bks, border=NA,
    col=rgb(0,0,0,.25), font.main=1,
    main='Confidence Interval for the mean')
abline(v=mq)
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-83-1.png" width="672" />

*Sample Percentile*. We repeat the process to estimate the 99th percentile for each sample. We then construct a 95% confidence interval for the 99th percentile estimator, using the 2.5th and 97.5th quantiles of these estimates.

``` r
## Upper Percentile
sample_quants <- apply(x,1,quantile, probs=.99)

# Middle 95% of estimates
mq <- quantile(sample_quants, probs=c(.025,.975))
paste0('we are 95% confident that the upper percentile is between ', 
    round(mq[1],2), ' and ', round(mq[2],2) )
## [1] "we are 95% confident that the upper percentile is between 0.97 and 1"

bks <- seq(.92,1,by=.001)
hist(sample_quants, breaks=bks, border=NA,
    col=rgb(0,0,0,.25), font.main=1,
    main='95% Confidence Interval for the 99% percentile')
abline(v=mq)
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-84-1.png" width="672" />

Note that X% confidence intervals do not generally cover X% of the data. Those intervals are a type of prediction interval that is covered later. See also https://online.stat.psu.edu/stat200/lesson/4/4.4/4.4.2

#### **Advanced Intervals**. {-}
In many cases, we want a X% interval to mean that X% of the intervals we generate will contain the true mean. E.g., in repeated sampling, 50% of constructed confidence intervals are expected to contain the true population mean.


``` r
# Theoretically: [-1 sd, +1 sd] has 2/3 coverage

# Confidence Interval for each sample
xq <- apply(x,1, function(r){ #theoretical se's 
    mean(r) + c(-1,1)*sd(r)/sqrt(length(r))
})
# First 4 interval estimates
xq[,1:4]
##           [,1]      [,2]      [,3]      [,4]
## [1,] 0.4979564 0.4849913 0.4887780 0.5044635
## [2,] 0.5308242 0.5183977 0.5223014 0.5383227

# Explicit calculation
mu_true <- 0.5
# Logical vector: whether the true mean is in each CI
covered <- mu_true >= xq[1, ] & mu_true <= xq[2, ]
# Empirical coverage rate
coverage_rate <- mean(covered)
cat(sprintf("Estimated coverage probability: %.2f%%\n", 100 * coverage_rate))
## Estimated coverage probability: 67.60%
```


``` r
# Visualize first N confidence intervals
N <- 100
plot.new()
plot.window(xlim = range(xq), ylim = c(0, N))
for (i in 1:N) {
  col_i <- if (covered[i]) rgb(0, 0, 0, 0.3) else rgb(1, 0, 0, 0.5)
  segments(xq[1, i], i, xq[2, i], i, col = col_i, lwd = 2)
}
abline(v = mu_true, col = "blue", lwd = 2)
axis(1)
title("Visualizing CI Coverage (Red = Missed)")
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-86-1.png" width="672" />

This differs from a **pointwise inclusion frequency interval**

``` r
# Frequency each point was in an interval
bks <- seq(0,1,by=.01)
xcovr <- sapply(bks, function(b){
    bl <- b >= xq[1,]
    bu <- b <= xq[2,]
    mean( bl & bu )
})
# 50\% Coverage
c_ul <- range(bks[xcovr>=.5])
c_ul # 50% confidence interval
## [1] 0.49 0.51

plot.new()
plot.window(xlim=c(0,1), ylim=c(0,1))
polygon( c(bks, rev(bks)), c(xcovr, xcovr*0), col=grey(.5,.5), border=NA)
mtext('Frequency each value was in an interval',2, line=2.5)
axis(1)
axis(2)
abline(h=.5, lwd=2)
segments(c_ul,0,c_ul,.5, lty=2)
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-87-1.png" width="672" />


## Resampling

Often, we only have one sample. How then can we estimate the sampling distribution of a statistic? 

``` r
sample_dat <- USArrests$Murder
mean(sample_dat)
## [1] 7.788
```

We can "resample" our data. *Hesterberg (2015)* provides a nice illustration of the idea. The two most basic versions are the jackknife and the bootstrap, which are discussed below.



<img src="02-BasicStats_files/figure-html/unnamed-chunk-90-1.png" width="672" />

#### **Jackknife Distribution**. {-}
Here, we compute all "leave-one-out" estimates. Specifically, for a dataset with $n$ observations, the jackknife uses $n-1$ observations other than $i$ for each unique subsample. Taking the mean, for example, we have 
\begin{itemize}
\item jackknifed estimates: $\overline{x}^{Jack}_{i}=\frac{1}{n-1} \sum_{j \neq i}^{n-1} X_{j}$
\item mean of the jackknife: $\overline{x}^{Jack}=\frac{1}{n} \sum_{i}^{n} \overline{x}^{Jack}_{i}$.
\item standard error of the jackknife: $\widehat{\sigma}^{Jack}= \sqrt{ \frac{1}{n} \sum_{i}^{n} \left[\overline{x}^{Jack}_{i} - \overline{x}^{Jack} \right]^2 }$.
\end{itemize}



``` r
sample_dat <- USArrests$Murder
sample_mean <- mean(sample_dat)

# Jackknife Estimates
n <- length(sample_dat)
Jmeans <- sapply(1:n, function(i){
    dati <- sample_dat[-i]
    mean(dati)
})
hist(Jmeans, breaks=25, border=NA,
    main='', xlab=expression(bar(X)[-i]))
abline(v=sample_mean, col='red', lty=2)
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-91-1.png" width="672" />

#### **Bootstrap Distribution**. {-}
Here, we draw $n$ observations with replacement from the original data to create a bootstrap sample and calculate a statistic. Each bootstrap sample $b=1...B$ uses a random set of observations (denoted $N_{b}$) to compute a statistic. We repeat that many times, say $B=9999$, to estimate the sampling distribution. Consider the sample mean as an example;
\begin{itemize}
\item bootstrap estimate: $\overline{x}^{Boot}_{b}= \frac{1}{n} \sum_{i \in N_b} X_{i} $
\item mean of the bootstrap: $\overline{x}^{Boot}= \frac{1}{B} \sum_{b} \overline{x}^{Boot}_{b}$.
\item standard error of the bootstrap: $\widehat{\sigma}^{Boot}= \sqrt{ \frac{1}{B} \sum_{b=1}^{B} \left[\overline{x}^{Boot}_{b} - \overline{x}^{Boot} \right]^2 }$.
\end{itemize}



``` r
# Bootstrap estimates
set.seed(2)
Bmeans <- sapply(1:10^4, function(i) {
    dat_b <- sample(sample_dat, replace=T) # c.f. jackknife
    mean(dat_b)
})

hist(Bmeans, breaks=25, border=NA,
    main='', xlab=expression(bar(X)[b]))
abline(v=sample_mean, col='red', lty=2)
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-92-1.png" width="672" />

**Caveat**. Note that we do not use the mean of the bootstrap or jackknife statistics as a replacement for the original estimate. This is because the bootstrap and jackknife distributions are centered at the observed statistic, not the population parameter. (The bootstrapped mean is centered at the sample mean, not the population mean.) This means that we cannot use the bootstrap to improve on $\overline{x}$; no matter how many bootstrap samples we take. We can, however, use the jackknife and bootstrap to estimate sampling variability.


#### **Intervals**. {-}
Note that both methods provide imperfect estimates, and can give different numbers. Percentiles of jackknife resamples are systematically less variable than they should be. Until you know more, a conservative approach is to take the larger estimate.


``` r
# Boot CI
boot_ci <- quantile(Bmeans, probs=c(.025, .975))
boot_ci
##    2.5%   97.5% 
## 6.58200 8.97005

# Jack CI
jack_ci <- quantile(Jmeans, probs=c(.025, .975))
jack_ci
##     2.5%    97.5% 
## 7.621582 7.904082

# more conservative estimate
ci_est <- boot_ci
```

Also note that the *standard deviation* refers to variance within a single sample, and is hence different from the standard error. Nonetheless, they can both be used to estimate the variability of a statistic.

``` r
boot_se <- sd(Bmeans)

sample_sd <- sd(sample_dat)

c(boot_se, sample_sd/sqrt(n))
## [1] 0.6056902 0.6159621
```

#### **Value of More Data**.{-}
Each additional data point you have provides more information, which ultimately decreases the standard error of your estimates. However, it does so at a decreasing rate (known in economics as diminishing returns).


``` r
Nseq <- seq(1,100, by=1) # Sample sizes
B <- 1000 # Number of draws per sample

SE <- sapply(Nseq, function(n){
    sample_statistics <- sapply(1:B, function(b){
        x <- rnorm(n) # Sample of size N
        quantile(x,probs=.4) # Statistic
    })
    sd(sample_statistics)
})

par(mfrow=c(1,2))
plot(Nseq, SE, pch=16, col=grey(0,.5),
    main='Absolute Gain', font.main=1,
    ylab='standard error', xlab='sample size')
plot(Nseq[-1], abs(diff(SE)), pch=16, col=grey(0,.5),
    main='Marginal Gain', font.main=1,
    ylab='decrease in standard error', xlab='sample size')
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-95-1.png" width="672" />


## Further Reading

See 

* https://www.r-bloggers.com/2025/02/bootstrap-vs-standard-error-confidence-intervals/


# Hypothesis Tests
***

## Basic Ideas

In this section, we test hypotheses using *data-driven* methods that assume much less about the data generating process. There are two main ways to conduct a hypothesis test to do so: inverting a confidence interval and imposing the null.

#### **Invert a CI**.{-}
One main way to conduct hypothesis tests is to examine whether a confidence interval contains a hypothesized value. We then use this decision rule

* reject the null if value falls outside of the interval
* fail to reject the null if value falls inside of the interval


``` r
sample_dat <- USArrests$Murder
sample_mean <- mean(sample_dat)

n <- length(sample_dat)
Jmeans <- sapply(1:n, function(i){
    dati <- sample_dat[-i]
    mean(dati)
})
hist(Jmeans, breaks=25,
    border=NA, xlim=c(7.5,8.1),
    main='', xlab=expression( bar(X)[-i]))
# CI
ci_95 <- quantile(Jmeans, probs=c(.025, .975))
abline(v=ci_95, lwd=2)
# H0: mean=8
abline(v=8, col=2, lwd=2)
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-96-1.png" width="672" />

#### **Impose the Null**. {-}
We can also compute a *null distribution*: the sampling distribution of the statistic under the null hypothesis (assuming your null hypothesis was true). We use the bootstrap to loop through a large number of "resamples". In each iteration of the loop, we impose the null hypothesis and re-estimate the statistic of interest. We then calculate the range of the statistic across all resamples and compare how extreme the original value we observed is. We use a 95% confidence interval of the null distribution to create a *rejection region*.

``` r
sample_dat <- USArrests$Murder
sample_mean <- mean(sample_dat)

# Bootstrap NULL: mean=8
set.seed(1)
Bmeans0 <- sapply(1:10^4, function(i) {
    dat_b <- sample(sample_dat, replace=T) 
    mean_b <- mean(dat_b) + (8 - sample_mean) # impose the null by recentering
    return(mean_b)
})
hist(Bmeans0, breaks=25, border=NA,
    main='', xlab=expression( bar(X)[b]) )
ci_95 <- quantile(Bmeans0, probs=c(.025, .975)) # critical region
abline(v=ci_95, lwd=2)
abline(v=sample_mean, lwd=2, col=2)
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-97-1.png" width="672" />



## Default Statistics

#### **p-values**.{-}
This is the frequency you would see something as extreme as your statistic when sampling from the null distribution.

There are three associated tests: the two-sided test (observed statistic is extremely high or low) or one of the one-sided tests (observed statistic is extremely low, observed statistic is extremely high). E.g.

* $HA​: \bar{X} > 8$ implies a right tail test
* $HA: \bar{X} < 8$ implies a left tail test
* $HA​: \bar{X} \neq 8$ implies a two tail test

In any case, typically "p<.05: statistically significant" and "p>.05: not statistically significant".


One sided example

``` r
# One-Sided Test, ALTERNATIVE: mean > 8
# Prob( boot0_means > sample_mean) 
Fhat0 <- ecdf(Bmeans0) # Right tail
plot(Fhat0,
    xlab=expression( beta[b] ),
    main='Null Bootstrap Distribution for means', font.main=1)
abline(v=sample_mean, col='red')
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-98-1.png" width="672" />

``` r

p <- 1- Fhat0(sample_mean) #Right Tail
if(p >.05){
    message('fail to reject the null that sample_mean=8, at the 5% level')
} else {
    message('reject the null that sample_mean=8 in favor of >8, at the 5% level')
}
```

Two sided example

``` r
# Two-Sided Test, ALTERNATIVE: mean < 8 or mean >8
# Prob(boot0_means > sample_mean or -boot0_means < sample_mean)

Fhat0 <- ecdf(Bmeans0)
p_left <- Fhat0(sample_mean) #Left Tail
p_right <- 1 - Fhat0(sample_mean) #Right Tail
p <- 2*min(p_left, p_right)

if(p >.05){
    message('fail to reject the null that sample_mean=8 at the 5% level')
} else {
    message('reject the null that sample_mean=8 in favor of either <8 or >8 at the 5% level')
}
```


#### **t-values**. {-}
A t-value standardizes the statistic you are using for hypothesis testing:
$$ t = (\hat{\mu} - \mu_{0}) / \hat{s_{\mu}} $$

``` r
jack_se <- sd(Jmeans)
mean0 <- 8
jack_t <- (sample_mean - mean0)/jack_se

# Note that you can also use a corrected se
# jack_se <- sqrt((n-1)/n) * sd(Jmeans)
```
There are several benefits to this:

* makes the statistic comparable across different studies
* makes the null distribution not depend on theoretical parameters ($\sigma$)
* makes the null distribution theoretically known asymptotically (approximately)

The last point implies we are dealing with a symmetric distributions: $Prob( t_{boot} > t ~\text{or}~ t_{boot} < -t) = Prob( |t| < |t_{boot}| )$.^[In another statistics class, you will learn the math behind the null t-distribution. In this class, we skip this because we can simply bootstrap the t-statistic too.]


``` r
set.seed(1)
boot_t0 <- sapply(1:10^3, function(i) {
    dat_b <- sample(sample_dat, replace=T) 
    mean_b <- mean(dat_b) + (8 - sample_mean) # impose the null by recentering
    # jack ses
    jack_se_b <- sd( sapply(1:length(dat_b), function(i){
        mean(dat_b[-i])
    }) )
    jack_t <- (mean_b - mean0)/jack_se_b
})

# Two Sided Test
Fhat0 <- ecdf(abs(boot_t0))
plot(Fhat0, xlim=range(boot_t0, jack_t),
    xlab=expression( abs(hat(t)[b]) ),
    main='Null Bootstrap Distribution for t', font.main=1)
abline(v=abs(jack_t), col='red')
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-101-1.png" width="672" />

``` r
p <- 1 - Fhat0( abs(jack_t) ) 
p
## [1] 0.727

if(p >.05){
    message('fail to reject the null that sample_mean=8, at the 5% level')
} else {
    message('reject the null that sample_mean=8 in favor of either <8 or >8, at the 5% level')
}
```


## Two-Sample Differences

Suppose we have 2 samples of data. 

Each $X_{is}$ is an individual observation $i$ from the sample $s=1,2$. (For example, the wages for men and women in Canada. For another example, homicide rates in two different American states.)


``` r
library(wooldridge)
x1 <- wage1[wage1$educ == 15, 'wage']
x2 <- wage1[wage1$educ == 16, 'wage']
```

For simplicity, we will assume that each $X_{is}$ is an independent observation. 


``` r
# Sample 1
n1 <- 100
x1 <- rnorm(n1, 0, 2)
# Sample 2
n2 <- 80
x2 <- rnorm(n2, 1, 1)

par(mfrow=c(1,2))
bks <- seq(-7,7, by=.5)
hist(x1, border=NA, breaks=bks,
    main='Sample 1', font.main=1)

hist(x2, border=NA, breaks=bks, 
    main='Sample 2', font.main=1)
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-103-1.png" width="672" />

There may be several differences between these samples. Often, the first summary statistic we investigate is the difference in means. 

#### **Equal Means**. {-}
We often want to know if the means of different sample are different in . To test this hypothesis, we compute the sample mean $\overline{X}_{s}$ over all observations in each sample and then examine the differences term
\begin{eqnarray} 
D = \overline{X}_{1} - \overline{X}_{2},
\end{eqnarray}
with a null hypothesis of $D=0$.


``` r
# Differences between means
m1 <- mean(x1)
m2 <- mean(x2)
d <- m1-m2
    
# Bootstrap Distribution
boot_d <- sapply(1:10^4, function(b){
    x1_b <- sample(x1, replace=T)
    x2_b <- sample(x2, replace=T)
    m1_b <- mean(x1_b)
    m2_b <- mean(x2_b)
    d_b <- m1_b - m2_b
    return(d_b)
})
hist(boot_d, border=NA, font.main=1,
    main='Difference in Means')

# 2-Sided Test
boot_ci <- quantile(boot_d, probs=c(.025, .975))
abline(v=boot_ci, lwd=2)
abline(v=0, lwd=2, col=2)
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-104-1.png" width="672" />

``` r

# p-value
1 - ecdf(boot_d)(0)
## [1] 0
```

Just as with one sample tests, we can standardize $D$ into a $t$ statistic. In which case, we can easily compute one or two sided hypothesis tests. Note, however, that we have to compute the standard error for the difference statistic, which is a bit more complicated. 

``` r
se_hat <- sqrt(var(x1)/n1 + var(x2)/n2);
t_obs <- d/se_hat
```

#### **Other Differences**. {-}
The above procedure generalized from differences in "means" to other statistics like "quantiles".


``` r
# Bootstrap Distribution Function
boot_fun <- function( fun, B=10^4, ...){
    boot_d <- sapply(1:B, function(b){
        x1_b <- sample(x1, replace=T)
        x2_b <- sample(x2, replace=T)
        f1_b <- fun(x1_b, ...)
        f2_b <- fun(x2_b, ...)
        d_b <- f1_b - f2_b
        return(d_b)
    })
    return(boot_d)
}

# 2-Sided Test for Median Differences
# d <- median(x2) - median(x1)
boot_d <- boot_fun(median)
hist(boot_d, border=NA, font.main=1,
    main='Difference in Medians')
abline(v=quantile(boot_d, probs=c(.025, .975)), lwd=2)
abline(v=0, lwd=2, col=2)
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-106-1.png" width="672" />

``` r
1 - ecdf(boot_d)(0)
## [1] 0
```

Note that these estimates suffer from a finite-sample bias, which we can correct for. Also note that bootstrap tests can perform poorly with highly unequal variances or skewed data.


``` r
# 2-Sided Test for SD Differences
#d <- sd(x2) - sd(x1)
boot_d <- boot_fun(sd)
hist(boot_d, border=NA, font.main=1,
    main='Difference in Standard Deviations')
abline(v=quantile(boot_d, probs=c(.025, .975)), lwd=2)
abline(v=0, lwd=2, col=2)
1 - ecdf(boot_d)(0)


# Try any function!
# boot_fun( function(xs) { IQR(xs)/median(xs) } )
```

## Further Reading

* https://learningstatisticswithr.com/book/hypothesistesting.html
* https://okanbulut.github.io/rbook/part5.html


# Data Analysis
***


## Inputs

#### **Reading Data**. {-}

The first step in data analysis is getting data into R. There are many ways to do this, depending on your data structure. Perhaps the most common case is reading in a csv file.


``` r
# Read in csv (downloaded from online)
# download source 'http://www.stern.nyu.edu/~wgreene/Text/Edition7/TableF19-3.csv'
# download destination '~/TableF19-3.csv'
read.csv('~/TableF19-3.csv')
 
# Can read in csv (directly from online)
# dat_csv <- read.csv('http://www.stern.nyu.edu/~wgreene/Text/Edition7/TableF19-3.csv')
```

Reading in other types of data can require the use of "packages". For example, the "wooldridge" package contains datasets on crime. To use this data, we must first install the package on our computer. Then, to access the data, we must first load the package.


``` r
# Install R Data Package and Load in
install.packages('wooldridge') # only once
library(wooldridge) # anytime you want to use the data

data('crime2') 
data('crime4')
```

We can use packages to access many different types of data. To read in a Stata data file, for example, we can use the "haven" package.

``` r
# Read in stata data file from online
#library(haven)
#dat_stata <- read_dta('https://www.ssc.wisc.edu/~bhansen/econometrics/DS2004.dta')
#dat_stata <- as.data.frame(dat_stata)

# For More Introductory Econometrics Data, see 
# https://www.ssc.wisc.edu/~bhansen/econometrics/Econometrics%20Data.zip
# https://pages.stern.nyu.edu/~wgreene/Text/Edition7/tablelist8new.htm
# R packages: wooldridge, causaldata, Ecdat, AER, ....
```


#### **Cleaning Data**. {-}

Data transformation is often necessary before analysis, so remember to be careful and check your code is doing what you want. (If you have large datasets, you can always test out the code on a sample.)


``` r
# Function to Create Sample Datasets
make_noisy_data <- function(n, b=0){
    # Simple Data Generating Process
    x <- seq(1,10, length.out=n) 
    e <- rnorm(n, mean=0, sd=10)
    y <- b*x + e 
    # Obervations
    xy_mat <- data.frame(ID=seq(x), x=x, y=y)
    return(xy_mat)
}

# Two simulated datasets
dat1 <- make_noisy_data(6)
dat2 <- make_noisy_data(6)

# Merging data in long format
dat_merged_long <- rbind(
    cbind(dat1,DF=1),
    cbind(dat2,DF=2))
```

Now suppose we want to transform into wide format

``` r
# Merging data in wide format, First Attempt
dat_merged_wide <- cbind( dat1, dat2)
names(dat_merged_wide) <- c(paste0(names(dat1),'.1'), paste0(names(dat2),'.2'))

# Merging data in wide format, Second Attempt
# higher performance
dat_merged_wide2 <- merge(dat1, dat2,
    by='ID', suffixes=c('.1','.2'))
## CHECK they are the same.
identical(dat_merged_wide, dat_merged_wide2)
## [1] FALSE
# Inspect any differences

# Merging data in wide format, Third Attempt with dedicated package
# (highest performance but with new type of object)
library(data.table)
dat_merged_longDT <- as.data.table(dat_merged_long)
dat_melted <- melt(dat_merged_longDT, id.vars=c('ID', 'DF'))
dat_merged_wide3 <- dcast(dat_melted, ID~DF+variable)

## CHECK they are the same.
identical(dat_merged_wide, dat_merged_wide3)
## [1] FALSE
```

Often, however, we ultimately want data in long format

``` r
# Merging data in long format, Second Attempt with dedicated package 
dat_melted2 <- melt(dat_merged_wide3, measure=c("1_x","1_y","2_x","2_y"))
melt_vars <- strsplit(as.character(dat_melted2$variable),'_')
dat_melted2$DF <- sapply(melt_vars, `[[`,1)
dat_melted2$variable <- sapply(melt_vars, `[[`,2)
dat_merged_long2 <- dcast(dat_melted2, DF+ID~variable)
dat_merged_long2 <- as.data.frame(dat_merged_long2)

## CHECK they are the same.
identical( dat_merged_long2, dat_merged_long)
## [1] FALSE

# Further Inspect
dat_merged_long2 <- dat_merged_long2[,c('ID','x','y','DF')]
mapply( identical, dat_merged_long2, dat_merged_long)
##    ID     x     y    DF 
##  TRUE  TRUE  TRUE FALSE
```

For more tips, see https://raw.githubusercontent.com/rstudio/cheatsheets/main/data-import.pdf and https://cran.r-project.org/web/packages/data.table/vignettes/datatable-reshape.html
<!--\url{https://github.com/rstudio/cheatsheets/raw/master/data-transformation.pdf}-->


## Outputs

#### **Polishing**.{-}

Your first figures are typically standard.


``` r
# Random Data
x <- seq(1, 10, by=.0002)
e <- rnorm(length(x), mean=0, sd=1)
y <- .25*x + e 

# First Drafts
# qqplot(x, y)
# plot(x, y)
```

Edit your plot to focus on the most useful information. For others to easily comprehend your work, you must also polish the plot.


``` r
# Second Draft: Focus
# (In this example: comparing shapes)
xs <- scale(x)
ys <- scale(y)
# qqplot(xs, ys)

# Third Draft: Polish
qqplot(ys, xs, 
    xlab=expression('['~X-bar(X)~'] /'~s[X]),
    ylab=expression('['~Y-bar(Y)~'] /'~s[Y]),
    pch=16, cex=.5, col=grey(0,.2))
abline(a=0, b=1, lty=2)
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-115-1.png" width="672" />

When polishing, you must do two things

* Add details that are necessary to understand the figure
* Remove unnecessary details (see e.g., <https://www.edwardtufte.com/notebook/chartjunk/> and <https://www.biostat.wisc.edu/~kbroman/topten_worstgraphs/>)


``` r
# Another Example
xy_dat <- data.frame(x=x, y=y)
par(fig=c(0,1,0,0.9), new=F)
plot(y~x, xy_dat, pch=16, col=rgb(0,0,0,.05), cex=.5,
    xlab='', ylab='') # Format Axis Labels Seperately
mtext( 'y=0.25 x + e\n e ~ standard-normal', 2, line=2.2)
mtext( expression(x%in%~'[0,10]'), 1, line=2.2)

abline( lm(y~x, data=xy_dat), lty=2)

title('Plot with good features, but too excessive in several ways',
    adj=0, font.main=1)

# Outer Legend (https://stackoverflow.com/questions/3932038/)
outer_legend <- function(...) {
  opar <- par(fig=c(0, 1, 0, 1), oma=c(0, 0, 0, 0), 
    mar=c(0, 0, 0, 0), new=TRUE)
  on.exit(par(opar))
  plot(0, 0, type='n', bty='n', xaxt='n', yaxt='n')
  legend(...)
}
outer_legend('topright', legend='single data point',
    title='do you see the normal distribution?',
    pch=16, col=rgb(0,0,0,.1), cex=1, bty='n')
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-116-1.png" width="672" />

For useful tips, see C. Wilke (2019) "Fundamentals of Data Visualization: A Primer on Making Informative and
Compelling Figures" https://clauswilke.com/dataviz/

#### **Saving**. {-}
You can export figures with specific dimensions

``` r
pdf( 'Figures/plot_example.pdf', height=5, width=5)
# plot goes here
dev.off()
```
For plotting math, see
https://astrostatistics.psu.edu/su07/R/html/grDevices/html/plotmath.html and 
https://library.virginia.edu/data/articles/mathematical-annotation-in-r

For exporting options, see `?pdf`.
For saving other types of files, see `png("*.png")`, `tiff("*.tiff")`, and  `jpeg("*.jpg")`

For some things to avoid, see https://www.data-to-viz.com/caveats.html

#### **Interactive Figures**. {-}

**Histograms**. See https://plotly.com/r/histograms/

``` r
pop_mean <- mean(USArrests$UrbanPop)
murder_lowpop <- USArrests[USArrests$UrbanPop< pop_mean,'Murder']
murder_highpop <- USArrests[USArrests$UrbanPop>= pop_mean,'Murder']

library(plotly)
fig <- plot_ly(alpha=0.6, 
    hovertemplate="%{y}")
fig <- fig %>% add_histogram(murder_lowpop, name='Low Pop. (< Mean)')
fig <- fig %>% add_histogram(murder_highpop, name='High Pop (>= Mean)')
fig <- fig %>% layout(barmode="stack") # barmode="overlay"
fig <- fig %>% layout(
    title="Crime and Urbanization in America 1975",
    xaxis = list(title='Murders Arrests per 100,000 People'),
    yaxis = list(title='Number of States'),
    legend=list(title=list(text='<b> % Urban Pop. </b>'))
)
fig
```


```{=html}
<div class="plotly html-widget html-fill-item" id="htmlwidget-8150a7413303e1a6c8f6" style="width:672px;height:480px;"></div>
<script type="application/json" data-for="htmlwidget-8150a7413303e1a6c8f6">{"x":{"visdat":{"44ee650e37a1":["function () ","plotlyVisDat"]},"cur_data":"44ee650e37a1","attrs":{"44ee650e37a1":{"hovertemplate":"%{y}","alpha":0.59999999999999998,"alpha_stroke":1,"sizes":[10,100],"spans":[1,20],"x":[13.199999999999999,10,8.8000000000000007,17.399999999999999,2.6000000000000001,7.2000000000000002,2.2000000000000002,9.6999999999999993,2.1000000000000001,16.100000000000001,6,4.2999999999999998,2.1000000000000001,13,0.80000000000000004,14.4,3.7999999999999998,13.199999999999999,2.2000000000000002,8.5,5.7000000000000002,6.7999999999999998],"type":"histogram","name":"Low Pop. (< Mean)","inherit":true},"44ee650e37a1.1":{"hovertemplate":"%{y}","alpha":0.59999999999999998,"alpha_stroke":1,"sizes":[10,100],"spans":[1,20],"x":[8.0999999999999996,9,7.9000000000000004,3.2999999999999998,5.9000000000000004,15.4,5.2999999999999998,10.4,6,15.4,11.300000000000001,4.4000000000000004,12.1,2.7000000000000002,9,12.199999999999999,7.4000000000000004,11.4,11.1,7.2999999999999998,6.5999999999999996,4.9000000000000004,6.2999999999999998,3.3999999999999999,12.699999999999999,3.2000000000000002,4,2.6000000000000001],"type":"histogram","name":"High Pop (>= Mean)","inherit":true}},"layout":{"margin":{"b":40,"l":60,"t":25,"r":10},"barmode":"stack","title":"Crime and Urbanization in America 1975","xaxis":{"domain":[0,1],"automargin":true,"title":"Murders Arrests per 100,000 People"},"yaxis":{"domain":[0,1],"automargin":true,"title":"Number of States"},"legend":{"title":{"text":"<b> % Urban Pop. <\/b>"}},"hovermode":"closest","showlegend":true},"source":"A","config":{"modeBarButtonsToAdd":["hoverclosest","hovercompare"],"showSendToCloud":false},"data":[{"hovertemplate":["%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}"],"x":[13.199999999999999,10,8.8000000000000007,17.399999999999999,2.6000000000000001,7.2000000000000002,2.2000000000000002,9.6999999999999993,2.1000000000000001,16.100000000000001,6,4.2999999999999998,2.1000000000000001,13,0.80000000000000004,14.4,3.7999999999999998,13.199999999999999,2.2000000000000002,8.5,5.7000000000000002,6.7999999999999998],"type":"histogram","name":"Low Pop. (< Mean)","marker":{"color":"rgba(31,119,180,0.6)","line":{"color":"rgba(31,119,180,1)"}},"error_y":{"color":"rgba(31,119,180,0.6)"},"error_x":{"color":"rgba(31,119,180,0.6)"},"xaxis":"x","yaxis":"y","frame":null},{"hovertemplate":["%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}"],"x":[8.0999999999999996,9,7.9000000000000004,3.2999999999999998,5.9000000000000004,15.4,5.2999999999999998,10.4,6,15.4,11.300000000000001,4.4000000000000004,12.1,2.7000000000000002,9,12.199999999999999,7.4000000000000004,11.4,11.1,7.2999999999999998,6.5999999999999996,4.9000000000000004,6.2999999999999998,3.3999999999999999,12.699999999999999,3.2000000000000002,4,2.6000000000000001],"type":"histogram","name":"High Pop (>= Mean)","marker":{"color":"rgba(255,127,14,0.6)","line":{"color":"rgba(255,127,14,1)"}},"error_y":{"color":"rgba(255,127,14,0.6)"},"error_x":{"color":"rgba(255,127,14,0.6)"},"xaxis":"x","yaxis":"y","frame":null}],"highlight":{"on":"plotly_click","persistent":false,"dynamic":false,"selectize":false,"opacityDim":0.20000000000000001,"selected":{"opacity":1},"debounce":0},"shinyEvents":["plotly_hover","plotly_click","plotly_selected","plotly_relayout","plotly_brushed","plotly_brushing","plotly_clickannotation","plotly_doubleclick","plotly_deselect","plotly_afterplot","plotly_sunburstclick"],"base_url":"https://plot.ly"},"evals":[],"jsHooks":[]}</script>
```


**Boxplots**. See https://plotly.com/r/box-plots/

``` r
USArrests$ID <- rownames(USArrests)
fig <- plot_ly(USArrests,
    y=~Murder, color=~cut(UrbanPop,4),
    alpha=0.6, type="box",
    pointpos=0, boxpoints = 'all',
    hoverinfo='text',    
    text = ~paste('<b>', ID, '</b>',
        "<br>Urban  :", UrbanPop,
        "<br>Assault:", Assault,
        "<br>Murder :", Murder))    
fig <- layout(fig,
    showlegend=FALSE,
    title='Crime and Urbanization in America 1975',
    xaxis = list(title = 'Percent of People in an Urban Area'),
    yaxis = list(title = 'Murders Arrests per 100,000 People'))
fig
```


```{=html}
<div class="plotly html-widget html-fill-item" id="htmlwidget-4aa3c4b3294103b01ec4" style="width:672px;height:480px;"></div>
<script type="application/json" data-for="htmlwidget-4aa3c4b3294103b01ec4">{"x":{"visdat":{"44ee75d50296":["function () ","plotlyVisDat"]},"cur_data":"44ee75d50296","attrs":{"44ee75d50296":{"y":{},"pointpos":0,"boxpoints":"all","hoverinfo":"text","text":{},"color":{},"alpha":0.59999999999999998,"alpha_stroke":1,"sizes":[10,100],"spans":[1,20],"type":"box"}},"layout":{"margin":{"b":40,"l":60,"t":25,"r":10},"showlegend":false,"title":"Crime and Urbanization in America 1975","xaxis":{"domain":[0,1],"automargin":true,"title":"Percent of People in an Urban Area"},"yaxis":{"domain":[0,1],"automargin":true,"title":"Murders Arrests per 100,000 People"},"hovermode":"closest"},"source":"A","config":{"modeBarButtonsToAdd":["hoverclosest","hovercompare"],"showSendToCloud":false},"data":[{"fillcolor":"rgba(102,194,165,0.6)","y":[16.100000000000001,13,0.80000000000000004,3.7999999999999998,2.2000000000000002,5.7000000000000002],"pointpos":0,"boxpoints":"all","hoverinfo":["text","text","text","text","text","text"],"text":["<b> Mississippi <\/b> <br>Urban  : 44 <br>Assault: 259 <br>Murder : 16.1","<b> North Carolina <\/b> <br>Urban  : 45 <br>Assault: 337 <br>Murder : 13","<b> North Dakota <\/b> <br>Urban  : 44 <br>Assault: 45 <br>Murder : 0.8","<b> South Dakota <\/b> <br>Urban  : 45 <br>Assault: 86 <br>Murder : 3.8","<b> Vermont <\/b> <br>Urban  : 32 <br>Assault: 48 <br>Murder : 2.2","<b> West Virginia <\/b> <br>Urban  : 39 <br>Assault: 81 <br>Murder : 5.7"],"type":"box","name":"(31.9,46.8]","marker":{"color":"rgba(102,194,165,0.6)","line":{"color":"rgba(102,194,165,1)"}},"line":{"color":"rgba(102,194,165,1)"},"xaxis":"x","yaxis":"y","frame":null},{"fillcolor":"rgba(252,141,98,0.6)","y":[13.199999999999999,10,8.8000000000000007,17.399999999999999,2.6000000000000001,2.2000000000000002,9.6999999999999993,2.1000000000000001,6,2.1000000000000001,14.4,13.199999999999999,6.7999999999999998],"pointpos":0,"boxpoints":"all","hoverinfo":["text","text","text","text","text","text","text","text","text","text","text","text","text"],"text":["<b> Alabama <\/b> <br>Urban  : 58 <br>Assault: 236 <br>Murder : 13.2","<b> Alaska <\/b> <br>Urban  : 48 <br>Assault: 263 <br>Murder : 10","<b> Arkansas <\/b> <br>Urban  : 50 <br>Assault: 190 <br>Murder : 8.8","<b> Georgia <\/b> <br>Urban  : 60 <br>Assault: 211 <br>Murder : 17.4","<b> Idaho <\/b> <br>Urban  : 54 <br>Assault: 120 <br>Murder : 2.6","<b> Iowa <\/b> <br>Urban  : 57 <br>Assault: 56 <br>Murder : 2.2","<b> Kentucky <\/b> <br>Urban  : 52 <br>Assault: 109 <br>Murder : 9.7","<b> Maine <\/b> <br>Urban  : 51 <br>Assault: 83 <br>Murder : 2.1","<b> Montana <\/b> <br>Urban  : 53 <br>Assault: 109 <br>Murder : 6","<b> New Hampshire <\/b> <br>Urban  : 56 <br>Assault: 57 <br>Murder : 2.1","<b> South Carolina <\/b> <br>Urban  : 48 <br>Assault: 279 <br>Murder : 14.4","<b> Tennessee <\/b> <br>Urban  : 59 <br>Assault: 188 <br>Murder : 13.2","<b> Wyoming <\/b> <br>Urban  : 60 <br>Assault: 161 <br>Murder : 6.8"],"type":"box","name":"(46.8,61.5]","marker":{"color":"rgba(252,141,98,0.6)","line":{"color":"rgba(252,141,98,1)"}},"line":{"color":"rgba(252,141,98,1)"},"xaxis":"x","yaxis":"y","frame":null},{"fillcolor":"rgba(141,160,203,0.6)","y":[5.9000000000000004,7.2000000000000002,6,15.4,11.300000000000001,12.1,2.7000000000000002,9,4.2999999999999998,11.4,7.2999999999999998,6.5999999999999996,4.9000000000000004,6.2999999999999998,8.5,4,2.6000000000000001],"pointpos":0,"boxpoints":"all","hoverinfo":["text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text"],"text":["<b> Delaware <\/b> <br>Urban  : 72 <br>Assault: 238 <br>Murder : 5.9","<b> Indiana <\/b> <br>Urban  : 65 <br>Assault: 113 <br>Murder : 7.2","<b> Kansas <\/b> <br>Urban  : 66 <br>Assault: 115 <br>Murder : 6","<b> Louisiana <\/b> <br>Urban  : 66 <br>Assault: 249 <br>Murder : 15.4","<b> Maryland <\/b> <br>Urban  : 67 <br>Assault: 300 <br>Murder : 11.3","<b> Michigan <\/b> <br>Urban  : 74 <br>Assault: 255 <br>Murder : 12.1","<b> Minnesota <\/b> <br>Urban  : 66 <br>Assault: 72 <br>Murder : 2.7","<b> Missouri <\/b> <br>Urban  : 70 <br>Assault: 178 <br>Murder : 9","<b> Nebraska <\/b> <br>Urban  : 62 <br>Assault: 102 <br>Murder : 4.3","<b> New Mexico <\/b> <br>Urban  : 70 <br>Assault: 285 <br>Murder : 11.4","<b> Ohio <\/b> <br>Urban  : 75 <br>Assault: 120 <br>Murder : 7.3","<b> Oklahoma <\/b> <br>Urban  : 68 <br>Assault: 151 <br>Murder : 6.6","<b> Oregon <\/b> <br>Urban  : 67 <br>Assault: 159 <br>Murder : 4.9","<b> Pennsylvania <\/b> <br>Urban  : 72 <br>Assault: 106 <br>Murder : 6.3","<b> Virginia <\/b> <br>Urban  : 63 <br>Assault: 156 <br>Murder : 8.5","<b> Washington <\/b> <br>Urban  : 73 <br>Assault: 145 <br>Murder : 4","<b> Wisconsin <\/b> <br>Urban  : 66 <br>Assault: 53 <br>Murder : 2.6"],"type":"box","name":"(61.5,76.2]","marker":{"color":"rgba(141,160,203,0.6)","line":{"color":"rgba(141,160,203,1)"}},"line":{"color":"rgba(141,160,203,1)"},"xaxis":"x","yaxis":"y","frame":null},{"fillcolor":"rgba(231,138,195,0.6)","y":[8.0999999999999996,9,7.9000000000000004,3.2999999999999998,15.4,5.2999999999999998,10.4,4.4000000000000004,12.199999999999999,7.4000000000000004,11.1,3.3999999999999999,12.699999999999999,3.2000000000000002],"pointpos":0,"boxpoints":"all","hoverinfo":["text","text","text","text","text","text","text","text","text","text","text","text","text","text"],"text":["<b> Arizona <\/b> <br>Urban  : 80 <br>Assault: 294 <br>Murder : 8.1","<b> California <\/b> <br>Urban  : 91 <br>Assault: 276 <br>Murder : 9","<b> Colorado <\/b> <br>Urban  : 78 <br>Assault: 204 <br>Murder : 7.9","<b> Connecticut <\/b> <br>Urban  : 77 <br>Assault: 110 <br>Murder : 3.3","<b> Florida <\/b> <br>Urban  : 80 <br>Assault: 335 <br>Murder : 15.4","<b> Hawaii <\/b> <br>Urban  : 83 <br>Assault: 46 <br>Murder : 5.3","<b> Illinois <\/b> <br>Urban  : 83 <br>Assault: 249 <br>Murder : 10.4","<b> Massachusetts <\/b> <br>Urban  : 85 <br>Assault: 149 <br>Murder : 4.4","<b> Nevada <\/b> <br>Urban  : 81 <br>Assault: 252 <br>Murder : 12.2","<b> New Jersey <\/b> <br>Urban  : 89 <br>Assault: 159 <br>Murder : 7.4","<b> New York <\/b> <br>Urban  : 86 <br>Assault: 254 <br>Murder : 11.1","<b> Rhode Island <\/b> <br>Urban  : 87 <br>Assault: 174 <br>Murder : 3.4","<b> Texas <\/b> <br>Urban  : 80 <br>Assault: 201 <br>Murder : 12.7","<b> Utah <\/b> <br>Urban  : 80 <br>Assault: 120 <br>Murder : 3.2"],"type":"box","name":"(76.2,91.1]","marker":{"color":"rgba(231,138,195,0.6)","line":{"color":"rgba(231,138,195,1)"}},"line":{"color":"rgba(231,138,195,1)"},"xaxis":"x","yaxis":"y","frame":null}],"highlight":{"on":"plotly_click","persistent":false,"dynamic":false,"selectize":false,"opacityDim":0.20000000000000001,"selected":{"opacity":1},"debounce":0},"shinyEvents":["plotly_hover","plotly_click","plotly_selected","plotly_relayout","plotly_brushed","plotly_brushing","plotly_clickannotation","plotly_doubleclick","plotly_deselect","plotly_afterplot","plotly_sunburstclick"],"base_url":"https://plot.ly"},"evals":[],"jsHooks":[]}</script>
```


**Scatterplots**. See https://plotly.com/r/bubble-charts/

``` r
# Simple Scatter Plot
#plot(Assault~UrbanPop, USArrests, col=grey(0,.5), pch=16,
#    cex=USArrests$Murder/diff(range(USArrests$Murder))*2,
#    main='US Murder arrests (per 100,000)')

# Scatter Plot
USArrests$ID <- rownames(USArrests)
fig <- plot_ly(
    USArrests, x = ~UrbanPop, y = ~Assault,
    mode='markers',
    type='scatter',
    hoverinfo='text',
    text = ~paste('<b>', ID, '</b>',
        "<br>Urban  :", UrbanPop,
        "<br>Assault:", Assault,
        "<br>Murder :", Murder),
    color=~Murder,
    marker=list(
        size=~Murder,
        opacity=0.5,
        showscale=T,  
        colorbar = list(title='Murder Arrests (per 100,000)')))
fig <- layout(fig,
    showlegend=F,
    title='Crime and Urbanization in America 1975',
    xaxis = list(title = 'Percent of People in an Urban Area'),
    yaxis = list(title = 'Assault Arrests per 100,000 People'))
fig
```


```{=html}
<div class="plotly html-widget html-fill-item" id="htmlwidget-eb20e9af2173ad916cf5" style="width:672px;height:480px;"></div>
<script type="application/json" data-for="htmlwidget-eb20e9af2173ad916cf5">{"x":{"visdat":{"44ee72825c43":["function () ","plotlyVisDat"]},"cur_data":"44ee72825c43","attrs":{"44ee72825c43":{"x":{},"y":{},"mode":"markers","hoverinfo":"text","text":{},"marker":{"size":{},"opacity":0.5,"showscale":true,"colorbar":{"title":"Murder Arrests (per 100,000)"}},"color":{},"alpha_stroke":1,"sizes":[10,100],"spans":[1,20],"type":"scatter"}},"layout":{"margin":{"b":40,"l":60,"t":25,"r":10},"showlegend":false,"title":"Crime and Urbanization in America 1975","xaxis":{"domain":[0,1],"automargin":true,"title":"Percent of People in an Urban Area"},"yaxis":{"domain":[0,1],"automargin":true,"title":"Assault Arrests per 100,000 People"},"hovermode":"closest"},"source":"A","config":{"modeBarButtonsToAdd":["hoverclosest","hovercompare"],"showSendToCloud":false},"data":[{"x":[58,48,80,50,91,78,77,72,80,60,83,54,83,65,57,66,52,66,51,67,85,74,66,44,70,53,62,81,56,89,70,86,45,44,75,68,67,72,87,48,45,59,80,80,32,63,73,39,66,60],"y":[236,263,294,190,276,204,110,238,335,211,46,120,249,113,56,115,109,249,83,300,149,255,72,259,178,109,102,252,57,159,285,254,337,45,120,151,159,106,174,279,86,188,201,120,48,156,145,81,53,161],"mode":"markers","hoverinfo":["text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text"],"text":["<b> Alabama <\/b> <br>Urban  : 58 <br>Assault: 236 <br>Murder : 13.2","<b> Alaska <\/b> <br>Urban  : 48 <br>Assault: 263 <br>Murder : 10","<b> Arizona <\/b> <br>Urban  : 80 <br>Assault: 294 <br>Murder : 8.1","<b> Arkansas <\/b> <br>Urban  : 50 <br>Assault: 190 <br>Murder : 8.8","<b> California <\/b> <br>Urban  : 91 <br>Assault: 276 <br>Murder : 9","<b> Colorado <\/b> <br>Urban  : 78 <br>Assault: 204 <br>Murder : 7.9","<b> Connecticut <\/b> <br>Urban  : 77 <br>Assault: 110 <br>Murder : 3.3","<b> Delaware <\/b> <br>Urban  : 72 <br>Assault: 238 <br>Murder : 5.9","<b> Florida <\/b> <br>Urban  : 80 <br>Assault: 335 <br>Murder : 15.4","<b> Georgia <\/b> <br>Urban  : 60 <br>Assault: 211 <br>Murder : 17.4","<b> Hawaii <\/b> <br>Urban  : 83 <br>Assault: 46 <br>Murder : 5.3","<b> Idaho <\/b> <br>Urban  : 54 <br>Assault: 120 <br>Murder : 2.6","<b> Illinois <\/b> <br>Urban  : 83 <br>Assault: 249 <br>Murder : 10.4","<b> Indiana <\/b> <br>Urban  : 65 <br>Assault: 113 <br>Murder : 7.2","<b> Iowa <\/b> <br>Urban  : 57 <br>Assault: 56 <br>Murder : 2.2","<b> Kansas <\/b> <br>Urban  : 66 <br>Assault: 115 <br>Murder : 6","<b> Kentucky <\/b> <br>Urban  : 52 <br>Assault: 109 <br>Murder : 9.7","<b> Louisiana <\/b> <br>Urban  : 66 <br>Assault: 249 <br>Murder : 15.4","<b> Maine <\/b> <br>Urban  : 51 <br>Assault: 83 <br>Murder : 2.1","<b> Maryland <\/b> <br>Urban  : 67 <br>Assault: 300 <br>Murder : 11.3","<b> Massachusetts <\/b> <br>Urban  : 85 <br>Assault: 149 <br>Murder : 4.4","<b> Michigan <\/b> <br>Urban  : 74 <br>Assault: 255 <br>Murder : 12.1","<b> Minnesota <\/b> <br>Urban  : 66 <br>Assault: 72 <br>Murder : 2.7","<b> Mississippi <\/b> <br>Urban  : 44 <br>Assault: 259 <br>Murder : 16.1","<b> Missouri <\/b> <br>Urban  : 70 <br>Assault: 178 <br>Murder : 9","<b> Montana <\/b> <br>Urban  : 53 <br>Assault: 109 <br>Murder : 6","<b> Nebraska <\/b> <br>Urban  : 62 <br>Assault: 102 <br>Murder : 4.3","<b> Nevada <\/b> <br>Urban  : 81 <br>Assault: 252 <br>Murder : 12.2","<b> New Hampshire <\/b> <br>Urban  : 56 <br>Assault: 57 <br>Murder : 2.1","<b> New Jersey <\/b> <br>Urban  : 89 <br>Assault: 159 <br>Murder : 7.4","<b> New Mexico <\/b> <br>Urban  : 70 <br>Assault: 285 <br>Murder : 11.4","<b> New York <\/b> <br>Urban  : 86 <br>Assault: 254 <br>Murder : 11.1","<b> North Carolina <\/b> <br>Urban  : 45 <br>Assault: 337 <br>Murder : 13","<b> North Dakota <\/b> <br>Urban  : 44 <br>Assault: 45 <br>Murder : 0.8","<b> Ohio <\/b> <br>Urban  : 75 <br>Assault: 120 <br>Murder : 7.3","<b> Oklahoma <\/b> <br>Urban  : 68 <br>Assault: 151 <br>Murder : 6.6","<b> Oregon <\/b> <br>Urban  : 67 <br>Assault: 159 <br>Murder : 4.9","<b> Pennsylvania <\/b> <br>Urban  : 72 <br>Assault: 106 <br>Murder : 6.3","<b> Rhode Island <\/b> <br>Urban  : 87 <br>Assault: 174 <br>Murder : 3.4","<b> South Carolina <\/b> <br>Urban  : 48 <br>Assault: 279 <br>Murder : 14.4","<b> South Dakota <\/b> <br>Urban  : 45 <br>Assault: 86 <br>Murder : 3.8","<b> Tennessee <\/b> <br>Urban  : 59 <br>Assault: 188 <br>Murder : 13.2","<b> Texas <\/b> <br>Urban  : 80 <br>Assault: 201 <br>Murder : 12.7","<b> Utah <\/b> <br>Urban  : 80 <br>Assault: 120 <br>Murder : 3.2","<b> Vermont <\/b> <br>Urban  : 32 <br>Assault: 48 <br>Murder : 2.2","<b> Virginia <\/b> <br>Urban  : 63 <br>Assault: 156 <br>Murder : 8.5","<b> Washington <\/b> <br>Urban  : 73 <br>Assault: 145 <br>Murder : 4","<b> West Virginia <\/b> <br>Urban  : 39 <br>Assault: 81 <br>Murder : 5.7","<b> Wisconsin <\/b> <br>Urban  : 66 <br>Assault: 53 <br>Murder : 2.6","<b> Wyoming <\/b> <br>Urban  : 60 <br>Assault: 161 <br>Murder : 6.8"],"marker":{"colorbar":{"title":"Murder Arrests (per 100,000)","ticklen":2},"cmin":0.80000000000000004,"cmax":17.399999999999999,"colorscale":[["0","rgba(68,1,84,1)"],["0.0416666666666667","rgba(70,19,97,1)"],["0.0833333333333333","rgba(72,32,111,1)"],["0.125","rgba(71,45,122,1)"],["0.166666666666667","rgba(68,58,128,1)"],["0.208333333333333","rgba(64,70,135,1)"],["0.25","rgba(60,82,138,1)"],["0.291666666666667","rgba(56,93,140,1)"],["0.333333333333333","rgba(49,104,142,1)"],["0.375","rgba(46,114,142,1)"],["0.416666666666667","rgba(42,123,142,1)"],["0.458333333333333","rgba(38,133,141,1)"],["0.5","rgba(37,144,140,1)"],["0.541666666666667","rgba(33,154,138,1)"],["0.583333333333333","rgba(39,164,133,1)"],["0.625","rgba(47,174,127,1)"],["0.666666666666667","rgba(53,183,121,1)"],["0.708333333333333","rgba(79,191,110,1)"],["0.75","rgba(98,199,98,1)"],["0.791666666666667","rgba(119,207,85,1)"],["0.833333333333333","rgba(147,214,70,1)"],["0.875","rgba(172,220,52,1)"],["0.916666666666667","rgba(199,225,42,1)"],["0.958333333333333","rgba(226,228,40,1)"],["1","rgba(253,231,37,1)"]],"showscale":true,"color":[13.199999999999999,10,8.0999999999999996,8.8000000000000007,9,7.9000000000000004,3.2999999999999998,5.9000000000000004,15.4,17.399999999999999,5.2999999999999998,2.6000000000000001,10.4,7.2000000000000002,2.2000000000000002,6,9.6999999999999993,15.4,2.1000000000000001,11.300000000000001,4.4000000000000004,12.1,2.7000000000000002,16.100000000000001,9,6,4.2999999999999998,12.199999999999999,2.1000000000000001,7.4000000000000004,11.4,11.1,13,0.80000000000000004,7.2999999999999998,6.5999999999999996,4.9000000000000004,6.2999999999999998,3.3999999999999999,14.4,3.7999999999999998,13.199999999999999,12.699999999999999,3.2000000000000002,2.2000000000000002,8.5,4,5.7000000000000002,2.6000000000000001,6.7999999999999998],"size":[13.199999999999999,10,8.0999999999999996,8.8000000000000007,9,7.9000000000000004,3.2999999999999998,5.9000000000000004,15.4,17.399999999999999,5.2999999999999998,2.6000000000000001,10.4,7.2000000000000002,2.2000000000000002,6,9.6999999999999993,15.4,2.1000000000000001,11.300000000000001,4.4000000000000004,12.1,2.7000000000000002,16.100000000000001,9,6,4.2999999999999998,12.199999999999999,2.1000000000000001,7.4000000000000004,11.4,11.1,13,0.80000000000000004,7.2999999999999998,6.5999999999999996,4.9000000000000004,6.2999999999999998,3.3999999999999999,14.4,3.7999999999999998,13.199999999999999,12.699999999999999,3.2000000000000002,2.2000000000000002,8.5,4,5.7000000000000002,2.6000000000000001,6.7999999999999998],"opacity":0.5,"line":{"colorbar":{"title":"","ticklen":2},"cmin":0.80000000000000004,"cmax":17.399999999999999,"colorscale":[["0","rgba(68,1,84,1)"],["0.0416666666666667","rgba(70,19,97,1)"],["0.0833333333333333","rgba(72,32,111,1)"],["0.125","rgba(71,45,122,1)"],["0.166666666666667","rgba(68,58,128,1)"],["0.208333333333333","rgba(64,70,135,1)"],["0.25","rgba(60,82,138,1)"],["0.291666666666667","rgba(56,93,140,1)"],["0.333333333333333","rgba(49,104,142,1)"],["0.375","rgba(46,114,142,1)"],["0.416666666666667","rgba(42,123,142,1)"],["0.458333333333333","rgba(38,133,141,1)"],["0.5","rgba(37,144,140,1)"],["0.541666666666667","rgba(33,154,138,1)"],["0.583333333333333","rgba(39,164,133,1)"],["0.625","rgba(47,174,127,1)"],["0.666666666666667","rgba(53,183,121,1)"],["0.708333333333333","rgba(79,191,110,1)"],["0.75","rgba(98,199,98,1)"],["0.791666666666667","rgba(119,207,85,1)"],["0.833333333333333","rgba(147,214,70,1)"],["0.875","rgba(172,220,52,1)"],["0.916666666666667","rgba(199,225,42,1)"],["0.958333333333333","rgba(226,228,40,1)"],["1","rgba(253,231,37,1)"]],"showscale":false,"color":[13.199999999999999,10,8.0999999999999996,8.8000000000000007,9,7.9000000000000004,3.2999999999999998,5.9000000000000004,15.4,17.399999999999999,5.2999999999999998,2.6000000000000001,10.4,7.2000000000000002,2.2000000000000002,6,9.6999999999999993,15.4,2.1000000000000001,11.300000000000001,4.4000000000000004,12.1,2.7000000000000002,16.100000000000001,9,6,4.2999999999999998,12.199999999999999,2.1000000000000001,7.4000000000000004,11.4,11.1,13,0.80000000000000004,7.2999999999999998,6.5999999999999996,4.9000000000000004,6.2999999999999998,3.3999999999999999,14.4,3.7999999999999998,13.199999999999999,12.699999999999999,3.2000000000000002,2.2000000000000002,8.5,4,5.7000000000000002,2.6000000000000001,6.7999999999999998]}},"type":"scatter","xaxis":"x","yaxis":"y","frame":null},{"x":[32,91],"y":[45,337],"type":"scatter","mode":"markers","opacity":0,"hoverinfo":"none","showlegend":false,"marker":{"colorbar":{"title":"Murder","ticklen":2},"cmin":0.80000000000000004,"cmax":17.399999999999999,"colorscale":[["0","rgba(68,1,84,1)"],["0.0416666666666667","rgba(70,19,97,1)"],["0.0833333333333333","rgba(72,32,111,1)"],["0.125","rgba(71,45,122,1)"],["0.166666666666667","rgba(68,58,128,1)"],["0.208333333333333","rgba(64,70,135,1)"],["0.25","rgba(60,82,138,1)"],["0.291666666666667","rgba(56,93,140,1)"],["0.333333333333333","rgba(49,104,142,1)"],["0.375","rgba(46,114,142,1)"],["0.416666666666667","rgba(42,123,142,1)"],["0.458333333333333","rgba(38,133,141,1)"],["0.5","rgba(37,144,140,1)"],["0.541666666666667","rgba(33,154,138,1)"],["0.583333333333333","rgba(39,164,133,1)"],["0.625","rgba(47,174,127,1)"],["0.666666666666667","rgba(53,183,121,1)"],["0.708333333333333","rgba(79,191,110,1)"],["0.75","rgba(98,199,98,1)"],["0.791666666666667","rgba(119,207,85,1)"],["0.833333333333333","rgba(147,214,70,1)"],["0.875","rgba(172,220,52,1)"],["0.916666666666667","rgba(199,225,42,1)"],["0.958333333333333","rgba(226,228,40,1)"],["1","rgba(253,231,37,1)"]],"showscale":true,"color":[0.80000000000000004,17.399999999999999],"line":{"color":"rgba(255,127,14,1)"}},"xaxis":"x","yaxis":"y","frame":null}],"highlight":{"on":"plotly_click","persistent":false,"dynamic":false,"selectize":false,"opacityDim":0.20000000000000001,"selected":{"opacity":1},"debounce":0},"shinyEvents":["plotly_hover","plotly_click","plotly_selected","plotly_relayout","plotly_brushed","plotly_brushing","plotly_clickannotation","plotly_doubleclick","plotly_deselect","plotly_afterplot","plotly_sunburstclick"],"base_url":"https://plot.ly"},"evals":[],"jsHooks":[]}</script>
```


If you have many point, you can also use a 2D histogram instead. https://plotly.com/r/2D-Histogram/.


``` r
fig <- plot_ly(
    USArrests, x = ~UrbanPop, y = ~Assault)
fig <- add_histogram2d(fig, nbinsx=25, nbinsy=25)
fig
```


#### **Tables**. {-}

You can also export tables in a variety of formats, for other software programs to easily read 

``` r
library(stargazer)
# summary statistics
stargazer(USArrests,
    type='html', 
    summary=T,
    title='Summary Statistics for USArrests')
```


<table style="text-align:center"><caption><strong>Summary Statistics for USArrests</strong></caption>
<tr><td colspan="6" style="border-bottom: 1px solid black"></td></tr><tr><td style="text-align:left">Statistic</td><td>N</td><td>Mean</td><td>St. Dev.</td><td>Min</td><td>Max</td></tr>
<tr><td colspan="6" style="border-bottom: 1px solid black"></td></tr><tr><td style="text-align:left">Murder</td><td>50</td><td>7.788</td><td>4.356</td><td>0.800</td><td>17.400</td></tr>
<tr><td style="text-align:left">Assault</td><td>50</td><td>170.760</td><td>83.338</td><td>45</td><td>337</td></tr>
<tr><td style="text-align:left">UrbanPop</td><td>50</td><td>65.540</td><td>14.475</td><td>32</td><td>91</td></tr>
<tr><td style="text-align:left">Rape</td><td>50</td><td>21.232</td><td>9.366</td><td>7.300</td><td>46.000</td></tr>
<tr><td colspan="6" style="border-bottom: 1px solid black"></td></tr></table>

You can create a basic interactive table to explore raw data.

``` r
data("USArrests")
library(reactable)
reactable(USArrests, filterable=T, highlight=T)
```


```{=html}
<div class="reactable html-widget html-fill-item" id="htmlwidget-f60e56a563f84aa3eb1d" style="width:auto;height:auto;"></div>
<script type="application/json" data-for="htmlwidget-f60e56a563f84aa3eb1d">{"x":{"tag":{"name":"Reactable","attribs":{"data":{".rownames":["Alabama","Alaska","Arizona","Arkansas","California","Colorado","Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois","Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland","Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana","Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York","North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania","Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah","Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"],"Murder":[13.2,10,8.1,8.8,9,7.9,3.3,5.9,15.4,17.4,5.3,2.6,10.4,7.2,2.2,6,9.7,15.4,2.1,11.3,4.4,12.1,2.7,16.1,9,6,4.3,12.2,2.1,7.4,11.4,11.1,13,0.8,7.3,6.6,4.9,6.3,3.4,14.4,3.8,13.2,12.7,3.2,2.2,8.5,4,5.7,2.6,6.8],"Assault":[236,263,294,190,276,204,110,238,335,211,46,120,249,113,56,115,109,249,83,300,149,255,72,259,178,109,102,252,57,159,285,254,337,45,120,151,159,106,174,279,86,188,201,120,48,156,145,81,53,161],"UrbanPop":[58,48,80,50,91,78,77,72,80,60,83,54,83,65,57,66,52,66,51,67,85,74,66,44,70,53,62,81,56,89,70,86,45,44,75,68,67,72,87,48,45,59,80,80,32,63,73,39,66,60],"Rape":[21.2,44.5,31,19.5,40.6,38.7,11.1,15.8,31.9,25.8,20.2,14.2,24,21,11.3,18,16.3,22.2,7.8,27.8,16.3,35.1,14.9,17.1,28.2,16.4,16.5,46,9.5,18.8,32.1,26.1,16.1,7.3,21.4,20,29.3,14.9,8.3,22.5,12.8,26.9,25.5,22.9,11.2,20.7,26.2,9.3,10.8,15.6]},"columns":[{"id":".rownames","name":"","type":"character","sortable":false,"filterable":false,"rowHeader":true},{"id":"Murder","name":"Murder","type":"numeric"},{"id":"Assault","name":"Assault","type":"numeric"},{"id":"UrbanPop","name":"UrbanPop","type":"numeric"},{"id":"Rape","name":"Rape","type":"numeric"}],"filterable":true,"highlight":true,"dataKey":"c49af85e0b2038b0b71caf77db2bacb3"},"children":[]},"class":"reactR_markup"},"evals":[],"jsHooks":[]}</script>
```


For further data exploration, your plots can also be made [interactive](https://r-graph-gallery.com/interactive-charts.html) via <https://plotly.com/r/>. For more details, see [examples](https://plotly-r.com/) and then [applications](https://bookdown.org/paulcbauer/applied-data-visualization/10-plotly.html).

``` r
#install.packages("plotly")
library(plotly)
```


#### **Custom Figures**. {-}

Many of the best plots are custom made (see https://www.r-graph-gallery.com/). Here are some ones that I have made over the years.

<!-- ## CONVERT IMAGES
for pdfile in *.pdf ; do 
convert -verbose -density 500  "${pdfile}" "${pdfile%.*}".png;
done
-->


<img src="./Figures_Manual/Vegetation.png" width="2400" />

<img src="./Figures_Manual/Balances_Trial.png" width="3000" />

<img src="./Figures_Manual/PopulationDensity2.png" width="3000" />

<img src="./Figures_Manual/SampleExample.png" width="1750" />

<img src="./Figures_Manual/SemiInclusive_Example.png" width="3000" />

<img src="./Figures_Manual/Stability_3.png" width="1000" />

<img src="./Figures_Manual/EvolutionaryDynamics.png" width="3000" />

<img src="./Figures_Manual/Experiment_Timeline.png" width="1750" />



## R-Markdown Reports

We will use R Markdown for communicating results to each other. Note that R and R Markdown are both languages. R studio interprets R code make statistical computations and interprets R Markdown code to produce pretty documents that contain both writing and statistics. Altogether, your project will use

* R: does statistical computations
* R Markdown: formats statistical computations for sharing
* Rstudio: graphical user interface that allows you to easily use both R and R Markdown.

Homework reports are probably the smallest document you can create. These little reports are almost entirely self-contained (showing both code and output). To make them, you will need to 

First install [Pandoc](http://pandoc.org) on your computer.

Then install any required packages

``` r
# Packages for Rmarkdown
install.packages("knitr")
install.packages("rmarkdown")

# Other packages frequently used
#install.packages("plotly") #for interactive plots
#install.packages("sf") #for spatial data
```


We will create simple reproducible reports via R Markdown.

#### **Example 1: Data Scientism**. {-}
<!-- 
**Clean workspace**.
Delete any temporary files which you do not want (or start a fresh session).

(for example *summarytable_example.txt* and *plot_example.pdf* and section *Data analysis examples: custom figures*)
-->


See [DataScientism.html](https://jadamso.github.io/Rbooks/Templates/DataScientism.html) and then create it by

* Clicking the "Code" button in the top right and then "Download Rmd"
* Open with Rstudio
* Change the name and title *to your own*, make other edits
* Then point-and-click "knit"

Alternatively,

* Download the source file from [DataScientism.Rmd](https://jadamso.github.io/Rbooks/Templates/DataScientism.Rmd)
* Change the name and title *to your own*, make other edits
* Use the console to run

``` r
rmarkdown::render('DataScientism.Rmd')
```

#### **Example 2: Homework Assignment**.  {-}
Below is a template of what homework questions (and answers) look like. Create a new *.Rmd* file from scratch and produce a *.html* file that looks similar to this:

*Problem:*
Simulate 100 random observations of the form $y=x\beta+\epsilon$ and plot the relationship. Plot and explore the data interactively via plotly, https://plotly.com/r/line-and-scatter/. Then play around with different styles, https://www.r-graph-gallery.com/13-scatter-plot.html, to best express your point.

*Solution:*
I simulate $400$ observations for $\epsilon \sim 2\times N(0,1)$ and $\beta=4$, as seen in this single chunk. Notice an upward trend.

``` r
# Simulation
n <- 100
E <- rnorm(n)
X <- seq(n)
Y <- 4*X + 2*E
# Plot
library(plotly)
dat <- data.frame(X=X,Y=Y)
plot_ly( data=dat, x=~X, y=~Y)
```


```{=html}
<div class="plotly html-widget html-fill-item" id="htmlwidget-7baeb9947b84aafaa214" style="width:672px;height:480px;"></div>
<script type="application/json" data-for="htmlwidget-7baeb9947b84aafaa214">{"x":{"visdat":{"44ee2a539726":["function () ","plotlyVisDat"]},"cur_data":"44ee2a539726","attrs":{"44ee2a539726":{"x":{},"y":{},"alpha_stroke":1,"sizes":[10,100],"spans":[1,20]}},"layout":{"margin":{"b":40,"l":60,"t":25,"r":10},"xaxis":{"domain":[0,1],"automargin":true,"title":"X"},"yaxis":{"domain":[0,1],"automargin":true,"title":"Y"},"hovermode":"closest","showlegend":false},"source":"A","config":{"modeBarButtonsToAdd":["hoverclosest","hovercompare"],"showSendToCloud":false},"data":[{"x":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100],"y":[5.5662272329299105,6.7633708549927274,9.7069593867394275,18.373641797539669,20.571335558977758,22.507098696136602,24.128031204937962,33.352954192768983,35.46518265845657,42.507159105373759,46.77894001722175,48.076610184200014,50.554258394941954,58.251237177172612,58.612016970428577,60.152910484218914,69.934963317460173,73.433552820089844,74.778388914089504,76.792352415704912,83.694919040924972,89.060601271929656,91.872303697959154,95.293628832313942,101.70666012900112,104.69477170825114,108.50442382824004,112.89567020768388,114.61823375166807,123.79721402455147,124.5811754769215,124.7463680821963,133.57321989742499,134.44669797585368,141.22014536543386,145.00275593961888,147.15617768762851,155.19229536562455,155.50582102772839,157.55954107018016,164.82470545224166,167.94158047916787,175.98800263351535,173.12339725866056,184.33731420314803,181.79955070134309,187.02422644015988,194.564679297743,196.11506302119912,199.69992458756533,205.13936605642928,210.58527018097271,208.97838728887342,214.99856081586717,219.9908169608363,226.72443561910688,230.10174539061776,229.88311903475181,237.3031970408158,238.41939601000499,242.39215392902568,248.28554587076098,253.17455679758351,255.37136099212051,260.72354856026283,268.38753183757564,267.10762583493761,273.89500496514989,274.07455906062228,277.79932182904486,282.34340722073051,282.40359920593687,291.46791387642094,294.02965441110189,297.66465787104266,303.2616367037765,310.2276459972154,311.90877340932491,311.76248830378222,321.4633234351432,322.47924747024501,330.67190519165786,331.39162677636898,337.23876137607215,338.16023360249363,348.69723905365964,346.86635033025942,351.90613388482819,359.31654832915086,358.56381783662022,361.27969777957065,371.83976011400028,373.11713029919537,375.41134017670981,380.44064498775583,384.00178553511444,389.77424635071486,393.75022062730477,394.84142180785238,400.34081254376576],"type":"scatter","mode":"markers","marker":{"color":"rgba(31,119,180,1)","line":{"color":"rgba(31,119,180,1)"}},"error_y":{"color":"rgba(31,119,180,1)"},"error_x":{"color":"rgba(31,119,180,1)"},"line":{"color":"rgba(31,119,180,1)"},"xaxis":"x","yaxis":"y","frame":null}],"highlight":{"on":"plotly_click","persistent":false,"dynamic":false,"selectize":false,"opacityDim":0.20000000000000001,"selected":{"opacity":1},"debounce":0},"shinyEvents":["plotly_hover","plotly_click","plotly_selected","plotly_relayout","plotly_brushed","plotly_brushing","plotly_clickannotation","plotly_doubleclick","plotly_deselect","plotly_afterplot","plotly_sunburstclick"],"base_url":"https://plot.ly"},"evals":[],"jsHooks":[]}</script>
```


``` r

# To Do:
# 1. Fit a regression line
# 2. Color points by their residual value
```


<!---
*Question 2:*
Verify the definition of a line segment for points $A=(0,3), B=(1,5)$ using a $101 \times 101$ grid. Recall a line segment is all points $s$ that have $d(s, A) + d(s, B) = d(A, B)$.

*Answer* 

``` r
library(sf)
s_1 <- c(0,3)
s_2 <- c(1,5)
Seg1 <- st_linestring( rbind(s_1,s_2) )
grid_pts <- expand.grid(
    x=seq(s_1[1],s_2[1], length.out=101),
    y=seq(s_1[2],s_2[2], length.out=101)
)

Seg1_dist <- dist( Seg1 )
grid_pts$dist <- apply(grid_pts, 1, function(s){
    dist( rbind(s,s_1) ) + dist( rbind(s,s_2) ) })
grid_pts$seg <- grid_pts$dist == Seg1_dist

D_point_seg <- st_multipoint( as.matrix(grid_pts[grid_pts$seg==T,1:2]) ) 
D_point_notseg <- st_multipoint( as.matrix(grid_pts[grid_pts$seg==F,1:2]) ) 

plot(Seg1)
points(D_point_notseg, col=2, pch='.')
points(D_point_seg, pch=16)
box()
```
--->


## Further Reading

For more guidance on how to create Rmarkdown documents, see

* https://github.com/rstudio/cheatsheets/blob/main/rmarkdown.pdf
* https://cran.r-project.org/web/packages/rmarkdown/vignettes/rmarkdown.html
* http://rmarkdown.rstudio.com
* https://bookdown.org/yihui/rmarkdown/
* https://bookdown.org/yihui/rmarkdown-cookbook/
* https://dept.stat.lsa.umich.edu/~jerrick/courses/stat701/notes/rmarkdown.html
* An Introduction to the Advanced Theory and Practice of Nonparametric Econometrics. Raccine 2019. Appendices B \& D.
* https://rmd4sci.njtierney.com/using-rmarkdown.html
* https://alexd106.github.io/intro2R/Rmarkdown_intro.html

If you are still lost, try one of the many online tutorials (such as these)

* https://www.rstudio.com/wp-content/uploads/2015/03/rmarkdown-reference.pdf
* https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
* https://www.neonscience.org/resources/learning-hub/tutorials/rmd-code-intro
* https://m-clark.github.io/Introduction-to-Rmarkdown/
* https://www.stat.cmu.edu/~cshalizi/rmarkdown/
* http://math.wsu.edu/faculty/xchen/stat412/HwWriteUp.Rmd
* http://math.wsu.edu/faculty/xchen/stat412/HwWriteUp.html
* https://holtzy.github.io/Pimp-my-rmd/
* https://ntaback.github.io/UofT_STA130/Rmarkdownforclassreports.html
* https://crd150.github.io/hw_guidelines.html
* https://r4ds.had.co.nz/r-markdown.html
* http://www.stat.cmu.edu/~cshalizi/rmarkdown
* http://www.ssc.wisc.edu/sscc/pubs/RFR/RFR_RMarkdown.html
* http://kbroman.org/knitr_knutshell/pages/Rmarkdown.html



# Probability Theory

You were already introduced to this with [https://jadamso.github.io/Rbooks/data.html#random-variables](random variables) and probability distributions. In this section, we will dig a little deeper theoretically into the statistics we are most likely to use in practice.

## Mean and Variance

The mean and variance are probably the two most basic statistics we might compute, and are often used. To understand them better, we separately analyze how they are computed for discrete and continuous random variables.

#### **Discrete**. {-} 
If the sample space is discrete, we can compute the theoretical mean (or expected value) as
$$
\mu = \sum_{i} x_{i} Prob(X=x_{i}),
$$
where $Prob(X=x_{i})$ is the probability the random variable $X$ takes the particular value $x_{i}$. Similarly, we can compute the theoretical variance as
$$
\sigma^2 = \sum_{i} [x_{i} - \mu]^2 Prob(X=x_{i}),
$$

For example, consider an unfair coin with a $.75$ probability of heads ($x_{i}=1$) and a $.25$ probability of tails ($x_{i}=0$) has a theoretical mean of 
$$
\mu = 1\times.75 + 0 \times .25 = .75
$$
and a theoretical variance of 
$$
\sigma^2 = [1 - .75]^2 \times.75 + [0 - .75]^2 \times.25 = 0.1875
$$


``` r
x <- rbinom(10000, size=1, prob=.75)

round( mean(x), 4)
## [1] 0.7519

round( var(x), 4)
## [1] 0.1866
```

#### **Continuous**. {-}
If the sample space is continuous, we can compute the theoretical mean (or expected value) as
$$
\mu = \int x f(x) d x,
$$
where $f(x)$ is the probability the random variable takes the particular value $x$. Similarly, we can compute the theoretical variance as
$$
\sigma^2 = \int [x - \mu]^2 f(x) d x,
$$
For example, consider a random variable with a continuous uniform distribution over [-1, 1]. In this case, $f(x)=1/[1 - (-1)]=1/2$ for each $x$ in  [-1, 1] and 
$$
\mu = \int_{-1}^{1} \frac{x}{2} d x = \int_{-1}^{0} \frac{x}{2} d x + \int_{0}^{1} \frac{x}{2} d x = 0
$$
and 
$$
\sigma^2 = \int_{-1}^{1} x^2 \frac{1}{2} d x = \frac{1}{2} \frac{x^3}{3}|_{-1}^{1} = \frac{1}{6}[1 - (-1)] = 2/6 =1/3
$$

``` r
x <- runif(10000, -1,1)
round( mean(x), 4)
## [1] -0.0021
round( var(x), 4)
## [1] 0.3275
```


## Bivariate Distributions
Suppose we have two discrete variables $X_{1}$ and $X_{2}$.

Their **joint distribution** is denoted as
\begin{eqnarray}
Prob(X_{1} = x_{1}, X_{2} = x_{2})
\end{eqnarray}
The **conditional distributions** are defined as
\begin{eqnarray}
Prob(X_{1} = x_{1} | X_{2} = x_{2}) = \frac{ Prob(X_{1} = x_{1}, X_{2} = x_{2})}{ Prob( X_{2} = x_{2} )}\\
Prob(X_{2} = x_{2} | X_{1} = x_{1}) = \frac{ Prob(X_{1} = x_{1}, X_{2} = x_{2})}{ Prob( X_{1} = x_{1} )}
\end{eqnarray}
The **marginal distributions** are then defined as
\begin{eqnarray}
Prob(X_{1} = x_{1}) = \sum_{x_{2}} Prob(X_{1} = x_{1} | X_{2} = x_{2}) Prob( X_{2} = x_{2} ) \\
Prob(X_{2} = x_{2}) = \sum_{x_{1}} Prob(X_{2} = x_{2} | X_{1} = x_{1}) Prob( X_{1} = x_{1} ),
\end{eqnarray}
which is also known as the *law of total probability*.

#### **Example: Fair Coin**. {-}
For one example, Consider flipping two coins. Denoted each coin as $i \in \{1, 2\}$, and mark whether "heads" is face up; $X_{i}=1$ if Heads and $=0$ if Tails. Suppose both coins are "fair": $Prob(X_{1}=1)= 1/2$ and $Prob(X_{2}=1|X_{1})=1/2$, then the four potential outcomes have equal probabilities. The joint distribution is 
\begin{eqnarray}
Prob(X_{1} = x_{1}, X_{2} = x_{2}) &=& Prob(X_{1} = x_{1}) Prob(X_{2} = x_{2})\\
Prob(X_{1} = 0, X_{2} = 0) &=& 1/2 \times 1/2 = 1/4 \\
Prob(X_{1} = 0, X_{2} = 1) &=& 1/4 \\
Prob(X_{1} = 1, X_{2} = 0) &=& 1/4 \\
Prob(X_{1} = 1, X_{2} = 1) &=& 1/4 .
\end{eqnarray}
The marginal distribution of the second coin is 
\begin{eqnarray}
Prob(X_{2} = 0) &=& Prob(X_{2} = 0 | X_{1} = 0) Prob(X_{1}=0) + Prob(X_{2} = 0 | X_{1} = 1) Prob(X_{1}=1)\\
&=& 1/2 \times 1/2 + 1/2 \times 1/2 = 1/2\\
Prob(X_{2} = 1) &=& Prob(X_{2} = 1 | X_{1} = 0) Prob(X_{1}=0) + Prob(X_{2} = 1 | X_{1} = 1) Prob(X_{1}=1)\\
&=& 1/2 \times 1/2 + 1/2 \times 1/2 = 1/2
\end{eqnarray}


``` r
# Create a 2x2 matrix for the joint distribution.
# Rows correspond to X1 (coin 1), and columns correspond to X2 (coin 2).
P_fair <- matrix(1/4, nrow = 2, ncol = 2)
rownames(P_fair) <- c("X1=0", "X1=1")
colnames(P_fair) <- c("X2=0", "X2=1")
P_fair
##      X2=0 X2=1
## X1=0 0.25 0.25
## X1=1 0.25 0.25

# Compute the marginal distributions.
# Marginal for X1: sum across columns.
P_X1 <- rowSums(P_fair)
P_X1
## X1=0 X1=1 
##  0.5  0.5
# Marginal for X2: sum across rows.
P_X2 <- colSums(P_fair)
P_X2
## X2=0 X2=1 
##  0.5  0.5

# Compute the conditional probabilities Prob(X2 | X1).
cond_X2_given_X1 <- matrix(0, nrow = 2, ncol = 2)
for (j in 1:2) {
  cond_X2_given_X1[, j] <- P_fair[, j] / P_X1[j]
}
rownames(cond_X2_given_X1) <- c("X2=0", "X2=1")
colnames(cond_X2_given_X1) <- c("given X1=0", "given X1=1")
cond_X2_given_X1
##      given X1=0 given X1=1
## X2=0        0.5        0.5
## X2=1        0.5        0.5
```

#### **Example: Unfair Coin**. {-}
Consider a second example, where the second coin is "Completely Unfair", so that it is always the same as the first. The outcomes generated with a Completely Unfair coin are the same as if we only flipped one coin.
\begin{eqnarray}
Prob(X_{1} = x_{1}, X_{2} = x_{2}) &=& Prob(X_{1} = x_{1}) \mathbf{1}( x_{1}=x_{2} )\\
Prob(X_{1} = 0, X_{2} = 0) &=& 1/2 \\
Prob(X_{1} = 0, X_{2} = 1) &=& 0 \\
Prob(X_{1} = 1, X_{2} = 0) &=& 0 \\
Prob(X_{1} = 1, X_{2} = 1) &=& 1/2 .
\end{eqnarray}
Note that $\mathbf{1}(X_{1}=1) $ means $X_{1}= 1$ and $0$ if $X_{1}\neq0$.
The marginal distribution of the second coin is 
\begin{eqnarray}
Prob(X_{2} = 0) 
&=& Prob(X_{2} = 0 | X_{1} = 0) Prob(X_{1}=0) + Prob(X_{2} = 0 | X_{1} = 1) Prob(X_{1}=1) \\
&=& 1/2 \times 1 + 0 \times 1/2 = 1/2\\
Prob(X_{2} = 1)
&=& Prob(X_{2} = 1 | X_{1} =0) Prob( X_{1} = 0) + Prob(X_{2} = 1 | X_{1} = 1) Prob( X_{1} =1)\\
&=& 0\times 1/2 + 1 \times 1/2 = 1/2
\end{eqnarray}
which is the same as in the first example! Different joint distributions can have the same marginal distributions.



``` r
# Create the joint distribution matrix for the unfair coin case.
P_unfair <- matrix(c(0.5, 0, 0, 0.5), nrow = 2, ncol = 2, byrow = TRUE)
rownames(P_unfair) <- c("X1=0", "X1=1")
colnames(P_unfair) <- c("X2=0", "X2=1")
P_unfair
##      X2=0 X2=1
## X1=0  0.5  0.0
## X1=1  0.0  0.5

# Compute the marginal distribution for X2 in the unfair case.
P_X2_unfair <- colSums(P_unfair)
P_X1_unfair <- rowSums(P_unfair)

# Compute the conditional probabilities Prob(X1 | X2) for the unfair coin.
cond_X2_given_X1_unfair <- matrix(NA, nrow = 2, ncol = 2)
for (j in 1:2) {
  if (P_X1_unfair[j] > 0) {
    cond_X2_given_X1_unfair[, j] <- P_unfair[, j] / P_X1_unfair[j]
  }
}
rownames(cond_X2_given_X1_unfair) <- c("X2=0", "X2=1")
colnames(cond_X2_given_X1_unfair) <- c("given X1=0", "given X1=1")
cond_X2_given_X1_unfair
##      given X1=0 given X1=1
## X2=0          1          0
## X2=1          0          1
```

#### **Bayes' Theorem**. {-}
Finally, note **Bayes' Theorem**:
\begin{eqnarray}
Prob(X_{1} = x_{1} | X_{2} = x_{2})  Prob( X_{2} = x_{2}) &=& Prob(X_{1} = x_{1}, X_{2} = x_{2}) = Prob(X_{2} = x_{2} | X_{1} = x_{1}) Prob(X_{1}=x_{1})\\
Prob(X_{1} = x_{1} | X_{2} = x_{2}) &=& \frac{ Prob(X_{2} = x_{2} | X_{1} = x_{1}) Prob(X_{1}=x_{1}) }{ Prob( X_{2} = x_{2}) }
\end{eqnarray}

``` r
# Verify Bayes' theorem for the unfair coin case:
# Compute Prob(X1=1 | X2=1) using the formula:
#   Prob(X1=1 | X2=1) = [Prob(X2=1 | X1=1) * Prob(X1=1)] / Prob(X2=1)

P_X1_1 <- 0.5
P_X2_1_given_X1_1 <- 1  # Since coin 2 copies coin 1.
P_X2_1 <- P_X2_unfair["X2=1"]

bayes_result <- (P_X2_1_given_X1_1 * P_X1_1) / P_X2_1
bayes_result
## X2=1 
##    1
```



## Further Reading 

Many introductory econometrics textbooks have a good appendix on probability and statistics. There are many useful texts online too

* [Refresher] https://www.khanacademy.org/math/statistics-probability/probability-library/basic-theoretical-probability/a/probability-the-basics
* https://www.r-bloggers.com/2024/03/calculating-conditional-probability-in-r/
* https://www.atmos.albany.edu/facstaff/timm/ATM315spring14/R/IPSUR.pdf
* https://math.dartmouth.edu/~prob/prob/prob.pdf
* https://bookdown.org/speegled/foundations-of-statistics/
* https://bookdown.org/probability/beta/discrete-random-variables.html
* https://www.econometrics-with-r.org/2.1-random-variables-and-probability-distributions.html
* https://probability4datascience.com/ch02.html
* https://rc2e.com/probability
* https://book.stat420.org/probability-and-statistics-in-r.html
* https://statsthinking21.github.io/statsthinking21-R-site/probability-in-r-with-lucy-king.html
* https://bookdown.org/probability/statistics/
* https://bookdown.org/probability/beta/
* https://bookdown.org/a_shaker/STM1001_Topic_3/
* https://bookdown.org/fsancier/bookdown-demo/
* https://bookdown.org/kevin_davisross/probsim-book/
* https://bookdown.org/machar1991/ITER/2-pt.html
* https://www.atmos.albany.edu/facstaff/timm/ATM315spring14/R/IPSUR.pdf
* https://math.dartmouth.edu/~prob/prob/prob.pdf


