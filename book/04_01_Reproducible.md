# (PART) Reproducible Research in R {-} 


# Large Projects
***

As you scale up a project, then you will have to be more organized. 

## Scripting

#### **Basics**. {-}
Save the following code as `MyFirstScript.R`

``` r
# Define New Function
sum_squared <- function(x1, x2) {
    y <- (x1 + x2)^2
    return(y)
} 

# Test New Function
x <- c(0,1,3,10,6)
sum_squared(x[1], x[3])
sum_squared(x, x[2])
sum_squared(x, x[7])
sum_squared(x, x)

message('Script Completed')
```

*Restart Rstudio*.^[Alternatively, *clean the workspace* by 1: clearing the environment and history (use the broom in top right panel). 2: clearing unsaved plots (use the broom in bottom right panel).]

*Replicate* in another tab via

``` r
source('MyFirstScript.R')
```
Note that you may first need to `setwd()` so your computer knows where you saved your code.^[You can also use *GUI: point-click* click 'Source > Source as a local job' on top right]


After you get this working:

* add a the line `print(sum_squared(y, y))` to the bottom of `MyFirstCode.R`. 
* apply the function to a vectors specified outside of that script
* record the session information


``` r
# Pass Objects/Functions *to* Script
y <- c(3,1,NA)
source('MyFirstScript.R')

# Pass Objects/Functions *from* Script
z <- sqrt(y)/2
sum_squared(z,z)

# Report all information relevant for replication
sessionInfo()
```

Note that you can open a new terminal in RStudio in the top bar by
clicking 'tools > terminal > new terminal'



#### **Logging/Sinking**. {-}

When executing the makefile, you can also log the output in three different ways: 

1. Inserting some code into the makefile that "sinks" the output 

``` r
# Project Structure
home_dir    <- path.expand("~/Desktop/Project/")
data_dir_r  <- paste0(data_dir, "Data/Raw/")
data_dir_c  <- paste0(data_dir, "Data/Clean/")
out_dir     <- paste0(hdir, "Output/")
code_dir    <- paste0(hdir, "Code/")

# Log Output
set.wd( code_dir )
sink("MAKEFILE.Rout", append=TRUE, split=TRUE)

# Execute Codes
source( "RBLOCK_001_DataClean.R" )
source( "RBLOCK_002_Figures.R" )
source( "RBLOCK_003_ModelsTests.R" )
source( "RBLOCK_004_Robust.R" )
sessionInfo()

# Stop Logging Output
sink()
```

2. Starting a session that "sinks" the makefile

``` r
sink("MAKEFILE.Rout", append=TRUE, split=TRUE)
source("MAKEFILE.R")
sink()
```

3. Execute the makefile via the commandline 

``` bash
R CMD BATCH MAKEFILE.R MAKEFILE.Rout
```


## Organizing

#### **Project Structure**. {-}
Large sized projects should have their own `Project` folder on your computer with files, subdirectories with files, and subsubdirectories with files. It should look like this
```
Project
    └── README.txt
    └── /Code
        └── MAKEFILE.R
        └── RBLOCK_001_DataClean.R
        └── RBLOCK_002_Figures.R
        └── RBLOCK_003_ModelsTests.R
        └── RBLOCK_004_Robust.R
        └── /Logs
            └── MAKEFILE.Rout
    └── /Data
        └── /Raw
            └── Source1.csv
            └── Source2.shp
            └── Source3.txt
        └── /Clean
            └── AllDatasets.Rdata
            └── MainDataset1.Rds
            └── MainDataset2.csv
    └── /Output
        └── MainFigure.pdf
        └── AppendixFigure.pdf
        └── MainTable.tex
        └── AppendixTable.tex
    └── /Writing
        └── /TermPaper
            └── TermPaper.tex
            └── TermPaper.bib
            └── TermPaper.pdf
        └── /Slides
            └── Slides.Rmd
            └── Slides.html
            └── Slides.pdf
        └── /Poster
            └── Poster.Rmd
            └── Poster.html
            └── Poster.pdf
        └── /Proposal
            └── Proposal.Rmd
            └── Proposal.html
            └── Proposal.pdf
```

There are two main meta-files

* `README.txt` overviews the project structure and what the codes are doing
* `MAKEFILE` explicitly describes and executes all codes (and typically logs the output).

**Class Projects**. Zip your project into a single file that is easy for *others* to identify: `Class_Project_LASTNAME_FIRSTNAME.zip`

#### **MAKEFILE**. {-}
If all code is written with the same program (such as R) the makefile can be written in a single language. For us, this looks like

``` r
# Project Structure
home_dir    <- path.expand("~/Desktop/Project/")
data_dir_r  <- paste0(data_dir, "Data/Raw/")
data_dir_c  <- paste0(data_dir, "Data/Clean/")
out_dir     <- paste0(hdir, "Output/")
code_dir    <- paste0(hdir, "Code/")

# Execute Codes
# libraries are loaded within each RBLOCK
setwd( code_dir )
source( "RBLOCK_001_DataClean.R" )
source( "RBLOCK_002_Figures.R" )
source( "RBLOCK_003_ModelsTests.R" )
source( "RBLOCK_004_Robust.R" )

# Report all information relevant for replication
sessionInfo()
```

Notice there is a lot of documentation `# like this`, which is crucial for large projects. Also notice that anyone should be able to replicate the entire project by downloading a zip file and simply changing `home_dir`.

