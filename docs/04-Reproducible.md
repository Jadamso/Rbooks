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



# Performance 
***

## Debugging 

In R, you use multiple functions on different types of data objects. Moreover, you "typically solve complex problems by decomposing them into simple functions, not simple objects." (H. Wickham)


Problems print to the console

``` r
warning("This is what a warning looks like")
stop("This is what an error looks like")
```

```
## Error: This is what an error looks like
```

Nonproblems also print to the console

``` r
message("This is what a message looks like")
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
##   0.133   0.006   0.139
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
<div class="profvis html-widget html-fill-item" id="htmlwidget-36cca166e137630be913" style="width:100%;height:600px;"></div>
<script type="application/json" data-for="htmlwidget-36cca166e137630be913">{"x":{"message":{"prof":{"time":[1,2,3,4,5,6,7,8,9,10,10,11,11,12,12,13,13,14,14,15,15,16,16,17,17,18,18,19,19,20,21,21,22,22,23,23,24,25,25,26,26,26,27,27,28,29,30,31,31,32,32,32,33,33,33,34,34,35,35,36,36,37,37,38,39,39,39,40,41,42,42,43,43,44,44,45,45,45,46,47,48,48,49,49,50,51,52,52,53,54,55,55,56,57,57,57,58,58,58,59,59,60,60,61,61,62,62,63,63,63,64,64,64,65,66,66,67,67,68,68,69,69,70,70,70,71,71,72,72,73,73,74,74,75,75,76,76,76,77,78,78,78,79,79,80,80,81,82,82,82,83,83,83,84,84,85,85,86,86,87,87,88,89,89,89,90,91,92,93,93,94,95,95,95,96,97,98,98,99,99,100,101,101,101,102,102,103,103,103,104,105,105,106,106,106,107,107,107,108,108,109,110,110,111,111,111,112,112,112,113,114,114,115,115,116,116,116,117,117,118,118,119,120,120,120,121,122,123,123,123,124,125,125,126,126,127,127,127,128,128,129,130,131,132,132,133,133,133,134,135,136,136,137,137,138,138,139,139,140,140,141,141,142,142,143,143,144,144,144,145,146,146,147,147,148,149,149,150,150,151,151,152,153,153,154,154,154,155,155,156,156,157,157,158,158,159,159,159,160,161,161,162,162,163,163,163,164,164,164,164,165,165,165,166,167,167,168,168,168,169,169,169,170,171,171,172,172,173,173,174,174,174,175,175,176,177,177,177,178,178,179,179,179,180,180,180,181,181,181,182,182,182,183,183,184,184,185,186,186,187,188,188,189,190,191,192,192,192,193,193,193,194,194,194,195,195,195,196,196,196,197,197,198,198,199,199,199,199,200,200,201,202,202,203,203,204,204,204,205,205,206,206,207,207,208,208,209,209,210,210,211,211,212,212,212,213,213,213,214,214,214,215,216,216,217,217,217,218,218,219,219,220,221,221,222,222,223,223,224,224,225,225,226,227,227,228,228,229,229,229,230,230,231,231,232,232,233,233,233,234,234,235,235,235,236,236,237,237,237,237,238,239,240,240,241,241,241,242,242,242,243,243,244,245,245,245,246,246,246,247,248,249,249,250,251,251,252,252,253,253,253,254,255,255,256,257,257,257,258,259,259,260,260,261,261,261,262,262,263,263,264,264,265,265,266,266,266,267,267,268,268,268,268,269,270,271,271,272,272,272,273,274,274,275,276,276,276,277,277,278,279,279,279,280,280,280,281,281,281,282,282,282,283,283,283,284,284,284,285,285,285,286,286,286,287,287,287,288,288,288,289,289,289,290,291,291,291,292,292,293,293,294,295,296,297,297,298,299,300,301,302,302,302,303,303,304,305,305,306,306,306,307,307,308,308,309,309,310,310,311,311,312,313,313,313,314,315,316,317,317,317,318,318,319,319,320,320,321,321,322,322,323,323,324,324,325,325,326,327,327,328,328,329,330,330,331,332,332,333,333,334,334,334,335,336,337,337,338,338,339,340,341,341,342,343,343,344,344,344,345,345,345,346,346,347,348,348,349,350,350,351,351,352,352,353,354,354,355,355,355,356,356,357,358,358,359,359,360,360,361,361,362,363,364,364,365,365,365,366,366,367,367,368,368,368,369,370,370,371,371,372,373,373,374,375,375,375,376,376,377,378,378,379,379,380,381,382,382,383,383,384,384,385,385,385,386,386,387,388,389,390,391,391,392,392,393,393,394,394,395,395,395,396,396,397,397,398,399,399,400,401,402,403,403,404,404,405,405,405,406,406,407,408,408,409,410,411,411,411,412,413,413,413,414,414,414,415,416,416,417,417,418,418,418,419,419,420,420,421,421,422,422,423,423,424,424,424,425,425,426,426,427,428,429,429,430,430,431,431,432,432,433,433,434,434,435,435,436,437,437,438,439,439,440,440,441,441,442,442,443,444,445,446,447,448,448,449,449,450,450,451,451,451,452,452,452,453,454,454,454,455,455,456,456,457,457,458,459,459,459,460,460,460,461,461,461,462,462,463,463,464,464,465,465,465,466,466,467,468,468,469,469,470,470,471,471,472,473,473,474,474,475,475,475,476,476,477,478,478,478,479,479,480,481,481,482,482,483,483,484,484,485,486,486,487,487,487,488,488,489,489,490,491,491,492,493,493,494,494,495,495,495,496,496,496,497,497,497,498,498,498,499,499,499,500,500,500,501,501,501,502,502,503,503,504,505,506,507,507,508,509,509,509,510,511,512,513,513,514,514,515,515,516,516,516,517,517,517,518,518,518,519,519,520,520,521,521,522,523,523,524,525,525,526,526,527,528,528,529,529,530,530,531,531,531,532,533,533,533,534,534,535,535,536,536,537,537,538,538,538,539,539,540,540,541,541,542,542,542,543,543,543,544,544,545,545,546,547,547,548,549,549,549,550,550,550,551,551,552,552,553,554,555,555,556,557,557,557,558,558,558,559,560,560,561,562,562,563,563,564,565,565,565,566,566,567,567,568,568,569,569,570,570,571,572,572,573,573,574,574,574,575,575,576,577,577,578,579,579,580,580,580,581,581,582,582,582,583,584,584,585,585,586,586,587,587,587,588,588,588,589,589,590,590,591,591,591,592,592,593,593,594,594,595,595,596,596,596,597,597,598,598,599,600,600,601,602,602,602,603,604,604,605,605,606,606,607,607,608,609,609,609,610,611,611,611,612,612,613,613,614,614,615,616,616,616,616,617,617,618,618,619,619,620,621,621,622,622,623,623,623,624,624,625,626,626,627,628,628,629,629,630,630,631,631,632,633,633,634,635,635,636,636,637,637,637,638,638,639,640,640,641,641,642,642,643,643,643,644,644,644,645,645,646,646,647,647,648,649,649,650,650,650,651,652,652,653,653,654,654,655,656,656,656,657,657,657,658,658,658,659,659,659,660,660,660,661,661,661,662,662,663,663,664,664,665,665,666,667,667,667,668,668,669,670,670,671,671,672,672,672,673,673,673,674,674,674,675,676,676,677,678,678,679,679,680,680,681,681,682,682,683,684,684,685,686,686,686,687,688,688,689,689,690,690,691,691,692,692,692,693,693,693,694,695,695,696,697,698,698,698,699,699,700,700,701,702,702,703,704,704,704,704,705,705,706,706,707,707,708,708,709,709,710,710,711,711,712,713,714,714,715,715,715,716,716,717,717,718,719,720,720,720,721,721,721,722,722,722,723,724,724,724,725,725,726,726,727,727,727,728,728,728,729,729,730,731,732,733,733,733,734,734,735,735,736,736,737,737,738,738,738,739,739,739,740,740,740,741,741,742,743,743,743,744,744,744,745,745,746,746,747,747,748,748,749,749,749,750,750,750,751,751,752,753,754,754,754,755,755,755,756,756,757,758,759,759,760,760,760,761,761,762,763,763,764,764,765,765,765,766,766,766,767,767,767,768,768,768,769,770,770,771,771,772,772,773,773,774,774,775,775,776,776,777,777,778,778,779,779,780,780,781,781,782,782,783,783,784,784,785,785,786,786,787,787,788,788,789,789,790,790,791,791,792,792,793,793,794,794,795,795,796,796,796,797,797,798,798,799,800,801,802,802,803,803,804,805,805,806,806,807,807,808,809,810,810,811,811,812,812,812,813,813,814,814,814,815,815,816,816,817,817,818,819,819,820,820,821,822,822,823,824,824,825,825,826,826,827,827,828,828,829,829,830,830,830,831,831,831,832,832,833,833,834,834,835,836,836,836,837,837,837,838,838,839,840,841,841,842,843,843,844,844,845,845,846,847,847,847,848,848,848,849,850,850,850,851,852,852,853,853,854,855,856,856,857,857,858,859,859,860,861,862,862,863,864,864,864,865,865,865,866,866,866,867,867,868,868,869,869,870,871,871,872,872,873,873,874,874,875,876,877,877,878,878,878,879,880,880,881,881,882,882,882,883,883,883,884,884,885,885,886,886,887,887,888,889,889,890,891,892,892,893,893,894,895,895,896,896,896,897,897,898,898,899,899,900,900,901,902,902,903,903,904,905,905,906,906,907,908,909,909,910,910,911,911,912,912,913,914,914,914,915,915,915,916,917,917,918,918,919,919,920,920,921,921,922,922,923,923,924,924,925,926,927,927,928,928,928,929,930,930,930,931,931,931,932,933,933,934,934,935,935,936,937,937,938,938,939,939,940,940,940,941,941,942,943,943,944,945,945,945,946,946,946,947,948,948,949,949,950,951,952,952,953,953,954,955,955,956,956,957,957,958,958,959,959,960,960,960,961,961,961,962,962,963,963,964,965,965,966,967,968,968,969,969,970,970,970,971,971,971,972,973,973,974,974,975,975,976,976,976,977,977,978,978,979,980,981,981,981,982,982,983,984,985,986,987,987,988,988,989,989,990,990,990,991,991,991,992,992,993,994,994,995,995,996,997,997,998,999,1000,1001,1002,1003,1003,1004,1004,1005,1005,1006,1006,1007,1007,1008,1008,1008,1009,1009,1010,1010,1011,1011,1012,1012,1013,1014,1014,1015,1015,1016,1016,1017,1017,1018,1018,1019,1019,1020,1020,1021,1021,1022,1023,1023,1024,1025,1025,1026,1026,1027,1027,1027,1028,1028,1029,1030,1030,1031,1031,1032,1033,1034,1034,1034,1035,1035,1035,1036,1036,1037,1037,1038,1038,1039,1039,1040,1040,1041,1041,1042,1042,1043,1044,1045,1046,1046,1047,1048,1048,1049,1049,1050,1050,1051,1051,1052,1053,1054,1054,1055,1055,1056,1056,1057,1057,1058,1058,1059,1059,1060,1060,1061,1061,1062,1062,1062,1063,1063,1063,1064,1064,1065,1065,1066,1067,1068,1068,1069,1069,1069,1070,1071,1072,1072,1073,1073,1074,1075,1075,1076,1076,1076,1077,1077,1077,1078,1078,1078,1079,1079,1080,1080,1081,1081,1081,1082,1083,1083,1084,1085,1085,1085,1086,1087,1088,1088,1089,1089,1089,1090,1090,1091,1092,1092,1093,1093,1094,1094,1095,1095,1096,1096,1097,1098,1099,1100,1100,1101,1101,1102,1102,1103,1103,1103,1104,1104,1104,1105,1105,1106,1106,1107,1107,1108,1108,1109,1110,1110,1111,1111,1112,1113,1113,1114,1114,1115,1116,1116,1116,1117,1117,1117,1118,1119,1120,1121,1121,1122,1122,1123,1124,1124,1124,1125,1125,1126,1126,1127,1127,1127,1128,1129,1129,1130,1130,1131,1132,1132,1133,1133,1134,1135,1136,1136,1137,1138,1139,1139,1139,1140,1140,1141,1141,1142,1142,1142,1143,1143,1143,1144,1144,1145,1145,1146,1146,1147,1148,1149,1149,1150,1150,1151,1152,1152,1153,1153,1154,1155,1155,1155,1156,1156,1156,1157,1158,1158,1159,1160,1160,1161,1162,1162,1163,1164,1164,1165,1165,1166,1166,1167,1168,1168,1168,1169,1169,1169,1170,1170,1170,1171,1171,1171,1172,1172,1172,1173,1173,1173,1174,1174,1174,1175,1175,1175,1176,1176,1176,1177,1177,1177,1178,1179,1179,1180,1180,1181,1181,1182,1183,1183,1184,1185,1186,1187,1187,1188,1188,1189,1189,1190,1190,1191,1192,1193,1194,1195,1195,1196,1197,1198,1198,1199,1199,1200,1200,1201,1201,1201,1202,1202,1202,1203,1203,1204,1205,1206,1206,1207,1207,1208,1208,1209,1209,1210,1211,1212,1213,1213,1213,1214,1214,1214,1215,1215,1216,1216,1217,1218,1219,1219,1220,1220,1221,1221,1222,1222,1223,1223,1224,1224,1225,1225,1225,1226,1226,1226,1227,1228,1229,1229,1229,1230,1231,1231,1232,1233,1233,1234,1234,1235,1236,1236,1237,1237,1237,1238,1238,1238,1239,1239,1240,1240,1241,1242,1242,1243,1244,1245,1245,1246,1246,1247,1247,1247,1248,1248,1248,1249,1249,1249,1250,1250,1251,1251,1252,1252,1253,1253,1254,1254,1255,1255,1256,1256,1257,1257,1258,1258,1259,1259,1260,1260,1260,1261,1261,1261,1262,1262,1263,1263,1264,1264,1265,1266,1266,1267,1268,1269,1269,1270,1270,1270,1271,1271,1271,1272,1272,1272,1273,1274,1275,1275,1276,1277,1278,1278,1279,1279,1280,1280,1281,1281,1282,1282,1283,1283,1283,1284,1284,1284,1285,1285,1286,1286,1287,1287,1288,1288,1289,1290,1290,1291,1291,1292,1293,1293,1294,1294,1294,1295,1295,1295,1296,1297,1297,1298,1298,1299,1300,1301,1301,1302,1302,1303,1303,1304,1304,1305,1305,1306,1306,1307,1307,1308,1308,1309,1309,1310,1310,1311,1311,1312,1312,1313,1313,1314,1314,1315,1315,1316,1316,1317,1317,1318,1318,1319,1319,1320,1320,1321,1321,1322,1322,1323,1323,1324,1324,1325,1325,1326,1326,1327,1327,1328,1328,1329,1329,1330,1330],"depth":[1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,3,2,1,2,1,1,1,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,1,3,2,1,1,1,2,1,2,1,2,1,3,2,1,1,1,2,1,2,1,1,1,2,1,1,1,2,1,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,3,2,1,2,1,2,1,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,1,3,2,1,1,1,1,2,1,1,3,2,1,1,1,2,1,2,1,1,3,2,1,2,1,3,2,1,1,2,1,3,2,1,3,2,1,2,1,1,2,1,3,2,1,3,2,1,1,2,1,2,1,3,2,1,2,1,2,1,1,3,2,1,1,1,3,2,1,1,2,1,2,1,3,2,1,2,1,1,1,1,2,1,3,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,3,2,1,4,3,2,1,3,2,1,1,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,3,2,1,2,1,1,3,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,1,2,1,1,1,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,4,3,2,1,2,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,3,2,1,2,1,3,2,1,2,1,4,3,2,1,1,1,2,1,3,2,1,3,2,1,2,1,1,3,2,1,3,2,1,1,1,2,1,1,2,1,2,1,3,2,1,1,2,1,1,3,2,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,4,3,2,1,1,1,2,1,3,2,1,1,2,1,1,3,2,1,2,1,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,1,3,2,1,2,1,2,1,1,1,1,2,1,1,1,1,1,3,2,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,1,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,1,2,1,2,1,3,2,1,1,1,2,1,2,1,1,1,2,1,1,2,1,3,2,1,3,2,1,2,1,1,2,1,1,2,1,2,1,2,1,1,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,1,1,2,1,3,2,1,2,1,2,1,3,2,1,1,2,1,2,1,1,2,1,1,3,2,1,2,1,1,2,1,2,1,1,1,2,1,2,1,2,1,3,2,1,2,1,1,1,1,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,1,1,1,2,1,2,1,3,2,1,2,1,1,2,1,1,1,3,2,1,1,3,2,1,3,2,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,1,1,1,1,1,2,1,2,1,2,1,3,2,1,3,2,1,1,3,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,2,1,2,1,1,2,1,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,1,1,1,2,1,1,3,2,1,1,1,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,1,3,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,1,3,2,1,3,2,1,2,1,2,1,1,1,2,1,1,3,2,1,3,2,1,1,2,1,1,2,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,1,2,1,1,2,1,3,2,1,2,1,3,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,1,3,2,1,1,2,1,2,1,2,1,2,1,1,3,2,1,1,3,2,1,2,1,2,1,2,1,1,4,3,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,3,2,1,1,2,1,2,1,2,1,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,3,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,3,2,1,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,1,2,1,1,1,3,2,1,2,1,2,1,1,2,1,1,4,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,3,2,1,2,1,2,1,1,1,3,2,1,3,2,1,3,2,1,1,3,2,1,2,1,2,1,3,2,1,3,2,1,2,1,1,1,1,3,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,1,1,3,2,1,3,2,1,2,1,1,1,2,1,3,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,1,1,2,1,2,1,1,2,1,2,1,2,1,1,1,2,1,2,1,3,2,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,2,1,1,1,2,1,1,2,1,2,1,2,1,1,3,2,1,3,2,1,1,3,2,1,1,2,1,2,1,1,1,2,1,2,1,1,2,1,1,1,2,1,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,1,2,1,3,2,1,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,1,1,2,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,3,2,1,1,3,2,1,3,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,1,3,2,1,3,2,1,1,2,1,2,1,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,1,1,2,1,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,1,3,2,1,2,1,1,1,1,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,1,2,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,1,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,1,2,1,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,1,1,2,1,3,2,1,1,1,2,1,2,1,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,3,2,1,1,2,1,1,3,2,1,1,1,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,1,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,1,3,2,1,3,2,1,1,1,1,2,1,2,1,1,3,2,1,2,1,2,1,3,2,1,1,2,1,2,1,1,2,1,2,1,1,1,2,1,1,1,3,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,1,2,1,2,1,1,2,1,2,1,1,3,2,1,3,2,1,1,2,1,1,2,1,1,2,1,1,2,1,2,1,2,1,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,1,2,1,1,1,1,2,1,2,1,2,1,2,1,1,1,1,1,2,1,1,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,1,1,2,1,2,1,2,1,2,1,1,1,1,3,2,1,3,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,1,1,3,2,1,1,2,1,1,2,1,2,1,1,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,1,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,1,1,2,1,3,2,1,3,2,1,3,2,1,1,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,3,2,1,3,2,1,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1],"label":["rowSums","rowSums","rowSums","rowSums","rowMeans","rowMeans","rowMeans","rowMeans","rowMeans","aperm.default","apply","aperm.default","apply","aperm.default","apply","aperm.default","apply","aperm.default","apply","aperm.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","apply","FUN","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","<GC>","is.na","local","mean.default","apply","apply","apply","apply","mean.default","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","<GC>","mean.default","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","apply","apply","FUN","apply","mean.default","apply","apply","apply","<GC>","apply","apply","apply","FUN","apply","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","<GC>","FUN","apply","mean.default","apply","FUN","apply","length","local","mean.default","apply","FUN","apply","<GC>","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","apply","<GC>","is.na","local","<GC>","is.na","local","mean.default","apply","mean.default","apply","is.na","local","FUN","apply","apply","<GC>","FUN","apply","apply","apply","apply","FUN","apply","apply","<GC>","FUN","apply","apply","apply","FUN","apply","FUN","apply","apply","<GC>","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","mean.default","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","apply","length","local","FUN","apply","isTRUE","mean.default","apply","<GC>","apply","is.na","local","apply","isTRUE","mean.default","apply","apply","apply","<GC>","FUN","apply","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","apply","apply","apply","apply","FUN","apply","<GC>","mean.default","apply","apply","apply","length","local","FUN","apply","FUN","apply","<GC>","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","apply","mean.default","apply","FUN","apply","apply","<GC>","apply","FUN","apply","mean.default","apply","apply","FUN","apply","<GC>","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","<GC>","is.numeric","local","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","length","local","apply","is.na","local","FUN","apply","mean.default","apply","<GC>","is.numeric","local","FUN","apply","apply","isTRUE","mean.default","apply","mean.default","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","<GC>","apply","mean.default","apply","apply","FUN","apply","apply","<GC>","apply","apply","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","<GC>","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","mean.default","apply","FUN","apply","length","local","<GC>","apply","FUN","apply","FUN","apply","mean.default","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","mean.default","apply","<GC>","mean.default","apply","FUN","apply","length","local","apply","<GC>","apply","mean.default","apply","FUN","apply","FUN","apply","<GC>","apply","apply","mean.default","apply","FUN","apply","<GC>","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","<GC>","FUN","apply","length","local","isTRUE","mean.default","apply","mean.default","apply","<GC>","isTRUE","mean.default","apply","apply","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","apply","<GC>","apply","apply","FUN","apply","length","local","<GC>","FUN","apply","apply","length","local","apply","<GC>","FUN","apply","apply","length","local","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","<GC>","apply","isTRUE","mean.default","apply","mean.default","apply","<GC>","isTRUE","mean.default","apply","apply","apply","FUN","apply","<GC>","FUN","apply","apply","mean.default","apply","apply","<GC>","FUN","apply","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","apply","apply","apply","mean.default","apply","apply","apply","apply","apply","<GC>","is.numeric","local","mean.default","apply","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","apply","<GC>","length","local","apply","apply","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","length","local","mean.default","apply","<GC>","apply","<GC>","apply","FUN","apply","apply","FUN","apply","mean.default","apply","apply","FUN","apply","apply","length","local","is.numeric","local","<GC>","FUN","apply","apply","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","FUN","apply","apply","mean.default","apply","FUN","apply","FUN","apply","apply","FUN","apply","<GC>","mean.default","apply","FUN","apply","apply","is.na","local","mean.default","apply","FUN","apply","length","local","apply","apply","mean.default","apply","<GC>","FUN","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","apply","mean.default","apply","FUN","apply","apply","FUN","apply","apply","<GC>","mean.default","apply","FUN","apply","apply","FUN","apply","length","local","apply","apply","mean.default","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","FUN","apply","apply","apply","apply","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","is.numeric","local","FUN","apply","apply","FUN","apply","apply","apply","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","mean.default","apply","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","apply","isTRUE","mean.default","apply","<GC>","mean.default","apply","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","mean.default","apply","apply","apply","FUN","apply","FUN","apply","is.numeric","local","mean.default","apply","<GC>","apply","is.numeric","local","FUN","apply","apply","FUN","apply","apply","length","local","FUN","apply","FUN","apply","<GC>","apply","apply","apply","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","isTRUE","mean.default","apply","is.na","local","length","local","FUN","apply","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","apply","FUN","apply","<GC>","apply","FUN","apply","mean.default","apply","apply","length","local","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","apply","<GC>","length","local","FUN","apply","apply","mean.default","apply","FUN","apply","FUN","apply","length","local","apply","mean.default","apply","<GC>","mean.default","apply","FUN","apply","is.numeric","local","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","apply","apply","apply","FUN","apply","apply","<GC>","is.na","local","apply","apply","apply","FUN","apply","is.numeric","local","FUN","apply","isTRUE","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","apply","isTRUE","mean.default","apply","<GC>","apply","mean.default","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","apply","<GC>","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","length","local","<GC>","apply","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","apply","FUN","apply","<GC>","mean.default","apply","is.na","local","isTRUE","mean.default","apply","apply","is.na","local","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","length","local","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","<GC>","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","apply","mean.default","apply","apply","<GC>","mean.default","apply","apply","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","<GC>","mean.default","apply","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","apply","<GC>","isTRUE","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","apply","FUN","apply","is.na","local","<GC>","FUN","apply","mean.default","apply","apply","mean.default","apply","apply","mean.default","apply","length","local","<GC>","apply","is.na","local","apply","is.na","local","apply","FUN","apply","mean.default","apply","<GC>","FUN","apply","FUN","apply","apply","FUN","apply","mean.default","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","is.numeric","local","mean.default","apply","apply","FUN","apply","<GC>","mean.default","apply","apply","FUN","apply","FUN","apply","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","FUN","apply","length","local","apply","<GC>","FUN","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","apply","mean.default","apply","<GC>","apply","<GC>","apply","mean.default","apply","is.numeric","local","apply","FUN","apply","apply","<GC>","mean.default","apply","apply","mean.default","apply","length","local","FUN","apply","FUN","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","apply","<GC>","mean.default","apply","FUN","apply","mean.default","apply","apply","is.na","local","apply","<GC>","isTRUE","mean.default","apply","mean.default","apply","is.numeric","local","FUN","apply","mean.default","apply","mean.default","apply","<GC>","apply","length","local","apply","apply","mean.default","apply","isTRUE","mean.default","apply","<GC>","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","length","local","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","apply","apply","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","length","local","is.numeric","local","<GC>","FUN","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","length","local","mean.default","apply","FUN","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","FUN","apply","apply","apply","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","is.na","local","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","isTRUE","mean.default","apply","FUN","apply","length","local","apply","apply","apply","FUN","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","length","local","apply","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","length","local","<GC>","mean.default","apply","FUN","apply","is.numeric","local","is.numeric","local","apply","mean.default","apply","FUN","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","length","local","apply","apply","FUN","apply","apply","FUN","apply","mean.default","apply","length","local","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","isTRUE","mean.default","apply","apply","FUN","apply","mean.default","apply","apply","apply","FUN","apply","FUN","apply","apply","mean.default","apply","apply","apply","mean.default","apply","apply","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","mean.default","apply","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","length","local","FUN","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","apply","mean.default","apply","apply","apply","FUN","apply","FUN","apply","apply","mean.default","apply","isTRUE","mean.default","apply","is.na","local","<GC>","apply","<GC>","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","apply","apply","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","length","local","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","length","local","length","local","is.na","local","apply","apply","mean.default","apply","isTRUE","mean.default","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","apply","is.numeric","local","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","mean.default","apply","apply","apply","is.numeric","local","FUN","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","mean.default","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","mean.default","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","apply","mean.default","apply","apply","apply","apply","apply","apply","FUN","apply","is.numeric","local","<GC>","apply","<GC>","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","<GC>","apply","<GC>","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","apply","apply","apply","is.numeric","local","apply","<GC>","apply","<GC>","apply","is.na","local","mean.default","apply","apply","apply","length","local","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","length","local","mean.default","apply","apply","apply","is.na","local","isTRUE","mean.default","apply","apply","apply","mean.default","apply","is.numeric","local","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","isTRUE","mean.default","apply","is.na","local","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","apply","mean.default","apply","isTRUE","mean.default","apply","<GC>","apply","apply","FUN","apply","is.na","local","FUN","apply","FUN","apply","FUN","apply","apply","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","is.na","local","FUN","apply","FUN","apply","FUN","apply","apply","is.na","local","mean.default","apply","apply","mean.default","apply","FUN","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","apply","apply","FUN","apply","mean.default","apply","apply","isTRUE","mean.default","apply","FUN","apply","is.na","local","isTRUE","mean.default","apply","apply","<GC>","apply","<GC>","apply","apply","FUN","apply","FUN","apply","apply","apply","mean.default","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","apply","apply","is.na","local","mean.default","apply","apply","mean.default","apply","mean.default","apply","apply","<GC>","is.numeric","local","<GC>","is.numeric","local","apply","is.na","local","apply","FUN","apply","apply","FUN","apply","apply","mean.default","apply","FUN","apply","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","apply","mean.default","apply","apply","apply","apply","FUN","apply","mean.default","apply","<GC>","apply","<GC>","apply","apply","apply","apply","apply","mean.default","apply","apply","apply","FUN","apply","FUN","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","length","local","apply","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","apply","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","FUN","apply","mean.default","apply","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","is.na","local","is.na","local","apply","FUN","apply","apply","apply","length","local","mean.default","apply","isTRUE","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","length","local","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","is.na","local","FUN","apply","FUN","apply","apply","FUN","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","apply","length","local","apply","apply","is.na","local","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","length","local","is.numeric","local","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","mean.default","apply","is.numeric","local","apply","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","is.numeric","local","mean.default","apply","mean.default","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","any","local","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply"],"filenum":[null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null],"linenum":[null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null],"memalloc":[122.1862258911133,122.1862258911133,122.1862258911133,122.1862258911133,137.4451751708984,137.4451751708984,137.4451751708984,137.4451751708984,137.4451751708984,167.4781723022461,167.4781723022461,167.4781723022461,167.4781723022461,167.4781723022461,167.4781723022461,167.4781723022461,167.4781723022461,167.4781723022461,167.4781723022461,167.4781723022461,167.4781723022461,167.4775695800781,167.4775695800781,167.4775695800781,167.4775695800781,167.4775695800781,167.4775695800781,167.4775695800781,167.4775695800781,182.8350601196289,183.1942596435547,183.1942596435547,183.5409317016602,183.5409317016602,183.8741989135742,183.8741989135742,184.2080917358398,184.5001449584961,184.5001449584961,184.6964721679688,184.6964721679688,184.6964721679688,182.9586334228516,182.9586334228516,183.3120269775391,183.6549987792969,183.9935302734375,184.3341903686523,184.3341903686523,184.67041015625,184.67041015625,184.67041015625,184.7307662963867,184.7307662963867,184.7307662963867,183.2245864868164,183.2245864868164,183.5737991333008,183.5737991333008,183.9170150756836,183.9170150756836,184.2567520141602,184.2567520141602,184.5948791503906,184.782829284668,184.782829284668,184.782829284668,183.1558685302734,183.5076217651367,183.8485717773438,183.8485717773438,184.185661315918,184.185661315918,184.5285415649414,184.5285415649414,184.8341064453125,184.8341064453125,184.8341064453125,183.1090469360352,183.4715118408203,183.820198059082,183.820198059082,184.1594314575195,184.1594314575195,184.4985275268555,184.8346786499023,184.8846206665039,184.8846206665039,183.4636001586914,183.8129043579102,184.152099609375,184.152099609375,184.4903106689453,184.8303375244141,184.8303375244141,184.8303375244141,184.934211730957,184.934211730957,184.934211730957,183.4778900146484,183.4778900146484,183.8246078491211,183.8246078491211,184.1618728637695,184.1618728637695,184.5010681152344,184.5010681152344,184.8416976928711,184.8416976928711,184.8416976928711,184.9831085205078,184.9831085205078,184.9831085205078,183.5122680664062,183.8660049438477,183.8660049438477,184.2062301635742,184.2062301635742,184.5447158813477,184.5447158813477,184.8846588134766,184.8846588134766,185.031135559082,185.031135559082,185.031135559082,183.579216003418,183.579216003418,183.931526184082,183.931526184082,184.2724914550781,184.2724914550781,184.6138229370117,184.6138229370117,184.9458312988281,184.9458312988281,185.0784378051758,185.0784378051758,185.0784378051758,183.6564331054688,184.0057144165039,184.0057144165039,184.0057144165039,184.3454208374023,184.3454208374023,184.6840896606445,184.6840896606445,185.0178298950195,185.1249008178711,185.1249008178711,185.1249008178711,185.1249008178711,185.1249008178711,185.1249008178711,183.5246200561523,183.5246200561523,183.8882064819336,183.8882064819336,184.2340774536133,184.2340774536133,184.5743103027344,184.5743103027344,184.9146118164062,185.1705703735352,185.1705703735352,185.1705703735352,183.6711959838867,184.0170593261719,184.3534469604492,184.6900787353516,184.6900787353516,185.0284042358398,185.215576171875,185.215576171875,185.215576171875,183.8040466308594,184.1501083374023,184.4881591796875,184.4881591796875,184.8277206420898,184.8277206420898,185.1620559692383,185.2599029541016,185.2599029541016,185.2599029541016,183.968620300293,183.968620300293,184.3113479614258,184.3113479614258,184.3113479614258,184.6504211425781,184.9923477172852,184.9923477172852,185.3034820556641,185.3034820556641,185.3034820556641,183.8180465698242,183.8180465698242,183.8180465698242,184.1726608276367,184.1726608276367,184.5128021240234,184.852653503418,184.852653503418,185.1948394775391,185.1948394775391,185.1948394775391,185.3464202880859,185.3464202880859,185.3464202880859,184.0547409057617,184.3997116088867,184.3997116088867,184.7420120239258,184.7420120239258,185.0861434936523,185.0861434936523,185.0861434936523,185.388542175293,185.388542175293,183.9640808105469,183.9640808105469,184.3078079223633,184.6480941772461,184.6480941772461,184.6480941772461,184.9862670898438,185.3282699584961,185.4301605224609,185.4301605224609,185.4301605224609,184.2220306396484,184.5622177124023,184.5622177124023,184.9042282104492,184.9042282104492,185.2476425170898,185.2476425170898,185.2476425170898,185.470947265625,185.470947265625,184.1630020141602,184.504997253418,184.8510971069336,185.1936721801758,185.1936721801758,185.5111465454102,185.5111465454102,185.5111465454102,184.1292572021484,184.4686279296875,184.8092498779297,184.8092498779297,185.1498260498047,185.1498260498047,185.4898986816406,185.4898986816406,185.5507354736328,185.5507354736328,184.447998046875,184.447998046875,184.7883834838867,184.7883834838867,185.1298370361328,185.1298370361328,185.4706115722656,185.4706115722656,185.5896072387695,185.5896072387695,185.5896072387695,184.4562225341797,184.7732925415039,184.7732925415039,185.1198120117188,185.1198120117188,185.4583587646484,185.6278762817383,185.6278762817383,184.4381942749023,184.4381942749023,184.7688140869141,184.7688140869141,185.1066513061523,185.4487609863281,185.4487609863281,185.6655349731445,185.6655349731445,185.6655349731445,184.4584503173828,184.4584503173828,184.7944641113281,184.7944641113281,185.1394119262695,185.1394119262695,185.4768524169922,185.4768524169922,185.7025527954102,185.7025527954102,185.7025527954102,184.5082244873047,184.8463134765625,184.8463134765625,185.1950378417969,185.1950378417969,185.5354156494141,185.5354156494141,185.5354156494141,185.7389831542969,185.7389831542969,185.7389831542969,185.7389831542969,184.5956039428711,184.5956039428711,184.5956039428711,184.9298553466797,185.2715225219727,185.2715225219727,185.6124801635742,185.6124801635742,185.6124801635742,185.7747955322266,185.7747955322266,185.7747955322266,184.6972427368164,185.0349884033203,185.0349884033203,185.3746948242188,185.3746948242188,185.7149887084961,185.7149887084961,185.8100509643555,185.8100509643555,185.8100509643555,184.8150405883789,184.8150405883789,185.1598510742188,185.5057373046875,185.5057373046875,185.5057373046875,185.8423004150391,185.8423004150391,185.8447494506836,185.8447494506836,185.8447494506836,184.9466094970703,184.9466094970703,184.9466094970703,185.2912368774414,185.2912368774414,185.2912368774414,185.6299209594727,185.6299209594727,185.6299209594727,185.8788833618164,185.8788833618164,184.7614440917969,184.7614440917969,185.0973129272461,185.4448623657227,185.4448623657227,185.7881622314453,185.9123992919922,185.9123992919922,184.932861328125,185.2758026123047,185.6176300048828,185.9455032348633,185.9455032348633,185.9455032348633,185.9455032348633,185.9455032348633,185.9455032348633,185.9455032348633,185.9455032348633,185.9455032348633,185.9455032348633,185.9455032348633,185.9455032348633,185.0437850952148,185.0437850952148,185.0437850952148,185.3880920410156,185.3880920410156,185.7274322509766,185.7274322509766,185.9776840209961,185.9776840209961,185.9776840209961,185.9776840209961,184.9208297729492,184.9208297729492,185.2591018676758,185.6044998168945,185.6044998168945,185.9459762573242,185.9459762573242,186.0096817016602,186.0096817016602,186.0096817016602,185.1526184082031,185.1526184082031,185.5010986328125,185.5010986328125,185.8436584472656,185.8436584472656,186.0411682128906,186.0411682128906,185.0756301879883,185.0756301879883,185.4151916503906,185.4151916503906,185.7596817016602,185.7596817016602,186.0721740722656,186.0721740722656,186.0721740722656,185.0093841552734,185.0093841552734,185.0093841552734,185.3371887207031,185.3371887207031,185.3371887207031,185.6851196289062,186.0252304077148,186.0252304077148,186.1026382446289,186.1026382446289,186.1026382446289,185.285530090332,185.285530090332,185.6322937011719,185.6322937011719,185.9778594970703,186.1326446533203,186.1326446533203,185.25244140625,185.25244140625,185.5968551635742,185.5968551635742,185.9437789916992,185.9437789916992,186.1621398925781,186.1621398925781,185.2371978759766,185.5768661499023,185.5768661499023,185.9225387573242,185.9225387573242,186.1912078857422,186.1912078857422,186.1912078857422,185.2361679077148,185.2361679077148,185.5720672607422,185.5720672607422,185.9194869995117,185.9194869995117,186.2197265625,186.2197265625,186.2197265625,185.2540969848633,185.2540969848633,185.5943222045898,185.5943222045898,185.5943222045898,185.9412536621094,185.9412536621094,186.247802734375,186.247802734375,186.247802734375,186.247802734375,185.2852325439453,185.6185302734375,185.9581832885742,185.9581832885742,186.2754592895508,186.2754592895508,186.2754592895508,186.2754592895508,186.2754592895508,186.2754592895508,185.6396636962891,185.6396636962891,185.9835968017578,186.3026275634766,186.3026275634766,186.3026275634766,186.3026275634766,186.3026275634766,186.3026275634766,185.688117980957,186.0356674194336,186.3294143676758,186.3294143676758,185.41650390625,185.7554016113281,185.7554016113281,186.1048355102539,186.1048355102539,186.3557205200195,186.3557205200195,186.3557205200195,185.4988327026367,185.843147277832,185.843147277832,186.1925582885742,186.3816528320312,186.3816528320312,186.3816528320312,185.6035232543945,185.9470596313477,185.9470596313477,186.2948226928711,186.2948226928711,186.4071426391602,186.4071426391602,186.4071426391602,185.7319717407227,185.7319717407227,186.0786972045898,186.0786972045898,186.4246063232422,186.4246063232422,186.4321746826172,186.4321746826172,185.8627166748047,185.8627166748047,185.8627166748047,186.2138519287109,186.2138519287109,186.4568710327148,186.4568710327148,186.4568710327148,186.4568710327148,185.6749954223633,186.0195236206055,186.3675994873047,186.3675994873047,186.4811477661133,186.4811477661133,186.4811477661133,185.81689453125,186.1562881469727,186.1562881469727,186.5007934570312,186.5049514770508,186.5049514770508,186.5049514770508,185.9759063720703,185.9759063720703,186.32568359375,186.5284805297852,186.5284805297852,186.5284805297852,186.5284805297852,186.5284805297852,186.5284805297852,186.5284805297852,186.5284805297852,186.5284805297852,186.5284805297852,186.5284805297852,186.5284805297852,186.5284805297852,186.5284805297852,186.5284805297852,186.5284805297852,186.5284805297852,186.5284805297852,186.5284805297852,186.5284805297852,186.5284805297852,186.5284805297852,186.5284805297852,186.5284805297852,186.5284805297852,186.5284805297852,186.5284805297852,186.5284805297852,186.5284805297852,186.5284805297852,186.5284805297852,186.5284805297852,186.5284805297852,185.8227767944336,186.187141418457,186.187141418457,186.187141418457,186.5129928588867,186.5129928588867,186.8612976074219,186.8612976074219,187.1837158203125,187.4561614990234,187.7289733886719,188.0019302368164,188.0019302368164,188.2746505737305,188.5470962524414,188.821891784668,189.0969390869141,189.1349792480469,189.1349792480469,189.1349792480469,186.1295471191406,186.1295471191406,186.474723815918,186.8129959106445,186.8129959106445,187.1600952148438,187.1600952148438,187.1600952148438,187.4990997314453,187.4990997314453,187.8415069580078,187.8415069580078,188.1832809448242,188.1832809448242,188.5250930786133,188.5250930786133,188.8701400756836,188.8701400756836,189.1983108520508,189.2284240722656,189.2284240722656,189.2284240722656,186.2850646972656,186.6230316162109,186.9715270996094,187.3182220458984,187.3182220458984,187.3182220458984,187.6628799438477,187.6628799438477,188.0026168823242,188.0026168823242,188.3442230224609,188.3442230224609,188.6843032836914,188.6843032836914,189.0298080444336,189.0298080444336,189.3203811645508,189.3203811645508,189.3203811645508,189.3203811645508,186.5095901489258,186.5095901489258,186.8486785888672,187.1985244750977,187.1985244750977,187.5419311523438,187.5419311523438,187.8846969604492,188.226448059082,188.226448059082,188.5696792602539,188.9126129150391,188.9126129150391,189.2505645751953,189.2505645751953,189.4107513427734,189.4107513427734,189.4107513427734,186.4323272705078,186.7846145629883,187.1366348266602,187.1366348266602,187.4821472167969,187.4821472167969,187.822624206543,188.1633987426758,188.507682800293,188.507682800293,188.8465347290039,189.1953048706055,189.1953048706055,189.4997711181641,189.4997711181641,189.4997711181641,189.4997711181641,189.4997711181641,189.4997711181641,186.7692413330078,186.7692413330078,187.1098403930664,187.4604415893555,187.4604415893555,187.7970733642578,188.1365661621094,188.1365661621094,188.4769744873047,188.4769744873047,188.8235473632812,188.8235473632812,189.1648406982422,189.5047378540039,189.5047378540039,189.587272644043,189.587272644043,189.587272644043,186.7864990234375,186.7864990234375,187.1203308105469,187.4712371826172,187.4712371826172,187.8112945556641,187.8112945556641,188.15380859375,188.15380859375,188.4962158203125,188.4962158203125,188.8392944335938,189.1819915771484,189.5220336914062,189.5220336914062,189.6734466552734,189.6734466552734,189.6734466552734,186.8183212280273,186.8183212280273,187.1635131835938,187.1635131835938,187.5135650634766,187.5135650634766,187.5135650634766,187.8545608520508,188.1958084106445,188.1958084106445,188.5370941162109,188.5370941162109,188.8800430297852,189.2223281860352,189.2223281860352,189.5641021728516,189.7581024169922,189.7581024169922,189.7581024169922,186.9101486206055,186.9101486206055,187.2555618286133,187.6097717285156,187.6097717285156,187.956184387207,187.956184387207,188.2928009033203,188.6294631958008,188.9711303710938,188.9711303710938,189.3136596679688,189.3136596679688,189.6577529907227,189.6577529907227,189.8414993286133,189.8414993286133,189.8414993286133,187.0520401000977,187.0520401000977,187.3972625732422,187.7472610473633,188.0895156860352,188.427131652832,188.7713928222656,188.7713928222656,189.1182556152344,189.1182556152344,189.4662246704102,189.4662246704102,189.8040161132812,189.8040161132812,189.9235305786133,189.9235305786133,189.9235305786133,187.2369155883789,187.2369155883789,187.5594711303711,187.5594711303711,187.9090194702148,188.2488632202148,188.2488632202148,188.587516784668,188.9313430786133,189.2766876220703,189.6221389770508,189.6221389770508,189.9550018310547,189.9550018310547,190.0041580200195,190.0041580200195,190.0041580200195,187.4412384033203,187.4412384033203,187.7905654907227,188.1382141113281,188.1382141113281,188.4754791259766,188.8176574707031,189.1610870361328,189.1610870361328,189.1610870361328,189.5058746337891,189.849479675293,189.849479675293,189.849479675293,190.0835647583008,190.0835647583008,190.0835647583008,187.365364074707,187.7143173217773,187.7143173217773,188.0610580444336,188.0610580444336,188.4012756347656,188.4012756347656,188.4012756347656,188.7369766235352,188.7369766235352,189.0796890258789,189.0796890258789,189.4228668212891,189.4228668212891,189.7708511352539,189.7708511352539,190.10302734375,190.10302734375,190.1616439819336,190.1616439819336,190.1616439819336,187.6678924560547,187.6678924560547,188.0164031982422,188.0164031982422,188.3595275878906,188.6981353759766,189.039909362793,189.039909362793,189.3862838745117,189.3862838745117,189.7298812866211,189.7298812866211,190.0749053955078,190.0749053955078,190.2384643554688,190.2384643554688,187.6816482543945,187.6816482543945,188.0287399291992,188.0287399291992,188.3725509643555,188.7127304077148,188.7127304077148,189.0512924194336,189.3951797485352,189.3951797485352,189.7406692504883,189.7406692504883,190.0868835449219,190.0868835449219,190.3141250610352,190.3141250610352,187.7305450439453,188.0779876708984,188.4236297607422,188.7601318359375,189.0741348266602,189.4037780761719,189.4037780761719,189.7513275146484,189.7513275146484,190.0992965698242,190.0992965698242,190.3884811401367,190.3884811401367,190.3884811401367,190.3884811401367,190.3884811401367,190.3884811401367,188.1274108886719,188.4688568115234,188.4688568115234,188.4688568115234,188.8115539550781,188.8115539550781,189.1502456665039,189.1502456665039,189.4929656982422,189.4929656982422,189.8366546630859,190.1837692260742,190.1837692260742,190.1837692260742,190.4617004394531,190.4617004394531,190.4617004394531,190.4617004394531,190.4617004394531,190.4617004394531,188.2523803710938,188.2523803710938,188.5929946899414,188.5929946899414,188.9356994628906,188.9356994628906,189.2780609130859,189.2780609130859,189.2780609130859,189.6183090209961,189.6183090209961,189.9615173339844,190.3066940307617,190.3066940307617,190.5337142944336,190.5337142944336,188.0734558105469,188.0734558105469,188.4107208251953,188.4107208251953,188.7500305175781,189.091926574707,189.091926574707,189.4294128417969,189.4294128417969,189.7708435058594,189.7708435058594,189.7708435058594,190.1119842529297,190.1119842529297,190.454475402832,190.6045532226562,190.6045532226562,190.6045532226562,188.2433853149414,188.2433853149414,188.5793151855469,188.9151611328125,188.9151611328125,189.2570037841797,189.2570037841797,189.5940246582031,189.5940246582031,189.9369354248047,189.9369354248047,190.2830123901367,190.6230316162109,190.6230316162109,190.6743011474609,190.6743011474609,190.6743011474609,188.4593276977539,188.4593276977539,188.7950592041016,188.7950592041016,189.1366653442383,189.4765777587891,189.4765777587891,189.8168106079102,190.1604537963867,190.1604537963867,190.5059051513672,190.5059051513672,190.7428512573242,190.7428512573242,190.7428512573242,190.7428512573242,190.7428512573242,190.7428512573242,190.7428512573242,190.7428512573242,190.7428512573242,190.7428512573242,190.7428512573242,190.7428512573242,190.7428512573242,190.7428512573242,190.7428512573242,190.7428512573242,190.7428512573242,190.7428512573242,188.3822860717773,188.3822860717773,188.3822860717773,188.679328918457,188.679328918457,189.0099105834961,189.0099105834961,189.3369522094727,189.6646118164062,189.9978408813477,190.3319625854492,190.3319625854492,190.6674575805664,190.8099746704102,190.8099746704102,190.8099746704102,188.5795593261719,188.917350769043,189.259880065918,189.6030426025391,189.6030426025391,189.9459686279297,189.9459686279297,190.2881011962891,190.2881011962891,190.6332855224609,190.6332855224609,190.6332855224609,190.8763580322266,190.8763580322266,190.8763580322266,190.8763580322266,190.8763580322266,190.8763580322266,188.9244995117188,188.9244995117188,189.2593231201172,189.2593231201172,189.5826034545898,189.5826034545898,189.9213790893555,190.264274597168,190.264274597168,190.6102523803711,190.9416656494141,190.9416656494141,190.9416656494141,190.9416656494141,188.9397048950195,189.2735748291016,189.2735748291016,189.6184387207031,189.6184387207031,189.9600601196289,189.9600601196289,190.3039779663086,190.3039779663086,190.3039779663086,190.647087097168,190.9944915771484,190.9944915771484,190.9944915771484,191.0059356689453,191.0059356689453,189.0127944946289,189.0127944946289,189.341438293457,189.341438293457,189.6792449951172,189.6792449951172,190.0137176513672,190.0137176513672,190.0137176513672,190.3527755737305,190.3527755737305,190.6949081420898,190.6949081420898,191.0402221679688,191.0402221679688,191.0691909790039,191.0691909790039,191.0691909790039,189.0797424316406,189.0797424316406,189.0797424316406,189.4120788574219,189.4120788574219,189.7540664672852,189.7540664672852,190.0979995727539,190.439323425293,190.439323425293,190.7865676879883,191.1313934326172,191.1313934326172,191.1313934326172,191.1313934326172,191.1313934326172,191.1313934326172,189.2023773193359,189.2023773193359,189.5364685058594,189.5364685058594,189.8805770874023,190.2174072265625,190.5588073730469,190.5588073730469,190.9043045043945,191.192626953125,191.192626953125,191.192626953125,191.192626953125,191.192626953125,191.192626953125,189.3681564331055,189.7065277099609,189.7065277099609,190.0503311157227,190.3919143676758,190.3919143676758,190.7365875244141,190.7365875244141,191.0785522460938,191.252815246582,191.252815246582,191.252815246582,189.2308807373047,189.2308807373047,189.5638961791992,189.5638961791992,189.9076309204102,189.9076309204102,190.2489471435547,190.2489471435547,190.5893783569336,190.5893783569336,190.9331130981445,191.2797088623047,191.2797088623047,191.312141418457,191.312141418457,189.4669570922852,189.4669570922852,189.4669570922852,189.801399230957,189.801399230957,190.1476745605469,190.4878463745117,190.4878463745117,190.8287963867188,191.1744995117188,191.1744995117188,191.3703765869141,191.3703765869141,191.3703765869141,189.3956604003906,189.3956604003906,189.7290573120117,189.7290573120117,189.7290573120117,190.0733108520508,190.4172744750977,190.4172744750977,190.758544921875,190.758544921875,191.1052856445312,191.1052856445312,191.4278259277344,191.4278259277344,191.4278259277344,191.4278259277344,191.4278259277344,191.4278259277344,189.6958389282227,189.6958389282227,190.0329513549805,190.0329513549805,190.3781127929688,190.3781127929688,190.3781127929688,190.7206420898438,190.7206420898438,191.0649261474609,191.0649261474609,191.411003112793,191.411003112793,191.4841842651367,191.4841842651367,189.674560546875,189.674560546875,189.674560546875,190.0056762695312,190.0056762695312,190.3501205444336,190.3501205444336,190.6935272216797,191.0367813110352,191.0367813110352,191.3818359375,191.5397338867188,191.5397338867188,191.5397338867188,189.6862335205078,190.0232925415039,190.0232925415039,190.3693466186523,190.3693466186523,190.7118835449219,190.7118835449219,191.0511932373047,191.0511932373047,191.3956069946289,191.5943374633789,191.5943374633789,191.5943374633789,189.7292785644531,190.061408996582,190.061408996582,190.061408996582,190.4053726196289,190.4053726196289,190.7498016357422,190.7498016357422,191.0919952392578,191.0919952392578,191.4398956298828,191.648063659668,191.648063659668,191.648063659668,191.648063659668,189.8215942382812,189.8215942382812,190.1569290161133,190.1569290161133,190.5021133422852,190.5021133422852,190.8453903198242,191.1876831054688,191.1876831054688,191.5353240966797,191.5353240966797,191.7009582519531,191.7009582519531,191.7009582519531,189.9398651123047,189.9398651123047,190.2732086181641,190.623161315918,190.623161315918,190.9674606323242,191.3117218017578,191.3117218017578,191.6582641601562,191.6582641601562,191.7528915405273,191.7528915405273,190.0832366943359,190.0832366943359,190.4209518432617,190.7663650512695,190.7663650512695,191.1092147827148,191.4505310058594,191.4505310058594,191.7965698242188,191.7965698242188,191.8041152954102,191.8041152954102,191.8041152954102,190.246711730957,190.246711730957,190.5858612060547,190.9315948486328,190.9315948486328,191.2496032714844,191.2496032714844,191.5906829833984,191.5906829833984,191.8544387817383,191.8544387817383,191.8544387817383,191.8544387817383,191.8544387817383,191.8544387817383,190.390869140625,190.390869140625,190.7319488525391,190.7319488525391,191.0748443603516,191.0748443603516,191.4169845581055,191.7595138549805,191.7595138549805,191.9039535522461,191.9039535522461,191.9039535522461,190.2563323974609,190.5927505493164,190.5927505493164,190.9396667480469,190.9396667480469,191.2811584472656,191.2811584472656,191.6205139160156,191.9527053833008,191.9527053833008,191.9527053833008,191.9527053833008,191.9527053833008,191.9527053833008,191.9527053833008,191.9527053833008,191.9527053833008,191.9527053833008,191.9527053833008,191.9527053833008,191.9527053833008,191.9527053833008,191.9527053833008,191.9527053833008,191.9527053833008,191.9527053833008,190.5643920898438,190.5643920898438,190.907112121582,190.907112121582,191.2492904663086,191.2492904663086,191.5920257568359,191.5920257568359,191.9311447143555,192.0005035400391,192.0005035400391,192.0005035400391,190.4711074829102,190.4711074829102,190.8004150390625,191.1422576904297,191.1422576904297,191.4809341430664,191.4809341430664,191.8194274902344,191.8194274902344,191.8194274902344,192.0477142333984,192.0477142333984,192.0477142333984,192.0477142333984,192.0477142333984,192.0477142333984,190.7306671142578,191.0747222900391,191.0747222900391,191.4187316894531,191.7594375610352,191.7594375610352,192.0941162109375,192.0941162109375,192.0941162109375,192.0941162109375,190.7000503540039,190.7000503540039,191.0386734008789,191.0386734008789,191.3862762451172,191.7284545898438,191.7284545898438,192.0705795288086,192.1398315429688,192.1398315429688,192.1398315429688,190.6873779296875,191.0254898071289,191.0254898071289,191.3732986450195,191.3732986450195,191.7157669067383,191.7157669067383,192.0593643188477,192.0593643188477,192.1848297119141,192.1848297119141,192.1848297119141,190.7086181640625,190.7086181640625,190.7086181640625,191.0437545776367,191.393196105957,191.393196105957,191.7367782592773,192.0803680419922,192.2289810180664,192.2289810180664,192.2289810180664,190.7469253540039,190.7469253540039,191.0845413208008,191.0845413208008,191.4330902099609,191.7801513671875,191.7801513671875,192.1224670410156,192.2725372314453,192.2725372314453,192.2725372314453,192.2725372314453,190.8275604248047,190.8275604248047,191.1665802001953,191.1665802001953,191.5166168212891,191.5166168212891,191.8616256713867,191.8616256713867,192.2052307128906,192.2052307128906,192.3153839111328,192.3153839111328,190.9321517944336,190.9321517944336,191.2717361450195,191.6236724853516,191.9657135009766,191.9657135009766,192.3073501586914,192.3073501586914,192.3073501586914,192.3574066162109,192.3574066162109,191.0451278686523,191.0451278686523,191.3848342895508,191.7330474853516,192.0764236450195,192.0764236450195,192.0764236450195,192.39892578125,192.39892578125,192.39892578125,192.39892578125,192.39892578125,192.39892578125,191.173454284668,191.5173568725586,191.5173568725586,191.5173568725586,191.8658218383789,191.8658218383789,192.2081909179688,192.2081909179688,192.4396438598633,192.4396438598633,192.4396438598633,192.4396438598633,192.4396438598633,192.4396438598633,191.3311004638672,191.3311004638672,191.6817779541016,192.0294494628906,192.3700790405273,192.4797668457031,192.4797668457031,192.4797668457031,191.1901626586914,191.1901626586914,191.5342712402344,191.5342712402344,191.8849258422852,191.8849258422852,192.2330322265625,192.2330322265625,192.5192337036133,192.5192337036133,192.5192337036133,192.5192337036133,192.5192337036133,192.5192337036133,191.4172668457031,191.4172668457031,191.4172668457031,191.7668075561523,191.7668075561523,192.115364074707,192.4587173461914,192.4587173461914,192.4587173461914,192.5580291748047,192.5580291748047,192.5580291748047,191.3143615722656,191.3143615722656,191.6584396362305,191.6584396362305,192.0095443725586,192.0095443725586,192.3540573120117,192.3540573120117,192.5962219238281,192.5962219238281,192.5962219238281,192.5962219238281,192.5962219238281,192.5962219238281,191.5771636962891,191.5771636962891,191.9263610839844,192.2734527587891,192.6117324829102,192.6117324829102,192.6117324829102,192.6338272094727,192.6338272094727,192.6338272094727,191.5142135620117,191.5142135620117,191.8635406494141,192.2156524658203,192.5603866577148,192.5603866577148,192.6707763671875,192.6707763671875,192.6707763671875,191.4811859130859,191.4811859130859,191.8257217407227,192.1792678833008,192.1792678833008,192.5280914306641,192.5280914306641,192.7071228027344,192.7071228027344,192.7071228027344,192.7071228027344,192.7071228027344,192.7071228027344,192.7071228027344,192.7071228027344,192.7071228027344,192.7071228027344,192.7071228027344,192.7071228027344,191.6641311645508,192.0104064941406,192.0104064941406,192.3519973754883,192.3519973754883,192.6905288696289,192.6905288696289,192.7427825927734,192.7427825927734,192.7427825927734,192.7427825927734,192.7427825927734,192.7427825927734,192.7427825927734,192.7427825927734,192.7427825927734,192.7427825927734,192.7427825927734,192.7427825927734,192.7427825927734,192.7427825927734,192.7427825927734,192.7427825927734,192.7427825927734,192.7427825927734,192.7427825927734,192.7427825927734,192.7427825927734,192.7427825927734,192.7427825927734,192.7427825927734,192.7427825927734,192.7427825927734,192.7427825927734,192.7427825927734,192.7427825927734,192.7427825927734,192.7427825927734,192.7427825927734,192.7427825927734,192.7427825927734,192.7427825927734,192.7427825927734,192.7427825927734,192.7427825927734,192.7427825927734,192.7427825927734,192.7427825927734,192.7427825927734,192.7427825927734,192.7427825927734,191.510856628418,191.510856628418,191.7790145874023,191.7790145874023,191.7790145874023,192.1325836181641,192.1325836181641,192.4726715087891,192.4726715087891,192.7910232543945,193.1255874633789,193.4582901000977,193.7744979858398,193.7744979858398,194.0508880615234,194.0508880615234,194.3258438110352,194.6004791259766,194.6004791259766,194.8789901733398,194.8789901733398,195.1566009521484,195.1566009521484,195.4360809326172,195.7161407470703,195.995849609375,195.995849609375,196.2759094238281,196.2759094238281,196.5517807006836,196.5517807006836,196.5517807006836,196.8251953125,196.8251953125,196.8711776733398,196.8711776733398,196.8711776733398,191.8197631835938,191.8197631835938,192.1912460327148,192.1912460327148,192.5450057983398,192.5450057983398,192.8702163696289,193.216552734375,193.216552734375,193.5629272460938,193.5629272460938,193.9077377319336,194.2551956176758,194.2551956176758,194.6014709472656,194.947624206543,194.947624206543,195.2976989746094,195.2976989746094,195.6472702026367,195.6472702026367,195.996452331543,195.996452331543,196.3473968505859,196.3473968505859,196.6936340332031,196.6936340332031,197.0178909301758,197.0178909301758,197.0178909301758,197.0178909301758,197.0178909301758,197.0178909301758,192.1003036499023,192.1003036499023,192.4675445556641,192.4675445556641,192.8067016601562,192.8067016601562,193.1415100097656,193.4858245849609,193.4858245849609,193.4858245849609,193.8350143432617,193.8350143432617,193.8350143432617,194.182991027832,194.182991027832,194.5321578979492,194.8831100463867,195.2316055297852,195.2316055297852,195.5799942016602,195.9273681640625,195.9273681640625,196.2765884399414,196.2765884399414,196.6256484985352,196.6256484985352,196.9641494750977,197.1620635986328,197.1620635986328,197.1620635986328,197.1620635986328,197.1620635986328,197.1620635986328,192.4487991333008,192.8070755004883,192.8070755004883,192.8070755004883,193.1341323852539,193.483154296875,193.483154296875,193.8264236450195,193.8264236450195,194.1707382202148,194.5130920410156,194.857666015625,194.857666015625,195.202995300293,195.202995300293,195.547981262207,195.8944320678711,195.8944320678711,196.2433624267578,196.5916061401367,196.9353103637695,196.9353103637695,197.2651901245117,197.3040084838867,197.3040084838867,197.3040084838867,197.3040084838867,197.3040084838867,197.3040084838867,197.3040084838867,197.3040084838867,197.3040084838867,192.4605560302734,192.4605560302734,192.8325653076172,192.8325653076172,193.1594772338867,193.1594772338867,193.4799499511719,193.8160934448242,193.8160934448242,194.1519546508789,194.1519546508789,194.4898071289062,194.4898071289062,194.8286056518555,194.8286056518555,195.1617126464844,195.5017852783203,195.8353118896484,195.8353118896484,196.1738128662109,196.1738128662109,196.1738128662109,196.5132293701172,196.8570938110352,196.8570938110352,197.1993408203125,197.1993408203125,197.4435501098633,197.4435501098633,197.4435501098633,197.4435501098633,197.4435501098633,197.4435501098633,192.8289566040039,192.8289566040039,193.1842727661133,193.1842727661133,193.5178070068359,193.5178070068359,193.8620910644531,193.8620910644531,194.2008285522461,194.5440139770508,194.5440139770508,194.8876419067383,195.2327346801758,195.5563278198242,195.5563278198242,195.901123046875,195.901123046875,196.2447738647461,196.590934753418,196.590934753418,196.9398040771484,196.9398040771484,196.9398040771484,197.2863616943359,197.2863616943359,197.5809555053711,197.5809555053711,197.5809555053711,197.5809555053711,192.9814682006836,192.9814682006836,193.3380355834961,193.6720886230469,193.6720886230469,194.01904296875,194.01904296875,194.3614120483398,194.7074432373047,194.7074432373047,195.0528945922852,195.0528945922852,195.3976516723633,195.7437438964844,196.0889205932617,196.0889205932617,196.4342956542969,196.4342956542969,196.7799530029297,196.7799530029297,197.1261825561523,197.1261825561523,197.4740142822266,197.7161102294922,197.7161102294922,197.7161102294922,197.7161102294922,197.7161102294922,197.7161102294922,193.2584838867188,193.6014099121094,193.6014099121094,193.9409255981445,193.9409255981445,194.2820816040039,194.2820816040039,194.6245651245117,194.6245651245117,194.9641342163086,194.9641342163086,195.3068618774414,195.3068618774414,195.6514739990234,195.6514739990234,195.9985809326172,195.9985809326172,196.3446578979492,196.6926193237305,197.0409317016602,197.0409317016602,197.3893890380859,197.3893890380859,197.3893890380859,197.7382125854492,197.8491287231445,197.8491287231445,197.8491287231445,197.8491287231445,197.8491287231445,197.8491287231445,193.6092758178711,193.9454803466797,193.9454803466797,194.2904205322266,194.2904205322266,194.6331100463867,194.6331100463867,194.9752426147461,195.3187561035156,195.3187561035156,195.6645736694336,195.6645736694336,196.0128784179688,196.0128784179688,196.3598251342773,196.3598251342773,196.3598251342773,196.7035751342773,196.7035751342773,197.0488891601562,197.3979339599609,197.3979339599609,197.7408676147461,197.97998046875,197.97998046875,197.97998046875,197.97998046875,197.97998046875,197.97998046875,193.6562271118164,193.9948272705078,193.9948272705078,194.3465270996094,194.3465270996094,194.6891860961914,195.0280990600586,195.3686752319336,195.3686752319336,195.7109985351562,195.7109985351562,196.0541152954102,196.3971405029297,196.3971405029297,196.7403259277344,196.7403259277344,197.0834197998047,197.0834197998047,197.4322738647461,197.4322738647461,197.7817916870117,197.7817916870117,198.1087036132812,198.1087036132812,198.1087036132812,198.1087036132812,198.1087036132812,198.1087036132812,193.7564849853516,193.7564849853516,194.1034164428711,194.1034164428711,194.4475860595703,194.78759765625,194.78759765625,195.1273040771484,195.467903137207,195.8085174560547,195.8085174560547,196.1549453735352,196.1549453735352,196.4985122680664,196.4985122680664,196.4985122680664,196.8433074951172,196.8433074951172,196.8433074951172,197.1894989013672,197.5404739379883,197.5404739379883,197.8863143920898,197.8863143920898,198.2176132202148,198.2176132202148,198.2353515625,198.2353515625,198.2353515625,193.9192428588867,193.9192428588867,194.2678604125977,194.2678604125977,194.6188888549805,194.9603576660156,195.2986297607422,195.2986297607422,195.2986297607422,195.6320114135742,195.6320114135742,195.9721527099609,196.3148574829102,196.6610717773438,197.0088729858398,197.3550262451172,197.3550262451172,197.6942291259766,197.6942291259766,198.0385131835938,198.0385131835938,198.359977722168,198.359977722168,198.359977722168,198.359977722168,198.359977722168,198.359977722168,194.122932434082,194.122932434082,194.4705352783203,194.8201065063477,194.8201065063477,195.1603546142578,195.1603546142578,195.5004730224609,195.837532043457,195.837532043457,196.1785125732422,196.5243988037109,196.8662033081055,197.2095413208008,197.5540008544922,197.9025650024414,197.9025650024414,198.2483749389648,198.2483749389648,198.4825134277344,198.4825134277344,198.4825134277344,198.4825134277344,194.4370956420898,194.4370956420898,194.7840270996094,194.7840270996094,194.7840270996094,195.1330261230469,195.1330261230469,195.4678573608398,195.4678573608398,195.801399230957,195.801399230957,196.1415100097656,196.1415100097656,196.4856491088867,196.8311538696289,196.8311538696289,197.1741638183594,197.1741638183594,197.5023040771484,197.5023040771484,197.8499069213867,197.8499069213867,198.1948928833008,198.1948928833008,198.5290145874023,198.5290145874023,198.6031951904297,198.6031951904297,198.6031951904297,198.6031951904297,194.7722244262695,195.1242446899414,195.1242446899414,195.4663619995117,195.7985992431641,195.7985992431641,196.1372528076172,196.1372528076172,196.4766616821289,196.4766616821289,196.4766616821289,196.8174667358398,196.8174667358398,197.1647415161133,197.5138626098633,197.5138626098633,197.8627090454102,197.8627090454102,198.2079620361328,198.5512771606445,198.7218551635742,198.7218551635742,198.7218551635742,198.7218551635742,198.7218551635742,198.7218551635742,194.8692626953125,194.8692626953125,195.2167587280273,195.2167587280273,195.5596084594727,195.5596084594727,195.8912506103516,195.8912506103516,196.2260437011719,196.2260437011719,196.5666427612305,196.5666427612305,196.9109497070312,196.9109497070312,197.2601928710938,197.6075134277344,197.9601669311523,198.3073806762695,198.3073806762695,198.6535797119141,198.8386001586914,198.8386001586914,198.8386001586914,198.8386001586914,195.0279693603516,195.0279693603516,195.3707046508789,195.3707046508789,195.7080383300781,196.0378036499023,196.3775787353516,196.3775787353516,196.7170715332031,196.7170715332031,197.0603713989258,197.0603713989258,197.4056549072266,197.4056549072266,197.7530822753906,197.7530822753906,198.1017684936523,198.1017684936523,198.4501266479492,198.4501266479492,198.7901840209961,198.7901840209961,198.9535293579102,198.9535293579102,198.9535293579102,198.9535293579102,198.9535293579102,198.9535293579102,195.2200469970703,195.2200469970703,195.5597839355469,195.5597839355469,195.8948287963867,196.221794128418,196.5596160888672,196.5596160888672,196.9005737304688,196.9005737304688,196.9005737304688,197.2410354614258,197.5838394165039,197.9279937744141,197.9279937744141,198.2717208862305,198.2717208862305,198.6183395385742,198.9543533325195,198.9543533325195,199.0664825439453,199.0664825439453,199.0664825439453,199.0664825439453,199.0664825439453,199.0664825439453,195.4264831542969,195.4264831542969,195.4264831542969,195.7676162719727,195.7676162719727,196.0994262695312,196.0994262695312,196.4314346313477,196.4314346313477,196.4314346313477,196.7689743041992,197.1117324829102,197.1117324829102,197.4546127319336,197.8008499145508,197.8008499145508,197.8008499145508,198.1465835571289,198.4971923828125,198.8463516235352,198.8463516235352,199.1776504516602,199.1776504516602,199.1776504516602,199.1776809692383,199.1776809692383,195.3873748779297,195.7300262451172,195.7300262451172,196.0683670043945,196.0683670043945,196.3980484008789,196.3980484008789,196.7333831787109,196.7333831787109,197.0746994018555,197.0746994018555,197.416862487793,197.7644805908203,198.112174987793,198.4583129882812,198.4583129882812,198.8068695068359,198.8068695068359,199.1467208862305,199.1467208862305,199.2871017456055,199.2871017456055,199.2871017456055,199.2871017456055,199.2871017456055,199.2871017456055,195.7584228515625,195.7584228515625,196.0942687988281,196.0942687988281,196.4248504638672,196.4248504638672,196.7570419311523,196.7570419311523,197.0947723388672,197.4328231811523,197.4328231811523,197.7766036987305,197.7766036987305,198.1182632446289,198.4698715209961,198.4698715209961,198.812385559082,198.812385559082,199.1577835083008,199.3946685791016,199.3946685791016,199.3946685791016,199.3946685791016,199.3946685791016,199.3946685791016,195.8252258300781,196.1623153686523,196.4936752319336,196.8262481689453,196.8262481689453,197.1672210693359,197.1672210693359,197.5103225708008,197.8549270629883,197.8549270629883,197.8549270629883,198.2016296386719,198.2016296386719,198.5508651733398,198.5508651733398,198.9021530151367,198.9021530151367,198.9021530151367,199.2491149902344,199.5005722045898,199.5005722045898,199.5005722045898,199.5005722045898,195.9217224121094,196.2557525634766,196.2557525634766,196.5854568481445,196.5854568481445,196.9180526733398,197.2412109375,197.5762405395508,197.5762405395508,197.9226531982422,198.265007019043,198.5932769775391,198.5932769775391,198.5932769775391,198.9396438598633,198.9396438598633,199.2876586914062,199.2876586914062,199.6047439575195,199.6047439575195,199.6047439575195,199.6047439575195,199.6047439575195,199.6047439575195,196.0388870239258,196.0388870239258,196.3787612915039,196.3787612915039,196.7095336914062,196.7095336914062,197.0404815673828,197.3774719238281,197.7218856811523,197.7218856811523,198.0665512084961,198.0665512084961,198.4092712402344,198.7526168823242,198.7526168823242,199.1002578735352,199.1002578735352,199.4465026855469,199.7072296142578,199.7072296142578,199.7072296142578,199.7072296142578,199.7072296142578,199.7072296142578,196.2764129638672,196.6055145263672,196.6055145263672,196.9322891235352,197.2614288330078,197.2614288330078,197.6051177978516,197.9499816894531,197.9499816894531,198.2963714599609,198.6443557739258,198.6443557739258,198.9940643310547,198.9940643310547,199.3413314819336,199.3413314819336,199.685791015625,199.8081130981445,199.8081130981445,199.8081130981445,199.8081130981445,199.8081130981445,199.8081130981445,199.8081130981445,199.8081130981445,199.8081130981445,199.8081130981445,199.8081130981445,199.8081130981445,199.8081130981445,199.8081130981445,199.8081130981445,199.8081130981445,199.8081130981445,199.8081130981445,199.8081130981445,199.8081130981445,199.8081130981445,199.8081130981445,199.8081130981445,199.8081130981445,199.8081130981445,199.8081130981445,199.8081130981445,199.8081130981445,199.8081130981445,199.8081130981445,196.4713439941406,196.8026962280273,196.8026962280273,197.1254119873047,197.1254119873047,197.4589767456055,197.4589767456055,197.7939605712891,198.1353149414062,198.1353149414062,198.4794921875,198.823127746582,199.1657257080078,199.5138168334961,199.5138168334961,199.8520126342773,199.8520126342773,199.9070129394531,199.9070129394531,199.9070129394531,199.9070129394531,196.7929840087891,197.1198272705078,197.4524841308594,197.7889862060547,198.1288375854492,198.1288375854492,198.4723510742188,198.8172073364258,199.1665802001953,199.1665802001953,199.5115814208984,199.5115814208984,199.8569183349609,199.8569183349609,200.0046691894531,200.0046691894531,200.0046691894531,200.0046691894531,200.0046691894531,200.0046691894531,196.8502883911133,196.8502883911133,197.1783752441406,197.5102767944336,197.8457260131836,197.8457260131836,198.18701171875,198.18701171875,198.5306167602539,198.5306167602539,198.8754196166992,198.8754196166992,199.2215728759766,199.5678329467773,199.9103622436523,200.1007766723633,200.1007766723633,200.1007766723633,200.1007766723633,200.1007766723633,200.1007766723633,196.9552841186523,196.9552841186523,197.2846527099609,197.2846527099609,197.6163024902344,197.9522933959961,198.2936401367188,198.2936401367188,198.6359939575195,198.6359939575195,198.9811706542969,198.9811706542969,199.3317947387695,199.3317947387695,199.6804656982422,199.6804656982422,200.0220947265625,200.0220947265625,200.1952896118164,200.1952896118164,200.1952896118164,200.1952896118164,200.1952896118164,200.1952896118164,197.117057800293,197.4463195800781,197.7780990600586,197.7780990600586,197.7780990600586,198.1143569946289,198.4557647705078,198.4557647705078,198.8005752563477,199.1450347900391,199.1450347900391,199.493766784668,199.493766784668,199.8436737060547,200.1878890991211,200.1878890991211,200.2882766723633,200.2882766723633,200.2882766723633,200.2882766723633,200.2882766723633,200.2882766723633,197.3403396606445,197.3403396606445,197.6695327758789,197.6695327758789,198.0070190429688,198.3459625244141,198.3459625244141,198.6889114379883,199.0341796875,199.3800964355469,199.3800964355469,199.7285995483398,199.7285995483398,200.0840759277344,200.0840759277344,200.0840759277344,200.3797454833984,200.3797454833984,200.3797454833984,200.3797454833984,200.3797454833984,200.3797454833984,197.2871780395508,197.2871780395508,197.6174163818359,197.6174163818359,197.9520492553711,197.9520492553711,198.2873458862305,198.2873458862305,198.6264038085938,198.6264038085938,198.9743194580078,198.9743194580078,199.3194808959961,199.3194808959961,199.6653823852539,199.6653823852539,200.0166702270508,200.0166702270508,200.3558578491211,200.3558578491211,200.4697494506836,200.4697494506836,200.4697494506836,200.4697494506836,200.4697494506836,200.4697494506836,197.5987319946289,197.5987319946289,197.9107666015625,197.9107666015625,198.2407836914062,198.2407836914062,198.5781021118164,198.9225082397461,198.9225082397461,199.2670211791992,199.6118316650391,199.9593811035156,199.9593811035156,200.307373046875,200.307373046875,200.307373046875,200.5583038330078,200.5583038330078,200.5583038330078,200.5583038330078,200.5583038330078,200.5583038330078,197.5658493041992,197.8991470336914,198.2323303222656,198.2323303222656,198.5743103027344,198.9132232666016,199.2548370361328,199.2548370361328,199.5947036743164,199.5947036743164,199.9383392333984,199.9383392333984,200.2862701416016,200.2862701416016,200.624397277832,200.624397277832,200.6454544067383,200.6454544067383,200.6454544067383,200.6454544067383,200.6454544067383,200.6454544067383,197.943489074707,197.943489074707,198.2742538452148,198.2742538452148,198.6110076904297,198.6110076904297,198.9498519897461,198.9498519897461,199.2925415039062,199.6377487182617,199.6377487182617,199.9865646362305,199.9865646362305,200.3381576538086,200.6767654418945,200.6767654418945,200.7311172485352,200.7311172485352,200.7311172485352,200.7311172485352,200.7311172485352,200.7311172485352,198.0429229736328,198.3750915527344,198.3750915527344,198.7138977050781,198.7138977050781,199.0536880493164,199.3984832763672,199.7418212890625,199.7418212890625,200.0901718139648,200.0901718139648,200.4403991699219,200.4403991699219,200.7813339233398,200.7813339233398,200.8155059814453,200.8155059814453,200.8155059814453,200.8155059814453,198.2176971435547,198.2176971435547,198.5521545410156,198.5521545410156,198.8938293457031,198.8938293457031,199.2360076904297,199.2360076904297,199.5794296264648,199.5794296264648,207.5419235229492,207.5419235229492,207.5419235229492,207.5419235229492,207.5419235229492,207.5419235229492,207.5419235229492,207.5419235229492,207.5419235229492,207.5419235229492,207.5419235229492,207.5419235229492,215.1713180541992,215.1713180541992,215.1713485717773,215.1713485717773,215.1713485717773,215.1713485717773,215.1713485717773,215.1713485717773,215.1713485717773,215.1713485717773,215.1713485717773,215.1713485717773,215.1713485717773,215.1713485717773,215.1713485717773,215.1713485717773,230.4301376342773,230.4301376342773,230.4301376342773,230.4301376342773,230.4301376342773,230.4301376342773,230.4301376342773,230.4301376342773,230.4301376342773,230.4301376342773],"meminc":[0,0,0,0,15.25894927978516,0,0,0,0,30.03299713134766,0,0,0,0,0,0,0,0,0,0,0,-0.00060272216796875,0,0,0,0,0,0,0,15.35749053955078,0.3591995239257812,0,0.3466720581054688,0,0.3332672119140625,0,0.333892822265625,0.29205322265625,0,0.1963272094726562,0,0,-1.737838745117188,0,0.3533935546875,0.3429718017578125,0.338531494140625,0.3406600952148438,0,0.3362197875976562,0,0,0.06035614013671875,0,0,-1.506179809570312,0,0.349212646484375,0,0.3432159423828125,0,0.3397369384765625,0,0.3381271362304688,0.1879501342773438,0,0,-1.626960754394531,0.3517532348632812,0.3409500122070312,0,0.3370895385742188,0,0.3428802490234375,0,0.3055648803710938,0,0,-1.725059509277344,0.3624649047851562,0.3486862182617188,0,0.3392333984375,0,0.3390960693359375,0.336151123046875,0.0499420166015625,0,-1.4210205078125,0.34930419921875,0.3391952514648438,0,0.3382110595703125,0.34002685546875,0,0,0.1038742065429688,0,0,-1.456321716308594,0,0.3467178344726562,0,0.3372650146484375,0,0.3391952514648438,0,0.3406295776367188,0,0,0.1414108276367188,0,0,-1.470840454101562,0.3537368774414062,0,0.3402252197265625,0,0.3384857177734375,0,0.3399429321289062,0,0.1464767456054688,0,0,-1.451919555664062,0,0.3523101806640625,0,0.3409652709960938,0,0.3413314819335938,0,0.3320083618164062,0,0.1326065063476562,0,0,-1.422004699707031,0.3492813110351562,0,0,0.3397064208984375,0,0.3386688232421875,0,0.333740234375,0.1070709228515625,0,0,0,0,0,-1.60028076171875,0,0.36358642578125,0,0.3458709716796875,0,0.3402328491210938,0,0.340301513671875,0.2559585571289062,0,0,-1.499374389648438,0.3458633422851562,0.3363876342773438,0.3366317749023438,0,0.3383255004882812,0.1871719360351562,0,0,-1.411529541015625,0.3460617065429688,0.3380508422851562,0,0.3395614624023438,0,0.3343353271484375,0.09784698486328125,0,0,-1.291282653808594,0,0.3427276611328125,0,0,0.3390731811523438,0.3419265747070312,0,0.3111343383789062,0,0,-1.485435485839844,0,0,0.3546142578125,0,0.3401412963867188,0.3398513793945312,0,0.3421859741210938,0,0,0.151580810546875,0,0,-1.291679382324219,0.344970703125,0,0.3423004150390625,0,0.3441314697265625,0,0,0.302398681640625,0,-1.424461364746094,0,0.3437271118164062,0.3402862548828125,0,0,0.3381729125976562,0.3420028686523438,0.1018905639648438,0,0,-1.2081298828125,0.3401870727539062,0,0.342010498046875,0,0.343414306640625,0,0,0.2233047485351562,0,-1.307945251464844,0.3419952392578125,0.346099853515625,0.3425750732421875,0,0.317474365234375,0,0,-1.381889343261719,0.3393707275390625,0.3406219482421875,0,0.340576171875,0,0.3400726318359375,0,0.0608367919921875,0,-1.102737426757812,0,0.3403854370117188,0,0.3414535522460938,0,0.3407745361328125,0,0.1189956665039062,0,0,-1.133384704589844,0.3170700073242188,0,0.3465194702148438,0,0.3385467529296875,0.1695175170898438,0,-1.189682006835938,0,0.3306198120117188,0,0.3378372192382812,0.3421096801757812,0,0.2167739868164062,0,0,-1.207084655761719,0,0.3360137939453125,0,0.3449478149414062,0,0.3374404907226562,0,0.2257003784179688,0,0,-1.194328308105469,0.3380889892578125,0,0.348724365234375,0,0.3403778076171875,0,0,0.2035675048828125,0,0,0,-1.143379211425781,0,0,0.3342514038085938,0.3416671752929688,0,0.3409576416015625,0,0,0.1623153686523438,0,0,-1.077552795410156,0.3377456665039062,0,0.3397064208984375,0,0.3402938842773438,0,0.095062255859375,0,0,-0.9950103759765625,0,0.3448104858398438,0.34588623046875,0,0,0.3365631103515625,0,0.00244903564453125,0,0,-0.8981399536132812,0,0,0.3446273803710938,0,0,0.33868408203125,0,0,0.24896240234375,0,-1.117439270019531,0,0.3358688354492188,0.3475494384765625,0,0.3432998657226562,0.124237060546875,0,-0.9795379638671875,0.3429412841796875,0.341827392578125,0.3278732299804688,0,0,0,0,0,0,0,0,0,0,0,-0.9017181396484375,0,0,0.3443069458007812,0,0.3393402099609375,0,0.2502517700195312,0,0,0,-1.056854248046875,0,0.3382720947265625,0.34539794921875,0,0.3414764404296875,0,0.0637054443359375,0,0,-0.8570632934570312,0,0.348480224609375,0,0.342559814453125,0,0.197509765625,0,-0.9655380249023438,0,0.3395614624023438,0,0.3444900512695312,0,0.3124923706054688,0,0,-1.062789916992188,0,0,0.3278045654296875,0,0,0.347930908203125,0.3401107788085938,0,0.0774078369140625,0,0,-0.817108154296875,0,0.3467636108398438,0,0.3455657958984375,0.15478515625,0,-0.8802032470703125,0,0.3444137573242188,0,0.346923828125,0,0.2183609008789062,0,-0.9249420166015625,0.3396682739257812,0,0.345672607421875,0,0.2686691284179688,0,0,-0.9550399780273438,0,0.3358993530273438,0,0.3474197387695312,0,0.3002395629882812,0,0,-0.9656295776367188,0,0.3402252197265625,0,0,0.3469314575195312,0,0.306549072265625,0,0,0,-0.9625701904296875,0.3332977294921875,0.3396530151367188,0,0.3172760009765625,0,0,0,0,0,-0.6357955932617188,0,0.34393310546875,0.31903076171875,0,0,0,0,0,-0.6145095825195312,0.3475494384765625,0.2937469482421875,0,-0.9129104614257812,0.338897705078125,0,0.3494338989257812,0,0.250885009765625,0,0,-0.8568878173828125,0.3443145751953125,0,0.3494110107421875,0.1890945434570312,0,0,-0.7781295776367188,0.343536376953125,0,0.3477630615234375,0,0.1123199462890625,0,0,-0.6751708984375,0,0.3467254638671875,0,0.3459091186523438,0,0.007568359375,0,-0.5694580078125,0,0,0.35113525390625,0,0.2430191040039062,0,0,0,-0.7818756103515625,0.3445281982421875,0.3480758666992188,0,0.1135482788085938,0,0,-0.6642532348632812,0.3393936157226562,0,0.3445053100585938,0.00415802001953125,0,0,-0.5290451049804688,0,0.3497772216796875,0.2027969360351562,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-0.7057037353515625,0.3643646240234375,0,0,0.3258514404296875,0,0.3483047485351562,0,0.322418212890625,0.2724456787109375,0.2728118896484375,0.2729568481445312,0,0.2727203369140625,0.2724456787109375,0.2747955322265625,0.2750473022460938,0.0380401611328125,0,0,-3.00543212890625,0,0.3451766967773438,0.3382720947265625,0,0.3470993041992188,0,0,0.3390045166015625,0,0.3424072265625,0,0.3417739868164062,0,0.3418121337890625,0,0.3450469970703125,0,0.3281707763671875,0.03011322021484375,0,0,-2.943359375,0.3379669189453125,0.3484954833984375,0.3466949462890625,0,0,0.3446578979492188,0,0.3397369384765625,0,0.3416061401367188,0,0.3400802612304688,0,0.3455047607421875,0,0.2905731201171875,0,0,0,-2.810791015625,0,0.3390884399414062,0.3498458862304688,0,0.3434066772460938,0,0.3427658081054688,0.3417510986328125,0,0.343231201171875,0.3429336547851562,0,0.33795166015625,0,0.160186767578125,0,0,-2.978424072265625,0.3522872924804688,0.352020263671875,0,0.3455123901367188,0,0.3404769897460938,0.3407745361328125,0.3442840576171875,0,0.3388519287109375,0.3487701416015625,0,0.3044662475585938,0,0,0,0,0,-2.73052978515625,0,0.3405990600585938,0.3506011962890625,0,0.3366317749023438,0.3394927978515625,0,0.3404083251953125,0,0.3465728759765625,0,0.3412933349609375,0.3398971557617188,0,0.0825347900390625,0,0,-2.800773620605469,0,0.333831787109375,0.3509063720703125,0,0.340057373046875,0,0.3425140380859375,0,0.3424072265625,0,0.34307861328125,0.3426971435546875,0.3400421142578125,0,0.1514129638671875,0,0,-2.855125427246094,0,0.3451919555664062,0,0.3500518798828125,0,0,0.3409957885742188,0.34124755859375,0,0.3412857055664062,0,0.3429489135742188,0.34228515625,0,0.3417739868164062,0.194000244140625,0,0,-2.847953796386719,0,0.3454132080078125,0.3542098999023438,0,0.3464126586914062,0,0.3366165161132812,0.3366622924804688,0.3416671752929688,0,0.342529296875,0,0.3440933227539062,0,0.183746337890625,0,0,-2.789459228515625,0,0.3452224731445312,0.3499984741210938,0.342254638671875,0.337615966796875,0.3442611694335938,0,0.34686279296875,0,0.3479690551757812,0,0.3377914428710938,0,0.1195144653320312,0,0,-2.686614990234375,0,0.3225555419921875,0,0.34954833984375,0.33984375,0,0.338653564453125,0.3438262939453125,0.3453445434570312,0.3454513549804688,0,0.3328628540039062,0,0.04915618896484375,0,0,-2.562919616699219,0,0.3493270874023438,0.3476486206054688,0,0.3372650146484375,0.3421783447265625,0.3434295654296875,0,0,0.34478759765625,0.3436050415039062,0,0,0.2340850830078125,0,0,-2.71820068359375,0.3489532470703125,0,0.34674072265625,0,0.3402175903320312,0,0,0.3357009887695312,0,0.34271240234375,0,0.3431777954101562,0,0.3479843139648438,0,0.3321762084960938,0,0.05861663818359375,0,0,-2.493751525878906,0,0.3485107421875,0,0.3431243896484375,0.3386077880859375,0.3417739868164062,0,0.34637451171875,0,0.343597412109375,0,0.3450241088867188,0,0.1635589599609375,0,-2.556816101074219,0,0.3470916748046875,0,0.34381103515625,0.340179443359375,0,0.33856201171875,0.3438873291015625,0,0.345489501953125,0,0.3462142944335938,0,0.2272415161132812,0,-2.583580017089844,0.347442626953125,0.34564208984375,0.3365020751953125,0.3140029907226562,0.3296432495117188,0,0.3475494384765625,0,0.3479690551757812,0,0.2891845703125,0,0,0,0,0,-2.261070251464844,0.3414459228515625,0,0,0.3426971435546875,0,0.3386917114257812,0,0.3427200317382812,0,0.34368896484375,0.3471145629882812,0,0,0.2779312133789062,0,0,0,0,0,-2.209320068359375,0,0.3406143188476562,0,0.3427047729492188,0,0.3423614501953125,0,0,0.3402481079101562,0,0.3432083129882812,0.3451766967773438,0,0.227020263671875,0,-2.460258483886719,0,0.3372650146484375,0,0.3393096923828125,0.3418960571289062,0,0.3374862670898438,0,0.3414306640625,0,0,0.3411407470703125,0,0.3424911499023438,0.1500778198242188,0,0,-2.361167907714844,0,0.3359298706054688,0.335845947265625,0,0.3418426513671875,0,0.3370208740234375,0,0.3429107666015625,0,0.3460769653320312,0.3400192260742188,0,0.05126953125,0,0,-2.214973449707031,0,0.3357315063476562,0,0.3416061401367188,0.3399124145507812,0,0.3402328491210938,0.3436431884765625,0,0.3454513549804688,0,0.2369461059570312,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2.360565185546875,0,0,0.2970428466796875,0,0.3305816650390625,0,0.3270416259765625,0.3276596069335938,0.3332290649414062,0.3341217041015625,0,0.3354949951171875,0.14251708984375,0,0,-2.230415344238281,0.3377914428710938,0.342529296875,0.3431625366210938,0,0.342926025390625,0,0.342132568359375,0,0.345184326171875,0,0,0.243072509765625,0,0,0,0,0,-1.951858520507812,0,0.3348236083984375,0,0.3232803344726562,0,0.338775634765625,0.3428955078125,0,0.345977783203125,0.3314132690429688,0,0,0,-2.001960754394531,0.3338699340820312,0,0.3448638916015625,0,0.3416213989257812,0,0.3439178466796875,0,0,0.343109130859375,0.3474044799804688,0,0,0.011444091796875,0,-1.993141174316406,0,0.328643798828125,0,0.3378067016601562,0,0.33447265625,0,0,0.3390579223632812,0,0.342132568359375,0,0.3453140258789062,0,0.02896881103515625,0,0,-1.989448547363281,0,0,0.33233642578125,0,0.3419876098632812,0,0.34393310546875,0.3413238525390625,0,0.3472442626953125,0.3448257446289062,0,0,0,0,0,-1.92901611328125,0,0.3340911865234375,0,0.3441085815429688,0.3368301391601562,0.341400146484375,0,0.3454971313476562,0.2883224487304688,0,0,0,0,0,-1.824470520019531,0.3383712768554688,0,0.3438034057617188,0.341583251953125,0,0.3446731567382812,0,0.3419647216796875,0.1742630004882812,0,0,-2.021934509277344,0,0.3330154418945312,0,0.3437347412109375,0,0.3413162231445312,0,0.3404312133789062,0,0.3437347412109375,0.3465957641601562,0,0.03243255615234375,0,-1.845184326171875,0,0,0.334442138671875,0,0.3462753295898438,0.3401718139648438,0,0.3409500122070312,0.345703125,0,0.1958770751953125,0,0,-1.974716186523438,0,0.3333969116210938,0,0,0.3442535400390625,0.343963623046875,0,0.3412704467773438,0,0.34674072265625,0,0.322540283203125,0,0,0,0,0,-1.731986999511719,0,0.3371124267578125,0,0.3451614379882812,0,0,0.342529296875,0,0.3442840576171875,0,0.3460769653320312,0,0.07318115234375,0,-1.809623718261719,0,0,0.33111572265625,0,0.3444442749023438,0,0.3434066772460938,0.3432540893554688,0,0.3450546264648438,0.15789794921875,0,0,-1.853500366210938,0.3370590209960938,0,0.3460540771484375,0,0.3425369262695312,0,0.3393096923828125,0,0.3444137573242188,0.19873046875,0,0,-1.865058898925781,0.3321304321289062,0,0,0.343963623046875,0,0.3444290161132812,0,0.342193603515625,0,0.347900390625,0.2081680297851562,0,0,0,-1.826469421386719,0,0.3353347778320312,0,0.345184326171875,0,0.3432769775390625,0.3422927856445312,0,0.3476409912109375,0,0.1656341552734375,0,0,-1.761093139648438,0,0.333343505859375,0.3499526977539062,0,0.34429931640625,0.3442611694335938,0,0.3465423583984375,0,0.09462738037109375,0,-1.669654846191406,0,0.3377151489257812,0.3454132080078125,0,0.3428497314453125,0.3413162231445312,0,0.346038818359375,0,0.00754547119140625,0,0,-1.557403564453125,0,0.3391494750976562,0.345733642578125,0,0.3180084228515625,0,0.3410797119140625,0,0.2637557983398438,0,0,0,0,0,-1.463569641113281,0,0.3410797119140625,0,0.3428955078125,0,0.3421401977539062,0.342529296875,0,0.144439697265625,0,0,-1.647621154785156,0.3364181518554688,0,0.3469161987304688,0,0.34149169921875,0,0.33935546875,0.3321914672851562,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.388313293457031,0,0.3427200317382812,0,0.3421783447265625,0,0.3427352905273438,0,0.3391189575195312,0.06935882568359375,0,0,-1.529396057128906,0,0.3293075561523438,0.3418426513671875,0,0.3386764526367188,0,0.3384933471679688,0,0,0.2282867431640625,0,0,0,0,0,-1.317047119140625,0.34405517578125,0,0.3440093994140625,0.3407058715820312,0,0.3346786499023438,0,0,0,-1.394065856933594,0,0.338623046875,0,0.3476028442382812,0.3421783447265625,0,0.3421249389648438,0.06925201416015625,0,0,-1.45245361328125,0.3381118774414062,0,0.347808837890625,0,0.34246826171875,0,0.343597412109375,0,0.1254653930664062,0,0,-1.476211547851562,0,0,0.3351364135742188,0.3494415283203125,0,0.3435821533203125,0.3435897827148438,0.1486129760742188,0,0,-1.4820556640625,0,0.337615966796875,0,0.3485488891601562,0.3470611572265625,0,0.342315673828125,0.1500701904296875,0,0,0,-1.444976806640625,0,0.339019775390625,0,0.35003662109375,0,0.3450088500976562,0,0.3436050415039062,0,0.1101531982421875,0,-1.383232116699219,0,0.3395843505859375,0.3519363403320312,0.342041015625,0,0.3416366577148438,0,0,0.05005645751953125,0,-1.312278747558594,0,0.3397064208984375,0.3482131958007812,0.3433761596679688,0,0,0.3225021362304688,0,0,0,0,0,-1.225471496582031,0.343902587890625,0,0,0.3484649658203125,0,0.3423690795898438,0,0.2314529418945312,0,0,0,0,0,-1.108543395996094,0,0.350677490234375,0.3476715087890625,0.3406295776367188,0.1096878051757812,0,0,-1.289604187011719,0,0.3441085815429688,0,0.3506546020507812,0,0.3481063842773438,0,0.2862014770507812,0,0,0,0,0,-1.101966857910156,0,0,0.3495407104492188,0,0.3485565185546875,0.343353271484375,0,0,0.09931182861328125,0,0,-1.243667602539062,0,0.3440780639648438,0,0.351104736328125,0,0.344512939453125,0,0.2421646118164062,0,0,0,0,0,-1.019058227539062,0,0.3491973876953125,0.3470916748046875,0.3382797241210938,0,0,0.0220947265625,0,0,-1.119613647460938,0,0.3493270874023438,0.35211181640625,0.3447341918945312,0,0.1103897094726562,0,0,-1.189590454101562,0,0.3445358276367188,0.353546142578125,0,0.3488235473632812,0,0.1790313720703125,0,0,0,0,0,0,0,0,0,0,0,-1.042991638183594,0.3462753295898438,0,0.3415908813476562,0,0.338531494140625,0,0.05225372314453125,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.231925964355469,0,0.268157958984375,0,0,0.3535690307617188,0,0.340087890625,0,0.3183517456054688,0.334564208984375,0.33270263671875,0.3162078857421875,0,0.2763900756835938,0,0.2749557495117188,0.2746353149414062,0,0.2785110473632812,0,0.2776107788085938,0,0.27947998046875,0.280059814453125,0.2797088623046875,0,0.280059814453125,0,0.2758712768554688,0,0,0.2734146118164062,0,0.04598236083984375,0,0,-5.051414489746094,0,0.3714828491210938,0,0.353759765625,0,0.3252105712890625,0.3463363647460938,0,0.34637451171875,0,0.3448104858398438,0.3474578857421875,0,0.3462753295898438,0.3461532592773438,0,0.3500747680664062,0,0.3495712280273438,0,0.34918212890625,0,0.3509445190429688,0,0.3462371826171875,0,0.3242568969726562,0,0,0,0,0,-4.917587280273438,0,0.3672409057617188,0,0.3391571044921875,0,0.334808349609375,0.3443145751953125,0,0,0.3491897583007812,0,0,0.3479766845703125,0,0.3491668701171875,0.3509521484375,0.3484954833984375,0,0.348388671875,0.3473739624023438,0,0.3492202758789062,0,0.34906005859375,0,0.3385009765625,0.1979141235351562,0,0,0,0,0,-4.713264465332031,0.3582763671875,0,0,0.327056884765625,0.3490219116210938,0,0.3432693481445312,0,0.3443145751953125,0.3423538208007812,0.344573974609375,0,0.3453292846679688,0,0.3449859619140625,0.3464508056640625,0,0.3489303588867188,0.3482437133789062,0.3437042236328125,0,0.3298797607421875,0.038818359375,0,0,0,0,0,0,0,0,-4.843452453613281,0,0.37200927734375,0,0.3269119262695312,0,0.3204727172851562,0.3361434936523438,0,0.3358612060546875,0,0.3378524780273438,0,0.3387985229492188,0,0.3331069946289062,0.3400726318359375,0.333526611328125,0,0.3385009765625,0,0,0.33941650390625,0.3438644409179688,0,0.3422470092773438,0,0.2442092895507812,0,0,0,0,0,-4.614593505859375,0,0.355316162109375,0,0.3335342407226562,0,0.3442840576171875,0,0.3387374877929688,0.3431854248046875,0,0.3436279296875,0.3450927734375,0.3235931396484375,0,0.3447952270507812,0,0.3436508178710938,0.346160888671875,0,0.3488693237304688,0,0,0.3465576171875,0,0.2945938110351562,0,0,0,-4.5994873046875,0,0.3565673828125,0.3340530395507812,0,0.346954345703125,0,0.3423690795898438,0.3460311889648438,0,0.3454513549804688,0,0.344757080078125,0.3460922241210938,0.3451766967773438,0,0.3453750610351562,0,0.3456573486328125,0,0.3462295532226562,0,0.3478317260742188,0.242095947265625,0,0,0,0,0,-4.457626342773438,0.342926025390625,0,0.3395156860351562,0,0.341156005859375,0,0.3424835205078125,0,0.339569091796875,0,0.3427276611328125,0,0.3446121215820312,0,0.34710693359375,0,0.3460769653320312,0.34796142578125,0.3483123779296875,0,0.3484573364257812,0,0,0.3488235473632812,0.1109161376953125,0,0,0,0,0,-4.239852905273438,0.3362045288085938,0,0.344940185546875,0,0.3426895141601562,0,0.342132568359375,0.3435134887695312,0,0.3458175659179688,0,0.3483047485351562,0,0.3469467163085938,0,0,0.34375,0,0.3453140258789062,0.3490447998046875,0,0.3429336547851562,0.2391128540039062,0,0,0,0,0,-4.323753356933594,0.3386001586914062,0,0.3516998291015625,0,0.3426589965820312,0.3389129638671875,0.340576171875,0,0.3423233032226562,0,0.3431167602539062,0.3430252075195312,0,0.3431854248046875,0,0.3430938720703125,0,0.3488540649414062,0,0.349517822265625,0,0.3269119262695312,0,0,0,0,0,-4.352218627929688,0,0.3469314575195312,0,0.3441696166992188,0.3400115966796875,0,0.3397064208984375,0.3405990600585938,0.3406143188476562,0,0.3464279174804688,0,0.34356689453125,0,0,0.3447952270507812,0,0,0.34619140625,0.3509750366210938,0,0.3458404541015625,0,0.331298828125,0,0.01773834228515625,0,0,-4.316108703613281,0,0.3486175537109375,0,0.3510284423828125,0.3414688110351562,0.3382720947265625,0,0,0.3333816528320312,0,0.3401412963867188,0.3427047729492188,0.3462142944335938,0.3478012084960938,0.3461532592773438,0,0.339202880859375,0,0.3442840576171875,0,0.3214645385742188,0,0,0,0,0,-4.237045288085938,0,0.3476028442382812,0.3495712280273438,0,0.3402481079101562,0,0.340118408203125,0.3370590209960938,0,0.3409805297851562,0.34588623046875,0.3418045043945312,0.3433380126953125,0.3444595336914062,0.3485641479492188,0,0.3458099365234375,0,0.2341384887695312,0,0,0,-4.045417785644531,0,0.3469314575195312,0,0,0.3489990234375,0,0.3348312377929688,0,0.3335418701171875,0,0.3401107788085938,0,0.3441390991210938,0.3455047607421875,0,0.3430099487304688,0,0.3281402587890625,0,0.3476028442382812,0,0.3449859619140625,0,0.3341217041015625,0,0.07418060302734375,0,0,0,-3.830970764160156,0.352020263671875,0,0.3421173095703125,0.3322372436523438,0,0.338653564453125,0,0.3394088745117188,0,0,0.3408050537109375,0,0.3472747802734375,0.34912109375,0,0.348846435546875,0,0.3452529907226562,0.3433151245117188,0.1705780029296875,0,0,0,0,0,-3.852592468261719,0,0.3474960327148438,0,0.3428497314453125,0,0.3316421508789062,0,0.3347930908203125,0,0.3405990600585938,0,0.3443069458007812,0,0.3492431640625,0.347320556640625,0.3526535034179688,0.3472137451171875,0,0.3461990356445312,0.1850204467773438,0,0,0,-3.810630798339844,0,0.3427352905273438,0,0.3373336791992188,0.3297653198242188,0.3397750854492188,0,0.3394927978515625,0,0.3432998657226562,0,0.3452835083007812,0,0.3474273681640625,0,0.3486862182617188,0,0.348358154296875,0,0.340057373046875,0,0.1633453369140625,0,0,0,0,0,-3.733482360839844,0,0.3397369384765625,0,0.3350448608398438,0.32696533203125,0.3378219604492188,0,0.3409576416015625,0,0,0.3404617309570312,0.342803955078125,0.3441543579101562,0,0.3437271118164062,0,0.34661865234375,0.3360137939453125,0,0.1121292114257812,0,0,0,0,0,-3.639999389648438,0,0,0.3411331176757812,0,0.3318099975585938,0,0.3320083618164062,0,0,0.3375396728515625,0.3427581787109375,0,0.3428802490234375,0.3462371826171875,0,0,0.345733642578125,0.3506088256835938,0.3491592407226562,0,0.331298828125,0,0,3.0517578125e-05,0,-3.790306091308594,0.3426513671875,0,0.3383407592773438,0,0.329681396484375,0,0.3353347778320312,0,0.3413162231445312,0,0.3421630859375,0.3476181030273438,0.3476943969726562,0.3461380004882812,0,0.3485565185546875,0,0.3398513793945312,0,0.140380859375,0,0,0,0,0,-3.528678894042969,0,0.335845947265625,0,0.3305816650390625,0,0.3321914672851562,0,0.3377304077148438,0.3380508422851562,0,0.343780517578125,0,0.3416595458984375,0.3516082763671875,0,0.3425140380859375,0,0.34539794921875,0.2368850708007812,0,0,0,0,0,-3.569442749023438,0.3370895385742188,0.33135986328125,0.3325729370117188,0,0.340972900390625,0,0.3431015014648438,0.3446044921875,0,0,0.3467025756835938,0,0.3492355346679688,0,0.351287841796875,0,0,0.3469619750976562,0.2514572143554688,0,0,0,-3.578849792480469,0.3340301513671875,0,0.3297042846679688,0,0.3325958251953125,0.3231582641601562,0.3350296020507812,0,0.3464126586914062,0.3423538208007812,0.3282699584960938,0,0,0.3463668823242188,0,0.3480148315429688,0,0.3170852661132812,0,0,0,0,0,-3.56585693359375,0,0.339874267578125,0,0.3307723999023438,0,0.3309478759765625,0.3369903564453125,0.3444137573242188,0,0.34466552734375,0,0.3427200317382812,0.3433456420898438,0,0.3476409912109375,0,0.3462448120117188,0.2607269287109375,0,0,0,0,0,-3.430816650390625,0.3291015625,0,0.3267745971679688,0.3291397094726562,0,0.34368896484375,0.3448638916015625,0,0.3463897705078125,0.3479843139648438,0,0.3497085571289062,0,0.3472671508789062,0,0.3444595336914062,0.1223220825195312,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-3.336769104003906,0.3313522338867188,0,0.3227157592773438,0,0.3335647583007812,0,0.3349838256835938,0.3413543701171875,0,0.34417724609375,0.3436355590820312,0.3425979614257812,0.3480911254882812,0,0.33819580078125,0,0.05500030517578125,0,0,0,-3.114028930664062,0.32684326171875,0.3326568603515625,0.3365020751953125,0.3398513793945312,0,0.3435134887695312,0.3448562622070312,0.3493728637695312,0,0.345001220703125,0,0.3453369140625,0,0.1477508544921875,0,0,0,0,0,-3.154380798339844,0,0.3280868530273438,0.3319015502929688,0.33544921875,0,0.3412857055664062,0,0.3436050415039062,0,0.3448028564453125,0,0.3461532592773438,0.3462600708007812,0.342529296875,0.1904144287109375,0,0,0,0,0,-3.145492553710938,0,0.3293685913085938,0,0.3316497802734375,0.3359909057617188,0.3413467407226562,0,0.3423538208007812,0,0.3451766967773438,0,0.3506240844726562,0,0.3486709594726562,0,0.3416290283203125,0,0.1731948852539062,0,0,0,0,0,-3.078231811523438,0.3292617797851562,0.3317794799804688,0,0,0.3362579345703125,0.3414077758789062,0,0.3448104858398438,0.3444595336914062,0,0.3487319946289062,0,0.3499069213867188,0.3442153930664062,0,0.1003875732421875,0,0,0,0,0,-2.94793701171875,0,0.329193115234375,0,0.3374862670898438,0.3389434814453125,0,0.3429489135742188,0.3452682495117188,0.345916748046875,0,0.3485031127929688,0,0.3554763793945312,0,0,0.2956695556640625,0,0,0,0,0,-3.092567443847656,0,0.3302383422851562,0,0.3346328735351562,0,0.335296630859375,0,0.3390579223632812,0,0.3479156494140625,0,0.3451614379882812,0,0.3459014892578125,0,0.351287841796875,0,0.3391876220703125,0,0.1138916015625,0,0,0,0,0,-2.871017456054688,0,0.3120346069335938,0,0.33001708984375,0,0.3373184204101562,0.3444061279296875,0,0.344512939453125,0.3448104858398438,0.3475494384765625,0,0.347991943359375,0,0,0.2509307861328125,0,0,0,0,0,-2.992454528808594,0.3332977294921875,0.3331832885742188,0,0.34197998046875,0.3389129638671875,0.34161376953125,0,0.3398666381835938,0,0.3436355590820312,0,0.347930908203125,0,0.3381271362304688,0,0.02105712890625,0,0,0,0,0,-2.70196533203125,0,0.3307647705078125,0,0.3367538452148438,0,0.3388442993164062,0,0.3426895141601562,0.3452072143554688,0,0.34881591796875,0,0.351593017578125,0.3386077880859375,0,0.054351806640625,0,0,0,0,0,-2.688194274902344,0.3321685791015625,0,0.33880615234375,0,0.3397903442382812,0.3447952270507812,0.3433380126953125,0,0.3483505249023438,0,0.3502273559570312,0,0.3409347534179688,0,0.03417205810546875,0,0,0,-2.597808837890625,0,0.3344573974609375,0,0.3416748046875,0,0.3421783447265625,0,0.3434219360351562,0,7.962493896484375,0,0,0,0,0,0,0,0,0,0,0,7.62939453125,0,3.0517578125e-05,0,0,0,0,0,0,0,0,0,0,0,0,0,15.2587890625,0,0,0,0,0,0,0,0,0],"filename":[null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null]},"interval":10,"files":[],"prof_output":"/tmp/RtmpqXdN5L/file6beb6f2126ee.prof","highlight":{"output":["^output\\$"],"gc":["^<GC>$"],"stacktrace":["^\\.\\.stacktraceo(n|ff)\\.\\.$"]},"split":"h"}},"evals":[],"jsHooks":[]}</script>
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
```

