# (PART) Reproducible Research in R {-} 


```r
knitr::opts_chunk$set(echo=TRUE, message=FALSE, warning=FALSE)
```

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
  * Google "worst excell errors" and note the frequency they arise from copy/paste via the "point-and-click" approach. Future economists should also read https://core.ac.uk/download/pdf/300464894.pdf.
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
<div class="plotly html-widget html-fill-item" id="htmlwidget-c9d28950339671541a68" style="width:672px;height:480px;"></div>
<script type="application/json" data-for="htmlwidget-c9d28950339671541a68">{"x":{"visdat":{"34b364ede5b3":["function () ","plotlyVisDat"]},"cur_data":"34b364ede5b3","attrs":{"34b364ede5b3":{"x":{},"y":{},"alpha_stroke":1,"sizes":[10,100],"spans":[1,20]}},"layout":{"margin":{"b":40,"l":60,"t":25,"r":10},"xaxis":{"domain":[0,1],"automargin":true,"title":"X"},"yaxis":{"domain":[0,1],"automargin":true,"title":"Y"},"hovermode":"closest","showlegend":false},"source":"A","config":{"modeBarButtonsToAdd":["hoverclosest","hovercompare"],"showSendToCloud":false},"data":[{"x":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100],"y":[1.8857438007536329,10.684495936578212,12.463906280484775,20.447629464001459,23.200752214896006,21.215618007028596,26.767845792443218,28.492271908012764,37.846062753873767,38.670535372797204,44.833681424244602,48.471281469120939,51.201950552539842,55.895701064935089,61.268455549712527,64.87657215789261,70.222813417335161,73.267427801232003,77.154644094173122,80.256473534363423,85.261587906178619,84.190722655719981,90.966291148230795,96.880428730537233,100.3990444276,103.49277587369222,107.77410533758858,110.2687316664467,113.92741245853399,123.01321982320538,124.29806897749158,126.52654833898535,130.61046133500099,136.97484096010234,138.58184911262131,140.22363970159094,146.8847717584965,149.82748509399926,153.8006941695721,159.17274976779782,162.5496612269485,168.34387868379244,170.20591728457148,176.96874680171783,179.59221979531358,180.53817542381745,191.71746555923812,191.04616451872056,196.26088100827303,199.70011856310637,204.54279746043287,205.8897455500327,213.67104471338359,215.93420146706615,217.7304045918786,228.46136619693431,222.49056604241659,233.66924947135234,240.92557623767888,240.64887443262526,245.36056288496448,245.0496475465747,252.77650367015622,251.70185488940481,258.31356140390398,264.32876355880006,265.6680026834868,273.33517307982129,276.19589343719383,280.45602622305364,284.27339686180272,290.73802155632285,288.24355977685457,298.47165888659367,299.94780623455307,305.97744269055312,306.65908013083776,314.04538859116877,318.33591123652235,319.39386001083318,327.28172112603471,326.62496067175749,333.87725149416991,338.19323275156091,340.56567884562736,344.77849883665669,349.69808658731483,350.89175464905685,355.89952806782048,362.97632477911793,364.31072417659067,369.20920432390028,370.51556107560219,375.10032486831602,377.56096195859095,384.99131430672884,387.11276652586162,391.97517778369655,395.04857594364256,400.28201381824499],"type":"scatter","mode":"markers","marker":{"color":"rgba(31,119,180,1)","line":{"color":"rgba(31,119,180,1)"}},"error_y":{"color":"rgba(31,119,180,1)"},"error_x":{"color":"rgba(31,119,180,1)"},"line":{"color":"rgba(31,119,180,1)"},"xaxis":"x","yaxis":"y","frame":null}],"highlight":{"on":"plotly_click","persistent":false,"dynamic":false,"selectize":false,"opacityDim":0.20000000000000001,"selected":{"opacity":1},"debounce":0},"shinyEvents":["plotly_hover","plotly_click","plotly_selected","plotly_relayout","plotly_brushed","plotly_brushing","plotly_clickannotation","plotly_doubleclick","plotly_deselect","plotly_afterplot","plotly_sunburstclick"],"base_url":"https://plot.ly"},"evals":[],"jsHooks":[]}</script>
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
* `MAKEFILE` explicitly describes and executes all codes (and typically logs the output).

**MAKEFILE**

If all code is written with the same program (such as R) the makefile can be written in a single language. For us, this looks like

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

Notice there is a lot of documentation `### like this`, which is crucial for large projects. Also notice that anyone should be able to replicate the entire project by downloading a zip file and simply changing `home_dir`.


If some folders or files need to be created, you can do this within R

```r
# list the files and directories
list.files(recursive=TRUE, include.dirs=TRUE)
# create directory called 'Data'
dir.create('Data')
```

## Logging/Sinking

When executing the makefile, you can also log the output. Either by 

1. Inserting some code into the makefile that logs/sinks the output 

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

In R, you use multiple functions on different types of data objects. Moreover, you "typically solve complex problems by decomposing them into simple functions, not simple objects." (H. Wickham)


We can use the following packages to help deal with various problems that may arise

```r
library(microbenchmark)
library(compiler)
library(profvis)
library(parallel)
library(Rcpp)
```

Problems print to the console

```r
message("This is what a message looks like")

warning("This is what a warning looks like")

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

###  Tracing 

Consider this example of an error process (originally taken from https://adv-r.hadley.nz/ ).

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

First try simple print debugging

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

If that fails, try traceback debugging

```r
traceback()
```

```
## No traceback available
```

And if that fails, try an Interactive approach

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



###  Isolating

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

### Handling

Simplest Example

```r
x <- 'A'
tryCatch(
  expr = log(x),
  error = function(e) {
        message('Caught an error but did not break')
        print(e)
        return(NA)
})
```

Simple Example

```r
x <- -2
tryCatch(
  expr = log(x),
  error = function(e) {
        message('Caught an error but did not break')
        print(e)
        return(NA)
    },
    warning = function(w){
        message('Caught a warning!')
        print(w)
        return(NA)        
    },
    finally = {
        message("Returned log(x) if successfull or NA if Error or Warning")
    }
)
```

```
## <simpleWarning in log(x): NaNs produced>
```

```
## [1] NA
```

<!--## Ignore warnings/messages
    Supressing errors is possible but a bad idea
    
    ```r
    try(1+2, silent=T)
    ```
    
    ```
    ## [1] 3
    ```
    
    ```r
    try(warning('warning'), silent=T)
    try(error('error'), silent=T)
    
    try(1+2, silent=F)
    ```
    
    ```
    ## [1] 3
    ```
    
    ```r
    try(warning('warning'), silent=F)
    try(error('error'), silent=F)
    ```
    
    ```
    ## Error in error("error") : could not find function "error"
    ```
    
    ```r
    #suppressMessages()    
    ```
-->

Safe Functions

```r
## Define
log_safe <- function(x){
    lnx <- tryCatch(
        expr = log(x),
        error = function(e){
            cat('Error Caught: \n\t')        
            print(e)
            return(NA)            
        },
        warning = function(w){
            cat('Warning Caught: \n\t')
            print(w)
            return(NA)            
        })
    return(lnx)
}

