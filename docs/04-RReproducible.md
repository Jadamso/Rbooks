# (PART) Reproducible Research in R {-} 

You want your work to be reproducible, and we will cover some of the basics of how to do this in R. Note the distintion

* Replicable: someone collecting new data comes to the same results.
* Reproducibile: someone reusing your data comes to the same results.

Will we cover some of both below. Note that you can read more about the distinction in many places, including

* https://www.annualreviews.org/doi/10.1146/annurev-psych-020821-114157
* https://nceas.github.io/sasap-training/materials/reproducible_research_in_r_fairbanks/

# Why?
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

We will use R Markdown for reproducible research, which is a good choice:

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

Homework reports are the smallest and probably first document you create. We will create little homework reports using R markdown that are almost entirely self-contained (showing both code and output). To do this, you will need to install [Pandoc](http://pandoc.org) on your computer.

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


# Small Projects
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

See [DataScientism.html](https://jadamso.github.io/Rbooks/Templates/DataScientism.html)

Download source file from [DataScientism.Rmd](https://jadamso.github.io/Rbooks/Templates/DataScientism.Rmd)


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
<div class="plotly html-widget html-fill-item" id="htmlwidget-f6fb1d66968e5e825f52" style="width:672px;height:480px;"></div>
<script type="application/json" data-for="htmlwidget-f6fb1d66968e5e825f52">{"x":{"visdat":{"19dd713f6e3c":["function () ","plotlyVisDat"]},"cur_data":"19dd713f6e3c","attrs":{"19dd713f6e3c":{"x":{},"y":{},"alpha_stroke":1,"sizes":[10,100],"spans":[1,20]}},"layout":{"margin":{"b":40,"l":60,"t":25,"r":10},"xaxis":{"domain":[0,1],"automargin":true,"title":"X"},"yaxis":{"domain":[0,1],"automargin":true,"title":"Y"},"hovermode":"closest","showlegend":false},"source":"A","config":{"modeBarButtonsToAdd":["hoverclosest","hovercompare"],"showSendToCloud":false},"data":[{"x":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100],"y":[3.5623904890415181,6.670913494555486,10.244536057062014,16.583406896999445,22.020561529358641,27.452914075207399,26.924650486981015,30.794914208468164,33.305468768402584,39.176783010540582,43.076083818022859,45.143661328586163,53.444819368319656,57.746105213694314,57.124809182031711,64.488403428282766,68.679008856047545,72.986736604753858,77.720449959409365,82.83153706435742,86.276821746518991,85.33932094933887,95.979362426534166,96.196733579391079,99.115577221675906,105.01426881781688,108.74634197407296,110.52357855511096,115.32912567478385,119.15756107950423,123.51973201621387,129.86194728264613,131.91289035771919,134.01959474164116,141.43704958461288,143.29416014275421,148.21089277069635,149.19567608615114,160.59898710897681,158.98841901458403,163.77812455058259,167.09335956419301,174.55297223761312,176.80337053435804,184.71265198160052,186.00908031076324,186.12832124467729,187.99697047439827,197.39337219921163,202.15319988377885,202.82343430190235,207.64399436499616,212.04937718622793,218.96943283036524,220.83322392733047,223.48403788288283,225.85256146888844,232.85602843794186,236.10863869247186,240.11147614798813,241.91379415100585,247.90918795967681,251.11509934306758,257.39510350294677,259.78629027174685,263.57442876233233,268.55290959876561,270.86125433140177,276.66405315465079,280.95073521031719,286.97081161895426,287.12340832155172,295.24731295144034,294.09672662756566,302.85444265933046,303.75948719965368,309.95562413209268,309.55279529756592,314.99909269650453,320.02765610866027,326.4296051068626,328.34798967209963,330.52963105623394,336.46131249782894,338.76291809674706,345.78736888082454,350.86878609337288,351.79723036732156,352.0890469516786,362.99140698864863,365.21936194056599,369.13926145815384,370.73670896177765,378.29256653439683,379.76169899250101,380.51131026874936,386.76860356886067,393.67648045895396,397.55096715529839,398.39186435523419],"type":"scatter","mode":"markers","marker":{"color":"rgba(31,119,180,1)","line":{"color":"rgba(31,119,180,1)"}},"error_y":{"color":"rgba(31,119,180,1)"},"error_x":{"color":"rgba(31,119,180,1)"},"line":{"color":"rgba(31,119,180,1)"},"xaxis":"x","yaxis":"y","frame":null}],"highlight":{"on":"plotly_click","persistent":false,"dynamic":false,"selectize":false,"opacityDim":0.20000000000000001,"selected":{"opacity":1},"debounce":0},"shinyEvents":["plotly_hover","plotly_click","plotly_selected","plotly_relayout","plotly_brushed","plotly_brushing","plotly_clickannotation","plotly_doubleclick","plotly_deselect","plotly_afterplot","plotly_sunburstclick"],"base_url":"https://plot.ly"},"evals":[],"jsHooks":[]}</script>
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

Posters and presentations are another important type of scientific document. R markdown is good at creating both of these, and actually *very* good with some additional packages. So we will also use [flexdashboard](https://pkgs.rstudio.com/flexdashboard/) for posters and [beamer]( https://bookdown.org/yihui/rmarkdown/beamer-presentation.html) for presentions. Since beamer is a pdf output, you will need to install [TinyTex](https://yihui.org/tinytex/), which can be done within R

```r
install.packages('tinytex')
tinytex::install_tinytex()  # install TinyTeX
```

See

* [DataScientism_Slides.pdf](https://jadamso.github.io/Rbooks/Templates/DataScientism_Slides.pdf)
* [DataScientism_Poster.html](https://jadamso.github.io/Rbooks/Templates/DataScientism_Poster.html)

And download source files

* [DataScientism_Slides.Rmd](https://jadamso.github.io/Rbooks/Templates/DataScientism_Slides.Rmd)
* [DataScientism_Poster.Rmd](https://jadamso.github.io/Rbooks/Templates/DataScientism_Poster.Rmd)

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





# Large Projects
***


As you scale up a project, then you will have to be more organized.

Medium and large sized projects should have their own `Project` folder on your computer with files, subdirectories with files, and subsubdirectories with files. It should look like this
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


In R, you use multiple functions on different types of data objects. Moreover, ``typically solve complex problems by decomposing them into simple functions, not simple objects.'' (H. Wickham)


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
##           used (Mb) gc trigger  (Mb) max used  (Mb)
## Ncells 1212036 64.8    2363704 126.3  2363704 126.3
## Vcells 2297802 17.6    8388608  64.0  3556025  27.2
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
##   0.004   0.000   0.005
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
<div class="profvis html-widget html-fill-item" id="htmlwidget-28c090079dfebbacbfe8" style="width:100%;height:600px;"></div>
<script type="application/json" data-for="htmlwidget-28c090079dfebbacbfe8">{"x":{"message":{"prof":{"time":[1,2,3,4,5,5,6,7,8,9,9,9,10,10,11,11,12,12,13,13,14,14,15,15,16,16,17,17,18,18,19,19,20,20,21,21,22,22,23,24,25,25,26,26,27,27,28,29,29,30,30,31,31,32,32,32,33,33,34,34,35,35,36,36,37,37,37,38,38,39,40,40,41,41,41,42,43,44,44,45,45,45,46,46,47,47,48,48,49,49,49,50,50,51,52,52,53,53,54,55,55,56,56,57,58,58,58,59,59,60,60,61,61,62,63,64,65,66,67,67,68,69,69,70,71,71,72,72,73,74,75,75,75,76,77,78,79,79,80,80,81,81,82,83,84,84,84,85,86,86,87,87,88,89,89,90,90,91,91,92,92,92,93,93,94,95,96,96,97,97,98,99,99,99,100,100,101,101,101,102,102,103,103,104,105,105,105,106,106,107,108,108,109,109,110,111,111,112,112,113,113,114,114,115,115,116,116,117,118,118,119,119,120,120,121,121,121,122,122,123,123,124,125,126,126,126,127,128,128,129,129,130,130,130,131,131,131,132,132,133,134,134,135,135,136,136,137,138,139,139,140,140,141,141,142,142,142,143,144,145,145,146,146,147,147,147,148,148,149,150,150,151,151,152,152,153,153,154,155,156,157,158,158,159,160,161,161,162,163,163,164,164,165,166,166,166,167,168,169,169,170,170,171,172,172,173,174,174,174,175,175,176,176,177,177,178,178,179,180,180,181,181,182,182,183,183,184,185,186,187,188,189,190,190,191,192,192,193,193,194,194,194,195,196,197,197,198,198,199,199,200,200,201,201,202,202,203,203,204,204,205,205,206,206,207,207,208,209,209,210,211,212,212,213,213,213,214,214,215,215,216,216,216,217,217,218,219,219,220,220,221,221,221,222,222,222,223,223,224,224,225,225,226,227,228,228,229,229,230,230,230,231,231,232,232,233,234,234,235,235,236,236,236,237,237,237,238,238,239,239,240,240,240,241,241,242,243,243,243,244,244,244,244,245,245,246,247,247,248,248,249,249,250,251,251,251,252,252,253,253,253,254,254,255,255,256,256,257,257,258,258,259,259,259,260,260,261,262,263,264,264,265,266,266,266,267,267,268,268,269,269,270,271,271,271,272,272,273,273,273,274,274,275,276,277,278,278,279,279,280,280,280,281,281,282,283,283,284,284,285,285,286,286,286,287,287,288,289,290,290,291,291,292,292,293,293,293,294,294,295,295,296,297,298,298,299,300,300,301,302,303,304,304,305,305,306,306,307,307,308,309,310,310,311,311,312,312,313,314,314,314,315,315,316,316,317,317,318,318,319,320,320,320,321,321,322,322,323,323,324,325,325,326,326,327,327,327,328,329,329,330,330,331,331,332,332,333,333,333,334,334,335,335,336,336,337,338,338,339,339,339,340,340,340,341,341,342,342,343,343,344,344,345,346,346,347,347,348,348,348,349,349,350,350,350,351,351,352,352,353,353,354,354,355,355,356,356,357,357,358,358,359,359,360,360,361,361,362,362,363,363,364,364,365,365,366,366,367,367,368,368,369,369,370,370,371,371,372,372,373,373,374,374,375,375,376,376,377,378,379,380,380,381,382,383,384,384,385,385,386,387,387,388,389,389,390,390,391,391,391,392,392,392,393,393,394,395,396,396,397,397,397,398,398,399,399,400,401,401,402,403,403,404,404,405,405,405,406,407,407,408,408,408,409,409,410,410,410,411,411,412,412,413,413,414,414,415,416,416,417,417,418,418,418,419,419,419,420,420,420,421,422,422,423,423,424,424,425,425,426,426,427,427,428,428,429,429,430,430,431,431,432,432,432,433,433,434,434,435,436,436,437,437,438,438,439,439,440,440,441,442,442,443,444,445,445,446,446,447,447,448,448,449,449,450,450,451,451,452,453,454,455,455,456,456,457,457,458,458,459,459,459,459,460,460,461,461,462,462,463,463,464,464,465,465,466,466,467,467,468,468,469,470,470,471,471,471,472,472,472,473,473,474,474,475,475,476,476,477,477,478,478,479,479,480,480,480,481,481,482,482,483,483,484,484,485,485,486,486,487,488,488,489,489,490,490,490,491,492,492,493,493,494,494,494,495,495,496,496,497,497,498,498,499,499,500,500,501,502,502,503,503,504,505,505,505,506,506,507,508,508,509,510,510,511,511,511,512,512,513,513,514,515,515,516,516,517,517,518,518,519,519,520,520,521,522,522,523,523,523,524,524,524,525,525,526,527,527,528,529,529,530,531,532,532,533,533,534,534,535,535,536,536,536,537,537,538,539,540,540,541,542,542,543,543,544,544,545,545,545,546,547,547,548,548,549,549,550,550,551,551,552,552,552,553,554,554,555,556,556,557,557,558,559,559,560,560,561,561,562,563,563,564,565,565,566,566,567,568,568,569,569,570,570,571,572,573,573,573,574,574,575,575,575,576,576,577,577,578,578,579,579,580,580,581,581,582,583,583,584,584,585,585,586,586,587,588,588,588,589,589,590,590,590,591,591,592,593,593,594,595,595,596,596,597,597,597,598,598,598,599,599,599,600,600,600,601,602,602,603,604,604,605,605,605,606,606,607,607,608,608,608,609,609,609,610,610,611,611,612,612,612,613,614,614,615,615,616,617,618,618,619,619,620,620,621,621,621,622,622,623,623,624,624,625,625,626,627,627,628,628,629,629,629,630,630,631,632,632,632,633,633,633,634,634,635,635,636,636,637,637,638,639,640,641,642,643,643,643,644,644,644,645,645,645,646,646,646,647,647,647,648,648,648,649,649,649,650,650,650,651,651,651,652,652,652,653,653,653,654,654,654,655,655,655,656,656,656,657,657,658,659,659,660,660,661,662,663,663,664,664,665,666,666,667,667,667,668,668,668,669,669,669,670,671,671,672,673,673,673,674,674,675,675,675,676,676,677,678,678,679,679,679,680,681,682,682,683,683,684,685,685,686,686,687,688,688,689,689,690,690,691,692,692,693,693,694,694,694,695,696,696,697,698,699,699,700,700,701,701,701,702,702,702,703,704,704,705,706,706,707,707,708,709,709,710,711,711,712,712,712,713,713,713,714,714,715,715,716,716,717,717,718,718,719,720,720,721,721,721,722,722,723,723,723,724,724,724,725,726,726,727,728,728,729,729,730,731,731,732,733,733,734,734,734,735,735,735,736,736,737,737,738,738,739,739,739,740,740,741,742,742,743,744,744,745,745,745,746,747,747,748,748,749,749,750,751,751,752,753,754,754,755,755,755,755,756,756,756,756,757,757,758,759,760,760,761,761,762,762,763,763,764,764,765,765,766,766,766,767,767,768,769,770,770,771,772,772,773,773,774,774,775,775,776,776,776,777,777,777,778,778,779,780,780,781,781,782,782,783,783,783,784,784,785,786,786,786,787,787,787,788,788,789,789,790,790,791,791,792,792,793,794,794,795,795,796,796,797,797,798,799,799,800,800,801,801,802,802,802,803,803,804,804,804,805,806,806,806,807,807,807,808,808,809,810,810,811,811,812,813,813,814,814,815,816,816,816,817,817,817,818,818,819,819,820,821,822,823,823,824,824,824,825,825,826,826,826,827,827,828,829,830,830,831,831,832,833,834,834,835,836,836,836,837,837,838,838,839,839,840,840,841,841,841,842,842,843,843,844,844,845,845,845,846,846,846,847,848,849,849,850,850,850,851,851,852,852,853,853,854,854,855,855,855,856,856,857,858,858,859,859,860,860,861,862,862,863,864,864,864,865,865,865,866,866,867,868,869,869,869,870,870,871,871,872,873,873,873,874,874,874,875,875,875,876,876,876,877,877,877,878,878,878,879,879,879,880,880,880,881,881,881,882,882,882,883,883,884,884,885,885,886,886,887,887,888,889,890,890,891,892,892,893,894,894,895,895,896,896,897,897,898,899,899,899,900,900,901,901,901,902,902,902,903,903,904,905,905,905,906,906,907,907,908,909,909,910,910,910,911,911,911,912,913,914,914,915,916,916,917,917,917,918,919,919,919,920,920,920,921,921,922,922,923,924,925,925,926,927,927,927,928,928,928,929,929,929,930,931,931,932,932,933,933,934,935,936,936,937,937,938,939,939,940,941,941,941,942,942,943,943,943,944,944,945,945,945,945,946,946,946,946,947,948,948,949,949,950,950,951,952,952,953,954,954,954,955,955,956,957,957,958,959,959,960,960,960,961,961,962,962,962,963,963,963,964,965,965,966,966,967,967,967,968,968,969,969,970,971,971,971,972,973,974,974,975,975,976,976,977,977,978,978,979,979,979,980,980,980,981,981,982,982,983,983,984,985,985,985,986,987,987,987,988,988,988,989,989,990,990,991,991,991,992,992,993,993,993,994,994,995,995,996,996,997,997,998,999,1000,1001,1002,1002,1002,1003,1003,1004,1004,1004,1005,1005,1006,1006,1007,1008,1009,1009,1010,1010,1011,1012,1012,1012,1013,1013,1013,1014,1014,1014,1015,1015,1015,1016,1016,1016,1017,1017,1017,1018,1019,1019,1020,1020,1021,1022,1022,1023,1024,1024,1025,1025,1026,1026,1027,1027,1028,1028,1029,1029,1030,1030,1031,1031,1032,1032,1033,1033,1034,1034,1035,1035,1036,1036,1037,1037,1038,1038,1039,1039,1040,1040,1041,1041,1042,1042,1043,1043,1044,1044,1045,1045,1046,1046,1047,1047,1048,1048,1049,1049,1050,1050,1051,1051,1052,1052,1053,1053,1054,1054,1055,1055,1056,1056,1057,1057,1058,1058,1059,1059,1060,1060,1061,1061,1062,1062,1063,1063,1064,1064,1065,1065,1066,1066,1067,1067,1068,1068,1069,1069,1070,1070,1071,1071,1072,1072,1073,1073,1074,1074,1075,1075,1076,1076,1077,1077,1078,1078,1079,1079,1080,1080,1081,1081,1082,1082,1083,1083,1084,1084,1084,1085,1085,1086,1086,1086,1087,1087,1088,1088,1089,1089,1090,1090,1091,1091,1092,1092,1093,1093,1094,1095,1095,1096,1097,1097,1098,1098,1099,1099,1100,1100,1100,1101,1101,1101,1102,1102,1103,1103,1103,1104,1104,1105,1105,1106,1106,1107,1108,1108,1109,1110,1110,1110,1111,1111,1112,1112,1113,1113,1114,1114,1115,1115,1116,1117,1118,1118,1118,1119,1120,1120,1120,1121,1121,1122,1122,1123,1123,1124,1124,1125,1125,1126,1126,1127,1127,1128,1128,1129,1129,1130,1131,1131,1132,1132,1133,1133,1134,1134,1135,1135,1135,1136,1136,1137,1137,1138,1139,1139,1139,1140,1140,1141,1141,1142,1143,1143,1144,1144,1145,1145,1146,1146,1147,1148,1148,1148,1149,1149,1150,1151,1151,1152,1152,1153,1153,1154,1154,1155,1155,1155,1156,1156,1156,1157,1157,1158,1158,1159,1160,1160,1161,1162,1163,1163,1164,1165,1165,1166,1166,1167,1167,1168,1168,1169,1170,1170,1171,1171,1172,1172,1173,1173,1174,1175,1175,1176,1176,1177,1177,1177,1178,1178,1179,1179,1180,1180,1180,1181,1181,1181,1182,1182,1183,1184,1185,1185,1186,1186,1186,1187,1187,1188,1189,1189,1189,1190,1190,1190,1191,1191,1191,1192,1192,1192,1193,1194,1194,1195,1195,1196,1197,1197,1198,1198,1199,1200,1201,1202,1203,1203,1204,1204,1204,1205,1205,1206,1207,1207,1208,1209,1209,1210,1210,1211,1212,1212,1212,1213,1213,1213,1214,1214,1215,1216,1216,1217,1218,1218,1219,1220,1220,1221,1221,1222,1222,1223,1224,1224,1224,1225,1225,1226,1226,1227,1227,1228,1228,1229,1229,1230,1231,1231,1232,1232,1233,1233,1233,1234,1234,1234,1235,1235,1235,1236,1236,1236,1237,1237,1237,1238,1238,1238,1239,1239,1239,1240,1240,1240,1241,1241,1241,1242,1242,1242,1243,1243,1244,1244,1245,1246,1246,1247,1247,1248,1249,1249,1250,1251,1251,1252,1252,1253,1253,1254,1254,1255,1255,1255,1256,1256,1257,1257,1258,1258,1259,1259,1260,1260,1261,1262,1263,1263,1263,1263,1264,1264,1264,1264,1265,1265,1266,1267,1267,1268,1268,1269,1269,1270,1271,1271,1271,1272,1272,1273,1274,1274,1275,1275,1276,1276,1277,1277,1277,1278,1278,1279,1279,1280,1281,1281,1282,1282,1283,1284,1284,1285,1285,1286,1286,1287,1287,1287,1288,1288,1288,1289,1289,1289,1290,1290,1290,1291,1291,1292,1293,1294,1294,1295,1295,1295,1296,1297,1297,1298,1298,1299,1299,1300,1300,1301,1301,1302,1302,1303,1303,1304,1304,1305,1305,1306,1306,1307,1307,1308,1308,1309,1309,1310,1310,1311,1312,1312,1313,1313,1314,1314,1315,1315,1316,1316,1317,1317,1318,1318,1319,1319,1320,1320,1321,1321,1322,1322,1323,1323,1324,1324,1325,1325,1326,1326,1327,1327,1328,1328,1329,1329,1330,1330,1331,1331,1332,1332,1333,1333,1333,1333,1333,1333,1333,1333,1333,1333,1333,1334,1334,1334,1334,1334,1334,1334,1334,1335,1335,1335,1335,1335,1335,1335,1335,1336,1336,1336,1336,1336,1336,1336,1336,1337,1337,1337,1337,1337,1337,1337,1337,1338,1338,1338,1338,1338,1338,1338,1338,1339,1339,1339,1339,1339,1339,1339,1339,1340,1340,1340,1340,1340,1340,1340,1340,1341,1341,1341,1341,1341,1341,1341,1341,1342,1342,1342,1342,1342,1342,1342,1342,1343,1343,1343,1343,1343,1343,1343,1343,1344,1344,1344,1344,1344,1344,1344,1344,1345,1345,1345,1345,1345,1345,1345,1345,1346,1346,1346,1346,1346,1346,1346,1346,1347,1347,1347,1347,1347,1347,1347,1347,1348,1348,1348,1348,1348,1348,1348,1348,1349,1349,1349,1349,1349,1349,1349,1349,1350,1350,1350,1350,1350,1350,1350,1350,1351,1351,1351,1351,1351,1351,1351,1351],"depth":[1,1,1,1,2,1,1,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,3,2,1,1,1,2,1,3,2,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,1,2,1,2,1,1,3,2,1,2,1,2,1,2,1,1,1,1,1,1,2,1,1,2,1,1,2,1,2,1,1,1,3,2,1,1,1,1,2,1,2,1,2,1,1,1,3,2,1,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,2,1,1,1,2,1,2,1,1,3,2,1,2,1,3,2,1,2,1,2,1,1,3,2,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,1,3,2,1,1,2,1,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,3,2,1,1,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,1,1,1,1,2,1,1,1,2,1,1,2,1,2,1,1,3,2,1,1,1,2,1,2,1,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,1,1,1,1,1,2,1,1,2,1,2,1,3,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,1,2,1,3,2,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,3,2,1,2,1,1,3,2,1,4,3,2,1,2,1,1,2,1,2,1,2,1,1,3,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,1,1,2,1,1,3,2,1,2,1,2,1,2,1,1,3,2,1,2,1,3,2,1,2,1,1,1,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,2,1,3,2,1,2,1,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,1,2,1,1,2,1,1,1,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,1,2,1,1,1,1,2,1,2,1,1,2,1,1,2,1,2,1,3,2,1,3,2,1,2,1,1,1,2,1,3,2,1,2,1,2,1,1,2,1,1,2,1,2,1,3,2,1,1,2,1,3,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,1,2,1,2,1,2,1,2,1,4,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,3,2,1,2,1,1,2,1,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,3,2,1,2,1,1,2,1,1,2,1,1,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,1,2,1,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,1,1,3,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,3,2,1,2,1,1,2,1,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,1,2,1,1,2,1,3,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,3,2,1,1,2,1,2,1,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,1,1,1,1,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,1,1,2,1,2,1,1,2,1,3,2,1,3,2,1,3,2,1,1,2,1,1,3,2,1,2,1,3,2,1,2,1,1,2,1,3,2,1,1,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,1,2,1,1,1,2,1,2,1,3,2,1,3,2,1,1,2,1,1,2,1,2,1,1,2,1,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,2,1,3,2,1,3,2,1,1,2,1,1,2,1,2,1,1,2,1,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,1,2,1,3,2,1,1,2,1,2,1,2,1,1,2,1,1,1,2,1,4,3,2,1,4,3,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,2,1,3,2,1,2,1,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,2,1,3,2,1,1,3,2,1,3,2,1,2,1,1,2,1,2,1,1,2,1,2,1,1,3,2,1,3,2,1,2,1,2,1,1,1,1,2,1,3,2,1,2,1,3,2,1,2,1,1,1,2,1,2,1,1,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,3,2,1,3,2,1,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,2,1,1,2,1,1,3,2,1,3,2,1,2,1,1,1,3,2,1,2,1,2,1,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,3,2,1,3,2,1,2,1,1,3,2,1,2,1,2,1,1,2,1,3,2,1,3,2,1,1,1,2,1,1,2,1,3,2,1,1,3,2,1,3,2,1,2,1,2,1,1,1,2,1,1,3,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,1,1,2,1,2,1,1,2,1,1,3,2,1,2,1,3,2,1,2,1,4,3,2,1,4,3,2,1,1,2,1,2,1,2,1,1,2,1,1,3,2,1,2,1,1,2,1,1,2,1,3,2,1,2,1,3,2,1,3,2,1,1,2,1,2,1,3,2,1,2,1,2,1,1,3,2,1,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,3,2,1,1,3,2,1,3,2,1,2,1,2,1,3,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,1,1,1,3,2,1,2,1,3,2,1,2,1,2,1,1,1,2,1,2,1,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,1,3,2,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,1,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,2,1,3,2,1,3,2,1,2,1,1,1,2,1,3,2,1,2,1,1,3,2,1,3,2,1,3,2,1,3,2,1,1,2,1,2,1,1,2,1,2,1,1,1,1,1,2,1,3,2,1,2,1,1,2,1,1,2,1,2,1,1,3,2,1,3,2,1,2,1,1,2,1,1,2,1,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,1,4,3,2,1,4,3,2,1,2,1,1,2,1,2,1,2,1,1,3,2,1,2,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,1,1,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,11,10,9,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1],"label":["rowSums","rowSums","rowSums","rowSums","/","local","rowMeans","rowMeans","rowMeans","<GC>","aperm.default","apply","aperm.default","apply","aperm.default","apply","aperm.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","mean.default","apply","apply","apply","FUN","apply","FUN","apply","is.na","local","apply","FUN","apply","FUN","apply","length","local","<GC>","is.numeric","local","FUN","apply","is.numeric","local","FUN","apply","FUN","apply","isTRUE","mean.default","apply","length","local","apply","mean.default","apply","isTRUE","mean.default","apply","apply","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","<GC>","FUN","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","apply","FUN","apply","FUN","apply","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","apply","apply","apply","<GC>","apply","apply","mean.default","apply","apply","FUN","apply","FUN","apply","apply","apply","<GC>","FUN","apply","apply","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","apply","<GC>","FUN","apply","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","<GC>","mean.default","apply","FUN","apply","apply","apply","FUN","apply","mean.default","apply","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","mean.default","apply","FUN","apply","mean.default","apply","apply","isTRUE","mean.default","apply","mean.default","apply","apply","mean.default","apply","<GC>","apply","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","apply","<GC>","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","apply","apply","<GC>","FUN","apply","apply","FUN","apply","is.numeric","local","isTRUE","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","<GC>","apply","is.na","local","FUN","apply","apply","apply","FUN","apply","FUN","apply","is.numeric","local","<GC>","FUN","apply","apply","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","<GC>","apply","mean.default","apply","FUN","apply","FUN","apply","apply","apply","apply","apply","<GC>","apply","apply","apply","mean.default","apply","apply","mean.default","apply","mean.default","apply","apply","<GC>","FUN","apply","apply","apply","FUN","apply","mean.default","apply","apply","FUN","apply","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","apply","length","local","length","local","<GC>","apply","is.numeric","local","apply","apply","apply","apply","apply","apply","<GC>","apply","apply","is.na","local","is.numeric","local","isTRUE","mean.default","apply","apply","apply","mean.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","apply","mean.default","apply","apply","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","apply","isTRUE","mean.default","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","is.numeric","local","FUN","apply","FUN","apply","mean.default","apply","apply","apply","mean.default","apply","FUN","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","apply","is.na","local","mean.default","apply","isTRUE","mean.default","apply","<GC>","length","local","is.na","local","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","apply","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","apply","<GC>","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","length","local","<GC>","FUN","apply","mean.default","apply","apply","apply","apply","FUN","apply","apply","<GC>","mean.default","apply","mean.default","apply","mean.default","apply","length","local","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","mean.default","apply","mean.default","apply","apply","apply","apply","mean.default","apply","mean.default","apply","<GC>","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","is.numeric","local","mean.default","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","is.na","local","is.na","local","FUN","apply","apply","apply","FUN","apply","apply","<GC>","apply","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","apply","apply","apply","mean.default","apply","FUN","apply","FUN","apply","apply","<GC>","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","<GC>","length","local","FUN","apply","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","apply","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","<GC>","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","is.na","local","mean.default","apply","FUN","apply","mean.default","apply","apply","<GC>","apply","length","local","isTRUE","mean.default","apply","length","local","isTRUE","mean.default","apply","mean.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","apply","apply","apply","FUN","apply","apply","apply","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","apply","mean.default","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","<GC>","is.numeric","local","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","isTRUE","mean.default","apply","apply","mean.default","apply","length","local","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","is.na","local","<GC>","FUN","apply","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","apply","is.na","local","apply","apply","<GC>","apply","<GC>","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","apply","is.numeric","local","FUN","apply","FUN","apply","FUN","apply","<GC>","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","is.na","local","is.numeric","local","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","mean.default","apply","isTRUE","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","<GC>","apply","FUN","apply","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","<GC>","apply","FUN","apply","is.na","local","apply","FUN","apply","length","local","apply","isTRUE","mean.default","apply","mean.default","apply","apply","mean.default","apply","apply","FUN","apply","<GC>","FUN","apply","mean.default","apply","mean.default","apply","apply","mean.default","apply","is.na","local","length","local","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","is.na","local","apply","FUN","apply","apply","apply","length","local","FUN","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","FUN","apply","apply","apply","FUN","apply","apply","length","local","mean.default","apply","is.na","local","isTRUE","mean.default","apply","apply","FUN","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","apply","FUN","apply","<GC>","apply","<GC>","apply","apply","mean.default","apply","apply","is.numeric","local","is.numeric","local","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","apply","<GC>","FUN","apply","is.na","local","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","apply","is.numeric","local","FUN","apply","<GC>","apply","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","mean.default","apply","apply","mean.default","apply","mean.default","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","length","local","FUN","apply","apply","apply","FUN","apply","mean.default","apply","<GC>","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","length","local","FUN","apply","apply","mean.default","apply","is.numeric","local","isTRUE","mean.default","apply","FUN","apply","apply","<GC>","is.numeric","local","isTRUE","mean.default","apply","length","local","FUN","apply","mean.default","apply","mean.default","apply","apply","apply","apply","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","is.numeric","local","apply","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","length","local","<GC>","is.numeric","local","apply","apply","is.na","local","FUN","apply","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","length","local","<GC>","apply","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","apply","FUN","apply","<GC>","length","local","<GC>","length","local","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","apply","mean.default","apply","FUN","apply","apply","FUN","apply","apply","FUN","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","apply","FUN","apply","apply","FUN","apply","<GC>","mean.default","apply","apply","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","apply","FUN","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","mean.default","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","length","local","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","apply","apply","mean.default","apply","apply","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","apply","is.numeric","local","length","local","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","<GC>","apply","<GC>","apply","apply","length","local","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","length","local","isTRUE","mean.default","apply","apply","<GC>","is.na","local","<GC>","is.na","local","is.numeric","local","apply","mean.default","apply","is.na","local","apply","FUN","apply","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","<GC>","FUN","apply","mean.default","apply","apply","apply","FUN","apply","mean.default","apply","apply","apply","FUN","apply","apply","<GC>","length","local","FUN","apply","FUN","apply","FUN","apply","is.numeric","local","isTRUE","mean.default","apply","is.na","local","mean.default","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","is.na","local","apply","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","is.na","local","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","mean.default","apply","is.numeric","local","FUN","apply","mean.default","apply","apply","apply","mean.default","apply","apply","<GC>","apply","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","length","local","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","length","local","FUN","apply","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","apply","mean.default","apply","apply","FUN","apply","isTRUE","mean.default","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","mean.default","apply","<GC>","apply","apply","mean.default","apply","apply","isTRUE","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","apply","is.na","local","FUN","apply","FUN","apply","apply","mean.default","apply","apply","<GC>","FUN","apply","FUN","apply","apply","FUN","apply","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","mean.default","apply","is.na","local","isTRUE","mean.default","apply","FUN","apply","FUN","apply","apply","<GC>","mean.default","apply","apply","apply","length","local","is.numeric","local","FUN","apply","mean.default","apply","length","local","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","is.na","local","mean.default","apply","apply","isTRUE","mean.default","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","is.na","local","isTRUE","mean.default","apply","FUN","apply","<GC>","apply","<GC>","apply","FUN","apply","apply","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","mean.default","apply","is.numeric","local","mean.default","apply","apply","apply","FUN","apply","length","local","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","length","local","FUN","apply","apply","mean.default","apply","apply","FUN","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","length","local","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","is.numeric","local","<GC>","is.numeric","local","length","local","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","apply","FUN","apply","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","apply","FUN","apply","<GC>","apply","<GC>","apply","<GC>","apply","apply","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","is.numeric","local","apply","FUN","apply","apply","apply","FUN","apply","apply","length","local","FUN","apply","<GC>","apply","<GC>","apply","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","isTRUE","mean.default","apply","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","FUN","apply","apply","apply","apply","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","FUN","apply","apply","FUN","apply","apply","is.numeric","local","FUN","apply","is.numeric","local","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","mean.default","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","is.na","local","mean.default","apply","length","local","FUN","apply","apply","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","mean.default","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","apply","length","local","mean.default","apply","apply","FUN","apply","mean.default","apply","length","local","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","mean.default","apply","FUN","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","$<-","make.noValueContext","make.loopContext","cmpForBody","h","tryInline","cmpCall","cmp","genCode","compile","compiler:::tryCompile","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis"],"filenum":[1,1,1,1,1,null,1,1,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,1,null,1,null,1,null,null,1,null,1,null,1,null,null,null,null,null,null,1,null,null,null,1,null,1,null,null,1,null,null,1,null,1,null,null,1,1,1,null,1,null,null,1,null,1,null,1,null,1,null,null,1,null,1,1,null,1,null,1,1,null,1,null,1,1,null,null,1,null,1,null,1,null,1,1,1,1,1,1,null,1,1,null,1,1,null,1,null,1,1,1,null,null,1,1,1,1,null,1,null,1,null,1,1,1,null,null,1,1,null,1,null,1,1,null,1,null,1,null,1,null,null,1,null,1,1,1,null,1,null,1,1,null,null,1,null,1,null,null,1,null,1,null,1,1,null,null,1,null,1,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,null,1,null,1,null,1,1,1,null,null,1,1,null,1,null,null,null,null,1,null,null,1,null,1,1,null,1,null,null,null,1,1,1,null,1,null,1,null,null,null,null,1,1,1,null,1,null,1,null,null,1,null,1,1,null,1,null,1,null,1,null,1,1,1,1,1,null,1,1,1,null,1,1,null,1,null,1,1,null,null,1,1,1,null,1,null,1,1,null,1,1,null,null,1,null,1,null,1,null,1,null,1,1,null,null,null,null,null,1,null,null,1,1,1,1,1,1,null,1,1,null,null,null,null,null,null,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,1,1,null,1,null,null,1,null,1,null,1,null,null,1,null,1,1,null,1,null,1,null,null,1,null,null,null,null,1,null,1,null,1,1,1,null,1,null,1,null,null,1,null,1,null,1,1,null,null,null,1,null,null,1,null,null,null,null,null,null,1,null,null,1,null,1,1,null,null,1,null,null,null,1,null,1,1,null,1,null,1,null,1,1,null,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,null,null,null,1,null,1,1,1,1,null,1,1,null,null,1,null,1,null,1,null,null,1,null,null,1,null,1,null,null,1,null,1,1,1,1,null,1,null,1,null,null,1,null,1,1,null,1,null,1,null,1,null,null,null,null,1,1,1,null,1,null,1,null,1,null,null,null,null,null,null,1,1,1,null,1,1,null,1,1,1,1,null,1,null,1,null,1,null,1,1,1,null,1,null,1,null,1,1,null,null,1,null,1,null,1,null,1,null,1,1,null,null,null,null,1,null,1,null,1,1,null,1,null,1,null,null,1,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,1,null,1,null,null,1,null,null,1,null,null,null,1,null,1,null,1,1,null,1,null,null,null,null,1,null,null,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,1,1,null,1,1,1,1,null,1,null,1,1,null,1,1,null,1,null,1,null,null,1,null,null,1,null,1,1,1,null,1,null,null,1,null,1,null,1,1,null,1,1,null,1,null,1,null,null,null,1,null,1,null,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,null,1,null,null,1,null,null,1,1,null,1,null,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,null,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,1,null,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,1,1,null,null,null,1,null,1,null,1,null,null,null,1,null,1,null,1,null,1,null,null,null,null,null,1,null,1,null,1,null,1,1,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,null,1,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,null,1,null,null,1,null,1,1,null,1,1,null,1,null,null,1,null,1,null,1,1,null,1,null,null,null,null,null,1,null,1,null,1,1,null,1,null,null,1,null,null,1,null,1,1,null,null,1,null,1,1,1,null,null,null,1,null,1,null,1,null,null,1,null,1,1,1,null,1,1,null,null,null,1,null,null,null,null,1,1,null,1,null,1,null,1,null,1,null,1,null,null,1,1,null,1,1,null,1,null,1,1,null,1,null,1,null,1,1,null,1,1,null,null,null,null,1,null,1,null,1,null,1,1,1,null,null,1,null,null,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,null,null,1,null,1,null,1,1,null,null,1,null,1,null,null,1,null,1,1,null,1,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,1,null,1,1,null,1,null,null,1,null,1,null,1,null,null,1,null,null,1,null,1,null,1,null,null,1,1,null,null,null,1,1,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,null,null,1,1,null,1,null,null,null,null,1,null,1,1,null,null,null,null,null,1,null,null,null,1,null,1,null,1,1,1,1,1,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,1,null,1,null,null,1,1,null,1,null,1,1,null,1,null,null,1,null,null,1,null,null,1,1,null,1,1,null,null,1,null,1,null,null,1,null,1,1,null,null,null,null,null,1,1,null,null,null,1,1,null,1,null,1,1,null,1,null,null,null,1,1,null,1,null,1,null,null,1,1,null,1,1,1,null,1,null,1,null,null,1,null,null,1,1,null,1,1,null,1,null,1,1,null,1,1,null,1,null,null,null,null,null,null,null,1,null,1,null,1,null,1,null,1,1,null,1,null,null,1,null,1,null,null,1,null,null,1,1,null,1,1,null,1,null,1,1,null,1,1,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,null,1,null,1,1,null,1,1,null,1,null,null,1,1,null,1,null,1,null,1,1,null,1,1,1,null,1,null,null,null,1,null,null,null,1,null,1,1,1,null,1,null,1,null,1,null,1,null,null,null,1,null,null,1,null,1,1,1,null,1,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,1,1,null,null,null,null,null,1,null,null,1,null,1,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,1,null,null,null,1,null,1,null,null,1,null,null,null,null,1,1,null,null,null,null,null,null,null,null,1,null,1,null,null,1,null,1,null,1,1,null,null,1,null,null,1,null,1,null,1,1,1,1,null,1,null,null,1,null,1,null,null,1,null,1,1,1,null,1,null,1,1,1,null,1,1,null,null,null,null,1,null,1,null,1,null,null,null,null,1,null,null,null,1,null,1,null,null,1,null,null,1,1,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,1,null,1,null,1,1,null,1,1,null,null,1,null,null,1,null,1,1,1,null,null,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,null,null,1,null,1,1,1,null,1,1,null,1,1,null,1,null,1,null,1,null,1,1,null,null,1,null,null,null,null,1,null,null,1,null,1,1,null,null,1,null,null,null,1,1,null,1,null,null,1,null,null,1,1,1,null,1,1,null,1,null,null,1,1,null,null,1,null,null,1,null,1,null,1,1,1,null,1,1,null,null,1,null,null,1,null,null,1,1,null,1,null,1,null,1,1,1,null,1,null,1,1,null,1,1,null,null,1,null,1,null,null,1,null,1,null,null,null,1,null,null,null,1,1,null,null,null,1,null,1,1,null,1,1,null,null,1,null,1,1,null,1,1,null,1,null,null,1,null,1,null,null,1,null,null,1,1,null,1,null,null,null,null,1,null,1,null,1,1,null,null,1,1,1,null,null,null,null,null,1,null,1,null,null,null,null,1,null,null,1,null,1,null,null,null,1,1,null,null,1,1,null,null,1,null,null,1,null,1,null,1,null,null,1,null,null,null,null,1,null,1,null,1,null,1,null,1,1,1,1,1,null,null,1,null,1,null,null,1,null,null,null,1,1,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,1,null,null,null,1,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,1,null,1,null,1,null,1,null,null,null,null,null,null,null,null,null,null,1,null,1,null,1,null,1,1,null,1,1,null,null,1,null,1,null,1,null,1,null,1,null,1,1,1,null,null,1,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,1,null,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,1,null,null,1,null,1,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,1,null,null,1,null,1,1,1,null,1,1,null,null,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,null,1,null,1,null,1,null,null,1,null,null,1,null,1,1,1,null,1,null,null,1,null,1,1,null,null,1,null,null,1,null,null,1,null,null,1,1,null,1,null,1,1,null,1,null,1,1,1,1,1,null,1,null,null,1,null,1,1,null,1,1,null,1,null,1,1,null,null,1,null,null,1,null,1,1,null,1,1,null,1,1,null,null,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,1,null,1,null,1,1,null,1,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,null,null,1,null,null,null,1,1,1,null,null,null,1,null,null,null,1,null,1,1,null,1,null,1,null,1,1,null,null,1,null,1,1,null,1,null,1,null,1,null,null,1,null,1,null,1,1,null,null,null,1,1,null,1,null,1,null,null,null,null,1,null,null,1,null,null,1,null,null,1,null,1,1,1,null,1,null,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,null,null,null,null,null,null,null,null,1,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null],"linenum":[10,10,10,10,10,null,11,11,11,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,12,null,12,null,12,null,null,12,null,12,null,12,null,null,null,null,null,null,12,null,null,null,12,null,12,null,null,12,null,null,12,null,12,null,null,12,12,12,null,12,null,null,12,null,12,null,12,null,12,null,null,12,null,12,12,null,12,null,12,12,null,12,null,12,12,null,null,12,null,12,null,12,null,12,12,12,12,12,12,null,12,12,null,12,12,null,12,null,12,12,12,null,null,12,12,12,12,null,12,null,12,null,12,12,12,null,null,12,12,null,12,null,12,12,null,12,null,12,null,12,null,null,12,null,12,12,12,null,12,null,12,12,null,null,12,null,12,null,null,12,null,12,null,12,12,null,null,12,null,12,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,null,12,null,12,null,12,12,12,null,null,12,12,null,12,null,null,null,null,12,null,null,12,null,12,12,null,12,null,null,null,12,12,12,null,12,null,12,null,null,null,null,12,12,12,null,12,null,12,null,null,12,null,12,12,null,12,null,12,null,12,null,12,12,12,12,12,null,12,12,12,null,12,12,null,12,null,12,12,null,null,12,12,12,null,12,null,12,12,null,12,12,null,null,12,null,12,null,12,null,12,null,12,12,null,null,null,null,null,12,null,null,12,12,12,12,12,12,null,12,12,null,null,null,null,null,null,12,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,12,12,null,12,null,null,12,null,12,null,12,null,null,12,null,12,12,null,12,null,12,null,null,12,null,null,null,null,12,null,12,null,12,12,12,null,12,null,12,null,null,12,null,12,null,12,12,null,null,null,12,null,null,12,null,null,null,null,null,null,12,null,null,12,null,12,12,null,null,12,null,null,null,12,null,12,12,null,12,null,12,null,12,12,null,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,null,null,null,12,null,12,12,12,12,null,12,12,null,null,12,null,12,null,12,null,null,12,null,null,12,null,12,null,null,12,null,12,12,12,12,null,12,null,12,null,null,12,null,12,12,null,12,null,12,null,12,null,null,null,null,12,12,12,null,12,null,12,null,12,null,null,null,null,null,null,12,12,12,null,12,12,null,12,12,12,12,null,12,null,12,null,12,null,12,12,12,null,12,null,12,null,12,12,null,null,12,null,12,null,12,null,12,null,12,12,null,null,null,null,12,null,12,null,12,12,null,12,null,12,null,null,12,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,12,null,12,null,null,12,null,null,12,null,null,null,12,null,12,null,12,12,null,12,null,null,null,null,12,null,null,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,12,12,null,12,12,12,12,null,12,null,12,12,null,12,12,null,12,null,12,null,null,12,null,null,12,null,12,12,12,null,12,null,null,12,null,12,null,12,12,null,12,12,null,12,null,12,null,null,null,12,null,12,null,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,null,12,null,null,12,null,null,12,12,null,12,null,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,null,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,12,null,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,12,12,null,null,null,12,null,12,null,12,null,null,null,12,null,12,null,12,null,12,null,null,null,null,null,12,null,12,null,12,null,12,12,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,null,12,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,null,12,null,null,12,null,12,12,null,12,12,null,12,null,null,12,null,12,null,12,12,null,12,null,null,null,null,null,12,null,12,null,12,12,null,12,null,null,12,null,null,12,null,12,12,null,null,12,null,12,12,12,null,null,null,12,null,12,null,12,null,null,12,null,12,12,12,null,12,12,null,null,null,12,null,null,null,null,12,12,null,12,null,12,null,12,null,12,null,12,null,null,12,12,null,12,12,null,12,null,12,12,null,12,null,12,null,12,12,null,12,12,null,null,null,null,12,null,12,null,12,null,12,12,12,null,null,12,null,null,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,null,null,12,null,12,null,12,12,null,null,12,null,12,null,null,12,null,12,12,null,12,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,12,null,12,12,null,12,null,null,12,null,12,null,12,null,null,12,null,null,12,null,12,null,12,null,null,12,12,null,null,null,12,12,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,null,null,12,12,null,12,null,null,null,null,12,null,12,12,null,null,null,null,null,12,null,null,null,12,null,12,null,12,12,12,12,12,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,12,null,12,null,null,12,12,null,12,null,12,12,null,12,null,null,12,null,null,12,null,null,12,12,null,12,12,null,null,12,null,12,null,null,12,null,12,12,null,null,null,null,null,12,12,null,null,null,12,12,null,12,null,12,12,null,12,null,null,null,12,12,null,12,null,12,null,null,12,12,null,12,12,12,null,12,null,12,null,null,12,null,null,12,12,null,12,12,null,12,null,12,12,null,12,12,null,12,null,null,null,null,null,null,null,12,null,12,null,12,null,12,null,12,12,null,12,null,null,12,null,12,null,null,12,null,null,12,12,null,12,12,null,12,null,12,12,null,12,12,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,null,12,null,12,12,null,12,12,null,12,null,null,12,12,null,12,null,12,null,12,12,null,12,12,12,null,12,null,null,null,12,null,null,null,12,null,12,12,12,null,12,null,12,null,12,null,12,null,null,null,12,null,null,12,null,12,12,12,null,12,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,12,12,null,null,null,null,null,12,null,null,12,null,12,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,12,null,null,null,12,null,12,null,null,12,null,null,null,null,12,12,null,null,null,null,null,null,null,null,12,null,12,null,null,12,null,12,null,12,12,null,null,12,null,null,12,null,12,null,12,12,12,12,null,12,null,null,12,null,12,null,null,12,null,12,12,12,null,12,null,12,12,12,null,12,12,null,null,null,null,12,null,12,null,12,null,null,null,null,12,null,null,null,12,null,12,null,null,12,null,null,12,12,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,12,null,12,null,12,12,null,12,12,null,null,12,null,null,12,null,12,12,12,null,null,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,null,null,12,null,12,12,12,null,12,12,null,12,12,null,12,null,12,null,12,null,12,12,null,null,12,null,null,null,null,12,null,null,12,null,12,12,null,null,12,null,null,null,12,12,null,12,null,null,12,null,null,12,12,12,null,12,12,null,12,null,null,12,12,null,null,12,null,null,12,null,12,null,12,12,12,null,12,12,null,null,12,null,null,12,null,null,12,12,null,12,null,12,null,12,12,12,null,12,null,12,12,null,12,12,null,null,12,null,12,null,null,12,null,12,null,null,null,12,null,null,null,12,12,null,null,null,12,null,12,12,null,12,12,null,null,12,null,12,12,null,12,12,null,12,null,null,12,null,12,null,null,12,null,null,12,12,null,12,null,null,null,null,12,null,12,null,12,12,null,null,12,12,12,null,null,null,null,null,12,null,12,null,null,null,null,12,null,null,12,null,12,null,null,null,12,12,null,null,12,12,null,null,12,null,null,12,null,12,null,12,null,null,12,null,null,null,null,12,null,12,null,12,null,12,null,12,12,12,12,12,null,null,12,null,12,null,null,12,null,null,null,12,12,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,12,null,null,null,12,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,12,null,12,null,12,null,12,null,null,null,null,null,null,null,null,null,null,12,null,12,null,12,null,12,12,null,12,12,null,null,12,null,12,null,12,null,12,null,12,null,12,12,12,null,null,12,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,12,null,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,12,null,null,12,null,12,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,12,null,null,12,null,12,12,12,null,12,12,null,null,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,null,12,null,12,null,12,null,null,12,null,null,12,null,12,12,12,null,12,null,null,12,null,12,12,null,null,12,null,null,12,null,null,12,null,null,12,12,null,12,null,12,12,null,12,null,12,12,12,12,12,null,12,null,null,12,null,12,12,null,12,12,null,12,null,12,12,null,null,12,null,null,12,null,12,12,null,12,12,null,12,12,null,null,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,12,null,12,null,12,12,null,12,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,null,null,12,null,null,null,12,12,12,null,null,null,12,null,null,null,12,null,12,12,null,12,null,12,null,12,12,null,null,12,null,12,12,null,12,null,12,null,12,null,null,12,null,12,null,12,12,null,null,null,12,12,null,12,null,12,null,null,null,null,12,null,null,12,null,null,12,null,null,12,null,12,12,12,null,12,null,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,null,null,null,null,null,null,null,null,13,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null],"memalloc":[124.4914169311523,124.4914169311523,124.4914169311523,124.4914169311523,124.4914398193359,124.4914398193359,139.7736511230469,139.7736511230469,139.7736511230469,139.7740173339844,139.7740173339844,139.7740173339844,170.2393951416016,170.2393951416016,170.2393951416016,170.2393951416016,170.2393951416016,170.2393951416016,170.2394409179688,170.2394409179688,170.2394409179688,170.2394409179688,170.2394409179688,170.2394409179688,170.2394409179688,170.2394409179688,170.2394409179688,170.2394409179688,170.2394409179688,170.2394409179688,170.2394409179688,170.2394409179688,170.2394409179688,170.2394409179688,170.2391357421875,170.2391357421875,185.6127853393555,185.6127853393555,185.8544235229492,186.1117782592773,186.3786926269531,186.3786926269531,186.6956024169922,186.6956024169922,187.0762329101562,187.0762329101562,187.4280242919922,187.8147735595703,187.8147735595703,188.2211761474609,188.2211761474609,188.6272888183594,188.6272888183594,188.7651901245117,188.7651901245117,188.7651901245117,185.9646072387695,185.9646072387695,186.3380432128906,186.3380432128906,186.7563552856445,186.7563552856445,187.1709899902344,187.1709899902344,187.576904296875,187.576904296875,187.576904296875,187.9829483032227,187.9829483032227,188.3932495117188,188.8015518188477,188.8015518188477,185.8364028930664,185.8364028930664,185.8364028930664,186.1819610595703,186.5429229736328,186.9175033569336,186.9175033569336,187.3155059814453,187.3155059814453,187.3155059814453,187.7173538208008,187.7173538208008,188.1172714233398,188.1172714233398,188.5209884643555,188.5209884643555,188.922492980957,188.922492980957,188.922492980957,186.0028228759766,186.0028228759766,186.349967956543,186.7140274047852,186.7140274047852,187.0946655273438,187.0946655273438,187.4916152954102,187.9021606445312,187.9021606445312,188.3134918212891,188.3134918212891,188.7276000976562,189.0083770751953,189.0083770751953,189.0083770751953,186.2384643554688,186.2384643554688,186.5864181518555,186.5864181518555,186.9549179077148,186.9549179077148,187.3417587280273,187.7417526245117,188.1476287841797,188.5559616088867,188.9651718139648,189.0928649902344,189.0928649902344,186.5269622802734,186.886848449707,186.886848449707,187.2592163085938,187.6550369262695,187.6550369262695,188.056510925293,188.056510925293,188.4661636352539,188.8756332397461,189.1760482788086,189.1760482788086,189.1760482788086,186.4778442382812,186.82177734375,187.186767578125,187.562255859375,187.562255859375,187.9546432495117,187.9546432495117,188.3522796630859,188.3522796630859,188.7565841674805,189.1666870117188,189.2578582763672,189.2578582763672,189.2578582763672,186.7384796142578,187.0865783691406,187.0865783691406,187.4471740722656,187.4471740722656,187.8159637451172,188.1964569091797,188.1964569091797,188.5933837890625,188.5933837890625,188.9877166748047,188.9877166748047,189.3383102416992,189.3383102416992,189.3383102416992,186.6402435302734,186.6402435302734,186.9594879150391,187.3090362548828,187.6686935424805,187.6686935424805,188.0400161743164,188.0400161743164,188.4252395629883,188.8238754272461,188.8238754272461,188.8238754272461,189.223762512207,189.223762512207,189.4175109863281,189.4175109863281,189.4175109863281,186.8675003051758,186.8675003051758,187.1878128051758,187.1878128051758,187.5329742431641,187.8937072753906,187.8937072753906,187.8937072753906,188.2680358886719,188.2680358886719,188.7019958496094,189.1036148071289,189.1036148071289,189.4954299926758,189.4954299926758,186.8583221435547,187.1797943115234,187.1797943115234,187.5276107788086,187.5276107788086,187.8896636962891,187.8896636962891,188.2614974975586,188.2614974975586,188.6508560180664,188.6508560180664,189.0517730712891,189.0517730712891,189.4543838500977,189.5720138549805,189.5720138549805,187.1885375976562,187.1885375976562,187.5271606445312,187.5271606445312,187.8839416503906,187.8839416503906,187.8839416503906,188.2522811889648,188.2522811889648,188.6330108642578,188.6330108642578,189.0316925048828,189.4328308105469,189.6474533081055,189.6474533081055,189.6474533081055,187.2328948974609,187.5640640258789,187.5640640258789,187.9130859375,187.9130859375,188.2754592895508,188.2754592895508,188.2754592895508,188.6555404663086,188.6555404663086,188.6555404663086,189.0538558959961,189.0538558959961,189.4527893066406,189.7217025756836,189.7217025756836,187.3013229370117,187.3013229370117,187.6217041015625,187.6217041015625,187.9606704711914,188.3164825439453,188.6859664916992,188.6859664916992,189.0755233764648,189.0755233764648,189.4758224487305,189.4758224487305,189.7946395874023,189.7946395874023,189.7946395874023,187.3681030273438,187.6809768676758,188.0165100097656,188.0165100097656,188.3663864135742,188.3663864135742,188.7693023681641,188.7693023681641,188.7693023681641,189.1539916992188,189.1539916992188,189.5353012084961,189.8664779663086,189.8664779663086,187.4644317626953,187.4644317626953,187.7675933837891,187.7675933837891,188.0945739746094,188.0945739746094,188.4404373168945,188.8007965087891,189.1839370727539,189.5773468017578,189.9371490478516,189.9371490478516,187.5554504394531,187.8516540527344,188.1622848510742,188.1622848510742,188.5015106201172,188.859260559082,188.859260559082,189.229362487793,189.229362487793,189.621223449707,190.0066909790039,190.0066909790039,190.0066909790039,187.6394653320312,187.9353942871094,188.2541580200195,188.2541580200195,188.5986404418945,188.5986404418945,188.9572906494141,189.3378982543945,189.3378982543945,189.734245300293,190.0750885009766,190.0750885009766,190.0750885009766,187.7814025878906,187.7814025878906,188.0772552490234,188.0772552490234,188.3963165283203,188.3963165283203,188.7417831420898,188.7417831420898,189.1025619506836,189.4841079711914,189.4841079711914,189.8808517456055,189.8808517456055,190.1423492431641,190.1423492431641,187.9406509399414,187.9406509399414,188.26513671875,188.5884628295898,188.9378356933594,189.2981567382812,189.6843795776367,190.0815048217773,190.2085342407227,190.2085342407227,188.1436996459961,188.4428482055664,188.4428482055664,188.7736282348633,188.7736282348633,189.1265029907227,189.1265029907227,189.1265029907227,189.4940948486328,189.8802185058594,190.268310546875,190.268310546875,190.273681640625,190.273681640625,190.273681640625,190.273681640625,190.273681640625,190.273681640625,190.273681640625,190.273681640625,190.273681640625,190.273681640625,190.273681640625,190.273681640625,190.273681640625,190.273681640625,190.273681640625,190.273681640625,188.03173828125,188.03173828125,188.1879653930664,188.1879653930664,188.4138031005859,188.6561889648438,188.6561889648438,188.9270706176758,189.2302932739258,189.562873840332,189.562873840332,189.8985443115234,189.8985443115234,189.8985443115234,190.2685852050781,190.2685852050781,190.3372650146484,190.3372650146484,188.3951873779297,188.3951873779297,188.3951873779297,188.6947631835938,188.6947631835938,189.0280075073242,189.382942199707,189.382942199707,189.7573852539062,189.7573852539062,190.1482009887695,190.1482009887695,190.1482009887695,190.4003677368164,190.4003677368164,190.4003677368164,188.3330535888672,188.3330535888672,188.6160278320312,188.6160278320312,188.932258605957,188.932258605957,189.2752456665039,189.6364212036133,190.0165405273438,190.0165405273438,190.4140243530273,190.4140243530273,190.4624099731445,190.4624099731445,190.4624099731445,188.5787582397461,188.5787582397461,188.8761749267578,188.8761749267578,189.2089996337891,189.5628433227539,189.5628433227539,189.9266128540039,189.9266128540039,190.3179092407227,190.3179092407227,190.3179092407227,190.5234222412109,190.5234222412109,190.5234222412109,188.5595245361328,188.5595245361328,188.8437652587891,188.8437652587891,189.1633453369141,189.1633453369141,189.1633453369141,189.506591796875,189.506591796875,189.8672103881836,190.2523422241211,190.2523422241211,190.2523422241211,190.5834732055664,190.5834732055664,190.5834732055664,190.5834732055664,188.5553207397461,188.5553207397461,188.8288192749023,189.1355514526367,189.1355514526367,189.4759902954102,189.4759902954102,189.8344879150391,189.8344879150391,190.2551574707031,190.6425552368164,190.6425552368164,190.6425552368164,188.6174621582031,188.6174621582031,188.8948593139648,188.8948593139648,188.8948593139648,189.1975402832031,189.1975402832031,189.5388870239258,189.5388870239258,189.8982009887695,189.8982009887695,190.2728576660156,190.2728576660156,190.670166015625,190.670166015625,190.7006683349609,190.7006683349609,190.7006683349609,188.9428863525391,188.9428863525391,189.2397308349609,189.5727844238281,189.9298782348633,190.3034744262695,190.3034744262695,190.7024993896484,190.7578353881836,190.7578353881836,190.7578353881836,189.0188293457031,189.0188293457031,189.3143157958984,189.3143157958984,189.6465148925781,189.6465148925781,190.0027542114258,190.376823425293,190.376823425293,190.376823425293,190.7770614624023,190.7770614624023,190.8141098022461,190.8141098022461,190.8141098022461,189.1051635742188,189.1051635742188,189.3980865478516,189.729621887207,190.0861358642578,190.4577407836914,190.4577407836914,190.8536148071289,190.8536148071289,190.8694458007812,190.8694458007812,190.8694458007812,189.2152786254883,189.2152786254883,189.5134811401367,189.8496398925781,189.8496398925781,190.2081298828125,190.2081298828125,190.5871505737305,190.5871505737305,190.9239044189453,190.9239044189453,190.9239044189453,189.1088180541992,189.1088180541992,189.3815383911133,189.6913299560547,190.0372924804688,190.0372924804688,190.3994750976562,190.3994750976562,190.7838745117188,190.7838745117188,190.9774551391602,190.9774551391602,190.9774551391602,189.2628631591797,189.2628631591797,189.5399169921875,189.5399169921875,189.850212097168,190.1953735351562,190.5531005859375,190.5531005859375,190.9226531982422,191.0302200317383,191.0302200317383,189.3743515014648,189.6373901367188,189.9178924560547,190.2338333129883,190.2338333129883,190.5823287963867,190.5823287963867,190.9447021484375,190.9447021484375,191.08203125,191.08203125,189.4407119750977,189.7238616943359,190.0478134155273,190.0478134155273,190.3956527709961,190.3956527709961,190.7546081542969,190.7546081542969,191.1316070556641,191.1331253051758,191.1331253051758,191.1331253051758,189.6191635131836,189.6191635131836,189.9400634765625,189.9400634765625,190.2795867919922,190.2795867919922,190.6337356567383,190.6337356567383,190.982666015625,191.1833114624023,191.1833114624023,191.1833114624023,189.516242980957,189.516242980957,189.769157409668,189.769157409668,190.0660095214844,190.0660095214844,190.3999252319336,190.7586135864258,190.7586135864258,191.1320114135742,191.1320114135742,191.2327499389648,191.2327499389648,191.2327499389648,189.7073287963867,189.9901657104492,189.9901657104492,190.3168869018555,190.3168869018555,190.6722412109375,190.6722412109375,191.0391616821289,191.0391616821289,191.2812957763672,191.2812957763672,191.2812957763672,189.6831512451172,189.6831512451172,189.9516067504883,189.9516067504883,190.2565841674805,190.2565841674805,190.5999603271484,190.9619979858398,190.9619979858398,191.3291091918945,191.3291091918945,191.3291091918945,191.3291091918945,191.3291091918945,191.3291091918945,189.9355773925781,189.9355773925781,190.2335586547852,190.2335586547852,190.5737533569336,190.5737533569336,190.9340209960938,190.9340209960938,191.3550415039062,191.3760986328125,191.3760986328125,189.9815444946289,189.9815444946289,190.2770156860352,190.2770156860352,190.2770156860352,190.6151885986328,190.6151885986328,190.9750595092773,190.9750595092773,190.9750595092773,191.3549575805664,191.3549575805664,191.4223937988281,191.4223937988281,191.4223937988281,191.4223937988281,191.4223937988281,191.4223937988281,191.4223937988281,191.4223937988281,191.4223937988281,191.4223937988281,191.4223937988281,191.4223937988281,191.4223937988281,191.4223937988281,191.4223937988281,191.4223937988281,191.4223937988281,191.4223937988281,191.4223937988281,191.4223937988281,191.4223937988281,191.4223937988281,191.4223937988281,191.4223937988281,191.4223937988281,191.4223937988281,191.4223937988281,191.4223937988281,191.4223937988281,191.4223937988281,191.4223937988281,191.4223937988281,191.4223937988281,191.4223937988281,191.4223937988281,191.4223937988281,191.4223937988281,191.4223937988281,191.4223937988281,191.4223937988281,191.4223937988281,191.4223937988281,191.4223937988281,191.4223937988281,191.4223937988281,191.4223937988281,191.4223937988281,191.4223937988281,189.8288879394531,189.8288879394531,189.9632339477539,190.2197799682617,190.5021896362305,190.8207855224609,190.8207855224609,191.1496963500977,191.4826812744141,191.8687973022461,192.2795791625977,192.2795791625977,192.6815795898438,192.6815795898438,193.0254364013672,193.3667831420898,193.3667831420898,193.708137512207,194.0501251220703,194.0501251220703,194.3883895874023,194.3883895874023,194.6811065673828,194.6811065673828,194.6811065673828,194.6811065673828,194.6811065673828,194.6811065673828,190.3386077880859,190.3386077880859,190.6900482177734,191.0525817871094,191.3974075317383,191.3974075317383,191.7968139648438,191.7968139648438,191.7968139648438,192.2197189331055,192.2197189331055,192.6152572631836,192.6152572631836,193.0246505737305,193.473991394043,193.473991394043,193.8818511962891,194.2887115478516,194.2887115478516,194.6838836669922,194.6838836669922,194.8137741088867,194.8137741088867,194.8137741088867,190.3630676269531,190.6772766113281,190.6772766113281,191.0224761962891,191.0224761962891,191.0224761962891,191.3611221313477,191.3611221313477,191.711555480957,191.711555480957,191.711555480957,192.1190338134766,192.1190338134766,192.5392532348633,192.5392532348633,192.9472579956055,192.9472579956055,193.3545303344727,193.3545303344727,193.7592544555664,194.1645126342773,194.1645126342773,194.5712661743164,194.5712661743164,194.9443511962891,194.9443511962891,194.9443511962891,194.9443511962891,194.9443511962891,194.9443511962891,190.6773529052734,190.6773529052734,190.6773529052734,190.9999771118164,191.3364791870117,191.3364791870117,191.6672134399414,191.6672134399414,192.0472717285156,192.0472717285156,192.4603576660156,192.4603576660156,192.8720092773438,192.8720092773438,193.2772216796875,193.2772216796875,193.6813049316406,193.6813049316406,194.0856170654297,194.0856170654297,194.4906692504883,194.4906692504883,194.8894882202148,194.8894882202148,195.0728302001953,195.0728302001953,195.0728302001953,190.715690612793,190.715690612793,191.0115280151367,191.0115280151367,191.3363952636719,191.6538314819336,191.6538314819336,192.010871887207,192.010871887207,192.3981704711914,192.3981704711914,192.8494567871094,192.8494567871094,193.2546310424805,193.2546310424805,193.6579666137695,194.0607986450195,194.0607986450195,194.464958190918,194.8694915771484,195.1991500854492,195.1991500854492,195.1991500854492,195.1991500854492,191.0943756103516,191.0943756103516,191.4068984985352,191.4068984985352,191.7190551757812,191.7190551757812,192.063232421875,192.063232421875,192.4386825561523,192.4386825561523,192.8428039550781,193.2506866455078,193.6560363769531,194.0618743896484,194.0618743896484,194.467887878418,194.467887878418,194.8748321533203,194.8748321533203,195.2689514160156,195.2689514160156,195.3235473632812,195.3235473632812,195.3235473632812,195.3235473632812,191.1888198852539,191.1888198852539,191.4879455566406,191.4879455566406,191.796257019043,191.796257019043,192.1298675537109,192.1298675537109,192.496452331543,192.496452331543,192.8908996582031,192.8908996582031,193.3002624511719,193.3002624511719,193.7040328979492,193.7040328979492,194.1085205078125,194.1085205078125,194.5128707885742,194.9185180664062,194.9185180664062,195.3170318603516,195.3170318603516,195.3170318603516,195.4458618164062,195.4458618164062,195.4458618164062,191.3242111206055,191.3242111206055,191.6153411865234,191.6153411865234,191.9162445068359,191.9162445068359,192.2801818847656,192.2801818847656,192.6416778564453,192.6416778564453,193.0303649902344,193.0303649902344,193.4372711181641,193.4372711181641,193.838623046875,193.838623046875,193.838623046875,194.2416534423828,194.2416534423828,194.6450729370117,194.6450729370117,195.0497817993164,195.0497817993164,195.4471740722656,195.4471740722656,195.5662155151367,195.5662155151367,191.5154113769531,191.5154113769531,191.8010864257812,192.0941314697266,192.0941314697266,192.4279556274414,192.4279556274414,192.7874603271484,192.7874603271484,192.7874603271484,193.1682968139648,193.5758514404297,193.5758514404297,193.9769897460938,193.9769897460938,194.3807830810547,194.3807830810547,194.3807830810547,194.7838668823242,194.7838668823242,195.1893539428711,195.1893539428711,195.5847549438477,195.5847549438477,195.6846237182617,195.6846237182617,191.7146606445312,191.7146606445312,191.993522644043,191.993522644043,192.2805709838867,192.6193084716797,192.6193084716797,192.9767074584961,192.9767074584961,193.3571166992188,193.7624969482422,193.7624969482422,193.7624969482422,194.1638031005859,194.1638031005859,194.5675506591797,194.9715118408203,194.9715118408203,195.3761444091797,195.7682266235352,195.7682266235352,195.8011627197266,195.8011627197266,195.8011627197266,191.9358825683594,191.9358825683594,192.2427520751953,192.2427520751953,192.5456695556641,192.8877944946289,192.8877944946289,193.2491149902344,193.2491149902344,193.6321792602539,193.6321792602539,194.0371475219727,194.0371475219727,194.4361801147461,194.4361801147461,194.8388977050781,194.8388977050781,195.2412338256836,195.6438064575195,195.6438064575195,195.9158020019531,195.9158020019531,195.9158020019531,195.9158020019531,195.9158020019531,195.9158020019531,192.2031021118164,192.2031021118164,192.4804229736328,192.8009872436523,192.8009872436523,193.1484603881836,193.5122222900391,193.5122222900391,193.9033584594727,194.3092422485352,194.709831237793,194.709831237793,195.1158447265625,195.1158447265625,195.5199508666992,195.5199508666992,195.9167022705078,195.9167022705078,196.0285339355469,196.0285339355469,196.0285339355469,192.2277374267578,192.2277374267578,192.4964599609375,192.7817916870117,193.1091537475586,193.1091537475586,193.4599304199219,193.8297119140625,193.8297119140625,194.2287139892578,194.2287139892578,194.6340789794922,194.6340789794922,195.0388946533203,195.0388946533203,195.0388946533203,195.4436874389648,195.848876953125,195.848876953125,196.139518737793,196.139518737793,196.139518737793,196.139518737793,192.576286315918,192.576286315918,192.8584518432617,192.8584518432617,193.1832122802734,193.1832122802734,193.1832122802734,193.5292282104492,193.8923110961914,193.8923110961914,194.283073425293,194.6863403320312,194.6863403320312,195.0888595581055,195.0888595581055,195.4948120117188,195.8967514038086,195.8967514038086,196.2487564086914,196.2487564086914,196.2487564086914,196.2487564086914,192.667350769043,192.9301528930664,192.9301528930664,193.2389755249023,193.5736236572266,193.5736236572266,193.9275588989258,193.9275588989258,194.3057632446289,194.7101898193359,194.7101898193359,195.1092224121094,195.1092224121094,195.5143737792969,195.5143737792969,195.9190902709961,196.3135604858398,196.3561401367188,196.3561401367188,196.3561401367188,192.7792053222656,192.7792053222656,193.0392608642578,193.0392608642578,193.0392608642578,193.3412322998047,193.3412322998047,193.6660461425781,193.6660461425781,194.014404296875,194.014404296875,194.3853759765625,194.3853759765625,194.7852630615234,194.7852630615234,195.1858291625977,195.1858291625977,195.6315383911133,196.0362243652344,196.0362243652344,196.4306564331055,196.4306564331055,196.461784362793,196.461784362793,192.9501953125,192.9501953125,193.2121658325195,193.5106735229492,193.5106735229492,193.5106735229492,193.8324737548828,193.8324737548828,194.1799392700195,194.1799392700195,194.1799392700195,194.5456085205078,194.5456085205078,194.9447174072266,195.3456420898438,195.3456420898438,195.7502517700195,196.1561508178711,196.1561508178711,196.5516662597656,196.5516662597656,196.5658645629883,196.5658645629883,196.5658645629883,193.1157760620117,193.1157760620117,193.1157760620117,193.3754806518555,193.3754806518555,193.3754806518555,193.6697540283203,193.6697540283203,193.6697540283203,193.9874114990234,194.3318023681641,194.3318023681641,194.6962127685547,195.0921630859375,195.0921630859375,195.494010925293,195.494010925293,195.494010925293,195.8986434936523,195.8986434936523,196.3046951293945,196.3046951293945,196.6681060791016,196.6681060791016,196.6681060791016,196.6681060791016,196.6681060791016,196.6681060791016,193.3025131225586,193.3025131225586,193.5683212280273,193.5683212280273,193.8650817871094,193.8650817871094,193.8650817871094,194.1874008178711,194.5399856567383,194.5399856567383,194.9110641479492,194.9110641479492,195.3115005493164,195.7600860595703,196.1682434082031,196.1682434082031,196.5711288452148,196.5711288452148,196.7687835693359,196.7687835693359,193.3143768310547,193.3143768310547,193.3143768310547,193.5642318725586,193.5642318725586,193.8427124023438,193.8427124023438,194.144905090332,194.144905090332,194.477409362793,194.477409362793,194.8360824584961,195.2103958129883,195.2103958129883,195.6085433959961,195.6085433959961,196.0007400512695,196.0007400512695,196.0007400512695,196.4067687988281,196.4067687988281,196.8027114868164,196.8677825927734,196.8677825927734,196.8677825927734,193.5531387329102,193.5531387329102,193.5531387329102,193.806022644043,193.806022644043,194.0874557495117,194.0874557495117,194.3938674926758,194.3938674926758,194.7316513061523,194.7316513061523,195.0914688110352,195.4824447631836,195.8863143920898,196.2891387939453,196.6952590942383,196.9652633666992,196.9652633666992,196.9652633666992,196.9652633666992,196.9652633666992,196.9652633666992,196.9652633666992,196.9652633666992,196.9652633666992,196.9652633666992,196.9652633666992,196.9652633666992,196.9652633666992,196.9652633666992,196.9652633666992,196.9652633666992,196.9652633666992,196.9652633666992,196.9652633666992,196.9652633666992,196.9652633666992,196.9652633666992,196.9652633666992,196.9652633666992,196.9652633666992,196.9652633666992,196.9652633666992,196.9652633666992,196.9652633666992,196.9652633666992,196.9652633666992,196.9652633666992,196.9652633666992,196.9652633666992,196.9652633666992,196.9652633666992,193.612190246582,193.612190246582,193.612190246582,193.6543197631836,193.6543197631836,193.6543197631836,193.8515243530273,193.8515243530273,194.0783157348633,194.3175888061523,194.3175888061523,194.5846862792969,194.5846862792969,194.888313293457,195.2114181518555,195.5491333007812,195.5491333007812,195.916015625,195.916015625,196.3166122436523,196.7220230102539,196.7220230102539,197.0608520507812,197.0608520507812,197.0608520507812,197.0608520507812,197.0608520507812,197.0608520507812,193.9280319213867,193.9280319213867,193.9280319213867,194.1914825439453,194.4807510375977,194.4807510375977,194.7974853515625,195.1410903930664,195.1410903930664,195.1410903930664,195.4957046508789,195.4957046508789,195.8765106201172,195.8765106201172,195.8765106201172,196.2741317749023,196.2741317749023,196.7137756347656,197.1204833984375,197.1204833984375,197.1551971435547,197.1551971435547,197.1551971435547,194.0125350952148,194.2633972167969,194.5392837524414,194.5392837524414,194.8470458984375,194.8470458984375,195.1862945556641,195.5366668701172,195.5366668701172,195.9018630981445,195.9018630981445,196.2879409790039,196.6854934692383,196.6854934692383,197.0799942016602,197.0799942016602,197.2479629516602,197.2479629516602,194.0742034912109,194.3167266845703,194.3167266845703,194.5824432373047,194.5824432373047,194.8779067993164,194.8779067993164,194.8779067993164,195.1787796020508,195.5111923217773,195.5111923217773,195.8579177856445,196.2151870727539,196.6033401489258,196.6033401489258,197.0055465698242,197.0055465698242,197.3393020629883,197.3393020629883,197.3393020629883,197.3393020629883,197.3393020629883,197.3393020629883,194.3561782836914,194.6128921508789,194.6128921508789,194.8969955444336,195.246337890625,195.246337890625,195.5939331054688,195.5939331054688,195.9549407958984,196.3377838134766,196.3377838134766,196.7355651855469,197.1423187255859,197.1423187255859,197.429069519043,197.429069519043,197.429069519043,197.429069519043,197.429069519043,197.429069519043,194.5247497558594,194.5247497558594,194.7820434570312,194.7820434570312,195.0669860839844,195.0669860839844,195.387565612793,195.387565612793,195.7332916259766,195.7332916259766,196.0919952392578,196.4704666137695,196.4704666137695,196.8686065673828,196.8686065673828,196.8686065673828,197.2685165405273,197.2685165405273,197.5175094604492,197.5175094604492,197.5175094604492,197.5175094604492,197.5175094604492,197.5175094604492,194.6773681640625,194.9343643188477,194.9343643188477,195.222900390625,195.5461120605469,195.5461120605469,195.8935012817383,195.8935012817383,196.2507705688477,196.6279373168945,196.6279373168945,197.0267944335938,197.4268264770508,197.4268264770508,197.6044082641602,197.6044082641602,197.6044082641602,194.6128005981445,194.6128005981445,194.6128005981445,194.8461608886719,194.8461608886719,195.1046371459961,195.1046371459961,195.3957672119141,195.3957672119141,195.7540969848633,195.7540969848633,195.7540969848633,196.1036376953125,196.1036376953125,196.4641189575195,196.8465881347656,196.8465881347656,197.2477951049805,197.6488647460938,197.6488647460938,197.6899642944336,197.6899642944336,197.6899642944336,194.8326797485352,195.0728530883789,195.0728530883789,195.3434219360352,195.3434219360352,195.6456069946289,195.6456069946289,195.9836273193359,196.3345108032227,196.3345108032227,196.7043151855469,197.0930938720703,197.4944076538086,197.4944076538086,197.7741394042969,197.7741394042969,197.7741394042969,197.7741394042969,197.7741394042969,197.7741394042969,197.7741394042969,197.7741394042969,195.0456237792969,195.0456237792969,195.2976379394531,195.5726623535156,195.8866577148438,195.8866577148438,196.2281875610352,196.2281875610352,196.5790710449219,196.5790710449219,196.9523696899414,196.9523696899414,197.3491134643555,197.3491134643555,197.7488098144531,197.7488098144531,197.8569259643555,197.8569259643555,197.8569259643555,195.0485000610352,195.0485000610352,195.3082427978516,195.5751953125,195.8720321655273,195.8720321655273,196.2070770263672,196.5412750244141,196.5412750244141,196.9064407348633,196.9064407348633,197.2919769287109,197.2919769287109,197.6936569213867,197.6936569213867,197.9383926391602,197.9383926391602,197.9383926391602,197.9383926391602,197.9383926391602,197.9383926391602,195.3316268920898,195.3316268920898,195.5862426757812,195.871940612793,195.871940612793,196.1930694580078,196.1930694580078,196.542236328125,196.542236328125,196.9040908813477,196.9040908813477,196.9040908813477,197.2882080078125,197.2882080078125,197.6906280517578,198.0185317993164,198.0185317993164,198.0185317993164,198.0185317993164,198.0185317993164,198.0185317993164,195.4017868041992,195.4017868041992,195.6480178833008,195.6480178833008,195.9259338378906,195.9259338378906,196.2379455566406,196.2379455566406,196.5812225341797,196.5812225341797,196.9383239746094,197.3147201538086,197.3147201538086,197.7133483886719,197.7133483886719,198.0973434448242,198.0973434448242,198.0973434448242,198.0973434448242,195.4970550537109,195.7732315063477,195.7732315063477,196.0569915771484,196.0569915771484,196.3798446655273,196.3798446655273,196.7255249023438,196.7255249023438,196.7255249023438,197.0857772827148,197.0857772827148,197.47216796875,197.47216796875,197.47216796875,197.8737640380859,198.1749572753906,198.1749572753906,198.1749572753906,198.1749572753906,198.1749572753906,198.1749572753906,195.6635971069336,195.6635971069336,195.9133834838867,196.1967163085938,196.1967163085938,196.5183334350586,196.5183334350586,196.8689804077148,197.2292251586914,197.2292251586914,197.6139755249023,197.6139755249023,198.01220703125,198.2513198852539,198.2513198852539,198.2513198852539,198.2513198852539,198.2513198852539,198.2513198852539,195.820426940918,195.820426940918,196.0737991333008,196.0737991333008,196.360954284668,196.6828765869141,197.0294418334961,197.3909225463867,197.3909225463867,197.7740097045898,197.7740097045898,197.7740097045898,198.1727066040039,198.1727066040039,198.3263931274414,198.3263931274414,198.3263931274414,195.7535629272461,195.7535629272461,196.0104827880859,196.2722244262695,196.570182800293,196.570182800293,196.8967666625977,196.8967666625977,197.2434844970703,197.605583190918,197.9906616210938,197.9906616210938,198.38818359375,198.4002456665039,198.4002456665039,198.4002456665039,195.9400405883789,195.9400405883789,196.175163269043,196.175163269043,196.4382171630859,196.4382171630859,196.7397155761719,196.7397155761719,197.0753784179688,197.0753784179688,197.0753784179688,197.4261627197266,197.4261627197266,197.7907867431641,197.7907867431641,198.1791229248047,198.1791229248047,198.4730224609375,198.4730224609375,198.4730224609375,198.4730224609375,198.4730224609375,198.4730224609375,196.1150436401367,196.3632354736328,196.6467742919922,196.6467742919922,196.9671783447266,196.9671783447266,196.9671783447266,197.3147888183594,197.3147888183594,197.6717529296875,197.6717529296875,198.0505447387695,198.0505447387695,198.452751159668,198.452751159668,198.5445175170898,198.5445175170898,198.5445175170898,196.1187286376953,196.1187286376953,196.3779373168945,196.6456451416016,196.6456451416016,196.9500961303711,196.9500961303711,197.2884140014648,197.2884140014648,197.6426544189453,198.0140075683594,198.0140075683594,198.4071426391602,198.614860534668,198.614860534668,198.614860534668,198.614860534668,198.614860534668,198.614860534668,196.3937606811523,196.3937606811523,196.6458740234375,196.9320602416992,197.2550048828125,197.2550048828125,197.2550048828125,197.6043548583984,197.6043548583984,197.9651718139648,197.9651718139648,198.3524856567383,198.6841201782227,198.6841201782227,198.6841201782227,198.6841201782227,198.6841201782227,198.6841201782227,198.6841201782227,198.6841201782227,198.6841201782227,198.6841201782227,198.6841201782227,198.6841201782227,198.6841201782227,198.6841201782227,198.6841201782227,198.6841201782227,198.6841201782227,198.6841201782227,198.6841201782227,198.6841201782227,198.6841201782227,198.6841201782227,198.6841201782227,198.6841201782227,198.6841201782227,198.6841201782227,198.6841201782227,198.6841201782227,198.6841201782227,198.6841201782227,196.3390274047852,196.3390274047852,196.5471649169922,196.5471649169922,196.7698440551758,196.7698440551758,197.0128707885742,197.0128707885742,197.2836380004883,197.2836380004883,197.5918807983398,197.9241790771484,198.2721328735352,198.2721328735352,198.6398696899414,198.7521286010742,198.7521286010742,196.4139099121094,196.6123046875,196.6123046875,196.8636322021484,196.8636322021484,197.1522598266602,197.1522598266602,197.4740676879883,197.4740676879883,197.8208084106445,198.182487487793,198.182487487793,198.182487487793,198.5648498535156,198.5648498535156,198.8191528320312,198.8191528320312,198.8191528320312,198.8191528320312,198.8191528320312,198.8191528320312,196.6654052734375,196.6654052734375,196.911018371582,197.1906356811523,197.1906356811523,197.1906356811523,197.5113983154297,197.5113983154297,197.8577651977539,197.8577651977539,198.2144241333008,198.5975952148438,198.5975952148438,198.8851928710938,198.8851928710938,198.8851928710938,198.8851928710938,198.8851928710938,198.8851928710938,196.7880020141602,197.0376586914062,197.3227386474609,197.3227386474609,197.642822265625,197.989501953125,197.989501953125,198.3497772216797,198.3497772216797,198.3497772216797,198.7370834350586,198.9500579833984,198.9500579833984,198.9500579833984,198.9500579833984,198.9500579833984,198.9500579833984,196.9060897827148,196.9060897827148,197.1557769775391,197.1557769775391,197.4425735473633,197.7673797607422,198.1191558837891,198.1191558837891,198.4801712036133,198.8687973022461,198.8687973022461,198.8687973022461,199.0139083862305,199.0139083862305,199.0139083862305,199.0139083862305,199.0139083862305,199.0139083862305,197.0381240844727,197.2915115356445,197.2915115356445,197.5837478637695,197.5837478637695,197.9118881225586,197.9118881225586,198.2637405395508,198.6177597045898,198.9954452514648,198.9954452514648,199.0766983032227,199.0766983032227,196.9289016723633,197.1942367553711,197.1942367553711,197.4691925048828,197.7827987670898,197.7827987670898,197.7827987670898,198.1295471191406,198.1295471191406,198.4929428100586,198.4929428100586,198.4929428100586,198.8793182373047,198.8793182373047,199.1385269165039,199.1385269165039,199.1385269165039,199.1385269165039,199.1385269165039,199.1385269165039,199.1385269165039,199.1385269165039,197.1718368530273,197.4191436767578,197.4191436767578,197.7033843994141,197.7033843994141,198.0255737304688,198.0255737304688,198.3712463378906,198.7305068969727,198.7305068969727,199.114631652832,199.199333190918,199.199333190918,199.199333190918,197.131591796875,197.131591796875,197.3610076904297,197.6195907592773,197.6195907592773,197.9105987548828,198.2366027832031,198.2366027832031,198.586311340332,198.586311340332,198.586311340332,198.9479827880859,198.9479827880859,199.2591094970703,199.2591094970703,199.2591094970703,199.2591094970703,199.2591094970703,199.2591094970703,197.3132019042969,197.5511169433594,197.5511169433594,197.8251876831055,197.8251876831055,198.1392822265625,198.1392822265625,198.1392822265625,198.5192260742188,198.5192260742188,198.8766174316406,198.8766174316406,199.2614898681641,199.3179779052734,199.3179779052734,199.3179779052734,197.3275604248047,197.5581359863281,197.8202896118164,197.8202896118164,198.1245498657227,198.1245498657227,198.4635391235352,198.4635391235352,198.8178253173828,198.8178253173828,199.1909255981445,199.1909255981445,199.3758697509766,199.3758697509766,199.3758697509766,199.3758697509766,199.3758697509766,199.3758697509766,197.5666122436523,197.5666122436523,197.8129959106445,197.8129959106445,198.0995788574219,198.0995788574219,198.4236907958984,198.7689819335938,198.7689819335938,198.7689819335938,199.128059387207,199.4328308105469,199.4328308105469,199.4328308105469,199.4328308105469,199.4328308105469,199.4328308105469,197.5724258422852,197.5724258422852,197.8097381591797,197.8097381591797,198.0837860107422,198.0837860107422,198.0837860107422,198.3998260498047,198.3998260498047,198.74462890625,198.74462890625,198.74462890625,199.1020660400391,199.1020660400391,199.4888687133789,199.4888687133789,199.4888687133789,199.4888687133789,197.6375961303711,197.6375961303711,197.8711547851562,198.1377029418945,198.4454879760742,198.7846832275391,199.1414642333984,199.1414642333984,199.1414642333984,199.5122756958008,199.5122756958008,199.5440063476562,199.5440063476562,199.5440063476562,197.6871337890625,197.6871337890625,197.917350769043,197.917350769043,198.1779708862305,198.4772567749023,198.8092575073242,198.8092575073242,199.1628646850586,199.1628646850586,199.5301895141602,199.5982437133789,199.5982437133789,199.5982437133789,199.5982437133789,199.5982437133789,199.5982437133789,199.5982437133789,199.5982437133789,199.5982437133789,199.5982437133789,199.5982437133789,199.5982437133789,199.5982437133789,199.5982437133789,199.5982437133789,197.730712890625,197.730712890625,197.730712890625,197.8283004760742,198.0714645385742,198.0714645385742,198.3151779174805,198.3151779174805,198.592903137207,198.9061965942383,198.9061965942383,199.2422180175781,199.5873794555664,199.5873794555664,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,199.6516036987305,197.8142166137695,197.8142166137695,197.8142166137695,197.8142166137695,197.9451675415039,197.9451675415039,198.196403503418,198.196403503418,198.4750595092773,198.4750595092773,198.7872314453125,198.7872314453125,199.1243209838867,199.1243209838867,199.4529876708984,199.4529876708984,199.7950057983398,199.7950057983398,200.1843948364258,200.1843948364258,200.1843948364258,200.5907897949219,200.5907897949219,200.9850921630859,200.9850921630859,200.9850921630859,201.359375,201.359375,201.6968154907227,201.6968154907227,202.0351181030273,202.0351181030273,202.3734512329102,202.3734512329102,202.7118148803711,202.7118148803711,203.0497817993164,203.0497817993164,203.3878784179688,203.3878784179688,203.7259063720703,204.0638122558594,204.0638122558594,204.4013061523438,204.7393798828125,204.7393798828125,205.0772399902344,205.0772399902344,205.4146118164062,205.4146118164062,205.4802780151367,205.4802780151367,205.4802780151367,205.4802780151367,205.4802780151367,205.4802780151367,198.3276596069336,198.3276596069336,198.6075286865234,198.6075286865234,198.6075286865234,198.9242248535156,198.9242248535156,199.2660903930664,199.2660903930664,199.5954360961914,199.5954360961914,199.9374923706055,200.3208389282227,200.3208389282227,200.7201690673828,201.1210479736328,201.1210479736328,201.1210479736328,201.5279541015625,201.5279541015625,201.9320755004883,201.9320755004883,202.3372344970703,202.3372344970703,202.7405242919922,202.7405242919922,203.1458435058594,203.1458435058594,203.5523223876953,203.957405090332,204.3633041381836,204.3633041381836,204.3633041381836,204.7689819335938,205.1696319580078,205.1696319580078,205.1696319580078,205.5589752197266,205.5589752197266,205.690055847168,205.690055847168,205.690055847168,205.690055847168,198.6175689697266,198.6175689697266,198.8807983398438,198.8807983398438,199.1803436279297,199.1803436279297,199.506721496582,199.506721496582,199.824333190918,199.824333190918,200.1588439941406,200.1588439941406,200.5151672363281,200.8719253540039,200.8719253540039,201.2476196289062,201.2476196289062,201.6361694335938,201.6361694335938,202.0334014892578,202.0334014892578,202.4334945678711,202.4334945678711,202.4334945678711,202.8287048339844,202.8287048339844,203.2196044921875,203.2196044921875,203.6136169433594,204.0031356811523,204.0031356811523,204.0031356811523,204.3762359619141,204.3762359619141,204.7436294555664,204.7436294555664,205.1317672729492,205.5214996337891,205.5214996337891,205.8963165283203,205.8963165283203,205.8963165283203,205.8963165283203,205.8963165283203,205.8963165283203,198.976318359375,199.236686706543,199.236686706543,199.236686706543,199.5244369506836,199.5244369506836,199.8349304199219,200.1700134277344,200.1700134277344,200.5281600952148,200.5281600952148,200.888786315918,200.888786315918,201.2509689331055,201.2509689331055,201.6303482055664,201.6303482055664,201.6303482055664,202.0232543945312,202.0232543945312,202.0232543945312,202.4145812988281,202.4145812988281,202.80322265625,202.80322265625,203.2035369873047,203.5991668701172,203.5991668701172,203.9919509887695,204.3910903930664,204.7880325317383,204.7880325317383,205.1795806884766,205.5780334472656,205.5780334472656,205.9687957763672,205.9687957763672,206.0992431640625,206.0992431640625,206.0992431640625,206.0992431640625,199.1848220825195,199.4328231811523,199.4328231811523,199.6975631713867,199.6975631713867,199.9863967895508,199.9863967895508,200.2785797119141,200.2785797119141,200.6094284057617,200.9627456665039,200.9627456665039,201.3158264160156,201.3158264160156,201.673095703125,201.673095703125,201.673095703125,202.0489654541016,202.0489654541016,202.4360580444336,202.4360580444336,202.8702087402344,202.8702087402344,202.8702087402344,203.2657165527344,203.2657165527344,203.2657165527344,203.6578826904297,203.6578826904297,204.0485687255859,204.4325103759766,204.8253402709961,204.8253402709961,205.2205200195312,205.2205200195312,205.2205200195312,205.6105804443359,205.6105804443359,205.9967727661133,206.2989959716797,206.2989959716797,206.2989959716797,206.2989959716797,206.2989959716797,206.2989959716797,206.2989959716797,206.2989959716797,206.2989959716797,199.6194458007812,199.6194458007812,199.6194458007812,199.8589401245117,200.1190567016602,200.1190567016602,200.4222183227539,200.4222183227539,200.7289505004883,201.0695877075195,201.0695877075195,201.4245529174805,201.4245529174805,201.7899475097656,202.1626815795898,202.55029296875,202.9448623657227,203.3395309448242,203.3395309448242,203.7320785522461,203.7320785522461,203.7320785522461,204.1286392211914,204.1286392211914,204.5253753662109,204.9195098876953,204.9195098876953,205.3131637573242,205.7059783935547,205.7059783935547,206.1023941040039,206.1023941040039,206.4892730712891,206.4954605102539,206.4954605102539,206.4954605102539,206.4954605102539,206.4954605102539,206.4954605102539,199.8744888305664,199.8744888305664,200.1242599487305,200.4205703735352,200.4205703735352,200.6968460083008,201.0185928344727,201.0185928344727,201.364875793457,201.7224655151367,201.7224655151367,202.0923461914062,202.0923461914062,202.4699935913086,202.4699935913086,202.8574829101562,203.2471618652344,203.2471618652344,203.2471618652344,203.633903503418,203.633903503418,204.0103073120117,204.0103073120117,204.3909606933594,204.3909606933594,204.7890472412109,204.7890472412109,205.1847610473633,205.1847610473633,205.5795364379883,205.9723358154297,205.9723358154297,206.3625411987305,206.3625411987305,206.6887588500977,206.6887588500977,206.6887588500977,206.6887588500977,206.6887588500977,206.6887588500977,206.6887588500977,206.6887588500977,206.6887588500977,206.6887588500977,206.6887588500977,206.6887588500977,206.6887588500977,206.6887588500977,206.6887588500977,206.6887588500977,206.6887588500977,206.6887588500977,206.6887588500977,206.6887588500977,206.6887588500977,206.6887588500977,206.6887588500977,206.6887588500977,200.0374450683594,200.0374450683594,200.0374450683594,200.0374450683594,200.0374450683594,200.0374450683594,200.1394500732422,200.1394500732422,200.3800277709961,200.3800277709961,200.6257629394531,200.8811264038086,200.8811264038086,201.1771545410156,201.1771545410156,201.5102081298828,201.840461730957,201.840461730957,202.1876220703125,202.569091796875,202.569091796875,202.9649200439453,202.9649200439453,203.3616790771484,203.3616790771484,203.7977142333984,203.7977142333984,204.1944885253906,204.1944885253906,204.1944885253906,204.593864440918,204.593864440918,204.9936218261719,204.9936218261719,205.3950958251953,205.3950958251953,205.7276458740234,205.7276458740234,205.9736251831055,205.9736251831055,206.3321151733398,206.737907409668,206.8787612915039,206.8787612915039,206.8787612915039,206.8787612915039,206.8787612915039,206.8787612915039,206.8787612915039,206.8787612915039,200.3609313964844,200.3609313964844,200.5837707519531,200.821891784668,200.821891784668,201.0651245117188,201.0651245117188,201.3404922485352,201.3404922485352,201.6523132324219,201.9711227416992,201.9711227416992,201.9711227416992,202.3262634277344,202.3262634277344,202.6483154296875,202.9525451660156,202.9525451660156,203.2034912109375,203.2034912109375,203.4791259765625,203.4791259765625,203.7383270263672,203.7383270263672,203.7383270263672,204.0203475952148,204.0203475952148,204.3254623413086,204.3254623413086,204.6492691040039,204.9857864379883,204.9857864379883,205.3327331542969,205.3327331542969,205.6958694458008,206.0744323730469,206.0744323730469,206.424560546875,206.424560546875,206.7909088134766,206.7909088134766,207.0659027099609,207.0659027099609,207.0659027099609,207.0659027099609,207.0659027099609,207.0659027099609,207.0659027099609,207.0659027099609,207.0659027099609,200.7212371826172,200.7212371826172,200.7212371826172,200.9516067504883,200.9516067504883,201.1877899169922,201.4325790405273,201.7255096435547,201.7255096435547,202.0334396362305,202.0334396362305,202.0334396362305,202.3593368530273,202.6935653686523,202.6935653686523,203.0355758666992,203.0355758666992,203.389030456543,203.389030456543,211.3409652709961,211.3409652709961,211.3409652709961,211.3409652709961,211.3409652709961,211.3409652709961,211.3409652709961,211.3409652709961,211.3409652709961,211.3409652709961,211.3409652709961,211.3409652709961,211.3409652709961,211.3409652709961,211.3409652709961,211.3409652709961,211.3409652709961,211.3409652709961,211.3409652709961,211.3409652709961,211.3409652709961,211.3409652709961,218.9703598022461,218.9703674316406,218.9703674316406,218.9703674316406,218.9703674316406,218.9703674316406,218.9703674316406,218.9703674316406,218.9703674316406,218.9703674316406,218.9703674316406,218.9703674316406,218.9703674316406,218.9703674316406,218.9703674316406,218.9703674316406,218.9703674316406,218.9703674316406,218.9703674316406,218.9703674316406,218.9703674316406,218.9703674316406,218.9703674316406,218.9703674316406,218.9703674316406,234.2291564941406,234.2291564941406,234.2291564941406,234.2291564941406,234.2291564941406,234.2291564941406,234.2291564941406,234.2291564941406,234.2291564941406,234.2291564941406,234.2291564941406,234.2291564941406,234.2291564941406,234.2291564941406,234.2291564941406,234.2291564941406,234.2291564941406,234.2291564941406,241.9217224121094,241.9217224121094,241.9217224121094,241.9217224121094,241.9217224121094,241.9217224121094,241.9217224121094,241.9217224121094,241.9217224121094,241.9217224121094,241.9217224121094,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984,257.2537689208984],"meminc":[0,0,0,0,2.288818359375e-05,0,15.28221130371094,0,0,0.0003662109375,0,0,30.46537780761719,0,0,0,0,0,4.57763671875e-05,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-0.00030517578125,0,15.37364959716797,0,0.24163818359375,0.257354736328125,0.2669143676757812,0,0.3169097900390625,0,0.3806304931640625,0,0.3517913818359375,0.386749267578125,0,0.406402587890625,0,0.4061126708984375,0,0.1379013061523438,0,0,-2.800582885742188,0,0.3734359741210938,0,0.4183120727539062,0,0.4146347045898438,0,0.405914306640625,0,0,0.4060440063476562,0,0.4103012084960938,0.4083023071289062,0,-2.96514892578125,0,0,0.3455581665039062,0.3609619140625,0.3745803833007812,0,0.3980026245117188,0,0,0.4018478393554688,0,0.3999176025390625,0,0.403717041015625,0,0.4015045166015625,0,0,-2.919670104980469,0,0.3471450805664062,0.3640594482421875,0,0.3806381225585938,0,0.3969497680664062,0.4105453491210938,0,0.4113311767578125,0,0.4141082763671875,0.2807769775390625,0,0,-2.769912719726562,0,0.3479537963867188,0,0.368499755859375,0,0.3868408203125,0.399993896484375,0.4058761596679688,0.4083328247070312,0.409210205078125,0.1276931762695312,0,-2.565902709960938,0.3598861694335938,0,0.3723678588867188,0.3958206176757812,0,0.4014739990234375,0,0.4096527099609375,0.4094696044921875,0.3004150390625,0,0,-2.698204040527344,0.34393310546875,0.364990234375,0.37548828125,0,0.3923873901367188,0,0.3976364135742188,0,0.4043045043945312,0.4101028442382812,0.0911712646484375,0,0,-2.519378662109375,0.3480987548828125,0,0.360595703125,0,0.3687896728515625,0.3804931640625,0,0.3969268798828125,0,0.3943328857421875,0,0.3505935668945312,0,0,-2.698066711425781,0,0.319244384765625,0.34954833984375,0.3596572875976562,0,0.3713226318359375,0,0.385223388671875,0.3986358642578125,0,0,0.3998870849609375,0,0.1937484741210938,0,0,-2.550010681152344,0,0.3203125,0,0.3451614379882812,0.3607330322265625,0,0,0.37432861328125,0,0.4339599609375,0.4016189575195312,0,0.391815185546875,0,-2.637107849121094,0.32147216796875,0,0.3478164672851562,0,0.3620529174804688,0,0.3718338012695312,0,0.3893585205078125,0,0.4009170532226562,0,0.4026107788085938,0.1176300048828125,0,-2.383476257324219,0,0.338623046875,0,0.356781005859375,0,0,0.3683395385742188,0,0.3807296752929688,0,0.398681640625,0.4011383056640625,0.2146224975585938,0,0,-2.414558410644531,0.3311691284179688,0,0.3490219116210938,0,0.3623733520507812,0,0,0.3800811767578125,0,0,0.3983154296875,0,0.3989334106445312,0.2689132690429688,0,-2.420379638671875,0,0.3203811645507812,0,0.3389663696289062,0.3558120727539062,0.3694839477539062,0,0.389556884765625,0,0.400299072265625,0,0.318817138671875,0,0,-2.426536560058594,0.3128738403320312,0.3355331420898438,0,0.3498764038085938,0,0.4029159545898438,0,0,0.3846893310546875,0,0.3813095092773438,0.3311767578125,0,-2.402046203613281,0,0.30316162109375,0,0.3269805908203125,0,0.3458633422851562,0.3603591918945312,0.3831405639648438,0.3934097290039062,0.35980224609375,0,-2.381698608398438,0.29620361328125,0.3106307983398438,0,0.3392257690429688,0.3577499389648438,0,0.3701019287109375,0,0.3918609619140625,0.385467529296875,0,0,-2.367225646972656,0.295928955078125,0.3187637329101562,0,0.344482421875,0,0.3586502075195312,0.3806076049804688,0,0.3963470458984375,0.3408432006835938,0,0,-2.293685913085938,0,0.2958526611328125,0,0.319061279296875,0,0.3454666137695312,0,0.36077880859375,0.3815460205078125,0,0.3967437744140625,0,0.2614974975585938,0,-2.201698303222656,0,0.3244857788085938,0.3233261108398438,0.3493728637695312,0.360321044921875,0.3862228393554688,0.397125244140625,0.1270294189453125,0,-2.064834594726562,0.2991485595703125,0,0.330780029296875,0,0.352874755859375,0,0,0.3675918579101562,0.3861236572265625,0.388092041015625,0,0.00537109375,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2.241943359375,0,0.1562271118164062,0,0.2258377075195312,0.2423858642578125,0,0.2708816528320312,0.30322265625,0.33258056640625,0,0.3356704711914062,0,0,0.3700408935546875,0,0.0686798095703125,0,-1.94207763671875,0,0,0.2995758056640625,0,0.3332443237304688,0.3549346923828125,0,0.3744430541992188,0,0.3908157348632812,0,0,0.252166748046875,0,0,-2.067314147949219,0,0.2829742431640625,0,0.3162307739257812,0,0.342987060546875,0.361175537109375,0.3801193237304688,0,0.3974838256835938,0,0.0483856201171875,0,0,-1.883651733398438,0,0.2974166870117188,0,0.33282470703125,0.3538436889648438,0,0.36376953125,0,0.39129638671875,0,0,0.2055130004882812,0,0,-1.963897705078125,0,0.28424072265625,0,0.319580078125,0,0,0.3432464599609375,0,0.3606185913085938,0.3851318359375,0,0,0.3311309814453125,0,0,0,-2.028152465820312,0,0.27349853515625,0.306732177734375,0,0.3404388427734375,0,0.3584976196289062,0,0.4206695556640625,0.3873977661132812,0,0,-2.025093078613281,0,0.2773971557617188,0,0,0.3026809692382812,0,0.3413467407226562,0,0.35931396484375,0,0.3746566772460938,0,0.397308349609375,0,0.0305023193359375,0,0,-1.757781982421875,0,0.296844482421875,0.3330535888671875,0.3570938110351562,0.37359619140625,0,0.3990249633789062,0.05533599853515625,0,0,-1.739006042480469,0,0.2954864501953125,0,0.3321990966796875,0,0.3562393188476562,0.3740692138671875,0,0,0.400238037109375,0,0.03704833984375,0,0,-1.708946228027344,0,0.2929229736328125,0.3315353393554688,0.3565139770507812,0.3716049194335938,0,0.3958740234375,0,0.01583099365234375,0,0,-1.654167175292969,0,0.2982025146484375,0.3361587524414062,0,0.358489990234375,0,0.3790206909179688,0,0.3367538452148438,0,0,-1.815086364746094,0,0.2727203369140625,0.3097915649414062,0.3459625244140625,0,0.3621826171875,0,0.3843994140625,0,0.1935806274414062,0,0,-1.714591979980469,0,0.2770538330078125,0,0.3102951049804688,0.3451614379882812,0.35772705078125,0,0.3695526123046875,0.1075668334960938,0,-1.655868530273438,0.2630386352539062,0.2805023193359375,0.3159408569335938,0,0.3484954833984375,0,0.3623733520507812,0,0.1373291015625,0,-1.641319274902344,0.2831497192382812,0.3239517211914062,0,0.34783935546875,0,0.3589553833007812,0,0.3769989013671875,0.00151824951171875,0,0,-1.513961791992188,0,0.3208999633789062,0,0.3395233154296875,0,0.3541488647460938,0,0.3489303588867188,0.2006454467773438,0,0,-1.667068481445312,0,0.2529144287109375,0,0.2968521118164062,0,0.3339157104492188,0.3586883544921875,0,0.3733978271484375,0,0.100738525390625,0,0,-1.525421142578125,0.2828369140625,0,0.32672119140625,0,0.3553543090820312,0,0.3669204711914062,0,0.2421340942382812,0,0,-1.59814453125,0,0.2684555053710938,0,0.3049774169921875,0,0.3433761596679688,0.3620376586914062,0,0.3671112060546875,0,0,0,0,0,-1.393531799316406,0,0.2979812622070312,0,0.3401947021484375,0,0.3602676391601562,0,0.4210205078125,0.02105712890625,0,-1.394554138183594,0,0.29547119140625,0,0,0.3381729125976562,0,0.3598709106445312,0,0,0.3798980712890625,0,0.06743621826171875,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.593505859375,0,0.1343460083007812,0.2565460205078125,0.28240966796875,0.3185958862304688,0,0.3289108276367188,0.3329849243164062,0.3861160278320312,0.4107818603515625,0,0.4020004272460938,0,0.3438568115234375,0.3413467407226562,0,0.3413543701171875,0.3419876098632812,0,0.3382644653320312,0,0.2927169799804688,0,0,0,0,0,-4.342498779296875,0,0.3514404296875,0.3625335693359375,0.3448257446289062,0,0.3994064331054688,0,0,0.4229049682617188,0,0.395538330078125,0,0.409393310546875,0.4493408203125,0,0.4078598022460938,0.4068603515625,0,0.395172119140625,0,0.1298904418945312,0,0,-4.450706481933594,0.314208984375,0,0.3451995849609375,0,0,0.3386459350585938,0,0.350433349609375,0,0,0.4074783325195312,0,0.4202194213867188,0,0.4080047607421875,0,0.4072723388671875,0,0.40472412109375,0.4052581787109375,0,0.4067535400390625,0,0.3730850219726562,0,0,0,0,0,-4.266998291015625,0,0,0.3226242065429688,0.3365020751953125,0,0.3307342529296875,0,0.3800582885742188,0,0.4130859375,0,0.411651611328125,0,0.40521240234375,0,0.404083251953125,0,0.4043121337890625,0,0.4050521850585938,0,0.3988189697265625,0,0.1833419799804688,0,0,-4.357139587402344,0,0.29583740234375,0,0.3248672485351562,0.3174362182617188,0,0.3570404052734375,0,0.387298583984375,0,0.4512863159179688,0,0.4051742553710938,0,0.4033355712890625,0.40283203125,0,0.4041595458984375,0.4045333862304688,0.3296585083007812,0,0,0,-4.104774475097656,0,0.3125228881835938,0,0.3121566772460938,0,0.34417724609375,0,0.3754501342773438,0,0.4041213989257812,0.4078826904296875,0.4053497314453125,0.4058380126953125,0,0.4060134887695312,0,0.4069442749023438,0,0.3941192626953125,0,0.054595947265625,0,0,0,-4.134727478027344,0,0.2991256713867188,0,0.3083114624023438,0,0.3336105346679688,0,0.3665847778320312,0,0.3944473266601562,0,0.40936279296875,0,0.4037704467773438,0,0.4044876098632812,0,0.4043502807617188,0.4056472778320312,0,0.3985137939453125,0,0,0.1288299560546875,0,0,-4.121650695800781,0,0.2911300659179688,0,0.3009033203125,0,0.3639373779296875,0,0.3614959716796875,0,0.3886871337890625,0,0.4069061279296875,0,0.4013519287109375,0,0,0.4030303955078125,0,0.4034194946289062,0,0.4047088623046875,0,0.3973922729492188,0,0.1190414428710938,0,-4.050804138183594,0,0.285675048828125,0.2930450439453125,0,0.3338241577148438,0,0.3595046997070312,0,0,0.3808364868164062,0.4075546264648438,0,0.4011383056640625,0,0.4037933349609375,0,0,0.4030838012695312,0,0.405487060546875,0,0.3954010009765625,0,0.0998687744140625,0,-3.969963073730469,0,0.2788619995117188,0,0.28704833984375,0.3387374877929688,0,0.3573989868164062,0,0.3804092407226562,0.4053802490234375,0,0,0.40130615234375,0,0.40374755859375,0.403961181640625,0,0.404632568359375,0.3920822143554688,0,0.03293609619140625,0,0,-3.865280151367188,0,0.3068695068359375,0,0.30291748046875,0.3421249389648438,0,0.3613204956054688,0,0.3830642700195312,0,0.40496826171875,0,0.3990325927734375,0,0.4027175903320312,0,0.4023361206054688,0.4025726318359375,0,0.2719955444335938,0,0,0,0,0,-3.712699890136719,0,0.2773208618164062,0.3205642700195312,0,0.34747314453125,0.3637619018554688,0,0.3911361694335938,0.4058837890625,0.4005889892578125,0,0.4060134887695312,0,0.4041061401367188,0,0.3967514038085938,0,0.1118316650390625,0,0,-3.800796508789062,0,0.2687225341796875,0.2853317260742188,0.327362060546875,0,0.3507766723632812,0.369781494140625,0,0.3990020751953125,0,0.405364990234375,0,0.404815673828125,0,0,0.4047927856445312,0.4051895141601562,0,0.2906417846679688,0,0,0,-3.563232421875,0,0.28216552734375,0,0.3247604370117188,0,0,0.3460159301757812,0.3630828857421875,0,0.3907623291015625,0.4032669067382812,0,0.4025192260742188,0,0.4059524536132812,0.4019393920898438,0,0.3520050048828125,0,0,0,-3.581405639648438,0.2628021240234375,0,0.3088226318359375,0.3346481323242188,0,0.3539352416992188,0,0.378204345703125,0.4044265747070312,0,0.3990325927734375,0,0.4051513671875,0,0.4047164916992188,0.39447021484375,0.04257965087890625,0,0,-3.576934814453125,0,0.2600555419921875,0,0,0.301971435546875,0,0.3248138427734375,0,0.348358154296875,0,0.3709716796875,0,0.3998870849609375,0,0.4005661010742188,0,0.445709228515625,0.4046859741210938,0,0.3944320678710938,0,0.0311279296875,0,-3.511589050292969,0,0.2619705200195312,0.2985076904296875,0,0,0.3218002319335938,0,0.3474655151367188,0,0,0.3656692504882812,0,0.39910888671875,0.4009246826171875,0,0.4046096801757812,0.4058990478515625,0,0.3955154418945312,0,0.01419830322265625,0,0,-3.450088500976562,0,0,0.25970458984375,0,0,0.2942733764648438,0,0,0.317657470703125,0.344390869140625,0,0.364410400390625,0.3959503173828125,0,0.4018478393554688,0,0,0.404632568359375,0,0.4060516357421875,0,0.3634109497070312,0,0,0,0,0,-3.365592956542969,0,0.26580810546875,0,0.2967605590820312,0,0,0.3223190307617188,0.3525848388671875,0,0.3710784912109375,0,0.4004364013671875,0.4485855102539062,0.4081573486328125,0,0.4028854370117188,0,0.1976547241210938,0,-3.45440673828125,0,0,0.2498550415039062,0,0.2784805297851562,0,0.3021926879882812,0,0.3325042724609375,0,0.358673095703125,0.3743133544921875,0,0.3981475830078125,0,0.3921966552734375,0,0,0.4060287475585938,0,0.3959426879882812,0.06507110595703125,0,0,-3.314643859863281,0,0,0.2528839111328125,0,0.28143310546875,0,0.3064117431640625,0,0.3377838134765625,0,0.3598175048828125,0.3909759521484375,0.40386962890625,0.4028244018554688,0.4061203002929688,0.2700042724609375,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-3.353073120117188,0,0,0.0421295166015625,0,0,0.19720458984375,0,0.2267913818359375,0.2392730712890625,0,0.2670974731445312,0,0.3036270141601562,0.3231048583984375,0.3377151489257812,0,0.36688232421875,0,0.4005966186523438,0.4054107666015625,0,0.3388290405273438,0,0,0,0,0,-3.132820129394531,0,0,0.2634506225585938,0.2892684936523438,0,0.3167343139648438,0.3436050415039062,0,0,0.3546142578125,0,0.3808059692382812,0,0,0.3976211547851562,0,0.4396438598632812,0.406707763671875,0,0.0347137451171875,0,0,-3.142662048339844,0.2508621215820312,0.2758865356445312,0,0.3077621459960938,0,0.3392486572265625,0.350372314453125,0,0.3651962280273438,0,0.386077880859375,0.397552490234375,0,0.394500732421875,0,0.16796875,0,-3.173759460449219,0.242523193359375,0,0.265716552734375,0,0.2954635620117188,0,0,0.300872802734375,0.3324127197265625,0,0.3467254638671875,0.357269287109375,0.388153076171875,0,0.4022064208984375,0,0.3337554931640625,0,0,0,0,0,-2.983123779296875,0.2567138671875,0,0.2841033935546875,0.3493423461914062,0,0.34759521484375,0,0.3610076904296875,0.382843017578125,0,0.3977813720703125,0.4067535400390625,0,0.2867507934570312,0,0,0,0,0,-2.904319763183594,0,0.257293701171875,0,0.284942626953125,0,0.3205795288085938,0,0.3457260131835938,0,0.35870361328125,0.3784713745117188,0,0.3981399536132812,0,0,0.3999099731445312,0,0.248992919921875,0,0,0,0,0,-2.840141296386719,0.2569961547851562,0,0.2885360717773438,0.323211669921875,0,0.3473892211914062,0,0.357269287109375,0.377166748046875,0,0.3988571166992188,0.4000320434570312,0,0.177581787109375,0,0,-2.991607666015625,0,0,0.2333602905273438,0,0.2584762573242188,0,0.2911300659179688,0,0.3583297729492188,0,0,0.3495407104492188,0,0.3604812622070312,0.3824691772460938,0,0.4012069702148438,0.4010696411132812,0,0.04109954833984375,0,0,-2.857284545898438,0.24017333984375,0,0.27056884765625,0,0.30218505859375,0,0.3380203247070312,0.3508834838867188,0,0.3698043823242188,0.3887786865234375,0.4013137817382812,0,0.2797317504882812,0,0,0,0,0,0,0,-2.728515625,0,0.25201416015625,0.2750244140625,0.313995361328125,0,0.3415298461914062,0,0.3508834838867188,0,0.3732986450195312,0,0.3967437744140625,0,0.3996963500976562,0,0.1081161499023438,0,0,-2.808425903320312,0,0.2597427368164062,0.2669525146484375,0.2968368530273438,0,0.3350448608398438,0.334197998046875,0,0.3651657104492188,0,0.3855361938476562,0,0.4016799926757812,0,0.2447357177734375,0,0,0,0,0,-2.606765747070312,0,0.2546157836914062,0.2856979370117188,0,0.3211288452148438,0,0.3491668701171875,0,0.3618545532226562,0,0,0.3841171264648438,0,0.4024200439453125,0.3279037475585938,0,0,0,0,0,-2.616744995117188,0,0.2462310791015625,0,0.2779159545898438,0,0.31201171875,0,0.3432769775390625,0,0.3571014404296875,0.3763961791992188,0,0.3986282348632812,0,0.3839950561523438,0,0,0,-2.600288391113281,0.2761764526367188,0,0.2837600708007812,0,0.3228530883789062,0,0.3456802368164062,0,0,0.3602523803710938,0,0.3863906860351562,0,0,0.4015960693359375,0.3011932373046875,0,0,0,0,0,-2.511360168457031,0,0.249786376953125,0.2833328247070312,0,0.3216171264648438,0,0.35064697265625,0.3602447509765625,0,0.3847503662109375,0,0.3982315063476562,0.2391128540039062,0,0,0,0,0,-2.430892944335938,0,0.2533721923828125,0,0.2871551513671875,0.3219223022460938,0.3465652465820312,0.361480712890625,0,0.383087158203125,0,0,0.3986968994140625,0,0.1536865234375,0,0,-2.572830200195312,0,0.2569198608398438,0.2617416381835938,0.2979583740234375,0,0.3265838623046875,0,0.3467178344726562,0.3620986938476562,0.3850784301757812,0,0.39752197265625,0.01206207275390625,0,0,-2.460205078125,0,0.2351226806640625,0,0.2630538940429688,0,0.3014984130859375,0,0.335662841796875,0,0,0.3507843017578125,0,0.3646240234375,0,0.388336181640625,0,0.2938995361328125,0,0,0,0,0,-2.357978820800781,0.2481918334960938,0.283538818359375,0,0.320404052734375,0,0,0.3476104736328125,0,0.356964111328125,0,0.3787918090820312,0,0.4022064208984375,0,0.091766357421875,0,0,-2.425788879394531,0,0.2592086791992188,0.2677078247070312,0,0.3044509887695312,0,0.33831787109375,0,0.3542404174804688,0.3713531494140625,0,0.3931350708007812,0.2077178955078125,0,0,0,0,0,-2.221099853515625,0,0.2521133422851562,0.2861862182617188,0.3229446411132812,0,0,0.3493499755859375,0,0.3608169555664062,0,0.3873138427734375,0.331634521484375,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2.3450927734375,0,0.2081375122070312,0,0.2226791381835938,0,0.2430267333984375,0,0.2707672119140625,0,0.3082427978515625,0.3322982788085938,0.3479537963867188,0,0.36773681640625,0.1122589111328125,0,-2.338218688964844,0.198394775390625,0,0.2513275146484375,0,0.2886276245117188,0,0.321807861328125,0,0.34674072265625,0.3616790771484375,0,0,0.3823623657226562,0,0.254302978515625,0,0,0,0,0,-2.15374755859375,0,0.2456130981445312,0.2796173095703125,0,0,0.3207626342773438,0,0.3463668823242188,0,0.356658935546875,0.3831710815429688,0,0.28759765625,0,0,0,0,0,-2.097190856933594,0.2496566772460938,0.2850799560546875,0,0.3200836181640625,0.3466796875,0,0.3602752685546875,0,0,0.3873062133789062,0.2129745483398438,0,0,0,0,0,-2.043968200683594,0,0.2496871948242188,0,0.2867965698242188,0.3248062133789062,0.351776123046875,0,0.3610153198242188,0.3886260986328125,0,0,0.145111083984375,0,0,0,0,0,-1.975784301757812,0.253387451171875,0,0.292236328125,0,0.3281402587890625,0,0.3518524169921875,0.3540191650390625,0.377685546875,0,0.0812530517578125,0,-2.147796630859375,0.2653350830078125,0,0.2749557495117188,0.3136062622070312,0,0,0.3467483520507812,0,0.3633956909179688,0,0,0.3863754272460938,0,0.2592086791992188,0,0,0,0,0,0,0,-1.966690063476562,0.2473068237304688,0,0.28424072265625,0,0.3221893310546875,0,0.345672607421875,0.3592605590820312,0,0.384124755859375,0.0847015380859375,0,0,-2.067741394042969,0,0.2294158935546875,0.2585830688476562,0,0.2910079956054688,0.3260040283203125,0,0.3497085571289062,0,0,0.3616714477539062,0,0.311126708984375,0,0,0,0,0,-1.945907592773438,0.2379150390625,0,0.2740707397460938,0,0.3140945434570312,0,0,0.37994384765625,0,0.357391357421875,0,0.3848724365234375,0.056488037109375,0,0,-1.99041748046875,0.2305755615234375,0.2621536254882812,0,0.30426025390625,0,0.3389892578125,0,0.3542861938476562,0,0.3731002807617188,0,0.1849441528320312,0,0,0,0,0,-1.809257507324219,0,0.2463836669921875,0,0.2865829467773438,0,0.3241119384765625,0.3452911376953125,0,0,0.3590774536132812,0.3047714233398438,0,0,0,0,0,-1.860404968261719,0,0.2373123168945312,0,0.2740478515625,0,0,0.3160400390625,0,0.3448028564453125,0,0,0.3574371337890625,0,0.3868026733398438,0,0,0,-1.851272583007812,0,0.2335586547851562,0.2665481567382812,0.3077850341796875,0.3391952514648438,0.356781005859375,0,0,0.3708114624023438,0,0.03173065185546875,0,0,-1.85687255859375,0,0.2302169799804688,0,0.2606201171875,0.299285888671875,0.332000732421875,0,0.353607177734375,0,0.3673248291015625,0.06805419921875,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.867530822753906,0,0,0.09758758544921875,0.2431640625,0,0.24371337890625,0,0.2777252197265625,0.31329345703125,0,0.3360214233398438,0.3451614379882812,0,0.0642242431640625,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.837387084960938,0,0,0,0.130950927734375,0,0.2512359619140625,0,0.278656005859375,0,0.3121719360351562,0,0.3370895385742188,0,0.3286666870117188,0,0.3420181274414062,0,0.3893890380859375,0,0,0.4063949584960938,0,0.3943023681640625,0,0,0.3742828369140625,0,0.3374404907226562,0,0.3383026123046875,0,0.3383331298828125,0,0.3383636474609375,0,0.3379669189453125,0,0.3380966186523438,0,0.3380279541015625,0.3379058837890625,0,0.337493896484375,0.33807373046875,0,0.337860107421875,0,0.337371826171875,0,0.06566619873046875,0,0,0,0,0,-7.152618408203125,0,0.2798690795898438,0,0,0.3166961669921875,0,0.3418655395507812,0,0.329345703125,0,0.3420562744140625,0.3833465576171875,0,0.3993301391601562,0.40087890625,0,0,0.4069061279296875,0,0.4041213989257812,0,0.4051589965820312,0,0.403289794921875,0,0.4053192138671875,0,0.4064788818359375,0.4050827026367188,0.4058990478515625,0,0,0.4056777954101562,0.4006500244140625,0,0,0.38934326171875,0,0.1310806274414062,0,0,0,-7.072486877441406,0,0.2632293701171875,0,0.2995452880859375,0,0.3263778686523438,0,0.3176116943359375,0,0.3345108032226562,0,0.3563232421875,0.3567581176757812,0,0.3756942749023438,0,0.3885498046875,0,0.3972320556640625,0,0.4000930786132812,0,0,0.3952102661132812,0,0.390899658203125,0,0.394012451171875,0.3895187377929688,0,0,0.3731002807617188,0,0.3673934936523438,0,0.3881378173828125,0.3897323608398438,0,0.37481689453125,0,0,0,0,0,-6.919998168945312,0.2603683471679688,0,0,0.287750244140625,0,0.3104934692382812,0.3350830078125,0,0.3581466674804688,0,0.360626220703125,0,0.3621826171875,0,0.3793792724609375,0,0,0.3929061889648438,0,0,0.391326904296875,0,0.388641357421875,0,0.4003143310546875,0.3956298828125,0,0.3927841186523438,0.399139404296875,0.396942138671875,0,0.3915481567382812,0.3984527587890625,0,0.3907623291015625,0,0.1304473876953125,0,0,0,-6.914421081542969,0.2480010986328125,0,0.264739990234375,0,0.2888336181640625,0,0.2921829223632812,0,0.3308486938476562,0.3533172607421875,0,0.3530807495117188,0,0.357269287109375,0,0,0.3758697509765625,0,0.3870925903320312,0,0.4341506958007812,0,0,0.3955078125,0,0,0.3921661376953125,0,0.39068603515625,0.383941650390625,0.3928298950195312,0,0.3951797485351562,0,0,0.3900604248046875,0,0.3861923217773438,0.3022232055664062,0,0,0,0,0,0,0,0,-6.679550170898438,0,0,0.2394943237304688,0.2601165771484375,0,0.30316162109375,0,0.306732177734375,0.34063720703125,0,0.3549652099609375,0,0.3653945922851562,0.3727340698242188,0.3876113891601562,0.3945693969726562,0.3946685791015625,0,0.392547607421875,0,0,0.3965606689453125,0,0.3967361450195312,0.394134521484375,0,0.3936538696289062,0.3928146362304688,0,0.3964157104492188,0,0.3868789672851562,0.00618743896484375,0,0,0,0,0,-6.6209716796875,0,0.2497711181640625,0.2963104248046875,0,0.276275634765625,0.321746826171875,0,0.346282958984375,0.3575897216796875,0,0.3698806762695312,0,0.3776473999023438,0,0.3874893188476562,0.389678955078125,0,0,0.3867416381835938,0,0.37640380859375,0,0.3806533813476562,0,0.3980865478515625,0,0.3957138061523438,0,0.394775390625,0.3927993774414062,0,0.3902053833007812,0,0.3262176513671875,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-6.651313781738281,0,0,0,0,0,0.1020050048828125,0,0.2405776977539062,0,0.2457351684570312,0.2553634643554688,0,0.2960281372070312,0,0.3330535888671875,0.3302536010742188,0,0.3471603393554688,0.3814697265625,0,0.3958282470703125,0,0.396759033203125,0,0.43603515625,0,0.3967742919921875,0,0,0.3993759155273438,0,0.3997573852539062,0,0.4014739990234375,0,0.332550048828125,0,0.2459793090820312,0,0.358489990234375,0.405792236328125,0.1408538818359375,0,0,0,0,0,0,0,-6.517829895019531,0,0.22283935546875,0.2381210327148438,0,0.2432327270507812,0,0.2753677368164062,0,0.3118209838867188,0.3188095092773438,0,0,0.3551406860351562,0,0.322052001953125,0.304229736328125,0,0.250946044921875,0,0.275634765625,0,0.2592010498046875,0,0,0.2820205688476562,0,0.30511474609375,0,0.3238067626953125,0.336517333984375,0,0.3469467163085938,0,0.3631362915039062,0.3785629272460938,0,0.350128173828125,0,0.3663482666015625,0,0.274993896484375,0,0,0,0,0,0,0,0,-6.34466552734375,0,0,0.2303695678710938,0,0.2361831665039062,0.2447891235351562,0.2929306030273438,0,0.3079299926757812,0,0,0.325897216796875,0.334228515625,0,0.342010498046875,0,0.35345458984375,0,7.951934814453125,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7.62939453125,7.62939453125e-06,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,15.2587890625,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7.69256591796875,0,0,0,0,0,0,0,0,0,0,15.33204650878906,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"filename":["<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,null,null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,null,null,null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,null,"<expr>",null,null,null,null,null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,null,"<expr>",null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,null,null,null,"<expr>",null,"<expr>","<expr>",null,null,null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,null,null,null,"<expr>","<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,null,null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,null,"<expr>","<expr>",null,null,null,null,null,null,null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>","<expr>",null,null,null,null,null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,null,null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>","<expr>","<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,null,null,null,null,null,"<expr>","<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null]},"interval":10,"files":[{"filename":"<expr>","content":"## Generate Large Random Dataset\nn <- 2e6\nx <- runif(n)\ny <- runif(n)\nz <- runif(n)\nXYZ <- cbind(x,y,z)\n\n## Inspect 4 equivalent `row mean` calculations \nprofvis::profvis({\n    m <- rowSums(XYZ)/ncol(XYZ)\n    m <- rowMeans(XYZ)\n    m <- apply(XYZ, 1, mean)\n    m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }\n})\n## rowSums(), colSums(), rowMeans(), and colMeans() are vectorised and fast.\n## for loop is not the slowest, but the ugliest.","normpath":"<expr>"}],"prof_output":"/tmp/Rtmpwpgmai/file19dd412b64f3.prof","highlight":{"output":["^output\\$"],"gc":["^<GC>$"],"stacktrace":["^\\.\\.stacktraceo(n|ff)\\.\\.$"]},"split":"h"}},"evals":[],"jsHooks":[]}</script>
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
## 1 mean1(x, 0.5)     20ms   21.8ms      46.2    7.63MB     2.10
## 2 mean2(x, 0.5)   19.2ms   20.9ms      48.2    7.63MB     0   
## 3 mean3(x, 0.5)     20ms   21.8ms      46.4    7.63MB     2.11
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
##   0.109   0.000   0.033
```

```r
system.time({ lm(Y~X, data=DAT) })
```

```
##    user  system elapsed 
##   0.406   0.003   0.138
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
## # A tibble: 2 × 6
##   expression      min   median `itr/sec` mem_alloc `gc/sec`
##   <bch:expr> <bch:tm> <bch:tm>     <dbl> <bch:byt>    <dbl>
## 1 ma1(y)      165.3ms  165.9ms      6.01    15.3MB     2.00
## 2 ma2(y)       22.1ms   22.1ms     45.3     91.6MB   362.
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
##   0.027   0.002   0.029
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
##   0.796   0.195   0.564
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


## Advanced Programming 

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

Translations of common procedures is provided by https://stata2r.github.io/. See also the textbook "R for Stata Users" by Robert A. Muenchen and Joseph M. Hilbe.

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





