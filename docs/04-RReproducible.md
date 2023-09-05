# (PART) Introduction to Reproducible R {-} 

# Why be reproducible 
***

Before hopping into reproducible programming, lets think about why. My main sell to you is that it is in your own self-interest.  

## An example workflow

Taking First Steps ...

**Step 1: Some Ideas and Data**

$X_{1} \to Y_{1}$

* You copy some data into a spreadsheet
* do some calculations and tables the same spreadsheet
* some other analysis from here and there, using this software and that.

**Step 2: Persuing the lead for a week or two**

* you beef up the data you got
* add some other types of data 
* copy in a spreadsheet data, manually aggregate
* do some more calculations and tables, same as before




Then, a Little Way Down the Road ...

**1 month later, someone asks about another factor:** $X_{2}$

* You repeat **Step 2** with some data on $X_{2}$.
* The details from your "point and click" method are a bit fuzzy.

It takes a little time, but you successfully redo the analysis.


**4 months later, someone asks about another factor:** $X_{3}\to Y_{1}$

* You again repeat **Step 2** with some data on $X_{3}$.
* You're pretty sure
  * it's the latest version of the spreadsheet.
  * none of tables your tried messed up the order of the rows or columns.

It takes more time -- the data processing was not transparent.



**6 months later, you want to explore:** $X_{2} \to Y_{2}$.

* You found out Excel had some bugs in it's statistical calculations (see e.g., https://biostat.app.vumc.org/wiki/pub/Main/TheresaScott/StatsInExcel.TAScot.handout.pdf).




**2 years later, you want to replicate:** $\{ X_{1}, X_{2}, X_{3} \} \to Y_{1}$


* A rival has proposed an alternative theory. Their idea doesn't actually make any sense, but their visuals are better and statistics are more sophisticated.
* You don't even have that computer anymore.
* A collaborator who handled the data on $X_{2}$ has moved on.



## An alternative workflow

Suppose you decided to code what you did beginning with Step 2.

**It doesn't take much time to update or replicate your results.**

* Your computer runs for 2 hours and reproduces the figures and tables.
(You wrote your big calculations to use multiple cores and this saved 6 hours--each time.)
* You decided to add some more data, and it adds almost no time.
* You see the exact steps you took and found an error
(glad you found it before publication!)


**Your results are transparent and easier to build on.**

