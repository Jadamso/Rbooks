# (PART) Reproducible Research in R {-} 





# Why?
***

You should make your work reproducible, and we will cover some of the basics of how to do this in R. You also want your work to be replicable

* Replicable: someone collecting new data comes to the same results.
* Reproducibile: someone reusing your data comes to the same results.

You can read more about the distinction in many places, including

* https://www.annualreviews.org/doi/10.1146/annurev-psych-020821-114157
* https://nceas.github.io/sasap-training/materials/reproducible_research_in_r_fairbanks/

My main sell to you is that being reproducible is in your own self-interest.

## An example workflow

Taking First Steps ...

**Step 1:** Some Ideas and Data

$X_{1} \to Y_{1}$

* You copy some data into a spreadsheet, manually aggregate
* do some calculations and tables the same spreadsheet
* some other analysis from here and there, using this software and that.

**Step 2:** Pursuing the lead for a week or two

* you extend your dataset with more observations
* copy in a spreadsheet data, manually aggregate
* do some more calculations and tables, same as before

Then, a Little Way Down the Road ...

**1 month later**, someone asks about another factor: $X_{2}$

* you download some other type of data
* You repeat **Step 2** with some data on $X_{2}$.
* The details from your "point and click" method are a bit fuzzy.
* It takes a little time, but you successfully redo the analysis.


**4 months later**, someone asks about another factor: $X_{3}\to Y_{1}$

* You again repeat **Step 2** with some data on $X_{3}$.
* You're pretty sure none of tables your tried messed up the order of the rows or columns.
* It takes more time and effort. The data processing was not transparent, but you eventually redo the analysis.



**6 months later**, you want to explore: $X_{2} \to Y_{2}$.

* You found out Excel had some bugs in it's statistical calculations (see e.g., https://biostat.app.vumc.org/wiki/pub/Main/TheresaScott/StatsInExcel.TAScot.handout.pdf). You now use a new version of the spreadsheet
* You're not sure you merged everything correctly. After much time and effort, most (but not all) of the numbers match exactly.
 

**2 years later**, you want to replicate: $\{ X_{1}, X_{2}, X_{3} \} \to Y_{1}$

* A rival has proposed something new. Their idea doesn't actually make any sense, but their figures and statistics look better.
* You don't even use that computer anymore and a collaborator who handled the data on $X_{2}$ has moved on.


## An alternative workflow

Suppose you decided to code what you did beginning with Step 2.

**It does not take much time to update or replicate your results**.

* Your computer runs for 2 hours and reproduces the figures and tables.
* You also rewrote your big calculations to use multiple cores, this took two hours to do but saved 6 hours *each time* you rerun your code.
* You add some more data. It adds almost no time to see whether much has changed.

**Your results are transparent and easier to build on**.

* You see the exact steps you took and found an error
  * glad you found it before publication! See https://retractionwatch.com/ and https://econjwatch.org/
  * Google "worst excell errors" and note the frequency they arise from copy/paste via the "point-and-click" approach. Future economists should also read https://core.ac.uk/download/pdf/300464894.pdf.
* You try out a new plot you found in *The Visual Display of Quantitative Information*, by Edward Tufte.
  * It's not a standard plot, but google answers most of your questions.
  * Tutorials help avoid bad practices, such as plotting 2D data as a 3D object (see e.g., https://clauswilke.com/dataviz/no-3d.html).
* You try out an obscure statistical approach that's hot in your field.
  * it doesn't make the paper, but you have some confidence that candidate issue isn't a big problem





Note that R (and Rmarkdown) is a good choice to address this issue

* http://www.r-bloggers.com/the-reproducibility-crisis-in-science-and-prospects-for-r/
* http://fmwww.bc.edu/GStat/docs/pointclick.html
* https://github.com/qinwf/awesome-R\#reproducible-research
* A Guide to Reproducible Code in Ecology and Evolution
* https://biostat.app.vumc.org/wiki/pub/Main/TheresaScott/ReproducibleResearch.TAScott.handout.pdf

## Task Views

Task views list relevant packages. 

For all students and early researchers, 

* https://cran.r-project.org/web/views/ReproducibleResearch.html

For microeconometrics,

* https://cran.r-project.org/web/views/Econometrics.html

For spatial econometrics 

* https://cran.r-project.org/web/views/Spatial.html
* https://cran.r-project.org/web/views/SpatioTemporal.html


Multiple packages may have the same function name for different commands. In this case use the syntax ``package::function`` to specify the package. For example

``` r
devtools::install_github
remotes::install_github
```


**Don't fret** Sometimes there is not a specific package for your data.

Odds are, you can do most of what you want with base code.

* Packages just wrap base code in convient formats
* see https://cran.r-project.org/web/views/ for topical overviews

Statisticians might have different naming conventions

* if the usual software just spits out a nice plot
you might have to dig a little to know precisely what you want
* your data are fundamentally numbers, strings, etc...
You only have to figure out how to read it in.


# Large Projects
***

As you scale up a project, then you will have to be more organized. 

## Scripting

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

**Restart Rstudio**. Alternatively, **clean the workspace** by

* clearing the environment and history (use the broom in top right panel)
* clearing unsaved plots (use the broom in bottom right panel)

**Replicate** in another tab *or directly in console on the bottom left) via

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

**CLI options** Note that there are also alternative ways to replicate via the command line interface (CLI) after opening a terminal.
 

``` bash
# Method 1
Rscript -e "source('MyFirstScript.R')"
# Method 2
Rscript MyFirstScript.R
```

Note that you can open a new terminal in RStudio in the top bar by
clicking 'tools > terminal > new terminal'


## Organization

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

**MAKEFILE**.

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

## Logging/Sinking

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


## Class Projects

Zip your project into a single file that is easy for *others* to identify: `Class_Project_LASTNAME_FIRSTNAME.zip`


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


## Debugging 

In R, you use multiple functions on different types of data objects. Moreover, you "typically solve complex problems by decomposing them into simple functions, not simple objects." (H. Wickham)


We can use the following packages to help deal with various problems that may arise

``` r
library(microbenchmark)
library(compiler)
library(profvis)
library(parallel)
library(Rcpp)
```

Problems print to the console

``` r
message("This is what a message looks like")

warning("This is what a warning looks like")

stop("This is what an error looks like")
```

```
## Error: This is what an error looks like
```

Nonproblems also print to the console

``` r
cat('cat\n')
```

```
## cat
```

``` r
print('print')
```

```
## [1] "print"
```

**Tracing**.

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
```

```
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
```

```
## f2 calls g2()
## g2 calls h2() 
## b = a 
## h2 call i()
```

```
## Error: `d` must be numeric
```

If that fails, try traceback debugging

``` r
traceback()
```

```
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
```

```
## Called from: g3(g0)
## debug: h(h0)
```

```
## Error: `d` must be numeric
```


**Isolating**.

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

**Handling**.

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
```

```
## <simpleWarning in log(x): NaNs produced>
```

```
## [1] NA
```

<!--# Ignore warnings/messages
    Supressing errors is possible but a bad idea
    
    ``` r
    try(1+2, silent=T)
    ```
    
    ```
    ## [1] 3
    ```
    
    ``` r
    try(warning('warning'), silent=T)
    try(error('error'), silent=T)
    
    try(1+2, silent=F)
    ```
    
    ```
    ## [1] 3
    ```
    
    ``` r
    try(warning('warning'), silent=F)
    try(error('error'), silent=F)
    ```
    
    ```
    ## Error in error("error") : could not find function "error"
    ```
    
    ``` r
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
```

```
## [1] 0
```

``` r
log_safe(-1)
```

```
## Warning Caught: 
## 	<simpleWarning in log(x): NaNs produced>
```

```
## [1] NA
```

``` r
log_safe(' ')
```

```
## Error Caught: 
## 	<simpleError in log(x): non-numeric argument to mathematical function>
```

```
## [1] NA
```

``` r
# Further Tests
s <- sapply(list("A",Inf, -Inf, NA, NaN, 0, -1, 1), log_safe)
```

```
## Error Caught: 
## 	<simpleError in log(x): non-numeric argument to mathematical function>
## Warning Caught: 
## 	<simpleWarning in log(x): NaNs produced>
## Warning Caught: 
## 	<simpleWarning in log(x): NaNs produced>
```

``` r
s
```

```
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


**Benchmarking**.

For identifying bottlenecks, the simplest approach is to time how long a code-chunk runs

``` r
system.time({
    x0 <- runif(1e5)
    x1 <- sqrt(x0)
    x2 <- paste0('J-', x1)
})
```

```
##    user  system elapsed 
##   0.125   0.005   0.130
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

