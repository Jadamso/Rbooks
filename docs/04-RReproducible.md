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
<div class="plotly html-widget html-fill-item-overflow-hidden html-fill-item" id="htmlwidget-8aefd2c098e70fc4b0cf" style="width:672px;height:480px;"></div>
<script type="application/json" data-for="htmlwidget-8aefd2c098e70fc4b0cf">{"x":{"visdat":{"20f5447736df":["function () ","plotlyVisDat"]},"cur_data":"20f5447736df","attrs":{"20f5447736df":{"x":{},"y":{},"alpha_stroke":1,"sizes":[10,100],"spans":[1,20]}},"layout":{"margin":{"b":40,"l":60,"t":25,"r":10},"xaxis":{"domain":[0,1],"automargin":true,"title":"X"},"yaxis":{"domain":[0,1],"automargin":true,"title":"Y"},"hovermode":"closest","showlegend":false},"source":"A","config":{"modeBarButtonsToAdd":["hoverclosest","hovercompare"],"showSendToCloud":false},"data":[{"x":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100],"y":[1.6262429616436838,9.2627506838236986,11.75167172751102,17.618248205179725,18.801819134442805,19.602871471418659,28.876589780960316,32.767638544707317,35.668104251643676,35.132331747623503,45.668821697022935,47.332411702699225,55.308558266019446,56.194433364604976,62.126140864248924,60.937068350867087,66.875020607557857,71.484637988749185,75.256906785810315,83.268045660133481,86.210290329479122,90.673153134743927,93.290540101876374,95.457415985676406,100.19650911297279,103.65432453406795,107.54651829033,109.76900194027013,116.12459401964199,122.53840885357319,120.53410359356013,128.6271761327308,129.3280002872273,134.09405692273313,142.43679506225018,136.20375426019746,149.76522906483899,150.15260620352265,157.66135742139878,162.43398896100513,164.62439438313166,167.54885283293632,173.30747922314319,173.95029549959247,181.50973890266391,185.50620852848203,186.17907455842996,191.4028383471769,195.3691643559365,195.24186671683844,207.92361871719939,209.61724067637519,211.83118774337225,216.73668655984591,220.39999401072009,223.63743469001719,227.02338287365313,232.26731542748695,236.76547811110254,240.37910776163935,244.15888115616866,245.6735688895269,251.04002791962188,254.96287987046347,262.69645593115507,263.90005515664444,267.83353115438024,274.12816268271672,276.91559155984874,281.63753716905973,280.19769884532957,287.1194393799824,292.31429256114961,294.80497763126385,301.07061762826339,306.7601432484372,306.81264662626512,311.84213030121253,317.66862490253902,321.9433315199438,322.33767118895247,328.38739333426076,331.92874809915656,331.51510345630419,342.75329883416907,342.28503058848423,349.02852495957495,350.39621186358062,354.42538322990555,361.86512272135053,364.85169371335621,369.23375430813729,370.33935283099026,378.47536632411584,382.72114433529686,381.60934843862185,390.35962979023014,394.75610027456128,394.54862400932547,398.82224802174818],"type":"scatter","mode":"markers","marker":{"color":"rgba(31,119,180,1)","line":{"color":"rgba(31,119,180,1)"}},"error_y":{"color":"rgba(31,119,180,1)"},"error_x":{"color":"rgba(31,119,180,1)"},"line":{"color":"rgba(31,119,180,1)"},"xaxis":"x","yaxis":"y","frame":null}],"highlight":{"on":"plotly_click","persistent":false,"dynamic":false,"selectize":false,"opacityDim":0.20000000000000001,"selected":{"opacity":1},"debounce":0},"shinyEvents":["plotly_hover","plotly_click","plotly_selected","plotly_relayout","plotly_brushed","plotly_brushing","plotly_clickannotation","plotly_doubleclick","plotly_deselect","plotly_afterplot","plotly_sunburstclick"],"base_url":"https://plot.ly"},"evals":[],"jsHooks":[]}</script>
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
## Ncells 1209802 64.7    2358830  126  2358830 126.0
## Vcells 2294644 17.6    8388608   64  3577172  27.3
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
<div class="profvis html-widget html-fill-item-overflow-hidden html-fill-item" id="htmlwidget-87abd646f6dac0a762ff" style="width:100%;height:600px;"></div>
<script type="application/json" data-for="htmlwidget-87abd646f6dac0a762ff">{"x":{"message":{"prof":{"time":[1,2,3,4,5,6,7,8,9,10,11,12,13,13,13,14,14,15,15,16,16,17,17,18,18,19,19,20,20,21,21,22,22,23,23,24,24,25,25,26,26,27,27,28,28,29,29,30,30,31,31,32,32,33,33,34,34,35,35,36,37,38,39,39,40,40,41,41,41,42,43,43,44,44,45,45,46,46,47,48,49,50,51,51,52,52,53,53,54,54,55,55,56,57,58,58,58,59,59,60,60,61,61,62,62,62,63,64,65,65,66,67,68,69,70,71,71,72,72,73,73,73,74,75,76,76,77,77,78,79,79,80,80,81,81,82,82,82,83,84,84,85,85,86,86,87,88,88,88,89,89,90,90,91,91,92,93,93,94,94,95,95,96,96,97,98,98,99,99,100,100,101,101,102,102,102,103,103,104,105,106,106,107,108,108,109,109,109,110,110,111,112,112,113,113,114,114,115,115,116,116,116,117,117,118,118,119,120,121,121,122,122,123,123,124,125,125,126,126,127,127,128,128,129,129,130,130,130,131,131,132,132,133,133,134,135,135,136,136,137,137,138,138,139,139,140,140,141,141,142,142,143,143,143,144,144,144,145,146,146,147,147,148,148,149,149,150,150,151,151,152,152,153,153,154,155,155,156,156,157,157,157,158,158,159,159,160,160,161,161,161,162,163,164,164,165,165,166,166,167,167,168,168,169,169,170,171,171,171,172,172,173,173,174,175,175,176,176,177,177,178,178,179,179,180,181,181,182,183,183,184,184,184,185,186,186,186,187,188,188,189,189,189,190,191,191,192,192,193,193,194,195,196,196,197,197,197,198,198,199,199,200,200,201,202,202,203,204,204,205,206,206,207,207,208,209,209,209,210,210,210,211,212,212,213,213,214,215,215,216,216,217,218,218,219,219,220,220,220,221,221,222,222,222,223,223,223,224,224,225,225,226,226,227,228,228,229,230,230,231,231,232,233,233,234,234,235,235,236,236,237,237,238,238,239,239,239,240,240,241,241,242,242,243,244,244,245,245,246,246,247,247,248,248,249,249,250,250,251,251,252,252,253,253,254,255,255,256,256,257,258,258,259,259,259,259,260,260,260,260,261,261,262,262,263,264,264,265,265,266,266,267,267,267,268,268,268,269,270,270,271,271,271,272,272,272,273,274,275,275,276,276,277,277,277,278,278,279,279,280,280,281,281,282,282,283,283,283,284,284,284,285,285,286,287,288,288,289,289,290,290,291,291,292,292,293,293,294,295,295,296,297,297,297,298,299,300,300,301,302,302,302,303,304,305,306,306,307,307,308,308,309,309,310,310,311,311,312,312,313,313,314,314,315,315,316,316,317,317,318,318,318,319,320,320,321,322,323,324,324,325,326,326,327,328,328,329,329,329,330,330,331,331,332,333,333,334,334,335,335,336,337,338,338,338,339,339,340,340,340,341,341,342,343,344,344,345,346,346,347,347,348,349,349,350,350,351,351,351,352,352,352,353,353,354,355,356,357,357,358,358,359,360,360,360,361,362,362,362,363,363,363,364,364,365,366,366,367,367,367,368,369,369,370,371,371,372,373,373,373,374,374,375,375,376,376,376,377,377,378,379,379,380,380,381,381,382,383,384,385,385,386,386,387,387,388,389,389,390,391,391,392,392,393,393,394,394,395,395,396,396,397,397,398,398,399,399,400,400,401,401,401,402,402,403,404,404,405,406,406,407,407,408,408,409,409,410,410,411,411,412,412,412,413,414,414,414,415,416,416,416,417,417,417,418,418,419,419,420,421,421,422,423,423,424,424,424,425,426,426,427,427,427,428,428,428,429,429,430,430,431,431,432,433,433,434,434,435,436,437,437,438,439,439,440,441,442,442,443,443,444,445,445,446,447,447,447,448,448,449,449,449,450,450,451,451,452,452,452,453,454,455,456,457,457,457,458,459,460,460,461,462,463,463,464,464,465,465,466,466,467,467,467,467,468,469,469,470,470,471,471,472,472,472,473,473,474,474,475,476,476,477,477,478,478,479,479,480,480,481,481,482,482,483,483,484,484,484,485,486,486,486,487,487,488,488,489,489,490,490,490,491,491,492,492,492,493,493,494,494,495,495,495,496,496,496,497,497,498,498,499,499,500,500,501,501,502,502,503,503,504,504,505,505,506,506,507,507,508,508,509,509,510,511,511,512,512,513,513,513,514,514,515,515,516,516,517,517,518,519,520,520,520,521,521,522,523,523,524,524,525,526,526,527,528,528,528,529,529,530,530,531,531,532,532,533,533,534,534,535,535,536,536,537,537,538,538,539,539,540,540,541,541,542,542,543,543,544,544,545,545,546,546,547,547,548,548,549,549,550,550,551,551,552,552,553,553,554,554,555,555,556,556,557,557,558,558,559,559,560,560,561,561,562,562,563,563,564,564,564,565,565,566,567,568,569,569,570,570,571,571,572,573,574,575,575,576,576,577,577,577,578,579,580,580,581,582,583,583,584,584,584,585,585,586,586,586,587,587,587,588,588,589,590,590,591,592,592,593,594,595,596,597,598,598,599,600,601,601,602,603,604,605,605,606,607,607,607,608,608,608,609,609,610,610,611,611,612,613,614,614,615,616,616,617,618,619,619,620,620,621,621,622,622,623,624,624,624,625,625,626,626,627,627,628,628,629,629,629,630,630,630,631,632,632,633,633,634,634,635,635,636,637,637,638,638,639,639,640,640,640,641,641,642,642,643,644,644,644,645,646,647,648,648,649,649,650,650,650,651,651,651,652,653,653,654,655,655,656,656,656,657,658,659,659,660,660,661,662,662,663,663,664,665,665,666,667,668,669,669,670,670,671,671,672,672,673,673,674,675,675,675,676,676,677,678,679,679,680,681,681,682,683,683,684,684,685,685,686,686,687,688,688,689,689,690,690,691,691,692,692,692,693,693,693,694,695,695,696,697,698,698,699,699,699,700,700,700,701,701,702,702,703,703,704,705,705,706,706,707,707,708,708,709,709,710,710,711,711,711,712,712,713,713,714,714,715,715,716,716,717,717,718,718,719,720,721,721,722,722,723,723,724,724,725,725,726,727,728,728,729,729,730,731,731,732,732,732,733,733,733,734,734,735,735,736,737,737,738,739,739,739,740,740,741,741,741,742,742,742,743,744,744,745,746,746,746,747,747,748,748,749,749,749,750,751,752,752,752,753,753,753,754,754,755,755,756,756,757,757,758,759,759,760,760,761,761,762,762,763,763,764,765,765,766,766,767,767,768,768,769,770,771,772,772,772,773,773,773,774,774,775,775,775,776,777,777,778,778,779,780,781,782,782,783,783,784,784,785,785,786,787,787,788,788,789,790,790,791,791,792,792,793,793,794,795,795,796,796,797,797,798,798,799,799,800,801,801,802,802,803,804,804,805,806,806,806,807,808,808,809,810,810,811,811,812,812,813,813,814,814,815,815,815,816,817,818,819,819,820,821,822,822,823,824,824,824,825,826,826,827,827,828,828,829,830,830,830,831,831,831,832,832,833,834,834,835,835,836,836,837,837,838,838,839,839,840,841,841,842,842,843,843,843,844,844,845,845,845,846,846,847,847,847,848,848,849,849,850,850,851,851,852,852,853,853,854,854,854,855,855,856,856,857,858,859,860,861,862,863,863,864,864,865,865,866,867,867,868,868,869,869,870,871,871,872,872,873,873,874,874,874,875,876,877,877,878,879,879,880,880,881,881,882,882,883,883,884,884,885,885,886,886,886,887,887,887,888,889,889,890,891,891,891,892,892,893,893,894,894,895,895,896,896,897,897,898,898,899,899,900,900,901,901,902,902,903,904,904,905,905,906,906,907,908,908,909,909,910,910,911,912,912,913,913,914,914,914,915,916,916,917,917,918,918,918,919,920,920,921,922,922,923,923,923,924,924,924,925,925,926,926,927,928,928,929,929,930,930,931,931,932,933,933,934,935,935,936,937,937,938,938,939,939,940,940,941,941,941,942,942,942,943,944,945,945,946,946,947,948,949,949,949,950,951,951,952,952,953,954,954,955,955,956,956,956,957,957,958,958,959,959,959,960,960,960,961,962,962,963,963,964,965,965,966,966,967,967,968,969,969,970,970,971,971,972,972,973,974,975,976,977,977,977,978,978,978,979,979,979,980,980,980,981,981,981,982,982,982,983,983,983,984,984,984,985,985,985,986,986,986,987,987,987,988,988,988,989,989,989,990,990,990,991,991,991,992,992,992,993,993,993,994,994,995,996,996,997,998,998,999,999,1000,1001,1001,1002,1002,1003,1003,1003,1004,1004,1005,1005,1006,1006,1007,1007,1008,1008,1009,1009,1010,1010,1010,1011,1011,1011,1012,1012,1013,1013,1014,1014,1015,1015,1016,1017,1017,1018,1019,1019,1019,1020,1020,1021,1022,1022,1023,1024,1024,1025,1025,1026,1026,1027,1027,1027,1028,1028,1028,1028,1029,1029,1029,1029,1030,1030,1031,1032,1033,1033,1033,1034,1034,1035,1035,1036,1036,1037,1037,1038,1038,1039,1039,1040,1040,1041,1041,1042,1042,1042,1043,1044,1044,1045,1045,1045,1046,1046,1046,1047,1047,1048,1048,1049,1049,1049,1050,1050,1051,1052,1052,1053,1054,1054,1055,1056,1056,1057,1057,1058,1059,1059,1060,1060,1061,1061,1061,1062,1062,1062,1063,1063,1063,1064,1065,1065,1066,1066,1067,1067,1068,1068,1069,1070,1070,1070,1071,1072,1072,1073,1074,1075,1075,1076,1076,1077,1078,1078,1078,1079,1079,1079,1080,1080,1081,1081,1081,1082,1082,1083,1083,1084,1084,1085,1085,1086,1086,1087,1088,1088,1089,1089,1090,1090,1091,1091,1092,1093,1093,1094,1094,1094,1095,1095,1095,1096,1096,1096,1097,1097,1097,1098,1098,1099,1099,1100,1100,1101,1102,1102,1103,1103,1104,1104,1104,1105,1105,1106,1107,1108,1108,1109,1110,1110,1110,1111,1111,1111,1112,1112,1112,1113,1113,1114,1114,1115,1115,1116,1116,1117,1118,1118,1119,1119,1120,1120,1121,1121,1122,1122,1123,1124,1124,1125,1126,1126,1126,1127,1127,1127,1128,1129,1130,1130,1131,1132,1132,1133,1133,1134,1134,1135,1135,1136,1136,1137,1137,1137,1138,1138,1139,1139,1140,1140,1141,1141,1142,1142,1142,1142,1143,1143,1143,1143,1144,1145,1145,1146,1146,1147,1147,1148,1148,1149,1150,1151,1151,1152,1152,1153,1154,1155,1156,1156,1157,1157,1158,1158,1159,1159,1160,1160,1161,1162,1162,1163,1163,1164,1164,1165,1165,1166,1166,1167,1168,1168,1169,1169,1170,1170,1171,1171,1172,1172,1173,1173,1174,1174,1175,1176,1176,1177,1178,1179,1180,1180,1181,1181,1182,1183,1183,1184,1184,1185,1186,1186,1187,1187,1188,1188,1188,1189,1189,1189,1190,1190,1191,1191,1192,1192,1193,1194,1194,1195,1195,1196,1196,1197,1198,1198,1199,1200,1200,1201,1201,1202,1202,1203,1203,1204,1204,1205,1205,1206,1206,1207,1208,1208,1209,1210,1211,1211,1212,1213,1213,1214,1215,1216,1216,1217,1217,1217,1218,1218,1218,1219,1220,1220,1221,1221,1222,1222,1223,1224,1224,1225,1225,1225,1226,1226,1227,1227,1228,1228,1229,1229,1230,1230,1231,1231,1232,1232,1232,1233,1233,1233,1234,1235,1235,1236,1236,1237,1238,1238,1239,1240,1240,1241,1241,1242,1242,1243,1243,1244,1244,1245,1245,1246,1246,1246,1247,1247,1247,1248,1249,1249,1250,1251,1251,1252,1253,1253,1254,1254,1255,1255,1256,1256,1256,1257,1258,1258,1259,1259,1260,1260,1260,1261,1261,1261,1262,1262,1262,1263,1263,1264,1264,1265,1265,1266,1266,1267,1267,1268,1268,1269,1269,1270,1271,1271,1272,1272,1273,1273,1274,1274,1275,1275,1276,1276,1277,1278,1278,1279,1279,1280,1280,1281,1282,1282,1282,1283,1283,1284,1284,1285,1286,1286,1287,1287,1288,1288,1289,1289,1290,1290,1291,1291,1292,1292,1292,1293,1293,1294,1295,1295,1296,1297,1298,1299,1299,1300,1300,1301,1301,1302,1302,1303,1303,1304,1304,1305,1305,1306,1306,1307,1307,1308,1308,1309,1309,1310,1311,1312,1312,1313,1313,1314,1314,1315,1315,1315,1316,1316,1316,1317,1317,1317,1318,1318,1318,1319,1319,1319,1320,1320,1320,1321,1321,1321,1322,1322,1322,1323,1323,1323,1324,1324,1324,1325,1325,1325,1326,1326,1326,1327,1328,1328,1329,1330,1330,1331,1331,1331,1332,1332,1332,1333,1333,1334,1335,1335,1336,1337,1337,1338,1338,1339,1339,1339,1340,1340,1340,1341,1342,1342,1343,1343,1344,1344,1345,1345,1346,1347,1348,1348,1348,1349,1350,1350,1351,1351,1351,1352,1352,1352,1353,1353,1353,1354,1354,1354,1355,1355,1355,1356,1357,1358,1358,1359,1359,1360,1360,1361,1361,1362,1363,1364,1365,1365,1365,1366,1366,1366,1367,1367,1367,1368,1369,1369,1370,1370,1371,1371,1372,1373,1374,1375,1376,1376,1377,1378,1378,1378,1379,1379,1379,1380,1380,1381,1381,1382,1382,1383,1384,1384,1385,1385,1386,1386,1387,1387,1388,1388,1389,1389,1390,1390,1391,1391,1391,1392,1392,1392,1393,1393,1394,1394,1395,1395,1396,1397,1397,1398,1398,1399,1399,1400,1400,1401,1401,1402,1402,1403,1403,1403,1404,1404,1404,1405,1405,1405,1406,1407,1407,1408,1408,1409,1409,1410,1410,1411,1411,1412,1412,1413,1413,1414,1414,1414,1415,1415,1415,1416,1416,1416,1417,1417,1417,1418,1418,1419,1419,1420,1420,1421,1421,1422,1422,1423,1423,1424,1424,1425,1426,1426,1426,1427,1427,1428,1428,1428,1429,1429,1429,1430,1430,1431,1431,1432,1432,1433,1434,1434,1435,1435,1436,1436,1437,1438,1438,1439,1439,1440,1440,1440,1441,1441,1441,1442,1443,1443,1444,1444,1444,1445,1445,1446,1446,1447,1447,1448,1449,1450,1450,1451,1451,1452,1452,1452,1453,1453,1453,1454,1455,1456,1456,1457,1457,1458,1459,1460,1461,1462,1463,1464,1464,1464,1465,1465,1465,1466,1466,1467,1468,1469,1469,1470,1471,1471,1472,1473,1473,1474,1474,1475,1475,1475,1475,1476,1476,1476,1476,1477,1477,1477,1477,1478,1478,1479,1479,1479,1480,1481,1481,1482,1482,1483,1483,1484,1484,1484,1485,1485,1486,1486,1487,1487,1487,1488,1488,1488,1489,1489,1489,1490,1490,1491,1492,1492,1493,1494,1494,1495,1495,1496,1497,1497,1498,1498,1499,1499,1500,1500,1501,1501,1502,1502,1503,1503,1504,1504,1505,1505,1506,1507,1508,1508,1509,1510,1510,1510,1511,1511,1511,1512,1512,1512,1513,1513,1513,1514,1514,1514,1515,1515,1515,1516,1516,1516,1517,1517,1517,1518,1518,1518,1519,1519,1520,1521,1521,1522,1522,1523,1524,1525,1525,1526,1526,1527,1527,1527,1528,1528,1528,1529,1529,1529,1530,1530,1530,1531,1531,1531,1532,1532,1532,1533,1533,1533,1534,1534,1534,1535,1535,1535,1536,1536,1536,1537,1537,1537,1538,1538,1538,1539,1539,1539,1540,1540,1540,1541,1541,1541,1542,1542,1542,1543,1543,1543,1544,1544,1544,1545,1545,1545,1546,1546,1546,1547,1547,1547,1548,1548,1548,1549,1549,1549,1550,1550,1550,1551,1551,1551,1552,1552,1552,1553,1553,1553,1554,1554,1554,1555,1555,1555,1556,1556,1556,1557,1557,1557,1558,1558,1558,1559,1559,1559,1560,1560,1560,1561,1561,1561,1562,1562,1562,1563,1563,1563,1564,1564,1564,1565,1565,1565,1566,1566,1566,1567,1567,1567,1568,1568,1568,1569,1569,1569,1570,1570,1570,1571,1571,1571,1572,1572,1572,1573,1573,1573,1574,1574,1574,1575,1575,1575,1576,1576,1576,1577,1577,1577,1578,1578,1578,1579,1579,1579,1580,1580,1580,1581,1581,1581,1582,1582,1582,1583,1583,1583,1584,1584,1584,1585,1585,1585,1586,1586,1586,1587,1587,1587,1588,1588,1588,1589,1589,1589,1590,1590,1591,1592,1592,1593,1594,1595,1595,1596,1596,1597,1597,1598,1598,1599,1599,1600,1601,1601,1602,1602,1602,1603,1603,1604,1604,1605,1605,1606,1606,1607,1608,1609,1610,1611,1611,1612,1613,1613,1614,1614,1615,1616,1617,1617,1618,1618,1618,1619,1619,1620,1620,1621,1621,1622,1622,1623,1624,1625,1625,1626,1626,1627,1627,1628,1628,1629,1629,1630,1630,1631,1631,1632,1632,1633,1633,1634,1635,1635,1636,1637,1637,1637,1638,1639,1639,1639,1640,1641,1641,1642,1643,1643,1644,1645,1645,1646,1647,1648,1649,1650,1650,1651,1651,1652,1652,1652,1653,1653,1654,1654,1655,1656,1657,1657,1658,1658,1659,1660,1660,1660,1661,1661,1661,1662,1662,1662,1663,1663,1664,1664,1664,1665,1666,1666,1666,1667,1668,1668,1669,1669,1669,1670,1671,1671,1672,1672,1673,1673,1674,1674,1674,1675,1675,1676,1676,1677,1678,1678,1679,1679,1679,1680,1680,1681,1682,1682,1683,1684,1684,1685,1685,1686,1686,1687,1688,1688,1689,1690,1690,1691,1691,1692,1692,1693,1694,1694,1694,1695,1695,1695,1696,1696,1696,1697,1697,1698,1698,1699,1699,1700,1701,1701,1702,1703,1704,1705,1706,1706,1707,1707,1708,1708,1708,1709,1709,1710,1710,1711,1711,1712,1712,1713,1713,1714,1715,1715,1716,1717,1718,1718,1719,1720,1721,1722,1723,1724,1724,1725,1725,1726,1726,1727,1727,1727,1728,1728,1729,1729,1730,1730,1731,1731,1732,1732,1733,1733,1734,1735,1735,1736,1736,1736,1737,1737,1738,1738,1739,1739,1740,1741,1741,1742,1743,1743,1744,1744,1745,1745,1746,1747,1748,1748,1749,1749,1750,1750,1751,1752,1752,1753,1753,1753,1754,1754,1755,1756,1756,1757,1757,1758,1758,1759,1759,1760,1760,1761,1761,1762,1762,1762,1763,1763,1763,1764,1764,1764,1765,1765,1766,1766,1767,1767,1768,1768,1769,1769,1770,1770,1771,1772,1773,1773,1774,1774,1774,1775,1775,1776,1776,1777,1777,1778,1778,1779,1780,1781,1781,1781,1782,1782,1783,1783,1784,1785,1785,1786,1786,1787,1787,1788,1788,1789,1789,1790,1790,1791,1791,1792,1792,1793,1794,1795,1795,1795,1796,1796,1796,1797,1797,1797,1798,1798,1799,1799,1800,1800,1801,1801,1801,1802,1802,1803,1803,1804,1804,1805,1806,1806,1807,1808,1808,1809,1809,1810,1810,1811,1811,1812,1813,1814,1815,1816,1817,1817,1818,1819,1819,1820,1821,1822,1823,1823,1824,1825,1825,1826,1827,1827,1828,1828,1828,1829,1829,1829,1830,1830,1830,1831,1831,1831,1832,1832,1832,1833,1833,1833,1834,1834,1834,1835,1835,1835,1836,1836,1836,1837,1837,1837,1838,1838,1838,1839,1839,1840,1840,1841,1842,1843,1844,1844,1845,1846,1846,1847,1847,1848,1849,1849,1850,1851,1851,1852,1852,1852,1853,1853,1854,1854,1855,1856,1856,1857,1858,1859,1859,1860,1861,1862,1863,1863,1864,1864,1865,1865,1866,1866,1867,1867,1867,1868,1869,1869,1869,1870,1870,1870,1871,1871,1871,1872,1872,1873,1873,1874,1874,1875,1876,1876,1877,1877,1878,1879,1880,1881,1882,1883,1883,1884,1884,1885,1885,1886,1886,1886,1887,1887,1888,1888,1889,1890,1890,1891,1891,1892,1892,1893,1893,1894,1895,1895,1896,1896,1897,1897,1898,1899,1899,1900,1900,1901,1901,1902,1902,1902,1903,1903,1903,1904,1904,1904,1905,1905,1906,1906,1907,1908,1908,1909,1909,1910,1910,1911,1912,1912,1913,1913,1914,1914,1915,1915,1916,1916,1917,1917,1918,1918,1919,1919,1919,1920,1920,1921,1921,1922,1922,1923,1923,1924,1924,1925,1925,1926,1926,1927,1927,1928,1928,1929,1929,1930,1930,1931,1931,1932,1932,1933,1933,1934,1935,1935,1936,1936,1937,1937,1938,1938,1939,1939,1940,1940,1941,1941,1942,1942,1943,1943,1944,1944,1945,1945,1946,1946,1947,1947,1948,1948,1949,1949,1950,1950,1951,1951,1952,1952,1953,1953,1954,1954,1955,1955,1956,1956,1957,1957,1957,1957,1957,1957,1957,1957,1958,1958,1958,1958,1958,1958,1958,1958,1958,1958,1958,1958,1958,1958,1958,1958,1958,1958,1958,1958,1958,1958,1958,1958,1958,1958,1958,1958,1958,1958,1958,1958,1958,1958,1958,1958,1958,1958,1959,1959,1959,1959,1959,1959,1959,1959,1960,1960,1960,1960,1960,1960,1960,1960,1961,1961,1961,1961,1961,1961,1961,1961,1962,1962,1962,1962,1962,1962,1962,1962,1963,1963,1963,1963,1963,1963,1963,1963,1964,1964,1964,1964,1964,1964,1964,1964,1965,1965,1965,1965,1965,1965,1965,1965,1966,1966,1966,1966,1966,1966,1966,1966,1967,1967,1967,1967,1967,1967,1967,1967,1968,1968,1968,1968,1968,1968,1968,1968,1969,1969,1969,1969,1969,1969,1969,1969,1970,1970,1970,1970,1970,1970,1970,1970,1971,1971,1971,1971,1971,1971,1971,1971,1972,1972,1972,1972,1972,1972,1972,1972,1973,1973,1973,1973,1973,1973,1973,1973,1974,1974,1974,1974,1974,1974,1974,1974,1975,1975,1975,1975,1975,1975,1975,1975,1976,1976,1976,1976,1976,1976,1976,1976,1977,1977,1977,1977,1977,1977,1977,1977,1978,1978,1978,1978,1978,1978,1978,1978,1979,1979,1979,1979,1979,1979,1979,1979,1980,1980,1980,1980,1980,1980,1980,1980,1981,1981,1981,1981,1981,1981,1981,1981,1982,1982,1982,1982,1982,1982,1982,1982,1983,1983,1983,1983,1983,1983,1983,1983,1984,1984,1984,1984,1984,1984,1984,1984,1985,1985,1985,1985,1985,1985,1985,1985,1986,1986,1986,1986,1986,1986,1986,1986,1987,1987,1987,1987,1987,1987,1987,1987,1988,1988,1988,1988,1988,1988,1988,1988],"depth":[1,1,1,1,1,1,1,1,1,1,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,2,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,1,1,3,2,1,2,1,2,1,2,1,3,2,1,1,1,2,1,1,1,1,1,1,2,1,2,1,3,2,1,1,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,1,2,1,1,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,3,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,3,2,1,1,3,2,1,1,2,1,3,2,1,1,2,1,2,1,2,1,1,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,1,2,1,1,2,1,2,1,1,3,2,1,3,2,1,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,4,3,2,1,4,3,2,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,1,2,1,3,2,1,3,2,1,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,3,2,1,1,1,2,1,1,3,2,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,1,1,1,2,1,1,2,1,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,1,1,3,2,1,2,1,3,2,1,2,1,1,1,2,1,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,2,1,1,1,1,2,1,2,1,1,3,2,1,1,3,2,1,3,2,1,2,1,1,2,1,3,2,1,1,2,1,1,2,1,1,3,2,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,2,1,1,1,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,3,2,1,1,3,2,1,3,2,1,2,1,2,1,1,2,1,1,2,1,3,2,1,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,1,1,2,1,1,2,1,1,1,2,1,2,1,1,2,1,1,3,2,1,2,1,3,2,1,2,1,2,1,3,2,1,1,1,1,1,3,2,1,1,1,2,1,1,1,2,1,2,1,2,1,2,1,4,3,2,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,3,2,1,2,1,2,1,2,1,3,2,1,2,1,3,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,1,3,2,1,2,1,1,2,1,2,1,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,1,1,2,1,2,1,2,1,1,1,1,2,1,2,1,3,2,1,1,1,2,1,1,1,2,1,3,2,1,2,1,3,2,1,3,2,1,2,1,1,2,1,1,2,1,1,1,1,1,1,2,1,1,1,2,1,1,1,1,2,1,1,3,2,1,3,2,1,2,1,2,1,2,1,1,1,2,1,1,2,1,1,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,3,2,1,1,1,1,2,1,2,1,3,2,1,3,2,1,1,2,1,1,2,1,3,2,1,1,1,2,1,2,1,1,2,1,2,1,1,2,1,1,1,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,1,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,1,2,1,1,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,1,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,1,3,2,1,2,1,3,2,1,3,2,1,1,2,1,1,3,2,1,2,1,2,1,3,2,1,1,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,1,1,3,2,1,3,2,1,2,1,3,2,1,1,2,1,2,1,1,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,1,3,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,1,1,2,1,1,1,2,1,1,3,2,1,1,2,1,2,1,2,1,1,3,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,3,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,1,1,1,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,1,2,1,2,1,3,2,1,1,2,1,1,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,1,1,2,1,2,1,1,1,3,2,1,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,2,1,3,2,1,3,2,1,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,1,1,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,1,2,1,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,1,3,2,1,2,1,1,2,1,1,2,1,2,1,2,1,3,2,1,4,3,2,1,4,3,2,1,2,1,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,3,2,1,3,2,1,2,1,2,1,3,2,1,2,1,1,2,1,1,2,1,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,1,3,2,1,1,2,1,1,1,2,1,2,1,1,3,2,1,3,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,1,1,2,1,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,3,2,1,3,2,1,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,4,3,2,1,4,3,2,1,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,1,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,1,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,1,2,1,1,2,1,1,1,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,1,2,1,1,2,1,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,1,2,1,1,2,1,3,2,1,3,2,1,2,1,1,2,1,1,2,1,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,1,1,3,2,1,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,1,1,2,1,2,1,2,1,2,1,1,1,1,3,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,1,1,1,1,2,1,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,1,2,1,3,2,1,2,1,2,1,2,1,1,1,2,1,2,1,3,2,1,3,2,1,1,1,2,1,2,1,1,1,1,1,1,1,3,2,1,3,2,1,2,1,1,1,2,1,1,2,1,1,2,1,2,1,4,3,2,1,4,3,2,1,4,3,2,1,2,1,3,2,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,1,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,1,1,1,2,1,1,2,1,2,1,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,3,2,1,1,3,2,1,1,2,1,1,2,1,1,2,1,1,1,1,1,2,1,2,1,3,2,1,2,1,2,1,1,1,2,1,2,1,1,3,2,1,3,2,1,3,2,1,2,1,3,2,1,1,3,2,1,1,2,1,3,2,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,3,2,1,2,1,1,2,1,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,1,1,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,1,2,1,1,1,1,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,1,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,1,1,1,1,1,2,1,1,2,1,1,1,1,2,1,1,2,1,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,1,1,1,2,1,1,2,1,2,1,1,2,1,1,2,1,3,2,1,2,1,2,1,1,2,1,1,1,2,1,1,1,1,2,1,2,1,2,1,2,1,3,2,1,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,1,1,1,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,8,7,6,5,4,3,2,1,38,37,36,35,34,33,32,31,30,29,28,27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1],"label":["rowSums","rowSums","rowSums","rowSums","rowSums","rowSums","rowMeans","rowMeans","rowMeans","rowMeans","rowMeans","rowMeans","<GC>","aperm.default","apply","aperm.default","apply","aperm.default","apply","aperm.default","apply","aperm.default","apply","aperm.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","apply","apply","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","apply","mean.default","apply","<GC>","apply","mean.default","apply","FUN","apply","apply","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","<GC>","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","apply","apply","mean.default","apply","apply","apply","apply","apply","apply","length","local","FUN","apply","<GC>","FUN","apply","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","FUN","apply","apply","apply","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","apply","mean.default","apply","mean.default","apply","is.numeric","local","FUN","apply","<GC>","mean.default","apply","FUN","apply","mean.default","apply","apply","apply","mean.default","apply","FUN","apply","FUN","apply","apply","length","local","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","<GC>","length","local","mean.default","apply","FUN","apply","length","local","apply","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","<GC>","length","local","apply","mean.default","apply","mean.default","apply","FUN","apply","length","local","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","apply","mean.default","apply","FUN","apply","<GC>","length","local","FUN","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","mean.default","apply","FUN","apply","is.na","local","FUN","apply","FUN","apply","FUN","apply","apply","<GC>","FUN","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","apply","FUN","apply","<GC>","FUN","apply","apply","isTRUE","mean.default","apply","apply","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","length","local","FUN","apply","apply","apply","FUN","apply","<GC>","mean.default","apply","length","local","FUN","apply","FUN","apply","apply","length","local","apply","FUN","apply","apply","mean.default","apply","length","local","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","FUN","apply","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","mean.default","apply","length","local","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","FUN","apply","<GC>","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","is.numeric","local","mean.default","apply","mean.default","apply","apply","mean.default","apply","mean.default","apply","length","local","<GC>","apply","<GC>","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","mean.default","apply","length","local","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","<GC>","length","local","<GC>","length","local","apply","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","apply","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","<GC>","apply","apply","isTRUE","mean.default","apply","apply","apply","mean.default","apply","apply","isTRUE","mean.default","apply","apply","apply","apply","is.na","local","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","apply","apply","FUN","apply","apply","FUN","apply","apply","mean.default","apply","<GC>","mean.default","apply","FUN","apply","mean.default","apply","apply","FUN","apply","FUN","apply","is.na","local","apply","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","mean.default","apply","mean.default","apply","apply","apply","length","local","apply","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","apply","apply","apply","FUN","apply","mean.default","apply","apply","isTRUE","mean.default","apply","apply","isTRUE","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","apply","FUN","apply","isTRUE","mean.default","apply","apply","length","local","apply","mean.default","apply","apply","isTRUE","mean.default","apply","<GC>","apply","mean.default","apply","isTRUE","mean.default","apply","length","local","apply","is.numeric","local","FUN","apply","FUN","apply","apply","apply","apply","<GC>","apply","FUN","apply","length","local","apply","FUN","apply","apply","FUN","apply","is.na","local","mean.default","apply","FUN","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","apply","FUN","apply","apply","<GC>","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","isTRUE","mean.default","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","is.na","local","isTRUE","mean.default","apply","apply","mean.default","apply","<GC>","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","apply","mean.default","apply","is.numeric","local","apply","apply","<GC>","apply","apply","FUN","apply","apply","apply","FUN","apply","FUN","apply","apply","mean.default","apply","apply","<GC>","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","apply","apply","<GC>","length","local","apply","apply","FUN","apply","apply","apply","FUN","apply","mean.default","apply","is.na","local","FUN","apply","<GC>","isTRUE","mean.default","apply","apply","mean.default","apply","is.numeric","local","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","is.numeric","local","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","<GC>","mean.default","apply","mean.default","apply","length","local","FUN","apply","isTRUE","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","is.na","local","mean.default","apply","FUN","apply","<GC>","apply","<GC>","apply","FUN","apply","is.numeric","local","FUN","apply","FUN","apply","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","mean.default","apply","apply","<GC>","apply","is.numeric","local","apply","FUN","apply","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","apply","FUN","apply","mean.default","apply","FUN","apply","apply","apply","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","length","local","apply","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","is.na","local","<GC>","is.na","local","FUN","apply","apply","FUN","apply","apply","mean.default","apply","apply","apply","apply","apply","apply","FUN","apply","apply","apply","FUN","apply","apply","apply","apply","FUN","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","apply","is.na","local","apply","apply","FUN","apply","FUN","apply","FUN","apply","is.numeric","local","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","<GC>","is.numeric","local","<GC>","is.numeric","local","apply","length","local","FUN","apply","mean.default","apply","FUN","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","apply","apply","FUN","apply","mean.default","apply","<GC>","is.numeric","local","<GC>","is.numeric","local","apply","FUN","apply","apply","length","local","isTRUE","mean.default","apply","apply","apply","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","apply","apply","FUN","apply","FUN","apply","<GC>","apply","<GC>","apply","mean.default","apply","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","mean.default","apply","apply","mean.default","apply","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","apply","FUN","apply","mean.default","apply","FUN","apply","length","local","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","FUN","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","<GC>","apply","<GC>","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","is.numeric","local","apply","apply","mean.default","apply","FUN","apply","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","mean.default","apply","apply","length","local","apply","isTRUE","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","<GC>","length","local","<GC>","length","local","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","apply","FUN","apply","length","local","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","apply","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","mean.default","apply","apply","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","<GC>","apply","<GC>","apply","FUN","apply","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","FUN","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","apply","mean.default","apply","apply","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","FUN","apply","mean.default","apply","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","<GC>","apply","<GC>","apply","mean.default","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","apply","apply","apply","apply","apply","apply","FUN","apply","mean.default","apply","FUN","apply","apply","FUN","apply","<GC>","apply","<GC>","apply","apply","FUN","apply","FUN","apply","is.numeric","local","isTRUE","mean.default","apply","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","is.numeric","local","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","<GC>","apply","<GC>","apply","apply","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","mean.default","apply","apply","is.na","local","FUN","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","is.numeric","local","<GC>","FUN","apply","<GC>","FUN","apply","apply","apply","FUN","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","FUN","apply","mean.default","apply","apply","FUN","apply","length","local","FUN","apply","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","apply","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","FUN","apply","apply","mean.default","apply","FUN","apply","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","length","local","mean.default","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","length","local","mean.default","apply","mean.default","apply","FUN","apply","apply","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","apply","mean.default","apply","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","mean.default","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","apply","is.na","local","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","length","local","isTRUE","mean.default","apply","FUN","apply","apply","mean.default","apply","apply","FUN","apply","apply","length","local","FUN","apply","apply","FUN","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","mean.default","apply","apply","apply","is.numeric","local","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","length","local","FUN","apply","mean.default","apply","apply","FUN","apply","length","local","mean.default","apply","mean.default","apply","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","apply","apply","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","is.numeric","local","FUN","apply","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","apply","FUN","apply","apply","FUN","apply","is.na","local","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","is.numeric","local","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","apply","mean.default","apply","length","local","FUN","apply","mean.default","apply","apply","apply","FUN","apply","mean.default","apply","apply","apply","apply","mean.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","length","local","mean.default","apply","<GC>","apply","<GC>","apply","apply","FUN","apply","apply","apply","apply","mean.default","apply","FUN","apply","apply","FUN","apply","mean.default","apply","apply","FUN","apply","is.numeric","local","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","is.na","local","apply","FUN","apply","apply","FUN","apply","FUN","apply","<GC>","apply","<GC>","apply","<GC>","apply","mean.default","apply","mean.default","apply","apply","mean.default","apply","apply","apply","FUN","apply","apply","FUN","apply","apply","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","mean.default","apply","FUN","apply","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","length","local","mean.default","apply","is.na","local","FUN","apply","FUN","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","mean.default","apply","mean.default","apply","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","mean.default","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","length","local","mean.default","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","FUN","apply","is.na","local","<GC>","apply","<GC>","apply","<GC>","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","apply","mean.default","apply","FUN","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","isTRUE","mean.default","apply","is.numeric","local","apply","mean.default","apply","apply","apply","apply","FUN","apply","FUN","apply","mean.default","apply","<GC>","apply","<GC>","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","FUN","apply","apply","mean.default","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","apply","FUN","apply","length","local","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","is.na","local","length","local","length","local","FUN","apply","apply","apply","isTRUE","mean.default","apply","apply","mean.default","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","length","local","length","local","FUN","apply","apply","apply","apply","apply","mean.default","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","is.numeric","local","FUN","apply","apply","FUN","apply","mean.default","apply","is.numeric","local","mean.default","apply","FUN","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","length","local","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","<GC>","is.numeric","local","<GC>","is.numeric","local","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","apply","isTRUE","mean.default","apply","mean.default","apply","<GC>","is.numeric","local","<GC>","is.numeric","local","is.numeric","local","FUN","apply","FUN","apply","apply","FUN","apply","mean.default","apply","FUN","apply","apply","FUN","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","apply","apply","mean.default","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","apply","FUN","apply","FUN","apply","apply","apply","apply","apply","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","apply","apply","mean.default","apply","apply","mean.default","apply","apply","FUN","apply","FUN","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","apply","FUN","apply","apply","FUN","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","<GC>","apply","<GC>","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","apply","apply","FUN","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","isTRUE","mean.default","apply","is.na","local","apply","mean.default","apply","mean.default","apply","apply","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","apply","FUN","apply","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","apply","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","<GC>","apply","<GC>","apply","<GC>","apply","length","local","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","apply","isTRUE","mean.default","apply","apply","isTRUE","mean.default","apply","apply","mean.default","apply","apply","mean.default","apply","apply","length","local","apply","apply","apply","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","apply","apply","FUN","apply","mean.default","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","length","local","isTRUE","mean.default","apply","apply","isTRUE","mean.default","apply","apply","mean.default","apply","isTRUE","mean.default","apply","apply","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","apply","mean.default","apply","FUN","apply","is.numeric","local","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","apply","is.numeric","local","apply","apply","apply","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","is.numeric","local","length","local","FUN","apply","FUN","apply","apply","mean.default","apply","apply","apply","FUN","apply","apply","apply","apply","apply","apply","FUN","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","is.na","local","apply","FUN","apply","apply","FUN","apply","length","local","mean.default","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","FUN","apply","length","local","mean.default","apply","FUN","apply","mean.default","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","apply","FUN","apply","mean.default","apply","length","local","FUN","apply","is.na","local","FUN","apply","FUN","apply","mean.default","apply","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","apply","length","local","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","apply","apply","apply","apply","apply","mean.default","apply","apply","FUN","apply","apply","apply","apply","mean.default","apply","apply","mean.default","apply","apply","is.na","local","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","mean.default","apply","apply","apply","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","apply","is.numeric","local","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","apply","is.na","local","apply","apply","FUN","apply","apply","apply","apply","FUN","apply","mean.default","apply","FUN","apply","length","local","isTRUE","mean.default","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","apply","apply","apply","apply","apply","mean.default","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","apply","is.na","local","mean.default","apply","mean.default","apply","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","mean.default","apply","apply","length","local","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","mean.default","apply","length","local","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","is.numeric","local","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","cmpCall","cmp","cmpPrim2","h","tryInline","cmpCall","cmp","cmpPrim2","h","tryInline","cmpCall","cmp","h","tryInline","cmpCall","cmp","cmpPrim2","h","tryInline","cmpCall","cmp","cmpComplexAssign","h","tryInline","cmpCall","cmp","h","tryInline","cmpCall","cmp","cmpForBody","h","tryInline","cmpCall","cmp","genCode","compile","compiler:::tryCompile","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis"],"filenum":[1,1,1,1,1,1,1,1,1,1,1,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,1,1,null,1,null,1,null,null,1,1,null,1,null,1,null,1,null,1,1,1,1,1,null,1,null,1,null,1,null,1,null,1,1,1,null,null,1,null,1,null,1,null,1,null,null,1,1,1,null,1,1,1,1,1,1,null,null,null,1,null,null,1,1,1,null,1,null,1,1,null,1,null,1,null,1,null,null,1,1,null,1,null,1,null,1,1,null,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,null,1,null,1,1,1,null,1,1,null,1,null,null,1,null,1,1,null,1,null,1,null,null,null,1,null,null,1,null,1,null,1,1,1,null,1,null,1,null,1,1,null,null,null,1,null,1,null,1,null,1,null,null,null,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,null,1,null,1,null,1,null,1,null,null,null,1,null,1,null,1,null,1,1,null,1,null,1,null,null,null,null,1,null,1,null,1,null,null,1,1,1,null,1,null,1,null,null,null,1,null,1,null,1,1,null,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,1,null,1,1,null,1,null,null,1,1,null,null,1,1,null,1,null,null,1,1,null,1,null,null,null,1,1,1,null,1,null,null,1,null,null,null,1,null,1,1,null,null,1,null,1,1,null,1,null,null,1,null,null,1,null,null,1,1,null,1,null,1,1,null,1,null,1,1,null,1,null,1,null,null,1,null,1,null,null,1,null,null,1,null,1,null,1,null,null,1,null,1,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,null,1,null,1,1,null,1,null,1,null,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,1,null,1,null,null,null,1,null,null,null,1,null,1,null,null,1,null,1,null,1,null,1,null,null,1,null,null,1,1,null,1,null,null,null,null,null,null,1,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,1,null,null,1,1,1,null,1,1,null,null,1,1,1,1,null,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,1,null,1,1,1,1,null,1,1,null,1,1,null,1,null,null,1,null,1,null,1,1,null,1,null,1,null,null,1,1,null,null,1,null,1,null,null,1,null,1,1,1,null,null,1,null,1,null,1,1,null,1,null,1,null,null,1,null,null,1,null,1,1,1,1,null,1,null,1,1,null,null,1,1,null,null,1,null,null,1,null,1,1,null,1,null,null,1,1,null,null,1,null,1,1,null,null,1,null,1,null,1,null,null,1,null,null,1,null,null,null,1,null,1,1,1,1,null,1,null,1,null,null,1,null,1,1,null,1,null,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,1,null,null,1,1,null,null,1,null,null,1,null,1,null,1,1,null,1,1,null,null,null,null,1,1,null,1,null,null,1,null,null,1,null,1,null,1,null,1,1,null,1,null,null,1,1,null,1,1,null,1,1,1,null,1,null,1,1,null,1,1,null,null,1,null,1,null,null,1,null,1,null,1,null,null,1,1,1,1,1,null,null,null,1,1,null,1,1,1,null,1,null,1,null,null,null,1,null,null,null,1,1,null,1,null,null,null,1,null,null,1,null,1,null,1,1,null,1,null,1,null,null,null,1,null,1,null,1,null,1,null,1,null,null,1,1,null,null,1,null,1,null,null,null,1,null,null,1,null,1,null,null,1,null,1,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,null,null,null,1,null,1,null,1,null,1,null,1,null,null,null,1,null,1,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,1,1,null,null,1,null,1,1,null,1,null,null,1,null,1,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,1,1,1,null,1,null,1,null,1,1,1,1,null,1,null,1,null,null,1,1,1,null,null,1,1,null,1,null,null,1,null,1,null,null,null,null,null,null,null,1,1,null,1,1,null,1,1,1,1,1,1,null,1,1,1,null,1,1,1,1,null,1,1,null,null,1,null,null,1,null,1,null,1,null,1,1,1,null,1,1,null,null,1,1,null,1,null,1,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,null,null,null,null,null,null,1,null,null,null,1,null,1,null,1,1,null,1,null,1,null,1,null,null,1,null,1,null,1,1,null,null,1,1,1,1,null,1,null,1,null,null,null,null,null,null,1,null,1,1,null,null,null,null,1,1,1,null,1,null,1,1,null,1,null,1,1,null,1,1,1,1,null,1,null,1,null,1,null,1,null,1,1,null,null,1,null,1,1,1,null,1,1,null,1,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,null,null,null,1,null,null,1,1,null,1,1,1,null,1,null,null,1,null,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,1,null,1,null,1,null,1,null,1,null,null,1,1,null,1,null,1,1,null,1,null,null,1,null,null,1,null,1,null,1,1,null,null,1,null,null,1,null,1,null,null,1,null,null,1,1,null,1,1,null,null,1,null,1,null,1,null,null,1,1,1,null,null,null,null,null,null,null,1,null,1,null,1,null,1,1,null,1,null,null,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,1,1,1,null,null,1,null,null,1,null,1,null,null,1,1,null,1,null,1,1,1,1,null,1,null,1,null,1,null,1,1,null,1,null,1,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,1,null,1,1,null,null,1,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,null,1,1,1,1,null,1,1,1,null,1,1,null,null,1,1,null,1,null,1,null,1,1,null,null,1,null,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,null,1,null,1,null,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,1,1,1,1,1,1,null,1,null,1,null,1,1,null,1,null,1,null,1,1,null,1,null,1,null,null,null,null,1,1,1,null,1,1,null,1,null,1,null,1,null,1,null,null,null,1,null,1,null,null,1,null,null,1,1,null,1,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,1,null,1,null,1,null,1,1,null,1,null,1,null,null,1,1,null,1,null,1,null,null,1,1,null,1,1,null,1,null,null,1,null,null,1,null,1,null,1,1,null,null,null,1,null,1,null,1,1,null,1,1,null,1,1,null,1,null,1,null,1,null,null,null,null,1,null,null,1,1,1,null,1,null,1,1,1,null,null,1,1,null,1,null,1,1,null,1,null,1,null,null,1,null,1,null,1,null,null,1,null,null,1,1,null,1,null,1,1,null,1,null,null,null,1,1,null,1,null,1,null,1,null,1,1,1,1,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,1,null,1,1,null,1,null,1,1,null,1,null,1,null,null,1,null,1,null,1,null,null,null,1,null,1,null,1,null,null,1,null,null,1,null,null,null,1,null,1,null,1,1,null,1,1,null,null,1,null,1,1,null,1,1,null,1,null,1,null,1,null,null,1,null,null,null,1,null,null,null,1,null,1,1,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,1,null,null,null,null,1,null,null,1,null,1,null,null,null,null,1,null,1,1,null,1,1,null,1,1,null,null,null,1,1,null,1,null,1,null,null,1,null,null,1,null,null,1,1,null,1,null,1,null,1,null,1,1,null,null,1,1,null,1,1,1,null,null,null,1,1,null,null,1,null,null,1,null,1,null,null,1,null,1,null,1,null,null,null,1,null,1,1,null,1,null,null,null,1,null,1,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,1,1,null,1,null,1,null,null,1,null,1,1,1,null,1,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,null,null,1,1,null,1,null,1,null,1,null,1,null,1,1,null,1,1,null,null,1,null,null,1,1,1,null,1,1,null,1,null,null,null,1,null,1,null,1,null,null,1,null,1,null,1,null,null,null,1,null,null,null,1,null,null,null,1,1,null,1,null,null,null,1,null,1,1,1,null,1,null,1,1,1,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,null,null,1,null,1,null,1,1,null,1,1,1,1,null,1,null,1,1,null,1,null,1,1,null,1,null,null,null,null,1,null,null,1,null,1,null,1,null,1,1,null,1,null,1,null,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,1,1,null,1,1,null,1,1,1,null,1,null,null,1,null,null,1,1,null,1,null,1,null,1,1,null,1,null,null,1,null,null,null,1,null,null,null,1,null,1,null,1,null,null,1,null,null,1,1,null,1,null,1,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,1,null,1,1,null,1,1,null,1,null,1,null,1,null,null,1,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,null,null,1,null,1,null,1,1,null,1,null,1,null,null,null,1,null,1,null,1,1,null,1,null,1,null,1,1,null,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,1,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,1,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,1,null,1,1,null,1,null,null,1,null,null,1,null,1,1,null,1,1,null,1,null,null,null,null,1,null,null,1,1,null,null,null,null,null,null,null,1,1,1,null,null,1,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,1,1,null,1,null,1,null,1,null,1,1,1,1,null,null,1,null,null,1,null,null,1,1,null,null,null,null,null,1,1,1,1,1,null,1,1,null,null,1,null,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,1,null,null,null,1,1,null,1,null,1,null,null,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,1,null,1,null,null,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,null,null,null,null,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,null,1,null,1,null,null,null,null,null,null,null,null,null,1,null,1,1,null,1,null,1,null,1,1,null,1,null,1,null,null,1,null,null,1,1,null,1,null,null,1,null,1,null,1,null,1,1,1,null,1,null,1,null,null,1,null,null,1,1,1,null,1,null,1,1,1,1,1,1,1,null,null,1,null,null,1,null,1,1,1,null,1,1,null,1,1,null,1,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,1,null,null,1,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,1,1,null,1,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,1,null,1,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,1,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,1,null,1,1,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,null,1,null,1,null,1,null,1,null,1,1,1,1,1,null,1,1,null,1,null,1,1,1,null,1,null,null,1,null,1,null,1,null,1,null,1,1,1,null,1,null,1,null,1,null,1,null,null,null,1,null,1,null,1,null,1,1,null,1,1,null,null,1,1,null,null,1,1,null,1,1,null,1,1,null,null,1,1,1,1,null,1,null,1,null,null,1,null,1,null,1,1,1,null,1,null,1,1,null,null,1,null,null,1,null,null,1,null,null,null,null,1,1,null,null,1,1,null,1,null,null,1,1,null,1,null,1,null,1,null,null,1,null,1,null,1,1,null,1,null,null,1,null,1,1,null,1,1,null,1,null,1,null,null,1,null,1,1,null,1,null,1,null,1,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,1,1,null,null,1,1,1,1,null,1,null,1,null,null,1,null,1,null,null,null,null,null,1,null,1,1,null,1,1,1,null,1,1,1,1,1,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,null,1,null,1,null,1,null,null,1,null,1,1,null,1,null,null,null,1,1,1,null,1,null,1,null,1,1,null,1,null,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,null,null,1,null,1,null,1,1,1,null,1,null,null,1,null,1,null,1,null,1,null,1,1,1,null,null,1,null,1,null,1,1,null,1,null,1,null,null,null,1,null,null,null,1,null,1,null,1,1,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,1,null,null,1,null,1,null,1,null,1,null,1,1,1,1,1,1,null,1,1,null,1,1,1,1,null,1,1,null,1,1,null,null,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,1,1,1,null,1,1,null,1,null,1,1,null,null,1,null,1,null,null,1,null,1,null,1,1,null,null,1,1,null,1,1,1,1,null,1,null,1,null,1,null,null,null,null,1,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,1,1,null,1,null,1,1,1,1,1,1,null,1,null,1,null,1,null,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,1,null,null,null,1,null,1,1,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,1,null,null,null,1,null,1,1,null,1,null,1,null,1,null,null,null,1,null,1,null,1,null,null,1,null,1,null,1,null,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,1,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null],"linenum":[10,10,10,10,10,10,11,11,11,11,11,11,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,12,12,null,12,null,12,null,null,12,12,null,12,null,12,null,12,null,12,12,12,12,12,null,12,null,12,null,12,null,12,null,12,12,12,null,null,12,null,12,null,12,null,12,null,null,12,12,12,null,12,12,12,12,12,12,null,null,null,12,null,null,12,12,12,null,12,null,12,12,null,12,null,12,null,12,null,null,12,12,null,12,null,12,null,12,12,null,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,null,12,null,12,12,12,null,12,12,null,12,null,null,12,null,12,12,null,12,null,12,null,null,null,12,null,null,12,null,12,null,12,12,12,null,12,null,12,null,12,12,null,null,null,12,null,12,null,12,null,12,null,null,null,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,null,12,null,12,null,12,null,12,null,null,null,12,null,12,null,12,null,12,12,null,12,null,12,null,null,null,null,12,null,12,null,12,null,null,12,12,12,null,12,null,12,null,null,null,12,null,12,null,12,12,null,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,12,null,12,12,null,12,null,null,12,12,null,null,12,12,null,12,null,null,12,12,null,12,null,null,null,12,12,12,null,12,null,null,12,null,null,null,12,null,12,12,null,null,12,null,12,12,null,12,null,null,12,null,null,12,null,null,12,12,null,12,null,12,12,null,12,null,12,12,null,12,null,12,null,null,12,null,12,null,null,12,null,null,12,null,12,null,12,null,null,12,null,12,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,null,12,null,12,12,null,12,null,12,null,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,12,null,12,null,null,null,12,null,null,null,12,null,12,null,null,12,null,12,null,12,null,12,null,null,12,null,null,12,12,null,12,null,null,null,null,null,null,12,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,12,12,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,12,null,null,12,12,12,null,12,12,null,null,12,12,12,12,null,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,12,null,12,12,12,12,null,12,12,null,12,12,null,12,null,null,12,null,12,null,12,12,null,12,null,12,null,null,12,12,null,null,12,null,12,null,null,12,null,12,12,12,null,null,12,null,12,null,12,12,null,12,null,12,null,null,12,null,null,12,null,12,12,12,12,null,12,null,12,12,null,null,12,12,null,null,12,null,null,12,null,12,12,null,12,null,null,12,12,null,null,12,null,12,12,null,null,12,null,12,null,12,null,null,12,null,null,12,null,null,null,12,null,12,12,12,12,null,12,null,12,null,null,12,null,12,12,null,12,null,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,12,null,null,12,12,null,null,12,null,null,12,null,12,null,12,12,null,12,12,null,null,null,null,12,12,null,12,null,null,12,null,null,12,null,12,null,12,null,12,12,null,12,null,null,12,12,null,12,12,null,12,12,12,null,12,null,12,12,null,12,12,null,null,12,null,12,null,null,12,null,12,null,12,null,null,12,12,12,12,12,null,null,null,12,12,null,12,12,12,null,12,null,12,null,null,null,12,null,null,null,12,12,null,12,null,null,null,12,null,null,12,null,12,null,12,12,null,12,null,12,null,null,null,12,null,12,null,12,null,12,null,12,null,null,12,12,null,null,12,null,12,null,null,null,12,null,null,12,null,12,null,null,12,null,12,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,null,null,12,null,12,null,12,null,12,null,12,null,null,null,12,null,12,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,12,12,null,null,12,null,12,12,null,12,null,null,12,null,12,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,12,12,12,null,12,null,12,null,12,12,12,12,null,12,null,12,null,null,12,12,12,null,null,12,12,null,12,null,null,12,null,12,null,null,null,null,null,null,null,12,12,null,12,12,null,12,12,12,12,12,12,null,12,12,12,null,12,12,12,12,null,12,12,null,null,12,null,null,12,null,12,null,12,null,12,12,12,null,12,12,null,null,12,12,null,12,null,12,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,null,null,null,null,null,12,null,null,null,12,null,12,null,12,12,null,12,null,12,null,12,null,null,12,null,12,null,12,12,null,null,12,12,12,12,null,12,null,12,null,null,null,null,null,null,12,null,12,12,null,null,null,null,12,12,12,null,12,null,12,12,null,12,null,12,12,null,12,12,12,12,null,12,null,12,null,12,null,12,null,12,12,null,null,12,null,12,12,12,null,12,12,null,12,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,null,null,null,12,null,null,12,12,null,12,12,12,null,12,null,null,12,null,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,12,null,12,null,12,null,12,null,12,null,null,12,12,null,12,null,12,12,null,12,null,null,12,null,null,12,null,12,null,12,12,null,null,12,null,null,12,null,12,null,null,12,null,null,12,12,null,12,12,null,null,12,null,12,null,12,null,null,12,12,12,null,null,null,null,null,null,null,12,null,12,null,12,null,12,12,null,12,null,null,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,12,12,12,null,null,12,null,null,12,null,12,null,null,12,12,null,12,null,12,12,12,12,null,12,null,12,null,12,null,12,12,null,12,null,12,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,12,null,12,12,null,null,12,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,null,12,12,12,12,null,12,12,12,null,12,12,null,null,12,12,null,12,null,12,null,12,12,null,null,12,null,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,null,12,null,12,null,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,12,12,12,12,12,12,null,12,null,12,null,12,12,null,12,null,12,null,12,12,null,12,null,12,null,null,null,null,12,12,12,null,12,12,null,12,null,12,null,12,null,12,null,null,null,12,null,12,null,null,12,null,null,12,12,null,12,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,12,null,12,null,12,null,12,12,null,12,null,12,null,null,12,12,null,12,null,12,null,null,12,12,null,12,12,null,12,null,null,12,null,null,12,null,12,null,12,12,null,null,null,12,null,12,null,12,12,null,12,12,null,12,12,null,12,null,12,null,12,null,null,null,null,12,null,null,12,12,12,null,12,null,12,12,12,null,null,12,12,null,12,null,12,12,null,12,null,12,null,null,12,null,12,null,12,null,null,12,null,null,12,12,null,12,null,12,12,null,12,null,null,null,12,12,null,12,null,12,null,12,null,12,12,12,12,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,12,null,12,12,null,12,null,12,12,null,12,null,12,null,null,12,null,12,null,12,null,null,null,12,null,12,null,12,null,null,12,null,null,12,null,null,null,12,null,12,null,12,12,null,12,12,null,null,12,null,12,12,null,12,12,null,12,null,12,null,12,null,null,12,null,null,null,12,null,null,null,12,null,12,12,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,12,null,null,null,null,12,null,null,12,null,12,null,null,null,null,12,null,12,12,null,12,12,null,12,12,null,null,null,12,12,null,12,null,12,null,null,12,null,null,12,null,null,12,12,null,12,null,12,null,12,null,12,12,null,null,12,12,null,12,12,12,null,null,null,12,12,null,null,12,null,null,12,null,12,null,null,12,null,12,null,12,null,null,null,12,null,12,12,null,12,null,null,null,12,null,12,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,12,12,null,12,null,12,null,null,12,null,12,12,12,null,12,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,null,null,12,12,null,12,null,12,null,12,null,12,null,12,12,null,12,12,null,null,12,null,null,12,12,12,null,12,12,null,12,null,null,null,12,null,12,null,12,null,null,12,null,12,null,12,null,null,null,12,null,null,null,12,null,null,null,12,12,null,12,null,null,null,12,null,12,12,12,null,12,null,12,12,12,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,null,null,12,null,12,null,12,12,null,12,12,12,12,null,12,null,12,12,null,12,null,12,12,null,12,null,null,null,null,12,null,null,12,null,12,null,12,null,12,12,null,12,null,12,null,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,12,12,null,12,12,null,12,12,12,null,12,null,null,12,null,null,12,12,null,12,null,12,null,12,12,null,12,null,null,12,null,null,null,12,null,null,null,12,null,12,null,12,null,null,12,null,null,12,12,null,12,null,12,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,12,null,12,12,null,12,12,null,12,null,12,null,12,null,null,12,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,null,null,12,null,12,null,12,12,null,12,null,12,null,null,null,12,null,12,null,12,12,null,12,null,12,null,12,12,null,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,12,12,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,12,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,12,null,12,12,null,12,null,null,12,null,null,12,null,12,12,null,12,12,null,12,null,null,null,null,12,null,null,12,12,null,null,null,null,null,null,null,12,12,12,null,null,12,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,12,12,null,12,null,12,null,12,null,12,12,12,12,null,null,12,null,null,12,null,null,12,12,null,null,null,null,null,12,12,12,12,12,null,12,12,null,null,12,null,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,12,null,null,null,12,12,null,12,null,12,null,null,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,12,null,12,null,null,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,null,null,null,null,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,null,12,null,12,null,null,null,null,null,null,null,null,null,12,null,12,12,null,12,null,12,null,12,12,null,12,null,12,null,null,12,null,null,12,12,null,12,null,null,12,null,12,null,12,null,12,12,12,null,12,null,12,null,null,12,null,null,12,12,12,null,12,null,12,12,12,12,12,12,12,null,null,12,null,null,12,null,12,12,12,null,12,12,null,12,12,null,12,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,12,null,null,12,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,12,12,null,12,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,12,null,12,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,12,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,12,null,12,12,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,null,12,null,12,null,12,null,12,null,12,12,12,12,12,null,12,12,null,12,null,12,12,12,null,12,null,null,12,null,12,null,12,null,12,null,12,12,12,null,12,null,12,null,12,null,12,null,null,null,12,null,12,null,12,null,12,12,null,12,12,null,null,12,12,null,null,12,12,null,12,12,null,12,12,null,null,12,12,12,12,null,12,null,12,null,null,12,null,12,null,12,12,12,null,12,null,12,12,null,null,12,null,null,12,null,null,12,null,null,null,null,12,12,null,null,12,12,null,12,null,null,12,12,null,12,null,12,null,12,null,null,12,null,12,null,12,12,null,12,null,null,12,null,12,12,null,12,12,null,12,null,12,null,null,12,null,12,12,null,12,null,12,null,12,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,12,12,null,null,12,12,12,12,null,12,null,12,null,null,12,null,12,null,null,null,null,null,12,null,12,12,null,12,12,12,null,12,12,12,12,12,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,null,12,null,12,null,12,null,null,12,null,12,12,null,12,null,null,null,12,12,12,null,12,null,12,null,12,12,null,12,null,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,null,null,12,null,12,null,12,12,12,null,12,null,null,12,null,12,null,12,null,12,null,12,12,12,null,null,12,null,12,null,12,12,null,12,null,12,null,null,null,12,null,null,null,12,null,12,null,12,12,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,12,null,null,12,null,12,null,12,null,12,null,12,12,12,12,12,12,null,12,12,null,12,12,12,12,null,12,12,null,12,12,null,null,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,12,12,12,null,12,12,null,12,null,12,12,null,null,12,null,12,null,null,12,null,12,null,12,12,null,null,12,12,null,12,12,12,12,null,12,null,12,null,12,null,null,null,null,12,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,12,12,null,12,null,12,12,12,12,12,12,null,12,null,12,null,12,null,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,12,null,null,null,12,null,12,12,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,12,null,null,null,12,null,12,12,null,12,null,12,null,12,null,null,null,12,null,12,null,12,null,null,12,null,12,null,12,null,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,13,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,13,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null],"memalloc":[124.4672927856445,124.4672927856445,124.4672927856445,124.4672927856445,124.4672927856445,124.4672927856445,139.7495269775391,139.7495269775391,139.7495269775391,139.7495269775391,139.7495269775391,139.7495269775391,124.4609527587891,124.4609527587891,124.4609527587891,170.2152709960938,170.2152709960938,170.2152709960938,170.2152709960938,170.2152709960938,170.2152709960938,170.2152709960938,170.2152709960938,170.2152709960938,170.2152709960938,170.2153167724609,170.2153167724609,170.2153167724609,170.2153167724609,170.2153167724609,170.2153167724609,170.2153167724609,170.2153167724609,170.2153167724609,170.2153167724609,170.2153167724609,170.2153167724609,170.2153167724609,170.2153167724609,170.2153167724609,170.2153167724609,170.2153167724609,170.2153167724609,170.2150115966797,170.2150115966797,185.5392913818359,185.5392913818359,185.7291564941406,185.7291564941406,185.9304656982422,185.9304656982422,186.1371612548828,186.1371612548828,186.3586273193359,186.3586273193359,186.5914688110352,186.5914688110352,186.8340148925781,186.8340148925781,187.0720748901367,187.300895690918,187.5296173095703,187.759765625,187.759765625,187.9889755249023,187.9889755249023,188.2204132080078,188.2204132080078,188.2204132080078,188.4554214477539,188.6931762695312,188.6931762695312,188.7336578369141,188.7336578369141,185.7566375732422,185.7566375732422,185.9919357299805,185.9919357299805,186.2341690063477,186.4771957397461,186.7426910400391,186.9822235107422,187.216423034668,187.216423034668,187.4480361938477,187.4480361938477,187.6786117553711,187.6786117553711,187.9077835083008,187.9077835083008,188.139778137207,188.139778137207,188.3728866577148,188.6045532226562,188.8034286499023,188.8034286499023,188.8034286499023,185.7583160400391,185.7583160400391,185.9727325439453,185.9727325439453,186.2033309936523,186.2033309936523,186.4445648193359,186.4445648193359,186.4445648193359,186.6848373413086,186.923942565918,187.1594467163086,187.1594467163086,187.3912353515625,187.6225128173828,187.8519897460938,188.0812759399414,188.3109741210938,188.5406341552734,188.5406341552734,188.7717742919922,188.7717742919922,188.8905181884766,188.8905181884766,188.8905181884766,185.9384765625,186.1465911865234,186.3686752319336,186.3686752319336,186.6076889038086,186.6076889038086,186.8470993041992,187.0842666625977,187.0842666625977,187.3410034179688,187.3410034179688,187.5715637207031,187.5715637207031,187.8032150268555,187.8032150268555,187.8032150268555,188.03271484375,188.2625885009766,188.2625885009766,188.4909362792969,188.4909362792969,188.7208023071289,188.7208023071289,188.949577331543,188.9762649536133,188.9762649536133,188.9762649536133,186.1728668212891,186.1728668212891,186.3985290527344,186.3985290527344,186.6319732666016,186.6319732666016,186.8744888305664,187.1139602661133,187.1139602661133,187.3498001098633,187.3498001098633,187.5820007324219,187.5820007324219,187.8109359741211,187.8109359741211,188.0396499633789,188.2671890258789,188.2671890258789,188.4952926635742,188.4952926635742,188.7242889404297,188.7242889404297,188.9545822143555,188.9545822143555,189.0605239868164,189.0605239868164,189.0605239868164,186.2230758666992,186.2230758666992,186.4383926391602,186.6726455688477,186.9168395996094,186.9168395996094,187.1574172973633,187.3957290649414,187.3957290649414,187.6317596435547,187.6317596435547,187.6317596435547,187.887809753418,187.887809753418,188.1215515136719,188.3527984619141,188.3527984619141,188.5840530395508,188.5840530395508,188.8146286010742,188.8146286010742,189.045539855957,189.045539855957,189.1434783935547,189.1434783935547,189.1434783935547,186.3543853759766,186.3543853759766,186.5679550170898,186.5679550170898,186.7941284179688,187.0346221923828,187.2728881835938,187.2728881835938,187.5097198486328,187.5097198486328,187.743293762207,187.743293762207,187.9756774902344,188.2078094482422,188.2078094482422,188.4385375976562,188.4385375976562,188.6702117919922,188.6702117919922,188.9016494750977,188.9016494750977,189.1344528198242,189.1344528198242,189.2250518798828,189.2250518798828,189.2250518798828,186.4929504394531,186.4929504394531,186.7105178833008,186.7105178833008,186.9453506469727,186.9453506469727,187.1878814697266,187.4240188598633,187.4240188598633,187.6598968505859,187.6598968505859,187.8938140869141,187.8938140869141,188.1239776611328,188.1239776611328,188.3554458618164,188.3554458618164,188.5853500366211,188.5853500366211,188.8395919799805,188.8395919799805,189.0703659057617,189.0703659057617,189.3023223876953,189.3023223876953,189.3023223876953,189.3053283691406,189.3053283691406,189.3053283691406,186.6875305175781,186.9048080444336,186.9048080444336,187.1401214599609,187.1401214599609,187.37890625,187.37890625,187.6149444580078,187.6149444580078,187.8509902954102,187.8509902954102,188.083984375,188.083984375,188.315788269043,188.315788269043,188.5479278564453,188.5479278564453,188.7783279418945,189.008918762207,189.008918762207,189.2398452758789,189.2398452758789,189.3843002319336,189.3843002319336,189.3843002319336,186.6775894165039,186.6775894165039,186.8848876953125,186.8848876953125,187.1108551025391,187.1108551025391,187.3497009277344,187.3497009277344,187.3497009277344,187.5871505737305,187.822639465332,188.0571975708008,188.0571975708008,188.2900543212891,188.2900543212891,188.5232849121094,188.5232849121094,188.7557525634766,188.7557525634766,188.9858169555664,188.9858169555664,189.2162017822266,189.2162017822266,189.4470825195312,189.462043762207,189.462043762207,189.462043762207,186.9405212402344,186.9405212402344,187.1584625244141,187.1584625244141,187.397087097168,187.6338043212891,187.6338043212891,187.8696670532227,187.8696670532227,188.1057205200195,188.1057205200195,188.3406448364258,188.3406448364258,188.5752868652344,188.5752868652344,188.8086929321289,189.0409469604492,189.0409469604492,189.273193359375,189.5056076049805,189.5056076049805,189.5384368896484,189.5384368896484,189.5384368896484,187.0165100097656,187.2333450317383,187.2333450317383,187.2333450317383,187.4683532714844,187.7061080932617,187.7061080932617,187.9433212280273,187.9433212280273,187.9433212280273,188.1806106567383,188.4155197143555,188.4155197143555,188.6471557617188,188.6471557617188,188.8791275024414,188.8791275024414,189.1101150512695,189.3420944213867,189.5736465454102,189.5736465454102,189.6136779785156,189.6136779785156,189.6136779785156,187.1241607666016,187.1241607666016,187.3382339477539,187.3382339477539,187.5687942504883,187.5687942504883,187.8285903930664,188.062255859375,188.062255859375,188.2983169555664,188.5329284667969,188.5329284667969,188.7642135620117,188.9960021972656,188.9960021972656,189.2272644042969,189.2272644042969,189.4597930908203,189.6876831054688,189.6876831054688,189.6876831054688,189.6876831054688,189.6876831054688,189.6876831054688,187.281623840332,187.4982604980469,187.4982604980469,187.7262725830078,187.7262725830078,187.9615859985352,188.1956634521484,188.1956634521484,188.4323348999023,188.4323348999023,188.6670074462891,188.898796081543,188.898796081543,189.1317672729492,189.1317672729492,189.3646621704102,189.3646621704102,189.3646621704102,189.5974960327148,189.5974960327148,189.7605133056641,189.7605133056641,189.7605133056641,189.7605133056641,189.7605133056641,189.7605133056641,187.4379577636719,187.4379577636719,187.6532897949219,187.6532897949219,187.8749160766602,187.8749160766602,188.1079254150391,188.3437881469727,188.3437881469727,188.5824813842773,188.8175888061523,188.8175888061523,189.0521621704102,189.0521621704102,189.3103561401367,189.5450897216797,189.5450897216797,189.7795104980469,189.7795104980469,189.8321533203125,189.8321533203125,187.4437637329102,187.4437637329102,187.6566162109375,187.6566162109375,187.8770294189453,187.8770294189453,188.1104354858398,188.1104354858398,188.1104354858398,188.3462753295898,188.3462753295898,188.5842056274414,188.5842056274414,188.8182830810547,188.8182830810547,189.0503234863281,189.2843704223633,189.2843704223633,189.5168762207031,189.5168762207031,189.7493896484375,189.7493896484375,189.9026031494141,189.9026031494141,189.9026031494141,189.9026031494141,187.6741714477539,187.6741714477539,187.8882064819336,187.8882064819336,188.109130859375,188.109130859375,188.3409194946289,188.3409194946289,188.5762329101562,188.5762329101562,188.8114395141602,189.0466842651367,189.0466842651367,189.2809448242188,189.2809448242188,189.5149230957031,189.7461700439453,189.7461700439453,189.9720077514648,189.9720077514648,189.9720077514648,189.9720077514648,189.9720077514648,189.9720077514648,189.9720077514648,189.9720077514648,187.7393417358398,187.7393417358398,187.9492111206055,187.9492111206055,188.1680068969727,188.3998794555664,188.3998794555664,188.6353149414062,188.6353149414062,188.8728942871094,188.8728942871094,189.1094589233398,189.1094589233398,189.1094589233398,189.3439025878906,189.3439025878906,189.3439025878906,189.5862808227539,189.8294143676758,189.8294143676758,190.0401840209961,190.0401840209961,190.0401840209961,190.0401840209961,190.0401840209961,190.0401840209961,187.8466262817383,188.056037902832,188.2744598388672,188.2744598388672,188.5073089599609,188.5073089599609,188.7419281005859,188.7419281005859,188.7419281005859,188.9805679321289,188.9805679321289,189.2171325683594,189.2171325683594,189.4599914550781,189.4599914550781,189.7033386230469,189.7033386230469,189.9451446533203,189.9451446533203,190.1072998046875,190.1072998046875,190.1072998046875,190.1072998046875,190.1072998046875,190.1072998046875,187.9839859008789,187.9839859008789,188.189338684082,188.4055328369141,188.6371002197266,188.6371002197266,188.8706436157227,188.8706436157227,189.128303527832,189.128303527832,189.3609237670898,189.3609237670898,189.5918502807617,189.5918502807617,189.8226165771484,189.8226165771484,190.0541229248047,190.1732711791992,190.1732711791992,187.9145050048828,188.1036911010742,188.1036911010742,188.1036911010742,188.3091506958008,188.5250549316406,188.7594451904297,188.7594451904297,188.9964904785156,189.2337646484375,189.2337646484375,189.2337646484375,189.4706268310547,189.7061157226562,189.9500274658203,190.192741394043,190.192741394043,190.2382888793945,190.2382888793945,190.2382888793945,190.2382888793945,190.2382888793945,190.2382888793945,190.2382888793945,190.2382888793945,190.2382888793945,190.2382888793945,190.2382888793945,190.2382888793945,190.2382888793945,190.2382888793945,190.2382888793945,190.2382888793945,190.2382888793945,190.2382888793945,190.2382888793945,190.2382888793945,188.0017242431641,188.0017242431641,188.1067276000977,188.1067276000977,188.1067276000977,188.282600402832,188.466796875,188.466796875,188.6584701538086,188.8692932128906,189.0936508178711,189.3313522338867,189.3313522338867,189.5646286010742,189.790397644043,189.790397644043,190.0196380615234,190.251953125,190.251953125,190.3019561767578,190.3019561767578,190.3019561767578,188.1660919189453,188.1660919189453,188.3641586303711,188.3641586303711,188.5692672729492,188.7933502197266,188.7933502197266,189.0304183959961,189.0304183959961,189.2696228027344,189.2696228027344,189.5088348388672,189.7450485229492,189.9811706542969,189.9811706542969,189.9811706542969,190.2256011962891,190.2256011962891,190.3649291992188,190.3649291992188,190.3649291992188,188.213005065918,188.213005065918,188.406494140625,188.6076583862305,188.8215484619141,188.8215484619141,189.0555801391602,189.2935256958008,189.2935256958008,189.5323638916016,189.5323638916016,189.7693099975586,190.0040969848633,190.0040969848633,190.2416229248047,190.2416229248047,190.4267959594727,190.4267959594727,190.4267959594727,190.4267959594727,190.4267959594727,190.4267959594727,188.4096450805664,188.4096450805664,188.6013336181641,188.8055191040039,189.0267944335938,189.2626342773438,189.2626342773438,189.4986877441406,189.4986877441406,189.734733581543,189.9680709838867,189.9680709838867,189.9680709838867,190.2009048461914,190.4443130493164,190.4443130493164,190.4443130493164,190.4876937866211,190.4876937866211,190.4876937866211,188.4546585083008,188.4546585083008,188.6437606811523,188.8450317382812,188.8450317382812,189.0619583129883,189.0619583129883,189.0619583129883,189.3203964233398,189.5568161010742,189.5568161010742,189.7931289672852,190.0258712768555,190.0258712768555,190.2578582763672,190.4862823486328,190.4862823486328,190.4862823486328,190.5476303100586,190.5476303100586,188.5313339233398,188.5313339233398,188.7178421020508,188.7178421020508,188.7178421020508,188.9145355224609,188.9145355224609,189.1291198730469,189.3618392944336,189.3618392944336,189.5995712280273,189.5995712280273,189.8369903564453,189.8369903564453,190.0726547241211,190.3074417114258,190.5452880859375,190.6065292358398,190.6065292358398,188.6317977905273,188.6317977905273,188.8229141235352,188.8229141235352,189.0249328613281,189.2490158081055,189.2490158081055,189.4864349365234,189.7253646850586,189.7253646850586,189.964225769043,189.964225769043,190.2023239135742,190.2023239135742,190.4418334960938,190.4418334960938,190.6645812988281,190.6645812988281,190.6645812988281,190.6645812988281,188.793586730957,188.793586730957,188.9873123168945,188.9873123168945,189.1970291137695,189.1970291137695,189.4295806884766,189.4295806884766,189.6687164306641,189.6687164306641,189.6687164306641,189.9085845947266,189.9085845947266,190.147102355957,190.383415222168,190.383415222168,190.6194152832031,190.7216644287109,190.7216644287109,188.7756195068359,188.7756195068359,188.9651565551758,188.9651565551758,189.1660537719727,189.1660537719727,189.3847198486328,189.3847198486328,189.6215744018555,189.6215744018555,189.8614730834961,189.8614730834961,189.8614730834961,190.1008682250977,190.3392944335938,190.3392944335938,190.3392944335938,190.5748291015625,190.7778015136719,190.7778015136719,190.7778015136719,190.7778015136719,190.7778015136719,190.7778015136719,188.9710083007812,188.9710083007812,189.1656112670898,189.1656112670898,189.3760757446289,189.6073532104492,189.6073532104492,189.8460540771484,190.1091842651367,190.1091842651367,190.3487014770508,190.3487014770508,190.3487014770508,190.5839004516602,190.8189697265625,190.8189697265625,190.8330230712891,190.8330230712891,190.8330230712891,189.0030670166016,189.0030670166016,189.0030670166016,189.1869583129883,189.1869583129883,189.3906860351562,189.3906860351562,189.6161575317383,189.6161575317383,189.8531188964844,190.0906677246094,190.0906677246094,190.3298568725586,190.3298568725586,190.5708160400391,190.8163070678711,190.8873748779297,190.8873748779297,189.0519943237305,189.2394332885742,189.2394332885742,189.4385986328125,189.6582412719727,189.8960647583008,189.8960647583008,190.1350631713867,190.1350631713867,190.3752059936523,190.6161041259766,190.6161041259766,190.8629379272461,190.9408645629883,190.9408645629883,190.9408645629883,189.1282348632812,189.1282348632812,189.3344268798828,189.3344268798828,189.3344268798828,189.5329360961914,189.5329360961914,189.7539672851562,189.7539672851562,189.9900054931641,189.9900054931641,189.9900054931641,190.2274703979492,190.4647750854492,190.7028350830078,190.9474487304688,190.9934005737305,190.9934005737305,190.9934005737305,189.2297210693359,189.4076538085938,189.6104507446289,189.6104507446289,189.8347625732422,190.0737609863281,190.3146896362305,190.3146896362305,190.5548934936523,190.5548934936523,190.7963409423828,190.7963409423828,191.0412673950195,191.0412673950195,191.045166015625,191.045166015625,191.045166015625,191.045166015625,189.3495254516602,189.5398941040039,189.5398941040039,189.7464065551758,189.7464065551758,189.9748916625977,189.9748916625977,190.215461730957,190.215461730957,190.215461730957,190.4563751220703,190.4563751220703,190.6971130371094,190.6971130371094,190.9411010742188,191.0960388183594,191.0960388183594,191.0960388183594,191.0960388183594,189.5180358886719,189.5180358886719,189.7164916992188,189.7164916992188,189.9339447021484,189.9339447021484,190.1717300415039,190.1717300415039,190.4125900268555,190.4125900268555,190.6554489135742,190.6554489135742,190.8949966430664,190.8949966430664,190.8949966430664,191.1380844116211,191.1461410522461,191.1461410522461,191.1461410522461,189.5022277832031,189.5022277832031,189.6921157836914,189.6921157836914,189.9001846313477,189.9001846313477,190.1234130859375,190.1234130859375,190.1234130859375,190.3437881469727,190.3437881469727,190.5840377807617,190.5840377807617,190.5840377807617,190.8237380981445,190.8237380981445,191.0597686767578,191.0597686767578,191.1953964233398,191.1953964233398,191.1953964233398,191.1953964233398,191.1953964233398,191.1953964233398,189.6499557495117,189.6499557495117,189.8403244018555,189.8403244018555,190.0516357421875,190.0516357421875,190.2870864868164,190.2870864868164,190.5278701782227,190.5278701782227,190.794059753418,190.794059753418,191.0328598022461,191.0328598022461,191.2438507080078,191.2438507080078,191.2438507080078,191.2438507080078,189.6774673461914,189.6774673461914,189.8675308227539,189.8675308227539,190.0772552490234,190.0772552490234,190.3083038330078,190.3083038330078,190.5494613647461,190.7906875610352,190.7906875610352,191.0308990478516,191.0308990478516,191.2732543945312,191.2732543945312,191.2732543945312,191.2915496826172,191.2915496826172,189.7067718505859,189.7067718505859,189.8820877075195,189.8820877075195,190.0861663818359,190.0861663818359,190.3131103515625,190.5548477172852,190.7957992553711,190.7957992553711,190.7957992553711,191.0363693237305,191.0363693237305,191.2727890014648,191.3385238647461,191.3385238647461,189.7413787841797,189.7413787841797,189.9241333007812,190.1166839599609,190.1166839599609,190.3318176269531,190.5920715332031,190.5920715332031,190.5920715332031,190.8308868408203,190.8308868408203,191.0699310302734,191.0699310302734,191.3076553344727,191.3076553344727,191.3846740722656,191.3846740722656,191.3846740722656,191.3846740722656,191.3846740722656,191.3846740722656,191.3846740722656,191.3846740722656,191.3846740722656,191.3846740722656,191.3846740722656,191.3846740722656,191.3846740722656,191.3846740722656,191.3846740722656,191.3846740722656,191.3846740722656,191.3846740722656,191.3846740722656,191.3846740722656,191.3846740722656,191.3846740722656,191.3846740722656,191.3846740722656,191.3846740722656,191.3846740722656,191.3846740722656,191.3846740722656,191.3846740722656,191.3846740722656,191.3846740722656,191.3846740722656,191.3846740722656,191.3846740722656,191.3846740722656,191.3846740722656,191.3846740722656,191.3846740722656,191.3846740722656,191.3846740722656,191.3846740722656,191.3846740722656,191.3846740722656,191.3846740722656,191.3846740722656,191.3846740722656,191.3846740722656,191.3846740722656,191.3846740722656,191.3846740722656,191.3846740722656,191.3846740722656,191.3846740722656,191.3846740722656,191.3846740722656,191.3846740722656,191.3846740722656,191.3846740722656,191.3846740722656,191.3846740722656,189.7949676513672,189.7949676513672,189.8025283813477,189.8025283813477,189.9945068359375,189.9945068359375,189.9945068359375,190.195930480957,190.195930480957,190.4344024658203,190.6673278808594,190.9045028686523,191.1292877197266,191.1292877197266,191.3467483520508,191.3467483520508,191.5857009887695,191.5857009887695,191.83154296875,192.0765075683594,192.3147048950195,192.552978515625,192.552978515625,192.7570037841797,192.7570037841797,192.955322265625,192.955322265625,192.955322265625,193.1529541015625,193.3511657714844,193.5491561889648,193.5491561889648,193.7466888427734,193.9446258544922,194.1420593261719,194.1420593261719,194.3403472900391,194.3403472900391,194.3403472900391,194.5375747680664,194.5375747680664,194.6348037719727,194.6348037719727,194.6348037719727,194.6348037719727,194.6348037719727,194.6348037719727,190.1561965942383,190.1561965942383,190.3771743774414,190.6175079345703,190.6175079345703,190.8602600097656,191.0930709838867,191.0930709838867,191.3121109008789,191.5457763671875,191.816535949707,192.068244934082,192.3175201416016,192.56494140625,192.56494140625,192.8127822875977,193.0610809326172,193.3086776733398,193.3086776733398,193.5556793212891,193.8029251098633,194.0498962402344,194.2969055175781,194.2969055175781,194.5366592407227,194.767219543457,194.767219543457,194.767219543457,194.767219543457,194.767219543457,194.767219543457,190.2520446777344,190.2520446777344,190.4592590332031,190.4592590332031,190.6847457885742,190.6847457885742,190.92626953125,191.1612319946289,191.3819274902344,191.3819274902344,191.6141357421875,191.8576583862305,191.8576583862305,192.1084518432617,192.3599319458008,192.6060333251953,192.6060333251953,192.8518905639648,192.8518905639648,193.0980834960938,193.0980834960938,193.3434066772461,193.3434066772461,193.5879516601562,193.8321151733398,193.8321151733398,193.8321151733398,194.0772247314453,194.0772247314453,194.3462524414062,194.3462524414062,194.5889129638672,194.5889129638672,194.8240509033203,194.8240509033203,194.8974380493164,194.8974380493164,194.8974380493164,194.8974380493164,194.8974380493164,194.8974380493164,190.5545043945312,190.7629241943359,190.7629241943359,190.9976959228516,190.9976959228516,191.2351379394531,191.2351379394531,191.4577789306641,191.4577789306641,191.6867752075195,191.9308776855469,191.9308776855469,192.1728820800781,192.1728820800781,192.424186706543,192.424186706543,192.6742095947266,192.6742095947266,192.6742095947266,192.9221801757812,192.9221801757812,193.1697235107422,193.1697235107422,193.4166870117188,193.6596908569336,193.6596908569336,193.6596908569336,193.9036331176758,194.1477203369141,194.3922653198242,194.6370544433594,194.6370544433594,194.8727416992188,194.8727416992188,195.0255737304688,195.0255737304688,195.0255737304688,195.0255737304688,195.0255737304688,195.0255737304688,190.7069244384766,190.938850402832,190.938850402832,191.1682510375977,191.3988189697266,191.3988189697266,191.6156692504883,191.6156692504883,191.6156692504883,191.8520812988281,192.094123840332,192.338493347168,192.338493347168,192.5895538330078,192.5895538330078,192.8386077880859,193.0842208862305,193.0842208862305,193.3302230834961,193.3302230834961,193.5759582519531,193.8199768066406,193.8199768066406,194.06494140625,194.3110275268555,194.5569763183594,194.8033447265625,194.8033447265625,195.0376052856445,195.0376052856445,195.1516647338867,195.1516647338867,195.1516647338867,195.1516647338867,190.9283447265625,190.9283447265625,191.1352767944336,191.3570404052734,191.3570404052734,191.3570404052734,191.5813369750977,191.5813369750977,191.8002166748047,192.0423126220703,192.2842483520508,192.2842483520508,192.5324249267578,192.7832946777344,192.7832946777344,193.0573272705078,193.3041076660156,193.3041076660156,193.5497589111328,193.5497589111328,193.7954483032227,193.7954483032227,194.0403900146484,194.0403900146484,194.2864761352539,194.5336685180664,194.5336685180664,194.7726669311523,194.7726669311523,195.009033203125,195.009033203125,195.2427978515625,195.2427978515625,195.2756271362305,195.2756271362305,195.2756271362305,195.2756271362305,195.2756271362305,195.2756271362305,191.1848678588867,191.3902816772461,191.3902816772461,191.602912902832,191.8153533935547,192.0504379272461,192.0504379272461,192.2915649414062,192.2915649414062,192.2915649414062,192.5338821411133,192.5338821411133,192.5338821411133,192.779914855957,192.779914855957,193.0309829711914,193.0309829711914,193.2786331176758,193.2786331176758,193.5239639282227,193.7688751220703,193.7688751220703,194.0145263671875,194.0145263671875,194.2600402832031,194.2600402832031,194.5060806274414,194.5060806274414,194.7527542114258,194.7527542114258,194.9996948242188,194.9996948242188,195.2609558105469,195.2609558105469,195.2609558105469,195.3976974487305,195.3976974487305,195.3976974487305,195.3976974487305,191.293701171875,191.293701171875,191.4972686767578,191.4972686767578,191.7094650268555,191.7094650268555,191.9197998046875,191.9197998046875,192.1533584594727,192.1533584594727,192.3939361572266,192.637092590332,192.881233215332,192.881233215332,193.1322326660156,193.1322326660156,193.3823928833008,193.3823928833008,193.6277084350586,193.6277084350586,193.8728637695312,193.8728637695312,194.116828918457,194.3615493774414,194.6060028076172,194.6060028076172,194.8509674072266,194.8509674072266,195.0966873168945,195.335090637207,195.335090637207,195.5177764892578,195.5177764892578,195.5177764892578,195.5177764892578,195.5177764892578,195.5177764892578,191.4396667480469,191.4396667480469,191.6413040161133,191.6413040161133,191.8485260009766,192.0538558959961,192.0538558959961,192.3095703125,192.5495758056641,192.5495758056641,192.5495758056641,192.7922744750977,192.7922744750977,193.0351333618164,193.0351333618164,193.0351333618164,193.2853469848633,193.2853469848633,193.2853469848633,193.5352020263672,193.7808837890625,193.7808837890625,194.0270614624023,194.2738189697266,194.2738189697266,194.2738189697266,194.5203475952148,194.5203475952148,194.7668685913086,194.7668685913086,195.0144882202148,195.0144882202148,195.0144882202148,195.2611389160156,195.4981460571289,195.6358489990234,195.6358489990234,195.6358489990234,195.6358489990234,195.6358489990234,195.6358489990234,191.6594009399414,191.6594009399414,191.8592834472656,191.8592834472656,192.0624694824219,192.0624694824219,192.2693786621094,192.2693786621094,192.5052642822266,192.7445449829102,192.7445449829102,192.9839401245117,192.9839401245117,193.2234191894531,193.2234191894531,193.4699630737305,193.4699630737305,193.7171020507812,193.7171020507812,193.9607238769531,194.2041702270508,194.2041702270508,194.4487686157227,194.4487686157227,194.7171249389648,194.7171249389648,194.9617538452148,194.9617538452148,195.20654296875,195.4496841430664,195.6844711303711,195.752067565918,195.752067565918,195.752067565918,195.752067565918,195.752067565918,195.752067565918,191.8924789428711,191.8924789428711,192.0895462036133,192.0895462036133,192.0895462036133,192.2878799438477,192.5078659057617,192.5078659057617,192.7474060058594,192.7474060058594,192.9876861572266,193.2287826538086,193.4704666137695,193.7174377441406,193.7174377441406,193.9646759033203,193.9646759033203,194.2079315185547,194.2079315185547,194.4523468017578,194.4523468017578,194.6969223022461,194.9411849975586,194.9411849975586,195.1854629516602,195.1854629516602,195.4307174682617,195.6705322265625,195.6705322265625,195.8663864135742,195.8663864135742,195.8663864135742,195.8663864135742,191.9600067138672,191.9600067138672,192.1739883422852,192.3655471801758,192.3655471801758,192.5729598999023,192.5729598999023,192.8058395385742,192.8058395385742,193.043571472168,193.043571472168,193.2816925048828,193.2816925048828,193.5187606811523,193.7597122192383,193.7597122192383,194.0073013305664,194.0073013305664,194.2499694824219,194.4919738769531,194.4919738769531,194.7348785400391,194.9790954589844,194.9790954589844,194.9790954589844,195.2227096557617,195.4663696289062,195.4663696289062,195.7080001831055,195.9426116943359,195.9426116943359,195.9789352416992,195.9789352416992,195.9789352416992,195.9789352416992,192.2678985595703,192.2678985595703,192.4574127197266,192.4574127197266,192.6574783325195,192.6574783325195,192.6574783325195,192.8842239379883,193.1212921142578,193.3585968017578,193.5960998535156,193.5960998535156,193.8356552124023,194.0782699584961,194.3228988647461,194.3228988647461,194.5642318725586,194.8302154541016,194.8302154541016,194.8302154541016,195.0734710693359,195.3164291381836,195.3164291381836,195.5582580566406,195.5582580566406,195.8016204833984,195.8016204833984,196.0354309082031,196.0895767211914,196.0895767211914,196.0895767211914,196.0895767211914,196.0895767211914,196.0895767211914,192.4212341308594,192.4212341308594,192.6083450317383,192.8082046508789,192.8082046508789,193.033821105957,193.033821105957,193.2677154541016,193.2677154541016,193.5018615722656,193.5018615722656,193.7372894287109,193.7372894287109,193.9798202514648,193.9798202514648,194.2270431518555,194.4738006591797,194.4738006591797,194.7138824462891,194.7138824462891,194.9570465087891,194.9570465087891,194.9570465087891,195.2009506225586,195.2009506225586,195.4452209472656,195.4452209472656,195.4452209472656,195.6882476806641,195.6882476806641,195.9309387207031,195.9309387207031,195.9309387207031,196.1648406982422,196.1648406982422,196.1985168457031,196.1985168457031,196.1985168457031,196.1985168457031,192.603889465332,192.603889465332,192.7890701293945,192.7890701293945,192.9917373657227,192.9917373657227,193.2117462158203,193.2117462158203,193.2117462158203,193.4439468383789,193.4439468383789,193.6235809326172,193.6235809326172,193.8561401367188,194.0902252197266,194.3295745849609,194.5652389526367,194.8037643432617,195.0401382446289,195.2774276733398,195.2774276733398,195.516487121582,195.516487121582,195.7629699707031,195.7629699707031,196.0100402832031,196.2455444335938,196.2455444335938,196.3056106567383,196.3056106567383,196.3056106567383,196.3056106567383,192.7479705810547,192.9340286254883,192.9340286254883,193.1365280151367,193.1365280151367,193.357666015625,193.357666015625,193.6148986816406,193.6148986816406,193.6148986816406,193.8507843017578,194.0917129516602,194.3332748413086,194.3332748413086,194.5756072998047,194.816535949707,194.816535949707,195.0539703369141,195.0539703369141,195.291618347168,195.291618347168,195.5295333862305,195.5295333862305,195.7676315307617,195.7676315307617,196.0055618286133,196.0055618286133,196.2377166748047,196.2377166748047,196.4111022949219,196.4111022949219,196.4111022949219,196.4111022949219,196.4111022949219,196.4111022949219,192.7911224365234,192.9747772216797,192.9747772216797,193.1597290039062,193.3592681884766,193.3592681884766,193.3592681884766,193.5712203979492,193.5712203979492,193.7942504882812,193.7942504882812,194.0264282226562,194.0264282226562,194.2671585083008,194.2671585083008,194.509162902832,194.509162902832,194.7506561279297,194.7506561279297,194.9917144775391,194.9917144775391,195.2285919189453,195.2285919189453,195.4672546386719,195.4672546386719,195.7306289672852,195.7306289672852,195.9691162109375,195.9691162109375,196.2070465087891,196.4346542358398,196.4346542358398,196.5147323608398,196.5147323608398,196.5147323608398,196.5147323608398,193.0398483276367,193.2206344604492,193.2206344604492,193.4121322631836,193.4121322631836,193.613525390625,193.613525390625,193.8273086547852,194.0539703369141,194.0539703369141,194.2936553955078,194.2936553955078,194.5351333618164,194.5351333618164,194.5351333618164,194.7755126953125,195.0182495117188,195.0182495117188,195.2573776245117,195.2573776245117,195.4951782226562,195.4951782226562,195.4951782226562,195.7342071533203,195.9734954833984,195.9734954833984,196.2099304199219,196.4390258789062,196.4390258789062,196.6168060302734,196.6168060302734,196.6168060302734,196.6168060302734,196.6168060302734,196.6168060302734,193.1301116943359,193.1301116943359,193.3102111816406,193.3102111816406,193.4952239990234,193.6930694580078,193.6930694580078,193.9015045166016,193.9015045166016,194.1233215332031,194.1233215332031,194.3589935302734,194.3589935302734,194.5974426269531,194.8606948852539,194.8606948852539,195.1014785766602,195.3387222290039,195.3387222290039,195.5778274536133,195.8212127685547,195.8212127685547,196.0646667480469,196.0646667480469,196.3046493530273,196.3046493530273,196.5366439819336,196.5366439819336,196.7172088623047,196.7172088623047,196.7172088623047,196.7172088623047,196.7172088623047,196.7172088623047,193.2947463989258,193.4737319946289,193.6597366333008,193.6597366333008,193.8545837402344,193.8545837402344,194.0605239868164,194.2802963256836,194.5171356201172,194.5171356201172,194.5171356201172,194.755126953125,194.9937591552734,194.9937591552734,195.2323913574219,195.2323913574219,195.4706497192383,195.7050857543945,195.7050857543945,195.9398727416992,195.9398727416992,196.1999588012695,196.1999588012695,196.1999588012695,196.4364700317383,196.4364700317383,196.6651306152344,196.6651306152344,196.8159103393555,196.8159103393555,196.8159103393555,196.8159103393555,196.8159103393555,196.8159103393555,193.4465103149414,193.6240386962891,193.6240386962891,193.8102264404297,193.8102264404297,194.0022430419922,194.2041473388672,194.2041473388672,194.4431762695312,194.4431762695312,194.6779479980469,194.6779479980469,194.9169998168945,195.1536636352539,195.1536636352539,195.3890151977539,195.3890151977539,195.6256790161133,195.6256790161133,195.8596115112305,195.8596115112305,196.0940933227539,196.3271865844727,196.5605087280273,196.7878570556641,196.9131622314453,196.9131622314453,196.9131622314453,196.9131622314453,196.9131622314453,196.9131622314453,196.9131622314453,196.9131622314453,196.9131622314453,196.9131622314453,196.9131622314453,196.9131622314453,196.9131622314453,196.9131622314453,196.9131622314453,196.9131622314453,196.9131622314453,196.9131622314453,196.9131622314453,196.9131622314453,196.9131622314453,196.9131622314453,196.9131622314453,196.9131622314453,196.9131622314453,196.9131622314453,196.9131622314453,196.9131622314453,196.9131622314453,196.9131622314453,196.9131622314453,196.9131622314453,196.9131622314453,196.9131622314453,196.9131622314453,196.9131622314453,196.9131622314453,196.9131622314453,196.9131622314453,196.9131622314453,196.9131622314453,196.9131622314453,196.9131622314453,196.9131622314453,196.9131622314453,196.9131622314453,196.9131622314453,196.9131622314453,193.5685195922852,193.5685195922852,193.5685195922852,193.595703125,193.595703125,193.7473831176758,193.9187545776367,193.9187545776367,194.1024780273438,194.2911529541016,194.2911529541016,194.4937896728516,194.4937896728516,194.7339706420898,194.9700469970703,194.9700469970703,195.1976852416992,195.1976852416992,195.4219055175781,195.4219055175781,195.4219055175781,195.649299621582,195.649299621582,195.8791885375977,195.8791885375977,196.1173248291016,196.1173248291016,196.357536315918,196.357536315918,196.5960083007812,196.5960083007812,196.8341293334961,196.8341293334961,197.0085372924805,197.0085372924805,197.0085372924805,197.0085372924805,197.0085372924805,197.0085372924805,193.7336502075195,193.7336502075195,193.9103240966797,193.9103240966797,194.0947418212891,194.0947418212891,194.2846069335938,194.2846069335938,194.486457824707,194.701530456543,194.701530456543,194.9342727661133,195.1697158813477,195.1697158813477,195.1697158813477,195.4262390136719,195.4262390136719,195.6593475341797,195.8924942016602,195.8924942016602,196.1262130737305,196.3608245849609,196.3608245849609,196.5968399047852,196.5968399047852,196.8334503173828,196.8334503173828,197.0762710571289,197.0762710571289,197.0762710571289,197.1026000976562,197.1026000976562,197.1026000976562,197.1026000976562,197.1026000976562,197.1026000976562,197.1026000976562,197.1026000976562,193.9887619018555,193.9887619018555,194.169807434082,194.3556365966797,194.5546646118164,194.5546646118164,194.5546646118164,194.7667770385742,194.7667770385742,194.9946060180664,194.9946060180664,195.2292022705078,195.2292022705078,195.4666213989258,195.4666213989258,195.7018890380859,195.7018890380859,195.9333419799805,195.9333419799805,196.1686553955078,196.1686553955078,196.4048690795898,196.4048690795898,196.6470336914062,196.6470336914062,196.6470336914062,196.88818359375,197.1294250488281,197.1294250488281,197.1952133178711,197.1952133178711,197.1952133178711,197.1952133178711,197.1952133178711,197.1952133178711,194.132194519043,194.132194519043,194.31298828125,194.31298828125,194.5019454956055,194.5019454956055,194.5019454956055,194.7072296142578,194.7072296142578,194.9257659912109,195.1585922241211,195.1585922241211,195.3942947387695,195.6288299560547,195.6288299560547,195.8631591796875,196.0968780517578,196.0968780517578,196.3300323486328,196.3300323486328,196.5640716552734,196.8030090332031,196.8030090332031,197.0495071411133,197.0495071411133,197.286262512207,197.286262512207,197.286262512207,197.286262512207,197.286262512207,197.286262512207,197.286262512207,197.286262512207,197.286262512207,194.3103790283203,194.4924850463867,194.4924850463867,194.6833801269531,194.6833801269531,194.8895492553711,194.8895492553711,195.1127548217773,195.1127548217773,195.3481597900391,195.5849990844727,195.5849990844727,195.5849990844727,195.8197479248047,196.0535202026367,196.0535202026367,196.3117370605469,196.5477523803711,196.7883987426758,196.7883987426758,197.0350952148438,197.0350952148438,197.28076171875,197.3758850097656,197.3758850097656,197.3758850097656,197.3758850097656,197.3758850097656,197.3758850097656,194.3692092895508,194.3692092895508,194.5504379272461,194.5504379272461,194.5504379272461,194.7369613647461,194.7369613647461,194.9384613037109,194.9384613037109,195.1539306640625,195.1539306640625,195.3839416503906,195.3839416503906,195.619255065918,195.619255065918,195.8486633300781,196.0784606933594,196.0784606933594,196.3113708496094,196.3113708496094,196.5452651977539,196.5452651977539,196.7816162109375,196.7816162109375,197.0191879272461,197.2570266723633,197.2570266723633,197.4640350341797,197.4640350341797,197.4640350341797,197.4640350341797,197.4640350341797,197.4640350341797,197.4640350341797,197.4640350341797,197.4640350341797,194.6010055541992,194.6010055541992,194.6010055541992,194.8022537231445,194.8022537231445,194.9984512329102,194.9984512329102,195.2102355957031,195.2102355957031,195.4392318725586,195.6780548095703,195.6780548095703,195.9169158935547,195.9169158935547,196.1534423828125,196.1534423828125,196.1534423828125,196.3896560668945,196.3896560668945,196.6261520385742,196.8639907836914,197.1057434082031,197.1057434082031,197.3491821289062,197.5507507324219,197.5507507324219,197.5507507324219,197.5507507324219,197.5507507324219,197.5507507324219,197.5507507324219,197.5507507324219,197.5507507324219,194.7403945922852,194.7403945922852,194.9222030639648,194.9222030639648,195.1169815063477,195.1169815063477,195.326904296875,195.326904296875,195.5538024902344,195.7929153442383,195.7929153442383,196.0306701660156,196.0306701660156,196.2663497924805,196.2663497924805,196.5030517578125,196.5030517578125,196.7385406494141,196.7385406494141,196.9735717773438,197.2118148803711,197.2118148803711,197.4743118286133,197.636116027832,197.636116027832,197.636116027832,197.636116027832,197.636116027832,197.636116027832,194.7182312011719,194.8964614868164,195.0788879394531,195.0788879394531,195.2740173339844,195.4865875244141,195.4865875244141,195.7150192260742,195.7150192260742,195.9531555175781,195.9531555175781,196.1928787231445,196.1928787231445,196.4282989501953,196.4282989501953,196.664176940918,196.664176940918,196.664176940918,196.8987503051758,196.8987503051758,197.1356811523438,197.1356811523438,197.376091003418,197.376091003418,197.6134872436523,197.6134872436523,197.7200164794922,197.7200164794922,197.7200164794922,197.7200164794922,197.7200164794922,197.7200164794922,197.7200164794922,197.7200164794922,194.8906021118164,195.0705947875977,195.0705947875977,195.2546920776367,195.2546920776367,195.4552154541016,195.4552154541016,195.669319152832,195.669319152832,195.9236297607422,196.1604537963867,196.3945541381836,196.3945541381836,196.6274490356445,196.6274490356445,196.8610305786133,197.0980224609375,197.3362197875977,197.5816802978516,197.5816802978516,197.8026275634766,197.8026275634766,197.8026275634766,197.8026275634766,197.8026275634766,197.8026275634766,195.1223526000977,195.1223526000977,195.3036727905273,195.4946975708008,195.4946975708008,195.7033996582031,195.7033996582031,195.9306182861328,195.9306182861328,196.1675186157227,196.1675186157227,196.4052658081055,196.4052658081055,196.640625,196.8757553100586,196.8757553100586,197.1133499145508,197.1133499145508,197.356689453125,197.356689453125,197.6025772094727,197.6025772094727,197.8487243652344,197.8487243652344,197.8838729858398,197.8838729858398,197.8838729858398,197.8838729858398,195.218635559082,195.3994750976562,195.3994750976562,195.5898208618164,195.7959289550781,196.0225219726562,196.2596664428711,196.2596664428711,196.4984664916992,196.4984664916992,196.7353591918945,196.9717254638672,196.9717254638672,197.2102355957031,197.2102355957031,197.4567413330078,197.7050399780273,197.7050399780273,197.9514465332031,197.9514465332031,197.9638824462891,197.9638824462891,197.9638824462891,197.9638824462891,197.9638824462891,197.9638824462891,195.3438110351562,195.3438110351562,195.5247039794922,195.5247039794922,195.7129821777344,195.7129821777344,195.91943359375,196.1418533325195,196.1418533325195,196.378173828125,196.378173828125,196.6159820556641,196.6159820556641,196.8524856567383,197.0879898071289,197.0879898071289,197.3222351074219,197.5568466186523,197.5568466186523,197.7976684570312,197.7976684570312,198.0424652099609,198.0424652099609,198.0424652099609,198.0424652099609,198.0424652099609,198.0424652099609,195.4844512939453,195.4844512939453,195.6652221679688,195.6652221679688,195.8560485839844,196.0652847290039,196.0652847290039,196.2921524047852,196.5291213989258,196.7675857543945,196.7675857543945,197.0034255981445,197.2392120361328,197.2392120361328,197.475830078125,197.7160415649414,197.9637603759766,197.9637603759766,198.1199264526367,198.1199264526367,198.1199264526367,198.1199264526367,198.1199264526367,198.1199264526367,195.4732131958008,195.6498718261719,195.6498718261719,195.8325347900391,195.8325347900391,196.0287704467773,196.0287704467773,196.2438354492188,196.4703750610352,196.4703750610352,196.7083511352539,196.7083511352539,196.7083511352539,196.9461364746094,196.9461364746094,197.1791458129883,197.1791458129883,197.4121932983398,197.4121932983398,197.668701171875,197.668701171875,197.9040145874023,197.9040145874023,198.1477966308594,198.1477966308594,198.1960296630859,198.1960296630859,198.1960296630859,198.1960296630859,198.1960296630859,198.1960296630859,195.6667709350586,195.8464050292969,195.8464050292969,196.031364440918,196.031364440918,196.2333145141602,196.453727722168,196.453727722168,196.6889190673828,196.9273376464844,196.9273376464844,197.1635131835938,197.1635131835938,197.3983688354492,197.3983688354492,197.6306457519531,197.6306457519531,197.8691024780273,197.8691024780273,198.1095199584961,198.1095199584961,198.2709579467773,198.2709579467773,198.2709579467773,198.2709579467773,198.2709579467773,198.2709579467773,195.703727722168,195.8803024291992,195.8803024291992,196.0635528564453,196.2600173950195,196.2600173950195,196.475227355957,196.729606628418,196.729606628418,196.970344543457,196.970344543457,197.209342956543,197.209342956543,197.4448623657227,197.4448623657227,197.4448623657227,197.6810913085938,197.9189834594727,197.9189834594727,198.1577911376953,198.1577911376953,198.3446731567383,198.3446731567383,198.3446731567383,198.3446731567383,198.3446731567383,198.3446731567383,198.3446731567383,198.3446731567383,198.3446731567383,195.9751052856445,195.9751052856445,196.1571350097656,196.1571350097656,196.3497467041016,196.3497467041016,196.5598373413086,196.5598373413086,196.7904281616211,196.7904281616211,197.0304718017578,197.0304718017578,197.2678756713867,197.2678756713867,197.5029754638672,197.7380065917969,197.7380065917969,197.9725646972656,197.9725646972656,198.2087707519531,198.2087707519531,198.4171752929688,198.4171752929688,198.4171752929688,198.4171752929688,198.4171752929688,198.4171752929688,196.0663986206055,196.2667846679688,196.2667846679688,196.4592208862305,196.4592208862305,196.6723098754883,196.6723098754883,196.9028244018555,197.1411590576172,197.1411590576172,197.1411590576172,197.3809967041016,197.3809967041016,197.6177139282227,197.6177139282227,197.8537979125977,198.0859069824219,198.0859069824219,198.3211975097656,198.3211975097656,198.4885482788086,198.4885482788086,198.4885482788086,198.4885482788086,198.4885482788086,198.4885482788086,196.1992416381836,196.1992416381836,196.3828125,196.3828125,196.3828125,196.5756759643555,196.5756759643555,196.7848052978516,197.0153961181641,197.0153961181641,197.2573623657227,197.4988861083984,197.7385177612305,197.9770050048828,197.9770050048828,198.218620300293,198.218620300293,198.4599533081055,198.4599533081055,198.5587615966797,198.5587615966797,198.5587615966797,198.5587615966797,196.2107162475586,196.2107162475586,196.3935165405273,196.3935165405273,196.5805587768555,196.5805587768555,196.7841110229492,196.7841110229492,197.008544921875,197.008544921875,197.248420715332,197.248420715332,197.4907531738281,197.7319259643555,197.9705657958984,197.9705657958984,198.2089920043945,198.2089920043945,198.4497909545898,198.4497909545898,198.6278762817383,198.6278762817383,198.6278762817383,198.6278762817383,198.6278762817383,198.6278762817383,198.6278762817383,198.6278762817383,198.6278762817383,198.6278762817383,198.6278762817383,198.6278762817383,198.6278762817383,198.6278762817383,198.6278762817383,198.6278762817383,198.6278762817383,198.6278762817383,198.6278762817383,198.6278762817383,198.6278762817383,198.6278762817383,198.6278762817383,198.6278762817383,198.6278762817383,198.6278762817383,198.6278762817383,198.6278762817383,198.6278762817383,198.6278762817383,198.6278762817383,198.6278762817383,198.6278762817383,198.6278762817383,198.6278762817383,198.6278762817383,196.2521667480469,196.3966522216797,196.3966522216797,196.5648651123047,196.7475967407227,196.7475967407227,196.9409332275391,196.9409332275391,196.9409332275391,197.153434753418,197.153434753418,197.153434753418,197.3797760009766,197.3797760009766,197.6197204589844,197.8582992553711,197.8582992553711,198.0946655273438,198.3307495117188,198.3307495117188,198.5700836181641,198.5700836181641,198.6955184936523,198.6955184936523,198.6955184936523,198.6955184936523,198.6955184936523,198.6955184936523,196.3853149414062,196.5637359619141,196.5637359619141,196.7476577758789,196.7476577758789,196.9480209350586,196.9480209350586,197.1682205200195,197.1682205200195,197.4038848876953,197.6237564086914,197.8785705566406,197.8785705566406,197.8785705566406,198.1137542724609,198.3511657714844,198.3511657714844,198.5889053344727,198.5889053344727,198.5889053344727,198.7624206542969,198.7624206542969,198.7624206542969,198.7624206542969,198.7624206542969,198.7624206542969,198.7624206542969,198.7624206542969,198.7624206542969,196.6245574951172,196.6245574951172,196.6245574951172,196.8062286376953,196.9988784790039,197.2146453857422,197.2146453857422,197.4473419189453,197.4473419189453,197.6863403320312,197.6863403320312,197.9256896972656,197.9256896972656,198.1627426147461,198.3997650146484,198.643440246582,198.8281631469727,198.8281631469727,198.8281631469727,198.8281631469727,198.8281631469727,198.8281631469727,198.8281631469727,198.8281631469727,198.8281631469727,196.7243957519531,196.9068450927734,196.9068450927734,197.1011047363281,197.1011047363281,197.3376159667969,197.3376159667969,197.57177734375,197.8115768432617,198.0511703491211,198.2877731323242,198.5265197753906,198.5265197753906,198.7688674926758,198.8929138183594,198.8929138183594,198.8929138183594,198.8929138183594,198.8929138183594,198.8929138183594,196.6899642944336,196.6899642944336,196.8645629882812,196.8645629882812,197.0485305786133,197.0485305786133,197.2434921264648,197.4617080688477,197.4617080688477,197.694953918457,197.694953918457,197.9360198974609,197.9360198974609,198.175895690918,198.175895690918,198.4133148193359,198.4133148193359,198.6512756347656,198.6512756347656,198.8899307250977,198.8899307250977,198.9566116333008,198.9566116333008,198.9566116333008,198.9566116333008,198.9566116333008,198.9566116333008,196.829719543457,196.829719543457,197.0099258422852,197.0099258422852,197.2157440185547,197.2157440185547,197.4236831665039,197.6511001586914,197.6511001586914,197.8909912109375,197.8909912109375,198.1317520141602,198.1317520141602,198.3706130981445,198.3706130981445,198.6072692871094,198.6072692871094,198.8449020385742,198.8449020385742,199.019287109375,199.019287109375,199.019287109375,199.019287109375,199.019287109375,199.019287109375,199.019287109375,199.019287109375,199.019287109375,197.0275192260742,197.2099609375,197.2099609375,197.406005859375,197.406005859375,197.6225051879883,197.6225051879883,197.8542938232422,197.8542938232422,198.0927658081055,198.0927658081055,198.331413269043,198.331413269043,198.5676193237305,198.5676193237305,198.8029403686523,198.8029403686523,198.8029403686523,199.039306640625,199.039306640625,199.039306640625,199.0808868408203,199.0808868408203,199.0808868408203,199.0808868408203,199.0808868408203,199.0808868408203,197.0416259765625,197.0416259765625,197.2192687988281,197.2192687988281,197.4236602783203,197.4236602783203,197.6278915405273,197.6278915405273,197.8548355102539,197.8548355102539,198.0917205810547,198.0917205810547,198.3310394287109,198.3310394287109,198.5665817260742,198.8002700805664,198.8002700805664,198.8002700805664,199.0380783081055,199.0380783081055,199.1415634155273,199.1415634155273,199.1415634155273,199.1415634155273,199.1415634155273,199.1415634155273,197.0923767089844,197.0923767089844,197.2715148925781,197.2715148925781,197.4573440551758,197.4573440551758,197.6628799438477,197.8872604370117,197.8872604370117,198.1268310546875,198.1268310546875,198.3692779541016,198.3692779541016,198.6092834472656,198.8465728759766,198.8465728759766,199.0868148803711,199.0868148803711,199.2012252807617,199.2012252807617,199.2012252807617,199.2012252807617,199.2012252807617,199.2012252807617,197.1786117553711,197.3740463256836,197.3740463256836,197.5604019165039,197.5604019165039,197.5604019165039,197.7629318237305,197.7629318237305,197.9847030639648,197.9847030639648,198.2224960327148,198.2224960327148,198.4655532836914,198.7059555053711,198.9438781738281,198.9438781738281,199.1828308105469,199.1828308105469,199.2599029541016,199.2599029541016,199.2599029541016,199.2599029541016,199.2599029541016,199.2599029541016,197.2890090942383,197.4644546508789,197.6483993530273,197.6483993530273,197.8487777709961,197.8487777709961,198.0695953369141,198.3059616088867,198.5462951660156,198.784309387207,199.0185699462891,199.2548675537109,199.3177032470703,199.3177032470703,199.3177032470703,199.3177032470703,199.3177032470703,199.3177032470703,197.3942184448242,197.3942184448242,197.5907135009766,197.776496887207,197.9817352294922,197.9817352294922,198.2063522338867,198.4444198608398,198.4444198608398,198.6841735839844,198.9215240478516,198.9215240478516,199.1567306518555,199.1567306518555,199.3744659423828,199.3744659423828,199.3744659423828,199.3744659423828,199.3744659423828,199.3744659423828,199.3744659423828,199.3744659423828,199.3744659423828,199.3744659423828,199.3744659423828,199.3744659423828,197.5373458862305,197.5373458862305,197.7175674438477,197.7175674438477,197.7175674438477,197.90771484375,198.1181564331055,198.1181564331055,198.3492965698242,198.3492965698242,198.5883255004883,198.5883255004883,198.8285064697266,198.8285064697266,198.8285064697266,199.0630950927734,199.0630950927734,199.2871780395508,199.2871780395508,199.4303894042969,199.4303894042969,199.4303894042969,199.4303894042969,199.4303894042969,199.4303894042969,199.4303894042969,199.4303894042969,199.4303894042969,197.6789398193359,197.6789398193359,197.8609390258789,198.0556488037109,198.0556488037109,198.2703247070312,198.5050430297852,198.5050430297852,198.746337890625,198.746337890625,198.9874267578125,199.2256164550781,199.2256164550781,199.4586334228516,199.4586334228516,199.4854278564453,199.4854278564453,199.4854278564453,199.4854278564453,197.6787109375,197.6787109375,197.8572082519531,197.8572082519531,198.045295715332,198.045295715332,198.25341796875,198.25341796875,198.479248046875,198.479248046875,198.7195281982422,198.9609832763672,199.2013320922852,199.2013320922852,199.4366302490234,199.5394821166992,199.5394821166992,199.5394821166992,199.5394821166992,199.5394821166992,199.5394821166992,199.5394821166992,199.5394821166992,199.5394821166992,199.5394821166992,199.5394821166992,199.5394821166992,199.5394821166992,199.5394821166992,199.5394821166992,199.5394821166992,199.5394821166992,199.5394821166992,199.5394821166992,199.5394821166992,199.5394821166992,197.6766891479492,197.6766891479492,197.6766891479492,197.8176040649414,197.8176040649414,197.8176040649414,197.9936065673828,197.9936065673828,198.1842346191406,198.3899917602539,198.3899917602539,198.6142730712891,198.6142730712891,198.8509521484375,199.0923004150391,199.3243865966797,199.3243865966797,199.5546798706055,199.5546798706055,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,199.5927047729492,197.7599868774414,197.7599868774414,197.7599868774414,197.7599868774414,197.7599868774414,197.7599868774414,197.7864990234375,197.7864990234375,197.7864990234375,197.9796905517578,197.9796905517578,198.1808395385742,198.3978271484375,198.3978271484375,198.6340866088867,198.8773040771484,199.1107864379883,199.1107864379883,199.3317718505859,199.3317718505859,199.5470352172852,199.5470352172852,199.7816314697266,199.7816314697266,200.016960144043,200.016960144043,200.2570648193359,200.4972839355469,200.4972839355469,200.7372970581055,200.7372970581055,200.7372970581055,200.9585647583008,200.9585647583008,201.1803512573242,201.1803512573242,201.3800888061523,201.3800888061523,201.5790557861328,201.5790557861328,201.778678894043,201.9780197143555,202.1775817871094,202.3773422241211,202.5768051147461,202.5768051147461,202.7761306762695,202.9759979248047,202.9759979248047,203.1755142211914,203.1755142211914,203.3756790161133,203.5751419067383,203.7733764648438,203.7733764648438,203.9725494384766,203.9725494384766,203.9725494384766,204.1717071533203,204.1717071533203,204.3716278076172,204.3716278076172,204.5712509155273,204.5712509155273,204.7704162597656,204.7704162597656,204.9695816040039,205.1688766479492,205.3682632446289,205.3682632446289,205.4079208374023,205.4079208374023,205.4079208374023,205.4079208374023,205.4079208374023,205.4079208374023,198.280387878418,198.280387878418,198.4833908081055,198.4833908081055,198.7025756835938,198.7025756835938,198.9364852905273,198.9364852905273,199.1779403686523,199.1779403686523,199.4055862426758,199.6215438842773,199.6215438842773,199.8541107177734,200.0932312011719,200.0932312011719,200.0932312011719,200.3265380859375,200.564208984375,200.564208984375,200.564208984375,200.8068237304688,201.053108215332,201.053108215332,201.3003768920898,201.5475921630859,201.5475921630859,201.793571472168,202.0364837646484,202.0364837646484,202.269287109375,202.5035018920898,202.7392120361328,202.9756469726562,203.2121200561523,203.2121200561523,203.4569320678711,203.4569320678711,203.7038345336914,203.7038345336914,203.7038345336914,203.9503631591797,203.9503631591797,204.1974563598633,204.1974563598633,204.4440383911133,204.6915130615234,204.9388046264648,204.9388046264648,205.1780166625977,205.1780166625977,205.413948059082,205.6170654296875,205.6170654296875,205.6170654296875,205.6170654296875,205.6170654296875,205.6170654296875,205.6170654296875,205.6170654296875,205.6170654296875,198.461067199707,198.461067199707,198.6577682495117,198.6577682495117,198.6577682495117,198.8614730834961,199.0822448730469,199.0822448730469,199.0822448730469,199.3195343017578,199.5495529174805,199.5495529174805,199.7666015625,199.7666015625,199.7666015625,199.9930114746094,200.2346343994141,200.2346343994141,200.47216796875,200.47216796875,200.7130966186523,200.7130966186523,200.9598388671875,200.9598388671875,200.9598388671875,201.2072982788086,201.2072982788086,201.454704284668,201.454704284668,201.7032012939453,201.9504318237305,201.9504318237305,202.1965942382812,202.1965942382812,202.1965942382812,202.4432907104492,202.4432907104492,202.6897354125977,202.9362182617188,202.9362182617188,203.1827163696289,203.4288024902344,203.4288024902344,203.6614608764648,203.6614608764648,203.9034423828125,203.9034423828125,204.1740798950195,204.4195556640625,204.4195556640625,204.6634826660156,204.9047546386719,204.9047546386719,205.1507110595703,205.1507110595703,205.387825012207,205.387825012207,205.6217575073242,205.8229598999023,205.8229598999023,205.8229598999023,205.8229598999023,205.8229598999023,205.8229598999023,205.8229598999023,205.8229598999023,205.8229598999023,198.7516326904297,198.7516326904297,198.9151611328125,198.9151611328125,199.1168060302734,199.1168060302734,199.3270034790039,199.5528869628906,199.5528869628906,199.7812652587891,199.9971466064453,200.228141784668,200.4691772460938,200.7064437866211,200.7064437866211,200.9449310302734,200.9449310302734,201.1870880126953,201.1870880126953,201.1870880126953,201.4315032958984,201.4315032958984,201.6759643554688,201.6759643554688,201.9206008911133,201.9206008911133,202.165168762207,202.165168762207,202.4087142944336,202.4087142944336,202.6768417358398,202.9207763671875,202.9207763671875,203.1643829345703,203.4060668945312,203.6388702392578,203.6388702392578,203.8773422241211,204.1177520751953,204.3609619140625,204.6004867553711,204.8447418212891,205.0896377563477,205.0896377563477,205.3311614990234,205.3311614990234,205.5710144042969,205.5710144042969,205.8052597045898,205.8052597045898,205.8052597045898,206.0253677368164,206.0253677368164,206.0253677368164,206.0253677368164,206.0253677368164,206.0253677368164,206.0253677368164,206.0253677368164,199.2246475219727,199.2246475219727,199.4228668212891,199.4228668212891,199.628173828125,199.8454132080078,199.8454132080078,200.0658340454102,200.0658340454102,200.0658340454102,200.2828903198242,200.2828903198242,200.5222854614258,200.5222854614258,200.7631912231445,200.7631912231445,201.0237350463867,201.2580642700195,201.2580642700195,201.4993515014648,201.7449417114258,201.7449417114258,201.9903106689453,201.9903106689453,202.2347564697266,202.2347564697266,202.4785003662109,202.7217102050781,202.9652709960938,202.9652709960938,203.2089538574219,203.2089538574219,203.4526901245117,203.4526901245117,203.6929702758789,203.9351272583008,203.9351272583008,204.1786499023438,204.1786499023438,204.1786499023438,204.4223556518555,204.4223556518555,204.6674957275391,204.9124755859375,204.9124755859375,205.1576156616211,205.1576156616211,205.4022750854492,205.4022750854492,205.6475296020508,205.6475296020508,205.8823318481445,205.8823318481445,206.1160507202148,206.1160507202148,206.2246704101562,206.2246704101562,206.2246704101562,206.2246704101562,206.2246704101562,206.2246704101562,206.2246704101562,206.2246704101562,206.2246704101562,199.4335403442383,199.4335403442383,199.6242370605469,199.6242370605469,199.8448257446289,199.8448257446289,200.0541763305664,200.0541763305664,200.2667083740234,200.2667083740234,200.4802093505859,200.4802093505859,200.7198944091797,200.9584350585938,201.1973648071289,201.1973648071289,201.4334182739258,201.4334182739258,201.4334182739258,201.6778335571289,201.6778335571289,201.9215698242188,201.9215698242188,202.1642379760742,202.1642379760742,202.4065704345703,202.4065704345703,202.6494293212891,202.8918304443359,203.1332550048828,203.1332550048828,203.1332550048828,203.3759155273438,203.3759155273438,203.6171951293945,203.6171951293945,203.85888671875,204.100456237793,204.100456237793,204.3428268432617,204.3428268432617,204.585334777832,204.585334777832,204.8284912109375,204.8284912109375,205.0701599121094,205.0701599121094,205.3105239868164,205.3105239868164,205.5538024902344,205.5538024902344,205.7976837158203,205.7976837158203,206.0325088500977,206.2663421630859,206.4206085205078,206.4206085205078,206.4206085205078,206.4206085205078,206.4206085205078,206.4206085205078,206.4206085205078,206.4206085205078,206.4206085205078,199.7130661010742,199.7130661010742,199.9010009765625,199.9010009765625,200.0986328125,200.0986328125,200.3002319335938,200.3002319335938,200.3002319335938,200.5072860717773,200.5072860717773,200.7173309326172,200.7173309326172,200.955322265625,200.955322265625,201.1941528320312,201.4325790405273,201.4325790405273,201.6674118041992,201.907112121582,201.907112121582,202.1487426757812,202.1487426757812,202.3903198242188,202.3903198242188,202.6336898803711,202.6336898803711,202.8734664916992,203.11572265625,203.3558502197266,203.597297668457,203.8386383056641,204.0798492431641,204.0798492431641,204.3232498168945,204.5655746459961,204.5655746459961,204.8083648681641,205.0509414672852,205.2898712158203,205.5341567993164,205.5341567993164,205.7796936035156,206.0263824462891,206.0263824462891,206.2641143798828,206.5222702026367,206.5222702026367,206.6135025024414,206.6135025024414,206.6135025024414,206.6135025024414,206.6135025024414,206.6135025024414,206.6135025024414,206.6135025024414,206.6135025024414,206.6135025024414,206.6135025024414,206.6135025024414,206.6135025024414,206.6135025024414,206.6135025024414,206.6135025024414,206.6135025024414,206.6135025024414,206.6135025024414,206.6135025024414,206.6135025024414,206.6135025024414,206.6135025024414,206.6135025024414,206.6135025024414,206.6135025024414,206.6135025024414,199.9779281616211,199.9779281616211,199.9779281616211,199.9779281616211,199.9779281616211,199.9779281616211,200.0112991333008,200.0112991333008,200.2016830444336,200.2016830444336,200.4003524780273,200.5999755859375,200.8028259277344,201.0225601196289,201.0225601196289,201.2329177856445,201.4758453369141,201.4758453369141,201.6926803588867,201.6926803588867,201.9199752807617,202.1406707763672,202.1406707763672,202.3732299804688,202.6093978881836,202.6093978881836,202.8475036621094,202.8475036621094,202.8475036621094,203.0856628417969,203.0856628417969,203.3242416381836,203.3242416381836,203.5621032714844,203.7999954223633,203.7999954223633,204.0388565063477,204.2776718139648,204.5174942016602,204.5174942016602,204.7572479248047,204.998176574707,205.2394790649414,205.4806671142578,205.4806671142578,205.7219848632812,205.7219848632812,205.9636459350586,205.9636459350586,206.2050628662109,206.2050628662109,206.4442367553711,206.4442367553711,206.4442367553711,206.6832962036133,206.8030700683594,206.8030700683594,206.8030700683594,206.8030700683594,206.8030700683594,206.8030700683594,206.8030700683594,206.8030700683594,206.8030700683594,200.3033447265625,200.3033447265625,200.5090026855469,200.5090026855469,200.7032775878906,200.7032775878906,200.8958206176758,201.0879211425781,201.0879211425781,201.3098907470703,201.3098907470703,201.5445556640625,201.7771224975586,202.0072174072266,202.2347030639648,202.4619445800781,202.696174621582,202.696174621582,202.9253540039062,202.9253540039062,203.1531295776367,203.1531295776367,203.3801651000977,203.3801651000977,203.3801651000977,203.6096649169922,203.6096649169922,203.8374328613281,203.8374328613281,204.0659027099609,204.2945861816406,204.2945861816406,204.5342483520508,204.5342483520508,204.7735977172852,204.7735977172852,205.0128326416016,205.0128326416016,205.2532653808594,205.4906311035156,205.4906311035156,205.7331390380859,205.7331390380859,205.9758071899414,205.9758071899414,206.2185363769531,206.4615707397461,206.4615707397461,206.7022705078125,206.7022705078125,206.9431838989258,206.9431838989258,206.9897079467773,206.9897079467773,206.9897079467773,206.9897079467773,206.9897079467773,206.9897079467773,206.9897079467773,206.9897079467773,206.9897079467773,200.6737060546875,200.6737060546875,200.8610687255859,200.8610687255859,201.0499267578125,201.2374649047852,201.2374649047852,201.4459686279297,201.4459686279297,201.6759567260742,201.6759567260742,201.9107437133789,202.1423721313477,202.1423721313477,202.3711929321289,202.3711929321289,202.5974426269531,202.5974426269531,202.8253860473633,202.8253860473633,203.0607070922852,203.0607070922852,203.2973709106445,203.2973709106445,203.5336151123047,203.5336151123047,203.7713394165039,203.7713394165039,203.7713394165039,204.0100250244141,204.0100250244141,204.2431945800781,204.2431945800781,204.4762420654297,204.4762420654297,212.1263885498047,212.1263885498047,212.1263885498047,212.1263885498047,212.1263885498047,212.1263885498047,212.1263885498047,212.1263885498047,212.1263885498047,212.1263885498047,212.1263885498047,212.1263885498047,212.1263885498047,212.1263885498047,212.1263885498047,212.1263885498047,212.1263885498047,212.1263885498047,212.1263885498047,212.1263885498047,212.1263885498047,212.1263885498047,219.7557830810547,219.7557907104492,219.7557907104492,219.7557907104492,219.7557907104492,219.7557907104492,219.7557907104492,219.7557907104492,219.7557907104492,219.7557907104492,219.7557907104492,219.7557907104492,219.7557907104492,219.7557907104492,219.7557907104492,219.7557907104492,219.7557907104492,219.7557907104492,219.7557907104492,219.7557907104492,219.7557907104492,219.7557907104492,219.7557907104492,219.7557907104492,219.7557907104492,235.0145797729492,235.0145797729492,235.0145797729492,235.0145797729492,235.0145797729492,235.0145797729492,235.0145797729492,235.0145797729492,235.0145797729492,235.0145797729492,235.0145797729492,235.0145797729492,235.0145797729492,235.0145797729492,235.0145797729492,235.0145797729492,235.0145797729492,235.0145797729492,235.0145797729492,235.0145797729492,242.6439971923828,242.6439971923828,242.6439971923828,242.6439971923828,242.6439971923828,242.6439971923828,242.6439971923828,242.6439971923828,242.7451019287109,242.7451019287109,242.7451019287109,242.7451019287109,242.7451019287109,242.7451019287109,242.7451019287109,242.7451019287109,242.7451019287109,242.7451019287109,242.7451019287109,242.7451019287109,242.7451019287109,242.7451019287109,242.7451019287109,242.7451019287109,242.7451019287109,242.7451019287109,242.7451019287109,242.7451019287109,242.7451019287109,242.7451019287109,242.7451019287109,242.7451019287109,242.7451019287109,242.7451019287109,242.7451019287109,242.7451019287109,242.7451019287109,242.7451019287109,242.7451019287109,242.7451019287109,242.7451019287109,242.7451019287109,242.7451019287109,242.7451019287109,242.7451019287109,242.7451019287109,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707,258.039192199707],"meminc":[0,0,0,0,0,0,15.28223419189453,0,0,0,0,0,-15.28857421875,0,0,45.75431823730469,0,0,0,0,0,0,0,0,0,4.57763671875e-05,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-0.00030517578125,0,15.32427978515625,0,0.1898651123046875,0,0.2013092041015625,0,0.206695556640625,0,0.221466064453125,0,0.2328414916992188,0,0.2425460815429688,0,0.2380599975585938,0.22882080078125,0.2287216186523438,0.2301483154296875,0,0.2292098999023438,0,0.2314376831054688,0,0,0.2350082397460938,0.2377548217773438,0,0.0404815673828125,0,-2.977020263671875,0,0.2352981567382812,0,0.2422332763671875,0.2430267333984375,0.2654953002929688,0.239532470703125,0.2341995239257812,0,0.2316131591796875,0,0.2305755615234375,0,0.2291717529296875,0,0.23199462890625,0,0.2331085205078125,0.2316665649414062,0.1988754272460938,0,0,-3.045112609863281,0,0.21441650390625,0,0.2305984497070312,0,0.2412338256835938,0,0,0.2402725219726562,0.239105224609375,0.235504150390625,0,0.2317886352539062,0.2312774658203125,0.2294769287109375,0.2292861938476562,0.2296981811523438,0.2296600341796875,0,0.23114013671875,0,0.118743896484375,0,0,-2.952041625976562,0.2081146240234375,0.2220840454101562,0,0.239013671875,0,0.239410400390625,0.2371673583984375,0,0.2567367553710938,0,0.230560302734375,0,0.2316513061523438,0,0,0.2294998168945312,0.2298736572265625,0,0.2283477783203125,0,0.2298660278320312,0,0.2287750244140625,0.0266876220703125,0,0,-2.803398132324219,0,0.2256622314453125,0,0.2334442138671875,0,0.2425155639648438,0.239471435546875,0,0.23583984375,0,0.2322006225585938,0,0.2289352416992188,0,0.2287139892578125,0.2275390625,0,0.2281036376953125,0,0.2289962768554688,0,0.2302932739257812,0,0.1059417724609375,0,0,-2.837448120117188,0,0.2153167724609375,0.2342529296875,0.2441940307617188,0,0.2405776977539062,0.238311767578125,0,0.2360305786132812,0,0,0.2560501098632812,0,0.2337417602539062,0.2312469482421875,0,0.2312545776367188,0,0.2305755615234375,0,0.2309112548828125,0,0.09793853759765625,0,0,-2.789093017578125,0,0.2135696411132812,0,0.2261734008789062,0.2404937744140625,0.2382659912109375,0,0.2368316650390625,0,0.2335739135742188,0,0.2323837280273438,0.2321319580078125,0,0.2307281494140625,0,0.2316741943359375,0,0.2314376831054688,0,0.2328033447265625,0,0.09059906005859375,0,0,-2.732101440429688,0,0.2175674438476562,0,0.234832763671875,0,0.2425308227539062,0.2361373901367188,0,0.2358779907226562,0,0.233917236328125,0,0.23016357421875,0,0.2314682006835938,0,0.2299041748046875,0,0.254241943359375,0,0.23077392578125,0,0.2319564819335938,0,0,0.0030059814453125,0,0,-2.6177978515625,0.2172775268554688,0,0.2353134155273438,0,0.2387847900390625,0,0.2360382080078125,0,0.2360458374023438,0,0.2329940795898438,0,0.2318038940429688,0,0.2321395874023438,0,0.2304000854492188,0.2305908203125,0,0.230926513671875,0,0.1444549560546875,0,0,-2.706710815429688,0,0.2072982788085938,0,0.2259674072265625,0,0.2388458251953125,0,0,0.2374496459960938,0.2354888916015625,0.23455810546875,0,0.2328567504882812,0,0.2332305908203125,0,0.2324676513671875,0,0.2300643920898438,0,0.2303848266601562,0,0.2308807373046875,0.01496124267578125,0,0,-2.521522521972656,0,0.2179412841796875,0,0.2386245727539062,0.2367172241210938,0,0.2358627319335938,0,0.236053466796875,0,0.23492431640625,0,0.2346420288085938,0,0.2334060668945312,0.2322540283203125,0,0.2322463989257812,0.2324142456054688,0,0.03282928466796875,0,0,-2.521926879882812,0.2168350219726562,0,0,0.2350082397460938,0.2377548217773438,0,0.237213134765625,0,0,0.2372894287109375,0.2349090576171875,0,0.2316360473632812,0,0.2319717407226562,0,0.230987548828125,0.2319793701171875,0.2315521240234375,0,0.04003143310546875,0,0,-2.489517211914062,0,0.2140731811523438,0,0.230560302734375,0,0.259796142578125,0.2336654663085938,0,0.2360610961914062,0.2346115112304688,0,0.2312850952148438,0.2317886352539062,0,0.23126220703125,0,0.2325286865234375,0.2278900146484375,0,0,0,0,0,-2.406059265136719,0.2166366577148438,0,0.2280120849609375,0,0.2353134155273438,0.2340774536132812,0,0.2366714477539062,0,0.2346725463867188,0.2317886352539062,0,0.23297119140625,0,0.2328948974609375,0,0,0.2328338623046875,0,0.1630172729492188,0,0,0,0,0,-2.322555541992188,0,0.21533203125,0,0.2216262817382812,0,0.2330093383789062,0.2358627319335938,0,0.2386932373046875,0.235107421875,0,0.2345733642578125,0,0.2581939697265625,0.2347335815429688,0,0.2344207763671875,0,0.052642822265625,0,-2.388389587402344,0,0.2128524780273438,0,0.2204132080078125,0,0.2334060668945312,0,0,0.23583984375,0,0.2379302978515625,0,0.2340774536132812,0,0.2320404052734375,0.2340469360351562,0,0.2325057983398438,0,0.232513427734375,0,0.1532135009765625,0,0,0,-2.228431701660156,0,0.2140350341796875,0,0.2209243774414062,0,0.2317886352539062,0,0.2353134155273438,0,0.2352066040039062,0.2352447509765625,0,0.2342605590820312,0,0.233978271484375,0.2312469482421875,0,0.2258377075195312,0,0,0,0,0,0,0,-2.232666015625,0,0.209869384765625,0,0.2187957763671875,0.23187255859375,0,0.2354354858398438,0,0.237579345703125,0,0.2365646362304688,0,0,0.2344436645507812,0,0,0.2423782348632812,0.243133544921875,0,0.2107696533203125,0,0,0,0,0,-2.193557739257812,0.20941162109375,0.2184219360351562,0,0.23284912109375,0,0.234619140625,0,0,0.2386398315429688,0,0.2365646362304688,0,0.24285888671875,0,0.24334716796875,0,0.2418060302734375,0,0.1621551513671875,0,0,0,0,0,-2.123313903808594,0,0.205352783203125,0.2161941528320312,0.2315673828125,0,0.2335433959960938,0,0.257659912109375,0,0.2326202392578125,0,0.230926513671875,0,0.2307662963867188,0,0.23150634765625,0.1191482543945312,0,-2.258766174316406,0.1891860961914062,0,0,0.2054595947265625,0.2159042358398438,0.2343902587890625,0,0.2370452880859375,0.237274169921875,0,0,0.2368621826171875,0.2354888916015625,0.2439117431640625,0.2427139282226562,0,0.0455474853515625,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2.236564636230469,0,0.1050033569335938,0,0,0.175872802734375,0.1841964721679688,0,0.1916732788085938,0.2108230590820312,0.2243576049804688,0.237701416015625,0,0.2332763671875,0.22576904296875,0,0.2292404174804688,0.2323150634765625,0,0.0500030517578125,0,0,-2.1358642578125,0,0.1980667114257812,0,0.205108642578125,0.2240829467773438,0,0.2370681762695312,0,0.2392044067382812,0,0.2392120361328125,0.2362136840820312,0.2361221313476562,0,0,0.2444305419921875,0,0.1393280029296875,0,0,-2.151924133300781,0,0.1934890747070312,0.2011642456054688,0.2138900756835938,0,0.2340316772460938,0.237945556640625,0,0.2388381958007812,0,0.2369461059570312,0.2347869873046875,0,0.2375259399414062,0,0.1851730346679688,0,0,0,0,0,-2.01715087890625,0,0.1916885375976562,0.2041854858398438,0.2212753295898438,0.23583984375,0,0.236053466796875,0,0.2360458374023438,0.23333740234375,0,0,0.2328338623046875,0.243408203125,0,0,0.0433807373046875,0,0,-2.033035278320312,0,0.1891021728515625,0.2012710571289062,0,0.2169265747070312,0,0,0.2584381103515625,0.236419677734375,0,0.2363128662109375,0.2327423095703125,0,0.2319869995117188,0.228424072265625,0,0,0.06134796142578125,0,-2.01629638671875,0,0.1865081787109375,0,0,0.1966934204101562,0,0.2145843505859375,0.2327194213867188,0,0.23773193359375,0,0.2374191284179688,0,0.2356643676757812,0.2347869873046875,0.2378463745117188,0.06124114990234375,0,-1.9747314453125,0,0.1911163330078125,0,0.2020187377929688,0.2240829467773438,0,0.2374191284179688,0.2389297485351562,0,0.238861083984375,0,0.23809814453125,0,0.2395095825195312,0,0.222747802734375,0,0,0,-1.870994567871094,0,0.1937255859375,0,0.209716796875,0,0.2325515747070312,0,0.2391357421875,0,0,0.2398681640625,0,0.2385177612304688,0.2363128662109375,0,0.2360000610351562,0.1022491455078125,0,-1.946044921875,0,0.1895370483398438,0,0.200897216796875,0,0.2186660766601562,0,0.2368545532226562,0,0.239898681640625,0,0,0.2393951416015625,0.2384262084960938,0,0,0.23553466796875,0.202972412109375,0,0,0,0,0,-1.806793212890625,0,0.1946029663085938,0,0.2104644775390625,0.2312774658203125,0,0.2387008666992188,0.2631301879882812,0,0.2395172119140625,0,0,0.235198974609375,0.2350692749023438,0,0.0140533447265625,0,0,-1.8299560546875,0,0,0.1838912963867188,0,0.2037277221679688,0,0.2254714965820312,0,0.2369613647460938,0.237548828125,0,0.2391891479492188,0,0.2409591674804688,0.2454910278320312,0.07106781005859375,0,-1.835380554199219,0.18743896484375,0,0.1991653442382812,0.2196426391601562,0.237823486328125,0,0.2389984130859375,0,0.240142822265625,0.2408981323242188,0,0.2468338012695312,0.0779266357421875,0,0,-1.812629699707031,0,0.2061920166015625,0,0,0.1985092163085938,0,0.2210311889648438,0,0.2360382080078125,0,0,0.2374649047851562,0.2373046875,0.2380599975585938,0.2446136474609375,0.04595184326171875,0,0,-1.763679504394531,0.1779327392578125,0.2027969360351562,0,0.2243118286132812,0.2389984130859375,0.2409286499023438,0,0.240203857421875,0,0.2414474487304688,0,0.2449264526367188,0,0.00389862060546875,0,0,0,-1.695640563964844,0.19036865234375,0,0.206512451171875,0,0.228485107421875,0,0.240570068359375,0,0,0.2409133911132812,0,0.2407379150390625,0,0.243988037109375,0.154937744140625,0,0,0,-1.5780029296875,0,0.198455810546875,0,0.2174530029296875,0,0.2377853393554688,0,0.2408599853515625,0,0.24285888671875,0,0.2395477294921875,0,0,0.2430877685546875,0.008056640625,0,0,-1.643913269042969,0,0.1898880004882812,0,0.20806884765625,0,0.2232284545898438,0,0,0.2203750610351562,0,0.2402496337890625,0,0,0.2397003173828125,0,0.2360305786132812,0,0.1356277465820312,0,0,0,0,0,-1.545440673828125,0,0.19036865234375,0,0.2113113403320312,0,0.2354507446289062,0,0.24078369140625,0,0.2661895751953125,0,0.238800048828125,0,0.2109909057617188,0,0,0,-1.566383361816406,0,0.1900634765625,0,0.2097244262695312,0,0.231048583984375,0,0.2411575317382812,0.2412261962890625,0,0.2402114868164062,0,0.2423553466796875,0,0,0.0182952880859375,0,-1.58477783203125,0,0.1753158569335938,0,0.2040786743164062,0,0.2269439697265625,0.2417373657226562,0.2409515380859375,0,0,0.240570068359375,0,0.236419677734375,0.06573486328125,0,-1.597145080566406,0,0.1827545166015625,0.1925506591796875,0,0.2151336669921875,0.26025390625,0,0,0.2388153076171875,0,0.239044189453125,0,0.2377243041992188,0,0.07701873779296875,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.589706420898438,0,0.00756072998046875,0,0.1919784545898438,0,0,0.2014236450195312,0,0.2384719848632812,0.2329254150390625,0.2371749877929688,0.2247848510742188,0,0.2174606323242188,0,0.23895263671875,0,0.2458419799804688,0.244964599609375,0.2381973266601562,0.2382736206054688,0,0.2040252685546875,0,0.1983184814453125,0,0,0.1976318359375,0.198211669921875,0.1979904174804688,0,0.1975326538085938,0.19793701171875,0.1974334716796875,0,0.1982879638671875,0,0,0.1972274780273438,0,0.09722900390625,0,0,0,0,0,-4.478607177734375,0,0.220977783203125,0.2403335571289062,0,0.2427520751953125,0.2328109741210938,0,0.2190399169921875,0.2336654663085938,0.2707595825195312,0.251708984375,0.2492752075195312,0.2474212646484375,0,0.2478408813476562,0.2482986450195312,0.2475967407226562,0,0.2470016479492188,0.2472457885742188,0.2469711303710938,0.24700927734375,0,0.2397537231445312,0.230560302734375,0,0,0,0,0,-4.515174865722656,0,0.20721435546875,0,0.2254867553710938,0,0.2415237426757812,0.2349624633789062,0.2206954956054688,0,0.232208251953125,0.2435226440429688,0,0.25079345703125,0.2514801025390625,0.2461013793945312,0,0.2458572387695312,0,0.2461929321289062,0,0.2453231811523438,0,0.2445449829101562,0.2441635131835938,0,0,0.2451095581054688,0,0.2690277099609375,0,0.2426605224609375,0,0.235137939453125,0,0.07338714599609375,0,0,0,0,0,-4.342933654785156,0.2084197998046875,0,0.234771728515625,0,0.2374420166015625,0,0.2226409912109375,0,0.2289962768554688,0.2441024780273438,0,0.24200439453125,0,0.2513046264648438,0,0.2500228881835938,0,0,0.2479705810546875,0,0.2475433349609375,0,0.2469635009765625,0.2430038452148438,0,0,0.2439422607421875,0.2440872192382812,0.2445449829101562,0.2447891235351562,0,0.235687255859375,0,0.15283203125,0,0,0,0,0,-4.318649291992188,0.2319259643554688,0,0.229400634765625,0.2305679321289062,0,0.2168502807617188,0,0,0.2364120483398438,0.2420425415039062,0.2443695068359375,0,0.2510604858398438,0,0.249053955078125,0.2456130981445312,0,0.246002197265625,0,0.2457351684570312,0.2440185546875,0,0.244964599609375,0.2460861206054688,0.2459487915039062,0.246368408203125,0,0.2342605590820312,0,0.1140594482421875,0,0,0,-4.223320007324219,0,0.2069320678710938,0.2217636108398438,0,0,0.2242965698242188,0,0.2188796997070312,0.242095947265625,0.2419357299804688,0,0.2481765747070312,0.2508697509765625,0,0.2740325927734375,0.2467803955078125,0,0.2456512451171875,0,0.2456893920898438,0,0.2449417114257812,0,0.2460861206054688,0.2471923828125,0,0.2389984130859375,0,0.2363662719726562,0,0.2337646484375,0,0.03282928466796875,0,0,0,0,0,-4.09075927734375,0.205413818359375,0,0.2126312255859375,0.2124404907226562,0.2350845336914062,0,0.2411270141601562,0,0,0.2423171997070312,0,0,0.24603271484375,0,0.251068115234375,0,0.247650146484375,0,0.245330810546875,0.2449111938476562,0,0.2456512451171875,0,0.245513916015625,0,0.2460403442382812,0,0.246673583984375,0,0.2469406127929688,0,0.261260986328125,0,0,0.1367416381835938,0,0,0,-4.103996276855469,0,0.2035675048828125,0,0.2121963500976562,0,0.2103347778320312,0,0.2335586547851562,0,0.2405776977539062,0.2431564331054688,0.244140625,0,0.2509994506835938,0,0.2501602172851562,0,0.2453155517578125,0,0.2451553344726562,0,0.2439651489257812,0.244720458984375,0.2444534301757812,0,0.244964599609375,0,0.2457199096679688,0.2384033203125,0,0.1826858520507812,0,0,0,0,0,-4.078109741210938,0,0.2016372680664062,0,0.2072219848632812,0.2053298950195312,0,0.2557144165039062,0.2400054931640625,0,0,0.2426986694335938,0,0.24285888671875,0,0,0.250213623046875,0,0,0.2498550415039062,0.2456817626953125,0,0.2461776733398438,0.2467575073242188,0,0,0.2465286254882812,0,0.24652099609375,0,0.24761962890625,0,0,0.2466506958007812,0.2370071411132812,0.1377029418945312,0,0,0,0,0,-3.976448059082031,0,0.1998825073242188,0,0.20318603515625,0,0.2069091796875,0,0.2358856201171875,0.2392807006835938,0,0.2393951416015625,0,0.2394790649414062,0,0.2465438842773438,0,0.2471389770507812,0,0.243621826171875,0.2434463500976562,0,0.244598388671875,0,0.2683563232421875,0,0.24462890625,0,0.2447891235351562,0.2431411743164062,0.2347869873046875,0.067596435546875,0,0,0,0,0,-3.859588623046875,0,0.1970672607421875,0,0,0.198333740234375,0.2199859619140625,0,0.2395401000976562,0,0.2402801513671875,0.2410964965820312,0.2416839599609375,0.2469711303710938,0,0.2472381591796875,0,0.243255615234375,0,0.244415283203125,0,0.2445755004882812,0.2442626953125,0,0.2442779541015625,0,0.2452545166015625,0.2398147583007812,0,0.1958541870117188,0,0,0,-3.906379699707031,0,0.2139816284179688,0.191558837890625,0,0.2074127197265625,0,0.232879638671875,0,0.23773193359375,0,0.2381210327148438,0,0.2370681762695312,0.2409515380859375,0,0.247589111328125,0,0.2426681518554688,0.24200439453125,0,0.2429046630859375,0.2442169189453125,0,0,0.2436141967773438,0.2436599731445312,0,0.2416305541992188,0.2346115112304688,0,0.03632354736328125,0,0,0,-3.711036682128906,0,0.18951416015625,0,0.2000656127929688,0,0,0.22674560546875,0.2370681762695312,0.2373046875,0.2375030517578125,0,0.2395553588867188,0.24261474609375,0.24462890625,0,0.2413330078125,0.2659835815429688,0,0,0.243255615234375,0.2429580688476562,0,0.2418289184570312,0,0.2433624267578125,0,0.2338104248046875,0.05414581298828125,0,0,0,0,0,-3.668342590332031,0,0.1871109008789062,0.199859619140625,0,0.225616455078125,0,0.2338943481445312,0,0.2341461181640625,0,0.2354278564453125,0,0.2425308227539062,0,0.247222900390625,0.2467575073242188,0,0.240081787109375,0,0.2431640625,0,0,0.2439041137695312,0,0.2442703247070312,0,0,0.2430267333984375,0,0.2426910400390625,0,0,0.2339019775390625,0,0.0336761474609375,0,0,0,-3.594627380371094,0,0.1851806640625,0,0.202667236328125,0,0.2200088500976562,0,0,0.2322006225585938,0,0.1796340942382812,0,0.2325592041015625,0.2340850830078125,0.239349365234375,0.2356643676757812,0.238525390625,0.2363739013671875,0.2372894287109375,0,0.2390594482421875,0,0.2464828491210938,0,0.2470703125,0.235504150390625,0,0.06006622314453125,0,0,0,-3.557640075683594,0.1860580444335938,0,0.2024993896484375,0,0.2211380004882812,0,0.257232666015625,0,0,0.2358856201171875,0.2409286499023438,0.2415618896484375,0,0.2423324584960938,0.2409286499023438,0,0.2374343872070312,0,0.2376480102539062,0,0.2379150390625,0,0.23809814453125,0,0.2379302978515625,0,0.2321548461914062,0,0.1733856201171875,0,0,0,0,0,-3.619979858398438,0.18365478515625,0,0.1849517822265625,0.1995391845703125,0,0,0.2119522094726562,0,0.2230300903320312,0,0.232177734375,0,0.2407302856445312,0,0.24200439453125,0,0.2414932250976562,0,0.241058349609375,0,0.23687744140625,0,0.2386627197265625,0,0.2633743286132812,0,0.2384872436523438,0,0.2379302978515625,0.2276077270507812,0,0.080078125,0,0,0,-3.474884033203125,0.1807861328125,0,0.191497802734375,0,0.2013931274414062,0,0.2137832641601562,0.2266616821289062,0,0.23968505859375,0,0.2414779663085938,0,0,0.2403793334960938,0.24273681640625,0,0.2391281127929688,0,0.2378005981445312,0,0,0.2390289306640625,0.239288330078125,0,0.2364349365234375,0.229095458984375,0,0.1777801513671875,0,0,0,0,0,-3.4866943359375,0,0.1800994873046875,0,0.1850128173828125,0.197845458984375,0,0.20843505859375,0,0.2218170166015625,0,0.2356719970703125,0,0.2384490966796875,0.2632522583007812,0,0.24078369140625,0.23724365234375,0,0.239105224609375,0.2433853149414062,0,0.2434539794921875,0,0.2399826049804688,0,0.23199462890625,0,0.1805648803710938,0,0,0,0,0,-3.422462463378906,0.178985595703125,0.186004638671875,0,0.1948471069335938,0,0.2059402465820312,0.2197723388671875,0.2368392944335938,0,0,0.2379913330078125,0.2386322021484375,0,0.2386322021484375,0,0.2382583618164062,0.23443603515625,0,0.2347869873046875,0,0.2600860595703125,0,0,0.23651123046875,0,0.2286605834960938,0,0.1507797241210938,0,0,0,0,0,-3.369400024414062,0.1775283813476562,0,0.186187744140625,0,0.1920166015625,0.201904296875,0,0.2390289306640625,0,0.234771728515625,0,0.2390518188476562,0.236663818359375,0,0.2353515625,0,0.236663818359375,0,0.2339324951171875,0,0.2344818115234375,0.23309326171875,0.2333221435546875,0.2273483276367188,0.12530517578125,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-3.344642639160156,0,0,0.02718353271484375,0,0.1516799926757812,0.1713714599609375,0,0.1837234497070312,0.1886749267578125,0,0.20263671875,0,0.2401809692382812,0.2360763549804688,0,0.2276382446289062,0,0.2242202758789062,0,0,0.2273941040039062,0,0.229888916015625,0,0.2381362915039062,0,0.2402114868164062,0,0.2384719848632812,0,0.2381210327148438,0,0.174407958984375,0,0,0,0,0,-3.274887084960938,0,0.1766738891601562,0,0.184417724609375,0,0.1898651123046875,0,0.2018508911132812,0.2150726318359375,0,0.2327423095703125,0.235443115234375,0,0,0.2565231323242188,0,0.2331085205078125,0.2331466674804688,0,0.2337188720703125,0.2346115112304688,0,0.2360153198242188,0,0.2366104125976562,0,0.2428207397460938,0,0,0.02632904052734375,0,0,0,0,0,0,0,-3.113838195800781,0,0.1810455322265625,0.1858291625976562,0.1990280151367188,0,0,0.2121124267578125,0,0.2278289794921875,0,0.2345962524414062,0,0.2374191284179688,0,0.2352676391601562,0,0.2314529418945312,0,0.2353134155273438,0,0.2362136840820312,0,0.2421646118164062,0,0,0.24114990234375,0.241241455078125,0,0.06578826904296875,0,0,0,0,0,-3.063018798828125,0,0.1807937622070312,0,0.1889572143554688,0,0,0.2052841186523438,0,0.218536376953125,0.2328262329101562,0,0.2357025146484375,0.2345352172851562,0,0.2343292236328125,0.2337188720703125,0,0.233154296875,0,0.234039306640625,0.2389373779296875,0,0.2464981079101562,0,0.23675537109375,0,0,0,0,0,0,0,0,-2.975883483886719,0.1821060180664062,0,0.1908950805664062,0,0.2061691284179688,0,0.22320556640625,0,0.2354049682617188,0.2368392944335938,0,0,0.2347488403320312,0.2337722778320312,0,0.2582168579101562,0.2360153198242188,0.2406463623046875,0,0.2466964721679688,0,0.24566650390625,0.095123291015625,0,0,0,0,0,-3.006675720214844,0,0.1812286376953125,0,0,0.1865234375,0,0.2014999389648438,0,0.2154693603515625,0,0.230010986328125,0,0.2353134155273438,0,0.2294082641601562,0.22979736328125,0,0.23291015625,0,0.2338943481445312,0,0.2363510131835938,0,0.2375717163085938,0.2378387451171875,0,0.2070083618164062,0,0,0,0,0,0,0,0,-2.863029479980469,0,0,0.2012481689453125,0,0.196197509765625,0,0.2117843627929688,0,0.2289962768554688,0.2388229370117188,0,0.238861083984375,0,0.2365264892578125,0,0,0.2362136840820312,0,0.2364959716796875,0.2378387451171875,0.2417526245117188,0,0.243438720703125,0.201568603515625,0,0,0,0,0,0,0,0,-2.810356140136719,0,0.1818084716796875,0,0.1947784423828125,0,0.2099227905273438,0,0.226898193359375,0.2391128540039062,0,0.2377548217773438,0,0.2356796264648438,0,0.2367019653320312,0,0.2354888916015625,0,0.2350311279296875,0.2382431030273438,0,0.2624969482421875,0.16180419921875,0,0,0,0,0,-2.917884826660156,0.1782302856445312,0.1824264526367188,0,0.19512939453125,0.2125701904296875,0,0.2284317016601562,0,0.2381362915039062,0,0.2397232055664062,0,0.2354202270507812,0,0.2358779907226562,0,0,0.2345733642578125,0,0.2369308471679688,0,0.2404098510742188,0,0.237396240234375,0,0.1065292358398438,0,0,0,0,0,0,0,-2.829414367675781,0.17999267578125,0,0.1840972900390625,0,0.2005233764648438,0,0.2141036987304688,0,0.2543106079101562,0.2368240356445312,0.234100341796875,0,0.2328948974609375,0,0.23358154296875,0.2369918823242188,0.2381973266601562,0.2454605102539062,0,0.220947265625,0,0,0,0,0,-2.680274963378906,0,0.1813201904296875,0.1910247802734375,0,0.2087020874023438,0,0.2272186279296875,0,0.2369003295898438,0,0.2377471923828125,0,0.2353591918945312,0.2351303100585938,0,0.2375946044921875,0,0.2433395385742188,0,0.2458877563476562,0,0.2461471557617188,0,0.03514862060546875,0,0,0,-2.665237426757812,0.1808395385742188,0,0.1903457641601562,0.2061080932617188,0.226593017578125,0.2371444702148438,0,0.238800048828125,0,0.2368927001953125,0.2363662719726562,0,0.2385101318359375,0,0.2465057373046875,0.2482986450195312,0,0.2464065551757812,0,0.0124359130859375,0,0,0,0,0,-2.620071411132812,0,0.1808929443359375,0,0.1882781982421875,0,0.206451416015625,0.2224197387695312,0,0.2363204956054688,0,0.2378082275390625,0,0.2365036010742188,0.235504150390625,0,0.2342453002929688,0.2346115112304688,0,0.2408218383789062,0,0.2447967529296875,0,0,0,0,0,-2.558013916015625,0,0.1807708740234375,0,0.190826416015625,0.2092361450195312,0,0.22686767578125,0.236968994140625,0.23846435546875,0,0.23583984375,0.2357864379882812,0,0.2366180419921875,0.2402114868164062,0.2477188110351562,0,0.1561660766601562,0,0,0,0,0,-2.646713256835938,0.1766586303710938,0,0.1826629638671875,0,0.1962356567382812,0,0.2150650024414062,0.2265396118164062,0,0.23797607421875,0,0,0.2377853393554688,0,0.2330093383789062,0,0.2330474853515625,0,0.2565078735351562,0,0.2353134155273438,0,0.2437820434570312,0,0.0482330322265625,0,0,0,0,0,-2.529258728027344,0.1796340942382812,0,0.1849594116210938,0,0.2019500732421875,0.2204132080078125,0,0.2351913452148438,0.2384185791015625,0,0.236175537109375,0,0.2348556518554688,0,0.2322769165039062,0,0.2384567260742188,0,0.24041748046875,0,0.16143798828125,0,0,0,0,0,-2.567230224609375,0.17657470703125,0,0.1832504272460938,0.1964645385742188,0,0.2152099609375,0.2543792724609375,0,0.2407379150390625,0,0.2389984130859375,0,0.2355194091796875,0,0,0.2362289428710938,0.2378921508789062,0,0.2388076782226562,0,0.1868820190429688,0,0,0,0,0,0,0,0,-2.36956787109375,0,0.1820297241210938,0,0.1926116943359375,0,0.2100906372070312,0,0.2305908203125,0,0.2400436401367188,0,0.2374038696289062,0,0.2350997924804688,0.2350311279296875,0,0.23455810546875,0,0.2362060546875,0,0.208404541015625,0,0,0,0,0,-2.350776672363281,0.2003860473632812,0,0.1924362182617188,0,0.2130889892578125,0,0.2305145263671875,0.2383346557617188,0,0,0.239837646484375,0,0.2367172241210938,0,0.236083984375,0.2321090698242188,0,0.23529052734375,0,0.1673507690429688,0,0,0,0,0,-2.289306640625,0,0.1835708618164062,0,0,0.1928634643554688,0,0.2091293334960938,0.2305908203125,0,0.2419662475585938,0.2415237426757812,0.2396316528320312,0.2384872436523438,0,0.2416152954101562,0,0.2413330078125,0,0.09880828857421875,0,0,0,-2.348045349121094,0,0.18280029296875,0,0.187042236328125,0,0.20355224609375,0,0.2244338989257812,0,0.2398757934570312,0,0.2423324584960938,0.2411727905273438,0.2386398315429688,0,0.2384262084960938,0,0.2407989501953125,0,0.1780853271484375,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2.375709533691406,0.1444854736328125,0,0.168212890625,0.1827316284179688,0,0.1933364868164062,0,0,0.2125015258789062,0,0,0.2263412475585938,0,0.2399444580078125,0.2385787963867188,0,0.2363662719726562,0.236083984375,0,0.2393341064453125,0,0.1254348754882812,0,0,0,0,0,-2.310203552246094,0.1784210205078125,0,0.1839218139648438,0,0.2003631591796875,0,0.2201995849609375,0,0.2356643676757812,0.2198715209960938,0.2548141479492188,0,0,0.2351837158203125,0.2374114990234375,0,0.2377395629882812,0,0,0.1735153198242188,0,0,0,0,0,0,0,0,-2.137863159179688,0,0,0.181671142578125,0.1926498413085938,0.2157669067382812,0,0.232696533203125,0,0.2389984130859375,0,0.239349365234375,0,0.2370529174804688,0.2370223999023438,0.2436752319335938,0.184722900390625,0,0,0,0,0,0,0,0,-2.103767395019531,0.1824493408203125,0,0.1942596435546875,0,0.23651123046875,0,0.234161376953125,0.2397994995117188,0.239593505859375,0.236602783203125,0.2387466430664062,0,0.2423477172851562,0.1240463256835938,0,0,0,0,0,-2.202949523925781,0,0.1745986938476562,0,0.1839675903320312,0,0.1949615478515625,0.2182159423828125,0,0.233245849609375,0,0.2410659790039062,0,0.2398757934570312,0,0.2374191284179688,0,0.2379608154296875,0,0.2386550903320312,0,0.066680908203125,0,0,0,0,0,-2.12689208984375,0,0.180206298828125,0,0.2058181762695312,0,0.2079391479492188,0.2274169921875,0,0.2398910522460938,0,0.2407608032226562,0,0.238861083984375,0,0.2366561889648438,0,0.2376327514648438,0,0.1743850708007812,0,0,0,0,0,0,0,0,-1.991767883300781,0.1824417114257812,0,0.196044921875,0,0.2164993286132812,0,0.2317886352539062,0,0.2384719848632812,0,0.2386474609375,0,0.2362060546875,0,0.235321044921875,0,0,0.2363662719726562,0,0,0.0415802001953125,0,0,0,0,0,-2.039260864257812,0,0.177642822265625,0,0.2043914794921875,0,0.2042312622070312,0,0.2269439697265625,0,0.2368850708007812,0,0.23931884765625,0,0.2355422973632812,0.2336883544921875,0,0,0.2378082275390625,0,0.103485107421875,0,0,0,0,0,-2.049186706542969,0,0.17913818359375,0,0.1858291625976562,0,0.205535888671875,0.2243804931640625,0,0.2395706176757812,0,0.2424468994140625,0,0.2400054931640625,0.2372894287109375,0,0.2402420043945312,0,0.114410400390625,0,0,0,0,0,-2.022613525390625,0.1954345703125,0,0.1863555908203125,0,0,0.2025299072265625,0,0.221771240234375,0,0.23779296875,0,0.2430572509765625,0.2404022216796875,0.2379226684570312,0,0.23895263671875,0,0.0770721435546875,0,0,0,0,0,-1.970893859863281,0.175445556640625,0.1839447021484375,0,0.20037841796875,0,0.2208175659179688,0.2363662719726562,0.2403335571289062,0.2380142211914062,0.2342605590820312,0.236297607421875,0.062835693359375,0,0,0,0,0,-1.923484802246094,0,0.1964950561523438,0.1857833862304688,0.2052383422851562,0,0.2246170043945312,0.238067626953125,0,0.2397537231445312,0.2373504638671875,0,0.2352066040039062,0,0.2177352905273438,0,0,0,0,0,0,0,0,0,0,0,-1.837120056152344,0,0.1802215576171875,0,0,0.1901473999023438,0.2104415893554688,0,0.23114013671875,0,0.2390289306640625,0,0.2401809692382812,0,0,0.234588623046875,0,0.2240829467773438,0,0.1432113647460938,0,0,0,0,0,0,0,0,-1.751449584960938,0,0.1819992065429688,0.1947097778320312,0,0.2146759033203125,0.2347183227539062,0,0.2412948608398438,0,0.2410888671875,0.238189697265625,0,0.2330169677734375,0,0.02679443359375,0,0,0,-1.806716918945312,0,0.178497314453125,0,0.1880874633789062,0,0.2081222534179688,0,0.225830078125,0,0.2402801513671875,0.241455078125,0.2403488159179688,0,0.2352981567382812,0.1028518676757812,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.86279296875,0,0,0.1409149169921875,0,0,0.1760025024414062,0,0.1906280517578125,0.2057571411132812,0,0.2242813110351562,0,0.2366790771484375,0.2413482666015625,0.232086181640625,0,0.2302932739257812,0,0.03802490234375,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.832717895507812,0,0,0,0,0,0.02651214599609375,0,0,0.1931915283203125,0,0.2011489868164062,0.2169876098632812,0,0.2362594604492188,0.2432174682617188,0.2334823608398438,0,0.2209854125976562,0,0.2152633666992188,0,0.2345962524414062,0,0.2353286743164062,0,0.2401046752929688,0.2402191162109375,0,0.2400131225585938,0,0,0.2212677001953125,0,0.2217864990234375,0,0.199737548828125,0,0.1989669799804688,0,0.1996231079101562,0.1993408203125,0.1995620727539062,0.1997604370117188,0.199462890625,0,0.1993255615234375,0.1998672485351562,0,0.1995162963867188,0,0.200164794921875,0.199462890625,0.1982345581054688,0,0.1991729736328125,0,0,0.19915771484375,0,0.199920654296875,0,0.1996231079101562,0,0.1991653442382812,0,0.1991653442382812,0.1992950439453125,0.1993865966796875,0,0.0396575927734375,0,0,0,0,0,-7.127532958984375,0,0.2030029296875,0,0.2191848754882812,0,0.2339096069335938,0,0.241455078125,0,0.2276458740234375,0.2159576416015625,0,0.2325668334960938,0.2391204833984375,0,0,0.233306884765625,0.2376708984375,0,0,0.24261474609375,0.2462844848632812,0,0.2472686767578125,0.2472152709960938,0,0.2459793090820312,0.2429122924804688,0,0.2328033447265625,0.2342147827148438,0.2357101440429688,0.2364349365234375,0.2364730834960938,0,0.24481201171875,0,0.2469024658203125,0,0,0.2465286254882812,0,0.2470932006835938,0,0.24658203125,0.2474746704101562,0.2472915649414062,0,0.2392120361328125,0,0.235931396484375,0.2031173706054688,0,0,0,0,0,0,0,0,-7.155998229980469,0,0.1967010498046875,0,0,0.203704833984375,0.2207717895507812,0,0,0.2372894287109375,0.2300186157226562,0,0.2170486450195312,0,0,0.226409912109375,0.2416229248046875,0,0.2375335693359375,0,0.2409286499023438,0,0.2467422485351562,0,0,0.2474594116210938,0,0.247406005859375,0,0.2484970092773438,0.2472305297851562,0,0.2461624145507812,0,0,0.2466964721679688,0,0.2464447021484375,0.2464828491210938,0,0.2464981079101562,0.2460861206054688,0,0.2326583862304688,0,0.2419815063476562,0,0.2706375122070312,0.2454757690429688,0,0.243927001953125,0.24127197265625,0,0.2459564208984375,0,0.2371139526367188,0,0.2339324951171875,0.201202392578125,0,0,0,0,0,0,0,0,-7.071327209472656,0,0.1635284423828125,0,0.2016448974609375,0,0.2101974487304688,0.2258834838867188,0,0.2283782958984375,0.21588134765625,0.2309951782226562,0.2410354614257812,0.2372665405273438,0,0.2384872436523438,0,0.242156982421875,0,0,0.244415283203125,0,0.2444610595703125,0,0.2446365356445312,0,0.24456787109375,0,0.2435455322265625,0,0.26812744140625,0.2439346313476562,0,0.2436065673828125,0.2416839599609375,0.2328033447265625,0,0.2384719848632812,0.2404098510742188,0.2432098388671875,0.2395248413085938,0.2442550659179688,0.2448959350585938,0,0.2415237426757812,0,0.2398529052734375,0,0.2342453002929688,0,0,0.2201080322265625,0,0,0,0,0,0,0,-6.80072021484375,0,0.1982192993164062,0,0.2053070068359375,0.2172393798828125,0,0.2204208374023438,0,0,0.2170562744140625,0,0.2393951416015625,0,0.24090576171875,0,0.2605438232421875,0.2343292236328125,0,0.2412872314453125,0.2455902099609375,0,0.2453689575195312,0,0.24444580078125,0,0.243743896484375,0.2432098388671875,0.243560791015625,0,0.243682861328125,0,0.2437362670898438,0,0.2402801513671875,0.242156982421875,0,0.2435226440429688,0,0,0.2437057495117188,0,0.2451400756835938,0.2449798583984375,0,0.2451400756835938,0,0.244659423828125,0,0.2452545166015625,0,0.23480224609375,0,0.2337188720703125,0,0.1086196899414062,0,0,0,0,0,0,0,0,-6.791130065917969,0,0.1906967163085938,0,0.2205886840820312,0,0.2093505859375,0,0.2125320434570312,0,0.2135009765625,0,0.23968505859375,0.2385406494140625,0.2389297485351562,0,0.236053466796875,0,0,0.244415283203125,0,0.2437362670898438,0,0.2426681518554688,0,0.2423324584960938,0,0.24285888671875,0.242401123046875,0.241424560546875,0,0,0.2426605224609375,0,0.2412796020507812,0,0.2416915893554688,0.2415695190429688,0,0.24237060546875,0,0.2425079345703125,0,0.2431564331054688,0,0.241668701171875,0,0.2403640747070312,0,0.2432785034179688,0,0.2438812255859375,0,0.2348251342773438,0.2338333129882812,0.154266357421875,0,0,0,0,0,0,0,0,-6.707542419433594,0,0.1879348754882812,0,0.1976318359375,0,0.20159912109375,0,0,0.2070541381835938,0,0.2100448608398438,0,0.2379913330078125,0,0.23883056640625,0.2384262084960938,0,0.234832763671875,0.2397003173828125,0,0.2416305541992188,0,0.2415771484375,0,0.2433700561523438,0,0.239776611328125,0.2422561645507812,0.2401275634765625,0.2414474487304688,0.2413406372070312,0.2412109375,0,0.2434005737304688,0.2423248291015625,0,0.2427902221679688,0.2425765991210938,0.2389297485351562,0.2442855834960938,0,0.2455368041992188,0.2466888427734375,0,0.23773193359375,0.2581558227539062,0,0.0912322998046875,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-6.635574340820312,0,0,0,0,0,0.0333709716796875,0,0.1903839111328125,0,0.19866943359375,0.1996231079101562,0.202850341796875,0.2197341918945312,0,0.210357666015625,0.2429275512695312,0,0.2168350219726562,0,0.227294921875,0.2206954956054688,0,0.2325592041015625,0.2361679077148438,0,0.2381057739257812,0,0,0.2381591796875,0,0.2385787963867188,0,0.2378616333007812,0.2378921508789062,0,0.238861083984375,0.2388153076171875,0.2398223876953125,0,0.2397537231445312,0.2409286499023438,0.241302490234375,0.2411880493164062,0,0.2413177490234375,0,0.2416610717773438,0,0.2414169311523438,0,0.2391738891601562,0,0,0.2390594482421875,0.1197738647460938,0,0,0,0,0,0,0,0,-6.499725341796875,0,0.205657958984375,0,0.19427490234375,0,0.1925430297851562,0.1921005249023438,0,0.2219696044921875,0,0.2346649169921875,0.2325668334960938,0.2300949096679688,0.2274856567382812,0.2272415161132812,0.2342300415039062,0,0.2291793823242188,0,0.2277755737304688,0,0.2270355224609375,0,0,0.2294998168945312,0,0.2277679443359375,0,0.2284698486328125,0.2286834716796875,0,0.2396621704101562,0,0.239349365234375,0,0.2392349243164062,0,0.2404327392578125,0.23736572265625,0,0.2425079345703125,0,0.2426681518554688,0,0.2427291870117188,0.2430343627929688,0,0.2406997680664062,0,0.2409133911132812,0,0.0465240478515625,0,0,0,0,0,0,0,0,-6.316001892089844,0,0.1873626708984375,0,0.1888580322265625,0.1875381469726562,0,0.2085037231445312,0,0.2299880981445312,0,0.2347869873046875,0.23162841796875,0,0.22882080078125,0,0.2262496948242188,0,0.2279434204101562,0,0.235321044921875,0,0.236663818359375,0,0.2362442016601562,0,0.2377243041992188,0,0,0.2386856079101562,0,0.2331695556640625,0,0.2330474853515625,0,7.650146484375,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7.62939453125,7.62939453125e-06,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,15.2587890625,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7.629417419433594,0,0,0,0,0,0,0,0.101104736328125,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,15.29409027099609,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"filename":["<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,null,null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,null,null,null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,null,"<expr>",null,"<expr>","<expr>",null,null,null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,null,null,null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,null,"<expr>",null,null,"<expr>","<expr>",null,null,null,null,null,null,null,"<expr>","<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,null,null,null,null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,null,null,null,null,null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,null,null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,"<expr>","<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null]},"interval":10,"files":[{"filename":"<expr>","content":"## Generate Large Random Dataset\nn <- 2e6\nx <- runif(n)\ny <- runif(n)\nz <- runif(n)\nXYZ <- cbind(x,y,z)\n\n## Inspect 4 equivalent `row mean` calculations \nprofvis::profvis({\n    m <- rowSums(XYZ)/ncol(XYZ)\n    m <- rowMeans(XYZ)\n    m <- apply(XYZ, 1, mean)\n    m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }\n})\n## rowSums(), colSums(), rowMeans(), and colMeans() are vectorised and fast.\n## for loop is not the slowest, but the ugliest.","normpath":"<expr>"}],"prof_output":"/tmp/Rtmp9toRaE/file20f56283e82f.prof","highlight":{"output":["^output\\$"],"gc":["^<GC>$"],"stacktrace":["^\\.\\.stacktraceo(n|ff)\\.\\.$"]},"split":"h"}},"evals":[],"jsHooks":[]}</script>
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
## 1 mean1(x, 0.5)   34.1ms   36.4ms      27.4    7.63MB     0   
## 2 mean2(x, 0.5)   32.6ms   35.7ms      28.6    7.63MB     2.20
## 3 mean3(x, 0.5)   36.4ms   37.1ms      26.9    7.63MB     0
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
##   0.114   0.000   0.039
```

```r
system.time({ lm(Y~X, data=DAT) })
```

```
##    user  system elapsed 
##   0.502   0.000   0.177
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
## 1 ma1(y)        283ms  282.9ms      3.53    15.3MB     3.53
## 2 ma2(y)         27ms   27.5ms     36.4     91.6MB   218.
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
##   0.032   0.006   0.039
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
##   1.318   0.345   0.929
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





