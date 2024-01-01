# (PART) Reproducible Research in R {-} 


# Why?
***

Before hopping into reproducible programming, lets think about why. My main sell to you is that it is in your own self-interest.  

## An example workflow

Taking First Steps ...

**Step 1:** Some Ideas and Data

$X_{1} \to Y_{1}$

* You copy some data into a spreadsheet, manually aggregate
* do some calculations and tables the same spreadsheet
* some other analysis from here and there, using this software and that.

**Step 2:** Pursuing the lead for a week or two

* you extend your dataset with more observations
* copy in a spreadsheet data, manually aggregate
* do some more calculations and tables, same as before



Then, a Little Way Down the Road ...

**1 month later**, someone asks about another factor: $X_{2}$

* you download some other type of data
* You repeat **Step 2** with some data on $X_{2}$.
* The details from your "point and click" method are a bit fuzzy.
* It takes a little time, but you successfully redo the analysis.


**4 months later**, someone asks about another factor: $X_{3}\to Y_{1}$

* You again repeat **Step 2** with some data on $X_{3}$.
* You're pretty sure none of tables your tried messed up the order of the rows or columns.
* It takes more time and effort. The data processing was not transparent, but you eventually redo the analysis.



**6 months later**, you want to explore: $X_{2} \to Y_{2}$.

* You found out Excel had some bugs in it's statistical calculations (see e.g., https://biostat.app.vumc.org/wiki/pub/Main/TheresaScott/StatsInExcel.TAScot.handout.pdf). You now use a new version of the spreadsheet
* You're not sure you merged everything correctly. After much time and effort, most (but not all) of the numbers match exactly.
 

**2 years later**, you want to replicate: $\{ X_{1}, X_{2}, X_{3} \} \to Y_{1}$

* A rival has proposed something new. Their idea doesn't actually make any sense, but their figures and statistics look better.
* You don't even use that computer anymore and a collaborator who handled the data on $X_{2}$ has moved on.


## An alternative workflow

Suppose you decided to code what you did beginning with Step 2.

**It does not take much time to update or replicate your results.**

* Your computer runs for 2 hours and reproduces the figures and tables.
* You also rewrote your big calculations to use multiple cores, this took two hours to do but saved 6 hours *each time* you rerun your code.
* You add some more data. It adds almost no time to see whether much has changed.

**Your results are transparent and easier to build on.**

* You see the exact steps you took and found an error
  * glad you found it before publication! See https://retractionwatch.com/ and https://econjwatch.org/
  * Google "worst excell errors" and note the frequency they arise from copy/paste via the "point-and-click" approach.
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


## Code Chunks

Save the following code as `CodeChunk.R`

```r
## Define New Function
sum_squared <- function(x1, x2) {
	y <- (x1 + x2)^2
	return(y)
} 

## Test New Function
x <- c(0,1,3,10,6)
sum_squared(x[1], x[3])
sum_squared(x, x[2])
sum_squared(x, x[7])
sum_squared(x, x)

message('Chunk Completed')
```

**Clean the workspace** In the right panels, manually cleanup

* save the code as *MyFirstCode.R*
* clear the environment and history (use the broom in top right panel)
* clear unsaved plots (use the broom in bottom right panel)

    
**Replicate** either in another tab or directly in console on the bottom left, enter

```r
source('MyFirstCode.R')
```
Note that you may first need to `setwd()` so your computer knows where you saved your code.^[You can also use *GUI: point-click* click 'Source > Source as a local job' on top right]


After you get this working
* add a the line `print(sum_squared(y, y))` to the bottom of `MyFirstCode.R`. 
* apply the function to a vectors specified outside of that script

```r
## Pass Objects/Functions *to* Script
y <- c(3,1,NA)
source('MyFirstCode.R')

## Pass Objects/Functions *from* Script
z <- sqrt(y)/2
sum_squared(z,z)
```

**CLI Alternatives** *(Skippable)* There are also alternative ways to replicate via the command line interface (CLI) after opening a terminal.
 

```bash
## Method 1
Rscript -e "source('CodeChunk.R')"
## Method 2
Rscript CodeChunk.R
```

Note that you can open a new terminal in RStudio in the top bar by
clicking 'tools > terminal > new terminal'



## Reports

We will create reproducible reports via R Markdown.

**Example 1: Data Scientism**
<!-- 
**Clean workspace**
Delete any temporary files which you do not want (or start a fresh session).

(for example *summarytable_example.txt* and *plot_example.pdf* and section *Data analysis examples: custom figures*)
-->