```{=html}
<div class="profvis html-widget html-fill-item" id="htmlwidget-206c60ca412e6eaf850c" style="width:100%;height:600px;"></div>
<script type="application/json" data-for="htmlwidget-206c60ca412e6eaf850c">{"x":{"message":{"prof":{"time":[1,2,3,4,5,6,7,8,9,9,10,10,11,11,12,12,13,13,14,14,15,15,16,16,17,17,18,18,19,19,20,20,21,21,22,22,23,23,23,24,25,25,26,26,27,27,28,28,29,29,30,30,31,32,33,33,34,34,35,35,36,36,37,37,38,38,39,39,39,40,40,41,41,42,42,42,43,44,44,45,45,45,46,46,47,47,48,49,49,50,50,50,50,51,51,52,53,53,53,54,54,55,55,55,56,56,57,57,58,58,59,59,60,60,61,61,62,62,62,63,64,65,65,65,66,66,67,67,68,69,70,70,70,71,71,71,72,72,72,73,74,74,75,75,76,76,77,77,77,78,78,79,79,80,81,82,82,82,83,83,84,85,86,87,87,88,88,89,89,90,90,91,91,92,92,92,93,93,94,95,95,96,96,96,97,98,98,99,99,100,100,101,101,101,102,103,103,103,104,104,105,105,105,106,106,106,107,108,109,109,110,110,110,111,111,111,112,113,113,114,114,114,115,115,115,116,117,117,118,118,119,119,119,120,121,121,122,122,123,123,123,124,125,126,127,128,128,128,129,129,130,131,131,132,132,133,133,134,134,134,135,136,136,136,137,138,138,139,139,140,140,140,141,141,142,142,143,143,143,144,144,144,145,145,145,146,146,147,148,148,148,149,149,149,150,151,152,153,153,154,154,155,156,156,157,157,157,158,158,159,160,160,161,161,162,163,163,164,164,165,165,165,165,166,166,166,166,167,167,167,167,168,168,169,169,170,171,171,171,172,172,173,173,174,174,174,175,175,176,177,177,178,178,178,179,179,180,181,181,182,182,183,184,185,185,186,186,187,187,188,188,188,189,189,189,190,191,192,193,193,193,194,194,194,195,195,196,197,197,197,198,198,199,199,200,200,200,201,201,202,202,203,203,204,204,205,205,206,206,207,207,207,207,208,208,209,210,210,211,211,212,213,213,214,214,214,215,216,216,217,217,217,218,219,220,220,220,221,221,221,222,222,223,224,224,225,225,225,226,226,226,227,227,227,228,228,229,229,230,230,230,231,231,232,233,233,234,234,235,235,236,236,237,237,238,238,239,239,240,240,241,241,242,242,243,243,244,244,244,245,245,246,246,247,247,248,249,249,250,250,251,251,252,252,253,253,254,254,254,255,255,256,256,257,257,258,258,258,259,259,260,260,261,262,263,263,264,264,265,265,265,266,266,266,267,268,268,268,269,270,270,271,272,272,273,273,274,274,275,275,275,276,276,276,277,277,278,278,279,280,280,280,281,281,282,283,283,284,284,285,286,286,286,286,287,288,289,290,291,291,292,292,292,293,293,293,294,294,295,295,296,296,296,297,298,298,299,300,300,301,301,302,302,303,303,304,304,305,305,306,306,306,307,307,308,309,309,310,310,311,312,313,313,314,315,315,316,316,317,317,318,319,319,319,320,320,321,321,322,322,323,324,325,325,326,327,327,328,329,329,330,330,331,332,333,333,334,334,335,335,336,336,337,338,338,339,340,341,342,342,343,343,344,344,345,346,347,347,348,348,349,349,350,350,351,351,352,352,352,353,353,353,354,354,354,355,355,356,357,358,358,359,359,360,360,361,361,362,362,363,364,365,365,366,366,367,367,368,369,369,370,370,370,371,371,371,372,372,373,374,374,374,375,375,376,377,378,378,379,379,380,380,381,382,383,384,384,385,385,386,386,387,387,388,388,388,389,389,389,390,391,392,392,393,393,394,394,395,395,396,396,397,397,397,398,398,399,399,400,401,401,402,402,403,403,404,404,405,405,405,406,406,406,407,407,408,409,409,410,410,411,411,412,412,413,414,414,414,415,415,416,417,418,419,419,419,420,420,421,422,422,422,423,423,423,424,424,425,426,426,426,427,427,428,429,429,429,430,430,431,431,432,433,433,434,434,435,435,436,436,437,438,438,439,439,440,440,440,441,442,443,443,444,445,446,447,447,447,447,448,448,449,450,450,451,452,452,453,453,454,455,455,455,456,456,456,457,458,458,459,459,460,460,461,462,463,463,463,464,464,464,465,465,465,466,466,466,467,467,467,468,468,468,469,470,470,471,471,472,472,472,473,473,474,475,476,476,476,477,478,479,479,480,480,481,481,482,482,483,483,483,484,484,484,485,485,486,486,487,487,488,488,489,489,490,490,491,491,492,493,493,494,495,496,497,497,498,498,499,499,500,501,501,502,503,504,505,505,506,506,506,507,507,508,508,509,510,510,511,511,512,512,513,513,514,514,515,515,516,516,517,518,519,520,520,520,520,521,521,521,521,522,523,524,524,525,525,525,526,526,527,527,527,528,528,528,529,529,530,530,530,531,531,532,533,533,534,534,535,535,536,536,537,538,538,539,539,540,541,541,541,542,543,544,544,545,546,547,547,548,548,548,549,549,550,550,551,551,552,552,553,553,554,555,555,555,556,556,557,557,558,559,559,560,560,561,561,562,562,563,564,564,565,566,566,567,568,568,568,568,569,569,570,571,571,572,572,573,574,574,574,575,575,575,576,577,578,578,578,579,579,580,581,581,582,583,584,585,585,586,586,587,587,587,588,588,588,589,589,590,590,591,592,593,593,593,593,594,594,594,594,595,595,596,596,596,597,597,598,598,599,599,600,600,601,601,602,602,603,604,605,605,606,606,607,607,608,609,610,610,611,612,612,612,613,613,613,614,614,614,615,615,615,616,616,616,617,617,617,618,619,619,620,621,621,622,623,623,623,624,625,625,626,626,627,627,628,628,628,629,629,629,630,630,631,631,632,632,633,634,634,635,635,636,636,637,637,638,639,640,641,641,641,641,642,642,642,643,643,644,644,644,645,645,646,646,646,647,647,647,648,648,649,649,650,650,651,652,652,653,653,654,654,655,655,656,657,657,658,658,659,659,660,660,661,662,662,663,664,664,664,665,665,666,666,667,667,668,669,669,669,670,670,670,671,671,672,673,674,675,675,675,676,676,676,677,677,678,678,679,680,680,681,681,681,682,683,683,684,684,685,685,685,686,686,686,687,687,687,688,688,689,690,690,690,691,692,692,692,693,693,694,694,695,695,696,696,697,697,697,698,698,698,699,699,700,700,701,702,702,703,703,704,704,705,705,706,706,707,708,708,709,709,710,710,711,711,711,712,712,712,713,713,713,714,714,714,715,715,715,716,716,716,717,717,717,718,718,718,719,719,719,720,720,720,721,721,721,722,722,722,723,723,723,724,724,724,725,725,725,726,726,726,727,727,727,728,728,728,729,729,729,730,730,730,731,731,731,732,732,732,733,733,733,734,734,734,735,735,735,736,736,736,737,737,737,738,738,738,739,739,740,741,741,742,742,743,743,743,744,744,744,745,745,746,746,747,747,748,748,748,749,749,749,750,750,751,751,752,752,753,753,753,754,754,755,755,756,756,757,757,758,759,760,760,761,761,762,762,763,764,764,765,765,766,767,767,768,769,769,770,770,771,771,772,772,773,774,774,775,776,777,777,777,778,779,780,780,781,781,782,783,783,784,784,785,785,786,786,787,787,788,788,789,789,790,791,791,792,793,793,794,794,795,796,796,797,798,798,799,799,800,800,801,802,802,803,804,804,804,805,805,806,806,807,807,808,809,809,810,810,811,811,812,812,813,814,815,815,816,817,817,818,818,819,819,819,820,820,820,821,821,821,822,822,822,823,823,824,824,825,825,826,827,827,828,829,829,830,830,830,831,831,832,832,833,833,834,834,835,835,836,836,837,838,838,839,839,840,840,841,842,842,843,844,844,844,845,846,846,847,848,849,850,850,851,851,852,852,853,853,854,854,855,855,856,856,856,857,858,858,859,860,861,861,861,862,863,864,864,865,865,866,866,867,867,868,868,868,869,869,869,870,871,871,872,873,874,874,874,875,875,876,876,877,877,877,878,879,879,880,880,880,881,881,881,882,882,883,883,883,884,884,884,885,886,886,887,888,889,889,890,890,891,892,893,893,894,894,895,896,897,897,898,898,898,899,899,899,900,900,901,901,902,902,903,903,904,904,905,906,906,907,908,908,909,910,910,911,912,912,913,913,914,914,915,915,916,916,917,917,918,918,919,919,920,920,920,921,921,922,922,923,923,924,924,925,925,926,927,927,927,928,928,928,929,930,930,931,931,932,932,933,933,934,935,935,936,937,938,938,939,939,940,941,941,942,942,943,943,944,944,944,945,945,946,946,947,948,948,949,950,950,950,951,951,952,952,952,953,954,954,954,955,955,955,956,956,957,957,958,959,959,960,960,961,962,962,963,963,964,965,965,966,966,967,967,968,968,969,969,970,970,971,971,972,972,973,974,974,975,975,976,976,977,977,978,978,979,979,980,980,981,982,982,983,983,984,984,985,985,986,986,986,987,988,988,989,990,990,991,991,992,992,993,993,994,995,995,995,996,996,996,997,997,998,998,999,999,999,1000,1000,1001,1001,1002,1003,1003,1004,1004,1005,1005,1006,1007,1008,1008,1008,1009,1009,1009,1010,1011,1012,1013,1014,1014,1015,1016,1016,1017,1017,1017,1018,1018,1018,1019,1019,1020,1020,1021,1021,1021,1022,1022,1022,1023,1024,1024,1025,1025,1026,1026,1027,1027,1028,1028,1029,1029,1030,1030,1030,1031,1032,1033,1034,1034,1034,1035,1035,1035,1036,1036,1037,1037,1038,1039,1039,1040,1040,1041,1042,1043,1044,1044,1045,1045,1045,1046,1046,1047,1047,1047,1048,1048,1048,1049,1050,1050,1051,1052,1052,1053,1053,1054,1055,1055,1056,1057,1058,1058,1059,1059,1059,1059,1060,1060,1060,1060,1061,1061,1062,1062,1063,1063,1064,1065,1066,1066,1067,1068,1068,1069,1070,1071,1072,1072,1073,1073,1074,1074,1075,1076,1076,1077,1077,1078,1078,1079,1079,1080,1080,1081,1081,1081,1082,1082,1082,1083,1084,1084,1084,1085,1085,1085,1086,1087,1087,1088,1088,1089,1089,1090,1090,1091,1092,1093,1093,1094,1094,1095,1095,1095,1096,1096,1097,1097,1098,1099,1099,1100,1100,1101,1101,1101,1102,1102,1103,1103,1103,1104,1104,1105,1106,1107,1107,1108,1108,1109,1110,1111,1112,1113,1114,1114,1114,1115,1116,1117,1117,1117,1118,1118,1119,1119,1120,1120,1121,1121,1121,1122,1122,1123,1123,1124,1124,1125,1125,1125,1126,1127,1128,1128,1129,1129,1130,1130,1131,1131,1131,1132,1132,1132,1133,1133,1133,1134,1134,1134,1135,1135,1135,1136,1136,1136,1137,1137,1137,1138,1138,1138,1139,1139,1139,1140,1140,1140,1141,1141,1141,1142,1142,1142,1143,1143,1143,1144,1144,1144,1145,1145,1145,1146,1146,1146,1147,1147,1147,1148,1148,1148,1149,1149,1149,1150,1150,1150,1151,1151,1151,1152,1152,1152,1153,1153,1153,1154,1154,1154,1155,1155,1155,1156,1156,1156,1157,1157,1157,1158,1158,1158,1159,1159,1159,1160,1160,1160,1161,1161,1161,1162,1162,1162,1163,1163,1163,1164,1164,1164,1165,1165,1165,1166,1166,1166,1167,1167,1167,1168,1168,1168,1169,1169,1169,1170,1170,1170,1171,1171,1171,1172,1172,1172,1173,1173,1173,1174,1174,1174,1175,1175,1176,1176,1177,1177,1178,1178,1179,1180,1180,1181,1181,1182,1183,1183,1184,1184,1184,1185,1185,1185,1186,1186,1187,1187,1188,1188,1188,1189,1190,1191,1191,1192,1192,1193,1193,1194,1194,1194,1195,1195,1195,1196,1196,1196,1197,1197,1197,1198,1199,1199,1199,1200,1200,1201,1201,1202,1202,1203,1204,1205,1206,1206,1206,1207,1207,1207,1208,1208,1208,1209,1209,1210,1210,1210,1211,1212,1212,1213,1213,1214,1215,1215,1216,1217,1217,1217,1218,1218,1219,1219,1220,1220,1221,1221,1222,1223,1223,1224,1224,1225,1225,1225,1226,1226,1227,1228,1229,1229,1229,1230,1230,1230,1231,1232,1233,1234,1234,1235,1235,1236,1236,1237,1237,1238,1239,1240,1240,1240,1240,1241,1241,1241,1241,1242,1243,1243,1244,1245,1245,1246,1247,1248,1249,1249,1250,1250,1250,1251,1251,1251,1252,1252,1252,1253,1253,1254,1254,1255,1255,1256,1256,1257,1258,1258,1259,1259,1259,1260,1260,1260,1261,1261,1261,1262,1262,1263,1263,1264,1265,1266,1266,1267,1268,1269,1269,1269,1270,1270,1271,1271,1271,1272,1272,1272,1273,1274,1274,1275,1275,1276,1276,1277,1277,1278,1278,1279,1279,1280,1281,1281,1282,1282,1283,1283,1284,1284,1285,1285,1286,1286,1287,1287,1288,1288,1289,1289,1290,1290,1291,1291,1292,1292],"depth":[1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,3,2,1,1,2,1,3,2,1,2,1,2,1,1,2,1,4,3,2,1,2,1,1,3,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,1,3,2,1,2,1,2,1,1,1,3,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,1,3,2,1,2,1,1,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,3,2,1,1,2,1,2,1,2,1,3,2,1,1,3,2,1,2,1,3,2,1,3,2,1,1,1,2,1,3,2,1,3,2,1,1,2,1,3,2,1,3,2,1,1,2,1,2,1,3,2,1,1,2,1,2,1,3,2,1,1,1,1,1,3,2,1,2,1,1,2,1,2,1,2,1,3,2,1,1,3,2,1,1,2,1,2,1,3,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,1,3,2,1,3,2,1,1,1,1,2,1,2,1,1,2,1,3,2,1,2,1,1,2,1,2,1,1,2,1,2,1,4,3,2,1,4,3,2,1,4,3,2,1,2,1,2,1,1,3,2,1,2,1,2,1,3,2,1,2,1,1,2,1,3,2,1,2,1,1,2,1,2,1,1,1,2,1,2,1,2,1,3,2,1,3,2,1,1,1,1,3,2,1,3,2,1,2,1,1,3,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,4,3,2,1,2,1,1,2,1,2,1,1,2,1,3,2,1,1,2,1,3,2,1,1,1,3,2,1,3,2,1,2,1,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,1,2,1,2,1,3,2,1,3,2,1,1,3,2,1,1,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,1,3,2,1,2,1,1,2,1,2,1,1,4,3,2,1,1,1,1,1,2,1,3,2,1,3,2,1,2,1,2,1,3,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,1,1,2,1,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,2,1,1,1,2,1,1,2,1,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,1,2,1,1,1,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,1,2,1,3,2,1,3,2,1,2,1,1,3,2,1,2,1,1,1,2,1,2,1,2,1,1,1,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,1,1,1,3,2,1,2,1,1,3,2,1,3,2,1,2,1,1,3,2,1,2,1,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,1,1,2,1,1,1,1,4,3,2,1,2,1,1,2,1,1,2,1,2,1,1,3,2,1,3,2,1,1,2,1,2,1,2,1,1,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,1,2,1,2,1,3,2,1,2,1,1,1,3,2,1,1,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,1,1,2,1,2,1,2,1,1,2,1,1,1,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,1,4,3,2,1,4,3,2,1,1,1,2,1,3,2,1,2,1,3,2,1,3,2,1,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,3,2,1,1,1,2,1,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,1,4,3,2,1,2,1,1,2,1,2,1,1,3,2,1,3,2,1,1,1,3,2,1,2,1,1,2,1,1,1,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,1,1,4,3,2,1,4,3,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,1,1,2,1,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,1,2,1,1,2,1,1,3,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,1,1,4,3,2,1,3,2,1,2,1,3,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,1,3,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,2,1,1,1,1,3,2,1,3,2,1,2,1,2,1,1,2,1,3,2,1,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,1,3,2,1,1,3,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,1,1,3,2,1,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,1,2,1,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,1,2,1,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,1,3,2,1,1,2,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,1,1,3,2,1,1,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,1,2,1,1,1,3,2,1,2,1,2,1,3,2,1,1,2,1,3,2,1,3,2,1,2,1,3,2,1,3,2,1,1,2,1,1,1,2,1,2,1,1,1,2,1,2,1,1,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,1,2,1,1,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,1,3,2,1,2,1,3,2,1,1,3,2,1,3,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,1,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,1,1,3,2,1,3,2,1,1,1,1,1,2,1,1,2,1,3,2,1,3,2,1,2,1,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,1,1,3,2,1,3,2,1,2,1,2,1,1,2,1,2,1,1,1,1,2,1,3,2,1,2,1,3,2,1,3,2,1,1,2,1,1,2,1,2,1,1,2,1,1,1,2,1,4,3,2,1,4,3,2,1,2,1,2,1,2,1,1,1,2,1,1,2,1,1,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,3,2,1,2,1,1,1,2,1,2,1,1,1,1,1,1,3,2,1,1,1,3,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,3,2,1,1,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,3,2,1,3,2,1,2,1,2,1,3,2,1,1,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,1,3,2,1,2,1,2,1,2,1,1,1,1,3,2,1,3,2,1,3,2,1,2,1,3,2,1,1,2,1,2,1,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,1,1,3,2,1,3,2,1,1,1,1,2,1,2,1,2,1,2,1,1,1,4,3,2,1,4,3,2,1,1,2,1,1,2,1,1,1,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,1,1,2,1,1,1,3,2,1,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1],"label":["rowSums","rowSums","rowSums","rowSums","rowMeans","rowMeans","rowMeans","rowMeans","aperm.default","apply","aperm.default","apply","aperm.default","apply","aperm.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","<GC>","mean.default","apply","apply","mean.default","apply","length","local","length","local","<GC>","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","<GC>","apply","mean.default","apply","length","local","mean.default","apply","mean.default","apply","<GC>","is.numeric","local","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","apply","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","FUN","apply","apply","FUN","apply","<GC>","isTRUE","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","<GC>","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","<GC>","FUN","apply","is.na","local","FUN","apply","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","is.numeric","local","is.na","local","mean.default","apply","<GC>","is.numeric","local","mean.default","apply","FUN","apply","apply","apply","<GC>","mean.default","apply","mean.default","apply","apply","apply","apply","<GC>","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","mean.default","apply","apply","FUN","apply","<GC>","mean.default","apply","apply","length","local","FUN","apply","mean.default","apply","<GC>","mean.default","apply","apply","isTRUE","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","apply","apply","FUN","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","mean.default","apply","<GC>","FUN","apply","apply","length","local","FUN","apply","<GC>","FUN","apply","apply","apply","apply","apply","<GC>","FUN","apply","FUN","apply","apply","FUN","apply","<GC>","apply","FUN","apply","isTRUE","mean.default","apply","apply","<GC>","length","local","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","is.numeric","local","mean.default","apply","isTRUE","mean.default","apply","<GC>","is.numeric","local","<GC>","is.numeric","local","FUN","apply","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","apply","apply","apply","<GC>","apply","mean.default","apply","apply","mean.default","apply","<GC>","mean.default","apply","FUN","apply","apply","FUN","apply","<GC>","apply","apply","mean.default","apply","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","apply","<GC>","is.na","local","FUN","apply","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","mean.default","apply","<GC>","mean.default","apply","length","local","apply","FUN","apply","<GC>","apply","apply","apply","FUN","apply","<GC>","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","mean.default","apply","apply","apply","apply","<GC>","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","<GC>","FUN","apply","FUN","apply","mean.default","apply","<GC>","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","<GC>","apply","mean.default","apply","mean.default","apply","<GC>","isTRUE","mean.default","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","apply","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","<GC>","FUN","apply","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","apply","<GC>","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","<GC>","mean.default","apply","length","local","mean.default","apply","<GC>","mean.default","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","apply","FUN","apply","length","local","isTRUE","mean.default","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","isTRUE","mean.default","apply","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","is.numeric","local","FUN","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","mean.default","apply","apply","isTRUE","mean.default","apply","length","local","apply","is.na","local","mean.default","apply","apply","<GC>","isTRUE","mean.default","apply","apply","apply","apply","apply","mean.default","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","<GC>","FUN","apply","apply","FUN","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","length","local","FUN","apply","mean.default","apply","<GC>","is.numeric","local","FUN","apply","apply","is.na","local","FUN","apply","apply","apply","mean.default","apply","apply","<GC>","apply","<GC>","apply","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","<GC>","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","apply","is.numeric","local","<GC>","apply","FUN","apply","length","local","apply","mean.default","apply","apply","apply","apply","FUN","apply","<GC>","apply","<GC>","apply","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","is.numeric","local","<GC>","FUN","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","<GC>","apply","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","is.numeric","local","apply","isTRUE","mean.default","apply","mean.default","apply","apply","apply","length","local","<GC>","apply","<GC>","apply","apply","apply","apply","is.numeric","local","FUN","apply","FUN","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","apply","FUN","apply","length","local","FUN","apply","mean.default","apply","FUN","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","<GC>","FUN","apply","FUN","apply","apply","apply","apply","isTRUE","mean.default","apply","mean.default","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","mean.default","apply","apply","isTRUE","mean.default","apply","<GC>","apply","<GC>","apply","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","apply","length","local","<GC>","apply","isTRUE","mean.default","apply","apply","apply","mean.default","apply","apply","apply","apply","<GC>","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","<GC>","mean.default","apply","isTRUE","mean.default","apply","apply","is.numeric","local","FUN","apply","FUN","apply","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","<GC>","FUN","apply","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","is.numeric","local","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","<GC>","apply","apply","FUN","apply","apply","apply","apply","is.na","local","<GC>","apply","<GC>","apply","apply","FUN","apply","apply","apply","apply","mean.default","apply","<GC>","length","local","is.numeric","local","FUN","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","<GC>","apply","FUN","apply","FUN","apply","is.na","local","apply","apply","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","mean.default","apply","<GC>","apply","<GC>","apply","mean.default","apply","apply","is.numeric","local","FUN","apply","apply","<GC>","FUN","apply","apply","apply","is.numeric","local","apply","apply","FUN","apply","<GC>","is.numeric","local","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","<GC>","FUN","apply","FUN","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","<GC>","apply","<GC>","apply","apply","FUN","apply","apply","FUN","apply","apply","<GC>","isTRUE","mean.default","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","apply","isTRUE","mean.default","apply","mean.default","apply","apply","<GC>","apply","apply","apply","apply","mean.default","apply","FUN","apply","<GC>","length","local","<GC>","length","local","FUN","apply","is.numeric","local","apply","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","length","local","<GC>","apply","mean.default","apply","length","local","apply","apply","FUN","apply","<GC>","apply","FUN","apply","apply","apply","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","apply","mean.default","apply","apply","<GC>","mean.default","apply","apply","mean.default","apply","mean.default","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","length","local","FUN","apply","mean.default","apply","apply","<GC>","apply","<GC>","apply","mean.default","apply","is.na","local","apply","apply","apply","<GC>","isTRUE","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","is.na","local","<GC>","is.numeric","local","<GC>","is.numeric","local","length","local","mean.default","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","<GC>","apply","<GC>","apply","FUN","apply","apply","mean.default","apply","apply","<GC>","mean.default","apply","FUN","apply","length","local","FUN","apply","apply","<GC>","is.numeric","local","<GC>","is.numeric","local","is.numeric","local","apply","apply","apply","<GC>","is.numeric","local","<GC>","is.numeric","local","FUN","apply","FUN","apply","apply","mean.default","apply","<GC>","mean.default","apply","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","is.na","local","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","apply","mean.default","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","is.na","local","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","apply","<GC>","apply","FUN","apply","apply","apply","FUN","apply","length","local","FUN","apply","apply","is.numeric","local","mean.default","apply","apply","FUN","apply","apply","FUN","apply","mean.default","apply","<GC>","apply","<GC>","apply","apply","mean.default","apply","apply","apply","isTRUE","mean.default","apply","apply","apply","length","local","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","apply","<GC>","apply","FUN","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","apply","<GC>","FUN","apply","mean.default","apply","is.numeric","local","FUN","apply","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","apply","apply","mean.default","apply","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","mean.default","apply","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","apply","<GC>","apply","apply","mean.default","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","apply","apply","FUN","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","mean.default","apply","FUN","apply","is.numeric","local","<GC>","FUN","apply","<GC>","FUN","apply","apply","mean.default","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","FUN","apply","apply","apply","length","local","mean.default","apply","apply","apply","FUN","apply","FUN","apply","apply","apply","is.na","local","<GC>","FUN","apply","<GC>","FUN","apply","length","local","FUN","apply","mean.default","apply","length","local","mean.default","apply","apply","FUN","apply","apply","FUN","apply","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","FUN","apply","length","local","FUN","apply","FUN","apply","isTRUE","mean.default","apply","is.numeric","local","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","FUN","apply","apply","apply","FUN","apply","mean.default","apply","apply","<GC>","apply","<GC>","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","apply","FUN","apply","apply","isTRUE","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","apply","<GC>","length","local","<GC>","length","local","FUN","apply","FUN","apply","apply","mean.default","apply","is.numeric","local","apply","mean.default","apply","FUN","apply","apply","length","local","mean.default","apply","mean.default","apply","<GC>","apply","<GC>","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","length","local","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","apply","<GC>","length","local","<GC>","length","local","is.na","local","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","apply","apply","apply","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","length","local","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","FUN","apply","apply","FUN","apply","length","local","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","mean.default","apply","apply","is.numeric","local","is.na","local","apply","FUN","apply","apply","apply","is.numeric","local","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","apply","FUN","apply","apply","apply","apply","<GC>","apply","is.numeric","local","FUN","apply","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","<GC>","is.na","local","<GC>","is.na","local","apply","is.na","local","mean.default","apply","mean.default","apply","mean.default","apply","apply","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","<GC>","apply","<GC>","apply","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","length","local","isTRUE","mean.default","apply","mean.default","apply","apply","apply","<GC>","apply","<GC>","apply","apply","apply","apply","apply","apply","isTRUE","mean.default","apply","apply","apply","isTRUE","mean.default","apply","length","local","<GC>","apply","<GC>","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","mean.default","apply","FUN","apply","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","length","local","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","length","local","FUN","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","is.numeric","local","apply","apply","apply","isTRUE","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","mean.default","apply","apply","FUN","apply","apply","isTRUE","mean.default","apply","<GC>","apply","<GC>","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","<GC>","is.numeric","local","<GC>","is.numeric","local","apply","apply","apply","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","apply","FUN","apply","apply","FUN","apply","apply","apply","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","mean.default","apply","apply","apply","length","local","apply","apply","isTRUE","mean.default","apply","mean.default","apply","<GC>","length","local","<GC>","length","local","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply"],"filenum":[null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null],"linenum":[null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null],"memalloc":[122.8409729003906,122.8409729003906,122.8409729003906,122.8409729003906,138.0999145507812,138.0999145507812,138.0999145507812,138.0999145507812,168.173095703125,168.173095703125,168.173095703125,168.173095703125,168.173095703125,168.173095703125,168.173095703125,168.173095703125,168.1731414794922,168.1731414794922,168.1729888916016,168.1729888916016,168.1729888916016,168.1729888916016,168.1729888916016,168.1729888916016,168.1729888916016,168.1729888916016,183.5497207641602,183.5497207641602,183.9559631347656,183.9559631347656,184.3411331176758,184.3411331176758,184.7056045532227,184.7056045532227,185.0790557861328,185.0790557861328,185.2138061523438,185.2138061523438,185.2138061523438,183.8004760742188,184.1654052734375,184.1654052734375,184.5424652099609,184.5424652099609,184.9237747192383,184.9237747192383,185.2431869506836,185.2431869506836,183.6718368530273,183.6718368530273,184.0773620605469,184.0773620605469,184.4412994384766,184.7927780151367,185.1609268188477,185.1609268188477,185.2905044555664,185.2905044555664,183.9309921264648,183.9309921264648,184.3177795410156,184.3177795410156,184.6864395141602,184.6864395141602,185.041259765625,185.041259765625,185.3370819091797,185.3370819091797,185.3370819091797,183.8177871704102,183.8177871704102,184.2143859863281,184.2143859863281,184.5905990600586,184.5905990600586,184.5905990600586,184.9677352905273,185.3406143188477,185.3406143188477,185.3828659057617,185.3828659057617,185.3828659057617,184.1611862182617,184.1611862182617,184.5435028076172,184.5435028076172,184.9154968261719,185.2897872924805,185.2897872924805,185.4279251098633,185.4279251098633,185.4279251098633,185.4279251098633,184.1241149902344,184.1241149902344,184.5159530639648,184.8943099975586,184.8943099975586,184.8943099975586,185.2707443237305,185.2707443237305,185.472297668457,185.472297668457,185.472297668457,184.1334457397461,184.1334457397461,184.5221099853516,184.5221099853516,184.9065399169922,184.9065399169922,185.2857666015625,185.2857666015625,185.5158462524414,185.5158462524414,184.1706466674805,184.1706466674805,184.5605773925781,184.5605773925781,184.5605773925781,184.9445648193359,185.3199081420898,185.5588531494141,185.5588531494141,185.5588531494141,184.2303924560547,184.2303924560547,184.6211395263672,184.6211395263672,184.9997711181641,185.3717193603516,185.6010208129883,185.6010208129883,185.6010208129883,185.6010208129883,185.6010208129883,185.6010208129883,185.6010208129883,185.6010208129883,185.6010208129883,184.2264022827148,184.6235885620117,184.6235885620117,184.9982299804688,184.9982299804688,185.365837097168,185.365837097168,185.6425552368164,185.6425552368164,185.6425552368164,184.302619934082,184.302619934082,184.6975936889648,184.6975936889648,185.068603515625,185.4459838867188,185.6834259033203,185.6834259033203,185.6834259033203,184.3957443237305,184.3957443237305,184.7924728393555,185.1710433959961,185.5502471923828,185.7236175537109,185.7236175537109,184.5424728393555,184.5424728393555,184.9306640625,184.9306640625,185.3092880249023,185.3092880249023,185.6913146972656,185.6913146972656,185.7632598876953,185.7632598876953,185.7632598876953,184.6999969482422,184.6999969482422,185.0856323242188,185.4639587402344,185.4639587402344,185.802116394043,185.802116394043,185.802116394043,184.4914398193359,184.8850173950195,184.8850173950195,185.2711868286133,185.2711868286133,185.6513290405273,185.6513290405273,185.8404541015625,185.8404541015625,185.8404541015625,184.7137298583984,185.1004486083984,185.1004486083984,185.1004486083984,185.4814300537109,185.4814300537109,185.8639450073242,185.8639450073242,185.8639450073242,185.8781356811523,185.8781356811523,185.8781356811523,184.9426116943359,185.3276596069336,185.7072677612305,185.7072677612305,185.9152221679688,185.9152221679688,185.9152221679688,184.8079681396484,184.8079681396484,184.8079681396484,185.1922912597656,185.5751571655273,185.5751571655273,185.9516983032227,185.9516983032227,185.9516983032227,185.9516983032227,185.9516983032227,185.9516983032227,185.0739364624023,185.4590530395508,185.4590530395508,185.8441009521484,185.8441009521484,185.9875869750977,185.9875869750977,185.9875869750977,184.9872970581055,185.3750762939453,185.3750762939453,185.7602005004883,185.7602005004883,186.0229034423828,186.0229034423828,186.0229034423828,184.9129180908203,185.2940979003906,185.6714935302734,186.0499954223633,186.0576629638672,186.0576629638672,186.0576629638672,185.1909713745117,185.1909713745117,185.5788421630859,185.9579772949219,185.9579772949219,186.0918197631836,186.0918197631836,185.118537902832,185.118537902832,185.5002365112305,185.5002365112305,185.5002365112305,185.8740310668945,186.1254425048828,186.1254425048828,186.1254425048828,185.0643539428711,185.4427871704102,185.4427871704102,185.8325881958008,185.8325881958008,186.1585693359375,186.1585693359375,186.1585693359375,185.0604858398438,185.0604858398438,185.4403991699219,185.4403991699219,185.8253936767578,185.8253936767578,185.8253936767578,186.1910781860352,186.1910781860352,186.1910781860352,186.1910781860352,186.1910781860352,186.1910781860352,185.4295883178711,185.4295883178711,185.813232421875,186.1929168701172,186.1929168701172,186.1929168701172,186.2230911254883,186.2230911254883,186.2230911254883,185.4542694091797,185.8370513916016,186.2183609008789,186.2546157836914,186.2546157836914,185.4682083129883,185.4682083129883,185.8553237915039,186.2301330566406,186.2301330566406,186.2855453491211,186.2855453491211,186.2855453491211,185.4850769042969,185.4850769042969,185.8722457885742,186.2554321289062,186.2554321289062,186.3160858154297,186.3160858154297,185.5430526733398,185.932975769043,185.932975769043,186.3095550537109,186.3095550537109,186.3460540771484,186.3460540771484,186.3460540771484,186.3460540771484,186.3460540771484,186.3460540771484,186.3460540771484,186.3460540771484,186.3460540771484,186.3460540771484,186.3460540771484,186.3460540771484,185.6041641235352,185.6041641235352,185.9908599853516,185.9908599853516,186.3726654052734,186.375358581543,186.375358581543,186.375358581543,185.6725616455078,185.6725616455078,186.0497665405273,186.0497665405273,186.4044189453125,186.4044189453125,186.4044189453125,185.4148330688477,185.4148330688477,185.78759765625,186.1713333129883,186.1713333129883,186.432975769043,186.432975769043,186.432975769043,185.5405349731445,185.5405349731445,185.9261779785156,186.3078384399414,186.3078384399414,186.4611053466797,186.4611053466797,185.6831359863281,186.0675354003906,186.4513168334961,186.4513168334961,186.4888534545898,186.4888534545898,185.8491897583008,185.8491897583008,186.2363128662109,186.2363128662109,186.2363128662109,186.5160217285156,186.5160217285156,186.5160217285156,185.6260452270508,186.0068283081055,186.3925323486328,186.542854309082,186.542854309082,186.542854309082,185.7839660644531,185.7839660644531,185.7839660644531,186.1763076782227,186.1763076782227,186.5537567138672,186.5692138671875,186.5692138671875,186.5692138671875,185.9886016845703,185.9886016845703,186.3775100708008,186.3775100708008,186.595100402832,186.595100402832,186.595100402832,185.8293304443359,185.8293304443359,186.2136306762695,186.2136306762695,186.6001815795898,186.6001815795898,186.62060546875,186.62060546875,186.0550384521484,186.0550384521484,186.4458236694336,186.4458236694336,186.6457061767578,186.6457061767578,186.6457061767578,186.6457061767578,185.9132766723633,185.9132766723633,186.305534362793,186.6703491210938,186.6703491210938,186.6703491210938,186.6703491210938,186.1614379882812,186.554801940918,186.554801940918,186.6946563720703,186.6946563720703,186.6946563720703,186.0484619140625,186.4421615600586,186.4421615600586,186.7185516357422,186.7185516357422,186.7185516357422,185.9664154052734,186.3598327636719,186.7420043945312,186.7420043945312,186.7420043945312,186.7420043945312,186.7420043945312,186.7420043945312,186.2689971923828,186.2689971923828,186.6545715332031,186.7651977539062,186.7651977539062,186.2016296386719,186.2016296386719,186.2016296386719,186.5987396240234,186.5987396240234,186.5987396240234,186.7879104614258,186.7879104614258,186.7879104614258,186.1518173217773,186.1518173217773,186.5450210571289,186.5450210571289,186.8103485107422,186.8103485107422,186.8103485107422,186.0884170532227,186.0884170532227,186.4778671264648,186.8323364257812,186.8323364257812,186.8323364257812,186.8323364257812,186.8323364257812,186.8323364257812,186.8323364257812,186.8323364257812,186.8323364257812,186.8323364257812,186.8323364257812,186.8323364257812,186.8323364257812,186.8323364257812,186.8323364257812,186.8323364257812,186.8323364257812,186.8323364257812,186.8323364257812,186.8323364257812,186.8323364257812,186.8323364257812,186.1229705810547,186.1229705810547,186.1229705810547,186.5330505371094,186.5330505371094,186.9078674316406,186.9078674316406,187.280387878418,187.280387878418,187.6482543945312,188.0152969360352,188.0152969360352,188.3237686157227,188.3237686157227,188.633674621582,188.633674621582,188.9356689453125,188.9356689453125,189.2415084838867,189.2415084838867,189.5475616455078,189.5475616455078,189.5475616455078,189.5691986083984,189.5691986083984,186.5279922485352,186.5279922485352,186.8926773071289,186.8926773071289,187.2865982055664,187.2865982055664,187.2865982055664,187.6663055419922,187.6663055419922,188.0513153076172,188.0513153076172,188.4359436035156,188.8210067749023,189.2048950195312,189.2048950195312,189.5760116577148,189.5760116577148,189.6648254394531,189.6648254394531,189.6648254394531,186.6227722167969,186.6227722167969,186.6227722167969,186.9957656860352,187.3903045654297,187.3903045654297,187.3903045654297,187.769660949707,188.1492156982422,188.1492156982422,188.5298919677734,188.9081878662109,188.9081878662109,189.2831420898438,189.2831420898438,189.6533966064453,189.6533966064453,189.7588729858398,189.7588729858398,189.7588729858398,186.5222549438477,186.5222549438477,186.5222549438477,186.7556228637695,186.7556228637695,187.1297607421875,187.1297607421875,187.5093612670898,187.8725662231445,187.8725662231445,187.8725662231445,188.2478942871094,188.2478942871094,188.6146850585938,188.9836730957031,188.9836730957031,189.3532638549805,189.3532638549805,189.7256317138672,189.8514022827148,189.8514022827148,189.8514022827148,189.8514022827148,186.8227691650391,187.1991653442383,187.5901260375977,187.9649505615234,188.3351669311523,188.3351669311523,188.70751953125,188.70751953125,188.70751953125,189.0793533325195,189.0793533325195,189.0793533325195,189.455078125,189.455078125,189.8316345214844,189.8316345214844,189.942497253418,189.942497253418,189.942497253418,186.9840545654297,187.3608016967773,187.3608016967773,187.7454452514648,188.1145782470703,188.1145782470703,188.4847106933594,188.4847106933594,188.8587875366211,188.8587875366211,189.2303085327148,189.2303085327148,189.6054229736328,189.6054229736328,189.980827331543,189.980827331543,190.0320205688477,190.0320205688477,190.0320205688477,187.189094543457,187.189094543457,187.5723342895508,187.9603424072266,187.9603424072266,188.3342514038086,188.3342514038086,188.7089614868164,189.0816040039062,189.454719543457,189.454719543457,189.8331680297852,190.120246887207,190.120246887207,190.120246887207,190.120246887207,187.4569778442383,187.4569778442383,187.8468856811523,188.2283248901367,188.2283248901367,188.2283248901367,188.6117172241211,188.6117172241211,188.9907455444336,188.9907455444336,189.3662719726562,189.3662719726562,189.7465896606445,190.1171951293945,190.2069702148438,190.2069702148438,187.410041809082,187.7975921630859,187.7975921630859,188.1848678588867,188.5586318969727,188.5586318969727,188.934684753418,188.934684753418,189.3205184936523,189.7093734741211,190.090934753418,190.090934753418,190.2923355102539,190.2923355102539,187.4150848388672,187.4150848388672,187.8076019287109,187.8076019287109,188.1975936889648,188.5726928710938,188.5726928710938,188.9487457275391,189.3241958618164,189.700309753418,190.09033203125,190.09033203125,190.3762512207031,190.3762512207031,190.3762512207031,190.3762512207031,187.8457641601562,188.2324066162109,188.6040344238281,188.6040344238281,188.9714431762695,188.9714431762695,189.3413696289062,189.3413696289062,189.7227249145508,189.7227249145508,190.0966339111328,190.0966339111328,190.4589538574219,190.4589538574219,190.4589538574219,190.4589538574219,190.4589538574219,190.4589538574219,187.9047546386719,187.9047546386719,187.9047546386719,188.2953262329102,188.2953262329102,188.6655349731445,189.0329208374023,189.4024047851562,189.4024047851562,189.7765655517578,189.7765655517578,190.1556015014648,190.1556015014648,190.5231704711914,190.5231704711914,190.5401916503906,190.5401916503906,187.9840240478516,188.3750915527344,188.7504577636719,188.7504577636719,189.1277236938477,189.1277236938477,189.5004653930664,189.5004653930664,189.8729553222656,190.2500534057617,190.2500534057617,190.6201477050781,190.6201477050781,190.6201477050781,190.6201477050781,190.6201477050781,190.6201477050781,188.1299514770508,188.1299514770508,188.5186080932617,188.8890686035156,188.8890686035156,188.8890686035156,189.2582626342773,189.2582626342773,189.6244049072266,189.9926986694336,190.3644714355469,190.3644714355469,190.6987915039062,190.6987915039062,190.6987915039062,190.6987915039062,188.277702331543,188.6616897583008,189.029541015625,189.4056015014648,189.4056015014648,189.7768936157227,189.7768936157227,190.1527633666992,190.1527633666992,190.5269165039062,190.5269165039062,190.7762451171875,190.7762451171875,190.7762451171875,190.7762451171875,190.7762451171875,190.7762451171875,188.4895706176758,188.8610534667969,189.2393112182617,189.2393112182617,189.6162872314453,189.6162872314453,189.9878921508789,189.9878921508789,190.3634719848633,190.3634719848633,190.7367172241211,190.7367172241211,190.8523101806641,190.8523101806641,190.8523101806641,188.3579025268555,188.3579025268555,188.7430572509766,188.7430572509766,189.1147155761719,189.4772872924805,189.4772872924805,189.8445358276367,189.8445358276367,190.2162322998047,190.2162322998047,190.5901184082031,190.5901184082031,190.9272308349609,190.9272308349609,190.9272308349609,190.9272308349609,190.9272308349609,190.9272308349609,188.6279754638672,188.6279754638672,189.0014343261719,189.3747787475586,189.3747787475586,189.7424011230469,189.7424011230469,190.1119918823242,190.1119918823242,190.4861068725586,190.4861068725586,190.8595504760742,191.0009307861328,191.0009307861328,191.0009307861328,188.5607986450195,188.5607986450195,188.943229675293,189.3105621337891,189.6807632446289,190.0569305419922,190.0569305419922,190.0569305419922,190.432991027832,190.432991027832,190.8112335205078,191.0734405517578,191.0734405517578,191.0734405517578,191.0734405517578,191.0734405517578,191.0734405517578,188.9292373657227,188.9292373657227,189.2890548706055,189.6576614379883,189.6576614379883,189.6576614379883,190.0296859741211,190.0296859741211,190.4038314819336,190.7787780761719,190.7787780761719,190.7787780761719,191.1447525024414,191.1447525024414,191.1447525024414,191.1447525024414,188.917366027832,189.2797393798828,189.2797393798828,189.6524505615234,189.6524505615234,190.0222091674805,190.0222091674805,190.3950653076172,190.3950653076172,190.7695159912109,191.1399688720703,191.1399688720703,191.2149429321289,191.2149429321289,188.9612579345703,188.9612579345703,188.9612579345703,189.3352432250977,189.7077102661133,190.0778121948242,190.0778121948242,190.453483581543,190.8260879516602,191.1963653564453,191.284049987793,191.284049987793,191.284049987793,191.284049987793,189.0495071411133,189.0495071411133,189.4128189086914,189.7785034179688,189.7785034179688,190.1477813720703,190.5181350708008,190.5181350708008,190.8906173706055,190.8906173706055,191.2626800537109,191.3519515991211,191.3519515991211,191.3519515991211,189.1300735473633,189.1300735473633,189.1300735473633,189.5007247924805,189.8674163818359,189.8674163818359,190.2373046875,190.2373046875,190.6129989624023,190.6129989624023,190.9853134155273,191.3541030883789,191.4188003540039,191.4188003540039,191.4188003540039,191.4188003540039,191.4188003540039,191.4188003540039,191.4188003540039,191.4188003540039,191.4188003540039,191.4188003540039,191.4188003540039,191.4188003540039,191.4188003540039,191.4188003540039,191.4188003540039,191.4188003540039,191.4188003540039,191.4188003540039,189.2015609741211,189.5758514404297,189.5758514404297,189.9536666870117,189.9536666870117,190.3223495483398,190.3223495483398,190.3223495483398,190.6939849853516,190.6939849853516,191.07080078125,191.440185546875,191.4841690063477,191.4841690063477,191.4841690063477,189.3596954345703,189.7102279663086,190.0829391479492,190.0829391479492,190.4539108276367,190.4539108276367,190.8298034667969,190.8298034667969,191.1975860595703,191.1975860595703,191.5488815307617,191.5488815307617,191.5488815307617,191.5488815307617,191.5488815307617,191.5488815307617,189.5543441772461,189.5543441772461,189.9203720092773,189.9203720092773,190.2928619384766,190.2928619384766,190.6592712402344,190.6592712402344,191.0326843261719,191.0326843261719,191.4041519165039,191.4041519165039,191.6125717163086,191.6125717163086,189.4552459716797,189.8251495361328,189.8251495361328,190.1952285766602,190.5654144287109,190.9405822753906,191.3201751708984,191.3201751708984,191.6752014160156,191.6752014160156,191.6752014160156,191.6752014160156,189.780387878418,190.1567230224609,190.1567230224609,190.5345764160156,190.9085159301758,191.2856140136719,191.6554870605469,191.6554870605469,191.7368927001953,191.7368927001953,191.7368927001953,189.7312469482422,189.7312469482422,190.099723815918,190.099723815918,190.4735412597656,190.8488235473633,190.8488235473633,191.2262878417969,191.2262878417969,191.608642578125,191.608642578125,191.7975082397461,191.7975082397461,189.7421264648438,189.7421264648438,190.1067657470703,190.1067657470703,190.4761734008789,190.4761734008789,190.8492050170898,191.2222671508789,191.6004943847656,191.8571701049805,191.8571701049805,191.8571701049805,191.8571701049805,191.8571701049805,191.8571701049805,191.8571701049805,191.8571701049805,190.1346282958984,190.5034790039062,190.8815765380859,190.8815765380859,191.2600936889648,191.2600936889648,191.2600936889648,191.6361236572266,191.6361236572266,191.9158401489258,191.9158401489258,191.9158401489258,191.9158401489258,191.9158401489258,191.9158401489258,190.1975173950195,190.1975173950195,190.5688247680664,190.5688247680664,190.5688247680664,190.939826965332,190.939826965332,191.3189315795898,191.6926116943359,191.6926116943359,191.9735565185547,191.9735565185547,191.9735565185547,191.9735565185547,190.2967300415039,190.2967300415039,190.6697769165039,191.0491943359375,191.0491943359375,191.4266052246094,191.4266052246094,191.8072814941406,192.0304336547852,192.0304336547852,192.0304336547852,190.0783386230469,190.4409255981445,190.8163375854492,190.8163375854492,191.1873474121094,191.5588302612305,191.9348220825195,191.9348220825195,192.0862579345703,192.0862579345703,192.0862579345703,190.2180862426758,190.2180862426758,190.5879821777344,190.5879821777344,190.9685745239258,190.9685745239258,191.3349838256836,191.3349838256836,191.7073440551758,191.7073440551758,192.0799331665039,192.1412963867188,192.1412963867188,192.1412963867188,190.384521484375,190.384521484375,190.7569427490234,190.7569427490234,191.130615234375,191.5023040771484,191.5023040771484,191.8785858154297,191.8785858154297,192.1953887939453,192.1953887939453,192.1953887939453,192.1953887939453,190.5995330810547,190.9734039306641,190.9734039306641,191.3536605834961,191.7312850952148,191.7312850952148,192.1111373901367,192.2486114501953,192.2486114501953,192.2486114501953,192.2486114501953,190.4941787719727,190.4941787719727,190.8657760620117,191.2426986694336,191.2426986694336,191.6150741577148,191.6150741577148,191.993278503418,192.3010177612305,192.3010177612305,192.3010177612305,192.3010177612305,192.3010177612305,192.3010177612305,190.7447052001953,191.1252593994141,191.5056381225586,191.5056381225586,191.5056381225586,191.8771438598633,191.8771438598633,192.2502136230469,192.3525161743164,192.3525161743164,190.6703262329102,191.0436553955078,191.4300308227539,191.8005905151367,191.8005905151367,192.1780166625977,192.1780166625977,192.403205871582,192.403205871582,192.403205871582,192.403205871582,192.403205871582,192.403205871582,191.0053634643555,191.0053634643555,191.3826522827148,191.3826522827148,191.7589263916016,192.1333236694336,192.4530639648438,192.4530639648438,192.4530639648438,192.4530639648438,192.4530639648438,192.4530639648438,192.4530639648438,192.4530639648438,190.9854049682617,190.9854049682617,191.3709259033203,191.3709259033203,191.3709259033203,191.7484130859375,191.7484130859375,192.1205368041992,192.1205368041992,192.4912033081055,192.4912033081055,192.5020980834961,192.5020980834961,190.9863128662109,190.9863128662109,191.3627243041992,191.3627243041992,191.7467803955078,192.1219482421875,192.5004501342773,192.5004501342773,192.5503768920898,192.5503768920898,191.0320205688477,191.0320205688477,191.4091796875,191.7932357788086,192.1708602905273,192.1708602905273,192.5433959960938,192.5979156494141,192.5979156494141,192.5979156494141,192.5979156494141,192.5979156494141,192.5979156494141,192.5979156494141,192.5979156494141,192.5979156494141,192.5979156494141,192.5979156494141,192.5979156494141,192.5979156494141,192.5979156494141,192.5979156494141,190.9625701904297,190.9625701904297,190.9625701904297,191.1598587036133,191.5376052856445,191.5376052856445,191.9141616821289,192.2739486694336,192.2739486694336,192.6430892944336,192.6445159912109,192.6445159912109,192.6445159912109,191.2134246826172,191.5836715698242,191.5836715698242,191.959846496582,191.959846496582,192.3334350585938,192.3334350585938,192.6905288696289,192.6905288696289,192.6905288696289,192.6905288696289,192.6905288696289,192.6905288696289,191.2825927734375,191.2825927734375,191.6587905883789,191.6587905883789,192.0381927490234,192.0381927490234,192.4169235229492,192.7357788085938,192.7357788085938,192.7357788085938,192.7357788085938,191.2680892944336,191.2680892944336,191.6300735473633,191.6300735473633,192.0150299072266,192.3880920410156,192.7505187988281,192.7803115844727,192.7803115844727,192.7803115844727,192.7803115844727,191.3603057861328,191.3603057861328,191.3603057861328,191.7123413085938,191.7123413085938,192.0957107543945,192.0957107543945,192.0957107543945,192.4587783813477,192.4587783813477,192.824104309082,192.824104309082,192.824104309082,192.824104309082,192.824104309082,192.824104309082,191.463493347168,191.463493347168,191.7944183349609,191.7944183349609,192.1504364013672,192.1504364013672,192.5200576782227,192.8672027587891,192.8672027587891,192.8672027587891,192.8672027587891,191.5738143920898,191.5738143920898,191.9470443725586,191.9470443725586,192.3231430053711,192.6984329223633,192.6984329223633,192.9095840454102,192.9095840454102,192.9095840454102,192.9095840454102,191.7339019775391,191.7339019775391,192.1176605224609,192.4804153442383,192.4804153442383,192.8486938476562,192.9513626098633,192.9513626098633,192.9513626098633,191.587646484375,191.587646484375,191.959358215332,191.959358215332,192.3423690795898,192.3423690795898,192.7159576416016,192.9923706054688,192.9923706054688,192.9923706054688,192.9923706054688,192.9923706054688,192.9923706054688,191.8468856811523,191.8468856811523,192.2294540405273,192.6085891723633,192.9741744995117,193.0327529907227,193.0327529907227,193.0327529907227,193.0327529907227,193.0327529907227,193.0327529907227,191.9883422851562,191.9883422851562,192.3617553710938,192.3617553710938,192.7071838378906,193.0607376098633,193.0607376098633,193.0724716186523,193.0724716186523,193.0724716186523,191.714111328125,192.0474014282227,192.0474014282227,192.4005126953125,192.4005126953125,192.7707290649414,192.7707290649414,192.7707290649414,193.1115417480469,193.1115417480469,193.1115417480469,193.1115417480469,193.1115417480469,193.1115417480469,191.9426498413086,191.9426498413086,192.3123092651367,192.6927719116211,192.6927719116211,192.6927719116211,193.0576248168945,193.1500396728516,193.1500396728516,193.1500396728516,191.9011383056641,191.9011383056641,192.2692184448242,192.2692184448242,192.6475677490234,192.6475677490234,193.0145034790039,193.0145034790039,193.1878509521484,193.1878509521484,193.1878509521484,193.1878509521484,193.1878509521484,193.1878509521484,192.1866683959961,192.1866683959961,192.577278137207,192.577278137207,192.9392852783203,193.2250366210938,193.2250366210938,193.2250366210938,193.2250366210938,193.2250366210938,193.2250366210938,193.2250366210938,193.2250366210938,193.2250366210938,193.2250366210938,192.0117874145508,192.3226852416992,192.3226852416992,192.6578369140625,192.6578369140625,193.0294952392578,193.0294952392578,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,193.2616500854492,192.0009078979492,192.0009078979492,192.0009078979492,192.3634948730469,192.3634948730469,192.7491912841797,193.0799560546875,193.0799560546875,193.4143524169922,193.4143524169922,193.7786636352539,193.7786636352539,193.7786636352539,194.1462936401367,194.1462936401367,194.1462936401367,194.5156555175781,194.5156555175781,194.8355712890625,194.8355712890625,195.1416320800781,195.1416320800781,195.4469146728516,195.4469146728516,195.4469146728516,195.7511901855469,195.7511901855469,195.7511901855469,196.0605926513672,196.0605926513672,196.3662719726562,196.3662719726562,196.6747207641602,196.6747207641602,196.984977722168,196.984977722168,196.984977722168,197.291862487793,197.291862487793,197.470832824707,197.470832824707,197.470832824707,197.470832824707,192.5235977172852,192.5235977172852,192.9193649291992,193.2527694702148,193.6244277954102,193.6244277954102,193.9978179931641,193.9978179931641,194.3776779174805,194.3776779174805,194.7494049072266,195.1266479492188,195.1266479492188,195.5139465332031,195.5139465332031,195.8983535766602,196.2833480834961,196.2833480834961,196.6600646972656,197.0333480834961,197.0333480834961,197.4139633178711,197.4139633178711,197.6203765869141,197.6203765869141,197.6203765869141,197.6203765869141,192.742073059082,193.1293716430664,193.1293716430664,193.4691390991211,193.8152542114258,194.1988983154297,194.1988983154297,194.1988983154297,194.5766754150391,194.9244689941406,195.2770233154297,195.2770233154297,195.65234375,195.65234375,195.9843444824219,196.351806640625,196.351806640625,196.7341537475586,196.7341537475586,197.0838928222656,197.0838928222656,197.4574661254883,197.4574661254883,197.7676544189453,197.7676544189453,197.7676544189453,197.7676544189453,192.7785949707031,192.7785949707031,193.1656341552734,193.5313873291016,193.5313873291016,193.8899383544922,194.2517013549805,194.2517013549805,194.6277465820312,194.6277465820312,194.9871215820312,195.3450927734375,195.3450927734375,195.7220153808594,196.0835189819336,196.0835189819336,196.4606094360352,196.4606094360352,196.8250961303711,196.8250961303711,197.1839752197266,197.558219909668,197.558219909668,197.893424987793,197.9124984741211,197.9124984741211,197.9124984741211,192.9340744018555,192.9340744018555,193.3389205932617,193.3389205932617,193.7015991210938,193.7015991210938,194.0660018920898,194.444221496582,194.444221496582,194.799186706543,194.799186706543,195.1590881347656,195.1590881347656,195.5318603515625,195.5318603515625,195.8893890380859,196.2627258300781,196.6219024658203,196.6219024658203,196.9829864501953,197.3556976318359,197.3556976318359,197.7119140625,197.7119140625,198.0549850463867,198.0549850463867,198.0549850463867,198.0549850463867,198.0549850463867,198.0549850463867,198.0549850463867,198.0549850463867,198.0549850463867,193.5414657592773,193.5414657592773,193.5414657592773,193.8980102539062,193.8980102539062,194.2665328979492,194.2665328979492,194.6381912231445,194.6381912231445,195.009651184082,195.3809967041016,195.3809967041016,195.7466049194336,196.1136245727539,196.1136245727539,196.4812164306641,196.4812164306641,196.4812164306641,196.8502197265625,196.8502197265625,197.2194213867188,197.2194213867188,197.5868835449219,197.5868835449219,197.9513320922852,197.9513320922852,198.195198059082,198.195198059082,198.195198059082,198.195198059082,193.4848556518555,193.8719024658203,193.8719024658203,194.2340698242188,194.2340698242188,194.610481262207,194.610481262207,194.9858093261719,195.354133605957,195.354133605957,195.7242126464844,196.0895767211914,196.0895767211914,196.0895767211914,196.4639129638672,196.8427658081055,196.8427658081055,197.2134780883789,197.5871353149414,197.9648361206055,198.3298568725586,198.3298568725586,198.3330917358398,198.3330917358398,198.3330917358398,198.3330917358398,198.3330917358398,198.3330917358398,198.3330917358398,198.3330917358398,193.7836227416992,193.7836227416992,194.1552810668945,194.1552810668945,194.1552810668945,194.5359344482422,194.9000473022461,194.9000473022461,195.267204284668,195.6368789672852,196.0035705566406,196.0035705566406,196.0035705566406,196.3612365722656,196.7249984741211,197.0995864868164,197.0995864868164,197.4677810668945,197.4677810668945,197.8467483520508,197.8467483520508,198.2119293212891,198.2119293212891,198.4686508178711,198.4686508178711,198.4686508178711,198.4686508178711,198.4686508178711,198.4686508178711,193.9174499511719,194.2969512939453,194.2969512939453,194.6590118408203,195.0204238891602,195.3996505737305,195.3996505737305,195.3996505737305,195.7656707763672,195.7656707763672,196.1269912719727,196.1269912719727,196.4995498657227,196.4995498657227,196.4995498657227,196.8753814697266,197.2456512451172,197.2456512451172,197.6190872192383,197.6190872192383,197.6190872192383,197.9968719482422,197.9968719482422,197.9968719482422,198.369758605957,198.369758605957,198.6021270751953,198.6021270751953,198.6021270751953,198.6021270751953,198.6021270751953,198.6021270751953,194.1706314086914,194.5324630737305,194.5324630737305,194.9234237670898,195.2918167114258,195.6645126342773,195.6645126342773,196.0287704467773,196.0287704467773,196.3959732055664,196.7740859985352,197.1405792236328,197.1405792236328,197.5219421386719,197.5219421386719,197.9070434570312,198.2819366455078,198.6524963378906,198.6524963378906,198.7335357666016,198.7335357666016,198.7335357666016,198.7335357666016,198.7335357666016,198.7335357666016,194.5131301879883,194.5131301879883,194.8821182250977,194.8821182250977,195.2434310913086,195.2434310913086,195.6056365966797,195.6056365966797,195.9723587036133,195.9723587036133,196.3398513793945,196.7022094726562,196.7022094726562,197.0857315063477,197.4565124511719,197.4565124511719,197.8343124389648,198.2093200683594,198.2093200683594,198.5817337036133,198.8627319335938,198.8627319335938,198.8627319335938,198.8627319335938,194.5441131591797,194.5441131591797,194.891731262207,194.891731262207,195.26123046875,195.26123046875,195.629768371582,195.629768371582,195.992790222168,195.992790222168,196.3496932983398,196.3496932983398,196.7185668945312,196.7185668945312,196.7185668945312,197.0867309570312,197.0867309570312,197.4670104980469,197.4670104980469,197.8349227905273,197.8349227905273,198.2025451660156,198.2025451660156,198.58544921875,198.58544921875,198.9395446777344,198.9899215698242,198.9899215698242,198.9899215698242,198.9899215698242,198.9899215698242,198.9899215698242,194.9600219726562,195.3466644287109,195.3466644287109,195.7174453735352,195.7174453735352,196.0974731445312,196.0974731445312,196.4621124267578,196.4621124267578,196.8303146362305,197.2005004882812,197.2005004882812,197.5753860473633,197.9531173706055,198.3333740234375,198.3333740234375,198.7143707275391,198.7143707275391,199.0750045776367,199.1150207519531,199.1150207519531,199.1150207519531,199.1150207519531,195.1654968261719,195.1654968261719,195.5527496337891,195.5527496337891,195.5527496337891,195.9174194335938,195.9174194335938,196.2821960449219,196.2821960449219,196.6477661132812,197.0188980102539,197.0188980102539,197.3879852294922,197.7637481689453,197.7637481689453,197.7637481689453,198.1401443481445,198.1401443481445,198.5191802978516,198.5191802978516,198.5191802978516,198.8926315307617,199.2381286621094,199.2381286621094,199.2381286621094,199.2381286621094,199.2381286621094,199.2381286621094,195.0457305908203,195.0457305908203,195.4280776977539,195.4280776977539,195.8043746948242,196.1658401489258,196.1658401489258,196.5269241333008,196.5269241333008,196.8944244384766,197.2653350830078,197.2653350830078,197.6387252807617,197.6387252807617,198.0142440795898,198.3903427124023,198.3903427124023,198.7607421875,198.7607421875,199.1362991333008,199.1362991333008,199.3592681884766,199.3592681884766,199.3592681884766,199.3592681884766,195.3396606445312,195.3396606445312,195.7153549194336,195.7153549194336,196.0826034545898,196.0826034545898,196.4395904541016,196.8045806884766,196.8045806884766,197.1740646362305,197.1740646362305,197.5405197143555,197.5405197143555,197.9182739257812,197.9182739257812,198.2955551147461,198.2955551147461,198.6738586425781,198.6738586425781,199.0556945800781,199.0556945800781,199.4257736206055,199.4783172607422,199.4783172607422,199.4783172607422,199.4783172607422,195.7158203125,195.7158203125,196.0908050537109,196.0908050537109,196.4477005004883,196.4477005004883,196.4477005004883,196.8067779541016,197.1704788208008,197.1704788208008,197.5330657958984,197.9047012329102,197.9047012329102,198.2795104980469,198.2795104980469,198.6560592651367,198.6560592651367,199.0346145629883,199.0346145629883,199.4084854125977,199.5955963134766,199.5955963134766,199.5955963134766,199.5955963134766,199.5955963134766,199.5955963134766,195.7544784545898,195.7544784545898,196.1257476806641,196.1257476806641,196.5016403198242,196.5016403198242,196.5016403198242,196.8683624267578,196.8683624267578,197.2414245605469,197.2414245605469,197.6171188354492,197.991096496582,197.991096496582,198.3690948486328,198.3690948486328,198.7499923706055,198.7499923706055,199.1341857910156,199.5119094848633,199.7109222412109,199.7109222412109,199.7109222412109,199.7109222412109,199.7109222412109,199.7109222412109,195.8805313110352,196.2513809204102,196.6049652099609,196.9536437988281,197.3139953613281,197.3139953613281,197.681266784668,198.0508193969727,198.0508193969727,198.4217987060547,198.4217987060547,198.4217987060547,198.7966156005859,198.7966156005859,198.7966156005859,199.1749420166016,199.1749420166016,199.5513534545898,199.5513534545898,199.8243713378906,199.8243713378906,199.8243713378906,199.8243713378906,199.8243713378906,199.8243713378906,196.0156784057617,196.3876190185547,196.3876190185547,196.7334976196289,196.7334976196289,197.0791931152344,197.0791931152344,197.4433517456055,197.4433517456055,197.8137130737305,197.8137130737305,198.1899337768555,198.1899337768555,198.5672302246094,198.5672302246094,198.5672302246094,198.9487686157227,199.3319320678711,199.7098617553711,199.9359741210938,199.9359741210938,199.9359741210938,199.9359741210938,199.9359741210938,199.9359741210938,196.2416687011719,196.2416687011719,196.615837097168,196.615837097168,196.9681930541992,197.3259353637695,197.3259353637695,197.6921920776367,197.6921920776367,198.0656204223633,198.4420166015625,198.8222732543945,199.2045669555664,199.2045669555664,199.5888824462891,199.5888824462891,199.5888824462891,199.9614181518555,199.9614181518555,200.0458221435547,200.0458221435547,200.0458221435547,200.0458221435547,200.0458221435547,200.0458221435547,196.5787353515625,196.9417724609375,196.9417724609375,197.296257019043,197.6601409912109,197.6601409912109,198.0346298217773,198.0346298217773,198.4096527099609,198.7873840332031,198.7873840332031,199.1682357788086,199.550422668457,199.9297485351562,199.9297485351562,200.1538467407227,200.1538467407227,200.1538467407227,200.1538467407227,200.1538467407227,200.1538467407227,200.1538467407227,200.1538467407227,196.5584030151367,196.5584030151367,196.9247894287109,196.9247894287109,197.279426574707,197.279426574707,197.6391525268555,198.0081787109375,198.383171081543,198.383171081543,198.7564086914062,199.1325225830078,199.1325225830078,199.5103225708008,199.8902359008789,200.2550430297852,200.2601318359375,200.2601318359375,196.6153411865234,196.6153411865234,196.9852066040039,196.9852066040039,197.3292083740234,197.6780014038086,197.6780014038086,198.0457992553711,198.0457992553711,198.4159164428711,198.4159164428711,198.791748046875,198.791748046875,199.1710052490234,199.1710052490234,199.5513916015625,199.5513916015625,199.5513916015625,199.9332275390625,199.9332275390625,199.9332275390625,200.3049392700195,200.3647308349609,200.3647308349609,200.3647308349609,200.3647308349609,200.3647308349609,200.3647308349609,197.0914154052734,197.4465408325195,197.4465408325195,197.8071746826172,197.8071746826172,198.1740570068359,198.1740570068359,198.5494155883789,198.5494155883789,198.9295272827148,199.3053283691406,199.6855850219727,199.6855850219727,200.0693664550781,200.0693664550781,200.4399795532227,200.4399795532227,200.4399795532227,200.4675979614258,200.4675979614258,200.4675979614258,200.4675979614258,197.2865447998047,197.6383590698242,197.6383590698242,197.9957427978516,197.9957427978516,198.3616333007812,198.3616333007812,198.3616333007812,198.7334976196289,198.7334976196289,199.1045989990234,199.1045989990234,199.1045989990234,199.4783935546875,199.4783935546875,199.8557434082031,200.2354736328125,200.5688247680664,200.5688247680664,200.5688247680664,200.5688247680664,197.1324310302734,197.4988784790039,197.8559722900391,198.2205123901367,198.5949020385742,198.9718475341797,198.9718475341797,198.9718475341797,199.3490982055664,199.7268981933594,200.1075286865234,200.1075286865234,200.1075286865234,200.4851531982422,200.4851531982422,200.6685028076172,200.6685028076172,200.6685028076172,200.6685028076172,197.4415054321289,197.4415054321289,197.4415054321289,197.8030166625977,197.8030166625977,198.1641006469727,198.1641006469727,198.5238723754883,198.5238723754883,198.8867263793945,198.8867263793945,198.8867263793945,199.2518615722656,199.6323623657227,200.0007934570312,200.0007934570312,200.3723297119141,200.3723297119141,200.7237701416016,200.7237701416016,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,200.7664337158203,197.3932113647461,197.3932113647461,197.3932113647461,197.3932113647461,197.3932113647461,197.3932113647461,197.3932113647461,197.3932113647461,197.3932113647461,197.7971801757812,197.7971801757812,198.1873779296875,198.1873779296875,198.5360488891602,198.5360488891602,198.9044189453125,198.9044189453125,199.2692642211914,199.6193008422852,199.6193008422852,199.9706192016602,199.9706192016602,200.2914047241211,200.6262054443359,200.6262054443359,200.8627243041992,200.8627243041992,200.8627243041992,200.8627243041992,200.8627243041992,200.8627243041992,197.662727355957,197.662727355957,198.0731658935547,198.0731658935547,198.4636306762695,198.4636306762695,198.4636306762695,198.833984375,199.1955795288086,199.5629806518555,199.5629806518555,199.9074172973633,199.9074172973633,200.2469635009766,200.2469635009766,200.6017990112305,200.6017990112305,200.6017990112305,200.9576568603516,200.9576568603516,200.9576568603516,200.9576568603516,200.9576568603516,200.9576568603516,200.9576568603516,200.9576568603516,200.9576568603516,198.0652313232422,198.4624710083008,198.4624710083008,198.4624710083008,198.8311538696289,198.8311538696289,199.1994400024414,199.1994400024414,199.5430450439453,199.5430450439453,199.8788375854492,200.1950912475586,200.5421295166016,200.9126434326172,200.9126434326172,200.9126434326172,201.0509490966797,201.0509490966797,201.0509490966797,201.0509490966797,201.0509490966797,201.0509490966797,198.0568008422852,198.0568008422852,198.4614715576172,198.4614715576172,198.4614715576172,198.8475723266602,199.2175750732422,199.2175750732422,199.5729522705078,199.5729522705078,199.9050903320312,200.2214736938477,200.2214736938477,200.5934829711914,200.9714813232422,200.9714813232422,200.9714813232422,201.1428985595703,201.1428985595703,201.1428985595703,201.1428985595703,198.1651916503906,198.1651916503906,198.5735321044922,198.5735321044922,198.9567031860352,199.3187561035156,199.3187561035156,199.662353515625,199.662353515625,199.9868316650391,199.9868316650391,199.9868316650391,200.3302001953125,200.3302001953125,200.703857421875,201.0792007446289,201.2332153320312,201.2332153320312,201.2332153320312,201.2332153320312,201.2332153320312,201.2332153320312,198.3373794555664,198.7463912963867,199.1309661865234,199.4812393188477,199.4812393188477,199.8146667480469,199.8146667480469,200.1408462524414,200.1408462524414,200.5186996459961,200.5186996459961,200.8934020996094,201.2718963623047,201.3221588134766,201.3221588134766,201.3221588134766,201.3221588134766,201.3221588134766,201.3221588134766,201.3221588134766,201.3221588134766,198.6227645874023,199.0210952758789,199.0210952758789,199.3828201293945,199.7258071899414,199.7258071899414,200.0459442138672,200.4198150634766,200.7986221313477,201.1805725097656,201.1805725097656,201.4096755981445,201.4096755981445,201.4096755981445,201.4096755981445,201.4096755981445,201.4096755981445,198.5654373168945,198.5654373168945,198.5654373168945,198.9723587036133,198.9723587036133,199.344596862793,199.344596862793,199.6855239868164,199.6855239868164,200.0067901611328,200.0067901611328,200.3794860839844,200.7550048828125,200.7550048828125,201.133186340332,201.133186340332,201.133186340332,201.4957046508789,201.4957046508789,201.4957046508789,201.4957046508789,201.4957046508789,201.4957046508789,198.5465621948242,198.5465621948242,198.9721069335938,198.9721069335938,199.3523254394531,199.6950988769531,200.0123443603516,200.0123443603516,200.3874588012695,200.761116027832,201.1390609741211,201.1390609741211,201.1390609741211,201.5184631347656,201.5184631347656,201.5803680419922,201.5803680419922,201.5803680419922,201.5803680419922,201.5803680419922,201.5803680419922,198.9975280761719,206.9618148803711,206.9618148803711,206.9618148803711,206.9618148803711,206.9618148803711,206.9618148803711,206.9618148803711,206.9618148803711,206.9618148803711,206.9618148803711,206.9618148803711,206.9618148803711,214.5912094116211,214.5912170410156,214.5912170410156,214.5912170410156,214.5912170410156,214.5912170410156,214.5912170410156,214.5912170410156,214.5912170410156,214.5912170410156,214.5912170410156,214.5912170410156,214.5912170410156,214.5912170410156,214.5912170410156,229.8500061035156,229.8500061035156,229.8500061035156,229.8500061035156,229.8500061035156,229.8500061035156,229.8500061035156,229.8500061035156,229.8500061035156,229.8500061035156],"meminc":[0,0,0,0,15.25894165039062,0,0,0,30.07318115234375,0,0,0,0,0,0,0,4.57763671875e-05,0,-0.000152587890625,0,0,0,0,0,0,0,15.37673187255859,0,0.4062423706054688,0,0.3851699829101562,0,0.364471435546875,0,0.3734512329101562,0,0.1347503662109375,0,0,-1.413330078125,0.36492919921875,0,0.3770599365234375,0,0.3813095092773438,0,0.3194122314453125,0,-1.57135009765625,0,0.4055252075195312,0,0.3639373779296875,0.3514785766601562,0.3681488037109375,0,0.12957763671875,0,-1.359512329101562,0,0.3867874145507812,0,0.3686599731445312,0,0.3548202514648438,0,0.2958221435546875,0,0,-1.519294738769531,0,0.3965988159179688,0,0.3762130737304688,0,0,0.37713623046875,0.3728790283203125,0,0.0422515869140625,0,0,-1.2216796875,0,0.3823165893554688,0,0.3719940185546875,0.3742904663085938,0,0.1381378173828125,0,0,0,-1.303810119628906,0,0.3918380737304688,0.37835693359375,0,0,0.376434326171875,0,0.2015533447265625,0,0,-1.338851928710938,0,0.3886642456054688,0,0.384429931640625,0,0.3792266845703125,0,0.2300796508789062,0,-1.345199584960938,0,0.3899307250976562,0,0,0.3839874267578125,0.3753433227539062,0.2389450073242188,0,0,-1.328460693359375,0,0.3907470703125,0,0.378631591796875,0.3719482421875,0.2293014526367188,0,0,0,0,0,0,0,0,-1.374618530273438,0.397186279296875,0,0.3746414184570312,0,0.3676071166992188,0,0.2767181396484375,0,0,-1.339935302734375,0,0.3949737548828125,0,0.3710098266601562,0.37738037109375,0.2374420166015625,0,0,-1.287681579589844,0,0.396728515625,0.378570556640625,0.3792037963867188,0.173370361328125,0,-1.181144714355469,0,0.3881912231445312,0,0.3786239624023438,0,0.3820266723632812,0,0.0719451904296875,0,0,-1.063262939453125,0,0.3856353759765625,0.378326416015625,0,0.3381576538085938,0,0,-1.310676574707031,0.3935775756835938,0,0.38616943359375,0,0.3801422119140625,0,0.1891250610351562,0,0,-1.126724243164062,0.38671875,0,0,0.3809814453125,0,0.3825149536132812,0,0,0.014190673828125,0,0,-0.9355239868164062,0.3850479125976562,0.379608154296875,0,0.2079544067382812,0,0,-1.107254028320312,0,0,0.3843231201171875,0.3828659057617188,0,0.3765411376953125,0,0,0,0,0,-0.8777618408203125,0.3851165771484375,0,0.3850479125976562,0,0.1434860229492188,0,0,-1.000289916992188,0.3877792358398438,0,0.3851242065429688,0,0.2627029418945312,0,0,-1.1099853515625,0.3811798095703125,0.3773956298828125,0.3785018920898438,0.00766754150390625,0,0,-0.8666915893554688,0,0.3878707885742188,0.3791351318359375,0,0.1338424682617188,0,-0.9732818603515625,0,0.3816986083984375,0,0,0.3737945556640625,0.2514114379882812,0,0,-1.061088562011719,0.3784332275390625,0,0.389801025390625,0,0.3259811401367188,0,0,-1.09808349609375,0,0.379913330078125,0,0.3849945068359375,0,0,0.3656845092773438,0,0,0,0,0,-0.7614898681640625,0,0.3836441040039062,0.3796844482421875,0,0,0.03017425537109375,0,0,-0.7688217163085938,0.382781982421875,0.3813095092773438,0.0362548828125,0,-0.786407470703125,0,0.387115478515625,0.3748092651367188,0,0.05541229248046875,0,0,-0.8004684448242188,0,0.3871688842773438,0.3831863403320312,0,0.0606536865234375,0,-0.7730331420898438,0.389923095703125,0,0.3765792846679688,0,0.0364990234375,0,0,0,0,0,0,0,0,0,0,0,-0.7418899536132812,0,0.3866958618164062,0,0.381805419921875,0.00269317626953125,0,0,-0.7027969360351562,0,0.3772048950195312,0,0.3546524047851562,0,0,-0.9895858764648438,0,0.3727645874023438,0.3837356567382812,0,0.2616424560546875,0,0,-0.8924407958984375,0,0.3856430053710938,0.3816604614257812,0,0.1532669067382812,0,-0.7779693603515625,0.3843994140625,0.3837814331054688,0,0.03753662109375,0,-0.6396636962890625,0,0.3871231079101562,0,0,0.2797088623046875,0,0,-0.8899765014648438,0.3807830810546875,0.3857040405273438,0.1503219604492188,0,0,-0.7588882446289062,0,0,0.3923416137695312,0,0.3774490356445312,0.0154571533203125,0,0,-0.5806121826171875,0,0.3889083862304688,0,0.21759033203125,0,0,-0.7657699584960938,0,0.3843002319335938,0,0.3865509033203125,0,0.02042388916015625,0,-0.5655670166015625,0,0.3907852172851562,0,0.1998825073242188,0,0,0,-0.7324295043945312,0,0.3922576904296875,0.3648147583007812,0,0,0,-0.5089111328125,0.3933639526367188,0,0.1398544311523438,0,0,-0.6461944580078125,0.3936996459960938,0,0.2763900756835938,0,0,-0.75213623046875,0.3934173583984375,0.382171630859375,0,0,0,0,0,-0.4730072021484375,0,0.3855743408203125,0.110626220703125,0,-0.563568115234375,0,0,0.3971099853515625,0,0,0.1891708374023438,0,0,-0.6360931396484375,0,0.3932037353515625,0,0.2653274536132812,0,0,-0.7219314575195312,0,0.3894500732421875,0.3544692993164062,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-0.7093658447265625,0,0,0.4100799560546875,0,0.37481689453125,0,0.3725204467773438,0,0.3678665161132812,0.3670425415039062,0,0.3084716796875,0,0.309906005859375,0,0.3019943237304688,0,0.3058395385742188,0,0.3060531616210938,0,0,0.021636962890625,0,-3.041206359863281,0,0.36468505859375,0,0.3939208984375,0,0,0.3797073364257812,0,0.385009765625,0,0.3846282958984375,0.3850631713867188,0.3838882446289062,0,0.3711166381835938,0,0.08881378173828125,0,0,-3.04205322265625,0,0,0.3729934692382812,0.3945388793945312,0,0,0.3793563842773438,0.3795547485351562,0,0.38067626953125,0.3782958984375,0,0.3749542236328125,0,0.3702545166015625,0,0.1054763793945312,0,0,-3.236618041992188,0,0,0.233367919921875,0,0.3741378784179688,0,0.3796005249023438,0.3632049560546875,0,0,0.3753280639648438,0,0.366790771484375,0.368988037109375,0,0.3695907592773438,0,0.3723678588867188,0.1257705688476562,0,0,0,-3.028633117675781,0.3763961791992188,0.390960693359375,0.3748245239257812,0.3702163696289062,0,0.3723526000976562,0,0,0.3718338012695312,0,0,0.3757247924804688,0,0.376556396484375,0,0.1108627319335938,0,0,-2.958442687988281,0.3767471313476562,0,0.3846435546875,0.3691329956054688,0,0.3701324462890625,0,0.3740768432617188,0,0.37152099609375,0,0.3751144409179688,0,0.3754043579101562,0,0.0511932373046875,0,0,-2.842926025390625,0,0.38323974609375,0.3880081176757812,0,0.3739089965820312,0,0.3747100830078125,0.3726425170898438,0.3731155395507812,0,0.378448486328125,0.287078857421875,0,0,0,-2.66326904296875,0,0.3899078369140625,0.381439208984375,0,0,0.383392333984375,0,0.3790283203125,0,0.3755264282226562,0,0.3803176879882812,0.37060546875,0.08977508544921875,0,-2.796928405761719,0.3875503540039062,0,0.3872756958007812,0.3737640380859375,0,0.3760528564453125,0,0.385833740234375,0.38885498046875,0.381561279296875,0,0.2014007568359375,0,-2.877250671386719,0,0.39251708984375,0,0.3899917602539062,0.3750991821289062,0,0.3760528564453125,0.3754501342773438,0.3761138916015625,0.3900222778320312,0,0.285919189453125,0,0,0,-2.530487060546875,0.3866424560546875,0.3716278076171875,0,0.3674087524414062,0,0.3699264526367188,0,0.3813552856445312,0,0.3739089965820312,0,0.3623199462890625,0,0,0,0,0,-2.55419921875,0,0,0.3905715942382812,0,0.370208740234375,0.3673858642578125,0.3694839477539062,0,0.3741607666015625,0,0.3790359497070312,0,0.3675689697265625,0,0.01702117919921875,0,-2.556167602539062,0.3910675048828125,0.3753662109375,0,0.3772659301757812,0,0.37274169921875,0,0.3724899291992188,0.3770980834960938,0,0.3700942993164062,0,0,0,0,0,-2.490196228027344,0,0.3886566162109375,0.3704605102539062,0,0,0.3691940307617188,0,0.3661422729492188,0.3682937622070312,0.3717727661132812,0,0.334320068359375,0,0,0,-2.421089172363281,0.3839874267578125,0.3678512573242188,0.3760604858398438,0,0.3712921142578125,0,0.3758697509765625,0,0.3741531372070312,0,0.24932861328125,0,0,0,0,0,-2.286674499511719,0.3714828491210938,0.3782577514648438,0,0.3769760131835938,0,0.3716049194335938,0,0.375579833984375,0,0.3732452392578125,0,0.1155929565429688,0,0,-2.494407653808594,0,0.3851547241210938,0,0.3716583251953125,0.3625717163085938,0,0.36724853515625,0,0.3716964721679688,0,0.3738861083984375,0,0.3371124267578125,0,0,0,0,0,-2.29925537109375,0,0.3734588623046875,0.3733444213867188,0,0.3676223754882812,0,0.3695907592773438,0,0.374114990234375,0,0.373443603515625,0.1413803100585938,0,0,-2.440132141113281,0,0.3824310302734375,0.3673324584960938,0.3702011108398438,0.3761672973632812,0,0,0.3760604858398438,0,0.3782424926757812,0.26220703125,0,0,0,0,0,-2.144203186035156,0,0.3598175048828125,0.3686065673828125,0,0,0.3720245361328125,0,0.3741455078125,0.3749465942382812,0,0,0.3659744262695312,0,0,0,-2.227386474609375,0.3623733520507812,0,0.372711181640625,0,0.3697586059570312,0,0.3728561401367188,0,0.37445068359375,0.370452880859375,0,0.07497406005859375,0,-2.253684997558594,0,0,0.3739852905273438,0.372467041015625,0.3701019287109375,0,0.37567138671875,0.3726043701171875,0.3702774047851562,0.08768463134765625,0,0,0,-2.234542846679688,0,0.363311767578125,0.3656845092773438,0,0.3692779541015625,0.3703536987304688,0,0.3724822998046875,0,0.3720626831054688,0.08927154541015625,0,0,-2.221878051757812,0,0,0.3706512451171875,0.3666915893554688,0,0.3698883056640625,0,0.3756942749023438,0,0.372314453125,0.3687896728515625,0.064697265625,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2.217239379882812,0.3742904663085938,0,0.3778152465820312,0,0.368682861328125,0,0,0.3716354370117188,0,0.3768157958984375,0.369384765625,0.04398345947265625,0,0,-2.124473571777344,0.3505325317382812,0.372711181640625,0,0.3709716796875,0,0.3758926391601562,0,0.3677825927734375,0,0.3512954711914062,0,0,0,0,0,-1.994537353515625,0,0.36602783203125,0,0.3724899291992188,0,0.3664093017578125,0,0.3734130859375,0,0.3714675903320312,0,0.2084197998046875,0,-2.157325744628906,0.369903564453125,0,0.3700790405273438,0.3701858520507812,0.3751678466796875,0.3795928955078125,0,0.3550262451171875,0,0,0,-1.894813537597656,0.3763351440429688,0,0.3778533935546875,0.3739395141601562,0.3770980834960938,0.369873046875,0,0.0814056396484375,0,0,-2.005645751953125,0,0.3684768676757812,0,0.3738174438476562,0.3752822875976562,0,0.3774642944335938,0,0.382354736328125,0,0.1888656616210938,0,-2.055381774902344,0,0.3646392822265625,0,0.3694076538085938,0,0.3730316162109375,0.3730621337890625,0.3782272338867188,0.2566757202148438,0,0,0,0,0,0,0,-1.722541809082031,0.3688507080078125,0.3780975341796875,0,0.3785171508789062,0,0,0.3760299682617188,0,0.2797164916992188,0,0,0,0,0,-1.71832275390625,0,0.371307373046875,0,0,0.371002197265625,0,0.3791046142578125,0.3736801147460938,0,0.28094482421875,0,0,0,-1.676826477050781,0,0.373046875,0.3794174194335938,0,0.377410888671875,0,0.38067626953125,0.2231521606445312,0,0,-1.952095031738281,0.3625869750976562,0.3754119873046875,0,0.3710098266601562,0.3714828491210938,0.3759918212890625,0,0.1514358520507812,0,0,-1.868171691894531,0,0.3698959350585938,0,0.3805923461914062,0,0.3664093017578125,0,0.3723602294921875,0,0.372589111328125,0.06136322021484375,0,0,-1.75677490234375,0,0.3724212646484375,0,0.3736724853515625,0.3716888427734375,0,0.37628173828125,0,0.316802978515625,0,0,0,-1.595855712890625,0.373870849609375,0,0.3802566528320312,0.37762451171875,0,0.379852294921875,0.1374740600585938,0,0,0,-1.754432678222656,0,0.3715972900390625,0.376922607421875,0,0.37237548828125,0,0.378204345703125,0.3077392578125,0,0,0,0,0,-1.556312561035156,0.38055419921875,0.3803787231445312,0,0,0.3715057373046875,0,0.3730697631835938,0.1023025512695312,0,-1.68218994140625,0.3733291625976562,0.3863754272460938,0.3705596923828125,0,0.3774261474609375,0,0.225189208984375,0,0,0,0,0,-1.397842407226562,0,0.377288818359375,0,0.3762741088867188,0.3743972778320312,0.3197402954101562,0,0,0,0,0,0,0,-1.467658996582031,0,0.3855209350585938,0,0,0.3774871826171875,0,0.3721237182617188,0,0.37066650390625,0,0.010894775390625,0,-1.515785217285156,0,0.3764114379882812,0,0.3840560913085938,0.3751678466796875,0.3785018920898438,0,0.0499267578125,0,-1.518356323242188,0,0.3771591186523438,0.3840560913085938,0.37762451171875,0,0.3725357055664062,0.0545196533203125,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.635345458984375,0,0,0.1972885131835938,0.37774658203125,0,0.376556396484375,0.3597869873046875,0,0.369140625,0.00142669677734375,0,0,-1.43109130859375,0.3702468872070312,0,0.3761749267578125,0,0.3735885620117188,0,0.3570938110351562,0,0,0,0,0,-1.407936096191406,0,0.3761978149414062,0,0.3794021606445312,0,0.3787307739257812,0.3188552856445312,0,0,0,-1.467689514160156,0,0.3619842529296875,0,0.3849563598632812,0.3730621337890625,0.3624267578125,0.02979278564453125,0,0,0,-1.420005798339844,0,0,0.3520355224609375,0,0.3833694458007812,0,0,0.363067626953125,0,0.365325927734375,0,0,0,0,0,-1.360610961914062,0,0.3309249877929688,0,0.35601806640625,0,0.3696212768554688,0.3471450805664062,0,0,0,-1.293388366699219,0,0.37322998046875,0,0.3760986328125,0.3752899169921875,0,0.211151123046875,0,0,0,-1.175682067871094,0,0.383758544921875,0.3627548217773438,0,0.3682785034179688,0.1026687622070312,0,0,-1.363716125488281,0,0.3717117309570312,0,0.3830108642578125,0,0.3735885620117188,0.2764129638671875,0,0,0,0,0,-1.145484924316406,0,0.382568359375,0.3791351318359375,0.3655853271484375,0.0585784912109375,0,0,0,0,0,-1.044410705566406,0,0.3734130859375,0,0.345428466796875,0.3535537719726562,0,0.0117340087890625,0,0,-1.358360290527344,0.3332901000976562,0,0.3531112670898438,0,0.3702163696289062,0,0,0.3408126831054688,0,0,0,0,0,-1.168891906738281,0,0.369659423828125,0.380462646484375,0,0,0.3648529052734375,0.09241485595703125,0,0,-1.2489013671875,0,0.3680801391601562,0,0.3783493041992188,0,0.3669357299804688,0,0.1733474731445312,0,0,0,0,0,-1.001182556152344,0,0.3906097412109375,0,0.3620071411132812,0.2857513427734375,0,0,0,0,0,0,0,0,0,-1.213249206542969,0.3108978271484375,0,0.3351516723632812,0,0.3716583251953125,0,0.2321548461914062,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.2607421875,0,0,0.3625869750976562,0,0.3856964111328125,0.3307647705078125,0,0.3343963623046875,0,0.3643112182617188,0,0,0.3676300048828125,0,0,0.3693618774414062,0,0.319915771484375,0,0.306060791015625,0,0.3052825927734375,0,0,0.3042755126953125,0,0,0.3094024658203125,0,0.3056793212890625,0,0.3084487915039062,0,0.3102569580078125,0,0,0.306884765625,0,0.1789703369140625,0,0,0,-4.947235107421875,0,0.3957672119140625,0.333404541015625,0.3716583251953125,0,0.3733901977539062,0,0.3798599243164062,0,0.3717269897460938,0.3772430419921875,0,0.387298583984375,0,0.3844070434570312,0.3849945068359375,0,0.3767166137695312,0.3732833862304688,0,0.380615234375,0,0.2064132690429688,0,0,0,-4.878303527832031,0.387298583984375,0,0.3397674560546875,0.3461151123046875,0.3836441040039062,0,0,0.377777099609375,0.3477935791015625,0.3525543212890625,0,0.3753204345703125,0,0.332000732421875,0.367462158203125,0,0.3823471069335938,0,0.3497390747070312,0,0.3735733032226562,0,0.3101882934570312,0,0,0,-4.989059448242188,0,0.3870391845703125,0.365753173828125,0,0.358551025390625,0.3617630004882812,0,0.3760452270507812,0,0.359375,0.35797119140625,0,0.376922607421875,0.3615036010742188,0,0.3770904541015625,0,0.3644866943359375,0,0.3588790893554688,0.3742446899414062,0,0.335205078125,0.019073486328125,0,0,-4.978424072265625,0,0.40484619140625,0,0.3626785278320312,0,0.3644027709960938,0.3782196044921875,0,0.3549652099609375,0,0.3599014282226562,0,0.372772216796875,0,0.3575286865234375,0.3733367919921875,0.3591766357421875,0,0.361083984375,0.372711181640625,0,0.3562164306640625,0,0.3430709838867188,0,0,0,0,0,0,0,0,-4.513519287109375,0,0,0.3565444946289062,0,0.3685226440429688,0,0.3716583251953125,0,0.3714599609375,0.3713455200195312,0,0.3656082153320312,0.3670196533203125,0,0.3675918579101562,0,0,0.3690032958984375,0,0.36920166015625,0,0.367462158203125,0,0.3644485473632812,0,0.243865966796875,0,0,0,-4.710342407226562,0.3870468139648438,0,0.3621673583984375,0,0.3764114379882812,0,0.3753280639648438,0.3683242797851562,0,0.3700790405273438,0.3653640747070312,0,0,0.3743362426757812,0.3788528442382812,0,0.3707122802734375,0.3736572265625,0.3777008056640625,0.365020751953125,0,0.00323486328125,0,0,0,0,0,0,0,-4.549468994140625,0,0.3716583251953125,0,0,0.3806533813476562,0.3641128540039062,0,0.367156982421875,0.3696746826171875,0.3666915893554688,0,0,0.357666015625,0.3637619018554688,0.3745880126953125,0,0.368194580078125,0,0.37896728515625,0,0.3651809692382812,0,0.2567214965820312,0,0,0,0,0,-4.551200866699219,0.3795013427734375,0,0.362060546875,0.3614120483398438,0.3792266845703125,0,0,0.3660202026367188,0,0.3613204956054688,0,0.37255859375,0,0,0.3758316040039062,0.370269775390625,0,0.3734359741210938,0,0,0.3777847290039062,0,0,0.3728866577148438,0,0.2323684692382812,0,0,0,0,0,-4.431495666503906,0.3618316650390625,0,0.390960693359375,0.3683929443359375,0.3726959228515625,0,0.3642578125,0,0.3672027587890625,0.37811279296875,0.3664932250976562,0,0.3813629150390625,0,0.385101318359375,0.3748931884765625,0.3705596923828125,0,0.0810394287109375,0,0,0,0,0,-4.220405578613281,0,0.368988037109375,0,0.3613128662109375,0,0.3622055053710938,0,0.3667221069335938,0,0.36749267578125,0.3623580932617188,0,0.3835220336914062,0.3707809448242188,0,0.3777999877929688,0.3750076293945312,0,0.3724136352539062,0.2809982299804688,0,0,0,-4.318618774414062,0,0.3476181030273438,0,0.3694992065429688,0,0.3685379028320312,0,0.3630218505859375,0,0.356903076171875,0,0.3688735961914062,0,0,0.3681640625,0,0.380279541015625,0,0.3679122924804688,0,0.3676223754882812,0,0.382904052734375,0,0.354095458984375,0.05037689208984375,0,0,0,0,0,-4.029899597167969,0.3866424560546875,0,0.3707809448242188,0,0.3800277709960938,0,0.3646392822265625,0,0.3682022094726562,0.3701858520507812,0,0.3748855590820312,0.3777313232421875,0.3802566528320312,0,0.3809967041015625,0,0.3606338500976562,0.04001617431640625,0,0,0,-3.94952392578125,0,0.3872528076171875,0,0,0.3646697998046875,0,0.364776611328125,0,0.365570068359375,0.3711318969726562,0,0.3690872192382812,0.375762939453125,0,0,0.3763961791992188,0,0.3790359497070312,0,0,0.3734512329101562,0.3454971313476562,0,0,0,0,0,-4.192398071289062,0,0.3823471069335938,0,0.3762969970703125,0.3614654541015625,0,0.361083984375,0,0.3675003051757812,0.37091064453125,0,0.3733901977539062,0,0.375518798828125,0.3760986328125,0,0.3703994750976562,0,0.3755569458007812,0,0.2229690551757812,0,0,0,-4.019607543945312,0,0.3756942749023438,0,0.36724853515625,0,0.3569869995117188,0.364990234375,0,0.3694839477539062,0,0.366455078125,0,0.3777542114257812,0,0.3772811889648438,0,0.3783035278320312,0,0.3818359375,0,0.3700790405273438,0.05254364013671875,0,0,0,-3.762496948242188,0,0.3749847412109375,0,0.3568954467773438,0,0,0.3590774536132812,0.3637008666992188,0,0.3625869750976562,0.3716354370117188,0,0.3748092651367188,0,0.3765487670898438,0,0.3785552978515625,0,0.373870849609375,0.1871109008789062,0,0,0,0,0,-3.841117858886719,0,0.3712692260742188,0,0.3758926391601562,0,0,0.3667221069335938,0,0.3730621337890625,0,0.3756942749023438,0.3739776611328125,0,0.3779983520507812,0,0.3808975219726562,0,0.3841934204101562,0.3777236938476562,0.1990127563476562,0,0,0,0,0,-3.830390930175781,0.370849609375,0.3535842895507812,0.3486785888671875,0.3603515625,0,0.3672714233398438,0.3695526123046875,0,0.3709793090820312,0,0,0.37481689453125,0,0,0.378326416015625,0,0.3764114379882812,0,0.2730178833007812,0,0,0,0,0,-3.808692932128906,0.3719406127929688,0,0.3458786010742188,0,0.3456954956054688,0,0.3641586303710938,0,0.370361328125,0,0.376220703125,0,0.3772964477539062,0,0,0.3815383911132812,0.3831634521484375,0.3779296875,0.2261123657226562,0,0,0,0,0,-3.694305419921875,0,0.3741683959960938,0,0.35235595703125,0.3577423095703125,0,0.3662567138671875,0,0.3734283447265625,0.3763961791992188,0.3802566528320312,0.382293701171875,0,0.3843154907226562,0,0,0.3725357055664062,0,0.08440399169921875,0,0,0,0,0,-3.467086791992188,0.363037109375,0,0.3544845581054688,0.3638839721679688,0,0.3744888305664062,0,0.3750228881835938,0.3777313232421875,0,0.3808517456054688,0.3821868896484375,0.3793258666992188,0,0.2240982055664062,0,0,0,0,0,0,0,-3.595443725585938,0,0.3663864135742188,0,0.3546371459960938,0,0.3597259521484375,0.3690261840820312,0.3749923706054688,0,0.3732376098632812,0.3761138916015625,0,0.3777999877929688,0.379913330078125,0.36480712890625,0.00508880615234375,0,-3.644790649414062,0,0.3698654174804688,0,0.3440017700195312,0.3487930297851562,0,0.3677978515625,0,0.3701171875,0,0.3758316040039062,0,0.3792572021484375,0,0.3803863525390625,0,0,0.3818359375,0,0,0.3717117309570312,0.05979156494140625,0,0,0,0,0,-3.2733154296875,0.3551254272460938,0,0.3606338500976562,0,0.36688232421875,0,0.3753585815429688,0,0.3801116943359375,0.3758010864257812,0.3802566528320312,0,0.3837814331054688,0,0.3706130981445312,0,0,0.027618408203125,0,0,0,-3.181053161621094,0.3518142700195312,0,0.3573837280273438,0,0.3658905029296875,0,0,0.3718643188476562,0,0.3711013793945312,0,0,0.3737945556640625,0,0.377349853515625,0.379730224609375,0.3333511352539062,0,0,0,-3.436393737792969,0.3664474487304688,0.3570938110351562,0.3645401000976562,0.3743896484375,0.3769454956054688,0,0,0.3772506713867188,0.3777999877929688,0.3806304931640625,0,0,0.37762451171875,0,0.183349609375,0,0,0,-3.226997375488281,0,0,0.36151123046875,0,0.361083984375,0,0.359771728515625,0,0.36285400390625,0,0,0.3651351928710938,0.3805007934570312,0.3684310913085938,0,0.3715362548828125,0,0.3514404296875,0,0.04266357421875,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-3.373222351074219,0,0,0,0,0,0,0,0,0.4039688110351562,0,0.39019775390625,0,0.3486709594726562,0,0.3683700561523438,0,0.3648452758789062,0.35003662109375,0,0.351318359375,0,0.3207855224609375,0.3348007202148438,0,0.2365188598632812,0,0,0,0,0,-3.199996948242188,0,0.4104385375976562,0,0.3904647827148438,0,0,0.3703536987304688,0.3615951538085938,0.367401123046875,0,0.3444366455078125,0,0.3395462036132812,0,0.3548355102539062,0,0,0.3558578491210938,0,0,0,0,0,0,0,0,-2.892425537109375,0.3972396850585938,0,0,0.368682861328125,0,0.3682861328125,0,0.3436050415039062,0,0.3357925415039062,0.316253662109375,0.3470382690429688,0.370513916015625,0,0,0.1383056640625,0,0,0,0,0,-2.994148254394531,0,0.4046707153320312,0,0,0.3861007690429688,0.3700027465820312,0,0.355377197265625,0,0.3321380615234375,0.3163833618164062,0,0.37200927734375,0.3779983520507812,0,0,0.171417236328125,0,0,0,-2.977706909179688,0,0.4083404541015625,0,0.3831710815429688,0.3620529174804688,0,0.343597412109375,0,0.3244781494140625,0,0,0.3433685302734375,0,0.3736572265625,0.3753433227539062,0.1540145874023438,0,0,0,0,0,-2.895835876464844,0.4090118408203125,0.3845748901367188,0.3502731323242188,0,0.3334274291992188,0,0.3261795043945312,0,0.3778533935546875,0,0.3747024536132812,0.3784942626953125,0.050262451171875,0,0,0,0,0,0,0,-2.699394226074219,0.3983306884765625,0,0.361724853515625,0.342987060546875,0,0.3201370239257812,0.373870849609375,0.3788070678710938,0.3819503784179688,0,0.2291030883789062,0,0,0,0,0,-2.84423828125,0,0,0.40692138671875,0,0.3722381591796875,0,0.3409271240234375,0,0.3212661743164062,0,0.3726959228515625,0.375518798828125,0,0.3781814575195312,0,0,0.362518310546875,0,0,0,0,0,-2.949142456054688,0,0.4255447387695312,0,0.380218505859375,0.3427734375,0.3172454833984375,0,0.3751144409179688,0.3736572265625,0.3779449462890625,0,0,0.3794021606445312,0,0.0619049072265625,0,0,0,0,0,-2.582839965820312,7.964286804199219,0,0,0,0,0,0,0,0,0,0,0,7.62939453125,7.62939453125e-06,0,0,0,0,0,0,0,0,0,0,0,0,0,15.2587890625,0,0,0,0,0,0,0,0,0],"filename":[null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null]},"interval":10,"files":[],"prof_output":"/tmp/Rtmplhcgkk/file2a3f23e68007.prof","highlight":{"output":["^output\\$"],"gc":["^<GC>$"],"stacktrace":["^\\.\\.stacktraceo(n|ff)\\.\\.$"]},"split":"h"}},"evals":[],"jsHooks":[]}</script>
```

