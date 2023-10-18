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
<div class="plotly html-widget html-fill-item-overflow-hidden html-fill-item" id="htmlwidget-5c2adeea4c73ce0e769c" style="width:672px;height:480px;"></div>
<script type="application/json" data-for="htmlwidget-5c2adeea4c73ce0e769c">{"x":{"visdat":{"16c7a8e7e85":["function () ","plotlyVisDat"]},"cur_data":"16c7a8e7e85","attrs":{"16c7a8e7e85":{"x":{},"y":{},"alpha_stroke":1,"sizes":[10,100],"spans":[1,20]}},"layout":{"margin":{"b":40,"l":60,"t":25,"r":10},"xaxis":{"domain":[0,1],"automargin":true,"title":"X"},"yaxis":{"domain":[0,1],"automargin":true,"title":"Y"},"hovermode":"closest","showlegend":false},"source":"A","config":{"modeBarButtonsToAdd":["hoverclosest","hovercompare"],"showSendToCloud":false},"data":[{"x":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100],"y":[2.9516446911220715,8.7475075586209829,11.017565686748828,16.377136986684985,21.837257742572277,22.241122753574952,31.491031575871233,32.322846576303007,35.687444604313981,38.616100802914566,43.158854910329211,47.580173175856174,52.951335997556406,55.913373091349044,58.596248822939195,66.008557100984405,68.558349425906329,72.470935730777654,73.766847116932837,83.041203489799017,87.80158029483357,89.02937224716554,91.219520905746151,95.083206139867016,103.01389379479967,104.89514764523832,104.87646139087585,109.99810575180859,115.12258486987015,121.23743506998298,121.63474613329846,123.38729232677814,133.11130181633649,137.23062916983412,141.06700492710681,141.94179550285801,145.96215009353065,149.9064018722579,155.29182678553354,160.48004322084674,165.07162555232955,166.89281015817218,170.6922732731361,177.80864754542017,180.9645742910007,186.5656013643968,191.55400236022564,195.15956692232055,192.24507162149956,201.17533429289506,202.0824343775019,209.20620173079675,208.52208152722801,216.67007176838229,219.61646112036701,223.93471057893689,227.55976870720539,231.99979495849109,233.46656642965871,244.61191390925293,240.77718201308619,249.92054846558361,250.78783390853886,254.93619647136791,256.90168984512673,265.03156326832055,266.62360582004408,269.85327183726429,277.31582583398608,283.25916004909561,281.88191774131246,287.57641989546465,291.15214473221783,298.34302059177219,303.6755502021494,301.25397651384156,311.22807154936419,312.46167553003357,315.42594059762155,318.27157195167621,323.48963614847969,327.83042543838064,332.92168959929137,336.48773229976047,340.60702311410574,342.99605189012112,350.54225417930911,353.52632919710737,358.86664154203982,362.47539383427062,366.26052038440656,368.75062698290242,370.54155223241816,375.83907892182492,377.82383248328648,387.65536097380351,387.33194935950905,392.63226263921564,399.08656677882851,397.58687304058549],"type":"scatter","mode":"markers","marker":{"color":"rgba(31,119,180,1)","line":{"color":"rgba(31,119,180,1)"}},"error_y":{"color":"rgba(31,119,180,1)"},"error_x":{"color":"rgba(31,119,180,1)"},"line":{"color":"rgba(31,119,180,1)"},"xaxis":"x","yaxis":"y","frame":null}],"highlight":{"on":"plotly_click","persistent":false,"dynamic":false,"selectize":false,"opacityDim":0.20000000000000001,"selected":{"opacity":1},"debounce":0},"shinyEvents":["plotly_hover","plotly_click","plotly_selected","plotly_relayout","plotly_brushed","plotly_brushing","plotly_clickannotation","plotly_doubleclick","plotly_deselect","plotly_afterplot","plotly_sunburstclick"],"base_url":"https://plot.ly"},"evals":[],"jsHooks":[]}</script>
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
##           used (Mb) gc trigger (Mb) max used  (Mb)
## Ncells 1209852 64.7    2359047  126  2359047 126.0
## Vcells 2294773 17.6    8388608   64  3574525  27.3
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
##   0.005   0.000   0.006
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
<div class="profvis html-widget html-fill-item-overflow-hidden html-fill-item" id="htmlwidget-1fdc3ff69b546abb1755" style="width:100%;height:600px;"></div>
<script type="application/json" data-for="htmlwidget-1fdc3ff69b546abb1755">{"x":{"message":{"prof":{"time":[1,2,3,4,5,6,7,8,9,10,11,12,13,13,14,14,15,15,16,16,17,17,18,18,19,19,20,20,21,21,22,22,23,23,24,24,25,25,26,26,27,27,28,28,29,29,30,31,31,32,33,33,33,34,34,35,35,36,36,37,38,39,39,40,41,41,42,43,43,43,44,44,44,45,45,46,46,47,47,47,48,49,49,50,51,51,52,52,53,53,54,54,55,55,56,56,57,58,58,58,59,59,59,60,61,61,62,63,63,63,64,65,65,65,66,67,67,68,69,69,70,70,71,71,72,73,73,73,73,74,74,75,75,76,76,77,77,78,78,78,79,80,80,81,81,82,82,83,83,84,85,85,86,87,87,87,88,89,90,91,92,92,93,93,94,94,95,95,96,97,98,98,99,100,101,101,101,101,102,103,104,105,105,106,107,107,108,109,109,110,110,111,112,112,113,113,114,114,115,115,115,116,116,117,118,118,119,119,120,120,121,121,122,122,123,123,124,124,125,125,126,127,127,128,128,129,129,129,130,131,131,132,132,133,133,134,134,134,135,135,136,136,137,137,138,139,139,140,140,141,142,142,142,143,143,143,144,145,146,146,147,147,147,148,148,149,149,149,150,151,151,152,152,153,153,154,154,155,156,156,156,157,157,158,158,159,160,161,161,161,162,162,163,163,164,164,165,165,165,166,166,167,167,168,168,169,169,170,170,171,171,172,173,173,174,174,175,175,176,176,177,177,178,179,180,180,181,181,182,182,182,183,183,183,184,185,186,186,187,188,188,189,189,189,190,191,191,191,192,192,193,193,194,194,195,195,195,196,197,197,198,198,199,200,200,201,202,203,204,205,206,207,207,208,208,208,209,209,210,211,211,211,212,212,212,213,214,214,215,215,216,216,217,218,218,218,219,220,220,221,221,221,222,222,222,223,223,224,224,225,226,226,227,227,228,228,229,229,230,230,231,232,233,233,233,234,235,235,236,237,238,239,239,240,241,241,242,242,243,243,244,244,245,245,245,245,246,246,246,246,247,247,247,248,248,249,250,250,251,252,252,253,254,254,255,255,256,256,257,257,257,258,258,258,259,260,260,261,261,262,262,263,263,264,264,265,265,266,267,267,267,268,268,269,269,270,270,270,271,271,272,273,274,274,275,275,276,277,277,278,279,280,280,281,282,282,282,283,284,284,285,285,285,286,287,287,288,289,289,290,291,292,293,293,294,294,294,295,296,296,296,297,298,298,299,299,300,300,301,301,302,303,304,304,305,305,305,306,306,306,307,307,307,308,308,308,309,309,309,310,310,310,311,311,311,312,312,312,313,313,313,314,314,314,315,315,315,316,316,317,317,318,319,320,320,321,322,323,324,324,325,325,326,326,327,327,328,328,329,329,330,330,331,332,332,333,333,334,334,335,335,336,337,338,338,339,339,340,340,341,342,342,342,343,343,344,344,345,346,346,347,347,348,349,349,350,350,350,351,351,352,352,353,353,354,354,355,355,356,357,357,358,358,358,359,359,360,360,361,361,361,362,363,364,364,364,365,365,366,366,367,367,368,368,369,369,369,370,370,371,371,372,372,372,373,374,374,375,376,377,378,378,379,380,380,381,382,382,383,383,383,384,384,385,385,386,386,387,387,388,388,389,390,391,391,392,393,393,393,394,394,394,395,396,397,398,399,400,401,401,402,402,403,403,404,404,404,405,405,406,406,407,408,408,409,410,410,411,411,412,412,413,414,414,415,415,416,416,417,417,418,419,419,420,420,421,421,422,422,423,423,424,424,425,425,426,426,426,427,427,428,428,429,429,430,430,431,431,431,432,432,433,433,434,434,435,435,436,436,436,437,438,438,439,440,441,441,442,442,443,444,444,444,444,445,445,445,445,446,447,447,448,448,449,449,450,450,451,452,452,452,453,453,454,454,454,455,455,455,456,457,457,458,458,459,460,460,461,461,462,463,463,464,464,464,465,466,467,468,469,470,470,471,471,472,472,473,473,474,474,474,475,475,476,476,477,478,478,479,479,480,480,481,481,482,483,483,483,484,484,484,485,485,486,486,486,487,488,488,489,489,490,491,491,492,492,492,493,493,494,494,494,495,495,496,496,497,497,497,498,499,500,500,501,502,502,503,503,504,504,504,505,506,506,507,507,508,508,509,510,511,511,511,511,512,513,513,514,514,515,515,516,516,516,517,518,519,519,520,520,521,522,523,524,524,525,525,526,526,526,527,528,529,529,530,530,531,531,532,532,533,533,534,534,535,535,536,536,537,537,538,538,539,539,540,540,541,541,542,542,543,543,544,544,545,545,546,546,547,547,548,548,549,549,550,550,551,551,552,552,553,553,554,554,555,555,556,556,557,557,558,558,559,559,560,560,561,561,562,562,563,563,564,564,565,565,566,567,567,568,568,569,570,571,572,572,573,573,574,575,576,576,577,577,578,578,579,580,580,580,581,582,582,582,583,583,584,585,585,586,586,587,587,588,588,589,589,590,590,591,592,593,594,595,596,596,597,598,598,598,599,599,600,600,601,601,602,603,604,605,605,605,606,606,607,607,608,608,609,609,610,610,610,611,611,612,612,612,613,613,614,614,614,615,615,616,616,617,617,618,619,619,620,620,621,621,622,622,622,623,623,623,624,625,625,626,626,626,627,627,627,628,628,629,629,630,630,630,631,631,632,633,633,633,634,634,635,636,637,637,638,638,638,639,640,640,641,641,642,642,643,643,643,644,644,645,646,646,647,648,648,648,649,649,649,650,650,650,651,652,652,653,653,654,655,655,656,656,657,657,658,658,659,659,660,661,662,662,663,663,664,664,664,665,665,666,666,667,667,668,668,669,669,669,670,670,670,671,671,672,672,673,673,674,674,675,676,677,677,678,679,679,680,681,681,682,682,683,683,684,684,685,685,686,686,687,687,688,689,689,690,690,690,691,691,691,692,692,693,694,694,695,696,696,697,697,698,698,699,699,700,701,702,703,704,704,705,705,706,706,707,708,708,709,710,710,711,711,712,712,713,714,714,714,715,716,717,717,718,718,719,720,720,721,722,722,723,723,724,724,725,725,726,726,727,727,728,728,729,729,730,730,730,731,731,732,732,733,733,734,735,735,736,736,737,737,738,738,738,739,740,740,741,741,742,743,743,744,744,745,745,746,746,747,747,748,748,749,749,749,750,750,751,751,751,752,752,752,753,753,754,754,755,755,756,756,756,757,757,758,758,759,760,761,761,762,762,763,764,765,766,766,767,767,768,769,770,770,770,771,771,771,772,772,773,773,774,775,775,776,776,776,777,778,778,779,779,780,780,780,781,782,783,783,784,785,786,786,787,787,788,788,789,789,790,790,790,791,791,791,792,792,793,793,794,794,795,795,795,796,796,797,797,798,799,799,800,800,801,801,801,802,802,803,804,804,805,806,807,807,808,808,809,810,810,810,811,811,811,812,812,813,813,814,815,816,817,817,818,818,818,819,820,820,821,821,822,822,823,823,824,824,825,826,826,827,827,828,828,829,829,829,829,830,830,830,830,831,832,832,833,834,835,836,836,837,837,838,838,839,840,840,841,841,842,842,843,843,843,844,845,845,846,846,847,848,848,849,849,850,851,851,852,853,854,854,855,855,856,856,856,857,857,858,858,859,860,860,861,862,862,862,863,863,864,865,865,866,867,867,868,868,869,869,870,870,871,871,872,872,873,873,874,874,875,875,876,877,877,878,878,879,879,880,880,881,881,882,883,883,884,884,885,885,885,886,886,886,887,888,888,889,889,890,890,891,891,892,893,893,894,894,895,895,895,896,896,897,897,898,898,899,899,900,900,901,901,901,902,902,903,903,903,904,904,904,905,906,907,908,909,909,910,910,911,912,913,913,914,914,915,916,916,917,917,918,918,919,920,921,921,921,922,922,922,923,924,924,925,925,926,926,927,928,928,929,929,930,931,931,932,932,933,933,934,934,935,935,936,937,937,938,938,939,939,940,940,941,941,941,942,943,944,944,945,945,946,946,947,947,947,948,948,948,949,950,950,951,951,951,952,952,953,954,955,955,955,956,956,957,957,957,958,958,958,959,959,960,960,961,961,962,962,963,963,964,965,966,966,967,967,968,968,969,969,970,970,971,971,972,972,973,974,975,975,975,975,976,976,976,976,977,977,977,977,978,978,978,978,979,979,979,979,980,980,980,980,981,981,981,981,982,982,982,982,983,983,983,983,984,984,984,984,985,985,985,985,986,986,986,986,987,987,987,987,988,988,988,988,989,989,989,989,990,990,990,990,991,991,992,992,993,994,994,995,995,996,996,997,998,999,1000,1000,1001,1002,1003,1003,1004,1005,1006,1006,1007,1007,1007,1008,1008,1008,1009,1010,1010,1010,1011,1011,1011,1012,1012,1013,1014,1014,1015,1016,1017,1018,1018,1019,1019,1020,1020,1021,1021,1022,1023,1023,1024,1024,1024,1024,1025,1025,1025,1025,1026,1026,1027,1027,1028,1029,1029,1030,1030,1031,1031,1031,1032,1032,1032,1033,1034,1034,1034,1035,1035,1036,1037,1037,1038,1038,1039,1040,1041,1041,1042,1042,1043,1043,1044,1044,1045,1046,1046,1046,1047,1048,1048,1049,1049,1050,1050,1051,1051,1052,1052,1053,1053,1054,1054,1055,1055,1056,1056,1057,1058,1058,1058,1059,1059,1059,1060,1061,1062,1062,1063,1063,1064,1065,1065,1066,1066,1067,1068,1068,1069,1069,1070,1070,1071,1072,1072,1073,1073,1074,1074,1075,1075,1076,1076,1077,1077,1077,1078,1079,1080,1080,1081,1081,1082,1082,1082,1083,1084,1085,1086,1086,1087,1088,1089,1089,1090,1091,1091,1091,1092,1092,1092,1093,1094,1095,1095,1096,1096,1097,1097,1098,1099,1099,1100,1100,1100,1101,1102,1102,1103,1103,1104,1104,1105,1105,1106,1107,1107,1108,1108,1109,1109,1110,1111,1111,1112,1112,1112,1113,1114,1115,1116,1116,1117,1118,1119,1120,1120,1121,1121,1121,1122,1123,1123,1123,1124,1124,1124,1125,1125,1126,1126,1126,1127,1128,1128,1129,1130,1130,1130,1131,1131,1132,1133,1133,1134,1134,1135,1136,1136,1137,1137,1138,1138,1139,1139,1139,1140,1140,1140,1141,1141,1142,1143,1143,1144,1144,1145,1145,1146,1147,1147,1148,1149,1149,1150,1150,1150,1151,1152,1152,1153,1153,1154,1154,1154,1155,1155,1155,1156,1156,1157,1158,1159,1159,1160,1160,1161,1161,1162,1162,1163,1163,1164,1164,1165,1165,1166,1166,1167,1167,1168,1168,1169,1169,1169,1170,1170,1170,1171,1172,1172,1172,1173,1174,1175,1176,1176,1177,1178,1178,1179,1180,1181,1182,1182,1183,1184,1184,1185,1185,1186,1186,1186,1187,1188,1188,1189,1190,1190,1191,1191,1191,1192,1193,1194,1194,1195,1195,1196,1196,1197,1197,1198,1198,1199,1199,1199,1200,1200,1200,1201,1201,1202,1203,1203,1204,1204,1205,1205,1206,1206,1207,1207,1208,1209,1209,1210,1210,1211,1211,1212,1213,1214,1214,1214,1215,1215,1215,1216,1216,1216,1217,1218,1218,1219,1220,1221,1222,1222,1223,1223,1224,1224,1225,1225,1226,1226,1227,1228,1229,1229,1229,1230,1230,1230,1231,1231,1232,1232,1233,1233,1234,1235,1235,1236,1236,1237,1237,1238,1238,1239,1240,1240,1241,1241,1242,1242,1243,1244,1244,1245,1245,1246,1246,1247,1247,1248,1248,1249,1250,1250,1251,1252,1252,1252,1253,1253,1254,1254,1255,1256,1256,1257,1257,1258,1258,1258,1259,1259,1259,1260,1260,1261,1262,1263,1263,1264,1264,1265,1265,1265,1266,1267,1267,1267,1268,1269,1270,1270,1271,1271,1272,1272,1273,1273,1274,1275,1275,1276,1276,1277,1278,1278,1279,1279,1280,1280,1280,1281,1281,1282,1282,1283,1283,1284,1284,1284,1285,1286,1286,1286,1287,1287,1287,1288,1289,1289,1290,1291,1291,1292,1293,1294,1295,1296,1297,1297,1298,1298,1298,1299,1300,1300,1301,1301,1302,1303,1304,1304,1305,1305,1306,1306,1307,1307,1308,1309,1309,1310,1310,1311,1311,1312,1312,1313,1313,1314,1314,1315,1315,1316,1316,1317,1317,1318,1318,1319,1319,1320,1320,1321,1321,1322,1322,1323,1323,1324,1324,1325,1325,1326,1326,1326,1327,1327,1328,1329,1329,1330,1330,1331,1331,1332,1332,1333,1333,1333,1334,1334,1335,1335,1336,1336,1336,1337,1337,1338,1338,1339,1339,1339,1340,1340,1341,1341,1342,1342,1343,1343,1344,1344,1344,1345,1345,1345,1346,1346,1347,1348,1348,1349,1350,1350,1351,1351,1352,1352,1353,1353,1354,1354,1354,1355,1355,1356,1356,1357,1358,1358,1359,1359,1360,1360,1361,1361,1361,1362,1362,1363,1363,1363,1364,1364,1364,1365,1365,1366,1367,1367,1368,1368,1369,1369,1370,1370,1371,1371,1372,1372,1373,1373,1374,1374,1375,1375,1375,1376,1376,1376,1377,1377,1377,1378,1378,1379,1380,1380,1381,1381,1381,1382,1382,1383,1384,1384,1385,1385,1386,1386,1387,1387,1388,1388,1388,1389,1389,1389,1390,1390,1391,1391,1391,1392,1392,1393,1394,1394,1395,1395,1396,1396,1397,1397,1398,1398,1399,1400,1400,1401,1401,1402,1402,1403,1403,1404,1404,1405,1406,1406,1407,1408,1409,1410,1411,1412,1412,1413,1413,1413,1414,1414,1414,1415,1415,1416,1416,1417,1418,1418,1419,1420,1420,1421,1422,1422,1423,1424,1425,1425,1425,1426,1426,1426,1427,1427,1428,1429,1429,1430,1430,1431,1431,1432,1432,1432,1433,1433,1434,1434,1435,1435,1436,1437,1437,1438,1438,1439,1439,1439,1440,1441,1441,1442,1442,1443,1444,1445,1445,1446,1446,1447,1447,1448,1448,1449,1449,1449,1450,1450,1450,1451,1452,1452,1453,1454,1455,1456,1456,1457,1457,1458,1458,1459,1460,1461,1461,1462,1462,1463,1463,1464,1465,1466,1466,1467,1467,1467,1468,1468,1469,1470,1471,1472,1472,1473,1473,1473,1474,1474,1474,1475,1475,1476,1476,1477,1477,1477,1478,1479,1479,1480,1480,1480,1481,1481,1482,1482,1483,1483,1484,1484,1485,1485,1486,1486,1487,1487,1488,1488,1489,1489,1490,1490,1491,1491,1491,1492,1493,1493,1494,1495,1496,1496,1496,1497,1497,1497,1498,1498,1499,1499,1500,1500,1501,1502,1502,1502,1503,1504,1504,1505,1505,1506,1507,1507,1507,1508,1508,1508,1509,1509,1509,1510,1510,1510,1511,1511,1511,1512,1512,1512,1513,1513,1513,1514,1514,1514,1515,1516,1516,1517,1517,1518,1519,1520,1520,1521,1521,1522,1522,1523,1523,1524,1524,1525,1525,1526,1526,1527,1527,1528,1528,1529,1529,1530,1530,1531,1531,1532,1532,1533,1533,1534,1534,1535,1535,1536,1536,1537,1537,1538,1538,1539,1539,1540,1540,1541,1541,1542,1542,1543,1543,1544,1544,1545,1545,1546,1546,1547,1547,1548,1548,1549,1549,1550,1550,1551,1551,1552,1552,1553,1553,1554,1554,1555,1555,1556,1556,1557,1557,1558,1558,1559,1559,1560,1560,1561,1561,1562,1562,1563,1563,1564,1564,1565,1565,1566,1566,1567,1567,1568,1568,1569,1569,1570,1570,1571,1571,1572,1572,1573,1573,1574,1574,1575,1575,1576,1576,1577,1577,1578,1578,1579,1579,1580,1580,1581,1581,1582,1582,1583,1583,1584,1584,1585,1585,1586,1586,1587,1587,1588,1588,1589,1589,1590,1590,1590,1591,1591,1592,1592,1593,1593,1594,1594,1595,1595,1595,1596,1597,1598,1598,1599,1599,1600,1600,1601,1601,1602,1602,1603,1603,1604,1604,1605,1605,1606,1607,1607,1607,1608,1608,1609,1609,1610,1611,1611,1612,1613,1613,1614,1614,1615,1616,1616,1617,1618,1618,1619,1619,1620,1621,1621,1621,1622,1622,1623,1623,1624,1624,1624,1625,1625,1626,1627,1627,1628,1628,1629,1629,1630,1630,1631,1631,1631,1632,1632,1633,1633,1634,1634,1635,1635,1636,1636,1637,1638,1638,1639,1639,1640,1640,1641,1642,1642,1643,1643,1644,1644,1645,1645,1645,1646,1647,1647,1648,1648,1649,1649,1650,1650,1651,1651,1651,1652,1652,1653,1653,1654,1654,1655,1656,1656,1657,1657,1658,1659,1659,1660,1661,1662,1662,1663,1663,1663,1664,1664,1664,1665,1665,1665,1666,1666,1666,1667,1668,1668,1669,1669,1670,1670,1671,1671,1672,1672,1673,1673,1674,1674,1675,1675,1676,1676,1677,1678,1679,1680,1680,1681,1681,1682,1682,1683,1683,1684,1685,1685,1686,1686,1687,1687,1688,1689,1689,1689,1690,1691,1691,1692,1693,1694,1694,1695,1695,1695,1696,1696,1697,1698,1698,1699,1699,1700,1700,1701,1701,1702,1703,1704,1704,1705,1705,1706,1706,1706,1707,1707,1708,1708,1709,1709,1710,1711,1711,1712,1712,1713,1713,1714,1714,1715,1715,1715,1716,1716,1717,1717,1718,1718,1719,1720,1720,1721,1721,1722,1722,1723,1723,1724,1724,1725,1726,1726,1727,1727,1728,1728,1729,1730,1730,1731,1731,1731,1732,1732,1733,1733,1733,1734,1734,1734,1735,1735,1735,1736,1736,1737,1737,1738,1738,1739,1739,1740,1740,1741,1742,1742,1743,1743,1743,1744,1745,1745,1746,1746,1747,1747,1748,1749,1749,1750,1751,1751,1752,1752,1753,1754,1755,1756,1756,1757,1757,1758,1758,1759,1759,1760,1760,1760,1761,1761,1762,1763,1764,1764,1765,1766,1766,1767,1767,1768,1768,1768,1769,1769,1769,1770,1770,1770,1771,1771,1772,1773,1774,1774,1775,1775,1776,1776,1776,1777,1777,1777,1778,1778,1779,1779,1780,1780,1780,1781,1781,1781,1782,1782,1783,1783,1783,1784,1784,1785,1785,1786,1786,1787,1787,1788,1788,1789,1789,1790,1791,1791,1792,1792,1793,1794,1794,1795,1795,1796,1796,1796,1797,1798,1798,1799,1800,1800,1801,1801,1802,1802,1803,1803,1804,1804,1805,1805,1806,1806,1807,1807,1807,1808,1808,1809,1809,1810,1811,1812,1813,1814,1815,1815,1816,1817,1817,1818,1819,1819,1820,1821,1822,1822,1823,1823,1824,1825,1825,1826,1826,1827,1827,1828,1829,1829,1830,1830,1831,1831,1832,1832,1832,1833,1833,1834,1835,1835,1835,1836,1836,1836,1837,1837,1837,1838,1838,1838,1839,1839,1839,1840,1840,1840,1841,1841,1841,1842,1842,1842,1843,1843,1843,1844,1844,1844,1845,1845,1845,1846,1846,1846,1847,1848,1848,1849,1849,1850,1850,1851,1852,1853,1854,1854,1855,1856,1856,1857,1858,1858,1859,1859,1860,1860,1861,1862,1862,1863,1864,1864,1864,1865,1865,1866,1867,1868,1869,1869,1869,1870,1870,1871,1871,1872,1872,1873,1873,1874,1875,1875,1876,1877,1877,1877,1878,1878,1878,1879,1879,1879,1880,1880,1881,1882,1882,1883,1884,1884,1885,1885,1886,1886,1887,1887,1887,1888,1889,1889,1890,1891,1891,1892,1892,1893,1894,1894,1895,1896,1896,1897,1897,1898,1899,1900,1900,1901,1902,1902,1903,1903,1904,1904,1904,1905,1905,1906,1907,1907,1908,1908,1909,1909,1910,1910,1911,1911,1912,1912,1913,1913,1914,1915,1915,1916,1916,1917,1917,1918,1919,1920,1921,1921,1922,1922,1923,1923,1924,1924,1925,1925,1926,1926,1926,1927,1927,1928,1928,1929,1929,1930,1930,1931,1931,1932,1932,1933,1933,1934,1934,1935,1935,1936,1936,1937,1937,1938,1938,1939,1939,1940,1940,1941,1941,1942,1943,1943,1944,1944,1945,1945,1946,1946,1947,1947,1948,1948,1949,1949,1950,1950,1951,1951,1952,1952,1953,1953,1954,1954,1955,1955,1956,1956,1957,1957,1958,1958,1959,1959,1960,1960,1961,1961,1962,1962,1963,1963,1964,1964,1965,1965,1965,1965,1965,1965,1965,1965,1966,1966,1966,1966,1966,1966,1966,1966,1966,1966,1966,1966,1966,1966,1966,1966,1966,1966,1966,1966,1966,1967,1967,1967,1967,1967,1967,1967,1967,1968,1968,1968,1968,1968,1968,1968,1968,1969,1969,1969,1969,1969,1969,1969,1969,1970,1970,1970,1970,1970,1970,1970,1970,1971,1971,1971,1971,1971,1971,1971,1971,1972,1972,1972,1972,1972,1972,1972,1972,1973,1973,1973,1973,1973,1973,1973,1973,1974,1974,1974,1974,1974,1974,1974,1974,1975,1975,1975,1975,1975,1975,1975,1975,1976,1976,1976,1976,1976,1976,1976,1976,1977,1977,1977,1977,1977,1977,1977,1977,1978,1978,1978,1978,1978,1978,1978,1978,1979,1979,1979,1979,1979,1979,1979,1979,1980,1980,1980,1980,1980,1980,1980,1980,1981,1981,1981,1981,1981,1981,1981,1981,1982,1982,1982,1982,1982,1982,1982,1982,1983,1983,1983,1983,1983,1983,1983,1983,1984,1984,1984,1984,1984,1984,1984,1984,1985,1985,1985,1985,1985,1985,1985,1985,1986,1986,1986,1986,1986,1986,1986,1986,1987,1987,1987,1987,1987,1987,1987,1987,1988,1988,1988,1988,1988,1988,1988,1988,1989,1989,1989,1989,1989,1989,1989,1989,1990,1990,1990,1990,1990,1990,1990,1990,1991,1991,1991,1991,1991,1991,1991,1991,1992,1992,1992,1992,1992,1992,1992,1992,1993,1993,1993,1993,1993,1993,1993,1993,1994,1994,1994,1994,1994,1994,1994,1994,1995,1995,1995,1995,1995,1995,1995,1995,1996,1996,1996,1996,1996,1996,1996,1996],"depth":[1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,3,2,1,2,1,2,1,2,1,1,1,2,1,1,2,1,1,3,2,1,3,2,1,2,1,2,1,3,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,1,2,1,1,3,2,1,1,3,2,1,1,2,1,1,2,1,2,1,2,1,1,4,3,2,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,2,1,1,2,1,1,3,2,1,1,1,1,1,2,1,2,1,2,1,2,1,1,1,2,1,1,1,4,3,2,1,1,1,1,2,1,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,1,3,2,1,3,2,1,1,1,2,1,3,2,1,2,1,3,2,1,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,1,1,3,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,3,2,1,3,2,1,1,1,2,1,1,2,1,3,2,1,1,3,2,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,1,2,1,1,1,1,1,1,1,2,1,3,2,1,2,1,1,3,2,1,3,2,1,1,2,1,2,1,2,1,1,3,2,1,1,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,1,3,2,1,1,2,1,1,1,1,2,1,1,2,1,2,1,2,1,2,1,4,3,2,1,4,3,2,1,3,2,1,2,1,1,2,1,1,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,3,2,1,2,1,1,1,2,1,2,1,1,2,1,1,1,2,1,1,3,2,1,1,2,1,3,2,1,1,2,1,1,2,1,1,1,1,2,1,3,2,1,1,3,2,1,1,2,1,2,1,2,1,2,1,1,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,1,1,2,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,1,2,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,2,1,2,1,3,2,1,1,1,3,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,3,2,1,1,2,1,1,1,1,2,1,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,1,3,2,1,3,2,1,1,1,1,1,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,1,1,2,1,2,1,1,4,3,2,1,4,3,2,1,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,3,2,1,3,2,1,1,2,1,2,1,1,2,1,2,1,1,2,1,3,2,1,1,1,1,1,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,2,1,3,2,1,1,2,1,2,1,1,2,1,3,2,1,2,1,3,2,1,2,1,2,1,3,2,1,1,1,2,1,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,1,1,4,3,2,1,1,2,1,2,1,2,1,3,2,1,1,1,2,1,2,1,1,1,1,2,1,2,1,3,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,1,1,2,1,2,1,1,1,2,1,2,1,2,1,1,3,2,1,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,1,1,1,2,1,1,3,2,1,2,1,2,1,2,1,1,1,1,3,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,3,2,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,1,2,1,3,2,1,3,2,1,2,1,2,1,3,2,1,2,1,1,3,2,1,2,1,1,1,2,1,3,2,1,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,1,3,2,1,3,2,1,3,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,1,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,3,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,1,1,1,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,1,3,2,1,1,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,1,2,1,2,1,1,1,1,2,1,2,1,1,1,3,2,1,3,2,1,2,1,2,1,1,2,1,3,2,1,1,2,1,2,1,3,2,1,1,1,2,1,1,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,1,2,1,1,1,2,1,2,1,1,3,2,1,3,2,1,2,1,2,1,1,1,1,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,4,3,2,1,4,3,2,1,1,2,1,1,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,1,2,1,2,1,1,2,1,1,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,1,3,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,3,2,1,3,2,1,1,1,1,1,2,1,2,1,1,1,2,1,2,1,1,2,1,2,1,2,1,1,1,3,2,1,3,2,1,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,1,1,2,1,2,1,2,1,3,2,1,3,2,1,1,2,1,3,2,1,2,1,1,1,3,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,2,1,2,1,1,2,1,2,1,2,1,1,1,1,2,1,1,1,2,1,1,1,2,1,3,2,1,3,2,1,1,3,2,1,3,2,1,2,1,1,2,1,1,1,1,2,1,2,1,2,1,2,1,1,2,1,4,3,2,1,4,3,2,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,1,3,2,1,2,1,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,1,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,1,2,1,2,1,3,2,1,1,1,1,2,1,1,1,2,1,1,3,2,1,3,2,1,1,1,2,1,2,1,2,1,1,2,1,3,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,3,2,1,1,1,1,2,1,1,1,1,2,1,3,2,1,1,3,2,1,3,2,1,2,1,3,2,1,1,2,1,1,3,2,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,2,1,1,2,1,1,2,1,3,2,1,1,2,1,2,1,3,2,1,3,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,1,3,2,1,1,1,1,2,1,1,2,1,1,1,1,2,1,1,2,1,2,1,3,2,1,1,2,1,1,2,1,3,2,1,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,1,3,2,1,3,2,1,3,2,1,1,2,1,1,1,1,2,1,2,1,2,1,2,1,2,1,1,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,3,2,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,2,1,1,1,2,1,2,1,3,2,1,1,3,2,1,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,3,2,1,1,3,2,1,3,2,1,1,2,1,1,2,1,1,1,1,1,1,2,1,3,2,1,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,3,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,1,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,1,1,1,1,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,1,2,1,1,2,1,1,1,3,2,1,3,2,1,2,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,1,2,1,1,1,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,1,1,2,1,3,2,1,2,1,1,1,1,2,1,3,2,1,3,2,1,2,1,2,1,3,2,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,1,1,3,2,1,3,2,1,2,1,2,1,2,1,1,3,2,1,1,2,1,2,1,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,3,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,1,2,1,1,2,1,2,1,1,2,1,1,2,1,2,1,1,3,2,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,1,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,3,2,1,1,2,1,1,1,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,3,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,1,1,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,1,2,1,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,1,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,3,2,1,3,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,3,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,1,1,1,1,2,1,1,2,1,1,2,1,1,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,2,1,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,1,1,1,2,1,1,2,1,1,2,1,2,1,2,1,1,2,1,1,3,2,1,2,1,1,1,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,1,3,2,1,3,2,1,3,2,1,2,1,1,2,1,1,2,1,2,1,2,1,3,2,1,1,2,1,1,2,1,2,1,1,2,1,1,2,1,2,1,1,1,2,1,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,8,7,6,5,4,3,2,1,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1],"label":["rowSums","rowSums","rowSums","rowSums","rowSums","rowSums","rowMeans","rowMeans","rowMeans","rowMeans","rowMeans","rowMeans","aperm.default","apply","aperm.default","apply","aperm.default","apply","aperm.default","apply","aperm.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","apply","mean.default","apply","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","apply","FUN","apply","apply","is.numeric","local","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","mean.default","apply","apply","is.numeric","local","is.numeric","local","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","isTRUE","mean.default","apply","apply","mean.default","apply","apply","mean.default","apply","mean.default","apply","is.na","local","apply","<GC>","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","apply","<GC>","length","local","apply","apply","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","apply","mean.default","apply","apply","apply","<GC>","isTRUE","mean.default","apply","apply","apply","apply","mean.default","apply","apply","mean.default","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","is.numeric","local","FUN","apply","<GC>","FUN","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","is.na","local","is.na","local","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","apply","<GC>","FUN","apply","mean.default","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","length","local","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","apply","<GC>","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","mean.default","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","apply","length","local","apply","FUN","apply","isTRUE","mean.default","apply","apply","isTRUE","mean.default","apply","is.numeric","local","mean.default","apply","mean.default","apply","<GC>","length","local","apply","mean.default","apply","mean.default","apply","apply","mean.default","apply","apply","apply","apply","apply","apply","apply","mean.default","apply","<GC>","mean.default","apply","length","local","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","mean.default","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","FUN","apply","<GC>","is.na","local","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","<GC>","FUN","apply","apply","FUN","apply","apply","apply","apply","mean.default","apply","apply","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","mean.default","apply","apply","FUN","apply","apply","mean.default","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","mean.default","apply","length","local","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","FUN","apply","apply","apply","FUN","apply","FUN","apply","apply","mean.default","apply","apply","apply","mean.default","apply","apply","<GC>","length","local","apply","mean.default","apply","isTRUE","mean.default","apply","apply","length","local","apply","FUN","apply","apply","apply","apply","length","local","<GC>","FUN","apply","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","apply","<GC>","apply","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","<GC>","apply","<GC>","apply","mean.default","apply","apply","isTRUE","mean.default","apply","length","local","FUN","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","<GC>","mean.default","apply","length","local","is.numeric","local","length","local","FUN","apply","mean.default","apply","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","apply","apply","apply","is.numeric","local","apply","mean.default","apply","apply","FUN","apply","<GC>","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","apply","<GC>","is.na","local","<GC>","is.na","local","apply","apply","apply","apply","apply","apply","length","local","mean.default","apply","mean.default","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","mean.default","apply","apply","<GC>","apply","FUN","apply","length","local","length","local","apply","FUN","apply","FUN","apply","mean.default","apply","length","local","FUN","apply","<GC>","apply","<GC>","apply","isTRUE","mean.default","apply","length","local","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","length","local","<GC>","apply","<GC>","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","apply","FUN","apply","FUN","apply","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","apply","is.numeric","local","FUN","apply","length","local","FUN","apply","apply","isTRUE","mean.default","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","apply","FUN","apply","<GC>","is.numeric","local","apply","apply","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","length","local","FUN","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","mean.default","apply","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","mean.default","apply","apply","<GC>","apply","FUN","apply","isTRUE","mean.default","apply","apply","mean.default","apply","mean.default","apply","mean.default","apply","apply","apply","<GC>","isTRUE","mean.default","apply","apply","mean.default","apply","is.na","local","FUN","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","<GC>","apply","apply","apply","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","is.numeric","local","mean.default","apply","FUN","apply","mean.default","apply","apply","FUN","apply","FUN","apply","apply","apply","apply","length","local","FUN","apply","apply","apply","FUN","apply","FUN","apply","is.na","local","apply","isTRUE","mean.default","apply","apply","isTRUE","mean.default","apply","<GC>","apply","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","apply","apply","apply","mean.default","apply","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","is.na","local","apply","apply","apply","<GC>","is.na","local","FUN","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","apply","apply","FUN","apply","is.numeric","local","isTRUE","mean.default","apply","is.numeric","local","mean.default","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","mean.default","apply","apply","FUN","apply","apply","length","local","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","apply","FUN","apply","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","apply","apply","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","is.numeric","local","apply","isTRUE","mean.default","apply","apply","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","apply","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","is.numeric","local","FUN","apply","is.numeric","local","isTRUE","mean.default","apply","<GC>","apply","<GC>","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","apply","is.numeric","local","mean.default","apply","apply","FUN","apply","length","local","FUN","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","<GC>","length","local","<GC>","length","local","FUN","apply","FUN","apply","is.na","local","isTRUE","mean.default","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","FUN","apply","apply","apply","apply","mean.default","apply","FUN","apply","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","apply","apply","FUN","apply","FUN","apply","mean.default","apply","is.na","local","<GC>","FUN","apply","<GC>","FUN","apply","length","local","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","apply","is.numeric","local","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","apply","apply","FUN","apply","is.na","local","apply","<GC>","length","local","<GC>","length","local","mean.default","apply","is.na","local","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","mean.default","apply","mean.default","apply","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","apply","length","local","apply","apply","apply","FUN","apply","mean.default","apply","FUN","apply","apply","FUN","apply","mean.default","apply","length","local","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","apply","mean.default","apply","apply","apply","FUN","apply","length","local","isTRUE","mean.default","apply","is.numeric","local","mean.default","apply","apply","mean.default","apply","apply","isTRUE","mean.default","apply","FUN","apply","apply","mean.default","apply","apply","<GC>","apply","<GC>","apply","is.numeric","local","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","FUN","apply","is.numeric","local","mean.default","apply","FUN","apply","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","apply","apply","apply","FUN","apply","mean.default","apply","apply","apply","FUN","apply","is.na","local","apply","mean.default","apply","FUN","apply","FUN","apply","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","is.numeric","local","is.numeric","local","FUN","apply","apply","is.numeric","local","mean.default","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","<GC>","apply","<GC>","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","is.numeric","local","isTRUE","mean.default","apply","is.na","local","apply","apply","isTRUE","mean.default","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","length","local","mean.default","apply","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","FUN","apply","FUN","apply","apply","apply","apply","mean.default","apply","apply","apply","mean.default","apply","apply","apply","mean.default","apply","<GC>","is.numeric","local","<GC>","is.numeric","local","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","length","local","apply","mean.default","apply","apply","apply","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","apply","FUN","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","mean.default","apply","apply","apply","<GC>","apply","<GC>","apply","is.numeric","local","FUN","apply","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","apply","FUN","apply","mean.default","apply","apply","FUN","apply","is.numeric","local","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","FUN","apply","<GC>","apply","<GC>","apply","<GC>","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","apply","apply","apply","FUN","apply","apply","apply","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","apply","FUN","apply","FUN","apply","length","local","apply","mean.default","apply","isTRUE","mean.default","apply","apply","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","apply","<GC>","apply","<GC>","apply","length","local","apply","mean.default","apply","isTRUE","mean.default","apply","apply","apply","apply","FUN","apply","apply","apply","apply","mean.default","apply","isTRUE","mean.default","apply","apply","<GC>","is.numeric","local","<GC>","is.numeric","local","is.na","local","isTRUE","mean.default","apply","apply","mean.default","apply","apply","isTRUE","mean.default","apply","FUN","apply","apply","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","length","local","apply","mean.default","apply","length","local","FUN","apply","apply","FUN","apply","apply","mean.default","apply","isTRUE","mean.default","apply","apply","mean.default","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","apply","apply","length","local","length","local","FUN","apply","FUN","apply","FUN","apply","FUN","apply","is.numeric","local","FUN","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","isTRUE","mean.default","apply","apply","apply","apply","mean.default","apply","apply","FUN","apply","apply","apply","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","mean.default","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","length","local","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","apply","<GC>","is.na","local","<GC>","is.na","local","isTRUE","mean.default","apply","apply","FUN","apply","apply","apply","apply","mean.default","apply","is.numeric","local","FUN","apply","is.numeric","local","FUN","apply","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","is.na","local","FUN","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","apply","mean.default","apply","FUN","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","mean.default","apply","length","local","mean.default","apply","apply","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","apply","is.na","local","FUN","apply","<GC>","length","local","<GC>","length","local","FUN","apply","apply","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","FUN","apply","<GC>","apply","<GC>","apply","apply","mean.default","apply","FUN","apply","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","is.numeric","local","isTRUE","mean.default","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","FUN","apply","apply","FUN","apply","apply","apply","apply","apply","apply","mean.default","apply","isTRUE","mean.default","apply","apply","<GC>","apply","<GC>","apply","apply","apply","FUN","apply","FUN","apply","is.na","local","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","apply","<GC>","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","is.numeric","local","apply","mean.default","apply","apply","<GC>","apply","<GC>","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","apply","FUN","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","is.numeric","local","FUN","apply","is.numeric","local","mean.default","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","<GC>","length","local","<GC>","length","local","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","mean.default","apply","FUN","apply","is.na","local","FUN","apply","apply","mean.default","apply","<GC>","apply","<GC>","apply","FUN","apply","mean.default","apply","apply","FUN","apply","apply","apply","apply","apply","apply","length","local","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","mean.default","apply","apply","FUN","apply","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","mean.default","apply","is.numeric","local","mean.default","apply","isTRUE","mean.default","apply","is.na","local","FUN","apply","mean.default","apply","apply","<GC>","apply","<GC>","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","is.numeric","local","apply","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","apply","<GC>","apply","<GC>","apply","mean.default","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","length","local","mean.default","apply","<GC>","apply","<GC>","apply","FUN","apply","mean.default","apply","FUN","apply","is.numeric","local","isTRUE","mean.default","apply","apply","mean.default","apply","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","mean.default","apply","is.na","local","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","apply","apply","mean.default","apply","mean.default","apply","is.numeric","local","mean.default","apply","is.na","local","FUN","apply","FUN","apply","length","local","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","apply","FUN","apply","is.na","local","apply","FUN","apply","apply","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","mean.default","apply","length","local","isTRUE","mean.default","apply","is.numeric","local","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","mean.default","apply","apply","FUN","apply","length","local","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","is.numeric","local","mean.default","apply","mean.default","apply","apply","is.na","local","is.na","local","apply","mean.default","apply","apply","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","length","local","apply","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","<GC>","apply","mean.default","apply","apply","apply","length","local","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","is.na","local","FUN","apply","FUN","apply","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","apply","FUN","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","isTRUE","mean.default","apply","apply","mean.default","apply","is.numeric","local","FUN","apply","apply","FUN","apply","apply","FUN","apply","mean.default","apply","apply","apply","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","apply","apply","mean.default","apply","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","apply","FUN","apply","length","local","isTRUE","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","length","local","apply","apply","apply","apply","apply","mean.default","apply","apply","mean.default","apply","apply","FUN","apply","apply","apply","FUN","apply","length","local","apply","is.numeric","local","FUN","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","is.numeric","local","isTRUE","mean.default","apply","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","FUN","apply","mean.default","apply","apply","apply","apply","FUN","apply","apply","FUN","apply","apply","is.na","local","mean.default","apply","FUN","apply","apply","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","length","local","apply","FUN","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","apply","is.na","local","apply","FUN","apply","is.na","local","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","mean.default","apply","is.na","local","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","apply","mean.default","apply","apply","length","local","is.na","local","isTRUE","mean.default","apply","mean.default","apply","apply","FUN","apply","FUN","apply","mean.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","apply","length","local","mean.default","apply","FUN","apply","apply","apply","apply","mean.default","apply","length","local","length","local","FUN","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","findCenvVar","getInlineInfo","trySetterInline","cmpSetterCall","cmpComplexAssign","h","tryInline","cmpCall","cmp","h","tryInline","cmpCall","cmp","cmpForBody","h","tryInline","cmpCall","cmp","genCode","compile","compiler:::tryCompile","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis"],"filenum":[1,1,1,1,1,1,1,1,1,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,1,null,null,1,null,1,null,1,null,1,1,1,null,1,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,null,1,1,null,1,1,null,null,null,null,null,1,null,1,null,1,null,1,1,null,null,1,null,null,1,1,null,1,1,null,null,1,1,null,null,1,1,null,1,1,null,1,null,1,null,null,1,null,null,null,1,null,1,null,1,null,1,null,1,null,null,1,1,null,1,null,1,null,1,null,1,1,null,1,1,null,null,null,1,1,1,1,null,1,null,1,null,1,null,1,1,1,null,1,1,1,null,null,null,1,1,1,1,null,1,1,null,1,1,null,1,null,1,1,null,1,null,null,null,1,null,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,null,null,1,null,1,null,1,null,null,1,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,1,null,1,null,1,1,null,null,1,null,null,1,1,1,null,1,null,null,1,null,1,null,null,1,1,null,1,null,1,null,1,null,1,1,null,null,1,null,1,null,1,1,1,null,null,1,null,1,null,1,null,null,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,1,1,null,1,null,1,null,null,1,null,null,1,1,1,null,null,1,null,1,null,null,1,1,null,null,1,null,null,null,1,null,1,null,null,null,1,null,1,null,1,1,null,1,1,1,1,1,1,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,1,null,1,null,1,null,1,1,null,null,1,1,null,1,null,null,null,null,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,1,1,null,null,1,1,null,1,1,1,1,null,1,1,null,1,null,1,null,1,null,1,null,null,null,1,null,null,null,1,null,null,1,null,1,1,null,1,1,null,1,1,null,1,null,1,null,1,null,null,1,null,null,1,1,null,1,null,null,null,1,null,1,null,1,null,1,1,null,null,1,null,1,null,1,null,null,1,null,1,1,1,null,1,null,1,1,null,1,1,1,null,1,1,null,null,null,1,null,1,null,null,1,1,null,null,1,null,1,1,1,1,null,null,null,null,1,1,null,null,1,1,null,1,null,1,null,1,null,1,1,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,1,1,null,1,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,1,1,null,1,null,1,null,1,1,null,null,1,null,null,null,1,1,null,1,null,1,1,null,1,null,null,1,null,null,null,null,null,null,null,1,null,1,1,null,1,null,null,1,null,1,null,1,null,null,1,1,1,null,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,null,1,1,null,1,1,1,1,null,null,1,null,1,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,1,1,null,1,1,null,null,null,null,null,null,1,1,1,1,1,1,null,null,null,1,null,1,null,null,1,null,1,null,1,1,null,1,1,null,1,null,1,null,1,1,null,1,null,1,null,null,null,null,1,null,1,null,1,null,1,null,null,null,1,null,1,null,1,null,null,1,null,null,null,1,null,1,null,1,null,null,1,null,1,null,null,null,1,null,1,null,null,1,1,null,1,1,1,null,1,null,1,1,null,null,null,1,null,null,null,1,1,null,null,null,1,null,null,null,1,1,null,null,1,null,1,null,null,1,null,null,1,1,null,1,null,1,1,null,1,null,1,1,null,1,null,null,null,1,1,1,1,1,null,1,null,1,null,1,null,1,null,null,null,null,1,null,1,1,null,1,null,1,null,1,null,1,1,null,null,1,null,null,1,null,1,null,null,1,1,null,1,null,1,1,null,1,null,null,1,null,1,null,null,1,null,1,null,1,null,null,1,1,1,null,1,1,null,1,null,1,null,null,1,1,null,1,null,1,null,1,1,1,null,null,null,1,1,null,1,null,null,null,1,null,null,1,1,1,null,1,null,1,1,1,1,null,1,null,1,null,null,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,null,1,null,1,null,1,1,null,1,null,1,1,1,1,null,null,null,1,1,1,null,1,null,1,null,null,1,null,null,1,1,null,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,1,1,1,1,1,null,1,1,null,null,1,null,1,null,1,null,null,1,1,1,null,null,null,null,1,null,1,null,1,null,1,null,null,1,null,1,null,null,1,null,1,null,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,null,1,null,null,1,1,null,1,null,null,1,null,null,1,null,1,null,1,null,null,1,null,1,1,null,null,1,null,1,1,1,null,1,null,null,1,1,null,1,null,1,null,1,null,null,1,null,1,1,null,1,1,null,null,1,null,null,1,null,null,1,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,1,1,null,1,null,null,null,null,1,null,null,null,1,null,1,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,1,1,null,1,1,null,1,1,null,null,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,null,1,null,null,1,null,1,1,null,1,1,null,1,null,1,null,1,null,1,1,1,1,1,null,1,null,1,null,1,1,null,1,1,null,1,null,1,null,null,1,null,null,1,1,1,null,1,null,1,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,null,null,1,null,null,null,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,null,1,1,null,null,null,1,1,null,1,null,null,null,1,null,1,null,1,null,1,null,null,1,null,1,null,null,null,null,null,null,null,1,null,1,null,null,null,null,1,null,1,null,1,1,1,null,1,null,1,1,1,1,null,1,null,1,1,1,null,null,1,null,null,1,null,1,null,1,1,null,1,null,null,1,1,null,1,null,1,null,null,1,1,1,null,1,1,1,null,1,null,1,null,1,null,null,null,null,1,null,null,1,null,null,null,1,null,1,null,null,1,null,1,null,1,1,null,null,null,1,null,null,1,null,1,1,null,1,1,1,null,1,null,null,1,null,null,null,null,null,null,null,1,null,null,1,1,1,null,1,null,null,1,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,null,null,1,null,null,null,1,1,null,null,1,1,1,null,1,null,1,null,1,1,null,1,null,1,null,null,null,null,1,1,null,1,null,1,1,null,1,null,1,1,null,1,1,1,null,1,null,null,null,null,1,null,null,null,1,1,null,1,1,null,null,1,null,1,1,null,1,1,null,1,null,1,null,null,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,null,1,null,null,1,1,null,1,null,null,null,1,null,1,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,null,1,null,null,1,1,1,1,1,null,1,null,1,1,1,null,1,null,null,1,null,1,null,1,null,1,1,1,null,null,1,null,null,1,1,null,null,null,null,null,1,1,null,null,null,1,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,null,1,1,1,null,1,null,1,null,1,null,null,1,null,null,1,1,null,null,null,null,1,null,null,1,1,null,null,1,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,null,null,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,1,null,1,1,null,1,null,1,null,1,1,1,1,null,1,1,1,null,1,1,1,null,1,null,null,null,null,null,null,1,null,null,1,null,null,1,null,null,1,null,1,1,1,1,null,1,null,1,null,1,null,1,1,null,1,null,null,null,1,null,null,null,1,null,1,null,1,1,null,1,null,1,null,null,1,null,null,1,1,null,null,1,null,1,1,null,1,null,1,1,1,null,1,null,1,null,null,null,1,1,null,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,null,1,null,null,1,1,1,null,1,null,1,1,null,1,null,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,null,1,1,1,null,1,null,1,null,null,1,1,1,1,null,1,1,1,null,1,1,null,null,1,null,null,1,1,1,null,1,null,1,null,null,1,null,1,null,null,1,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,null,1,null,1,null,null,1,1,1,1,null,1,1,1,1,null,1,null,null,1,1,null,null,null,null,null,null,null,null,null,null,1,1,null,1,1,null,null,1,null,1,1,null,1,null,1,1,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,1,null,null,null,1,1,null,1,1,null,1,null,null,1,1,null,1,null,1,null,null,1,null,null,1,null,1,1,1,null,null,null,null,null,1,null,1,null,1,null,1,null,null,null,1,null,1,null,1,null,null,1,null,null,1,1,null,null,1,1,1,1,null,1,1,null,1,1,1,1,null,1,1,null,1,null,1,null,null,1,1,null,1,1,null,1,null,null,1,1,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,1,1,null,null,null,null,null,null,null,null,1,1,null,1,1,1,1,null,1,null,null,null,1,null,null,null,1,1,1,null,null,1,null,null,1,null,null,null,1,null,1,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,null,null,1,1,null,1,1,null,null,1,null,1,null,1,1,null,null,null,1,null,null,null,null,null,null,null,1,1,1,null,1,null,1,null,null,1,1,null,null,1,1,1,null,1,null,1,null,1,null,1,1,null,1,null,1,1,null,1,null,1,null,null,1,null,1,null,1,null,null,null,null,1,1,null,null,1,null,null,1,1,null,1,1,null,1,1,1,1,1,1,null,1,null,null,1,1,null,1,null,1,1,1,null,1,null,1,null,null,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,1,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,1,null,1,null,1,null,1,null,null,1,null,1,null,null,1,null,null,1,null,1,1,null,1,null,1,null,null,null,1,null,null,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,1,1,null,1,null,null,1,null,1,1,null,1,null,1,null,1,null,1,null,null,null,null,null,null,null,1,null,null,1,null,1,1,null,1,null,1,null,1,null,null,null,1,1,null,1,null,1,null,1,null,1,null,1,1,null,1,1,1,1,1,1,null,null,null,null,1,null,null,1,null,1,null,1,1,null,1,1,null,1,1,null,1,1,1,null,null,1,null,null,1,null,1,1,null,1,null,null,null,1,null,null,1,null,null,null,1,null,1,1,null,1,null,1,null,null,1,1,null,1,null,1,1,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,1,null,null,1,1,1,null,1,null,1,null,1,1,1,null,1,null,1,null,1,1,1,null,1,null,null,1,null,1,1,1,1,null,1,null,null,1,null,null,1,null,1,null,1,null,null,1,1,null,1,null,null,1,null,1,null,1,null,null,null,1,null,1,null,1,null,1,null,1,null,1,null,null,null,null,1,1,null,1,1,1,null,null,1,null,null,1,null,1,null,1,null,1,1,null,null,1,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,1,null,1,null,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,null,1,1,1,null,1,null,1,null,null,null,1,null,null,null,1,null,1,null,null,1,null,null,1,null,1,null,1,1,null,1,1,null,1,null,null,1,null,1,1,null,1,null,1,1,null,null,1,null,1,null,null,null,null,1,null,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,1,null,1,null,null,null,1,null,null,1,1,null,1,null,1,null,1,null,1,null,null,1,null,null,null,1,null,1,1,null,null,null,null,1,null,1,1,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,1,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,1,null,null,1,1,null,null,1,1,null,1,null,null,1,null,1,1,null,1,null,1,null,1,null,1,1,1,null,null,null,1,null,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,null,1,null,null,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,1,null,1,null,null,1,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,null,1,1,null,1,null,null,null,1,1,null,1,1,null,1,null,1,1,1,1,null,1,null,1,null,1,null,1,null,null,1,null,1,1,1,null,1,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,1,1,1,null,1,null,null,null,null,1,null,null,1,null,1,null,1,null,null,1,null,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,1,null,1,null,1,null,null,1,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,null,1,1,1,1,1,null,1,1,null,1,1,null,1,1,1,null,1,null,null,1,null,null,null,1,null,1,1,null,1,null,1,null,null,null,null,1,null,1,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,1,null,1,null,1,null,1,1,1,1,null,1,1,null,1,1,null,null,null,1,null,1,1,null,1,1,null,null,1,null,1,1,1,1,null,null,1,null,1,null,1,null,1,null,null,1,null,1,1,null,null,1,null,null,1,null,null,1,null,1,1,null,null,1,null,1,null,null,null,1,null,null,1,1,null,1,1,null,1,null,null,1,null,1,1,null,1,null,1,1,1,null,1,1,null,null,null,null,null,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,null,null,1,null,1,1,1,1,null,1,null,null,null,null,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,1,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null],"linenum":[10,10,10,10,10,10,11,11,11,11,11,11,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,12,null,null,12,null,12,null,12,null,12,12,12,null,12,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,null,12,12,null,12,12,null,null,null,null,null,12,null,12,null,12,null,12,12,null,null,12,null,null,12,12,null,12,12,null,null,12,12,null,null,12,12,null,12,12,null,12,null,12,null,null,12,null,null,null,12,null,12,null,12,null,12,null,12,null,null,12,12,null,12,null,12,null,12,null,12,12,null,12,12,null,null,null,12,12,12,12,null,12,null,12,null,12,null,12,12,12,null,12,12,12,null,null,null,12,12,12,12,null,12,12,null,12,12,null,12,null,12,12,null,12,null,null,null,12,null,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,null,null,12,null,12,null,12,null,null,12,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,12,null,12,null,12,12,null,null,12,null,null,12,12,12,null,12,null,null,12,null,12,null,null,12,12,null,12,null,12,null,12,null,12,12,null,null,12,null,12,null,12,12,12,null,null,12,null,12,null,12,null,null,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,12,12,null,12,null,12,null,null,12,null,null,12,12,12,null,null,12,null,12,null,null,12,12,null,null,12,null,null,null,12,null,12,null,null,null,12,null,12,null,12,12,null,12,12,12,12,12,12,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,12,null,12,null,12,null,12,12,null,null,12,12,null,12,null,null,null,null,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,12,12,null,null,12,12,null,12,12,12,12,null,12,12,null,12,null,12,null,12,null,12,null,null,null,12,null,null,null,12,null,null,12,null,12,12,null,12,12,null,12,12,null,12,null,12,null,12,null,null,12,null,null,12,12,null,12,null,null,null,12,null,12,null,12,null,12,12,null,null,12,null,12,null,12,null,null,12,null,12,12,12,null,12,null,12,12,null,12,12,12,null,12,12,null,null,null,12,null,12,null,null,12,12,null,null,12,null,12,12,12,12,null,null,null,null,12,12,null,null,12,12,null,12,null,12,null,12,null,12,12,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,12,12,null,12,12,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,12,12,null,12,null,12,null,12,12,null,null,12,null,null,null,12,12,null,12,null,12,12,null,12,null,null,12,null,null,null,null,null,null,null,12,null,12,12,null,12,null,null,12,null,12,null,12,null,null,12,12,12,null,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,null,12,12,null,12,12,12,12,null,null,12,null,12,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,12,12,null,12,12,null,null,null,null,null,null,12,12,12,12,12,12,null,null,null,12,null,12,null,null,12,null,12,null,12,12,null,12,12,null,12,null,12,null,12,12,null,12,null,12,null,null,null,null,12,null,12,null,12,null,12,null,null,null,12,null,12,null,12,null,null,12,null,null,null,12,null,12,null,12,null,null,12,null,12,null,null,null,12,null,12,null,null,12,12,null,12,12,12,null,12,null,12,12,null,null,null,12,null,null,null,12,12,null,null,null,12,null,null,null,12,12,null,null,12,null,12,null,null,12,null,null,12,12,null,12,null,12,12,null,12,null,12,12,null,12,null,null,null,12,12,12,12,12,null,12,null,12,null,12,null,12,null,null,null,null,12,null,12,12,null,12,null,12,null,12,null,12,12,null,null,12,null,null,12,null,12,null,null,12,12,null,12,null,12,12,null,12,null,null,12,null,12,null,null,12,null,12,null,12,null,null,12,12,12,null,12,12,null,12,null,12,null,null,12,12,null,12,null,12,null,12,12,12,null,null,null,12,12,null,12,null,null,null,12,null,null,12,12,12,null,12,null,12,12,12,12,null,12,null,12,null,null,12,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,null,12,null,12,null,12,12,null,12,null,12,12,12,12,null,null,null,12,12,12,null,12,null,12,null,null,12,null,null,12,12,null,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,12,12,12,12,12,null,12,12,null,null,12,null,12,null,12,null,null,12,12,12,null,null,null,null,12,null,12,null,12,null,12,null,null,12,null,12,null,null,12,null,12,null,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,null,12,null,null,12,12,null,12,null,null,12,null,null,12,null,12,null,12,null,null,12,null,12,12,null,null,12,null,12,12,12,null,12,null,null,12,12,null,12,null,12,null,12,null,null,12,null,12,12,null,12,12,null,null,12,null,null,12,null,null,12,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,12,12,null,12,null,null,null,null,12,null,null,null,12,null,12,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,12,12,null,12,12,null,12,12,null,null,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,null,12,null,null,12,null,12,12,null,12,12,null,12,null,12,null,12,null,12,12,12,12,12,null,12,null,12,null,12,12,null,12,12,null,12,null,12,null,null,12,null,null,12,12,12,null,12,null,12,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,null,null,12,null,null,null,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,null,12,12,null,null,null,12,12,null,12,null,null,null,12,null,12,null,12,null,12,null,null,12,null,12,null,null,null,null,null,null,null,12,null,12,null,null,null,null,12,null,12,null,12,12,12,null,12,null,12,12,12,12,null,12,null,12,12,12,null,null,12,null,null,12,null,12,null,12,12,null,12,null,null,12,12,null,12,null,12,null,null,12,12,12,null,12,12,12,null,12,null,12,null,12,null,null,null,null,12,null,null,12,null,null,null,12,null,12,null,null,12,null,12,null,12,12,null,null,null,12,null,null,12,null,12,12,null,12,12,12,null,12,null,null,12,null,null,null,null,null,null,null,12,null,null,12,12,12,null,12,null,null,12,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,null,null,12,null,null,null,12,12,null,null,12,12,12,null,12,null,12,null,12,12,null,12,null,12,null,null,null,null,12,12,null,12,null,12,12,null,12,null,12,12,null,12,12,12,null,12,null,null,null,null,12,null,null,null,12,12,null,12,12,null,null,12,null,12,12,null,12,12,null,12,null,12,null,null,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,null,12,null,null,12,12,null,12,null,null,null,12,null,12,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,null,12,null,null,12,12,12,12,12,null,12,null,12,12,12,null,12,null,null,12,null,12,null,12,null,12,12,12,null,null,12,null,null,12,12,null,null,null,null,null,12,12,null,null,null,12,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,null,12,12,12,null,12,null,12,null,12,null,null,12,null,null,12,12,null,null,null,null,12,null,null,12,12,null,null,12,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,null,null,12,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,12,null,12,12,null,12,null,12,null,12,12,12,12,null,12,12,12,null,12,12,12,null,12,null,null,null,null,null,null,12,null,null,12,null,null,12,null,null,12,null,12,12,12,12,null,12,null,12,null,12,null,12,12,null,12,null,null,null,12,null,null,null,12,null,12,null,12,12,null,12,null,12,null,null,12,null,null,12,12,null,null,12,null,12,12,null,12,null,12,12,12,null,12,null,12,null,null,null,12,12,null,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,null,12,null,null,12,12,12,null,12,null,12,12,null,12,null,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,null,12,12,12,null,12,null,12,null,null,12,12,12,12,null,12,12,12,null,12,12,null,null,12,null,null,12,12,12,null,12,null,12,null,null,12,null,12,null,null,12,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,null,12,null,12,null,null,12,12,12,12,null,12,12,12,12,null,12,null,null,12,12,null,null,null,null,null,null,null,null,null,null,12,12,null,12,12,null,null,12,null,12,12,null,12,null,12,12,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,12,null,null,null,12,12,null,12,12,null,12,null,null,12,12,null,12,null,12,null,null,12,null,null,12,null,12,12,12,null,null,null,null,null,12,null,12,null,12,null,12,null,null,null,12,null,12,null,12,null,null,12,null,null,12,12,null,null,12,12,12,12,null,12,12,null,12,12,12,12,null,12,12,null,12,null,12,null,null,12,12,null,12,12,null,12,null,null,12,12,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,12,12,null,null,null,null,null,null,null,null,12,12,null,12,12,12,12,null,12,null,null,null,12,null,null,null,12,12,12,null,null,12,null,null,12,null,null,null,12,null,12,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,null,null,12,12,null,12,12,null,null,12,null,12,null,12,12,null,null,null,12,null,null,null,null,null,null,null,12,12,12,null,12,null,12,null,null,12,12,null,null,12,12,12,null,12,null,12,null,12,null,12,12,null,12,null,12,12,null,12,null,12,null,null,12,null,12,null,12,null,null,null,null,12,12,null,null,12,null,null,12,12,null,12,12,null,12,12,12,12,12,12,null,12,null,null,12,12,null,12,null,12,12,12,null,12,null,12,null,null,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,12,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,12,null,12,null,12,null,12,null,null,12,null,12,null,null,12,null,null,12,null,12,12,null,12,null,12,null,null,null,12,null,null,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,12,12,null,12,null,null,12,null,12,12,null,12,null,12,null,12,null,12,null,null,null,null,null,null,null,12,null,null,12,null,12,12,null,12,null,12,null,12,null,null,null,12,12,null,12,null,12,null,12,null,12,null,12,12,null,12,12,12,12,12,12,null,null,null,null,12,null,null,12,null,12,null,12,12,null,12,12,null,12,12,null,12,12,12,null,null,12,null,null,12,null,12,12,null,12,null,null,null,12,null,null,12,null,null,null,12,null,12,12,null,12,null,12,null,null,12,12,null,12,null,12,12,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,12,null,null,12,12,12,null,12,null,12,null,12,12,12,null,12,null,12,null,12,12,12,null,12,null,null,12,null,12,12,12,12,null,12,null,null,12,null,null,12,null,12,null,12,null,null,12,12,null,12,null,null,12,null,12,null,12,null,null,null,12,null,12,null,12,null,12,null,12,null,12,null,null,null,null,12,12,null,12,12,12,null,null,12,null,null,12,null,12,null,12,null,12,12,null,null,12,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,12,null,12,null,12,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,null,12,12,12,null,12,null,12,null,null,null,12,null,null,null,12,null,12,null,null,12,null,null,12,null,12,null,12,12,null,12,12,null,12,null,null,12,null,12,12,null,12,null,12,12,null,null,12,null,12,null,null,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,12,null,12,null,null,null,12,null,null,12,12,null,12,null,12,null,12,null,12,null,null,12,null,null,null,12,null,12,12,null,null,null,null,12,null,12,12,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,12,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,12,null,null,12,12,null,null,12,12,null,12,null,null,12,null,12,12,null,12,null,12,null,12,null,12,12,12,null,null,null,12,null,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,null,12,null,null,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,12,null,12,null,null,12,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,null,12,12,null,12,null,null,null,12,12,null,12,12,null,12,null,12,12,12,12,null,12,null,12,null,12,null,12,null,null,12,null,12,12,12,null,12,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,12,12,12,null,12,null,null,null,null,12,null,null,12,null,12,null,12,null,null,12,null,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,12,null,12,null,12,null,null,12,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,null,12,12,12,12,12,null,12,12,null,12,12,null,12,12,12,null,12,null,null,12,null,null,null,12,null,12,12,null,12,null,12,null,null,null,null,12,null,12,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,12,null,12,null,12,null,12,12,12,12,null,12,12,null,12,12,null,null,null,12,null,12,12,null,12,12,null,null,12,null,12,12,12,12,null,null,12,null,12,null,12,null,12,null,null,12,null,12,12,null,null,12,null,null,12,null,null,12,null,12,12,null,null,12,null,12,null,null,null,12,null,null,12,12,null,12,12,null,12,null,null,12,null,12,12,null,12,null,12,12,12,null,12,12,null,null,null,null,null,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,null,null,12,null,12,12,12,12,null,12,null,null,null,null,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,13,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,13,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null],"memalloc":[124.4683074951172,124.4683074951172,124.4683074951172,124.4683074951172,124.4683074951172,124.4683074951172,139.7505416870117,139.7505416870117,139.7505416870117,139.7505416870117,139.7505416870117,139.7505416870117,170.2162857055664,170.2162857055664,170.2162857055664,170.2162857055664,170.2162857055664,170.2162857055664,170.2162857055664,170.2162857055664,170.2162857055664,170.2162857055664,170.2163314819336,170.2163314819336,170.2163314819336,170.2163314819336,170.2163314819336,170.2163314819336,170.2163314819336,170.2163314819336,170.2163314819336,170.2163314819336,170.2163314819336,170.2163314819336,170.2163314819336,170.2163314819336,170.2163314819336,170.2163314819336,170.2163314819336,170.2163314819336,170.2160263061523,170.2160263061523,170.2160263061523,170.2160263061523,185.6359405517578,185.6359405517578,185.8265991210938,186.0245056152344,186.0245056152344,186.2271881103516,186.4466781616211,186.4466781616211,186.4466781616211,186.6807861328125,186.6807861328125,186.9206619262695,186.9206619262695,187.1517181396484,187.1517181396484,187.3811950683594,187.6083602905273,187.8381805419922,187.8381805419922,188.069694519043,188.3079376220703,188.3079376220703,188.5455093383789,188.7350845336914,188.7350845336914,188.7350845336914,188.7350845336914,188.7350845336914,188.7350845336914,185.8434448242188,185.8434448242188,186.0806655883789,186.0806655883789,186.3238983154297,186.3238983154297,186.3238983154297,186.5878677368164,186.8270034790039,186.8270034790039,187.0623474121094,187.2940979003906,187.2940979003906,187.5251998901367,187.5251998901367,187.755126953125,187.755126953125,187.9844741821289,187.9844741821289,188.2153549194336,188.2153549194336,188.4457473754883,188.4457473754883,188.6763076782227,188.804931640625,188.804931640625,188.804931640625,185.8235778808594,185.8235778808594,185.8235778808594,186.0456008911133,186.2835464477539,186.2835464477539,186.5235290527344,186.7630767822266,186.7630767822266,186.7630767822266,187.0020523071289,187.2358093261719,187.2358093261719,187.2358093261719,187.467658996582,187.701171875,187.701171875,187.9342575073242,188.1674041748047,188.1674041748047,188.3995666503906,188.3995666503906,188.6324310302734,188.6324310302734,188.8624496459961,188.8919677734375,188.8919677734375,188.8919677734375,188.8919677734375,186.0442352294922,186.0442352294922,186.2679748535156,186.2679748535156,186.509765625,186.509765625,186.7535171508789,186.7535171508789,187.0200729370117,187.0200729370117,187.0200729370117,187.2549057006836,187.489990234375,187.489990234375,187.7237243652344,187.7237243652344,187.9560394287109,187.9560394287109,188.1878662109375,188.1878662109375,188.4212265014648,188.6548080444336,188.6548080444336,188.8891143798828,188.9776840209961,188.9776840209961,188.9776840209961,186.1197357177734,186.3384475708008,186.5717163085938,186.8126907348633,187.0504608154297,187.0504608154297,187.2875747680664,187.2875747680664,187.5234298706055,187.5234298706055,187.7553482055664,187.7553482055664,187.9890365600586,188.2217102050781,188.4562225341797,188.4562225341797,188.6887741088867,188.9199829101562,189.0619812011719,189.0619812011719,189.0619812011719,189.0619812011719,186.1985626220703,186.4164352416992,186.6477813720703,186.8923873901367,186.8923873901367,187.1350784301758,187.3721008300781,187.3721008300781,187.6317367553711,187.863655090332,187.863655090332,188.0969848632812,188.0969848632812,188.3278503417969,188.5590057373047,188.5590057373047,188.7895889282227,188.7895889282227,189.0192718505859,189.0192718505859,189.1449279785156,189.1449279785156,189.1449279785156,186.3380355834961,186.3380355834961,186.5542526245117,186.7865142822266,186.7865142822266,187.0295257568359,187.0295257568359,187.2688751220703,187.2688751220703,187.5066833496094,187.5066833496094,187.7432250976562,187.7432250976562,187.9773330688477,187.9773330688477,188.2085800170898,188.2085800170898,188.4400405883789,188.4400405883789,188.6737060546875,188.9060668945312,188.9060668945312,189.1375198364258,189.1375198364258,189.2265014648438,189.2265014648438,189.2265014648438,186.4949417114258,186.7092819213867,186.7092819213867,186.9422912597656,186.9422912597656,187.1832046508789,187.1832046508789,187.4188919067383,187.4188919067383,187.4188919067383,187.6550827026367,187.6550827026367,187.8896865844727,187.8896865844727,188.1207733154297,188.1207733154297,188.3726501464844,188.6040344238281,188.6040344238281,188.8374862670898,188.8374862670898,189.06982421875,189.3021087646484,189.3021087646484,189.3021087646484,189.3068313598633,189.3068313598633,189.3068313598633,186.6859893798828,186.8997192382812,187.1360244750977,187.1360244750977,187.3746871948242,187.3746871948242,187.3746871948242,187.6126174926758,187.6126174926758,187.8489990234375,187.8489990234375,187.8489990234375,188.0811996459961,188.3120651245117,188.3120651245117,188.5431518554688,188.5431518554688,188.7760696411133,188.7760696411133,189.0098114013672,189.0098114013672,189.2438278198242,189.3858032226562,189.3858032226562,189.3858032226562,186.6965637207031,186.6965637207031,186.9160614013672,186.9160614013672,187.1456451416016,187.3879013061523,187.6249923706055,187.6249923706055,187.6249923706055,187.861686706543,187.861686706543,188.0958404541016,188.0958404541016,188.3291778564453,188.3291778564453,188.5636215209961,188.5636215209961,188.5636215209961,188.7969741821289,188.7969741821289,189.0549240112305,189.0549240112305,189.2897109985352,189.2897109985352,189.4635009765625,189.4635009765625,189.4635009765625,189.4635009765625,186.9917526245117,186.9917526245117,187.2180023193359,187.456413269043,187.456413269043,187.694580078125,187.694580078125,187.9303588867188,187.9303588867188,188.1660385131836,188.1660385131836,188.4014053344727,188.4014053344727,188.6333847045898,188.8641357421875,189.0953903198242,189.0953903198242,189.3283996582031,189.3283996582031,189.5400161743164,189.5400161743164,189.5400161743164,189.5400161743164,189.5400161743164,189.5400161743164,187.0769500732422,187.3028945922852,187.5441970825195,187.5441970825195,187.7848815917969,188.0213623046875,188.0213623046875,188.2562789916992,188.2562789916992,188.2562789916992,188.491813659668,188.7265701293945,188.7265701293945,188.7265701293945,188.9627685546875,188.9627685546875,189.1984329223633,189.1984329223633,189.4428405761719,189.4428405761719,189.6151885986328,189.6151885986328,189.6151885986328,187.0498809814453,187.2635879516602,187.2635879516602,187.4955596923828,187.4955596923828,187.7304306030273,187.9688415527344,187.9688415527344,188.2059173583984,188.4419860839844,188.6775970458984,188.9116897583008,189.1416625976562,189.3726654052734,189.6017837524414,189.6017837524414,189.689208984375,189.689208984375,189.689208984375,187.2081527709961,187.2081527709961,187.4183883666992,187.6412124633789,187.6412124633789,187.6412124633789,187.8742446899414,187.8742446899414,187.8742446899414,188.1062545776367,188.3392333984375,188.3392333984375,188.5733184814453,188.5733184814453,188.806510925293,188.806510925293,189.0385589599609,189.2680358886719,189.2680358886719,189.2680358886719,189.5013961791992,189.7407455444336,189.7407455444336,189.7620086669922,189.7620086669922,189.7620086669922,187.3791580200195,187.3791580200195,187.3791580200195,187.5940933227539,187.5940933227539,187.8209838867188,187.8209838867188,188.0797500610352,188.3135681152344,188.3135681152344,188.5500717163086,188.5500717163086,188.7846832275391,188.7846832275391,189.0177154541016,189.0177154541016,189.2463607788086,189.2463607788086,189.4794845581055,189.7158279418945,189.8336791992188,189.8336791992188,189.8336791992188,187.4069213867188,187.6158447265625,187.6158447265625,187.836669921875,188.0705718994141,188.3022003173828,188.5362319946289,188.5362319946289,188.7717056274414,189.0061950683594,189.0061950683594,189.2395477294922,189.2395477294922,189.4709930419922,189.4709930419922,189.7037048339844,189.7037048339844,189.9040908813477,189.9040908813477,189.9040908813477,189.9040908813477,189.9040908813477,189.9040908813477,189.9040908813477,189.9040908813477,187.6447372436523,187.6447372436523,187.6447372436523,187.8579711914062,187.8579711914062,188.0834579467773,188.31591796875,188.31591796875,188.5525665283203,188.7882766723633,188.7882766723633,189.0243606567383,189.281379699707,189.281379699707,189.5158004760742,189.5158004760742,189.7518310546875,189.7518310546875,189.9734649658203,189.9734649658203,189.9734649658203,189.9734649658203,189.9734649658203,189.9734649658203,187.7294464111328,187.9164733886719,187.9164733886719,188.1088180541992,188.1088180541992,188.3168869018555,188.3168869018555,188.5429000854492,188.5429000854492,188.781005859375,188.781005859375,189.016845703125,189.016845703125,189.2524566650391,189.4860916137695,189.4860916137695,189.4860916137695,189.7180633544922,189.7180633544922,189.9517822265625,189.9517822265625,190.0416641235352,190.0416641235352,190.0416641235352,187.7455902099609,187.7455902099609,187.9505004882812,188.1628723144531,188.3816909790039,188.3816909790039,188.6157760620117,188.6157760620117,188.843017578125,189.0706329345703,189.0706329345703,189.3069763183594,189.5397491455078,189.7944641113281,189.7944641113281,190.0300064086914,190.108772277832,190.108772277832,190.108772277832,187.8557891845703,188.0566940307617,188.0566940307617,188.2654800415039,188.2654800415039,188.2654800415039,188.4900665283203,188.7256088256836,188.7256088256836,188.9627990722656,189.1992340087891,189.1992340087891,189.4340209960938,189.6675872802734,189.9083557128906,190.1518783569336,190.1518783569336,190.1748275756836,190.1748275756836,190.1748275756836,188.0126266479492,188.2151489257812,188.2151489257812,188.2151489257812,188.4265441894531,188.6555862426758,188.6555862426758,188.8916015625,188.8916015625,189.1281433105469,189.1281433105469,189.3634414672852,189.3634414672852,189.5972442626953,189.8359985351562,190.080436706543,190.080436706543,190.2397842407227,190.2397842407227,190.2397842407227,190.2397842407227,190.2397842407227,190.2397842407227,190.2397842407227,190.2397842407227,190.2397842407227,190.2397842407227,190.2397842407227,190.2397842407227,190.2397842407227,190.2397842407227,190.2397842407227,190.2397842407227,190.2397842407227,190.2397842407227,190.2397842407227,190.2397842407227,190.2397842407227,190.2397842407227,190.2397842407227,190.2397842407227,190.2397842407227,190.2397842407227,190.2397842407227,190.2397842407227,190.2397842407227,190.2397842407227,190.2397842407227,190.2397842407227,190.2397842407227,188.0549774169922,188.0549774169922,188.2279968261719,188.2279968261719,188.406982421875,188.5921859741211,188.7914505004883,188.7914505004883,189.0085144042969,189.2368774414062,189.4681549072266,189.6909408569336,189.6909408569336,189.9164276123047,189.9164276123047,190.1426162719727,190.1426162719727,190.303596496582,190.303596496582,190.303596496582,190.303596496582,188.2813186645508,188.2813186645508,188.4815139770508,188.4815139770508,188.7198104858398,188.9523315429688,188.9523315429688,189.1871185302734,189.1871185302734,189.4225921630859,189.4225921630859,189.6570281982422,189.6570281982422,189.8905410766602,190.1314086914062,190.3665542602539,190.3665542602539,190.3665542602539,190.3665542602539,188.325927734375,188.325927734375,188.5239715576172,188.7333374023438,188.7333374023438,188.7333374023438,188.9616622924805,188.9616622924805,189.1944808959961,189.1944808959961,189.4269256591797,189.6589508056641,189.6589508056641,189.8905792236328,189.8905792236328,190.1228637695312,190.3622589111328,190.3622589111328,190.4284744262695,190.4284744262695,190.4284744262695,188.361083984375,188.361083984375,188.5583038330078,188.5583038330078,188.7623672485352,188.7623672485352,188.9834442138672,188.9834442138672,189.2157897949219,189.2157897949219,189.4501037597656,189.6841659545898,189.6841659545898,189.9175338745117,189.9175338745117,189.9175338745117,190.1735229492188,190.1735229492188,190.4132385253906,190.4132385253906,190.4893951416016,190.4893951416016,190.4893951416016,188.4345550537109,188.6237182617188,188.8268737792969,188.8268737792969,188.8268737792969,189.0481262207031,189.0481262207031,189.2847137451172,189.2847137451172,189.5239028930664,189.5239028930664,189.7607345581055,189.7607345581055,189.9988861083984,189.9988861083984,189.9988861083984,190.241081237793,190.241081237793,190.4838714599609,190.4838714599609,190.5493392944336,190.5493392944336,190.5493392944336,188.5483627319336,188.7453536987305,188.7453536987305,188.9500350952148,189.1763916015625,189.4142684936523,189.6480407714844,189.6480407714844,189.8857727050781,190.1218109130859,190.1218109130859,190.3542938232422,190.5864639282227,190.5864639282227,190.6082458496094,190.6082458496094,190.6082458496094,188.6500473022461,188.6500473022461,188.8559265136719,188.8559265136719,189.0642166137695,189.0642166137695,189.2888336181641,189.2888336181641,189.5249557495117,189.5249557495117,189.7613906860352,189.9980392456055,190.2338790893555,190.2338790893555,190.4780349731445,190.6662826538086,190.6662826538086,190.6662826538086,190.6662826538086,190.6662826538086,190.6662826538086,188.8261871337891,189.0226516723633,189.2365570068359,189.4686050415039,189.7035751342773,189.9417495727539,190.1759338378906,190.1759338378906,190.4168243408203,190.4168243408203,190.660041809082,190.660041809082,190.7233810424805,190.7233810424805,190.7233810424805,188.8177261352539,188.8177261352539,189.0104675292969,189.0104675292969,189.2152481079102,189.4386291503906,189.4386291503906,189.6740493774414,189.9127655029297,189.9127655029297,190.151237487793,190.151237487793,190.3956298828125,190.3956298828125,190.6643295288086,190.7794418334961,190.7794418334961,188.8633804321289,188.8633804321289,189.0522003173828,189.0522003173828,189.2531433105469,189.2531433105469,189.4728698730469,189.7098770141602,189.7098770141602,189.9501037597656,189.9501037597656,190.189323425293,190.189323425293,190.4309463500977,190.4309463500977,190.6755065917969,190.6755065917969,190.8347320556641,190.8347320556641,190.8347320556641,190.8347320556641,189.1057891845703,189.1057891845703,189.1057891845703,189.3044509887695,189.3044509887695,189.5195999145508,189.5195999145508,189.7524032592773,189.7524032592773,189.9864730834961,189.9864730834961,190.223388671875,190.223388671875,190.223388671875,190.4574890136719,190.4574890136719,190.6901779174805,190.6901779174805,190.8891220092773,190.8891220092773,190.8891220092773,190.8891220092773,189.1403884887695,189.1403884887695,189.1403884887695,189.3316192626953,189.5392074584961,189.5392074584961,189.7845230102539,190.0209808349609,190.2569046020508,190.2569046020508,190.4927597045898,190.4927597045898,190.7252044677734,190.942512512207,190.942512512207,190.942512512207,190.942512512207,190.942512512207,190.942512512207,190.942512512207,190.942512512207,189.209587097168,189.3997192382812,189.3997192382812,189.6067428588867,189.6067428588867,189.8347320556641,189.8347320556641,190.0699996948242,190.0699996948242,190.3075942993164,190.5454025268555,190.5454025268555,190.5454025268555,190.7898483276367,190.7898483276367,190.9951629638672,190.9951629638672,190.9951629638672,190.9951629638672,190.9951629638672,190.9951629638672,189.312385559082,189.5079956054688,189.5079956054688,189.7215881347656,189.7215881347656,189.9547348022461,190.1942596435547,190.1942596435547,190.4340057373047,190.4340057373047,190.6728515625,190.9168701171875,190.9168701171875,191.0469131469727,191.0469131469727,191.0469131469727,189.2833557128906,189.4685516357422,189.667366027832,189.8844299316406,190.1175689697266,190.353759765625,190.353759765625,190.5892562866211,190.5892562866211,190.8250885009766,190.8250885009766,191.0680160522461,191.0680160522461,191.0978012084961,191.0978012084961,191.0978012084961,189.4167556762695,189.4167556762695,189.6078872680664,189.6078872680664,189.814811706543,190.0407943725586,190.0407943725586,190.2792205810547,190.2792205810547,190.5182571411133,190.5182571411133,190.7568817138672,190.7568817138672,190.9995498657227,191.1478881835938,191.1478881835938,191.1478881835938,191.1478881835938,191.1478881835938,191.1478881835938,189.5944671630859,189.5944671630859,189.7929534912109,189.7929534912109,189.7929534912109,190.0101165771484,190.2434005737305,190.2434005737305,190.4804458618164,190.4804458618164,190.7160034179688,190.9524765014648,190.9524765014648,191.1958999633789,191.1958999633789,191.1958999633789,191.1971588134766,191.1971588134766,189.6122512817383,189.6122512817383,189.6122512817383,189.8071823120117,189.8071823120117,190.0204010009766,190.0204010009766,190.251350402832,190.251350402832,190.251350402832,190.4924850463867,190.7314834594727,190.9706268310547,190.9706268310547,191.2073059082031,191.2456359863281,191.2456359863281,189.6364669799805,189.6364669799805,189.8244247436523,189.8244247436523,189.8244247436523,190.0276718139648,190.2506561279297,190.2506561279297,190.4884262084961,190.4884262084961,190.7270660400391,190.7270660400391,190.9638366699219,191.2046966552734,191.2933502197266,191.2933502197266,191.2933502197266,191.2933502197266,189.678466796875,189.8658676147461,189.8658676147461,190.0674591064453,190.0674591064453,190.288703918457,190.288703918457,190.5259704589844,190.5259704589844,190.5259704589844,190.7647705078125,191.0250778198242,191.2655792236328,191.2655792236328,191.3403015136719,191.3403015136719,189.7526016235352,189.9280776977539,190.1306915283203,190.3511962890625,190.3511962890625,190.5877380371094,190.5877380371094,190.8273010253906,190.8273010253906,190.8273010253906,191.0658111572266,191.3071899414062,191.3865051269531,191.3865051269531,191.3865051269531,191.3865051269531,191.3865051269531,191.3865051269531,191.3865051269531,191.3865051269531,191.3865051269531,191.3865051269531,191.3865051269531,191.3865051269531,191.3865051269531,191.3865051269531,191.3865051269531,191.3865051269531,191.3865051269531,191.3865051269531,191.3865051269531,191.3865051269531,191.3865051269531,191.3865051269531,191.3865051269531,191.3865051269531,191.3865051269531,191.3865051269531,191.3865051269531,191.3865051269531,191.3865051269531,191.3865051269531,191.3865051269531,191.3865051269531,191.3865051269531,191.3865051269531,191.3865051269531,191.3865051269531,191.3865051269531,191.3865051269531,191.3865051269531,191.3865051269531,191.3865051269531,191.3865051269531,191.3865051269531,191.3865051269531,191.3865051269531,191.3865051269531,191.3865051269531,191.3865051269531,191.3865051269531,191.3865051269531,191.3865051269531,191.3865051269531,191.3865051269531,191.3865051269531,191.3865051269531,191.3865051269531,191.3865051269531,191.3865051269531,189.7965774536133,189.7965774536133,189.7965774536133,189.7965774536133,189.9020385742188,189.9020385742188,190.0949020385742,190.0949020385742,190.2984619140625,190.2984619140625,190.5218353271484,190.5218353271484,190.759765625,190.759765625,190.9870300292969,190.9870300292969,191.2036743164062,191.4281539916992,191.4281539916992,191.6662750244141,191.6662750244141,191.9142990112305,192.1570358276367,192.393798828125,192.6244277954102,192.6244277954102,192.8219604492188,192.8219604492188,193.019287109375,193.2156753540039,193.4122619628906,193.4122619628906,193.6081085205078,193.6081085205078,193.802375793457,193.802375793457,193.9977264404297,194.1924514770508,194.1924514770508,194.1924514770508,194.3880844116211,194.5811309814453,194.5811309814453,194.5811309814453,194.6369781494141,194.6369781494141,190.0375747680664,190.2498474121094,190.2498474121094,190.4820022583008,190.4820022583008,190.722053527832,190.722053527832,190.9582290649414,190.9582290649414,191.1815032958984,191.1815032958984,191.3944625854492,191.3944625854492,191.6350402832031,191.8794784545898,192.1238708496094,192.3664932250977,192.6073532104492,192.8461990356445,192.8461990356445,193.08447265625,193.3219299316406,193.3219299316406,193.3219299316406,193.5591354370117,193.5591354370117,193.796028137207,193.796028137207,194.0336532592773,194.0336532592773,194.2702331542969,194.5029144287109,194.7334976196289,194.7694244384766,194.7694244384766,194.7694244384766,190.2302932739258,190.2302932739258,190.4350738525391,190.4350738525391,190.6577682495117,190.6577682495117,190.8941192626953,190.8941192626953,191.1257705688477,191.1257705688477,191.1257705688477,191.3651123046875,191.3651123046875,191.5906219482422,191.5906219482422,191.5906219482422,191.8305206298828,191.8305206298828,192.0779037475586,192.0779037475586,192.0779037475586,192.3251266479492,192.3251266479492,192.5681762695312,192.5681762695312,192.8089370727539,192.8089370727539,193.0460510253906,193.2846450805664,193.2846450805664,193.5227508544922,193.5227508544922,193.7612228393555,193.7612228393555,193.9990310668945,193.9990310668945,193.9990310668945,194.2387161254883,194.2387161254883,194.2387161254883,194.4803237915039,194.7130279541016,194.7130279541016,194.8997116088867,194.8997116088867,194.8997116088867,194.8997116088867,194.8997116088867,194.8997116088867,190.4976501464844,190.4976501464844,190.69873046875,190.69873046875,190.9173965454102,190.9173965454102,190.9173965454102,191.1479644775391,191.1479644775391,191.374137878418,191.5896453857422,191.5896453857422,191.5896453857422,191.8319549560547,191.8319549560547,192.0727767944336,192.3180923461914,192.5614471435547,192.5614471435547,192.8016586303711,192.8016586303711,192.8016586303711,193.0410614013672,193.2805099487305,193.2805099487305,193.5423355102539,193.5423355102539,193.7811965942383,193.7811965942383,194.0173645019531,194.0173645019531,194.0173645019531,194.2563323974609,194.2563323974609,194.4991073608398,194.7395935058594,194.7395935058594,194.973747253418,195.0277862548828,195.0277862548828,195.0277862548828,195.0277862548828,195.0277862548828,195.0277862548828,190.8030471801758,190.8030471801758,190.8030471801758,191.0199127197266,191.2471694946289,191.2471694946289,191.4735336303711,191.4735336303711,191.6912841796875,191.9364471435547,191.9364471435547,192.18017578125,192.18017578125,192.428825378418,192.428825378418,192.6792831420898,192.6792831420898,192.9253005981445,192.9253005981445,193.167106628418,193.4084930419922,193.6487197875977,193.6487197875977,193.8877563476562,193.8877563476562,194.1267395019531,194.1267395019531,194.1267395019531,194.3659133911133,194.3659133911133,194.6054763793945,194.6054763793945,194.8437805175781,194.8437805175781,195.0746536254883,195.0746536254883,195.1539688110352,195.1539688110352,195.1539688110352,195.1539688110352,195.1539688110352,195.1539688110352,190.9947738647461,190.9947738647461,191.2079391479492,191.2079391479492,191.4316711425781,191.4316711425781,191.6522445678711,191.6522445678711,191.878173828125,192.1189041137695,192.3561401367188,192.3561401367188,192.5935668945312,192.8363723754883,192.8363723754883,193.0761260986328,193.3112487792969,193.3112487792969,193.5467224121094,193.5467224121094,193.7810134887695,193.7810134887695,194.0154190063477,194.0154190063477,194.2516174316406,194.2516174316406,194.4882888793945,194.4882888793945,194.7251815795898,194.7251815795898,194.9623184204102,195.190788269043,195.190788269043,195.2779541015625,195.2779541015625,195.2779541015625,195.2779541015625,195.2779541015625,195.2779541015625,191.1579513549805,191.1579513549805,191.3654174804688,191.582763671875,191.582763671875,191.7989501953125,192.0292434692383,192.0292434692383,192.2922515869141,192.2922515869141,192.5307006835938,192.5307006835938,192.7772445678711,192.7772445678711,193.0235443115234,193.2668838500977,193.5056991577148,193.7434692382812,193.9821014404297,193.9821014404297,194.2203674316406,194.2203674316406,194.4595184326172,194.4595184326172,194.6989974975586,194.9412002563477,194.9412002563477,195.1778182983398,195.4000701904297,195.4000701904297,195.4000701904297,195.4000701904297,191.227165222168,191.227165222168,191.4069900512695,191.62109375,191.62109375,191.62109375,191.8349761962891,192.0561676025391,192.2956390380859,192.2956390380859,192.5358428955078,192.5358428955078,192.7746505737305,193.0210800170898,193.0210800170898,193.2692108154297,193.5123672485352,193.5123672485352,193.7517395019531,193.7517395019531,193.9917678833008,193.9917678833008,194.2326812744141,194.2326812744141,194.4723968505859,194.4723968505859,194.7124557495117,194.7124557495117,194.9775772094727,194.9775772094727,195.2183456420898,195.2183456420898,195.4510345458984,195.4510345458984,195.4510345458984,195.5201034545898,195.5201034545898,195.5201034545898,195.5201034545898,191.5524520874023,191.5524520874023,191.7591400146484,191.9673080444336,191.9673080444336,192.1853713989258,192.1853713989258,192.4246063232422,192.4246063232422,192.663215637207,192.663215637207,192.663215637207,192.9034194946289,193.1476974487305,193.1476974487305,193.3942489624023,193.3942489624023,193.6378555297852,193.8788909912109,193.8788909912109,194.1212463378906,194.1212463378906,194.3647994995117,194.3647994995117,194.6083450317383,194.6083450317383,194.8526077270508,194.8526077270508,195.0972213745117,195.0972213745117,195.3402786254883,195.3402786254883,195.3402786254883,195.5752792358398,195.5752792358398,195.6382675170898,195.6382675170898,195.6382675170898,195.6382675170898,195.6382675170898,195.6382675170898,191.7389755249023,191.7389755249023,191.9654998779297,191.9654998779297,192.1722412109375,192.1722412109375,192.4015808105469,192.4015808105469,192.4015808105469,192.6423110961914,192.6423110961914,192.8686904907227,192.8686904907227,193.1084442138672,193.3544616699219,193.6014633178711,193.6014633178711,193.8459014892578,193.8459014892578,194.0874252319336,194.329231262207,194.5716705322266,194.8126373291016,194.8126373291016,195.054069519043,195.054069519043,195.2967376708984,195.5315933227539,195.7545700073242,195.7545700073242,195.7545700073242,195.7545700073242,195.7545700073242,195.7545700073242,191.7703323364258,191.7703323364258,191.9679107666016,191.9679107666016,192.1606979370117,192.3430633544922,192.3430633544922,192.5696258544922,192.5696258544922,192.5696258544922,192.8065643310547,193.0460891723633,193.0460891723633,193.2858963012695,193.2858963012695,193.552116394043,193.552116394043,193.552116394043,193.8015899658203,194.0480575561523,194.291374206543,194.291374206543,194.5344772338867,194.7762145996094,195.0176696777344,195.0176696777344,195.2598419189453,195.2598419189453,195.5028762817383,195.5028762817383,195.7362747192383,195.7362747192383,195.8689193725586,195.8689193725586,195.8689193725586,195.8689193725586,195.8689193725586,195.8689193725586,192.0284042358398,192.0284042358398,192.2228240966797,192.2228240966797,192.4188613891602,192.4188613891602,192.6355514526367,192.6355514526367,192.6355514526367,192.8706665039062,192.8706665039062,193.106330871582,193.106330871582,193.3408355712891,193.5740127563477,193.5740127563477,193.8071823120117,193.8071823120117,194.0498962402344,194.0498962402344,194.0498962402344,194.2872848510742,194.2872848510742,194.5242462158203,194.7612457275391,194.7612457275391,194.9990921020508,195.2363357543945,195.473747253418,195.473747253418,195.7099075317383,195.7099075317383,195.9385833740234,195.9813766479492,195.9813766479492,195.9813766479492,195.9813766479492,195.9813766479492,195.9813766479492,192.2961807250977,192.2961807250977,192.4837875366211,192.4837875366211,192.6815795898438,192.9051361083984,193.1358184814453,193.3670959472656,193.3670959472656,193.5989227294922,193.5989227294922,193.5989227294922,193.8355178833008,194.078125,194.078125,194.3196182250977,194.3196182250977,194.5570678710938,194.5570678710938,194.7941055297852,194.7941055297852,195.0311737060547,195.0311737060547,195.2691497802734,195.5054702758789,195.5054702758789,195.7436294555664,195.7436294555664,195.965934753418,195.965934753418,196.0921020507812,196.0921020507812,196.0921020507812,196.0921020507812,196.0921020507812,196.0921020507812,196.0921020507812,196.0921020507812,192.3818206787109,192.5689239501953,192.5689239501953,192.7565307617188,192.9728240966797,193.2262115478516,193.4566116333008,193.4566116333008,193.6879501342773,193.6879501342773,193.9179382324219,193.9179382324219,194.1575393676758,194.3990936279297,194.3990936279297,194.6361770629883,194.6361770629883,194.872932434082,194.872932434082,195.1083984375,195.1083984375,195.1083984375,195.3469085693359,195.584098815918,195.584098815918,195.8218536376953,195.8218536376953,196.0533752441406,196.2010040283203,196.2010040283203,196.2010040283203,196.2010040283203,192.5300827026367,192.7163848876953,192.7163848876953,192.9119186401367,193.1327209472656,193.3668670654297,193.3668670654297,193.6013107299805,193.6013107299805,193.8375091552734,193.8375091552734,193.8375091552734,194.0775527954102,194.0775527954102,194.3211135864258,194.3211135864258,194.5701599121094,194.811393737793,194.811393737793,195.051139831543,195.2904434204102,195.2904434204102,195.2904434204102,195.5320510864258,195.5320510864258,195.7958602905273,196.035530090332,196.035530090332,196.2660217285156,196.3081817626953,196.3081817626953,196.3081817626953,196.3081817626953,192.7825775146484,192.7825775146484,192.967399597168,192.967399597168,193.1734085083008,193.1734085083008,193.3916320800781,193.3916320800781,193.6223983764648,193.6223983764648,193.8540344238281,193.8540344238281,194.0910949707031,194.0910949707031,194.3297958374023,194.5740051269531,194.5740051269531,194.8222885131836,194.8222885131836,195.0676040649414,195.0676040649414,195.3117294311523,195.3117294311523,195.5547256469727,195.5547256469727,195.7969589233398,196.0381622314453,196.0381622314453,196.2721405029297,196.2721405029297,196.4135665893555,196.4135665893555,196.4135665893555,196.4135665893555,196.4135665893555,196.4135665893555,192.8643493652344,193.0481719970703,193.0481719970703,193.2421112060547,193.2421112060547,193.4752960205078,193.4752960205078,193.6992034912109,193.6992034912109,193.9272003173828,194.1598281860352,194.1598281860352,194.3937377929688,194.3937377929688,194.6359024047852,194.6359024047852,194.6359024047852,194.8794631958008,194.8794631958008,195.1189727783203,195.1189727783203,195.3571472167969,195.3571472167969,195.5932769775391,195.5932769775391,195.8313980102539,195.8313980102539,196.0681381225586,196.0681381225586,196.0681381225586,196.3034744262695,196.3034744262695,196.5173492431641,196.5173492431641,196.5173492431641,196.5173492431641,196.5173492431641,196.5173492431641,192.9618606567383,193.1498641967773,193.3377990722656,193.5449676513672,193.7627487182617,193.7627487182617,193.991569519043,193.991569519043,194.2266464233398,194.4641799926758,194.7036514282227,194.7036514282227,194.9484634399414,194.9484634399414,195.1935653686523,195.4347076416016,195.4347076416016,195.6757736206055,195.6757736206055,195.9177551269531,195.9177551269531,196.1830749511719,196.419921875,196.6193542480469,196.6193542480469,196.6193542480469,196.6193542480469,196.6193542480469,196.6193542480469,193.1304550170898,193.3145446777344,193.3145446777344,193.5019760131836,193.5019760131836,193.7059097290039,193.7059097290039,193.9188690185547,194.1436767578125,194.1436767578125,194.3742828369141,194.3742828369141,194.6071548461914,194.8392562866211,194.8392562866211,195.0808944702148,195.0808944702148,195.3240966796875,195.3240966796875,195.5627288818359,195.5627288818359,195.8012542724609,195.8012542724609,196.0404510498047,196.2780380249023,196.2780380249023,196.5101699829102,196.5101699829102,196.7198181152344,196.7198181152344,196.7198181152344,196.7198181152344,193.2750244140625,193.2750244140625,193.2750244140625,193.4552764892578,193.6355895996094,193.8531799316406,193.8531799316406,194.0601043701172,194.0601043701172,194.2808380126953,194.2808380126953,194.5080795288086,194.5080795288086,194.5080795288086,194.7391815185547,194.7391815185547,194.7391815185547,194.9741973876953,195.2119369506836,195.2119369506836,195.4512634277344,195.4512634277344,195.4512634277344,195.6871109008789,195.6871109008789,195.9220428466797,196.1577835083008,196.3944473266602,196.3944473266602,196.3944473266602,196.6257247924805,196.6257247924805,196.8185653686523,196.8185653686523,196.8185653686523,196.8185653686523,196.8185653686523,196.8185653686523,193.4432525634766,193.4432525634766,193.6234283447266,193.6234283447266,193.7896041870117,193.7896041870117,193.9884719848633,193.9884719848633,194.1955261230469,194.1955261230469,194.4164733886719,194.6458206176758,194.8787841796875,194.8787841796875,195.1134567260742,195.1134567260742,195.3573684692383,195.3573684692383,195.6017608642578,195.6017608642578,195.8423233032227,195.8423233032227,196.079216003418,196.079216003418,196.3413925170898,196.3413925170898,196.5799179077148,196.8092651367188,196.9157409667969,196.9157409667969,196.9157409667969,196.9157409667969,196.9157409667969,196.9157409667969,196.9157409667969,196.9157409667969,196.9157409667969,196.9157409667969,196.9157409667969,196.9157409667969,196.9157409667969,196.9157409667969,196.9157409667969,196.9157409667969,196.9157409667969,196.9157409667969,196.9157409667969,196.9157409667969,196.9157409667969,196.9157409667969,196.9157409667969,196.9157409667969,196.9157409667969,196.9157409667969,196.9157409667969,196.9157409667969,196.9157409667969,196.9157409667969,196.9157409667969,196.9157409667969,196.9157409667969,196.9157409667969,196.9157409667969,196.9157409667969,196.9157409667969,196.9157409667969,196.9157409667969,196.9157409667969,196.9157409667969,196.9157409667969,196.9157409667969,196.9157409667969,196.9157409667969,196.9157409667969,196.9157409667969,196.9157409667969,196.9157409667969,196.9157409667969,196.9157409667969,196.9157409667969,196.9157409667969,196.9157409667969,196.9157409667969,196.9157409667969,196.9157409667969,196.9157409667969,196.9157409667969,196.9157409667969,193.5705871582031,193.5705871582031,193.5705871582031,193.5705871582031,193.6606369018555,193.6606369018555,193.8250122070312,193.8250122070312,194.0038757324219,194.1891708374023,194.1891708374023,194.3886413574219,194.3886413574219,194.6027069091797,194.6027069091797,194.833984375,195.066032409668,195.2857513427734,195.5083541870117,195.5083541870117,195.7412643432617,195.975700378418,196.2102813720703,196.2102813720703,196.4443283081055,196.6794357299805,196.9123840332031,196.9123840332031,197.0109558105469,197.0109558105469,197.0109558105469,197.0109558105469,197.0109558105469,197.0109558105469,193.8203277587891,193.9990921020508,193.9990921020508,193.9990921020508,194.1915893554688,194.1915893554688,194.1915893554688,194.3948211669922,194.3948211669922,194.6120071411133,194.837028503418,194.837028503418,195.0677185058594,195.2967147827148,195.531852722168,195.7668380737305,195.7668380737305,196.0272216796875,196.0272216796875,196.2646560668945,196.2646560668945,196.5035247802734,196.5035247802734,196.7409515380859,196.9779510498047,196.9779510498047,197.1050262451172,197.1050262451172,197.1050262451172,197.1050262451172,197.1050262451172,197.1050262451172,197.1050262451172,197.1050262451172,193.9308319091797,193.9308319091797,194.1103515625,194.1103515625,194.2942276000977,194.4879913330078,194.4879913330078,194.6945037841797,194.6945037841797,194.914909362793,194.914909362793,194.914909362793,195.1475982666016,195.1475982666016,195.1475982666016,195.3798980712891,195.6075286865234,195.6075286865234,195.6075286865234,195.8370819091797,195.8370819091797,196.0673065185547,196.3057098388672,196.3057098388672,196.5450744628906,196.5450744628906,196.7855911254883,197.0274429321289,197.1976547241211,197.1976547241211,197.1976547241211,197.1976547241211,194.0489349365234,194.0489349365234,194.2461318969727,194.2461318969727,194.4303817749023,194.627815246582,194.627815246582,194.627815246582,194.8389663696289,195.0631637573242,195.0631637573242,195.2930374145508,195.2930374145508,195.5245361328125,195.5245361328125,195.7531204223633,195.7531204223633,195.9883270263672,195.9883270263672,196.2256927490234,196.2256927490234,196.4648895263672,196.4648895263672,196.7036895751953,196.7036895751953,196.9437789916992,196.9437789916992,197.1828994750977,197.2887191772461,197.2887191772461,197.2887191772461,197.2887191772461,197.2887191772461,197.2887191772461,194.2312469482422,194.411003112793,194.5957107543945,194.5957107543945,194.7956390380859,194.7956390380859,195.0065002441406,195.2333908081055,195.2333908081055,195.4664611816406,195.4664611816406,195.6958389282227,195.9242401123047,195.9242401123047,196.15380859375,196.15380859375,196.3922576904297,196.3922576904297,196.6333389282227,196.8740997314453,196.8740997314453,197.1392517089844,197.1392517089844,197.3783111572266,197.3783111572266,197.3783111572266,197.3783111572266,197.3783111572266,197.3783111572266,194.4640121459961,194.4640121459961,194.4640121459961,194.6440963745117,194.8375778198242,195.0436553955078,195.0436553955078,195.2634811401367,195.2634811401367,195.4942474365234,195.4942474365234,195.4942474365234,195.7252044677734,195.9547271728516,196.1860046386719,196.4223175048828,196.4223175048828,196.6617279052734,196.9017715454102,197.1415939331055,197.1415939331055,197.3816299438477,197.4665756225586,197.4665756225586,197.4665756225586,197.4665756225586,197.4665756225586,197.4665756225586,194.5318450927734,194.7124786376953,194.8993072509766,194.8993072509766,195.1018600463867,195.1018600463867,195.3166046142578,195.3166046142578,195.5713653564453,195.8056411743164,195.8056411743164,196.0402603149414,196.0402603149414,196.0402603149414,196.2773818969727,196.5147476196289,196.5147476196289,196.7583465576172,196.7583465576172,196.9999771118164,196.9999771118164,197.2419128417969,197.2419128417969,197.4844055175781,197.5532608032227,197.5532608032227,197.5532608032227,197.5532608032227,194.6787414550781,194.6787414550781,194.8586196899414,195.0452728271484,195.0452728271484,195.2476043701172,195.2476043701172,195.2476043701172,195.463020324707,195.6941680908203,195.9265670776367,196.1574935913086,196.1574935913086,196.3841400146484,196.6110992431641,196.8466949462891,197.0871200561523,197.0871200561523,197.3282241821289,197.3282241821289,197.3282241821289,197.5684280395508,197.6386337280273,197.6386337280273,197.6386337280273,197.6386337280273,197.6386337280273,197.6386337280273,194.8295211791992,194.8295211791992,195.0088653564453,195.0088653564453,195.0088653564453,195.1966552734375,195.3979187011719,195.3979187011719,195.6121139526367,195.8374557495117,195.8374557495117,195.8374557495117,196.068000793457,196.068000793457,196.2975921630859,196.5265808105469,196.5265808105469,196.7549896240234,196.7549896240234,196.9901275634766,197.2298278808594,197.2298278808594,197.4701232910156,197.4701232910156,197.7092437744141,197.7092437744141,197.7225799560547,197.7225799560547,197.7225799560547,197.7225799560547,197.7225799560547,197.7225799560547,194.9820098876953,194.9820098876953,195.1604080200195,195.349983215332,195.349983215332,195.5572128295898,195.5572128295898,195.7801895141602,195.7801895141602,196.0146942138672,196.2496032714844,196.2496032714844,196.4840240478516,196.7174301147461,196.7174301147461,196.9553756713867,196.9553756713867,196.9553756713867,197.2221450805664,197.4635543823242,197.4635543823242,197.7055358886719,197.7055358886719,197.8051986694336,197.8051986694336,197.8051986694336,197.8051986694336,197.8051986694336,197.8051986694336,195.0463409423828,195.0463409423828,195.2256393432617,195.409782409668,195.6101531982422,195.6101531982422,195.8242111206055,195.8242111206055,196.0528335571289,196.0528335571289,196.2867584228516,196.2867584228516,196.5194244384766,196.5194244384766,196.7507171630859,196.7507171630859,196.9850006103516,196.9850006103516,197.226432800293,197.226432800293,197.46875,197.46875,197.7112579345703,197.7112579345703,197.8864288330078,197.8864288330078,197.8864288330078,197.8864288330078,197.8864288330078,197.8864288330078,195.1100082397461,195.2789459228516,195.2789459228516,195.2789459228516,195.4601898193359,195.6550369262695,195.8667678833008,196.1157913208008,196.1157913208008,196.3505554199219,196.5842895507812,196.5842895507812,196.8168869018555,197.0574417114258,197.2980194091797,197.5399322509766,197.5399322509766,197.7814636230469,197.9664077758789,197.9664077758789,197.9664077758789,197.9664077758789,195.2292175292969,195.2292175292969,195.2292175292969,195.3933944702148,195.5738296508789,195.5738296508789,195.769905090332,195.9809799194336,195.9809799194336,196.2097930908203,196.2097930908203,196.2097930908203,196.4477691650391,196.6837921142578,196.9188690185547,196.9188690185547,197.1587905883789,197.1587905883789,197.401237487793,197.401237487793,197.6463775634766,197.6463775634766,197.891357421875,197.891357421875,198.0450820922852,198.0450820922852,198.0450820922852,198.0450820922852,198.0450820922852,198.0450820922852,195.3711547851562,195.3711547851562,195.5559768676758,195.737922668457,195.737922668457,195.9363403320312,195.9363403320312,196.1492538452148,196.1492538452148,196.3755569458008,196.3755569458008,196.6077270507812,196.6077270507812,196.8399963378906,197.0708084106445,197.0708084106445,197.3064575195312,197.3064575195312,197.543212890625,197.543212890625,197.7812957763672,198.0199432373047,198.1224517822266,198.1224517822266,198.1224517822266,198.1224517822266,198.1224517822266,198.1224517822266,195.5180740356445,195.5180740356445,195.5180740356445,195.6920776367188,195.8738098144531,195.8738098144531,196.0739059448242,196.3088150024414,196.5375671386719,196.7710037231445,196.7710037231445,197.0029449462891,197.0029449462891,197.233154296875,197.233154296875,197.4672775268555,197.4672775268555,197.6985321044922,197.6985321044922,197.9316177368164,198.1628952026367,198.1986389160156,198.1986389160156,198.1986389160156,198.1986389160156,198.1986389160156,198.1986389160156,195.7016754150391,195.7016754150391,195.8794708251953,195.8794708251953,196.0627746582031,196.0627746582031,196.2623596191406,196.4792175292969,196.4792175292969,196.7098007202148,196.7098007202148,196.9413986206055,196.9413986206055,197.1730270385742,197.1730270385742,197.4007339477539,197.5768203735352,197.5768203735352,197.8040237426758,197.8040237426758,198.0345993041992,198.0345993041992,198.2689361572266,198.2734909057617,198.2734909057617,198.2734909057617,198.2734909057617,195.824577331543,195.824577331543,196.0007629394531,196.0007629394531,196.2031021118164,196.2031021118164,196.404052734375,196.6207122802734,196.6207122802734,196.8502960205078,197.0802993774414,197.0802993774414,197.0802993774414,197.3087539672852,197.3087539672852,197.5363464355469,197.5363464355469,197.7697830200195,197.9861068725586,197.9861068725586,198.2145462036133,198.2145462036133,198.3472290039062,198.3472290039062,198.3472290039062,198.3472290039062,198.3472290039062,198.3472290039062,195.8585433959961,195.8585433959961,196.0311126708984,196.2119522094727,196.4049987792969,196.4049987792969,196.6162643432617,196.6162643432617,196.8419342041016,196.8419342041016,196.8419342041016,197.0757217407227,197.3315124511719,197.3315124511719,197.3315124511719,197.5612564086914,197.7937698364258,198.0241088867188,198.0241088867188,198.2552642822266,198.2552642822266,198.419792175293,198.419792175293,198.419792175293,198.419792175293,195.9284362792969,196.1033325195312,196.1033325195312,196.3024749755859,196.3024749755859,196.4990081787109,196.7083511352539,196.7083511352539,196.9337005615234,196.9337005615234,197.1684875488281,197.1684875488281,197.1684875488281,197.4021987915039,197.4021987915039,197.6334609985352,197.6334609985352,197.867057800293,197.867057800293,198.1100769042969,198.1100769042969,198.1100769042969,198.3533325195312,198.4910583496094,198.4910583496094,198.4910583496094,198.4910583496094,198.4910583496094,198.4910583496094,196.0885543823242,196.2649536132812,196.2649536132812,196.449836730957,196.6511764526367,196.6511764526367,196.86962890625,197.1029281616211,197.3389205932617,197.573356628418,197.8111267089844,198.0529022216797,198.0529022216797,198.2952194213867,198.2952194213867,198.2952194213867,198.5378799438477,198.5612945556641,198.5612945556641,198.5612945556641,198.5612945556641,196.2738800048828,196.4542617797852,196.6454620361328,196.6454620361328,196.8535766601562,196.8535766601562,197.0797958374023,197.0797958374023,197.3143768310547,197.3143768310547,197.5497589111328,197.7860565185547,197.7860565185547,198.0250549316406,198.0250549316406,198.2635955810547,198.2635955810547,198.5301132202148,198.5301132202148,198.6303482055664,198.6303482055664,198.6303482055664,198.6303482055664,198.6303482055664,198.6303482055664,198.6303482055664,198.6303482055664,198.6303482055664,198.6303482055664,198.6303482055664,198.6303482055664,198.6303482055664,198.6303482055664,198.6303482055664,198.6303482055664,198.6303482055664,198.6303482055664,198.6303482055664,198.6303482055664,198.6303482055664,198.6303482055664,198.6303482055664,198.6303482055664,196.2763900756836,196.2763900756836,196.416618347168,196.416618347168,196.416618347168,196.5822525024414,196.5822525024414,196.7627105712891,196.9551315307617,196.9551315307617,197.1652069091797,197.1652069091797,197.414176940918,197.414176940918,197.6515960693359,197.6515960693359,197.8876190185547,197.8876190185547,197.8876190185547,198.1230850219727,198.1230850219727,198.3556060791016,198.3556060791016,198.5960159301758,198.5960159301758,198.5960159301758,198.6981887817383,198.6981887817383,198.6981887817383,198.6981887817383,196.4239959716797,196.4239959716797,196.4239959716797,196.6010589599609,196.6010589599609,196.7837295532227,196.7837295532227,196.9867324829102,196.9867324829102,197.2074890136719,197.2074890136719,197.441047668457,197.441047668457,197.441047668457,197.6781158447266,197.6781158447266,197.6781158447266,197.9129028320312,197.9129028320312,198.1554641723633,198.3979568481445,198.3979568481445,198.6419296264648,198.7650604248047,198.7650604248047,198.7650604248047,198.7650604248047,196.5170059204102,196.5170059204102,196.6956787109375,196.6956787109375,196.881477355957,196.881477355957,196.881477355957,197.1052093505859,197.1052093505859,197.3280563354492,197.3280563354492,197.5643005371094,197.8023529052734,197.8023529052734,198.0391311645508,198.0391311645508,198.2815780639648,198.2815780639648,198.527458190918,198.527458190918,198.527458190918,198.7742080688477,198.7742080688477,198.8308715820312,198.8308715820312,198.8308715820312,198.8308715820312,198.8308715820312,198.8308715820312,196.6647644042969,196.6647644042969,196.844856262207,197.0324401855469,197.0324401855469,197.2389068603516,197.2389068603516,197.4610824584961,197.4610824584961,197.6984786987305,197.6984786987305,197.9357452392578,197.9357452392578,198.1717758178711,198.1717758178711,198.4102096557617,198.4102096557617,198.6520309448242,198.6520309448242,198.8955993652344,198.8955993652344,198.8955993652344,198.8955993652344,198.8955993652344,198.8955993652344,198.8955993652344,198.8955993652344,198.8955993652344,196.8077087402344,196.8077087402344,197.0078201293945,197.2002639770508,197.2002639770508,197.4113693237305,197.4113693237305,197.4113693237305,197.640754699707,197.640754699707,197.8772354125977,198.1125869750977,198.1125869750977,198.346809387207,198.346809387207,198.5883026123047,198.5883026123047,198.8309631347656,198.8309631347656,198.9592742919922,198.9592742919922,198.9592742919922,198.9592742919922,198.9592742919922,198.9592742919922,196.8104095458984,196.8104095458984,196.9865493774414,196.9865493774414,196.9865493774414,197.1704177856445,197.1704177856445,197.3700103759766,197.5871887207031,197.5871887207031,197.8191909790039,197.8191909790039,198.0560607910156,198.0560607910156,198.2905197143555,198.2905197143555,198.5254592895508,198.5254592895508,198.765625,199.0077133178711,199.0077133178711,199.0219345092773,199.0219345092773,199.0219345092773,199.0219345092773,196.9896011352539,196.9896011352539,197.1866989135742,197.1866989135742,197.3761138916016,197.5844497680664,197.5844497680664,197.811637878418,198.0461959838867,198.2811660766602,198.5157699584961,198.7536468505859,198.9972534179688,198.9972534179688,199.0835876464844,199.0835876464844,199.0835876464844,199.0835876464844,199.0835876464844,199.0835876464844,197.0336456298828,197.0336456298828,197.2096481323242,197.2096481323242,197.3912124633789,197.5894470214844,197.5894470214844,197.8047561645508,198.0356292724609,198.0356292724609,198.2725067138672,198.5048522949219,198.5048522949219,198.7591705322266,199.0014343261719,199.144287109375,199.144287109375,199.144287109375,199.144287109375,199.144287109375,199.144287109375,197.0796737670898,197.0796737670898,197.2553939819336,197.4385833740234,197.4385833740234,197.6333389282227,197.6333389282227,197.8498764038086,197.8498764038086,198.0769271850586,198.0769271850586,198.0769271850586,198.3143539428711,198.3143539428711,198.5735015869141,198.5735015869141,198.8086624145508,198.8086624145508,199.0425491333008,199.2038879394531,199.2038879394531,199.2038879394531,199.2038879394531,197.1578903198242,197.1578903198242,197.1578903198242,197.3292083740234,197.5109252929688,197.5109252929688,197.7011413574219,197.7011413574219,197.9329452514648,198.1613159179688,198.4004516601562,198.4004516601562,198.6383590698242,198.6383590698242,198.8738708496094,198.8738708496094,199.1140747070312,199.1140747070312,199.2627029418945,199.2627029418945,199.2627029418945,199.2627029418945,199.2627029418945,199.2627029418945,197.2557144165039,197.4446792602539,197.4446792602539,197.6267776489258,197.8184661865234,198.0325469970703,198.2621994018555,198.2621994018555,198.4981918334961,198.4981918334961,198.733039855957,198.733039855957,198.9660797119141,199.2059555053711,199.320442199707,199.320442199707,199.320442199707,199.320442199707,197.3864822387695,197.3864822387695,197.5612335205078,197.7422180175781,197.9416656494141,197.9416656494141,198.1587677001953,198.1587677001953,198.1587677001953,198.3871994018555,198.3871994018555,198.6225814819336,198.8554458618164,199.1107559204102,199.3465957641602,199.3465957641602,199.3772888183594,199.3772888183594,199.3772888183594,199.3772888183594,199.3772888183594,199.3772888183594,197.5110549926758,197.5110549926758,197.6905670166016,197.6905670166016,197.8475799560547,197.8475799560547,197.8475799560547,198.0604095458984,198.275016784668,198.275016784668,198.50439453125,198.50439453125,198.50439453125,198.7381362915039,198.7381362915039,198.9718475341797,198.9718475341797,199.2031555175781,199.2031555175781,199.4309005737305,199.4309005737305,199.4332885742188,199.4332885742188,199.4332885742188,199.4332885742188,197.6484603881836,197.6484603881836,197.8263931274414,197.8263931274414,198.016242980957,198.016242980957,198.2240447998047,198.2240447998047,198.4482879638672,198.4482879638672,198.4482879638672,198.6814270019531,198.9150695800781,198.9150695800781,199.146614074707,199.3795852661133,199.4883270263672,199.4883270263672,199.4883270263672,199.4883270263672,199.4883270263672,199.4883270263672,197.6522369384766,197.6522369384766,197.8272018432617,197.8272018432617,198.0109100341797,198.0109100341797,198.2121353149414,198.4292678833008,198.4292678833008,198.4292678833008,198.6584167480469,198.8923645019531,198.8923645019531,199.1241607666016,199.1241607666016,199.3773422241211,199.54248046875,199.54248046875,199.54248046875,199.54248046875,199.54248046875,199.54248046875,199.54248046875,199.54248046875,199.54248046875,199.54248046875,199.54248046875,199.54248046875,199.54248046875,199.54248046875,199.54248046875,199.54248046875,199.54248046875,199.54248046875,199.54248046875,199.54248046875,199.54248046875,197.6793975830078,197.6793975830078,197.6793975830078,197.7358856201172,197.9020614624023,197.9020614624023,198.0808715820312,198.0808715820312,198.273193359375,198.4838943481445,198.7066192626953,198.7066192626953,198.9447631835938,198.9447631835938,199.1790237426758,199.1790237426758,199.4027328491211,199.4027328491211,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,199.5955810546875,197.7626876831055,197.7626876831055,197.7626876831055,197.7626876831055,197.9239807128906,197.9239807128906,197.9239807128906,198.1206970214844,198.1206970214844,198.3280868530273,198.3280868530273,198.5533981323242,198.5533981323242,198.7908554077148,198.7908554077148,199.0219268798828,199.0219268798828,199.0219268798828,199.2455368041992,199.4553985595703,199.6987380981445,199.6987380981445,199.9218063354492,199.9218063354492,200.1541213989258,200.1541213989258,200.3871612548828,200.3871612548828,200.6198196411133,200.6198196411133,200.8528213500977,200.8528213500977,201.0498962402344,201.0498962402344,201.2450332641602,201.2450332641602,201.4393310546875,201.633903503418,201.633903503418,201.633903503418,201.8284683227539,201.8284683227539,202.0420455932617,202.0420455932617,202.235466003418,202.4286193847656,202.4286193847656,202.6228485107422,202.8164138793945,202.8164138793945,203.0106811523438,203.0106811523438,203.2014617919922,203.3924865722656,203.3924865722656,203.5839996337891,203.7757720947266,203.7757720947266,203.9891052246094,203.9891052246094,204.1831817626953,204.3769454956055,204.3769454956055,204.3769454956055,204.5727844238281,204.5727844238281,204.7689514160156,204.7689514160156,204.9570541381836,204.9570541381836,204.9570541381836,205.1525497436523,205.1525497436523,205.3484115600586,205.4114074707031,205.4114074707031,205.4114074707031,205.4114074707031,205.4114074707031,205.4114074707031,198.2336273193359,198.2336273193359,198.4282531738281,198.4282531738281,198.4282531738281,198.6309051513672,198.6309051513672,198.8488693237305,198.8488693237305,199.0820541381836,199.0820541381836,199.3132171630859,199.3132171630859,199.531623840332,199.531623840332,199.7505111694336,199.98828125,199.98828125,200.2435302734375,200.2435302734375,200.4767761230469,200.4767761230469,200.7101211547852,200.9419403076172,200.9419403076172,201.1720275878906,201.1720275878906,201.4031448364258,201.4031448364258,201.6335144042969,201.6335144042969,201.6335144042969,201.8656997680664,202.0931167602539,202.0931167602539,202.3225936889648,202.3225936889648,202.5535202026367,202.5535202026367,202.7849655151367,202.7849655151367,203.0160903930664,203.0160903930664,203.0160903930664,203.2462997436523,203.2462997436523,203.4776077270508,203.4776077270508,203.706787109375,203.706787109375,203.9390563964844,204.1737060546875,204.1737060546875,204.4076156616211,204.4076156616211,204.6424331665039,204.8750839233398,204.8750839233398,205.1055145263672,205.326789855957,205.5478210449219,205.5478210449219,205.6206665039062,205.6206665039062,205.6206665039062,205.6206665039062,205.6206665039062,205.6206665039062,205.6206665039062,205.6206665039062,205.6206665039062,198.5630874633789,198.5630874633789,198.5630874633789,198.7564926147461,198.9573440551758,198.9573440551758,199.1707382202148,199.1707382202148,199.3965682983398,199.3965682983398,199.621696472168,199.621696472168,199.8363723754883,199.8363723754883,200.0716552734375,200.0716552734375,200.3104553222656,200.3104553222656,200.5442428588867,200.5442428588867,200.7779769897461,200.7779769897461,201.0124893188477,201.2459030151367,201.4785308837891,201.7147903442383,201.7147903442383,201.9499130249023,201.9499130249023,202.1843643188477,202.1843643188477,202.4193344116211,202.4193344116211,202.6530456542969,202.8852233886719,202.8852233886719,203.1175842285156,203.1175842285156,203.3491744995117,203.3491744995117,203.5828475952148,203.8161239624023,203.8161239624023,203.8161239624023,204.0582046508789,204.3014907836914,204.3014907836914,204.540641784668,204.7811126708984,205.0235748291016,205.0235748291016,205.2655563354492,205.2655563354492,205.2655563354492,205.4962844848633,205.4962844848633,205.7496719360352,205.8264770507812,205.8264770507812,205.8264770507812,205.8264770507812,205.8264770507812,205.8264770507812,198.8586196899414,198.8586196899414,199.0486373901367,199.2463989257812,199.4540328979492,199.4540328979492,199.6745758056641,199.6745758056641,199.897087097168,199.897087097168,199.897087097168,200.1157073974609,200.1157073974609,200.3573379516602,200.3573379516602,200.5972366333008,200.5972366333008,200.8327713012695,201.0676651000977,201.0676651000977,201.302490234375,201.302490234375,201.5362243652344,201.5362243652344,201.7716751098633,201.7716751098633,202.0045547485352,202.0045547485352,202.0045547485352,202.2382965087891,202.2382965087891,202.4699096679688,202.4699096679688,202.7015914916992,202.7015914916992,202.9314651489258,203.1837768554688,203.1837768554688,203.4150085449219,203.4150085449219,203.6482849121094,203.6482849121094,203.8791580200195,203.8791580200195,204.1106109619141,204.1106109619141,204.3404693603516,204.5677108764648,204.5677108764648,204.7958908081055,204.7958908081055,205.0269317626953,205.0269317626953,205.2586364746094,205.4891510009766,205.4891510009766,205.7335968017578,205.7335968017578,205.7335968017578,205.9571304321289,205.9571304321289,206.0289535522461,206.0289535522461,206.0289535522461,206.0289535522461,206.0289535522461,206.0289535522461,206.0289535522461,206.0289535522461,206.0289535522461,199.1667404174805,199.1667404174805,199.3558959960938,199.3558959960938,199.5547103881836,199.5547103881836,199.7824783325195,199.7824783325195,199.9955368041992,199.9955368041992,200.2050094604492,200.4359588623047,200.4359588623047,200.6753082275391,200.6753082275391,200.6753082275391,200.9116516113281,201.1436462402344,201.1436462402344,201.3754577636719,201.3754577636719,201.6069564819336,201.6069564819336,201.8377685546875,202.0913925170898,202.0913925170898,202.3244094848633,202.5574417114258,202.5574417114258,202.7766494750977,202.7766494750977,203.0087661743164,203.2396926879883,203.4664764404297,203.6920700073242,203.6920700073242,203.9188461303711,203.9188461303711,204.1451644897461,204.1451644897461,204.3722152709961,204.3722152709961,204.5991439819336,204.5991439819336,204.5991439819336,204.8277740478516,204.8277740478516,205.0561752319336,205.2864456176758,205.5165328979492,205.5165328979492,205.7445068359375,205.9729080200195,205.9729080200195,206.1956024169922,206.1956024169922,206.2282409667969,206.2282409667969,206.2282409667969,206.2282409667969,206.2282409667969,206.2282409667969,206.2282409667969,206.2282409667969,206.2282409667969,199.5172424316406,199.5172424316406,199.710075378418,199.9080810546875,200.1154251098633,200.1154251098633,200.3218383789062,200.3218383789062,200.5316772460938,200.5316772460938,200.5316772460938,200.768928527832,200.768928527832,200.768928527832,201.0055084228516,201.0055084228516,201.2409896850586,201.2409896850586,201.4720611572266,201.4720611572266,201.4720611572266,201.704216003418,201.704216003418,201.704216003418,201.9377822875977,201.9377822875977,202.1713256835938,202.1713256835938,202.1713256835938,202.4055633544922,202.4055633544922,202.6433486938477,202.6433486938477,202.8761901855469,202.8761901855469,203.1182327270508,203.1182327270508,203.3522796630859,203.3522796630859,203.5852890014648,203.5852890014648,203.8197250366211,204.0552825927734,204.0552825927734,204.29052734375,204.29052734375,204.5221557617188,204.7582321166992,204.7582321166992,204.9887619018555,204.9887619018555,205.2419891357422,205.2419891357422,205.2419891357422,205.4733047485352,205.7041778564453,205.7041778564453,205.9343872070312,206.1642990112305,206.1642990112305,206.3966598510742,206.3966598510742,206.4242095947266,206.4242095947266,206.4242095947266,206.4242095947266,206.4242095947266,206.4242095947266,199.8035888671875,199.8035888671875,199.994140625,199.994140625,200.1924667358398,200.1924667358398,200.1924667358398,200.3898544311523,200.3898544311523,200.590461730957,200.590461730957,200.804557800293,201.0405807495117,201.2779922485352,201.5153427124023,201.7462692260742,201.976203918457,201.976203918457,202.205207824707,202.4352035522461,202.4352035522461,202.6663665771484,202.8957061767578,202.8957061767578,203.1268081665039,203.3796691894531,203.6089630126953,203.6089630126953,203.8406295776367,203.8406295776367,204.0714569091797,204.3035049438477,204.3035049438477,204.5374069213867,204.5374069213867,204.7709884643555,204.7709884643555,205.0045776367188,205.2375640869141,205.2375640869141,205.4716415405273,205.4716415405273,205.7050323486328,205.7050323486328,205.9412307739258,205.9412307739258,205.9412307739258,206.1743011474609,206.1743011474609,206.4025268554688,206.6171340942383,206.6171340942383,206.6171340942383,206.6171340942383,206.6171340942383,206.6171340942383,206.6171340942383,206.6171340942383,206.6171340942383,206.6171340942383,206.6171340942383,206.6171340942383,206.6171340942383,206.6171340942383,206.6171340942383,206.6171340942383,206.6171340942383,206.6171340942383,206.6171340942383,206.6171340942383,206.6171340942383,206.6171340942383,206.6171340942383,206.6171340942383,206.6171340942383,206.6171340942383,206.6171340942383,206.6171340942383,206.6171340942383,206.6171340942383,199.9808807373047,199.9808807373047,199.9808807373047,199.9808807373047,199.9808807373047,199.9808807373047,199.9925308227539,200.1730422973633,200.1730422973633,200.3655395507812,200.3655395507812,200.5605316162109,200.5605316162109,200.758659362793,200.9635467529297,201.1986846923828,201.4354019165039,201.4354019165039,201.6597518920898,201.8874282836914,201.8874282836914,202.1075668334961,202.3380889892578,202.3380889892578,202.5744857788086,202.5744857788086,202.8090438842773,202.8090438842773,203.046745300293,203.2845840454102,203.2845840454102,203.5209350585938,203.7553939819336,203.7553939819336,203.7553939819336,203.9916305541992,203.9916305541992,204.2297592163086,204.4648895263672,204.703010559082,204.9428405761719,204.9428405761719,204.9428405761719,205.2078018188477,205.2078018188477,205.4452056884766,205.4452056884766,205.6860198974609,205.6860198974609,205.9246368408203,205.9246368408203,206.1637802124023,206.4026031494141,206.4026031494141,206.6376342773438,206.8067398071289,206.8067398071289,206.8067398071289,206.8067398071289,206.8067398071289,206.8067398071289,206.8067398071289,206.8067398071289,206.8067398071289,200.304573059082,200.304573059082,200.4893035888672,200.6829299926758,200.6829299926758,200.8752212524414,201.0699996948242,201.0699996948242,201.2893753051758,201.2893753051758,201.5243225097656,201.5243225097656,201.760871887207,201.760871887207,201.760871887207,201.996337890625,202.2307739257812,202.2307739257812,202.4633483886719,202.696159362793,202.696159362793,202.9283294677734,202.9283294677734,203.1612167358398,203.3897933959961,203.3897933959961,203.6216659545898,203.879020690918,203.879020690918,204.1097717285156,204.1097717285156,204.3414001464844,204.5747833251953,204.8063049316406,204.8063049316406,205.0443572998047,205.2797012329102,205.2797012329102,205.5222091674805,205.5222091674805,205.7634811401367,205.7634811401367,205.7634811401367,206.0049285888672,206.0049285888672,206.2459106445312,206.4860687255859,206.4860687255859,206.7208557128906,206.7208557128906,206.9618453979492,206.9618453979492,206.9934387207031,206.9934387207031,206.9934387207031,206.9934387207031,206.9934387207031,206.9934387207031,200.6709289550781,200.6709289550781,200.8587493896484,201.0510482788086,201.0510482788086,201.2393417358398,201.2393417358398,201.4447631835938,201.4447631835938,201.6693725585938,201.9033508300781,202.1346282958984,202.3637924194336,202.3637924194336,202.6143646240234,202.6143646240234,202.842658996582,202.842658996582,203.0703811645508,203.0703811645508,203.3023529052734,203.3023529052734,203.5383911132812,203.5383911132812,203.5383911132812,203.7770156860352,203.7770156860352,204.0147857666016,204.0147857666016,204.2527694702148,204.2527694702148,212.0829544067383,212.0829544067383,212.0829544067383,212.0829544067383,212.0829544067383,212.0829544067383,212.0829544067383,212.0829544067383,212.0829544067383,212.0829544067383,212.0829544067383,212.0829544067383,212.0829544067383,212.0829544067383,212.0829544067383,212.0829544067383,212.0829544067383,212.0829544067383,212.0829544067383,212.0829544067383,212.0829544067383,212.0829544067383,212.0829544067383,212.0829544067383,219.7123489379883,219.7123565673828,219.7123565673828,219.7123565673828,219.7123565673828,219.7123565673828,219.7123565673828,219.7123565673828,219.7123565673828,219.7123565673828,219.7123565673828,219.7123565673828,219.7123565673828,219.7123565673828,219.7123565673828,219.7123565673828,219.7123565673828,219.7123565673828,219.7123565673828,219.7123565673828,219.7123565673828,219.7123565673828,219.7123565673828,219.7123565673828,219.7123565673828,234.9711456298828,234.9711456298828,234.9711456298828,234.9711456298828,234.9711456298828,234.9711456298828,234.9711456298828,234.9711456298828,234.9711456298828,234.9711456298828,234.9711456298828,234.9711456298828,234.9711456298828,234.9711456298828,234.9711456298828,234.9711456298828,234.9711456298828,234.9711456298828,234.9711456298828,234.9711456298828,242.6005630493164,242.6005630493164,242.6005630493164,242.6005630493164,242.6005630493164,242.6005630493164,242.6005630493164,242.6005630493164,242.7273712158203,242.7273712158203,242.7273712158203,242.7273712158203,242.7273712158203,242.7273712158203,242.7273712158203,242.7273712158203,242.7273712158203,242.7273712158203,242.7273712158203,242.7273712158203,242.7273712158203,242.7273712158203,242.7273712158203,242.7273712158203,242.7273712158203,242.7273712158203,242.7273712158203,242.7273712158203,242.7273712158203,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406,257.9957580566406],"meminc":[0,0,0,0,0,0,15.28223419189453,0,0,0,0,0,30.46574401855469,0,0,0,0,0,0,0,0,0,4.57763671875e-05,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-0.00030517578125,0,0,0,15.41991424560547,0,0.1906585693359375,0.197906494140625,0,0.2026824951171875,0.2194900512695312,0,0,0.2341079711914062,0,0.2398757934570312,0,0.2310562133789062,0,0.2294769287109375,0.2271652221679688,0.2298202514648438,0,0.2315139770507812,0.2382431030273438,0,0.2375717163085938,0.1895751953125,0,0,0,0,0,-2.891639709472656,0,0.2372207641601562,0,0.2432327270507812,0,0,0.2639694213867188,0.2391357421875,0,0.2353439331054688,0.23175048828125,0,0.2311019897460938,0,0.2299270629882812,0,0.2293472290039062,0,0.2308807373046875,0,0.2303924560546875,0,0.230560302734375,0.1286239624023438,0,0,-2.981353759765625,0,0,0.2220230102539062,0.237945556640625,0,0.2399826049804688,0.2395477294921875,0,0,0.2389755249023438,0.2337570190429688,0,0,0.2318496704101562,0.2335128784179688,0,0.2330856323242188,0.2331466674804688,0,0.2321624755859375,0,0.2328643798828125,0,0.2300186157226562,0.02951812744140625,0,0,0,-2.847732543945312,0,0.2237396240234375,0,0.241790771484375,0,0.2437515258789062,0,0.2665557861328125,0,0,0.234832763671875,0.2350845336914062,0,0.233734130859375,0,0.2323150634765625,0,0.2318267822265625,0,0.2333602905273438,0.23358154296875,0,0.2343063354492188,0.08856964111328125,0,0,-2.857948303222656,0.2187118530273438,0.2332687377929688,0.2409744262695312,0.2377700805664062,0,0.2371139526367188,0,0.2358551025390625,0,0.2319183349609375,0,0.2336883544921875,0.2326736450195312,0.2345123291015625,0,0.2325515747070312,0.2312088012695312,0.141998291015625,0,0,0,-2.863418579101562,0.2178726196289062,0.2313461303710938,0.2446060180664062,0,0.2426910400390625,0.2370223999023438,0,0.2596359252929688,0.2319183349609375,0,0.2333297729492188,0,0.230865478515625,0.2311553955078125,0,0.2305831909179688,0,0.2296829223632812,0,0.1256561279296875,0,0,-2.806892395019531,0,0.216217041015625,0.2322616577148438,0,0.243011474609375,0,0.239349365234375,0,0.2378082275390625,0,0.236541748046875,0,0.2341079711914062,0,0.2312469482421875,0,0.2314605712890625,0,0.2336654663085938,0.23236083984375,0,0.2314529418945312,0,0.08898162841796875,0,0,-2.731559753417969,0.2143402099609375,0,0.2330093383789062,0,0.2409133911132812,0,0.235687255859375,0,0,0.2361907958984375,0,0.2346038818359375,0,0.2310867309570312,0,0.2518768310546875,0.23138427734375,0,0.2334518432617188,0,0.2323379516601562,0.2322845458984375,0,0,0.00472259521484375,0,0,-2.620841979980469,0.2137298583984375,0.2363052368164062,0,0.2386627197265625,0,0,0.2379302978515625,0,0.2363815307617188,0,0,0.2322006225585938,0.230865478515625,0,0.2310867309570312,0,0.2329177856445312,0,0.2337417602539062,0,0.2340164184570312,0.1419754028320312,0,0,-2.689239501953125,0,0.2194976806640625,0,0.229583740234375,0.2422561645507812,0.237091064453125,0,0,0.2366943359375,0,0.2341537475585938,0,0.23333740234375,0,0.2344436645507812,0,0,0.2333526611328125,0,0.2579498291015625,0,0.2347869873046875,0,0.1737899780273438,0,0,0,-2.471748352050781,0,0.2262496948242188,0.2384109497070312,0,0.2381668090820312,0,0.23577880859375,0,0.2356796264648438,0,0.2353668212890625,0,0.2319793701171875,0.2307510375976562,0.2312545776367188,0,0.2330093383789062,0,0.2116165161132812,0,0,0,0,0,-2.463066101074219,0.2259445190429688,0.241302490234375,0,0.2406845092773438,0.236480712890625,0,0.2349166870117188,0,0,0.23553466796875,0.2347564697265625,0,0,0.2361984252929688,0,0.2356643676757812,0,0.2444076538085938,0,0.1723480224609375,0,0,-2.5653076171875,0.2137069702148438,0,0.2319717407226562,0,0.2348709106445312,0.2384109497070312,0,0.2370758056640625,0.2360687255859375,0.2356109619140625,0.2340927124023438,0.2299728393554688,0.2310028076171875,0.2291183471679688,0,0.08742523193359375,0,0,-2.481056213378906,0,0.210235595703125,0.2228240966796875,0,0,0.2330322265625,0,0,0.2320098876953125,0.2329788208007812,0,0.2340850830078125,0,0.2331924438476562,0,0.2320480346679688,0.2294769287109375,0,0,0.2333602905273438,0.239349365234375,0,0.02126312255859375,0,0,-2.382850646972656,0,0,0.214935302734375,0,0.2268905639648438,0,0.2587661743164062,0.2338180541992188,0,0.2365036010742188,0,0.2346115112304688,0,0.2330322265625,0,0.2286453247070312,0,0.233123779296875,0.2363433837890625,0.1178512573242188,0,0,-2.4267578125,0.20892333984375,0,0.2208251953125,0.2339019775390625,0.23162841796875,0.2340316772460938,0,0.2354736328125,0.2344894409179688,0,0.2333526611328125,0,0.2314453125,0,0.2327117919921875,0,0.2003860473632812,0,0,0,0,0,0,0,-2.259353637695312,0,0,0.2132339477539062,0,0.2254867553710938,0.2324600219726562,0,0.2366485595703125,0.2357101440429688,0,0.236083984375,0.25701904296875,0,0.2344207763671875,0,0.2360305786132812,0,0.2216339111328125,0,0,0,0,0,-2.2440185546875,0.1870269775390625,0,0.1923446655273438,0,0.20806884765625,0,0.22601318359375,0,0.2381057739257812,0,0.23583984375,0,0.2356109619140625,0.2336349487304688,0,0,0.2319717407226562,0,0.2337188720703125,0,0.08988189697265625,0,0,-2.296073913574219,0,0.2049102783203125,0.212371826171875,0.2188186645507812,0,0.2340850830078125,0,0.2272415161132812,0.2276153564453125,0,0.2363433837890625,0.2327728271484375,0.2547149658203125,0,0.2355422973632812,0.078765869140625,0,0,-2.252983093261719,0.2009048461914062,0,0.2087860107421875,0,0,0.2245864868164062,0.2355422973632812,0,0.2371902465820312,0.2364349365234375,0,0.2347869873046875,0.2335662841796875,0.2407684326171875,0.2435226440429688,0,0.02294921875,0,0,-2.162200927734375,0.2025222778320312,0,0,0.211395263671875,0.2290420532226562,0,0.2360153198242188,0,0.236541748046875,0,0.2352981567382812,0,0.2338027954101562,0.2387542724609375,0.2444381713867188,0,0.1593475341796875,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2.184806823730469,0,0.1730194091796875,0,0.178985595703125,0.1852035522460938,0.1992645263671875,0,0.2170639038085938,0.228363037109375,0.2312774658203125,0.2227859497070312,0,0.2254867553710938,0,0.2261886596679688,0,0.160980224609375,0,0,0,-2.02227783203125,0,0.2001953125,0,0.2382965087890625,0.2325210571289062,0,0.2347869873046875,0,0.2354736328125,0,0.23443603515625,0,0.2335128784179688,0.2408676147460938,0.2351455688476562,0,0,0,-2.040626525878906,0,0.1980438232421875,0.2093658447265625,0,0,0.2283248901367188,0,0.232818603515625,0,0.2324447631835938,0.232025146484375,0,0.23162841796875,0,0.2322845458984375,0.2393951416015625,0,0.06621551513671875,0,0,-2.067390441894531,0,0.1972198486328125,0,0.2040634155273438,0,0.2210769653320312,0,0.2323455810546875,0,0.23431396484375,0.2340621948242188,0,0.233367919921875,0,0,0.2559890747070312,0,0.239715576171875,0,0.0761566162109375,0,0,-2.054840087890625,0.1891632080078125,0.203155517578125,0,0,0.22125244140625,0,0.2365875244140625,0,0.2391891479492188,0,0.2368316650390625,0,0.2381515502929688,0,0,0.2421951293945312,0,0.2427902221679688,0,0.06546783447265625,0,0,-2.0009765625,0.196990966796875,0,0.204681396484375,0.2263565063476562,0.2378768920898438,0.2337722778320312,0,0.23773193359375,0.2360382080078125,0,0.23248291015625,0.2321701049804688,0,0.02178192138671875,0,0,-1.958198547363281,0,0.2058792114257812,0,0.2082901000976562,0,0.2246170043945312,0,0.2361221313476562,0,0.2364349365234375,0.2366485595703125,0.23583984375,0,0.2441558837890625,0.1882476806640625,0,0,0,0,0,-1.840095520019531,0.1964645385742188,0.2139053344726562,0.2320480346679688,0.2349700927734375,0.2381744384765625,0.2341842651367188,0,0.2408905029296875,0,0.2432174682617188,0,0.0633392333984375,0,0,-1.905654907226562,0,0.1927413940429688,0,0.2047805786132812,0.2233810424804688,0,0.2354202270507812,0.2387161254882812,0,0.2384719848632812,0,0.2443923950195312,0,0.2686996459960938,0.1151123046875,0,-1.916061401367188,0,0.1888198852539062,0,0.2009429931640625,0,0.2197265625,0.2370071411132812,0,0.2402267456054688,0,0.2392196655273438,0,0.2416229248046875,0,0.2445602416992188,0,0.1592254638671875,0,0,0,-1.72894287109375,0,0,0.1986618041992188,0,0.21514892578125,0,0.2328033447265625,0,0.23406982421875,0,0.2369155883789062,0,0,0.234100341796875,0,0.2326889038085938,0,0.198944091796875,0,0,0,-1.748733520507812,0,0,0.1912307739257812,0.2075881958007812,0,0.2453155517578125,0.2364578247070312,0.2359237670898438,0,0.2358551025390625,0,0.2324447631835938,0.2173080444335938,0,0,0,0,0,0,0,-1.732925415039062,0.1901321411132812,0,0.2070236206054688,0,0.2279891967773438,0,0.2352676391601562,0,0.2375946044921875,0.2378082275390625,0,0,0.24444580078125,0,0.2053146362304688,0,0,0,0,0,-1.682777404785156,0.1956100463867188,0,0.213592529296875,0,0.2331466674804688,0.2395248413085938,0,0.23974609375,0,0.2388458251953125,0.2440185546875,0,0.1300430297851562,0,0,-1.763557434082031,0.1851959228515625,0.1988143920898438,0.2170639038085938,0.2331390380859375,0.2361907958984375,0,0.2354965209960938,0,0.2358322143554688,0,0.2429275512695312,0,0.02978515625,0,0,-1.681045532226562,0,0.191131591796875,0,0.2069244384765625,0.225982666015625,0,0.2384262084960938,0,0.2390365600585938,0,0.2386245727539062,0,0.2426681518554688,0.1483383178710938,0,0,0,0,0,-1.553421020507812,0,0.198486328125,0,0,0.2171630859375,0.2332839965820312,0,0.2370452880859375,0,0.2355575561523438,0.2364730834960938,0,0.2434234619140625,0,0,0.00125885009765625,0,-1.584907531738281,0,0,0.1949310302734375,0,0.2132186889648438,0,0.2309494018554688,0,0,0.2411346435546875,0.2389984130859375,0.2391433715820312,0,0.2366790771484375,0.038330078125,0,-1.609169006347656,0,0.187957763671875,0,0,0.2032470703125,0.2229843139648438,0,0.2377700805664062,0,0.2386398315429688,0,0.2367706298828125,0.2408599853515625,0.088653564453125,0,0,0,-1.614883422851562,0.1874008178710938,0,0.2015914916992188,0,0.2212448120117188,0,0.2372665405273438,0,0,0.238800048828125,0.2603073120117188,0.2405014038085938,0,0.0747222900390625,0,-1.587699890136719,0.17547607421875,0.2026138305664062,0.2205047607421875,0,0.236541748046875,0,0.23956298828125,0,0,0.2385101318359375,0.2413787841796875,0.079315185546875,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.589927673339844,0,0,0,0.1054611206054688,0,0.1928634643554688,0,0.2035598754882812,0,0.2233734130859375,0,0.2379302978515625,0,0.227264404296875,0,0.216644287109375,0.2244796752929688,0,0.2381210327148438,0,0.2480239868164062,0.24273681640625,0.2367630004882812,0.2306289672851562,0,0.1975326538085938,0,0.19732666015625,0.1963882446289062,0.1965866088867188,0,0.1958465576171875,0,0.1942672729492188,0,0.1953506469726562,0.1947250366210938,0,0,0.1956329345703125,0.1930465698242188,0,0,0.05584716796875,0,-4.599403381347656,0.2122726440429688,0,0.2321548461914062,0,0.24005126953125,0,0.236175537109375,0,0.2232742309570312,0,0.2129592895507812,0,0.2405776977539062,0.2444381713867188,0.2443923950195312,0.2426223754882812,0.2408599853515625,0.2388458251953125,0,0.2382736206054688,0.237457275390625,0,0,0.2372055053710938,0,0.2368927001953125,0,0.2376251220703125,0,0.2365798950195312,0.2326812744140625,0.2305831909179688,0.03592681884765625,0,0,-4.539131164550781,0,0.2047805786132812,0,0.2226943969726562,0,0.2363510131835938,0,0.2316513061523438,0,0,0.2393417358398438,0,0.2255096435546875,0,0,0.239898681640625,0,0.2473831176757812,0,0,0.247222900390625,0,0.2430496215820312,0,0.2407608032226562,0,0.2371139526367188,0.2385940551757812,0,0.2381057739257812,0,0.2384719848632812,0,0.2378082275390625,0,0,0.23968505859375,0,0,0.241607666015625,0.2327041625976562,0,0.1866836547851562,0,0,0,0,0,-4.402061462402344,0,0.201080322265625,0,0.2186660766601562,0,0,0.2305679321289062,0,0.2261734008789062,0.2155075073242188,0,0,0.2423095703125,0,0.2408218383789062,0.2453155517578125,0.2433547973632812,0,0.2402114868164062,0,0,0.2394027709960938,0.2394485473632812,0,0.2618255615234375,0,0.238861083984375,0,0.2361679077148438,0,0,0.2389678955078125,0,0.2427749633789062,0.2404861450195312,0,0.2341537475585938,0.05403900146484375,0,0,0,0,0,-4.224739074707031,0,0,0.2168655395507812,0.2272567749023438,0,0.2263641357421875,0,0.2177505493164062,0.2451629638671875,0,0.2437286376953125,0,0.2486495971679688,0,0.250457763671875,0,0.2460174560546875,0,0.2418060302734375,0.2413864135742188,0.2402267456054688,0,0.2390365600585938,0,0.238983154296875,0,0,0.2391738891601562,0,0.23956298828125,0,0.2383041381835938,0,0.2308731079101562,0,0.079315185546875,0,0,0,0,0,-4.159194946289062,0,0.213165283203125,0,0.2237319946289062,0,0.2205734252929688,0,0.2259292602539062,0.2407302856445312,0.2372360229492188,0,0.2374267578125,0.2428054809570312,0,0.2397537231445312,0.2351226806640625,0,0.2354736328125,0,0.2342910766601562,0,0.234405517578125,0,0.2361984252929688,0,0.2366714477539062,0,0.2368927001953125,0,0.2371368408203125,0.2284698486328125,0,0.08716583251953125,0,0,0,0,0,-4.120002746582031,0,0.2074661254882812,0.21734619140625,0,0.2161865234375,0.2302932739257812,0,0.2630081176757812,0,0.2384490966796875,0,0.2465438842773438,0,0.2462997436523438,0.2433395385742188,0.2388153076171875,0.2377700805664062,0.2386322021484375,0,0.2382659912109375,0,0.2391510009765625,0,0.2394790649414062,0.2422027587890625,0,0.2366180419921875,0.2222518920898438,0,0,0,-4.172904968261719,0,0.1798248291015625,0.2141036987304688,0,0,0.2138824462890625,0.22119140625,0.239471435546875,0,0.240203857421875,0,0.2388076782226562,0.246429443359375,0,0.2481307983398438,0.2431564331054688,0,0.2393722534179688,0,0.2400283813476562,0,0.2409133911132812,0,0.239715576171875,0,0.2400588989257812,0,0.2651214599609375,0,0.2407684326171875,0,0.2326889038085938,0,0,0.06906890869140625,0,0,0,-3.9676513671875,0,0.2066879272460938,0.2081680297851562,0,0.2180633544921875,0,0.2392349243164062,0,0.2386093139648438,0,0,0.240203857421875,0.2442779541015625,0,0.246551513671875,0,0.2436065673828125,0.2410354614257812,0,0.2423553466796875,0,0.2435531616210938,0,0.2435455322265625,0,0.2442626953125,0,0.2446136474609375,0,0.2430572509765625,0,0,0.2350006103515625,0,0.06298828125,0,0,0,0,0,-3.8992919921875,0,0.2265243530273438,0,0.2067413330078125,0,0.229339599609375,0,0,0.2407302856445312,0,0.22637939453125,0,0.2397537231445312,0.2460174560546875,0.2470016479492188,0,0.2444381713867188,0,0.2415237426757812,0.2418060302734375,0.2424392700195312,0.240966796875,0,0.2414321899414062,0,0.2426681518554688,0.2348556518554688,0.2229766845703125,0,0,0,0,0,-3.984237670898438,0,0.1975784301757812,0,0.1927871704101562,0.1823654174804688,0,0.2265625,0,0,0.2369384765625,0.2395248413085938,0,0.23980712890625,0,0.2662200927734375,0,0,0.2494735717773438,0.2464675903320312,0.243316650390625,0,0.24310302734375,0.2417373657226562,0.241455078125,0,0.2421722412109375,0,0.2430343627929688,0,0.2333984375,0,0.1326446533203125,0,0,0,0,0,-3.84051513671875,0,0.1944198608398438,0,0.1960372924804688,0,0.2166900634765625,0,0,0.2351150512695312,0,0.2356643676757812,0,0.2345046997070312,0.2331771850585938,0,0.2331695556640625,0,0.2427139282226562,0,0,0.2373886108398438,0,0.2369613647460938,0.23699951171875,0,0.2378463745117188,0.23724365234375,0.2374114990234375,0,0.2361602783203125,0,0.2286758422851562,0.04279327392578125,0,0,0,0,0,-3.685195922851562,0,0.1876068115234375,0,0.1977920532226562,0.2235565185546875,0.230682373046875,0.2312774658203125,0,0.2318267822265625,0,0,0.2365951538085938,0.2426071166992188,0,0.2414932250976562,0,0.2374496459960938,0,0.2370376586914062,0,0.2370681762695312,0,0.23797607421875,0.2363204956054688,0,0.2381591796875,0,0.2223052978515625,0,0.1261672973632812,0,0,0,0,0,0,0,-3.710281372070312,0.187103271484375,0,0.1876068115234375,0.2162933349609375,0.253387451171875,0.2304000854492188,0,0.2313385009765625,0,0.2299880981445312,0,0.2396011352539062,0.2415542602539062,0,0.2370834350585938,0,0.23675537109375,0,0.2354660034179688,0,0,0.2385101318359375,0.2371902465820312,0,0.2377548217773438,0,0.2315216064453125,0.1476287841796875,0,0,0,-3.670921325683594,0.1863021850585938,0,0.1955337524414062,0.2208023071289062,0.2341461181640625,0,0.2344436645507812,0,0.2361984252929688,0,0,0.2400436401367188,0,0.243560791015625,0,0.2490463256835938,0.2412338256835938,0,0.23974609375,0.2393035888671875,0,0,0.241607666015625,0,0.2638092041015625,0.2396697998046875,0,0.2304916381835938,0.0421600341796875,0,0,0,-3.525604248046875,0,0.1848220825195312,0,0.2060089111328125,0,0.2182235717773438,0,0.2307662963867188,0,0.2316360473632812,0,0.237060546875,0,0.2387008666992188,0.2442092895507812,0,0.2482833862304688,0,0.2453155517578125,0,0.2441253662109375,0,0.2429962158203125,0,0.2422332763671875,0.2412033081054688,0,0.233978271484375,0,0.1414260864257812,0,0,0,0,0,-3.549217224121094,0.1838226318359375,0,0.193939208984375,0,0.233184814453125,0,0.223907470703125,0,0.227996826171875,0.2326278686523438,0,0.2339096069335938,0,0.2421646118164062,0,0,0.243560791015625,0,0.2395095825195312,0,0.2381744384765625,0,0.2361297607421875,0,0.2381210327148438,0,0.2367401123046875,0,0,0.2353363037109375,0,0.2138748168945312,0,0,0,0,0,-3.555488586425781,0.1880035400390625,0.1879348754882812,0.2071685791015625,0.2177810668945312,0,0.22882080078125,0,0.235076904296875,0.2375335693359375,0.239471435546875,0,0.24481201171875,0,0.2451019287109375,0.2411422729492188,0,0.2410659790039062,0,0.2419815063476562,0,0.26531982421875,0.236846923828125,0.199432373046875,0,0,0,0,0,-3.488899230957031,0.1840896606445312,0,0.1874313354492188,0,0.2039337158203125,0,0.2129592895507812,0.2248077392578125,0,0.2306060791015625,0,0.2328720092773438,0.2321014404296875,0,0.24163818359375,0,0.2432022094726562,0,0.2386322021484375,0,0.238525390625,0,0.23919677734375,0.2375869750976562,0,0.2321319580078125,0,0.2096481323242188,0,0,0,-3.444793701171875,0,0,0.1802520751953125,0.1803131103515625,0.21759033203125,0,0.2069244384765625,0,0.220733642578125,0,0.2272415161132812,0,0,0.2311019897460938,0,0,0.235015869140625,0.2377395629882812,0,0.2393264770507812,0,0,0.2358474731445312,0,0.2349319458007812,0.2357406616210938,0.236663818359375,0,0,0.2312774658203125,0,0.192840576171875,0,0,0,0,0,-3.375312805175781,0,0.18017578125,0,0.1661758422851562,0,0.1988677978515625,0,0.2070541381835938,0,0.220947265625,0.2293472290039062,0.2329635620117188,0,0.2346725463867188,0,0.2439117431640625,0,0.2443923950195312,0,0.2405624389648438,0,0.2368927001953125,0,0.262176513671875,0,0.238525390625,0.2293472290039062,0.106475830078125,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-3.34515380859375,0,0,0,0.09004974365234375,0,0.1643753051757812,0,0.178863525390625,0.1852951049804688,0,0.1994705200195312,0,0.2140655517578125,0,0.2312774658203125,0.2320480346679688,0.2197189331054688,0.2226028442382812,0,0.23291015625,0.23443603515625,0.2345809936523438,0,0.2340469360351562,0.235107421875,0.2329483032226562,0,0.09857177734375,0,0,0,0,0,-3.190628051757812,0.1787643432617188,0,0,0.1924972534179688,0,0,0.2032318115234375,0,0.2171859741210938,0.2250213623046875,0,0.2306900024414062,0.2289962768554688,0.235137939453125,0.2349853515625,0,0.2603836059570312,0,0.2374343872070312,0,0.2388687133789062,0,0.2374267578125,0.23699951171875,0,0.1270751953125,0,0,0,0,0,0,0,-3.1741943359375,0,0.1795196533203125,0,0.1838760375976562,0.1937637329101562,0,0.206512451171875,0,0.2204055786132812,0,0,0.2326889038085938,0,0,0.2322998046875,0.227630615234375,0,0,0.22955322265625,0,0.230224609375,0.2384033203125,0,0.2393646240234375,0,0.2405166625976562,0.241851806640625,0.1702117919921875,0,0,0,-3.148719787597656,0,0.1971969604492188,0,0.1842498779296875,0.1974334716796875,0,0,0.211151123046875,0.2241973876953125,0,0.2298736572265625,0,0.2314987182617188,0,0.2285842895507812,0,0.2352066040039062,0,0.23736572265625,0,0.23919677734375,0,0.238800048828125,0,0.2400894165039062,0,0.2391204833984375,0.1058197021484375,0,0,0,0,0,-3.057472229003906,0.1797561645507812,0.1847076416015625,0,0.1999282836914062,0,0.2108612060546875,0.2268905639648438,0,0.2330703735351562,0,0.2293777465820312,0.2284011840820312,0,0.2295684814453125,0,0.2384490966796875,0,0.2410812377929688,0.2407608032226562,0,0.2651519775390625,0,0.2390594482421875,0,0,0,0,0,-2.914299011230469,0,0,0.180084228515625,0.1934814453125,0.2060775756835938,0,0.2198257446289062,0,0.2307662963867188,0,0,0.23095703125,0.229522705078125,0.2312774658203125,0.2363128662109375,0,0.239410400390625,0.2400436401367188,0.2398223876953125,0,0.2400360107421875,0.0849456787109375,0,0,0,0,0,-2.934730529785156,0.180633544921875,0.18682861328125,0,0.2025527954101562,0,0.2147445678710938,0,0.2547607421875,0.2342758178710938,0,0.234619140625,0,0,0.23712158203125,0.23736572265625,0,0.2435989379882812,0,0.2416305541992188,0,0.2419357299804688,0,0.24249267578125,0.06885528564453125,0,0,0,-2.874519348144531,0,0.1798782348632812,0.1866531372070312,0,0.20233154296875,0,0,0.2154159545898438,0.2311477661132812,0.2323989868164062,0.230926513671875,0,0.2266464233398438,0.226959228515625,0.235595703125,0.2404251098632812,0,0.2411041259765625,0,0,0.240203857421875,0.0702056884765625,0,0,0,0,0,-2.809112548828125,0,0.1793441772460938,0,0,0.1877899169921875,0.201263427734375,0,0.2141952514648438,0.225341796875,0,0,0.2305450439453125,0,0.2295913696289062,0.2289886474609375,0,0.2284088134765625,0,0.235137939453125,0.2397003173828125,0,0.24029541015625,0,0.2391204833984375,0,0.013336181640625,0,0,0,0,0,-2.740570068359375,0,0.1783981323242188,0.1895751953125,0,0.2072296142578125,0,0.2229766845703125,0,0.2345046997070312,0.2349090576171875,0,0.2344207763671875,0.2334060668945312,0,0.237945556640625,0,0,0.2667694091796875,0.2414093017578125,0,0.2419815063476562,0,0.09966278076171875,0,0,0,0,0,-2.758857727050781,0,0.1792984008789062,0.18414306640625,0.2003707885742188,0,0.2140579223632812,0,0.2286224365234375,0,0.2339248657226562,0,0.232666015625,0,0.231292724609375,0,0.234283447265625,0,0.2414321899414062,0,0.2423171997070312,0,0.2425079345703125,0,0.1751708984375,0,0,0,0,0,-2.776420593261719,0.1689376831054688,0,0,0.181243896484375,0.1948471069335938,0.21173095703125,0.2490234375,0,0.2347640991210938,0.233734130859375,0,0.2325973510742188,0.2405548095703125,0.2405776977539062,0.241912841796875,0,0.2415313720703125,0.1849441528320312,0,0,0,-2.737190246582031,0,0,0.1641769409179688,0.1804351806640625,0,0.196075439453125,0.2110748291015625,0,0.2288131713867188,0,0,0.23797607421875,0.23602294921875,0.235076904296875,0,0.2399215698242188,0,0.2424468994140625,0,0.2451400756835938,0,0.2449798583984375,0,0.1537246704101562,0,0,0,0,0,-2.673927307128906,0,0.1848220825195312,0.18194580078125,0,0.1984176635742188,0,0.2129135131835938,0,0.2263031005859375,0,0.2321701049804688,0,0.232269287109375,0.2308120727539062,0,0.2356491088867188,0,0.23675537109375,0,0.2380828857421875,0.2386474609375,0.102508544921875,0,0,0,0,0,-2.604377746582031,0,0,0.1740036010742188,0.181732177734375,0,0.2000961303710938,0.2349090576171875,0.2287521362304688,0.2334365844726562,0,0.2319412231445312,0,0.2302093505859375,0,0.2341232299804688,0,0.2312545776367188,0,0.2330856323242188,0.2312774658203125,0.03574371337890625,0,0,0,0,0,-2.496963500976562,0,0.17779541015625,0,0.1833038330078125,0,0.1995849609375,0.21685791015625,0,0.2305831909179688,0,0.231597900390625,0,0.23162841796875,0,0.2277069091796875,0.17608642578125,0,0.227203369140625,0,0.2305755615234375,0,0.2343368530273438,0.00455474853515625,0,0,0,-2.44891357421875,0,0.1761856079101562,0,0.2023391723632812,0,0.2009506225585938,0.2166595458984375,0,0.229583740234375,0.2300033569335938,0,0,0.22845458984375,0,0.2275924682617188,0,0.2334365844726562,0.2163238525390625,0,0.2284393310546875,0,0.1326828002929688,0,0,0,0,0,-2.488685607910156,0,0.1725692749023438,0.1808395385742188,0.1930465698242188,0,0.2112655639648438,0,0.2256698608398438,0,0,0.2337875366210938,0.2557907104492188,0,0,0.2297439575195312,0.232513427734375,0.2303390502929688,0,0.2311553955078125,0,0.1645278930664062,0,0,0,-2.491355895996094,0.174896240234375,0,0.1991424560546875,0,0.196533203125,0.2093429565429688,0,0.2253494262695312,0,0.2347869873046875,0,0,0.2337112426757812,0,0.23126220703125,0,0.2335968017578125,0,0.2430191040039062,0,0,0.243255615234375,0.137725830078125,0,0,0,0,0,-2.402503967285156,0.1763992309570312,0,0.1848831176757812,0.2013397216796875,0,0.2184524536132812,0.2332992553710938,0.235992431640625,0.23443603515625,0.2377700805664062,0.2417755126953125,0,0.2423171997070312,0,0,0.2426605224609375,0.02341461181640625,0,0,0,-2.28741455078125,0.1803817749023438,0.1912002563476562,0,0.2081146240234375,0,0.2262191772460938,0,0.2345809936523438,0,0.235382080078125,0.236297607421875,0,0.2389984130859375,0,0.2385406494140625,0,0.2665176391601562,0,0.1002349853515625,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2.353958129882812,0,0.140228271484375,0,0,0.1656341552734375,0,0.1804580688476562,0.1924209594726562,0,0.2100753784179688,0,0.2489700317382812,0,0.2374191284179688,0,0.23602294921875,0,0,0.2354660034179688,0,0.2325210571289062,0,0.2404098510742188,0,0,0.1021728515625,0,0,0,-2.274192810058594,0,0,0.17706298828125,0,0.1826705932617188,0,0.2030029296875,0,0.2207565307617188,0,0.2335586547851562,0,0,0.2370681762695312,0,0,0.2347869873046875,0,0.2425613403320312,0.24249267578125,0,0.2439727783203125,0.1231307983398438,0,0,0,-2.248054504394531,0,0.1786727905273438,0,0.1857986450195312,0,0,0.2237319946289062,0,0.2228469848632812,0,0.2362442016601562,0.2380523681640625,0,0.2367782592773438,0,0.2424468994140625,0,0.245880126953125,0,0,0.2467498779296875,0,0.05666351318359375,0,0,0,0,0,-2.166107177734375,0,0.1800918579101562,0.1875839233398438,0,0.2064666748046875,0,0.2221755981445312,0,0.237396240234375,0,0.2372665405273438,0,0.2360305786132812,0,0.238433837890625,0,0.2418212890625,0,0.2435684204101562,0,0,0,0,0,0,0,0,-2.087890625,0,0.2001113891601562,0.19244384765625,0,0.2111053466796875,0,0,0.2293853759765625,0,0.236480712890625,0.2353515625,0,0.234222412109375,0,0.2414932250976562,0,0.2426605224609375,0,0.1283111572265625,0,0,0,0,0,-2.14886474609375,0,0.1761398315429688,0,0,0.183868408203125,0,0.1995925903320312,0.2171783447265625,0,0.2320022583007812,0,0.2368698120117188,0,0.2344589233398438,0,0.2349395751953125,0,0.2401657104492188,0.2420883178710938,0,0.01422119140625,0,0,0,-2.032333374023438,0,0.1970977783203125,0,0.1894149780273438,0.2083358764648438,0,0.2271881103515625,0.23455810546875,0.2349700927734375,0.2346038818359375,0.2378768920898438,0.2436065673828125,0,0.086334228515625,0,0,0,0,0,-2.049942016601562,0,0.1760025024414062,0,0.1815643310546875,0.1982345581054688,0,0.2153091430664062,0.2308731079101562,0,0.23687744140625,0.2323455810546875,0,0.2543182373046875,0.2422637939453125,0.142852783203125,0,0,0,0,0,-2.064613342285156,0,0.17572021484375,0.1831893920898438,0,0.1947555541992188,0,0.2165374755859375,0,0.22705078125,0,0,0.2374267578125,0,0.2591476440429688,0,0.2351608276367188,0,0.23388671875,0.1613388061523438,0,0,0,-2.045997619628906,0,0,0.1713180541992188,0.1817169189453125,0,0.190216064453125,0,0.2318038940429688,0.2283706665039062,0.2391357421875,0,0.2379074096679688,0,0.2355117797851562,0,0.240203857421875,0,0.1486282348632812,0,0,0,0,0,-2.006988525390625,0.18896484375,0,0.182098388671875,0.1916885375976562,0.214080810546875,0.2296524047851562,0,0.235992431640625,0,0.2348480224609375,0,0.2330398559570312,0.2398757934570312,0.1144866943359375,0,0,0,-1.9339599609375,0,0.1747512817382812,0.1809844970703125,0.1994476318359375,0,0.21710205078125,0,0,0.2284317016601562,0,0.235382080078125,0.2328643798828125,0.25531005859375,0.23583984375,0,0.03069305419921875,0,0,0,0,0,-1.866233825683594,0,0.1795120239257812,0,0.157012939453125,0,0,0.21282958984375,0.2146072387695312,0,0.2293777465820312,0,0,0.2337417602539062,0,0.2337112426757812,0,0.2313079833984375,0,0.2277450561523438,0,0.00238800048828125,0,0,0,-1.784828186035156,0,0.1779327392578125,0,0.189849853515625,0,0.2078018188476562,0,0.2242431640625,0,0,0.2331390380859375,0.233642578125,0,0.2315444946289062,0.23297119140625,0.1087417602539062,0,0,0,0,0,-1.836090087890625,0,0.1749649047851562,0,0.1837081909179688,0,0.2012252807617188,0.217132568359375,0,0,0.2291488647460938,0.23394775390625,0,0.2317962646484375,0,0.2531814575195312,0.1651382446289062,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.863082885742188,0,0,0.056488037109375,0.1661758422851562,0,0.1788101196289062,0,0.19232177734375,0.2107009887695312,0.2227249145507812,0,0.2381439208984375,0,0.2342605590820312,0,0.2237091064453125,0,0.1928482055664062,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.832893371582031,0,0,0,0.1612930297851562,0,0,0.19671630859375,0,0.2073898315429688,0,0.225311279296875,0,0.237457275390625,0,0.2310714721679688,0,0,0.2236099243164062,0.2098617553710938,0.2433395385742188,0,0.2230682373046875,0,0.2323150634765625,0,0.2330398559570312,0,0.2326583862304688,0,0.233001708984375,0,0.1970748901367188,0,0.1951370239257812,0,0.1942977905273438,0.1945724487304688,0,0,0.1945648193359375,0,0.2135772705078125,0,0.19342041015625,0.1931533813476562,0,0.1942291259765625,0.1935653686523438,0,0.1942672729492188,0,0.1907806396484375,0.1910247802734375,0,0.1915130615234375,0.1917724609375,0,0.2133331298828125,0,0.1940765380859375,0.1937637329101562,0,0,0.1958389282226562,0,0.1961669921875,0,0.1881027221679688,0,0,0.19549560546875,0,0.19586181640625,0.06299591064453125,0,0,0,0,0,-7.177780151367188,0,0.1946258544921875,0,0,0.2026519775390625,0,0.2179641723632812,0,0.233184814453125,0,0.2311630249023438,0,0.2184066772460938,0,0.2188873291015625,0.2377700805664062,0,0.2552490234375,0,0.233245849609375,0,0.2333450317382812,0.2318191528320312,0,0.2300872802734375,0,0.2311172485351562,0,0.2303695678710938,0,0,0.2321853637695312,0.2274169921875,0,0.2294769287109375,0,0.230926513671875,0,0.2314453125,0,0.2311248779296875,0,0,0.2302093505859375,0,0.2313079833984375,0,0.2291793823242188,0,0.232269287109375,0.234649658203125,0,0.2339096069335938,0,0.2348175048828125,0.2326507568359375,0,0.2304306030273438,0.2212753295898438,0.2210311889648438,0,0.072845458984375,0,0,0,0,0,0,0,0,-7.057579040527344,0,0,0.1934051513671875,0.2008514404296875,0,0.2133941650390625,0,0.225830078125,0,0.225128173828125,0,0.2146759033203125,0,0.2352828979492188,0,0.238800048828125,0,0.2337875366210938,0,0.233734130859375,0,0.2345123291015625,0.2334136962890625,0.2326278686523438,0.2362594604492188,0,0.2351226806640625,0,0.2344512939453125,0,0.2349700927734375,0,0.2337112426757812,0.232177734375,0,0.23236083984375,0,0.2315902709960938,0,0.233673095703125,0.2332763671875,0,0,0.2420806884765625,0.2432861328125,0,0.2391510009765625,0.2404708862304688,0.242462158203125,0,0.2419815063476562,0,0,0.2307281494140625,0,0.253387451171875,0.07680511474609375,0,0,0,0,0,-6.967857360839844,0,0.1900177001953125,0.1977615356445312,0.2076339721679688,0,0.2205429077148438,0,0.2225112915039062,0,0,0.2186203002929688,0,0.2416305541992188,0,0.239898681640625,0,0.23553466796875,0.234893798828125,0,0.2348251342773438,0,0.233734130859375,0,0.2354507446289062,0,0.232879638671875,0,0,0.2337417602539062,0,0.2316131591796875,0,0.2316818237304688,0,0.2298736572265625,0.2523117065429688,0,0.231231689453125,0,0.2332763671875,0,0.2308731079101562,0,0.2314529418945312,0,0.2298583984375,0.2272415161132812,0,0.228179931640625,0,0.2310409545898438,0,0.2317047119140625,0.2305145263671875,0,0.24444580078125,0,0,0.2235336303710938,0,0.0718231201171875,0,0,0,0,0,0,0,0,-6.862213134765625,0,0.1891555786132812,0,0.1988143920898438,0,0.2277679443359375,0,0.2130584716796875,0,0.20947265625,0.2309494018554688,0,0.239349365234375,0,0,0.2363433837890625,0.23199462890625,0,0.2318115234375,0,0.2314987182617188,0,0.2308120727539062,0.2536239624023438,0,0.2330169677734375,0.2330322265625,0,0.219207763671875,0,0.23211669921875,0.230926513671875,0.2267837524414062,0.2255935668945312,0,0.226776123046875,0,0.226318359375,0,0.22705078125,0,0.2269287109375,0,0,0.2286300659179688,0,0.2284011840820312,0.2302703857421875,0.2300872802734375,0,0.2279739379882812,0.2284011840820312,0,0.2226943969726562,0,0.0326385498046875,0,0,0,0,0,0,0,0,-6.71099853515625,0,0.1928329467773438,0.1980056762695312,0.2073440551757812,0,0.2064132690429688,0,0.2098388671875,0,0,0.2372512817382812,0,0,0.2365798950195312,0,0.2354812622070312,0,0.2310714721679688,0,0,0.2321548461914062,0,0,0.2335662841796875,0,0.2335433959960938,0,0,0.2342376708984375,0,0.2377853393554688,0,0.2328414916992188,0,0.2420425415039062,0,0.2340469360351562,0,0.2330093383789062,0,0.23443603515625,0.2355575561523438,0,0.2352447509765625,0,0.23162841796875,0.2360763549804688,0,0.23052978515625,0,0.2532272338867188,0,0,0.2313156127929688,0.2308731079101562,0,0.2302093505859375,0.2299118041992188,0,0.23236083984375,0,0.02754974365234375,0,0,0,0,0,-6.620620727539062,0,0.1905517578125,0,0.1983261108398438,0,0,0.1973876953125,0,0.2006072998046875,0,0.2140960693359375,0.23602294921875,0.2374114990234375,0.2373504638671875,0.230926513671875,0.2299346923828125,0,0.22900390625,0.2299957275390625,0,0.2311630249023438,0.229339599609375,0,0.2311019897460938,0.2528610229492188,0.2292938232421875,0,0.2316665649414062,0,0.2308273315429688,0.2320480346679688,0,0.2339019775390625,0,0.23358154296875,0,0.2335891723632812,0.2329864501953125,0,0.2340774536132812,0,0.2333908081054688,0,0.2361984252929688,0,0,0.2330703735351562,0,0.2282257080078125,0.2146072387695312,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-6.636253356933594,0,0,0,0,0,0.01165008544921875,0.180511474609375,0,0.1924972534179688,0,0.1949920654296875,0,0.1981277465820312,0.2048873901367188,0.235137939453125,0.2367172241210938,0,0.2243499755859375,0.2276763916015625,0,0.2201385498046875,0.2305221557617188,0,0.2363967895507812,0,0.23455810546875,0,0.237701416015625,0.2378387451171875,0,0.2363510131835938,0.2344589233398438,0,0,0.236236572265625,0,0.238128662109375,0.2351303100585938,0.2381210327148438,0.2398300170898438,0,0,0.2649612426757812,0,0.2374038696289062,0,0.240814208984375,0,0.238616943359375,0,0.2391433715820312,0.2388229370117188,0,0.2350311279296875,0.1691055297851562,0,0,0,0,0,0,0,0,-6.502166748046875,0,0.1847305297851562,0.1936264038085938,0,0.192291259765625,0.1947784423828125,0,0.2193756103515625,0,0.2349472045898438,0,0.2365493774414062,0,0,0.2354660034179688,0.23443603515625,0,0.232574462890625,0.2328109741210938,0,0.2321701049804688,0,0.2328872680664062,0.22857666015625,0,0.23187255859375,0.257354736328125,0,0.2307510375976562,0,0.23162841796875,0.2333831787109375,0.2315216064453125,0,0.2380523681640625,0.2353439331054688,0,0.2425079345703125,0,0.24127197265625,0,0,0.2414474487304688,0,0.2409820556640625,0.2401580810546875,0,0.2347869873046875,0,0.2409896850585938,0,0.03159332275390625,0,0,0,0,0,-6.322509765625,0,0.1878204345703125,0.1922988891601562,0,0.18829345703125,0,0.2054214477539062,0,0.224609375,0.233978271484375,0.2312774658203125,0.2291641235351562,0,0.2505722045898438,0,0.2282943725585938,0,0.22772216796875,0,0.2319717407226562,0,0.2360382080078125,0,0,0.2386245727539062,0,0.2377700805664062,0,0.2379837036132812,0,7.830184936523438,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7.62939453125,7.62939453125e-06,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,15.2587890625,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7.629417419433594,0,0,0,0,0,0,0,0.1268081665039062,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,15.26838684082031,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"filename":["<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,null,null,null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,null,null,null,null,"<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,null,null,"<expr>","<expr>",null,null,null,"<expr>",null,null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>","<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,null,null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,null,null,null,null,"<expr>","<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,null,null,null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,null,null,null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,null,null,null,null,null,null,null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,null,null,null,null,null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,null,null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,null,null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,null,null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,"<expr>","<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null]},"interval":10,"files":[{"filename":"<expr>","content":"## Generate Large Random Dataset\nn <- 2e6\nx <- runif(n)\ny <- runif(n)\nz <- runif(n)\nXYZ <- cbind(x,y,z)\n\n## Inspect 4 equivalent `row mean` calculations \nprofvis::profvis({\n    m <- rowSums(XYZ)/ncol(XYZ)\n    m <- rowMeans(XYZ)\n    m <- apply(XYZ, 1, mean)\n    m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }\n})\n## rowSums(), colSums(), rowMeans(), and colMeans() are vectorised and fast.\n## for loop is not the slowest, but the ugliest.","normpath":"<expr>"}],"prof_output":"/tmp/RtmpOMjaFU/file16c775b145fa.prof","highlight":{"output":["^output\\$"],"gc":["^<GC>$"],"stacktrace":["^\\.\\.stacktraceo(n|ff)\\.\\.$"]},"split":"h"}},"evals":[],"jsHooks":[]}</script>
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
## 1 mean1(x, 0.5)   34.1ms   37.1ms      27.2    7.63MB     0   
## 2 mean2(x, 0.5)   32.6ms   35.7ms      28.6    7.63MB     2.20
## 3 mean3(x, 0.5)     37ms   37.1ms      26.8    7.63MB     0
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
##   0.117   0.000   0.039
```

```r
system.time({ lm(Y~X, data=DAT) })
```

```
##    user  system elapsed 
##   0.497   0.000   0.177
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
## 1 ma1(y)      279.7ms  279.7ms      3.58    15.3MB     3.58
## 2 ma2(y)       26.9ms   27.6ms     36.3     91.6MB   254.
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
##   1.316   0.299   0.909
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