See [DataScientism.html](https://jadamso.github.io/Rbooks/Templates/DataScientism.html) and then create it by

* Clicking the "Code" button in the top right and then "Download Rmd"
* Opening with Rstudio, change the name to your own, change the title to "Data Scientism Replication"
* then point-and-click "knit"


Alternatively, 
* download the source file from [DataScientism.Rmd](https://jadamso.github.io/Rbooks/Templates/DataScientism.Rmd)
* use the console to run

```r
rmarkdown::render('DataScientism.Rmd')
```


**Example 2: Homework Assignment**
Below is a template of what homework questions (and answers) look like. Create an .Rmd from scratch that produces a similar looking .html file.

*Question 1:*
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
<div class="plotly html-widget html-fill-item" id="htmlwidget-359269e09303dd2357db" style="width:672px;height:480px;"></div>
<script type="application/json" data-for="htmlwidget-359269e09303dd2357db">{"x":{"visdat":{"3195201b852":["function () ","plotlyVisDat"]},"cur_data":"3195201b852","attrs":{"3195201b852":{"x":{},"y":{},"alpha_stroke":1,"sizes":[10,100],"spans":[1,20]}},"layout":{"margin":{"b":40,"l":60,"t":25,"r":10},"xaxis":{"domain":[0,1],"automargin":true,"title":"X"},"yaxis":{"domain":[0,1],"automargin":true,"title":"Y"},"hovermode":"closest","showlegend":false},"source":"A","config":{"modeBarButtonsToAdd":["hoverclosest","hovercompare"],"showSendToCloud":false},"data":[{"x":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100],"y":[3.7951211061150221,6.8483697786925291,13.080166509251193,15.559497530871807,23.748529016468169,23.274870446661453,29.226369072903772,30.921277027090721,37.460626553163365,43.018899225345109,44.056574703456981,47.615032867817291,51.53352996183483,55.486484555394689,59.453774029631163,63.928771114168661,64.959163216242985,73.272116279291495,75.004721194549219,79.44192988751783,82.403563157721294,85.640044393555897,92.798942123498918,98.741858213272195,101.92878468844644,107.1570622041575,108.27011116364815,115.46964121363573,116.69831448944346,119.83950524017156,122.53255104731228,129.47982828884201,133.66902645355796,134.89972156047614,144.13678796288002,143.85125668644145,152.21416477211147,153.44436628346989,153.62336225442147,159.73236906223494,162.23722149103614,164.8982856955104,174.7118753994159,173.76028566146366,179.4551044007367,182.30656728060859,185.95015592070783,190.86986748775621,199.28352157094645,200.60031010361863,208.56633878118183,211.60309786778012,208.7595414630606,218.15184804485989,218.47022986373588,225.08191212231949,225.23050766852145,229.9001189972831,236.02206541252369,239.01838666058202,240.45038760509456,248.21478825082824,253.44637599077623,258.25103138679242,260.78468731527681,263.93559596932886,265.20881435154075,270.90629449895391,275.51965050577684,279.08299772272625,282.63843766015435,285.49719998913787,289.82570004736652,296.07082570636499,296.0393370484623,306.0859458736237,305.2863850395118,312.77637713817211,315.67766488211794,315.7955014362422,324.26007199169328,327.10542543224744,331.93595624245069,336.14417659889062,337.55629764729076,342.85214613315117,345.83976154512658,353.3405277597405,354.25943480249094,361.06399541538121,365.34442633167959,369.78741566143083,369.85771415093546,376.98352050538864,380.76528763229948,382.8510054900139,390.83631333226526,390.86678424302102,397.71172447794862,398.30629266570048],"type":"scatter","mode":"markers","marker":{"color":"rgba(31,119,180,1)","line":{"color":"rgba(31,119,180,1)"}},"error_y":{"color":"rgba(31,119,180,1)"},"error_x":{"color":"rgba(31,119,180,1)"},"line":{"color":"rgba(31,119,180,1)"},"xaxis":"x","yaxis":"y","frame":null}],"highlight":{"on":"plotly_click","persistent":false,"dynamic":false,"selectize":false,"opacityDim":0.20000000000000001,"selected":{"opacity":1},"debounce":0},"shinyEvents":["plotly_hover","plotly_click","plotly_selected","plotly_relayout","plotly_brushed","plotly_brushing","plotly_clickannotation","plotly_doubleclick","plotly_deselect","plotly_afterplot","plotly_sunburstclick"],"base_url":"https://plot.ly"},"evals":[],"jsHooks":[]}</script>
```

*Question 2:*
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
points(D_point_seg, pch=16)
box()
```

<img src="04-RReproducible_files/figure-html/answer2-1.png" width="672" />

## Posters and Slides

Posters and presentations are another important type of scientific document. R markdown is good at creating both of these, and actually *very* good with some additional packages. So we will also use [flexdashboard](https://pkgs.rstudio.com/flexdashboard/) for posters and [beamer]( https://bookdown.org/yihui/rmarkdown/beamer-presentation.html) for presentations. 

**Poster**

See [DataScientism_Poster.html](https://jadamso.github.io/Rbooks/Templates/DataScientism_Poster.html) and recreate from the source file [DataScientism_Poster.Rmd](https://jadamso.github.io/Rbooks/Templates/DataScientism_Poster.Rmd). Simply change the name to your own, and knit the document.

**Slides**

See [DataScientism_Slides.pdf](https://jadamso.github.io/Rbooks/Templates/DataScientism_Slides.pdf)

Since beamer is a pdf output, you will need to install [Latex](https://tug.org/texlive/). Alternatively, you can install a lightweight version [TinyTex](https://yihui.org/tinytex/) from within R

```r
install.packages('tinytex')
tinytex::install_tinytex()  # install TinyTeX
```

Then download source file [DataScientism_Slides.Rmd](https://jadamso.github.io/Rbooks/Templates/DataScientism_Slides.Rmd), change the name to your own, and knit the document.

If you cannot install *Latex*, then you must specify a different output. For example, change `output: beamer_presentation` to `output: ioslides_presentation` on line 6 of the source file.


## More Literature

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


Some other good packages for posters/presenting you should be aware of

* https://github.com/mathematicalcoffee/beamerposter-rmarkdown-example
* https://github.com/rstudio/pagedown
* https://github.com/brentthorne/posterdown
* https://odeleongt.github.io/postr/
* https://wytham.rbind.io/post/making-a-poster-in-r/
* https://www.animateyour.science/post/How-to-design-an-award-winning-conference-poster




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


There are two main meta-files

* `README.txt` overviews the project structure and what the codes are doing
* `MAKEFILE` explicitly describes and executes all codes. 

## MAKEFILE

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
##           used (Mb) gc trigger (Mb) max used  (Mb)
## Ncells 1217529 65.1    2283195  122  2283195 122.0
## Vcells 2305178 17.6    8388608   64  3287591  25.1
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
<div class="profvis html-widget html-fill-item" id="htmlwidget-2472ba0fe4a912b3d014" style="width:100%;height:600px;"></div>
<script type="application/json" data-for="htmlwidget-2472ba0fe4a912b3d014">{"x":{"message":{"prof":{"time":[1,2,3,4,5,6,7,8,9,9,10,10,11,11,12,12,13,13,14,14,15,15,16,16,17,17,18,18,19,19,20,20,21,21,22,23,24,24,24,25,26,26,26,27,28,28,29,29,30,31,32,32,33,33,34,34,35,35,35,36,36,37,38,38,39,39,40,41,42,42,43,43,44,44,45,45,46,46,46,47,48,49,49,49,50,50,51,51,52,52,53,53,53,54,54,54,55,55,55,56,56,57,57,57,58,59,59,60,61,62,62,62,63,63,64,64,65,65,66,66,67,67,68,68,69,69,70,70,70,71,71,72,73,73,74,75,75,76,76,77,77,78,78,79,79,80,80,81,81,81,82,83,84,84,84,85,85,85,86,86,87,87,87,88,88,89,89,90,90,90,91,91,92,92,93,93,94,95,95,96,96,97,98,98,99,99,99,100,100,101,101,102,103,103,103,104,105,106,106,107,108,109,109,110,110,111,111,111,112,113,113,114,114,115,116,117,117,118,118,119,119,119,120,120,120,121,122,123,124,125,125,126,126,126,127,128,129,129,130,130,131,132,133,134,134,135,135,135,136,136,137,137,138,138,139,140,140,141,142,142,142,143,143,144,144,144,145,145,146,146,147,148,148,149,149,149,150,150,150,151,151,152,153,154,154,155,156,156,157,157,157,158,158,159,159,159,160,161,161,162,162,163,163,164,164,164,165,166,166,166,167,168,168,169,170,170,171,172,172,172,173,173,174,174,175,176,176,177,177,178,179,179,180,181,181,182,182,182,183,184,185,185,185,186,186,186,186,187,187,187,187,188,188,188,188,189,189,189,189,190,190,190,190,191,191,191,191,192,192,192,192,193,193,193,193,194,195,195,196,197,197,198,199,199,200,200,201,201,202,203,203,203,204,205,206,206,207,207,207,208,208,209,209,210,211,211,211,212,212,213,213,214,214,214,215,216,216,217,218,218,219,219,220,220,221,221,222,223,223,223,224,224,225,225,226,226,227,227,228,228,229,230,230,230,231,231,232,232,233,234,235,236,237,237,237,238,239,240,240,241,241,242,243,244,244,244,245,246,247,247,248,248,249,249,250,250,250,251,251,252,252,253,254,255,256,257,257,257,258,258,258,258,259,260,260,261,262,262,263,264,265,265,265,265,266,266,267,267,267,268,268,269,269,269,270,270,271,271,272,272,272,273,273,274,274,275,275,276,276,277,277,278,278,278,279,279,280,280,281,282,283,284,284,285,285,285,286,286,287,288,289,289,290,291,291,291,292,292,293,293,293,294,295,296,296,296,297,297,297,298,298,299,299,299,300,301,301,302,302,303,303,304,304,305,305,306,306,307,308,309,309,309,310,310,310,311,311,312,312,313,313,314,314,314,315,315,316,316,317,317,318,318,319,320,320,321,322,322,322,323,323,324,325,325,326,326,327,327,328,328,328,329,329,330,330,331,331,332,332,333,333,334,334,335,335,336,336,337,337,338,338,339,339,340,340,341,341,342,342,343,343,344,344,345,345,346,346,347,347,348,348,349,349,350,350,351,351,352,352,353,353,354,354,355,355,356,356,357,357,358,358,359,359,360,361,361,362,363,363,364,364,364,365,365,366,367,368,368,368,369,369,370,370,371,371,372,373,373,373,374,374,374,375,376,376,377,378,378,379,379,379,380,380,381,382,383,384,384,384,385,385,386,386,387,387,388,388,389,389,390,391,391,392,393,394,394,395,396,396,397,397,397,398,398,398,399,399,400,400,401,401,402,402,403,403,403,404,405,405,406,406,407,408,408,408,409,410,410,411,411,412,413,413,414,414,415,415,415,416,416,416,417,418,419,420,421,421,422,422,423,424,424,425,426,427,428,429,429,429,430,430,431,431,432,432,433,433,433,434,434,435,435,436,436,437,438,438,439,439,439,440,440,441,442,442,443,444,444,444,445,445,445,446,447,448,448,449,449,450,450,450,451,452,453,453,454,454,455,455,456,457,457,458,459,459,459,460,460,461,462,462,463,464,465,465,466,466,467,467,468,468,468,469,469,470,470,471,471,472,472,472,473,473,474,474,475,475,476,477,477,478,478,479,479,480,481,481,482,482,483,483,484,484,485,485,485,486,486,486,487,488,489,490,491,491,491,492,492,492,493,493,494,494,495,495,496,496,497,497,498,498,498,498,499,499,499,499,500,500,501,502,502,503,503,504,504,505,505,506,507,507,508,508,509,509,510,510,511,511,511,512,512,512,513,513,514,514,515,515,516,517,517,518,518,519,519,520,520,521,522,523,523,524,524,525,525,525,526,526,527,527,528,528,529,530,530,531,532,532,533,534,534,535,536,537,537,538,538,538,539,540,540,541,542,543,544,545,545,546,547,547,548,548,549,550,550,551,551,551,552,552,553,553,554,554,555,556,556,557,558,558,559,559,559,560,560,561,561,562,562,563,563,563,563,564,564,565,566,567,567,568,568,569,569,570,571,571,572,572,573,573,574,574,575,575,576,576,577,578,578,579,580,580,581,581,582,583,584,584,584,585,585,586,586,586,587,588,588,589,589,589,590,591,592,592,592,593,593,593,594,594,595,596,597,598,599,599,600,600,601,601,602,603,603,604,604,604,605,606,607,607,608,608,609,609,610,610,611,611,612,612,612,613,613,614,614,615,616,616,617,617,618,619,619,620,620,621,621,622,622,623,623,624,624,625,625,626,627,627,628,628,629,629,629,630,630,631,631,632,632,633,633,634,635,635,636,636,637,637,638,638,639,639,640,640,641,641,642,642,643,643,644,644,645,645,646,646,647,647,648,648,649,650,651,651,652,652,653,654,655,655,656,657,657,657,658,659,659,660,660,661,662,662,662,663,664,664,665,665,666,667,667,668,668,669,669,670,670,671,671,671,672,672,672,673,673,674,675,675,676,677,678,678,679,679,680,681,681,682,683,683,684,684,684,685,685,685,686,686,687,687,687,688,688,689,690,691,691,692,693,693,694,694,695,696,697,697,698,699,700,700,701,702,702,703,703,704,705,705,705,706,706,706,707,707,708,709,710,710,711,711,712,712,713,713,714,714,715,716,716,716,717,717,717,718,718,719,720,720,721,721,722,722,723,723,724,724,725,725,726,727,727,727,728,728,728,729,729,730,731,731,732,733,733,733,734,734,735,735,736,736,737,737,738,738,739,739,740,740,741,741,742,743,743,744,745,745,746,746,747,747,748,749,749,749,750,750,751,751,752,752,753,753,754,754,755,756,756,757,758,758,759,759,759,760,760,760,761,761,762,762,763,763,764,764,765,766,766,767,767,768,768,769,769,770,770,770,771,771,772,773,773,774,775,775,776,776,777,777,778,778,779,779,780,780,780,781,781,781,782,783,783,784,785,785,786,787,787,787,788,789,789,790,790,791,791,791,792,793,793,794,794,795,796,796,797,798,798,798,799,799,800,800,801,801,801,802,802,803,803,804,804,805,805,806,806,806,807,807,808,808,809,810,811,811,812,813,814,815,815,816,816,817,817,818,818,818,819,820,821,821,821,822,822,822,823,823,823,824,825,826,826,827,827,828,828,828,829,830,830,831,831,831,832,832,832,833,833,834,835,835,836,836,837,837,837,838,838,839,839,840,840,841,841,841,841,842,843,843,844,844,845,846,847,847,848,848,849,849,850,850,851,851,852,852,853,854,854,855,856,856,857,857,858,859,859,860,860,861,861,862,863,863,863,864,865,865,866,866,867,868,869,869,870,870,870,871,871,871,872,872,872,873,873,873,874,874,874,875,875,875,876,876,876,877,877,877,878,878,878,879,879,880,880,881,881,882,883,883,884,884,885,886,886,887,888,888,889,889,890,890,890,891,891,892,893,894,894,895,895,896,897,897,898,898,899,899,900,900,901,901,902,902,903,904,904,905,905,906,907,907,907,908,908,909,909,910,910,911,911,911,912,913,913,914,914,915,915,915,916,916,917,918,918,919,920,921,921,922,922,923,923,924,924,925,925,925,926,926,927,927,927,928,928,929,929,930,930,931,931,932,933,933,934,934,934,935,935,936,937,938,938,939,940,941,941,942,943,943,944,945,945,946,946,947,947,948,948,949,949,950,951,951,951,952,952,952,953,954,955,955,956,956,957,958,958,959,960,960,960,961,961,961,962,962,963,964,964,964,965,966,967,968,968,969,969,969,970,970,970,971,971,972,972,973,973,974,975,975,976,976,977,977,977,978,978,978,979,979,980,981,981,982,982,983,983,984,984,985,986,986,986,987,987,987,988,988,989,990,990,991,991,992,993,993,994,995,995,995,996,996,996,997,998,999,999,1000,1000,1001,1002,1002,1003,1003,1004,1004,1004,1005,1005,1006,1006,1007,1008,1008,1009,1010,1011,1011,1012,1012,1012,1013,1013,1013,1014,1014,1014,1015,1015,1015,1016,1016,1016,1017,1017,1017,1018,1018,1019,1020,1021,1021,1022,1022,1023,1023,1024,1025,1025,1025,1026,1026,1026,1027,1027,1027,1028,1028,1028,1029,1029,1029,1030,1030,1030,1031,1031,1031,1032,1032,1032,1033,1033,1033,1034,1034,1034,1035,1035,1035,1036,1036,1036,1037,1037,1037,1038,1038,1038,1039,1039,1039,1040,1040,1040,1041,1041,1041,1042,1042,1042,1043,1043,1043,1044,1044,1044,1045,1045,1045,1046,1046,1046,1047,1047,1047,1048,1048,1048,1049,1049,1049,1050,1050,1050,1051,1051,1051,1052,1052,1052,1053,1053,1053,1054,1054,1054,1055,1055,1055,1056,1056,1056,1057,1057,1057,1058,1058,1058,1059,1059,1059,1060,1060,1060,1061,1061,1061,1062,1062,1062,1063,1063,1063,1064,1064,1064,1065,1065,1065,1066,1066,1066,1067,1067,1067,1068,1068,1068,1069,1069,1069,1070,1070,1070,1071,1071,1071,1072,1072,1072,1073,1073,1073,1074,1074,1074,1075,1076,1077,1078,1078,1078,1079,1079,1080,1080,1081,1081,1082,1083,1083,1084,1085,1086,1086,1087,1087,1088,1088,1089,1089,1090,1091,1092,1093,1094,1095,1095,1096,1096,1097,1097,1098,1098,1098,1099,1099,1099,1100,1101,1102,1102,1103,1104,1105,1105,1106,1107,1107,1108,1109,1109,1110,1110,1111,1112,1113,1114,1115,1115,1115,1116,1116,1117,1117,1118,1119,1120,1120,1120,1121,1121,1121,1122,1122,1123,1124,1124,1124,1125,1125,1126,1126,1127,1127,1127,1128,1128,1129,1130,1130,1130,1131,1131,1132,1133,1133,1134,1134,1135,1136,1136,1137,1138,1138,1139,1140,1141,1142,1142,1142,1143,1143,1143,1144,1144,1145,1146,1146,1147,1148,1149,1150,1151,1151,1152,1153,1153,1154,1154,1155,1155,1156,1157,1158,1158,1159,1159,1160,1160,1161,1161,1162,1163,1163,1164,1164,1165,1165,1166,1166,1167,1167,1168,1168,1169,1169,1170,1170,1171,1172,1172,1173,1173,1174,1174,1175,1175,1176,1176,1177,1178,1178,1178,1179,1180,1180,1181,1181,1182,1182,1183,1183,1184,1184,1185,1186,1186,1187,1187,1188,1189,1190,1190,1191,1191,1192,1192,1193,1193,1194,1195,1196,1197,1197,1198,1198,1199,1199,1200,1201,1202,1202,1202,1203,1204,1204,1205,1206,1207,1207,1208,1208,1209,1209,1210,1211,1211,1212,1213,1213,1214,1214,1215,1216,1217,1218,1218,1218,1219,1220,1220,1220,1221,1221,1222,1222,1223,1223,1224,1225,1225,1226,1226,1227,1227,1228,1228,1229,1229,1230,1230,1231,1231,1232,1232,1233,1233,1234,1234,1235,1235,1236,1236,1237,1237,1238,1238,1239,1240,1240,1240,1241,1242,1242,1243,1243,1244,1244,1245,1245,1245,1246,1247,1248,1248,1249,1249,1250,1251,1251,1252,1252,1253,1253,1254,1254,1254,1255,1255,1255,1256,1256,1257,1258,1258,1258,1259,1259,1259,1260,1261,1261,1262,1263,1263,1264,1264,1264,1265,1265,1266,1266,1267,1267,1268,1269,1270,1271,1271,1272,1272,1273,1273,1274,1274,1275,1275,1276,1276,1277,1277,1278,1278,1279,1279,1280,1280,1281,1282,1282,1283,1283,1284,1285,1286,1287,1287,1288,1289,1289,1289,1290,1290,1291,1291,1292,1293,1293,1294,1294,1295,1295,1296,1297,1297,1298,1298,1299,1300,1300,1300,1301,1301,1301,1302,1302,1302,1303,1303,1304,1305,1305,1306,1307,1307,1308,1309,1309,1310,1311,1311,1312,1312,1312,1313,1313,1314,1315,1315,1316,1316,1316,1317,1317,1318,1318,1319,1319,1320,1320,1321,1321,1322,1322,1323,1323,1324,1324,1325,1325,1326,1326,1327,1327,1328,1329,1329,1330,1330,1331,1331,1332,1332,1333,1333,1334,1334,1335,1335,1336,1336,1337,1337,1338,1338,1339,1339,1340,1340,1341,1341,1342,1342,1343,1343,1344,1344,1345,1345,1346,1346,1347,1347,1348,1348,1348,1348,1348,1348,1348,1348,1348,1349,1349,1349,1349,1349,1349,1349,1349,1350,1350,1350,1350,1350,1350,1350,1350,1351,1351,1351,1351,1351,1351,1351,1351,1352,1352,1352,1352,1352,1352,1352,1352,1353,1353,1353,1353,1353,1353,1353,1353,1354,1354,1354,1354,1354,1354,1354,1354,1355,1355,1355,1355,1355,1355,1355,1355,1356,1356,1356,1356,1356,1356,1356,1356,1357,1357,1357,1357,1357,1357,1357,1357,1358,1358,1358,1358,1358,1358,1358,1358,1359,1359,1359,1359,1359,1359,1359,1359,1360,1360,1360,1360,1360,1360,1360,1360,1361,1361,1361,1361,1361,1361,1361,1361,1362,1362,1362,1362,1362,1362,1362,1362,1363,1363,1363,1363,1363,1363,1363,1363,1364,1364,1364,1364,1364,1364,1364,1364,1365,1365,1365,1365,1365,1365,1365,1365,1366,1366,1366,1366,1366,1366,1366,1366,1367,1367,1367,1367,1367,1367,1367,1367],"depth":[1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,3,2,1,1,3,2,1,1,2,1,2,1,1,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,3,2,1,1,1,3,2,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,3,2,1,1,2,1,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,1,3,2,1,3,2,1,2,1,3,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,3,2,1,2,1,2,1,1,3,2,1,1,1,2,1,1,1,2,1,2,1,3,2,1,1,2,1,2,1,1,1,2,1,2,1,3,2,1,3,2,1,1,1,1,1,2,1,3,2,1,1,1,2,1,2,1,1,1,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,1,3,2,1,2,1,3,2,1,2,1,2,1,1,2,1,3,2,1,3,2,1,2,1,1,1,2,1,1,2,1,3,2,1,2,1,3,2,1,1,2,1,2,1,2,1,3,2,1,1,3,2,1,1,2,1,1,2,1,1,3,2,1,2,1,2,1,1,2,1,2,1,1,2,1,1,2,1,3,2,1,1,1,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,1,2,1,1,2,1,1,2,1,2,1,2,1,1,3,2,1,1,1,2,1,3,2,1,2,1,2,1,1,3,2,1,2,1,2,1,3,2,1,1,2,1,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,1,1,1,1,3,2,1,1,1,2,1,2,1,1,1,3,2,1,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,1,1,1,3,2,1,4,3,2,1,1,2,1,1,2,1,1,1,4,3,2,1,2,1,3,2,1,2,1,3,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,1,1,2,1,3,2,1,2,1,1,1,2,1,1,3,2,1,2,1,3,2,1,1,1,3,2,1,3,2,1,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,3,2,1,3,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,1,3,2,1,2,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,3,2,1,2,1,1,1,3,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,1,2,1,1,2,1,3,2,1,2,1,1,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,1,2,1,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,1,3,2,1,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,1,1,1,1,2,1,2,1,1,2,1,1,1,1,1,3,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,3,2,1,2,1,1,2,1,1,3,2,1,3,2,1,1,1,2,1,2,1,3,2,1,1,1,2,1,2,1,2,1,1,2,1,1,3,2,1,2,1,1,2,1,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,1,1,1,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,4,3,2,1,4,3,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,1,2,1,1,2,1,1,1,2,1,3,2,1,1,2,1,1,1,1,1,2,1,1,2,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,4,3,2,1,2,1,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,1,1,3,2,1,2,1,3,2,1,1,2,1,3,2,1,1,1,3,2,1,3,2,1,2,1,1,1,1,1,2,1,2,1,2,1,1,2,1,3,2,1,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,1,1,2,1,1,3,2,1,1,2,1,2,1,1,3,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,1,2,1,1,1,2,1,2,1,1,2,1,1,2,1,3,2,1,3,2,1,2,1,3,2,1,2,1,1,1,2,1,1,2,1,2,1,1,1,2,1,1,1,2,1,1,2,1,2,1,1,3,2,1,3,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,2,1,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,1,2,1,1,2,1,1,3,2,1,1,2,1,2,1,3,2,1,1,2,1,2,1,1,2,1,1,3,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,1,2,1,1,1,1,2,1,2,1,2,1,3,2,1,1,1,3,2,1,3,2,1,3,2,1,1,1,2,1,2,1,3,2,1,1,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,4,3,2,1,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,1,3,2,1,1,2,1,2,1,1,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,1,2,1,2,1,3,2,1,2,1,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,3,2,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,3,2,1,2,1,1,2,1,1,1,2,1,2,1,2,1,2,1,3,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,2,1,1,1,2,1,1,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,1,1,2,1,2,1,1,2,1,1,3,2,1,3,2,1,2,1,1,3,2,1,1,1,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,2,1,1,2,1,2,1,1,2,1,1,3,2,1,3,2,1,1,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,1,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,1,1,2,1,2,1,2,1,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,1,1,1,3,2,1,2,1,2,1,2,1,1,2,1,1,1,2,1,2,1,2,1,2,1,1,1,1,1,1,2,1,2,1,2,1,3,2,1,3,2,1,1,1,2,1,1,1,2,1,1,2,1,1,2,1,2,1,1,1,1,1,3,2,1,2,1,2,1,1,1,3,2,1,3,2,1,2,1,1,3,2,1,2,1,2,1,3,2,1,2,1,1,3,2,1,2,1,1,2,1,2,1,1,2,1,1,2,1,1,1,1,3,2,1,3,2,1,2,1,1,2,1,1,1,1,1,2,1,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,1,1,1,2,1,2,1,2,1,1,1,3,2,1,1,2,1,1,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,1,1,1,3,2,1,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,1,2,1,2,1,2,1,3,2,1,1,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,1,3,2,1,3,2,1,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,1,1,2,1,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,1,3,2,1,3,2,1,3,2,1,2,1,1,2,1,1,2,1,1,2,1,1,2,1,3,2,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,9,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1],"label":["rowSums","rowSums","rowSums","rowSums","rowMeans","rowMeans","rowMeans","rowMeans","aperm.default","apply","aperm.default","apply","aperm.default","apply","aperm.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","mean.default","apply","apply","apply","isTRUE","mean.default","apply","apply","isTRUE","mean.default","apply","apply","mean.default","apply","FUN","apply","apply","apply","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","apply","<GC>","apply","FUN","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","is.numeric","local","<GC>","FUN","apply","apply","apply","isTRUE","mean.default","apply","length","local","FUN","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","length","local","isTRUE","mean.default","apply","apply","mean.default","apply","apply","apply","<GC>","FUN","apply","FUN","apply","is.na","local","is.numeric","local","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","apply","length","local","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","length","local","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","<GC>","apply","mean.default","apply","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","apply","<GC>","length","local","apply","apply","mean.default","apply","apply","apply","mean.default","apply","FUN","apply","<GC>","mean.default","apply","apply","mean.default","apply","mean.default","apply","apply","apply","mean.default","apply","FUN","apply","<GC>","mean.default","apply","isTRUE","mean.default","apply","apply","apply","apply","apply","FUN","apply","<GC>","FUN","apply","apply","apply","FUN","apply","FUN","apply","apply","apply","apply","<GC>","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","mean.default","apply","apply","<GC>","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","apply","FUN","apply","<GC>","mean.default","apply","isTRUE","mean.default","apply","length","local","apply","apply","FUN","apply","apply","mean.default","apply","<GC>","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","<GC>","FUN","apply","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","FUN","apply","apply","<GC>","mean.default","apply","mean.default","apply","is.na","local","apply","mean.default","apply","FUN","apply","apply","<GC>","apply","apply","length","local","isTRUE","mean.default","apply","apply","apply","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","apply","mean.default","apply","apply","length","local","apply","FUN","apply","mean.default","apply","<GC>","apply","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","apply","mean.default","apply","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","apply","<GC>","FUN","apply","mean.default","apply","FUN","apply","apply","apply","apply","apply","<GC>","FUN","apply","apply","apply","is.numeric","local","is.na","local","apply","apply","<GC>","FUN","apply","apply","apply","FUN","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","apply","FUN","apply","apply","apply","apply","apply","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","apply","mean.default","apply","apply","FUN","apply","apply","apply","<GC>","isTRUE","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","apply","apply","apply","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","apply","mean.default","apply","apply","<GC>","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","mean.default","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","<GC>","length","local","mean.default","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","apply","mean.default","apply","length","local","apply","mean.default","apply","apply","<GC>","mean.default","apply","FUN","apply","apply","mean.default","apply","FUN","apply","FUN","apply","<GC>","length","local","length","local","FUN","apply","length","local","FUN","apply","length","local","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","mean.default","apply","FUN","apply","apply","is.na","local","apply","FUN","apply","isTRUE","mean.default","apply","is.na","local","apply","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","<GC>","apply","<GC>","apply","mean.default","apply","apply","FUN","apply","apply","apply","mean.default","apply","apply","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","is.numeric","local","<GC>","apply","<GC>","apply","isTRUE","mean.default","apply","apply","mean.default","apply","mean.default","apply","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","is.na","local","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","apply","apply","apply","FUN","apply","is.na","local","apply","mean.default","apply","apply","apply","apply","apply","<GC>","length","local","FUN","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","mean.default","apply","apply","isTRUE","mean.default","apply","<GC>","mean.default","apply","apply","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","apply","apply","mean.default","apply","FUN","apply","is.numeric","local","apply","FUN","apply","apply","<GC>","mean.default","apply","FUN","apply","apply","length","local","apply","apply","is.numeric","local","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","is.na","local","<GC>","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","is.na","local","apply","is.numeric","local","FUN","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","apply","apply","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","length","local","mean.default","apply","length","local","mean.default","apply","FUN","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","mean.default","apply","apply","length","local","FUN","apply","mean.default","apply","FUN","apply","apply","is.numeric","local","mean.default","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","mean.default","apply","mean.default","apply","length","local","apply","FUN","apply","apply","FUN","apply","apply","mean.default","apply","apply","apply","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","apply","apply","apply","apply","FUN","apply","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","<GC>","length","local","FUN","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","<GC>","isTRUE","mean.default","apply","is.na","local","apply","apply","mean.default","apply","FUN","apply","FUN","apply","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","apply","<GC>","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","<GC>","apply","isTRUE","mean.default","apply","apply","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","apply","apply","FUN","apply","<GC>","apply","mean.default","apply","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","length","local","mean.default","apply","is.numeric","local","FUN","apply","mean.default","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","mean.default","apply","FUN","apply","length","local","FUN","apply","<GC>","apply","length","local","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","apply","apply","FUN","apply","FUN","apply","apply","apply","mean.default","apply","apply","isTRUE","mean.default","apply","apply","FUN","apply","<GC>","apply","apply","isTRUE","mean.default","apply","apply","FUN","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","<GC>","length","local","<GC>","length","local","FUN","apply","apply","FUN","apply","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","<GC>","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","length","local","isTRUE","mean.default","apply","FUN","apply","apply","apply","FUN","apply","apply","mean.default","apply","<GC>","apply","apply","apply","FUN","apply","apply","apply","mean.default","apply","apply","FUN","apply","FUN","apply","apply","<GC>","is.numeric","local","<GC>","is.numeric","local","mean.default","apply","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","apply","<GC>","is.numeric","local","<GC>","is.numeric","local","FUN","apply","apply","mean.default","apply","length","local","mean.default","apply","FUN","apply","mean.default","apply","length","local","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","is.numeric","local","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","length","local","FUN","apply","mean.default","apply","apply","is.numeric","local","apply","FUN","apply","<GC>","length","local","<GC>","length","local","FUN","apply","is.na","local","mean.default","apply","FUN","apply","apply","length","local","FUN","apply","mean.default","apply","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","mean.default","apply","apply","is.na","local","FUN","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","mean.default","apply","apply","mean.default","apply","apply","isTRUE","mean.default","apply","apply","FUN","apply","mean.default","apply","<GC>","FUN","apply","apply","mean.default","apply","FUN","apply","apply","is.numeric","local","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","<GC>","FUN","apply","length","local","is.numeric","local","is.na","local","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","apply","apply","<GC>","apply","apply","apply","apply","FUN","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","is.numeric","local","FUN","apply","<GC>","isTRUE","mean.default","apply","apply","FUN","apply","is.na","local","apply","apply","mean.default","apply","mean.default","apply","is.numeric","local","<GC>","apply","<GC>","apply","FUN","apply","apply","FUN","apply","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","<GC>","apply","<GC>","apply","apply","isTRUE","mean.default","apply","apply","mean.default","apply","FUN","apply","apply","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","is.na","local","mean.default","apply","mean.default","apply","apply","FUN","apply","FUN","apply","apply","mean.default","apply","apply","<GC>","apply","<GC>","apply","isTRUE","mean.default","apply","mean.default","apply","apply","apply","FUN","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","FUN","apply","apply","<GC>","mean.default","apply","is.numeric","local","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","apply","length","local","FUN","apply","isTRUE","mean.default","apply","<GC>","apply","apply","mean.default","apply","apply","apply","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","<GC>","length","local","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","apply","mean.default","apply","apply","apply","FUN","apply","apply","<GC>","apply","apply","length","local","length","local","FUN","apply","FUN","apply","is.numeric","local","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","apply","mean.default","apply","mean.default","apply","apply","is.numeric","local","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","apply","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","is.na","local","mean.default","apply","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","apply","<GC>","is.numeric","local","<GC>","is.numeric","local","FUN","apply","apply","FUN","apply","mean.default","apply","apply","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","mean.default","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","apply","mean.default","apply","apply","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","length","local","mean.default","apply","apply","FUN","apply","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","apply","apply","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","apply","FUN","apply","apply","apply","FUN","apply","apply","FUN","apply","apply","is.numeric","local","FUN","apply","apply","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","FUN","apply","apply","apply","apply","<GC>","length","local","<GC>","length","local","mean.default","apply","apply","mean.default","apply","apply","apply","apply","apply","FUN","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","FUN","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","apply","<GC>","apply","<GC>","apply","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","length","local","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","apply","mean.default","apply","apply","apply","FUN","apply","<GC>","apply","<GC>","apply","apply","FUN","apply","apply","mean.default","apply","FUN","apply","apply","apply","apply","isTRUE","mean.default","apply","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","is.numeric","local","FUN","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","apply","isTRUE","mean.default","apply","apply","FUN","apply","mean.default","apply","length","local","isTRUE","mean.default","apply","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","is.numeric","local","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","is.numeric","local","FUN","apply","apply","apply","apply","FUN","apply","mean.default","apply","FUN","apply","length","local","FUN","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","apply","<GC>","apply","apply","FUN","apply","length","local","apply","apply","apply","FUN","apply","apply","isTRUE","mean.default","apply","is.na","local","FUN","apply","apply","is.numeric","local","mean.default","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","apply","FUN","apply","apply","mean.default","apply","apply","FUN","apply","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","%in%","findLocals1","FUN","lapply","findLocalsList1","findLocalsList","findLocals","compile","compiler:::tryCompile","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis"],"filenum":[1,1,1,1,1,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,1,null,null,1,1,null,null,1,1,null,1,null,1,1,1,null,1,null,1,null,1,null,null,1,null,1,1,null,1,null,1,1,1,null,1,null,1,null,1,null,null,null,null,1,1,1,null,null,1,null,null,null,1,null,1,null,null,1,null,null,1,null,null,1,null,null,null,null,1,1,null,1,1,1,null,null,1,null,1,null,null,null,null,null,1,null,1,null,1,null,1,null,null,1,null,1,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,1,1,null,null,1,null,null,1,null,1,null,null,1,null,null,null,1,null,null,1,null,1,null,1,null,1,1,null,1,null,1,1,null,1,null,null,1,null,1,null,1,1,null,null,null,1,1,null,1,1,1,null,1,null,1,null,null,1,1,null,1,null,1,1,1,null,1,null,1,null,null,1,null,null,1,1,1,1,1,null,1,null,null,1,1,1,null,1,null,1,1,1,1,null,1,null,null,1,null,1,null,1,null,1,1,null,1,1,null,null,1,null,1,null,null,1,null,1,null,1,1,null,1,null,null,1,null,null,1,null,null,1,1,null,1,1,null,1,null,null,1,null,1,null,null,1,1,null,1,null,1,null,1,null,null,1,1,null,null,1,1,null,1,1,null,1,1,null,null,1,null,1,null,null,1,null,1,null,1,1,null,1,1,null,null,null,null,1,1,1,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,1,null,1,1,null,null,1,null,1,null,1,null,1,1,null,null,1,1,1,null,1,null,null,1,null,1,null,1,1,null,null,1,null,1,null,1,null,null,1,1,null,1,1,null,1,null,1,null,1,null,1,1,null,null,1,null,1,null,1,null,1,null,1,null,1,1,null,null,1,null,1,null,1,1,1,1,1,null,null,1,1,1,null,null,null,null,1,1,null,null,1,1,1,null,1,null,1,null,1,null,null,1,null,1,null,1,1,1,1,1,null,null,1,null,null,null,1,1,null,1,1,null,1,1,1,null,null,null,1,null,1,null,null,1,null,1,null,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,1,1,1,null,1,null,null,1,null,1,1,1,null,1,1,null,null,1,null,1,null,null,1,1,1,null,null,1,null,null,1,null,1,null,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,1,1,null,null,1,null,null,null,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,null,1,null,1,1,null,null,1,null,1,1,null,1,null,1,null,1,null,null,null,null,null,null,1,null,null,null,1,null,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,null,1,null,1,null,null,1,null,null,1,1,null,null,1,null,1,null,1,null,1,1,null,null,1,null,null,1,1,null,1,1,null,1,null,null,1,null,1,1,1,1,null,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,1,1,null,1,1,null,1,null,null,1,null,null,1,null,1,null,null,null,1,null,1,null,null,1,1,null,1,null,1,1,null,null,1,1,null,1,null,1,1,null,1,null,null,null,null,1,null,null,1,1,1,1,1,null,1,null,null,1,null,1,1,1,1,1,null,null,null,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,1,null,1,null,null,1,null,1,1,null,1,1,null,null,1,null,null,1,1,1,null,1,null,1,null,null,1,1,1,null,1,null,1,null,null,1,null,1,1,null,null,1,null,1,1,null,null,1,1,null,null,null,1,null,1,null,null,1,null,1,null,1,null,null,null,null,1,null,1,null,1,null,1,1,null,1,null,1,null,null,1,null,null,null,1,null,1,null,1,null,null,1,null,null,1,1,1,1,1,null,null,1,null,null,1,null,null,null,1,null,null,null,1,null,1,null,null,null,1,null,null,null,1,null,1,1,null,null,null,1,null,1,null,1,1,null,null,null,1,null,1,null,1,null,null,1,null,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,1,1,null,1,null,1,null,null,1,null,1,null,1,null,null,1,null,1,1,null,1,1,null,1,1,1,null,1,null,null,1,1,null,1,1,1,1,1,null,1,1,null,1,null,1,1,null,1,null,null,null,null,1,null,1,null,1,1,null,1,1,null,1,null,null,1,null,1,null,1,null,1,null,null,null,1,null,null,1,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,1,null,1,null,1,1,1,null,null,1,null,1,null,null,1,1,null,1,null,null,1,1,1,null,null,1,null,null,1,null,1,1,1,1,1,null,1,null,1,null,1,1,null,1,null,null,1,1,1,null,null,null,1,null,null,null,1,null,1,null,null,1,null,1,null,1,1,null,1,null,1,1,null,1,null,1,null,1,null,null,null,1,null,1,null,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,1,null,1,null,1,1,1,null,1,1,null,null,1,1,null,1,null,1,1,null,null,1,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,null,null,null,null,null,null,1,1,null,1,1,1,null,1,null,1,1,null,1,1,null,1,null,null,1,null,null,1,null,null,null,null,1,null,1,1,1,null,1,1,null,1,null,1,1,1,null,1,1,1,null,1,1,null,1,null,1,1,null,null,null,null,null,null,null,1,1,1,null,1,null,1,null,1,null,1,null,1,1,null,null,null,null,null,null,null,1,1,null,1,null,null,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,1,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,1,null,1,null,1,null,1,1,null,null,1,null,1,null,1,null,null,null,1,null,1,1,null,null,1,null,1,null,null,null,null,null,null,null,1,null,null,null,1,null,1,1,null,null,null,1,null,1,null,1,null,null,1,null,1,1,null,1,1,null,null,null,1,null,1,null,1,null,1,null,null,1,null,null,1,1,null,1,1,null,1,1,null,null,1,1,null,1,null,1,null,null,1,1,null,1,null,1,1,null,null,1,null,null,1,null,1,null,1,null,null,1,null,null,null,null,null,null,null,1,null,null,1,null,1,null,1,1,1,null,1,1,1,1,null,1,null,1,null,1,null,null,1,1,1,null,null,1,null,null,1,null,null,1,1,1,null,1,null,1,null,null,1,1,null,1,null,null,1,null,null,1,null,1,1,null,1,null,1,null,null,1,null,1,null,null,null,1,null,null,null,1,1,null,1,null,null,1,1,null,1,null,1,null,null,null,1,null,1,null,1,1,null,1,1,null,1,null,1,1,null,1,null,1,null,1,1,null,null,1,1,null,1,null,1,1,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,null,1,null,1,1,null,1,null,1,1,null,1,1,null,1,null,1,null,null,1,null,1,1,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,1,null,null,1,null,null,null,1,null,1,null,null,1,1,null,null,null,1,null,null,1,null,1,1,null,1,1,1,null,1,null,1,null,1,null,1,null,null,null,null,1,null,null,1,null,1,null,1,null,1,null,1,1,null,1,null,null,1,null,1,1,1,null,1,1,1,null,1,1,null,1,1,null,null,null,null,null,1,null,1,null,null,1,null,null,1,null,null,1,1,1,null,1,null,1,1,null,null,1,null,null,1,null,null,1,null,1,1,null,null,1,1,1,1,null,1,null,null,1,null,null,1,null,1,null,null,null,1,1,null,1,null,1,null,null,1,null,null,1,null,1,1,null,1,null,1,null,1,null,1,1,null,null,null,null,null,null,null,1,1,null,1,null,1,1,null,1,1,null,null,1,null,null,1,1,1,null,1,null,1,1,null,1,null,1,null,null,1,null,1,null,1,1,null,1,1,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,1,1,null,1,null,1,null,1,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,1,1,1,null,null,1,null,1,null,null,null,1,1,null,1,1,1,null,1,null,1,null,1,null,1,1,1,1,1,1,null,1,null,1,null,1,null,null,1,null,null,1,1,1,null,1,1,1,null,1,1,null,1,1,null,null,null,1,1,1,1,1,null,null,1,null,1,null,1,1,1,null,null,1,null,null,1,null,1,1,null,null,1,null,1,null,1,null,null,1,null,1,1,null,null,1,null,1,1,null,1,null,1,1,null,1,1,null,1,1,1,1,null,null,null,null,null,null,null,1,1,null,1,1,1,1,1,null,1,1,null,1,null,1,null,1,1,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,1,null,null,1,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,1,1,null,1,null,1,null,1,null,null,1,1,1,null,1,null,1,null,1,1,1,null,null,1,1,null,1,1,1,null,1,null,1,null,1,1,null,1,1,null,1,null,1,1,1,1,null,null,1,1,null,null,1,null,1,null,1,null,1,1,null,1,null,1,null,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,null,1,1,null,1,null,1,null,null,null,null,1,1,1,null,1,null,1,1,null,1,null,null,null,1,null,null,1,null,null,1,null,1,1,null,null,1,null,null,1,1,null,1,1,null,1,null,null,1,null,1,null,null,null,1,1,1,1,null,1,null,1,null,1,null,null,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,null,1,1,1,null,1,1,null,null,1,null,null,null,1,1,null,null,null,1,null,1,1,null,1,null,1,1,null,null,1,null,null,1,null,null,1,null,1,1,null,1,1,null,1,1,null,1,1,null,1,null,null,1,null,1,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,null,null,null,null,null,null,1,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null],"linenum":[10,10,10,10,11,11,11,11,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,12,null,null,12,12,null,null,12,12,null,12,null,12,12,12,null,12,null,12,null,12,null,null,12,null,12,12,null,12,null,12,12,12,null,12,null,12,null,12,null,null,null,null,12,12,12,null,null,12,null,null,null,12,null,12,null,null,12,null,null,12,null,null,12,null,null,null,null,12,12,null,12,12,12,null,null,12,null,12,null,null,null,null,null,12,null,12,null,12,null,12,null,null,12,null,12,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,12,12,null,null,12,null,null,12,null,12,null,null,12,null,null,null,12,null,null,12,null,12,null,12,null,12,12,null,12,null,12,12,null,12,null,null,12,null,12,null,12,12,null,null,null,12,12,null,12,12,12,null,12,null,12,null,null,12,12,null,12,null,12,12,12,null,12,null,12,null,null,12,null,null,12,12,12,12,12,null,12,null,null,12,12,12,null,12,null,12,12,12,12,null,12,null,null,12,null,12,null,12,null,12,12,null,12,12,null,null,12,null,12,null,null,12,null,12,null,12,12,null,12,null,null,12,null,null,12,null,null,12,12,null,12,12,null,12,null,null,12,null,12,null,null,12,12,null,12,null,12,null,12,null,null,12,12,null,null,12,12,null,12,12,null,12,12,null,null,12,null,12,null,null,12,null,12,null,12,12,null,12,12,null,null,null,null,12,12,12,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,12,null,12,12,null,null,12,null,12,null,12,null,12,12,null,null,12,12,12,null,12,null,null,12,null,12,null,12,12,null,null,12,null,12,null,12,null,null,12,12,null,12,12,null,12,null,12,null,12,null,12,12,null,null,12,null,12,null,12,null,12,null,12,null,12,12,null,null,12,null,12,null,12,12,12,12,12,null,null,12,12,12,null,null,null,null,12,12,null,null,12,12,12,null,12,null,12,null,12,null,null,12,null,12,null,12,12,12,12,12,null,null,12,null,null,null,12,12,null,12,12,null,12,12,12,null,null,null,12,null,12,null,null,12,null,12,null,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,12,12,12,null,12,null,null,12,null,12,12,12,null,12,12,null,null,12,null,12,null,null,12,12,12,null,null,12,null,null,12,null,12,null,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,12,12,null,null,12,null,null,null,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,null,12,null,12,12,null,null,12,null,12,12,null,12,null,12,null,12,null,null,null,null,null,null,12,null,null,null,12,null,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,null,12,null,12,null,null,12,null,null,12,12,null,null,12,null,12,null,12,null,12,12,null,null,12,null,null,12,12,null,12,12,null,12,null,null,12,null,12,12,12,12,null,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,12,12,null,12,12,null,12,null,null,12,null,null,12,null,12,null,null,null,12,null,12,null,null,12,12,null,12,null,12,12,null,null,12,12,null,12,null,12,12,null,12,null,null,null,null,12,null,null,12,12,12,12,12,null,12,null,null,12,null,12,12,12,12,12,null,null,null,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,12,null,12,null,null,12,null,12,12,null,12,12,null,null,12,null,null,12,12,12,null,12,null,12,null,null,12,12,12,null,12,null,12,null,null,12,null,12,12,null,null,12,null,12,12,null,null,12,12,null,null,null,12,null,12,null,null,12,null,12,null,12,null,null,null,null,12,null,12,null,12,null,12,12,null,12,null,12,null,null,12,null,null,null,12,null,12,null,12,null,null,12,null,null,12,12,12,12,12,null,null,12,null,null,12,null,null,null,12,null,null,null,12,null,12,null,null,null,12,null,null,null,12,null,12,12,null,null,null,12,null,12,null,12,12,null,null,null,12,null,12,null,12,null,null,12,null,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,12,12,null,12,null,12,null,null,12,null,12,null,12,null,null,12,null,12,12,null,12,12,null,12,12,12,null,12,null,null,12,12,null,12,12,12,12,12,null,12,12,null,12,null,12,12,null,12,null,null,null,null,12,null,12,null,12,12,null,12,12,null,12,null,null,12,null,12,null,12,null,12,null,null,null,12,null,null,12,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,12,null,12,null,12,12,12,null,null,12,null,12,null,null,12,12,null,12,null,null,12,12,12,null,null,12,null,null,12,null,12,12,12,12,12,null,12,null,12,null,12,12,null,12,null,null,12,12,12,null,null,null,12,null,null,null,12,null,12,null,null,12,null,12,null,12,12,null,12,null,12,12,null,12,null,12,null,12,null,null,null,12,null,12,null,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,12,null,12,null,12,12,12,null,12,12,null,null,12,12,null,12,null,12,12,null,null,12,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,null,null,null,null,null,null,12,12,null,12,12,12,null,12,null,12,12,null,12,12,null,12,null,null,12,null,null,12,null,null,null,null,12,null,12,12,12,null,12,12,null,12,null,12,12,12,null,12,12,12,null,12,12,null,12,null,12,12,null,null,null,null,null,null,null,12,12,12,null,12,null,12,null,12,null,12,null,12,12,null,null,null,null,null,null,null,12,12,null,12,null,null,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,12,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,12,null,12,null,12,null,12,12,null,null,12,null,12,null,12,null,null,null,12,null,12,12,null,null,12,null,12,null,null,null,null,null,null,null,12,null,null,null,12,null,12,12,null,null,null,12,null,12,null,12,null,null,12,null,12,12,null,12,12,null,null,null,12,null,12,null,12,null,12,null,null,12,null,null,12,12,null,12,12,null,12,12,null,null,12,12,null,12,null,12,null,null,12,12,null,12,null,12,12,null,null,12,null,null,12,null,12,null,12,null,null,12,null,null,null,null,null,null,null,12,null,null,12,null,12,null,12,12,12,null,12,12,12,12,null,12,null,12,null,12,null,null,12,12,12,null,null,12,null,null,12,null,null,12,12,12,null,12,null,12,null,null,12,12,null,12,null,null,12,null,null,12,null,12,12,null,12,null,12,null,null,12,null,12,null,null,null,12,null,null,null,12,12,null,12,null,null,12,12,null,12,null,12,null,null,null,12,null,12,null,12,12,null,12,12,null,12,null,12,12,null,12,null,12,null,12,12,null,null,12,12,null,12,null,12,12,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,null,12,null,12,12,null,12,null,12,12,null,12,12,null,12,null,12,null,null,12,null,12,12,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,12,null,null,12,null,null,null,12,null,12,null,null,12,12,null,null,null,12,null,null,12,null,12,12,null,12,12,12,null,12,null,12,null,12,null,12,null,null,null,null,12,null,null,12,null,12,null,12,null,12,null,12,12,null,12,null,null,12,null,12,12,12,null,12,12,12,null,12,12,null,12,12,null,null,null,null,null,12,null,12,null,null,12,null,null,12,null,null,12,12,12,null,12,null,12,12,null,null,12,null,null,12,null,null,12,null,12,12,null,null,12,12,12,12,null,12,null,null,12,null,null,12,null,12,null,null,null,12,12,null,12,null,12,null,null,12,null,null,12,null,12,12,null,12,null,12,null,12,null,12,12,null,null,null,null,null,null,null,12,12,null,12,null,12,12,null,12,12,null,null,12,null,null,12,12,12,null,12,null,12,12,null,12,null,12,null,null,12,null,12,null,12,12,null,12,12,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,12,12,null,12,null,12,null,12,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,12,12,12,null,null,12,null,12,null,null,null,12,12,null,12,12,12,null,12,null,12,null,12,null,12,12,12,12,12,12,null,12,null,12,null,12,null,null,12,null,null,12,12,12,null,12,12,12,null,12,12,null,12,12,null,null,null,12,12,12,12,12,null,null,12,null,12,null,12,12,12,null,null,12,null,null,12,null,12,12,null,null,12,null,12,null,12,null,null,12,null,12,12,null,null,12,null,12,12,null,12,null,12,12,null,12,12,null,12,12,12,12,null,null,null,null,null,null,null,12,12,null,12,12,12,12,12,null,12,12,null,12,null,12,null,12,12,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,12,null,null,12,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,12,12,null,12,null,12,null,12,null,null,12,12,12,null,12,null,12,null,12,12,12,null,null,12,12,null,12,12,12,null,12,null,12,null,12,12,null,12,12,null,12,null,12,12,12,12,null,null,12,12,null,null,12,null,12,null,12,null,12,12,null,12,null,12,null,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,null,12,12,null,12,null,12,null,null,null,null,12,12,12,null,12,null,12,12,null,12,null,null,null,12,null,null,12,null,null,12,null,12,12,null,null,12,null,null,12,12,null,12,12,null,12,null,null,12,null,12,null,null,null,12,12,12,12,null,12,null,12,null,12,null,null,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,null,12,12,12,null,12,12,null,null,12,null,null,null,12,12,null,null,null,12,null,12,12,null,12,null,12,12,null,null,12,null,null,12,null,null,12,null,12,12,null,12,12,null,12,12,null,12,12,null,12,null,null,12,null,12,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,null,null,null,null,null,null,13,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null],"memalloc":[124.5457000732422,124.5457000732422,124.5457000732422,124.5457000732422,139.8279342651367,139.8279342651367,139.8279342651367,139.8279342651367,170.2936782836914,170.2936782836914,170.2936782836914,170.2936782836914,170.2936782836914,170.2936782836914,170.2936782836914,170.2936782836914,170.2937240600586,170.2937240600586,170.2937240600586,170.2937240600586,170.2937240600586,170.2937240600586,170.2937240600586,170.2937240600586,170.2937240600586,170.2937240600586,170.2937240600586,170.2937240600586,170.2937240600586,170.2937240600586,170.2934188842773,170.2934188842773,185.7424774169922,185.7424774169922,185.9997787475586,186.2827529907227,186.5996856689453,186.5996856689453,186.5996856689453,186.9812164306641,187.3366851806641,187.3366851806641,187.3366851806641,187.7135848999023,188.1149215698242,188.1149215698242,188.5162124633789,188.5162124633789,185.7616882324219,186.1338043212891,186.5226821899414,186.5226821899414,186.9299392700195,186.9299392700195,187.3355331420898,187.3355331420898,187.7373275756836,187.7373275756836,187.7373275756836,188.1365280151367,188.1365280151367,188.5257873535156,188.6398468017578,188.6398468017578,186.1633758544922,186.1633758544922,186.5356674194336,186.9333648681641,187.3377838134766,187.3377838134766,187.7332916259766,187.7332916259766,188.1265335083008,188.1265335083008,188.5182113647461,188.5182113647461,188.7207107543945,188.7207107543945,188.7207107543945,186.1931228637695,186.5575790405273,186.9463882446289,186.9463882446289,186.9463882446289,187.3441925048828,187.3441925048828,187.7416381835938,187.7416381835938,188.1345138549805,188.1345138549805,188.5261993408203,188.5261993408203,188.5261993408203,188.8001098632812,188.8001098632812,188.8001098632812,186.2445831298828,186.2445831298828,186.2445831298828,186.6006546020508,186.6006546020508,186.9708938598633,186.9708938598633,186.9708938598633,187.3613586425781,187.7491149902344,187.7491149902344,188.1388244628906,188.527946472168,188.8782958984375,188.8782958984375,188.8782958984375,186.2923126220703,186.2923126220703,186.6443557739258,186.6443557739258,187.0111083984375,187.0111083984375,187.393669128418,187.393669128418,187.7801895141602,187.7801895141602,188.1620254516602,188.1620254516602,188.5440826416016,188.5440826416016,188.9551849365234,188.9551849365234,188.9551849365234,186.393424987793,186.393424987793,186.744384765625,187.1084747314453,187.1084747314453,187.4862976074219,187.8703460693359,187.8703460693359,188.2534103393555,188.2534103393555,188.6408615112305,188.6408615112305,189.0308380126953,189.0308380126953,186.4895935058594,186.4895935058594,186.8348999023438,186.8348999023438,187.1923675537109,187.1923675537109,187.1923675537109,187.5636367797852,187.9416122436523,188.3224182128906,188.3224182128906,188.3224182128906,188.6995315551758,188.6995315551758,188.6995315551758,189.0822219848633,189.0822219848633,186.5731887817383,186.5731887817383,186.5731887817383,186.9116973876953,186.9116973876953,187.2610778808594,187.2610778808594,187.6184997558594,187.6184997558594,187.6184997558594,187.9806442260742,187.9806442260742,188.3477401733398,188.3477401733398,188.723274230957,188.723274230957,189.102180480957,189.1785125732422,189.1785125732422,186.9470901489258,186.9470901489258,187.2881088256836,187.6400604248047,187.6400604248047,188.0022277832031,188.0022277832031,188.0022277832031,188.3728103637695,188.3728103637695,188.747314453125,188.747314453125,189.1277084350586,189.2505645751953,189.2505645751953,189.2505645751953,187.0198211669922,187.3538818359375,187.7012710571289,187.7012710571289,188.0583419799805,188.4252624511719,188.7967834472656,188.7967834472656,189.2150802612305,189.2150802612305,189.3214416503906,189.3214416503906,189.3214416503906,187.1447677612305,187.4821548461914,187.4821548461914,187.8299789428711,187.8299789428711,188.1835098266602,188.5504989624023,188.9236831665039,188.9236831665039,189.3056793212891,189.3056793212891,189.3911590576172,189.3911590576172,189.3911590576172,187.2773895263672,187.2773895263672,187.2773895263672,187.6185607910156,187.9689865112305,188.3348617553711,188.7092514038086,189.0902786254883,189.0902786254883,189.4597778320312,189.4597778320312,189.4597778320312,187.1453170776367,187.4692459106445,187.8089141845703,187.8089141845703,188.1586227416992,188.1586227416992,188.5241394042969,188.8997268676758,189.2858352661133,189.5272827148438,189.5272827148438,187.3559112548828,187.3559112548828,187.3559112548828,187.6866607666016,187.6866607666016,188.0272598266602,188.0272598266602,188.38330078125,188.38330078125,188.7526321411133,189.1294784545898,189.1294784545898,189.5134353637695,189.5937347412109,189.5937347412109,189.5937347412109,187.5875778198242,187.5875778198242,187.914665222168,187.914665222168,187.914665222168,188.2617340087891,188.2617340087891,188.6244583129883,188.6244583129883,188.9952926635742,189.3712692260742,189.3712692260742,189.6590728759766,189.6590728759766,189.6590728759766,187.5259399414062,187.5259399414062,187.5259399414062,187.8410949707031,187.8410949707031,188.1717376708984,188.5212860107422,188.8835754394531,188.8835754394531,189.2549514770508,189.6332702636719,189.6332702636719,189.7234191894531,189.7234191894531,189.7234191894531,187.765022277832,187.765022277832,188.0822906494141,188.0822906494141,188.0822906494141,188.422119140625,188.7757720947266,188.7757720947266,189.1415023803711,189.1415023803711,189.5178375244141,189.5178375244141,189.7866821289062,189.7866821289062,189.7866821289062,187.7191390991211,188.023193359375,188.023193359375,188.023193359375,188.3481521606445,188.6961364746094,188.6961364746094,189.0534591674805,189.421012878418,189.421012878418,189.799690246582,189.8488616943359,189.8488616943359,189.8488616943359,187.9938735961914,187.9938735961914,188.3071136474609,188.3071136474609,188.6469802856445,189.0020294189453,189.0020294189453,189.3699417114258,189.3699417114258,189.7492218017578,189.9101257324219,189.9101257324219,187.9989318847656,188.3058319091797,188.3058319091797,188.6402587890625,188.6402587890625,188.6402587890625,188.9901962280273,189.3568267822266,189.7338256835938,189.7338256835938,189.7338256835938,189.9703674316406,189.9703674316406,189.9703674316406,189.9703674316406,189.9703674316406,189.9703674316406,189.9703674316406,189.9703674316406,189.9703674316406,189.9703674316406,189.9703674316406,189.9703674316406,189.9703674316406,189.9703674316406,189.9703674316406,189.9703674316406,189.9703674316406,189.9703674316406,189.9703674316406,189.9703674316406,189.9703674316406,189.9703674316406,189.9703674316406,189.9703674316406,189.9703674316406,189.9703674316406,189.9703674316406,189.9703674316406,187.8966445922852,187.8966445922852,187.8966445922852,187.8966445922852,188.0370712280273,188.2653121948242,188.2653121948242,188.5065689086914,188.7815628051758,188.7815628051758,189.0890426635742,189.4222183227539,189.4222183227539,189.7570724487305,189.7570724487305,190.0294189453125,190.0294189453125,188.0442352294922,188.3187026977539,188.3187026977539,188.3187026977539,188.6321487426758,188.9762573242188,189.3338088989258,189.3338088989258,189.7077713012695,189.7077713012695,189.7077713012695,190.0877990722656,190.0877990722656,188.0944519042969,188.0944519042969,188.3803329467773,188.6892929077148,188.6892929077148,188.6892929077148,189.0312881469727,189.0312881469727,189.3887176513672,189.3887176513672,189.7600479125977,189.7600479125977,189.7600479125977,190.1406326293945,188.1805953979492,188.1805953979492,188.4645385742188,188.76611328125,188.76611328125,189.0812911987305,189.0812911987305,189.4629898071289,189.4629898071289,189.8207244873047,189.8207244873047,190.1884918212891,190.2016983032227,190.2016983032227,190.2016983032227,188.5121536254883,188.5121536254883,188.8088684082031,188.8088684082031,189.1426239013672,189.1426239013672,189.4731140136719,189.4731140136719,189.8187866210938,189.8187866210938,190.1777572631836,190.2572631835938,190.2572631835938,190.2572631835938,188.5492858886719,188.5492858886719,188.8382797241211,188.8382797241211,189.1660690307617,189.5032272338867,189.8503265380859,190.2156600952148,190.3119430541992,190.3119430541992,190.3119430541992,188.5662231445312,188.8385620117188,189.1505737304688,189.1505737304688,189.4933013916016,189.4933013916016,189.8509521484375,190.2205657958984,190.3657455444336,190.3657455444336,190.3657455444336,188.5976638793945,188.8540878295898,189.1506881713867,189.1506881713867,189.4653549194336,189.4653549194336,189.8054046630859,189.8054046630859,190.1505813598633,190.1505813598633,190.1505813598633,190.4186248779297,190.4186248779297,188.6475296020508,188.6475296020508,188.9126739501953,189.2000350952148,189.5263366699219,189.8732833862305,190.2199249267578,190.2199249267578,190.2199249267578,190.4706954956055,190.4706954956055,190.4706954956055,190.4706954956055,188.7452774047852,189.0088195800781,189.0088195800781,189.3039245605469,189.6324844360352,189.6324844360352,189.9809112548828,190.3340377807617,190.5219345092773,190.5219345092773,190.5219345092773,190.5219345092773,188.8773651123047,188.8773651123047,189.1500473022461,189.1500473022461,189.1500473022461,189.4592437744141,189.4592437744141,189.8343963623047,189.8343963623047,189.8343963623047,190.1923446655273,190.1923446655273,190.5640182495117,190.5640182495117,190.5722961425781,190.5722961425781,190.5722961425781,189.092529296875,189.092529296875,189.389274597168,189.389274597168,189.716194152832,189.716194152832,190.0601196289062,190.0601196289062,190.4119491577148,190.4119491577148,190.6218566894531,190.6218566894531,190.6218566894531,188.9976272583008,188.9976272583008,189.2708587646484,189.2708587646484,189.5784530639648,189.9111557006836,190.2635803222656,190.628044128418,190.628044128418,190.6706314086914,190.6706314086914,190.6706314086914,189.2101821899414,189.2101821899414,189.5015411376953,189.8235397338867,190.1698989868164,190.1698989868164,190.5301132202148,190.7185897827148,190.7185897827148,190.7185897827148,189.171760559082,189.171760559082,189.4486999511719,189.4486999511719,189.4486999511719,189.795051574707,190.1424102783203,190.4997863769531,190.4997863769531,190.4997863769531,190.7658004760742,190.7658004760742,190.7658004760742,189.195182800293,189.195182800293,189.4667816162109,189.4667816162109,189.4667816162109,189.7728805541992,190.1104049682617,190.1104049682617,190.4612426757812,190.4612426757812,190.8122024536133,190.8122024536133,190.8122024536133,190.8122024536133,189.4677352905273,189.4677352905273,189.7643585205078,189.7643585205078,190.0975875854492,190.4435119628906,190.8041839599609,190.8041839599609,190.8041839599609,190.85791015625,190.85791015625,190.85791015625,189.4810791015625,189.4810791015625,189.7655258178711,189.7655258178711,190.0894622802734,190.0894622802734,190.4305419921875,190.4305419921875,190.4305419921875,190.7909469604492,190.7909469604492,190.9029006958008,190.9029006958008,189.5121536254883,189.5121536254883,189.7904891967773,189.7904891967773,190.1078720092773,190.4546508789062,190.4546508789062,190.8107757568359,190.9470443725586,190.9470443725586,190.9470443725586,189.5572891235352,189.5572891235352,189.8316268920898,190.1736145019531,190.1736145019531,190.5138092041016,190.5138092041016,190.8667602539062,190.8667602539062,190.9906005859375,190.9906005859375,190.9906005859375,189.6330032348633,189.6330032348633,189.9125137329102,189.9125137329102,190.2291259765625,190.2291259765625,190.5672149658203,190.5672149658203,190.915771484375,190.915771484375,191.0334548950195,191.0334548950195,191.0334548950195,191.0334548950195,191.0334548950195,191.0334548950195,191.0334548950195,191.0334548950195,191.0334548950195,191.0334548950195,191.0334548950195,191.0334548950195,191.0334548950195,191.0334548950195,191.0334548950195,191.0334548950195,191.0334548950195,191.0334548950195,191.0334548950195,191.0334548950195,191.0334548950195,191.0334548950195,191.0334548950195,191.0334548950195,191.0334548950195,191.0334548950195,191.0334548950195,191.0334548950195,191.0334548950195,191.0334548950195,191.0334548950195,191.0334548950195,191.0334548950195,191.0334548950195,191.0334548950195,191.0334548950195,191.0334548950195,191.0334548950195,191.0334548950195,191.0334548950195,191.0334548950195,191.0334548950195,191.0334548950195,191.0334548950195,191.0334548950195,191.0334548950195,189.5592880249023,189.5592880249023,189.5672225952148,189.5672225952148,189.8072509765625,189.8072509765625,190.0662384033203,190.3517684936523,190.3517684936523,190.6631088256836,190.9694137573242,190.9694137573242,191.3275833129883,191.3275833129883,191.3275833129883,191.7022323608398,191.7022323608398,192.0914077758789,192.4261703491211,192.759651184082,192.759651184082,192.759651184082,193.0918197631836,193.0918197631836,193.4241485595703,193.4241485595703,193.7568511962891,193.7568511962891,194.089973449707,194.3833160400391,194.3833160400391,194.3833160400391,194.3833160400391,194.3833160400391,194.3833160400391,190.0637969970703,190.4080200195312,190.4080200195312,190.7569274902344,191.1339492797852,191.1339492797852,191.5268630981445,191.5268630981445,191.5268630981445,191.9285659790039,191.9285659790039,192.3294677734375,192.7242889404297,193.1026840209961,193.4637680053711,193.4637680053711,193.4637680053711,193.8359298706055,193.8359298706055,194.2084808349609,194.2084808349609,194.515266418457,194.515266418457,194.515266418457,194.515266418457,190.2430648803711,190.2430648803711,190.5769348144531,190.9157791137695,190.9157791137695,191.2483749389648,191.6309127807617,192.0255508422852,192.0255508422852,192.4208374023438,192.8160095214844,192.8160095214844,193.1933212280273,193.1933212280273,193.1933212280273,193.570930480957,193.570930480957,193.570930480957,193.9424133300781,193.9424133300781,194.3107376098633,194.3107376098633,194.6451263427734,194.6451263427734,194.6451263427734,194.6451263427734,190.415168762207,190.415168762207,190.415168762207,190.7380218505859,191.0663528442383,191.0663528442383,191.3992691040039,191.3992691040039,191.7742767333984,192.1688919067383,192.1688919067383,192.1688919067383,192.5622253417969,192.9555282592773,192.9555282592773,193.3420867919922,193.3420867919922,193.7179565429688,194.091911315918,194.091911315918,194.4656982421875,194.4656982421875,194.7728042602539,194.7728042602539,194.7728042602539,194.7728042602539,194.7728042602539,194.7728042602539,190.647087097168,190.9626007080078,191.2780303955078,191.6211547851562,191.9862518310547,191.9862518310547,192.3660202026367,192.3660202026367,192.7470092773438,193.1337509155273,193.1337509155273,193.5194549560547,193.9049758911133,194.2829513549805,194.6532135009766,194.8985061645508,194.8985061645508,194.8985061645508,190.5758743286133,190.5758743286133,190.8684158325195,190.8684158325195,191.1814270019531,191.1814270019531,191.4867858886719,191.4867858886719,191.4867858886719,191.8394622802734,191.8394622802734,192.0588455200195,192.0588455200195,192.2699737548828,192.2699737548828,192.4807281494141,192.7202453613281,192.7202453613281,193.0739593505859,193.0739593505859,193.0739593505859,193.4346084594727,193.4346084594727,193.8056182861328,194.1627807617188,194.1627807617188,194.5275802612305,194.8841705322266,194.8841705322266,194.8841705322266,195.0221252441406,195.0221252441406,195.0221252441406,190.8286056518555,191.1048736572266,191.3989028930664,191.3989028930664,191.7062149047852,191.7062149047852,192.0552062988281,192.0552062988281,192.0552062988281,192.4448089599609,192.7913055419922,193.1486282348633,193.1486282348633,193.5209350585938,193.5209350585938,193.8994827270508,193.8994827270508,194.2860794067383,194.6773223876953,194.6773223876953,195.0625610351562,195.1437530517578,195.1437530517578,195.1437530517578,191.0956573486328,191.0956573486328,191.3871765136719,191.6821060180664,191.6821060180664,192.0211029052734,192.3777465820312,192.7556686401367,192.7556686401367,193.1405181884766,193.1405181884766,193.5189666748047,193.5189666748047,193.9090728759766,193.9090728759766,193.9090728759766,194.2984848022461,194.2984848022461,194.6902694702148,194.6902694702148,195.0839004516602,195.0839004516602,195.2633972167969,195.2633972167969,195.2633972167969,191.2032699584961,191.2032699584961,191.4866180419922,191.4866180419922,191.7758102416992,191.7758102416992,192.1046981811523,192.4554290771484,192.4554290771484,192.8235549926758,192.8235549926758,193.2077102661133,193.2077102661133,193.5877532958984,193.9771728515625,193.9771728515625,194.3675842285156,194.3675842285156,194.7339782714844,194.7339782714844,195.1231689453125,195.1231689453125,195.3811340332031,195.3811340332031,195.3811340332031,195.3811340332031,195.3811340332031,195.3811340332031,191.6130981445312,191.8929290771484,192.202995300293,192.541259765625,192.9021682739258,192.9021682739258,192.9021682739258,193.2792816162109,193.2792816162109,193.2792816162109,193.6397323608398,193.6397323608398,194.0174942016602,194.0174942016602,194.3997192382812,194.3997192382812,194.7669677734375,194.7669677734375,195.1529922485352,195.1529922485352,195.4969329833984,195.4969329833984,195.4969329833984,195.4969329833984,195.4969329833984,195.4969329833984,195.4969329833984,195.4969329833984,191.6616973876953,191.6616973876953,191.9329071044922,192.2270889282227,192.2270889282227,192.5427551269531,192.5427551269531,192.8896942138672,192.8896942138672,193.2521896362305,193.2521896362305,193.6139144897461,193.9878082275391,193.9878082275391,194.3529663085938,194.3529663085938,194.7255325317383,194.7255325317383,195.1073837280273,195.1073837280273,195.4907608032227,195.4907608032227,195.4907608032227,195.610954284668,195.610954284668,195.610954284668,191.7471771240234,191.7471771240234,192.0102157592773,192.0102157592773,192.289924621582,192.289924621582,192.5977096557617,192.9332885742188,192.9332885742188,193.2876968383789,193.2876968383789,193.6125030517578,193.6125030517578,194.0176773071289,194.0176773071289,194.3962326049805,194.780632019043,195.1521301269531,195.1521301269531,195.5374755859375,195.5374755859375,195.7229995727539,195.7229995727539,195.7229995727539,191.869987487793,191.869987487793,192.1270294189453,192.1270294189453,192.3953628540039,192.3953628540039,192.7085342407227,193.0421295166016,193.0421295166016,193.3962936401367,193.766845703125,193.766845703125,194.1476821899414,194.5310745239258,194.5310745239258,194.9212036132812,195.3016357421875,195.6835556030273,195.6835556030273,195.8334121704102,195.8334121704102,195.8334121704102,192.0931015014648,192.3519592285156,192.3519592285156,192.638053894043,192.9589996337891,193.2981262207031,193.6540603637695,194.0311584472656,194.0311584472656,194.4115982055664,194.7917785644531,194.7917785644531,195.1563034057617,195.1563034057617,195.5391311645508,195.9234390258789,195.9234390258789,195.9418716430664,195.9418716430664,195.9418716430664,192.3378601074219,192.3378601074219,192.6205749511719,192.6205749511719,192.9225463867188,192.9225463867188,193.2475280761719,193.5908203125,193.5908203125,193.9535369873047,194.3351974487305,194.3351974487305,194.7157592773438,194.7157592773438,194.7157592773438,195.1046447753906,195.1046447753906,195.4961013793945,195.4961013793945,195.8856506347656,195.8856506347656,196.0486907958984,196.0486907958984,196.0486907958984,196.0486907958984,192.4216156005859,192.4216156005859,192.6806640625,192.9683151245117,193.2807769775391,193.2807769775391,193.6150131225586,193.6150131225586,193.9664764404297,193.9664764404297,194.3307647705078,194.7045516967773,194.7045516967773,195.0792388916016,195.0792388916016,195.4703750610352,195.4703750610352,195.8599319458008,195.8599319458008,196.1537857055664,196.1537857055664,196.1537857055664,196.1537857055664,192.7338562011719,192.9941940307617,192.9941940307617,193.2881164550781,193.6018676757812,193.6018676757812,193.9380798339844,193.9380798339844,194.2935104370117,194.6632766723633,195.0420227050781,195.0420227050781,195.0420227050781,195.4278869628906,195.4278869628906,195.8190307617188,195.8190307617188,195.8190307617188,196.2092666625977,196.2570648193359,196.2570648193359,192.8169555664062,192.8169555664062,192.8169555664062,193.0949554443359,193.3817901611328,193.6911849975586,193.6911849975586,193.6911849975586,194.0251159667969,194.0251159667969,194.0251159667969,194.3804244995117,194.3804244995117,194.7519073486328,195.1277770996094,195.5156478881836,195.9046783447266,196.2852172851562,196.2852172851562,196.3588180541992,196.3588180541992,192.9515991210938,192.9515991210938,193.1988983154297,193.4762573242188,193.4762573242188,193.7752914428711,193.7752914428711,193.7752914428711,194.1003189086914,194.4485702514648,194.8137817382812,194.8137817382812,195.1905212402344,195.1905212402344,195.5691986083984,195.5691986083984,195.9613494873047,195.9613494873047,196.3474197387695,196.3474197387695,196.4588623046875,196.4588623046875,196.4588623046875,193.0832901000977,193.0832901000977,193.3249206542969,193.3249206542969,193.5830993652344,193.8755493164062,193.8755493164062,194.1979141235352,194.1979141235352,194.5417251586914,194.9069976806641,194.9069976806641,195.2860488891602,195.2860488891602,195.6689300537109,195.6689300537109,196.0635833740234,196.0635833740234,196.4448699951172,196.4448699951172,196.5573501586914,196.5573501586914,193.2352905273438,193.2352905273438,193.5081253051758,193.7834625244141,193.7834625244141,194.0842132568359,194.0842132568359,194.4169540405273,194.4169540405273,194.4169540405273,194.769287109375,194.769287109375,195.1438064575195,195.1438064575195,195.5178680419922,195.5178680419922,195.8983001708984,195.8983001708984,196.2934112548828,196.6541290283203,196.6541290283203,196.6541290283203,196.6541290283203,196.6541290283203,196.6541290283203,196.6541290283203,196.6541290283203,196.6541290283203,196.6541290283203,196.6541290283203,196.6541290283203,196.6541290283203,196.6541290283203,196.6541290283203,196.6541290283203,196.6541290283203,196.6541290283203,196.6541290283203,196.6541290283203,196.6541290283203,196.6541290283203,196.6541290283203,196.6541290283203,193.3203811645508,193.3203811645508,193.3448944091797,193.3448944091797,193.5361175537109,193.75732421875,193.9906311035156,193.9906311035156,194.2410507202148,194.2410507202148,194.5305709838867,194.8470306396484,195.2000350952148,195.2000350952148,195.5461196899414,195.9265060424805,195.9265060424805,195.9265060424805,196.3189163208008,196.7163162231445,196.7163162231445,196.7491836547852,196.7491836547852,193.585334777832,193.8359832763672,193.8359832763672,193.8359832763672,194.1072463989258,194.4123992919922,194.4123992919922,194.7439346313477,194.7439346313477,195.0871734619141,195.4389343261719,195.4389343261719,195.8066024780273,195.8066024780273,196.1871795654297,196.1871795654297,196.5750350952148,196.5750350952148,196.8429718017578,196.8429718017578,196.8429718017578,196.8429718017578,196.8429718017578,196.8429718017578,193.8107604980469,193.8107604980469,194.0655517578125,194.3435745239258,194.3435745239258,194.656623840332,194.9938201904297,195.3419647216797,195.3419647216797,195.702392578125,195.702392578125,196.0724716186523,196.455078125,196.455078125,196.8457107543945,196.9352569580078,196.9352569580078,193.8268127441406,193.8268127441406,193.8268127441406,194.0768585205078,194.0768585205078,194.0768585205078,194.3501052856445,194.3501052856445,194.6547012329102,194.6547012329102,194.6547012329102,194.9861526489258,194.9861526489258,195.3322601318359,195.6881790161133,196.0558700561523,196.0558700561523,196.4751358032227,196.8634185791016,196.8634185791016,197.0260314941406,197.0260314941406,193.9297332763672,194.1700286865234,194.4294891357422,194.4294891357422,194.7196273803711,195.0416259765625,195.3843154907227,195.3843154907227,195.7367324829102,196.1021270751953,196.1021270751953,196.4809951782227,196.4809951782227,196.8686752319336,197.115364074707,197.115364074707,197.115364074707,197.115364074707,197.115364074707,197.115364074707,194.2546081542969,194.2546081542969,194.5094451904297,194.7927703857422,195.1089935302734,195.1089935302734,195.4497756958008,195.4497756958008,195.8015975952148,195.8015975952148,196.1634521484375,196.1634521484375,196.5347366333008,196.5347366333008,196.9184875488281,197.2033004760742,197.2033004760742,197.2033004760742,197.2033004760742,197.2033004760742,197.2033004760742,194.3656387329102,194.3656387329102,194.6152191162109,194.8943710327148,194.8943710327148,195.2032241821289,195.2032241821289,195.5399322509766,195.5399322509766,195.8889465332031,195.8889465332031,196.2478256225586,196.2478256225586,196.6209030151367,196.6209030151367,197.0061874389648,197.2897720336914,197.2897720336914,197.2897720336914,197.2897720336914,197.2897720336914,197.2897720336914,194.5250244140625,194.5250244140625,194.7767639160156,195.0563354492188,195.0563354492188,195.3722305297852,195.7138290405273,195.7138290405273,195.7138290405273,196.0630035400391,196.0630035400391,196.4239959716797,196.4239959716797,196.8015823364258,196.8015823364258,197.1876525878906,197.1876525878906,197.374755859375,197.374755859375,197.374755859375,197.374755859375,194.6767044067383,194.6767044067383,194.9302673339844,194.9302673339844,195.2144546508789,195.5333938598633,195.5333938598633,195.8736953735352,196.2240905761719,196.2240905761719,196.5860748291016,196.5860748291016,196.95947265625,196.95947265625,197.3401489257812,197.4585342407227,197.4585342407227,197.4585342407227,194.619255065918,194.619255065918,194.8533554077148,194.8533554077148,195.107307434082,195.107307434082,195.3945083618164,195.3945083618164,195.7179260253906,195.7179260253906,196.0631408691406,196.4182739257812,196.4182739257812,196.7696075439453,197.1508636474609,197.1508636474609,197.5407791137695,197.5407791137695,197.5407791137695,197.5407791137695,197.5407791137695,197.5407791137695,194.8345947265625,194.8345947265625,195.0776596069336,195.0776596069336,195.3491134643555,195.3491134643555,195.6563491821289,195.6563491821289,195.9938583374023,196.3418045043945,196.3418045043945,196.7020111083984,196.7020111083984,197.0735549926758,197.0735549926758,197.4604187011719,197.4604187011719,197.6218719482422,197.6218719482422,197.6218719482422,194.8490676879883,194.8490676879883,195.0819931030273,195.3404235839844,195.3404235839844,195.6302871704102,195.9526748657227,195.9526748657227,196.2972717285156,196.2972717285156,196.6513977050781,196.6513977050781,197.0232162475586,197.0232162475586,197.4069976806641,197.4069976806641,197.7014923095703,197.7014923095703,197.7014923095703,197.7014923095703,197.7014923095703,197.7014923095703,195.1141967773438,195.3628158569336,195.3628158569336,195.6386947631836,195.9537963867188,195.9537963867188,196.2939758300781,196.6446533203125,196.6446533203125,196.6446533203125,197.0047073364258,197.3777694702148,197.3777694702148,197.7661437988281,197.7661437988281,197.7799758911133,197.7799758911133,197.7799758911133,195.1723098754883,195.4125595092773,195.4125595092773,195.679084777832,195.679084777832,196.0131454467773,196.3473129272461,196.3473129272461,196.6979751586914,197.0578231811523,197.0578231811523,197.0578231811523,197.4298477172852,197.4298477172852,197.8176651000977,197.8176651000977,197.8571090698242,197.8571090698242,197.8571090698242,195.2713317871094,195.2713317871094,195.5037994384766,195.5037994384766,195.7649230957031,195.7649230957031,196.0619888305664,196.0619888305664,196.3896102905273,196.3896102905273,196.3896102905273,196.7367172241211,196.7367172241211,197.0895614624023,197.0895614624023,197.4589385986328,197.8408508300781,197.9329681396484,197.9329681396484,195.3482360839844,195.5776901245117,195.8363418579102,196.1278076171875,196.1278076171875,196.4524383544922,196.4524383544922,196.7944641113281,196.7944641113281,197.1375198364258,197.1375198364258,197.1375198364258,197.5018539428711,197.8776550292969,198.007698059082,198.007698059082,198.007698059082,198.007698059082,198.007698059082,198.007698059082,195.6558609008789,195.6558609008789,195.6558609008789,195.9274597167969,196.2127838134766,196.5268859863281,196.5268859863281,196.8683624267578,196.8683624267578,197.2179336547852,197.2179336547852,197.2179336547852,197.5756225585938,197.953369140625,197.953369140625,198.0811233520508,198.0811233520508,198.0811233520508,198.0811233520508,198.0811233520508,198.0811233520508,195.774658203125,195.774658203125,196.0267944335938,196.3026428222656,196.3026428222656,196.6232528686523,196.6232528686523,196.9663162231445,196.9663162231445,196.9663162231445,197.315315246582,197.315315246582,197.6768112182617,197.6768112182617,198.0556640625,198.0556640625,198.1534118652344,198.1534118652344,198.1534118652344,198.1534118652344,195.689208984375,195.919189453125,195.919189453125,196.1738357543945,196.1738357543945,196.4631652832031,196.7867431640625,197.1331558227539,197.1331558227539,197.4895401000977,197.4895401000977,197.8589172363281,197.8589172363281,198.224494934082,198.224494934082,198.224494934082,198.224494934082,195.8505630493164,195.8505630493164,196.1062316894531,196.3760604858398,196.3760604858398,196.6847076416016,197.0228652954102,197.0228652954102,197.3745040893555,197.3745040893555,197.7376937866211,198.1117401123047,198.1117401123047,198.2945251464844,198.2945251464844,198.2945251464844,198.2945251464844,196.0849380493164,196.3335342407227,196.3335342407227,196.3335342407227,196.6082611083984,196.9262924194336,196.9262924194336,197.2654647827148,197.2654647827148,197.6167221069336,197.9816513061523,198.362190246582,198.362190246582,198.3632888793945,198.3632888793945,198.3632888793945,198.3632888793945,198.3632888793945,198.3632888793945,198.3632888793945,198.3632888793945,198.3632888793945,198.3632888793945,198.3632888793945,198.3632888793945,198.3632888793945,198.3632888793945,198.3632888793945,198.3632888793945,198.3632888793945,198.3632888793945,198.3632888793945,198.3632888793945,198.3632888793945,198.3632888793945,198.3632888793945,198.3632888793945,198.3632888793945,198.3632888793945,198.3632888793945,196.0221481323242,196.0221481323242,196.2072677612305,196.2072677612305,196.4480590820312,196.4480590820312,196.6692733764648,196.9337310791016,196.9337310791016,197.2304611206055,197.2304611206055,197.5572509765625,197.899772644043,197.899772644043,198.2489776611328,198.4307708740234,198.4307708740234,198.4307708740234,198.4307708740234,196.2818069458008,196.2818069458008,196.2818069458008,196.5248413085938,196.5248413085938,196.8025970458984,197.1155395507812,197.4587020874023,197.4587020874023,197.8096542358398,197.8096542358398,198.1743621826172,198.4974136352539,198.4974136352539,198.4974136352539,198.4974136352539,196.3095245361328,196.3095245361328,196.5443267822266,196.5443267822266,196.8088150024414,196.8088150024414,197.1115036010742,197.1115036010742,197.4467391967773,197.7987899780273,197.7987899780273,198.1604461669922,198.1604461669922,198.534912109375,198.5630111694336,198.5630111694336,198.5630111694336,196.3626022338867,196.3626022338867,196.5924530029297,196.5924530029297,196.8756637573242,196.8756637573242,197.1736373901367,197.1736373901367,197.1736373901367,197.5042724609375,197.8497619628906,197.8497619628906,198.2028427124023,198.2028427124023,198.5709533691406,198.5709533691406,198.5709533691406,198.6274948120117,198.6274948120117,196.4395370483398,196.668098449707,196.668098449707,196.922721862793,197.2086791992188,197.539665222168,197.539665222168,197.8859024047852,197.8859024047852,198.2406692504883,198.2406692504883,198.6147689819336,198.6147689819336,198.6909790039062,198.6909790039062,198.6909790039062,196.5335235595703,196.5335235595703,196.7635726928711,196.7635726928711,196.7635726928711,197.0206680297852,197.0206680297852,197.315788269043,197.315788269043,197.643440246582,197.643440246582,197.9761047363281,197.9761047363281,198.3202667236328,198.6768341064453,198.6768341064453,198.7534637451172,198.7534637451172,198.7534637451172,196.6228790283203,196.6228790283203,196.850471496582,197.1024551391602,197.3911361694336,197.3911361694336,197.7150421142578,198.0643157958984,198.4208068847656,198.4208068847656,198.7956237792969,198.8148803710938,198.8148803710938,196.7590026855469,196.9899215698242,196.9899215698242,197.2483596801758,197.2483596801758,197.5336761474609,197.5336761474609,197.8540954589844,197.8540954589844,198.1964492797852,198.1964492797852,198.587043762207,198.8753662109375,198.8753662109375,198.8753662109375,198.8753662109375,198.8753662109375,198.8753662109375,196.9081726074219,197.1415557861328,197.4054565429688,197.4054565429688,197.709716796875,197.709716796875,198.0457153320312,198.3986358642578,198.3986358642578,198.7620086669922,198.9348678588867,198.9348678588867,198.9348678588867,198.9348678588867,198.9348678588867,198.9348678588867,197.0727996826172,197.0727996826172,197.2954788208008,197.557487487793,197.557487487793,197.557487487793,197.8568267822266,198.1892471313477,198.5362701416016,198.886360168457,198.886360168457,198.9934005737305,198.9934005737305,198.9934005737305,198.9934005737305,198.9934005737305,198.9934005737305,197.2008972167969,197.2008972167969,197.4190444946289,197.4190444946289,197.6886138916016,197.6886138916016,197.9980316162109,198.3195724487305,198.3195724487305,198.7031631469727,198.7031631469727,199.0509567260742,199.0509567260742,199.0509567260742,199.0509567260742,199.0509567260742,199.0509567260742,197.0927276611328,197.0927276611328,197.3187408447266,197.5591583251953,197.5591583251953,197.8330841064453,197.8330841064453,198.1447067260742,198.1447067260742,198.4833908081055,198.4833908081055,198.8082504272461,199.1075820922852,199.1075820922852,199.1075820922852,199.1075820922852,199.1075820922852,199.1075820922852,197.2275161743164,197.2275161743164,197.4581832885742,197.7183227539062,197.7183227539062,197.9957885742188,197.9957885742188,198.3107986450195,198.6567687988281,198.6567687988281,199.0126342773438,199.1633682250977,199.1633682250977,199.1633682250977,199.1633682250977,199.1633682250977,199.1633682250977,197.3745040893555,197.6198806762695,197.8769989013672,197.8769989013672,198.1718368530273,198.1718368530273,198.4933395385742,198.8391723632812,198.8391723632812,199.1887054443359,199.1887054443359,199.2181777954102,199.2181777954102,199.2181777954102,197.3376007080078,197.3376007080078,197.5499114990234,197.5499114990234,197.7954711914062,198.0716247558594,198.0716247558594,198.3921966552734,198.7404098510742,199.0967483520508,199.0967483520508,199.2720947265625,199.2720947265625,199.2720947265625,199.2720947265625,199.2720947265625,199.2720947265625,199.2720947265625,199.2720947265625,199.2720947265625,199.2720947265625,199.2720947265625,199.2720947265625,199.2720947265625,199.2720947265625,199.2720947265625,199.2720947265625,199.2720947265625,199.2720947265625,197.4625549316406,197.4625549316406,197.6731262207031,197.9079818725586,198.1676788330078,198.1676788330078,198.4657669067383,198.4657669067383,198.8286743164062,198.8286743164062,199.1740493774414,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,199.3250732421875,197.4984283447266,197.4984283447266,197.4984283447266,197.5372619628906,197.7826385498047,198.0446701049805,198.338264465332,198.338264465332,198.338264465332,198.66357421875,198.66357421875,198.9941940307617,198.9941940307617,199.3182983398438,199.3182983398438,199.6808776855469,200.0797348022461,200.0797348022461,200.4883041381836,200.8438186645508,201.1801376342773,201.1801376342773,201.5161285400391,201.5161285400391,201.8519744873047,201.8519744873047,202.1870193481445,202.1870193481445,202.5218887329102,202.8562927246094,203.1923370361328,203.5285415649414,203.8645095825195,204.2007217407227,204.2007217407227,204.5367813110352,204.5367813110352,204.8712539672852,204.8712539672852,205.087776184082,205.087776184082,205.087776184082,205.087776184082,205.087776184082,205.087776184082,197.9301300048828,198.2005386352539,198.5065155029297,198.5065155029297,198.8401489257812,199.1759414672852,199.5067291259766,199.5067291259766,199.8760452270508,200.2566986083984,200.2566986083984,200.6468505859375,201.0454864501953,201.0454864501953,201.4473037719727,201.4473037719727,201.8516693115234,202.2576065063477,202.659912109375,203.0642166137695,203.4688186645508,203.4688186645508,203.4688186645508,203.8716812133789,203.8716812133789,204.2744216918945,204.2744216918945,204.6774673461914,205.0642929077148,205.2953414916992,205.2953414916992,205.2953414916992,205.2953414916992,205.2953414916992,205.2953414916992,198.2099075317383,198.2099075317383,198.4654312133789,198.7465133666992,198.7465133666992,198.7465133666992,199.0635986328125,199.0635986328125,199.384880065918,199.384880065918,199.7075805664062,199.7075805664062,199.7075805664062,200.0708084106445,200.0708084106445,200.4423522949219,200.8262405395508,200.8262405395508,200.8262405395508,201.2001571655273,201.2001571655273,201.62744140625,202.0162963867188,202.0162963867188,202.407958984375,202.407958984375,202.806770324707,203.2039337158203,203.2039337158203,203.6030197143555,204.004280090332,204.004280090332,204.4077529907227,204.812858581543,205.2053527832031,205.4995422363281,205.4995422363281,205.4995422363281,205.4995422363281,205.4995422363281,205.4995422363281,198.4860458374023,198.4860458374023,198.737190246582,199.0034942626953,199.0034942626953,199.3034286499023,199.6113891601562,199.9340896606445,200.2840957641602,200.6455764770508,200.6455764770508,201.0188827514648,201.4017181396484,201.4017181396484,201.7923355102539,201.7923355102539,202.1841735839844,202.1841735839844,202.5743026733398,202.9729843139648,203.3728408813477,203.3728408813477,203.7729263305664,203.7729263305664,204.1716461181641,204.1716461181641,204.5724487304688,204.5724487304688,204.9749908447266,205.3681793212891,205.3681793212891,205.7005157470703,205.7005157470703,205.7005157470703,205.7005157470703,205.7005157470703,205.7005157470703,199.001106262207,199.001106262207,199.2932891845703,199.2932891845703,199.5872192382812,199.5872192382812,199.887321472168,199.887321472168,200.2170715332031,200.5737915039062,200.5737915039062,200.9371566772461,200.9371566772461,201.3138809204102,201.3138809204102,201.6953659057617,201.6953659057617,202.0856246948242,202.0856246948242,202.4767150878906,202.8649520874023,202.8649520874023,202.8649520874023,203.2526092529297,203.6479110717773,203.6479110717773,204.0446548461914,204.0446548461914,204.44384765625,204.44384765625,204.8428802490234,204.8428802490234,205.2442092895508,205.2442092895508,205.6318893432617,205.8981475830078,205.8981475830078,205.8981475830078,205.8981475830078,199.1050872802734,199.3520736694336,199.6153717041016,199.6153717041016,199.899528503418,199.899528503418,200.1918487548828,200.1918487548828,200.5329895019531,200.5329895019531,200.8893966674805,201.2509841918945,201.6227111816406,202.0043182373047,202.0043182373047,202.3898315429688,202.3898315429688,202.7769927978516,202.7769927978516,203.1638488769531,203.5496139526367,203.9382476806641,203.9382476806641,203.9382476806641,204.3302383422852,204.7282791137695,204.7282791137695,205.1300582885742,205.5333786010742,205.9218215942383,205.9218215942383,206.0927200317383,206.0927200317383,206.0927200317383,206.0927200317383,199.489875793457,199.7402954101562,199.7402954101562,200.0098114013672,200.2907638549805,200.2907638549805,200.604850769043,200.604850769043,200.9535903930664,201.3117370605469,201.6748580932617,202.0504608154297,202.0504608154297,202.0504608154297,202.4286422729492,202.811149597168,202.811149597168,202.811149597168,203.1998062133789,203.1998062133789,203.5897445678711,203.5897445678711,203.9734802246094,203.9734802246094,204.3623199462891,204.7540435791016,204.7540435791016,205.1553115844727,205.1553115844727,205.5571823120117,205.5571823120117,205.9504470825195,205.9504470825195,206.2840347290039,206.2840347290039,206.2840347290039,206.2840347290039,206.2840347290039,206.2840347290039,206.2840347290039,206.2840347290039,206.2840347290039,206.2840347290039,206.2840347290039,206.2840347290039,206.2840347290039,206.2840347290039,206.2840347290039,206.2840347290039,199.6992950439453,199.6992950439453,199.6992950439453,199.6992950439453,199.9261093139648,200.1965408325195,200.1965408325195,200.1965408325195,200.4513778686523,200.7310333251953,200.7310333251953,201.0537414550781,201.0537414550781,201.3822326660156,201.3822326660156,201.718620300293,201.718620300293,201.718620300293,202.0710220336914,202.4509353637695,202.8407821655273,202.8407821655273,203.2326049804688,203.2326049804688,203.6239166259766,204.0203170776367,204.0203170776367,204.4155120849609,204.4155120849609,204.814697265625,204.814697265625,205.2142791748047,205.2142791748047,205.2142791748047,205.6148986816406,205.6148986816406,205.6148986816406,206.016357421875,206.016357421875,206.4161834716797,206.4722595214844,206.4722595214844,206.4722595214844,206.4722595214844,206.4722595214844,206.4722595214844,200.1255264282227,200.3748092651367,200.3748092651367,200.634407043457,200.9138870239258,200.9138870239258,201.2406387329102,201.2406387329102,201.2406387329102,201.5835037231445,201.5835037231445,201.9302673339844,201.9302673339844,202.2843551635742,202.2843551635742,202.6495742797852,203.0201797485352,203.3997344970703,203.7774658203125,203.7774658203125,204.1635665893555,204.1635665893555,204.5508575439453,204.5508575439453,204.9396667480469,204.9396667480469,205.3307800292969,205.3307800292969,205.7240219116211,205.7240219116211,206.1252288818359,206.1252288818359,206.5264739990234,206.5264739990234,206.6574554443359,206.6574554443359,206.6574554443359,206.6574554443359,200.3841400146484,200.6269454956055,200.6269454956055,200.8745727539062,200.8745727539062,201.1455307006836,201.4599838256836,201.7938461303711,202.1362152099609,202.1362152099609,202.4831161499023,202.843391418457,202.843391418457,202.843391418457,203.2126007080078,203.2126007080078,203.5903701782227,203.5903701782227,203.9684143066406,204.3482666015625,204.3482666015625,204.7373352050781,204.7373352050781,205.1296463012695,205.1296463012695,205.5196228027344,205.9121627807617,205.9121627807617,206.31591796875,206.31591796875,206.7197036743164,206.8397216796875,206.8397216796875,206.8397216796875,206.8397216796875,206.8397216796875,206.8397216796875,200.6508331298828,200.6508331298828,200.6508331298828,200.8926544189453,200.8926544189453,201.1362457275391,201.4117431640625,201.4117431640625,201.7284088134766,202.0632553100586,202.0632553100586,202.4057464599609,202.7530136108398,202.7530136108398,203.1117630004883,203.4798583984375,203.4798583984375,203.8573150634766,203.8573150634766,203.8573150634766,204.2372055053711,204.2372055053711,204.6219100952148,205.0529937744141,205.0529937744141,205.4437942504883,205.4437942504883,205.4437942504883,205.8356170654297,205.8356170654297,206.2345275878906,206.2345275878906,213.8860473632812,213.8860473632812,213.8860473632812,213.8860473632812,213.8860473632812,213.8860473632812,213.8860473632812,213.8860473632812,213.8860473632812,213.8860473632812,213.8860473632812,213.8860473632812,213.8860473632812,213.8860473632812,213.8860473632812,213.8860473632812,213.8860473632812,213.8860473632812,221.5154418945312,221.5154495239258,221.5154495239258,221.5154495239258,221.5154495239258,221.5154495239258,221.5154495239258,221.5154495239258,221.5154495239258,221.5154495239258,221.5154495239258,221.5154495239258,221.5154495239258,221.5154495239258,221.5154495239258,221.5154495239258,221.5154495239258,221.5154495239258,221.5154495239258,221.5154495239258,221.5154495239258,221.5154495239258,221.5154495239258,236.7742385864258,236.7742385864258,236.7742385864258,236.7742385864258,236.7742385864258,236.7742385864258,236.7742385864258,236.7742385864258,236.7742385864258,236.7742385864258,236.7742385864258,236.7742385864258,236.7742385864258,236.7742385864258,236.7742385864258,236.7742385864258,244.4415435791016,244.4415435791016,244.4415435791016,244.4415435791016,244.4415435791016,244.4415435791016,244.4415435791016,244.4415435791016,244.4415435791016,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836,259.7988510131836],"meminc":[0,0,0,0,15.28223419189453,0,0,0,30.46574401855469,0,0,0,0,0,0,0,4.57763671875e-05,0,0,0,0,0,0,0,0,0,0,0,0,0,-0.00030517578125,0,15.44905853271484,0,0.2573013305664062,0.2829742431640625,0.3169326782226562,0,0,0.38153076171875,0.35546875,0,0,0.3768997192382812,0.401336669921875,0,0.4012908935546875,0,-2.754524230957031,0.3721160888671875,0.3888778686523438,0,0.407257080078125,0,0.4055938720703125,0,0.40179443359375,0,0,0.399200439453125,0,0.3892593383789062,0.1140594482421875,0,-2.476470947265625,0,0.3722915649414062,0.3976974487304688,0.4044189453125,0,0.3955078125,0,0.3932418823242188,0,0.3916778564453125,0,0.2024993896484375,0,0,-2.527587890625,0.3644561767578125,0.3888092041015625,0,0,0.3978042602539062,0,0.3974456787109375,0,0.3928756713867188,0,0.3916854858398438,0,0,0.2739105224609375,0,0,-2.555526733398438,0,0,0.3560714721679688,0,0.3702392578125,0,0,0.3904647827148438,0.38775634765625,0,0.38970947265625,0.3891220092773438,0.3503494262695312,0,0,-2.585983276367188,0,0.3520431518554688,0,0.3667526245117188,0,0.3825607299804688,0,0.3865203857421875,0,0.3818359375,0,0.3820571899414062,0,0.411102294921875,0,0,-2.561759948730469,0,0.3509597778320312,0.3640899658203125,0,0.3778228759765625,0.3840484619140625,0,0.3830642700195312,0,0.387451171875,0,0.3899765014648438,0,-2.541244506835938,0,0.345306396484375,0,0.3574676513671875,0,0,0.3712692260742188,0.3779754638671875,0.3808059692382812,0,0,0.3771133422851562,0,0,0.3826904296875,0,-2.509033203125,0,0,0.3385086059570312,0,0.3493804931640625,0,0.357421875,0,0,0.3621444702148438,0,0.367095947265625,0,0.3755340576171875,0,0.37890625,0.07633209228515625,0,-2.231422424316406,0,0.3410186767578125,0.3519515991210938,0,0.3621673583984375,0,0,0.3705825805664062,0,0.3745040893554688,0,0.3803939819335938,0.1228561401367188,0,0,-2.230743408203125,0.3340606689453125,0.3473892211914062,0,0.3570709228515625,0.3669204711914062,0.37152099609375,0,0.4182968139648438,0,0.1063613891601562,0,0,-2.176673889160156,0.3373870849609375,0,0.3478240966796875,0,0.3535308837890625,0.3669891357421875,0.3731842041015625,0,0.3819961547851562,0,0.085479736328125,0,0,-2.11376953125,0,0,0.3411712646484375,0.3504257202148438,0.365875244140625,0.3743896484375,0.3810272216796875,0,0.3694992065429688,0,0,-2.314460754394531,0.3239288330078125,0.3396682739257812,0,0.3497085571289062,0,0.3655166625976562,0.3755874633789062,0.3861083984375,0.2414474487304688,0,-2.171371459960938,0,0,0.33074951171875,0,0.3405990600585938,0,0.3560409545898438,0,0.3693313598632812,0.3768463134765625,0,0.3839569091796875,0.08029937744140625,0,0,-2.006156921386719,0,0.32708740234375,0,0,0.3470687866210938,0,0.3627243041992188,0,0.3708343505859375,0.3759765625,0,0.2878036499023438,0,0,-2.133132934570312,0,0,0.315155029296875,0,0.3306427001953125,0.34954833984375,0.3622894287109375,0,0.3713760375976562,0.3783187866210938,0,0.09014892578125,0,0,-1.958396911621094,0,0.3172683715820312,0,0,0.3398284912109375,0.3536529541015625,0,0.3657302856445312,0,0.3763351440429688,0,0.2688446044921875,0,0,-2.067543029785156,0.3040542602539062,0,0,0.3249588012695312,0.3479843139648438,0,0.3573226928710938,0.3675537109375,0,0.3786773681640625,0.04917144775390625,0,0,-1.854988098144531,0,0.3132400512695312,0,0.3398666381835938,0.3550491333007812,0,0.3679122924804688,0,0.3792800903320312,0.1609039306640625,0,-1.91119384765625,0.3069000244140625,0,0.3344268798828125,0,0,0.3499374389648438,0.3666305541992188,0.3769989013671875,0,0,0.236541748046875,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2.073722839355469,0,0,0,0.1404266357421875,0.228240966796875,0,0.2412567138671875,0.274993896484375,0,0.3074798583984375,0.3331756591796875,0,0.3348541259765625,0,0.2723464965820312,0,-1.985183715820312,0.2744674682617188,0,0,0.313446044921875,0.3441085815429688,0.3575515747070312,0,0.37396240234375,0,0,0.3800277709960938,0,-1.99334716796875,0,0.2858810424804688,0.3089599609375,0,0,0.3419952392578125,0,0.3574295043945312,0,0.3713302612304688,0,0,0.380584716796875,-1.960037231445312,0,0.2839431762695312,0.30157470703125,0,0.3151779174804688,0,0.3816986083984375,0,0.3577346801757812,0,0.367767333984375,0.01320648193359375,0,0,-1.689544677734375,0,0.2967147827148438,0,0.3337554931640625,0,0.3304901123046875,0,0.345672607421875,0,0.3589706420898438,0.07950592041015625,0,0,-1.707977294921875,0,0.2889938354492188,0,0.327789306640625,0.337158203125,0.3470993041992188,0.3653335571289062,0.096282958984375,0,0,-1.745719909667969,0.2723388671875,0.31201171875,0,0.3427276611328125,0,0.3576507568359375,0.3696136474609375,0.1451797485351562,0,0,-1.768081665039062,0.2564239501953125,0.296600341796875,0,0.314666748046875,0,0.3400497436523438,0,0.3451766967773438,0,0,0.2680435180664062,0,-1.771095275878906,0,0.2651443481445312,0.2873611450195312,0.3263015747070312,0.3469467163085938,0.3466415405273438,0,0,0.2507705688476562,0,0,0,-1.725418090820312,0.2635421752929688,0,0.29510498046875,0.3285598754882812,0,0.3484268188476562,0.3531265258789062,0.187896728515625,0,0,0,-1.644569396972656,0,0.2726821899414062,0,0,0.3091964721679688,0,0.375152587890625,0,0,0.3579483032226562,0,0.371673583984375,0,0.00827789306640625,0,0,-1.479766845703125,0,0.2967453002929688,0,0.3269195556640625,0,0.3439254760742188,0,0.3518295288085938,0,0.2099075317382812,0,0,-1.624229431152344,0,0.2732315063476562,0,0.3075942993164062,0.33270263671875,0.3524246215820312,0.3644638061523438,0,0.0425872802734375,0,0,-1.46044921875,0,0.2913589477539062,0.3219985961914062,0.3463592529296875,0,0.3602142333984375,0.1884765625,0,0,-1.546829223632812,0,0.2769393920898438,0,0,0.3463516235351562,0.3473587036132812,0.3573760986328125,0,0,0.2660140991210938,0,0,-1.57061767578125,0,0.2715988159179688,0,0,0.3060989379882812,0.3375244140625,0,0.3508377075195312,0,0.3509597778320312,0,0,0,-1.344467163085938,0,0.2966232299804688,0,0.3332290649414062,0.3459243774414062,0.3606719970703125,0,0,0.0537261962890625,0,0,-1.3768310546875,0,0.2844467163085938,0,0.3239364624023438,0,0.3410797119140625,0,0,0.3604049682617188,0,0.1119537353515625,0,-1.3907470703125,0,0.2783355712890625,0,0.3173828125,0.3467788696289062,0,0.3561248779296875,0.1362686157226562,0,0,-1.389755249023438,0,0.2743377685546875,0.3419876098632812,0,0.3401947021484375,0,0.3529510498046875,0,0.12384033203125,0,0,-1.357597351074219,0,0.279510498046875,0,0.3166122436523438,0,0.3380889892578125,0,0.3485565185546875,0,0.1176834106445312,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.474166870117188,0,0.0079345703125,0,0.2400283813476562,0,0.2589874267578125,0.2855300903320312,0,0.31134033203125,0.306304931640625,0,0.3581695556640625,0,0,0.3746490478515625,0,0.3891754150390625,0.3347625732421875,0.3334808349609375,0,0,0.3321685791015625,0,0.3323287963867188,0,0.33270263671875,0,0.3331222534179688,0.2933425903320312,0,0,0,0,0,-4.31951904296875,0.3442230224609375,0,0.348907470703125,0.3770217895507812,0,0.392913818359375,0,0,0.401702880859375,0,0.4009017944335938,0.3948211669921875,0.3783950805664062,0.361083984375,0,0,0.372161865234375,0,0.3725509643554688,0,0.3067855834960938,0,0,0,-4.272201538085938,0,0.3338699340820312,0.3388442993164062,0,0.3325958251953125,0.382537841796875,0.3946380615234375,0,0.3952865600585938,0.395172119140625,0,0.3773117065429688,0,0,0.3776092529296875,0,0,0.3714828491210938,0,0.3683242797851562,0,0.3343887329101562,0,0,0,-4.229957580566406,0,0,0.3228530883789062,0.3283309936523438,0,0.332916259765625,0,0.3750076293945312,0.3946151733398438,0,0,0.3933334350585938,0.3933029174804688,0,0.3865585327148438,0,0.3758697509765625,0.3739547729492188,0,0.3737869262695312,0,0.3071060180664062,0,0,0,0,0,-4.125717163085938,0.3155136108398438,0.3154296875,0.3431243896484375,0.3650970458984375,0,0.3797683715820312,0,0.3809890747070312,0.3867416381835938,0,0.3857040405273438,0.3855209350585938,0.3779754638671875,0.3702621459960938,0.2452926635742188,0,0,-4.3226318359375,0,0.29254150390625,0,0.3130111694335938,0,0.30535888671875,0,0,0.3526763916015625,0,0.2193832397460938,0,0.2111282348632812,0,0.21075439453125,0.2395172119140625,0,0.3537139892578125,0,0,0.3606491088867188,0,0.3710098266601562,0.3571624755859375,0,0.3647994995117188,0.3565902709960938,0,0,0.1379547119140625,0,0,-4.193519592285156,0.2762680053710938,0.2940292358398438,0,0.30731201171875,0,0.3489913940429688,0,0,0.3896026611328125,0.34649658203125,0.3573226928710938,0,0.3723068237304688,0,0.3785476684570312,0,0.3865966796875,0.3912429809570312,0,0.3852386474609375,0.0811920166015625,0,0,-4.048095703125,0,0.2915191650390625,0.2949295043945312,0,0.3389968872070312,0.3566436767578125,0.3779220581054688,0,0.3848495483398438,0,0.378448486328125,0,0.390106201171875,0,0,0.3894119262695312,0,0.39178466796875,0,0.3936309814453125,0,0.1794967651367188,0,0,-4.060127258300781,0,0.2833480834960938,0,0.2891921997070312,0,0.328887939453125,0.3507308959960938,0,0.3681259155273438,0,0.3841552734375,0,0.3800430297851562,0.3894195556640625,0,0.390411376953125,0,0.36639404296875,0,0.389190673828125,0,0.257965087890625,0,0,0,0,0,-3.768035888671875,0.2798309326171875,0.3100662231445312,0.3382644653320312,0.3609085083007812,0,0,0.3771133422851562,0,0,0.3604507446289062,0,0.3777618408203125,0,0.3822250366210938,0,0.36724853515625,0,0.3860244750976562,0,0.3439407348632812,0,0,0,0,0,0,0,-3.835235595703125,0,0.271209716796875,0.2941818237304688,0,0.3156661987304688,0,0.3469390869140625,0,0.3624954223632812,0,0.361724853515625,0.3738937377929688,0,0.3651580810546875,0,0.3725662231445312,0,0.3818511962890625,0,0.3833770751953125,0,0,0.1201934814453125,0,0,-3.863777160644531,0,0.2630386352539062,0,0.2797088623046875,0,0.3077850341796875,0.3355789184570312,0,0.3544082641601562,0,0.3248062133789062,0,0.4051742553710938,0,0.3785552978515625,0.3843994140625,0.3714981079101562,0,0.385345458984375,0,0.1855239868164062,0,0,-3.853012084960938,0,0.2570419311523438,0,0.2683334350585938,0,0.31317138671875,0.3335952758789062,0,0.3541641235351562,0.3705520629882812,0,0.3808364868164062,0.383392333984375,0,0.3901290893554688,0.38043212890625,0.3819198608398438,0,0.1498565673828125,0,0,-3.740310668945312,0.2588577270507812,0,0.2860946655273438,0.3209457397460938,0.3391265869140625,0.3559341430664062,0.3770980834960938,0,0.3804397583007812,0.3801803588867188,0,0.3645248413085938,0,0.3828277587890625,0.384307861328125,0,0.0184326171875,0,0,-3.604011535644531,0,0.28271484375,0,0.301971435546875,0,0.324981689453125,0.343292236328125,0,0.3627166748046875,0.3816604614257812,0,0.3805618286132812,0,0,0.388885498046875,0,0.3914566040039062,0,0.3895492553710938,0,0.1630401611328125,0,0,0,-3.6270751953125,0,0.2590484619140625,0.2876510620117188,0.3124618530273438,0,0.3342361450195312,0,0.3514633178710938,0,0.364288330078125,0.3737869262695312,0,0.3746871948242188,0,0.3911361694335938,0,0.389556884765625,0,0.293853759765625,0,0,0,-3.419929504394531,0.2603378295898438,0,0.2939224243164062,0.313751220703125,0,0.336212158203125,0,0.3554306030273438,0.3697662353515625,0.3787460327148438,0,0,0.3858642578125,0,0.391143798828125,0,0,0.3902359008789062,0.04779815673828125,0,-3.440109252929688,0,0,0.2779998779296875,0.286834716796875,0.3093948364257812,0,0,0.3339309692382812,0,0,0.3553085327148438,0,0.3714828491210938,0.3758697509765625,0.3878707885742188,0.3890304565429688,0.3805389404296875,0,0.07360076904296875,0,-3.407218933105469,0,0.2472991943359375,0.2773590087890625,0,0.2990341186523438,0,0,0.3250274658203125,0.3482513427734375,0.3652114868164062,0,0.376739501953125,0,0.3786773681640625,0,0.39215087890625,0,0.3860702514648438,0,0.1114425659179688,0,0,-3.375572204589844,0,0.2416305541992188,0,0.2581787109375,0.292449951171875,0,0.3223648071289062,0,0.34381103515625,0.3652725219726562,0,0.3790512084960938,0,0.3828811645507812,0,0.3946533203125,0,0.38128662109375,0,0.1124801635742188,0,-3.322059631347656,0,0.2728347778320312,0.2753372192382812,0,0.300750732421875,0,0.3327407836914062,0,0,0.3523330688476562,0,0.3745193481445312,0,0.3740615844726562,0,0.38043212890625,0,0.395111083984375,0.3607177734375,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-3.333747863769531,0,0.02451324462890625,0,0.19122314453125,0.2212066650390625,0.233306884765625,0,0.2504196166992188,0,0.289520263671875,0.3164596557617188,0.3530044555664062,0,0.3460845947265625,0.3803863525390625,0,0,0.3924102783203125,0.39739990234375,0,0.032867431640625,0,-3.163848876953125,0.2506484985351562,0,0,0.2712631225585938,0.3051528930664062,0,0.3315353393554688,0,0.3432388305664062,0.3517608642578125,0,0.3676681518554688,0,0.3805770874023438,0,0.3878555297851562,0,0.2679367065429688,0,0,0,0,0,-3.032211303710938,0,0.254791259765625,0.2780227661132812,0,0.31304931640625,0.3371963500976562,0.34814453125,0,0.3604278564453125,0,0.3700790405273438,0.3826065063476562,0,0.3906326293945312,0.08954620361328125,0,-3.108444213867188,0,0,0.2500457763671875,0,0,0.2732467651367188,0,0.304595947265625,0,0,0.331451416015625,0,0.3461074829101562,0.3559188842773438,0.3676910400390625,0,0.4192657470703125,0.3882827758789062,0,0.1626129150390625,0,-3.096298217773438,0.24029541015625,0.25946044921875,0,0.2901382446289062,0.3219985961914062,0.3426895141601562,0,0.3524169921875,0.3653945922851562,0,0.3788681030273438,0,0.3876800537109375,0.2466888427734375,0,0,0,0,0,-2.860755920410156,0,0.2548370361328125,0.2833251953125,0.31622314453125,0,0.3407821655273438,0,0.3518218994140625,0,0.3618545532226562,0,0.3712844848632812,0,0.3837509155273438,0.2848129272460938,0,0,0,0,0,-2.837661743164062,0,0.2495803833007812,0.2791519165039062,0,0.3088531494140625,0,0.3367080688476562,0,0.3490142822265625,0,0.3588790893554688,0,0.373077392578125,0,0.385284423828125,0.2835845947265625,0,0,0,0,0,-2.764747619628906,0,0.251739501953125,0.279571533203125,0,0.3158950805664062,0.3415985107421875,0,0,0.3491744995117188,0,0.360992431640625,0,0.3775863647460938,0,0.3860702514648438,0,0.187103271484375,0,0,0,-2.698051452636719,0,0.2535629272460938,0,0.2841873168945312,0.318939208984375,0,0.340301513671875,0.3503952026367188,0,0.3619842529296875,0,0.3733978271484375,0,0.38067626953125,0.1183853149414062,0,0,-2.839279174804688,0,0.234100341796875,0,0.2539520263671875,0,0.287200927734375,0,0.3234176635742188,0,0.34521484375,0.355133056640625,0,0.3513336181640625,0.381256103515625,0,0.3899154663085938,0,0,0,0,0,-2.706184387207031,0,0.2430648803710938,0,0.271453857421875,0,0.3072357177734375,0,0.3375091552734375,0.3479461669921875,0,0.3602066040039062,0,0.3715438842773438,0,0.3868637084960938,0,0.1614532470703125,0,0,-2.772804260253906,0,0.2329254150390625,0.2584304809570312,0,0.2898635864257812,0.3223876953125,0,0.3445968627929688,0,0.3541259765625,0,0.3718185424804688,0,0.3837814331054688,0,0.29449462890625,0,0,0,0,0,-2.587295532226562,0.2486190795898438,0,0.27587890625,0.3151016235351562,0,0.340179443359375,0.350677490234375,0,0,0.3600540161132812,0.3730621337890625,0,0.3883743286132812,0,0.01383209228515625,0,0,-2.607666015625,0.2402496337890625,0,0.2665252685546875,0,0.3340606689453125,0.33416748046875,0,0.3506622314453125,0.3598480224609375,0,0,0.3720245361328125,0,0.3878173828125,0,0.0394439697265625,0,0,-2.585777282714844,0,0.2324676513671875,0,0.2611236572265625,0,0.2970657348632812,0,0.3276214599609375,0,0,0.34710693359375,0,0.35284423828125,0,0.3693771362304688,0.3819122314453125,0.0921173095703125,0,-2.584732055664062,0.2294540405273438,0.2586517333984375,0.2914657592773438,0,0.3246307373046875,0,0.3420257568359375,0,0.3430557250976562,0,0,0.3643341064453125,0.3758010864257812,0.1300430297851562,0,0,0,0,0,-2.351837158203125,0,0,0.2715988159179688,0.2853240966796875,0.3141021728515625,0,0.3414764404296875,0,0.3495712280273438,0,0,0.3576889038085938,0.37774658203125,0,0.1277542114257812,0,0,0,0,0,-2.306465148925781,0,0.25213623046875,0.275848388671875,0,0.3206100463867188,0,0.3430633544921875,0,0,0.3489990234375,0,0.3614959716796875,0,0.3788528442382812,0,0.097747802734375,0,0,0,-2.464202880859375,0.22998046875,0,0.2546463012695312,0,0.2893295288085938,0.323577880859375,0.3464126586914062,0,0.35638427734375,0,0.3693771362304688,0,0.3655776977539062,0,0,0,-2.373931884765625,0,0.2556686401367188,0.2698287963867188,0,0.3086471557617188,0.3381576538085938,0,0.3516387939453125,0,0.363189697265625,0.3740463256835938,0,0.1827850341796875,0,0,0,-2.209587097167969,0.24859619140625,0,0,0.2747268676757812,0.3180313110351562,0,0.33917236328125,0,0.35125732421875,0.36492919921875,0.3805389404296875,0,0.0010986328125,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2.341140747070312,0,0.18511962890625,0,0.2407913208007812,0,0.2212142944335938,0.2644577026367188,0,0.2967300415039062,0,0.3267898559570312,0.3425216674804688,0,0.3492050170898438,0.181793212890625,0,0,0,-2.148963928222656,0,0,0.2430343627929688,0,0.2777557373046875,0.3129425048828125,0.3431625366210938,0,0.3509521484375,0,0.3647079467773438,0.3230514526367188,0,0,0,-2.187889099121094,0,0.23480224609375,0,0.2644882202148438,0,0.3026885986328125,0,0.335235595703125,0.35205078125,0,0.3616561889648438,0,0.3744659423828125,0.02809906005859375,0,0,-2.200408935546875,0,0.2298507690429688,0,0.2832107543945312,0,0.2979736328125,0,0,0.3306350708007812,0.345489501953125,0,0.3530807495117188,0,0.3681106567382812,0,0,0.05654144287109375,0,-2.187957763671875,0.2285614013671875,0,0.2546234130859375,0.2859573364257812,0.3309860229492188,0,0.3462371826171875,0,0.354766845703125,0,0.3740997314453125,0,0.07621002197265625,0,0,-2.157455444335938,0,0.2300491333007812,0,0,0.2570953369140625,0,0.2951202392578125,0,0.3276519775390625,0,0.3326644897460938,0,0.3441619873046875,0.3565673828125,0,0.076629638671875,0,0,-2.130584716796875,0,0.2275924682617188,0.251983642578125,0.2886810302734375,0,0.3239059448242188,0.349273681640625,0.3564910888671875,0,0.37481689453125,0.019256591796875,0,-2.055877685546875,0.2309188842773438,0,0.2584381103515625,0,0.2853164672851562,0,0.3204193115234375,0,0.3423538208007812,0,0.390594482421875,0.2883224487304688,0,0,0,0,0,-1.967193603515625,0.2333831787109375,0.2639007568359375,0,0.30426025390625,0,0.33599853515625,0.3529205322265625,0,0.363372802734375,0.1728591918945312,0,0,0,0,0,-1.862068176269531,0,0.2226791381835938,0.2620086669921875,0,0,0.2993392944335938,0.3324203491210938,0.3470230102539062,0.3500900268554688,0,0.1070404052734375,0,0,0,0,0,-1.792503356933594,0,0.2181472778320312,0,0.2695693969726562,0,0.309417724609375,0.3215408325195312,0,0.3835906982421875,0,0.3477935791015625,0,0,0,0,0,-1.958229064941406,0,0.22601318359375,0.24041748046875,0,0.27392578125,0,0.3116226196289062,0,0.33868408203125,0,0.324859619140625,0.2993316650390625,0,0,0,0,0,-1.88006591796875,0,0.2306671142578125,0.2601394653320312,0,0.2774658203125,0,0.3150100708007812,0.3459701538085938,0,0.355865478515625,0.1507339477539062,0,0,0,0,0,-1.788864135742188,0.2453765869140625,0.2571182250976562,0,0.2948379516601562,0,0.321502685546875,0.3458328247070312,0,0.3495330810546875,0,0.02947235107421875,0,0,-1.880577087402344,0,0.212310791015625,0,0.2455596923828125,0.276153564453125,0,0.3205718994140625,0.3482131958007812,0.3563385009765625,0,0.1753463745117188,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.809539794921875,0,0.2105712890625,0.2348556518554688,0.2596969604492188,0,0.2980880737304688,0,0.3629074096679688,0,0.3453750610351562,0.1510238647460938,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.826644897460938,0,0,0.0388336181640625,0.2453765869140625,0.2620315551757812,0.2935943603515625,0,0,0.3253097534179688,0,0.3306198120117188,0,0.3241043090820312,0,0.362579345703125,0.3988571166992188,0,0.4085693359375,0.3555145263671875,0.3363189697265625,0,0.3359909057617188,0,0.335845947265625,0,0.3350448608398438,0,0.334869384765625,0.3344039916992188,0.3360443115234375,0.3362045288085938,0.335968017578125,0.336212158203125,0,0.3360595703125,0,0.33447265625,0,0.216522216796875,0,0,0,0,0,-7.157646179199219,0.2704086303710938,0.3059768676757812,0,0.3336334228515625,0.3357925415039062,0.3307876586914062,0,0.3693161010742188,0.3806533813476562,0,0.3901519775390625,0.3986358642578125,0,0.4018173217773438,0,0.4043655395507812,0.4059371948242188,0.4023056030273438,0.4043045043945312,0.40460205078125,0,0,0.402862548828125,0,0.402740478515625,0,0.403045654296875,0.3868255615234375,0.231048583984375,0,0,0,0,0,-7.085433959960938,0,0.255523681640625,0.2810821533203125,0,0,0.3170852661132812,0,0.3212814331054688,0,0.3227005004882812,0,0,0.3632278442382812,0,0.3715438842773438,0.3838882446289062,0,0,0.3739166259765625,0,0.4272842407226562,0.38885498046875,0,0.39166259765625,0,0.3988113403320312,0.3971633911132812,0,0.3990859985351562,0.4012603759765625,0,0.403472900390625,0.4051055908203125,0.3924942016601562,0.294189453125,0,0,0,0,0,-7.013496398925781,0,0.2511444091796875,0.2663040161132812,0,0.2999343872070312,0.3079605102539062,0.3227005004882812,0.350006103515625,0.361480712890625,0,0.3733062744140625,0.3828353881835938,0,0.3906173706054688,0,0.3918380737304688,0,0.3901290893554688,0.398681640625,0.3998565673828125,0,0.40008544921875,0,0.3987197875976562,0,0.4008026123046875,0,0.4025421142578125,0.3931884765625,0,0.33233642578125,0,0,0,0,0,-6.699409484863281,0,0.2921829223632812,0,0.2939300537109375,0,0.3001022338867188,0,0.3297500610351562,0.356719970703125,0,0.3633651733398438,0,0.3767242431640625,0,0.3814849853515625,0,0.3902587890625,0,0.3910903930664062,0.3882369995117188,0,0,0.3876571655273438,0.3953018188476562,0,0.3967437744140625,0,0.3991928100585938,0,0.3990325927734375,0,0.4013290405273438,0,0.3876800537109375,0.2662582397460938,0,0,0,-6.793060302734375,0.2469863891601562,0.2632980346679688,0,0.2841567993164062,0,0.2923202514648438,0,0.3411407470703125,0,0.3564071655273438,0.3615875244140625,0.3717269897460938,0.3816070556640625,0,0.3855133056640625,0,0.3871612548828125,0,0.3868560791015625,0.3857650756835938,0.3886337280273438,0,0,0.3919906616210938,0.398040771484375,0,0.4017791748046875,0.4033203125,0.3884429931640625,0,0.1708984375,0,0,0,-6.60284423828125,0.2504196166992188,0,0.2695159912109375,0.2809524536132812,0,0.3140869140625,0,0.3487396240234375,0.3581466674804688,0.3631210327148438,0.3756027221679688,0,0,0.3781814575195312,0.38250732421875,0,0,0.3886566162109375,0,0.3899383544921875,0,0.3837356567382812,0,0.3888397216796875,0.3917236328125,0,0.4012680053710938,0,0.4018707275390625,0,0.3932647705078125,0,0.333587646484375,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-6.584739685058594,0,0,0,0.2268142700195312,0.2704315185546875,0,0,0.2548370361328125,0.2796554565429688,0,0.3227081298828125,0,0.3284912109375,0,0.3363876342773438,0,0,0.3524017333984375,0.379913330078125,0.3898468017578125,0,0.3918228149414062,0,0.3913116455078125,0.3964004516601562,0,0.3951950073242188,0,0.3991851806640625,0,0.3995819091796875,0,0,0.4006195068359375,0,0,0.401458740234375,0,0.3998260498046875,0.0560760498046875,0,0,0,0,0,-6.346733093261719,0.2492828369140625,0,0.2595977783203125,0.27947998046875,0,0.326751708984375,0,0,0.342864990234375,0,0.3467636108398438,0,0.3540878295898438,0,0.3652191162109375,0.37060546875,0.3795547485351562,0.3777313232421875,0,0.3861007690429688,0,0.3872909545898438,0,0.3888092041015625,0,0.39111328125,0,0.3932418823242188,0,0.4012069702148438,0,0.4012451171875,0,0.1309814453125,0,0,0,-6.2733154296875,0.2428054809570312,0,0.2476272583007812,0,0.2709579467773438,0.314453125,0.3338623046875,0.3423690795898438,0,0.3469009399414062,0.3602752685546875,0,0,0.3692092895507812,0,0.3777694702148438,0,0.3780441284179688,0.379852294921875,0,0.389068603515625,0,0.3923110961914062,0,0.3899765014648438,0.3925399780273438,0,0.4037551879882812,0,0.4037857055664062,0.1200180053710938,0,0,0,0,0,-6.188888549804688,0,0,0.2418212890625,0,0.24359130859375,0.2754974365234375,0,0.3166656494140625,0.3348464965820312,0,0.3424911499023438,0.3472671508789062,0,0.3587493896484375,0.3680953979492188,0,0.3774566650390625,0,0,0.3798904418945312,0,0.38470458984375,0.4310836791992188,0,0.3908004760742188,0,0,0.3918228149414062,0,0.3989105224609375,0,7.651519775390625,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7.62939453125,7.62939453125e-06,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,15.2587890625,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7.667304992675781,0,0,0,0,0,0,0,0,15.35730743408203,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"filename":["<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,null,null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,null,"<expr>","<expr>","<expr>",null,null,null,null,"<expr>","<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,null,null,null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,null,null,null,null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,null,null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,null,null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,null,null,null,null,null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,null,null,null,"<expr>","<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null]},"interval":10,"files":[{"filename":"<expr>","content":"## Generate Large Random Dataset\nn <- 2e6\nx <- runif(n)\ny <- runif(n)\nz <- runif(n)\nXYZ <- cbind(x,y,z)\n\n## Inspect 4 equivalent `row mean` calculations \nprofvis::profvis({\n    m <- rowSums(XYZ)/ncol(XYZ)\n    m <- rowMeans(XYZ)\n    m <- apply(XYZ, 1, mean)\n    m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }\n})\n## rowSums(), colSums(), rowMeans(), and colMeans() are vectorised and fast.\n## for loop is not the slowest, but the ugliest.","normpath":"<expr>"}],"prof_output":"/tmp/RtmpfdIabG/file31951b6738a5.prof","highlight":{"output":["^output\\$"],"gc":["^<GC>$"],"stacktrace":["^\\.\\.stacktraceo(n|ff)\\.\\.$"]},"split":"h"}},"evals":[],"jsHooks":[]}</script>
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
## 1 mean1(x, 0.5)     20ms   22.7ms      44.3    7.63MB     2.01
## 2 mean2(x, 0.5)   19.3ms   22.1ms      45.9    7.63MB     0   
## 3 mean3(x, 0.5)   20.7ms     23ms      43.8    7.63MB     2.09
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
##   0.105   0.000   0.036
```

```r
system.time({ lm(Y~X, data=DAT) })
```

```
##    user  system elapsed 
##   0.478   0.001   0.166
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
## 1 ma1(y)      179.3ms  181.3ms      5.52    15.3MB     2.76
## 2 ma2(y)       23.2ms   23.2ms     43.1     91.6MB   646.
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
##   0.029   0.000   0.029
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
##   0.831   0.206   0.587
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



# Web Applications

[Shiny](https://shiny.posit.co/) is an R packag to build web applications.

Shiny Flexdashboards are nicely formatted Shiny Apps. While it is possible to use Shiny without the Flexdashboard formatting, I think it is easier to remember

* `.R` files are codes for statistical analysis
* `.Rmd` files are for communicating: reports, slides, posters, and apps


**Example: Histogram**
Download the source file [TrialApp1_Histogram_Dashboard.Rmd](https://jadamso.github.io/Rbooks/Templates/TrialApp1_Histogram_Dashboard.Rmd)
and open it with `rstudio`. Then run it with 

```r
rmarkdown::run('TrialApp1_Histogram_Dashboard.Rmd')
```

* Within the app, experiment with how larger sample sizes change the distribution. 

* Edit the app to let the user specify the number of breaks in the histogram. 

If you are having difficulty, you can try working first with the barebones shiny code. To do this, download [TrialApp0_Histogram.Rmd](https://jadamso.github.io/Rbooks/Templates/TrialApp0_Histogram.Rmd) and edit it in Rstudio. You can run the code with `rmarkdown::run('TrialApp0_Histogram.Rmd')`.


## More Literature

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