``` r
# rowSums(), colSums(), rowMeans(), and colMeans() are vectorised and fast.
# for loop is not the slowest, but the ugliest.
```


For systematic speed comparisons, try the `microbenchmark` package

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
  mean3(x,.5)
)
```

```
## Unit: milliseconds
##           expr      min       lq     mean   median       uq      max neval cld
##  mean1(x, 0.5) 20.53848 22.59038 23.00716 22.95674 23.38703 35.12610   100  ab
##  mean2(x, 0.5) 19.79849 21.66087 22.46968 21.95363 22.60861 36.14500   100  a 
##  mean3(x, 0.5) 20.59353 22.60208 23.36886 22.96599 23.38462 34.80657   100   b
```

**Vectorize**.

Computers are really good at math, so exploit this.

* First try vectors
* Then try `apply` functions
* See https://uscbiostats.github.io/software-dev-site/handbook-slow-patterns.html


Vector operations are generally faster and easier to read than loops

``` r
x <- runif(1e6)

# Compare 2 moving averages

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
```

```
## [1]  0  8 -1
```

``` r
ma2 <- function(y){
    z2 <- diff(y)/2
    z2 <- c(NA, z2) 
    return(z2)
}

all.equal(ma1(y),ma2(y))
```

```
## [1] TRUE
```

``` r
microbenchmark::microbenchmark(
  ma1(y),
  ma2(y)
)
```

```
## Unit: milliseconds
##    expr       min        lq      mean    median        uq      max neval cld
##  ma1(y) 146.67654 160.82927 163.14244 163.75267 167.78925 179.1736   100  a 
##  ma2(y)  18.98932  23.15959  26.01814  24.92404  27.31825 114.6350   100   b
```
Likewise, matrix operations are often faster than vector operations.


**Packages**.

Before creating your own program, check if there is a faster or more memory efficient version. E.g., [data.table](https://cran.r-project.org/web/packages/data.table/vignettes/datatable-intro.html) or [Rfast2](https://cran.r-project.org/web/packages/Rfast2/index.html) for basic data manipulation.

Some functions are simply wrappers for the function you want, and calling it directly can speed things up. 

``` r
X <- cbind(1, runif(1e6))
Y <- X %*% c(1,2) + rnorm(1e6)
DAT <- as.data.frame(cbind(Y,X))

