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


```{=html}
<div class="profvis html-widget html-fill-item" id="htmlwidget-52947c7d25605dce292e" style="width:100%;height:600px;"></div>
<script type="application/json" data-for="htmlwidget-52947c7d25605dce292e">{"x":{"message":{"prof":{"time":[1,2,3,4,5,6,7,8,9,9,9,10,10,11,11,12,12,13,13,14,14,15,15,16,16,17,17,18,18,19,19,20,20,20,21,21,22,23,24,24,25,25,25,26,27,28,29,29,30,31,32,32,32,33,33,34,35,35,36,37,37,38,38,38,39,39,40,40,41,41,42,43,43,44,44,44,45,45,46,46,47,47,47,48,48,49,50,50,51,51,51,52,52,53,53,54,54,55,56,56,56,57,57,58,58,59,60,61,62,62,63,63,63,64,64,65,66,66,67,67,68,68,69,69,70,71,71,72,72,73,73,74,74,75,75,75,76,76,77,77,78,78,79,79,80,80,81,81,82,82,83,84,85,85,86,86,87,87,87,88,88,88,89,90,90,91,92,92,93,93,94,94,94,95,95,96,96,97,97,97,98,98,99,99,100,100,100,101,101,102,102,103,103,104,105,105,106,106,107,107,108,109,109,109,110,111,111,111,112,112,113,113,114,114,115,115,115,116,116,117,117,117,118,118,119,119,120,120,121,122,122,122,123,123,123,124,124,124,125,125,126,126,126,127,127,128,128,128,129,130,130,131,131,132,133,133,133,134,134,135,136,136,137,137,138,138,139,139,140,141,142,143,143,144,144,144,145,145,146,146,147,147,148,149,149,150,151,151,152,153,153,154,154,154,155,155,155,156,156,157,158,159,159,160,160,160,161,161,162,162,163,163,164,164,165,165,165,166,166,167,167,168,169,169,170,170,170,171,171,172,172,173,173,174,175,175,175,176,177,177,178,179,179,180,180,180,181,181,182,182,183,184,184,185,185,185,186,186,187,187,188,189,190,190,191,192,193,193,193,194,195,195,195,196,196,196,197,197,197,198,199,199,200,200,201,201,201,202,203,203,204,204,205,206,206,206,207,208,209,209,210,210,211,211,212,213,214,214,215,215,215,216,217,218,218,218,219,219,219,220,220,221,221,222,222,223,223,224,224,225,225,226,226,226,227,227,227,228,228,229,230,230,230,231,231,232,232,233,233,234,234,235,235,236,236,237,237,238,238,238,239,239,239,240,240,241,241,242,242,243,243,244,245,245,245,246,246,247,247,248,249,249,250,250,251,251,252,252,253,253,254,254,255,255,256,256,256,257,258,259,259,259,260,260,261,261,262,262,263,263,263,264,265,266,267,267,267,268,268,269,270,270,270,271,271,272,272,273,273,274,274,275,275,276,276,277,277,277,278,278,278,279,279,279,280,280,280,281,281,281,282,282,282,283,283,283,284,284,284,285,285,285,286,286,286,287,287,287,288,288,289,289,290,290,291,291,292,292,293,294,294,295,295,296,296,297,298,298,298,298,299,299,300,300,301,302,302,303,304,305,305,306,306,307,308,308,308,309,309,310,311,311,312,312,313,314,314,315,316,317,317,318,318,318,319,319,320,320,321,321,322,322,322,323,323,324,324,325,325,326,326,327,327,328,328,328,329,330,330,331,332,332,332,333,334,334,335,336,336,337,337,337,338,339,339,340,340,341,341,342,342,343,344,345,345,346,347,347,347,348,348,349,349,350,350,351,351,352,352,353,353,353,354,354,355,356,356,357,358,359,359,359,360,360,361,361,362,362,363,363,364,365,365,366,366,366,367,367,368,368,368,369,370,370,371,372,372,373,374,374,375,375,375,376,377,377,378,378,378,379,379,380,381,381,382,382,383,383,384,384,384,385,385,386,386,387,388,388,389,390,390,391,391,392,392,393,393,393,394,394,395,395,396,397,398,398,399,399,400,400,401,402,402,402,403,403,404,405,405,406,406,407,407,408,409,410,410,410,411,411,411,412,413,414,414,414,415,415,416,417,417,418,418,419,419,419,420,420,421,422,423,424,424,425,425,426,426,426,427,427,428,428,428,429,429,430,430,431,431,432,432,433,433,434,434,435,435,436,436,437,437,438,438,439,440,441,442,442,443,443,444,444,445,445,446,447,447,448,448,449,449,450,451,452,452,453,453,453,454,455,456,457,457,458,458,458,459,459,460,460,461,461,462,462,463,464,465,465,466,466,467,467,467,468,468,469,469,469,470,470,471,472,472,473,474,474,474,475,475,476,476,477,477,477,478,478,478,479,479,479,480,480,480,481,481,481,482,482,482,483,483,483,484,484,485,486,486,487,487,488,489,489,490,490,491,491,491,491,492,492,493,493,494,495,495,495,496,497,498,498,498,499,499,499,500,500,501,501,502,502,503,503,503,504,505,505,506,506,506,507,508,508,509,509,510,511,512,513,513,513,514,514,514,515,515,516,516,517,517,518,518,519,520,521,521,522,522,523,524,524,525,525,526,526,527,527,528,528,529,529,530,530,531,531,532,533,533,534,534,535,535,536,536,537,538,538,539,539,540,540,541,541,542,542,543,543,543,544,544,545,545,546,546,547,547,548,548,549,549,550,550,550,551,551,552,552,552,553,553,554,554,555,555,556,556,556,557,557,558,558,559,560,561,562,562,563,563,564,564,564,565,566,566,567,567,568,568,569,569,569,570,570,571,571,572,572,573,573,574,574,575,575,576,576,577,578,578,578,579,580,580,581,581,582,582,583,583,584,584,584,585,585,585,586,587,587,588,588,588,589,589,590,591,591,592,593,594,595,596,597,597,597,598,598,598,599,600,600,601,601,602,603,603,604,604,604,605,605,606,606,606,607,608,608,609,609,609,610,610,610,611,611,611,612,613,614,614,615,615,616,616,617,617,618,619,619,620,621,621,622,622,623,623,624,624,625,625,626,626,627,627,628,629,629,630,630,631,631,632,632,633,633,634,635,635,635,636,636,637,638,639,639,639,640,641,642,642,643,643,643,644,644,645,645,645,646,647,647,647,648,648,649,649,650,650,651,651,651,652,652,653,653,654,655,655,656,656,656,657,657,657,658,658,659,659,660,660,661,661,662,662,663,663,664,665,665,666,666,667,668,668,668,668,669,669,670,670,671,671,672,672,673,674,674,674,674,675,676,676,677,678,678,679,679,680,680,681,681,682,682,683,683,684,684,685,685,685,686,687,688,689,689,690,690,690,691,692,693,694,694,695,695,696,696,697,698,698,699,699,700,701,701,701,702,702,703,703,704,705,705,706,706,706,707,707,708,709,709,710,710,711,711,712,712,713,714,714,715,715,715,716,716,716,717,717,717,718,718,719,719,720,720,721,721,722,722,722,723,723,724,724,725,725,726,727,727,728,728,729,729,730,731,732,732,732,733,733,733,734,734,734,735,736,737,737,738,738,738,739,739,740,740,741,741,742,742,743,743,744,744,745,745,746,746,747,747,748,748,749,749,750,750,751,751,752,752,753,753,754,754,755,755,756,756,757,757,758,758,759,759,760,760,761,761,761,762,763,763,764,765,765,766,766,767,768,768,769,769,770,770,770,771,771,772,772,773,774,774,775,775,776,777,778,778,778,779,779,779,780,781,781,782,782,783,783,784,785,786,786,787,787,788,788,789,790,790,791,791,792,793,794,794,794,795,796,797,797,797,798,799,800,800,801,801,802,802,803,803,804,804,805,806,807,807,808,809,809,809,810,810,810,811,811,812,812,813,814,814,815,815,816,817,817,818,818,819,819,820,821,822,822,823,823,824,825,825,825,826,826,826,827,827,827,828,828,828,829,829,830,830,831,831,832,833,833,834,835,835,836,836,837,837,838,838,839,839,840,840,841,841,842,843,843,843,844,844,845,845,846,847,847,848,849,849,850,850,851,851,852,852,853,853,854,854,855,855,856,856,857,858,858,858,859,859,860,860,861,861,862,862,863,863,864,864,864,865,866,867,867,868,868,868,869,869,870,870,871,871,872,872,872,873,873,873,874,875,876,876,877,877,878,878,879,879,880,880,881,881,882,883,884,885,885,886,886,887,887,887,888,888,888,889,889,889,890,890,890,891,891,892,892,893,893,894,894,894,895,896,897,897,898,898,899,900,900,901,901,902,902,902,903,903,903,904,905,906,907,907,907,908,908,909,909,910,910,911,912,913,913,913,914,914,915,916,916,917,917,918,918,919,920,921,922,922,923,924,924,924,925,925,926,926,927,927,928,928,929,929,930,930,931,931,932,932,933,933,934,934,935,935,936,936,937,937,938,938,939,939,940,940,941,941,942,942,943,943,944,944,945,945,946,947,948,948,949,949,949,950,950,951,952,952,953,954,955,956,956,957,958,958,958,958,959,959,959,959,960,960,960,961,961,962,962,963,963,964,965,966,966,967,968,968,968,969,970,970,970,971,971,972,972,972,973,973,974,974,975,975,976,976,976,977,978,978,979,979,979,980,980,981,981,982,982,983,983,984,985,985,986,986,987,987,988,988,989,989,990,991,991,992,992,993,994,994,995,996,996,997,998,998,998,999,999,999,1000,1000,1001,1001,1002,1002,1003,1003,1004,1004,1005,1005,1006,1006,1007,1007,1008,1008,1009,1009,1010,1010,1011,1011,1012,1012,1013,1013,1014,1014,1015,1015,1016,1016,1017,1017,1018,1018,1019,1020,1020,1021,1022,1022,1022,1023,1023,1024,1024,1024,1025,1025,1025,1026,1026,1027,1028,1028,1029,1029,1030,1031,1031,1032,1033,1033,1033,1034,1034,1035,1036,1036,1037,1037,1037,1038,1038,1038,1039,1039,1040,1041,1042,1042,1043,1044,1044,1045,1045,1046,1046,1047,1048,1048,1049,1049,1049,1050,1050,1050,1051,1051,1051,1052,1053,1053,1054,1055,1055,1055,1056,1056,1057,1057,1058,1058,1059,1060,1060,1060,1061,1061,1062,1062,1063,1063,1064,1064,1065,1065,1066,1066,1067,1067,1068,1068,1069,1070,1070,1071,1071,1072,1072,1072,1073,1074,1074,1074,1075,1075,1076,1076,1076,1077,1077,1077,1078,1079,1079,1080,1080,1080,1081,1081,1082,1083,1083,1084,1084,1085,1085,1086,1087,1087,1088,1088,1088,1089,1089,1089,1090,1090,1091,1091,1092,1092,1093,1093,1094,1094,1095,1095,1096,1097,1097,1098,1098,1099,1099,1100,1100,1100,1101,1101,1101,1102,1102,1102,1103,1103,1104,1104,1105,1106,1106,1107,1108,1109,1110,1111,1111,1112,1112,1113,1113,1114,1114,1115,1115,1116,1116,1117,1117,1118,1118,1119,1119,1120,1120,1121,1121,1122,1123,1124,1124,1125,1126,1126,1127,1128,1129,1129,1129,1130,1130,1131,1131,1131,1132,1132,1132,1133,1133,1133,1134,1134,1135,1135,1136,1136,1136,1137,1137,1138,1138,1139,1139,1139,1140,1140,1141,1141,1141,1142,1143,1144,1144,1144,1145,1145,1145,1146,1146,1147,1148,1148,1149,1149,1150,1150,1150,1151,1152,1152,1152,1153,1153,1153,1154,1154,1155,1156,1156,1157,1157,1158,1158,1159,1160,1160,1161,1161,1162,1162,1162,1163,1163,1164,1165,1165,1166,1167,1167,1167,1168,1168,1168,1169,1169,1169,1170,1171,1171,1171,1172,1172,1172,1173,1173,1174,1175,1175,1176,1177,1177,1178,1178,1178,1179,1179,1179,1180,1180,1181,1181,1182,1182,1183,1183,1184,1184,1185,1185,1186,1186,1187,1188,1188,1188,1189,1189,1189,1190,1190,1190,1191,1191,1192,1193,1193,1194,1194,1195,1196,1197,1197,1198,1198,1199,1200,1200,1201,1201,1202,1202,1202,1203,1203,1204,1204,1205,1205,1206,1206,1207,1207,1208,1209,1210,1210,1211,1211,1212,1212,1213,1214,1215,1215,1216,1216,1216,1217,1218,1218,1218,1219,1219,1219,1220,1221,1221,1221,1222,1222,1222,1223,1223,1224,1225,1225,1226,1226,1227,1227,1227,1228,1228,1229,1229,1230,1231,1231,1232,1232,1233,1233,1234,1234,1235,1235,1235,1236,1237,1237,1237,1238,1238,1239,1239,1240,1240,1240,1241,1241,1242,1242,1242,1243,1243,1243,1244,1244,1245,1246,1247,1248,1248,1249,1249,1250,1250,1251,1251,1252,1252,1253,1253,1254,1254,1255,1255,1256,1256,1257,1257,1258,1258,1259,1259,1260,1260,1261,1261,1262,1262,1263,1263,1264,1264,1265,1265,1266,1266,1267,1267,1336,1336],"depth":[1,1,1,1,1,1,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,1,2,1,3,2,1,1,1,1,2,1,1,1,3,2,1,2,1,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,3,2,1,2,1,2,1,3,2,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,1,1,1,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,3,2,1,3,2,1,1,2,1,1,2,1,2,1,3,2,1,2,1,2,1,3,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,3,2,1,1,3,2,1,2,1,2,1,2,1,3,2,1,2,1,3,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,3,2,1,2,1,3,2,1,2,1,3,2,1,1,2,1,2,1,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,1,1,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,1,2,1,1,2,1,3,2,1,3,2,1,2,1,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,1,3,2,1,1,2,1,1,2,1,3,2,1,2,1,2,1,1,2,1,3,2,1,2,1,2,1,1,1,2,1,1,1,3,2,1,1,3,2,1,3,2,1,3,2,1,1,2,1,2,1,3,2,1,1,2,1,2,1,1,3,2,1,1,1,2,1,2,1,2,1,1,1,2,1,3,2,1,1,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,1,3,2,1,2,1,2,1,2,1,3,2,1,1,1,1,3,2,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,4,3,2,1,2,1,2,1,1,2,1,1,1,2,1,2,1,1,3,2,1,2,1,1,2,1,2,1,1,2,1,1,1,2,1,3,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,1,3,2,1,1,2,1,1,2,1,3,2,1,1,2,1,2,1,2,1,2,1,1,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,1,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,2,1,3,2,1,1,2,1,1,2,1,1,2,1,3,2,1,1,2,1,3,2,1,2,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,1,2,1,2,1,2,1,1,3,2,1,2,1,1,2,1,2,1,2,1,1,1,3,2,1,3,2,1,1,1,3,2,1,2,1,1,2,1,2,1,3,2,1,2,1,1,1,1,2,1,2,1,3,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,1,2,1,3,2,1,1,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,3,2,1,2,1,3,2,1,2,1,1,2,1,1,3,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,1,2,1,2,1,4,3,2,1,2,1,2,1,1,3,2,1,1,1,3,2,1,3,2,1,2,1,2,1,2,1,3,2,1,1,2,1,3,2,1,1,2,1,2,1,1,1,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,3,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,1,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,1,2,1,3,2,1,2,1,1,2,1,1,1,1,1,1,3,2,1,3,2,1,1,2,1,2,1,1,2,1,3,2,1,2,1,3,2,1,1,2,1,3,2,1,3,2,1,3,2,1,1,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,1,1,3,2,1,1,1,2,1,3,2,1,2,1,3,2,1,1,3,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,4,3,2,1,2,1,2,1,2,1,2,1,1,4,3,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,1,1,2,1,3,2,1,1,1,1,2,1,2,1,2,1,1,2,1,2,1,1,3,2,1,2,1,2,1,1,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,1,3,2,1,3,2,1,3,2,1,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,1,1,3,2,1,3,2,1,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,1,2,1,2,1,1,1,3,2,1,1,1,3,2,1,1,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,1,3,2,1,3,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,1,1,2,1,2,1,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,1,2,1,3,2,1,2,1,2,1,2,1,3,2,1,3,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,3,2,1,1,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,1,1,1,3,2,1,2,1,2,1,2,1,1,1,3,2,1,2,1,1,2,1,2,1,2,1,1,1,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,3,2,1,2,1,1,2,1,1,1,1,2,1,1,4,3,2,1,4,3,2,1,3,2,1,2,1,2,1,2,1,1,1,2,1,1,3,2,1,1,3,2,1,2,1,3,2,1,2,1,2,1,2,1,3,2,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,1,2,1,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,3,2,1,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,1,2,1,1,3,2,1,2,1,1,2,1,3,2,1,3,2,1,2,1,1,1,2,1,1,2,1,2,1,2,1,1,2,1,3,2,1,3,2,1,3,2,1,1,2,1,1,3,2,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,1,3,2,1,2,1,3,2,1,3,2,1,1,2,1,3,2,1,2,1,1,2,1,2,1,2,1,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,1,2,1,1,1,3,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,3,2,1,2,1,2,1,3,2,1,2,1,3,2,1,1,1,3,2,1,3,2,1,2,1,1,2,1,2,1,3,2,1,1,3,2,1,3,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,1,2,1,1,3,2,1,3,2,1,3,2,1,1,3,2,1,3,2,1,2,1,1,2,1,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,1,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,1,1,2,1,3,2,1,1,3,2,1,3,2,1,1,3,2,1,3,2,1,2,1,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,1,3,2,1,2,1,2,1,3,2,1,2,1,3,2,1,3,2,1,2,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1],"label":["rowSums","rowSums","rowSums","rowSums","rowMeans","rowMeans","rowMeans","rowMeans","<GC>","aperm.default","apply","aperm.default","apply","aperm.default","apply","aperm.default","apply","aperm.default","apply","aperm.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","FUN","apply","<GC>","FUN","apply","apply","apply","apply","FUN","apply","apply","apply","<GC>","mean.default","apply","FUN","apply","apply","mean.default","apply","apply","mean.default","apply","<GC>","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","apply","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","mean.default","apply","<GC>","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","<GC>","apply","mean.default","apply","apply","apply","apply","FUN","apply","<GC>","mean.default","apply","mean.default","apply","apply","is.na","local","FUN","apply","mean.default","apply","<GC>","apply","apply","mean.default","apply","mean.default","apply","length","local","FUN","apply","<GC>","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","is.numeric","local","FUN","apply","<GC>","apply","<GC>","apply","apply","apply","length","local","mean.default","apply","isTRUE","mean.default","apply","<GC>","mean.default","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","<GC>","is.numeric","local","mean.default","apply","FUN","apply","FUN","apply","apply","<GC>","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","<GC>","FUN","apply","FUN","apply","mean.default","apply","length","local","isTRUE","mean.default","apply","length","local","<GC>","FUN","apply","is.na","local","FUN","apply","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","length","local","isTRUE","mean.default","apply","FUN","apply","<GC>","length","local","apply","mean.default","apply","mean.default","apply","apply","<GC>","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","apply","apply","apply","apply","length","local","<GC>","mean.default","apply","FUN","apply","is.numeric","local","mean.default","apply","apply","<GC>","apply","apply","mean.default","apply","apply","FUN","apply","<GC>","length","local","<GC>","length","local","FUN","apply","apply","apply","FUN","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","<GC>","FUN","apply","mean.default","apply","FUN","apply","apply","FUN","apply","<GC>","FUN","apply","length","local","mean.default","apply","mean.default","apply","apply","<GC>","FUN","apply","apply","is.na","local","apply","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","apply","apply","<GC>","apply","apply","apply","isTRUE","mean.default","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","mean.default","apply","<GC>","mean.default","apply","apply","FUN","apply","mean.default","apply","apply","<GC>","FUN","apply","apply","apply","FUN","apply","<GC>","apply","<GC>","apply","apply","apply","FUN","apply","<GC>","FUN","apply","apply","apply","isTRUE","mean.default","apply","<GC>","length","local","FUN","apply","mean.default","apply","FUN","apply","<GC>","apply","mean.default","apply","mean.default","apply","<GC>","length","local","<GC>","length","local","mean.default","apply","apply","<GC>","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","<GC>","apply","FUN","apply","mean.default","apply","FUN","apply","<GC>","is.na","local","isTRUE","mean.default","apply","FUN","apply","FUN","apply","<GC>","apply","mean.default","apply","apply","<GC>","length","local","mean.default","apply","FUN","apply","apply","<GC>","apply","FUN","apply","mean.default","apply","mean.default","apply","<GC>","apply","mean.default","apply","FUN","apply","<GC>","mean.default","apply","apply","apply","isTRUE","mean.default","apply","<GC>","apply","length","local","FUN","apply","<GC>","FUN","apply","apply","apply","apply","<GC>","FUN","apply","FUN","apply","apply","<GC>","FUN","apply","is.numeric","local","FUN","apply","<GC>","apply","FUN","apply","FUN","apply","length","local","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","is.numeric","local","FUN","apply","FUN","apply","FUN","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","<GC>","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","apply","apply","FUN","apply","FUN","apply","apply","<GC>","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","mean.default","apply","apply","apply","FUN","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","length","local","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","<GC>","FUN","apply","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","FUN","apply","<GC>","mean.default","apply","apply","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","apply","apply","mean.default","apply","apply","<GC>","FUN","apply","length","local","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","apply","<GC>","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","<GC>","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","mean.default","apply","apply","mean.default","apply","<GC>","length","local","apply","is.na","local","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","mean.default","apply","length","local","<GC>","FUN","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","<GC>","FUN","apply","is.numeric","local","FUN","apply","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","<GC>","FUN","apply","mean.default","apply","apply","is.na","local","FUN","apply","FUN","apply","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","FUN","apply","apply","apply","apply","mean.default","apply","is.na","local","isTRUE","mean.default","apply","is.numeric","local","<GC>","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","length","local","FUN","apply","length","local","mean.default","apply","<GC>","apply","length","local","FUN","apply","apply","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","<GC>","apply","apply","FUN","apply","length","local","FUN","apply","apply","apply","FUN","apply","<GC>","FUN","apply","apply","apply","apply","mean.default","apply","isTRUE","mean.default","apply","length","local","mean.default","apply","<GC>","apply","length","local","apply","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","FUN","apply","is.na","local","apply","mean.default","apply","apply","isTRUE","mean.default","apply","length","local","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","FUN","apply","<GC>","isTRUE","mean.default","apply","is.numeric","local","length","local","apply","isTRUE","mean.default","apply","apply","apply","<GC>","is.na","local","<GC>","is.na","local","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","<GC>","is.numeric","local","apply","mean.default","apply","FUN","apply","apply","apply","apply","<GC>","length","local","<GC>","length","local","is.na","local","FUN","apply","mean.default","apply","FUN","apply","apply","apply","<GC>","apply","is.na","local","apply","mean.default","apply","FUN","apply","FUN","apply","length","local","<GC>","apply","<GC>","apply","length","local","FUN","apply","apply","FUN","apply","FUN","apply","mean.default","apply","<GC>","apply","apply","mean.default","apply","FUN","apply","FUN","apply","is.na","local","is.numeric","local","<GC>","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","length","local","mean.default","apply","<GC>","FUN","apply","is.numeric","local","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","apply","length","local","apply","apply","apply","FUN","apply","FUN","apply","<GC>","is.numeric","local","apply","FUN","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","is.numeric","local","<GC>","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","<GC>","mean.default","apply","apply","is.numeric","local","FUN","apply","mean.default","apply","is.na","local","<GC>","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","<GC>","apply","apply","apply","apply","apply","apply","<GC>","length","local","<GC>","length","local","apply","FUN","apply","mean.default","apply","apply","FUN","apply","<GC>","FUN","apply","length","local","isTRUE","mean.default","apply","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","<GC>","apply","apply","mean.default","apply","apply","mean.default","apply","mean.default","apply","<GC>","apply","mean.default","apply","length","local","FUN","apply","length","local","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","<GC>","length","local","apply","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","<GC>","FUN","apply","length","local","mean.default","apply","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","length","local","<GC>","apply","<GC>","apply","apply","mean.default","apply","length","local","apply","<GC>","isTRUE","mean.default","apply","length","local","FUN","apply","FUN","apply","FUN","apply","apply","<GC>","isTRUE","mean.default","apply","apply","FUN","apply","apply","mean.default","apply","<GC>","apply","<GC>","apply","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","<GC>","length","local","apply","apply","apply","mean.default","apply","<GC>","is.numeric","local","apply","apply","apply","mean.default","apply","<GC>","apply","<GC>","apply","apply","FUN","apply","FUN","apply","apply","<GC>","FUN","apply","FUN","apply","mean.default","apply","apply","FUN","apply","<GC>","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","<GC>","apply","<GC>","apply","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","<GC>","length","local","FUN","apply","FUN","apply","FUN","apply","apply","<GC>","apply","FUN","apply","FUN","apply","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","mean.default","apply","FUN","apply","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","apply","FUN","apply","mean.default","apply","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","mean.default","apply","length","local","FUN","apply","apply","apply","mean.default","apply","is.na","local","mean.default","apply","apply","mean.default","apply","FUN","apply","apply","apply","<GC>","is.numeric","local","apply","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","mean.default","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","mean.default","apply","apply","apply","FUN","apply","mean.default","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","mean.default","apply","apply","length","local","is.na","local","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","length","local","apply","<GC>","FUN","apply","mean.default","apply","is.na","local","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","apply","FUN","apply","mean.default","apply","FUN","apply","is.numeric","local","FUN","apply","FUN","apply","apply","apply","apply","mean.default","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","is.na","local","FUN","apply","isTRUE","mean.default","apply","apply","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","apply","apply","apply","isTRUE","mean.default","apply","is.na","local","FUN","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","FUN","apply","apply","apply","apply","mean.default","apply","apply","isTRUE","mean.default","apply","is.numeric","local","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","apply","<GC>","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","apply","apply","apply","mean.default","apply","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","isTRUE","mean.default","apply","length","local","FUN","apply","length","local","apply","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","isTRUE","mean.default","apply","is.na","local","<GC>","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","is.numeric","local","is.na","local","apply","<GC>","apply","<GC>","apply","length","local","mean.default","apply","FUN","apply","apply","FUN","apply","is.numeric","local","apply","mean.default","apply","apply","FUN","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","<GC>","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","FUN","apply","apply","length","local","mean.default","apply","apply","FUN","apply","apply","isTRUE","mean.default","apply","mean.default","apply","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","length","local","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","length","local","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","<GC>","apply","<GC>","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","mean.default","apply","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","length","local","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","apply","apply","apply","apply","length","local","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","apply","apply","FUN","apply","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","is.numeric","local","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","<GC>","apply","is.na","local","FUN","apply","apply","length","local","is.na","local","isTRUE","mean.default","apply","FUN","apply","apply","length","local","apply","<GC>","length","local","<GC>","length","local","isTRUE","mean.default","apply","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","apply","FUN","apply","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","length","local","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","length","local","FUN","apply","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","apply","FUN","apply","FUN","apply","apply","apply","mean.default","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","apply","is.numeric","local","<GC>","apply","<GC>","apply","apply","apply","is.numeric","local","isTRUE","mean.default","apply","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","<GC>","apply","<GC>","apply","mean.default","apply","isTRUE","mean.default","apply","apply","isTRUE","mean.default","apply","is.numeric","local","FUN","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","is.na","local","apply","apply","apply","mean.default","apply","mean.default","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","any","local","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply",".External","local"],"filenum":[null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null],"linenum":[null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null],"memalloc":[122.1817016601562,122.1817016601562,122.1817016601562,122.1817016601562,137.4406509399414,137.4406509399414,137.4406509399414,137.4406509399414,137.441047668457,137.441047668457,137.441047668457,167.4736480712891,167.4736480712891,167.4736480712891,167.4736480712891,167.4736480712891,167.4736480712891,167.4736480712891,167.4736480712891,167.4736480712891,167.4736480712891,167.4730453491211,167.4730453491211,167.4730453491211,167.4730453491211,167.4730453491211,167.4730453491211,167.4730453491211,167.4730453491211,167.4728622436523,167.4728622436523,183.0510635375977,183.0510635375977,183.0510635375977,183.4139251708984,183.4139251708984,183.7682800292969,184.1270599365234,184.4587249755859,184.4587249755859,184.6931610107422,184.6931610107422,184.6931610107422,182.9161529541016,183.2620162963867,183.6035003662109,183.9414596557617,183.9414596557617,184.2917709350586,184.6438903808594,184.7273941040039,184.7273941040039,184.7273941040039,183.1717147827148,183.1717147827148,183.5295715332031,183.8842010498047,183.8842010498047,184.2372665405273,184.5894165039062,184.5894165039062,184.7796096801758,184.7796096801758,184.7796096801758,183.1509170532227,183.1509170532227,183.5020904541016,183.5020904541016,183.8596649169922,183.8596649169922,184.2111968994141,184.5624465942383,184.5624465942383,184.8309173583984,184.8309173583984,184.8309173583984,183.1376953125,183.1376953125,183.4597625732422,183.4597625732422,183.775764465332,183.775764465332,183.775764465332,184.0893173217773,184.0893173217773,184.4145278930664,184.7656097412109,184.7656097412109,184.8814010620117,184.8814010620117,184.8814010620117,183.3608474731445,183.3608474731445,183.7154846191406,183.7154846191406,184.0662612915039,184.0662612915039,184.415168762207,184.7681274414062,184.7681274414062,184.7681274414062,184.9310836791992,184.9310836791992,183.3856201171875,183.3856201171875,183.7416000366211,184.0945510864258,184.44287109375,184.7951583862305,184.7951583862305,184.9799575805664,184.9799575805664,184.9799575805664,183.4509963989258,183.4509963989258,183.8067321777344,184.1592254638672,184.1592254638672,184.5083923339844,184.5083923339844,184.8567504882812,184.8567504882812,185.0280685424805,185.0280685424805,183.5168762207031,183.8714599609375,183.8714599609375,184.2236633300781,184.2236633300781,184.5762023925781,184.5762023925781,184.9290390014648,184.9290390014648,185.0754013061523,185.0754013061523,185.0754013061523,183.6090240478516,183.6090240478516,183.9601287841797,183.9601287841797,184.3098526000977,184.3098526000977,184.6590957641602,184.6590957641602,185.0089492797852,185.0089492797852,185.1218566894531,185.1218566894531,185.1218566894531,185.1218566894531,183.5621185302734,183.9116668701172,184.2622375488281,184.2622375488281,184.6128311157227,184.6128311157227,184.9662246704102,184.9662246704102,184.9662246704102,185.1674957275391,185.1674957275391,185.1674957275391,183.7306213378906,184.0833740234375,184.0833740234375,184.4349212646484,184.7868576049805,184.7868576049805,185.1381759643555,185.1381759643555,185.2125701904297,185.2125701904297,185.2125701904297,183.8937072753906,183.8937072753906,184.1993865966797,184.1993865966797,184.5052490234375,184.5052490234375,184.5052490234375,184.8474426269531,184.8474426269531,185.1948471069336,185.1948471069336,185.2568283081055,185.2568283081055,185.2568283081055,183.9972915649414,183.9972915649414,184.3454360961914,184.3454360961914,184.6944427490234,184.6944427490234,185.0442428588867,185.300537109375,185.300537109375,183.8636245727539,183.8636245727539,184.1682357788086,184.1682357788086,184.4721603393555,184.7910232543945,184.7910232543945,184.7910232543945,185.1432495117188,185.3434143066406,185.3434143066406,185.3434143066406,183.9776229858398,183.9776229858398,184.2810440063477,184.2810440063477,184.5862274169922,184.5862274169922,184.8918914794922,184.8918914794922,184.8918914794922,185.1995086669922,185.1995086669922,185.3856582641602,185.3856582641602,185.3856582641602,184.0393600463867,184.0393600463867,184.3811721801758,184.3811721801758,184.733512878418,184.733512878418,185.0854110717773,185.4271850585938,185.4271850585938,185.4271850585938,185.4271850585938,185.4271850585938,185.4271850585938,184.3189849853516,184.3189849853516,184.3189849853516,184.6647033691406,184.6647033691406,185.0130004882812,185.0130004882812,185.0130004882812,185.3639221191406,185.3639221191406,185.4680328369141,185.4680328369141,185.4680328369141,184.2440643310547,184.5410614013672,184.5410614013672,184.8479537963867,184.8479537963867,185.1893539428711,185.5082473754883,185.5082473754883,185.5082473754883,184.1312561035156,184.1312561035156,184.4272232055664,184.7320861816406,184.7320861816406,185.0600509643555,185.0600509643555,185.4128112792969,185.4128112792969,185.5477523803711,185.5477523803711,184.3457794189453,184.6427841186523,184.9709930419922,185.3222503662109,185.3222503662109,185.5866851806641,185.5866851806641,185.5866851806641,184.3003387451172,184.3003387451172,184.5939254760742,184.5939254760742,184.9428100585938,184.9428100585938,185.2952880859375,185.6249084472656,185.6249084472656,184.3086318969727,184.6354904174805,184.6354904174805,184.9829864501953,185.3321075439453,185.3321075439453,185.6625823974609,185.6625823974609,185.6625823974609,185.6625823974609,185.6625823974609,185.6625823974609,184.6516571044922,184.6516571044922,184.9726715087891,185.3268890380859,185.6768035888672,185.6768035888672,185.6996231079102,185.6996231079102,185.6996231079102,184.6755065917969,184.6755065917969,184.9795913696289,184.9795913696289,185.2895431518555,185.2895431518555,185.5998992919922,185.5998992919922,185.736083984375,185.736083984375,185.736083984375,184.6303405761719,184.6303405761719,184.9272003173828,184.9272003173828,185.2369003295898,185.5557403564453,185.5557403564453,185.7719421386719,185.7719421386719,185.7719421386719,184.6115417480469,184.6115417480469,184.9037322998047,184.9037322998047,185.212890625,185.212890625,185.5244064331055,185.8072204589844,185.8072204589844,185.8072204589844,184.5965270996094,184.9075469970703,184.9075469970703,185.2187042236328,185.5694122314453,185.5694122314453,185.8419418334961,185.8419418334961,185.8419418334961,184.6862716674805,184.6862716674805,185.0138168334961,185.0138168334961,185.3646621704102,185.7176513671875,185.7176513671875,185.8761215209961,185.8761215209961,185.8761215209961,184.8362121582031,184.8362121582031,185.170654296875,185.170654296875,185.5223083496094,185.8705215454102,185.9096603393555,185.9096603393555,184.9744415283203,185.2783050537109,185.5899124145508,185.5899124145508,185.5899124145508,185.9063339233398,185.9427795410156,185.9427795410156,185.9427795410156,185.9427795410156,185.9427795410156,185.9427795410156,185.9427795410156,185.9427795410156,185.9427795410156,184.9396514892578,185.287727355957,185.287727355957,185.6499252319336,185.6499252319336,185.9750823974609,185.9750823974609,185.9750823974609,184.8607864379883,185.1563949584961,185.1563949584961,185.4733200073242,185.4733200073242,185.7927398681641,186.0071182250977,186.0071182250977,186.0071182250977,184.9905471801758,185.3361358642578,185.7009429931641,185.7009429931641,186.0386199951172,186.0386199951172,186.0386199951172,186.0386199951172,185.1780395507812,185.5478363037109,185.9368133544922,185.9368133544922,186.0696487426758,186.0696487426758,186.0696487426758,185.2239990234375,185.6218032836914,186.0090484619141,186.0090484619141,186.0090484619141,186.1001358032227,186.1001358032227,186.1001358032227,185.321159362793,185.321159362793,185.7008895874023,185.7008895874023,186.0848159790039,186.0848159790039,186.1301574707031,186.1301574707031,185.4077224731445,185.4077224731445,185.7867584228516,185.7867584228516,186.15966796875,186.15966796875,186.15966796875,186.15966796875,186.15966796875,186.15966796875,185.4975051879883,185.4975051879883,185.8778076171875,186.1887054443359,186.1887054443359,186.1887054443359,185.2461090087891,185.2461090087891,185.6174011230469,185.6174011230469,185.9999618530273,185.9999618530273,186.2172470092773,186.2172470092773,185.3679428100586,185.3679428100586,185.7376861572266,185.7376861572266,186.115119934082,186.115119934082,186.2453536987305,186.2453536987305,186.2453536987305,185.4846878051758,185.4846878051758,185.4846878051758,185.8633499145508,185.8633499145508,186.2407836914062,186.2407836914062,186.2729721069336,186.2729721069336,185.6333465576172,185.6333465576172,186.0146331787109,186.3001861572266,186.3001861572266,186.3001861572266,185.4264678955078,185.4264678955078,185.7858428955078,185.7858428955078,186.1638717651367,186.3269958496094,186.3269958496094,185.5763473510742,185.5763473510742,185.9477157592773,185.9477157592773,186.3216171264648,186.3216171264648,186.3532485961914,186.3532485961914,185.7608871459961,185.7608871459961,186.1438827514648,186.1438827514648,186.3792190551758,186.3792190551758,186.3792190551758,185.5915832519531,185.9654769897461,186.3479232788086,186.3479232788086,186.3479232788086,186.4047393798828,186.4047393798828,185.8154830932617,185.8154830932617,186.1976623535156,186.1976623535156,186.4298095703125,186.4298095703125,186.4298095703125,185.6877517700195,186.0611724853516,186.4397735595703,186.4545211791992,186.4545211791992,186.4545211791992,185.9349746704102,185.9349746704102,186.3191604614258,186.4787902832031,186.4787902832031,186.4787902832031,185.8291244506836,185.8291244506836,186.2123641967773,186.2123641967773,186.5027084350586,186.5027084350586,185.7458572387695,185.7458572387695,186.1159362792969,186.1159362792969,186.4986572265625,186.4986572265625,186.5261993408203,186.5261993408203,186.5261993408203,186.5261993408203,186.5261993408203,186.5261993408203,186.5261993408203,186.5261993408203,186.5261993408203,186.5261993408203,186.5261993408203,186.5261993408203,186.5261993408203,186.5261993408203,186.5261993408203,186.5261993408203,186.5261993408203,186.5261993408203,186.5261993408203,186.5261993408203,186.5261993408203,186.5261993408203,186.5261993408203,186.5261993408203,186.5261993408203,186.5261993408203,186.5261993408203,186.5261993408203,186.5261993408203,186.5261993408203,185.7560882568359,185.7560882568359,185.7560882568359,186.1548156738281,186.1548156738281,186.5188980102539,186.5188980102539,186.9019241333008,186.9019241333008,187.2493667602539,187.2493667602539,187.5527801513672,187.5527801513672,187.8561630249023,188.1606369018555,188.1606369018555,188.4598693847656,188.4598693847656,188.7607574462891,188.7607574462891,189.0636825561523,189.1334915161133,189.1334915161133,189.1334915161133,189.1334915161133,186.1291351318359,186.1291351318359,186.5069808959961,186.5069808959961,186.8865509033203,187.2646408081055,187.2646408081055,187.6437301635742,188.0215225219727,188.3963394165039,188.3963394165039,188.7710876464844,188.7710876464844,189.142463684082,189.2269821166992,189.2269821166992,189.2269821166992,186.2457275390625,186.2457275390625,186.6176376342773,186.9967803955078,186.9967803955078,187.3705291748047,187.3705291748047,187.7444686889648,188.1180801391602,188.1180801391602,188.4941711425781,188.8726043701172,189.2411041259766,189.2411041259766,189.3188629150391,189.3188629150391,189.3188629150391,186.3820571899414,186.3820571899414,186.7482604980469,186.7482604980469,187.1366119384766,187.1366119384766,187.5117797851562,187.5117797851562,187.5117797851562,187.8823776245117,187.8823776245117,188.2575531005859,188.2575531005859,188.6348648071289,188.6348648071289,189.0099945068359,189.0099945068359,189.3763885498047,189.3763885498047,189.4093704223633,189.4093704223633,189.4093704223633,186.5977249145508,186.9627151489258,186.9627151489258,187.3436737060547,187.718620300293,187.718620300293,187.718620300293,188.0944671630859,188.4705123901367,188.4705123901367,188.8473281860352,189.227165222168,189.227165222168,189.4983291625977,189.4983291625977,189.4983291625977,186.4758682250977,186.8569259643555,186.8569259643555,187.2393112182617,187.2393112182617,187.6169357299805,187.6169357299805,187.9885940551758,187.9885940551758,188.360466003418,188.733528137207,189.1072311401367,189.1072311401367,189.4764862060547,189.5859298706055,189.5859298706055,189.5859298706055,186.7878341674805,186.7878341674805,187.1580429077148,187.1580429077148,187.5390167236328,187.5390167236328,187.9164657592773,187.9164657592773,188.2900619506836,188.2900619506836,188.6620864868164,188.6620864868164,188.6620864868164,189.0362243652344,189.0362243652344,189.4079971313477,189.6720886230469,189.6720886230469,186.7314376831055,187.1053085327148,187.4971694946289,187.4971694946289,187.4971694946289,187.8723831176758,187.8723831176758,188.2402877807617,188.2402877807617,188.6131973266602,188.6131973266602,188.9887542724609,188.9887542724609,189.3645629882812,189.7309722900391,189.7309722900391,189.7567977905273,189.7567977905273,189.7567977905273,187.1169967651367,187.1169967651367,187.4913101196289,187.4913101196289,187.4913101196289,187.8688049316406,188.2347946166992,188.2347946166992,188.6082611083984,188.9827194213867,188.9827194213867,189.3553695678711,189.7304000854492,189.7304000854492,189.8402328491211,189.8402328491211,189.8402328491211,187.1660919189453,187.5393600463867,187.5393600463867,187.9161071777344,187.9161071777344,187.9161071777344,188.2873992919922,188.2873992919922,188.6557846069336,189.0229797363281,189.0229797363281,189.3918762207031,189.3918762207031,189.7636871337891,189.7636871337891,189.9223098754883,189.9223098754883,189.9223098754883,187.2444763183594,187.2444763183594,187.6189956665039,187.6189956665039,188.0018310546875,188.3768463134766,188.3768463134766,188.7457427978516,189.1207046508789,189.1207046508789,189.4937438964844,189.4937438964844,189.8656234741211,189.8656234741211,190.0029754638672,190.0029754638672,190.0029754638672,187.3915328979492,187.3915328979492,187.7635040283203,187.7635040283203,188.1446075439453,188.5147933959961,188.8881454467773,188.8881454467773,189.2601623535156,189.2601623535156,189.6349716186523,189.6349716186523,190.0057373046875,190.0824279785156,190.0824279785156,190.0824279785156,187.5682601928711,187.5682601928711,187.9489135742188,188.3259811401367,188.3259811401367,188.6974411010742,188.6974411010742,189.0708541870117,189.0708541870117,189.4456558227539,189.8224716186523,190.1605606079102,190.1605606079102,190.1605606079102,190.1605606079102,190.1605606079102,190.1605606079102,187.7962112426758,188.1771621704102,188.5419311523438,188.5419311523438,188.5419311523438,188.9046173095703,188.9046173095703,189.2758178710938,189.6507415771484,189.6507415771484,190.0262603759766,190.0262603759766,190.2374038696289,190.2374038696289,190.2374038696289,187.6479263305664,187.6479263305664,188.0210571289062,188.3995590209961,188.7685852050781,189.1375961303711,189.1375961303711,189.5118637084961,189.5118637084961,189.8835144042969,189.8835144042969,189.8835144042969,190.2522048950195,190.2522048950195,190.3130798339844,190.3130798339844,190.3130798339844,187.9130172729492,187.9130172729492,188.289421081543,188.289421081543,188.6642150878906,188.6642150878906,189.0339660644531,189.0339660644531,189.4070053100586,189.4070053100586,189.7844772338867,189.7844772338867,190.1622772216797,190.1622772216797,190.3874588012695,190.3874588012695,187.8886413574219,187.8886413574219,188.2525405883789,188.2525405883789,188.6188125610352,188.9844360351562,189.3500213623047,189.7211227416992,189.7211227416992,190.0950241088867,190.0950241088867,190.4554748535156,190.4554748535156,190.4607162475586,190.4607162475586,188.1762237548828,188.5412139892578,188.5412139892578,188.9120407104492,188.9120407104492,189.2796859741211,189.2796859741211,189.6456146240234,190.0175628662109,190.3903961181641,190.3903961181641,190.5327072143555,190.5327072143555,190.5327072143555,188.1817092895508,188.5491561889648,188.9184265136719,189.2905807495117,189.2905807495117,189.6581878662109,189.6581878662109,189.6581878662109,190.0291748046875,190.0291748046875,190.4043121337891,190.4043121337891,190.6035766601562,190.6035766601562,188.2353210449219,188.2353210449219,188.5977478027344,188.9648971557617,189.3376083374023,189.3376083374023,189.7095031738281,189.7095031738281,190.0714721679688,190.0714721679688,190.0714721679688,190.4466323852539,190.4466323852539,190.6733474731445,190.6733474731445,190.6733474731445,188.3080444335938,188.3080444335938,188.6691436767578,189.0317306518555,189.0317306518555,189.4063186645508,189.7650146484375,189.7650146484375,189.7650146484375,190.1357955932617,190.1357955932617,190.5097732543945,190.5097732543945,190.7419204711914,190.7419204711914,190.7419204711914,190.7419204711914,190.7419204711914,190.7419204711914,190.7419204711914,190.7419204711914,190.7419204711914,190.7419204711914,190.7419204711914,190.7419204711914,190.7419204711914,190.7419204711914,190.7419204711914,190.7419204711914,190.7419204711914,190.7419204711914,188.3805236816406,188.3805236816406,188.3805236816406,188.6289672851562,188.6289672851562,188.9883193969727,189.3466644287109,189.3466644287109,189.7102508544922,189.7102508544922,190.0726547241211,190.4342422485352,190.4342422485352,190.8034591674805,190.8034591674805,190.80908203125,190.80908203125,190.80908203125,190.80908203125,188.7485275268555,188.7485275268555,189.1042556762695,189.1042556762695,189.4734802246094,189.8415756225586,189.8415756225586,189.8415756225586,190.2125778198242,190.5799560546875,190.87548828125,190.87548828125,190.87548828125,190.87548828125,190.87548828125,190.87548828125,188.9363479614258,188.9363479614258,189.2938079833984,189.2938079833984,189.6636962890625,189.6636962890625,190.0330963134766,190.0330963134766,190.0330963134766,190.4056091308594,190.781494140625,190.781494140625,190.9408264160156,190.9408264160156,190.9408264160156,188.8032379150391,189.156608581543,189.156608581543,189.5231399536133,189.5231399536133,189.8901901245117,190.2644195556641,190.6343231201172,191.0050888061523,191.0050888061523,191.0050888061523,191.0050888061523,191.0050888061523,191.0050888061523,189.0553970336914,189.0553970336914,189.4142303466797,189.4142303466797,189.7883529663086,189.7883529663086,190.1571807861328,190.1571807861328,190.5298919677734,190.9039077758789,191.0683288574219,191.0683288574219,188.9939270019531,188.9939270019531,189.3475723266602,189.7183074951172,189.7183074951172,190.084831237793,190.084831237793,190.4547500610352,190.4547500610352,190.8253936767578,190.8253936767578,191.1305618286133,191.1305618286133,191.1305618286133,191.1305618286133,189.3116683959961,189.3116683959961,189.6747207641602,189.6747207641602,190.0451354980469,190.4062652587891,190.4062652587891,190.7751159667969,190.7751159667969,191.1473388671875,191.1473388671875,191.1918182373047,191.1918182373047,189.2806091308594,189.6309967041016,189.6309967041016,189.9999847412109,189.9999847412109,190.3725204467773,190.3725204467773,190.744384765625,190.744384765625,191.1219940185547,191.1219940185547,191.2520294189453,191.2520294189453,191.2520294189453,189.2730255126953,189.2730255126953,189.6188659667969,189.6188659667969,189.9777297973633,189.9777297973633,190.3435821533203,190.3435821533203,190.7105255126953,190.7105255126953,191.0820007324219,191.0820007324219,191.3113479614258,191.3113479614258,191.3113479614258,189.2972106933594,189.2972106933594,189.6476364135742,189.6476364135742,189.6476364135742,190.0136413574219,190.0136413574219,190.3827056884766,190.3827056884766,190.7522201538086,190.7522201538086,191.1251449584961,191.1251449584961,191.1251449584961,191.3696136474609,191.3696136474609,189.3739471435547,189.3739471435547,189.7226638793945,190.0919723510742,190.4619445800781,190.8340759277344,190.8340759277344,191.2078399658203,191.2078399658203,191.4270095825195,191.4270095825195,191.4270095825195,189.5035247802734,189.8605270385742,189.8605270385742,190.2332534790039,190.2332534790039,190.6040802001953,190.6040802001953,190.981330871582,190.981330871582,190.981330871582,191.3572082519531,191.3572082519531,191.4834060668945,191.4834060668945,189.6761245727539,189.6761245727539,190.032112121582,190.032112121582,190.4034042358398,190.4034042358398,190.7689590454102,190.7689590454102,191.139892578125,191.139892578125,191.5114288330078,191.5389556884766,191.5389556884766,191.5389556884766,189.8420639038086,190.1996307373047,190.1996307373047,190.5761871337891,190.5761871337891,190.94580078125,190.94580078125,191.3162078857422,191.3162078857422,191.5936126708984,191.5936126708984,191.5936126708984,191.5936126708984,191.5936126708984,191.5936126708984,190.0448989868164,190.4131088256836,190.4131088256836,190.7835464477539,190.7835464477539,190.7835464477539,191.1539688110352,191.1539688110352,191.5284881591797,191.6473083496094,191.6473083496094,189.9345932006836,190.2794036865234,190.6448516845703,191.0071029663086,191.3717498779297,191.7002105712891,191.7002105712891,191.7002105712891,191.7002105712891,191.7002105712891,191.7002105712891,190.1508865356445,190.5093841552734,190.5093841552734,190.8826599121094,190.8826599121094,191.2503128051758,191.615234375,191.615234375,191.7522811889648,191.7522811889648,191.7522811889648,190.0593719482422,190.0593719482422,190.4103240966797,190.4103240966797,190.4103240966797,190.7799835205078,191.1448440551758,191.1448440551758,191.511962890625,191.511962890625,191.511962890625,191.8034210205078,191.8034210205078,191.8034210205078,191.8034210205078,191.8034210205078,191.8034210205078,190.3648986816406,190.7324752807617,191.1019744873047,191.1019744873047,191.4634552001953,191.4634552001953,191.8335113525391,191.8335113525391,191.8537826538086,191.8537826538086,190.3244018554688,190.6828994750977,190.6828994750977,191.0529098510742,191.419189453125,191.419189453125,191.7846832275391,191.7846832275391,191.9033432006836,191.9033432006836,190.3137893676758,190.3137893676758,190.6700134277344,190.6700134277344,191.0440826416016,191.0440826416016,191.4126358032227,191.4126358032227,191.7848587036133,191.9521179199219,191.9521179199219,191.9521179199219,191.9521179199219,191.9521179199219,191.9521179199219,191.9521179199219,191.9521179199219,191.9521179199219,191.9521179199219,190.442138671875,190.8063888549805,190.8063888549805,190.8063888549805,191.1794204711914,191.1794204711914,191.5471115112305,191.9163131713867,192,192,192,190.5029144287109,190.8602523803711,191.2334213256836,191.2334213256836,191.5956268310547,191.5956268310547,191.5956268310547,191.9681396484375,191.9681396484375,192.0472946166992,192.0472946166992,192.0472946166992,190.5653686523438,190.924186706543,190.924186706543,190.924186706543,191.2923126220703,191.2923126220703,191.6627655029297,191.6627655029297,192.0345611572266,192.0345611572266,192.0937118530273,192.0937118530273,192.0937118530273,190.6484298706055,190.6484298706055,191.0065536499023,191.0065536499023,191.3766784667969,191.7475662231445,191.7475662231445,192.1155776977539,192.1155776977539,192.1155776977539,192.1394195556641,192.1394195556641,192.1394195556641,190.7566375732422,190.7566375732422,191.1193237304688,191.1193237304688,191.4948577880859,191.4948577880859,191.867431640625,191.867431640625,192.1843566894531,192.1843566894531,192.1843566894531,192.1843566894531,190.9103012084961,191.2786102294922,191.2786102294922,191.6495666503906,191.6495666503906,192.0193099975586,192.2286224365234,192.2286224365234,192.2286224365234,192.2286224365234,190.7372512817383,190.7372512817383,191.0963973999023,191.0963973999023,191.4727935791016,191.4727935791016,191.8402404785156,191.8402404785156,192.2121963500977,192.2721099853516,192.2721099853516,192.2721099853516,192.2721099853516,190.9517059326172,191.3131866455078,191.3131866455078,191.6877212524414,192.0563888549805,192.0563888549805,192.3149795532227,192.3149795532227,192.3149795532227,192.3149795532227,191.1625747680664,191.1625747680664,191.5339965820312,191.5339965820312,191.9055023193359,191.9055023193359,192.2748947143555,192.2748947143555,192.3570327758789,192.3570327758789,192.3570327758789,191.0526580810547,191.4147720336914,191.7896575927734,192.1577606201172,192.1577606201172,192.3985290527344,192.3985290527344,192.3985290527344,190.9752578735352,191.3237609863281,191.7010269165039,192.0729904174805,192.0729904174805,192.4393615722656,192.4393615722656,192.4393615722656,192.4393615722656,191.2614288330078,191.6310501098633,191.6310501098633,192.0033569335938,192.0033569335938,192.3743667602539,192.4794235229492,192.4794235229492,192.4794235229492,191.2173767089844,191.2173767089844,191.5822372436523,191.5822372436523,191.9503936767578,192.3204040527344,192.3204040527344,192.518913269043,192.518913269043,192.518913269043,191.1912231445312,191.1912231445312,191.5500640869141,191.9308471679688,191.9308471679688,192.3046264648438,192.3046264648438,192.5577926635742,192.5577926635742,192.5577926635742,192.5577926635742,191.5206909179688,191.8899459838867,191.8899459838867,192.2565536499023,192.2565536499023,192.2565536499023,192.595947265625,192.595947265625,192.595947265625,192.595947265625,192.595947265625,192.595947265625,191.5157699584961,191.5157699584961,191.8867568969727,191.8867568969727,192.2582321166992,192.2582321166992,192.6216049194336,192.6216049194336,192.6335830688477,192.6335830688477,192.6335830688477,191.5332183837891,191.5332183837891,191.902587890625,191.902587890625,192.2744216918945,192.2744216918945,192.6345672607422,192.670539855957,192.670539855957,191.5690765380859,191.5690765380859,191.9374008178711,191.9374008178711,192.312744140625,192.6818466186523,192.7069244384766,192.7069244384766,192.7069244384766,192.7069244384766,192.7069244384766,192.7069244384766,192.7069244384766,192.7069244384766,192.7069244384766,191.5276565551758,191.8911743164062,192.2688674926758,192.2688674926758,192.6262664794922,192.6262664794922,192.6262664794922,192.7424774169922,192.7424774169922,192.7424774169922,192.7424774169922,192.7424774169922,192.7424774169922,192.7424774169922,192.7424774169922,192.7424774169922,192.7424774169922,192.7424774169922,192.7424774169922,192.7424774169922,192.7424774169922,192.7424774169922,192.7424774169922,192.7424774169922,192.7424774169922,192.7424774169922,192.7424774169922,192.7424774169922,192.7424774169922,192.7424774169922,192.7424774169922,192.7424774169922,192.7424774169922,192.7424774169922,192.7424774169922,192.7424774169922,192.7424774169922,192.7424774169922,192.7424774169922,192.7424774169922,192.7424774169922,192.7424774169922,192.7424774169922,192.7424774169922,192.7424774169922,192.7424774169922,192.7424774169922,192.7424774169922,192.7424774169922,191.5100479125977,191.5100479125977,191.5535202026367,191.5535202026367,191.5535202026367,191.9501419067383,192.3271713256836,192.3271713256836,192.6616973876953,193.0221176147461,193.0221176147461,193.3870468139648,193.3870468139648,193.7414016723633,194.0442199707031,194.0442199707031,194.3420562744141,194.3420562744141,194.6450653076172,194.6450653076172,194.6450653076172,194.9447479248047,194.9447479248047,195.2455291748047,195.2455291748047,195.5464096069336,195.8495025634766,195.8495025634766,196.1515350341797,196.1515350341797,196.4519805908203,196.7546081542969,196.872184753418,196.872184753418,196.872184753418,196.872184753418,196.872184753418,196.872184753418,192.1224517822266,192.5066070556641,192.5066070556641,192.855094909668,192.855094909668,193.2309494018555,193.2309494018555,193.6085586547852,193.9863586425781,194.3596343994141,194.3596343994141,194.733039855957,194.733039855957,195.108039855957,195.108039855957,195.4815063476562,195.8503265380859,195.8503265380859,196.2257843017578,196.2257843017578,196.6004943847656,196.9613800048828,197.0187759399414,197.0187759399414,197.0187759399414,192.0641174316406,192.4599456787109,192.8250045776367,192.8250045776367,192.8250045776367,193.1902236938477,193.5576629638672,193.9245300292969,193.9245300292969,194.299201965332,194.299201965332,194.6729202270508,194.6729202270508,195.0475616455078,195.0475616455078,195.4206390380859,195.4206390380859,195.796142578125,196.1676254272461,196.5435104370117,196.5435104370117,196.9110107421875,197.1631164550781,197.1631164550781,197.1631164550781,197.1631164550781,197.1631164550781,197.1631164550781,192.446044921875,192.446044921875,192.8318023681641,192.8318023681641,193.1832885742188,193.5575103759766,193.5575103759766,193.9288177490234,193.9288177490234,194.2985458374023,194.6684494018555,194.6684494018555,195.0415115356445,195.0415115356445,195.4151229858398,195.4151229858398,195.7876358032227,196.1558609008789,196.5227203369141,196.5227203369141,196.8907241821289,196.8907241821289,197.2397689819336,197.3050384521484,197.3050384521484,197.3050384521484,197.3050384521484,197.3050384521484,197.3050384521484,197.3050384521484,197.3050384521484,197.3050384521484,192.4203338623047,192.4203338623047,192.4203338623047,192.7408676147461,192.7408676147461,193.0879745483398,193.0879745483398,193.4159393310547,193.4159393310547,193.782844543457,194.1471557617188,194.1471557617188,194.5111389160156,194.8740081787109,194.8740081787109,195.2380981445312,195.2380981445312,195.6007919311523,195.6007919311523,195.9654235839844,195.9654235839844,196.3311309814453,196.3311309814453,196.6999588012695,196.6999588012695,197.0602645874023,197.0602645874023,197.4252014160156,197.444694519043,197.444694519043,197.444694519043,192.7227554321289,192.7227554321289,193.1161804199219,193.1161804199219,193.4664688110352,193.8358001708984,193.8358001708984,194.2055740356445,194.5738296508789,194.5738296508789,194.9441528320312,194.9441528320312,195.3131256103516,195.3131256103516,195.6837310791016,195.6837310791016,196.0557250976562,196.0557250976562,196.4266815185547,196.4266815185547,196.7988815307617,196.7988815307617,197.1743850708008,197.1743850708008,197.5472183227539,197.5820770263672,197.5820770263672,197.5820770263672,192.929801940918,192.929801940918,193.3146209716797,193.3146209716797,193.6708908081055,193.6708908081055,194.0383071899414,194.0383071899414,194.4079055786133,194.4079055786133,194.7732162475586,194.7732162475586,194.7732162475586,195.1417465209961,195.5132293701172,195.8797454833984,195.8797454833984,196.2522888183594,196.2522888183594,196.2522888183594,196.623046875,196.623046875,196.9954528808594,196.9954528808594,197.3699188232422,197.3699188232422,197.7173309326172,197.7173309326172,197.7173309326172,197.7173309326172,197.7173309326172,197.7173309326172,193.2106018066406,193.5802536010742,193.9431381225586,193.9431381225586,194.3118743896484,194.3118743896484,194.67822265625,194.67822265625,195.0467300415039,195.0467300415039,195.4175033569336,195.4175033569336,195.7898635864258,195.7898635864258,196.1629867553711,196.5349884033203,196.9063568115234,197.2788238525391,197.2788238525391,197.6506118774414,197.6506118774414,197.8503036499023,197.8503036499023,197.8503036499023,197.8503036499023,197.8503036499023,197.8503036499023,193.5671234130859,193.5671234130859,193.5671234130859,193.9221115112305,193.9221115112305,193.9221115112305,194.2934112548828,194.2934112548828,194.6568374633789,194.6568374633789,195.0209197998047,195.0209197998047,195.387336730957,195.387336730957,195.387336730957,195.7561645507812,196.1224517822266,196.4921264648438,196.4921264648438,196.8599243164062,196.8599243164062,197.233039855957,197.5974578857422,197.5974578857422,197.956169128418,197.956169128418,197.9812164306641,197.9812164306641,197.9812164306641,193.5530776977539,193.5530776977539,193.5530776977539,193.9214401245117,194.2881164550781,194.654052734375,195.0177688598633,195.0177688598633,195.0177688598633,195.3813705444336,195.3813705444336,195.7468490600586,195.7468490600586,196.1136093139648,196.1136093139648,196.4856033325195,196.8474349975586,197.2168350219727,197.2168350219727,197.2168350219727,197.5900497436523,197.5900497436523,197.9549331665039,198.1099853515625,198.1099853515625,198.1099853515625,198.1099853515625,193.9691467285156,193.9691467285156,194.3290023803711,194.693229675293,195.0551376342773,195.4145812988281,195.4145812988281,195.7776718139648,196.1422653198242,196.1422653198242,196.1422653198242,196.5077819824219,196.5077819824219,196.8738403320312,196.8738403320312,197.2416152954102,197.2416152954102,197.6108169555664,197.6108169555664,197.9793167114258,197.9793167114258,198.2366256713867,198.2366256713867,198.2366256713867,198.2366256713867,194.0763244628906,194.0763244628906,194.4363861083984,194.4363861083984,194.8054275512695,194.8054275512695,195.1658401489258,195.1658401489258,195.5294418334961,195.5294418334961,195.8938903808594,195.8938903808594,196.2624588012695,196.2624588012695,196.6312561035156,196.6312561035156,197.002197265625,197.002197265625,197.3745574951172,197.3745574951172,197.7479705810547,197.7479705810547,198.1157836914062,198.1157836914062,198.361328125,198.361328125,198.361328125,198.361328125,194.2814102172852,194.6429214477539,195.0086822509766,195.0086822509766,195.3694152832031,195.3694152832031,195.3694152832031,195.7317504882812,195.7317504882812,196.0987396240234,196.4624481201172,196.4624481201172,196.8306503295898,197.2019577026367,197.5745468139648,197.949104309082,197.949104309082,198.3144073486328,198.4839477539062,198.4839477539062,198.4839477539062,198.4839477539062,198.4839477539062,198.4839477539062,198.4839477539062,198.4839477539062,194.5353088378906,194.5353088378906,194.5353088378906,194.9052200317383,194.9052200317383,195.2735290527344,195.2735290527344,195.6320343017578,195.6320343017578,195.9939727783203,196.357780456543,196.7278594970703,196.7278594970703,197.1001129150391,197.4687423706055,197.4687423706055,197.4687423706055,197.8380966186523,198.2097778320312,198.2097778320312,198.2097778320312,198.570915222168,198.570915222168,198.6045913696289,198.6045913696289,198.6045913696289,194.4974212646484,194.4974212646484,194.8667602539062,194.8667602539062,195.2390975952148,195.2390975952148,195.5967559814453,195.5967559814453,195.5967559814453,195.9549407958984,196.318115234375,196.318115234375,196.6841659545898,196.6841659545898,196.6841659545898,197.0519409179688,197.0519409179688,197.4251937866211,197.4251937866211,197.795295715332,197.795295715332,198.1681823730469,198.1681823730469,198.5374145507812,198.7232437133789,198.7232437133789,198.7232437133789,198.7232437133789,194.8907623291016,194.8907623291016,195.2597885131836,195.2597885131836,195.6184310913086,195.6184310913086,195.9754028320312,196.3370056152344,196.3370056152344,196.704833984375,196.704833984375,197.0769729614258,197.4486923217773,197.4486923217773,197.8187789916992,198.1882781982422,198.1882781982422,198.5568923950195,198.8400421142578,198.8400421142578,198.8400421142578,198.8400421142578,198.8400421142578,198.8400421142578,194.9632720947266,194.9632720947266,195.3256530761719,195.3256530761719,195.6839370727539,195.6839370727539,196.0357666015625,196.0357666015625,196.393928527832,196.393928527832,196.7567977905273,196.7567977905273,197.1209564208984,197.1209564208984,197.4860916137695,197.4860916137695,197.856330871582,197.856330871582,198.2288665771484,198.2288665771484,198.596549987793,198.596549987793,198.9528961181641,198.9528961181641,198.9549865722656,198.9549865722656,195.0518569946289,195.0518569946289,195.4175796508789,195.4175796508789,195.7749938964844,195.7749938964844,196.1250534057617,196.1250534057617,196.4832000732422,196.4832000732422,196.8467864990234,196.8467864990234,197.2155838012695,197.5830993652344,197.5830993652344,197.9530563354492,198.3274765014648,198.3274765014648,198.3274765014648,198.6984100341797,198.6984100341797,199.0518569946289,199.0518569946289,199.0518569946289,199.0679779052734,199.0679779052734,199.0679779052734,195.233283996582,195.233283996582,195.5925445556641,195.9487380981445,195.9487380981445,196.298957824707,196.298957824707,196.6586151123047,197.0234909057617,197.0234909057617,197.3922271728516,197.7610244750977,197.7610244750977,197.7610244750977,198.1316528320312,198.1316528320312,198.5001831054688,198.8740615844727,198.8740615844727,199.1792221069336,199.1792221069336,199.1792221069336,199.1792221069336,199.1792221069336,199.1792221069336,195.4150238037109,195.4150238037109,195.7732543945312,196.1270980834961,196.4733123779297,196.4733123779297,196.8066635131836,197.1507186889648,197.1507186889648,197.5114974975586,197.5114974975586,197.8771209716797,197.8771209716797,198.2460403442383,198.6142959594727,198.6142959594727,198.9838714599609,198.9838714599609,198.9838714599609,199.2886657714844,199.2886657714844,199.2886657714844,199.2886657714844,199.2886657714844,199.2886657714844,195.6113357543945,195.9658203125,195.9658203125,196.3138427734375,196.6643905639648,196.6643905639648,196.6643905639648,197.025146484375,197.025146484375,197.388786315918,197.388786315918,197.7553558349609,197.7553558349609,198.1217651367188,198.4216079711914,198.4216079711914,198.4216079711914,198.7027206420898,198.7027206420898,199.067756652832,199.067756652832,199.3963088989258,199.3963088989258,199.3963088989258,199.3963088989258,195.7428207397461,195.7428207397461,196.0974578857422,196.0974578857422,196.4441986083984,196.4441986083984,196.7897109985352,196.7897109985352,197.1465148925781,197.5099105834961,197.5099105834961,197.8706283569336,197.8706283569336,198.2351150512695,198.2351150512695,198.2351150512695,198.6023635864258,198.9740447998047,198.9740447998047,198.9740447998047,199.3400802612305,199.3400802612305,199.5022277832031,199.5022277832031,199.5022277832031,199.5022277832031,199.5022277832031,199.5022277832031,196.0835189819336,196.4330139160156,196.4330139160156,196.7848510742188,196.7848510742188,196.7848510742188,197.1421127319336,197.1421127319336,197.5039291381836,197.8727951049805,197.8727951049805,198.2418060302734,198.2418060302734,198.6127777099609,198.6127777099609,198.9854278564453,199.3553771972656,199.3553771972656,199.6064987182617,199.6064987182617,199.6064987182617,199.6064987182617,199.6064987182617,199.6064987182617,196.1822967529297,196.1822967529297,196.5345306396484,196.5345306396484,196.8826370239258,196.8826370239258,197.2369766235352,197.2369766235352,197.5954284667969,197.5954284667969,197.9598693847656,197.9598693847656,198.3280868530273,198.6905746459961,198.6905746459961,199.0601196289062,199.0601196289062,199.4312973022461,199.4312973022461,199.7090225219727,199.7090225219727,199.7090225219727,199.7090225219727,199.7090225219727,199.7090225219727,196.3006362915039,196.3006362915039,196.3006362915039,196.6523056030273,196.6523056030273,196.9971389770508,196.9971389770508,197.3467025756836,197.7070541381836,197.7070541381836,198.0704650878906,198.4406356811523,198.8122024536133,199.1825256347656,199.5539855957031,199.5539855957031,199.8098526000977,199.8098526000977,199.8098526000977,199.8098526000977,199.8098526000977,199.8098526000977,199.8098526000977,199.8098526000977,199.8098526000977,199.8098526000977,199.8098526000977,199.8098526000977,199.8098526000977,199.8098526000977,199.8098526000977,199.8098526000977,199.8098526000977,199.8098526000977,199.8098526000977,199.8098526000977,196.3772583007812,196.7331924438477,197.0842514038086,197.0842514038086,197.4374389648438,197.8012466430664,197.8012466430664,198.1633224487305,198.5312271118164,198.897819519043,198.897819519043,198.897819519043,199.2673721313477,199.2673721313477,199.6400985717773,199.6400985717773,199.6400985717773,199.9089050292969,199.9089050292969,199.9089050292969,199.9089050292969,199.9089050292969,199.9089050292969,196.5946197509766,196.5946197509766,196.9413909912109,196.9413909912109,197.2861785888672,197.2861785888672,197.2861785888672,197.6376342773438,197.6376342773438,198.0009307861328,198.0009307861328,198.3627243041992,198.3627243041992,198.3627243041992,198.7310638427734,198.7310638427734,199.0665664672852,199.0665664672852,199.0665664672852,199.4341125488281,199.7976379394531,200.0065765380859,200.0065765380859,200.0065765380859,200.0065765380859,200.0065765380859,200.0065765380859,196.8325958251953,196.8325958251953,197.1802520751953,197.5320739746094,197.5320739746094,197.8892974853516,197.8892974853516,198.250602722168,198.250602722168,198.250602722168,198.619255065918,198.9914703369141,198.9914703369141,198.9914703369141,199.3654174804688,199.3654174804688,199.3654174804688,199.7375793457031,199.7375793457031,200.096305847168,200.1026229858398,200.1026229858398,196.8243789672852,196.8243789672852,197.1738967895508,197.1738967895508,197.520637512207,197.8716506958008,197.8716506958008,198.2302932739258,198.2302932739258,198.5931701660156,198.5931701660156,198.5931701660156,198.961296081543,198.961296081543,199.3326721191406,199.7022171020508,199.7022171020508,200.0667953491211,200.1972274780273,200.1972274780273,200.1972274780273,200.1972274780273,200.1972274780273,200.1972274780273,197.2069473266602,197.2069473266602,197.2069473266602,197.553092956543,197.9063949584961,197.9063949584961,197.9063949584961,198.2678756713867,198.2678756713867,198.2678756713867,198.6305770874023,198.6305770874023,198.99755859375,199.3658065795898,199.3658065795898,199.7338562011719,200.1008911132812,200.1008911132812,200.2902374267578,200.2902374267578,200.2902374267578,200.2902374267578,200.2902374267578,200.2902374267578,197.2906341552734,197.2906341552734,197.6364593505859,197.6364593505859,197.9914321899414,197.9914321899414,198.3520584106445,198.3520584106445,198.7193222045898,198.7193222045898,199.0859069824219,199.0859069824219,199.455078125,199.455078125,199.8286666870117,200.1994781494141,200.1994781494141,200.1994781494141,200.3817825317383,200.3817825317383,200.3817825317383,200.3817825317383,200.3817825317383,200.3817825317383,197.4404983520508,197.4404983520508,197.7894439697266,198.1420288085938,198.1420288085938,198.5045776367188,198.5045776367188,198.8697280883789,199.2376022338867,199.6064300537109,199.6064300537109,199.9796142578125,199.9796142578125,200.3451309204102,200.4718246459961,200.4718246459961,200.4718246459961,200.4718246459961,197.6211090087891,197.6211090087891,197.6211090087891,197.9699401855469,197.9699401855469,198.3246154785156,198.3246154785156,198.6855392456055,198.6855392456055,199.0471878051758,199.0471878051758,199.4132308959961,199.4132308959961,199.7786331176758,200.1409149169922,200.5024337768555,200.5024337768555,200.5603790283203,200.5603790283203,200.5603790283203,200.5603790283203,197.8000106811523,198.1477890014648,198.5043258666992,198.5043258666992,198.8643798828125,198.8643798828125,198.8643798828125,199.2290649414062,199.5936584472656,199.5936584472656,199.5936584472656,199.9609375,199.9609375,199.9609375,200.3339691162109,200.6476058959961,200.6476058959961,200.6476058959961,200.6476058959961,200.6476058959961,200.6476058959961,197.6926116943359,197.6926116943359,198.0440902709961,198.3971481323242,198.3971481323242,198.7565383911133,198.7565383911133,199.1197814941406,199.1197814941406,199.1197814941406,199.4821395874023,199.4821395874023,199.8506774902344,199.8506774902344,200.2228775024414,200.5893859863281,200.5893859863281,200.7333374023438,200.7333374023438,200.7333374023438,200.7333374023438,198.0087509155273,198.0087509155273,198.3586120605469,198.3586120605469,198.3586120605469,198.7097854614258,199.0610427856445,199.0610427856445,199.0610427856445,199.4198837280273,199.4198837280273,199.7829437255859,199.7829437255859,200.1496963500977,200.1496963500977,200.1496963500977,200.5173110961914,200.5173110961914,200.8177261352539,200.8177261352539,200.8177261352539,200.8177261352539,200.8177261352539,200.8177261352539,197.9658813476562,197.9658813476562,198.3131790161133,198.6650085449219,199.0234375,199.3840560913086,199.3840560913086,199.7471389770508,199.7471389770508,207.4083404541016,207.4083404541016,207.4083404541016,207.4083404541016,207.4083404541016,207.4083404541016,207.4083404541016,207.4083404541016,207.4083404541016,207.4083404541016,215.0377349853516,215.0377349853516,215.0377655029297,215.0377655029297,215.0377655029297,215.0377655029297,215.0377655029297,215.0377655029297,215.0377655029297,215.0377655029297,215.0377655029297,215.0377655029297,215.0377655029297,215.0377655029297,215.0377655029297,215.0377655029297,230.2965545654297,230.2965545654297,230.2965545654297,230.2965545654297,230.2965545654297,230.2965545654297,230.2965545654297,230.2965545654297,230.2965545654297,230.2965545654297,253.18505859375,253.18505859375],"meminc":[0,0,0,0,15.25894927978516,0,0,0,0.000396728515625,0,0,30.03260040283203,0,0,0,0,0,0,0,0,0,-0.00060272216796875,0,0,0,0,0,0,0,-0.00018310546875,0,15.57820129394531,0,0,0.3628616333007812,0,0.3543548583984375,0.3587799072265625,0.3316650390625,0,0.23443603515625,0,0,-1.777008056640625,0.3458633422851562,0.3414840698242188,0.3379592895507812,0,0.350311279296875,0.3521194458007812,0.08350372314453125,0,0,-1.555679321289062,0,0.3578567504882812,0.3546295166015625,0,0.3530654907226562,0.3521499633789062,0,0.1901931762695312,0,0,-1.628692626953125,0,0.3511734008789062,0,0.357574462890625,0,0.351531982421875,0.3512496948242188,0,0.2684707641601562,0,0,-1.693222045898438,0,0.3220672607421875,0,0.3160018920898438,0,0,0.3135528564453125,0,0.3252105712890625,0.3510818481445312,0,0.1157913208007812,0,0,-1.520553588867188,0,0.3546371459960938,0,0.3507766723632812,0,0.348907470703125,0.3529586791992188,0,0,0.1629562377929688,0,-1.545463562011719,0,0.3559799194335938,0.3529510498046875,0.3483200073242188,0.3522872924804688,0,0.1847991943359375,0,0,-1.528961181640625,0,0.3557357788085938,0.3524932861328125,0,0.3491668701171875,0,0.348358154296875,0,0.1713180541992188,0,-1.511192321777344,0.354583740234375,0,0.352203369140625,0,0.3525390625,0,0.3528366088867188,0,0.1463623046875,0,0,-1.466377258300781,0,0.351104736328125,0,0.3497238159179688,0,0.3492431640625,0,0.349853515625,0,0.1129074096679688,0,0,0,-1.559738159179688,0.34954833984375,0.3505706787109375,0,0.3505935668945312,0,0.3533935546875,0,0,0.2012710571289062,0,0,-1.436874389648438,0.352752685546875,0,0.3515472412109375,0.3519363403320312,0,0.351318359375,0,0.07439422607421875,0,0,-1.318862915039062,0,0.3056793212890625,0,0.3058624267578125,0,0,0.342193603515625,0,0.3474044799804688,0,0.061981201171875,0,0,-1.259536743164062,0,0.34814453125,0,0.3490066528320312,0,0.3498001098632812,0.2562942504882812,0,-1.436912536621094,0,0.3046112060546875,0,0.303924560546875,0.3188629150390625,0,0,0.3522262573242188,0.200164794921875,0,0,-1.365791320800781,0,0.3034210205078125,0,0.3051834106445312,0,0.3056640625,0,0,0.3076171875,0,0.1861495971679688,0,0,-1.346298217773438,0,0.3418121337890625,0,0.3523406982421875,0,0.351898193359375,0.3417739868164062,0,0,0,0,0,-1.108200073242188,0,0,0.3457183837890625,0,0.348297119140625,0,0,0.350921630859375,0,0.1041107177734375,0,0,-1.223968505859375,0.2969970703125,0,0.3068923950195312,0,0.341400146484375,0.3188934326171875,0,0,-1.376991271972656,0,0.2959671020507812,0.3048629760742188,0,0.3279647827148438,0,0.3527603149414062,0,0.1349411010742188,0,-1.201972961425781,0.2970046997070312,0.3282089233398438,0.35125732421875,0,0.264434814453125,0,0,-1.286346435546875,0,0.2935867309570312,0,0.3488845825195312,0,0.35247802734375,0.329620361328125,0,-1.316276550292969,0.3268585205078125,0,0.3474960327148438,0.34912109375,0,0.330474853515625,0,0,0,0,0,-1.01092529296875,0,0.321014404296875,0.354217529296875,0.34991455078125,0,0.02281951904296875,0,0,-1.024116516113281,0,0.3040847778320312,0,0.3099517822265625,0,0.3103561401367188,0,0.1361846923828125,0,0,-1.105743408203125,0,0.2968597412109375,0,0.3097000122070312,0.3188400268554688,0,0.2162017822265625,0,0,-1.160400390625,0,0.2921905517578125,0,0.3091583251953125,0,0.3115158081054688,0.2828140258789062,0,0,-1.210693359375,0.3110198974609375,0,0.3111572265625,0.3507080078125,0,0.2725296020507812,0,0,-1.155670166015625,0,0.327545166015625,0,0.3508453369140625,0.3529891967773438,0,0.1584701538085938,0,0,-1.039909362792969,0,0.334442138671875,0,0.351654052734375,0.3482131958007812,0.0391387939453125,0,-0.9352188110351562,0.303863525390625,0.3116073608398438,0,0,0.3164215087890625,0.03644561767578125,0,0,0,0,0,0,0,0,-1.003128051757812,0.3480758666992188,0,0.3621978759765625,0,0.3251571655273438,0,0,-1.114295959472656,0.2956085205078125,0,0.316925048828125,0,0.3194198608398438,0.2143783569335938,0,0,-1.016571044921875,0.3455886840820312,0.36480712890625,0,0.337677001953125,0,0,0,-0.8605804443359375,0.3697967529296875,0.38897705078125,0,0.1328353881835938,0,0,-0.8456497192382812,0.3978042602539062,0.3872451782226562,0,0,0.09108734130859375,0,0,-0.7789764404296875,0,0.379730224609375,0,0.3839263916015625,0,0.04534149169921875,0,-0.7224349975585938,0,0.3790359497070312,0,0.3729095458984375,0,0,0,0,0,-0.6621627807617188,0,0.3803024291992188,0.3108978271484375,0,0,-0.942596435546875,0,0.3712921142578125,0,0.3825607299804688,0,0.21728515625,0,-0.84930419921875,0,0.3697433471679688,0,0.3774337768554688,0,0.1302337646484375,0,0,-0.7606658935546875,0,0,0.378662109375,0,0.3774337768554688,0,0.03218841552734375,0,-0.6396255493164062,0,0.38128662109375,0.285552978515625,0,0,-0.87371826171875,0,0.359375,0,0.3780288696289062,0.1631240844726562,0,-0.7506484985351562,0,0.371368408203125,0,0.3739013671875,0,0.0316314697265625,0,-0.5923614501953125,0,0.38299560546875,0,0.2353363037109375,0,0,-0.7876358032226562,0.3738937377929688,0.3824462890625,0,0,0.05681610107421875,0,-0.5892562866210938,0,0.3821792602539062,0,0.232147216796875,0,0,-0.7420578002929688,0.3734207153320312,0.37860107421875,0.01474761962890625,0,0,-0.5195465087890625,0,0.384185791015625,0.1596298217773438,0,0,-0.6496658325195312,0,0.38323974609375,0,0.29034423828125,0,-0.7568511962890625,0,0.3700790405273438,0,0.382720947265625,0,0.0275421142578125,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-0.770111083984375,0,0,0.3987274169921875,0,0.3640823364257812,0,0.383026123046875,0,0.347442626953125,0,0.3034133911132812,0,0.3033828735351562,0.304473876953125,0,0.2992324829101562,0,0.3008880615234375,0,0.3029251098632812,0.0698089599609375,0,0,0,-3.004356384277344,0,0.3778457641601562,0,0.3795700073242188,0.3780899047851562,0,0.37908935546875,0.3777923583984375,0.37481689453125,0,0.3747482299804688,0,0.3713760375976562,0.0845184326171875,0,0,-2.981254577636719,0,0.3719100952148438,0.3791427612304688,0,0.373748779296875,0,0.3739395141601562,0.3736114501953125,0,0.3760910034179688,0.3784332275390625,0.368499755859375,0,0.0777587890625,0,0,-2.936805725097656,0,0.3662033081054688,0,0.3883514404296875,0,0.3751678466796875,0,0,0.3705978393554688,0,0.3751754760742188,0,0.3773117065429688,0,0.3751296997070312,0,0.36639404296875,0,0.03298187255859375,0,0,-2.8116455078125,0.364990234375,0,0.3809585571289062,0.3749465942382812,0,0,0.3758468627929688,0.3760452270507812,0,0.3768157958984375,0.3798370361328125,0,0.2711639404296875,0,0,-3.0224609375,0.3810577392578125,0,0.38238525390625,0,0.37762451171875,0,0.3716583251953125,0,0.3718719482421875,0.3730621337890625,0.3737030029296875,0,0.3692550659179688,0.1094436645507812,0,0,-2.798095703125,0,0.370208740234375,0,0.3809738159179688,0,0.3774490356445312,0,0.37359619140625,0,0.3720245361328125,0,0,0.3741378784179688,0,0.3717727661132812,0.2640914916992188,0,-2.940650939941406,0.373870849609375,0.3918609619140625,0,0,0.375213623046875,0,0.3679046630859375,0,0.3729095458984375,0,0.3755569458007812,0,0.3758087158203125,0.3664093017578125,0,0.02582550048828125,0,0,-2.639801025390625,0,0.3743133544921875,0,0,0.3774948120117188,0.3659896850585938,0,0.3734664916992188,0.3744583129882812,0,0.372650146484375,0.375030517578125,0,0.109832763671875,0,0,-2.674140930175781,0.3732681274414062,0,0.3767471313476562,0,0,0.3712921142578125,0,0.3683853149414062,0.3671951293945312,0,0.368896484375,0,0.3718109130859375,0,0.1586227416992188,0,0,-2.677833557128906,0,0.3745193481445312,0,0.3828353881835938,0.3750152587890625,0,0.368896484375,0.3749618530273438,0,0.3730392456054688,0,0.3718795776367188,0,0.1373519897460938,0,0,-2.611442565917969,0,0.3719711303710938,0,0.381103515625,0.3701858520507812,0.37335205078125,0,0.3720169067382812,0,0.3748092651367188,0,0.3707656860351562,0.076690673828125,0,0,-2.514167785644531,0,0.3806533813476562,0.3770675659179688,0,0.3714599609375,0,0.3734130859375,0,0.3748016357421875,0.3768157958984375,0.3380889892578125,0,0,0,0,0,-2.364349365234375,0.380950927734375,0.3647689819335938,0,0,0.3626861572265625,0,0.3712005615234375,0.3749237060546875,0,0.375518798828125,0,0.2111434936523438,0,0,-2.5894775390625,0,0.3731307983398438,0.3785018920898438,0.3690261840820312,0.3690109252929688,0,0.374267578125,0,0.3716506958007812,0,0,0.3686904907226562,0,0.06087493896484375,0,0,-2.400062561035156,0,0.37640380859375,0,0.3747940063476562,0,0.3697509765625,0,0.3730392456054688,0,0.377471923828125,0,0.3777999877929688,0,0.2251815795898438,0,-2.498817443847656,0,0.3638992309570312,0,0.36627197265625,0.3656234741210938,0.3655853271484375,0.3711013793945312,0,0.3739013671875,0,0.3604507446289062,0,0.00524139404296875,0,-2.284492492675781,0.364990234375,0,0.3708267211914062,0,0.367645263671875,0,0.3659286499023438,0.3719482421875,0.372833251953125,0,0.1423110961914062,0,0,-2.350997924804688,0.3674468994140625,0.3692703247070312,0.3721542358398438,0,0.3676071166992188,0,0,0.3709869384765625,0,0.3751373291015625,0,0.1992645263671875,0,-2.368255615234375,0,0.3624267578125,0.3671493530273438,0.372711181640625,0,0.3718948364257812,0,0.361968994140625,0,0,0.3751602172851562,0,0.226715087890625,0,0,-2.365303039550781,0,0.3610992431640625,0.3625869750976562,0,0.3745880126953125,0.3586959838867188,0,0,0.3707809448242188,0,0.3739776611328125,0,0.232147216796875,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2.361396789550781,0,0,0.248443603515625,0,0.3593521118164062,0.3583450317382812,0,0.36358642578125,0,0.3624038696289062,0.3615875244140625,0,0.3692169189453125,0,0.00562286376953125,0,0,0,-2.060554504394531,0,0.3557281494140625,0,0.3692245483398438,0.3680953979492188,0,0,0.371002197265625,0.3673782348632812,0.2955322265625,0,0,0,0,0,-1.939140319824219,0,0.3574600219726562,0,0.3698883056640625,0,0.3694000244140625,0,0,0.3725128173828125,0.375885009765625,0,0.159332275390625,0,0,-2.137588500976562,0.3533706665039062,0,0.3665313720703125,0,0.3670501708984375,0.3742294311523438,0.369903564453125,0.3707656860351562,0,0,0,0,0,-1.949691772460938,0,0.3588333129882812,0,0.3741226196289062,0,0.3688278198242188,0,0.372711181640625,0.3740158081054688,0.1644210815429688,0,-2.07440185546875,0,0.3536453247070312,0.3707351684570312,0,0.3665237426757812,0,0.3699188232421875,0,0.3706436157226562,0,0.3051681518554688,0,0,0,-1.818893432617188,0,0.3630523681640625,0,0.3704147338867188,0.3611297607421875,0,0.3688507080078125,0,0.372222900390625,0,0.0444793701171875,0,-1.911209106445312,0.3503875732421875,0,0.368988037109375,0,0.3725357055664062,0,0.3718643188476562,0,0.3776092529296875,0,0.130035400390625,0,0,-1.97900390625,0,0.3458404541015625,0,0.3588638305664062,0,0.3658523559570312,0,0.366943359375,0,0.3714752197265625,0,0.2293472290039062,0,0,-2.014137268066406,0,0.3504257202148438,0,0,0.3660049438476562,0,0.3690643310546875,0,0.3695144653320312,0,0.3729248046875,0,0,0.2444686889648438,0,-1.99566650390625,0,0.3487167358398438,0.3693084716796875,0.3699722290039062,0.37213134765625,0,0.3737640380859375,0,0.2191696166992188,0,0,-1.923484802246094,0.3570022583007812,0,0.3727264404296875,0,0.3708267211914062,0,0.3772506713867188,0,0,0.3758773803710938,0,0.1261978149414062,0,-1.807281494140625,0,0.355987548828125,0,0.3712921142578125,0,0.3655548095703125,0,0.3709335327148438,0,0.3715362548828125,0.02752685546875,0,0,-1.696891784667969,0.3575668334960938,0,0.376556396484375,0,0.3696136474609375,0,0.3704071044921875,0,0.27740478515625,0,0,0,0,0,-1.548713684082031,0.3682098388671875,0,0.3704376220703125,0,0,0.37042236328125,0,0.3745193481445312,0.1188201904296875,0,-1.712715148925781,0.3448104858398438,0.365447998046875,0.3622512817382812,0.3646469116210938,0.328460693359375,0,0,0,0,0,-1.549324035644531,0.3584976196289062,0,0.3732757568359375,0,0.3676528930664062,0.3649215698242188,0,0.1370468139648438,0,0,-1.692909240722656,0,0.3509521484375,0,0,0.369659423828125,0.3648605346679688,0,0.3671188354492188,0,0,0.2914581298828125,0,0,0,0,0,-1.438522338867188,0.3675765991210938,0.3694992065429688,0,0.361480712890625,0,0.37005615234375,0,0.02027130126953125,0,-1.529380798339844,0.3584976196289062,0,0.3700103759765625,0.3662796020507812,0,0.3654937744140625,0,0.1186599731445312,0,-1.589553833007812,0,0.3562240600585938,0,0.3740692138671875,0,0.3685531616210938,0,0.372222900390625,0.1672592163085938,0,0,0,0,0,0,0,0,0,-1.509979248046875,0.3642501831054688,0,0,0.3730316162109375,0,0.3676910400390625,0.36920166015625,0.08368682861328125,0,0,-1.497085571289062,0.3573379516601562,0.3731689453125,0,0.3622055053710938,0,0,0.3725128173828125,0,0.07915496826171875,0,0,-1.481925964355469,0.3588180541992188,0,0,0.3681259155273438,0,0.370452880859375,0,0.371795654296875,0,0.05915069580078125,0,0,-1.445281982421875,0,0.358123779296875,0,0.3701248168945312,0.3708877563476562,0,0.368011474609375,0,0,0.02384185791015625,0,0,-1.382781982421875,0,0.3626861572265625,0,0.3755340576171875,0,0.3725738525390625,0,0.316925048828125,0,0,0,-1.274055480957031,0.3683090209960938,0,0.3709564208984375,0,0.3697433471679688,0.2093124389648438,0,0,0,-1.491371154785156,0,0.3591461181640625,0,0.3763961791992188,0,0.3674468994140625,0,0.3719558715820312,0.05991363525390625,0,0,0,-1.320404052734375,0.361480712890625,0,0.3745346069335938,0.3686676025390625,0,0.2585906982421875,0,0,0,-1.15240478515625,0,0.3714218139648438,0,0.3715057373046875,0,0.3693923950195312,0,0.0821380615234375,0,0,-1.304374694824219,0.3621139526367188,0.3748855590820312,0.36810302734375,0,0.2407684326171875,0,0,-1.423271179199219,0.3485031127929688,0.3772659301757812,0.3719635009765625,0,0.3663711547851562,0,0,0,-1.177932739257812,0.3696212768554688,0,0.3723068237304688,0,0.3710098266601562,0.1050567626953125,0,0,-1.262046813964844,0,0.3648605346679688,0,0.3681564331054688,0.3700103759765625,0,0.1985092163085938,0,0,-1.327690124511719,0,0.3588409423828125,0.3807830810546875,0,0.373779296875,0,0.2531661987304688,0,0,0,-1.037101745605469,0.3692550659179688,0,0.366607666015625,0,0,0.3393936157226562,0,0,0,0,0,-1.080177307128906,0,0.3709869384765625,0,0.3714752197265625,0,0.363372802734375,0,0.0119781494140625,0,0,-1.100364685058594,0,0.3693695068359375,0,0.3718338012695312,0,0.3601455688476562,0.03597259521484375,0,-1.101463317871094,0,0.3683242797851562,0,0.3753433227539062,0.3691024780273438,0.02507781982421875,0,0,0,0,0,0,0,0,-1.179267883300781,0.3635177612304688,0.3776931762695312,0,0.3573989868164062,0,0,0.1162109375,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.232429504394531,0,0.0434722900390625,0,0,0.3966217041015625,0.3770294189453125,0,0.3345260620117188,0.3604202270507812,0,0.36492919921875,0,0.3543548583984375,0.3028182983398438,0,0.2978363037109375,0,0.303009033203125,0,0,0.2996826171875,0,0.30078125,0,0.3008804321289062,0.3030929565429688,0,0.302032470703125,0,0.300445556640625,0.3026275634765625,0.1175765991210938,0,0,0,0,0,-4.749732971191406,0.3841552734375,0,0.3484878540039062,0,0.3758544921875,0,0.3776092529296875,0.3777999877929688,0.3732757568359375,0,0.3734054565429688,0,0.375,0,0.3734664916992188,0.3688201904296875,0,0.375457763671875,0,0.3747100830078125,0.3608856201171875,0.05739593505859375,0,0,-4.954658508300781,0.3958282470703125,0.3650588989257812,0,0,0.3652191162109375,0.3674392700195312,0.3668670654296875,0,0.3746719360351562,0,0.37371826171875,0,0.3746414184570312,0,0.373077392578125,0,0.3755035400390625,0.3714828491210938,0.375885009765625,0,0.3675003051757812,0.252105712890625,0,0,0,0,0,-4.717071533203125,0,0.3857574462890625,0,0.3514862060546875,0.3742218017578125,0,0.371307373046875,0,0.3697280883789062,0.369903564453125,0,0.3730621337890625,0,0.3736114501953125,0,0.3725128173828125,0.36822509765625,0.3668594360351562,0,0.3680038452148438,0,0.3490447998046875,0.06526947021484375,0,0,0,0,0,0,0,0,-4.88470458984375,0,0,0.3205337524414062,0,0.34710693359375,0,0.3279647827148438,0,0.3669052124023438,0.3643112182617188,0,0.363983154296875,0.3628692626953125,0,0.3640899658203125,0,0.3626937866210938,0,0.3646316528320312,0,0.3657073974609375,0,0.3688278198242188,0,0.3603057861328125,0,0.3649368286132812,0.01949310302734375,0,0,-4.721939086914062,0,0.3934249877929688,0,0.3502883911132812,0.3693313598632812,0,0.3697738647460938,0.368255615234375,0,0.3703231811523438,0,0.3689727783203125,0,0.37060546875,0,0.3719940185546875,0,0.3709564208984375,0,0.3722000122070312,0,0.3755035400390625,0,0.372833251953125,0.03485870361328125,0,0,-4.652275085449219,0,0.3848190307617188,0,0.3562698364257812,0,0.3674163818359375,0,0.369598388671875,0,0.3653106689453125,0,0,0.3685302734375,0.3714828491210938,0.36651611328125,0,0.3725433349609375,0,0,0.370758056640625,0,0.372406005859375,0,0.3744659423828125,0,0.347412109375,0,0,0,0,0,-4.506729125976562,0.3696517944335938,0.362884521484375,0,0.3687362670898438,0,0.3663482666015625,0,0.3685073852539062,0,0.3707733154296875,0,0.3723602294921875,0,0.3731231689453125,0.3720016479492188,0.371368408203125,0.372467041015625,0,0.3717880249023438,0,0.1996917724609375,0,0,0,0,0,-4.283180236816406,0,0,0.3549880981445312,0,0,0.3712997436523438,0,0.3634262084960938,0,0.3640823364257812,0,0.3664169311523438,0,0,0.3688278198242188,0.3662872314453125,0.3696746826171875,0,0.3677978515625,0,0.3731155395507812,0.3644180297851562,0,0.3587112426757812,0,0.02504730224609375,0,0,-4.428138732910156,0,0,0.3683624267578125,0.3666763305664062,0.365936279296875,0.3637161254882812,0,0,0.3636016845703125,0,0.365478515625,0,0.36676025390625,0,0.3719940185546875,0.3618316650390625,0.3694000244140625,0,0,0.3732147216796875,0,0.3648834228515625,0.1550521850585938,0,0,0,-4.140838623046875,0,0.3598556518554688,0.364227294921875,0.361907958984375,0.3594436645507812,0,0.3630905151367188,0.364593505859375,0,0,0.3655166625976562,0,0.366058349609375,0,0.3677749633789062,0,0.36920166015625,0,0.368499755859375,0,0.2573089599609375,0,0,0,-4.160301208496094,0,0.3600616455078125,0,0.3690414428710938,0,0.36041259765625,0,0.3636016845703125,0,0.3644485473632812,0,0.3685684204101562,0,0.3687973022460938,0,0.370941162109375,0,0.3723602294921875,0,0.3734130859375,0,0.3678131103515625,0,0.24554443359375,0,0,0,-4.079917907714844,0.36151123046875,0.3657608032226562,0,0.3607330322265625,0,0,0.362335205078125,0,0.3669891357421875,0.36370849609375,0,0.3682022094726562,0.371307373046875,0.372589111328125,0.3745574951171875,0,0.3653030395507812,0.1695404052734375,0,0,0,0,0,0,0,-3.948638916015625,0,0,0.3699111938476562,0,0.3683090209960938,0,0.3585052490234375,0,0.3619384765625,0.3638076782226562,0.3700790405273438,0,0.37225341796875,0.3686294555664062,0,0,0.369354248046875,0.3716812133789062,0,0,0.3611373901367188,0,0.0336761474609375,0,0,-4.107170104980469,0,0.3693389892578125,0,0.3723373413085938,0,0.3576583862304688,0,0,0.358184814453125,0.3631744384765625,0,0.3660507202148438,0,0,0.3677749633789062,0,0.3732528686523438,0,0.3701019287109375,0,0.3728866577148438,0,0.369232177734375,0.1858291625976562,0,0,0,-3.832481384277344,0,0.3690261840820312,0,0.358642578125,0,0.3569717407226562,0.361602783203125,0,0.367828369140625,0,0.3721389770507812,0.3717193603515625,0,0.370086669921875,0.3694992065429688,0,0.3686141967773438,0.2831497192382812,0,0,0,0,0,-3.87677001953125,0,0.3623809814453125,0,0.3582839965820312,0,0.3518295288085938,0,0.3581619262695312,0,0.3628692626953125,0,0.3641586303710938,0,0.3651351928710938,0,0.3702392578125,0,0.3725357055664062,0,0.3676834106445312,0,0.3563461303710938,0,0.0020904541015625,0,-3.903129577636719,0,0.36572265625,0,0.3574142456054688,0,0.3500595092773438,0,0.3581466674804688,0,0.36358642578125,0,0.3687973022460938,0.3675155639648438,0,0.3699569702148438,0.374420166015625,0,0,0.3709335327148438,0,0.3534469604492188,0,0,0.01612091064453125,0,0,-3.834693908691406,0,0.3592605590820312,0.3561935424804688,0,0.3502197265625,0,0.3596572875976562,0.3648757934570312,0,0.3687362670898438,0.3687973022460938,0,0,0.3706283569335938,0,0.3685302734375,0.3738784790039062,0,0.3051605224609375,0,0,0,0,0,-3.764198303222656,0,0.3582305908203125,0.3538436889648438,0.3462142944335938,0,0.3333511352539062,0.34405517578125,0,0.36077880859375,0,0.3656234741210938,0,0.3689193725585938,0.368255615234375,0,0.3695755004882812,0,0,0.3047943115234375,0,0,0,0,0,-3.677330017089844,0.3544845581054688,0,0.3480224609375,0.3505477905273438,0,0,0.3607559204101562,0,0.3636398315429688,0,0.3665695190429688,0,0.3664093017578125,0.2998428344726562,0,0,0.2811126708984375,0,0.3650360107421875,0,0.32855224609375,0,0,0,-3.653488159179688,0,0.3546371459960938,0,0.34674072265625,0,0.3455123901367188,0,0.3568038940429688,0.3633956909179688,0,0.3607177734375,0,0.3644866943359375,0,0,0.36724853515625,0.3716812133789062,0,0,0.3660354614257812,0,0.1621475219726562,0,0,0,0,0,-3.418708801269531,0.3494949340820312,0,0.351837158203125,0,0,0.3572616577148438,0,0.36181640625,0.368865966796875,0,0.3690109252929688,0,0.3709716796875,0,0.372650146484375,0.3699493408203125,0,0.2511215209960938,0,0,0,0,0,-3.424201965332031,0,0.35223388671875,0,0.3481063842773438,0,0.354339599609375,0,0.3584518432617188,0,0.36444091796875,0,0.3682174682617188,0.36248779296875,0,0.3695449829101562,0,0.3711776733398438,0,0.2777252197265625,0,0,0,0,0,-3.40838623046875,0,0,0.3516693115234375,0,0.3448333740234375,0,0.3495635986328125,0.3603515625,0,0.3634109497070312,0.3701705932617188,0.3715667724609375,0.3703231811523438,0.3714599609375,0,0.2558670043945312,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-3.432594299316406,0.3559341430664062,0.3510589599609375,0,0.3531875610351562,0.3638076782226562,0,0.3620758056640625,0.3679046630859375,0.3665924072265625,0,0,0.3695526123046875,0,0.3727264404296875,0,0,0.2688064575195312,0,0,0,0,0,-3.314285278320312,0,0.346771240234375,0,0.34478759765625,0,0,0.3514556884765625,0,0.3632965087890625,0,0.3617935180664062,0,0,0.3683395385742188,0,0.3355026245117188,0,0,0.3675460815429688,0.363525390625,0.2089385986328125,0,0,0,0,0,-3.173980712890625,0,0.34765625,0.3518218994140625,0,0.3572235107421875,0,0.3613052368164062,0,0,0.36865234375,0.3722152709960938,0,0,0.3739471435546875,0,0,0.372161865234375,0,0.3587265014648438,0.006317138671875,0,-3.278244018554688,0,0.349517822265625,0,0.34674072265625,0.35101318359375,0,0.358642578125,0,0.3628768920898438,0,0,0.3681259155273438,0,0.3713760375976562,0.3695449829101562,0,0.3645782470703125,0.13043212890625,0,0,0,0,0,-2.990280151367188,0,0,0.3461456298828125,0.353302001953125,0,0,0.361480712890625,0,0,0.362701416015625,0,0.3669815063476562,0.3682479858398438,0,0.3680496215820312,0.367034912109375,0,0.1893463134765625,0,0,0,0,0,-2.999603271484375,0,0.3458251953125,0,0.3549728393554688,0,0.360626220703125,0,0.3672637939453125,0,0.3665847778320312,0,0.369171142578125,0,0.3735885620117188,0.3708114624023438,0,0,0.1823043823242188,0,0,0,0,0,-2.9412841796875,0,0.3489456176757812,0.3525848388671875,0,0.362548828125,0,0.3651504516601562,0.3678741455078125,0.3688278198242188,0,0.3731842041015625,0,0.3655166625976562,0.1266937255859375,0,0,0,-2.850715637207031,0,0,0.3488311767578125,0,0.35467529296875,0,0.3609237670898438,0,0.3616485595703125,0,0.3660430908203125,0,0.3654022216796875,0.3622817993164062,0.3615188598632812,0,0.05794525146484375,0,0,0,-2.760368347167969,0.3477783203125,0.356536865234375,0,0.3600540161132812,0,0,0.36468505859375,0.364593505859375,0,0,0.367279052734375,0,0,0.3730316162109375,0.3136367797851562,0,0,0,0,0,-2.954994201660156,0,0.3514785766601562,0.353057861328125,0,0.3593902587890625,0,0.3632431030273438,0,0,0.3623580932617188,0,0.3685379028320312,0,0.3722000122070312,0.3665084838867188,0,0.143951416015625,0,0,0,-2.724586486816406,0,0.3498611450195312,0,0,0.3511734008789062,0.35125732421875,0,0,0.3588409423828125,0,0.3630599975585938,0,0.3667526245117188,0,0,0.36761474609375,0,0.3004150390625,0,0,0,0,0,-2.851844787597656,0,0.3472976684570312,0.3518295288085938,0.358428955078125,0.3606185913085938,0,0.3630828857421875,0,7.661201477050781,0,0,0,0,0,0,0,0,0,7.62939453125,0,3.0517578125e-05,0,0,0,0,0,0,0,0,0,0,0,0,0,15.2587890625,0,0,0,0,0,0,0,0,0,22.88850402832031,0],"filename":[null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null]},"interval":10,"files":[],"prof_output":"/tmp/Rtmpakqreo/file453863389e5d.prof","highlight":{"output":["^output\\$"],"gc":["^<GC>$"],"stacktrace":["^\\.\\.stacktraceo(n|ff)\\.\\.$"]},"split":"h"}},"evals":[],"jsHooks":[]}</script>
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



