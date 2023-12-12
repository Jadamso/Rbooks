# (PART) Reproducible Research in R {-} 


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


## Replicable

You should make your work reproducible, and we will cover some of the basics of how to do this in R. You also want your work to be replicable

* Replicable: someone collecting new data comes to the same results.
* Reproducibile: someone reusing your data comes to the same results.

You can read more about the distinction in many places, including

* https://www.annualreviews.org/doi/10.1146/annurev-psych-020821-114157
* https://nceas.github.io/sasap-training/materials/reproducible_research_in_r_fairbanks/


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
<div class="plotly html-widget html-fill-item" id="htmlwidget-d348ddbf18d8d66183ce" style="width:672px;height:480px;"></div>
<script type="application/json" data-for="htmlwidget-d348ddbf18d8d66183ce">{"x":{"visdat":{"29c54ea1b0dc":["function () ","plotlyVisDat"]},"cur_data":"29c54ea1b0dc","attrs":{"29c54ea1b0dc":{"x":{},"y":{},"alpha_stroke":1,"sizes":[10,100],"spans":[1,20]}},"layout":{"margin":{"b":40,"l":60,"t":25,"r":10},"xaxis":{"domain":[0,1],"automargin":true,"title":"X"},"yaxis":{"domain":[0,1],"automargin":true,"title":"Y"},"hovermode":"closest","showlegend":false},"source":"A","config":{"modeBarButtonsToAdd":["hoverclosest","hovercompare"],"showSendToCloud":false},"data":[{"x":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100],"y":[5.1089982646477683,6.2067689247018265,13.338681136256229,14.296877875169235,22.322006593155432,22.422459917308704,28.563079616919435,30.486561339705016,37.020840360433013,40.961990071629224,46.279220754400221,48.417348656563291,53.654691535578884,54.727416595535523,56.600114619792585,62.887340091877341,69.602488875724774,72.941481959448566,74.939513852181165,75.963759116678148,83.82899981895703,84.946973238202673,93.804779021352147,94.393795296053952,99.579429363780221,99.934528988296222,107.92806589835735,110.05928106505682,111.09374494431803,115.36341948217425,126.25198074559157,124.90289480821613,133.1990993824196,134.86741120281886,141.90938730987233,141.67460568998391,147.54020133342962,149.72846430216936,156.58549345597044,160.42451344527322,160.70101572164651,162.18239766361114,169.70805545159627,173.87078825110765,182.11529260824003,181.55107241957617,189.09952793907914,190.78006854787427,197.72550073325797,203.2047349294146,203.15701147526229,205.23872502123427,212.39189282885292,215.89683583206312,217.68213003832238,220.45174335442667,230.16733201085952,229.54660189548463,237.27825029009,239.41914203777435,245.52804676453343,248.77868054570322,251.80909827294619,255.78978232554809,257.79035166696127,266.39819398783573,266.86416878866089,274.0501026278161,276.59985131152354,283.66008064523095,286.58500933407464,286.03928993754113,292.88276146596638,302.18813827960042,299.51275508914989,304.88900117471195,311.37706353645154,310.53119984044326,312.85622475807583,325.00149653647804,326.33861109493688,329.51242864362871,332.76148561188415,337.2181047344842,341.74138547336383,342.97972999726142,347.98625346953537,350.91882488365906,356.5067781771798,360.88560527320163,363.03709519211111,369.04501109402599,374.49584398459592,377.87884169038233,379.55085897933452,382.0765498845671,388.46833620235384,391.32519799079824,396.51254113474897,399.48921147698002],"type":"scatter","mode":"markers","marker":{"color":"rgba(31,119,180,1)","line":{"color":"rgba(31,119,180,1)"}},"error_y":{"color":"rgba(31,119,180,1)"},"error_x":{"color":"rgba(31,119,180,1)"},"line":{"color":"rgba(31,119,180,1)"},"xaxis":"x","yaxis":"y","frame":null}],"highlight":{"on":"plotly_click","persistent":false,"dynamic":false,"selectize":false,"opacityDim":0.20000000000000001,"selected":{"opacity":1},"debounce":0},"shinyEvents":["plotly_hover","plotly_click","plotly_selected","plotly_relayout","plotly_brushed","plotly_brushing","plotly_clickannotation","plotly_doubleclick","plotly_deselect","plotly_afterplot","plotly_sunburstclick"],"base_url":"https://plot.ly"},"evals":[],"jsHooks":[]}</script>
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
## Ncells 1212935 64.8    2366027 126.4  2366027 126.4
## Vcells 2298898 17.6    8388608  64.0  3571878  27.3
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
##   0.006   0.000   0.006
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
<div class="profvis html-widget html-fill-item" id="htmlwidget-355ba3481a2e4be92ee7" style="width:100%;height:600px;"></div>
<script type="application/json" data-for="htmlwidget-355ba3481a2e4be92ee7">{"x":{"message":{"prof":{"time":[1,2,3,4,5,6,7,8,9,10,11,12,13,13,14,14,15,15,16,16,17,17,18,18,19,19,20,20,21,21,22,22,23,23,24,24,25,25,26,26,27,27,28,28,29,29,30,30,30,31,31,32,32,33,33,34,34,35,35,36,36,37,37,38,39,39,40,40,41,41,42,42,43,43,44,44,44,44,45,45,46,47,48,48,48,49,49,49,50,50,51,51,52,53,53,54,54,55,55,56,56,57,58,59,59,59,60,61,61,62,62,62,63,64,64,65,66,66,67,68,68,69,69,70,70,71,72,72,73,73,74,74,74,75,75,76,76,77,77,78,78,79,79,80,81,81,82,82,83,83,84,85,86,86,87,88,88,88,89,89,90,90,91,92,92,93,93,94,95,95,96,97,98,98,99,100,101,101,102,102,102,103,103,103,104,104,105,106,106,107,107,108,109,110,110,111,112,112,113,113,114,114,115,115,116,116,116,117,117,117,118,118,119,119,120,120,121,122,122,123,123,124,124,125,126,127,127,128,128,129,129,129,130,130,131,131,132,132,133,133,134,134,135,135,136,137,137,138,138,139,139,140,140,141,141,142,143,144,144,144,145,146,146,147,148,148,149,150,151,152,152,153,154,154,155,155,156,156,157,157,158,158,158,159,159,160,160,161,162,163,163,164,164,165,165,166,166,167,167,168,168,169,169,170,171,171,172,173,174,175,175,176,177,177,178,178,179,179,180,180,181,182,182,183,183,184,184,184,185,185,185,186,186,187,187,188,188,189,189,190,190,191,191,191,192,192,193,193,193,194,195,195,196,196,197,197,197,198,198,198,199,200,200,201,201,202,203,203,204,205,205,206,206,207,207,208,208,209,210,210,210,211,212,212,213,214,214,214,215,215,216,217,217,218,218,218,219,220,221,222,222,223,223,223,224,225,225,226,226,226,227,227,227,228,228,229,229,230,230,231,231,232,232,232,233,233,234,234,235,235,235,236,236,236,237,238,238,239,239,240,240,241,241,242,242,243,244,245,246,246,247,247,248,248,248,249,250,250,250,251,251,252,252,253,254,254,255,255,256,256,257,257,257,258,258,258,259,260,260,261,261,261,262,262,263,264,264,265,266,266,266,267,268,269,269,270,271,271,271,272,272,272,273,273,273,274,274,275,275,276,276,277,277,278,278,278,279,279,280,280,281,281,282,282,283,283,284,284,285,285,286,286,287,287,288,288,289,289,290,290,290,291,291,292,292,293,293,294,295,296,296,296,297,297,297,298,299,299,299,300,300,301,301,302,302,303,303,303,304,305,306,306,307,308,308,309,309,310,310,311,311,312,312,313,313,314,314,315,315,316,316,317,317,318,319,320,320,321,321,321,322,323,323,324,325,325,326,326,327,328,328,329,329,330,330,330,331,331,332,332,333,334,334,335,336,336,337,338,338,338,339,339,340,341,341,342,342,343,343,344,345,345,346,346,346,347,347,348,348,348,349,349,349,350,350,351,351,352,352,353,353,354,355,355,356,356,357,357,358,359,360,361,362,362,363,363,364,364,364,365,365,366,366,367,368,368,369,369,370,370,371,372,372,373,373,374,374,375,375,375,376,376,377,377,378,378,378,379,379,380,380,381,382,383,383,384,384,385,385,386,386,386,387,387,388,389,389,390,390,390,391,391,392,393,393,393,394,394,395,396,396,396,397,397,397,398,398,399,399,400,400,401,401,402,402,403,404,405,405,406,406,407,407,407,408,408,409,409,410,410,410,411,412,413,413,414,414,415,415,416,416,416,417,418,418,419,420,420,421,422,422,423,424,424,424,425,425,426,427,427,428,428,429,429,430,430,430,431,431,431,432,432,433,434,435,436,436,437,437,438,438,438,439,439,440,440,441,442,443,443,444,445,445,446,446,447,448,448,448,449,449,449,450,450,451,451,452,452,453,453,454,454,455,455,456,456,457,458,458,458,459,459,459,460,460,461,461,462,463,463,464,465,465,466,467,468,468,468,469,469,469,470,470,471,471,472,473,473,474,475,476,476,477,477,478,478,478,479,479,479,480,481,481,482,482,483,483,483,484,484,485,485,486,487,487,488,488,489,489,490,490,491,491,492,492,493,493,494,494,495,496,496,497,497,497,498,498,498,499,500,500,501,501,502,502,503,504,504,505,505,506,506,507,507,507,508,509,509,510,510,511,512,512,513,514,514,515,515,516,516,517,517,517,518,518,519,519,520,520,521,521,522,522,523,523,524,524,525,525,526,526,527,527,528,529,530,530,531,532,532,533,534,534,535,535,536,536,537,537,538,538,539,539,540,540,541,541,542,542,543,543,544,544,545,545,546,546,547,547,548,548,549,549,550,550,551,551,552,552,553,553,554,554,555,555,556,556,557,557,558,558,559,559,560,560,561,561,562,562,563,563,564,564,565,565,565,566,566,567,567,568,568,569,569,569,570,571,572,572,573,573,574,574,575,575,576,577,577,578,579,580,581,582,582,583,583,583,584,584,585,585,586,587,587,588,588,588,589,589,589,590,590,591,591,592,592,593,594,595,595,596,596,597,598,598,599,599,600,600,600,601,601,602,602,603,603,604,604,605,605,606,606,607,607,608,608,609,609,610,610,610,610,611,611,611,611,612,613,613,614,614,615,615,616,616,617,617,617,618,618,619,620,621,622,622,623,623,624,625,625,626,627,627,628,628,629,629,630,630,631,631,632,632,632,633,633,633,634,634,635,635,636,637,637,638,638,638,639,640,640,641,641,642,643,643,644,644,645,646,646,647,647,648,648,649,649,650,651,652,653,654,654,655,655,656,656,657,658,658,659,659,660,660,661,661,662,662,663,663,664,664,665,665,666,666,667,668,669,669,670,670,671,671,672,672,673,673,673,674,675,675,676,676,677,677,678,678,679,679,679,680,680,680,681,681,681,682,682,683,684,685,685,686,686,687,687,688,688,689,689,690,690,691,692,692,693,693,693,694,694,695,695,696,697,697,697,698,698,698,699,700,700,701,701,702,702,703,703,704,704,705,706,706,707,707,708,709,709,710,711,712,713,713,713,714,715,715,716,716,717,717,718,718,719,719,720,720,720,721,721,721,722,723,723,724,724,725,725,726,726,727,728,728,729,729,730,731,731,732,733,733,734,735,735,736,737,738,738,738,739,739,739,740,740,740,741,741,742,742,742,743,743,744,744,745,745,745,746,747,747,748,749,749,749,750,751,752,752,753,753,753,754,755,755,756,756,756,757,757,758,759,759,760,760,761,761,762,762,763,764,764,764,765,765,766,767,767,767,768,768,769,769,770,770,770,771,772,773,773,774,774,775,775,776,776,777,777,778,778,779,779,780,780,781,781,782,782,782,783,783,783,784,785,785,786,786,787,787,788,789,789,789,790,790,791,791,792,792,792,793,793,794,794,795,795,796,797,797,798,798,799,800,800,801,801,802,802,802,803,803,803,804,804,805,806,806,807,807,808,808,809,810,810,811,811,812,812,813,813,814,814,815,815,816,817,817,818,818,819,819,820,820,821,821,822,822,822,823,823,823,824,824,825,825,826,826,827,828,829,830,830,831,831,831,832,832,833,833,834,834,835,836,836,837,837,838,838,839,839,840,841,841,842,842,842,843,843,843,844,844,845,845,846,846,847,847,848,848,849,850,851,851,852,852,853,853,854,854,855,855,856,856,857,857,857,858,858,859,859,860,860,860,861,861,861,862,862,862,863,863,863,864,865,866,866,867,867,868,868,869,870,870,871,872,872,873,874,874,875,875,876,876,876,877,877,878,879,880,880,881,881,882,882,883,883,884,884,885,885,886,887,888,889,890,891,891,892,892,893,893,894,895,895,896,897,897,898,898,899,899,900,900,901,901,902,902,903,903,903,904,904,904,905,905,906,907,907,908,908,909,910,910,911,912,913,913,914,915,915,916,917,917,918,918,919,919,920,920,921,921,922,923,924,925,925,926,927,927,928,928,928,929,929,930,931,932,932,932,933,933,934,935,935,936,936,937,937,937,938,938,938,939,940,940,941,942,942,943,943,944,945,946,946,947,948,948,948,949,949,950,950,951,952,952,953,953,954,954,955,955,955,956,956,956,957,958,958,959,960,960,961,961,962,963,963,964,964,965,966,966,967,967,968,969,970,970,971,971,972,972,973,973,973,974,974,974,975,975,976,976,977,978,979,979,980,980,981,982,983,984,985,985,986,987,987,988,988,989,989,990,990,991,991,992,992,992,993,993,993,994,994,994,995,995,995,996,996,996,997,997,997,998,998,998,999,999,999,1000,1000,1000,1001,1001,1001,1002,1002,1002,1003,1003,1003,1004,1004,1004,1005,1005,1005,1006,1006,1006,1007,1007,1007,1008,1008,1008,1009,1009,1009,1010,1010,1011,1011,1012,1012,1013,1013,1014,1014,1015,1016,1016,1016,1017,1017,1018,1018,1019,1020,1021,1021,1022,1023,1023,1024,1024,1025,1026,1026,1026,1027,1027,1027,1028,1029,1029,1030,1030,1031,1032,1033,1033,1034,1034,1035,1036,1036,1037,1037,1038,1039,1039,1040,1041,1041,1041,1042,1042,1042,1043,1043,1044,1044,1045,1046,1046,1047,1047,1048,1048,1049,1049,1050,1050,1051,1051,1052,1052,1053,1054,1054,1055,1055,1056,1056,1057,1057,1058,1058,1059,1059,1060,1060,1061,1061,1062,1062,1063,1063,1064,1064,1065,1065,1066,1066,1067,1067,1067,1068,1068,1069,1070,1071,1071,1072,1072,1073,1073,1074,1074,1075,1075,1075,1076,1076,1077,1077,1077,1078,1078,1078,1079,1079,1080,1080,1081,1081,1081,1082,1082,1083,1083,1084,1085,1085,1085,1086,1086,1087,1087,1088,1088,1089,1089,1090,1090,1091,1092,1092,1093,1093,1094,1094,1095,1095,1096,1097,1097,1098,1099,1100,1100,1101,1101,1102,1102,1103,1104,1105,1105,1105,1106,1107,1107,1108,1108,1109,1109,1110,1110,1111,1111,1111,1112,1112,1112,1113,1114,1114,1115,1116,1116,1116,1117,1117,1118,1119,1120,1120,1121,1122,1122,1123,1124,1124,1125,1126,1126,1127,1127,1127,1128,1128,1128,1129,1129,1129,1130,1130,1130,1131,1131,1132,1132,1133,1133,1134,1135,1135,1135,1136,1137,1137,1138,1139,1140,1140,1141,1141,1142,1142,1142,1143,1144,1144,1145,1145,1146,1146,1147,1147,1148,1148,1149,1149,1150,1150,1151,1151,1152,1152,1153,1153,1154,1154,1155,1155,1156,1156,1157,1157,1157,1158,1158,1159,1160,1160,1161,1161,1161,1162,1162,1162,1163,1163,1164,1164,1165,1166,1167,1167,1168,1169,1169,1170,1170,1171,1171,1172,1172,1173,1173,1174,1175,1176,1176,1177,1177,1177,1178,1178,1178,1179,1179,1179,1180,1180,1181,1182,1182,1183,1184,1184,1185,1186,1186,1186,1187,1187,1188,1188,1189,1189,1190,1190,1190,1191,1191,1192,1193,1193,1193,1194,1194,1194,1195,1196,1196,1196,1197,1197,1198,1198,1199,1199,1200,1201,1202,1202,1203,1203,1204,1204,1205,1206,1207,1208,1208,1209,1209,1210,1211,1211,1212,1212,1213,1214,1214,1215,1215,1216,1216,1217,1217,1218,1218,1219,1219,1219,1220,1221,1221,1222,1222,1223,1223,1224,1224,1224,1225,1225,1225,1226,1227,1228,1228,1229,1230,1231,1231,1232,1232,1233,1233,1234,1234,1235,1235,1236,1236,1237,1238,1238,1239,1239,1239,1240,1240,1240,1241,1242,1242,1243,1243,1244,1244,1245,1245,1246,1246,1246,1247,1247,1248,1249,1249,1250,1251,1251,1252,1253,1253,1254,1254,1255,1255,1256,1256,1257,1257,1258,1259,1260,1260,1261,1261,1262,1262,1263,1264,1264,1265,1266,1267,1268,1268,1269,1269,1270,1270,1270,1271,1271,1272,1272,1273,1274,1274,1275,1275,1276,1276,1277,1277,1278,1279,1280,1281,1281,1282,1283,1283,1283,1284,1284,1284,1285,1286,1286,1287,1287,1288,1289,1289,1290,1290,1290,1291,1291,1292,1293,1294,1295,1295,1296,1296,1297,1297,1297,1298,1298,1298,1299,1299,1300,1301,1301,1301,1302,1302,1302,1303,1303,1304,1304,1305,1305,1306,1306,1307,1308,1308,1309,1309,1310,1310,1311,1311,1312,1312,1313,1313,1314,1314,1315,1316,1317,1318,1319,1320,1321,1322,1322,1323,1323,1324,1324,1325,1325,1325,1326,1326,1326,1327,1327,1328,1328,1329,1329,1330,1331,1332,1332,1333,1333,1334,1334,1335,1336,1336,1337,1337,1338,1338,1338,1338,1339,1339,1339,1339,1340,1340,1340,1340,1341,1341,1341,1341,1342,1342,1342,1342,1343,1343,1343,1343,1344,1344,1344,1344,1345,1345,1345,1345,1346,1346,1346,1346,1347,1347,1347,1347,1348,1348,1348,1348,1349,1349,1349,1349,1350,1350,1350,1350,1351,1352,1352,1353,1354,1355,1355,1356,1356,1356,1357,1357,1358,1359,1360,1360,1360,1361,1361,1362,1363,1363,1363,1364,1364,1364,1365,1365,1366,1366,1367,1368,1368,1369,1369,1370,1370,1371,1371,1372,1372,1373,1374,1375,1375,1376,1376,1377,1377,1378,1378,1379,1379,1380,1380,1381,1382,1383,1383,1384,1384,1385,1386,1387,1388,1388,1388,1389,1390,1390,1390,1391,1391,1391,1392,1392,1392,1393,1393,1394,1394,1395,1395,1395,1396,1396,1397,1398,1399,1399,1400,1400,1401,1401,1402,1403,1403,1403,1403,1404,1404,1404,1404,1405,1405,1405,1405,1406,1406,1407,1407,1408,1409,1409,1410,1410,1411,1412,1413,1413,1414,1414,1415,1415,1416,1416,1416,1417,1417,1417,1418,1418,1418,1419,1419,1419,1420,1420,1421,1421,1422,1422,1423,1423,1424,1424,1425,1425,1426,1426,1427,1427,1428,1428,1428,1429,1430,1430,1430,1431,1431,1431,1432,1432,1433,1433,1434,1435,1435,1436,1436,1437,1438,1438,1439,1440,1440,1441,1442,1442,1443,1443,1444,1444,1445,1445,1446,1447,1448,1448,1449,1449,1449,1450,1450,1451,1452,1453,1453,1454,1454,1455,1456,1456,1456,1457,1457,1457,1458,1458,1459,1459,1460,1460,1461,1461,1462,1463,1463,1464,1465,1466,1466,1467,1468,1468,1469,1469,1470,1470,1471,1471,1472,1472,1473,1474,1474,1474,1475,1476,1476,1477,1477,1478,1478,1479,1480,1480,1481,1481,1481,1482,1482,1482,1483,1483,1484,1485,1485,1485,1486,1487,1487,1488,1488,1488,1489,1490,1491,1492,1493,1493,1494,1494,1494,1495,1495,1495,1496,1497,1498,1498,1499,1499,1500,1501,1501,1502,1503,1504,1505,1505,1505,1506,1506,1507,1507,1507,1508,1508,1508,1509,1509,1509,1510,1511,1511,1512,1513,1514,1515,1516,1516,1517,1517,1518,1519,1519,1519,1520,1520,1520,1521,1521,1521,1522,1522,1523,1523,1524,1524,1525,1526,1526,1527,1527,1528,1529,1529,1529,1530,1530,1531,1531,1531,1532,1532,1532,1533,1533,1534,1535,1535,1536,1536,1537,1537,1538,1539,1539,1540,1540,1541,1541,1541,1542,1543,1543,1543,1544,1544,1544,1545,1545,1545,1546,1546,1546,1547,1547,1547,1548,1548,1548,1549,1549,1549,1550,1550,1550,1551,1551,1552,1553,1553,1553,1554,1554,1554,1555,1555,1556,1557,1557,1558,1559,1559,1560,1560,1561,1561,1561,1562,1562,1562,1563,1563,1563,1564,1564,1564,1565,1565,1565,1566,1566,1566,1567,1567,1567,1568,1568,1568,1569,1569,1569,1570,1570,1570,1571,1571,1571,1572,1572,1572,1573,1573,1573,1574,1574,1574,1575,1575,1575,1576,1576,1576,1577,1577,1577,1578,1578,1578,1579,1579,1579,1580,1580,1580,1581,1581,1581,1582,1582,1582,1583,1583,1583,1584,1584,1584,1585,1585,1585,1586,1586,1586,1587,1587,1587,1588,1588,1588,1589,1589,1589,1590,1590,1590,1591,1591,1591,1592,1592,1592,1593,1593,1593,1594,1594,1594,1595,1595,1595,1596,1596,1596,1597,1597,1597,1598,1598,1598,1599,1599,1599,1600,1600,1600,1601,1601,1601,1602,1602,1602,1603,1603,1603,1604,1604,1604,1605,1605,1605,1606,1606,1606,1607,1607,1607,1608,1608,1608,1609,1609,1609,1610,1610,1610,1611,1611,1611,1612,1612,1612,1613,1613,1613,1614,1614,1614,1615,1615,1615,1616,1616,1616,1617,1617,1617,1618,1618,1618,1619,1619,1619,1620,1620,1620,1621,1621,1621,1622,1622,1622,1623,1623,1623,1624,1624,1624,1625,1625,1625,1626,1626,1626,1627,1627,1627,1628,1628,1628,1629,1629,1629,1630,1630,1630,1631,1631,1631,1632,1632,1632,1633,1633,1633,1634,1634,1635,1635,1636,1636,1637,1637,1638,1638,1639,1640,1640,1641,1641,1642,1643,1644,1644,1645,1645,1646,1646,1646,1647,1648,1648,1649,1650,1650,1651,1651,1652,1653,1653,1654,1654,1655,1655,1656,1656,1657,1657,1657,1658,1659,1659,1660,1660,1661,1661,1662,1663,1663,1663,1664,1665,1666,1667,1668,1668,1669,1669,1669,1670,1671,1671,1672,1672,1672,1673,1673,1673,1674,1674,1674,1675,1676,1677,1678,1678,1679,1680,1680,1681,1681,1682,1683,1683,1684,1684,1685,1685,1686,1687,1688,1688,1688,1689,1689,1690,1690,1691,1692,1692,1692,1693,1693,1693,1694,1695,1696,1696,1697,1697,1698,1699,1699,1699,1700,1700,1701,1701,1702,1702,1703,1703,1704,1705,1705,1706,1706,1707,1707,1707,1708,1708,1708,1709,1709,1709,1710,1710,1710,1711,1711,1712,1712,1713,1714,1714,1715,1715,1716,1716,1717,1718,1719,1719,1719,1720,1720,1721,1722,1722,1723,1724,1724,1724,1725,1726,1726,1727,1727,1728,1728,1729,1729,1730,1730,1731,1732,1733,1733,1734,1734,1735,1735,1736,1736,1737,1737,1738,1739,1740,1741,1741,1742,1742,1743,1743,1744,1744,1744,1745,1745,1745,1746,1746,1746,1747,1747,1748,1749,1749,1750,1751,1752,1753,1754,1755,1756,1756,1757,1757,1758,1758,1759,1759,1760,1761,1761,1762,1763,1763,1764,1765,1765,1766,1767,1767,1768,1768,1769,1770,1770,1771,1771,1772,1772,1773,1773,1774,1774,1775,1776,1776,1777,1777,1778,1778,1778,1779,1779,1780,1780,1780,1781,1781,1781,1782,1782,1782,1783,1783,1784,1784,1785,1785,1786,1786,1787,1788,1789,1790,1791,1791,1791,1792,1792,1793,1793,1794,1794,1795,1795,1796,1796,1797,1797,1798,1798,1798,1799,1800,1801,1802,1803,1804,1804,1805,1806,1807,1807,1808,1808,1809,1809,1810,1810,1811,1812,1813,1814,1814,1815,1815,1816,1816,1816,1817,1817,1817,1818,1818,1818,1819,1819,1820,1821,1821,1822,1822,1823,1823,1824,1825,1825,1825,1826,1826,1827,1827,1828,1828,1829,1830,1830,1831,1832,1832,1833,1833,1834,1834,1835,1835,1836,1836,1837,1837,1838,1839,1839,1839,1840,1840,1841,1842,1842,1842,1843,1843,1844,1844,1845,1845,1846,1847,1847,1848,1849,1850,1850,1851,1851,1851,1852,1852,1852,1853,1853,1853,1854,1855,1855,1856,1857,1858,1859,1859,1860,1860,1861,1861,1862,1863,1863,1864,1864,1865,1865,1866,1867,1868,1869,1870,1871,1871,1872,1872,1873,1874,1875,1876,1877,1877,1878,1878,1879,1879,1879,1880,1880,1881,1882,1883,1883,1884,1885,1885,1886,1886,1887,1887,1888,1888,1889,1889,1890,1890,1891,1891,1892,1892,1893,1893,1894,1894,1895,1895,1896,1896,1897,1897,1898,1898,1899,1899,1900,1900,1901,1901,1901,1902,1902,1903,1903,1904,1904,1905,1906,1906,1907,1908,1908,1909,1909,1910,1911,1911,1912,1912,1912,1913,1913,1914,1915,1915,1916,1916,1917,1918,1918,1919,1919,1920,1921,1922,1923,1924,1924,1925,1926,1926,1926,1927,1927,1928,1929,1929,1929,1930,1930,1930,1931,1931,1931,1932,1932,1932,1933,1934,1935,1935,1936,1937,1937,1938,1939,1940,1941,1942,1942,1943,1943,1944,1945,1945,1946,1946,1947,1948,1949,1950,1950,1951,1951,1951,1952,1952,1953,1954,1954,1955,1955,1956,1956,1956,1957,1958,1958,1959,1960,1961,1961,1962,1963,1963,1964,1964,1965,1965,1966,1967,1968,1968,1969,1970,1970,1971,1972,1972,1973,1974,1975,1975,1976,1976,1977,1977,1977,1978,1978,1978,1979,1979,1980,1980,1981,1981,1982,1982,1983,1983,1984,1984,1985,1985,1986,1986,1987,1987,1988,1988,1989,1989,1990,1990,1991,1992,1992,1993,1993,1994,1994,1995,1995,1996,1996,1997,1997,1998,1998,1999,1999,2000,2000,2001,2001,2002,2002,2003,2003,2004,2004,2005,2005,2006,2006,2007,2007,2008,2008,2009,2009,2010,2010,2011,2011,2012,2012,2013,2013,2014,2014,2015,2015,2016,2016,2016,2016,2016,2016,2016,2016,2017,2017,2017,2017,2017,2017,2017,2017,2018,2018,2018,2018,2018,2018,2018,2018,2019,2019,2019,2019,2019,2019,2019,2019,2020,2020,2020,2020,2020,2020,2020,2020,2021,2021,2021,2021,2021,2021,2021,2021,2022,2022,2022,2022,2022,2022,2022,2022,2023,2023,2023,2023,2023,2023,2023,2023,2024,2024,2024,2024,2024,2024,2024,2024,2025,2025,2025,2025,2025,2025,2025,2025,2026,2026,2026,2026,2026,2026,2026,2026,2027,2027,2027,2027,2027,2027,2027,2027,2028,2028,2028,2028,2028,2028,2028,2028,2029,2029,2029,2029,2029,2029,2029,2029,2030,2030,2030,2030,2030,2030,2030,2030,2031,2031,2031,2031,2031,2031,2031,2031,2032,2032,2032,2032,2032,2032,2032,2032,2033,2033,2033,2033,2033,2033,2033,2033,2034,2034,2034,2034,2034,2034,2034,2034,2035,2035,2035,2035,2035,2035,2035,2035,2036,2036,2036,2036,2036,2036,2036,2036,2037,2037,2037,2037,2037,2037,2037,2037,2038,2038,2038,2038,2038,2038,2038,2038,2039,2039,2039,2039,2039,2039,2039,2039,2040,2040,2040,2040,2040,2040,2040,2040,2041,2041,2041,2041,2041,2041,2041,2041,2042,2042,2042,2042,2042,2042,2042,2042,2043,2043,2043,2043,2043,2043,2043,2043,2044,2044,2044,2044,2044,2044,2044,2044,2045,2045,2045,2045,2045,2045,2045,2045,2046,2046,2046,2046,2046,2046,2046,2046,2047,2047,2047,2047,2047,2047,2047,2047],"depth":[1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,4,3,2,1,2,1,1,1,3,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,1,3,2,1,1,2,1,3,2,1,1,2,1,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,1,2,1,1,3,2,1,2,1,2,1,1,2,1,2,1,1,2,1,1,1,2,1,1,1,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,1,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,1,3,2,1,1,2,1,1,2,1,1,1,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,1,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,3,2,1,1,2,1,2,1,3,2,1,3,2,1,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,1,3,2,1,1,2,1,1,3,2,1,2,1,1,2,1,3,2,1,1,1,1,2,1,3,2,1,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,1,1,1,2,1,2,1,3,2,1,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,1,2,1,3,2,1,2,1,1,2,1,1,3,2,1,1,1,2,1,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,1,3,2,1,3,2,1,1,3,2,1,2,1,2,1,2,1,3,2,1,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,3,2,1,1,2,1,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,1,2,1,1,3,2,1,2,1,1,2,1,2,1,2,1,1,2,1,3,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,1,1,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,3,2,1,2,1,2,1,1,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,3,2,1,2,1,1,3,2,1,2,1,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,3,2,1,2,1,2,1,3,2,1,1,1,2,1,2,1,2,1,3,2,1,1,2,1,1,2,1,1,2,1,1,3,2,1,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,1,1,1,2,1,2,1,3,2,1,2,1,2,1,1,1,2,1,1,2,1,2,1,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,2,1,2,1,1,2,1,1,2,1,1,1,3,2,1,3,2,1,2,1,2,1,1,2,1,1,1,2,1,2,1,3,2,1,3,2,1,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,3,2,1,1,1,2,1,2,1,2,1,2,1,1,2,1,1,1,1,1,2,1,3,2,1,2,1,2,1,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,4,3,2,1,4,3,2,1,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,1,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,3,2,1,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,1,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,2,1,2,1,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,1,1,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,1,2,1,1,2,1,1,1,3,2,1,3,2,1,3,2,1,2,1,3,2,1,2,1,2,1,3,2,1,1,2,1,1,3,2,1,1,1,2,1,3,2,1,1,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,1,3,2,1,2,1,2,1,3,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,1,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,1,1,2,1,2,1,2,1,1,2,1,1,2,1,1,2,1,2,1,3,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,1,1,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,1,2,1,1,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,1,1,2,1,1,2,1,3,2,1,2,1,1,1,3,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,1,2,1,1,2,1,2,1,1,1,2,1,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,1,2,1,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,1,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,1,1,2,1,2,1,1,1,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,1,1,2,1,1,2,1,2,1,1,3,2,1,3,2,1,1,2,1,2,1,1,1,2,1,2,1,1,2,1,2,1,1,2,1,1,3,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,1,2,1,2,1,2,1,2,1,3,2,1,2,1,3,2,1,3,2,1,2,1,2,1,3,2,1,2,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,1,1,2,1,2,1,2,1,1,1,3,2,1,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,1,2,1,1,3,2,1,2,1,1,1,2,1,1,2,1,1,2,1,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,3,2,1,1,2,1,1,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,3,2,1,3,2,1,2,1,2,1,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,3,2,1,3,2,1,3,2,1,2,1,1,2,1,1,2,1,1,3,2,1,2,1,2,1,2,1,3,2,1,2,1,1,3,2,1,3,2,1,1,3,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,1,1,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,1,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,1,2,1,1,1,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,1,1,2,1,1,3,2,1,3,2,1,1,2,1,2,1,1,2,1,3,2,1,2,1,1,1,1,2,1,2,1,3,2,1,3,2,1,2,1,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,1,1,1,1,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,1,2,1,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,1,2,1,1,1,2,1,3,2,1,2,1,1,1,3,2,1,2,1,1,3,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,1,1,1,3,2,1,1,3,2,1,3,2,1,3,2,1,2,1,2,1,3,2,1,2,1,1,1,2,1,2,1,2,1,1,4,3,2,1,4,3,2,1,4,3,2,1,2,1,2,1,1,2,1,2,1,1,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,3,2,1,3,2,1,2,1,2,1,1,2,1,2,1,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,1,1,2,1,3,2,1,2,1,1,1,2,1,2,1,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,1,2,1,2,1,2,1,1,2,1,3,2,1,3,2,1,2,1,1,3,2,1,1,2,1,3,2,1,1,1,1,1,2,1,3,2,1,3,2,1,1,1,2,1,2,1,1,2,1,1,1,1,3,2,1,2,1,3,2,1,3,2,1,3,2,1,1,2,1,1,1,1,1,2,1,2,1,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,1,3,2,1,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,1,3,2,1,3,2,1,2,1,1,2,1,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,1,2,1,2,1,3,2,1,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,1,3,2,1,1,1,1,1,2,1,3,2,1,1,2,1,3,2,1,3,2,1,3,2,1,1,1,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,1,1,3,2,1,2,1,2,1,1,3,2,1,3,2,1,1,1,2,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,1,1,3,2,1,2,1,1,2,1,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,1,1,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,1,2,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,1,1,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,1,1,1,1,2,1,1,1,2,1,2,1,2,1,2,1,1,1,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,1,3,2,1,2,1,2,1,2,1,1,2,1,1,1,2,1,3,2,1,3,2,1,3,2,1,1,2,1,1,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,1,1,1,1,2,1,2,1,1,1,1,1,2,1,2,1,3,2,1,2,1,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,1,2,1,3,2,1,2,1,1,2,1,2,1,1,2,1,2,1,1,1,1,1,2,1,1,3,2,1,2,1,1,3,2,1,3,2,1,3,2,1,3,2,1,1,1,2,1,1,2,1,1,1,1,1,2,1,2,1,1,2,1,2,1,1,1,1,2,1,3,2,1,2,1,1,2,1,2,1,3,2,1,1,2,1,1,1,2,1,1,2,1,2,1,2,1,1,1,2,1,1,2,1,1,2,1,1,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1],"label":["rowSums","rowSums","rowSums","rowSums","rowSums","rowSums","rowMeans","rowMeans","rowMeans","rowMeans","rowMeans","rowMeans","aperm.default","apply","aperm.default","apply","aperm.default","apply","aperm.default","apply","aperm.default","apply","aperm.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","length","local","<GC>","isTRUE","mean.default","apply","mean.default","apply","apply","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","is.numeric","local","apply","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","apply","<GC>","mean.default","apply","apply","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","<GC>","length","local","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","apply","mean.default","apply","apply","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","mean.default","apply","FUN","apply","apply","apply","mean.default","apply","apply","FUN","apply","FUN","apply","is.na","local","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","apply","<GC>","apply","is.na","local","FUN","apply","is.numeric","local","FUN","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","apply","apply","<GC>","mean.default","apply","apply","FUN","apply","apply","mean.default","apply","apply","apply","apply","FUN","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","<GC>","is.numeric","local","mean.default","apply","FUN","apply","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","<GC>","apply","apply","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","is.numeric","local","mean.default","apply","apply","FUN","apply","length","local","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","mean.default","apply","<GC>","is.na","local","<GC>","is.na","local","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","<GC>","mean.default","apply","apply","FUN","apply","apply","isTRUE","mean.default","apply","mean.default","apply","apply","mean.default","apply","isTRUE","mean.default","apply","apply","apply","apply","FUN","apply","<GC>","length","local","apply","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","<GC>","length","local","<GC>","length","local","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","length","local","apply","apply","apply","FUN","apply","mean.default","apply","<GC>","mean.default","apply","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","<GC>","apply","isTRUE","mean.default","apply","mean.default","apply","apply","length","local","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","<GC>","apply","<GC>","apply","FUN","apply","is.numeric","local","length","local","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","length","local","mean.default","apply","apply","apply","<GC>","mean.default","apply","isTRUE","mean.default","apply","apply","isTRUE","mean.default","apply","mean.default","apply","length","local","mean.default","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","apply","apply","is.numeric","local","isTRUE","mean.default","apply","apply","FUN","apply","apply","FUN","apply","mean.default","apply","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","FUN","apply","mean.default","apply","apply","length","local","apply","length","local","apply","isTRUE","mean.default","apply","mean.default","apply","apply","<GC>","apply","<GC>","apply","length","local","apply","length","local","isTRUE","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","<GC>","apply","apply","is.na","local","FUN","apply","FUN","apply","apply","apply","apply","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","FUN","apply","mean.default","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","is.na","local","isTRUE","mean.default","apply","mean.default","apply","apply","isTRUE","mean.default","apply","mean.default","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","length","local","mean.default","apply","isTRUE","mean.default","apply","apply","<GC>","apply","apply","mean.default","apply","apply","mean.default","apply","apply","isTRUE","mean.default","apply","mean.default","apply","apply","FUN","apply","<GC>","apply","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","apply","mean.default","apply","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","mean.default","apply","apply","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","length","local","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","<GC>","is.numeric","local","<GC>","is.numeric","local","mean.default","apply","mean.default","apply","apply","FUN","apply","apply","mean.default","apply","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","is.na","local","apply","mean.default","apply","apply","apply","mean.default","apply","length","local","<GC>","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","<GC>","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","mean.default","apply","FUN","apply","FUN","apply","apply","FUN","apply","mean.default","apply","FUN","apply","<GC>","mean.default","apply","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","<GC>","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","<GC>","apply","<GC>","apply","FUN","apply","apply","apply","length","local","apply","mean.default","apply","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","apply","apply","length","local","FUN","apply","apply","FUN","apply","is.numeric","local","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","length","local","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","apply","is.na","local","FUN","apply","length","local","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","apply","apply","apply","FUN","apply","FUN","apply","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","<GC>","is.na","local","<GC>","is.na","local","mean.default","apply","FUN","apply","apply","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","mean.default","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","mean.default","apply","is.na","local","apply","apply","apply","apply","<GC>","apply","<GC>","apply","FUN","apply","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","length","local","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","is.numeric","local","apply","is.numeric","local","apply","apply","apply","isTRUE","mean.default","apply","apply","is.na","local","FUN","apply","mean.default","apply","<GC>","apply","<GC>","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","FUN","apply","is.numeric","local","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","apply","mean.default","apply","apply","mean.default","apply","apply","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","is.numeric","local","isTRUE","mean.default","apply","apply","is.na","local","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","apply","FUN","apply","<GC>","apply","<GC>","apply","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","mean.default","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","length","local","mean.default","apply","length","local","mean.default","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","FUN","apply","length","local","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","length","local","length","local","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","length","local","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","length","local","FUN","apply","apply","apply","mean.default","apply","is.numeric","local","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","mean.default","apply","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","apply","apply","apply","is.na","local","FUN","apply","FUN","apply","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","FUN","apply","<GC>","apply","<GC>","apply","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","apply","apply","FUN","apply","apply","mean.default","apply","apply","FUN","apply","<GC>","apply","<GC>","apply","FUN","apply","mean.default","apply","apply","apply","apply","mean.default","apply","apply","is.na","local","isTRUE","mean.default","apply","mean.default","apply","apply","apply","isTRUE","mean.default","apply","mean.default","apply","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","apply","apply","mean.default","apply","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","mean.default","apply","apply","FUN","apply","length","local","apply","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","mean.default","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","apply","apply","length","local","FUN","apply","apply","apply","apply","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","is.numeric","local","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","apply","apply","mean.default","apply","apply","mean.default","apply","mean.default","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","is.na","local","mean.default","apply","apply","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","<GC>","apply","<GC>","apply","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","is.na","local","<GC>","apply","<GC>","apply","<GC>","apply","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","apply","apply","FUN","apply","is.numeric","local","is.na","local","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","is.na","local","apply","isTRUE","mean.default","apply","mean.default","apply","is.na","local","FUN","apply","FUN","apply","FUN","apply","apply","mean.default","apply","FUN","apply","<GC>","apply","<GC>","apply","apply","FUN","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","apply","FUN","apply","is.na","local","FUN","apply","length","local","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","FUN","apply","apply","isTRUE","mean.default","apply","is.numeric","local","apply","apply","mean.default","apply","apply","FUN","apply","apply","mean.default","apply","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","apply","<GC>","apply","<GC>","apply","mean.default","apply","FUN","apply","is.na","local","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","is.numeric","local","isTRUE","mean.default","apply","mean.default","apply","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","FUN","apply","apply","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","mean.default","apply","<GC>","is.na","local","<GC>","is.na","local","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","apply","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","is.numeric","local","mean.default","apply","isTRUE","mean.default","apply","length","local","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","apply","apply","<GC>","apply","<GC>","apply","apply","is.na","local","FUN","apply","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","apply","mean.default","apply","apply","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","length","local","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","mean.default","apply","is.numeric","local","is.na","local","length","local","isTRUE","mean.default","apply","mean.default","apply","apply","FUN","apply","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","mean.default","apply","apply","apply","FUN","apply","is.na","local","FUN","apply","apply","mean.default","apply","apply","apply","apply","<GC>","apply","<GC>","apply","isTRUE","mean.default","apply","length","local","FUN","apply","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","apply","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","mean.default","apply","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","apply","mean.default","apply","FUN","apply","<GC>","is.numeric","local","<GC>","is.numeric","local","FUN","apply","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","length","local","FUN","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","<GC>","apply","<GC>","apply","is.na","local","mean.default","apply","apply","apply","apply","apply","apply","apply","apply","is.numeric","local","is.na","local","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","length","local","mean.default","apply","mean.default","apply","apply","apply","is.na","local","FUN","apply","mean.default","apply","apply","FUN","apply","FUN","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","apply","FUN","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","length","local","apply","apply","isTRUE","mean.default","apply","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","apply","apply","FUN","apply","FUN","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","FUN","apply","apply","apply","apply","isTRUE","mean.default","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","mean.default","apply","FUN","apply","FUN","apply","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","mean.default","apply","length","local","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","apply","is.na","local","length","local","apply","FUN","apply","apply","FUN","apply","apply","FUN","apply","<GC>","apply","<GC>","apply","FUN","apply","apply","apply","is.numeric","local","isTRUE","mean.default","apply","FUN","apply","apply","apply","mean.default","apply","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","mean.default","apply","length","local","is.numeric","local","apply","FUN","apply","apply","apply","mean.default","apply","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","FUN","apply","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","length","local","apply","isTRUE","mean.default","apply","apply","length","local","isTRUE","mean.default","apply","apply","apply","apply","apply","length","local","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","apply","mean.default","apply","FUN","apply","apply","FUN","apply","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","apply","apply","apply","mean.default","apply","mean.default","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","is.na","local","apply","FUN","apply","length","local","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","apply","FUN","apply","is.na","local","length","local","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","is.numeric","local","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","is.numeric","local","apply","mean.default","apply","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","apply","mean.default","apply","FUN","apply","apply","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","is.numeric","local","mean.default","apply","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","apply","apply","mean.default","apply","apply","FUN","apply","is.numeric","local","apply","mean.default","apply","FUN","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","mean.default","apply","length","local","FUN","apply","FUN","apply","apply","mean.default","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","FUN","apply","apply","length","local","mean.default","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","apply","mean.default","apply","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","apply","apply","apply","mean.default","apply","mean.default","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","is.na","local","apply","apply","apply","apply","apply","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","FUN","apply","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","is.numeric","local","FUN","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","apply","apply","apply","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","apply","apply","apply","FUN","apply","apply","apply","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","apply","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","is.na","local","mean.default","apply","mean.default","apply","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","is.na","local","apply","mean.default","apply","apply","FUN","apply","is.numeric","local","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","is.na","local","mean.default","apply","apply","FUN","apply","apply","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","apply","apply","apply","mean.default","apply","FUN","apply","FUN","apply","apply","length","local","mean.default","apply","FUN","apply","apply","apply","apply","apply","apply","FUN","apply","mean.default","apply","apply","apply","apply","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","length","local","apply","FUN","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","FUN","apply","is.numeric","local","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","apply","apply","apply","FUN","apply","apply","isTRUE","mean.default","apply","mean.default","apply","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","apply","FUN","apply","apply","FUN","apply","apply","apply","apply","apply","FUN","apply","mean.default","apply","apply","FUN","apply","FUN","apply","apply","apply","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","apply","length","local","apply","<GC>","apply","<GC>","apply","<GC>","apply","apply","apply","FUN","apply","apply","FUN","apply","apply","mean.default","apply","apply","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","apply","any","local","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","lapply","FUN","lapply","findLocalsList1","findLocalsList","findLocals","compile","compiler:::tryCompile","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis"],"filenum":[1,1,1,1,1,1,1,1,1,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,null,null,null,null,1,null,1,1,1,null,null,1,null,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,1,1,null,null,1,1,null,1,null,null,1,1,null,1,1,null,1,1,null,1,null,1,null,1,1,null,1,null,1,null,null,null,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,1,1,null,1,1,null,null,1,null,1,null,1,1,null,1,null,1,1,null,1,1,1,null,1,1,1,null,1,null,null,1,null,null,1,null,1,1,null,1,null,1,1,1,null,1,1,null,1,null,1,null,null,null,1,null,null,1,null,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,1,1,null,1,null,1,null,null,1,null,1,null,1,null,null,null,1,null,null,null,1,1,null,1,null,1,null,1,null,1,null,1,1,1,null,null,1,1,null,1,1,null,1,1,1,1,null,1,1,null,1,null,1,null,1,null,1,null,null,null,null,1,null,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,1,1,1,null,1,1,null,1,null,1,null,null,null,1,1,null,1,null,null,null,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,null,1,1,null,1,null,1,null,null,null,null,null,null,1,null,1,null,1,1,null,1,1,null,1,null,1,null,1,null,1,1,null,null,1,1,null,1,1,null,null,1,null,1,1,null,1,null,null,1,1,1,1,null,1,null,null,null,1,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,null,null,null,null,null,1,null,1,null,1,null,1,null,1,null,null,1,1,1,null,1,null,1,null,null,1,1,null,null,1,null,1,null,1,1,null,1,null,1,null,1,null,null,1,null,null,1,1,null,1,null,null,1,null,1,1,null,null,1,null,null,1,1,1,null,1,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,null,null,null,1,null,null,1,null,1,null,null,null,1,1,1,null,null,1,null,null,1,1,null,null,1,null,1,null,null,null,1,null,null,1,1,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,1,null,null,null,null,1,1,null,1,1,null,1,null,1,1,null,1,null,1,null,null,1,null,1,null,1,1,null,null,1,null,null,1,null,null,1,null,1,1,null,1,null,1,null,null,1,null,null,null,null,1,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,1,null,null,null,1,null,1,1,1,1,1,null,1,null,1,null,null,1,null,1,null,1,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,null,1,null,1,null,1,1,1,null,1,null,1,null,1,null,null,1,null,1,1,null,null,null,null,1,null,1,1,null,null,1,null,1,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,1,1,null,1,null,1,null,null,1,null,1,null,1,null,null,1,1,1,null,1,null,null,null,1,null,null,1,1,null,1,1,null,1,1,null,1,1,null,null,1,null,1,1,null,1,null,1,null,1,null,null,1,null,null,1,null,1,1,1,1,null,1,null,1,null,null,1,null,1,null,1,1,1,null,1,1,null,1,null,1,1,null,null,1,null,null,1,null,null,null,1,null,1,null,1,null,1,null,1,null,1,1,null,null,null,null,null,null,null,1,null,1,1,null,1,1,null,1,1,1,null,null,1,null,null,1,null,1,null,null,1,null,1,1,1,null,1,null,null,null,null,1,null,null,1,1,null,1,null,1,null,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,null,1,null,null,1,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,null,1,1,null,1,null,1,1,null,1,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,1,null,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,null,1,1,1,null,1,null,1,null,1,null,1,1,null,1,1,1,1,1,null,1,null,null,1,null,1,null,1,1,null,1,null,null,1,null,null,1,null,1,null,1,null,1,1,1,null,null,null,1,1,null,1,null,null,null,null,1,null,1,null,1,null,1,null,1,null,null,null,1,null,1,null,1,null,1,null,null,null,1,null,null,null,1,1,null,null,null,1,null,null,null,1,null,null,1,null,1,1,1,1,null,1,null,1,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,null,null,null,null,null,null,1,null,1,1,null,1,null,null,1,1,null,1,null,1,1,null,1,null,1,1,null,1,null,1,null,1,null,null,1,1,1,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,1,null,1,null,1,null,1,null,1,null,null,1,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,1,1,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,null,1,null,1,null,1,1,null,null,1,null,null,1,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,null,1,null,null,1,1,1,null,null,1,1,null,null,null,1,null,1,null,1,null,1,null,null,1,null,null,1,1,null,1,null,1,null,1,null,null,1,null,1,null,1,1,null,1,1,null,1,1,null,1,1,1,null,null,1,null,null,1,null,null,1,null,1,null,null,1,null,1,null,null,null,null,1,1,null,null,1,null,null,1,1,1,null,1,null,null,1,1,null,1,null,null,1,null,1,1,null,1,null,1,null,1,null,1,1,null,null,1,null,1,1,null,null,1,null,1,null,1,null,null,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,1,null,1,null,1,null,1,1,null,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,1,null,1,null,1,1,null,1,null,1,null,null,1,null,null,1,null,1,1,null,1,null,1,null,1,1,null,null,null,1,null,null,null,1,null,1,null,1,1,null,1,null,1,null,1,null,null,null,1,null,null,1,null,null,1,null,1,null,null,null,null,1,1,1,null,1,null,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,null,1,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,null,null,1,1,1,null,1,null,null,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,1,1,null,1,null,1,null,1,1,null,1,1,null,1,1,null,1,null,1,null,null,1,null,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,1,1,1,1,1,null,null,null,1,null,1,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,1,1,null,1,null,1,1,null,1,1,1,null,1,1,null,1,1,null,1,null,1,null,1,null,1,null,1,1,1,1,null,1,1,null,null,null,null,1,null,1,1,1,null,null,1,null,1,1,null,1,null,1,null,null,1,null,null,1,1,null,1,1,null,1,null,1,1,1,null,1,1,null,null,1,null,1,null,1,1,null,1,null,1,null,1,null,null,1,null,null,1,1,null,1,1,null,1,null,null,1,null,1,null,1,1,null,1,null,1,1,1,null,1,null,1,null,1,null,null,1,null,null,1,null,1,null,1,1,1,null,null,null,1,1,1,1,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,1,null,1,1,1,null,1,1,null,1,null,1,1,null,null,1,null,null,1,1,null,null,null,1,1,1,null,1,null,1,1,null,1,null,1,1,null,1,1,null,null,1,null,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,1,1,null,1,null,null,null,null,null,1,null,null,1,null,1,null,null,1,null,null,1,null,1,null,1,null,null,1,null,1,null,null,1,null,null,1,null,1,null,null,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,1,null,1,1,1,null,1,null,1,null,1,1,1,null,null,1,1,null,1,null,null,null,1,null,null,null,null,1,null,null,1,1,null,1,1,null,null,1,null,null,1,1,null,1,1,null,1,1,null,1,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,1,1,null,null,1,1,null,1,1,1,null,1,null,1,null,null,1,1,null,1,null,1,null,1,null,1,null,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,null,null,1,null,1,1,null,1,null,null,1,null,null,1,null,1,null,1,1,1,null,1,1,null,1,null,1,null,1,null,1,null,1,1,1,null,1,null,null,null,null,null,null,null,null,1,null,1,1,null,1,1,null,1,1,null,null,1,null,1,null,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,1,null,null,1,null,1,null,1,null,1,1,1,null,1,null,1,null,1,1,1,1,null,1,null,1,1,null,null,null,1,1,null,1,null,1,null,1,null,1,null,1,null,null,1,1,null,1,null,1,null,1,null,null,1,null,null,1,1,1,null,1,1,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,null,1,null,null,1,1,null,1,null,null,null,null,null,null,null,null,1,null,1,1,null,1,1,null,1,1,null,1,null,1,null,1,null,1,null,1,1,1,null,1,null,null,null,1,1,null,1,1,1,1,null,1,null,1,null,null,1,null,null,null,1,1,null,1,null,1,null,1,null,1,1,1,1,null,1,1,null,null,1,null,null,1,1,null,1,null,1,1,null,1,null,null,1,null,1,1,1,1,null,1,null,1,null,null,null,null,null,null,null,1,1,null,null,1,null,null,1,null,null,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,null,null,1,1,1,1,1,1,1,1,null,null,null,null,null,1,null,null,1,null,null,1,null,null,null,1,null,1,1,1,null,null,null,1,null,1,1,null,1,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,1,null,1,1,1,null,1,null,null,1,null,null,1,1,null,null,1,null,1,1,null,null,1,null,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,1,1,null,1,null,1,1,1,1,null,null,1,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,null,1,null,1,1,1,null,1,null,1,null,1,1,null,null,null,1,null,null,null,1,null,null,null,1,null,1,null,1,1,null,1,null,1,1,1,null,1,null,1,null,null,null,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,1,null,null,1,null,null,1,null,1,null,1,1,null,null,null,null,1,null,1,1,null,1,1,null,1,null,1,null,1,null,1,1,1,null,null,null,null,1,null,1,1,1,null,1,null,1,1,null,null,1,null,null,1,null,1,null,1,null,null,null,null,1,null,1,1,1,null,1,1,null,1,null,1,null,1,null,1,null,1,1,null,null,1,1,null,1,null,1,null,1,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,1,null,null,null,null,1,1,1,1,1,null,null,null,null,1,null,null,1,1,1,null,1,null,1,1,null,1,1,1,1,null,null,1,null,1,null,null,1,null,null,1,null,null,1,1,null,1,1,1,1,1,null,1,null,1,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,null,1,null,1,null,null,1,null,null,1,null,1,null,null,1,null,null,1,null,1,1,null,1,null,null,null,null,1,null,1,null,1,null,null,1,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,1,1,null,1,null,1,null,null,1,1,null,1,1,null,null,null,1,1,null,1,null,1,null,1,null,1,null,null,1,1,null,1,null,1,null,1,1,null,null,1,1,1,1,1,null,1,null,null,1,1,null,1,null,null,1,null,null,1,null,null,1,1,1,1,null,1,1,null,1,null,null,1,null,1,null,1,null,1,1,1,null,null,1,null,1,null,1,1,null,null,1,null,null,1,1,1,null,1,null,1,1,null,null,1,null,1,null,null,null,1,null,1,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,1,null,null,null,1,null,1,1,1,null,null,1,null,1,1,null,1,1,null,null,1,1,null,1,null,1,null,1,null,1,null,1,1,1,null,1,null,1,null,1,null,1,null,1,1,1,1,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,1,1,null,null,1,1,1,1,1,1,null,1,null,1,null,1,null,1,1,null,1,1,null,1,1,null,1,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,1,null,null,null,1,null,null,1,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,1,1,1,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,1,1,1,1,1,null,1,1,1,null,1,null,1,null,1,null,1,1,1,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,1,1,null,null,null,1,null,1,1,null,null,1,null,1,null,1,null,null,1,null,1,1,null,1,null,null,null,1,null,1,null,1,null,1,1,null,null,1,null,1,1,null,null,1,null,1,null,null,null,1,1,null,1,1,1,null,1,null,null,1,null,null,1,null,null,1,1,null,1,1,1,1,null,1,null,1,null,1,1,null,null,null,1,null,1,1,1,1,1,1,null,1,null,1,1,1,1,1,null,1,null,1,null,null,1,null,1,1,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,1,null,1,1,null,1,null,null,1,null,1,null,null,1,null,1,1,null,1,null,1,1,null,1,null,1,1,1,1,1,null,1,1,null,null,1,null,1,1,null,null,1,null,null,1,null,null,1,null,null,1,1,1,null,1,1,null,1,1,1,1,1,null,1,null,1,1,null,1,null,1,1,1,1,null,1,null,null,1,null,1,1,null,1,null,1,null,null,1,1,null,1,1,1,null,null,1,null,1,null,1,null,1,1,1,null,1,1,null,1,1,null,1,1,1,null,1,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,null,null,null,null,null,null,null,null,null,null,null,null,null,1,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null],"linenum":[10,10,10,10,10,10,11,11,11,11,11,11,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,null,null,null,null,12,null,12,12,12,null,null,12,null,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,12,12,null,null,12,12,null,12,null,null,12,12,null,12,12,null,12,12,null,12,null,12,null,12,12,null,12,null,12,null,null,null,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,12,12,null,12,12,null,null,12,null,12,null,12,12,null,12,null,12,12,null,12,12,12,null,12,12,12,null,12,null,null,12,null,null,12,null,12,12,null,12,null,12,12,12,null,12,12,null,12,null,12,null,null,null,12,null,null,12,null,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,12,12,null,12,null,12,null,null,12,null,12,null,12,null,null,null,12,null,null,null,12,12,null,12,null,12,null,12,null,12,null,12,12,12,null,null,12,12,null,12,12,null,12,12,12,12,null,12,12,null,12,null,12,null,12,null,12,null,null,null,null,12,null,12,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,12,12,12,null,12,12,null,12,null,12,null,null,null,12,12,null,12,null,null,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,null,12,12,null,12,null,12,null,null,null,null,null,null,12,null,12,null,12,12,null,12,12,null,12,null,12,null,12,null,12,12,null,null,12,12,null,12,12,null,null,12,null,12,12,null,12,null,null,12,12,12,12,null,12,null,null,null,12,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,null,null,null,null,null,12,null,12,null,12,null,12,null,12,null,null,12,12,12,null,12,null,12,null,null,12,12,null,null,12,null,12,null,12,12,null,12,null,12,null,12,null,null,12,null,null,12,12,null,12,null,null,12,null,12,12,null,null,12,null,null,12,12,12,null,12,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,null,null,null,12,null,null,12,null,12,null,null,null,12,12,12,null,null,12,null,null,12,12,null,null,12,null,12,null,null,null,12,null,null,12,12,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,12,null,null,null,null,12,12,null,12,12,null,12,null,12,12,null,12,null,12,null,null,12,null,12,null,12,12,null,null,12,null,null,12,null,null,12,null,12,12,null,12,null,12,null,null,12,null,null,null,null,12,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,12,null,null,null,12,null,12,12,12,12,12,null,12,null,12,null,null,12,null,12,null,12,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,null,12,null,12,null,12,12,12,null,12,null,12,null,12,null,null,12,null,12,12,null,null,null,null,12,null,12,12,null,null,12,null,12,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,12,12,null,12,null,12,null,null,12,null,12,null,12,null,null,12,12,12,null,12,null,null,null,12,null,null,12,12,null,12,12,null,12,12,null,12,12,null,null,12,null,12,12,null,12,null,12,null,12,null,null,12,null,null,12,null,12,12,12,12,null,12,null,12,null,null,12,null,12,null,12,12,12,null,12,12,null,12,null,12,12,null,null,12,null,null,12,null,null,null,12,null,12,null,12,null,12,null,12,null,12,12,null,null,null,null,null,null,null,12,null,12,12,null,12,12,null,12,12,12,null,null,12,null,null,12,null,12,null,null,12,null,12,12,12,null,12,null,null,null,null,12,null,null,12,12,null,12,null,12,null,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,null,12,null,null,12,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,null,12,12,null,12,null,12,12,null,12,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,12,null,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,null,12,12,12,null,12,null,12,null,12,null,12,12,null,12,12,12,12,12,null,12,null,null,12,null,12,null,12,12,null,12,null,null,12,null,null,12,null,12,null,12,null,12,12,12,null,null,null,12,12,null,12,null,null,null,null,12,null,12,null,12,null,12,null,12,null,null,null,12,null,12,null,12,null,12,null,null,null,12,null,null,null,12,12,null,null,null,12,null,null,null,12,null,null,12,null,12,12,12,12,null,12,null,12,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,null,null,null,null,null,null,12,null,12,12,null,12,null,null,12,12,null,12,null,12,12,null,12,null,12,12,null,12,null,12,null,12,null,null,12,12,12,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,12,null,12,null,12,null,12,null,12,null,null,12,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,12,12,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,null,12,null,12,null,12,12,null,null,12,null,null,12,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,null,12,null,null,12,12,12,null,null,12,12,null,null,null,12,null,12,null,12,null,12,null,null,12,null,null,12,12,null,12,null,12,null,12,null,null,12,null,12,null,12,12,null,12,12,null,12,12,null,12,12,12,null,null,12,null,null,12,null,null,12,null,12,null,null,12,null,12,null,null,null,null,12,12,null,null,12,null,null,12,12,12,null,12,null,null,12,12,null,12,null,null,12,null,12,12,null,12,null,12,null,12,null,12,12,null,null,12,null,12,12,null,null,12,null,12,null,12,null,null,12,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,12,null,12,null,12,null,12,12,null,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,12,null,12,null,12,12,null,12,null,12,null,null,12,null,null,12,null,12,12,null,12,null,12,null,12,12,null,null,null,12,null,null,null,12,null,12,null,12,12,null,12,null,12,null,12,null,null,null,12,null,null,12,null,null,12,null,12,null,null,null,null,12,12,12,null,12,null,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,null,12,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,null,null,12,12,12,null,12,null,null,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,12,12,null,12,null,12,null,12,12,null,12,12,null,12,12,null,12,null,12,null,null,12,null,12,12,12,null,12,null,12,null,12,null,12,null,12,null,12,12,12,12,12,12,null,null,null,12,null,12,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,12,12,null,12,null,12,12,null,12,12,12,null,12,12,null,12,12,null,12,null,12,null,12,null,12,null,12,12,12,12,null,12,12,null,null,null,null,12,null,12,12,12,null,null,12,null,12,12,null,12,null,12,null,null,12,null,null,12,12,null,12,12,null,12,null,12,12,12,null,12,12,null,null,12,null,12,null,12,12,null,12,null,12,null,12,null,null,12,null,null,12,12,null,12,12,null,12,null,null,12,null,12,null,12,12,null,12,null,12,12,12,null,12,null,12,null,12,null,null,12,null,null,12,null,12,null,12,12,12,null,null,null,12,12,12,12,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,12,null,12,12,12,null,12,12,null,12,null,12,12,null,null,12,null,null,12,12,null,null,null,12,12,12,null,12,null,12,12,null,12,null,12,12,null,12,12,null,null,12,null,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,12,12,null,12,null,null,null,null,null,12,null,null,12,null,12,null,null,12,null,null,12,null,12,null,12,null,null,12,null,12,null,null,12,null,null,12,null,12,null,null,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,12,null,12,12,12,null,12,null,12,null,12,12,12,null,null,12,12,null,12,null,null,null,12,null,null,null,null,12,null,null,12,12,null,12,12,null,null,12,null,null,12,12,null,12,12,null,12,12,null,12,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,12,12,null,null,12,12,null,12,12,12,null,12,null,12,null,null,12,12,null,12,null,12,null,12,null,12,null,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,null,null,12,null,12,12,null,12,null,null,12,null,null,12,null,12,null,12,12,12,null,12,12,null,12,null,12,null,12,null,12,null,12,12,12,null,12,null,null,null,null,null,null,null,null,12,null,12,12,null,12,12,null,12,12,null,null,12,null,12,null,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,12,null,null,12,null,12,null,12,null,12,12,12,null,12,null,12,null,12,12,12,12,null,12,null,12,12,null,null,null,12,12,null,12,null,12,null,12,null,12,null,12,null,null,12,12,null,12,null,12,null,12,null,null,12,null,null,12,12,12,null,12,12,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,null,12,null,null,12,12,null,12,null,null,null,null,null,null,null,null,12,null,12,12,null,12,12,null,12,12,null,12,null,12,null,12,null,12,null,12,12,12,null,12,null,null,null,12,12,null,12,12,12,12,null,12,null,12,null,null,12,null,null,null,12,12,null,12,null,12,null,12,null,12,12,12,12,null,12,12,null,null,12,null,null,12,12,null,12,null,12,12,null,12,null,null,12,null,12,12,12,12,null,12,null,12,null,null,null,null,null,null,null,12,12,null,null,12,null,null,12,null,null,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,null,null,12,12,12,12,12,12,12,12,null,null,null,null,null,12,null,null,12,null,null,12,null,null,null,12,null,12,12,12,null,null,null,12,null,12,12,null,12,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,12,null,12,12,12,null,12,null,null,12,null,null,12,12,null,null,12,null,12,12,null,null,12,null,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,12,12,null,12,null,12,null,12,null,12,null,12,null,12,12,12,null,12,null,12,12,12,12,null,null,12,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,null,12,null,12,12,12,null,12,null,12,null,12,12,null,null,null,12,null,null,null,12,null,null,null,12,null,12,null,12,12,null,12,null,12,12,12,null,12,null,12,null,null,null,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,12,null,null,12,null,null,12,null,12,null,12,12,null,null,null,null,12,null,12,12,null,12,12,null,12,null,12,null,12,null,12,12,12,null,null,null,null,12,null,12,12,12,null,12,null,12,12,null,null,12,null,null,12,null,12,null,12,null,null,null,null,12,null,12,12,12,null,12,12,null,12,null,12,null,12,null,12,null,12,12,null,null,12,12,null,12,null,12,null,12,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,12,null,null,null,null,12,12,12,12,12,null,null,null,null,12,null,null,12,12,12,null,12,null,12,12,null,12,12,12,12,null,null,12,null,12,null,null,12,null,null,12,null,null,12,12,null,12,12,12,12,12,null,12,null,12,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,null,12,null,12,null,null,12,null,null,12,null,12,null,null,12,null,null,12,null,12,12,null,12,null,null,null,null,12,null,12,null,12,null,null,12,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,12,12,null,12,null,12,null,null,12,12,null,12,12,null,null,null,12,12,null,12,null,12,null,12,null,12,null,null,12,12,null,12,null,12,null,12,12,null,null,12,12,12,12,12,null,12,null,null,12,12,null,12,null,null,12,null,null,12,null,null,12,12,12,12,null,12,12,null,12,null,null,12,null,12,null,12,null,12,12,12,null,null,12,null,12,null,12,12,null,null,12,null,null,12,12,12,null,12,null,12,12,null,null,12,null,12,null,null,null,12,null,12,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,12,null,null,null,12,null,12,12,12,null,null,12,null,12,12,null,12,12,null,null,12,12,null,12,null,12,null,12,null,12,null,12,12,12,null,12,null,12,null,12,null,12,null,12,12,12,12,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,12,12,null,null,12,12,12,12,12,12,null,12,null,12,null,12,null,12,12,null,12,12,null,12,12,null,12,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,12,null,null,null,12,null,null,12,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,12,12,12,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,12,12,12,12,12,null,12,12,12,null,12,null,12,null,12,null,12,12,12,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,12,12,null,null,null,12,null,12,12,null,null,12,null,12,null,12,null,null,12,null,12,12,null,12,null,null,null,12,null,12,null,12,null,12,12,null,null,12,null,12,12,null,null,12,null,12,null,null,null,12,12,null,12,12,12,null,12,null,null,12,null,null,12,null,null,12,12,null,12,12,12,12,null,12,null,12,null,12,12,null,null,null,12,null,12,12,12,12,12,12,null,12,null,12,12,12,12,12,null,12,null,12,null,null,12,null,12,12,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,12,null,12,12,null,12,null,null,12,null,12,null,null,12,null,12,12,null,12,null,12,12,null,12,null,12,12,12,12,12,null,12,12,null,null,12,null,12,12,null,null,12,null,null,12,null,null,12,null,null,12,12,12,null,12,12,null,12,12,12,12,12,null,12,null,12,12,null,12,null,12,12,12,12,null,12,null,null,12,null,12,12,null,12,null,12,null,null,12,12,null,12,12,12,null,null,12,null,12,null,12,null,12,12,12,null,12,12,null,12,12,null,12,12,12,null,12,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,13,null,null,null,null,null,null,null,null,null,null,null,null,null,null,13,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null],"memalloc":[124.4997787475586,124.4997787475586,124.4997787475586,124.4997787475586,124.4997787475586,124.4997787475586,139.7820129394531,139.7820129394531,139.7820129394531,139.7820129394531,139.7820129394531,139.7820129394531,170.2477569580078,170.2477569580078,170.2477569580078,170.2477569580078,170.2477569580078,170.2477569580078,170.2477569580078,170.2477569580078,170.2477569580078,170.2477569580078,170.2477569580078,170.2477569580078,170.247802734375,170.247802734375,170.247802734375,170.247802734375,170.247802734375,170.247802734375,170.247802734375,170.247802734375,170.247802734375,170.247802734375,170.247802734375,170.247802734375,170.247802734375,170.247802734375,170.247802734375,170.247802734375,170.247802734375,170.247802734375,170.2474975585938,170.2474975585938,185.5525436401367,185.5525436401367,185.7372894287109,185.7372894287109,185.7372894287109,185.9335021972656,185.9335021972656,186.1368103027344,186.1368103027344,186.3507614135742,186.3507614135742,186.5752182006836,186.5752182006836,186.8053894042969,186.8053894042969,187.0217971801758,187.0217971801758,187.2300415039062,187.2300415039062,187.454460144043,187.6815795898438,187.6815795898438,187.9103469848633,187.9103469848633,188.1369552612305,188.1369552612305,188.364143371582,188.364143371582,188.5924453735352,188.5924453735352,188.777587890625,188.777587890625,188.777587890625,188.777587890625,185.6820831298828,185.6820831298828,185.9196166992188,186.1495590209961,186.3936004638672,186.3936004638672,186.3936004638672,186.6350708007812,186.6350708007812,186.6350708007812,186.8759994506836,186.8759994506836,187.1232299804688,187.1232299804688,187.3565902709961,187.5910415649414,187.5910415649414,187.8244094848633,187.8244094848633,188.0572891235352,188.0572891235352,188.29052734375,188.29052734375,188.5244522094727,188.7589492797852,188.8476715087891,188.8476715087891,188.8476715087891,185.8699722290039,186.0616455078125,186.0616455078125,186.2925415039062,186.2925415039062,186.2925415039062,186.5347442626953,186.7759704589844,186.7759704589844,187.0162734985352,187.2504501342773,187.2504501342773,187.4845275878906,187.7182769775391,187.7182769775391,187.9509429931641,187.9509429931641,188.1834716796875,188.1834716796875,188.4164505004883,188.6504058837891,188.6504058837891,188.8843002319336,188.8843002319336,188.93505859375,188.93505859375,188.93505859375,186.0538024902344,186.0538024902344,186.2762832641602,186.2762832641602,186.541618347168,186.541618347168,186.7844619750977,186.7844619750977,187.0266647338867,187.0266647338867,187.2637557983398,187.4990158081055,187.4990158081055,187.7330856323242,187.7330856323242,187.9664688110352,187.9664688110352,188.1999206542969,188.43408203125,188.6699676513672,188.6699676513672,188.9075469970703,189.0210876464844,189.0210876464844,189.0210876464844,186.1235122680664,186.1235122680664,186.3394546508789,186.3394546508789,186.5715026855469,186.8155899047852,186.8155899047852,187.0566253662109,187.0566253662109,187.2942199707031,187.529899597168,187.529899597168,187.7633895874023,187.9973526000977,188.2291717529297,188.2291717529297,188.4614868164062,188.6947631835938,188.9277267456055,188.9277267456055,189.1056594848633,189.1056594848633,189.1056594848633,189.1056594848633,189.1056594848633,189.1056594848633,186.3981323242188,186.3981323242188,186.6192321777344,186.8572006225586,186.8572006225586,187.0997009277344,187.0997009277344,187.3375854492188,187.5969543457031,187.8307342529297,187.8307342529297,188.0559463500977,188.2888870239258,188.2888870239258,188.5222854614258,188.5222854614258,188.7563858032227,188.7563858032227,188.9902801513672,188.9902801513672,189.1889190673828,189.1889190673828,189.1889190673828,189.1889190673828,189.1889190673828,189.1889190673828,186.5048522949219,186.5048522949219,186.7289505004883,186.7289505004883,186.9695739746094,186.9695739746094,187.2133407592773,187.4515609741211,187.4515609741211,187.688102722168,187.688102722168,187.9221878051758,187.9221878051758,188.1557312011719,188.3880615234375,188.6222152709961,188.6222152709961,188.8548431396484,188.8548431396484,189.0875473022461,189.0875473022461,189.0875473022461,189.2707748413086,189.2707748413086,189.2707748413086,189.2707748413086,186.6388702392578,186.6388702392578,186.8636169433594,186.8636169433594,187.0871963500977,187.0871963500977,187.3271179199219,187.3271179199219,187.5648880004883,187.8235168457031,187.8235168457031,188.0576171875,188.0576171875,188.2916412353516,188.2916412353516,188.5243606567383,188.5243606567383,188.7578811645508,188.7578811645508,188.9916915893555,189.2245483398438,189.3513870239258,189.3513870239258,189.3513870239258,186.6119918823242,186.8254699707031,186.8254699707031,187.0528869628906,187.2938537597656,187.2938537597656,187.5322570800781,187.7688293457031,188.0021057128906,188.2364730834961,188.2364730834961,188.4709854125977,188.7046432495117,188.7046432495117,188.9384002685547,188.9384002685547,189.1719970703125,189.1719970703125,189.4053573608398,189.4053573608398,189.4306259155273,189.4306259155273,189.4306259155273,186.826904296875,186.826904296875,187.0442810058594,187.0442810058594,187.2765655517578,187.5151596069336,187.7519760131836,187.7519760131836,187.988395690918,187.988395690918,188.2231903076172,188.2231903076172,188.4570999145508,188.4570999145508,188.6906356811523,188.6906356811523,188.9246978759766,188.9246978759766,189.1844482421875,189.1844482421875,189.4199447631836,189.5086669921875,189.5086669921875,186.8723602294922,187.0867233276367,187.3133316040039,187.5462951660156,187.5462951660156,187.7802734375,188.0132369995117,188.0132369995117,188.2450561523438,188.2450561523438,188.4770584106445,188.4770584106445,188.7097473144531,188.7097473144531,188.9415054321289,189.1743621826172,189.1743621826172,189.4065628051758,189.4065628051758,189.5853424072266,189.5853424072266,189.5853424072266,189.5853424072266,189.5853424072266,189.5853424072266,187.1344833374023,187.1344833374023,187.3559341430664,187.3559341430664,187.5924758911133,187.5924758911133,187.8287353515625,187.8287353515625,188.0650482177734,188.0650482177734,188.3009033203125,188.3009033203125,188.3009033203125,188.5344467163086,188.5344467163086,188.7688980102539,188.7688980102539,188.7688980102539,189.0017242431641,189.2358093261719,189.2358093261719,189.468864440918,189.468864440918,189.6608428955078,189.6608428955078,189.6608428955078,189.6608428955078,189.6608428955078,189.6608428955078,187.2585678100586,187.4825439453125,187.4825439453125,187.7186660766602,187.7186660766602,187.9539794921875,188.188591003418,188.188591003418,188.4234466552734,188.6573257446289,188.6573257446289,188.8914108276367,188.8914108276367,189.1249465942383,189.1249465942383,189.3588409423828,189.3588409423828,189.5928192138672,189.735107421875,189.735107421875,189.735107421875,187.1945648193359,187.4023284912109,187.4023284912109,187.6220932006836,187.854377746582,187.854377746582,187.854377746582,188.0888061523438,188.0888061523438,188.3248062133789,188.5608673095703,188.5608673095703,188.7963485717773,188.7963485717773,188.7963485717773,189.0315170288086,189.2659530639648,189.5007476806641,189.7360000610352,189.7360000610352,189.8081588745117,189.8081588745117,189.8081588745117,187.3723220825195,187.5835266113281,187.5835266113281,187.8027191162109,187.8027191162109,187.8027191162109,188.0364532470703,188.0364532470703,188.0364532470703,188.2700500488281,188.2700500488281,188.5289916992188,188.5289916992188,188.7654037475586,188.7654037475586,188.9912109375,188.9912109375,189.2263641357422,189.2263641357422,189.2263641357422,189.4579620361328,189.4579620361328,189.6908187866211,189.6908187866211,189.8800277709961,189.8800277709961,189.8800277709961,189.8800277709961,189.8800277709961,189.8800277709961,187.5869598388672,187.8050079345703,187.8050079345703,188.0347213745117,188.0347213745117,188.2661590576172,188.2661590576172,188.4999008178711,188.4999008178711,188.7342071533203,188.7342071533203,188.9669036865234,189.1989898681641,189.430793762207,189.6634750366211,189.6634750366211,189.8965682983398,189.8965682983398,189.9507522583008,189.9507522583008,189.9507522583008,187.598876953125,187.8090515136719,187.8090515136719,187.8090515136719,188.0262680053711,188.0262680053711,188.2558364868164,188.2558364868164,188.4890670776367,188.723503112793,188.723503112793,188.9592895507812,188.9592895507812,189.1937637329102,189.1937637329102,189.4286956787109,189.4286956787109,189.4286956787109,189.6626052856445,189.6626052856445,189.6626052856445,189.9054412841797,190.0202941894531,190.0202941894531,187.6542739868164,187.6542739868164,187.6542739868164,187.8492050170898,187.8492050170898,188.0623397827148,188.2877502441406,188.2877502441406,188.5209121704102,188.7565994262695,188.7565994262695,188.7565994262695,188.9921340942383,189.2262191772461,189.460075378418,189.460075378418,189.6930465698242,189.9268646240234,189.9268646240234,189.9268646240234,190.0888061523438,190.0888061523438,190.0888061523438,190.0888061523438,190.0888061523438,190.0888061523438,187.9258880615234,187.9258880615234,188.1325836181641,188.1325836181641,188.3500671386719,188.3500671386719,188.5830307006836,188.5830307006836,188.8194351196289,188.8194351196289,188.8194351196289,189.05615234375,189.05615234375,189.2909393310547,189.2909393310547,189.5244979858398,189.5244979858398,189.7592468261719,189.7592468261719,189.9949264526367,189.9949264526367,190.1560745239258,190.1560745239258,190.1560745239258,190.1560745239258,188.0265884399414,188.0265884399414,188.2338638305664,188.2338638305664,188.4732208251953,188.4732208251953,188.7051544189453,188.7051544189453,188.9408416748047,188.9408416748047,188.9408416748047,189.1679382324219,189.1679382324219,189.4014892578125,189.4014892578125,189.6350402832031,189.6350402832031,189.8700332641602,190.1068572998047,190.2223815917969,190.2223815917969,190.2223815917969,187.9662857055664,187.9662857055664,187.9662857055664,188.1673049926758,188.3723449707031,188.3723449707031,188.3723449707031,188.5929107666016,188.5929107666016,188.827880859375,188.827880859375,189.0658569335938,189.0658569335938,189.3030624389648,189.3030624389648,189.3030624389648,189.5385971069336,189.7736663818359,190.0075759887695,190.0075759887695,190.2442932128906,190.2875900268555,190.2875900268555,190.2875900268555,190.2875900268555,190.2875900268555,190.2875900268555,190.2875900268555,190.2875900268555,190.2875900268555,190.2875900268555,190.2875900268555,190.2875900268555,190.2875900268555,190.2875900268555,190.2875900268555,190.2875900268555,190.2875900268555,190.2875900268555,190.2875900268555,190.2875900268555,188.0641555786133,188.2326126098633,188.4103393554688,188.4103393554688,188.5896682739258,188.5896682739258,188.5896682739258,188.7647171020508,188.9626998901367,188.9626998901367,189.1787796020508,189.4059524536133,189.4059524536133,189.6381225585938,189.6381225585938,189.8638381958008,190.0918884277344,190.0918884277344,190.3247604370117,190.3247604370117,190.3516082763672,190.3516082763672,190.3516082763672,188.2369766235352,188.2369766235352,188.4386367797852,188.4386367797852,188.6480712890625,188.8741836547852,188.8741836547852,189.0830154418945,189.3174057006836,189.3174057006836,189.5743713378906,189.8083877563477,189.8083877563477,189.8083877563477,190.0433959960938,190.0433959960938,190.2774124145508,190.4148101806641,190.4148101806641,190.4148101806641,190.4148101806641,188.424690246582,188.424690246582,188.6208877563477,188.8298645019531,188.8298645019531,189.0595321655273,189.0595321655273,189.0595321655273,189.2945251464844,189.2945251464844,189.5291137695312,189.5291137695312,189.5291137695312,189.76318359375,189.76318359375,189.76318359375,189.9967651367188,189.9967651367188,190.2225723266602,190.2225723266602,190.4542236328125,190.4542236328125,190.4768905639648,190.4768905639648,188.4222946166992,188.6151123046875,188.6151123046875,188.8168716430664,188.8168716430664,189.0372848510742,189.0372848510742,189.2712478637695,189.5068435668945,189.7420501708984,189.9768600463867,190.2124328613281,190.2124328613281,190.4470596313477,190.4470596313477,190.5381164550781,190.5381164550781,190.5381164550781,188.4895324707031,188.4895324707031,188.6822052001953,188.6822052001953,188.8828277587891,189.103874206543,189.103874206543,189.3381805419922,189.3381805419922,189.5736236572266,189.5736236572266,189.8080444335938,190.0426559448242,190.0426559448242,190.2793884277344,190.2793884277344,190.5221176147461,190.5221176147461,190.5982284545898,190.5982284545898,190.5982284545898,188.5759735107422,188.5759735107422,188.7669982910156,188.7669982910156,188.9672393798828,188.9672393798828,188.9672393798828,189.1857223510742,189.1857223510742,189.420654296875,189.420654296875,189.6566619873047,189.8915176391602,190.1104583740234,190.1104583740234,190.3450546264648,190.3450546264648,190.5891418457031,190.5891418457031,190.6574172973633,190.6574172973633,190.6574172973633,188.6788635253906,188.6788635253906,188.8731155395508,189.0760040283203,189.0760040283203,189.2983245849609,189.2983245849609,189.2983245849609,189.5345458984375,189.5345458984375,189.7724990844727,190.0328674316406,190.0328674316406,190.0328674316406,190.2697906494141,190.2697906494141,190.5119781494141,190.7156295776367,190.7156295776367,190.7156295776367,190.7156295776367,190.7156295776367,190.7156295776367,188.8501892089844,188.8501892089844,189.0458221435547,189.0458221435547,189.2559051513672,189.2559051513672,189.4855651855469,189.4855651855469,189.7226333618164,189.7226333618164,189.9617767333984,190.1991195678711,190.435417175293,190.435417175293,190.679573059082,190.679573059082,190.7728805541992,190.7728805541992,190.7728805541992,188.8243789672852,188.8243789672852,189.004264831543,189.004264831543,189.2040863037109,189.2040863037109,189.2040863037109,189.4077377319336,189.6386108398438,189.8725204467773,189.8725204467773,190.1088409423828,190.1088409423828,190.3438034057617,190.3438034057617,190.578239440918,190.578239440918,190.578239440918,190.8130950927734,190.829216003418,190.829216003418,188.9778518676758,189.1674270629883,189.1674270629883,189.3935546875,189.6215362548828,189.6215362548828,189.8556518554688,190.0916290283203,190.0916290283203,190.0916290283203,190.3267593383789,190.3267593383789,190.5609970092773,190.7949066162109,190.7949066162109,190.8846435546875,190.8846435546875,189.0103149414062,189.0103149414062,189.193359375,189.193359375,189.193359375,189.393928527832,189.393928527832,189.393928527832,189.6143035888672,189.6143035888672,189.8500366210938,190.0879898071289,190.3270874023438,190.5628128051758,190.5628128051758,190.8029937744141,190.8029937744141,190.9391708374023,190.9391708374023,190.9391708374023,189.0639801025391,189.0639801025391,189.2505187988281,189.2505187988281,189.4449996948242,189.6366119384766,189.8178100585938,189.8178100585938,190.0521392822266,190.2893600463867,190.2893600463867,190.5476379394531,190.5476379394531,190.7814178466797,190.9928131103516,190.9928131103516,190.9928131103516,190.9928131103516,190.9928131103516,190.9928131103516,189.2613677978516,189.2613677978516,189.4568023681641,189.4568023681641,189.6653060913086,189.6653060913086,189.8965454101562,189.8965454101562,190.1337890625,190.1337890625,190.3717498779297,190.3717498779297,190.6093444824219,190.6093444824219,190.8538436889648,191.0455780029297,191.0455780029297,191.0455780029297,191.0455780029297,191.0455780029297,191.0455780029297,189.3682327270508,189.3682327270508,189.5644073486328,189.5644073486328,189.7752456665039,190.0049743652344,190.0049743652344,190.2422180175781,190.4802017211914,190.4802017211914,190.7171249389648,190.9542465209961,191.0975036621094,191.0975036621094,191.0975036621094,191.0975036621094,191.0975036621094,191.0975036621094,189.4744262695312,189.4744262695312,189.6835861206055,189.6835861206055,189.8336563110352,190.0643615722656,190.0643615722656,190.2944793701172,190.5305328369141,190.7654037475586,190.7654037475586,191.0002059936523,191.0002059936523,191.1486206054688,191.1486206054688,191.1486206054688,191.1486206054688,191.1486206054688,191.1486206054688,189.5482330322266,189.7412567138672,189.7412567138672,189.9524230957031,189.9524230957031,190.1868209838867,190.1868209838867,190.1868209838867,190.422119140625,190.422119140625,190.6609878540039,190.6609878540039,190.8972930908203,191.1361236572266,191.1361236572266,191.1988296508789,191.1988296508789,189.5132751464844,189.5132751464844,189.6999664306641,189.6999664306641,189.8853378295898,189.8853378295898,190.0976486206055,190.0976486206055,190.3257141113281,190.3257141113281,190.5620956420898,190.5620956420898,190.8206481933594,191.0542907714844,191.0542907714844,191.2483673095703,191.2483673095703,191.2483673095703,191.2483673095703,191.2483673095703,191.2483673095703,189.6639099121094,189.8532638549805,189.8532638549805,190.0604858398438,190.0604858398438,190.2903594970703,190.2903594970703,190.5256729125977,190.7613372802734,190.7613372802734,190.9956436157227,190.9956436157227,191.2296829223633,191.2296829223633,191.2969512939453,191.2969512939453,191.2969512939453,189.6643981933594,189.8515014648438,189.8515014648438,190.0534515380859,190.0534515380859,190.2817230224609,190.5190353393555,190.5190353393555,190.7561264038086,190.9932861328125,190.9932861328125,191.2308883666992,191.2308883666992,191.3449325561523,191.3449325561523,189.7029724121094,189.7029724121094,189.7029724121094,189.8884353637695,189.8884353637695,190.0879440307617,190.0879440307617,190.3047027587891,190.3047027587891,190.5632934570312,190.5632934570312,190.7996597290039,190.7996597290039,191.0353240966797,191.0353240966797,191.2689056396484,191.2689056396484,191.391960144043,191.391960144043,191.391960144043,191.391960144043,189.9441146850586,189.9441146850586,190.1407089233398,190.3414459228516,190.5646362304688,190.5646362304688,190.7992630004883,191.0359344482422,191.0359344482422,191.2724533081055,191.438346862793,191.438346862793,191.438346862793,191.438346862793,191.438346862793,191.438346862793,191.438346862793,191.438346862793,191.438346862793,191.438346862793,191.438346862793,191.438346862793,191.438346862793,191.438346862793,191.438346862793,191.438346862793,191.438346862793,191.438346862793,191.438346862793,191.438346862793,191.438346862793,191.438346862793,191.438346862793,191.438346862793,191.438346862793,191.438346862793,191.438346862793,191.438346862793,191.438346862793,191.438346862793,191.438346862793,191.438346862793,191.438346862793,191.438346862793,191.438346862793,191.438346862793,191.438346862793,191.438346862793,191.438346862793,191.438346862793,191.438346862793,191.438346862793,191.438346862793,191.438346862793,191.438346862793,191.438346862793,191.438346862793,191.438346862793,191.438346862793,191.438346862793,191.438346862793,191.438346862793,191.438346862793,191.438346862793,191.438346862793,191.438346862793,191.438346862793,191.438346862793,191.438346862793,191.438346862793,189.8427658081055,189.8427658081055,189.8660583496094,189.8660583496094,189.8660583496094,190.0529327392578,190.0529327392578,190.254035949707,190.254035949707,190.4658126831055,190.4658126831055,190.696418762207,190.696418762207,190.696418762207,190.9307174682617,191.1547317504883,191.3681335449219,191.3681335449219,191.6076354980469,191.6076354980469,191.8504943847656,191.8504943847656,192.095458984375,192.095458984375,192.3340225219727,192.5725784301758,192.5725784301758,192.7823638916016,192.9775772094727,193.1718978881836,193.366081237793,193.5599822998047,193.5599822998047,193.7526779174805,193.7526779174805,193.7526779174805,193.9649963378906,193.9649963378906,194.1589508056641,194.1589508056641,194.3530349731445,194.5477523803711,194.5477523803711,194.7000961303711,194.7000961303711,194.7000961303711,194.7000961303711,194.7000961303711,194.7000961303711,190.1669921875,190.1669921875,190.3638763427734,190.3638763427734,190.6025848388672,190.6025848388672,190.8542251586914,191.086784362793,191.307991027832,191.307991027832,191.5325622558594,191.5325622558594,191.7774658203125,192.0245819091797,192.0245819091797,192.2713241577148,192.2713241577148,192.516471862793,192.516471862793,192.516471862793,192.7617568969727,192.7617568969727,193.006721496582,193.006721496582,193.2499313354492,193.2499313354492,193.4924468994141,193.4924468994141,193.7356796264648,193.7356796264648,193.9783477783203,193.9783477783203,194.221565246582,194.221565246582,194.464225769043,194.464225769043,194.6967468261719,194.6967468261719,194.8329238891602,194.8329238891602,194.8329238891602,194.8329238891602,194.8329238891602,194.8329238891602,194.8329238891602,194.8329238891602,190.4068832397461,190.6235580444336,190.6235580444336,190.8589096069336,190.8589096069336,191.0985946655273,191.0985946655273,191.3231735229492,191.3231735229492,191.5383071899414,191.5383071899414,191.5383071899414,191.7794342041016,191.7794342041016,192.0182113647461,192.2576904296875,192.4925918579102,192.7329254150391,192.7329254150391,192.9710464477539,192.9710464477539,193.2062530517578,193.4422225952148,193.4422225952148,193.6747055053711,193.912841796875,193.912841796875,194.146598815918,194.146598815918,194.3794174194336,194.3794174194336,194.6172027587891,194.6172027587891,194.8488845825195,194.8488845825195,194.9636077880859,194.9636077880859,194.9636077880859,194.9636077880859,194.9636077880859,194.9636077880859,190.5927352905273,190.5927352905273,190.8055801391602,190.8055801391602,191.0361404418945,191.2718200683594,191.2718200683594,191.5138168334961,191.5138168334961,191.5138168334961,191.7406768798828,191.9828338623047,191.9828338623047,192.222770690918,192.222770690918,192.4605484008789,192.698616027832,192.698616027832,192.9404754638672,192.9404754638672,193.1821670532227,193.4159622192383,193.4159622192383,193.6482925415039,193.6482925415039,193.8796081542969,193.8796081542969,194.11279296875,194.11279296875,194.3474426269531,194.5825119018555,194.81982421875,195.0535659790039,195.092170715332,195.092170715332,195.092170715332,195.092170715332,190.8648681640625,190.8648681640625,191.0821838378906,191.3121566772461,191.3121566772461,191.5380172729492,191.5380172729492,191.7580413818359,191.7580413818359,192.0018463134766,192.0018463134766,192.2458801269531,192.2458801269531,192.486457824707,192.486457824707,192.7377395629883,192.7377395629883,192.9807586669922,192.9807586669922,193.2496109008789,193.2496109008789,193.4934005737305,193.7304611206055,193.9746551513672,193.9746551513672,194.2197952270508,194.2197952270508,194.4649353027344,194.4649353027344,194.7106170654297,194.7106170654297,194.9515533447266,194.9515533447266,194.9515533447266,195.1858596801758,195.2186813354492,195.2186813354492,195.2186813354492,195.2186813354492,191.0415344238281,191.0415344238281,191.1484146118164,191.1484146118164,191.289680480957,191.289680480957,191.289680480957,191.4965667724609,191.4965667724609,191.4965667724609,191.711540222168,191.711540222168,191.711540222168,191.9354248046875,191.9354248046875,192.1770401000977,192.4206008911133,192.6605453491211,192.6605453491211,192.9016036987305,192.9016036987305,193.138313293457,193.138313293457,193.3736801147461,193.3736801147461,193.5759353637695,193.5759353637695,193.8344650268555,193.8344650268555,194.0702056884766,194.3020706176758,194.3020706176758,194.5337142944336,194.5337142944336,194.5337142944336,194.7728576660156,194.7728576660156,195.0041580200195,195.0041580200195,195.2305679321289,195.3431777954102,195.3431777954102,195.3431777954102,195.3431777954102,195.3431777954102,195.3431777954102,191.1757202148438,191.3750610351562,191.3750610351562,191.5899505615234,191.5899505615234,191.8022918701172,191.8022918701172,192.027587890625,192.027587890625,192.2717361450195,192.2717361450195,192.5124969482422,192.7548294067383,192.7548294067383,192.9923706054688,192.9923706054688,193.2284622192383,193.4640808105469,193.4640808105469,193.6923980712891,193.9280624389648,194.1570587158203,194.3884658813477,194.3884658813477,194.3884658813477,194.6231307983398,194.8534851074219,194.8534851074219,195.1145782470703,195.1145782470703,195.336067199707,195.336067199707,195.4656448364258,195.4656448364258,195.4656448364258,195.4656448364258,191.3085632324219,191.3085632324219,191.3085632324219,191.4893112182617,191.4893112182617,191.4893112182617,191.6930770874023,191.8948059082031,191.8948059082031,192.1094131469727,192.1094131469727,192.3471984863281,192.3471984863281,192.5907821655273,192.5907821655273,192.8290405273438,193.0625991821289,193.0625991821289,193.3039169311523,193.3039169311523,193.5344543457031,193.7676849365234,193.7676849365234,193.9998168945312,194.2284851074219,194.2284851074219,194.4668273925781,194.6993255615234,194.6993255615234,194.9356994628906,195.1647033691406,195.3913650512695,195.3913650512695,195.3913650512695,195.5861358642578,195.5861358642578,195.5861358642578,195.5861358642578,195.5861358642578,195.5861358642578,191.5032501220703,191.5032501220703,191.7060546875,191.7060546875,191.7060546875,191.9099960327148,191.9099960327148,192.1196441650391,192.1196441650391,192.3482971191406,192.3482971191406,192.3482971191406,192.5895080566406,192.8310394287109,192.8310394287109,193.0684280395508,193.3092041015625,193.3092041015625,193.3092041015625,193.5442733764648,193.7810363769531,194.0110855102539,194.0110855102539,194.2418594360352,194.2418594360352,194.2418594360352,194.4806594848633,194.7110595703125,194.7110595703125,194.9483413696289,194.9483413696289,194.9483413696289,195.1815338134766,195.1815338134766,195.4104080200195,195.6382751464844,195.6382751464844,195.7046813964844,195.7046813964844,195.7046813964844,195.7046813964844,191.7008209228516,191.7008209228516,191.8937377929688,192.0863800048828,192.0863800048828,192.0863800048828,192.2632217407227,192.2632217407227,192.4732666015625,192.7042236328125,192.7042236328125,192.7042236328125,192.9210815429688,192.9210815429688,193.1506500244141,193.1506500244141,193.3497924804688,193.3497924804688,193.3497924804688,193.5683135986328,193.8004608154297,194.0313186645508,194.0313186645508,194.262809753418,194.262809753418,194.4960479736328,194.4960479736328,194.7216415405273,194.7216415405273,194.9494552612305,194.9494552612305,195.1912689208984,195.1912689208984,195.4347991943359,195.4347991943359,195.6493988037109,195.6493988037109,195.7853775024414,195.7853775024414,195.8213653564453,195.8213653564453,195.8213653564453,195.8213653564453,195.8213653564453,195.8213653564453,191.9410781860352,192.1380233764648,192.1380233764648,192.3377151489258,192.3377151489258,192.5589904785156,192.5589904785156,192.7970962524414,193.0340118408203,193.0340118408203,193.0340118408203,193.2724838256836,193.2724838256836,193.5090713500977,193.5090713500977,193.7529373168945,193.7529373168945,193.7529373168945,193.9974212646484,193.9974212646484,194.2389831542969,194.2389831542969,194.4811553955078,194.4811553955078,194.7237167358398,194.9672775268555,194.9672775268555,195.209716796875,195.209716796875,195.452995300293,195.6932144165039,195.6932144165039,195.9274291992188,195.9274291992188,195.9360733032227,195.9360733032227,195.9360733032227,195.9360733032227,195.9360733032227,195.9360733032227,192.1625900268555,192.1625900268555,192.3521575927734,192.546012878418,192.546012878418,192.7735824584961,192.7735824584961,192.9975128173828,192.9975128173828,193.2172622680664,193.4502639770508,193.4502639770508,193.6819152832031,193.6819152832031,193.9161605834961,193.9161605834961,194.1496887207031,194.1496887207031,194.3793792724609,194.3793792724609,194.6084213256836,194.6084213256836,194.8385848999023,195.0695343017578,195.0695343017578,195.2992095947266,195.2992095947266,195.5305023193359,195.5305023193359,195.7604064941406,195.7604064941406,195.982551574707,195.982551574707,196.0490341186523,196.0490341186523,196.0490341186523,196.0490341186523,196.0490341186523,196.0490341186523,192.3001480102539,192.3001480102539,192.4823150634766,192.4823150634766,192.692741394043,192.692741394043,192.9150924682617,193.1468887329102,193.3785171508789,193.6114959716797,193.6114959716797,193.8443603515625,193.8443603515625,193.8443603515625,194.0754928588867,194.0754928588867,194.3002243041992,194.3002243041992,194.531364440918,194.531364440918,194.7611541748047,194.9910736083984,194.9910736083984,195.2232513427734,195.2232513427734,195.4555969238281,195.4555969238281,195.6898803710938,195.6898803710938,195.9235534667969,196.1250228881836,196.1250228881836,196.1600952148438,196.1600952148438,196.1600952148438,196.1600952148438,196.1600952148438,196.1600952148438,192.484001159668,192.484001159668,192.6687469482422,192.6687469482422,192.8658599853516,192.8658599853516,193.0906372070312,193.0906372070312,193.3476638793945,193.3476638793945,193.5804595947266,193.8145446777344,194.0497894287109,194.0497894287109,194.2847366333008,194.2847366333008,194.5261611938477,194.5261611938477,194.7630386352539,194.7630386352539,194.9934616088867,194.9934616088867,195.2268218994141,195.2268218994141,195.463737487793,195.463737487793,195.463737487793,195.6948318481445,195.6948318481445,195.9347610473633,195.9347610473633,196.1616058349609,196.1616058349609,196.1616058349609,196.2693481445312,196.2693481445312,196.2693481445312,196.2693481445312,196.2693481445312,196.2693481445312,192.6077575683594,192.6077575683594,192.6077575683594,192.7932739257812,192.9849014282227,193.2022476196289,193.2022476196289,193.4319381713867,193.4319381713867,193.6627044677734,193.6627044677734,193.8967742919922,194.1322784423828,194.1322784423828,194.3667678833008,194.6097869873047,194.6097869873047,194.8724975585938,195.0993347167969,195.0993347167969,195.3309783935547,195.3309783935547,195.5492553710938,195.5492553710938,195.5492553710938,195.7575378417969,195.7575378417969,195.9803771972656,196.2023544311523,196.376953125,196.376953125,196.376953125,196.376953125,196.376953125,196.376953125,192.8379364013672,192.8379364013672,193.0149917602539,193.0149917602539,193.2118606567383,193.2118606567383,193.4277648925781,193.6542358398438,193.8825988769531,194.1157379150391,194.3502426147461,194.6095657348633,194.6095657348633,194.8458938598633,194.8458938598633,195.0775375366211,195.0775375366211,195.3121032714844,195.5517044067383,195.5517044067383,195.7882766723633,196.0256423950195,196.0256423950195,196.2539291381836,196.2539291381836,196.4802780151367,196.4802780151367,196.4826889038086,196.4826889038086,196.4826889038086,196.4826889038086,193.0104904174805,193.0104904174805,193.1874084472656,193.1874084472656,193.1874084472656,193.3876113891602,193.3876113891602,193.3876113891602,193.6006164550781,193.6006164550781,193.8227157592773,194.0532379150391,194.0532379150391,194.2892074584961,194.2892074584961,194.5250930786133,194.7615661621094,194.7615661621094,194.9975814819336,195.2298049926758,195.4625930786133,195.4625930786133,195.699836730957,195.940803527832,195.940803527832,196.2064361572266,196.438591003418,196.438591003418,196.5868225097656,196.5868225097656,196.5868225097656,196.5868225097656,193.0279006958008,193.0279006958008,193.2102661132812,193.2102661132812,193.3948822021484,193.5984802246094,193.815071105957,194.0412979125977,194.0412979125977,194.2772750854492,194.478401184082,194.478401184082,194.709846496582,194.709846496582,194.709846496582,194.9430465698242,194.9430465698242,195.1801681518555,195.4142532348633,195.6565399169922,195.6565399169922,195.6565399169922,195.8960800170898,195.8960800170898,196.1407241821289,196.3826370239258,196.3826370239258,196.6168975830078,196.6168975830078,196.6892395019531,196.6892395019531,196.6892395019531,196.6892395019531,196.6892395019531,196.6892395019531,193.2881469726562,193.4664001464844,193.4664001464844,193.6362915039062,193.841926574707,193.841926574707,194.0591888427734,194.0591888427734,194.2862548828125,194.5211486816406,194.7551116943359,194.7551116943359,194.989387512207,195.2302703857422,195.2302703857422,195.2302703857422,195.4582443237305,195.4582443237305,195.693000793457,195.693000793457,195.9272384643555,196.161735534668,196.161735534668,196.396125793457,196.396125793457,196.6247787475586,196.6247787475586,196.7900695800781,196.7900695800781,196.7900695800781,196.7900695800781,196.7900695800781,196.7900695800781,193.3631057739258,193.5477752685547,193.5477752685547,193.7375717163086,193.9418258666992,193.9418258666992,194.1763153076172,194.1763153076172,194.4072570800781,194.6434020996094,194.6434020996094,194.8818664550781,194.8818664550781,195.1188125610352,195.3577575683594,195.3577575683594,195.5928802490234,195.5928802490234,195.8259811401367,196.0591888427734,196.2936248779297,196.2936248779297,196.528190612793,196.528190612793,196.7594451904297,196.7594451904297,196.8891372680664,196.8891372680664,196.8891372680664,196.8891372680664,196.8891372680664,196.8891372680664,193.5466461181641,193.5466461181641,193.7284927368164,193.7284927368164,193.9186401367188,194.1200866699219,194.3268203735352,194.3268203735352,194.5314712524414,194.5314712524414,194.761344909668,194.9846572875977,195.1954727172852,195.4338760375977,195.6723709106445,195.6723709106445,195.9059066772461,196.1218032836914,196.1218032836914,196.3312759399414,196.3312759399414,196.5667724609375,196.5667724609375,196.7669830322266,196.7669830322266,196.9842300415039,196.9842300415039,196.9866790771484,196.9866790771484,196.9866790771484,196.9866790771484,196.9866790771484,196.9866790771484,196.9866790771484,196.9866790771484,196.9866790771484,196.9866790771484,196.9866790771484,196.9866790771484,196.9866790771484,196.9866790771484,196.9866790771484,196.9866790771484,196.9866790771484,196.9866790771484,196.9866790771484,196.9866790771484,196.9866790771484,196.9866790771484,196.9866790771484,196.9866790771484,196.9866790771484,196.9866790771484,196.9866790771484,196.9866790771484,196.9866790771484,196.9866790771484,196.9866790771484,196.9866790771484,196.9866790771484,196.9866790771484,196.9866790771484,196.9866790771484,196.9866790771484,196.9866790771484,196.9866790771484,196.9866790771484,196.9866790771484,196.9866790771484,196.9866790771484,196.9866790771484,196.9866790771484,196.9866790771484,196.9866790771484,196.9866790771484,193.6300048828125,193.6300048828125,193.6300048828125,193.6387939453125,193.6387939453125,193.6387939453125,193.794303894043,193.794303894043,193.9664459228516,193.9664459228516,194.1630859375,194.1630859375,194.3499908447266,194.3499908447266,194.5489807128906,194.5489807128906,194.7643356323242,194.9934768676758,194.9934768676758,194.9934768676758,195.2180480957031,195.2180480957031,195.4434127807617,195.4434127807617,195.6652908325195,195.8906478881836,196.1163711547852,196.1163711547852,196.3434524536133,196.5802917480469,196.5802917480469,196.8180541992188,196.8180541992188,197.0546493530273,197.0823287963867,197.0823287963867,197.0823287963867,197.0823287963867,197.0823287963867,197.0823287963867,193.922248840332,194.1016693115234,194.1016693115234,194.2913513183594,194.2913513183594,194.4924926757812,194.6955413818359,194.9063720703125,194.9063720703125,195.1313858032227,195.1313858032227,195.3622131347656,195.5918045043945,195.5918045043945,195.8209533691406,195.8209533691406,196.0742340087891,196.3049774169922,196.3049774169922,196.5355682373047,196.7680206298828,196.7680206298828,196.7680206298828,197.0000076293945,197.0000076293945,197.0000076293945,197.1767501831055,197.1767501831055,197.1767501831055,197.1767501831055,193.9533157348633,194.1311950683594,194.1311950683594,194.3147430419922,194.3147430419922,194.5103988647461,194.5103988647461,194.7186737060547,194.7186737060547,194.9403457641602,194.9403457641602,195.1728668212891,195.1728668212891,195.4058380126953,195.4058380126953,195.6386489868164,195.8694686889648,195.8694686889648,196.1016235351562,196.1016235351562,196.3351745605469,196.3351745605469,196.5691223144531,196.5691223144531,196.8114013671875,196.8114013671875,197.0549926757812,197.0549926757812,197.2696380615234,197.2696380615234,197.2696380615234,197.2696380615234,197.2696380615234,197.2696380615234,194.2463531494141,194.2463531494141,194.4463577270508,194.4463577270508,194.6395492553711,194.6395492553711,194.8471603393555,194.8471603393555,195.0712432861328,195.0712432861328,195.0712432861328,195.299186706543,195.299186706543,195.5320053100586,195.7619476318359,195.9910507202148,195.9910507202148,196.2207870483398,196.2207870483398,196.4538116455078,196.4538116455078,196.6861190795898,196.6861190795898,196.9179382324219,196.9179382324219,196.9179382324219,197.1528930664062,197.1528930664062,197.3610458374023,197.3610458374023,197.3610458374023,197.3610458374023,197.3610458374023,197.3610458374023,194.2214202880859,194.2214202880859,194.3997268676758,194.3997268676758,194.5792236328125,194.5792236328125,194.5792236328125,194.7717132568359,194.7717132568359,194.9808959960938,194.9808959960938,195.2049026489258,195.4381790161133,195.4381790161133,195.4381790161133,195.6714096069336,195.6714096069336,195.9047775268555,195.9047775268555,196.1397247314453,196.1397247314453,196.3732681274414,196.3732681274414,196.6107025146484,196.6107025146484,196.8473587036133,197.1162948608398,197.1162948608398,197.3608627319336,197.3608627319336,197.4509353637695,197.4509353637695,197.4509353637695,197.4509353637695,194.4495010375977,194.6296539306641,194.6296539306641,194.8115005493164,195.0106658935547,195.2234573364258,195.2234573364258,195.4506912231445,195.4506912231445,195.685546875,195.685546875,195.9184036254883,196.1505584716797,196.3830184936523,196.3830184936523,196.3830184936523,196.6160278320312,196.8500061035156,196.8500061035156,197.0849380493164,197.0849380493164,197.309684753418,197.309684753418,197.5380325317383,197.5380325317383,197.539421081543,197.539421081543,197.539421081543,197.539421081543,197.539421081543,197.539421081543,194.6406707763672,194.8193588256836,194.8193588256836,195.0198211669922,195.2042007446289,195.2042007446289,195.2042007446289,195.4009323120117,195.4009323120117,195.6092529296875,195.8296432495117,196.0588073730469,196.0588073730469,196.2892150878906,196.5214920043945,196.5214920043945,196.7521209716797,196.983528137207,196.983528137207,197.2167892456055,197.4495697021484,197.4495697021484,197.62646484375,197.62646484375,197.62646484375,197.62646484375,197.62646484375,197.62646484375,197.62646484375,197.62646484375,197.62646484375,194.7747192382812,194.7747192382812,194.7747192382812,194.9493103027344,194.9493103027344,195.1337127685547,195.1337127685547,195.3227233886719,195.3227233886719,195.5243225097656,195.736328125,195.736328125,195.736328125,195.9609069824219,196.1827087402344,196.1827087402344,196.4339904785156,196.6680755615234,196.8983154296875,196.8983154296875,197.1329345703125,197.1329345703125,197.3670196533203,197.3670196533203,197.3670196533203,197.6003341674805,197.7120513916016,197.7120513916016,197.7120513916016,197.7120513916016,194.8161163330078,194.8161163330078,194.9884185791016,194.9884185791016,195.1516418457031,195.1516418457031,195.3362274169922,195.3362274169922,195.5236663818359,195.5236663818359,195.6899948120117,195.6899948120117,195.8896636962891,195.8896636962891,196.0742874145508,196.0742874145508,196.2715530395508,196.2715530395508,196.4941940307617,196.4941940307617,196.7312927246094,196.7312927246094,196.9597473144531,196.9597473144531,196.9597473144531,197.1892852783203,197.1892852783203,197.42041015625,197.6521606445312,197.6521606445312,197.7963943481445,197.7963943481445,197.7963943481445,197.7963943481445,197.7963943481445,197.7963943481445,194.9219284057617,194.9219284057617,195.0926284790039,195.0926284790039,195.2705612182617,195.4547119140625,195.6555709838867,195.6555709838867,195.8696365356445,196.1027297973633,196.1027297973633,196.3360748291016,196.3360748291016,196.5711975097656,196.5711975097656,196.8047637939453,196.8047637939453,197.0369186401367,197.0369186401367,197.2687759399414,197.5000534057617,197.7316284179688,197.7316284179688,197.8792190551758,197.8792190551758,197.8792190551758,197.8792190551758,197.8792190551758,197.8792190551758,195.0467071533203,195.0467071533203,195.0467071533203,195.2367248535156,195.2367248535156,195.4147872924805,195.6010131835938,195.6010131835938,195.8046340942383,196.0191879272461,196.0191879272461,196.2484130859375,196.4835052490234,196.4835052490234,196.4835052490234,196.7193374633789,196.7193374633789,196.9516906738281,196.9516906738281,197.1838455200195,197.1838455200195,197.4170532226562,197.4170532226562,197.4170532226562,197.6501007080078,197.6501007080078,197.8833236694336,197.9608306884766,197.9608306884766,197.9608306884766,197.9608306884766,197.9608306884766,197.9608306884766,195.2353057861328,195.4089736938477,195.4089736938477,195.4089736938477,195.5902633666992,195.5902633666992,195.7779769897461,195.7779769897461,195.9839859008789,195.9839859008789,196.2018203735352,196.4358367919922,196.6699676513672,196.6699676513672,196.9028244018555,196.9028244018555,197.1368637084961,197.1368637084961,197.3697967529297,197.6024017333984,197.8597183227539,198.0410919189453,198.0410919189453,198.0410919189453,198.0410919189453,195.2820892333984,195.452262878418,195.452262878418,195.6320953369141,195.6320953369141,195.8154678344727,196.015739440918,196.015739440918,196.2325897216797,196.2325897216797,196.4663238525391,196.4663238525391,196.6999359130859,196.6999359130859,196.9322128295898,196.9322128295898,197.1643905639648,197.1643905639648,197.1643905639648,197.3947067260742,197.6281356811523,197.6281356811523,197.8635025024414,197.8635025024414,198.0965270996094,198.0965270996094,198.1200103759766,198.1200103759766,198.1200103759766,198.1200103759766,198.1200103759766,198.1200103759766,195.522216796875,195.7007064819336,195.8839645385742,195.8839645385742,196.0829620361328,196.3203125,196.550537109375,196.550537109375,196.786376953125,196.786376953125,197.0206604003906,197.0206604003906,197.2554397583008,197.2554397583008,197.4897003173828,197.4897003173828,197.7239990234375,197.7239990234375,197.9593353271484,198.1944122314453,198.1944122314453,198.1977462768555,198.1977462768555,198.1977462768555,198.1977462768555,198.1977462768555,198.1977462768555,195.6556396484375,195.8338623046875,195.8338623046875,196.0181198120117,196.0181198120117,196.2188720703125,196.2188720703125,196.4328002929688,196.4328002929688,196.6626434326172,196.6626434326172,196.6626434326172,196.8976440429688,196.8976440429688,197.1285095214844,197.3605041503906,197.3605041503906,197.5911331176758,197.8230590820312,197.8230590820312,198.0565032958984,198.2741088867188,198.2741088867188,198.2741088867188,198.2741088867188,198.2741088867188,198.2741088867188,195.8073272705078,195.8073272705078,195.9864883422852,195.9864883422852,196.1732482910156,196.3756790161133,196.5939712524414,196.5939712524414,196.8263320922852,196.8263320922852,197.0610885620117,197.0610885620117,197.2951736450195,197.5279083251953,197.5279083251953,197.7608871459961,197.9952239990234,198.230110168457,198.3493270874023,198.3493270874023,198.3493270874023,198.3493270874023,195.805793762207,195.805793762207,195.805793762207,195.9772567749023,195.9772567749023,196.1574249267578,196.1574249267578,196.3461837768555,196.5542144775391,196.5542144775391,196.7800140380859,196.7800140380859,197.0149917602539,197.0149917602539,197.2497634887695,197.2497634887695,197.4828643798828,197.7167053222656,197.9489288330078,198.1818923950195,198.1818923950195,198.4158020019531,198.4233474731445,198.4233474731445,198.4233474731445,198.4233474731445,198.4233474731445,198.4233474731445,196.0219650268555,196.1990737915039,196.1990737915039,196.3836212158203,196.3836212158203,196.5850372314453,196.8040771484375,196.8040771484375,197.0367660522461,197.0367660522461,197.0367660522461,197.2717056274414,197.2717056274414,197.5055313110352,197.7390670776367,197.9720306396484,198.2050857543945,198.2050857543945,198.4387969970703,198.4387969970703,198.4960403442383,198.4960403442383,198.4960403442383,198.4960403442383,198.4960403442383,198.4960403442383,196.0830230712891,196.0830230712891,196.2598876953125,196.4425811767578,196.4425811767578,196.4425811767578,196.638427734375,196.638427734375,196.638427734375,196.853759765625,196.853759765625,197.0849914550781,197.0849914550781,197.3218688964844,197.3218688964844,197.5572204589844,197.5572204589844,197.7922134399414,198.0485382080078,198.0485382080078,198.2850723266602,198.2850723266602,198.5206069946289,198.5206069946289,198.5677490234375,198.5677490234375,198.5677490234375,198.5677490234375,196.1858596801758,196.1858596801758,196.3541488647461,196.3541488647461,196.5367813110352,196.7362518310547,196.9523773193359,197.1847076416016,197.4242324829102,197.6620025634766,197.8967895507812,198.1319046020508,198.1319046020508,198.3672103881836,198.3672103881836,198.6030807495117,198.6030807495117,198.6381301879883,198.6381301879883,198.6381301879883,198.6381301879883,198.6381301879883,198.6381301879883,196.3117294311523,196.3117294311523,196.4908981323242,196.4908981323242,196.674430847168,196.674430847168,196.8644256591797,197.0796279907227,197.3338623046875,197.3338623046875,197.5700836181641,197.5700836181641,197.8023986816406,197.8023986816406,198.0368499755859,198.2694778442383,198.2694778442383,198.5019836425781,198.5019836425781,198.7074737548828,198.7074737548828,198.7074737548828,198.7074737548828,198.7074737548828,198.7074737548828,198.7074737548828,198.7074737548828,198.7074737548828,198.7074737548828,198.7074737548828,198.7074737548828,198.7074737548828,198.7074737548828,198.7074737548828,198.7074737548828,198.7074737548828,198.7074737548828,198.7074737548828,198.7074737548828,198.7074737548828,198.7074737548828,198.7074737548828,198.7074737548828,198.7074737548828,198.7074737548828,198.7074737548828,198.7074737548828,198.7074737548828,198.7074737548828,198.7074737548828,198.7074737548828,198.7074737548828,198.7074737548828,198.7074737548828,198.7074737548828,198.7074737548828,198.7074737548828,198.7074737548828,198.7074737548828,198.7074737548828,198.7074737548828,198.7074737548828,198.7074737548828,198.7074737548828,198.7074737548828,198.7074737548828,198.7074737548828,198.7074737548828,198.7074737548828,198.7074737548828,198.7074737548828,196.359733581543,196.4988861083984,196.4988861083984,196.6641845703125,196.842887878418,197.0326843261719,197.0326843261719,197.2369613647461,197.2369613647461,197.2369613647461,197.4368286132812,197.4368286132812,197.6729965209961,197.9072570800781,198.1404876708984,198.1404876708984,198.1404876708984,198.3751449584961,198.3751449584961,198.6099319458008,198.7755279541016,198.7755279541016,198.7755279541016,198.7755279541016,198.7755279541016,198.7755279541016,196.4363555908203,196.4363555908203,196.6076049804688,196.6076049804688,196.7820892333984,196.9669876098633,196.9669876098633,197.168083190918,197.168083190918,197.3860244750977,197.3860244750977,197.6229629516602,197.6229629516602,197.8540496826172,197.8540496826172,198.0881652832031,198.3413696289062,198.5515213012695,198.5515213012695,198.7843933105469,198.7843933105469,198.8426361083984,198.8426361083984,198.8426361083984,198.8426361083984,196.5828247070312,196.5828247070312,196.7491760253906,196.7491760253906,196.934196472168,197.1193237304688,197.3228073120117,197.3228073120117,197.5401153564453,197.5401153564453,197.7694625854492,198.0048370361328,198.2358093261719,198.468879699707,198.468879699707,198.468879699707,198.7001876831055,198.9086456298828,198.9086456298828,198.9086456298828,198.9086456298828,198.9086456298828,198.9086456298828,198.9086456298828,198.9086456298828,198.9086456298828,196.7938613891602,196.7938613891602,196.9716186523438,196.9716186523438,197.1576538085938,197.1576538085938,197.1576538085938,197.3637008666992,197.3637008666992,197.584098815918,197.8195877075195,198.0557632446289,198.0557632446289,198.2896347045898,198.2896347045898,198.5249328613281,198.5249328613281,198.7558288574219,198.9736633300781,198.9736633300781,198.9736633300781,198.9736633300781,198.9736633300781,198.9736633300781,198.9736633300781,198.9736633300781,198.9736633300781,198.9736633300781,198.9736633300781,198.9736633300781,196.8534774780273,196.8534774780273,197.0268325805664,197.0268325805664,197.2095031738281,197.4113006591797,197.4113006591797,197.6294860839844,197.6294860839844,197.8632278442383,198.0753021240234,198.3108062744141,198.3108062744141,198.5438461303711,198.5438461303711,198.8030319213867,198.8030319213867,199.0376129150391,199.0376129150391,199.0376129150391,199.0376129150391,199.0376129150391,199.0376129150391,199.0376129150391,199.0376129150391,199.0376129150391,196.8467025756836,196.8467025756836,196.8467025756836,196.9914321899414,196.9914321899414,197.1682052612305,197.1682052612305,197.3494415283203,197.3494415283203,197.5512008666992,197.5512008666992,197.7687911987305,197.7687911987305,198.0016479492188,198.0016479492188,198.22802734375,198.22802734375,198.4621658325195,198.4621658325195,198.6962051391602,198.6962051391602,198.6962051391602,198.9301605224609,199.1004791259766,199.1004791259766,199.1004791259766,199.1004791259766,199.1004791259766,199.1004791259766,196.9401702880859,196.9401702880859,197.1089706420898,197.1089706420898,197.2838134765625,197.4694366455078,197.4694366455078,197.6677093505859,197.6677093505859,197.8822937011719,198.1096038818359,198.1096038818359,198.3309020996094,198.5664749145508,198.5664749145508,198.8032608032227,199.0381546020508,199.0381546020508,199.1623916625977,199.1623916625977,199.1623916625977,199.1623916625977,197.0538635253906,197.0538635253906,197.2230911254883,197.3991546630859,197.5869750976562,197.5869750976562,197.7872161865234,197.7872161865234,197.7872161865234,198.0052947998047,198.0052947998047,198.2359466552734,198.4721298217773,198.7063369750977,198.7063369750977,198.944091796875,198.944091796875,199.1796493530273,199.2232894897461,199.2232894897461,199.2232894897461,199.2232894897461,199.2232894897461,199.2232894897461,197.2221221923828,197.2221221923828,197.3948135375977,197.3948135375977,197.5734481811523,197.5734481811523,197.7640151977539,197.7640151977539,197.9726333618164,198.1942749023438,198.1942749023438,198.4299240112305,198.6637268066406,198.8988189697266,198.8988189697266,199.1334762573242,199.2831649780273,199.2831649780273,199.2831649780273,199.2831649780273,197.227653503418,197.227653503418,197.3945159912109,197.3945159912109,197.5724639892578,197.5724639892578,197.7605590820312,197.9597473144531,197.9597473144531,197.9597473144531,198.1789703369141,198.4115753173828,198.4115753173828,198.6462020874023,198.6462020874023,198.8602676391602,198.8602676391602,199.1048812866211,199.3195037841797,199.3195037841797,199.3421401977539,199.3421401977539,199.3421401977539,199.3421401977539,199.3421401977539,199.3421401977539,197.3943710327148,197.3943710327148,197.5564804077148,197.7376098632812,197.7376098632812,197.7376098632812,197.8932876586914,198.0478668212891,198.0478668212891,198.2556076049805,198.2556076049805,198.2556076049805,198.4611282348633,198.6754379272461,198.8871841430664,199.1182861328125,199.3332214355469,199.3332214355469,199.4000701904297,199.4000701904297,199.4000701904297,199.4000701904297,199.4000701904297,199.4000701904297,197.4555740356445,197.6237487792969,197.7853164672852,197.7853164672852,197.9649810791016,197.9649810791016,198.1497573852539,198.3462982177734,198.3462982177734,198.5686874389648,198.7913665771484,199.0173873901367,199.2415924072266,199.2415924072266,199.2415924072266,199.4496841430664,199.4496841430664,199.4571075439453,199.4571075439453,199.4571075439453,199.4571075439453,199.4571075439453,199.4571075439453,197.5838088989258,197.5838088989258,197.5838088989258,197.7636489868164,197.9352645874023,197.9352645874023,198.1246032714844,198.3159637451172,198.5191421508789,198.7464904785156,198.9455413818359,198.9455413818359,199.1736602783203,199.1736602783203,199.4010162353516,199.5132064819336,199.5132064819336,199.5132064819336,199.5132064819336,199.5132064819336,199.5132064819336,199.5132064819336,199.5132064819336,199.5132064819336,197.7295379638672,197.7295379638672,197.9037704467773,197.9037704467773,198.0885772705078,198.0885772705078,198.2769012451172,198.4856491088867,198.4856491088867,198.7094039916992,198.7094039916992,198.9665222167969,199.2003860473633,199.2003860473633,199.2003860473633,199.4341049194336,199.4341049194336,199.5683975219727,199.5683975219727,199.5683975219727,199.5683975219727,199.5683975219727,199.5683975219727,197.6739807128906,197.6739807128906,197.8438415527344,198.0228271484375,198.0228271484375,198.2115020751953,198.2115020751953,198.4175033569336,198.4175033569336,198.6273422241211,198.8521423339844,198.8521423339844,199.0868072509766,199.0868072509766,199.3229675292969,199.3229675292969,199.3229675292969,199.5526962280273,199.6227035522461,199.6227035522461,199.6227035522461,199.6227035522461,199.6227035522461,199.6227035522461,199.6227035522461,199.6227035522461,199.6227035522461,199.6227035522461,199.6227035522461,199.6227035522461,199.6227035522461,199.6227035522461,199.6227035522461,199.6227035522461,199.6227035522461,199.6227035522461,199.6227035522461,199.6227035522461,199.6227035522461,197.7530975341797,197.7530975341797,197.7530975341797,197.8136138916016,197.8136138916016,197.9716796875,198.1422805786133,198.1422805786133,198.1422805786133,198.331428527832,198.331428527832,198.331428527832,198.5319900512695,198.5319900512695,198.7506866455078,198.9844131469727,198.9844131469727,199.2192077636719,199.4458694458008,199.4458694458008,199.6711807250977,199.6711807250977,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,199.6759185791016,197.8366928100586,197.8366928100586,197.8366928100586,197.8366928100586,197.8366928100586,197.8366928100586,197.8873901367188,197.8873901367188,198.0777893066406,198.0777893066406,198.2759475708008,198.2759475708008,198.4831314086914,198.4831314086914,198.7023162841797,198.7023162841797,198.9343490600586,199.1676864624023,199.1676864624023,199.3885879516602,199.3885879516602,199.6011581420898,199.8364028930664,200.0655746459961,200.0655746459961,200.295166015625,200.295166015625,200.5246429443359,200.5246429443359,200.5246429443359,200.7589492797852,201.0082473754883,201.0082473754883,201.2041320800781,201.4004440307617,201.4004440307617,201.595588684082,201.595588684082,201.7912826538086,201.9856567382812,201.9856567382812,202.1812896728516,202.1812896728516,202.376594543457,202.376594543457,202.5714416503906,202.5714416503906,202.7644195556641,202.7644195556641,202.7644195556641,202.95654296875,203.151496887207,203.151496887207,203.3454437255859,203.3454437255859,203.540771484375,203.540771484375,203.7359008789062,203.9311599731445,203.9311599731445,203.9311599731445,204.1241149902344,204.3196411132812,204.5048980712891,204.6962814331055,204.8916931152344,204.8916931152344,205.0800018310547,205.0800018310547,205.0800018310547,205.268684387207,205.4635848999023,205.4635848999023,205.5107879638672,205.5107879638672,205.5107879638672,205.5107879638672,205.5107879638672,205.5107879638672,205.5107879638672,205.5107879638672,205.5107879638672,198.3420333862305,198.5397109985352,198.7439498901367,198.9638061523438,198.9638061523438,199.1997604370117,199.4289321899414,199.4289321899414,199.6455078125,199.6455078125,199.8679733276367,200.1059799194336,200.1059799194336,200.3396682739258,200.3396682739258,200.5732116699219,200.5732116699219,200.8090515136719,201.0442581176758,201.2797164916992,201.2797164916992,201.2797164916992,201.5162200927734,201.5162200927734,201.7508316040039,201.7508316040039,201.9854431152344,202.2190246582031,202.2190246582031,202.2190246582031,202.453125,202.453125,202.453125,202.687873840332,202.9218521118164,203.1567611694336,203.1567611694336,203.3915328979492,203.3915328979492,203.6254425048828,203.8602523803711,203.8602523803711,203.8602523803711,204.095588684082,204.095588684082,204.3308868408203,204.3308868408203,204.5891723632812,204.5891723632812,204.8222045898438,204.8222045898438,205.0555725097656,205.2835693359375,205.2835693359375,205.5079498291016,205.5079498291016,205.7206497192383,205.7206497192383,205.7206497192383,205.7206497192383,205.7206497192383,205.7206497192383,205.7206497192383,205.7206497192383,205.7206497192383,205.7206497192383,205.7206497192383,205.7206497192383,198.6388168334961,198.6388168334961,198.832763671875,198.832763671875,199.0352630615234,199.2421417236328,199.2421417236328,199.4625015258789,199.4625015258789,199.6791915893555,199.6791915893555,199.8917617797852,200.1206893920898,200.3590087890625,200.3590087890625,200.3590087890625,200.5934219360352,200.5934219360352,200.8286895751953,201.0644226074219,201.0644226074219,201.2990798950195,201.5278625488281,201.5278625488281,201.5278625488281,201.7871856689453,202.0188140869141,202.0188140869141,202.2520217895508,202.2520217895508,202.4857559204102,202.4857559204102,202.7207565307617,202.7207565307617,202.9537506103516,202.9537506103516,203.1854553222656,203.4180603027344,203.6470642089844,203.6470642089844,203.8622283935547,203.8622283935547,204.0927886962891,204.0927886962891,204.3235168457031,204.3235168457031,204.5544586181641,204.5544586181641,204.7873687744141,205.0194549560547,205.2532577514648,205.4792251586914,205.4792251586914,205.7017288208008,205.7017288208008,205.9265441894531,205.9265441894531,205.9271926879883,205.9271926879883,205.9271926879883,205.9271926879883,205.9271926879883,205.9271926879883,205.9271926879883,205.9271926879883,205.9271926879883,198.9572982788086,198.9572982788086,199.1668853759766,199.3609237670898,199.3609237670898,199.5467910766602,199.7419204711914,199.9290008544922,200.1211242675781,200.3373107910156,200.5715713500977,200.8047637939453,200.8047637939453,201.0356369018555,201.0356369018555,201.2688446044922,201.2688446044922,201.498893737793,201.498893737793,201.7216415405273,201.9491653442383,201.9491653442383,202.1799850463867,202.411735534668,202.411735534668,202.6413116455078,202.8725814819336,202.8725814819336,203.1043243408203,203.336181640625,203.336181640625,203.5675811767578,203.5675811767578,203.7970581054688,204.0275039672852,204.0275039672852,204.2570266723633,204.2570266723633,204.5110015869141,204.5110015869141,204.7422332763672,204.7422332763672,204.9598236083984,204.9598236083984,205.1844863891602,205.4172897338867,205.4172897338867,205.6340026855469,205.6340026855469,205.8531799316406,205.8531799316406,205.8531799316406,206.0762023925781,206.0762023925781,206.1302947998047,206.1302947998047,206.1302947998047,206.1302947998047,206.1302947998047,206.1302947998047,206.1302947998047,206.1302947998047,206.1302947998047,199.1843795776367,199.1843795776367,199.3532257080078,199.3532257080078,199.5437545776367,199.5437545776367,199.7206878662109,199.7206878662109,199.9147720336914,200.1107025146484,200.3071823120117,200.5219116210938,200.7487564086914,200.7487564086914,200.7487564086914,200.9826812744141,200.9826812744141,201.2170791625977,201.2170791625977,201.4722366333008,201.4722366333008,201.7029876708984,201.7029876708984,201.935546875,201.935546875,202.1669311523438,202.1669311523438,202.401741027832,202.401741027832,202.401741027832,202.6328887939453,202.8625183105469,203.0953750610352,203.3258438110352,203.5579986572266,203.7875213623047,203.7875213623047,204.0166931152344,204.2491989135742,204.4801254272461,204.4801254272461,204.7126235961914,204.7126235961914,204.9407272338867,204.9407272338867,205.1570587158203,205.1570587158203,205.3852310180664,205.6019439697266,205.830940246582,206.0521469116211,206.0521469116211,206.270263671875,206.270263671875,206.3302764892578,206.3302764892578,206.3302764892578,206.3302764892578,206.3302764892578,206.3302764892578,206.3302764892578,206.3302764892578,206.3302764892578,199.5227508544922,199.5227508544922,199.7011032104492,199.8921585083008,199.8921585083008,200.0885238647461,200.0885238647461,200.2824020385742,200.2824020385742,200.4791870117188,200.6928482055664,200.6928482055664,200.6928482055664,200.9278030395508,200.9278030395508,201.1655578613281,201.1655578613281,201.3865203857422,201.3865203857422,201.6190567016602,201.8513793945312,201.8513793945312,202.0825500488281,202.3128356933594,202.3128356933594,202.5444869995117,202.5444869995117,202.7759628295898,202.7759628295898,203.0068435668945,203.0068435668945,203.2375946044922,203.2375946044922,203.4671096801758,203.4671096801758,203.6977691650391,203.9281158447266,203.9281158447266,203.9281158447266,204.1577911376953,204.1577911376953,204.389404296875,204.6207046508789,204.6207046508789,204.6207046508789,204.8520278930664,204.8520278930664,205.1081848144531,205.1081848144531,205.3410339355469,205.3410339355469,205.5737686157227,205.8067245483398,205.8067245483398,206.0370254516602,206.2573471069336,206.4791488647461,206.4791488647461,206.5268936157227,206.5268936157227,206.5268936157227,206.5268936157227,206.5268936157227,206.5268936157227,206.5268936157227,206.5268936157227,206.5268936157227,199.8218078613281,199.9909820556641,199.9909820556641,200.1742401123047,200.3513946533203,200.5388031005859,200.7128982543945,200.7128982543945,200.9103546142578,200.9103546142578,201.1247863769531,201.1247863769531,201.3510818481445,201.5859146118164,201.5859146118164,201.8168487548828,201.8168487548828,202.0708999633789,202.0708999633789,202.3020553588867,202.5315093994141,202.761100769043,202.9918518066406,203.2222518920898,203.4520568847656,203.4520568847656,203.6801986694336,203.6801986694336,203.9099426269531,204.1414184570312,204.3713226318359,204.6025466918945,204.8325424194336,204.8325424194336,205.0632781982422,205.0632781982422,205.2956314086914,205.2956314086914,205.2956314086914,205.5277786254883,205.5277786254883,205.7605133056641,205.9931945800781,206.2228851318359,206.2228851318359,206.4466247558594,206.6702880859375,206.6702880859375,206.7203750610352,206.7203750610352,206.7203750610352,206.7203750610352,206.7203750610352,206.7203750610352,206.7203750610352,206.7203750610352,206.7203750610352,206.7203750610352,206.7203750610352,206.7203750610352,206.7203750610352,206.7203750610352,206.7203750610352,206.7203750610352,206.7203750610352,206.7203750610352,206.7203750610352,206.7203750610352,200.0621337890625,200.0621337890625,200.0621337890625,200.0621337890625,200.0621337890625,200.0621337890625,200.2080535888672,200.2080535888672,200.3961791992188,200.3961791992188,200.5906219482422,200.5906219482422,200.5906219482422,200.7788772583008,200.7788772583008,200.9675827026367,200.9675827026367,201.190544128418,201.190544128418,201.4218215942383,201.6486053466797,201.6486053466797,201.8733901977539,202.0937194824219,202.0937194824219,202.3195953369141,202.3195953369141,202.5451126098633,202.7954635620117,202.7954635620117,203.0209732055664,203.0209732055664,203.0209732055664,203.2562484741211,203.2562484741211,203.4823913574219,203.6916046142578,203.6916046142578,203.9204254150391,203.9204254150391,204.1368637084961,204.3601837158203,204.3601837158203,204.5879364013672,204.5879364013672,204.8141250610352,205.0422439575195,205.2693099975586,205.4920654296875,205.7231063842773,205.7231063842773,205.9491729736328,206.1807556152344,206.1807556152344,206.1807556152344,206.4183731079102,206.4183731079102,206.6563415527344,206.89599609375,206.89599609375,206.89599609375,206.9107284545898,206.9107284545898,206.9107284545898,206.9107284545898,206.9107284545898,206.9107284545898,206.9107284545898,206.9107284545898,206.9107284545898,200.4565582275391,200.6604614257812,200.8499755859375,200.8499755859375,201.036506652832,201.2258453369141,201.2258453369141,201.4397506713867,201.6700820922852,201.9052886962891,202.1384963989258,202.3709487915039,202.3709487915039,202.602424621582,202.602424621582,202.8355941772461,203.0670471191406,203.0670471191406,203.2971649169922,203.2971649169922,203.5292510986328,203.7623519897461,203.9944381713867,204.2260818481445,204.2260818481445,204.4584197998047,204.4584197998047,204.4584197998047,204.6900405883789,204.6900405883789,204.9218978881836,205.1543350219727,205.1543350219727,205.3875579833984,205.3875579833984,205.6204223632812,205.6204223632812,205.6204223632812,205.855712890625,206.0894470214844,206.0894470214844,206.3237762451172,206.5565643310547,206.7896499633789,206.7896499633789,207.0244522094727,207.0979766845703,207.0979766845703,207.0979766845703,207.0979766845703,207.0979766845703,207.0979766845703,200.7250747680664,200.9045181274414,201.0738525390625,201.0738525390625,201.2548370361328,201.4371032714844,201.4371032714844,201.6451034545898,201.872673034668,201.872673034668,202.1034393310547,202.3365783691406,202.5664520263672,202.5664520263672,202.7930068969727,202.7930068969727,203.0227127075195,203.0227127075195,203.0227127075195,203.2506561279297,203.2506561279297,203.2506561279297,210.9748687744141,210.9748687744141,210.9748687744141,210.9748687744141,210.9748687744141,210.9748687744141,210.9748687744141,210.9748687744141,210.9748687744141,210.9748687744141,210.9748687744141,210.9748687744141,210.9748687744141,210.9748687744141,210.9748687744141,210.9748687744141,210.9748687744141,210.9748687744141,210.9748687744141,210.9748687744141,210.9748687744141,210.9748687744141,210.9748687744141,210.9748687744141,218.6042633056641,218.6042633056641,218.6042633056641,218.6042709350586,218.6042709350586,218.6042709350586,218.6042709350586,218.6042709350586,218.6042709350586,218.6042709350586,218.6042709350586,218.6042709350586,218.6042709350586,218.6042709350586,218.6042709350586,218.6042709350586,218.6042709350586,218.6042709350586,218.6042709350586,218.6042709350586,218.6042709350586,218.6042709350586,218.6042709350586,218.6042709350586,218.6042709350586,218.6042709350586,218.6042709350586,218.6042709350586,218.6042709350586,233.8630599975586,233.8630599975586,233.8630599975586,233.8630599975586,233.8630599975586,233.8630599975586,233.8630599975586,233.8630599975586,233.8630599975586,233.8630599975586,233.8630599975586,233.8630599975586,233.8630599975586,233.8630599975586,233.8630599975586,233.8630599975586,233.8630599975586,233.8630599975586,233.8630599975586,233.8630599975586,241.4924774169922,241.4924774169922,241.4924774169922,241.4924774169922,241.4924774169922,241.4924774169922,241.4924774169922,241.4924774169922,241.5276870727539,241.5276870727539,241.5276870727539,241.5276870727539,241.5276870727539,241.5276870727539,241.5276870727539,241.5276870727539,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164,256.8876724243164],"meminc":[0,0,0,0,0,0,15.28223419189453,0,0,0,0,0,30.46574401855469,0,0,0,0,0,0,0,0,0,0,0,4.57763671875e-05,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-0.00030517578125,0,15.30504608154297,0,0.1847457885742188,0,0,0.1962127685546875,0,0.20330810546875,0,0.2139511108398438,0,0.224456787109375,0,0.2301712036132812,0,0.2164077758789062,0,0.2082443237304688,0,0.2244186401367188,0.2271194458007812,0,0.2287673950195312,0,0.2266082763671875,0,0.2271881103515625,0,0.228302001953125,0,0.1851425170898438,0,0,0,-3.095504760742188,0,0.2375335693359375,0.2299423217773438,0.2440414428710938,0,0,0.2414703369140625,0,0,0.2409286499023438,0,0.2472305297851562,0,0.2333602905273438,0.2344512939453125,0,0.233367919921875,0,0.232879638671875,0,0.2332382202148438,0,0.2339248657226562,0.2344970703125,0.08872222900390625,0,0,-2.977699279785156,0.1916732788085938,0,0.23089599609375,0,0,0.2422027587890625,0.2412261962890625,0,0.2403030395507812,0.2341766357421875,0,0.2340774536132812,0.2337493896484375,0,0.232666015625,0,0.2325286865234375,0,0.2329788208007812,0.2339553833007812,0,0.2338943481445312,0,0.05075836181640625,0,0,-2.881256103515625,0,0.2224807739257812,0,0.2653350830078125,0,0.2428436279296875,0,0.2422027587890625,0,0.237091064453125,0.235260009765625,0,0.23406982421875,0,0.2333831787109375,0,0.2334518432617188,0.234161376953125,0.2358856201171875,0,0.237579345703125,0.1135406494140625,0,0,-2.897575378417969,0,0.2159423828125,0,0.2320480346679688,0.2440872192382812,0,0.2410354614257812,0,0.2375946044921875,0.2356796264648438,0,0.233489990234375,0.2339630126953125,0.2318191528320312,0,0.2323150634765625,0.2332763671875,0.2329635620117188,0,0.1779327392578125,0,0,0,0,0,-2.707527160644531,0,0.221099853515625,0.2379684448242188,0,0.2425003051757812,0,0.237884521484375,0.259368896484375,0.2337799072265625,0,0.2252120971679688,0.232940673828125,0,0.2333984375,0,0.234100341796875,0,0.2338943481445312,0,0.198638916015625,0,0,0,0,0,-2.684066772460938,0,0.2240982055664062,0,0.2406234741210938,0,0.2437667846679688,0.23822021484375,0,0.236541748046875,0,0.2340850830078125,0,0.2335433959960938,0.232330322265625,0.2341537475585938,0,0.2326278686523438,0,0.2327041625976562,0,0,0.1832275390625,0,0,0,-2.631904602050781,0,0.2247467041015625,0,0.2235794067382812,0,0.2399215698242188,0,0.2377700805664062,0.2586288452148438,0,0.234100341796875,0,0.2340240478515625,0,0.2327194213867188,0,0.2335205078125,0,0.2338104248046875,0.2328567504882812,0.1268386840820312,0,0,-2.739395141601562,0.2134780883789062,0,0.2274169921875,0.240966796875,0,0.2384033203125,0.236572265625,0.2332763671875,0.2343673706054688,0,0.2345123291015625,0.2336578369140625,0,0.2337570190429688,0,0.2335968017578125,0,0.2333602905273438,0,0.0252685546875,0,0,-2.603721618652344,0,0.217376708984375,0,0.2322845458984375,0.2385940551757812,0.23681640625,0,0.236419677734375,0,0.2347946166992188,0,0.2339096069335938,0,0.2335357666015625,0,0.2340621948242188,0,0.2597503662109375,0,0.2354965209960938,0.08872222900390625,0,-2.636306762695312,0.2143630981445312,0.2266082763671875,0.2329635620117188,0,0.233978271484375,0.2329635620117188,0,0.2318191528320312,0,0.2320022583007812,0,0.2326889038085938,0,0.2317581176757812,0.2328567504882812,0,0.2322006225585938,0,0.1787796020507812,0,0,0,0,0,-2.450859069824219,0,0.2214508056640625,0,0.236541748046875,0,0.2362594604492188,0,0.2363128662109375,0,0.2358551025390625,0,0,0.2335433959960938,0,0.2344512939453125,0,0,0.2328262329101562,0.2340850830078125,0,0.2330551147460938,0,0.1919784545898438,0,0,0,0,0,-2.402275085449219,0.2239761352539062,0,0.2361221313476562,0,0.2353134155273438,0.2346115112304688,0,0.2348556518554688,0.2338790893554688,0,0.2340850830078125,0,0.2335357666015625,0,0.2338943481445312,0,0.233978271484375,0.1422882080078125,0,0,-2.540542602539062,0.207763671875,0,0.2197647094726562,0.2322845458984375,0,0,0.2344284057617188,0,0.2360000610351562,0.2360610961914062,0,0.2354812622070312,0,0,0.23516845703125,0.23443603515625,0.2347946166992188,0.2352523803710938,0,0.0721588134765625,0,0,-2.435836791992188,0.2112045288085938,0,0.2191925048828125,0,0,0.233734130859375,0,0,0.2335968017578125,0,0.258941650390625,0,0.2364120483398438,0,0.2258071899414062,0,0.2351531982421875,0,0,0.231597900390625,0,0.2328567504882812,0,0.189208984375,0,0,0,0,0,-2.293067932128906,0.218048095703125,0,0.2297134399414062,0,0.2314376831054688,0,0.2337417602539062,0,0.2343063354492188,0,0.232696533203125,0.232086181640625,0.2318038940429688,0.2326812744140625,0,0.23309326171875,0,0.0541839599609375,0,0,-2.351875305175781,0.210174560546875,0,0,0.2172164916992188,0,0.2295684814453125,0,0.2332305908203125,0.23443603515625,0,0.2357864379882812,0,0.2344741821289062,0,0.2349319458007812,0,0,0.2339096069335938,0,0,0.2428359985351562,0.1148529052734375,0,-2.366020202636719,0,0,0.1949310302734375,0,0.213134765625,0.2254104614257812,0,0.2331619262695312,0.235687255859375,0,0,0.23553466796875,0.2340850830078125,0.233856201171875,0,0.23297119140625,0.2338180541992188,0,0,0.1619415283203125,0,0,0,0,0,-2.162918090820312,0,0.206695556640625,0,0.2174835205078125,0,0.2329635620117188,0,0.2364044189453125,0,0,0.2367172241210938,0,0.2347869873046875,0,0.2335586547851562,0,0.2347488403320312,0,0.2356796264648438,0,0.1611480712890625,0,0,0,-2.129486083984375,0,0.207275390625,0,0.2393569946289062,0,0.23193359375,0,0.235687255859375,0,0,0.2270965576171875,0,0.233551025390625,0,0.233551025390625,0,0.2349929809570312,0.2368240356445312,0.1155242919921875,0,0,-2.256095886230469,0,0,0.201019287109375,0.2050399780273438,0,0,0.2205657958984375,0,0.2349700927734375,0,0.23797607421875,0,0.2372055053710938,0,0,0.23553466796875,0.2350692749023438,0.2339096069335938,0,0.2367172241210938,0.04329681396484375,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2.223434448242188,0.16845703125,0.1777267456054688,0,0.1793289184570312,0,0,0.175048828125,0.1979827880859375,0,0.2160797119140625,0.2271728515625,0,0.2321701049804688,0,0.2257156372070312,0.2280502319335938,0,0.2328720092773438,0,0.02684783935546875,0,0,-2.114631652832031,0,0.20166015625,0,0.2094345092773438,0.2261123657226562,0,0.208831787109375,0.2343902587890625,0,0.2569656372070312,0.2340164184570312,0,0,0.2350082397460938,0,0.2340164184570312,0.1373977661132812,0,0,0,-1.990119934082031,0,0.196197509765625,0.2089767456054688,0,0.2296676635742188,0,0,0.2349929809570312,0,0.234588623046875,0,0,0.23406982421875,0,0,0.23358154296875,0,0.2258071899414062,0,0.2316513061523438,0,0.02266693115234375,0,-2.054595947265625,0.1928176879882812,0,0.2017593383789062,0,0.2204132080078125,0,0.2339630126953125,0.235595703125,0.2352066040039062,0.2348098754882812,0.2355728149414062,0,0.2346267700195312,0,0.09105682373046875,0,0,-2.048583984375,0,0.1926727294921875,0,0.20062255859375,0.2210464477539062,0,0.2343063354492188,0,0.235443115234375,0,0.2344207763671875,0.2346115112304688,0,0.2367324829101562,0,0.2427291870117188,0,0.07611083984375,0,0,-2.022254943847656,0,0.1910247802734375,0,0.2002410888671875,0,0,0.2184829711914062,0,0.2349319458007812,0,0.2360076904296875,0.2348556518554688,0.2189407348632812,0,0.2345962524414062,0,0.2440872192382812,0,0.06827545166015625,0,0,-1.978553771972656,0,0.1942520141601562,0.2028884887695312,0,0.222320556640625,0,0,0.2362213134765625,0,0.2379531860351562,0.2603683471679688,0,0,0.2369232177734375,0,0.2421875,0.2036514282226562,0,0,0,0,0,-1.865440368652344,0,0.1956329345703125,0,0.2100830078125,0,0.2296600341796875,0,0.2370681762695312,0,0.2391433715820312,0.2373428344726562,0.236297607421875,0,0.2441558837890625,0,0.0933074951171875,0,0,-1.948501586914062,0,0.1798858642578125,0,0.1998214721679688,0,0,0.2036514282226562,0.2308731079101562,0.2339096069335938,0,0.2363204956054688,0,0.2349624633789062,0,0.23443603515625,0,0,0.2348556518554688,0.01612091064453125,0,-1.851364135742188,0.1895751953125,0,0.2261276245117188,0.2279815673828125,0,0.2341156005859375,0.2359771728515625,0,0,0.2351303100585938,0,0.2342376708984375,0.2339096069335938,0,0.0897369384765625,0,-1.87432861328125,0,0.18304443359375,0,0,0.2005691528320312,0,0,0.2203750610351562,0,0.2357330322265625,0.2379531860351562,0.2390975952148438,0.2357254028320312,0,0.2401809692382812,0,0.1361770629882812,0,0,-1.875190734863281,0,0.1865386962890625,0,0.1944808959960938,0.1916122436523438,0.1811981201171875,0,0.2343292236328125,0.2372207641601562,0,0.2582778930664062,0,0.2337799072265625,0.211395263671875,0,0,0,0,0,-1.7314453125,0,0.1954345703125,0,0.2085037231445312,0,0.2312393188476562,0,0.23724365234375,0,0.2379608154296875,0,0.2375946044921875,0,0.2444992065429688,0.1917343139648438,0,0,0,0,0,-1.677345275878906,0,0.1961746215820312,0,0.2108383178710938,0.2297286987304688,0,0.23724365234375,0.2379837036132812,0,0.2369232177734375,0.23712158203125,0.1432571411132812,0,0,0,0,0,-1.623077392578125,0,0.2091598510742188,0,0.1500701904296875,0.2307052612304688,0,0.2301177978515625,0.236053466796875,0.2348709106445312,0,0.23480224609375,0,0.1484146118164062,0,0,0,0,0,-1.600387573242188,0.193023681640625,0,0.2111663818359375,0,0.2343978881835938,0,0,0.2352981567382812,0,0.2388687133789062,0,0.2363052368164062,0.23883056640625,0,0.06270599365234375,0,-1.685554504394531,0,0.1866912841796875,0,0.1853713989257812,0,0.212310791015625,0,0.2280654907226562,0,0.2363815307617188,0,0.2585525512695312,0.233642578125,0,0.1940765380859375,0,0,0,0,0,-1.584457397460938,0.1893539428710938,0,0.2072219848632812,0,0.2298736572265625,0,0.2353134155273438,0.2356643676757812,0,0.2343063354492188,0,0.234039306640625,0,0.06726837158203125,0,0,-1.632553100585938,0.187103271484375,0,0.2019500732421875,0,0.228271484375,0.2373123168945312,0,0.237091064453125,0.2371597290039062,0,0.2376022338867188,0,0.114044189453125,0,-1.641960144042969,0,0,0.1854629516601562,0,0.1995086669921875,0,0.2167587280273438,0,0.2585906982421875,0,0.2363662719726562,0,0.2356643676757812,0,0.23358154296875,0,0.1230545043945312,0,0,0,-1.447845458984375,0,0.19659423828125,0.2007369995117188,0.2231903076171875,0,0.2346267700195312,0.2366714477539062,0,0.2365188598632812,0.1658935546875,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.5955810546875,0,0.02329254150390625,0,0,0.1868743896484375,0,0.2011032104492188,0,0.2117767333984375,0,0.2306060791015625,0,0,0.2342987060546875,0.2240142822265625,0.2134017944335938,0,0.239501953125,0,0.24285888671875,0,0.244964599609375,0,0.2385635375976562,0.238555908203125,0,0.2097854614257812,0.1952133178710938,0.1943206787109375,0.194183349609375,0.1939010620117188,0,0.1926956176757812,0,0,0.2123184204101562,0,0.1939544677734375,0,0.1940841674804688,0.1947174072265625,0,0.15234375,0,0,0,0,0,-4.533103942871094,0,0.1968841552734375,0,0.23870849609375,0,0.2516403198242188,0.2325592041015625,0.2212066650390625,0,0.2245712280273438,0,0.244903564453125,0.2471160888671875,0,0.2467422485351562,0,0.245147705078125,0,0,0.2452850341796875,0,0.244964599609375,0,0.2432098388671875,0,0.2425155639648438,0,0.2432327270507812,0,0.2426681518554688,0,0.2432174682617188,0,0.2426605224609375,0,0.2325210571289062,0,0.1361770629882812,0,0,0,0,0,0,0,-4.426040649414062,0.2166748046875,0,0.2353515625,0,0.23968505859375,0,0.224578857421875,0,0.2151336669921875,0,0,0.2411270141601562,0,0.2387771606445312,0.2394790649414062,0.2349014282226562,0.2403335571289062,0,0.2381210327148438,0,0.2352066040039062,0.2359695434570312,0,0.23248291015625,0.2381362915039062,0,0.2337570190429688,0,0.232818603515625,0,0.2377853393554688,0,0.2316818237304688,0,0.1147232055664062,0,0,0,0,0,-4.370872497558594,0,0.2128448486328125,0,0.230560302734375,0.2356796264648438,0,0.2419967651367188,0,0,0.2268600463867188,0.242156982421875,0,0.2399368286132812,0,0.2377777099609375,0.238067626953125,0,0.2418594360351562,0,0.2416915893554688,0.233795166015625,0,0.232330322265625,0,0.2313156127929688,0,0.233184814453125,0,0.234649658203125,0.2350692749023438,0.2373123168945312,0.2337417602539062,0.038604736328125,0,0,0,-4.227302551269531,0,0.217315673828125,0.2299728393554688,0,0.225860595703125,0,0.2200241088867188,0,0.243804931640625,0,0.2440338134765625,0,0.2405776977539062,0,0.25128173828125,0,0.2430191040039062,0,0.2688522338867188,0,0.2437896728515625,0.237060546875,0.2441940307617188,0,0.2451400756835938,0,0.2451400756835938,0,0.2456817626953125,0,0.240936279296875,0,0,0.2343063354492188,0.0328216552734375,0,0,0,-4.177146911621094,0,0.1068801879882812,0,0.141265869140625,0,0,0.2068862915039062,0,0,0.2149734497070312,0,0,0.2238845825195312,0,0.2416152954101562,0.243560791015625,0.2399444580078125,0,0.241058349609375,0,0.2367095947265625,0,0.2353668212890625,0,0.2022552490234375,0,0.2585296630859375,0,0.2357406616210938,0.2318649291992188,0,0.2316436767578125,0,0,0.2391433715820312,0,0.2313003540039062,0,0.226409912109375,0.11260986328125,0,0,0,0,0,-4.167457580566406,0.1993408203125,0,0.2148895263671875,0,0.21234130859375,0,0.2252960205078125,0,0.2441482543945312,0,0.2407608032226562,0.2423324584960938,0,0.2375411987304688,0,0.2360916137695312,0.2356185913085938,0,0.2283172607421875,0.2356643676757812,0.2289962768554688,0.2314071655273438,0,0,0.2346649169921875,0.2303543090820312,0,0.2610931396484375,0,0.2214889526367188,0,0.12957763671875,0,0,0,-4.157081604003906,0,0,0.1807479858398438,0,0,0.203765869140625,0.2017288208007812,0,0.2146072387695312,0,0.2377853393554688,0,0.2435836791992188,0,0.2382583618164062,0.2335586547851562,0,0.2413177490234375,0,0.2305374145507812,0.2332305908203125,0,0.2321319580078125,0.228668212890625,0,0.23834228515625,0.2324981689453125,0,0.2363739013671875,0.22900390625,0.2266616821289062,0,0,0.1947708129882812,0,0,0,0,0,-4.0828857421875,0,0.2028045654296875,0,0,0.2039413452148438,0,0.2096481323242188,0,0.2286529541015625,0,0,0.2412109375,0.2415313720703125,0,0.2373886108398438,0.2407760620117188,0,0,0.2350692749023438,0.2367630004882812,0.2300491333007812,0,0.23077392578125,0,0,0.238800048828125,0.2304000854492188,0,0.2372817993164062,0,0,0.2331924438476562,0,0.2288742065429688,0.2278671264648438,0,0.06640625,0,0,0,-4.003860473632812,0,0.1929168701171875,0.1926422119140625,0,0,0.1768417358398438,0,0.2100448608398438,0.23095703125,0,0,0.21685791015625,0,0.2295684814453125,0,0.1991424560546875,0,0,0.2185211181640625,0.232147216796875,0.2308578491210938,0,0.2314910888671875,0,0.2332382202148438,0,0.2255935668945312,0,0.227813720703125,0,0.2418136596679688,0,0.2435302734375,0,0.214599609375,0,0.1359786987304688,0,0.03598785400390625,0,0,0,0,0,-3.880287170410156,0.1969451904296875,0,0.1996917724609375,0,0.2212753295898438,0,0.2381057739257812,0.2369155883789062,0,0,0.2384719848632812,0,0.2365875244140625,0,0.243865966796875,0,0,0.2444839477539062,0,0.2415618896484375,0,0.2421722412109375,0,0.2425613403320312,0.243560791015625,0,0.2424392700195312,0,0.2432785034179688,0.2402191162109375,0,0.2342147827148438,0,0.00864410400390625,0,0,0,0,0,-3.773483276367188,0,0.1895675659179688,0.1938552856445312,0,0.227569580078125,0,0.2239303588867188,0,0.2197494506835938,0.233001708984375,0,0.2316513061523438,0,0.2342453002929688,0,0.2335281372070312,0,0.2296905517578125,0,0.2290420532226562,0,0.23016357421875,0.2309494018554688,0,0.22967529296875,0,0.231292724609375,0,0.2299041748046875,0,0.2221450805664062,0,0.0664825439453125,0,0,0,0,0,-3.748886108398438,0,0.1821670532226562,0,0.2104263305664062,0,0.22235107421875,0.2317962646484375,0.23162841796875,0.2329788208007812,0,0.2328643798828125,0,0,0.2311325073242188,0,0.2247314453125,0,0.23114013671875,0,0.2297897338867188,0.22991943359375,0,0.232177734375,0,0.2323455810546875,0,0.234283447265625,0,0.233673095703125,0.2014694213867188,0,0.03507232666015625,0,0,0,0,0,-3.676094055175781,0,0.1847457885742188,0,0.197113037109375,0,0.2247772216796875,0,0.2570266723632812,0,0.2327957153320312,0.2340850830078125,0.2352447509765625,0,0.2349472045898438,0,0.241424560546875,0,0.23687744140625,0,0.2304229736328125,0,0.2333602905273438,0,0.2369155883789062,0,0,0.2310943603515625,0,0.23992919921875,0,0.2268447875976562,0,0,0.1077423095703125,0,0,0,0,0,-3.661590576171875,0,0,0.185516357421875,0.1916275024414062,0.21734619140625,0,0.2296905517578125,0,0.2307662963867188,0,0.23406982421875,0.235504150390625,0,0.2344894409179688,0.2430191040039062,0,0.2627105712890625,0.226837158203125,0,0.2316436767578125,0,0.2182769775390625,0,0,0.208282470703125,0,0.22283935546875,0.2219772338867188,0.1745986938476562,0,0,0,0,0,-3.539016723632812,0,0.1770553588867188,0,0.196868896484375,0,0.2159042358398438,0.226470947265625,0.228363037109375,0.2331390380859375,0.2345046997070312,0.2593231201171875,0,0.236328125,0,0.2316436767578125,0,0.2345657348632812,0.2396011352539062,0,0.236572265625,0.23736572265625,0,0.2282867431640625,0,0.226348876953125,0,0.002410888671875,0,0,0,-3.472198486328125,0,0.1769180297851562,0,0,0.2002029418945312,0,0,0.2130050659179688,0,0.2220993041992188,0.2305221557617188,0,0.2359695434570312,0,0.2358856201171875,0.2364730834960938,0,0.2360153198242188,0.2322235107421875,0.2327880859375,0,0.23724365234375,0.240966796875,0,0.2656326293945312,0.2321548461914062,0,0.1482315063476562,0,0,0,-3.558921813964844,0,0.1823654174804688,0,0.1846160888671875,0.2035980224609375,0.2165908813476562,0.226226806640625,0,0.2359771728515625,0.2011260986328125,0,0.2314453125,0,0,0.2332000732421875,0,0.23712158203125,0.2340850830078125,0.2422866821289062,0,0,0.2395401000976562,0,0.2446441650390625,0.241912841796875,0,0.2342605590820312,0,0.0723419189453125,0,0,0,0,0,-3.401092529296875,0.178253173828125,0,0.169891357421875,0.2056350708007812,0,0.2172622680664062,0,0.2270660400390625,0.234893798828125,0.2339630126953125,0,0.2342758178710938,0.2408828735351562,0,0,0.2279739379882812,0,0.2347564697265625,0,0.2342376708984375,0.2344970703125,0,0.2343902587890625,0,0.2286529541015625,0,0.1652908325195312,0,0,0,0,0,-3.426963806152344,0.1846694946289062,0,0.1897964477539062,0.204254150390625,0,0.2344894409179688,0,0.2309417724609375,0.23614501953125,0,0.23846435546875,0,0.2369461059570312,0.2389450073242188,0,0.2351226806640625,0,0.2331008911132812,0.2332077026367188,0.23443603515625,0,0.2345657348632812,0,0.2312545776367188,0,0.1296920776367188,0,0,0,0,0,-3.342491149902344,0,0.1818466186523438,0,0.1901473999023438,0.201446533203125,0.2067337036132812,0,0.20465087890625,0,0.2298736572265625,0.2233123779296875,0.2108154296875,0.2384033203125,0.238494873046875,0,0.2335357666015625,0.2158966064453125,0,0.20947265625,0,0.2354965209960938,0,0.2002105712890625,0,0.2172470092773438,0,0.00244903564453125,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-3.356674194335938,0,0,0.0087890625,0,0,0.1555099487304688,0,0.1721420288085938,0,0.1966400146484375,0,0.1869049072265625,0,0.1989898681640625,0,0.2153549194335938,0.2291412353515625,0,0,0.2245712280273438,0,0.2253646850585938,0,0.2218780517578125,0.2253570556640625,0.2257232666015625,0,0.227081298828125,0.2368392944335938,0,0.237762451171875,0,0.2365951538085938,0.027679443359375,0,0,0,0,0,-3.160079956054688,0.1794204711914062,0,0.1896820068359375,0,0.201141357421875,0.2030487060546875,0.2108306884765625,0,0.2250137329101562,0,0.2308273315429688,0.2295913696289062,0,0.2291488647460938,0,0.2532806396484375,0.230743408203125,0,0.2305908203125,0.232452392578125,0,0,0.2319869995117188,0,0,0.1767425537109375,0,0,0,-3.223434448242188,0.1778793334960938,0,0.1835479736328125,0,0.1956558227539062,0,0.2082748413085938,0,0.2216720581054688,0,0.2325210571289062,0,0.23297119140625,0,0.2328109741210938,0.2308197021484375,0,0.2321548461914062,0,0.233551025390625,0,0.23394775390625,0,0.242279052734375,0,0.24359130859375,0,0.2146453857421875,0,0,0,0,0,-3.023284912109375,0,0.2000045776367188,0,0.1931915283203125,0,0.207611083984375,0,0.2240829467773438,0,0,0.2279434204101562,0,0.232818603515625,0.2299423217773438,0.2291030883789062,0,0.229736328125,0,0.2330245971679688,0,0.2323074340820312,0,0.2318191528320312,0,0,0.234954833984375,0,0.2081527709960938,0,0,0,0,0,-3.139625549316406,0,0.1783065795898438,0,0.1794967651367188,0,0,0.1924896240234375,0,0.2091827392578125,0,0.2240066528320312,0.2332763671875,0,0,0.2332305908203125,0,0.233367919921875,0,0.2349472045898438,0,0.2335433959960938,0,0.2374343872070312,0,0.2366561889648438,0.2689361572265625,0,0.24456787109375,0,0.0900726318359375,0,0,0,-3.001434326171875,0.1801528930664062,0,0.1818466186523438,0.1991653442382812,0.2127914428710938,0,0.22723388671875,0,0.2348556518554688,0,0.2328567504882812,0.2321548461914062,0.2324600219726562,0,0,0.2330093383789062,0.233978271484375,0,0.2349319458007812,0,0.2247467041015625,0,0.2283477783203125,0,0.0013885498046875,0,0,0,0,0,-2.898750305175781,0.1786880493164062,0,0.2004623413085938,0.1843795776367188,0,0,0.1967315673828125,0,0.2083206176757812,0.2203903198242188,0.2291641235351562,0,0.23040771484375,0.2322769165039062,0,0.2306289672851562,0.2314071655273438,0,0.2332611083984375,0.2327804565429688,0,0.1768951416015625,0,0,0,0,0,0,0,0,-2.85174560546875,0,0,0.174591064453125,0,0.1844024658203125,0,0.1890106201171875,0,0.20159912109375,0.212005615234375,0,0,0.224578857421875,0.2218017578125,0,0.25128173828125,0.2340850830078125,0.2302398681640625,0,0.234619140625,0,0.2340850830078125,0,0,0.2333145141601562,0.1117172241210938,0,0,0,-2.89593505859375,0,0.17230224609375,0,0.1632232666015625,0,0.1845855712890625,0,0.18743896484375,0,0.1663284301757812,0,0.1996688842773438,0,0.1846237182617188,0,0.197265625,0,0.2226409912109375,0,0.2370986938476562,0,0.22845458984375,0,0,0.2295379638671875,0,0.2311248779296875,0.23175048828125,0,0.1442337036132812,0,0,0,0,0,-2.874465942382812,0,0.1707000732421875,0,0.1779327392578125,0.1841506958007812,0.2008590698242188,0,0.2140655517578125,0.23309326171875,0,0.2333450317382812,0,0.2351226806640625,0,0.2335662841796875,0,0.2321548461914062,0,0.2318572998046875,0.2312774658203125,0.2315750122070312,0,0.1475906372070312,0,0,0,0,0,-2.832511901855469,0,0,0.1900177001953125,0,0.1780624389648438,0.1862258911132812,0,0.2036209106445312,0.2145538330078125,0,0.2292251586914062,0.2350921630859375,0,0,0.2358322143554688,0,0.2323532104492188,0,0.2321548461914062,0,0.2332077026367188,0,0,0.2330474853515625,0,0.2332229614257812,0.07750701904296875,0,0,0,0,0,-2.72552490234375,0.1736679077148438,0,0,0.1812896728515625,0,0.187713623046875,0,0.2060089111328125,0,0.21783447265625,0.2340164184570312,0.234130859375,0,0.2328567504882812,0,0.234039306640625,0,0.2329330444335938,0.23260498046875,0.2573165893554688,0.1813735961914062,0,0,0,-2.759002685546875,0.1701736450195312,0,0.1798324584960938,0,0.1833724975585938,0.2002716064453125,0,0.2168502807617188,0,0.233734130859375,0,0.233612060546875,0,0.2322769165039062,0,0.232177734375,0,0,0.230316162109375,0.233428955078125,0,0.2353668212890625,0,0.2330245971679688,0,0.0234832763671875,0,0,0,0,0,-2.597793579101562,0.1784896850585938,0.183258056640625,0,0.1989974975585938,0.2373504638671875,0.230224609375,0,0.23583984375,0,0.234283447265625,0,0.2347793579101562,0,0.2342605590820312,0,0.2342987060546875,0,0.2353363037109375,0.235076904296875,0,0.00333404541015625,0,0,0,0,0,-2.542106628417969,0.17822265625,0,0.1842575073242188,0,0.2007522583007812,0,0.21392822265625,0,0.2298431396484375,0,0,0.2350006103515625,0,0.230865478515625,0.23199462890625,0,0.2306289672851562,0.2319259643554688,0,0.2334442138671875,0.2176055908203125,0,0,0,0,0,-2.466781616210938,0,0.1791610717773438,0,0.1867599487304688,0.2024307250976562,0.218292236328125,0,0.23236083984375,0,0.2347564697265625,0,0.2340850830078125,0.2327346801757812,0,0.2329788208007812,0.2343368530273438,0.2348861694335938,0.1192169189453125,0,0,0,-2.543533325195312,0,0,0.1714630126953125,0,0.1801681518554688,0,0.1887588500976562,0.2080307006835938,0,0.225799560546875,0,0.2349777221679688,0,0.234771728515625,0,0.2331008911132812,0.2338409423828125,0.2322235107421875,0.2329635620117188,0,0.2339096069335938,0.00754547119140625,0,0,0,0,0,-2.401382446289062,0.1771087646484375,0,0.1845474243164062,0,0.201416015625,0.2190399169921875,0,0.2326889038085938,0,0,0.2349395751953125,0,0.23382568359375,0.2335357666015625,0.2329635620117188,0.2330551147460938,0,0.2337112426757812,0,0.05724334716796875,0,0,0,0,0,-2.413017272949219,0,0.1768646240234375,0.1826934814453125,0,0,0.1958465576171875,0,0,0.21533203125,0,0.231231689453125,0,0.23687744140625,0,0.2353515625,0,0.2349929809570312,0.2563247680664062,0,0.2365341186523438,0,0.23553466796875,0,0.04714202880859375,0,0,0,-2.381889343261719,0,0.1682891845703125,0,0.1826324462890625,0.1994705200195312,0.21612548828125,0.232330322265625,0.2395248413085938,0.2377700805664062,0.2347869873046875,0.2351150512695312,0,0.2353057861328125,0,0.235870361328125,0,0.0350494384765625,0,0,0,0,0,-2.326400756835938,0,0.179168701171875,0,0.18353271484375,0,0.1899948120117188,0.2152023315429688,0.2542343139648438,0,0.2362213134765625,0,0.2323150634765625,0,0.2344512939453125,0.2326278686523438,0,0.2325057983398438,0,0.2054901123046875,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2.347740173339844,0.1391525268554688,0,0.1652984619140625,0.1787033081054688,0.1897964477539062,0,0.2042770385742188,0,0,0.1998672485351562,0,0.2361679077148438,0.2342605590820312,0.2332305908203125,0,0,0.2346572875976562,0,0.2347869873046875,0.1655960083007812,0,0,0,0,0,-2.33917236328125,0,0.1712493896484375,0,0.1744842529296875,0.1848983764648438,0,0.2010955810546875,0,0.2179412841796875,0,0.2369384765625,0,0.2310867309570312,0,0.2341156005859375,0.253204345703125,0.2101516723632812,0,0.2328720092773438,0,0.0582427978515625,0,0,0,-2.259811401367188,0,0.166351318359375,0,0.1850204467773438,0.1851272583007812,0.2034835815429688,0,0.2173080444335938,0,0.2293472290039062,0.2353744506835938,0.2309722900390625,0.2330703735351562,0,0,0.2313079833984375,0.2084579467773438,0,0,0,0,0,0,0,0,-2.114784240722656,0,0.1777572631835938,0,0.18603515625,0,0,0.2060470581054688,0,0.22039794921875,0.2354888916015625,0.236175537109375,0,0.2338714599609375,0,0.2352981567382812,0,0.23089599609375,0.21783447265625,0,0,0,0,0,0,0,0,0,0,0,-2.120185852050781,0,0.1733551025390625,0,0.1826705932617188,0.2017974853515625,0,0.2181854248046875,0,0.2337417602539062,0.2120742797851562,0.235504150390625,0,0.2330398559570312,0,0.259185791015625,0,0.2345809936523438,0,0,0,0,0,0,0,0,-2.190910339355469,0,0,0.1447296142578125,0,0.1767730712890625,0,0.1812362670898438,0,0.2017593383789062,0,0.21759033203125,0,0.2328567504882812,0,0.22637939453125,0,0.2341384887695312,0,0.234039306640625,0,0,0.2339553833007812,0.170318603515625,0,0,0,0,0,-2.160308837890625,0,0.1688003540039062,0,0.1748428344726562,0.1856231689453125,0,0.198272705078125,0,0.2145843505859375,0.2273101806640625,0,0.2212982177734375,0.2355728149414062,0,0.236785888671875,0.234893798828125,0,0.124237060546875,0,0,0,-2.108528137207031,0,0.1692276000976562,0.1760635375976562,0.1878204345703125,0,0.2002410888671875,0,0,0.21807861328125,0,0.23065185546875,0.2361831665039062,0.2342071533203125,0,0.2377548217773438,0,0.2355575561523438,0.04364013671875,0,0,0,0,0,-2.001167297363281,0,0.1726913452148438,0,0.1786346435546875,0,0.1905670166015625,0,0.2086181640625,0.2216415405273438,0,0.2356491088867188,0.2338027954101562,0.2350921630859375,0,0.2346572875976562,0.149688720703125,0,0,0,-2.055511474609375,0,0.1668624877929688,0,0.177947998046875,0,0.1880950927734375,0.199188232421875,0,0,0.2192230224609375,0.23260498046875,0,0.2346267700195312,0,0.2140655517578125,0,0.2446136474609375,0.2146224975585938,0,0.02263641357421875,0,0,0,0,0,-1.947769165039062,0,0.162109375,0.1811294555664062,0,0,0.1556777954101562,0.1545791625976562,0,0.2077407836914062,0,0,0.2055206298828125,0.2143096923828125,0.2117462158203125,0.2311019897460938,0.214935302734375,0,0.0668487548828125,0,0,0,0,0,-1.944496154785156,0.1681747436523438,0.1615676879882812,0,0.1796646118164062,0,0.1847763061523438,0.1965408325195312,0,0.2223892211914062,0.2226791381835938,0.2260208129882812,0.2242050170898438,0,0,0.2080917358398438,0,0.00742340087890625,0,0,0,0,0,-1.873298645019531,0,0,0.179840087890625,0.1716156005859375,0,0.1893386840820312,0.1913604736328125,0.2031784057617188,0.2273483276367188,0.1990509033203125,0,0.228118896484375,0,0.22735595703125,0.1121902465820312,0,0,0,0,0,0,0,0,-1.783668518066406,0,0.1742324829101562,0,0.1848068237304688,0,0.188323974609375,0.2087478637695312,0,0.2237548828125,0,0.2571182250976562,0.2338638305664062,0,0,0.2337188720703125,0,0.1342926025390625,0,0,0,0,0,-1.894416809082031,0,0.16986083984375,0.178985595703125,0,0.1886749267578125,0,0.2060012817382812,0,0.2098388671875,0.2248001098632812,0,0.2346649169921875,0,0.2361602783203125,0,0,0.2297286987304688,0.07000732421875,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.869606018066406,0,0,0.060516357421875,0,0.1580657958984375,0.1706008911132812,0,0,0.18914794921875,0,0,0.2005615234375,0,0.2186965942382812,0.2337265014648438,0,0.2347946166992188,0.2266616821289062,0,0.225311279296875,0,0.00473785400390625,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.839225769042969,0,0,0,0,0,0.05069732666015625,0,0.190399169921875,0,0.1981582641601562,0,0.207183837890625,0,0.2191848754882812,0,0.2320327758789062,0.23333740234375,0,0.2209014892578125,0,0.2125701904296875,0.2352447509765625,0.2291717529296875,0,0.2295913696289062,0,0.2294769287109375,0,0,0.2343063354492188,0.249298095703125,0,0.1958847045898438,0.1963119506835938,0,0.1951446533203125,0,0.1956939697265625,0.1943740844726562,0,0.1956329345703125,0,0.1953048706054688,0,0.1948471069335938,0,0.1929779052734375,0,0,0.1921234130859375,0.1949539184570312,0,0.1939468383789062,0,0.1953277587890625,0,0.19512939453125,0.1952590942382812,0,0,0.1929550170898438,0.195526123046875,0.1852569580078125,0.1913833618164062,0.1954116821289062,0,0.1883087158203125,0,0,0.1886825561523438,0.1949005126953125,0,0.04720306396484375,0,0,0,0,0,0,0,0,-7.168754577636719,0.1976776123046875,0.2042388916015625,0.2198562622070312,0,0.2359542846679688,0.2291717529296875,0,0.2165756225585938,0,0.2224655151367188,0.238006591796875,0,0.2336883544921875,0,0.2335433959960938,0,0.23583984375,0.2352066040039062,0.2354583740234375,0,0,0.2365036010742188,0,0.2346115112304688,0,0.2346115112304688,0.23358154296875,0,0,0.234100341796875,0,0,0.2347488403320312,0.233978271484375,0.2349090576171875,0,0.234771728515625,0,0.2339096069335938,0.2348098754882812,0,0,0.2353363037109375,0,0.2352981567382812,0,0.2582855224609375,0,0.2330322265625,0,0.233367919921875,0.227996826171875,0,0.2243804931640625,0,0.2126998901367188,0,0,0,0,0,0,0,0,0,0,0,-7.081832885742188,0,0.1939468383789062,0,0.2024993896484375,0.206878662109375,0,0.2203598022460938,0,0.2166900634765625,0,0.2125701904296875,0.2289276123046875,0.2383193969726562,0,0,0.2344131469726562,0,0.2352676391601562,0.2357330322265625,0,0.2346572875976562,0.2287826538085938,0,0,0.2593231201171875,0.23162841796875,0,0.2332077026367188,0,0.233734130859375,0,0.2350006103515625,0,0.2329940795898438,0,0.2317047119140625,0.23260498046875,0.22900390625,0,0.2151641845703125,0,0.230560302734375,0,0.2307281494140625,0,0.2309417724609375,0,0.23291015625,0.232086181640625,0.2338027954101562,0.2259674072265625,0,0.222503662109375,0,0.2248153686523438,0,0.00064849853515625,0,0,0,0,0,0,0,0,-6.969894409179688,0,0.2095870971679688,0.1940383911132812,0,0.1858673095703125,0.19512939453125,0.1870803833007812,0.1921234130859375,0.2161865234375,0.2342605590820312,0.2331924438476562,0,0.2308731079101562,0,0.2332077026367188,0,0.2300491333007812,0,0.222747802734375,0.2275238037109375,0,0.2308197021484375,0.23175048828125,0,0.2295761108398438,0.2312698364257812,0,0.2317428588867188,0.2318572998046875,0,0.2313995361328125,0,0.2294769287109375,0.2304458618164062,0,0.229522705078125,0,0.2539749145507812,0,0.231231689453125,0,0.21759033203125,0,0.2246627807617188,0.2328033447265625,0,0.2167129516601562,0,0.21917724609375,0,0,0.2230224609375,0,0.0540924072265625,0,0,0,0,0,0,0,0,-6.945915222167969,0,0.1688461303710938,0,0.1905288696289062,0,0.1769332885742188,0,0.1940841674804688,0.1959304809570312,0.1964797973632812,0.2147293090820312,0.2268447875976562,0,0,0.2339248657226562,0,0.2343978881835938,0,0.255157470703125,0,0.2307510375976562,0,0.2325592041015625,0,0.23138427734375,0,0.2348098754882812,0,0,0.2311477661132812,0.2296295166015625,0.2328567504882812,0.23046875,0.2321548461914062,0.229522705078125,0,0.2291717529296875,0.2325057983398438,0.230926513671875,0,0.2324981689453125,0,0.2281036376953125,0,0.2163314819335938,0,0.2281723022460938,0.2167129516601562,0.2289962768554688,0.2212066650390625,0,0.2181167602539062,0,0.0600128173828125,0,0,0,0,0,0,0,0,-6.807525634765625,0,0.1783523559570312,0.1910552978515625,0,0.1963653564453125,0,0.193878173828125,0,0.1967849731445312,0.2136611938476562,0,0,0.234954833984375,0,0.2377548217773438,0,0.2209625244140625,0,0.2325363159179688,0.2323226928710938,0,0.231170654296875,0.23028564453125,0,0.2316513061523438,0,0.231475830078125,0,0.2308807373046875,0,0.2307510375976562,0,0.2295150756835938,0,0.2306594848632812,0.2303466796875,0,0,0.22967529296875,0,0.2316131591796875,0.2313003540039062,0,0,0.2313232421875,0,0.2561569213867188,0,0.23284912109375,0,0.2327346801757812,0.2329559326171875,0,0.2303009033203125,0.2203216552734375,0.2218017578125,0,0.0477447509765625,0,0,0,0,0,0,0,0,-6.705085754394531,0.1691741943359375,0,0.183258056640625,0.177154541015625,0.187408447265625,0.1740951538085938,0,0.1974563598632812,0,0.2144317626953125,0,0.2262954711914062,0.234832763671875,0,0.2309341430664062,0,0.2540512084960938,0,0.2311553955078125,0.2294540405273438,0.2295913696289062,0.2307510375976562,0.2304000854492188,0.2298049926757812,0,0.2281417846679688,0,0.2297439575195312,0.231475830078125,0.2299041748046875,0.2312240600585938,0.2299957275390625,0,0.2307357788085938,0,0.2323532104492188,0,0,0.232147216796875,0,0.2327346801757812,0.2326812744140625,0.2296905517578125,0,0.2237396240234375,0.223663330078125,0,0.05008697509765625,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-6.658241271972656,0,0,0,0,0,0.1459197998046875,0,0.1881256103515625,0,0.1944427490234375,0,0,0.1882553100585938,0,0.1887054443359375,0,0.22296142578125,0,0.2312774658203125,0.2267837524414062,0,0.2247848510742188,0.2203292846679688,0,0.2258758544921875,0,0.2255172729492188,0.2503509521484375,0,0.2255096435546875,0,0,0.2352752685546875,0,0.2261428833007812,0.2092132568359375,0,0.22882080078125,0,0.2164382934570312,0.2233200073242188,0,0.227752685546875,0,0.2261886596679688,0.228118896484375,0.2270660400390625,0.2227554321289062,0.2310409545898438,0,0.2260665893554688,0.2315826416015625,0,0,0.2376174926757812,0,0.2379684448242188,0.239654541015625,0,0,0.01473236083984375,0,0,0,0,0,0,0,0,-6.454170227050781,0.2039031982421875,0.18951416015625,0,0.1865310668945312,0.1893386840820312,0,0.2139053344726562,0.2303314208984375,0.2352066040039062,0.2332077026367188,0.232452392578125,0,0.231475830078125,0,0.2331695556640625,0.2314529418945312,0,0.2301177978515625,0,0.232086181640625,0.2331008911132812,0.232086181640625,0.2316436767578125,0,0.2323379516601562,0,0,0.2316207885742188,0,0.2318572998046875,0.2324371337890625,0,0.2332229614257812,0,0.2328643798828125,0,0,0.23529052734375,0.233734130859375,0,0.2343292236328125,0.2327880859375,0.2330856323242188,0,0.23480224609375,0.07352447509765625,0,0,0,0,0,-6.372901916503906,0.179443359375,0.1693344116210938,0,0.1809844970703125,0.1822662353515625,0,0.2080001831054688,0.227569580078125,0,0.2307662963867188,0.2331390380859375,0.2298736572265625,0,0.2265548706054688,0,0.229705810546875,0,0,0.2279434204101562,0,0,7.724212646484375,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7.62939453125,0,0,7.62939453125e-06,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,15.2587890625,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7.629417419433594,0,0,0,0,0,0,0,0.03520965576171875,0,0,0,0,0,0,0,15.3599853515625,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"filename":["<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,null,null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>","<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,null,null,null,null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,null,null,null,null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,null,null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,null,null,null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,null,null,null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,null,null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,null,null,null,null,null,null,null,null,null,null,null,"<expr>","<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null]},"interval":10,"files":[{"filename":"<expr>","content":"## Generate Large Random Dataset\nn <- 2e6\nx <- runif(n)\ny <- runif(n)\nz <- runif(n)\nXYZ <- cbind(x,y,z)\n\n## Inspect 4 equivalent `row mean` calculations \nprofvis::profvis({\n    m <- rowSums(XYZ)/ncol(XYZ)\n    m <- rowMeans(XYZ)\n    m <- apply(XYZ, 1, mean)\n    m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }\n})\n## rowSums(), colSums(), rowMeans(), and colMeans() are vectorised and fast.\n## for loop is not the slowest, but the ugliest.","normpath":"<expr>"}],"prof_output":"/tmp/RtmpwL8mAL/file29c54386f703.prof","highlight":{"output":["^output\\$"],"gc":["^<GC>$"],"stacktrace":["^\\.\\.stacktraceo(n|ff)\\.\\.$"]},"split":"h"}},"evals":[],"jsHooks":[]}</script>
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
## 1 mean1(x, 0.5)     36ms   37.4ms      26.3    7.63MB     0   
## 2 mean2(x, 0.5)   32.6ms   39.6ms      25.4    7.63MB     2.12
## 3 mean3(x, 0.5)   36.3ms   37.1ms      26.9    7.63MB     0
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
##   0.121   0.000   0.043
```

```r
system.time({ lm(Y~X, data=DAT) })
```

```
##    user  system elapsed 
##   0.522   0.000   0.185
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
## 1 ma1(y)      281.6ms  281.6ms      3.55    15.3MB     3.55
## 2 ma2(y)       32.1ms   32.6ms     30.7     91.6MB   169.
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
##   0.039   0.002   0.042
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
##   1.288   0.354   0.935
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





