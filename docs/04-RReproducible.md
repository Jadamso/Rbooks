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
<div class="plotly html-widget html-fill-item-overflow-hidden html-fill-item" id="htmlwidget-25d8172224369b1f6ae6" style="width:672px;height:480px;"></div>
<script type="application/json" data-for="htmlwidget-25d8172224369b1f6ae6">{"x":{"visdat":{"46b975a5c8b7":["function () ","plotlyVisDat"]},"cur_data":"46b975a5c8b7","attrs":{"46b975a5c8b7":{"x":{},"y":{},"alpha_stroke":1,"sizes":[10,100],"spans":[1,20]}},"layout":{"margin":{"b":40,"l":60,"t":25,"r":10},"xaxis":{"domain":[0,1],"automargin":true,"title":"X"},"yaxis":{"domain":[0,1],"automargin":true,"title":"Y"},"hovermode":"closest","showlegend":false},"source":"A","config":{"modeBarButtonsToAdd":["hoverclosest","hovercompare"],"showSendToCloud":false},"data":[{"x":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100],"y":[4.3582628408223636,5.6926263750699562,7.5632149906505859,16.815732570370781,18.432272497060069,23.752460091428443,28.902814874678281,34.548487256248968,33.924171933368825,42.759692445680074,46.850256885038938,47.197633828254872,47.858587565142038,54.781458167779974,58.540334669731024,62.737859167768057,67.758241864345038,76.069075546651661,75.187458230402896,85.457079578648973,84.580930342337098,87.355626045189638,88.33920734649746,99.413114626625628,98.951219040666317,104.81092087205627,105.75617123171486,112.4682058480297,117.97158157903316,119.78472561553764,122.13404642752177,126.21218488121312,134.89155787135417,136.68951946661036,138.12517104533964,146.04222492542786,143.76314627822836,153.54408794892461,156.41887821007137,164.5808942550988,164.93877691536292,165.10717817329299,174.0557242528167,176.7004716482196,181.31500608949631,181.73665327298571,187.67677601571526,191.95567726852278,195.99926614654092,200.7738172399128,204.58867320810398,212.07514406054224,212.23397788597435,219.30633078081152,220.69896204035012,223.00868949816456,225.89472419989414,231.57542740688277,240.07615968834284,241.81416433181104,244.03110719809038,246.41339093169671,250.6259668878387,255.90606888591742,259.14224097794443,263.4908890550837,266.60710042912302,276.95005680766673,277.85278726233275,284.1230746661617,284.34356318307459,287.18926100415842,291.94167715676514,293.97476976030617,296.57754840287754,301.17306498054819,307.05274558244975,311.74593470938407,314.10748053095648,319.383885735695,324.63017602432245,327.67531082287206,329.95717300645612,334.35181937933476,337.21660238915342,342.90688248453921,347.49490993439866,352.99691884534155,358.56091491051279,361.54805132598779,362.50453623133285,367.90400820967528,366.75628413823898,376.12395369538939,383.16264294970136,387.23836089808367,388.83990239200728,393.50531522285519,395.19647923666832,400.19391852725869],"type":"scatter","mode":"markers","marker":{"color":"rgba(31,119,180,1)","line":{"color":"rgba(31,119,180,1)"}},"error_y":{"color":"rgba(31,119,180,1)"},"error_x":{"color":"rgba(31,119,180,1)"},"line":{"color":"rgba(31,119,180,1)"},"xaxis":"x","yaxis":"y","frame":null}],"highlight":{"on":"plotly_click","persistent":false,"dynamic":false,"selectize":false,"opacityDim":0.20000000000000001,"selected":{"opacity":1},"debounce":0},"shinyEvents":["plotly_hover","plotly_click","plotly_selected","plotly_relayout","plotly_brushed","plotly_brushing","plotly_clickannotation","plotly_doubleclick","plotly_deselect","plotly_afterplot","plotly_sunburstclick"],"base_url":"https://plot.ly"},"evals":[],"jsHooks":[]}</script>
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
## Ncells 1209376 64.6    2357217 125.9  2357217 125.9
## Vcells 2293487 17.5    8388608  64.0  3529912  27.0
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
<div class="profvis html-widget html-fill-item-overflow-hidden html-fill-item" id="htmlwidget-9de8e9a0d563fb44ad67" style="width:100%;height:600px;"></div>
<script type="application/json" data-for="htmlwidget-9de8e9a0d563fb44ad67">{"x":{"message":{"prof":{"time":[1,2,3,4,5,5,6,7,8,9,9,9,10,10,11,11,12,12,13,13,14,14,15,15,16,16,17,17,18,18,19,19,20,20,21,22,23,24,24,24,25,25,26,26,27,27,28,28,29,29,30,31,31,32,32,33,33,34,34,35,35,36,36,37,37,37,38,39,39,40,40,41,41,41,42,43,43,44,45,46,47,48,48,49,49,50,50,51,51,52,52,52,53,53,54,54,54,55,56,57,57,58,58,59,59,59,60,60,61,61,62,62,63,63,64,64,65,65,65,66,66,67,67,68,68,68,69,70,70,71,72,72,73,73,74,75,75,75,76,77,77,78,79,80,80,81,81,81,82,82,83,84,84,85,85,85,86,86,87,88,89,89,90,91,92,93,93,94,94,94,95,96,97,98,98,99,100,101,101,102,102,103,103,103,104,104,105,105,106,106,106,107,107,108,109,110,110,111,111,111,112,112,113,114,115,115,115,116,117,117,118,118,119,120,120,121,121,122,122,123,123,124,124,125,125,126,126,127,127,128,128,129,130,130,131,131,132,132,133,134,134,135,136,136,136,137,138,138,139,139,140,141,141,142,142,143,144,144,145,145,146,146,147,147,148,148,149,150,150,151,152,152,153,154,154,155,156,157,158,158,159,159,160,160,161,161,162,163,163,164,164,165,165,166,167,167,168,168,168,169,169,170,170,171,171,172,172,173,173,174,174,175,175,175,176,176,176,177,177,178,178,179,180,180,181,182,183,183,183,184,184,184,185,185,186,186,187,187,188,189,190,190,191,191,192,192,192,193,193,194,194,195,195,195,196,196,197,198,198,199,199,200,200,200,201,201,201,202,202,202,203,203,203,204,204,204,205,205,205,206,206,206,207,207,207,208,208,208,209,210,211,211,212,213,214,214,215,215,216,216,217,217,217,218,218,219,219,220,220,221,222,222,223,224,225,225,225,226,226,227,227,228,228,229,229,230,230,231,232,232,233,233,234,234,235,235,235,236,236,237,237,237,238,239,239,240,240,240,241,241,242,242,243,243,244,245,246,246,247,247,247,248,248,248,249,249,250,250,251,251,252,253,253,254,255,255,256,257,257,258,259,259,260,260,261,262,262,262,263,263,264,265,265,266,267,268,268,268,269,269,269,270,270,271,272,273,273,274,275,275,276,276,276,276,277,278,279,279,279,280,280,281,282,282,283,283,283,283,284,284,284,284,285,285,286,286,287,287,288,288,288,289,289,290,290,290,290,291,291,292,293,293,294,294,295,295,296,296,297,297,297,298,299,299,300,300,301,301,302,302,303,304,304,304,305,306,307,307,308,308,309,310,311,311,312,312,312,313,314,314,315,316,317,318,318,318,319,319,320,320,321,321,322,322,323,323,324,324,324,325,325,325,326,327,327,328,328,329,329,330,330,331,331,332,332,333,333,334,335,335,336,337,337,338,338,338,339,340,341,341,342,342,343,344,344,344,345,346,346,347,347,348,348,349,349,349,350,350,350,351,352,352,353,353,354,355,355,356,356,356,357,357,357,358,358,358,359,359,359,360,360,360,361,361,361,362,362,362,363,363,363,364,364,364,365,365,365,366,366,366,367,367,367,368,368,368,369,369,369,370,370,370,371,371,371,372,372,372,373,373,373,374,374,374,375,375,375,376,376,376,377,377,377,378,378,378,379,379,379,380,380,380,381,381,381,382,382,383,384,384,384,385,386,386,387,387,387,388,389,389,390,391,392,392,392,393,393,393,394,394,395,395,396,397,397,398,398,398,399,400,400,401,401,402,402,403,403,404,404,404,405,406,407,408,408,409,409,410,411,411,411,412,413,413,414,415,416,416,417,417,418,418,419,420,420,421,422,422,423,423,424,424,425,425,426,427,427,427,428,428,429,429,430,431,431,432,433,433,434,435,435,436,436,437,437,438,438,438,439,439,439,440,440,441,441,442,442,442,443,443,444,444,445,446,447,447,448,449,449,449,450,450,451,451,451,452,452,452,453,453,453,454,454,455,455,456,456,457,457,458,459,460,460,461,461,462,462,463,464,465,465,465,466,467,467,468,468,469,469,470,470,471,471,472,473,473,474,475,476,476,476,477,477,478,478,478,478,479,479,479,479,480,480,480,481,482,483,483,484,485,485,486,486,486,487,487,488,488,489,489,490,490,491,492,492,492,493,494,494,495,495,496,496,497,497,498,499,500,500,501,501,502,502,503,503,504,505,505,506,506,507,507,508,508,509,509,510,510,511,511,512,512,513,513,513,514,514,514,515,516,516,517,517,517,518,518,519,519,520,521,521,521,522,522,522,523,523,523,524,525,526,527,528,529,529,530,531,531,532,532,533,533,534,534,535,535,536,536,537,537,538,538,539,540,541,542,542,543,543,544,544,545,545,546,546,547,548,549,550,550,551,551,552,552,553,554,554,555,556,557,557,558,559,559,560,561,561,562,563,563,563,564,564,565,565,566,566,567,567,568,569,569,570,571,571,572,573,573,574,575,576,576,577,577,578,578,579,579,580,580,581,581,582,582,583,584,584,584,585,586,587,588,588,589,590,591,591,591,592,593,594,594,595,596,596,597,598,598,599,599,600,601,601,602,602,603,603,604,604,605,606,606,607,607,608,608,608,609,609,610,610,611,612,613,613,614,614,615,615,616,616,616,617,617,617,618,618,618,619,619,620,620,621,621,622,623,624,625,625,626,626,627,627,628,629,629,629,630,630,630,631,631,632,632,633,634,634,635,635,636,637,638,638,639,639,639,640,640,640,641,641,641,642,642,642,643,643,644,644,645,645,646,647,648,649,650,651,652,652,653,654,654,654,655,655,655,656,656,656,657,658,659,660,660,661,662,663,664,665,665,666,666,667,667,668,668,669,669,670,670,671,671,672,672,673,673,674,674,675,675,676,676,677,677,678,678,679,679,680,680,681,681,682,682,683,683,684,685,686,686,687,687,687,688,689,690,690,691,691,692,692,693,693,694,694,695,696,696,697,697,697,698,699,699,700,700,701,701,702,702,703,704,704,704,705,705,705,706,706,707,707,708,708,709,710,710,711,711,712,713,714,715,716,716,717,717,718,718,719,720,721,722,723,724,725,726,726,726,727,727,728,728,729,729,730,730,731,732,732,733,733,734,735,736,736,736,737,737,737,738,738,739,739,740,740,741,742,742,742,743,743,743,744,744,745,745,746,747,747,748,748,749,749,750,751,751,751,752,752,753,754,754,755,756,757,757,758,759,759,760,760,761,762,762,763,763,763,764,764,765,765,766,766,767,768,768,769,769,770,770,770,771,772,773,773,773,773,774,775,775,776,776,777,777,778,778,779,779,780,780,781,781,782,782,783,783,784,784,784,784,785,785,785,785,786,786,787,788,788,789,789,790,790,791,792,792,793,793,794,795,795,795,796,796,796,797,798,798,799,799,800,800,801,801,802,802,803,803,804,805,806,806,807,807,807,808,808,809,809,810,810,811,812,812,813,814,815,815,816,816,817,817,818,818,818,819,819,819,820,820,820,821,821,822,823,824,824,825,825,826,826,827,827,828,828,829,829,830,830,831,831,832,832,833,833,834,834,835,835,836,837,837,837,838,839,839,840,840,841,842,842,843,843,844,844,845,845,846,847,848,848,849,849,850,850,851,851,852,853,853,854,854,855,856,856,857,857,858,858,859,860,860,861,861,862,862,862,863,863,864,865,865,866,867,868,868,869,869,870,870,870,871,871,871,872,872,872,873,874,874,875,875,875,876,876,877,877,877,878,878,879,879,880,881,881,881,882,883,883,884,884,885,885,886,887,888,888,889,889,890,890,891,891,891,892,892,893,894,894,895,895,896,896,897,898,898,899,899,900,901,901,901,902,903,904,905,905,905,906,906,907,907,908,908,908,909,909,910,910,910,911,911,911,912,912,912,913,913,913,914,914,914,915,915,915,916,916,916,917,917,917,918,918,918,919,919,919,920,920,920,921,922,922,923,923,924,924,925,925,926,926,927,927,927,928,929,930,930,930,930,931,931,931,931,932,933,933,934,935,936,936,937,938,939,940,940,940,941,941,941,942,943,944,944,945,946,946,947,947,948,948,949,949,949,950,950,950,951,951,952,952,953,953,954,955,955,956,956,957,957,958,958,959,959,960,960,961,962,962,963,963,964,964,965,966,967,967,967,968,968,969,969,970,970,971,971,972,972,973,973,974,975,975,976,976,976,977,977,978,978,978,979,979,979,980,980,981,981,982,983,983,984,985,985,985,986,987,987,987,988,988,988,989,989,990,990,991,991,992,992,993,994,995,995,995,996,996,997,997,998,999,1000,1000,1001,1001,1002,1002,1003,1004,1005,1005,1006,1006,1007,1008,1009,1010,1010,1011,1011,1012,1013,1013,1014,1014,1014,1014,1015,1015,1015,1015,1016,1017,1017,1018,1019,1019,1020,1020,1021,1021,1022,1022,1023,1023,1023,1024,1024,1024,1025,1026,1026,1027,1028,1029,1029,1030,1030,1031,1032,1032,1033,1033,1034,1034,1035,1035,1036,1037,1038,1039,1040,1040,1040,1040,1041,1041,1041,1041,1042,1042,1042,1042,1043,1043,1044,1044,1045,1045,1046,1047,1048,1048,1049,1049,1049,1050,1050,1050,1051,1052,1052,1053,1053,1054,1054,1055,1055,1056,1056,1057,1057,1057,1058,1058,1058,1059,1059,1059,1060,1060,1060,1061,1061,1061,1062,1062,1062,1063,1063,1063,1064,1064,1064,1065,1065,1066,1067,1068,1068,1069,1069,1070,1071,1071,1071,1072,1072,1072,1073,1073,1073,1074,1074,1074,1075,1075,1075,1076,1076,1076,1077,1077,1077,1078,1078,1078,1079,1079,1079,1080,1080,1080,1081,1081,1081,1082,1082,1082,1083,1083,1083,1084,1084,1084,1085,1085,1085,1086,1086,1086,1087,1087,1087,1088,1088,1088,1089,1089,1089,1090,1090,1090,1091,1091,1091,1092,1092,1092,1093,1093,1093,1094,1094,1094,1095,1095,1095,1096,1096,1096,1097,1097,1097,1098,1098,1098,1099,1099,1099,1100,1100,1100,1101,1101,1101,1102,1102,1102,1103,1103,1103,1104,1104,1104,1105,1105,1105,1106,1106,1106,1107,1107,1107,1108,1108,1108,1109,1109,1109,1110,1110,1110,1111,1111,1111,1112,1112,1112,1113,1113,1113,1114,1114,1114,1115,1115,1115,1116,1116,1116,1117,1117,1117,1118,1118,1118,1119,1119,1119,1120,1120,1120,1121,1121,1121,1122,1122,1122,1123,1123,1123,1124,1124,1124,1125,1125,1125,1126,1126,1126,1127,1128,1128,1129,1130,1131,1131,1132,1132,1133,1134,1134,1135,1136,1137,1137,1137,1138,1138,1139,1140,1140,1141,1142,1143,1144,1145,1145,1146,1146,1146,1147,1147,1148,1149,1150,1150,1150,1151,1151,1151,1152,1152,1153,1154,1154,1154,1155,1155,1156,1156,1157,1158,1158,1158,1159,1159,1160,1160,1161,1161,1162,1162,1163,1163,1164,1164,1165,1165,1166,1166,1167,1168,1168,1169,1169,1170,1170,1171,1171,1172,1172,1172,1173,1173,1173,1174,1174,1175,1175,1175,1176,1177,1177,1178,1178,1179,1179,1180,1181,1182,1183,1183,1183,1184,1185,1185,1186,1186,1187,1187,1188,1188,1188,1189,1190,1190,1191,1192,1192,1193,1193,1193,1194,1194,1195,1195,1196,1196,1197,1197,1198,1199,1199,1200,1200,1201,1201,1202,1203,1203,1204,1204,1205,1205,1206,1206,1206,1207,1208,1209,1210,1210,1211,1211,1212,1212,1213,1214,1214,1215,1216,1216,1217,1217,1218,1218,1219,1220,1220,1221,1222,1222,1223,1223,1224,1224,1224,1225,1226,1226,1227,1228,1228,1229,1229,1230,1230,1231,1231,1232,1232,1233,1233,1234,1234,1235,1235,1236,1237,1238,1238,1238,1239,1239,1239,1240,1240,1240,1241,1241,1242,1242,1243,1243,1244,1244,1245,1245,1246,1246,1247,1247,1248,1248,1249,1249,1250,1250,1251,1251,1252,1253,1253,1254,1254,1255,1255,1256,1256,1257,1258,1258,1259,1260,1260,1261,1261,1262,1262,1263,1263,1264,1265,1265,1266,1266,1267,1268,1268,1269,1270,1270,1270,1271,1271,1272,1272,1273,1273,1274,1274,1275,1275,1276,1277,1277,1278,1279,1279,1279,1280,1281,1281,1282,1283,1284,1284,1284,1285,1285,1285,1286,1286,1286,1287,1287,1287,1288,1288,1288,1289,1289,1289,1290,1290,1290,1291,1291,1291,1292,1292,1292,1293,1293,1293,1294,1295,1295,1296,1296,1297,1297,1298,1299,1299,1300,1301,1302,1303,1303,1304,1304,1305,1306,1306,1306,1307,1307,1307,1308,1308,1309,1309,1310,1310,1311,1311,1311,1312,1313,1313,1314,1314,1315,1315,1316,1317,1317,1318,1318,1319,1319,1320,1321,1321,1322,1323,1324,1324,1324,1325,1325,1326,1327,1328,1328,1329,1329,1330,1330,1330,1331,1331,1332,1333,1333,1334,1335,1335,1335,1336,1336,1336,1337,1337,1337,1338,1338,1338,1339,1340,1340,1340,1341,1342,1343,1343,1344,1344,1345,1345,1346,1347,1348,1348,1349,1349,1349,1350,1350,1351,1352,1352,1353,1353,1354,1354,1355,1355,1356,1356,1357,1357,1358,1358,1359,1359,1360,1360,1361,1361,1362,1363,1363,1364,1364,1365,1365,1366,1366,1367,1367,1368,1368,1369,1369,1370,1370,1371,1371,1372,1372,1373,1373,1374,1374,1375,1375,1376,1376,1377,1377,1378,1378,1379,1379,1380,1380,1381,1381,1382,1382,1383,1383,1383,1383,1383,1383,1383,1383,1384,1384,1384,1384,1384,1384,1384,1384,1385,1385,1385,1385,1385,1385,1385,1385,1386,1386,1386,1386,1386,1386,1386,1386,1387,1387,1387,1387,1387,1387,1387,1387,1388,1388,1388,1388,1388,1388,1388,1388,1389,1389,1389,1389,1389,1389,1389,1389,1390,1390,1390,1390,1390,1390,1390,1390,1391,1391,1391,1391,1391,1391,1391,1391,1392,1392,1392,1392,1392,1392,1392,1392,1393,1393,1393,1393,1393,1393,1393,1393,1394,1394,1394,1394,1394,1394,1394,1394,1395,1395,1395,1395,1395,1395,1395,1395,1396,1396,1396,1396,1396,1396,1396,1396,1397,1397,1397,1397,1397,1397,1397,1397,1398,1398,1398,1398,1398,1398,1398,1398,1399,1399,1399,1399,1399,1399,1399,1399,1400,1400,1400,1400,1400,1400,1400,1400,1401,1401,1401,1401,1401,1401,1401,1401,1402,1402,1402,1402,1402,1402,1402,1402],"depth":[1,1,1,1,2,1,1,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,3,2,1,1,2,1,1,1,1,1,2,1,2,1,2,1,2,1,3,2,1,2,1,3,2,1,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,3,2,1,1,2,1,1,2,1,2,1,1,3,2,1,1,2,1,1,1,2,1,3,2,1,2,1,1,2,1,3,2,1,2,1,1,1,2,1,1,1,1,2,1,3,2,1,1,1,1,2,1,1,1,2,1,2,1,3,2,1,2,1,2,1,3,2,1,2,1,1,1,2,1,3,2,1,2,1,1,1,3,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,1,3,2,1,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,1,2,1,1,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,1,1,3,2,1,3,2,1,2,1,2,1,2,1,1,1,2,1,2,1,3,2,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,1,1,2,1,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,2,1,3,2,1,1,2,1,3,2,1,2,1,2,1,2,1,1,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,1,2,1,1,2,1,1,2,1,2,1,1,3,2,1,2,1,1,2,1,1,1,3,2,1,3,2,1,2,1,1,1,2,1,1,2,1,4,3,2,1,1,1,3,2,1,2,1,1,2,1,4,3,2,1,4,3,2,1,2,1,2,1,2,1,3,2,1,2,1,4,3,2,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,2,1,1,3,2,1,1,1,2,1,2,1,1,1,2,1,3,2,1,1,2,1,1,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,3,2,1,1,1,2,1,2,1,1,3,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,1,2,1,2,1,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,1,3,2,1,1,2,1,3,2,1,1,2,1,1,1,3,2,1,3,2,1,2,1,2,1,1,2,1,3,2,1,1,2,1,2,1,2,1,2,1,3,2,1,1,1,1,2,1,2,1,1,3,2,1,1,2,1,1,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,1,2,1,1,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,3,2,1,2,1,2,1,1,1,2,1,1,3,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,1,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,1,3,2,1,2,1,4,3,2,1,4,3,2,1,3,2,1,1,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,3,2,1,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,1,2,1,3,2,1,2,1,2,1,1,3,2,1,3,2,1,3,2,1,1,1,1,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,1,2,1,2,1,2,1,2,1,2,1,1,1,1,2,1,2,1,2,1,1,2,1,1,1,2,1,1,2,1,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,1,1,1,2,1,1,1,3,2,1,1,1,2,1,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,2,1,1,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,1,1,2,1,2,1,2,1,1,3,2,1,3,2,1,2,1,2,1,1,2,1,2,1,1,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,1,1,1,1,1,2,1,1,3,2,1,3,2,1,3,2,1,1,1,1,2,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,3,2,1,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,1,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,1,1,1,1,2,1,2,1,2,1,1,1,1,1,1,1,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,1,3,2,1,3,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,1,3,2,1,2,1,1,2,1,1,1,2,1,1,2,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,1,1,4,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,4,3,2,1,4,3,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,1,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,1,2,1,1,1,2,1,2,1,3,2,1,3,2,1,3,2,1,1,2,1,3,2,1,2,1,3,2,1,2,1,2,1,1,3,2,1,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,1,3,2,1,1,1,1,3,2,1,2,1,2,1,3,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,1,4,3,2,1,4,3,2,1,1,2,1,1,1,2,1,1,1,1,3,2,1,3,2,1,1,1,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,1,3,2,1,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,1,1,3,2,1,2,1,2,1,1,1,2,1,2,1,2,1,1,1,2,1,2,1,1,1,1,2,1,2,1,1,2,1,4,3,2,1,4,3,2,1,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,1,2,1,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,1,1,1,4,3,2,1,4,3,2,1,4,3,2,1,2,1,2,1,2,1,1,1,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,1,1,2,1,2,1,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,1,2,1,1,1,2,1,2,1,1,2,1,1,1,3,2,1,2,1,1,2,1,1,1,1,1,2,1,3,2,1,2,1,1,1,3,2,1,3,2,1,2,1,1,3,2,1,2,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,3,2,1,1,2,1,2,1,2,1,1,1,1,3,2,1,1,2,1,2,1,2,1,3,2,1,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,1,1,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,3,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,3,2,1,1,2,1,1,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,1,2,1,1,1,1,2,1,2,1,1,3,2,1,3,2,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,1,1,3,2,1,2,1,1,1,2,1,2,1,3,2,1,2,1,1,2,1,1,3,2,1,3,2,1,3,2,1,3,2,1,1,3,2,1,1,1,2,1,2,1,2,1,1,1,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1],"label":["rowSums","rowSums","rowSums","rowSums","/","local","rowMeans","rowMeans","rowMeans","<GC>","aperm.default","apply","aperm.default","apply","aperm.default","apply","aperm.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","apply","apply","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","<GC>","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","apply","mean.default","apply","apply","apply","apply","apply","is.na","local","FUN","apply","<GC>","apply","is.na","local","isTRUE","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","mean.default","apply","<GC>","mean.default","apply","FUN","apply","length","local","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","<GC>","FUN","apply","apply","FUN","apply","apply","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","mean.default","apply","apply","apply","is.na","local","isTRUE","mean.default","apply","is.numeric","local","apply","FUN","apply","<GC>","mean.default","apply","FUN","apply","apply","apply","mean.default","apply","apply","apply","apply","FUN","apply","<GC>","FUN","apply","apply","apply","apply","length","local","apply","apply","length","local","FUN","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","mean.default","apply","<GC>","FUN","apply","is.numeric","local","apply","apply","isTRUE","mean.default","apply","apply","is.na","local","mean.default","apply","apply","<GC>","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","apply","apply","mean.default","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","<GC>","FUN","apply","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","FUN","apply","apply","<GC>","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","FUN","apply","apply","<GC>","apply","apply","FUN","apply","apply","apply","apply","FUN","apply","mean.default","apply","<GC>","apply","FUN","apply","apply","FUN","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","is.numeric","local","FUN","apply","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","<GC>","mean.default","apply","FUN","apply","is.numeric","local","mean.default","apply","apply","apply","is.numeric","local","is.numeric","local","<GC>","mean.default","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","apply","length","local","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","<GC>","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","apply","apply","<GC>","FUN","apply","FUN","apply","is.na","local","length","local","FUN","apply","FUN","apply","apply","<GC>","apply","is.na","local","is.numeric","local","isTRUE","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","<GC>","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","is.na","local","FUN","apply","mean.default","apply","apply","FUN","apply","apply","<GC>","apply","apply","FUN","apply","apply","FUN","apply","mean.default","apply","apply","<GC>","mean.default","apply","FUN","apply","apply","mean.default","apply","apply","apply","isTRUE","mean.default","apply","<GC>","mean.default","apply","is.na","local","apply","apply","FUN","apply","apply","mean.default","apply","<GC>","isTRUE","mean.default","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","FUN","apply","length","local","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","isTRUE","mean.default","apply","mean.default","apply","apply","is.numeric","local","mean.default","apply","mean.default","apply","mean.default","apply","<GC>","length","local","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","<GC>","FUN","apply","apply","apply","is.numeric","local","mean.default","apply","apply","apply","<GC>","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","apply","apply","<GC>","length","local","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","apply","FUN","apply","mean.default","apply","apply","FUN","apply","apply","FUN","apply","<GC>","FUN","apply","apply","apply","is.numeric","local","mean.default","apply","apply","<GC>","FUN","apply","apply","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","mean.default","apply","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","apply","<GC>","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","apply","FUN","apply","is.na","local","apply","<GC>","is.numeric","local","apply","FUN","apply","apply","apply","length","local","FUN","apply","FUN","apply","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","<GC>","apply","<GC>","apply","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","apply","mean.default","apply","apply","length","local","apply","FUN","apply","mean.default","apply","FUN","apply","<GC>","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","apply","apply","length","local","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","FUN","apply","is.na","local","FUN","apply","mean.default","apply","apply","apply","mean.default","apply","mean.default","apply","mean.default","apply","apply","apply","<GC>","mean.default","apply","apply","FUN","apply","FUN","apply","FUN","apply","is.numeric","local","FUN","apply","apply","mean.default","apply","apply","apply","isTRUE","mean.default","apply","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","apply","is.numeric","local","apply","FUN","apply","isTRUE","mean.default","apply","length","local","FUN","apply","mean.default","apply","FUN","apply","apply","<GC>","FUN","apply","apply","mean.default","apply","is.na","local","FUN","apply","FUN","apply","apply","apply","FUN","apply","is.na","local","FUN","apply","mean.default","apply","apply","is.numeric","local","<GC>","apply","<GC>","apply","mean.default","apply","mean.default","apply","mean.default","apply","length","local","mean.default","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","isTRUE","mean.default","apply","apply","apply","apply","apply","apply","is.numeric","local","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","<GC>","apply","<GC>","apply","mean.default","apply","mean.default","apply","apply","apply","apply","is.numeric","local","FUN","apply","is.na","local","FUN","apply","mean.default","apply","apply","apply","apply","length","local","<GC>","apply","<GC>","apply","apply","mean.default","apply","apply","apply","FUN","apply","apply","FUN","apply","apply","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","apply","mean.default","apply","length","local","apply","FUN","apply","apply","mean.default","apply","apply","FUN","apply","apply","apply","mean.default","apply","is.na","local","<GC>","apply","mean.default","apply","mean.default","apply","length","local","FUN","apply","apply","isTRUE","mean.default","apply","apply","apply","apply","FUN","apply","apply","apply","<GC>","mean.default","apply","apply","apply","is.na","local","apply","mean.default","apply","apply","FUN","apply","length","local","apply","mean.default","apply","is.numeric","local","mean.default","apply","<GC>","apply","apply","is.numeric","local","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","apply","apply","apply","FUN","apply","mean.default","apply","FUN","apply","apply","<GC>","length","local","<GC>","length","local","FUN","apply","mean.default","apply","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","apply","apply","apply","apply","apply","apply","FUN","apply","apply","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","apply","apply","apply","mean.default","apply","apply","apply","apply","apply","FUN","apply","mean.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","mean.default","apply","is.na","local","apply","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","mean.default","apply","FUN","apply","<GC>","apply","mean.default","apply","apply","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","mean.default","apply","FUN","apply","apply","apply","apply","apply","<GC>","apply","<GC>","apply","FUN","apply","apply","apply","apply","apply","apply","apply","apply","isTRUE","mean.default","apply","mean.default","apply","<GC>","apply","<GC>","apply","FUN","apply","apply","FUN","apply","mean.default","apply","apply","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","apply","<GC>","apply","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","<GC>","FUN","apply","FUN","apply","apply","FUN","apply","apply","apply","mean.default","apply","apply","mean.default","apply","mean.default","apply","apply","<GC>","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","length","local","apply","mean.default","apply","length","local","isTRUE","mean.default","apply","apply","apply","<GC>","isTRUE","mean.default","apply","apply","FUN","apply","mean.default","apply","is.na","local","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","length","local","apply","is.numeric","local","FUN","apply","length","local","apply","mean.default","apply","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","length","local","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","apply","FUN","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","is.numeric","local","apply","mean.default","apply","apply","apply","mean.default","apply","is.numeric","local","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","<GC>","apply","<GC>","apply","mean.default","apply","length","local","FUN","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","<GC>","apply","<GC>","apply","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","FUN","apply","<GC>","apply","<GC>","apply","apply","FUN","apply","FUN","apply","apply","is.na","local","FUN","apply","mean.default","apply","apply","<GC>","apply","<GC>","apply","isTRUE","mean.default","apply","mean.default","apply","apply","is.na","local","apply","apply","mean.default","apply","length","local","<GC>","FUN","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","apply","<GC>","mean.default","apply","apply","mean.default","apply","length","local","mean.default","apply","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","<GC>","mean.default","apply","FUN","apply","apply","FUN","apply","mean.default","apply","is.na","local","apply","FUN","apply","FUN","apply","apply","<GC>","FUN","apply","apply","apply","apply","isTRUE","mean.default","apply","mean.default","apply","length","local","isTRUE","mean.default","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","apply","FUN","apply","apply","apply","FUN","apply","apply","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","apply","length","local","apply","FUN","apply","mean.default","apply","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","mean.default","apply","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","is.na","local","<GC>","apply","<GC>","apply","apply","mean.default","apply","is.na","local","is.na","local","apply","apply","isTRUE","mean.default","apply","<GC>","apply","<GC>","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","<GC>","is.numeric","local","<GC>","is.numeric","local","mean.default","apply","mean.default","apply","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","<GC>","apply","<GC>","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","<GC>","apply","<GC>","apply","apply","apply","apply","FUN","apply","mean.default","apply","apply","FUN","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","<GC>","is.na","local","<GC>","is.na","local","apply","FUN","apply","apply","apply","FUN","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","is.numeric","local","FUN","apply","apply","apply","apply","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","mean.default","apply","length","local","FUN","apply","apply","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","is.numeric","local","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","apply","apply","FUN","apply","FUN","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","FUN","apply","apply","apply","mean.default","apply","mean.default","apply","apply","is.numeric","local","apply","apply","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","apply","apply","apply","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","is.na","local","FUN","apply","apply","mean.default","apply","length","local","FUN","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","mean.default","apply","apply","apply","apply","isTRUE","mean.default","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","length","local","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","apply","<GC>","apply","FUN","apply","is.numeric","local","apply","is.na","local","length","local","FUN","apply","apply","length","local","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","apply","FUN","apply","FUN","apply","mean.default","apply","apply","is.na","local","apply","<GC>","apply","<GC>","apply","FUN","apply","apply","FUN","apply","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","is.na","local","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","<GC>","apply","mean.default","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","is.numeric","local","FUN","apply","apply","mean.default","apply","apply","isTRUE","mean.default","apply","apply","mean.default","apply","apply","apply","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","apply","FUN","apply","FUN","apply","FUN","apply","apply","mean.default","apply","apply","apply","apply","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","mean.default","apply","<GC>","apply","<GC>","apply","apply","FUN","apply","FUN","apply","mean.default","apply","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","length","local","apply","apply","is.na","local","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","mean.default","apply","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","isTRUE","mean.default","apply","apply","apply","mean.default","apply","length","local","length","local","apply","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","mayCallBrowserList","mayCallBrowser","mayCallBrowserList","mayCallBrowser","mayCallBrowserList","mayCallBrowser","compile","compiler:::tryCompile","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis"],"filenum":[1,1,1,1,1,null,1,1,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,1,1,null,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,1,null,1,null,1,null,null,1,1,null,1,1,1,1,1,null,null,null,1,null,1,null,null,null,null,1,null,1,null,null,1,1,1,null,1,null,1,null,null,1,null,1,null,null,null,1,null,1,null,1,null,null,1,null,1,null,1,null,null,1,1,null,1,1,null,1,null,1,1,null,null,1,1,null,1,1,1,null,null,null,null,1,null,null,1,null,1,null,null,1,null,1,1,1,null,1,1,1,1,null,1,null,null,1,1,1,1,null,null,1,1,null,null,null,1,null,null,1,null,1,null,1,null,null,1,null,1,1,1,null,1,null,null,1,null,null,1,1,null,null,1,1,null,null,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,1,null,1,1,null,null,1,1,null,1,null,1,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,1,null,1,1,null,1,1,null,1,1,1,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,null,null,1,1,null,1,1,1,null,null,1,null,null,1,null,1,null,null,null,1,1,1,null,null,null,null,null,null,1,null,1,null,1,null,null,1,null,1,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,1,1,null,null,1,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,1,null,1,1,1,null,null,1,null,1,null,null,null,null,null,1,null,1,1,null,1,null,null,null,null,null,null,1,null,1,null,null,1,1,null,1,null,null,1,null,1,null,1,null,1,1,1,null,1,null,null,1,null,null,1,null,null,null,1,null,1,1,null,1,1,null,1,1,null,1,1,null,1,null,1,1,null,null,1,null,1,1,null,1,1,1,null,null,1,null,null,1,null,null,1,1,null,1,1,null,1,null,null,null,1,1,1,null,null,1,null,1,1,null,1,null,null,null,1,null,null,null,1,null,1,null,null,null,1,null,null,1,null,1,null,null,null,1,null,1,1,null,null,null,1,null,1,null,1,null,null,null,1,null,1,null,1,null,1,null,1,1,null,null,1,1,1,null,null,null,1,1,1,null,1,null,null,1,1,null,1,1,1,1,null,null,null,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,1,null,1,null,null,1,1,1,null,null,null,1,1,null,null,1,1,null,1,null,1,null,1,null,null,1,null,null,1,1,null,1,null,1,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,1,null,null,1,1,null,1,null,null,1,1,null,1,1,1,null,null,1,null,null,1,null,1,null,1,1,null,1,null,null,1,1,null,1,null,1,null,1,null,1,null,null,1,1,1,1,null,1,null,null,1,null,null,null,1,null,1,1,1,null,null,null,1,null,1,1,null,1,1,null,1,null,1,null,1,null,1,1,null,null,1,null,1,null,1,1,null,1,1,null,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,1,null,1,null,null,1,null,1,null,1,1,1,null,null,1,null,null,1,null,1,null,null,1,null,null,1,null,null,1,null,1,null,null,null,1,null,1,1,1,null,1,null,1,null,1,1,1,null,null,1,1,null,1,null,1,null,1,null,null,null,1,1,null,1,1,1,null,null,1,null,1,null,null,null,1,null,null,null,1,null,null,1,1,1,null,null,1,null,1,null,null,1,null,null,null,1,null,1,null,1,1,null,null,1,1,null,1,null,null,null,1,null,1,1,1,null,1,null,null,null,1,null,1,1,null,null,null,1,null,1,null,1,null,1,null,1,null,null,null,1,null,null,1,null,null,1,1,null,1,null,null,1,null,1,null,1,1,null,null,1,null,null,1,null,null,1,1,1,1,1,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,1,1,null,null,null,1,null,null,null,1,null,1,1,1,1,null,null,null,1,null,1,1,null,1,1,1,null,1,1,null,1,1,null,1,1,null,null,1,null,1,null,1,null,1,null,null,1,null,1,1,null,1,1,null,1,1,1,null,1,null,null,null,1,null,1,null,1,null,null,null,1,1,null,null,1,1,1,1,null,1,1,1,null,null,1,1,1,null,null,1,null,1,1,null,1,null,null,1,null,1,null,null,null,1,null,1,1,null,null,null,1,null,null,1,null,1,null,1,1,1,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,1,1,1,1,null,1,null,1,null,1,1,null,null,null,null,null,null,null,1,null,1,1,null,1,null,1,1,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,1,1,1,1,1,1,1,null,1,1,null,null,null,null,null,null,null,null,null,1,1,1,null,1,1,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,1,null,1,null,null,1,1,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,null,1,1,null,1,null,1,null,1,null,1,1,null,null,1,null,null,1,null,1,null,1,null,1,1,null,1,null,1,1,1,1,1,null,1,null,1,null,1,1,1,1,1,1,1,1,null,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,1,1,null,null,1,null,null,1,null,1,null,1,null,1,1,null,null,1,null,null,1,null,1,null,1,1,null,1,null,1,null,1,1,null,null,1,null,1,1,null,1,1,1,null,1,1,null,1,null,1,1,null,1,null,null,1,null,1,null,1,null,null,1,null,1,null,null,null,null,1,1,1,null,null,null,1,1,null,1,null,1,null,null,null,1,null,1,null,1,null,1,null,1,null,1,null,null,null,1,null,null,null,1,null,null,1,null,null,null,1,null,null,1,null,1,null,1,1,null,null,1,null,null,1,1,null,1,null,null,null,1,null,1,null,1,null,1,1,1,null,1,null,null,1,null,1,null,1,null,null,1,null,1,1,1,null,1,null,null,null,1,null,null,1,null,null,1,null,null,1,null,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,null,1,null,1,null,1,1,null,null,1,1,null,1,null,1,1,null,1,null,1,null,1,null,1,1,1,null,1,null,1,null,1,null,1,1,null,1,null,1,1,null,null,null,1,null,1,1,null,1,null,1,null,null,1,null,1,1,null,null,1,1,null,1,null,null,null,null,1,null,null,1,null,null,1,1,null,1,null,null,1,null,1,null,null,1,null,1,null,1,1,null,null,1,1,null,1,null,null,null,1,1,1,null,1,null,1,null,1,null,null,1,null,1,1,null,1,null,1,null,null,1,null,1,null,1,1,null,null,1,1,1,1,null,null,1,null,1,null,null,null,null,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,1,null,1,null,1,null,1,null,1,null,1,null,null,1,1,1,null,null,null,1,null,null,null,1,1,null,1,1,1,null,1,1,1,1,null,null,1,null,null,1,1,1,null,null,1,null,1,null,1,null,null,null,null,null,null,null,null,null,1,null,1,null,1,1,null,1,null,1,null,1,null,null,null,1,null,1,1,null,1,null,null,null,null,1,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,null,1,null,1,null,null,null,null,null,null,null,1,null,1,1,null,1,1,null,null,1,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,1,1,null,null,1,null,1,null,1,1,1,null,1,null,1,null,1,1,1,null,1,null,1,1,1,1,null,1,null,1,1,null,1,null,null,null,1,null,null,null,1,1,null,1,1,null,1,null,1,null,1,null,1,null,null,null,null,null,null,1,null,1,1,1,null,1,null,1,1,null,1,null,1,null,null,null,1,1,1,1,1,null,null,null,1,null,null,null,1,null,null,null,1,null,1,null,null,null,1,1,1,null,1,null,null,1,null,null,1,1,null,null,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,1,1,null,1,null,1,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,1,null,1,1,1,null,1,null,1,1,null,null,1,1,null,null,1,null,1,1,null,1,1,1,1,1,null,1,null,null,1,null,1,1,1,null,null,1,null,null,1,null,1,1,null,null,1,null,1,null,1,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,null,1,1,null,1,null,null,null,1,null,1,null,null,1,null,null,1,null,1,null,null,1,1,null,1,null,1,null,1,1,1,1,null,null,1,1,null,1,null,1,null,1,null,null,1,1,null,null,1,null,1,null,null,1,null,1,null,1,null,1,null,null,1,null,null,null,null,null,1,1,null,null,null,1,null,1,null,null,1,1,1,1,null,1,null,1,null,1,1,null,null,1,null,1,null,1,null,1,1,null,1,1,null,1,null,1,null,null,1,1,null,1,1,null,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,1,null,1,1,null,1,null,1,null,1,null,1,1,null,1,null,1,1,null,1,1,null,null,1,null,1,null,1,null,1,null,null,null,1,1,null,1,1,null,null,1,1,null,1,1,1,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,1,null,1,null,1,null,1,1,null,1,1,1,1,null,1,null,1,1,null,null,1,null,null,1,null,1,null,1,null,1,null,null,1,1,null,1,null,1,null,1,1,null,1,null,1,null,1,1,null,1,1,1,null,null,1,null,null,1,1,null,null,null,1,null,null,1,null,1,1,null,1,1,null,null,1,null,null,1,null,null,1,null,null,1,1,null,null,1,1,1,null,1,null,null,null,null,1,1,null,1,null,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,null,null,null,null,null,1,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null],"linenum":[10,10,10,10,10,null,11,11,11,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,12,12,null,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,12,null,12,null,12,null,null,12,12,null,12,12,12,12,12,null,null,null,12,null,12,null,null,null,null,12,null,12,null,null,12,12,12,null,12,null,12,null,null,12,null,12,null,null,null,12,null,12,null,12,null,null,12,null,12,null,12,null,null,12,12,null,12,12,null,12,null,12,12,null,null,12,12,null,12,12,12,null,null,null,null,12,null,null,12,null,12,null,null,12,null,12,12,12,null,12,12,12,12,null,12,null,null,12,12,12,12,null,null,12,12,null,null,null,12,null,null,12,null,12,null,12,null,null,12,null,12,12,12,null,12,null,null,12,null,null,12,12,null,null,12,12,null,null,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,12,null,12,12,null,null,12,12,null,12,null,12,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,12,null,12,12,null,12,12,null,12,12,12,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,null,null,12,12,null,12,12,12,null,null,12,null,null,12,null,12,null,null,null,12,12,12,null,null,null,null,null,null,12,null,12,null,12,null,null,12,null,12,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,12,12,null,null,12,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,12,null,12,12,12,null,null,12,null,12,null,null,null,null,null,12,null,12,12,null,12,null,null,null,null,null,null,12,null,12,null,null,12,12,null,12,null,null,12,null,12,null,12,null,12,12,12,null,12,null,null,12,null,null,12,null,null,null,12,null,12,12,null,12,12,null,12,12,null,12,12,null,12,null,12,12,null,null,12,null,12,12,null,12,12,12,null,null,12,null,null,12,null,null,12,12,null,12,12,null,12,null,null,null,12,12,12,null,null,12,null,12,12,null,12,null,null,null,12,null,null,null,12,null,12,null,null,null,12,null,null,12,null,12,null,null,null,12,null,12,12,null,null,null,12,null,12,null,12,null,null,null,12,null,12,null,12,null,12,null,12,12,null,null,12,12,12,null,null,null,12,12,12,null,12,null,null,12,12,null,12,12,12,12,null,null,null,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,12,null,12,null,null,12,12,12,null,null,null,12,12,null,null,12,12,null,12,null,12,null,12,null,null,12,null,null,12,12,null,12,null,12,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,12,null,null,12,12,null,12,null,null,12,12,null,12,12,12,null,null,12,null,null,12,null,12,null,12,12,null,12,null,null,12,12,null,12,null,12,null,12,null,12,null,null,12,12,12,12,null,12,null,null,12,null,null,null,12,null,12,12,12,null,null,null,12,null,12,12,null,12,12,null,12,null,12,null,12,null,12,12,null,null,12,null,12,null,12,12,null,12,12,null,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,12,null,12,null,null,12,null,12,null,12,12,12,null,null,12,null,null,12,null,12,null,null,12,null,null,12,null,null,12,null,12,null,null,null,12,null,12,12,12,null,12,null,12,null,12,12,12,null,null,12,12,null,12,null,12,null,12,null,null,null,12,12,null,12,12,12,null,null,12,null,12,null,null,null,12,null,null,null,12,null,null,12,12,12,null,null,12,null,12,null,null,12,null,null,null,12,null,12,null,12,12,null,null,12,12,null,12,null,null,null,12,null,12,12,12,null,12,null,null,null,12,null,12,12,null,null,null,12,null,12,null,12,null,12,null,12,null,null,null,12,null,null,12,null,null,12,12,null,12,null,null,12,null,12,null,12,12,null,null,12,null,null,12,null,null,12,12,12,12,12,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,12,12,null,null,null,12,null,null,null,12,null,12,12,12,12,null,null,null,12,null,12,12,null,12,12,12,null,12,12,null,12,12,null,12,12,null,null,12,null,12,null,12,null,12,null,null,12,null,12,12,null,12,12,null,12,12,12,null,12,null,null,null,12,null,12,null,12,null,null,null,12,12,null,null,12,12,12,12,null,12,12,12,null,null,12,12,12,null,null,12,null,12,12,null,12,null,null,12,null,12,null,null,null,12,null,12,12,null,null,null,12,null,null,12,null,12,null,12,12,12,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,12,12,12,12,null,12,null,12,null,12,12,null,null,null,null,null,null,null,12,null,12,12,null,12,null,12,12,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,12,12,12,12,12,12,12,null,12,12,null,null,null,null,null,null,null,null,null,12,12,12,null,12,12,12,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,12,null,12,null,null,12,12,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,null,12,12,null,12,null,12,null,12,null,12,12,null,null,12,null,null,12,null,12,null,12,null,12,12,null,12,null,12,12,12,12,12,null,12,null,12,null,12,12,12,12,12,12,12,12,null,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,12,12,null,null,12,null,null,12,null,12,null,12,null,12,12,null,null,12,null,null,12,null,12,null,12,12,null,12,null,12,null,12,12,null,null,12,null,12,12,null,12,12,12,null,12,12,null,12,null,12,12,null,12,null,null,12,null,12,null,12,null,null,12,null,12,null,null,null,null,12,12,12,null,null,null,12,12,null,12,null,12,null,null,null,12,null,12,null,12,null,12,null,12,null,12,null,null,null,12,null,null,null,12,null,null,12,null,null,null,12,null,null,12,null,12,null,12,12,null,null,12,null,null,12,12,null,12,null,null,null,12,null,12,null,12,null,12,12,12,null,12,null,null,12,null,12,null,12,null,null,12,null,12,12,12,null,12,null,null,null,12,null,null,12,null,null,12,null,null,12,null,12,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,null,12,null,12,null,12,12,null,null,12,12,null,12,null,12,12,null,12,null,12,null,12,null,12,12,12,null,12,null,12,null,12,null,12,12,null,12,null,12,12,null,null,null,12,null,12,12,null,12,null,12,null,null,12,null,12,12,null,null,12,12,null,12,null,null,null,null,12,null,null,12,null,null,12,12,null,12,null,null,12,null,12,null,null,12,null,12,null,12,12,null,null,12,12,null,12,null,null,null,12,12,12,null,12,null,12,null,12,null,null,12,null,12,12,null,12,null,12,null,null,12,null,12,null,12,12,null,null,12,12,12,12,null,null,12,null,12,null,null,null,null,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,12,null,12,null,12,null,12,null,12,null,12,null,null,12,12,12,null,null,null,12,null,null,null,12,12,null,12,12,12,null,12,12,12,12,null,null,12,null,null,12,12,12,null,null,12,null,12,null,12,null,null,null,null,null,null,null,null,null,12,null,12,null,12,12,null,12,null,12,null,12,null,null,null,12,null,12,12,null,12,null,null,null,null,12,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,null,12,null,12,null,null,null,null,null,null,null,12,null,12,12,null,12,12,null,null,12,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,12,12,null,null,12,null,12,null,12,12,12,null,12,null,12,null,12,12,12,null,12,null,12,12,12,12,null,12,null,12,12,null,12,null,null,null,12,null,null,null,12,12,null,12,12,null,12,null,12,null,12,null,12,null,null,null,null,null,null,12,null,12,12,12,null,12,null,12,12,null,12,null,12,null,null,null,12,12,12,12,12,null,null,null,12,null,null,null,12,null,null,null,12,null,12,null,null,null,12,12,12,null,12,null,null,12,null,null,12,12,null,null,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,12,12,null,12,null,12,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,12,null,12,12,12,null,12,null,12,12,null,null,12,12,null,null,12,null,12,12,null,12,12,12,12,12,null,12,null,null,12,null,12,12,12,null,null,12,null,null,12,null,12,12,null,null,12,null,12,null,12,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,null,12,12,null,12,null,null,null,12,null,12,null,null,12,null,null,12,null,12,null,null,12,12,null,12,null,12,null,12,12,12,12,null,null,12,12,null,12,null,12,null,12,null,null,12,12,null,null,12,null,12,null,null,12,null,12,null,12,null,12,null,null,12,null,null,null,null,null,12,12,null,null,null,12,null,12,null,null,12,12,12,12,null,12,null,12,null,12,12,null,null,12,null,12,null,12,null,12,12,null,12,12,null,12,null,12,null,null,12,12,null,12,12,null,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,12,null,12,12,null,12,null,12,null,12,null,12,12,null,12,null,12,12,null,12,12,null,null,12,null,12,null,12,null,12,null,null,null,12,12,null,12,12,null,null,12,12,null,12,12,12,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,12,null,12,null,12,null,12,12,null,12,12,12,12,null,12,null,12,12,null,null,12,null,null,12,null,12,null,12,null,12,null,null,12,12,null,12,null,12,null,12,12,null,12,null,12,null,12,12,null,12,12,12,null,null,12,null,null,12,12,null,null,null,12,null,null,12,null,12,12,null,12,12,null,null,12,null,null,12,null,null,12,null,null,12,12,null,null,12,12,12,null,12,null,null,null,null,12,12,null,12,null,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,null,null,null,null,null,13,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null],"memalloc":[124.45849609375,124.45849609375,124.45849609375,124.45849609375,124.4585189819336,124.4585189819336,139.7407302856445,139.7407302856445,139.7407302856445,139.741096496582,139.741096496582,139.741096496582,170.2064743041992,170.2064743041992,170.2064743041992,170.2064743041992,170.2064743041992,170.2064743041992,170.2065200805664,170.2065200805664,170.2065200805664,170.2065200805664,170.2065200805664,170.2065200805664,170.2065200805664,170.2065200805664,170.2065200805664,170.2065200805664,170.2065200805664,170.2065200805664,170.2065200805664,170.2065200805664,170.2062149047852,170.2062149047852,185.4650039672852,185.6904220581055,185.9454956054688,186.2241897583008,186.2241897583008,186.2241897583008,186.5386428833008,186.5386428833008,186.8830795288086,186.8830795288086,187.2368392944336,187.2368392944336,187.617431640625,187.617431640625,188.0238494873047,188.0238494873047,188.4741744995117,188.7214279174805,188.7214279174805,185.8330383300781,185.8330383300781,186.2011489868164,186.2011489868164,186.5519943237305,186.5519943237305,186.9176330566406,186.9176330566406,187.2828216552734,187.2828216552734,187.6644821166992,187.6644821166992,187.6644821166992,188.0373992919922,188.3486938476562,188.3486938476562,188.6976470947266,188.6976470947266,188.7911911010742,188.7911911010742,188.7911911010742,186.0452194213867,186.40966796875,186.40966796875,186.7987213134766,187.1936416625977,187.5751953125,187.9703674316406,188.3660278320312,188.3660278320312,188.7413558959961,188.7413558959961,188.8781051635742,188.8781051635742,186.1157455444336,186.1157455444336,186.4614181518555,186.4614181518555,186.4614181518555,186.8323516845703,186.8323516845703,187.2172012329102,187.2172012329102,187.2172012329102,187.6057434082031,187.9802169799805,188.3642578125,188.3642578125,188.7480392456055,188.7480392456055,188.9637451171875,188.9637451171875,188.9637451171875,186.2034072875977,186.2034072875977,186.5478210449219,186.5478210449219,186.916862487793,186.916862487793,187.2977981567383,187.2977981567383,187.6861267089844,187.6861267089844,188.0734252929688,188.0734252929688,188.0734252929688,188.4594497680664,188.4594497680664,188.8578033447266,188.8578033447266,189.0479888916016,189.0479888916016,189.0479888916016,186.3738479614258,186.7589645385742,186.7589645385742,187.1277465820312,187.5082778930664,187.5082778930664,187.899543762207,187.899543762207,188.2882995605469,188.6827163696289,188.6827163696289,188.6827163696289,189.0823822021484,186.2846755981445,186.2846755981445,186.6185836791992,186.9729385375977,187.3356094360352,187.3356094360352,187.7172775268555,187.7172775268555,187.7172775268555,188.1045608520508,188.1045608520508,188.4922180175781,188.886100769043,188.886100769043,189.2123336791992,189.2123336791992,189.2123336791992,186.4991455078125,186.4991455078125,186.8262939453125,187.1854934692383,187.5478210449219,187.5478210449219,187.9261703491211,188.3099365234375,188.6930618286133,189.08740234375,189.08740234375,189.2925491333008,189.2925491333008,189.2925491333008,186.7161560058594,187.0557098388672,187.4167327880859,187.7798461914062,187.7798461914062,188.1465682983398,188.5219802856445,188.907829284668,188.907829284668,189.2950592041016,189.2950592041016,189.3714141845703,189.3714141845703,189.3714141845703,186.9334564208984,186.9334564208984,187.28369140625,187.28369140625,187.6417007446289,187.6417007446289,187.6417007446289,188.0082321166992,188.0082321166992,188.3822479248047,188.7619018554688,189.1465835571289,189.1465835571289,189.4490814208984,189.4490814208984,189.4490814208984,186.9049453735352,186.9049453735352,187.2383804321289,187.5915451049805,187.9479598999023,187.9479598999023,187.9479598999023,188.3177337646484,188.6937484741211,188.6937484741211,189.0741577148438,189.0741577148438,189.4623641967773,189.5254364013672,189.5254364013672,187.1729507446289,187.1729507446289,187.5127029418945,187.5127029418945,187.8662338256836,187.8662338256836,188.2312393188477,188.2312393188477,188.6069183349609,188.6069183349609,188.9889984130859,188.9889984130859,189.3745193481445,189.3745193481445,189.6006393432617,189.6006393432617,187.1688461303711,187.498176574707,187.498176574707,187.848388671875,187.848388671875,188.2105865478516,188.2105865478516,188.5874938964844,188.970573425293,188.970573425293,189.3640518188477,189.6745834350586,189.6745834350586,189.6745834350586,187.2133865356445,187.5322418212891,187.5322418212891,187.8754959106445,187.8754959106445,188.2334976196289,188.6075439453125,188.6075439453125,188.9870986938477,188.9870986938477,189.3787612915039,189.7473297119141,189.7473297119141,187.2832336425781,187.2832336425781,187.595100402832,187.595100402832,187.9316711425781,187.9316711425781,188.2838439941406,188.2838439941406,188.6525497436523,189.0350646972656,189.0350646972656,189.4704208374023,189.8189163208008,189.8189163208008,187.4021606445312,187.7129287719727,187.7129287719727,188.0419158935547,188.3941955566406,188.7619247436523,189.1444625854492,189.1444625854492,189.539176940918,189.539176940918,189.8893585205078,189.8893585205078,187.5057373046875,187.5057373046875,187.8074493408203,188.1263961791992,188.1263961791992,188.4638366699219,188.4638366699219,188.8190231323242,188.8190231323242,189.187744140625,189.5691833496094,189.5691833496094,189.9585647583008,189.9585647583008,189.9585647583008,187.5834579467773,187.5834579467773,187.8815689086914,187.8815689086914,188.1965484619141,188.1965484619141,188.5396041870117,188.5396041870117,188.9007415771484,188.9007415771484,189.2783584594727,189.2783584594727,189.6586227416992,189.6586227416992,189.6586227416992,190.0267639160156,190.0267639160156,190.0267639160156,187.6875,187.6875,187.9771728515625,187.9771728515625,188.284782409668,188.6206436157227,188.6206436157227,188.9765853881836,189.3473587036133,189.7274017333984,189.7274017333984,189.7274017333984,190.0937881469727,190.0937881469727,190.0937881469727,187.8109970092773,187.8109970092773,188.0977630615234,188.0977630615234,188.4060592651367,188.4060592651367,188.7782897949219,189.1363677978516,189.5113830566406,189.5113830566406,189.8986587524414,189.8986587524414,190.1597595214844,190.1597595214844,190.1597595214844,187.990234375,187.990234375,188.2836685180664,188.2836685180664,188.5986328125,188.5986328125,188.5986328125,188.9462509155273,188.9462509155273,189.3128662109375,189.6920166015625,189.6920166015625,190.0659561157227,190.0659561157227,190.2246322631836,190.2246322631836,190.2246322631836,190.2246322631836,190.2246322631836,190.2246322631836,190.2246322631836,190.2246322631836,190.2246322631836,190.2246322631836,190.2246322631836,190.2246322631836,190.2246322631836,190.2246322631836,190.2246322631836,190.2246322631836,190.2246322631836,190.2246322631836,190.2246322631836,190.2246322631836,190.2246322631836,190.2246322631836,190.2246322631836,190.2246322631836,190.2246322631836,190.2246322631836,190.2246322631836,188.0438232421875,188.2550277709961,188.4847564697266,188.4847564697266,188.7351303100586,189.0199279785156,189.337776184082,189.337776184082,189.6723709106445,189.6723709106445,190.0238418579102,190.0238418579102,190.2882843017578,190.2882843017578,190.2882843017578,188.1683959960938,188.1683959960938,188.4732208251953,188.4732208251953,188.7769088745117,188.7769088745117,189.1162796020508,189.4767227172852,189.4767227172852,189.8529968261719,190.2385177612305,190.3511199951172,190.3511199951172,190.3511199951172,188.3692092895508,188.3692092895508,188.6535110473633,188.6535110473633,188.9741287231445,188.9741287231445,189.3274841308594,189.3274841308594,189.6993865966797,189.6993865966797,190.0622024536133,190.4129791259766,190.4129791259766,188.2900314331055,188.2900314331055,188.5602645874023,188.5602645874023,188.848030090332,188.848030090332,188.848030090332,189.1781463623047,189.1781463623047,189.5309906005859,189.5309906005859,189.5309906005859,189.8972473144531,190.2746276855469,190.2746276855469,190.4738082885742,190.4738082885742,190.4738082885742,188.4912261962891,188.4912261962891,188.7646255493164,188.7646255493164,189.0769271850586,189.0769271850586,189.4219818115234,189.7848663330078,190.1524887084961,190.1524887084961,190.5337371826172,190.5337371826172,190.5337371826172,190.5337371826172,190.5337371826172,190.5337371826172,188.7259902954102,188.7259902954102,189.01708984375,189.01708984375,189.3452377319336,189.3452377319336,189.6971206665039,190.0666122436523,190.0666122436523,190.4859848022461,190.5925674438477,190.5925674438477,188.7361145019531,189.0140075683594,189.0140075683594,189.3343200683594,189.6827392578125,189.6827392578125,190.0470886230469,190.0470886230469,190.4238510131836,190.6505508422852,190.6505508422852,190.6505508422852,188.7410049438477,188.7410049438477,189.0109481811523,189.3169097900391,189.3169097900391,189.6585006713867,190.0193481445312,190.391487121582,190.391487121582,190.391487121582,190.7075424194336,190.7075424194336,190.7075424194336,188.7766952514648,188.7766952514648,189.0445098876953,189.3452758789062,189.6856307983398,189.6856307983398,190.0442581176758,190.4175872802734,190.4175872802734,190.7636184692383,190.7636184692383,190.7636184692383,190.7636184692383,188.8380432128906,189.1004791259766,189.3918075561523,189.3918075561523,189.3918075561523,189.7236633300781,189.7236633300781,190.0753173828125,190.4409561157227,190.4409561157227,190.8187713623047,190.8187713623047,190.8187713623047,190.8187713623047,190.8187713623047,190.8187713623047,190.8187713623047,190.8187713623047,189.1615829467773,189.1615829467773,189.4529190063477,189.4529190063477,189.7841949462891,189.7841949462891,190.1391830444336,190.1391830444336,190.1391830444336,190.5462799072266,190.5462799072266,190.8730316162109,190.8730316162109,190.8730316162109,190.8730316162109,189.0230102539062,189.0230102539062,189.2851104736328,189.5799942016602,189.5799942016602,189.9137649536133,189.9137649536133,190.2654190063477,190.2654190063477,190.6265106201172,190.6265106201172,190.9264068603516,190.9264068603516,190.9264068603516,189.0942077636719,189.3480529785156,189.3480529785156,189.6388168334961,189.6388168334961,189.9688873291016,189.9688873291016,190.3201904296875,190.3201904296875,190.6861267089844,190.9789428710938,190.9789428710938,190.9789428710938,189.1979751586914,189.4588623046875,189.753547668457,189.753547668457,190.0890579223633,190.0890579223633,190.4442749023438,190.811897277832,191.030647277832,191.030647277832,189.3289260864258,189.3289260864258,189.3289260864258,189.5963973999023,189.8997268676758,189.8997268676758,190.2397994995117,190.5971374511719,190.9668655395508,191.0814361572266,191.0814361572266,191.0814361572266,189.4721755981445,189.4721755981445,189.7431488037109,189.7431488037109,190.0536804199219,190.0536804199219,190.430305480957,190.430305480957,190.7888107299805,190.7888107299805,191.1315155029297,191.1315155029297,191.1315155029297,191.1315155029297,191.1315155029297,191.1315155029297,189.6497955322266,189.9372940063477,189.9372940063477,190.2671890258789,190.2671890258789,190.6198272705078,190.6198272705078,190.9890441894531,190.9890441894531,191.1807174682617,191.1807174682617,189.5755081176758,189.5755081176758,189.839485168457,189.839485168457,190.1433486938477,190.4830703735352,190.4830703735352,190.8419876098633,191.2156829833984,191.2156829833984,191.2291946411133,191.2291946411133,191.2291946411133,189.7685928344727,190.0513610839844,190.3815689086914,190.3815689086914,190.7355270385742,190.7355270385742,191.1036148071289,191.2768096923828,191.2768096923828,191.2768096923828,189.7328643798828,190.0044555664062,190.0044555664062,190.3195877075195,190.3195877075195,190.6629943847656,190.6629943847656,191.0201263427734,191.0201263427734,191.0201263427734,191.3236770629883,191.3236770629883,191.3236770629883,189.7170257568359,189.9685363769531,189.9685363769531,190.2599487304688,190.2599487304688,190.5924758911133,190.9838104248047,190.9838104248047,191.3444290161133,191.3444290161133,191.3444290161133,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,191.3698501586914,189.7817153930664,189.7817153930664,189.7817153930664,189.8534698486328,189.8534698486328,190.1073837280273,190.3802719116211,190.3802719116211,190.3802719116211,190.6874618530273,191.0157089233398,191.0157089233398,191.3345260620117,191.3345260620117,191.3345260620117,191.7034072875977,192.1032485961914,192.1032485961914,192.5070877075195,192.8566360473633,193.1915740966797,193.1915740966797,193.1915740966797,193.5267333984375,193.5267333984375,193.5267333984375,193.8617095947266,193.8617095947266,194.1954498291016,194.1954498291016,194.5287475585938,194.6210479736328,194.6210479736328,190.131233215332,190.131233215332,190.131233215332,190.4528579711914,190.8045120239258,190.8045120239258,191.1468658447266,191.1468658447266,191.4908218383789,191.4908218383789,191.8831787109375,191.8831787109375,192.2934646606445,192.2934646606445,192.2934646606445,192.7007751464844,193.108512878418,193.5144577026367,193.9201583862305,193.9201583862305,194.3293380737305,194.3293380737305,194.7209625244141,194.7534408569336,194.7534408569336,194.7534408569336,190.4107208251953,190.7365112304688,190.7365112304688,191.0791091918945,191.4015655517578,191.7606353759766,191.7606353759766,192.1455841064453,192.1455841064453,192.5459136962891,192.5459136962891,192.9454040527344,193.3548126220703,193.3548126220703,193.7624893188477,194.1702270507812,194.1702270507812,194.5771942138672,194.5771942138672,194.883659362793,194.883659362793,194.883659362793,194.883659362793,190.6680374145508,190.9908676147461,190.9908676147461,190.9908676147461,191.3244476318359,191.3244476318359,191.6547317504883,191.6547317504883,192.0277328491211,192.419807434082,192.419807434082,192.8206024169922,193.2259292602539,193.2259292602539,193.6341094970703,194.0414962768555,194.0414962768555,194.4449310302734,194.4449310302734,194.8444747924805,194.8444747924805,195.0117645263672,195.0117645263672,195.0117645263672,190.6664047241211,190.6664047241211,190.6664047241211,190.9604797363281,190.9604797363281,191.28271484375,191.28271484375,191.5966033935547,191.5966033935547,191.5966033935547,191.9477081298828,191.9477081298828,192.3264389038086,192.3264389038086,192.7254867553711,193.1336441040039,193.5446014404297,193.5446014404297,193.9548034667969,194.3640365600586,194.3640365600586,194.3640365600586,194.8153381347656,194.8153381347656,195.1378784179688,195.1378784179688,195.1378784179688,195.1378784179688,195.1378784179688,195.1378784179688,191.0296859741211,191.0296859741211,191.0296859741211,191.3385162353516,191.3385162353516,191.6514053344727,191.6514053344727,191.9918670654297,191.9918670654297,192.3643493652344,192.3643493652344,192.7587051391602,193.1640472412109,193.5695495605469,193.5695495605469,193.9787292480469,193.9787292480469,194.389030456543,194.389030456543,194.8000335693359,195.2000274658203,195.2618560791016,195.2618560791016,195.2618560791016,191.1230239868164,191.4163589477539,191.4163589477539,191.7197418212891,191.7197418212891,192.046142578125,192.046142578125,192.4092025756836,192.4092025756836,192.7928466796875,192.7928466796875,193.1938171386719,193.5547332763672,193.5547332763672,193.9235458374023,194.3166122436523,194.7000503540039,194.7000503540039,194.7000503540039,195.0915603637695,195.0915603637695,195.3838882446289,195.3838882446289,195.3838882446289,195.3838882446289,195.3838882446289,195.3838882446289,195.3838882446289,195.3838882446289,191.3755187988281,191.3755187988281,191.3755187988281,191.6585311889648,191.9462051391602,192.2799301147461,192.2799301147461,192.6366348266602,193.018310546875,193.018310546875,193.4150695800781,193.4150695800781,193.4150695800781,193.8135833740234,193.8135833740234,194.2165145874023,194.2165145874023,194.6242904663086,194.6242904663086,195.0304794311523,195.0304794311523,195.4174041748047,195.5039291381836,195.5039291381836,195.5039291381836,191.4698791503906,191.724967956543,191.724967956543,192.0250473022461,192.0250473022461,192.3320999145508,192.3320999145508,192.6272659301758,192.6272659301758,192.9523086547852,193.3025512695312,193.6095657348633,193.6095657348633,193.9291381835938,193.9291381835938,194.2737426757812,194.2737426757812,194.6270217895508,194.6270217895508,194.9276351928711,195.3108215332031,195.3108215332031,195.6219940185547,195.6219940185547,195.6219940185547,195.6219940185547,191.6188812255859,191.6188812255859,191.8773956298828,191.8773956298828,192.1253433227539,192.1253433227539,192.4020690917969,192.4020690917969,192.7333526611328,192.7333526611328,193.0576171875,193.0576171875,193.0576171875,193.4176864624023,193.4176864624023,193.4176864624023,193.7734222412109,194.1395797729492,194.1395797729492,194.4694900512695,194.4694900512695,194.4694900512695,194.8102874755859,194.8102874755859,195.1865234375,195.1865234375,195.5364303588867,195.7382125854492,195.7382125854492,195.7382125854492,195.7382125854492,195.7382125854492,195.7382125854492,191.944953918457,191.944953918457,191.944953918457,192.1904907226562,192.4657135009766,192.7847595214844,193.1097412109375,193.4653244018555,193.8351745605469,193.8351745605469,194.2084655761719,194.5314636230469,194.5314636230469,194.8827667236328,194.8827667236328,195.2109603881836,195.2109603881836,195.5434646606445,195.5434646606445,195.8525009155273,195.8525009155273,195.8525009155273,195.8525009155273,191.9695053100586,191.9695053100586,192.2301254272461,192.2301254272461,192.4738693237305,192.7207641601562,193.0164413452148,193.3499755859375,193.3499755859375,193.606689453125,193.606689453125,193.8927383422852,193.8927383422852,194.2259292602539,194.2259292602539,194.5179824829102,194.5179824829102,194.7988586425781,195.1337356567383,195.4853897094727,195.7150421142578,195.7150421142578,195.9650192260742,195.9650192260742,195.9650192260742,195.9650192260742,192.1861343383789,192.4242935180664,192.4242935180664,192.6787719726562,193.0057830810547,193.3356781005859,193.3356781005859,193.6869812011719,194.0558471679688,194.0558471679688,194.4410018920898,194.8375930786133,194.8375930786133,195.2382583618164,195.6405792236328,195.6405792236328,195.6405792236328,196.0411682128906,196.0411682128906,196.0756530761719,196.0756530761719,192.3739013671875,192.3739013671875,192.6255416870117,192.6255416870117,192.9083633422852,193.2229919433594,193.2229919433594,193.5631408691406,193.9231643676758,193.9231643676758,194.2696075439453,194.6071472167969,194.6071472167969,194.9973754882812,195.3934555053711,195.7584915161133,195.7584915161133,196.1362762451172,196.1362762451172,196.1845703125,196.1845703125,192.521598815918,192.521598815918,192.7749862670898,192.7749862670898,193.0464096069336,193.0464096069336,193.35546875,193.35546875,193.6633605957031,194.0162734985352,194.0162734985352,194.0162734985352,194.3889541625977,194.7490310668945,195.13525390625,195.5377960205078,195.5377960205078,195.9179458618164,196.2915344238281,196.2917022705078,196.2917022705078,196.2917022705078,192.7182998657227,192.9254302978516,193.1731643676758,193.1731643676758,193.4706344604492,193.7718963623047,193.7718963623047,194.1417617797852,194.5035934448242,194.5035934448242,194.8747482299805,194.8747482299805,195.2236404418945,195.6002044677734,195.6002044677734,195.9957122802734,195.9957122802734,196.3501892089844,196.3501892089844,196.3970565795898,196.3970565795898,192.8246994018555,193.0384674072266,193.0384674072266,193.2947998046875,193.2947998046875,193.5878677368164,193.5878677368164,193.5878677368164,193.8960037231445,193.8960037231445,194.2325668334961,194.2325668334961,194.5849685668945,194.965576171875,195.3379287719727,195.3379287719727,195.7266082763672,195.7266082763672,196.1294555664062,196.1294555664062,196.5007705688477,196.5007705688477,196.5007705688477,196.5007705688477,196.5007705688477,196.5007705688477,193.0588150024414,193.0588150024414,193.0588150024414,193.2937545776367,193.2937545776367,193.5608444213867,193.5608444213867,193.8573837280273,193.8573837280273,194.1807403564453,194.5236663818359,194.8877792358398,195.2726135253906,195.2726135253906,195.6532211303711,195.6532211303711,196.0475006103516,196.0475006103516,196.4394149780273,196.6027603149414,196.6027603149414,196.6027603149414,196.6027603149414,196.6027603149414,196.6027603149414,193.329475402832,193.329475402832,193.5939559936523,193.5939559936523,193.877555847168,194.1883239746094,194.1883239746094,194.5304489135742,194.5304489135742,194.8676986694336,195.2288970947266,195.6082077026367,195.6082077026367,195.9893798828125,195.9893798828125,195.9893798828125,196.3505096435547,196.3505096435547,196.3505096435547,196.7031784057617,196.7031784057617,196.7031784057617,196.7031784057617,196.7031784057617,196.7031784057617,193.3451614379883,193.3451614379883,193.5787200927734,193.5787200927734,193.8468475341797,193.8468475341797,194.116081237793,194.4282531738281,194.7700119018555,195.0914840698242,195.440299987793,195.7988967895508,196.1322326660156,196.1322326660156,196.4650039672852,196.8018646240234,196.8018646240234,196.8018646240234,196.8018646240234,196.8018646240234,196.8018646240234,196.8018646240234,196.8018646240234,196.8018646240234,193.6213302612305,193.859733581543,194.1047897338867,194.4202499389648,194.4202499389648,194.7429046630859,195.0789108276367,195.4374389648438,195.8117294311523,196.2040939331055,196.2040939331055,196.5986175537109,196.5986175537109,196.8990478515625,196.8990478515625,196.8990478515625,196.8990478515625,196.8990478515625,196.8990478515625,196.8990478515625,196.8990478515625,196.8990478515625,196.8990478515625,196.8990478515625,196.8990478515625,196.8990478515625,196.8990478515625,196.8990478515625,196.8990478515625,196.8990478515625,196.8990478515625,196.8990478515625,196.8990478515625,196.8990478515625,196.8990478515625,196.8990478515625,196.8990478515625,196.8990478515625,196.8990478515625,193.5548477172852,193.5548477172852,193.5988922119141,193.5988922119141,193.7787322998047,193.7787322998047,194.0007019042969,194.0007019042969,194.2384338378906,194.5027694702148,194.7740020751953,194.7740020751953,195.0898666381836,195.0898666381836,195.0898666381836,195.4183349609375,195.7528610229492,196.1276092529297,196.1276092529297,196.5323104858398,196.5323104858398,196.9323425292969,196.9323425292969,196.9945297241211,196.9945297241211,193.7714233398438,193.7714233398438,194.0112380981445,194.2584991455078,194.2584991455078,194.5411987304688,194.5411987304688,194.5411987304688,194.8599090576172,195.2039489746094,195.2039489746094,195.5529708862305,195.5529708862305,195.9180145263672,195.9180145263672,196.3044281005859,196.3044281005859,196.6966400146484,197.0886077880859,197.0886077880859,197.0886077880859,197.0886077880859,197.0886077880859,197.0886077880859,193.9437103271484,193.9437103271484,194.1807632446289,194.1807632446289,194.4446792602539,194.4446792602539,194.767204284668,195.0876617431641,195.0876617431641,195.4313812255859,195.4313812255859,195.7837371826172,196.1478500366211,196.5227432250977,196.912467956543,197.1811828613281,197.1811828613281,197.1811828613281,197.1811828613281,194.1372375488281,194.1372375488281,194.3748168945312,194.6382064819336,194.9332504272461,195.2614517211914,195.6101684570312,195.9689178466797,196.341796875,196.7283248901367,196.7283248901367,196.7283248901367,197.127197265625,197.127197265625,197.2722778320312,197.2722778320312,197.2722778320312,197.2722778320312,194.3488540649414,194.3488540649414,194.5923461914062,194.8660354614258,194.8660354614258,195.1720352172852,195.1720352172852,195.5049438476562,195.8525695800781,196.2110137939453,196.2110137939453,196.2110137939453,196.5874252319336,196.5874252319336,196.5874252319336,196.9836807250977,196.9836807250977,197.3618392944336,197.3618392944336,197.3618392944336,197.3618392944336,194.4040908813477,194.6415863037109,194.6415863037109,194.6415863037109,194.9058532714844,194.9058532714844,194.9058532714844,195.2009963989258,195.2009963989258,195.5310668945312,195.5310668945312,195.879150390625,196.2413787841797,196.2413787841797,196.6162109375,196.6162109375,197.0091018676758,197.0091018676758,197.4140853881836,197.4500732421875,197.4500732421875,197.4500732421875,194.4800491333008,194.4800491333008,194.7126998901367,194.9680480957031,194.9680480957031,195.25537109375,195.5767211914062,195.9272613525391,195.9272613525391,196.2807846069336,196.650390625,196.650390625,197.0399169921875,197.0399169921875,197.4425659179688,197.5367889404297,197.5367889404297,194.5796890258789,194.5796890258789,194.5796890258789,194.8083343505859,194.8083343505859,195.0590667724609,195.0590667724609,195.3437423706055,195.3437423706055,195.6603164672852,196.0086288452148,196.0086288452148,196.3981781005859,196.3981781005859,196.7699966430664,196.7699966430664,196.7699966430664,197.15625,197.5603790283203,197.6221084594727,197.6221084594727,197.6221084594727,197.6221084594727,194.7091751098633,194.9161682128906,194.9161682128906,195.1476440429688,195.1476440429688,195.4254302978516,195.4254302978516,195.7375869750977,195.7375869750977,196.0464096069336,196.0464096069336,196.3940734863281,196.3940734863281,196.7562103271484,196.7562103271484,197.0862808227539,197.0862808227539,197.442497253418,197.442497253418,197.7060852050781,197.7060852050781,197.7060852050781,197.7060852050781,197.7060852050781,197.7060852050781,197.7060852050781,197.7060852050781,194.9172439575195,194.9172439575195,195.1439666748047,195.3973236083984,195.3973236083984,195.6645355224609,195.6645355224609,195.9792175292969,195.9792175292969,196.3204650878906,196.6532135009766,196.6532135009766,197.0146636962891,197.0146636962891,197.3947296142578,197.788688659668,197.788688659668,197.788688659668,197.788688659668,197.788688659668,197.788688659668,195.0117797851562,195.2400665283203,195.2400665283203,195.4657135009766,195.4657135009766,195.7394638061523,195.7394638061523,196.0486145019531,196.0486145019531,196.3572540283203,196.3572540283203,196.702995300293,196.702995300293,197.0557174682617,197.4013366699219,197.7680816650391,197.7680816650391,197.8699035644531,197.8699035644531,197.8699035644531,195.0764465332031,195.0764465332031,195.2816848754883,195.2816848754883,195.5147323608398,195.5147323608398,195.779052734375,196.0559234619141,196.0559234619141,196.3815689086914,196.7262802124023,197.0624618530273,197.0624618530273,197.4191741943359,197.4191741943359,197.7966232299805,197.7966232299805,197.9498596191406,197.9498596191406,197.9498596191406,197.9498596191406,197.9498596191406,197.9498596191406,195.3531188964844,195.3531188964844,195.3531188964844,195.5822830200195,195.5822830200195,195.832389831543,196.1171875,196.4380798339844,196.4380798339844,196.7827224731445,196.7827224731445,197.1335220336914,197.1335220336914,197.4985046386719,197.4985046386719,197.8810729980469,197.8810729980469,198.0285491943359,198.0285491943359,198.0285491943359,198.0285491943359,195.5244216918945,195.5244216918945,195.7576141357422,195.7576141357422,196.0216598510742,196.0216598510742,196.3201446533203,196.3201446533203,196.6512832641602,196.6512832641602,196.998779296875,197.3525009155273,197.3525009155273,197.3525009155273,197.7205123901367,198.1059188842773,198.1059188842773,198.1059188842773,198.1059188842773,195.5110778808594,195.739387512207,195.739387512207,195.9845123291016,195.9845123291016,196.2628173828125,196.2628173828125,196.5677947998047,196.5677947998047,196.9423294067383,197.29345703125,197.6571502685547,197.6571502685547,198.0374221801758,198.0374221801758,198.1820755004883,198.1820755004883,198.1820755004883,198.1820755004883,195.7626190185547,195.9961090087891,195.9961090087891,196.2565155029297,196.2565155029297,196.5521621704102,196.8814163208008,196.8814163208008,197.2323379516602,197.2323379516602,197.5910339355469,197.5910339355469,197.9688873291016,198.2570724487305,198.2570724487305,198.2570724487305,198.2570724487305,195.7920227050781,195.7920227050781,195.7920227050781,196.0210342407227,196.0210342407227,196.273567199707,196.5609512329102,196.5609512329102,196.8835144042969,197.2321929931641,197.5857391357422,197.5857391357422,197.9545974731445,197.9545974731445,198.3307876586914,198.3307876586914,198.3307876586914,198.3307876586914,198.3307876586914,198.3307876586914,195.853271484375,195.853271484375,195.853271484375,196.076545715332,196.3423004150391,196.3423004150391,196.6197509765625,196.6197509765625,196.6197509765625,196.9316101074219,196.9316101074219,197.2748031616211,197.2748031616211,197.2748031616211,197.6265029907227,197.6265029907227,197.9935836791992,197.9935836791992,198.3780670166016,198.4032897949219,198.4032897949219,198.4032897949219,195.9536285400391,196.1787338256836,196.1787338256836,196.4196548461914,196.4196548461914,196.6951446533203,196.6951446533203,197.0056304931641,197.3423461914062,197.6906204223633,197.6906204223633,198.0533065795898,198.0533065795898,198.4327087402344,198.4327087402344,198.4746475219727,198.4746475219727,198.4746475219727,196.0584335327148,196.0584335327148,196.2813491821289,196.5172348022461,196.5172348022461,196.7785339355469,196.7785339355469,197.0784454345703,197.0784454345703,197.4100112915039,197.7571487426758,197.7571487426758,198.1116104125977,198.1116104125977,198.4861679077148,198.5448608398438,198.5448608398438,198.5448608398438,196.1686401367188,196.3908996582031,196.6283874511719,196.8999786376953,196.8999786376953,196.8999786376953,197.204948425293,197.204948425293,197.5410003662109,197.5410003662109,197.8896789550781,197.8896789550781,197.8896789550781,198.250244140625,198.250244140625,198.6138534545898,198.6138534545898,198.6138534545898,198.6138534545898,198.6138534545898,198.6138534545898,198.6138534545898,198.6138534545898,198.6138534545898,198.6138534545898,198.6138534545898,198.6138534545898,198.6138534545898,198.6138534545898,198.6138534545898,198.6138534545898,198.6138534545898,198.6138534545898,198.6138534545898,198.6138534545898,198.6138534545898,198.6138534545898,198.6138534545898,198.6138534545898,198.6138534545898,198.6138534545898,198.6138534545898,198.6138534545898,198.6138534545898,198.6138534545898,198.6138534545898,198.6138534545898,198.6138534545898,196.3364105224609,196.5213623046875,196.5213623046875,196.7378463745117,196.7378463745117,196.9753189086914,196.9753189086914,197.2167663574219,197.2167663574219,197.4941329956055,197.4941329956055,197.8409118652344,197.8409118652344,197.8409118652344,198.1698913574219,198.5098648071289,198.6814422607422,198.6814422607422,198.6814422607422,198.6814422607422,198.6814422607422,198.6814422607422,198.6814422607422,198.6814422607422,196.4817962646484,196.7101516723633,196.7101516723633,196.9577331542969,197.2419052124023,197.5608596801758,197.5608596801758,197.9045715332031,198.2563247680664,198.6234283447266,198.7483062744141,198.7483062744141,198.7483062744141,198.7483062744141,198.7483062744141,198.7483062744141,196.6495208740234,196.8843078613281,197.15087890625,197.15087890625,197.4488143920898,197.7797622680664,197.7797622680664,198.1279525756836,198.1279525756836,198.47802734375,198.47802734375,198.8140563964844,198.8140563964844,198.8140563964844,198.8140563964844,198.8140563964844,198.8140563964844,196.5912704467773,196.5912704467773,196.8359909057617,196.8359909057617,197.0738296508789,197.0738296508789,197.3451385498047,197.65283203125,197.65283203125,197.9923934936523,197.9923934936523,198.3445663452148,198.3445663452148,198.7097549438477,198.7097549438477,198.878776550293,198.878776550293,198.878776550293,198.878776550293,196.7998580932617,197.0295104980469,197.0295104980469,197.2795791625977,197.2795791625977,197.5712203979492,197.5712203979492,197.8982238769531,198.2457885742188,198.6068649291992,198.6068649291992,198.6068649291992,198.9425277709961,198.9425277709961,198.9425277709961,198.9425277709961,196.8159027099609,196.8159027099609,197.0369644165039,197.0369644165039,197.2775268554688,197.2775268554688,197.5500564575195,197.5500564575195,197.8583068847656,198.1980972290039,198.1980972290039,198.5506286621094,198.5506286621094,198.5506286621094,198.9161605834961,198.9161605834961,199.0051040649414,199.0051040649414,199.0051040649414,199.0051040649414,199.0051040649414,199.0051040649414,197.0381546020508,197.0381546020508,197.2733306884766,197.2733306884766,197.5352554321289,197.835334777832,197.835334777832,198.169075012207,198.5174179077148,198.5174179077148,198.5174179077148,198.8794708251953,199.0668258666992,199.0668258666992,199.0668258666992,199.0668258666992,199.0668258666992,199.0668258666992,197.0784606933594,197.0784606933594,197.3072814941406,197.3072814941406,197.5559539794922,197.5559539794922,197.8400268554688,197.8400268554688,198.1584091186523,198.5035018920898,198.8616714477539,198.8616714477539,198.8616714477539,199.1273956298828,199.1273956298828,199.1273956298828,199.1273956298828,197.1193771362305,197.3371429443359,197.5836868286133,197.5836868286133,197.8672561645508,197.8672561645508,198.1848831176758,198.1848831176758,198.5321350097656,198.8858947753906,199.1871032714844,199.1871032714844,199.1871032714844,199.1871032714844,197.2086715698242,197.4294891357422,197.6784896850586,197.9667434692383,197.9667434692383,198.2905426025391,198.2905426025391,198.6420288085938,199.0016860961914,199.0016860961914,199.2458038330078,199.2458038330078,199.2458038330078,199.2458038330078,199.2458038330078,199.2458038330078,199.2458038330078,199.2458038330078,197.3263092041016,197.553825378418,197.553825378418,197.8012466430664,198.0862350463867,198.0862350463867,198.4063034057617,198.4063034057617,198.7551345825195,198.7551345825195,199.1113510131836,199.1113510131836,199.3035278320312,199.3035278320312,199.3035278320312,199.3035278320312,199.3035278320312,199.3035278320312,197.4468841552734,197.6741256713867,197.6741256713867,197.9250564575195,198.2152938842773,198.5407485961914,198.5407485961914,198.8902816772461,198.8902816772461,199.2483215332031,199.3603820800781,199.3603820800781,199.3603820800781,199.3603820800781,197.6005630493164,197.6005630493164,197.833381652832,197.833381652832,198.0945587158203,198.3942031860352,198.7304840087891,199.0854721069336,199.4162063598633,199.4162063598633,199.4162063598633,199.4162063598633,199.4162063598633,199.4162063598633,199.4162063598633,199.4162063598633,199.4162063598633,199.4162063598633,199.4162063598633,199.4162063598633,197.6724395751953,197.6724395751953,197.9017791748047,197.9017791748047,198.1607284545898,198.1607284545898,198.456298828125,198.7867279052734,199.1330795288086,199.1330795288086,199.4712371826172,199.4712371826172,199.4712371826172,199.4712371826172,199.4712371826172,199.4712371826172,197.6128692626953,197.8223571777344,197.8223571777344,198.0653533935547,198.0653533935547,198.3452529907227,198.3452529907227,198.6977691650391,198.6977691650391,199.0494384765625,199.0494384765625,199.4079437255859,199.4079437255859,199.4079437255859,199.5253372192383,199.5253372192383,199.5253372192383,199.5253372192383,199.5253372192383,199.5253372192383,199.5253372192383,199.5253372192383,199.5253372192383,199.5253372192383,199.5253372192383,199.5253372192383,199.5253372192383,199.5253372192383,199.5253372192383,199.5253372192383,199.5253372192383,199.5253372192383,197.6627960205078,197.6627960205078,197.6627960205078,197.8510589599609,197.8510589599609,198.0759124755859,198.302734375,198.5805130004883,198.5805130004883,198.8933868408203,198.8933868408203,199.2317733764648,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,199.5785064697266,197.7460861206055,197.7460861206055,197.7460861206055,197.7460861206055,197.7460861206055,197.7460861206055,197.98193359375,198.2361297607422,198.2361297607422,198.5150375366211,198.8319396972656,199.1609420776367,199.1609420776367,199.4751815795898,199.4751815795898,199.8321533203125,200.220085144043,200.220085144043,200.6278686523438,201.0040893554688,201.3401489257812,201.3401489257812,201.3401489257812,201.6751251220703,201.6751251220703,202.0438537597656,202.3786087036133,202.3786087036133,202.7120666503906,203.0471572875977,203.3829193115234,203.7184295654297,204.050048828125,204.050048828125,204.3836212158203,204.3836212158203,204.3836212158203,204.7162857055664,204.7162857055664,205.0494079589844,205.382568359375,205.3924026489258,205.3924026489258,205.3924026489258,205.3924026489258,205.3924026489258,205.3924026489258,198.2692413330078,198.2692413330078,198.533332824707,198.8302001953125,198.8302001953125,198.8302001953125,199.1592025756836,199.1592025756836,199.4834823608398,199.4834823608398,199.8130798339844,200.1790771484375,200.1790771484375,200.1790771484375,200.5626602172852,200.5626602172852,200.9544830322266,200.9544830322266,201.3530120849609,201.3530120849609,201.7495651245117,201.7495651245117,202.1550903320312,202.1550903320312,202.5632553100586,202.5632553100586,202.9709091186523,202.9709091186523,203.3776321411133,203.3776321411133,203.7893905639648,204.2033081054688,204.2033081054688,204.6181030273438,204.6181030273438,205.0321960449219,205.0321960449219,205.4289703369141,205.4289703369141,205.6014633178711,205.6014633178711,205.6014633178711,205.6014633178711,205.6014633178711,205.6014633178711,198.487174987793,198.487174987793,198.7440948486328,198.7440948486328,198.7440948486328,199.0259552001953,199.3356704711914,199.3356704711914,199.6544418334961,199.6544418334961,199.980842590332,199.980842590332,200.3486251831055,200.7254409790039,201.1200866699219,201.5257415771484,201.5257415771484,201.5257415771484,201.9410705566406,202.3563079833984,202.3563079833984,202.7718276977539,202.7718276977539,203.1857223510742,203.1857223510742,203.6000595092773,203.6000595092773,203.6000595092773,204.0140380859375,204.4281463623047,204.4281463623047,204.8239669799805,205.2393188476562,205.2393188476562,205.6361083984375,205.6361083984375,205.6361083984375,205.8072357177734,205.8072357177734,205.8072357177734,205.8072357177734,198.7789459228516,198.7789459228516,199.0333862304688,199.0333862304688,199.3058395385742,199.6084365844727,199.6084365844727,199.9174728393555,199.9174728393555,200.2490844726562,200.2490844726562,200.6159591674805,200.9901580810547,200.9901580810547,201.3810653686523,201.3810653686523,201.7848358154297,201.7848358154297,202.1933746337891,202.1933746337891,202.1933746337891,202.6466674804688,203.0597457885742,203.4740600585938,203.8877410888672,203.8877410888672,204.3001098632812,204.3001098632812,204.711296081543,204.711296081543,205.1230087280273,205.530403137207,205.530403137207,205.9225616455078,206.0096664428711,206.0096664428711,206.0096664428711,206.0096664428711,199.1296081542969,199.1296081542969,199.3803634643555,199.6462249755859,199.6462249755859,199.9328308105469,200.2258605957031,200.2258605957031,200.5681610107422,200.5681610107422,200.9321365356445,200.9321365356445,200.9321365356445,201.305778503418,201.6940307617188,201.6940307617188,202.0776062011719,202.4798355102539,202.4798355102539,202.8876266479492,202.8876266479492,203.2989883422852,203.2989883422852,203.7093734741211,203.7093734741211,204.1203460693359,204.1203460693359,204.5323791503906,204.5323791503906,204.9453048706055,204.9453048706055,205.3590240478516,205.3590240478516,205.7670822143555,206.1632919311523,206.208854675293,206.208854675293,206.208854675293,206.208854675293,206.208854675293,206.208854675293,199.4895248413086,199.4895248413086,199.4895248413086,199.7410049438477,199.7410049438477,200.0082244873047,200.0082244873047,200.289909362793,200.289909362793,200.5960922241211,200.5960922241211,200.9421157836914,200.9421157836914,201.3044509887695,201.3044509887695,201.6669998168945,201.6669998168945,202.0497131347656,202.0497131347656,202.4445343017578,202.4445343017578,202.8432235717773,202.8432235717773,203.2424240112305,203.2424240112305,203.646484375,204.0520553588867,204.0520553588867,204.4242630004883,204.4242630004883,204.7964248657227,204.7964248657227,205.1858444213867,205.1858444213867,205.5457077026367,205.8773574829102,205.8773574829102,206.2244491577148,206.4047393798828,206.4047393798828,206.4047393798828,206.4047393798828,206.4047393798828,206.4047393798828,199.8672256469727,199.8672256469727,200.038215637207,200.2790832519531,200.2790832519531,200.5259094238281,200.5259094238281,200.745849609375,201.0425109863281,201.0425109863281,201.3744049072266,201.7002182006836,201.7002182006836,201.7002182006836,202.013069152832,202.013069152832,202.360725402832,202.360725402832,202.7120590209961,202.7120590209961,203.0656204223633,203.0656204223633,203.4246139526367,203.4246139526367,203.8056259155273,204.1477966308594,204.1477966308594,204.5212173461914,204.9110870361328,204.9110870361328,204.9110870361328,205.2772750854492,205.6517562866211,205.6517562866211,206.0384902954102,206.4076919555664,206.5975723266602,206.5975723266602,206.5975723266602,206.5975723266602,206.5975723266602,206.5975723266602,206.5975723266602,206.5975723266602,206.5975723266602,206.5975723266602,206.5975723266602,206.5975723266602,206.5975723266602,206.5975723266602,206.5975723266602,206.5975723266602,206.5975723266602,206.5975723266602,206.5975723266602,206.5975723266602,206.5975723266602,206.5975723266602,206.5975723266602,206.5975723266602,199.9635467529297,199.9635467529297,199.9635467529297,199.9635467529297,199.9635467529297,199.9635467529297,200.0206298828125,200.2597351074219,200.2597351074219,200.5276870727539,200.5276870727539,200.7558059692383,200.7558059692383,201.0310211181641,201.3494644165039,201.3494644165039,201.6523818969727,201.9852676391602,202.3351593017578,202.7055816650391,202.7055816650391,203.0945510864258,203.0945510864258,203.4955139160156,203.9010620117188,203.9010620117188,203.9010620117188,204.3029022216797,204.3029022216797,204.3029022216797,204.7077713012695,204.7077713012695,205.1087188720703,205.1087188720703,205.5091094970703,205.5091094970703,205.9093856811523,205.9093856811523,205.9093856811523,206.3144378662109,206.7109527587891,206.7109527587891,206.787223815918,206.787223815918,206.787223815918,206.787223815918,200.3263854980469,200.5518035888672,200.5518035888672,200.7969436645508,200.7969436645508,201.0515823364258,201.0515823364258,201.3234405517578,201.6536331176758,201.6536331176758,201.9850921630859,202.2874374389648,202.6120910644531,202.6120910644531,202.6120910644531,202.9681625366211,202.9681625366211,203.333869934082,203.6504287719727,204.0227584838867,204.0227584838867,204.4086074829102,204.4086074829102,204.7274551391602,204.7274551391602,204.7274551391602,205.1076889038086,205.1076889038086,205.5004730224609,205.8417663574219,205.8417663574219,206.219596862793,206.6134719848633,206.6134719848633,206.6134719848633,206.973876953125,206.973876953125,206.973876953125,206.973876953125,206.973876953125,206.973876953125,206.973876953125,206.973876953125,206.973876953125,200.6222991943359,200.8286972045898,200.8286972045898,200.8286972045898,201.0684280395508,201.3176651000977,201.6025466918945,201.6025466918945,201.9189453125,201.9189453125,202.2553100585938,202.2553100585938,202.5841903686523,202.947883605957,203.3137512207031,203.3137512207031,203.6950912475586,203.6950912475586,203.6950912475586,204.0383529663086,204.0383529663086,204.4205551147461,212.2431564331055,212.2431564331055,212.2431564331055,212.2431564331055,212.2431564331055,212.2431564331055,212.2431564331055,212.2431564331055,212.2431564331055,212.2431564331055,212.2431564331055,212.2431564331055,212.2431564331055,212.2431564331055,212.2431564331055,212.2431564331055,212.2431564331055,212.2431564331055,212.2431564331055,212.2431564331055,219.8725509643555,219.87255859375,219.87255859375,219.87255859375,219.87255859375,219.87255859375,219.87255859375,219.87255859375,219.87255859375,219.87255859375,219.87255859375,219.87255859375,219.87255859375,219.87255859375,219.87255859375,219.87255859375,219.87255859375,219.87255859375,219.87255859375,219.87255859375,219.87255859375,219.87255859375,219.87255859375,235.13134765625,235.13134765625,235.13134765625,235.13134765625,235.13134765625,235.13134765625,235.13134765625,235.13134765625,235.13134765625,235.13134765625,235.13134765625,235.13134765625,235.13134765625,235.13134765625,235.13134765625,235.13134765625,235.13134765625,235.13134765625,242.803337097168,242.803337097168,242.803337097168,242.803337097168,242.803337097168,242.803337097168,242.803337097168,242.803337097168,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078,258.1559600830078],"meminc":[0,0,0,0,2.288818359375e-05,0,15.28221130371094,0,0,0.0003662109375,0,0,30.46537780761719,0,0,0,0,0,4.57763671875e-05,0,0,0,0,0,0,0,0,0,0,0,0,0,-0.00030517578125,0,15.2587890625,0.2254180908203125,0.2550735473632812,0.2786941528320312,0,0,0.314453125,0,0.3444366455078125,0,0.353759765625,0,0.3805923461914062,0,0.4064178466796875,0,0.4503250122070312,0.24725341796875,0,-2.888389587402344,0,0.3681106567382812,0,0.3508453369140625,0,0.3656387329101562,0,0.3651885986328125,0,0.3816604614257812,0,0,0.3729171752929688,0.3112945556640625,0,0.3489532470703125,0,0.09354400634765625,0,0,-2.7459716796875,0.3644485473632812,0,0.3890533447265625,0.3949203491210938,0.3815536499023438,0.395172119140625,0.395660400390625,0,0.3753280639648438,0,0.136749267578125,0,-2.762359619140625,0,0.345672607421875,0,0,0.3709335327148438,0,0.3848495483398438,0,0,0.3885421752929688,0.3744735717773438,0.3840408325195312,0,0.3837814331054688,0,0.2157058715820312,0,0,-2.760337829589844,0,0.3444137573242188,0,0.3690414428710938,0,0.3809356689453125,0,0.3883285522460938,0,0.387298583984375,0,0,0.3860244750976562,0,0.3983535766601562,0,0.190185546875,0,0,-2.674140930175781,0.3851165771484375,0,0.3687820434570312,0.3805313110351562,0,0.391265869140625,0,0.3887557983398438,0.3944168090820312,0,0,0.3996658325195312,-2.797706604003906,0,0.3339080810546875,0.3543548583984375,0.3626708984375,0,0.3816680908203125,0,0,0.3872833251953125,0,0.3876571655273438,0.3938827514648438,0,0.32623291015625,0,0,-2.713188171386719,0,0.3271484375,0.3591995239257812,0.3623275756835938,0,0.3783493041992188,0.3837661743164062,0.3831253051757812,0.3943405151367188,0,0.2051467895507812,0,0,-2.576393127441406,0.3395538330078125,0.36102294921875,0.3631134033203125,0,0.3667221069335938,0.3754119873046875,0.3858489990234375,0,0.3872299194335938,0,0.07635498046875,0,0,-2.437957763671875,0,0.3502349853515625,0,0.3580093383789062,0,0,0.3665313720703125,0,0.3740158081054688,0.3796539306640625,0.3846817016601562,0,0.3024978637695312,0,0,-2.544136047363281,0,0.33343505859375,0.3531646728515625,0.356414794921875,0,0,0.3697738647460938,0.3760147094726562,0,0.3804092407226562,0,0.3882064819335938,0.06307220458984375,0,-2.352485656738281,0,0.339752197265625,0,0.3535308837890625,0,0.3650054931640625,0,0.3756790161132812,0,0.382080078125,0,0.3855209350585938,0,0.2261199951171875,0,-2.431793212890625,0.3293304443359375,0,0.3502120971679688,0,0.3621978759765625,0,0.3769073486328125,0.3830795288085938,0,0.3934783935546875,0.3105316162109375,0,0,-2.461196899414062,0.3188552856445312,0,0.3432540893554688,0,0.358001708984375,0.3740463256835938,0,0.3795547485351562,0,0.39166259765625,0.3685684204101562,0,-2.464096069335938,0,0.3118667602539062,0,0.3365707397460938,0,0.3521728515625,0,0.3687057495117188,0.3825149536132812,0,0.4353561401367188,0.3484954833984375,0,-2.416755676269531,0.3107681274414062,0,0.3289871215820312,0.3522796630859375,0.3677291870117188,0.382537841796875,0,0.39471435546875,0,0.3501815795898438,0,-2.383621215820312,0,0.3017120361328125,0.3189468383789062,0,0.3374404907226562,0,0.3551864624023438,0,0.3687210083007812,0.381439208984375,0,0.3893814086914062,0,0,-2.375106811523438,0,0.2981109619140625,0,0.3149795532226562,0,0.3430557250976562,0,0.3611373901367188,0,0.3776168823242188,0,0.3802642822265625,0,0,0.3681411743164062,0,0,-2.339263916015625,0,0.2896728515625,0,0.3076095581054688,0.3358612060546875,0,0.3559417724609375,0.3707733154296875,0.3800430297851562,0,0,0.3663864135742188,0,0,-2.282791137695312,0,0.2867660522460938,0,0.3082962036132812,0,0.3722305297851562,0.3580780029296875,0.3750152587890625,0,0.3872756958007812,0,0.2611007690429688,0,0,-2.169525146484375,0,0.2934341430664062,0,0.3149642944335938,0,0,0.3476181030273438,0,0.3666152954101562,0.379150390625,0,0.3739395141601562,0,0.1586761474609375,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2.180809020996094,0.2112045288085938,0.2297286987304688,0,0.2503738403320312,0.2847976684570312,0.3178482055664062,0,0.3345947265625,0,0.351470947265625,0,0.2644424438476562,0,0,-2.119888305664062,0,0.3048248291015625,0,0.3036880493164062,0,0.3393707275390625,0.360443115234375,0,0.3762741088867188,0.3855209350585938,0.1126022338867188,0,0,-1.981910705566406,0,0.2843017578125,0,0.32061767578125,0,0.3533554077148438,0,0.3719024658203125,0,0.3628158569335938,0.3507766723632812,0,-2.122947692871094,0,0.270233154296875,0,0.2877655029296875,0,0,0.3301162719726562,0,0.35284423828125,0,0,0.3662567138671875,0.37738037109375,0,0.1991806030273438,0,0,-1.982582092285156,0,0.2733993530273438,0,0.3123016357421875,0,0.3450546264648438,0.362884521484375,0.3676223754882812,0,0.3812484741210938,0,0,0,0,0,-1.807746887207031,0,0.2910995483398438,0,0.3281478881835938,0,0.3518829345703125,0.3694915771484375,0,0.41937255859375,0.1065826416015625,0,-1.856452941894531,0.27789306640625,0,0.3203125,0.348419189453125,0,0.364349365234375,0,0.3767623901367188,0.2266998291015625,0,0,-1.9095458984375,0,0.2699432373046875,0.3059616088867188,0,0.3415908813476562,0.3608474731445312,0.3721389770507812,0,0,0.3160552978515625,0,0,-1.93084716796875,0,0.2678146362304688,0.3007659912109375,0.3403549194335938,0,0.3586273193359375,0.3733291625976562,0,0.3460311889648438,0,0,0,-1.925575256347656,0.2624359130859375,0.2913284301757812,0,0,0.3318557739257812,0,0.351654052734375,0.3656387329101562,0,0.3778152465820312,0,0,0,0,0,0,0,-1.657188415527344,0,0.2913360595703125,0,0.3312759399414062,0,0.3549880981445312,0,0,0.4070968627929688,0,0.326751708984375,0,0,0,-1.850021362304688,0,0.2621002197265625,0.2948837280273438,0,0.333770751953125,0,0.351654052734375,0,0.3610916137695312,0,0.299896240234375,0,0,-1.832199096679688,0.25384521484375,0,0.2907638549804688,0,0.3300704956054688,0,0.3513031005859375,0,0.365936279296875,0.292816162109375,0,0,-1.780967712402344,0.2608871459960938,0.2946853637695312,0,0.33551025390625,0,0.3552169799804688,0.3676223754882812,0.21875,0,-1.70172119140625,0,0,0.2674713134765625,0.3033294677734375,0,0.3400726318359375,0.3573379516601562,0.3697280883789062,0.1145706176757812,0,0,-1.609260559082031,0,0.2709732055664062,0,0.3105316162109375,0,0.3766250610351562,0,0.3585052490234375,0,0.3427047729492188,0,0,0,0,0,-1.481719970703125,0.2874984741210938,0,0.32989501953125,0,0.3526382446289062,0,0.3692169189453125,0,0.1916732788085938,0,-1.605209350585938,0,0.26397705078125,0,0.303863525390625,0.3397216796875,0,0.358917236328125,0.3736953735351562,0,0.01351165771484375,0,0,-1.460601806640625,0.2827682495117188,0.3302078247070312,0,0.3539581298828125,0,0.3680877685546875,0.1731948852539062,0,0,-1.5439453125,0.2715911865234375,0,0.3151321411132812,0,0.3434066772460938,0,0.3571319580078125,0,0,0.3035507202148438,0,0,-1.606651306152344,0.2515106201171875,0,0.291412353515625,0,0.3325271606445312,0.3913345336914062,0,0.3606185913085938,0,0,0.025421142578125,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.588134765625,0,0,0.07175445556640625,0,0.2539138793945312,0.27288818359375,0,0,0.30718994140625,0.3282470703125,0,0.318817138671875,0,0,0.3688812255859375,0.39984130859375,0,0.403839111328125,0.34954833984375,0.3349380493164062,0,0,0.3351593017578125,0,0,0.3349761962890625,0,0.333740234375,0,0.3332977294921875,0.0923004150390625,0,-4.489814758300781,0,0,0.321624755859375,0.351654052734375,0,0.3423538208007812,0,0.3439559936523438,0,0.3923568725585938,0,0.4102859497070312,0,0,0.4073104858398438,0.4077377319335938,0.40594482421875,0.40570068359375,0,0.4091796875,0,0.3916244506835938,0.03247833251953125,0,0,-4.342720031738281,0.3257904052734375,0,0.3425979614257812,0.3224563598632812,0.35906982421875,0,0.38494873046875,0,0.40032958984375,0,0.3994903564453125,0.4094085693359375,0,0.4076766967773438,0.4077377319335938,0,0.4069671630859375,0,0.3064651489257812,0,0,0,-4.215621948242188,0.3228302001953125,0,0,0.3335800170898438,0,0.3302841186523438,0,0.3730010986328125,0.3920745849609375,0,0.4007949829101562,0.4053268432617188,0,0.4081802368164062,0.4073867797851562,0,0.4034347534179688,0,0.3995437622070312,0,0.1672897338867188,0,0,-4.345359802246094,0,0,0.2940750122070312,0,0.322235107421875,0,0.3138885498046875,0,0,0.351104736328125,0,0.3787307739257812,0,0.3990478515625,0.4081573486328125,0.4109573364257812,0,0.4102020263671875,0.4092330932617188,0,0,0.4513015747070312,0,0.322540283203125,0,0,0,0,0,-4.108192443847656,0,0,0.3088302612304688,0,0.3128890991210938,0,0.3404617309570312,0,0.3724822998046875,0,0.3943557739257812,0.4053421020507812,0.4055023193359375,0,0.4091796875,0,0.4103012084960938,0,0.4110031127929688,0.399993896484375,0.06182861328125,0,0,-4.138832092285156,0.2933349609375,0,0.3033828735351562,0,0.3264007568359375,0,0.3630599975585938,0,0.3836441040039062,0,0.400970458984375,0.3609161376953125,0,0.3688125610351562,0.39306640625,0.3834381103515625,0,0,0.391510009765625,0,0.292327880859375,0,0,0,0,0,0,0,-4.008369445800781,0,0,0.2830123901367188,0.2876739501953125,0.3337249755859375,0,0.3567047119140625,0.3816757202148438,0,0.396759033203125,0,0,0.3985137939453125,0,0.4029312133789062,0,0.40777587890625,0,0.40618896484375,0,0.3869247436523438,0.08652496337890625,0,0,-4.034049987792969,0.2550888061523438,0,0.300079345703125,0,0.3070526123046875,0,0.295166015625,0,0.325042724609375,0.3502426147460938,0.3070144653320312,0,0.3195724487304688,0,0.3446044921875,0,0.3532791137695312,0,0.3006134033203125,0.3831863403320312,0,0.3111724853515625,0,0,0,-4.00311279296875,0,0.258514404296875,0,0.2479476928710938,0,0.2767257690429688,0,0.3312835693359375,0,0.3242645263671875,0,0,0.3600692749023438,0,0,0.3557357788085938,0.3661575317382812,0,0.3299102783203125,0,0,0.3407974243164062,0,0.3762359619140625,0,0.3499069213867188,0.2017822265625,0,0,0,0,0,-3.793258666992188,0,0,0.2455368041992188,0.2752227783203125,0.3190460205078125,0.324981689453125,0.3555831909179688,0.3698501586914062,0,0.373291015625,0.322998046875,0,0.3513031005859375,0,0.3281936645507812,0,0.3325042724609375,0,0.3090362548828125,0,0,0,-3.88299560546875,0,0.2606201171875,0,0.243743896484375,0.2468948364257812,0.2956771850585938,0.3335342407226562,0,0.2567138671875,0,0.2860488891601562,0,0.33319091796875,0,0.29205322265625,0,0.2808761596679688,0.3348770141601562,0.351654052734375,0.2296524047851562,0,0.2499771118164062,0,0,0,-3.778884887695312,0.2381591796875,0,0.2544784545898438,0.3270111083984375,0.32989501953125,0,0.3513031005859375,0.368865966796875,0,0.3851547241210938,0.3965911865234375,0,0.400665283203125,0.4023208618164062,0,0,0.4005889892578125,0,0.03448486328125,0,-3.701751708984375,0,0.2516403198242188,0,0.2828216552734375,0.3146286010742188,0,0.34014892578125,0.3600234985351562,0,0.3464431762695312,0.3375396728515625,0,0.390228271484375,0.3960800170898438,0.3650360107421875,0,0.3777847290039062,0,0.0482940673828125,0,-3.662971496582031,0,0.253387451171875,0,0.27142333984375,0,0.3090591430664062,0,0.307891845703125,0.3529129028320312,0,0,0.3726806640625,0.360076904296875,0.3862228393554688,0.4025421142578125,0,0.3801498413085938,0.3735885620117188,0.0001678466796875,0,0,-3.573402404785156,0.2071304321289062,0.2477340698242188,0,0.2974700927734375,0.3012619018554688,0,0.3698654174804688,0.3618316650390625,0,0.37115478515625,0,0.3488922119140625,0.3765640258789062,0,0.3955078125,0,0.3544769287109375,0,0.04686737060546875,0,-3.572357177734375,0.2137680053710938,0,0.2563323974609375,0,0.2930679321289062,0,0,0.308135986328125,0,0.3365631103515625,0,0.3524017333984375,0.3806076049804688,0.3723526000976562,0,0.3886795043945312,0,0.4028472900390625,0,0.3713150024414062,0,0,0,0,0,-3.44195556640625,0,0,0.2349395751953125,0,0.26708984375,0,0.296539306640625,0,0.3233566284179688,0.342926025390625,0.3641128540039062,0.3848342895507812,0,0.3806076049804688,0,0.3942794799804688,0,0.3919143676757812,0.1633453369140625,0,0,0,0,0,-3.273284912109375,0,0.2644805908203125,0,0.283599853515625,0.3107681274414062,0,0.3421249389648438,0,0.337249755859375,0.3611984252929688,0.3793106079101562,0,0.3811721801757812,0,0,0.3611297607421875,0,0,0.3526687622070312,0,0,0,0,0,-3.358016967773438,0,0.2335586547851562,0,0.26812744140625,0,0.2692337036132812,0.3121719360351562,0.3417587280273438,0.32147216796875,0.34881591796875,0.3585968017578125,0.3333358764648438,0,0.3327713012695312,0.3368606567382812,0,0,0,0,0,0,0,0,-3.180534362792969,0.2384033203125,0.24505615234375,0.315460205078125,0,0.3226547241210938,0.3360061645507812,0.3585281372070312,0.3742904663085938,0.392364501953125,0,0.3945236206054688,0,0.3004302978515625,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-3.344200134277344,0,0.04404449462890625,0,0.179840087890625,0,0.2219696044921875,0,0.23773193359375,0.2643356323242188,0.2712326049804688,0,0.3158645629882812,0,0,0.3284683227539062,0.3345260620117188,0.3747482299804688,0,0.4047012329101562,0,0.4000320434570312,0,0.06218719482421875,0,-3.223106384277344,0,0.2398147583007812,0.2472610473632812,0,0.2826995849609375,0,0,0.3187103271484375,0.3440399169921875,0,0.3490219116210938,0,0.3650436401367188,0,0.38641357421875,0,0.3922119140625,0.3919677734375,0,0,0,0,0,-3.1448974609375,0,0.2370529174804688,0,0.263916015625,0,0.3225250244140625,0.3204574584960938,0,0.343719482421875,0,0.35235595703125,0.3641128540039062,0.3748931884765625,0.3897247314453125,0.2687149047851562,0,0,0,-3.0439453125,0,0.237579345703125,0.2633895874023438,0.2950439453125,0.3282012939453125,0.3487167358398438,0.3587493896484375,0.3728790283203125,0.3865280151367188,0,0,0.3988723754882812,0,0.14508056640625,0,0,0,-2.923423767089844,0,0.2434921264648438,0.2736892700195312,0,0.305999755859375,0,0.3329086303710938,0.347625732421875,0.3584442138671875,0,0,0.3764114379882812,0,0,0.3962554931640625,0,0.3781585693359375,0,0,0,-2.957748413085938,0.2374954223632812,0,0,0.2642669677734375,0,0,0.2951431274414062,0,0.3300704956054688,0,0.34808349609375,0.3622283935546875,0,0.3748321533203125,0,0.3928909301757812,0,0.4049835205078125,0.03598785400390625,0,0,-2.970024108886719,0,0.2326507568359375,0.2553482055664062,0,0.287322998046875,0.32135009765625,0.3505401611328125,0,0.3535232543945312,0.3696060180664062,0,0.3895263671875,0,0.40264892578125,0.0942230224609375,0,-2.957099914550781,0,0,0.2286453247070312,0,0.250732421875,0,0.2846755981445312,0,0.3165740966796875,0.3483123779296875,0,0.3895492553710938,0,0.3718185424804688,0,0,0.3862533569335938,0.4041290283203125,0.06172943115234375,0,0,0,-2.912933349609375,0.2069931030273438,0,0.231475830078125,0,0.2777862548828125,0,0.3121566772460938,0,0.3088226318359375,0,0.3476638793945312,0,0.3621368408203125,0,0.3300704956054688,0,0.3562164306640625,0,0.2635879516601562,0,0,0,0,0,0,0,-2.788841247558594,0,0.2267227172851562,0.25335693359375,0,0.2672119140625,0,0.3146820068359375,0,0.34124755859375,0.3327484130859375,0,0.3614501953125,0,0.38006591796875,0.3939590454101562,0,0,0,0,0,-2.776908874511719,0.2282867431640625,0,0.22564697265625,0,0.2737503051757812,0,0.3091506958007812,0,0.3086395263671875,0,0.3457412719726562,0,0.35272216796875,0.3456192016601562,0.3667449951171875,0,0.1018218994140625,0,0,-2.79345703125,0,0.2052383422851562,0,0.2330474853515625,0,0.2643203735351562,0.2768707275390625,0,0.3256454467773438,0.3447113037109375,0.336181640625,0,0.3567123413085938,0,0.3774490356445312,0,0.1532363891601562,0,0,0,0,0,-2.59674072265625,0,0,0.2291641235351562,0,0.2501068115234375,0.2847976684570312,0.320892333984375,0,0.3446426391601562,0,0.350799560546875,0,0.3649826049804688,0,0.382568359375,0,0.1474761962890625,0,0,0,-2.504127502441406,0,0.2331924438476562,0,0.2640457153320312,0,0.2984848022460938,0,0.3311386108398438,0,0.3474960327148438,0.3537216186523438,0,0,0.368011474609375,0.385406494140625,0,0,0,-2.594841003417969,0.2283096313476562,0,0.2451248168945312,0,0.2783050537109375,0,0.3049774169921875,0,0.3745346069335938,0.3511276245117188,0.3636932373046875,0,0.3802719116210938,0,0.1446533203125,0,0,0,-2.419456481933594,0.233489990234375,0,0.260406494140625,0,0.2956466674804688,0.329254150390625,0,0.350921630859375,0,0.3586959838867188,0,0.3778533935546875,0.2881851196289062,0,0,0,-2.465049743652344,0,0,0.2290115356445312,0,0.252532958984375,0.287384033203125,0,0.3225631713867188,0.3486785888671875,0.353546142578125,0,0.3688583374023438,0,0.376190185546875,0,0,0,0,0,-2.477516174316406,0,0,0.2232742309570312,0.2657546997070312,0,0.2774505615234375,0,0,0.311859130859375,0,0.3431930541992188,0,0,0.3516998291015625,0,0.3670806884765625,0,0.3844833374023438,0.0252227783203125,0,0,-2.449661254882812,0.2251052856445312,0,0.2409210205078125,0,0.2754898071289062,0,0.31048583984375,0.3367156982421875,0.3482742309570312,0,0.3626861572265625,0,0.3794021606445312,0,0.04193878173828125,0,0,-2.416213989257812,0,0.2229156494140625,0.2358856201171875,0,0.2612991333007812,0,0.2999114990234375,0,0.3315658569335938,0.347137451171875,0,0.354461669921875,0,0.3745574951171875,0.05869293212890625,0,0,-2.376220703125,0.222259521484375,0.23748779296875,0.2715911865234375,0,0,0.3049697875976562,0,0.3360519409179688,0,0.3486785888671875,0,0,0.360565185546875,0,0.3636093139648438,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2.277442932128906,0.1849517822265625,0,0.2164840698242188,0,0.2374725341796875,0,0.2414474487304688,0,0.2773666381835938,0,0.3467788696289062,0,0,0.3289794921875,0.3399734497070312,0.1715774536132812,0,0,0,0,0,0,0,-2.19964599609375,0.2283554077148438,0,0.2475814819335938,0.2841720581054688,0.3189544677734375,0,0.3437118530273438,0.3517532348632812,0.3671035766601562,0.1248779296875,0,0,0,0,0,-2.098785400390625,0.2347869873046875,0.266571044921875,0,0.2979354858398438,0.3309478759765625,0,0.3481903076171875,0,0.3500747680664062,0,0.336029052734375,0,0,0,0,0,-2.222785949707031,0,0.244720458984375,0,0.2378387451171875,0,0.2713088989257812,0.3076934814453125,0,0.3395614624023438,0,0.3521728515625,0,0.3651885986328125,0,0.1690216064453125,0,0,0,-2.07891845703125,0.2296524047851562,0,0.2500686645507812,0,0.2916412353515625,0,0.3270034790039062,0.347564697265625,0.3610763549804688,0,0,0.335662841796875,0,0,0,-2.126625061035156,0,0.2210617065429688,0,0.2405624389648438,0,0.2725296020507812,0,0.3082504272460938,0.3397903442382812,0,0.3525314331054688,0,0,0.3655319213867188,0,0.0889434814453125,0,0,0,0,0,-1.966949462890625,0,0.2351760864257812,0,0.2619247436523438,0.300079345703125,0,0.333740234375,0.3483428955078125,0,0,0.3620529174804688,0.1873550415039062,0,0,0,0,0,-1.988365173339844,0,0.22882080078125,0,0.2486724853515625,0,0.2840728759765625,0,0.3183822631835938,0.3450927734375,0.3581695556640625,0,0,0.2657241821289062,0,0,0,-2.008018493652344,0.2177658081054688,0.2465438842773438,0,0.2835693359375,0,0.317626953125,0,0.3472518920898438,0.353759765625,0.30120849609375,0,0,0,-1.978431701660156,0.2208175659179688,0.2490005493164062,0.2882537841796875,0,0.3237991333007812,0,0.3514862060546875,0.3596572875976562,0,0.2441177368164062,0,0,0,0,0,0,0,-1.91949462890625,0.2275161743164062,0,0.2474212646484375,0.2849884033203125,0,0.320068359375,0,0.3488311767578125,0,0.3562164306640625,0,0.1921768188476562,0,0,0,0,0,-1.856643676757812,0.2272415161132812,0,0.2509307861328125,0.2902374267578125,0.3254547119140625,0,0.3495330810546875,0,0.3580398559570312,0.112060546875,0,0,0,-1.759819030761719,0,0.232818603515625,0,0.2611770629882812,0.2996444702148438,0.3362808227539062,0.3549880981445312,0.3307342529296875,0,0,0,0,0,0,0,0,0,0,0,-1.743766784667969,0,0.229339599609375,0,0.2589492797851562,0,0.2955703735351562,0.3304290771484375,0.3463516235351562,0,0.3381576538085938,0,0,0,0,0,-1.858367919921875,0.2094879150390625,0,0.2429962158203125,0,0.2798995971679688,0,0.3525161743164062,0,0.3516693115234375,0,0.3585052490234375,0,0,0.1173934936523438,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.862541198730469,0,0,0.188262939453125,0,0.224853515625,0.2268218994140625,0.2777786254882812,0,0.3128738403320312,0,0.3383865356445312,0.3467330932617188,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.832420349121094,0,0,0,0,0,0.2358474731445312,0.2541961669921875,0,0.2789077758789062,0.3169021606445312,0.3290023803710938,0,0.314239501953125,0,0.3569717407226562,0.3879318237304688,0,0.4077835083007812,0.376220703125,0.3360595703125,0,0,0.3349761962890625,0,0.3687286376953125,0.3347549438476562,0,0.3334579467773438,0.3350906372070312,0.3357620239257812,0.33551025390625,0.3316192626953125,0,0.3335723876953125,0,0,0.3326644897460938,0,0.3331222534179688,0.333160400390625,0.00983428955078125,0,0,0,0,0,-7.123161315917969,0,0.2640914916992188,0.2968673706054688,0,0,0.3290023803710938,0,0.32427978515625,0,0.3295974731445312,0.365997314453125,0,0,0.3835830688476562,0,0.3918228149414062,0,0.398529052734375,0,0.3965530395507812,0,0.4055252075195312,0,0.4081649780273438,0,0.40765380859375,0,0.4067230224609375,0,0.4117584228515625,0.4139175415039062,0,0.414794921875,0,0.414093017578125,0,0.3967742919921875,0,0.1724929809570312,0,0,0,0,0,-7.114288330078125,0,0.2569198608398438,0,0,0.2818603515625,0.3097152709960938,0,0.3187713623046875,0,0.3264007568359375,0,0.3677825927734375,0.3768157958984375,0.3946456909179688,0.4056549072265625,0,0,0.4153289794921875,0.4152374267578125,0,0.4155197143554688,0,0.4138946533203125,0,0.414337158203125,0,0,0.4139785766601562,0.4141082763671875,0,0.3958206176757812,0.4153518676757812,0,0.39678955078125,0,0,0.1711273193359375,0,0,0,-7.028289794921875,0,0.2544403076171875,0,0.2724533081054688,0.3025970458984375,0,0.3090362548828125,0,0.3316116333007812,0,0.3668746948242188,0.3741989135742188,0,0.3909072875976562,0,0.4037704467773438,0,0.408538818359375,0,0,0.4532928466796875,0.4130783081054688,0.4143142700195312,0.4136810302734375,0,0.4123687744140625,0,0.4111862182617188,0,0.411712646484375,0.4073944091796875,0,0.3921585083007812,0.08710479736328125,0,0,0,-6.880058288574219,0,0.2507553100585938,0.2658615112304688,0,0.2866058349609375,0.29302978515625,0,0.3423004150390625,0,0.3639755249023438,0,0,0.3736419677734375,0.3882522583007812,0,0.383575439453125,0.4022293090820312,0,0.4077911376953125,0,0.4113616943359375,0,0.4103851318359375,0,0.4109725952148438,0,0.4120330810546875,0,0.4129257202148438,0,0.4137191772460938,0,0.4080581665039062,0.396209716796875,0.045562744140625,0,0,0,0,0,-6.719329833984375,0,0,0.2514801025390625,0,0.2672195434570312,0,0.2816848754882812,0,0.306182861328125,0,0.3460235595703125,0,0.362335205078125,0,0.362548828125,0,0.3827133178710938,0,0.3948211669921875,0,0.3986892700195312,0,0.399200439453125,0,0.4040603637695312,0.4055709838867188,0,0.3722076416015625,0,0.372161865234375,0,0.3894195556640625,0,0.35986328125,0.3316497802734375,0,0.3470916748046875,0.1802902221679688,0,0,0,0,0,-6.537513732910156,0,0.170989990234375,0.2408676147460938,0,0.246826171875,0,0.219940185546875,0.296661376953125,0,0.3318939208984375,0.3258132934570312,0,0,0.3128509521484375,0,0.34765625,0,0.3513336181640625,0,0.3535614013671875,0,0.3589935302734375,0,0.381011962890625,0.3421707153320312,0,0.3734207153320312,0.3898696899414062,0,0,0.3661880493164062,0.374481201171875,0,0.3867340087890625,0.36920166015625,0.18988037109375,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-6.634025573730469,0,0,0,0,0,0.0570831298828125,0.239105224609375,0,0.2679519653320312,0,0.228118896484375,0,0.2752151489257812,0.3184432983398438,0,0.30291748046875,0.3328857421875,0.3498916625976562,0.37042236328125,0,0.3889694213867188,0,0.4009628295898438,0.405548095703125,0,0,0.4018402099609375,0,0,0.4048690795898438,0,0.4009475708007812,0,0.400390625,0,0.4002761840820312,0,0,0.4050521850585938,0.396514892578125,0,0.07627105712890625,0,0,0,-6.460838317871094,0.2254180908203125,0,0.2451400756835938,0,0.254638671875,0,0.2718582153320312,0.3301925659179688,0,0.3314590454101562,0.3023452758789062,0.3246536254882812,0,0,0.3560714721679688,0,0.3657073974609375,0.316558837890625,0.3723297119140625,0,0.3858489990234375,0,0.31884765625,0,0,0.3802337646484375,0,0.3927841186523438,0.3412933349609375,0,0.3778305053710938,0.3938751220703125,0,0,0.3604049682617188,0,0,0,0,0,0,0,0,-6.351577758789062,0.2063980102539062,0,0,0.2397308349609375,0.249237060546875,0.284881591796875,0,0.3163986206054688,0,0.33636474609375,0,0.3288803100585938,0.3636932373046875,0.3658676147460938,0,0.3813400268554688,0,0,0.34326171875,0,0.3822021484375,7.822601318359375,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7.62939453125,7.62939453125e-06,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,15.2587890625,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7.671989440917969,0,0,0,0,0,0,0,15.35262298583984,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"filename":["<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,null,"<expr>","<expr>",null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>","<expr>",null,null,null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,null,null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>","<expr>",null,null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,null,null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,null,null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,null,null,null,null,null,null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,null,"<expr>","<expr>","<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,null,null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,null,null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,null,null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,null,null,"<expr>","<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null]},"interval":10,"files":[{"filename":"<expr>","content":"## Generate Large Random Dataset\nn <- 2e6\nx <- runif(n)\ny <- runif(n)\nz <- runif(n)\nXYZ <- cbind(x,y,z)\n\n## Inspect 4 equivalent `row mean` calculations \nprofvis::profvis({\n    m <- rowSums(XYZ)/ncol(XYZ)\n    m <- rowMeans(XYZ)\n    m <- apply(XYZ, 1, mean)\n    m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }\n})\n## rowSums(), colSums(), rowMeans(), and colMeans() are vectorised and fast.\n## for loop is not the slowest, but the ugliest.","normpath":"<expr>"}],"prof_output":"/tmp/Rtmpf4PlN0/file46b94d23cc65.prof","highlight":{"output":["^output\\$"],"gc":["^<GC>$"],"stacktrace":["^\\.\\.stacktraceo(n|ff)\\.\\.$"]},"split":"h"}},"evals":[],"jsHooks":[]}</script>
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
## 1 mean1(x, 0.5)     20ms   21.8ms      45.9    7.63MB     2.09
## 2 mean2(x, 0.5)   19.1ms   20.9ms      48.0    7.63MB     0   
## 3 mean3(x, 0.5)     20ms   21.8ms      46.5    7.63MB     2.11
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
##   0.105   0.000   0.033
```

```r
system.time({ lm(Y~X, data=DAT) })
```

```
##    user  system elapsed 
##   0.407   0.000   0.139
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
## 1 ma1(y)      173.8ms  174.2ms      5.74    15.3MB     2.87
## 2 ma2(y)       21.4ms   21.4ms     46.8     91.6MB   749.
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
##   0.028   0.001   0.028
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
##   0.789   0.237   0.578
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