system.time({ lm(Y~X, data=DAT) })
```

```
##    user  system elapsed 
##   0.351   0.003   0.141
```

``` r
system.time({ .lm.fit(X, Y) })
```

```
##    user  system elapsed 
##   0.148   0.000   0.036
```

``` r
system.time({ solve(t(X)%*%X) %*% (t(X)%*%Y) })
```

```
##    user  system elapsed 
##   0.029   0.000   0.018
```
Note that such functions to have fewer checks and return less information, so you must know exactly what you are putting in and getting out.


**Parallel**.

Sometimes there will still be a problematic bottleneck. 

Your next step should be parallelism:

* Write the function as a general vectorized function.
* Apply the same function to every element in a list *at the same time*


``` r
# lapply in parallel on {m}ultiple {c}ores
x <- c(10,20,30,40,50)
f <- function(element) { element^element } 
parallel::mclapply( x, mc.cores=2, FUN=f)
```

```
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
```

```
##    user  system elapsed 
##   0.020   0.001   0.020
```

``` r
# brute power
x <- 0:1E6
s_bp <- system.time({
  e_power_e_mc <- unlist( parallel::mclapply(x, mc.cores=2, FUN=e_power_e_fun))
})
s_bp
```

```
##    user  system elapsed 
##   0.879   0.153   0.580
```

``` r
# Same results
all(e_power_e_vec==e_power_e_mc)
```

```
## [1] TRUE
```

Parallelism does not go great with a GUI.
For identifying bottlenecks on a cluster without a GUI, try `Rprof()`

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

If you still are stuck, you can

* try [Amazon Web Server](https://aws.amazon.com/ec2/) for more brute-power 
* rewrite bottlenecks with a working C++ compiler or Fortran compiler.

Before doing that, however, look into <https://cran.r-project.org/web/views/HighPerformanceComputing.html>


**Compiled Code**.

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
```

