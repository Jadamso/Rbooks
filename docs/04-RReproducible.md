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
<div class="plotly html-widget html-fill-item" id="htmlwidget-106cd4fd820c89d88cda" style="width:672px;height:480px;"></div>
<script type="application/json" data-for="htmlwidget-106cd4fd820c89d88cda">{"x":{"visdat":{"49d57c5f754":["function () ","plotlyVisDat"]},"cur_data":"49d57c5f754","attrs":{"49d57c5f754":{"x":{},"y":{},"alpha_stroke":1,"sizes":[10,100],"spans":[1,20]}},"layout":{"margin":{"b":40,"l":60,"t":25,"r":10},"xaxis":{"domain":[0,1],"automargin":true,"title":"X"},"yaxis":{"domain":[0,1],"automargin":true,"title":"Y"},"hovermode":"closest","showlegend":false},"source":"A","config":{"modeBarButtonsToAdd":["hoverclosest","hovercompare"],"showSendToCloud":false},"data":[{"x":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100],"y":[3.877220848851608,14.372627779413648,17.258832797144105,16.006151400049024,16.924613136305247,24.099754978822926,26.055416915401569,30.864496466067219,36.283865811671504,38.64045073656461,45.613938202832479,51.257184879053682,53.084464717793047,54.139058784999079,57.452444949505455,64.444309042305434,70.826760887045154,72.799028956720477,73.55180737128957,78.222370332993549,81.781515625445323,87.134770788024099,91.825088074053212,95.135707669753913,99.930469961873214,103.72988091879738,107.4641171381319,111.07752571558726,112.90400118318998,118.92505009287517,124.92690433876305,127.36573425624451,130.81655325123711,134.00087857089989,140.17064607314234,144.6583038502414,148.02552453044407,153.56455459853231,154.91884108800909,156.48929710304952,166.59215328630762,166.94952505933782,172.88263784288569,174.55804229712982,180.11835726297303,180.62886253227236,187.50488128286736,189.03737874035528,198.40027948925328,197.67800692371037,203.41152331000151,209.23796247280922,211.94616269199753,217.85264697869985,219.72084136449431,224.45667615315259,226.46765506466267,231.30447265540261,239.02837011337201,240.55133255591721,244.11531197990274,245.51006062873734,251.91202681014789,255.10039819359258,255.18530689119063,266.10241203319055,268.77335661455106,275.05901553690802,276.43805365618772,278.00948414937398,283.8789378076288,287.9278092922296,291.75637512062616,291.83184947813658,300.23524224633979,302.79116922672972,309.70588530355644,312.42585420864691,314.29941471786941,317.43527368742542,323.29237659729762,325.64733473919142,333.04130769137436,337.77036265794453,341.23203458645014,342.93741119616197,348.18190848939111,353.63932725547272,356.77493707789841,359.77726208826175,363.14869926032549,369.43353266920775,374.68959856129538,376.30442624747928,378.06408285354144,378.01425003252666,387.71613963301223,392.80441912617789,397.142810862077,400.40209855078683],"type":"scatter","mode":"markers","marker":{"color":"rgba(31,119,180,1)","line":{"color":"rgba(31,119,180,1)"}},"error_y":{"color":"rgba(31,119,180,1)"},"error_x":{"color":"rgba(31,119,180,1)"},"line":{"color":"rgba(31,119,180,1)"},"xaxis":"x","yaxis":"y","frame":null}],"highlight":{"on":"plotly_click","persistent":false,"dynamic":false,"selectize":false,"opacityDim":0.20000000000000001,"selected":{"opacity":1},"debounce":0},"shinyEvents":["plotly_hover","plotly_click","plotly_selected","plotly_relayout","plotly_brushed","plotly_brushing","plotly_clickannotation","plotly_doubleclick","plotly_deselect","plotly_afterplot","plotly_sunburstclick"],"base_url":"https://plot.ly"},"evals":[],"jsHooks":[]}</script>
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
##           used (Mb) gc trigger  (Mb) max used  (Mb)
## Ncells 1213842 64.9    2272610 121.4  2272610 121.4
## Vcells 2300797 17.6    8388608  64.0  3287585  25.1
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
<div class="profvis html-widget html-fill-item" id="htmlwidget-3b66966b388659797e56" style="width:100%;height:600px;"></div>
<script type="application/json" data-for="htmlwidget-3b66966b388659797e56">{"x":{"message":{"prof":{"time":[1,2,3,4,5,6,7,8,9,10,11,12,12,12,13,13,14,14,15,15,16,16,17,17,18,18,19,19,20,20,21,21,22,22,23,23,24,24,25,25,26,26,27,27,28,29,29,30,30,31,31,32,32,33,34,34,35,36,36,37,37,37,38,38,39,40,41,41,42,42,43,44,44,45,45,46,46,47,48,48,48,49,49,50,50,51,51,52,53,53,53,54,54,55,55,56,56,56,57,57,57,58,58,58,59,59,60,60,61,61,62,62,63,63,64,64,65,66,66,67,67,68,69,69,69,70,71,71,72,72,73,73,74,74,75,76,76,77,77,78,78,79,79,80,80,81,81,82,82,82,83,83,84,85,85,86,86,87,87,87,88,89,90,91,92,92,93,94,94,95,95,95,96,96,97,97,98,99,99,100,101,101,102,102,103,103,104,104,105,105,106,106,107,107,108,108,108,109,109,110,111,111,112,112,113,113,114,115,116,117,117,118,119,119,120,120,121,121,121,121,122,122,122,123,123,124,125,126,126,127,128,128,129,129,130,131,131,132,132,133,133,134,134,134,135,135,136,136,137,137,138,139,139,140,140,141,141,142,143,143,144,144,145,146,146,146,147,147,148,149,149,150,151,152,152,153,153,154,154,155,155,156,156,157,158,158,159,159,159,160,161,162,162,162,163,163,164,164,165,165,166,167,167,167,168,168,169,169,170,170,171,171,171,172,172,173,173,174,174,175,176,176,177,178,178,179,180,181,181,182,183,183,184,185,185,186,186,187,187,188,189,189,190,190,191,191,192,192,193,193,194,194,194,195,195,195,196,196,197,197,198,199,200,200,201,201,202,202,203,203,204,204,205,206,206,207,207,208,208,209,210,210,211,212,212,213,213,214,214,215,215,216,217,217,218,218,218,219,220,221,221,222,223,224,224,225,225,226,227,227,228,229,229,229,230,230,231,231,232,232,233,233,233,234,234,235,235,236,236,237,238,238,239,240,240,240,240,241,241,241,241,242,242,243,243,244,245,245,246,246,247,247,247,248,249,249,250,251,251,251,252,252,252,253,254,254,255,255,256,256,257,257,258,259,260,261,262,262,263,263,263,263,264,264,265,266,266,267,268,268,269,269,270,270,271,272,273,273,274,274,274,275,275,276,276,277,277,278,278,279,279,280,280,281,282,282,283,284,284,285,285,286,286,287,287,288,288,289,289,290,290,291,291,292,292,293,293,294,294,295,296,296,297,297,298,298,299,299,300,300,301,301,302,303,304,305,305,306,306,307,308,308,309,309,310,310,311,312,312,313,313,314,315,315,316,316,316,317,317,318,318,319,320,321,321,322,322,323,323,323,324,324,325,325,326,326,326,327,327,327,328,328,329,329,330,331,331,331,332,332,333,333,334,335,336,336,337,337,338,339,340,340,340,341,342,342,343,344,344,345,345,346,347,347,347,348,349,350,350,351,351,352,353,354,355,355,356,357,357,357,358,358,359,359,360,360,361,361,362,362,363,363,364,365,366,366,367,367,367,368,368,369,369,370,370,371,371,372,373,373,374,374,375,375,376,376,377,377,378,378,379,380,380,381,382,382,383,384,384,385,386,386,387,387,388,388,389,390,390,391,391,392,392,393,393,394,394,395,395,396,396,396,397,397,397,398,398,399,399,400,401,402,402,403,404,404,405,405,406,406,407,407,408,408,409,409,410,410,410,411,411,412,412,413,414,414,414,415,415,415,416,417,418,418,419,419,420,421,421,422,423,423,424,424,424,425,425,426,426,427,427,428,428,428,429,429,430,430,431,431,432,432,433,433,433,434,434,435,436,437,438,438,438,439,439,440,440,440,441,441,442,442,443,443,444,444,444,445,445,446,446,447,448,448,449,449,450,451,451,451,452,452,453,453,453,454,455,456,457,458,459,460,460,461,461,462,462,463,463,464,465,465,466,466,467,467,468,468,468,469,469,469,470,470,470,471,471,472,473,473,474,474,475,475,476,476,477,477,477,477,478,478,479,479,480,481,481,482,482,483,484,484,485,485,485,486,486,486,487,487,488,488,489,490,491,492,493,493,494,494,494,495,495,495,496,496,496,497,497,497,498,498,498,499,499,499,500,500,500,501,501,501,502,502,502,503,503,503,504,504,504,505,505,505,506,506,506,507,507,507,508,508,508,509,509,509,510,510,510,511,511,511,512,512,512,513,513,513,514,514,514,515,515,515,516,516,516,517,517,517,518,518,518,519,519,519,520,520,520,521,521,521,522,522,522,523,523,524,525,525,526,527,527,528,528,529,529,530,530,530,531,531,531,532,533,533,534,534,535,535,536,536,537,537,538,538,539,539,540,540,541,542,542,543,544,544,545,545,546,546,546,547,547,547,548,549,549,550,551,552,552,553,553,554,555,556,556,557,558,559,559,560,560,561,561,562,562,563,564,564,565,566,567,568,568,568,569,569,570,570,571,572,572,573,574,575,575,576,577,577,578,578,579,579,580,581,581,582,583,584,584,585,586,587,587,588,588,589,589,589,590,590,590,591,591,592,592,593,594,594,595,595,596,597,598,598,599,600,600,601,601,602,603,603,604,604,605,605,606,606,606,607,607,608,609,610,611,612,612,613,613,614,614,615,615,616,616,617,617,618,618,619,619,619,620,621,621,622,622,623,623,624,625,625,626,627,628,629,629,630,630,631,631,631,632,632,633,633,634,634,635,635,636,636,637,637,638,638,638,639,639,640,640,641,641,642,642,643,644,644,645,646,646,647,647,648,648,648,649,649,650,650,651,652,652,653,653,654,654,655,655,655,656,657,657,657,658,658,658,659,659,660,661,661,662,662,663,663,663,664,664,664,665,665,665,666,666,667,667,668,669,670,670,670,671,671,671,672,673,673,674,675,675,676,677,677,677,678,678,678,679,680,680,681,681,682,683,683,683,684,684,685,686,687,687,687,688,688,689,689,690,690,691,691,692,693,693,694,694,694,695,696,696,697,697,697,698,698,698,699,699,700,701,701,702,703,703,704,704,705,706,707,708,708,709,709,710,710,711,711,711,712,713,713,713,714,714,715,715,716,716,717,717,717,718,718,718,719,720,721,722,722,723,723,724,724,725,725,726,726,727,727,728,729,729,729,730,730,731,732,732,733,733,734,734,735,735,736,736,737,737,737,738,738,738,739,740,741,741,742,743,744,744,745,745,746,746,747,748,748,749,749,750,750,751,752,752,753,753,754,754,755,755,756,756,756,757,757,757,758,759,759,760,760,760,761,761,762,763,764,764,764,765,765,766,766,766,767,768,769,770,770,771,772,772,773,773,773,774,774,775,775,775,776,776,776,777,777,778,778,779,779,780,781,781,781,782,782,782,783,783,784,784,784,785,785,786,786,787,787,788,789,789,790,790,791,791,791,792,792,793,793,794,794,794,795,795,795,796,797,798,798,799,799,800,800,801,802,803,803,804,805,805,806,807,808,808,809,809,810,811,811,812,812,813,813,813,814,814,814,815,815,816,816,817,817,817,818,818,819,820,820,821,821,822,822,823,823,824,825,826,826,827,827,827,828,829,829,830,830,831,831,831,831,832,832,832,832,833,834,834,835,836,837,837,838,838,839,839,840,841,841,842,843,843,843,844,844,845,845,846,846,846,847,847,848,849,850,850,851,851,852,852,853,853,854,854,855,855,856,856,856,857,857,858,858,859,860,860,861,861,862,862,863,863,864,865,865,866,867,867,868,868,868,869,869,869,870,871,871,872,872,873,873,874,875,875,876,876,877,877,878,879,879,880,880,881,882,882,883,883,884,884,885,886,886,886,887,887,887,888,888,888,889,889,889,890,891,892,892,893,893,894,895,895,896,897,897,898,899,899,899,900,900,901,901,902,903,903,903,904,904,904,905,905,906,906,907,907,908,908,909,909,910,911,911,912,912,913,913,914,914,915,915,916,916,917,917,918,918,919,920,920,921,921,921,921,922,922,922,922,923,923,924,924,925,925,926,926,927,927,928,928,929,929,930,930,931,931,932,932,933,933,934,934,935,936,936,937,937,938,938,938,939,939,939,940,940,940,941,941,941,942,942,942,943,943,943,944,944,944,945,945,945,946,946,946,947,947,947,948,948,948,949,949,949,950,950,950,951,951,951,952,952,952,953,953,953,954,954,955,956,957,957,958,958,958,959,959,959,960,960,960,961,961,962,963,963,964,964,964,965,965,966,967,967,968,968,969,970,970,970,971,971,971,972,972,973,973,974,975,975,976,976,977,978,978,979,979,980,980,981,981,982,982,983,984,985,985,986,986,987,987,987,988,988,988,989,989,990,990,991,992,992,993,993,994,994,995,995,996,996,997,997,998,999,999,1000,1000,1001,1001,1002,1002,1003,1003,1003,1004,1004,1004,1005,1006,1007,1007,1007,1008,1008,1009,1009,1010,1010,1010,1011,1012,1013,1014,1014,1014,1015,1015,1016,1016,1017,1018,1018,1019,1019,1020,1020,1020,1021,1021,1021,1022,1023,1023,1024,1024,1025,1025,1026,1027,1027,1027,1028,1028,1029,1029,1030,1030,1031,1031,1032,1032,1033,1034,1034,1035,1035,1036,1036,1036,1037,1037,1037,1038,1039,1039,1040,1040,1041,1041,1042,1042,1043,1043,1044,1044,1045,1045,1046,1046,1047,1047,1048,1048,1049,1049,1050,1050,1051,1052,1052,1053,1053,1054,1054,1055,1055,1056,1057,1058,1059,1060,1061,1061,1062,1063,1063,1064,1064,1065,1065,1066,1067,1067,1068,1068,1068,1068,1069,1069,1069,1069,1070,1071,1071,1071,1072,1072,1073,1073,1073,1074,1075,1075,1076,1076,1077,1078,1078,1079,1080,1080,1080,1081,1081,1082,1082,1082,1083,1084,1084,1085,1085,1086,1087,1088,1088,1089,1089,1090,1090,1091,1091,1091,1092,1093,1093,1094,1095,1096,1096,1097,1097,1098,1098,1099,1099,1099,1100,1100,1100,1101,1101,1102,1103,1103,1104,1104,1105,1105,1106,1106,1107,1107,1107,1108,1108,1109,1109,1110,1110,1111,1111,1112,1112,1113,1113,1114,1115,1115,1116,1116,1117,1118,1118,1119,1120,1120,1121,1121,1122,1122,1123,1123,1124,1124,1125,1125,1126,1127,1128,1128,1129,1130,1130,1130,1131,1131,1131,1132,1133,1133,1134,1134,1135,1136,1136,1137,1137,1138,1139,1140,1141,1141,1142,1143,1144,1144,1145,1145,1146,1146,1147,1148,1149,1149,1150,1151,1152,1152,1153,1153,1153,1154,1154,1155,1155,1155,1156,1156,1157,1158,1158,1159,1159,1160,1160,1161,1161,1162,1162,1162,1163,1164,1164,1165,1165,1166,1166,1167,1167,1167,1168,1168,1169,1169,1170,1170,1171,1171,1171,1172,1172,1172,1173,1173,1174,1174,1175,1175,1176,1176,1177,1177,1178,1179,1179,1180,1180,1181,1181,1182,1182,1183,1183,1184,1185,1185,1185,1186,1186,1187,1187,1188,1188,1189,1189,1190,1190,1191,1192,1192,1193,1193,1194,1195,1195,1196,1197,1197,1198,1198,1198,1199,1199,1200,1200,1201,1201,1202,1202,1203,1203,1204,1204,1205,1206,1206,1206,1207,1208,1208,1209,1210,1210,1211,1211,1212,1212,1213,1213,1214,1215,1216,1216,1216,1217,1217,1217,1218,1218,1218,1219,1220,1221,1222,1222,1223,1223,1224,1224,1225,1225,1226,1226,1227,1227,1228,1229,1230,1230,1230,1231,1231,1231,1232,1232,1232,1233,1233,1234,1234,1235,1235,1235,1236,1236,1237,1237,1238,1239,1239,1240,1240,1240,1241,1241,1242,1242,1243,1243,1244,1244,1244,1245,1245,1245,1246,1246,1246,1247,1247,1248,1249,1249,1250,1250,1251,1252,1252,1253,1253,1253,1254,1255,1256,1257,1258,1258,1259,1259,1260,1260,1261,1261,1261,1262,1262,1263,1264,1264,1265,1265,1265,1266,1266,1266,1267,1267,1268,1269,1270,1270,1271,1271,1272,1272,1273,1273,1274,1274,1275,1275,1276,1276,1277,1277,1278,1278,1279,1279,1280,1280,1281,1281,1282,1282,1283,1283,1283,1284,1284,1285,1286,1286,1287,1287,1288,1289,1289,1290,1291,1291,1291,1292,1293,1293,1294,1294,1295,1295,1295,1296,1296,1296,1297,1297,1298,1299,1299,1300,1300,1301,1301,1302,1303,1304,1304,1305,1305,1306,1306,1307,1307,1308,1308,1309,1309,1310,1310,1311,1312,1312,1313,1313,1314,1314,1315,1315,1316,1316,1316,1317,1318,1319,1319,1320,1320,1321,1321,1321,1322,1322,1322,1323,1323,1324,1324,1325,1326,1326,1327,1327,1328,1328,1329,1329,1330,1330,1331,1331,1332,1332,1333,1333,1334,1334,1335,1335,1336,1336,1337,1337,1338,1339,1339,1340,1340,1341,1342,1342,1342,1343,1343,1344,1345,1345,1346,1346,1347,1347,1348,1348,1348,1349,1349,1350,1351,1351,1352,1352,1353,1354,1354,1355,1355,1356,1357,1357,1358,1358,1359,1359,1360,1360,1361,1362,1362,1363,1364,1364,1365,1366,1367,1367,1368,1368,1369,1369,1370,1370,1371,1371,1371,1372,1372,1372,1373,1374,1374,1374,1375,1375,1376,1376,1377,1378,1379,1379,1380,1380,1381,1381,1382,1382,1383,1383,1384,1384,1385,1386,1387,1387,1388,1389,1389,1390,1390,1391,1391,1392,1393,1393,1394,1394,1395,1395,1396,1396,1397,1397,1398,1399,1400,1401,1402,1402,1403,1403,1404,1405,1405,1406,1406,1407,1407,1408,1408,1409,1409,1410,1410,1410,1411,1411,1412,1412,1413,1413,1414,1415,1416,1416,1417,1417,1418,1418,1419,1419,1419,1420,1420,1420,1421,1422,1423,1423,1424,1424,1425,1425,1426,1426,1427,1427,1428,1429,1429,1430,1430,1430,1431,1431,1431,1432,1432,1432,1433,1434,1435,1436,1436,1437,1438,1438,1439,1440,1441,1441,1442,1442,1442,1443,1443,1443,1444,1445,1445,1446,1447,1447,1448,1448,1449,1450,1450,1451,1451,1452,1452,1453,1453,1453,1454,1454,1454,1455,1455,1455,1456,1457,1457,1458,1459,1460,1460,1460,1461,1462,1463,1463,1464,1464,1464,1465,1465,1465,1466,1466,1466,1467,1467,1467,1468,1468,1468,1469,1469,1469,1470,1470,1470,1471,1471,1471,1472,1472,1473,1474,1475,1476,1477,1477,1478,1478,1478,1479,1480,1480,1481,1481,1482,1482,1483,1483,1484,1484,1485,1485,1486,1486,1487,1487,1488,1488,1489,1489,1490,1490,1491,1491,1492,1492,1493,1493,1494,1494,1495,1495,1496,1496,1497,1497,1498,1498,1499,1499,1500,1500,1501,1501,1502,1502,1503,1503,1504,1504,1505,1505,1506,1506,1507,1507,1508,1508,1509,1509,1510,1510,1511,1511,1512,1512,1513,1513,1514,1514,1515,1515,1516,1516,1517,1517,1518,1518,1519,1519,1520,1520,1521,1521,1522,1522,1523,1523,1524,1524,1525,1525,1526,1526,1527,1527,1528,1528,1529,1529,1530,1530,1531,1531,1532,1532,1533,1533,1534,1534,1535,1535,1536,1536,1537,1537,1538,1538,1539,1539,1540,1540,1541,1541,1542,1542,1543,1543,1544,1544,1545,1545,1546,1546,1547,1548,1548,1549,1549,1550,1550,1551,1551,1552,1552,1553,1553,1554,1555,1555,1556,1557,1557,1558,1558,1559,1559,1559,1560,1561,1561,1562,1563,1564,1564,1565,1565,1566,1567,1567,1568,1568,1569,1570,1570,1571,1571,1572,1573,1573,1574,1574,1575,1575,1576,1577,1577,1578,1578,1579,1579,1580,1580,1581,1581,1581,1582,1582,1582,1583,1583,1583,1584,1585,1585,1586,1587,1587,1588,1589,1589,1590,1590,1591,1591,1592,1592,1593,1593,1594,1595,1595,1596,1596,1597,1597,1598,1599,1599,1600,1601,1601,1602,1602,1603,1603,1604,1605,1605,1606,1606,1606,1607,1607,1608,1608,1609,1609,1610,1611,1612,1613,1613,1614,1614,1615,1615,1615,1616,1616,1616,1617,1617,1617,1618,1619,1620,1621,1622,1623,1623,1624,1625,1625,1626,1627,1627,1628,1628,1629,1629,1630,1630,1631,1632,1632,1633,1634,1634,1635,1635,1636,1636,1637,1638,1639,1639,1640,1641,1641,1642,1642,1643,1643,1644,1644,1645,1646,1646,1647,1647,1648,1649,1649,1649,1650,1650,1650,1651,1651,1651,1652,1652,1653,1654,1654,1655,1656,1657,1658,1658,1659,1659,1660,1660,1661,1661,1662,1662,1663,1664,1664,1665,1666,1666,1667,1667,1667,1668,1668,1668,1669,1669,1670,1670,1671,1671,1672,1672,1673,1674,1674,1674,1675,1675,1676,1677,1677,1678,1679,1679,1680,1680,1681,1682,1682,1683,1683,1683,1684,1684,1684,1685,1685,1685,1686,1686,1687,1688,1688,1689,1690,1691,1691,1691,1692,1692,1693,1694,1694,1695,1695,1696,1697,1697,1698,1698,1698,1699,1699,1700,1700,1701,1702,1702,1703,1703,1704,1705,1705,1706,1706,1707,1708,1708,1709,1709,1710,1710,1710,1711,1711,1712,1712,1713,1714,1714,1715,1716,1716,1717,1717,1717,1718,1718,1718,1719,1719,1719,1720,1720,1721,1721,1722,1722,1723,1723,1724,1724,1725,1725,1726,1727,1728,1728,1729,1730,1731,1732,1732,1733,1733,1734,1734,1735,1736,1737,1738,1739,1739,1740,1741,1742,1743,1743,1744,1744,1745,1746,1746,1747,1747,1748,1748,1749,1749,1749,1750,1750,1750,1751,1751,1751,1752,1752,1752,1753,1753,1754,1754,1755,1756,1757,1757,1758,1759,1759,1760,1761,1762,1762,1763,1763,1764,1764,1765,1766,1766,1767,1767,1768,1768,1769,1769,1770,1770,1771,1771,1772,1772,1772,1773,1773,1774,1775,1775,1776,1776,1777,1777,1777,1778,1778,1779,1780,1781,1781,1782,1783,1783,1783,1784,1784,1784,1785,1785,1785,1786,1786,1786,1787,1787,1787,1788,1788,1788,1789,1789,1789,1790,1790,1790,1791,1791,1791,1792,1792,1792,1793,1793,1793,1794,1795,1796,1796,1797,1797,1798,1798,1799,1799,1800,1800,1801,1802,1802,1802,1803,1803,1804,1805,1805,1806,1806,1806,1807,1808,1809,1809,1810,1811,1811,1812,1812,1813,1813,1814,1814,1815,1815,1816,1817,1817,1817,1818,1818,1819,1819,1820,1820,1821,1821,1822,1822,1823,1823,1824,1824,1824,1825,1825,1825,1826,1826,1826,1827,1828,1828,1829,1830,1831,1831,1832,1832,1833,1834,1834,1835,1835,1835,1836,1836,1837,1837,1838,1838,1839,1840,1840,1841,1842,1842,1843,1843,1844,1845,1845,1845,1846,1846,1847,1848,1849,1849,1850,1850,1851,1851,1852,1852,1852,1853,1853,1854,1854,1855,1856,1856,1857,1857,1858,1858,1859,1859,1860,1861,1862,1862,1863,1864,1865,1865,1866,1866,1867,1868,1869,1869,1870,1870,1871,1871,1872,1872,1873,1874,1874,1875,1876,1877,1877,1878,1878,1879,1879,1880,1880,1881,1881,1882,1882,1882,1883,1884,1884,1885,1886,1887,1887,1888,1889,1889,1889,1890,1890,1890,1891,1891,1891,1892,1892,1893,1893,1893,1894,1895,1895,1896,1896,1897,1897,1898,1899,1899,1900,1901,1902,1902,1903,1904,1905,1905,1906,1906,1907,1908,1908,1909,1909,1910,1910,1911,1911,1912,1912,1913,1913,1914,1914,1915,1916,1916,1917,1917,1918,1918,1919,1919,1920,1920,1921,1921,1921,1922,1922,1922,1923,1923,1923,1924,1924,1924,1925,1926,1927,1928,1928,1929,1930,1930,1931,1931,1932,1932,1933,1933,1934,1934,1935,1935,1936,1936,1937,1937,1938,1938,1939,1939,1940,1940,1941,1941,1942,1943,1944,1944,1945,1945,1946,1946,1947,1947,1948,1948,1949,1949,1950,1950,1951,1951,1952,1952,1953,1953,1954,1954,1955,1955,1956,1956,1957,1957,1958,1958,1959,1959,1960,1960,1961,1961,1962,1962,1963,1963,1964,1964,1965,1965,1966,1966,1967,1967,1968,1968,1969,1969,1970,1970,1971,1971,1971,1971,1971,1971,1971,1971,1972,1972,1972,1972,1972,1972,1972,1972,1972,1972,1972,1972,1972,1972,1972,1972,1972,1972,1972,1972,1972,1972,1972,1972,1972,1972,1972,1972,1973,1973,1973,1973,1973,1973,1973,1973,1974,1974,1974,1974,1974,1974,1974,1974,1975,1975,1975,1975,1975,1975,1975,1975,1976,1976,1976,1976,1976,1976,1976,1976,1977,1977,1977,1977,1977,1977,1977,1977,1978,1978,1978,1978,1978,1978,1978,1978,1979,1979,1979,1979,1979,1979,1979,1979,1980,1980,1980,1980,1980,1980,1980,1980,1981,1981,1981,1981,1981,1981,1981,1981,1982,1982,1982,1982,1982,1982,1982,1982,1983,1983,1983,1983,1983,1983,1983,1983,1984,1984,1984,1984,1984,1984,1984,1984,1985,1985,1985,1985,1985,1985,1985,1985,1986,1986,1986,1986,1986,1986,1986,1986,1987,1987,1987,1987,1987,1987,1987,1987,1988,1988,1988,1988,1988,1988,1988,1988,1989,1989,1989,1989,1989,1989,1989,1989,1990,1990,1990,1990,1990,1990,1990,1990,1991,1991,1991,1991,1991,1991,1991,1991,1992,1992,1992,1992,1992,1992,1992,1992,1993,1993,1993,1993,1993,1993,1993,1993,1994,1994,1994,1994,1994,1994,1994,1994,1995,1995,1995,1995,1995,1995,1995,1995,1996,1996,1996,1996,1996,1996,1996,1996,1997,1997,1997,1997,1997,1997,1997,1997,1998,1998,1998,1998,1998,1998,1998,1998,1999,1999,1999,1999,1999,1999,1999,1999,2000,2000,2000,2000,2000,2000,2000,2000,2001,2001,2001,2001,2001,2001,2001,2001,2002,2002,2002,2002,2002,2002,2002,2002],"depth":[1,1,1,1,1,1,1,1,1,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,3,2,1,2,1,1,1,2,1,2,1,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,3,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,3,2,1,1,1,1,1,2,1,1,2,1,3,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,2,1,1,1,1,2,1,1,2,1,2,1,4,3,2,1,3,2,1,2,1,1,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,1,3,2,1,2,1,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,1,1,3,2,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,1,2,1,1,1,2,1,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,1,1,2,1,1,1,2,1,2,1,1,2,1,1,3,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,1,4,3,2,1,4,3,2,1,2,1,2,1,1,2,1,2,1,3,2,1,1,2,1,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,1,1,1,1,2,1,4,3,2,1,2,1,1,2,1,1,2,1,2,1,2,1,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,3,2,1,2,1,2,1,1,1,2,1,2,1,3,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,1,3,2,1,2,1,2,1,1,1,2,1,2,1,1,1,3,2,1,1,2,1,1,2,1,2,1,1,3,2,1,1,1,2,1,2,1,1,1,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,3,2,1,3,2,1,1,1,2,1,2,1,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,1,1,3,2,1,2,1,3,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,1,3,2,1,2,1,3,2,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,4,3,2,1,2,1,2,1,1,2,1,2,1,1,2,1,3,2,1,3,2,1,2,1,2,1,1,1,1,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,1,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,3,2,1,3,2,1,1,2,1,1,1,2,1,2,1,1,1,2,1,1,1,2,1,2,1,2,1,2,1,1,2,1,1,1,1,3,2,1,2,1,2,1,1,2,1,1,1,2,1,1,2,1,2,1,2,1,1,2,1,1,1,2,1,1,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,2,1,1,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,2,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,1,2,1,1,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,1,3,2,1,3,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,1,1,3,2,1,3,2,1,1,2,1,1,2,1,1,3,2,1,3,2,1,1,2,1,2,1,1,3,2,1,2,1,1,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,1,2,1,3,2,1,3,2,1,2,1,1,2,1,1,2,1,2,1,1,1,1,2,1,2,1,2,1,3,2,1,1,3,2,1,2,1,2,1,2,1,3,2,1,3,2,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,1,1,2,1,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,1,2,1,3,2,1,2,1,1,1,3,2,1,2,1,3,2,1,1,1,1,2,1,1,2,1,3,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,2,1,3,2,1,3,2,1,1,1,2,1,2,1,2,1,1,1,2,1,1,2,1,1,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,1,1,2,1,3,2,1,1,2,1,2,1,4,3,2,1,4,3,2,1,1,2,1,1,1,2,1,2,1,2,1,1,2,1,1,3,2,1,2,1,2,1,3,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,1,3,2,1,3,2,1,3,2,1,3,2,1,1,1,2,1,2,1,1,2,1,1,2,1,1,3,2,1,2,1,2,1,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,4,3,2,1,4,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,1,1,2,1,3,2,1,3,2,1,3,2,1,2,1,1,2,1,3,2,1,2,1,1,2,1,2,1,1,3,2,1,3,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,1,1,3,2,1,2,1,2,1,3,2,1,1,1,1,3,2,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,1,1,1,1,2,1,1,2,1,2,1,2,1,1,2,1,4,3,2,1,4,3,2,1,1,3,2,1,2,1,3,2,1,1,2,1,2,1,1,2,1,1,3,2,1,2,1,3,2,1,1,2,1,2,1,1,1,2,1,2,1,2,1,3,2,1,1,2,1,1,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,1,3,2,1,3,2,1,1,2,1,2,1,1,2,1,2,1,1,1,1,2,1,1,1,2,1,2,1,2,1,1,1,2,1,1,1,2,1,3,2,1,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,1,2,1,1,2,1,2,1,2,1,2,1,1,1,3,2,1,3,2,1,3,2,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,3,2,1,3,2,1,3,2,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,1,2,1,3,2,1,1,1,1,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,3,2,1,3,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,1,2,1,1,3,2,1,1,2,1,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,1,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,3,2,1,2,1,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,1,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,1,3,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,1,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,3,2,1,3,2,1,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,3,2,1,3,2,1,1,1,1,2,1,1,2,1,1,1,2,1,3,2,1,3,2,1,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,1,2,1,1,1,3,2,1,1,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,1,1,1,1,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,3,2,1,1,2,1,1,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,1,1,1,2,1,2,1,3,2,1,3,2,1,3,2,1,1,1,1,1,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,1,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,3,2,1,3,2,1,3,2,1,2,1,1,2,1,1,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,1,2,1,1,2,1,2,1,1,2,1,3,2,1,3,2,1,3,2,1,2,1,1,2,1,1,1,3,2,1,2,1,1,2,1,2,1,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,1,1,1,2,1,2,1,2,1,1,1,1,1,2,1,1,1,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,1,1,2,1,1,2,1,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,3,2,1,2,1,1,1,2,1,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,1,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,1,2,1,3,2,1,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,1,2,1,1,1,2,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,1,3,2,1,2,1,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,1,2,1,1,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,1,1,2,1,1,3,2,1,3,2,1,3,2,1,2,1,3,2,1,1,2,1,2,1,2,1,1,2,1,1,1,2,1,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,1,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,8,7,6,5,4,3,2,1,28,27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1],"label":["rowSums","rowSums","rowSums","rowSums","rowSums","rowSums","rowMeans","rowMeans","rowMeans","rowMeans","rowMeans","<GC>","aperm.default","apply","aperm.default","apply","aperm.default","apply","aperm.default","apply","aperm.default","apply","aperm.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","apply","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","FUN","apply","<GC>","apply","apply","mean.default","apply","mean.default","apply","length","local","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","is.na","local","mean.default","apply","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","<GC>","mean.default","apply","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","apply","FUN","apply","FUN","apply","is.na","local","FUN","apply","is.na","local","length","local","<GC>","mean.default","apply","mean.default","apply","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","apply","apply","mean.default","apply","apply","FUN","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","apply","mean.default","apply","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","<GC>","mean.default","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","FUN","apply","apply","apply","apply","is.numeric","local","apply","FUN","apply","FUN","apply","<GC>","isTRUE","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","mean.default","apply","apply","FUN","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","<GC>","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","apply","FUN","apply","mean.default","apply","length","local","apply","FUN","apply","FUN","apply","apply","<GC>","FUN","apply","FUN","apply","apply","mean.default","apply","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","apply","FUN","apply","<GC>","FUN","apply","apply","apply","isTRUE","mean.default","apply","mean.default","apply","is.numeric","local","FUN","apply","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","<GC>","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","FUN","apply","apply","FUN","apply","apply","apply","FUN","apply","apply","<GC>","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","is.numeric","local","mean.default","apply","FUN","apply","FUN","apply","is.numeric","local","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","length","local","apply","apply","mean.default","apply","is.na","local","FUN","apply","mean.default","apply","FUN","apply","apply","<GC>","apply","FUN","apply","mean.default","apply","apply","length","local","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","<GC>","mean.default","apply","apply","apply","FUN","apply","apply","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","apply","mean.default","apply","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","mean.default","apply","apply","isTRUE","mean.default","apply","<GC>","length","local","apply","mean.default","apply","FUN","apply","length","local","FUN","apply","apply","apply","apply","apply","is.numeric","local","<GC>","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","apply","mean.default","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","<GC>","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","mean.default","apply","apply","FUN","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","apply","mean.default","apply","length","local","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","apply","apply","apply","<GC>","apply","FUN","apply","apply","FUN","apply","FUN","apply","mean.default","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","<GC>","FUN","apply","mean.default","apply","FUN","apply","apply","apply","length","local","FUN","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","<GC>","length","local","<GC>","length","local","FUN","apply","mean.default","apply","apply","isTRUE","mean.default","apply","FUN","apply","is.numeric","local","apply","apply","mean.default","apply","<GC>","apply","apply","apply","isTRUE","mean.default","apply","apply","mean.default","apply","apply","FUN","apply","FUN","apply","apply","<GC>","mean.default","apply","apply","apply","FUN","apply","mean.default","apply","apply","apply","apply","mean.default","apply","apply","<GC>","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","apply","length","local","<GC>","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","apply","mean.default","apply","apply","length","local","apply","is.numeric","local","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","apply","apply","mean.default","apply","apply","is.numeric","local","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","length","local","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","length","local","<GC>","mean.default","apply","FUN","apply","length","local","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","<GC>","FUN","apply","mean.default","apply","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","<GC>","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","apply","mean.default","apply","length","local","apply","<GC>","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","apply","apply","apply","apply","<GC>","apply","FUN","apply","length","local","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","is.na","local","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","isTRUE","mean.default","apply","is.numeric","local","FUN","apply","apply","mean.default","apply","is.na","local","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","mean.default","apply","apply","apply","apply","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","apply","FUN","apply","apply","FUN","apply","length","local","is.numeric","local","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","length","local","FUN","apply","FUN","apply","is.numeric","local","mean.default","apply","is.na","local","mean.default","apply","mean.default","apply","apply","FUN","apply","apply","FUN","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","apply","apply","length","local","FUN","apply","apply","apply","FUN","apply","apply","apply","mean.default","apply","mean.default","apply","length","local","FUN","apply","apply","mean.default","apply","apply","apply","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","apply","mean.default","apply","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","mean.default","apply","apply","FUN","apply","apply","apply","is.numeric","local","apply","apply","FUN","apply","mean.default","apply","<GC>","is.na","local","<GC>","is.na","local","FUN","apply","FUN","apply","apply","length","local","FUN","apply","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","mean.default","apply","FUN","apply","length","local","isTRUE","mean.default","apply","FUN","apply","apply","apply","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","<GC>","apply","<GC>","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","apply","mean.default","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","apply","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","apply","<GC>","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","is.na","local","is.numeric","local","apply","FUN","apply","apply","is.numeric","local","FUN","apply","isTRUE","mean.default","apply","FUN","apply","length","local","apply","FUN","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","FUN","apply","is.na","local","isTRUE","mean.default","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","length","local","apply","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","mean.default","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","is.na","local","mean.default","apply","mean.default","apply","apply","FUN","apply","isTRUE","mean.default","apply","apply","length","local","<GC>","is.numeric","local","<GC>","is.numeric","local","FUN","apply","apply","FUN","apply","apply","is.numeric","local","FUN","apply","apply","apply","apply","is.na","local","FUN","apply","is.na","local","isTRUE","mean.default","apply","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","apply","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","isTRUE","mean.default","apply","mean.default","apply","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","apply","mean.default","apply","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","FUN","apply","length","local","FUN","apply","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","<GC>","length","local","<GC>","length","local","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","apply","FUN","apply","apply","mean.default","apply","isTRUE","mean.default","apply","is.numeric","local","<GC>","FUN","apply","<GC>","FUN","apply","is.na","local","FUN","apply","mean.default","apply","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","apply","is.numeric","local","FUN","apply","FUN","apply","apply","apply","FUN","apply","apply","FUN","apply","apply","apply","mean.default","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","apply","apply","mean.default","apply","isTRUE","mean.default","apply","apply","mean.default","apply","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","apply","FUN","apply","apply","apply","FUN","apply","mean.default","apply","FUN","apply","apply","is.na","local","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","apply","apply","<GC>","apply","<GC>","apply","length","local","mean.default","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","is.numeric","local","FUN","apply","apply","FUN","apply","mean.default","apply","FUN","apply","is.numeric","local","apply","FUN","apply","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","mean.default","apply","FUN","apply","FUN","apply","apply","FUN","apply","mean.default","apply","FUN","apply","apply","FUN","apply","mean.default","apply","apply","is.numeric","local","mean.default","apply","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","apply","mean.default","apply","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","length","local","FUN","apply","is.na","local","FUN","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","is.na","local","FUN","apply","FUN","apply","length","local","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","length","local","apply","apply","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","length","local","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","apply","FUN","apply","is.na","local","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","apply","mean.default","apply","FUN","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","apply","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","apply","FUN","apply","FUN","apply","length","local","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","length","local","apply","is.na","local","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","is.numeric","local","FUN","apply","is.na","local","FUN","apply","mean.default","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","FUN","apply","mean.default","apply","apply","apply","apply","apply","apply","mean.default","apply","apply","FUN","apply","FUN","apply","mean.default","apply","apply","FUN","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","apply","isTRUE","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","isTRUE","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","apply","<GC>","apply","<GC>","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","apply","mean.default","apply","mean.default","apply","is.na","local","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","length","local","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","<GC>","apply","<GC>","apply","apply","is.numeric","local","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","mean.default","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","apply","apply","apply","FUN","apply","apply","apply","mean.default","apply","<GC>","apply","<GC>","apply","apply","apply","FUN","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","apply","mean.default","apply","<GC>","apply","<GC>","apply","FUN","apply","isTRUE","mean.default","apply","apply","is.na","local","FUN","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","apply","<GC>","apply","mean.default","apply","FUN","apply","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","<GC>","apply","<GC>","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","<GC>","apply","<GC>","apply","<GC>","apply","apply","isTRUE","mean.default","apply","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","length","local","FUN","apply","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","is.numeric","local","apply","mean.default","apply","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","apply","apply","<GC>","apply","<GC>","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","apply","apply","FUN","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","isTRUE","mean.default","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","apply","mean.default","apply","mean.default","apply","mean.default","apply","apply","apply","is.numeric","local","FUN","apply","FUN","apply","mean.default","apply","<GC>","apply","<GC>","apply","FUN","apply","apply","is.na","local","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","length","local","mean.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","length","local","apply","is.na","local","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","apply","mean.default","apply","<GC>","apply","<GC>","apply","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","mean.default","apply","FUN","apply","apply","FUN","apply","<GC>","apply","<GC>","apply","<GC>","apply","apply","FUN","apply","apply","FUN","apply","apply","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","<GC>","apply","<GC>","apply","apply","apply","length","local","apply","mean.default","apply","mean.default","apply","mean.default","apply","apply","is.numeric","local","mean.default","apply","<GC>","apply","<GC>","apply","FUN","apply","apply","apply","apply","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","FUN","apply","<GC>","apply","<GC>","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","apply","FUN","apply","is.numeric","local","FUN","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","apply","apply","FUN","apply","apply","FUN","apply","apply","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","is.numeric","local","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","apply","apply","mean.default","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","is.na","local","apply","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","apply","mean.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","mean.default","apply","apply","is.na","local","FUN","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","apply","FUN","apply","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","is.numeric","local","FUN","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","mean.default","apply","apply","mean.default","apply","apply","FUN","apply","is.numeric","local","FUN","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","is.numeric","local","mean.default","apply","apply","FUN","apply","apply","mean.default","apply","FUN","apply","FUN","apply","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","apply","apply","mean.default","apply","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","apply","apply","apply","apply","apply","FUN","apply","apply","mean.default","apply","apply","length","local","FUN","apply","FUN","apply","FUN","apply","apply","length","local","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","is.numeric","local","FUN","apply","apply","FUN","apply","FUN","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","apply","mean.default","apply","apply","apply","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","apply","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","apply","mean.default","apply","FUN","apply","apply","is.numeric","local","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","length","local","apply","mean.default","apply","is.na","local","apply","length","local","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","mean.default","apply","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","apply","apply","FUN","apply","apply","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","apply","apply","apply","mean.default","apply","apply","apply","apply","mean.default","apply","mean.default","apply","apply","length","local","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","apply","apply","mean.default","apply","apply","FUN","apply","apply","apply","mean.default","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","mean.default","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","apply","is.numeric","local","FUN","apply","length","local","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","apply","mean.default","apply","isTRUE","mean.default","apply","apply","apply","length","local","apply","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","length","local","FUN","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","mean.default","apply","apply","apply","mean.default","apply","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","apply","FUN","apply","apply","FUN","apply","mean.default","apply","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","apply","apply","length","local","apply","apply","FUN","apply","FUN","apply","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","length","local","is.na","local","isTRUE","mean.default","apply","apply","mean.default","apply","apply","apply","mean.default","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","is.numeric","local","FUN","apply","mean.default","apply","apply","mean.default","apply","apply","apply","FUN","apply","apply","apply","FUN","apply","is.na","local","apply","is.numeric","local","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","apply","apply","mean.default","apply","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","apply","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","getFoldFun","constantFoldCall","constantFold","constantFoldCall","constantFold","cmp","cmpPrim2","h","tryInline","cmpCall","cmp","cmpComplexAssign","h","tryInline","cmpCall","cmp","h","tryInline","cmpCall","cmp","cmpForBody","h","tryInline","cmpCall","cmp","genCode","compile","compiler:::tryCompile","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis"],"filenum":[1,1,1,1,1,1,1,1,1,1,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,1,null,1,1,null,1,null,null,1,null,1,1,1,null,1,null,1,1,null,1,null,1,null,null,1,null,null,1,null,1,null,1,null,1,1,null,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,null,null,1,null,1,null,1,1,null,1,null,1,1,null,null,1,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,null,null,1,null,null,null,null,null,null,1,null,1,1,null,1,null,1,null,null,1,1,1,1,1,null,1,1,null,1,null,null,1,null,1,null,1,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,1,null,1,null,1,null,1,1,1,1,null,null,1,null,1,null,1,null,null,null,1,null,null,1,null,1,1,1,null,1,1,null,1,null,1,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,1,null,1,null,1,null,null,1,null,1,null,1,1,null,null,1,null,1,1,null,1,1,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,null,1,1,1,null,null,1,null,1,null,null,null,1,1,null,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,1,null,1,1,null,1,1,1,null,1,1,null,1,1,null,1,null,1,null,1,1,null,null,null,1,null,1,null,1,null,null,null,null,1,null,null,1,null,1,null,null,1,1,null,1,null,null,null,1,null,1,null,1,1,null,1,null,1,null,1,1,null,null,1,null,1,null,1,null,1,null,1,1,null,1,null,null,1,1,1,null,1,1,1,null,1,null,1,1,null,1,1,null,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,1,null,1,1,null,null,null,1,null,null,null,1,null,1,null,1,1,null,1,null,1,null,null,1,1,null,1,1,null,null,1,null,null,null,1,null,1,null,1,null,null,null,1,1,1,1,1,null,null,null,null,null,1,null,1,1,null,1,1,null,1,null,1,null,1,1,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,null,null,1,null,1,null,1,null,1,1,1,1,null,1,null,1,1,null,1,null,1,null,1,1,null,1,null,1,1,null,1,null,null,1,null,1,null,1,1,1,null,null,null,1,null,null,1,null,1,null,1,null,null,null,null,null,null,null,1,null,1,1,null,null,1,null,1,null,null,1,1,null,1,null,1,1,1,null,null,1,1,null,1,1,null,1,null,1,1,null,null,1,1,1,null,1,null,1,1,1,1,null,1,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,1,null,null,null,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,null,1,null,null,1,null,1,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,1,null,1,1,1,null,1,1,null,null,null,1,null,1,null,1,null,1,null,null,null,null,1,null,1,null,1,1,null,null,1,null,null,1,1,1,null,1,null,1,1,null,1,1,null,null,null,null,1,null,1,null,null,null,1,null,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,1,1,1,null,null,1,null,1,null,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,1,null,1,null,null,1,null,null,1,null,1,null,null,1,1,1,1,1,1,1,null,1,null,1,null,null,null,1,1,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,null,null,null,1,null,null,null,1,1,null,1,null,null,1,null,1,null,null,1,null,null,1,null,1,null,1,1,1,1,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,1,null,1,1,null,1,null,null,null,null,null,null,1,null,null,1,1,null,null,null,1,null,1,null,null,null,1,null,null,null,1,null,1,1,null,1,1,null,1,null,1,null,null,1,null,null,1,1,null,1,1,1,null,null,null,1,1,1,null,1,1,1,null,1,null,1,null,null,null,1,1,null,1,1,1,1,null,null,1,null,1,null,1,1,null,1,1,1,null,1,1,null,1,null,1,null,1,1,null,1,1,1,null,null,1,1,null,1,null,1,null,null,null,null,null,null,null,1,null,1,1,null,null,null,1,1,1,null,1,1,null,1,null,1,1,null,1,null,1,null,null,null,null,1,null,1,1,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,1,null,1,null,1,null,1,1,null,1,1,1,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,null,null,null,1,null,1,1,null,null,null,1,null,null,1,null,1,null,null,1,null,1,null,1,null,1,null,null,1,1,null,null,1,null,null,1,null,1,1,null,1,null,null,null,null,1,null,null,1,null,null,1,null,1,null,null,1,1,null,null,1,null,null,1,1,null,1,1,null,1,1,null,null,1,null,null,1,1,null,1,null,1,1,null,null,1,null,1,1,1,null,null,1,null,1,null,null,null,1,null,1,1,null,1,null,null,1,1,null,null,null,null,null,null,null,null,null,1,1,null,1,1,null,null,null,1,1,1,1,null,null,null,1,null,null,null,null,1,1,null,null,1,null,1,null,1,null,1,null,null,1,null,null,1,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,1,1,null,1,1,1,null,1,null,1,null,1,1,null,1,null,null,null,1,1,null,1,null,1,null,1,null,1,null,null,null,null,null,null,1,null,1,null,null,1,null,1,1,1,null,null,1,null,1,null,null,1,1,1,1,null,1,1,null,1,null,null,1,null,null,null,null,1,null,null,1,null,null,null,1,null,1,1,null,null,1,null,null,1,null,1,null,null,1,null,1,null,1,null,1,1,null,1,null,1,null,null,1,null,1,null,1,null,null,1,null,null,1,1,1,null,null,null,1,null,1,1,1,null,1,1,null,1,1,1,null,1,null,1,1,null,1,null,1,null,null,1,null,null,1,null,1,null,1,null,null,1,null,1,1,null,1,null,1,null,1,null,1,1,1,null,1,null,null,1,1,null,1,null,1,null,null,null,1,null,null,null,1,1,null,1,1,1,null,1,null,1,null,1,1,null,null,1,null,null,1,null,1,null,1,null,null,1,null,1,1,1,null,1,null,1,null,null,null,1,null,1,null,1,null,null,1,null,null,null,1,1,null,1,null,1,null,1,null,null,1,null,1,1,null,1,null,null,1,null,null,1,1,null,1,null,1,null,1,1,null,1,null,1,null,1,1,null,1,null,1,1,null,null,null,1,null,1,1,null,null,1,null,null,1,null,null,1,null,null,1,1,1,null,1,null,1,1,null,1,1,null,1,1,null,null,1,null,1,null,1,1,null,null,1,null,null,1,null,1,null,null,null,1,null,null,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,null,null,1,null,null,null,1,null,1,null,1,null,1,null,1,null,null,null,1,null,1,null,null,null,1,null,1,null,1,null,1,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,null,null,1,null,1,1,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,1,1,null,1,null,1,null,null,1,null,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,null,null,1,null,null,1,null,null,1,1,1,null,null,1,null,1,null,1,null,null,1,1,1,1,null,null,1,null,1,null,1,1,null,1,null,1,null,null,1,null,null,1,1,null,1,null,1,null,1,1,null,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,null,1,null,null,1,null,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,null,1,null,null,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,1,1,1,1,1,null,1,1,null,1,null,1,null,1,1,null,1,null,null,null,1,null,null,null,1,1,null,null,1,null,1,null,null,1,1,null,1,null,1,1,null,1,1,null,null,1,null,1,null,null,1,1,null,1,null,1,1,1,null,1,null,1,null,1,null,null,1,1,null,1,1,1,null,1,null,1,null,null,null,null,1,null,null,1,null,1,1,null,1,null,1,null,1,null,1,null,null,1,null,null,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,1,null,1,1,null,null,1,null,null,1,1,null,1,null,1,1,null,1,null,1,1,1,1,null,1,1,1,null,1,null,1,null,1,1,1,null,1,1,1,null,1,null,null,1,null,1,null,null,1,null,1,1,null,1,null,1,null,1,null,1,null,null,1,1,null,null,null,1,null,1,null,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,1,null,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,1,null,1,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,null,1,1,null,1,1,null,1,null,1,null,1,null,1,1,1,null,null,1,null,null,1,null,null,1,1,1,1,null,1,null,1,null,1,null,1,null,null,null,1,1,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,null,1,null,1,null,1,1,null,1,null,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,1,null,1,null,null,1,1,1,1,1,null,1,null,1,null,1,null,null,1,null,1,1,null,1,null,null,1,null,null,1,null,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,1,null,1,null,1,1,null,1,1,null,null,1,1,null,1,null,1,null,null,1,null,null,1,null,1,1,null,1,null,1,null,1,1,1,null,null,null,1,null,1,null,1,null,1,null,1,null,1,1,null,null,null,1,null,1,null,1,null,null,1,1,1,null,1,null,1,null,null,1,null,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,null,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,null,1,1,null,null,1,null,1,1,null,1,null,1,null,1,null,null,1,null,1,1,null,1,null,1,1,null,1,null,1,1,null,1,null,1,null,1,null,1,1,null,1,1,null,1,1,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,1,null,null,1,null,1,null,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,1,1,null,null,1,null,1,null,1,null,1,1,null,null,null,1,null,1,null,1,null,1,1,1,1,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,1,1,null,1,null,1,null,1,null,null,1,null,null,1,1,1,null,1,null,null,null,1,null,1,null,1,1,null,1,null,null,1,null,null,1,null,null,1,1,1,1,null,1,1,null,1,1,1,null,1,null,null,1,null,null,1,1,null,1,1,null,1,null,1,1,null,1,null,1,null,null,null,null,1,null,null,1,null,null,1,1,null,1,1,1,null,null,1,1,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,1,1,1,null,1,null,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,null,null,1,null,1,null,1,null,1,null,1,1,null,1,1,null,1,null,1,null,null,1,1,null,1,1,1,null,1,null,1,1,null,1,null,1,1,null,1,null,1,1,null,1,null,null,null,1,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,1,null,1,1,null,1,1,null,1,null,null,null,1,null,1,null,1,1,null,1,null,null,null,1,1,null,1,1,null,1,null,1,null,1,1,null,1,null,null,1,null,1,null,1,null,1,1,1,1,null,1,null,null,null,null,null,null,null,null,null,null,null,1,1,1,1,1,null,1,1,null,1,1,null,null,null,1,null,1,null,1,1,null,null,1,null,1,null,1,null,1,1,1,null,1,1,null,1,null,1,null,null,null,1,1,null,1,null,1,1,null,null,1,null,null,1,null,null,1,null,1,1,null,1,1,1,1,null,1,null,1,null,1,null,1,null,1,1,null,1,1,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,1,null,null,1,null,1,1,null,1,1,null,1,null,1,1,null,null,null,null,1,null,null,1,null,null,1,null,1,1,null,1,1,1,null,null,1,null,null,1,null,1,null,null,1,null,null,null,null,1,null,1,null,1,1,null,1,null,1,1,null,1,null,1,1,null,1,null,1,null,null,1,null,1,null,1,1,null,1,1,null,1,null,null,null,null,null,null,null,null,null,null,1,null,1,null,1,null,1,null,1,null,1,1,1,null,1,1,1,1,null,1,null,1,null,1,1,1,1,1,null,1,1,1,1,null,1,null,1,1,null,null,null,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,1,1,null,1,1,null,1,1,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,1,null,1,null,1,null,null,1,null,1,1,1,null,1,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,1,1,null,null,null,1,null,null,null,1,null,1,1,null,null,1,null,1,1,null,1,null,null,1,1,1,null,null,1,null,1,null,1,null,1,null,1,null,1,1,null,null,1,null,1,null,1,null,null,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,1,null,1,1,1,null,1,null,1,1,null,1,null,null,1,null,1,null,1,null,1,1,null,1,1,null,1,null,1,1,null,null,1,null,1,1,1,null,1,null,1,null,1,null,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,1,1,null,null,1,1,null,1,null,1,1,1,null,1,null,1,null,1,null,1,1,null,1,1,1,null,1,null,1,null,1,null,null,null,null,null,null,1,1,null,1,1,1,null,1,1,null,null,1,null,null,1,null,null,1,null,1,null,null,1,1,null,null,null,1,null,1,1,null,1,1,1,null,1,1,1,null,1,null,null,1,null,null,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,1,1,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,1,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null],"linenum":[10,10,10,10,10,10,11,11,11,11,11,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,12,null,12,12,null,12,null,null,12,null,12,12,12,null,12,null,12,12,null,12,null,12,null,null,12,null,null,12,null,12,null,12,null,12,12,null,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,null,null,12,null,12,null,12,12,null,12,null,12,12,null,null,12,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,null,null,12,null,null,null,null,null,null,12,null,12,12,null,12,null,12,null,null,12,12,12,12,12,null,12,12,null,12,null,null,12,null,12,null,12,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,12,null,12,null,12,null,12,12,12,12,null,null,12,null,12,null,12,null,null,null,12,null,null,12,null,12,12,12,null,12,12,null,12,null,12,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,12,null,12,null,12,null,null,12,null,12,null,12,12,null,null,12,null,12,12,null,12,12,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,null,12,12,12,null,null,12,null,12,null,null,null,12,12,null,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,12,null,12,12,null,12,12,12,null,12,12,null,12,12,null,12,null,12,null,12,12,null,null,null,12,null,12,null,12,null,null,null,null,12,null,null,12,null,12,null,null,12,12,null,12,null,null,null,12,null,12,null,12,12,null,12,null,12,null,12,12,null,null,12,null,12,null,12,null,12,null,12,12,null,12,null,null,12,12,12,null,12,12,12,null,12,null,12,12,null,12,12,null,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,12,null,12,12,null,null,null,12,null,null,null,12,null,12,null,12,12,null,12,null,12,null,null,12,12,null,12,12,null,null,12,null,null,null,12,null,12,null,12,null,null,null,12,12,12,12,12,null,null,null,null,null,12,null,12,12,null,12,12,null,12,null,12,null,12,12,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,null,null,12,null,12,null,12,null,12,12,12,12,null,12,null,12,12,null,12,null,12,null,12,12,null,12,null,12,12,null,12,null,null,12,null,12,null,12,12,12,null,null,null,12,null,null,12,null,12,null,12,null,null,null,null,null,null,null,12,null,12,12,null,null,12,null,12,null,null,12,12,null,12,null,12,12,12,null,null,12,12,null,12,12,null,12,null,12,12,null,null,12,12,12,null,12,null,12,12,12,12,null,12,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,12,null,null,null,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,null,12,null,null,12,null,12,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,12,null,12,12,12,null,12,12,null,null,null,12,null,12,null,12,null,12,null,null,null,null,12,null,12,null,12,12,null,null,12,null,null,12,12,12,null,12,null,12,12,null,12,12,null,null,null,null,12,null,12,null,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,12,12,12,null,null,12,null,12,null,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,12,null,12,null,null,12,null,null,12,null,12,null,null,12,12,12,12,12,12,12,null,12,null,12,null,null,null,12,12,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,null,null,12,null,null,null,12,12,null,12,null,null,12,null,12,null,null,12,null,null,12,null,12,null,12,12,12,12,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,12,null,12,12,null,12,null,null,null,null,null,null,12,null,null,12,12,null,null,null,12,null,12,null,null,null,12,null,null,null,12,null,12,12,null,12,12,null,12,null,12,null,null,12,null,null,12,12,null,12,12,12,null,null,null,12,12,12,null,12,12,12,null,12,null,12,null,null,null,12,12,null,12,12,12,12,null,null,12,null,12,null,12,12,null,12,12,12,null,12,12,null,12,null,12,null,12,12,null,12,12,12,null,null,12,12,null,12,null,12,null,null,null,null,null,null,null,12,null,12,12,null,null,null,12,12,12,null,12,12,null,12,null,12,12,null,12,null,12,null,null,null,null,12,null,12,12,12,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,12,null,12,null,12,null,12,12,null,12,12,12,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,null,null,null,12,null,12,12,null,null,null,12,null,null,12,null,12,null,null,12,null,12,null,12,null,12,null,null,12,12,null,null,12,null,null,12,null,12,12,null,12,null,null,null,null,12,null,null,12,null,null,12,null,12,null,null,12,12,null,null,12,null,null,12,12,null,12,12,null,12,12,null,null,12,null,null,12,12,null,12,null,12,12,null,null,12,null,12,12,12,null,null,12,null,12,null,null,null,12,null,12,12,null,12,null,null,12,12,null,null,null,null,null,null,null,null,null,12,12,null,12,12,null,null,null,12,12,12,12,null,null,null,12,null,null,null,null,12,12,null,null,12,null,12,null,12,null,12,null,null,12,null,null,12,12,12,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,12,12,null,12,12,12,null,12,null,12,null,12,12,null,12,null,null,null,12,12,null,12,null,12,null,12,null,12,null,null,null,null,null,null,12,null,12,null,null,12,null,12,12,12,null,null,12,null,12,null,null,12,12,12,12,null,12,12,null,12,null,null,12,null,null,null,null,12,null,null,12,null,null,null,12,null,12,12,null,null,12,null,null,12,null,12,null,null,12,null,12,null,12,null,12,12,null,12,null,12,null,null,12,null,12,null,12,null,null,12,null,null,12,12,12,null,null,null,12,null,12,12,12,null,12,12,null,12,12,12,null,12,null,12,12,null,12,null,12,null,null,12,null,null,12,null,12,null,12,null,null,12,null,12,12,null,12,null,12,null,12,null,12,12,12,null,12,null,null,12,12,null,12,null,12,null,null,null,12,null,null,null,12,12,null,12,12,12,null,12,null,12,null,12,12,null,null,12,null,null,12,null,12,null,12,null,null,12,null,12,12,12,null,12,null,12,null,null,null,12,null,12,null,12,null,null,12,null,null,null,12,12,null,12,null,12,null,12,null,null,12,null,12,12,null,12,null,null,12,null,null,12,12,null,12,null,12,null,12,12,null,12,null,12,null,12,12,null,12,null,12,12,null,null,null,12,null,12,12,null,null,12,null,null,12,null,null,12,null,null,12,12,12,null,12,null,12,12,null,12,12,null,12,12,null,null,12,null,12,null,12,12,null,null,12,null,null,12,null,12,null,null,null,12,null,null,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,null,null,12,null,null,null,12,null,12,null,12,null,12,null,12,null,null,null,12,null,12,null,null,null,12,null,12,null,12,null,12,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,null,null,12,null,12,12,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,12,12,null,12,null,12,null,null,12,null,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,null,null,12,null,null,12,null,null,12,12,12,null,null,12,null,12,null,12,null,null,12,12,12,12,null,null,12,null,12,null,12,12,null,12,null,12,null,null,12,null,null,12,12,null,12,null,12,null,12,12,null,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,null,12,null,null,12,null,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,null,12,null,null,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,12,12,12,12,12,null,12,12,null,12,null,12,null,12,12,null,12,null,null,null,12,null,null,null,12,12,null,null,12,null,12,null,null,12,12,null,12,null,12,12,null,12,12,null,null,12,null,12,null,null,12,12,null,12,null,12,12,12,null,12,null,12,null,12,null,null,12,12,null,12,12,12,null,12,null,12,null,null,null,null,12,null,null,12,null,12,12,null,12,null,12,null,12,null,12,null,null,12,null,null,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,12,null,12,12,null,null,12,null,null,12,12,null,12,null,12,12,null,12,null,12,12,12,12,null,12,12,12,null,12,null,12,null,12,12,12,null,12,12,12,null,12,null,null,12,null,12,null,null,12,null,12,12,null,12,null,12,null,12,null,12,null,null,12,12,null,null,null,12,null,12,null,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,12,null,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,12,null,12,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,null,12,12,null,12,12,null,12,null,12,null,12,null,12,12,12,null,null,12,null,null,12,null,null,12,12,12,12,null,12,null,12,null,12,null,12,null,null,null,12,12,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,null,12,null,12,null,12,12,null,12,null,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,12,null,12,null,null,12,12,12,12,12,null,12,null,12,null,12,null,null,12,null,12,12,null,12,null,null,12,null,null,12,null,12,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,12,null,12,null,12,12,null,12,12,null,null,12,12,null,12,null,12,null,null,12,null,null,12,null,12,12,null,12,null,12,null,12,12,12,null,null,null,12,null,12,null,12,null,12,null,12,null,12,12,null,null,null,12,null,12,null,12,null,null,12,12,12,null,12,null,12,null,null,12,null,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,null,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,null,12,12,null,null,12,null,12,12,null,12,null,12,null,12,null,null,12,null,12,12,null,12,null,12,12,null,12,null,12,12,null,12,null,12,null,12,null,12,12,null,12,12,null,12,12,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,12,null,null,12,null,12,null,12,12,12,null,12,null,12,null,12,null,12,null,12,null,12,12,12,null,null,12,null,12,null,12,null,12,12,null,null,null,12,null,12,null,12,null,12,12,12,12,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,12,12,null,12,null,12,null,12,null,null,12,null,null,12,12,12,null,12,null,null,null,12,null,12,null,12,12,null,12,null,null,12,null,null,12,null,null,12,12,12,12,null,12,12,null,12,12,12,null,12,null,null,12,null,null,12,12,null,12,12,null,12,null,12,12,null,12,null,12,null,null,null,null,12,null,null,12,null,null,12,12,null,12,12,12,null,null,12,12,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,12,12,12,null,12,null,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,null,null,12,null,12,null,12,null,12,null,12,12,null,12,12,null,12,null,12,null,null,12,12,null,12,12,12,null,12,null,12,12,null,12,null,12,12,null,12,null,12,12,null,12,null,null,null,12,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,12,null,12,12,null,12,12,null,12,null,null,null,12,null,12,null,12,12,null,12,null,null,null,12,12,null,12,12,null,12,null,12,null,12,12,null,12,null,null,12,null,12,null,12,null,12,12,12,12,null,12,null,null,null,null,null,null,null,null,null,null,null,12,12,12,12,12,null,12,12,null,12,12,null,null,null,12,null,12,null,12,12,null,null,12,null,12,null,12,null,12,12,12,null,12,12,null,12,null,12,null,null,null,12,12,null,12,null,12,12,null,null,12,null,null,12,null,null,12,null,12,12,null,12,12,12,12,null,12,null,12,null,12,null,12,null,12,12,null,12,12,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,12,null,null,12,null,12,12,null,12,12,null,12,null,12,12,null,null,null,null,12,null,null,12,null,null,12,null,12,12,null,12,12,12,null,null,12,null,null,12,null,12,null,null,12,null,null,null,null,12,null,12,null,12,12,null,12,null,12,12,null,12,null,12,12,null,12,null,12,null,null,12,null,12,null,12,12,null,12,12,null,12,null,null,null,null,null,null,null,null,null,null,12,null,12,null,12,null,12,null,12,null,12,12,12,null,12,12,12,12,null,12,null,12,null,12,12,12,12,12,null,12,12,12,12,null,12,null,12,12,null,null,null,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,12,12,null,12,12,null,12,12,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,12,null,12,null,12,null,null,12,null,12,12,12,null,12,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,12,12,null,null,null,12,null,null,null,12,null,12,12,null,null,12,null,12,12,null,12,null,null,12,12,12,null,null,12,null,12,null,12,null,12,null,12,null,12,12,null,null,12,null,12,null,12,null,null,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,12,null,12,12,12,null,12,null,12,12,null,12,null,null,12,null,12,null,12,null,12,12,null,12,12,null,12,null,12,12,null,null,12,null,12,12,12,null,12,null,12,null,12,null,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,12,12,null,null,12,12,null,12,null,12,12,12,null,12,null,12,null,12,null,12,12,null,12,12,12,null,12,null,12,null,12,null,null,null,null,null,null,12,12,null,12,12,12,null,12,12,null,null,12,null,null,12,null,null,12,null,12,null,null,12,12,null,null,null,12,null,12,12,null,12,12,12,null,12,12,12,null,12,null,null,12,null,null,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,12,12,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,13,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,13,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null],"memalloc":[124.5122756958008,124.5122756958008,124.5122756958008,124.5122756958008,124.5122756958008,124.5122756958008,139.7945098876953,139.7945098876953,139.7945098876953,139.7945098876953,139.7945098876953,139.7948760986328,139.7948760986328,139.7948760986328,170.26025390625,170.26025390625,170.26025390625,170.26025390625,170.26025390625,170.26025390625,170.26025390625,170.26025390625,170.26025390625,170.26025390625,170.2602996826172,170.2602996826172,170.2602996826172,170.2602996826172,170.2602996826172,170.2602996826172,170.2602996826172,170.2602996826172,170.2602996826172,170.2602996826172,170.2602996826172,170.2602996826172,170.2602996826172,170.2602996826172,170.2602996826172,170.2602996826172,170.2602996826172,170.2602996826172,170.2599945068359,170.2599945068359,185.5187835693359,185.7369537353516,185.7369537353516,185.9324340820312,185.9324340820312,186.1333541870117,186.1333541870117,186.3334426879883,186.3334426879883,186.5466537475586,186.7771759033203,186.7771759033203,187.0137786865234,187.2439270019531,187.2439270019531,187.4718933105469,187.4718933105469,187.4718933105469,187.6984100341797,187.6984100341797,187.9267730712891,188.1535949707031,188.3839950561523,188.3839950561523,188.523567199707,188.523567199707,185.7264022827148,185.9406433105469,185.9406433105469,186.1725845336914,186.1725845336914,186.4168853759766,186.4168853759766,186.6609878540039,186.9002914428711,186.9002914428711,186.9002914428711,187.1383895874023,187.1383895874023,187.3673858642578,187.3673858642578,187.6032409667969,187.6032409667969,187.8373870849609,188.0735321044922,188.0735321044922,188.0735321044922,188.3102874755859,188.3102874755859,188.5685882568359,188.5685882568359,188.5864334106445,188.5864334106445,188.5864334106445,185.9545745849609,185.9545745849609,185.9545745849609,186.1860198974609,186.1860198974609,186.1860198974609,186.4285049438477,186.4285049438477,186.6740341186523,186.6740341186523,186.918815612793,186.918815612793,187.1595611572266,187.1595611572266,187.3974990844727,187.3974990844727,187.6333389282227,187.6333389282227,187.8688125610352,188.1048431396484,188.1048431396484,188.3417205810547,188.3417205810547,188.5769500732422,188.6665878295898,188.6665878295898,188.6665878295898,186.0038986206055,186.2262649536133,186.2262649536133,186.4625930786133,186.4625930786133,186.7079086303711,186.7079086303711,186.9502563476562,186.9502563476562,187.1915893554688,187.4291305541992,187.4291305541992,187.6640777587891,187.6640777587891,187.8978500366211,187.8978500366211,188.1326141357422,188.1326141357422,188.3665466308594,188.3665466308594,188.6013259887695,188.6013259887695,188.7455596923828,188.7455596923828,188.7455596923828,186.0850448608398,186.0850448608398,186.2958221435547,186.5258712768555,186.5258712768555,186.7681350708008,186.7681350708008,187.0104904174805,187.0104904174805,187.0104904174805,187.2511138916016,187.4904861450195,187.727180480957,187.9621429443359,188.195686340332,188.195686340332,188.4310684204102,188.6661529541016,188.6661529541016,188.8231887817383,188.8231887817383,188.8231887817383,186.1721267700195,186.1721267700195,186.3802261352539,186.3802261352539,186.6068420410156,186.8470077514648,186.8470077514648,187.0899200439453,187.3290252685547,187.3290252685547,187.566162109375,187.566162109375,187.8003768920898,187.8003768920898,188.0339279174805,188.0339279174805,188.2664337158203,188.2664337158203,188.5007171630859,188.5007171630859,188.7351303100586,188.7351303100586,188.8995895385742,188.8995895385742,188.8995895385742,186.2850341796875,186.2850341796875,186.4979400634766,186.7523651123047,186.7523651123047,186.9960403442383,186.9960403442383,187.2343368530273,187.2343368530273,187.4704208374023,187.7063369750977,187.938591003418,188.1710433959961,188.1710433959961,188.4029006958008,188.6368103027344,188.6368103027344,188.8713531494141,188.8713531494141,188.9747467041016,188.9747467041016,188.9747467041016,188.9747467041016,186.4505996704102,186.4505996704102,186.4505996704102,186.662727355957,186.662727355957,186.8895111083984,187.1297378540039,187.369255065918,187.369255065918,187.6072311401367,187.8436813354492,187.8436813354492,188.0789947509766,188.0789947509766,188.3143768310547,188.5474014282227,188.5474014282227,188.7830276489258,188.7830276489258,189.0193862915039,189.0193862915039,189.0486907958984,189.0486907958984,189.0486907958984,186.6283416748047,186.6283416748047,186.846923828125,186.846923828125,187.0801315307617,187.0801315307617,187.3441162109375,187.5827102661133,187.5827102661133,187.8194351196289,187.8194351196289,188.0460052490234,188.0460052490234,188.2783508300781,188.5095596313477,188.5095596313477,188.7426071166992,188.7426071166992,188.9776229858398,189.1214599609375,189.1214599609375,189.1214599609375,186.6340713500977,186.6340713500977,186.8408889770508,187.0668411254883,187.0668411254883,187.3026885986328,187.5411682128906,187.7787322998047,187.7787322998047,188.0152893066406,188.0152893066406,188.2482604980469,188.2482604980469,188.4818649291992,188.4818649291992,188.7148666381836,188.7148666381836,188.9507598876953,189.1854782104492,189.1854782104492,189.1930389404297,189.1930389404297,189.1930389404297,186.8775863647461,187.1019515991211,187.3373031616211,187.3373031616211,187.3373031616211,187.5745239257812,187.5745239257812,187.810546875,187.810546875,188.0469055175781,188.0469055175781,188.3054351806641,188.5387802124023,188.5387802124023,188.5387802124023,188.7718505859375,188.7718505859375,189.0066146850586,189.0066146850586,189.2415542602539,189.2415542602539,189.2634811401367,189.2634811401367,189.2634811401367,186.9665298461914,186.9665298461914,187.1858749389648,187.1858749389648,187.4194793701172,187.4194793701172,187.6554946899414,187.8917922973633,187.8917922973633,188.1284255981445,188.364875793457,188.364875793457,188.5990371704102,188.8326950073242,189.0676727294922,189.0676727294922,189.3027954101562,189.3328018188477,189.3328018188477,187.0666351318359,187.2843475341797,187.2843475341797,187.5151443481445,187.5151443481445,187.7504119873047,187.7504119873047,187.9868545532227,188.2241973876953,188.2241973876953,188.4602584838867,188.4602584838867,188.6941223144531,188.6941223144531,188.9283676147461,188.9283676147461,189.163703918457,189.163703918457,189.4009475708008,189.4009475708008,189.4009475708008,189.4009475708008,189.4009475708008,189.4009475708008,187.2183303833008,187.2183303833008,187.4373779296875,187.4373779296875,187.6685028076172,187.9050369262695,188.1411743164062,188.1411743164062,188.3782653808594,188.3782653808594,188.6137847900391,188.6137847900391,188.8482131958008,188.8482131958008,189.0820770263672,189.0820770263672,189.3179702758789,189.4681091308594,189.4681091308594,187.1716995239258,187.1716995239258,187.3810653686523,187.3810653686523,187.6039733886719,187.8351974487305,187.8351974487305,188.0704040527344,188.3072052001953,188.3072052001953,188.5432357788086,188.5432357788086,188.7795867919922,188.7795867919922,189.0145950317383,189.0145950317383,189.2483520507812,189.4834899902344,189.4834899902344,189.5340194702148,189.5340194702148,189.5340194702148,187.3516693115234,187.5620651245117,187.7809906005859,187.7809906005859,188.0370101928711,188.2744979858398,188.5116958618164,188.5116958618164,188.7498092651367,188.7498092651367,188.9855346679688,189.220832824707,189.220832824707,189.4561538696289,189.5989837646484,189.5989837646484,189.5989837646484,187.375846862793,187.375846862793,187.5778045654297,187.5778045654297,187.7926025390625,187.7926025390625,188.0140609741211,188.0140609741211,188.0140609741211,188.2492141723633,188.2492141723633,188.4875335693359,188.4875335693359,188.7266616821289,188.7266616821289,188.963493347168,189.1976470947266,189.1976470947266,189.4317779541016,189.6628494262695,189.6628494262695,189.6628494262695,189.6628494262695,189.6628494262695,189.6628494262695,189.6628494262695,189.6628494262695,187.5811309814453,187.5811309814453,187.7748413085938,187.7748413085938,187.9846115112305,188.2056350708008,188.2056350708008,188.4421768188477,188.4421768188477,188.7015533447266,188.7015533447266,188.7015533447266,188.9393005371094,189.1734085083008,189.1734085083008,189.4081726074219,189.6415939331055,189.6415939331055,189.6415939331055,189.7256622314453,189.7256622314453,189.7256622314453,187.6214447021484,187.8262023925781,187.8262023925781,188.0400695800781,188.0400695800781,188.2647094726562,188.2647094726562,188.5020980834961,188.5020980834961,188.7400970458984,188.9777984619141,189.2136383056641,189.448600769043,189.6825332641602,189.6825332641602,189.7874755859375,189.7874755859375,189.7874755859375,189.7874755859375,187.6995544433594,187.6995544433594,187.8991394042969,188.1080780029297,188.1080780029297,188.3295822143555,188.5666198730469,188.5666198730469,188.8054046630859,188.8054046630859,189.0433654785156,189.0433654785156,189.2782592773438,189.5128173828125,189.7463073730469,189.7463073730469,189.8482818603516,189.8482818603516,189.8482818603516,187.8114318847656,187.8114318847656,188.0062713623047,188.0062713623047,188.2134704589844,188.2134704589844,188.4363021850586,188.4363021850586,188.6723861694336,188.6723861694336,188.909049987793,188.909049987793,189.1471557617188,189.3816452026367,189.3816452026367,189.615852355957,189.8487243652344,189.8487243652344,189.908088684082,189.908088684082,189.908088684082,189.908088684082,189.908088684082,189.908088684082,189.908088684082,189.908088684082,189.908088684082,189.908088684082,189.908088684082,189.908088684082,189.908088684082,189.908088684082,189.908088684082,189.908088684082,189.908088684082,189.908088684082,187.8477630615234,187.8477630615234,187.9535064697266,188.1448364257812,188.1448364257812,188.3271179199219,188.3271179199219,188.5176849365234,188.5176849365234,188.7259674072266,188.7259674072266,188.9528579711914,188.9528579711914,189.1885528564453,189.1885528564453,189.4198608398438,189.644645690918,189.8687210083008,189.9668121337891,189.9668121337891,187.9735870361328,187.9735870361328,188.1695938110352,188.3716888427734,188.3716888427734,188.5908584594727,188.5908584594727,188.8242797851562,188.8242797851562,189.060417175293,189.2966232299805,189.2966232299805,189.5305328369141,189.5305328369141,189.7636260986328,189.9953536987305,189.9953536987305,190.0248336791992,190.0248336791992,190.0248336791992,188.1181945800781,188.1181945800781,188.3130187988281,188.3130187988281,188.5167465209961,188.740478515625,188.9768295288086,188.9768295288086,189.2130355834961,189.2130355834961,189.4735870361328,189.4735870361328,189.4735870361328,189.7078170776367,189.7078170776367,189.9402008056641,189.9402008056641,190.0817718505859,190.0817718505859,190.0817718505859,190.0817718505859,190.0817718505859,190.0817718505859,188.3016586303711,188.3016586303711,188.4991149902344,188.4991149902344,188.7116317749023,188.9446105957031,188.9446105957031,188.9446105957031,189.1811294555664,189.1811294555664,189.4178924560547,189.4178924560547,189.6543426513672,189.8873138427734,190.1203002929688,190.1203002929688,190.1379013061523,190.1379013061523,188.2985153198242,188.4929428100586,188.6994400024414,188.6994400024414,188.6994400024414,188.9264755249023,189.1646194458008,189.1646194458008,189.4023666381836,189.6396102905273,189.6396102905273,189.8742904663086,189.8742904663086,190.1091842651367,190.1931076049805,190.1931076049805,190.1931076049805,188.3321533203125,188.5411987304688,188.7453460693359,188.7453460693359,188.9697799682617,188.9697799682617,189.2056732177734,189.4430923461914,189.6792831420898,189.9131622314453,189.9131622314453,190.1535949707031,190.2474212646484,190.2474212646484,190.2474212646484,188.4104614257812,188.4104614257812,188.6000213623047,188.6000213623047,188.80078125,188.80078125,189.0210037231445,189.0210037231445,189.2582015991211,189.2582015991211,189.4956665039062,189.4956665039062,189.731689453125,189.9671096801758,190.2038803100586,190.2038803100586,190.3008651733398,190.3008651733398,190.3008651733398,188.4921875,188.4921875,188.6817016601562,188.6817016601562,188.8841857910156,188.8841857910156,189.1072158813477,189.1072158813477,189.3459320068359,189.5859298706055,189.5859298706055,189.8256149291992,189.8256149291992,190.0867385864258,190.0867385864258,190.3280029296875,190.3280029296875,190.3534164428711,190.3534164428711,188.6250381469727,188.6250381469727,188.8169937133789,189.0233993530273,189.0233993530273,189.2504196166992,189.4890823364258,189.4890823364258,189.7281341552734,189.968132019043,189.968132019043,190.2051849365234,190.4051284790039,190.4051284790039,190.4051284790039,190.4051284790039,188.7536315917969,188.7536315917969,188.9471817016602,189.1603775024414,189.1603775024414,189.3935470581055,189.3935470581055,189.6346282958984,189.6346282958984,189.8748550415039,189.8748550415039,190.1145706176758,190.1145706176758,190.3515167236328,190.3515167236328,190.4560852050781,190.4560852050781,190.4560852050781,188.7264099121094,188.7264099121094,188.7264099121094,188.9150619506836,188.9150619506836,189.118049621582,189.118049621582,189.3387985229492,189.6017303466797,189.8412246704102,189.8412246704102,190.0799026489258,190.3243103027344,190.3243103027344,190.5061340332031,190.5061340332031,190.5061340332031,190.5061340332031,188.9441757202148,188.9441757202148,189.1430587768555,189.1430587768555,189.3623657226562,189.3623657226562,189.6011810302734,189.6011810302734,189.6011810302734,189.8408813476562,189.8408813476562,190.080078125,190.080078125,190.3199768066406,190.5554122924805,190.5554122924805,190.5554122924805,190.5554122924805,190.5554122924805,190.5554122924805,188.9739532470703,189.1698608398438,189.3817596435547,189.3817596435547,189.6138076782227,189.6138076782227,189.8529815673828,190.0911026000977,190.0911026000977,190.3289337158203,190.5636520385742,190.5636520385742,190.6038208007812,190.6038208007812,190.6038208007812,188.9985504150391,188.9985504150391,189.1856689453125,189.1856689453125,189.4103927612305,189.4103927612305,189.6390609741211,189.6390609741211,189.6390609741211,189.8789367675781,189.8789367675781,190.1186370849609,190.1186370849609,190.3587188720703,190.3587188720703,190.595573425293,190.595573425293,190.6515502929688,190.6515502929688,190.6515502929688,189.065559387207,189.065559387207,189.2535018920898,189.4560623168945,189.6822967529297,189.9213180541992,189.9213180541992,189.9213180541992,190.1583633422852,190.1583633422852,190.388786315918,190.388786315918,190.388786315918,190.6244430541992,190.6244430541992,190.6983795166016,190.6983795166016,189.1083221435547,189.1083221435547,189.2884979248047,189.2884979248047,189.2884979248047,189.4864654541016,189.4864654541016,189.7059936523438,189.7059936523438,189.9434204101562,190.1807861328125,190.1807861328125,190.4206924438477,190.4206924438477,190.6580657958984,190.7445907592773,190.7445907592773,190.7445907592773,189.1958618164062,189.1958618164062,189.3843307495117,189.3843307495117,189.3843307495117,189.5888671875,189.8142929077148,190.0531158447266,190.2920455932617,190.5302429199219,190.7668838500977,190.7899398803711,190.7899398803711,189.3025894165039,189.3025894165039,189.4923248291016,189.4923248291016,189.6986389160156,189.6986389160156,189.9264755249023,190.1657562255859,190.1657562255859,190.4052810668945,190.4052810668945,190.6442947387695,190.6442947387695,190.8346710205078,190.8346710205078,190.8346710205078,190.8346710205078,190.8346710205078,190.8346710205078,189.4140090942383,189.4140090942383,189.4140090942383,189.6056442260742,189.6056442260742,189.8181076049805,190.0499496459961,190.0499496459961,190.2892761230469,190.2892761230469,190.5285034179688,190.5285034179688,190.7911376953125,190.7911376953125,190.878547668457,190.878547668457,190.878547668457,190.878547668457,189.384880065918,189.384880065918,189.5708465576172,189.5708465576172,189.7717666625977,189.9944839477539,189.9944839477539,190.2336578369141,190.2336578369141,190.4736404418945,190.7125473022461,190.7125473022461,190.9218521118164,190.9218521118164,190.9218521118164,190.9218521118164,190.9218521118164,190.9218521118164,189.5424041748047,189.5424041748047,189.7326431274414,189.7326431274414,189.9401016235352,190.1708526611328,190.4078521728516,190.6446380615234,190.8820266723633,190.8820266723633,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,190.9643249511719,189.4998474121094,189.4998474121094,189.4998474121094,189.4998474121094,189.4998474121094,189.4998474121094,189.5747604370117,189.5747604370117,189.770637512207,189.975700378418,189.975700378418,190.1948699951172,190.4306030273438,190.4306030273438,190.6597595214844,190.6597595214844,190.8764419555664,190.8764419555664,191.1140365600586,191.1140365600586,191.1140365600586,191.3544387817383,191.3544387817383,191.3544387817383,191.5982284545898,191.8378753662109,191.8378753662109,192.0652694702148,192.0652694702148,192.2633819580078,192.2633819580078,192.4604873657227,192.4604873657227,192.6568222045898,192.6568222045898,192.8524856567383,192.8524856567383,193.0481719970703,193.0481719970703,193.2454147338867,193.2454147338867,193.4423065185547,193.6545715332031,193.6545715332031,193.8395843505859,194.0293884277344,194.0293884277344,194.225959777832,194.225959777832,194.3017272949219,194.3017272949219,194.3017272949219,194.3017272949219,194.3017272949219,194.3017272949219,189.8844223022461,190.1009521484375,190.1009521484375,190.3387222290039,190.5780715942383,190.8028182983398,190.8028182983398,191.0212554931641,191.0212554931641,191.2647094726562,191.5149383544922,191.7626571655273,191.7626571655273,192.0062713623047,192.250358581543,192.4952697753906,192.4952697753906,192.7379837036133,192.7379837036133,192.9811706542969,192.9811706542969,193.2250747680664,193.2250747680664,193.4674682617188,193.7118530273438,193.7118530273438,193.9559860229492,194.1936569213867,194.4282989501953,194.4330520629883,194.4330520629883,194.4330520629883,189.9640197753906,189.9640197753906,190.1532516479492,190.1532516479492,190.3786239624023,190.6171646118164,190.6171646118164,190.845085144043,191.0578384399414,191.297477722168,191.297477722168,191.5403900146484,191.7896728515625,191.7896728515625,192.0356903076172,192.0356903076172,192.2798156738281,192.2798156738281,192.5231628417969,192.7672500610352,192.7672500610352,193.0093002319336,193.2533187866211,193.4960174560547,193.4960174560547,193.7391052246094,193.9831924438477,194.2270355224609,194.2270355224609,194.459228515625,194.459228515625,194.5622253417969,194.5622253417969,194.5622253417969,194.5622253417969,194.5622253417969,194.5622253417969,190.2588272094727,190.2588272094727,190.4675369262695,190.4675369262695,190.713134765625,190.9153060913086,190.9153060913086,191.0807647705078,191.0807647705078,191.2161178588867,191.353515625,191.4892654418945,191.4892654418945,191.6250839233398,191.7594985961914,191.7594985961914,191.8952102661133,191.8952102661133,192.0309600830078,192.164909362793,192.164909362793,192.298210144043,192.298210144043,192.4640579223633,192.4640579223633,192.6730651855469,192.6730651855469,192.6730651855469,192.9150085449219,192.9150085449219,193.1572341918945,193.3999176025391,193.6417236328125,193.8818817138672,194.1252670288086,194.1252670288086,194.3664169311523,194.3664169311523,194.5969848632812,194.5969848632812,194.6894226074219,194.6894226074219,194.6894226074219,194.6894226074219,190.4812698364258,190.4812698364258,190.6899719238281,190.6899719238281,190.9122695922852,190.9122695922852,190.9122695922852,191.1327056884766,191.35498046875,191.35498046875,191.5950317382812,191.5950317382812,191.8342056274414,191.8342056274414,192.0739593505859,192.3222045898438,192.3222045898438,192.5651168823242,192.8088531494141,193.0524139404297,193.2945404052734,193.2945404052734,193.5368728637695,193.5368728637695,193.7804183959961,193.7804183959961,193.7804183959961,194.0237808227539,194.0237808227539,194.2689361572266,194.2689361572266,194.5123138427734,194.5123138427734,194.7457046508789,194.7457046508789,194.8144760131836,194.8144760131836,194.8144760131836,194.8144760131836,190.6739959716797,190.6739959716797,190.6739959716797,190.8814086914062,190.8814086914062,191.0893707275391,191.0893707275391,191.2980041503906,191.2980041503906,191.5476837158203,191.5476837158203,191.7881469726562,192.0293502807617,192.0293502807617,192.2758483886719,192.5235290527344,192.5235290527344,192.7649459838867,192.7649459838867,193.0078430175781,193.0078430175781,193.0078430175781,193.2515563964844,193.2515563964844,193.4768829345703,193.4768829345703,193.7026901245117,193.9353866577148,193.9353866577148,194.168098449707,194.168098449707,194.4206008911133,194.4206008911133,194.6539688110352,194.6539688110352,194.6539688110352,194.8778533935547,194.9375305175781,194.9375305175781,194.9375305175781,194.9375305175781,194.9375305175781,194.9375305175781,190.8703765869141,190.8703765869141,191.0750350952148,191.2881698608398,191.2881698608398,191.4961471557617,191.4961471557617,191.7367172241211,191.7367172241211,191.7367172241211,191.9767684936523,191.9767684936523,191.9767684936523,192.2164764404297,192.2164764404297,192.2164764404297,192.4642105102539,192.4642105102539,192.7106018066406,192.7106018066406,192.9536819458008,193.1958389282227,193.4375991821289,193.4375991821289,193.4375991821289,193.679931640625,193.679931640625,193.679931640625,193.9230194091797,194.1670989990234,194.1670989990234,194.4111862182617,194.6562805175781,194.6562805175781,194.8925170898438,195.0586395263672,195.0586395263672,195.0586395263672,195.0586395263672,195.0586395263672,195.0586395263672,190.965461730957,191.1880950927734,191.1880950927734,191.3959045410156,191.3959045410156,191.6024932861328,191.8394622802734,191.8394622802734,191.8394622802734,192.0796813964844,192.0796813964844,192.3196716308594,192.5629272460938,192.8114395141602,192.8114395141602,192.8114395141602,193.0556640625,193.0556640625,193.2980346679688,193.2980346679688,193.5414199829102,193.5414199829102,193.7842559814453,193.7842559814453,194.0245361328125,194.2668151855469,194.2668151855469,194.5095062255859,194.5095062255859,194.5095062255859,194.7539215087891,194.9912185668945,194.9912185668945,195.177734375,195.177734375,195.177734375,195.177734375,195.177734375,195.177734375,191.1264953613281,191.1264953613281,191.3252487182617,191.5277938842773,191.5277938842773,191.7306442260742,191.9637145996094,191.9637145996094,192.2035522460938,192.2035522460938,192.442626953125,192.6832046508789,192.9318466186523,193.1999359130859,193.1999359130859,193.4422378540039,193.4422378540039,193.6849517822266,193.6849517822266,193.9290466308594,193.9290466308594,193.9290466308594,194.1722183227539,194.4159774780273,194.4159774780273,194.4159774780273,194.6603927612305,194.6603927612305,194.9055480957031,194.9055480957031,195.1412658691406,195.1412658691406,195.2949371337891,195.2949371337891,195.2949371337891,195.2949371337891,195.2949371337891,195.2949371337891,191.3422241210938,191.5407104492188,191.7389755249023,191.9453125,191.9453125,192.1798934936523,192.1798934936523,192.4180679321289,192.4180679321289,192.6566848754883,192.6566848754883,192.8976440429688,192.8976440429688,193.1438217163086,193.1438217163086,193.386100769043,193.6268768310547,193.6268768310547,193.6268768310547,193.8695983886719,193.8695983886719,194.1138687133789,194.3554458618164,194.3554458618164,194.5986404418945,194.5986404418945,194.8415679931641,194.8415679931641,195.0849456787109,195.0849456787109,195.3179397583008,195.3179397583008,195.4102325439453,195.4102325439453,195.4102325439453,195.4102325439453,195.4102325439453,195.4102325439453,191.5874710083008,191.7848587036133,191.9723815917969,191.9723815917969,192.1926193237305,192.429084777832,192.6647644042969,192.6647644042969,192.900276184082,192.900276184082,193.1429214477539,193.1429214477539,193.3863754272461,193.6279525756836,193.6279525756836,193.8704681396484,193.8704681396484,194.1126022338867,194.1126022338867,194.3555297851562,194.5985107421875,194.5985107421875,194.8408432006836,194.8408432006836,195.0837020874023,195.0837020874023,195.3211441040039,195.3211441040039,195.5236282348633,195.5236282348633,195.5236282348633,195.5236282348633,195.5236282348633,195.5236282348633,191.6529312133789,191.847526550293,191.847526550293,192.0391082763672,192.0391082763672,192.0391082763672,192.2484512329102,192.2484512329102,192.5012893676758,192.7380065917969,192.9754638671875,192.9754638671875,192.9754638671875,193.2114410400391,193.2114410400391,193.4573059082031,193.4573059082031,193.4573059082031,193.7007446289062,193.9437713623047,194.1871566772461,194.4306488037109,194.4306488037109,194.6740341186523,194.9186859130859,194.9186859130859,195.1632843017578,195.1632843017578,195.1632843017578,195.4038543701172,195.4038543701172,195.6352920532227,195.6352920532227,195.6352920532227,195.6352920532227,195.6352920532227,195.6352920532227,191.8040313720703,191.8040313720703,191.9977188110352,191.9977188110352,192.1863784790039,192.1863784790039,192.3922805786133,192.6201705932617,192.6201705932617,192.6201705932617,192.857048034668,192.857048034668,192.857048034668,193.0939865112305,193.0939865112305,193.3303070068359,193.3303070068359,193.3303070068359,193.5746078491211,193.5746078491211,193.8216171264648,193.8216171264648,194.065544128418,194.065544128418,194.3095169067383,194.5541152954102,194.5541152954102,194.7978286743164,194.7978286743164,195.066291809082,195.066291809082,195.066291809082,195.3112869262695,195.3112869262695,195.5505981445312,195.5505981445312,195.7450332641602,195.7450332641602,195.7450332641602,195.7450332641602,195.7450332641602,195.7450332641602,192.0021820068359,192.1952285766602,192.3827362060547,192.3827362060547,192.5987319946289,192.5987319946289,192.8274459838867,192.8274459838867,193.0632934570312,193.2998352050781,193.5379486083984,193.5379486083984,193.782844543457,194.0292129516602,194.0292129516602,194.2747802734375,194.5207901000977,194.7669372558594,194.7669372558594,195.0118942260742,195.0118942260742,195.2576141357422,195.5039749145508,195.5039749145508,195.7404708862305,195.7404708862305,195.8531265258789,195.8531265258789,195.8531265258789,195.8531265258789,195.8531265258789,195.8531265258789,192.2376937866211,192.2376937866211,192.4250793457031,192.4250793457031,192.622688293457,192.622688293457,192.622688293457,192.8660507202148,192.8660507202148,193.0975723266602,193.3326416015625,193.3326416015625,193.5686721801758,193.5686721801758,193.8075485229492,193.8075485229492,194.0536727905273,194.0536727905273,194.2978286743164,194.5419235229492,194.7872009277344,194.7872009277344,195.0321578979492,195.0321578979492,195.0321578979492,195.276741027832,195.5217437744141,195.5217437744141,195.7625198364258,195.7625198364258,195.9593658447266,195.9593658447266,195.9593658447266,195.9593658447266,195.9593658447266,195.9593658447266,195.9593658447266,195.9593658447266,192.3302764892578,192.5192794799805,192.5192794799805,192.7076950073242,192.9169692993164,193.1378173828125,193.1378173828125,193.3675765991211,193.3675765991211,193.5984420776367,193.5984420776367,193.8361663818359,194.0736694335938,194.0736694335938,194.3097152709961,194.5434036254883,194.5434036254883,194.5434036254883,194.782096862793,194.782096862793,195.0266418457031,195.0266418457031,195.2956695556641,195.2956695556641,195.2956695556641,195.5408096313477,195.5408096313477,195.7853012084961,196.0193099975586,196.0639495849609,196.0639495849609,196.0639495849609,196.0639495849609,192.6096496582031,192.6096496582031,192.7915954589844,192.7915954589844,192.9968795776367,192.9968795776367,193.2102966308594,193.2102966308594,193.4350662231445,193.4350662231445,193.4350662231445,193.6673889160156,193.6673889160156,193.9046173095703,193.9046173095703,194.1435317993164,194.3885955810547,194.3885955810547,194.6333847045898,194.6333847045898,194.8776473999023,194.8776473999023,195.1222610473633,195.1222610473633,195.3667526245117,195.6116485595703,195.6116485595703,195.8568649291992,196.0911178588867,196.0911178588867,196.1668701171875,196.1668701171875,196.1668701171875,196.1668701171875,196.1668701171875,196.1668701171875,192.7414169311523,192.9235458374023,192.9235458374023,193.1440734863281,193.1440734863281,193.356575012207,193.356575012207,193.5783615112305,193.8107070922852,193.8107070922852,194.0470733642578,194.0470733642578,194.2860565185547,194.2860565185547,194.5283584594727,194.7728271484375,194.7728271484375,195.0160598754883,195.0160598754883,195.260368347168,195.5044326782227,195.5044326782227,195.7474822998047,195.7474822998047,195.9920349121094,195.9920349121094,196.2249603271484,196.2680740356445,196.2680740356445,196.2680740356445,196.2680740356445,196.2680740356445,196.2680740356445,192.9271392822266,192.9271392822266,192.9271392822266,193.1096343994141,193.1096343994141,193.1096343994141,193.3059616088867,193.514778137207,193.7343673706055,193.7343673706055,193.9659881591797,193.9659881591797,194.2021179199219,194.4406127929688,194.4406127929688,194.6874847412109,194.9305572509766,194.9305572509766,195.173095703125,195.4408264160156,195.4408264160156,195.4408264160156,195.6840744018555,195.6840744018555,195.9293441772461,195.9293441772461,196.1697311401367,196.3676834106445,196.3676834106445,196.3676834106445,196.3676834106445,196.3676834106445,196.3676834106445,192.9589004516602,192.9589004516602,193.1419677734375,193.1419677734375,193.3305435180664,193.3305435180664,193.533073425293,193.533073425293,193.7446670532227,193.7446670532227,193.9691009521484,194.202018737793,194.202018737793,194.4393768310547,194.4393768310547,194.6783905029297,194.6783905029297,194.9251327514648,194.9251327514648,195.1690444946289,195.1690444946289,195.4132690429688,195.4132690429688,195.6575469970703,195.6575469970703,195.9009170532227,195.9009170532227,196.145881652832,196.380859375,196.380859375,196.4656295776367,196.4656295776367,196.4656295776367,196.4656295776367,196.4656295776367,196.4656295776367,196.4656295776367,196.4656295776367,193.1987686157227,193.1987686157227,193.3829498291016,193.3829498291016,193.595344543457,193.595344543457,193.8011245727539,193.8011245727539,194.020133972168,194.020133972168,194.2534866333008,194.2534866333008,194.4903945922852,194.4903945922852,194.7290725708008,194.7290725708008,194.9716033935547,194.9716033935547,195.2159729003906,195.2159729003906,195.4594268798828,195.4594268798828,195.7036895751953,195.7036895751953,195.9484786987305,196.1923904418945,196.1923904418945,196.4314956665039,196.4314956665039,196.5620651245117,196.5620651245117,196.5620651245117,196.5620651245117,196.5620651245117,196.5620651245117,196.5620651245117,196.5620651245117,196.5620651245117,196.5620651245117,196.5620651245117,196.5620651245117,196.5620651245117,196.5620651245117,196.5620651245117,196.5620651245117,196.5620651245117,196.5620651245117,196.5620651245117,196.5620651245117,196.5620651245117,196.5620651245117,196.5620651245117,196.5620651245117,196.5620651245117,196.5620651245117,196.5620651245117,196.5620651245117,196.5620651245117,196.5620651245117,196.5620651245117,196.5620651245117,196.5620651245117,196.5620651245117,196.5620651245117,196.5620651245117,196.5620651245117,196.5620651245117,196.5620651245117,196.5620651245117,196.5620651245117,196.5620651245117,196.5620651245117,196.5620651245117,196.5620651245117,193.2437057495117,193.2437057495117,193.2437057495117,193.3054809570312,193.3054809570312,193.4685440063477,193.6471786499023,193.8324127197266,193.8324127197266,194.0259857177734,194.0259857177734,194.0259857177734,194.239013671875,194.239013671875,194.239013671875,194.4678344726562,194.4678344726562,194.4678344726562,194.7038726806641,194.7038726806641,194.9296188354492,195.1562728881836,195.1562728881836,195.3892593383789,195.3892593383789,195.3892593383789,195.6286010742188,195.6286010742188,195.8680267333984,196.1078109741211,196.1078109741211,196.3464889526367,196.3464889526367,196.5861587524414,196.6567153930664,196.6567153930664,196.6567153930664,196.6567153930664,196.6567153930664,196.6567153930664,193.4981536865234,193.4981536865234,193.699951171875,193.699951171875,193.8919219970703,194.0960235595703,194.0960235595703,194.3149948120117,194.3149948120117,194.5476303100586,194.782112121582,194.782112121582,195.0167388916016,195.0167388916016,195.2541885375977,195.2541885375977,195.4954452514648,195.4954452514648,195.7390289306641,195.7390289306641,195.984016418457,196.2284545898438,196.4729995727539,196.4729995727539,196.716926574707,196.716926574707,196.7500915527344,196.7500915527344,196.7500915527344,196.7500915527344,196.7500915527344,196.7500915527344,193.677116394043,193.677116394043,193.8611373901367,193.8611373901367,194.0545654296875,194.2622985839844,194.2622985839844,194.4835510253906,194.4835510253906,194.7184982299805,194.7184982299805,194.9546890258789,194.9546890258789,195.1894912719727,195.1894912719727,195.4284896850586,195.4284896850586,195.6694793701172,195.9075241088867,195.9075241088867,196.1430282592773,196.1430282592773,196.4080123901367,196.4080123901367,196.6523056030273,196.6523056030273,196.8419418334961,196.8419418334961,196.8419418334961,196.8419418334961,196.8419418334961,196.8419418334961,193.6994094848633,193.8817291259766,194.0682144165039,194.0682144165039,194.0682144165039,194.2670211791992,194.2670211791992,194.481803894043,194.481803894043,194.713981628418,194.713981628418,194.713981628418,194.9510803222656,195.1889572143555,195.4283752441406,195.6732940673828,195.6732940673828,195.6732940673828,195.9173736572266,195.9173736572266,196.1634292602539,196.1634292602539,196.4101638793945,196.6552352905273,196.6552352905273,196.900390625,196.900390625,196.9323120117188,196.9323120117188,196.9323120117188,196.9323120117188,196.9323120117188,196.9323120117188,193.9472503662109,194.128532409668,194.128532409668,194.3166427612305,194.3166427612305,194.5189514160156,194.5189514160156,194.7377700805664,194.9939880371094,194.9939880371094,194.9939880371094,195.2287521362305,195.2287521362305,195.4603958129883,195.4603958129883,195.6920700073242,195.6920700073242,195.9290924072266,195.9290924072266,196.1700668334961,196.1700668334961,196.4133453369141,196.6568145751953,196.6568145751953,196.8984756469727,196.8984756469727,197.0212554931641,197.0212554931641,197.0212554931641,197.0212554931641,197.0212554931641,197.0212554931641,194.0114974975586,194.1886749267578,194.1886749267578,194.3708267211914,194.3708267211914,194.5663223266602,194.5663223266602,194.7772750854492,194.7772750854492,195.0060729980469,195.0060729980469,195.2406997680664,195.2406997680664,195.4758148193359,195.4758148193359,195.7110900878906,195.7110900878906,195.9532852172852,195.9532852172852,196.1945266723633,196.1945266723633,196.4374008178711,196.4374008178711,196.6816482543945,196.6816482543945,196.9250335693359,197.108757019043,197.108757019043,197.108757019043,197.108757019043,194.1364059448242,194.1364059448242,194.3154525756836,194.3154525756836,194.4990081787109,194.6964263916016,194.9087448120117,195.1399536132812,195.3755111694336,195.610595703125,195.610595703125,195.8433303833008,196.0849075317383,196.0849075317383,196.3270645141602,196.3270645141602,196.5718994140625,196.5718994140625,196.8161697387695,197.0591506958008,197.0591506958008,197.1948013305664,197.1948013305664,197.1948013305664,197.1948013305664,197.1948013305664,197.1948013305664,197.1948013305664,197.1948013305664,194.2862091064453,194.4662017822266,194.4662017822266,194.4662017822266,194.6506271362305,194.6506271362305,194.8501586914062,194.8501586914062,194.8501586914062,195.0633926391602,195.294319152832,195.294319152832,195.5308074951172,195.5308074951172,195.7672348022461,196.0010757446289,196.0010757446289,196.234977722168,196.5029525756836,196.5029525756836,196.5029525756836,196.7484817504883,196.7484817504883,196.9937591552734,196.9937591552734,196.9937591552734,197.2375411987305,197.2795333862305,197.2795333862305,197.2795333862305,197.2795333862305,194.4817581176758,194.6640701293945,194.8501815795898,194.8501815795898,195.0523300170898,195.0523300170898,195.2683563232422,195.2683563232422,195.5008697509766,195.5008697509766,195.5008697509766,195.7383422851562,195.9744567871094,195.9744567871094,196.2091445922852,196.4468383789062,196.6919937133789,196.6919937133789,196.9380569458008,196.9380569458008,197.1824645996094,197.1824645996094,197.3628387451172,197.3628387451172,197.3628387451172,197.3628387451172,197.3628387451172,197.3628387451172,194.5102233886719,194.5102233886719,194.6870193481445,194.8685607910156,194.8685607910156,195.0610427856445,195.0610427856445,195.2914581298828,195.2914581298828,195.5190505981445,195.5190505981445,195.7566680908203,195.7566680908203,195.7566680908203,195.9937515258789,195.9937515258789,196.2288360595703,196.2288360595703,196.4648513793945,196.4648513793945,196.7078857421875,196.7078857421875,196.9533920288086,196.9533920288086,197.1990661621094,197.1990661621094,197.4426040649414,197.4447784423828,197.4447784423828,197.4447784423828,197.4447784423828,194.7624740600586,194.9426422119141,194.9426422119141,195.1292266845703,195.3302459716797,195.3302459716797,195.549430847168,195.549430847168,195.7854309082031,195.7854309082031,196.0221481323242,196.0221481323242,196.2573547363281,196.2573547363281,196.4918975830078,196.4918975830078,196.7322158813477,196.978141784668,197.2248611450195,197.2248611450195,197.470703125,197.5254669189453,197.5254669189453,197.5254669189453,197.5254669189453,197.5254669189453,197.5254669189453,194.8676528930664,195.0478591918945,195.0478591918945,195.2341918945312,195.2341918945312,195.4349746704102,195.6540832519531,195.6540832519531,195.8893814086914,195.8893814086914,196.1272277832031,196.3635940551758,196.5989074707031,196.8374786376953,196.8374786376953,197.0835647583008,197.329231262207,197.5748672485352,197.5748672485352,197.6047286987305,197.6047286987305,197.6047286987305,197.6047286987305,194.9929046630859,195.1745758056641,195.362922668457,195.362922668457,195.5658798217773,195.7869262695312,196.0239410400391,196.0239410400391,196.2608413696289,196.2608413696289,196.2608413696289,196.4975357055664,196.4975357055664,196.7337493896484,196.7337493896484,196.7337493896484,196.9762954711914,196.9762954711914,197.2221450805664,197.492546081543,197.492546081543,197.6828231811523,197.6828231811523,197.6828231811523,197.6828231811523,195.0008316040039,195.0008316040039,195.1754531860352,195.1754531860352,195.1754531860352,195.3582305908203,195.5492248535156,195.5492248535156,195.7580108642578,195.7580108642578,195.9847946166992,195.9847946166992,196.2225189208984,196.2225189208984,196.2225189208984,196.4602661132812,196.4602661132812,196.6961441040039,196.6961441040039,196.9328460693359,196.9328460693359,197.1757049560547,197.1757049560547,197.1757049560547,197.4224243164062,197.4224243164062,197.4224243164062,197.6685943603516,197.6685943603516,197.7595596313477,197.7595596313477,197.7595596313477,197.7595596313477,195.1902008056641,195.1902008056641,195.369499206543,195.369499206543,195.551872253418,195.7503356933594,195.7503356933594,195.9663162231445,195.9663162231445,196.1977310180664,196.1977310180664,196.4358673095703,196.4358673095703,196.6960983276367,196.6960983276367,196.9294662475586,197.1684875488281,197.1684875488281,197.1684875488281,197.4136428833008,197.4136428833008,197.6538543701172,197.6538543701172,197.8351669311523,197.8351669311523,197.8351669311523,197.8351669311523,195.2374954223633,195.2374954223633,195.4125595092773,195.5936508178711,195.5936508178711,195.7860260009766,195.7860260009766,195.9959869384766,196.2253875732422,196.2253875732422,196.4623260498047,196.6993408203125,196.6993408203125,196.9346618652344,196.9346618652344,196.9346618652344,197.1775131225586,197.1775131225586,197.4204254150391,197.4204254150391,197.6661987304688,197.6661987304688,197.9094848632812,197.9094848632812,197.9094848632812,197.9094848632812,197.9094848632812,197.9094848632812,195.4904479980469,195.6716690063477,195.6716690063477,195.6716690063477,195.8615112304688,196.090705871582,196.090705871582,196.3135375976562,196.5486907958984,196.5486907958984,196.7864837646484,196.7864837646484,197.0212478637695,197.0212478637695,197.2571182250977,197.2571182250977,197.4951934814453,197.7406845092773,197.982666015625,197.982666015625,197.982666015625,197.982666015625,197.982666015625,197.982666015625,197.982666015625,197.982666015625,197.982666015625,195.600944519043,195.7814407348633,195.9649887084961,196.1673126220703,196.1673126220703,196.3898162841797,196.3898162841797,196.6277770996094,196.6277770996094,196.8664321899414,196.8664321899414,197.101921081543,197.101921081543,197.3377380371094,197.3377380371094,197.5802459716797,197.826789855957,198.054573059082,198.054573059082,198.054573059082,198.054573059082,198.054573059082,198.054573059082,198.054573059082,198.054573059082,198.054573059082,195.7403335571289,195.7403335571289,195.9208984375,195.9208984375,196.1097183227539,196.1097183227539,196.1097183227539,196.3150024414062,196.3150024414062,196.5331649780273,196.5331649780273,196.7670974731445,196.9913024902344,196.9913024902344,197.2267990112305,197.2267990112305,197.2267990112305,197.4624404907227,197.4624404907227,197.6963500976562,197.6963500976562,197.9332885742188,197.9332885742188,198.1254043579102,198.1254043579102,198.1254043579102,198.1254043579102,198.1254043579102,198.1254043579102,198.1254043579102,198.1254043579102,198.1254043579102,195.8544921875,195.8544921875,196.0357818603516,196.2268447875977,196.2268447875977,196.4363250732422,196.4363250732422,196.6643447875977,196.9020538330078,196.9020538330078,197.1405410766602,197.1405410766602,197.1405410766602,197.3766021728516,197.6138458251953,197.857048034668,198.1033020019531,198.1950149536133,198.1950149536133,198.1950149536133,198.1950149536133,195.8792877197266,195.8792877197266,196.0575714111328,196.0575714111328,196.0575714111328,196.2430419921875,196.2430419921875,196.443489074707,196.6634674072266,196.6634674072266,196.9003829956055,196.9003829956055,196.9003829956055,197.1395568847656,197.1395568847656,197.1395568847656,197.3764495849609,197.3764495849609,197.6129684448242,197.8524932861328,198.0988616943359,198.0988616943359,198.2635879516602,198.2635879516602,198.2635879516602,198.2635879516602,198.2635879516602,198.2635879516602,198.2635879516602,198.2635879516602,198.2635879516602,198.2635879516602,198.2635879516602,198.2635879516602,198.2635879516602,198.2635879516602,198.2635879516602,198.2635879516602,198.2635879516602,198.2635879516602,198.2635879516602,198.2635879516602,198.2635879516602,198.2635879516602,198.2635879516602,198.2635879516602,195.9120101928711,195.9120101928711,195.9120101928711,196.0508346557617,196.0508346557617,196.2154388427734,196.3947296142578,196.3947296142578,196.5856399536133,196.5856399536133,196.7922897338867,197.0168075561523,197.0168075561523,197.256721496582,197.4937438964844,197.4937438964844,197.4937438964844,197.7307815551758,197.9659194946289,197.9659194946289,198.2091293334961,198.2091293334961,198.3305969238281,198.3305969238281,198.3305969238281,198.3305969238281,198.3305969238281,198.3305969238281,196.0517349243164,196.0517349243164,196.227165222168,196.4111022949219,196.4111022949219,196.6060333251953,196.6060333251953,196.8227691650391,196.8227691650391,197.0581130981445,197.2981719970703,197.5611572265625,197.5611572265625,197.7975158691406,197.7975158691406,198.0397262573242,198.0397262573242,198.2860488891602,198.2860488891602,198.3969955444336,198.3969955444336,198.3969955444336,198.3969955444336,196.1628265380859,196.1628265380859,196.339469909668,196.5244979858398,196.5244979858398,196.7255630493164,196.7255630493164,196.9459762573242,196.9459762573242,197.1842727661133,197.1842727661133,197.4248580932617,197.4248580932617,197.4248580932617,197.6632080078125,197.9044799804688,198.1465682983398,198.1465682983398,198.393180847168,198.393180847168,198.462272644043,198.462272644043,198.462272644043,198.462272644043,198.462272644043,198.462272644043,196.2957382202148,196.2957382202148,196.4745559692383,196.4745559692383,196.6612548828125,196.8639984130859,196.8639984130859,197.0884323120117,197.0884323120117,197.3275375366211,197.3275375366211,197.5914688110352,197.5914688110352,197.8292388916016,197.8292388916016,198.0731811523438,198.0731811523438,198.3177719116211,198.3177719116211,198.5264663696289,198.5264663696289,198.5264663696289,198.5264663696289,198.5264663696289,198.5264663696289,196.4675598144531,196.4675598144531,196.6455459594727,196.6455459594727,196.8308715820312,197.0340270996094,197.0340270996094,197.2577438354492,197.2577438354492,197.4953918457031,197.7339935302734,197.7339935302734,197.7339935302734,197.9717559814453,197.9717559814453,198.2081756591797,198.449089050293,198.449089050293,198.5896606445312,198.5896606445312,198.5896606445312,198.5896606445312,196.4372940063477,196.4372940063477,196.4372940063477,196.6116790771484,196.6116790771484,196.7938919067383,196.9879150390625,196.9879150390625,197.2019958496094,197.2019958496094,197.458251953125,197.6972122192383,197.6972122192383,197.935661315918,197.935661315918,198.1718063354492,198.4148864746094,198.4148864746094,198.6518325805664,198.6518325805664,198.6518325805664,198.6518325805664,198.6518325805664,198.6518325805664,196.6370391845703,196.8147277832031,196.8147277832031,197.0012130737305,197.2079849243164,197.2079849243164,197.4356384277344,197.6749801635742,197.9135818481445,197.9135818481445,198.1506271362305,198.1506271362305,198.3878707885742,198.3878707885742,198.6316452026367,198.6316452026367,198.7130355834961,198.7130355834961,198.7130355834961,198.7130355834961,198.7130355834961,198.7130355834961,196.6724700927734,196.8471984863281,196.8471984863281,196.8471984863281,197.0303726196289,197.0303726196289,197.2265701293945,197.2265701293945,197.467658996582,197.7046203613281,197.9434432983398,197.9434432983398,198.1795654296875,198.1795654296875,198.4149017333984,198.4149017333984,198.6498413085938,198.6498413085938,198.7732009887695,198.7732009887695,198.7732009887695,198.7732009887695,196.7332534790039,196.9062728881836,197.0893478393555,197.0893478393555,197.2860717773438,197.5046844482422,197.5046844482422,197.7412033081055,197.7412033081055,197.9809417724609,197.9809417724609,198.2201309204102,198.4606628417969,198.4606628417969,198.7003631591797,198.7003631591797,198.8323745727539,198.8323745727539,198.8323745727539,198.8323745727539,196.8178863525391,196.8178863525391,196.9946670532227,197.1777877807617,197.3773040771484,197.6198806762695,197.8583374023438,197.8583374023438,198.0981750488281,198.0981750488281,198.3366317749023,198.5768966674805,198.5768966674805,198.8198928833008,198.8198928833008,198.8906784057617,198.8906784057617,198.8906784057617,198.8906784057617,196.9435882568359,196.9435882568359,197.1073303222656,197.1073303222656,197.1073303222656,197.2912063598633,197.2912063598633,197.4886245727539,197.4886245727539,197.7085037231445,197.7085037231445,197.9459762573242,198.1834487915039,198.4203872680664,198.4203872680664,198.6597366333008,198.6597366333008,198.9012069702148,198.9012069702148,198.9480590820312,198.9480590820312,198.9480590820312,198.9480590820312,198.9480590820312,198.9480590820312,197.0548477172852,197.229377746582,197.413818359375,197.413818359375,197.6122817993164,197.6122817993164,197.8546142578125,197.8546142578125,198.0908050537109,198.0908050537109,198.329460144043,198.329460144043,198.5660552978516,198.8034133911133,198.8034133911133,199.0043716430664,199.0043716430664,199.0043716430664,199.0043716430664,199.0043716430664,199.0043716430664,199.0043716430664,199.0043716430664,199.0043716430664,197.2049179077148,197.3845291137695,197.5743942260742,197.7770004272461,197.7770004272461,197.998176574707,198.232780456543,198.232780456543,198.4732894897461,198.7095565795898,198.9437408447266,198.9437408447266,199.0599212646484,199.0599212646484,199.0599212646484,199.0599212646484,199.0599212646484,199.0599212646484,197.1741638183594,197.3471221923828,197.3471221923828,197.531608581543,197.7270126342773,197.7270126342773,197.9668884277344,197.9668884277344,198.2032089233398,198.4449005126953,198.4449005126953,198.6838836669922,198.6838836669922,198.9214935302734,198.9214935302734,199.114501953125,199.114501953125,199.114501953125,199.114501953125,199.114501953125,199.114501953125,199.114501953125,199.114501953125,199.114501953125,197.3787460327148,197.5594177246094,197.5594177246094,197.7502365112305,197.9623794555664,198.1916809082031,198.1916809082031,198.1916809082031,198.4332885742188,198.6746368408203,198.9136047363281,198.9136047363281,199.1459197998047,199.1459197998047,199.1459197998047,199.1681976318359,199.1681976318359,199.1681976318359,199.1681976318359,199.1681976318359,199.1681976318359,199.1681976318359,199.1681976318359,199.1681976318359,199.1681976318359,199.1681976318359,199.1681976318359,199.1681976318359,199.1681976318359,199.1681976318359,199.1681976318359,199.1681976318359,199.1681976318359,199.1681976318359,199.1681976318359,199.1681976318359,197.3326187133789,197.3326187133789,197.4935760498047,197.6694030761719,197.8587951660156,198.0660781860352,198.2933349609375,198.2933349609375,198.5333938598633,198.5333938598633,198.5333938598633,198.7727890014648,199.0035171508789,199.0035171508789,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,199.2207870483398,197.4025344848633,197.4025344848633,197.4025344848633,197.4025344848633,197.4624710083008,197.4624710083008,197.6563949584961,197.6563949584961,197.8591232299805,198.0771942138672,198.0771942138672,198.315299987793,198.315299987793,198.5569839477539,198.5569839477539,198.7887344360352,198.7887344360352,199.0077285766602,199.0077285766602,199.2276000976562,199.2276000976562,199.4598083496094,199.6997909545898,199.6997909545898,199.941162109375,200.1818237304688,200.1818237304688,200.4227905273438,200.4227905273438,200.6323089599609,200.6323089599609,200.6323089599609,200.8327865600586,201.0316543579102,201.0316543579102,201.2301864624023,201.4491119384766,201.6477661132812,201.6477661132812,201.846565246582,201.846565246582,202.0450286865234,202.2438430786133,202.2438430786133,202.4427261352539,202.4427261352539,202.6418914794922,202.8406372070312,202.8406372070312,203.0394592285156,203.0394592285156,203.2377395629883,203.4362182617188,203.4362182617188,203.6348648071289,203.6348648071289,203.8340225219727,203.8340225219727,204.0318374633789,204.2302322387695,204.2302322387695,204.4282150268555,204.4282150268555,204.6264801025391,204.6264801025391,204.8256378173828,204.8256378173828,204.9581069946289,204.9581069946289,204.9581069946289,204.9581069946289,204.9581069946289,204.9581069946289,204.9581069946289,204.9581069946289,204.9581069946289,197.8209609985352,198.0182113647461,198.0182113647461,198.2243804931641,198.4477844238281,198.4477844238281,198.6812133789062,198.9368286132812,198.9368286132812,199.1561737060547,199.1561737060547,199.3740997314453,199.3740997314453,199.614013671875,199.614013671875,199.8491134643555,199.8491134643555,200.0946807861328,200.3413467407227,200.3413467407227,200.5868606567383,200.5868606567383,200.8331985473633,200.8331985473633,201.0799713134766,201.3260955810547,201.3260955810547,201.5735855102539,201.8206100463867,201.8206100463867,202.066780090332,202.066780090332,202.3133239746094,202.3133239746094,202.5603485107422,202.8073120117188,202.8073120117188,203.0540313720703,203.0540313720703,203.0540313720703,203.3005523681641,203.3005523681641,203.5469665527344,203.5469665527344,203.7934875488281,203.7934875488281,204.0390853881836,204.2846984863281,204.5316925048828,204.7695236206055,204.7695236206055,205.003776550293,205.003776550293,205.164680480957,205.164680480957,205.164680480957,205.164680480957,205.164680480957,205.164680480957,205.164680480957,205.164680480957,205.164680480957,198.14111328125,198.337287902832,198.5413665771484,198.7635192871094,198.9984817504883,199.2251434326172,199.2251434326172,199.4397354125977,199.672981262207,199.672981262207,199.9134216308594,200.1539764404297,200.1539764404297,200.400993347168,200.400993347168,200.6456069946289,200.6456069946289,200.891975402832,200.891975402832,201.1384124755859,201.3849334716797,201.3849334716797,201.6302032470703,201.876220703125,201.876220703125,202.1164703369141,202.1164703369141,202.3516235351562,202.3516235351562,202.5864410400391,202.8272705078125,203.0622634887695,203.0622634887695,203.3023910522461,203.5464019775391,203.5464019775391,203.791374206543,203.791374206543,204.0368804931641,204.0368804931641,204.2821884155273,204.2821884155273,204.5280914306641,204.7750854492188,204.7750854492188,205.0344543457031,205.0344543457031,205.2692947387695,205.3680419921875,205.3680419921875,205.3680419921875,205.3680419921875,205.3680419921875,205.3680419921875,205.3680419921875,205.3680419921875,205.3680419921875,198.4608993530273,198.4608993530273,198.6554870605469,198.8575210571289,198.8575210571289,199.0738220214844,199.2958679199219,199.5172500610352,199.7371215820312,199.7371215820312,199.9782409667969,199.9782409667969,200.2179946899414,200.2179946899414,200.4522018432617,200.4522018432617,200.6885681152344,200.6885681152344,200.9243927001953,201.1674728393555,201.1674728393555,201.4140396118164,201.6603546142578,201.6603546142578,201.9051513671875,201.9051513671875,201.9051513671875,202.1506423950195,202.1506423950195,202.1506423950195,202.396125793457,202.396125793457,202.6417999267578,202.6417999267578,202.8611755371094,202.8611755371094,203.0866241455078,203.0866241455078,203.3398971557617,203.5720062255859,203.5720062255859,203.5720062255859,203.8067626953125,203.8067626953125,204.0407409667969,204.27587890625,204.27587890625,204.5118942260742,204.7470016479492,204.7470016479492,204.9833297729492,204.9833297729492,205.2092361450195,205.4111633300781,205.4111633300781,205.5680389404297,205.5680389404297,205.5680389404297,205.5680389404297,205.5680389404297,205.5680389404297,205.5680389404297,205.5680389404297,205.5680389404297,198.6899642944336,198.6899642944336,198.8840866088867,199.0849380493164,199.0849380493164,199.2919006347656,199.5036926269531,199.7161636352539,199.7161636352539,199.7161636352539,199.9321823120117,199.9321823120117,200.195426940918,200.4331817626953,200.4331817626953,200.6614532470703,200.6614532470703,200.891716003418,201.1271514892578,201.1271514892578,201.3666915893555,201.3666915893555,201.3666915893555,201.6083450317383,201.6083450317383,201.8500900268555,201.8500900268555,202.0909118652344,202.3320083618164,202.3320083618164,202.57275390625,202.57275390625,202.8138961791992,203.0556259155273,203.0556259155273,203.2956619262695,203.2956619262695,203.5352554321289,203.7750625610352,203.7750625610352,204.0158309936523,204.0158309936523,204.2566070556641,204.2566070556641,204.2566070556641,204.4974975585938,204.4974975585938,204.7366714477539,204.7366714477539,204.9795989990234,205.2143173217773,205.2143173217773,205.4436645507812,205.6737518310547,205.6737518310547,205.7648239135742,205.7648239135742,205.7648239135742,205.7648239135742,205.7648239135742,205.7648239135742,205.7648239135742,205.7648239135742,205.7648239135742,199.0775299072266,199.0775299072266,199.2647247314453,199.2647247314453,199.460563659668,199.460563659668,199.6640930175781,199.6640930175781,199.8699951171875,199.8699951171875,200.0722732543945,200.0722732543945,200.3078155517578,200.5448760986328,200.7801895141602,200.7801895141602,201.0119247436523,201.2460098266602,201.4850997924805,201.7235412597656,201.7235412597656,201.9668655395508,201.9668655395508,202.2106246948242,202.2106246948242,202.4526519775391,202.6905975341797,202.9127502441406,203.1501770019531,203.3925018310547,203.3925018310547,203.633430480957,203.8752365112305,204.1172180175781,204.3593444824219,204.3593444824219,204.6032791137695,204.6032791137695,204.8458023071289,205.0893096923828,205.0893096923828,205.3575897216797,205.3575897216797,205.5938415527344,205.5938415527344,205.8275451660156,205.8275451660156,205.8275451660156,205.9584426879883,205.9584426879883,205.9584426879883,205.9584426879883,205.9584426879883,205.9584426879883,205.9584426879883,205.9584426879883,205.9584426879883,199.3226776123047,199.3226776123047,199.4960479736328,199.4960479736328,199.6881942749023,199.8860244750977,200.0886535644531,200.0886535644531,200.2919006347656,200.5290756225586,200.5290756225586,200.7693710327148,201.0074234008789,201.2427597045898,201.2427597045898,201.4829788208008,201.4829788208008,201.7240905761719,201.7240905761719,201.9654159545898,202.2066268920898,202.2066268920898,202.448974609375,202.448974609375,202.6911697387695,202.6911697387695,202.9322891235352,202.9322891235352,203.1733627319336,203.1733627319336,203.4146728515625,203.4146728515625,203.6552124023438,203.6552124023438,203.6552124023438,203.8973388671875,203.8973388671875,204.1628341674805,204.404182434082,204.404182434082,204.6476974487305,204.6476974487305,204.8914337158203,204.8914337158203,204.8914337158203,205.1342697143555,205.1342697143555,205.3791275024414,205.6243743896484,205.8578186035156,205.8578186035156,206.0915603637695,206.1489181518555,206.1489181518555,206.1489181518555,206.1489181518555,206.1489181518555,206.1489181518555,206.1489181518555,206.1489181518555,206.1489181518555,206.1489181518555,206.1489181518555,206.1489181518555,206.1489181518555,206.1489181518555,206.1489181518555,206.1489181518555,206.1489181518555,206.1489181518555,206.1489181518555,206.1489181518555,206.1489181518555,206.1489181518555,206.1489181518555,206.1489181518555,206.1489181518555,206.1489181518555,206.1489181518555,199.5937347412109,199.5937347412109,199.5937347412109,199.5937347412109,199.5937347412109,199.5937347412109,199.6376342773438,199.8236312866211,200.02099609375,200.02099609375,200.2389144897461,200.2389144897461,200.4395370483398,200.4395370483398,200.664794921875,200.664794921875,200.9030914306641,200.9030914306641,201.1336669921875,201.3570861816406,201.3570861816406,201.3570861816406,201.5832366943359,201.5832366943359,201.810432434082,202.0449676513672,202.0449676513672,202.2806091308594,202.2806091308594,202.2806091308594,202.5163116455078,202.7521514892578,202.9867401123047,202.9867401123047,203.2216567993164,203.4575119018555,203.4575119018555,203.6931991577148,203.6931991577148,203.9299163818359,203.9299163818359,204.1661148071289,204.1661148071289,204.4029998779297,204.4029998779297,204.6411590576172,204.8785247802734,204.8785247802734,204.8785247802734,205.116096496582,205.116096496582,205.3491439819336,205.3491439819336,205.5900802612305,205.5900802612305,205.8192291259766,205.8192291259766,206.0577011108398,206.0577011108398,206.2959976196289,206.2959976196289,206.3363723754883,206.3363723754883,206.3363723754883,206.3363723754883,206.3363723754883,206.3363723754883,206.3363723754883,206.3363723754883,206.3363723754883,199.9951324462891,200.1832046508789,200.1832046508789,200.3748550415039,200.5638427734375,200.7624359130859,200.7624359130859,200.9889678955078,200.9889678955078,201.2231140136719,201.4525604248047,201.4525604248047,201.6833343505859,201.6833343505859,201.6833343505859,201.9075775146484,201.9075775146484,202.1377944946289,202.1377944946289,202.3671569824219,202.3671569824219,202.5965805053711,202.8276062011719,202.8276062011719,203.058837890625,203.2894592285156,203.2894592285156,203.5189895629883,203.5189895629883,203.7503204345703,203.9829483032227,203.9829483032227,203.9829483032227,204.220344543457,204.220344543457,204.4528045654297,204.7096633911133,204.944709777832,204.944709777832,205.1783294677734,205.1783294677734,205.4115219116211,205.4115219116211,205.6464614868164,205.6464614868164,205.6464614868164,205.8817977905273,205.8817977905273,206.1171264648438,206.1171264648438,206.3526229858398,206.5207290649414,206.5207290649414,206.5207290649414,206.5207290649414,206.5207290649414,206.5207290649414,206.5207290649414,206.5207290649414,200.3053665161133,200.4882125854492,200.6739196777344,200.6739196777344,200.8558349609375,201.0552444458008,201.2768020629883,201.2768020629883,201.5070266723633,201.5070266723633,201.7423400878906,201.9749374389648,202.2059631347656,202.2059631347656,202.4384689331055,202.4384689331055,202.6678466796875,202.6678466796875,202.8975601196289,202.8975601196289,203.1066665649414,203.3367309570312,203.3367309570312,203.5643768310547,203.7970657348633,204.0300369262695,204.0300369262695,204.2623519897461,204.2623519897461,204.4966125488281,204.4966125488281,204.7311019897461,204.7311019897461,204.965690612793,204.965690612793,205.2008361816406,205.2008361816406,205.2008361816406,205.4363632202148,205.6702117919922,205.6702117919922,205.9047012329102,206.138542175293,206.3721389770508,206.3721389770508,206.6051330566406,206.7021942138672,206.7021942138672,206.7021942138672,206.7021942138672,206.7021942138672,206.7021942138672,206.7021942138672,206.7021942138672,206.7021942138672,200.4746780395508,200.4746780395508,200.6386032104492,200.6386032104492,200.6386032104492,200.8187408447266,201.0027236938477,201.0027236938477,201.2101669311523,201.2101669311523,201.4224853515625,201.4224853515625,201.6445770263672,201.8679962158203,201.8679962158203,202.0990600585938,202.3271331787109,202.5531921386719,202.5531921386719,202.7803268432617,203.0094985961914,203.2373733520508,203.2373733520508,203.4678115844727,203.4678115844727,203.6980667114258,203.9271926879883,203.9271926879883,204.1572723388672,204.1572723388672,204.3874969482422,204.3874969482422,204.6192474365234,204.6192474365234,204.8498229980469,204.8498229980469,205.079719543457,205.079719543457,205.3106842041016,205.3106842041016,205.5414428710938,205.7739334106445,205.7739334106445,206.0066299438477,206.0066299438477,206.2394409179688,206.2394409179688,206.4721145629883,206.4721145629883,206.7034454345703,206.7034454345703,206.8806686401367,206.8806686401367,206.8806686401367,206.8806686401367,206.8806686401367,206.8806686401367,206.8806686401367,206.8806686401367,206.8806686401367,206.8806686401367,206.8806686401367,206.8806686401367,200.8715591430664,201.050895690918,201.2295303344727,201.4102172851562,201.4102172851562,201.616813659668,209.3848419189453,209.3848419189453,209.3848419189453,209.3848419189453,209.3848419189453,209.3848419189453,209.3848419189453,209.3848419189453,209.3848419189453,209.3848419189453,209.3848419189453,209.3848419189453,209.3848419189453,209.3848419189453,209.3848419189453,209.3848419189453,209.3848419189453,209.3848419189453,209.3848419189453,209.3848419189453,209.3848419189453,209.3848419189453,209.3848419189453,209.3848419189453,217.0142364501953,217.0142364501953,217.0142440795898,217.0142440795898,217.0142440795898,217.0142440795898,217.0142440795898,217.0142440795898,217.0142440795898,217.0142440795898,217.0142440795898,217.0142440795898,217.0142440795898,217.0142440795898,217.0142440795898,217.0142440795898,217.0142440795898,217.0142440795898,217.0142440795898,217.0142440795898,217.0142440795898,217.0142440795898,217.0142440795898,217.0142440795898,217.0142440795898,217.0142440795898,217.0142440795898,217.0142440795898,217.0142440795898,217.0142440795898,217.0142440795898,217.0142440795898,232.2730331420898,232.2730331420898,232.2730331420898,232.2730331420898,232.2730331420898,232.2730331420898,232.2730331420898,232.2730331420898,232.2730331420898,232.2730331420898,232.2730331420898,232.2730331420898,232.2730331420898,232.2730331420898,232.2730331420898,232.2730331420898,232.2730331420898,232.2730331420898,232.2730331420898,232.2730331420898,232.2730331420898,232.2730331420898,232.2730331420898,232.2730331420898,239.9024505615234,239.9024505615234,239.9024505615234,239.9024505615234,239.9024505615234,239.9024505615234,239.9024505615234,239.9024505615234,239.986457824707,239.986457824707,239.986457824707,239.986457824707,239.986457824707,239.986457824707,239.986457824707,239.986457824707,239.986457824707,239.986457824707,239.986457824707,239.986457824707,239.986457824707,239.986457824707,239.986457824707,239.986457824707,239.986457824707,239.986457824707,239.986457824707,239.986457824707,239.986457824707,239.986457824707,239.986457824707,239.986457824707,239.986457824707,239.986457824707,239.986457824707,239.986457824707,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477,255.2976455688477],"meminc":[0,0,0,0,0,0,15.28223419189453,0,0,0,0,0.0003662109375,0,0,30.46537780761719,0,0,0,0,0,0,0,0,0,4.57763671875e-05,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-0.00030517578125,0,15.2587890625,0.218170166015625,0,0.1954803466796875,0,0.2009201049804688,0,0.2000885009765625,0,0.2132110595703125,0.2305221557617188,0,0.236602783203125,0.2301483154296875,0,0.22796630859375,0,0,0.2265167236328125,0,0.228363037109375,0.2268218994140625,0.2304000854492188,0,0.1395721435546875,0,-2.797164916992188,0.2142410278320312,0,0.2319412231445312,0,0.2443008422851562,0,0.2441024780273438,0.2393035888671875,0,0,0.23809814453125,0,0.2289962768554688,0,0.2358551025390625,0,0.2341461181640625,0.23614501953125,0,0,0.23675537109375,0,0.25830078125,0,0.01784515380859375,0,0,-2.631858825683594,0,0,0.2314453125,0,0,0.2424850463867188,0,0.2455291748046875,0,0.244781494140625,0,0.2407455444335938,0,0.2379379272460938,0,0.23583984375,0,0.2354736328125,0.2360305786132812,0,0.23687744140625,0,0.2352294921875,0.08963775634765625,0,0,-2.662689208984375,0.2223663330078125,0,0.236328125,0,0.2453155517578125,0,0.2423477172851562,0,0.2413330078125,0.2375411987304688,0,0.2349472045898438,0,0.2337722778320312,0,0.2347640991210938,0,0.2339324951171875,0,0.2347793579101562,0,0.1442337036132812,0,0,-2.660514831542969,0,0.2107772827148438,0.2300491333007812,0,0.2422637939453125,0,0.2423553466796875,0,0,0.2406234741210938,0.2393722534179688,0.2366943359375,0.2349624633789062,0.2335433959960938,0,0.235382080078125,0.2350845336914062,0,0.1570358276367188,0,0,-2.65106201171875,0,0.208099365234375,0,0.2266159057617188,0.2401657104492188,0,0.2429122924804688,0.239105224609375,0,0.2371368408203125,0,0.2342147827148438,0,0.233551025390625,0,0.2325057983398438,0,0.234283447265625,0,0.2344131469726562,0,0.164459228515625,0,0,-2.614555358886719,0,0.2129058837890625,0.254425048828125,0,0.2436752319335938,0,0.2382965087890625,0,0.236083984375,0.2359161376953125,0.2322540283203125,0.232452392578125,0,0.2318572998046875,0.2339096069335938,0,0.2345428466796875,0,0.1033935546875,0,0,0,-2.524147033691406,0,0,0.212127685546875,0,0.2267837524414062,0.2402267456054688,0.2395172119140625,0,0.23797607421875,0.2364501953125,0,0.2353134155273438,0,0.235382080078125,0.2330245971679688,0,0.235626220703125,0,0.236358642578125,0,0.02930450439453125,0,0,-2.42034912109375,0,0.2185821533203125,0,0.2332077026367188,0,0.2639846801757812,0.2385940551757812,0,0.236724853515625,0,0.2265701293945312,0,0.2323455810546875,0.2312088012695312,0,0.2330474853515625,0,0.235015869140625,0.1438369750976562,0,0,-2.487388610839844,0,0.206817626953125,0.2259521484375,0,0.2358474731445312,0.2384796142578125,0.2375640869140625,0,0.2365570068359375,0,0.23297119140625,0,0.2336044311523438,0,0.233001708984375,0,0.2358932495117188,0.2347183227539062,0,0.00756072998046875,0,0,-2.315452575683594,0.224365234375,0.2353515625,0,0,0.2372207641601562,0,0.23602294921875,0,0.236358642578125,0,0.2585296630859375,0.2333450317382812,0,0,0.2330703735351562,0,0.2347640991210938,0,0.2349395751953125,0,0.0219268798828125,0,0,-2.296951293945312,0,0.2193450927734375,0,0.2336044311523438,0,0.2360153198242188,0.236297607421875,0,0.23663330078125,0.2364501953125,0,0.234161376953125,0.2336578369140625,0.2349777221679688,0,0.2351226806640625,0.03000640869140625,0,-2.266166687011719,0.21771240234375,0,0.2307968139648438,0,0.2352676391601562,0,0.2364425659179688,0.2373428344726562,0,0.2360610961914062,0,0.2338638305664062,0,0.2342453002929688,0,0.2353363037109375,0,0.23724365234375,0,0,0,0,0,-2.1826171875,0,0.2190475463867188,0,0.2311248779296875,0.2365341186523438,0.2361373901367188,0,0.237091064453125,0,0.2355194091796875,0,0.2344284057617188,0,0.2338638305664062,0,0.2358932495117188,0.1501388549804688,0,-2.296409606933594,0,0.2093658447265625,0,0.2229080200195312,0.2312240600585938,0,0.2352066040039062,0.2368011474609375,0,0.2360305786132812,0,0.2363510131835938,0,0.2350082397460938,0,0.2337570190429688,0.235137939453125,0,0.05052947998046875,0,0,-2.182350158691406,0.2103958129882812,0.2189254760742188,0,0.2560195922851562,0.23748779296875,0.2371978759765625,0,0.2381134033203125,0,0.2357254028320312,0.2352981567382812,0,0.235321044921875,0.1428298950195312,0,0,-2.223136901855469,0,0.2019577026367188,0,0.2147979736328125,0,0.2214584350585938,0,0,0.2351531982421875,0,0.2383193969726562,0,0.2391281127929688,0,0.2368316650390625,0.2341537475585938,0,0.234130859375,0.2310714721679688,0,0,0,0,0,0,0,-2.081718444824219,0,0.1937103271484375,0,0.2097702026367188,0.2210235595703125,0,0.236541748046875,0,0.2593765258789062,0,0,0.2377471923828125,0.2341079711914062,0,0.2347640991210938,0.2334213256835938,0,0,0.08406829833984375,0,0,-2.104217529296875,0.2047576904296875,0,0.2138671875,0,0.224639892578125,0,0.2373886108398438,0,0.2379989624023438,0.237701416015625,0.23583984375,0.2349624633789062,0.2339324951171875,0,0.1049423217773438,0,0,0,-2.087921142578125,0,0.1995849609375,0.2089385986328125,0,0.2215042114257812,0.2370376586914062,0,0.2387847900390625,0,0.2379608154296875,0,0.234893798828125,0.23455810546875,0.233489990234375,0,0.1019744873046875,0,0,-2.036849975585938,0,0.1948394775390625,0,0.2071990966796875,0,0.2228317260742188,0,0.236083984375,0,0.236663818359375,0,0.2381057739257812,0.2344894409179688,0,0.2342071533203125,0.2328720092773438,0,0.05936431884765625,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2.060325622558594,0,0.105743408203125,0.1913299560546875,0,0.182281494140625,0,0.1905670166015625,0,0.208282470703125,0,0.2268905639648438,0,0.2356948852539062,0,0.2313079833984375,0.2247848510742188,0.2240753173828125,0.09809112548828125,0,-1.99322509765625,0,0.1960067749023438,0.2020950317382812,0,0.2191696166992188,0,0.2334213256835938,0,0.2361373901367188,0.2362060546875,0,0.2339096069335938,0,0.23309326171875,0.2317276000976562,0,0.02947998046875,0,0,-1.906639099121094,0,0.19482421875,0,0.2037277221679688,0.2237319946289062,0.2363510131835938,0,0.2362060546875,0,0.2605514526367188,0,0,0.2342300415039062,0,0.2323837280273438,0,0.141571044921875,0,0,0,0,0,-1.780113220214844,0,0.1974563598632812,0,0.2125167846679688,0.2329788208007812,0,0,0.2365188598632812,0,0.2367630004882812,0,0.2364501953125,0.23297119140625,0.2329864501953125,0,0.01760101318359375,0,-1.839385986328125,0.194427490234375,0.2064971923828125,0,0,0.2270355224609375,0.2381439208984375,0,0.2377471923828125,0.23724365234375,0,0.23468017578125,0,0.234893798828125,0.08392333984375,0,0,-1.860954284667969,0.20904541015625,0.2041473388671875,0,0.2244338989257812,0,0.2358932495117188,0.2374191284179688,0.2361907958984375,0.2338790893554688,0,0.2404327392578125,0.0938262939453125,0,0,-1.836959838867188,0,0.1895599365234375,0,0.2007598876953125,0,0.2202224731445312,0,0.2371978759765625,0,0.2374649047851562,0,0.23602294921875,0.2354202270507812,0.2367706298828125,0,0.09698486328125,0,0,-1.808677673339844,0,0.18951416015625,0,0.202484130859375,0,0.2230300903320312,0,0.2387161254882812,0.2399978637695312,0,0.23968505859375,0,0.2611236572265625,0,0.2412643432617188,0,0.02541351318359375,0,-1.728378295898438,0,0.19195556640625,0.2064056396484375,0,0.227020263671875,0.2386627197265625,0,0.2390518188476562,0.2399978637695312,0,0.2370529174804688,0.1999435424804688,0,0,0,-1.651496887207031,0,0.1935501098632812,0.21319580078125,0,0.2331695556640625,0,0.2410812377929688,0,0.2402267456054688,0,0.239715576171875,0,0.2369461059570312,0,0.1045684814453125,0,0,-1.72967529296875,0,0,0.1886520385742188,0,0.2029876708984375,0,0.2207489013671875,0.2629318237304688,0.2394943237304688,0,0.238677978515625,0.2444076538085938,0,0.18182373046875,0,0,0,-1.561958312988281,0,0.198883056640625,0,0.2193069458007812,0,0.2388153076171875,0,0,0.2397003173828125,0,0.23919677734375,0,0.239898681640625,0.2354354858398438,0,0,0,0,0,-1.581459045410156,0.1959075927734375,0.2118988037109375,0,0.2320480346679688,0,0.2391738891601562,0.2381210327148438,0,0.2378311157226562,0.2347183227539062,0,0.04016876220703125,0,0,-1.605270385742188,0,0.1871185302734375,0,0.2247238159179688,0,0.228668212890625,0,0,0.2398757934570312,0,0.2397003173828125,0,0.240081787109375,0,0.2368545532226562,0,0.05597686767578125,0,0,-1.585990905761719,0,0.1879425048828125,0.2025604248046875,0.2262344360351562,0.2390213012695312,0,0,0.2370452880859375,0,0.2304229736328125,0,0,0.23565673828125,0,0.07393646240234375,0,-1.590057373046875,0,0.18017578125,0,0,0.197967529296875,0,0.2195281982421875,0,0.2374267578125,0.23736572265625,0,0.2399063110351562,0,0.2373733520507812,0.08652496337890625,0,0,-1.548728942871094,0,0.1884689331054688,0,0,0.2045364379882812,0.2254257202148438,0.2388229370117188,0.2389297485351562,0.2381973266601562,0.2366409301757812,0.0230560302734375,0,-1.487350463867188,0,0.1897354125976562,0,0.2063140869140625,0,0.2278366088867188,0.2392807006835938,0,0.2395248413085938,0,0.239013671875,0,0.1903762817382812,0,0,0,0,0,-1.420661926269531,0,0,0.1916351318359375,0,0.21246337890625,0.231842041015625,0,0.2393264770507812,0,0.239227294921875,0,0.26263427734375,0,0.08740997314453125,0,0,0,-1.493667602539062,0,0.1859664916992188,0,0.2009201049804688,0.22271728515625,0,0.2391738891601562,0,0.2399826049804688,0.2389068603515625,0,0.2093048095703125,0,0,0,0,0,-1.379447937011719,0,0.1902389526367188,0,0.20745849609375,0.2307510375976562,0.23699951171875,0.236785888671875,0.2373886108398438,0,0.08229827880859375,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.4644775390625,0,0,0,0,0,0.07491302490234375,0,0.1958770751953125,0.2050628662109375,0,0.2191696166992188,0.2357330322265625,0,0.229156494140625,0,0.2166824340820312,0,0.2375946044921875,0,0,0.2404022216796875,0,0,0.2437896728515625,0.2396469116210938,0,0.2273941040039062,0,0.1981124877929688,0,0.1971054077148438,0,0.1963348388671875,0,0.1956634521484375,0,0.1956863403320312,0,0.1972427368164062,0,0.1968917846679688,0.2122650146484375,0,0.1850128173828125,0.1898040771484375,0,0.1965713500976562,0,0.07576751708984375,0,0,0,0,0,-4.417304992675781,0.2165298461914062,0,0.2377700805664062,0.239349365234375,0.2247467041015625,0,0.2184371948242188,0,0.2434539794921875,0.2502288818359375,0.2477188110351562,0,0.2436141967773438,0.2440872192382812,0.2449111938476562,0,0.2427139282226562,0,0.2431869506835938,0,0.2439041137695312,0,0.2423934936523438,0.244384765625,0,0.2441329956054688,0.2376708984375,0.2346420288085938,0.00475311279296875,0,0,-4.469032287597656,0,0.1892318725585938,0,0.225372314453125,0.2385406494140625,0,0.2279205322265625,0.2127532958984375,0.2396392822265625,0,0.2429122924804688,0.2492828369140625,0,0.2460174560546875,0,0.2441253662109375,0,0.24334716796875,0.2440872192382812,0,0.2420501708984375,0.2440185546875,0.2426986694335938,0,0.2430877685546875,0.2440872192382812,0.2438430786132812,0,0.2321929931640625,0,0.102996826171875,0,0,0,0,0,-4.303398132324219,0,0.208709716796875,0,0.2455978393554688,0.2021713256835938,0,0.1654586791992188,0,0.1353530883789062,0.1373977661132812,0.1357498168945312,0,0.1358184814453125,0.1344146728515625,0,0.135711669921875,0,0.1357498168945312,0.1339492797851562,0,0.13330078125,0,0.1658477783203125,0,0.2090072631835938,0,0,0.241943359375,0,0.2422256469726562,0.2426834106445312,0.2418060302734375,0.2401580810546875,0.2433853149414062,0,0.24114990234375,0,0.2305679321289062,0,0.092437744140625,0,0,0,-4.208152770996094,0,0.2087020874023438,0,0.2222976684570312,0,0,0.2204360961914062,0.2222747802734375,0,0.24005126953125,0,0.2391738891601562,0,0.2397537231445312,0.2482452392578125,0,0.2429122924804688,0.2437362670898438,0.243560791015625,0.24212646484375,0,0.2423324584960938,0,0.2435455322265625,0,0,0.2433624267578125,0,0.2451553344726562,0,0.243377685546875,0,0.2333908081054688,0,0.0687713623046875,0,0,0,-4.140480041503906,0,0,0.2074127197265625,0,0.2079620361328125,0,0.2086334228515625,0,0.2496795654296875,0,0.2404632568359375,0.2412033081054688,0,0.2464981079101562,0.2476806640625,0,0.2414169311523438,0,0.2428970336914062,0,0,0.24371337890625,0,0.2253265380859375,0,0.2258071899414062,0.232696533203125,0,0.2327117919921875,0,0.25250244140625,0,0.233367919921875,0,0,0.2238845825195312,0.0596771240234375,0,0,0,0,0,-4.067153930664062,0,0.2046585083007812,0.213134765625,0,0.207977294921875,0,0.240570068359375,0,0,0.24005126953125,0,0,0.2397079467773438,0,0,0.2477340698242188,0,0.2463912963867188,0,0.2430801391601562,0.242156982421875,0.24176025390625,0,0,0.2423324584960938,0,0,0.2430877685546875,0.24407958984375,0,0.2440872192382812,0.2450942993164062,0,0.236236572265625,0.1661224365234375,0,0,0,0,0,-4.093177795410156,0.2226333618164062,0,0.2078094482421875,0,0.2065887451171875,0.236968994140625,0,0,0.2402191162109375,0,0.239990234375,0.243255615234375,0.2485122680664062,0,0,0.2442245483398438,0,0.24237060546875,0,0.2433853149414062,0,0.2428359985351562,0,0.2402801513671875,0.242279052734375,0,0.2426910400390625,0,0,0.244415283203125,0.2372970581054688,0,0.1865158081054688,0,0,0,0,0,-4.051239013671875,0,0.1987533569335938,0.202545166015625,0,0.202850341796875,0.2330703735351562,0,0.239837646484375,0,0.23907470703125,0.2405776977539062,0.2486419677734375,0.2680892944335938,0,0.2423019409179688,0,0.2427139282226562,0,0.2440948486328125,0,0,0.2431716918945312,0.2437591552734375,0,0,0.244415283203125,0,0.2451553344726562,0,0.2357177734375,0,0.1536712646484375,0,0,0,0,0,-3.952713012695312,0.198486328125,0.1982650756835938,0.2063369750976562,0,0.2345809936523438,0,0.2381744384765625,0,0.238616943359375,0,0.2409591674804688,0,0.2461776733398438,0,0.242279052734375,0.2407760620117188,0,0,0.2427215576171875,0,0.2442703247070312,0.2415771484375,0,0.243194580078125,0,0.2429275512695312,0,0.243377685546875,0,0.2329940795898438,0,0.09229278564453125,0,0,0,0,0,-3.822761535644531,0.1973876953125,0.1875228881835938,0,0.2202377319335938,0.2364654541015625,0.2356796264648438,0,0.2355117797851562,0,0.242645263671875,0,0.2434539794921875,0.2415771484375,0,0.2425155639648438,0,0.2421340942382812,0,0.2429275512695312,0.24298095703125,0,0.2423324584960938,0,0.24285888671875,0,0.2374420166015625,0,0.202484130859375,0,0,0,0,0,-3.870697021484375,0.1945953369140625,0,0.1915817260742188,0,0,0.2093429565429688,0,0.252838134765625,0.2367172241210938,0.237457275390625,0,0,0.2359771728515625,0,0.2458648681640625,0,0,0.243438720703125,0.2430267333984375,0.2433853149414062,0.2434921264648438,0,0.2433853149414062,0.2446517944335938,0,0.244598388671875,0,0,0.240570068359375,0,0.2314376831054688,0,0,0,0,0,-3.831260681152344,0,0.1936874389648438,0,0.18865966796875,0,0.205902099609375,0.2278900146484375,0,0,0.23687744140625,0,0,0.2369384765625,0,0.2363204956054688,0,0,0.2443008422851562,0,0.24700927734375,0,0.243927001953125,0,0.2439727783203125,0.244598388671875,0,0.24371337890625,0,0.268463134765625,0,0,0.2449951171875,0,0.2393112182617188,0,0.1944351196289062,0,0,0,0,0,-3.742851257324219,0.1930465698242188,0.1875076293945312,0,0.2159957885742188,0,0.2287139892578125,0,0.2358474731445312,0.236541748046875,0.2381134033203125,0,0.2448959350585938,0.246368408203125,0,0.2455673217773438,0.2460098266601562,0.2461471557617188,0,0.2449569702148438,0,0.2457199096679688,0.2463607788085938,0,0.2364959716796875,0,0.1126556396484375,0,0,0,0,0,-3.615432739257812,0,0.1873855590820312,0,0.1976089477539062,0,0,0.2433624267578125,0,0.2315216064453125,0.2350692749023438,0,0.2360305786132812,0,0.2388763427734375,0,0.246124267578125,0,0.2441558837890625,0.2440948486328125,0.2452774047851562,0,0.2449569702148438,0,0,0.2445831298828125,0.2450027465820312,0,0.2407760620117188,0,0.1968460083007812,0,0,0,0,0,0,0,-3.62908935546875,0.1890029907226562,0,0.18841552734375,0.2092742919921875,0.2208480834960938,0,0.2297592163085938,0,0.230865478515625,0,0.2377243041992188,0.2375030517578125,0,0.2360458374023438,0.2336883544921875,0,0,0.2386932373046875,0,0.2445449829101562,0,0.2690277099609375,0,0,0.2451400756835938,0,0.2444915771484375,0.2340087890625,0.04463958740234375,0,0,0,-3.454299926757812,0,0.18194580078125,0,0.2052841186523438,0,0.2134170532226562,0,0.2247695922851562,0,0,0.2323226928710938,0,0.2372283935546875,0,0.2389144897460938,0.2450637817382812,0,0.2447891235351562,0,0.2442626953125,0,0.2446136474609375,0,0.2444915771484375,0.2448959350585938,0,0.2452163696289062,0.2342529296875,0,0.07575225830078125,0,0,0,0,0,-3.425453186035156,0.18212890625,0,0.2205276489257812,0,0.2125015258789062,0,0.2217864990234375,0.2323455810546875,0,0.2363662719726562,0,0.238983154296875,0,0.2423019409179688,0.2444686889648438,0,0.2432327270507812,0,0.2443084716796875,0.2440643310546875,0,0.2430496215820312,0,0.2445526123046875,0,0.2329254150390625,0.04311370849609375,0,0,0,0,0,-3.340934753417969,0,0,0.1824951171875,0,0,0.1963272094726562,0.2088165283203125,0.2195892333984375,0,0.2316207885742188,0,0.2361297607421875,0.238494873046875,0,0.2468719482421875,0.243072509765625,0,0.2425384521484375,0.267730712890625,0,0,0.2432479858398438,0,0.245269775390625,0,0.240386962890625,0.1979522705078125,0,0,0,0,0,-3.408782958984375,0,0.1830673217773438,0,0.1885757446289062,0,0.2025299072265625,0,0.2115936279296875,0,0.2244338989257812,0.2329177856445312,0,0.2373580932617188,0,0.239013671875,0,0.2467422485351562,0,0.2439117431640625,0,0.2442245483398438,0,0.2442779541015625,0,0.2433700561523438,0,0.244964599609375,0.2349777221679688,0,0.08477020263671875,0,0,0,0,0,0,0,-3.266860961914062,0,0.1841812133789062,0,0.2123947143554688,0,0.205780029296875,0,0.2190093994140625,0,0.2333526611328125,0,0.236907958984375,0,0.238677978515625,0,0.2425308227539062,0,0.2443695068359375,0,0.2434539794921875,0,0.2442626953125,0,0.2447891235351562,0.2439117431640625,0,0.239105224609375,0,0.1305694580078125,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-3.318359375,0,0,0.06177520751953125,0,0.1630630493164062,0.1786346435546875,0.1852340698242188,0,0.193572998046875,0,0,0.2130279541015625,0,0,0.22882080078125,0,0,0.2360382080078125,0,0.2257461547851562,0.226654052734375,0,0.2329864501953125,0,0,0.2393417358398438,0,0.2394256591796875,0.2397842407226562,0,0.238677978515625,0,0.2396697998046875,0.070556640625,0,0,0,0,0,-3.158561706542969,0,0.2017974853515625,0,0.1919708251953125,0.2041015625,0,0.2189712524414062,0,0.232635498046875,0.2344818115234375,0,0.2346267700195312,0,0.2374496459960938,0,0.2412567138671875,0,0.2435836791992188,0,0.2449874877929688,0.2444381713867188,0.2445449829101562,0,0.243927001953125,0,0.03316497802734375,0,0,0,0,0,-3.072975158691406,0,0.18402099609375,0,0.1934280395507812,0.207733154296875,0,0.22125244140625,0,0.2349472045898438,0,0.2361907958984375,0,0.23480224609375,0,0.2389984130859375,0,0.2409896850585938,0.2380447387695312,0,0.235504150390625,0,0.264984130859375,0,0.244293212890625,0,0.18963623046875,0,0,0,0,0,-3.142532348632812,0.1823196411132812,0.1864852905273438,0,0,0.1988067626953125,0,0.21478271484375,0,0.232177734375,0,0,0.2370986938476562,0.2378768920898438,0.2394180297851562,0.2449188232421875,0,0,0.24407958984375,0,0.2460556030273438,0,0.246734619140625,0.2450714111328125,0,0.2451553344726562,0,0.03192138671875,0,0,0,0,0,-2.985061645507812,0.1812820434570312,0,0.1881103515625,0,0.2023086547851562,0,0.2188186645507812,0.2562179565429688,0,0,0.2347640991210938,0,0.2316436767578125,0,0.2316741943359375,0,0.2370223999023438,0,0.2409744262695312,0,0.2432785034179688,0.24346923828125,0,0.2416610717773438,0,0.1227798461914062,0,0,0,0,0,-3.009757995605469,0.1771774291992188,0,0.1821517944335938,0,0.19549560546875,0,0.2109527587890625,0,0.2287979125976562,0,0.2346267700195312,0,0.2351150512695312,0,0.2352752685546875,0,0.2421951293945312,0,0.241241455078125,0,0.2428741455078125,0,0.2442474365234375,0,0.2433853149414062,0.1837234497070312,0,0,0,-2.97235107421875,0,0.179046630859375,0,0.1835556030273438,0.197418212890625,0.2123184204101562,0.2312088012695312,0.2355575561523438,0.2350845336914062,0,0.2327346801757812,0.2415771484375,0,0.242156982421875,0,0.2448348999023438,0,0.2442703247070312,0.24298095703125,0,0.135650634765625,0,0,0,0,0,0,0,-2.908592224121094,0.17999267578125,0,0,0.1844253540039062,0,0.1995315551757812,0,0,0.2132339477539062,0.230926513671875,0,0.2364883422851562,0,0.2364273071289062,0.2338409423828125,0,0.2339019775390625,0.267974853515625,0,0,0.2455291748046875,0,0.2452774047851562,0,0,0.2437820434570312,0.0419921875,0,0,0,-2.797775268554688,0.18231201171875,0.1861114501953125,0,0.2021484375,0,0.2160263061523438,0,0.232513427734375,0,0,0.2374725341796875,0.236114501953125,0,0.2346878051757812,0.2376937866210938,0.2451553344726562,0,0.246063232421875,0,0.2444076538085938,0,0.1803741455078125,0,0,0,0,0,-2.852615356445312,0,0.1767959594726562,0.1815414428710938,0,0.1924819946289062,0,0.2304153442382812,0,0.2275924682617188,0,0.2376174926757812,0,0,0.2370834350585938,0,0.2350845336914062,0,0.2360153198242188,0,0.2430343627929688,0,0.2455062866210938,0,0.2456741333007812,0,0.2435379028320312,0.00217437744140625,0,0,0,-2.682304382324219,0.1801681518554688,0,0.18658447265625,0.201019287109375,0,0.2191848754882812,0,0.2360000610351562,0,0.2367172241210938,0,0.2352066040039062,0,0.2345428466796875,0,0.2403182983398438,0.2459259033203125,0.2467193603515625,0,0.2458419799804688,0.0547637939453125,0,0,0,0,0,-2.657814025878906,0.180206298828125,0,0.1863327026367188,0,0.2007827758789062,0.2191085815429688,0,0.2352981567382812,0,0.2378463745117188,0.2363662719726562,0.2353134155273438,0.2385711669921875,0,0.2460861206054688,0.24566650390625,0.245635986328125,0,0.0298614501953125,0,0,0,-2.611824035644531,0.181671142578125,0.1883468627929688,0,0.2029571533203125,0.2210464477539062,0.2370147705078125,0,0.2369003295898438,0,0,0.2366943359375,0,0.2362136840820312,0,0,0.2425460815429688,0,0.245849609375,0.2704010009765625,0,0.190277099609375,0,0,0,-2.681991577148438,0,0.17462158203125,0,0,0.1827774047851562,0.1909942626953125,0,0.2087860107421875,0,0.2267837524414062,0,0.2377243041992188,0,0,0.2377471923828125,0,0.2358779907226562,0,0.2367019653320312,0,0.24285888671875,0,0,0.2467193603515625,0,0,0.2461700439453125,0,0.09096527099609375,0,0,0,-2.569358825683594,0,0.1792984008789062,0,0.182373046875,0.1984634399414062,0,0.2159805297851562,0,0.231414794921875,0,0.2381362915039062,0,0.2602310180664062,0,0.233367919921875,0.2390213012695312,0,0,0.2451553344726562,0,0.2402114868164062,0,0.1813125610351562,0,0,0,-2.597671508789062,0,0.1750640869140625,0.18109130859375,0,0.1923751831054688,0,0.2099609375,0.229400634765625,0,0.2369384765625,0.2370147705078125,0,0.235321044921875,0,0,0.2428512573242188,0,0.2429122924804688,0,0.2457733154296875,0,0.2432861328125,0,0,0,0,0,-2.419036865234375,0.1812210083007812,0,0,0.1898422241210938,0.2291946411132812,0,0.2228317260742188,0.2351531982421875,0,0.23779296875,0,0.2347640991210938,0,0.235870361328125,0,0.2380752563476562,0.2454910278320312,0.2419815063476562,0,0,0,0,0,0,0,0,-2.381721496582031,0.1804962158203125,0.1835479736328125,0.2023239135742188,0,0.222503662109375,0,0.2379608154296875,0,0.2386550903320312,0,0.2354888916015625,0,0.2358169555664062,0,0.2425079345703125,0.2465438842773438,0.227783203125,0,0,0,0,0,0,0,0,-2.314239501953125,0,0.1805648803710938,0,0.1888198852539062,0,0,0.2052841186523438,0,0.2181625366210938,0,0.2339324951171875,0.2242050170898438,0,0.2354965209960938,0,0,0.2356414794921875,0,0.2339096069335938,0,0.2369384765625,0,0.1921157836914062,0,0,0,0,0,0,0,0,-2.270912170410156,0,0.1812896728515625,0.1910629272460938,0,0.2094802856445312,0,0.2280197143554688,0.2377090454101562,0,0.2384872436523438,0,0,0.2360610961914062,0.23724365234375,0.2432022094726562,0.2462539672851562,0.09171295166015625,0,0,0,-2.315727233886719,0,0.17828369140625,0,0,0.1854705810546875,0,0.2004470825195312,0.2199783325195312,0,0.2369155883789062,0,0,0.2391738891601562,0,0,0.2368927001953125,0,0.2365188598632812,0.2395248413085938,0.246368408203125,0,0.1647262573242188,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2.351577758789062,0,0,0.138824462890625,0,0.1646041870117188,0.179290771484375,0,0.1909103393554688,0,0.2066497802734375,0.224517822265625,0,0.2399139404296875,0.2370223999023438,0,0,0.2370376586914062,0.235137939453125,0,0.2432098388671875,0,0.1214675903320312,0,0,0,0,0,-2.278861999511719,0,0.1754302978515625,0.1839370727539062,0,0.1949310302734375,0,0.21673583984375,0,0.2353439331054688,0.2400588989257812,0.2629852294921875,0,0.236358642578125,0,0.2422103881835938,0,0.2463226318359375,0,0.1109466552734375,0,0,0,-2.234169006347656,0,0.1766433715820312,0.185028076171875,0,0.2010650634765625,0,0.2204132080078125,0,0.2382965087890625,0,0.2405853271484375,0,0,0.2383499145507812,0.24127197265625,0.2420883178710938,0,0.246612548828125,0,0.069091796875,0,0,0,0,0,-2.166534423828125,0,0.1788177490234375,0,0.1866989135742188,0.2027435302734375,0,0.2244338989257812,0,0.239105224609375,0,0.2639312744140625,0,0.2377700805664062,0,0.2439422607421875,0,0.2445907592773438,0,0.2086944580078125,0,0,0,0,0,-2.058906555175781,0,0.1779861450195312,0,0.1853256225585938,0.203155517578125,0,0.2237167358398438,0,0.2376480102539062,0.2386016845703125,0,0,0.237762451171875,0,0.236419677734375,0.2409133911132812,0,0.1405715942382812,0,0,0,-2.152366638183594,0,0,0.1743850708007812,0,0.1822128295898438,0.1940231323242188,0,0.214080810546875,0,0.256256103515625,0.2389602661132812,0,0.2384490966796875,0,0.23614501953125,0.2430801391601562,0,0.2369461059570312,0,0,0,0,0,-2.014793395996094,0.1776885986328125,0,0.1864852905273438,0.2067718505859375,0,0.2276535034179688,0.2393417358398438,0.2386016845703125,0,0.2370452880859375,0,0.23724365234375,0,0.2437744140625,0,0.081390380859375,0,0,0,0,0,-2.040565490722656,0.1747283935546875,0,0,0.1831741333007812,0,0.196197509765625,0,0.2410888671875,0.2369613647460938,0.2388229370117188,0,0.2361221313476562,0,0.2353363037109375,0,0.2349395751953125,0,0.1233596801757812,0,0,0,-2.039947509765625,0.1730194091796875,0.183074951171875,0,0.1967239379882812,0.2186126708984375,0,0.2365188598632812,0,0.2397384643554688,0,0.2391891479492188,0.2405319213867188,0,0.2397003173828125,0,0.1320114135742188,0,0,0,-2.014488220214844,0,0.1767807006835938,0.1831207275390625,0.1995162963867188,0.2425765991210938,0.2384567260742188,0,0.239837646484375,0,0.2384567260742188,0.240264892578125,0,0.2429962158203125,0,0.0707855224609375,0,0,0,-1.947090148925781,0,0.1637420654296875,0,0,0.1838760375976562,0,0.197418212890625,0,0.219879150390625,0,0.2374725341796875,0.2374725341796875,0.2369384765625,0,0.239349365234375,0,0.2414703369140625,0,0.04685211181640625,0,0,0,0,0,-1.893211364746094,0.174530029296875,0.1844406127929688,0,0.1984634399414062,0,0.2423324584960938,0,0.2361907958984375,0,0.2386550903320312,0,0.2365951538085938,0.2373580932617188,0,0.200958251953125,0,0,0,0,0,0,0,0,-1.799453735351562,0.1796112060546875,0.1898651123046875,0.202606201171875,0,0.2211761474609375,0.2346038818359375,0,0.240509033203125,0.23626708984375,0.2341842651367188,0,0.116180419921875,0,0,0,0,0,-1.885757446289062,0.1729583740234375,0,0.1844863891601562,0.195404052734375,0,0.2398757934570312,0,0.2363204956054688,0.2416915893554688,0,0.238983154296875,0,0.23760986328125,0,0.1930084228515625,0,0,0,0,0,0,0,0,-1.735755920410156,0.1806716918945312,0,0.1908187866210938,0.2121429443359375,0.2293014526367188,0,0,0.241607666015625,0.2413482666015625,0.2389678955078125,0,0.2323150634765625,0,0,0.02227783203125,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.835578918457031,0,0.1609573364257812,0.1758270263671875,0.18939208984375,0.2072830200195312,0.2272567749023438,0,0.2400588989257812,0,0,0.2393951416015625,0.2307281494140625,0,0.2172698974609375,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.818252563476562,0,0,0,0.0599365234375,0,0.1939239501953125,0,0.202728271484375,0.2180709838867188,0,0.2381057739257812,0,0.2416839599609375,0,0.23175048828125,0,0.218994140625,0,0.2198715209960938,0,0.232208251953125,0.2399826049804688,0,0.2413711547851562,0.24066162109375,0,0.240966796875,0,0.2095184326171875,0,0,0.2004776000976562,0.1988677978515625,0,0.1985321044921875,0.2189254760742188,0.1986541748046875,0,0.1987991333007812,0,0.1984634399414062,0.1988143920898438,0,0.198883056640625,0,0.1991653442382812,0.1987457275390625,0,0.198822021484375,0,0.1982803344726562,0.1984786987304688,0,0.1986465454101562,0,0.19915771484375,0,0.19781494140625,0.198394775390625,0,0.1979827880859375,0,0.1982650756835938,0,0.19915771484375,0,0.1324691772460938,0,0,0,0,0,0,0,0,-7.13714599609375,0.1972503662109375,0,0.2061691284179688,0.2234039306640625,0,0.233428955078125,0.255615234375,0,0.2193450927734375,0,0.217926025390625,0,0.2399139404296875,0,0.2350997924804688,0,0.2455673217773438,0.2466659545898438,0,0.245513916015625,0,0.246337890625,0,0.2467727661132812,0.246124267578125,0,0.2474899291992188,0.2470245361328125,0,0.2461700439453125,0,0.2465438842773438,0,0.2470245361328125,0.2469635009765625,0,0.2467193603515625,0,0,0.24652099609375,0,0.2464141845703125,0,0.24652099609375,0,0.2455978393554688,0.2456130981445312,0.2469940185546875,0.2378311157226562,0,0.2342529296875,0,0.1609039306640625,0,0,0,0,0,0,0,0,-7.023567199707031,0.1961746215820312,0.2040786743164062,0.2221527099609375,0.2349624633789062,0.2266616821289062,0,0.2145919799804688,0.233245849609375,0,0.2404403686523438,0.2405548095703125,0,0.2470169067382812,0,0.2446136474609375,0,0.246368408203125,0,0.2464370727539062,0.24652099609375,0,0.245269775390625,0.2460174560546875,0,0.2402496337890625,0,0.2351531982421875,0,0.2348175048828125,0.2408294677734375,0.2349929809570312,0,0.2401275634765625,0.2440109252929688,0,0.2449722290039062,0,0.2455062866210938,0,0.2453079223632812,0,0.2459030151367188,0.2469940185546875,0,0.259368896484375,0,0.2348403930664062,0.09874725341796875,0,0,0,0,0,0,0,0,-6.907142639160156,0,0.1945877075195312,0.2020339965820312,0,0.2163009643554688,0.2220458984375,0.2213821411132812,0.2198715209960938,0,0.241119384765625,0,0.2397537231445312,0,0.2342071533203125,0,0.2363662719726562,0,0.2358245849609375,0.2430801391601562,0,0.2465667724609375,0.2463150024414062,0,0.2447967529296875,0,0,0.2454910278320312,0,0,0.2454833984375,0,0.2456741333007812,0,0.2193756103515625,0,0.2254486083984375,0,0.2532730102539062,0.2321090698242188,0,0,0.2347564697265625,0,0.233978271484375,0.235137939453125,0,0.2360153198242188,0.235107421875,0,0.236328125,0,0.2259063720703125,0.2019271850585938,0,0.1568756103515625,0,0,0,0,0,0,0,0,-6.878074645996094,0,0.194122314453125,0.2008514404296875,0,0.2069625854492188,0.2117919921875,0.2124710083007812,0,0,0.2160186767578125,0,0.26324462890625,0.2377548217773438,0,0.228271484375,0,0.2302627563476562,0.2354354858398438,0,0.2395401000976562,0,0,0.2416534423828125,0,0.2417449951171875,0,0.2408218383789062,0.2410964965820312,0,0.2407455444335938,0,0.2411422729492188,0.241729736328125,0,0.2400360107421875,0,0.239593505859375,0.23980712890625,0,0.2407684326171875,0,0.2407760620117188,0,0,0.2408905029296875,0,0.2391738891601562,0,0.2429275512695312,0.2347183227539062,0,0.2293472290039062,0.2300872802734375,0,0.09107208251953125,0,0,0,0,0,0,0,0,-6.687294006347656,0,0.18719482421875,0,0.1958389282226562,0,0.2035293579101562,0,0.205902099609375,0,0.2022781372070312,0,0.2355422973632812,0.237060546875,0.2353134155273438,0,0.2317352294921875,0.2340850830078125,0.2390899658203125,0.2384414672851562,0,0.2433242797851562,0,0.2437591552734375,0,0.2420272827148438,0.237945556640625,0.2221527099609375,0.2374267578125,0.2423248291015625,0,0.2409286499023438,0.2418060302734375,0.2419815063476562,0.24212646484375,0,0.2439346313476562,0,0.242523193359375,0.2435073852539062,0,0.268280029296875,0,0.2362518310546875,0,0.23370361328125,0,0,0.1308975219726562,0,0,0,0,0,0,0,0,-6.635765075683594,0,0.173370361328125,0,0.1921463012695312,0.1978302001953125,0.2026290893554688,0,0.2032470703125,0.2371749877929688,0,0.24029541015625,0.2380523681640625,0.2353363037109375,0,0.2402191162109375,0,0.2411117553710938,0,0.2413253784179688,0.2412109375,0,0.2423477172851562,0,0.2421951293945312,0,0.241119384765625,0,0.2410736083984375,0,0.2413101196289062,0,0.24053955078125,0,0,0.24212646484375,0,0.2654953002929688,0.2413482666015625,0,0.2435150146484375,0,0.2437362670898438,0,0,0.2428359985351562,0,0.2448577880859375,0.2452468872070312,0.2334442138671875,0,0.2337417602539062,0.0573577880859375,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-6.555183410644531,0,0,0,0,0,0.0438995361328125,0.1859970092773438,0.1973648071289062,0,0.2179183959960938,0,0.20062255859375,0,0.2252578735351562,0,0.2382965087890625,0,0.2305755615234375,0.223419189453125,0,0,0.2261505126953125,0,0.2271957397460938,0.2345352172851562,0,0.2356414794921875,0,0,0.2357025146484375,0.23583984375,0.234588623046875,0,0.2349166870117188,0.2358551025390625,0,0.235687255859375,0,0.2367172241210938,0,0.2361984252929688,0,0.2368850708007812,0,0.2381591796875,0.23736572265625,0,0,0.2375717163085938,0,0.2330474853515625,0,0.240936279296875,0,0.2291488647460938,0,0.2384719848632812,0,0.2382965087890625,0,0.040374755859375,0,0,0,0,0,0,0,0,-6.341239929199219,0.1880722045898438,0,0.191650390625,0.1889877319335938,0.1985931396484375,0,0.226531982421875,0,0.2341461181640625,0.2294464111328125,0,0.23077392578125,0,0,0.2242431640625,0,0.2302169799804688,0,0.2293624877929688,0,0.2294235229492188,0.2310256958007812,0,0.231231689453125,0.230621337890625,0,0.2295303344726562,0,0.2313308715820312,0.2326278686523438,0,0,0.237396240234375,0,0.2324600219726562,0.2568588256835938,0.23504638671875,0,0.2336196899414062,0,0.2331924438476562,0,0.2349395751953125,0,0,0.2353363037109375,0,0.2353286743164062,0,0.2354965209960938,0.1681060791015625,0,0,0,0,0,0,0,-6.215362548828125,0.1828460693359375,0.1857070922851562,0,0.181915283203125,0.1994094848632812,0.2215576171875,0,0.230224609375,0,0.2353134155273438,0.2325973510742188,0.2310256958007812,0,0.2325057983398438,0,0.2293777465820312,0,0.2297134399414062,0,0.2091064453125,0.2300643920898438,0,0.2276458740234375,0.2326889038085938,0.23297119140625,0,0.2323150634765625,0,0.2342605590820312,0,0.2344894409179688,0,0.234588623046875,0,0.2351455688476562,0,0,0.2355270385742188,0.2338485717773438,0,0.2344894409179688,0.2338409423828125,0.2335968017578125,0,0.2329940795898438,0.0970611572265625,0,0,0,0,0,0,0,0,-6.227516174316406,0,0.1639251708984375,0,0,0.1801376342773438,0.1839828491210938,0,0.2074432373046875,0,0.2123184204101562,0,0.2220916748046875,0.223419189453125,0,0.2310638427734375,0.2280731201171875,0.2260589599609375,0,0.2271347045898438,0.2291717529296875,0.227874755859375,0,0.230438232421875,0,0.230255126953125,0.2291259765625,0,0.2300796508789062,0,0.230224609375,0,0.23175048828125,0,0.2305755615234375,0,0.2298965454101562,0,0.2309646606445312,0,0.2307586669921875,0.2324905395507812,0,0.232696533203125,0,0.2328109741210938,0,0.2326736450195312,0,0.2313308715820312,0,0.1772232055664062,0,0,0,0,0,0,0,0,0,0,0,-6.009109497070312,0.1793365478515625,0.1786346435546875,0.1806869506835938,0,0.2065963745117188,7.768028259277344,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7.62939453125,0,7.62939453125e-06,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,15.2587890625,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7.629417419433594,0,0,0,0,0,0,0,0.08400726318359375,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,15.31118774414062,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"filename":["<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,null,null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,null,null,null,"<expr>",null,null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,null,null,null,null,null,null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,null,"<expr>","<expr>","<expr>","<expr>",null,null,null,"<expr>",null,null,null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,null,null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,null,null,null,null,null,null,null,null,null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,null,null,null,null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,"<expr>","<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null]},"interval":10,"files":[{"filename":"<expr>","content":"## Generate Large Random Dataset\nn <- 2e6\nx <- runif(n)\ny <- runif(n)\nz <- runif(n)\nXYZ <- cbind(x,y,z)\n\n## Inspect 4 equivalent `row mean` calculations \nprofvis::profvis({\n    m <- rowSums(XYZ)/ncol(XYZ)\n    m <- rowMeans(XYZ)\n    m <- apply(XYZ, 1, mean)\n    m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }\n})\n## rowSums(), colSums(), rowMeans(), and colMeans() are vectorised and fast.\n## for loop is not the slowest, but the ugliest.","normpath":"<expr>"}],"prof_output":"/tmp/Rtmp49PNhN/file49d51bab625a.prof","highlight":{"output":["^output\\$"],"gc":["^<GC>$"],"stacktrace":["^\\.\\.stacktraceo(n|ff)\\.\\.$"]},"split":"h"}},"evals":[],"jsHooks":[]}</script>
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
## 1 mean1(x, 0.5)   36.2ms   37.1ms      27.0    7.63MB     0   
## 2 mean2(x, 0.5)   32.6ms   35.6ms      28.4    7.63MB     2.18
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
##   0.115   0.000   0.042
```

```r
system.time({ lm(Y~X, data=DAT) })
```

```
##    user  system elapsed 
##   0.501   0.000   0.182
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
## 1 ma1(y)      277.3ms  277.3ms      3.61    15.3MB     3.61
## 2 ma2(y)       29.4ms   29.6ms     33.8     91.6MB   203.
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
##   0.035   0.003   0.039
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
##   1.237   0.329   0.878
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