## Test 
log_safe( 1)
```

```
## [1] 0
```

```r
log_safe(-1)
```

```
## Warning Caught: 
## 	<simpleWarning in log(x): NaNs produced>
```

```
## [1] NA
```

```r
log_safe(' ')
```

```
## Error Caught: 
## 	<simpleError in log(x): non-numeric argument to mathematical function>
```

```
## [1] NA
```

```r
## Further Tests
s <- sapply(list("A",Inf, -Inf, NA, NaN, 0, -1, 1), log_safe)
```

```
## Error Caught: 
## 	<simpleError in log(x): non-numeric argument to mathematical function>
## Warning Caught: 
## 	<simpleWarning in log(x): NaNs produced>
## Warning Caught: 
## 	<simpleWarning in log(x): NaNs produced>
```

```r
s
```

```
## [1]   NA  Inf   NA   NA  NaN -Inf   NA    0
```



## Optimizing 

In General: Clean code is often faster and less error prone

*Repetitive tasks can be optimized* You end up with code that

* is cleaner, faster, and more general
* can be easily parallelized

*Computers have big memories and are really good at math.*

* First try vectors
* Then try `apply` functions
* See https://uscbiostats.github.io/software-dev-site/handbook-slow-patterns.html

*Don't waste time on code that is not holding you back.*

* Your code may break, be slow, or incorrect.
* Look at what has already done.


###  Benchmarking

The simplest approach is to time how long a code-chunk runs

```r
system.time({
    x <- runif(1e5)
    sqrt(x)
})
```

```
##    user  system elapsed 
##   0.005   0.001   0.006
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
<div class="profvis html-widget html-fill-item" id="htmlwidget-c9810a4996aa1353f521" style="width:100%;height:600px;"></div>
<script type="application/json" data-for="htmlwidget-c9810a4996aa1353f521">{"x":{"message":{"prof":{"time":[1,2,3,4,5,6,6,7,8,9,10,11,12,12,12,13,13,14,14,15,15,16,16,17,17,18,18,19,19,20,20,21,21,22,22,23,23,24,24,25,25,26,26,27,27,28,29,29,30,30,30,31,32,33,33,33,34,34,35,35,36,37,38,39,40,40,41,41,42,42,42,43,43,44,44,45,45,46,47,47,48,48,49,50,50,51,52,52,53,53,54,54,55,55,56,56,56,57,57,58,58,59,59,59,60,60,61,62,62,63,63,64,64,65,66,67,68,69,70,70,70,70,71,72,72,73,73,73,74,74,75,75,76,76,76,77,78,78,79,79,80,80,81,81,82,83,83,83,84,84,84,85,86,86,87,87,88,89,89,90,91,91,92,93,93,94,94,94,95,95,96,96,97,97,97,98,98,99,99,100,101,101,101,102,102,103,103,104,104,105,105,106,106,107,107,108,108,109,110,110,110,111,111,112,112,113,114,114,115,116,117,118,118,119,119,120,121,121,122,122,123,123,123,124,124,124,125,125,126,126,127,127,128,128,128,129,129,130,130,131,132,132,133,133,134,134,135,135,136,136,136,137,138,138,139,140,140,140,141,142,143,144,145,146,147,147,148,148,149,149,150,150,151,151,152,152,153,153,154,154,155,156,157,158,159,160,160,161,161,162,162,163,163,164,165,165,165,166,166,167,167,168,169,169,169,170,170,171,172,172,173,174,174,174,175,175,176,176,176,177,177,178,178,178,179,180,180,180,181,182,182,183,183,184,185,186,186,187,187,187,188,189,189,190,191,191,192,193,194,194,195,195,196,196,196,197,197,198,198,199,199,200,201,201,202,202,203,204,204,205,205,206,207,207,208,208,209,210,210,211,212,212,213,213,214,214,215,216,216,217,217,218,218,219,219,219,220,220,221,222,222,223,223,223,224,224,224,225,225,225,226,226,226,227,228,229,229,230,230,231,231,232,232,233,234,235,235,236,236,237,237,237,238,238,239,239,240,241,241,242,243,244,245,246,247,247,248,248,249,249,250,250,251,251,251,252,252,253,253,253,254,254,255,255,256,256,257,258,259,260,261,261,262,262,263,264,265,265,266,267,267,268,268,269,269,270,271,271,272,272,273,273,274,274,275,276,277,277,278,279,279,280,280,281,281,282,282,283,283,284,284,284,285,286,286,287,287,288,289,289,290,291,291,292,292,293,293,294,294,294,295,295,295,296,296,296,297,297,297,298,298,298,299,299,299,300,300,300,301,301,301,302,302,302,303,303,303,304,304,304,305,305,306,306,307,307,308,309,309,310,311,311,312,312,313,313,314,315,315,316,316,316,317,318,319,319,320,320,321,321,322,322,323,323,324,325,326,327,327,327,328,328,328,329,329,330,330,331,332,333,334,335,336,336,337,337,337,338,338,338,339,340,340,341,342,342,343,343,344,344,345,345,346,346,347,348,349,349,349,350,350,351,351,352,352,353,354,354,355,355,356,356,357,358,358,359,359,359,360,360,360,361,362,363,364,364,365,366,366,367,367,368,369,370,370,370,371,371,372,372,373,373,374,375,375,376,376,377,378,378,379,379,380,380,380,381,381,382,383,383,384,385,385,385,386,387,387,388,388,389,390,390,390,391,391,392,392,393,394,394,395,395,396,396,397,397,397,398,398,398,399,399,399,400,400,400,401,402,402,403,403,404,404,405,405,406,406,407,407,408,408,409,409,410,410,411,411,412,412,412,413,413,414,414,415,415,416,416,417,417,418,418,418,419,419,419,419,420,420,420,420,421,422,422,423,424,424,425,425,426,427,427,428,428,429,429,430,430,431,432,432,433,433,434,434,435,436,436,436,437,438,438,438,439,439,439,440,440,441,441,442,442,443,444,444,445,445,446,447,447,448,448,449,449,450,451,451,452,452,453,453,453,454,454,455,455,456,457,457,457,458,459,459,460,461,461,462,462,463,463,464,464,465,465,466,466,467,468,469,470,470,471,472,472,473,473,474,475,475,475,476,476,476,477,477,478,478,479,479,480,480,481,481,482,483,484,484,484,484,485,485,486,486,487,488,488,489,490,490,491,491,492,492,493,493,493,494,494,495,496,496,497,497,498,498,499,499,500,500,501,501,502,502,503,504,505,506,506,507,507,508,508,509,509,509,510,510,510,511,511,511,512,512,512,513,513,513,514,514,514,515,515,515,516,516,516,517,517,517,518,518,518,519,519,519,520,520,520,521,521,521,522,522,522,523,523,523,524,524,524,525,525,525,526,526,526,527,527,527,528,528,528,529,529,529,530,530,530,531,531,531,532,532,532,533,533,533,534,534,534,535,535,535,536,536,536,537,537,537,538,538,538,539,539,540,541,542,543,544,544,545,545,546,547,548,548,549,549,550,550,550,551,551,551,552,552,552,553,553,554,554,555,555,556,556,557,557,557,558,558,559,560,561,561,562,562,562,563,563,563,564,565,565,566,566,567,567,568,568,569,569,570,571,571,572,573,574,574,574,575,575,576,576,577,577,578,578,579,580,581,581,582,582,583,583,584,584,584,585,585,585,586,586,587,587,588,589,589,590,590,591,591,591,592,592,593,593,594,594,595,595,596,596,597,598,598,599,599,600,600,601,601,602,602,603,603,603,604,604,605,605,606,606,606,607,608,608,609,609,610,610,611,612,613,613,614,614,614,615,615,616,617,618,619,619,620,620,621,622,622,623,624,625,626,626,627,627,627,628,628,628,629,629,630,630,631,631,632,632,633,634,634,635,635,635,636,636,636,637,637,637,638,638,639,639,640,641,641,642,642,643,643,644,645,646,646,647,648,648,649,649,650,650,651,651,652,652,653,654,654,655,655,656,657,658,658,659,659,660,660,661,661,661,662,663,664,664,665,666,667,667,668,668,669,669,669,670,670,670,671,671,671,672,673,674,674,674,675,675,676,676,677,678,679,679,680,680,680,681,681,682,683,684,684,685,686,686,687,688,689,689,690,690,690,691,691,691,692,692,693,694,695,695,696,696,696,697,698,699,699,700,700,701,701,702,703,704,705,706,706,707,707,708,709,709,710,710,711,711,712,712,713,713,714,714,715,716,716,717,718,718,718,719,719,720,720,721,721,721,722,722,723,724,724,725,725,726,726,727,727,728,728,729,730,731,731,732,732,732,732,733,733,733,733,734,735,735,736,736,737,738,739,739,740,740,741,741,742,743,743,744,745,745,746,747,747,748,748,748,749,749,750,750,750,751,751,752,752,752,753,753,753,754,754,755,755,756,756,757,758,758,759,759,759,760,760,761,761,762,762,763,764,765,765,766,767,768,769,769,770,771,771,772,772,772,773,773,773,774,774,775,775,776,776,777,778,778,779,779,779,780,781,781,782,783,783,784,785,785,786,786,787,787,788,789,790,790,790,791,791,792,792,793,794,794,794,795,795,795,796,796,797,798,799,799,800,800,801,801,802,802,803,803,804,804,805,805,806,806,806,807,808,808,809,809,810,810,811,811,812,812,813,814,814,815,815,816,816,817,817,818,818,819,820,821,821,822,823,823,824,824,825,826,826,827,828,828,829,829,830,830,831,832,833,833,834,834,834,835,835,835,836,837,838,838,839,840,840,841,841,842,842,843,843,844,844,845,845,846,847,847,848,848,849,849,850,850,851,851,852,852,853,853,853,854,854,854,855,856,857,857,858,859,860,861,861,862,863,863,864,865,865,866,866,867,867,868,869,869,870,870,871,872,872,872,873,873,873,874,874,874,875,876,876,877,878,879,880,881,881,882,882,883,884,884,885,885,886,886,886,887,887,888,888,889,889,889,890,890,891,891,892,892,893,894,895,895,896,896,897,898,899,899,900,900,901,902,903,903,904,904,905,905,906,906,907,908,908,908,909,909,910,910,910,910,911,911,911,911,912,913,913,914,915,915,915,916,916,917,917,918,919,919,920,921,921,922,922,923,923,924,925,925,926,926,927,927,928,929,929,929,930,930,930,931,932,932,933,933,934,935,935,936,936,937,937,938,938,938,939,939,940,940,941,941,941,942,942,943,943,944,945,945,946,947,947,947,948,948,948,949,949,950,950,951,951,952,953,953,954,954,955,956,956,957,957,958,958,959,960,960,961,961,962,963,963,964,964,965,965,965,966,966,966,967,967,967,968,968,968,969,969,969,970,970,970,971,971,971,972,972,972,973,973,973,974,974,974,975,975,975,976,976,976,977,977,977,978,978,978,979,979,979,980,980,980,981,981,982,982,982,983,983,984,984,985,986,986,987,987,988,988,989,990,990,991,991,992,993,993,994,995,995,996,996,997,997,997,998,998,998,999,999,1000,1000,1001,1002,1002,1003,1003,1004,1004,1005,1005,1006,1006,1007,1007,1008,1009,1009,1010,1010,1011,1012,1012,1013,1013,1014,1014,1015,1015,1016,1016,1017,1018,1018,1019,1020,1020,1021,1022,1022,1023,1024,1024,1025,1025,1026,1026,1027,1027,1028,1028,1029,1029,1030,1031,1031,1031,1032,1032,1032,1033,1033,1033,1034,1035,1035,1036,1036,1037,1037,1038,1039,1039,1040,1040,1041,1041,1041,1042,1042,1043,1043,1044,1044,1045,1045,1045,1046,1046,1047,1047,1048,1048,1048,1049,1049,1049,1050,1051,1051,1051,1052,1053,1054,1054,1055,1056,1056,1056,1057,1057,1057,1058,1058,1059,1059,1060,1060,1061,1061,1062,1062,1063,1063,1064,1065,1065,1066,1066,1067,1067,1068,1068,1068,1069,1069,1069,1070,1070,1071,1071,1072,1072,1073,1073,1074,1074,1075,1075,1076,1077,1077,1078,1078,1079,1080,1080,1080,1081,1081,1081,1082,1082,1082,1083,1083,1084,1084,1085,1085,1086,1086,1087,1087,1088,1088,1089,1089,1090,1090,1091,1091,1092,1092,1093,1093,1094,1094,1094,1095,1095,1095,1096,1097,1097,1098,1098,1099,1099,1100,1100,1101,1101,1102,1103,1103,1104,1105,1105,1106,1106,1107,1107,1107,1108,1109,1109,1110,1110,1111,1112,1112,1112,1113,1113,1114,1114,1115,1115,1116,1116,1116,1117,1117,1117,1118,1118,1118,1119,1119,1120,1121,1122,1122,1123,1124,1124,1125,1125,1125,1126,1126,1126,1127,1128,1128,1129,1129,1130,1131,1131,1132,1132,1133,1133,1134,1134,1135,1135,1136,1136,1137,1137,1138,1138,1138,1139,1140,1141,1142,1142,1142,1143,1143,1144,1145,1145,1146,1147,1147,1148,1149,1150,1150,1151,1151,1152,1152,1153,1153,1154,1154,1155,1156,1156,1157,1157,1158,1159,1160,1160,1161,1161,1162,1163,1164,1165,1166,1166,1167,1167,1167,1168,1168,1168,1169,1169,1170,1171,1171,1172,1173,1173,1174,1174,1175,1175,1176,1176,1176,1177,1178,1178,1179,1179,1180,1180,1181,1181,1182,1183,1183,1184,1184,1185,1185,1185,1186,1186,1187,1187,1188,1188,1188,1189,1189,1189,1190,1190,1191,1191,1192,1192,1192,1193,1194,1195,1196,1197,1197,1198,1199,1200,1200,1201,1202,1202,1203,1203,1203,1204,1204,1204,1205,1206,1206,1207,1207,1207,1208,1208,1209,1209,1210,1211,1212,1212,1213,1214,1215,1215,1216,1216,1217,1217,1218,1218,1219,1219,1220,1221,1221,1221,1222,1222,1222,1223,1223,1224,1224,1225,1225,1226,1227,1228,1229,1229,1230,1231,1231,1232,1232,1233,1233,1234,1234,1235,1236,1236,1236,1237,1237,1238,1239,1239,1240,1240,1241,1242,1243,1244,1244,1244,1245,1245,1246,1246,1247,1248,1248,1249,1249,1250,1250,1251,1251,1252,1253,1254,1254,1255,1256,1256,1256,1257,1257,1258,1259,1259,1260,1260,1261,1262,1262,1262,1263,1263,1263,1264,1264,1264,1265,1265,1266,1267,1267,1268,1268,1269,1270,1270,1271,1271,1272,1272,1273,1273,1274,1275,1275,1276,1276,1277,1277,1277,1278,1278,1278,1279,1279,1280,1281,1282,1283,1283,1284,1284,1285,1285,1286,1286,1287,1288,1288,1289,1290,1291,1291,1292,1292,1293,1293,1294,1294,1295,1296,1297,1297,1298,1299,1299,1300,1300,1301,1301,1302,1303,1304,1304,1305,1306,1306,1307,1307,1308,1308,1308,1309,1309,1309,1310,1310,1310,1311,1312,1313,1313,1314,1315,1316,1316,1317,1317,1318,1318,1318,1319,1319,1320,1320,1321,1321,1322,1322,1323,1324,1324,1324,1325,1325,1325,1326,1326,1326,1327,1327,1327,1328,1328,1328,1329,1329,1329,1330,1330,1330,1331,1331,1331,1332,1332,1332,1333,1333,1333,1334,1334,1334,1335,1335,1335,1336,1336,1336,1337,1337,1337,1338,1339,1339,1340,1341,1341,1342,1343,1344,1345,1345,1346,1346,1347,1347,1348,1348,1349,1349,1350,1350,1351,1352,1352,1352,1353,1353,1353,1354,1354,1355,1356,1357,1357,1358,1358,1359,1359,1360,1360,1361,1361,1362,1363,1364,1364,1365,1365,1366,1366,1367,1367,1368,1368,1369,1369,1370,1370,1371,1371,1372,1372,1373,1373,1374,1374,1375,1375,1376,1376,1377,1377,1378,1378,1379,1379,1380,1380,1380,1381,1381,1382,1382,1383,1383,1384,1384,1385,1386,1386,1387,1387,1388,1389,1389,1390,1390,1391,1392,1392,1393,1394,1394,1395,1395,1395,1396,1396,1396,1397,1397,1397,1398,1399,1400,1400,1400,1401,1401,1401,1402,1403,1403,1404,1405,1406,1407,1407,1408,1408,1408,1409,1409,1409,1410,1410,1410,1411,1411,1411,1412,1412,1413,1413,1414,1414,1414,1415,1416,1417,1417,1418,1418,1419,1419,1420,1421,1421,1421,1421,1422,1422,1422,1422,1423,1424,1424,1424,1425,1425,1426,1426,1427,1427,1427,1428,1428,1429,1429,1430,1430,1431,1432,1432,1433,1434,1434,1435,1435,1436,1436,1436,1437,1438,1439,1439,1440,1440,1441,1442,1442,1443,1444,1445,1445,1446,1446,1447,1447,1447,1448,1448,1448,1449,1449,1450,1450,1451,1452,1452,1452,1453,1453,1454,1455,1456,1457,1458,1458,1459,1460,1460,1461,1461,1462,1462,1463,1464,1464,1465,1465,1465,1466,1467,1467,1468,1468,1469,1470,1470,1471,1472,1473,1474,1474,1474,1475,1475,1475,1476,1476,1477,1477,1478,1479,1479,1480,1480,1481,1481,1482,1483,1484,1484,1485,1485,1486,1487,1487,1487,1488,1488,1488,1489,1489,1489,1490,1490,1491,1491,1492,1492,1493,1493,1494,1494,1495,1495,1496,1497,1498,1498,1499,1499,1500,1500,1501,1501,1502,1502,1503,1503,1504,1504,1504,1505,1505,1506,1506,1507,1507,1508,1508,1509,1509,1509,1510,1510,1511,1511,1512,1512,1513,1513,1513,1514,1514,1514,1515,1516,1516,1517,1518,1518,1519,1519,1520,1520,1521,1522,1523,1523,1524,1524,1524,1525,1525,1525,1526,1526,1526,1527,1528,1529,1530,1530,1531,1532,1532,1532,1533,1534,1535,1536,1536,1536,1537,1537,1537,1538,1538,1538,1539,1539,1539,1540,1540,1540,1541,1541,1541,1542,1542,1542,1543,1543,1543,1544,1544,1545,1546,1546,1547,1548,1548,1549,1549,1550,1550,1551,1551,1552,1553,1553,1554,1554,1555,1555,1556,1556,1557,1557,1557,1558,1558,1558,1559,1559,1559,1560,1560,1560,1561,1561,1561,1562,1562,1562,1563,1563,1563,1564,1564,1564,1565,1565,1565,1566,1566,1566,1567,1567,1567,1568,1568,1568,1569,1569,1569,1570,1570,1570,1571,1571,1571,1572,1572,1572,1573,1573,1573,1574,1574,1574,1575,1575,1575,1576,1576,1576,1577,1577,1577,1578,1578,1578,1579,1579,1579,1580,1580,1580,1581,1581,1581,1582,1582,1582,1583,1583,1583,1584,1584,1584,1585,1585,1585,1586,1586,1586,1587,1587,1587,1588,1588,1588,1589,1589,1589,1590,1590,1590,1591,1591,1591,1592,1592,1592,1593,1593,1593,1594,1594,1594,1595,1595,1595,1596,1596,1596,1597,1597,1597,1598,1598,1598,1599,1599,1599,1600,1600,1600,1601,1601,1601,1602,1602,1602,1603,1603,1603,1604,1604,1604,1605,1605,1605,1606,1606,1606,1607,1607,1607,1608,1608,1608,1609,1609,1609,1610,1610,1610,1611,1611,1611,1612,1612,1612,1613,1613,1613,1614,1614,1614,1615,1615,1615,1616,1616,1616,1617,1617,1618,1618,1619,1620,1620,1621,1622,1622,1623,1623,1624,1625,1625,1626,1626,1627,1627,1628,1628,1629,1630,1630,1631,1632,1632,1633,1633,1634,1635,1636,1636,1637,1637,1638,1638,1639,1640,1640,1641,1641,1642,1643,1644,1644,1645,1645,1646,1646,1647,1647,1648,1648,1649,1649,1650,1650,1651,1652,1652,1653,1654,1654,1655,1655,1656,1656,1657,1657,1658,1658,1658,1659,1659,1660,1661,1661,1662,1663,1664,1664,1665,1665,1666,1666,1667,1667,1668,1669,1669,1670,1671,1671,1672,1672,1673,1673,1674,1674,1675,1675,1676,1676,1677,1678,1678,1679,1679,1680,1680,1681,1682,1682,1683,1683,1684,1684,1685,1685,1686,1686,1687,1687,1688,1689,1689,1689,1690,1690,1690,1691,1691,1691,1692,1692,1692,1693,1694,1695,1695,1696,1696,1697,1698,1699,1699,1699,1700,1701,1701,1702,1702,1703,1704,1704,1705,1705,1705,1706,1706,1707,1708,1708,1709,1710,1710,1711,1711,1712,1712,1713,1713,1713,1714,1714,1715,1715,1716,1716,1717,1718,1718,1719,1720,1720,1721,1721,1722,1723,1723,1724,1725,1725,1725,1726,1726,1726,1727,1727,1727,1728,1728,1729,1729,1730,1731,1732,1732,1733,1734,1734,1734,1735,1736,1737,1737,1738,1738,1739,1739,1740,1740,1741,1741,1742,1742,1743,1743,1744,1744,1745,1746,1746,1747,1747,1748,1749,1749,1750,1751,1752,1752,1752,1753,1753,1754,1754,1755,1755,1756,1756,1757,1758,1758,1759,1760,1760,1760,1761,1761,1761,1762,1762,1762,1763,1763,1763,1764,1765,1766,1767,1767,1768,1768,1769,1769,1770,1770,1771,1771,1771,1772,1773,1773,1774,1774,1775,1776,1777,1778,1778,1779,1780,1780,1781,1781,1781,1782,1782,1783,1784,1784,1785,1785,1786,1786,1787,1787,1788,1789,1789,1790,1790,1791,1791,1792,1792,1793,1793,1794,1794,1795,1795,1795,1795,1796,1796,1796,1796,1797,1797,1797,1797,1798,1798,1798,1798,1799,1800,1800,1801,1801,1802,1803,1804,1805,1805,1806,1806,1807,1807,1808,1808,1809,1809,1810,1810,1810,1811,1812,1813,1813,1814,1814,1814,1815,1815,1816,1816,1817,1817,1818,1818,1819,1819,1819,1820,1821,1822,1822,1823,1823,1824,1824,1825,1826,1827,1827,1828,1828,1829,1829,1830,1830,1830,1831,1831,1831,1832,1832,1832,1833,1834,1834,1835,1835,1836,1836,1836,1837,1837,1838,1839,1840,1840,1841,1842,1842,1843,1843,1844,1844,1845,1845,1846,1847,1848,1849,1850,1850,1851,1851,1851,1852,1852,1853,1853,1854,1854,1855,1855,1856,1857,1857,1858,1859,1860,1861,1861,1862,1863,1864,1864,1865,1865,1866,1866,1867,1867,1868,1868,1869,1869,1870,1870,1871,1871,1872,1872,1873,1873,1874,1874,1875,1875,1876,1877,1878,1878,1879,1879,1880,1880,1881,1881,1882,1883,1884,1884,1885,1885,1885,1886,1886,1887,1887,1888,1888,1889,1889,1889,1890,1890,1891,1891,1892,1892,1893,1894,1895,1895,1896,1897,1898,1899,1899,1900,1901,1901,1902,1902,1902,1903,1903,1904,1904,1905,1905,1906,1907,1907,1907,1908,1908,1908,1909,1909,1909,1910,1910,1910,1911,1911,1912,1913,1913,1914,1914,1915,1916,1917,1918,1918,1919,1919,1920,1920,1921,1921,1922,1922,1923,1924,1925,1926,1926,1926,1927,1927,1928,1928,1929,1929,1929,1930,1931,1931,1932,1932,1933,1933,1934,1935,1935,1936,1937,1937,1938,1939,1939,1940,1941,1941,1941,1942,1942,1942,1943,1943,1943,1944,1944,1944,1945,1945,1946,1946,1947,1947,1948,1948,1949,1949,1950,1950,1951,1952,1952,1952,1953,1954,1954,1955,1956,1956,1957,1958,1958,1959,1959,1960,1960,1961,1961,1961,1962,1962,1963,1963,1964,1964,1965,1965,1966,1967,1967,1968,1968,1969,1969,1969,1970,1971,1971,1972,1972,1973,1973,1974,1974,1974,1975,1975,1975,1976,1976,1976,1977,1977,1977,1978,1979,1979,1980,1980,1981,1981,1982,1982,1983,1984,1984,1985,1985,1986,1987,1987,1988,1988,1989,1989,1990,1990,1991,1991,1992,1993,1993,1994,1995,1995,1996,1996,1997,1997,1998,1998,1999,1999,2000,2000,2001,2001,2002,2002,2003,2003,2004,2004,2005,2005,2006,2006,2007,2007,2008,2009,2009,2010,2010,2011,2011,2012,2012,2013,2013,2014,2014,2015,2015,2016,2016,2017,2017,2018,2018,2019,2019,2020,2020,2021,2021,2022,2022,2023,2023,2024,2024,2025,2025,2026,2026,2027,2027,2028,2028,2029,2029,2030,2030,2031,2031,2032,2032,2033,2033,2033,2033,2033,2033,2033,2033,2034,2034,2034,2034,2034,2034,2034,2034,2034,2034,2034,2034,2034,2034,2034,2035,2035,2035,2035,2035,2035,2035,2035,2036,2036,2036,2036,2036,2036,2036,2036,2037,2037,2037,2037,2037,2037,2037,2037,2038,2038,2038,2038,2038,2038,2038,2038,2039,2039,2039,2039,2039,2039,2039,2039,2040,2040,2040,2040,2040,2040,2040,2040,2041,2041,2041,2041,2041,2041,2041,2041,2042,2042,2042,2042,2042,2042,2042,2042,2043,2043,2043,2043,2043,2043,2043,2043,2044,2044,2044,2044,2044,2044,2044,2044,2045,2045,2045,2045,2045,2045,2045,2045,2046,2046,2046,2046,2046,2046,2046,2046,2047,2047,2047,2047,2047,2047,2047,2047,2048,2048,2048,2048,2048,2048,2048,2048,2049,2049,2049,2049,2049,2049,2049,2049,2050,2050,2050,2050,2050,2050,2050,2050,2051,2051,2051,2051,2051,2051,2051,2051,2052,2052,2052,2052,2052,2052,2052,2052,2053,2053,2053,2053,2053,2053,2053,2053,2054,2054,2054,2054,2054,2054,2054,2054,2055,2055,2055,2055,2055,2055,2055,2055,2056,2056,2056,2056,2056,2056,2056,2056,2057,2057,2057,2057,2057,2057,2057,2057,2058,2058,2058,2058,2058,2058,2058,2058,2059,2059,2059,2059,2059,2059,2059,2059,2060,2060,2060,2060,2060,2060,2060,2060,2061,2061,2061,2061,2061,2061,2061,2061,2062,2062,2062,2062,2062,2062,2062,2062,2063,2063,2063,2063,2063,2063,2063,2063,2064,2064,2064,2064,2064,2064,2064,2064],"depth":[1,1,1,1,1,2,1,1,1,1,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,1,1,3,2,1,2,1,2,1,1,1,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,2,1,1,1,1,1,1,4,3,2,1,1,2,1,3,2,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,1,2,1,2,1,1,2,1,1,2,1,1,2,1,3,2,1,2,1,2,1,3,2,1,2,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,1,2,1,1,1,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,1,3,2,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,1,1,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,1,3,2,1,2,1,1,2,1,1,3,2,1,2,1,3,2,1,2,1,3,2,1,1,3,2,1,1,2,1,2,1,1,1,2,1,3,2,1,1,2,1,1,2,1,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,1,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,1,1,1,1,1,2,1,2,1,2,1,2,1,3,2,1,2,1,3,2,1,2,1,2,1,2,1,1,1,1,1,2,1,2,1,1,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,1,2,1,3,2,1,1,1,2,1,2,1,2,1,2,1,2,1,1,1,1,3,2,1,3,2,1,2,1,2,1,1,1,1,1,1,2,1,3,2,1,3,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,3,2,1,3,2,1,1,1,1,2,1,1,2,1,2,1,1,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,1,2,1,1,3,2,1,1,2,1,2,1,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,4,3,2,1,4,3,2,1,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,3,2,1,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,2,1,1,3,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,1,2,1,1,2,1,2,1,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,1,4,3,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,1,1,1,1,2,1,2,1,1,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,1,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,1,3,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,1,1,2,1,3,2,1,2,1,1,1,1,2,1,2,1,1,2,1,1,1,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,1,2,1,2,1,2,1,3,2,1,1,1,2,1,1,1,2,1,2,1,3,2,1,3,2,1,3,2,1,1,1,3,2,1,2,1,2,1,1,1,2,1,3,2,1,2,1,1,1,2,1,1,2,1,1,1,2,1,3,2,1,3,2,1,2,1,1,1,2,1,3,2,1,1,1,2,1,2,1,2,1,1,1,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,3,2,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,4,3,2,1,4,3,2,1,1,2,1,2,1,1,1,2,1,2,1,2,1,1,2,1,1,2,1,1,2,1,3,2,1,2,1,3,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,1,1,2,1,1,1,1,2,1,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,3,2,1,1,2,1,1,2,1,1,2,1,2,1,2,1,1,1,3,2,1,2,1,2,1,1,3,2,1,3,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,1,1,2,1,3,2,1,3,2,1,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,1,1,2,1,1,1,1,2,1,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,1,3,2,1,3,2,1,3,2,1,1,2,1,1,1,1,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,1,2,1,2,1,1,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,4,3,2,1,4,3,2,1,1,2,1,1,3,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,3,2,1,3,2,1,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,3,2,1,3,2,1,1,3,2,1,1,1,2,1,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,3,2,1,1,2,1,2,1,1,3,2,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,1,1,2,1,1,2,1,3,2,1,3,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,1,1,3,2,1,2,1,1,2,1,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,1,2,1,2,1,1,1,1,1,2,1,3,2,1,3,2,1,2,1,1,2,1,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,3,2,1,1,1,1,1,2,1,1,1,2,1,1,2,1,3,2,1,3,2,1,1,2,1,3,2,1,2,1,2,1,1,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,2,1,2,1,2,1,1,1,1,2,1,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,1,2,1,2,1,1,1,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,1,2,1,1,3,2,1,2,1,1,2,1,2,1,1,3,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,2,1,1,1,1,2,1,2,1,2,1,2,1,1,2,1,1,1,2,1,2,1,2,1,2,1,1,1,2,1,1,2,1,2,1,2,1,1,1,2,1,1,2,1,2,1,3,2,1,3,2,1,3,2,1,1,1,2,1,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,1,2,1,1,2,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,1,2,1,1,2,1,3,2,1,3,2,1,3,2,1,1,1,3,2,1,3,2,1,1,2,1,1,1,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,3,2,1,1,1,2,1,2,1,2,1,1,4,3,2,1,4,3,2,1,1,3,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,3,2,1,1,1,2,1,2,1,1,2,1,1,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,1,3,2,1,2,1,1,1,1,1,2,1,1,2,1,2,1,2,1,1,2,1,3,2,1,1,2,1,2,1,1,2,1,1,1,1,3,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,1,1,2,1,2,1,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,3,2,1,3,2,1,1,2,1,1,2,1,2,1,2,1,1,1,2,1,3,2,1,3,2,1,3,2,1,1,1,1,2,1,1,3,2,1,1,1,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,1,1,2,1,2,1,2,1,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,1,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,3,2,1,3,2,1,1,1,2,1,2,1,1,1,3,2,1,1,2,1,2,1,1,2,1,3,2,1,2,1,1,2,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,1,2,1,1,3,2,1,3,2,1,3,2,1,2,1,2,1,1,1,2,1,1,3,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,1,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,1,3,2,1,3,2,1,3,2,1,3,2,1,1,1,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,1,1,1,2,1,1,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,1,2,1,2,1,1,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,3,2,1,1,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,1,2,1,2,1,3,2,1,2,1,1,1,2,1,1,2,1,2,1,2,1,2,1,1,1,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,1,1,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,1,1,2,1,3,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,1,2,1,1,1,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,1,1,1,2,1,2,1,2,1,2,1,2,1,1,1,1,3,2,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,1,2,1,1,2,1,1,2,1,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,1,2,1,1,2,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,8,7,6,5,4,3,2,1,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1],"label":["rowSums","rowSums","rowSums","rowSums","rowSums","/","local","rowMeans","rowMeans","rowMeans","rowMeans","rowMeans","<GC>","aperm.default","apply","aperm.default","apply","aperm.default","apply","aperm.default","apply","aperm.default","apply","aperm.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","apply","mean.default","apply","isTRUE","mean.default","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","apply","apply","apply","apply","length","local","FUN","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","mean.default","apply","FUN","apply","apply","length","local","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","length","local","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","apply","apply","apply","apply","<GC>","isTRUE","mean.default","apply","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","mean.default","apply","mean.default","apply","length","local","length","local","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","FUN","apply","apply","mean.default","apply","apply","mean.default","apply","apply","length","local","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","<GC>","mean.default","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","apply","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","<GC>","length","local","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","<GC>","mean.default","apply","apply","mean.default","apply","apply","isTRUE","mean.default","apply","apply","apply","apply","apply","apply","apply","mean.default","apply","mean.default","apply","<GC>","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","apply","apply","apply","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","<GC>","apply","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","apply","isTRUE","mean.default","apply","mean.default","apply","apply","mean.default","apply","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","isTRUE","mean.default","apply","apply","mean.default","apply","mean.default","apply","apply","apply","mean.default","apply","isTRUE","mean.default","apply","apply","<GC>","apply","apply","mean.default","apply","apply","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","<GC>","apply","<GC>","apply","apply","FUN","apply","FUN","apply","apply","mean.default","apply","FUN","apply","apply","FUN","apply","apply","FUN","apply","<GC>","apply","<GC>","apply","apply","FUN","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","<GC>","length","local","<GC>","length","local","apply","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","apply","apply","length","local","mean.default","apply","<GC>","length","local","mean.default","apply","FUN","apply","apply","mean.default","apply","apply","apply","apply","apply","apply","FUN","apply","FUN","apply","<GC>","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","apply","apply","apply","<GC>","apply","FUN","apply","apply","apply","mean.default","apply","apply","FUN","apply","FUN","apply","mean.default","apply","apply","FUN","apply","<GC>","apply","<GC>","apply","mean.default","apply","apply","apply","is.na","local","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","apply","is.numeric","local","mean.default","apply","apply","FUN","apply","apply","mean.default","apply","is.na","local","FUN","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","apply","FUN","apply","apply","mean.default","apply","FUN","apply","FUN","apply","apply","length","local","<GC>","FUN","apply","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","apply","apply","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","apply","apply","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","mean.default","apply","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","is.numeric","local","apply","apply","<GC>","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","FUN","apply","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","apply","apply","FUN","apply","apply","is.na","local","is.numeric","local","apply","apply","<GC>","FUN","apply","mean.default","apply","is.numeric","local","FUN","apply","apply","is.numeric","local","FUN","apply","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","FUN","apply","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","apply","<GC>","FUN","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","is.numeric","local","isTRUE","mean.default","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","<GC>","mean.default","apply","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","apply","FUN","apply","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","FUN","apply","<GC>","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","length","local","apply","isTRUE","mean.default","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","apply","FUN","apply","length","local","apply","<GC>","apply","<GC>","apply","FUN","apply","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","apply","<GC>","mean.default","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","<GC>","apply","apply","apply","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","is.numeric","local","apply","apply","<GC>","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","<GC>","is.na","local","FUN","apply","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","<GC>","apply","<GC>","apply","apply","apply","apply","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","apply","apply","apply","FUN","apply","FUN","apply","apply","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","apply","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","FUN","apply","is.numeric","local","FUN","apply","FUN","apply","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","apply","apply","FUN","apply","FUN","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","is.na","local","FUN","apply","FUN","apply","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","<GC>","is.numeric","local","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","apply","length","local","mean.default","apply","apply","mean.default","apply","apply","apply","apply","FUN","apply","<GC>","is.numeric","local","<GC>","is.numeric","local","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","apply","mean.default","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","is.na","local","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","mean.default","apply","apply","<GC>","apply","<GC>","apply","FUN","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","apply","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","apply","apply","FUN","apply","apply","mean.default","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","is.numeric","local","FUN","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","mean.default","apply","FUN","apply","FUN","apply","apply","apply","apply","apply","FUN","apply","FUN","apply","apply","is.na","local","mean.default","apply","<GC>","apply","<GC>","apply","mean.default","apply","FUN","apply","apply","is.numeric","local","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","apply","FUN","apply","length","local","length","local","mean.default","apply","FUN","apply","apply","apply","length","local","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","apply","FUN","apply","mean.default","apply","apply","apply","mean.default","apply","is.na","local","FUN","apply","apply","mean.default","apply","apply","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","apply","mean.default","apply","apply","apply","apply","length","local","apply","FUN","apply","<GC>","length","local","<GC>","length","local","FUN","apply","FUN","apply","is.numeric","local","apply","FUN","apply","isTRUE","mean.default","apply","apply","mean.default","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","apply","length","local","FUN","apply","apply","is.numeric","local","apply","FUN","apply","mean.default","apply","FUN","apply","apply","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","apply","mean.default","apply","apply","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","apply","FUN","apply","apply","apply","apply","FUN","apply","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","is.na","local","apply","FUN","apply","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","apply","mean.default","apply","apply","apply","apply","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","<GC>","apply","<GC>","apply","apply","apply","FUN","apply","FUN","apply","apply","apply","mean.default","apply","mean.default","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","apply","FUN","apply","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","apply","is.numeric","local","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","mean.default","apply","FUN","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","apply","mean.default","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","is.na","local","FUN","apply","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","is.numeric","local","FUN","apply","apply","is.na","local","mean.default","apply","apply","mean.default","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","is.numeric","local","is.numeric","local","apply","FUN","apply","mean.default","apply","FUN","apply","apply","is.na","local","FUN","apply","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","apply","FUN","apply","FUN","apply","<GC>","apply","<GC>","apply","is.na","local","apply","mean.default","apply","apply","is.na","local","apply","mean.default","apply","apply","mean.default","apply","is.numeric","local","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","mean.default","apply","FUN","apply","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","is.na","local","<GC>","FUN","apply","<GC>","FUN","apply","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","length","local","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","length","local","FUN","apply","mean.default","apply","FUN","apply","apply","length","local","mean.default","apply","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","is.numeric","local","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","<GC>","apply","<GC>","apply","mean.default","apply","apply","mean.default","apply","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","is.numeric","local","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","is.numeric","local","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","length","local","apply","apply","is.numeric","local","apply","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","apply","isTRUE","mean.default","apply","mean.default","apply","apply","FUN","apply","apply","FUN","apply","apply","apply","<GC>","apply","<GC>","apply","mean.default","apply","length","local","FUN","apply","apply","mean.default","apply","mean.default","apply","apply","apply","mean.default","apply","FUN","apply","apply","apply","apply","apply","FUN","apply","<GC>","is.na","local","<GC>","is.na","local","FUN","apply","apply","is.numeric","local","apply","FUN","apply","FUN","apply","is.numeric","local","isTRUE","mean.default","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","is.numeric","local","is.na","local","isTRUE","mean.default","apply","apply","apply","apply","apply","mean.default","apply","apply","apply","FUN","apply","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","length","local","mean.default","apply","apply","apply","FUN","apply","apply","apply","length","local","FUN","apply","FUN","apply","<GC>","apply","<GC>","apply","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","length","local","mean.default","apply","FUN","apply","apply","apply","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","<GC>","apply","<GC>","apply","apply","isTRUE","mean.default","apply","is.numeric","local","apply","mean.default","apply","mean.default","apply","apply","apply","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","apply","apply","mean.default","apply","apply","isTRUE","mean.default","apply","FUN","apply","apply","length","local","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","FUN","apply","is.numeric","local","apply","FUN","apply","FUN","apply","FUN","apply","length","local","apply","FUN","apply","FUN","apply","<GC>","length","local","<GC>","length","local","FUN","apply","apply","apply","apply","FUN","apply","length","local","mean.default","apply","FUN","apply","apply","mean.default","apply","apply","apply","FUN","apply","<GC>","apply","<GC>","apply","is.na","local","apply","apply","FUN","apply","apply","is.na","local","FUN","apply","FUN","apply","apply","apply","is.na","local","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","apply","FUN","apply","apply","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","mean.default","apply","apply","mean.default","apply","apply","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","is.na","local","mean.default","apply","apply","apply","is.numeric","local","FUN","apply","mean.default","apply","<GC>","apply","<GC>","apply","FUN","apply","length","local","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","is.numeric","local","isTRUE","mean.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","apply","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","length","local","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","mean.default","apply","apply","apply","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","apply","isTRUE","mean.default","apply","FUN","apply","length","local","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","isTRUE","mean.default","apply","apply","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","apply","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","mean.default","apply","apply","isTRUE","mean.default","apply","is.na","local","apply","apply","apply","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","length","local","apply","is.numeric","local","isTRUE","mean.default","apply","apply","mean.default","apply","FUN","apply","apply","FUN","apply","apply","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","mean.default","apply","apply","FUN","apply","length","local","FUN","apply","apply","apply","mean.default","apply","length","local","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","is.numeric","local","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","apply","apply","mean.default","apply","mean.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","length","local","isTRUE","mean.default","apply","mean.default","apply","is.na","local","length","local","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","FUN","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","apply","apply","mean.default","apply","apply","isTRUE","mean.default","apply","apply","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","mean.default","apply","length","local","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","is.numeric","local","mean.default","apply","apply","apply","FUN","apply","is.numeric","local","mean.default","apply","apply","FUN","apply","FUN","apply","apply","apply","mean.default","apply","FUN","apply","length","local","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","apply","mean.default","apply","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","is.numeric","local","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","apply","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","apply","isTRUE","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","apply","length","local","is.na","local","apply","apply","isTRUE","mean.default","apply","apply","FUN","apply","mean.default","apply","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","apply","mean.default","apply","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","apply","is.na","local","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","FUN","apply","apply","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","apply","mean.default","apply","FUN","apply","length","local","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","apply","isTRUE","mean.default","apply","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","apply","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","mean.default","apply","apply","apply","apply","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","length","local","is.na","local","FUN","apply","FUN","apply","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","apply","apply","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","mean.default","apply","FUN","apply","apply","apply","FUN","apply","FUN","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","length","local","apply","apply","FUN","apply","apply","mean.default","apply","FUN","apply","is.na","local","FUN","apply","apply","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","apply","apply","mean.default","apply","apply","apply","mean.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","apply","apply","mean.default","apply","FUN","apply","FUN","apply","is.na","local","apply","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","is.numeric","local","FUN","apply","apply","apply","FUN","apply","apply","apply","apply","is.numeric","local","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","apply","mean.default","apply","mean.default","apply","apply","apply","apply","mean.default","apply","length","local","FUN","apply","is.na","local","mean.default","apply","apply","apply","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","apply","FUN","apply","apply","FUN","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","length","local","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","mean.default","apply","apply","mean.default","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","apply","mean.default","apply","is.na","local","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","is.na","local","FUN","apply","is.na","local","FUN","apply","apply","is.numeric","local","FUN","apply","apply","FUN","apply","FUN","apply","length","local","FUN","apply","mean.default","apply","apply","mean.default","apply","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","cb$putcode","cmpSym","cmp","cmpPrim2","h","tryInline","cmpCall","cmp","h","tryInline","cmpCall","cmp","genCode","compile","compiler:::tryCompile","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis"],"filenum":[1,1,1,1,1,1,null,1,1,1,1,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,null,1,1,1,null,null,1,null,1,null,1,1,1,1,1,null,null,null,1,null,null,1,null,1,null,1,null,1,1,null,1,null,1,1,null,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,null,1,null,null,1,null,1,1,null,1,null,1,null,1,1,1,1,1,1,null,null,null,1,1,null,1,null,null,1,null,1,null,1,null,null,1,1,null,1,null,1,null,null,null,null,1,null,null,1,null,null,1,1,null,1,null,1,1,null,1,1,null,1,1,null,null,null,null,1,null,1,null,1,null,null,1,null,1,null,1,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,null,1,null,1,null,1,1,null,1,1,1,1,null,1,null,1,1,null,1,null,1,null,null,null,null,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,null,1,1,null,1,1,null,null,1,1,1,1,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,1,1,1,1,null,1,null,1,null,1,null,1,1,null,null,1,null,1,null,1,1,null,null,1,null,1,1,null,1,1,null,null,1,null,1,null,null,1,null,1,null,null,1,1,null,null,1,1,null,1,null,1,1,1,null,1,null,null,1,1,null,1,1,null,1,1,1,null,1,null,1,null,null,1,null,1,null,1,null,1,1,null,1,null,1,1,null,1,null,1,1,null,1,null,1,1,null,1,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,null,1,null,1,1,null,1,null,null,1,null,null,1,null,null,null,null,null,null,1,1,null,1,null,1,null,1,null,1,1,1,null,null,null,1,null,null,null,null,1,null,1,1,null,1,1,1,1,1,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,null,1,null,1,null,1,null,1,1,1,1,1,null,1,null,1,1,1,null,1,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,1,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,1,null,null,null,1,1,null,1,1,null,1,null,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,1,1,null,1,1,null,1,null,1,null,1,1,null,null,null,null,1,1,1,null,1,null,1,null,1,null,1,null,1,1,1,1,null,null,1,null,null,1,null,1,null,1,1,1,1,1,1,null,1,null,null,1,null,null,1,1,null,1,1,null,1,null,1,null,1,null,1,null,null,1,1,null,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,1,null,1,null,null,1,null,null,1,1,1,1,null,1,1,null,null,null,null,1,1,null,null,1,null,1,null,null,null,1,1,null,null,null,1,1,null,1,null,1,null,null,1,null,1,1,null,1,1,null,null,1,1,null,1,null,1,1,null,null,1,null,1,null,1,1,null,1,null,1,null,null,null,null,1,null,null,1,null,null,1,null,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,null,1,null,null,null,1,1,null,1,1,null,1,null,1,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,null,1,null,null,1,1,null,null,1,null,null,1,null,1,null,1,null,1,1,null,1,null,null,1,null,1,null,1,null,1,1,null,1,null,1,null,null,1,null,1,null,1,1,null,null,1,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,1,1,1,null,1,1,null,1,null,1,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,null,null,1,1,null,null,null,1,null,1,null,1,1,null,1,1,null,1,null,1,null,1,null,null,null,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,1,1,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,1,1,1,1,null,1,null,1,1,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,1,1,null,1,null,null,1,null,null,1,1,null,1,null,1,null,null,null,1,null,1,1,null,1,1,1,null,null,1,null,1,null,1,null,1,null,1,1,1,null,1,null,1,null,1,null,null,1,null,null,1,null,1,null,1,1,null,1,null,1,null,null,1,null,1,null,1,null,null,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,null,null,1,null,1,null,1,null,1,1,1,null,1,null,null,1,null,1,1,1,1,null,null,null,1,1,null,1,1,1,1,null,1,null,null,null,null,null,null,null,1,null,1,null,1,null,1,1,null,1,null,null,1,null,null,1,null,null,1,null,1,null,null,1,null,1,null,1,null,1,1,1,null,1,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,1,1,null,1,null,1,null,1,null,null,1,1,1,null,1,1,1,null,1,null,1,null,null,1,null,null,1,null,null,1,1,1,null,null,1,null,1,null,1,1,1,null,1,null,null,1,null,1,1,1,null,1,1,null,1,1,1,null,1,null,null,1,null,null,null,null,1,1,1,null,1,null,null,1,1,1,null,1,null,1,null,1,1,1,1,1,null,1,null,1,1,null,null,null,1,null,1,null,1,null,1,null,1,1,null,null,1,null,null,1,null,1,null,1,null,null,1,null,1,1,null,1,null,null,null,null,null,1,null,1,1,1,null,null,null,null,null,1,null,null,null,1,1,null,1,null,1,1,1,null,1,null,null,null,1,1,null,1,1,null,1,1,null,1,null,null,1,null,1,null,null,1,null,1,null,null,1,null,null,1,null,1,null,1,null,1,1,null,1,null,null,1,null,1,null,1,null,1,1,1,null,1,1,1,1,null,null,1,null,1,null,null,null,null,null,null,null,1,null,1,null,null,1,null,1,null,null,1,1,null,1,1,null,1,1,null,1,null,1,null,1,1,1,null,null,1,null,1,null,1,1,null,null,1,null,null,1,null,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,1,1,null,1,1,null,null,null,1,1,null,null,1,null,1,null,1,null,1,1,1,null,1,null,null,1,null,null,1,1,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,1,1,null,1,1,1,1,null,1,1,null,1,1,null,1,null,1,null,null,1,null,1,null,1,1,null,null,1,null,null,1,null,null,1,1,null,1,1,1,1,1,null,1,null,1,1,null,1,null,1,null,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,1,1,null,1,null,1,1,1,null,1,null,1,1,1,null,1,null,1,null,1,null,1,1,null,null,1,null,1,null,null,null,1,null,null,null,1,1,null,1,1,null,null,1,null,1,null,1,1,null,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,1,null,null,1,null,null,1,1,null,1,null,1,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,null,1,null,1,null,1,1,null,1,1,null,null,1,null,null,1,null,1,null,null,null,1,1,null,1,null,1,1,null,1,null,null,null,1,1,null,null,null,1,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,null,null,1,null,null,null,null,1,null,1,null,1,null,1,1,null,null,null,1,1,null,1,1,null,1,null,1,null,null,1,null,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,null,1,null,1,1,null,null,1,null,1,1,null,1,null,null,null,1,null,1,null,1,null,1,1,null,null,1,null,null,1,null,null,1,1,null,1,null,1,null,1,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,null,1,null,1,null,null,null,null,1,null,null,1,1,null,null,1,1,1,null,1,1,null,null,1,null,null,1,null,null,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,null,1,null,null,1,null,1,null,1,null,null,null,1,null,1,null,1,1,null,null,null,1,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,null,null,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,1,null,1,null,1,null,1,null,1,null,1,1,null,1,1,null,1,null,1,null,null,1,1,null,1,null,null,1,null,null,1,null,1,null,1,null,null,null,null,1,null,null,1,null,null,1,null,null,1,1,null,null,1,null,1,null,null,1,null,null,1,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,1,1,1,null,null,1,null,1,1,null,1,1,null,1,1,1,null,1,null,1,null,1,null,null,null,1,1,null,1,null,1,1,1,null,1,null,1,1,1,1,1,null,1,null,null,null,null,null,null,null,1,1,null,null,1,null,1,null,1,null,null,null,null,1,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,null,1,null,1,null,1,null,null,1,null,null,1,null,null,null,null,null,null,1,1,1,1,1,null,1,1,1,null,1,1,null,1,null,null,1,null,null,1,1,null,1,null,null,1,null,null,null,1,1,1,null,1,1,1,null,null,null,1,null,1,null,1,null,1,1,null,null,1,null,null,1,null,null,null,1,null,1,1,1,1,null,1,1,null,1,null,1,null,1,null,1,1,null,null,1,null,null,1,null,1,null,1,1,1,1,null,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,1,1,null,1,1,null,null,1,null,1,1,null,null,null,1,1,null,null,1,null,null,1,null,null,1,null,1,1,null,1,null,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,null,null,null,null,null,null,1,1,1,1,null,1,null,null,null,1,null,1,1,null,1,1,1,null,1,null,1,null,1,null,null,1,1,null,1,1,null,null,null,1,null,1,1,1,null,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,1,1,null,1,1,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,1,null,1,1,null,1,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,null,1,null,null,1,null,1,1,1,null,1,null,1,null,1,null,null,null,1,1,1,null,null,null,1,null,1,null,1,null,1,null,1,null,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,null,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,1,null,1,null,1,1,null,null,1,null,1,null,null,1,null,null,1,null,null,1,1,1,null,null,1,null,null,1,1,null,1,1,1,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,null,1,1,1,null,1,null,1,null,1,1,null,null,null,1,null,null,null,1,1,null,null,1,null,1,null,null,null,null,1,null,1,null,1,null,1,1,null,1,1,null,1,null,1,null,null,1,1,1,null,1,null,1,1,null,1,1,1,null,1,null,1,null,null,1,null,null,1,null,1,null,1,1,null,null,1,null,null,1,1,1,1,null,1,1,null,1,null,1,null,null,1,null,null,null,null,1,1,null,1,null,1,1,null,1,1,1,1,null,null,1,null,null,1,null,1,null,1,1,null,1,null,null,null,1,1,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,null,null,null,1,null,1,null,1,null,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,null,null,null,1,null,1,null,null,null,null,null,null,1,null,null,1,1,null,1,1,null,1,null,1,null,1,1,1,null,1,null,null,1,null,null,1,null,null,1,1,1,1,null,1,1,null,null,1,1,1,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,1,null,1,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,1,null,1,1,null,1,null,null,1,null,1,null,1,null,1,null,1,1,null,1,1,null,null,null,1,1,1,null,1,null,null,null,1,1,null,1,null,1,1,1,null,1,null,1,null,null,null,1,null,1,null,1,null,1,1,null,1,1,null,1,null,1,null,1,null,1,null,null,1,null,1,1,null,1,1,1,null,1,null,1,null,1,null,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,null,1,null,null,1,null,null,1,null,null,1,1,1,null,null,null,null,1,1,null,null,1,1,null,1,null,1,1,null,1,null,null,1,null,1,1,null,1,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,1,null,null,1,null,1,null,1,1,null,1,1,null,null,1,null,null,1,null,null,1,null,1,null,1,1,1,null,1,1,null,null,1,1,1,null,1,null,1,null,null,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,1,null,1,1,1,null,null,1,null,1,null,1,null,1,null,1,1,null,1,1,null,null,1,null,null,null,null,null,null,null,null,null,1,1,1,null,1,null,1,null,1,null,1,null,null,1,1,null,1,null,1,1,1,1,null,1,1,null,1,null,null,1,null,1,1,null,null,null,null,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,1,null,1,null,1,1,1,1,null,1,null,1,null,1,null,1,null,1,null,null,1,1,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,null,1,1,1,null,1,null,1,null,1,1,1,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,1,null,1,null,1,null,null,1,null,null,1,1,null,1,1,null,1,null,1,null,null,null,1,1,1,1,1,null,1,null,null,1,null,1,null,1,null,1,null,1,1,null,1,1,1,1,null,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,1,null,1,null,1,null,1,null,null,1,1,null,1,null,null,1,null,1,null,1,null,1,null,null,1,null,1,null,null,null,1,1,1,null,1,1,1,1,null,null,1,null,1,null,null,1,null,1,null,1,null,1,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,1,null,1,null,1,1,1,1,null,1,null,null,null,1,null,null,null,1,1,1,1,null,null,1,null,1,null,1,null,null,1,1,null,1,null,1,null,1,1,null,1,1,null,1,1,null,1,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,null,null,null,1,null,1,null,1,null,1,1,null,null,1,1,null,1,1,null,1,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,1,null,1,null,null,null,null,1,1,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,1,null,null,null,1,null,null,null,1,1,null,null,null,1,1,null,1,null,1,null,null,null,1,null,1,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,1,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null],"linenum":[10,10,10,10,10,10,null,11,11,11,11,11,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,null,12,12,12,null,null,12,null,12,null,12,12,12,12,12,null,null,null,12,null,null,12,null,12,null,12,null,12,12,null,12,null,12,12,null,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,null,12,null,null,12,null,12,12,null,12,null,12,null,12,12,12,12,12,12,null,null,null,12,12,null,12,null,null,12,null,12,null,12,null,null,12,12,null,12,null,12,null,null,null,null,12,null,null,12,null,null,12,12,null,12,null,12,12,null,12,12,null,12,12,null,null,null,null,12,null,12,null,12,null,null,12,null,12,null,12,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,null,12,null,12,null,12,12,null,12,12,12,12,null,12,null,12,12,null,12,null,12,null,null,null,null,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,null,12,12,null,12,12,null,null,12,12,12,12,12,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,12,12,12,12,null,12,null,12,null,12,null,12,12,null,null,12,null,12,null,12,12,null,null,12,null,12,12,null,12,12,null,null,12,null,12,null,null,12,null,12,null,null,12,12,null,null,12,12,null,12,null,12,12,12,null,12,null,null,12,12,null,12,12,null,12,12,12,null,12,null,12,null,null,12,null,12,null,12,null,12,12,null,12,null,12,12,null,12,null,12,12,null,12,null,12,12,null,12,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,null,12,null,12,12,null,12,null,null,12,null,null,12,null,null,null,null,null,null,12,12,null,12,null,12,null,12,null,12,12,12,null,null,null,12,null,null,null,null,12,null,12,12,null,12,12,12,12,12,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,null,12,null,12,null,12,null,12,12,12,12,12,null,12,null,12,12,12,null,12,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,12,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,12,null,null,null,12,12,null,12,12,null,12,null,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,12,12,null,12,12,null,12,null,12,null,12,12,null,null,null,null,12,12,12,null,12,null,12,null,12,null,12,null,12,12,12,12,null,null,12,null,null,12,null,12,null,12,12,12,12,12,12,null,12,null,null,12,null,null,12,12,null,12,12,null,12,null,12,null,12,null,12,null,null,12,12,null,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,12,null,12,null,null,12,null,null,12,12,12,12,null,12,12,null,null,null,null,12,12,null,null,12,null,12,null,null,null,12,12,null,null,null,12,12,null,12,null,12,null,null,12,null,12,12,null,12,12,null,null,12,12,null,12,null,12,12,null,null,12,null,12,null,12,12,null,12,null,12,null,null,null,null,12,null,null,12,null,null,12,null,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,null,12,null,null,null,12,12,null,12,12,null,12,null,12,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,null,12,null,null,12,12,null,null,12,null,null,12,null,12,null,12,null,12,12,null,12,null,null,12,null,12,null,12,null,12,12,null,12,null,12,null,null,12,null,12,null,12,12,null,null,12,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,12,12,12,null,12,12,null,12,null,12,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,null,12,12,null,null,null,12,null,12,null,12,12,null,12,12,null,12,null,12,null,12,null,null,null,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,12,12,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,12,12,12,12,null,12,null,12,12,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,12,12,null,12,null,null,12,null,null,12,12,null,12,null,12,null,null,null,12,null,12,12,null,12,12,12,null,null,12,null,12,null,12,null,12,null,12,12,12,null,12,null,12,null,12,null,null,12,null,null,12,null,12,null,12,12,null,12,null,12,null,null,12,null,12,null,12,null,null,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,null,null,12,null,12,null,12,null,12,12,12,null,12,null,null,12,null,12,12,12,12,null,null,null,12,12,null,12,12,12,12,null,12,null,null,null,null,null,null,null,12,null,12,null,12,null,12,12,null,12,null,null,12,null,null,12,null,null,12,null,12,null,null,12,null,12,null,12,null,12,12,12,null,12,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,12,12,null,12,null,12,null,12,null,null,12,12,12,null,12,12,12,null,12,null,12,null,null,12,null,null,12,null,null,12,12,12,null,null,12,null,12,null,12,12,12,null,12,null,null,12,null,12,12,12,null,12,12,null,12,12,12,null,12,null,null,12,null,null,null,null,12,12,12,null,12,null,null,12,12,12,null,12,null,12,null,12,12,12,12,12,null,12,null,12,12,null,null,null,12,null,12,null,12,null,12,null,12,12,null,null,12,null,null,12,null,12,null,12,null,null,12,null,12,12,null,12,null,null,null,null,null,12,null,12,12,12,null,null,null,null,null,12,null,null,null,12,12,null,12,null,12,12,12,null,12,null,null,null,12,12,null,12,12,null,12,12,null,12,null,null,12,null,12,null,null,12,null,12,null,null,12,null,null,12,null,12,null,12,null,12,12,null,12,null,null,12,null,12,null,12,null,12,12,12,null,12,12,12,12,null,null,12,null,12,null,null,null,null,null,null,null,12,null,12,null,null,12,null,12,null,null,12,12,null,12,12,null,12,12,null,12,null,12,null,12,12,12,null,null,12,null,12,null,12,12,null,null,12,null,null,12,null,12,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,12,12,null,12,12,null,null,null,12,12,null,null,12,null,12,null,12,null,12,12,12,null,12,null,null,12,null,null,12,12,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,12,12,null,12,12,12,12,null,12,12,null,12,12,null,12,null,12,null,null,12,null,12,null,12,12,null,null,12,null,null,12,null,null,12,12,null,12,12,12,12,12,null,12,null,12,12,null,12,null,12,null,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,12,12,null,12,null,12,12,12,null,12,null,12,12,12,null,12,null,12,null,12,null,12,12,null,null,12,null,12,null,null,null,12,null,null,null,12,12,null,12,12,null,null,12,null,12,null,12,12,null,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,12,null,null,12,null,null,12,12,null,12,null,12,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,null,12,null,12,null,12,12,null,12,12,null,null,12,null,null,12,null,12,null,null,null,12,12,null,12,null,12,12,null,12,null,null,null,12,12,null,null,null,12,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,null,null,12,null,null,null,null,12,null,12,null,12,null,12,12,null,null,null,12,12,null,12,12,null,12,null,12,null,null,12,null,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,null,12,null,12,12,null,null,12,null,12,12,null,12,null,null,null,12,null,12,null,12,null,12,12,null,null,12,null,null,12,null,null,12,12,null,12,null,12,null,12,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,null,12,null,12,null,null,null,null,12,null,null,12,12,null,null,12,12,12,null,12,12,null,null,12,null,null,12,null,null,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,null,12,null,null,12,null,12,null,12,null,null,null,12,null,12,null,12,12,null,null,null,12,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,null,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,12,null,12,null,12,null,12,null,12,null,12,12,null,12,12,null,12,null,12,null,null,12,12,null,12,null,null,12,null,null,12,null,12,null,12,null,null,null,null,12,null,null,12,null,null,12,null,null,12,12,null,null,12,null,12,null,null,12,null,null,12,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,12,12,12,null,null,12,null,12,12,null,12,12,null,12,12,12,null,12,null,12,null,12,null,null,null,12,12,null,12,null,12,12,12,null,12,null,12,12,12,12,12,null,12,null,null,null,null,null,null,null,12,12,null,null,12,null,12,null,12,null,null,null,null,12,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,null,12,null,12,null,12,null,null,12,null,null,12,null,null,null,null,null,null,12,12,12,12,12,null,12,12,12,null,12,12,null,12,null,null,12,null,null,12,12,null,12,null,null,12,null,null,null,12,12,12,null,12,12,12,null,null,null,12,null,12,null,12,null,12,12,null,null,12,null,null,12,null,null,null,12,null,12,12,12,12,null,12,12,null,12,null,12,null,12,null,12,12,null,null,12,null,null,12,null,12,null,12,12,12,12,null,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,12,12,null,12,12,null,null,12,null,12,12,null,null,null,12,12,null,null,12,null,null,12,null,null,12,null,12,12,null,12,null,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,null,null,null,null,null,null,12,12,12,12,null,12,null,null,null,12,null,12,12,null,12,12,12,null,12,null,12,null,12,null,null,12,12,null,12,12,null,null,null,12,null,12,12,12,null,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,12,12,null,12,12,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,12,null,12,12,null,12,12,12,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,null,12,null,null,12,null,12,12,12,null,12,null,12,null,12,null,null,null,12,12,12,null,null,null,12,null,12,null,12,null,12,null,12,null,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,null,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,12,null,12,null,12,12,null,null,12,null,12,null,null,12,null,null,12,null,null,12,12,12,null,null,12,null,null,12,12,null,12,12,12,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,null,12,12,12,null,12,null,12,null,12,12,null,null,null,12,null,null,null,12,12,null,null,12,null,12,null,null,null,null,12,null,12,null,12,null,12,12,null,12,12,null,12,null,12,null,null,12,12,12,null,12,null,12,12,null,12,12,12,null,12,null,12,null,null,12,null,null,12,null,12,null,12,12,null,null,12,null,null,12,12,12,12,null,12,12,null,12,null,12,null,null,12,null,null,null,null,12,12,null,12,null,12,12,null,12,12,12,12,null,null,12,null,null,12,null,12,null,12,12,null,12,null,null,null,12,12,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,null,null,null,12,null,12,null,12,null,12,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,null,null,null,12,null,12,null,null,null,null,null,null,12,null,null,12,12,null,12,12,null,12,null,12,null,12,12,12,null,12,null,null,12,null,null,12,null,null,12,12,12,12,null,12,12,null,null,12,12,12,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,12,null,12,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,12,null,12,12,null,12,null,null,12,null,12,null,12,null,12,null,12,12,null,12,12,null,null,null,12,12,12,null,12,null,null,null,12,12,null,12,null,12,12,12,null,12,null,12,null,null,null,12,null,12,null,12,null,12,12,null,12,12,null,12,null,12,null,12,null,12,null,null,12,null,12,12,null,12,12,12,null,12,null,12,null,12,null,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,null,12,null,null,12,null,null,12,null,null,12,12,12,null,null,null,null,12,12,null,null,12,12,null,12,null,12,12,null,12,null,null,12,null,12,12,null,12,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,12,null,null,12,null,12,null,12,12,null,12,12,null,null,12,null,null,12,null,null,12,null,12,null,12,12,12,null,12,12,null,null,12,12,12,null,12,null,12,null,null,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,12,null,12,12,12,null,null,12,null,12,null,12,null,12,null,12,12,null,12,12,null,null,12,null,null,null,null,null,null,null,null,null,12,12,12,null,12,null,12,null,12,null,12,null,null,12,12,null,12,null,12,12,12,12,null,12,12,null,12,null,null,12,null,12,12,null,null,null,null,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,12,null,12,null,12,12,12,12,null,12,null,12,null,12,null,12,null,12,null,null,12,12,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,null,12,12,12,null,12,null,12,null,12,12,12,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,12,null,12,null,12,null,null,12,null,null,12,12,null,12,12,null,12,null,12,null,null,null,12,12,12,12,12,null,12,null,null,12,null,12,null,12,null,12,null,12,12,null,12,12,12,12,null,12,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,12,null,12,null,12,null,12,null,null,12,12,null,12,null,null,12,null,12,null,12,null,12,null,null,12,null,12,null,null,null,12,12,12,null,12,12,12,12,null,null,12,null,12,null,null,12,null,12,null,12,null,12,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,12,null,12,null,12,12,12,12,null,12,null,null,null,12,null,null,null,12,12,12,12,null,null,12,null,12,null,12,null,null,12,12,null,12,null,12,null,12,12,null,12,12,null,12,12,null,12,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,null,null,null,12,null,12,null,12,null,12,12,null,null,12,12,null,12,12,null,12,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,12,null,12,null,null,null,null,12,12,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,12,null,null,null,12,null,null,null,12,12,null,null,null,12,12,null,12,null,12,null,null,null,12,null,12,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,13,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,13,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null],"memalloc":[124.5360641479492,124.5360641479492,124.5360641479492,124.5360641479492,124.5360641479492,124.5360870361328,124.5360870361328,139.8182983398438,139.8182983398438,139.8182983398438,139.8182983398438,139.8182983398438,139.8186645507812,139.8186645507812,139.8186645507812,170.2840423583984,170.2840423583984,170.2840423583984,170.2840423583984,170.2840423583984,170.2840423583984,170.2840423583984,170.2840423583984,170.2840423583984,170.2840423583984,170.2840881347656,170.2840881347656,170.2840881347656,170.2840881347656,170.2840881347656,170.2840881347656,170.2840881347656,170.2840881347656,170.2840881347656,170.2840881347656,170.2840881347656,170.2840881347656,170.2840881347656,170.2840881347656,170.2840881347656,170.2840881347656,170.2840881347656,170.2840881347656,170.2837829589844,170.2837829589844,185.5425720214844,185.7111129760742,185.7111129760742,185.9104309082031,185.9104309082031,185.9104309082031,186.1118087768555,186.3361129760742,186.5705871582031,186.5705871582031,186.5705871582031,186.8097381591797,186.8097381591797,187.0724487304688,187.0724487304688,187.2975006103516,187.5227737426758,187.7516326904297,187.9876937866211,188.2255249023438,188.2255249023438,188.4635848999023,188.4635848999023,188.6059188842773,188.6059188842773,188.6059188842773,185.7161178588867,185.7161178588867,185.9404449462891,185.9404449462891,186.1837615966797,186.1837615966797,186.4264450073242,186.6707458496094,186.6707458496094,186.9149703979492,186.9149703979492,187.162109375,187.404426574707,187.404426574707,187.6404800415039,187.8729095458984,187.8729095458984,188.1052398681641,188.1052398681641,188.3380813598633,188.3380813598633,188.5684814453125,188.5684814453125,188.6703109741211,188.6703109741211,188.6703109741211,185.8786849975586,185.8786849975586,186.1055755615234,186.1055755615234,186.3459930419922,186.3459930419922,186.3459930419922,186.5872344970703,186.5872344970703,186.8281631469727,187.0908660888672,187.0908660888672,187.3251113891602,187.3251113891602,187.555534362793,187.555534362793,187.7714157104492,188.0016403198242,188.2330932617188,188.465705871582,188.6958312988281,188.7521057128906,188.7521057128906,188.7521057128906,188.7521057128906,186.0399398803711,186.2573013305664,186.2573013305664,186.4980621337891,186.4980621337891,186.4980621337891,186.7394943237305,186.7394943237305,186.9811248779297,186.9811248779297,187.2194442749023,187.2194442749023,187.2194442749023,187.4537506103516,187.6843185424805,187.6843185424805,187.9157333374023,187.9157333374023,188.1457824707031,188.1457824707031,188.3772354125977,188.3772354125977,188.6097946166992,188.8325881958008,188.8325881958008,188.8325881958008,188.8325881958008,188.8325881958008,188.8325881958008,186.2552108764648,186.4892425537109,186.4892425537109,186.7298049926758,186.7298049926758,186.9688034057617,187.2085189819336,187.2085189819336,187.4685592651367,187.7111282348633,187.7111282348633,187.9455718994141,188.1687698364258,188.1687698364258,188.3965072631836,188.3965072631836,188.3965072631836,188.6288299560547,188.6288299560547,188.8604507446289,188.8604507446289,188.9117202758789,188.9117202758789,188.9117202758789,186.3172760009766,186.3172760009766,186.5429153442383,186.5429153442383,186.7823333740234,187.0225143432617,187.0225143432617,187.0225143432617,187.2611541748047,187.2611541748047,187.4962921142578,187.4962921142578,187.7329940795898,187.7329940795898,187.9619903564453,187.9619903564453,188.1917037963867,188.1917037963867,188.4203567504883,188.4203567504883,188.6504440307617,188.6504440307617,188.8808517456055,188.989631652832,188.989631652832,188.989631652832,186.3818283081055,186.3818283081055,186.6062240600586,186.6062240600586,186.845703125,187.0859603881836,187.0859603881836,187.3241577148438,187.559814453125,187.794075012207,188.0291442871094,188.0291442871094,188.2804260253906,188.2804260253906,188.5084991455078,188.7377166748047,188.7377166748047,188.9672393798828,188.9672393798828,189.0662536621094,189.0662536621094,189.0662536621094,186.5066757202148,186.5066757202148,186.5066757202148,186.7283020019531,186.7283020019531,186.9460983276367,186.9460983276367,187.1804656982422,187.1804656982422,187.4179153442383,187.4179153442383,187.4179153442383,187.6540908813477,187.6540908813477,187.887321472168,187.887321472168,188.116455078125,188.3459930419922,188.3459930419922,188.5758666992188,188.5758666992188,188.8048629760742,188.8048629760742,189.0350723266602,189.0350723266602,189.1416473388672,189.1416473388672,189.1416473388672,186.6123504638672,186.8333358764648,186.8333358764648,187.0693588256836,187.3081359863281,187.3081359863281,187.3081359863281,187.5446548461914,187.7787399291992,188.0085067749023,188.2314224243164,188.4477310180664,188.6760940551758,188.9239120483398,188.9239120483398,189.1534423828125,189.1534423828125,189.2158584594727,189.2158584594727,186.7115707397461,186.7115707397461,186.8938751220703,186.8938751220703,187.068962097168,187.068962097168,187.2524032592773,187.2524032592773,187.4534454345703,187.4534454345703,187.6749496459961,187.8883285522461,188.1093063354492,188.3358993530273,188.5396270751953,188.7657012939453,188.7657012939453,188.9846343994141,188.9846343994141,189.2055740356445,189.2055740356445,189.2888031005859,189.2888031005859,186.8536758422852,187.0565490722656,187.0565490722656,187.0565490722656,187.2637786865234,187.2637786865234,187.4824676513672,187.4824676513672,187.7042770385742,187.9246292114258,187.9246292114258,187.9246292114258,188.1588821411133,188.1588821411133,188.3838272094727,188.6102523803711,188.6102523803711,188.8431167602539,189.0538177490234,189.0538177490234,189.0538177490234,189.2878952026367,189.2878952026367,189.3607177734375,189.3607177734375,189.3607177734375,186.9510879516602,186.9510879516602,187.1547775268555,187.1547775268555,187.1547775268555,187.3466110229492,187.5664443969727,187.5664443969727,187.5664443969727,187.7778625488281,187.9884490966797,187.9884490966797,188.2460556030273,188.2460556030273,188.4328155517578,188.6549606323242,188.8639068603516,188.8639068603516,189.0625534057617,189.0625534057617,189.0625534057617,189.2888870239258,189.4313201904297,189.4313201904297,187.009162902832,187.220100402832,187.220100402832,187.4423294067383,187.6735153198242,187.9091949462891,187.9091949462891,188.140495300293,188.140495300293,188.3721237182617,188.3721237182617,188.3721237182617,188.6093826293945,188.6093826293945,188.8457107543945,188.8457107543945,189.0799942016602,189.0799942016602,189.3207778930664,189.5008239746094,189.5008239746094,189.5008239746094,189.5008239746094,187.328239440918,187.5527954101562,187.5527954101562,187.784423828125,187.784423828125,187.9973297119141,188.2208786010742,188.2208786010742,188.4512176513672,188.4512176513672,188.6836166381836,188.9143142700195,188.9143142700195,189.1466293334961,189.3787841796875,189.3787841796875,189.5692672729492,189.5692672729492,189.5692672729492,189.5692672729492,187.3859024047852,187.5999145507812,187.5999145507812,187.8264694213867,187.8264694213867,188.0575714111328,188.0575714111328,188.292724609375,188.292724609375,188.292724609375,188.5276718139648,188.5276718139648,188.7594146728516,188.9879455566406,188.9879455566406,189.2174758911133,189.2174758911133,189.2174758911133,189.4462966918945,189.4462966918945,189.4462966918945,189.6365432739258,189.6365432739258,189.6365432739258,189.6365432739258,189.6365432739258,189.6365432739258,187.5259857177734,187.7465591430664,187.9740829467773,187.9740829467773,188.2048873901367,188.2048873901367,188.4376907348633,188.4376907348633,188.6712646484375,188.6712646484375,188.9022521972656,189.1308212280273,189.3642578125,189.3642578125,189.5976028442383,189.5976028442383,189.7027206420898,189.7027206420898,189.7027206420898,187.4664306640625,187.4664306640625,187.6697540283203,187.6697540283203,187.8772735595703,188.0940628051758,188.0940628051758,188.32421875,188.558349609375,188.7929306030273,189.0248336791992,189.2557601928711,189.4857559204102,189.4857559204102,189.7149276733398,189.7149276733398,189.7678527832031,189.7678527832031,187.6029815673828,187.6029815673828,187.8007049560547,187.8007049560547,187.8007049560547,187.9935607910156,187.9935607910156,188.173583984375,188.173583984375,188.173583984375,188.386474609375,188.386474609375,188.6163482666016,188.6163482666016,188.85107421875,188.85107421875,189.0828323364258,189.3136291503906,189.5454330444336,189.7753067016602,189.8318786621094,189.8318786621094,187.695671081543,187.695671081543,187.8887481689453,188.090202331543,188.2931671142578,188.2931671142578,188.512451171875,188.7455291748047,188.7455291748047,188.9817352294922,188.9817352294922,189.2155151367188,189.2155151367188,189.4460983276367,189.669075012207,189.669075012207,189.8949661254883,189.8949661254883,189.8949661254883,189.8949661254883,187.8548431396484,187.8548431396484,188.0467758178711,188.2488174438477,188.4642639160156,188.4642639160156,188.6962127685547,188.9326477050781,188.9326477050781,189.1671905517578,189.1671905517578,189.3997116088867,189.3997116088867,189.6320419311523,189.6320419311523,189.863655090332,189.863655090332,189.9570236206055,189.9570236206055,189.9570236206055,187.8586578369141,188.0504150390625,188.0504150390625,188.248161315918,188.248161315918,188.4580764770508,188.681755065918,188.681755065918,188.9178848266602,189.1529083251953,189.1529083251953,189.3863143920898,189.3863143920898,189.6158142089844,189.6158142089844,189.8455200195312,189.8455200195312,189.8455200195312,190.0180053710938,190.0180053710938,190.0180053710938,190.0180053710938,190.0180053710938,190.0180053710938,190.0180053710938,190.0180053710938,190.0180053710938,190.0180053710938,190.0180053710938,190.0180053710938,190.0180053710938,190.0180053710938,190.0180053710938,190.0180053710938,190.0180053710938,190.0180053710938,190.0180053710938,190.0180053710938,190.0180053710938,190.0180053710938,190.0180053710938,190.0180053710938,190.0180053710938,190.0180053710938,190.0180053710938,190.0180053710938,190.0180053710938,190.0180053710938,187.9371185302734,187.9371185302734,188.0948791503906,188.0948791503906,188.2686538696289,188.2686538696289,188.4506225585938,188.6420135498047,188.6420135498047,188.8515853881836,189.0747451782227,189.0747451782227,189.3084564208984,189.3084564208984,189.5402755737305,189.5402755737305,189.7708358764648,190.0018157958984,190.0018157958984,190.0779190063477,190.0779190063477,190.0779190063477,188.0576324462891,188.2280197143555,188.4160003662109,188.4160003662109,188.6194000244141,188.6194000244141,188.8644866943359,188.8644866943359,189.0985717773438,189.0985717773438,189.3347625732422,189.3347625732422,189.5686569213867,189.8003540039062,190.0329666137695,190.1370239257812,190.1370239257812,190.1370239257812,188.1259460449219,188.1259460449219,188.1259460449219,188.3123245239258,188.3123245239258,188.5046081542969,188.5046081542969,188.7118911743164,188.935905456543,189.1709365844727,189.4048461914062,189.6364822387695,189.8656463623047,189.8656463623047,190.0935592651367,190.0935592651367,190.0935592651367,190.1951446533203,190.1951446533203,190.1951446533203,188.2185440063477,188.4066314697266,188.4066314697266,188.6028366088867,188.8142166137695,188.8142166137695,189.04150390625,189.04150390625,189.2774963378906,189.2774963378906,189.5122604370117,189.5122604370117,189.7453079223633,189.7453079223633,189.9759368896484,190.2292098999023,190.2524337768555,190.2524337768555,190.2524337768555,188.3733596801758,188.3733596801758,188.5656280517578,188.5656280517578,188.7685317993164,188.7685317993164,188.9845581054688,189.2191619873047,189.2191619873047,189.4480972290039,189.4480972290039,189.6837768554688,189.6837768554688,189.9145889282227,190.1451263427734,190.1451263427734,190.3086547851562,190.3086547851562,190.3086547851562,190.3086547851562,190.3086547851562,190.3086547851562,188.5272750854492,188.716796875,188.9234313964844,189.1471786499023,189.1471786499023,189.382194519043,189.6197509765625,189.6197509765625,189.8562850952148,189.8562850952148,190.0898208618164,190.3214492797852,190.3640899658203,190.3640899658203,190.3640899658203,188.5347900390625,188.5347900390625,188.7263870239258,188.7263870239258,188.9293975830078,188.9293975830078,189.1733856201172,189.4097137451172,189.4097137451172,189.6460418701172,189.6460418701172,189.8815994262695,190.1144027709961,190.1144027709961,190.3463668823242,190.3463668823242,190.4185104370117,190.4185104370117,190.4185104370117,188.5987701416016,188.5987701416016,188.793327331543,188.9965744018555,188.9965744018555,189.2200317382812,189.4570465087891,189.4570465087891,189.4570465087891,189.6934661865234,189.9290542602539,189.9290542602539,190.1615600585938,190.1615600585938,190.3932571411133,190.47216796875,190.47216796875,190.47216796875,188.6719741821289,188.6719741821289,188.8606338500977,188.8606338500977,189.061882019043,189.2779083251953,189.2779083251953,189.5083084106445,189.5083084106445,189.745735168457,189.745735168457,189.9833297729492,189.9833297729492,189.9833297729492,190.2182998657227,190.2182998657227,190.2182998657227,190.4574661254883,190.4574661254883,190.4574661254883,190.5248489379883,190.5248489379883,190.5248489379883,188.7762680053711,188.964729309082,188.964729309082,189.1672286987305,189.1672286987305,189.3879776000977,189.3879776000977,189.6245727539062,189.6245727539062,189.8619918823242,189.8619918823242,190.0979690551758,190.0979690551758,190.3310012817383,190.3310012817383,190.5617523193359,190.5617523193359,190.5767211914062,190.5767211914062,188.8830413818359,188.8830413818359,189.0711059570312,189.0711059570312,189.0711059570312,189.275520324707,189.275520324707,189.4998397827148,189.4998397827148,189.7359771728516,189.7359771728516,189.9721984863281,189.9721984863281,190.2071151733398,190.2071151733398,190.4396438598633,190.4396438598633,190.4396438598633,190.6277618408203,190.6277618408203,190.6277618408203,190.6277618408203,190.6277618408203,190.6277618408203,190.6277618408203,190.6277618408203,189.00537109375,189.1966400146484,189.1966400146484,189.4051055908203,189.6334609985352,189.6334609985352,189.8711853027344,189.8711853027344,190.1078872680664,190.3671035766602,190.3671035766602,190.5995864868164,190.5995864868164,190.6780090332031,190.6780090332031,188.9998245239258,188.9998245239258,189.1934356689453,189.3976516723633,189.3976516723633,189.6206665039062,189.6206665039062,189.8561782836914,189.8561782836914,190.0922241210938,190.3288879394531,190.3288879394531,190.3288879394531,190.5695114135742,190.7273864746094,190.7273864746094,190.7273864746094,190.7273864746094,190.7273864746094,190.7273864746094,189.2013702392578,189.2013702392578,189.401237487793,189.401237487793,189.6186752319336,189.6186752319336,189.8529815673828,190.0896301269531,190.0896301269531,190.3255233764648,190.3255233764648,190.5671005249023,190.7759857177734,190.7759857177734,190.7759857177734,190.7759857177734,189.2299652099609,189.2299652099609,189.4262619018555,189.6121368408203,189.6121368408203,189.8171081542969,189.8171081542969,190.0673599243164,190.0673599243164,190.0673599243164,190.3058166503906,190.3058166503906,190.5428771972656,190.5428771972656,190.7761383056641,190.8238372802734,190.8238372802734,190.8238372802734,189.2210922241211,189.3971405029297,189.3971405029297,189.5991897583008,189.8205642700195,189.8205642700195,190.0558929443359,190.0558929443359,190.2947235107422,190.2947235107422,190.5336990356445,190.5336990356445,190.7695999145508,190.7695999145508,190.8708572387695,190.8708572387695,189.2670288085938,189.4482955932617,189.6429595947266,189.8481597900391,189.8481597900391,190.0729904174805,190.3112182617188,190.3112182617188,190.5481262207031,190.5481262207031,190.7840423583984,190.9171600341797,190.9171600341797,190.9171600341797,190.9171600341797,190.9171600341797,190.9171600341797,189.4923629760742,189.4923629760742,189.7030944824219,189.7030944824219,189.9194793701172,189.9194793701172,190.151237487793,190.151237487793,190.3905944824219,190.3905944824219,190.6292953491211,190.8659362792969,190.9626617431641,190.9626617431641,190.9626617431641,190.9626617431641,189.4120330810547,189.4120330810547,189.5950698852539,189.5950698852539,189.7941207885742,190.0149230957031,190.0149230957031,190.2508316040039,190.4911880493164,190.4911880493164,190.7302169799805,190.7302169799805,190.9675827026367,190.9675827026367,191.0074462890625,191.0074462890625,191.0074462890625,189.5300445556641,189.5300445556641,189.720329284668,189.9287261962891,189.9287261962891,190.1569137573242,190.1569137573242,190.3962554931641,190.3962554931641,190.6353912353516,190.6353912353516,190.8729629516602,190.8729629516602,191.0514907836914,191.0514907836914,191.0514907836914,191.0514907836914,189.6804275512695,189.899772644043,190.1126861572266,190.3454513549805,190.3454513549805,190.5863571166992,190.5863571166992,190.8257598876953,190.8257598876953,191.0619049072266,191.0619049072266,191.0619049072266,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,191.0948867797852,189.6016082763672,189.6016082763672,189.6016082763672,189.6016082763672,189.6016082763672,189.6016082763672,189.6930313110352,189.6930313110352,189.8880920410156,190.0926513671875,190.315559387207,190.5525665283203,190.7804412841797,190.7804412841797,190.9940643310547,190.9940643310547,191.2396621704102,191.4662704467773,191.697868347168,191.697868347168,191.934211730957,191.934211730957,192.17041015625,192.17041015625,192.17041015625,192.3983612060547,192.3983612060547,192.3983612060547,192.5943603515625,192.5943603515625,192.5943603515625,192.7861328125,192.7861328125,192.9807510375977,192.9807510375977,193.1739807128906,193.1739807128906,193.3696060180664,193.3696060180664,193.5628204345703,193.5628204345703,193.5628204345703,193.7572402954102,193.7572402954102,193.9494323730469,194.1438674926758,194.3370513916016,194.3370513916016,194.4387817382812,194.4387817382812,194.4387817382812,194.4387817382812,194.4387817382812,194.4387817382812,189.9843063354492,190.2092819213867,190.2092819213867,190.4472274780273,190.4472274780273,190.6851959228516,190.6851959228516,190.91064453125,190.91064453125,191.1251449584961,191.1251449584961,191.3611602783203,191.5930709838867,191.5930709838867,191.8260040283203,192.0606307983398,192.3227233886719,192.3227233886719,192.3227233886719,192.5645065307617,192.5645065307617,192.8066635131836,192.8066635131836,193.0456619262695,193.0456619262695,193.2867813110352,193.2867813110352,193.5286407470703,193.7702941894531,194.0120086669922,194.0120086669922,194.2510070800781,194.2510070800781,194.4809036254883,194.4809036254883,194.5710906982422,194.5710906982422,194.5710906982422,194.5710906982422,194.5710906982422,194.5710906982422,190.1990280151367,190.1990280151367,190.4213562011719,190.4213562011719,190.6562728881836,190.8879623413086,190.8879623413086,191.1067657470703,191.1067657470703,191.3328170776367,191.3328170776367,191.3328170776367,191.5670547485352,191.5670547485352,191.7991943359375,191.7991943359375,192.0333099365234,192.0333099365234,192.26806640625,192.26806640625,192.509521484375,192.509521484375,192.7527313232422,192.9949569702148,192.9949569702148,193.2344360351562,193.2344360351562,193.4730606079102,193.4730606079102,193.7132873535156,193.7132873535156,193.954460144043,193.954460144043,194.2193984985352,194.2193984985352,194.2193984985352,194.4538116455078,194.4538116455078,194.6849212646484,194.6849212646484,194.7012329101562,194.7012329101562,194.7012329101562,190.2551879882812,190.4595565795898,190.4595565795898,190.6785354614258,190.6785354614258,190.9106903076172,190.9106903076172,191.1344909667969,191.3532409667969,191.5910263061523,191.5910263061523,191.8251190185547,191.8251190185547,191.8251190185547,192.0570831298828,192.0570831298828,192.2907104492188,192.5242691040039,192.7602767944336,193.0013580322266,193.0013580322266,193.2437133789062,193.2437133789062,193.4845733642578,193.7271194458008,193.7271194458008,193.96923828125,194.212516784668,194.4566116333008,194.6878128051758,194.6878128051758,194.8292846679688,194.8292846679688,194.8292846679688,194.8292846679688,194.8292846679688,194.8292846679688,190.5555419921875,190.5555419921875,190.7667770385742,190.7667770385742,190.988395690918,190.988395690918,191.2127075195312,191.2127075195312,191.4299545288086,191.6669845581055,191.6669845581055,191.902458190918,191.902458190918,191.902458190918,192.1346206665039,192.1346206665039,192.1346206665039,192.3676452636719,192.3676452636719,192.3676452636719,192.5997924804688,192.5997924804688,192.8324890136719,192.8324890136719,193.0702972412109,193.3143157958984,193.3143157958984,193.5575256347656,193.5575256347656,193.800910949707,193.800910949707,194.0435943603516,194.2864532470703,194.531608581543,194.531608581543,194.7671508789062,194.9552688598633,194.9552688598633,194.9552688598633,194.9552688598633,190.6849517822266,190.6849517822266,190.884880065918,190.884880065918,191.0964584350586,191.0964584350586,191.3119964599609,191.517448425293,191.517448425293,191.7747116088867,191.7747116088867,192.0109710693359,192.2434234619141,192.472526550293,192.472526550293,192.701545715332,192.701545715332,192.9326400756836,192.9326400756836,193.1644515991211,193.1644515991211,193.1644515991211,193.3950729370117,193.6255798339844,193.85791015625,193.85791015625,194.0890121459961,194.3306427001953,194.5732040405273,194.5732040405273,194.8116836547852,194.8116836547852,195.0366058349609,195.0366058349609,195.0366058349609,195.0792465209961,195.0792465209961,195.0792465209961,195.0792465209961,195.0792465209961,195.0792465209961,191.0019912719727,191.2068405151367,191.4168395996094,191.4168395996094,191.4168395996094,191.6266860961914,191.6266860961914,191.8641052246094,191.8641052246094,192.1014785766602,192.3373107910156,192.5925064086914,192.5925064086914,192.8246841430664,192.8246841430664,192.8246841430664,193.0558090209961,193.0558090209961,193.2862548828125,193.5182113647461,193.7606506347656,193.7606506347656,194.0032272338867,194.2453765869141,194.2453765869141,194.4882431030273,194.7329635620117,194.9700469970703,194.9700469970703,195.2001037597656,195.2001037597656,195.2001037597656,195.201171875,195.201171875,195.201171875,191.0210113525391,191.0210113525391,191.202522277832,191.4111709594727,191.6202774047852,191.6202774047852,191.8373489379883,191.8373489379883,191.8373489379883,192.0753402709961,192.3126907348633,192.5459213256836,192.5459213256836,192.7755966186523,192.7755966186523,193.0066986083984,193.0066986083984,193.2379760742188,193.4693222045898,193.7019348144531,193.9367218017578,194.1930923461914,194.1930923461914,194.4317398071289,194.4317398071289,194.6747741699219,194.9187164306641,194.9187164306641,195.1535263061523,195.1535263061523,195.3212280273438,195.3212280273438,195.3212280273438,195.3212280273438,191.2553329467773,191.2553329467773,191.4362030029297,191.4362030029297,191.643440246582,191.8484191894531,191.8484191894531,192.0821304321289,192.3194046020508,192.3194046020508,192.3194046020508,192.556282043457,192.556282043457,192.7903747558594,192.7903747558594,193.0218353271484,193.0218353271484,193.0218353271484,193.2518920898438,193.2518920898438,193.4824295043945,193.7140579223633,193.7140579223633,193.9411773681641,193.9411773681641,194.1708679199219,194.1708679199219,194.4008941650391,194.4008941650391,194.6319885253906,194.6319885253906,194.8635559082031,195.0978622436523,195.3284606933594,195.3284606933594,195.4392013549805,195.4392013549805,195.4392013549805,195.4392013549805,195.4392013549805,195.4392013549805,195.4392013549805,195.4392013549805,191.5196380615234,191.7210998535156,191.7210998535156,191.9235992431641,191.9235992431641,192.1444625854492,192.3795394897461,192.6141510009766,192.6141510009766,192.8475036621094,192.8475036621094,193.0773391723633,193.0773391723633,193.3084411621094,193.5406188964844,193.5406188964844,193.7747497558594,194.0070266723633,194.0070266723633,194.2420425415039,194.4829711914062,194.4829711914062,194.7238693237305,194.7238693237305,194.7238693237305,194.9426956176758,194.9426956176758,195.1511383056641,195.1511383056641,195.1511383056641,195.3771438598633,195.3771438598633,195.5554275512695,195.5554275512695,195.5554275512695,195.5554275512695,195.5554275512695,195.5554275512695,191.6158065795898,191.6158065795898,191.8001937866211,191.8001937866211,191.9909820556641,191.9909820556641,192.2184295654297,192.4508590698242,192.4508590698242,192.6886672973633,192.6886672973633,192.6886672973633,192.9199295043945,192.9199295043945,193.1478652954102,193.1478652954102,193.3802490234375,193.3802490234375,193.6127548217773,193.8450164794922,194.0787658691406,194.0787658691406,194.3012542724609,194.5342864990234,194.7679672241211,195.0081176757812,195.0081176757812,195.245491027832,195.4708709716797,195.4708709716797,195.6696395874023,195.6696395874023,195.6696395874023,195.6696395874023,195.6696395874023,195.6696395874023,191.7452545166016,191.7452545166016,191.9393310546875,191.9393310546875,192.1269607543945,192.1269607543945,192.2960739135742,192.4989242553711,192.4989242553711,192.7188339233398,192.7188339233398,192.7188339233398,192.9181365966797,193.1413650512695,193.1413650512695,193.3453140258789,193.5670471191406,193.5670471191406,193.7948837280273,194.0029296875,194.0029296875,194.2268524169922,194.2268524169922,194.4400405883789,194.4400405883789,194.6652450561523,194.895751953125,195.1161880493164,195.1161880493164,195.1161880493164,195.3511734008789,195.3511734008789,195.5683746337891,195.5683746337891,195.7794494628906,195.782096862793,195.782096862793,195.782096862793,195.782096862793,195.782096862793,195.782096862793,192.0882339477539,192.0882339477539,192.281852722168,192.4600677490234,192.6604614257812,192.6604614257812,192.8637161254883,192.8637161254883,193.0823440551758,193.0823440551758,193.2960510253906,193.2960510253906,193.5157318115234,193.5157318115234,193.7357940673828,193.7357940673828,193.9496994018555,193.9496994018555,194.1797714233398,194.1797714233398,194.1797714233398,194.3996047973633,194.6212463378906,194.6212463378906,194.8529052734375,194.8529052734375,195.0722045898438,195.0722045898438,195.3055877685547,195.3055877685547,195.5284423828125,195.5284423828125,195.7442779541016,195.8927307128906,195.8927307128906,195.8927307128906,195.8927307128906,192.1616897583008,192.1616897583008,192.3425903320312,192.3425903320312,192.5216445922852,192.5216445922852,192.7254791259766,192.9411392211914,193.1706619262695,193.1706619262695,193.4026412963867,193.6327438354492,193.6327438354492,193.8604583740234,193.8604583740234,194.0898742675781,194.3193511962891,194.3193511962891,194.5499725341797,194.7811813354492,194.7811813354492,195.0123443603516,195.0123443603516,195.2435607910156,195.2435607910156,195.4756317138672,195.7080459594727,195.9288101196289,195.9288101196289,196.0015029907227,196.0015029907227,196.0015029907227,196.0015029907227,196.0015029907227,196.0015029907227,192.3836669921875,192.567985534668,192.7609634399414,192.7609634399414,192.9741439819336,193.2239151000977,193.2239151000977,193.4569473266602,193.4569473266602,193.6901092529297,193.6901092529297,193.9219131469727,193.9219131469727,194.153938293457,194.153938293457,194.3853378295898,194.3853378295898,194.6157913208008,194.8455963134766,194.8455963134766,195.0774002075195,195.0774002075195,195.3086776733398,195.3086776733398,195.5404815673828,195.5404815673828,195.7724761962891,195.7724761962891,195.9944763183594,195.9944763183594,196.1086730957031,196.1086730957031,196.1086730957031,196.1086730957031,196.1086730957031,196.1086730957031,192.5108947753906,192.6953201293945,192.8830795288086,192.8830795288086,193.0923767089844,193.3128204345703,193.5421676635742,193.7759170532227,193.7759170532227,194.0087585449219,194.2392196655273,194.2392196655273,194.4706802368164,194.7024841308594,194.7024841308594,194.9570465087891,194.9570465087891,195.1893920898438,195.1893920898438,195.4195861816406,195.6515808105469,195.6515808105469,195.8842620849609,195.8842620849609,196.1079788208008,196.213981628418,196.213981628418,196.213981628418,196.213981628418,196.213981628418,196.213981628418,192.6850433349609,192.6850433349609,192.6850433349609,192.8675994873047,193.0605773925781,193.0605773925781,193.2682495117188,193.4876403808594,193.7142486572266,193.9476318359375,194.179084777832,194.179084777832,194.4100036621094,194.4100036621094,194.6412887573242,194.87255859375,194.87255859375,195.1020202636719,195.1020202636719,195.3196334838867,195.3196334838867,195.3196334838867,195.5524673461914,195.5524673461914,195.7820053100586,195.7820053100586,196.0119018554688,196.0119018554688,196.0119018554688,196.2280654907227,196.2280654907227,196.3176116943359,196.3176116943359,196.3176116943359,196.3176116943359,192.8592910766602,193.0354080200195,193.2230987548828,193.2230987548828,193.4122619628906,193.4122619628906,193.6051788330078,193.814582824707,194.0248870849609,194.0248870849609,194.2526702880859,194.2526702880859,194.4799270629883,194.6981048583984,194.9283905029297,194.9283905029297,195.1475448608398,195.1475448608398,195.3708190917969,195.3708190917969,195.6020431518555,195.6020431518555,195.8230209350586,196.0607452392578,196.0607452392578,196.0607452392578,196.2986755371094,196.2986755371094,196.4196014404297,196.4196014404297,196.4196014404297,196.4196014404297,196.4196014404297,196.4196014404297,196.4196014404297,196.4196014404297,192.9556579589844,193.1398315429688,193.1398315429688,193.3139724731445,193.5008087158203,193.5008087158203,193.5008087158203,193.7017669677734,193.7017669677734,193.8979034423828,193.8979034423828,194.1174087524414,194.3313598632812,194.3313598632812,194.5456390380859,194.7779159545898,194.7779159545898,194.9972610473633,194.9972610473633,195.2299499511719,195.2299499511719,195.450569152832,195.6746368408203,195.6746368408203,195.9077911376953,195.9077911376953,196.1490936279297,196.1490936279297,196.3755569458008,196.5198974609375,196.5198974609375,196.5198974609375,196.5198974609375,196.5198974609375,196.5198974609375,193.1066665649414,193.286491394043,193.286491394043,193.4707717895508,193.4707717895508,193.6659240722656,193.8723678588867,193.8723678588867,194.0945358276367,194.0945358276367,194.3266906738281,194.3266906738281,194.5602569580078,194.5602569580078,194.5602569580078,194.7899322509766,194.7899322509766,195.0209197998047,195.0209197998047,195.2502365112305,195.2502365112305,195.2502365112305,195.4806060791016,195.4806060791016,195.7120742797852,195.7120742797852,195.9440383911133,196.1773071289062,196.1773071289062,196.4063110351562,196.6185913085938,196.6185913085938,196.6185913085938,196.6185913085938,196.6185913085938,196.6185913085938,193.2463455200195,193.2463455200195,193.4286727905273,193.4286727905273,193.6181716918945,193.6181716918945,193.8181991577148,194.0179061889648,194.0179061889648,194.2358779907227,194.2358779907227,194.4672393798828,194.7008590698242,194.7008590698242,194.9323120117188,194.9323120117188,195.1649932861328,195.1649932861328,195.396728515625,195.629150390625,195.629150390625,195.861328125,195.861328125,196.0950012207031,196.3289260864258,196.3289260864258,196.5553436279297,196.5553436279297,196.7156829833984,196.7156829833984,196.7156829833984,196.7156829833984,196.7156829833984,196.7156829833984,196.7156829833984,196.7156829833984,196.7156829833984,196.7156829833984,196.7156829833984,196.7156829833984,196.7156829833984,196.7156829833984,196.7156829833984,196.7156829833984,196.7156829833984,196.7156829833984,196.7156829833984,196.7156829833984,196.7156829833984,196.7156829833984,196.7156829833984,196.7156829833984,196.7156829833984,196.7156829833984,196.7156829833984,196.7156829833984,196.7156829833984,196.7156829833984,196.7156829833984,196.7156829833984,196.7156829833984,196.7156829833984,196.7156829833984,196.7156829833984,196.7156829833984,196.7156829833984,196.7156829833984,196.7156829833984,196.7156829833984,196.7156829833984,196.7156829833984,196.7156829833984,196.7156829833984,196.7156829833984,196.7156829833984,196.7156829833984,193.4919738769531,193.4919738769531,193.6479644775391,193.6479644775391,193.6479644775391,193.8245086669922,193.8245086669922,194.0085601806641,194.0085601806641,194.1996994018555,194.4086227416992,194.4086227416992,194.6374588012695,194.6374588012695,194.8713684082031,194.8713684082031,195.1032257080078,195.3358688354492,195.3358688354492,195.5676574707031,195.5676574707031,195.823486328125,196.0551300048828,196.0551300048828,196.2936630249023,196.5379104614258,196.5379104614258,196.7710800170898,196.7710800170898,196.8110885620117,196.8110885620117,196.8110885620117,196.8110885620117,196.8110885620117,196.8110885620117,193.6661071777344,193.6661071777344,193.8494415283203,193.8494415283203,194.0415878295898,194.2447891235352,194.2447891235352,194.4627990722656,194.4627990722656,194.6940078735352,194.6940078735352,194.9283294677734,194.9283294677734,195.1607894897461,195.1607894897461,195.3926010131836,195.3926010131836,195.6235733032227,195.8560104370117,195.8560104370117,196.0880279541016,196.0880279541016,196.3217926025391,196.5558090209961,196.5558090209961,196.7893829345703,196.7893829345703,196.9051361083984,196.9051361083984,196.9051361083984,196.9051361083984,193.7439880371094,193.7439880371094,193.9253997802734,194.1277847290039,194.1277847290039,194.3247833251953,194.5367889404297,194.5367889404297,194.7624206542969,194.996223449707,194.996223449707,195.2289047241211,195.4590759277344,195.4590759277344,195.6905364990234,195.6905364990234,195.9211273193359,195.9211273193359,196.1523818969727,196.1523818969727,196.3896484375,196.3896484375,196.6295547485352,196.6295547485352,196.8583068847656,196.9976501464844,196.9976501464844,196.9976501464844,196.9976501464844,196.9976501464844,196.9976501464844,193.8676681518555,193.8676681518555,193.8676681518555,194.0479278564453,194.2310562133789,194.2310562133789,194.4239654541016,194.4239654541016,194.6338424682617,194.6338424682617,194.8586273193359,195.09423828125,195.09423828125,195.329231262207,195.329231262207,195.5610122680664,195.5610122680664,195.5610122680664,195.7942123413086,195.7942123413086,196.0263671875,196.0263671875,196.2590484619141,196.2590484619141,196.4980545043945,196.4980545043945,196.4980545043945,196.7668609619141,196.7668609619141,197.0002746582031,197.0002746582031,197.0886993408203,197.0886993408203,197.0886993408203,197.0886993408203,197.0886993408203,197.0886993408203,194.0534286499023,194.2352447509766,194.2352447509766,194.2352447509766,194.420524597168,194.618766784668,194.8309631347656,194.8309631347656,195.0595016479492,195.2951278686523,195.2951278686523,195.2951278686523,195.5279769897461,195.5279769897461,195.5279769897461,195.75927734375,195.75927734375,195.9917526245117,195.9917526245117,196.223014831543,196.223014831543,196.4562225341797,196.4562225341797,196.6889724731445,196.6889724731445,196.922477722168,196.922477722168,197.1452102661133,197.1782608032227,197.1782608032227,197.1782608032227,197.1782608032227,194.2269515991211,194.2269515991211,194.4089431762695,194.4089431762695,194.4089431762695,194.5938949584961,194.5938949584961,194.5938949584961,194.8144683837891,194.8144683837891,195.0317001342773,195.0317001342773,195.2644195556641,195.2644195556641,195.4995193481445,195.4995193481445,195.7313537597656,195.7313537597656,195.9633026123047,195.9633026123047,196.1979751586914,196.435188293457,196.435188293457,196.6715621948242,196.6715621948242,196.9137954711914,197.1490020751953,197.1490020751953,197.1490020751953,197.2663879394531,197.2663879394531,197.2663879394531,197.2663879394531,197.2663879394531,197.2663879394531,194.2605667114258,194.2605667114258,194.4322052001953,194.4322052001953,194.6037979125977,194.6037979125977,194.7881164550781,194.7881164550781,194.9496765136719,194.9496765136719,195.1405792236328,195.1405792236328,195.3508453369141,195.3508453369141,195.5746002197266,195.5746002197266,195.7939300537109,195.7939300537109,196.0041122436523,196.0041122436523,196.2177200317383,196.2177200317383,196.4415817260742,196.4415817260742,196.4415817260742,196.6551361083984,196.6551361083984,196.6551361083984,196.8825302124023,197.0985412597656,197.0985412597656,197.3032150268555,197.3032150268555,197.3530731201172,197.3530731201172,197.3530731201172,197.3530731201172,194.4508819580078,194.4508819580078,194.5980606079102,194.7769317626953,194.7769317626953,194.9410095214844,195.1248550415039,195.1248550415039,195.3340225219727,195.3340225219727,195.5239105224609,195.5239105224609,195.5239105224609,195.7369689941406,195.9567718505859,195.9567718505859,196.1671905517578,196.1671905517578,196.4022064208984,196.6150054931641,196.6150054931641,196.6150054931641,196.8350982666016,196.8350982666016,197.0624923706055,197.0624923706055,197.267951965332,197.267951965332,197.4383773803711,197.4383773803711,197.4383773803711,197.4383773803711,197.4383773803711,197.4383773803711,197.4383773803711,197.4383773803711,197.4383773803711,194.6317367553711,194.6317367553711,194.7818145751953,194.9750137329102,195.1423645019531,195.1423645019531,195.3212280273438,195.5315704345703,195.5315704345703,195.7319717407227,195.7319717407227,195.7319717407227,195.9551773071289,195.9551773071289,195.9551773071289,196.1821670532227,196.4085845947266,196.4085845947266,196.635124206543,196.635124206543,196.8586807250977,197.0841903686523,197.0841903686523,197.3095016479492,197.3095016479492,197.522331237793,197.522331237793,197.522331237793,197.522331237793,197.522331237793,197.522331237793,194.7722396850586,194.7722396850586,194.963134765625,194.963134765625,195.1465148925781,195.1465148925781,195.1465148925781,195.3416900634766,195.5543746948242,195.780029296875,195.9926681518555,195.9926681518555,195.9926681518555,196.2187042236328,196.2187042236328,196.4008636474609,196.6227874755859,196.6227874755859,196.8389587402344,197.0572662353516,197.0572662353516,197.2686996459961,197.4901504516602,197.6048049926758,197.6048049926758,197.6048049926758,197.6048049926758,194.7956314086914,194.7956314086914,194.9360198974609,194.9360198974609,195.1163787841797,195.1163787841797,195.2616195678711,195.4404983520508,195.4404983520508,195.6354751586914,195.6354751586914,195.8230209350586,196.0447769165039,196.262077331543,196.262077331543,196.4651031494141,196.4651031494141,196.6932754516602,196.8913879394531,197.116455078125,197.3411331176758,197.5588455200195,197.5588455200195,197.6860809326172,197.6860809326172,197.6860809326172,197.6860809326172,197.6860809326172,197.6860809326172,194.9332962036133,194.9332962036133,195.072509765625,195.1658020019531,195.1658020019531,195.3183441162109,195.4932403564453,195.4932403564453,195.65625,195.65625,195.7362747192383,195.7362747192383,195.8371810913086,195.8371810913086,195.8371810913086,195.930778503418,196.0191955566406,196.0191955566406,196.1172332763672,196.1172332763672,196.2228775024414,196.2228775024414,196.4288635253906,196.4288635253906,196.6216049194336,196.8218231201172,196.8218231201172,197.0449752807617,197.0449752807617,197.2773208618164,197.2773208618164,197.2773208618164,197.510498046875,197.510498046875,197.7314682006836,197.7314682006836,197.7660064697266,197.7660064697266,197.7660064697266,197.7660064697266,197.7660064697266,197.7660064697266,195.1268310546875,195.1268310546875,195.3223037719727,195.3223037719727,195.5074234008789,195.5074234008789,195.5074234008789,195.7067413330078,195.9238052368164,196.1571884155273,196.3921508789062,196.6252288818359,196.6252288818359,196.8535461425781,197.0884399414062,197.3239288330078,197.3239288330078,197.5597229003906,197.7863235473633,197.7863235473633,197.8445816040039,197.8445816040039,197.8445816040039,197.8445816040039,197.8445816040039,197.8445816040039,195.1913986206055,195.3638916015625,195.3638916015625,195.5448379516602,195.5448379516602,195.5448379516602,195.7340240478516,195.7340240478516,195.939697265625,195.939697265625,196.1639556884766,196.3978729248047,196.631706237793,196.631706237793,196.8625259399414,197.0946807861328,197.3485565185547,197.3485565185547,197.5799789428711,197.5799789428711,197.8072204589844,197.8072204589844,197.9219818115234,197.9219818115234,197.9219818115234,197.9219818115234,195.3156814575195,195.4935684204102,195.4935684204102,195.4935684204102,195.6753692626953,195.6753692626953,195.6753692626953,195.872802734375,195.872802734375,196.086540222168,196.086540222168,196.3179321289062,196.3179321289062,196.555305480957,196.7913208007812,197.0222473144531,197.254997253418,197.254997253418,197.4873046875,197.7198486328125,197.7198486328125,197.9460144042969,197.9460144042969,197.9980163574219,197.9980163574219,197.9980163574219,197.9980163574219,195.4832382202148,195.6630554199219,195.6630554199219,195.6630554199219,195.8487243652344,195.8487243652344,196.0473937988281,196.2460098266602,196.2460098266602,196.4411163330078,196.4411163330078,196.6705703735352,196.9049453735352,197.135627746582,197.3681640625,197.3681640625,197.3681640625,197.5994567871094,197.5994567871094,197.8321075439453,197.8321075439453,198.0281677246094,198.0730209350586,198.0730209350586,198.0730209350586,198.0730209350586,195.582389831543,195.582389831543,195.7570037841797,195.7570037841797,195.9261474609375,196.114501953125,196.3176956176758,196.3176956176758,196.5376815795898,196.7724914550781,196.7724914550781,196.7724914550781,197.0070953369141,197.0070953369141,197.2398300170898,197.4730224609375,197.4730224609375,197.7040863037109,197.7040863037109,197.9581604003906,198.1466369628906,198.1466369628906,198.1466369628906,198.1466369628906,198.1466369628906,198.1466369628906,198.1466369628906,198.1466369628906,198.1466369628906,195.7776947021484,195.7776947021484,195.9541778564453,196.1379470825195,196.1379470825195,196.333625793457,196.333625793457,196.5475616455078,196.7743988037109,196.7743988037109,197.0097122192383,197.0097122192383,197.2422180175781,197.2422180175781,197.4738540649414,197.4738540649414,197.7058868408203,197.9388427734375,197.9388427734375,198.1631164550781,198.1631164550781,198.2191314697266,198.2191314697266,198.2191314697266,198.2191314697266,198.2191314697266,198.2191314697266,195.8152770996094,195.8152770996094,195.9924926757812,196.1729507446289,196.3517608642578,196.5620880126953,196.5620880126953,196.765510559082,196.765510559082,196.9757080078125,196.9757080078125,197.1950302124023,197.1950302124023,197.3953247070312,197.5991744995117,197.5991744995117,197.8116073608398,198.0173873901367,198.2302322387695,198.2302322387695,198.2904434204102,198.2904434204102,198.2904434204102,198.2904434204102,195.8788986206055,195.8788986206055,196.0408935546875,196.2180557250977,196.3945846557617,196.3945846557617,196.5947036743164,196.7904891967773,196.7904891967773,196.99560546875,196.99560546875,197.182014465332,197.182014465332,197.3149566650391,197.4732360839844,197.6592712402344,197.6592712402344,197.8468246459961,198.0507278442383,198.0507278442383,198.2556991577148,198.2556991577148,198.3606338500977,198.3606338500977,198.3606338500977,198.3606338500977,198.3606338500977,198.3606338500977,198.3606338500977,198.3606338500977,198.3606338500977,196.0844345092773,196.2571563720703,196.4230499267578,196.4230499267578,196.6131439208984,196.7985534667969,196.9856109619141,196.9856109619141,197.196907043457,197.196907043457,197.3927383422852,197.3927383422852,197.3927383422852,197.6080856323242,197.6080856323242,197.8139266967773,197.8139266967773,198.0103912353516,198.0103912353516,198.2307891845703,198.2307891845703,198.4275665283203,198.4296188354492,198.4296188354492,198.4296188354492,198.4296188354492,198.4296188354492,198.4296188354492,198.4296188354492,198.4296188354492,198.4296188354492,198.4296188354492,198.4296188354492,198.4296188354492,198.4296188354492,198.4296188354492,198.4296188354492,198.4296188354492,198.4296188354492,198.4296188354492,198.4296188354492,198.4296188354492,198.4296188354492,198.4296188354492,198.4296188354492,198.4296188354492,198.4296188354492,198.4296188354492,198.4296188354492,198.4296188354492,198.4296188354492,198.4296188354492,198.4296188354492,198.4296188354492,198.4296188354492,198.4296188354492,198.4296188354492,198.4296188354492,198.4296188354492,198.4296188354492,198.4296188354492,196.0534973144531,196.0534973144531,196.0534973144531,196.0954895019531,196.2433700561523,196.2433700561523,196.3973159790039,196.5458908081055,196.5458908081055,196.7306442260742,196.9003295898438,197.1041259765625,197.3188400268555,197.3188400268555,197.5068206787109,197.5068206787109,197.7114181518555,197.7114181518555,197.8870468139648,197.8870468139648,198.0793533325195,198.0793533325195,198.2515640258789,198.2515640258789,198.4022979736328,198.4972152709961,198.4972152709961,198.4972152709961,198.4972152709961,198.4972152709961,198.4972152709961,196.1599655151367,196.1599655151367,196.326774597168,196.4828948974609,196.6597442626953,196.6597442626953,196.833625793457,196.833625793457,197.0168151855469,197.0168151855469,197.2177581787109,197.2177581787109,197.4106216430664,197.4106216430664,197.6231460571289,197.8434677124023,198.0500259399414,198.0500259399414,198.2753143310547,198.2753143310547,198.4848709106445,198.4848709106445,198.5640487670898,198.5640487670898,198.5640487670898,198.5640487670898,196.3241348266602,196.3241348266602,196.4949188232422,196.4949188232422,196.6658020019531,196.6658020019531,196.8440933227539,196.8440933227539,197.0278091430664,197.0278091430664,197.2115173339844,197.2115173339844,197.4153137207031,197.4153137207031,197.6162033081055,197.6162033081055,197.8303070068359,197.8303070068359,198.0478515625,198.0478515625,198.2531585693359,198.2531585693359,198.4758453369141,198.4758453369141,198.4758453369141,198.6298904418945,198.6298904418945,198.6298904418945,198.6298904418945,198.6298904418945,198.6298904418945,196.4984359741211,196.4984359741211,196.6735458374023,196.8215255737305,196.8215255737305,196.9851913452148,196.9851913452148,197.1677551269531,197.3652725219727,197.3652725219727,197.5838088989258,197.5838088989258,197.8112335205078,198.04248046875,198.04248046875,198.2739562988281,198.5035858154297,198.5035858154297,198.6945266723633,198.6945266723633,198.6945266723633,198.6945266723633,198.6945266723633,198.6945266723633,198.6945266723633,198.6945266723633,198.6945266723633,196.6148452758789,196.8093032836914,196.9909973144531,196.9909973144531,196.9909973144531,197.1875381469727,197.1875381469727,197.1875381469727,197.4018936157227,197.6327514648438,197.6327514648438,197.8694763183594,198.1033172607422,198.3323822021484,198.582893371582,198.582893371582,198.7582168579102,198.7582168579102,198.7582168579102,198.7582168579102,198.7582168579102,198.7582168579102,198.7582168579102,198.7582168579102,198.7582168579102,196.7345962524414,196.7345962524414,196.7345962524414,196.9095153808594,196.9095153808594,197.0907821655273,197.0907821655273,197.2890930175781,197.2890930175781,197.2890930175781,197.5033950805664,197.7379379272461,197.9626007080078,197.9626007080078,198.1945953369141,198.1945953369141,198.4263916015625,198.4263916015625,198.655632019043,198.8208312988281,198.8208312988281,198.8208312988281,198.8208312988281,198.8208312988281,198.8208312988281,198.8208312988281,198.8208312988281,196.6779861450195,196.8480453491211,196.8480453491211,196.8480453491211,197.0245513916016,197.0245513916016,197.211311340332,197.211311340332,197.4125518798828,197.4125518798828,197.4125518798828,197.6320953369141,197.6320953369141,197.8689575195312,197.8689575195312,198.1007614135742,198.1007614135742,198.3338470458984,198.5641937255859,198.5641937255859,198.7939453125,198.8824615478516,198.8824615478516,198.8824615478516,198.8824615478516,196.8057403564453,196.8057403564453,196.8057403564453,196.972900390625,197.1528778076172,197.3407669067383,197.3407669067383,197.5401000976562,197.5401000976562,197.7542343139648,197.9789962768555,197.9789962768555,198.2168960571289,198.4517517089844,198.6838531494141,198.6838531494141,198.9102172851562,198.9102172851562,198.9430389404297,198.9430389404297,198.9430389404297,198.9430389404297,198.9430389404297,198.9430389404297,196.9441070556641,196.9441070556641,197.1115493774414,197.1115493774414,197.297981262207,197.4880905151367,197.4880905151367,197.4880905151367,197.6823577880859,197.6823577880859,197.8883285522461,198.0774383544922,198.2877807617188,198.4828414916992,198.6900787353516,198.6900787353516,198.900016784668,199.0027770996094,199.0027770996094,199.0027770996094,199.0027770996094,196.9527206420898,196.9527206420898,197.1002731323242,197.2687683105469,197.2687683105469,197.4401931762695,197.4401931762695,197.4401931762695,197.6170501708984,197.7964248657227,197.7964248657227,197.975212097168,197.975212097168,198.1792297363281,198.3515930175781,198.3515930175781,198.5592498779297,198.7595748901367,198.9443054199219,199.061408996582,199.061408996582,199.061408996582,199.061408996582,199.061408996582,199.061408996582,197.0429458618164,197.0429458618164,197.2068939208984,197.2068939208984,197.3737182617188,197.5383148193359,197.5383148193359,197.7271575927734,197.7271575927734,197.9013748168945,197.9013748168945,198.0938720703125,198.2935638427734,198.4987106323242,198.4987106323242,198.6936721801758,198.6936721801758,198.9050140380859,199.1191940307617,199.1191940307617,199.1191940307617,199.1191940307617,199.1191940307617,199.1191940307617,199.1191940307617,199.1191940307617,199.1191940307617,197.204216003418,197.204216003418,197.3498611450195,197.3498611450195,197.5294036865234,197.5294036865234,197.7102737426758,197.7102737426758,197.9019165039062,197.9019165039062,198.1035308837891,198.1035308837891,198.2992401123047,198.5220260620117,198.7394561767578,198.7394561767578,198.9614334106445,198.9614334106445,199.1759262084961,199.1759262084961,199.1759262084961,199.1759262084961,199.1759262084961,199.1759262084961,197.2964782714844,197.2964782714844,197.4684753417969,197.4684753417969,197.4684753417969,197.6660995483398,197.6660995483398,197.857536315918,197.857536315918,198.0626068115234,198.0626068115234,198.2858428955078,198.2858428955078,198.5209884643555,198.5209884643555,198.5209884643555,198.7555847167969,198.7555847167969,198.987922668457,198.987922668457,199.2202453613281,199.2202453613281,199.2318572998047,199.2318572998047,199.2318572998047,199.2318572998047,199.2318572998047,199.2318572998047,197.4079742431641,197.5805206298828,197.5805206298828,197.7634811401367,197.955680847168,197.955680847168,198.1606521606445,198.1606521606445,198.385612487793,198.385612487793,198.6228408813477,198.8589248657227,199.0938186645508,199.0938186645508,199.2868576049805,199.2868576049805,199.2868576049805,199.2868576049805,199.2868576049805,199.2868576049805,199.2868576049805,199.2868576049805,199.2868576049805,197.5487594604492,197.7251129150391,197.913932800293,198.1099243164062,198.1099243164062,198.3215560913086,198.5517425537109,198.5517425537109,198.5517425537109,198.7905349731445,199.0145111083984,199.2487716674805,199.3408889770508,199.3408889770508,199.3408889770508,199.3408889770508,199.3408889770508,199.3408889770508,199.3408889770508,199.3408889770508,199.3408889770508,199.3408889770508,199.3408889770508,199.3408889770508,199.3408889770508,199.3408889770508,199.3408889770508,199.3408889770508,199.3408889770508,199.3408889770508,199.3408889770508,199.3408889770508,199.3408889770508,199.3408889770508,199.3408889770508,199.3408889770508,197.5865249633789,197.5865249633789,197.7605438232422,197.9129638671875,197.9129638671875,198.080810546875,198.2184295654297,198.2184295654297,198.3249435424805,198.3249435424805,198.4286956787109,198.4286956787109,198.5790328979492,198.5790328979492,198.7376022338867,198.9233016967773,198.9233016967773,199.0864944458008,199.0864944458008,199.2075729370117,199.2075729370117,199.3906555175781,199.3906555175781,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,199.3939437866211,197.5622634887695,197.5622634887695,197.5622634887695,197.5622634887695,197.5622634887695,197.5622634887695,197.5622634887695,197.5622634887695,197.5622634887695,197.6701812744141,197.6701812744141,197.8537826538086,197.8537826538086,198.0415420532227,198.2383575439453,198.2383575439453,198.4567184448242,198.6902770996094,198.6902770996094,198.921012878418,198.921012878418,199.1336364746094,199.3399963378906,199.3399963378906,199.5646057128906,199.5646057128906,199.7895812988281,199.7895812988281,200.015754699707,200.015754699707,200.2502593994141,200.4858551025391,200.4858551025391,200.7206420898438,200.9579086303711,200.9579086303711,201.1921691894531,201.1921691894531,201.4223709106445,201.613883972168,201.8073654174805,201.8073654174805,201.9971008300781,201.9971008300781,202.1911849975586,202.1911849975586,202.3807373046875,202.5952682495117,202.5952682495117,202.7853088378906,202.7853088378906,202.9788436889648,203.1694107055664,203.3629989624023,203.3629989624023,203.5541229248047,203.5541229248047,203.7478332519531,203.7478332519531,203.93115234375,203.93115234375,204.1177520751953,204.1177520751953,204.2991485595703,204.2991485595703,204.4867630004883,204.4867630004883,204.6710357666016,204.8527526855469,204.8527526855469,205.0388259887695,205.1746520996094,205.1746520996094,205.1746520996094,205.1746520996094,205.1746520996094,205.1746520996094,197.9446563720703,197.9446563720703,198.1376342773438,198.1376342773438,198.1376342773438,198.3366394042969,198.3366394042969,198.5522613525391,198.8090057373047,198.8090057373047,199.0417556762695,199.2639923095703,199.4716033935547,199.4716033935547,199.7032089233398,199.7032089233398,199.9343566894531,199.9343566894531,200.1659622192383,200.1659622192383,200.3966903686523,200.6297836303711,200.6297836303711,200.863525390625,201.0965118408203,201.0965118408203,201.330924987793,201.330924987793,201.5662612915039,201.5662612915039,201.7989883422852,201.7989883422852,202.0345840454102,202.0345840454102,202.2667617797852,202.2667617797852,202.5017013549805,202.7384185791016,202.7384185791016,202.9695358276367,202.9695358276367,203.2025527954102,203.2025527954102,203.4358291625977,203.6691589355469,203.6691589355469,203.9044952392578,203.9044952392578,204.1382064819336,204.1382064819336,204.3733444213867,204.3733444213867,204.6314544677734,204.6314544677734,204.8213806152344,204.8213806152344,205.0258178710938,205.2431869506836,205.2431869506836,205.2431869506836,205.3828887939453,205.3828887939453,205.3828887939453,205.3828887939453,205.3828887939453,205.3828887939453,205.3828887939453,205.3828887939453,205.3828887939453,198.2864990234375,198.4757308959961,198.6752395629883,198.6752395629883,198.8819274902344,198.8819274902344,199.1029434204102,199.324089050293,199.5422286987305,199.5422286987305,199.5422286987305,199.7603225708008,199.9928283691406,199.9928283691406,200.2251739501953,200.2251739501953,200.4594192504883,200.694221496582,200.694221496582,200.9286804199219,200.9286804199219,200.9286804199219,201.1864700317383,201.1864700317383,201.422607421875,201.659912109375,201.659912109375,201.9055862426758,202.1403198242188,202.1403198242188,202.3756332397461,202.3756332397461,202.6081237792969,202.6081237792969,202.8422393798828,202.8422393798828,202.8422393798828,203.0801696777344,203.0801696777344,203.3183288574219,203.3183288574219,203.553825378418,203.553825378418,203.7885513305664,204.0224914550781,204.0224914550781,204.2573699951172,204.494514465332,204.494514465332,204.7319107055664,204.7319107055664,204.9775314331055,205.2111511230469,205.2111511230469,205.4406280517578,205.5877304077148,205.5877304077148,205.5877304077148,205.5877304077148,205.5877304077148,205.5877304077148,205.5877304077148,205.5877304077148,205.5877304077148,198.597038269043,198.597038269043,198.784065246582,198.784065246582,198.9804763793945,199.1840286254883,199.3971786499023,199.3971786499023,199.5544586181641,199.7419967651367,199.7419967651367,199.7419967651367,199.9521942138672,200.1819610595703,200.4147644042969,200.4147644042969,200.6467437744141,200.6467437744141,200.8785629272461,200.8785629272461,201.1136703491211,201.1136703491211,201.3486480712891,201.3486480712891,201.5929107666016,201.5929107666016,201.8287353515625,201.8287353515625,202.0618209838867,202.0618209838867,202.2760238647461,202.4404602050781,202.4404602050781,202.6747741699219,202.6747741699219,202.9043579101562,203.1367340087891,203.1367340087891,203.3700103759766,203.6026229858398,203.8362121582031,203.8362121582031,203.8362121582031,204.0929489135742,204.0929489135742,204.3354263305664,204.3354263305664,204.5684661865234,204.5684661865234,204.7993850708008,204.7993850708008,205.0322952270508,205.2645797729492,205.2645797729492,205.4859008789062,205.7087097167969,205.7087097167969,205.7087097167969,205.7892456054688,205.7892456054688,205.7892456054688,205.7892456054688,205.7892456054688,205.7892456054688,205.7892456054688,205.7892456054688,205.7892456054688,198.9521942138672,199.1443481445312,199.3435134887695,199.5538787841797,199.5538787841797,199.7702560424805,199.7702560424805,199.9865570068359,199.9865570068359,200.2159042358398,200.2159042358398,200.4507293701172,200.4507293701172,200.4507293701172,200.6846008300781,200.9172821044922,200.9172821044922,201.1477432250977,201.1477432250977,201.3800811767578,201.6183853149414,201.8589553833008,202.1226425170898,202.1226425170898,202.3575439453125,202.5851821899414,202.5851821899414,202.8143844604492,202.8143844604492,202.8143844604492,203.0472259521484,203.0472259521484,203.2790908813477,203.5104904174805,203.5104904174805,203.7444076538086,203.7444076538086,203.9755477905273,203.9755477905273,204.2081756591797,204.2081756591797,204.4391555786133,204.6705551147461,204.6705551147461,204.9041442871094,204.9041442871094,205.1362686157227,205.1362686157227,205.3695220947266,205.3695220947266,205.5872421264648,205.5872421264648,205.8053665161133,205.8053665161133,205.9875106811523,205.9875106811523,205.9875106811523,205.9875106811523,205.9875106811523,205.9875106811523,205.9875106811523,205.9875106811523,205.9875106811523,205.9875106811523,205.9875106811523,205.9875106811523,205.9875106811523,205.9875106811523,205.9875106811523,205.9875106811523,199.326545715332,199.5365905761719,199.5365905761719,199.734001159668,199.734001159668,199.9330673217773,200.1343307495117,200.3477096557617,200.5854263305664,200.5854263305664,200.8148040771484,200.8148040771484,201.0483169555664,201.0483169555664,201.2785568237305,201.2785568237305,201.507942199707,201.507942199707,201.7418212890625,201.7418212890625,201.7418212890625,201.97314453125,202.2045288085938,202.4337005615234,202.4337005615234,202.6618423461914,202.6618423461914,202.6618423461914,202.8925857543945,202.8925857543945,203.1221542358398,203.1221542358398,203.3474044799805,203.3474044799805,203.5762252807617,203.5762252807617,203.8048934936523,203.8048934936523,203.8048934936523,204.0368499755859,204.2606506347656,204.493278503418,204.493278503418,204.7501754760742,204.7501754760742,204.9828567504883,204.9828567504883,205.2183303833008,205.4472808837891,205.6763305664062,205.6763305664062,205.8967361450195,205.8967361450195,206.1163024902344,206.1163024902344,206.1825942993164,206.1825942993164,206.1825942993164,206.1825942993164,206.1825942993164,206.1825942993164,206.1825942993164,206.1825942993164,206.1825942993164,199.5068817138672,199.6666870117188,199.6666870117188,199.8544540405273,199.8544540405273,200.0441589355469,200.0441589355469,200.0441589355469,200.2293014526367,200.2293014526367,200.4156036376953,200.6191558837891,200.8404388427734,200.8404388427734,201.0684509277344,201.3216018676758,201.3216018676758,201.5533905029297,201.5533905029297,201.7813720703125,201.7813720703125,202.013313293457,202.013313293457,202.2420272827148,202.4682159423828,202.698112487793,202.9289474487305,203.1593475341797,203.1593475341797,203.387321472168,203.387321472168,203.387321472168,203.6154098510742,203.6154098510742,203.8455200195312,203.8455200195312,204.0762100219727,204.0762100219727,204.3081893920898,204.3081893920898,204.537956237793,204.7672348022461,204.7672348022461,204.9994659423828,205.2315444946289,205.4649276733398,205.6981735229492,205.6981735229492,205.9202575683594,206.1401596069336,206.3596954345703,206.3596954345703,206.3744888305664,206.3744888305664,206.3744888305664,206.3744888305664,206.3744888305664,206.3744888305664,206.3744888305664,206.3744888305664,206.3744888305664,206.3744888305664,206.3744888305664,206.3744888305664,206.3744888305664,206.3744888305664,206.3744888305664,206.3744888305664,206.3744888305664,206.3744888305664,206.3744888305664,206.3744888305664,206.3744888305664,206.3744888305664,199.8457260131836,199.9917221069336,200.1716461181641,200.1716461181641,200.3591690063477,200.3591690063477,200.5443115234375,200.5443115234375,200.7320861816406,200.7320861816406,200.9633331298828,201.1891403198242,201.4234313964844,201.4234313964844,201.6556167602539,201.6556167602539,201.6556167602539,201.8874053955078,201.8874053955078,202.1170883178711,202.1170883178711,202.3145141601562,202.3145141601562,202.5438766479492,202.5438766479492,202.5438766479492,202.7740859985352,202.7740859985352,203.0008316040039,203.0008316040039,203.2254104614258,203.2254104614258,203.45751953125,203.6780776977539,203.9078369140625,203.9078369140625,204.1312713623047,204.3546524047852,204.5876159667969,204.8125991821289,204.8125991821289,205.0462036132812,205.2730941772461,205.2730941772461,205.49853515625,205.49853515625,205.49853515625,205.7342147827148,205.7342147827148,205.9607391357422,205.9607391357422,206.1848678588867,206.1848678588867,206.4238891601562,206.5633544921875,206.5633544921875,206.5633544921875,206.5633544921875,206.5633544921875,206.5633544921875,206.5633544921875,206.5633544921875,206.5633544921875,206.5633544921875,206.5633544921875,206.5633544921875,200.1863327026367,200.1863327026367,200.3665924072266,200.5497589111328,200.5497589111328,200.7299652099609,200.7299652099609,200.9097290039062,201.1098175048828,201.3272323608398,201.5503234863281,201.5503234863281,201.777214050293,201.777214050293,202.0127105712891,202.0127105712891,202.2355270385742,202.2355270385742,202.468017578125,202.468017578125,202.6963653564453,202.9217529296875,203.155517578125,203.4062957763672,203.4062957763672,203.4062957763672,203.636360168457,203.636360168457,203.8636016845703,203.8636016845703,204.0885543823242,204.0885543823242,204.0885543823242,204.3219833374023,204.5502014160156,204.5502014160156,204.7811431884766,204.7811431884766,205.0126266479492,205.0126266479492,205.2408294677734,205.4767608642578,205.4767608642578,205.7078857421875,205.942253112793,205.942253112793,206.1750030517578,206.3949813842773,206.3949813842773,206.6115188598633,206.749137878418,206.749137878418,206.749137878418,206.749137878418,206.749137878418,206.749137878418,206.749137878418,206.749137878418,206.749137878418,206.749137878418,206.749137878418,206.749137878418,200.4917449951172,200.4917449951172,200.6726989746094,200.6726989746094,200.859001159668,200.859001159668,201.057991027832,201.057991027832,201.2538452148438,201.2538452148438,201.4747619628906,201.4747619628906,201.6990051269531,201.9306564331055,201.9306564331055,201.9306564331055,202.1616287231445,202.3902206420898,202.3902206420898,202.6244659423828,202.8489608764648,202.8489608764648,203.0780715942383,203.3065567016602,203.3065567016602,203.5336685180664,203.5336685180664,203.7694625854492,203.7694625854492,203.998291015625,203.998291015625,203.998291015625,204.2282104492188,204.2282104492188,204.4604949951172,204.4604949951172,204.6857833862305,204.6857833862305,204.9189910888672,204.9189910888672,205.1478805541992,205.3838424682617,205.3838424682617,205.6188201904297,205.6188201904297,205.8488693237305,205.8488693237305,205.8488693237305,206.0850982666016,206.320182800293,206.320182800293,206.5475921630859,206.5475921630859,206.7699279785156,206.7699279785156,206.9319381713867,206.9319381713867,206.9319381713867,206.9319381713867,206.9319381713867,206.9319381713867,206.9319381713867,206.9319381713867,206.9319381713867,206.9319381713867,206.9319381713867,206.9319381713867,200.7942123413086,200.9751586914062,200.9751586914062,201.1597290039062,201.1597290039062,201.3383941650391,201.3383941650391,201.5381240844727,201.5381240844727,201.75634765625,201.9809799194336,201.9809799194336,202.2113571166992,202.2113571166992,202.4339294433594,202.6567153930664,202.6567153930664,202.8811492919922,202.8811492919922,203.1033248901367,203.1033248901367,203.3315963745117,203.3315963745117,203.5766220092773,203.5766220092773,203.8001861572266,204.0310668945312,204.0310668945312,204.2804718017578,212.054817199707,212.054817199707,212.054817199707,212.054817199707,212.054817199707,212.054817199707,212.054817199707,212.054817199707,212.054817199707,212.054817199707,212.054817199707,212.054817199707,212.054817199707,212.054817199707,212.054817199707,212.054817199707,212.054817199707,212.054817199707,212.054817199707,212.054817199707,212.054817199707,212.054817199707,212.054817199707,212.054817199707,212.054817199707,212.054817199707,219.684211730957,219.6842193603516,219.6842193603516,219.6842193603516,219.6842193603516,219.6842193603516,219.6842193603516,219.6842193603516,219.6842193603516,219.6842193603516,219.6842193603516,219.6842193603516,219.6842193603516,219.6842193603516,219.6842193603516,219.6842193603516,219.6842193603516,219.6842193603516,219.6842193603516,219.6842193603516,219.6842193603516,219.6842193603516,219.6842193603516,219.6842193603516,219.6842193603516,219.6842193603516,219.6842193603516,219.6842193603516,219.6842193603516,234.9430084228516,234.9430084228516,234.9430084228516,234.9430084228516,234.9430084228516,234.9430084228516,234.9430084228516,234.9430084228516,234.9430084228516,234.9430084228516,234.9430084228516,234.9430084228516,234.9430084228516,234.9430084228516,234.9430084228516,234.9430084228516,234.9430084228516,234.9430084228516,234.9430084228516,234.9430084228516,242.5724258422852,242.5724258422852,242.5724258422852,242.5724258422852,242.5724258422852,242.5724258422852,242.5724258422852,242.5724258422852,242.6263275146484,242.6263275146484,242.6263275146484,242.6263275146484,242.6263275146484,242.6263275146484,242.6263275146484,242.6263275146484,242.6263275146484,242.6263275146484,242.6263275146484,242.6263275146484,242.6263275146484,242.6263275146484,242.6263275146484,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094,257.9676208496094],"meminc":[0,0,0,0,0,2.288818359375e-05,0,15.28221130371094,0,0,0,0,0.0003662109375,0,0,30.46537780761719,0,0,0,0,0,0,0,0,0,4.57763671875e-05,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-0.00030517578125,0,15.2587890625,0.1685409545898438,0,0.1993179321289062,0,0,0.2013778686523438,0.22430419921875,0.2344741821289062,0,0,0.2391510009765625,0,0.2627105712890625,0,0.2250518798828125,0.2252731323242188,0.2288589477539062,0.2360610961914062,0.2378311157226562,0,0.2380599975585938,0,0.142333984375,0,0,-2.889801025390625,0,0.2243270874023438,0,0.243316650390625,0,0.2426834106445312,0.2443008422851562,0,0.2442245483398438,0,0.2471389770507812,0.2423171997070312,0,0.236053466796875,0.2324295043945312,0,0.232330322265625,0,0.2328414916992188,0,0.2304000854492188,0,0.1018295288085938,0,0,-2.7916259765625,0,0.2268905639648438,0,0.24041748046875,0,0,0.241241455078125,0,0.2409286499023438,0.2627029418945312,0,0.2342453002929688,0,0.2304229736328125,0,0.21588134765625,0.230224609375,0.2314529418945312,0.2326126098632812,0.2301254272460938,0.0562744140625,0,0,0,-2.712165832519531,0.2173614501953125,0,0.2407608032226562,0,0,0.2414321899414062,0,0.2416305541992188,0,0.2383193969726562,0,0,0.2343063354492188,0.2305679321289062,0,0.231414794921875,0,0.2300491333007812,0,0.2314529418945312,0,0.2325592041015625,0.2227935791015625,0,0,0,0,0,-2.577377319335938,0.2340316772460938,0,0.2405624389648438,0,0.2389984130859375,0.239715576171875,0,0.260040283203125,0.2425689697265625,0,0.2344436645507812,0.2231979370117188,0,0.2277374267578125,0,0,0.2323226928710938,0,0.2316207885742188,0,0.05126953125,0,0,-2.594444274902344,0,0.2256393432617188,0,0.2394180297851562,0.2401809692382812,0,0,0.2386398315429688,0,0.235137939453125,0,0.2367019653320312,0,0.2289962768554688,0,0.2297134399414062,0,0.2286529541015625,0,0.2300872802734375,0,0.23040771484375,0.1087799072265625,0,0,-2.607803344726562,0,0.224395751953125,0,0.2394790649414062,0.2402572631835938,0,0.2381973266601562,0.23565673828125,0.2342605590820312,0.2350692749023438,0,0.25128173828125,0,0.2280731201171875,0.229217529296875,0,0.229522705078125,0,0.0990142822265625,0,0,-2.559577941894531,0,0,0.2216262817382812,0,0.2177963256835938,0,0.2343673706054688,0,0.2374496459960938,0,0,0.236175537109375,0,0.2332305908203125,0,0.2291336059570312,0.2295379638671875,0,0.2298736572265625,0,0.2289962768554688,0,0.2302093505859375,0,0.1065750122070312,0,0,-2.529296875,0.2209854125976562,0,0.23602294921875,0.2387771606445312,0,0,0.2365188598632812,0.2340850830078125,0.229766845703125,0.2229156494140625,0.21630859375,0.228363037109375,0.2478179931640625,0,0.2295303344726562,0,0.06241607666015625,0,-2.504287719726562,0,0.1823043823242188,0,0.1750869750976562,0,0.183441162109375,0,0.2010421752929688,0,0.2215042114257812,0.21337890625,0.220977783203125,0.226593017578125,0.2037277221679688,0.22607421875,0,0.21893310546875,0,0.2209396362304688,0,0.08322906494140625,0,-2.435127258300781,0.2028732299804688,0,0,0.2072296142578125,0,0.21868896484375,0,0.2218093872070312,0.2203521728515625,0,0,0.2342529296875,0,0.224945068359375,0.2264251708984375,0,0.2328643798828125,0.2107009887695312,0,0,0.2340774536132812,0,0.07282257080078125,0,0,-2.409629821777344,0,0.2036895751953125,0,0,0.19183349609375,0.2198333740234375,0,0,0.2114181518554688,0.2105865478515625,0,0.2576065063476562,0,0.1867599487304688,0.2221450805664062,0.2089462280273438,0,0.1986465454101562,0,0,0.2263336181640625,0.1424331665039062,0,-2.422157287597656,0.2109375,0,0.22222900390625,0.2311859130859375,0.2356796264648438,0,0.2313003540039062,0,0.23162841796875,0,0,0.2372589111328125,0,0.236328125,0,0.234283447265625,0,0.24078369140625,0.1800460815429688,0,0,0,-2.172584533691406,0.2245559692382812,0,0.23162841796875,0,0.2129058837890625,0.2235488891601562,0,0.2303390502929688,0,0.2323989868164062,0.2306976318359375,0,0.2323150634765625,0.2321548461914062,0,0.1904830932617188,0,0,0,-2.183364868164062,0.2140121459960938,0,0.2265548706054688,0,0.2311019897460938,0,0.2351531982421875,0,0,0.2349472045898438,0,0.2317428588867188,0.2285308837890625,0,0.2295303344726562,0,0,0.22882080078125,0,0,0.19024658203125,0,0,0,0,0,-2.110557556152344,0.2205734252929688,0.2275238037109375,0,0.230804443359375,0,0.2328033447265625,0,0.2335739135742188,0,0.230987548828125,0.2285690307617188,0.2334365844726562,0,0.2333450317382812,0,0.1051177978515625,0,0,-2.236289978027344,0,0.2033233642578125,0,0.20751953125,0.2167892456054688,0,0.2301559448242188,0.234130859375,0.2345809936523438,0.231903076171875,0.230926513671875,0.2299957275390625,0,0.2291717529296875,0,0.05292510986328125,0,-2.164871215820312,0,0.197723388671875,0,0,0.1928558349609375,0,0.180023193359375,0,0,0.212890625,0,0.2298736572265625,0,0.2347259521484375,0,0.2317581176757812,0.2307968139648438,0.2318038940429688,0.2298736572265625,0.05657196044921875,0,-2.136207580566406,0,0.1930770874023438,0.2014541625976562,0.2029647827148438,0,0.2192840576171875,0.2330780029296875,0,0.2362060546875,0,0.2337799072265625,0,0.2305831909179688,0.2229766845703125,0,0.22589111328125,0,0,0,-2.040122985839844,0,0.1919326782226562,0.2020416259765625,0.2154464721679688,0,0.2319488525390625,0.2364349365234375,0,0.2345428466796875,0,0.2325210571289062,0,0.232330322265625,0,0.2316131591796875,0,0.0933685302734375,0,0,-2.098365783691406,0.1917572021484375,0,0.1977462768554688,0,0.2099151611328125,0.2236785888671875,0,0.2361297607421875,0.2350234985351562,0,0.2334060668945312,0,0.2294998168945312,0,0.229705810546875,0,0,0.1724853515625,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2.080886840820312,0,0.1577606201171875,0,0.1737747192382812,0,0.1819686889648438,0.1913909912109375,0,0.2095718383789062,0.2231597900390625,0,0.2337112426757812,0,0.2318191528320312,0,0.230560302734375,0.2309799194335938,0,0.07610321044921875,0,0,-2.020286560058594,0.1703872680664062,0.1879806518554688,0,0.203399658203125,0,0.245086669921875,0,0.2340850830078125,0,0.2361907958984375,0,0.2338943481445312,0.2316970825195312,0.2326126098632812,0.1040573120117188,0,0,-2.011077880859375,0,0,0.1863784790039062,0,0.1922836303710938,0,0.2072830200195312,0.2240142822265625,0.2350311279296875,0.2339096069335938,0.2316360473632812,0.2291641235351562,0,0.2279129028320312,0,0,0.1015853881835938,0,0,-1.976600646972656,0.1880874633789062,0,0.1962051391601562,0.2113800048828125,0,0.2272872924804688,0,0.235992431640625,0,0.2347640991210938,0,0.2330474853515625,0,0.2306289672851562,0.2532730102539062,0.023223876953125,0,0,-1.879074096679688,0,0.1922683715820312,0,0.2029037475585938,0,0.2160263061523438,0.2346038818359375,0,0.2289352416992188,0,0.2356796264648438,0,0.2308120727539062,0.2305374145507812,0,0.1635284423828125,0,0,0,0,0,-1.781379699707031,0.1895217895507812,0.206634521484375,0.2237472534179688,0,0.235015869140625,0.2375564575195312,0,0.2365341186523438,0,0.2335357666015625,0.23162841796875,0.04264068603515625,0,0,-1.829299926757812,0,0.1915969848632812,0,0.2030105590820312,0,0.243988037109375,0.236328125,0,0.236328125,0,0.2355575561523438,0.2328033447265625,0,0.231964111328125,0,0.0721435546875,0,0,-1.819740295410156,0,0.1945571899414062,0.2032470703125,0,0.2234573364257812,0.2370147705078125,0,0,0.236419677734375,0.2355880737304688,0,0.2325057983398438,0,0.2316970825195312,0.07891082763671875,0,0,-1.800193786621094,0,0.18865966796875,0,0.2012481689453125,0.2160263061523438,0,0.2304000854492188,0,0.2374267578125,0,0.2375946044921875,0,0,0.2349700927734375,0,0,0.239166259765625,0,0,0.0673828125,0,0,-1.748580932617188,0.1884613037109375,0,0.2024993896484375,0,0.2207489013671875,0,0.2365951538085938,0,0.2374191284179688,0,0.2359771728515625,0,0.2330322265625,0,0.2307510375976562,0,0.0149688720703125,0,-1.693679809570312,0,0.1880645751953125,0,0,0.2044143676757812,0,0.2243194580078125,0,0.2361373901367188,0,0.2362213134765625,0,0.2349166870117188,0,0.2325286865234375,0,0,0.1881179809570312,0,0,0,0,0,0,0,-1.622390747070312,0.1912689208984375,0,0.208465576171875,0.2283554077148438,0,0.2377243041992188,0,0.2367019653320312,0.25921630859375,0,0.23248291015625,0,0.07842254638671875,0,-1.678184509277344,0,0.1936111450195312,0.2042160034179688,0,0.2230148315429688,0,0.2355117797851562,0,0.2360458374023438,0.236663818359375,0,0,0.2406234741210938,0.1578750610351562,0,0,0,0,0,-1.526016235351562,0,0.1998672485351562,0,0.217437744140625,0,0.2343063354492188,0.2366485595703125,0,0.2358932495117188,0,0.2415771484375,0.2088851928710938,0,0,0,-1.5460205078125,0,0.1962966918945312,0.1858749389648438,0,0.2049713134765625,0,0.2502517700195312,0,0,0.2384567260742188,0,0.237060546875,0,0.2332611083984375,0.047698974609375,0,0,-1.602745056152344,0.1760482788085938,0,0.2020492553710938,0.22137451171875,0,0.2353286743164062,0,0.23883056640625,0,0.2389755249023438,0,0.23590087890625,0,0.10125732421875,0,-1.603828430175781,0.1812667846679688,0.1946640014648438,0.2052001953125,0,0.2248306274414062,0.2382278442382812,0,0.236907958984375,0,0.2359161376953125,0.13311767578125,0,0,0,0,0,-1.424797058105469,0,0.2107315063476562,0,0.2163848876953125,0,0.2317581176757812,0,0.2393569946289062,0,0.2387008666992188,0.2366409301757812,0.0967254638671875,0,0,0,-1.550628662109375,0,0.1830368041992188,0,0.1990509033203125,0.2208023071289062,0,0.2359085083007812,0.2403564453125,0,0.2390289306640625,0,0.23736572265625,0,0.03986358642578125,0,0,-1.477401733398438,0,0.1902847290039062,0.2083969116210938,0,0.2281875610351562,0,0.2393417358398438,0,0.2391357421875,0,0.2375717163085938,0,0.17852783203125,0,0,0,-1.371063232421875,0.2193450927734375,0.2129135131835938,0.2327651977539062,0,0.24090576171875,0,0.2394027709960938,0,0.23614501953125,0,0,0.03298187255859375,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.493278503417969,0,0,0,0,0,0.09142303466796875,0,0.1950607299804688,0.204559326171875,0.2229080200195312,0.2370071411132812,0.227874755859375,0,0.213623046875,0,0.2455978393554688,0.2266082763671875,0.231597900390625,0,0.2363433837890625,0,0.2361984252929688,0,0,0.2279510498046875,0,0,0.1959991455078125,0,0,0.1917724609375,0,0.1946182250976562,0,0.1932296752929688,0,0.1956253051757812,0,0.1932144165039062,0,0,0.1944198608398438,0,0.1921920776367188,0.1944351196289062,0.1931838989257812,0,0.1017303466796875,0,0,0,0,0,-4.454475402832031,0.2249755859375,0,0.237945556640625,0,0.2379684448242188,0,0.2254486083984375,0,0.2145004272460938,0,0.2360153198242188,0.2319107055664062,0,0.2329330444335938,0.2346267700195312,0.2620925903320312,0,0,0.2417831420898438,0,0.242156982421875,0,0.2389984130859375,0,0.241119384765625,0,0.2418594360351562,0.2416534423828125,0.2417144775390625,0,0.2389984130859375,0,0.2298965454101562,0,0.09018707275390625,0,0,0,0,0,-4.372062683105469,0,0.2223281860351562,0,0.2349166870117188,0.231689453125,0,0.2188034057617188,0,0.2260513305664062,0,0,0.2342376708984375,0,0.2321395874023438,0,0.2341156005859375,0,0.2347564697265625,0,0.241455078125,0,0.2432098388671875,0.2422256469726562,0,0.2394790649414062,0,0.2386245727539062,0,0.2402267456054688,0,0.2411727905273438,0,0.2649383544921875,0,0,0.2344131469726562,0,0.231109619140625,0,0.0163116455078125,0,0,-4.446044921875,0.2043685913085938,0,0.2189788818359375,0,0.2321548461914062,0,0.2238006591796875,0.21875,0.2377853393554688,0,0.2340927124023438,0,0,0.231964111328125,0,0.2336273193359375,0.2335586547851562,0.2360076904296875,0.2410812377929688,0,0.2423553466796875,0,0.2408599853515625,0.2425460815429688,0,0.2421188354492188,0.2432785034179688,0.2440948486328125,0.231201171875,0,0.1414718627929688,0,0,0,0,0,-4.27374267578125,0,0.2112350463867188,0,0.22161865234375,0,0.2243118286132812,0,0.2172470092773438,0.237030029296875,0,0.2354736328125,0,0,0.2321624755859375,0,0,0.2330245971679688,0,0,0.232147216796875,0,0.232696533203125,0,0.2378082275390625,0.2440185546875,0,0.2432098388671875,0,0.2433853149414062,0,0.2426834106445312,0.24285888671875,0.2451553344726562,0,0.2355422973632812,0.1881179809570312,0,0,0,-4.270317077636719,0,0.1999282836914062,0,0.211578369140625,0,0.2155380249023438,0.2054519653320312,0,0.25726318359375,0,0.2362594604492188,0.232452392578125,0.2291030883789062,0,0.2290191650390625,0,0.2310943603515625,0,0.2318115234375,0,0,0.230621337890625,0.2305068969726562,0.232330322265625,0,0.2311019897460938,0.2416305541992188,0.2425613403320312,0,0.2384796142578125,0,0.2249221801757812,0,0,0.04264068603515625,0,0,0,0,0,-4.077255249023438,0.2048492431640625,0.2099990844726562,0,0,0.2098464965820312,0,0.2374191284179688,0,0.2373733520507812,0.2358322143554688,0.2551956176757812,0,0.232177734375,0,0,0.2311248779296875,0,0.2304458618164062,0.2319564819335938,0.2424392700195312,0,0.2425765991210938,0.2421493530273438,0,0.2428665161132812,0.244720458984375,0.2370834350585938,0,0.2300567626953125,0,0,0.001068115234375,0,0,-4.180160522460938,0,0.1815109252929688,0.208648681640625,0.2091064453125,0,0.217071533203125,0,0,0.2379913330078125,0.2373504638671875,0.2332305908203125,0,0.22967529296875,0,0.2311019897460938,0,0.2312774658203125,0.2313461303710938,0.2326126098632812,0.2347869873046875,0.2563705444335938,0,0.2386474609375,0,0.2430343627929688,0.2439422607421875,0,0.2348098754882812,0,0.1677017211914062,0,0,0,-4.065895080566406,0,0.1808700561523438,0,0.2072372436523438,0.2049789428710938,0,0.2337112426757812,0.237274169921875,0,0,0.23687744140625,0,0.2340927124023438,0,0.2314605712890625,0,0,0.2300567626953125,0,0.2305374145507812,0.23162841796875,0,0.2271194458007812,0,0.2296905517578125,0,0.2300262451171875,0,0.2310943603515625,0,0.2315673828125,0.2343063354492188,0.2305984497070312,0,0.1107406616210938,0,0,0,0,0,0,0,-3.919563293457031,0.2014617919921875,0,0.2024993896484375,0,0.2208633422851562,0.235076904296875,0.2346115112304688,0,0.2333526611328125,0,0.2298355102539062,0,0.2311019897460938,0.232177734375,0,0.234130859375,0.2322769165039062,0,0.235015869140625,0.2409286499023438,0,0.2408981323242188,0,0,0.2188262939453125,0,0.2084426879882812,0,0,0.2260055541992188,0,0.17828369140625,0,0,0,0,0,-3.939620971679688,0,0.18438720703125,0,0.1907882690429688,0,0.227447509765625,0.2324295043945312,0,0.2378082275390625,0,0,0.23126220703125,0,0.227935791015625,0,0.2323837280273438,0,0.2325057983398438,0.2322616577148438,0.2337493896484375,0,0.2224884033203125,0.2330322265625,0.2336807250976562,0.2401504516601562,0,0.2373733520507812,0.2253799438476562,0,0.1987686157226562,0,0,0,0,0,-3.924385070800781,0,0.1940765380859375,0,0.1876296997070312,0,0.1691131591796875,0.202850341796875,0,0.21990966796875,0,0,0.1993026733398438,0.2232284545898438,0,0.203948974609375,0.2217330932617188,0,0.2278366088867188,0.2080459594726562,0,0.2239227294921875,0,0.2131881713867188,0,0.2252044677734375,0.2305068969726562,0.2204360961914062,0,0,0.2349853515625,0,0.2172012329101562,0,0.2110748291015625,0.00264739990234375,0,0,0,0,0,-3.693862915039062,0,0.1936187744140625,0.1782150268554688,0.2003936767578125,0,0.2032546997070312,0,0.2186279296875,0,0.2137069702148438,0,0.2196807861328125,0,0.220062255859375,0,0.2139053344726562,0,0.230072021484375,0,0,0.2198333740234375,0.2216415405273438,0,0.231658935546875,0,0.21929931640625,0,0.2333831787109375,0,0.2228546142578125,0,0.2158355712890625,0.1484527587890625,0,0,0,-3.731040954589844,0,0.1809005737304688,0,0.1790542602539062,0,0.2038345336914062,0.2156600952148438,0.229522705078125,0,0.2319793701171875,0.2301025390625,0,0.2277145385742188,0,0.2294158935546875,0.2294769287109375,0,0.230621337890625,0.2312088012695312,0,0.2311630249023438,0,0.2312164306640625,0,0.2320709228515625,0.2324142456054688,0.22076416015625,0,0.07269287109375,0,0,0,0,0,-3.617835998535156,0.1843185424804688,0.1929779052734375,0,0.2131805419921875,0.2497711181640625,0,0.2330322265625,0,0.2331619262695312,0,0.2318038940429688,0,0.232025146484375,0,0.2313995361328125,0,0.2304534912109375,0.2298049926757812,0,0.2318038940429688,0,0.2312774658203125,0,0.2318038940429688,0,0.23199462890625,0,0.2220001220703125,0,0.11419677734375,0,0,0,0,0,-3.5977783203125,0.1844253540039062,0.1877593994140625,0,0.2092971801757812,0.2204437255859375,0.2293472290039062,0.2337493896484375,0,0.2328414916992188,0.2304611206054688,0,0.2314605712890625,0.2318038940429688,0,0.2545623779296875,0,0.2323455810546875,0,0.230194091796875,0.23199462890625,0,0.2326812744140625,0,0.2237167358398438,0.1060028076171875,0,0,0,0,0,-3.528938293457031,0,0,0.18255615234375,0.1929779052734375,0,0.207672119140625,0.219390869140625,0.2266082763671875,0.2333831787109375,0.2314529418945312,0,0.2309188842773438,0,0.2312850952148438,0.2312698364257812,0,0.229461669921875,0,0.2176132202148438,0,0,0.2328338623046875,0,0.2295379638671875,0,0.2298965454101562,0,0,0.2161636352539062,0,0.08954620361328125,0,0,0,-3.458320617675781,0.176116943359375,0.1876907348632812,0,0.1891632080078125,0,0.1929168701171875,0.2094039916992188,0.2103042602539062,0,0.227783203125,0,0.2272567749023438,0.2181777954101562,0.23028564453125,0,0.2191543579101562,0,0.2232742309570312,0,0.2312240600585938,0,0.220977783203125,0.2377243041992188,0,0,0.2379302978515625,0,0.1209259033203125,0,0,0,0,0,0,0,-3.463943481445312,0.184173583984375,0,0.1741409301757812,0.1868362426757812,0,0,0.200958251953125,0,0.196136474609375,0,0.2195053100585938,0.2139511108398438,0,0.2142791748046875,0.2322769165039062,0,0.2193450927734375,0,0.2326889038085938,0,0.2206192016601562,0.2240676879882812,0,0.233154296875,0,0.241302490234375,0,0.2264633178710938,0.1443405151367188,0,0,0,0,0,-3.413230895996094,0.1798248291015625,0,0.1842803955078125,0,0.1951522827148438,0.2064437866210938,0,0.22216796875,0,0.2321548461914062,0,0.2335662841796875,0,0,0.22967529296875,0,0.230987548828125,0,0.2293167114257812,0,0,0.2303695678710938,0,0.2314682006835938,0,0.231964111328125,0.2332687377929688,0,0.22900390625,0.2122802734375,0,0,0,0,0,-3.372245788574219,0,0.1823272705078125,0,0.1894989013671875,0,0.2000274658203125,0.19970703125,0,0.2179718017578125,0,0.2313613891601562,0.2336196899414062,0,0.2314529418945312,0,0.2326812744140625,0,0.2317352294921875,0.232421875,0,0.232177734375,0,0.233673095703125,0.2339248657226562,0,0.2264175415039062,0,0.16033935546875,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-3.223709106445312,0,0.1559906005859375,0,0,0.176544189453125,0,0.184051513671875,0,0.1911392211914062,0.20892333984375,0,0.2288360595703125,0,0.2339096069335938,0,0.2318572998046875,0.2326431274414062,0,0.2317886352539062,0,0.255828857421875,0.2316436767578125,0,0.2385330200195312,0.2442474365234375,0,0.2331695556640625,0,0.040008544921875,0,0,0,0,0,-3.144981384277344,0,0.1833343505859375,0,0.1921463012695312,0.2032012939453125,0,0.2180099487304688,0,0.2312088012695312,0,0.2343215942382812,0,0.2324600219726562,0,0.2318115234375,0,0.2309722900390625,0.2324371337890625,0,0.2320175170898438,0,0.2337646484375,0.2340164184570312,0,0.2335739135742188,0,0.115753173828125,0,0,0,-3.161148071289062,0,0.1814117431640625,0.2023849487304688,0,0.1969985961914062,0.212005615234375,0,0.2256317138671875,0.2338027954101562,0,0.2326812744140625,0.2301712036132812,0,0.2314605712890625,0,0.2305908203125,0,0.2312545776367188,0,0.2372665405273438,0,0.2399063110351562,0,0.2287521362304688,0.13934326171875,0,0,0,0,0,-3.129981994628906,0,0,0.1802597045898438,0.1831283569335938,0,0.1929092407226562,0,0.2098770141601562,0,0.2247848510742188,0.2356109619140625,0,0.2349929809570312,0,0.231781005859375,0,0,0.2332000732421875,0,0.2321548461914062,0,0.2326812744140625,0,0.2390060424804688,0,0,0.2688064575195312,0,0.2334136962890625,0,0.0884246826171875,0,0,0,0,0,-3.035270690917969,0.1818161010742188,0,0,0.1852798461914062,0.1982421875,0.2121963500976562,0,0.2285385131835938,0.235626220703125,0,0,0.23284912109375,0,0,0.2313003540039062,0,0.2324752807617188,0,0.23126220703125,0,0.2332077026367188,0,0.2327499389648438,0,0.2335052490234375,0,0.2227325439453125,0.033050537109375,0,0,0,-2.951309204101562,0,0.1819915771484375,0,0,0.1849517822265625,0,0,0.2205734252929688,0,0.2172317504882812,0,0.2327194213867188,0,0.2350997924804688,0,0.2318344116210938,0,0.2319488525390625,0,0.2346725463867188,0.237213134765625,0,0.2363739013671875,0,0.2422332763671875,0.2352066040039062,0,0,0.1173858642578125,0,0,0,0,0,-3.005821228027344,0,0.1716384887695312,0,0.1715927124023438,0,0.1843185424804688,0,0.16156005859375,0,0.1909027099609375,0,0.21026611328125,0,0.2237548828125,0,0.219329833984375,0,0.2101821899414062,0,0.2136077880859375,0,0.2238616943359375,0,0,0.2135543823242188,0,0,0.2273941040039062,0.2160110473632812,0,0.2046737670898438,0,0.04985809326171875,0,0,0,-2.902191162109375,0,0.1471786499023438,0.1788711547851562,0,0.1640777587890625,0.1838455200195312,0,0.20916748046875,0,0.1898880004882812,0,0,0.2130584716796875,0.2198028564453125,0,0.210418701171875,0,0.235015869140625,0.212799072265625,0,0,0.2200927734375,0,0.2273941040039062,0,0.2054595947265625,0,0.1704254150390625,0,0,0,0,0,0,0,0,-2.806640625,0,0.1500778198242188,0.1931991577148438,0.1673507690429688,0,0.178863525390625,0.2103424072265625,0,0.2004013061523438,0,0,0.22320556640625,0,0,0.22698974609375,0.2264175415039062,0,0.2265396118164062,0,0.2235565185546875,0.2255096435546875,0,0.225311279296875,0,0.21282958984375,0,0,0,0,0,-2.750091552734375,0,0.1908950805664062,0,0.183380126953125,0,0,0.1951751708984375,0.2126846313476562,0.2256546020507812,0.2126388549804688,0,0,0.2260360717773438,0,0.182159423828125,0.221923828125,0,0.2161712646484375,0.2183074951171875,0,0.2114334106445312,0.2214508056640625,0.114654541015625,0,0,0,-2.809173583984375,0,0.1403884887695312,0,0.18035888671875,0,0.1452407836914062,0.1788787841796875,0,0.194976806640625,0,0.1875457763671875,0.2217559814453125,0.2173004150390625,0,0.2030258178710938,0,0.2281723022460938,0.1981124877929688,0.225067138671875,0.2246780395507812,0.21771240234375,0,0.1272354125976562,0,0,0,0,0,-2.752784729003906,0,0.1392135620117188,0.093292236328125,0,0.1525421142578125,0.174896240234375,0,0.1630096435546875,0,0.08002471923828125,0,0.1009063720703125,0,0,0.093597412109375,0.08841705322265625,0,0.0980377197265625,0,0.1056442260742188,0,0.2059860229492188,0,0.1927413940429688,0.2002182006835938,0,0.2231521606445312,0,0.2323455810546875,0,0,0.2331771850585938,0,0.2209701538085938,0,0.03453826904296875,0,0,0,0,0,-2.639175415039062,0,0.1954727172851562,0,0.18511962890625,0,0,0.1993179321289062,0.2170639038085938,0.2333831787109375,0.2349624633789062,0.2330780029296875,0,0.2283172607421875,0.234893798828125,0.2354888916015625,0,0.2357940673828125,0.2266006469726562,0,0.058258056640625,0,0,0,0,0,-2.653182983398438,0.1724929809570312,0,0.1809463500976562,0,0,0.1891860961914062,0,0.2056732177734375,0,0.2242584228515625,0.233917236328125,0.2338333129882812,0,0.2308197021484375,0.2321548461914062,0.253875732421875,0,0.2314224243164062,0,0.2272415161132812,0,0.1147613525390625,0,0,0,-2.606300354003906,0.177886962890625,0,0,0.1818008422851562,0,0,0.1974334716796875,0,0.2137374877929688,0,0.2313919067382812,0,0.2373733520507812,0.2360153198242188,0.230926513671875,0.2327499389648438,0,0.2323074340820312,0.2325439453125,0,0.226165771484375,0,0.052001953125,0,0,0,-2.514778137207031,0.1798171997070312,0,0,0.1856689453125,0,0.19866943359375,0.1986160278320312,0,0.1951065063476562,0,0.2294540405273438,0.234375,0.230682373046875,0.2325363159179688,0,0,0.231292724609375,0,0.2326507568359375,0,0.1960601806640625,0.04485321044921875,0,0,0,-2.490631103515625,0,0.1746139526367188,0,0.1691436767578125,0.1883544921875,0.2031936645507812,0,0.2199859619140625,0.2348098754882812,0,0,0.2346038818359375,0,0.2327346801757812,0.2331924438476562,0,0.2310638427734375,0,0.2540740966796875,0.1884765625,0,0,0,0,0,0,0,0,-2.368942260742188,0,0.176483154296875,0.1837692260742188,0,0.1956787109375,0,0.2139358520507812,0.226837158203125,0,0.2353134155273438,0,0.2325057983398438,0,0.2316360473632812,0,0.2320327758789062,0.2329559326171875,0,0.224273681640625,0,0.0560150146484375,0,0,0,0,0,-2.403854370117188,0,0.177215576171875,0.1804580688476562,0.1788101196289062,0.2103271484375,0,0.2034225463867188,0,0.2101974487304688,0,0.2193222045898438,0,0.2002944946289062,0.2038497924804688,0,0.212432861328125,0.205780029296875,0.2128448486328125,0,0.060211181640625,0,0,0,-2.411544799804688,0,0.1619949340820312,0.1771621704101562,0.1765289306640625,0,0.2001190185546875,0.1957855224609375,0,0.2051162719726562,0,0.1864089965820312,0,0.1329421997070312,0.1582794189453125,0.18603515625,0,0.1875534057617188,0.2039031982421875,0,0.2049713134765625,0,0.1049346923828125,0,0,0,0,0,0,0,0,-2.276199340820312,0.1727218627929688,0.1658935546875,0,0.190093994140625,0.1854095458984375,0.1870574951171875,0,0.2112960815429688,0,0.195831298828125,0,0,0.2153472900390625,0,0.205841064453125,0,0.1964645385742188,0,0.22039794921875,0,0.19677734375,0.00205230712890625,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2.376121520996094,0,0,0.0419921875,0.1478805541992188,0,0.1539459228515625,0.1485748291015625,0,0.18475341796875,0.1696853637695312,0.20379638671875,0.2147140502929688,0,0.1879806518554688,0,0.2045974731445312,0,0.175628662109375,0,0.1923065185546875,0,0.172210693359375,0,0.1507339477539062,0.09491729736328125,0,0,0,0,0,-2.337249755859375,0,0.16680908203125,0.1561203002929688,0.176849365234375,0,0.1738815307617188,0,0.1831893920898438,0,0.2009429931640625,0,0.1928634643554688,0,0.2125244140625,0.2203216552734375,0.2065582275390625,0,0.2252883911132812,0,0.2095565795898438,0,0.0791778564453125,0,0,0,-2.239913940429688,0,0.1707839965820312,0,0.1708831787109375,0,0.1782913208007812,0,0.1837158203125,0,0.1837081909179688,0,0.20379638671875,0,0.2008895874023438,0,0.2141036987304688,0,0.2175445556640625,0,0.2053070068359375,0,0.222686767578125,0,0,0.1540451049804688,0,0,0,0,0,-2.131454467773438,0,0.17510986328125,0.147979736328125,0,0.163665771484375,0,0.1825637817382812,0.1975173950195312,0,0.218536376953125,0,0.2274246215820312,0.2312469482421875,0,0.231475830078125,0.2296295166015625,0,0.1909408569335938,0,0,0,0,0,0,0,0,-2.079681396484375,0.1944580078125,0.1816940307617188,0,0,0.1965408325195312,0,0,0.21435546875,0.2308578491210938,0,0.236724853515625,0.2338409423828125,0.22906494140625,0.2505111694335938,0,0.175323486328125,0,0,0,0,0,0,0,0,-2.02362060546875,0,0,0.1749191284179688,0,0.1812667846679688,0,0.1983108520507812,0,0,0.2143020629882812,0.2345428466796875,0.2246627807617188,0,0.23199462890625,0,0.2317962646484375,0,0.2292404174804688,0.1651992797851562,0,0,0,0,0,0,0,-2.142845153808594,0.1700592041015625,0,0,0.1765060424804688,0,0.1867599487304688,0,0.2012405395507812,0,0,0.21954345703125,0,0.2368621826171875,0,0.2318038940429688,0,0.2330856323242188,0.2303466796875,0,0.2297515869140625,0.0885162353515625,0,0,0,-2.07672119140625,0,0,0.1671600341796875,0.1799774169921875,0.1878890991210938,0,0.1993331909179688,0,0.2141342163085938,0.224761962890625,0,0.2378997802734375,0.2348556518554688,0.2321014404296875,0,0.2263641357421875,0,0.0328216552734375,0,0,0,0,0,-1.998931884765625,0,0.1674423217773438,0,0.186431884765625,0.1901092529296875,0,0,0.1942672729492188,0,0.2059707641601562,0.1891098022460938,0.2103424072265625,0.1950607299804688,0.2072372436523438,0,0.2099380493164062,0.1027603149414062,0,0,0,-2.050056457519531,0,0.147552490234375,0.1684951782226562,0,0.1714248657226562,0,0,0.1768569946289062,0.1793746948242188,0,0.1787872314453125,0,0.2040176391601562,0.17236328125,0,0.2076568603515625,0.2003250122070312,0.1847305297851562,0.1171035766601562,0,0,0,0,0,-2.018463134765625,0,0.1639480590820312,0,0.1668243408203125,0.1645965576171875,0,0.1888427734375,0,0.1742172241210938,0,0.1924972534179688,0.1996917724609375,0.2051467895507812,0,0.1949615478515625,0,0.2113418579101562,0.2141799926757812,0,0,0,0,0,0,0,0,-1.91497802734375,0,0.1456451416015625,0,0.1795425415039062,0,0.1808700561523438,0,0.1916427612304688,0,0.2016143798828125,0,0.195709228515625,0.2227859497070312,0.2174301147460938,0,0.2219772338867188,0,0.2144927978515625,0,0,0,0,0,-1.879447937011719,0,0.1719970703125,0,0,0.1976242065429688,0,0.191436767578125,0,0.2050704956054688,0,0.223236083984375,0,0.2351455688476562,0,0,0.2345962524414062,0,0.2323379516601562,0,0.2323226928710938,0,0.0116119384765625,0,0,0,0,0,-1.823883056640625,0.17254638671875,0,0.1829605102539062,0.19219970703125,0,0.2049713134765625,0,0.2249603271484375,0,0.2372283935546875,0.236083984375,0.234893798828125,0,0.1930389404296875,0,0,0,0,0,0,0,0,-1.73809814453125,0.1763534545898438,0.1888198852539062,0.1959915161132812,0,0.2116317749023438,0.2301864624023438,0,0,0.2387924194335938,0.2239761352539062,0.2342605590820312,0.0921173095703125,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.754364013671875,0,0.1740188598632812,0.1524200439453125,0,0.1678466796875,0.1376190185546875,0,0.1065139770507812,0,0.1037521362304688,0,0.1503372192382812,0,0.1585693359375,0.185699462890625,0,0.1631927490234375,0,0.1210784912109375,0,0.1830825805664062,0,0.00328826904296875,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.831680297851562,0,0,0,0,0,0,0,0,0.1079177856445312,0,0.1836013793945312,0,0.1877593994140625,0.1968154907226562,0,0.2183609008789062,0.2335586547851562,0,0.2307357788085938,0,0.2126235961914062,0.20635986328125,0,0.224609375,0,0.2249755859375,0,0.2261734008789062,0,0.2345046997070312,0.235595703125,0,0.2347869873046875,0.2372665405273438,0,0.2342605590820312,0,0.2302017211914062,0.1915130615234375,0.1934814453125,0,0.1897354125976562,0,0.1940841674804688,0,0.1895523071289062,0.2145309448242188,0,0.1900405883789062,0,0.1935348510742188,0.1905670166015625,0.1935882568359375,0,0.1911239624023438,0,0.1937103271484375,0,0.183319091796875,0,0.1865997314453125,0,0.181396484375,0,0.1876144409179688,0,0.1842727661132812,0.1817169189453125,0,0.1860733032226562,0.1358261108398438,0,0,0,0,0,-7.229995727539062,0,0.1929779052734375,0,0,0.199005126953125,0,0.2156219482421875,0.256744384765625,0,0.2327499389648438,0.2222366333007812,0.207611083984375,0,0.2316055297851562,0,0.2311477661132812,0,0.2316055297851562,0,0.2307281494140625,0.23309326171875,0,0.2337417602539062,0.2329864501953125,0,0.2344131469726562,0,0.2353363037109375,0,0.23272705078125,0,0.235595703125,0,0.232177734375,0,0.2349395751953125,0.2367172241210938,0,0.2311172485351562,0,0.2330169677734375,0,0.2332763671875,0.2333297729492188,0,0.2353363037109375,0,0.2337112426757812,0,0.235137939453125,0,0.2581100463867188,0,0.1899261474609375,0,0.204437255859375,0.2173690795898438,0,0,0.1397018432617188,0,0,0,0,0,0,0,0,-7.096389770507812,0.1892318725585938,0.1995086669921875,0,0.2066879272460938,0,0.2210159301757812,0.2211456298828125,0.2181396484375,0,0,0.2180938720703125,0.2325057983398438,0,0.2323455810546875,0,0.2342453002929688,0.23480224609375,0,0.2344589233398438,0,0,0.2577896118164062,0,0.2361373901367188,0.2373046875,0,0.2456741333007812,0.2347335815429688,0,0.2353134155273438,0,0.2324905395507812,0,0.2341156005859375,0,0,0.2379302978515625,0,0.2381591796875,0,0.2354965209960938,0,0.2347259521484375,0.2339401245117188,0,0.2348785400390625,0.2371444702148438,0,0.237396240234375,0,0.2456207275390625,0.2336196899414062,0,0.2294769287109375,0.1471023559570312,0,0,0,0,0,0,0,0,-6.990692138671875,0,0.1870269775390625,0,0.1964111328125,0.20355224609375,0.2131500244140625,0,0.1572799682617188,0.1875381469726562,0,0,0.2101974487304688,0.229766845703125,0.2328033447265625,0,0.2319793701171875,0,0.2318191528320312,0,0.235107421875,0,0.2349777221679688,0,0.2442626953125,0,0.2358245849609375,0,0.2330856323242188,0,0.214202880859375,0.1644363403320312,0,0.23431396484375,0,0.229583740234375,0.2323760986328125,0,0.2332763671875,0.2326126098632812,0.2335891723632812,0,0,0.2567367553710938,0,0.2424774169921875,0,0.2330398559570312,0,0.2309188842773438,0,0.23291015625,0.2322845458984375,0,0.2213211059570312,0.222808837890625,0,0,0.080535888671875,0,0,0,0,0,0,0,0,-6.837051391601562,0.1921539306640625,0.1991653442382812,0.2103652954101562,0,0.2163772583007812,0,0.2163009643554688,0,0.2293472290039062,0,0.2348251342773438,0,0,0.2338714599609375,0.2326812744140625,0,0.2304611206054688,0,0.2323379516601562,0.2383041381835938,0.240570068359375,0.2636871337890625,0,0.2349014282226562,0.2276382446289062,0,0.2292022705078125,0,0,0.2328414916992188,0,0.2318649291992188,0.2313995361328125,0,0.233917236328125,0,0.23114013671875,0,0.2326278686523438,0,0.2309799194335938,0.2313995361328125,0,0.2335891723632812,0,0.2321243286132812,0,0.2332534790039062,0,0.2177200317382812,0,0.2181243896484375,0,0.1821441650390625,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-6.660964965820312,0.2100448608398438,0,0.1974105834960938,0,0.199066162109375,0.201263427734375,0.21337890625,0.2377166748046875,0,0.2293777465820312,0,0.2335128784179688,0,0.2302398681640625,0,0.2293853759765625,0,0.2338790893554688,0,0,0.2313232421875,0.23138427734375,0.2291717529296875,0,0.2281417846679688,0,0,0.230743408203125,0,0.2295684814453125,0,0.225250244140625,0,0.22882080078125,0,0.228668212890625,0,0,0.2319564819335938,0.2238006591796875,0.2326278686523438,0,0.25689697265625,0,0.2326812744140625,0,0.2354736328125,0.2289505004882812,0.2290496826171875,0,0.2204055786132812,0,0.2195663452148438,0,0.06629180908203125,0,0,0,0,0,0,0,0,-6.675712585449219,0.1598052978515625,0,0.1877670288085938,0,0.1897048950195312,0,0,0.1851425170898438,0,0.1863021850585938,0.20355224609375,0.221282958984375,0,0.2280120849609375,0.2531509399414062,0,0.2317886352539062,0,0.2279815673828125,0,0.2319412231445312,0,0.2287139892578125,0.2261886596679688,0.2298965454101562,0.2308349609375,0.2304000854492188,0,0.2279739379882812,0,0,0.22808837890625,0,0.2301101684570312,0,0.2306900024414062,0,0.2319793701171875,0,0.229766845703125,0.229278564453125,0,0.2322311401367188,0.2320785522460938,0.2333831787109375,0.233245849609375,0,0.2220840454101562,0.2199020385742188,0.2195358276367188,0,0.01479339599609375,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-6.528762817382812,0.14599609375,0.1799240112304688,0,0.1875228881835938,0,0.1851425170898438,0,0.187774658203125,0,0.2312469482421875,0.2258071899414062,0.2342910766601562,0,0.2321853637695312,0,0,0.2317886352539062,0,0.2296829223632812,0,0.1974258422851562,0,0.2293624877929688,0,0,0.2302093505859375,0,0.22674560546875,0,0.224578857421875,0,0.2321090698242188,0.2205581665039062,0.2297592163085938,0,0.2234344482421875,0.2233810424804688,0.2329635620117188,0.2249832153320312,0,0.2336044311523438,0.2268905639648438,0,0.2254409790039062,0,0,0.2356796264648438,0,0.2265243530273438,0,0.2241287231445312,0,0.2390213012695312,0.13946533203125,0,0,0,0,0,0,0,0,0,0,0,-6.377021789550781,0,0.1802597045898438,0.18316650390625,0,0.180206298828125,0,0.1797637939453125,0.2000885009765625,0.2174148559570312,0.2230911254882812,0,0.2268905639648438,0,0.2354965209960938,0,0.2228164672851562,0,0.2324905395507812,0,0.2283477783203125,0.2253875732421875,0.2337646484375,0.2507781982421875,0,0,0.2300643920898438,0,0.2272415161132812,0,0.2249526977539062,0,0,0.233428955078125,0.2282180786132812,0,0.2309417724609375,0,0.2314834594726562,0,0.2282028198242188,0.235931396484375,0,0.2311248779296875,0.2343673706054688,0,0.2327499389648438,0.2199783325195312,0,0.2165374755859375,0.1376190185546875,0,0,0,0,0,0,0,0,0,0,0,-6.257392883300781,0,0.1809539794921875,0,0.1863021850585938,0,0.1989898681640625,0,0.1958541870117188,0,0.220916748046875,0,0.2242431640625,0.2316513061523438,0,0,0.2309722900390625,0.2285919189453125,0,0.2342453002929688,0.2244949340820312,0,0.2291107177734375,0.228485107421875,0,0.22711181640625,0,0.2357940673828125,0,0.2288284301757812,0,0,0.22991943359375,0,0.2322845458984375,0,0.2252883911132812,0,0.2332077026367188,0,0.2288894653320312,0.2359619140625,0,0.2349777221679688,0,0.2300491333007812,0,0,0.2362289428710938,0.2350845336914062,0,0.2274093627929688,0,0.2223358154296875,0,0.1620101928710938,0,0,0,0,0,0,0,0,0,0,0,-6.137725830078125,0.1809463500976562,0,0.1845703125,0,0.1786651611328125,0,0.1997299194335938,0,0.2182235717773438,0.2246322631835938,0,0.230377197265625,0,0.2225723266601562,0.2227859497070312,0,0.2244338989257812,0,0.2221755981445312,0,0.228271484375,0,0.245025634765625,0,0.2235641479492188,0.2308807373046875,0,0.2494049072265625,7.774345397949219,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7.62939453125,7.62939453125e-06,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,15.2587890625,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7.629417419433594,0,0,0,0,0,0,0,0.05390167236328125,0,0,0,0,0,0,0,0,0,0,0,0,0,0,15.34129333496094,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"filename":["<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,null,null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,null,"<expr>",null,null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,null,null,null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,null,null,null,null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,null,null,null,null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,null,null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,"<expr>",null,null,null,null,null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,null,null,null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,null,null,null,null,null,null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,null,null,"<expr>",null,null,null,"<expr>","<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,"<expr>","<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null]},"interval":10,"files":[{"filename":"<expr>","content":"## Generate Large Random Dataset\nn <- 2e6\nx <- runif(n)\ny <- runif(n)\nz <- runif(n)\nXYZ <- cbind(x,y,z)\n\n## Inspect 4 equivalent `row mean` calculations \nprofvis::profvis({\n    m <- rowSums(XYZ)/ncol(XYZ)\n    m <- rowMeans(XYZ)\n    m <- apply(XYZ, 1, mean)\n    m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }\n})\n## rowSums(), colSums(), rowMeans(), and colMeans() are vectorised and fast.\n## for loop is not the slowest, but the ugliest.","normpath":"<expr>"}],"prof_output":"/tmp/RtmpN1kdh0/file34b33c2aa2c0.prof","highlight":{"output":["^output\\$"],"gc":["^<GC>$"],"stacktrace":["^\\.\\.stacktraceo(n|ff)\\.\\.$"]},"split":"h"}},"evals":[],"jsHooks":[]}</script>
```

```r
## rowSums(), colSums(), rowMeans(), and colMeans() are vectorised and fast.
## for loop is not the slowest, but the ugliest.
```

For more systematic speed comparisons, use the `microbenchmark` package

```r
## 3 Equivalent calculations of the mean of a vector
mean1 <- function(x,p=1) mean(x^p)
mean2 <- function(x,p=1) sum(x^p) / length(x)
mean3 <- function(x,p=1) mean.default(x^p)

## Time them
x <- runif(1e6)
microbenchmark::microbenchmark(
  mean1(x,.5),
  mean2(x,.5),
  mean3(x,.5)
)
```

```
## Unit: milliseconds
##           expr      min       lq     mean   median       uq      max neval cld
##  mean1(x, 0.5) 33.30031 34.03861 36.08242 35.55705 37.30569 46.99263   100  a 
##  mean2(x, 0.5) 32.23356 33.02763 34.87750 34.52339 36.23635 42.82114   100   b
##  mean3(x, 0.5) 33.24843 34.08497 36.61801 35.69416 37.85592 48.67265   100  a
```


For memory leaks, first free up space and use the `bench` package for timing

```r
gc() ## garbage cleanup

bench::mark(
  mean1(x,.5),
  mean2(x,.5),
  mean3(x,.5))
```

### Speed-Ups


**vectorize**

Vector operations are generally faster and easier to read than loops

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
microbenchmark::microbenchmark(
  ma1(y),
  ma2(y)
)
```

```
## Unit: milliseconds
##    expr       min        lq      mean    median        uq      max neval cld
##  ma1(y) 282.33405 286.62609 295.36223 294.48476 300.52952 357.0284   100  a 
##  ma2(y)  27.10752  30.69989  38.45477  32.94287  37.29114 230.6200   100   b
```
Likewise, matrix operations are often faster than vector operations.




**Packages**
Before creating your own program, check if there is a faster or more memory efficient version. E.g., [data.table](https://cran.r-project.org/web/packages/data.table/vignettes/datatable-intro.html) or [Rfast2](https://cran.r-project.org/web/packages/Rfast2/index.html) for basic data manipulation.

```r
X <- cbind(1, runif(1e6))
Y <- X %*% c(1,2) + rnorm(1e6)
DAT <- as.data.frame(cbind(Y,X))

system.time({.lm.fit(X, Y) })
```

```
##    user  system elapsed 
##   0.136   0.000   0.045
```

```r
system.time({ lm(Y~X, data=DAT) })
```

```
##    user  system elapsed 
##   0.538   0.023   0.224
```
Note that quicker codes tend to have fewer checks and return less information. So you must know exactly what you are putting in and getting out.


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
##   0.038   0.001   0.040
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
##   1.441   0.267   0.970
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

Before doing that, however, look into https://cran.r-project.org/web/views/HighPerformanceComputing.html

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


## More Literature

Advanced Programming 

* https://rmd4sci.njtierney.com/
* https://smac-group.github.io/ds/high-performance-computing.html
* https://www.stat.umn.edu/geyer/3701/notes/arithmetic.Rmd

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
* https://bookdown.dongzhuoer.com/hadley/adv-r/

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

To remove packages duplicated in multiple libraries

```r
## Libraries
i <- installed.packages()
libs <- .libPaths()
## Find Duplicated Packages
i1 <- i[ i[,'LibPath']==libs[1], ]
i2 <- i[ i[,'LibPath']==libs[2], ]
dups <- i2[,'Package'] %in% i1[,'Package']
all( dups )
## Remove
remove.packages(  i2[,'Package'], libs[2] )
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