* You easily see that not much has changed with the new data.
* You try out a new plot you found in *The Visual Display of Quantitative Information*, by Edward Tufte.
  * It's not a standard plot, but google answers most of your questions.
  * Tutorials help avoid bad practices, such as plotting 2D data as a 3D object (see e.g., https://clauswilke.com/dataviz/no-3d.html).
* You try out an obscure statistical approach that's hot in your field.
  * it doesn't make the paper, but you have some confidence that candidate issue isn't a big problem



## R and R-Markdown

R is good for complex stats, concise figures, and coherent organization.

* Built and developed by applied statisticians for statistics.
* Used by many in academia and industry.


R Markdown is good for reproducible research 

* http://www.r-bloggers.com/the-reproducibility-crisis-in-science-and-prospects-for-r/
* http://fmwww.bc.edu/GStat/docs/pointclick.html
* https://github.com/qinwf/awesome-R\#reproducible-research
* A Guide to Reproducible Code in Ecology and Evolution
* https://biostat.app.vumc.org/wiki/pub/Main/TheresaScott/ReproducibleResearch.TAScott.handout.pdf

Note that R and R markdown are both languages: R studio interprets R code to produce statistics, R studio interprets R markdown code to produce pretty documents which contain both writing and statistics. (You should already be a bit familiar with R, but not necessarily R Markdown.) Altogether, your project will use

* R is our software
* Rstudio is our GUI
* R Markdown is our document



Both are good for teaching

* https://doi.org/10.1080/00220485.2019.1618765
* https://doi.org/10.1002/jae.657

Both are good for getting a job

* As a student, think about labour demand. R skills, unlike other purely academic software, is something future employers use and want. Do more of your own research on this to understand how much to invest.





https://kbroman.org/steps2rr/pages/organize.html


## Types of Projects

Homework reports are the smallest and probably first document you create. We will create little homework reports using R markdown that are almost entirely self-contained (showing both code and output). To do this, you will need to install [Pandoc](http://pandoc.org) on your computer.

Posters and presentations are another important type of scientific document. R markdown is good at creating both of these, and actually *very* good with some additional packages. So we will also use [flexdashboard](https://pkgs.rstudio.com/flexdashboard/) for posters and [beamer]( https://bookdown.org/yihui/rmarkdown/beamer-presentation.html) for presentions. Since beamer is a pdf output, you will need to install [TinyTex](https://yihui.org/tinytex/), which can be done within R

```r
install.packages('tinytex')
tinytex::install_tinytex()  # install TinyTeX
```

Install any required packages

```r
## Packages for Rmarkdown
install.packages("knitr")
install.packages("rmarkdown")
install.packages("bookdown")

## Other packages used in this primer
install.packages("plotly")
install.packages("sf")
```

To get started with R Markdown, you can first read and work through https://jadamso.github.io/Rbooks/small-scale-projects.html, and then recreate https://jadamso.github.io/Rbooks/small-scale-projects.html#a-homework-example yourself.


# Small Scale Projects
***

## An R Code Chunk

Save the following code as `CodeChunk.R`

```r
sum_squared <- function(x1, x2) {
	y <- (x1 + x2)^2
	return(y)
} 

x <- c(0,1,3,10,6)
sum_squared(x[1], x[3])
sum_squared(x, x[2])
sum_squared(x, x[7])
sum_squared(x, x) 
```

**Clean the workspace** In the right panels, manually cleanup

* save the code as *MyFirstCode.R*
* clear the environment and history (use the broom in top right panel)
* clear unsaved plots (use the broom in bottom right panel)

    
**Replicate** using the grahical user interface (GUI) while in Rstudio either using a "point-click" or "console" method

*GUI: point-click*
click 'Source > Source as a local job' on top right

*GUI: console*
into the console on the bottom left, enter

```r
source('MyFirstCode.R')
```


**CLI Alternatives** *(Skippable)* There are also alternative ways to replicate via the command line interface (CLI) after opening a terminal
 
*CLI: console*

```bash
Rscript -e "source('CodeChunk.R')"
```

*CLI: direct*


```bash
Rscript CodeChunk.R
```

Note that you can open a new terminal in RStudio in the top bar by
clicking 'tools > terminal > new terminal'



## An R Markdown Document

### Copy/Paste Example
<!-- 
**Clean workspace**
Delete any temporary files which you do not want (or start a fresh session).

(for example *summarytable_example.txt* and *plot_example.pdf* and section *Data analysis examples: custom figures*)
-->



**Download** 

See [DataScientism.html](https://jadamso.github.io/Rbooks/DataScientism.html)

Download source file from [DataScientism.Rmd](https://jadamso.github.io/Rbooks/DataScientism.Rmd)


**Replicate**

You can now create the primers by opening the Rstudio GUI and then point-and-click.

Alternatively, you can use the console to run

```r
rmarkdown::render('DataScientism.Rmd')
```

### A Homework Example {.tabset}
Below is a template of what homework questions (and answers) look like. Create an .Rmd from scratch that produces a similar looking .html file.

**Question 1**
Simulate 100 random observations of the form $y=x\beta+\epsilon$ and plot the relationship. Plot and explore the data interactively via plotly, https://plotly.com/r/line-and-scatter/. Then play around with different styles, https://www.r-graph-gallery.com/13-scatter-plot.html, to best express your point.

*Answer*
I simulate $400$ observations for $\epsilon \sim 2\times N(0,1)$ and $\beta=4$, as seen in this single chunk. Notice an upward trend.

```r
n <- 100
E <- rnorm(n)
X <- seq(n)
Y <- 4*X + 2*E

library(plotly)
plot_ly( data=data.frame(X=X,Y=Y), x=~X, y=~Y)
```

```{=html}
<div class="plotly html-widget html-fill-item-overflow-hidden html-fill-item" id="htmlwidget-4ccab6c877c391e9f9eb" style="width:672px;height:480px;"></div>
<script type="application/json" data-for="htmlwidget-4ccab6c877c391e9f9eb">{"x":{"visdat":{"be1d6059bc3b":["function () ","plotlyVisDat"]},"cur_data":"be1d6059bc3b","attrs":{"be1d6059bc3b":{"x":{},"y":{},"alpha_stroke":1,"sizes":[10,100],"spans":[1,20]}},"layout":{"margin":{"b":40,"l":60,"t":25,"r":10},"xaxis":{"domain":[0,1],"automargin":true,"title":"X"},"yaxis":{"domain":[0,1],"automargin":true,"title":"Y"},"hovermode":"closest","showlegend":false},"source":"A","config":{"modeBarButtonsToAdd":["hoverclosest","hovercompare"],"showSendToCloud":false},"data":[{"x":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100],"y":[7.5187201667309118,5.1675358951225183,12.901802595533892,17.632068431271275,16.714888307641559,25.01734730141008,26.176340451067325,32.349200310970154,34.90913623719873,41.514968943334559,44.561641721903953,48.281101931546289,52.072405641770203,56.714064482312736,62.15468783868571,63.318462152675409,69.333445461416687,73.26363807043947,75.84485437106035,79.540574590354595,84.755955124827707,89.433432660305613,91.444387796853661,96.523369533940354,96.439956089200138,100.95787880466209,107.97411602099727,114.97574094971719,115.37124665207735,120.5694357587481,124.62104922916015,126.60630466698792,135.08586960921062,139.05037565676216,142.80719919135569,147.36427761619237,150.13611563977867,152.84976141017569,152.5992712906141,160.39420928605068,163.28866201119473,168.13368001846754,171.91494943910513,175.70949162720132,178.33212247183025,184.20298142709467,187.92551995308736,190.56051284215044,194.25232303314681,201.01602719777966,206.56614079307118,206.8272257953395,215.08091122739171,216.43570253950327,219.13571904467457,224.90125636105512,230.28708816555636,230.87776377437473,237.90836959057634,243.13270250277148,244.97230889619743,248.61585257323071,254.63198215232526,254.20145345614335,256.29230814114004,267.55220728987484,268.32700102335605,273.65182443401613,277.78981720584864,278.93769573543273,285.27183308667276,287.54785819591478,291.70102336036268,292.58448580037322,297.06634219722957,298.98824008984008,310.06861916623797,312.36359684497853,317.71049885740052,322.24898430086915,323.12147750955529,330.62455617155308,333.94245485277452,333.91229013455359,337.66143648723579,343.60455873643019,350.77185178997053,354.06803564044816,353.71090601240633,361.74423236548091,361.80079157590092,366.179077474895,372.76926894825317,379.57997141175179,378.46124217627488,385.07841863648861,390.04606369860801,391.06834666940756,395.02540158501199,398.60444295501435],"type":"scatter","mode":"markers","marker":{"color":"rgba(31,119,180,1)","line":{"color":"rgba(31,119,180,1)"}},"error_y":{"color":"rgba(31,119,180,1)"},"error_x":{"color":"rgba(31,119,180,1)"},"line":{"color":"rgba(31,119,180,1)"},"xaxis":"x","yaxis":"y","frame":null}],"highlight":{"on":"plotly_click","persistent":false,"dynamic":false,"selectize":false,"opacityDim":0.20000000000000001,"selected":{"opacity":1},"debounce":0},"shinyEvents":["plotly_hover","plotly_click","plotly_selected","plotly_relayout","plotly_brushed","plotly_brushing","plotly_clickannotation","plotly_doubleclick","plotly_deselect","plotly_afterplot","plotly_sunburstclick"],"base_url":"https://plot.ly"},"evals":[],"jsHooks":[]}</script>
```

**Question 2**
Verify the definition of a line segment for points $A=(0,3), B=(1,5)$ using a $101 \times 101$ grid. Recall a line segment is all points $s$ that have $d(s, A) + d(s, B) = d(A, B)$.

*Answer* 

```r
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
points(D_point_seg)
box()
```

<img src="04-RReproducible_files/figure-html/answer2-1.png" width="672" />

## Posters and Slides

See

* [DataScientism_Slides.pdf](https://jadamso.github.io/Rbooks/DataScientism_Slides.pdf)
* [DataScientism_Poster.html](https://jadamso.github.io/Rbooks/DataScientism_Poster.html)

And download source files

* [DataScientism_Slides.Rmd](https://jadamso.github.io/Rbooks/DataScientism_Slides.Rmd)
* [DataScientism_Poster.Rmd](https://jadamso.github.io/Rbooks/DataScientism_Poster.Rmd)

Simply change the name to your own, and compile the document. If you have not installed *Latex*, then you must do that or specify a different output in order to compile `DataScientism_Slides`. For example, simply change `output: beamer_presentation` to `output: ioslides_presentation` on line 6.

## Getting help w/ R Markdown

For more guidance on how to create Rmarkdown documents, see

* https://github.com/rstudio/cheatsheets/blob/main/rmarkdown.pdf
* https://cran.r-project.org/web/packages/rmarkdown/vignettes/rmarkdown.html
* http://rmarkdown.rstudio.com
* https://bookdown.org/yihui/rmarkdown/
* https://bookdown.org/yihui/rmarkdown-cookbook/
* https://dept.stat.lsa.umich.edu/~jerrick/courses/stat701/notes/rmarkdown.html
* An Introduction to the Advanced Theory and Practice of Nonparametric Econometrics. Raccine 2019. Appendices B \& D.
* https://rmd4sci.njtierney.com/using-rmarkdown.html

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




# Medium Scale Projects
***

As you scale up to a medium sized project, however, you will have to be more organized.

Medium sized projects should have their own `Project` folder on your computer with files, subdirectories with files, and subsubdirectories with files. It should look like this
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



## MAKEFILE

There are two main meta-files

* `README.txt` overviews the project structure and what the codes are doing
* `MAKEFILE` explicitly describes and executes all codes. 


If all code is written with the same program, the makefile can be written in that programs code: `MAKEFILE.R`, which looks like

```r
### Project Structure
home_dir    <- path.expand("~/Desktop/Project/")

data_dir    <- paste0(home_dir, "Data/")
data_dir_r  <- paste0(data_dir, "Raw/")
data_dir_c  <- paste0(data_dir, "Clean/")

out_dir  <- paste0(hdir, "Output/")

code_dir  <- paste0(hdir, "Code/")


### Execute Codes
### libraries are loaded within each RBLOCK
set.wd( code_dir )
source( "RBLOCK_001_DataClean.R" )
source( "RBLOCK_002_Figures.R" )
source( "RBLOCK_003_ModelsTests.R" )
source( "RBLOCK_004_Robust.R" )
```


If some folders or files are not created, you can do this within R

```r
# create directory called 'Data'
dir.create('Data')

# list the files and directories
list.files(recursive=TRUE, include.dirs=TRUE)
```


## Logging/Sinking

You can then execute the makefile within R and log the output. Either by 

1. Inserting some code that logs/sinks the output 

```r
### Project Structure
home_dir    <- path.expand("~/Desktop/Project/")

data_dir    <- paste0(home_dir, "Data/")
data_dir_r  <- paste0(data_dir, "Raw/")
data_dir_c  <- paste0(data_dir, "Clean/")

out_dir  <- paste0(hdir, "Output/")

code_dir  <- paste0(hdir, "Code/")

### Log Output
set.wd( code_dir )
sink("MAKEFILE.Rout", append=TRUE, split=TRUE)

### Execute Codes
source( "RBLOCK_001_DataClean.R" )
source( "RBLOCK_002_Figures.R" )
source( "RBLOCK_003_ModelsTests.R" )
source( "RBLOCK_004_Robust.R" )

### Stop Logging Output
sink()
```

2. Starting a session that logs/sinks you sourcing the makefile

```r
sink("MAKEFILE.Rout", append=TRUE, split=TRUE)
source("MAKEFILE.R")
sink()
```

3. Execute the makefile via the commandline 

```bash
R CMD BATCH MAKEFILE.R MAKEFILE.Rout
```




## Final Step

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


# Large Scale Projects


For larger scale projects, use scripts 

* https://kbroman.org/steps2rr/pages/scripts.html
* https://kbroman.org/steps2rr/pages/automate.html

## Debugging 

We can use the following packages to help deal with various problems that may arise

```r
library(profvis)
library(bench)
library(parallel)
library(Rcpp)
library(compiler)
```

(Note that many of the examples are taken from https://adv-r.hadley.nz/).


Problems print to the console

```r
message("This is what a message looks like")
```

```
## This is what a message looks like
```

```r
warning("This is what a warning looks like")
```

```
## Warning: This is what a warning looks like
```

```r
stop("This is what an error looks like")
```

```
## Error in eval(expr, envir, enclos): This is what an error looks like
```


Nonproblems also print to the console

```r
cat('cat\n')
```

```
## cat
```

```r
print('print')
```

```
## [1] "print"
```


###  Tracing Errors

First, use garbage cleanup to "cleanup" memory leaks

```r
gc()
```

```
##           used (Mb) gc trigger (Mb) max used (Mb)
## Ncells 1209376 64.6    2357425  126  2357425  126
## Vcells 2293487 17.5    8388608   64  3534636   27
```
Then trace the error process. 

Example of error process

```r
## Let i() check if its argument is numeric
i <- function(i0) {
  if ( !is.numeric(i0) ) {
    stop("`d` must be numeric", call.=FALSE)
  }
  i0 + 10
}

## Let f() call g() call h() call i()
h <- function(i0) i(i0)
g <- function(h0) h(h0)
f <- function(g0) g(g0)

## Observe Error
f("a")
```

```
## Error: `d` must be numeric
```



Traceback debugging

```r
traceback()
```

```
## No traceback available
```



Simple print debugging

```r
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


Interactive approach

```r
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
## debug at <text>#3: h(h0)
```

```
## Error: `d` must be numeric
```




###  Checking problems 

To inspect objects

```r
is.object(f)
is.object(c(1,1))

class(f)
class(c(1,1))

## Storage Mode Type 
typeof(f)
typeof(c(1,1))

storage.mode(f)
storage.mode(c(1,1))
```


To check for valid inputs/outputs

```r
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
## Many others
```


To check for values

```r
all( x > -2 )
any( x > -2 )
## Check Matrix Rows
rowAny <- function(x) rowSums(x) > 0
rowAll <- function(x) rowSums(x) == ncol(x)
```


## Being Proactive

Supressing errors is possible but a bad idea

```r
try(1+2, silent=T)
```

```
## [1] 3
```

```r
try(warning('warning'), silent=T)
```

```
## Warning in doTryCatch(return(expr), name, parentenv, handler): warning
```

```r
try(error('error'), silent=T)
```

```r
try(1+2, silent=F)
```

```
## [1] 3
```

```r
try(warning('warning'), silent=F)
```

```
## Warning in doTryCatch(return(expr), name, parentenv, handler): warning
```

```r
try(error('error'), silent=F)
```

```
## Error in error("error") : could not find function "error"
```

Try to handle errors

```r
tryCatch(
  error = function(e) {
    # code to run when error is thrown
  },
  code_to_run_while_handlers_are_active
)
```

Simple Example

```r
tryCatch(
    expr = {
        message( log(-Inf) )
        message("Successfully executed the log(x) call.")
    },
    error = function(e){
        message('Caught an error!')
        print(e)
    },
    warning = function(w){
        message('Caught an warning!')
        print(w)
    },
    finally = {
        message('All done, quitting.')
    }
)
```

```
## Caught an warning!
```

```
## <simpleWarning in log(-Inf): NaNs produced>
```

```
## All done, quitting.
```



<!--## Ignore warnings/messages-->
<!--#suppressWarnings()-->
<!--#suppressMessages()-->

Safe Functions

```r
## Define
log_safe <- function(x){
    tryCatch(
        expr = {
            message( log(x) )
            message("Successfully executed the log(x) call.")
        },
        error = function(e){
            message('Caught an error!')
            print(e)
        },
        warning = function(w){
            message('Caught an warning!')
            print(w)
        },
        finally = {
            message('All done, quitting.')
        }
    )
}

## Test 
log_safe( 10)
```

```
## 2.30258509299405
```

```
## Successfully executed the log(x) call.
```

```
## All done, quitting.
```

```r
log_safe(-10)
```

```
## Caught an warning!
```

```
## <simpleWarning in log(x): NaNs produced>
```

```
## All done, quitting.
```

```r
log_safe(' ')
```

```
## Caught an error!
```

```
## <simpleError in log(x): non-numeric argument to mathematical function>
```

```
## All done, quitting.
```











## Optimizing 


In General: Clean code is often faster and less error prone


*Repetitive tasks can be optimized* You end up with code that

* is cleaner, faster, and more general
* can be easily parallelized


*Computers have big memories and are really good at math.*

* First try vectors
* then try `apply` functions


*Don't waste time on code that is not holding you back.*

* Your code may break, be slow, or incorrect.
* Look at what has already done.




###  Benchmarking

The simplest approach


```r
system.time({
    x <- runif(1e5)
    sqrt(x)
})
```

```
##    user  system elapsed 
##   0.004   0.000   0.004
```




For identifying bottlenecks

```r
## Generate Large Random Dataset
n <- 2e6
x <- runif(n)
y <- runif(n)
z <- runif(n)
XYZ <- cbind(x,y,z)

## Inspect 4 equivalent `row mean` calculations 
profvis::profvis({
    m <- rowSums(XYZ)/ncol(XYZ)
    m <- rowMeans(XYZ)
    m <- apply(XYZ, 1, mean)
    m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }
})
```

```{=html}
<div class="profvis html-widget html-fill-item-overflow-hidden html-fill-item" id="htmlwidget-50dc7bc37c66af3ec972" style="width:100%;height:600px;"></div>
<script type="application/json" data-for="htmlwidget-50dc7bc37c66af3ec972">{"x":{"message":{"prof":{"time":[1,2,3,4,5,6,7,8,9,9,9,10,10,11,11,12,12,13,13,14,14,15,15,16,16,17,17,18,18,19,19,20,20,21,21,22,22,23,23,24,24,25,25,25,26,27,27,28,28,29,29,30,31,31,32,32,33,34,34,34,35,36,37,38,38,39,39,40,40,40,41,41,41,42,42,42,43,44,45,45,46,46,47,47,48,48,48,49,49,50,50,51,51,51,52,52,53,54,55,55,56,56,57,58,59,60,60,61,61,62,62,63,63,64,64,65,66,67,68,69,70,71,71,72,72,72,73,73,73,74,74,75,75,76,76,77,77,78,79,80,81,82,82,83,83,84,84,84,85,85,86,86,87,87,88,88,88,89,89,90,90,91,91,92,92,93,94,94,94,95,96,96,97,97,98,98,99,100,100,101,101,102,102,102,103,104,104,105,105,106,106,107,108,109,109,110,111,112,113,113,114,114,114,115,115,116,117,118,119,119,120,120,121,121,122,122,123,123,124,124,124,125,125,126,126,127,128,128,129,129,130,130,130,131,131,132,132,133,133,134,135,135,136,136,137,138,139,139,139,140,140,140,141,141,142,142,143,144,144,145,145,146,146,146,147,147,147,148,149,149,149,149,150,151,151,152,152,153,153,154,155,156,157,157,158,159,159,159,160,160,161,161,162,162,163,163,164,164,165,165,165,166,167,168,168,169,169,170,170,171,171,172,173,173,173,174,174,175,175,176,177,178,179,179,180,181,181,182,182,183,183,184,185,186,186,186,187,187,187,188,188,189,189,190,190,190,191,192,192,192,193,193,194,194,195,196,197,197,198,198,199,199,200,200,200,201,201,202,203,203,204,204,205,206,206,206,207,207,208,208,209,209,210,210,211,211,212,212,213,214,214,215,215,216,216,216,217,218,219,220,220,221,221,222,222,223,223,223,224,224,224,225,225,225,226,226,226,227,227,227,228,228,228,229,229,229,230,230,230,231,231,231,232,232,233,233,234,234,235,235,235,236,237,237,238,238,239,240,240,240,240,241,241,242,243,243,244,245,245,246,246,247,247,248,249,249,250,250,251,251,252,252,253,253,254,255,255,255,256,256,257,258,258,259,259,260,261,261,262,262,263,264,264,265,265,266,266,267,268,269,269,270,270,271,272,272,273,274,275,275,276,276,276,277,277,278,278,279,280,280,281,282,283,283,283,284,285,285,286,287,288,289,290,290,290,291,291,292,292,293,294,294,295,295,296,296,297,297,297,298,299,299,300,300,301,302,303,303,304,304,304,305,306,306,307,307,308,308,309,309,310,310,311,311,312,312,313,313,314,315,315,316,316,316,317,318,318,318,319,319,319,320,320,321,322,322,323,324,324,325,326,327,327,328,328,328,329,330,330,331,331,332,332,333,333,333,334,334,334,335,335,336,336,337,337,338,338,339,339,340,340,341,341,341,342,342,343,343,344,345,345,345,346,346,347,347,348,349,349,350,350,351,352,352,353,353,353,354,354,355,356,356,357,357,357,358,358,359,359,360,360,360,361,361,362,362,363,364,365,365,366,366,366,367,367,368,368,369,370,371,372,372,373,373,374,374,375,375,376,377,378,379,379,379,380,380,380,381,381,381,382,382,382,383,383,383,384,384,384,385,385,385,386,386,386,387,387,387,388,388,388,389,389,389,390,390,390,391,391,391,392,392,392,393,393,393,394,394,394,395,395,395,396,396,396,397,397,397,398,398,398,399,399,399,400,400,400,401,401,401,402,402,402,403,403,403,404,404,404,405,405,405,406,406,407,407,408,408,409,409,410,410,410,411,412,413,413,414,414,415,415,415,416,416,417,417,417,418,419,419,420,420,421,421,421,422,422,423,424,424,425,426,427,427,428,428,429,430,431,431,432,432,433,433,433,434,434,435,435,435,436,436,436,437,437,438,438,438,439,439,440,440,441,441,442,442,442,443,443,444,445,446,446,447,447,448,449,449,450,450,451,452,453,453,454,455,455,455,456,457,457,458,458,459,459,460,460,461,461,462,462,463,464,464,465,465,466,466,467,467,468,468,469,469,470,471,471,471,472,472,473,473,474,474,475,475,476,477,477,478,478,479,479,480,480,481,481,482,483,483,483,484,484,485,486,486,487,488,488,489,489,490,490,491,491,491,492,493,493,494,494,495,496,496,497,497,498,498,499,499,500,500,501,501,501,502,502,503,504,504,505,505,506,506,507,507,508,509,509,510,511,512,512,513,513,514,515,515,516,516,517,517,518,518,518,519,519,520,520,521,521,522,523,524,524,525,525,526,526,526,527,527,528,528,529,529,529,530,530,531,531,531,532,532,533,533,534,534,535,535,536,536,537,538,538,539,540,541,541,542,542,543,544,544,545,545,545,546,546,547,547,548,548,549,549,550,550,550,551,551,552,553,554,554,555,555,555,556,556,557,557,558,558,559,559,560,560,560,561,561,562,562,563,563,563,564,565,565,566,566,567,567,568,568,568,569,570,570,571,571,572,572,572,573,573,573,574,575,575,576,576,577,577,578,578,579,579,579,580,580,581,581,582,583,583,584,584,584,585,585,585,586,587,587,588,589,590,590,591,592,592,592,593,593,594,595,595,596,597,597,597,598,599,599,600,600,601,601,602,602,603,603,604,604,605,606,606,607,607,608,609,609,609,609,610,610,611,612,612,613,613,614,614,615,615,616,616,617,618,618,619,620,620,621,621,621,622,622,622,623,623,623,624,624,625,626,626,627,628,628,629,629,629,630,631,631,632,633,633,633,634,634,634,635,635,636,636,637,637,638,638,639,640,640,641,642,642,643,643,644,644,645,645,646,646,647,647,648,648,649,650,651,652,653,654,654,654,655,655,656,656,657,657,658,659,659,659,660,660,661,662,663,663,664,665,665,666,666,667,667,668,668,668,669,669,670,670,670,671,671,671,672,672,673,673,674,674,675,675,676,676,677,677,678,678,679,680,681,681,681,682,682,682,683,683,683,684,684,684,685,685,685,686,686,686,687,687,687,688,688,688,689,689,689,690,690,690,691,691,691,692,692,692,693,693,693,694,694,694,695,695,696,696,697,697,698,698,699,700,701,701,702,702,703,704,705,705,706,706,706,707,707,707,708,709,709,710,711,711,712,713,713,713,714,714,715,715,716,716,717,717,717,718,718,718,719,719,719,720,720,721,721,722,723,723,724,724,725,726,726,727,728,728,729,729,730,730,731,731,732,732,733,733,734,735,736,736,737,738,738,739,739,740,740,741,741,741,742,742,743,743,744,744,745,746,747,747,748,748,749,749,750,751,751,752,752,752,753,753,753,754,754,755,755,756,756,757,758,758,758,759,759,759,760,760,761,762,763,763,763,764,764,764,765,766,766,767,767,768,768,769,769,770,771,772,773,773,774,775,775,776,776,777,777,778,778,779,779,780,780,781,781,782,782,783,784,785,786,787,787,787,788,788,788,789,789,790,790,791,791,792,792,793,793,794,794,795,795,796,796,797,797,797,798,798,798,799,800,801,801,802,802,803,803,804,804,805,806,806,807,807,808,808,808,809,809,809,810,810,810,811,812,813,813,814,815,815,816,816,816,817,818,818,819,819,820,821,822,823,823,824,824,825,825,826,826,827,827,828,828,829,829,829,829,830,830,830,830,831,831,832,832,833,833,834,835,835,836,836,837,838,838,839,839,839,840,840,840,841,842,843,844,845,845,846,846,847,847,848,848,849,849,849,850,850,850,851,851,852,852,853,853,854,855,856,857,858,859,859,860,860,860,861,862,862,863,864,865,866,866,867,867,868,868,869,869,870,870,870,871,871,872,872,873,873,874,875,875,876,877,878,878,879,879,880,880,881,881,882,882,882,883,883,884,884,884,885,885,886,887,888,889,889,889,890,890,890,891,891,891,892,892,893,893,894,894,895,895,896,896,897,898,898,899,899,899,900,900,900,901,902,902,903,904,904,905,905,906,907,907,908,908,909,909,909,909,910,910,910,910,911,911,912,912,913,913,914,915,916,916,916,917,917,918,918,919,919,919,920,920,920,921,921,921,922,922,922,923,923,923,924,924,924,925,925,925,926,926,926,927,927,927,928,928,928,929,930,930,931,931,932,933,933,934,934,935,935,936,936,937,937,938,938,938,939,939,939,940,940,940,941,941,942,942,943,943,943,944,944,944,945,945,945,946,947,947,948,948,949,950,950,951,951,952,952,952,953,953,954,954,955,955,956,956,957,957,958,958,959,959,960,961,962,963,963,964,964,964,965,965,966,966,966,967,967,968,968,968,969,969,969,970,971,972,972,973,973,974,975,976,977,977,978,978,978,979,979,980,980,981,981,982,982,982,983,983,983,984,984,985,985,986,986,987,987,988,988,988,989,989,989,990,991,992,993,993,994,994,995,995,996,997,997,998,998,999,1000,1000,1001,1001,1002,1002,1003,1004,1004,1005,1005,1006,1007,1007,1007,1008,1008,1008,1009,1010,1010,1011,1012,1013,1014,1014,1015,1016,1016,1017,1017,1017,1018,1018,1019,1019,1020,1020,1021,1021,1022,1023,1023,1024,1024,1024,1025,1025,1026,1026,1027,1027,1027,1028,1028,1028,1029,1029,1029,1030,1031,1031,1032,1032,1032,1033,1034,1034,1035,1035,1036,1036,1037,1037,1038,1038,1039,1039,1040,1041,1041,1041,1042,1042,1043,1043,1044,1044,1045,1045,1046,1046,1046,1047,1047,1047,1048,1048,1049,1049,1050,1051,1051,1052,1052,1053,1053,1053,1054,1054,1055,1055,1056,1056,1057,1058,1058,1059,1059,1060,1060,1061,1062,1062,1062,1063,1063,1063,1064,1064,1064,1065,1065,1066,1067,1067,1067,1068,1068,1068,1069,1070,1071,1072,1072,1072,1073,1073,1073,1074,1074,1074,1075,1075,1075,1076,1076,1076,1077,1077,1077,1078,1078,1078,1079,1079,1080,1080,1080,1081,1081,1082,1083,1083,1084,1084,1084,1085,1086,1086,1086,1087,1087,1087,1088,1088,1088,1089,1089,1089,1090,1090,1090,1091,1091,1091,1092,1092,1092,1093,1093,1093,1094,1094,1094,1095,1095,1095,1096,1096,1096,1097,1097,1097,1098,1098,1098,1099,1099,1099,1100,1100,1100,1101,1101,1101,1102,1102,1102,1103,1103,1103,1104,1104,1104,1105,1105,1105,1106,1106,1106,1107,1107,1107,1108,1108,1108,1109,1109,1109,1110,1110,1110,1111,1111,1111,1112,1112,1112,1113,1113,1113,1114,1114,1114,1115,1115,1115,1116,1116,1116,1117,1117,1117,1118,1118,1118,1119,1119,1119,1120,1120,1120,1121,1121,1121,1122,1122,1122,1123,1123,1123,1124,1124,1124,1125,1125,1125,1126,1126,1126,1127,1127,1127,1128,1128,1128,1129,1129,1129,1130,1130,1130,1131,1131,1131,1132,1132,1132,1133,1133,1133,1134,1134,1134,1135,1135,1135,1136,1136,1136,1137,1137,1137,1138,1138,1138,1139,1139,1139,1140,1140,1140,1141,1141,1141,1142,1142,1143,1144,1144,1145,1145,1146,1146,1147,1148,1148,1149,1150,1150,1151,1152,1153,1153,1153,1154,1154,1155,1156,1157,1157,1158,1158,1159,1159,1160,1160,1161,1162,1163,1163,1163,1164,1164,1165,1165,1165,1166,1166,1166,1167,1167,1168,1168,1169,1170,1171,1171,1171,1172,1172,1173,1173,1174,1175,1176,1177,1177,1178,1179,1179,1179,1180,1180,1181,1181,1182,1182,1183,1183,1184,1185,1186,1186,1187,1187,1188,1188,1189,1189,1190,1190,1190,1191,1192,1192,1193,1193,1194,1194,1195,1195,1196,1196,1197,1198,1198,1199,1199,1200,1201,1202,1202,1203,1203,1204,1204,1204,1205,1206,1206,1207,1208,1208,1209,1209,1210,1211,1211,1212,1212,1213,1213,1213,1214,1214,1215,1215,1216,1216,1217,1217,1218,1218,1219,1219,1220,1221,1221,1222,1222,1222,1223,1223,1224,1224,1225,1225,1226,1226,1226,1227,1227,1228,1229,1230,1231,1232,1232,1232,1233,1233,1233,1234,1234,1234,1235,1235,1236,1236,1237,1238,1238,1239,1239,1240,1240,1241,1241,1242,1242,1243,1243,1243,1244,1245,1245,1246,1246,1247,1248,1248,1249,1249,1250,1251,1252,1252,1253,1253,1254,1254,1255,1255,1255,1256,1256,1256,1257,1257,1257,1258,1258,1259,1260,1261,1261,1262,1262,1263,1263,1264,1264,1265,1265,1266,1267,1268,1269,1269,1270,1271,1272,1272,1273,1274,1274,1275,1276,1277,1278,1278,1279,1279,1280,1281,1282,1283,1284,1285,1285,1286,1286,1287,1287,1288,1289,1290,1291,1291,1292,1293,1293,1294,1294,1295,1296,1296,1296,1297,1298,1298,1299,1300,1300,1301,1301,1302,1302,1303,1303,1304,1304,1305,1305,1306,1306,1307,1307,1308,1308,1309,1309,1310,1310,1311,1311,1312,1313,1313,1313,1314,1314,1315,1315,1316,1316,1317,1317,1318,1319,1319,1320,1321,1321,1322,1323,1323,1324,1325,1325,1325,1326,1327,1328,1329,1330,1330,1331,1331,1332,1332,1333,1333,1334,1335,1335,1336,1337,1337,1338,1338,1338,1339,1339,1340,1340,1341,1341,1341,1342,1342,1342,1343,1343,1344,1345,1345,1346,1346,1347,1347,1348,1349,1350,1350,1351,1351,1351,1351,1352,1352,1352,1352,1353,1354,1354,1355,1355,1356,1356,1357,1357,1358,1359,1360,1360,1361,1361,1362,1363,1363,1364,1364,1364,1365,1365,1366,1366,1367,1367,1368,1368,1369,1369,1370,1370,1371,1371,1372,1372,1373,1373,1374,1374,1375,1375,1376,1376,1377,1377,1378,1378,1379,1379,1380,1380,1381,1381,1382,1382,1383,1383,1384,1384,1385,1385,1386,1386,1387,1387,1388,1388,1389,1389,1390,1390,1391,1391,1392,1392,1393,1393,1394,1394,1395,1395,1396,1396,1397,1397,1398,1398,1399,1399,1399,1399,1399,1399,1399,1399,1399,1399,1399,1400,1400,1400,1400,1400,1400,1400,1400,1401,1401,1401,1401,1401,1401,1401,1401,1402,1402,1402,1402,1402,1402,1402,1402,1403,1403,1403,1403,1403,1403,1403,1403,1404,1404,1404,1404,1404,1404,1404,1404,1405,1405,1405,1405,1405,1405,1405,1405,1406,1406,1406,1406,1406,1406,1406,1406,1407,1407,1407,1407,1407,1407,1407,1407,1408,1408,1408,1408,1408,1408,1408,1408,1409,1409,1409,1409,1409,1409,1409,1409,1410,1410,1410,1410,1410,1410,1410,1410,1411,1411,1411,1411,1411,1411,1411,1411,1412,1412,1412,1412,1412,1412,1412,1412,1413,1413,1413,1413,1413,1413,1413,1413,1414,1414,1414,1414,1414,1414,1414,1414,1415,1415,1415,1415,1415,1415,1415,1415,1416,1416,1416,1416,1416,1416,1416,1416,1417,1417,1417,1417,1417,1417,1417,1417,1418,1418,1418,1418,1418,1418,1418,1418],"depth":[1,1,1,1,1,1,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,1,2,1,2,1,1,3,2,1,1,1,1,2,1,2,1,3,2,1,3,2,1,3,2,1,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,3,2,1,2,1,1,1,2,1,2,1,1,1,1,2,1,2,1,2,1,2,1,2,1,1,1,1,1,1,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,1,1,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,3,2,1,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,1,1,2,1,1,1,1,2,1,3,2,1,2,1,1,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,1,1,3,2,1,3,2,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,1,4,3,2,1,1,2,1,2,1,2,1,1,1,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,1,1,1,2,1,1,2,1,2,1,2,1,1,1,3,2,1,3,2,1,2,1,2,1,3,2,1,1,3,2,1,2,1,2,1,1,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,1,1,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,1,4,3,2,1,2,1,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,1,1,2,1,2,1,1,2,1,1,1,2,1,3,2,1,2,1,2,1,1,2,1,1,1,3,2,1,1,2,1,1,1,1,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,1,1,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,1,3,2,1,3,2,1,2,1,1,2,1,1,2,1,1,1,2,1,3,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,3,2,1,2,1,2,1,1,2,1,2,1,1,2,1,3,2,1,2,1,1,2,1,3,2,1,2,1,2,1,3,2,1,2,1,2,1,1,1,2,1,3,2,1,2,1,2,1,1,1,1,2,1,2,1,2,1,2,1,1,1,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,3,2,1,1,1,2,1,2,1,3,2,1,2,1,3,2,1,1,2,1,2,1,3,2,1,2,1,1,2,1,1,1,2,1,2,1,1,1,2,1,2,1,3,2,1,2,1,3,2,1,3,2,1,2,1,3,2,1,2,1,2,1,2,1,3,2,1,2,1,1,1,2,1,2,1,1,2,1,2,1,1,1,2,1,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,1,2,1,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,1,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,1,2,1,2,1,3,2,1,2,1,2,1,3,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,1,2,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,3,2,1,3,2,1,1,2,1,1,1,2,1,1,3,2,1,2,1,1,2,1,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,4,3,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,3,2,1,3,2,1,3,2,1,2,1,1,2,1,1,2,1,3,2,1,1,2,1,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,1,1,1,3,2,1,2,1,2,1,2,1,1,3,2,1,2,1,1,1,2,1,1,2,1,2,1,2,1,3,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,1,1,2,1,3,2,1,3,2,1,1,2,1,1,2,1,1,3,2,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,2,1,1,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,1,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,1,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,3,2,1,1,1,2,1,1,2,1,3,2,1,1,2,1,2,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,4,3,2,1,4,3,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,3,2,1,3,2,1,1,1,1,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,1,1,1,1,2,1,3,2,1,1,2,1,1,1,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,1,1,2,1,2,1,2,1,2,1,3,2,1,2,1,3,2,1,2,1,1,1,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,3,2,1,1,2,1,1,2,1,2,1,1,2,1,2,1,4,3,2,1,4,3,2,1,2,1,2,1,2,1,1,1,3,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,1,2,1,3,2,1,2,1,3,2,1,2,1,3,2,1,3,2,1,1,1,2,1,2,1,1,1,1,2,1,3,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,1,1,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,1,3,2,1,3,2,1,1,2,1,1,1,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,1,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,3,2,1,3,2,1,3,2,1,2,1,1,3,2,1,3,2,1,1,1,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,3,2,1,2,1,1,2,1,3,2,1,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,2,1,1,2,1,1,2,1,1,1,3,2,1,2,1,1,1,2,1,2,1,2,1,2,1,1,1,3,2,1,2,1,3,2,1,3,2,1,2,1,2,1,1,1,3,2,1,2,1,2,1,1,1,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,1,2,1,2,1,3,2,1,1,2,1,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,3,2,1,2,1,1,1,1,1,3,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,1,2,1,2,1,1,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,1,1,1,2,1,1,1,2,1,1,2,1,1,1,1,2,1,2,1,1,1,1,1,1,2,1,2,1,2,1,1,1,1,2,1,1,2,1,2,1,1,3,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,1,2,1,1,3,2,1,1,1,1,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,3,2,1,2,1,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,2,1,1,1,2,1,4,3,2,1,4,3,2,1,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,11,10,9,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1],"label":["rowSums","rowSums","rowSums","rowSums","rowMeans","rowMeans","rowMeans","rowMeans","<GC>","aperm.default","apply","aperm.default","apply","aperm.default","apply","aperm.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","mean.default","apply","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","apply","apply","mean.default","apply","mean.default","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","<GC>","is.numeric","local","length","local","apply","apply","mean.default","apply","mean.default","apply","apply","apply","apply","mean.default","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","apply","apply","apply","apply","apply","apply","mean.default","apply","<GC>","length","local","<GC>","length","local","FUN","apply","FUN","apply","mean.default","apply","length","local","apply","apply","apply","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","is.numeric","local","length","local","FUN","apply","FUN","apply","apply","<GC>","FUN","apply","apply","mean.default","apply","FUN","apply","FUN","apply","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","<GC>","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","apply","apply","apply","length","local","<GC>","mean.default","apply","is.na","local","apply","apply","apply","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","<GC>","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","<GC>","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","apply","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","mean.default","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","<GC>","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","apply","<GC>","apply","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","is.na","local","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","apply","<GC>","FUN","apply","mean.default","apply","FUN","apply","apply","apply","apply","FUN","apply","apply","<GC>","apply","length","local","mean.default","apply","apply","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","<GC>","mean.default","apply","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","apply","apply","FUN","apply","<GC>","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","length","local","FUN","apply","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","apply","<GC>","apply","is.numeric","local","isTRUE","mean.default","apply","apply","apply","apply","is.numeric","local","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","mean.default","apply","is.na","local","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","apply","<GC>","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","<GC>","apply","apply","length","local","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","<GC>","FUN","apply","mean.default","apply","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","<GC>","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","apply","<GC>","apply","FUN","apply","apply","FUN","apply","apply","apply","FUN","apply","<GC>","FUN","apply","FUN","apply","is.na","local","apply","FUN","apply","apply","apply","<GC>","FUN","apply","apply","FUN","apply","apply","apply","apply","apply","<GC>","is.numeric","local","length","local","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","apply","FUN","apply","FUN","apply","apply","apply","mean.default","apply","<GC>","mean.default","apply","apply","length","local","length","local","mean.default","apply","FUN","apply","mean.default","apply","<GC>","apply","<GC>","apply","is.numeric","local","apply","mean.default","apply","isTRUE","mean.default","apply","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","length","local","apply","FUN","apply","apply","FUN","apply","apply","apply","<GC>","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","is.numeric","local","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","<GC>","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","apply","isTRUE","mean.default","apply","mean.default","apply","<GC>","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","<GC>","FUN","apply","FUN","apply","is.na","local","apply","apply","apply","FUN","apply","<GC>","apply","FUN","apply","FUN","apply","apply","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","length","local","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","apply","mean.default","apply","FUN","apply","<GC>","mean.default","apply","FUN","apply","apply","FUN","apply","apply","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","is.numeric","local","<GC>","is.numeric","local","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","mean.default","apply","FUN","apply","apply","FUN","apply","<GC>","apply","apply","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","FUN","apply","length","local","FUN","apply","FUN","apply","apply","<GC>","apply","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","is.na","local","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","mean.default","apply","apply","isTRUE","mean.default","apply","mean.default","apply","apply","FUN","apply","apply","mean.default","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","apply","mean.default","apply","FUN","apply","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","apply","<GC>","apply","<GC>","apply","is.numeric","local","length","local","apply","FUN","apply","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","mean.default","apply","mean.default","apply","length","local","apply","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","is.numeric","local","<GC>","FUN","apply","mean.default","apply","is.na","local","mean.default","apply","FUN","apply","FUN","apply","apply","mean.default","apply","apply","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","is.numeric","local","apply","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","<GC>","apply","<GC>","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","is.na","local","apply","apply","FUN","apply","apply","isTRUE","mean.default","apply","mean.default","apply","apply","FUN","apply","apply","<GC>","FUN","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","is.na","local","mean.default","apply","FUN","apply","apply","is.na","local","FUN","apply","apply","<GC>","isTRUE","mean.default","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","apply","FUN","apply","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","apply","mean.default","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","length","local","mean.default","apply","FUN","apply","apply","FUN","apply","apply","is.numeric","local","FUN","apply","length","local","FUN","apply","<GC>","apply","<GC>","apply","FUN","apply","apply","apply","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","<GC>","FUN","apply","FUN","apply","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","apply","apply","isTRUE","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","length","local","FUN","apply","mean.default","apply","apply","apply","FUN","apply","mean.default","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","apply","mean.default","apply","apply","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","apply","FUN","apply","is.na","local","apply","FUN","apply","apply","mean.default","apply","FUN","apply","<GC>","apply","FUN","apply","length","local","length","local","apply","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","mean.default","apply","<GC>","FUN","apply","is.numeric","local","mean.default","apply","mean.default","apply","apply","apply","mean.default","apply","FUN","apply","FUN","apply","apply","length","local","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","length","local","is.na","local","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","mean.default","apply","length","local","FUN","apply","length","local","apply","apply","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","FUN","apply","mean.default","apply","is.na","local","length","local","is.na","local","is.numeric","local","apply","apply","apply","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","apply","apply","mean.default","apply","apply","length","local","isTRUE","mean.default","apply","apply","FUN","apply","<GC>","apply","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","FUN","apply","is.na","local","mean.default","apply","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","apply","apply","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","is.numeric","local","FUN","apply","apply","apply","apply","apply","apply","mean.default","apply","<GC>","length","local","apply","is.numeric","local","apply","apply","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","<GC>","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","apply","apply","FUN","apply","<GC>","apply","<GC>","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","is.na","local","apply","apply","apply","<GC>","length","local","<GC>","length","local","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","mean.default","apply","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","<GC>","apply","<GC>","apply","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","<GC>","apply","<GC>","apply","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","apply","is.numeric","local","FUN","apply","apply","apply","apply","FUN","apply","<GC>","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","apply","apply","FUN","apply","mean.default","apply","is.numeric","local","apply","<GC>","apply","<GC>","apply","apply","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","mean.default","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","length","local","apply","apply","apply","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","apply","<GC>","apply","FUN","apply","length","local","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","apply","is.numeric","local","FUN","apply","mean.default","apply","<GC>","apply","<GC>","apply","length","local","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","length","local","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","apply","<GC>","apply","apply","mean.default","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","is.na","local","apply","FUN","apply","isTRUE","mean.default","apply","apply","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","mean.default","apply","FUN","apply","apply","FUN","apply","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","mean.default","apply","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","is.na","local","apply","apply","isTRUE","mean.default","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","mean.default","apply","is.na","local","apply","apply","apply","is.na","local","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","length","local","FUN","apply","apply","apply","length","local","<GC>","apply","<GC>","apply","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","length","local","mean.default","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","apply","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","mean.default","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","length","local","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","length","local","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","apply","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","length","local","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","apply","mean.default","apply","length","local","apply","apply","FUN","apply","FUN","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","apply","apply","is.na","local","FUN","apply","FUN","apply","mean.default","apply","length","local","apply","apply","apply","mean.default","apply","apply","apply","FUN","apply","apply","mean.default","apply","apply","apply","apply","<GC>","apply","<GC>","apply","apply","apply","apply","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","mean.default","apply","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","apply","is.na","local","apply","FUN","apply","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","apply","apply","apply","<GC>","apply","<GC>","apply","length","local","FUN","apply","apply","FUN","apply","apply","mean.default","apply","isTRUE","mean.default","apply","length","local","length","local","isTRUE","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","apply","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","apply","apply","length","local","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","any","local","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","$<-","make.callContext","cmpCall","cmp","h","tryInline","cmpCall","cmp","genCode","compile","compiler:::tryCompile","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis"],"filenum":[1,1,1,1,1,1,1,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,1,null,1,null,1,null,1,1,null,1,null,1,1,null,null,1,1,1,1,null,1,null,1,null,null,1,null,null,1,null,null,1,1,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,null,null,null,null,1,1,null,1,null,1,1,1,1,null,1,null,1,null,1,null,1,null,1,1,1,1,1,1,1,null,1,null,null,null,null,null,null,null,1,null,1,null,1,null,null,1,1,1,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,null,1,null,null,null,null,null,1,null,1,1,null,null,1,1,null,1,null,1,null,1,1,null,1,null,1,null,null,1,1,null,1,null,1,null,1,1,1,null,1,1,1,1,null,null,null,null,1,null,null,1,1,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,1,null,1,null,1,null,null,1,null,1,null,1,null,1,1,null,1,null,1,1,1,null,null,1,null,null,1,null,1,null,1,1,null,1,null,1,null,null,1,null,null,1,1,null,null,null,1,1,null,1,null,1,null,1,1,1,1,null,1,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,null,null,1,1,null,1,null,1,null,1,null,1,1,null,null,1,null,1,null,1,1,1,1,null,1,1,null,1,null,null,null,1,1,1,null,null,1,null,null,1,null,1,null,1,null,null,1,1,null,null,1,null,1,null,1,1,1,null,1,null,1,null,1,null,null,1,null,1,1,null,null,null,1,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,null,null,null,1,1,1,1,null,null,null,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,null,null,null,1,1,null,1,null,1,1,null,null,null,1,null,1,1,null,1,1,null,1,null,1,null,1,1,null,null,null,1,null,1,null,1,null,1,1,null,null,1,null,1,1,null,1,null,1,1,null,1,null,1,1,null,1,null,1,null,1,1,1,null,1,null,1,1,null,1,1,1,null,1,null,null,1,null,1,null,null,1,null,1,1,1,null,null,1,1,null,1,1,1,1,1,null,null,null,null,null,null,1,1,null,1,null,1,null,1,null,null,1,1,null,1,null,1,1,1,null,1,null,null,1,1,null,null,null,null,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,null,1,1,null,null,1,null,null,1,null,null,1,null,1,1,null,1,1,1,null,1,null,null,1,1,null,1,null,1,null,1,null,null,null,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,1,null,null,1,null,1,null,1,1,null,1,null,1,1,null,1,null,null,1,null,1,1,null,1,null,null,1,null,1,null,1,null,null,1,null,1,null,1,1,1,null,1,null,null,1,null,1,null,null,1,1,1,null,1,null,1,null,1,null,1,1,1,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,null,null,null,1,null,1,null,null,1,1,1,null,1,null,1,null,null,1,null,1,null,null,1,1,null,1,null,1,null,null,1,null,1,1,null,1,1,1,null,1,null,1,1,1,null,1,null,1,null,null,1,null,1,null,null,null,null,null,null,null,1,null,null,1,null,1,null,1,null,1,null,null,1,null,1,1,1,null,1,null,1,1,null,1,null,1,1,1,null,1,1,null,null,1,1,null,1,null,1,null,1,null,null,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,1,null,null,1,null,1,1,null,1,1,null,1,null,1,null,1,null,null,1,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,1,null,1,null,1,null,null,null,null,1,null,1,1,1,null,1,null,1,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,null,1,1,null,1,null,1,null,null,1,null,1,null,1,null,null,1,null,null,null,null,1,null,1,null,null,null,1,null,1,null,1,1,null,1,1,1,null,1,null,1,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,null,1,1,null,1,null,1,null,1,null,null,1,1,null,1,null,1,null,null,1,null,null,1,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,1,null,1,null,null,1,null,null,1,1,null,null,1,1,null,1,1,null,null,1,null,1,1,null,1,1,null,null,1,1,null,1,null,1,null,1,null,null,null,1,null,1,1,null,null,null,1,1,null,null,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,1,null,1,1,null,1,null,null,1,null,null,1,null,null,1,null,1,1,null,1,1,null,1,null,null,1,1,null,1,1,null,null,1,null,null,1,null,1,null,null,null,1,null,1,1,null,1,1,null,null,null,1,null,null,null,1,null,1,null,1,null,1,1,1,1,1,1,null,null,1,null,1,null,1,null,1,1,null,null,1,null,1,1,1,null,1,1,null,1,null,1,null,1,null,null,1,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,null,null,null,1,null,1,1,1,null,1,null,1,1,1,null,1,null,null,1,null,null,1,1,null,1,1,null,1,1,null,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,1,null,1,null,null,1,null,1,1,null,1,null,1,null,1,null,1,null,null,null,null,1,1,null,1,1,null,1,null,1,null,1,null,null,1,null,null,null,1,null,1,1,1,null,1,null,1,null,1,1,null,null,null,null,1,null,null,1,null,1,null,null,null,null,1,null,null,1,null,null,1,null,1,1,1,null,null,1,null,null,1,1,null,1,null,null,null,1,null,null,1,1,1,null,1,1,null,1,null,1,null,1,null,1,null,null,null,null,null,null,null,null,1,1,1,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,1,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,null,1,null,null,1,null,null,1,1,1,null,1,1,null,null,null,null,1,1,null,1,null,1,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,null,1,null,null,null,1,null,1,null,null,null,1,1,null,1,null,1,1,null,1,null,null,1,null,null,1,1,1,1,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,1,null,null,null,1,1,1,1,1,1,null,1,null,null,null,1,null,null,1,1,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,1,null,1,1,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,null,1,null,null,1,1,1,null,null,null,null,null,null,null,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,null,1,null,null,1,1,null,1,1,null,1,null,1,1,null,1,null,1,null,null,null,1,null,null,null,1,null,1,null,1,null,1,1,1,null,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,1,null,1,null,1,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,1,1,null,1,null,null,1,null,1,null,null,1,null,1,null,null,1,null,null,1,1,1,null,null,null,1,1,1,1,null,1,null,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,1,1,1,null,1,null,1,null,null,1,null,1,null,1,1,null,1,null,1,null,1,1,null,1,null,1,1,null,null,1,null,null,1,1,null,null,1,1,1,null,1,1,null,1,null,null,1,null,1,null,1,null,1,null,null,1,null,1,null,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,1,null,1,null,null,1,1,null,null,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,1,null,1,null,null,null,1,null,null,1,null,null,1,null,1,null,1,1,null,1,null,1,null,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,1,null,null,1,null,null,1,null,null,1,null,1,1,null,null,1,null,null,1,1,1,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,null,null,1,null,null,1,null,1,null,null,1,1,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,1,null,1,1,null,1,null,1,null,1,1,null,1,1,null,1,1,1,null,null,1,null,1,1,1,null,1,null,1,null,1,null,null,1,1,null,null,1,null,1,null,null,1,null,null,1,null,1,null,1,1,1,null,null,1,null,1,null,null,1,1,1,null,null,1,null,null,1,null,1,null,1,null,null,null,1,1,1,null,null,null,1,null,1,null,1,null,null,1,1,null,1,null,null,null,1,null,1,null,1,1,null,1,null,1,1,1,null,1,null,1,null,null,1,1,null,1,1,null,1,null,1,1,null,1,null,1,null,null,1,null,1,null,1,null,null,null,1,null,1,null,1,1,null,1,null,null,1,null,1,null,null,null,1,null,null,1,null,1,1,1,1,1,null,null,1,null,null,1,null,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,null,null,null,1,1,null,1,null,1,1,null,1,null,null,1,1,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,1,1,1,null,null,null,1,null,1,null,1,null,null,1,1,1,null,1,1,1,null,1,1,null,1,1,1,1,null,1,null,1,1,1,1,1,1,null,1,null,1,null,1,1,1,1,null,1,1,null,1,null,1,1,null,null,1,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,null,1,null,1,null,1,null,1,null,1,1,null,null,1,null,1,1,null,1,1,null,null,1,1,1,1,1,null,1,null,1,null,null,null,1,1,null,1,1,null,1,null,null,1,null,null,null,null,null,null,1,null,null,1,null,1,1,null,1,null,1,null,1,1,1,null,1,null,null,null,1,null,null,null,1,1,null,1,null,1,null,1,null,1,1,1,null,null,null,1,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,null,null,null,null,null,null,null,null,1,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null],"linenum":[10,10,10,10,11,11,11,11,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,12,null,12,null,12,null,12,12,null,12,null,12,12,null,null,12,12,12,12,null,12,null,12,null,null,12,null,null,12,null,null,12,12,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,null,null,null,null,12,12,null,12,null,12,12,12,12,null,12,null,12,null,12,null,12,null,12,12,12,12,12,12,12,null,12,null,null,null,null,null,null,null,12,null,12,null,12,null,null,12,12,12,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,null,12,null,null,null,null,null,12,null,12,12,null,null,12,12,null,12,null,12,null,12,12,null,12,null,12,null,null,12,12,null,12,null,12,null,12,12,12,null,12,12,12,12,null,null,null,null,12,null,null,12,12,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,12,null,12,null,12,null,null,12,null,12,null,12,null,12,12,null,12,null,12,12,12,null,null,12,null,null,12,null,12,null,12,12,null,12,null,12,null,null,12,null,null,12,12,null,null,null,12,12,null,12,null,12,null,12,12,12,12,null,12,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,null,null,12,12,null,12,null,12,null,12,null,12,12,null,null,12,null,12,null,12,12,12,12,null,12,12,null,12,null,null,null,12,12,12,null,null,12,null,null,12,null,12,null,12,null,null,12,12,null,null,12,null,12,null,12,12,12,null,12,null,12,null,12,null,null,12,null,12,12,null,null,null,12,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,null,null,null,12,12,12,12,null,null,null,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,null,null,null,12,12,null,12,null,12,12,null,null,null,12,null,12,12,null,12,12,null,12,null,12,null,12,12,null,null,null,12,null,12,null,12,null,12,12,null,null,12,null,12,12,null,12,null,12,12,null,12,null,12,12,null,12,null,12,null,12,12,12,null,12,null,12,12,null,12,12,12,null,12,null,null,12,null,12,null,null,12,null,12,12,12,null,null,12,12,null,12,12,12,12,12,null,null,null,null,null,null,12,12,null,12,null,12,null,12,null,null,12,12,null,12,null,12,12,12,null,12,null,null,12,12,null,null,null,null,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,null,12,12,null,null,12,null,null,12,null,null,12,null,12,12,null,12,12,12,null,12,null,null,12,12,null,12,null,12,null,12,null,null,null,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,12,null,null,12,null,12,null,12,12,null,12,null,12,12,null,12,null,null,12,null,12,12,null,12,null,null,12,null,12,null,12,null,null,12,null,12,null,12,12,12,null,12,null,null,12,null,12,null,null,12,12,12,null,12,null,12,null,12,null,12,12,12,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,null,null,null,12,null,12,null,null,12,12,12,null,12,null,12,null,null,12,null,12,null,null,12,12,null,12,null,12,null,null,12,null,12,12,null,12,12,12,null,12,null,12,12,12,null,12,null,12,null,null,12,null,12,null,null,null,null,null,null,null,12,null,null,12,null,12,null,12,null,12,null,null,12,null,12,12,12,null,12,null,12,12,null,12,null,12,12,12,null,12,12,null,null,12,12,null,12,null,12,null,12,null,null,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,12,null,null,12,null,12,12,null,12,12,null,12,null,12,null,12,null,null,12,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,12,null,12,null,12,null,null,null,null,12,null,12,12,12,null,12,null,12,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,null,12,12,null,12,null,12,null,null,12,null,12,null,12,null,null,12,null,null,null,null,12,null,12,null,null,null,12,null,12,null,12,12,null,12,12,12,null,12,null,12,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,null,12,12,null,12,null,12,null,12,null,null,12,12,null,12,null,12,null,null,12,null,null,12,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,12,null,12,null,null,12,null,null,12,12,null,null,12,12,null,12,12,null,null,12,null,12,12,null,12,12,null,null,12,12,null,12,null,12,null,12,null,null,null,12,null,12,12,null,null,null,12,12,null,null,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,12,null,12,12,null,12,null,null,12,null,null,12,null,null,12,null,12,12,null,12,12,null,12,null,null,12,12,null,12,12,null,null,12,null,null,12,null,12,null,null,null,12,null,12,12,null,12,12,null,null,null,12,null,null,null,12,null,12,null,12,null,12,12,12,12,12,12,null,null,12,null,12,null,12,null,12,12,null,null,12,null,12,12,12,null,12,12,null,12,null,12,null,12,null,null,12,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,null,null,null,12,null,12,12,12,null,12,null,12,12,12,null,12,null,null,12,null,null,12,12,null,12,12,null,12,12,null,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,12,null,12,null,null,12,null,12,12,null,12,null,12,null,12,null,12,null,null,null,null,12,12,null,12,12,null,12,null,12,null,12,null,null,12,null,null,null,12,null,12,12,12,null,12,null,12,null,12,12,null,null,null,null,12,null,null,12,null,12,null,null,null,null,12,null,null,12,null,null,12,null,12,12,12,null,null,12,null,null,12,12,null,12,null,null,null,12,null,null,12,12,12,null,12,12,null,12,null,12,null,12,null,12,null,null,null,null,null,null,null,null,12,12,12,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,12,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,null,12,null,null,12,null,null,12,12,12,null,12,12,null,null,null,null,12,12,null,12,null,12,12,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,null,12,null,null,null,12,null,12,null,null,null,12,12,null,12,null,12,12,null,12,null,null,12,null,null,12,12,12,12,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,12,null,null,null,12,12,12,12,12,12,null,12,null,null,null,12,null,null,12,12,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,12,null,12,12,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,null,12,null,null,12,12,12,null,null,null,null,null,null,null,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,null,12,null,null,12,12,null,12,12,null,12,null,12,12,null,12,null,12,null,null,null,12,null,null,null,12,null,12,null,12,null,12,12,12,null,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,12,null,12,null,12,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,12,12,null,12,null,null,12,null,12,null,null,12,null,12,null,null,12,null,null,12,12,12,null,null,null,12,12,12,12,null,12,null,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,12,12,12,null,12,null,12,null,null,12,null,12,null,12,12,null,12,null,12,null,12,12,null,12,null,12,12,null,null,12,null,null,12,12,null,null,12,12,12,null,12,12,null,12,null,null,12,null,12,null,12,null,12,null,null,12,null,12,null,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,12,null,12,null,null,12,12,null,null,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,12,null,12,null,null,null,12,null,null,12,null,null,12,null,12,null,12,12,null,12,null,12,null,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,12,null,null,12,null,null,12,null,null,12,null,12,12,null,null,12,null,null,12,12,12,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,null,null,12,null,null,12,null,12,null,null,12,12,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,12,null,12,12,null,12,null,12,null,12,12,null,12,12,null,12,12,12,null,null,12,null,12,12,12,null,12,null,12,null,12,null,null,12,12,null,null,12,null,12,null,null,12,null,null,12,null,12,null,12,12,12,null,null,12,null,12,null,null,12,12,12,null,null,12,null,null,12,null,12,null,12,null,null,null,12,12,12,null,null,null,12,null,12,null,12,null,null,12,12,null,12,null,null,null,12,null,12,null,12,12,null,12,null,12,12,12,null,12,null,12,null,null,12,12,null,12,12,null,12,null,12,12,null,12,null,12,null,null,12,null,12,null,12,null,null,null,12,null,12,null,12,12,null,12,null,null,12,null,12,null,null,null,12,null,null,12,null,12,12,12,12,12,null,null,12,null,null,12,null,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,null,null,null,12,12,null,12,null,12,12,null,12,null,null,12,12,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,12,12,12,null,null,null,12,null,12,null,12,null,null,12,12,12,null,12,12,12,null,12,12,null,12,12,12,12,null,12,null,12,12,12,12,12,12,null,12,null,12,null,12,12,12,12,null,12,12,null,12,null,12,12,null,null,12,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,null,12,null,12,null,12,null,12,null,12,12,null,null,12,null,12,12,null,12,12,null,null,12,12,12,12,12,null,12,null,12,null,null,null,12,12,null,12,12,null,12,null,null,12,null,null,null,null,null,null,12,null,null,12,null,12,12,null,12,null,12,null,12,12,12,null,12,null,null,null,12,null,null,null,12,12,null,12,null,12,null,12,null,12,12,12,null,null,null,12,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,null,null,null,null,null,null,null,null,13,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null],"memalloc":[124.4584884643555,124.4584884643555,124.4584884643555,124.4584884643555,139.74072265625,139.74072265625,139.74072265625,139.74072265625,139.7410888671875,139.7410888671875,139.7410888671875,170.2064666748047,170.2064666748047,170.2064666748047,170.2064666748047,170.2064666748047,170.2064666748047,170.2065124511719,170.2065124511719,170.2065124511719,170.2065124511719,170.2065124511719,170.2065124511719,170.2065124511719,170.2065124511719,170.2065124511719,170.2065124511719,170.2065124511719,170.2065124511719,170.2065124511719,170.2065124511719,170.2065124511719,170.2065124511719,170.2065124511719,170.2065124511719,170.2065124511719,170.2065124511719,170.2062072753906,170.2062072753906,170.2062072753906,170.2062072753906,185.6661682128906,185.6661682128906,185.6661682128906,185.9137954711914,186.1579895019531,186.1579895019531,186.3831253051758,186.3831253051758,186.5373840332031,186.5373840332031,186.7201156616211,186.8542785644531,186.8542785644531,186.9986953735352,186.9986953735352,187.148551940918,187.2987823486328,187.2987823486328,187.2987823486328,187.4603729248047,187.6361999511719,187.9473876953125,188.2710952758789,188.2710952758789,188.638053894043,188.638053894043,188.7220611572266,188.7220611572266,188.7220611572266,185.7563247680664,185.7563247680664,185.7563247680664,186.085334777832,186.085334777832,186.085334777832,186.4240493774414,186.6889190673828,187.0646820068359,187.0646820068359,187.4547424316406,187.4547424316406,187.7020111083984,187.7020111083984,188.0673370361328,188.0673370361328,188.0673370361328,188.4480972290039,188.4480972290039,188.7308044433594,188.7308044433594,188.7917175292969,188.7917175292969,188.7917175292969,186.0375289916992,186.0375289916992,186.3636322021484,186.6341247558594,187.0040512084961,187.0040512084961,187.3149948120117,187.3149948120117,187.5092926025391,187.8388442993164,188.2171630859375,188.5252685546875,188.5252685546875,188.8788146972656,188.8788146972656,188.8788146972656,188.8788146972656,186.0381011962891,186.0381011962891,186.2853317260742,186.2853317260742,186.6301422119141,186.9867095947266,187.3440475463867,187.6800842285156,188.0596389770508,188.4032211303711,188.6939544677734,188.6939544677734,188.9643478393555,188.9643478393555,188.9643478393555,188.9643478393555,188.9643478393555,188.9643478393555,186.2095794677734,186.2095794677734,186.4963226318359,186.4963226318359,186.7974395751953,186.7974395751953,187.0629730224609,187.0629730224609,187.369743347168,187.7209548950195,187.994873046875,188.3219604492188,188.6504516601562,188.6504516601562,188.9696578979492,188.9696578979492,189.0486297607422,189.0486297607422,189.0486297607422,186.3751220703125,186.3751220703125,186.6828689575195,186.6828689575195,186.9918975830078,186.9918975830078,187.3346099853516,187.3346099853516,187.3346099853516,187.6855545043945,187.6855545043945,188.0396957397461,188.0396957397461,188.3844604492188,188.3844604492188,188.7323226928711,188.7323226928711,189.055549621582,189.131477355957,189.131477355957,189.131477355957,186.4472808837891,186.7478256225586,186.7478256225586,187.0326156616211,187.0326156616211,187.3256607055664,187.3256607055664,187.6763153076172,187.9872283935547,187.9872283935547,188.3069229125977,188.3069229125977,188.6638565063477,188.6638565063477,188.6638565063477,188.9887237548828,189.2129592895508,189.2129592895508,186.4888534545898,186.4888534545898,186.7881088256836,186.7881088256836,187.0807342529297,187.4189453125,187.7768630981445,187.7768630981445,188.0949401855469,188.4475860595703,188.849250793457,189.2003555297852,189.2003555297852,189.2931976318359,189.2931976318359,189.2931976318359,186.783073425293,186.783073425293,187.1177444458008,187.4468231201172,187.8044891357422,188.1709442138672,188.1709442138672,188.5181732177734,188.5181732177734,188.8917541503906,188.8917541503906,189.2894058227539,189.2894058227539,189.3720932006836,189.3720932006836,186.897705078125,186.897705078125,186.897705078125,187.2488327026367,187.2488327026367,187.5932693481445,187.5932693481445,187.9306030273438,188.2869262695312,188.2869262695312,188.6624450683594,188.6624450683594,189.0072784423828,189.0072784423828,189.0072784423828,189.3801956176758,189.3801956176758,189.4498062133789,189.4498062133789,187.029655456543,187.029655456543,187.3489151000977,187.6928176879883,187.6928176879883,188.0460739135742,188.0460739135742,188.3993148803711,188.7624359130859,189.154182434082,189.154182434082,189.154182434082,189.5261688232422,189.5261688232422,189.5261688232422,186.9267044067383,186.9267044067383,187.2726058959961,187.2726058959961,187.6052474975586,187.9599075317383,187.9599075317383,188.3235397338867,188.3235397338867,188.7018356323242,188.7018356323242,188.7018356323242,189.0836715698242,189.0836715698242,189.0836715698242,189.4896850585938,189.601318359375,189.601318359375,189.601318359375,189.601318359375,187.2735214233398,187.611083984375,187.611083984375,187.9693908691406,187.9693908691406,188.3317489624023,188.3317489624023,188.7145309448242,189.1175994873047,189.5315475463867,189.6752624511719,189.6752624511719,187.358772277832,187.6979293823242,187.6979293823242,187.6979293823242,188.0578308105469,188.0578308105469,188.4292755126953,188.4292755126953,188.8230438232422,188.8230438232422,189.2319030761719,189.2319030761719,189.6522369384766,189.6522369384766,189.7480087280273,189.7480087280273,189.7480087280273,187.5156402587891,187.846061706543,188.1966171264648,188.1966171264648,188.5684661865234,188.5684661865234,188.9643173217773,188.9643173217773,189.3719329833984,189.3719329833984,189.7892913818359,189.8195877075195,189.8195877075195,189.8195877075195,187.6611404418945,187.6611404418945,187.9769744873047,187.9769744873047,188.3190689086914,188.6601943969727,189.0209503173828,189.4004364013672,189.4004364013672,189.7723388671875,189.8899612426758,189.8899612426758,187.6275253295898,187.6275253295898,187.8987731933594,187.8987731933594,188.1818008422852,188.5089569091797,188.8635482788086,188.8635482788086,188.8635482788086,189.1679992675781,189.1679992675781,189.1679992675781,189.5160064697266,189.5160064697266,189.8807601928711,189.8807601928711,189.9592437744141,189.9592437744141,189.9592437744141,187.7670669555664,188.0726089477539,188.0726089477539,188.0726089477539,188.3933868408203,188.3933868408203,188.7306213378906,188.7306213378906,189.0922622680664,189.4703140258789,189.8305053710938,189.8305053710938,190.0274429321289,190.0274429321289,187.8066329956055,187.8066329956055,188.0766983032227,188.0766983032227,188.0766983032227,188.3748245239258,188.3748245239258,188.7123184204102,189.0653610229492,189.0653610229492,189.4117126464844,189.4117126464844,189.7744750976562,190.0944976806641,190.0944976806641,190.0944976806641,187.8222961425781,187.8222961425781,188.103759765625,188.103759765625,188.4120712280273,188.4120712280273,188.7326812744141,188.7326812744141,189.0834655761719,189.0834655761719,189.4503631591797,189.4503631591797,189.817024230957,190.160514831543,190.160514831543,187.9008941650391,187.9008941650391,188.171989440918,188.171989440918,188.171989440918,188.4448318481445,188.7577056884766,189.1059188842773,189.4463195800781,189.4463195800781,189.804069519043,189.804069519043,190.184326171875,190.184326171875,190.2254028320312,190.2254028320312,190.2254028320312,190.2254028320312,190.2254028320312,190.2254028320312,190.2254028320312,190.2254028320312,190.2254028320312,190.2254028320312,190.2254028320312,190.2254028320312,190.2254028320312,190.2254028320312,190.2254028320312,190.2254028320312,190.2254028320312,190.2254028320312,190.2254028320312,190.2254028320312,190.2254028320312,190.2254028320312,190.2254028320312,190.2254028320312,190.2254028320312,190.2254028320312,190.2254028320312,188.0863037109375,188.0863037109375,188.310905456543,188.310905456543,188.5734024047852,188.5734024047852,188.8395843505859,188.8395843505859,188.8395843505859,189.1435546875,189.477783203125,189.477783203125,189.8197708129883,189.8197708129883,190.1943054199219,190.2890167236328,190.2890167236328,190.2890167236328,190.2890167236328,188.2969665527344,188.2969665527344,188.5853958129883,188.9104461669922,188.9104461669922,189.2654876708984,189.635498046875,189.635498046875,190.0303192138672,190.0303192138672,190.351921081543,190.351921081543,188.2422866821289,188.52197265625,188.52197265625,188.8290100097656,188.8290100097656,189.1731185913086,189.1731185913086,189.5401077270508,189.5401077270508,189.9273147583008,189.9273147583008,190.3293991088867,190.4137496948242,190.4137496948242,190.4137496948242,188.5016708374023,188.5016708374023,188.7917861938477,189.119026184082,189.119026184082,189.4740142822266,189.4740142822266,189.8415069580078,190.2388687133789,190.2388687133789,190.4746017456055,190.4746017456055,188.4858627319336,188.7647094726562,188.7647094726562,189.0783157348633,189.0783157348633,189.4288711547852,189.4288711547852,189.7934265136719,190.1876983642578,190.5345458984375,190.5345458984375,188.5310134887695,188.5310134887695,188.809211730957,189.1199111938477,189.1199111938477,189.4664764404297,189.8323440551758,190.2238311767578,190.2238311767578,190.5933990478516,190.5933990478516,190.5933990478516,188.5877456665039,188.5877456665039,188.8639755249023,188.8639755249023,189.1718597412109,189.5177841186523,189.5177841186523,189.8824081420898,190.2646865844727,190.6513595581055,190.6513595581055,190.6513595581055,188.6582717895508,188.9316635131836,188.9316635131836,189.2355880737305,189.5805206298828,189.9466857910156,190.3339691162109,190.7083740234375,190.7083740234375,190.7083740234375,188.7607269287109,188.7607269287109,189.0328521728516,189.0328521728516,189.3343734741211,189.6771850585938,189.6771850585938,190.0378570556641,190.0378570556641,190.4087448120117,190.4087448120117,190.7644577026367,190.7644577026367,190.7644577026367,188.8370590209961,189.0953598022461,189.0953598022461,189.3884735107422,189.3884735107422,189.7268981933594,190.0890808105469,190.461669921875,190.461669921875,190.8196258544922,190.8196258544922,190.8196258544922,188.9580612182617,189.2244186401367,189.2244186401367,189.5257034301758,189.5257034301758,189.8677062988281,189.8677062988281,190.2188034057617,190.2188034057617,190.5522079467773,190.5522079467773,190.873908996582,190.873908996582,190.873908996582,190.873908996582,189.2101440429688,189.2101440429688,189.4535598754883,189.7460708618164,189.7460708618164,190.0690994262695,190.0690994262695,190.0690994262695,190.3763961791992,190.7292404174805,190.7292404174805,190.7292404174805,190.9273300170898,190.9273300170898,190.9273300170898,189.0988464355469,189.0988464355469,189.3320922851562,189.5996398925781,189.5996398925781,189.9067764282227,190.2425689697266,190.2425689697266,190.5995635986328,190.9634246826172,190.9798736572266,190.9798736572266,189.3783874511719,189.3783874511719,189.3783874511719,189.6825256347656,190.001823425293,190.001823425293,190.3515625,190.3515625,190.7216415405273,190.7216415405273,191.0315551757812,191.0315551757812,191.0315551757812,189.2765884399414,189.2765884399414,189.2765884399414,189.5353927612305,189.5353927612305,189.8296661376953,189.8296661376953,190.1653518676758,190.1653518676758,190.5270309448242,190.5270309448242,190.8981399536133,190.8981399536133,191.0824584960938,191.0824584960938,189.4387588500977,189.4387588500977,189.4387588500977,189.7030639648438,189.7030639648438,190.0059204101562,190.0059204101562,190.3475952148438,190.7069244384766,190.7069244384766,190.7069244384766,191.0798110961914,191.0798110961914,191.1324996948242,191.1324996948242,189.6022796630859,189.8823394775391,189.8823394775391,190.2003173828125,190.2003173828125,190.5516052246094,190.9197540283203,190.9197540283203,191.181755065918,191.181755065918,191.181755065918,189.5357666015625,189.5357666015625,189.7965240478516,190.0903778076172,190.0903778076172,190.4045028686523,190.4045028686523,190.4045028686523,190.7349166870117,190.7349166870117,191.0909423828125,191.0909423828125,191.2301406860352,191.2301406860352,191.2301406860352,189.6936416625977,189.6936416625977,189.9598236083984,189.9598236083984,190.2683792114258,190.614875793457,190.9804077148438,190.9804077148438,191.2778396606445,191.2778396606445,191.2778396606445,189.6655120849609,189.6655120849609,189.9218444824219,189.9218444824219,190.2179183959961,190.5576324462891,190.906379699707,191.2684326171875,191.2684326171875,191.3247451782227,191.3247451782227,189.8811950683594,189.8811950683594,190.1486358642578,190.1486358642578,190.4671096801758,190.8181381225586,191.1873321533203,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,191.3708343505859,189.7824554443359,189.7824554443359,189.7824554443359,189.8493347167969,189.8493347167969,190.1264190673828,190.1264190673828,190.3954162597656,190.3954162597656,190.6964874267578,190.6964874267578,191.0135955810547,191.0135955810547,191.0135955810547,191.3271484375,191.6942443847656,192.0817184448242,192.0817184448242,192.4918441772461,192.4918441772461,192.849609375,192.849609375,192.849609375,193.1828689575195,193.1828689575195,193.5218505859375,193.5218505859375,193.5218505859375,193.8676452636719,194.2044906616211,194.2044906616211,194.5429382324219,194.5429382324219,194.6221084594727,194.6221084594727,194.6221084594727,190.149284362793,190.149284362793,190.4489517211914,190.7841415405273,190.7841415405273,191.1264953613281,191.4337005615234,191.7938461303711,191.7938461303711,192.1704177856445,192.1704177856445,192.560905456543,192.9188766479492,193.3129425048828,193.3129425048828,193.7226791381836,193.7226791381836,194.0873260498047,194.0873260498047,194.0873260498047,194.4744033813477,194.4744033813477,194.7544784545898,194.7544784545898,194.7544784545898,194.7544784545898,194.7544784545898,194.7544784545898,190.47802734375,190.47802734375,190.7972259521484,190.7972259521484,190.7972259521484,191.1285400390625,191.1285400390625,191.431266784668,191.431266784668,191.7860260009766,191.7860260009766,192.164192199707,192.164192199707,192.164192199707,192.5168838500977,192.5168838500977,192.8889465332031,193.2813110351562,193.6497802734375,193.6497802734375,194.0180816650391,194.0180816650391,194.4152374267578,194.793212890625,194.793212890625,194.8847427368164,194.8847427368164,190.4775924682617,190.7543182373047,191.0344848632812,191.0344848632812,191.3388290405273,191.6539535522461,191.6539535522461,191.6539535522461,191.9958190917969,192.3572235107422,192.3572235107422,192.7304763793945,192.7304763793945,193.1196823120117,193.1196823120117,193.5171661376953,193.5171661376953,193.9274520874023,193.9274520874023,194.3430862426758,194.3430862426758,194.7526473999023,195.0127944946289,195.0127944946289,190.6043243408203,190.6043243408203,190.8849639892578,190.8849639892578,191.228157043457,191.228157043457,191.5405349731445,191.5405349731445,191.8832321166992,191.8832321166992,192.257209777832,192.6609344482422,192.6609344482422,192.6609344482422,193.0808792114258,193.0808792114258,193.4995498657227,193.4995498657227,193.9183654785156,193.9183654785156,194.3363723754883,194.3363723754883,194.7561569213867,195.1389770507812,195.1389770507812,195.1389770507812,195.1389770507812,190.9860687255859,190.9860687255859,191.2656173706055,191.2656173706055,191.5576171875,191.5576171875,191.8599395751953,192.204963684082,192.204963684082,192.204963684082,192.5694046020508,192.5694046020508,192.9624557495117,193.365348815918,193.365348815918,193.7741012573242,194.1885681152344,194.1885681152344,194.603157043457,194.603157043457,195.0148239135742,195.0148239135742,195.2629623413086,195.2629623413086,195.2629623413086,190.9966354370117,191.2736663818359,191.2736663818359,191.5668792724609,191.5668792724609,191.8666458129883,192.2122650146484,192.2122650146484,192.5771408081055,192.5771408081055,192.9694595336914,192.9694595336914,193.3786773681641,193.3786773681641,193.7869873046875,193.7869873046875,194.1990280151367,194.1990280151367,194.1990280151367,194.6157760620117,194.6157760620117,195.0335693359375,195.3850479125977,195.3850479125977,195.3850479125977,195.3850479125977,191.3665008544922,191.3665008544922,191.6525421142578,191.6525421142578,191.9240951538086,192.2202453613281,192.2202453613281,192.572883605957,192.9414520263672,193.3319931030273,193.3319931030273,193.730339050293,193.730339050293,194.1364440917969,194.549690246582,194.549690246582,194.9645156860352,194.9645156860352,195.3678817749023,195.3678817749023,195.5051040649414,195.5051040649414,195.5051040649414,191.4311599731445,191.4311599731445,191.6926574707031,191.6926574707031,191.9665603637695,191.9665603637695,192.2646484375,192.6024398803711,192.9679565429688,192.9679565429688,193.3496246337891,193.3496246337891,193.7536010742188,193.7536010742188,193.7536010742188,194.1705551147461,194.1705551147461,194.5876007080078,194.5876007080078,195.0038528442383,195.0038528442383,195.0038528442383,195.4153442382812,195.4153442382812,195.6232681274414,195.6232681274414,195.6232681274414,191.5801849365234,191.5801849365234,191.8402481079102,191.8402481079102,192.1078338623047,192.1078338623047,192.4115753173828,192.4115753173828,192.7404098510742,192.7404098510742,193.1233673095703,193.4905853271484,193.4905853271484,193.8429946899414,194.2054061889648,194.5896224975586,194.5896224975586,194.9844131469727,194.9844131469727,195.3510894775391,195.7393569946289,195.7393569946289,195.7394866943359,195.7394866943359,195.7394866943359,191.8290252685547,191.8290252685547,192.0738143920898,192.0738143920898,192.345817565918,192.345817565918,192.657096862793,192.657096862793,192.9531478881836,192.9531478881836,192.9531478881836,193.3151550292969,193.3151550292969,193.6902694702148,194.01611328125,194.4050216674805,194.4050216674805,194.8146057128906,194.8146057128906,194.8146057128906,195.1626052856445,195.1626052856445,195.5506973266602,195.5506973266602,195.8538131713867,195.8538131713867,195.8538131713867,195.8538131713867,192.0906448364258,192.0906448364258,192.0906448364258,192.3642044067383,192.3642044067383,192.6679382324219,192.6679382324219,192.9513549804688,192.9513549804688,192.9513549804688,193.3013610839844,193.6731338500977,193.6731338500977,194.041389465332,194.041389465332,194.4225234985352,194.4225234985352,194.8272094726562,194.8272094726562,194.8272094726562,195.1916351318359,195.5710296630859,195.5710296630859,195.9646072387695,195.9646072387695,195.9663772583008,195.9663772583008,195.9663772583008,192.1972274780273,192.1972274780273,192.1972274780273,192.4601364135742,192.7508316040039,192.7508316040039,193.0693588256836,193.0693588256836,193.4178161621094,193.4178161621094,193.7865142822266,193.7865142822266,194.1681747436523,194.1681747436523,194.1681747436523,194.5568313598633,194.5568313598633,194.9657287597656,194.9657287597656,195.381217956543,195.7923583984375,195.7923583984375,196.0769958496094,196.0769958496094,196.0769958496094,196.0769958496094,196.0769958496094,196.0769958496094,192.4778442382812,192.7399673461914,192.7399673461914,193.0481414794922,193.3810272216797,193.7319183349609,193.7319183349609,194.1031112670898,194.5035095214844,194.5035095214844,194.5035095214844,194.9136276245117,194.9136276245117,195.329963684082,195.7384872436523,195.7384872436523,196.1193237304688,196.1859359741211,196.1859359741211,196.1859359741211,192.5552291870117,192.7987365722656,192.7987365722656,193.0867004394531,193.0867004394531,193.4060592651367,193.4060592651367,193.7480850219727,193.7480850219727,194.1079940795898,194.1079940795898,194.4890823364258,194.4890823364258,194.8927536010742,195.3043746948242,195.3043746948242,195.7167129516602,195.7167129516602,196.1246948242188,196.2930145263672,196.2930145263672,196.2930145263672,196.2930145263672,192.6336441040039,192.6336441040039,192.8833923339844,193.1586608886719,193.1586608886719,193.4661178588867,193.4661178588867,193.7991333007812,193.7991333007812,194.151725769043,194.151725769043,194.5019149780273,194.5019149780273,194.8657455444336,195.2529678344727,195.2529678344727,195.6617126464844,196.0733032226562,196.0733032226562,196.3984756469727,196.3984756469727,196.3984756469727,196.3984756469727,196.3984756469727,196.3984756469727,192.9451217651367,192.9451217651367,192.9451217651367,193.1969223022461,193.1969223022461,193.4703674316406,193.8052825927734,193.8052825927734,194.1357040405273,194.4912185668945,194.4912185668945,194.8676452636719,194.8676452636719,194.8676452636719,195.2721786499023,195.6862564086914,195.6862564086914,196.1019134521484,196.5021743774414,196.5021743774414,196.5021743774414,196.5021743774414,196.5021743774414,196.5021743774414,193.0569000244141,193.0569000244141,193.3004379272461,193.3004379272461,193.5794448852539,193.5794448852539,193.8836898803711,193.8836898803711,194.2170791625977,194.5710144042969,194.5710144042969,194.866340637207,195.2220458984375,195.2220458984375,195.5854568481445,195.5854568481445,195.973991394043,195.973991394043,196.3538513183594,196.3538513183594,196.6041488647461,196.6041488647461,196.6041488647461,196.6041488647461,193.2716217041016,193.2716217041016,193.5115509033203,193.7812652587891,194.0802688598633,194.4101638793945,194.7634201049805,195.1378326416016,195.1378326416016,195.1378326416016,195.5310363769531,195.5310363769531,195.9177856445312,195.9177856445312,196.3142547607422,196.3142547607422,196.6996002197266,196.7046356201172,196.7046356201172,196.7046356201172,193.3769683837891,193.3769683837891,193.6145629882812,193.8827667236328,194.1729278564453,194.1729278564453,194.4963989257812,194.8460540771484,194.8460540771484,195.2194671630859,195.2194671630859,195.6084976196289,195.6084976196289,196.0070266723633,196.0070266723633,196.0070266723633,196.4207916259766,196.4207916259766,196.8033294677734,196.8033294677734,196.8033294677734,196.8033294677734,196.8033294677734,196.8033294677734,193.5259552001953,193.5259552001953,193.7680740356445,193.7680740356445,194.0372467041016,194.0372467041016,194.3341369628906,194.3341369628906,194.6670150756836,194.6670150756836,195.0290298461914,195.0290298461914,195.4047698974609,195.4047698974609,195.8087387084961,196.2237319946289,196.6397399902344,196.6397399902344,196.6397399902344,196.9005126953125,196.9005126953125,196.9005126953125,196.9005126953125,196.9005126953125,196.9005126953125,196.9005126953125,196.9005126953125,196.9005126953125,196.9005126953125,196.9005126953125,196.9005126953125,196.9005126953125,196.9005126953125,196.9005126953125,196.9005126953125,196.9005126953125,196.9005126953125,196.9005126953125,196.9005126953125,196.9005126953125,196.9005126953125,196.9005126953125,196.9005126953125,196.9005126953125,196.9005126953125,196.9005126953125,196.9005126953125,196.9005126953125,196.9005126953125,196.9005126953125,196.9005126953125,196.9005126953125,196.9005126953125,196.9005126953125,196.9005126953125,196.9005126953125,196.9005126953125,196.9005126953125,193.5594329833984,193.5594329833984,193.7482833862305,193.7482833862305,193.9679412841797,193.9679412841797,194.2032623291016,194.2032623291016,194.4523086547852,194.738395690918,195.0590515136719,195.0590515136719,195.3854598999023,195.3854598999023,195.7142639160156,196.0613555908203,196.4347686767578,196.4347686767578,196.8454055786133,196.8454055786133,196.8454055786133,196.9957809448242,196.9957809448242,196.9957809448242,193.730094909668,193.9646148681641,193.9646148681641,194.2231216430664,194.5083770751953,194.5083770751953,194.827392578125,195.1713485717773,195.1713485717773,195.1713485717773,195.5638809204102,195.5638809204102,195.9309768676758,195.9309768676758,196.3243789672852,196.3243789672852,196.7364273071289,196.7364273071289,196.7364273071289,197.0898284912109,197.0898284912109,197.0898284912109,197.0898284912109,197.0898284912109,197.0898284912109,193.9982604980469,193.9982604980469,194.2398910522461,194.2398910522461,194.5049285888672,194.8031692504883,194.8031692504883,195.13818359375,195.13818359375,195.4915618896484,195.8597259521484,195.8597259521484,196.2568130493164,196.6655120849609,196.6655120849609,197.0822525024414,197.0822525024414,197.1824493408203,197.1824493408203,194.0476913452148,194.0476913452148,194.2772369384766,194.2772369384766,194.5367889404297,194.5367889404297,194.8257522583008,195.1516799926758,195.5076599121094,195.5076599121094,195.8734130859375,196.263801574707,196.263801574707,196.6710815429688,196.6710815429688,197.0892791748047,197.0892791748047,197.2734832763672,197.2734832763672,197.2734832763672,194.1424942016602,194.1424942016602,194.3755493164062,194.3755493164062,194.6273345947266,194.6273345947266,194.8949890136719,195.2371444702148,195.5791015625,195.5791015625,195.9368896484375,195.9368896484375,196.3094253540039,196.3094253540039,196.7115173339844,197.1275253295898,197.1275253295898,197.3631439208984,197.3631439208984,197.3631439208984,197.3631439208984,197.3631439208984,197.3631439208984,194.4836044311523,194.4836044311523,194.7342147827148,194.7342147827148,195.0105743408203,195.0105743408203,195.3210296630859,195.6626358032227,195.6626358032227,195.6626358032227,196.0223693847656,196.0223693847656,196.0223693847656,196.4010162353516,196.4010162353516,196.8055648803711,197.2210922241211,197.4512557983398,197.4512557983398,197.4512557983398,197.4512557983398,197.4512557983398,197.4512557983398,194.603401184082,194.8310852050781,194.8310852050781,195.0918579101562,195.0918579101562,195.3600997924805,195.3600997924805,195.6465301513672,195.6465301513672,195.9741821289062,196.3115310668945,196.6229019165039,196.9761276245117,196.9761276245117,197.378776550293,197.5380020141602,197.5380020141602,197.5380020141602,197.5380020141602,194.7172927856445,194.7172927856445,194.9428024291992,194.9428024291992,195.1909255981445,195.1909255981445,195.4718475341797,195.4718475341797,195.7819213867188,195.7819213867188,196.1144332885742,196.1144332885742,196.4636154174805,196.8287811279297,197.212272644043,197.6226348876953,197.6233520507812,197.6233520507812,197.6233520507812,194.7731475830078,194.7731475830078,194.7731475830078,195.0044021606445,195.0044021606445,195.2611236572266,195.2611236572266,195.5504837036133,195.5504837036133,195.871955871582,195.871955871582,196.2209777832031,196.2209777832031,196.5775604248047,196.5775604248047,196.9478378295898,196.9478378295898,197.3428497314453,197.3428497314453,197.707275390625,197.707275390625,197.707275390625,197.707275390625,197.707275390625,197.707275390625,194.9254531860352,195.1597137451172,195.4445114135742,195.4445114135742,195.7385406494141,195.7385406494141,196.0607528686523,196.0607528686523,196.4073486328125,196.4073486328125,196.7591094970703,197.1283264160156,197.1283264160156,197.5285720825195,197.5285720825195,197.7898712158203,197.7898712158203,197.7898712158203,197.7898712158203,197.7898712158203,197.7898712158203,195.1206436157227,195.1206436157227,195.1206436157227,195.3535690307617,195.6173629760742,195.9152450561523,195.9152450561523,196.2487564086914,196.5879745483398,196.5879745483398,196.9457702636719,196.9457702636719,196.9457702636719,197.3201293945312,197.7234573364258,197.7234573364258,197.8711013793945,197.8711013793945,195.0854644775391,195.3172225952148,195.5578994750977,195.8376083374023,195.8376083374023,196.1539916992188,196.1539916992188,196.5040664672852,196.5040664672852,196.8694458007812,196.8694458007812,197.2581024169922,197.2581024169922,197.6671371459961,197.6671371459961,197.9510650634766,197.9510650634766,197.9510650634766,197.9510650634766,197.9510650634766,197.9510650634766,197.9510650634766,197.9510650634766,195.3880844116211,195.3880844116211,195.6300964355469,195.6300964355469,195.9052810668945,195.9052810668945,196.2196655273438,196.5664215087891,196.5664215087891,196.9330368041992,196.9330368041992,197.3125991821289,197.7200393676758,197.7200393676758,198.0297164916992,198.0297164916992,198.0297164916992,198.0297164916992,198.0297164916992,198.0297164916992,195.4726638793945,195.7121810913086,195.9778594970703,196.2822341918945,196.6235580444336,196.6235580444336,196.9880676269531,196.9880676269531,197.3621139526367,197.3621139526367,197.7718505859375,197.7718505859375,198.1070709228516,198.1070709228516,198.1070709228516,198.1070709228516,198.1070709228516,198.1070709228516,195.5775375366211,195.5775375366211,195.8156509399414,195.8156509399414,196.0848159790039,196.0848159790039,196.3881072998047,196.7165298461914,197.0551986694336,197.4135894775391,197.7789306640625,198.1721267700195,198.1721267700195,198.1832046508789,198.1832046508789,198.1832046508789,195.6545715332031,195.8876266479492,195.8876266479492,196.1466064453125,196.4398956298828,196.7652282714844,197.1161117553711,197.1161117553711,197.4786529541016,197.4786529541016,197.8531799316406,197.8531799316406,198.2514419555664,198.2514419555664,198.2581253051758,198.2581253051758,198.2581253051758,195.7500839233398,195.7500839233398,195.9813919067383,195.9813919067383,196.2363891601562,196.2363891601562,196.5258560180664,196.8489303588867,196.8489303588867,197.2018585205078,197.5642242431641,197.9481582641602,197.9481582641602,198.3318099975586,198.3318099975586,198.3318099975586,198.3318099975586,195.8789749145508,195.8789749145508,196.114128112793,196.114128112793,196.114128112793,196.3764801025391,196.3764801025391,196.6735458374023,196.6735458374023,196.6735458374023,197.0052032470703,197.0052032470703,197.3611679077148,197.7281341552734,198.1143569946289,198.404296875,198.404296875,198.404296875,198.404296875,198.404296875,198.404296875,196.0776824951172,196.0776824951172,196.0776824951172,196.3173675537109,196.3173675537109,196.5882873535156,196.5882873535156,196.8946838378906,196.8946838378906,197.2294769287109,197.2294769287109,197.5832595825195,197.5832595825195,197.9494094848633,198.3190078735352,198.3190078735352,198.4757232666016,198.4757232666016,198.4757232666016,198.4757232666016,198.4757232666016,198.4757232666016,196.2099380493164,196.4443435668945,196.4443435668945,196.7102737426758,197.0114593505859,197.0114593505859,197.3338088989258,197.3338088989258,197.684700012207,198.0436096191406,198.0436096191406,198.4042587280273,198.4042587280273,198.5458374023438,198.5458374023438,198.5458374023438,198.5458374023438,198.5458374023438,198.5458374023438,198.5458374023438,198.5458374023438,196.3132019042969,196.3132019042969,196.5484008789062,196.5484008789062,196.8091125488281,196.8091125488281,197.106071472168,197.434814453125,197.8202133178711,197.8202133178711,197.8202133178711,198.1780014038086,198.1780014038086,198.5572357177734,198.5572357177734,198.6149368286133,198.6149368286133,198.6149368286133,198.6149368286133,198.6149368286133,198.6149368286133,198.6149368286133,198.6149368286133,198.6149368286133,198.6149368286133,198.6149368286133,198.6149368286133,198.6149368286133,198.6149368286133,198.6149368286133,198.6149368286133,198.6149368286133,198.6149368286133,198.6149368286133,198.6149368286133,198.6149368286133,198.6149368286133,198.6149368286133,198.6149368286133,198.6149368286133,198.6149368286133,198.6149368286133,198.6149368286133,198.6149368286133,198.6149368286133,196.2689437866211,196.452507019043,196.452507019043,196.6645126342773,196.6645126342773,196.9005737304688,197.1595001220703,197.1595001220703,197.4487380981445,197.4487380981445,197.7724838256836,197.7724838256836,198.1200561523438,198.1200561523438,198.4826126098633,198.4826126098633,198.6826782226562,198.6826782226562,198.6826782226562,198.6826782226562,198.6826782226562,198.6826782226562,196.5283279418945,196.5283279418945,196.5283279418945,196.7625885009766,196.7625885009766,197.0282974243164,197.0282974243164,197.3349990844727,197.3349990844727,197.3349990844727,197.6782302856445,197.6782302856445,197.6782302856445,198.0372543334961,198.0372543334961,198.0372543334961,198.4073715209961,198.7495574951172,198.7495574951172,198.7495574951172,198.7495574951172,196.5445251464844,196.7759170532227,196.7759170532227,197.0307083129883,197.0307083129883,197.3235855102539,197.3235855102539,197.3235855102539,197.6556015014648,197.6556015014648,197.9534072875977,197.9534072875977,198.1481399536133,198.1481399536133,198.362907409668,198.362907409668,198.5622711181641,198.5622711181641,198.8153533935547,198.8153533935547,198.8153533935547,198.8153533935547,196.5680541992188,196.764762878418,196.9946365356445,197.2427749633789,197.2427749633789,197.5251235961914,197.5251235961914,197.5251235961914,197.8450164794922,197.8450164794922,198.1896667480469,198.1896667480469,198.1896667480469,198.5516967773438,198.5516967773438,198.8801422119141,198.8801422119141,198.8801422119141,198.8801422119141,198.8801422119141,198.8801422119141,196.7246551513672,196.9533462524414,197.2018356323242,197.2018356323242,197.4892654418945,197.4892654418945,197.8085708618164,198.1575317382812,198.514274597168,198.8811264038086,198.8811264038086,198.9437866210938,198.9437866210938,198.9437866210938,196.7621078491211,196.7621078491211,196.9674377441406,196.9674377441406,197.1544570922852,197.1544570922852,197.401741027832,197.401741027832,197.401741027832,197.6803894042969,197.6803894042969,197.6803894042969,197.989372253418,197.989372253418,198.2949142456055,198.2949142456055,198.6424942016602,198.6424942016602,198.9539642333984,198.9539642333984,199.0064468383789,199.0064468383789,199.0064468383789,199.0064468383789,199.0064468383789,199.0064468383789,197.0165863037109,197.2456359863281,197.4940567016602,197.7705459594727,197.7705459594727,198.0753936767578,198.0753936767578,198.4085845947266,198.4085845947266,198.7392349243164,199.0680770874023,199.0680770874023,199.0680770874023,199.0680770874023,196.9639739990234,197.1514892578125,197.1514892578125,197.3861083984375,197.3861083984375,197.6383209228516,197.6383209228516,197.9257507324219,198.2443466186523,198.2443466186523,198.5893936157227,198.5893936157227,198.9382476806641,199.1287612915039,199.1287612915039,199.1287612915039,199.1287612915039,199.1287612915039,199.1287612915039,197.134407043457,197.3547821044922,197.3547821044922,197.598014831543,197.8222045898438,198.1005783081055,198.350456237793,198.350456237793,198.6046524047852,198.897346496582,198.897346496582,199.1430358886719,199.1430358886719,199.1430358886719,199.1884613037109,199.1884613037109,199.1884613037109,199.1884613037109,197.2225875854492,197.2225875854492,197.4324111938477,197.4324111938477,197.6891098022461,197.9260025024414,197.9260025024414,198.1941680908203,198.1941680908203,198.1941680908203,198.5054244995117,198.5054244995117,198.8398971557617,198.8398971557617,199.1764678955078,199.1764678955078,199.1764678955078,199.2471618652344,199.2471618652344,199.2471618652344,199.2471618652344,199.2471618652344,199.2471618652344,197.4194641113281,197.6528930664062,197.6528930664062,197.9142150878906,197.9142150878906,197.9142150878906,198.2082748413086,198.5257263183594,198.5257263183594,198.8692932128906,198.8692932128906,199.2276382446289,199.2276382446289,199.3049011230469,199.3049011230469,199.3049011230469,199.3049011230469,197.5087661743164,197.5087661743164,197.7230453491211,197.9762191772461,197.9762191772461,197.9762191772461,198.2621002197266,198.2621002197266,198.567253112793,198.567253112793,198.8960876464844,198.8960876464844,199.2494506835938,199.2494506835938,199.3617935180664,199.3617935180664,199.3617935180664,199.3617935180664,199.3617935180664,199.3617935180664,197.5784378051758,197.5784378051758,197.813102722168,197.813102722168,198.0635070800781,198.3610458374023,198.3610458374023,198.6925888061523,198.6925888061523,199.0315628051758,199.0315628051758,199.0315628051758,199.3759994506836,199.3759994506836,199.4177169799805,199.4177169799805,199.4177169799805,199.4177169799805,197.6935653686523,197.9262619018555,197.9262619018555,198.1933898925781,198.1933898925781,198.4421615600586,198.4421615600586,198.7741470336914,199.1312789916992,199.1312789916992,199.1312789916992,199.4727325439453,199.4727325439453,199.4727325439453,199.4727325439453,199.4727325439453,199.4727325439453,197.5934829711914,197.5934829711914,197.8153381347656,198.0539474487305,198.0539474487305,198.0539474487305,198.3529434204102,198.3529434204102,198.3529434204102,198.6235046386719,198.9540023803711,199.3021392822266,199.5268707275391,199.5268707275391,199.5268707275391,199.5268707275391,199.5268707275391,199.5268707275391,199.5268707275391,199.5268707275391,199.5268707275391,199.5268707275391,199.5268707275391,199.5268707275391,199.5268707275391,199.5268707275391,199.5268707275391,199.5268707275391,199.5268707275391,199.5268707275391,197.6640319824219,197.6640319824219,197.6640319824219,197.7553253173828,197.7553253173828,197.9632415771484,197.9632415771484,197.9632415771484,198.1981964111328,198.1981964111328,198.4560089111328,198.7481079101562,198.7481079101562,199.0764465332031,199.0764465332031,199.0764465332031,199.4160614013672,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,199.5798797607422,197.7473220825195,197.7473220825195,197.7473220825195,197.7473220825195,197.7473220825195,197.7473220825195,197.7473373413086,197.7473373413086,197.7473373413086,197.9857788085938,197.9857788085938,198.2412719726562,198.5252075195312,198.5252075195312,198.8418121337891,198.8418121337891,199.1625213623047,199.1625213623047,199.4734115600586,199.8213272094727,199.8213272094727,200.1939697265625,200.6012649536133,200.6012649536133,200.9784164428711,201.3156127929688,201.6516876220703,201.6516876220703,201.6516876220703,201.9835357666016,201.9835357666016,202.3107070922852,202.6450881958008,202.983512878418,202.983512878418,203.3147048950195,203.3147048950195,203.6514358520508,203.6514358520508,204.023063659668,204.023063659668,204.3603668212891,204.6977386474609,205.0339736938477,205.0339736938477,205.0339736938477,205.3705749511719,205.3705749511719,205.39404296875,205.39404296875,205.39404296875,205.39404296875,205.39404296875,205.39404296875,198.2682113647461,198.2682113647461,198.5330047607422,198.5330047607422,198.8334274291992,199.1648941040039,199.4921264648438,199.4921264648438,199.4921264648438,199.8243103027344,199.8243103027344,200.1936798095703,200.1936798095703,200.5791625976562,200.9844131469727,201.3975830078125,201.8050689697266,201.8050689697266,202.2181854248047,202.6175155639648,202.6175155639648,202.6175155639648,203.0204467773438,203.0204467773438,203.4258041381836,203.4258041381836,203.8318481445312,203.8318481445312,204.2474899291992,204.2474899291992,204.6615600585938,205.0749359130859,205.4704055786133,205.4704055786133,205.6031112670898,205.6031112670898,205.6031112670898,205.6031112670898,198.4545211791992,198.4545211791992,198.6919097900391,198.6919097900391,198.6919097900391,198.9518356323242,199.2260284423828,199.2260284423828,199.5178756713867,199.5178756713867,199.7986679077148,199.7986679077148,200.1218338012695,200.1218338012695,200.4687881469727,200.4687881469727,200.8151397705078,201.1733245849609,201.1733245849609,201.5280990600586,201.5280990600586,201.8905258178711,202.2543487548828,202.6207885742188,202.6207885742188,203.0010452270508,203.0010452270508,203.3836059570312,203.3836059570312,203.3836059570312,203.7806854248047,204.1830520629883,204.1830520629883,204.5891723632812,204.9921951293945,204.9921951293945,205.3952560424805,205.3952560424805,205.7900161743164,205.8089065551758,205.8089065551758,205.8089065551758,205.8089065551758,198.8607406616211,198.8607406616211,198.8607406616211,199.1141357421875,199.1141357421875,199.3962631225586,199.3962631225586,199.6872253417969,199.6872253417969,199.9827041625977,199.9827041625977,200.3182144165039,200.3182144165039,200.6756744384766,200.6756744384766,201.0400161743164,201.420036315918,201.420036315918,201.8099594116211,201.8099594116211,201.8099594116211,202.2105484008789,202.2105484008789,202.6201324462891,202.6201324462891,203.0256500244141,203.0256500244141,203.4341659545898,203.4341659545898,203.4341659545898,203.8430023193359,203.8430023193359,204.2506332397461,204.6582641601562,205.0678253173828,205.4807205200195,205.8771438598633,205.8771438598633,205.8771438598633,206.0113754272461,206.0113754272461,206.0113754272461,206.0113754272461,206.0113754272461,206.0113754272461,199.0993881225586,199.0993881225586,199.3488082885742,199.3488082885742,199.6136016845703,199.8978652954102,199.8978652954102,200.1791000366211,200.1791000366211,200.4970932006836,200.4970932006836,200.8443374633789,200.8443374633789,201.1972274780273,201.1972274780273,201.5881958007812,201.5881958007812,201.5881958007812,201.9590148925781,202.3490295410156,202.3490295410156,202.747184753418,202.747184753418,203.1427993774414,203.5331802368164,203.5331802368164,203.923454284668,203.923454284668,204.317138671875,204.7089004516602,205.1087417602539,205.1087417602539,205.5048065185547,205.5048065185547,205.8855972290039,205.8855972290039,206.2105560302734,206.2105560302734,206.2105560302734,206.2105560302734,206.2105560302734,206.2105560302734,206.2105560302734,206.2105560302734,206.2105560302734,199.4856109619141,199.4856109619141,199.734992980957,199.9965057373047,200.2680511474609,200.2680511474609,200.557975769043,200.557975769043,200.8932418823242,200.8932418823242,201.2443923950195,201.2443923950195,201.6011352539062,201.6011352539062,201.960205078125,202.329231262207,202.6997680664062,203.0823287963867,203.0823287963867,203.4615783691406,203.8997955322266,204.2992477416992,204.2992477416992,204.6879119873047,205.0847091674805,205.0847091674805,205.4927139282227,205.8933258056641,206.2842864990234,206.4065246582031,206.4065246582031,206.4065246582031,206.4065246582031,199.680534362793,199.9206619262695,200.1727447509766,200.4358520507812,200.7090682983398,201.0385971069336,201.0385971069336,201.3868789672852,201.3868789672852,201.7402954101562,201.7402954101562,202.1032257080078,202.4776916503906,202.8677749633789,203.2541122436523,203.2541122436523,203.6537399291992,204.0539932250977,204.0539932250977,204.4445495605469,204.4445495605469,204.8432846069336,205.232795715332,205.232795715332,205.232795715332,205.632926940918,206.0283813476562,206.0283813476562,206.4037933349609,206.5992965698242,206.5992965698242,206.5992965698242,206.5992965698242,206.5992965698242,206.5992965698242,206.5992965698242,206.5992965698242,206.5992965698242,206.5992965698242,206.5992965698242,206.5992965698242,206.5992965698242,206.5992965698242,206.5992965698242,206.5992965698242,199.9648590087891,199.9648590087891,199.9648590087891,199.9648590087891,200.031623840332,200.031623840332,200.2550201416016,200.2550201416016,200.4984588623047,200.7397003173828,200.7397003173828,200.7397003173828,201.0037612915039,201.0037612915039,201.3155822753906,201.3155822753906,201.6345977783203,201.6345977783203,201.9643783569336,201.9643783569336,202.3029403686523,202.7145156860352,202.7145156860352,203.1113052368164,203.5102615356445,203.5102615356445,203.9105911254883,204.3148193359375,204.3148193359375,204.7204208374023,205.1239700317383,205.1239700317383,205.1239700317383,205.529182434082,205.9359359741211,206.3426895141602,206.7483901977539,206.7889862060547,206.7889862060547,206.7889862060547,206.7889862060547,200.3155822753906,200.3155822753906,200.5605087280273,200.5605087280273,200.8060684204102,201.0621871948242,201.0621871948242,201.3622512817383,201.6979904174805,201.6979904174805,202.048210144043,202.048210144043,202.048210144043,202.4037246704102,202.4037246704102,202.7690887451172,202.7690887451172,203.1486358642578,203.1486358642578,203.1486358642578,203.5265960693359,203.5265960693359,203.5265960693359,203.901985168457,203.901985168457,204.2885589599609,204.6863479614258,204.6863479614258,205.0832748413086,205.0832748413086,205.492431640625,205.492431640625,205.9060974121094,206.3190689086914,206.7341537475586,206.7341537475586,206.9755935668945,206.9755935668945,206.9755935668945,206.9755935668945,206.9755935668945,206.9755935668945,206.9755935668945,206.9755935668945,200.5579986572266,200.7992782592773,200.7992782592773,201.0423126220703,201.0423126220703,201.2902755737305,201.2902755737305,201.5937271118164,201.5937271118164,201.9288940429688,202.2785415649414,202.6362152099609,202.6362152099609,203.0074844360352,203.0074844360352,203.3929901123047,203.7903366088867,203.7903366088867,204.1900405883789,204.1900405883789,204.1900405883789,212.2120208740234,212.2120208740234,212.2120208740234,212.2120208740234,212.2120208740234,212.2120208740234,212.2120208740234,212.2120208740234,212.2120208740234,212.2120208740234,212.2120208740234,212.2120208740234,212.2120208740234,212.2120208740234,212.2120208740234,212.2120208740234,212.2120208740234,212.2120208740234,212.2120208740234,212.2120208740234,212.2120208740234,212.2120208740234,219.8414154052734,219.8414154052734,219.841423034668,219.841423034668,219.841423034668,219.841423034668,219.841423034668,219.841423034668,219.841423034668,219.841423034668,219.841423034668,219.841423034668,219.841423034668,219.841423034668,219.841423034668,219.841423034668,219.841423034668,219.841423034668,219.841423034668,219.841423034668,219.841423034668,219.841423034668,219.841423034668,219.841423034668,219.841423034668,219.841423034668,235.100212097168,235.100212097168,235.100212097168,235.100212097168,235.100212097168,235.100212097168,235.100212097168,235.100212097168,235.100212097168,235.100212097168,235.100212097168,235.100212097168,235.100212097168,235.100212097168,235.100212097168,235.100212097168,235.100212097168,235.100212097168,235.100212097168,235.100212097168,242.7801513671875,242.7801513671875,242.7801513671875,242.7801513671875,242.7801513671875,242.7801513671875,242.7801513671875,242.7801513671875,242.7801513671875,242.7801513671875,242.7801513671875,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258,258.1248245239258],"meminc":[0,0,0,0,15.28223419189453,0,0,0,0.0003662109375,0,0,30.46537780761719,0,0,0,0,0,4.57763671875e-05,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-0.00030517578125,0,0,0,15.4599609375,0,0,0.2476272583007812,0.2441940307617188,0,0.2251358032226562,0,0.1542587280273438,0,0.1827316284179688,0.1341629028320312,0,0.1444168090820312,0,0.1498565673828125,0.1502304077148438,0,0,0.161590576171875,0.1758270263671875,0.311187744140625,0.3237075805664062,0,0.3669586181640625,0,0.08400726318359375,0,0,-2.965736389160156,0,0,0.329010009765625,0,0,0.338714599609375,0.2648696899414062,0.375762939453125,0,0.3900604248046875,0,0.2472686767578125,0,0.365325927734375,0,0,0.3807601928710938,0,0.2827072143554688,0,0.0609130859375,0,0,-2.754188537597656,0,0.3261032104492188,0.2704925537109375,0.3699264526367188,0,0.310943603515625,0,0.1942977905273438,0.3295516967773438,0.3783187866210938,0.30810546875,0,0.353546142578125,0,0,0,-2.840713500976562,0,0.2472305297851562,0,0.3448104858398438,0.3565673828125,0.3573379516601562,0.3360366821289062,0.3795547485351562,0.3435821533203125,0.2907333374023438,0,0.2703933715820312,0,0,0,0,0,-2.754768371582031,0,0.2867431640625,0,0.301116943359375,0,0.265533447265625,0,0.3067703247070312,0.3512115478515625,0.2739181518554688,0.32708740234375,0.3284912109375,0,0.3192062377929688,0,0.07897186279296875,0,0,-2.673507690429688,0,0.3077468872070312,0,0.3090286254882812,0,0.34271240234375,0,0,0.3509445190429688,0,0.3541412353515625,0,0.3447647094726562,0,0.3478622436523438,0,0.3232269287109375,0.075927734375,0,0,-2.684196472167969,0.3005447387695312,0,0.2847900390625,0,0.2930450439453125,0,0.3506546020507812,0.3109130859375,0,0.3196945190429688,0,0.35693359375,0,0,0.3248672485351562,0.2242355346679688,0,-2.724105834960938,0,0.29925537109375,0,0.2926254272460938,0.3382110595703125,0.3579177856445312,0,0.3180770874023438,0.3526458740234375,0.4016647338867188,0.351104736328125,0,0.09284210205078125,0,0,-2.510124206542969,0,0.3346710205078125,0.3290786743164062,0.357666015625,0.366455078125,0,0.34722900390625,0,0.3735809326171875,0,0.3976516723632812,0,0.0826873779296875,0,-2.474388122558594,0,0,0.3511276245117188,0,0.3444366455078125,0,0.3373336791992188,0.3563232421875,0,0.375518798828125,0,0.3448333740234375,0,0,0.3729171752929688,0,0.069610595703125,0,-2.420150756835938,0,0.3192596435546875,0.343902587890625,0,0.3532562255859375,0,0.353240966796875,0.3631210327148438,0.3917465209960938,0,0,0.3719863891601562,0,0,-2.599464416503906,0,0.3459014892578125,0,0.3326416015625,0.3546600341796875,0,0.3636322021484375,0,0.3782958984375,0,0,0.3818359375,0,0,0.4060134887695312,0.11163330078125,0,0,0,-2.327796936035156,0.3375625610351562,0,0.358306884765625,0,0.3623580932617188,0,0.382781982421875,0.4030685424804688,0.4139480590820312,0.1437149047851562,0,-2.316490173339844,0.3391571044921875,0,0,0.3599014282226562,0,0.3714447021484375,0,0.393768310546875,0,0.4088592529296875,0,0.4203338623046875,0,0.09577178955078125,0,0,-2.232368469238281,0.3304214477539062,0.350555419921875,0,0.3718490600585938,0,0.3958511352539062,0,0.4076156616210938,0,0.4173583984375,0.03029632568359375,0,0,-2.158447265625,0,0.3158340454101562,0,0.3420944213867188,0.34112548828125,0.3607559204101562,0.379486083984375,0,0.3719024658203125,0.1176223754882812,0,-2.262435913085938,0,0.2712478637695312,0,0.2830276489257812,0.3271560668945312,0.3545913696289062,0,0,0.3044509887695312,0,0,0.3480072021484375,0,0.3647537231445312,0,0.07848358154296875,0,0,-2.192176818847656,0.3055419921875,0,0,0.3207778930664062,0,0.3372344970703125,0,0.3616409301757812,0.3780517578125,0.3601913452148438,0,0.1969375610351562,0,-2.220809936523438,0,0.2700653076171875,0,0,0.298126220703125,0,0.337493896484375,0.3530426025390625,0,0.3463516235351562,0,0.362762451171875,0.3200225830078125,0,0,-2.272201538085938,0,0.281463623046875,0,0.3083114624023438,0,0.3206100463867188,0,0.3507843017578125,0,0.3668975830078125,0,0.3666610717773438,0.3434906005859375,0,-2.259620666503906,0,0.2710952758789062,0,0,0.2728424072265625,0.3128738403320312,0.3482131958007812,0.3404006958007812,0,0.3577499389648438,0,0.3802566528320312,0,0.04107666015625,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2.13909912109375,0,0.2246017456054688,0,0.2624969482421875,0,0.2661819458007812,0,0,0.3039703369140625,0.334228515625,0,0.3419876098632812,0,0.3745346069335938,0.0947113037109375,0,0,0,-1.992050170898438,0,0.2884292602539062,0.3250503540039062,0,0.35504150390625,0.3700103759765625,0,0.3948211669921875,0,0.3216018676757812,0,-2.109634399414062,0.2796859741210938,0,0.307037353515625,0,0.3441085815429688,0,0.3669891357421875,0,0.38720703125,0,0.4020843505859375,0.0843505859375,0,0,-1.912078857421875,0,0.2901153564453125,0.327239990234375,0,0.3549880981445312,0,0.36749267578125,0.3973617553710938,0,0.2357330322265625,0,-1.988739013671875,0.2788467407226562,0,0.3136062622070312,0,0.350555419921875,0,0.3645553588867188,0.3942718505859375,0.3468475341796875,0,-2.003532409667969,0,0.2781982421875,0.310699462890625,0,0.3465652465820312,0.3658676147460938,0.3914871215820312,0,0.36956787109375,0,0,-2.005653381347656,0,0.2762298583984375,0,0.3078842163085938,0.3459243774414062,0,0.3646240234375,0.3822784423828125,0.3866729736328125,0,0,-1.993087768554688,0.2733917236328125,0,0.303924560546875,0.3449325561523438,0.3661651611328125,0.3872833251953125,0.3744049072265625,0,0,-1.947647094726562,0,0.272125244140625,0,0.3015213012695312,0.3428115844726562,0,0.3606719970703125,0,0.3708877563476562,0,0.355712890625,0,0,-1.927398681640625,0.25830078125,0,0.2931137084960938,0,0.3384246826171875,0.3621826171875,0.372589111328125,0,0.3579559326171875,0,0,-1.861564636230469,0.266357421875,0,0.3012847900390625,0,0.3420028686523438,0,0.3510971069335938,0,0.333404541015625,0,0.3217010498046875,0,0,0,-1.663764953613281,0,0.2434158325195312,0.292510986328125,0,0.323028564453125,0,0,0.3072967529296875,0.35284423828125,0,0,0.198089599609375,0,0,-1.828483581542969,0,0.233245849609375,0.267547607421875,0,0.3071365356445312,0.3357925415039062,0,0.35699462890625,0.363861083984375,0.016448974609375,0,-1.601486206054688,0,0,0.30413818359375,0.3192977905273438,0,0.3497390747070312,0,0.3700790405273438,0,0.3099136352539062,0,0,-1.754966735839844,0,0,0.2588043212890625,0,0.2942733764648438,0,0.3356857299804688,0,0.3616790771484375,0,0.3711090087890625,0,0.1843185424804688,0,-1.643699645996094,0,0,0.2643051147460938,0,0.3028564453125,0,0.3416748046875,0.3593292236328125,0,0,0.3728866577148438,0,0.0526885986328125,0,-1.530220031738281,0.280059814453125,0,0.3179779052734375,0,0.351287841796875,0.3681488037109375,0,0.2620010375976562,0,0,-1.645988464355469,0,0.2607574462890625,0.293853759765625,0,0.3141250610351562,0,0,0.330413818359375,0,0.3560256958007812,0,0.1391983032226562,0,0,-1.5364990234375,0,0.2661819458007812,0,0.3085556030273438,0.34649658203125,0.3655319213867188,0,0.2974319458007812,0,0,-1.612327575683594,0,0.2563323974609375,0,0.2960739135742188,0.3397140502929688,0.3487472534179688,0.3620529174804688,0,0.05631256103515625,0,-1.443550109863281,0,0.2674407958984375,0,0.3184738159179688,0.3510284423828125,0.3691940307617188,0.183502197265625,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.58837890625,0,0,0.0668792724609375,0,0.2770843505859375,0,0.2689971923828125,0,0.3010711669921875,0,0.317108154296875,0,0,0.3135528564453125,0.367095947265625,0.3874740600585938,0,0.410125732421875,0,0.3577651977539062,0,0,0.3332595825195312,0,0.3389816284179688,0,0,0.345794677734375,0.3368453979492188,0,0.3384475708007812,0,0.07917022705078125,0,0,-4.472824096679688,0,0.2996673583984375,0.3351898193359375,0,0.3423538208007812,0.3072052001953125,0.3601455688476562,0,0.3765716552734375,0,0.3904876708984375,0.35797119140625,0.3940658569335938,0,0.4097366333007812,0,0.3646469116210938,0,0,0.3870773315429688,0,0.2800750732421875,0,0,0,0,0,-4.276451110839844,0,0.3191986083984375,0,0,0.3313140869140625,0,0.3027267456054688,0,0.3547592163085938,0,0.3781661987304688,0,0,0.352691650390625,0,0.3720626831054688,0.392364501953125,0.36846923828125,0,0.3683013916015625,0,0.39715576171875,0.3779754638671875,0,0.09152984619140625,0,-4.407150268554688,0.2767257690429688,0.2801666259765625,0,0.3043441772460938,0.31512451171875,0,0,0.3418655395507812,0.3614044189453125,0,0.3732528686523438,0,0.3892059326171875,0,0.3974838256835938,0,0.4102859497070312,0,0.4156341552734375,0,0.4095611572265625,0.2601470947265625,0,-4.408470153808594,0,0.2806396484375,0,0.3431930541992188,0,0.3123779296875,0,0.3426971435546875,0,0.3739776611328125,0.4037246704101562,0,0,0.4199447631835938,0,0.418670654296875,0,0.4188156127929688,0,0.4180068969726562,0,0.4197845458984375,0.3828201293945312,0,0,0,-4.152908325195312,0,0.2795486450195312,0,0.2919998168945312,0,0.3023223876953125,0.3450241088867188,0,0,0.36444091796875,0,0.3930511474609375,0.40289306640625,0,0.40875244140625,0.4144668579101562,0,0.4145889282226562,0,0.4116668701171875,0,0.248138427734375,0,0,-4.266326904296875,0.2770309448242188,0,0.293212890625,0,0.2997665405273438,0.3456192016601562,0,0.3648757934570312,0,0.3923187255859375,0,0.4092178344726562,0,0.4083099365234375,0,0.4120407104492188,0,0,0.416748046875,0,0.4177932739257812,0.3514785766601562,0,0,0,-4.018547058105469,0,0.286041259765625,0,0.2715530395507812,0.2961502075195312,0,0.3526382446289062,0.3685684204101562,0.3905410766601562,0,0.398345947265625,0,0.4061050415039062,0.4132461547851562,0,0.414825439453125,0,0.4033660888671875,0,0.1372222900390625,0,0,-4.073944091796875,0,0.2614974975585938,0,0.2739028930664062,0,0.2980880737304688,0.3377914428710938,0.3655166625976562,0,0.3816680908203125,0,0.4039764404296875,0,0,0.4169540405273438,0,0.4170455932617188,0,0.4162521362304688,0,0,0.4114913940429688,0,0.2079238891601562,0,0,-4.043083190917969,0,0.2600631713867188,0,0.2675857543945312,0,0.303741455078125,0,0.3288345336914062,0,0.3829574584960938,0.367218017578125,0,0.3524093627929688,0.3624114990234375,0.38421630859375,0,0.3947906494140625,0,0.3666763305664062,0.3882675170898438,0,0.00012969970703125,0,0,-3.91046142578125,0,0.2447891235351562,0,0.272003173828125,0,0.311279296875,0,0.296051025390625,0,0,0.3620071411132812,0,0.3751144409179688,0.3258438110351562,0.3889083862304688,0,0.4095840454101562,0,0,0.3479995727539062,0,0.388092041015625,0,0.3031158447265625,0,0,0,-3.763168334960938,0,0,0.2735595703125,0,0.3037338256835938,0,0.283416748046875,0,0,0.350006103515625,0.3717727661132812,0,0.368255615234375,0,0.381134033203125,0,0.4046859741210938,0,0,0.3644256591796875,0.37939453125,0,0.3935775756835938,0,0.00177001953125,0,0,-3.769149780273438,0,0,0.262908935546875,0.2906951904296875,0,0.3185272216796875,0,0.3484573364257812,0,0.3686981201171875,0,0.3816604614257812,0,0,0.3886566162109375,0,0.4088973999023438,0,0.4154891967773438,0.4111404418945312,0,0.284637451171875,0,0,0,0,0,-3.599151611328125,0.2621231079101562,0,0.3081741333007812,0.3328857421875,0.35089111328125,0,0.3711929321289062,0.4003982543945312,0,0,0.4101181030273438,0,0.4163360595703125,0.4085235595703125,0,0.3808364868164062,0.06661224365234375,0,0,-3.630706787109375,0.2435073852539062,0,0.2879638671875,0,0.3193588256835938,0,0.3420257568359375,0,0.3599090576171875,0,0.3810882568359375,0,0.4036712646484375,0.41162109375,0,0.4123382568359375,0,0.4079818725585938,0.1683197021484375,0,0,0,-3.659370422363281,0,0.2497482299804688,0.2752685546875,0,0.3074569702148438,0,0.3330154418945312,0,0.3525924682617188,0,0.350189208984375,0,0.36383056640625,0.3872222900390625,0,0.4087448120117188,0.411590576171875,0,0.3251724243164062,0,0,0,0,0,-3.453353881835938,0,0,0.251800537109375,0,0.2734451293945312,0.3349151611328125,0,0.3304214477539062,0.3555145263671875,0,0.3764266967773438,0,0,0.4045333862304688,0.4140777587890625,0,0.4156570434570312,0.4002609252929688,0,0,0,0,0,-3.445274353027344,0,0.2435379028320312,0,0.2790069580078125,0,0.3042449951171875,0,0.3333892822265625,0.3539352416992188,0,0.2953262329101562,0.3557052612304688,0,0.3634109497070312,0,0.3885345458984375,0,0.3798599243164062,0,0.2502975463867188,0,0,0,-3.332527160644531,0,0.23992919921875,0.26971435546875,0.2990036010742188,0.32989501953125,0.3532562255859375,0.3744125366210938,0,0,0.3932037353515625,0,0.386749267578125,0,0.3964691162109375,0,0.385345458984375,0.005035400390625,0,0,-3.327667236328125,0,0.2375946044921875,0.2682037353515625,0.2901611328125,0,0.3234710693359375,0.3496551513671875,0,0.3734130859375,0,0.3890304565429688,0,0.398529052734375,0,0,0.4137649536132812,0,0.382537841796875,0,0,0,0,0,-3.277374267578125,0,0.2421188354492188,0,0.2691726684570312,0,0.2968902587890625,0,0.3328781127929688,0,0.3620147705078125,0,0.3757400512695312,0,0.4039688110351562,0.4149932861328125,0.4160079956054688,0,0,0.260772705078125,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-3.341079711914062,0,0.1888504028320312,0,0.2196578979492188,0,0.235321044921875,0,0.2490463256835938,0.2860870361328125,0.3206558227539062,0,0.3264083862304688,0,0.3288040161132812,0.3470916748046875,0.3734130859375,0,0.4106369018554688,0,0,0.1503753662109375,0,0,-3.26568603515625,0.2345199584960938,0,0.2585067749023438,0.2852554321289062,0,0.3190155029296875,0.3439559936523438,0,0,0.3925323486328125,0,0.367095947265625,0,0.393402099609375,0,0.41204833984375,0,0,0.3534011840820312,0,0,0,0,0,-3.091567993164062,0,0.2416305541992188,0,0.2650375366210938,0.2982406616210938,0,0.3350143432617188,0,0.3533782958984375,0.3681640625,0,0.3970870971679688,0.4086990356445312,0,0.4167404174804688,0,0.1001968383789062,0,-3.134757995605469,0,0.2295455932617188,0,0.259552001953125,0,0.2889633178710938,0.325927734375,0.3559799194335938,0,0.365753173828125,0.3903884887695312,0,0.4072799682617188,0,0.4181976318359375,0,0.1842041015625,0,0,-3.130989074707031,0,0.2330551147460938,0,0.2517852783203125,0,0.2676544189453125,0.3421554565429688,0.3419570922851562,0,0.3577880859375,0,0.3725357055664062,0,0.4020919799804688,0.4160079956054688,0,0.2356185913085938,0,0,0,0,0,-2.879539489746094,0,0.2506103515625,0,0.2763595581054688,0,0.310455322265625,0.3416061401367188,0,0,0.3597335815429688,0,0,0.3786468505859375,0,0.4045486450195312,0.41552734375,0.23016357421875,0,0,0,0,0,-2.847854614257812,0.2276840209960938,0,0.260772705078125,0,0.2682418823242188,0,0.2864303588867188,0,0.3276519775390625,0.3373489379882812,0.311370849609375,0.3532257080078125,0,0.40264892578125,0.1592254638671875,0,0,0,-2.820709228515625,0,0.2255096435546875,0,0.2481231689453125,0,0.2809219360351562,0,0.3100738525390625,0,0.3325119018554688,0,0.34918212890625,0.3651657104492188,0.3834915161132812,0.4103622436523438,0.0007171630859375,0,0,-2.850204467773438,0,0,0.2312545776367188,0,0.2567214965820312,0,0.2893600463867188,0,0.32147216796875,0,0.3490219116210938,0,0.3565826416015625,0,0.3702774047851562,0,0.3950119018554688,0,0.3644256591796875,0,0,0,0,0,-2.781822204589844,0.2342605590820312,0.2847976684570312,0,0.2940292358398438,0,0.3222122192382812,0,0.3465957641601562,0,0.3517608642578125,0.3692169189453125,0,0.4002456665039062,0,0.2612991333007812,0,0,0,0,0,-2.669227600097656,0,0,0.2329254150390625,0.2637939453125,0.297882080078125,0,0.3335113525390625,0.3392181396484375,0,0.3577957153320312,0,0,0.374359130859375,0.4033279418945312,0,0.14764404296875,0,-2.785636901855469,0.2317581176757812,0.2406768798828125,0.2797088623046875,0,0.3163833618164062,0,0.3500747680664062,0,0.3653793334960938,0,0.3886566162109375,0,0.4090347290039062,0,0.2839279174804688,0,0,0,0,0,0,0,-2.562980651855469,0,0.2420120239257812,0,0.2751846313476562,0,0.3143844604492188,0.3467559814453125,0,0.3666152954101562,0,0.3795623779296875,0.407440185546875,0,0.3096771240234375,0,0,0,0,0,-2.557052612304688,0.2395172119140625,0.2656784057617188,0.3043746948242188,0.3413238525390625,0,0.3645095825195312,0,0.3740463256835938,0,0.4097366333007812,0,0.3352203369140625,0,0,0,0,0,-2.529533386230469,0,0.2381134033203125,0,0.2691650390625,0,0.3032913208007812,0.3284225463867188,0.3386688232421875,0.3583908081054688,0.3653411865234375,0.3931961059570312,0,0.011077880859375,0,0,-2.528633117675781,0.2330551147460938,0,0.2589797973632812,0.2932891845703125,0.3253326416015625,0.3508834838867188,0,0.3625411987304688,0,0.3745269775390625,0,0.3982620239257812,0,0.006683349609375,0,0,-2.508041381835938,0,0.2313079833984375,0,0.2549972534179688,0,0.2894668579101562,0.3230743408203125,0,0.3529281616210938,0.36236572265625,0.3839340209960938,0,0.3836517333984375,0,0,0,-2.452835083007812,0,0.2351531982421875,0,0,0.2623519897460938,0,0.2970657348632812,0,0,0.3316574096679688,0,0.3559646606445312,0.3669662475585938,0.3862228393554688,0.2899398803710938,0,0,0,0,0,-2.326614379882812,0,0,0.23968505859375,0,0.2709197998046875,0,0.306396484375,0,0.3347930908203125,0,0.3537826538085938,0,0.36614990234375,0.369598388671875,0,0.1567153930664062,0,0,0,0,0,-2.265785217285156,0.234405517578125,0,0.26593017578125,0.3011856079101562,0,0.3223495483398438,0,0.35089111328125,0.3589096069335938,0,0.3606491088867188,0,0.1415786743164062,0,0,0,0,0,0,0,-2.232635498046875,0,0.235198974609375,0,0.260711669921875,0,0.2969589233398438,0.3287429809570312,0.3853988647460938,0,0,0.3577880859375,0,0.3792343139648438,0,0.05770111083984375,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2.345993041992188,0.183563232421875,0,0.212005615234375,0,0.2360610961914062,0.2589263916015625,0,0.2892379760742188,0,0.3237457275390625,0,0.3475723266601562,0,0.3625564575195312,0,0.2000656127929688,0,0,0,0,0,-2.154350280761719,0,0,0.2342605590820312,0,0.2657089233398438,0,0.30670166015625,0,0,0.343231201171875,0,0,0.3590240478515625,0,0,0.3701171875,0.3421859741210938,0,0,0,-2.205032348632812,0.2313919067382812,0,0.254791259765625,0,0.292877197265625,0,0,0.3320159912109375,0,0.2978057861328125,0,0.194732666015625,0,0.2147674560546875,0,0.1993637084960938,0,0.253082275390625,0,0,0,-2.247299194335938,0.1967086791992188,0.2298736572265625,0.248138427734375,0,0.2823486328125,0,0,0.3198928833007812,0,0.3446502685546875,0,0,0.362030029296875,0,0.3284454345703125,0,0,0,0,0,-2.155487060546875,0.2286911010742188,0.2484893798828125,0,0.2874298095703125,0,0.319305419921875,0.3489608764648438,0.3567428588867188,0.366851806640625,0,0.06266021728515625,0,0,-2.181678771972656,0,0.2053298950195312,0,0.1870193481445312,0,0.247283935546875,0,0,0.2786483764648438,0,0,0.3089828491210938,0,0.3055419921875,0,0.3475799560546875,0,0.3114700317382812,0,0.05248260498046875,0,0,0,0,0,-1.989860534667969,0.2290496826171875,0.2484207153320312,0.2764892578125,0,0.3048477172851562,0,0.33319091796875,0,0.3306503295898438,0.3288421630859375,0,0,0,-2.104103088378906,0.1875152587890625,0,0.234619140625,0,0.2522125244140625,0,0.2874298095703125,0.3185958862304688,0,0.3450469970703125,0,0.3488540649414062,0.1905136108398438,0,0,0,0,0,-1.994354248046875,0.2203750610351562,0,0.2432327270507812,0.2241897583007812,0.2783737182617188,0.2498779296875,0,0.2541961669921875,0.292694091796875,0,0.2456893920898438,0,0,0.0454254150390625,0,0,0,-1.965873718261719,0,0.2098236083984375,0,0.2566986083984375,0.2368927001953125,0,0.2681655883789062,0,0,0.3112564086914062,0,0.33447265625,0,0.3365707397460938,0,0,0.0706939697265625,0,0,0,0,0,-1.82769775390625,0.233428955078125,0,0.261322021484375,0,0,0.2940597534179688,0.3174514770507812,0,0.34356689453125,0,0.3583450317382812,0,0.07726287841796875,0,0,0,-1.796134948730469,0,0.2142791748046875,0.253173828125,0,0,0.2858810424804688,0,0.3051528930664062,0,0.3288345336914062,0,0.353363037109375,0,0.1123428344726562,0,0,0,0,0,-1.783355712890625,0,0.2346649169921875,0,0.2504043579101562,0.2975387573242188,0,0.33154296875,0,0.3389739990234375,0,0,0.3444366455078125,0,0.041717529296875,0,0,0,-1.724151611328125,0.232696533203125,0,0.2671279907226562,0,0.2487716674804688,0,0.3319854736328125,0.3571319580078125,0,0,0.3414535522460938,0,0,0,0,0,-1.879249572753906,0,0.2218551635742188,0.2386093139648438,0,0,0.2989959716796875,0,0,0.2705612182617188,0.3304977416992188,0.3481369018554688,0.2247314453125,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.862838745117188,0,0,0.0912933349609375,0,0.207916259765625,0,0,0.234954833984375,0,0.2578125,0.2920989990234375,0,0.328338623046875,0,0,0.3396148681640625,0.163818359375,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.832557678222656,0,0,0,0,0,1.52587890625e-05,0,0,0.2384414672851562,0,0.2554931640625,0.283935546875,0,0.3166046142578125,0,0.320709228515625,0,0.3108901977539062,0.3479156494140625,0,0.3726425170898438,0.4072952270507812,0,0.3771514892578125,0.3371963500976562,0.3360748291015625,0,0,0.33184814453125,0,0.3271713256835938,0.334381103515625,0.3384246826171875,0,0.3311920166015625,0,0.33673095703125,0,0.3716278076171875,0,0.3373031616210938,0.337371826171875,0.3362350463867188,0,0,0.3366012573242188,0,0.023468017578125,0,0,0,0,0,-7.125831604003906,0,0.2647933959960938,0,0.3004226684570312,0.3314666748046875,0.3272323608398438,0,0,0.332183837890625,0,0.3693695068359375,0,0.3854827880859375,0.4052505493164062,0.4131698608398438,0.4074859619140625,0,0.413116455078125,0.3993301391601562,0,0,0.4029312133789062,0,0.4053573608398438,0,0.4060440063476562,0,0.4156417846679688,0,0.4140701293945312,0.4133758544921875,0.3954696655273438,0,0.1327056884765625,0,0,0,-7.148590087890625,0,0.2373886108398438,0,0,0.2599258422851562,0.2741928100585938,0,0.2918472290039062,0,0.280792236328125,0,0.3231658935546875,0,0.346954345703125,0,0.3463516235351562,0.358184814453125,0,0.3547744750976562,0,0.3624267578125,0.3638229370117188,0.3664398193359375,0,0.3802566528320312,0,0.3825607299804688,0,0,0.3970794677734375,0.4023666381835938,0,0.4061203002929688,0.4030227661132812,0,0.4030609130859375,0,0.3947601318359375,0.018890380859375,0,0,0,-6.948165893554688,0,0,0.2533950805664062,0,0.2821273803710938,0,0.2909622192382812,0,0.2954788208007812,0,0.33551025390625,0,0.3574600219726562,0,0.3643417358398438,0.3800201416015625,0,0.389923095703125,0,0,0.4005889892578125,0,0.4095840454101562,0,0.405517578125,0,0.4085159301757812,0,0,0.4088363647460938,0,0.4076309204101562,0.4076309204101562,0.4095611572265625,0.4128952026367188,0.39642333984375,0,0,0.1342315673828125,0,0,0,0,0,-6.9119873046875,0,0.249420166015625,0,0.2647933959960938,0.2842636108398438,0,0.2812347412109375,0,0.3179931640625,0,0.3472442626953125,0,0.3528900146484375,0,0.3909683227539062,0,0,0.370819091796875,0.3900146484375,0,0.3981552124023438,0,0.3956146240234375,0.390380859375,0,0.3902740478515625,0,0.3936843872070312,0.3917617797851562,0.39984130859375,0,0.3960647583007812,0,0.3807907104492188,0,0.3249588012695312,0,0,0,0,0,0,0,0,-6.724945068359375,0,0.2493820190429688,0.2615127563476562,0.27154541015625,0,0.2899246215820312,0,0.33526611328125,0,0.3511505126953125,0,0.3567428588867188,0,0.35906982421875,0.3690261840820312,0.3705368041992188,0.3825607299804688,0,0.3792495727539062,0.4382171630859375,0.3994522094726562,0,0.3886642456054688,0.3967971801757812,0,0.4080047607421875,0.4006118774414062,0.390960693359375,0.1222381591796875,0,0,0,-6.725990295410156,0.2401275634765625,0.2520828247070312,0.2631072998046875,0.2732162475585938,0.32952880859375,0,0.3482818603515625,0,0.3534164428710938,0,0.3629302978515625,0.3744659423828125,0.3900833129882812,0.3863372802734375,0,0.399627685546875,0.4002532958984375,0,0.3905563354492188,0,0.3987350463867188,0.3895111083984375,0,0,0.4001312255859375,0.3954544067382812,0,0.3754119873046875,0.1955032348632812,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-6.634437561035156,0,0,0,0.06676483154296875,0,0.2233963012695312,0,0.243438720703125,0.241241455078125,0,0,0.2640609741210938,0,0.3118209838867188,0,0.3190155029296875,0,0.3297805786132812,0,0.33856201171875,0.4115753173828125,0,0.39678955078125,0.398956298828125,0,0.40032958984375,0.4042282104492188,0,0.4056015014648438,0.4035491943359375,0,0,0.40521240234375,0.4067535400390625,0.4067535400390625,0.40570068359375,0.04059600830078125,0,0,0,-6.473403930664062,0,0.2449264526367188,0,0.2455596923828125,0.2561187744140625,0,0.3000640869140625,0.3357391357421875,0,0.3502197265625,0,0,0.3555145263671875,0,0.3653640747070312,0,0.379547119140625,0,0,0.377960205078125,0,0,0.3753890991210938,0,0.3865737915039062,0.3977890014648438,0,0.3969268798828125,0,0.4091567993164062,0,0.413665771484375,0.4129714965820312,0.4150848388671875,0,0.2414398193359375,0,0,0,0,0,0,0,-6.417594909667969,0.2412796020507812,0,0.2430343627929688,0,0.2479629516601562,0,0.3034515380859375,0,0.3351669311523438,0.3496475219726562,0.3576736450195312,0,0.3712692260742188,0,0.3855056762695312,0.3973464965820312,0,0.3997039794921875,0,0,8.021980285644531,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7.62939453125,0,7.62939453125e-06,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,15.2587890625,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7.679939270019531,0,0,0,0,0,0,0,0,0,0,15.34467315673828,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"filename":["<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,null,null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,null,"<expr>","<expr>","<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,null,null,null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,null,null,null,"<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,null,null,null,null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,null,null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,null,null,null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,null,null,null,null,null,"<expr>","<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null]},"interval":10,"files":[{"filename":"<expr>","content":"## Generate Large Random Dataset\nn <- 2e6\nx <- runif(n)\ny <- runif(n)\nz <- runif(n)\nXYZ <- cbind(x,y,z)\n\n## Inspect 4 equivalent `row mean` calculations \nprofvis::profvis({\n    m <- rowSums(XYZ)/ncol(XYZ)\n    m <- rowMeans(XYZ)\n    m <- apply(XYZ, 1, mean)\n    m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }\n})\n## rowSums(), colSums(), rowMeans(), and colMeans() are vectorised and fast.\n## for loop is not the slowest, but the ugliest.","normpath":"<expr>"}],"prof_output":"/tmp/Rtmp6vpcas/filebe1d12171867.prof","highlight":{"output":["^output\\$"],"gc":["^<GC>$"],"stacktrace":["^\\.\\.stacktraceo(n|ff)\\.\\.$"]},"split":"h"}},"evals":[],"jsHooks":[]}</script>
```

```r
## rowSums(), colSums(), rowMeans(), and colMeans() are vectorised and fast.
## for loop is not the slowest, but the ugliest.
```



For easily comparing solutions to specific bottlenecks

```r
## 3 Equivalent calculations of the mean of a vector
mean1 <- function(x,p=1) mean(x^p)
mean2 <- function(x,p=1) sum(x^p) / length(x)
mean3 <- function(x,p=1) mean.default(x^p)

## Time them
x <- runif(1e6)
bench::mark(
  mean1(x,.5),
  mean2(x,.5),
  mean3(x,.5)
)
```

```
## # A tibble: 3 × 6
##   expression         min   median `itr/sec` mem_alloc `gc/sec`
##   <bch:expr>    <bch:tm> <bch:tm>     <dbl> <bch:byt>    <dbl>
## 1 mean1(x, 0.5)     20ms   21.8ms      45.8    7.63MB     2.08
## 2 mean2(x, 0.5)   19.1ms     21ms      48.0    7.63MB     0   
## 3 mean3(x, 0.5)     20ms   21.9ms      46.1    7.63MB     2.09
```

Check for easy speed-ups before creating your own program

```r
X <- cbind(1, runif(1e6))
Y <- X %*% c(1,2) + rnorm(1e6)
DAT <- as.data.frame(cbind(Y,X))

system.time({.lm.fit(X, Y) })
```

```
##    user  system elapsed 
##   0.103   0.000   0.032
```

```r
system.time({ lm(Y~X, data=DAT) })
```

```
##    user  system elapsed 
##   0.413   0.000   0.147
```

```r
## But note that quicker codes 
## tend to have fewer checks
## and return less information
```


**Vectors are generally faster and easier to read than loops**

```r
x <- runif(1e6)

## Compare 2 moving averages

## First Try
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

```r
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

```r
bench::mark(
  ma1(y),
  ma2(y)
)
```

```
## Warning: Some expressions had a GC in every iteration; so filtering is
## disabled.
```

```
## # A tibble: 2 × 6
##   expression      min   median `itr/sec` mem_alloc `gc/sec`
##   <bch:expr> <bch:tm> <bch:tm>     <dbl> <bch:byt>    <dbl>
## 1 ma1(y)      175.7ms  177.5ms      5.64    15.3MB     1.88
## 2 ma2(y)       25.6ms   27.2ms     28.8     91.6MB    28.8
```

###  Bottlenecks

Sometimes there will still be a problematic bottleneck. 



Your next step should be parallelism:

* Write the function as a general vectorized function.
* Apply the same function to every element in a list *at the same time*


```r
## lapply in parallel on {m}ultiple {c}ores
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


```r
## vectorize and compile
e_power_e_fun <- compiler::cmpfun( function(vector){ vector^vector} )

## base R
x <- 0:1E6
s_vc <- system.time( e_power_e_vec <- e_power_e_fun(x) )
s_vc
```

```
##    user  system elapsed 
##   0.026   0.003   0.029
```

```r
## brute power
x <- 0:1E6
s_bp <- system.time({
  e_power_e_mc <- unlist( parallel::mclapply(x, mc.cores=2, FUN=e_power_e_fun))
})
s_bp
```

```
##    user  system elapsed 
##   0.804   0.232   0.584
```

```r
## Same results
all(e_power_e_vec==e_power_e_mc)
```

```
## [1] TRUE
```

Parallelism does not go great with a GUI.
For identifying bottlenecks on a cluster without a GUI, try `Rprof()`

```r
Rprof( interval = 0.005)
    # Create Data
    x <- runif(2e6)
    y <- sqrt(x)
    ## Loop Format Data
    z <- y*NA
    for(i in 2:length(y)){ z[i] <- (y[i]-y[i-1])/2 }
    ## Regression
    X <- cbind(1,x)[-1,]
    Z <- z[-1]
    reg_fast <- .lm.fit(X, Z)
Rprof(NULL)
summaryRprof()
```


If you still are stuck, you can

* try [Amazon Web Server](https://aws.amazon.com/ec2/) for more brute-power 
* rewrite bottlenecks with a working C++ compiler or Fortran compiler.



##### Compiled Code


To get C++

* On Windows, install Rtools.
* On Mac, install Xcode from the app store.
* On Linux, sudo apt-get install r-base-dev or similar.

To call C++ from R use package `Rcpp`

```r
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

```r
.C
.Fortran
```
For a tutorial, see https://masuday.github.io/fortran_tutorial/r.html


##  Further Programming Guidance

https://rmd4sci.njtierney.com/
https://smac-group.github.io/ds/high-performance-computing.html
https://www.stat.umn.edu/geyer/3701/notes/arithmetic.Rmd

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



# Shiny 

First Steps with Shiny

* Download [RShiny.R](https://jadamso.github.io/Rbooks/RShiny.R) and open it with `rstudio`.
* Run the application and experiment with how larger sample sizes change the distribution. 
* Edit the application to add a `Resample` capability (remove the lines commented out by a single "#").


First Steps with Shiny Markdown

* Download [RShiny.Rmd](https://jadamso.github.io/Rbooks/RShiny.Rmd) and open it with `rstudio`.
* Run the application. 
* Edit the application to add writing that describes the code (see https://shiny.rstudio.com/articles/rmarkdown.html).



### Programming Guidance

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


## Latest versions

Make sure your packages are up to date

```r
update.packages()
```

After reinstalling, you can update *all* packages stored in *all* `.libPaths()` with the following command

```r
install.packages(old.packages(checkBuilt=T)[,"Package"])
```

To find broken packages after an update

```r
library(purrr)

set_names(.libPaths()) %>%
  map(function(lib) {
    .packages(all.available = TRUE, lib.loc = lib) %>%
        keep(function(pkg) {
            f <- system.file('Meta', 'package.rds', package = pkg, lib.loc = lib)
            tryCatch({readRDS(f); FALSE}, error = function(e) TRUE)
        })
  })
## https://stackoverflow.com/questions/31935516/installing-r-packages-error-in-readrdsfile-error-reading-from-connection/55997765
```


## Stata

For those transitioning from Stata or replicating others' Stata work, you can work with Stata data and code within R.

Translations of common procedures is provided by https://stata2r.github.io/

Many packages allows you to read data created by different programs. As of right now, `haven` is a particularly useful for reading in Stata files

```r
library(haven)
read_dta()
## See also foreign::read.dta
```

You can also execute stata commands directly in R via package `Rstata`. (Last time I checked, `Rstata` requires you to have purchased a non-student version of Stata.) Moreover, you can include stata in the markdown reports via package `Statamarkdown`:

```r
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

## General Workflow

If you want to go further down the reproducibility route (recommended, but not required for our class), consider making your entire workflow use Free Open Source Software


**Linux:** An alternative to windows and mac operating systems.
Used in computing clusters, big labs, and phones.
E.g., Ubuntu and Fedora are popular brands

* https://www.r-bloggers.com/linux-data-science-virtual-machine-new-and-upgraded-tools/,
* http://www.howtogeek.com/249966/how-to-install-and-use-the-linux-bash-shell-on-windows-10/


On Fedora, you can open RStudio on the commandline with

```bash
rstudio
```

Alternatively, you are encouraged to try using R without a GUI. E.g., on Fedora, this document can be created directly via 

```bash
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




**Sweave:** is an alternative to Rmarkdown for integrating latex and R. While Rmarkdown "writes R and latex within markdown", Sweave "write R in latex". Sweave files end in ".Rnw" and can be called within R


```r
Sweave('Sweave_file.Rnw')
```

or directly from the command line


```bash
R CMD Sweave Sweave_file.Rnw 
```

In both cases, a latex file `Sweave_file.tex` is produced, which can then be converted to `Sweave_file.pdf`.



For more on Sweave,

* https://rpubs.com/YaRrr/SweaveIntro
* https://support.rstudio.com/hc/en-us/articles/200552056-Using-Sweave-and-knitr
* https://www.statistik.lmu.de/~leisch/Sweave/Sweave-manual.pdf


**Knitr:** 
You can also produce a pdf from an .Rnw file via `knitr`


```bash
Rscript -e "knitr::Sweave2knitr('Sweave_file.Rnw')"
Rscript -e "knitr::knit2pdf('Sweave_file-knitr.Rnw')"
```

For background on knitr

* https://yihui.org/knitr/
* https://kbroman.org/knitr_knutshell/pages/latex.html
* https://sachsmc.github.io/knit-git-markr-guide/knitr/knit.html



**Misc:** 
Some other good packages for posters/presenting you should be aware of

* https://github.com/mathematicalcoffee/beamerposter-rmarkdown-example
* https://github.com/rstudio/pagedown
* https://github.com/brentthorne/posterdown
* https://odeleongt.github.io/postr/
* https://wytham.rbind.io/post/making-a-poster-in-r/
* https://www.animateyour.science/post/How-to-design-an-award-winning-conference-poster