```
## Unit: milliseconds
##           expr      min       lq     mean   median       uq      max neval cld
##  mean1(x, 0.5) 21.41562 21.65715 23.30394 23.46639 23.74809 31.79446    20  a 
##  mean2(x, 0.5) 20.47924 20.62251 21.73227 21.09111 22.67298 24.88078    20   b
##  mean3(x, 0.5) 21.48345 21.76114 23.17252 23.48885 23.85145 25.60360    20  a
```

``` r
# Time them (w/ memory)
bench::mark(
  mean1(x,.5),
  mean2(x,.5),
  mean3(x,.5),
  iterations=20
)
```

```
## # A tibble: 3 × 6
##   expression         min   median `itr/sec` mem_alloc `gc/sec`
##   <bch:expr>    <bch:tm> <bch:tm>     <dbl> <bch:byt>    <dbl>
## 1 mean1(x, 0.5)   21.3ms   23.9ms      43.6    7.63MB     0   
## 2 mean2(x, 0.5)   20.5ms     21ms      45.6    7.63MB     2.40
## 3 mean3(x, 0.5)   21.3ms   24.1ms      42.5    7.63MB     2.24
```


**Vectorize**.

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

all.equal(ma1(x),ma2(x))
```

```
## [1] TRUE
```

``` r
system.time( ma1(x) )
```

```
##    user  system elapsed 
##   0.187   0.000   0.188
```

``` r
system.time( ma2(x) )
```

```
##    user  system elapsed 
##   0.028   0.006   0.034
```

``` r
ma3 <- compiler::cmpfun(ma2)
system.time( ma3(x) )
```

```
##    user  system elapsed 
##   0.029   0.000   0.029
```
Likewise, matrix operations are often faster than vector operations.

**Pre-allocate**

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
```

