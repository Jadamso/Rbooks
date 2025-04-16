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
##   0.130   0.008   0.139
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
<div class="profvis html-widget html-fill-item" id="htmlwidget-a1f375ea437656c62a0a" style="width:100%;height:600px;"></div>
<script type="application/json" data-for="htmlwidget-a1f375ea437656c62a0a">{"x":{"message":{"prof":{"time":[1,2,3,5,6,7,8,8,8,9,9,10,10,11,11,12,12,13,13,14,14,15,15,16,16,17,17,17,18,18,19,19,20,20,21,22,22,22,23,24,25,26,26,27,27,27,28,28,29,30,30,30,31,32,32,33,33,33,34,34,35,36,37,37,38,39,39,39,40,41,42,43,44,44,44,45,45,46,46,47,47,48,48,49,49,49,50,50,50,51,51,52,52,53,53,54,54,55,55,56,57,58,58,59,59,60,60,61,61,61,62,62,63,64,64,65,65,66,66,66,67,67,68,68,69,69,70,71,71,72,72,73,73,74,74,75,75,76,76,77,77,78,79,79,79,80,80,81,81,82,82,83,83,84,84,84,85,85,86,86,87,87,88,89,89,89,90,90,90,91,92,92,93,93,94,95,95,96,96,96,97,97,98,99,100,100,101,101,101,102,103,104,105,105,106,106,106,106,107,108,108,109,109,110,110,111,111,111,112,112,113,113,113,114,115,115,116,116,116,117,117,118,118,119,120,120,121,121,121,122,122,123,123,124,125,126,126,126,127,127,128,128,129,130,130,131,131,131,132,133,133,134,135,135,136,136,136,137,137,137,138,138,139,140,140,141,141,142,142,143,144,144,145,145,145,146,146,147,147,148,148,149,149,150,150,150,151,151,152,152,152,153,153,154,154,154,155,155,156,156,157,157,158,158,159,159,159,160,161,161,162,162,163,163,163,164,164,165,165,166,166,167,168,168,168,169,169,170,171,171,172,172,172,173,173,173,174,174,175,175,176,176,176,177,177,177,178,178,178,179,179,179,180,180,181,181,182,182,183,183,184,184,185,186,187,187,188,188,189,190,191,191,191,192,192,193,193,194,195,195,195,196,196,197,197,198,198,199,199,199,200,200,201,201,202,202,203,203,203,204,204,205,205,206,207,207,208,208,209,209,210,210,210,211,211,211,212,213,213,213,214,214,214,215,215,215,216,216,217,218,218,218,219,220,221,222,222,222,223,223,224,224,225,225,225,226,226,227,227,228,228,229,230,230,230,231,231,231,232,232,232,233,233,233,234,234,235,236,236,237,237,238,238,239,239,240,240,241,241,242,242,243,243,244,244,244,245,245,246,246,247,247,248,248,248,249,250,250,251,251,252,252,253,253,254,254,254,254,255,255,255,255,256,256,257,258,258,259,259,260,260,261,261,262,262,263,263,264,264,265,265,266,266,267,267,268,268,269,269,270,270,271,272,273,273,274,274,275,275,276,276,277,277,278,278,279,279,279,280,280,281,281,282,283,283,284,284,285,286,287,287,288,289,289,290,290,291,292,292,293,293,294,294,295,296,296,297,298,298,298,299,300,301,301,301,302,303,304,305,306,307,307,308,308,309,310,310,311,312,312,313,313,314,314,315,315,316,317,317,318,318,319,319,320,320,321,321,322,322,323,323,324,324,325,325,326,326,327,327,328,328,328,329,330,330,331,331,332,332,333,334,334,334,335,336,336,336,337,337,337,338,338,339,340,340,341,341,342,342,343,343,344,344,345,345,346,346,346,347,347,348,349,350,350,351,351,352,352,353,354,354,355,355,356,356,356,357,358,359,359,359,360,360,361,361,362,362,363,363,364,364,364,365,365,366,367,367,368,368,369,369,370,370,371,371,372,373,373,374,374,375,375,375,376,376,377,377,377,378,378,379,379,380,381,381,382,382,382,383,383,384,384,385,385,386,386,387,388,388,389,390,390,391,391,391,392,393,394,394,394,395,396,396,397,397,398,399,399,399,400,400,400,401,401,402,402,403,403,404,405,406,407,407,408,408,409,409,410,410,411,411,412,412,412,413,414,414,415,416,416,416,417,417,417,418,419,419,420,420,421,422,423,423,424,425,425,425,426,427,427,428,428,429,430,430,431,431,432,432,433,433,433,434,434,434,435,435,436,436,437,438,438,439,439,440,440,440,441,441,441,442,442,442,443,444,444,445,445,446,447,448,448,449,449,450,450,451,451,451,452,453,453,454,454,455,455,456,457,457,458,458,459,459,460,460,461,461,462,462,463,463,464,465,465,466,466,467,467,468,468,469,469,469,470,470,471,471,471,472,472,472,473,473,474,474,475,475,476,476,476,477,478,478,479,479,480,481,482,482,483,483,484,485,486,486,486,487,487,488,488,489,490,491,491,492,493,493,494,494,495,495,496,496,497,498,498,498,499,500,500,501,501,501,502,503,503,503,504,504,505,506,506,507,507,508,508,508,509,509,509,510,511,511,512,512,513,513,514,514,515,516,516,516,517,517,518,518,519,519,520,521,521,522,522,523,523,523,524,524,525,525,526,527,527,527,528,528,529,529,530,530,530,531,532,532,533,534,534,535,536,536,537,537,537,538,538,539,539,540,541,541,542,542,543,543,544,544,544,545,545,546,546,547,547,548,549,549,550,550,550,551,551,551,552,552,553,554,555,555,556,556,557,557,558,558,559,560,560,561,561,562,563,563,564,564,564,565,566,566,567,568,568,569,569,570,570,570,570,571,571,571,571,572,572,573,574,574,575,576,576,577,577,577,578,578,579,579,580,580,581,581,582,583,583,584,584,585,586,586,587,587,588,588,589,589,590,590,590,591,591,592,593,593,594,594,595,595,595,596,596,596,597,597,598,599,599,600,600,601,601,602,602,602,603,603,604,604,605,606,607,607,608,608,609,609,610,610,611,611,612,612,613,613,614,614,615,615,616,617,617,618,618,618,619,619,620,620,621,621,621,622,622,622,623,623,624,624,624,625,625,626,626,627,628,628,629,629,630,630,631,631,632,632,633,634,635,635,636,636,636,636,637,637,638,639,639,640,640,640,641,641,641,642,642,642,643,643,644,645,646,646,647,647,648,648,649,649,650,650,651,652,653,653,654,654,655,655,656,656,656,657,657,658,658,658,659,660,660,661,661,662,662,663,663,663,664,664,664,665,665,666,666,667,667,668,669,669,670,670,671,671,671,672,672,673,673,674,674,674,674,675,675,675,675,676,677,677,678,678,678,679,679,680,680,680,680,681,681,682,682,683,683,684,685,685,686,686,687,688,688,689,690,690,690,691,691,692,692,693,693,694,694,695,695,695,696,696,696,697,697,698,698,699,699,699,700,700,701,701,701,702,703,703,704,704,705,706,706,707,707,708,709,710,711,711,711,712,712,712,713,713,713,714,714,714,715,715,715,716,716,716,717,717,717,718,718,719,719,720,720,721,721,722,722,723,723,724,724,725,725,726,726,727,727,728,728,729,729,730,730,731,731,732,732,733,733,734,734,735,735,736,736,737,737,738,738,739,739,740,740,741,741,742,742,743,744,744,744,745,745,745,746,746,746,747,748,748,749,749,750,750,751,751,752,752,753,753,754,754,755,756,757,757,758,758,759,759,760,760,761,761,762,762,763,763,764,764,765,765,766,767,767,767,768,768,768,769,770,770,771,771,772,772,773,773,774,774,775,775,776,776,777,777,778,778,779,779,780,780,781,781,782,783,783,784,784,785,785,786,786,787,788,788,788,789,789,789,790,790,791,791,792,792,793,794,794,795,795,796,796,796,797,797,798,799,799,800,801,801,802,802,803,803,803,804,804,804,805,805,805,806,806,806,807,807,807,808,809,809,810,810,811,811,811,812,812,813,814,814,815,815,815,816,816,817,817,818,818,819,819,820,820,820,821,821,821,822,822,823,823,824,825,825,826,826,827,827,828,828,829,829,830,831,831,832,832,833,833,834,834,835,835,835,836,836,836,837,837,838,838,839,839,840,840,841,841,842,842,843,843,844,844,845,845,846,846,847,847,848,849,849,850,850,850,850,851,852,852,853,853,854,855,855,856,857,857,858,858,859,859,860,860,861,862,862,863,863,864,864,864,865,865,865,866,866,867,867,868,868,869,869,870,870,871,871,872,872,873,873,874,875,875,876,876,877,877,878,878,878,879,879,879,880,880,881,881,882,882,883,883,884,884,885,885,886,887,887,887,888,889,890,890,891,891,892,892,893,893,893,894,894,894,895,896,897,898,898,899,899,900,900,901,902,903,903,904,905,905,906,906,907,907,907,908,908,908,909,909,910,910,911,912,912,913,913,914,914,915,915,916,917,917,918,918,919,920,920,921,921,922,922,923,923,924,925,926,926,927,927,928,929,929,930,930,931,931,932,933,933,933,934,934,934,935,935,935,936,936,936,937,937,937,938,938,939,939,940,941,941,942,943,944,944,945,945,946,947,947,947,948,948,949,949,950,950,951,951,952,953,953,954,954,955,955,956,956,957,957,958,958,959,959,960,961,961,962,962,963,963,964,965,966,967,968,969,969,970,970,970,971,972,973,974,974,975,975,975,976,976,976,977,977,978,978,979,979,980,981,981,981,982,982,983,983,984,984,985,986,987,987,987,988,988,988,989,989,989,990,991,992,993,993,994,995,996,996,997,998,998,999,999,1000,1001,1001,1001,1002,1002,1003,1004,1004,1005,1005,1006,1006,1007,1007,1008,1008,1009,1009,1010,1010,1011,1012,1012,1013,1013,1013,1014,1014,1014,1015,1015,1016,1017,1017,1018,1019,1019,1020,1020,1021,1021,1022,1022,1023,1023,1024,1024,1025,1025,1025,1026,1026,1026,1027,1027,1028,1028,1029,1029,1030,1031,1031,1032,1032,1033,1033,1033,1034,1035,1035,1036,1036,1037,1037,1038,1038,1039,1039,1040,1041,1041,1042,1042,1043,1043,1044,1045,1045,1046,1047,1047,1048,1048,1049,1049,1049,1050,1050,1050,1051,1051,1051,1052,1052,1053,1053,1054,1054,1055,1055,1056,1056,1057,1057,1058,1058,1059,1059,1060,1060,1061,1062,1062,1062,1062,1063,1063,1063,1063,1064,1065,1065,1066,1066,1067,1067,1068,1069,1069,1070,1070,1071,1072,1072,1073,1073,1074,1074,1074,1075,1075,1075,1076,1077,1077,1078,1079,1079,1080,1080,1081,1082,1082,1083,1084,1085,1086,1086,1087,1087,1088,1088,1089,1089,1090,1090,1091,1091,1092,1092,1093,1093,1094,1094,1095,1095,1096,1096,1097,1098,1099,1099,1100,1100,1101,1101,1102,1102,1103,1104,1104,1104,1105,1105,1105,1106,1106,1106,1107,1107,1107,1108,1108,1109,1110,1110,1111,1112,1112,1113,1113,1114,1114,1115,1115,1116,1117,1117,1117,1118,1118,1118,1119,1119,1120,1120,1121,1121,1122,1123,1123,1124,1124,1125,1125,1126,1126,1127,1128,1129,1129,1130,1130,1131,1131,1131,1132,1133,1133,1134,1135,1135,1136,1137,1138,1138,1138,1139,1139,1140,1140,1140,1141,1141,1141,1142,1142,1142,1143,1143,1143,1144,1144,1145,1146,1146,1147,1148,1148,1149,1149,1150,1151,1152,1152,1152,1153,1153,1153,1154,1154,1155,1155,1156,1156,1157,1158,1159,1160,1161,1161,1162,1163,1163,1163,1164,1164,1164,1165,1165,1166,1167,1167,1168,1169,1169,1170,1171,1171,1172,1172,1172,1173,1173,1174,1174,1175,1175,1176,1177,1178,1178,1179,1179,1180,1180,1181,1182,1182,1183,1183,1184,1184,1184,1185,1185,1185,1186,1186,1186,1187,1188,1188,1189,1190,1190,1191,1192,1193,1193,1194,1194,1195,1195,1196,1196,1197,1197,1198,1199,1199,1200,1200,1201,1201,1202,1202,1203,1204,1204,1205,1206,1206,1206,1207,1207,1207,1208,1208,1209,1210,1211,1212,1212,1213,1213,1214,1215,1215,1216,1217,1217,1218,1218,1219,1219,1220,1220,1221,1221,1222,1222,1223,1223,1224,1224,1225,1225,1226,1226,1227,1227,1228,1228,1228,1229,1229,1230,1231,1232,1233,1233,1234,1234,1235,1235,1236,1236,1236,1237,1237,1237,1238,1238,1239,1239,1240,1240,1241,1242,1243,1244,1244,1245,1245,1246,1246,1246,1247,1248,1248,1248,1249,1249,1249,1250,1250,1251,1251,1252,1252,1253,1253,1254,1254,1255,1255,1256,1256,1257,1257,1258,1259,1259,1260,1260,1261,1261,1262,1262,1263,1263,1264,1264,1265,1265,1266,1266,1267,1267,1268,1268,1269,1269,1270,1270,1271,1271,1272,1272],"depth":[1,1,1,1,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,3,2,1,1,1,1,2,1,3,2,1,2,1,1,3,2,1,1,2,1,3,2,1,2,1,1,1,2,1,1,3,2,1,1,1,1,1,3,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,1,2,1,2,1,1,2,1,3,2,1,2,1,1,1,2,1,3,2,1,1,1,1,2,1,4,3,2,1,1,2,1,2,1,2,1,3,2,1,2,1,3,2,1,1,2,1,3,2,1,2,1,2,1,1,2,1,3,2,1,2,1,2,1,1,1,3,2,1,2,1,2,1,1,2,1,3,2,1,1,2,1,1,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,3,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,3,2,1,2,1,1,2,1,3,2,1,3,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,1,1,3,2,1,2,1,2,1,1,3,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,1,3,2,1,3,2,1,3,2,1,2,1,1,3,2,1,1,1,1,3,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,2,1,4,3,2,1,4,3,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,1,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,1,3,2,1,1,1,3,2,1,1,1,1,1,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,1,3,2,1,1,3,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,1,1,3,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,3,2,1,2,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,3,2,1,1,1,3,2,1,1,2,1,2,1,1,3,2,1,3,2,1,2,1,2,1,2,1,1,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,1,3,2,1,3,2,1,1,2,1,2,1,1,1,2,1,1,3,2,1,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,3,2,1,1,2,1,2,1,1,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,1,1,2,1,2,1,1,1,3,2,1,2,1,2,1,1,1,2,1,1,2,1,2,1,2,1,2,1,1,3,2,1,1,2,1,3,2,1,1,3,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,2,1,1,3,2,1,2,1,2,1,3,2,1,1,2,1,1,2,1,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,3,2,1,3,2,1,2,1,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,3,2,1,1,2,1,1,2,1,2,1,4,3,2,1,4,3,2,1,2,1,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,2,1,2,1,3,2,1,3,2,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,4,3,2,1,2,1,1,2,1,3,2,1,3,2,1,3,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,3,2,1,2,1,3,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,2,1,4,3,2,1,4,3,2,1,1,2,1,3,2,1,2,1,4,3,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,3,2,1,2,1,3,2,1,1,2,1,2,1,1,2,1,2,1,1,1,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,1,2,1,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,1,2,1,2,1,3,2,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,4,3,2,1,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,1,1,2,1,2,1,2,1,3,2,1,3,2,1,1,1,1,2,1,2,1,2,1,1,1,2,1,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,1,2,1,2,1,2,1,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,1,1,2,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,1,1,1,1,2,1,3,2,1,1,1,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,2,1,1,1,3,2,1,3,2,1,3,2,1,1,1,1,2,1,1,1,2,1,1,2,1,2,1,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,3,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,4,3,2,1,4,3,2,1,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,1,2,1,1,2,1,2,1,1,2,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,3,2,1,1,2,1,1,2,1,1,1,3,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,1,2,1,1,2,1,2,1,1,1,3,2,1,3,2,1,2,1,2,1,2,1,1,1,1,1,2,1,1,3,2,1,3,2,1,2,1,1,2,1,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,3,2,1,1,2,1,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,1,3,2,1,3,2,1,2,1,1,1,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,1,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,1,1,2,1,2,1,3,2,1,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1],"label":["rowSums","rowSums","rowSums","rowMeans","rowMeans","rowMeans","<GC>","aperm.default","apply","aperm.default","apply","aperm.default","apply","aperm.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","apply","<GC>","FUN","apply","apply","apply","apply","FUN","apply","<GC>","FUN","apply","mean.default","apply","apply","isTRUE","mean.default","apply","apply","length","local","<GC>","FUN","apply","mean.default","apply","apply","apply","mean.default","apply","apply","<GC>","mean.default","apply","apply","apply","apply","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","is.na","local","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","<GC>","apply","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","<GC>","FUN","apply","mean.default","apply","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","is.numeric","local","FUN","apply","mean.default","apply","apply","is.na","local","<GC>","apply","<GC>","apply","<GC>","apply","is.numeric","local","length","local","mean.default","apply","apply","<GC>","FUN","apply","FUN","apply","is.na","local","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","<GC>","apply","FUN","apply","mean.default","apply","apply","isTRUE","mean.default","apply","<GC>","mean.default","apply","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","<GC>","mean.default","apply","is.na","local","apply","apply","length","local","<GC>","length","local","apply","apply","apply","FUN","apply","<GC>","isTRUE","mean.default","apply","apply","is.na","local","mean.default","apply","FUN","apply","<GC>","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","<GC>","FUN","apply","FUN","apply","mean.default","apply","apply","is.na","local","<GC>","mean.default","apply","is.numeric","local","mean.default","apply","apply","apply","<GC>","mean.default","apply","length","local","FUN","apply","apply","mean.default","apply","<GC>","FUN","apply","apply","mean.default","apply","apply","FUN","apply","<GC>","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","<GC>","apply","FUN","apply","FUN","apply","apply","is.numeric","local","<GC>","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","<GC>","is.numeric","local","FUN","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","apply","mean.default","apply","mean.default","apply","<GC>","is.na","local","length","local","FUN","apply","length","local","apply","<GC>","FUN","apply","mean.default","apply","apply","FUN","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","is.numeric","local","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","apply","FUN","apply","apply","apply","<GC>","apply","FUN","apply","apply","apply","<GC>","length","local","FUN","apply","mean.default","apply","apply","<GC>","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","<GC>","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","apply","<GC>","apply","mean.default","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","apply","<GC>","mean.default","apply","apply","apply","apply","<GC>","mean.default","apply","length","local","FUN","apply","isTRUE","mean.default","apply","<GC>","apply","FUN","apply","FUN","apply","apply","<GC>","mean.default","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","length","local","apply","FUN","apply","<GC>","apply","mean.default","apply","mean.default","apply","FUN","apply","<GC>","apply","FUN","apply","mean.default","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","<GC>","apply","length","local","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","is.numeric","local","is.na","local","FUN","apply","<GC>","FUN","apply","mean.default","apply","FUN","apply","apply","FUN","apply","mean.default","apply","apply","apply","FUN","apply","apply","<GC>","apply","is.numeric","local","apply","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","<GC>","mean.default","apply","apply","apply","isTRUE","mean.default","apply","apply","apply","apply","apply","apply","FUN","apply","<GC>","apply","apply","length","local","apply","FUN","apply","length","local","mean.default","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","<GC>","apply","isTRUE","mean.default","apply","apply","FUN","apply","is.numeric","local","FUN","apply","apply","isTRUE","mean.default","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","<GC>","length","local","mean.default","apply","apply","apply","FUN","apply","mean.default","apply","FUN","apply","apply","FUN","apply","<GC>","apply","isTRUE","mean.default","apply","apply","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","is.na","local","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","apply","mean.default","apply","length","local","FUN","apply","FUN","apply","length","local","apply","<GC>","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","apply","is.na","local","<GC>","is.na","local","is.na","local","FUN","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","apply","mean.default","apply","<GC>","FUN","apply","apply","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","is.numeric","local","FUN","apply","apply","apply","apply","FUN","apply","<GC>","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","mean.default","apply","apply","apply","FUN","apply","apply","<GC>","FUN","apply","apply","FUN","apply","is.na","local","apply","mean.default","apply","is.na","local","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","is.numeric","local","mean.default","apply","apply","apply","is.na","local","<GC>","apply","<GC>","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","mean.default","apply","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","apply","is.na","local","FUN","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","<GC>","apply","<GC>","apply","apply","apply","is.numeric","local","mean.default","apply","apply","apply","<GC>","FUN","apply","mean.default","apply","FUN","apply","apply","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","FUN","apply","mean.default","apply","apply","isTRUE","mean.default","apply","apply","mean.default","apply","<GC>","FUN","apply","apply","isTRUE","mean.default","apply","is.numeric","local","apply","mean.default","apply","FUN","apply","<GC>","length","local","<GC>","length","local","apply","FUN","apply","FUN","apply","mean.default","apply","is.na","local","apply","<GC>","FUN","apply","length","local","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","<GC>","FUN","apply","apply","FUN","apply","apply","mean.default","apply","apply","mean.default","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","apply","is.na","local","mean.default","apply","FUN","apply","<GC>","FUN","apply","is.na","local","FUN","apply","length","local","apply","FUN","apply","<GC>","is.na","local","<GC>","is.na","local","is.numeric","local","apply","apply","FUN","apply","FUN","apply","<GC>","apply","<GC>","apply","apply","FUN","apply","mean.default","apply","apply","FUN","apply","<GC>","mean.default","apply","apply","mean.default","apply","apply","mean.default","apply","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","mean.default","apply","apply","FUN","apply","apply","mean.default","apply","<GC>","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","<GC>","apply","<GC>","apply","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","mean.default","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","<GC>","FUN","apply","FUN","apply","is.numeric","local","apply","apply","mean.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","length","local","length","local","FUN","apply","apply","mean.default","apply","<GC>","FUN","apply","is.numeric","local","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","FUN","apply","is.numeric","local","FUN","apply","apply","FUN","apply","FUN","apply","<GC>","apply","length","local","is.numeric","local","apply","apply","FUN","apply","<GC>","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","length","local","apply","apply","FUN","apply","<GC>","apply","length","local","FUN","apply","FUN","apply","apply","apply","<GC>","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","mean.default","apply","apply","FUN","apply","mean.default","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","<GC>","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","apply","is.na","local","isTRUE","mean.default","apply","FUN","apply","<GC>","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","apply","<GC>","apply","FUN","apply","apply","is.numeric","local","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","FUN","apply","apply","length","local","FUN","apply","apply","<GC>","apply","<GC>","apply","apply","apply","apply","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","isTRUE","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","length","local","apply","apply","mean.default","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","<GC>","length","local","<GC>","length","local","mean.default","apply","FUN","apply","FUN","apply","apply","is.numeric","local","is.numeric","local","isTRUE","mean.default","apply","is.na","local","apply","FUN","apply","apply","FUN","apply","length","local","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","is.na","local","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","is.na","local","apply","mean.default","apply","FUN","apply","is.numeric","local","FUN","apply","FUN","apply","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","is.na","local","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","<GC>","isTRUE","mean.default","apply","apply","mean.default","apply","FUN","apply","apply","length","local","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","length","local","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","length","local","mean.default","apply","mean.default","apply","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","mean.default","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","apply","apply","is.na","local","mean.default","apply","FUN","apply","apply","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","mean.default","apply","apply","mean.default","apply","<GC>","apply","<GC>","apply","FUN","apply","apply","apply","FUN","apply","length","local","apply","FUN","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","<GC>","is.numeric","local","<GC>","is.numeric","local","isTRUE","mean.default","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","apply","FUN","apply","mean.default","apply","apply","isTRUE","mean.default","apply","is.numeric","local","<GC>","apply","<GC>","apply","FUN","apply","apply","FUN","apply","length","local","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","<GC>","apply","<GC>","apply","apply","apply","apply","apply","apply","mean.default","apply","isTRUE","mean.default","apply","apply","apply","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","is.na","local","mean.default","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","<GC>","is.numeric","local","<GC>","is.numeric","local","apply","apply","apply","is.na","local","apply","apply","mean.default","apply","apply","FUN","apply","FUN","apply","apply","<GC>","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","mean.default","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","<GC>","is.na","local","<GC>","is.na","local","FUN","apply","FUN","apply","length","local","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","mean.default","apply","<GC>","apply","<GC>","apply","apply","FUN","apply","length","local","FUN","apply","apply","mean.default","apply","apply","mean.default","apply","is.na","local","isTRUE","mean.default","apply","<GC>","is.na","local","<GC>","is.na","local","FUN","apply","FUN","apply","mean.default","apply","is.na","local","mean.default","apply","mean.default","apply","FUN","apply","length","local","mean.default","apply","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","apply","length","local","mean.default","apply","length","local","apply","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","FUN","apply","apply","FUN","apply","mean.default","apply","apply","FUN","apply","apply","apply","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","length","local","apply","FUN","apply","apply","FUN","apply","FUN","apply","is.numeric","local","FUN","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","length","local","mean.default","apply","mean.default","apply","apply","apply","<GC>","apply","<GC>","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","mean.default","apply","apply","apply","isTRUE","mean.default","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","is.na","local","apply","FUN","apply","apply","is.na","local","mean.default","apply","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","apply","apply","apply","apply","mean.default","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","apply","FUN","apply","apply","mean.default","apply","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","<GC>","apply","<GC>","apply","apply","apply","length","local","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","is.numeric","local","apply","FUN","apply","apply","apply","mean.default","apply","length","local","<GC>","apply","<GC>","apply","is.numeric","local","apply","length","local","FUN","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","length","local","apply","apply","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","length","local","FUN","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","apply","mean.default","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","apply","apply","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply"],"filenum":[null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null],"linenum":[null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null],"memalloc":[122.0793380737305,122.0793380737305,122.0793380737305,137.3382797241211,137.3382797241211,137.3382797241211,137.3386764526367,137.3386764526367,137.3386764526367,167.3755950927734,167.3755950927734,167.3755950927734,167.3755950927734,167.3755950927734,167.3755950927734,167.3756408691406,167.3756408691406,167.3749923706055,167.3749923706055,167.3749923706055,167.3749923706055,167.3749923706055,167.3749923706055,167.3748092651367,167.3748092651367,182.931266784668,182.931266784668,182.931266784668,183.3539733886719,183.3539733886719,183.7558135986328,183.7558135986328,184.1345291137695,184.1345291137695,184.4619903564453,184.5675659179688,184.5675659179688,184.5675659179688,183.0065231323242,183.4204177856445,183.8286972045898,184.2369613647461,184.2369613647461,184.6010894775391,184.6010894775391,184.6010894775391,182.8546142578125,182.8546142578125,183.2279052734375,183.6423416137695,183.6423416137695,183.6423416137695,184.0471267700195,184.4451599121094,184.4451599121094,184.6525192260742,184.6525192260742,184.6525192260742,183.0600509643555,183.0600509643555,183.4421539306641,183.8441314697266,184.2471237182617,184.2471237182617,184.6450881958008,184.7030563354492,184.7030563354492,184.7030563354492,183.3236312866211,183.7216339111328,184.1152038574219,184.5114288330078,184.7528610229492,184.7528610229492,184.7528610229492,183.1992263793945,183.1992263793945,183.6050491333008,183.6050491333008,183.9975891113281,183.9975891113281,184.3902893066406,184.3902893066406,184.7802200317383,184.7802200317383,184.7802200317383,184.8018112182617,184.8018112182617,184.8018112182617,183.4504165649414,183.4504165649414,183.8429946899414,183.8429946899414,184.2327575683594,184.2327575683594,184.6282348632812,184.6282348632812,184.8500137329102,184.8500137329102,183.3375091552734,183.7056045532227,184.0963592529297,184.0963592529297,184.4896087646484,184.4896087646484,184.8761978149414,184.8761978149414,184.8973770141602,184.8973770141602,184.8973770141602,183.6196899414062,183.6196899414062,184.0031509399414,184.369140625,184.369140625,184.7330780029297,184.7330780029297,184.9440002441406,184.9440002441406,184.9440002441406,183.4475326538086,183.4475326538086,183.7767105102539,183.7767105102539,184.1377029418945,184.1377029418945,184.5064086914062,184.8824157714844,184.8824157714844,184.9899520874023,184.9899520874023,184.9899520874023,184.9899520874023,184.9899520874023,184.9899520874023,183.7262649536133,183.7262649536133,184.0868911743164,184.0868911743164,184.4511795043945,184.4511795043945,184.8182907104492,185.0349349975586,185.0349349975586,185.0349349975586,183.5830001831055,183.5830001831055,183.915901184082,183.915901184082,184.2778701782227,184.2778701782227,184.6413345336914,184.6413345336914,185.0040283203125,185.0040283203125,185.0040283203125,185.0793380737305,185.0793380737305,183.7827606201172,183.7827606201172,184.1363677978516,184.1363677978516,184.4971237182617,184.8675842285156,184.8675842285156,184.8675842285156,185.1230850219727,185.1230850219727,185.1230850219727,183.6945037841797,184.0280990600586,184.0280990600586,184.3959045410156,184.3959045410156,184.7695388793945,185.1415405273438,185.1415405273438,185.1660690307617,185.1660690307617,185.1660690307617,183.9945526123047,183.9945526123047,184.3630828857422,184.7299346923828,185.1033706665039,185.1033706665039,185.2083358764648,185.2083358764648,185.2083358764648,183.9784851074219,184.3444519042969,184.7119750976562,185.0855560302734,185.0855560302734,185.2499465942383,185.2499465942383,185.2499465942383,185.2499465942383,183.9803161621094,184.3457946777344,184.3457946777344,184.713752746582,184.713752746582,185.0884399414062,185.0884399414062,185.290885925293,185.290885925293,185.290885925293,184.0055847167969,184.0055847167969,184.3426971435547,184.3426971435547,184.3426971435547,184.7238998413086,185.111083984375,185.111083984375,185.3311462402344,185.3311462402344,185.3311462402344,184.0625762939453,184.0625762939453,184.3980407714844,184.3980407714844,184.7819595336914,185.1754150390625,185.1754150390625,185.3707427978516,185.3707427978516,185.3707427978516,184.1326065063477,184.1326065063477,184.4846496582031,184.4846496582031,184.8642120361328,185.2521896362305,185.4097366333008,185.4097366333008,185.4097366333008,184.2171859741211,184.2171859741211,184.5501098632812,184.5501098632812,184.936164855957,185.3325500488281,185.3325500488281,185.448127746582,185.448127746582,185.448127746582,184.313117980957,184.6601943969727,184.6601943969727,185.0389404296875,185.4225769042969,185.4225769042969,185.4857940673828,185.4857940673828,185.4857940673828,184.4480895996094,184.4480895996094,184.4480895996094,184.8346557617188,184.8346557617188,185.2198791503906,185.52294921875,185.52294921875,184.2771072387695,184.2771072387695,184.5930252075195,184.5930252075195,184.9719390869141,185.3578948974609,185.3578948974609,185.5594940185547,185.5594940185547,185.5594940185547,184.429313659668,184.429313659668,184.7981872558594,184.7981872558594,185.1764755249023,185.1764755249023,185.5553283691406,185.5553283691406,185.5953750610352,185.5953750610352,185.5953750610352,184.6485595703125,184.6485595703125,185.0191879272461,185.0191879272461,185.0191879272461,185.4017028808594,185.4017028808594,185.6307373046875,185.6307373046875,185.6307373046875,184.5060424804688,184.5060424804688,184.8353500366211,184.8353500366211,185.2192916870117,185.2192916870117,185.605339050293,185.605339050293,185.6655426025391,185.6655426025391,185.6655426025391,184.698112487793,185.0630798339844,185.0630798339844,185.4451065063477,185.4451065063477,185.6996917724609,185.6996917724609,185.6996917724609,184.5986480712891,184.5986480712891,184.9300689697266,184.9300689697266,185.3150939941406,185.3150939941406,185.7014083862305,185.7334136962891,185.7334136962891,185.7334136962891,184.8294982910156,184.8294982910156,185.2029190063477,185.5913543701172,185.5913543701172,185.7664947509766,185.7664947509766,185.7664947509766,184.785514831543,184.785514831543,184.785514831543,185.1624298095703,185.1624298095703,185.5484619140625,185.5484619140625,185.7990646362305,185.7990646362305,185.7990646362305,185.7990646362305,185.7990646362305,185.7990646362305,185.7990646362305,185.7990646362305,185.7990646362305,184.6767959594727,184.6767959594727,184.6767959594727,185.0320053100586,185.0320053100586,185.4165802001953,185.4165802001953,185.7963256835938,185.7963256835938,185.8309478759766,185.8309478759766,185.0150604248047,185.0150604248047,185.4053726196289,185.8014221191406,185.8625946044922,185.8625946044922,185.0382614135742,185.0382614135742,185.4336090087891,185.8255157470703,185.8935775756836,185.8935775756836,185.8935775756836,185.0857086181641,185.0857086181641,185.4875259399414,185.4875259399414,185.8752822875977,185.9242401123047,185.9242401123047,185.9242401123047,185.1399002075195,185.1399002075195,185.5238265991211,185.5238265991211,185.9072875976562,185.9072875976562,185.9542617797852,185.9542617797852,185.9542617797852,185.1587524414062,185.1587524414062,185.5280685424805,185.5280685424805,185.9144668579102,185.9144668579102,185.9838409423828,185.9838409423828,185.9838409423828,185.2193908691406,185.2193908691406,185.6103515625,185.6103515625,185.9950485229492,186.0129470825195,186.0129470825195,185.2747268676758,185.2747268676758,185.6532211303711,185.6532211303711,186.0415802001953,186.0415802001953,186.0415802001953,186.0415802001953,186.0415802001953,186.0415802001953,185.3419342041016,185.7300491333008,185.7300491333008,185.7300491333008,186.0697479248047,186.0697479248047,186.0697479248047,186.0697479248047,186.0697479248047,186.0697479248047,185.463249206543,185.463249206543,185.8574371337891,186.0974197387695,186.0974197387695,186.0974197387695,185.2172393798828,185.5422515869141,185.9301223754883,186.1246795654297,186.1246795654297,186.1246795654297,185.306884765625,185.306884765625,185.6886672973633,185.6886672973633,186.0703506469727,186.0703506469727,186.0703506469727,186.1514739990234,186.1514739990234,185.4022445678711,185.4022445678711,185.7616195678711,185.7616195678711,186.1446838378906,186.1778717041016,186.1778717041016,186.1778717041016,185.5080718994141,185.5080718994141,185.5080718994141,185.877799987793,185.877799987793,185.877799987793,186.2038269042969,186.2038269042969,186.2038269042969,185.3230895996094,185.3230895996094,185.6896362304688,186.0698928833008,186.0698928833008,186.2293548583984,186.2293548583984,185.4931716918945,185.4931716918945,185.8466033935547,185.8466033935547,186.2350616455078,186.2350616455078,186.2544937133789,186.2544937133789,185.6457214355469,185.6457214355469,186.0226821899414,186.0226821899414,186.2792358398438,186.2792358398438,186.2792358398438,185.4994125366211,185.4994125366211,185.8758087158203,185.8758087158203,186.2518539428711,186.2518539428711,186.3036346435547,186.3036346435547,186.3036346435547,185.7350463867188,186.1313934326172,186.1313934326172,186.3275604248047,186.3275604248047,185.6268463134766,185.6268463134766,186.0081939697266,186.0081939697266,186.3510513305664,186.3510513305664,186.3510513305664,186.3510513305664,186.3510513305664,186.3510513305664,186.3510513305664,186.3510513305664,185.8493270874023,185.8493270874023,186.2340393066406,186.3742446899414,186.3742446899414,186.3742446899414,186.3742446899414,186.3742446899414,186.3742446899414,186.3742446899414,186.3742446899414,186.3742446899414,186.3742446899414,186.3742446899414,186.3742446899414,186.3742446899414,186.3742446899414,186.3742446899414,186.3742446899414,186.3742446899414,186.3742446899414,186.3742446899414,186.3742446899414,186.3742446899414,186.3742446899414,185.5762329101562,185.5762329101562,185.9906539916992,185.9906539916992,186.3639678955078,186.7649078369141,187.120246887207,187.120246887207,187.4407958984375,187.4407958984375,187.7596664428711,187.7596664428711,188.0774154663086,188.0774154663086,188.3966293334961,188.3966293334961,188.7143936157227,188.7143936157227,188.9519882202148,188.9519882202148,188.9519882202148,185.7309875488281,185.7309875488281,186.1398391723633,186.1398391723633,186.5226821899414,186.9333419799805,186.9333419799805,187.3350524902344,187.3350524902344,187.7342681884766,188.1342849731445,188.5316314697266,188.5316314697266,188.9241790771484,189.044303894043,189.044303894043,186.0664138793945,186.0664138793945,186.4577560424805,186.8623275756836,186.8623275756836,187.2638168334961,187.2638168334961,187.6605682373047,187.6605682373047,188.0594940185547,188.4586486816406,188.4586486816406,188.8584899902344,189.1351165771484,189.1351165771484,189.1351165771484,186.0301055908203,186.3943939208984,186.7788238525391,186.7788238525391,186.7788238525391,187.183967590332,187.5776290893555,187.9681243896484,188.355094909668,188.7436752319336,189.1143951416016,189.1143951416016,189.2245788574219,189.2245788574219,186.3116455078125,186.6914672851562,186.6914672851562,187.0928039550781,187.4724655151367,187.4724655151367,187.8494415283203,187.8494415283203,188.2282638549805,188.2282638549805,188.6084976196289,188.6084976196289,188.9863739013672,189.3124771118164,189.3124771118164,189.3124771118164,189.3124771118164,186.6553421020508,186.6553421020508,187.0291595458984,187.0291595458984,187.4130477905273,187.4130477905273,187.7843399047852,187.7843399047852,188.1572875976562,188.1572875976562,188.53173828125,188.53173828125,188.9086303710938,188.9086303710938,189.2790679931641,189.2790679931641,189.3990707397461,189.3990707397461,186.5563278198242,186.5563278198242,186.5563278198242,186.9271469116211,187.3108444213867,187.3108444213867,187.6835708618164,187.6835708618164,188.0529479980469,188.0529479980469,188.4243087768555,188.7973251342773,188.7973251342773,188.7973251342773,189.16650390625,189.4841766357422,189.4841766357422,189.4841766357422,189.4841766357422,189.4841766357422,189.4841766357422,186.853874206543,186.853874206543,187.2351684570312,187.6327972412109,187.6327972412109,188.0160369873047,188.0160369873047,188.3684310913086,188.3684310913086,188.7553329467773,188.7553329467773,189.1417770385742,189.1417770385742,189.5160217285156,189.5160217285156,189.5679702758789,189.5679702758789,189.5679702758789,186.9059982299805,186.9059982299805,187.2915725708008,187.687858581543,188.0655975341797,188.0655975341797,188.4435729980469,188.4435729980469,188.8154067993164,188.8154067993164,189.1886520385742,189.5607604980469,189.5607604980469,189.6503295898438,189.6503295898438,186.9491806030273,186.9491806030273,186.9491806030273,187.3138656616211,187.6996688842773,188.0753860473633,188.0753860473633,188.0753860473633,188.4458312988281,188.4458312988281,188.8197326660156,188.8197326660156,189.1951141357422,189.1951141357422,189.5638122558594,189.5638122558594,189.7313919067383,189.7313919067383,189.7313919067383,187.0255279541016,187.0255279541016,187.3440628051758,187.725715637207,187.725715637207,188.0910491943359,188.0910491943359,188.4676361083984,188.4676361083984,188.8409805297852,188.8409805297852,189.2168807983398,189.2168807983398,189.594123840332,189.8111877441406,189.8111877441406,187.0898895263672,187.0898895263672,187.4144744873047,187.4144744873047,187.4144744873047,187.8064651489258,187.8064651489258,188.1899185180664,188.1899185180664,188.1899185180664,188.5624618530273,188.5624618530273,188.9407424926758,188.9407424926758,189.3209991455078,189.7035675048828,189.7035675048828,189.8895721435547,189.8895721435547,189.8895721435547,187.2496337890625,187.2496337890625,187.5700912475586,187.5700912475586,187.9552536010742,187.9552536010742,188.3348159790039,188.3348159790039,188.7102127075195,189.0893096923828,189.0893096923828,189.4747085571289,189.8563385009766,189.8563385009766,189.9668502807617,189.9668502807617,189.9668502807617,187.434196472168,187.8194732666016,188.2055435180664,188.2055435180664,188.2055435180664,188.5867233276367,188.9679641723633,188.9679641723633,189.3557662963867,189.3557662963867,189.7439880371094,190.0427703857422,190.0427703857422,190.0427703857422,190.0427703857422,190.0427703857422,190.0427703857422,187.7181625366211,187.7181625366211,188.096809387207,188.096809387207,188.4684295654297,188.4684295654297,188.8364028930664,189.2119979858398,189.588493347168,189.9662933349609,189.9662933349609,190.1175003051758,190.1175003051758,187.6234512329102,187.6234512329102,187.9940719604492,187.9940719604492,188.3659057617188,188.3659057617188,188.7345886230469,188.7345886230469,188.7345886230469,189.1037673950195,189.4775314331055,189.4775314331055,189.8585586547852,190.191032409668,190.191032409668,190.191032409668,190.191032409668,190.191032409668,190.191032409668,187.9207382202148,188.282096862793,188.282096862793,188.6451873779297,188.6451873779297,189.0089797973633,189.378288269043,189.7480316162109,189.7480316162109,190.1162948608398,190.2634048461914,190.2634048461914,190.2634048461914,187.8155136108398,188.1884002685547,188.1884002685547,188.5709762573242,188.5709762573242,188.9545288085938,189.3334197998047,189.3334197998047,189.7156066894531,189.7156066894531,190.101806640625,190.101806640625,190.3345260620117,190.3345260620117,190.3345260620117,190.3345260620117,190.3345260620117,190.3345260620117,188.2000732421875,188.2000732421875,188.5594329833984,188.5594329833984,188.9406433105469,189.3205413818359,189.3205413818359,189.703010559082,189.703010559082,190.0903091430664,190.0903091430664,190.0903091430664,190.4045791625977,190.4045791625977,190.4045791625977,190.4045791625977,190.4045791625977,190.4045791625977,188.2736968994141,188.6380004882812,188.6380004882812,189.0244216918945,189.0244216918945,189.4103775024414,189.7928695678711,190.1727294921875,190.1727294921875,190.4734649658203,190.4734649658203,190.4734649658203,190.4734649658203,188.3645401000977,188.3645401000977,188.3645401000977,188.7397689819336,189.1297607421875,189.1297607421875,189.5149459838867,189.5149459838867,189.9032821655273,189.9032821655273,190.2894821166992,190.5411834716797,190.5411834716797,190.5411834716797,190.5411834716797,190.5411834716797,190.5411834716797,190.5411834716797,190.5411834716797,190.5411834716797,190.5411834716797,190.5411834716797,190.5411834716797,190.5411834716797,190.5411834716797,188.2954177856445,188.6576385498047,188.6576385498047,189.0209045410156,189.0209045410156,189.376220703125,189.376220703125,189.7490615844727,189.7490615844727,190.1291656494141,190.1291656494141,190.1291656494141,190.5095748901367,190.5095748901367,190.6075057983398,190.6075057983398,190.6075057983398,188.4327087402344,188.4327087402344,188.4327087402344,188.7989044189453,188.7989044189453,189.1830825805664,189.1830825805664,189.5701370239258,189.5701370239258,189.9502258300781,189.9502258300781,189.9502258300781,190.3351974487305,190.6730575561523,190.6730575561523,190.6730575561523,190.6730575561523,188.6776504516602,189.0459060668945,189.4181289672852,189.4181289672852,189.7936706542969,189.7936706542969,190.1771011352539,190.550163269043,190.7376861572266,190.7376861572266,190.7376861572266,188.5776138305664,188.5776138305664,188.9175643920898,188.9175643920898,189.2847671508789,189.6607131958008,190.0419464111328,190.0419464111328,190.425666809082,190.8011474609375,190.8011474609375,190.8011474609375,190.8011474609375,188.8100814819336,188.8100814819336,189.145637512207,189.145637512207,189.5203094482422,189.8980560302734,189.8980560302734,189.8980560302734,190.2850341796875,190.6740112304688,190.6740112304688,190.8636932373047,190.8636932373047,190.8636932373047,188.7611770629883,189.0759353637695,189.0759353637695,189.0759353637695,189.4418029785156,189.4418029785156,189.820182800293,190.1988220214844,190.1988220214844,190.5864105224609,190.5864105224609,190.9251327514648,190.9251327514648,190.9251327514648,190.9251327514648,190.9251327514648,190.9251327514648,189.0931549072266,189.4565658569336,189.4565658569336,189.8343811035156,189.8343811035156,190.2155227661133,190.2155227661133,190.5989532470703,190.5989532470703,190.9843292236328,190.9856796264648,190.9856796264648,190.9856796264648,189.0815734863281,189.0815734863281,189.4149551391602,189.4149551391602,189.7918930053711,189.7918930053711,190.1708068847656,190.5550231933594,190.5550231933594,190.9435272216797,190.9435272216797,191.0451507568359,191.0451507568359,191.0451507568359,189.1203308105469,189.1203308105469,189.4591598510742,189.4591598510742,189.8451080322266,190.2232055664062,190.2232055664062,190.2232055664062,190.6095962524414,190.6095962524414,191.0003890991211,191.0003890991211,191.1037368774414,191.1037368774414,191.1037368774414,189.2013473510742,189.5261001586914,189.5261001586914,189.8986206054688,190.2833251953125,190.2833251953125,190.672119140625,191.0622253417969,191.0622253417969,191.1613616943359,191.1613616943359,191.1613616943359,189.2974243164062,189.2974243164062,189.6238784790039,189.6238784790039,189.9944839477539,190.3822555541992,190.3822555541992,190.7577743530273,190.7577743530273,191.1481857299805,191.1481857299805,191.2180252075195,191.2180252075195,191.2180252075195,189.3832015991211,189.3832015991211,189.7449951171875,189.7449951171875,190.1386108398438,190.1386108398438,190.5255126953125,190.9156036376953,190.9156036376953,191.2737731933594,191.2737731933594,191.2737731933594,191.2737731933594,191.2737731933594,191.2737731933594,189.561897277832,189.561897277832,189.9056854248047,190.2854232788086,190.6654434204102,190.6654434204102,191.0507736206055,191.0507736206055,191.3286285400391,191.3286285400391,191.3286285400391,191.3286285400391,189.7028427124023,190.0620956420898,190.0620956420898,190.4459228515625,190.4459228515625,190.8308563232422,191.2319946289062,191.2319946289062,191.3826141357422,191.3826141357422,191.3826141357422,189.595344543457,189.9164581298828,189.9164581298828,190.2965469360352,190.6800918579102,190.6800918579102,191.0693435668945,191.0693435668945,191.4357070922852,191.4357070922852,191.4357070922852,191.4357070922852,191.4357070922852,191.4357070922852,191.4357070922852,191.4357070922852,189.8150253295898,189.8150253295898,190.1648254394531,190.5538864135742,190.5538864135742,190.9410552978516,191.3305892944336,191.3305892944336,191.4879608154297,191.4879608154297,191.4879608154297,189.7553482055664,189.7553482055664,190.0717391967773,190.0717391967773,190.4504089355469,190.4504089355469,190.8329467773438,190.8329467773438,191.2203826904297,191.5392990112305,191.5392990112305,191.5392990112305,191.5392990112305,190.0135955810547,190.3685836791992,190.3685836791992,190.7538146972656,190.7538146972656,191.1387634277344,191.1387634277344,191.5288314819336,191.5288314819336,191.5899124145508,191.5899124145508,191.5899124145508,190.0096740722656,190.0096740722656,190.3764038085938,190.7635040283203,190.7635040283203,191.1493988037109,191.1493988037109,191.5419387817383,191.5419387817383,191.5419387817383,191.6396713256836,191.6396713256836,191.6396713256836,190.0351257324219,190.0351257324219,190.3704147338867,190.7579040527344,190.7579040527344,191.1476211547852,191.1476211547852,191.5336608886719,191.5336608886719,191.688606262207,191.688606262207,191.688606262207,190.0457382202148,190.0457382202148,190.3858413696289,190.3858413696289,190.7800140380859,191.1672668457031,191.5599517822266,191.5599517822266,191.7367935180664,191.7367935180664,191.7367935180664,191.7367935180664,191.7367935180664,191.7367935180664,191.7367935180664,191.7367935180664,191.7367935180664,191.7367935180664,190.1648330688477,190.1648330688477,190.4906997680664,190.4906997680664,190.8730239868164,190.8730239868164,191.2492294311523,191.6363754272461,191.6363754272461,191.7840805053711,191.7840805053711,191.7840805053711,190.2012939453125,190.2012939453125,190.5264358520508,190.5264358520508,190.9172592163086,190.9172592163086,190.9172592163086,191.3043441772461,191.3043441772461,191.3043441772461,191.7069320678711,191.7069320678711,191.8307647705078,191.8307647705078,191.8307647705078,190.2959060668945,190.2959060668945,190.6153182983398,190.6153182983398,190.9983139038086,191.3873443603516,191.3873443603516,191.7838134765625,191.7838134765625,191.8766403198242,191.8766403198242,190.4016952514648,190.4016952514648,190.7440414428711,190.7440414428711,191.1448593139648,191.5261001586914,191.9123229980469,191.9123229980469,191.9218292236328,191.9218292236328,191.9218292236328,191.9218292236328,190.5255508422852,190.5255508422852,190.863166809082,191.2488784790039,191.2488784790039,191.6266937255859,191.6266937255859,191.6266937255859,191.9662322998047,191.9662322998047,191.9662322998047,191.9662322998047,191.9662322998047,191.9662322998047,190.646240234375,190.646240234375,191.0030975341797,191.3981628417969,191.7911758422852,191.7911758422852,192.0099487304688,192.0099487304688,190.5144958496094,190.5144958496094,190.8357467651367,190.8357467651367,191.2307357788086,191.2307357788086,191.627555847168,192.0276412963867,192.0529098510742,192.0529098510742,190.7438201904297,190.7438201904297,191.1019058227539,191.1019058227539,191.5030670166016,191.5030670166016,191.5030670166016,191.9029541015625,191.9029541015625,192.0952911376953,192.0952911376953,192.0952911376953,190.6600189208984,191.0304489135742,191.0304489135742,191.4330139160156,191.4330139160156,191.820442199707,191.820442199707,192.1368713378906,192.1368713378906,192.1368713378906,192.1368713378906,192.1368713378906,192.1368713378906,190.9255676269531,190.9255676269531,191.2891387939453,191.2891387939453,191.6794128417969,191.6794128417969,192.0667419433594,192.1778182983398,192.1778182983398,190.8403091430664,190.8403091430664,191.1573486328125,191.1573486328125,191.1573486328125,191.5455474853516,191.5455474853516,191.9310607910156,191.9310607910156,192.2181015014648,192.2181015014648,192.2181015014648,192.2181015014648,192.2181015014648,192.2181015014648,192.2181015014648,192.2181015014648,191.0757522583008,191.4452667236328,191.4452667236328,191.8335876464844,191.8335876464844,191.8335876464844,192.217155456543,192.217155456543,192.2577133178711,192.2577133178711,192.2577133178711,192.2577133178711,191.0333404541016,191.0333404541016,191.3762588500977,191.3762588500977,191.7664794921875,191.7664794921875,192.1539306640625,192.2966842651367,192.2966842651367,191.0155029296875,191.0155029296875,191.3552093505859,191.759895324707,191.759895324707,192.16064453125,192.3350830078125,192.3350830078125,192.3350830078125,191.0591430664062,191.0591430664062,191.3867568969727,191.3867568969727,191.7890167236328,191.7890167236328,192.1890335083008,192.1890335083008,192.3727798461914,192.3727798461914,192.3727798461914,192.3727798461914,192.3727798461914,192.3727798461914,191.1381378173828,191.1381378173828,191.4574432373047,191.4574432373047,191.8477249145508,191.8477249145508,191.8477249145508,192.2402420043945,192.2402420043945,192.4099426269531,192.4099426269531,192.4099426269531,191.1692810058594,191.474739074707,191.474739074707,191.8194198608398,191.8194198608398,192.2069473266602,192.4464721679688,192.4464721679688,192.4464721679688,192.4464721679688,191.4539489746094,191.8383483886719,192.2270278930664,192.4823913574219,192.4823913574219,192.4823913574219,192.4823913574219,192.4823913574219,192.4823913574219,192.4823913574219,192.4823913574219,192.4823913574219,192.4823913574219,192.4823913574219,192.4823913574219,191.2448501586914,191.2448501586914,191.2448501586914,191.5784225463867,191.5784225463867,191.5784225463867,191.9735794067383,191.9735794067383,191.9735794067383,192.3422546386719,192.3422546386719,192.5176239013672,192.5176239013672,192.5176239013672,192.5176239013672,192.5176239013672,192.5176239013672,192.5176239013672,192.5176239013672,192.5176239013672,192.5176239013672,192.5176239013672,192.5176239013672,192.5176239013672,192.5176239013672,192.5176239013672,192.5176239013672,192.5176239013672,192.5176239013672,192.5176239013672,192.5176239013672,192.5176239013672,192.5176239013672,192.5176239013672,192.5176239013672,192.5176239013672,192.5176239013672,192.5176239013672,192.5176239013672,192.5176239013672,192.5176239013672,192.5176239013672,192.5176239013672,192.5176239013672,192.5176239013672,192.5176239013672,192.5176239013672,192.5176239013672,192.5176239013672,192.5176239013672,192.5176239013672,192.5176239013672,192.5176239013672,192.5176239013672,192.5176239013672,192.5176239013672,192.5176239013672,191.3001251220703,191.3001251220703,191.3994293212891,191.7956161499023,191.7956161499023,191.7956161499023,192.2100830078125,192.2100830078125,192.2100830078125,192.5727920532227,192.5727920532227,192.5727920532227,192.9736175537109,193.372932434082,193.372932434082,193.7144088745117,193.7144088745117,194.0388793945312,194.0388793945312,194.361213684082,194.361213684082,194.6858596801758,194.6858596801758,195.0087890625,195.0087890625,195.331657409668,195.331657409668,195.6537246704102,195.977653503418,196.3004531860352,196.3004531860352,196.598274230957,196.598274230957,196.598274230957,196.598274230957,191.6985321044922,191.6985321044922,192.1221160888672,192.1221160888672,192.4993896484375,192.4993896484375,192.8851013183594,192.8851013183594,193.2847061157227,193.2847061157227,193.6865310668945,193.6865310668945,194.0883255004883,194.4905395507812,194.4905395507812,194.4905395507812,194.8927307128906,194.8927307128906,194.8927307128906,195.2940979003906,195.6950225830078,195.6950225830078,196.0956420898438,196.0956420898438,196.4879608154297,196.4879608154297,196.7431716918945,196.7431716918945,196.7431716918945,196.7431716918945,191.9823837280273,191.9823837280273,192.375114440918,192.375114440918,192.7358932495117,192.7358932495117,193.1414413452148,193.1414413452148,193.538330078125,193.538330078125,193.9377288818359,193.9377288818359,194.3332824707031,194.3332824707031,194.7232131958008,195.1127166748047,195.1127166748047,195.5021057128906,195.5021057128906,195.8909378051758,195.8909378051758,196.2803649902344,196.2803649902344,196.661979675293,196.8857345581055,196.8857345581055,196.8857345581055,196.8857345581055,196.8857345581055,196.8857345581055,192.2208251953125,192.2208251953125,192.6217193603516,192.6217193603516,192.9846038818359,192.9846038818359,193.3805465698242,193.7675933837891,193.7675933837891,194.1552200317383,194.1552200317383,194.5418014526367,194.5418014526367,194.5418014526367,194.9234771728516,194.9234771728516,195.3127746582031,195.700813293457,195.700813293457,196.090705871582,196.4804534912109,196.4804534912109,196.8577346801758,196.8577346801758,197.026008605957,197.026008605957,197.026008605957,197.026008605957,197.026008605957,197.026008605957,197.026008605957,197.026008605957,197.026008605957,192.1995468139648,192.1995468139648,192.1995468139648,192.4801559448242,192.4801559448242,192.4801559448242,192.855110168457,193.2097930908203,193.2097930908203,193.5940399169922,193.5940399169922,193.9748458862305,193.9748458862305,193.9748458862305,194.3512649536133,194.3512649536133,194.7276840209961,195.1054153442383,195.1054153442383,195.4822006225586,195.4822006225586,195.4822006225586,195.8596267700195,195.8596267700195,196.2333908081055,196.2333908081055,196.6136703491211,196.6136703491211,197.0058441162109,197.0058441162109,197.1639862060547,197.1639862060547,197.1639862060547,197.1639862060547,197.1639862060547,197.1639862060547,192.683723449707,192.683723449707,193.0383911132812,193.0383911132812,193.4038772583008,193.7797698974609,193.7797698974609,194.1714096069336,194.1714096069336,194.5548629760742,194.5548629760742,194.9287643432617,194.9287643432617,195.3021774291992,195.3021774291992,195.6732025146484,196.049186706543,196.049186706543,196.4242095947266,196.4242095947266,196.8012771606445,196.8012771606445,197.1783828735352,197.1783828735352,197.2998123168945,197.2998123168945,197.2998123168945,197.2998123168945,197.2998123168945,197.2998123168945,192.9404602050781,192.9404602050781,193.2926406860352,193.2926406860352,193.6772766113281,193.6772766113281,194.0570068359375,194.0570068359375,194.4314727783203,194.4314727783203,194.8015670776367,194.8015670776367,195.1736068725586,195.1736068725586,195.5467987060547,195.5467987060547,195.9156494140625,195.9156494140625,196.2927322387695,196.2927322387695,196.6705322265625,196.6705322265625,197.0447235107422,197.4186019897461,197.4186019897461,197.433349609375,197.433349609375,197.433349609375,197.433349609375,192.8517379760742,193.2001953125,193.2001953125,193.5637512207031,193.5637512207031,193.9487380981445,194.3258895874023,194.3258895874023,194.705696105957,195.0814590454102,195.0814590454102,195.4615859985352,195.4615859985352,195.8377532958984,195.8377532958984,196.2087097167969,196.2087097167969,196.5807723999023,196.9583511352539,196.9583511352539,197.3322830200195,197.3322830200195,197.5647964477539,197.5647964477539,197.5647964477539,197.5647964477539,197.5647964477539,197.5647964477539,193.2273635864258,193.2273635864258,193.5811080932617,193.5811080932617,193.9622573852539,193.9622573852539,194.3334274291992,194.3334274291992,194.7050476074219,194.7050476074219,195.07763671875,195.07763671875,195.4543304443359,195.4543304443359,195.8273773193359,195.8273773193359,196.2059478759766,196.5840454101562,196.5840454101562,196.9611282348633,196.9611282348633,197.3405227661133,197.3405227661133,197.6941070556641,197.6941070556641,197.6941070556641,197.6941070556641,197.6941070556641,197.6941070556641,193.2685928344727,193.2685928344727,193.6007919311523,193.6007919311523,193.9629745483398,193.9629745483398,194.3327331542969,194.3327331542969,194.7033081054688,194.7033081054688,195.0747909545898,195.0747909545898,195.4455184936523,195.8181076049805,195.8181076049805,195.8181076049805,196.1940231323242,196.5704727172852,196.9511337280273,196.9511337280273,197.3291702270508,197.3291702270508,197.6993637084961,197.6993637084961,197.8213348388672,197.8213348388672,197.8213348388672,197.8213348388672,197.8213348388672,197.8213348388672,193.6971740722656,194.0212783813477,194.4072189331055,194.783576965332,194.783576965332,195.0794372558594,195.0794372558594,195.4564971923828,195.4564971923828,195.8490371704102,196.2238540649414,196.6002731323242,196.6002731323242,196.9782943725586,197.3585052490234,197.3585052490234,197.7306823730469,197.7306823730469,197.9465103149414,197.9465103149414,197.9465103149414,197.9465103149414,197.9465103149414,197.9465103149414,193.8151702880859,193.8151702880859,194.1729049682617,194.1729049682617,194.546142578125,194.9076843261719,194.9076843261719,195.2717590332031,195.2717590332031,195.6423568725586,195.6423568725586,196.0196380615234,196.0196380615234,196.3979415893555,196.7754516601562,196.7754516601562,197.1504440307617,197.1504440307617,197.5267791748047,197.8965682983398,197.8965682983398,198.0696487426758,198.0696487426758,198.0696487426758,198.0696487426758,194.0143356323242,194.0143356323242,194.3312301635742,194.6856918334961,195.0505218505859,195.0505218505859,195.4272766113281,195.4272766113281,195.796630859375,196.1625671386719,196.1625671386719,196.5359268188477,196.5359268188477,196.9091644287109,196.9091644287109,197.287727355957,197.6698684692383,197.6698684692383,197.6698684692383,198.0415191650391,198.0415191650391,198.0415191650391,198.1908416748047,198.1908416748047,198.1908416748047,198.1908416748047,198.1908416748047,198.1908416748047,194.2100219726562,194.2100219726562,194.2100219726562,194.5469131469727,194.5469131469727,194.9134826660156,194.9134826660156,195.2694244384766,195.627685546875,195.627685546875,195.991325378418,196.3668975830078,196.7510833740234,196.7510833740234,197.1297836303711,197.1297836303711,197.5060577392578,197.8862457275391,197.8862457275391,197.8862457275391,198.2491226196289,198.2491226196289,198.3100662231445,198.3100662231445,198.3100662231445,198.3100662231445,194.510986328125,194.510986328125,194.888069152832,195.2592010498047,195.2592010498047,195.6254730224609,195.6254730224609,196.0016403198242,196.0016403198242,196.3812484741211,196.3812484741211,196.7634353637695,196.7634353637695,197.1594924926758,197.1594924926758,197.5572509765625,197.5572509765625,197.9441146850586,198.3212585449219,198.3212585449219,198.427375793457,198.427375793457,198.427375793457,198.427375793457,194.6325454711914,194.9904251098633,195.3564682006836,195.7142639160156,196.0852966308594,196.4615097045898,196.4615097045898,196.8438415527344,196.8438415527344,196.8438415527344,197.2283401489258,197.6158981323242,198.0050582885742,198.3834915161133,198.3834915161133,198.5427780151367,198.5427780151367,198.5427780151367,198.5427780151367,198.5427780151367,198.5427780151367,194.7867126464844,194.7867126464844,195.1397247314453,195.1397247314453,195.5057678222656,195.5057678222656,195.8648452758789,196.2394561767578,196.2394561767578,196.2394561767578,196.6197128295898,196.6197128295898,197.0035018920898,197.0035018920898,197.3905410766602,197.3905410766602,197.7800979614258,198.1715850830078,198.5513381958008,198.5513381958008,198.5513381958008,198.6562881469727,198.6562881469727,198.6562881469727,198.6562881469727,198.6562881469727,198.6562881469727,195.0062713623047,195.3644180297852,195.7233200073242,196.0841827392578,196.0841827392578,196.4587936401367,196.8414001464844,197.2269134521484,197.2269134521484,197.6123733520508,198.0014038085938,198.0014038085938,198.3927230834961,198.3927230834961,198.7670059204102,198.7680587768555,198.7680587768555,198.7680587768555,194.9491958618164,194.9491958618164,195.2665252685547,195.6300430297852,195.6300430297852,195.9859085083008,195.9859085083008,196.3538970947266,196.3538970947266,196.7352600097656,196.7352600097656,197.1223297119141,197.1223297119141,197.5111618041992,197.5111618041992,197.9031600952148,197.9031600952148,198.2971954345703,198.6868591308594,198.6868591308594,198.8779296875,198.8779296875,198.8779296875,198.8779296875,198.8779296875,198.8779296875,195.2766189575195,195.2766189575195,195.6138687133789,195.9789276123047,195.9789276123047,196.3472518920898,196.72802734375,196.72802734375,197.1073608398438,197.1073608398438,197.4898834228516,197.4898834228516,197.8759307861328,197.8759307861328,198.2630920410156,198.2630920410156,198.6540069580078,198.6540069580078,198.9860229492188,198.9860229492188,198.9860229492188,198.9860229492188,198.9860229492188,198.9860229492188,195.3072967529297,195.3072967529297,195.6698455810547,195.6698455810547,196.0281753540039,196.0281753540039,196.3775939941406,196.7421646118164,196.7421646118164,197.1198043823242,197.1198043823242,197.5009613037109,197.5009613037109,197.5009613037109,197.8845138549805,198.2709121704102,198.2709121704102,198.6601181030273,198.6601181030273,199.0356597900391,199.0356597900391,199.0924911499023,199.0924911499023,199.0924911499023,199.0924911499023,195.7153167724609,196.0777816772461,196.0777816772461,196.4377136230469,196.4377136230469,196.8011093139648,196.8011093139648,197.1728210449219,197.5465545654297,197.5465545654297,197.9246673583984,198.3079223632812,198.3079223632812,198.6967926025391,198.6967926025391,199.077392578125,199.077392578125,199.077392578125,199.1970748901367,199.1970748901367,199.1970748901367,199.1970748901367,199.1970748901367,199.1970748901367,195.8000106811523,195.8000106811523,196.133430480957,196.133430480957,196.4808807373047,196.4808807373047,196.8374633789062,196.8374633789062,197.2234878540039,197.2234878540039,197.603271484375,197.603271484375,197.9862823486328,197.9862823486328,198.373779296875,198.373779296875,198.7629470825195,198.7629470825195,199.1474609375,199.3000793457031,199.3000793457031,199.3000793457031,199.3000793457031,199.3000793457031,199.3000793457031,199.3000793457031,199.3000793457031,195.9280395507812,196.2493133544922,196.2493133544922,196.5960693359375,196.5960693359375,196.9504928588867,196.9504928588867,197.3213195800781,197.6990509033203,197.6990509033203,198.0807113647461,198.0807113647461,198.4643707275391,198.8535079956055,198.8535079956055,199.2346420288086,199.2346420288086,199.4013671875,199.4013671875,199.4013671875,199.4013671875,199.4013671875,199.4013671875,196.1248092651367,196.4739379882812,196.4739379882812,196.8246078491211,197.1881256103516,197.1881256103516,197.5619125366211,197.5619125366211,197.9389419555664,198.3201370239258,198.3201370239258,198.7044143676758,199.0867767333984,199.4601058959961,199.5010299682617,199.5010299682617,199.5010299682617,199.5010299682617,199.5010299682617,199.5010299682617,199.5010299682617,199.5010299682617,199.5010299682617,199.5010299682617,199.5010299682617,199.5010299682617,199.5010299682617,199.5010299682617,199.5010299682617,199.5010299682617,199.5010299682617,199.5010299682617,199.5010299682617,199.5010299682617,199.5010299682617,199.5010299682617,196.3814926147461,196.703498840332,197.0624084472656,197.0624084472656,197.4380874633789,197.4380874633789,197.8262405395508,197.8262405395508,198.2191467285156,198.2191467285156,198.6170654296875,199.0154800415039,199.0154800415039,199.0154800415039,199.4073181152344,199.4073181152344,199.4073181152344,199.5987854003906,199.5987854003906,199.5987854003906,199.5987854003906,199.5987854003906,199.5987854003906,196.39306640625,196.39306640625,196.7112274169922,197.0582427978516,197.0582427978516,197.4247131347656,197.804557800293,197.804557800293,198.1919937133789,198.1919937133789,198.5841979980469,198.5841979980469,198.9777908325195,198.9777908325195,199.376106262207,199.6953430175781,199.6953430175781,199.6953430175781,199.6953430175781,199.6953430175781,199.6953430175781,196.4158020019531,196.4158020019531,196.7306594848633,196.7306594848633,197.0825958251953,197.0825958251953,197.4484329223633,197.8288955688477,197.8288955688477,198.2177734375,198.2177734375,198.6101531982422,198.6101531982422,199.0053100585938,199.0053100585938,199.3999328613281,199.7799072265625,199.790283203125,199.790283203125,199.790283203125,199.790283203125,196.7938232421875,196.7938232421875,196.7938232421875,197.1460952758789,197.5042953491211,197.5042953491211,197.8700561523438,198.2402801513672,198.2402801513672,198.5813217163086,198.8300933837891,199.1630935668945,199.1630935668945,199.1630935668945,199.5433502197266,199.5433502197266,199.8837509155273,199.8837509155273,199.8837509155273,199.8837509155273,199.8837509155273,199.8837509155273,199.8837509155273,199.8837509155273,199.8837509155273,196.9562377929688,196.9562377929688,196.9562377929688,197.2875289916992,197.2875289916992,197.6344833374023,197.9881896972656,197.9881896972656,198.3540420532227,198.7229232788086,198.7229232788086,199.0951156616211,199.0951156616211,199.4680557250977,199.8349533081055,199.9756317138672,199.9756317138672,199.9756317138672,199.9756317138672,199.9756317138672,199.9756317138672,197.0094680786133,197.0094680786133,197.3520355224609,197.3520355224609,197.7050552368164,197.7050552368164,198.0686416625977,198.4424743652344,198.8199310302734,199.1989593505859,199.5839004516602,199.5839004516602,199.9619216918945,200.0661010742188,200.0661010742188,200.0661010742188,200.0661010742188,200.0661010742188,200.0661010742188,197.1980285644531,197.1980285644531,197.5378036499023,197.8909759521484,197.8909759521484,198.2533187866211,198.6211776733398,198.6211776733398,198.9960021972656,199.3727188110352,199.3727188110352,199.7522583007812,199.7522583007812,199.7522583007812,200.1206207275391,200.1206207275391,200.1550216674805,200.1550216674805,200.1550216674805,200.1550216674805,197.3347091674805,197.6448822021484,197.9939575195312,197.9939575195312,198.3615875244141,198.3615875244141,198.7407302856445,198.7407302856445,199.1220397949219,199.5066833496094,199.5066833496094,199.893798828125,199.893798828125,200.2426452636719,200.2426452636719,200.2426452636719,200.2426452636719,200.2426452636719,200.2426452636719,200.2426452636719,200.2426452636719,200.2426452636719,197.5134353637695,197.8287887573242,197.8287887573242,198.1870880126953,198.5590972900391,198.5590972900391,198.9395980834961,199.3254776000977,199.7111587524414,199.7111587524414,200.0992736816406,200.0992736816406,200.3286743164062,200.3286743164062,200.3286743164062,200.3286743164062,197.4415512084961,197.4415512084961,197.760627746582,198.1204986572266,198.1204986572266,198.4849319458008,198.4849319458008,198.8610000610352,198.8610000610352,199.2373580932617,199.2373580932617,199.6208419799805,200.0028076171875,200.0028076171875,200.3685455322266,200.413459777832,200.413459777832,200.413459777832,200.413459777832,200.413459777832,200.413459777832,197.7267074584961,197.7267074584961,198.0773239135742,198.4431228637695,198.8123931884766,199.1812362670898,199.1812362670898,199.5591735839844,199.5591735839844,199.9347381591797,200.2758026123047,200.2758026123047,200.4575881958008,200.4967956542969,200.4967956542969,200.4967956542969,200.4967956542969,200.4967956542969,200.4967956542969,200.4967956542969,200.4967956542969,200.4967956542969,200.4967956542969,200.4967956542969,200.4967956542969,200.4967956542969,200.4967956542969,200.4967956542969,200.4967956542969,197.6580810546875,197.6580810546875,197.7810440063477,197.7810440063477,197.999870300293,197.999870300293,198.3059310913086,198.3059310913086,198.3059310913086,198.609130859375,198.609130859375,198.9152679443359,199.2297744750977,199.5464019775391,199.8662643432617,199.8662643432617,200.1869964599609,200.1869964599609,200.505485534668,200.505485534668,200.5788497924805,200.5788497924805,200.5788497924805,200.5788497924805,200.5788497924805,200.5788497924805,197.8866577148438,197.8866577148438,198.1807556152344,198.1807556152344,198.4004745483398,198.4004745483398,198.6798782348633,199.004508972168,199.3287963867188,199.6602630615234,199.6602630615234,199.995719909668,199.995719909668,200.3373794555664,200.3373794555664,200.3373794555664,200.6583709716797,200.6595458984375,200.6595458984375,200.6595458984375,200.6595458984375,200.6595458984375,200.6595458984375,198.0859603881836,198.0859603881836,205.8545684814453,205.8545684814453,205.8545684814453,205.8545684814453,205.8545684814453,205.8545684814453,205.8545684814453,205.8545684814453,205.8545684814453,205.8545684814453,205.8545684814453,205.8545684814453,205.8545684814453,205.8545684814453,213.4839630126953,213.4839706420898,213.4839706420898,213.4839706420898,213.4839706420898,213.4839706420898,213.4839706420898,213.4839706420898,213.4839706420898,213.4839706420898,213.4839706420898,213.4839706420898,213.4839706420898,213.4839706420898,213.4839706420898,213.4839706420898,213.4839706420898,228.7427597045898,228.7427597045898,228.7427597045898,228.7427597045898,228.7427597045898,228.7427597045898,228.7427597045898,228.7427597045898,228.7427597045898,228.7427597045898,228.7427597045898,228.7427597045898],"meminc":[0,0,0,15.25894165039062,0,0,0.000396728515625,0,0,30.03691864013672,0,0,0,0,0,4.57763671875e-05,0,-0.00064849853515625,0,0,0,0,0,-0.00018310546875,0,15.55645751953125,0,0,0.4227066040039062,0,0.4018402099609375,0,0.3787155151367188,0,0.3274612426757812,0.1055755615234375,0,0,-1.561042785644531,0.4138946533203125,0.4082794189453125,0.40826416015625,0,0.3641281127929688,0,0,-1.746475219726562,0,0.373291015625,0.4144363403320312,0,0,0.40478515625,0.3980331420898438,0,0.2073593139648438,0,0,-1.59246826171875,0,0.3821029663085938,0.4019775390625,0.4029922485351562,0,0.3979644775390625,0.0579681396484375,0,0,-1.379425048828125,0.3980026245117188,0.3935699462890625,0.3962249755859375,0.2414321899414062,0,0,-1.553634643554688,0,0.40582275390625,0,0.3925399780273438,0,0.3927001953125,0,0.3899307250976562,0,0,0.0215911865234375,0,0,-1.351394653320312,0,0.392578125,0,0.3897628784179688,0,0.395477294921875,0,0.2217788696289062,0,-1.512504577636719,0.3680953979492188,0.3907546997070312,0,0.39324951171875,0,0.3865890502929688,0,0.02117919921875,0,0,-1.277687072753906,0,0.3834609985351562,0.3659896850585938,0,0.3639373779296875,0,0.2109222412109375,0,0,-1.496467590332031,0,0.3291778564453125,0,0.360992431640625,0,0.3687057495117188,0.376007080078125,0,0.1075363159179688,0,0,0,0,0,-1.263687133789062,0,0.360626220703125,0,0.364288330078125,0,0.3671112060546875,0.216644287109375,0,0,-1.451934814453125,0,0.3329010009765625,0,0.361968994140625,0,0.36346435546875,0,0.3626937866210938,0,0,0.07530975341796875,0,-1.296577453613281,0,0.353607177734375,0,0.3607559204101562,0.3704605102539062,0,0,0.2555007934570312,0,0,-1.428581237792969,0.3335952758789062,0,0.3678054809570312,0,0.3736343383789062,0.3720016479492188,0,0.02452850341796875,0,0,-1.171516418457031,0,0.3685302734375,0.366851806640625,0.3734359741210938,0,0.1049652099609375,0,0,-1.229850769042969,0.365966796875,0.367523193359375,0.3735809326171875,0,0.1643905639648438,0,0,0,-1.269630432128906,0.365478515625,0,0.3679580688476562,0,0.3746871948242188,0,0.2024459838867188,0,0,-1.285301208496094,0,0.3371124267578125,0,0,0.3812026977539062,0.3871841430664062,0,0.220062255859375,0,0,-1.268569946289062,0,0.3354644775390625,0,0.3839187622070312,0.3934555053710938,0,0.1953277587890625,0,0,-1.238136291503906,0,0.3520431518554688,0,0.3795623779296875,0.3879776000976562,0.1575469970703125,0,0,-1.192550659179688,0,0.3329238891601562,0,0.3860549926757812,0.3963851928710938,0,0.1155776977539062,0,0,-1.135009765625,0.347076416015625,0,0.3787460327148438,0.383636474609375,0,0.0632171630859375,0,0,-1.037704467773438,0,0,0.386566162109375,0,0.385223388671875,0.303070068359375,0,-1.245841979980469,0,0.31591796875,0,0.3789138793945312,0.385955810546875,0,0.20159912109375,0,0,-1.130180358886719,0,0.3688735961914062,0,0.3782882690429688,0,0.3788528442382812,0,0.04004669189453125,0,0,-0.9468154907226562,0,0.3706283569335938,0,0,0.3825149536132812,0,0.229034423828125,0,0,-1.12469482421875,0,0.3293075561523438,0,0.383941650390625,0,0.38604736328125,0,0.06020355224609375,0,0,-0.9674301147460938,0.3649673461914062,0,0.3820266723632812,0,0.2545852661132812,0,0,-1.101043701171875,0,0.3314208984375,0,0.3850250244140625,0,0.3863143920898438,0.03200531005859375,0,0,-0.9039154052734375,0,0.3734207153320312,0.3884353637695312,0,0.175140380859375,0,0,-0.9809799194335938,0,0,0.3769149780273438,0,0.3860321044921875,0,0.2506027221679688,0,0,0,0,0,0,0,0,-1.122268676757812,0,0,0.3552093505859375,0,0.3845748901367188,0,0.3797454833984375,0,0.0346221923828125,0,-0.815887451171875,0,0.3903121948242188,0.3960494995117188,0.0611724853515625,0,-0.8243331909179688,0,0.3953475952148438,0.39190673828125,0.06806182861328125,0,0,-0.8078689575195312,0,0.4018173217773438,0,0.38775634765625,0.04895782470703125,0,0,-0.7843399047851562,0,0.3839263916015625,0,0.3834609985351562,0,0.04697418212890625,0,0,-0.7955093383789062,0,0.3693161010742188,0,0.3863983154296875,0,0.06937408447265625,0,0,-0.7644500732421875,0,0.390960693359375,0,0.3846969604492188,0.0178985595703125,0,-0.73822021484375,0,0.3784942626953125,0,0.3883590698242188,0,0,0,0,0,-0.69964599609375,0.3881149291992188,0,0,0.3396987915039062,0,0,0,0,0,-0.6064987182617188,0,0.3941879272460938,0.2399826049804688,0,0,-0.8801803588867188,0.32501220703125,0.3878707885742188,0.1945571899414062,0,0,-0.8177947998046875,0,0.3817825317382812,0,0.381683349609375,0,0,0.08112335205078125,0,-0.7492294311523438,0,0.359375,0,0.3830642700195312,0.0331878662109375,0,0,-0.6697998046875,0,0,0.3697280883789062,0,0,0.3260269165039062,0,0,-0.8807373046875,0,0.366546630859375,0.3802566528320312,0,0.1594619750976562,0,-0.7361831665039062,0,0.3534317016601562,0,0.388458251953125,0,0.01943206787109375,0,-0.6087722778320312,0,0.3769607543945312,0,0.2565536499023438,0,0,-0.7798233032226562,0,0.3763961791992188,0,0.3760452270507812,0,0.05178070068359375,0,0,-0.5685882568359375,0.3963470458984375,0,0.1961669921875,0,-0.700714111328125,0,0.38134765625,0,0.3428573608398438,0,0,0,0,0,0,0,-0.5017242431640625,0,0.3847122192382812,0.1402053833007812,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-0.7980117797851562,0,0.4144210815429688,0,0.3733139038085938,0.40093994140625,0.3553390502929688,0,0.3205490112304688,0,0.3188705444335938,0,0.3177490234375,0,0.3192138671875,0,0.3177642822265625,0,0.2375946044921875,0,0,-3.221000671386719,0,0.4088516235351562,0,0.382843017578125,0.4106597900390625,0,0.4017105102539062,0,0.3992156982421875,0.4000167846679688,0.3973464965820312,0,0.392547607421875,0.1201248168945312,0,-2.977890014648438,0,0.3913421630859375,0.404571533203125,0,0.4014892578125,0,0.3967514038085938,0,0.39892578125,0.3991546630859375,0,0.39984130859375,0.2766265869140625,0,0,-3.105010986328125,0.364288330078125,0.384429931640625,0,0,0.4051437377929688,0.3936614990234375,0.3904953002929688,0.3869705200195312,0.388580322265625,0.3707199096679688,0,0.1101837158203125,0,-2.912933349609375,0.37982177734375,0,0.401336669921875,0.3796615600585938,0,0.3769760131835938,0,0.3788223266601562,0,0.3802337646484375,0,0.3778762817382812,0.3261032104492188,0,0,0,-2.657135009765625,0,0.3738174438476562,0,0.3838882446289062,0,0.3712921142578125,0,0.3729476928710938,0,0.37445068359375,0,0.37689208984375,0,0.3704376220703125,0,0.1200027465820312,0,-2.842742919921875,0,0,0.370819091796875,0.383697509765625,0,0.3727264404296875,0,0.3693771362304688,0,0.3713607788085938,0.373016357421875,0,0,0.3691787719726562,0.3176727294921875,0,0,0,0,0,-2.630302429199219,0,0.3812942504882812,0.3976287841796875,0,0.38323974609375,0,0.3523941040039062,0,0.38690185546875,0,0.386444091796875,0,0.3742446899414062,0,0.05194854736328125,0,0,-2.661972045898438,0,0.3855743408203125,0.3962860107421875,0.3777389526367188,0,0.3779754638671875,0,0.3718338012695312,0,0.3732452392578125,0.3721084594726562,0,0.089569091796875,0,-2.701148986816406,0,0,0.36468505859375,0.38580322265625,0.3757171630859375,0,0,0.3704452514648438,0,0.3739013671875,0,0.3753814697265625,0,0.3686981201171875,0,0.1675796508789062,0,0,-2.705863952636719,0,0.3185348510742188,0.38165283203125,0,0.3653335571289062,0,0.3765869140625,0,0.3733444213867188,0,0.3759002685546875,0,0.3772430419921875,0.2170639038085938,0,-2.721298217773438,0,0.3245849609375,0,0,0.3919906616210938,0,0.383453369140625,0,0,0.3725433349609375,0,0.3782806396484375,0,0.3802566528320312,0.382568359375,0,0.186004638671875,0,0,-2.639938354492188,0,0.3204574584960938,0,0.385162353515625,0,0.3795623779296875,0,0.375396728515625,0.3790969848632812,0,0.3853988647460938,0.3816299438476562,0,0.1105117797851562,0,0,-2.53265380859375,0.3852767944335938,0.3860702514648438,0,0,0.3811798095703125,0.3812408447265625,0,0.3878021240234375,0,0.3882217407226562,0.2987823486328125,0,0,0,0,0,-2.324607849121094,0,0.3786468505859375,0,0.3716201782226562,0,0.3679733276367188,0.3755950927734375,0.376495361328125,0.3777999877929688,0,0.1512069702148438,0,-2.494049072265625,0,0.3706207275390625,0,0.3718338012695312,0,0.368682861328125,0,0,0.3691787719726562,0.3737640380859375,0,0.3810272216796875,0.3324737548828125,0,0,0,0,0,-2.270294189453125,0.361358642578125,0,0.3630905151367188,0,0.3637924194335938,0.3693084716796875,0.3697433471679688,0,0.3682632446289062,0.1471099853515625,0,0,-2.447891235351562,0.3728866577148438,0,0.3825759887695312,0,0.3835525512695312,0.3788909912109375,0,0.3821868896484375,0,0.386199951171875,0,0.2327194213867188,0,0,0,0,0,-2.134452819824219,0,0.3593597412109375,0,0.3812103271484375,0.3798980712890625,0,0.3824691772460938,0,0.387298583984375,0,0,0.31427001953125,0,0,0,0,0,-2.130882263183594,0.3643035888671875,0,0.3864212036132812,0,0.385955810546875,0.3824920654296875,0.3798599243164062,0,0.3007354736328125,0,0,0,-2.108924865722656,0,0,0.3752288818359375,0.3899917602539062,0,0.3851852416992188,0,0.388336181640625,0,0.386199951171875,0.2517013549804688,0,0,0,0,0,0,0,0,0,0,0,0,0,-2.245765686035156,0.3622207641601562,0,0.3632659912109375,0,0.355316162109375,0,0.3728408813476562,0,0.3801040649414062,0,0,0.3804092407226562,0,0.097930908203125,0,0,-2.174797058105469,0,0,0.3661956787109375,0,0.3841781616210938,0,0.387054443359375,0,0.3800888061523438,0,0,0.3849716186523438,0.337860107421875,0,0,0,-1.995407104492188,0.368255615234375,0.372222900390625,0,0.3755416870117188,0,0.3834304809570312,0.3730621337890625,0.1875228881835938,0,0,-2.160072326660156,0,0.3399505615234375,0,0.3672027587890625,0.375946044921875,0.3812332153320312,0,0.3837203979492188,0.3754806518554688,0,0,0,-1.991065979003906,0,0.3355560302734375,0,0.3746719360351562,0.37774658203125,0,0,0.3869781494140625,0.38897705078125,0,0.1896820068359375,0,0,-2.102516174316406,0.31475830078125,0,0,0.3658676147460938,0,0.3783798217773438,0.3786392211914062,0,0.3875885009765625,0,0.3387222290039062,0,0,0,0,0,-1.831977844238281,0.3634109497070312,0,0.3778152465820312,0,0.3811416625976562,0,0.3834304809570312,0,0.3853759765625,0.00135040283203125,0,0,-1.904106140136719,0,0.3333816528320312,0,0.3769378662109375,0,0.3789138793945312,0.38421630859375,0,0.3885040283203125,0,0.10162353515625,0,0,-1.924819946289062,0,0.3388290405273438,0,0.3859481811523438,0.3780975341796875,0,0,0.3863906860351562,0,0.3907928466796875,0,0.1033477783203125,0,0,-1.902389526367188,0.3247528076171875,0,0.3725204467773438,0.38470458984375,0,0.3887939453125,0.390106201171875,0,0.0991363525390625,0,0,-1.863937377929688,0,0.3264541625976562,0,0.37060546875,0.3877716064453125,0,0.375518798828125,0,0.390411376953125,0,0.0698394775390625,0,0,-1.834823608398438,0,0.3617935180664062,0,0.39361572265625,0,0.38690185546875,0.3900909423828125,0,0.3581695556640625,0,0,0,0,0,-1.711875915527344,0,0.3437881469726562,0.3797378540039062,0.3800201416015625,0,0.3853302001953125,0,0.2778549194335938,0,0,0,-1.625785827636719,0.3592529296875,0,0.3838272094726562,0,0.3849334716796875,0.4011383056640625,0,0.1506195068359375,0,0,-1.787269592285156,0.3211135864257812,0,0.3800888061523438,0.383544921875,0,0.389251708984375,0,0.366363525390625,0,0,0,0,0,0,0,-1.620681762695312,0,0.3498001098632812,0.3890609741210938,0,0.3871688842773438,0.3895339965820312,0,0.1573715209960938,0,0,-1.732612609863281,0,0.3163909912109375,0,0.3786697387695312,0,0.382537841796875,0,0.3874359130859375,0.3189163208007812,0,0,0,-1.525703430175781,0.3549880981445312,0,0.3852310180664062,0,0.38494873046875,0,0.3900680541992188,0,0.0610809326171875,0,0,-1.580238342285156,0,0.366729736328125,0.3871002197265625,0,0.385894775390625,0,0.3925399780273438,0,0,0.0977325439453125,0,0,-1.604545593261719,0,0.3352890014648438,0.3874893188476562,0,0.3897171020507812,0,0.3860397338867188,0,0.1549453735351562,0,0,-1.642868041992188,0,0.3401031494140625,0,0.3941726684570312,0.3872528076171875,0.3926849365234375,0,0.1768417358398438,0,0,0,0,0,0,0,0,0,-1.57196044921875,0,0.32586669921875,0,0.38232421875,0,0.3762054443359375,0.38714599609375,0,0.147705078125,0,0,-1.582786560058594,0,0.3251419067382812,0,0.3908233642578125,0,0,0.3870849609375,0,0,0.402587890625,0,0.1238327026367188,0,0,-1.534858703613281,0,0.3194122314453125,0,0.38299560546875,0.3890304565429688,0,0.3964691162109375,0,0.09282684326171875,0,-1.474945068359375,0,0.34234619140625,0,0.40081787109375,0.3812408447265625,0.3862228393554688,0,0.0095062255859375,0,0,0,-1.396278381347656,0,0.337615966796875,0.385711669921875,0,0.3778152465820312,0,0,0.33953857421875,0,0,0,0,0,-1.319992065429688,0,0.3568572998046875,0.3950653076171875,0.3930130004882812,0,0.2187728881835938,0,-1.495452880859375,0,0.3212509155273438,0,0.394989013671875,0,0.396820068359375,0.40008544921875,0.0252685546875,0,-1.309089660644531,0,0.3580856323242188,0,0.4011611938476562,0,0,0.3998870849609375,0,0.1923370361328125,0,0,-1.435272216796875,0.3704299926757812,0,0.4025650024414062,0,0.3874282836914062,0,0.3164291381835938,0,0,0,0,0,-1.2113037109375,0,0.3635711669921875,0,0.3902740478515625,0,0.3873291015625,0.1110763549804688,0,-1.337509155273438,0,0.3170394897460938,0,0,0.3881988525390625,0,0.3855133056640625,0,0.2870407104492188,0,0,0,0,0,0,0,-1.142349243164062,0.3695144653320312,0,0.3883209228515625,0,0,0.3835678100585938,0,0.040557861328125,0,0,0,-1.224372863769531,0,0.3429183959960938,0,0.3902206420898438,0,0.387451171875,0.1427536010742188,0,-1.281181335449219,0,0.3397064208984375,0.4046859741210938,0,0.4007492065429688,0.1744384765625,0,0,-1.27593994140625,0,0.3276138305664062,0,0.4022598266601562,0,0.4000167846679688,0,0.183746337890625,0,0,0,0,0,-1.234642028808594,0,0.319305419921875,0,0.3902816772460938,0,0,0.39251708984375,0,0.1697006225585938,0,0,-1.24066162109375,0.3054580688476562,0,0.3446807861328125,0,0.3875274658203125,0.2395248413085938,0,0,0,-0.992523193359375,0.3843994140625,0.3886795043945312,0.2553634643554688,0,0,0,0,0,0,0,0,0,0,0,-1.237541198730469,0,0,0.3335723876953125,0,0,0.3951568603515625,0,0,0.3686752319335938,0,0.1753692626953125,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.217498779296875,0,0.09930419921875,0.3961868286132812,0,0,0.4144668579101562,0,0,0.3627090454101562,0,0,0.4008255004882812,0.3993148803710938,0,0.3414764404296875,0,0.3244705200195312,0,0.3223342895507812,0,0.32464599609375,0,0.3229293823242188,0,0.3228683471679688,0,0.3220672607421875,0.3239288330078125,0.3227996826171875,0,0.297821044921875,0,0,0,-4.899742126464844,0,0.423583984375,0,0.3772735595703125,0,0.385711669921875,0,0.3996047973632812,0,0.401824951171875,0,0.40179443359375,0.4022140502929688,0,0,0.402191162109375,0,0,0.4013671875,0.4009246826171875,0,0.4006195068359375,0,0.3923187255859375,0,0.2552108764648438,0,0,0,-4.760787963867188,0,0.392730712890625,0,0.36077880859375,0,0.405548095703125,0,0.3968887329101562,0,0.3993988037109375,0,0.3955535888671875,0,0.3899307250976562,0.3895034790039062,0,0.3893890380859375,0,0.3888320922851562,0,0.3894271850585938,0,0.3816146850585938,0.2237548828125,0,0,0,0,0,-4.664909362792969,0,0.4008941650390625,0,0.362884521484375,0,0.3959426879882812,0.3870468139648438,0,0.3876266479492188,0,0.3865814208984375,0,0,0.3816757202148438,0,0.3892974853515625,0.3880386352539062,0,0.389892578125,0.3897476196289062,0,0.3772811889648438,0,0.16827392578125,0,0,0,0,0,0,0,0,-4.826461791992188,0,0,0.280609130859375,0,0,0.3749542236328125,0.3546829223632812,0,0.384246826171875,0,0.3808059692382812,0,0,0.3764190673828125,0,0.3764190673828125,0.3777313232421875,0,0.3767852783203125,0,0,0.3774261474609375,0,0.3737640380859375,0,0.380279541015625,0,0.3921737670898438,0,0.15814208984375,0,0,0,0,0,-4.480262756347656,0,0.3546676635742188,0,0.3654861450195312,0.3758926391601562,0,0.3916397094726562,0,0.383453369140625,0,0.3739013671875,0,0.3734130859375,0,0.3710250854492188,0.3759841918945312,0,0.3750228881835938,0,0.3770675659179688,0,0.377105712890625,0,0.121429443359375,0,0,0,0,0,-4.359352111816406,0,0.3521804809570312,0,0.3846359252929688,0,0.379730224609375,0,0.3744659423828125,0,0.3700942993164062,0,0.372039794921875,0,0.3731918334960938,0,0.3688507080078125,0,0.3770828247070312,0,0.3777999877929688,0,0.3741912841796875,0.3738784790039062,0,0.01474761962890625,0,0,0,-4.581611633300781,0.3484573364257812,0,0.363555908203125,0,0.3849868774414062,0.3771514892578125,0,0.3798065185546875,0.375762939453125,0,0.380126953125,0,0.3761672973632812,0,0.3709564208984375,0,0.3720626831054688,0.3775787353515625,0,0.373931884765625,0,0.232513427734375,0,0,0,0,0,-4.337432861328125,0,0.3537445068359375,0,0.3811492919921875,0,0.3711700439453125,0,0.3716201782226562,0,0.372589111328125,0,0.3766937255859375,0,0.373046875,0,0.378570556640625,0.3780975341796875,0,0.3770828247070312,0,0.37939453125,0,0.3535842895507812,0,0,0,0,0,-4.425514221191406,0,0.3321990966796875,0,0.3621826171875,0,0.3697586059570312,0,0.370574951171875,0,0.3714828491210938,0,0.3707275390625,0.372589111328125,0,0,0.37591552734375,0.3764495849609375,0.3806610107421875,0,0.3780364990234375,0,0.3701934814453125,0,0.1219711303710938,0,0,0,0,0,-4.124160766601562,0.3241043090820312,0.3859405517578125,0.3763580322265625,0,0.2958602905273438,0,0.3770599365234375,0,0.3925399780273438,0.37481689453125,0.3764190673828125,0,0.378021240234375,0.3802108764648438,0,0.3721771240234375,0,0.2158279418945312,0,0,0,0,0,-4.131340026855469,0,0.3577346801757812,0,0.3732376098632812,0.361541748046875,0,0.36407470703125,0,0.3705978393554688,0,0.3772811889648438,0,0.3783035278320312,0.3775100708007812,0,0.3749923706054688,0,0.3763351440429688,0.3697891235351562,0,0.1730804443359375,0,0,0,-4.055313110351562,0,0.31689453125,0.354461669921875,0.3648300170898438,0,0.3767547607421875,0,0.369354248046875,0.365936279296875,0,0.3733596801757812,0,0.3732376098632812,0,0.3785629272460938,0.38214111328125,0,0,0.3716506958007812,0,0,0.149322509765625,0,0,0,0,0,-3.980819702148438,0,0,0.3368911743164062,0,0.3665695190429688,0,0.3559417724609375,0.3582611083984375,0,0.3636398315429688,0.3755722045898438,0.384185791015625,0,0.3787002563476562,0,0.3762741088867188,0.38018798828125,0,0,0.3628768920898438,0,0.060943603515625,0,0,0,-3.799079895019531,0,0.3770828247070312,0.3711318969726562,0,0.36627197265625,0,0.3761672973632812,0,0.379608154296875,0,0.3821868896484375,0,0.39605712890625,0,0.3977584838867188,0,0.3868637084960938,0.3771438598632812,0,0.1061172485351562,0,0,0,-3.794830322265625,0.357879638671875,0.3660430908203125,0.3577957153320312,0.37103271484375,0.3762130737304688,0,0.3823318481445312,0,0,0.3844985961914062,0.3875579833984375,0.38916015625,0.3784332275390625,0,0.1592864990234375,0,0,0,0,0,-3.756065368652344,0,0.3530120849609375,0,0.3660430908203125,0,0.3590774536132812,0.3746109008789062,0,0,0.3802566528320312,0,0.3837890625,0,0.3870391845703125,0,0.389556884765625,0.3914871215820312,0.3797531127929688,0,0,0.104949951171875,0,0,0,0,0,-3.650016784667969,0.3581466674804688,0.3589019775390625,0.3608627319335938,0,0.3746109008789062,0.3826065063476562,0.3855133056640625,0,0.3854598999023438,0.3890304565429688,0,0.3913192749023438,0,0.3742828369140625,0.0010528564453125,0,0,-3.818862915039062,0,0.3173294067382812,0.3635177612304688,0,0.355865478515625,0,0.3679885864257812,0,0.3813629150390625,0,0.3870697021484375,0,0.3888320922851562,0,0.391998291015625,0,0.3940353393554688,0.3896636962890625,0,0.191070556640625,0,0,0,0,0,-3.601310729980469,0,0.337249755859375,0.3650588989257812,0,0.3683242797851562,0.3807754516601562,0,0.37933349609375,0,0.3825225830078125,0,0.38604736328125,0,0.3871612548828125,0,0.3909149169921875,0,0.3320159912109375,0,0,0,0,0,-3.678726196289062,0,0.362548828125,0,0.3583297729492188,0,0.3494186401367188,0.3645706176757812,0,0.3776397705078125,0,0.3811569213867188,0,0,0.3835525512695312,0.3863983154296875,0,0.3892059326171875,0,0.3755416870117188,0,0.05683135986328125,0,0,0,-3.377174377441406,0.3624649047851562,0,0.3599319458007812,0,0.3633956909179688,0,0.3717117309570312,0.3737335205078125,0,0.37811279296875,0.3832550048828125,0,0.3888702392578125,0,0.3805999755859375,0,0,0.1196823120117188,0,0,0,0,0,-3.397064208984375,0,0.3334197998046875,0,0.3474502563476562,0,0.3565826416015625,0,0.3860244750976562,0,0.3797836303710938,0,0.3830108642578125,0,0.3874969482421875,0,0.3891677856445312,0,0.3845138549804688,0.152618408203125,0,0,0,0,0,0,0,-3.372039794921875,0.3212738037109375,0,0.3467559814453125,0,0.3544235229492188,0,0.3708267211914062,0.3777313232421875,0,0.3816604614257812,0,0.3836593627929688,0.3891372680664062,0,0.381134033203125,0,0.1667251586914062,0,0,0,0,0,-3.276557922363281,0.3491287231445312,0,0.3506698608398438,0.3635177612304688,0,0.3737869262695312,0,0.3770294189453125,0.381195068359375,0,0.38427734375,0.3823623657226562,0.3733291625976562,0.040924072265625,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-3.119537353515625,0.3220062255859375,0.3589096069335938,0,0.3756790161132812,0,0.388153076171875,0,0.3929061889648438,0,0.397918701171875,0.3984146118164062,0,0,0.3918380737304688,0,0,0.19146728515625,0,0,0,0,0,-3.205718994140625,0,0.3181610107421875,0.347015380859375,0,0.3664703369140625,0.3798446655273438,0,0.3874359130859375,0,0.3922042846679688,0,0.3935928344726562,0,0.3983154296875,0.3192367553710938,0,0,0,0,0,-3.279541015625,0,0.3148574829101562,0,0.3519363403320312,0,0.3658370971679688,0.380462646484375,0,0.3888778686523438,0,0.3923797607421875,0,0.3951568603515625,0,0.394622802734375,0.379974365234375,0.0103759765625,0,0,0,-2.9964599609375,0,0,0.3522720336914062,0.3582000732421875,0,0.3657608032226562,0.3702239990234375,0,0.3410415649414062,0.2487716674804688,0.3330001831054688,0,0,0.3802566528320312,0,0.3404006958007812,0,0,0,0,0,0,0,0,-2.927513122558594,0,0,0.3312911987304688,0,0.346954345703125,0.3537063598632812,0,0.3658523559570312,0.3688812255859375,0,0.3721923828125,0,0.3729400634765625,0.3668975830078125,0.1406784057617188,0,0,0,0,0,-2.966163635253906,0,0.3425674438476562,0,0.3530197143554688,0,0.36358642578125,0.3738327026367188,0.3774566650390625,0.3790283203125,0.3849411010742188,0,0.378021240234375,0.1041793823242188,0,0,0,0,0,-2.868072509765625,0,0.3397750854492188,0.3531723022460938,0,0.3623428344726562,0.36785888671875,0,0.3748245239257812,0.3767166137695312,0,0.3795394897460938,0,0,0.3683624267578125,0,0.03440093994140625,0,0,0,-2.8203125,0.3101730346679688,0.3490753173828125,0,0.3676300048828125,0,0.3791427612304688,0,0.3813095092773438,0.3846435546875,0,0.387115478515625,0,0.348846435546875,0,0,0,0,0,0,0,0,-2.729209899902344,0.3153533935546875,0,0.3582992553710938,0.37200927734375,0,0.3805007934570312,0.3858795166015625,0.38568115234375,0,0.3881149291992188,0,0.229400634765625,0,0,0,-2.887123107910156,0,0.3190765380859375,0.3598709106445312,0,0.3644332885742188,0,0.376068115234375,0,0.3763580322265625,0,0.38348388671875,0.3819656372070312,0,0.3657379150390625,0.04491424560546875,0,0,0,0,0,-2.686752319335938,0,0.350616455078125,0.3657989501953125,0.3692703247070312,0.3688430786132812,0,0.3779373168945312,0,0.3755645751953125,0.341064453125,0,0.1817855834960938,0.03920745849609375,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2.838714599609375,0,0.1229629516601562,0,0.2188262939453125,0,0.306060791015625,0,0,0.3031997680664062,0,0.3061370849609375,0.3145065307617188,0.3166275024414062,0.3198623657226562,0,0.3207321166992188,0,0.3184890747070312,0,0.0733642578125,0,0,0,0,0,-2.692192077636719,0,0.294097900390625,0,0.2197189331054688,0,0.2794036865234375,0.3246307373046875,0.3242874145507812,0.3314666748046875,0,0.3354568481445312,0,0.3416595458984375,0,0,0.3209915161132812,0.0011749267578125,0,0,0,0,0,-2.573585510253906,0,7.768608093261719,0,0,0,0,0,0,0,0,0,0,0,0,0,7.62939453125,7.62939453125e-06,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,15.2587890625,0,0,0,0,0,0,0,0,0,0,0],"filename":[null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null]},"interval":10,"files":[],"prof_output":"/tmp/RtmpPGYc6H/file1c133aac4262.prof","highlight":{"output":["^output\\$"],"gc":["^<GC>$"],"stacktrace":["^\\.\\.stacktraceo(n|ff)\\.\\.$"]},"split":"h"}},"evals":[],"jsHooks":[]}</script>
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
##  mean1(x, 0.5) 21.22159 24.05092 27.19083 26.93219 29.28603 38.83637    20   a
##  mean2(x, 0.5) 22.64585 23.40534 25.91066 24.89418 27.29905 35.28588    20   a
##  mean3(x, 0.5) 21.49653 24.04798 26.32646 25.70899 29.43275 31.42388    20   a
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
## 1 mean1(x, 0.5)   20.8ms   22.7ms      44.7    7.63MB     0   
## 2 mean2(x, 0.5)   19.4ms     22ms      47.2    7.63MB     2.49
## 3 mean3(x, 0.5)   20.8ms   23.1ms      44.2    7.63MB     2.33
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
##   0.153   0.000   0.154
```

``` r
system.time( ma2(x) )
```

```
##    user  system elapsed 
##   0.018   0.011   0.029
```

``` r
ma3 <- compiler::cmpfun(ma2)
system.time( ma3(x) )
```

```
##    user  system elapsed 
##    0.02    0.00    0.02
```
Likewise, matrix operations are often faster than vector operations.


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
##   0.550   0.010   0.179
```

