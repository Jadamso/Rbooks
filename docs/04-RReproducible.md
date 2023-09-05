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
<div class="plotly html-widget html-fill-item-overflow-hidden html-fill-item" id="htmlwidget-ba853a966cd707f07922" style="width:672px;height:480px;"></div>
<script type="application/json" data-for="htmlwidget-ba853a966cd707f07922">{"x":{"visdat":{"a67f72d2dcb7":["function () ","plotlyVisDat"]},"cur_data":"a67f72d2dcb7","attrs":{"a67f72d2dcb7":{"x":{},"y":{},"alpha_stroke":1,"sizes":[10,100],"spans":[1,20]}},"layout":{"margin":{"b":40,"l":60,"t":25,"r":10},"xaxis":{"domain":[0,1],"automargin":true,"title":"X"},"yaxis":{"domain":[0,1],"automargin":true,"title":"Y"},"hovermode":"closest","showlegend":false},"source":"A","config":{"modeBarButtonsToAdd":["hoverclosest","hovercompare"],"showSendToCloud":false},"data":[{"x":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100],"y":[5.892049583029924,6.7734263430615709,14.280256502598881,19.749562388196924,24.152087288576745,25.291176880656462,31.29566355204474,31.697090214837509,36.067667372263514,42.669676974021499,43.64587050653256,48.733297770924899,50.647358788459172,61.47132832250427,58.048226544321459,65.514518622378134,67.641547933628289,72.744218840721658,77.272457275301761,79.183432586557444,83.442925005039669,87.910883364218151,91.993730861681044,97.70539810919179,101.18052408651161,105.09437446709065,105.47024994037463,111.86592257549941,113.54656804258117,119.55399686135135,125.72024083472152,128.72173416535281,132.5621141710167,137.15677736308254,139.7506973447413,141.41386360360508,146.3207891203179,152.87844737912516,154.40993014475524,153.82759273723224,167.73557275279509,168.55335439272247,174.23234784512081,174.76683562496834,180.5338812082878,184.10075787569053,188.62669309550159,192.46622138216071,195.16753491979173,199.25070923567867,204.22584473218012,208.10816157508646,211.97341077585216,220.63804820834602,217.37618469960194,224.15489014038525,226.26591930966623,233.34566521111685,236.74208818438464,237.08080792247512,246.21877923209422,250.12316590408838,251.51673208762128,255.7259020619247,259.81098612425376,262.72375995775678,269.49475715051722,268.75447000947128,274.34967125138218,280.81543317436052,284.16042352302895,288.51917821450019,291.51731991735409,294.62294797026578,298.85232058716383,304.84915569111479,308.96802556076256,310.53824570117087,317.99299204441064,321.17976735695311,324.41372819052071,325.56095650309214,332.13669682439792,339.02188074162018,340.24034188586825,341.95309104999745,346.16222176264478,353.06068206030199,352.46151896203315,362.24992499790676,360.02200014234597,368.36612348393419,373.04106814785774,376.06899355241319,379.95442826413796,383.59863738495881,385.94082720142558,393.75749445040861,397.0833635367087,398.13031918191558],"type":"scatter","mode":"markers","marker":{"color":"rgba(31,119,180,1)","line":{"color":"rgba(31,119,180,1)"}},"error_y":{"color":"rgba(31,119,180,1)"},"error_x":{"color":"rgba(31,119,180,1)"},"line":{"color":"rgba(31,119,180,1)"},"xaxis":"x","yaxis":"y","frame":null}],"highlight":{"on":"plotly_click","persistent":false,"dynamic":false,"selectize":false,"opacityDim":0.20000000000000001,"selected":{"opacity":1},"debounce":0},"shinyEvents":["plotly_hover","plotly_click","plotly_selected","plotly_relayout","plotly_brushed","plotly_brushing","plotly_clickannotation","plotly_doubleclick","plotly_deselect","plotly_afterplot","plotly_sunburstclick"],"base_url":"https://plot.ly"},"evals":[],"jsHooks":[]}</script>
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
##           used (Mb) gc trigger  (Mb) max used  (Mb)
## Ncells 1209553 64.6    2357228 125.9  2357228 125.9
## Vcells 2293954 17.6    8388608  64.0  3532446  27.0
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
##   0.005   0.000   0.005
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
<div class="profvis html-widget html-fill-item-overflow-hidden html-fill-item" id="htmlwidget-0c59f8d74f334ab1e31c" style="width:100%;height:600px;"></div>
<script type="application/json" data-for="htmlwidget-0c59f8d74f334ab1e31c">{"x":{"message":{"prof":{"time":[1,2,3,4,5,5,6,7,8,9,10,10,11,11,12,12,13,13,14,14,15,15,16,16,17,17,18,18,19,19,20,20,21,21,22,22,23,23,24,24,25,25,26,26,26,27,28,29,29,30,31,32,32,32,33,33,34,35,35,35,36,36,37,37,38,38,39,39,39,40,40,41,41,41,42,42,43,43,43,44,45,45,45,46,47,47,48,49,49,50,50,50,51,51,51,52,53,53,54,54,55,55,56,56,56,57,57,58,59,60,60,61,62,63,63,64,64,65,65,66,66,67,67,67,68,68,69,70,70,71,72,73,73,74,74,75,75,76,76,77,78,78,79,80,81,82,83,83,84,84,85,85,85,86,86,87,88,88,89,89,89,90,90,91,91,92,92,92,93,94,94,94,95,95,96,97,97,98,98,99,99,100,101,102,102,103,103,103,104,104,104,105,105,106,106,107,108,108,109,110,110,111,111,111,112,113,114,114,115,116,116,116,117,117,118,118,119,119,120,121,121,121,122,122,123,124,125,125,126,126,127,127,128,128,129,129,129,130,130,131,132,133,133,134,135,135,136,137,137,138,138,138,139,139,140,141,141,142,143,144,144,145,145,146,146,146,147,147,148,148,149,149,150,150,150,151,151,152,152,152,153,153,153,154,154,155,155,156,156,157,157,158,158,159,160,160,160,161,161,162,162,163,163,164,164,165,165,166,166,167,167,168,169,169,170,171,171,172,173,173,174,174,175,175,176,176,177,178,178,179,179,180,180,181,181,182,182,183,183,184,184,185,186,186,187,187,188,188,188,189,189,190,190,191,191,192,193,194,194,195,195,196,196,197,197,198,198,199,199,200,201,202,202,203,203,204,204,205,205,206,206,207,207,208,208,209,209,210,210,211,211,212,212,213,213,214,214,215,215,216,216,217,217,218,218,219,219,219,220,221,221,221,222,222,222,223,224,224,224,225,226,226,227,228,228,229,230,230,231,231,232,233,234,234,235,236,237,237,238,238,238,239,240,241,242,242,243,243,244,244,244,245,246,246,246,247,247,248,248,249,249,250,250,251,252,252,253,253,254,254,254,255,255,256,256,257,258,259,260,261,261,262,262,262,263,263,264,264,265,265,266,266,267,267,268,268,269,269,269,270,270,271,271,272,272,273,273,274,274,275,276,276,277,277,278,278,279,280,280,281,281,282,283,283,284,284,284,285,285,286,286,287,287,287,288,288,288,289,289,290,291,291,292,292,293,294,294,295,295,296,296,297,298,298,299,299,300,300,301,301,302,303,304,304,305,305,306,306,306,307,307,307,308,308,309,310,310,311,312,312,313,313,314,314,315,315,316,316,317,317,318,318,319,320,320,320,321,321,322,322,323,323,323,324,325,325,326,326,327,327,328,328,329,329,330,330,331,331,332,332,333,333,334,334,335,335,336,336,337,337,337,338,339,339,340,340,341,342,342,342,343,343,344,344,345,345,345,346,346,347,347,348,348,348,349,349,350,351,351,351,352,353,354,354,354,355,355,355,356,356,357,357,358,359,359,360,360,361,361,362,362,362,363,363,363,364,364,365,365,366,366,367,367,368,368,369,369,369,370,370,370,371,371,371,372,372,372,373,373,373,374,374,374,375,375,375,376,376,376,377,377,377,378,378,378,379,379,379,380,380,380,381,381,381,382,382,382,383,383,383,384,384,384,385,385,385,386,386,386,387,387,387,388,388,388,389,389,389,390,390,390,391,391,391,392,392,392,393,393,393,394,394,394,395,395,395,396,396,396,397,397,398,398,399,399,400,400,401,401,402,403,403,404,404,404,405,406,407,408,409,409,409,410,410,411,411,411,412,412,412,413,413,414,415,416,417,418,419,420,420,421,422,422,423,423,424,424,425,425,426,426,427,428,428,429,429,429,430,431,432,433,433,434,434,435,435,436,436,437,437,438,438,438,439,439,439,440,440,440,441,441,442,442,443,443,444,444,445,445,445,446,446,447,447,448,449,449,449,450,451,452,452,453,453,453,454,454,454,455,455,456,456,457,457,458,458,459,459,460,460,460,461,461,462,463,464,465,465,466,466,467,468,468,469,469,470,470,471,471,471,472,472,473,474,475,475,476,477,478,478,479,480,481,481,481,482,482,482,483,484,484,485,485,485,486,486,487,487,488,489,489,490,490,491,491,492,493,494,494,495,495,495,496,496,497,498,498,499,500,500,501,502,502,503,504,505,505,506,506,507,508,508,508,509,509,509,510,510,511,511,512,512,513,514,514,515,515,516,516,517,517,518,518,519,520,520,521,521,521,522,522,523,523,524,524,525,525,526,526,527,527,528,528,529,529,530,530,531,532,533,533,534,534,535,535,536,536,536,537,537,538,538,538,539,539,539,540,540,541,542,542,542,543,543,544,545,546,546,547,547,547,548,548,548,549,549,550,550,551,552,552,552,553,553,554,554,555,556,557,557,558,558,559,559,560,560,561,562,562,562,563,563,564,565,565,566,566,567,567,567,568,569,569,570,570,571,572,572,573,573,574,574,574,575,576,576,577,578,578,579,579,579,580,580,580,581,581,582,583,583,584,584,585,585,586,586,587,587,588,588,589,590,591,591,592,592,593,593,593,594,594,594,595,595,596,596,597,597,598,598,599,599,599,600,601,602,602,603,603,604,604,605,605,606,606,607,607,608,608,609,609,610,610,611,611,612,612,613,613,614,615,616,617,617,618,619,619,619,620,621,621,622,623,623,623,624,624,625,625,625,626,626,627,628,629,629,630,630,631,631,631,632,632,632,633,633,634,634,635,635,636,636,637,637,638,638,639,639,640,641,641,642,642,643,643,644,644,645,645,646,646,647,648,648,649,649,650,650,651,651,652,652,653,654,654,655,656,657,657,657,658,658,658,659,660,660,661,662,662,663,663,664,664,665,666,666,667,667,668,669,669,670,670,671,671,672,672,673,673,674,675,676,677,677,677,678,678,679,679,680,680,681,681,682,683,683,684,684,684,685,685,685,686,686,686,687,687,687,688,688,688,689,689,689,690,690,690,691,691,691,692,692,692,693,693,693,694,694,694,695,695,695,696,696,696,697,697,697,698,698,698,699,699,700,700,701,701,702,702,703,703,704,704,705,705,705,706,706,707,707,708,709,709,710,710,711,711,711,712,712,712,713,713,714,715,715,716,717,717,718,718,719,719,720,720,721,722,722,723,723,723,724,724,724,725,725,726,726,727,727,728,729,729,730,730,731,731,731,732,733,734,734,735,735,735,736,736,736,737,737,738,738,739,739,740,740,741,741,741,742,742,743,744,745,745,746,746,747,747,748,748,749,749,749,750,750,751,751,752,753,753,754,754,755,756,756,757,758,759,759,759,760,760,760,761,761,762,762,763,764,764,765,765,766,766,767,767,768,769,769,770,771,771,772,772,773,773,774,774,775,775,776,776,776,777,777,778,778,779,779,780,780,781,782,782,783,783,784,784,785,785,786,786,786,787,787,788,788,789,790,790,791,792,792,792,793,793,794,794,795,795,796,796,797,798,798,799,799,800,800,801,801,802,803,803,804,804,805,805,805,806,806,807,807,808,808,809,810,811,811,811,812,813,814,814,815,816,816,816,817,817,817,818,818,819,819,820,821,821,822,822,823,823,824,824,825,825,826,826,827,827,828,828,828,829,829,829,830,830,831,831,832,832,833,833,834,834,835,835,836,837,837,838,839,839,839,840,840,840,841,842,842,843,843,844,844,845,845,846,847,847,847,848,848,849,849,850,850,850,851,851,851,852,853,853,853,854,854,855,855,856,857,858,859,859,860,860,861,861,862,862,863,863,864,865,865,866,866,867,867,868,868,869,870,871,871,872,872,872,873,873,873,874,875,875,876,876,877,877,878,879,879,880,880,881,882,882,883,883,883,884,884,884,885,885,886,886,887,887,888,889,889,890,890,891,891,892,893,894,894,894,895,895,895,896,896,897,897,898,898,899,900,901,902,902,903,903,904,904,904,905,905,905,906,906,907,907,908,909,910,910,911,911,912,912,913,913,914,914,915,915,916,916,917,917,918,918,919,920,921,921,922,922,923,923,924,924,925,925,925,926,926,926,927,928,928,929,930,930,931,931,932,933,933,934,934,935,935,935,936,936,936,937,937,937,938,938,938,939,939,939,940,940,940,941,941,941,942,942,942,943,943,943,944,944,944,945,945,945,946,946,947,947,948,949,950,950,951,951,952,952,953,953,954,955,955,956,956,957,958,958,959,959,960,960,961,962,962,963,964,964,965,965,965,966,966,966,967,968,968,969,970,970,971,971,972,972,973,973,974,974,975,975,975,976,976,976,977,978,978,979,979,980,980,981,981,982,982,983,983,984,985,985,986,986,986,987,987,987,988,988,989,989,989,990,990,991,992,993,993,994,995,995,996,996,997,997,998,998,999,999,1000,1000,1001,1001,1002,1002,1003,1003,1003,1004,1005,1005,1006,1006,1007,1007,1008,1008,1008,1009,1009,1010,1010,1010,1011,1011,1012,1012,1013,1013,1014,1015,1016,1016,1016,1017,1017,1017,1018,1018,1019,1019,1020,1020,1021,1021,1022,1023,1023,1024,1024,1025,1025,1026,1026,1027,1028,1028,1029,1029,1029,1030,1031,1032,1032,1033,1033,1034,1034,1034,1035,1035,1035,1036,1037,1038,1038,1039,1040,1041,1042,1042,1043,1043,1043,1044,1044,1044,1045,1046,1047,1047,1048,1048,1049,1050,1051,1051,1052,1052,1052,1053,1053,1053,1054,1054,1054,1055,1056,1057,1057,1058,1058,1058,1059,1060,1060,1061,1061,1062,1062,1062,1063,1063,1063,1064,1064,1065,1065,1066,1066,1067,1067,1068,1068,1069,1069,1070,1070,1071,1071,1072,1072,1073,1073,1074,1075,1075,1076,1077,1078,1078,1078,1079,1080,1080,1080,1081,1081,1081,1082,1083,1084,1084,1085,1085,1086,1086,1086,1087,1087,1088,1088,1088,1089,1089,1089,1090,1090,1090,1091,1091,1091,1092,1092,1092,1093,1093,1093,1094,1094,1094,1095,1096,1096,1096,1097,1098,1098,1099,1100,1101,1101,1102,1102,1102,1103,1103,1103,1104,1104,1104,1105,1105,1105,1106,1106,1106,1107,1107,1107,1108,1108,1108,1109,1109,1109,1110,1110,1110,1111,1111,1111,1112,1112,1112,1113,1113,1113,1114,1114,1114,1115,1115,1115,1116,1116,1116,1117,1117,1117,1118,1118,1118,1119,1119,1119,1120,1120,1120,1121,1121,1121,1122,1122,1122,1123,1123,1123,1124,1124,1124,1125,1125,1125,1126,1126,1126,1127,1127,1127,1128,1128,1128,1129,1129,1129,1130,1130,1130,1131,1131,1131,1132,1132,1132,1133,1133,1133,1134,1134,1134,1135,1135,1135,1136,1136,1136,1137,1137,1137,1138,1138,1138,1139,1139,1139,1140,1140,1140,1141,1141,1141,1142,1142,1142,1143,1143,1143,1144,1144,1144,1145,1145,1145,1146,1146,1146,1147,1147,1147,1148,1148,1148,1149,1149,1149,1150,1150,1150,1151,1151,1151,1152,1152,1152,1153,1153,1153,1154,1154,1154,1155,1155,1155,1156,1156,1156,1157,1157,1157,1158,1158,1158,1159,1160,1160,1161,1161,1162,1162,1163,1163,1164,1164,1165,1166,1166,1167,1167,1168,1168,1169,1169,1170,1171,1171,1171,1172,1172,1172,1173,1173,1174,1175,1176,1176,1177,1177,1178,1179,1179,1180,1181,1181,1182,1182,1183,1183,1183,1184,1184,1184,1185,1185,1186,1187,1187,1188,1189,1190,1190,1191,1191,1192,1192,1193,1194,1194,1195,1196,1196,1197,1198,1199,1200,1200,1201,1201,1202,1203,1204,1204,1205,1205,1206,1206,1206,1207,1207,1207,1208,1208,1209,1210,1211,1212,1212,1213,1214,1214,1215,1215,1216,1217,1217,1218,1218,1219,1220,1221,1221,1222,1222,1223,1223,1224,1224,1225,1225,1226,1226,1227,1227,1228,1228,1228,1229,1229,1229,1230,1230,1230,1231,1232,1232,1233,1233,1234,1234,1235,1236,1237,1237,1238,1239,1239,1240,1240,1241,1241,1242,1243,1243,1243,1244,1244,1244,1245,1246,1246,1247,1247,1248,1248,1249,1250,1250,1251,1251,1251,1252,1252,1252,1253,1253,1253,1254,1254,1255,1255,1256,1256,1257,1257,1257,1258,1258,1259,1260,1260,1261,1261,1262,1263,1263,1263,1264,1265,1265,1266,1267,1267,1268,1268,1269,1269,1270,1271,1272,1272,1273,1274,1274,1275,1275,1276,1276,1277,1277,1277,1278,1278,1279,1279,1280,1280,1281,1281,1282,1283,1284,1285,1286,1286,1287,1288,1289,1289,1290,1290,1291,1292,1292,1293,1293,1294,1294,1295,1295,1296,1296,1296,1297,1297,1297,1298,1298,1298,1299,1299,1300,1300,1300,1301,1301,1302,1302,1303,1303,1304,1304,1305,1305,1306,1306,1307,1308,1309,1309,1309,1310,1311,1311,1312,1313,1313,1314,1314,1315,1316,1317,1317,1318,1318,1319,1319,1320,1320,1321,1321,1322,1322,1323,1323,1324,1324,1325,1325,1326,1326,1327,1327,1328,1328,1329,1329,1330,1330,1331,1331,1332,1333,1333,1334,1335,1335,1336,1337,1337,1338,1339,1340,1340,1341,1341,1341,1342,1342,1342,1343,1344,1344,1345,1345,1346,1346,1347,1347,1348,1348,1348,1349,1349,1349,1350,1350,1350,1351,1352,1353,1353,1354,1355,1356,1357,1357,1358,1359,1359,1360,1360,1360,1361,1361,1362,1363,1363,1363,1364,1364,1365,1365,1366,1366,1367,1367,1368,1369,1369,1370,1370,1371,1371,1372,1372,1373,1373,1374,1374,1375,1375,1376,1377,1377,1378,1379,1380,1381,1381,1382,1382,1382,1383,1383,1383,1384,1384,1385,1385,1386,1386,1387,1387,1388,1388,1389,1389,1390,1390,1391,1391,1392,1392,1393,1393,1394,1394,1395,1395,1396,1397,1397,1398,1398,1399,1399,1400,1400,1401,1401,1402,1402,1403,1403,1404,1404,1405,1405,1406,1406,1407,1407,1408,1408,1409,1409,1410,1410,1411,1411,1412,1412,1413,1413,1414,1414,1415,1415,1416,1416,1417,1417,1418,1418,1418,1418,1418,1418,1418,1418,1418,1418,1418,1418,1418,1418,1418,1419,1419,1419,1419,1419,1419,1419,1419,1420,1420,1420,1420,1420,1420,1420,1420,1421,1421,1421,1421,1421,1421,1421,1421,1422,1422,1422,1422,1422,1422,1422,1422,1423,1423,1423,1423,1423,1423,1423,1423,1424,1424,1424,1424,1424,1424,1424,1424,1425,1425,1425,1425,1425,1425,1425,1425,1426,1426,1426,1426,1426,1426,1426,1426,1427,1427,1427,1427,1427,1427,1427,1427,1428,1428,1428,1428,1428,1428,1428,1428,1429,1429,1429,1429,1429,1429,1429,1429,1430,1430,1430,1430,1430,1430,1430,1430,1431,1431,1431,1431,1431,1431,1431,1431,1432,1432,1432,1432,1432,1432,1432,1432,1433,1433,1433,1433,1433,1433,1433,1433,1434,1434,1434,1434,1434,1434,1434,1434,1435,1435,1435,1435,1435,1435,1435,1435,1436,1436,1436,1436,1436,1436,1436,1436,1437,1437,1437,1437,1437,1437,1437,1437],"depth":[1,1,1,1,2,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,1,2,1,1,1,3,2,1,2,1,1,3,2,1,2,1,2,1,2,1,3,2,1,2,1,3,2,1,2,1,3,2,1,1,3,2,1,1,2,1,1,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,3,2,1,2,1,1,1,2,1,1,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,1,1,2,1,2,1,2,1,2,1,1,2,1,1,1,1,1,2,1,2,1,3,2,1,2,1,1,2,1,3,2,1,2,1,2,1,3,2,1,1,3,2,1,2,1,1,2,1,2,1,2,1,1,1,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,1,2,1,3,2,1,1,1,2,1,1,3,2,1,2,1,2,1,2,1,1,3,2,1,2,1,1,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,1,2,1,1,2,1,1,2,1,3,2,1,2,1,1,2,1,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,3,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,3,2,1,3,2,1,1,3,2,1,1,2,1,1,2,1,1,2,1,2,1,1,1,2,1,1,1,2,1,3,2,1,1,1,1,2,1,2,1,3,2,1,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,2,1,1,1,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,3,2,1,2,1,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,3,2,1,3,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,1,3,2,1,2,1,2,1,3,2,1,2,1,2,1,3,2,1,2,1,1,3,2,1,1,1,3,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,1,1,1,1,3,2,1,2,1,3,2,1,3,2,1,2,1,1,1,1,1,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,1,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,3,2,1,1,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,1,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,2,1,1,1,2,1,1,1,2,1,1,1,3,2,1,3,2,1,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,1,1,2,1,3,2,1,2,1,1,2,1,1,2,1,1,2,1,1,1,2,1,2,1,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,3,2,1,2,1,3,2,1,3,2,1,2,1,1,3,2,1,2,1,1,1,2,1,3,2,1,3,2,1,2,1,2,1,1,3,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,1,2,1,2,1,3,2,1,1,2,1,2,1,1,2,1,2,1,3,2,1,1,2,1,1,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,3,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,1,2,1,1,3,2,1,1,2,1,1,3,2,1,2,1,3,2,1,2,1,1,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,1,3,2,1,3,2,1,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,1,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,1,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,1,2,1,1,1,3,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,1,3,2,1,1,1,2,1,1,3,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,3,2,1,3,2,1,1,3,2,1,2,1,2,1,1,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,1,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,1,3,2,1,3,2,1,2,1,2,1,2,1,1,1,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,1,2,1,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,1,2,1,3,2,1,3,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,3,2,1,2,1,3,2,1,2,1,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,3,2,1,2,1,3,2,1,2,1,2,1,2,1,1,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,1,1,2,1,2,1,3,2,1,3,2,1,1,1,2,1,1,1,1,2,1,3,2,1,3,2,1,1,1,2,1,2,1,1,1,2,1,3,2,1,3,2,1,3,2,1,1,1,2,1,3,2,1,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,1,3,2,1,1,3,2,1,3,2,1,1,1,2,1,2,1,3,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,1,3,2,1,1,2,1,1,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,2,1,1,1,2,1,2,1,1,2,1,1,2,1,2,1,3,2,1,3,2,1,2,1,1,2,1,1,1,2,1,2,1,2,1,1,2,1,1,2,1,1,1,1,2,1,2,1,1,1,2,1,2,1,3,2,1,3,2,1,2,1,1,1,1,2,1,1,2,1,2,1,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,1,1,2,1,1,2,1,2,1,2,1,1,3,2,1,3,2,1,1,2,1,2,1,2,1,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,1,3,2,1,1,2,1,1,2,1,2,1,2,1,1,1,2,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,1,1,1,2,1,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,3,2,1,1,2,1,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,1,2,1,1,1,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,1,1,2,1,1,1,1,2,1,1,2,1,3,2,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,1,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1],"label":["rowSums","rowSums","rowSums","rowSums","/","local","rowMeans","rowMeans","rowMeans","rowMeans","aperm.default","apply","aperm.default","apply","aperm.default","apply","aperm.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","apply","apply","mean.default","apply","apply","apply","<GC>","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","apply","isTRUE","mean.default","apply","apply","mean.default","apply","apply","mean.default","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","FUN","apply","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","<GC>","mean.default","apply","FUN","apply","apply","mean.default","apply","apply","apply","FUN","apply","FUN","apply","mean.default","apply","<GC>","apply","apply","FUN","apply","apply","apply","apply","apply","mean.default","apply","FUN","apply","<GC>","mean.default","apply","mean.default","apply","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","<GC>","FUN","apply","mean.default","apply","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","<GC>","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","mean.default","apply","<GC>","FUN","apply","apply","apply","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","length","local","apply","<GC>","FUN","apply","FUN","apply","apply","apply","FUN","apply","FUN","apply","mean.default","apply","is.numeric","local","<GC>","FUN","apply","FUN","apply","apply","apply","mean.default","apply","apply","FUN","apply","apply","FUN","apply","<GC>","length","local","FUN","apply","apply","mean.default","apply","apply","apply","FUN","apply","mean.default","apply","<GC>","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","<GC>","apply","mean.default","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","<GC>","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","mean.default","apply","apply","<GC>","apply","apply","length","local","FUN","apply","FUN","apply","FUN","apply","apply","mean.default","apply","FUN","apply","<GC>","apply","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","apply","apply","FUN","apply","mean.default","apply","<GC>","apply","is.na","local","mean.default","apply","FUN","apply","apply","apply","FUN","apply","FUN","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","is.numeric","local","FUN","apply","length","local","mean.default","apply","isTRUE","mean.default","apply","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","apply","isTRUE","mean.default","apply","apply","mean.default","apply","apply","FUN","apply","apply","<GC>","apply","FUN","apply","apply","apply","mean.default","apply","apply","apply","is.numeric","local","<GC>","length","local","apply","apply","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","<GC>","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","apply","apply","apply","apply","FUN","apply","<GC>","mean.default","apply","is.na","local","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","mean.default","apply","FUN","apply","is.numeric","local","FUN","apply","FUN","apply","apply","mean.default","apply","<GC>","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","<GC>","apply","mean.default","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","FUN","apply","<GC>","apply","mean.default","apply","FUN","apply","apply","apply","mean.default","apply","FUN","apply","<GC>","is.numeric","local","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","apply","mean.default","apply","<GC>","apply","FUN","apply","length","local","FUN","apply","FUN","apply","FUN","apply","apply","<GC>","is.na","local","mean.default","apply","length","local","isTRUE","mean.default","apply","apply","mean.default","apply","FUN","apply","<GC>","apply","<GC>","apply","mean.default","apply","mean.default","apply","is.na","local","FUN","apply","FUN","apply","<GC>","apply","<GC>","apply","FUN","apply","isTRUE","mean.default","apply","apply","mean.default","apply","mean.default","apply","apply","<GC>","mean.default","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","<GC>","apply","apply","isTRUE","mean.default","apply","apply","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","<GC>","apply","is.na","local","apply","is.na","local","FUN","apply","is.na","local","<GC>","is.na","local","<GC>","is.na","local","mean.default","apply","is.numeric","local","FUN","apply","mean.default","apply","is.numeric","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","is.numeric","local","FUN","apply","length","local","apply","mean.default","apply","isTRUE","mean.default","apply","apply","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","apply","apply","apply","apply","apply","apply","mean.default","apply","apply","FUN","apply","FUN","apply","mean.default","apply","<GC>","apply","<GC>","apply","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","length","local","mean.default","apply","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","length","local","apply","apply","apply","mean.default","apply","FUN","apply","apply","<GC>","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","FUN","apply","apply","apply","FUN","apply","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","mean.default","apply","<GC>","length","local","FUN","apply","apply","FUN","apply","apply","mean.default","apply","apply","FUN","apply","apply","apply","mean.default","apply","FUN","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","apply","is.na","local","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","<GC>","apply","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","apply","apply","FUN","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","length","local","<GC>","length","local","mean.default","apply","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","apply","<GC>","mean.default","apply","FUN","apply","mean.default","apply","apply","apply","FUN","apply","FUN","apply","length","local","FUN","apply","apply","isTRUE","mean.default","apply","mean.default","apply","apply","<GC>","apply","<GC>","apply","isTRUE","mean.default","apply","apply","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","is.na","local","length","local","mean.default","apply","FUN","apply","apply","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","apply","<GC>","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","apply","apply","apply","mean.default","apply","apply","<GC>","FUN","apply","apply","is.na","local","apply","isTRUE","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","is.numeric","local","apply","apply","FUN","apply","is.na","local","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","mean.default","apply","is.na","local","<GC>","apply","<GC>","apply","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","mean.default","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","<GC>","apply","mean.default","apply","FUN","apply","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","apply","FUN","apply","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","is.numeric","local","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","FUN","apply","is.na","local","<GC>","apply","<GC>","apply","isTRUE","mean.default","apply","length","local","FUN","apply","apply","mean.default","apply","FUN","apply","apply","FUN","apply","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","apply","mean.default","apply","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","apply","<GC>","apply","<GC>","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","is.numeric","local","apply","FUN","apply","apply","isTRUE","mean.default","apply","<GC>","apply","<GC>","apply","mean.default","apply","is.numeric","local","apply","FUN","apply","FUN","apply","is.na","local","mean.default","apply","apply","length","local","mean.default","apply","<GC>","length","local","FUN","apply","is.na","local","length","local","apply","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","is.na","local","mean.default","apply","apply","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","mean.default","apply","is.numeric","local","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","mean.default","apply","is.na","local","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","apply","apply","apply","FUN","apply","FUN","apply","<GC>","apply","<GC>","apply","FUN","apply","apply","mean.default","apply","length","local","mean.default","apply","FUN","apply","apply","apply","length","local","<GC>","FUN","apply","<GC>","FUN","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","FUN","apply","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","FUN","apply","mean.default","apply","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","is.na","local","mean.default","apply","FUN","apply","apply","apply","apply","FUN","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","length","local","apply","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","<GC>","is.numeric","local","<GC>","is.numeric","local","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","FUN","apply","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","<GC>","apply","<GC>","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","FUN","apply","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","mean.default","apply","apply","FUN","apply","FUN","apply","is.numeric","local","mean.default","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","mean.default","apply","FUN","apply","length","local","mean.default","apply","FUN","apply","mean.default","apply","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","FUN","apply","apply","FUN","apply","<GC>","apply","<GC>","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","is.numeric","local","<GC>","apply","<GC>","apply","isTRUE","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","length","local","mean.default","apply","mean.default","apply","apply","apply","<GC>","length","local","<GC>","length","local","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","FUN","apply","<GC>","apply","<GC>","apply","apply","mean.default","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","apply","mean.default","apply","apply","apply","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","apply","mean.default","apply","FUN","apply","apply","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","apply","mean.default","apply","isTRUE","mean.default","apply","apply","length","local","length","local","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","FUN","apply","is.numeric","local","FUN","apply","FUN","apply","FUN","apply","is.numeric","local","<GC>","apply","<GC>","apply","is.numeric","local","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","FUN","apply","length","local","apply","mean.default","apply","apply","is.numeric","local","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","apply","FUN","apply","apply","apply","mean.default","apply","FUN","apply","FUN","apply","apply","mean.default","apply","apply","mean.default","apply","apply","apply","apply","FUN","apply","length","local","apply","apply","FUN","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","apply","apply","apply","FUN","apply","apply","mean.default","apply","is.numeric","local","apply","FUN","apply","mean.default","apply","apply","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","FUN","apply","mean.default","apply","apply","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","mean.default","apply","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","apply","is.na","local","length","local","apply","isTRUE","mean.default","apply","apply","mean.default","apply","apply","mean.default","apply","mean.default","apply","mean.default","apply","apply","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","<GC>","apply","isTRUE","mean.default","apply","FUN","apply","is.numeric","local","FUN","apply","FUN","apply","apply","apply","apply","apply","mean.default","apply","apply","apply","mean.default","apply","FUN","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","length","local","FUN","apply","apply","apply","FUN","apply","FUN","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","mean.default","apply","mean.default","apply","mean.default","apply","apply","is.numeric","local","apply","mean.default","apply","apply","is.na","local","apply","apply","mean.default","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","is.na","local","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","apply","length","local","apply","apply","apply","FUN","apply","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","<GC>","apply","<GC>","apply","<GC>","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","apply","apply","apply","mean.default","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","isLoopTopFun","checkSkipLoopCntxt","checkSkipLoopCntxtList","checkSkipLoopCntxt","checkSkipLoopCntxtList","checkSkipLoopCntxt","checkSkipLoopCntxtList","checkSkipLoopCntxt","h","tryInline","cmpCall","cmp","genCode","compile","compiler:::tryCompile","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis"],"filenum":[1,1,1,1,1,null,1,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,1,1,null,1,1,1,null,null,1,null,1,1,null,null,1,null,1,null,1,null,1,null,null,1,null,1,null,null,1,null,1,null,null,1,1,null,null,1,1,null,1,1,null,1,null,null,1,null,null,1,1,null,1,null,1,null,1,null,null,1,null,1,1,1,null,1,1,1,null,1,null,1,null,1,null,1,null,null,1,null,1,1,null,1,1,1,null,1,null,1,null,1,null,1,1,null,1,1,1,1,1,null,1,null,1,null,null,1,null,1,1,null,1,null,null,1,null,1,null,1,null,null,1,1,null,null,1,null,1,1,null,1,null,1,null,1,1,1,null,1,null,null,1,null,null,1,null,1,null,1,1,null,1,1,null,1,null,null,1,1,1,null,1,1,null,null,1,null,1,null,1,null,null,1,null,null,1,null,1,1,1,null,1,null,1,null,1,null,null,null,null,1,null,1,1,1,null,1,1,null,1,1,null,1,null,null,null,null,1,1,null,1,1,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,null,1,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,1,null,1,1,null,null,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,null,1,null,1,null,1,null,1,1,1,null,1,null,1,null,1,null,null,null,1,null,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,null,1,null,null,null,1,null,null,1,1,null,null,1,null,null,1,1,null,null,1,1,null,1,1,null,1,1,null,1,null,1,1,1,null,1,1,1,null,null,null,null,null,1,1,1,null,1,null,1,null,null,1,1,null,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,null,1,null,1,null,1,1,1,1,1,null,1,null,null,1,null,null,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,null,null,1,null,1,1,null,1,null,1,null,1,1,null,1,null,1,1,null,1,null,null,1,null,1,null,1,null,null,1,null,null,1,null,1,1,null,1,null,1,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,1,1,null,1,null,1,null,null,null,null,null,1,null,1,1,null,1,1,null,1,null,1,null,1,null,null,null,1,null,1,null,1,1,null,null,null,null,1,null,null,null,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,null,1,null,1,null,1,null,1,null,1,null,null,1,1,null,1,null,1,1,null,null,1,null,1,null,1,null,null,1,null,1,null,1,null,null,1,null,1,1,null,null,1,1,1,null,null,1,null,null,1,null,1,null,null,1,null,null,null,1,null,null,null,null,null,null,null,null,null,1,null,null,null,1,null,1,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,1,null,1,null,1,null,null,null,1,null,null,1,null,1,null,null,1,1,1,1,1,null,null,1,null,1,null,null,1,null,null,1,null,1,1,1,1,1,1,1,null,1,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,null,1,1,1,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,null,1,1,null,null,1,1,1,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,1,1,null,1,null,1,1,null,1,null,1,null,1,null,null,1,null,1,1,1,null,1,1,1,null,1,1,1,null,null,1,null,null,1,1,null,1,null,null,1,null,1,null,1,1,null,1,null,1,null,1,1,1,null,1,null,null,null,null,1,1,null,1,1,null,1,1,null,1,1,1,null,1,null,1,1,null,null,1,null,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,1,null,null,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,1,null,1,null,1,null,1,null,null,1,null,1,null,null,null,null,null,null,null,1,1,null,null,1,null,1,1,1,null,1,null,null,1,null,null,1,null,1,null,1,1,null,null,1,null,1,null,1,1,1,null,1,null,1,null,null,null,1,1,null,null,1,null,1,1,null,1,null,1,null,null,1,1,null,1,null,1,1,null,1,null,1,null,null,1,1,null,1,1,null,1,null,null,1,null,null,1,null,1,1,null,1,null,1,null,null,null,null,null,1,null,1,1,1,null,1,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,null,null,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,1,1,null,1,1,null,null,1,1,null,null,1,null,null,1,null,1,null,null,1,null,null,1,1,null,1,null,null,null,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,null,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,1,null,1,1,1,null,null,1,null,null,1,1,null,1,1,null,1,null,1,null,1,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,1,1,1,null,null,1,null,1,null,1,null,1,null,1,1,null,1,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,1,null,1,null,1,null,null,1,null,null,1,null,1,1,null,1,1,null,1,null,1,null,1,null,1,1,null,1,null,null,1,null,null,1,null,1,null,1,null,1,1,null,1,null,1,null,null,1,1,1,null,1,null,null,1,null,null,1,null,null,null,1,null,1,null,1,null,null,1,null,1,1,1,null,1,null,null,null,1,null,1,null,null,1,null,null,null,1,1,null,1,null,1,1,null,1,1,1,null,null,1,null,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,null,1,null,1,1,null,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,null,null,1,1,null,null,null,1,null,null,null,null,1,null,null,null,null,1,1,null,null,1,1,1,null,1,1,null,null,1,null,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,null,null,null,1,1,null,1,1,null,null,1,null,null,1,1,null,1,null,null,null,1,null,1,1,null,null,1,null,1,null,null,null,null,1,null,null,1,1,null,null,1,null,1,null,1,1,1,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,null,null,1,null,1,1,1,null,null,null,null,1,null,null,1,1,null,1,null,1,null,1,1,null,1,null,1,1,null,1,null,null,1,null,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,1,1,null,null,1,null,null,1,null,null,null,1,null,1,1,1,1,null,1,null,1,null,null,1,null,null,1,null,1,null,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,1,null,1,null,1,null,1,null,1,null,null,null,null,null,null,1,null,1,1,null,1,null,1,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,1,1,null,1,null,1,null,1,null,1,1,null,1,null,1,1,null,1,null,1,null,1,1,null,1,1,null,1,null,null,1,null,null,1,1,null,1,1,null,1,null,1,null,null,null,1,null,1,null,null,1,null,null,1,1,null,1,null,1,null,null,null,1,null,1,null,1,1,null,1,null,null,1,null,null,1,null,1,null,null,1,null,1,1,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,1,null,null,null,1,null,1,null,null,1,null,1,null,null,1,null,null,null,1,null,1,1,1,null,null,null,null,null,null,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,1,null,1,null,null,1,1,1,null,1,null,1,null,null,1,null,null,1,1,1,null,1,1,1,1,null,1,null,null,1,null,null,1,1,1,null,1,null,1,1,1,null,1,null,null,1,null,null,1,null,null,1,1,1,null,1,null,null,1,1,null,null,null,null,null,null,1,null,null,1,null,1,null,1,null,null,null,1,null,1,null,1,null,null,null,1,null,1,null,null,1,null,1,1,1,null,null,1,1,null,null,1,null,null,1,1,1,null,1,null,1,null,null,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,1,null,null,1,1,null,1,1,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,1,null,null,1,null,null,1,null,1,1,1,null,1,null,null,1,null,1,1,null,null,null,1,null,null,1,null,null,1,null,1,1,null,1,1,1,null,1,null,1,null,1,1,null,1,1,null,1,1,1,1,null,1,null,null,1,1,null,1,null,1,null,null,1,null,null,1,null,1,1,1,1,null,1,1,null,1,null,null,1,null,1,null,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,1,null,1,null,1,null,1,1,1,null,1,1,null,1,null,1,null,1,1,null,null,1,null,null,1,1,null,1,null,1,null,1,1,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,null,1,null,1,1,null,null,null,null,1,null,null,1,1,null,1,1,null,1,null,1,null,1,1,1,null,1,1,null,1,null,1,null,1,null,null,1,null,1,null,null,null,1,null,1,1,1,1,1,null,1,1,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,1,null,null,1,1,null,1,1,null,null,null,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,null,1,null,1,1,null,null,1,1,null,1,null,null,1,null,null,1,1,null,1,null,null,null,1,null,1,null,null,1,null,null,1,null,null,1,1,1,null,null,1,1,1,null,1,1,null,1,null,null,1,null,1,1,null,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,1,1,1,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,null,null,null,null,null,null,null,null,null,null,null,null,1,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null],"linenum":[10,10,10,10,10,null,11,11,11,11,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,12,12,null,12,12,12,null,null,12,null,12,12,null,null,12,null,12,null,12,null,12,null,null,12,null,12,null,null,12,null,12,null,null,12,12,null,null,12,12,null,12,12,null,12,null,null,12,null,null,12,12,null,12,null,12,null,12,null,null,12,null,12,12,12,null,12,12,12,null,12,null,12,null,12,null,12,null,null,12,null,12,12,null,12,12,12,null,12,null,12,null,12,null,12,12,null,12,12,12,12,12,null,12,null,12,null,null,12,null,12,12,null,12,null,null,12,null,12,null,12,null,null,12,12,null,null,12,null,12,12,null,12,null,12,null,12,12,12,null,12,null,null,12,null,null,12,null,12,null,12,12,null,12,12,null,12,null,null,12,12,12,null,12,12,null,null,12,null,12,null,12,null,null,12,null,null,12,null,12,12,12,null,12,null,12,null,12,null,null,null,null,12,null,12,12,12,null,12,12,null,12,12,null,12,null,null,null,null,12,12,null,12,12,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,null,12,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,12,null,12,12,null,null,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,null,12,null,12,null,12,null,12,12,12,null,12,null,12,null,12,null,null,null,12,null,12,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,null,12,null,null,null,12,null,null,12,12,null,null,12,null,null,12,12,null,null,12,12,null,12,12,null,12,12,null,12,null,12,12,12,null,12,12,12,null,null,null,null,null,12,12,12,null,12,null,12,null,null,12,12,null,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,null,12,null,12,null,12,12,12,12,12,null,12,null,null,12,null,null,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,null,null,12,null,12,12,null,12,null,12,null,12,12,null,12,null,12,12,null,12,null,null,12,null,12,null,12,null,null,12,null,null,12,null,12,12,null,12,null,12,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,12,12,null,12,null,12,null,null,null,null,null,12,null,12,12,null,12,12,null,12,null,12,null,12,null,null,null,12,null,12,null,12,12,null,null,null,null,12,null,null,null,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,null,12,null,12,null,12,null,12,null,12,null,null,12,12,null,12,null,12,12,null,null,12,null,12,null,12,null,null,12,null,12,null,12,null,null,12,null,12,12,null,null,12,12,12,null,null,12,null,null,12,null,12,null,null,12,null,null,null,12,null,null,null,null,null,null,null,null,null,12,null,null,null,12,null,12,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,12,null,12,null,12,null,null,null,12,null,null,12,null,12,null,null,12,12,12,12,12,null,null,12,null,12,null,null,12,null,null,12,null,12,12,12,12,12,12,12,null,12,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,null,12,12,12,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,null,12,12,null,null,12,12,12,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,12,12,null,12,null,12,12,null,12,null,12,null,12,null,null,12,null,12,12,12,null,12,12,12,null,12,12,12,null,null,12,null,null,12,12,null,12,null,null,12,null,12,null,12,12,null,12,null,12,null,12,12,12,null,12,null,null,null,null,12,12,null,12,12,null,12,12,null,12,12,12,null,12,null,12,12,null,null,12,null,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,12,null,null,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,12,null,12,null,12,null,12,null,null,12,null,12,null,null,null,null,null,null,null,12,12,null,null,12,null,12,12,12,null,12,null,null,12,null,null,12,null,12,null,12,12,null,null,12,null,12,null,12,12,12,null,12,null,12,null,null,null,12,12,null,null,12,null,12,12,null,12,null,12,null,null,12,12,null,12,null,12,12,null,12,null,12,null,null,12,12,null,12,12,null,12,null,null,12,null,null,12,null,12,12,null,12,null,12,null,null,null,null,null,12,null,12,12,12,null,12,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,null,12,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,12,12,null,12,12,null,null,12,12,null,null,12,null,null,12,null,12,null,null,12,null,null,12,12,null,12,null,null,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,null,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,12,null,12,12,12,null,null,12,null,null,12,12,null,12,12,null,12,null,12,null,12,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,12,12,12,null,null,12,null,12,null,12,null,12,null,12,12,null,12,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,12,null,12,null,12,null,null,12,null,null,12,null,12,12,null,12,12,null,12,null,12,null,12,null,12,12,null,12,null,null,12,null,null,12,null,12,null,12,null,12,12,null,12,null,12,null,null,12,12,12,null,12,null,null,12,null,null,12,null,null,null,12,null,12,null,12,null,null,12,null,12,12,12,null,12,null,null,null,12,null,12,null,null,12,null,null,null,12,12,null,12,null,12,12,null,12,12,12,null,null,12,null,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,null,12,null,12,12,null,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,null,null,12,12,null,null,null,12,null,null,null,null,12,null,null,null,null,12,12,null,null,12,12,12,null,12,12,null,null,12,null,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,null,null,12,12,null,12,12,null,null,12,null,null,12,12,null,12,null,null,null,12,null,12,12,null,null,12,null,12,null,null,null,null,12,null,null,12,12,null,null,12,null,12,null,12,12,12,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,null,null,12,null,12,12,12,null,null,null,null,12,null,null,12,12,null,12,null,12,null,12,12,null,12,null,12,12,null,12,null,null,12,null,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,12,12,null,null,12,null,null,12,null,null,null,12,null,12,12,12,12,null,12,null,12,null,null,12,null,null,12,null,12,null,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,12,null,12,null,12,null,12,null,12,null,null,null,null,null,null,12,null,12,12,null,12,null,12,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,12,12,null,12,null,12,null,12,null,12,12,null,12,null,12,12,null,12,null,12,null,12,12,null,12,12,null,12,null,null,12,null,null,12,12,null,12,12,null,12,null,12,null,null,null,12,null,12,null,null,12,null,null,12,12,null,12,null,12,null,null,null,12,null,12,null,12,12,null,12,null,null,12,null,null,12,null,12,null,null,12,null,12,12,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,12,null,null,null,12,null,12,null,null,12,null,12,null,null,12,null,null,null,12,null,12,12,12,null,null,null,null,null,null,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,12,null,12,null,null,12,12,12,null,12,null,12,null,null,12,null,null,12,12,12,null,12,12,12,12,null,12,null,null,12,null,null,12,12,12,null,12,null,12,12,12,null,12,null,null,12,null,null,12,null,null,12,12,12,null,12,null,null,12,12,null,null,null,null,null,null,12,null,null,12,null,12,null,12,null,null,null,12,null,12,null,12,null,null,null,12,null,12,null,null,12,null,12,12,12,null,null,12,12,null,null,12,null,null,12,12,12,null,12,null,12,null,null,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,12,null,null,12,12,null,12,12,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,12,null,null,12,null,null,12,null,12,12,12,null,12,null,null,12,null,12,12,null,null,null,12,null,null,12,null,null,12,null,12,12,null,12,12,12,null,12,null,12,null,12,12,null,12,12,null,12,12,12,12,null,12,null,null,12,12,null,12,null,12,null,null,12,null,null,12,null,12,12,12,12,null,12,12,null,12,null,null,12,null,12,null,12,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,12,null,12,null,12,null,12,12,12,null,12,12,null,12,null,12,null,12,12,null,null,12,null,null,12,12,null,12,null,12,null,12,12,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,null,12,null,12,12,null,null,null,null,12,null,null,12,12,null,12,12,null,12,null,12,null,12,12,12,null,12,12,null,12,null,12,null,12,null,null,12,null,12,null,null,null,12,null,12,12,12,12,12,null,12,12,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,12,null,null,12,12,null,12,12,null,null,null,12,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,null,12,null,12,12,null,null,12,12,null,12,null,null,12,null,null,12,12,null,12,null,null,null,12,null,12,null,null,12,null,null,12,null,null,12,12,12,null,null,12,12,12,null,12,12,null,12,null,null,12,null,12,12,null,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,12,12,12,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,null,null,null,null,null,null,null,null,null,null,null,null,13,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null],"memalloc":[124.4620590209961,124.4620590209961,124.4620590209961,124.4620590209961,124.4620819091797,124.4620819091797,139.7442932128906,139.7442932128906,139.7442932128906,139.7442932128906,170.2100372314453,170.2100372314453,170.2100372314453,170.2100372314453,170.2100372314453,170.2100372314453,170.2100372314453,170.2100372314453,170.2100830078125,170.2100830078125,170.2100830078125,170.2100830078125,170.2100830078125,170.2100830078125,170.2100830078125,170.2100830078125,170.2100830078125,170.2100830078125,170.2100830078125,170.2100830078125,170.2100830078125,170.2100830078125,170.2097778320312,170.2097778320312,185.5444259643555,185.5444259643555,185.7860794067383,185.7860794067383,186.0476760864258,186.0476760864258,186.3404083251953,186.3404083251953,186.6669540405273,186.6669540405273,186.6669540405273,187.0133209228516,187.3535690307617,187.7387542724609,187.7387542724609,188.1394195556641,188.5424957275391,188.7245788574219,188.7245788574219,188.7245788574219,185.8702087402344,185.8702087402344,186.2387619018555,186.6361846923828,186.6361846923828,186.6361846923828,187.0390548706055,187.0390548706055,187.4278945922852,187.4278945922852,187.817626953125,187.817626953125,188.2124710083008,188.2124710083008,188.2124710083008,188.6045227050781,188.6045227050781,188.7942047119141,188.7942047119141,188.7942047119141,185.9997787475586,185.9997787475586,186.3503570556641,186.3503570556641,186.3503570556641,186.7200088500977,187.1191177368164,187.1191177368164,187.1191177368164,187.5122299194336,187.9087982177734,187.9087982177734,188.307487487793,188.7070236206055,188.7070236206055,188.8812408447266,188.8812408447266,188.8812408447266,186.16259765625,186.16259765625,186.16259765625,186.5246505737305,186.9123992919922,186.9123992919922,187.3163223266602,187.3163223266602,187.7192535400391,187.7192535400391,188.1198501586914,188.1198501586914,188.1198501586914,188.5211410522461,188.5211410522461,188.9625396728516,186.0840301513672,186.4362258911133,186.4362258911133,186.8060073852539,187.1907272338867,187.5847549438477,187.5847549438477,187.9770660400391,187.9770660400391,188.3637008666992,188.3637008666992,188.7409286499023,188.7409286499023,189.0509948730469,189.0509948730469,189.0509948730469,186.2604370117188,186.2604370117188,186.5962982177734,186.9576644897461,186.9576644897461,187.3320236206055,187.7183609008789,188.094352722168,188.094352722168,188.4863662719727,188.4863662719727,188.8783874511719,188.8783874511719,189.1338577270508,189.1338577270508,186.4211349487305,186.7555923461914,186.7555923461914,187.1118087768555,187.4722366333008,187.8402099609375,188.2172012329102,188.58935546875,188.58935546875,188.9744873046875,188.9744873046875,189.2152862548828,189.2152862548828,189.2152862548828,186.550407409668,186.550407409668,186.8804092407227,187.2307205200195,187.2307205200195,187.585205078125,187.585205078125,187.585205078125,187.9542083740234,187.9542083740234,188.3290252685547,188.3290252685547,188.7049026489258,188.7049026489258,188.7049026489258,189.0890655517578,189.2955474853516,189.2955474853516,189.2955474853516,186.7299880981445,186.7299880981445,187.0560531616211,187.4036026000977,187.4036026000977,187.762451171875,187.762451171875,188.1251602172852,188.1251602172852,188.5015258789062,188.8765487670898,189.268928527832,189.268928527832,189.374397277832,189.374397277832,189.374397277832,186.9099273681641,186.9099273681641,186.9099273681641,187.2481155395508,187.2481155395508,187.5998764038086,187.5998764038086,187.9624786376953,188.3435440063477,188.3435440063477,188.7303619384766,189.1190338134766,189.1190338134766,189.4520416259766,189.4520416259766,189.4520416259766,186.7975387573242,187.0893630981445,187.3927536010742,187.3927536010742,187.7174911499023,188.0556564331055,188.0556564331055,188.0556564331055,188.4016723632812,188.4016723632812,188.762451171875,188.762451171875,189.1308288574219,189.1308288574219,189.5094528198242,189.5284042358398,189.5284042358398,189.5284042358398,187.2055282592773,187.2055282592773,187.5398101806641,187.8903427124023,188.2460479736328,188.2460479736328,188.615234375,188.615234375,188.995361328125,188.995361328125,189.3777008056641,189.3777008056641,189.6035308837891,189.6035308837891,189.6035308837891,187.1859741210938,187.1859741210938,187.5038299560547,187.8398742675781,188.1907653808594,188.1907653808594,188.5486145019531,188.9159927368164,188.9159927368164,189.2907028198242,189.6738891601562,189.6738891601562,189.6774291992188,189.6774291992188,189.6774291992188,187.4285049438477,187.4285049438477,187.751091003418,188.0870666503906,188.0870666503906,188.4255447387695,188.776496887207,189.1344680786133,189.1344680786133,189.510009765625,189.510009765625,189.7502288818359,189.7502288818359,189.7502288818359,187.3395080566406,187.3395080566406,187.6418304443359,187.6418304443359,187.9610214233398,187.9610214233398,188.2916564941406,188.2916564941406,188.2916564941406,188.645378112793,188.645378112793,189.0053024291992,189.0053024291992,189.0053024291992,189.3848724365234,189.3848724365234,189.3848724365234,189.7675628662109,189.7675628662109,189.8217391967773,189.8217391967773,187.5850601196289,187.5850601196289,187.8845748901367,187.8845748901367,188.2053451538086,188.2053451538086,188.5437316894531,188.9348297119141,188.9348297119141,188.9348297119141,189.3031234741211,189.3031234741211,189.6770782470703,189.6770782470703,189.8921661376953,189.8921661376953,187.5832748413086,187.5832748413086,187.878776550293,187.878776550293,188.2001419067383,188.2001419067383,188.5387573242188,188.5387573242188,188.8885345458984,189.2510223388672,189.2510223388672,189.6279983520508,189.9615020751953,189.9615020751953,187.6048583984375,187.8796157836914,187.8796157836914,188.1815948486328,188.1815948486328,188.5065612792969,188.5065612792969,188.8564605712891,188.8564605712891,189.2209243774414,189.5924224853516,189.5924224853516,189.984260559082,189.984260559082,190.0296478271484,190.0296478271484,187.9292373657227,187.9292373657227,188.2219390869141,188.2219390869141,188.5434494018555,188.5434494018555,188.8876876831055,188.8876876831055,189.2454681396484,189.619758605957,189.619758605957,190.0053482055664,190.0053482055664,190.0967254638672,190.0967254638672,190.0967254638672,187.9963760375977,187.9963760375977,188.3140563964844,188.3140563964844,188.6369018554688,188.6369018554688,188.9777069091797,189.3356781005859,189.7062301635742,189.7062301635742,190.0902252197266,190.0902252197266,190.1626968383789,190.1626968383789,188.0830154418945,188.0830154418945,188.3648376464844,188.3648376464844,188.6747589111328,188.6747589111328,189.0127334594727,189.3712463378906,189.7358093261719,189.7358093261719,190.1139450073242,190.1139450073242,190.227653503418,190.227653503418,190.227653503418,190.227653503418,190.227653503418,190.227653503418,190.227653503418,190.227653503418,190.227653503418,190.227653503418,190.227653503418,190.227653503418,190.227653503418,190.227653503418,190.227653503418,190.227653503418,190.227653503418,190.227653503418,190.227653503418,190.227653503418,188.0920562744141,188.0920562744141,188.3255844116211,188.3255844116211,188.5578765869141,188.5578765869141,188.8060531616211,188.8060531616211,189.0957641601562,189.0957641601562,189.412467956543,189.412467956543,189.412467956543,189.7385559082031,190.0848922729492,190.0848922729492,190.0848922729492,190.2910690307617,190.2910690307617,190.2910690307617,188.1642227172852,188.4241256713867,188.4241256713867,188.4241256713867,188.7072143554688,189.0248031616211,189.0248031616211,189.3605117797852,189.7096405029297,189.7096405029297,190.0641021728516,190.353889465332,190.353889465332,188.2033309936523,188.2033309936523,188.4594116210938,188.7359771728516,189.0421371459961,189.0421371459961,189.3800582885742,189.7288055419922,190.0851593017578,190.0851593017578,190.4157638549805,190.4157638549805,190.4157638549805,188.2967681884766,188.5500106811523,188.8304901123047,189.1380310058594,189.1380310058594,189.47705078125,189.47705078125,189.8222351074219,189.8222351074219,189.8222351074219,190.2173843383789,190.4765853881836,190.4765853881836,190.4765853881836,188.4284210205078,188.4284210205078,188.6860122680664,188.6860122680664,188.973762512207,188.973762512207,189.2987289428711,189.2987289428711,189.6447601318359,190.0030975341797,190.0030975341797,190.3768463134766,190.3768463134766,190.5364074707031,190.5364074707031,190.5364074707031,188.6011428833008,188.6011428833008,188.8656005859375,188.8656005859375,189.1585235595703,189.4914779663086,189.8388519287109,190.196647644043,190.5657730102539,190.5657730102539,190.5952758789062,190.5952758789062,190.5952758789062,188.7472381591797,188.7472381591797,189.0112991333008,189.0112991333008,189.3145370483398,189.3145370483398,189.6505584716797,189.6505584716797,189.9999465942383,189.9999465942383,190.3645858764648,190.3645858764648,190.6532287597656,190.6532287597656,190.6532287597656,188.6878814697266,188.6878814697266,188.9438781738281,188.9438781738281,189.2302780151367,189.2302780151367,189.5573425292969,189.5573425292969,189.9021682739258,189.9021682739258,190.2597732543945,190.6281127929688,190.6281127929688,190.7102203369141,190.7102203369141,188.942741394043,188.942741394043,189.2154998779297,189.5300750732422,189.5300750732422,189.8740081787109,189.8740081787109,190.2337188720703,190.6073226928711,190.6073226928711,190.7663040161133,190.7663040161133,190.7663040161133,188.9662857055664,188.9662857055664,189.2324676513672,189.2324676513672,189.5383529663086,189.5383529663086,189.5383529663086,189.871940612793,189.871940612793,189.871940612793,190.223030090332,190.223030090332,190.5915298461914,190.8214721679688,190.8214721679688,188.9274139404297,188.9274139404297,189.1633911132812,189.4452285766602,189.4452285766602,189.7630157470703,189.7630157470703,190.1102752685547,190.1102752685547,190.4667816162109,190.8404312133789,190.8404312133789,190.8757553100586,190.8757553100586,189.201301574707,189.201301574707,189.4724197387695,189.4724197387695,189.7852935791016,190.126594543457,190.4680252075195,190.4680252075195,190.8268508911133,190.8268508911133,190.9291687011719,190.9291687011719,190.9291687011719,189.2500076293945,189.2500076293945,189.2500076293945,189.5100402832031,189.5100402832031,189.8073654174805,190.0985870361328,190.0985870361328,190.4306564331055,190.7706832885742,190.7706832885742,190.9816589355469,190.9816589355469,189.2305068969727,189.2305068969727,189.4772720336914,189.4772720336914,189.7613220214844,189.7613220214844,190.0862884521484,190.0862884521484,190.4347915649414,190.4347915649414,190.7942276000977,191.0333633422852,191.0333633422852,191.0333633422852,189.2658843994141,189.2658843994141,189.5069885253906,189.5069885253906,189.7791290283203,189.7791290283203,189.7791290283203,190.0899429321289,190.4270248413086,190.4270248413086,190.777229309082,190.777229309082,191.0841903686523,191.0841903686523,191.0841903686523,191.0841903686523,189.564208984375,189.564208984375,189.8272018432617,189.8272018432617,190.1192169189453,190.1192169189453,190.4490737915039,190.4490737915039,190.7893218994141,190.7893218994141,191.1342010498047,191.1342010498047,191.1342010498047,191.1342010498047,189.6059036254883,189.6059036254883,189.8482437133789,189.8482437133789,189.8482437133789,190.1362533569336,190.4635009765625,190.4635009765625,190.8056716918945,190.8056716918945,191.1634902954102,191.1834411621094,191.1834411621094,191.1834411621094,189.6370697021484,189.6370697021484,189.8853149414062,189.8853149414062,190.1715393066406,190.1715393066406,190.1715393066406,190.4935836791992,190.4935836791992,190.8341751098633,190.8341751098633,191.1854400634766,191.1854400634766,191.1854400634766,191.2318115234375,191.2318115234375,189.7187423706055,189.9706878662109,189.9706878662109,189.9706878662109,190.2600860595703,190.5815811157227,190.924919128418,190.924919128418,190.924919128418,191.2763977050781,191.2763977050781,191.2763977050781,191.2795333862305,191.2795333862305,189.8056564331055,189.8056564331055,190.050666809082,190.3794631958008,190.3794631958008,190.7079238891602,190.7079238891602,191.0432891845703,191.0432891845703,191.3263320922852,191.3263320922852,191.3263320922852,191.3263320922852,191.3263320922852,191.3263320922852,189.9241256713867,189.9241256713867,190.1720504760742,190.1720504760742,190.4713897705078,190.4713897705078,190.8046722412109,190.8046722412109,191.156135559082,191.156135559082,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,191.3724822998047,189.7846755981445,189.7846755981445,189.7846755981445,189.8520584106445,189.8520584106445,189.8520584106445,190.090202331543,190.090202331543,190.3444213867188,190.3444213867188,190.6294097900391,190.6294097900391,190.937370300293,190.937370300293,191.2462387084961,191.2462387084961,191.621711730957,191.9912872314453,191.9912872314453,192.3813705444336,192.3813705444336,192.3813705444336,192.7471160888672,193.0798110961914,193.4083099365234,193.7384262084961,194.0685882568359,194.0685882568359,194.0685882568359,194.399040222168,194.399040222168,194.6246490478516,194.6246490478516,194.6246490478516,194.6246490478516,194.6246490478516,194.6246490478516,190.2545700073242,190.2545700073242,190.5704574584961,190.9144439697266,191.2421798706055,191.5883255004883,191.9826965332031,192.3953399658203,192.8067169189453,192.8067169189453,193.2162857055664,193.6236724853516,193.6236724853516,194.0320205688477,194.0320205688477,194.4347686767578,194.4347686767578,194.756965637207,194.756965637207,194.756965637207,194.756965637207,190.4273910522461,190.7405395507812,190.7405395507812,191.0769500732422,191.0769500732422,191.0769500732422,191.3966979980469,191.7552032470703,192.144157409668,192.5386428833008,192.5386428833008,192.9339752197266,192.9339752197266,193.370735168457,193.370735168457,193.7745590209961,193.7745590209961,194.1779251098633,194.1779251098633,194.5813674926758,194.5813674926758,194.5813674926758,194.8872375488281,194.8872375488281,194.8872375488281,194.8872375488281,194.8872375488281,194.8872375488281,190.6318283081055,190.6318283081055,190.9334716796875,190.9334716796875,191.2460174560547,191.2460174560547,191.5513381958008,191.5513381958008,191.9030151367188,191.9030151367188,191.9030151367188,192.2657318115234,192.2657318115234,192.6554412841797,192.6554412841797,193.0485534667969,193.4471893310547,193.4471893310547,193.4471893310547,193.8470764160156,194.2521438598633,194.6595458984375,194.6595458984375,195.0154113769531,195.0154113769531,195.0154113769531,195.0154113769531,195.0154113769531,195.0154113769531,190.7451324462891,190.7451324462891,191.0243759155273,191.0243759155273,191.3295059204102,191.3295059204102,191.6294097900391,191.6294097900391,191.9780960083008,191.9780960083008,192.3451461791992,192.3451461791992,192.3451461791992,192.725227355957,192.725227355957,193.1154632568359,193.5094757080078,193.9012145996094,194.2941970825195,194.2941970825195,194.6982574462891,194.6982574462891,195.0882339477539,195.1414031982422,195.1414031982422,190.9217376708984,190.9217376708984,191.1970443725586,191.1970443725586,191.4937973022461,191.4937973022461,191.4937973022461,191.7940826416016,191.7940826416016,192.140754699707,192.5112533569336,192.9031982421875,192.9031982421875,193.3081970214844,193.7088088989258,194.1136322021484,194.1136322021484,194.5171203613281,194.9239807128906,195.2654800415039,195.2654800415039,195.2654800415039,195.2654800415039,195.2654800415039,195.2654800415039,191.1757965087891,191.4601440429688,191.4601440429688,191.7559967041016,191.7559967041016,191.7559967041016,192.0792007446289,192.0792007446289,192.4379272460938,192.4379272460938,192.8189544677734,193.2182312011719,193.2182312011719,193.618896484375,193.618896484375,194.0208587646484,194.0208587646484,194.4269714355469,194.8369827270508,195.234977722168,195.234977722168,195.3874740600586,195.3874740600586,195.3874740600586,191.2232513427734,191.2232513427734,191.4935531616211,191.7798767089844,191.7798767089844,192.0864181518555,192.4700241088867,192.4700241088867,192.819206237793,193.1914596557617,193.1914596557617,193.58154296875,193.9686431884766,194.35888671875,194.35888671875,194.7464599609375,194.7464599609375,195.1411056518555,195.5075225830078,195.5075225830078,195.5075225830078,195.5075225830078,195.5075225830078,195.5075225830078,191.4688415527344,191.4688415527344,191.7186050415039,191.7186050415039,191.9735107421875,191.9735107421875,192.2274932861328,192.5146942138672,192.5146942138672,192.8658447265625,192.8658447265625,193.2013549804688,193.2013549804688,193.5510406494141,193.5510406494141,193.8876724243164,193.8876724243164,194.2182006835938,194.5570831298828,194.5570831298828,194.8950500488281,194.8950500488281,194.8950500488281,195.2359771728516,195.2359771728516,195.5748596191406,195.5748596191406,195.6256484985352,195.6256484985352,191.5804290771484,191.5804290771484,191.8445129394531,191.8445129394531,192.1175537109375,192.1175537109375,192.394416809082,192.394416809082,192.6860809326172,192.6860809326172,193.0026168823242,193.0026168823242,193.3333740234375,193.6742172241211,194.0314178466797,194.0314178466797,194.3925476074219,194.3925476074219,194.7643966674805,194.7643966674805,195.1436080932617,195.1436080932617,195.1436080932617,195.526123046875,195.526123046875,195.741828918457,195.741828918457,195.741828918457,195.741828918457,195.741828918457,195.741828918457,191.9585418701172,191.9585418701172,192.2091751098633,192.4832000732422,192.4832000732422,192.4832000732422,192.834831237793,192.834831237793,193.1750793457031,193.5270843505859,193.8991088867188,193.8991088867188,194.2853393554688,194.2853393554688,194.2853393554688,194.6662979125977,194.6662979125977,194.6662979125977,195.049201965332,195.049201965332,195.4512023925781,195.4512023925781,195.8391265869141,195.8562164306641,195.8562164306641,195.8562164306641,192.0065155029297,192.0065155029297,192.2531127929688,192.2531127929688,192.5102005004883,192.8411560058594,193.171501159668,193.171501159668,193.4994659423828,193.4994659423828,193.8488693237305,193.8488693237305,194.2157592773438,194.2157592773438,194.5728073120117,194.9347229003906,194.9347229003906,194.9347229003906,195.3078155517578,195.3078155517578,195.6952743530273,195.9687347412109,195.9687347412109,195.9687347412109,195.9687347412109,192.1985931396484,192.1985931396484,192.1985931396484,192.4066543579102,192.6525421142578,192.6525421142578,192.9569931030273,192.9569931030273,193.2624816894531,193.5974655151367,193.5974655151367,193.9326934814453,193.9326934814453,194.2976455688477,194.2976455688477,194.2976455688477,194.6592712402344,195.0317001342773,195.0317001342773,195.4219589233398,195.7867279052734,195.7867279052734,196.0794143676758,196.0794143676758,196.0794143676758,196.0794143676758,196.0794143676758,196.0794143676758,192.3629608154297,192.3629608154297,192.5922241210938,192.8328857421875,192.8328857421875,193.1185607910156,193.1185607910156,193.4083023071289,193.4083023071289,193.7255935668945,193.7255935668945,194.0717697143555,194.0717697143555,194.4076232910156,194.4076232910156,194.78076171875,195.1494216918945,195.5239868164062,195.5239868164062,195.9107360839844,195.9107360839844,196.1883544921875,196.1883544921875,196.1883544921875,196.1883544921875,196.1883544921875,196.1883544921875,192.5831985473633,192.5831985473633,192.8226013183594,192.8226013183594,193.0954666137695,193.0954666137695,193.3888092041016,193.3888092041016,193.7215347290039,193.7215347290039,193.7215347290039,194.0714645385742,194.4371643066406,194.8272247314453,194.8272247314453,195.2114639282227,195.2114639282227,195.6049499511719,195.6049499511719,196.0084762573242,196.0084762573242,196.2954483032227,196.2954483032227,196.2954483032227,196.2954483032227,192.7610549926758,192.7610549926758,193.0051956176758,193.0051956176758,193.2901153564453,193.2901153564453,193.6022720336914,193.6022720336914,193.9362640380859,193.9362640380859,194.2920837402344,194.2920837402344,194.6722183227539,195.0624771118164,195.4655456542969,195.8721160888672,195.8721160888672,196.2707366943359,196.4009399414062,196.4009399414062,196.4009399414062,192.7820358276367,193.0195846557617,193.0195846557617,193.2779235839844,193.5967330932617,193.5967330932617,193.5967330932617,193.910285949707,193.910285949707,194.2496643066406,194.2496643066406,194.2496643066406,194.6050033569336,194.6050033569336,194.9795150756836,195.361701965332,195.7485733032227,195.7485733032227,196.1414794921875,196.1414794921875,196.5045700073242,196.5045700073242,196.5045700073242,196.5045700073242,196.5045700073242,196.5045700073242,193.0057907104492,193.0057907104492,193.2310943603516,193.2310943603516,193.4878692626953,193.4878692626953,193.763313293457,193.763313293457,194.0700302124023,194.0700302124023,194.4067687988281,194.4067687988281,194.7560119628906,194.7560119628906,195.1226043701172,195.4912719726562,195.4912719726562,195.8781967163086,195.8781967163086,196.2693099975586,196.2693099975586,196.6066665649414,196.6066665649414,196.6066665649414,196.6066665649414,193.1774444580078,193.1774444580078,193.4069671630859,193.6631622314453,193.6631622314453,193.9427108764648,193.9427108764648,194.28857421875,194.28857421875,194.6285247802734,194.6285247802734,194.9885330200195,194.9885330200195,195.365348815918,195.7471160888672,195.7471160888672,196.1302490234375,196.5212173461914,196.7070236206055,196.7070236206055,196.7070236206055,196.7070236206055,196.7070236206055,196.7070236206055,193.3652267456055,193.5948715209961,193.5948715209961,193.8414688110352,194.1127090454102,194.1127090454102,194.4326400756836,194.4326400756836,194.7086029052734,194.7086029052734,195.0445404052734,195.4073486328125,195.4073486328125,195.7244338989258,195.7244338989258,196.074577331543,196.4505920410156,196.4505920410156,196.7955627441406,196.7955627441406,196.8058624267578,196.8058624267578,193.4143371582031,193.4143371582031,193.6397018432617,193.6397018432617,193.8537139892578,194.1073532104492,194.3936538696289,194.6902389526367,194.6902389526367,194.6902389526367,195.0278396606445,195.0278396606445,195.3880767822266,195.3880767822266,195.7287139892578,195.7287139892578,196.0554275512695,196.0554275512695,196.4173126220703,196.7903060913086,196.7903060913086,196.9029846191406,196.9029846191406,196.9029846191406,196.9029846191406,196.9029846191406,196.9029846191406,196.9029846191406,196.9029846191406,196.9029846191406,196.9029846191406,196.9029846191406,196.9029846191406,196.9029846191406,196.9029846191406,196.9029846191406,196.9029846191406,196.9029846191406,196.9029846191406,196.9029846191406,196.9029846191406,196.9029846191406,196.9029846191406,196.9029846191406,196.9029846191406,196.9029846191406,196.9029846191406,196.9029846191406,196.9029846191406,196.9029846191406,196.9029846191406,196.9029846191406,196.9029846191406,196.9029846191406,196.9029846191406,196.9029846191406,196.9029846191406,196.9029846191406,196.9029846191406,196.9029846191406,196.9029846191406,196.9029846191406,196.9029846191406,196.9029846191406,196.9029846191406,196.9029846191406,193.5628356933594,193.5628356933594,193.7379608154297,193.7379608154297,193.9462661743164,193.9462661743164,194.1702270507812,194.1702270507812,194.4067001342773,194.4067001342773,194.6699295043945,194.6699295043945,194.9628219604492,194.9628219604492,194.9628219604492,195.2746429443359,195.2746429443359,195.5964660644531,195.5964660644531,195.9418869018555,196.3591079711914,196.3591079711914,196.7396545410156,196.7396545410156,196.9983596801758,196.9983596801758,196.9983596801758,196.9983596801758,196.9983596801758,196.9983596801758,193.8375701904297,193.8375701904297,194.0684432983398,194.3239898681641,194.3239898681641,194.6041259765625,194.9096221923828,194.9096221923828,195.2426071166992,195.2426071166992,195.5892105102539,195.5892105102539,195.948371887207,195.948371887207,196.3217849731445,196.7196044921875,196.7196044921875,197.0924835205078,197.0924835205078,197.0924835205078,197.0924835205078,197.0924835205078,197.0924835205078,193.9415740966797,193.9415740966797,194.1717910766602,194.1717910766602,194.4232025146484,194.4232025146484,194.7027969360352,195.0203323364258,195.0203323364258,195.3618087768555,195.3618087768555,195.7120971679688,195.7120971679688,195.7120971679688,196.0749435424805,196.4554443359375,196.852653503418,196.852653503418,197.1850204467773,197.1850204467773,197.1850204467773,197.1850204467773,197.1850204467773,197.1850204467773,194.1305999755859,194.1305999755859,194.363151550293,194.363151550293,194.6220855712891,194.6220855712891,194.9098663330078,194.9098663330078,195.2248687744141,195.2248687744141,195.2248687744141,195.5591278076172,195.5591278076172,195.9066619873047,196.2587509155273,196.6309509277344,196.6309509277344,197.0173645019531,197.0173645019531,197.2761306762695,197.2761306762695,197.2761306762695,197.2761306762695,194.26123046875,194.26123046875,194.26123046875,194.4892044067383,194.4892044067383,194.7383270263672,194.7383270263672,195.0183334350586,195.3298797607422,195.3298797607422,195.6643142700195,195.6643142700195,196.0127639770508,196.3702545166016,196.3702545166016,196.7447204589844,197.1373291015625,197.3657455444336,197.3657455444336,197.3657455444336,197.3657455444336,197.3657455444336,197.3657455444336,194.4182586669922,194.4182586669922,194.6509399414062,194.6509399414062,194.9079666137695,195.1935729980469,195.1935729980469,195.5497894287109,195.5497894287109,195.8873596191406,195.8873596191406,196.2367324829102,196.2367324829102,196.6025390625,196.9802474975586,196.9802474975586,197.3744049072266,197.4539489746094,197.4539489746094,197.4539489746094,197.4539489746094,194.6408386230469,194.6408386230469,194.8770980834961,194.8770980834961,195.1423721313477,195.1423721313477,195.4424438476562,195.4424438476562,195.4424438476562,195.7761688232422,195.7761688232422,196.1217346191406,196.1217346191406,196.4815979003906,196.4815979003906,196.8576507568359,196.8576507568359,197.2483062744141,197.5406723022461,197.5406723022461,197.5406723022461,197.5406723022461,194.6735992431641,194.6735992431641,194.9045104980469,194.9045104980469,195.158447265625,195.158447265625,195.158447265625,195.4449844360352,195.4449844360352,195.7669906616211,195.7669906616211,196.1136779785156,196.4657135009766,196.4657135009766,196.8363189697266,197.2295989990234,197.2295989990234,197.2295989990234,197.6260833740234,197.6260833740234,197.6260833740234,197.6260833740234,194.7646560668945,194.7646560668945,194.9929275512695,194.9929275512695,195.2461776733398,195.5330047607422,195.5330047607422,195.8544769287109,195.8544769287109,196.1921234130859,196.1921234130859,196.5365753173828,196.5365753173828,196.9030151367188,197.2823867797852,197.2823867797852,197.6749038696289,197.6749038696289,197.7100067138672,197.7100067138672,197.7100067138672,194.8253860473633,194.8253860473633,195.0401840209961,195.0401840209961,195.2683181762695,195.2683181762695,195.5227890014648,195.8410949707031,196.1660385131836,196.1660385131836,196.1660385131836,196.4976119995117,196.824821472168,197.1623611450195,197.1623611450195,197.5117340087891,197.7926864624023,197.7926864624023,197.7926864624023,197.7926864624023,197.7926864624023,197.7926864624023,195.0251083374023,195.0251083374023,195.2447509765625,195.2447509765625,195.474739074707,195.7420349121094,195.7420349121094,196.0372467041016,196.0372467041016,196.3588333129883,196.3588333129883,196.7009048461914,196.7009048461914,197.0438919067383,197.0438919067383,197.4059219360352,197.4059219360352,197.78955078125,197.78955078125,197.873908996582,197.873908996582,197.873908996582,197.873908996582,197.873908996582,197.873908996582,195.291618347168,195.291618347168,195.5209655761719,195.5209655761719,195.7821807861328,195.7821807861328,196.0769805908203,196.0769805908203,196.4046249389648,196.4046249389648,196.7487487792969,196.7487487792969,197.1041107177734,197.4762268066406,197.4762268066406,197.8698196411133,197.9538879394531,197.9538879394531,197.9538879394531,197.9538879394531,197.9538879394531,197.9538879394531,195.4032440185547,195.6332397460938,195.6332397460938,195.91015625,195.91015625,196.2019958496094,196.2019958496094,196.5225296020508,196.5225296020508,196.8429489135742,197.1786651611328,197.1786651611328,197.1786651611328,197.5262756347656,197.5262756347656,197.8865356445312,197.8865356445312,198.0325241088867,198.0325241088867,198.0325241088867,198.0325241088867,198.0325241088867,198.0325241088867,195.4607238769531,195.6798553466797,195.6798553466797,195.6798553466797,195.9195327758789,195.9195327758789,196.1929702758789,196.1929702758789,196.504280090332,196.8703155517578,197.21435546875,197.554443359375,197.554443359375,197.8972015380859,197.8972015380859,198.1099319458008,198.1099319458008,198.1099319458008,198.1099319458008,195.5084686279297,195.5084686279297,195.7213973999023,195.9519119262695,195.9519119262695,196.2251434326172,196.2251434326172,196.5115280151367,196.5115280151367,196.828239440918,196.828239440918,197.154914855957,197.4941558837891,197.8416213989258,197.8416213989258,198.1860733032227,198.1860733032227,198.1860733032227,198.1860733032227,198.1860733032227,198.1860733032227,195.5784149169922,195.7925643920898,195.7925643920898,196.0219268798828,196.0219268798828,196.3005447387695,196.3005447387695,196.5983963012695,196.9166641235352,196.9166641235352,197.2486419677734,197.2486419677734,197.5956268310547,197.9524917602539,197.9524917602539,198.2610015869141,198.2610015869141,198.2610015869141,198.2610015869141,198.2610015869141,198.2610015869141,195.7209625244141,195.7209625244141,195.9508438110352,195.9508438110352,196.2030410766602,196.2030410766602,196.4939193725586,196.8166198730469,196.8166198730469,197.1572189331055,197.1572189331055,197.5043716430664,197.5043716430664,197.87060546875,198.2458724975586,198.3347091674805,198.3347091674805,198.3347091674805,198.3347091674805,198.3347091674805,198.3347091674805,195.9970703125,195.9970703125,196.2271041870117,196.2271041870117,196.4855728149414,196.4855728149414,196.7789077758789,197.1073379516602,197.4512710571289,197.8014526367188,197.8014526367188,198.1657562255859,198.1657562255859,198.4072189331055,198.4072189331055,198.4072189331055,198.4072189331055,198.4072189331055,198.4072189331055,196.0466690063477,196.0466690063477,196.2711563110352,196.2711563110352,196.5130844116211,196.7832107543945,197.083381652832,197.083381652832,197.4150466918945,197.4150466918945,197.7598648071289,197.7598648071289,198.1225509643555,198.1225509643555,198.4785919189453,198.4785919189453,198.4785919189453,198.4785919189453,196.0569076538086,196.0569076538086,196.2757263183594,196.2757263183594,196.5094757080078,196.5094757080078,196.7751998901367,197.0644912719727,197.3915786743164,197.3915786743164,197.7341537475586,197.7341537475586,198.0791168212891,198.0791168212891,198.4457244873047,198.4457244873047,198.5487060546875,198.5487060546875,198.5487060546875,198.5487060546875,198.5487060546875,198.5487060546875,196.3036575317383,196.5297775268555,196.5297775268555,196.7791976928711,197.0699615478516,197.0699615478516,197.3910140991211,197.3910140991211,197.7346649169922,198.0853729248047,198.0853729248047,198.4452743530273,198.4452743530273,198.6178131103516,198.6178131103516,198.6178131103516,198.6178131103516,198.6178131103516,198.6178131103516,198.6178131103516,198.6178131103516,198.6178131103516,198.6178131103516,198.6178131103516,198.6178131103516,198.6178131103516,198.6178131103516,198.6178131103516,198.6178131103516,198.6178131103516,198.6178131103516,198.6178131103516,198.6178131103516,198.6178131103516,198.6178131103516,198.6178131103516,198.6178131103516,198.6178131103516,198.6178131103516,198.6178131103516,198.6178131103516,198.6178131103516,198.6178131103516,198.6178131103516,198.6178131103516,198.6178131103516,196.2943649291992,196.2943649291992,196.4782028198242,196.4782028198242,196.7139358520508,196.9488296508789,197.2124481201172,197.2124481201172,197.5047378540039,197.5047378540039,197.8300933837891,197.8300933837891,198.1726226806641,198.1726226806641,198.5292358398438,198.685432434082,198.685432434082,198.685432434082,198.685432434082,196.4834899902344,196.7122650146484,196.7122650146484,196.9626617431641,196.9626617431641,197.2381439208984,197.2381439208984,197.5495147705078,197.8710861206055,197.8710861206055,198.2047424316406,198.5600662231445,198.5600662231445,198.7523422241211,198.7523422241211,198.7523422241211,198.7523422241211,198.7523422241211,198.7523422241211,196.5500946044922,196.777702331543,196.777702331543,197.0007858276367,197.2658615112305,197.2658615112305,197.5729598999023,197.5729598999023,197.9149856567383,197.9149856567383,198.2463073730469,198.2463073730469,198.5983200073242,198.5983200073242,198.8181381225586,198.8181381225586,198.8181381225586,198.8181381225586,198.8181381225586,198.8181381225586,196.5979309082031,196.8205413818359,196.8205413818359,197.0345687866211,197.0345687866211,197.2925643920898,197.2925643920898,197.5869903564453,197.5869903564453,197.8596572875977,197.8596572875977,198.1850051879883,198.1850051879883,198.5221557617188,198.8611145019531,198.8611145019531,198.8828735351562,198.8828735351562,198.8828735351562,198.8828735351562,198.8828735351562,198.8828735351562,196.8112640380859,196.8112640380859,197.025032043457,197.025032043457,197.025032043457,197.262939453125,197.262939453125,197.5404357910156,197.8354110717773,198.1929626464844,198.1929626464844,198.5313491821289,198.8741607666016,198.8741607666016,198.9465255737305,198.9465255737305,198.9465255737305,198.9465255737305,196.8892517089844,196.8892517089844,197.1020889282227,197.1020889282227,197.3274002075195,197.3274002075195,197.5995788574219,197.5995788574219,197.8876953125,197.8876953125,198.1925354003906,198.1925354003906,198.1925354003906,198.5335235595703,198.8604049682617,198.8604049682617,199.0092315673828,199.0092315673828,199.0092315673828,199.0092315673828,196.9325180053711,196.9325180053711,196.9325180053711,197.1490631103516,197.1490631103516,197.383659362793,197.383659362793,197.383659362793,197.6530151367188,197.6530151367188,197.9592361450195,197.9592361450195,198.2959823608398,198.2959823608398,198.6421508789062,199.0058670043945,199.0708618164062,199.0708618164062,199.0708618164062,199.0708618164062,199.0708618164062,199.0708618164062,197.1483535766602,197.1483535766602,197.3795166015625,197.3795166015625,197.6409759521484,197.6409759521484,197.9401168823242,197.9401168823242,198.272346496582,198.6225509643555,198.6225509643555,198.9852523803711,198.9852523803711,199.1314849853516,199.1314849853516,199.1314849853516,199.1314849853516,197.1769638061523,197.405891418457,197.405891418457,197.6618804931641,197.6618804931641,197.6618804931641,197.9556045532227,198.284797668457,198.6340637207031,198.6340637207031,198.993034362793,198.993034362793,199.1911697387695,199.1911697387695,199.1911697387695,199.1911697387695,199.1911697387695,199.1911697387695,197.2335815429688,197.4602355957031,197.7011413574219,197.7011413574219,197.9803466796875,198.292350769043,198.666389465332,199.0175323486328,199.0175323486328,199.249870300293,199.249870300293,199.249870300293,199.249870300293,199.249870300293,199.249870300293,197.2717437744141,197.4893341064453,197.7255172729492,197.7255172729492,197.9901428222656,197.9901428222656,198.2923126220703,198.6258926391602,198.9732818603516,198.9732818603516,199.3076095581055,199.3076095581055,199.3076095581055,199.3076095581055,199.3076095581055,199.3076095581055,199.3076095581055,199.3076095581055,199.3076095581055,197.4867172241211,197.7098541259766,197.9618530273438,197.9618530273438,198.2427978515625,198.2427978515625,198.2427978515625,198.5606307983398,198.8976974487305,198.8976974487305,199.2437362670898,199.2437362670898,199.3644409179688,199.3644409179688,199.3644409179688,199.3644409179688,199.3644409179688,199.3644409179688,197.5291595458984,197.5291595458984,197.7523498535156,197.7523498535156,197.9950714111328,197.9950714111328,198.2773895263672,198.2773895263672,198.5909652709961,198.5909652709961,198.9343566894531,198.9343566894531,199.2872543334961,199.2872543334961,199.4203186035156,199.4203186035156,199.4203186035156,199.4203186035156,197.601318359375,197.601318359375,197.8248977661133,198.0722503662109,198.0722503662109,198.3550109863281,198.6756057739258,199.0238952636719,199.0238952636719,199.0238952636719,199.379020690918,199.4753723144531,199.4753723144531,199.4753723144531,199.4753723144531,199.4753723144531,199.4753723144531,197.7292633056641,197.9568557739258,198.2105255126953,198.2105255126953,198.5058517456055,198.5058517456055,198.8354187011719,198.8354187011719,198.8354187011719,199.1895217895508,199.1895217895508,199.529426574707,199.529426574707,199.529426574707,199.529426574707,199.529426574707,199.529426574707,199.529426574707,199.529426574707,199.529426574707,199.529426574707,199.529426574707,199.529426574707,199.529426574707,199.529426574707,199.529426574707,199.529426574707,199.529426574707,199.529426574707,199.529426574707,199.529426574707,199.529426574707,197.7179718017578,197.9262237548828,197.9262237548828,197.9262237548828,198.158935546875,198.4136734008789,198.4136734008789,198.6925582885742,199.0122756958008,199.3494873046875,199.3494873046875,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,199.5826950073242,197.7499771118164,197.7499771118164,197.7499771118164,197.7499771118164,197.7499771118164,197.7499771118164,197.8474197387695,198.0935821533203,198.0935821533203,198.3508529663086,198.3508529663086,198.6422576904297,198.6422576904297,198.9586563110352,198.9586563110352,199.3095932006836,199.3095932006836,199.6264038085938,199.976936340332,199.976936340332,200.3652954101562,200.3652954101562,200.7635879516602,200.7635879516602,201.1080627441406,201.1080627441406,201.4354019165039,201.7601547241211,201.7601547241211,201.7601547241211,202.0888061523438,202.0888061523438,202.0888061523438,202.4148178100586,202.4148178100586,202.7430267333984,203.0702896118164,203.3978500366211,203.3978500366211,203.7281265258789,203.7281265258789,204.0544662475586,204.3806915283203,204.3806915283203,204.7087097167969,205.0345458984375,205.0345458984375,205.3639373779297,205.3639373779297,205.3968811035156,205.3968811035156,205.3968811035156,205.3968811035156,205.3968811035156,205.3968811035156,198.1960601806641,198.1960601806641,198.4454650878906,198.7151031494141,198.7151031494141,199.0139389038086,199.3242492675781,199.6307983398438,199.6307983398438,199.9751968383789,199.9751968383789,200.3356246948242,200.3356246948242,200.71728515625,201.1170806884766,201.1170806884766,201.5217361450195,201.9323425292969,201.9323425292969,202.3412857055664,202.7484893798828,203.154296875,203.5631561279297,203.5631561279297,203.9694366455078,203.9694366455078,204.3725204467773,204.7772750854492,205.1800079345703,205.1800079345703,205.5706634521484,205.5706634521484,205.6060638427734,205.6060638427734,205.6060638427734,205.6060638427734,205.6060638427734,205.6060638427734,198.5322189331055,198.5322189331055,198.7850570678711,199.0637130737305,199.3738479614258,199.6889343261719,199.6889343261719,200.0189056396484,200.3819580078125,200.3819580078125,200.7553253173828,200.7553253173828,201.1519546508789,201.5475769042969,201.5475769042969,201.9441909790039,201.9441909790039,202.3464126586914,202.7470245361328,203.1459884643555,203.1459884643555,203.5466003417969,203.5466003417969,203.9492034912109,203.9492034912109,204.3501052856445,204.3501052856445,204.7525405883789,204.7525405883789,205.1548385620117,205.1548385620117,205.5412521362305,205.5412521362305,205.8118209838867,205.8118209838867,205.8118209838867,205.8118209838867,205.8118209838867,205.8118209838867,205.8118209838867,205.8118209838867,205.8118209838867,198.8852386474609,199.1317138671875,199.1317138671875,199.3975601196289,199.3975601196289,199.6883392333984,199.6883392333984,199.9824905395508,200.3146667480469,200.6666641235352,200.6666641235352,201.0211944580078,201.3957061767578,201.3957061767578,201.7781295776367,201.7781295776367,202.2113342285156,202.2113342285156,202.6026992797852,202.9964218139648,202.9964218139648,202.9964218139648,203.3951110839844,203.3951110839844,203.3951110839844,203.7921371459961,204.1961441040039,204.1961441040039,204.5934219360352,204.5934219360352,204.9981231689453,204.9981231689453,205.4034729003906,205.7951354980469,205.7951354980469,206.0142517089844,206.0142517089844,206.0142517089844,206.0142517089844,206.0142517089844,206.0142517089844,206.0142517089844,206.0142517089844,206.0142517089844,199.2095947265625,199.2095947265625,199.4592971801758,199.4592971801758,199.7223358154297,199.7223358154297,200.0001373291016,200.0001373291016,200.0001373291016,200.2867050170898,200.2867050170898,200.6213912963867,200.9743881225586,200.9743881225586,201.3283462524414,201.3283462524414,201.7004318237305,202.087776184082,202.087776184082,202.087776184082,202.5202713012695,202.9100494384766,202.9100494384766,203.302001953125,203.6909637451172,203.6909637451172,204.0885543823242,204.0885543823242,204.4891815185547,204.4891815185547,204.8850173950195,205.2875595092773,205.6897506713867,205.6897506713867,206.0786056518555,206.2134399414062,206.2134399414062,206.2134399414062,206.2134399414062,206.2134399414062,206.2134399414062,199.5500640869141,199.5500640869141,199.5500640869141,199.7958831787109,199.7958831787109,200.085090637207,200.085090637207,200.3523178100586,200.3523178100586,200.6586837768555,200.6586837768555,201.0016326904297,201.3533477783203,201.7106628417969,202.0815887451172,202.465934753418,202.465934753418,202.8515090942383,203.2392349243164,203.6325302124023,203.6325302124023,204.0313339233398,204.0313339233398,204.4329986572266,204.837646484375,204.837646484375,205.2451248168945,205.2451248168945,205.65380859375,205.65380859375,206.0530624389648,206.0530624389648,206.409423828125,206.409423828125,206.409423828125,206.409423828125,206.409423828125,206.409423828125,206.409423828125,206.409423828125,206.409423828125,199.7409973144531,199.7409973144531,200.0082702636719,200.0082702636719,200.0082702636719,200.2623519897461,200.2623519897461,200.5262603759766,200.5262603759766,200.8191833496094,200.8191833496094,201.1491928100586,201.1491928100586,201.494026184082,201.494026184082,201.8430252075195,201.8430252075195,202.197380065918,202.564582824707,202.9422302246094,202.9422302246094,202.9422302246094,203.3331680297852,203.7178268432617,203.7178268432617,204.1099700927734,204.5139923095703,204.5139923095703,204.9101867675781,204.9101867675781,205.307975769043,205.7065505981445,206.1043014526367,206.1043014526367,206.4959487915039,206.4959487915039,206.6022567749023,206.6022567749023,206.6022567749023,206.6022567749023,206.6022567749023,206.6022567749023,206.6022567749023,206.6022567749023,206.6022567749023,206.6022567749023,206.6022567749023,206.6022567749023,206.6022567749023,206.6022567749023,206.6022567749023,206.6022567749023,199.9676132202148,199.9676132202148,199.9676132202148,199.9676132202148,200.1213836669922,200.1213836669922,200.3603744506836,200.3603744506836,200.6032562255859,200.6032562255859,200.8497619628906,201.1451263427734,201.1451263427734,201.4722518920898,201.7973556518555,201.7973556518555,202.1417922973633,202.520149230957,202.520149230957,202.9176940917969,203.3222885131836,203.7234039306641,203.7234039306641,204.1227645874023,204.1227645874023,204.1227645874023,204.524787902832,204.524787902832,204.524787902832,204.9287033081055,205.3328247070312,205.3328247070312,205.7397918701172,205.7397918701172,206.1468734741211,206.1468734741211,206.5534362792969,206.5534362792969,206.7919158935547,206.7919158935547,206.7919158935547,206.7919158935547,206.7919158935547,206.7919158935547,206.7919158935547,206.7919158935547,206.7919158935547,200.4041748046875,200.6455078125,200.8874130249023,200.8874130249023,201.1426315307617,201.4473724365234,201.7769165039062,202.1137619018555,202.1137619018555,202.5017395019531,202.8534469604492,202.8534469604492,203.2205123901367,203.2205123901367,203.2205123901367,203.6027450561523,203.6027450561523,203.9884414672852,204.3823394775391,204.3823394775391,204.3823394775391,204.7790679931641,204.7790679931641,205.1837158203125,205.1837158203125,205.5907135009766,205.5907135009766,205.9988708496094,205.9988708496094,206.4051055908203,206.8107299804688,206.8107299804688,206.9785537719727,206.9785537719727,206.9785537719727,206.9785537719727,206.9785537719727,206.9785537719727,200.7221450805664,200.7221450805664,200.9584732055664,200.9584732055664,201.1952133178711,201.1952133178711,201.4625091552734,201.7718200683594,201.7718200683594,202.1378479003906,202.480094909668,202.8262100219727,203.1879196166992,203.1879196166992,203.5595932006836,203.5595932006836,203.5595932006836,203.9426422119141,203.9426422119141,203.9426422119141,204.3317108154297,204.3317108154297,212.2343444824219,212.2343444824219,212.2343444824219,212.2343444824219,212.2343444824219,212.2343444824219,212.2343444824219,212.2343444824219,212.2343444824219,212.2343444824219,212.2343444824219,212.2343444824219,212.2343444824219,212.2343444824219,212.2343444824219,212.2343444824219,212.2343444824219,212.2343444824219,212.2343444824219,212.2343444824219,212.2343444824219,212.2343444824219,219.8637390136719,219.8637466430664,219.8637466430664,219.8637466430664,219.8637466430664,219.8637466430664,219.8637466430664,219.8637466430664,219.8637466430664,219.8637466430664,219.8637466430664,219.8637466430664,219.8637466430664,219.8637466430664,219.8637466430664,219.8637466430664,219.8637466430664,219.8637466430664,219.8637466430664,219.8637466430664,219.8637466430664,219.8637466430664,219.8637466430664,235.1225357055664,235.1225357055664,235.1225357055664,235.1225357055664,235.1225357055664,235.1225357055664,235.1225357055664,235.1225357055664,235.1225357055664,235.1225357055664,235.1225357055664,235.1225357055664,235.1225357055664,235.1225357055664,235.1225357055664,235.1225357055664,235.1225357055664,235.1225357055664,235.1225357055664,235.1225357055664,242.8118286132812,242.8118286132812,242.8118286132812,242.8118286132812,242.8118286132812,242.8118286132812,242.8118286132812,242.8118286132812,242.8118286132812,242.8118286132812,242.8118286132812,242.8118286132812,242.8118286132812,242.8118286132812,242.8118286132812,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242,258.1471481323242],"meminc":[0,0,0,0,2.288818359375e-05,0,15.28221130371094,0,0,0,30.46574401855469,0,0,0,0,0,0,0,4.57763671875e-05,0,0,0,0,0,0,0,0,0,0,0,0,0,-0.00030517578125,0,15.33464813232422,0,0.2416534423828125,0,0.2615966796875,0,0.2927322387695312,0,0.3265457153320312,0,0,0.3463668823242188,0.3402481079101562,0.3851852416992188,0,0.400665283203125,0.403076171875,0.1820831298828125,0,0,-2.8543701171875,0,0.3685531616210938,0.3974227905273438,0,0,0.4028701782226562,0,0.3888397216796875,0,0.3897323608398438,0,0.3948440551757812,0,0,0.3920516967773438,0,0.1896820068359375,0,0,-2.794425964355469,0,0.3505783081054688,0,0,0.3696517944335938,0.39910888671875,0,0,0.3931121826171875,0.3965682983398438,0,0.3986892700195312,0.3995361328125,0,0.1742172241210938,0,0,-2.718643188476562,0,0,0.3620529174804688,0.3877487182617188,0,0.4039230346679688,0,0.4029312133789062,0,0.4005966186523438,0,0,0.4012908935546875,0,0.4413986206054688,-2.878509521484375,0.3521957397460938,0,0.369781494140625,0.3847198486328125,0.3940277099609375,0,0.3923110961914062,0,0.3866348266601562,0,0.377227783203125,0,0.3100662231445312,0,0,-2.790557861328125,0,0.3358612060546875,0.3613662719726562,0,0.374359130859375,0.3863372802734375,0.3759918212890625,0,0.3920135498046875,0,0.3920211791992188,0,0.2554702758789062,0,-2.712722778320312,0.3344573974609375,0,0.3562164306640625,0.3604278564453125,0.3679733276367188,0.3769912719726562,0.3721542358398438,0,0.3851318359375,0,0.2407989501953125,0,0,-2.664878845214844,0,0.3300018310546875,0.350311279296875,0,0.3544845581054688,0,0,0.3690032958984375,0,0.37481689453125,0,0.3758773803710938,0,0,0.3841629028320312,0.20648193359375,0,0,-2.565559387207031,0,0.3260650634765625,0.3475494384765625,0,0.3588485717773438,0,0.3627090454101562,0,0.3763656616210938,0.3750228881835938,0.3923797607421875,0,0.10546875,0,0,-2.464469909667969,0,0,0.3381881713867188,0,0.3517608642578125,0,0.3626022338867188,0.3810653686523438,0,0.3868179321289062,0.388671875,0,0.3330078125,0,0,-2.654502868652344,0.2918243408203125,0.3033905029296875,0,0.324737548828125,0.338165283203125,0,0,0.3460159301757812,0,0.36077880859375,0,0.368377685546875,0,0.3786239624023438,0.018951416015625,0,0,-2.3228759765625,0,0.3342819213867188,0.3505325317382812,0.3557052612304688,0,0.3691864013671875,0,0.380126953125,0,0.3823394775390625,0,0.225830078125,0,0,-2.417556762695312,0,0.3178558349609375,0.3360443115234375,0.35089111328125,0,0.35784912109375,0.3673782348632812,0,0.3747100830078125,0.3831863403320312,0,0.0035400390625,0,0,-2.248924255371094,0,0.3225860595703125,0.3359756469726562,0,0.3384780883789062,0.3509521484375,0.35797119140625,0,0.3755416870117188,0,0.2402191162109375,0,0,-2.410720825195312,0,0.3023223876953125,0,0.3191909790039062,0,0.3306350708007812,0,0,0.3537216186523438,0,0.35992431640625,0,0,0.3795700073242188,0,0,0.3826904296875,0,0.05417633056640625,0,-2.236679077148438,0,0.2995147705078125,0,0.320770263671875,0,0.3383865356445312,0.3910980224609375,0,0,0.3682937622070312,0,0.3739547729492188,0,0.215087890625,0,-2.308891296386719,0,0.295501708984375,0,0.3213653564453125,0,0.3386154174804688,0,0.3497772216796875,0.36248779296875,0,0.3769760131835938,0.3335037231445312,0,-2.356643676757812,0.2747573852539062,0,0.3019790649414062,0,0.3249664306640625,0,0.3498992919921875,0,0.3644638061523438,0.3714981079101562,0,0.3918380737304688,0,0.04538726806640625,0,-2.100410461425781,0,0.2927017211914062,0,0.3215103149414062,0,0.34423828125,0,0.3577804565429688,0.3742904663085938,0,0.385589599609375,0,0.09137725830078125,0,0,-2.100349426269531,0,0.3176803588867188,0,0.322845458984375,0,0.3408050537109375,0.35797119140625,0.3705520629882812,0,0.3839950561523438,0,0.07247161865234375,0,-2.079681396484375,0,0.2818222045898438,0,0.3099212646484375,0,0.3379745483398438,0.3585128784179688,0.36456298828125,0,0.3781356811523438,0,0.11370849609375,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2.135597229003906,0,0.2335281372070312,0,0.2322921752929688,0,0.2481765747070312,0,0.2897109985351562,0,0.3167037963867188,0,0,0.3260879516601562,0.3463363647460938,0,0,0.2061767578125,0,0,-2.126846313476562,0.2599029541015625,0,0,0.2830886840820312,0.3175888061523438,0,0.3357086181640625,0.3491287231445312,0,0.354461669921875,0.2897872924804688,0,-2.150558471679688,0,0.2560806274414062,0.2765655517578125,0.3061599731445312,0,0.337921142578125,0.3487472534179688,0.356353759765625,0,0.3306045532226562,0,0,-2.118995666503906,0.2532424926757812,0.2804794311523438,0.3075408935546875,0,0.339019775390625,0,0.345184326171875,0,0,0.3951492309570312,0.2592010498046875,0,0,-2.048164367675781,0,0.2575912475585938,0,0.287750244140625,0,0.3249664306640625,0,0.3460311889648438,0.35833740234375,0,0.373748779296875,0,0.1595611572265625,0,0,-1.935264587402344,0,0.2644577026367188,0,0.2929229736328125,0.3329544067382812,0.3473739624023438,0.3577957153320312,0.3691253662109375,0,0.02950286865234375,0,0,-1.848037719726562,0,0.2640609741210938,0,0.3032379150390625,0,0.3360214233398438,0,0.3493881225585938,0,0.3646392822265625,0,0.2886428833007812,0,0,-1.965347290039062,0,0.2559967041015625,0,0.2863998413085938,0,0.3270645141601562,0,0.3448257446289062,0,0.35760498046875,0.3683395385742188,0,0.0821075439453125,0,-1.767478942871094,0,0.2727584838867188,0.3145751953125,0,0.34393310546875,0,0.359710693359375,0.3736038208007812,0,0.1589813232421875,0,0,-1.800018310546875,0,0.2661819458007812,0,0.3058853149414062,0,0,0.333587646484375,0,0,0.3510894775390625,0,0.368499755859375,0.2299423217773438,0,-1.894058227539062,0,0.2359771728515625,0.2818374633789062,0,0.3177871704101562,0,0.347259521484375,0,0.35650634765625,0.3736495971679688,0,0.0353240966796875,0,-1.674453735351562,0,0.2711181640625,0,0.3128738403320312,0.3413009643554688,0.3414306640625,0,0.35882568359375,0,0.1023178100585938,0,0,-1.679161071777344,0,0,0.2600326538085938,0,0.2973251342773438,0.2912216186523438,0,0.3320693969726562,0.34002685546875,0,0.2109756469726562,0,-1.751152038574219,0,0.24676513671875,0,0.2840499877929688,0,0.3249664306640625,0,0.3485031127929688,0,0.35943603515625,0.2391357421875,0,0,-1.767478942871094,0,0.2411041259765625,0,0.2721405029296875,0,0,0.3108139038085938,0.3370819091796875,0,0.3502044677734375,0,0.3069610595703125,0,0,0,-1.519981384277344,0,0.2629928588867188,0,0.2920150756835938,0,0.3298568725585938,0,0.3402481079101562,0,0.344879150390625,0,0,0,-1.528297424316406,0,0.242340087890625,0,0,0.2880096435546875,0.3272476196289062,0,0.3421707153320312,0,0.357818603515625,0.01995086669921875,0,0,-1.546371459960938,0,0.2482452392578125,0,0.286224365234375,0,0,0.3220443725585938,0,0.3405914306640625,0,0.3512649536132812,0,0,0.0463714599609375,0,-1.513069152832031,0.2519454956054688,0,0,0.289398193359375,0.3214950561523438,0.3433380126953125,0,0,0.3514785766601562,0,0,0.00313568115234375,0,-1.473876953125,0,0.2450103759765625,0.32879638671875,0,0.328460693359375,0,0.3353652954101562,0,0.2830429077148438,0,0,0,0,0,-1.402206420898438,0,0.2479248046875,0,0.2993392944335938,0,0.333282470703125,0,0.3514633178710938,0,0.2163467407226562,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.587806701660156,0,0,0.0673828125,0,0,0.2381439208984375,0,0.2542190551757812,0,0.2849884033203125,0,0.3079605102539062,0,0.308868408203125,0,0.3754730224609375,0.3695755004882812,0,0.3900833129882812,0,0,0.3657455444335938,0.3326950073242188,0.3284988403320312,0.3301162719726562,0.3301620483398438,0,0,0.3304519653320312,0,0.2256088256835938,0,0,0,0,0,-4.370079040527344,0,0.315887451171875,0.3439865112304688,0.3277359008789062,0.3461456298828125,0.3943710327148438,0.4126434326171875,0.411376953125,0,0.4095687866210938,0.4073867797851562,0,0.4083480834960938,0,0.4027481079101562,0,0.3221969604492188,0,0,0,-4.329574584960938,0.3131484985351562,0,0.3364105224609375,0,0,0.3197479248046875,0.3585052490234375,0.3889541625976562,0.3944854736328125,0,0.3953323364257812,0,0.4367599487304688,0,0.4038238525390625,0,0.4033660888671875,0,0.4034423828125,0,0,0.3058700561523438,0,0,0,0,0,-4.255409240722656,0,0.3016433715820312,0,0.3125457763671875,0,0.3053207397460938,0,0.3516769409179688,0,0,0.3627166748046875,0,0.38970947265625,0,0.3931121826171875,0.3986358642578125,0,0,0.3998870849609375,0.4050674438476562,0.4074020385742188,0,0.355865478515625,0,0,0,0,0,-4.270278930664062,0,0.2792434692382812,0,0.3051300048828125,0,0.2999038696289062,0,0.3486862182617188,0,0.3670501708984375,0,0,0.3800811767578125,0,0.3902359008789062,0.394012451171875,0.3917388916015625,0.3929824829101562,0,0.4040603637695312,0,0.3899765014648438,0.05316925048828125,0,-4.21966552734375,0,0.2753067016601562,0,0.2967529296875,0,0,0.3002853393554688,0,0.3466720581054688,0.3704986572265625,0.3919448852539062,0,0.404998779296875,0.4006118774414062,0.4048233032226562,0,0.4034881591796875,0.4068603515625,0.3414993286132812,0,0,0,0,0,-4.089683532714844,0.2843475341796875,0,0.2958526611328125,0,0,0.3232040405273438,0,0.3587265014648438,0,0.3810272216796875,0.3992767333984375,0,0.400665283203125,0,0.4019622802734375,0,0.4061126708984375,0.4100112915039062,0.3979949951171875,0,0.152496337890625,0,0,-4.164222717285156,0,0.2703018188476562,0.2863235473632812,0,0.3065414428710938,0.38360595703125,0,0.34918212890625,0.37225341796875,0,0.3900833129882812,0.3871002197265625,0.3902435302734375,0,0.3875732421875,0,0.3946456909179688,0.3664169311523438,0,0,0,0,0,-4.038681030273438,0,0.2497634887695312,0,0.2549057006835938,0,0.2539825439453125,0.287200927734375,0,0.3511505126953125,0,0.33551025390625,0,0.3496856689453125,0,0.3366317749023438,0,0.3305282592773438,0.3388824462890625,0,0.3379669189453125,0,0,0.3409271240234375,0,0.3388824462890625,0,0.05078887939453125,0,-4.045219421386719,0,0.2640838623046875,0,0.273040771484375,0,0.2768630981445312,0,0.2916641235351562,0,0.3165359497070312,0,0.3307571411132812,0.3408432006835938,0.3572006225585938,0,0.3611297607421875,0,0.3718490600585938,0,0.37921142578125,0,0,0.3825149536132812,0,0.2157058715820312,0,0,0,0,0,-3.783287048339844,0,0.2506332397460938,0.2740249633789062,0,0,0.3516311645507812,0,0.3402481079101562,0.3520050048828125,0.3720245361328125,0,0.38623046875,0,0,0.3809585571289062,0,0,0.382904052734375,0,0.4020004272460938,0,0.3879241943359375,0.01708984375,0,0,-3.849700927734375,0,0.2465972900390625,0,0.2570877075195312,0.3309555053710938,0.3303451538085938,0,0.3279647827148438,0,0.3494033813476562,0,0.3668899536132812,0,0.3570480346679688,0.3619155883789062,0,0,0.3730926513671875,0,0.3874588012695312,0.2734603881835938,0,0,0,-3.7701416015625,0,0,0.2080612182617188,0.2458877563476562,0,0.3044509887695312,0,0.3054885864257812,0.3349838256835938,0,0.3352279663085938,0,0.3649520874023438,0,0,0.3616256713867188,0.3724288940429688,0,0.3902587890625,0.3647689819335938,0,0.2926864624023438,0,0,0,0,0,-3.716453552246094,0,0.2292633056640625,0.24066162109375,0,0.285675048828125,0,0.2897415161132812,0,0.317291259765625,0,0.3461761474609375,0,0.3358535766601562,0,0.373138427734375,0.3686599731445312,0.3745651245117188,0,0.386749267578125,0,0.277618408203125,0,0,0,0,0,-3.605155944824219,0,0.2394027709960938,0,0.2728652954101562,0,0.2933425903320312,0,0.3327255249023438,0,0,0.3499298095703125,0.3656997680664062,0.3900604248046875,0,0.3842391967773438,0,0.3934860229492188,0,0.4035263061523438,0,0.2869720458984375,0,0,0,-3.534393310546875,0,0.244140625,0,0.2849197387695312,0,0.3121566772460938,0,0.3339920043945312,0,0.3558197021484375,0,0.3801345825195312,0.3902587890625,0.4030685424804688,0.4065704345703125,0,0.39862060546875,0.1302032470703125,0,0,-3.618904113769531,0.237548828125,0,0.2583389282226562,0.3188095092773438,0,0,0.3135528564453125,0,0.3393783569335938,0,0,0.3553390502929688,0,0.37451171875,0.3821868896484375,0.386871337890625,0,0.3929061889648438,0,0.3630905151367188,0,0,0,0,0,-3.498779296875,0,0.2253036499023438,0,0.25677490234375,0,0.2754440307617188,0,0.3067169189453125,0,0.3367385864257812,0,0.3492431640625,0,0.3665924072265625,0.3686676025390625,0,0.3869247436523438,0,0.39111328125,0,0.3373565673828125,0,0,0,-3.429222106933594,0,0.229522705078125,0.256195068359375,0,0.2795486450195312,0,0.3458633422851562,0,0.3399505615234375,0,0.3600082397460938,0,0.3768157958984375,0.3817672729492188,0,0.3831329345703125,0.3909683227539062,0.1858062744140625,0,0,0,0,0,-3.341796875,0.229644775390625,0,0.2465972900390625,0.271240234375,0,0.3199310302734375,0,0.2759628295898438,0,0.3359375,0.3628082275390625,0,0.3170852661132812,0,0.3501434326171875,0.3760147094726562,0,0.344970703125,0,0.0102996826171875,0,-3.391525268554688,0,0.2253646850585938,0,0.2140121459960938,0.2536392211914062,0.2863006591796875,0.2965850830078125,0,0,0.3376007080078125,0,0.3602371215820312,0,0.34063720703125,0,0.3267135620117188,0,0.3618850708007812,0.3729934692382812,0,0.1126785278320312,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-3.34014892578125,0,0.1751251220703125,0,0.2083053588867188,0,0.2239608764648438,0,0.2364730834960938,0,0.2632293701171875,0,0.2928924560546875,0,0,0.3118209838867188,0,0.3218231201171875,0,0.3454208374023438,0.4172210693359375,0,0.3805465698242188,0,0.2587051391601562,0,0,0,0,0,-3.160789489746094,0,0.2308731079101562,0.2555465698242188,0,0.2801361083984375,0.3054962158203125,0,0.3329849243164062,0,0.3466033935546875,0,0.359161376953125,0,0.3734130859375,0.3978195190429688,0,0.3728790283203125,0,0,0,0,0,-3.150909423828125,0,0.2302169799804688,0,0.2514114379882812,0,0.2795944213867188,0.317535400390625,0,0.3414764404296875,0,0.3502883911132812,0,0,0.3628463745117188,0.3805007934570312,0.3972091674804688,0,0.332366943359375,0,0,0,0,0,-3.054420471191406,0,0.2325515747070312,0,0.2589340209960938,0,0.28778076171875,0,0.31500244140625,0,0,0.334259033203125,0,0.3475341796875,0.3520889282226562,0.3722000122070312,0,0.38641357421875,0,0.2587661743164062,0,0,0,-3.014900207519531,0,0,0.2279739379882812,0,0.2491226196289062,0,0.2800064086914062,0.3115463256835938,0,0.3344345092773438,0,0.34844970703125,0.3574905395507812,0,0.3744659423828125,0.392608642578125,0.2284164428710938,0,0,0,0,0,-2.947486877441406,0,0.2326812744140625,0,0.2570266723632812,0.2856063842773438,0,0.3562164306640625,0,0.3375701904296875,0,0.3493728637695312,0,0.3658065795898438,0.3777084350585938,0,0.3941574096679688,0.0795440673828125,0,0,0,-2.8131103515625,0,0.2362594604492188,0,0.2652740478515625,0,0.3000717163085938,0,0,0.3337249755859375,0,0.3455657958984375,0,0.35986328125,0,0.3760528564453125,0,0.390655517578125,0.2923660278320312,0,0,0,-2.867073059082031,0,0.2309112548828125,0,0.253936767578125,0,0,0.2865371704101562,0,0.3220062255859375,0,0.3466873168945312,0.3520355224609375,0,0.37060546875,0.393280029296875,0,0,0.396484375,0,0,0,-2.861427307128906,0,0.228271484375,0,0.2532501220703125,0.2868270874023438,0,0.32147216796875,0,0.337646484375,0,0.344451904296875,0,0.3664398193359375,0.3793716430664062,0,0.39251708984375,0,0.03510284423828125,0,0,-2.884620666503906,0,0.2147979736328125,0,0.2281341552734375,0,0.2544708251953125,0.3183059692382812,0.3249435424804688,0,0,0.331573486328125,0.32720947265625,0.3375396728515625,0,0.3493728637695312,0.2809524536132812,0,0,0,0,0,-2.767578125,0,0.2196426391601562,0,0.2299880981445312,0.2672958374023438,0,0.2952117919921875,0,0.3215866088867188,0,0.342071533203125,0,0.342987060546875,0,0.362030029296875,0,0.3836288452148438,0,0.08435821533203125,0,0,0,0,0,-2.582290649414062,0,0.2293472290039062,0,0.2612152099609375,0,0.2947998046875,0,0.3276443481445312,0,0.3441238403320312,0,0.3553619384765625,0.3721160888671875,0,0.3935928344726562,0.08406829833984375,0,0,0,0,0,-2.550643920898438,0.2299957275390625,0,0.27691650390625,0,0.291839599609375,0,0.3205337524414062,0,0.3204193115234375,0.3357162475585938,0,0,0.3476104736328125,0,0.360260009765625,0,0.1459884643554688,0,0,0,0,0,-2.571800231933594,0.2191314697265625,0,0,0.2396774291992188,0,0.2734375,0,0.311309814453125,0.3660354614257812,0.3440399169921875,0.340087890625,0,0.3427581787109375,0,0.2127304077148438,0,0,0,-2.601463317871094,0,0.2129287719726562,0.2305145263671875,0,0.2732315063476562,0,0.2863845825195312,0,0.31671142578125,0,0.3266754150390625,0.3392410278320312,0.3474655151367188,0,0.344451904296875,0,0,0,0,0,-2.607658386230469,0.2141494750976562,0,0.2293624877929688,0,0.2786178588867188,0,0.2978515625,0.318267822265625,0,0.3319778442382812,0,0.34698486328125,0.3568649291992188,0,0.3085098266601562,0,0,0,0,0,-2.5400390625,0,0.2298812866210938,0,0.252197265625,0,0.2908782958984375,0.3227005004882812,0,0.3405990600585938,0,0.3471527099609375,0,0.3662338256835938,0.3752670288085938,0.088836669921875,0,0,0,0,0,-2.337638854980469,0,0.2300338745117188,0,0.2584686279296875,0,0.2933349609375,0.32843017578125,0.34393310546875,0.3501815795898438,0,0.3643035888671875,0,0.2414627075195312,0,0,0,0,0,-2.360549926757812,0,0.2244873046875,0,0.2419281005859375,0.2701263427734375,0.3001708984375,0,0.3316650390625,0,0.344818115234375,0,0.3626861572265625,0,0.3560409545898438,0,0,0,-2.421684265136719,0,0.2188186645507812,0,0.2337493896484375,0,0.2657241821289062,0.2892913818359375,0.32708740234375,0,0.3425750732421875,0,0.3449630737304688,0,0.366607666015625,0,0.1029815673828125,0,0,0,0,0,-2.245048522949219,0.2261199951171875,0,0.249420166015625,0.2907638549804688,0,0.3210525512695312,0,0.3436508178710938,0.3507080078125,0,0.3599014282226562,0,0.1725387573242188,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2.323448181152344,0,0.183837890625,0,0.2357330322265625,0.234893798828125,0.2636184692382812,0,0.2922897338867188,0,0.3253555297851562,0,0.342529296875,0,0.3566131591796875,0.1561965942382812,0,0,0,-2.201942443847656,0.2287750244140625,0,0.250396728515625,0,0.275482177734375,0,0.311370849609375,0.3215713500976562,0,0.3336563110351562,0.3553237915039062,0,0.1922760009765625,0,0,0,0,0,-2.202247619628906,0.2276077270507812,0,0.22308349609375,0.26507568359375,0,0.307098388671875,0,0.3420257568359375,0,0.3313217163085938,0,0.3520126342773438,0,0.219818115234375,0,0,0,0,0,-2.220207214355469,0.2226104736328125,0,0.2140274047851562,0,0.25799560546875,0,0.2944259643554688,0,0.2726669311523438,0,0.325347900390625,0,0.3371505737304688,0.338958740234375,0,0.021759033203125,0,0,0,0,0,-2.071609497070312,0,0.2137680053710938,0,0,0.2379074096679688,0,0.277496337890625,0.2949752807617188,0.3575515747070312,0,0.3383865356445312,0.3428115844726562,0,0.07236480712890625,0,0,0,-2.057273864746094,0,0.2128372192382812,0,0.225311279296875,0,0.2721786499023438,0,0.288116455078125,0,0.304840087890625,0,0,0.3409881591796875,0.3268814086914062,0,0.1488265991210938,0,0,0,-2.076713562011719,0,0,0.2165451049804688,0,0.2345962524414062,0,0,0.2693557739257812,0,0.3062210083007812,0,0.3367462158203125,0,0.3461685180664062,0.3637161254882812,0.06499481201171875,0,0,0,0,0,-1.922508239746094,0,0.2311630249023438,0,0.2614593505859375,0,0.2991409301757812,0,0.3322296142578125,0.3502044677734375,0,0.362701416015625,0,0.1462326049804688,0,0,0,-1.954521179199219,0.2289276123046875,0,0.2559890747070312,0,0,0.2937240600585938,0.329193115234375,0.3492660522460938,0,0.3589706420898438,0,0.1981353759765625,0,0,0,0,0,-1.957588195800781,0.226654052734375,0.24090576171875,0,0.279205322265625,0.3120040893554688,0.3740386962890625,0.3511428833007812,0,0.2323379516601562,0,0,0,0,0,-1.978126525878906,0.21759033203125,0.2361831665039062,0,0.2646255493164062,0,0.3021697998046875,0.3335800170898438,0.3473892211914062,0,0.3343276977539062,0,0,0,0,0,0,0,0,-1.820892333984375,0.2231369018554688,0.2519989013671875,0,0.28094482421875,0,0,0.3178329467773438,0.337066650390625,0,0.346038818359375,0,0.1207046508789062,0,0,0,0,0,-1.835281372070312,0,0.2231903076171875,0,0.2427215576171875,0,0.282318115234375,0,0.3135757446289062,0,0.3433914184570312,0,0.3528976440429688,0,0.1330642700195312,0,0,0,-1.819000244140625,0,0.2235794067382812,0.2473526000976562,0,0.2827606201171875,0.3205947875976562,0.3482894897460938,0,0,0.3551254272460938,0.09635162353515625,0,0,0,0,0,-1.746109008789062,0.2275924682617188,0.2536697387695312,0,0.2953262329101562,0,0.3295669555664062,0,0,0.3541030883789062,0,0.33990478515625,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.811454772949219,0.208251953125,0,0,0.2327117919921875,0.2547378540039062,0,0.2788848876953125,0.3197174072265625,0.3372116088867188,0,0.2332077026367188,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.832717895507812,0,0,0,0,0,0.097442626953125,0.2461624145507812,0,0.2572708129882812,0,0.2914047241210938,0,0.3163986206054688,0,0.3509368896484375,0,0.3168106079101562,0.3505325317382812,0,0.3883590698242188,0,0.3982925415039062,0,0.3444747924804688,0,0.3273391723632812,0.3247528076171875,0,0,0.3286514282226562,0,0,0.3260116577148438,0,0.3282089233398438,0.3272628784179688,0.3275604248046875,0,0.3302764892578125,0,0.3263397216796875,0.3262252807617188,0,0.3280181884765625,0.325836181640625,0,0.3293914794921875,0,0.0329437255859375,0,0,0,0,0,-7.200820922851562,0,0.2494049072265625,0.2696380615234375,0,0.2988357543945312,0.3103103637695312,0.306549072265625,0,0.3443984985351562,0,0.3604278564453125,0,0.3816604614257812,0.3997955322265625,0,0.4046554565429688,0.4106063842773438,0,0.4089431762695312,0.4072036743164062,0.4058074951171875,0.4088592529296875,0,0.406280517578125,0,0.4030838012695312,0.404754638671875,0.4027328491210938,0,0.390655517578125,0,0.035400390625,0,0,0,0,0,-7.073844909667969,0,0.252838134765625,0.278656005859375,0.3101348876953125,0.3150863647460938,0,0.3299713134765625,0.3630523681640625,0,0.3733673095703125,0,0.3966293334960938,0.3956222534179688,0,0.3966140747070312,0,0.4022216796875,0.4006118774414062,0.3989639282226562,0,0.4006118774414062,0,0.4026031494140625,0,0.4009017944335938,0,0.402435302734375,0,0.4022979736328125,0,0.38641357421875,0,0.27056884765625,0,0,0,0,0,0,0,0,-6.926582336425781,0.2464752197265625,0,0.2658462524414062,0,0.2907791137695312,0,0.2941513061523438,0.3321762084960938,0.3519973754882812,0,0.3545303344726562,0.37451171875,0,0.3824234008789062,0,0.4332046508789062,0,0.3913650512695312,0.3937225341796875,0,0,0.3986892700195312,0,0,0.3970260620117188,0.4040069580078125,0,0.39727783203125,0,0.4047012329101562,0,0.4053497314453125,0.39166259765625,0,0.2191162109375,0,0,0,0,0,0,0,0,-6.804656982421875,0,0.2497024536132812,0,0.2630386352539062,0,0.277801513671875,0,0,0.2865676879882812,0,0.334686279296875,0.352996826171875,0,0.3539581298828125,0,0.3720855712890625,0.3873443603515625,0,0,0.4324951171875,0.3897781372070312,0,0.3919525146484375,0.3889617919921875,0,0.3975906372070312,0,0.4006271362304688,0,0.3958358764648438,0.4025421142578125,0.402191162109375,0,0.38885498046875,0.1348342895507812,0,0,0,0,0,-6.663375854492188,0,0,0.245819091796875,0,0.2892074584960938,0,0.2672271728515625,0,0.306365966796875,0,0.3429489135742188,0.351715087890625,0.3573150634765625,0.3709259033203125,0.3843460083007812,0,0.3855743408203125,0.387725830078125,0.3932952880859375,0,0.3988037109375,0,0.4016647338867188,0.4046478271484375,0,0.4074783325195312,0,0.4086837768554688,0,0.3992538452148438,0,0.3563613891601562,0,0,0,0,0,0,0,0,-6.668426513671875,0,0.26727294921875,0,0,0.2540817260742188,0,0.2639083862304688,0,0.2929229736328125,0,0.3300094604492188,0,0.3448333740234375,0,0.3489990234375,0,0.3543548583984375,0.3672027587890625,0.3776473999023438,0,0,0.3909378051757812,0.3846588134765625,0,0.3921432495117188,0.404022216796875,0,0.3961944580078125,0,0.3977890014648438,0.3985748291015625,0.3977508544921875,0,0.3916473388671875,0,0.1063079833984375,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-6.6346435546875,0,0,0,0.1537704467773438,0,0.2389907836914062,0,0.2428817749023438,0,0.2465057373046875,0.2953643798828125,0,0.3271255493164062,0.325103759765625,0,0.3444366455078125,0.37835693359375,0,0.3975448608398438,0.4045944213867188,0.4011154174804688,0,0.3993606567382812,0,0,0.4020233154296875,0,0,0.4039154052734375,0.4041213989257812,0,0.4069671630859375,0,0.4070816040039062,0,0.4065628051757812,0,0.2384796142578125,0,0,0,0,0,0,0,0,-6.387741088867188,0.2413330078125,0.2419052124023438,0,0.255218505859375,0.3047409057617188,0.3295440673828125,0.3368453979492188,0,0.3879776000976562,0.3517074584960938,0,0.3670654296875,0,0,0.382232666015625,0,0.3856964111328125,0.3938980102539062,0,0,0.396728515625,0,0.4046478271484375,0,0.4069976806640625,0,0.4081573486328125,0,0.4062347412109375,0.4056243896484375,0,0.1678237915039062,0,0,0,0,0,-6.25640869140625,0,0.236328125,0,0.2367401123046875,0,0.2672958374023438,0.3093109130859375,0,0.36602783203125,0.3422470092773438,0.3461151123046875,0.3617095947265625,0,0.371673583984375,0,0,0.3830490112304688,0,0,0.389068603515625,0,7.902633666992188,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7.62939453125,7.62939453125e-06,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,15.2587890625,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7.689292907714844,0,0,0,0,0,0,0,0,0,0,0,0,0,0,15.33531951904297,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"filename":["<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,null,null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,null,"<expr>",null,null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,null,null,null,null,null,null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,"<expr>","<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,null,null,null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,null,null,"<expr>",null,null,null,null,"<expr>",null,null,null,null,"<expr>","<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,null,null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,null,null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,null,null,null,null,null,null,null,null,null,"<expr>","<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null]},"interval":10,"files":[{"filename":"<expr>","content":"## Generate Large Random Dataset\nn <- 2e6\nx <- runif(n)\ny <- runif(n)\nz <- runif(n)\nXYZ <- cbind(x,y,z)\n\n## Inspect 4 equivalent `row mean` calculations \nprofvis::profvis({\n    m <- rowSums(XYZ)/ncol(XYZ)\n    m <- rowMeans(XYZ)\n    m <- apply(XYZ, 1, mean)\n    m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }\n})\n## rowSums(), colSums(), rowMeans(), and colMeans() are vectorised and fast.\n## for loop is not the slowest, but the ugliest.","normpath":"<expr>"}],"prof_output":"/tmp/RtmpAl9aZF/filea67f2860c4db.prof","highlight":{"output":["^output\\$"],"gc":["^<GC>$"],"stacktrace":["^\\.\\.stacktraceo(n|ff)\\.\\.$"]},"split":"h"}},"evals":[],"jsHooks":[]}</script>
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
## 1 mean1(x, 0.5)     20ms   21.9ms      45.9    7.63MB     2.09
## 2 mean2(x, 0.5)   19.2ms     21ms      48.2    7.63MB     0   
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
##   0.106   0.000   0.034
```

```r
system.time({ lm(Y~X, data=DAT) })
```

```
##    user  system elapsed 
##   0.410   0.000   0.141
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
## 1 ma1(y)        176ms  176.3ms      5.67    15.3MB     2.84
## 2 ma2(y)       24.4ms   24.4ms     40.9     91.6MB   614.
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
##   0.028   0.002   0.030
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
##   0.829   0.249   0.605
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





