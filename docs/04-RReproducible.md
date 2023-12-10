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
<div class="plotly html-widget html-fill-item" id="htmlwidget-0dafc4b7f8d138810ada" style="width:672px;height:480px;"></div>
<script type="application/json" data-for="htmlwidget-0dafc4b7f8d138810ada">{"x":{"visdat":{"36555ddd60e1":["function () ","plotlyVisDat"]},"cur_data":"36555ddd60e1","attrs":{"36555ddd60e1":{"x":{},"y":{},"alpha_stroke":1,"sizes":[10,100],"spans":[1,20]}},"layout":{"margin":{"b":40,"l":60,"t":25,"r":10},"xaxis":{"domain":[0,1],"automargin":true,"title":"X"},"yaxis":{"domain":[0,1],"automargin":true,"title":"Y"},"hovermode":"closest","showlegend":false},"source":"A","config":{"modeBarButtonsToAdd":["hoverclosest","hovercompare"],"showSendToCloud":false},"data":[{"x":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100],"y":[4.2846566924517022,6.200122559171982,15.267108642157302,13.361204379236057,21.035272334658011,23.401065575815753,26.914957243289567,32.806660794678322,35.796656704448424,39.8437709493152,42.583107449685002,50.365769765351253,51.512889975160846,56.538823626940129,60.482028040713544,65.358038397899691,67.974364127203827,70.705630200857058,73.520428355250786,79.943338129464934,82.973494853879544,89.060405127346797,93.557096273336882,96.747017588494273,101.17062679122077,102.08570716445864,110.01547161203192,115.84600565564313,119.78004013542436,122.30816400010079,123.19039042089598,130.90119275557188,133.97855311148899,136.86690891710793,140.07880800140049,142.38420982155966,147.48505615412557,151.24323268650326,158.77095244366086,158.02019056913787,162.00793230867473,167.33783138043364,168.18317729777806,177.41830685961182,179.59488168326266,180.91014434657492,189.06418477216897,191.92557977035156,194.12042118933542,199.39844712324262,203.28897830747692,204.58850609771139,209.1874432984869,217.01894577979013,219.89118233667,223.50316089495496,230.66478762687822,231.50680672304088,236.24352671147668,239.87958600736354,244.00071887831362,249.74018503281187,249.3349801853247,257.59818825606925,258.72359775164711,264.90678457499024,273.67930710371502,271.64421830879121,275.48197531399177,281.16661768654308,282.12463406970915,286.755652560496,294.10669957853878,294.20479567978515,303.34789649217345,305.96005542677409,307.10816199723638,313.42264892846941,317.85009157709584,321.51740941712256,327.65190094765649,324.62084158809705,333.35254186852251,339.58339106389059,336.61385968751745,340.4910186656079,347.47447432806968,353.98061049851327,357.03312041933583,358.16453563423613,364.20696989912869,370.85686510426979,374.67492174466031,377.28726902677965,378.36632860636593,384.54885307816215,382.45300700687676,394.68200581725489,398.6758358195209,401.25318938282157],"type":"scatter","mode":"markers","marker":{"color":"rgba(31,119,180,1)","line":{"color":"rgba(31,119,180,1)"}},"error_y":{"color":"rgba(31,119,180,1)"},"error_x":{"color":"rgba(31,119,180,1)"},"line":{"color":"rgba(31,119,180,1)"},"xaxis":"x","yaxis":"y","frame":null}],"highlight":{"on":"plotly_click","persistent":false,"dynamic":false,"selectize":false,"opacityDim":0.20000000000000001,"selected":{"opacity":1},"debounce":0},"shinyEvents":["plotly_hover","plotly_click","plotly_selected","plotly_relayout","plotly_brushed","plotly_brushing","plotly_clickannotation","plotly_doubleclick","plotly_deselect","plotly_afterplot","plotly_sunburstclick"],"base_url":"https://plot.ly"},"evals":[],"jsHooks":[]}</script>
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

Notice there are a lot of documentation `### like this`, which is crucial for large projects. Also notice that anyone should be able to replicate the entire project by downloading a zip file and simply changing `home_dir`.


If some folders or files need to be created, you can do this within R

