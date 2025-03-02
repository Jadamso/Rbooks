# (PART) Data Analysis in R {-}



# First Steps
***

## Why R

We focus on R because it is good for complex stats, concise figures, and coherent organization. It is built and developed by applied statisticians for statistics, and used by many in academia and industry. For students, think about labor demand and what may be good for getting a job. Do some of your own research to best understand how much to invest.

## Install R

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

*Make sure you have the latest version of R and Rstudio for class.* If not, then reinstall. 

## Interfacing with R

Rstudio is easiest to get going with. (There are other GUI's.) There are 4 panes. The top left is where you write and save code

 * Create and save a new `R Script` file *My_First_Script.R*
 * could also use a plain .txt file.

![](./Figures_Manual/Rstudio.svg)<!-- -->

The pane below is where your code is executed. For all following examples, make sure to both execute and store your code.

Note that the coded examples generally have objects, functions, and comments.

## Introductions to R

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



# Mathematics
***

Scalars and vectors are probably your most common mathematical objects

## Scalars


``` r
xs <- 2 # Your first scalar
xs  # Print the scalar
```

```
## [1] 2
```

``` r
(xs+1)^2 # Perform and print a simple calculation
```

```
## [1] 9
```

``` r
xs + NA # often used for missing values
```

```
## [1] NA
```

``` r
xs*2
```

```
## [1] 4
```

## Vectors
 

``` r
x <- c(0,1,3,10,6) # Your First Vector
x # Print the vector
```

```
## [1]  0  1  3 10  6
```

``` r
x[2] # Print the 2nd Element; 1
```

```
## [1] 1
```

``` r
x+2 # Print simple calculation; 2,3,5,8,12
```

```
## [1]  2  3  5 12  8
```

``` r
x*2
```

```
## [1]  0  2  6 20 12
```

``` r
x^2
```

```
## [1]   0   1   9 100  36
```

Mathematical operations apply elementwise

``` r
x+x
```

```
## [1]  0  2  6 20 12
```

``` r
x*x
```

```
## [1]   0   1   9 100  36
```

``` r
x^x
```

```
## [1] 1.0000e+00 1.0000e+00 2.7000e+01 1.0000e+10 4.6656e+04
```


``` r
c(1) # scalars are vectors
```

```
## [1] 1
```

``` r
1:7
```

```
## [1] 1 2 3 4 5 6 7
```

``` r
seq(0,1,by=.1)
```

```
##  [1] 0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0
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
```

```
## [1]  2  3  5 12  8
```

``` r
# notice 'output_vector' is not available here
```

There are many many generalizations

``` r
add_vec <- function(input_vector1, input_vector2) {
    output_vector <- input_vector1 + input_vector2
    return(output_vector)
}
add_vec(x,3)
```

```
## [1]  3  4  6 13  9
```

``` r
add_vec(x,x)
```

```
## [1]  0  2  6 20 12
```

``` r
sum_squared <- function(x1, x2) {
	y <- (x1 + x2)^2
	return(y)
}

sum_squared(1, 3)
```

```
## [1] 16
```

``` r
sum_squared(x, 2)
```

```
## [1]   4   9  25 144  64
```

``` r
sum_squared(x, NA) 
```

```
## [1] NA NA NA NA NA
```

``` r
sum_squared(x, x)
```

```
## [1]   0   4  36 400 144
```

``` r
sum_squared(x, 2*x)
```

```
## [1]   0   9  81 900 324
```

Applying the same function over and over again

``` r
sapply(1:3, exp)
```

```
## [1]  2.718282  7.389056 20.085537
```

``` r
c( exp(1), exp(2), exp(3))
```

```
## [1]  2.718282  7.389056 20.085537
```

``` r
# More complex example
sapply(1:10, function(i){
    x <- i^(i-1)
    y <- x + mean( 0:i )
    z <- log(y)/i
    return(z)
})
```

```
##  [1] 0.4054651 0.5493061 0.7837918 1.0474137 1.2883487 1.4931972 1.6679272
##  [8] 1.8195116 1.9530885 2.0723266
```

``` r
# mapply takes multiple vectors
# mapply(sum, 1:3, exp(1:3) )
```


Functions can take functions as arguments

``` r
fun_of_seq <- function(f){
    x <- seq(1,3, length.out=12)
    y <- f(x)
    return(y)
}

fun_of_seq(mean)
```

```
## [1] 2
```

``` r
fun_of_seq(sd)
```

```
## [1] 0.6555548
```


<!---
recursive functions

``` r
# For Loop
x <- rep(1, 3)
for(i in 2:length(x) ){
    x[i] <- (x[i-1]+1)^2
}
x
```

```
## [1]  1  4 25
```

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
```

```
## [1]      1      4     25    676 458329
```
--->


## Logic 

**Basic**.


``` r
x <- c(1,2,3,NA)
x > 2
```

```
## [1] FALSE FALSE  TRUE    NA
```

``` r
x==2
```

```
## [1] FALSE  TRUE FALSE    NA
```

``` r
any(x==2)
```

```
## [1] TRUE
```

``` r
all(x==2)
```

```
## [1] FALSE
```

``` r
2 %in% x
```

```
## [1] TRUE
```

``` r
is.numeric(x)
```

```
## [1] TRUE
```

``` r
is.na(x)
```

```
## [1] FALSE FALSE FALSE  TRUE
```

The "&" and "|" commands are logical operations that compare vectors to the left and right.

``` r
x <- 1:3
is.numeric(x) & (x < 2)
```

```
## [1]  TRUE FALSE FALSE
```

``` r
is.numeric(x) | (x < 2)
```

```
## [1] TRUE TRUE TRUE
```

``` r
if(length(x) >= 5 & x[5] > 12) print("ok")
```

see https://bookdown.org/rwnahhas/IntroToR/logical.html


**Advanced**.


``` r
x <- 1:10
cut(x, 4)
```

```
##  [1] (0.991,3.25] (0.991,3.25] (0.991,3.25] (3.25,5.5]   (3.25,5.5]  
##  [6] (5.5,7.75]   (5.5,7.75]   (7.75,10]    (7.75,10]    (7.75,10]   
## Levels: (0.991,3.25] (3.25,5.5] (5.5,7.75] (7.75,10]
```

``` r
split(x, cut(x, 4))
```

```
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
```

```
## (0.991,3.25]   (3.25,5.5]   (5.5,7.75]    (7.75,10] 
##          2.0          4.5          6.5          9.0
```

``` r
# shortcut
aggregate(x, list(cut(x,4)), mean)
```

```
##        Group.1   x
## 1 (0.991,3.25] 2.0
## 2   (3.25,5.5] 4.5
## 3   (5.5,7.75] 6.5
## 4    (7.75,10] 9.0
```


##  Matrices

Matrices are objects

``` r
x1 <- c(1,4,9)
x2 <- c(3,0,2)
x_mat <- rbind(x1, x2)

x_mat       # Print full matrix
```

```
##    [,1] [,2] [,3]
## x1    1    4    9
## x2    3    0    2
```

``` r
x_mat[2,]   # Print Second Row
```

```
## [1] 3 0 2
```

``` r
x_mat[,2]   # Print Second Column
```

```
## x1 x2 
##  4  0
```

``` r
x_mat[2,2]  # Print Element in Second Column and Second Row
```

```
## x2 
##  0
```

There are elementwise operations
```
x_mat+2
x_mat*2
x_mat^2

x_mat + x_mat
x_mat*x_mat
x_mat^x_mat
```

**Functions**. 

You can apply functions to matrices

``` r
sum_squared(x_mat, x_mat)
```

```
##    [,1] [,2] [,3]
## x1    4   64  324
## x2   36    0   16
```

``` r
# Apply function to each matrix row
y <- apply(x_mat, 1, sum)^2 
# ?apply  #checks the function details
y - sum_squared(x, x) # tests if there are any differences
```

```
##  [1]  192    9  160  -39   96 -119    0 -231 -128 -375
```

There are many possible functions you can apply

``` r
# Return Y-value with minimum absolute difference from 3
abs_diff_y <- abs( y - 3 ) 
abs_diff_y # is this the luckiest number?
```

```
##  x1  x2 
## 193  22
```

``` r
#min(abs_diff_y)
#which.min(abs_diff_y)
y[ which.min(abs_diff_y) ]
```

```
## x2 
## 25
```

There are also some useful built in functions

``` r
m <- matrix(c(1:3,2*(1:3)),byrow=TRUE,ncol=3)
m
```

```
##      [,1] [,2] [,3]
## [1,]    1    2    3
## [2,]    2    4    6
```

``` r
# normalize rows
m/rowSums(m)
```

```
##           [,1]      [,2] [,3]
## [1,] 0.1666667 0.3333333  0.5
## [2,] 0.1666667 0.3333333  0.5
```

``` r
# normalize columns
t(t(m)/colSums(m))
```

```
##           [,1]      [,2]      [,3]
## [1,] 0.3333333 0.3333333 0.3333333
## [2,] 0.6666667 0.6666667 0.6666667
```

``` r
# de-mean rows
sweep(m,1,rowMeans(m), '-')
```

```
##      [,1] [,2] [,3]
## [1,]   -1    0    1
## [2,]   -2    0    2
```

``` r
# de-mean columns
sweep(m,2,colMeans(m), '-')
```

```
##      [,1] [,2] [,3]
## [1,] -0.5   -1 -1.5
## [2,]  0.5    1  1.5
```


**Matrix Algebra**.

And you can also use matrix algebra

``` r
x_mat1 <- matrix(2:7,2,3)
x_mat1
```

```
##      [,1] [,2] [,3]
## [1,]    2    4    6
## [2,]    3    5    7
```

``` r
x_mat2 <- matrix(4:-1,2,3)
x_mat2
```

```
##      [,1] [,2] [,3]
## [1,]    4    2    0
## [2,]    3    1   -1
```

``` r
tcrossprod(x_mat1, x_mat2) #x_mat1 %*% t(x_mat2)
```

```
##      [,1] [,2]
## [1,]   16    4
## [2,]   22    7
```

``` r
crossprod(x_mat1, x_mat2)
```

```
##      [,1] [,2] [,3]
## [1,]   17    7   -3
## [2,]   31   13   -5
## [3,]   45   19   -7
```

``` r
# x_mat1 * x_mat2
```


## Arrays

Generalization of matrices (often used in spatial econometrics)


``` r
a <- array(data = 1:24, dim = c(2, 3, 4))
a
```

```
## , , 1
## 
##      [,1] [,2] [,3]
## [1,]    1    3    5
## [2,]    2    4    6
## 
## , , 2
## 
##      [,1] [,2] [,3]
## [1,]    7    9   11
## [2,]    8   10   12
## 
## , , 3
## 
##      [,1] [,2] [,3]
## [1,]   13   15   17
## [2,]   14   16   18
## 
## , , 4
## 
##      [,1] [,2] [,3]
## [1,]   19   21   23
## [2,]   20   22   24
```

``` r
a[1, , , drop = FALSE]  # Row 1
```

```
## , , 1
## 
##      [,1] [,2] [,3]
## [1,]    1    3    5
## 
## , , 2
## 
##      [,1] [,2] [,3]
## [1,]    7    9   11
## 
## , , 3
## 
##      [,1] [,2] [,3]
## [1,]   13   15   17
## 
## , , 4
## 
##      [,1] [,2] [,3]
## [1,]   19   21   23
```

``` r
#a[, 1, , drop = FALSE]  # Column 1
#a[, , 1, drop = FALSE]  # Layer 1

a[ 1, 1,  ]  # Row 1, column 1
```

```
## [1]  1  7 13 19
```

``` r
#a[ 1,  , 1]  # Row 1, "layer" 1
#a[  , 1, 1]  # Column 1, "layer" 1
a[1 , 1, 1]  # Row 1, column 1, "layer" 1
```

```
## [1] 1
```

Apply extends to arrays

``` r
apply(a, 1, mean)    # Row means
```

```
## [1] 12 13
```

``` r
apply(a, 2, mean)    # Column means
```

```
## [1] 10.5 12.5 14.5
```

``` r
apply(a, 3, mean)    # "Layer" means
```

```
## [1]  3.5  9.5 15.5 21.5
```

``` r
apply(a, 1:2, mean)  # Row/Column combination 
```

```
##      [,1] [,2] [,3]
## [1,]   10   12   14
## [2,]   11   13   15
```


Outer products yield arrays

``` r
x <- c(1,2,3)
x_mat1 <- outer(x, x) # x %o% x
x_mat1
```

```
##      [,1] [,2] [,3]
## [1,]    1    2    3
## [2,]    2    4    6
## [3,]    3    6    9
```

``` r
is.array(x_mat) # Matrices are arrays
```

```
## [1] TRUE
```

``` r
x_mat2 <- matrix(6:1,2,3)
outer(x_mat2, x)
```

```
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
```

``` r
# outer(x_mat2, matrix(x))
# outer(x_mat2, t(x))
# outer(x_mat1, x_mat2)
```

# Data
***

## Types

The two most common data types are

* *cardinal*: the difference between elements always mean the same thing. E.g., 2-1=3-2.
* *factor*: the difference between  elements does not always mean the same thing. E.g., First place - Second place = ??.

We can further distinguish between whether cardinal data are discrete or continuous (i.e., whether an arbitrary number of decimal points are allowed.)
We can also further distinguish between whether factor data are ordered or not (i.e., whether the labels {"A", "B", and "C"} correspond to any meaningful order like {first, second, and third}.)


``` r
d1d <- 1:3 # Cardinal data (Discrete)
d1d
```

```
## [1] 1 2 3
```

``` r
class(d1d)
```

```
## [1] "integer"
```

``` r
d1c <- c(1.1, 2/3, 3) # Cardinal data (Continuous)
d1c
```

```
## [1] 1.1000000 0.6666667 3.0000000
```

``` r
class(d1c)
```

```
## [1] "numeric"
```

``` r
d2o <- factor(c('A','B','C'), ordered=T) # Factor data (Ordinal)
d2o
```

```
## [1] A B C
## Levels: A < B < C
```

``` r
class(d2o)
```

```
## [1] "ordered" "factor"
```

``` r
d2c <- factor(c('Leipzig','Los Angeles','Logan'), ordered=F) # Factor data (Categorical)
d2c
```

```
## [1] Leipzig     Los Angeles Logan      
## Levels: Leipzig Logan Los Angeles
```

``` r
class(d2c)
```

```
## [1] "factor"
```



R also allows for more unstructured data types.

``` r
c('hello world', 'hi mom')  # character strings
```

```
## [1] "hello world" "hi mom"
```

``` r
list(d1c, d2c)  # lists
```

```
## [[1]]
## [1] 1.1000000 0.6666667 3.0000000
## 
## [[2]]
## [1] Leipzig     Los Angeles Logan      
## Levels: Leipzig Logan Los Angeles
```

``` r
list(d1c, c('hello world'),
    list(d1d, list('...inception...'))) # lists
```

```
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
```

``` r
# data.frames: your most common data type
    # matrix of different data-types
    # well-ordered lists
d0 <- data.frame(y=d1c, x=d2c)
d0
```

```
##           y           x
## 1 1.1000000     Leipzig
## 2 0.6666667 Los Angeles
## 3 3.0000000       Logan
```


**Strings**.


``` r
paste( 'hi', 'mom')
```

```
## [1] "hi mom"
```

``` r
paste( c('hi', 'mom'), collapse='--')
```

```
## [1] "hi--mom"
```

``` r
kingText <- "The king infringes the law on playing curling."
gsub(pattern="ing", replacement="", kingText)
```

```
## [1] "The k infres the law on play curl."
```

``` r
# advanced usage
#gsub("[aeiouy]", "_", kingText)
#gsub("([[:alpha:]]{3,})ing\\b", "\\1", kingText) 
```

See 

* https://meek-parfait-60672c.netlify.app/docs/M1_R-intro_03_text.html
* https://raw.githubusercontent.com/rstudio/cheatsheets/main/regex.pdf


**Initial Inspection**.

You typically begin by inspecting your data by examining the first few observations.
 
Consider, for example, historical data on crime in the US.


``` r
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
# Check NA values
sum(is.na(x))
```

```
## [1] 0
```

To further examine data, we look at "distributions". In what follows, we will denote the data for a single variable as $\{X_{i}\}_{i=1}^{N}$, where there are $N$ observations and $X_{i}$ is the value of the $i$th one. While $X_{i}$ could be 

## Distributions

**Histogram**. The histogram divides the range of $\{X_{i}\}_{i=1}^{N}$ into $L$ exclusive bins of equal-width $h=[\text{max}(X_{i}) - \text{min}(X_{i})]/L$, and counts the number of observations within each bin. We often scale the counts to interpret the numbers as a density. Mathematically, for an exclusive bin with midpoint $x$, we compute
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

<img src="02-BasicStats_files/figure-html/unnamed-chunk-28-1.png" width="672" />


**Empirical *Cumulative* Distribution Function**. The ECDF counts the proportion of observations whose values $X_{i}$ are less than $x$; 
\begin{eqnarray}
\widehat{F}_{ECDF}(x) = \frac{1}{N} \sum_{i}^{N} \mathbf{1}(X_{i} \leq x) 
\end{eqnarray}
for each unique value of $x$ in the dataset.


``` r
F_murder <- ecdf(USArrests$Murder)
# proportion of murders < 10
F_murder(10)
```

```
## [1] 0.7
```

``` r
# proportion of murders < x, for all x
plot(F_murder, main='', xlab='Murder Arrests',
    pch=16, col=grey(0,.5))
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-29-1.png" width="672" />


**Boxplots**. Boxplots summarize the distribution of data using *quantiles*: the $q$th quantile is the value where $q$ percent of the data are below and ($1-q$) percent are above.

* The "median" is the point where half of the data has lower values and the other half has higher values.
* The "lower quartile" is the point where 25% of the data has lower values and the other 75% has higher values.
* The "min" is the smallest value (or largest negative value if there are any) where 0% of the data has lower values.


``` r
x <- USArrests$Murder

# quantiles
median(x)
```

```
## [1] 7.25
```

``` r
range(x)
```

```
## [1]  0.8 17.4
```

``` r
quantile(x, probs=c(0,.25,.5))
```

```
##    0%   25%   50% 
## 0.800 4.075 7.250
```

``` r
# deciles are quantiles
quantile(x, probs=seq(0,1, by=.1))
```

```
##    0%   10%   20%   30%   40%   50%   60%   70%   80%   90%  100% 
##  0.80  2.56  3.38  4.75  6.00  7.25  8.62 10.12 12.12 13.32 17.40
```

To compute quantiles, we sort the observations from smallest to largest as $X_{(1)}, X_{(2)},... X_{(N)}$, and then compute quantiles as $X_{ (q*N) }$. Note that $(q*N)$ is rounded and there are different ways to break ties.

``` r
xo <- sort(x)
xo
```

```
##  [1]  0.8  2.1  2.1  2.2  2.2  2.6  2.6  2.7  3.2  3.3  3.4  3.8  4.0  4.3  4.4
## [16]  4.9  5.3  5.7  5.9  6.0  6.0  6.3  6.6  6.8  7.2  7.3  7.4  7.9  8.1  8.5
## [31]  8.8  9.0  9.0  9.7 10.0 10.4 11.1 11.3 11.4 12.1 12.2 12.7 13.0 13.2 13.2
## [46] 14.4 15.4 15.4 16.1 17.4
```

``` r
# median
xo[length(xo)*.5]
```

```
## [1] 7.2
```

``` r
quantile(x, probs=.5, type=4)
```

```
## 50% 
## 7.2
```

``` r
# min
xo[1]
```

```
## [1] 0.8
```

``` r
min(xo)
```

```
## [1] 0.8
```

``` r
quantile(xo,probs=0)
```

```
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

<img src="02-BasicStats_files/figure-html/unnamed-chunk-32-1.png" width="672" />



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

<img src="02-BasicStats_files/figure-html/unnamed-chunk-33-1.png" width="672" />

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

<img src="02-BasicStats_files/figure-html/unnamed-chunk-34-1.png" width="672" />


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

<img src="02-BasicStats_files/figure-html/unnamed-chunk-35-1.png" width="672" />

``` r
# 4 Groups with equal numbers of observations
#Qcuts <- c(
#    '0%'=min(USArrests$UrbanPop)-10*.Machine$double.eps,
#    quantile(USArrests$UrbanPop, probs=c(.25,.5,.75,1)))
#USArrests$UrbanPop_cut <- cut(USArrests$UrbanPop, Qcuts)
#boxplot(Murder~UrbanPop_cut, USArrests, col=hcl.colors(4,alpha=.5))
```



## Joint Distributions

Scatterplots are used frequently to summarize the joint relationship between two variables. They can be enhanced in several ways. As a default, use semi-transparent points so as not to hide any points (and perhaps see if your observations are concentrated anywhere).

You can also add regression lines (and confidence intervals), although I will defer this until later.


``` r
plot(Murder~UrbanPop, USArrests, pch=16, col=grey(0.,.5))
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-36-1.png" width="672" />

``` r
# Add the line of best fit for pooled data
#reg <- lm(Murder~UrbanPop, data=USArrests)
#abline(reg, lty=2)
```

**Conditional Relationships**. You can also use size, color, and shape to distinguish different conditional relationships.


``` r
# High Assault Areas
assault_high <- USArrests$Assault > median(USArrests$Assault)
cols <- ifelse(assault_high, rgb(1,0,0,.5), rgb(0,0,1,.5))

# Scatterplot
# Show High Assault Areas via 'cex=' or 'pch='
plot(Murder~UrbanPop, USArrests, pch=16, col=cols)
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-37-1.png" width="672" />

``` r
# Could also add regression lines y for each data split
#reg_high <- lm(Murder~UrbanPop, data=USArrests[assault_high,])
#abline(reg_high, lty=2, col=rgb(1,0,0,1))
#reg_low <- lm(Murder~UrbanPop, data=USArrests[!assault_high,])
#abline(reg_low, lty=2, col= rgb(0,0,1,1))
```


**Marginal Distributions**. You can also show the distributions of each variable along each axis.


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

<img src="02-BasicStats_files/figure-html/unnamed-chunk-38-1.png" width="672" />



## Further Reading 
For plotting histograms and marginals, see 

* https://www.r-bloggers.com/2011/06/example-8-41-scatterplot-with-marginal-histograms/
* https://r-graph-gallery.com/histogram.html
* https://r-graph-gallery.com/74-margin-and-oma-cheatsheet.html 
* https://jtr13.github.io/cc21fall2/tutorial-for-scatter-plot-with-marginal-distribution.html.



# Statistics
***

## Random Variables

Random variables are vectors that are generated from a probabilistic process. 

The *sample space* of a random variable refers to the set of all possible outcomes.
A *probability* assigns to any set of events a number between $0$ and $1$.

There are two basic types of sample spaces:

**Discrete**.
The random variable can take one of several discrete values.  E.g., any number in $\{1,2,3,4\}$.


``` r
# Bernoulli (Coin Flip: Heads=1 Tails=0)
rbinom(1, 1, 0.5) # 1 draw
```

```
## [1] 1
```

``` r
rbinom(4, 1, 0.5) # 4 draws
```

```
## [1] 0 0 0 0
```

``` r
x0 <- rbinom(1000, 1, 0.5)
hist(x0, breaks=50, border=NA, main=NA, freq=T)
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-39-1.png" width="672" />

``` r
# plot(table(x0))

# Bernoulli (Coin Flip: Heads=1 Tails=0)
x0 <- rbinom(1000, 1, 0.2)
hist(x0, breaks=50, border=NA, main=NA, freq=T)
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-39-2.png" width="672" />

``` r
# plot(table(x0))
```


``` r
# Discrete Uniform (numbers 1,...4 all have equal probability)
sample(1:4, 1, replace=T) # 1 draw
```

```
## [1] 4
```

``` r
sample(1:4, 3, replace=T) # 3 draws
```

```
## [1] 4 4 4
```

``` r
x1 <- sample(1:4, 1000, replace=T)
hist(x1, breaks=50, border=NA, main=NA, freq=T)
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-40-1.png" width="672" />

``` r
# plot(table(x1))
```


**Continuous**.
The random variable can take one value out of an uncountably infinite number. E.g., any number between $[0,1]$ allowing for any number of decimal points.


``` r
# Continuous Uniform
runif(3) # 3 draws
```

```
## [1] 0.9593647 0.1682418 0.4078311
```

``` r
x2 <- runif(2000)
hist(x2, breaks=25, border=NA, main=NA, freq=F)
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-41-1.png" width="672" />

``` r
# Normal (Gaussian)
rnorm(3) # 3 draws
```

```
## [1]  1.0808476 -0.4670859  0.4303165
```

``` r
x3 <- rnorm(1000)
hist(x3, breaks=25, border=NA, main=NA, freq=F)
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-41-2.png" width="672" />


We might further distinguish types of random variables based on whether their maximum value is theoretically finite or infinite. In any case, we often summarize distributions with *statistics*: functions of data. The most basic way to do this is

``` r
summary(x1)
```

```
##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
##   1.000   2.000   3.000   2.503   3.000   4.000
```

``` r
summary(x3)
```

```
##     Min.  1st Qu.   Median     Mean  3rd Qu.     Max. 
## -3.12854 -0.63213  0.04556  0.03611  0.68480  3.32838
```

The values in "summary" can all be calculated individually. (E.g., the "mean" computes the [sum of all values] divided by [number of values].) There are many other combinations of statistics you can use.


## Center/Spread Statistics
The most basic statistics summarize the center of a distribution and how far apart the values are spread.

**Mean and Variance**. Perhaps the most common statistic is the mean;
$$\overline{X}=\frac{\sum_{i=1}^{N}X_{i}}{N}$$, where $X_{i}$ denotes the value of the $i$th observation.


``` r
# compute the mean of a random sample
x <- runif(100)
hist(x, border=NA, main=NA)
m <- mean(x)  #sum(x)/length(x)
abline(v=m, col=2, lwd=2)
title(paste0('mean= ', round(m,2)), font.main=1)
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-43-1.png" width="672" />

``` r
# is m close to it's true value (1-0)/2=.5?
```

Perhaps the second most common statistic is the variance: the average squared deviation from the mean
$$V_{X} =\frac{\sum_{i=1}^{N} [X_{i} - \overline{X}]^2}{N}.$$
The standard deviation is simply $s_{X} = \sqrt{V_{X}}$.^[Note that a "corrected version" is used by R and many statisticians: $V_{X} =\frac{\sum_{i=1}^{N} [X_{i} - \overline{X}]^2}{N-1}$.]


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

<img src="02-BasicStats_files/figure-html/unnamed-chunk-44-1.png" width="672" />

``` r
# Note a small sample correction: 
# var(x)
# mean( (x - mean(x))^2 )
```

Together, these statistics summarize the central tendency and dispersion of a distribution. In some special cases, such as with the normal distribution, they completely describe the distribution. Other distributions are easier to describe with other statistics.


**Median, Interquartile Range, Median Absolute Deviation**. Recall that the $q$th quantile is the value where $q$ percent of the data are below and ($1-q$) percent are above. 

The median ($q=.5$) is the point where half of the data is lower values and the other half is higher.
The first and third quartiles ($q=.25$ and $q=.75$) together measure is the middle 50 percent of the data. The size of that range (interquartile range: the difference between the quartiles) represents "spread" or "dispersion" of the data.

The mean absolute deviation also measures spread
$$MAD_{X} = med\left( | X_{i} - med(X) | \right).$$


``` r
x <- rgeom(50, .4)
x
```

```
##  [1]  0  0  0  4  2  0  0  0 12  2  8  4  1  0  0  6  0  1  0  0  5  3  5  0  2
## [26]  0  1  0  1  0  0  2  1  2  5  0  0  0  3  0  2  0  5  0  1  0  1  2  0  3
```

``` r
plot(table(x))
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-45-1.png" width="672" />

``` r
#mean(x)
median(x)
```

```
## [1] 1
```

``` r
#sd(x)
#IQR(x) # diff( quantile(x, probs=c(.25,.75)))
mad(x, constant=1) # median( abs(x - median(x)) )
```

```
## [1] 1
```


``` r
# other absolute deviations:
#mean( abs(x - mean(x)) )
#mean( abs(x - median(x)) )
#median( abs(x - mean(x)) )
```


**Mode and Share Concentration**. Sometimes, none of the above work well. With categorical data, for example, distributions are easier to describe with other statistics. The mode is the most common observation: the value with the highest observed frequency. We can also measure the spread/dispersion of the frequencies, or compare the highest frequency to the average frequency to measure concentration at the mode.


``` r
# Draw 3 Random Letters
K <- length(LETTERS)
x_id <- rmultinom(3, 1, prob=rep(1/K,K))
x_id
```

```
##       [,1] [,2] [,3]
##  [1,]    0    0    0
##  [2,]    0    0    1
##  [3,]    0    0    0
##  [4,]    0    0    0
##  [5,]    0    0    0
##  [6,]    0    0    0
##  [7,]    0    0    0
##  [8,]    0    0    0
##  [9,]    0    0    0
## [10,]    0    0    0
## [11,]    0    0    0
## [12,]    0    0    0
## [13,]    0    0    0
## [14,]    0    0    0
## [15,]    0    0    0
## [16,]    0    0    0
## [17,]    0    0    0
## [18,]    0    0    0
## [19,]    1    0    0
## [20,]    0    0    0
## [21,]    0    0    0
## [22,]    0    0    0
## [23,]    0    0    0
## [24,]    0    1    0
## [25,]    0    0    0
## [26,]    0    0    0
```

``` r
# Draw Random Letters 100 Times
x_id <- rowSums(rmultinom(100, 1, prob=rep(1/K,K)))
x <- lapply(1:K, function(k){
    rep(LETTERS[k], x_id[k])
})
x <- factor(unlist(x), levels=LETTERS)

plot(x)
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-47-1.png" width="672" />

``` r
tx <- table(x)
# mode(s)
names(tx)[tx==max(tx)]
```

```
## [1] "U"
```

``` r
# freq. spread
sx <- tx/sum(tx)
sd(sx) # mad(sx)
```

```
## [1] 0.01826304
```

``` r
# freq. concentration 
max(tx)/mean(tx)
```

```
## [1] 2.34
```


## Shape Statistics

Central tendency and dispersion are often insufficient to describe a distribution. To further describe shape, we can compute these to "standard moments":

$$Skew_{X} =\frac{\sum_{i=1}^{N} [X_{i} - \overline{X}]^3 / N}{ [s_{X}]^3 }$$
$$Kurt_{X} =\frac{\sum_{i=1}^{N} [X_{i} - \overline{X}]^4 / N}{ [s_{X}]^4 }.$$

**Skewness**.
Skew captures how symmetric the distribution is.


``` r
x <- rlnorm(1000)

hist(x, border=NA, main=NA, freq=F, breaks=20)
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-48-1.png" width="672" />


``` r
skewness <-  function(x) {
 x_bar <- mean(x)
 m3 <- mean((x - x_bar)^3)
 skew <- m3/(sd(x)^3)
 return(skew)
}

skewness(rlnorm(1000))
```

```
## [1] 4.244953
```

``` r
skewness(rnorm(1000))
```

```
## [1] -0.0002386932
```

**Kurtosis**.
Kurt captures how many "outliers" there are.


``` r
x <- rcauchy(1000)

par(mfrow=c(1,2))
hist(x, border=NA, main=NA, freq=F, breaks=100)
boxplot(x, main=NA)
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-50-1.png" width="672" />



``` r
kurtosis <- function(x) {  
 x_bar <- mean(x)
 m4 <- mean((x - x_bar)^4) 
 kurt <- m4/(sd(x)^4) - 3  
 return(kurt)
}

kurtosis(rcauchy(1000))
```

```
## [1] 118.8045
```

``` r
kurtosis(rnorm(1000))
```

```
## [1] 0.07173244
```


**Clusters/Gaps**. You can also describe distributions in terms of how clustered the values are


``` r
# Number of Modes
x <- rbeta(1000, .6, .6)
hist(x, border=NA, main=NA, freq=F, breaks=20)
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-52-1.png" width="672" />

But remember: *a picture is worth a thousand words*.


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

<img src="02-BasicStats_files/figure-html/unnamed-chunk-53-1.png" width="672" />

``` r
# Show True Density
#d_ugly1 <- function(x, theta1=c(-8,-1), theta2=c(-2,2), rho=.25){
#    rho     * dunif(x, theta1[1], theta2[1]) +
#    (1-rho) * dnorm(x, theta1[2], theta2[2]) }
#dx <- d_ugly1(X)
#lines(X, dx, col=1)
```






## Beyond Basics

Use expansion "packages" for less common procedures and more functionality

**CRAN**.
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

**Probability Distributions**.
There are many many different [probability distributions](https://en.wikipedia.org/wiki/List_of_probability_distributions). The most common ones are [easily accessible](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/Distributions.html)


``` r
library(extraDistr)

par(mfrow=c(1,2))
for(p in c(-.5,0)){
    x <- rgev(2000, mu=0, sigma=1, xi=p)
    hist(x, breaks=50, border=NA, main=NA, freq=F)
}
title('GEV distributions', outer=T, line=-1)
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-55-1.png" width="672" />


``` r
library(extraDistr)

par(mfrow=c(1,3))
for(p in c(-1, 0,2)){
    x <- rtlambda(2000, p)
    hist(x, breaks=100, border=NA, main=NA, freq=F)
}
title('Tukey Lambda distributions', outer=T, line=-1)
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-56-1.png" width="672" />




``` r
pars <- expand.grid( c(.5,1,2), c(.5,1,2) )
par(mfrow=c(3,3))
apply(pars, 1, function(p){
    x <- rbeta(2000, p[1], p[2])
    hist(x, breaks=50, border=NA, main=NA, freq=F)
})
title('Beta distributions', outer=T, line=-1)
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-57-1.png" width="672" />



## Further Reading

Many introductory econometrics textbooks have a good appendix on probability and statistics. There are many useful texts online too

* [Refresher] https://www.khanacademy.org/math/statistics-probability/probability-library/basic-theoretical-probability/a/probability-the-basics
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
sapply(1:3, function(i){
    x <- runif(100) 
    m <-  mean(x)
    hist(x,
        breaks=seq(0,1,by=.1), #for comparability
        main=NA, border=NA)
    abline(v=m, col=2, lwd=2)
    title(paste0('mean= ', round(m,2)),  font.main=1)
    return(m)
})
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-58-1.png" width="672" />

```
## [1] 0.5183512 0.5298982 0.5194884
```

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

<img src="02-BasicStats_files/figure-html/unnamed-chunk-59-1.png" width="672" />


Examine the sampling distribution of "order statistics"

``` r
# Create 300 samples, each with 1000 random uniform variables
x <- sapply(1:300, function(i) runif(1000) )
# Each row is a new sample
length(x[1,])
```

```
## [1] 300
```

``` r
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

<img src="02-BasicStats_files/figure-html/unnamed-chunk-60-1.png" width="672" />



**Complex Functions**.
You can sample more complex statistics. For example, examine the sampling distribution of the standard deviation.

``` r
three_sds <- c(  sd(runif(100)),  sd(runif(100)),  sd(runif(100))  )
three_sds
```

```
## [1] 0.2962351 0.2603989 0.2835583
```

``` r
sample_sds <- sapply(1:1000, function(i){
    s <- sd(runif(100))
    return(s)
})
hist(sample_sds, breaks=50, border=NA,
    col=4, font.main=1,
    main='Sampling Distribution of the sd')
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-61-1.png" width="672" />


Try any function!

``` r
fun_of_rv <- function(f, n=100){
  x <- runif(n)
  y <- f(x)
  return(y)
}

fun_of_rv( f=mean )
```

```
## [1] 0.5394034
```

``` r
fun_of_rv( f=function(i){ diff(range(exp(i))) } )
```

```
## [1] 1.703668
```


## Intervals

Using either the bootstrap or jackknife distribution, we can calculate 

* *confidence interval:* range your statistic varies across different samples.
* *standard error*: variance of your statistic across different samples.



``` r
sample_means <- apply(x,1,mean)
# standard error
sd(sample_means)
```

```
## [1] 0.01606439
```

Note that in some cases (not discussed here), you can estimate the standard error to get a confidence interval.

``` r
x00 <- x[1,]
# standard error
s00 <- sd(x00)/sqrt(length(x00))
ci <- mean(x00) + c(1.96, -1.96)*s00
```


**Confidence Interval**. Compute the upper and lower quantiles of the sampling distribution.


``` r
bks <- seq(.4,.6,by=.001)
hist(sample_means, breaks=bks, border=NA,
    col=rgb(0,0,0,.25), font.main=1,
    main='Confidence Interval for the mean')

# Middle 90%
mq <- quantile(sample_means, probs=c(.05,.95))
abline(v=mq)
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-65-1.png" width="672" />

``` r
paste0('we are 90% confident that the mean is between ', 
    round(mq[1],2), ' and ', round(mq[2],2) )
```

```
## [1] "we are 90% confident that the mean is between 0.47 and 0.53"
```


``` r
sample_quants <- apply(x,1,quantile, probs=.99)

bks <- seq(.92,1,by=.001)
hist(sample_quants, breaks=bks, border=NA,
    col=rgb(0,0,0,.25), font.main=1,
    main='Confidence Interval for the 99% percentile')

# Middle 95%
mq <- quantile(sample_quants, probs=c(.025,.975))
abline(v=mq)
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-66-1.png" width="672" />

``` r
paste0('we are 95% confident that the upper percentile is between ', 
    round(mq[1],2), ' and ', round(mq[2],2) )
```

```
## [1] "we are 95% confident that the upper percentile is between 0.97 and 1"
```


(See also https://online.stat.psu.edu/stat200/lesson/4/4.4/4.4.2)

**Prediction Interval**. Compute the frequency each value was covered.


``` r
# Middle 90% of values
xq0 <- quantile(x, probs=c(.05,.95))

bks <- seq(0,1,by=.01)
hist(x, breaks=bks, border=NA,
    main='Prediction Interval', font.main=1)
abline(v=xq0)
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-67-1.png" width="672" />

``` r
paste0('we are 90% confident that the a future data point will be between ', 
    round(xq0[1],2), ' and ', round(xq0[2],2) )
```

```
## [1] "we are 90% confident that the a future data point will be between 0.05 and 0.95"
```

**Advanced Intervals**.
In many cases, we want a X% interval to mean that X% of the intervals we generate will contain the mean (confidence interval) or new observations (prediction interval). E.g., a 50% CI means that half of intervals we create contain the true mean.


``` r
# Confidence Interval for each sample
xq <- apply(x,1, function(r){ mean(r) + c(-1,1)*sd(r) })
# First 4 interval estimates
xq[,1:4]
```

```
##           [,1]      [,2]      [,3]      [,4]
## [1,] 0.2000212 0.1996063 0.1976142 0.2254125
## [2,] 0.7939777 0.8010905 0.7666877 0.7836741
```

``` r
# Frequency each point was in an interval
bks <- seq(0,1,by=.01)
xcov <- sapply(bks, function(b){
    bl <- b >= xq[1,]
    bu <- b <= xq[2,]
    mean( bl & bu )
})
plot.new()
plot.window(xlim=c(0,1), ylim=c(0,1))
polygon( c(bks, rev(bks)), c(xcov, xcov*0), col=grey(.5,.5), border=NA)
mtext('Frequency each value was in an interval',2, line=2.5)
axis(1)
axis(2)

# 50\% Coverage
c_ul <- range(bks[xcov>=.5])
abline(h=.5, lwd=2)
segments(c_ul,0,c_ul,.5, lty=2)
c_ul # 50% confidence interval
```

```
## [1] 0.22 0.78
```

``` r
# True mean
abline(v=.5, col=2, lwd=2)
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-68-1.png" width="672" />


## Resampling

Often, we only have one sample. 


``` r
sample_dat <- USArrests$Murder
mean(sample_dat)
```

```
## [1] 7.788
```

How then can we estimate the sampling distribution of a statistic? We can "resample" our data. 
Hesterberg (2015) provides a nice illustration of the idea. The two most basic versions are the jackknife and the bootstrap, which are discussed below.



<img src="02-BasicStats_files/figure-html/unnamed-chunk-71-1.png" width="672" />



**Jackknife Distribution**. Here, we compute all "leave-one-out" estimates. Specifically, for a dataset with $n$ observations, the jackknife uses $n-1$ observations other than $i$ for each unique subsample. Taking the mean, for example, we have 
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

<img src="02-BasicStats_files/figure-html/unnamed-chunk-72-1.png" width="672" />


**Bootstrap Distribution**. Here, we draw $n$ observations with replacement from the original data to create a bootstrap sample and calculate a statistic. Each bootstrap sample $b=1...B$ uses a random set of observations (denoted $N_{b}$) to compute a statistic. We repeat that many times, say $B=9999$, to estimate the sampling distribution. Consider the sample mean as an example;
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

<img src="02-BasicStats_files/figure-html/unnamed-chunk-73-1.png" width="672" />

**Caveat**.
Note that we do not use the mean of the bootstrap or jackknife statistics as a replacement for the original estimate. This is because the bootstrap and jackknife distributions are centered at the observed statistic, not the population parameter. (The bootstrapped mean is centered at the sample mean, not the population mean.) This means that we cannot use the bootstrap to improve on $\overline{x}$; no matter how many bootstrap samples we take. We can, however, use the jackknife and bootstrap to estimate sampling variability.

**Intervals**.
Note that both methods provide imperfect estimates, and can give different numbers. Until you know more, a conservative approach is to take the larger estimate.

``` r
# Boot CI
boot_ci <- quantile(Bmeans, probs=c(.025, .975))
boot_ci
```

```
##    2.5%   97.5% 
## 6.58200 8.97005
```

``` r
# Jack CI
jack_ci <- quantile(Jmeans, probs=c(.025, .975))
jack_ci
```

```
##     2.5%    97.5% 
## 7.621582 7.904082
```

``` r
# more conservative estimate
ci_est <- boot_ci
```

Also note that the *standard deviation* refers to variance within a single sample, and is hence different from the standard error. Nonetheless, they can both be used to estimate the variability of a statistic.

``` r
boot_se <- sd(Bmeans)

sample_sd <- sd(sample_dat)

c(boot_se, sample_sd/sqrt(n))
```

```
## [1] 0.6056902 0.6159621
```




## Value of More Data

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

<img src="02-BasicStats_files/figure-html/unnamed-chunk-76-1.png" width="672" />


## Further Reading

See 

* https://www.r-bloggers.com/2025/02/bootstrap-vs-standard-error-confidence-intervals/

# Hypothesis Tests
***

## Basic Ideas

In this section, we test hypotheses using *data-driven* methods that assume much less about the data generating process. There are two main ways to conduct a hypothesis test to do so: inverting a confidence interval and imposing the null.

**Invert a CI**.
One main way to conduct hypothesis tests is to examine whether a confidence interval contains a hypothesized value. We then have this decision rule

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

<img src="02-BasicStats_files/figure-html/unnamed-chunk-77-1.png" width="672" />

**Impose the Null**.
We can also compute a *null distribution*: the sampling distribution of the statistic under the null hypothesis (assuming your null hypothesis was true). We focus on the simplest, the bootstrap, where loop through a large number of simulations. In each iteration of the loop, we drop impose the null hypothesis and reestimate the statistic of interest. We then calculate the standard deviation of the statistic across all ``resamples''. Specifically, we compute the distribution of t-values on data with randomly reshuffled outcomes (imposing the null), and compare how extreme the observed value is.

``` r
sample_dat <- USArrests$Murder
sample_mean <- mean(sample_dat)

# Bootstrap estimates
set.seed(1)
Bmeans0 <- sapply(1:10^4, function(i) {
    dat_b <- sample(sample_dat, replace=T) 
    mean_b <- mean(dat_b) + (8 - sample_mean) # impose the null by recentering
    return(mean_b)
})
hist(Bmeans0, breaks=25, border=NA,
    main='', xlab=expression( bar(X)[b]) )
ci_95 <- quantile(Bmeans0, probs=c(.025, .975))
abline(v=ci_95, lwd=2)

abline(v=sample_mean, lwd=2, col=2)
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-78-1.png" width="672" />


## Default Statistics

**p-values**. A *p-value* is the frequency you would see something as extreme as your statistic when sampling from the null distribution.


``` r
# P( boot0_means > sample_mean) 
# NULL: mean=8
That_NullDist1 <- ecdf(Bmeans0)
plot(That_NullDist1,
    xlab=expression( beta[b] ),
    main='Null Bootstrap Distribution for means', font.main=1)
abline(v=sample_mean, col='red')
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-79-1.png" width="672" />

``` r
p <- That_NullDist1(sample_mean)
p
```

```
## [1] 0.3751
```

There are three associated tests: the two-sided test (observed statistic is extremely high or low) or one of the one-sided tests (observed statistic is extremely low, observed statistic is extremely high). In either case, typically "p<.05: statistically significant" and "p>.05: statistically insignificant".^[Note that the p-value is not the ``probability that we reject the null based on the data we have and given the null is true''. This is called the statistical power of the test.]

``` r
# One-Sided Test, ALTERNATIVE: mean < 8
if(p >.05){
    message('fail to reject the null that sample_mean=8 at the 5% level')
} else {
    message('reject the null that sample_mean=8 in favor of <8 at the 5% level')
}

# Two-Sided Test, ALTERNATIVE: mean < 8 or mean >8
if( p >.025 | p >.975){
    message('fail to reject the null that sample_mean=8 at the 5% level')
} else {
    message('reject the null that sample_mean=8 in favor of either <8 or >8 at the 5% level')
}
```


**t-values**. A t-value standardizes the statistic you are using for hypothesis testing.

``` r
jack_se <- sd(Jmeans)
mean0 <- 8
jack_t <- (sample_mean - mean0)/jack_se
```
There are several benefits to this:

* makes the statistic comparable across different studies
* makes the null distribution theoretically known (at least approximately)
* makes the null distribution not depend on theoretical parameters ($\sigma$)


``` r
# Two-Sided Test, based on theory
# 1-pt( abs(jack_t), n-1) + pt(-abs(jack_t), n-1)
```
In another statistics class, you will learn the math behind the null t-distribution. In this class, we skip this because we can simply bootstrap the t-statistic too.

``` r
set.seed(1)
boot_t0 <- sapply(1:10^4, function(i) {
    dat_b <- sample(sample_dat, replace=T) 
    mean_b <- mean(dat_b) + (8 - sample_mean) # impose the null by recentering
    jack_t <- (mean_b - mean0)/jack_se
})

# Two Sided Test for P(t > jack_t or  t < -jack_t | Null)
That_NullDist2 <- ecdf(abs(boot_t0))
plot(That_NullDist2, xlim=range(boot_t0, jack_t),
    xlab=expression( abs(hat(t)[b]) ),
    main='Null Bootstrap Distribution for t', font.main=1)
abline(v=abs(jack_t), col='red')
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-83-1.png" width="672" />

``` r
p <- That_NullDist2( abs(jack_t) ) 
p
```

```
## [1] 0.2659
```

``` r
if(p >.05){
    message('fail to reject the null that sample_mean=8 at the 5% level')
} else {
    message('reject the null that sample_mean=8 in favor of either <8 or >8 at the 5% level')
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

Although it not necessary, we will assume that each $X_{is}$ is an independent observation for simplicity. 


``` r
# Sample 1
n1 <- 100
x1 <- rnorm(n1, 0, 2)
# Sample 2
n2 <- 80
x2 <- rnorm(n1, 1, 1)

par(mfrow=c(1,2))
bks <- seq(-7,7, by=.5)
hist(x1, border=NA, breaks=bks,
    main='Sample 1', font.main=1)

hist(x2, border=NA, breaks=bks, 
    main='Sample 2', font.main=1)
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-85-1.png" width="672" />

There may be several differences between these samples. Often, the first summary statistic we investigate is the difference in means. 

**Equal Means**. The sample mean $\overline{X}_{s}$ is the average value of all the observations in the sample. We want to know if the means are different. To test this hypothesis, we examine the differences term
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

<img src="02-BasicStats_files/figure-html/unnamed-chunk-86-1.png" width="672" />

``` r
ecdf(boot_d)(0)
```

```
## [1] 1
```

Just as with one sample tests, we can standardize $D$ into a $t$ statistic. (In which case we also theoretically know the distribution.) Similarly, we can also compute one or two sided hypothesis tests. 


**Equal Quantiles or Variances**.

The above procedure generalized from "means" to other statistics like "variances" or "quantiles".


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

<img src="02-BasicStats_files/figure-html/unnamed-chunk-87-1.png" width="672" />

``` r
ecdf(boot_d)(0)
```

```
## [1] 0.9995
```

``` r
# 2-Sided Test for SD Differences
#d <- sd(x2) - sd(x1)
boot_d <- boot_fun(sd)
hist(boot_d, border=NA, font.main=1,
    main='Difference in Standard Deviations')
abline(v=quantile(boot_d, probs=c(.025, .975)), lwd=2)
abline(v=0, lwd=2, col=2)
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-87-2.png" width="672" />

``` r
ecdf(boot_d)(0)
```

```
## [1] 0
```

``` r
# Try any function!
# boot_fun( function(xs) { IQR(xs)/median(xs) } )
```


## Distributional Tests

We can also examine whether there are any differences between the entire *distributions*

``` r
# Compute Quantiles
quants <- seq(0,1,length.out=101)
Q1 <- quantile(x1, probs=quants)
Q2 <- quantile(x2, probs=quants)

# Compare Distributions via Quantiles
rx <- range(c(x1, x2))
par(mfrow=c(1,2))
plot(rx, c(0,1), type='n', font.main=1,
    main='Distributional Comparison',
    xlab=expression(Q[s]),
    ylab=expression(F[s]))
lines(Q1, quants, col=2)
lines(Q2, quants, col=4)
legend('topleft', col=c(2,4), lty=1,
legend=c('F1', 'F2'))

# Compare Quantiles
plot(Q1, Q2, xlim=rx, ylim=rx,
    main='Quantile-Quantile Plot', font.main=1,
pch=16, col=grey(0,.25))
abline(a=0,b=1,lty=2)
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-88-1.png" width="672" />

We can also test for a differences in entire *distributions*, using all sample data $x \in \{X_1\} \cup \{X_2\}$.

``` r
# Sorted Sample Data
x1 <- sort(x1)
x2 <- sort(x2)
x <- sort(c(x1, x2))

# Distributions
F1 <- ecdf(x1)(x)
F2 <- ecdf(x2)(x)

library(twosamples)
```

The starting point is the Kolmogorov-Smirnov Statistic: the maximum absolute difference between two CDF's. 
\begin{eqnarray}
KS &=& \max_{x} |F_{1}(x)- F_{2}(x)|^{p}.
\end{eqnarray}


``` r
# Kolmogorov-Smirnov
KSq <- which.max(abs(F2 - F1))
KSqv <- round(twosamples::ks_stat(x1, x2),2)

plot(range(x), c(0,1), type="n", xlab='x', ylab='ECDF')
title(paste0('KS = ', KSqv), font.main=1)
segments(x[KSq], F1[KSq], x[KSq], F2[KSq], lwd=1, col=grey(0,.5))
lines(x, F1, col=2, lwd=2)
lines(x, F2, col=4, lwd=2)
legend('bottomright', col=c(2,4), lty=1,
    legend=c(expression(F[1]), expression(F[2])))
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-90-1.png" width="672" />

An intuitive alternative is the Cramer-von Mises Statistic: the sum of absolute distances (raised to a power) between two CDF's. 
\begin{eqnarray}
CVM=\sum_{x} |F_{1}(x)- F_{2}(x)|^{p}.
\end{eqnarray}


``` r
# Cramer-von Mises Statistic (p=2)
CVMqv <- round(twosamples::cvm_stat(x1, x2, power=2), 2) 

plot(range(x), c(0,1), type="n", xlab='x', ylab='ECDF')
segments(x, F1, x, F2, lwd=.5, col=grey(0,.1))
lines(x, F1, col=2, lwd=2)
lines(x, F2, col=4, lwd=2)
title(paste0('CVM = ',CVMqv), font.main=1)
```

<img src="02-BasicStats_files/figure-html/unnamed-chunk-91-1.png" width="672" />

Just as before, you use bootstrapping for hypothesis testing.

``` r
twosamples::cvm_test(x1, x2)
```

```
## Test Stat   P-Value 
##  11.30520   0.00025
```


# Data Analysis
***


## Reading In

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


**Github**.
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

**Base**.
While additional packages can make your code faster, they also create dependancies that can lead to problems. So learn base R well before becoming dependant on other packages

* https://bitsofanalytics.org/posts/base-vs-tidy/
* https://jtr13.github.io/cc21fall2/comparison-among-base-r-tidyverse-and-datatable.html




## Cleaning Data

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
```

```
## [1] FALSE
```

``` r
# Inspect any differences

# Merging data in wide format, Third Attempt with dedicated package
# (highest performance but with new type of object)
library(data.table)
dat_merged_longDT <- as.data.table(dat_merged_long)
dat_melted <- melt(dat_merged_longDT, id.vars=c('ID', 'DF'))
dat_merged_wide3 <- dcast(dat_melted, ID~DF+variable)

## CHECK they are the same.
identical(dat_merged_wide, dat_merged_wide3)
```

```
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
```

```
## [1] FALSE
```

``` r
# Further Inspect
dat_merged_long2 <- dat_merged_long2[,c('ID','x','y','DF')]
mapply( identical, dat_merged_long2, dat_merged_long)
```

```
##    ID     x     y    DF 
##  TRUE  TRUE  TRUE FALSE
```

For more tips, see https://raw.githubusercontent.com/rstudio/cheatsheets/main/data-import.pdf and https://cran.r-project.org/web/packages/data.table/vignettes/datatable-reshape.html
<!--\url{https://github.com/rstudio/cheatsheets/raw/master/data-transformation.pdf}-->



## Polishing


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

<img src="02-BasicStats_files/figure-html/unnamed-chunk-102-1.png" width="672" />

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

<img src="02-BasicStats_files/figure-html/unnamed-chunk-103-1.png" width="672" />


**Saving**.
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


**Tables**.

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


## Interactive


**Tables**.

You can create a basic interactive table to explore raw data.


``` r
data("USArrests")
library(reactable)
reactable(USArrests, filterable=T, highlight=T)
```

```{=html}
<div class="reactable html-widget html-fill-item" id="htmlwidget-25b1251c2bae0d612df9" style="width:auto;height:auto;"></div>
<script type="application/json" data-for="htmlwidget-25b1251c2bae0d612df9">{"x":{"tag":{"name":"Reactable","attribs":{"data":{".rownames":["Alabama","Alaska","Arizona","Arkansas","California","Colorado","Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois","Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland","Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana","Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York","North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania","Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah","Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"],"Murder":[13.2,10,8.1,8.8,9,7.9,3.3,5.9,15.4,17.4,5.3,2.6,10.4,7.2,2.2,6,9.7,15.4,2.1,11.3,4.4,12.1,2.7,16.1,9,6,4.3,12.2,2.1,7.4,11.4,11.1,13,0.8,7.3,6.6,4.9,6.3,3.4,14.4,3.8,13.2,12.7,3.2,2.2,8.5,4,5.7,2.6,6.8],"Assault":[236,263,294,190,276,204,110,238,335,211,46,120,249,113,56,115,109,249,83,300,149,255,72,259,178,109,102,252,57,159,285,254,337,45,120,151,159,106,174,279,86,188,201,120,48,156,145,81,53,161],"UrbanPop":[58,48,80,50,91,78,77,72,80,60,83,54,83,65,57,66,52,66,51,67,85,74,66,44,70,53,62,81,56,89,70,86,45,44,75,68,67,72,87,48,45,59,80,80,32,63,73,39,66,60],"Rape":[21.2,44.5,31,19.5,40.6,38.7,11.1,15.8,31.9,25.8,20.2,14.2,24,21,11.3,18,16.3,22.2,7.8,27.8,16.3,35.1,14.9,17.1,28.2,16.4,16.5,46,9.5,18.8,32.1,26.1,16.1,7.3,21.4,20,29.3,14.9,8.3,22.5,12.8,26.9,25.5,22.9,11.2,20.7,26.2,9.3,10.8,15.6]},"columns":[{"id":".rownames","name":"","type":"character","sortable":false,"filterable":false,"rowHeader":true},{"id":"Murder","name":"Murder","type":"numeric"},{"id":"Assault","name":"Assault","type":"numeric"},{"id":"UrbanPop","name":"UrbanPop","type":"numeric"},{"id":"Rape","name":"Rape","type":"numeric"}],"filterable":true,"highlight":true,"dataKey":"c49af85e0b2038b0b71caf77db2bacb3"},"children":[]},"class":"reactR_markup"},"evals":[],"jsHooks":[]}</script>
```

For further data exploration, your plots can also be made [interactive](https://r-graph-gallery.com/interactive-charts.html) via <https://plotly.com/r/>. For more details, see [examples](https://plotly-r.com/) and then [applications](https://bookdown.org/paulcbauer/applied-data-visualization/10-plotly.html).


``` r
#install.packages("plotly")
library(plotly)
```


**Histograms**. See https://plotly.com/r/histograms/

``` r
pop_mean <- mean(USArrests$UrbanPop)
murder_lowpop <- USArrests[USArrests$UrbanPop< pop_mean,'Murder']
murder_highpop <- USArrests[USArrests$UrbanPop>= pop_mean,'Murder']


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
<div class="plotly html-widget html-fill-item" id="htmlwidget-89c6aa5050c63be742a4" style="width:672px;height:480px;"></div>
<script type="application/json" data-for="htmlwidget-89c6aa5050c63be742a4">{"x":{"visdat":{"29e775fcfc8d":["function () ","plotlyVisDat"]},"cur_data":"29e775fcfc8d","attrs":{"29e775fcfc8d":{"hovertemplate":"%{y}","alpha":0.59999999999999998,"alpha_stroke":1,"sizes":[10,100],"spans":[1,20],"x":[13.199999999999999,10,8.8000000000000007,17.399999999999999,2.6000000000000001,7.2000000000000002,2.2000000000000002,9.6999999999999993,2.1000000000000001,16.100000000000001,6,4.2999999999999998,2.1000000000000001,13,0.80000000000000004,14.4,3.7999999999999998,13.199999999999999,2.2000000000000002,8.5,5.7000000000000002,6.7999999999999998],"type":"histogram","name":"Low Pop. (< Mean)","inherit":true},"29e775fcfc8d.1":{"hovertemplate":"%{y}","alpha":0.59999999999999998,"alpha_stroke":1,"sizes":[10,100],"spans":[1,20],"x":[8.0999999999999996,9,7.9000000000000004,3.2999999999999998,5.9000000000000004,15.4,5.2999999999999998,10.4,6,15.4,11.300000000000001,4.4000000000000004,12.1,2.7000000000000002,9,12.199999999999999,7.4000000000000004,11.4,11.1,7.2999999999999998,6.5999999999999996,4.9000000000000004,6.2999999999999998,3.3999999999999999,12.699999999999999,3.2000000000000002,4,2.6000000000000001],"type":"histogram","name":"High Pop (>= Mean)","inherit":true}},"layout":{"margin":{"b":40,"l":60,"t":25,"r":10},"barmode":"stack","title":"Crime and Urbanization in America 1975","xaxis":{"domain":[0,1],"automargin":true,"title":"Murders Arrests per 100,000 People"},"yaxis":{"domain":[0,1],"automargin":true,"title":"Number of States"},"legend":{"title":{"text":"<b> % Urban Pop. <\/b>"}},"hovermode":"closest","showlegend":true},"source":"A","config":{"modeBarButtonsToAdd":["hoverclosest","hovercompare"],"showSendToCloud":false},"data":[{"hovertemplate":["%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}"],"x":[13.199999999999999,10,8.8000000000000007,17.399999999999999,2.6000000000000001,7.2000000000000002,2.2000000000000002,9.6999999999999993,2.1000000000000001,16.100000000000001,6,4.2999999999999998,2.1000000000000001,13,0.80000000000000004,14.4,3.7999999999999998,13.199999999999999,2.2000000000000002,8.5,5.7000000000000002,6.7999999999999998],"type":"histogram","name":"Low Pop. (< Mean)","marker":{"color":"rgba(31,119,180,0.6)","line":{"color":"rgba(31,119,180,1)"}},"error_y":{"color":"rgba(31,119,180,0.6)"},"error_x":{"color":"rgba(31,119,180,0.6)"},"xaxis":"x","yaxis":"y","frame":null},{"hovertemplate":["%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}","%{y}"],"x":[8.0999999999999996,9,7.9000000000000004,3.2999999999999998,5.9000000000000004,15.4,5.2999999999999998,10.4,6,15.4,11.300000000000001,4.4000000000000004,12.1,2.7000000000000002,9,12.199999999999999,7.4000000000000004,11.4,11.1,7.2999999999999998,6.5999999999999996,4.9000000000000004,6.2999999999999998,3.3999999999999999,12.699999999999999,3.2000000000000002,4,2.6000000000000001],"type":"histogram","name":"High Pop (>= Mean)","marker":{"color":"rgba(255,127,14,0.6)","line":{"color":"rgba(255,127,14,1)"}},"error_y":{"color":"rgba(255,127,14,0.6)"},"error_x":{"color":"rgba(255,127,14,0.6)"},"xaxis":"x","yaxis":"y","frame":null}],"highlight":{"on":"plotly_click","persistent":false,"dynamic":false,"selectize":false,"opacityDim":0.20000000000000001,"selected":{"opacity":1},"debounce":0},"shinyEvents":["plotly_hover","plotly_click","plotly_selected","plotly_relayout","plotly_brushed","plotly_brushing","plotly_clickannotation","plotly_doubleclick","plotly_deselect","plotly_afterplot","plotly_sunburstclick"],"base_url":"https://plot.ly"},"evals":[],"jsHooks":[]}</script>
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
<div class="plotly html-widget html-fill-item" id="htmlwidget-068f3a3e21d0ad35a7fe" style="width:672px;height:480px;"></div>
<script type="application/json" data-for="htmlwidget-068f3a3e21d0ad35a7fe">{"x":{"visdat":{"29e76190cb7a":["function () ","plotlyVisDat"]},"cur_data":"29e76190cb7a","attrs":{"29e76190cb7a":{"y":{},"pointpos":0,"boxpoints":"all","hoverinfo":"text","text":{},"color":{},"alpha":0.59999999999999998,"alpha_stroke":1,"sizes":[10,100],"spans":[1,20],"type":"box"}},"layout":{"margin":{"b":40,"l":60,"t":25,"r":10},"showlegend":false,"title":"Crime and Urbanization in America 1975","xaxis":{"domain":[0,1],"automargin":true,"title":"Percent of People in an Urban Area"},"yaxis":{"domain":[0,1],"automargin":true,"title":"Murders Arrests per 100,000 People"},"hovermode":"closest"},"source":"A","config":{"modeBarButtonsToAdd":["hoverclosest","hovercompare"],"showSendToCloud":false},"data":[{"fillcolor":"rgba(102,194,165,0.6)","y":[16.100000000000001,13,0.80000000000000004,3.7999999999999998,2.2000000000000002,5.7000000000000002],"pointpos":0,"boxpoints":"all","hoverinfo":["text","text","text","text","text","text"],"text":["<b> Mississippi <\/b> <br>Urban  : 44 <br>Assault: 259 <br>Murder : 16.1","<b> North Carolina <\/b> <br>Urban  : 45 <br>Assault: 337 <br>Murder : 13","<b> North Dakota <\/b> <br>Urban  : 44 <br>Assault: 45 <br>Murder : 0.8","<b> South Dakota <\/b> <br>Urban  : 45 <br>Assault: 86 <br>Murder : 3.8","<b> Vermont <\/b> <br>Urban  : 32 <br>Assault: 48 <br>Murder : 2.2","<b> West Virginia <\/b> <br>Urban  : 39 <br>Assault: 81 <br>Murder : 5.7"],"type":"box","name":"(31.9,46.8]","marker":{"color":"rgba(102,194,165,0.6)","line":{"color":"rgba(102,194,165,1)"}},"line":{"color":"rgba(102,194,165,1)"},"xaxis":"x","yaxis":"y","frame":null},{"fillcolor":"rgba(252,141,98,0.6)","y":[13.199999999999999,10,8.8000000000000007,17.399999999999999,2.6000000000000001,2.2000000000000002,9.6999999999999993,2.1000000000000001,6,2.1000000000000001,14.4,13.199999999999999,6.7999999999999998],"pointpos":0,"boxpoints":"all","hoverinfo":["text","text","text","text","text","text","text","text","text","text","text","text","text"],"text":["<b> Alabama <\/b> <br>Urban  : 58 <br>Assault: 236 <br>Murder : 13.2","<b> Alaska <\/b> <br>Urban  : 48 <br>Assault: 263 <br>Murder : 10","<b> Arkansas <\/b> <br>Urban  : 50 <br>Assault: 190 <br>Murder : 8.8","<b> Georgia <\/b> <br>Urban  : 60 <br>Assault: 211 <br>Murder : 17.4","<b> Idaho <\/b> <br>Urban  : 54 <br>Assault: 120 <br>Murder : 2.6","<b> Iowa <\/b> <br>Urban  : 57 <br>Assault: 56 <br>Murder : 2.2","<b> Kentucky <\/b> <br>Urban  : 52 <br>Assault: 109 <br>Murder : 9.7","<b> Maine <\/b> <br>Urban  : 51 <br>Assault: 83 <br>Murder : 2.1","<b> Montana <\/b> <br>Urban  : 53 <br>Assault: 109 <br>Murder : 6","<b> New Hampshire <\/b> <br>Urban  : 56 <br>Assault: 57 <br>Murder : 2.1","<b> South Carolina <\/b> <br>Urban  : 48 <br>Assault: 279 <br>Murder : 14.4","<b> Tennessee <\/b> <br>Urban  : 59 <br>Assault: 188 <br>Murder : 13.2","<b> Wyoming <\/b> <br>Urban  : 60 <br>Assault: 161 <br>Murder : 6.8"],"type":"box","name":"(46.8,61.5]","marker":{"color":"rgba(252,141,98,0.6)","line":{"color":"rgba(252,141,98,1)"}},"line":{"color":"rgba(252,141,98,1)"},"xaxis":"x","yaxis":"y","frame":null},{"fillcolor":"rgba(141,160,203,0.6)","y":[5.9000000000000004,7.2000000000000002,6,15.4,11.300000000000001,12.1,2.7000000000000002,9,4.2999999999999998,11.4,7.2999999999999998,6.5999999999999996,4.9000000000000004,6.2999999999999998,8.5,4,2.6000000000000001],"pointpos":0,"boxpoints":"all","hoverinfo":["text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text"],"text":["<b> Delaware <\/b> <br>Urban  : 72 <br>Assault: 238 <br>Murder : 5.9","<b> Indiana <\/b> <br>Urban  : 65 <br>Assault: 113 <br>Murder : 7.2","<b> Kansas <\/b> <br>Urban  : 66 <br>Assault: 115 <br>Murder : 6","<b> Louisiana <\/b> <br>Urban  : 66 <br>Assault: 249 <br>Murder : 15.4","<b> Maryland <\/b> <br>Urban  : 67 <br>Assault: 300 <br>Murder : 11.3","<b> Michigan <\/b> <br>Urban  : 74 <br>Assault: 255 <br>Murder : 12.1","<b> Minnesota <\/b> <br>Urban  : 66 <br>Assault: 72 <br>Murder : 2.7","<b> Missouri <\/b> <br>Urban  : 70 <br>Assault: 178 <br>Murder : 9","<b> Nebraska <\/b> <br>Urban  : 62 <br>Assault: 102 <br>Murder : 4.3","<b> New Mexico <\/b> <br>Urban  : 70 <br>Assault: 285 <br>Murder : 11.4","<b> Ohio <\/b> <br>Urban  : 75 <br>Assault: 120 <br>Murder : 7.3","<b> Oklahoma <\/b> <br>Urban  : 68 <br>Assault: 151 <br>Murder : 6.6","<b> Oregon <\/b> <br>Urban  : 67 <br>Assault: 159 <br>Murder : 4.9","<b> Pennsylvania <\/b> <br>Urban  : 72 <br>Assault: 106 <br>Murder : 6.3","<b> Virginia <\/b> <br>Urban  : 63 <br>Assault: 156 <br>Murder : 8.5","<b> Washington <\/b> <br>Urban  : 73 <br>Assault: 145 <br>Murder : 4","<b> Wisconsin <\/b> <br>Urban  : 66 <br>Assault: 53 <br>Murder : 2.6"],"type":"box","name":"(61.5,76.2]","marker":{"color":"rgba(141,160,203,0.6)","line":{"color":"rgba(141,160,203,1)"}},"line":{"color":"rgba(141,160,203,1)"},"xaxis":"x","yaxis":"y","frame":null},{"fillcolor":"rgba(231,138,195,0.6)","y":[8.0999999999999996,9,7.9000000000000004,3.2999999999999998,15.4,5.2999999999999998,10.4,4.4000000000000004,12.199999999999999,7.4000000000000004,11.1,3.3999999999999999,12.699999999999999,3.2000000000000002],"pointpos":0,"boxpoints":"all","hoverinfo":["text","text","text","text","text","text","text","text","text","text","text","text","text","text"],"text":["<b> Arizona <\/b> <br>Urban  : 80 <br>Assault: 294 <br>Murder : 8.1","<b> California <\/b> <br>Urban  : 91 <br>Assault: 276 <br>Murder : 9","<b> Colorado <\/b> <br>Urban  : 78 <br>Assault: 204 <br>Murder : 7.9","<b> Connecticut <\/b> <br>Urban  : 77 <br>Assault: 110 <br>Murder : 3.3","<b> Florida <\/b> <br>Urban  : 80 <br>Assault: 335 <br>Murder : 15.4","<b> Hawaii <\/b> <br>Urban  : 83 <br>Assault: 46 <br>Murder : 5.3","<b> Illinois <\/b> <br>Urban  : 83 <br>Assault: 249 <br>Murder : 10.4","<b> Massachusetts <\/b> <br>Urban  : 85 <br>Assault: 149 <br>Murder : 4.4","<b> Nevada <\/b> <br>Urban  : 81 <br>Assault: 252 <br>Murder : 12.2","<b> New Jersey <\/b> <br>Urban  : 89 <br>Assault: 159 <br>Murder : 7.4","<b> New York <\/b> <br>Urban  : 86 <br>Assault: 254 <br>Murder : 11.1","<b> Rhode Island <\/b> <br>Urban  : 87 <br>Assault: 174 <br>Murder : 3.4","<b> Texas <\/b> <br>Urban  : 80 <br>Assault: 201 <br>Murder : 12.7","<b> Utah <\/b> <br>Urban  : 80 <br>Assault: 120 <br>Murder : 3.2"],"type":"box","name":"(76.2,91.1]","marker":{"color":"rgba(231,138,195,0.6)","line":{"color":"rgba(231,138,195,1)"}},"line":{"color":"rgba(231,138,195,1)"},"xaxis":"x","yaxis":"y","frame":null}],"highlight":{"on":"plotly_click","persistent":false,"dynamic":false,"selectize":false,"opacityDim":0.20000000000000001,"selected":{"opacity":1},"debounce":0},"shinyEvents":["plotly_hover","plotly_click","plotly_selected","plotly_relayout","plotly_brushed","plotly_brushing","plotly_clickannotation","plotly_doubleclick","plotly_deselect","plotly_afterplot","plotly_sunburstclick"],"base_url":"https://plot.ly"},"evals":[],"jsHooks":[]}</script>
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
<div class="plotly html-widget html-fill-item" id="htmlwidget-51205323a2a1fdc211fe" style="width:672px;height:480px;"></div>
<script type="application/json" data-for="htmlwidget-51205323a2a1fdc211fe">{"x":{"visdat":{"29e77c24c2bd":["function () ","plotlyVisDat"]},"cur_data":"29e77c24c2bd","attrs":{"29e77c24c2bd":{"x":{},"y":{},"mode":"markers","hoverinfo":"text","text":{},"marker":{"size":{},"opacity":0.5,"showscale":true,"colorbar":{"title":"Murder Arrests (per 100,000)"}},"color":{},"alpha_stroke":1,"sizes":[10,100],"spans":[1,20],"type":"scatter"}},"layout":{"margin":{"b":40,"l":60,"t":25,"r":10},"showlegend":false,"title":"Crime and Urbanization in America 1975","xaxis":{"domain":[0,1],"automargin":true,"title":"Percent of People in an Urban Area"},"yaxis":{"domain":[0,1],"automargin":true,"title":"Assault Arrests per 100,000 People"},"hovermode":"closest"},"source":"A","config":{"modeBarButtonsToAdd":["hoverclosest","hovercompare"],"showSendToCloud":false},"data":[{"x":[58,48,80,50,91,78,77,72,80,60,83,54,83,65,57,66,52,66,51,67,85,74,66,44,70,53,62,81,56,89,70,86,45,44,75,68,67,72,87,48,45,59,80,80,32,63,73,39,66,60],"y":[236,263,294,190,276,204,110,238,335,211,46,120,249,113,56,115,109,249,83,300,149,255,72,259,178,109,102,252,57,159,285,254,337,45,120,151,159,106,174,279,86,188,201,120,48,156,145,81,53,161],"mode":"markers","hoverinfo":["text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text","text"],"text":["<b> Alabama <\/b> <br>Urban  : 58 <br>Assault: 236 <br>Murder : 13.2","<b> Alaska <\/b> <br>Urban  : 48 <br>Assault: 263 <br>Murder : 10","<b> Arizona <\/b> <br>Urban  : 80 <br>Assault: 294 <br>Murder : 8.1","<b> Arkansas <\/b> <br>Urban  : 50 <br>Assault: 190 <br>Murder : 8.8","<b> California <\/b> <br>Urban  : 91 <br>Assault: 276 <br>Murder : 9","<b> Colorado <\/b> <br>Urban  : 78 <br>Assault: 204 <br>Murder : 7.9","<b> Connecticut <\/b> <br>Urban  : 77 <br>Assault: 110 <br>Murder : 3.3","<b> Delaware <\/b> <br>Urban  : 72 <br>Assault: 238 <br>Murder : 5.9","<b> Florida <\/b> <br>Urban  : 80 <br>Assault: 335 <br>Murder : 15.4","<b> Georgia <\/b> <br>Urban  : 60 <br>Assault: 211 <br>Murder : 17.4","<b> Hawaii <\/b> <br>Urban  : 83 <br>Assault: 46 <br>Murder : 5.3","<b> Idaho <\/b> <br>Urban  : 54 <br>Assault: 120 <br>Murder : 2.6","<b> Illinois <\/b> <br>Urban  : 83 <br>Assault: 249 <br>Murder : 10.4","<b> Indiana <\/b> <br>Urban  : 65 <br>Assault: 113 <br>Murder : 7.2","<b> Iowa <\/b> <br>Urban  : 57 <br>Assault: 56 <br>Murder : 2.2","<b> Kansas <\/b> <br>Urban  : 66 <br>Assault: 115 <br>Murder : 6","<b> Kentucky <\/b> <br>Urban  : 52 <br>Assault: 109 <br>Murder : 9.7","<b> Louisiana <\/b> <br>Urban  : 66 <br>Assault: 249 <br>Murder : 15.4","<b> Maine <\/b> <br>Urban  : 51 <br>Assault: 83 <br>Murder : 2.1","<b> Maryland <\/b> <br>Urban  : 67 <br>Assault: 300 <br>Murder : 11.3","<b> Massachusetts <\/b> <br>Urban  : 85 <br>Assault: 149 <br>Murder : 4.4","<b> Michigan <\/b> <br>Urban  : 74 <br>Assault: 255 <br>Murder : 12.1","<b> Minnesota <\/b> <br>Urban  : 66 <br>Assault: 72 <br>Murder : 2.7","<b> Mississippi <\/b> <br>Urban  : 44 <br>Assault: 259 <br>Murder : 16.1","<b> Missouri <\/b> <br>Urban  : 70 <br>Assault: 178 <br>Murder : 9","<b> Montana <\/b> <br>Urban  : 53 <br>Assault: 109 <br>Murder : 6","<b> Nebraska <\/b> <br>Urban  : 62 <br>Assault: 102 <br>Murder : 4.3","<b> Nevada <\/b> <br>Urban  : 81 <br>Assault: 252 <br>Murder : 12.2","<b> New Hampshire <\/b> <br>Urban  : 56 <br>Assault: 57 <br>Murder : 2.1","<b> New Jersey <\/b> <br>Urban  : 89 <br>Assault: 159 <br>Murder : 7.4","<b> New Mexico <\/b> <br>Urban  : 70 <br>Assault: 285 <br>Murder : 11.4","<b> New York <\/b> <br>Urban  : 86 <br>Assault: 254 <br>Murder : 11.1","<b> North Carolina <\/b> <br>Urban  : 45 <br>Assault: 337 <br>Murder : 13","<b> North Dakota <\/b> <br>Urban  : 44 <br>Assault: 45 <br>Murder : 0.8","<b> Ohio <\/b> <br>Urban  : 75 <br>Assault: 120 <br>Murder : 7.3","<b> Oklahoma <\/b> <br>Urban  : 68 <br>Assault: 151 <br>Murder : 6.6","<b> Oregon <\/b> <br>Urban  : 67 <br>Assault: 159 <br>Murder : 4.9","<b> Pennsylvania <\/b> <br>Urban  : 72 <br>Assault: 106 <br>Murder : 6.3","<b> Rhode Island <\/b> <br>Urban  : 87 <br>Assault: 174 <br>Murder : 3.4","<b> South Carolina <\/b> <br>Urban  : 48 <br>Assault: 279 <br>Murder : 14.4","<b> South Dakota <\/b> <br>Urban  : 45 <br>Assault: 86 <br>Murder : 3.8","<b> Tennessee <\/b> <br>Urban  : 59 <br>Assault: 188 <br>Murder : 13.2","<b> Texas <\/b> <br>Urban  : 80 <br>Assault: 201 <br>Murder : 12.7","<b> Utah <\/b> <br>Urban  : 80 <br>Assault: 120 <br>Murder : 3.2","<b> Vermont <\/b> <br>Urban  : 32 <br>Assault: 48 <br>Murder : 2.2","<b> Virginia <\/b> <br>Urban  : 63 <br>Assault: 156 <br>Murder : 8.5","<b> Washington <\/b> <br>Urban  : 73 <br>Assault: 145 <br>Murder : 4","<b> West Virginia <\/b> <br>Urban  : 39 <br>Assault: 81 <br>Murder : 5.7","<b> Wisconsin <\/b> <br>Urban  : 66 <br>Assault: 53 <br>Murder : 2.6","<b> Wyoming <\/b> <br>Urban  : 60 <br>Assault: 161 <br>Murder : 6.8"],"marker":{"colorbar":{"title":"Murder Arrests (per 100,000)","ticklen":2},"cmin":0.80000000000000004,"cmax":17.399999999999999,"colorscale":[["0","rgba(68,1,84,1)"],["0.0416666666666667","rgba(70,19,97,1)"],["0.0833333333333333","rgba(72,32,111,1)"],["0.125","rgba(71,45,122,1)"],["0.166666666666667","rgba(68,58,128,1)"],["0.208333333333333","rgba(64,70,135,1)"],["0.25","rgba(60,82,138,1)"],["0.291666666666667","rgba(56,93,140,1)"],["0.333333333333333","rgba(49,104,142,1)"],["0.375","rgba(46,114,142,1)"],["0.416666666666667","rgba(42,123,142,1)"],["0.458333333333333","rgba(38,133,141,1)"],["0.5","rgba(37,144,140,1)"],["0.541666666666667","rgba(33,154,138,1)"],["0.583333333333333","rgba(39,164,133,1)"],["0.625","rgba(47,174,127,1)"],["0.666666666666667","rgba(53,183,121,1)"],["0.708333333333333","rgba(79,191,110,1)"],["0.75","rgba(98,199,98,1)"],["0.791666666666667","rgba(119,207,85,1)"],["0.833333333333333","rgba(147,214,70,1)"],["0.875","rgba(172,220,52,1)"],["0.916666666666667","rgba(199,225,42,1)"],["0.958333333333333","rgba(226,228,40,1)"],["1","rgba(253,231,37,1)"]],"showscale":true,"color":[13.199999999999999,10,8.0999999999999996,8.8000000000000007,9,7.9000000000000004,3.2999999999999998,5.9000000000000004,15.4,17.399999999999999,5.2999999999999998,2.6000000000000001,10.4,7.2000000000000002,2.2000000000000002,6,9.6999999999999993,15.4,2.1000000000000001,11.300000000000001,4.4000000000000004,12.1,2.7000000000000002,16.100000000000001,9,6,4.2999999999999998,12.199999999999999,2.1000000000000001,7.4000000000000004,11.4,11.1,13,0.80000000000000004,7.2999999999999998,6.5999999999999996,4.9000000000000004,6.2999999999999998,3.3999999999999999,14.4,3.7999999999999998,13.199999999999999,12.699999999999999,3.2000000000000002,2.2000000000000002,8.5,4,5.7000000000000002,2.6000000000000001,6.7999999999999998],"size":[13.199999999999999,10,8.0999999999999996,8.8000000000000007,9,7.9000000000000004,3.2999999999999998,5.9000000000000004,15.4,17.399999999999999,5.2999999999999998,2.6000000000000001,10.4,7.2000000000000002,2.2000000000000002,6,9.6999999999999993,15.4,2.1000000000000001,11.300000000000001,4.4000000000000004,12.1,2.7000000000000002,16.100000000000001,9,6,4.2999999999999998,12.199999999999999,2.1000000000000001,7.4000000000000004,11.4,11.1,13,0.80000000000000004,7.2999999999999998,6.5999999999999996,4.9000000000000004,6.2999999999999998,3.3999999999999999,14.4,3.7999999999999998,13.199999999999999,12.699999999999999,3.2000000000000002,2.2000000000000002,8.5,4,5.7000000000000002,2.6000000000000001,6.7999999999999998],"opacity":0.5,"line":{"colorbar":{"title":"","ticklen":2},"cmin":0.80000000000000004,"cmax":17.399999999999999,"colorscale":[["0","rgba(68,1,84,1)"],["0.0416666666666667","rgba(70,19,97,1)"],["0.0833333333333333","rgba(72,32,111,1)"],["0.125","rgba(71,45,122,1)"],["0.166666666666667","rgba(68,58,128,1)"],["0.208333333333333","rgba(64,70,135,1)"],["0.25","rgba(60,82,138,1)"],["0.291666666666667","rgba(56,93,140,1)"],["0.333333333333333","rgba(49,104,142,1)"],["0.375","rgba(46,114,142,1)"],["0.416666666666667","rgba(42,123,142,1)"],["0.458333333333333","rgba(38,133,141,1)"],["0.5","rgba(37,144,140,1)"],["0.541666666666667","rgba(33,154,138,1)"],["0.583333333333333","rgba(39,164,133,1)"],["0.625","rgba(47,174,127,1)"],["0.666666666666667","rgba(53,183,121,1)"],["0.708333333333333","rgba(79,191,110,1)"],["0.75","rgba(98,199,98,1)"],["0.791666666666667","rgba(119,207,85,1)"],["0.833333333333333","rgba(147,214,70,1)"],["0.875","rgba(172,220,52,1)"],["0.916666666666667","rgba(199,225,42,1)"],["0.958333333333333","rgba(226,228,40,1)"],["1","rgba(253,231,37,1)"]],"showscale":false,"color":[13.199999999999999,10,8.0999999999999996,8.8000000000000007,9,7.9000000000000004,3.2999999999999998,5.9000000000000004,15.4,17.399999999999999,5.2999999999999998,2.6000000000000001,10.4,7.2000000000000002,2.2000000000000002,6,9.6999999999999993,15.4,2.1000000000000001,11.300000000000001,4.4000000000000004,12.1,2.7000000000000002,16.100000000000001,9,6,4.2999999999999998,12.199999999999999,2.1000000000000001,7.4000000000000004,11.4,11.1,13,0.80000000000000004,7.2999999999999998,6.5999999999999996,4.9000000000000004,6.2999999999999998,3.3999999999999999,14.4,3.7999999999999998,13.199999999999999,12.699999999999999,3.2000000000000002,2.2000000000000002,8.5,4,5.7000000000000002,2.6000000000000001,6.7999999999999998]}},"type":"scatter","xaxis":"x","yaxis":"y","frame":null},{"x":[32,91],"y":[45,337],"type":"scatter","mode":"markers","opacity":0,"hoverinfo":"none","showlegend":false,"marker":{"colorbar":{"title":"Murder","ticklen":2},"cmin":0.80000000000000004,"cmax":17.399999999999999,"colorscale":[["0","rgba(68,1,84,1)"],["0.0416666666666667","rgba(70,19,97,1)"],["0.0833333333333333","rgba(72,32,111,1)"],["0.125","rgba(71,45,122,1)"],["0.166666666666667","rgba(68,58,128,1)"],["0.208333333333333","rgba(64,70,135,1)"],["0.25","rgba(60,82,138,1)"],["0.291666666666667","rgba(56,93,140,1)"],["0.333333333333333","rgba(49,104,142,1)"],["0.375","rgba(46,114,142,1)"],["0.416666666666667","rgba(42,123,142,1)"],["0.458333333333333","rgba(38,133,141,1)"],["0.5","rgba(37,144,140,1)"],["0.541666666666667","rgba(33,154,138,1)"],["0.583333333333333","rgba(39,164,133,1)"],["0.625","rgba(47,174,127,1)"],["0.666666666666667","rgba(53,183,121,1)"],["0.708333333333333","rgba(79,191,110,1)"],["0.75","rgba(98,199,98,1)"],["0.791666666666667","rgba(119,207,85,1)"],["0.833333333333333","rgba(147,214,70,1)"],["0.875","rgba(172,220,52,1)"],["0.916666666666667","rgba(199,225,42,1)"],["0.958333333333333","rgba(226,228,40,1)"],["1","rgba(253,231,37,1)"]],"showscale":true,"color":[0.80000000000000004,17.399999999999999],"line":{"color":"rgba(255,127,14,1)"}},"xaxis":"x","yaxis":"y","frame":null}],"highlight":{"on":"plotly_click","persistent":false,"dynamic":false,"selectize":false,"opacityDim":0.20000000000000001,"selected":{"opacity":1},"debounce":0},"shinyEvents":["plotly_hover","plotly_click","plotly_selected","plotly_relayout","plotly_brushed","plotly_brushing","plotly_clickannotation","plotly_doubleclick","plotly_deselect","plotly_afterplot","plotly_sunburstclick"],"base_url":"https://plot.ly"},"evals":[],"jsHooks":[]}</script>
```



## Custom Figures

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


# Reporting
***

## R and R-Markdown

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


## Simple Reports

We will create reproducible reports via R Markdown.

**Example 1: Data Scientism**.
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

**Example 2: Homework Assignment**.
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
<div class="plotly html-widget html-fill-item" id="htmlwidget-d52e8a77a43c034cdbda" style="width:672px;height:480px;"></div>
<script type="application/json" data-for="htmlwidget-d52e8a77a43c034cdbda">{"x":{"visdat":{"29e75faf661c":["function () ","plotlyVisDat"]},"cur_data":"29e75faf661c","attrs":{"29e75faf661c":{"x":{},"y":{},"alpha_stroke":1,"sizes":[10,100],"spans":[1,20]}},"layout":{"margin":{"b":40,"l":60,"t":25,"r":10},"xaxis":{"domain":[0,1],"automargin":true,"title":"X"},"yaxis":{"domain":[0,1],"automargin":true,"title":"Y"},"hovermode":"closest","showlegend":false},"source":"A","config":{"modeBarButtonsToAdd":["hoverclosest","hovercompare"],"showSendToCloud":false},"data":[{"x":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100],"y":[4.5991821626822631,9.5042795582700741,8.9425752406243539,11.881634581402238,17.004529766069965,24.794681191293563,24.536515878885485,32.705969393290893,35.136343005339398,33.825303127399572,41.91456585270943,46.729375438694113,52.743940506045192,56.248919531464374,57.901935279610314,63.471371277200781,69.119711112746486,75.323050616621984,75.764291626729033,76.387118235049044,83.996748708154698,87.912663506307396,91.123680664794747,98.086772261131699,100.93055416898154,105.02356330786922,106.9049477908744,114.63877593721193,116.33151789441902,117.39891466716018,123.96918943962019,129.57057182206304,132.21399593513812,132.5820957144183,146.57800176052532,143.10677557952417,147.45597012416951,154.07357210020444,154.6115680214466,159.30654939339263,164.98275562858439,165.06321210231235,174.59285941567703,176.30774617882514,179.53465905631069,180.34484661264048,188.34483106715038,190.96766421386155,194.740253977631,197.47203917281362,201.18275559296285,209.60182681812284,209.91292968911611,211.01318993954621,222.49759103067981,225.51133460729713,229.54111888845435,235.06288652922223,234.07035975269486,240.62957942619408,243.16250031608701,248.70603141682767,255.5471559124301,255.78327279468812,259.5399959743263,263.924870535558,266.94691336808756,272.40663544424461,274.49258837995507,278.63582174871442,282.76154291428907,283.81690883103647,293.03708390061723,295.39924620848456,299.10216439789093,305.00960239163999,307.676916392875,315.19234121781545,314.80035199502447,319.11082749574751,321.92967629170573,329.52707354557657,331.32214963924713,336.90440146927909,337.50151012266252,344.61806126626993,348.14656561871061,354.38283280053867,352.66860128089081,359.80641627939991,361.74714546203091,367.67216297663907,373.61915403545902,376.34799825752037,380.12552807774199,381.01531666708888,387.12250999523468,387.53225274232005,394.40909076189206,401.82391229530828],"type":"scatter","mode":"markers","marker":{"color":"rgba(31,119,180,1)","line":{"color":"rgba(31,119,180,1)"}},"error_y":{"color":"rgba(31,119,180,1)"},"error_x":{"color":"rgba(31,119,180,1)"},"line":{"color":"rgba(31,119,180,1)"},"xaxis":"x","yaxis":"y","frame":null}],"highlight":{"on":"plotly_click","persistent":false,"dynamic":false,"selectize":false,"opacityDim":0.20000000000000001,"selected":{"opacity":1},"debounce":0},"shinyEvents":["plotly_hover","plotly_click","plotly_selected","plotly_relayout","plotly_brushed","plotly_brushing","plotly_clickannotation","plotly_doubleclick","plotly_deselect","plotly_afterplot","plotly_sunburstclick"],"base_url":"https://plot.ly"},"evals":[],"jsHooks":[]}</script>
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



## Posters and Slides

Posters and presentations are another important type of scientific document. R markdown is good at creating both of these, and actually *very* good with some additional packages. So we will also use [flexdashboard](https://pkgs.rstudio.com/flexdashboard/) for posters and [beamer]( https://bookdown.org/yihui/rmarkdown/beamer-presentation.html) for presentations. 

**Poster**.

See [DataScientism_Poster.html](https://jadamso.github.io/Rbooks/Templates/DataScientism_Poster.html) and recreate from the source file [DataScientism_Poster.Rmd](https://jadamso.github.io/Rbooks/Templates/DataScientism_Poster.Rmd). Simply change the name to your own, and knit the document.

**Slides**.

See [DataScientism_Slides.pdf](https://jadamso.github.io/Rbooks/Templates/DataScientism_Slides.pdf)

Since beamer is a pdf output, you will need to install [Latex](https://tug.org/texlive/). Alternatively, you can install a lightweight version [TinyTex](https://yihui.org/tinytex/) from within R

``` r
install.packages('tinytex')
tinytex::install_tinytex()  # install TinyTeX
```

Then download source file [DataScientism_Slides.Rmd](https://jadamso.github.io/Rbooks/Templates/DataScientism_Slides.Rmd), change the name to your own, and knit the document.

If you cannot install *Latex*, then you must specify a different output. For example, change `output: beamer_presentation` to `output: ioslides_presentation` on line 6 of the source file.


## More Literature

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

Some other good packages for posters/presenting you should be aware of

* https://github.com/mathematicalcoffee/beamerposter-rmarkdown-example
* https://github.com/rstudio/pagedown
* https://github.com/brentthorne/posterdown
* https://odeleongt.github.io/postr/
* https://wytham.rbind.io/post/making-a-poster-in-r/
* https://www.animateyour.science/post/How-to-design-an-award-winning-conference-poster