```
## [1]   1   4  25 676
```


**Memory Usage**.

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
##   0.424   0.004   0.225
```

``` r
system.time({ .lm.fit(X, Y) })
```

```
##    user  system elapsed 
##   0.095   0.000   0.027
```

``` r
system.time({ solve(t(X)%*%X) %*% (t(X)%*%Y) })
```

```
##    user  system elapsed 
##   0.026   0.000   0.025
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
##   0.023   0.000   0.023
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
##   0.891   0.154   0.599
```

``` r
# Same results
all(e_power_e_vec==e_power_e_mc)
```

```
## [1] TRUE
```

Note that parallelism does not go well with a GUI.


## Advanced Optimizing

If you still are stuck, you can

* try [Amazon Web Server](https://aws.amazon.com/ec2/) for more brute-power 
* rewrite bottlenecks with a working C++ compiler or Fortran compiler.

Before doing that, however, look into <https://cran.r-project.org/web/views/HighPerformanceComputing.html>

In what follows, note that there are alternative ways to run R via the command line. For example,

``` bash
# Method 1
R -e "source('MyFirstScript.R')"
# Method 2
R CMD BATCH MyFirstScript.R
```

**Cluster Computing**

For parallel computations on a computer cluster, you will need to use both R and the linux command line.


``` bash
R --slave -e '1:10'

R --slave -e '
    1:10
    seq(0,1,by=.2)
    paste(c("A","D"), 1:2)
'
```

```
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
```

```
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
## [16] tibble_3.2.1         bookdown_0.43        profvis_0.4.0       
## [19] bslib_0.9.0          pillar_1.10.2        rlang_1.1.6         
## [22] utf8_1.2.5           multcomp_1.4-28      cachem_1.1.0        
## [25] xfun_0.52            sass_0.4.10          cli_3.6.5           
## [28] magrittr_2.0.3       digest_0.6.37        grid_4.5.0          
## [31] mvtnorm_1.3-3        sandwich_3.1-1       lifecycle_1.0.4     
## [34] vctrs_0.6.5          bench_1.1.4          evaluate_1.0.3      
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