```r
# list the files and directories
list.files(recursive=TRUE, include.dirs=TRUE)
# create directory called 'Data'
dir.create('Data')
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
## Ncells 1212920 64.8    2365982 126.4  2365982 126.4
## Vcells 2298854 17.6    8388608  64.0  3571834  27.3
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
##   0.006   0.000   0.007
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
<div class="profvis html-widget html-fill-item" id="htmlwidget-b9840e84149666c19c7d" style="width:100%;height:600px;"></div>
<script type="application/json" data-for="htmlwidget-b9840e84149666c19c7d">{"x":{"message":{"prof":{"time":[1,2,3,4,5,6,7,7,8,9,10,11,12,13,14,15,15,16,16,17,17,18,18,19,19,20,20,21,21,22,22,23,23,24,24,25,25,26,26,27,27,28,28,29,29,30,30,31,31,32,32,33,33,34,34,34,35,35,36,37,37,37,38,38,38,39,40,40,41,41,42,42,43,44,45,45,46,46,47,47,48,48,49,49,50,50,51,51,52,52,52,53,53,53,54,54,55,55,56,57,57,58,59,59,60,60,61,62,63,64,65,65,65,66,66,67,67,68,69,70,70,70,71,71,71,72,72,73,73,74,74,75,76,77,77,78,79,80,80,81,81,82,82,83,84,84,85,85,85,86,86,87,88,88,89,89,90,91,91,91,92,93,93,94,94,94,95,95,96,96,97,97,98,98,98,99,99,99,100,101,102,102,102,103,104,105,105,105,106,106,107,107,107,108,109,109,110,111,111,112,112,113,114,114,115,115,116,117,118,118,119,119,120,120,121,121,122,123,123,124,124,125,126,126,126,127,127,128,128,129,130,131,131,132,132,133,134,134,135,136,136,137,137,138,139,140,140,141,141,142,142,143,143,143,144,144,145,146,147,147,147,148,149,149,150,151,151,152,152,153,154,154,155,155,156,157,157,158,158,159,159,160,160,161,161,162,162,162,163,164,165,166,166,167,167,168,168,169,169,170,170,171,171,172,172,173,173,174,174,175,175,175,176,176,176,177,177,177,178,178,179,179,179,180,181,182,182,183,183,184,184,185,185,185,186,187,187,188,189,189,190,190,191,191,191,192,192,192,193,193,194,194,195,195,196,197,197,198,198,199,199,200,200,201,202,202,203,204,204,204,205,206,206,207,207,208,208,209,209,209,210,210,210,211,212,212,213,214,214,215,215,216,216,216,217,218,218,218,219,219,219,220,220,221,221,222,223,223,224,224,225,226,226,226,226,227,227,227,227,228,228,229,229,230,230,231,231,232,232,233,233,234,234,235,236,237,238,239,239,240,240,241,241,242,242,242,243,243,243,244,244,245,245,246,247,247,248,248,248,249,250,250,251,251,252,252,253,253,254,254,255,255,256,257,257,258,258,258,259,259,259,260,261,261,262,263,263,264,265,266,267,267,268,268,269,269,270,271,271,272,272,273,273,274,274,274,275,275,276,276,277,278,279,279,280,280,281,281,282,283,284,284,285,286,287,287,288,289,289,289,290,290,290,291,292,292,292,293,293,294,295,295,296,296,297,297,298,298,299,299,300,300,301,301,302,303,303,304,304,305,305,306,306,306,307,307,307,308,308,309,309,309,310,310,311,311,312,312,313,313,313,314,314,315,315,316,316,317,317,318,319,320,320,321,322,322,322,323,323,323,324,325,326,326,327,328,328,329,329,330,330,330,331,331,332,332,333,333,334,334,335,335,336,337,337,338,338,339,339,339,339,340,340,341,342,342,343,343,344,345,346,346,347,347,348,348,349,349,350,350,351,351,352,353,353,353,354,354,354,355,355,356,356,357,358,358,359,359,360,360,360,361,362,362,362,363,364,364,365,365,365,366,366,367,367,368,369,369,370,370,371,371,372,372,372,373,373,374,374,375,376,376,377,377,378,378,379,380,380,380,381,381,381,382,382,382,383,383,383,384,384,384,385,385,385,386,386,386,387,387,387,388,388,388,389,389,389,390,390,390,391,391,391,392,392,393,393,394,394,395,395,395,396,396,397,398,398,399,400,400,401,401,401,402,403,403,404,405,405,406,406,407,407,408,409,410,411,412,412,413,413,414,415,415,415,416,416,417,417,417,418,418,418,419,419,420,420,421,422,422,422,423,423,424,424,425,425,426,427,427,428,428,429,429,430,430,430,431,431,431,432,433,433,434,435,435,436,437,437,438,438,439,439,440,441,442,443,443,444,444,444,445,446,446,447,447,448,449,450,451,451,452,452,453,453,454,455,456,456,457,457,457,458,458,458,459,459,459,460,460,461,461,462,462,463,464,465,466,466,467,468,469,469,470,470,471,472,472,473,473,474,475,475,475,476,477,477,478,479,480,480,480,481,482,482,482,483,483,483,484,485,486,487,487,487,488,488,489,490,490,491,491,492,493,493,494,494,494,495,495,495,496,496,497,497,498,498,499,500,501,501,502,502,503,504,505,505,506,506,506,507,507,508,508,509,509,510,510,511,511,512,512,513,513,513,514,515,515,515,516,516,517,518,518,518,519,519,520,520,521,521,522,522,523,523,524,525,526,527,527,528,529,530,530,530,531,531,531,532,533,534,535,535,536,536,537,537,538,538,539,540,540,541,541,541,542,542,542,543,543,544,544,545,545,546,547,547,548,549,549,549,550,551,551,552,552,552,553,553,553,554,555,555,556,557,557,558,559,559,560,560,561,562,562,563,563,564,564,565,565,566,567,567,568,568,569,569,570,570,571,571,572,572,573,574,574,574,575,575,575,576,576,577,578,578,579,579,580,581,581,582,583,583,584,585,585,586,587,587,588,588,588,589,589,589,590,590,591,591,592,593,593,594,594,595,596,596,597,598,599,599,599,600,600,600,601,601,602,602,603,603,603,604,605,605,606,606,607,607,607,608,609,610,610,611,612,612,613,613,614,614,615,616,616,617,618,619,619,620,621,622,622,623,623,624,624,624,625,625,625,626,627,627,628,628,629,630,630,631,631,632,633,634,635,635,635,636,636,636,637,637,638,638,639,640,640,641,641,642,642,643,644,644,645,646,646,646,647,647,647,648,648,648,649,649,649,650,650,650,651,651,651,652,652,652,653,653,653,654,654,654,655,655,655,656,656,656,657,657,657,658,658,658,659,659,659,660,660,660,661,661,661,662,662,662,663,663,663,664,664,664,665,665,665,666,666,666,667,667,667,668,668,668,669,669,669,670,670,670,671,671,671,672,672,672,673,673,673,674,674,674,675,675,675,676,676,676,677,677,677,678,678,679,679,679,680,680,681,682,683,683,684,684,685,685,686,687,687,688,688,689,690,691,692,692,693,693,694,695,696,696,697,698,698,699,700,700,701,701,702,702,702,703,703,703,704,704,705,705,706,707,708,708,709,709,709,710,711,711,712,712,713,713,714,714,715,716,716,716,717,717,718,719,720,720,721,721,722,723,723,724,725,725,726,726,726,726,727,727,727,727,728,728,729,729,730,731,731,732,733,733,734,735,735,736,736,737,737,737,738,738,739,740,740,741,741,741,742,742,743,743,744,744,745,746,746,747,748,749,749,750,750,751,752,752,753,754,754,755,756,756,757,758,758,759,759,760,760,761,761,762,763,763,764,764,765,765,766,766,767,768,768,769,769,770,771,772,772,772,773,773,773,774,775,775,776,776,777,777,778,778,779,780,781,781,782,783,784,784,785,786,786,787,787,788,788,789,790,791,791,792,793,794,795,795,796,796,797,798,798,799,800,800,801,801,802,802,803,803,804,805,805,806,806,807,808,808,809,809,810,810,811,811,812,812,813,814,815,815,816,817,817,818,818,818,819,819,819,820,820,820,821,821,822,822,823,823,824,825,825,826,827,827,827,828,828,829,830,830,831,831,832,832,832,833,834,834,835,836,836,837,837,838,838,839,840,840,840,840,841,841,841,841,842,842,842,842,843,843,844,844,845,846,846,847,847,848,848,849,850,850,851,851,851,852,852,853,853,854,854,855,855,856,856,857,858,858,859,860,860,860,861,861,862,862,863,863,863,863,864,864,864,864,865,865,866,866,867,867,868,868,869,870,871,871,872,872,873,873,874,874,875,875,876,876,877,877,878,878,879,880,881,881,881,882,882,883,883,884,885,885,886,886,886,887,887,887,888,888,889,889,890,890,891,891,891,892,892,893,893,894,894,895,896,896,897,897,898,898,899,899,900,901,901,902,902,903,904,904,905,905,906,907,907,908,908,909,909,910,911,911,912,913,913,914,914,915,916,916,917,918,918,919,919,920,920,921,922,923,923,924,925,925,926,926,927,927,928,928,928,929,929,929,930,930,931,931,932,933,934,935,935,936,937,937,938,939,939,940,940,940,941,941,941,942,943,943,944,944,945,946,946,947,947,948,948,948,949,949,949,950,950,950,951,951,952,952,953,954,955,955,956,956,957,958,958,959,959,960,960,961,962,963,963,964,964,965,966,966,967,967,967,968,968,968,969,969,969,970,971,971,972,972,973,973,974,974,975,976,976,977,977,978,978,979,980,981,981,982,983,983,984,984,985,985,986,986,987,987,987,988,988,988,989,989,990,990,991,991,992,992,993,993,994,995,995,995,996,997,998,998,999,1000,1000,1001,1002,1002,1003,1003,1004,1004,1005,1005,1005,1006,1006,1006,1007,1008,1008,1009,1010,1010,1011,1011,1012,1012,1013,1013,1014,1014,1015,1016,1016,1016,1017,1017,1018,1018,1019,1019,1020,1020,1021,1022,1022,1022,1023,1023,1024,1024,1025,1025,1026,1026,1027,1027,1028,1029,1029,1030,1030,1030,1031,1031,1032,1032,1033,1033,1034,1034,1035,1035,1036,1036,1037,1037,1038,1038,1039,1040,1040,1041,1042,1042,1043,1043,1044,1045,1045,1046,1047,1048,1048,1049,1049,1050,1050,1051,1051,1052,1052,1053,1053,1054,1054,1055,1056,1056,1057,1057,1058,1059,1059,1060,1060,1060,1061,1061,1061,1062,1062,1063,1063,1063,1064,1064,1065,1066,1066,1067,1067,1068,1069,1070,1070,1071,1072,1073,1074,1074,1075,1076,1077,1077,1078,1078,1078,1079,1079,1079,1080,1080,1081,1082,1082,1083,1083,1084,1084,1085,1086,1086,1087,1087,1087,1088,1089,1090,1091,1091,1092,1092,1092,1093,1093,1094,1094,1095,1095,1096,1096,1096,1097,1098,1098,1098,1099,1099,1099,1100,1100,1100,1101,1101,1102,1102,1103,1104,1105,1105,1106,1106,1107,1108,1108,1109,1109,1110,1110,1111,1111,1112,1112,1112,1113,1113,1114,1114,1114,1115,1115,1116,1116,1117,1117,1117,1118,1118,1119,1119,1119,1120,1120,1120,1121,1121,1121,1122,1122,1122,1123,1123,1123,1124,1124,1124,1125,1125,1125,1126,1126,1126,1127,1127,1127,1128,1128,1128,1129,1129,1129,1130,1130,1130,1131,1131,1131,1132,1132,1132,1133,1133,1133,1134,1134,1134,1135,1135,1135,1136,1136,1136,1137,1138,1139,1140,1140,1141,1141,1142,1142,1143,1143,1144,1144,1145,1145,1146,1146,1147,1147,1148,1148,1149,1150,1150,1151,1151,1152,1152,1153,1153,1153,1154,1154,1154,1155,1156,1156,1157,1157,1158,1158,1159,1159,1160,1160,1161,1161,1161,1162,1162,1163,1163,1164,1164,1165,1165,1166,1166,1167,1167,1168,1168,1169,1169,1170,1170,1171,1171,1171,1172,1172,1172,1173,1174,1174,1175,1175,1176,1177,1177,1178,1178,1179,1180,1180,1181,1181,1182,1182,1182,1183,1183,1184,1184,1185,1186,1186,1187,1187,1187,1188,1188,1188,1189,1189,1189,1190,1190,1191,1192,1192,1193,1193,1194,1195,1195,1196,1196,1197,1198,1199,1199,1200,1200,1201,1201,1202,1202,1203,1203,1203,1204,1204,1205,1205,1205,1206,1206,1206,1207,1207,1208,1208,1209,1209,1210,1210,1211,1211,1212,1212,1212,1213,1214,1215,1215,1216,1217,1217,1218,1219,1220,1221,1221,1221,1222,1222,1222,1223,1224,1224,1224,1225,1225,1226,1226,1227,1228,1228,1229,1230,1230,1231,1231,1232,1232,1233,1233,1234,1235,1235,1236,1237,1238,1238,1238,1239,1239,1239,1240,1241,1242,1242,1243,1243,1244,1244,1245,1246,1247,1247,1248,1248,1249,1249,1250,1250,1251,1252,1252,1253,1254,1255,1255,1256,1257,1257,1258,1258,1259,1259,1260,1260,1261,1261,1262,1263,1263,1264,1264,1265,1265,1265,1266,1266,1267,1267,1268,1268,1269,1269,1270,1270,1271,1272,1272,1273,1273,1274,1274,1275,1275,1276,1276,1276,1277,1277,1277,1278,1278,1278,1279,1279,1280,1280,1281,1281,1282,1283,1284,1284,1284,1285,1285,1285,1286,1286,1287,1287,1287,1288,1288,1289,1290,1290,1291,1291,1292,1293,1293,1294,1294,1294,1295,1295,1295,1296,1296,1297,1297,1298,1298,1299,1299,1300,1300,1301,1301,1302,1302,1303,1304,1304,1305,1306,1306,1307,1308,1309,1309,1310,1310,1310,1311,1311,1312,1313,1313,1313,1314,1314,1314,1315,1315,1316,1316,1317,1318,1318,1319,1319,1320,1321,1321,1321,1322,1322,1323,1324,1324,1325,1325,1326,1326,1327,1327,1328,1328,1329,1329,1330,1331,1331,1332,1332,1333,1334,1335,1335,1336,1337,1338,1338,1339,1340,1340,1340,1341,1342,1343,1343,1344,1345,1345,1346,1346,1347,1348,1348,1349,1349,1350,1350,1351,1351,1352,1352,1353,1353,1354,1354,1355,1355,1355,1356,1357,1357,1358,1358,1358,1359,1359,1360,1360,1361,1361,1362,1362,1363,1363,1364,1365,1365,1366,1366,1366,1367,1368,1368,1369,1370,1370,1370,1371,1371,1372,1372,1372,1373,1373,1373,1374,1374,1374,1375,1375,1375,1376,1376,1377,1377,1378,1378,1378,1379,1379,1380,1381,1382,1383,1383,1383,1384,1385,1386,1386,1387,1387,1388,1388,1388,1389,1390,1390,1390,1391,1391,1391,1392,1392,1392,1393,1393,1394,1394,1395,1396,1396,1397,1397,1398,1398,1399,1400,1400,1401,1402,1402,1403,1404,1405,1405,1406,1407,1408,1408,1409,1409,1409,1410,1410,1410,1411,1411,1411,1412,1412,1413,1414,1415,1415,1416,1416,1417,1417,1418,1419,1419,1419,1420,1421,1421,1422,1422,1423,1424,1424,1425,1425,1426,1426,1426,1427,1427,1427,1428,1428,1428,1429,1429,1429,1430,1431,1431,1432,1432,1433,1433,1434,1434,1435,1435,1436,1437,1437,1438,1439,1440,1441,1441,1442,1442,1443,1444,1444,1445,1445,1446,1446,1446,1447,1447,1447,1448,1449,1449,1450,1450,1451,1451,1452,1453,1453,1454,1454,1455,1455,1456,1457,1457,1458,1458,1459,1460,1460,1461,1462,1462,1462,1463,1463,1463,1464,1464,1464,1465,1465,1466,1466,1467,1467,1468,1469,1470,1470,1471,1472,1472,1473,1473,1474,1475,1475,1476,1477,1477,1478,1478,1479,1479,1479,1480,1480,1480,1481,1481,1482,1482,1483,1483,1484,1485,1486,1487,1487,1488,1488,1489,1490,1490,1490,1491,1491,1491,1492,1492,1493,1493,1494,1494,1495,1495,1495,1496,1496,1496,1497,1497,1497,1498,1499,1499,1500,1501,1501,1502,1503,1504,1505,1506,1506,1507,1507,1507,1508,1509,1509,1510,1510,1511,1511,1512,1512,1513,1513,1514,1514,1515,1515,1516,1516,1517,1517,1518,1518,1519,1519,1520,1520,1521,1521,1522,1522,1523,1523,1524,1524,1524,1525,1526,1526,1527,1527,1528,1529,1529,1530,1530,1531,1531,1532,1532,1533,1533,1534,1535,1535,1536,1536,1537,1537,1538,1538,1539,1539,1540,1541,1541,1542,1542,1543,1543,1544,1544,1544,1545,1545,1546,1546,1546,1547,1547,1548,1549,1550,1550,1551,1551,1552,1552,1552,1553,1553,1553,1554,1554,1555,1556,1556,1557,1558,1558,1559,1560,1561,1561,1562,1562,1563,1563,1563,1564,1565,1565,1566,1566,1566,1567,1567,1567,1568,1568,1568,1569,1570,1570,1571,1571,1572,1572,1573,1573,1574,1574,1575,1575,1576,1576,1577,1578,1578,1578,1579,1579,1580,1580,1581,1581,1582,1582,1582,1583,1583,1584,1584,1585,1585,1586,1586,1586,1587,1587,1588,1589,1590,1590,1591,1591,1592,1592,1593,1593,1593,1594,1594,1594,1595,1595,1595,1596,1596,1596,1597,1597,1597,1598,1598,1599,1599,1600,1600,1601,1601,1602,1602,1603,1603,1604,1604,1605,1605,1606,1606,1607,1607,1608,1608,1609,1609,1610,1610,1611,1612,1612,1613,1613,1614,1614,1615,1616,1616,1617,1617,1618,1618,1619,1619,1620,1620,1620,1621,1621,1621,1622,1622,1623,1623,1624,1624,1625,1625,1626,1626,1627,1627,1627,1628,1628,1629,1630,1630,1631,1631,1632,1633,1633,1634,1634,1635,1636,1636,1637,1638,1638,1639,1639,1640,1640,1641,1642,1643,1643,1644,1644,1645,1646,1646,1646,1647,1647,1647,1648,1648,1649,1649,1650,1651,1651,1652,1652,1653,1654,1654,1655,1655,1656,1657,1657,1658,1658,1659,1659,1660,1660,1661,1661,1662,1662,1663,1664,1664,1665,1665,1666,1666,1667,1667,1668,1668,1669,1670,1670,1671,1671,1672,1672,1673,1673,1674,1674,1675,1675,1676,1676,1677,1678,1678,1679,1679,1680,1681,1682,1682,1683,1683,1684,1684,1685,1686,1686,1686,1687,1687,1688,1688,1689,1689,1689,1690,1690,1691,1691,1692,1693,1693,1693,1694,1695,1695,1695,1696,1696,1696,1697,1698,1699,1699,1700,1700,1701,1701,1702,1702,1703,1703,1704,1704,1705,1705,1706,1707,1707,1707,1708,1708,1708,1709,1709,1710,1710,1711,1711,1712,1712,1713,1713,1714,1714,1715,1715,1716,1716,1716,1717,1717,1718,1718,1719,1719,1720,1720,1721,1721,1722,1722,1723,1723,1724,1724,1725,1725,1726,1726,1727,1727,1728,1728,1729,1730,1730,1731,1732,1732,1733,1733,1734,1735,1735,1736,1736,1737,1737,1738,1738,1739,1739,1740,1740,1741,1741,1742,1742,1743,1743,1744,1744,1745,1745,1746,1746,1747,1747,1748,1748,1749,1749,1750,1750,1751,1751,1752,1752,1753,1753,1754,1754,1755,1755,1756,1756,1757,1757,1758,1758,1759,1759,1760,1760,1761,1761,1762,1762,1763,1763,1764,1764,1765,1765,1766,1766,1767,1767,1768,1768,1769,1769,1770,1770,1771,1771,1772,1772,1773,1773,1774,1774,1775,1775,1776,1776,1777,1777,1778,1778,1779,1779,1780,1780,1781,1781,1782,1782,1783,1783,1784,1784,1785,1785,1786,1786,1787,1787,1788,1788,1789,1789,1790,1790,1791,1791,1792,1792,1793,1793,1794,1794,1795,1795,1796,1796,1797,1797,1798,1798,1799,1799,1800,1800,1801,1801,1802,1802,1803,1803,1804,1804,1805,1805,1806,1806,1807,1807,1808,1809,1809,1810,1811,1812,1812,1813,1813,1814,1815,1816,1817,1817,1818,1818,1819,1820,1820,1821,1821,1822,1823,1823,1824,1824,1825,1826,1826,1827,1827,1828,1828,1829,1829,1830,1830,1831,1831,1832,1832,1833,1834,1834,1835,1836,1837,1837,1838,1839,1839,1840,1840,1840,1841,1842,1843,1843,1844,1844,1845,1845,1846,1846,1847,1847,1848,1848,1849,1849,1850,1850,1850,1851,1851,1852,1852,1853,1853,1854,1855,1856,1857,1857,1858,1859,1859,1860,1860,1861,1862,1862,1863,1863,1864,1865,1866,1867,1868,1869,1869,1870,1871,1871,1872,1873,1874,1874,1875,1876,1876,1877,1877,1878,1878,1879,1879,1880,1880,1880,1881,1881,1881,1882,1882,1882,1883,1883,1884,1884,1885,1885,1886,1887,1887,1888,1889,1890,1890,1891,1891,1892,1892,1893,1893,1894,1894,1894,1895,1895,1896,1896,1897,1897,1898,1898,1899,1900,1900,1901,1901,1902,1902,1902,1903,1903,1904,1904,1905,1905,1906,1906,1907,1908,1909,1910,1910,1911,1911,1912,1913,1913,1914,1914,1914,1915,1916,1916,1916,1916,1917,1917,1917,1917,1918,1918,1918,1918,1919,1919,1920,1921,1922,1923,1923,1924,1925,1926,1926,1927,1928,1928,1929,1930,1930,1931,1931,1932,1932,1933,1933,1934,1935,1935,1936,1936,1937,1937,1938,1939,1939,1940,1940,1941,1941,1942,1942,1943,1943,1944,1944,1945,1945,1946,1947,1947,1948,1948,1949,1949,1950,1950,1951,1951,1952,1952,1953,1953,1953,1954,1954,1954,1955,1955,1955,1956,1956,1957,1957,1958,1958,1958,1959,1960,1960,1960,1961,1961,1961,1962,1962,1962,1963,1964,1964,1965,1966,1966,1967,1967,1967,1968,1969,1969,1970,1970,1971,1972,1973,1974,1974,1975,1975,1976,1977,1977,1978,1978,1979,1980,1980,1981,1981,1982,1983,1983,1984,1984,1985,1985,1986,1986,1987,1987,1988,1988,1989,1989,1990,1990,1991,1991,1992,1992,1993,1993,1994,1995,1996,1997,1998,1998,1999,2000,2000,2001,2001,2002,2003,2003,2004,2004,2004,2005,2005,2006,2006,2007,2008,2008,2009,2009,2010,2011,2011,2012,2013,2013,2014,2014,2015,2015,2016,2017,2017,2018,2019,2020,2020,2021,2021,2022,2022,2023,2024,2024,2024,2025,2025,2025,2026,2026,2026,2027,2028,2028,2029,2029,2030,2030,2030,2031,2032,2033,2034,2034,2034,2035,2035,2036,2037,2037,2038,2039,2039,2040,2041,2041,2042,2043,2043,2044,2044,2045,2045,2046,2046,2047,2047,2048,2048,2049,2049,2050,2050,2051,2051,2051,2052,2052,2053,2053,2054,2054,2055,2056,2057,2058,2058,2058,2059,2059,2059,2060,2060,2060,2061,2061,2061,2062,2062,2062,2063,2063,2063,2064,2064,2064,2065,2065,2065,2066,2066,2066,2067,2067,2067,2068,2068,2068,2069,2069,2069,2070,2070,2070,2071,2071,2072,2072,2073,2073,2074,2075,2075,2076,2076,2077,2077,2077,2078,2078,2079,2079,2079,2080,2081,2081,2082,2083,2083,2084,2084,2084,2085,2086,2087,2087,2087,2088,2088,2089,2089,2090,2090,2091,2091,2092,2092,2093,2093,2094,2094,2095,2095,2096,2096,2097,2097,2098,2098,2099,2099,2100,2100,2101,2101,2101,2102,2102,2102,2103,2103,2103,2104,2104,2105,2105,2106,2107,2108,2109,2109,2110,2110,2110,2111,2112,2113,2114,2115,2115,2116,2117,2118,2119,2119,2120,2120,2121,2121,2122,2122,2122,2123,2124,2124,2125,2126,2126,2127,2127,2128,2128,2128,2129,2130,2130,2130,2131,2131,2132,2133,2133,2133,2134,2134,2134,2135,2135,2135,2136,2136,2136,2137,2137,2138,2138,2139,2139,2140,2140,2140,2141,2141,2141,2142,2143,2143,2144,2144,2145,2145,2146,2146,2146,2147,2147,2148,2148,2148,2149,2149,2150,2151,2151,2151,2152,2153,2153,2154,2154,2155,2155,2156,2156,2157,2157,2158,2158,2159,2159,2160,2160,2161,2161,2162,2162,2163,2163,2164,2164,2165,2165,2166,2167,2167,2168,2168,2169,2169,2170,2170,2171,2171,2172,2172,2173,2173,2174,2174,2175,2175,2176,2176,2177,2177,2178,2178,2179,2179,2180,2180,2181,2181,2182,2182,2183,2183,2184,2184,2185,2185,2186,2186,2187,2187,2188,2188,2189,2189,2190,2190,2191,2191,2191,2191,2191,2191,2191,2191,2192,2192,2192,2192,2192,2193,2193,2193,2193,2193,2193,2193,2193,2194,2194,2194,2194,2194,2194,2194,2194,2195,2195,2195,2195,2195,2195,2195,2195,2196,2196,2196,2196,2196,2196,2196,2196,2197,2197,2197,2197,2197,2197,2197,2197,2198,2198,2198,2198,2198,2198,2198,2198,2199,2199,2199,2199,2199,2199,2199,2199,2200,2200,2200,2200,2200,2200,2200,2200,2201,2201,2201,2201,2201,2201,2201,2201,2202,2202,2202,2202,2202,2202,2202,2202,2203,2203,2203,2203,2203,2203,2203,2203,2204,2204,2204,2204,2204,2204,2204,2204,2205,2205,2205,2205,2205,2205,2205,2205,2206,2206,2206,2206,2206,2206,2206,2206,2207,2207,2207,2207,2207,2207,2207,2207,2208,2208,2208,2208,2208,2208,2208,2208,2209,2209,2209,2209,2209,2209,2209,2209,2210,2210,2210,2210,2210,2210,2210,2210,2211,2211,2211,2211,2211,2211,2211,2211,2212,2212,2212,2212,2212,2212,2212,2212,2213,2213,2213,2213,2213,2213,2213,2213,2214,2214,2214,2214,2214,2214,2214,2214,2215,2215,2215,2215,2215,2215,2215,2215,2216,2216,2216,2216,2216,2216,2216,2216,2217,2217,2217,2217,2217,2217,2217,2217,2218,2218,2218,2218,2218,2218,2218,2218,2219,2219,2219,2219,2219,2219,2219,2219,2220,2220,2220,2220,2220,2220,2220,2220,2221,2221,2221,2221,2221,2221,2221,2221],"depth":[1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,3,2,1,3,2,1,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,1,2,1,2,1,1,1,1,1,3,2,1,2,1,2,1,1,1,3,2,1,3,2,1,2,1,2,1,2,1,1,1,2,1,1,1,2,1,2,1,2,1,1,2,1,3,2,1,2,1,1,2,1,2,1,1,3,2,1,1,2,1,3,2,1,2,1,2,1,2,1,3,2,1,3,2,1,1,1,3,2,1,1,1,3,2,1,2,1,3,2,1,1,2,1,1,2,1,2,1,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,3,2,1,2,1,2,1,1,1,2,1,2,1,1,2,1,1,2,1,2,1,1,1,2,1,2,1,2,1,3,2,1,2,1,1,1,3,2,1,1,2,1,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,3,2,1,1,1,2,1,2,1,2,1,3,2,1,1,2,1,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,1,3,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,1,2,1,1,2,1,2,1,3,2,1,1,3,2,1,3,2,1,2,1,2,1,1,2,1,2,1,1,4,3,2,1,4,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,1,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,3,2,1,1,2,1,1,2,1,1,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,1,2,1,2,1,2,1,1,1,2,1,1,1,2,1,1,3,2,1,3,2,1,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,3,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,1,2,1,1,3,2,1,3,2,1,1,1,2,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,4,3,2,1,2,1,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,2,1,2,1,1,2,1,2,1,3,2,1,1,3,2,1,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,1,2,1,3,2,1,1,2,1,1,2,1,2,1,2,1,1,1,1,1,2,1,2,1,1,3,2,1,2,1,3,2,1,3,2,1,2,1,2,1,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,1,2,1,1,2,1,1,2,1,2,1,2,1,1,1,1,2,1,3,2,1,1,2,1,2,1,1,1,1,2,1,2,1,2,1,1,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,1,1,2,1,1,1,2,1,2,1,1,2,1,2,1,1,3,2,1,1,2,1,1,1,3,2,1,1,3,2,1,3,2,1,1,1,1,3,2,1,2,1,1,2,1,2,1,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,1,2,1,2,1,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,3,2,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,1,1,2,1,1,1,3,2,1,3,2,1,1,1,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,1,3,2,1,1,2,1,3,2,1,3,2,1,1,2,1,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,2,1,1,2,1,2,1,1,2,1,1,2,1,1,2,1,1,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,2,1,1,2,1,1,1,3,2,1,3,2,1,2,1,2,1,3,2,1,1,2,1,2,1,3,2,1,1,1,2,1,1,2,1,2,1,2,1,1,2,1,1,1,2,1,1,1,2,1,2,1,3,2,1,3,2,1,1,2,1,2,1,1,2,1,2,1,1,1,1,3,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,3,2,1,2,1,1,1,2,1,2,1,2,1,1,2,1,2,1,1,1,1,2,1,2,1,1,1,2,1,1,2,1,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,1,1,2,1,3,2,1,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,1,1,2,1,2,1,1,2,1,1,2,1,4,3,2,1,4,3,2,1,2,1,2,1,1,2,1,1,2,1,1,2,1,2,1,3,2,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,1,1,2,1,2,1,1,2,1,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,1,1,2,1,1,1,2,1,1,2,1,2,1,2,1,1,1,2,1,1,1,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,1,3,2,1,2,1,1,2,1,2,1,3,2,1,1,2,1,1,2,1,2,1,2,1,1,4,3,2,1,4,3,2,1,4,3,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,3,2,1,2,1,2,1,4,3,2,1,4,3,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,3,2,1,2,1,2,1,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,1,1,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,1,1,1,2,1,1,2,1,1,2,1,3,2,1,3,2,1,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,1,1,2,1,2,1,1,2,1,2,1,2,1,1,1,2,1,2,1,1,2,1,3,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,1,1,2,1,1,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,3,2,1,3,2,1,2,1,3,2,1,2,1,1,2,1,2,1,1,1,2,1,1,1,1,2,1,1,1,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,2,1,1,2,1,3,2,1,1,1,1,2,1,3,2,1,2,1,2,1,2,1,3,2,1,1,3,2,1,3,2,1,3,2,1,2,1,2,1,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,2,1,3,2,1,2,1,2,1,3,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,3,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,3,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,1,2,1,1,2,1,1,1,1,3,2,1,3,2,1,1,3,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,1,1,3,2,1,3,2,1,1,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,1,2,1,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,1,3,2,1,3,2,1,2,1,3,2,1,2,1,1,2,1,2,1,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,1,1,2,1,3,2,1,2,1,1,3,2,1,3,2,1,2,1,2,1,1,2,1,2,1,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,1,2,1,1,1,2,1,1,3,2,1,1,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,1,2,1,1,3,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,3,2,1,2,1,1,1,1,3,2,1,1,1,2,1,2,1,3,2,1,1,3,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,1,2,1,1,1,2,1,1,1,2,1,3,2,1,3,2,1,3,2,1,2,1,1,1,2,1,2,1,2,1,1,3,2,1,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,1,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,1,2,1,1,2,1,2,1,1,2,1,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,1,1,2,1,2,1,1,3,2,1,3,2,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,1,2,1,1,2,1,1,1,1,1,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,2,1,3,2,1,2,1,1,1,2,1,2,1,3,2,1,3,2,1,2,1,1,2,1,1,2,1,1,1,2,1,2,1,3,2,1,1,2,1,3,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,3,2,1,2,1,1,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,1,1,2,1,2,1,1,3,2,1,3,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,3,2,1,2,1,2,1,1,3,2,1,1,3,2,1,3,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,1,2,1,2,1,1,1,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,1,2,1,1,2,1,3,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,1,1,2,1,1,2,1,2,1,1,2,1,2,1,1,1,1,1,1,2,1,1,2,1,1,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,1,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,1,1,2,1,2,1,1,2,1,3,2,1,1,4,3,2,1,4,3,2,1,4,3,2,1,2,1,1,1,1,2,1,1,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,3,2,1,1,3,2,1,3,2,1,3,2,1,1,2,1,1,2,1,3,2,1,1,2,1,2,1,1,1,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,1,1,2,1,1,2,1,2,1,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,1,2,1,1,1,2,1,2,1,2,1,1,3,2,1,3,2,1,3,2,1,1,2,1,2,1,3,2,1,1,1,1,3,2,1,2,1,1,2,1,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,1,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,3,2,1,1,2,1,1,2,1,3,2,1,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,1,1,1,2,1,3,2,1,1,1,1,1,2,1,1,1,1,2,1,2,1,2,1,3,2,1,1,2,1,1,2,1,2,1,3,2,1,1,3,2,1,2,1,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,3,2,1,2,1,3,2,1,2,1,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,8,7,6,5,4,3,2,1,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1],"label":["rowSums","rowSums","rowSums","rowSums","rowSums","rowSums","/","local","rowMeans","rowMeans","rowMeans","rowMeans","rowMeans","rowMeans","rowMeans","aperm.default","apply","aperm.default","apply","aperm.default","apply","aperm.default","apply","aperm.default","apply","aperm.default","apply","aperm.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","isTRUE","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","is.numeric","local","mean.default","apply","FUN","apply","apply","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","length","local","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","apply","is.na","local","mean.default","apply","apply","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","apply","apply","FUN","apply","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","is.na","local","mean.default","apply","apply","<GC>","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","apply","isTRUE","mean.default","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","<GC>","apply","apply","mean.default","apply","length","local","apply","FUN","apply","mean.default","apply","apply","apply","is.numeric","local","FUN","apply","mean.default","apply","FUN","apply","apply","FUN","apply","mean.default","apply","apply","<GC>","FUN","apply","length","local","mean.default","apply","apply","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","mean.default","apply","apply","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","is.numeric","local","FUN","apply","apply","is.numeric","local","<GC>","apply","<GC>","apply","is.na","local","FUN","apply","isTRUE","mean.default","apply","apply","apply","apply","is.numeric","local","FUN","apply","FUN","apply","length","local","length","local","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","FUN","apply","is.na","local","isTRUE","mean.default","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","FUN","apply","length","local","mean.default","apply","apply","mean.default","apply","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","FUN","apply","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","apply","apply","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","length","local","apply","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","is.na","local","FUN","apply","is.na","local","mean.default","apply","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","mean.default","apply","apply","FUN","apply","apply","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","FUN","apply","length","local","mean.default","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","apply","FUN","apply","apply","apply","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","apply","mean.default","apply","FUN","apply","<GC>","isTRUE","mean.default","apply","FUN","apply","apply","mean.default","apply","FUN","apply","apply","apply","FUN","apply","mean.default","apply","is.na","local","FUN","apply","is.numeric","local","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","apply","length","local","FUN","apply","isTRUE","mean.default","apply","apply","isTRUE","mean.default","apply","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","apply","<GC>","apply","apply","FUN","apply","length","local","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","mean.default","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","is.na","local","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","mean.default","apply","apply","mean.default","apply","isTRUE","mean.default","apply","apply","mean.default","apply","apply","<GC>","apply","is.na","local","FUN","apply","apply","apply","apply","apply","mean.default","apply","mean.default","apply","apply","isTRUE","mean.default","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","is.numeric","local","mean.default","apply","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","FUN","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","mean.default","apply","apply","FUN","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","apply","apply","FUN","apply","<GC>","length","local","apply","FUN","apply","is.numeric","local","apply","apply","apply","FUN","apply","mean.default","apply","FUN","apply","apply","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","isTRUE","mean.default","apply","is.numeric","local","FUN","apply","FUN","apply","apply","apply","apply","FUN","apply","apply","apply","FUN","apply","<GC>","apply","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","length","local","apply","apply","isTRUE","mean.default","apply","apply","<GC>","length","local","<GC>","length","local","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","apply","mean.default","apply","FUN","apply","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","FUN","apply","apply","apply","mean.default","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","length","local","isTRUE","mean.default","apply","apply","isTRUE","mean.default","apply","is.na","local","apply","<GC>","length","local","FUN","apply","is.numeric","local","mean.default","apply","length","local","FUN","apply","apply","apply","apply","mean.default","apply","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","apply","apply","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","FUN","apply","apply","is.numeric","local","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","<GC>","apply","length","local","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","apply","is.na","local","mean.default","apply","apply","is.na","local","apply","FUN","apply","apply","mean.default","apply","apply","mean.default","apply","<GC>","length","local","<GC>","length","local","mean.default","apply","mean.default","apply","apply","FUN","apply","length","local","apply","FUN","apply","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","apply","apply","mean.default","apply","apply","FUN","apply","<GC>","apply","<GC>","apply","apply","FUN","apply","apply","apply","mean.default","apply","apply","apply","mean.default","apply","FUN","apply","<GC>","is.numeric","local","<GC>","is.numeric","local","apply","is.numeric","local","is.na","local","apply","length","local","FUN","apply","apply","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","mean.default","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","apply","apply","FUN","apply","mean.default","apply","is.na","local","apply","FUN","apply","is.numeric","local","apply","apply","apply","FUN","apply","mean.default","apply","apply","apply","FUN","apply","apply","FUN","apply","apply","FUN","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","length","local","FUN","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","apply","length","local","mean.default","apply","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","length","local","apply","apply","FUN","apply","mean.default","apply","apply","FUN","apply","apply","is.numeric","local","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","FUN","apply","FUN","apply","apply","is.na","local","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","apply","is.na","local","isTRUE","mean.default","apply","length","local","FUN","apply","FUN","apply","apply","FUN","apply","apply","apply","<GC>","apply","<GC>","apply","apply","length","local","apply","length","local","apply","length","local","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","mean.default","apply","FUN","apply","is.na","local","FUN","apply","apply","mean.default","apply","FUN","apply","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","mean.default","apply","is.numeric","local","FUN","apply","apply","apply","is.na","local","apply","apply","FUN","apply","apply","mean.default","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","apply","apply","apply","<GC>","apply","<GC>","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","mean.default","apply","FUN","apply","is.na","local","FUN","apply","apply","apply","mean.default","apply","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","is.numeric","local","FUN","apply","FUN","apply","apply","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","apply","length","local","isTRUE","mean.default","apply","FUN","apply","FUN","apply","is.numeric","local","FUN","apply","mean.default","apply","apply","mean.default","apply","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","is.na","local","apply","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","length","local","is.numeric","local","FUN","apply","apply","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","apply","length","local","<GC>","length","local","<GC>","length","local","FUN","apply","is.na","local","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","is.numeric","local","mean.default","apply","mean.default","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","apply","is.na","local","FUN","apply","apply","FUN","apply","<GC>","apply","<GC>","apply","apply","FUN","apply","apply","mean.default","apply","FUN","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","mean.default","apply","apply","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","length","local","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","apply","apply","apply","FUN","apply","apply","FUN","apply","apply","mean.default","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","mean.default","apply","FUN","apply","apply","FUN","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","is.numeric","local","apply","apply","FUN","apply","FUN","apply","apply","is.na","local","mean.default","apply","mean.default","apply","apply","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","is.numeric","local","is.na","local","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","is.na","local","FUN","apply","is.na","local","FUN","apply","mean.default","apply","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","apply","mean.default","apply","apply","FUN","apply","FUN","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","isTRUE","mean.default","apply","length","local","length","local","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","mean.default","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","is.na","local","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","apply","mean.default","apply","apply","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","is.numeric","local","FUN","apply","FUN","apply","apply","mean.default","apply","FUN","apply","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","length","local","isTRUE","mean.default","apply","mean.default","apply","apply","FUN","apply","length","local","apply","apply","FUN","apply","apply","apply","apply","mean.default","apply","apply","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","apply","mean.default","apply","isTRUE","mean.default","apply","apply","apply","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","apply","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","FUN","apply","FUN","apply","is.numeric","local","isTRUE","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","apply","apply","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","length","local","FUN","apply","FUN","apply","is.na","local","mean.default","apply","apply","FUN","apply","FUN","apply","is.na","local","<GC>","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","length","local","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","is.numeric","local","<GC>","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","length","local","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","apply","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","<GC>","is.numeric","local","<GC>","is.numeric","local","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","apply","mean.default","apply","apply","apply","apply","<GC>","is.numeric","local","<GC>","is.numeric","local","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","apply","FUN","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","apply","mean.default","apply","FUN","apply","FUN","apply","apply","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","mean.default","apply","apply","apply","FUN","apply","apply","mean.default","apply","<GC>","apply","<GC>","apply","mean.default","apply","FUN","apply","apply","length","local","length","local","isTRUE","mean.default","apply","is.na","local","FUN","apply","FUN","apply","is.na","local","length","local","apply","FUN","apply","is.na","local","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","length","local","FUN","apply","is.numeric","local","apply","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","is.na","local","isTRUE","mean.default","apply","mean.default","apply","apply","mean.default","apply","is.numeric","local","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","is.na","local","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","apply","FUN","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","<GC>","apply","<GC>","apply","apply","apply","FUN","apply","apply","apply","is.na","local","apply","isTRUE","mean.default","apply","apply","apply","mean.default","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","mean.default","apply","FUN","apply","<GC>","apply","<GC>","apply","is.numeric","local","mean.default","apply","isTRUE","mean.default","apply","apply","is.numeric","local","isTRUE","mean.default","apply","length","local","is.na","local","FUN","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","isTRUE","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","apply","isTRUE","mean.default","apply","apply","apply","mean.default","apply","length","local","isTRUE","mean.default","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","FUN","apply","apply","FUN","apply","apply","FUN","apply","apply","apply","FUN","apply","apply","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","apply","FUN","apply","length","local","FUN","apply","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","is.numeric","local","mean.default","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","apply","apply","apply","FUN","apply","mean.default","apply","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","mean.default","apply","is.numeric","local","mean.default","apply","apply","is.numeric","local","FUN","apply","apply","FUN","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","apply","apply","is.na","local","apply","FUN","apply","FUN","apply","apply","mean.default","apply","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","is.numeric","local","apply","apply","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","apply","mean.default","apply","apply","FUN","apply","apply","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","apply","FUN","apply","is.na","local","<GC>","apply","<GC>","apply","<GC>","apply","apply","mean.default","apply","FUN","apply","length","local","isTRUE","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","length","local","FUN","apply","<GC>","is.na","local","<GC>","is.na","local","mean.default","apply","apply","FUN","apply","apply","mean.default","apply","apply","apply","length","local","length","local","isTRUE","mean.default","apply","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","FUN","apply","FUN","apply","mean.default","apply","is.na","local","mean.default","apply","is.na","local","FUN","apply","apply","isTRUE","mean.default","apply","length","local","<GC>","apply","<GC>","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","apply","<GC>","apply","length","local","FUN","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","apply","length","local","FUN","apply","apply","<GC>","apply","<GC>","apply","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","FUN","apply","apply","apply","mean.default","apply","mean.default","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","is.na","local","FUN","apply","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","FUN","apply","apply","mean.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","length","local","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","apply","mean.default","apply","FUN","apply","apply","apply","length","local","<GC>","apply","<GC>","apply","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","mean.default","apply","apply","FUN","apply","apply","FUN","apply","mean.default","apply","apply","FUN","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","apply","apply","mean.default","apply","mean.default","apply","apply","apply","apply","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","is.numeric","local","apply","mean.default","apply","apply","apply","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","is.numeric","local","mean.default","apply","apply","apply","apply","FUN","apply","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","apply","apply","apply","apply","apply","mean.default","apply","apply","mean.default","apply","apply","apply","mean.default","apply","apply","FUN","apply","is.numeric","local","mean.default","apply","is.numeric","local","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","mean.default","apply","apply","apply","length","local","FUN","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","is.numeric","local","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","is.na","local","mean.default","apply","mean.default","apply","apply","apply","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","isTRUE","mean.default","apply","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","mean.default","apply","apply","apply","apply","FUN","apply","apply","apply","FUN","apply","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","apply","length","local","FUN","apply","mean.default","apply","apply","is.na","local","FUN","apply","length","local","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","apply","is.numeric","local","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","is.numeric","local","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","length","local","length","local","isTRUE","mean.default","apply","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","apply","apply","apply","is.numeric","local","mean.default","apply","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","FUN","apply","apply","mean.default","apply","is.na","local","FUN","apply","length","local","is.numeric","local","FUN","apply","mean.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","apply","apply","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","apply","length","local","mean.default","apply","apply","mean.default","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","is.numeric","local","apply","apply","length","local","mean.default","apply","mean.default","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","apply","isTRUE","mean.default","apply","mean.default","apply","apply","mean.default","apply","apply","mean.default","apply","apply","mean.default","apply","apply","is.numeric","local","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","is.na","local","isTRUE","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","isTRUE","mean.default","apply","length","local","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","length","local","FUN","apply","FUN","apply","length","local","FUN","apply","FUN","apply","FUN","apply","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","FUN","apply","FUN","apply","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","apply","apply","FUN","apply","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","mean.default","apply","apply","FUN","apply","is.numeric","local","isTRUE","mean.default","apply","apply","isTRUE","mean.default","apply","mean.default","apply","apply","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","mean.default","apply","is.numeric","local","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","apply","any","local","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","findLocalsList1","findLocalsList","findLocals","compile","compiler:::tryCompile","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis"],"filenum":[1,1,1,1,1,1,1,null,1,1,1,1,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,1,null,null,1,null,null,1,1,null,null,null,1,null,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,null,null,1,null,null,1,null,1,null,1,1,null,1,1,null,null,null,1,1,1,1,1,null,null,1,null,1,null,1,1,1,null,null,1,null,null,1,null,1,null,1,null,1,1,1,null,1,1,1,null,1,null,1,null,1,1,null,1,null,null,1,null,1,1,null,null,null,1,1,null,null,1,1,null,1,null,null,1,null,1,null,1,null,1,null,null,1,null,null,1,1,1,null,null,1,1,1,null,null,1,null,1,null,null,1,1,null,1,1,null,1,null,null,1,null,1,null,1,1,1,null,null,null,1,null,1,null,1,1,null,1,null,1,1,null,null,1,null,null,null,1,1,1,null,1,null,1,1,null,1,1,null,1,null,1,1,1,null,1,null,1,null,1,null,null,1,null,1,1,1,null,null,1,1,null,1,1,null,1,null,1,1,null,null,null,1,1,null,null,null,1,null,1,null,null,null,1,null,null,1,1,1,1,null,null,null,1,null,1,null,null,null,null,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,1,null,null,1,1,1,null,1,null,1,null,null,null,null,1,1,null,1,1,null,1,null,1,null,null,1,null,null,1,null,1,null,1,null,1,1,null,1,null,1,null,null,null,1,1,null,1,1,null,null,1,1,null,1,null,1,null,1,null,null,1,null,null,1,1,null,1,1,null,1,null,1,null,null,1,1,null,null,1,null,null,1,null,1,null,1,1,null,1,null,1,1,null,null,null,1,null,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,1,1,1,null,1,null,1,null,1,null,null,1,null,null,1,null,1,null,null,1,null,1,null,null,1,1,null,1,null,1,null,null,null,1,null,null,null,1,1,null,1,null,null,1,null,null,1,1,null,1,1,null,1,1,1,1,null,1,null,1,null,1,1,null,1,null,null,null,1,null,null,1,null,1,null,1,1,1,null,1,null,1,null,1,1,1,null,1,1,1,null,1,1,null,null,1,null,null,1,1,null,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,null,1,null,null,1,null,1,null,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,1,1,null,1,1,null,null,1,null,null,1,1,1,null,1,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,null,null,1,null,1,1,null,1,null,1,1,1,null,1,null,1,null,null,null,1,null,null,null,1,1,null,null,1,null,null,1,null,1,null,1,1,null,null,null,1,null,null,1,1,null,null,1,1,null,1,null,null,1,null,1,null,1,1,null,1,null,null,null,1,null,null,1,null,1,null,1,1,null,1,null,1,null,1,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,null,null,null,1,null,null,1,null,1,1,null,1,1,null,1,null,null,1,1,null,1,1,null,1,null,null,null,1,1,1,1,1,null,1,null,1,1,null,null,1,null,1,null,null,1,null,null,1,null,null,null,1,1,null,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,null,1,null,null,1,1,null,1,1,null,1,1,null,1,null,1,null,1,1,1,1,null,1,null,null,null,1,null,1,null,null,1,1,1,null,1,null,1,null,1,1,1,null,1,null,null,1,null,null,1,null,null,1,null,null,null,1,null,1,1,1,1,null,1,1,1,null,1,null,1,1,null,1,null,1,1,null,null,1,1,null,null,1,1,null,null,1,1,null,null,null,null,null,null,1,1,1,null,null,1,null,1,1,null,1,null,1,1,null,1,null,null,1,null,null,1,null,1,null,1,null,1,1,1,null,1,null,1,1,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,null,null,null,1,1,null,null,1,null,null,1,null,null,null,null,1,null,null,null,1,null,null,null,1,1,1,1,null,1,1,1,null,null,1,null,null,1,1,1,1,null,1,null,1,null,1,null,1,1,null,1,null,null,1,null,null,1,null,1,null,1,null,1,1,null,1,1,null,null,1,1,null,1,null,null,1,null,null,1,1,null,1,1,null,null,1,null,1,null,1,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,null,1,null,null,1,null,1,1,null,null,null,1,1,null,null,1,null,1,1,null,1,1,null,1,null,null,null,null,null,null,null,1,null,1,1,null,1,null,null,1,null,1,1,1,null,null,1,null,null,1,null,1,null,1,null,null,1,1,null,1,null,1,null,null,1,1,1,null,1,1,null,1,null,1,null,1,1,null,1,1,1,null,1,1,1,null,1,null,1,null,null,null,null,null,null,1,null,null,null,null,1,null,null,null,1,1,1,1,null,null,1,null,null,1,null,1,null,1,1,null,1,null,1,null,1,1,null,1,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,null,null,1,null,1,1,1,null,1,null,1,null,null,1,null,1,null,null,1,1,1,null,1,null,1,1,1,null,1,1,null,1,1,null,1,null,1,null,null,1,null,null,1,null,null,null,1,1,1,null,1,null,null,1,1,null,null,null,1,null,1,null,1,1,null,null,1,null,null,1,1,null,1,null,1,1,null,1,1,null,null,null,null,null,1,null,null,null,1,null,1,null,1,1,null,null,1,null,1,1,null,1,null,1,null,null,1,null,1,1,null,null,null,null,1,null,null,null,1,null,1,1,null,1,1,1,null,1,null,1,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,null,null,1,1,null,1,null,1,1,1,null,null,1,null,null,1,1,null,1,null,1,null,null,null,1,1,1,null,null,1,1,null,1,1,null,1,null,1,null,1,1,1,null,1,1,1,1,null,1,null,1,1,null,1,1,null,1,null,1,null,1,null,1,1,null,1,null,1,1,null,1,null,1,null,1,null,null,null,1,1,1,null,1,1,null,1,null,null,1,null,null,1,null,null,1,null,null,null,1,null,1,1,null,1,1,null,null,1,null,1,1,null,1,null,1,null,null,1,1,null,1,1,null,1,null,1,null,1,1,null,null,null,1,null,null,null,1,null,null,null,1,null,1,null,1,1,null,1,null,1,null,1,1,null,null,null,null,1,null,1,null,1,null,null,null,1,null,1,1,null,1,1,null,null,1,null,1,null,1,null,null,null,1,null,null,null,1,null,1,null,1,null,1,null,null,1,1,null,1,null,1,null,1,null,1,null,1,null,null,null,null,null,1,1,1,null,null,1,null,1,null,1,1,null,null,null,null,null,null,null,null,null,1,null,null,null,1,null,null,1,null,1,null,1,null,1,1,null,null,null,1,null,1,null,1,1,null,1,null,1,1,null,null,null,1,1,null,1,null,1,null,1,1,null,1,1,null,1,null,1,1,null,1,1,null,1,null,1,null,1,1,1,null,1,1,null,1,null,1,null,null,null,null,1,null,null,1,null,1,null,1,1,1,1,null,1,1,null,1,1,null,1,null,null,1,null,null,1,1,null,1,null,1,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,1,null,null,1,1,null,1,null,1,1,null,null,null,1,null,1,1,1,null,1,null,1,1,null,1,null,null,1,null,null,1,null,null,1,1,null,null,null,null,null,1,null,1,1,null,1,null,1,null,1,1,1,null,1,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,null,null,1,null,null,null,1,null,1,1,null,null,1,1,1,null,1,1,null,1,1,null,1,null,1,null,1,null,null,1,null,null,1,1,null,1,1,null,1,null,1,null,1,null,1,null,1,1,null,null,1,null,null,null,null,null,1,null,1,1,null,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,null,1,null,1,null,null,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,1,null,1,null,1,1,null,1,1,1,null,1,null,1,null,1,null,1,null,null,null,1,null,1,1,null,1,null,1,1,null,1,null,null,1,null,null,1,null,null,null,null,1,null,1,1,null,1,null,null,1,1,null,1,1,1,1,null,1,1,1,null,1,null,null,1,null,null,1,null,1,1,null,1,null,1,null,1,1,null,1,null,null,1,1,1,1,null,1,null,null,1,null,1,null,1,null,1,null,null,1,1,null,null,1,null,null,1,null,null,1,null,1,null,1,1,1,null,1,null,1,1,null,1,null,1,null,1,null,null,null,null,1,null,1,null,null,1,null,1,null,1,null,null,1,null,1,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,1,1,1,null,1,null,1,null,1,null,1,null,null,null,1,null,1,null,null,null,1,1,null,1,null,1,null,null,null,null,1,null,null,1,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,null,null,1,null,1,null,1,null,1,null,1,null,null,null,null,1,null,null,1,1,null,1,null,1,1,null,1,null,null,1,null,1,null,1,null,null,1,null,1,null,1,1,null,1,null,null,1,null,null,1,null,null,1,null,1,1,null,1,null,1,1,null,1,null,1,1,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,null,null,null,null,null,null,1,null,1,null,1,null,1,null,1,null,null,1,1,1,null,1,1,null,1,1,1,1,null,null,null,null,null,null,1,null,null,1,null,1,null,1,1,null,1,1,null,1,null,1,null,1,null,1,1,null,1,1,1,null,null,1,null,null,1,1,1,null,1,null,1,null,1,1,1,null,1,null,1,null,1,null,1,1,null,1,1,1,null,1,1,null,1,null,1,null,1,null,1,null,1,1,null,null,null,null,null,null,1,null,null,null,1,null,1,null,null,null,null,1,null,1,null,null,null,1,null,1,null,null,1,null,null,1,null,null,1,null,null,null,1,null,null,1,1,null,null,1,null,null,1,null,null,null,null,1,null,1,1,null,1,null,null,1,null,1,null,null,1,null,null,1,null,null,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,1,null,1,1,1,null,1,null,null,1,null,1,1,null,null,1,null,null,1,null,1,null,1,1,null,1,null,1,1,null,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,1,1,null,1,1,1,null,null,1,null,null,1,1,1,null,1,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,null,null,1,null,null,1,1,null,null,null,null,1,null,null,null,null,null,1,null,1,null,1,1,null,1,null,null,1,1,null,1,1,null,null,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,null,1,null,1,1,1,1,null,null,1,1,1,null,1,null,null,null,null,1,1,null,null,1,null,null,1,null,null,1,null,1,null,1,1,null,1,null,1,null,1,1,null,1,1,null,1,1,1,null,1,1,1,null,1,null,null,1,null,null,1,null,null,1,null,1,1,1,null,1,null,null,null,1,1,null,null,1,1,null,1,null,1,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,1,null,1,null,null,null,1,null,1,null,1,1,null,1,1,1,1,null,1,null,1,1,null,1,null,1,null,null,1,null,null,1,1,null,1,null,1,null,1,1,null,1,null,null,null,1,1,null,null,null,1,1,null,1,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,1,1,1,null,null,1,null,1,null,1,1,null,1,1,null,1,null,1,null,null,1,null,null,1,null,1,null,1,null,null,1,1,1,null,1,null,1,1,null,null,1,null,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,1,null,1,1,null,1,1,1,1,1,null,1,null,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,null,null,1,null,1,null,1,1,null,1,null,1,null,null,null,null,1,null,1,null,null,1,null,1,1,1,null,null,null,1,null,null,null,null,null,null,null,1,1,null,1,1,null,1,1,1,null,null,null,null,null,null,1,1,null,1,null,null,1,null,null,1,null,null,1,1,null,1,null,1,null,1,null,null,null,1,null,null,null,1,1,null,null,1,null,null,null,1,null,1,null,null,1,null,1,null,1,null,1,null,null,1,null,1,1,1,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,null,1,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,1,null,null,null,1,1,null,1,null,1,1,null,1,1,null,1,null,1,null,1,1,1,null,1,null,1,1,null,null,1,null,null,1,null,null,null,1,1,null,1,null,1,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,1,1,null,null,null,1,null,1,1,null,null,1,null,1,null,1,null,null,1,null,1,null,1,1,null,null,1,1,null,null,1,null,null,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,1,1,null,1,null,1,1,1,1,null,1,null,1,1,null,1,null,1,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,1,1,null,1,1,null,1,null,null,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,null,null,1,1,1,1,null,1,1,null,1,null,1,1,null,1,null,1,1,1,1,1,1,null,1,1,null,1,1,1,null,1,1,null,1,null,null,null,1,null,null,null,null,1,null,null,1,null,null,1,null,1,null,1,null,1,1,null,1,1,1,null,null,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,1,null,null,null,1,null,null,1,null,1,null,null,null,1,null,1,1,1,1,null,1,null,1,1,null,1,null,null,1,1,null,null,null,1,null,null,null,1,null,null,null,1,null,1,1,1,1,null,1,1,1,null,1,1,null,1,1,null,1,null,1,null,1,null,1,1,null,null,null,1,null,1,1,null,null,null,1,null,null,null,1,null,1,null,1,null,1,1,null,null,null,1,null,1,null,1,null,1,null,null,null,null,1,null,null,1,null,null,1,null,null,null,null,null,null,1,1,null,null,1,null,null,1,null,null,1,1,null,1,1,null,1,null,null,1,1,null,1,null,1,1,1,1,null,null,null,1,1,null,1,null,1,1,null,1,null,1,1,null,1,null,null,null,1,null,null,null,null,null,1,null,1,null,1,null,1,null,1,null,1,1,1,1,1,null,1,1,null,1,null,1,1,null,1,null,null,1,null,1,null,1,1,null,null,null,1,1,null,1,1,null,1,null,1,null,1,1,null,null,1,1,null,null,null,1,null,1,1,null,null,1,null,null,1,null,null,1,1,null,1,null,1,null,null,1,1,1,1,null,null,1,null,1,1,null,1,1,null,1,1,null,1,1,null,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,1,1,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,1,1,null,1,null,null,null,null,1,null,1,null,null,1,1,null,1,1,null,1,null,null,1,1,1,null,null,1,null,null,null,1,null,1,null,1,null,1,null,1,null,null,null,1,null,1,null,null,null,1,null,1,null,1,null,null,null,null,null,null,null,null,null,null,1,null,1,1,1,1,null,1,null,null,1,1,1,1,1,null,1,1,1,1,null,1,null,1,null,1,null,null,1,1,null,1,1,null,1,null,null,null,null,1,1,null,null,1,null,1,1,null,null,null,null,null,null,null,null,null,null,null,null,null,1,null,null,null,1,null,null,1,null,null,1,1,null,1,null,1,null,1,null,null,1,null,1,null,null,1,null,1,1,null,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,null,null,null,null,null,null,null,null,null,null,1,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null],"linenum":[10,10,10,10,10,10,10,null,11,11,11,11,11,11,11,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,12,null,null,12,null,null,12,12,null,null,null,12,null,12,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,null,null,12,null,null,12,null,12,null,12,12,null,12,12,null,null,null,12,12,12,12,12,null,null,12,null,12,null,12,12,12,null,null,12,null,null,12,null,12,null,12,null,12,12,12,null,12,12,12,null,12,null,12,null,12,12,null,12,null,null,12,null,12,12,null,null,null,12,12,null,null,12,12,null,12,null,null,12,null,12,null,12,null,12,null,null,12,null,null,12,12,12,null,null,12,12,12,null,null,12,null,12,null,null,12,12,null,12,12,null,12,null,null,12,null,12,null,12,12,12,null,null,null,12,null,12,null,12,12,null,12,null,12,12,null,null,12,null,null,null,12,12,12,null,12,null,12,12,null,12,12,null,12,null,12,12,12,null,12,null,12,null,12,null,null,12,null,12,12,12,null,null,12,12,null,12,12,null,12,null,12,12,null,null,null,12,12,null,null,null,12,null,12,null,null,null,12,null,null,12,12,12,12,null,null,null,12,null,12,null,null,null,null,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,12,null,null,12,12,12,null,12,null,12,null,null,null,null,12,12,null,12,12,null,12,null,12,null,null,12,null,null,12,null,12,null,12,null,12,12,null,12,null,12,null,null,null,12,12,null,12,12,null,null,12,12,null,12,null,12,null,12,null,null,12,null,null,12,12,null,12,12,null,12,null,12,null,null,12,12,null,null,12,null,null,12,null,12,null,12,12,null,12,null,12,12,null,null,null,12,null,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,12,12,12,null,12,null,12,null,12,null,null,12,null,null,12,null,12,null,null,12,null,12,null,null,12,12,null,12,null,12,null,null,null,12,null,null,null,12,12,null,12,null,null,12,null,null,12,12,null,12,12,null,12,12,12,12,null,12,null,12,null,12,12,null,12,null,null,null,12,null,null,12,null,12,null,12,12,12,null,12,null,12,null,12,12,12,null,12,12,12,null,12,12,null,null,12,null,null,12,12,null,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,null,12,null,null,12,null,12,null,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,12,12,null,12,12,null,null,12,null,null,12,12,12,null,12,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,null,null,12,null,12,12,null,12,null,12,12,12,null,12,null,12,null,null,null,12,null,null,null,12,12,null,null,12,null,null,12,null,12,null,12,12,null,null,null,12,null,null,12,12,null,null,12,12,null,12,null,null,12,null,12,null,12,12,null,12,null,null,null,12,null,null,12,null,12,null,12,12,null,12,null,12,null,12,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,null,null,null,12,null,null,12,null,12,12,null,12,12,null,12,null,null,12,12,null,12,12,null,12,null,null,null,12,12,12,12,12,null,12,null,12,12,null,null,12,null,12,null,null,12,null,null,12,null,null,null,12,12,null,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,null,12,null,null,12,12,null,12,12,null,12,12,null,12,null,12,null,12,12,12,12,null,12,null,null,null,12,null,12,null,null,12,12,12,null,12,null,12,null,12,12,12,null,12,null,null,12,null,null,12,null,null,12,null,null,null,12,null,12,12,12,12,null,12,12,12,null,12,null,12,12,null,12,null,12,12,null,null,12,12,null,null,12,12,null,null,12,12,null,null,null,null,null,null,12,12,12,null,null,12,null,12,12,null,12,null,12,12,null,12,null,null,12,null,null,12,null,12,null,12,null,12,12,12,null,12,null,12,12,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,null,null,null,12,12,null,null,12,null,null,12,null,null,null,null,12,null,null,null,12,null,null,null,12,12,12,12,null,12,12,12,null,null,12,null,null,12,12,12,12,null,12,null,12,null,12,null,12,12,null,12,null,null,12,null,null,12,null,12,null,12,null,12,12,null,12,12,null,null,12,12,null,12,null,null,12,null,null,12,12,null,12,12,null,null,12,null,12,null,12,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,null,12,null,null,12,null,12,12,null,null,null,12,12,null,null,12,null,12,12,null,12,12,null,12,null,null,null,null,null,null,null,12,null,12,12,null,12,null,null,12,null,12,12,12,null,null,12,null,null,12,null,12,null,12,null,null,12,12,null,12,null,12,null,null,12,12,12,null,12,12,null,12,null,12,null,12,12,null,12,12,12,null,12,12,12,null,12,null,12,null,null,null,null,null,null,12,null,null,null,null,12,null,null,null,12,12,12,12,null,null,12,null,null,12,null,12,null,12,12,null,12,null,12,null,12,12,null,12,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,null,null,12,null,12,12,12,null,12,null,12,null,null,12,null,12,null,null,12,12,12,null,12,null,12,12,12,null,12,12,null,12,12,null,12,null,12,null,null,12,null,null,12,null,null,null,12,12,12,null,12,null,null,12,12,null,null,null,12,null,12,null,12,12,null,null,12,null,null,12,12,null,12,null,12,12,null,12,12,null,null,null,null,null,12,null,null,null,12,null,12,null,12,12,null,null,12,null,12,12,null,12,null,12,null,null,12,null,12,12,null,null,null,null,12,null,null,null,12,null,12,12,null,12,12,12,null,12,null,12,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,null,null,12,12,null,12,null,12,12,12,null,null,12,null,null,12,12,null,12,null,12,null,null,null,12,12,12,null,null,12,12,null,12,12,null,12,null,12,null,12,12,12,null,12,12,12,12,null,12,null,12,12,null,12,12,null,12,null,12,null,12,null,12,12,null,12,null,12,12,null,12,null,12,null,12,null,null,null,12,12,12,null,12,12,null,12,null,null,12,null,null,12,null,null,12,null,null,null,12,null,12,12,null,12,12,null,null,12,null,12,12,null,12,null,12,null,null,12,12,null,12,12,null,12,null,12,null,12,12,null,null,null,12,null,null,null,12,null,null,null,12,null,12,null,12,12,null,12,null,12,null,12,12,null,null,null,null,12,null,12,null,12,null,null,null,12,null,12,12,null,12,12,null,null,12,null,12,null,12,null,null,null,12,null,null,null,12,null,12,null,12,null,12,null,null,12,12,null,12,null,12,null,12,null,12,null,12,null,null,null,null,null,12,12,12,null,null,12,null,12,null,12,12,null,null,null,null,null,null,null,null,null,12,null,null,null,12,null,null,12,null,12,null,12,null,12,12,null,null,null,12,null,12,null,12,12,null,12,null,12,12,null,null,null,12,12,null,12,null,12,null,12,12,null,12,12,null,12,null,12,12,null,12,12,null,12,null,12,null,12,12,12,null,12,12,null,12,null,12,null,null,null,null,12,null,null,12,null,12,null,12,12,12,12,null,12,12,null,12,12,null,12,null,null,12,null,null,12,12,null,12,null,12,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,12,null,null,12,12,null,12,null,12,12,null,null,null,12,null,12,12,12,null,12,null,12,12,null,12,null,null,12,null,null,12,null,null,12,12,null,null,null,null,null,12,null,12,12,null,12,null,12,null,12,12,12,null,12,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,null,null,12,null,null,null,12,null,12,12,null,null,12,12,12,null,12,12,null,12,12,null,12,null,12,null,12,null,null,12,null,null,12,12,null,12,12,null,12,null,12,null,12,null,12,null,12,12,null,null,12,null,null,null,null,null,12,null,12,12,null,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,null,12,null,12,null,null,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,12,null,12,null,12,12,null,12,12,12,null,12,null,12,null,12,null,12,null,null,null,12,null,12,12,null,12,null,12,12,null,12,null,null,12,null,null,12,null,null,null,null,12,null,12,12,null,12,null,null,12,12,null,12,12,12,12,null,12,12,12,null,12,null,null,12,null,null,12,null,12,12,null,12,null,12,null,12,12,null,12,null,null,12,12,12,12,null,12,null,null,12,null,12,null,12,null,12,null,null,12,12,null,null,12,null,null,12,null,null,12,null,12,null,12,12,12,null,12,null,12,12,null,12,null,12,null,12,null,null,null,null,12,null,12,null,null,12,null,12,null,12,null,null,12,null,12,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,12,12,12,null,12,null,12,null,12,null,12,null,null,null,12,null,12,null,null,null,12,12,null,12,null,12,null,null,null,null,12,null,null,12,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,null,null,12,null,12,null,12,null,12,null,12,null,null,null,null,12,null,null,12,12,null,12,null,12,12,null,12,null,null,12,null,12,null,12,null,null,12,null,12,null,12,12,null,12,null,null,12,null,null,12,null,null,12,null,12,12,null,12,null,12,12,null,12,null,12,12,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,null,null,null,null,null,null,12,null,12,null,12,null,12,null,12,null,null,12,12,12,null,12,12,null,12,12,12,12,null,null,null,null,null,null,12,null,null,12,null,12,null,12,12,null,12,12,null,12,null,12,null,12,null,12,12,null,12,12,12,null,null,12,null,null,12,12,12,null,12,null,12,null,12,12,12,null,12,null,12,null,12,null,12,12,null,12,12,12,null,12,12,null,12,null,12,null,12,null,12,null,12,12,null,null,null,null,null,null,12,null,null,null,12,null,12,null,null,null,null,12,null,12,null,null,null,12,null,12,null,null,12,null,null,12,null,null,12,null,null,null,12,null,null,12,12,null,null,12,null,null,12,null,null,null,null,12,null,12,12,null,12,null,null,12,null,12,null,null,12,null,null,12,null,null,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,12,null,12,12,12,null,12,null,null,12,null,12,12,null,null,12,null,null,12,null,12,null,12,12,null,12,null,12,12,null,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,12,12,null,12,12,12,null,null,12,null,null,12,12,12,null,12,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,null,null,12,null,null,12,12,null,null,null,null,12,null,null,null,null,null,12,null,12,null,12,12,null,12,null,null,12,12,null,12,12,null,null,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,null,12,null,12,12,12,12,null,null,12,12,12,null,12,null,null,null,null,12,12,null,null,12,null,null,12,null,null,12,null,12,null,12,12,null,12,null,12,null,12,12,null,12,12,null,12,12,12,null,12,12,12,null,12,null,null,12,null,null,12,null,null,12,null,12,12,12,null,12,null,null,null,12,12,null,null,12,12,null,12,null,12,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,12,null,12,null,null,null,12,null,12,null,12,12,null,12,12,12,12,null,12,null,12,12,null,12,null,12,null,null,12,null,null,12,12,null,12,null,12,null,12,12,null,12,null,null,null,12,12,null,null,null,12,12,null,12,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,12,12,12,null,null,12,null,12,null,12,12,null,12,12,null,12,null,12,null,null,12,null,null,12,null,12,null,12,null,null,12,12,12,null,12,null,12,12,null,null,12,null,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,12,null,12,12,null,12,12,12,12,12,null,12,null,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,null,null,12,null,12,null,12,12,null,12,null,12,null,null,null,null,12,null,12,null,null,12,null,12,12,12,null,null,null,12,null,null,null,null,null,null,null,12,12,null,12,12,null,12,12,12,null,null,null,null,null,null,12,12,null,12,null,null,12,null,null,12,null,null,12,12,null,12,null,12,null,12,null,null,null,12,null,null,null,12,12,null,null,12,null,null,null,12,null,12,null,null,12,null,12,null,12,null,12,null,null,12,null,12,12,12,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,null,12,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,12,null,null,null,12,12,null,12,null,12,12,null,12,12,null,12,null,12,null,12,12,12,null,12,null,12,12,null,null,12,null,null,12,null,null,null,12,12,null,12,null,12,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,12,12,null,null,null,12,null,12,12,null,null,12,null,12,null,12,null,null,12,null,12,null,12,12,null,null,12,12,null,null,12,null,null,12,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,12,12,null,12,null,12,12,12,12,null,12,null,12,12,null,12,null,12,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,12,12,null,12,12,null,12,null,null,12,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,null,null,12,12,12,12,null,12,12,null,12,null,12,12,null,12,null,12,12,12,12,12,12,null,12,12,null,12,12,12,null,12,12,null,12,null,null,null,12,null,null,null,null,12,null,null,12,null,null,12,null,12,null,12,null,12,12,null,12,12,12,null,null,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,12,null,null,null,12,null,null,12,null,12,null,null,null,12,null,12,12,12,12,null,12,null,12,12,null,12,null,null,12,12,null,null,null,12,null,null,null,12,null,null,null,12,null,12,12,12,12,null,12,12,12,null,12,12,null,12,12,null,12,null,12,null,12,null,12,12,null,null,null,12,null,12,12,null,null,null,12,null,null,null,12,null,12,null,12,null,12,12,null,null,null,12,null,12,null,12,null,12,null,null,null,null,12,null,null,12,null,null,12,null,null,null,null,null,null,12,12,null,null,12,null,null,12,null,null,12,12,null,12,12,null,12,null,null,12,12,null,12,null,12,12,12,12,null,null,null,12,12,null,12,null,12,12,null,12,null,12,12,null,12,null,null,null,12,null,null,null,null,null,12,null,12,null,12,null,12,null,12,null,12,12,12,12,12,null,12,12,null,12,null,12,12,null,12,null,null,12,null,12,null,12,12,null,null,null,12,12,null,12,12,null,12,null,12,null,12,12,null,null,12,12,null,null,null,12,null,12,12,null,null,12,null,null,12,null,null,12,12,null,12,null,12,null,null,12,12,12,12,null,null,12,null,12,12,null,12,12,null,12,12,null,12,12,null,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,12,12,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,12,12,null,12,null,null,null,null,12,null,12,null,null,12,12,null,12,12,null,12,null,null,12,12,12,null,null,12,null,null,null,12,null,12,null,12,null,12,null,12,null,null,null,12,null,12,null,null,null,12,null,12,null,12,null,null,null,null,null,null,null,null,null,null,12,null,12,12,12,12,null,12,null,null,12,12,12,12,12,null,12,12,12,12,null,12,null,12,null,12,null,null,12,12,null,12,12,null,12,null,null,null,null,12,12,null,null,12,null,12,12,null,null,null,null,null,null,null,null,null,null,null,null,null,12,null,null,null,12,null,null,12,null,null,12,12,null,12,null,12,null,12,null,null,12,null,12,null,null,12,null,12,12,null,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,13,null,null,null,null,null,null,null,null,null,null,null,13,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null],"memalloc":[124.4994735717773,124.4994735717773,124.4994735717773,124.4994735717773,124.4994735717773,124.4994735717773,124.4994964599609,124.4994964599609,139.7817077636719,139.7817077636719,139.7817077636719,139.7817077636719,139.7817077636719,139.7817077636719,139.7817077636719,170.2474517822266,170.2474517822266,170.2474517822266,170.2474517822266,170.2474517822266,170.2474517822266,170.2474517822266,170.2474517822266,170.2474517822266,170.2474517822266,170.2474517822266,170.2474517822266,170.2474517822266,170.2474517822266,170.2474975585938,170.2474975585938,170.2474975585938,170.2474975585938,170.2474975585938,170.2474975585938,170.2474975585938,170.2474975585938,170.2474975585938,170.2474975585938,170.2474975585938,170.2474975585938,170.2474975585938,170.2474975585938,170.2474975585938,170.2474975585938,170.2474975585938,170.2474975585938,170.2474975585938,170.2474975585938,170.2471923828125,170.2471923828125,170.2471923828125,170.2471923828125,185.5820236206055,185.5820236206055,185.5820236206055,185.7597579956055,185.7597579956055,185.9530334472656,186.0726547241211,186.0726547241211,186.0726547241211,186.2365493774414,186.2365493774414,186.2365493774414,186.4297943115234,186.6082077026367,186.6082077026367,186.8144073486328,186.8144073486328,187.0307998657227,187.0307998657227,187.2205963134766,187.4133377075195,187.5603179931641,187.5603179931641,187.7435302734375,187.7435302734375,187.9181289672852,187.9181289672852,188.0997314453125,188.0997314453125,188.3005447387695,188.3005447387695,188.4873733520508,188.4873733520508,188.6433792114258,188.6433792114258,188.7772445678711,188.7772445678711,188.7772445678711,188.7772445678711,188.7772445678711,188.7772445678711,185.8215866088867,185.8215866088867,185.9769058227539,185.9769058227539,186.1453399658203,186.3526382446289,186.3526382446289,186.5326843261719,186.7276077270508,186.7276077270508,186.927848815918,186.927848815918,187.1449203491211,187.3512802124023,187.5318450927734,187.7337493896484,187.9345169067383,187.9345169067383,187.9345169067383,188.119987487793,188.119987487793,188.3151168823242,188.3151168823242,188.5025787353516,188.6683044433594,188.8473358154297,188.8473358154297,188.8473358154297,188.8473358154297,188.8473358154297,188.8473358154297,185.8910903930664,185.8910903930664,186.0063781738281,186.0063781738281,186.1269760131836,186.1269760131836,186.2374801635742,186.3730163574219,186.5455093383789,186.5455093383789,186.7369537353516,186.926643371582,187.1259384155273,187.1259384155273,187.3162002563477,187.3162002563477,187.4951553344727,187.4951553344727,187.6281967163086,187.7971572875977,187.7971572875977,187.9662933349609,187.9662933349609,187.9662933349609,188.1645736694336,188.1645736694336,188.3498611450195,188.5055465698242,188.5055465698242,188.6880645751953,188.6880645751953,188.8642730712891,188.9347381591797,188.9347381591797,188.9347381591797,185.9462585449219,186.1463012695312,186.1463012695312,186.3623352050781,186.3623352050781,186.3623352050781,186.5814971923828,186.5814971923828,186.80224609375,186.80224609375,186.9947967529297,186.9947967529297,187.1616363525391,187.1616363525391,187.1616363525391,187.3271026611328,187.3271026611328,187.3271026611328,187.4978179931641,187.6729431152344,187.8619537353516,187.8619537353516,187.8619537353516,188.0610961914062,188.25341796875,188.4524307250977,188.4524307250977,188.4524307250977,188.6375503540039,188.6375503540039,188.8321685791016,188.8321685791016,188.8321685791016,189.0089340209961,189.0207748413086,189.0207748413086,186.1498489379883,186.3563766479492,186.3563766479492,186.5599212646484,186.5599212646484,186.751838684082,186.9322280883789,186.9322280883789,187.150016784668,187.150016784668,187.3678283691406,187.5808639526367,187.7160949707031,187.7160949707031,187.8441772460938,187.8441772460938,188.0377502441406,188.0377502441406,188.2183074951172,188.2183074951172,188.3888549804688,188.5950393676758,188.5950393676758,188.8352890014648,188.8352890014648,189.0618743896484,189.105339050293,189.105339050293,189.105339050293,186.24658203125,186.24658203125,186.4369659423828,186.4369659423828,186.6004104614258,186.7979431152344,186.9914779663086,186.9914779663086,187.1926956176758,187.1926956176758,187.374382019043,187.5629653930664,187.5629653930664,187.7597274780273,187.9518051147461,187.9518051147461,188.1523742675781,188.1523742675781,188.2920532226562,188.4741973876953,188.6562347412109,188.6562347412109,188.8676147460938,188.8676147460938,189.0906448364258,189.0906448364258,189.1885833740234,189.1885833740234,189.1885833740234,186.3506469726562,186.3506469726562,186.5531234741211,186.7737655639648,186.9888534545898,186.9888534545898,186.9888534545898,187.1803436279297,187.4056549072266,187.4056549072266,187.5838165283203,187.8274307250977,187.8274307250977,188.0102920532227,188.0102920532227,188.2244338989258,188.4477767944336,188.4477767944336,188.6702423095703,188.6702423095703,188.8954467773438,189.121940612793,189.121940612793,189.2704925537109,189.2704925537109,189.2704925537109,189.2704925537109,186.63818359375,186.63818359375,186.8469772338867,186.8469772338867,187.0663452148438,187.0663452148438,187.0663452148438,187.284782409668,187.4965286254883,187.6741104125977,187.8005218505859,187.8005218505859,187.9238662719727,187.9238662719727,188.0947952270508,188.0947952270508,188.2365875244141,188.2365875244141,188.4205169677734,188.4205169677734,188.6133270263672,188.6133270263672,188.8051681518555,188.8051681518555,188.9972534179688,188.9972534179688,189.1893997192383,189.1893997192383,189.3510360717773,189.3510360717773,189.3510360717773,189.3510360717773,189.3510360717773,189.3510360717773,186.7084045410156,186.7084045410156,186.7084045410156,186.902473449707,186.902473449707,187.1019973754883,187.1019973754883,187.1019973754883,187.2996292114258,187.4919509887695,187.7075424194336,187.7075424194336,187.8974075317383,187.8974075317383,188.0904693603516,188.0904693603516,188.2761077880859,188.2761077880859,188.2761077880859,188.4680023193359,188.6686248779297,188.6686248779297,188.8715438842773,189.0660781860352,189.0660781860352,189.2674179077148,189.2674179077148,189.4303665161133,189.4303665161133,189.4303665161133,189.4303665161133,189.4303665161133,189.4303665161133,186.7206802368164,186.7206802368164,186.8679428100586,186.8679428100586,187.0437622070312,187.0437622070312,187.2542495727539,187.4404602050781,187.4404602050781,187.6150588989258,187.6150588989258,187.7765579223633,187.7765579223633,187.966926574707,187.966926574707,188.1431350708008,188.3224411010742,188.3224411010742,188.4947204589844,188.6633911132812,188.6633911132812,188.6633911132812,188.828125,188.9965896606445,188.9965896606445,189.164176940918,189.164176940918,189.3698806762695,189.3698806762695,189.5082931518555,189.5082931518555,189.5082931518555,189.5082931518555,189.5082931518555,189.5082931518555,186.9291839599609,187.1095733642578,187.1095733642578,187.2882766723633,187.4452819824219,187.4452819824219,187.6249465942383,187.6249465942383,187.8062362670898,187.8062362670898,187.8062362670898,187.9950942993164,188.1775436401367,188.1775436401367,188.1775436401367,188.3610916137695,188.3610916137695,188.3610916137695,188.5553436279297,188.5553436279297,188.7573165893555,188.7573165893555,188.9414367675781,189.135986328125,189.135986328125,189.3351516723633,189.3351516723633,189.4847106933594,189.5850372314453,189.5850372314453,189.5850372314453,189.5850372314453,189.5850372314453,189.5850372314453,189.5850372314453,189.5850372314453,187.0720672607422,187.0720672607422,187.2005157470703,187.2005157470703,187.3824996948242,187.3824996948242,187.5706634521484,187.5706634521484,187.794563293457,187.794563293457,187.943359375,187.943359375,188.0914306640625,188.0914306640625,188.2531967163086,188.4536590576172,188.6570358276367,188.8700637817383,189.0791854858398,189.0791854858398,189.2742919921875,189.2742919921875,189.4957656860352,189.4957656860352,189.660530090332,189.660530090332,189.660530090332,189.660530090332,189.660530090332,189.660530090332,187.2075805664062,187.2075805664062,187.3725738525391,187.3725738525391,187.5369491577148,187.6970520019531,187.6970520019531,187.8893432617188,187.8893432617188,187.8893432617188,188.0921249389648,188.285530090332,188.285530090332,188.4720611572266,188.4720611572266,188.6372222900391,188.6372222900391,188.8244857788086,188.8244857788086,189.036247253418,189.036247253418,189.234001159668,189.234001159668,189.4129104614258,189.5805435180664,189.5805435180664,189.7348022460938,189.7348022460938,189.7348022460938,189.7348022460938,189.7348022460938,189.7348022460938,187.2749938964844,187.4622802734375,187.4622802734375,187.6539459228516,187.8558502197266,187.8558502197266,188.0553665161133,188.2550582885742,188.43359375,188.5921859741211,188.5921859741211,188.7915115356445,188.7915115356445,188.9713516235352,188.9713516235352,189.1649703979492,189.3493270874023,189.3493270874023,189.5315170288086,189.5315170288086,189.7138290405273,189.7138290405273,189.807861328125,189.807861328125,189.807861328125,187.3023376464844,187.3023376464844,187.4757080078125,187.4757080078125,187.6398544311523,187.8260345458984,188.0144195556641,188.0144195556641,188.1980285644531,188.1980285644531,188.3608474731445,188.3608474731445,188.5616760253906,188.7725448608398,188.9753265380859,188.9753265380859,189.1931686401367,189.4079513549805,189.6035308837891,189.6035308837891,189.7380142211914,189.8797454833984,189.8797454833984,189.8797454833984,189.8797454833984,189.8797454833984,189.8797454833984,187.4521179199219,187.6405258178711,187.6405258178711,187.6405258178711,187.7786026000977,187.7786026000977,187.9602890014648,188.1454010009766,188.1454010009766,188.3369903564453,188.3369903564453,188.541633605957,188.541633605957,188.7467269897461,188.7467269897461,188.9459075927734,188.9459075927734,189.1306686401367,189.1306686401367,189.2663497924805,189.2663497924805,189.3805923461914,189.5005722045898,189.5005722045898,189.6277847290039,189.6277847290039,189.7868041992188,189.7868041992188,189.9504852294922,189.9504852294922,189.9504852294922,189.9504852294922,189.9504852294922,189.9504852294922,187.5982437133789,187.5982437133789,187.7828140258789,187.7828140258789,187.7828140258789,187.9829940795898,187.9829940795898,188.1707916259766,188.1707916259766,188.3595809936523,188.3595809936523,188.5692825317383,188.5692825317383,188.5692825317383,188.7808837890625,188.7808837890625,188.9800491333008,188.9800491333008,189.1334838867188,189.1334838867188,189.2581787109375,189.2581787109375,189.3905563354492,189.5478057861328,189.711784362793,189.711784362793,189.8958587646484,190.0200958251953,190.0200958251953,190.0200958251953,190.0200958251953,190.0200958251953,190.0200958251953,187.6862716674805,187.7947158813477,187.9752197265625,187.9752197265625,188.1344909667969,188.304573059082,188.304573059082,188.4863662719727,188.4863662719727,188.6710052490234,188.6710052490234,188.6710052490234,188.8454132080078,188.8454132080078,189.0170669555664,189.0170669555664,189.1863784790039,189.1863784790039,189.3495330810547,189.3495330810547,189.5360641479492,189.5360641479492,189.7265853881836,189.8747711181641,189.8747711181641,190.0568771362305,190.0568771362305,190.088493347168,190.088493347168,190.088493347168,190.088493347168,187.7699737548828,187.7699737548828,187.9584274291992,188.1673049926758,188.1673049926758,188.3716735839844,188.3716735839844,188.5751724243164,188.7929916381836,188.9949798583984,188.9949798583984,189.1638107299805,189.1638107299805,189.3262939453125,189.3262939453125,189.5089492797852,189.5089492797852,189.6904144287109,189.6904144287109,189.8833999633789,189.8833999633789,190.0680770874023,190.1559219360352,190.1559219360352,190.1559219360352,190.1559219360352,190.1559219360352,190.1559219360352,187.9861221313477,187.9861221313477,188.1526641845703,188.1526641845703,188.338020324707,188.4994125366211,188.4994125366211,188.6943435668945,188.6943435668945,188.8963394165039,188.8963394165039,188.8963394165039,189.1135559082031,189.3364486694336,189.3364486694336,189.3364486694336,189.5626678466797,189.7956466674805,189.7956466674805,190.0453720092773,190.0453720092773,190.0453720092773,190.2221069335938,190.2221069335938,190.2221069335938,190.2221069335938,188.0017776489258,188.1306457519531,188.1306457519531,188.3137969970703,188.3137969970703,188.4650497436523,188.4650497436523,188.6403732299805,188.6403732299805,188.6403732299805,188.8502655029297,188.8502655029297,189.064826965332,189.064826965332,189.2879104614258,189.5022888183594,189.5022888183594,189.7203903198242,189.7203903198242,189.9492340087891,189.9492340087891,190.1808395385742,190.2873687744141,190.2873687744141,190.2873687744141,190.2873687744141,190.2873687744141,190.2873687744141,190.2873687744141,190.2873687744141,190.2873687744141,190.2873687744141,190.2873687744141,190.2873687744141,190.2873687744141,190.2873687744141,190.2873687744141,190.2873687744141,190.2873687744141,190.2873687744141,190.2873687744141,190.2873687744141,190.2873687744141,190.2873687744141,190.2873687744141,190.2873687744141,190.2873687744141,190.2873687744141,190.2873687744141,190.2873687744141,190.2873687744141,190.2873687744141,190.2873687744141,190.2873687744141,190.2873687744141,190.2873687744141,190.2873687744141,190.2873687744141,188.087776184082,188.087776184082,188.2434539794922,188.2434539794922,188.4173431396484,188.4173431396484,188.600715637207,188.600715637207,188.600715637207,188.7938919067383,188.7938919067383,188.9842834472656,189.1835021972656,189.1835021972656,189.3788223266602,189.5181350708008,189.5181350708008,189.7023544311523,189.7023544311523,189.7023544311523,189.9029693603516,190.106819152832,190.106819152832,190.3396606445312,190.351188659668,190.351188659668,188.219352722168,188.219352722168,188.4021835327148,188.4021835327148,188.5810470581055,188.7674102783203,188.9686737060547,189.1814575195312,189.4048538208008,189.4048538208008,189.6258239746094,189.6258239746094,189.8428955078125,190.0618438720703,190.0618438720703,190.0618438720703,190.2862930297852,190.2862930297852,190.4143676757812,190.4143676757812,190.4143676757812,190.4143676757812,190.4143676757812,190.4143676757812,188.4107971191406,188.4107971191406,188.5913848876953,188.5913848876953,188.7820663452148,188.9795074462891,188.9795074462891,188.9795074462891,189.1790161132812,189.1790161132812,189.3833084106445,189.3833084106445,189.5910339355469,189.5910339355469,189.8083419799805,190.0032043457031,190.0032043457031,190.1999130249023,190.1999130249023,190.4045562744141,190.4045562744141,190.4764785766602,190.4764785766602,190.4764785766602,190.4764785766602,190.4764785766602,190.4764785766602,188.3661041259766,188.4731063842773,188.4731063842773,188.6401901245117,188.8224411010742,188.8224411010742,189.0295028686523,189.2260360717773,189.2260360717773,189.43017578125,189.43017578125,189.6461868286133,189.6461868286133,189.8704528808594,190.0962905883789,190.3168716430664,190.5326309204102,190.5326309204102,190.53759765625,190.53759765625,190.53759765625,188.5083999633789,188.6790618896484,188.6790618896484,188.8449020385742,188.8449020385742,189.0276794433594,189.2214584350586,189.4080581665039,189.5288925170898,189.5288925170898,189.7105712890625,189.7105712890625,189.8788070678711,189.8788070678711,190.0626602172852,190.2289352416992,190.4194488525391,190.4194488525391,190.5977401733398,190.5977401733398,190.5977401733398,190.5977401733398,190.5977401733398,190.5977401733398,188.5905609130859,188.5905609130859,188.5905609130859,188.749382019043,188.749382019043,188.9193801879883,188.9193801879883,189.1073150634766,189.1073150634766,189.300163269043,189.5113906860352,189.722785949707,189.9645156860352,189.9645156860352,190.1905288696289,190.4096527099609,190.6246719360352,190.6246719360352,190.6568603515625,190.6568603515625,188.6572113037109,188.8260192871094,188.8260192871094,189.0020294189453,189.0020294189453,189.1835327148438,189.3866958618164,189.3866958618164,189.3866958618164,189.6031494140625,189.7715377807617,189.7715377807617,189.9786148071289,190.1906967163086,190.4056777954102,190.4056777954102,190.4056777954102,190.6213912963867,190.7150650024414,190.7150650024414,190.7150650024414,190.7150650024414,190.7150650024414,190.7150650024414,188.897102355957,189.0763931274414,189.2630996704102,189.4560852050781,189.4560852050781,189.4560852050781,189.6041641235352,189.6041641235352,189.7772445678711,189.9849472045898,189.9849472045898,190.1990280151367,190.1990280151367,190.410888671875,190.6122589111328,190.6122589111328,190.7723159790039,190.7723159790039,190.7723159790039,190.7723159790039,190.7723159790039,190.7723159790039,188.8792495727539,188.8792495727539,189.0591049194336,189.0591049194336,189.2315979003906,189.2315979003906,189.4183731079102,189.6136856079102,189.8433074951172,189.8433074951172,190.0586166381836,190.0586166381836,190.2823486328125,190.5054473876953,190.7356414794922,190.7356414794922,190.8286285400391,190.8286285400391,190.8286285400391,188.8940887451172,188.8940887451172,189.0684967041016,189.0684967041016,189.24853515625,189.24853515625,189.4280471801758,189.4280471801758,189.6219635009766,189.6219635009766,189.8171234130859,189.8171234130859,190.0111770629883,190.0111770629883,190.0111770629883,190.2125549316406,190.3965225219727,190.3965225219727,190.3965225219727,190.6057052612305,190.6057052612305,190.8245544433594,190.8840255737305,190.8840255737305,190.8840255737305,189.0030975341797,189.0030975341797,189.1861267089844,189.1861267089844,189.3698501586914,189.3698501586914,189.5770950317383,189.5770950317383,189.7674560546875,189.7674560546875,189.9500198364258,190.123046875,190.308349609375,190.4867477416992,190.4867477416992,190.6639633178711,190.8561096191406,190.9385986328125,190.9385986328125,190.9385986328125,190.9385986328125,190.9385986328125,190.9385986328125,189.2226104736328,189.4021224975586,189.590690612793,189.790397644043,189.790397644043,189.9695892333984,189.9695892333984,190.1592788696289,190.1592788696289,190.3666687011719,190.3666687011719,190.5838851928711,190.8074417114258,190.8074417114258,190.9922180175781,190.9922180175781,190.9922180175781,190.9922180175781,190.9922180175781,190.9922180175781,189.2564010620117,189.2564010620117,189.4393539428711,189.4393539428711,189.6283645629883,189.6283645629883,189.8237152099609,190.0229873657227,190.0229873657227,190.21923828125,190.4148559570312,190.4148559570312,190.4148559570312,190.6215362548828,190.8400192260742,190.8400192260742,191.0449829101562,191.0449829101562,191.0449829101562,191.0449829101562,191.0449829101562,191.0449829101562,189.2556762695312,189.4043884277344,189.4043884277344,189.5872344970703,189.7311401367188,189.7311401367188,189.9322891235352,190.1453170776367,190.1453170776367,190.3711013793945,190.3711013793945,190.6049652099609,190.8376998901367,190.8376998901367,191.0689544677734,191.0689544677734,191.096923828125,191.096923828125,189.3659286499023,189.3659286499023,189.5472106933594,189.7309188842773,189.7309188842773,189.9274139404297,189.9274139404297,190.1413192749023,190.1413192749023,190.366828918457,190.366828918457,190.5866851806641,190.5866851806641,190.7914428710938,190.7914428710938,191.0142974853516,191.1480331420898,191.1480331420898,191.1480331420898,191.1480331420898,191.1480331420898,191.1480331420898,189.4740219116211,189.4740219116211,189.6004943847656,189.6980895996094,189.6980895996094,189.7963790893555,189.7963790893555,189.8960723876953,190.0702743530273,190.0702743530273,190.2491836547852,190.4236679077148,190.4236679077148,190.6226425170898,190.8342819213867,190.8342819213867,191.0296401977539,191.1661529541016,191.1661529541016,191.1982574462891,191.1982574462891,191.1982574462891,191.1982574462891,191.1982574462891,191.1982574462891,189.6232223510742,189.6232223510742,189.7951736450195,189.7951736450195,189.9709625244141,190.1645126342773,190.1645126342773,190.3430252075195,190.3430252075195,190.5433654785156,190.742073059082,190.742073059082,190.9353790283203,191.1401596069336,191.2477416992188,191.2477416992188,191.2477416992188,191.2477416992188,191.2477416992188,191.2477416992188,189.6769332885742,189.6769332885742,189.8445129394531,189.8445129394531,190.0352783203125,190.0352783203125,190.0352783203125,190.2179946899414,190.40673828125,190.40673828125,190.58837890625,190.58837890625,190.7392883300781,190.7392883300781,190.7392883300781,190.843391418457,190.9474487304688,191.0547943115234,191.0547943115234,191.1580200195312,191.2746429443359,191.2746429443359,191.2964019775391,191.2964019775391,191.2964019775391,191.2964019775391,189.723030090332,189.9073867797852,189.9073867797852,190.0955581665039,190.2977066040039,190.5117797851562,190.5117797851562,190.7183227539062,190.9149627685547,191.0760650634766,191.0760650634766,191.2727737426758,191.2727737426758,191.3442153930664,191.3442153930664,191.3442153930664,191.3442153930664,191.3442153930664,191.3442153930664,189.7124786376953,189.8929672241211,189.8929672241211,190.0746002197266,190.0746002197266,190.2636489868164,190.4629440307617,190.4629440307617,190.6636428833008,190.6636428833008,190.8690185546875,191.0639038085938,191.2654190063477,191.3913650512695,191.3913650512695,191.3913650512695,191.3913650512695,191.3913650512695,191.3913650512695,189.899169921875,189.899169921875,190.0818481445312,190.0818481445312,190.2727203369141,190.4659881591797,190.4659881591797,190.6621704101562,190.6621704101562,190.8121566772461,190.8121566772461,191.0016479492188,191.2149124145508,191.2149124145508,191.4140853881836,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,191.4377212524414,189.8423004150391,189.8423004150391,189.8423004150391,189.8423004150391,189.8423004150391,189.8423004150391,189.9449462890625,189.9449462890625,190.1267700195312,190.1267700195312,190.1267700195312,190.3201599121094,190.3201599121094,190.516731262207,190.7181549072266,190.9336395263672,190.9336395263672,191.1446838378906,191.1446838378906,191.3475494384766,191.3475494384766,191.5836029052734,191.8193740844727,191.8193740844727,192.0561370849609,192.0561370849609,192.3058624267578,192.5350952148438,192.7442016601562,192.9317321777344,192.9317321777344,193.1240997314453,193.1240997314453,193.299690246582,193.4605026245117,193.6390762329102,193.6390762329102,193.8202285766602,194.0117721557617,194.0117721557617,194.1890029907227,194.3695678710938,194.3695678710938,194.5438537597656,194.5438537597656,194.6994781494141,194.6994781494141,194.6994781494141,194.6994781494141,194.6994781494141,194.6994781494141,190.098876953125,190.098876953125,190.2907943725586,190.2907943725586,190.493537902832,190.7097473144531,190.9168930053711,190.9168930053711,191.1380157470703,191.1380157470703,191.1380157470703,191.3391571044922,191.5533981323242,191.5533981323242,191.769416809082,191.769416809082,191.9929733276367,191.9929733276367,192.2375411987305,192.2375411987305,192.4330749511719,192.6518478393555,192.6518478393555,192.6518478393555,192.8656005859375,192.8656005859375,193.0879592895508,193.2962417602539,193.502197265625,193.502197265625,193.7163238525391,193.7163238525391,193.9414749145508,194.1755523681641,194.1755523681641,194.4096908569336,194.6370086669922,194.6370086669922,194.8323287963867,194.8323287963867,194.8323287963867,194.8323287963867,194.8323287963867,194.8323287963867,194.8323287963867,194.8323287963867,190.3172073364258,190.3172073364258,190.5186386108398,190.5186386108398,190.7296295166016,190.9557876586914,190.9557876586914,191.1830596923828,191.4199066162109,191.4199066162109,191.6439666748047,191.8791427612305,191.8791427612305,192.1175765991211,192.1175765991211,192.3562469482422,192.3562469482422,192.3562469482422,192.5910339355469,192.5910339355469,192.8235855102539,193.042724609375,193.042724609375,193.2710037231445,193.2710037231445,193.2710037231445,193.4531555175781,193.4531555175781,193.6654510498047,193.6654510498047,193.8649826049805,193.8649826049805,194.0873870849609,194.3208541870117,194.3208541870117,194.5572204589844,194.7841796875,194.9630966186523,194.9630966186523,194.9630966186523,194.9630966186523,190.5417938232422,190.7398681640625,190.7398681640625,190.9281234741211,191.1199417114258,191.1199417114258,191.3226623535156,191.5286560058594,191.5286560058594,191.74365234375,191.9837875366211,191.9837875366211,192.2194671630859,192.2194671630859,192.4554824829102,192.4554824829102,192.6907806396484,192.6907806396484,192.9247589111328,193.1609268188477,193.1609268188477,193.3960189819336,193.3960189819336,193.6315383911133,193.6315383911133,193.8670120239258,193.8670120239258,194.1013488769531,194.3339920043945,194.3339920043945,194.5669860839844,194.5669860839844,194.7964935302734,195.0199432373047,195.0916595458984,195.0916595458984,195.0916595458984,195.0916595458984,195.0916595458984,195.0916595458984,190.779411315918,190.9792785644531,190.9792785644531,191.1770553588867,191.1770553588867,191.3706283569336,191.3706283569336,191.5553665161133,191.5553665161133,191.7362823486328,191.9464569091797,192.1876449584961,192.1876449584961,192.4281845092773,192.6428680419922,192.8779983520508,192.8779983520508,193.1118392944336,193.3456268310547,193.3456268310547,193.5786056518555,193.5786056518555,193.8009490966797,193.8009490966797,194.0287017822266,194.2530364990234,194.4396820068359,194.4396820068359,194.6666259765625,194.903450012207,195.1161270141602,195.2181549072266,195.2181549072266,195.2181549072266,195.2181549072266,190.9595108032227,191.1572723388672,191.1572723388672,191.3488082885742,191.5457916259766,191.5457916259766,191.7353591918945,191.7353591918945,191.9235992431641,191.9235992431641,192.1336822509766,192.1336822509766,192.36865234375,192.6053009033203,192.6053009033203,192.8430786132812,192.8430786132812,193.0785598754883,193.3110656738281,193.3110656738281,193.5450210571289,193.5450210571289,193.7753753662109,193.7753753662109,194.0126495361328,194.0126495361328,194.2023086547852,194.2023086547852,194.408561706543,194.6425476074219,194.8731994628906,194.8731994628906,195.1024017333984,195.3237762451172,195.3237762451172,195.3427276611328,195.3427276611328,195.3427276611328,195.3427276611328,195.3427276611328,195.3427276611328,191.2236862182617,191.2236862182617,191.2236862182617,191.4223175048828,191.4223175048828,191.6181488037109,191.6181488037109,191.7860641479492,191.7860641479492,191.9644165039062,192.1686706542969,192.1686706542969,192.3677673339844,192.5936279296875,192.5936279296875,192.5936279296875,192.8326034545898,192.8326034545898,193.0919570922852,193.328369140625,193.328369140625,193.5569686889648,193.5569686889648,193.7905578613281,193.7905578613281,193.7905578613281,194.0242614746094,194.2592926025391,194.2592926025391,194.4937362670898,194.7289962768555,194.7289962768555,194.9642868041992,194.9642868041992,195.1833038330078,195.1833038330078,195.3642654418945,195.4651260375977,195.4651260375977,195.4651260375977,195.4651260375977,195.4651260375977,195.4651260375977,195.4651260375977,195.4651260375977,195.4651260375977,195.4651260375977,195.4651260375977,195.4651260375977,191.3994598388672,191.3994598388672,191.6035537719727,191.6035537719727,191.8149871826172,192.0220489501953,192.0220489501953,192.2605209350586,192.2605209350586,192.4747772216797,192.4747772216797,192.6659393310547,192.9247512817383,192.9247512817383,193.1063385009766,193.1063385009766,193.1063385009766,193.2552947998047,193.2552947998047,193.4690246582031,193.4690246582031,193.6971664428711,193.6971664428711,193.9307022094727,193.9307022094727,194.1664123535156,194.1664123535156,194.4029769897461,194.6377563476562,194.6377563476562,194.8736038208008,195.1099395751953,195.1099395751953,195.1099395751953,195.3415908813477,195.3415908813477,195.5663146972656,195.5663146972656,195.5856399536133,195.5856399536133,195.5856399536133,195.5856399536133,195.5856399536133,195.5856399536133,195.5856399536133,195.5856399536133,191.6318893432617,191.6318893432617,191.8317337036133,191.8317337036133,191.9989776611328,191.9989776611328,192.1918411254883,192.1918411254883,192.3580551147461,192.4998397827148,192.6435470581055,192.6435470581055,192.845703125,192.845703125,193.0092468261719,193.0092468261719,193.1488800048828,193.1488800048828,193.3462753295898,193.3462753295898,193.5851211547852,193.5851211547852,193.8172836303711,193.8172836303711,194.0529098510742,194.0529098510742,194.2881774902344,194.5236053466797,194.7590560913086,194.7590560913086,194.7590560913086,194.9943618774414,194.9943618774414,195.2308959960938,195.2308959960938,195.4403991699219,195.6641616821289,195.6641616821289,195.7041625976562,195.7041625976562,195.7041625976562,195.7041625976562,195.7041625976562,195.7041625976562,191.8042068481445,191.8042068481445,192.0035705566406,192.0035705566406,192.2079772949219,192.2079772949219,192.4541931152344,192.4541931152344,192.4541931152344,192.6945724487305,192.6945724487305,192.9349594116211,192.9349594116211,193.1758880615234,193.1758880615234,193.4167098999023,193.6658401489258,193.6658401489258,193.9113616943359,193.9113616943359,194.1555938720703,194.1555938720703,194.4014511108398,194.4014511108398,194.64697265625,194.8924179077148,194.8924179077148,195.0571823120117,195.0571823120117,195.1774368286133,195.2983093261719,195.2983093261719,195.4138031005859,195.4138031005859,195.5215682983398,195.7078323364258,195.7078323364258,195.8208389282227,195.8208389282227,195.8208389282227,195.8208389282227,191.8602752685547,192.0669326782227,192.0669326782227,192.2501831054688,192.4342575073242,192.4342575073242,192.6453018188477,192.6453018188477,192.8737106323242,193.1102981567383,193.1102981567383,193.347541809082,193.5825042724609,193.5825042724609,193.8171844482422,193.8171844482422,194.0512619018555,194.0512619018555,194.2854309082031,194.5242004394531,194.7643814086914,194.7643814086914,195.0083160400391,195.2493515014648,195.2493515014648,195.4938125610352,195.4938125610352,195.73193359375,195.73193359375,195.9355163574219,195.9355163574219,195.9355163574219,195.9355163574219,195.9355163574219,195.9355163574219,192.0141448974609,192.0141448974609,192.2078018188477,192.2078018188477,192.3977355957031,192.5919876098633,192.8182830810547,193.0560684204102,193.0560684204102,193.3131942749023,193.5498428344727,193.5498428344727,193.7850570678711,194.0225982666016,194.0225982666016,194.2633514404297,194.2633514404297,194.2633514404297,194.4948043823242,194.4948043823242,194.4948043823242,194.7282943725586,194.9463195800781,194.9463195800781,195.1792068481445,195.1792068481445,195.4137496948242,195.6578369140625,195.6578369140625,195.8879470825195,195.8879470825195,196.048469543457,196.048469543457,196.048469543457,196.048469543457,196.048469543457,196.048469543457,192.2093811035156,192.2093811035156,192.2093811035156,192.4032592773438,192.4032592773438,192.590705871582,192.590705871582,192.7957153320312,193.0238647460938,193.2615814208984,193.2615814208984,193.4994735717773,193.4994735717773,193.7362442016602,193.9729232788086,193.9729232788086,194.2117309570312,194.2117309570312,194.4547653198242,194.4547653198242,194.6975021362305,194.9410705566406,195.2098693847656,195.2098693847656,195.4531021118164,195.4531021118164,195.6961364746094,195.9361801147461,195.9361801147461,196.1595230102539,196.1595230102539,196.1595230102539,196.1595230102539,196.1595230102539,196.1595230102539,196.1595230102539,196.1595230102539,196.1595230102539,192.5278167724609,192.7132415771484,192.7132415771484,192.9133071899414,192.9133071899414,193.1303405761719,193.1303405761719,193.3603820800781,193.3603820800781,193.5971755981445,193.8338851928711,193.8338851928711,194.0729904174805,194.0729904174805,194.3121643066406,194.3121643066406,194.5512313842773,194.7961959838867,195.0409317016602,195.0409317016602,195.2871780395508,195.5335464477539,195.5335464477539,195.7799072265625,195.7799072265625,196.0233001708984,196.0233001708984,196.2583694458008,196.2583694458008,196.2687835693359,196.2687835693359,196.2687835693359,196.2687835693359,196.2687835693359,196.2687835693359,192.7073440551758,192.7073440551758,192.8926086425781,192.8926086425781,193.0986557006836,193.0986557006836,193.3227157592773,193.3227157592773,193.5582046508789,193.5582046508789,193.7937469482422,194.0319976806641,194.0319976806641,194.0319976806641,194.2716751098633,194.5138320922852,194.7584609985352,194.7584609985352,195.0038375854492,195.2508926391602,195.2508926391602,195.4981536865234,195.7444458007812,195.7444458007812,195.9914093017578,195.9914093017578,196.2296524047852,196.2296524047852,196.376350402832,196.376350402832,196.376350402832,196.376350402832,196.376350402832,196.376350402832,192.7453842163086,192.9334945678711,192.9334945678711,193.1229629516602,193.3364410400391,193.3364410400391,193.5645446777344,193.5645446777344,193.7975616455078,193.7975616455078,194.0346221923828,194.0346221923828,194.2733001708984,194.2733001708984,194.5063552856445,194.7518081665039,194.7518081665039,194.7518081665039,194.9925765991211,194.9925765991211,195.2559509277344,195.2559509277344,195.5026550292969,195.5026550292969,195.7484817504883,195.7484817504883,195.9951019287109,196.2380905151367,196.2380905151367,196.2380905151367,196.473258972168,196.473258972168,196.4820404052734,196.4820404052734,196.4820404052734,196.4820404052734,193.0155410766602,193.0155410766602,193.1975631713867,193.1975631713867,193.4032211303711,193.6207427978516,193.6207427978516,193.8334579467773,193.8334579467773,193.8334579467773,194.032958984375,194.032958984375,194.2451248168945,194.2451248168945,194.4813461303711,194.4813461303711,194.7180557250977,194.7180557250977,194.9617309570312,194.9617309570312,195.2019577026367,195.2019577026367,195.4441528320312,195.4441528320312,195.686637878418,195.686637878418,195.930534362793,196.1734085083008,196.1734085083008,196.4101104736328,196.586181640625,196.586181640625,196.586181640625,196.586181640625,193.057487487793,193.2429656982422,193.2429656982422,193.42626953125,193.6314010620117,193.8396987915039,193.8396987915039,194.055061340332,194.055061340332,194.2882080078125,194.2882080078125,194.5261535644531,194.5261535644531,194.7655258178711,194.7655258178711,195.0052719116211,195.0052719116211,195.2438507080078,195.2438507080078,195.4871292114258,195.7339706420898,195.7339706420898,195.9817962646484,195.9817962646484,196.2272186279297,196.468864440918,196.468864440918,196.6885681152344,196.6885681152344,196.6885681152344,196.6885681152344,196.6885681152344,196.6885681152344,193.1679000854492,193.1679000854492,193.3540649414062,193.3540649414062,193.3540649414062,193.5398712158203,193.5398712158203,193.741828918457,193.9550323486328,193.9550323486328,194.179313659668,194.179313659668,194.3997573852539,194.6365814208984,194.8994445800781,194.8994445800781,195.1381683349609,195.3759307861328,195.6062622070312,195.8433685302734,195.8433685302734,196.0897903442383,196.336311340332,196.5780715942383,196.5780715942383,196.7893371582031,196.7893371582031,196.7893371582031,196.7893371582031,196.7893371582031,196.7893371582031,193.3274230957031,193.3274230957031,193.5099182128906,193.6948852539062,193.6948852539062,193.8929824829102,193.8929824829102,194.0932006835938,194.0932006835938,194.3091049194336,194.540153503418,194.540153503418,194.7779312133789,194.7779312133789,194.7779312133789,195.016975402832,195.2565078735352,195.4867324829102,195.7218551635742,195.7218551635742,195.9441604614258,195.9441604614258,195.9441604614258,196.1759262084961,196.1759262084961,196.3266754150391,196.3266754150391,196.4731826782227,196.4731826782227,196.5993728637695,196.5993728637695,196.5993728637695,196.7338333129883,196.8883819580078,196.8883819580078,196.8883819580078,196.8883819580078,196.8883819580078,196.8883819580078,193.4907836914062,193.4907836914062,193.4907836914062,193.6743698120117,193.6743698120117,193.8567962646484,193.8567962646484,194.040168762207,194.223014831543,194.4171142578125,194.4171142578125,194.6176834106445,194.6176834106445,194.8212814331055,195.0251846313477,195.0251846313477,195.2304229736328,195.2304229736328,195.434326171875,195.434326171875,195.6378936767578,195.6378936767578,195.8323287963867,195.8323287963867,195.8323287963867,196.0263824462891,196.0263824462891,196.2399597167969,196.2399597167969,196.2399597167969,196.4343872070312,196.4343872070312,196.6167068481445,196.6167068481445,196.7300720214844,196.7300720214844,196.7300720214844,196.84375,196.84375,196.9859085083008,196.9859085083008,196.9859085083008,196.9859085083008,196.9859085083008,196.9859085083008,196.9859085083008,196.9859085083008,196.9859085083008,196.9859085083008,196.9859085083008,196.9859085083008,196.9859085083008,196.9859085083008,196.9859085083008,196.9859085083008,196.9859085083008,196.9859085083008,196.9859085083008,196.9859085083008,196.9859085083008,196.9859085083008,196.9859085083008,196.9859085083008,196.9859085083008,196.9859085083008,196.9859085083008,196.9859085083008,196.9859085083008,196.9859085083008,196.9859085083008,196.9859085083008,196.9859085083008,196.9859085083008,196.9859085083008,196.9859085083008,196.9859085083008,196.9859085083008,196.9859085083008,196.9859085083008,196.9859085083008,196.9859085083008,196.9859085083008,196.9859085083008,196.9859085083008,196.9859085083008,196.9859085083008,196.9859085083008,193.6293487548828,193.6293487548828,193.6293487548828,193.6293487548828,193.6293487548828,193.6293487548828,193.7653884887695,193.9338455200195,194.1058120727539,194.2822723388672,194.2822723388672,194.4644775390625,194.4644775390625,194.6572799682617,194.6572799682617,194.8685760498047,194.8685760498047,195.0954513549805,195.0954513549805,195.3116149902344,195.3116149902344,195.5076370239258,195.5076370239258,195.7312088012695,195.7312088012695,195.9801940917969,195.9801940917969,196.198371887207,196.4326248168945,196.4326248168945,196.6703414916992,196.6703414916992,196.9060287475586,196.9060287475586,197.081657409668,197.081657409668,197.081657409668,197.081657409668,197.081657409668,197.081657409668,193.8046798706055,193.9834899902344,193.9834899902344,194.169075012207,194.169075012207,194.3651504516602,194.3651504516602,194.5753021240234,194.5753021240234,194.7978744506836,194.7978744506836,195.0312118530273,195.0312118530273,195.0312118530273,195.2651214599609,195.2651214599609,195.4972534179688,195.4972534179688,195.7296295166016,195.7296295166016,195.9645614624023,195.9645614624023,196.2021560668945,196.2021560668945,196.441032409668,196.441032409668,196.6864547729492,196.6864547729492,196.9322967529297,196.9322967529297,197.1713104248047,197.1713104248047,197.1760482788086,197.1760482788086,197.1760482788086,197.1760482788086,197.1760482788086,197.1760482788086,194.077033996582,194.2594528198242,194.2594528198242,194.4497222900391,194.4497222900391,194.6529388427734,194.8725814819336,194.8725814819336,195.1051025390625,195.1051025390625,195.3394012451172,195.572380065918,195.572380065918,195.8025894165039,195.8025894165039,196.0345916748047,196.0345916748047,196.0345916748047,196.2742691040039,196.2742691040039,196.5113983154297,196.5113983154297,196.7561950683594,197.002685546875,197.002685546875,197.2460784912109,197.2460784912109,197.2460784912109,197.268928527832,197.268928527832,197.268928527832,197.268928527832,197.268928527832,197.268928527832,194.2003555297852,194.2003555297852,194.3816909790039,194.5667953491211,194.5667953491211,194.7645797729492,194.7645797729492,194.9778900146484,195.206184387207,195.206184387207,195.4397430419922,195.4397430419922,195.6950607299805,195.9257049560547,196.1572647094727,196.1572647094727,196.3895950317383,196.3895950317383,196.6252593994141,196.6252593994141,196.8685302734375,196.8685302734375,197.1125793457031,197.1125793457031,197.1125793457031,197.3544006347656,197.3544006347656,197.3603439331055,197.3603439331055,197.3603439331055,197.3603439331055,197.3603439331055,197.3603439331055,194.3556060791016,194.3556060791016,194.5371551513672,194.5371551513672,194.7212753295898,194.7212753295898,194.9228668212891,194.9228668212891,195.140266418457,195.140266418457,195.3726348876953,195.3726348876953,195.3726348876953,195.6066818237305,195.8403091430664,196.0724105834961,196.0724105834961,196.3044509887695,196.5404281616211,196.5404281616211,196.7779006958008,197.0225982666016,197.2678070068359,197.4502487182617,197.4502487182617,197.4502487182617,197.4502487182617,197.4502487182617,197.4502487182617,194.3828659057617,194.5601654052734,194.5601654052734,194.5601654052734,194.7418060302734,194.7418060302734,194.932731628418,194.932731628418,195.1387939453125,195.3613662719727,195.3613662719727,195.593635559082,195.8256759643555,195.8256759643555,196.0568237304688,196.0568237304688,196.2886276245117,196.2886276245117,196.5193405151367,196.5193405151367,196.7551574707031,196.9908294677734,196.9908294677734,197.2337493896484,197.4767913818359,197.5386962890625,197.5386962890625,197.5386962890625,197.5386962890625,197.5386962890625,197.5386962890625,194.5848388671875,194.7644195556641,194.9477462768555,194.9477462768555,195.1470642089844,195.1470642089844,195.3630905151367,195.3630905151367,195.5937805175781,195.7376708984375,195.8718032836914,195.8718032836914,195.9921569824219,195.9921569824219,196.1099014282227,196.1099014282227,196.2276458740234,196.2276458740234,196.3579177856445,196.5456695556641,196.5456695556641,196.7322158813477,196.957275390625,197.1747055053711,197.1747055053711,197.3639831542969,197.5444412231445,197.5444412231445,197.625732421875,197.625732421875,197.625732421875,197.625732421875,194.7100830078125,194.7100830078125,194.8820953369141,194.8820953369141,195.0234146118164,195.2098693847656,195.2098693847656,195.4077987670898,195.4077987670898,195.6129150390625,195.6129150390625,195.6129150390625,195.838752746582,195.838752746582,196.068489074707,196.068489074707,196.2689895629883,196.2689895629883,196.458366394043,196.458366394043,196.6268157958984,196.6268157958984,196.8003311157227,197.0327301025391,197.0327301025391,197.2418670654297,197.2418670654297,197.4371490478516,197.4371490478516,197.6326141357422,197.6326141357422,197.7114181518555,197.7114181518555,197.7114181518555,197.7114181518555,197.7114181518555,197.7114181518555,197.7114181518555,197.7114181518555,197.7114181518555,194.9227600097656,194.9227600097656,195.0997924804688,195.0997924804688,195.2814483642578,195.2814483642578,195.4666137695312,195.6546478271484,195.8533172607422,195.8533172607422,195.8533172607422,196.0329971313477,196.0329971313477,196.0329971313477,196.2195358276367,196.2195358276367,196.4308166503906,196.4308166503906,196.4308166503906,196.6533279418945,196.6533279418945,196.8837738037109,197.1158981323242,197.1158981323242,197.3359069824219,197.3359069824219,197.5304870605469,197.6979064941406,197.6979064941406,197.7956466674805,197.7956466674805,197.7956466674805,197.7956466674805,197.7956466674805,197.7956466674805,194.9440689086914,194.9440689086914,195.1074523925781,195.1074523925781,195.2553482055664,195.2553482055664,195.4157333374023,195.4157333374023,195.5320739746094,195.5320739746094,195.6795196533203,195.6795196533203,195.8432159423828,195.8432159423828,196.0020523071289,196.1741409301758,196.1741409301758,196.3707809448242,196.5817565917969,196.5817565917969,196.7709884643555,196.9807891845703,197.1741638183594,197.1741638183594,197.4024963378906,197.4024963378906,197.4024963378906,197.5842666625977,197.5842666625977,197.8018417358398,197.8785400390625,197.8785400390625,197.8785400390625,197.8785400390625,197.8785400390625,197.8785400390625,195.0522155761719,195.0522155761719,195.2038116455078,195.2038116455078,195.3372192382812,195.489990234375,195.489990234375,195.6577606201172,195.6577606201172,195.853401184082,196.0657501220703,196.0657501220703,196.0657501220703,196.2789306640625,196.2789306640625,196.4834289550781,196.6753768920898,196.6753768920898,196.9032745361328,196.9032745361328,197.1078948974609,197.1078948974609,197.2654571533203,197.2654571533203,197.4313354492188,197.4313354492188,197.632942199707,197.632942199707,197.8649597167969,197.9601669311523,197.9601669311523,197.9601669311523,197.9601669311523,195.1981658935547,195.3551483154297,195.4735946655273,195.4735946655273,195.6307220458984,195.7544326782227,195.9267044067383,195.9267044067383,196.1274185180664,196.2630920410156,196.2630920410156,196.2630920410156,196.4573822021484,196.6488800048828,196.7665634155273,196.7665634155273,196.9269561767578,197.0621948242188,197.0621948242188,197.2206344604492,197.2206344604492,197.4026031494141,197.5895004272461,197.5895004272461,197.8000793457031,197.8000793457031,198.0138549804688,198.0138549804688,198.0403518676758,198.0403518676758,198.0403518676758,198.0403518676758,195.326171875,195.326171875,195.4512939453125,195.4512939453125,195.5497360229492,195.5497360229492,195.5497360229492,195.6492767333984,195.7489166259766,195.7489166259766,195.8522644042969,195.8522644042969,195.8522644042969,195.9552612304688,195.9552612304688,196.1184616088867,196.1184616088867,196.3270874023438,196.3270874023438,196.5397872924805,196.5397872924805,196.6682357788086,196.6682357788086,196.8693618774414,197.082145690918,197.082145690918,197.2274703979492,197.2274703979492,197.2274703979492,197.3407516479492,197.4964447021484,197.4964447021484,197.6110992431641,197.7552947998047,197.7552947998047,197.7552947998047,197.8791961669922,197.8791961669922,197.9983367919922,197.9983367919922,197.9983367919922,198.1194000244141,198.1194000244141,198.1194000244141,198.1194000244141,198.1194000244141,198.1194000244141,198.1194000244141,198.1194000244141,198.1194000244141,195.4743576049805,195.4743576049805,195.6519012451172,195.6519012451172,195.8188018798828,195.8188018798828,195.8188018798828,196.0075912475586,196.0075912475586,196.2112121582031,196.414421081543,196.603401184082,196.8102493286133,196.8102493286133,196.8102493286133,197.0205078125,197.22802734375,197.4421234130859,197.4421234130859,197.6562194824219,197.6562194824219,197.8701248168945,197.8701248168945,197.8701248168945,198.0674057006836,198.197021484375,198.197021484375,198.197021484375,198.197021484375,198.197021484375,198.197021484375,198.197021484375,198.197021484375,198.197021484375,195.6576995849609,195.6576995849609,195.8308715820312,195.8308715820312,196.0099945068359,196.1947708129883,196.1947708129883,196.3787384033203,196.3787384033203,196.5676727294922,196.5676727294922,196.7704010009766,196.9756546020508,196.9756546020508,197.1890869140625,197.3645095825195,197.3645095825195,197.4981002807617,197.6642074584961,197.794059753418,197.794059753418,197.9884872436523,198.0987548828125,198.2087707519531,198.2087707519531,198.2734756469727,198.2734756469727,198.2734756469727,198.2734756469727,198.2734756469727,198.2734756469727,198.2734756469727,198.2734756469727,198.2734756469727,195.7677536010742,195.7677536010742,195.9595489501953,196.1319351196289,196.3019180297852,196.3019180297852,196.4735794067383,196.4735794067383,196.645133972168,196.645133972168,196.822265625,196.9922561645508,196.9922561645508,196.9922561645508,197.1719131469727,197.3498458862305,197.3498458862305,197.5188446044922,197.5188446044922,197.6947860717773,197.8780288696289,197.8780288696289,198.0387802124023,198.0387802124023,198.2453384399414,198.2453384399414,198.2453384399414,198.3486709594727,198.3486709594727,198.3486709594727,198.3486709594727,198.3486709594727,198.3486709594727,198.3486709594727,198.3486709594727,198.3486709594727,195.901985168457,196.0410766601562,196.0410766601562,196.1726837158203,196.1726837158203,196.3304824829102,196.3304824829102,196.4953918457031,196.4953918457031,196.6573715209961,196.6573715209961,196.8201751708984,196.9867172241211,196.9867172241211,197.1599655151367,197.3245620727539,197.5017242431641,197.6912384033203,197.6912384033203,197.8595809936523,197.8595809936523,198.0526123046875,198.2359313964844,198.2359313964844,198.3965454101562,198.3965454101562,198.4226379394531,198.4226379394531,198.4226379394531,198.4226379394531,198.4226379394531,198.4226379394531,195.9209823608398,196.0974044799805,196.0974044799805,196.2700271606445,196.2700271606445,196.4541168212891,196.4541168212891,196.6385040283203,196.8073654174805,196.8073654174805,196.9696426391602,196.9696426391602,197.1512603759766,197.1512603759766,197.3443374633789,197.5480194091797,197.5480194091797,197.7499694824219,197.7499694824219,197.9493103027344,198.1449661254883,198.1449661254883,198.3471145629883,198.4954147338867,198.4954147338867,198.4954147338867,198.4954147338867,198.4954147338867,198.4954147338867,198.4954147338867,198.4954147338867,198.4954147338867,196.1412200927734,196.1412200927734,196.3118438720703,196.3118438720703,196.4818267822266,196.4818267822266,196.6656112670898,196.8573303222656,197.0442428588867,197.0442428588867,197.2167816162109,197.3993759155273,197.3993759155273,197.5799407958984,197.5799407958984,197.768180847168,197.9086227416992,197.9086227416992,198.1004791259766,198.2936172485352,198.2936172485352,198.4592514038086,198.4592514038086,198.5670166015625,198.5670166015625,198.5670166015625,198.5670166015625,198.5670166015625,198.5670166015625,196.107795715332,196.107795715332,196.2787246704102,196.2787246704102,196.4505386352539,196.4505386352539,196.6307830810547,196.8155670166016,197.0050735473633,197.194694519043,197.194694519043,197.3926467895508,197.3926467895508,197.583625793457,197.777473449707,197.777473449707,197.777473449707,197.9680404663086,197.9680404663086,197.9680404663086,198.1592864990234,198.1592864990234,198.3495025634766,198.3495025634766,198.539909362793,198.539909362793,198.6374740600586,198.6374740600586,198.6374740600586,198.6374740600586,198.6374740600586,198.6374740600586,196.2142105102539,196.2142105102539,196.2142105102539,196.383415222168,196.5532302856445,196.5532302856445,196.7324981689453,196.9145126342773,196.9145126342773,197.104377746582,197.2994003295898,197.4948120117188,197.6872024536133,197.8791046142578,197.8791046142578,198.0718002319336,198.0718002319336,198.0718002319336,198.2619476318359,198.4236755371094,198.4236755371094,198.581428527832,198.581428527832,198.7067184448242,198.7067184448242,198.7067184448242,198.7067184448242,198.7067184448242,198.7067184448242,198.7067184448242,198.7067184448242,198.7067184448242,198.7067184448242,198.7067184448242,198.7067184448242,198.7067184448242,198.7067184448242,198.7067184448242,198.7067184448242,198.7067184448242,198.7067184448242,198.7067184448242,198.7067184448242,198.7067184448242,198.7067184448242,198.7067184448242,198.7067184448242,198.7067184448242,198.7067184448242,196.4068832397461,196.4068832397461,196.4068832397461,196.5843353271484,196.7174530029297,196.7174530029297,196.8841705322266,196.8841705322266,197.0590057373047,197.2498626708984,197.2498626708984,197.438720703125,197.438720703125,197.6309967041016,197.6309967041016,197.8224411010742,197.8224411010742,198.0204238891602,198.0204238891602,198.2218780517578,198.4114990234375,198.4114990234375,198.6061401367188,198.6061401367188,198.7747344970703,198.7747344970703,198.7747344970703,198.7747344970703,198.7747344970703,198.7747344970703,196.4932250976562,196.6712875366211,196.6712875366211,196.8467407226562,196.8467407226562,196.9999542236328,196.9999542236328,197.1829833984375,197.1829833984375,197.1829833984375,197.3723373413086,197.3723373413086,197.5772705078125,197.5772705078125,197.5772705078125,197.7976455688477,197.7976455688477,198.0229568481445,198.2540588378906,198.4865951538086,198.4865951538086,198.7204742431641,198.7204742431641,198.8417587280273,198.8417587280273,198.8417587280273,198.8417587280273,198.8417587280273,198.8417587280273,196.5358963012695,196.5358963012695,196.6922988891602,196.8640365600586,196.8640365600586,197.046760559082,197.238899230957,197.238899230957,197.4399337768555,197.6519775390625,197.8793869018555,197.8793869018555,198.0987167358398,198.0987167358398,198.322265625,198.322265625,198.322265625,198.5304336547852,198.7458953857422,198.7458953857422,198.9078369140625,198.9078369140625,198.9078369140625,198.9078369140625,198.9078369140625,198.9078369140625,198.9078369140625,198.9078369140625,198.9078369140625,196.7489929199219,196.9178924560547,196.9178924560547,197.0959930419922,197.0959930419922,197.285530090332,197.285530090332,197.4815444946289,197.4815444946289,197.6884613037109,197.6884613037109,197.9105911254883,197.9105911254883,198.1406021118164,198.1406021118164,198.3742904663086,198.608268737793,198.608268737793,198.608268737793,198.8404312133789,198.8404312133789,198.9727783203125,198.9727783203125,198.9727783203125,198.9727783203125,196.7573318481445,196.7573318481445,196.7573318481445,196.9227828979492,196.9227828979492,197.0970916748047,197.0970916748047,197.2809295654297,197.2809295654297,197.4713592529297,197.4713592529297,197.4713592529297,197.6783828735352,197.6783828735352,197.9011306762695,198.1364440917969,198.3695831298828,198.3695831298828,198.6009063720703,198.6009063720703,198.8179626464844,198.8179626464844,199.0367584228516,199.0367584228516,199.0367584228516,199.0367584228516,199.0367584228516,199.0367584228516,199.0367584228516,199.0367584228516,199.0367584228516,196.9457244873047,196.9457244873047,196.9457244873047,197.1154174804688,197.1154174804688,197.1154174804688,197.2938385009766,197.2938385009766,197.481086730957,197.481086730957,197.680305480957,197.680305480957,197.8935012817383,197.8935012817383,198.1230239868164,198.1230239868164,198.3560104370117,198.3560104370117,198.5870971679688,198.5870971679688,198.8197784423828,198.8197784423828,199.0738677978516,199.0738677978516,199.0995635986328,199.0995635986328,199.0995635986328,199.0995635986328,196.9952545166016,196.9952545166016,197.1636657714844,197.1636657714844,197.3393859863281,197.5274963378906,197.5274963378906,197.7243728637695,197.7243728637695,197.9326171875,197.9326171875,198.1581573486328,198.3944702148438,198.3944702148438,198.6274871826172,198.6274871826172,198.8594818115234,198.8594818115234,199.0905685424805,199.0905685424805,199.1614837646484,199.1614837646484,199.1614837646484,199.1614837646484,199.1614837646484,199.1614837646484,197.0670852661133,197.0670852661133,197.2325210571289,197.2325210571289,197.4051666259766,197.4051666259766,197.6103210449219,197.6103210449219,197.8052673339844,197.8052673339844,198.015495300293,198.015495300293,198.015495300293,198.2406234741211,198.2406234741211,198.476692199707,198.7126693725586,198.7126693725586,198.948127746582,198.948127746582,199.1830902099609,199.2223968505859,199.2223968505859,199.2223968505859,199.2223968505859,197.1915512084961,197.3615493774414,197.3615493774414,197.5396881103516,197.7272644042969,197.7272644042969,197.9118041992188,197.9118041992188,198.0602645874023,198.0602645874023,198.2789688110352,198.5150451660156,198.7516479492188,198.7516479492188,198.983283996582,198.983283996582,199.2156600952148,199.2822723388672,199.2822723388672,199.2822723388672,199.2822723388672,199.2822723388672,199.2822723388672,197.2759323120117,197.2759323120117,197.4449005126953,197.4449005126953,197.6227188110352,197.8114700317383,197.8114700317383,198.0117416381836,198.0117416381836,198.2318954467773,198.4651031494141,198.4651031494141,198.7039260864258,198.7039260864258,198.9391326904297,199.1749420166016,199.1749420166016,199.3412094116211,199.3412094116211,199.3412094116211,199.3412094116211,199.3412094116211,199.3412094116211,197.4502944946289,197.4502944946289,197.6240005493164,197.6240005493164,197.8122863769531,198.0083084106445,198.0083084106445,198.2199325561523,198.2199325561523,198.4471740722656,198.4471740722656,198.6861724853516,198.6861724853516,198.9224014282227,198.9224014282227,199.1567840576172,199.3991928100586,199.3991928100586,199.3991928100586,199.3991928100586,199.3991928100586,199.3991928100586,197.5097961425781,197.5097961425781,197.6823425292969,197.6823425292969,197.8661880493164,197.8661880493164,198.0571060180664,198.0571060180664,198.2654647827148,198.4889678955078,198.4889678955078,198.7258453369141,198.7258453369141,198.9631576538086,199.1977691650391,199.4265518188477,199.4265518188477,199.4563522338867,199.4563522338867,199.4563522338867,199.4563522338867,197.5676040649414,197.738899230957,197.738899230957,197.738899230957,197.9166641235352,197.9166641235352,198.1057891845703,198.1057891845703,198.2949752807617,198.2949752807617,198.2949752807617,198.5150604248047,198.5150604248047,198.7752304077148,198.7752304077148,199.0100936889648,199.2428970336914,199.2428970336914,199.2428970336914,199.4708862304688,199.5124206542969,199.5124206542969,199.5124206542969,199.5124206542969,199.5124206542969,199.5124206542969,197.6381225585938,197.8094940185547,197.9884796142578,197.9884796142578,198.1784057617188,198.1784057617188,198.3810195922852,198.3810195922852,198.6030578613281,198.6030578613281,198.840087890625,198.840087890625,199.0769577026367,199.0769577026367,199.3124618530273,199.3124618530273,199.5421447753906,199.5676498413086,199.5676498413086,199.5676498413086,199.5676498413086,199.5676498413086,199.5676498413086,197.7395248413086,197.7395248413086,197.9108123779297,197.9108123779297,198.092643737793,198.092643737793,198.2837371826172,198.2837371826172,198.4939193725586,198.4939193725586,198.7413177490234,198.7413177490234,198.9789123535156,198.9789123535156,199.2149505615234,199.2149505615234,199.2149505615234,199.4491882324219,199.4491882324219,199.6220321655273,199.6220321655273,199.6220321655273,199.6220321655273,199.6220321655273,199.6220321655273,199.6220321655273,199.6220321655273,199.6220321655273,199.6220321655273,199.6220321655273,199.6220321655273,199.6220321655273,199.6220321655273,199.6220321655273,199.6220321655273,197.7523345947266,197.7523345947266,197.8769378662109,197.8769378662109,198.0452194213867,198.0452194213867,198.2119064331055,198.3926467895508,198.3926467895508,198.5876007080078,198.781867980957,198.781867980957,198.9912109375,198.9912109375,199.2167510986328,199.4670867919922,199.4670867919922,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,199.6751022338867,197.8358688354492,197.8358688354492,197.8358688354492,197.8358688354492,197.8358688354492,197.8358688354492,198.009880065918,198.009880065918,198.2007827758789,198.2007827758789,198.4002990722656,198.6114501953125,198.6114501953125,198.8367080688477,199.0720901489258,199.2949371337891,199.2949371337891,199.4959869384766,199.4959869384766,199.7155685424805,199.9431533813477,200.1711730957031,200.3988342285156,200.3988342285156,200.6270904541016,200.6270904541016,200.8564376831055,201.0668334960938,201.0668334960938,201.2617874145508,201.2617874145508,201.4550552368164,201.6483764648438,201.6483764648438,201.8420867919922,201.8420867919922,202.035530090332,202.2290267944336,202.2290267944336,202.4222793579102,202.4222793579102,202.6157760620117,202.6157760620117,202.8044662475586,202.8044662475586,203.0149841308594,203.0149841308594,203.208869934082,203.208869934082,203.4022903442383,203.4022903442383,203.5765838623047,203.7255249023438,203.7255249023438,203.9001388549805,204.0777206420898,204.2633056640625,204.2633056640625,204.4456253051758,204.617431640625,204.617431640625,204.8013381958008,204.8013381958008,204.8013381958008,204.9870376586914,205.1705169677734,205.3467636108398,205.3467636108398,205.5096664428711,205.5096664428711,205.5096664428711,205.5096664428711,205.5096664428711,205.5096664428711,198.1845626831055,198.1845626831055,198.3897171020508,198.3897171020508,198.5870895385742,198.5870895385742,198.7864532470703,198.7864532470703,198.7864532470703,198.9944152832031,198.9944152832031,199.2183151245117,199.2183151245117,199.4462814331055,199.4462814331055,199.6628875732422,199.8890151977539,200.1276626586914,200.3606262207031,200.3606262207031,200.5989227294922,200.8373947143555,200.8373947143555,201.076416015625,201.076416015625,201.3153915405273,201.554084777832,201.554084777832,201.7921752929688,201.7921752929688,202.0303497314453,202.2689971923828,202.5070495605469,202.7446441650391,202.9820175170898,203.2193222045898,203.2193222045898,203.4562683105469,203.693489074707,203.693489074707,203.9314575195312,204.1675338745117,204.4020309448242,204.4020309448242,204.6395263671875,204.8761520385742,204.8761520385742,205.1120071411133,205.1120071411133,205.3613662719727,205.3613662719727,205.5789566040039,205.5789566040039,205.7195129394531,205.7195129394531,205.7195129394531,205.7195129394531,205.7195129394531,205.7195129394531,205.7195129394531,205.7195129394531,205.7195129394531,198.5270614624023,198.5270614624023,198.7063980102539,198.7063980102539,198.8985595703125,198.8985595703125,199.0999908447266,199.3058853149414,199.3058853149414,199.521728515625,199.7358093261719,199.9405670166016,199.9405670166016,200.1739730834961,200.1739730834961,200.4131317138672,200.4131317138672,200.648567199707,200.648567199707,200.8854827880859,200.8854827880859,200.8854827880859,201.1238250732422,201.1238250732422,201.3611755371094,201.3611755371094,201.5978927612305,201.5978927612305,201.8289947509766,201.8289947509766,202.063850402832,202.2994842529297,202.2994842529297,202.5354614257812,202.5354614257812,202.7716903686523,202.7716903686523,202.7716903686523,203.0324478149414,203.0324478149414,203.2693405151367,203.2693405151367,203.5069580078125,203.5069580078125,203.7442016601562,203.7442016601562,203.9812774658203,204.2179946899414,204.4545364379883,204.6912078857422,204.6912078857422,204.9289779663086,204.9289779663086,205.1660232543945,205.3997573852539,205.3997573852539,205.6251068115234,205.6251068115234,205.6251068115234,205.8510360717773,205.9260330200195,205.9260330200195,205.9260330200195,205.9260330200195,205.9260330200195,205.9260330200195,205.9260330200195,205.9260330200195,205.9260330200195,205.9260330200195,205.9260330200195,205.9260330200195,198.8812255859375,198.8812255859375,199.062255859375,199.2562866210938,199.455924987793,199.6599426269531,199.6599426269531,199.8697509765625,200.0789642333984,200.3014678955078,200.3014678955078,200.5411224365234,200.8017883300781,200.8017883300781,201.0356597900391,201.2711486816406,201.2711486816406,201.5064849853516,201.5064849853516,201.7403717041016,201.7403717041016,201.952522277832,201.952522277832,202.1872024536133,202.4198455810547,202.4198455810547,202.6372299194336,202.6372299194336,202.8665924072266,202.8665924072266,203.0556335449219,203.2735366821289,203.2735366821289,203.4816360473633,203.4816360473633,203.6996154785156,203.6996154785156,203.9205551147461,203.9205551147461,204.1367111206055,204.1367111206055,204.3627243041992,204.3627243041992,204.5840072631836,204.5840072631836,204.8075866699219,205.0375823974609,205.0375823974609,205.2590866088867,205.2590866088867,205.478889465332,205.478889465332,205.6694717407227,205.6694717407227,205.8655090332031,205.8655090332031,206.0890350341797,206.0890350341797,206.1292190551758,206.1292190551758,206.1292190551758,206.1292190551758,206.1292190551758,206.1292190551758,206.1292190551758,206.1292190551758,206.1292190551758,199.1644592285156,199.1644592285156,199.3401489257812,199.3401489257812,199.523307800293,199.523307800293,199.523307800293,199.7160263061523,199.9098968505859,199.9098968505859,199.9098968505859,200.0913238525391,200.0913238525391,200.0913238525391,200.2794494628906,200.2794494628906,200.2794494628906,200.4732055664062,200.6882705688477,200.6882705688477,200.9071578979492,201.0817031860352,201.0817031860352,201.3043899536133,201.3043899536133,201.3043899536133,201.5034255981445,201.7272796630859,201.7272796630859,201.9474868774414,201.9474868774414,202.1683807373047,202.399055480957,202.6211090087891,202.8484268188477,202.8484268188477,203.0791931152344,203.0791931152344,203.3136444091797,203.5475234985352,203.5475234985352,203.7807235717773,203.7807235717773,204.0123825073242,204.2439422607422,204.2439422607422,204.47802734375,204.47802734375,204.7126388549805,204.947639465332,204.947639465332,205.183479309082,205.183479309082,205.4129638671875,205.4129638671875,205.6509323120117,205.6509323120117,205.8783416748047,205.8783416748047,206.1001434326172,206.1001434326172,206.3224716186523,206.3224716186523,206.3290176391602,206.3290176391602,206.3290176391602,206.3290176391602,206.3290176391602,206.3290176391602,199.5689697265625,199.5689697265625,199.7556076049805,199.952018737793,200.148796081543,200.3487396240234,200.547248840332,200.547248840332,200.7779846191406,201.0154037475586,201.0154037475586,201.2528228759766,201.2528228759766,201.4876098632812,201.7201538085938,201.7201538085938,201.9535293579102,201.9535293579102,201.9535293579102,202.1863784790039,202.1863784790039,202.420280456543,202.420280456543,202.654296875,202.8891830444336,202.8891830444336,203.1229095458984,203.1229095458984,203.3570251464844,203.5910568237305,203.5910568237305,203.8232650756836,204.0578308105469,204.0578308105469,204.2913818359375,204.2913818359375,204.5258026123047,204.5258026123047,204.7605361938477,204.9957427978516,204.9957427978516,205.2309341430664,205.4662475585938,205.7017288208008,205.7017288208008,205.9614105224609,205.9614105224609,206.1854782104492,206.1854782104492,206.4094924926758,206.5257263183594,206.5257263183594,206.5257263183594,206.5257263183594,206.5257263183594,206.5257263183594,206.5257263183594,206.5257263183594,206.5257263183594,199.7790298461914,199.9498901367188,199.9498901367188,200.1391906738281,200.1391906738281,200.3341674804688,200.3341674804688,200.3341674804688,200.5281677246094,200.7242965698242,200.9463806152344,201.1827774047852,201.1827774047852,201.1827774047852,201.4207153320312,201.4207153320312,201.656135559082,201.8867721557617,201.8867721557617,202.118278503418,202.3488388061523,202.3488388061523,202.5823440551758,202.8152465820312,202.8152465820312,203.0443725585938,203.2768936157227,203.2768936157227,203.5080184936523,203.5080184936523,203.7393188476562,203.7393188476562,203.9714508056641,203.9714508056641,204.2276077270508,204.2276077270508,204.4603042602539,204.4603042602539,204.6931915283203,204.6931915283203,204.9271087646484,204.9271087646484,205.1606369018555,205.1606369018555,205.1606369018555,205.396125793457,205.396125793457,205.6316070556641,205.6316070556641,205.8669738769531,205.8669738769531,206.1031646728516,206.3305130004883,206.5552444458008,206.7192077636719,206.7192077636719,206.7192077636719,206.7192077636719,206.7192077636719,206.7192077636719,206.7192077636719,206.7192077636719,206.7192077636719,206.7192077636719,206.7192077636719,206.7192077636719,206.7192077636719,206.7192077636719,206.7192077636719,206.7192077636719,206.7192077636719,206.7192077636719,206.7192077636719,206.7192077636719,206.7192077636719,206.7192077636719,206.7192077636719,206.7192077636719,206.7192077636719,206.7192077636719,206.7192077636719,206.7192077636719,206.7192077636719,206.7192077636719,200.0613632202148,200.0613632202148,200.0613632202148,200.0613632202148,200.0613632202148,200.0613632202148,200.0613632202148,200.0613632202148,200.0613632202148,200.2265319824219,200.2265319824219,200.4174270629883,200.4174270629883,200.6121826171875,200.6121826171875,200.8064193725586,201.0045471191406,201.0045471191406,201.2307510375977,201.2307510375977,201.4683380126953,201.4683380126953,201.4683380126953,201.6948547363281,201.6948547363281,201.9215927124023,201.9215927124023,201.9215927124023,202.143440246582,202.3716659545898,202.3716659545898,202.6031875610352,202.834114074707,202.834114074707,203.060432434082,203.060432434082,203.060432434082,203.2916030883789,203.5281219482422,203.7637405395508,203.7637405395508,203.7637405395508,204.0002899169922,204.0002899169922,204.2366256713867,204.2366256713867,204.4582901000977,204.4582901000977,204.6970977783203,204.6970977783203,204.9350433349609,204.9350433349609,205.1730346679688,205.1730346679688,205.4111404418945,205.4111404418945,205.6734237670898,205.6734237670898,205.9119644165039,205.9119644165039,206.1514739990234,206.1514739990234,206.391471862793,206.391471862793,206.6299591064453,206.6299591064453,206.8680648803711,206.8680648803711,206.9094924926758,206.9094924926758,206.9094924926758,206.9094924926758,206.9094924926758,206.9094924926758,206.9094924926758,206.9094924926758,206.9094924926758,200.4448089599609,200.4448089599609,200.6327438354492,200.6327438354492,200.8275909423828,201.0185699462891,201.2129364013672,201.4390716552734,201.4390716552734,201.6780776977539,201.6780776977539,201.6780776977539,201.9136199951172,202.1471710205078,202.3793334960938,202.6120147705078,202.8437423706055,202.8437423706055,203.0759658813477,203.3104019165039,203.5439682006836,203.7792205810547,203.7792205810547,204.0122375488281,204.0122375488281,204.2442169189453,204.2442169189453,204.5009765625,204.5009765625,204.5009765625,204.7347412109375,204.9679183959961,204.9679183959961,205.2016830444336,205.4355239868164,205.4355239868164,205.6694793701172,205.6694793701172,205.9042510986328,205.9042510986328,205.9042510986328,206.1418838500977,206.3864517211914,206.3864517211914,206.3864517211914,206.6305313110352,206.6305313110352,206.8739776611328,207.0967788696289,207.0967788696289,207.0967788696289,207.0967788696289,207.0967788696289,207.0967788696289,207.0967788696289,207.0967788696289,207.0967788696289,207.0967788696289,207.0967788696289,207.0967788696289,200.7487411499023,200.7487411499023,200.8634872436523,200.8634872436523,200.9912796020508,200.9912796020508,201.1788177490234,201.1788177490234,201.1788177490234,201.3635940551758,201.3635940551758,201.3635940551758,201.5950927734375,201.8247604370117,201.8247604370117,202.0397186279297,202.0397186279297,202.2342834472656,202.2342834472656,202.3604736328125,202.3604736328125,202.3604736328125,202.4673156738281,202.4673156738281,202.5780639648438,202.5780639648438,202.5780639648438,202.6861343383789,202.6861343383789,202.8414306640625,203.0380020141602,203.0380020141602,203.0380020141602,203.2359008789062,210.9873352050781,210.9873352050781,210.9873352050781,210.9873352050781,210.9873352050781,210.9873352050781,210.9873352050781,210.9873352050781,210.9873352050781,210.9873352050781,210.9873352050781,210.9873352050781,210.9873352050781,210.9873352050781,210.9873352050781,210.9873352050781,210.9873352050781,210.9873352050781,210.9873352050781,210.9873352050781,210.9873352050781,210.9873352050781,210.9873352050781,210.9873352050781,210.9873352050781,210.9873352050781,218.6167297363281,218.6167297363281,218.6167297363281,218.6167373657227,218.6167373657227,218.6167373657227,218.6167373657227,218.6167373657227,218.6167373657227,218.6167373657227,218.6167373657227,218.6167373657227,218.6167373657227,218.6167373657227,218.6167373657227,218.6167373657227,218.6167373657227,218.6167373657227,218.6167373657227,218.6167373657227,218.6167373657227,218.6167373657227,218.6167373657227,218.6167373657227,218.6167373657227,218.6167373657227,218.6167373657227,218.6167373657227,218.6167373657227,233.8755264282227,233.8755264282227,233.8755264282227,233.8755264282227,233.8755264282227,233.8755264282227,233.8755264282227,233.8755264282227,233.8755264282227,233.8755264282227,233.8755264282227,233.8755264282227,233.8755264282227,233.8755264282227,233.8755264282227,233.8755264282227,233.8755264282227,233.8755264282227,233.8755264282227,233.8755264282227,241.5049438476562,241.5049438476562,241.5049438476562,241.5049438476562,241.5049438476562,241.5049438476562,241.5049438476562,241.5049438476562,241.5442657470703,241.5442657470703,241.5442657470703,241.5442657470703,241.5442657470703,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805,256.9001388549805],"meminc":[0,0,0,0,0,0,2.288818359375e-05,0,15.28221130371094,0,0,0,0,0,0,30.46574401855469,0,0,0,0,0,0,0,0,0,0,0,0,0,4.57763671875e-05,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-0.00030517578125,0,0,0,15.33483123779297,0,0,0.177734375,0,0.1932754516601562,0.1196212768554688,0,0,0.1638946533203125,0,0,0.1932449340820312,0.1784133911132812,0,0.2061996459960938,0,0.2163925170898438,0,0.1897964477539062,0.1927413940429688,0.1469802856445312,0,0.1832122802734375,0,0.1745986938476562,0,0.1816024780273438,0,0.2008132934570312,0,0.18682861328125,0,0.156005859375,0,0.1338653564453125,0,0,0,0,0,-2.955657958984375,0,0.1553192138671875,0,0.1684341430664062,0.2072982788085938,0,0.1800460815429688,0.1949234008789062,0,0.2002410888671875,0,0.217071533203125,0.20635986328125,0.1805648803710938,0.201904296875,0.2007675170898438,0,0,0.1854705810546875,0,0.19512939453125,0,0.1874618530273438,0.1657257080078125,0.1790313720703125,0,0,0,0,0,-2.956245422363281,0,0.1152877807617188,0,0.1205978393554688,0,0.110504150390625,0.1355361938476562,0.1724929809570312,0,0.1914443969726562,0.1896896362304688,0.1992950439453125,0,0.1902618408203125,0,0.178955078125,0,0.1330413818359375,0.1689605712890625,0,0.1691360473632812,0,0,0.1982803344726562,0,0.1852874755859375,0.1556854248046875,0,0.1825180053710938,0,0.17620849609375,0.070465087890625,0,0,-2.988479614257812,0.200042724609375,0,0.216033935546875,0,0,0.2191619873046875,0,0.2207489013671875,0,0.1925506591796875,0,0.166839599609375,0,0,0.16546630859375,0,0,0.17071533203125,0.1751251220703125,0.1890106201171875,0,0,0.1991424560546875,0.19232177734375,0.1990127563476562,0,0,0.18511962890625,0,0.1946182250976562,0,0,0.1767654418945312,0.0118408203125,0,-2.870925903320312,0.2065277099609375,0,0.2035446166992188,0,0.1919174194335938,0.180389404296875,0,0.2177886962890625,0,0.2178115844726562,0.2130355834960938,0.1352310180664062,0,0.128082275390625,0,0.193572998046875,0,0.1805572509765625,0,0.1705474853515625,0.2061843872070312,0,0.2402496337890625,0,0.2265853881835938,0.04346466064453125,0,0,-2.858757019042969,0,0.1903839111328125,0,0.1634445190429688,0.1975326538085938,0.1935348510742188,0,0.2012176513671875,0,0.1816864013671875,0.1885833740234375,0,0.1967620849609375,0.19207763671875,0,0.2005691528320312,0,0.139678955078125,0.1821441650390625,0.182037353515625,0,0.2113800048828125,0,0.2230300903320312,0,0.09793853759765625,0,0,-2.837936401367188,0,0.2024765014648438,0.22064208984375,0.215087890625,0,0,0.1914901733398438,0.225311279296875,0,0.17816162109375,0.2436141967773438,0,0.182861328125,0,0.214141845703125,0.2233428955078125,0,0.2224655151367188,0,0.2252044677734375,0.2264938354492188,0,0.1485519409179688,0,0,0,-2.632308959960938,0,0.2087936401367188,0,0.2193679809570312,0,0,0.2184371948242188,0.2117462158203125,0.177581787109375,0.1264114379882812,0,0.1233444213867188,0,0.170928955078125,0,0.1417922973632812,0,0.183929443359375,0,0.19281005859375,0,0.1918411254882812,0,0.1920852661132812,0,0.1921463012695312,0,0.1616363525390625,0,0,0,0,0,-2.642631530761719,0,0,0.1940689086914062,0,0.19952392578125,0,0,0.1976318359375,0.19232177734375,0.2155914306640625,0,0.1898651123046875,0,0.1930618286132812,0,0.185638427734375,0,0,0.19189453125,0.20062255859375,0,0.2029190063476562,0.1945343017578125,0,0.2013397216796875,0,0.1629486083984375,0,0,0,0,0,-2.709686279296875,0,0.1472625732421875,0,0.1758193969726562,0,0.2104873657226562,0.1862106323242188,0,0.1745986938476562,0,0.1614990234375,0,0.19036865234375,0,0.17620849609375,0.1793060302734375,0,0.1722793579101562,0.168670654296875,0,0,0.16473388671875,0.1684646606445312,0,0.1675872802734375,0,0.2057037353515625,0,0.1384124755859375,0,0,0,0,0,-2.579109191894531,0.180389404296875,0,0.1787033081054688,0.1570053100585938,0,0.1796646118164062,0,0.1812896728515625,0,0,0.1888580322265625,0.1824493408203125,0,0,0.1835479736328125,0,0,0.1942520141601562,0,0.2019729614257812,0,0.1841201782226562,0.194549560546875,0,0.1991653442382812,0,0.1495590209960938,0.1003265380859375,0,0,0,0,0,0,0,-2.512969970703125,0,0.128448486328125,0,0.1819839477539062,0,0.1881637573242188,0,0.2238998413085938,0,0.1487960815429688,0,0.1480712890625,0,0.1617660522460938,0.2004623413085938,0.2033767700195312,0.2130279541015625,0.2091217041015625,0,0.1951065063476562,0,0.2214736938476562,0,0.164764404296875,0,0,0,0,0,-2.452949523925781,0,0.1649932861328125,0,0.1643753051757812,0.1601028442382812,0,0.192291259765625,0,0,0.2027816772460938,0.1934051513671875,0,0.1865310668945312,0,0.1651611328125,0,0.1872634887695312,0,0.211761474609375,0,0.19775390625,0,0.1789093017578125,0.167633056640625,0,0.1542587280273438,0,0,0,0,0,-2.459808349609375,0.187286376953125,0,0.1916656494140625,0.201904296875,0,0.1995162963867188,0.1996917724609375,0.1785354614257812,0.1585922241210938,0,0.1993255615234375,0,0.179840087890625,0,0.1936187744140625,0.184356689453125,0,0.18218994140625,0,0.18231201171875,0,0.09403228759765625,0,0,-2.505523681640625,0,0.173370361328125,0,0.1641464233398438,0.1861801147460938,0.188385009765625,0,0.1836090087890625,0,0.1628189086914062,0,0.2008285522460938,0.2108688354492188,0.2027816772460938,0,0.2178421020507812,0.21478271484375,0.1955795288085938,0,0.1344833374023438,0.1417312622070312,0,0,0,0,0,-2.427627563476562,0.1884078979492188,0,0,0.1380767822265625,0,0.1816864013671875,0.1851119995117188,0,0.19158935546875,0,0.2046432495117188,0,0.2050933837890625,0,0.1991806030273438,0,0.1847610473632812,0,0.13568115234375,0,0.1142425537109375,0.1199798583984375,0,0.1272125244140625,0,0.1590194702148438,0,0.1636810302734375,0,0,0,0,0,-2.352241516113281,0,0.1845703125,0,0,0.2001800537109375,0,0.1877975463867188,0,0.1887893676757812,0,0.2097015380859375,0,0,0.2116012573242188,0,0.1991653442382812,0,0.1534347534179688,0,0.12469482421875,0,0.1323776245117188,0.1572494506835938,0.1639785766601562,0,0.1840744018554688,0.124237060546875,0,0,0,0,0,-2.333824157714844,0.1084442138671875,0.1805038452148438,0,0.159271240234375,0.1700820922851562,0,0.181793212890625,0,0.1846389770507812,0,0,0.174407958984375,0,0.1716537475585938,0,0.1693115234375,0,0.1631546020507812,0,0.1865310668945312,0,0.190521240234375,0.1481857299804688,0,0.1821060180664062,0,0.0316162109375,0,0,0,-2.318519592285156,0,0.1884536743164062,0.2088775634765625,0,0.2043685913085938,0,0.2034988403320312,0.2178192138671875,0.2019882202148438,0,0.1688308715820312,0,0.1624832153320312,0,0.1826553344726562,0,0.1814651489257812,0,0.1929855346679688,0,0.1846771240234375,0.0878448486328125,0,0,0,0,0,-2.1697998046875,0,0.1665420532226562,0,0.1853561401367188,0.1613922119140625,0,0.1949310302734375,0,0.201995849609375,0,0,0.2172164916992188,0.2228927612304688,0,0,0.2262191772460938,0.2329788208007812,0,0.249725341796875,0,0,0.1767349243164062,0,0,0,-2.220329284667969,0.1288681030273438,0,0.1831512451171875,0,0.1512527465820312,0,0.175323486328125,0,0,0.2098922729492188,0,0.2145614624023438,0,0.22308349609375,0.2143783569335938,0,0.2181015014648438,0,0.2288436889648438,0,0.2316055297851562,0.1065292358398438,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2.199592590332031,0,0.1556777954101562,0,0.17388916015625,0,0.1833724975585938,0,0,0.19317626953125,0,0.1903915405273438,0.19921875,0,0.1953201293945312,0.139312744140625,0,0.1842193603515625,0,0,0.2006149291992188,0.2038497924804688,0,0.2328414916992188,0.01152801513671875,0,-2.1318359375,0,0.182830810546875,0,0.178863525390625,0.1863632202148438,0.201263427734375,0.2127838134765625,0.2233963012695312,0,0.2209701538085938,0,0.217071533203125,0.2189483642578125,0,0,0.2244491577148438,0,0.1280746459960938,0,0,0,0,0,-2.003570556640625,0,0.1805877685546875,0,0.1906814575195312,0.1974411010742188,0,0,0.1995086669921875,0,0.2042922973632812,0,0.2077255249023438,0,0.2173080444335938,0.1948623657226562,0,0.1967086791992188,0,0.2046432495117188,0,0.07192230224609375,0,0,0,0,0,-2.110374450683594,0.1070022583007812,0,0.167083740234375,0.1822509765625,0,0.207061767578125,0.196533203125,0,0.2041397094726562,0,0.2160110473632812,0,0.2242660522460938,0.2258377075195312,0.2205810546875,0.21575927734375,0,0.00496673583984375,0,0,-2.029197692871094,0.1706619262695312,0,0.1658401489257812,0,0.1827774047851562,0.1937789916992188,0.1865997314453125,0.1208343505859375,0,0.1816787719726562,0,0.1682357788085938,0,0.1838531494140625,0.1662750244140625,0.1905136108398438,0,0.1782913208007812,0,0,0,0,0,-2.007179260253906,0,0,0.1588211059570312,0,0.1699981689453125,0,0.1879348754882812,0,0.1928482055664062,0.2112274169921875,0.211395263671875,0.241729736328125,0,0.22601318359375,0.2191238403320312,0.2150192260742188,0,0.03218841552734375,0,-1.999649047851562,0.1688079833984375,0,0.1760101318359375,0,0.1815032958984375,0.2031631469726562,0,0,0.2164535522460938,0.1683883666992188,0,0.2070770263671875,0.2120819091796875,0.2149810791015625,0,0,0.2157135009765625,0.0936737060546875,0,0,0,0,0,-1.817962646484375,0.179290771484375,0.18670654296875,0.1929855346679688,0,0,0.1480789184570312,0,0.1730804443359375,0.20770263671875,0,0.214080810546875,0,0.2118606567382812,0.2013702392578125,0,0.1600570678710938,0,0,0,0,0,-1.89306640625,0,0.1798553466796875,0,0.1724929809570312,0,0.1867752075195312,0.1953125,0.2296218872070312,0,0.2153091430664062,0,0.2237319946289062,0.2230987548828125,0.230194091796875,0,0.092987060546875,0,0,-1.934539794921875,0,0.174407958984375,0,0.1800384521484375,0,0.1795120239257812,0,0.1939163208007812,0,0.195159912109375,0,0.1940536499023438,0,0,0.2013778686523438,0.1839675903320312,0,0,0.2091827392578125,0,0.2188491821289062,0.05947113037109375,0,0,-1.880928039550781,0,0.1830291748046875,0,0.1837234497070312,0,0.207244873046875,0,0.1903610229492188,0,0.1825637817382812,0.1730270385742188,0.185302734375,0.1783981323242188,0,0.177215576171875,0.1921463012695312,0.082489013671875,0,0,0,0,0,-1.715988159179688,0.1795120239257812,0.188568115234375,0.19970703125,0,0.1791915893554688,0,0.1896896362304688,0,0.2073898315429688,0,0.2172164916992188,0.2235565185546875,0,0.1847763061523438,0,0,0,0,0,-1.735816955566406,0,0.182952880859375,0,0.1890106201171875,0,0.1953506469726562,0.1992721557617188,0,0.1962509155273438,0.19561767578125,0,0,0.2066802978515625,0.2184829711914062,0,0.2049636840820312,0,0,0,0,0,-1.789306640625,0.148712158203125,0,0.1828460693359375,0.1439056396484375,0,0.2011489868164062,0.2130279541015625,0,0.2257843017578125,0,0.2338638305664062,0.2327346801757812,0,0.2312545776367188,0,0.0279693603515625,0,-1.730995178222656,0,0.1812820434570312,0.1837081909179688,0,0.1964950561523438,0,0.2139053344726562,0,0.2255096435546875,0,0.2198562622070312,0,0.2047576904296875,0,0.2228546142578125,0.1337356567382812,0,0,0,0,0,-1.67401123046875,0,0.1264724731445312,0.09759521484375,0,0.09828948974609375,0,0.09969329833984375,0.1742019653320312,0,0.1789093017578125,0.1744842529296875,0,0.198974609375,0.211639404296875,0,0.1953582763671875,0.1365127563476562,0,0.0321044921875,0,0,0,0,0,-1.575035095214844,0,0.1719512939453125,0,0.1757888793945312,0.1935501098632812,0,0.1785125732421875,0,0.2003402709960938,0.1987075805664062,0,0.1933059692382812,0.2047805786132812,0.1075820922851562,0,0,0,0,0,-1.570808410644531,0,0.1675796508789062,0,0.190765380859375,0,0,0.1827163696289062,0.1887435913085938,0,0.181640625,0,0.150909423828125,0,0,0.1041030883789062,0.1040573120117188,0.1073455810546875,0,0.1032257080078125,0.1166229248046875,0,0.021759033203125,0,0,0,-1.573371887207031,0.184356689453125,0,0.18817138671875,0.2021484375,0.2140731811523438,0,0.20654296875,0.1966400146484375,0.161102294921875,0,0.1967086791992188,0,0.071441650390625,0,0,0,0,0,-1.631736755371094,0.1804885864257812,0,0.1816329956054688,0,0.1890487670898438,0.1992950439453125,0,0.2006988525390625,0,0.2053756713867188,0.19488525390625,0.2015151977539062,0.125946044921875,0,0,0,0,0,-1.492195129394531,0,0.18267822265625,0,0.1908721923828125,0.193267822265625,0,0.1961822509765625,0,0.1499862670898438,0,0.1894912719726562,0.2132644653320312,0,0.1991729736328125,0.0236358642578125,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.595420837402344,0,0,0,0,0,0.1026458740234375,0,0.18182373046875,0,0,0.193389892578125,0,0.1965713500976562,0.2014236450195312,0.215484619140625,0,0.2110443115234375,0,0.2028656005859375,0,0.236053466796875,0.2357711791992188,0,0.2367630004882812,0,0.249725341796875,0.2292327880859375,0.2091064453125,0.187530517578125,0,0.1923675537109375,0,0.1755905151367188,0.1608123779296875,0.1785736083984375,0,0.18115234375,0.1915435791015625,0,0.1772308349609375,0.1805648803710938,0,0.174285888671875,0,0.1556243896484375,0,0,0,0,0,-4.600601196289062,0,0.1919174194335938,0,0.2027435302734375,0.2162094116210938,0.2071456909179688,0,0.2211227416992188,0,0,0.201141357421875,0.2142410278320312,0,0.2160186767578125,0,0.2235565185546875,0,0.24456787109375,0,0.1955337524414062,0.2187728881835938,0,0,0.2137527465820312,0,0.2223587036132812,0.208282470703125,0.2059555053710938,0,0.2141265869140625,0,0.2251510620117188,0.2340774536132812,0,0.2341384887695312,0.2273178100585938,0,0.1953201293945312,0,0,0,0,0,0,0,-4.515121459960938,0,0.2014312744140625,0,0.2109909057617188,0.2261581420898438,0,0.2272720336914062,0.236846923828125,0,0.22406005859375,0.2351760864257812,0,0.238433837890625,0,0.2386703491210938,0,0,0.2347869873046875,0,0.2325515747070312,0.2191390991210938,0,0.2282791137695312,0,0,0.1821517944335938,0,0.2122955322265625,0,0.1995315551757812,0,0.2224044799804688,0.2334671020507812,0,0.2363662719726562,0.226959228515625,0.1789169311523438,0,0,0,-4.421302795410156,0.1980743408203125,0,0.1882553100585938,0.1918182373046875,0,0.2027206420898438,0.20599365234375,0,0.214996337890625,0.2401351928710938,0,0.2356796264648438,0,0.2360153198242188,0,0.2352981567382812,0,0.233978271484375,0.2361679077148438,0,0.2350921630859375,0,0.2355194091796875,0,0.2354736328125,0,0.2343368530273438,0.2326431274414062,0,0.2329940795898438,0,0.2295074462890625,0.22344970703125,0.07171630859375,0,0,0,0,0,-4.312248229980469,0.1998672485351562,0,0.1977767944335938,0,0.193572998046875,0,0.1847381591796875,0,0.1809158325195312,0.210174560546875,0.2411880493164062,0,0.24053955078125,0.2146835327148438,0.2351303100585938,0,0.2338409423828125,0.2337875366210938,0,0.2329788208007812,0,0.2223434448242188,0,0.227752685546875,0.224334716796875,0.1866455078125,0,0.2269439697265625,0.2368240356445312,0.212677001953125,0.1020278930664062,0,0,0,-4.258644104003906,0.1977615356445312,0,0.1915359497070312,0.1969833374023438,0,0.1895675659179688,0,0.1882400512695312,0,0.2100830078125,0,0.2349700927734375,0.2366485595703125,0,0.2377777099609375,0,0.2354812622070312,0.2325057983398438,0,0.2339553833007812,0,0.2303543090820312,0,0.237274169921875,0,0.1896591186523438,0,0.2062530517578125,0.2339859008789062,0.23065185546875,0,0.2292022705078125,0.22137451171875,0,0.018951416015625,0,0,0,0,0,-4.119041442871094,0,0,0.1986312866210938,0,0.195831298828125,0,0.1679153442382812,0,0.1783523559570312,0.204254150390625,0,0.1990966796875,0.225860595703125,0,0,0.2389755249023438,0,0.2593536376953125,0.2364120483398438,0,0.2285995483398438,0,0.2335891723632812,0,0,0.23370361328125,0.2350311279296875,0,0.2344436645507812,0.235260009765625,0,0.23529052734375,0,0.2190170288085938,0,0.1809616088867188,0.100860595703125,0,0,0,0,0,0,0,0,0,0,0,-4.065666198730469,0,0.2040939331054688,0,0.2114334106445312,0.207061767578125,0,0.2384719848632812,0,0.2142562866210938,0,0.191162109375,0.2588119506835938,0,0.1815872192382812,0,0,0.148956298828125,0,0.2137298583984375,0,0.2281417846679688,0,0.2335357666015625,0,0.2357101440429688,0,0.2365646362304688,0.2347793579101562,0,0.2358474731445312,0.2363357543945312,0,0,0.2316513061523438,0,0.2247238159179688,0,0.01932525634765625,0,0,0,0,0,0,0,-3.953750610351562,0,0.1998443603515625,0,0.1672439575195312,0,0.1928634643554688,0,0.1662139892578125,0.14178466796875,0.143707275390625,0,0.2021560668945312,0,0.163543701171875,0,0.1396331787109375,0,0.1973953247070312,0,0.2388458251953125,0,0.2321624755859375,0,0.235626220703125,0,0.2352676391601562,0.2354278564453125,0.2354507446289062,0,0,0.2353057861328125,0,0.2365341186523438,0,0.209503173828125,0.2237625122070312,0,0.04000091552734375,0,0,0,0,0,-3.899955749511719,0,0.1993637084960938,0,0.20440673828125,0,0.2462158203125,0,0,0.2403793334960938,0,0.240386962890625,0,0.2409286499023438,0,0.2408218383789062,0.2491302490234375,0,0.2455215454101562,0,0.244232177734375,0,0.2458572387695312,0,0.2455215454101562,0.2454452514648438,0,0.164764404296875,0,0.1202545166015625,0.1208724975585938,0,0.1154937744140625,0,0.1077651977539062,0.1862640380859375,0,0.113006591796875,0,0,0,-3.960563659667969,0.2066574096679688,0,0.1832504272460938,0.1840744018554688,0,0.2110443115234375,0,0.2284088134765625,0.2365875244140625,0,0.23724365234375,0.2349624633789062,0,0.23468017578125,0,0.2340774536132812,0,0.2341690063476562,0.23876953125,0.2401809692382812,0,0.2439346313476562,0.2410354614257812,0,0.2444610595703125,0,0.2381210327148438,0,0.203582763671875,0,0,0,0,0,-3.921371459960938,0,0.1936569213867188,0,0.1899337768554688,0.1942520141601562,0.2262954711914062,0.2377853393554688,0,0.2571258544921875,0.2366485595703125,0,0.2352142333984375,0.2375411987304688,0,0.240753173828125,0,0,0.2314529418945312,0,0,0.233489990234375,0.2180252075195312,0,0.2328872680664062,0,0.2345428466796875,0.2440872192382812,0,0.2301101684570312,0,0.1605224609375,0,0,0,0,0,-3.839088439941406,0,0,0.193878173828125,0,0.1874465942382812,0,0.2050094604492188,0.2281494140625,0.2377166748046875,0,0.2378921508789062,0,0.2367706298828125,0.2366790771484375,0,0.2388076782226562,0,0.2430343627929688,0,0.24273681640625,0.2435684204101562,0.268798828125,0,0.2432327270507812,0,0.2430343627929688,0.2400436401367188,0,0.2233428955078125,0,0,0,0,0,0,0,0,-3.631706237792969,0.1854248046875,0,0.2000656127929688,0,0.2170333862304688,0,0.23004150390625,0,0.2367935180664062,0.2367095947265625,0,0.239105224609375,0,0.2391738891601562,0,0.2390670776367188,0.244964599609375,0.2447357177734375,0,0.246246337890625,0.246368408203125,0,0.2463607788085938,0,0.2433929443359375,0,0.2350692749023438,0,0.01041412353515625,0,0,0,0,0,-3.561439514160156,0,0.1852645874023438,0,0.2060470581054688,0,0.22406005859375,0,0.2354888916015625,0,0.2355422973632812,0.238250732421875,0,0,0.2396774291992188,0.242156982421875,0.24462890625,0,0.2453765869140625,0.2470550537109375,0,0.2472610473632812,0.2462921142578125,0,0.2469635009765625,0,0.2382431030273438,0,0.146697998046875,0,0,0,0,0,-3.630966186523438,0.1881103515625,0,0.1894683837890625,0.2134780883789062,0,0.2281036376953125,0,0.2330169677734375,0,0.237060546875,0,0.238677978515625,0,0.2330551147460938,0.245452880859375,0,0,0.2407684326171875,0,0.2633743286132812,0,0.2467041015625,0,0.2458267211914062,0,0.2466201782226562,0.2429885864257812,0,0,0.23516845703125,0,0.00878143310546875,0,0,0,-3.466499328613281,0,0.1820220947265625,0,0.205657958984375,0.2175216674804688,0,0.2127151489257812,0,0,0.1995010375976562,0,0.2121658325195312,0,0.2362213134765625,0,0.2367095947265625,0,0.2436752319335938,0,0.2402267456054688,0,0.2421951293945312,0,0.2424850463867188,0,0.243896484375,0.2428741455078125,0,0.2367019653320312,0.1760711669921875,0,0,0,-3.528694152832031,0.1854782104492188,0,0.1833038330078125,0.2051315307617188,0.2082977294921875,0,0.215362548828125,0,0.2331466674804688,0,0.237945556640625,0,0.2393722534179688,0,0.23974609375,0,0.2385787963867188,0,0.2432785034179688,0.2468414306640625,0,0.2478256225585938,0,0.24542236328125,0.2416458129882812,0,0.2197036743164062,0,0,0,0,0,-3.520668029785156,0,0.1861648559570312,0,0,0.1858062744140625,0,0.2019577026367188,0.2132034301757812,0,0.2242813110351562,0,0.2204437255859375,0.2368240356445312,0.2628631591796875,0,0.2387237548828125,0.237762451171875,0.2303314208984375,0.2371063232421875,0,0.2464218139648438,0.24652099609375,0.24176025390625,0,0.2112655639648438,0,0,0,0,0,-3.4619140625,0,0.1824951171875,0.184967041015625,0,0.1980972290039062,0,0.2002182006835938,0,0.2159042358398438,0.231048583984375,0,0.2377777099609375,0,0,0.239044189453125,0.239532470703125,0.230224609375,0.2351226806640625,0,0.2223052978515625,0,0,0.2317657470703125,0,0.1507492065429688,0,0.1465072631835938,0,0.126190185546875,0,0,0.13446044921875,0.1545486450195312,0,0,0,0,0,-3.397598266601562,0,0,0.1835861206054688,0,0.1824264526367188,0,0.1833724975585938,0.1828460693359375,0.1940994262695312,0,0.2005691528320312,0,0.2035980224609375,0.2039031982421875,0,0.2052383422851562,0,0.2039031982421875,0,0.2035675048828125,0,0.1944351196289062,0,0,0.1940536499023438,0,0.2135772705078125,0,0,0.194427490234375,0,0.1823196411132812,0,0.1133651733398438,0,0,0.113677978515625,0,0.1421585083007812,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-3.356559753417969,0,0,0,0,0,0.1360397338867188,0.16845703125,0.171966552734375,0.1764602661132812,0,0.1822052001953125,0,0.1928024291992188,0,0.2112960815429688,0,0.2268753051757812,0,0.2161636352539062,0,0.1960220336914062,0,0.22357177734375,0,0.2489852905273438,0,0.2181777954101562,0.2342529296875,0,0.2377166748046875,0,0.235687255859375,0,0.175628662109375,0,0,0,0,0,-3.2769775390625,0.1788101196289062,0,0.1855850219726562,0,0.196075439453125,0,0.2101516723632812,0,0.2225723266601562,0,0.23333740234375,0,0,0.2339096069335938,0,0.2321319580078125,0,0.2323760986328125,0,0.2349319458007812,0,0.2375946044921875,0,0.2388763427734375,0,0.24542236328125,0,0.2458419799804688,0,0.239013671875,0,0.00473785400390625,0,0,0,0,0,-3.099014282226562,0.1824188232421875,0,0.1902694702148438,0,0.203216552734375,0.2196426391601562,0,0.2325210571289062,0,0.2342987060546875,0.2329788208007812,0,0.2302093505859375,0,0.2320022583007812,0,0,0.2396774291992188,0,0.2371292114257812,0,0.2447967529296875,0.246490478515625,0,0.2433929443359375,0,0,0.02285003662109375,0,0,0,0,0,-3.068572998046875,0,0.18133544921875,0.1851043701171875,0,0.197784423828125,0,0.2133102416992188,0.2282943725585938,0,0.2335586547851562,0,0.2553176879882812,0.2306442260742188,0.2315597534179688,0,0.232330322265625,0,0.2356643676757812,0,0.2432708740234375,0,0.244049072265625,0,0,0.2418212890625,0,0.00594329833984375,0,0,0,0,0,-3.004737854003906,0,0.181549072265625,0,0.1841201782226562,0,0.2015914916992188,0,0.2173995971679688,0,0.2323684692382812,0,0,0.2340469360351562,0.2336273193359375,0.2321014404296875,0,0.2320404052734375,0.2359771728515625,0,0.2374725341796875,0.2446975708007812,0.245208740234375,0.1824417114257812,0,0,0,0,0,-3.0673828125,0.1772994995117188,0,0,0.181640625,0,0.1909255981445312,0,0.2060623168945312,0.2225723266601562,0,0.232269287109375,0.2320404052734375,0,0.2311477661132812,0,0.2318038940429688,0,0.230712890625,0,0.2358169555664062,0.2356719970703125,0,0.242919921875,0.2430419921875,0.0619049072265625,0,0,0,0,0,-2.953857421875,0.1795806884765625,0.1833267211914062,0,0.1993179321289062,0,0.2160263061523438,0,0.2306900024414062,0.143890380859375,0.1341323852539062,0,0.1203536987304688,0,0.1177444458007812,0,0.1177444458007812,0,0.1302719116210938,0.1877517700195312,0,0.1865463256835938,0.2250595092773438,0.2174301147460938,0,0.1892776489257812,0.1804580688476562,0,0.08129119873046875,0,0,0,-2.9156494140625,0,0.1720123291015625,0,0.1413192749023438,0.1864547729492188,0,0.1979293823242188,0,0.2051162719726562,0,0,0.2258377075195312,0,0.229736328125,0,0.20050048828125,0,0.1893768310546875,0,0.1684494018554688,0,0.1735153198242188,0.2323989868164062,0,0.209136962890625,0,0.195281982421875,0,0.195465087890625,0,0.07880401611328125,0,0,0,0,0,0,0,0,-2.788658142089844,0,0.177032470703125,0,0.1816558837890625,0,0.1851654052734375,0.1880340576171875,0.19866943359375,0,0,0.1796798706054688,0,0,0.1865386962890625,0,0.2112808227539062,0,0,0.2225112915039062,0,0.2304458618164062,0.2321243286132812,0,0.2200088500976562,0,0.194580078125,0.16741943359375,0,0.09774017333984375,0,0,0,0,0,-2.851577758789062,0,0.1633834838867188,0,0.1478958129882812,0,0.1603851318359375,0,0.1163406372070312,0,0.1474456787109375,0,0.1636962890625,0,0.1588363647460938,0.172088623046875,0,0.1966400146484375,0.2109756469726562,0,0.1892318725585938,0.2098007202148438,0.1933746337890625,0,0.22833251953125,0,0,0.1817703247070312,0,0.2175750732421875,0.07669830322265625,0,0,0,0,0,-2.826324462890625,0,0.1515960693359375,0,0.1334075927734375,0.15277099609375,0,0.1677703857421875,0,0.1956405639648438,0.2123489379882812,0,0,0.2131805419921875,0,0.204498291015625,0.1919479370117188,0,0.2278976440429688,0,0.204620361328125,0,0.157562255859375,0,0.1658782958984375,0,0.2016067504882812,0,0.2320175170898438,0.09520721435546875,0,0,0,-2.762001037597656,0.156982421875,0.1184463500976562,0,0.1571273803710938,0.1237106323242188,0.172271728515625,0,0.200714111328125,0.1356735229492188,0,0,0.1942901611328125,0.191497802734375,0.1176834106445312,0,0.1603927612304688,0.1352386474609375,0,0.1584396362304688,0,0.1819686889648438,0.1868972778320312,0,0.2105789184570312,0,0.213775634765625,0,0.02649688720703125,0,0,0,-2.714179992675781,0,0.1251220703125,0,0.09844207763671875,0,0,0.09954071044921875,0.099639892578125,0,0.1033477783203125,0,0,0.102996826171875,0,0.1632003784179688,0,0.2086257934570312,0,0.2126998901367188,0,0.128448486328125,0,0.2011260986328125,0.2127838134765625,0,0.14532470703125,0,0,0.11328125,0.1556930541992188,0,0.114654541015625,0.144195556640625,0,0,0.1239013671875,0,0.119140625,0,0,0.121063232421875,0,0,0,0,0,0,0,0,-2.645042419433594,0,0.1775436401367188,0,0.166900634765625,0,0,0.1887893676757812,0,0.2036209106445312,0.2032089233398438,0.1889801025390625,0.20684814453125,0,0,0.2102584838867188,0.20751953125,0.2140960693359375,0,0.2140960693359375,0,0.2139053344726562,0,0,0.1972808837890625,0.1296157836914062,0,0,0,0,0,0,0,0,-2.539321899414062,0,0.1731719970703125,0,0.1791229248046875,0.1847763061523438,0,0.1839675903320312,0,0.188934326171875,0,0.202728271484375,0.2052536010742188,0,0.2134323120117188,0.1754226684570312,0,0.1335906982421875,0.166107177734375,0.129852294921875,0,0.194427490234375,0.1102676391601562,0.110015869140625,0,0.06470489501953125,0,0,0,0,0,0,0,0,-2.505722045898438,0,0.1917953491210938,0.1723861694335938,0.16998291015625,0,0.171661376953125,0,0.1715545654296875,0,0.1771316528320312,0.1699905395507812,0,0,0.179656982421875,0.1779327392578125,0,0.1689987182617188,0,0.1759414672851562,0.1832427978515625,0,0.1607513427734375,0,0.2065582275390625,0,0,0.10333251953125,0,0,0,0,0,0,0,0,-2.446685791015625,0.1390914916992188,0,0.1316070556640625,0,0.1577987670898438,0,0.1649093627929688,0,0.1619796752929688,0,0.1628036499023438,0.1665420532226562,0,0.173248291015625,0.1645965576171875,0.1771621704101562,0.18951416015625,0,0.1683425903320312,0,0.1930313110351562,0.183319091796875,0,0.160614013671875,0,0.026092529296875,0,0,0,0,0,-2.501655578613281,0.176422119140625,0,0.1726226806640625,0,0.1840896606445312,0,0.18438720703125,0.1688613891601562,0,0.1622772216796875,0,0.1816177368164062,0,0.1930770874023438,0.2036819458007812,0,0.2019500732421875,0,0.1993408203125,0.1956558227539062,0,0.2021484375,0.1483001708984375,0,0,0,0,0,0,0,0,-2.354194641113281,0,0.170623779296875,0,0.16998291015625,0,0.1837844848632812,0.1917190551757812,0.1869125366210938,0,0.1725387573242188,0.1825942993164062,0,0.1805648803710938,0,0.1882400512695312,0.14044189453125,0,0.1918563842773438,0.1931381225585938,0,0.1656341552734375,0,0.1077651977539062,0,0,0,0,0,-2.459220886230469,0,0.170928955078125,0,0.17181396484375,0,0.1802444458007812,0.184783935546875,0.1895065307617188,0.1896209716796875,0,0.1979522705078125,0,0.19097900390625,0.19384765625,0,0,0.1905670166015625,0,0,0.1912460327148438,0,0.190216064453125,0,0.1904067993164062,0,0.097564697265625,0,0,0,0,0,-2.423263549804688,0,0,0.1692047119140625,0.1698150634765625,0,0.1792678833007812,0.1820144653320312,0,0.1898651123046875,0.1950225830078125,0.1954116821289062,0.1923904418945312,0.1919021606445312,0,0.1926956176757812,0,0,0.1901473999023438,0.1617279052734375,0,0.1577529907226562,0,0.1252899169921875,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2.299835205078125,0,0,0.1774520874023438,0.13311767578125,0,0.166717529296875,0,0.174835205078125,0.19085693359375,0,0.1888580322265625,0,0.1922760009765625,0,0.1914443969726562,0,0.1979827880859375,0,0.2014541625976562,0.1896209716796875,0,0.19464111328125,0,0.1685943603515625,0,0,0,0,0,-2.281509399414062,0.1780624389648438,0,0.1754531860351562,0,0.1532135009765625,0,0.1830291748046875,0,0,0.1893539428710938,0,0.2049331665039062,0,0,0.2203750610351562,0,0.225311279296875,0.2311019897460938,0.2325363159179688,0,0.2338790893554688,0,0.1212844848632812,0,0,0,0,0,-2.305862426757812,0,0.156402587890625,0.1717376708984375,0,0.1827239990234375,0.192138671875,0,0.2010345458984375,0.2120437622070312,0.2274093627929688,0,0.219329833984375,0,0.2235488891601562,0,0,0.2081680297851562,0.2154617309570312,0,0.1619415283203125,0,0,0,0,0,0,0,0,-2.158843994140625,0.1688995361328125,0,0.1781005859375,0,0.1895370483398438,0,0.196014404296875,0,0.2069168090820312,0,0.2221298217773438,0,0.230010986328125,0,0.2336883544921875,0.233978271484375,0,0,0.2321624755859375,0,0.1323471069335938,0,0,0,-2.215446472167969,0,0,0.1654510498046875,0,0.1743087768554688,0,0.183837890625,0,0.1904296875,0,0,0.2070236206054688,0,0.222747802734375,0.2353134155273438,0.2331390380859375,0,0.2313232421875,0,0.2170562744140625,0,0.2187957763671875,0,0,0,0,0,0,0,0,-2.091033935546875,0,0,0.1696929931640625,0,0,0.1784210205078125,0,0.1872482299804688,0,0.19921875,0,0.21319580078125,0,0.229522705078125,0,0.2329864501953125,0,0.2310867309570312,0,0.2326812744140625,0,0.25408935546875,0,0.02569580078125,0,0,0,-2.10430908203125,0,0.1684112548828125,0,0.17572021484375,0.1881103515625,0,0.1968765258789062,0,0.2082443237304688,0,0.2255401611328125,0.2363128662109375,0,0.2330169677734375,0,0.23199462890625,0,0.2310867309570312,0,0.07091522216796875,0,0,0,0,0,-2.094398498535156,0,0.165435791015625,0,0.1726455688476562,0,0.2051544189453125,0,0.1949462890625,0,0.2102279663085938,0,0,0.225128173828125,0,0.2360687255859375,0.2359771728515625,0,0.2354583740234375,0,0.2349624633789062,0.039306640625,0,0,0,-2.030845642089844,0.1699981689453125,0,0.1781387329101562,0.1875762939453125,0,0.184539794921875,0,0.1484603881835938,0,0.2187042236328125,0.2360763549804688,0.236602783203125,0,0.2316360473632812,0,0.2323760986328125,0.06661224365234375,0,0,0,0,0,-2.006340026855469,0,0.1689682006835938,0,0.1778182983398438,0.188751220703125,0,0.2002716064453125,0,0.22015380859375,0.2332077026367188,0,0.2388229370117188,0,0.2352066040039062,0.235809326171875,0,0.1662673950195312,0,0,0,0,0,-1.890914916992188,0,0.1737060546875,0,0.1882858276367188,0.1960220336914062,0,0.2116241455078125,0,0.2272415161132812,0,0.2389984130859375,0,0.2362289428710938,0,0.2343826293945312,0.2424087524414062,0,0,0,0,0,-1.889396667480469,0,0.17254638671875,0,0.1838455200195312,0,0.19091796875,0,0.2083587646484375,0.2235031127929688,0,0.23687744140625,0,0.2373123168945312,0.2346115112304688,0.2287826538085938,0,0.0298004150390625,0,0,0,-1.888748168945312,0.171295166015625,0,0,0.177764892578125,0,0.1891250610351562,0,0.1891860961914062,0,0,0.2200851440429688,0,0.2601699829101562,0,0.23486328125,0.2328033447265625,0,0,0.2279891967773438,0.041534423828125,0,0,0,0,0,-1.874298095703125,0.1713714599609375,0.178985595703125,0,0.1899261474609375,0,0.2026138305664062,0,0.2220382690429688,0,0.237030029296875,0,0.2368698120117188,0,0.235504150390625,0,0.2296829223632812,0.02550506591796875,0,0,0,0,0,-1.828125,0,0.1712875366210938,0,0.1818313598632812,0,0.1910934448242188,0,0.2101821899414062,0,0.2473983764648438,0,0.2375946044921875,0,0.2360382080078125,0,0,0.2342376708984375,0,0.1728439331054688,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.869697570800781,0,0.124603271484375,0,0.1682815551757812,0,0.16668701171875,0.1807403564453125,0,0.1949539184570312,0.1942672729492188,0,0.2093429565429688,0,0.2255401611328125,0.250335693359375,0,0.2080154418945312,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.8392333984375,0,0,0,0,0,0.17401123046875,0,0.1909027099609375,0,0.1995162963867188,0.211151123046875,0,0.2252578735351562,0.235382080078125,0.2228469848632812,0,0.2010498046875,0,0.2195816040039062,0.2275848388671875,0.2280197143554688,0.2276611328125,0,0.2282562255859375,0,0.2293472290039062,0.2103958129882812,0,0.1949539184570312,0,0.193267822265625,0.1933212280273438,0,0.1937103271484375,0,0.1934432983398438,0.1934967041015625,0,0.1932525634765625,0,0.1934967041015625,0,0.188690185546875,0,0.2105178833007812,0,0.1938858032226562,0,0.19342041015625,0,0.1742935180664062,0.1489410400390625,0,0.1746139526367188,0.177581787109375,0.1855850219726562,0,0.1823196411132812,0.1718063354492188,0,0.1839065551757812,0,0,0.185699462890625,0.1834793090820312,0.1762466430664062,0,0.16290283203125,0,0,0,0,0,-7.325103759765625,0,0.2051544189453125,0,0.1973724365234375,0,0.1993637084960938,0,0,0.2079620361328125,0,0.2238998413085938,0,0.22796630859375,0,0.2166061401367188,0.2261276245117188,0.2386474609375,0.2329635620117188,0,0.2382965087890625,0.2384719848632812,0,0.2390213012695312,0,0.2389755249023438,0.2386932373046875,0,0.2380905151367188,0,0.2381744384765625,0.2386474609375,0.2380523681640625,0.2375946044921875,0.2373733520507812,0.2373046875,0,0.2369461059570312,0.2372207641601562,0,0.2379684448242188,0.2360763549804688,0.2344970703125,0,0.2374954223632812,0.2366256713867188,0,0.2358551025390625,0,0.249359130859375,0,0.21759033203125,0,0.1405563354492188,0,0,0,0,0,0,0,0,-7.192451477050781,0,0.1793365478515625,0,0.1921615600585938,0,0.2014312744140625,0.2058944702148438,0,0.2158432006835938,0.214080810546875,0.2047576904296875,0,0.2334060668945312,0,0.2391586303710938,0,0.2354354858398438,0,0.2369155883789062,0,0,0.23834228515625,0,0.2373504638671875,0,0.2367172241210938,0,0.2311019897460938,0,0.2348556518554688,0.2356338500976562,0,0.2359771728515625,0,0.2362289428710938,0,0,0.2607574462890625,0,0.2368927001953125,0,0.2376174926757812,0,0.23724365234375,0,0.2370758056640625,0.2367172241210938,0.236541748046875,0.2366714477539062,0,0.2377700805664062,0,0.2370452880859375,0.233734130859375,0,0.2253494262695312,0,0,0.2259292602539062,0.0749969482421875,0,0,0,0,0,0,0,0,0,0,0,-7.044807434082031,0,0.1810302734375,0.19403076171875,0.1996383666992188,0.2040176391601562,0,0.209808349609375,0.2092132568359375,0.222503662109375,0,0.239654541015625,0.2606658935546875,0,0.2338714599609375,0.2354888916015625,0,0.2353363037109375,0,0.23388671875,0,0.2121505737304688,0,0.23468017578125,0.2326431274414062,0,0.2173843383789062,0,0.2293624877929688,0,0.1890411376953125,0.2179031372070312,0,0.208099365234375,0,0.2179794311523438,0,0.2209396362304688,0,0.216156005859375,0,0.22601318359375,0,0.221282958984375,0,0.2235794067382812,0.2299957275390625,0,0.2215042114257812,0,0.2198028564453125,0,0.190582275390625,0,0.1960372924804688,0,0.2235260009765625,0,0.04018402099609375,0,0,0,0,0,0,0,0,-6.964759826660156,0,0.175689697265625,0,0.1831588745117188,0,0,0.192718505859375,0.1938705444335938,0,0,0.181427001953125,0,0,0.1881256103515625,0,0,0.193756103515625,0.2150650024414062,0,0.2188873291015625,0.1745452880859375,0,0.222686767578125,0,0,0.19903564453125,0.2238540649414062,0,0.2202072143554688,0,0.2208938598632812,0.2306747436523438,0.2220535278320312,0.2273178100585938,0,0.2307662963867188,0,0.2344512939453125,0.2338790893554688,0,0.2332000732421875,0,0.231658935546875,0.2315597534179688,0,0.2340850830078125,0,0.2346115112304688,0.2350006103515625,0,0.23583984375,0,0.2294845581054688,0,0.2379684448242188,0,0.2274093627929688,0,0.2218017578125,0,0.2223281860351562,0,0.0065460205078125,0,0,0,0,0,-6.760047912597656,0,0.1866378784179688,0.1964111328125,0.19677734375,0.1999435424804688,0.1985092163085938,0,0.2307357788085938,0.2374191284179688,0,0.2374191284179688,0,0.2347869873046875,0.2325439453125,0,0.2333755493164062,0,0,0.23284912109375,0,0.2339019775390625,0,0.2340164184570312,0.2348861694335938,0,0.2337265014648438,0,0.2341156005859375,0.2340316772460938,0,0.232208251953125,0.2345657348632812,0,0.233551025390625,0,0.2344207763671875,0,0.2347335815429688,0.2352066040039062,0,0.2351913452148438,0.2353134155273438,0.2354812622070312,0,0.2596817016601562,0,0.2240676879882812,0,0.2240142822265625,0.1162338256835938,0,0,0,0,0,0,0,0,-6.746696472167969,0.1708602905273438,0,0.189300537109375,0,0.194976806640625,0,0,0.194000244140625,0.1961288452148438,0.2220840454101562,0.2363967895507812,0,0,0.2379379272460938,0,0.2354202270507812,0.2306365966796875,0,0.23150634765625,0.230560302734375,0,0.2335052490234375,0.2329025268554688,0,0.2291259765625,0.2325210571289062,0,0.2311248779296875,0,0.2313003540039062,0,0.2321319580078125,0,0.2561569213867188,0,0.232696533203125,0,0.2328872680664062,0,0.233917236328125,0,0.2335281372070312,0,0,0.2354888916015625,0,0.2354812622070312,0,0.2353668212890625,0,0.2361907958984375,0.2273483276367188,0.2247314453125,0.1639633178710938,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-6.657844543457031,0,0,0,0,0,0,0,0,0.1651687622070312,0,0.1908950805664062,0,0.1947555541992188,0,0.1942367553710938,0.1981277465820312,0,0.2262039184570312,0,0.2375869750976562,0,0,0.2265167236328125,0,0.2267379760742188,0,0,0.2218475341796875,0.2282257080078125,0,0.2315216064453125,0.230926513671875,0,0.226318359375,0,0,0.231170654296875,0.2365188598632812,0.2356185913085938,0,0,0.2365493774414062,0,0.2363357543945312,0,0.2216644287109375,0,0.2388076782226562,0,0.237945556640625,0,0.2379913330078125,0,0.2381057739257812,0,0.2622833251953125,0,0.2385406494140625,0,0.2395095825195312,0,0.2399978637695312,0,0.2384872436523438,0,0.2381057739257812,0,0.0414276123046875,0,0,0,0,0,0,0,0,-6.464683532714844,0,0.1879348754882812,0,0.1948471069335938,0.19097900390625,0.194366455078125,0.22613525390625,0,0.2390060424804688,0,0,0.2355422973632812,0.233551025390625,0.2321624755859375,0.2326812744140625,0.2317276000976562,0,0.2322235107421875,0.23443603515625,0.2335662841796875,0.2352523803710938,0,0.2330169677734375,0,0.2319793701171875,0,0.2567596435546875,0,0,0.2337646484375,0.2331771850585938,0,0.2337646484375,0.2338409423828125,0,0.2339553833007812,0,0.234771728515625,0,0,0.2376327514648438,0.24456787109375,0,0,0.24407958984375,0,0.2434463500976562,0.2228012084960938,0,0,0,0,0,0,0,0,0,0,0,-6.348037719726562,0,0.11474609375,0,0.1277923583984375,0,0.1875381469726562,0,0,0.1847763061523438,0,0,0.2314987182617188,0.2296676635742188,0,0.2149581909179688,0,0.1945648193359375,0,0.126190185546875,0,0,0.106842041015625,0,0.110748291015625,0,0,0.1080703735351562,0,0.1552963256835938,0.1965713500976562,0,0,0.1978988647460938,7.751434326171875,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7.62939453125,0,0,7.62939453125e-06,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,15.2587890625,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7.629417419433594,0,0,0,0,0,0,0,0.0393218994140625,0,0,0,0,15.35587310791016,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"filename":["<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,null,null,null,null,null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,null,"<expr>",null,null,null,null,"<expr>",null,null,null,"<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,null,null,null,null,null,null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,null,null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,null,null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,null,null,null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>","<expr>",null,null,null,null,"<expr>",null,null,null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,null,null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,null,null,null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>","<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,null,null,null,null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,null,null,null,null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,null,null,null,null,null,null,null,null,null,null,null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,null,null,null,null,null,null,null,null,"<expr>","<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null]},"interval":10,"files":[{"filename":"<expr>","content":"## Generate Large Random Dataset\nn <- 2e6\nx <- runif(n)\ny <- runif(n)\nz <- runif(n)\nXYZ <- cbind(x,y,z)\n\n## Inspect 4 equivalent `row mean` calculations \nprofvis::profvis({\n    m <- rowSums(XYZ)/ncol(XYZ)\n    m <- rowMeans(XYZ)\n    m <- apply(XYZ, 1, mean)\n    m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }\n})\n## rowSums(), colSums(), rowMeans(), and colMeans() are vectorised and fast.\n## for loop is not the slowest, but the ugliest.","normpath":"<expr>"}],"prof_output":"/tmp/Rtmp5Qq32o/file36556e71b31a.prof","highlight":{"output":["^output\\$"],"gc":["^<GC>$"],"stacktrace":["^\\.\\.stacktraceo(n|ff)\\.\\.$"]},"split":"h"}},"evals":[],"jsHooks":[]}</script>
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
## 1 mean1(x, 0.5)   36.5ms   37.2ms      26.5    7.63MB     0   
## 2 mean2(x, 0.5)   32.7ms   35.8ms      28.0    7.63MB     2.15
## 3 mean3(x, 0.5)   36.4ms   37.1ms      26.8    7.63MB     0
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
##   0.135   0.000   0.046
```

```r
system.time({ lm(Y~X, data=DAT) })
```

```
##    user  system elapsed 
##   0.505   0.001   0.191
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
## 1 ma1(y)      284.4ms  284.4ms      3.52    15.3MB     3.52
## 2 ma2(y)       29.8ms   30.5ms     32.7     91.6MB   180.
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
##   0.036   0.002   0.038
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
##   1.281   0.323   0.897
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