```
## [1] 6
```

For help getting started with Rcpp, see https://cran.r-project.org/web/packages/Rcpp/vignettes/Rcpp-quickref.pdf


First try to use C++ (or Fortran) code that others have written

``` r
.C
.Fortran
```
For a tutorial, see https://masuday.github.io/fortran_tutorial/r.html


**Memory Usage**.

For finding problematic blocks or whole scripts: `utils::Rprof(memory.profiling = TRUE)` logs total memory usage of R at regular time intervals

For finding problematic functions: `utils::Rprofmem()` logs memory usage at each call

For memory leaks, first free up space and use the `bench` package for timing

``` r
gc() # garbage cleanup

bench::mark(
  mean1(x,.5),
  mean2(x,.5),
  mean3(x,.5))
```



## More Literature

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


# Applications
***

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


## More Literature

Overview

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



# Software {.tabset}

The current version of R (and any packages) used to make this document are

``` r
sessionInfo()
```

```
## R version 4.4.3 (2025-02-28)
## Platform: x86_64-redhat-linux-gnu
## Running under: Fedora Linux 42 (Workstation Edition Prerelease)
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
## [1] parallel  stats     graphics  grDevices utils     datasets  compiler 
## [8] methods   base     
## 
## other attached packages:
## [1] Rcpp_1.0.14          profvis_0.4.0        microbenchmark_1.5.0
## [4] colorout_1.3-2      
## 
## loaded via a namespace (and not attached):
##  [1] cli_3.6.4         knitr_1.49        TH.data_1.1-3     rlang_1.1.5      
##  [5] xfun_0.51         jsonlite_1.9.0    zoo_1.8-13        htmltools_0.5.8.1
##  [9] sass_0.4.9        rmarkdown_2.29    grid_4.4.3        evaluate_1.0.3   
## [13] jquerylib_0.1.4   MASS_7.3-65       fastmap_1.2.0     mvtnorm_1.3-3    
## [17] yaml_2.3.10       lifecycle_1.0.4   bookdown_0.42     multcomp_1.4-28  
## [21] codetools_0.2-20  sandwich_3.1-1    htmlwidgets_1.6.4 lattice_0.22-6   
## [25] digest_0.6.37     R6_2.6.1          splines_4.4.3     Matrix_1.7-2     
## [29] bslib_0.9.0       tools_4.4.3       survival_3.8-3    cachem_1.1.0
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

**Used Rarely:**

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


**Linux:** An alternative to windows and mac operating systems.
Used in computing clusters, big labs, and phones.
E.g., Ubuntu and Fedora are popular brands

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


**Latex:** An alternative to Microsoft Word.
Great for writing many equations and typesetting.
Easy to integrate Figures, Tables, and References.
Steep learning curve.

* easiest to get started online with [Overleaf](https://www.overleaf.com/)
* can also download yourself via [Tex Live](https://www.tug.org/texlive/) and GUI [TexStudio](https://www.texstudio.org/)

To begin programming, see 

* https://biostat.app.vumc.org/wiki/pub/Main/TheresaScott/Intro.to.LaTeX.TAScott.pdf
* https://www.tug.org/begin.html



## Sweave


**Knitr:** 
You can produce a pdf from an .Rnw file via `knitr`


``` bash
Rscript -e "knitr::Sweave2knitr('Sweave_file.Rnw')"
Rscript -e "knitr::knit2pdf('Sweave_file-knitr.Rnw')"
```

For background on knitr

* https://yihui.org/knitr/
* https://kbroman.org/knitr_knutshell/pages/latex.html
* https://sachsmc.github.io/knit-git-markr-guide/knitr/knit.html


**Sweave:** is an alternative to Rmarkdown for integrating latex and R. While Rmarkdown "writes R and latex within markdown", Sweave "write R in latex". Sweave files end in ".Rnw" and can be called within R


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