``` r
system.time({ .lm.fit(X, Y) })
```

```
##    user  system elapsed 
##   0.104   0.000   0.030
```

``` r
system.time({ solve(t(X)%*%X) %*% (t(X)%*%Y) })
```

```
##    user  system elapsed 
##   0.017   0.000   0.015
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
##   0.020   0.001   0.021
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
##   1.186   0.204   0.878
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
## R version 4.4.3 (2025-02-28)
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
##  [4] parallel_4.4.3       jquerylib_0.1.4      splines_4.4.3       
##  [7] yaml_2.3.10          fastmap_1.2.0        lattice_0.22-7      
## [10] TH.data_1.1-3        R6_2.6.1             microbenchmark_1.5.0
## [13] knitr_1.50           htmlwidgets_1.6.4    MASS_7.3-65         
## [16] tibble_3.2.1         bookdown_0.43        profvis_0.4.0       
## [19] bslib_0.9.0          pillar_1.10.2        rlang_1.1.6         
## [22] utf8_1.2.4           multcomp_1.4-28      cachem_1.1.0        
## [25] xfun_0.52            sass_0.4.10          cli_3.6.4           
## [28] magrittr_2.0.3       digest_0.6.37        grid_4.4.3          
## [31] mvtnorm_1.3-3        sandwich_3.1-1       lifecycle_1.0.4     
## [34] vctrs_0.6.5          bench_1.1.4          evaluate_1.0.3      
## [37] glue_1.8.0           codetools_0.2-20     zoo_1.8-14          
## [40] survival_3.8-3       profmem_0.6.0        rmarkdown_2.29      
## [43] tools_4.4.3          pkgconfig_2.0.3      htmltools_0.5.8.1
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