If some folders or files need to be created, you can do this within R

``` r
# list the files and directories
list.files(recursive=TRUE, include.dirs=TRUE)
# create directory called 'Data'
dir.create('Data')
```



#### **Names**. {-}

Your file names do not matter technically, but they should be informative.

The variable names in your scripts also do not matter technically, but they should be informative
```{r}
one <- 1 # good variable name
one

one <- 43 # bad variable name
one
```

Good names avoid confusion later
```{r}
x <- 43
x_plus_two <- x + 2 # better
x_plus_two
```


## Posters and Slides

Posters and presentations are another important type of scientific document. R markdown is good at creating both of these, and actually *very* good with some additional packages. So we will also use [flexdashboard](https://pkgs.rstudio.com/flexdashboard/) for posters and [beamer]( https://bookdown.org/yihui/rmarkdown/beamer-presentation.html) for presentations. 

**Poster**. 
See [DataScientism_Poster.html](https://jadamso.github.io/Rbooks/Templates/DataScientism_Poster.html) and recreate from the source file [DataScientism_Poster.Rmd](https://jadamso.github.io/Rbooks/Templates/DataScientism_Poster.Rmd). Simply change the name to your own, and knit the document.

**Slides**.
See [DataScientism_Slides.pdf](https://jadamso.github.io/Rbooks/Templates/DataScientism_Slides.pdf) and recreate from the source file [DataScientism_Slides.Rmd](https://jadamso.github.io/Rbooks/Templates/DataScientism_Slides.Rmd).


Since beamer is a pdf output, you will need to install [Latex](https://tug.org/texlive/). Alternatively, you can install a lightweight version [TinyTex](https://yihui.org/tinytex/) from within R

``` r
install.packages('tinytex')
tinytex::install_tinytex()  # install TinyTeX
```

If you cannot install *Latex*, then you must specify a different output. For example, change `output: beamer_presentation` to `output: ioslides_presentation` on line 6 of the source file.

## Applications

[Shiny](https://shiny.posit.co/) is an R package to build web applications.

Shiny Flexdashboards are nicely formatted Shiny Apps. While it is possible to use Shiny without the Flexdashboard formatting, I think it is easier to remember

* `.R` files are codes for statistical analysis
* `.Rmd` files are for communicating: reports, slides, posters, and apps


**Example: Histogram**.
Download the source file [TrialApp1_Histogram_Dashboard.Rmd](https://jadamso.github.io/Rbooks/Templates/TrialApp1_Histogram_Dashboard.Rmd)
and open it with `rstudio`. Then run it with 

``` r
rmarkdown::run('TrialApp1_Histogram_Dashboard.Rmd')
```

* Within the app, experiment with how larger sample sizes change the distribution. 

* Edit the app to let the user specify the number of breaks in the histogram. 

If you are having difficulty, you can try working first with the barebones shiny code. To do this, download [TrialApp0_Histogram.Rmd](https://jadamso.github.io/Rbooks/Templates/TrialApp0_Histogram.Rmd) and edit it in Rstudio. You can run the code with `rmarkdown::run('TrialApp0_Histogram.Rmd')`.


## Further Reading

Your code should be readable and error free. For code writing guides, see

* https://google.github.io/styleguide/Rguide.html
* https://style.tidyverse.org/
* https://dept.stat.lsa.umich.edu/~jerrick/courses/stat701/notes/codestyle.html
* http://adv-r.had.co.nz/Style.html
* https://www.burns-stat.com/pages/Tutor/R_inferno.pdf

For organization guidelines, see

* https://guides.lib.berkeley.edu/c.php?g=652220&p=4575532
* https://kbroman.org/steps2rr/pages/organize.html
* https://drivendata.github.io/cookiecutter-data-science/
* https://ecorepsci.github.io/reproducible-science/project-organization.html

For additional logging capabilities, see https://cran.r-project.org/web/packages/logr/

For very large projects, there are many more tools available at https://cran.r-project.org/web/views/ReproducibleResearch.html

For larger scale projects, use scripts 

* https://kbroman.org/steps2rr/pages/scripts.html
* https://kbroman.org/steps2rr/pages/automate.html


Some other good packages for posters/presenting you should be aware of

* https://github.com/mathematicalcoffee/beamerposter-rmarkdown-example
* https://github.com/rstudio/pagedown
* https://github.com/brentthorne/posterdown
* https://odeleongt.github.io/postr/
* https://wytham.rbind.io/post/making-a-poster-in-r/
* https://www.animateyour.science/post/How-to-design-an-award-winning-conference-poster

Overview of Applications

* https://bookdown.org/yihui/rmarkdown/shiny-documents.html
* https://shiny.rstudio.com/tutorial/
* https://shiny.rstudio.com/articles/
* https://shiny.rstudio.com/gallery/
* https://rstudio.github.io/leaflet/shiny.html
* https://mastering-shiny.org/

More Help with Shiny Apps

* https://shiny.rstudio.com/tutorial/written-tutorial/lesson1/
* https://mastering-shiny.org/basic-app.html
* https://towardsdatascience.com/beginners-guide-to-creating-an-r-shiny-app-1664387d95b3
* https://shiny.rstudio.com/articles/interactive-docs.html
* https://bookdown.org/yihui/rmarkdown/shiny-documents.html
* https://shiny.rstudio.com/gallery/plot-interaction-basic.html
* https://www.brodrigues.co/blog/2021-03-02-no_shiny_dashboard/
* https://bookdown.org/yihui/rmarkdown/shiny.html
* https://shinyserv.es/shiny/
* https://bookdown.org/egarpor/NP-UC3M/kre-i-kre.html#fig:kreg
* https://engineering-shiny.org/



# Performance 
***

## Functions 
There are many possible functions you can make and use. You will want to test them, debug them, and optimize them in large projects.
```{r}
sum_squared <- function(x1, x2) {
    y <- (x1 + x2)^2
    return(y)
}

sum_squared(1, 3)
sum_squared(x, 2)
sum_squared(x, NA) 
sum_squared(x, x)
sum_squared(x, 2*x)

fun_of_seq <- function(f, constant=2){
    x1 <- seq(1,3, length.out=12)
    x2 <- x1+constant
    x <- cbind(x1,x2)
    y <- f(x)
    return(y)
}
fun_of_seq(sum)
fun_of_seq(sum, 3)
fun_of_seq(prod)
fun_of_seq(prod, 3)
```

A more complicated example
```{r}
complicated_fun <- function(i, j=0){
    x <- i^(i-1)
    y <- x + mean( seq(j,i) )
    z <- log(y)/i
    return(z)
}
complicated_vector <- vector(length=10)
for(i in seq(1,10) ){
    complicated_vector[i] <- complicated_fun(i)
}
```

```{r}
# for loop in a function
r_fun <- function(n){
    x <- rep(1,n)
    for(i in seq(2,length(x)) ){
        x[i] <- (x[i-1]+1)^2
    }
    return(x)
}
r_fun(5)
```


```{r, eval=F, echo=F}
# mapply takes multiple vectors
# x <- seq(1,3)
# mapply(sum, x, exp(x) )
```

## Debugging 

In R, you use multiple functions on different types of data objects. Moreover, you "typically solve complex problems by decomposing them into simple functions, not simple objects." (H. Wickham)


Problems print to the console

``` r
warning("This is what a warning looks like")
stop("This is what an error looks like")
## Error: This is what an error looks like
```

Nonproblems also print to the console

``` r
message("This is what a message looks like")
cat('cat\n')
## cat
print('print')
## [1] "print"
```

#### **Tracing**. {-}

Consider this example of an error process (originally taken from https://adv-r.hadley.nz/ ).

``` r
# Let i() check if its argument is numeric
i <- function(i0) {
  if ( !is.numeric(i0) ) {
    stop("`d` must be numeric", call.=FALSE)
  }
  i0 + 10
}

# Let f() call g() call h() call i()
h <- function(i0) i(i0)
g <- function(h0) h(h0)
f <- function(g0) g(g0)

# Observe Error
f("a")
## Error: `d` must be numeric
```

First try simple print debugging

``` r
f2 <- function(g0) {
  cat("f2 calls g2()\n")
  g2(g0)
}
g2 <- function(h0) {
  cat("g2 calls h2() \n")
  cat("b =", h0, "\n")
  h2(h0)
}
h2 <- function(i0) {
  cat("h2 call i() \n")
  i(i0)
}

f2("a")
## f2 calls g2()
## g2 calls h2() 
## b = a 
## h2 call i()
## Error: `d` must be numeric
```

If that fails, try traceback debugging

``` r
traceback()
## No traceback available
```

And if that fails, try an Interactive approach

``` r
g3 <- function(h0) {
  browser()
  h(h0)
}
f3 <- function(g0){
  g3(g0)
}
f3("a")
## Called from: g3(g0)
## debug: h(h0)
## Error: `d` must be numeric
```

#### **Isolating**. {-}

To inspect objects

``` r
is.object(f)
is.object(c(1,1))

class(f)
class(c(1,1))

# Storage Mode Type 
typeof(f)
typeof(c(1,1))

storage.mode(f)
storage.mode(c(1,1))
```

To check for valid inputs/outputs

``` r
x <- c(NA, NULL, NaN, Inf, 0)

cat("Vector to inspect: ")
x

cat("NA: ")
is.na(x)

cat("NULL: ")
is.null(x)

cat("NaN: ")
is.nan(x)

cat("Finite: ")
is.finite(x)

cat("Infinite: ")
is.infinite(x)
# Many others
```

To check for values

``` r
all( x > -2 )
any( x > -2 )
# Check Matrix Rows
rowAny <- function(x) rowSums(x) > 0
rowAll <- function(x) rowSums(x) == ncol(x)
```

#### **Handling**. {-}

Simplest example

``` r
x <- 'A'
tryCatch(
  expr = log(x),
  error = function(e) {
        message('Caught an error but did not break')
        print(e)
        return(NA)
})
```

Another example

``` r
x <- -2
tryCatch(
  expr = log(x),
  error = function(e) {
        message('Caught an error but did not break')
        print(e)
        return(NA)
    },
    warning = function(w){
        message('Caught a warning!')
        print(w)
        return(NA)        
    },
    finally = {
        message("Returned log(x) if successfull or NA if Error or Warning")
    }
)
## <simpleWarning in log(x): NaNs produced>
## [1] NA
```

<!--# Ignore warnings/messages
    Supressing errors is possible but a bad idea
    
    ``` r
    try(1+2, silent=T)
    ## [1] 3
    try(warning('warning'), silent=T)
    try(error('error'), silent=T)
    
    try(1+2, silent=F)
    ## [1] 3
    try(warning('warning'), silent=F)
    try(error('error'), silent=F)
    ## Error in error("error") : could not find function "error"
    
    #suppressMessages()    
    ```
-->

Safe Functions

``` r
# Define
log_safe <- function(x){
    lnx <- tryCatch(
        expr = log(x),
        error = function(e){
            cat('Error Caught: \n\t')        
            print(e)
            return(NA)            
        },
        warning = function(w){
            cat('Warning Caught: \n\t')
            print(w)
            return(NA)            
        })
    return(lnx)
}

# Test 
log_safe( 1)
## [1] 0
log_safe(-1)
## Warning Caught: 
## 	<simpleWarning in log(x): NaNs produced>
## [1] NA
log_safe(' ')
## Error Caught: 
## 	<simpleError in log(x): non-numeric argument to mathematical function>
## [1] NA


# Further Tests
s <- sapply(list("A",Inf, -Inf, NA, NaN, 0, -1, 1), log_safe)
## Error Caught: 
## 	<simpleError in log(x): non-numeric argument to mathematical function>
## Warning Caught: 
## 	<simpleWarning in log(x): NaNs produced>
## Warning Caught: 
## 	<simpleWarning in log(x): NaNs produced>

s
## [1]   NA  Inf   NA   NA  NaN -Inf   NA    0
```



## Optimizing 

In General, clean code is faster and less error prone. 

By optimizing repetitive tasks, you end up with code that

* is cleaner, faster, and more general
* can be easily parallelized

So, after identifying a bottleneck, try 

1. **vectorize your code**
2. use a dedicated package 
3. use parallel computations
4. compile your code in C++


But remember

* Don't waste time optimizing code that is not holding you back.
* Look at what has already done.

#### **Benchmarking**. {-}

For identifying bottlenecks, the simplest approach is to time how long a code-chunk runs

``` r
system.time({
    x0 <- runif(1e5)
    x1 <- sqrt(x0)
    x2 <- paste0('J-', x1)
})
##    user  system elapsed 
##   0.130   0.004   0.134
```

You can *visually* identify bottlenecks in larger blocks

``` r
# Generate Large Random Dataset
n <- 2e6
x <- runif(n)
y <- runif(n)
z <- runif(n)
XYZ <- cbind(x,y,z)

# Inspect 4 equivalent `row mean` calculations 
profvis::profvis({
    m <- rowSums(XYZ)/ncol(XYZ)
    m <- rowMeans(XYZ)
    m <- apply(XYZ, 1, mean)
    m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }
})
```



``` r
# rowSums(), colSums(), rowMeans(), and colMeans() are vectorised and fast.
# for loop is not the slowest, but the ugliest.
```


For systematic speed comparisons, try a benchmarking package

``` r
# 3 Equivalent calculations of the mean of a vector
mean1 <- function(x,p=1) mean(x^p)
mean2 <- function(x,p=1) sum(x^p) / length(x)
mean3 <- function(x,p=1) mean.default(x^p)

# Time them
x <- runif(1e6)
microbenchmark::microbenchmark(
  mean1(x,.5),
  mean2(x,.5),
  mean3(x,.5),
  times=20
)
## Unit: milliseconds
##           expr      min       lq     mean   median       uq      max neval cld
##  mean1(x, 0.5) 19.99996 21.08001 21.74110 22.06529 22.31428 23.07532    20   a
##  mean2(x, 0.5) 19.15722 20.10658 20.91981 21.12252 21.73134 22.79755    20   a
##  mean3(x, 0.5) 19.94863 20.39546 22.13567 22.02917 22.52014 32.40659    20   a

# Time them (w/ memory)
bench::mark(
  mean1(x,.5),
  mean2(x,.5),
  mean3(x,.5),
  iterations=20
)
## # A tibble: 3 × 6
##   expression         min   median `itr/sec` mem_alloc `gc/sec`
##   <bch:expr>    <bch:tm> <bch:tm>     <dbl> <bch:byt>    <dbl>
## 1 mean1(x, 0.5)   19.9ms   22.6ms      45.9    7.63MB     0   
## 2 mean2(x, 0.5)   19.1ms   21.6ms      48.3    7.63MB     2.54
## 3 mean3(x, 0.5)   19.8ms   22.6ms      45.3    7.63MB     2.39
```

#### **Vectorize**. {-}

Computers are really good at math, so exploit this.

* First try vectors
* Then try `apply` functions
* See https://uscbiostats.github.io/software-dev-site/handbook-slow-patterns.html


Vector operations are generally faster and easier to read than loops

``` r
# Compare 2 moving averages
x <- runif(2e6)

# First Try
ma1 <- function(y){
    z <- y*NA
    for(i in 2:length(y)){
        z[i] <- (y[i]-y[i-1])/2
    }
    return(z)
}

# Optimized using diff
diff( c(2,2,10,9) )
## [1]  0  8 -1

ma2 <- function(y){
    z2 <- diff(y)/2
    z2 <- c(NA, z2) 
    return(z2)
}

all.equal(ma1(x),ma2(x))
## [1] TRUE

system.time( ma1(x) )
##    user  system elapsed 
##   0.173   0.000   0.174
system.time( ma2(x) )
##    user  system elapsed 
##   0.031   0.006   0.037

ma3 <- compiler::cmpfun(ma2)
system.time( ma3(x) )
##    user  system elapsed 
##   0.028   0.000   0.028
```
Likewise, matrix operations are often faster than vector operations.


#### **Pre-allocate**. {-}

1. Put as few things in a loop as possible. (If there is a bottleneck, try to take stuff out of a loop.)
2. create objects first and then fill them. (Do not grow lists or vectors dynammically)

more complicated example

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
for(i in 2:length(x)){
    x[i] <- (x[i-1]+1)^2
}
x
## [1]   1   4  25 676
```

#### **Memory Usage**. {-}

For finding problematic blocks `utils::Rprof(memory.profiling = TRUE)` logs total memory usage of R at regular time intervals. E.g.

``` r
Rprof( interval = 0.005)
    # Create Data
    x <- runif(2e6)
    y <- sqrt(x)
    # Loop Format Data
    z <- y*NA
    for(i in 2:length(y)){ z[i] <- (y[i]-y[i-1])/2 }
    # Regression
    X <- cbind(1,x)[-1,]
    Z <- z[-1]
    reg_fast <- .lm.fit(X, Z)
Rprof(NULL)
summaryRprof()
```

For finding problematic functions: `utils::Rprofmem()` logs memory usage at each call

For finding problematic scripts, see "Advanced Optimization". (With Rprof, you can identifying bottlenecks on a cluster without a GUI.)

#### **Packages**. {-}

Before creating your own program, check if there is a faster or more memory efficient version. E.g., [data.table](https://cran.r-project.org/web/packages/data.table/vignettes/datatable-intro.html) or [Rfast2](https://cran.r-project.org/web/packages/Rfast2/index.html) for basic data manipulation.

Some functions are simply wrappers for the function you want, and calling it directly can speed things up. 

``` r
X <- cbind(1, runif(1e6))
Y <- X %*% c(1,2) + rnorm(1e6)
DAT <- as.data.frame(cbind(Y,X))

system.time({ lm(Y~X, data=DAT) })
##    user  system elapsed 
##   0.324   0.007   0.134
system.time({ .lm.fit(X, Y) })
##    user  system elapsed 
##   0.093   0.000   0.026
system.time({ solve(t(X)%*%X) %*% (t(X)%*%Y) })
##    user  system elapsed 
##   0.029   0.000   0.024
```
Note that such functions to have fewer checks and return less information, so you must know exactly what you are putting in and getting out.


**Task Views**

Task views list relevant packages. For all students and early researchers, see 

* https://cran.r-project.org/web/views/ReproducibleResearch.html

For microeconometrics, see

* https://cran.r-project.org/web/views/Econometrics.html

For spatial econometrics , see

* https://cran.r-project.org/web/views/Spatial.html
* https://cran.r-project.org/web/views/SpatioTemporal.html

Multiple packages may have the same function name for different commands. In this case use the syntax ``package::function`` to specify the package. For example

``` r
devtools::install_github
remotes::install_github
```


*Don't fret* Sometimes there is not a specific package for your data. Odds are, you can do most of what you want with base code.

* Packages just wrap base code in convient formats
* see https://cran.r-project.org/web/views/ for topical overviews

Statisticians might have different naming conventions

* if the usual software just spits out a nice plot
you might have to dig a little to know precisely what you want
* your data are fundamentally numbers, strings, etc...
You only have to figure out how to read it in.



## Advanced Optimizing

If you still are stuck with slow code, you can

* make your code run on parallel processors
* try [Amazon Web Server](https://aws.amazon.com/ec2/) for more brute-power 
* rewrite bottlenecks with a working C++ compiler or Fortran compiler.

In what follows, note that there are alternative ways to run R via the command line. For example,

``` bash
# Method 1
R -e "source('MyFirstScript.R')"
# Method 2
R CMD BATCH MyFirstScript.R
```

Also, look into <https://cran.r-project.org/web/views/HighPerformanceComputing.html>

#### **Parallel**. {-}

Sometimes there will still be a problematic bottleneck. 

Your next step should be parallelism:

* Write the function as a general vectorized function.
* Apply the same function to every element in a list *at the same time*


``` r
# lapply in parallel on {m}ultiple {c}ores
x <- c(10,20,30,40,50)
f <- function(element) { element^element }
parallel::mclapply( x, mc.cores=2, FUN=f)
## [[1]]
## [1] 1e+10
## 
## [[2]]
## [1] 1.048576e+26
## 
## [[3]]
## [1] 2.058911e+44
## 
## [[4]]
## [1] 1.208926e+64
## 
## [[5]]
## [1] 8.881784e+84
```

More power is often not the solution


``` r
# vectorize and compile
e_power_e_fun <- compiler::cmpfun( function(vector){ vector^vector} )

# base R
x <- 0:1E6
s_vc <- system.time( e_power_e_vec <- e_power_e_fun(x) )
s_vc
##    user  system elapsed 
##   0.020   0.002   0.022

# brute power
x <- 0:1E6
s_bp <- system.time({
  e_power_e_mc <- unlist( parallel::mclapply(x, mc.cores=2, FUN=e_power_e_fun))
})
s_bp
##    user  system elapsed 
##   1.101   0.247   0.738

# Same results
all(e_power_e_vec==e_power_e_mc)
## [1] TRUE
```

Note that parallelism does not go well with a GUI.

#### **Computer Clusters**. {-}

For parallel computations on a computer cluster, you will need to use both R and the linux command line.


``` bash
R --slave -e '1:10'

R --slave -e '
    1:10
    seq(0,1,by=.2)
    paste(c("A","D"), 1:2)
'
##  [1]  1  2  3  4  5  6  7  8  9 10
##  [1]  1  2  3  4  5  6  7  8  9 10
## [1] 0.0 0.2 0.4 0.6 0.8 1.0
## [1] "A 1" "D 2"
```


``` bash
R --slave -e '
    .libPaths("~/R-Libs")    
    options(repos="https://cloud.r-project.org/")
    
    update.packages(ask=F)
    
    suppressPackageStartupMessages(library(stargazer))
'    
```

You will often want to rerun entire scripts with a different parameter. To do so, you need to edit your R scripts to accept parameters from the command line 


``` r
args <- commandArgs(TRUE)
```

For example

``` bash
R --slave -e '
    args <- commandArgs(TRUE)
    paste0(1, args)
' --args a b c

R --slave -e '
    args <- commandArgs(TRUE)
    my_numbers <- as.numeric(args)
    my_numbers + 1
' --args $(seq 1 10)
## [1] "1a" "1b" "1c"
##  [1]  2  3  4  5  6  7  8  9 10 11
```

You can also store the output and computer resources of a script. For example, save the last script as `RBLOCK.R` in the folder `$HOME/R_Code` and run the following


``` bash
# Which Code
RDIR=$HOME/R_Code #main directory
infile=$RDIR/RBLOCK.R #specific code
outfile=$RDIR/R_Logs/RBLOCK$design_N.Rout #log R output
memfile=$RDIR/R_Logs/RBLOCK$design_N.Rtime #log computer resources

# Execute the Script and store resource useage via `time`
command time -o $memfile -v \
    R CMD BATCH --no-save --quiet --no-restore "--args 1 2 3" $infile $outfile 
```
Note that you need to have https://ftp.gnu.org/gnu/time installed


On an academic computing cluster, you may have to use a scheduler like *slurm*. In which case you can submit  a bash script

``` bash
sbatch  --mem 10GB --time=0-01:00:00 -a 50 SlurmJob.sh
```
where ` SlurmJob.sh` looks like

``` bash
#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --error=$HOME/R_Code/Slurm_Logs/%x.error-%j
#SBATCH --output=$HOME/R_Code/Slurm_Logs/%x.out-%j

# Which Code
RDIR=$HOME/R_Code
infile=$RDIR/RBLOCK.R
outfile=$RDIR/R_Logs/RBLOCK$design_N.Rout
memfile=$RDIR/R_Logs/RBLOCK$design_N.Rtime

# Which Parameter
a="${SLURM_ARRAY_TASK_ID}"

# Execute the Script with a specific parameter, and store memory/time useage
command time -o $memfile -v \
    R CMD BATCH --no-save --quiet --no-restore "--args $a" $infile $outfile 

# Summarize memory/time useage
echo "design_N: $design_N Gridpoints"
cat $memfile | awk '/User time/ {printf "Time: %.2f Hours\n", $4/3600}'
cat $memfile | awk '/Maximum resident set size/ {printf "Memory: %.2f GB\n", $6/1048576}'
echo "Partition: $SLURM_JOB_PARTITION"
```

#### **Compiled Code**. {-}

You can use C++ code within R to speed up a specific chunk.

To get C++ on your computer

* On Windows, install Rtools.
* On Mac, install Xcode from the app store.
* On Linux, sudo apt-get install r-base-dev or similar.

To call C++ from R use package `Rcpp`

``` r
Rcpp::cppFunction('
  int add(int x, int y, int z) {
    int sum = x + y + z;
    return sum;
  }'
)
add(1, 2, 3)
## [1] 6
```

For help getting started with Rcpp, see https://cran.r-project.org/web/packages/Rcpp/vignettes/Rcpp-quickref.pdf


First try to use C++ (or Fortran) code that others have written

``` r
.C
.Fortran
```
For a tutorial, see https://masuday.github.io/fortran_tutorial/r.html


## Further Reading

Advanced Programming 

* https://rmd4sci.njtierney.com/
* https://smac-group.github.io/ds/high-performance-computing.html
* https://www.stat.umn.edu/geyer/3701/notes/arithmetic.Rmd

For debugging tips

* https://cran.r-project.org/doc/manuals/R-lang.html#Debugging
* https://cran.r-project.org/doc/manuals/R-exts.html#Debugging
* https://adv-r.hadley.nz/debugging.html
* https://adv-r.hadley.nz/conditions.html
* https://dept.stat.lsa.umich.edu/~jerrick/courses/stat701/notes/debugging.html
* https://dept.stat.lsa.umich.edu/~jerrick/courses/stat701/notes/functions.html


For optimization tips

* https://cran.r-project.org/doc/manuals/R-exts.html#Tidying-and-profiling-R-code
* https://cran.r-project.org/doc/manuals/R-lang.html#Exception-handling
* https://adv-r.hadley.nz/perf-measure.html.libPaths()
* https://adv-r.hadley.nz/perf-improve.html
* https://cran.r-project.org/doc/manuals/R-exts.html#System-and-foreign-language-interfaces
 https://dept.stat.lsa.umich.edu/~jerrick/courses/stat701/notes/profiling.html
* https://adv-r.hadley.nz/rcpp.html
* https://bookdown.dongzhuoer.com/hadley/adv-r/

For parallel programming 

* https://dept.stat.lsa.umich.edu/~jerrick/courses/stat701/notes/parallel.html
* https://bookdown.org/rdpeng/rprogdatascience/parallel-computation.html
* https://grantmcdermott.com/ds4e/parallel.html
* https://psu-psychology.github.io/r-bootcamp-2018/talks/parallel_r.html


For general tips

* https://github.com/christophergandrud/Rep-Res-Book
* Efficient R programming. C. Gillespie R. Lovelace. 2021. https://csgillespie.github.io/efficientR/
* Data Science at the Command Line, 1e. Janssens J. 2020. https://www.datascienceatthecommandline.com/1e/
* R Programming for Data Science. Peng R. 2020. https://bookdown.org/rdpeng/rprogdatascience/
* Advanced R. H. Wickham 2019. https://adv-r.hadley.nz/
* Econometrics in R. Grant Farnsworth. 2008. http://cran.r-project.org/doc/contrib/Farnsworth-EconometricsInR.pdf
* The R Inferno. https://www.burns-stat.com/documents/books/the-r-inferno/




# Software
**** 

The current version of R (and any packages) used to make this document are

``` r
sessionInfo()
## R version 4.5.0 (2025-04-11)
## Platform: x86_64-redhat-linux-gnu
## Running under: Fedora Linux 42 (Workstation Edition)
## 
## Matrix products: default
## BLAS/LAPACK: FlexiBLAS OPENBLAS-OPENMP;  LAPACK version 3.12.0
## 
## locale:
##  [1] LC_CTYPE=en_US.UTF-8       LC_NUMERIC=C              
##  [3] LC_TIME=en_US.UTF-8        LC_COLLATE=en_US.UTF-8    
##  [5] LC_MONETARY=en_US.UTF-8    LC_MESSAGES=en_US.UTF-8   
##  [7] LC_PAPER=en_US.UTF-8       LC_NAME=C                 
##  [9] LC_ADDRESS=C               LC_TELEPHONE=C            
## [11] LC_MEASUREMENT=en_US.UTF-8 LC_IDENTIFICATION=C       
## 
## time zone: Europe/Berlin
## tzcode source: system (glibc)
## 
## attached base packages:
## [1] stats     graphics  grDevices utils     datasets  compiler  methods  
## [8] base     
## 
## other attached packages:
## [1] colorout_1.3-2
## 
## loaded via a namespace (and not attached):
##  [1] Matrix_1.7-3         jsonlite_2.0.0       Rcpp_1.0.14         
##  [4] parallel_4.5.0       jquerylib_0.1.4      splines_4.5.0       
##  [7] yaml_2.3.10          fastmap_1.2.0        lattice_0.22-7      
## [10] TH.data_1.1-3        R6_2.6.1             microbenchmark_1.5.0
## [13] knitr_1.50           htmlwidgets_1.6.4    MASS_7.3-65         
## [16] tibble_3.3.0         bookdown_0.43        profvis_0.4.0       
## [19] bslib_0.9.0          pillar_1.10.2        rlang_1.1.6         
## [22] utf8_1.2.6           multcomp_1.4-28      cachem_1.1.0        
## [25] xfun_0.52            sass_0.4.10          cli_3.6.5           
## [28] magrittr_2.0.3       digest_0.6.37        grid_4.5.0          
## [31] mvtnorm_1.3-3        sandwich_3.1-1       lifecycle_1.0.4     
## [34] vctrs_0.6.5          bench_1.1.4          evaluate_1.0.4      
## [37] glue_1.8.0           codetools_0.2-20     zoo_1.8-14          
## [40] survival_3.8-3       profmem_0.7.0        rmarkdown_2.29      
## [43] tools_4.5.0          pkgconfig_2.0.3      htmltools_0.5.8.1
```
With Rstudio, you can update both R and Rstudio.

## Latest versions

Make sure R is up to date.

Make sure your R packages are up to date.

``` r
update.packages()
```

After updating R, you can update *all* packages stored in *all* `.libPaths()` with the following command

``` r
update.packages(checkBuilt=T, ask=F)
# install.packages(old.packages(checkBuilt=T)[,"Package"])
```

#### **Tricks: Used Rarely:** {-}

To find specific broken packages after an update

``` r
library(purrr)

set_names(.libPaths()) %>%
  map(function(lib) {
    .packages(all.available = TRUE, lib.loc = lib) %>%
        keep(function(pkg) {
            f <- system.file('Meta', 'package.rds', package = pkg, lib.loc = lib)
            tryCatch({readRDS(f); FALSE}, error = function(e) TRUE)
        })
  })
# https://stackoverflow.com/questions/31935516/installing-r-packages-error-in-readrdsfile-error-reading-from-connection/55997765
```

To remove packages duplicated in multiple libraries

``` r
# Libraries
i <- installed.packages()
libs <- .libPaths()
# Find Duplicated Packages
i1 <- i[ i[,'LibPath']==libs[1], ]
i2 <- i[ i[,'LibPath']==libs[2], ]
dups <- i2[,'Package'] %in% i1[,'Package']
all( dups )
# Remove
remove.packages(  i2[,'Package'], libs[2] )
```


## General Workflow

If you want to go further down the reproducibility route (recommended, but not required for our class), consider making your entire workflow use Free Open Source Software


#### **Linux**. {-}

An alternative to windows and mac operating systems.
Used in computing clusters, big labs, and phones.
Ubuntu and Fedora are popular brands.

* https://www.r-bloggers.com/linux-data-science-virtual-machine-new-and-upgraded-tools/,
* http://www.howtogeek.com/249966/how-to-install-and-use-the-linux-bash-shell-on-windows-10/


On Fedora, you can open RStudio on the commandline with

``` bash
rstudio
```

Alternatively, you are encouraged to try using R without a GUI. E.g., on Fedora, this document can be created directly via 

``` bash
Rscript -e "rmarkdown::render('RMarkown.Rmd')"
```

#### **Latex**. {-}
An alternative to Microsoft Word.
Great for writing many equations and typesetting.
Easy to integrate Figures, Tables, and References.
Steep learning curve.

* easiest to get started online with [Overleaf](https://www.overleaf.com/)
* can also download yourself via [Tex Live](https://www.tug.org/texlive/) and GUI [TexStudio](https://www.texstudio.org/)

To begin programming, see 

* https://biostat.app.vumc.org/wiki/pub/Main/TheresaScott/Intro.to.LaTeX.TAScott.pdf
* https://www.tug.org/begin.html



## Sweave

*Sweave* is an alternative to Rmarkdown for integrating latex and R. While Rmarkdown "writes R and latex within markdown", Sweave "write R in latex". Sweave files end in ".Rnw" and can be called within R


``` r
Sweave('Sweavefile.Rnw')
```

or directly from the command line


``` bash
R CMD Sweave Sweavefile.Rnw 
```

In both cases, a latex file `Sweavefile.tex` is produced, which can then be converted to `Sweavefile.pdf`.

For more on Sweave,

* https://rpubs.com/YaRrr/SweaveIntro
* https://support.rstudio.com/hc/en-us/articles/200552056-Using-Sweave-and-knitr
* https://www.statistik.lmu.de/~leisch/Sweave/Sweave-manual.pdf


#### **Knitr**. {-} 
You can produce a pdf from an .Rnw file via `knitr`


``` bash
Rscript -e "knitr::Sweave2knitr('Sweave_file.Rnw')"
Rscript -e "knitr::knit2pdf('Sweave_file-knitr.Rnw')"
```

For background on knitr

* https://yihui.org/knitr/
* https://kbroman.org/knitr_knutshell/pages/latex.html
* https://sachsmc.github.io/knit-git-markr-guide/knitr/knit.html

## Stata

For those transitioning from Stata or replicating others' Stata work, you can work with Stata data and code within R.

Translations of common procedures is provided by https://stata2r.github.io/. See also the textbook "R for Stata Users" by Robert A. Muenchen and Joseph M. Hilbe.

Many packages allows you to read data created by different programs. As of right now, `haven` is a particularly useful for reading in Stata files

``` r
library(haven)
read_dta()
# See also foreign::read.dta
```

You can also execute stata commands directly in R via package `Rstata`. (Last time I checked, `Rstata` requires you to have purchased a non-student version of Stata.) Moreover, you can include stata in the markdown reports via package `Statamarkdown`:

``` r
library(Rstata)
library(Statamarkdown)
```

There are many R packages to replicate or otherwise directly copy what Stata does. For example, see the `margins` package  https://cran.r-project.org/web/packages/margins/vignettes/Introduction.html


For more information on R and Stata, see

* https://github.com/lbraglia/RStata
* https://ignacioriveros1.github.io/r/2020/03/22/r_and_stata.html
* https://bookdown.org/yihui/rmarkdown-cookbook/eng-stata.html
* https://rpubs.com/quarcs-lab/stata-from-Rstudio
* https://clanfear.github.io/Stata_R_Equivalency/docs/r_stata_commands.html
* https://libguides.bates.edu/c.php?g=209169&p=7233333

You can also use other software (such as Python) within R. You can also use R within Stata, or both within Python. With R, you can easily import many different data types

* https://cran.r-project.org/doc/manuals/R-data.html
* https://raw.githubusercontent.com/rstudio/cheatsheets/main/data-import.pdf






## Further Reading

Some of my programming examples originally come from <https://r4ds.had.co.nz/> and I recommend <https://intro2r.com>. 

I have also used online material from many places over the years, as there are many good yet free-online tutorials and courses specifically on R programming. See e.g., 

* <https://cran.r-project.org/doc/manuals/R-intro.html>
* R Graphics Cookbook, 2nd edition. Winston Chang. 2021. <https://r-graphics.org/>
* R for Data Science. H. Wickham and G. Grolemund. 2017. <https://r4ds.had.co.nz/index.html>
* An Introduction to R. W. N. Venables, D. M. Smith, R Core Team. 2017. <https://colinfay.me/intro-to-r/>
* Introduction to R for Econometrics. Kieran Marray. <https://bookdown.org/kieranmarray/intro_to_r_for_econometrics/>
* Wollschläger, D. (2020). Grundlagen der Datenanalyse mit R: eine anwendungsorientierte Einführung. <http://www.dwoll.de/rexrepos/>
* Spatial Data Science with R: Introduction to R. Robert J. Hijmans. 2021. <https://rspatial.org/intr/index.html>
* <https://www.econometrics-with-r.org/1.2-a-very-short-introduction-to-r-and-rstudio.html>
* <https://rafalab.github.io/dsbook/>
* <https://moderndive.com/foreword.html>
* <https://rstudio.cloud/learn/primers/1.2>
* <https://cran.r-project.org/manuals.html>
* <https://stats.idre.ucla.edu/stat/data/intro_r/intro_r_interactive_flat.html>
* <https://cswr.nrhstat.org/app-r>

