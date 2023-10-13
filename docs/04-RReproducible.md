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
<div class="plotly html-widget html-fill-item-overflow-hidden html-fill-item" id="htmlwidget-5a9c563d1f0977145345" style="width:672px;height:480px;"></div>
<script type="application/json" data-for="htmlwidget-5a9c563d1f0977145345">{"x":{"visdat":{"44c3918b2e9":["function () ","plotlyVisDat"]},"cur_data":"44c3918b2e9","attrs":{"44c3918b2e9":{"x":{},"y":{},"alpha_stroke":1,"sizes":[10,100],"spans":[1,20]}},"layout":{"margin":{"b":40,"l":60,"t":25,"r":10},"xaxis":{"domain":[0,1],"automargin":true,"title":"X"},"yaxis":{"domain":[0,1],"automargin":true,"title":"Y"},"hovermode":"closest","showlegend":false},"source":"A","config":{"modeBarButtonsToAdd":["hoverclosest","hovercompare"],"showSendToCloud":false},"data":[{"x":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100],"y":[4.2960844100071442,8.905942726230526,10.204646688632696,14.18159788924515,17.468504139392074,22.04402815782689,28.312002989993296,30.813056746346479,37.089300052405243,40.046006941864427,44.81071423707003,46.220355543879208,53.582777640103437,56.770932320063835,56.798259457149655,63.427831589011106,74.80106600990301,72.468197395238718,76.189215012550264,81.174403268433494,83.034688772866318,90.022828926604291,92.273287600090697,94.578258883345669,99.15370010368045,103.71798511932246,110.9725117900669,108.41999734916043,112.625151358412,121.3760514565799,120.86920343556555,130.95769277292868,128.65044672825371,132.41020259268842,142.86692291799565,146.87368370527597,149.8316414427,155.03776474488703,154.56550703575871,157.45732773865669,160.94411204775824,166.00524883672082,172.66797192798154,180.28304746425903,181.39223640472559,181.03015890222557,183.34381891358174,190.73868785731383,198.7944494649422,201.74222566586843,200.4182743095831,206.29483263752871,210.66148333304034,217.00879446760112,219.35356521931658,223.31330359099874,229.61412122082629,230.36606813198293,236.15315827117263,240.13136475709268,244.00423944110406,252.96779615862854,253.34955559305942,258.68711655433333,258.83291624454915,266.35960622447004,267.21923222623786,271.71145113197031,276.56091947042398,283.75188562161276,284.61804103079942,284.34469430447564,290.93154378671437,292.89813137718403,301.88457916877729,305.04964457685332,308.69859583079483,309.91042989945726,313.80938392403232,318.34579686734213,324.8554391706968,331.05534361651803,334.35547850913173,333.29405103469287,337.91985624681325,343.63183655043059,346.91404839843386,350.51617591358291,355.45549006732051,358.05795421823376,365.87380297391019,363.27117428729014,372.13774775021255,375.12014887095404,380.36813587317869,381.74671906765656,386.64120878953571,394.40039961474054,395.93661833100106,401.36566969480327],"type":"scatter","mode":"markers","marker":{"color":"rgba(31,119,180,1)","line":{"color":"rgba(31,119,180,1)"}},"error_y":{"color":"rgba(31,119,180,1)"},"error_x":{"color":"rgba(31,119,180,1)"},"line":{"color":"rgba(31,119,180,1)"},"xaxis":"x","yaxis":"y","frame":null}],"highlight":{"on":"plotly_click","persistent":false,"dynamic":false,"selectize":false,"opacityDim":0.20000000000000001,"selected":{"opacity":1},"debounce":0},"shinyEvents":["plotly_hover","plotly_click","plotly_selected","plotly_relayout","plotly_brushed","plotly_brushing","plotly_clickannotation","plotly_doubleclick","plotly_deselect","plotly_afterplot","plotly_sunburstclick"],"base_url":"https://plot.ly"},"evals":[],"jsHooks":[]}</script>
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
## Ncells 1209814 64.7    2358980  126  2358980 126.0
## Vcells 2294705 17.6    8388608   64  3574492  27.3
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
<div class="profvis html-widget html-fill-item-overflow-hidden html-fill-item" id="htmlwidget-62f8bf5e63ed6de9023f" style="width:100%;height:600px;"></div>
<script type="application/json" data-for="htmlwidget-62f8bf5e63ed6de9023f">{"x":{"message":{"prof":{"time":[1,2,3,4,5,5,6,7,8,9,10,10,11,11,12,12,13,13,14,14,15,15,16,16,17,17,18,18,19,19,20,20,21,21,22,22,23,23,24,24,24,25,25,26,27,27,28,28,29,30,31,31,31,32,33,33,34,34,35,35,36,36,37,38,38,39,40,40,40,41,41,42,42,43,43,43,44,44,45,45,46,46,46,47,48,48,49,49,49,50,50,51,51,52,52,53,53,54,54,55,55,56,56,57,58,58,59,59,60,61,62,62,63,63,64,64,65,65,66,66,67,67,68,68,69,70,71,71,71,72,73,73,74,74,75,75,75,76,77,77,78,79,79,80,80,81,81,82,83,83,84,85,86,86,87,87,88,89,89,90,90,91,91,92,92,92,93,93,94,94,95,95,96,96,97,97,98,98,99,99,100,100,101,101,101,102,103,104,104,105,106,106,107,107,108,108,109,109,109,110,111,111,112,113,114,115,115,116,116,116,117,117,117,118,118,119,120,120,121,122,123,124,124,125,125,126,126,127,128,128,129,129,130,130,131,131,132,132,133,133,134,134,135,135,135,136,137,138,139,139,140,140,141,141,142,142,143,143,144,144,145,145,146,146,147,147,148,149,149,150,150,150,151,152,152,152,153,153,153,154,155,155,156,156,156,157,158,158,158,159,159,160,160,161,161,162,163,164,164,165,165,166,166,167,167,168,169,170,171,171,172,172,173,173,174,174,175,175,176,176,177,178,178,179,180,180,181,182,182,182,183,183,184,185,186,186,186,187,188,188,189,190,190,190,191,191,192,193,193,194,195,195,196,197,198,198,198,199,199,199,200,200,200,201,201,201,202,202,202,203,203,203,204,204,204,205,205,205,206,206,206,207,208,208,209,209,210,211,212,212,213,214,214,215,215,215,216,216,217,217,218,218,219,220,221,221,222,222,222,223,223,223,224,224,224,225,226,227,227,228,228,229,229,230,230,231,231,232,232,233,233,233,234,235,235,235,236,236,237,237,238,238,239,239,240,240,241,241,242,243,243,244,244,245,245,245,246,246,247,247,248,248,249,249,250,250,251,251,252,252,252,253,253,253,254,254,255,255,256,257,257,258,258,258,259,260,260,261,261,262,262,263,264,265,266,266,267,267,267,268,269,269,270,270,271,271,272,272,272,273,273,274,274,275,275,275,276,276,277,277,278,278,279,279,280,280,281,281,281,282,283,283,284,285,286,286,287,287,288,288,289,289,290,291,292,292,293,293,294,294,295,295,295,296,296,297,297,298,298,299,299,300,301,301,301,302,302,302,303,303,303,304,304,304,305,305,306,306,307,307,308,308,308,309,309,309,310,310,311,311,312,312,313,313,314,314,315,315,316,316,316,317,318,319,320,320,320,321,321,322,322,323,323,324,324,325,326,326,327,327,328,329,329,329,330,330,331,332,332,333,334,334,335,336,336,336,336,337,338,338,339,339,340,340,341,342,342,342,343,343,344,344,345,345,346,347,348,348,348,349,349,349,350,350,351,351,352,353,354,355,355,356,356,357,357,358,358,359,359,360,360,361,361,362,362,363,363,364,364,365,365,366,366,367,367,368,368,369,369,370,370,371,371,372,372,373,373,374,374,375,375,376,376,377,377,378,378,379,379,380,380,381,381,382,382,383,384,384,385,386,386,387,387,388,389,389,390,390,390,391,392,392,393,393,394,394,395,395,395,396,397,397,398,398,399,400,400,401,402,403,404,404,405,405,406,407,408,408,408,409,409,409,410,410,411,411,412,412,413,413,414,414,414,415,415,416,416,417,417,418,419,420,420,421,421,422,422,422,423,423,423,424,425,425,426,426,427,428,429,429,429,430,431,431,432,432,433,433,434,434,435,436,436,437,438,438,439,439,440,441,441,442,442,443,443,443,444,445,445,446,447,447,448,449,449,450,450,451,451,452,452,453,453,454,455,455,456,456,457,457,458,459,459,460,461,462,463,463,464,464,465,465,466,466,467,467,468,468,469,470,470,471,471,472,473,473,474,474,475,475,475,476,476,476,477,477,478,479,480,480,480,481,481,482,482,482,483,483,483,484,484,485,485,486,486,487,488,488,489,489,489,490,490,491,491,492,492,492,493,493,494,494,495,495,496,496,496,497,497,498,498,499,500,500,501,501,502,502,502,502,503,504,504,505,505,506,507,507,508,508,509,510,511,512,512,512,513,514,514,514,515,515,516,516,517,517,518,518,519,520,521,522,522,523,523,524,524,525,525,526,526,527,527,528,528,528,529,529,530,530,531,532,532,533,533,534,534,535,536,536,537,537,538,538,539,539,540,540,541,541,542,542,543,543,544,544,545,545,546,547,547,548,549,550,550,550,551,552,552,553,553,554,554,555,555,556,556,557,557,558,558,559,559,560,561,561,561,562,563,563,564,564,564,565,565,566,566,567,567,568,568,569,570,571,571,572,572,573,574,574,575,576,577,577,578,578,578,578,579,579,579,579,580,581,582,582,583,583,584,585,585,586,586,587,588,588,589,590,591,591,591,592,592,593,593,594,594,595,596,596,597,598,598,598,599,600,601,601,602,602,603,603,603,604,604,605,605,606,606,607,608,608,609,609,610,611,612,612,613,613,614,615,615,616,616,617,618,618,619,619,619,620,621,621,622,622,623,624,624,625,625,626,626,627,627,628,628,629,630,630,631,631,632,632,633,633,634,634,635,635,636,637,637,638,639,639,640,640,641,642,642,643,643,644,644,645,645,646,646,647,647,648,648,649,650,650,650,651,651,651,652,652,652,653,653,653,654,654,654,655,655,655,656,656,656,657,657,657,658,658,658,659,659,659,660,660,660,661,661,661,662,662,662,663,663,663,664,664,665,666,667,668,668,669,669,670,671,671,672,672,673,673,674,674,675,675,676,676,677,677,678,678,679,679,680,680,681,681,682,683,683,683,684,685,685,686,686,686,687,687,687,688,688,688,689,689,690,691,691,691,692,693,693,694,695,695,696,696,697,697,697,698,699,699,700,700,701,701,701,702,702,703,703,704,705,705,706,707,708,709,709,709,710,710,710,711,711,711,712,712,713,713,714,715,716,717,717,718,719,719,720,721,721,721,722,722,722,723,723,723,724,725,725,726,726,727,727,728,728,729,729,730,731,731,732,733,733,734,734,734,735,735,735,736,736,737,737,738,739,739,739,740,740,741,741,741,742,742,743,743,744,745,745,745,746,746,746,747,748,749,749,750,750,751,751,752,753,754,755,755,756,756,757,757,757,758,758,758,759,759,760,761,761,762,762,763,763,763,764,764,764,765,766,767,767,768,768,768,769,769,769,770,770,770,771,772,772,773,773,774,774,775,776,776,777,778,779,779,779,779,780,780,780,780,781,782,782,783,784,785,786,787,788,788,789,789,790,790,791,791,792,792,793,794,794,795,796,797,797,798,798,799,799,800,800,800,801,801,801,802,802,803,803,804,805,805,806,806,807,807,808,809,809,810,810,811,811,811,812,812,812,813,813,814,815,815,816,817,818,818,819,819,820,820,821,821,822,822,822,823,823,823,824,825,826,826,827,827,828,828,829,829,830,830,831,832,832,833,833,833,834,835,836,836,837,837,838,838,839,840,841,842,843,843,843,844,844,844,845,845,846,847,847,848,848,849,849,850,850,851,851,851,852,852,853,853,854,854,855,856,856,857,857,858,858,859,860,861,861,862,862,863,863,864,864,865,865,866,866,867,867,868,869,869,870,870,871,872,873,873,874,874,875,875,876,876,877,877,878,878,879,879,880,881,882,882,882,883,883,884,885,885,886,886,887,887,888,888,889,890,891,891,892,892,893,893,894,894,895,895,896,896,896,897,897,898,898,899,899,900,900,901,901,902,902,903,903,904,904,905,905,906,906,907,908,908,909,909,910,910,911,911,912,912,913,913,914,915,916,917,917,917,918,919,919,920,920,920,921,922,923,923,924,924,925,925,926,926,927,927,928,928,929,929,929,930,930,931,931,932,932,932,933,934,935,935,935,936,936,937,937,938,938,939,939,939,940,941,942,942,943,944,945,945,945,946,946,946,947,947,947,948,949,950,951,951,952,952,953,953,954,954,955,955,955,956,957,957,958,958,958,959,959,960,960,961,961,962,963,964,964,964,965,965,965,966,967,967,968,968,969,970,971,972,972,973,973,974,974,974,974,975,975,975,975,976,977,977,978,979,980,981,982,982,983,983,984,984,984,985,985,985,986,986,987,988,988,989,989,990,990,991,991,992,992,993,993,993,993,994,994,994,994,995,995,996,997,997,998,998,999,999,1000,1000,1001,1001,1002,1002,1002,1003,1003,1003,1004,1004,1005,1006,1007,1007,1008,1009,1010,1010,1010,1011,1011,1011,1012,1012,1012,1013,1013,1014,1014,1015,1016,1017,1017,1018,1019,1019,1020,1020,1020,1021,1021,1021,1022,1023,1023,1024,1024,1025,1026,1027,1028,1029,1029,1029,1030,1030,1030,1031,1031,1032,1032,1032,1033,1033,1034,1034,1035,1035,1036,1036,1037,1037,1038,1038,1039,1039,1040,1040,1041,1041,1042,1042,1043,1044,1044,1045,1045,1046,1046,1047,1047,1047,1048,1048,1048,1049,1049,1049,1050,1050,1050,1051,1051,1051,1052,1052,1052,1053,1053,1053,1054,1055,1056,1056,1056,1057,1057,1058,1058,1059,1059,1060,1060,1061,1061,1061,1062,1062,1062,1063,1063,1063,1064,1064,1064,1065,1065,1065,1066,1066,1066,1067,1067,1067,1068,1068,1068,1069,1069,1069,1070,1070,1070,1071,1071,1071,1072,1072,1072,1073,1073,1073,1074,1074,1074,1075,1075,1075,1076,1076,1076,1077,1077,1077,1078,1078,1078,1079,1079,1079,1080,1080,1080,1081,1081,1081,1082,1082,1082,1083,1083,1083,1084,1084,1084,1085,1085,1085,1086,1086,1086,1087,1087,1087,1088,1088,1088,1089,1089,1089,1090,1090,1090,1091,1091,1091,1092,1092,1092,1093,1093,1093,1094,1094,1094,1095,1095,1095,1096,1096,1096,1097,1097,1097,1098,1098,1098,1099,1099,1099,1100,1100,1100,1101,1101,1101,1102,1102,1102,1103,1103,1103,1104,1104,1104,1105,1105,1105,1106,1106,1106,1107,1107,1107,1108,1108,1108,1109,1109,1109,1110,1110,1110,1111,1111,1111,1112,1112,1112,1113,1113,1113,1114,1114,1114,1115,1115,1115,1116,1116,1116,1117,1117,1117,1118,1118,1119,1120,1120,1121,1121,1121,1122,1122,1123,1124,1125,1125,1126,1126,1127,1127,1128,1129,1129,1130,1130,1131,1131,1132,1132,1133,1134,1134,1135,1136,1136,1137,1137,1138,1139,1140,1141,1142,1142,1142,1143,1143,1143,1144,1144,1145,1145,1145,1146,1146,1147,1148,1148,1149,1149,1150,1150,1151,1151,1152,1152,1153,1153,1154,1154,1155,1155,1156,1156,1157,1157,1158,1158,1159,1159,1160,1160,1160,1161,1162,1163,1163,1164,1164,1165,1165,1166,1166,1167,1167,1168,1168,1169,1170,1170,1171,1171,1172,1172,1173,1173,1174,1174,1175,1175,1176,1177,1177,1177,1178,1179,1179,1180,1180,1180,1181,1182,1182,1183,1183,1184,1184,1184,1185,1185,1186,1187,1187,1188,1188,1189,1189,1190,1190,1191,1191,1192,1192,1193,1193,1194,1194,1195,1195,1196,1196,1197,1197,1198,1199,1199,1200,1200,1201,1201,1202,1202,1203,1204,1204,1205,1206,1206,1206,1207,1208,1208,1209,1210,1211,1211,1212,1212,1213,1213,1213,1214,1214,1214,1215,1215,1215,1216,1217,1217,1217,1218,1219,1220,1220,1221,1221,1222,1222,1223,1223,1224,1224,1225,1226,1227,1227,1228,1228,1228,1229,1229,1230,1230,1231,1232,1232,1233,1234,1234,1235,1235,1236,1236,1236,1237,1237,1237,1238,1238,1238,1239,1239,1240,1240,1241,1242,1242,1243,1244,1245,1246,1246,1247,1248,1248,1249,1249,1250,1250,1251,1252,1252,1253,1254,1254,1255,1256,1256,1257,1257,1258,1258,1259,1259,1260,1260,1261,1262,1263,1263,1264,1265,1265,1266,1267,1267,1268,1268,1269,1269,1270,1270,1270,1271,1271,1272,1272,1273,1273,1274,1274,1275,1275,1276,1276,1277,1278,1278,1279,1279,1280,1280,1281,1281,1282,1282,1283,1283,1284,1284,1285,1285,1286,1286,1287,1287,1288,1288,1289,1289,1290,1290,1291,1291,1292,1292,1293,1293,1294,1295,1295,1296,1296,1296,1297,1297,1298,1298,1299,1299,1300,1301,1301,1302,1302,1303,1304,1305,1305,1306,1306,1307,1307,1308,1308,1309,1310,1310,1310,1311,1311,1311,1312,1312,1313,1314,1315,1315,1316,1316,1317,1318,1318,1319,1319,1320,1321,1321,1322,1322,1323,1323,1323,1324,1324,1324,1325,1325,1326,1327,1327,1327,1328,1329,1330,1331,1331,1331,1332,1332,1332,1333,1333,1333,1334,1334,1335,1335,1336,1336,1337,1338,1338,1339,1339,1340,1340,1341,1341,1342,1342,1343,1343,1344,1344,1344,1345,1345,1346,1346,1347,1347,1348,1348,1349,1349,1350,1350,1351,1351,1352,1352,1353,1353,1354,1354,1355,1355,1356,1357,1357,1358,1358,1359,1359,1360,1360,1361,1361,1362,1362,1363,1363,1364,1364,1365,1365,1366,1366,1367,1367,1368,1368,1369,1369,1370,1370,1371,1371,1372,1372,1373,1373,1374,1374,1375,1375,1376,1376,1377,1377,1377,1377,1377,1377,1377,1377,1378,1378,1378,1378,1378,1378,1378,1378,1378,1378,1378,1378,1378,1378,1378,1378,1378,1379,1379,1379,1379,1379,1379,1379,1379,1380,1380,1380,1380,1380,1380,1380,1380,1381,1381,1381,1381,1381,1381,1381,1381,1382,1382,1382,1382,1382,1382,1382,1382,1383,1383,1383,1383,1383,1383,1383,1383,1384,1384,1384,1384,1384,1384,1384,1384,1385,1385,1385,1385,1385,1385,1385,1385,1386,1386,1386,1386,1386,1386,1386,1386,1387,1387,1387,1387,1387,1387,1387,1387,1388,1388,1388,1388,1388,1388,1388,1388,1389,1389,1389,1389,1389,1389,1389,1389,1390,1390,1390,1390,1390,1390,1390,1390,1391,1391,1391,1391,1391,1391,1391,1391,1392,1392,1392,1392,1392,1392,1392,1392,1393,1393,1393,1393,1393,1393,1393,1393,1394,1394,1394,1394,1394,1394,1394,1394,1395,1395,1395,1395,1395,1395,1395,1395,1396,1396,1396,1396,1396,1396,1396,1396,1397,1397,1397,1397,1397,1397,1397,1397],"depth":[1,1,1,1,2,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,1,1,3,2,1,1,2,1,2,1,2,1,2,1,1,2,1,1,3,2,1,2,1,2,1,3,2,1,2,1,2,1,3,2,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,3,2,1,1,2,1,2,1,3,2,1,1,2,1,1,2,1,2,1,2,1,1,2,1,1,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,1,2,1,1,2,1,2,1,2,1,3,2,1,1,2,1,1,1,1,2,1,3,2,1,3,2,1,2,1,1,2,1,1,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,1,3,2,1,3,2,1,1,2,1,3,2,1,1,3,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,1,3,2,1,2,1,1,1,3,2,1,1,2,1,1,3,2,1,2,1,1,2,1,1,2,1,1,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,1,2,1,2,1,1,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,1,1,2,1,3,2,1,3,2,1,3,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,3,2,1,1,2,1,2,1,2,1,1,1,1,2,1,3,2,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,1,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,1,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,3,2,1,2,1,1,2,1,1,2,1,1,4,3,2,1,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,2,1,1,1,3,2,1,3,2,1,2,1,2,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,1,2,1,3,2,1,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,1,2,1,1,1,1,2,1,2,1,1,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,1,2,1,2,1,3,2,1,3,2,1,1,2,1,2,1,1,1,3,2,1,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,1,2,1,2,1,3,2,1,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,2,1,1,1,3,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,3,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,4,3,2,1,1,2,1,2,1,1,2,1,2,1,1,1,1,3,2,1,1,3,2,1,2,1,2,1,2,1,2,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,1,2,1,1,1,2,1,4,3,2,1,4,3,2,1,1,1,2,1,2,1,1,2,1,2,1,1,2,1,1,1,3,2,1,2,1,2,1,2,1,1,2,1,1,3,2,1,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,1,1,2,1,2,1,1,2,1,2,1,1,2,1,3,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,1,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,1,2,1,3,2,1,3,2,1,3,2,1,2,1,1,3,2,1,1,2,1,1,2,1,2,1,3,2,1,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,1,1,1,3,2,1,3,2,1,3,2,1,2,1,2,1,1,1,1,2,1,1,2,1,1,3,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,3,2,1,3,2,1,2,1,2,1,1,3,2,1,2,1,3,2,1,2,1,2,1,1,3,2,1,3,2,1,1,1,2,1,2,1,2,1,1,1,1,2,1,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,1,1,2,1,3,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,1,2,1,1,1,4,3,2,1,4,3,2,1,1,2,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,2,1,1,2,1,1,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,1,1,2,1,2,1,2,1,1,1,1,1,3,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,1,3,2,1,1,2,1,3,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,3,2,1,1,1,3,2,1,2,1,2,1,2,1,3,2,1,1,1,2,1,1,1,3,2,1,3,2,1,3,2,1,1,1,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,3,2,1,2,1,2,1,2,1,1,1,3,2,1,3,2,1,1,2,1,2,1,1,1,1,2,1,2,1,4,3,2,1,4,3,2,1,1,2,1,1,1,1,1,2,1,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,4,3,2,1,4,3,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,1,1,2,1,1,1,3,2,1,3,2,1,3,2,1,2,1,2,1,1,1,2,1,1,2,1,3,2,1,3,2,1,1,2,1,2,1,1,1,1,1,3,2,1,3,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,1,1,3,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,1,2,1,3,2,1,2,1,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,1,1,1,1,3,2,1,3,2,1,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,1,2,1,3,2,1,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,1,3,2,1,1,2,1,1,1,2,1,2,1,3,2,1,3,2,1,3,2,1,1,3,2,1,1,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,3,2,1,2,1,2,1,1,2,1,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,1,1,1,2,1,1,2,1,2,1,2,1,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,1,2,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,2,1,1,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,2,1,1,3,2,1,1,1,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,8,7,6,5,4,3,2,1,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1],"label":["rowSums","rowSums","rowSums","rowSums","/","local","rowMeans","rowMeans","rowMeans","rowMeans","aperm.default","apply","aperm.default","apply","aperm.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","is.na","local","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","mean.default","apply","apply","apply","<GC>","FUN","apply","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","apply","mean.default","apply","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","apply","mean.default","apply","<GC>","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","length","local","mean.default","apply","apply","mean.default","apply","FUN","apply","apply","apply","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","<GC>","apply","FUN","apply","mean.default","apply","apply","apply","isTRUE","mean.default","apply","apply","is.na","local","mean.default","apply","<GC>","FUN","apply","apply","mean.default","apply","apply","mean.default","apply","length","local","FUN","apply","apply","<GC>","apply","apply","apply","FUN","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","length","local","<GC>","is.na","local","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","<GC>","FUN","apply","apply","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","<GC>","FUN","apply","apply","FUN","apply","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","mean.default","apply","apply","apply","apply","FUN","apply","mean.default","apply","<GC>","apply","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","is.numeric","local","mean.default","apply","<GC>","apply","isTRUE","mean.default","apply","apply","apply","apply","FUN","apply","mean.default","apply","FUN","apply","<GC>","apply","FUN","apply","mean.default","apply","length","local","mean.default","apply","mean.default","apply","apply","is.na","local","<GC>","mean.default","apply","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","isTRUE","mean.default","apply","apply","<GC>","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","apply","FUN","apply","FUN","apply","<GC>","apply","FUN","apply","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","apply","mean.default","apply","FUN","apply","apply","FUN","apply","apply","mean.default","apply","apply","<GC>","FUN","apply","mean.default","apply","apply","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","<GC>","FUN","apply","FUN","apply","apply","FUN","apply","apply","length","local","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","FUN","apply","mean.default","apply","apply","apply","length","local","apply","FUN","apply","<GC>","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","apply","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","apply","apply","mean.default","apply","FUN","apply","FUN","apply","<GC>","apply","length","local","mean.default","apply","isTRUE","mean.default","apply","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","<GC>","apply","length","local","length","local","FUN","apply","apply","FUN","apply","mean.default","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","length","local","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","apply","<GC>","apply","mean.default","apply","FUN","apply","apply","apply","apply","FUN","apply","<GC>","is.na","local","apply","FUN","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","is.na","local","FUN","apply","<GC>","is.na","local","apply","mean.default","apply","apply","apply","length","local","FUN","apply","<GC>","apply","mean.default","apply","apply","apply","FUN","apply","mean.default","apply","FUN","apply","<GC>","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","<GC>","mean.default","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","length","local","isTRUE","mean.default","apply","<GC>","length","local","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","<GC>","mean.default","apply","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","apply","<GC>","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","apply","<GC>","mean.default","apply","FUN","apply","apply","mean.default","apply","apply","mean.default","apply","apply","<GC>","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","FUN","apply","apply","<GC>","length","local","FUN","apply","FUN","apply","mean.default","apply","apply","apply","<GC>","length","local","<GC>","length","local","FUN","apply","mean.default","apply","apply","apply","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","mean.default","apply","FUN","apply","FUN","apply","apply","length","local","apply","FUN","apply","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","is.na","local","<GC>","is.numeric","local","apply","mean.default","apply","FUN","apply","apply","FUN","apply","apply","apply","apply","FUN","apply","mean.default","apply","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","is.numeric","local","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","apply","mean.default","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","mean.default","apply","length","local","apply","apply","isTRUE","mean.default","apply","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","<GC>","apply","apply","is.na","local","FUN","apply","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","mean.default","apply","apply","is.numeric","local","apply","<GC>","apply","<GC>","apply","mean.default","apply","FUN","apply","is.numeric","local","apply","FUN","apply","FUN","apply","mean.default","apply","apply","FUN","apply","apply","apply","apply","<GC>","apply","mean.default","apply","mean.default","apply","length","local","FUN","apply","is.na","local","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","<GC>","mean.default","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","FUN","apply","<GC>","FUN","apply","FUN","apply","is.numeric","local","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","apply","is.na","local","FUN","apply","<GC>","isTRUE","mean.default","apply","apply","mean.default","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","apply","apply","apply","isTRUE","mean.default","apply","apply","isTRUE","mean.default","apply","<GC>","apply","FUN","apply","is.numeric","local","FUN","apply","apply","apply","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","<GC>","mean.default","apply","mean.default","apply","is.numeric","local","apply","mean.default","apply","FUN","apply","FUN","apply","apply","mean.default","apply","FUN","apply","length","local","mean.default","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","apply","FUN","apply","<GC>","apply","<GC>","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","apply","isTRUE","mean.default","apply","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","<GC>","apply","mean.default","apply","FUN","apply","apply","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","apply","apply","FUN","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","apply","apply","FUN","apply","FUN","apply","apply","is.numeric","local","mean.default","apply","apply","mean.default","apply","apply","apply","<GC>","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","mean.default","apply","apply","<GC>","apply","<GC>","apply","apply","is.na","local","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","apply","<GC>","apply","apply","length","local","length","local","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","apply","FUN","apply","FUN","apply","mean.default","apply","is.na","local","FUN","apply","FUN","apply","mean.default","apply","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","apply","apply","apply","FUN","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","mean.default","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","apply","isTRUE","mean.default","apply","apply","mean.default","apply","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","apply","<GC>","apply","length","local","isTRUE","mean.default","apply","mean.default","apply","is.na","local","apply","FUN","apply","apply","apply","apply","isTRUE","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","apply","apply","apply","mean.default","apply","apply","FUN","apply","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","apply","FUN","apply","FUN","apply","mean.default","apply","apply","apply","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","is.na","local","is.numeric","local","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","isTRUE","mean.default","apply","apply","mean.default","apply","is.na","local","FUN","apply","apply","FUN","apply","apply","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","apply","mean.default","apply","apply","apply","apply","apply","apply","mean.default","apply","FUN","apply","<GC>","apply","<GC>","apply","mean.default","apply","apply","FUN","apply","apply","apply","FUN","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","is.na","local","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","mean.default","apply","apply","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","apply","is.na","local","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","apply","FUN","apply","<GC>","mean.default","apply","apply","apply","is.numeric","local","FUN","apply","FUN","apply","apply","apply","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","apply","<GC>","apply","apply","mean.default","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","apply","<GC>","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","apply","apply","FUN","apply","FUN","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","<GC>","apply","<GC>","apply","<GC>","apply","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","length","local","mean.default","apply","isTRUE","mean.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","is.numeric","local","apply","apply","apply","<GC>","is.na","local","apply","mean.default","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","<GC>","apply","<GC>","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","apply","apply","isTRUE","mean.default","apply","<GC>","apply","<GC>","apply","mean.default","apply","isTRUE","mean.default","apply","apply","apply","mean.default","apply","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","apply","apply","apply","is.na","local","FUN","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","mean.default","apply","FUN","apply","apply","apply","apply","FUN","apply","FUN","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","apply","FUN","apply","apply","apply","apply","apply","is.na","local","FUN","apply","<GC>","is.numeric","local","<GC>","is.numeric","local","mean.default","apply","apply","FUN","apply","length","local","FUN","apply","FUN","apply","FUN","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","length","local","apply","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","<GC>","length","local","<GC>","length","local","FUN","apply","apply","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","mean.default","apply","apply","apply","FUN","apply","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","is.na","local","FUN","apply","apply","apply","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","<GC>","apply","<GC>","apply","mean.default","apply","FUN","apply","FUN","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","apply","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","FUN","apply","FUN","apply","length","local","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","apply","apply","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","length","local","mean.default","apply","length","local","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","is.numeric","local","mean.default","apply","<GC>","apply","<GC>","apply","FUN","apply","is.numeric","local","apply","mean.default","apply","length","local","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","is.na","local","FUN","apply","mean.default","apply","is.numeric","local","apply","FUN","apply","length","local","FUN","apply","mean.default","apply","apply","mean.default","apply","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","is.numeric","local","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","apply","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","<GC>","apply","<GC>","apply","<GC>","apply","apply","apply","mean.default","apply","apply","FUN","apply","apply","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","is.numeric","local","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","apply","FUN","apply","mean.default","apply","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","apply","apply","FUN","apply","is.numeric","local","apply","FUN","apply","FUN","apply","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","apply","isTRUE","mean.default","apply","apply","apply","apply","<GC>","length","local","<GC>","length","local","<GC>","length","local","FUN","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","findCenvVar","getInlineInfo","tryInline","cmpCall","cmp","h","tryInline","cmpCall","cmp","cmpForBody","h","tryInline","cmpCall","cmp","genCode","compile","compiler:::tryCompile","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis"],"filenum":[1,1,1,1,1,null,1,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,null,1,null,null,1,null,1,1,null,1,null,1,1,1,null,null,1,1,null,1,null,1,null,1,null,1,1,null,1,1,null,null,1,null,1,null,1,null,null,1,null,1,null,1,null,null,1,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,null,null,1,1,null,1,null,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,1,null,null,1,1,null,null,null,1,null,null,1,1,null,1,1,null,1,null,null,null,1,1,null,1,1,1,null,1,null,1,1,null,1,null,1,null,null,null,null,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,1,1,null,1,1,null,1,null,1,null,1,null,null,1,1,null,1,1,1,1,null,1,null,null,1,null,null,1,null,1,1,null,1,1,1,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,null,null,1,null,1,null,null,1,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,null,1,null,1,1,null,null,null,null,1,1,null,null,1,null,null,1,1,null,1,null,null,1,1,null,null,1,null,1,null,1,null,1,1,1,null,1,null,1,null,1,null,1,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,1,null,1,1,null,null,1,null,1,1,1,null,null,1,1,null,1,1,null,null,1,null,1,1,null,1,1,null,null,1,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,1,null,1,null,1,1,1,null,null,1,null,1,null,null,1,null,1,null,1,null,1,1,1,null,1,null,null,1,null,null,1,null,null,1,1,1,null,1,null,1,null,1,null,1,null,null,null,1,null,null,1,1,null,null,1,null,1,null,1,null,1,null,null,null,null,null,1,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,null,null,1,1,null,1,null,null,1,1,null,1,null,1,null,1,1,1,1,null,1,null,null,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,null,null,1,null,null,null,1,null,1,1,1,null,null,null,1,null,1,null,1,1,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,null,null,null,1,null,null,null,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,1,1,1,null,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,1,null,null,1,null,1,1,null,1,1,null,1,1,null,null,null,1,1,null,1,null,1,null,1,1,null,null,null,null,1,null,1,null,1,1,1,null,null,null,null,null,null,null,1,null,1,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,null,1,null,1,null,1,1,null,1,null,null,1,1,null,1,null,1,null,null,null,null,null,1,null,1,null,1,1,null,1,1,1,1,null,1,null,1,1,1,null,null,1,null,null,1,null,1,null,1,null,1,null,null,null,null,1,null,1,null,1,null,1,1,1,null,1,null,1,null,null,1,null,null,1,1,null,1,null,null,1,1,null,null,1,1,null,1,null,1,null,1,null,1,1,null,1,1,null,null,null,1,1,null,1,null,1,null,null,1,1,null,1,1,null,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,1,null,1,1,1,1,null,1,null,1,null,1,null,null,null,1,null,null,1,null,1,null,1,1,null,1,null,1,null,null,1,null,null,1,null,1,1,1,null,null,1,null,1,null,null,1,null,null,1,null,1,null,1,null,1,1,null,1,null,null,1,null,1,null,null,null,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,1,null,null,null,1,null,null,null,1,1,null,1,null,1,1,null,1,null,1,1,1,1,null,null,1,1,null,null,1,null,1,null,1,null,null,null,1,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,null,1,null,1,null,1,null,1,1,null,1,null,1,null,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,1,1,null,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,null,1,1,null,1,null,null,1,null,1,null,1,null,1,null,1,1,1,null,1,null,1,1,null,1,1,1,null,1,null,null,null,1,null,null,null,1,1,1,null,1,null,1,1,null,null,null,1,1,null,1,1,1,null,null,1,null,1,null,1,null,1,1,null,1,1,null,null,1,1,1,null,1,null,1,null,null,1,null,1,null,1,null,1,1,null,1,null,1,1,1,null,1,null,1,1,null,1,null,1,1,null,null,null,null,1,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,1,null,null,null,null,null,1,null,1,null,1,null,1,1,null,1,1,null,1,null,1,1,null,1,null,1,null,1,null,null,null,1,null,1,null,1,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,1,1,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,null,1,1,null,1,null,null,1,null,null,1,null,null,1,null,1,1,null,null,1,1,null,1,1,null,1,null,1,null,null,1,1,null,1,null,null,null,null,1,null,1,null,null,1,null,1,1,1,1,null,null,1,null,null,1,null,null,1,null,1,null,1,1,1,1,null,1,1,null,1,1,null,null,1,null,null,1,null,null,1,1,null,1,null,1,null,1,null,1,null,1,1,null,1,1,null,1,null,null,1,null,null,1,null,1,null,1,1,null,null,1,null,1,null,null,1,null,1,null,1,1,null,null,1,null,null,1,1,1,null,1,null,1,null,1,1,1,1,null,1,null,1,null,null,1,null,null,1,null,1,1,null,null,null,null,null,null,1,null,null,1,1,1,null,1,null,null,1,null,null,1,null,null,1,1,null,1,null,null,null,1,1,null,1,1,1,null,null,null,1,null,null,null,1,1,null,1,1,1,1,1,1,null,1,null,1,null,1,null,1,null,1,1,null,1,1,1,null,1,null,1,null,1,null,null,1,null,null,1,null,1,null,null,1,null,1,null,1,null,1,1,null,1,null,1,null,null,1,null,null,1,null,1,1,null,1,1,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,1,1,null,null,null,1,null,1,null,1,null,1,1,null,1,null,null,1,1,1,null,null,null,1,null,1,1,1,1,1,null,null,1,null,null,1,null,1,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,1,null,null,1,null,1,1,null,1,null,1,null,1,null,1,1,1,null,1,null,1,null,1,null,null,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,null,1,1,1,null,null,null,1,null,1,null,null,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,null,1,1,1,null,null,1,null,1,null,1,null,1,null,null,1,1,1,null,1,1,1,null,null,1,null,null,1,null,null,1,1,1,1,null,null,null,1,null,1,null,1,null,null,1,1,null,1,null,null,1,null,1,null,1,null,1,1,1,null,null,1,null,null,1,1,null,1,null,1,1,1,1,null,1,null,1,null,null,null,1,null,null,null,1,1,null,1,1,1,1,1,null,null,null,1,null,null,null,null,null,null,null,1,1,null,1,null,null,null,1,null,1,null,1,null,null,null,1,null,null,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,null,null,null,null,null,null,1,1,1,null,1,1,1,null,null,1,null,null,1,null,null,1,null,1,null,1,1,1,null,1,1,null,1,null,null,1,null,null,1,1,null,null,null,1,1,1,1,1,null,null,1,null,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,1,1,null,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,1,null,1,null,null,1,null,1,1,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,1,null,1,1,null,1,null,1,1,1,1,1,null,null,1,null,null,1,null,1,null,null,1,null,1,1,null,1,null,1,null,1,null,1,null,null,null,1,null,null,null,1,null,1,null,1,null,1,null,1,null,null,1,1,1,null,null,null,1,null,1,null,1,null,1,null,null,1,null,1,null,null,null,1,null,1,null,1,null,1,1,null,null,1,1,null,1,null,null,1,1,null,1,null,1,null,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,null,1,null,1,null,null,1,null,1,null,null,null,1,null,1,1,null,1,1,null,null,1,1,null,1,1,1,null,1,null,1,null,null,1,null,null,1,null,null,1,1,null,null,1,1,1,null,1,null,1,null,1,null,1,null,1,1,1,null,1,null,null,1,null,1,null,null,1,null,1,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,1,null,1,1,1,1,null,1,1,null,1,null,1,null,1,1,null,1,1,null,1,1,null,1,null,1,null,1,null,1,null,1,1,1,null,1,1,null,1,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,null,1,null,1,null,1,null,1,1,null,1,null,1,1,1,null,1,null,1,null,1,null,1,1,null,null,1,null,null,1,null,1,1,1,null,1,null,null,1,null,1,null,1,1,null,1,null,1,null,null,1,null,null,1,null,1,1,null,null,1,1,1,1,null,null,null,null,null,null,null,null,null,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,1,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null],"linenum":[10,10,10,10,10,null,11,11,11,11,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,null,12,null,null,12,null,12,12,null,12,null,12,12,12,null,null,12,12,null,12,null,12,null,12,null,12,12,null,12,12,null,null,12,null,12,null,12,null,null,12,null,12,null,12,null,null,12,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,null,null,12,12,null,12,null,12,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,12,null,null,12,12,null,null,null,12,null,null,12,12,null,12,12,null,12,null,null,null,12,12,null,12,12,12,null,12,null,12,12,null,12,null,12,null,null,null,null,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,12,12,null,12,12,null,12,null,12,null,12,null,null,12,12,null,12,12,12,12,null,12,null,null,12,null,null,12,null,12,12,null,12,12,12,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,null,null,12,null,12,null,null,12,12,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,null,12,null,12,12,null,null,null,null,12,12,null,null,12,null,null,12,12,null,12,null,null,12,12,null,null,12,null,12,null,12,null,12,12,12,null,12,null,12,null,12,null,12,12,12,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,12,null,12,12,null,null,12,null,12,12,12,null,null,12,12,null,12,12,null,null,12,null,12,12,null,12,12,null,null,12,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,12,null,12,null,12,12,12,null,null,12,null,12,null,null,12,null,12,null,12,null,12,12,12,null,12,null,null,12,null,null,12,null,null,12,12,12,null,12,null,12,null,12,null,12,null,null,null,12,null,null,12,12,null,null,12,null,12,null,12,null,12,null,null,null,null,null,12,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,null,null,12,12,null,12,null,null,12,12,null,12,null,12,null,12,12,12,12,null,12,null,null,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,null,null,12,null,null,null,12,null,12,12,12,null,null,null,12,null,12,null,12,12,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,null,null,null,12,null,null,null,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,12,12,12,null,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,12,null,null,12,null,12,12,null,12,12,null,12,12,null,null,null,12,12,null,12,null,12,null,12,12,null,null,null,null,12,null,12,null,12,12,12,null,null,null,null,null,null,null,12,null,12,12,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,null,12,null,12,null,12,12,null,12,null,null,12,12,null,12,null,12,null,null,null,null,null,12,null,12,null,12,12,null,12,12,12,12,null,12,null,12,12,12,null,null,12,null,null,12,null,12,null,12,null,12,null,null,null,null,12,null,12,null,12,null,12,12,12,null,12,null,12,null,null,12,null,null,12,12,null,12,null,null,12,12,null,null,12,12,null,12,null,12,null,12,null,12,12,null,12,12,null,null,null,12,12,null,12,null,12,null,null,12,12,null,12,12,null,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,12,null,12,12,12,12,null,12,null,12,null,12,null,null,null,12,null,null,12,null,12,null,12,12,null,12,null,12,null,null,12,null,null,12,null,12,12,12,null,null,12,null,12,null,null,12,null,null,12,null,12,null,12,null,12,12,null,12,null,null,12,null,12,null,null,null,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,12,null,null,null,12,null,null,null,12,12,null,12,null,12,12,null,12,null,12,12,12,12,null,null,12,12,null,null,12,null,12,null,12,null,null,null,12,12,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,null,12,null,12,null,12,null,12,12,null,12,null,12,null,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,12,12,null,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,null,12,12,null,12,null,null,12,null,12,null,12,null,12,null,12,12,12,null,12,null,12,12,null,12,12,12,null,12,null,null,null,12,null,null,null,12,12,12,null,12,null,12,12,null,null,null,12,12,null,12,12,12,null,null,12,null,12,null,12,null,12,12,null,12,12,null,null,12,12,12,null,12,null,12,null,null,12,null,12,null,12,null,12,12,null,12,null,12,12,12,null,12,null,12,12,null,12,null,12,12,null,null,null,null,12,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,12,null,null,null,null,null,12,null,12,null,12,null,12,12,null,12,12,null,12,null,12,12,null,12,null,12,null,12,null,null,null,12,null,12,null,12,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,12,12,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,null,12,12,null,12,null,null,12,null,null,12,null,null,12,null,12,12,null,null,12,12,null,12,12,null,12,null,12,null,null,12,12,null,12,null,null,null,null,12,null,12,null,null,12,null,12,12,12,12,null,null,12,null,null,12,null,null,12,null,12,null,12,12,12,12,null,12,12,null,12,12,null,null,12,null,null,12,null,null,12,12,null,12,null,12,null,12,null,12,null,12,12,null,12,12,null,12,null,null,12,null,null,12,null,12,null,12,12,null,null,12,null,12,null,null,12,null,12,null,12,12,null,null,12,null,null,12,12,12,null,12,null,12,null,12,12,12,12,null,12,null,12,null,null,12,null,null,12,null,12,12,null,null,null,null,null,null,12,null,null,12,12,12,null,12,null,null,12,null,null,12,null,null,12,12,null,12,null,null,null,12,12,null,12,12,12,null,null,null,12,null,null,null,12,12,null,12,12,12,12,12,12,null,12,null,12,null,12,null,12,null,12,12,null,12,12,12,null,12,null,12,null,12,null,null,12,null,null,12,null,12,null,null,12,null,12,null,12,null,12,12,null,12,null,12,null,null,12,null,null,12,null,12,12,null,12,12,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,12,12,null,null,null,12,null,12,null,12,null,12,12,null,12,null,null,12,12,12,null,null,null,12,null,12,12,12,12,12,null,null,12,null,null,12,null,12,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,12,null,null,12,null,12,12,null,12,null,12,null,12,null,12,12,12,null,12,null,12,null,12,null,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,null,12,12,12,null,null,null,12,null,12,null,null,12,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,null,12,12,12,null,null,12,null,12,null,12,null,12,null,null,12,12,12,null,12,12,12,null,null,12,null,null,12,null,null,12,12,12,12,null,null,null,12,null,12,null,12,null,null,12,12,null,12,null,null,12,null,12,null,12,null,12,12,12,null,null,12,null,null,12,12,null,12,null,12,12,12,12,null,12,null,12,null,null,null,12,null,null,null,12,12,null,12,12,12,12,12,null,null,null,12,null,null,null,null,null,null,null,12,12,null,12,null,null,null,12,null,12,null,12,null,null,null,12,null,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,null,null,null,null,null,null,12,12,12,null,12,12,12,null,null,12,null,null,12,null,null,12,null,12,null,12,12,12,null,12,12,null,12,null,null,12,null,null,12,12,null,null,null,12,12,12,12,12,null,null,12,null,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,12,12,null,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,12,null,12,null,null,12,null,12,12,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,12,null,12,12,null,12,null,12,12,12,12,12,null,null,12,null,null,12,null,12,null,null,12,null,12,12,null,12,null,12,null,12,null,12,null,null,null,12,null,null,null,12,null,12,null,12,null,12,null,12,null,null,12,12,12,null,null,null,12,null,12,null,12,null,12,null,null,12,null,12,null,null,null,12,null,12,null,12,null,12,12,null,null,12,12,null,12,null,null,12,12,null,12,null,12,null,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,null,12,null,12,null,null,12,null,12,null,null,null,12,null,12,12,null,12,12,null,null,12,12,null,12,12,12,null,12,null,12,null,null,12,null,null,12,null,null,12,12,null,null,12,12,12,null,12,null,12,null,12,null,12,null,12,12,12,null,12,null,null,12,null,12,null,null,12,null,12,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,12,null,12,12,12,12,null,12,12,null,12,null,12,null,12,12,null,12,12,null,12,12,null,12,null,12,null,12,null,12,null,12,12,12,null,12,12,null,12,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,null,12,null,12,null,12,null,12,12,null,12,null,12,12,12,null,12,null,12,null,12,null,12,12,null,null,12,null,null,12,null,12,12,12,null,12,null,null,12,null,12,null,12,12,null,12,null,12,null,null,12,null,null,12,null,12,12,null,null,12,12,12,12,null,null,null,null,null,null,null,null,null,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,13,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,13,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null],"memalloc":[124.4677886962891,124.4677886962891,124.4677886962891,124.4677886962891,124.4678115844727,124.4678115844727,139.7500228881836,139.7500228881836,139.7500228881836,139.7500228881836,170.2157669067383,170.2157669067383,170.2157669067383,170.2157669067383,170.2157669067383,170.2157669067383,170.2158126831055,170.2158126831055,170.2158126831055,170.2158126831055,170.2158126831055,170.2158126831055,170.2158126831055,170.2158126831055,170.2158126831055,170.2158126831055,170.2158126831055,170.2158126831055,170.2158126831055,170.2158126831055,170.2158126831055,170.2158126831055,170.2155075073242,170.2155075073242,185.6654663085938,185.6654663085938,185.9167785644531,185.9167785644531,186.1910171508789,186.1910171508789,186.1910171508789,186.503044128418,186.503044128418,186.8825302124023,187.2334976196289,187.2334976196289,187.6183395385742,187.6183395385742,188.019157409668,188.4215316772461,188.7345199584961,188.7345199584961,188.7345199584961,185.7783660888672,186.1445846557617,186.1445846557617,186.5438079833984,186.5438079833984,186.9619522094727,186.9619522094727,187.3680038452148,187.3680038452148,187.7706146240234,188.1740112304688,188.1740112304688,188.5782623291016,188.8042907714844,188.8042907714844,188.8042907714844,185.9962158203125,185.9962158203125,186.3557662963867,186.3557662963867,186.7369232177734,186.7369232177734,186.7369232177734,187.1459350585938,187.1459350585938,187.5524063110352,187.5524063110352,187.9531555175781,187.9531555175781,187.9531555175781,188.3573150634766,188.7617416381836,188.7617416381836,188.8914108276367,188.8914108276367,188.8914108276367,186.2074661254883,186.2074661254883,186.5702133178711,186.5702133178711,186.9554977416992,186.9554977416992,187.3559951782227,187.3559951782227,187.7611236572266,187.7611236572266,188.1621322631836,188.1621322631836,188.564453125,188.564453125,188.9691543579102,186.0931701660156,186.0931701660156,186.4431838989258,186.4431838989258,186.8088760375977,187.1904296875,187.590461730957,187.590461730957,187.9891510009766,187.9891510009766,188.3754119873047,188.3754119873047,188.7807388305664,188.7807388305664,189.0614624023438,189.0614624023438,186.3185577392578,186.3185577392578,186.661735534668,186.661735534668,187.0273056030273,187.4063339233398,187.7991790771484,187.7991790771484,187.7991790771484,188.1911697387695,188.6367416381836,188.6367416381836,189.0410232543945,189.0410232543945,189.1443710327148,189.1443710327148,189.1443710327148,186.6026000976562,186.9559707641602,186.9559707641602,187.3223266601562,187.7107009887695,187.7107009887695,188.0937423706055,188.0937423706055,188.4716949462891,188.4716949462891,188.8604431152344,189.2259674072266,189.2259674072266,186.4764938354492,186.8022918701172,187.1240463256836,187.1240463256836,187.4809799194336,187.4809799194336,187.8302307128906,188.2018585205078,188.2018585205078,188.5892944335938,188.5892944335938,188.9765701293945,188.9765701293945,189.3062973022461,189.3062973022461,189.3062973022461,186.6375198364258,186.6375198364258,186.9646759033203,186.9646759033203,187.3194198608398,187.3194198608398,187.6791458129883,187.6791458129883,188.1015167236328,188.1015167236328,188.4926528930664,188.4926528930664,188.8820724487305,188.8820724487305,189.2823104858398,189.2823104858398,189.3853149414062,189.3853149414062,189.3853149414062,186.9396896362305,187.2874908447266,187.6426010131836,187.6426010131836,188.0179214477539,188.4080276489258,188.4080276489258,188.7958068847656,188.7958068847656,189.1962585449219,189.1962585449219,189.4629821777344,189.4629821777344,189.4629821777344,186.9195861816406,187.2499542236328,187.2499542236328,187.5996856689453,187.9565277099609,188.3308868408203,188.7198486328125,188.7198486328125,189.1124114990234,189.1124114990234,189.1124114990234,189.5188140869141,189.5188140869141,189.5188140869141,186.9136810302734,186.9136810302734,187.23583984375,187.5796356201172,187.5796356201172,187.9328994750977,188.3053665161133,188.6921157836914,189.0804595947266,189.0804595947266,189.4790115356445,189.4790115356445,189.6146621704102,189.6146621704102,187.2369766235352,187.5652236938477,187.5652236938477,187.9089889526367,187.9089889526367,188.2662658691406,188.2662658691406,188.6438903808594,188.6438903808594,189.0327682495117,189.0327682495117,189.425666809082,189.425666809082,189.6887283325195,189.6887283325195,187.2528457641602,187.2528457641602,187.2528457641602,187.5702514648438,187.9409255981445,188.2912368774414,188.6617813110352,188.6617813110352,189.0501022338867,189.0501022338867,189.4408264160156,189.4408264160156,189.7615966796875,189.7615966796875,187.3393020629883,187.3393020629883,187.6562194824219,187.6562194824219,187.9942169189453,187.9942169189453,188.3463668823242,188.3463668823242,188.7219009399414,188.7219009399414,189.1135940551758,189.5162811279297,189.5162811279297,189.8331756591797,189.8331756591797,189.8331756591797,187.4482421875,187.7588577270508,187.7588577270508,187.7588577270508,188.0882415771484,188.0882415771484,188.0882415771484,188.4331893920898,188.8066177368164,188.8066177368164,189.1965484619141,189.1965484619141,189.1965484619141,189.5959625244141,189.9037017822266,189.9037017822266,189.9037017822266,187.5530166625977,187.5530166625977,187.8527069091797,187.8527069091797,188.1762619018555,188.1762619018555,188.5203475952148,188.8911972045898,189.2775268554688,189.2775268554688,189.6802597045898,189.6802597045898,189.973030090332,189.973030090332,187.6829452514648,187.6829452514648,187.9836654663086,188.3031463623047,188.6435699462891,189.0071029663086,189.0071029663086,189.3920822143555,189.3920822143555,189.7844467163086,189.7844467163086,190.0412979125977,190.0412979125977,187.8261947631836,187.8261947631836,188.1236038208008,188.1236038208008,188.442268371582,188.7844619750977,188.7844619750977,189.1482772827148,189.5272979736328,189.5272979736328,189.9198455810547,190.1084289550781,190.1084289550781,190.1084289550781,187.9439010620117,187.9439010620117,188.2329177856445,188.5488815307617,188.8886260986328,188.8886260986328,188.8886260986328,189.2491607666016,189.6201782226562,189.6201782226562,190.0174407958984,190.1745071411133,190.1745071411133,190.1745071411133,188.0714263916016,188.0714263916016,188.3626098632812,188.6788177490234,188.6788177490234,189.0235595703125,189.3826293945312,189.3826293945312,189.7568740844727,190.1508865356445,190.2394561767578,190.2394561767578,190.2394561767578,190.2394561767578,190.2394561767578,190.2394561767578,190.2394561767578,190.2394561767578,190.2394561767578,190.2394561767578,190.2394561767578,190.2394561767578,190.2394561767578,190.2394561767578,190.2394561767578,190.2394561767578,190.2394561767578,190.2394561767578,190.2394561767578,190.2394561767578,190.2394561767578,190.2394561767578,190.2394561767578,190.2394561767578,188.0026702880859,188.0026702880859,188.0026702880859,188.1426773071289,188.3660659790039,188.3660659790039,188.6045532226562,188.6045532226562,188.8437728881836,189.1409606933594,189.467041015625,189.467041015625,189.8016967773438,190.1620712280273,190.1620712280273,190.3031539916992,190.3031539916992,190.3031539916992,188.2675323486328,188.2675323486328,188.5515060424805,188.5515060424805,188.8735198974609,188.8735198974609,189.2203674316406,189.5920944213867,189.9793395996094,189.9793395996094,190.3660507202148,190.3660507202148,190.3660507202148,190.3660507202148,190.3660507202148,190.3660507202148,188.474494934082,188.474494934082,188.474494934082,188.7723159790039,189.1052551269531,189.4522399902344,189.4522399902344,189.8265075683594,189.8265075683594,190.2199249267578,190.2199249267578,190.4279327392578,190.4279327392578,188.4191284179688,188.4191284179688,188.6970443725586,188.6970443725586,189.0104675292969,189.0104675292969,189.0104675292969,189.3519744873047,189.7102508544922,189.7102508544922,189.7102508544922,190.0903244018555,190.0903244018555,190.4848022460938,190.4848022460938,190.488883972168,190.488883972168,188.6435012817383,188.6435012817383,188.93359375,188.93359375,189.2587127685547,189.2587127685547,189.6074600219727,190.0041198730469,190.0041198730469,190.3791732788086,190.3791732788086,190.5488204956055,190.5488204956055,190.5488204956055,188.6038818359375,188.6038818359375,188.8682556152344,188.8682556152344,189.1704711914062,189.1704711914062,189.5056228637695,189.5056228637695,189.8571014404297,189.8571014404297,190.2320938110352,190.2320938110352,190.6077651977539,190.6077651977539,190.6077651977539,190.6077651977539,190.6077651977539,190.6077651977539,188.8256530761719,188.8256530761719,189.1130523681641,189.1130523681641,189.4379730224609,189.7858276367188,189.7858276367188,190.1511840820312,190.1511840820312,190.1511840820312,190.5408020019531,190.6657257080078,190.6657257080078,188.8301239013672,188.8301239013672,189.1090087890625,189.1090087890625,189.4265518188477,189.7738952636719,190.137580871582,190.5229263305664,190.5229263305664,190.7228240966797,190.7228240966797,190.7228240966797,188.8680267333984,189.1411209106445,189.1411209106445,189.4531860351562,189.4531860351562,189.7968902587891,189.7968902587891,190.1571655273438,190.1571655273438,190.1571655273438,190.5323104858398,190.5323104858398,190.7789840698242,190.7789840698242,188.9148254394531,188.9148254394531,188.9148254394531,189.1816864013672,189.1816864013672,189.5140838623047,189.5140838623047,189.8530807495117,189.8530807495117,190.2050933837891,190.2050933837891,190.5793533325195,190.5793533325195,190.8341751098633,190.8341751098633,190.8341751098633,188.9916381835938,189.2508087158203,189.2508087158203,189.5494766235352,189.8854446411133,190.2385482788086,190.2385482788086,190.6105117797852,190.6105117797852,190.8885879516602,190.8885879516602,189.0650024414062,189.0650024414062,189.3255233764648,189.617057800293,189.9463577270508,189.9463577270508,190.2964477539062,190.2964477539062,190.6686172485352,190.6686172485352,190.9420318603516,190.9420318603516,190.9420318603516,189.1531677246094,189.1531677246094,189.410774230957,189.410774230957,189.7043380737305,189.7043380737305,190.0373764038086,190.0373764038086,190.3938446044922,190.7693099975586,190.7693099975586,190.7693099975586,190.9946594238281,190.9946594238281,190.9946594238281,189.2591857910156,189.2591857910156,189.2591857910156,189.522216796875,189.522216796875,189.522216796875,189.8236618041992,189.8236618041992,190.1941604614258,190.1941604614258,190.5466461181641,190.5466461181641,190.9198837280273,190.9198837280273,190.9198837280273,191.0464019775391,191.0464019775391,191.0464019775391,189.3918380737305,189.3918380737305,189.6518707275391,189.6518707275391,189.9581069946289,189.9581069946289,190.2969055175781,190.2969055175781,190.6538238525391,190.6538238525391,191.0323715209961,191.0323715209961,191.0973052978516,191.0973052978516,191.0973052978516,189.5159454345703,189.7931976318359,190.1125564575195,190.4552230834961,190.4552230834961,190.4552230834961,190.8149185180664,190.8149185180664,191.1474456787109,191.1474456787109,191.1474456787109,191.1474456787109,189.671272277832,189.671272277832,189.9561004638672,190.2783966064453,190.2783966064453,190.6249542236328,190.6249542236328,190.9871215820312,191.196662902832,191.196662902832,191.196662902832,189.5735778808594,189.5735778808594,189.8619613647461,190.1683044433594,190.1683044433594,190.5070571899414,190.8596649169922,190.8596649169922,191.2394409179688,191.2451858520508,191.2451858520508,191.2451858520508,191.2451858520508,189.7864227294922,190.0665893554688,190.0665893554688,190.3919372558594,190.3919372558594,190.7421722412109,190.7421722412109,191.108039855957,191.2928695678711,191.2928695678711,191.2928695678711,189.743782043457,189.743782043457,190.0071716308594,190.0071716308594,190.3132247924805,190.3132247924805,190.6539764404297,191.013069152832,191.3397827148438,191.3397827148438,191.3397827148438,191.3397827148438,191.3397827148438,191.3397827148438,189.9774703979492,189.9774703979492,190.2649154663086,190.2649154663086,190.593391418457,190.9431838989258,191.3110046386719,191.3859710693359,191.3859710693359,191.3859710693359,191.3859710693359,191.3859710693359,191.3859710693359,191.3859710693359,191.3859710693359,191.3859710693359,191.3859710693359,191.3859710693359,191.3859710693359,191.3859710693359,191.3859710693359,191.3859710693359,191.3859710693359,191.3859710693359,191.3859710693359,191.3859710693359,191.3859710693359,191.3859710693359,191.3859710693359,191.3859710693359,191.3859710693359,191.3859710693359,191.3859710693359,191.3859710693359,191.3859710693359,191.3859710693359,191.3859710693359,191.3859710693359,191.3859710693359,191.3859710693359,191.3859710693359,191.3859710693359,191.3859710693359,191.3859710693359,191.3859710693359,191.3859710693359,191.3859710693359,191.3859710693359,191.3859710693359,191.3859710693359,191.3859710693359,191.3859710693359,191.3859710693359,189.7960205078125,189.7960205078125,189.7960205078125,189.7960205078125,189.9733123779297,189.9733123779297,190.2251739501953,190.2251739501953,190.5072860717773,190.5072860717773,190.8228530883789,191.1428909301758,191.1428909301758,191.4759674072266,191.8530654907227,191.8530654907227,192.1997375488281,192.1997375488281,192.5713958740234,192.9042739868164,192.9042739868164,193.237174987793,193.237174987793,193.237174987793,193.572135925293,193.9032592773438,193.9032592773438,194.2378921508789,194.2378921508789,194.5736083984375,194.5736083984375,194.6364135742188,194.6364135742188,194.6364135742188,190.1979064941406,190.5263748168945,190.5263748168945,190.8830871582031,190.8830871582031,191.2219848632812,191.5733947753906,191.5733947753906,191.9810256958008,192.3937454223633,192.8012008666992,193.2070770263672,193.2070770263672,193.6166763305664,193.6166763305664,194.0266189575195,194.4331970214844,194.7688369750977,194.7688369750977,194.7688369750977,194.7688369750977,194.7688369750977,194.7688369750977,190.4316635131836,190.4316635131836,190.7489471435547,190.7489471435547,191.0932159423828,191.0932159423828,191.4162826538086,191.4162826538086,191.7802047729492,191.7802047729492,191.7802047729492,192.1829452514648,192.1829452514648,192.5977249145508,192.5977249145508,193.0059204101562,193.0059204101562,193.4188461303711,193.82763671875,194.229850769043,194.229850769043,194.6313705444336,194.6313705444336,194.8991088867188,194.8991088867188,194.8991088867188,194.8991088867188,194.8991088867188,194.8991088867188,190.6793899536133,190.9990539550781,190.9990539550781,191.3316192626953,191.3316192626953,191.6577758789062,192.0316696166992,192.43603515625,192.43603515625,192.43603515625,192.851432800293,193.2549743652344,193.2549743652344,193.6627883911133,193.6627883911133,194.0718154907227,194.0718154907227,194.4820861816406,194.4820861816406,194.8828506469727,195.0272674560547,195.0272674560547,190.7190170288086,191.0151824951172,191.0151824951172,191.3385543823242,191.3385543823242,191.6544799804688,192.0208511352539,192.0208511352539,192.4073791503906,192.4073791503906,192.8194198608398,192.8194198608398,192.8194198608398,193.2313079833984,193.6402969360352,193.6402969360352,194.0490264892578,194.4580154418945,194.4580154418945,194.8663940429688,195.1533050537109,195.1533050537109,195.1533050537109,195.1533050537109,191.0582580566406,191.0582580566406,191.3675842285156,191.3675842285156,191.6781997680664,191.6781997680664,192.0219192504883,192.391471862793,192.391471862793,192.7878723144531,192.7878723144531,193.2003021240234,193.2003021240234,193.6110305786133,194.0221710205078,194.0221710205078,194.4321594238281,194.8431167602539,195.2440795898438,195.2774200439453,195.2774200439453,191.1522750854492,191.1522750854492,191.4484786987305,191.4484786987305,191.7546768188477,191.7546768188477,192.0862808227539,192.0862808227539,192.4511337280273,192.4511337280273,192.8396682739258,193.2472305297852,193.2472305297852,193.6547012329102,193.6547012329102,194.0630187988281,194.5101928710938,194.5101928710938,194.9183120727539,194.9183120727539,195.3164749145508,195.3164749145508,195.3164749145508,195.3994674682617,195.3994674682617,195.3994674682617,191.2990188598633,191.2990188598633,191.5858001708984,191.8810272216797,192.2081680297852,192.2081680297852,192.2081680297852,192.5667037963867,192.5667037963867,192.9372863769531,192.9372863769531,192.9372863769531,193.3228073120117,193.3228073120117,193.3228073120117,193.7212982177734,193.7212982177734,194.1241683959961,194.1241683959961,194.5244750976562,194.5244750976562,194.9339065551758,195.3371276855469,195.3371276855469,195.5195693969727,195.5195693969727,195.5195693969727,191.4069442749023,191.4069442749023,191.6794052124023,191.6794052124023,191.9652786254883,191.9652786254883,191.9652786254883,192.2769012451172,192.2769012451172,192.6305313110352,192.6305313110352,193.0010757446289,193.0010757446289,193.4001312255859,193.4001312255859,193.4001312255859,193.8082809448242,193.8082809448242,194.2192459106445,194.2192459106445,194.629035949707,195.0392608642578,195.0392608642578,195.4458770751953,195.4458770751953,195.6376419067383,195.6376419067383,195.6376419067383,195.6376419067383,191.5886154174805,191.8614654541016,191.8614654541016,192.1424102783203,192.1424102783203,192.4570465087891,192.8444519042969,192.8444519042969,193.2131042480469,193.2131042480469,193.5988693237305,193.9934463500977,194.3792114257812,194.7725830078125,194.7725830078125,194.7725830078125,195.1746444702148,195.5759124755859,195.5759124755859,195.5759124755859,195.7538909912109,195.7538909912109,191.7652282714844,191.7652282714844,192.0314483642578,192.0314483642578,192.304801940918,192.304801940918,192.6247634887695,192.9747695922852,193.3401794433594,193.7263336181641,193.7263336181641,194.1304550170898,194.1304550170898,194.5409317016602,194.5409317016602,194.9538269042969,194.9538269042969,195.3667068481445,195.3667068481445,195.7706451416016,195.7706451416016,195.8682556152344,195.8682556152344,195.8682556152344,192.0014343261719,192.0014343261719,192.2653121948242,192.2653121948242,192.5431442260742,192.8708801269531,192.8708801269531,193.2242736816406,193.2242736816406,193.5902099609375,193.5902099609375,193.9841537475586,194.3833465576172,194.3833465576172,194.7905731201172,194.7905731201172,195.197021484375,195.197021484375,195.6058578491211,195.6058578491211,195.9807815551758,195.9807815551758,195.9807815551758,195.9807815551758,192.2682342529297,192.2682342529297,192.529182434082,192.529182434082,192.7987442016602,192.7987442016602,193.1015701293945,193.1015701293945,193.4383087158203,193.7896118164062,193.7896118164062,194.167236328125,194.5611801147461,194.9597091674805,194.9597091674805,194.9597091674805,195.3619537353516,195.7670669555664,195.7670669555664,196.0915069580078,196.0915069580078,196.0915069580078,196.0915069580078,192.4511260986328,192.4511260986328,192.7074737548828,192.7074737548828,193.0098037719727,193.0098037719727,193.3423309326172,193.3423309326172,193.6845321655273,193.6845321655273,194.0460586547852,194.4317169189453,194.4317169189453,194.4317169189453,194.8325424194336,195.2403030395508,195.2403030395508,195.6482849121094,195.6482849121094,195.6482849121094,196.0494689941406,196.0494689941406,196.2003860473633,196.2003860473633,192.4785537719727,192.4785537719727,192.7320861816406,192.7320861816406,193.0360870361328,193.3477172851562,193.6833267211914,193.6833267211914,194.0387191772461,194.0387191772461,194.4240112304688,194.8249969482422,194.8249969482422,195.2309265136719,195.6390075683594,196.0419006347656,196.0419006347656,196.3076019287109,196.3076019287109,196.3076019287109,196.3076019287109,196.3076019287109,196.3076019287109,196.3076019287109,196.3076019287109,192.8182601928711,193.0749816894531,193.3724136352539,193.3724136352539,193.6976928710938,193.6976928710938,194.0458221435547,194.4110107421875,194.4110107421875,194.7924957275391,194.7924957275391,195.1864929199219,195.5951614379883,195.5951614379883,196.0005416870117,196.3936920166016,196.4130096435547,196.4130096435547,196.4130096435547,192.8610534667969,192.8610534667969,193.1088027954102,193.1088027954102,193.3974609375,193.3974609375,193.7113418579102,194.0495986938477,194.0495986938477,194.4064483642578,194.7883148193359,194.7883148193359,194.7883148193359,195.1849899291992,195.5884094238281,195.9948577880859,195.9948577880859,196.3970489501953,196.3970489501953,196.5167388916016,196.5167388916016,196.5167388916016,193.0034942626953,193.0034942626953,193.2435455322266,193.2435455322266,193.5168228149414,193.5168228149414,193.815315246582,194.1425094604492,194.1425094604492,194.4892501831055,194.4892501831055,194.8542404174805,195.2410583496094,195.6356506347656,195.6356506347656,196.0426025390625,196.0426025390625,196.4408493041992,196.6187210083008,196.6187210083008,196.6187210083008,196.6187210083008,193.3369293212891,193.599479675293,193.599479675293,193.8900527954102,193.8900527954102,193.8900527954102,194.2080612182617,194.5598220825195,194.5598220825195,194.9302520751953,194.9302520751953,195.3262023925781,195.7286682128906,195.7286682128906,196.1372451782227,196.1372451782227,196.5395431518555,196.5395431518555,196.7191467285156,196.7191467285156,196.7191467285156,196.7191467285156,193.434455871582,193.6805191040039,193.6805191040039,193.9560165405273,193.9560165405273,194.2578353881836,194.2578353881836,194.5931396484375,194.5931396484375,194.9540939331055,194.9540939331055,195.3496170043945,195.3496170043945,195.8024063110352,196.2163467407227,196.2163467407227,196.6239852905273,196.8179550170898,196.8179550170898,196.8179550170898,196.8179550170898,193.6217727661133,193.875862121582,193.875862121582,194.1545867919922,194.1545867919922,194.4604110717773,194.4604110717773,194.7999572753906,194.7999572753906,195.1642761230469,195.1642761230469,195.5621871948242,195.5621871948242,195.9726409912109,195.9726409912109,196.3854141235352,196.7877349853516,196.7877349853516,196.7877349853516,196.9151229858398,196.9151229858398,196.9151229858398,196.9151229858398,196.9151229858398,196.9151229858398,196.9151229858398,196.9151229858398,196.9151229858398,196.9151229858398,196.9151229858398,196.9151229858398,196.9151229858398,196.9151229858398,196.9151229858398,196.9151229858398,196.9151229858398,196.9151229858398,196.9151229858398,196.9151229858398,196.9151229858398,196.9151229858398,196.9151229858398,196.9151229858398,196.9151229858398,196.9151229858398,196.9151229858398,196.9151229858398,196.9151229858398,196.9151229858398,196.9151229858398,196.9151229858398,196.9151229858398,196.9151229858398,196.9151229858398,196.9151229858398,193.5700759887695,193.5700759887695,193.5700759887695,193.6376724243164,193.6376724243164,193.8352737426758,194.0601654052734,194.2965316772461,194.5634307861328,194.5634307861328,194.8663024902344,194.8663024902344,195.1867904663086,195.5220947265625,195.5220947265625,195.8923263549805,195.8923263549805,196.2902984619141,196.2902984619141,196.6867141723633,196.6867141723633,197.0104446411133,197.0104446411133,197.0104446411133,197.0104446411133,193.8124160766602,193.8124160766602,194.0537109375,194.0537109375,194.3278121948242,194.3278121948242,194.6347198486328,194.6347198486328,194.9679260253906,194.9679260253906,195.291748046875,195.6544189453125,195.6544189453125,195.6544189453125,196.0352401733398,196.4395065307617,196.4395065307617,196.8869552612305,196.8869552612305,196.8869552612305,197.1045379638672,197.1045379638672,197.1045379638672,197.1045379638672,197.1045379638672,197.1045379638672,194.0539245605469,194.0539245605469,194.3027038574219,194.5759429931641,194.5759429931641,194.5759429931641,194.8855895996094,195.2238159179688,195.2238159179688,195.5767288208008,195.9522247314453,195.9522247314453,196.3521041870117,196.3521041870117,196.7622146606445,196.7622146606445,196.7622146606445,197.1709289550781,197.1971817016602,197.1971817016602,194.0817947387695,194.0817947387695,194.3183135986328,194.3183135986328,194.3183135986328,194.5788803100586,194.5788803100586,194.8705444335938,194.8705444335938,195.1946792602539,195.5431060791016,195.5431060791016,195.9040603637695,196.2921600341797,196.6904373168945,196.9448318481445,196.9448318481445,196.9448318481445,197.2882385253906,197.2882385253906,197.2882385253906,197.2882385253906,197.2882385253906,197.2882385253906,194.2546081542969,194.2546081542969,194.4912185668945,194.4912185668945,194.7523345947266,195.079948425293,195.3988418579102,195.6986465454102,195.6986465454102,196.0266342163086,196.3764801025391,196.3764801025391,196.7420501708984,197.1357727050781,197.1357727050781,197.1357727050781,197.3779220581055,197.3779220581055,197.3779220581055,197.3779220581055,197.3779220581055,197.3779220581055,194.3985366821289,194.6289367675781,194.6289367675781,194.8677749633789,194.8677749633789,195.1611709594727,195.1611709594727,195.4868392944336,195.4868392944336,195.8357315063477,195.8357315063477,196.183723449707,196.5304336547852,196.5304336547852,196.9090728759766,197.3085174560547,197.3085174560547,197.4660491943359,197.4660491943359,197.4660491943359,197.4660491943359,197.4660491943359,197.4660491943359,194.6389846801758,194.6389846801758,194.8850021362305,194.8850021362305,195.1577606201172,195.4640960693359,195.4640960693359,195.4640960693359,195.8022155761719,195.8022155761719,196.1528472900391,196.1528472900391,196.1528472900391,196.5532989501953,196.5532989501953,196.9391708374023,196.9391708374023,197.3408584594727,197.5527877807617,197.5527877807617,197.5527877807617,197.5527877807617,197.5527877807617,197.5527877807617,194.7405700683594,194.9734268188477,195.2365875244141,195.2365875244141,195.5273513793945,195.5273513793945,195.8519821166992,195.8519821166992,196.1973724365234,196.5318298339844,196.8671646118164,197.2313995361328,197.2313995361328,197.626220703125,197.626220703125,197.6381530761719,197.6381530761719,197.6381530761719,197.6381530761719,197.6381530761719,197.6381530761719,194.9012603759766,194.9012603759766,195.1305084228516,195.3857803344727,195.3857803344727,195.6753234863281,195.6753234863281,196.0004806518555,196.0004806518555,196.0004806518555,196.3433456420898,196.3433456420898,196.3433456420898,196.6963806152344,197.0737991333008,197.4659042358398,197.4659042358398,197.7220611572266,197.7220611572266,197.7220611572266,197.7220611572266,197.7220611572266,197.7220611572266,194.9942398071289,194.9942398071289,194.9942398071289,195.2266159057617,195.4843368530273,195.4843368530273,195.7710876464844,195.7710876464844,196.0911254882812,196.0911254882812,196.4295043945312,196.7802810668945,196.7802810668945,197.1520462036133,197.5449371337891,197.8046722412109,197.8046722412109,197.8046722412109,197.8046722412109,197.8046722412109,197.8046722412109,197.8046722412109,197.8046722412109,195.1014404296875,195.3335418701172,195.3335418701172,195.5959854125977,195.8880996704102,196.2168731689453,196.5643844604492,196.9162750244141,197.2962875366211,197.2962875366211,197.6987686157227,197.6987686157227,197.8859176635742,197.8859176635742,197.8859176635742,197.8859176635742,195.2679595947266,195.2679595947266,195.5015563964844,195.7638168334961,195.7638168334961,196.0609741210938,196.391845703125,196.7400588989258,196.7400588989258,197.0956802368164,197.0956802368164,197.5114059448242,197.5114059448242,197.9064178466797,197.9064178466797,197.9064178466797,197.9658889770508,197.9658889770508,197.9658889770508,195.2298202514648,195.2298202514648,195.4540481567383,195.4540481567383,195.6920394897461,195.9609680175781,195.9609680175781,196.2647399902344,196.2647399902344,196.6000900268555,196.6000900268555,196.9504776000977,197.3026580810547,197.3026580810547,197.6718597412109,197.6718597412109,198.0445709228516,198.0445709228516,198.0445709228516,198.0445709228516,198.0445709228516,198.0445709228516,195.3932495117188,195.3932495117188,195.6156387329102,195.853385925293,195.853385925293,196.1233520507812,196.4273910522461,196.7621688842773,196.7621688842773,197.1119232177734,197.1119232177734,197.469123840332,197.469123840332,197.8504867553711,197.8504867553711,198.1219177246094,198.1219177246094,198.1219177246094,198.1219177246094,198.1219177246094,198.1219177246094,195.5823440551758,195.8111419677734,196.0858993530273,196.0858993530273,196.3703308105469,196.3703308105469,196.691650390625,196.691650390625,197.0358963012695,197.0358963012695,197.3909530639648,197.3909530639648,197.7623672485352,198.1642761230469,198.1642761230469,198.1980972290039,198.1980972290039,198.1980972290039,195.6129379272461,195.8374862670898,196.0773086547852,196.0773086547852,196.3496322631836,196.3496322631836,196.6584854125977,196.6584854125977,196.9951019287109,197.3455276489258,197.708869934082,198.1049194335938,198.2730407714844,198.2730407714844,198.2730407714844,198.2730407714844,198.2730407714844,198.2730407714844,195.8794021606445,195.8794021606445,196.1137466430664,196.3779373168945,196.3779373168945,196.6794357299805,196.6794357299805,197.0126190185547,197.0126190185547,197.362060546875,197.362060546875,197.7266540527344,197.7266540527344,197.7266540527344,198.1207504272461,198.1207504272461,198.3467102050781,198.3467102050781,198.3467102050781,198.3467102050781,195.9532012939453,196.2029571533203,196.2029571533203,196.4622573852539,196.4622573852539,196.7561798095703,196.7561798095703,197.0857238769531,197.3888397216797,197.7149810791016,197.7149810791016,198.0657577514648,198.0657577514648,198.3524856567383,198.3524856567383,198.4192352294922,198.4192352294922,198.4192352294922,198.4192352294922,196.0581359863281,196.0581359863281,196.2639770507812,196.2639770507812,196.5020523071289,196.7617568969727,196.7617568969727,197.0239410400391,197.0239410400391,197.3372116088867,197.6708984375,197.9890518188477,197.9890518188477,198.3339157104492,198.3339157104492,198.4906158447266,198.4906158447266,198.4906158447266,198.4906158447266,196.151252746582,196.151252746582,196.3727035522461,196.3727035522461,196.6099624633789,196.6099624633789,196.8244476318359,197.1066207885742,197.4217224121094,197.4217224121094,197.4217224121094,197.6780853271484,197.6780853271484,197.9862976074219,198.3226089477539,198.3226089477539,198.5608444213867,198.5608444213867,198.5608444213867,198.5608444213867,198.5608444213867,198.5608444213867,196.322868347168,196.541862487793,196.7800903320312,196.7800903320312,197.0523147583008,197.0523147583008,197.3598785400391,197.3598785400391,197.6989288330078,197.6989288330078,198.0895156860352,198.0895156860352,198.4694213867188,198.4694213867188,198.4694213867188,198.6298522949219,198.6298522949219,198.6298522949219,198.6298522949219,198.6298522949219,198.6298522949219,198.6298522949219,198.6298522949219,198.6298522949219,198.6298522949219,198.6298522949219,198.6298522949219,198.6298522949219,198.6298522949219,198.6298522949219,198.6298522949219,198.6298522949219,198.6298522949219,198.6298522949219,198.6298522949219,196.2689437866211,196.4285202026367,196.4285202026367,196.5674285888672,196.5674285888672,196.7759323120117,196.7759323120117,197.0175933837891,197.0175933837891,197.2912673950195,197.2912673950195,197.5973205566406,197.5973205566406,197.9313049316406,198.2798538208008,198.6488265991211,198.6975631713867,198.6975631713867,198.6975631713867,196.3927536010742,196.6152954101562,196.6152954101562,196.8520126342773,196.8520126342773,196.8520126342773,197.1229858398438,197.4283676147461,197.7355117797852,197.7355117797852,198.086311340332,198.086311340332,198.4502487182617,198.4502487182617,198.7644424438477,198.7644424438477,198.7644424438477,198.7644424438477,196.5336456298828,196.5336456298828,196.7586288452148,196.7586288452148,196.7586288452148,197.0013580322266,197.0013580322266,197.2815628051758,197.2815628051758,197.5991592407227,197.5991592407227,197.5991592407227,197.9464721679688,198.3053817749023,198.6864166259766,198.6864166259766,198.6864166259766,198.8302764892578,198.8302764892578,198.8302764892578,198.8302764892578,196.7458190917969,196.7458190917969,196.963020324707,196.963020324707,196.963020324707,197.2208404541016,197.5170440673828,197.8486862182617,197.8486862182617,198.1978912353516,198.5988540649414,198.8950042724609,198.8950042724609,198.8950042724609,198.8950042724609,198.8950042724609,198.8950042724609,196.7595443725586,196.7595443725586,196.7595443725586,196.9869995117188,197.2338943481445,197.5195693969727,197.8422393798828,197.8422393798828,198.1919403076172,198.1919403076172,198.5505981445312,198.5505981445312,198.9424362182617,198.9424362182617,198.9587707519531,198.9587707519531,198.9587707519531,196.7855834960938,196.9996566772461,196.9996566772461,197.237922668457,197.237922668457,197.237922668457,197.5068969726562,197.5068969726562,197.8109970092773,197.8109970092773,198.1461563110352,198.1461563110352,198.4964752197266,198.8353271484375,199.0214462280273,199.0214462280273,199.0214462280273,199.0214462280273,199.0214462280273,199.0214462280273,196.9632720947266,197.1779022216797,197.1779022216797,197.4177551269531,197.4177551269531,197.6795654296875,197.9677734375,198.2952041625977,198.6408233642578,198.6408233642578,198.9793167114258,198.9793167114258,199.0830612182617,199.0830612182617,199.0830612182617,199.0830612182617,199.0830612182617,199.0830612182617,199.0830612182617,199.0830612182617,197.1115951538086,197.3195343017578,197.3195343017578,197.556884765625,197.809814453125,198.088996887207,198.4131011962891,198.7585830688477,198.7585830688477,199.0544128417969,199.0544128417969,199.1437530517578,199.1437530517578,199.1437530517578,199.1437530517578,199.1437530517578,199.1437530517578,197.2121047973633,197.2121047973633,197.4376525878906,197.7023849487305,197.7023849487305,197.9765167236328,197.9765167236328,198.2596817016602,198.2596817016602,198.6131591796875,198.6131591796875,198.9465103149414,198.9465103149414,199.2034301757812,199.2034301757812,199.2034301757812,199.2034301757812,199.2034301757812,199.2034301757812,199.2034301757812,199.2034301757812,197.204833984375,197.204833984375,197.4220962524414,197.6595153808594,197.6595153808594,197.9374389648438,197.9374389648438,198.2424011230469,198.2424011230469,198.577766418457,198.577766418457,198.9311752319336,198.9311752319336,199.2621154785156,199.2621154785156,199.2621154785156,199.2621154785156,199.2621154785156,199.2621154785156,197.2847671508789,197.2847671508789,197.5285568237305,197.7501831054688,198.0203628540039,198.0203628540039,198.330940246582,198.6384429931641,198.9840927124023,198.9840927124023,198.9840927124023,199.3199234008789,199.3199234008789,199.3199234008789,199.3199234008789,199.3199234008789,199.3199234008789,197.3640441894531,197.3640441894531,197.5814056396484,197.5814056396484,197.8214416503906,198.0911026000977,198.399284362793,198.399284362793,198.7396011352539,199.0891036987305,199.0891036987305,199.3767013549805,199.3767013549805,199.3767013549805,199.3767013549805,199.3767013549805,199.3767013549805,197.481071472168,197.7054672241211,197.7054672241211,197.9431991577148,197.9431991577148,198.2184143066406,198.5263977050781,198.867431640625,199.2430191040039,199.4326553344727,199.4326553344727,199.4326553344727,199.4326553344727,199.4326553344727,199.4326553344727,197.5526123046875,197.5526123046875,197.7684173583984,197.7684173583984,197.7684173583984,198.0053405761719,198.0053405761719,198.2811279296875,198.2811279296875,198.5893020629883,198.5893020629883,198.9247894287109,198.9247894287109,199.2809906005859,199.2809906005859,199.4876556396484,199.4876556396484,199.4876556396484,199.4876556396484,197.6864929199219,197.6864929199219,197.9042663574219,197.9042663574219,198.1344223022461,198.1344223022461,198.3764038085938,198.684211730957,198.684211730957,199.0219802856445,199.0219802856445,199.3741989135742,199.3741989135742,199.5417633056641,199.5417633056641,199.5417633056641,199.5417633056641,199.5417633056641,199.5417633056641,199.5417633056641,199.5417633056641,199.5417633056641,199.5417633056641,199.5417633056641,199.5417633056641,199.5417633056641,199.5417633056641,199.5417633056641,199.5417633056641,199.5417633056641,199.5417633056641,197.6787109375,197.6787109375,197.6787109375,197.7879104614258,197.9980545043945,198.228141784668,198.228141784668,198.228141784668,198.4814910888672,198.4814910888672,198.7696228027344,198.7696228027344,199.0904159545898,199.0904159545898,199.4266052246094,199.4266052246094,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,199.5948944091797,197.7620086669922,197.7620086669922,197.7620086669922,197.7620086669922,197.7620086669922,197.7620086669922,197.8041305541992,197.8041305541992,198.0389938354492,198.2905502319336,198.2905502319336,198.5688629150391,198.5688629150391,198.5688629150391,198.8810119628906,198.8810119628906,199.2019577026367,199.5109710693359,199.8587646484375,199.8587646484375,200.2395477294922,200.2395477294922,200.6426620483398,200.6426620483398,201.0169067382812,201.3519058227539,201.3519058227539,201.6850128173828,201.6850128173828,202.0173416137695,202.0173416137695,202.3496627807617,202.3496627807617,202.6811904907227,203.0156402587891,203.0156402587891,203.3508682250977,203.684211730957,203.684211730957,204.0188369750977,204.0188369750977,204.3535842895508,204.6870574951172,205.020637512207,205.355094909668,205.4106597900391,205.4106597900391,205.4106597900391,205.4106597900391,205.4106597900391,205.4106597900391,198.2454299926758,198.2454299926758,198.4947357177734,198.4947357177734,198.4947357177734,198.7649841308594,198.7649841308594,199.0708770751953,199.3908920288086,199.3908920288086,199.695671081543,199.695671081543,200.0519256591797,200.0519256591797,200.4160537719727,200.4160537719727,200.811897277832,200.811897277832,201.2165756225586,201.2165756225586,201.6273574829102,201.6273574829102,202.0163421630859,202.0163421630859,202.4083938598633,202.4083938598633,202.8063583374023,202.8063583374023,203.206787109375,203.206787109375,203.6103820800781,203.6103820800781,204.021354675293,204.021354675293,204.021354675293,204.4316635131836,204.8126220703125,205.2102279663086,205.2102279663086,205.6041488647461,205.6041488647461,205.6198196411133,205.6198196411133,205.6198196411133,205.6198196411133,198.4808883666992,198.4808883666992,198.7060623168945,198.7060623168945,198.9521102905273,199.2602005004883,199.2602005004883,199.5518417358398,199.5518417358398,199.838020324707,199.838020324707,200.1714859008789,200.1714859008789,200.5264358520508,200.5264358520508,200.861572265625,200.861572265625,201.2255783081055,201.6142272949219,201.6142272949219,201.6142272949219,201.9587173461914,202.3164596557617,202.3164596557617,202.6972503662109,202.6972503662109,202.6972503662109,203.094856262207,203.408447265625,203.408447265625,203.7799835205078,203.7799835205078,204.1737213134766,204.1737213134766,204.1737213134766,204.5060348510742,204.5060348510742,204.8814697265625,205.2736206054688,205.2736206054688,205.6244049072266,205.6244049072266,205.82568359375,205.82568359375,205.82568359375,205.82568359375,205.82568359375,205.82568359375,198.9215087890625,198.9215087890625,199.1711578369141,199.1711578369141,199.4642181396484,199.4642181396484,199.706413269043,199.706413269043,199.9876556396484,199.9876556396484,200.3047332763672,200.3047332763672,200.6030960083008,200.9406433105469,200.9406433105469,201.294075012207,201.294075012207,201.6611480712891,201.6611480712891,202.0363388061523,202.0363388061523,202.4357681274414,202.8388214111328,202.8388214111328,203.2059326171875,203.6028137207031,203.6028137207031,203.6028137207031,204.0011901855469,204.3680419921875,204.3680419921875,204.7636413574219,205.1672897338867,205.5470809936523,205.5470809936523,205.9160919189453,205.9160919189453,206.0282363891602,206.0282363891602,206.0282363891602,206.0282363891602,206.0282363891602,206.0282363891602,206.0282363891602,206.0282363891602,206.0282363891602,199.2862854003906,199.5361175537109,199.5361175537109,199.5361175537109,199.772590637207,200.0540542602539,200.3477401733398,200.3477401733398,200.6959915161133,200.6959915161133,201.0435028076172,201.0435028076172,201.4019317626953,201.4019317626953,201.7774658203125,201.7774658203125,202.1405868530273,202.5426712036133,202.9392929077148,202.9392929077148,203.3081512451172,203.3081512451172,203.3081512451172,203.707878112793,203.707878112793,204.1062393188477,204.1062393188477,204.4821319580078,204.8804626464844,204.8804626464844,205.2878494262695,205.6972732543945,205.6972732543945,206.0548782348633,206.0548782348633,206.2274017333984,206.2274017333984,206.2274017333984,206.2274017333984,206.2274017333984,206.2274017333984,206.2274017333984,206.2274017333984,206.2274017333984,199.579963684082,199.579963684082,199.8296661376953,199.8296661376953,200.0714721679688,200.3455657958984,200.3455657958984,200.6472778320312,200.9878845214844,201.3107604980469,201.6684799194336,201.6684799194336,202.0481033325195,202.4134368896484,202.4134368896484,202.8110198974609,202.8110198974609,203.2121429443359,203.2121429443359,203.6031723022461,203.9923553466797,203.9923553466797,204.3887786865234,204.8358383178711,204.8358383178711,205.2393112182617,205.6486282348633,205.6486282348633,206.0500106811523,206.0500106811523,206.4234237670898,206.4234237670898,206.4234237670898,206.4234237670898,206.4234237670898,206.4234237670898,199.7714157104492,200.0127639770508,200.263313293457,200.263313293457,200.5235748291016,200.8104095458984,200.8104095458984,201.1415328979492,201.4921569824219,201.4921569824219,201.8474884033203,201.8474884033203,202.2229919433594,202.2229919433594,202.6116943359375,202.6116943359375,202.6116943359375,202.9975967407227,202.9975967407227,203.3862609863281,203.3862609863281,203.7801666259766,203.7801666259766,204.1646347045898,204.1646347045898,204.5605239868164,204.5605239868164,204.9632949829102,204.9632949829102,205.368049621582,205.7725448608398,205.7725448608398,206.1712417602539,206.1712417602539,206.5600738525391,206.5600738525391,206.6162796020508,206.6162796020508,206.6162796020508,206.6162796020508,206.6162796020508,206.6162796020508,206.6162796020508,206.6162796020508,206.6162796020508,206.6162796020508,206.6162796020508,206.6162796020508,206.6162796020508,206.6162796020508,206.6162796020508,206.6162796020508,199.9801025390625,199.9801025390625,199.9801025390625,199.9801025390625,200.1925506591797,200.1925506591797,200.4300231933594,200.4300231933594,200.6726531982422,200.6726531982422,200.9257431030273,201.2340087890625,201.2340087890625,201.5635528564453,201.5635528564453,201.5635528564453,201.9037780761719,201.9037780761719,202.2589874267578,202.2589874267578,202.6539535522461,202.6539535522461,203.0563049316406,203.4576187133789,203.4576187133789,203.853157043457,203.853157043457,204.2534790039062,204.6575241088867,205.0609436035156,205.0609436035156,205.4660034179688,205.4660034179688,205.8718338012695,205.8718338012695,206.2792892456055,206.2792892456055,206.6859436035156,206.8059234619141,206.8059234619141,206.8059234619141,206.8059234619141,206.8059234619141,206.8059234619141,200.315055847168,200.315055847168,200.5463409423828,200.7859725952148,201.0286636352539,201.0286636352539,201.30908203125,201.30908203125,201.6276245117188,201.9665756225586,201.9665756225586,202.3173675537109,202.3173675537109,202.6794509887695,203.0559310913086,203.0559310913086,203.4534072875977,203.4534072875977,203.851921081543,203.851921081543,203.851921081543,204.2453308105469,204.2453308105469,204.2453308105469,204.6494903564453,204.6494903564453,205.0492324829102,205.4391098022461,205.4391098022461,205.4391098022461,205.8007278442383,206.200065612793,206.6055297851562,206.9925842285156,206.9925842285156,206.9925842285156,206.9925842285156,206.9925842285156,206.9925842285156,206.9925842285156,206.9925842285156,206.9925842285156,200.6353530883789,200.6353530883789,200.8638229370117,200.8638229370117,201.100944519043,201.100944519043,201.3415222167969,201.6285552978516,201.6285552978516,201.9457931518555,201.9457931518555,202.2837600708008,202.2837600708008,202.666877746582,202.666877746582,203.0342864990234,203.0342864990234,203.4187622070312,203.4187622070312,203.8141174316406,203.8141174316406,203.8141174316406,204.2154006958008,204.2154006958008,212.0868606567383,212.0868606567383,212.0868606567383,212.0868606567383,212.0868606567383,212.0868606567383,212.0868606567383,212.0868606567383,212.0868606567383,212.0868606567383,212.0868606567383,212.0868606567383,212.0868606567383,212.0868606567383,212.0868606567383,212.0868606567383,212.0868606567383,212.0868606567383,212.0868606567383,212.0868606567383,219.7162551879883,219.7162628173828,219.7162628173828,219.7162628173828,219.7162628173828,219.7162628173828,219.7162628173828,219.7162628173828,219.7162628173828,219.7162628173828,219.7162628173828,219.7162628173828,219.7162628173828,219.7162628173828,219.7162628173828,219.7162628173828,219.7162628173828,219.7162628173828,219.7162628173828,219.7162628173828,219.7162628173828,219.7162628173828,219.7162628173828,219.7162628173828,219.7162628173828,234.9750518798828,234.9750518798828,234.9750518798828,234.9750518798828,234.9750518798828,234.9750518798828,234.9750518798828,234.9750518798828,234.9750518798828,234.9750518798828,234.9750518798828,234.9750518798828,234.9750518798828,234.9750518798828,234.9750518798828,234.9750518798828,242.6044692993164,242.6044692993164,242.6044692993164,242.6044692993164,242.6044692993164,242.6044692993164,242.6044692993164,242.6044692993164,242.6714172363281,242.6714172363281,242.6714172363281,242.6714172363281,242.6714172363281,242.6714172363281,242.6714172363281,242.6714172363281,242.6714172363281,242.6714172363281,242.6714172363281,242.6714172363281,242.6714172363281,242.6714172363281,242.6714172363281,242.6714172363281,242.6714172363281,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406,257.9996643066406],"meminc":[0,0,0,0,2.288818359375e-05,0,15.28221130371094,0,0,0,30.46574401855469,0,0,0,0,0,4.57763671875e-05,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-0.00030517578125,0,15.44995880126953,0,0.251312255859375,0,0.2742385864257812,0,0,0.3120269775390625,0,0.379486083984375,0.3509674072265625,0,0.3848419189453125,0,0.40081787109375,0.402374267578125,0.31298828125,0,0,-2.956153869628906,0.3662185668945312,0,0.3992233276367188,0,0.4181442260742188,0,0.4060516357421875,0,0.4026107788085938,0.4033966064453125,0,0.4042510986328125,0.2260284423828125,0,0,-2.808074951171875,0,0.3595504760742188,0,0.3811569213867188,0,0,0.4090118408203125,0,0.4064712524414062,0,0.4007492065429688,0,0,0.4041595458984375,0.4044265747070312,0,0.129669189453125,0,0,-2.683944702148438,0,0.3627471923828125,0,0.385284423828125,0,0.4004974365234375,0,0.4051284790039062,0,0.4010086059570312,0,0.4023208618164062,0,0.4047012329101562,-2.875984191894531,0,0.3500137329101562,0,0.365692138671875,0.3815536499023438,0.4000320434570312,0,0.3986892700195312,0,0.386260986328125,0,0.4053268432617188,0,0.2807235717773438,0,-2.742904663085938,0,0.3431777954101562,0,0.365570068359375,0.3790283203125,0.3928451538085938,0,0,0.3919906616210938,0.4455718994140625,0,0.4042816162109375,0,0.1033477783203125,0,0,-2.541770935058594,0.3533706665039062,0,0.3663558959960938,0.3883743286132812,0,0.3830413818359375,0,0.3779525756835938,0,0.3887481689453125,0.3655242919921875,0,-2.749473571777344,0.3257980346679688,0.3217544555664062,0,0.35693359375,0,0.3492507934570312,0.3716278076171875,0,0.3874359130859375,0,0.3872756958007812,0,0.3297271728515625,0,0,-2.668777465820312,0,0.3271560668945312,0,0.3547439575195312,0,0.3597259521484375,0,0.4223709106445312,0,0.3911361694335938,0,0.3894195556640625,0,0.400238037109375,0,0.1030044555664062,0,0,-2.445625305175781,0.3478012084960938,0.3551101684570312,0,0.3753204345703125,0.390106201171875,0,0.3877792358398438,0,0.40045166015625,0,0.2667236328125,0,0,-2.54339599609375,0.3303680419921875,0,0.3497314453125,0.356842041015625,0.374359130859375,0.3889617919921875,0,0.3925628662109375,0,0,0.406402587890625,0,0,-2.605133056640625,0,0.3221588134765625,0.3437957763671875,0,0.3532638549804688,0.372467041015625,0.386749267578125,0.3883438110351562,0,0.3985519409179688,0,0.135650634765625,0,-2.377685546875,0.3282470703125,0,0.3437652587890625,0,0.3572769165039062,0,0.37762451171875,0,0.3888778686523438,0,0.3928985595703125,0,0.2630615234375,0,-2.435882568359375,0,0,0.3174057006835938,0.3706741333007812,0.350311279296875,0.37054443359375,0,0.3883209228515625,0,0.3907241821289062,0,0.320770263671875,0,-2.422294616699219,0,0.3169174194335938,0,0.3379974365234375,0,0.3521499633789062,0,0.3755340576171875,0,0.391693115234375,0.4026870727539062,0,0.31689453125,0,0,-2.384933471679688,0.3106155395507812,0,0,0.3293838500976562,0,0,0.3449478149414062,0.3734283447265625,0,0.3899307250976562,0,0,0.3994140625,0.3077392578125,0,0,-2.350685119628906,0,0.2996902465820312,0,0.3235549926757812,0,0.344085693359375,0.370849609375,0.3863296508789062,0,0.4027328491210938,0,0.2927703857421875,0,-2.290084838867188,0,0.30072021484375,0.3194808959960938,0.340423583984375,0.3635330200195312,0,0.384979248046875,0,0.392364501953125,0,0.2568511962890625,0,-2.215103149414062,0,0.2974090576171875,0,0.31866455078125,0.342193603515625,0,0.3638153076171875,0.3790206909179688,0,0.392547607421875,0.1885833740234375,0,0,-2.164527893066406,0,0.2890167236328125,0.3159637451171875,0.3397445678710938,0,0,0.36053466796875,0.3710174560546875,0,0.3972625732421875,0.1570663452148438,0,0,-2.103080749511719,0,0.2911834716796875,0.3162078857421875,0,0.3447418212890625,0.35906982421875,0,0.3742446899414062,0.394012451171875,0.08856964111328125,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2.236785888671875,0,0,0.1400070190429688,0.223388671875,0,0.2384872436523438,0,0.2392196655273438,0.2971878051757812,0.326080322265625,0,0.33465576171875,0.3603744506835938,0,0.141082763671875,0,0,-2.035621643066406,0,0.2839736938476562,0,0.3220138549804688,0,0.3468475341796875,0.3717269897460938,0.3872451782226562,0,0.3867111206054688,0,0,0,0,0,-1.891555786132812,0,0,0.297821044921875,0.3329391479492188,0.34698486328125,0,0.374267578125,0,0.3934173583984375,0,0.2080078125,0,-2.008804321289062,0,0.2779159545898438,0,0.3134231567382812,0,0,0.3415069580078125,0.3582763671875,0,0,0.3800735473632812,0,0.3944778442382812,0,0.00408172607421875,0,-1.845382690429688,0,0.2900924682617188,0,0.3251190185546875,0,0.3487472534179688,0.3966598510742188,0,0.3750534057617188,0,0.169647216796875,0,0,-1.944938659667969,0,0.264373779296875,0,0.302215576171875,0,0.3351516723632812,0,0.3514785766601562,0,0.3749923706054688,0,0.37567138671875,0,0,0,0,0,-1.782112121582031,0,0.2873992919921875,0,0.324920654296875,0.3478546142578125,0,0.3653564453125,0,0,0.389617919921875,0.1249237060546875,0,-1.835601806640625,0,0.2788848876953125,0,0.3175430297851562,0.3473434448242188,0.3636856079101562,0.385345458984375,0,0.1998977661132812,0,0,-1.85479736328125,0.2730941772460938,0,0.3120651245117188,0,0.3437042236328125,0,0.3602752685546875,0,0,0.3751449584960938,0,0.246673583984375,0,-1.864158630371094,0,0,0.2668609619140625,0,0.3323974609375,0,0.3389968872070312,0,0.3520126342773438,0,0.3742599487304688,0,0.25482177734375,0,0,-1.842536926269531,0.2591705322265625,0,0.2986679077148438,0.335968017578125,0.3531036376953125,0,0.3719635009765625,0,0.278076171875,0,-1.823585510253906,0,0.2605209350585938,0.291534423828125,0.3292999267578125,0,0.3500900268554688,0,0.3721694946289062,0,0.2734146118164062,0,0,-1.788864135742188,0,0.2576065063476562,0,0.2935638427734375,0,0.333038330078125,0,0.3564682006835938,0.3754653930664062,0,0,0.2253494262695312,0,0,-1.7354736328125,0,0,0.263031005859375,0,0,0.3014450073242188,0,0.3704986572265625,0,0.3524856567382812,0,0.3732376098632812,0,0,0.1265182495117188,0,0,-1.654563903808594,0,0.2600326538085938,0,0.3062362670898438,0,0.3387985229492188,0,0.3569183349609375,0,0.3785476684570312,0,0.06493377685546875,0,0,-1.58135986328125,0.277252197265625,0.3193588256835938,0.3426666259765625,0,0,0.3596954345703125,0,0.3325271606445312,0,0,0,-1.476173400878906,0,0.2848281860351562,0.322296142578125,0,0.3465576171875,0,0.3621673583984375,0.2095413208007812,0,0,-1.623085021972656,0,0.2883834838867188,0.3063430786132812,0,0.3387527465820312,0.3526077270507812,0,0.3797760009765625,0.00574493408203125,0,0,0,-1.458763122558594,0.2801666259765625,0,0.325347900390625,0,0.3502349853515625,0,0.3658676147460938,0.1848297119140625,0,0,-1.549087524414062,0,0.2633895874023438,0,0.3060531616210938,0,0.3407516479492188,0.3590927124023438,0.3267135620117188,0,0,0,0,0,-1.362312316894531,0,0.287445068359375,0,0.3284759521484375,0.34979248046875,0.3678207397460938,0.0749664306640625,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.589950561523438,0,0,0,0.1772918701171875,0,0.251861572265625,0,0.2821121215820312,0,0.3155670166015625,0.320037841796875,0,0.3330764770507812,0.3770980834960938,0,0.3466720581054688,0,0.3716583251953125,0.3328781127929688,0,0.3329010009765625,0,0,0.3349609375,0.3311233520507812,0,0.3346328735351562,0,0.3357162475585938,0,0.06280517578125,0,0,-4.438507080078125,0.3284683227539062,0,0.3567123413085938,0,0.338897705078125,0.351409912109375,0,0.4076309204101562,0.4127197265625,0.4074554443359375,0.4058761596679688,0,0.4095993041992188,0,0.409942626953125,0.4065780639648438,0.3356399536132812,0,0,0,0,0,-4.337173461914062,0,0.3172836303710938,0,0.344268798828125,0,0.3230667114257812,0,0.363922119140625,0,0,0.402740478515625,0,0.4147796630859375,0,0.4081954956054688,0,0.4129257202148438,0.4087905883789062,0.4022140502929688,0,0.401519775390625,0,0.2677383422851562,0,0,0,0,0,-4.219718933105469,0.3196640014648438,0,0.3325653076171875,0,0.3261566162109375,0.3738937377929688,0.4043655395507812,0,0,0.4153976440429688,0.4035415649414062,0,0.4078140258789062,0,0.409027099609375,0,0.4102706909179688,0,0.4007644653320312,0.1444168090820312,0,-4.308250427246094,0.2961654663085938,0,0.3233718872070312,0,0.3159255981445312,0.3663711547851562,0,0.3865280151367188,0,0.4120407104492188,0,0,0.4118881225585938,0.4089889526367188,0,0.4087295532226562,0.4089889526367188,0,0.4083786010742188,0.2869110107421875,0,0,0,-4.095046997070312,0,0.309326171875,0,0.3106155395507812,0,0.343719482421875,0.3695526123046875,0,0.3964004516601562,0,0.4124298095703125,0,0.4107284545898438,0.4111404418945312,0,0.4099884033203125,0.4109573364257812,0.4009628295898438,0.0333404541015625,0,-4.125144958496094,0,0.29620361328125,0,0.3061981201171875,0,0.33160400390625,0,0.3648529052734375,0,0.3885345458984375,0.407562255859375,0,0.407470703125,0,0.4083175659179688,0.447174072265625,0,0.4081192016601562,0,0.398162841796875,0,0,0.0829925537109375,0,0,-4.100448608398438,0,0.2867813110351562,0.29522705078125,0.3271408081054688,0,0,0.3585357666015625,0,0.3705825805664062,0,0,0.3855209350585938,0,0,0.3984909057617188,0,0.4028701782226562,0,0.4003067016601562,0,0.4094314575195312,0.4032211303710938,0,0.1824417114257812,0,0,-4.112625122070312,0,0.2724609375,0,0.2858734130859375,0,0,0.3116226196289062,0,0.3536300659179688,0,0.37054443359375,0,0.3990554809570312,0,0,0.4081497192382812,0,0.4109649658203125,0,0.4097900390625,0.4102249145507812,0,0.4066162109375,0,0.1917648315429688,0,0,0,-4.049026489257812,0.2728500366210938,0,0.28094482421875,0,0.31463623046875,0.3874053955078125,0,0.36865234375,0,0.3857650756835938,0.3945770263671875,0.3857650756835938,0.39337158203125,0,0,0.4020614624023438,0.4012680053710938,0,0,0.177978515625,0,-3.988662719726562,0,0.2662200927734375,0,0.2733535766601562,0,0.3199615478515625,0.350006103515625,0.3654098510742188,0.3861541748046875,0,0.4041213989257812,0,0.4104766845703125,0,0.4128952026367188,0,0.4128799438476562,0,0.4039382934570312,0,0.0976104736328125,0,0,-3.8668212890625,0,0.2638778686523438,0,0.27783203125,0.3277359008789062,0,0.3533935546875,0,0.365936279296875,0,0.3939437866210938,0.3991928100585938,0,0.4072265625,0,0.4064483642578125,0,0.4088363647460938,0,0.3749237060546875,0,0,0,-3.712547302246094,0,0.2609481811523438,0,0.269561767578125,0,0.302825927734375,0,0.3367385864257812,0.3513031005859375,0,0.37762451171875,0.3939437866210938,0.398529052734375,0,0,0.4022445678710938,0.4051132202148438,0,0.3244400024414062,0,0,0,-3.640380859375,0,0.25634765625,0,0.3023300170898438,0,0.3325271606445312,0,0.3422012329101562,0,0.3615264892578125,0.3856582641601562,0,0,0.4008255004882812,0.4077606201171875,0,0.4079818725585938,0,0,0.40118408203125,0,0.1509170532226562,0,-3.721832275390625,0,0.2535324096679688,0,0.3040008544921875,0.3116302490234375,0.3356094360351562,0,0.3553924560546875,0,0.3852920532226562,0.4009857177734375,0,0.4059295654296875,0.4080810546875,0.40289306640625,0,0.2657012939453125,0,0,0,0,0,0,0,-3.489341735839844,0.2567214965820312,0.2974319458007812,0,0.3252792358398438,0,0.3481292724609375,0.3651885986328125,0,0.3814849853515625,0,0.3939971923828125,0.4086685180664062,0,0.4053802490234375,0.3931503295898438,0.019317626953125,0,0,-3.551956176757812,0,0.2477493286132812,0,0.2886581420898438,0,0.3138809204101562,0.3382568359375,0,0.3568496704101562,0.381866455078125,0,0,0.3966751098632812,0.4034194946289062,0.4064483642578125,0,0.402191162109375,0,0.11968994140625,0,0,-3.51324462890625,0,0.24005126953125,0,0.2732772827148438,0,0.298492431640625,0.3271942138671875,0,0.34674072265625,0,0.364990234375,0.3868179321289062,0.39459228515625,0,0.406951904296875,0,0.3982467651367188,0.1778717041015625,0,0,0,-3.281791687011719,0.2625503540039062,0,0.2905731201171875,0,0,0.3180084228515625,0.3517608642578125,0,0.3704299926757812,0,0.3959503173828125,0.4024658203125,0,0.4085769653320312,0,0.4022979736328125,0,0.1796035766601562,0,0,0,-3.284690856933594,0.246063232421875,0,0.2754974365234375,0,0.30181884765625,0,0.3353042602539062,0,0.3609542846679688,0,0.3955230712890625,0,0.452789306640625,0.4139404296875,0,0.4076385498046875,0.1939697265625,0,0,0,-3.196182250976562,0.25408935546875,0,0.2787246704101562,0,0.3058242797851562,0,0.3395462036132812,0,0.36431884765625,0,0.3979110717773438,0,0.4104537963867188,0,0.4127731323242188,0.4023208618164062,0,0,0.1273880004882812,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-3.345046997070312,0,0,0.067596435546875,0,0.197601318359375,0.2248916625976562,0.2363662719726562,0.2668991088867188,0,0.3028717041015625,0,0.3204879760742188,0.3353042602539062,0,0.3702316284179688,0,0.3979721069335938,0,0.3964157104492188,0,0.32373046875,0,0,0,-3.198028564453125,0,0.2412948608398438,0,0.2741012573242188,0,0.3069076538085938,0,0.3332061767578125,0,0.323822021484375,0.3626708984375,0,0,0.3808212280273438,0.404266357421875,0,0.44744873046875,0,0,0.2175827026367188,0,0,0,0,0,-3.050613403320312,0,0.248779296875,0.2732391357421875,0,0,0.3096466064453125,0.338226318359375,0,0.3529129028320312,0.3754959106445312,0,0.3998794555664062,0,0.4101104736328125,0,0,0.4087142944335938,0.02625274658203125,0,-3.115386962890625,0,0.2365188598632812,0,0,0.2605667114257812,0,0.2916641235351562,0,0.3241348266601562,0.3484268188476562,0,0.3609542846679688,0.3880996704101562,0.3982772827148438,0.25439453125,0,0,0.3434066772460938,0,0,0,0,0,-3.03363037109375,0,0.2366104125976562,0,0.2611160278320312,0.3276138305664062,0.3188934326171875,0.2998046875,0,0.3279876708984375,0.3498458862304688,0,0.365570068359375,0.3937225341796875,0,0,0.2421493530273438,0,0,0,0,0,-2.979385375976562,0.2304000854492188,0,0.2388381958007812,0,0.29339599609375,0,0.3256683349609375,0,0.3488922119140625,0,0.347991943359375,0.346710205078125,0,0.3786392211914062,0.399444580078125,0,0.15753173828125,0,0,0,0,0,-2.827064514160156,0,0.2460174560546875,0,0.2727584838867188,0.30633544921875,0,0,0.3381195068359375,0,0.3506317138671875,0,0,0.40045166015625,0,0.3858718872070312,0,0.4016876220703125,0.2119293212890625,0,0,0,0,0,-2.812217712402344,0.2328567504882812,0.2631607055664062,0,0.2907638549804688,0,0.3246307373046875,0,0.3453903198242188,0.3344573974609375,0.3353347778320312,0.3642349243164062,0,0.3948211669921875,0,0.011932373046875,0,0,0,0,0,-2.736892700195312,0,0.229248046875,0.2552719116210938,0,0.2895431518554688,0,0.3251571655273438,0,0,0.342864990234375,0,0,0.3530349731445312,0.3774185180664062,0.3921051025390625,0,0.2561569213867188,0,0,0,0,0,-2.727821350097656,0,0,0.2323760986328125,0.257720947265625,0,0.2867507934570312,0,0.320037841796875,0,0.33837890625,0.3507766723632812,0,0.37176513671875,0.3928909301757812,0.259735107421875,0,0,0,0,0,0,0,-2.703231811523438,0.2321014404296875,0,0.2624435424804688,0.2921142578125,0.3287734985351562,0.3475112915039062,0.3518905639648438,0.3800125122070312,0,0.4024810791015625,0,0.1871490478515625,0,0,0,-2.617958068847656,0,0.2335968017578125,0.2622604370117188,0,0.2971572875976562,0.33087158203125,0.3482131958007812,0,0.355621337890625,0,0.4157257080078125,0,0.3950119018554688,0,0,0.05947113037109375,0,0,-2.736068725585938,0,0.2242279052734375,0,0.2379913330078125,0.2689285278320312,0,0.30377197265625,0,0.3353500366210938,0,0.3503875732421875,0.3521804809570312,0,0.36920166015625,0,0.372711181640625,0,0,0,0,0,-2.651321411132812,0,0.2223892211914062,0.2377471923828125,0,0.2699661254882812,0.3040390014648438,0.33477783203125,0,0.3497543334960938,0,0.3572006225585938,0,0.3813629150390625,0,0.2714309692382812,0,0,0,0,0,-2.539573669433594,0.2287979125976562,0.2747573852539062,0,0.2844314575195312,0,0.321319580078125,0,0.3442459106445312,0,0.3550567626953125,0,0.3714141845703125,0.4019088745117188,0,0.03382110595703125,0,0,-2.585159301757812,0.22454833984375,0.2398223876953125,0,0.2723236083984375,0,0.3088531494140625,0,0.3366165161132812,0.3504257202148438,0.36334228515625,0.3960494995117188,0.168121337890625,0,0,0,0,0,-2.393638610839844,0,0.234344482421875,0.264190673828125,0,0.3014984130859375,0,0.3331832885742188,0,0.3494415283203125,0,0.364593505859375,0,0,0.3940963745117188,0,0.2259597778320312,0,0,0,-2.393508911132812,0.249755859375,0,0.2593002319335938,0,0.2939224243164062,0,0.3295440673828125,0.3031158447265625,0.326141357421875,0,0.3507766723632812,0,0.2867279052734375,0,0.06674957275390625,0,0,0,-2.361099243164062,0,0.205841064453125,0,0.2380752563476562,0.25970458984375,0,0.2621841430664062,0,0.3132705688476562,0.3336868286132812,0.3181533813476562,0,0.3448638916015625,0,0.1567001342773438,0,0,0,-2.339363098144531,0,0.2214508056640625,0,0.2372589111328125,0,0.2144851684570312,0.2821731567382812,0.3151016235351562,0,0,0.2563629150390625,0,0.3082122802734375,0.3363113403320312,0,0.2382354736328125,0,0,0,0,0,-2.23797607421875,0.218994140625,0.2382278442382812,0,0.2722244262695312,0,0.3075637817382812,0,0.33905029296875,0,0.3905868530273438,0,0.3799057006835938,0,0,0.160430908203125,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2.360908508300781,0.159576416015625,0,0.1389083862304688,0,0.2085037231445312,0,0.2416610717773438,0,0.2736740112304688,0,0.3060531616210938,0,0.333984375,0.3485488891601562,0.3689727783203125,0.048736572265625,0,0,-2.3048095703125,0.2225418090820312,0,0.2367172241210938,0,0,0.2709732055664062,0.3053817749023438,0.3071441650390625,0,0.350799560546875,0,0.3639373779296875,0,0.3141937255859375,0,0,0,-2.230796813964844,0,0.2249832153320312,0,0,0.2427291870117188,0,0.2802047729492188,0,0.317596435546875,0,0,0.3473129272460938,0.3589096069335938,0.3810348510742188,0,0,0.14385986328125,0,0,0,-2.084457397460938,0,0.2172012329101562,0,0,0.2578201293945312,0.29620361328125,0.3316421508789062,0,0.3492050170898438,0.4009628295898438,0.2961502075195312,0,0,0,0,0,-2.135459899902344,0,0,0.2274551391601562,0.2468948364257812,0.285675048828125,0.3226699829101562,0,0.349700927734375,0,0.3586578369140625,0,0.3918380737304688,0,0.01633453369140625,0,0,-2.173187255859375,0.2140731811523438,0,0.2382659912109375,0,0,0.2689743041992188,0,0.3041000366210938,0,0.3351593017578125,0,0.3503189086914062,0.3388519287109375,0.1861190795898438,0,0,0,0,0,-2.058174133300781,0.214630126953125,0,0.2398529052734375,0,0.261810302734375,0.2882080078125,0.3274307250976562,0.3456192016601562,0,0.3384933471679688,0,0.1037445068359375,0,0,0,0,0,0,0,-1.971466064453125,0.2079391479492188,0,0.2373504638671875,0.2529296875,0.2791824340820312,0.3241043090820312,0.3454818725585938,0,0.2958297729492188,0,0.0893402099609375,0,0,0,0,0,-1.931648254394531,0,0.2255477905273438,0.2647323608398438,0,0.2741317749023438,0,0.2831649780273438,0,0.3534774780273438,0,0.3333511352539062,0,0.2569198608398438,0,0,0,0,0,0,0,-1.99859619140625,0,0.2172622680664062,0.2374191284179688,0,0.277923583984375,0,0.304962158203125,0,0.3353652954101562,0,0.3534088134765625,0,0.3309402465820312,0,0,0,0,0,-1.977348327636719,0,0.2437896728515625,0.2216262817382812,0.2701797485351562,0,0.310577392578125,0.3075027465820312,0.3456497192382812,0,0,0.3358306884765625,0,0,0,0,0,-1.955879211425781,0,0.2173614501953125,0,0.2400360107421875,0.2696609497070312,0.3081817626953125,0,0.3403167724609375,0.3495025634765625,0,0.28759765625,0,0,0,0,0,-1.8956298828125,0.224395751953125,0,0.23773193359375,0,0.2752151489257812,0.3079833984375,0.341033935546875,0.3755874633789062,0.18963623046875,0,0,0,0,0,-1.880043029785156,0,0.2158050537109375,0,0,0.2369232177734375,0,0.275787353515625,0,0.3081741333007812,0,0.3354873657226562,0,0.356201171875,0,0.2066650390625,0,0,0,-1.801162719726562,0,0.2177734375,0,0.2301559448242188,0,0.2419815063476562,0.3078079223632812,0,0.3377685546875,0,0.3522186279296875,0,0.1675643920898438,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.863052368164062,0,0,0.1091995239257812,0.21014404296875,0.2300872802734375,0,0,0.2533493041992188,0,0.2881317138671875,0,0.3207931518554688,0,0.3361892700195312,0,0.1682891845703125,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.8328857421875,0,0,0,0,0,0.04212188720703125,0,0.23486328125,0.251556396484375,0,0.2783126831054688,0,0,0.3121490478515625,0,0.3209457397460938,0.3090133666992188,0.3477935791015625,0,0.3807830810546875,0,0.4031143188476562,0,0.3742446899414062,0.3349990844726562,0,0.3331069946289062,0,0.3323287963867188,0,0.3323211669921875,0,0.3315277099609375,0.3344497680664062,0,0.3352279663085938,0.333343505859375,0,0.334625244140625,0,0.334747314453125,0.3334732055664062,0.3335800170898438,0.3344573974609375,0.05556488037109375,0,0,0,0,0,-7.165229797363281,0,0.2493057250976562,0,0,0.2702484130859375,0,0.3058929443359375,0.3200149536132812,0,0.304779052734375,0,0.3562545776367188,0,0.3641281127929688,0,0.395843505859375,0,0.4046783447265625,0,0.4107818603515625,0,0.3889846801757812,0,0.3920516967773438,0,0.3979644775390625,0,0.4004287719726562,0,0.403594970703125,0,0.4109725952148438,0,0,0.410308837890625,0.3809585571289062,0.3976058959960938,0,0.3939208984375,0,0.0156707763671875,0,0,0,-7.138931274414062,0,0.2251739501953125,0,0.2460479736328125,0.3080902099609375,0,0.2916412353515625,0,0.2861785888671875,0,0.333465576171875,0,0.354949951171875,0,0.3351364135742188,0,0.3640060424804688,0.3886489868164062,0,0,0.3444900512695312,0.3577423095703125,0,0.3807907104492188,0,0,0.3976058959960938,0.3135910034179688,0,0.3715362548828125,0,0.39373779296875,0,0,0.3323135375976562,0,0.3754348754882812,0.39215087890625,0,0.3507843017578125,0,0.2012786865234375,0,0,0,0,0,-6.9041748046875,0,0.2496490478515625,0,0.293060302734375,0,0.2421951293945312,0,0.2812423706054688,0,0.31707763671875,0,0.2983627319335938,0.3375473022460938,0,0.3534317016601562,0,0.3670730590820312,0,0.3751907348632812,0,0.3994293212890625,0.4030532836914062,0,0.3671112060546875,0.396881103515625,0,0,0.39837646484375,0.366851806640625,0,0.395599365234375,0.4036483764648438,0.379791259765625,0,0.3690109252929688,0,0.1121444702148438,0,0,0,0,0,0,0,0,-6.741950988769531,0.2498321533203125,0,0,0.2364730834960938,0.281463623046875,0.2936859130859375,0,0.3482513427734375,0,0.3475112915039062,0,0.358428955078125,0,0.3755340576171875,0,0.3631210327148438,0.4020843505859375,0.3966217041015625,0,0.3688583374023438,0,0,0.3997268676757812,0,0.3983612060546875,0,0.3758926391601562,0.3983306884765625,0,0.4073867797851562,0.409423828125,0,0.35760498046875,0,0.1725234985351562,0,0,0,0,0,0,0,0,-6.647438049316406,0,0.2497024536132812,0,0.2418060302734375,0.2740936279296875,0,0.3017120361328125,0.340606689453125,0.3228759765625,0.3577194213867188,0,0.3796234130859375,0.3653335571289062,0,0.3975830078125,0,0.401123046875,0,0.3910293579101562,0.3891830444335938,0,0.39642333984375,0.4470596313476562,0,0.403472900390625,0.4093170166015625,0,0.4013824462890625,0,0.3734130859375,0,0,0,0,0,-6.652008056640625,0.2413482666015625,0.25054931640625,0,0.2602615356445312,0.286834716796875,0,0.3311233520507812,0.3506240844726562,0,0.3553314208984375,0,0.3755035400390625,0,0.388702392578125,0,0,0.3859024047851562,0,0.3886642456054688,0,0.3939056396484375,0,0.3844680786132812,0,0.3958892822265625,0,0.40277099609375,0,0.404754638671875,0.4044952392578125,0,0.3986968994140625,0,0.3888320922851562,0,0.05620574951171875,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-6.636177062988281,0,0,0,0.2124481201171875,0,0.2374725341796875,0,0.2426300048828125,0,0.2530899047851562,0.3082656860351562,0,0.3295440673828125,0,0,0.3402252197265625,0,0.3552093505859375,0,0.3949661254882812,0,0.4023513793945312,0.4013137817382812,0,0.395538330078125,0,0.4003219604492188,0.4040451049804688,0.4034194946289062,0,0.405059814453125,0,0.4058303833007812,0,0.4074554443359375,0,0.4066543579101562,0.1199798583984375,0,0,0,0,0,-6.490867614746094,0,0.2312850952148438,0.2396316528320312,0.2426910400390625,0,0.2804183959960938,0,0.31854248046875,0.3389511108398438,0,0.3507919311523438,0,0.3620834350585938,0.3764801025390625,0,0.3974761962890625,0,0.3985137939453125,0,0,0.3934097290039062,0,0,0.4041595458984375,0,0.3997421264648438,0.3898773193359375,0,0,0.3616180419921875,0.3993377685546875,0.4054641723632812,0.387054443359375,0,0,0,0,0,0,0,0,-6.357231140136719,0,0.2284698486328125,0,0.23712158203125,0,0.2405776977539062,0.2870330810546875,0,0.3172378540039062,0,0.3379669189453125,0,0.38311767578125,0,0.3674087524414062,0,0.3844757080078125,0,0.395355224609375,0,0,0.4012832641601562,0,7.8714599609375,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7.62939453125,7.62939453125e-06,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,15.2587890625,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7.629417419433594,0,0,0,0,0,0,0,0.06694793701171875,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,15.3282470703125,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"filename":["<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>","<expr>",null,null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,null,null,null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,null,null,null,null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,null,null,null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,null,null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,null,null,null,null,null,null,null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,"<expr>","<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null]},"interval":10,"files":[{"filename":"<expr>","content":"## Generate Large Random Dataset\nn <- 2e6\nx <- runif(n)\ny <- runif(n)\nz <- runif(n)\nXYZ <- cbind(x,y,z)\n\n## Inspect 4 equivalent `row mean` calculations \nprofvis::profvis({\n    m <- rowSums(XYZ)/ncol(XYZ)\n    m <- rowMeans(XYZ)\n    m <- apply(XYZ, 1, mean)\n    m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }\n})\n## rowSums(), colSums(), rowMeans(), and colMeans() are vectorised and fast.\n## for loop is not the slowest, but the ugliest.","normpath":"<expr>"}],"prof_output":"/tmp/RtmpdLvgof/file44c35c3d4a6f.prof","highlight":{"output":["^output\\$"],"gc":["^<GC>$"],"stacktrace":["^\\.\\.stacktraceo(n|ff)\\.\\.$"]},"split":"h"}},"evals":[],"jsHooks":[]}</script>
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
## 1 mean1(x, 0.5)   20.2ms   21.9ms      45.9    7.63MB     2.09
## 2 mean2(x, 0.5)   19.1ms   21.1ms      47.8    7.63MB     0   
## 3 mean3(x, 0.5)     20ms   21.9ms      46.2    7.63MB     2.10
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
##   0.104   0.000   0.032
```

```r
system.time({ lm(Y~X, data=DAT) })
```

```
##    user  system elapsed 
##   0.405   0.000   0.136
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
## 1 ma1(y)      163.3ms    166ms      6.05    15.3MB     2.02
## 2 ma2(y)       21.6ms   21.8ms     45.9     91.6MB   367.
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
##   0.027   0.003   0.030
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
##   0.795   0.249   0.586
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





