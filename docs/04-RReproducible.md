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
<div class="plotly html-widget html-fill-item" id="htmlwidget-8fc7e83dc1d6383cd39d" style="width:672px;height:480px;"></div>
<script type="application/json" data-for="htmlwidget-8fc7e83dc1d6383cd39d">{"x":{"visdat":{"27a466e6e454":["function () ","plotlyVisDat"]},"cur_data":"27a466e6e454","attrs":{"27a466e6e454":{"x":{},"y":{},"alpha_stroke":1,"sizes":[10,100],"spans":[1,20]}},"layout":{"margin":{"b":40,"l":60,"t":25,"r":10},"xaxis":{"domain":[0,1],"automargin":true,"title":"X"},"yaxis":{"domain":[0,1],"automargin":true,"title":"Y"},"hovermode":"closest","showlegend":false},"source":"A","config":{"modeBarButtonsToAdd":["hoverclosest","hovercompare"],"showSendToCloud":false},"data":[{"x":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100],"y":[8.45505841006689,10.225758805049669,13.11076667293576,16.860795557630798,22.343052955009913,24.292840377332226,28.213766282221492,30.485135330163384,35.44949567535086,42.539106862356796,41.172113033082319,49.476556296861673,54.882430388632187,56.689464380772961,59.070495945268128,64.949321167054521,67.430563017575352,71.767142269327067,76.365967502313126,78.585266392616106,81.321259311953753,86.704402130529203,88.702686486818649,95.976605628220227,99.810857897087772,109.39803871175269,107.03625390879122,109.16910435273161,114.64996344859226,120.61799687663519,123.10362333584818,129.03684877361266,133.36933414506782,135.52701201880379,139.16976432320192,143.56679890510807,147.61219814695963,151.99480908974499,155.79108801992962,162.6147732088177,162.41680754432488,166.01936241856629,170.87369656658095,177.20376475385936,175.65927266366907,186.82313403860576,187.42332870712227,190.34790682381163,192.53102463840162,199.44632656175781,205.79038524493424,207.18668225668594,213.91168849121044,216.85317656260506,216.80880815540547,223.88193767663566,231.14527357899985,234.27933957680332,241.54228176838441,237.93450518076665,247.14508001698655,245.80138227068198,249.84716101205706,257.12266948537621,259.49830626941917,264.43875817068079,267.79137331128356,272.26048322421178,277.30462207569968,281.38127146931646,282.08918449221846,289.68659773494505,291.32062082290588,298.35748616794672,298.94873216909048,304.44906002959976,306.79034482667657,311.71147498144126,312.44018601586419,318.27605856557386,324.07912733226084,323.92255118085376,330.05781894356005,335.16702706982653,341.56288802094548,344.71917820748348,350.37864784503444,350.10086067113656,355.86213321945684,359.74860541171927,363.9018064555238,367.20614794128386,370.63280659387266,376.29932709681793,378.74020492397904,383.2868110710495,389.05862045031637,392.6913240841435,391.99227418202025,400.44053674478982],"type":"scatter","mode":"markers","marker":{"color":"rgba(31,119,180,1)","line":{"color":"rgba(31,119,180,1)"}},"error_y":{"color":"rgba(31,119,180,1)"},"error_x":{"color":"rgba(31,119,180,1)"},"line":{"color":"rgba(31,119,180,1)"},"xaxis":"x","yaxis":"y","frame":null}],"highlight":{"on":"plotly_click","persistent":false,"dynamic":false,"selectize":false,"opacityDim":0.20000000000000001,"selected":{"opacity":1},"debounce":0},"shinyEvents":["plotly_hover","plotly_click","plotly_selected","plotly_relayout","plotly_brushed","plotly_brushing","plotly_clickannotation","plotly_doubleclick","plotly_deselect","plotly_afterplot","plotly_sunburstclick"],"base_url":"https://plot.ly"},"evals":[],"jsHooks":[]}</script>
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
## Ncells 1212919 64.8    2365977 126.4  2365977 126.4
## Vcells 2298838 17.6    8388608  64.0  3571816  27.3
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
<div class="profvis html-widget html-fill-item" id="htmlwidget-39651101b44d0619e574" style="width:100%;height:600px;"></div>
<script type="application/json" data-for="htmlwidget-39651101b44d0619e574">{"x":{"message":{"prof":{"time":[1,2,3,4,5,6,7,8,9,10,11,12,13,13,14,14,15,15,16,16,17,17,18,18,19,19,20,20,21,21,22,22,23,23,24,24,25,25,26,26,27,27,28,28,29,29,30,31,31,32,32,33,33,34,35,35,36,36,37,37,38,38,39,39,39,40,41,41,42,43,43,44,44,45,45,46,46,47,48,48,49,49,50,51,51,52,53,54,54,55,56,56,57,57,58,59,59,59,60,60,61,61,62,62,63,63,64,64,65,65,66,67,67,67,68,69,70,70,71,71,72,72,73,73,74,74,74,75,76,77,77,78,78,79,79,80,81,81,81,82,83,83,84,84,85,85,86,86,87,88,88,89,89,89,90,90,91,92,93,93,94,94,95,95,96,96,97,97,98,99,99,100,101,101,102,102,103,103,103,104,105,105,106,106,107,107,107,108,108,109,109,110,111,111,112,112,113,113,114,114,115,115,116,116,117,117,117,118,119,119,120,120,121,121,122,123,124,124,125,125,125,126,126,126,127,127,128,129,129,130,130,131,131,132,133,133,134,134,135,136,136,137,137,138,139,140,140,141,142,142,143,143,143,144,144,145,145,145,146,146,147,147,148,148,148,149,150,150,151,152,153,153,154,154,154,155,156,156,157,157,158,159,159,159,160,160,161,162,162,163,163,164,165,165,166,167,168,168,168,169,169,169,170,171,171,172,172,173,173,173,174,174,174,175,176,176,177,177,178,178,178,179,179,180,180,181,181,182,183,184,184,185,186,186,187,187,188,189,189,190,191,192,192,193,194,194,194,195,195,196,196,197,198,199,199,199,200,200,200,201,201,202,202,203,204,204,204,205,206,206,207,207,208,209,209,210,210,211,211,212,213,213,214,214,215,216,217,217,218,218,219,219,220,221,221,222,222,223,223,224,224,225,225,225,226,226,226,227,227,228,228,229,229,230,230,231,231,232,232,233,233,234,234,235,235,235,236,236,236,237,238,238,238,239,240,240,241,242,242,243,243,243,244,244,244,245,245,246,246,247,247,248,248,249,249,250,250,250,251,251,251,252,252,253,254,254,255,255,256,257,257,258,259,259,260,261,262,263,263,264,265,265,265,266,266,266,267,267,268,268,269,270,270,271,272,273,273,274,274,275,276,276,277,277,278,279,280,280,280,281,282,282,283,283,284,284,285,285,285,286,287,288,288,289,290,290,291,292,292,293,293,294,294,295,295,296,297,298,298,299,299,300,300,300,301,301,302,302,303,304,304,305,305,305,306,306,307,307,307,308,308,309,309,310,310,311,312,313,314,315,316,316,316,317,318,318,318,319,319,319,320,320,320,321,321,321,322,322,322,323,323,323,324,324,324,325,325,325,326,326,326,327,327,327,328,328,328,329,329,329,330,330,331,331,332,333,333,334,335,335,336,337,337,338,339,339,339,340,341,341,342,342,343,343,344,344,345,345,346,347,347,348,348,349,350,351,351,352,352,353,353,354,354,355,356,356,356,357,358,358,359,359,360,360,361,361,362,362,363,363,364,365,365,365,366,366,366,367,367,368,368,369,369,370,370,371,371,372,373,374,375,376,376,377,377,378,378,379,379,379,380,380,381,381,382,382,382,383,384,384,385,385,385,386,386,387,387,388,389,389,389,390,390,390,391,392,392,393,393,394,394,395,395,396,396,397,398,399,400,400,401,401,401,402,402,403,403,404,404,405,405,406,406,407,407,408,409,410,410,411,411,412,412,412,412,413,413,413,413,414,414,415,416,416,416,417,417,418,419,419,420,420,421,422,422,423,423,424,424,424,425,425,426,427,427,428,429,429,429,430,431,431,432,432,433,433,434,434,435,435,436,437,438,439,439,440,441,441,441,442,442,443,444,444,445,445,446,446,447,447,448,448,448,449,450,451,451,452,453,453,454,454,455,456,456,457,457,457,458,459,459,460,460,461,461,462,462,463,464,465,465,466,466,467,467,468,468,468,469,469,470,471,471,471,472,473,473,474,475,475,475,476,477,477,478,478,479,479,479,480,480,481,482,483,483,483,484,485,485,486,486,486,487,487,488,489,489,489,489,490,490,490,490,491,491,492,492,493,493,494,494,495,495,496,497,497,498,499,499,499,500,500,500,501,501,502,502,503,503,504,505,506,506,506,507,507,508,509,509,510,510,511,511,512,512,513,513,514,514,515,516,516,516,517,518,518,519,519,520,520,520,521,521,521,522,522,523,524,525,526,526,527,528,528,528,529,529,530,530,530,530,531,531,531,531,532,533,534,534,535,535,535,536,536,537,537,537,538,538,539,539,540,540,540,540,541,541,541,541,542,542,543,543,544,544,545,545,546,546,547,547,548,548,549,549,550,550,551,551,552,553,554,555,555,556,556,557,557,558,558,559,559,559,560,560,560,561,561,561,562,562,562,563,563,563,564,564,564,565,565,565,566,566,566,567,567,567,568,568,568,569,569,569,570,570,570,571,571,571,572,572,572,573,573,573,574,574,574,575,575,575,576,576,576,577,577,577,578,578,578,579,579,579,580,580,580,581,581,581,582,582,582,583,583,583,584,584,584,585,585,585,586,586,586,587,587,587,588,588,588,589,589,589,590,590,590,591,591,591,592,592,592,593,593,593,594,594,595,596,597,598,598,599,599,600,600,601,601,602,602,603,603,604,604,605,606,607,608,609,609,610,610,611,611,612,612,613,613,614,615,615,616,616,617,617,618,618,618,619,619,620,620,620,621,621,621,622,623,623,624,624,625,625,626,626,627,627,628,628,629,629,630,631,631,632,633,634,634,635,636,636,637,638,639,640,641,642,642,642,643,643,643,644,644,645,645,646,646,647,648,648,649,649,650,650,651,652,652,653,653,654,654,655,656,657,657,658,658,659,660,661,661,662,663,663,664,664,664,665,665,666,666,667,667,668,668,669,669,670,670,670,671,671,672,672,673,673,673,674,675,675,676,676,677,678,679,679,680,680,681,681,681,682,683,684,684,685,685,686,686,687,687,688,688,689,689,690,690,691,692,692,693,693,694,695,696,696,697,697,698,698,699,700,700,701,701,702,703,703,704,704,705,705,705,706,706,707,708,708,709,709,710,711,711,712,712,713,713,714,714,715,715,716,717,717,718,718,719,719,719,720,721,722,723,724,724,725,726,726,727,727,728,728,728,729,729,730,730,731,731,732,733,734,735,735,736,736,737,737,737,738,738,738,739,740,741,742,743,743,744,744,745,745,746,747,747,748,749,750,751,751,752,752,753,753,753,754,754,755,755,756,756,757,758,758,759,759,759,760,760,760,761,761,761,762,763,763,764,764,765,765,766,767,768,769,769,770,770,771,771,772,773,773,774,774,775,775,776,776,777,778,779,779,779,780,780,780,780,781,781,781,781,782,782,783,783,784,785,786,786,786,787,787,788,788,789,789,790,790,791,791,792,792,793,793,794,794,794,795,796,797,797,798,799,799,800,800,800,801,801,801,802,802,802,803,803,804,804,805,806,806,807,807,808,809,809,810,811,811,812,813,813,814,815,815,816,816,817,818,818,819,819,820,820,821,821,822,822,823,823,824,824,825,825,826,827,828,829,830,831,832,832,833,833,833,834,835,836,836,837,837,838,838,838,839,839,840,840,841,842,842,843,844,844,844,845,845,845,846,846,847,848,848,849,849,850,850,851,851,852,853,853,854,854,855,855,855,856,856,857,857,858,859,859,860,861,862,862,863,863,863,864,864,865,865,866,866,866,867,867,867,868,869,869,870,870,871,871,872,872,873,874,874,875,875,876,876,877,877,878,879,879,880,880,881,882,882,883,883,884,885,886,886,886,887,887,887,888,889,890,890,891,892,892,893,893,894,894,895,895,896,896,897,897,898,898,898,899,900,900,901,901,902,902,903,904,905,905,906,906,906,907,907,907,908,908,909,909,910,910,911,911,912,913,914,914,914,915,915,916,916,917,917,918,918,919,919,920,920,920,921,921,922,923,924,925,925,925,926,926,926,927,927,928,928,929,930,930,931,931,932,932,933,933,934,934,935,935,936,936,937,938,938,939,939,940,940,941,942,942,943,943,944,944,945,945,946,946,947,947,948,948,949,949,950,950,951,952,953,953,954,954,955,956,956,957,957,958,959,959,960,961,961,962,963,963,963,964,964,964,965,965,966,967,967,968,969,970,970,971,971,972,973,973,974,974,975,976,977,977,978,978,979,979,980,981,982,982,983,983,984,984,985,985,986,986,987,988,988,989,989,989,990,991,991,992,993,994,994,995,996,997,997,998,999,999,1000,1000,1001,1001,1001,1002,1002,1002,1003,1003,1004,1004,1005,1006,1007,1007,1008,1009,1009,1010,1010,1010,1011,1011,1011,1012,1013,1014,1014,1015,1015,1016,1017,1017,1018,1019,1019,1020,1020,1020,1021,1021,1021,1022,1023,1023,1023,1024,1024,1025,1025,1026,1027,1027,1028,1029,1029,1030,1030,1031,1032,1033,1033,1034,1034,1035,1035,1036,1036,1037,1037,1038,1038,1038,1039,1039,1039,1040,1040,1040,1041,1041,1041,1042,1042,1042,1043,1043,1043,1044,1044,1044,1045,1045,1045,1046,1046,1046,1047,1047,1047,1048,1048,1048,1049,1049,1049,1050,1050,1050,1051,1051,1051,1052,1052,1052,1053,1053,1053,1054,1054,1054,1055,1055,1056,1056,1056,1057,1057,1058,1058,1058,1059,1060,1061,1062,1062,1063,1064,1065,1066,1066,1067,1067,1068,1069,1070,1071,1071,1072,1072,1073,1073,1074,1074,1074,1075,1075,1076,1077,1078,1078,1079,1079,1080,1081,1081,1082,1082,1083,1084,1085,1085,1086,1086,1087,1087,1088,1088,1089,1089,1090,1090,1091,1092,1093,1093,1094,1094,1095,1095,1096,1097,1098,1099,1099,1100,1101,1101,1102,1103,1104,1105,1105,1105,1106,1106,1106,1107,1107,1107,1108,1108,1108,1109,1109,1110,1110,1111,1112,1113,1113,1114,1114,1114,1115,1115,1116,1116,1117,1118,1119,1120,1121,1122,1122,1123,1123,1124,1124,1125,1125,1126,1126,1127,1127,1128,1128,1129,1129,1129,1130,1130,1131,1131,1131,1132,1132,1133,1134,1134,1135,1135,1136,1137,1137,1138,1138,1139,1139,1140,1140,1141,1141,1142,1142,1142,1143,1143,1143,1144,1144,1145,1145,1145,1146,1147,1147,1148,1149,1149,1150,1151,1152,1152,1153,1153,1154,1154,1155,1155,1156,1156,1157,1158,1158,1159,1159,1159,1160,1160,1160,1161,1162,1162,1163,1163,1164,1165,1166,1166,1167,1168,1169,1169,1170,1171,1171,1172,1172,1173,1174,1174,1175,1175,1176,1176,1176,1176,1177,1177,1177,1177,1178,1179,1179,1180,1180,1181,1182,1182,1183,1184,1184,1185,1185,1186,1186,1187,1188,1188,1189,1189,1190,1190,1191,1191,1192,1192,1193,1193,1193,1194,1194,1194,1195,1195,1196,1196,1197,1198,1199,1200,1200,1201,1201,1202,1202,1203,1203,1203,1204,1204,1205,1206,1206,1207,1208,1208,1209,1210,1210,1210,1211,1211,1211,1212,1212,1212,1213,1213,1214,1215,1215,1216,1216,1217,1217,1218,1218,1219,1220,1220,1221,1221,1221,1222,1222,1223,1223,1224,1225,1225,1226,1226,1227,1228,1228,1228,1229,1229,1229,1230,1230,1230,1231,1231,1231,1232,1232,1233,1233,1234,1234,1235,1235,1236,1236,1237,1237,1238,1238,1239,1239,1240,1240,1241,1241,1242,1243,1243,1244,1244,1245,1246,1246,1247,1247,1248,1248,1249,1249,1250,1251,1252,1252,1253,1253,1253,1254,1254,1255,1255,1256,1256,1257,1257,1258,1258,1259,1260,1260,1261,1261,1262,1262,1263,1263,1264,1265,1265,1266,1266,1267,1267,1268,1268,1269,1269,1270,1270,1271,1272,1272,1272,1273,1273,1274,1274,1275,1276,1276,1277,1277,1278,1279,1280,1280,1281,1281,1282,1282,1282,1283,1283,1283,1284,1284,1285,1285,1286,1287,1288,1288,1289,1290,1290,1291,1291,1292,1292,1293,1294,1294,1294,1295,1295,1296,1296,1297,1297,1298,1298,1298,1299,1299,1299,1300,1300,1301,1301,1302,1302,1303,1303,1303,1304,1305,1305,1306,1307,1307,1308,1308,1309,1309,1310,1311,1311,1312,1312,1312,1313,1313,1314,1314,1315,1315,1315,1316,1316,1316,1317,1317,1317,1318,1318,1319,1319,1320,1320,1321,1321,1322,1323,1323,1324,1324,1325,1326,1327,1327,1328,1329,1330,1331,1332,1332,1333,1333,1334,1334,1335,1335,1335,1336,1336,1337,1337,1338,1338,1339,1339,1340,1340,1341,1341,1342,1342,1343,1344,1344,1345,1345,1346,1347,1347,1347,1348,1348,1348,1349,1349,1349,1350,1350,1350,1351,1352,1353,1353,1353,1354,1354,1355,1355,1356,1356,1357,1357,1358,1359,1359,1360,1360,1361,1361,1362,1362,1363,1363,1363,1364,1364,1364,1365,1366,1366,1367,1367,1367,1368,1368,1369,1369,1370,1371,1372,1373,1373,1374,1374,1375,1375,1376,1376,1377,1377,1377,1377,1378,1378,1378,1378,1379,1380,1380,1381,1381,1382,1382,1383,1383,1384,1384,1385,1386,1386,1387,1388,1388,1388,1389,1389,1390,1390,1391,1391,1391,1392,1392,1392,1393,1393,1393,1394,1394,1395,1395,1396,1397,1397,1398,1399,1399,1400,1400,1401,1401,1401,1402,1402,1402,1403,1403,1404,1404,1405,1405,1406,1406,1407,1407,1408,1408,1409,1409,1410,1410,1411,1411,1412,1412,1413,1413,1414,1414,1415,1415,1416,1416,1417,1417,1418,1418,1419,1419,1420,1420,1421,1422,1422,1422,1423,1424,1425,1425,1426,1426,1427,1428,1428,1429,1430,1431,1431,1432,1432,1433,1433,1433,1434,1434,1434,1435,1435,1435,1436,1436,1437,1437,1438,1439,1439,1440,1441,1441,1442,1442,1443,1443,1444,1444,1445,1446,1446,1447,1447,1448,1448,1449,1450,1450,1451,1451,1452,1452,1452,1453,1453,1454,1454,1455,1455,1456,1456,1457,1458,1459,1459,1459,1460,1461,1461,1461,1462,1462,1462,1463,1463,1464,1465,1465,1466,1467,1467,1468,1468,1469,1469,1470,1470,1471,1472,1473,1473,1474,1474,1474,1475,1475,1475,1476,1476,1477,1477,1478,1478,1479,1479,1480,1481,1481,1482,1482,1483,1483,1484,1484,1485,1486,1486,1487,1487,1488,1488,1489,1489,1490,1490,1491,1492,1492,1493,1493,1494,1494,1495,1495,1496,1496,1497,1497,1498,1499,1499,1500,1500,1500,1501,1501,1501,1502,1502,1502,1503,1503,1504,1504,1505,1506,1506,1507,1508,1508,1509,1510,1511,1512,1512,1513,1513,1513,1514,1514,1514,1515,1515,1515,1516,1516,1517,1517,1517,1518,1518,1519,1519,1520,1520,1521,1522,1523,1524,1524,1525,1526,1526,1526,1527,1527,1527,1528,1528,1529,1530,1531,1531,1532,1532,1533,1534,1535,1535,1536,1537,1537,1538,1538,1538,1539,1539,1539,1540,1540,1540,1541,1542,1542,1543,1544,1544,1545,1545,1546,1546,1547,1547,1548,1549,1549,1550,1550,1550,1551,1551,1551,1552,1552,1552,1553,1553,1554,1554,1555,1555,1556,1556,1557,1557,1558,1559,1559,1560,1560,1561,1561,1562,1562,1563,1563,1564,1564,1565,1565,1566,1566,1567,1568,1569,1570,1570,1571,1571,1571,1572,1573,1573,1574,1574,1575,1575,1575,1575,1576,1576,1576,1576,1577,1577,1578,1578,1579,1579,1580,1581,1581,1582,1582,1583,1583,1584,1585,1586,1587,1587,1588,1588,1589,1590,1590,1591,1591,1592,1592,1593,1594,1594,1595,1595,1596,1596,1597,1597,1598,1599,1599,1600,1600,1601,1601,1602,1602,1603,1603,1604,1605,1605,1606,1606,1607,1607,1608,1608,1609,1610,1610,1610,1611,1611,1611,1612,1612,1612,1613,1613,1613,1614,1614,1614,1615,1615,1615,1616,1616,1616,1617,1617,1617,1618,1618,1618,1619,1619,1620,1620,1621,1622,1623,1623,1624,1625,1626,1627,1628,1628,1629,1629,1630,1630,1631,1631,1632,1632,1633,1633,1634,1634,1635,1635,1636,1636,1637,1637,1638,1638,1639,1639,1640,1640,1641,1641,1642,1642,1643,1643,1644,1644,1645,1645,1646,1646,1647,1647,1648,1648,1649,1649,1650,1650,1651,1651,1652,1652,1653,1653,1654,1654,1655,1655,1656,1656,1657,1657,1658,1658,1659,1659,1660,1660,1661,1661,1662,1662,1663,1663,1664,1664,1665,1665,1666,1666,1667,1667,1668,1668,1669,1669,1670,1670,1671,1671,1672,1672,1673,1673,1674,1674,1675,1675,1676,1676,1677,1677,1678,1678,1679,1679,1680,1680,1681,1681,1682,1682,1683,1683,1684,1684,1685,1685,1686,1686,1687,1687,1688,1688,1689,1689,1690,1690,1691,1691,1692,1692,1693,1693,1694,1694,1695,1695,1696,1696,1697,1697,1698,1699,1699,1700,1700,1701,1701,1702,1703,1704,1704,1705,1705,1706,1707,1707,1708,1709,1709,1710,1710,1711,1711,1712,1713,1713,1714,1714,1715,1715,1716,1716,1717,1717,1718,1719,1719,1720,1721,1721,1722,1723,1724,1725,1725,1726,1726,1727,1728,1728,1729,1729,1730,1730,1731,1731,1732,1733,1733,1734,1734,1734,1735,1735,1735,1736,1736,1736,1737,1737,1737,1738,1738,1739,1740,1740,1741,1741,1742,1742,1743,1743,1743,1744,1744,1745,1745,1746,1746,1747,1747,1748,1749,1749,1750,1750,1750,1751,1752,1753,1753,1754,1755,1756,1756,1757,1757,1758,1758,1759,1759,1760,1760,1761,1762,1763,1764,1764,1765,1766,1766,1767,1767,1768,1768,1769,1769,1770,1770,1771,1771,1772,1773,1773,1774,1774,1774,1775,1775,1776,1776,1777,1778,1779,1779,1780,1780,1781,1781,1782,1782,1782,1783,1783,1784,1784,1785,1786,1787,1787,1788,1788,1789,1789,1790,1790,1791,1791,1792,1793,1793,1794,1795,1795,1796,1797,1797,1798,1798,1799,1799,1800,1801,1802,1802,1803,1803,1803,1804,1804,1804,1805,1805,1805,1806,1806,1807,1807,1808,1808,1809,1809,1810,1810,1811,1811,1812,1812,1813,1813,1814,1814,1815,1816,1816,1817,1817,1818,1819,1819,1820,1820,1821,1821,1822,1823,1823,1823,1824,1824,1825,1825,1825,1826,1826,1827,1827,1828,1828,1829,1830,1830,1831,1831,1832,1832,1833,1833,1834,1834,1835,1835,1836,1836,1837,1837,1837,1838,1838,1838,1839,1839,1839,1840,1840,1841,1841,1842,1842,1843,1843,1843,1844,1844,1845,1845,1846,1846,1847,1847,1848,1849,1849,1850,1851,1851,1852,1852,1853,1853,1854,1854,1855,1855,1856,1856,1857,1857,1858,1858,1859,1859,1860,1860,1861,1861,1862,1862,1863,1863,1864,1865,1866,1866,1866,1867,1868,1869,1869,1870,1871,1871,1871,1872,1872,1872,1873,1873,1873,1874,1874,1874,1875,1875,1875,1876,1876,1877,1877,1878,1879,1880,1880,1881,1881,1882,1882,1883,1883,1884,1885,1885,1886,1887,1888,1888,1889,1890,1890,1891,1891,1892,1893,1893,1894,1894,1894,1895,1895,1896,1896,1897,1897,1898,1899,1899,1900,1900,1901,1901,1902,1903,1903,1904,1904,1905,1905,1906,1906,1907,1907,1908,1908,1909,1909,1910,1911,1912,1912,1913,1913,1914,1915,1915,1916,1916,1917,1918,1918,1918,1919,1919,1920,1920,1921,1921,1922,1923,1924,1925,1925,1926,1927,1927,1927,1928,1928,1928,1929,1930,1931,1931,1932,1933,1933,1934,1935,1936,1937,1937,1938,1939,1939,1940,1940,1941,1941,1942,1942,1943,1943,1944,1944,1945,1945,1946,1946,1947,1947,1948,1948,1949,1949,1950,1950,1951,1951,1952,1953,1953,1954,1954,1955,1955,1956,1956,1957,1957,1958,1958,1959,1959,1960,1960,1961,1961,1961,1962,1962,1963,1964,1964,1965,1966,1967,1968,1968,1969,1969,1970,1970,1971,1971,1971,1972,1972,1973,1973,1974,1974,1975,1976,1977,1977,1978,1978,1979,1979,1980,1980,1980,1981,1981,1981,1981,1982,1982,1982,1982,1983,1983,1983,1983,1984,1984,1985,1985,1986,1987,1988,1989,1989,1990,1991,1991,1992,1992,1993,1993,1994,1994,1995,1995,1996,1997,1998,1998,1998,1999,1999,2000,2001,2001,2002,2003,2003,2004,2004,2005,2006,2007,2007,2008,2008,2009,2009,2010,2011,2011,2012,2013,2013,2014,2014,2015,2015,2016,2016,2017,2017,2018,2018,2019,2020,2020,2021,2022,2022,2023,2023,2023,2024,2024,2025,2026,2027,2027,2028,2028,2029,2029,2030,2030,2031,2031,2032,2032,2033,2033,2034,2034,2035,2035,2036,2036,2037,2037,2038,2038,2039,2039,2040,2041,2041,2042,2042,2043,2043,2044,2044,2045,2045,2046,2046,2047,2047,2048,2048,2049,2049,2050,2050,2051,2051,2052,2052,2053,2053,2054,2054,2055,2055,2056,2056,2057,2057,2058,2058,2059,2059,2060,2060,2061,2061,2062,2062,2063,2063,2064,2064,2065,2065,2065,2065,2065,2065,2065,2065,2066,2066,2066,2066,2066,2067,2067,2067,2067,2067,2067,2067,2067,2068,2068,2068,2068,2068,2068,2068,2068,2069,2069,2069,2069,2069,2069,2069,2069,2070,2070,2070,2070,2070,2070,2070,2070,2071,2071,2071,2071,2071,2071,2071,2071,2072,2072,2072,2072,2072,2072,2072,2072,2073,2073,2073,2073,2073,2073,2073,2073,2074,2074,2074,2074,2074,2074,2074,2074,2075,2075,2075,2075,2075,2075,2075,2075,2076,2076,2076,2076,2076,2076,2076,2076,2077,2077,2077,2077,2077,2077,2077,2077,2078,2078,2078,2078,2078,2078,2078,2078,2079,2079,2079,2079,2079,2079,2079,2079,2080,2080,2080,2080,2080,2080,2080,2080,2081,2081,2081,2081,2081,2081,2081,2081,2082,2082,2082,2082,2082,2082,2082,2082,2083,2083,2083,2083,2083,2083,2083,2083,2084,2084,2084,2084,2084,2084,2084,2084,2085,2085,2085,2085,2085,2085,2085,2085,2086,2086,2086,2086,2086,2086,2086,2086,2087,2087,2087,2087,2087,2087,2087,2087,2088,2088,2088,2088,2088,2088,2088,2088,2089,2089,2089,2089,2089,2089,2089,2089,2090,2090,2090,2090,2090,2090,2090,2090,2091,2091,2091,2091,2091,2091,2091,2091,2092,2092,2092,2092,2092,2092,2092,2092,2093,2093,2093,2093,2093,2093,2093,2093,2094,2094,2094,2094,2094,2094,2094,2094],"depth":[1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,1,1,2,1,1,2,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,1,1,2,1,2,1,2,1,2,1,3,2,1,1,1,2,1,2,1,2,1,1,3,2,1,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,3,2,1,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,1,1,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,1,1,2,1,1,2,1,3,2,1,2,1,3,2,1,2,1,2,1,3,2,1,1,2,1,1,1,2,1,3,2,1,1,2,1,2,1,1,3,2,1,2,1,1,2,1,2,1,1,2,1,1,1,3,2,1,3,2,1,1,2,1,2,1,3,2,1,3,2,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,1,2,1,1,2,1,2,1,1,2,1,1,1,2,1,1,3,2,1,2,1,2,1,1,1,3,2,1,3,2,1,2,1,2,1,1,3,2,1,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,1,3,2,1,1,2,1,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,1,2,1,1,2,1,1,1,1,2,1,1,3,2,1,3,2,1,2,1,2,1,1,2,1,1,1,2,1,2,1,1,2,1,2,1,1,1,3,2,1,1,2,1,2,1,2,1,3,2,1,1,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,3,2,1,2,1,3,2,1,2,1,2,1,2,1,1,1,1,1,1,3,2,1,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,1,2,1,1,2,1,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,1,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,3,2,1,1,2,1,3,2,1,2,1,2,1,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,1,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,4,3,2,1,4,3,2,1,2,1,1,3,2,1,2,1,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,1,2,1,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,1,1,1,2,1,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,1,1,2,1,1,2,1,2,1,1,2,1,3,2,1,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,3,2,1,2,1,1,3,2,1,1,2,1,1,3,2,1,1,2,1,2,1,3,2,1,2,1,1,1,3,2,1,1,2,1,3,2,1,2,1,1,4,3,2,1,4,3,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,3,2,1,3,2,1,2,1,2,1,2,1,1,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,1,2,1,2,1,3,2,1,3,2,1,2,1,1,1,1,2,1,1,3,2,1,2,1,4,3,2,1,4,3,2,1,1,1,2,1,3,2,1,2,1,3,2,1,2,1,2,1,4,3,2,1,4,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,1,2,1,1,2,1,1,1,1,1,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,1,2,1,2,1,1,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,3,2,1,1,2,1,2,1,1,1,2,1,2,1,3,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,1,1,1,1,2,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,1,1,2,1,2,1,3,2,1,3,2,1,1,1,1,1,2,1,2,1,2,1,1,2,1,1,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,3,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,1,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,1,3,2,1,4,3,2,1,4,3,2,1,2,1,2,1,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,1,2,1,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,2,1,1,2,1,1,2,1,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,1,1,1,1,2,1,3,2,1,1,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,1,3,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,1,1,2,1,3,2,1,2,1,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,1,1,3,2,1,3,2,1,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,1,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,1,1,3,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,1,2,1,2,1,1,2,1,1,2,1,1,3,2,1,3,2,1,2,1,1,2,1,1,1,2,1,2,1,1,2,1,2,1,1,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,1,2,1,1,1,2,1,1,1,2,1,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,1,1,2,1,1,2,1,3,2,1,3,2,1,1,1,2,1,2,1,1,2,1,1,2,1,3,2,1,3,2,1,1,3,2,1,2,1,2,1,1,2,1,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,3,2,1,2,1,3,2,1,1,1,1,2,1,1,1,1,2,1,2,1,1,1,1,2,1,2,1,2,1,3,2,1,2,1,1,1,2,1,2,1,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,1,1,1,2,1,1,2,1,1,1,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,1,1,2,1,3,2,1,2,1,2,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,3,2,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,3,2,1,1,2,1,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,3,2,1,1,2,1,2,1,1,1,2,1,1,1,2,1,1,2,1,2,1,1,2,1,2,1,4,3,2,1,4,3,2,1,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,1,1,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,1,2,1,1,3,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,1,2,1,2,1,1,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,1,1,2,1,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,3,2,1,1,2,1,1,2,1,2,1,2,1,1,2,1,3,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,1,2,1,1,1,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,3,2,1,3,2,1,3,2,1,3,2,1,1,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,1,2,1,3,2,1,2,1,2,1,1,1,1,2,1,2,1,2,1,2,1,4,3,2,1,4,3,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,3,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,1,1,2,1,2,1,1,2,1,1,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,1,3,2,1,1,3,2,1,3,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,1,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,1,2,1,1,1,1,2,1,3,2,1,3,2,1,3,2,1,2,1,3,2,1,2,1,2,1,2,1,1,1,1,2,1,1,3,2,1,3,2,1,2,1,1,1,2,1,2,1,1,1,2,1,1,2,1,3,2,1,3,2,1,3,2,1,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,1,2,1,3,2,1,1,2,1,2,1,4,3,2,1,4,3,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,1,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,1,1,2,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,1,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,1,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,1,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,2,1,2,1,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,1,2,1,2,1,2,1,1,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,1,3,2,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,3,2,1,1,1,2,1,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,1,2,1,1,1,2,1,1,2,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,1,2,1,2,1,1,3,2,1,2,1,2,1,2,1,1,1,1,2,1,1,3,2,1,3,2,1,1,1,2,1,1,2,1,1,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,1,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,2,1,2,1,1,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,1,3,2,1,2,1,1,2,1,1,2,1,2,1,1,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,3,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,8,7,6,5,4,3,2,1,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1],"label":["rowSums","rowSums","rowSums","rowSums","rowSums","rowSums","rowMeans","rowMeans","rowMeans","rowMeans","rowMeans","rowMeans","aperm.default","apply","aperm.default","apply","aperm.default","apply","aperm.default","apply","aperm.default","apply","aperm.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","apply","FUN","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","mean.default","apply","apply","FUN","apply","<GC>","apply","FUN","apply","FUN","apply","apply","length","local","mean.default","apply","apply","FUN","apply","apply","apply","mean.default","apply","apply","mean.default","apply","is.numeric","local","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","is.na","local","<GC>","FUN","apply","apply","apply","mean.default","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","apply","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","apply","mean.default","apply","FUN","apply","FUN","apply","is.numeric","local","mean.default","apply","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","<GC>","mean.default","apply","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","<GC>","mean.default","apply","apply","mean.default","apply","FUN","apply","is.numeric","local","apply","apply","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","apply","mean.default","apply","is.na","local","<GC>","apply","apply","mean.default","apply","mean.default","apply","apply","is.numeric","local","FUN","apply","apply","apply","FUN","apply","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","FUN","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","mean.default","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","apply","mean.default","apply","FUN","apply","apply","<GC>","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","mean.default","apply","apply","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","apply","FUN","apply","apply","mean.default","apply","<GC>","apply","apply","FUN","apply","apply","apply","mean.default","apply","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","mean.default","apply","FUN","apply","apply","<GC>","apply","FUN","apply","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","is.numeric","local","mean.default","apply","FUN","apply","FUN","apply","<GC>","length","local","<GC>","length","local","mean.default","apply","mean.default","apply","is.na","local","FUN","apply","FUN","apply","FUN","apply","FUN","apply","length","local","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","<GC>","length","local","apply","length","local","apply","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","mean.default","apply","apply","apply","apply","FUN","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","apply","is.numeric","local","apply","apply","FUN","apply","FUN","apply","apply","mean.default","apply","FUN","apply","apply","apply","<GC>","mean.default","apply","apply","is.numeric","local","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","apply","apply","mean.default","apply","apply","FUN","apply","apply","mean.default","apply","FUN","apply","<GC>","apply","<GC>","apply","apply","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","is.numeric","local","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","apply","apply","apply","apply","isTRUE","mean.default","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","FUN","apply","apply","mean.default","apply","apply","isTRUE","mean.default","apply","apply","FUN","apply","<GC>","apply","mean.default","apply","FUN","apply","length","local","apply","FUN","apply","mean.default","apply","apply","apply","mean.default","apply","FUN","apply","<GC>","apply","<GC>","apply","apply","isTRUE","mean.default","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","is.numeric","local","mean.default","apply","FUN","apply","mean.default","apply","apply","apply","apply","apply","mean.default","apply","<GC>","apply","<GC>","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","isTRUE","mean.default","apply","length","local","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","apply","mean.default","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","mean.default","apply","FUN","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","FUN","apply","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","apply","<GC>","apply","apply","apply","apply","mean.default","apply","apply","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","<GC>","apply","<GC>","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","apply","FUN","apply","is.numeric","local","apply","mean.default","apply","<GC>","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","is.numeric","local","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","<GC>","FUN","apply","length","local","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","<GC>","apply","is.numeric","local","mean.default","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","is.numeric","local","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","apply","apply","mean.default","apply","apply","isTRUE","mean.default","apply","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","apply","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","mean.default","apply","length","local","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","apply","<GC>","apply","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","is.na","local","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","is.na","local","FUN","apply","FUN","apply","FUN","apply","apply","apply","apply","apply","length","local","is.numeric","local","FUN","apply","is.na","local","mean.default","apply","apply","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","is.numeric","local","FUN","apply","FUN","apply","FUN","apply","length","local","mean.default","apply","FUN","apply","apply","is.numeric","local","apply","apply","mean.default","apply","apply","FUN","apply","apply","apply","apply","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","length","local","apply","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","length","local","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","<GC>","apply","<GC>","apply","FUN","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","apply","apply","FUN","apply","is.numeric","local","mean.default","apply","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","apply","mean.default","apply","mean.default","apply","apply","mean.default","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","apply","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","apply","apply","is.numeric","local","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","apply","apply","apply","FUN","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","apply","apply","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","length","local","length","local","apply","is.na","local","<GC>","mean.default","apply","<GC>","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","apply","is.numeric","local","FUN","apply","FUN","apply","mean.default","apply","apply","apply","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","apply","apply","isTRUE","mean.default","apply","mean.default","apply","is.numeric","local","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","mean.default","apply","apply","is.na","local","<GC>","mean.default","apply","<GC>","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","mean.default","apply","apply","FUN","apply","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","apply","length","local","mean.default","apply","length","local","<GC>","apply","<GC>","apply","<GC>","apply","mean.default","apply","mean.default","apply","apply","apply","apply","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","is.numeric","local","apply","length","local","apply","<GC>","length","local","<GC>","length","local","is.numeric","local","apply","length","local","FUN","apply","is.na","local","FUN","apply","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","apply","mean.default","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","length","local","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","apply","FUN","apply","is.numeric","local","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","is.numeric","local","FUN","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","is.na","local","mean.default","apply","FUN","apply","length","local","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","apply","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","FUN","apply","apply","FUN","apply","mean.default","apply","FUN","apply","length","local","mean.default","apply","FUN","apply","FUN","apply","apply","mean.default","apply","length","local","FUN","apply","apply","FUN","apply","FUN","apply","<GC>","apply","<GC>","apply","is.numeric","local","FUN","apply","FUN","apply","mean.default","apply","is.numeric","local","apply","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","FUN","apply","apply","FUN","apply","apply","FUN","apply","apply","<GC>","length","local","<GC>","length","local","FUN","apply","apply","is.numeric","local","apply","apply","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","is.na","local","apply","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","apply","FUN","apply","apply","apply","FUN","apply","apply","FUN","apply","is.na","local","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","apply","is.numeric","local","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","is.na","local","is.numeric","local","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","length","local","isTRUE","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","apply","is.numeric","local","apply","apply","apply","FUN","apply","mean.default","apply","apply","apply","apply","<GC>","apply","<GC>","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","is.na","local","mean.default","apply","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","FUN","apply","is.numeric","local","FUN","apply","<GC>","apply","<GC>","apply","apply","apply","FUN","apply","length","local","mean.default","apply","apply","apply","apply","FUN","apply","apply","mean.default","apply","apply","apply","apply","isTRUE","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","is.na","local","FUN","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","is.numeric","local","length","local","apply","apply","apply","apply","apply","FUN","apply","FUN","apply","<GC>","apply","<GC>","apply","FUN","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","length","local","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","<GC>","length","local","<GC>","length","local","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","FUN","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","<GC>","length","local","<GC>","length","local","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","apply","apply","FUN","apply","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","apply","is.numeric","local","FUN","apply","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","FUN","apply","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","mean.default","apply","apply","mean.default","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","apply","FUN","apply","mean.default","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","length","local","FUN","apply","FUN","apply","FUN","apply","is.numeric","local","length","local","apply","FUN","apply","FUN","apply","apply","mean.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","apply","apply","mean.default","apply","isTRUE","mean.default","apply","is.numeric","local","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","FUN","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","mean.default","apply","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","mean.default","apply","apply","apply","FUN","apply","apply","FUN","apply","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","length","local","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","apply","apply","apply","apply","<GC>","apply","<GC>","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","is.numeric","local","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","is.na","local","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","FUN","apply","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","is.na","local","is.numeric","local","apply","length","local","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","mean.default","apply","apply","FUN","apply","apply","apply","FUN","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","length","local","length","local","mean.default","apply","mean.default","apply","apply","FUN","apply","<GC>","apply","<GC>","apply","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","length","local","apply","apply","isTRUE","mean.default","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","apply","FUN","apply","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","FUN","apply","apply","apply","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","length","local","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","apply","apply","apply","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","apply","length","local","FUN","apply","apply","apply","FUN","apply","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","length","local","apply","FUN","apply","FUN","apply","length","local","mean.default","apply","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","length","local","FUN","apply","is.numeric","local","FUN","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","<GC>","apply","<GC>","apply","mean.default","apply","mean.default","apply","apply","apply","apply","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","apply","apply","<GC>","apply","<GC>","apply","apply","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","is.numeric","local","apply","<GC>","apply","<GC>","apply","FUN","apply","length","local","FUN","apply","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","length","local","apply","apply","FUN","apply","apply","apply","apply","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","length","local","apply","FUN","apply","FUN","apply","mean.default","apply","apply","apply","mean.default","apply","FUN","apply","apply","is.numeric","local","apply","mean.default","apply","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","FUN","apply","apply","FUN","apply","apply","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","apply","mean.default","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","apply","apply","FUN","apply","length","local","FUN","apply","FUN","apply","mean.default","apply","apply","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","apply","<GC>","apply","<GC>","apply","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","apply","apply","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","FUN","apply","apply","mean.default","apply","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","length","local","mean.default","apply","mean.default","apply","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","length","local","is.na","local","mean.default","apply","FUN","apply","FUN","apply","is.numeric","local","mean.default","apply","is.numeric","local","FUN","apply","mean.default","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","apply","apply","mean.default","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","is.numeric","local","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","apply","FUN","apply","apply","apply","FUN","apply","apply","length","local","FUN","apply","apply","length","local","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","FUN","apply","FUN","apply","apply","mean.default","apply","is.numeric","local","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","apply","apply","FUN","apply","mean.default","apply","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","apply","apply","FUN","apply","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","apply","mean.default","apply","apply","FUN","apply","apply","apply","apply","mean.default","apply","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","apply","FUN","apply","apply","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","FUN","apply","FUN","apply","apply","apply","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","apply","isTRUE","mean.default","apply","mean.default","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","mean.default","apply","mean.default","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","apply","any","local","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","cb$commitlocs","codeBufCode","genCode","compile","compiler:::tryCompile","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis"],"filenum":[1,1,1,1,1,1,1,1,1,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,null,1,1,null,1,1,null,1,null,1,null,1,null,1,1,null,null,null,1,1,null,1,1,1,null,1,1,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,null,1,1,1,null,1,null,1,null,1,null,null,null,null,1,1,1,null,1,null,1,null,1,1,null,null,1,1,null,1,null,1,null,1,null,1,1,null,1,null,null,1,null,1,1,1,null,1,null,1,null,1,null,null,null,1,1,null,1,1,null,1,null,1,null,null,1,1,null,1,null,1,null,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,1,null,1,null,1,null,null,1,1,null,1,null,null,1,null,null,1,null,1,1,null,1,null,null,null,1,1,null,1,null,1,1,null,null,null,1,1,1,null,1,1,null,1,null,null,1,null,1,null,null,1,null,1,null,1,null,null,1,1,null,1,1,1,null,1,null,null,1,1,null,1,null,1,1,null,null,1,null,1,1,null,1,null,1,1,null,1,1,1,null,null,1,null,null,1,1,null,1,null,1,null,null,1,null,null,1,1,null,1,null,1,null,null,1,null,1,null,1,null,1,1,1,null,1,1,null,1,null,1,1,null,1,1,1,null,1,1,null,null,1,null,1,null,1,1,1,null,null,1,null,null,1,null,1,null,1,1,null,null,1,1,null,1,null,1,1,null,1,null,1,null,1,1,null,1,null,1,1,1,null,1,null,1,null,1,1,null,null,null,1,null,1,null,1,null,null,null,null,null,null,null,1,null,1,null,null,null,1,null,1,null,1,null,1,null,null,null,null,1,null,null,1,1,null,null,null,1,null,null,1,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,1,1,null,1,null,1,1,null,1,1,null,1,1,1,1,null,1,1,null,null,1,null,null,1,null,1,null,1,1,null,null,1,1,null,1,null,1,1,null,1,null,1,1,1,null,null,1,1,null,null,null,1,null,1,null,null,1,1,1,null,1,1,null,1,1,null,1,null,1,null,1,null,1,1,1,null,1,null,1,null,null,1,null,null,null,1,1,null,1,null,null,1,null,1,null,null,1,null,1,null,1,null,1,1,1,1,1,1,null,null,1,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,1,null,1,1,null,1,1,null,1,1,null,null,1,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,1,1,null,1,null,1,null,1,null,1,1,null,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,null,1,null,null,1,null,1,null,null,null,1,null,1,null,1,1,1,1,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,null,1,1,null,1,null,null,1,null,null,null,1,1,null,null,1,null,null,1,1,null,1,null,1,null,1,null,1,null,1,1,1,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,1,null,1,null,1,null,null,null,1,null,null,null,1,null,1,1,null,null,1,null,1,1,null,1,null,1,1,null,1,null,1,null,null,1,null,1,1,null,1,1,null,null,1,1,null,1,null,1,null,1,null,1,null,1,1,1,1,null,1,1,null,null,1,null,1,1,null,1,null,1,null,1,null,1,null,null,1,1,1,null,1,1,null,1,null,null,1,null,1,null,null,1,1,null,1,null,1,null,1,null,null,1,1,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,1,null,1,1,null,null,1,1,null,1,null,1,null,null,1,null,1,1,1,null,null,1,1,null,1,null,null,1,null,1,1,null,null,null,1,null,null,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,1,null,null,1,null,null,1,null,1,null,1,null,1,1,1,null,null,1,null,1,1,null,1,null,1,null,null,null,1,null,1,null,1,1,null,null,1,1,null,null,null,1,null,null,1,null,null,1,null,1,1,1,1,null,1,1,null,null,1,null,1,null,null,null,1,null,null,null,1,1,1,null,1,null,null,1,null,1,null,null,1,null,1,null,1,null,null,null,1,null,null,null,1,null,1,null,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,1,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,1,1,null,1,null,1,null,1,null,null,null,1,null,1,null,1,1,1,1,1,null,null,null,null,null,1,null,null,null,1,1,null,1,null,1,null,1,null,null,1,null,1,null,null,1,null,null,1,1,null,null,null,1,null,1,null,1,null,null,null,1,null,1,1,null,null,1,1,null,1,1,null,1,1,1,1,1,1,null,null,1,null,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,1,null,1,null,1,null,null,1,1,null,1,null,1,1,1,null,1,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,null,1,null,null,1,1,null,1,null,1,1,1,null,1,null,1,null,null,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,1,1,null,1,null,null,null,1,1,null,1,null,1,1,null,1,null,1,null,null,1,null,1,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,null,1,1,1,1,1,null,1,1,null,1,null,1,null,null,1,null,1,null,1,null,1,1,1,1,null,null,null,1,null,null,1,null,null,1,1,1,1,1,null,1,null,1,null,1,1,null,1,1,1,1,null,1,null,1,null,null,1,null,1,null,null,null,null,1,null,null,null,null,1,null,null,1,null,null,1,1,null,1,null,1,null,1,1,1,1,null,1,null,1,null,1,1,null,null,null,1,null,1,null,1,1,1,null,null,1,null,null,null,1,null,null,null,1,null,1,null,1,1,1,null,null,1,null,1,null,null,null,1,null,1,null,1,null,1,null,1,null,null,1,1,1,null,1,1,null,null,null,null,1,null,null,1,null,null,1,null,1,null,1,1,null,1,null,1,1,null,1,1,null,1,1,null,1,1,null,1,null,1,1,null,null,null,1,null,null,null,1,null,1,null,1,null,1,null,1,1,1,1,1,1,1,null,1,null,null,1,1,1,null,1,null,1,null,null,1,null,1,null,null,1,null,null,1,null,null,null,null,null,null,null,null,1,null,null,null,1,null,null,null,1,1,null,1,null,1,null,null,1,null,1,null,1,1,null,1,1,1,null,1,null,null,1,null,1,null,1,null,null,1,null,null,1,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,1,null,1,null,null,1,1,null,null,1,null,null,1,1,1,null,1,1,null,1,null,1,null,null,null,1,null,1,null,1,null,null,1,1,null,1,null,1,null,1,1,1,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,1,1,null,null,1,null,null,null,1,null,1,null,null,null,1,null,null,1,null,1,1,1,1,null,null,1,null,null,1,null,1,null,1,1,null,1,null,1,null,1,null,null,null,1,null,1,null,1,1,null,1,null,null,null,1,1,null,1,null,1,null,1,null,1,null,null,null,1,null,1,null,1,null,null,1,1,null,1,null,1,1,null,1,null,1,1,null,1,1,null,1,1,null,null,null,null,null,null,null,1,1,null,null,1,1,null,1,null,1,1,null,1,null,1,1,1,null,1,null,1,null,1,1,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,null,1,1,null,1,1,1,null,1,1,1,null,1,1,null,1,null,null,null,null,1,null,null,1,null,1,null,1,1,1,null,1,1,null,null,null,null,1,null,null,1,1,1,null,1,null,1,1,null,1,1,null,1,null,null,1,null,null,1,1,null,null,1,null,1,null,1,1,null,1,1,null,1,null,1,1,1,null,1,null,1,null,1,null,null,null,null,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,null,null,1,null,1,null,null,1,1,1,1,null,null,1,1,1,null,1,null,1,1,1,1,null,1,null,1,null,1,null,null,1,null,1,1,1,null,null,null,1,1,null,1,null,1,1,1,null,1,null,1,null,null,null,1,null,1,null,1,1,1,null,1,null,null,null,1,1,1,1,null,1,1,null,1,1,1,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,null,1,1,1,null,1,null,null,1,null,null,null,null,1,1,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,null,null,1,null,1,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,null,null,null,null,null,null,1,null,null,1,1,null,1,1,null,1,1,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,null,null,null,null,null,1,null,1,null,1,1,1,null,1,1,1,null,1,1,null,1,null,1,1,null,1,null,1,null,null,null,1,null,null,null,1,1,null,null,null,1,1,null,1,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,1,null,1,1,1,1,null,1,null,1,null,1,null,null,1,null,1,1,null,1,1,null,1,1,null,null,1,null,null,1,null,null,1,null,1,1,null,1,null,1,null,1,null,1,1,null,1,null,null,1,null,1,null,1,1,null,1,null,1,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,null,null,null,1,null,1,null,1,null,null,null,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,1,1,null,1,null,null,1,null,null,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,null,1,null,1,null,1,1,null,1,null,1,1,1,null,1,null,1,null,null,1,null,null,1,null,1,null,1,1,1,null,1,1,null,1,null,1,null,1,1,null,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,null,1,1,null,1,1,null,1,null,1,null,null,1,null,1,null,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,1,1,null,1,1,1,1,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,null,null,1,null,1,1,null,1,null,1,1,null,null,1,null,null,1,null,null,1,null,null,1,1,1,null,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,1,null,1,null,null,1,null,1,null,null,1,1,1,null,1,null,1,null,1,null,1,null,null,null,1,null,null,null,1,1,null,1,null,1,null,1,null,1,null,1,1,null,1,1,null,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,null,null,null,1,null,null,1,null,1,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,null,1,1,1,null,1,null,1,1,null,1,1,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,1,null,1,1,null,null,null,null,null,1,null,1,1,null,1,null,1,null,1,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,null,1,1,null,null,1,1,null,null,1,null,null,1,null,1,1,null,1,1,null,1,null,1,null,1,null,1,1,1,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,1,null,1,1,null,1,1,1,1,null,1,null,null,1,null,null,1,null,null,1,null,null,null,null,1,null,1,null,1,null,1,1,1,1,null,1,1,null,null,1,null,null,1,null,1,1,1,null,null,null,1,1,1,null,1,1,null,1,null,null,1,null,null,1,null,null,1,1,null,null,1,null,1,null,1,null,null,null,1,1,null,1,null,null,1,null,null,1,null,null,1,null,null,null,1,null,null,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,1,1,null,1,null,null,1,1,null,1,null,1,null,null,null,1,null,null,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,1,1,1,null,1,null,1,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,null,null,1,1,null,1,null,1,null,1,null,1,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,null,null,1,1,null,1,1,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,1,1,null,1,null,1,1,null,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,1,null,1,1,null,1,1,1,1,null,1,null,1,1,null,1,null,1,null,1,null,1,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,1,null,1,null,null,1,1,1,null,1,1,1,null,1,null,null,null,1,null,1,null,1,1,1,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,null,1,null,1,null,1,1,1,null,1,null,1,null,1,null,null,1,null,1,null,1,1,1,null,1,null,1,null,1,null,1,null,1,1,null,1,1,null,1,1,null,1,null,1,null,1,1,1,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,1,null,1,null,1,null,1,1,null,null,1,null,1,null,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,null,1,null,1,null,null,null,1,null,1,1,null,1,1,null,1,null,1,null,null,null,null,null,1,null,1,null,1,null,null,null,1,null,null,null,1,null,1,null,1,1,1,null,null,1,1,1,null,1,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,null,null,1,1,null,1,null,1,null,1,null,1,1,null,1,1,1,null,1,1,null,null,null,1,1,null,null,null,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,1,null,1,null,null,null,1,null,1,null,1,null,1,null,1,1,1,null,1,null,1,1,null,1,null,1,1,null,null,1,null,1,null,1,null,1,1,1,1,null,1,1,null,null,1,null,null,1,1,1,null,1,1,null,1,1,1,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,1,null,1,1,1,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,1,1,null,1,null,1,null,1,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,1,null,1,1,1,1,null,1,1,null,1,null,1,null,1,null,1,null,1,1,1,null,null,1,null,1,1,null,1,1,null,1,null,1,1,1,null,1,null,1,null,1,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,1,null,1,null,null,1,null,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,null,null,null,null,null,null,null,null,null,null,1,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null],"linenum":[10,10,10,10,10,10,11,11,11,11,11,11,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,null,12,12,null,12,12,null,12,null,12,null,12,null,12,12,null,null,null,12,12,null,12,12,12,null,12,12,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,null,12,12,12,null,12,null,12,null,12,null,null,null,null,12,12,12,null,12,null,12,null,12,12,null,null,12,12,null,12,null,12,null,12,null,12,12,null,12,null,null,12,null,12,12,12,null,12,null,12,null,12,null,null,null,12,12,null,12,12,null,12,null,12,null,null,12,12,null,12,null,12,null,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,12,null,12,null,12,null,null,12,12,null,12,null,null,12,null,null,12,null,12,12,null,12,null,null,null,12,12,null,12,null,12,12,null,null,null,12,12,12,null,12,12,null,12,null,null,12,null,12,null,null,12,null,12,null,12,null,null,12,12,null,12,12,12,null,12,null,null,12,12,null,12,null,12,12,null,null,12,null,12,12,null,12,null,12,12,null,12,12,12,null,null,12,null,null,12,12,null,12,null,12,null,null,12,null,null,12,12,null,12,null,12,null,null,12,null,12,null,12,null,12,12,12,null,12,12,null,12,null,12,12,null,12,12,12,null,12,12,null,null,12,null,12,null,12,12,12,null,null,12,null,null,12,null,12,null,12,12,null,null,12,12,null,12,null,12,12,null,12,null,12,null,12,12,null,12,null,12,12,12,null,12,null,12,null,12,12,null,null,null,12,null,12,null,12,null,null,null,null,null,null,null,12,null,12,null,null,null,12,null,12,null,12,null,12,null,null,null,null,12,null,null,12,12,null,null,null,12,null,null,12,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,12,12,null,12,null,12,12,null,12,12,null,12,12,12,12,null,12,12,null,null,12,null,null,12,null,12,null,12,12,null,null,12,12,null,12,null,12,12,null,12,null,12,12,12,null,null,12,12,null,null,null,12,null,12,null,null,12,12,12,null,12,12,null,12,12,null,12,null,12,null,12,null,12,12,12,null,12,null,12,null,null,12,null,null,null,12,12,null,12,null,null,12,null,12,null,null,12,null,12,null,12,null,12,12,12,12,12,12,null,null,12,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,12,null,12,12,null,12,12,null,12,12,null,null,12,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,12,12,null,12,null,12,null,12,null,12,12,null,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,null,12,null,null,12,null,12,null,null,null,12,null,12,null,12,12,12,12,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,null,12,12,null,12,null,null,12,null,null,null,12,12,null,null,12,null,null,12,12,null,12,null,12,null,12,null,12,null,12,12,12,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,12,null,12,null,12,null,null,null,12,null,null,null,12,null,12,12,null,null,12,null,12,12,null,12,null,12,12,null,12,null,12,null,null,12,null,12,12,null,12,12,null,null,12,12,null,12,null,12,null,12,null,12,null,12,12,12,12,null,12,12,null,null,12,null,12,12,null,12,null,12,null,12,null,12,null,null,12,12,12,null,12,12,null,12,null,null,12,null,12,null,null,12,12,null,12,null,12,null,12,null,null,12,12,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,12,null,12,12,null,null,12,12,null,12,null,12,null,null,12,null,12,12,12,null,null,12,12,null,12,null,null,12,null,12,12,null,null,null,12,null,null,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,12,null,null,12,null,null,12,null,12,null,12,null,12,12,12,null,null,12,null,12,12,null,12,null,12,null,null,null,12,null,12,null,12,12,null,null,12,12,null,null,null,12,null,null,12,null,null,12,null,12,12,12,12,null,12,12,null,null,12,null,12,null,null,null,12,null,null,null,12,12,12,null,12,null,null,12,null,12,null,null,12,null,12,null,12,null,null,null,12,null,null,null,12,null,12,null,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,12,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,12,12,null,12,null,12,null,12,null,null,null,12,null,12,null,12,12,12,12,12,null,null,null,null,null,12,null,null,null,12,12,null,12,null,12,null,12,null,null,12,null,12,null,null,12,null,null,12,12,null,null,null,12,null,12,null,12,null,null,null,12,null,12,12,null,null,12,12,null,12,12,null,12,12,12,12,12,12,null,null,12,null,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,12,null,12,null,12,null,null,12,12,null,12,null,12,12,12,null,12,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,null,12,null,null,12,12,null,12,null,12,12,12,null,12,null,12,null,null,12,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,12,12,null,12,null,null,null,12,12,null,12,null,12,12,null,12,null,12,null,null,12,null,12,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,null,12,12,12,12,12,null,12,12,null,12,null,12,null,null,12,null,12,null,12,null,12,12,12,12,null,null,null,12,null,null,12,null,null,12,12,12,12,12,null,12,null,12,null,12,12,null,12,12,12,12,null,12,null,12,null,null,12,null,12,null,null,null,null,12,null,null,null,null,12,null,null,12,null,null,12,12,null,12,null,12,null,12,12,12,12,null,12,null,12,null,12,12,null,null,null,12,null,12,null,12,12,12,null,null,12,null,null,null,12,null,null,null,12,null,12,null,12,12,12,null,null,12,null,12,null,null,null,12,null,12,null,12,null,12,null,12,null,null,12,12,12,null,12,12,null,null,null,null,12,null,null,12,null,null,12,null,12,null,12,12,null,12,null,12,12,null,12,12,null,12,12,null,12,12,null,12,null,12,12,null,null,null,12,null,null,null,12,null,12,null,12,null,12,null,12,12,12,12,12,12,12,null,12,null,null,12,12,12,null,12,null,12,null,null,12,null,12,null,null,12,null,null,12,null,null,null,null,null,null,null,null,12,null,null,null,12,null,null,null,12,12,null,12,null,12,null,null,12,null,12,null,12,12,null,12,12,12,null,12,null,null,12,null,12,null,12,null,null,12,null,null,12,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,12,null,12,null,null,12,12,null,null,12,null,null,12,12,12,null,12,12,null,12,null,12,null,null,null,12,null,12,null,12,null,null,12,12,null,12,null,12,null,12,12,12,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,12,12,null,null,12,null,null,null,12,null,12,null,null,null,12,null,null,12,null,12,12,12,12,null,null,12,null,null,12,null,12,null,12,12,null,12,null,12,null,12,null,null,null,12,null,12,null,12,12,null,12,null,null,null,12,12,null,12,null,12,null,12,null,12,null,null,null,12,null,12,null,12,null,null,12,12,null,12,null,12,12,null,12,null,12,12,null,12,12,null,12,12,null,null,null,null,null,null,null,12,12,null,null,12,12,null,12,null,12,12,null,12,null,12,12,12,null,12,null,12,null,12,12,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,null,12,12,null,12,12,12,null,12,12,12,null,12,12,null,12,null,null,null,null,12,null,null,12,null,12,null,12,12,12,null,12,12,null,null,null,null,12,null,null,12,12,12,null,12,null,12,12,null,12,12,null,12,null,null,12,null,null,12,12,null,null,12,null,12,null,12,12,null,12,12,null,12,null,12,12,12,null,12,null,12,null,12,null,null,null,null,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,null,null,12,null,12,null,null,12,12,12,12,null,null,12,12,12,null,12,null,12,12,12,12,null,12,null,12,null,12,null,null,12,null,12,12,12,null,null,null,12,12,null,12,null,12,12,12,null,12,null,12,null,null,null,12,null,12,null,12,12,12,null,12,null,null,null,12,12,12,12,null,12,12,null,12,12,12,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,null,12,12,12,null,12,null,null,12,null,null,null,null,12,12,12,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,null,null,12,null,12,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,null,null,null,null,null,null,12,null,null,12,12,null,12,12,null,12,12,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,null,null,null,null,null,12,null,12,null,12,12,12,null,12,12,12,null,12,12,null,12,null,12,12,null,12,null,12,null,null,null,12,null,null,null,12,12,null,null,null,12,12,null,12,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,12,null,12,12,12,12,null,12,null,12,null,12,null,null,12,null,12,12,null,12,12,null,12,12,null,null,12,null,null,12,null,null,12,null,12,12,null,12,null,12,null,12,null,12,12,null,12,null,null,12,null,12,null,12,12,null,12,null,12,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,null,null,12,null,12,null,12,null,null,null,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,12,12,null,12,null,null,12,null,null,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,null,12,null,12,null,12,12,null,12,null,12,12,12,null,12,null,12,null,null,12,null,null,12,null,12,null,12,12,12,null,12,12,null,12,null,12,null,12,12,null,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,null,12,12,null,12,12,null,12,null,12,null,null,12,null,12,null,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,12,12,null,12,12,12,12,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,null,null,12,null,12,12,null,12,null,12,12,null,null,12,null,null,12,null,null,12,null,null,12,12,12,null,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,12,null,12,null,null,12,null,12,null,null,12,12,12,null,12,null,12,null,12,null,12,null,null,null,12,null,null,null,12,12,null,12,null,12,null,12,null,12,null,12,12,null,12,12,null,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,null,null,null,12,null,null,12,null,12,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,null,12,12,12,null,12,null,12,12,null,12,12,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,12,null,12,12,null,null,null,null,null,12,null,12,12,null,12,null,12,null,12,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,null,12,12,null,null,12,12,null,null,12,null,null,12,null,12,12,null,12,12,null,12,null,12,null,12,null,12,12,12,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,12,null,12,12,null,12,12,12,12,null,12,null,null,12,null,null,12,null,null,12,null,null,null,null,12,null,12,null,12,null,12,12,12,12,null,12,12,null,null,12,null,null,12,null,12,12,12,null,null,null,12,12,12,null,12,12,null,12,null,null,12,null,null,12,null,null,12,12,null,null,12,null,12,null,12,null,null,null,12,12,null,12,null,null,12,null,null,12,null,null,12,null,null,null,12,null,null,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,12,12,null,12,null,null,12,12,null,12,null,12,null,null,null,12,null,null,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,12,12,12,null,12,null,12,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,null,null,12,12,null,12,null,12,null,12,null,12,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,null,null,12,12,null,12,12,12,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,12,12,null,12,null,12,12,null,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,12,null,12,12,null,12,12,12,12,null,12,null,12,12,null,12,null,12,null,12,null,12,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,12,null,12,null,null,12,12,12,null,12,12,12,null,12,null,null,null,12,null,12,null,12,12,12,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,null,12,null,12,null,12,12,12,null,12,null,12,null,12,null,null,12,null,12,null,12,12,12,null,12,null,12,null,12,null,12,null,12,12,null,12,12,null,12,12,null,12,null,12,null,12,12,12,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,12,null,12,null,12,null,12,12,null,null,12,null,12,null,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,null,12,null,12,null,null,null,12,null,12,12,null,12,12,null,12,null,12,null,null,null,null,null,12,null,12,null,12,null,null,null,12,null,null,null,12,null,12,null,12,12,12,null,null,12,12,12,null,12,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,null,null,12,12,null,12,null,12,null,12,null,12,12,null,12,12,12,null,12,12,null,null,null,12,12,null,null,null,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,12,null,12,null,null,null,12,null,12,null,12,null,12,null,12,12,12,null,12,null,12,12,null,12,null,12,12,null,null,12,null,12,null,12,null,12,12,12,12,null,12,12,null,null,12,null,null,12,12,12,null,12,12,null,12,12,12,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,12,null,12,12,12,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,12,12,null,12,null,12,null,12,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,12,null,12,12,12,12,null,12,12,null,12,null,12,null,12,null,12,null,12,12,12,null,null,12,null,12,12,null,12,12,null,12,null,12,12,12,null,12,null,12,null,12,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,12,null,12,null,null,12,null,12,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,13,null,null,null,null,null,null,null,null,null,null,null,13,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null],"memalloc":[124.4993209838867,124.4993209838867,124.4993209838867,124.4993209838867,124.4993209838867,124.4993209838867,139.7815551757812,139.7815551757812,139.7815551757812,139.7815551757812,139.7815551757812,139.7815551757812,170.2472991943359,170.2472991943359,170.2472991943359,170.2472991943359,170.2472991943359,170.2472991943359,170.2472991943359,170.2472991943359,170.2472991943359,170.2472991943359,170.2472991943359,170.2472991943359,170.2473449707031,170.2473449707031,170.2473449707031,170.2473449707031,170.2473449707031,170.2473449707031,170.2473449707031,170.2473449707031,170.2473449707031,170.2473449707031,170.2473449707031,170.2473449707031,170.2473449707031,170.2473449707031,170.2473449707031,170.2473449707031,170.2473449707031,170.2473449707031,170.2470397949219,170.2470397949219,185.553840637207,185.553840637207,185.7584457397461,185.9605407714844,185.9605407714844,186.1605682373047,186.1605682373047,186.3615036010742,186.3615036010742,186.5805511474609,186.8063812255859,186.8063812255859,187.0427017211914,187.0427017211914,187.258415222168,187.258415222168,187.488410949707,187.488410949707,187.7177658081055,187.7177658081055,187.7177658081055,187.9415969848633,188.1666488647461,188.1666488647461,188.389533996582,188.6147766113281,188.6147766113281,188.7770919799805,188.7770919799805,185.6943893432617,185.6943893432617,185.9069061279297,185.9069061279297,186.1267166137695,186.3477401733398,186.3477401733398,186.607780456543,186.607780456543,186.8361053466797,187.0724182128906,187.0724182128906,187.3001708984375,187.527587890625,187.7646789550781,187.7646789550781,187.9937210083008,188.2172698974609,188.2172698974609,188.4477996826172,188.4477996826172,188.674919128418,188.84716796875,188.84716796875,188.84716796875,185.7923202514648,185.7923202514648,185.9974517822266,185.9974517822266,186.2173385620117,186.2173385620117,186.4414749145508,186.4414749145508,186.6814575195312,186.6814575195312,186.9136810302734,186.9136810302734,187.1483001708984,187.3781204223633,187.3781204223633,187.3781204223633,187.6280975341797,187.8624114990234,188.0875473022461,188.0875473022461,188.3188247680664,188.3188247680664,188.5506439208984,188.5506439208984,188.7756271362305,188.7756271362305,188.9345855712891,188.9345855712891,188.9345855712891,185.9324035644531,186.1351470947266,186.3584823608398,186.3584823608398,186.5837860107422,186.5837860107422,186.8276824951172,186.8276824951172,187.0595550537109,187.2925567626953,187.2925567626953,187.2925567626953,187.532112121582,187.7665405273438,187.7665405273438,188.0002288818359,188.0002288818359,188.2351913452148,188.2351913452148,188.4692611694336,188.4692611694336,188.7037734985352,188.9176177978516,188.9176177978516,189.020622253418,189.020622253418,189.020622253418,186.1399765014648,186.1399765014648,186.3676223754883,186.609260559082,186.8554382324219,186.8554382324219,187.0994644165039,187.0994644165039,187.3360748291016,187.3360748291016,187.5710067749023,187.5710067749023,187.8061294555664,187.8061294555664,188.0406188964844,188.2753448486328,188.2753448486328,188.5108184814453,188.7470703125,188.7470703125,188.982551574707,188.982551574707,189.1051788330078,189.1051788330078,189.1051788330078,186.2416381835938,186.4592895507812,186.4592895507812,186.6966705322266,186.6966705322266,186.9412994384766,186.9412994384766,186.9412994384766,187.1836547851562,187.1836547851562,187.4232940673828,187.4232940673828,187.6611328125,187.89111328125,187.89111328125,188.1199340820312,188.1199340820312,188.3498458862305,188.3498458862305,188.6077728271484,188.6077728271484,188.8437881469727,188.8437881469727,189.0796127319336,189.0796127319336,189.1884307861328,189.1884307861328,189.1884307861328,186.3724822998047,186.5890121459961,186.5890121459961,186.8218078613281,186.8218078613281,187.0681915283203,187.0681915283203,187.3092346191406,187.5503845214844,187.7776260375977,187.7776260375977,188.0120849609375,188.0120849609375,188.0120849609375,188.2470474243164,188.2470474243164,188.2470474243164,188.4828872680664,188.4828872680664,188.7149124145508,188.9507369995117,188.9507369995117,189.18603515625,189.18603515625,189.2702941894531,189.2702941894531,186.509162902832,186.7247161865234,186.7247161865234,186.9644317626953,186.9644317626953,187.1855697631836,187.4257354736328,187.4257354736328,187.6650695800781,187.6650695800781,187.9020309448242,188.1605072021484,188.3952941894531,188.3952941894531,188.6291351318359,188.8639373779297,188.8639373779297,189.0996170043945,189.0996170043945,189.0996170043945,189.3343811035156,189.3343811035156,189.3508834838867,189.3508834838867,189.3508834838867,186.7171325683594,186.7171325683594,186.943489074707,186.943489074707,187.1831970214844,187.1831970214844,187.1831970214844,187.4211959838867,187.6480484008789,187.6480484008789,187.8856735229492,188.1216888427734,188.3518600463867,188.3518600463867,188.5852508544922,188.5852508544922,188.5852508544922,188.7854461669922,189.0134124755859,189.0134124755859,189.1929016113281,189.1929016113281,189.427864074707,189.4301528930664,189.4301528930664,189.4301528930664,186.8002700805664,186.8002700805664,186.9967727661133,187.2133560180664,187.2133560180664,187.4472503662109,187.4472503662109,187.6879043579102,187.9238662719727,187.9238662719727,188.1595840454102,188.3919677734375,188.6235046386719,188.6235046386719,188.6235046386719,188.7889785766602,188.7889785766602,188.7889785766602,188.9653625488281,189.1437530517578,189.1437530517578,189.3302841186523,189.3302841186523,189.5080871582031,189.5080871582031,189.5080871582031,189.5080871582031,189.5080871582031,189.5080871582031,186.9879760742188,187.1992416381836,187.1992416381836,187.4266128540039,187.4266128540039,187.6635131835938,187.6635131835938,187.6635131835938,187.9004211425781,187.9004211425781,188.1376419067383,188.1376419067383,188.374382019043,188.374382019043,188.6090240478516,188.8426055908203,189.0787048339844,189.0787048339844,189.3121566772461,189.5093460083008,189.5093460083008,189.584846496582,189.584846496582,187.0239028930664,187.2418365478516,187.2418365478516,187.4983139038086,187.7328186035156,187.9666748046875,187.9666748046875,188.2015151977539,188.4373092651367,188.4373092651367,188.4373092651367,188.6686325073242,188.6686325073242,188.9031753540039,188.9031753540039,189.1586685180664,189.3579025268555,189.5954513549805,189.5954513549805,189.5954513549805,189.6603698730469,189.6603698730469,189.6603698730469,187.1206436157227,187.1206436157227,187.3253860473633,187.3253860473633,187.5514678955078,187.7858581542969,187.7858581542969,187.7858581542969,188.0205154418945,188.2561111450195,188.2561111450195,188.4894943237305,188.4894943237305,188.7220001220703,188.956787109375,188.956787109375,189.1905746459961,189.1905746459961,189.428466796875,189.428466796875,189.6682357788086,189.7345657348633,189.7345657348633,187.2516174316406,187.2516174316406,187.4639434814453,187.6935348510742,187.9300308227539,187.9300308227539,188.1640930175781,188.1640930175781,188.4252243041992,188.4252243041992,188.6588287353516,188.8912887573242,188.8912887573242,189.1260757446289,189.1260757446289,189.3620681762695,189.3620681762695,189.5965194702148,189.5965194702148,189.8076553344727,189.8076553344727,189.8076553344727,189.8076553344727,189.8076553344727,189.8076553344727,187.4435806274414,187.4435806274414,187.6615447998047,187.6615447998047,187.8922653198242,187.8922653198242,188.1268463134766,188.1268463134766,188.3619918823242,188.3619918823242,188.5994186401367,188.5994186401367,188.8334884643555,188.8334884643555,189.0693740844727,189.0693740844727,189.3034362792969,189.3034362792969,189.3034362792969,189.5398178100586,189.5398178100586,189.5398178100586,189.7766723632812,189.879524230957,189.879524230957,189.879524230957,187.4471817016602,187.6478881835938,187.6478881835938,187.8714141845703,188.0979537963867,188.0979537963867,188.3336563110352,188.3336563110352,188.3336563110352,188.5949249267578,188.5949249267578,188.5949249267578,188.8244247436523,188.8244247436523,189.0590515136719,189.0590515136719,189.2933654785156,189.2933654785156,189.5258483886719,189.5258483886719,189.7600860595703,189.7600860595703,189.9502792358398,189.9502792358398,189.9502792358398,189.9502792358398,189.9502792358398,189.9502792358398,187.6783905029297,187.6783905029297,187.8912963867188,188.0728378295898,188.0728378295898,188.2054977416992,188.2054977416992,188.4013290405273,188.5729446411133,188.5729446411133,188.7759704589844,188.9837493896484,188.9837493896484,189.1505813598633,189.3744125366211,189.5597152709961,189.7468795776367,189.7468795776367,189.9476928710938,190.0197906494141,190.0197906494141,190.0197906494141,190.0197906494141,190.0197906494141,190.0197906494141,187.7712707519531,187.7712707519531,187.9351654052734,187.9351654052734,188.1094665527344,188.2559356689453,188.2559356689453,188.4587707519531,188.6302795410156,188.8167419433594,188.8167419433594,189.0191345214844,189.0191345214844,189.1857681274414,189.4086456298828,189.4086456298828,189.6369857788086,189.6369857788086,189.8434524536133,190.0619888305664,190.0882873535156,190.0882873535156,190.0882873535156,187.7748718261719,187.9565124511719,187.9565124511719,188.1269149780273,188.1269149780273,188.3129425048828,188.3129425048828,188.4834671020508,188.4834671020508,188.4834671020508,188.6781158447266,188.8814926147461,189.0802764892578,189.0802764892578,189.294059753418,189.4969940185547,189.4969940185547,189.7162933349609,189.9645233154297,189.9645233154297,190.1239700317383,190.1239700317383,190.1556243896484,190.1556243896484,190.1556243896484,190.1556243896484,188.0192947387695,188.2033157348633,188.3764343261719,188.3764343261719,188.5756149291992,188.5756149291992,188.7914657592773,188.7914657592773,188.7914657592773,189.0207977294922,189.0207977294922,189.2552185058594,189.2552185058594,189.4891967773438,189.7244415283203,189.7244415283203,189.9578552246094,189.9578552246094,189.9578552246094,190.1912078857422,190.1912078857422,190.2219314575195,190.2219314575195,190.2219314575195,188.0201187133789,188.0201187133789,188.2129669189453,188.2129669189453,188.4342498779297,188.4342498779297,188.6521682739258,188.8842163085938,189.1215667724609,189.3574752807617,189.5950698852539,189.8308639526367,189.8308639526367,189.8308639526367,190.0684356689453,190.2870941162109,190.2870941162109,190.2870941162109,190.2870941162109,190.2870941162109,190.2870941162109,190.2870941162109,190.2870941162109,190.2870941162109,190.2870941162109,190.2870941162109,190.2870941162109,190.2870941162109,190.2870941162109,190.2870941162109,190.2870941162109,190.2870941162109,190.2870941162109,190.2870941162109,190.2870941162109,190.2870941162109,190.2870941162109,190.2870941162109,190.2870941162109,190.2870941162109,190.2870941162109,190.2870941162109,190.2870941162109,190.2870941162109,190.2870941162109,190.2870941162109,190.2870941162109,190.2870941162109,190.2870941162109,190.2870941162109,190.2870941162109,188.0545806884766,188.0545806884766,188.2107009887695,188.2107009887695,188.3820190429688,188.5630416870117,188.5630416870117,188.7535018920898,188.9566497802734,188.9566497802734,189.1709594726562,189.3985443115234,189.3985443115234,189.6282501220703,189.8496551513672,189.8496551513672,189.8496551513672,190.0759963989258,190.3016586303711,190.3016586303711,190.3510360717773,190.3510360717773,188.1911773681641,188.1911773681641,188.3785629272461,188.3785629272461,188.5711135864258,188.5711135864258,188.7772445678711,189.0216827392578,189.0216827392578,189.2557907104492,189.2557907104492,189.4888687133789,189.721305847168,189.9538345336914,189.9538345336914,190.1856155395508,190.1856155395508,190.4142608642578,190.4142608642578,190.4142608642578,190.4142608642578,188.3305969238281,188.5190811157227,188.5190811157227,188.5190811157227,188.7164688110352,188.9342956542969,188.9342956542969,189.1649856567383,189.1649856567383,189.4013671875,189.4013671875,189.6382598876953,189.6382598876953,189.8725738525391,189.8725738525391,190.1022720336914,190.1022720336914,190.334358215332,190.4763336181641,190.4763336181641,190.4763336181641,190.4763336181641,190.4763336181641,190.4763336181641,188.4892272949219,188.4892272949219,188.6715850830078,188.6715850830078,188.8640823364258,188.8640823364258,189.0653305053711,189.0653305053711,189.2848739624023,189.2848739624023,189.5149536132812,189.7455825805664,189.9738311767578,190.2024688720703,190.433723449707,190.433723449707,190.5374603271484,190.5374603271484,190.5374603271484,190.5374603271484,188.58935546875,188.58935546875,188.58935546875,188.7699203491211,188.7699203491211,188.9688873291016,188.9688873291016,189.1829833984375,189.1829833984375,189.1829833984375,189.4137725830078,189.6055145263672,189.6055145263672,189.8336410522461,189.8336410522461,189.8336410522461,190.0426635742188,190.0426635742188,190.2861709594727,190.2861709594727,190.5179748535156,190.59765625,190.59765625,190.59765625,190.59765625,190.59765625,190.59765625,188.7070999145508,188.8774490356445,188.8774490356445,189.0747146606445,189.0747146606445,189.2666168212891,189.2666168212891,189.4782409667969,189.4782409667969,189.6963577270508,189.6963577270508,189.9136734008789,190.1442413330078,190.3593826293945,190.5783615112305,190.5783615112305,190.6567611694336,190.6567611694336,190.6567611694336,188.6289443969727,188.6289443969727,188.8138275146484,188.8138275146484,189.0072631835938,189.0072631835938,189.1939086914062,189.1939086914062,189.4169540405273,189.4169540405273,189.6399688720703,189.6399688720703,189.8769912719727,190.1023025512695,190.3183746337891,190.3183746337891,190.5514068603516,190.5514068603516,190.7149658203125,190.7149658203125,190.7149658203125,190.7149658203125,190.7149658203125,190.7149658203125,190.7149658203125,190.7149658203125,188.8242034912109,188.8242034912109,188.9903793334961,189.1778106689453,189.1778106689453,189.1778106689453,189.3825836181641,189.3825836181641,189.606201171875,189.8374633789062,189.8374633789062,190.0693969726562,190.0693969726562,190.3031921386719,190.5349349975586,190.5349349975586,190.7661972045898,190.7661972045898,190.7722091674805,190.7722091674805,190.7722091674805,188.8982009887695,188.8982009887695,189.08251953125,189.2784729003906,189.2784729003906,189.4933090209961,189.7222595214844,189.7222595214844,189.7222595214844,189.9556884765625,190.1909484863281,190.1909484863281,190.4237899780273,190.4237899780273,190.6576995849609,190.6576995849609,190.8285598754883,190.8285598754883,190.8285598754883,190.8285598754883,189.0084686279297,189.1844635009766,189.377311706543,189.5922241210938,189.5922241210938,189.8205871582031,190.0561828613281,190.0561828613281,190.0561828613281,190.2862777709961,190.2862777709961,190.5368576049805,190.7454299926758,190.7454299926758,190.8839492797852,190.8839492797852,190.8839492797852,190.8839492797852,189.0824127197266,189.0824127197266,189.2515411376953,189.2515411376953,189.2515411376953,189.4377517700195,189.6298980712891,189.8519821166992,189.8519821166992,190.0731506347656,190.2969970703125,190.2969970703125,190.5200424194336,190.5200424194336,190.6917037963867,190.922233581543,190.922233581543,190.9385452270508,190.9385452270508,190.9385452270508,189.0959014892578,189.282356262207,189.282356262207,189.4539566040039,189.4539566040039,189.6434783935547,189.6434783935547,189.8360137939453,189.8360137939453,190.0530319213867,190.2699203491211,190.4873504638672,190.4873504638672,190.7177963256836,190.7177963256836,190.9374313354492,190.9374313354492,190.9921951293945,190.9921951293945,190.9921951293945,189.1703720092773,189.1703720092773,189.3487319946289,189.5349807739258,189.5349807739258,189.5349807739258,189.7170028686523,189.9118804931641,189.9118804931641,190.1065521240234,190.3188323974609,190.3188323974609,190.3188323974609,190.5505065917969,190.7724304199219,190.7724304199219,190.9966735839844,190.9966735839844,191.0449447631836,191.0449447631836,191.0449447631836,189.2522430419922,189.2522430419922,189.4316482543945,189.6132736206055,189.8062438964844,189.8062438964844,189.8062438964844,190.0153884887695,190.2398910522461,190.2398910522461,190.4790191650391,190.4790191650391,190.4790191650391,190.7097625732422,190.7097625732422,190.9388122558594,191.0968704223633,191.0968704223633,191.0968704223633,191.0968704223633,191.0968704223633,191.0968704223633,191.0968704223633,191.0968704223633,189.4444274902344,189.4444274902344,189.6248397827148,189.6248397827148,189.8124008178711,189.8124008178711,190.0189361572266,190.0189361572266,190.2408065795898,190.2408065795898,190.4971771240234,190.7313690185547,190.7313690185547,190.9649276733398,191.1479721069336,191.1479721069336,191.1479721069336,191.1479721069336,191.1479721069336,191.1479721069336,189.4952850341797,189.4952850341797,189.6745071411133,189.6745071411133,189.8562469482422,189.8562469482422,190.0258712768555,190.2191925048828,190.4362030029297,190.4362030029297,190.4362030029297,190.6546478271484,190.6546478271484,190.8921356201172,191.1235198974609,191.1235198974609,191.1982421875,191.1982421875,189.4763107299805,189.4763107299805,189.6523361206055,189.6523361206055,189.8374176025391,189.8374176025391,190.0255279541016,190.0255279541016,190.2516174316406,190.4777526855469,190.4777526855469,190.4777526855469,190.7062530517578,190.93994140625,190.93994140625,191.1725997924805,191.1725997924805,191.2477111816406,191.2477111816406,191.2477111816406,191.2477111816406,191.2477111816406,191.2477111816406,189.7140579223633,189.7140579223633,189.8955688476562,190.0833282470703,190.2868804931641,190.5142822265625,190.5142822265625,190.7369766235352,190.9699630737305,190.9699630737305,190.9699630737305,191.2051162719727,191.2051162719727,191.2963562011719,191.2963562011719,191.2963562011719,191.2963562011719,191.2963562011719,191.2963562011719,191.2963562011719,191.2963562011719,189.7847595214844,189.9659194946289,190.1632995605469,190.1632995605469,190.3870239257812,190.3870239257812,190.3870239257812,190.6055221557617,190.6055221557617,190.8093872070312,190.8093872070312,190.8093872070312,191.0378494262695,191.0378494262695,191.2518005371094,191.2518005371094,191.3442535400391,191.3442535400391,191.3442535400391,191.3442535400391,191.3442535400391,191.3442535400391,191.3442535400391,191.3442535400391,189.8463745117188,189.8463745117188,190.0276794433594,190.0276794433594,190.2010345458984,190.2010345458984,190.3875885009766,190.3875885009766,190.6050109863281,190.6050109863281,190.8149871826172,190.8149871826172,191.0351028442383,191.0351028442383,191.2592926025391,191.2592926025391,191.3913192749023,191.3913192749023,191.3913192749023,191.3913192749023,189.9371719360352,190.1170349121094,190.31591796875,190.5331573486328,190.5331573486328,190.7628021240234,190.7628021240234,191.0003967285156,191.0003967285156,191.2367477416992,191.2367477416992,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,191.4376831054688,189.8422775268555,189.8422775268555,189.8422775268555,189.8422775268555,189.8422775268555,189.8422775268555,189.9607467651367,189.9607467651367,190.1277618408203,190.2877960205078,190.4864349365234,190.689811706543,190.689811706543,190.8642349243164,190.8642349243164,191.0497817993164,191.0497817993164,191.2757568359375,191.2757568359375,191.4901733398438,191.4901733398438,191.6716003417969,191.6716003417969,191.8223342895508,191.8223342895508,191.9913864135742,192.1756973266602,192.3721694946289,192.5754776000977,192.7620544433594,192.7620544433594,192.9478607177734,192.9478607177734,193.1247329711914,193.1247329711914,193.311637878418,193.311637878418,193.4909896850586,193.4909896850586,193.6720962524414,193.8594589233398,193.8594589233398,194.0384216308594,194.0384216308594,194.2258453369141,194.2258453369141,194.4234390258789,194.4234390258789,194.4234390258789,194.6045227050781,194.6045227050781,194.6996307373047,194.6996307373047,194.6996307373047,194.6996307373047,194.6996307373047,194.6996307373047,190.1817016601562,190.38818359375,190.38818359375,190.6077041625977,190.6077041625977,190.8345794677734,190.8345794677734,191.0641708374023,191.0641708374023,191.286979675293,191.286979675293,191.5102005004883,191.5102005004883,191.7538986206055,191.7538986206055,191.9966506958008,192.2380828857422,192.2380828857422,192.4767761230469,192.7165145874023,192.954216003418,192.954216003418,193.1919937133789,193.4289932250977,193.4289932250977,193.6665878295898,193.9038314819336,194.140266418457,194.3770904541016,194.6059875488281,194.8324661254883,194.8324661254883,194.8324661254883,194.8324661254883,194.8324661254883,194.8324661254883,190.305793762207,190.305793762207,190.5093460083008,190.5093460083008,190.7253570556641,190.7253570556641,190.9625549316406,191.1979370117188,191.1979370117188,191.4199066162109,191.4199066162109,191.6500015258789,191.6500015258789,191.8942718505859,192.1374359130859,192.1374359130859,192.3799209594727,192.3799209594727,192.616340637207,192.616340637207,192.8368301391602,193.0746994018555,193.3113479614258,193.3113479614258,193.5390090942383,193.5390090942383,193.760986328125,193.9892120361328,194.2101364135742,194.2101364135742,194.4297332763672,194.6632232666016,194.6632232666016,194.8787231445312,194.8787231445312,194.8787231445312,194.9631729125977,194.9631729125977,194.9631729125977,194.9631729125977,190.6154708862305,190.6154708862305,190.8162689208984,190.8162689208984,191.0185470581055,191.0185470581055,191.2356109619141,191.2356109619141,191.2356109619141,191.4490280151367,191.4490280151367,191.6491851806641,191.6491851806641,191.8918914794922,191.8918914794922,191.8918914794922,192.1233901977539,192.3577575683594,192.3577575683594,192.5944747924805,192.5944747924805,192.8191528320312,193.0565032958984,193.2834091186523,193.2834091186523,193.5118637084961,193.5118637084961,193.7452850341797,193.7452850341797,193.7452850341797,193.9786987304688,194.1969223022461,194.4250564575195,194.4250564575195,194.6570434570312,194.6570434570312,194.8849639892578,194.8849639892578,195.0918502807617,195.0918502807617,195.0918502807617,195.0918502807617,190.6742324829102,190.6742324829102,190.8871078491211,190.8871078491211,191.0894775390625,191.2868347167969,191.2868347167969,191.4861831665039,191.4861831665039,191.6848678588867,191.8814010620117,192.1063079833984,192.1063079833984,192.3160247802734,192.3160247802734,192.5288543701172,192.5288543701172,192.751838684082,192.9561767578125,192.9561767578125,193.1753082275391,193.1753082275391,193.3801498413086,193.5931015014648,193.5931015014648,193.8108673095703,193.8108673095703,193.9947967529297,193.9947967529297,193.9947967529297,194.2148742675781,194.2148742675781,194.3927459716797,194.596321105957,194.596321105957,194.7997131347656,194.7997131347656,194.9902420043945,195.1976776123047,195.1976776123047,195.2183609008789,195.2183609008789,195.2183609008789,195.2183609008789,190.9843521118164,190.9843521118164,191.1594924926758,191.1594924926758,191.357307434082,191.5039520263672,191.5039520263672,191.6794128417969,191.6794128417969,191.8603515625,191.8603515625,191.8603515625,192.0553512573242,192.275749206543,192.4729843139648,192.6866455078125,192.9037628173828,192.9037628173828,193.1186676025391,193.3486099243164,193.3486099243164,193.5500030517578,193.5500030517578,193.7591781616211,193.7591781616211,193.7591781616211,193.9786911010742,193.9786911010742,194.1908416748047,194.1908416748047,194.3356170654297,194.3356170654297,194.5396728515625,194.7274322509766,194.9714126586914,195.1098098754883,195.1098098754883,195.2866973876953,195.2866973876953,195.3428421020508,195.3428421020508,195.3428421020508,195.3428421020508,195.3428421020508,195.3428421020508,191.1460189819336,191.3435287475586,191.5417633056641,191.7421035766602,191.9426040649414,191.9426040649414,192.1754608154297,192.1754608154297,192.4155731201172,192.4155731201172,192.654052734375,192.8912734985352,192.8912734985352,193.1283645629883,193.3628616333008,193.595588684082,193.8284606933594,193.8284606933594,194.0615005493164,194.0615005493164,194.2838287353516,194.2838287353516,194.2838287353516,194.5396957397461,194.5396957397461,194.7720031738281,194.7720031738281,195.0041580200195,195.0041580200195,195.2310943603516,195.4540863037109,195.4540863037109,195.4653472900391,195.4653472900391,195.4653472900391,195.4653472900391,195.4653472900391,195.4653472900391,191.4451217651367,191.4451217651367,191.4451217651367,191.644157409668,191.8413238525391,191.8413238525391,192.0366439819336,192.0366439819336,192.2597274780273,192.2597274780273,192.5009384155273,192.7421646118164,192.9817428588867,193.2191619873047,193.2191619873047,193.4548263549805,193.4548263549805,193.6883850097656,193.6883850097656,193.9227142333984,194.1590347290039,194.1590347290039,194.3922882080078,194.3922882080078,194.6240234375,194.6240234375,194.8562316894531,194.8562316894531,195.0909194946289,195.343376159668,195.565299987793,195.565299987793,195.565299987793,195.5858459472656,195.5858459472656,195.5858459472656,195.5858459472656,195.5858459472656,195.5858459472656,195.5858459472656,195.5858459472656,191.6056594848633,191.6056594848633,191.8012619018555,191.8012619018555,191.9943389892578,192.1943817138672,192.4263153076172,192.4263153076172,192.4263153076172,192.6649932861328,192.6649932861328,192.904655456543,192.904655456543,193.1418991088867,193.1418991088867,193.3784484863281,193.3784484863281,193.6139373779297,193.6139373779297,193.8480682373047,193.8480682373047,194.0813980102539,194.0813980102539,194.3165435791016,194.3165435791016,194.3165435791016,194.5519027709961,194.7872161865234,195.0242691040039,195.0242691040039,195.2615280151367,195.4915390014648,195.4915390014648,195.7043838500977,195.7043838500977,195.7043838500977,195.7043838500977,195.7043838500977,195.7043838500977,191.6512832641602,191.6512832641602,191.6512832641602,191.8476638793945,191.8476638793945,192.0398178100586,192.0398178100586,192.2307434082031,192.4411315917969,192.4411315917969,192.6697082519531,192.6697082519531,192.9084243774414,193.1489868164062,193.1489868164062,193.3878860473633,193.6260528564453,193.6260528564453,193.8616180419922,194.0951156616211,194.0951156616211,194.3307647705078,194.5667877197266,194.5667877197266,194.7991256713867,194.7991256713867,195.0090484619141,195.2420425415039,195.2420425415039,195.4776992797852,195.4776992797852,195.6840667724609,195.6840667724609,195.8209838867188,195.8209838867188,195.8209838867188,195.8209838867188,195.8209838867188,195.8209838867188,191.9685821533203,191.9685821533203,192.1516189575195,192.1516189575195,192.3220367431641,192.5121841430664,192.6884918212891,192.8730316162109,193.0853576660156,193.2832260131836,193.5087127685547,193.5087127685547,193.7157974243164,193.7157974243164,193.7157974243164,193.9248352050781,194.154182434082,194.3599472045898,194.3599472045898,194.5873794555664,194.5873794555664,194.7905960083008,194.7905960083008,194.7905960083008,195.0208053588867,195.0208053588867,195.2494735717773,195.2494735717773,195.4538650512695,195.6816864013672,195.6816864013672,195.8795700073242,195.9357452392578,195.9357452392578,195.9357452392578,195.9357452392578,195.9357452392578,195.9357452392578,192.0615158081055,192.0615158081055,192.2468719482422,192.4194869995117,192.4194869995117,192.5730056762695,192.5730056762695,192.7769393920898,192.7769393920898,192.949577331543,192.949577331543,193.1531982421875,193.3816528320312,193.3816528320312,193.5895385742188,193.5895385742188,193.8190994262695,193.8190994262695,193.8190994262695,194.0189971923828,194.0189971923828,194.2353057861328,194.2353057861328,194.4604949951172,194.6539993286133,194.6539993286133,194.8792877197266,195.1041412353516,195.2716522216797,195.2716522216797,195.4455795288086,195.4455795288086,195.4455795288086,195.6387634277344,195.6387634277344,195.8665161132812,195.8665161132812,196.0486755371094,196.0486755371094,196.0486755371094,196.0486755371094,196.0486755371094,196.0486755371094,192.1762924194336,192.3625717163086,192.3625717163086,192.5487670898438,192.5487670898438,192.7375640869141,192.7375640869141,192.9494094848633,192.9494094848633,193.1757278442383,193.4121475219727,193.4121475219727,193.6497039794922,193.6497039794922,193.8876495361328,193.8876495361328,194.1257705688477,194.1257705688477,194.3627166748047,194.5974578857422,194.5974578857422,194.8323974609375,194.8323974609375,195.0679626464844,195.3037948608398,195.3037948608398,195.5392379760742,195.5392379760742,195.7759323120117,196.0039443969727,196.1597137451172,196.1597137451172,196.1597137451172,196.1597137451172,196.1597137451172,196.1597137451172,192.3965225219727,192.5841751098633,192.7663192749023,192.7663192749023,192.9695205688477,193.1905517578125,193.1905517578125,193.4218978881836,193.4218978881836,193.6596374511719,193.6596374511719,193.8994750976562,193.8994750976562,194.1376190185547,194.1376190185547,194.3778228759766,194.3778228759766,194.6145706176758,194.6145706176758,194.6145706176758,194.8483505249023,195.0706558227539,195.0706558227539,195.3187408447266,195.3187408447266,195.5538787841797,195.5538787841797,195.7776870727539,196.0122756958008,196.2424545288086,196.2424545288086,196.2689819335938,196.2689819335938,196.2689819335938,196.2689819335938,196.2689819335938,196.2689819335938,192.6619033813477,192.6619033813477,192.8465042114258,192.8465042114258,193.0351486206055,193.0351486206055,193.2528915405273,193.2528915405273,193.4927215576172,193.7260437011719,193.9514846801758,193.9514846801758,193.9514846801758,194.1901397705078,194.1901397705078,194.4167098999023,194.4167098999023,194.6563491821289,194.6563491821289,194.8964462280273,194.8964462280273,195.1368026733398,195.1368026733398,195.3526611328125,195.3526611328125,195.3526611328125,195.5976257324219,195.5976257324219,195.8349151611328,196.0609283447266,196.2875747680664,196.3765563964844,196.3765563964844,196.3765563964844,196.3765563964844,196.3765563964844,196.3765563964844,192.7629852294922,192.7629852294922,192.9482803344727,192.9482803344727,193.1272506713867,193.3376617431641,193.3376617431641,193.5644073486328,193.5644073486328,193.802848815918,193.802848815918,194.0164184570312,194.0164184570312,194.2635040283203,194.2635040283203,194.5003509521484,194.5003509521484,194.726188659668,194.726188659668,194.9600448608398,195.2063522338867,195.2063522338867,195.4418029785156,195.4418029785156,195.6669158935547,195.6669158935547,195.9033508300781,196.1257858276367,196.1257858276367,196.3568878173828,196.3568878173828,196.4822998046875,196.4822998046875,196.4822998046875,196.4822998046875,192.916633605957,192.916633605957,193.0915603637695,193.0915603637695,193.2786026000977,193.2786026000977,193.4642944335938,193.4642944335938,193.6792297363281,193.6792297363281,193.9151229858398,194.1489639282227,194.3746490478516,194.3746490478516,194.6125717163086,194.6125717163086,194.8525161743164,195.0727081298828,195.0727081298828,195.3087005615234,195.3087005615234,195.5521392822266,195.7879104614258,195.7879104614258,196.0165557861328,196.251708984375,196.251708984375,196.4681777954102,196.5863800048828,196.5863800048828,196.5863800048828,196.5863800048828,196.5863800048828,196.5863800048828,193.0807723999023,193.0807723999023,193.2551956176758,193.4465026855469,193.4465026855469,193.6535949707031,193.8598861694336,194.0836334228516,194.0836334228516,194.3313903808594,194.3313903808594,194.5706329345703,194.7969970703125,194.7969970703125,195.0373992919922,195.0373992919922,195.2839431762695,195.4945220947266,195.7389450073242,195.7389450073242,195.9777603149414,195.9777603149414,196.1979293823242,196.1979293823242,196.4364929199219,196.6631927490234,196.6888046264648,196.6888046264648,196.6888046264648,196.6888046264648,193.3081130981445,193.3081130981445,193.4892730712891,193.4892730712891,193.6708526611328,193.6708526611328,193.8742752075195,194.0782775878906,194.0782775878906,194.3032608032227,194.3032608032227,194.3032608032227,194.524055480957,194.7671966552734,194.7671966552734,195.0060195922852,195.2226257324219,195.4382858276367,195.4382858276367,195.648567199707,195.8665084838867,196.0845108032227,196.0845108032227,196.3237991333008,196.5481185913086,196.5481185913086,196.7731018066406,196.7731018066406,196.7895736694336,196.7895736694336,196.7895736694336,196.7895736694336,196.7895736694336,196.7895736694336,193.4582595825195,193.4582595825195,193.6284866333008,193.6284866333008,193.8157043457031,194.0104827880859,194.1777114868164,194.1777114868164,194.3765258789062,194.5746765136719,194.5746765136719,194.7766342163086,194.7766342163086,194.7766342163086,195.0045776367188,195.0045776367188,195.0045776367188,195.2489929199219,195.4932556152344,195.7087554931641,195.7087554931641,195.9505615234375,195.9505615234375,196.1876831054688,196.4132766723633,196.4132766723633,196.6481323242188,196.8813247680664,196.8813247680664,196.8886566162109,196.8886566162109,196.8886566162109,196.8886566162109,196.8886566162109,196.8886566162109,193.5967559814453,193.7702713012695,193.7702713012695,193.7702713012695,193.9578170776367,193.9578170776367,194.1575622558594,194.1575622558594,194.3742980957031,194.6000595092773,194.6000595092773,194.8258972167969,195.065071105957,195.065071105957,195.2914352416992,195.2914352416992,195.5317306518555,195.77978515625,196.0168762207031,196.0168762207031,196.2423400878906,196.2423400878906,196.4798049926758,196.4798049926758,196.7201919555664,196.7201919555664,196.9298706054688,196.9298706054688,196.986198425293,196.986198425293,196.986198425293,196.986198425293,196.986198425293,196.986198425293,196.986198425293,196.986198425293,196.986198425293,196.986198425293,196.986198425293,196.986198425293,196.986198425293,196.986198425293,196.986198425293,196.986198425293,196.986198425293,196.986198425293,196.986198425293,196.986198425293,196.986198425293,196.986198425293,196.986198425293,196.986198425293,196.986198425293,196.986198425293,196.986198425293,196.986198425293,196.986198425293,196.986198425293,196.986198425293,196.986198425293,196.986198425293,196.986198425293,196.986198425293,196.986198425293,196.986198425293,196.986198425293,196.986198425293,196.986198425293,196.986198425293,196.986198425293,196.986198425293,196.986198425293,196.986198425293,196.986198425293,196.986198425293,196.986198425293,193.6294784545898,193.6294784545898,193.6294784545898,193.7316436767578,193.7316436767578,193.9000701904297,193.9000701904297,193.9000701904297,194.0883331298828,194.0883331298828,194.2533111572266,194.2533111572266,194.2533111572266,194.4563064575195,194.6651916503906,194.883659362793,195.1171951293945,195.1171951293945,195.3504257202148,195.5764389038086,195.8039627075195,196.0333099365234,196.0333099365234,196.252326965332,196.252326965332,196.4856567382812,196.7093124389648,196.9395904541016,197.0818481445312,197.0818481445312,197.0818481445312,197.0818481445312,193.8157119750977,193.8157119750977,193.9843292236328,193.9843292236328,193.9843292236328,194.1677474975586,194.1677474975586,194.3650894165039,194.5453796386719,194.7720565795898,194.7720565795898,195.0010375976562,195.0010375976562,195.2239379882812,195.460075378418,195.460075378418,195.6987075805664,195.6987075805664,195.9409332275391,196.1562652587891,196.4037704467773,196.4037704467773,196.6399612426758,196.6399612426758,196.864616394043,196.864616394043,197.0990219116211,197.0990219116211,197.1763076782227,197.1763076782227,197.1763076782227,197.1763076782227,194.0184020996094,194.199089050293,194.3816909790039,194.3816909790039,194.5722808837891,194.5722808837891,194.775146484375,194.775146484375,194.9935760498047,195.2275543212891,195.4600830078125,195.6928558349609,195.6928558349609,195.9253540039062,196.1577224731445,196.1577224731445,196.3913192749023,196.6274337768555,196.8649826049805,197.1008911132812,197.1008911132812,197.1008911132812,197.2692108154297,197.2692108154297,197.2692108154297,197.2692108154297,197.2692108154297,197.2692108154297,197.2692108154297,197.2692108154297,197.2692108154297,194.218132019043,194.218132019043,194.3976058959961,194.3976058959961,194.5820999145508,194.7668838500977,194.9643936157227,194.9643936157227,195.1793746948242,195.1793746948242,195.1793746948242,195.4081954956055,195.4081954956055,195.6422882080078,195.6422882080078,195.8770446777344,196.1072692871094,196.3399505615234,196.5732879638672,196.8083648681641,197.0450820922852,197.0450820922852,197.2708511352539,197.2708511352539,197.360595703125,197.360595703125,197.360595703125,197.360595703125,194.2934875488281,194.2934875488281,194.4684829711914,194.4684829711914,194.6444473266602,194.6444473266602,194.8313598632812,194.8313598632812,194.8313598632812,195.015625,195.015625,195.2065124511719,195.2065124511719,195.2065124511719,195.4128494262695,195.4128494262695,195.6390380859375,195.8692779541016,195.8692779541016,196.1007308959961,196.1007308959961,196.3322372436523,196.5664901733398,196.5664901733398,196.7682266235352,196.7682266235352,197.0026779174805,197.0026779174805,197.2062149047852,197.2062149047852,197.4413909912109,197.4413909912109,197.4505310058594,197.4505310058594,197.4505310058594,197.4505310058594,197.4505310058594,197.4505310058594,194.4787063598633,194.4787063598633,194.6536331176758,194.6536331176758,194.6536331176758,194.8366851806641,195.0247268676758,195.0247268676758,195.217399597168,195.4272842407227,195.4272842407227,195.6493148803711,195.87744140625,196.1109390258789,196.1109390258789,196.3402862548828,196.3402862548828,196.5645294189453,196.5645294189453,196.7868576049805,196.7868576049805,197.0220642089844,197.0220642089844,197.253044128418,197.4863052368164,197.4863052368164,197.5389938354492,197.5389938354492,197.5389938354492,197.5389938354492,197.5389938354492,197.5389938354492,194.5583953857422,194.7318725585938,194.7318725585938,194.9291229248047,194.9291229248047,195.1153793334961,195.3073883056641,195.5123901367188,195.5123901367188,195.7323303222656,195.9468688964844,196.1713180541992,196.1713180541992,196.3954544067383,196.6269073486328,196.6269073486328,196.8607635498047,196.8607635498047,197.0789947509766,197.3150787353516,197.3150787353516,197.5463485717773,197.5463485717773,197.6260375976562,197.6260375976562,197.6260375976562,197.6260375976562,197.6260375976562,197.6260375976562,197.6260375976562,197.6260375976562,194.684455871582,194.84619140625,194.84619140625,195.0263900756836,195.0263900756836,195.2128143310547,195.4038391113281,195.4038391113281,195.602424621582,195.831184387207,195.831184387207,196.0464859008789,196.0464859008789,196.2707061767578,196.2707061767578,196.4903869628906,196.7155838012695,196.7155838012695,196.9468383789062,196.9468383789062,197.1842880249023,197.1842880249023,197.3833999633789,197.3833999633789,197.6166534423828,197.6166534423828,197.7117004394531,197.7117004394531,197.7117004394531,197.7117004394531,197.7117004394531,197.7117004394531,194.7858581542969,194.7858581542969,194.9501113891602,194.9501113891602,195.1176986694336,195.2971343994141,195.4574127197266,195.6455230712891,195.6455230712891,195.8272476196289,195.8272476196289,196.0378341674805,196.0378341674805,196.2577133178711,196.2577133178711,196.2577133178711,196.4770355224609,196.4770355224609,196.7004852294922,196.9264907836914,196.9264907836914,197.1300506591797,197.3507919311523,197.3507919311523,197.5766448974609,197.7959289550781,197.7959289550781,197.7959289550781,197.7959289550781,197.7959289550781,197.7959289550781,197.7959289550781,197.7959289550781,197.7959289550781,195.0003433227539,195.0003433227539,195.1514434814453,195.3277435302734,195.3277435302734,195.511100769043,195.511100769043,195.6989212036133,195.6989212036133,195.9024276733398,195.9024276733398,196.0873336791992,196.2919845581055,196.2919845581055,196.4648361206055,196.4648361206055,196.4648361206055,196.6613922119141,196.6613922119141,196.8624572753906,196.8624572753906,197.0605545043945,197.2665634155273,197.2665634155273,197.4722747802734,197.4722747802734,197.6753158569336,197.8788223266602,197.8788223266602,197.8788223266602,197.8788223266602,197.8788223266602,197.8788223266602,197.8788223266602,197.8788223266602,197.8788223266602,197.8788223266602,197.8788223266602,197.8788223266602,195.1602096557617,195.1602096557617,195.3277740478516,195.3277740478516,195.4829406738281,195.4829406738281,195.6632843017578,195.6632843017578,195.8372344970703,195.8372344970703,196.0249557495117,196.0249557495117,196.2195434570312,196.2195434570312,196.4029159545898,196.4029159545898,196.6031494140625,196.6031494140625,196.793586730957,196.793586730957,196.9974975585938,197.1915054321289,197.1915054321289,197.3834762573242,197.3834762573242,197.5937652587891,197.7876205444336,197.7876205444336,197.9604415893555,197.9604415893555,197.9604415893555,197.9604415893555,197.9604415893555,197.9604415893555,195.220458984375,195.3663711547852,195.5158081054688,195.5158081054688,195.6911163330078,195.6911163330078,195.6911163330078,195.8470993041992,195.8470993041992,196.0257568359375,196.0257568359375,196.20068359375,196.20068359375,196.3796539306641,196.3796539306641,196.6052093505859,196.6052093505859,196.781494140625,196.998405456543,196.998405456543,197.1900177001953,197.1900177001953,197.3842926025391,197.3842926025391,197.5979843139648,197.5979843139648,197.7780990600586,197.9780807495117,197.9780807495117,198.0406036376953,198.0406036376953,198.0406036376953,198.0406036376953,195.281135559082,195.281135559082,195.4127426147461,195.4127426147461,195.5864868164062,195.5864868164062,195.7872772216797,195.9755249023438,195.9755249023438,195.9755249023438,196.1704635620117,196.1704635620117,196.3847045898438,196.3847045898438,196.6109619140625,196.8441162109375,196.8441162109375,197.0593032836914,197.0593032836914,197.2888259887695,197.5161743164062,197.7537689208984,197.7537689208984,197.9912033081055,197.9912033081055,198.1196517944336,198.1196517944336,198.1196517944336,198.1196517944336,198.1196517944336,198.1196517944336,195.4105453491211,195.4105453491211,195.5788269042969,195.5788269042969,195.7524261474609,195.9366760253906,196.1264877319336,196.1264877319336,196.3341903686523,196.5547027587891,196.5547027587891,196.7835159301758,196.7835159301758,197.0407180786133,197.0407180786133,197.2743835449219,197.5074920654297,197.5074920654297,197.5074920654297,197.7366638183594,197.7366638183594,197.9710998535156,197.9710998535156,198.1960372924805,198.1960372924805,198.1972808837891,198.1972808837891,198.1972808837891,198.1972808837891,198.1972808837891,198.1972808837891,195.595085144043,195.595085144043,195.7391510009766,195.7391510009766,195.9137649536133,195.9137649536133,196.0890884399414,196.0890884399414,196.0890884399414,196.2667617797852,196.4466705322266,196.4466705322266,196.6207427978516,196.8016738891602,196.8016738891602,196.9990692138672,196.9990692138672,197.1735153198242,197.1735153198242,197.3482208251953,197.5583114624023,197.5583114624023,197.7382125854492,197.7382125854492,197.7382125854492,197.959846496582,197.959846496582,198.1614608764648,198.1614608764648,198.2737426757812,198.2737426757812,198.2737426757812,198.2737426757812,198.2737426757812,198.2737426757812,198.2737426757812,198.2737426757812,198.2737426757812,195.7641830444336,195.7641830444336,195.9231643676758,195.9231643676758,196.1010818481445,196.1010818481445,196.2904357910156,196.2904357910156,196.4653701782227,196.6601486206055,196.6601486206055,196.8493270874023,196.8493270874023,197.0388946533203,197.2549057006836,197.4487533569336,197.4487533569336,197.6629104614258,197.8641586303711,198.0668411254883,198.2882919311523,198.3489303588867,198.3489303588867,198.3489303588867,198.3489303588867,195.7677917480469,195.7677917480469,195.9324035644531,195.9324035644531,195.9324035644531,196.1071548461914,196.1071548461914,196.2701644897461,196.2701644897461,196.4530258178711,196.4530258178711,196.6471099853516,196.6471099853516,196.8199768066406,196.8199768066406,196.9697875976562,196.9697875976562,197.1178894042969,197.1178894042969,197.3194046020508,197.5274505615234,197.5274505615234,197.7353897094727,197.7353897094727,197.9631118774414,198.1927185058594,198.1927185058594,198.1927185058594,198.4229202270508,198.4229202270508,198.4229202270508,198.4229202270508,198.4229202270508,198.4229202270508,198.4229202270508,198.4229202270508,198.4229202270508,195.9973831176758,196.170036315918,196.3547210693359,196.3547210693359,196.3547210693359,196.5461273193359,196.5461273193359,196.7537307739258,196.7537307739258,196.9779891967773,196.9779891967773,197.2145309448242,197.2145309448242,197.4529876708984,197.6890716552734,197.6890716552734,197.9250335693359,197.9250335693359,198.1610488891602,198.1610488891602,198.3984527587891,198.3984527587891,198.4956893920898,198.4956893920898,198.4956893920898,198.4956893920898,198.4956893920898,198.4956893920898,196.0306549072266,196.2039566040039,196.2039566040039,196.376823425293,196.376823425293,196.376823425293,196.5663604736328,196.5663604736328,196.7635879516602,196.7635879516602,196.9779815673828,197.2070465087891,197.4697341918945,197.7074356079102,197.7074356079102,197.9455718994141,197.9455718994141,198.1833267211914,198.1833267211914,198.421272277832,198.421272277832,198.5673065185547,198.5673065185547,198.5673065185547,198.5673065185547,198.5673065185547,198.5673065185547,198.5673065185547,198.5673065185547,196.1091232299805,196.2811050415039,196.2811050415039,196.4597854614258,196.4597854614258,196.6489334106445,196.6489334106445,196.8470230102539,196.8470230102539,197.0644149780273,197.0644149780273,197.2953414916992,197.5329360961914,197.5329360961914,197.7724609375,198.0109558105469,198.0109558105469,198.0109558105469,198.249267578125,198.249267578125,198.4878768920898,198.4878768920898,198.6377487182617,198.6377487182617,198.6377487182617,198.6377487182617,198.6377487182617,198.6377487182617,198.6377487182617,198.6377487182617,198.6377487182617,196.3815689086914,196.3815689086914,196.5522918701172,196.5522918701172,196.7320327758789,196.9101181030273,196.9101181030273,197.0157089233398,197.1714248657227,197.1714248657227,197.3775634765625,197.3775634765625,197.5974426269531,197.5974426269531,197.5974426269531,197.8248596191406,197.8248596191406,197.8248596191406,198.0510406494141,198.0510406494141,198.2845764160156,198.2845764160156,198.5215377807617,198.5215377807617,198.7070159912109,198.7070159912109,198.7070159912109,198.7070159912109,198.7070159912109,198.7070159912109,198.7070159912109,198.7070159912109,198.7070159912109,198.7070159912109,198.7070159912109,198.7070159912109,198.7070159912109,198.7070159912109,198.7070159912109,198.7070159912109,198.7070159912109,198.7070159912109,198.7070159912109,198.7070159912109,198.7070159912109,198.7070159912109,198.7070159912109,198.7070159912109,198.7070159912109,198.7070159912109,198.7070159912109,198.7070159912109,198.7070159912109,198.7070159912109,196.4099807739258,196.5463485717773,196.5463485717773,196.5463485717773,196.7274932861328,196.9066467285156,197.0989685058594,197.0989685058594,197.2888031005859,197.2888031005859,197.4904556274414,197.7051696777344,197.7051696777344,197.9333572387695,198.1682510375977,198.4025268554688,198.4025268554688,198.6371383666992,198.6371383666992,198.7750625610352,198.7750625610352,198.7750625610352,198.7750625610352,198.7750625610352,198.7750625610352,198.7750625610352,198.7750625610352,198.7750625610352,196.5784683227539,196.5784683227539,196.7487869262695,196.7487869262695,196.9294204711914,197.1179885864258,197.1179885864258,197.3173294067383,197.5365447998047,197.5365447998047,197.7678298950195,197.7678298950195,198.0020599365234,198.0020599365234,198.2356185913086,198.2356185913086,198.4689788818359,198.703254699707,198.703254699707,198.8421096801758,198.8421096801758,198.8421096801758,198.8421096801758,196.5397033691406,196.702995300293,196.702995300293,196.8761978149414,196.8761978149414,197.0625610351562,197.0625610351562,197.0625610351562,197.2543411254883,197.2543411254883,197.4648971557617,197.4648971557617,197.6890411376953,197.6890411376953,197.9267959594727,197.9267959594727,198.1636428833008,198.3996276855469,198.6351699829102,198.6351699829102,198.6351699829102,198.8707122802734,198.908203125,198.908203125,198.908203125,198.908203125,198.908203125,198.908203125,196.7042846679688,196.7042846679688,196.8761215209961,197.056282043457,197.056282043457,197.245849609375,197.4656677246094,197.4656677246094,197.6841888427734,197.6841888427734,197.9183807373047,197.9183807373047,198.1540451049805,198.1540451049805,198.388557434082,198.6241455078125,198.8580551147461,198.8580551147461,198.9731826782227,198.9731826782227,198.9731826782227,198.9731826782227,198.9731826782227,198.9731826782227,196.7489624023438,196.7489624023438,196.9165191650391,196.9165191650391,197.0921783447266,197.0921783447266,197.2795867919922,197.2795867919922,197.4747619628906,197.6860275268555,197.6860275268555,197.9133987426758,197.9133987426758,198.1515197753906,198.1515197753906,198.3887481689453,198.3887481689453,198.6250076293945,198.8611907958984,198.8611907958984,199.0370330810547,199.0370330810547,199.0370330810547,199.0370330810547,199.0370330810547,199.0370330810547,196.9933013916016,196.9933013916016,197.1669769287109,197.3535079956055,197.3535079956055,197.5481338500977,197.5481338500977,197.7621917724609,197.7621917724609,197.9929962158203,197.9929962158203,198.2312774658203,198.2312774658203,198.4674377441406,198.4674377441406,198.7027435302734,198.937744140625,198.937744140625,199.1000366210938,199.1000366210938,199.1000366210938,199.1000366210938,199.1000366210938,199.1000366210938,199.1000366210938,199.1000366210938,199.1000366210938,197.0756378173828,197.0756378173828,197.2488327026367,197.2488327026367,197.4357681274414,197.6266860961914,197.6266860961914,197.8297119140625,198.0509185791016,198.0509185791016,198.2840194702148,198.5202102661133,198.7568588256836,199.0158615112305,199.0158615112305,199.1618728637695,199.1618728637695,199.1618728637695,199.1618728637695,199.1618728637695,199.1618728637695,199.1618728637695,199.1618728637695,199.1618728637695,197.1881408691406,197.1881408691406,197.3625411987305,197.3625411987305,197.3625411987305,197.5501556396484,197.5501556396484,197.7456436157227,197.7456436157227,197.9607238769531,197.9607238769531,198.1913528442383,198.4294738769531,198.6669006347656,198.9037322998047,198.9037322998047,199.139274597168,199.2227478027344,199.2227478027344,199.2227478027344,199.2227478027344,199.2227478027344,199.2227478027344,197.1565017700195,197.1565017700195,197.3228530883789,197.499626159668,197.6883926391602,197.6883926391602,197.8877105712891,197.8877105712891,198.1308135986328,198.3650741577148,198.6029663085938,198.6029663085938,198.8400192260742,199.0766296386719,199.0766296386719,199.2826232910156,199.2826232910156,199.2826232910156,199.2826232910156,199.2826232910156,199.2826232910156,199.2826232910156,199.2826232910156,199.2826232910156,197.3338088989258,197.5080261230469,197.5080261230469,197.6935272216797,197.886848449707,197.886848449707,198.0993347167969,198.0993347167969,198.330810546875,198.330810546875,198.571403503418,198.571403503418,198.8088531494141,199.0455703735352,199.0455703735352,199.2806777954102,199.2806777954102,199.2806777954102,199.341552734375,199.341552734375,199.341552734375,199.341552734375,199.341552734375,199.341552734375,197.3628768920898,197.3628768920898,197.5534057617188,197.5534057617188,197.7374801635742,197.7374801635742,197.9306793212891,197.9306793212891,198.1418151855469,198.1418151855469,198.3685531616211,198.6101303100586,198.6101303100586,198.8495254516602,198.8495254516602,199.087776184082,199.087776184082,199.3251953125,199.3251953125,199.399528503418,199.399528503418,199.399528503418,199.399528503418,197.4408569335938,197.4408569335938,197.6078720092773,197.6078720092773,197.7856826782227,197.9760055541992,198.1786804199219,198.4022903442383,198.4022903442383,198.6393280029297,198.6393280029297,198.6393280029297,198.8784790039062,199.1167755126953,199.1167755126953,199.3516082763672,199.3516082763672,199.4565353393555,199.4565353393555,199.4565353393555,199.4565353393555,199.4565353393555,199.4565353393555,199.4565353393555,199.4565353393555,197.5133590698242,197.5133590698242,197.6853408813477,197.6853408813477,197.8645401000977,197.8645401000977,198.0561065673828,198.2605819702148,198.2605819702148,198.4844589233398,198.4844589233398,198.7222137451172,198.7222137451172,198.9616317749023,199.2002105712891,199.4341201782227,199.5127334594727,199.5127334594727,199.5127334594727,199.5127334594727,197.6132202148438,197.7852935791016,197.7852935791016,197.9674530029297,197.9674530029297,198.1608123779297,198.1608123779297,198.3684005737305,198.593376159668,198.593376159668,198.8348388671875,198.8348388671875,199.0752334594727,199.0752334594727,199.3140563964844,199.3140563964844,199.5449676513672,199.5678558349609,199.5678558349609,199.5678558349609,199.5678558349609,197.7562713623047,197.7562713623047,197.9307556152344,197.9307556152344,198.1174011230469,198.1174011230469,198.3127059936523,198.5273284912109,198.5273284912109,198.750358581543,198.750358581543,198.9857177734375,198.9857177734375,199.2137908935547,199.2137908935547,199.4410858154297,199.6222839355469,199.6222839355469,199.6222839355469,199.6222839355469,199.6222839355469,199.6222839355469,199.6222839355469,199.6222839355469,199.6222839355469,199.6222839355469,199.6222839355469,199.6222839355469,199.6222839355469,199.6222839355469,199.6222839355469,199.6222839355469,199.6222839355469,199.6222839355469,199.6222839355469,199.6222839355469,199.6222839355469,199.6222839355469,199.6222839355469,199.6222839355469,197.7526550292969,197.7526550292969,197.7526550292969,197.8312683105469,197.8312683105469,197.9958877563477,197.9958877563477,198.1742401123047,198.3677749633789,198.5754699707031,198.5754699707031,198.7990951538086,199.0394897460938,199.2797393798828,199.5099411010742,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,199.6755218505859,197.8362503051758,197.8362503051758,197.8362503051758,197.8362503051758,197.8362503051758,197.8362503051758,198.0026550292969,198.0026550292969,198.2008895874023,198.4056854248047,198.4056854248047,198.6276626586914,198.6276626586914,198.8684158325195,198.8684158325195,199.1292877197266,199.3532409667969,199.5659408569336,199.5659408569336,199.7970352172852,199.7970352172852,200.0260848999023,200.2567901611328,200.2567901611328,200.4937286376953,200.7353439331055,200.7353439331055,200.9714813232422,200.9714813232422,201.1687164306641,201.1687164306641,201.3651428222656,201.5612716674805,201.5612716674805,201.7577972412109,201.7577972412109,201.9541702270508,201.9541702270508,202.1507034301758,202.1507034301758,202.347038269043,202.347038269043,202.5431137084961,202.7396469116211,202.7396469116211,202.9360656738281,203.1326522827148,203.1326522827148,203.3286514282227,203.5251846313477,203.72119140625,203.9149322509766,203.9149322509766,204.110237121582,204.110237121582,204.3065795898438,204.5026016235352,204.5026016235352,204.7184448242188,204.7184448242188,204.9151458740234,204.9151458740234,205.1111602783203,205.1111602783203,205.3070373535156,205.502815246582,205.502815246582,205.5101928710938,205.5101928710938,205.5101928710938,205.5101928710938,205.5101928710938,205.5101928710938,205.5101928710938,205.5101928710938,205.5101928710938,198.3596725463867,198.3596725463867,198.3596725463867,198.5619735717773,198.5619735717773,198.7707901000977,199.0001525878906,199.0001525878906,199.2425079345703,199.2425079345703,199.4722061157227,199.4722061157227,199.6899719238281,199.6899719238281,199.6899719238281,199.9223175048828,199.9223175048828,200.1623611450195,200.1623611450195,200.4006118774414,200.4006118774414,200.6400299072266,200.6400299072266,200.8798370361328,201.1188735961914,201.1188735961914,201.3578567504883,201.3578567504883,201.3578567504883,201.6063766479492,201.8547821044922,202.1018524169922,202.1018524169922,202.3744583129883,202.6223831176758,202.8714904785156,202.8714904785156,203.1201629638672,203.1201629638672,203.3628234863281,203.3628234863281,203.6004333496094,203.6004333496094,203.8380584716797,203.8380584716797,204.0758514404297,204.3140335083008,204.5571823120117,204.7975158691406,204.7975158691406,205.0328979492188,205.263298034668,205.263298034668,205.4895935058594,205.4895935058594,205.7161331176758,205.7161331176758,205.7201690673828,205.7201690673828,205.7201690673828,205.7201690673828,205.7201690673828,205.7201690673828,198.6578598022461,198.8569183349609,198.8569183349609,199.0641250610352,199.0641250610352,199.0641250610352,199.2853775024414,199.2853775024414,199.5203247070312,199.5203247070312,199.7469329833984,199.9632949829102,200.2326354980469,200.2326354980469,200.4731750488281,200.4731750488281,200.7104034423828,200.7104034423828,200.9494323730469,200.9494323730469,200.9494323730469,201.1889266967773,201.1889266967773,201.4309463500977,201.4309463500977,201.6806869506836,201.9297866821289,202.1775588989258,202.1775588989258,202.4266204833984,202.4266204833984,202.6756134033203,202.6756134033203,202.9240951538086,202.9240951538086,203.1725234985352,203.1725234985352,203.4192962646484,203.6626129150391,203.6626129150391,203.9093017578125,204.156982421875,204.156982421875,204.4048309326172,204.6523132324219,204.6523132324219,204.8962097167969,204.8962097167969,205.144157409668,205.144157409668,205.3881378173828,205.6183624267578,205.8513412475586,205.8513412475586,205.9266204833984,205.9266204833984,205.9266204833984,205.9266204833984,205.9266204833984,205.9266204833984,205.9266204833984,205.9266204833984,205.9266204833984,198.8786087036133,198.8786087036133,199.0661773681641,199.0661773681641,199.265007019043,199.265007019043,199.4678421020508,199.4678421020508,199.6849670410156,199.6849670410156,199.9068984985352,199.9068984985352,200.1206130981445,200.1206130981445,200.359260559082,200.359260559082,200.5993804931641,200.5993804931641,200.836799621582,201.0720443725586,201.0720443725586,201.3080749511719,201.3080749511719,201.5449066162109,201.7825622558594,201.7825622558594,202.0251235961914,202.0251235961914,202.2675628662109,202.2675628662109,202.5122451782227,202.7580490112305,202.7580490112305,202.7580490112305,203.004035949707,203.004035949707,203.2502593994141,203.2502593994141,203.2502593994141,203.4964218139648,203.4964218139648,203.7421035766602,203.7421035766602,203.9877700805664,203.9877700805664,204.2333908081055,204.4794387817383,204.4794387817383,204.7488174438477,204.7488174438477,204.9932479858398,204.9932479858398,205.2382431030273,205.2382431030273,205.4847564697266,205.4847564697266,205.722526550293,205.722526550293,205.9580001831055,205.9580001831055,206.1298141479492,206.1298141479492,206.1298141479492,206.1298141479492,206.1298141479492,206.1298141479492,206.1298141479492,206.1298141479492,206.1298141479492,199.1425704956055,199.1425704956055,199.3246994018555,199.3246994018555,199.5219345092773,199.5219345092773,199.7242965698242,199.7242965698242,199.7242965698242,199.9380035400391,199.9380035400391,200.1529998779297,200.1529998779297,200.3689804077148,200.3689804077148,200.6102600097656,200.6102600097656,200.8509902954102,201.0875473022461,201.0875473022461,201.3221435546875,201.5562896728516,201.5562896728516,201.7975540161133,201.7975540161133,202.0360260009766,202.0360260009766,202.2765960693359,202.2765960693359,202.5436706542969,202.5436706542969,202.786506652832,202.786506652832,203.0298919677734,203.0298919677734,203.2645263671875,203.2645263671875,203.4981002807617,203.4981002807617,203.7323303222656,203.7323303222656,203.9706192016602,203.9706192016602,204.2042007446289,204.2042007446289,204.4438629150391,204.4438629150391,204.6789474487305,204.9201736450195,205.1656188964844,205.1656188964844,205.1656188964844,205.4108123779297,205.656120300293,205.8947372436523,205.8947372436523,206.1279754638672,206.329719543457,206.329719543457,206.329719543457,206.329719543457,206.329719543457,206.329719543457,206.329719543457,206.329719543457,206.329719543457,206.329719543457,206.329719543457,206.329719543457,199.5988388061523,199.5988388061523,199.5988388061523,199.7939605712891,199.7939605712891,199.9954299926758,199.9954299926758,200.2030487060547,200.4154815673828,200.65625,200.65625,200.8976898193359,200.8976898193359,201.1379776000977,201.1379776000977,201.3756866455078,201.3756866455078,201.6097717285156,201.8489532470703,201.8489532470703,202.0869598388672,202.3243789672852,202.5666427612305,202.5666427612305,202.802978515625,203.0408325195312,203.0408325195312,203.2829513549805,203.2829513549805,203.5272903442383,203.7716903686523,203.7716903686523,204.0147094726562,204.0147094726562,204.0147094726562,204.2552490234375,204.2552490234375,204.4993743896484,204.4993743896484,204.7445373535156,204.7445373535156,204.9891586303711,205.2344207763672,205.2344207763672,205.4799118041992,205.4799118041992,205.7255630493164,205.7255630493164,205.9715805053711,206.2050018310547,206.2050018310547,206.4389114379883,206.4389114379883,206.5263290405273,206.5263290405273,206.5263290405273,206.5263290405273,206.5263290405273,206.5263290405273,206.5263290405273,206.5263290405273,199.8282623291016,199.8282623291016,200.0296020507812,200.2326278686523,200.4464645385742,200.4464645385742,200.6577911376953,200.6577911376953,200.8863372802734,201.1269607543945,201.1269607543945,201.3682479858398,201.3682479858398,201.6078338623047,201.8453826904297,201.8453826904297,201.8453826904297,202.0865249633789,202.0865249633789,202.3237609863281,202.3237609863281,202.5618438720703,202.5618438720703,202.8004760742188,203.0460586547852,203.2920532226562,203.5371246337891,203.5371246337891,203.8066101074219,204.052360534668,204.052360534668,204.052360534668,204.2980117797852,204.2980117797852,204.2980117797852,204.5437240600586,204.789924621582,205.0367965698242,205.0367965698242,205.2838134765625,205.5310592651367,205.5310592651367,205.7738189697266,206.0091857910156,206.2415618896484,206.4684906005859,206.4684906005859,206.7023620605469,206.7198638916016,206.7198638916016,206.7198638916016,206.7198638916016,206.7198638916016,206.7198638916016,206.7198638916016,206.7198638916016,206.7198638916016,206.7198638916016,206.7198638916016,206.7198638916016,206.7198638916016,206.7198638916016,206.7198638916016,206.7198638916016,206.7198638916016,206.7198638916016,206.7198638916016,206.7198638916016,200.0617294311523,200.0617294311523,200.0617294311523,200.0617294311523,200.164794921875,200.164794921875,200.3567504882812,200.5540008544922,200.5540008544922,200.7500610351562,200.7500610351562,200.9500350952148,200.9500350952148,201.1823806762695,201.1823806762695,201.4217300415039,201.4217300415039,201.6501998901367,201.6501998901367,201.8767242431641,201.8767242431641,202.100471496582,202.100471496582,202.3298263549805,202.3298263549805,202.3298263549805,202.5677947998047,202.5677947998047,202.8057708740234,203.0401306152344,203.0401306152344,203.2775497436523,203.515739440918,203.7517547607422,203.9891662597656,203.9891662597656,204.2270736694336,204.2270736694336,204.4655227661133,204.4655227661133,204.7280731201172,204.7280731201172,204.7280731201172,204.9675598144531,204.9675598144531,205.2077865600586,205.2077865600586,205.4478454589844,205.4478454589844,205.6889419555664,205.9299621582031,206.1702880859375,206.1702880859375,206.4094696044922,206.4094696044922,206.6488342285156,206.6488342285156,206.8888702392578,206.8888702392578,206.8888702392578,206.9101028442383,206.9101028442383,206.9101028442383,206.9101028442383,206.9101028442383,206.9101028442383,206.9101028442383,206.9101028442383,206.9101028442383,206.9101028442383,206.9101028442383,206.9101028442383,200.4534606933594,200.4534606933594,200.6410369873047,200.6410369873047,200.8349380493164,201.0250473022461,201.2205276489258,201.4478988647461,201.4478988647461,201.6869430541992,201.9236145019531,201.9236145019531,202.1589050292969,202.1589050292969,202.3933410644531,202.3933410644531,202.6281967163086,202.6281967163086,202.8622512817383,202.8622512817383,203.1223373413086,203.3644256591797,203.6036224365234,203.6036224365234,203.6036224365234,203.8485870361328,203.8485870361328,204.0925521850586,204.3346328735352,204.3346328735352,204.576789855957,204.8106994628906,204.8106994628906,205.0475921630859,205.0475921630859,205.2854385375977,205.5216293334961,205.7582702636719,205.7582702636719,205.9955368041992,205.9955368041992,206.2310180664062,206.2310180664062,206.4724578857422,206.7178115844727,206.7178115844727,206.9626541137695,207.0975036621094,207.0975036621094,207.0975036621094,207.0975036621094,207.0975036621094,207.0975036621094,200.6575469970703,200.6575469970703,200.8327178955078,200.8327178955078,201.0232620239258,201.0232620239258,201.2112274169922,201.4215698242188,201.4215698242188,201.6451797485352,201.885009765625,201.885009765625,202.1227798461914,202.1227798461914,202.1227798461914,202.3571929931641,202.3571929931641,202.5911026000977,202.8231506347656,203.0566864013672,203.0566864013672,203.290397644043,203.290397644043,210.9747772216797,210.9747772216797,210.9747772216797,210.9747772216797,210.9747772216797,210.9747772216797,210.9747772216797,210.9747772216797,210.9747772216797,210.9747772216797,210.9747772216797,210.9747772216797,210.9747772216797,210.9747772216797,210.9747772216797,210.9747772216797,210.9747772216797,210.9747772216797,210.9747772216797,210.9747772216797,210.9747772216797,210.9747772216797,218.6041717529297,218.6041717529297,218.6041717529297,218.6041793823242,218.6041793823242,218.6041793823242,218.6041793823242,218.6041793823242,218.6041793823242,218.6041793823242,218.6041793823242,218.6041793823242,218.6041793823242,218.6041793823242,218.6041793823242,218.6041793823242,218.6041793823242,218.6041793823242,218.6041793823242,218.6041793823242,218.6041793823242,218.6041793823242,218.6041793823242,218.6041793823242,218.6041793823242,218.6041793823242,218.6041793823242,218.6041793823242,218.6041793823242,233.8629684448242,233.8629684448242,233.8629684448242,233.8629684448242,233.8629684448242,233.8629684448242,233.8629684448242,233.8629684448242,233.8629684448242,233.8629684448242,233.8629684448242,233.8629684448242,233.8629684448242,233.8629684448242,233.8629684448242,233.8629684448242,233.8629684448242,233.8629684448242,233.8629684448242,233.8629684448242,241.4923858642578,241.4923858642578,241.4923858642578,241.4923858642578,241.4923858642578,241.4923858642578,241.4923858642578,241.4923858642578,241.6262512207031,241.6262512207031,241.6262512207031,241.6262512207031,241.6262512207031,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582,256.887580871582],"meminc":[0,0,0,0,0,0,15.28223419189453,0,0,0,0,0,30.46574401855469,0,0,0,0,0,0,0,0,0,0,0,4.57763671875e-05,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-0.00030517578125,0,15.30680084228516,0,0.2046051025390625,0.2020950317382812,0,0.2000274658203125,0,0.2009353637695312,0,0.2190475463867188,0.225830078125,0,0.2363204956054688,0,0.2157135009765625,0,0.2299957275390625,0,0.2293548583984375,0,0,0.2238311767578125,0.2250518798828125,0,0.2228851318359375,0.2252426147460938,0,0.1623153686523438,0,-3.08270263671875,0,0.2125167846679688,0,0.2198104858398438,0.2210235595703125,0,0.260040283203125,0,0.2283248901367188,0.2363128662109375,0,0.227752685546875,0.2274169921875,0.237091064453125,0,0.2290420532226562,0.2235488891601562,0,0.23052978515625,0,0.2271194458007812,0.1722488403320312,0,0,-3.054847717285156,0,0.2051315307617188,0,0.2198867797851562,0,0.2241363525390625,0,0.2399826049804688,0,0.2322235107421875,0,0.234619140625,0.2298202514648438,0,0,0.2499771118164062,0.23431396484375,0.2251358032226562,0,0.2312774658203125,0,0.2318191528320312,0,0.2249832153320312,0,0.1589584350585938,0,0,-3.002182006835938,0.2027435302734375,0.2233352661132812,0,0.2253036499023438,0,0.243896484375,0,0.23187255859375,0.233001708984375,0,0,0.2395553588867188,0.2344284057617188,0,0.2336883544921875,0,0.2349624633789062,0,0.23406982421875,0,0.2345123291015625,0.2138442993164062,0,0.1030044555664062,0,0,-2.880645751953125,0,0.2276458740234375,0.24163818359375,0.2461776733398438,0,0.2440261840820312,0,0.2366104125976562,0,0.2349319458007812,0,0.2351226806640625,0,0.2344894409179688,0.2347259521484375,0,0.2354736328125,0.2362518310546875,0,0.2354812622070312,0,0.1226272583007812,0,0,-2.863540649414062,0.2176513671875,0,0.2373809814453125,0,0.24462890625,0,0,0.2423553466796875,0,0.2396392822265625,0,0.2378387451171875,0.22998046875,0,0.22882080078125,0,0.2299118041992188,0,0.2579269409179688,0,0.2360153198242188,0,0.2358245849609375,0,0.1088180541992188,0,0,-2.815948486328125,0.2165298461914062,0,0.2327957153320312,0,0.2463836669921875,0,0.2410430908203125,0.24114990234375,0.2272415161132812,0,0.2344589233398438,0,0,0.2349624633789062,0,0,0.23583984375,0,0.232025146484375,0.2358245849609375,0,0.2352981567382812,0,0.084259033203125,0,-2.761131286621094,0.2155532836914062,0,0.239715576171875,0,0.2211380004882812,0.2401657104492188,0,0.2393341064453125,0,0.2369613647460938,0.2584762573242188,0.2347869873046875,0,0.2338409423828125,0.23480224609375,0,0.2356796264648438,0,0,0.2347640991210938,0,0.01650238037109375,0,0,-2.633750915527344,0,0.2263565063476562,0,0.2397079467773438,0,0,0.2379989624023438,0.2268524169921875,0,0.2376251220703125,0.2360153198242188,0.2301712036132812,0,0.2333908081054688,0,0,0.2001953125,0.22796630859375,0,0.1794891357421875,0,0.2349624633789062,0.002288818359375,0,0,-2.6298828125,0,0.196502685546875,0.216583251953125,0,0.2338943481445312,0,0.2406539916992188,0.2359619140625,0,0.2357177734375,0.2323837280273438,0.231536865234375,0,0,0.1654739379882812,0,0,0.1763839721679688,0.1783905029296875,0,0.1865310668945312,0,0.1778030395507812,0,0,0,0,0,-2.520111083984375,0.2112655639648438,0,0.2273712158203125,0,0.2369003295898438,0,0,0.236907958984375,0,0.2372207641601562,0,0.2367401123046875,0,0.2346420288085938,0.23358154296875,0.2360992431640625,0,0.2334518432617188,0.1971893310546875,0,0.07550048828125,0,-2.560943603515625,0.2179336547851562,0,0.2564773559570312,0.2345046997070312,0.233856201171875,0,0.2348403930664062,0.2357940673828125,0,0,0.2313232421875,0,0.2345428466796875,0,0.2554931640625,0.1992340087890625,0.237548828125,0,0,0.06491851806640625,0,0,-2.539726257324219,0,0.204742431640625,0,0.2260818481445312,0.2343902587890625,0,0,0.2346572875976562,0.235595703125,0,0.2333831787109375,0,0.2325057983398438,0.2347869873046875,0,0.2337875366210938,0,0.2378921508789062,0,0.2397689819335938,0.0663299560546875,0,-2.482948303222656,0,0.2123260498046875,0.2295913696289062,0.2364959716796875,0,0.2340621948242188,0,0.2611312866210938,0,0.2336044311523438,0.2324600219726562,0,0.2347869873046875,0,0.235992431640625,0,0.2344512939453125,0,0.2111358642578125,0,0,0,0,0,-2.36407470703125,0,0.2179641723632812,0,0.2307205200195312,0,0.2345809936523438,0,0.2351455688476562,0,0.2374267578125,0,0.23406982421875,0,0.2358856201171875,0,0.2340621948242188,0,0,0.2363815307617188,0,0,0.2368545532226562,0.1028518676757812,0,0,-2.432342529296875,0.2007064819335938,0,0.2235260009765625,0.2265396118164062,0,0.2357025146484375,0,0,0.2612686157226562,0,0,0.2294998168945312,0,0.2346267700195312,0,0.23431396484375,0,0.23248291015625,0,0.2342376708984375,0,0.1901931762695312,0,0,0,0,0,-2.271888732910156,0,0.2129058837890625,0.1815414428710938,0,0.132659912109375,0,0.195831298828125,0.1716156005859375,0,0.2030258178710938,0.2077789306640625,0,0.1668319702148438,0.2238311767578125,0.185302734375,0.187164306640625,0,0.2008132934570312,0.0720977783203125,0,0,0,0,0,-2.248519897460938,0,0.1638946533203125,0,0.1743011474609375,0.1464691162109375,0,0.2028350830078125,0.1715087890625,0.18646240234375,0,0.202392578125,0,0.1666336059570312,0.2228775024414062,0,0.2283401489257812,0,0.2064666748046875,0.218536376953125,0.02629852294921875,0,0,-2.31341552734375,0.181640625,0,0.1704025268554688,0,0.1860275268554688,0,0.1705245971679688,0,0,0.1946487426757812,0.2033767700195312,0.1987838745117188,0,0.2137832641601562,0.2029342651367188,0,0.21929931640625,0.24822998046875,0,0.1594467163085938,0,0.03165435791015625,0,0,0,-2.136329650878906,0.18402099609375,0.1731185913085938,0,0.1991806030273438,0,0.215850830078125,0,0,0.2293319702148438,0,0.2344207763671875,0,0.233978271484375,0.2352447509765625,0,0.2334136962890625,0,0,0.2333526611328125,0,0.03072357177734375,0,0,-2.201812744140625,0,0.1928482055664062,0,0.221282958984375,0,0.2179183959960938,0.2320480346679688,0.2373504638671875,0.2359085083007812,0.2375946044921875,0.2357940673828125,0,0,0.2375717163085938,0.218658447265625,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2.232513427734375,0,0.1561203002929688,0,0.1713180541992188,0.1810226440429688,0,0.190460205078125,0.2031478881835938,0,0.2143096923828125,0.2275848388671875,0,0.229705810546875,0.221405029296875,0,0,0.2263412475585938,0.2256622314453125,0,0.04937744140625,0,-2.159858703613281,0,0.1873855590820312,0,0.1925506591796875,0,0.2061309814453125,0.2444381713867188,0,0.2341079711914062,0,0.2330780029296875,0.2324371337890625,0.2325286865234375,0,0.231781005859375,0,0.2286453247070312,0,0,0,-2.083663940429688,0.1884841918945312,0,0,0.1973876953125,0.2178268432617188,0,0.2306900024414062,0,0.2363815307617188,0,0.2368927001953125,0,0.23431396484375,0,0.2296981811523438,0,0.232086181640625,0.1419754028320312,0,0,0,0,0,-1.987106323242188,0,0.1823577880859375,0,0.1924972534179688,0,0.2012481689453125,0,0.21954345703125,0,0.2300796508789062,0.2306289672851562,0.2282485961914062,0.2286376953125,0.2312545776367188,0,0.1037368774414062,0,0,0,-1.948104858398438,0,0,0.1805648803710938,0,0.1989669799804688,0,0.2140960693359375,0,0,0.2307891845703125,0.191741943359375,0,0.2281265258789062,0,0,0.2090225219726562,0,0.2435073852539062,0,0.2318038940429688,0.079681396484375,0,0,0,0,0,-1.890556335449219,0.17034912109375,0,0.197265625,0,0.1919021606445312,0,0.2116241455078125,0,0.2181167602539062,0,0.217315673828125,0.2305679321289062,0.2151412963867188,0.2189788818359375,0,0.078399658203125,0,0,-2.027816772460938,0,0.1848831176757812,0,0.1934356689453125,0,0.1866455078125,0,0.2230453491210938,0,0.2230148315429688,0,0.2370223999023438,0.225311279296875,0.2160720825195312,0,0.2330322265625,0,0.1635589599609375,0,0,0,0,0,0,0,-1.890762329101562,0,0.1661758422851562,0.1874313354492188,0,0,0.20477294921875,0,0.2236175537109375,0.23126220703125,0,0.23193359375,0,0.233795166015625,0.2317428588867188,0,0.23126220703125,0,0.006011962890625,0,0,-1.874008178710938,0,0.1843185424804688,0.195953369140625,0,0.2148361206054688,0.2289505004882812,0,0,0.233428955078125,0.235260009765625,0,0.2328414916992188,0,0.2339096069335938,0,0.1708602905273438,0,0,0,-1.820091247558594,0.175994873046875,0.1928482055664062,0.2149124145507812,0,0.228363037109375,0.235595703125,0,0,0.2300949096679688,0,0.250579833984375,0.2085723876953125,0,0.138519287109375,0,0,0,-1.801536560058594,0,0.16912841796875,0,0,0.1862106323242188,0.1921463012695312,0.2220840454101562,0,0.2211685180664062,0.223846435546875,0,0.2230453491210938,0,0.171661376953125,0.23052978515625,0,0.0163116455078125,0,0,-1.842643737792969,0.1864547729492188,0,0.171600341796875,0,0.1895217895507812,0,0.192535400390625,0,0.2170181274414062,0.216888427734375,0.2174301147460938,0,0.2304458618164062,0,0.219635009765625,0,0.0547637939453125,0,0,-1.821823120117188,0,0.1783599853515625,0.186248779296875,0,0,0.1820220947265625,0.1948776245117188,0,0.194671630859375,0.2122802734375,0,0,0.2316741943359375,0.221923828125,0,0.2242431640625,0,0.04827117919921875,0,0,-1.792701721191406,0,0.1794052124023438,0.1816253662109375,0.1929702758789062,0,0,0.2091445922851562,0.2245025634765625,0,0.2391281127929688,0,0,0.230743408203125,0,0.2290496826171875,0.1580581665039062,0,0,0,0,0,0,0,-1.652442932128906,0,0.1804122924804688,0,0.18756103515625,0,0.2065353393554688,0,0.2218704223632812,0,0.2563705444335938,0.23419189453125,0,0.2335586547851562,0.18304443359375,0,0,0,0,0,-1.652687072753906,0,0.1792221069335938,0,0.1817398071289062,0,0.1696243286132812,0.1933212280273438,0.217010498046875,0,0,0.21844482421875,0,0.23748779296875,0.23138427734375,0,0.0747222900390625,0,-1.721931457519531,0,0.176025390625,0,0.1850814819335938,0,0.1881103515625,0,0.2260894775390625,0.22613525390625,0,0,0.2285003662109375,0.2336883544921875,0,0.2326583862304688,0,0.07511138916015625,0,0,0,0,0,-1.533653259277344,0,0.1815109252929688,0.1877593994140625,0.20355224609375,0.2274017333984375,0,0.2226943969726562,0.2329864501953125,0,0,0.2351531982421875,0,0.09123992919921875,0,0,0,0,0,0,0,-1.5115966796875,0.1811599731445312,0.1973800659179688,0,0.223724365234375,0,0,0.2184982299804688,0,0.2038650512695312,0,0,0.2284622192382812,0,0.2139511108398438,0,0.0924530029296875,0,0,0,0,0,0,0,-1.497879028320312,0,0.181304931640625,0,0.1733551025390625,0,0.186553955078125,0,0.2174224853515625,0,0.2099761962890625,0,0.2201156616210938,0,0.2241897583007812,0,0.1320266723632812,0,0,0,-1.454147338867188,0.1798629760742188,0.198883056640625,0.2172393798828125,0,0.229644775390625,0,0.2375946044921875,0,0.2363510131835938,0,0.2009353637695312,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.595405578613281,0,0,0,0,0,0.11846923828125,0,0.1670150756835938,0.1600341796875,0.198638916015625,0.2033767700195312,0,0.1744232177734375,0,0.185546875,0,0.2259750366210938,0,0.21441650390625,0,0.181427001953125,0,0.1507339477539062,0,0.1690521240234375,0.1843109130859375,0.19647216796875,0.20330810546875,0.1865768432617188,0,0.1858062744140625,0,0.1768722534179688,0,0.1869049072265625,0,0.179351806640625,0,0.1811065673828125,0.1873626708984375,0,0.1789627075195312,0,0.1874237060546875,0,0.1975936889648438,0,0,0.1810836791992188,0,0.0951080322265625,0,0,0,0,0,-4.517929077148438,0.20648193359375,0,0.2195205688476562,0,0.2268753051757812,0,0.2295913696289062,0,0.222808837890625,0,0.2232208251953125,0,0.2436981201171875,0,0.2427520751953125,0.2414321899414062,0,0.2386932373046875,0.2397384643554688,0.237701416015625,0,0.2377777099609375,0.23699951171875,0,0.2375946044921875,0.23724365234375,0.2364349365234375,0.2368240356445312,0.2288970947265625,0.2264785766601562,0,0,0,0,0,-4.52667236328125,0,0.20355224609375,0,0.2160110473632812,0,0.2371978759765625,0.235382080078125,0,0.2219696044921875,0,0.2300949096679688,0,0.2442703247070312,0.2431640625,0,0.2424850463867188,0,0.236419677734375,0,0.220489501953125,0.2378692626953125,0.2366485595703125,0,0.2276611328125,0,0.2219772338867188,0.2282257080078125,0.2209243774414062,0,0.2195968627929688,0.233489990234375,0,0.2154998779296875,0,0,0.08444976806640625,0,0,0,-4.347702026367188,0,0.2007980346679688,0,0.2022781372070312,0,0.2170639038085938,0,0,0.2134170532226562,0,0.2001571655273438,0,0.242706298828125,0,0,0.2314987182617188,0.2343673706054688,0,0.2367172241210938,0,0.2246780395507812,0.2373504638671875,0.2269058227539062,0,0.22845458984375,0,0.2334213256835938,0,0,0.2334136962890625,0.2182235717773438,0.2281341552734375,0,0.2319869995117188,0,0.2279205322265625,0,0.2068862915039062,0,0,0,-4.417617797851562,0,0.2128753662109375,0,0.2023696899414062,0.197357177734375,0,0.1993484497070312,0,0.1986846923828125,0.196533203125,0.2249069213867188,0,0.209716796875,0,0.21282958984375,0,0.2229843139648438,0.2043380737304688,0,0.2191314697265625,0,0.2048416137695312,0.21295166015625,0,0.2177658081054688,0,0.183929443359375,0,0,0.2200775146484375,0,0.1778717041015625,0.2035751342773438,0,0.2033920288085938,0,0.1905288696289062,0.2074356079101562,0,0.02068328857421875,0,0,0,-4.2340087890625,0,0.175140380859375,0,0.19781494140625,0.1466445922851562,0,0.1754608154296875,0,0.180938720703125,0,0,0.1949996948242188,0.22039794921875,0.197235107421875,0.2136611938476562,0.2171173095703125,0,0.21490478515625,0.2299423217773438,0,0.2013931274414062,0,0.2091751098632812,0,0,0.219512939453125,0,0.2121505737304688,0,0.144775390625,0,0.2040557861328125,0.1877593994140625,0.2439804077148438,0.138397216796875,0,0.1768875122070312,0,0.05614471435546875,0,0,0,0,0,-4.196823120117188,0.197509765625,0.1982345581054688,0.2003402709960938,0.20050048828125,0,0.2328567504882812,0,0.2401123046875,0,0.2384796142578125,0.2372207641601562,0,0.237091064453125,0.2344970703125,0.23272705078125,0.2328720092773438,0,0.2330398559570312,0,0.2223281860351562,0,0,0.2558670043945312,0,0.2323074340820312,0,0.2321548461914062,0,0.2269363403320312,0.222991943359375,0,0.011260986328125,0,0,0,0,0,-4.020225524902344,0,0,0.19903564453125,0.1971664428710938,0,0.1953201293945312,0,0.22308349609375,0,0.2412109375,0.2412261962890625,0.2395782470703125,0.2374191284179688,0,0.2356643676757812,0,0.2335586547851562,0,0.2343292236328125,0.2363204956054688,0,0.2332534790039062,0,0.2317352294921875,0,0.232208251953125,0,0.2346878051757812,0.2524566650390625,0.221923828125,0,0,0.02054595947265625,0,0,0,0,0,0,0,-3.980186462402344,0,0.1956024169921875,0,0.1930770874023438,0.200042724609375,0.23193359375,0,0,0.238677978515625,0,0.2396621704101562,0,0.23724365234375,0,0.2365493774414062,0,0.2354888916015625,0,0.234130859375,0,0.2333297729492188,0,0.2351455688476562,0,0,0.2353591918945312,0.2353134155273438,0.2370529174804688,0,0.2372589111328125,0.230010986328125,0,0.2128448486328125,0,0,0,0,0,-4.0531005859375,0,0,0.196380615234375,0,0.1921539306640625,0,0.1909255981445312,0.21038818359375,0,0.22857666015625,0,0.2387161254882812,0.2405624389648438,0,0.2388992309570312,0.2381668090820312,0,0.235565185546875,0.2334976196289062,0,0.2356491088867188,0.23602294921875,0,0.2323379516601562,0,0.2099227905273438,0.2329940795898438,0,0.23565673828125,0,0.2063674926757812,0,0.1369171142578125,0,0,0,0,0,-3.852401733398438,0,0.1830368041992188,0,0.1704177856445312,0.1901473999023438,0.1763076782226562,0.184539794921875,0.2123260498046875,0.1978683471679688,0.2254867553710938,0,0.2070846557617188,0,0,0.2090377807617188,0.2293472290039062,0.2057647705078125,0,0.2274322509765625,0,0.203216552734375,0,0,0.2302093505859375,0,0.228668212890625,0,0.2043914794921875,0.2278213500976562,0,0.1978836059570312,0.05617523193359375,0,0,0,0,0,-3.874229431152344,0,0.1853561401367188,0.1726150512695312,0,0.1535186767578125,0,0.2039337158203125,0,0.172637939453125,0,0.2036209106445312,0.22845458984375,0,0.2078857421875,0,0.2295608520507812,0,0,0.1998977661132812,0,0.21630859375,0,0.225189208984375,0.1935043334960938,0,0.2252883911132812,0.224853515625,0.167510986328125,0,0.1739273071289062,0,0,0.1931838989257812,0,0.227752685546875,0,0.182159423828125,0,0,0,0,0,-3.872383117675781,0.186279296875,0,0.1861953735351562,0,0.1887969970703125,0,0.2118453979492188,0,0.226318359375,0.236419677734375,0,0.2375564575195312,0,0.237945556640625,0,0.2381210327148438,0,0.2369461059570312,0.2347412109375,0,0.2349395751953125,0,0.235565185546875,0.2358322143554688,0,0.235443115234375,0,0.2366943359375,0.2280120849609375,0.1557693481445312,0,0,0,0,0,-3.763191223144531,0.187652587890625,0.1821441650390625,0,0.2032012939453125,0.2210311889648438,0,0.2313461303710938,0,0.2377395629882812,0,0.239837646484375,0,0.2381439208984375,0,0.240203857421875,0,0.2367477416992188,0,0,0.2337799072265625,0.2223052978515625,0,0.2480850219726562,0,0.235137939453125,0,0.2238082885742188,0.234588623046875,0.2301788330078125,0,0.02652740478515625,0,0,0,0,0,-3.607078552246094,0,0.184600830078125,0,0.1886444091796875,0,0.217742919921875,0,0.2398300170898438,0.2333221435546875,0.2254409790039062,0,0,0.2386550903320312,0,0.2265701293945312,0,0.2396392822265625,0,0.2400970458984375,0,0.2403564453125,0,0.2158584594726562,0,0,0.244964599609375,0,0.2372894287109375,0.22601318359375,0.2266464233398438,0.08898162841796875,0,0,0,0,0,-3.613571166992188,0,0.1852951049804688,0,0.1789703369140625,0.2104110717773438,0,0.22674560546875,0,0.2384414672851562,0,0.2135696411132812,0,0.2470855712890625,0,0.236846923828125,0,0.2258377075195312,0,0.233856201171875,0.246307373046875,0,0.2354507446289062,0,0.2251129150390625,0,0.2364349365234375,0.2224349975585938,0,0.2311019897460938,0,0.1254119873046875,0,0,0,-3.565666198730469,0,0.1749267578125,0,0.187042236328125,0,0.1856918334960938,0,0.214935302734375,0,0.2358932495117188,0.2338409423828125,0.2256851196289062,0,0.2379226684570312,0,0.2399444580078125,0.2201919555664062,0,0.235992431640625,0,0.243438720703125,0.2357711791992188,0,0.2286453247070312,0.2351531982421875,0,0.2164688110351562,0.1182022094726562,0,0,0,0,0,-3.505607604980469,0,0.1744232177734375,0.1913070678710938,0,0.20709228515625,0.2062911987304688,0.2237472534179688,0,0.2477569580078125,0,0.2392425537109375,0.2263641357421875,0,0.2404022216796875,0,0.2465438842773438,0.2105789184570312,0.2444229125976562,0,0.2388153076171875,0,0.2201690673828125,0,0.2385635375976562,0.2266998291015625,0.02561187744140625,0,0,0,-3.380691528320312,0,0.1811599731445312,0,0.18157958984375,0,0.2034225463867188,0.2040023803710938,0,0.2249832153320312,0,0,0.220794677734375,0.2431411743164062,0,0.2388229370117188,0.2166061401367188,0.2156600952148438,0,0.2102813720703125,0.2179412841796875,0.2180023193359375,0,0.239288330078125,0.2243194580078125,0,0.2249832153320312,0,0.01647186279296875,0,0,0,0,0,-3.331314086914062,0,0.17022705078125,0,0.1872177124023438,0.1947784423828125,0.1672286987304688,0,0.1988143920898438,0.198150634765625,0,0.2019577026367188,0,0,0.2279434204101562,0,0,0.244415283203125,0.2442626953125,0.2154998779296875,0,0.2418060302734375,0,0.23712158203125,0.2255935668945312,0,0.2348556518554688,0.2331924438476562,0,0.00733184814453125,0,0,0,0,0,-3.291900634765625,0.1735153198242188,0,0,0.1875457763671875,0,0.1997451782226562,0,0.21673583984375,0.2257614135742188,0,0.2258377075195312,0.2391738891601562,0,0.2263641357421875,0,0.24029541015625,0.2480545043945312,0.237091064453125,0,0.2254638671875,0,0.2374649047851562,0,0.240386962890625,0,0.2096786499023438,0,0.05632781982421875,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-3.356719970703125,0,0,0.1021652221679688,0,0.168426513671875,0,0,0.188262939453125,0,0.16497802734375,0,0,0.2029953002929688,0.2088851928710938,0.2184677124023438,0.2335357666015625,0,0.2332305908203125,0.22601318359375,0.2275238037109375,0.2293472290039062,0,0.2190170288085938,0,0.2333297729492188,0.2236557006835938,0.2302780151367188,0.1422576904296875,0,0,0,-3.266136169433594,0,0.1686172485351562,0,0,0.1834182739257812,0,0.1973419189453125,0.1802902221679688,0.2266769409179688,0,0.2289810180664062,0,0.222900390625,0.2361373901367188,0,0.2386322021484375,0,0.2422256469726562,0.21533203125,0.2475051879882812,0,0.2361907958984375,0,0.2246551513671875,0,0.234405517578125,0,0.0772857666015625,0,0,0,-3.157905578613281,0.1806869506835938,0.1826019287109375,0,0.1905899047851562,0,0.2028656005859375,0,0.2184295654296875,0.233978271484375,0.2325286865234375,0.2327728271484375,0,0.2324981689453125,0.2323684692382812,0,0.2335968017578125,0.236114501953125,0.237548828125,0.2359085083007812,0,0,0.1683197021484375,0,0,0,0,0,0,0,0,-3.051078796386719,0,0.179473876953125,0,0.1844940185546875,0.184783935546875,0.197509765625,0,0.2149810791015625,0,0,0.22882080078125,0,0.2340927124023438,0,0.2347564697265625,0.230224609375,0.2326812744140625,0.23333740234375,0.235076904296875,0.2367172241210938,0,0.22576904296875,0,0.08974456787109375,0,0,0,-3.067108154296875,0,0.1749954223632812,0,0.17596435546875,0,0.1869125366210938,0,0,0.18426513671875,0,0.190887451171875,0,0,0.2063369750976562,0,0.2261886596679688,0.2302398681640625,0,0.2314529418945312,0,0.23150634765625,0.2342529296875,0,0.2017364501953125,0,0.2344512939453125,0,0.2035369873046875,0,0.2351760864257812,0,0.0091400146484375,0,0,0,0,0,-2.971824645996094,0,0.1749267578125,0,0,0.1830520629882812,0.1880416870117188,0,0.1926727294921875,0.2098846435546875,0,0.2220306396484375,0.2281265258789062,0.2334976196289062,0,0.2293472290039062,0,0.2242431640625,0,0.2223281860351562,0,0.2352066040039062,0,0.2309799194335938,0.2332611083984375,0,0.0526885986328125,0,0,0,0,0,-2.980598449707031,0.1734771728515625,0,0.1972503662109375,0,0.1862564086914062,0.1920089721679688,0.2050018310546875,0,0.219940185546875,0.21453857421875,0.2244491577148438,0,0.2241363525390625,0.2314529418945312,0,0.233856201171875,0,0.218231201171875,0.236083984375,0,0.2312698364257812,0,0.07968902587890625,0,0,0,0,0,0,0,-2.941581726074219,0.1617355346679688,0,0.1801986694335938,0,0.1864242553710938,0.1910247802734375,0,0.1985855102539062,0.228759765625,0,0.215301513671875,0,0.2242202758789062,0,0.2196807861328125,0.2251968383789062,0,0.2312545776367188,0,0.2374496459960938,0,0.1991119384765625,0,0.2332534790039062,0,0.0950469970703125,0,0,0,0,0,-2.92584228515625,0,0.1642532348632812,0,0.1675872802734375,0.1794357299804688,0.1602783203125,0.1881103515625,0,0.1817245483398438,0,0.2105865478515625,0,0.219879150390625,0,0,0.2193222045898438,0,0.22344970703125,0.2260055541992188,0,0.2035598754882812,0.2207412719726562,0,0.2258529663085938,0.2192840576171875,0,0,0,0,0,0,0,0,-2.795585632324219,0,0.1511001586914062,0.176300048828125,0,0.1833572387695312,0,0.1878204345703125,0,0.2035064697265625,0,0.184906005859375,0.20465087890625,0,0.1728515625,0,0,0.1965560913085938,0,0.2010650634765625,0,0.1980972290039062,0.2060089111328125,0,0.2057113647460938,0,0.2030410766601562,0.2035064697265625,0,0,0,0,0,0,0,0,0,0,0,-2.718612670898438,0,0.1675643920898438,0,0.1551666259765625,0,0.1803436279296875,0,0.1739501953125,0,0.1877212524414062,0,0.1945877075195312,0,0.1833724975585938,0,0.2002334594726562,0,0.1904373168945312,0,0.2039108276367188,0.1940078735351562,0,0.1919708251953125,0,0.2102890014648438,0.1938552856445312,0,0.172821044921875,0,0,0,0,0,-2.739982604980469,0.1459121704101562,0.1494369506835938,0,0.1753082275390625,0,0,0.1559829711914062,0,0.1786575317382812,0,0.1749267578125,0,0.1789703369140625,0,0.225555419921875,0,0.1762847900390625,0.2169113159179688,0,0.1916122436523438,0,0.19427490234375,0,0.2136917114257812,0,0.18011474609375,0.199981689453125,0,0.06252288818359375,0,0,0,-2.759468078613281,0,0.1316070556640625,0,0.1737442016601562,0,0.2007904052734375,0.1882476806640625,0,0,0.1949386596679688,0,0.2142410278320312,0,0.22625732421875,0.233154296875,0,0.2151870727539062,0,0.229522705078125,0.2273483276367188,0.2375946044921875,0,0.2374343872070312,0,0.128448486328125,0,0,0,0,0,-2.7091064453125,0,0.1682815551757812,0,0.1735992431640625,0.1842498779296875,0.1898117065429688,0,0.20770263671875,0.2205123901367188,0,0.2288131713867188,0,0.2572021484375,0,0.2336654663085938,0.2331085205078125,0,0,0.2291717529296875,0,0.23443603515625,0,0.2249374389648438,0,0.00124359130859375,0,0,0,0,0,-2.602195739746094,0,0.1440658569335938,0,0.1746139526367188,0,0.175323486328125,0,0,0.17767333984375,0.1799087524414062,0,0.174072265625,0.1809310913085938,0,0.1973953247070312,0,0.1744461059570312,0,0.1747055053710938,0.2100906372070312,0,0.179901123046875,0,0,0.2216339111328125,0,0.2016143798828125,0,0.1122817993164062,0,0,0,0,0,0,0,0,-2.509559631347656,0,0.1589813232421875,0,0.17791748046875,0,0.1893539428710938,0,0.1749343872070312,0.1947784423828125,0,0.189178466796875,0,0.1895675659179688,0.2160110473632812,0.19384765625,0,0.2141571044921875,0.2012481689453125,0.2026824951171875,0.2214508056640625,0.060638427734375,0,0,0,-2.581138610839844,0,0.16461181640625,0,0,0.1747512817382812,0,0.1630096435546875,0,0.182861328125,0,0.1940841674804688,0,0.1728668212890625,0,0.149810791015625,0,0.148101806640625,0,0.2015151977539062,0.2080459594726562,0,0.2079391479492188,0,0.22772216796875,0.2296066284179688,0,0,0.2302017211914062,0,0,0,0,0,0,0,0,-2.425537109375,0.1726531982421875,0.1846847534179688,0,0,0.19140625,0,0.2076034545898438,0,0.2242584228515625,0,0.236541748046875,0,0.2384567260742188,0.236083984375,0,0.2359619140625,0,0.2360153198242188,0,0.2374038696289062,0,0.09723663330078125,0,0,0,0,0,-2.465034484863281,0.1733016967773438,0,0.1728668212890625,0,0,0.1895370483398438,0,0.1972274780273438,0,0.2143936157226562,0.22906494140625,0.2626876831054688,0.237701416015625,0,0.2381362915039062,0,0.2377548217773438,0,0.237945556640625,0,0.1460342407226562,0,0,0,0,0,0,0,-2.458183288574219,0.1719818115234375,0,0.178680419921875,0,0.18914794921875,0,0.198089599609375,0,0.2173919677734375,0,0.230926513671875,0.2375946044921875,0,0.2395248413085938,0.238494873046875,0,0,0.238311767578125,0,0.2386093139648438,0,0.149871826171875,0,0,0,0,0,0,0,0,-2.256179809570312,0,0.1707229614257812,0,0.1797409057617188,0.1780853271484375,0,0.1055908203125,0.1557159423828125,0,0.2061386108398438,0,0.219879150390625,0,0,0.2274169921875,0,0,0.2261810302734375,0,0.2335357666015625,0,0.2369613647460938,0,0.1854782104492188,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2.297035217285156,0.1363677978515625,0,0,0.1811447143554688,0.1791534423828125,0.19232177734375,0,0.1898345947265625,0,0.2016525268554688,0.2147140502929688,0,0.2281875610351562,0.234893798828125,0.2342758178710938,0,0.2346115112304688,0,0.1379241943359375,0,0,0,0,0,0,0,0,-2.19659423828125,0,0.170318603515625,0,0.180633544921875,0.188568115234375,0,0.1993408203125,0.2192153930664062,0,0.2312850952148438,0,0.2342300415039062,0,0.2335586547851562,0,0.2333602905273438,0.2342758178710938,0,0.13885498046875,0,0,0,-2.302406311035156,0.1632919311523438,0,0.1732025146484375,0,0.1863632202148438,0,0,0.1917800903320312,0,0.2105560302734375,0,0.2241439819335938,0,0.2377548217773438,0,0.236846923828125,0.2359848022460938,0.2355422973632812,0,0,0.2355422973632812,0.0374908447265625,0,0,0,0,0,-2.20391845703125,0,0.1718368530273438,0.1801605224609375,0,0.1895675659179688,0.219818115234375,0,0.2185211181640625,0,0.23419189453125,0,0.2356643676757812,0,0.2345123291015625,0.2355880737304688,0.2339096069335938,0,0.1151275634765625,0,0,0,0,0,-2.224220275878906,0,0.1675567626953125,0,0.1756591796875,0,0.187408447265625,0,0.1951751708984375,0.2112655639648438,0,0.2273712158203125,0,0.2381210327148438,0,0.2372283935546875,0,0.2362594604492188,0.2361831665039062,0,0.17584228515625,0,0,0,0,0,-2.043731689453125,0,0.173675537109375,0.1865310668945312,0,0.1946258544921875,0,0.2140579223632812,0,0.230804443359375,0,0.23828125,0,0.2361602783203125,0,0.2353057861328125,0.2350006103515625,0,0.16229248046875,0,0,0,0,0,0,0,0,-2.024398803710938,0,0.1731948852539062,0,0.1869354248046875,0.19091796875,0,0.2030258178710938,0.2212066650390625,0,0.2331008911132812,0.2361907958984375,0.2366485595703125,0.259002685546875,0,0.1460113525390625,0,0,0,0,0,0,0,0,-1.973731994628906,0,0.1744003295898438,0,0,0.1876144409179688,0,0.1954879760742188,0,0.2150802612304688,0,0.2306289672851562,0.2381210327148438,0.2374267578125,0.2368316650390625,0,0.2355422973632812,0.08347320556640625,0,0,0,0,0,-2.066246032714844,0,0.166351318359375,0.1767730712890625,0.1887664794921875,0,0.1993179321289062,0,0.24310302734375,0.2342605590820312,0.2378921508789062,0,0.2370529174804688,0.2366104125976562,0,0.20599365234375,0,0,0,0,0,0,0,0,-1.948814392089844,0.1742172241210938,0,0.1855010986328125,0.1933212280273438,0,0.2124862670898438,0,0.231475830078125,0,0.2405929565429688,0,0.2374496459960938,0.2367172241210938,0,0.235107421875,0,0,0.06087493896484375,0,0,0,0,0,-1.978675842285156,0,0.1905288696289062,0,0.1840744018554688,0,0.1931991577148438,0,0.2111358642578125,0,0.2267379760742188,0.2415771484375,0,0.2393951416015625,0,0.238250732421875,0,0.2374191284179688,0,0.07433319091796875,0,0,0,-1.958671569824219,0,0.1670150756835938,0,0.1778106689453125,0.1903228759765625,0.2026748657226562,0.2236099243164062,0,0.2370376586914062,0,0,0.2391510009765625,0.2382965087890625,0,0.234832763671875,0,0.1049270629882812,0,0,0,0,0,0,0,-1.94317626953125,0,0.1719818115234375,0,0.17919921875,0,0.1915664672851562,0.2044754028320312,0,0.223876953125,0,0.2377548217773438,0,0.2394180297851562,0.2385787963867188,0.2339096069335938,0.07861328125,0,0,0,-1.899513244628906,0.1720733642578125,0,0.182159423828125,0,0.193359375,0,0.2075881958007812,0.2249755859375,0,0.2414627075195312,0,0.2403945922851562,0,0.2388229370117188,0,0.2309112548828125,0.02288818359375,0,0,0,-1.81158447265625,0,0.1744842529296875,0,0.1866455078125,0,0.1953048706054688,0.2146224975585938,0,0.2230300903320312,0,0.2353591918945312,0,0.2280731201171875,0,0.227294921875,0.1811981201171875,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.86962890625,0,0,0.07861328125,0,0.1646194458007812,0,0.1783523559570312,0.1935348510742188,0.2076950073242188,0,0.2236251831054688,0.2403945922851562,0.2402496337890625,0.2302017211914062,0.1655807495117188,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.839271545410156,0,0,0,0,0,0.1664047241210938,0,0.1982345581054688,0.2047958374023438,0,0.2219772338867188,0,0.240753173828125,0,0.2608718872070312,0.2239532470703125,0.2126998901367188,0,0.2310943603515625,0,0.2290496826171875,0.2307052612304688,0,0.2369384765625,0.2416152954101562,0,0.2361373901367188,0,0.197235107421875,0,0.1964263916015625,0.1961288452148438,0,0.1965255737304688,0,0.1963729858398438,0,0.196533203125,0,0.1963348388671875,0,0.196075439453125,0.196533203125,0,0.1964187622070312,0.1965866088867188,0,0.1959991455078125,0.196533203125,0.1960067749023438,0.1937408447265625,0,0.1953048706054688,0,0.1963424682617188,0.1960220336914062,0,0.2158432006835938,0,0.1967010498046875,0,0.196014404296875,0,0.1958770751953125,0.1957778930664062,0,0.00737762451171875,0,0,0,0,0,0,0,0,-7.150520324707031,0,0,0.202301025390625,0,0.2088165283203125,0.2293624877929688,0,0.2423553466796875,0,0.2296981811523438,0,0.2177658081054688,0,0,0.2323455810546875,0,0.2400436401367188,0,0.238250732421875,0,0.2394180297851562,0,0.23980712890625,0.2390365600585938,0,0.238983154296875,0,0,0.2485198974609375,0.2484054565429688,0.2470703125,0,0.2726058959960938,0.2479248046875,0.2491073608398438,0,0.2486724853515625,0,0.2426605224609375,0,0.23760986328125,0,0.2376251220703125,0,0.23779296875,0.2381820678710938,0.2431488037109375,0.2403335571289062,0,0.235382080078125,0.2304000854492188,0,0.2262954711914062,0,0.2265396118164062,0,0.00403594970703125,0,0,0,0,0,-7.062309265136719,0.1990585327148438,0,0.2072067260742188,0,0,0.22125244140625,0,0.2349472045898438,0,0.2266082763671875,0.2163619995117188,0.2693405151367188,0,0.24053955078125,0,0.2372283935546875,0,0.2390289306640625,0,0,0.2394943237304688,0,0.2420196533203125,0,0.2497406005859375,0.2490997314453125,0.247772216796875,0,0.2490615844726562,0,0.248992919921875,0,0.2484817504882812,0,0.2484283447265625,0,0.2467727661132812,0.243316650390625,0,0.2466888427734375,0.2476806640625,0,0.2478485107421875,0.2474822998046875,0,0.243896484375,0,0.2479476928710938,0,0.2439804077148438,0.230224609375,0.2329788208007812,0,0.07527923583984375,0,0,0,0,0,0,0,0,-7.048011779785156,0,0.1875686645507812,0,0.1988296508789062,0,0.2028350830078125,0,0.2171249389648438,0,0.2219314575195312,0,0.213714599609375,0,0.2386474609375,0,0.2401199340820312,0,0.2374191284179688,0.2352447509765625,0,0.2360305786132812,0,0.2368316650390625,0.2376556396484375,0,0.2425613403320312,0,0.2424392700195312,0,0.2446823120117188,0.2458038330078125,0,0,0.2459869384765625,0,0.2462234497070312,0,0,0.2461624145507812,0,0.2456817626953125,0,0.24566650390625,0,0.2456207275390625,0.2460479736328125,0,0.269378662109375,0,0.2444305419921875,0,0.2449951171875,0,0.2465133666992188,0,0.2377700805664062,0,0.2354736328125,0,0.17181396484375,0,0,0,0,0,0,0,0,-6.98724365234375,0,0.18212890625,0,0.197235107421875,0,0.202362060546875,0,0,0.2137069702148438,0,0.214996337890625,0,0.2159805297851562,0,0.2412796020507812,0,0.2407302856445312,0.2365570068359375,0,0.2345962524414062,0.2341461181640625,0,0.2412643432617188,0,0.2384719848632812,0,0.240570068359375,0,0.2670745849609375,0,0.2428359985351562,0,0.2433853149414062,0,0.2346343994140625,0,0.2335739135742188,0,0.2342300415039062,0,0.2382888793945312,0,0.23358154296875,0,0.2396621704101562,0,0.2350845336914062,0.2412261962890625,0.2454452514648438,0,0,0.2451934814453125,0.2453079223632812,0.238616943359375,0,0.2332382202148438,0.2017440795898438,0,0,0,0,0,0,0,0,0,0,0,-6.730880737304688,0,0,0.1951217651367188,0,0.2014694213867188,0,0.2076187133789062,0.212432861328125,0.2407684326171875,0,0.2414398193359375,0,0.2402877807617188,0,0.2377090454101562,0,0.2340850830078125,0.2391815185546875,0,0.238006591796875,0.2374191284179688,0.2422637939453125,0,0.2363357543945312,0.23785400390625,0,0.2421188354492188,0,0.2443389892578125,0.2444000244140625,0,0.2430191040039062,0,0,0.24053955078125,0,0.2441253662109375,0,0.2451629638671875,0,0.2446212768554688,0.2452621459960938,0,0.2454910278320312,0,0.2456512451171875,0,0.2460174560546875,0.2334213256835938,0,0.2339096069335938,0,0.0874176025390625,0,0,0,0,0,0,0,-6.698066711425781,0,0.2013397216796875,0.2030258178710938,0.213836669921875,0,0.2113265991210938,0,0.228546142578125,0.2406234741210938,0,0.2412872314453125,0,0.2395858764648438,0.237548828125,0,0,0.2411422729492188,0,0.2372360229492188,0,0.2380828857421875,0,0.2386322021484375,0.2455825805664062,0.2459945678710938,0.2450714111328125,0,0.2694854736328125,0.2457504272460938,0,0,0.2456512451171875,0,0,0.2457122802734375,0.2462005615234375,0.2468719482421875,0,0.2470169067382812,0.2472457885742188,0,0.2427597045898438,0.2353668212890625,0.2323760986328125,0.2269287109375,0,0.2338714599609375,0.0175018310546875,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-6.658134460449219,0,0,0,0.1030654907226562,0,0.19195556640625,0.1972503662109375,0,0.1960601806640625,0,0.1999740600585938,0,0.2323455810546875,0,0.239349365234375,0,0.2284698486328125,0,0.2265243530273438,0,0.2237472534179688,0,0.2293548583984375,0,0,0.2379684448242188,0,0.23797607421875,0.2343597412109375,0,0.2374191284179688,0.238189697265625,0.2360153198242188,0.2374114990234375,0,0.2379074096679688,0,0.2384490966796875,0,0.2625503540039062,0,0,0.2394866943359375,0,0.2402267456054688,0,0.2400588989257812,0,0.2410964965820312,0.2410202026367188,0.240325927734375,0,0.2391815185546875,0,0.2393646240234375,0,0.2400360107421875,0,0,0.02123260498046875,0,0,0,0,0,0,0,0,0,0,0,-6.456642150878906,0,0.1875762939453125,0,0.1939010620117188,0.1901092529296875,0.1954803466796875,0.2273712158203125,0,0.239044189453125,0.2366714477539062,0,0.23529052734375,0,0.23443603515625,0,0.2348556518554688,0,0.2340545654296875,0,0.2600860595703125,0.2420883178710938,0.23919677734375,0,0,0.244964599609375,0,0.2439651489257812,0.2420806884765625,0,0.242156982421875,0.2339096069335938,0,0.2368927001953125,0,0.2378463745117188,0.2361907958984375,0.2366409301757812,0,0.2372665405273438,0,0.2354812622070312,0,0.2414398193359375,0.2453536987304688,0,0.244842529296875,0.1348495483398438,0,0,0,0,0,-6.439956665039062,0,0.1751708984375,0,0.1905441284179688,0,0.1879653930664062,0.2103424072265625,0,0.2236099243164062,0.2398300170898438,0,0.2377700805664062,0,0,0.2344131469726562,0,0.2339096069335938,0.2320480346679688,0.2335357666015625,0,0.2337112426757812,0,7.684379577636719,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7.62939453125,0,0,7.62939453125e-06,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,15.2587890625,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7.629417419433594,0,0,0,0,0,0,0,0.1338653564453125,0,0,0,0,15.26132965087891,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"filename":["<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,null,"<expr>","<expr>",null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,null,null,null,null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,null,null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,null,null,null,null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,null,null,null,null,null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,null,null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>","<expr>",null,null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,null,"<expr>","<expr>",null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,null,null,null,null,null,null,null,null,"<expr>","<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null]},"interval":10,"files":[{"filename":"<expr>","content":"## Generate Large Random Dataset\nn <- 2e6\nx <- runif(n)\ny <- runif(n)\nz <- runif(n)\nXYZ <- cbind(x,y,z)\n\n## Inspect 4 equivalent `row mean` calculations \nprofvis::profvis({\n    m <- rowSums(XYZ)/ncol(XYZ)\n    m <- rowMeans(XYZ)\n    m <- apply(XYZ, 1, mean)\n    m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }\n})\n## rowSums(), colSums(), rowMeans(), and colMeans() are vectorised and fast.\n## for loop is not the slowest, but the ugliest.","normpath":"<expr>"}],"prof_output":"/tmp/RtmpCyELZx/file27a48193371.prof","highlight":{"output":["^output\\$"],"gc":["^<GC>$"],"stacktrace":["^\\.\\.stacktraceo(n|ff)\\.\\.$"]},"split":"h"}},"evals":[],"jsHooks":[]}</script>
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
## 1 mean1(x, 0.5)     36ms   37.1ms      27.0    7.63MB     0   
## 2 mean2(x, 0.5)   32.6ms   35.7ms      28.3    7.63MB     2.18
## 3 mean3(x, 0.5)   37.1ms   37.1ms      26.8    7.63MB     0
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
##   0.119   0.000   0.043
```

```r
system.time({ lm(Y~X, data=DAT) })
```

```
##    user  system elapsed 
##   0.526   0.000   0.184
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
## 1 ma1(y)      277.1ms  277.1ms      3.61    15.3MB     3.61
## 2 ma2(y)       29.4ms   29.7ms     33.7     91.6MB   185.
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
##   0.034   0.004   0.037
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
##   1.215   0.368   0.886
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





