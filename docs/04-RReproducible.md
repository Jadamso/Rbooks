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
<div class="plotly html-widget html-fill-item" id="htmlwidget-3f092049d93d2f618ad9" style="width:672px;height:480px;"></div>
<script type="application/json" data-for="htmlwidget-3f092049d93d2f618ad9">{"x":{"visdat":{"32dc1f3f8692":["function () ","plotlyVisDat"]},"cur_data":"32dc1f3f8692","attrs":{"32dc1f3f8692":{"x":{},"y":{},"alpha_stroke":1,"sizes":[10,100],"spans":[1,20]}},"layout":{"margin":{"b":40,"l":60,"t":25,"r":10},"xaxis":{"domain":[0,1],"automargin":true,"title":"X"},"yaxis":{"domain":[0,1],"automargin":true,"title":"Y"},"hovermode":"closest","showlegend":false},"source":"A","config":{"modeBarButtonsToAdd":["hoverclosest","hovercompare"],"showSendToCloud":false},"data":[{"x":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100],"y":[3.726058073066369,11.297592719839022,13.678573551322277,17.015317125357111,21.305115527824874,24.489599256410305,24.15764882075549,33.2699148283697,34.601478545040173,36.666777008141374,44.917026361161859,47.744793772729103,49.710267609515533,55.858115812453569,58.735559019353893,64.49659384946726,69.173087427638592,71.156830533161525,75.073763030159526,78.050245402557636,87.928754705794134,87.830432111058784,93.841988944810765,96.066654798056575,100.60803885122621,104.40721497650894,106.80081991298769,111.60891066529888,115.41089975611472,118.0078833736374,125.54408896984782,128.2311606697387,132.37008297590256,133.46299167332415,142.32500975566344,146.29504820931362,147.32686217164149,154.53327563362515,154.97284696260124,156.26356368374732,162.32725259136296,169.09023899337498,174.08772265775158,175.48081501297258,178.92442493318612,181.98215056598494,190.93288456458583,191.06330191729469,198.95953123295877,198.14052666041761,204.34030455797759,207.55855508248126,211.15385081239734,215.41511510957048,217.79286137329197,222.17263291228156,228.0894590278572,233.41110264599715,237.75641044116529,243.09010207708729,245.10627699808964,247.99001438805297,252.49923598207258,259.12640988633149,259.87034672292037,264.79056402824506,266.63100746293765,270.77304659267753,273.76693500945112,278.24937371173166,281.32691862122442,290.15370050319325,290.11910544617285,293.18724766387714,300.19157530727682,307.1351092299264,308.58668210860554,311.78612826375564,315.23888366872285,317.61455574475303,323.27191849216734,330.10614920686754,333.06830290030621,337.35559488578571,342.20224826302268,345.04052098499716,348.61290414045067,352.60096330486789,352.60538984565102,359.02368396153219,366.32762168755107,365.4668063097846,373.87824764589902,377.73985513183879,378.6630007357802,385.10734638685631,387.84800650358738,388.59709568620127,394.38292474972843,398.30046835597636],"type":"scatter","mode":"markers","marker":{"color":"rgba(31,119,180,1)","line":{"color":"rgba(31,119,180,1)"}},"error_y":{"color":"rgba(31,119,180,1)"},"error_x":{"color":"rgba(31,119,180,1)"},"line":{"color":"rgba(31,119,180,1)"},"xaxis":"x","yaxis":"y","frame":null}],"highlight":{"on":"plotly_click","persistent":false,"dynamic":false,"selectize":false,"opacityDim":0.20000000000000001,"selected":{"opacity":1},"debounce":0},"shinyEvents":["plotly_hover","plotly_click","plotly_selected","plotly_relayout","plotly_brushed","plotly_brushing","plotly_clickannotation","plotly_doubleclick","plotly_deselect","plotly_afterplot","plotly_sunburstclick"],"base_url":"https://plot.ly"},"evals":[],"jsHooks":[]}</script>
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
##   0.005   0.003   0.007
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
<div class="profvis html-widget html-fill-item" id="htmlwidget-e7b23f5d7c816c8525aa" style="width:100%;height:600px;"></div>
<script type="application/json" data-for="htmlwidget-e7b23f5d7c816c8525aa">{"x":{"message":{"prof":{"time":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,15,16,16,17,17,18,18,19,19,20,20,21,21,22,22,23,23,24,24,25,25,26,26,27,27,28,28,29,29,30,30,31,31,32,33,33,34,35,35,36,36,37,38,39,39,40,40,41,42,42,43,43,44,44,45,46,46,47,47,48,48,48,49,49,50,50,51,51,52,52,53,54,55,55,56,56,57,57,58,58,59,59,60,60,61,61,62,62,63,64,64,65,65,66,67,67,68,68,69,70,71,72,72,73,74,74,75,75,76,76,77,77,78,78,79,80,80,81,81,81,82,82,82,83,84,84,84,85,85,86,86,86,87,87,88,88,89,89,89,90,90,91,91,92,92,93,94,94,95,95,95,96,97,97,98,98,99,99,100,100,101,101,102,102,102,103,103,103,104,104,105,105,106,107,107,108,109,110,110,111,112,112,113,113,113,114,115,115,116,116,117,117,117,118,119,120,120,120,121,121,122,122,122,123,123,124,124,125,125,126,127,127,128,128,129,129,130,130,131,131,132,132,133,133,134,134,135,135,136,136,136,137,137,138,139,139,139,140,140,141,142,142,143,143,143,144,144,145,145,146,147,148,148,149,149,150,150,151,151,152,152,153,154,155,155,156,156,157,157,158,158,159,159,160,160,161,162,162,163,164,165,165,166,166,166,167,167,168,169,169,169,170,170,170,171,171,172,173,173,173,174,175,175,176,176,177,177,178,179,179,180,181,182,182,183,183,184,184,184,185,185,185,186,186,187,187,188,188,189,189,190,190,191,192,192,193,193,194,195,195,196,197,197,197,198,198,198,199,199,199,200,200,200,201,201,202,202,203,203,204,204,205,205,206,206,207,207,208,208,209,209,210,210,210,211,212,212,213,213,214,215,215,216,217,217,218,218,219,219,220,220,221,222,222,222,223,224,224,225,225,226,226,226,226,227,227,227,228,228,229,229,230,231,231,232,233,233,234,235,235,236,236,237,237,237,238,239,239,239,240,240,240,241,241,241,242,243,243,244,244,245,246,246,247,248,249,250,251,251,252,252,253,253,253,254,254,254,255,256,256,257,258,259,259,260,260,261,261,262,262,262,263,263,264,265,265,266,266,267,267,268,268,269,269,270,271,271,272,273,273,274,274,275,276,277,277,278,278,279,280,280,281,281,282,282,283,283,284,284,285,286,287,287,288,288,289,289,289,290,290,290,291,291,292,292,293,294,294,295,295,296,296,297,298,299,299,300,301,301,301,302,302,303,303,304,305,305,306,306,306,307,308,308,309,309,310,310,310,311,311,312,312,312,313,313,313,314,314,314,315,315,315,316,316,316,317,317,317,318,318,318,319,319,319,320,320,320,321,321,321,322,322,322,323,324,324,324,325,325,326,327,327,328,328,329,329,330,330,331,331,332,332,333,333,334,334,335,335,336,337,337,337,338,339,340,341,341,342,342,343,343,344,344,345,345,345,346,346,346,347,347,348,348,349,350,350,351,351,351,352,352,353,353,353,354,354,355,355,356,356,356,357,357,357,358,359,359,360,360,361,361,362,363,363,364,365,365,366,366,367,367,368,368,369,369,370,370,371,371,371,372,372,373,374,375,375,376,376,377,378,378,379,379,379,380,381,381,382,382,383,383,384,384,385,385,386,387,387,388,388,389,389,389,390,390,390,391,391,392,393,393,394,394,395,395,396,396,397,397,398,398,399,400,400,400,401,401,402,402,403,403,404,404,405,406,406,407,407,408,408,409,410,410,411,411,412,412,413,413,413,414,414,415,415,416,416,417,418,418,419,419,420,420,420,421,421,421,422,422,423,424,424,424,425,425,426,426,427,427,428,428,429,429,430,431,431,432,432,433,433,434,435,435,436,436,437,438,439,439,440,440,441,441,442,442,443,443,444,445,445,446,446,446,447,447,448,448,449,449,450,451,451,451,452,452,453,453,454,454,454,455,455,456,456,457,457,458,459,460,460,461,461,462,462,462,463,463,463,464,464,465,465,466,467,468,468,469,469,470,471,471,472,472,473,474,474,474,475,475,475,476,476,477,478,478,479,479,480,480,481,481,482,482,482,483,484,484,485,485,486,486,486,487,488,488,489,489,490,490,491,492,492,493,493,493,494,494,495,495,496,496,497,498,498,499,499,500,500,500,501,501,502,502,502,503,504,505,505,506,506,506,507,508,509,509,509,510,511,511,512,512,513,513,514,515,515,515,516,516,516,517,518,519,519,520,520,521,522,522,523,523,524,524,524,525,525,525,526,526,526,527,527,528,528,529,529,530,530,531,532,532,533,533,534,534,535,535,536,537,537,538,538,539,539,540,541,542,542,542,543,543,543,544,544,544,545,545,545,546,546,546,547,547,547,548,548,548,549,549,549,550,550,550,551,551,551,552,552,552,553,553,553,554,554,554,555,555,555,556,556,556,557,557,557,558,558,558,559,559,559,560,560,560,561,561,561,562,562,562,563,563,563,564,564,564,565,565,565,566,566,566,567,567,567,568,568,568,569,569,569,570,570,570,571,571,571,572,572,572,573,573,573,574,574,574,575,576,576,576,577,577,578,578,578,579,579,580,580,581,581,582,582,583,583,584,584,584,585,586,586,587,587,588,588,589,589,590,590,591,591,592,592,593,593,594,595,596,596,597,597,598,599,599,600,600,601,601,602,602,603,604,605,606,607,608,608,608,609,609,610,610,611,612,613,613,614,614,615,615,616,617,617,618,619,619,620,620,621,622,622,622,623,623,623,624,625,625,626,626,627,627,627,628,628,628,629,630,630,631,632,632,633,634,634,635,635,636,637,638,638,638,639,639,639,640,641,641,642,642,643,643,643,644,645,645,646,646,647,647,648,648,648,649,650,650,651,651,652,652,653,653,654,654,655,655,656,657,657,658,658,659,659,660,660,660,661,661,662,662,663,663,664,664,665,665,665,666,666,667,667,668,668,669,669,670,671,671,672,673,674,674,675,675,675,676,676,677,677,678,679,679,680,680,681,681,682,683,684,684,685,685,686,686,687,687,687,688,688,689,689,689,690,690,690,691,692,692,693,693,694,694,695,695,696,696,697,697,698,698,699,699,699,700,700,701,701,702,702,703,704,705,705,706,706,707,708,708,708,709,709,710,710,711,711,712,712,712,713,713,713,714,715,715,716,717,718,718,718,719,720,720,720,721,721,722,722,723,723,724,724,725,725,726,727,727,728,729,730,730,731,731,732,732,733,733,734,734,734,735,735,735,736,736,737,738,738,739,739,740,740,741,741,742,742,743,743,744,745,746,746,747,747,748,748,749,749,750,750,751,752,753,753,754,754,755,755,756,756,757,757,758,759,759,760,760,761,762,762,763,764,764,765,765,765,766,767,768,769,770,770,771,771,772,773,773,774,775,775,776,776,777,778,778,778,779,779,779,780,781,782,782,782,783,784,784,784,785,786,786,787,787,788,788,789,789,790,791,791,792,792,792,793,793,794,795,795,795,796,796,797,797,798,798,799,799,800,800,801,801,802,802,803,803,804,805,805,806,807,808,809,809,810,811,811,812,813,813,814,814,815,816,816,817,817,818,818,819,819,820,821,822,823,823,823,824,824,824,825,825,826,826,827,827,828,829,830,830,831,831,832,833,833,834,835,835,836,836,837,837,838,839,839,840,840,841,842,843,844,845,845,846,846,846,847,847,847,848,848,848,849,850,850,851,851,852,852,853,853,854,854,855,855,856,856,857,857,858,858,859,860,860,861,861,862,863,863,864,864,865,865,866,867,867,868,868,868,869,869,869,870,871,872,873,873,874,874,875,876,877,877,878,878,879,880,881,881,882,882,883,883,884,884,885,886,886,887,888,888,888,889,889,889,890,890,891,892,892,893,893,894,895,895,896,896,897,897,898,898,899,900,900,901,901,902,902,903,903,903,904,904,905,906,907,907,907,908,908,908,909,909,910,910,911,912,912,913,914,914,915,915,916,916,917,917,918,918,919,920,921,922,922,923,924,925,925,926,926,926,927,927,927,928,929,929,929,930,931,931,932,932,933,933,933,934,934,935,936,936,936,937,938,939,940,940,941,941,942,942,943,943,944,945,945,945,946,946,946,947,947,948,948,949,950,950,951,952,952,953,953,954,954,955,956,956,957,957,958,958,959,959,960,961,961,961,962,963,963,963,964,964,965,965,965,966,966,966,967,967,968,968,969,969,970,971,971,971,972,972,973,973,974,974,975,975,975,976,977,978,978,979,979,980,980,981,981,982,982,982,983,984,984,985,985,985,986,986,986,987,988,989,989,990,990,991,991,992,993,993,993,994,994,995,995,996,996,997,997,998,998,999,999,1000,1001,1002,1002,1003,1004,1004,1005,1005,1005,1006,1006,1006,1007,1007,1008,1008,1009,1009,1010,1010,1011,1011,1012,1012,1013,1014,1014,1015,1015,1016,1017,1017,1018,1018,1019,1020,1020,1020,1021,1021,1022,1022,1022,1023,1023,1023,1024,1024,1024,1025,1025,1025,1026,1026,1026,1027,1027,1027,1028,1028,1028,1029,1029,1029,1030,1030,1030,1031,1031,1031,1032,1032,1032,1033,1033,1033,1034,1034,1034,1035,1035,1035,1036,1036,1036,1037,1037,1037,1038,1038,1038,1039,1040,1040,1041,1042,1042,1043,1043,1044,1044,1045,1045,1046,1046,1047,1047,1048,1048,1048,1049,1049,1050,1051,1051,1052,1052,1052,1053,1053,1054,1054,1054,1055,1055,1055,1056,1056,1056,1057,1057,1058,1058,1059,1060,1060,1060,1061,1061,1062,1063,1063,1064,1064,1065,1066,1066,1066,1067,1067,1068,1068,1069,1069,1070,1071,1071,1072,1073,1074,1074,1074,1075,1075,1075,1076,1076,1076,1077,1078,1078,1079,1079,1080,1080,1081,1081,1082,1083,1083,1084,1084,1085,1085,1086,1086,1087,1088,1088,1089,1089,1090,1091,1091,1092,1092,1093,1093,1093,1094,1094,1095,1095,1095,1096,1096,1096,1097,1098,1098,1099,1099,1100,1100,1101,1101,1102,1103,1103,1104,1105,1106,1107,1107,1108,1108,1108,1109,1109,1110,1110,1111,1112,1113,1113,1114,1114,1115,1115,1116,1116,1117,1117,1118,1118,1119,1119,1119,1120,1120,1121,1121,1122,1122,1123,1124,1124,1125,1125,1126,1126,1127,1128,1128,1129,1129,1130,1130,1130,1131,1131,1131,1132,1132,1133,1133,1134,1134,1134,1135,1135,1135,1136,1136,1137,1137,1138,1138,1138,1139,1139,1140,1140,1140,1141,1141,1142,1143,1143,1143,1144,1145,1145,1146,1146,1147,1148,1148,1148,1149,1149,1149,1150,1150,1151,1151,1152,1152,1153,1154,1154,1155,1155,1156,1156,1157,1157,1158,1158,1159,1160,1161,1162,1162,1163,1163,1164,1165,1165,1166,1166,1167,1167,1167,1168,1168,1168,1169,1169,1170,1170,1171,1171,1172,1173,1173,1174,1174,1174,1175,1175,1176,1177,1178,1178,1179,1180,1180,1181,1181,1182,1183,1183,1184,1184,1184,1185,1185,1185,1186,1186,1187,1188,1188,1189,1190,1190,1191,1191,1192,1192,1193,1193,1194,1194,1195,1195,1196,1196,1197,1198,1199,1200,1200,1200,1201,1201,1201,1202,1202,1203,1204,1205,1205,1206,1206,1207,1207,1208,1208,1209,1209,1210,1210,1211,1212,1212,1213,1213,1214,1214,1215,1215,1216,1216,1216,1217,1217,1217,1218,1218,1219,1219,1220,1221,1221,1222,1222,1223,1223,1224,1225,1225,1226,1226,1227,1228,1229,1230,1230,1231,1232,1232,1232,1233,1233,1233,1234,1235,1235,1236,1237,1237,1238,1239,1240,1240,1241,1241,1242,1242,1243,1243,1244,1245,1245,1246,1246,1247,1247,1248,1249,1249,1249,1250,1250,1250,1251,1252,1253,1253,1254,1254,1255,1255,1255,1256,1256,1257,1257,1258,1258,1259,1259,1260,1260,1261,1261,1261,1262,1263,1264,1265,1265,1266,1266,1266,1267,1267,1267,1268,1268,1269,1269,1270,1270,1270,1271,1271,1271,1272,1272,1273,1273,1274,1275,1276,1276,1277,1277,1278,1278,1279,1280,1281,1281,1282,1282,1283,1283,1284,1284,1285,1285,1286,1286,1287,1287,1288,1288,1289,1289,1290,1291,1291,1292,1293,1293,1294,1294,1295,1295,1296,1296,1297,1297,1297,1298,1298,1298,1299,1299,1299,1300,1300,1301,1301,1302,1303,1303,1304,1305,1306,1306,1307,1307,1308,1308,1309,1310,1310,1311,1312,1312,1312,1313,1313,1313,1314,1314,1314,1315,1316,1316,1317,1317,1318,1319,1319,1320,1321,1321,1322,1322,1323,1323,1324,1324,1325,1325,1326,1326,1327,1327,1328,1328,1329,1330,1331,1331,1332,1332,1332,1333,1333,1334,1334,1335,1335,1335,1336,1336,1337,1338,1339,1339,1340,1340,1341,1342,1342,1343,1343,1344,1345,1345,1346,1346,1347,1348,1349,1349,1349,1350,1351,1351,1352,1352,1353,1353,1354,1354,1355,1355,1356,1356,1357,1357,1357,1358,1358,1358,1359,1360,1360,1361,1362,1362,1363,1363,1364,1364,1364,1365,1365,1366,1366,1367,1367,1367,1368,1368,1369,1370,1370,1371,1371,1372,1372,1373,1373,1373,1374,1374,1374,1375,1375,1375,1376,1376,1377,1377,1378,1379,1379,1379,1380,1381,1382,1382,1383,1383,1383,1384,1384,1385,1386,1386,1387,1387,1387,1388,1388,1388,1389,1389,1389,1390,1390,1390,1391,1391,1391,1392,1392,1392,1393,1393,1393,1394,1394,1394,1395,1395,1395,1396,1396,1396,1397,1397,1397,1398,1398,1398,1399,1399,1399,1400,1400,1400,1401,1401,1401,1402,1403,1404,1405,1405,1406,1406,1407,1407,1408,1408,1409,1410,1410,1411,1411,1412,1412,1413,1413,1414,1415,1415,1415,1416,1416,1416,1417,1418,1418,1419,1419,1420,1420,1420,1421,1421,1422,1423,1423,1424,1424,1425,1425,1425,1426,1426,1426,1427,1427,1427,1428,1428,1428,1429,1429,1429,1430,1430,1430,1431,1431,1432,1433,1433,1434,1435,1435,1436,1437,1438,1439,1440,1440,1441,1441,1441,1442,1442,1443,1443,1444,1444,1444,1445,1446,1447,1447,1448,1449,1450,1451,1452,1452,1453,1454,1454,1455,1455,1456,1456,1457,1457,1458,1458,1459,1460,1460,1461,1462,1462,1463,1463,1464,1464,1465,1466,1467,1467,1468,1468,1469,1469,1470,1470,1471,1472,1472,1473,1474,1474,1475,1476,1477,1477,1478,1479,1479,1480,1480,1481,1481,1481,1482,1482,1482,1483,1484,1484,1485,1485,1486,1486,1487,1487,1488,1488,1489,1489,1490,1490,1491,1491,1492,1492,1492,1493,1493,1494,1494,1494,1495,1495,1495,1496,1496,1497,1497,1498,1499,1499,1500,1500,1501,1501,1502,1502,1503,1504,1504,1505,1506,1506,1507,1507,1508,1508,1509,1509,1510,1510,1511,1511,1512,1512,1513,1514,1515,1515,1515,1516,1516,1517,1517,1518,1518,1519,1519,1519,1520,1520,1520,1521,1521,1522,1523,1524,1524,1525,1525,1526,1526,1527,1527,1528,1529,1529,1529,1530,1531,1531,1532,1532,1533,1533,1533,1534,1535,1535,1536,1537,1538,1538,1539,1540,1541,1541,1542,1542,1543,1543,1543,1544,1544,1544,1545,1545,1546,1547,1547,1548,1549,1550,1550,1551,1552,1552,1553,1553,1554,1554,1554,1555,1555,1555,1555,1556,1556,1556,1556,1557,1557,1558,1558,1559,1559,1560,1561,1561,1562,1562,1563,1564,1565,1565,1566,1566,1566,1567,1567,1567,1568,1568,1568,1569,1570,1570,1571,1571,1571,1572,1572,1573,1573,1574,1575,1575,1576,1576,1576,1577,1578,1578,1579,1579,1580,1580,1581,1581,1581,1582,1582,1583,1584,1584,1585,1586,1587,1587,1588,1589,1589,1590,1590,1590,1591,1591,1591,1592,1592,1592,1593,1593,1593,1594,1594,1594,1595,1595,1595,1596,1596,1596,1597,1598,1599,1599,1600,1600,1601,1601,1602,1602,1603,1603,1604,1604,1605,1605,1606,1606,1606,1607,1607,1607,1608,1608,1608,1609,1609,1609,1610,1610,1610,1611,1611,1611,1612,1612,1612,1613,1613,1613,1614,1614,1614,1615,1615,1615,1616,1616,1616,1617,1617,1617,1618,1618,1618,1619,1619,1619,1620,1620,1620,1621,1621,1621,1622,1622,1622,1623,1623,1623,1624,1624,1624,1625,1625,1625,1626,1626,1626,1627,1627,1627,1628,1628,1628,1629,1629,1629,1630,1630,1630,1631,1631,1631,1632,1632,1632,1633,1633,1633,1634,1634,1634,1635,1635,1635,1636,1636,1636,1637,1637,1637,1638,1638,1638,1639,1639,1639,1640,1640,1640,1641,1641,1641,1642,1642,1642,1643,1643,1643,1644,1644,1644,1645,1645,1645,1646,1646,1646,1647,1647,1647,1648,1648,1648,1649,1649,1649,1650,1650,1650,1651,1651,1651,1652,1652,1652,1653,1653,1653,1654,1654,1654,1655,1655,1655,1656,1656,1656,1657,1657,1657,1658,1658,1658,1659,1659,1659,1660,1660,1660,1661,1661,1661,1662,1662,1662,1663,1663,1663,1664,1664,1664,1665,1665,1665,1666,1666,1666,1667,1667,1667,1668,1668,1668,1669,1669,1669,1670,1670,1670,1671,1671,1671,1672,1672,1672,1673,1674,1674,1675,1675,1675,1676,1677,1678,1678,1679,1679,1680,1680,1681,1681,1682,1682,1683,1684,1684,1685,1685,1686,1686,1687,1687,1688,1688,1689,1689,1690,1691,1691,1691,1692,1692,1693,1693,1693,1694,1694,1695,1695,1696,1696,1697,1697,1698,1698,1698,1699,1699,1700,1700,1701,1702,1703,1703,1704,1705,1706,1707,1707,1708,1709,1709,1710,1710,1710,1711,1711,1711,1712,1712,1712,1713,1713,1714,1715,1715,1716,1716,1717,1717,1718,1719,1719,1720,1720,1721,1721,1722,1723,1723,1724,1724,1725,1726,1726,1727,1727,1728,1729,1729,1730,1730,1731,1732,1733,1734,1734,1735,1736,1737,1738,1739,1739,1740,1740,1741,1741,1742,1742,1743,1743,1744,1744,1745,1745,1746,1746,1747,1747,1748,1748,1749,1749,1750,1750,1750,1751,1751,1752,1752,1753,1753,1754,1754,1754,1755,1755,1755,1756,1756,1757,1757,1757,1758,1758,1759,1760,1761,1762,1762,1762,1763,1763,1764,1764,1765,1766,1766,1767,1767,1768,1768,1769,1770,1771,1772,1772,1773,1774,1774,1775,1775,1775,1776,1777,1778,1778,1779,1779,1780,1781,1781,1782,1782,1782,1783,1783,1784,1784,1784,1785,1786,1786,1787,1787,1788,1788,1789,1789,1790,1790,1790,1791,1791,1792,1792,1793,1793,1793,1794,1794,1795,1795,1796,1796,1797,1797,1798,1799,1799,1800,1800,1801,1801,1802,1802,1803,1804,1804,1805,1805,1806,1807,1807,1808,1808,1809,1810,1811,1811,1812,1812,1813,1813,1814,1814,1815,1815,1816,1817,1817,1818,1819,1819,1820,1820,1821,1821,1822,1822,1822,1823,1823,1823,1824,1824,1824,1825,1825,1825,1826,1826,1827,1827,1827,1828,1829,1830,1830,1831,1832,1833,1833,1834,1835,1836,1836,1836,1837,1837,1837,1838,1838,1839,1840,1840,1841,1841,1842,1842,1843,1843,1844,1844,1845,1845,1846,1846,1847,1847,1847,1848,1849,1849,1850,1850,1851,1851,1852,1853,1854,1854,1855,1856,1856,1857,1857,1857,1858,1858,1858,1859,1859,1859,1860,1860,1860,1861,1861,1861,1862,1862,1863,1863,1864,1864,1865,1865,1866,1867,1867,1868,1869,1869,1870,1870,1871,1871,1872,1872,1873,1874,1875,1876,1876,1877,1878,1878,1879,1879,1880,1881,1881,1882,1883,1884,1884,1885,1886,1887,1887,1888,1889,1890,1890,1891,1891,1892,1893,1893,1894,1894,1895,1895,1896,1896,1897,1897,1898,1898,1899,1900,1900,1901,1902,1903,1903,1904,1904,1904,1905,1905,1906,1906,1907,1908,1908,1909,1910,1910,1911,1912,1912,1913,1913,1914,1914,1915,1915,1915,1916,1916,1917,1917,1918,1919,1919,1920,1920,1921,1921,1922,1923,1923,1924,1924,1925,1926,1926,1927,1927,1928,1928,1928,1929,1929,1929,1930,1930,1930,1931,1931,1931,1932,1932,1932,1933,1933,1933,1934,1934,1934,1935,1935,1935,1936,1936,1936,1937,1937,1937,1938,1939,1940,1941,1942,1942,1943,1943,1944,1945,1946,1947,1947,1948,1949,1950,1950,1951,1952,1952,1953,1953,1954,1954,1954,1955,1955,1955,1956,1956,1957,1957,1958,1958,1959,1960,1960,1961,1961,1962,1962,1963,1963,1964,1964,1965,1965,1966,1967,1967,1968,1968,1969,1969,1969,1970,1970,1970,1971,1971,1971,1972,1972,1972,1973,1973,1974,1974,1975,1975,1976,1977,1978,1978,1979,1979,1980,1980,1981,1981,1982,1983,1984,1984,1985,1986,1986,1987,1988,1988,1989,1989,1990,1990,1991,1991,1992,1992,1993,1993,1994,1995,1995,1996,1997,1997,1998,1999,1999,2000,2000,2001,2001,2002,2003,2003,2003,2004,2004,2004,2005,2005,2005,2006,2007,2008,2008,2008,2009,2009,2010,2010,2011,2011,2012,2012,2013,2013,2014,2015,2016,2016,2017,2017,2018,2018,2019,2019,2020,2020,2021,2022,2022,2023,2023,2023,2024,2024,2024,2025,2025,2026,2027,2027,2027,2028,2029,2029,2030,2030,2030,2031,2032,2033,2033,2033,2034,2034,2035,2035,2036,2036,2037,2037,2038,2038,2039,2039,2040,2040,2041,2042,2043,2043,2044,2044,2045,2045,2046,2046,2047,2047,2048,2048,2049,2049,2050,2050,2050,2051,2051,2051,2052,2052,2053,2053,2054,2054,2055,2055,2056,2057,2057,2058,2058,2058,2059,2059,2060,2060,2061,2061,2062,2062,2063,2063,2064,2064,2065,2065,2066,2066,2067,2067,2068,2068,2069,2069,2070,2070,2071,2072,2072,2073,2073,2074,2074,2075,2075,2076,2076,2077,2077,2078,2078,2079,2079,2080,2080,2081,2081,2082,2082,2083,2083,2084,2084,2085,2085,2086,2086,2087,2087,2088,2088,2089,2089,2090,2090,2091,2091,2092,2092,2093,2093,2094,2094,2095,2095,2095,2095,2095,2095,2095,2095,2096,2096,2096,2096,2096,2096,2096,2096,2096,2096,2096,2096,2096,2096,2096,2096,2096,2096,2096,2096,2096,2096,2096,2096,2096,2096,2096,2096,2096,2096,2096,2096,2096,2096,2096,2096,2096,2096,2096,2096,2096,2096,2096,2096,2096,2097,2097,2097,2097,2097,2097,2097,2097,2098,2098,2098,2098,2098,2098,2098,2098,2099,2099,2099,2099,2099,2099,2099,2099,2100,2100,2100,2100,2100,2100,2100,2100,2101,2101,2101,2101,2101,2101,2101,2101,2102,2102,2102,2102,2102,2102,2102,2102,2103,2103,2103,2103,2103,2103,2103,2103,2104,2104,2104,2104,2104,2104,2104,2104,2105,2105,2105,2105,2105,2105,2105,2105,2106,2106,2106,2106,2106,2106,2106,2106,2107,2107,2107,2107,2107,2107,2107,2107,2108,2108,2108,2108,2108,2108,2108,2108,2109,2109,2109,2109,2109,2109,2109,2109,2110,2110,2110,2110,2110,2110,2110,2110,2111,2111,2111,2111,2111,2111,2111,2111,2112,2112,2112,2112,2112,2112,2112,2112,2113,2113,2113,2113,2113,2113,2113,2113,2114,2114,2114,2114,2114,2114,2114,2114,2115,2115,2115,2115,2115,2115,2115,2115,2116,2116,2116,2116,2116,2116,2116,2116,2117,2117,2117,2117,2117,2117,2117,2117,2118,2118,2118,2118,2118,2118,2118,2118,2119,2119,2119,2119,2119,2119,2119,2119,2120,2120,2120,2120,2120,2120,2120,2120,2121,2121,2121,2121,2121,2121,2121,2121,2122,2122,2122,2122,2122,2122,2122,2122,2123,2123,2123,2123,2123,2123,2123,2123,2124,2124,2124,2124,2124,2124,2124,2124,2125,2125,2125,2125,2125,2125,2125,2125],"depth":[1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,1,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,1,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,3,2,1,1,3,2,1,2,1,3,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,1,1,2,1,1,2,1,3,2,1,1,2,1,2,1,3,2,1,1,1,3,2,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,3,2,1,2,1,1,2,1,3,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,1,2,1,3,2,1,2,1,1,3,2,1,3,2,1,2,1,1,3,2,1,1,2,1,2,1,2,1,1,2,1,1,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,1,3,2,1,1,2,1,2,1,4,3,2,1,3,2,1,2,1,2,1,1,2,1,1,2,1,1,2,1,2,1,3,2,1,1,3,2,1,3,2,1,3,2,1,1,2,1,2,1,1,2,1,1,1,1,1,2,1,2,1,3,2,1,3,2,1,1,2,1,1,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,1,1,2,1,1,3,2,1,2,1,2,1,1,2,1,3,2,1,1,2,1,2,1,3,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,1,1,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,3,2,1,2,1,3,2,1,2,1,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,1,2,1,2,1,1,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,1,1,2,1,2,1,1,2,1,2,1,1,3,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,3,2,1,1,1,2,1,3,2,1,1,1,3,2,1,1,2,1,2,1,2,1,1,3,2,1,3,2,1,1,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,1,3,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,1,1,1,1,3,2,1,2,1,2,1,1,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,1,3,2,1,3,2,1,1,2,1,2,1,3,2,1,3,2,1,1,2,1,1,2,1,1,2,1,2,1,1,1,3,2,1,3,2,1,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,1,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,3,2,1,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,1,2,1,2,1,1,3,2,1,2,1,2,1,2,1,3,2,1,3,2,1,1,2,1,1,1,3,2,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,1,2,1,3,2,1,1,1,1,1,2,1,2,1,1,2,1,1,2,1,2,1,1,3,2,1,3,2,1,1,1,3,2,1,1,3,2,1,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,1,1,2,1,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,1,1,3,2,1,3,2,1,2,1,2,1,2,1,1,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,1,1,1,1,2,1,3,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,3,2,1,3,2,1,1,1,1,2,1,2,1,1,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,1,2,1,1,3,2,1,3,2,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,2,1,1,1,3,2,1,3,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,1,1,2,1,1,1,2,1,3,2,1,3,2,1,1,3,2,1,1,2,1,2,1,3,2,1,2,1,1,3,2,1,1,1,1,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,3,2,1,1,3,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,2,1,3,2,1,1,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,3,2,1,3,2,1,1,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,1,3,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,3,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,1,3,2,1,2,1,1,2,1,2,1,1,3,2,1,2,1,2,1,2,1,1,2,1,1,1,3,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,1,2,1,1,1,1,2,1,3,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,3,2,1,2,1,3,2,1,2,1,1,3,2,1,1,2,1,2,1,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,1,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,3,2,1,2,1,1,1,2,1,1,2,1,2,1,1,2,1,3,2,1,3,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,1,3,2,1,3,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,1,1,1,2,1,1,3,2,1,3,2,1,1,2,1,1,2,1,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,3,2,1,3,2,1,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,1,1,2,1,3,2,1,3,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,1,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,1,1,2,1,2,1,2,1,1,2,1,1,3,2,1,3,2,1,3,2,1,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,3,2,1,2,1,2,1,3,2,1,2,1,1,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,1,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,1,2,1,1,2,1,2,1,3,2,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,1,3,2,1,1,1,2,1,3,2,1,2,1,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,1,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,1,2,1,1,2,1,1,1,1,1,2,1,3,2,1,2,1,2,1,3,2,1,1,1,2,1,1,1,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,1,1,2,1,1,2,1,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,3,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,1,1,2,1,2,1,2,1,2,1,1,3,2,1,1,2,1,2,1,3,2,1,1,2,1,1,1,2,1,1,1,2,1,2,1,3,2,1,3,2,1,2,1,1,2,1,1,1,2,1,1,2,1,2,1,3,2,1,4,3,2,1,4,3,2,1,2,1,2,1,2,1,1,2,1,2,1,1,1,2,1,3,2,1,3,2,1,3,2,1,1,2,1,3,2,1,2,1,2,1,1,2,1,3,2,1,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,1,1,2,1,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,1,2,1,3,2,1,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,1,2,1,1,1,1,2,1,1,2,1,3,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,1,1,1,2,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,3,2,1,2,1,1,1,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,1,1,1,2,1,1,2,1,3,2,1,1,1,2,1,2,1,1,2,1,3,2,1,2,1,3,2,1,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,3,2,1,1,1,2,1,1,1,2,1,1,1,3,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,1,1,2,1,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,1,1,1,2,1,1,2,1,2,1,1,2,1,1,1,2,1,1,1,2,1,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,1,2,1,3,2,1,2,1,2,1,1,2,1,1,2,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,1,1,1,1,2,1,2,1,1,1,1,2,1,1,1,2,1,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,1,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,1,2,1,2,1,2,1,1,3,2,1,3,2,1,3,2,1,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,3,2,1,2,1,1,3,2,1,1,2,1,3,2,1,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,8,7,6,5,4,3,2,1,45,44,43,42,41,40,39,38,37,36,35,34,33,32,31,30,29,28,27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1],"label":["rowSums","rowSums","rowSums","rowSums","rowSums","rowSums","rowMeans","rowMeans","rowMeans","rowMeans","rowMeans","rowMeans","rowMeans","rowMeans","aperm.default","apply","aperm.default","apply","aperm.default","apply","aperm.default","apply","aperm.default","apply","aperm.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","apply","FUN","apply","apply","mean.default","apply","FUN","apply","apply","apply","FUN","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","<GC>","apply","<GC>","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","<GC>","apply","<GC>","apply","FUN","apply","apply","mean.default","apply","FUN","apply","apply","is.numeric","local","FUN","apply","apply","apply","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","isTRUE","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","<GC>","is.numeric","local","FUN","apply","mean.default","apply","FUN","apply","apply","is.na","local","isTRUE","mean.default","apply","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","apply","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","apply","mean.default","apply","<GC>","apply","isTRUE","mean.default","apply","apply","apply","isTRUE","mean.default","apply","length","local","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","<GC>","apply","mean.default","apply","FUN","apply","mean.default","apply","length","local","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","apply","isTRUE","mean.default","apply","FUN","apply","apply","mean.default","apply","<GC>","FUN","apply","mean.default","apply","mean.default","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","apply","FUN","apply","<GC>","apply","<GC>","apply","mean.default","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","is.numeric","local","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","apply","isTRUE","mean.default","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","length","local","apply","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","apply","is.numeric","local","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","length","local","is.na","local","FUN","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","<GC>","apply","mean.default","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","isTRUE","mean.default","apply","apply","mean.default","apply","FUN","apply","<GC>","isTRUE","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","apply","length","local","apply","FUN","apply","apply","mean.default","apply","is.numeric","local","isTRUE","mean.default","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","apply","mean.default","apply","apply","apply","apply","apply","mean.default","apply","mean.default","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","apply","is.numeric","local","<GC>","apply","FUN","apply","length","local","FUN","apply","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","apply","apply","mean.default","apply","<GC>","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","is.numeric","local","FUN","apply","apply","apply","mean.default","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","length","local","FUN","apply","apply","mean.default","apply","mean.default","apply","mean.default","apply","apply","apply","FUN","apply","apply","<GC>","is.na","local","FUN","apply","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","isTRUE","mean.default","apply","mean.default","apply","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","apply","<GC>","apply","mean.default","apply","apply","isTRUE","mean.default","apply","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","is.numeric","local","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","FUN","apply","apply","mean.default","apply","FUN","apply","<GC>","apply","<GC>","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","<GC>","mean.default","apply","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","FUN","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","is.numeric","local","apply","FUN","apply","mean.default","apply","FUN","apply","is.numeric","local","mean.default","apply","FUN","apply","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","is.numeric","local","mean.default","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","<GC>","apply","length","local","isTRUE","mean.default","apply","length","local","length","local","FUN","apply","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","length","local","mean.default","apply","mean.default","apply","apply","<GC>","apply","is.numeric","local","mean.default","apply","apply","FUN","apply","FUN","apply","apply","apply","is.numeric","local","mean.default","apply","<GC>","apply","FUN","apply","mean.default","apply","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","<GC>","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","apply","apply","mean.default","apply","is.na","local","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","mean.default","apply","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","is.na","local","isTRUE","mean.default","apply","apply","mean.default","apply","<GC>","apply","isTRUE","mean.default","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","apply","<GC>","apply","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","<GC>","FUN","apply","apply","apply","isTRUE","mean.default","apply","apply","FUN","apply","mean.default","apply","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","apply","FUN","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","length","local","is.na","local","apply","FUN","apply","<GC>","apply","<GC>","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","is.numeric","local","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","isTRUE","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","mean.default","apply","apply","is.na","local","<GC>","apply","<GC>","apply","mean.default","apply","apply","apply","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","FUN","apply","apply","mean.default","apply","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","is.na","local","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","apply","<GC>","apply","<GC>","apply","FUN","apply","isTRUE","mean.default","apply","apply","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","<GC>","apply","<GC>","apply","FUN","apply","apply","FUN","apply","apply","apply","is.numeric","local","isTRUE","mean.default","apply","FUN","apply","length","local","apply","FUN","apply","mean.default","apply","FUN","apply","apply","apply","FUN","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","length","local","<GC>","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","is.na","local","FUN","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","apply","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","mean.default","apply","apply","apply","isTRUE","mean.default","apply","apply","isTRUE","mean.default","apply","mean.default","apply","is.numeric","local","FUN","apply","is.na","local","mean.default","apply","apply","mean.default","apply","apply","apply","FUN","apply","mean.default","apply","length","local","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","<GC>","apply","<GC>","apply","apply","mean.default","apply","FUN","apply","apply","FUN","apply","apply","mean.default","apply","isTRUE","mean.default","apply","apply","apply","apply","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","apply","isTRUE","mean.default","apply","apply","isTRUE","mean.default","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","apply","<GC>","apply","mean.default","apply","FUN","apply","length","local","apply","FUN","apply","apply","apply","apply","mean.default","apply","apply","mean.default","apply","apply","FUN","apply","length","local","apply","mean.default","apply","FUN","apply","is.na","local","mean.default","apply","apply","apply","apply","<GC>","length","local","<GC>","length","local","length","local","FUN","apply","mean.default","apply","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","mean.default","apply","apply","apply","apply","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","FUN","apply","is.na","local","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","length","local","apply","FUN","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","is.numeric","local","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","apply","apply","mean.default","apply","FUN","apply","apply","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","is.na","local","apply","<GC>","FUN","apply","<GC>","FUN","apply","is.na","local","apply","FUN","apply","FUN","apply","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","apply","mean.default","apply","apply","apply","mean.default","apply","<GC>","length","local","<GC>","length","local","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","is.numeric","local","apply","isTRUE","mean.default","apply","apply","apply","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","apply","FUN","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","apply","apply","length","local","FUN","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","apply","FUN","apply","FUN","apply","length","local","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","apply","apply","mean.default","apply","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","length","local","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","is.na","local","mean.default","apply","apply","isTRUE","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","apply","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","is.numeric","local","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","apply","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","apply","is.na","local","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","is.numeric","local","FUN","apply","length","local","FUN","apply","apply","FUN","apply","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","apply","apply","<GC>","apply","<GC>","apply","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","length","local","mean.default","apply","apply","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","length","local","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","length","local","isTRUE","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","FUN","apply","mean.default","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","is.numeric","local","apply","apply","apply","FUN","apply","mean.default","apply","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","FUN","apply","is.numeric","local","apply","is.na","local","isTRUE","mean.default","apply","mean.default","apply","apply","apply","FUN","apply","apply","FUN","apply","mean.default","apply","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","apply","FUN","apply","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","apply","is.na","local","FUN","apply","is.numeric","local","FUN","apply","FUN","apply","mean.default","apply","apply","length","local","is.numeric","local","mean.default","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","FUN","apply","FUN","apply","apply","mean.default","apply","FUN","apply","apply","apply","apply","FUN","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","length","local","apply","FUN","apply","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","apply","length","local","mean.default","apply","mean.default","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","length","local","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","is.na","local","apply","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","<GC>","apply","<GC>","apply","is.numeric","local","mean.default","apply","mean.default","apply","is.numeric","local","FUN","apply","FUN","apply","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","FUN","apply","length","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","FUN","apply","FUN","apply","apply","FUN","apply","apply","apply","is.na","local","mean.default","apply","FUN","apply","apply","mean.default","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","is.na","local","FUN","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","mean.default","apply","is.numeric","local","FUN","apply","mean.default","apply","<GC>","apply","<GC>","apply","apply","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","is.numeric","local","isTRUE","mean.default","apply","length","local","apply","apply","FUN","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","apply","mean.default","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","length","local","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","mean.default","apply","apply","isTRUE","mean.default","apply","apply","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","apply","apply","mean.default","apply","is.na","local","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","is.numeric","local","isTRUE","mean.default","apply","mean.default","apply","apply","FUN","apply","length","local","isTRUE","mean.default","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","FUN","apply","apply","FUN","apply","apply","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","apply","<GC>","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","apply","apply","apply","apply","mean.default","apply","apply","mean.default","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","FUN","apply","apply","apply","FUN","apply","<GC>","apply","<GC>","apply","mean.default","apply","apply","FUN","apply","apply","is.numeric","local","apply","apply","FUN","apply","apply","is.na","local","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","is.numeric","local","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","length","local","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","apply","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","<GC>","apply","<GC>","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","apply","is.na","local","apply","apply","FUN","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","apply","FUN","apply","apply","apply","FUN","apply","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","apply","mean.default","apply","isTRUE","mean.default","apply","apply","<GC>","apply","<GC>","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","mean.default","apply","apply","apply","FUN","apply","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","length","local","FUN","apply","mean.default","apply","apply","isTRUE","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","apply","apply","apply","mean.default","apply","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","FUN","apply","apply","FUN","apply","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","FUN","apply","apply","apply","apply","FUN","apply","apply","apply","apply","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","is.numeric","local","FUN","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","apply","length","local","FUN","apply","FUN","apply","apply","apply","apply","FUN","apply","apply","mean.default","apply","isTRUE","mean.default","apply","apply","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","<GC>","apply","<GC>","apply","<GC>","apply","isTRUE","mean.default","apply","FUN","apply","is.numeric","local","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","apply","FUN","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","apply","apply","FUN","apply","length","local","FUN","apply","FUN","apply","FUN","apply","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","apply","apply","mean.default","apply","apply","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","mean.default","apply","FUN","apply","FUN","apply","length","local","FUN","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","apply","mean.default","apply","is.na","local","mean.default","apply","apply","apply","mean.default","apply","apply","mean.default","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","apply","apply","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","apply","FUN","apply","apply","apply","mean.default","apply","apply","apply","FUN","apply","apply","apply","FUN","apply","mean.default","apply","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","mean.default","apply","apply","FUN","apply","apply","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","apply","FUN","apply","apply","mean.default","apply","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","apply","apply","apply","FUN","apply","is.na","local","apply","apply","apply","FUN","apply","apply","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","is.numeric","local","FUN","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","apply","apply","FUN","apply","apply","mean.default","apply","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","mean.default","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","apply","apply","is.numeric","local","is.na","local","mean.default","apply","FUN","apply","is.numeric","local","apply","mean.default","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","is.na","local","<GC>","apply","<GC>","apply","<GC>","apply","apply","apply","length","local","FUN","apply","length","local","length","local","length","local","FUN","apply","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","length","local","length","local","mean.default","apply","apply","FUN","apply","isTRUE","mean.default","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","findVar","cmpSym","cmp","cmpIndices","cmpSubsetDispatch","h","tryInline","cmpCall","cmp","cmpPrim2","h","tryInline","cmpCall","cmp","cmpPrim2","h","tryInline","cmpCall","cmp","h","tryInline","cmpCall","cmp","cmpPrim2","h","tryInline","cmpCall","cmp","cmpComplexAssign","h","tryInline","cmpCall","cmp","h","tryInline","cmpCall","cmp","cmpForBody","h","tryInline","cmpCall","cmp","genCode","compile","compiler:::tryCompile","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis"],"filenum":[1,1,1,1,1,1,1,1,1,1,1,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,1,null,1,null,1,1,1,null,1,null,1,1,null,1,null,1,null,1,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,1,null,null,null,1,1,1,1,null,1,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,null,1,null,null,1,1,null,null,1,null,1,null,null,1,null,1,null,1,null,null,null,null,1,null,1,null,1,1,null,null,null,null,1,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,1,null,1,1,null,1,1,1,null,1,1,null,1,null,null,1,1,null,1,null,1,null,null,1,1,1,null,null,1,null,null,null,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,null,1,null,null,1,null,1,1,null,null,1,null,1,1,null,1,null,null,1,null,1,null,1,1,1,null,1,null,1,null,1,null,1,null,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,1,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,1,null,null,1,1,null,1,null,1,null,1,1,null,null,1,1,null,1,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,null,null,null,null,1,null,1,null,1,null,1,null,null,1,1,null,1,null,1,1,null,1,1,null,1,null,1,null,1,null,1,1,null,null,1,1,null,1,null,1,null,null,null,1,null,null,1,null,1,null,1,1,null,null,1,null,1,1,null,1,null,null,null,null,1,1,null,null,1,null,null,1,null,null,1,1,null,1,null,1,1,null,1,1,1,1,1,null,1,null,1,null,null,1,null,null,1,1,null,1,1,1,null,1,null,1,null,1,null,null,1,null,1,1,null,null,null,1,null,1,null,null,null,1,1,null,1,1,null,1,null,1,1,1,null,1,null,1,1,null,1,null,1,null,1,null,null,null,1,1,1,null,1,null,1,null,null,1,null,null,1,null,null,null,1,1,null,1,null,1,null,1,1,1,null,1,1,null,null,null,null,1,null,1,1,null,1,null,null,1,1,null,1,null,1,null,null,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,1,null,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,null,1,1,1,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,1,null,1,1,null,1,null,null,1,null,1,null,null,1,null,1,null,1,null,null,1,null,null,null,1,null,1,null,1,null,1,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,1,1,null,1,null,1,1,null,1,null,null,1,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,null,null,1,null,1,1,null,null,1,null,1,null,1,null,null,null,1,1,null,1,null,1,null,1,1,null,1,null,1,null,null,null,null,1,null,null,null,null,null,1,1,null,1,null,1,null,null,1,null,null,1,null,1,1,null,null,1,null,1,null,1,null,null,null,1,null,1,1,null,1,null,null,null,1,1,null,1,null,1,1,1,null,null,null,1,null,1,null,1,null,1,1,null,1,null,null,1,null,1,null,1,null,1,1,null,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,1,1,null,1,null,null,null,null,1,null,null,1,null,1,null,1,1,1,null,1,null,1,1,null,1,null,1,1,null,null,1,null,null,1,null,1,1,null,1,null,1,null,1,null,null,null,null,1,1,null,1,null,1,null,null,1,1,null,1,null,1,null,1,1,null,1,null,null,1,null,1,null,1,null,1,1,null,1,null,1,null,null,1,null,1,null,null,1,1,1,null,1,null,null,1,1,1,null,null,1,1,null,1,null,1,null,1,1,null,null,1,null,null,1,1,1,null,1,null,1,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,null,null,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,null,1,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,1,null,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,1,null,1,null,1,1,null,null,null,1,null,1,null,1,1,1,1,1,1,null,null,1,null,1,null,1,1,1,null,1,null,1,null,1,1,null,1,1,null,1,null,1,1,null,null,1,null,null,1,1,null,1,null,1,null,null,1,null,null,1,1,null,null,1,null,1,1,null,1,null,1,1,1,null,null,1,null,null,1,1,null,1,null,1,null,null,1,1,null,1,null,1,null,1,null,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,1,null,1,1,1,null,null,null,null,1,null,1,null,null,1,null,1,null,1,null,1,1,1,null,1,null,1,null,1,null,null,1,null,null,null,null,1,null,null,1,1,null,1,null,1,null,1,null,1,null,null,null,1,null,1,null,null,1,null,1,null,1,null,1,1,1,null,1,null,1,1,null,null,1,null,1,null,1,null,1,null,null,1,null,null,1,1,null,1,1,1,null,null,1,1,null,null,1,null,1,null,null,null,1,null,null,null,1,1,null,1,1,1,null,1,null,1,null,null,null,1,null,null,1,null,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,1,1,null,1,null,1,null,1,null,1,null,1,1,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,1,null,1,1,null,1,null,null,1,1,1,1,1,null,1,null,1,1,null,1,1,null,1,null,1,1,null,null,1,null,null,1,1,1,null,null,1,1,null,null,1,1,null,1,null,1,null,1,null,1,1,null,1,null,null,1,null,1,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,1,1,1,null,1,1,null,1,1,null,1,null,null,1,null,1,null,1,null,null,null,1,1,1,1,null,null,null,null,null,null,null,null,null,1,null,1,1,1,null,1,null,1,1,null,1,1,null,1,null,1,null,1,1,null,1,null,1,1,1,1,1,null,1,null,null,1,null,null,1,null,null,1,1,null,1,null,null,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,1,null,1,null,1,null,1,1,null,null,null,null,1,null,null,1,1,1,1,null,1,null,1,1,1,null,1,null,1,1,1,null,1,null,1,null,1,null,1,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,null,1,null,1,1,1,null,null,1,null,null,1,null,1,null,1,1,null,1,1,null,1,null,1,null,1,null,1,null,1,1,1,1,null,1,1,1,null,1,null,null,null,null,null,null,1,null,null,1,1,null,1,null,1,null,null,1,null,null,1,null,null,1,1,1,1,null,1,null,1,null,1,null,1,1,null,null,1,null,null,1,null,1,null,1,1,null,1,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,1,null,null,1,1,null,null,1,null,1,null,null,1,null,null,1,null,1,null,1,null,1,1,null,null,1,null,1,null,1,null,1,null,null,1,1,1,null,null,null,1,null,1,null,1,null,null,1,1,null,1,null,null,1,null,null,1,1,1,null,1,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,1,null,1,1,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,null,null,1,null,1,1,null,1,null,1,1,null,null,null,1,1,null,null,1,null,1,null,null,1,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,1,null,1,1,null,1,null,1,null,1,null,1,null,null,null,1,null,null,1,null,1,1,null,1,null,null,1,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,1,null,null,1,null,1,1,null,1,null,1,1,null,null,1,null,1,null,1,null,1,1,null,null,1,1,null,null,1,null,null,1,null,null,1,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,1,null,1,null,1,1,null,1,null,1,null,null,1,null,1,null,null,1,null,null,1,1,null,null,null,1,null,null,null,1,1,null,1,1,1,1,null,1,null,null,1,null,1,null,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,null,null,1,1,null,1,null,1,null,1,1,null,1,null,null,null,null,1,null,null,1,null,1,null,null,null,null,1,null,null,1,null,1,null,1,null,null,1,null,1,null,null,1,null,1,1,null,null,1,1,null,1,null,1,1,null,null,1,null,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,null,1,1,1,null,1,null,1,1,null,1,null,1,null,null,1,null,null,1,null,1,null,1,null,null,1,null,null,null,null,1,null,1,1,1,null,1,1,null,1,null,1,1,null,1,null,null,1,null,null,1,null,1,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,1,1,null,null,1,null,null,1,null,1,1,1,null,null,null,1,null,null,null,1,null,1,null,1,1,null,null,null,null,null,1,null,1,null,null,1,null,null,1,null,1,null,1,1,null,1,null,1,null,1,1,null,1,null,1,1,1,1,null,1,1,null,null,1,null,null,1,1,null,null,1,null,1,1,1,null,1,null,1,null,1,null,1,1,null,null,null,1,null,1,1,null,null,1,null,null,1,1,1,null,1,null,1,null,null,1,null,1,null,1,null,null,null,1,null,1,null,null,1,1,1,1,null,1,null,null,1,null,null,1,null,1,null,1,null,null,1,null,null,1,null,1,null,null,1,1,null,1,null,1,null,1,1,1,null,1,null,1,null,1,null,null,null,1,null,1,null,null,null,1,null,1,1,null,1,1,null,1,null,1,null,1,null,null,null,null,null,null,null,null,null,null,null,null,1,null,1,1,null,1,1,1,null,null,null,1,null,1,1,null,1,1,null,null,1,null,null,1,null,null,1,1,null,null,null,1,1,null,1,1,null,1,null,1,null,1,null,null,null,1,null,1,null,1,null,1,1,1,null,1,null,null,1,null,1,null,null,null,null,1,null,null,1,1,null,1,null,1,1,null,1,null,1,1,null,1,null,1,1,1,null,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,1,null,1,1,null,1,null,1,null,null,1,null,1,null,null,null,null,1,null,1,1,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,1,null,null,1,1,1,null,1,null,null,1,null,1,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,1,1,1,null,1,null,null,null,1,null,1,1,null,1,null,1,null,1,null,1,1,null,null,1,null,null,1,1,null,1,null,null,null,null,1,null,1,1,null,1,null,null,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,1,null,1,1,null,1,1,1,1,1,null,1,null,null,1,null,1,null,1,null,null,1,1,1,null,1,1,1,1,1,null,1,1,null,1,null,1,null,1,null,1,null,1,1,null,1,1,null,1,null,1,null,1,1,1,null,1,null,1,null,1,null,1,1,null,1,1,null,null,1,1,null,1,1,null,null,null,1,null,null,1,null,null,1,1,null,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,null,1,null,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,1,null,null,1,null,1,null,null,null,1,null,null,1,null,null,1,null,1,1,1,null,1,null,1,null,1,null,1,1,null,null,1,1,null,1,null,1,null,null,1,1,null,1,1,1,null,null,1,1,null,1,null,1,null,null,1,null,null,1,null,1,1,null,1,1,1,null,1,1,null,1,null,1,null,null,1,null,null,null,1,null,null,null,1,null,1,null,1,null,1,1,null,1,null,1,1,1,null,1,null,null,1,null,null,1,null,null,1,1,null,1,null,null,1,null,1,null,1,1,null,1,null,null,1,1,null,1,null,1,null,1,null,null,1,null,1,1,null,1,1,1,null,1,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,1,null,1,null,null,1,1,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,null,null,1,null,1,1,null,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,1,1,null,1,1,1,1,null,1,1,null,1,null,null,1,null,null,1,null,null,1,null,1,1,null,1,null,1,null,1,1,null,1,null,1,null,1,1,null,1,null,1,1,null,1,null,1,1,null,1,null,1,1,1,1,null,1,1,1,1,1,null,1,null,1,null,1,null,1,null,1,null,null,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,1,null,null,1,null,1,1,1,1,null,null,1,null,1,null,1,1,null,null,null,1,null,1,1,1,1,null,1,1,null,1,null,null,1,1,1,null,1,null,1,1,null,1,null,null,1,null,1,null,null,1,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,null,null,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,1,null,1,null,1,1,null,1,null,1,1,1,null,1,null,null,null,1,null,1,null,1,1,null,1,1,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,null,null,1,1,1,null,1,1,1,null,1,1,1,null,null,1,null,null,1,null,1,1,null,1,null,1,null,1,null,null,null,1,null,1,null,1,null,null,1,1,null,1,null,null,null,1,1,1,null,1,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,1,null,1,1,null,1,null,1,null,1,null,1,1,1,1,null,1,1,null,1,null,1,1,null,1,1,1,null,1,1,1,null,1,1,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,1,1,null,1,null,null,1,null,1,null,1,1,null,1,1,null,1,1,null,1,null,1,null,1,null,null,1,null,1,null,1,1,null,1,null,1,null,1,1,null,1,null,1,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,1,1,1,1,null,1,null,null,1,1,1,null,1,1,1,null,1,1,null,1,null,1,null,null,1,null,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,null,null,null,1,1,1,null,1,null,1,null,1,null,1,1,1,null,1,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,1,null,1,1,null,1,null,1,null,1,1,null,null,1,null,null,1,null,null,1,1,1,null,null,1,null,1,null,1,null,1,null,1,null,1,1,1,null,null,null,null,null,1,null,1,null,null,1,null,1,null,null,1,null,null,1,null,1,1,null,null,1,1,null,1,null,null,1,1,1,null,null,1,null,1,null,1,null,1,null,null,null,1,null,1,null,1,1,1,null,null,null,1,null,null,null,null,null,null,null,1,null,1,null,null,1,null,null,1,null,1,null,null,null,null,null,1,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,1,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null],"linenum":[10,10,10,10,10,10,11,11,11,11,11,11,11,11,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,12,null,12,null,12,12,12,null,12,null,12,12,null,12,null,12,null,12,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,12,null,null,null,12,12,12,12,null,12,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,null,12,null,null,12,12,null,null,12,null,12,null,null,12,null,12,null,12,null,null,null,null,12,null,12,null,12,12,null,null,null,null,12,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,12,null,12,12,null,12,12,12,null,12,12,null,12,null,null,12,12,null,12,null,12,null,null,12,12,12,null,null,12,null,null,null,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,null,12,null,null,12,null,12,12,null,null,12,null,12,12,null,12,null,null,12,null,12,null,12,12,12,null,12,null,12,null,12,null,12,null,12,12,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,12,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,12,null,null,12,12,null,12,null,12,null,12,12,null,null,12,12,null,12,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,null,null,null,null,12,null,12,null,12,null,12,null,null,12,12,null,12,null,12,12,null,12,12,null,12,null,12,null,12,null,12,12,null,null,12,12,null,12,null,12,null,null,null,12,null,null,12,null,12,null,12,12,null,null,12,null,12,12,null,12,null,null,null,null,12,12,null,null,12,null,null,12,null,null,12,12,null,12,null,12,12,null,12,12,12,12,12,null,12,null,12,null,null,12,null,null,12,12,null,12,12,12,null,12,null,12,null,12,null,null,12,null,12,12,null,null,null,12,null,12,null,null,null,12,12,null,12,12,null,12,null,12,12,12,null,12,null,12,12,null,12,null,12,null,12,null,null,null,12,12,12,null,12,null,12,null,null,12,null,null,12,null,null,null,12,12,null,12,null,12,null,12,12,12,null,12,12,null,null,null,null,12,null,12,12,null,12,null,null,12,12,null,12,null,12,null,null,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,12,null,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,null,12,12,12,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,12,null,12,12,null,12,null,null,12,null,12,null,null,12,null,12,null,12,null,null,12,null,null,null,12,null,12,null,12,null,12,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,12,12,null,12,null,12,12,null,12,null,null,12,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,null,null,12,null,12,12,null,null,12,null,12,null,12,null,null,null,12,12,null,12,null,12,null,12,12,null,12,null,12,null,null,null,null,12,null,null,null,null,null,12,12,null,12,null,12,null,null,12,null,null,12,null,12,12,null,null,12,null,12,null,12,null,null,null,12,null,12,12,null,12,null,null,null,12,12,null,12,null,12,12,12,null,null,null,12,null,12,null,12,null,12,12,null,12,null,null,12,null,12,null,12,null,12,12,null,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,12,12,null,12,null,null,null,null,12,null,null,12,null,12,null,12,12,12,null,12,null,12,12,null,12,null,12,12,null,null,12,null,null,12,null,12,12,null,12,null,12,null,12,null,null,null,null,12,12,null,12,null,12,null,null,12,12,null,12,null,12,null,12,12,null,12,null,null,12,null,12,null,12,null,12,12,null,12,null,12,null,null,12,null,12,null,null,12,12,12,null,12,null,null,12,12,12,null,null,12,12,null,12,null,12,null,12,12,null,null,12,null,null,12,12,12,null,12,null,12,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,null,null,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,null,12,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,12,null,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,12,null,12,null,12,12,null,null,null,12,null,12,null,12,12,12,12,12,12,null,null,12,null,12,null,12,12,12,null,12,null,12,null,12,12,null,12,12,null,12,null,12,12,null,null,12,null,null,12,12,null,12,null,12,null,null,12,null,null,12,12,null,null,12,null,12,12,null,12,null,12,12,12,null,null,12,null,null,12,12,null,12,null,12,null,null,12,12,null,12,null,12,null,12,null,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,12,null,12,12,12,null,null,null,null,12,null,12,null,null,12,null,12,null,12,null,12,12,12,null,12,null,12,null,12,null,null,12,null,null,null,null,12,null,null,12,12,null,12,null,12,null,12,null,12,null,null,null,12,null,12,null,null,12,null,12,null,12,null,12,12,12,null,12,null,12,12,null,null,12,null,12,null,12,null,12,null,null,12,null,null,12,12,null,12,12,12,null,null,12,12,null,null,12,null,12,null,null,null,12,null,null,null,12,12,null,12,12,12,null,12,null,12,null,null,null,12,null,null,12,null,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,12,12,null,12,null,12,null,12,null,12,null,12,12,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,12,null,12,12,null,12,null,null,12,12,12,12,12,null,12,null,12,12,null,12,12,null,12,null,12,12,null,null,12,null,null,12,12,12,null,null,12,12,null,null,12,12,null,12,null,12,null,12,null,12,12,null,12,null,null,12,null,12,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,12,12,12,null,12,12,null,12,12,null,12,null,null,12,null,12,null,12,null,null,null,12,12,12,12,null,null,null,null,null,null,null,null,null,12,null,12,12,12,null,12,null,12,12,null,12,12,null,12,null,12,null,12,12,null,12,null,12,12,12,12,12,null,12,null,null,12,null,null,12,null,null,12,12,null,12,null,null,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,12,null,12,null,12,null,12,12,null,null,null,null,12,null,null,12,12,12,12,null,12,null,12,12,12,null,12,null,12,12,12,null,12,null,12,null,12,null,12,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,null,12,null,12,12,12,null,null,12,null,null,12,null,12,null,12,12,null,12,12,null,12,null,12,null,12,null,12,null,12,12,12,12,null,12,12,12,null,12,null,null,null,null,null,null,12,null,null,12,12,null,12,null,12,null,null,12,null,null,12,null,null,12,12,12,12,null,12,null,12,null,12,null,12,12,null,null,12,null,null,12,null,12,null,12,12,null,12,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,12,null,null,12,12,null,null,12,null,12,null,null,12,null,null,12,null,12,null,12,null,12,12,null,null,12,null,12,null,12,null,12,null,null,12,12,12,null,null,null,12,null,12,null,12,null,null,12,12,null,12,null,null,12,null,null,12,12,12,null,12,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,12,null,12,12,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,null,null,12,null,12,12,null,12,null,12,12,null,null,null,12,12,null,null,12,null,12,null,null,12,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,12,null,12,12,null,12,null,12,null,12,null,12,null,null,null,12,null,null,12,null,12,12,null,12,null,null,12,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,12,null,null,12,null,12,12,null,12,null,12,12,null,null,12,null,12,null,12,null,12,12,null,null,12,12,null,null,12,null,null,12,null,null,12,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,12,null,12,null,12,12,null,12,null,12,null,null,12,null,12,null,null,12,null,null,12,12,null,null,null,12,null,null,null,12,12,null,12,12,12,12,null,12,null,null,12,null,12,null,12,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,null,null,12,12,null,12,null,12,null,12,12,null,12,null,null,null,null,12,null,null,12,null,12,null,null,null,null,12,null,null,12,null,12,null,12,null,null,12,null,12,null,null,12,null,12,12,null,null,12,12,null,12,null,12,12,null,null,12,null,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,null,12,12,12,null,12,null,12,12,null,12,null,12,null,null,12,null,null,12,null,12,null,12,null,null,12,null,null,null,null,12,null,12,12,12,null,12,12,null,12,null,12,12,null,12,null,null,12,null,null,12,null,12,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,12,12,null,null,12,null,null,12,null,12,12,12,null,null,null,12,null,null,null,12,null,12,null,12,12,null,null,null,null,null,12,null,12,null,null,12,null,null,12,null,12,null,12,12,null,12,null,12,null,12,12,null,12,null,12,12,12,12,null,12,12,null,null,12,null,null,12,12,null,null,12,null,12,12,12,null,12,null,12,null,12,null,12,12,null,null,null,12,null,12,12,null,null,12,null,null,12,12,12,null,12,null,12,null,null,12,null,12,null,12,null,null,null,12,null,12,null,null,12,12,12,12,null,12,null,null,12,null,null,12,null,12,null,12,null,null,12,null,null,12,null,12,null,null,12,12,null,12,null,12,null,12,12,12,null,12,null,12,null,12,null,null,null,12,null,12,null,null,null,12,null,12,12,null,12,12,null,12,null,12,null,12,null,null,null,null,null,null,null,null,null,null,null,null,12,null,12,12,null,12,12,12,null,null,null,12,null,12,12,null,12,12,null,null,12,null,null,12,null,null,12,12,null,null,null,12,12,null,12,12,null,12,null,12,null,12,null,null,null,12,null,12,null,12,null,12,12,12,null,12,null,null,12,null,12,null,null,null,null,12,null,null,12,12,null,12,null,12,12,null,12,null,12,12,null,12,null,12,12,12,null,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,12,null,12,12,null,12,null,12,null,null,12,null,12,null,null,null,null,12,null,12,12,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,12,null,null,12,12,12,null,12,null,null,12,null,12,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,12,12,12,null,12,null,null,null,12,null,12,12,null,12,null,12,null,12,null,12,12,null,null,12,null,null,12,12,null,12,null,null,null,null,12,null,12,12,null,12,null,null,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,12,null,12,12,null,12,12,12,12,12,null,12,null,null,12,null,12,null,12,null,null,12,12,12,null,12,12,12,12,12,null,12,12,null,12,null,12,null,12,null,12,null,12,12,null,12,12,null,12,null,12,null,12,12,12,null,12,null,12,null,12,null,12,12,null,12,12,null,null,12,12,null,12,12,null,null,null,12,null,null,12,null,null,12,12,null,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,null,12,null,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,12,null,null,12,null,12,null,null,null,12,null,null,12,null,null,12,null,12,12,12,null,12,null,12,null,12,null,12,12,null,null,12,12,null,12,null,12,null,null,12,12,null,12,12,12,null,null,12,12,null,12,null,12,null,null,12,null,null,12,null,12,12,null,12,12,12,null,12,12,null,12,null,12,null,null,12,null,null,null,12,null,null,null,12,null,12,null,12,null,12,12,null,12,null,12,12,12,null,12,null,null,12,null,null,12,null,null,12,12,null,12,null,null,12,null,12,null,12,12,null,12,null,null,12,12,null,12,null,12,null,12,null,null,12,null,12,12,null,12,12,12,null,12,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,12,null,12,null,null,12,12,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,null,null,12,null,12,12,null,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,12,12,null,12,12,12,12,null,12,12,null,12,null,null,12,null,null,12,null,null,12,null,12,12,null,12,null,12,null,12,12,null,12,null,12,null,12,12,null,12,null,12,12,null,12,null,12,12,null,12,null,12,12,12,12,null,12,12,12,12,12,null,12,null,12,null,12,null,12,null,12,null,null,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,12,null,null,12,null,12,12,12,12,null,null,12,null,12,null,12,12,null,null,null,12,null,12,12,12,12,null,12,12,null,12,null,null,12,12,12,null,12,null,12,12,null,12,null,null,12,null,12,null,null,12,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,null,null,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,12,null,12,null,12,12,null,12,null,12,12,12,null,12,null,null,null,12,null,12,null,12,12,null,12,12,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,null,null,12,12,12,null,12,12,12,null,12,12,12,null,null,12,null,null,12,null,12,12,null,12,null,12,null,12,null,null,null,12,null,12,null,12,null,null,12,12,null,12,null,null,null,12,12,12,null,12,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,12,null,12,12,null,12,null,12,null,12,null,12,12,12,12,null,12,12,null,12,null,12,12,null,12,12,12,null,12,12,12,null,12,12,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,12,12,null,12,null,null,12,null,12,null,12,12,null,12,12,null,12,12,null,12,null,12,null,12,null,null,12,null,12,null,12,12,null,12,null,12,null,12,12,null,12,null,12,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,12,12,12,12,null,12,null,null,12,12,12,null,12,12,12,null,12,12,null,12,null,12,null,null,12,null,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,null,null,null,12,12,12,null,12,null,12,null,12,null,12,12,12,null,12,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,12,null,12,12,null,12,null,12,null,12,12,null,null,12,null,null,12,null,null,12,12,12,null,null,12,null,12,null,12,null,12,null,12,null,12,12,12,null,null,null,null,null,12,null,12,null,null,12,null,12,null,null,12,null,null,12,null,12,12,null,null,12,12,null,12,null,null,12,12,12,null,null,12,null,12,null,12,null,12,null,null,null,12,null,12,null,12,12,12,null,null,null,12,null,null,null,null,null,null,null,12,null,12,null,null,12,null,null,12,null,12,null,null,null,null,null,12,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,13,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,13,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null],"memalloc":[124.5360641479492,124.5360641479492,124.5360641479492,124.5360641479492,124.5360641479492,124.5360641479492,139.8182983398438,139.8182983398438,139.8182983398438,139.8182983398438,139.8182983398438,139.8182983398438,139.8182983398438,139.8182983398438,170.2840423583984,170.2840423583984,170.2840423583984,170.2840423583984,170.2840423583984,170.2840423583984,170.2840423583984,170.2840423583984,170.2840423583984,170.2840423583984,170.2840423583984,170.2840423583984,170.2840881347656,170.2840881347656,170.2840881347656,170.2840881347656,170.2840881347656,170.2840881347656,170.2840881347656,170.2840881347656,170.2840881347656,170.2840881347656,170.2840881347656,170.2840881347656,170.2840881347656,170.2840881347656,170.2840881347656,170.2840881347656,170.2840881347656,170.2840881347656,170.2837829589844,170.2837829589844,170.2837829589844,170.2837829589844,185.7027130126953,185.8574295043945,185.8574295043945,186.0299072265625,186.196647644043,186.196647644043,186.3999862670898,186.3999862670898,186.6144866943359,186.8271636962891,187.0417022705078,187.0417022705078,187.2610626220703,187.2610626220703,187.4888153076172,187.7162322998047,187.7162322998047,187.9443893432617,187.9443893432617,188.1737594604492,188.1737594604492,188.3994827270508,188.6059646606445,188.6059646606445,188.6059646606445,188.6059646606445,185.8518371582031,185.8518371582031,185.8518371582031,186.0804672241211,186.0804672241211,186.3204040527344,186.3204040527344,186.5635604858398,186.5635604858398,186.8071212768555,186.8071212768555,187.0476837158203,187.2858734130859,187.5202407836914,187.5202407836914,187.7531356811523,187.7531356811523,187.9879302978516,187.9879302978516,188.2213134765625,188.2213134765625,188.4551773071289,188.4551773071289,188.6703796386719,188.6703796386719,188.6703796386719,188.6703796386719,186.0063095092773,186.0063095092773,186.2530288696289,186.4935836791992,186.4935836791992,186.7390289306641,186.7390289306641,186.982063293457,187.2223129272461,187.2223129272461,187.4584808349609,187.4584808349609,187.6924591064453,187.9245452880859,188.1574020385742,188.3904342651367,188.3904342651367,188.6210784912109,188.7521667480469,188.7521667480469,188.7521667480469,188.7521667480469,186.079833984375,186.079833984375,186.2875595092773,186.2875595092773,186.4778213500977,186.4778213500977,186.6903305053711,186.9232940673828,186.9232940673828,187.1617889404297,187.1617889404297,187.1617889404297,187.3951721191406,187.3951721191406,187.3951721191406,187.6256790161133,187.8793106079102,187.8793106079102,187.8793106079102,188.1095657348633,188.1095657348633,188.3415145874023,188.3415145874023,188.3415145874023,188.5734710693359,188.5734710693359,188.8044357299805,188.8044357299805,188.8326644897461,188.8326644897461,188.8326644897461,186.1863327026367,186.1863327026367,186.3872985839844,186.3872985839844,186.5969467163086,186.5969467163086,186.8234405517578,187.0537414550781,187.0537414550781,187.2897567749023,187.2897567749023,187.2897567749023,187.5240631103516,187.7547378540039,187.7547378540039,187.9872665405273,187.9872665405273,188.2185211181641,188.2185211181641,188.449821472168,188.449821472168,188.6817779541016,188.6817779541016,188.9118423461914,188.9118423461914,188.9118423461914,188.9118423461914,188.9118423461914,188.9118423461914,186.3311538696289,186.3311538696289,186.5301284790039,186.5301284790039,186.7377166748047,186.9588165283203,186.9588165283203,187.1923751831055,187.4286346435547,187.6635284423828,187.6635284423828,187.919792175293,188.1529312133789,188.1529312133789,188.384407043457,188.384407043457,188.384407043457,188.6157913208008,188.8483657836914,188.8483657836914,188.9897766113281,188.9897766113281,186.3215103149414,186.3215103149414,186.3215103149414,186.5224075317383,186.7248001098633,186.9365539550781,186.9365539550781,186.9365539550781,187.159782409668,187.159782409668,187.3903350830078,187.3903350830078,187.3903350830078,187.6265258789062,187.6265258789062,187.8611297607422,187.8611297607422,188.0946731567383,188.0946731567383,188.3285827636719,188.5586471557617,188.5586471557617,188.7926025390625,188.7926025390625,189.0263290405273,189.0263290405273,189.0663757324219,189.0663757324219,186.5303115844727,186.5303115844727,186.7317047119141,186.7317047119141,186.9347686767578,186.9347686767578,187.1499099731445,187.1499099731445,187.3759384155273,187.3759384155273,187.6036682128906,187.6036682128906,187.6036682128906,187.8400497436523,187.8400497436523,188.0758514404297,188.3099594116211,188.3099594116211,188.3099594116211,188.567008972168,188.567008972168,188.7997589111328,189.0311660766602,189.0311660766602,189.1418838500977,189.1418838500977,189.1418838500977,186.5766296386719,186.5766296386719,186.7541809082031,186.7541809082031,186.9551544189453,187.1643753051758,187.3857727050781,187.3857727050781,187.6147003173828,187.6147003173828,187.8467483520508,187.8467483520508,188.0795974731445,188.0795974731445,188.3101348876953,188.3101348876953,188.5420913696289,188.7722091674805,189.0030822753906,189.0030822753906,189.2160415649414,189.2160415649414,189.2160415649414,189.2160415649414,186.8073806762695,186.8073806762695,187.007194519043,187.007194519043,187.2084655761719,187.2084655761719,187.4210586547852,187.6425933837891,187.6425933837891,187.8663940429688,188.1001281738281,188.3341445922852,188.3341445922852,188.5686111450195,188.5686111450195,188.5686111450195,188.8026885986328,188.8026885986328,189.0605087280273,189.2890853881836,189.2890853881836,189.2890853881836,189.2890853881836,189.2890853881836,189.2890853881836,186.9143524169922,186.9143524169922,187.1165542602539,187.331298828125,187.331298828125,187.331298828125,187.5527877807617,187.7375564575195,187.7375564575195,187.9415969848633,187.9415969848633,188.1639099121094,188.1639099121094,188.3629608154297,188.5840377807617,188.5840377807617,188.7645568847656,188.9604568481445,189.1363906860352,189.1363906860352,189.3215179443359,189.3215179443359,189.3608856201172,189.3608856201172,189.3608856201172,186.9572296142578,186.9572296142578,186.9572296142578,187.1702575683594,187.1702575683594,187.3588562011719,187.3588562011719,187.5471420288086,187.5471420288086,187.7594833374023,187.7594833374023,187.958122253418,187.958122253418,188.1713104248047,188.3797912597656,188.3797912597656,188.5795288085938,188.5795288085938,188.8031539916992,189.0025787353516,189.0025787353516,189.2164459228516,189.420036315918,189.420036315918,189.420036315918,189.4315948486328,189.4315948486328,189.4315948486328,187.0774993896484,187.0774993896484,187.0774993896484,187.2587738037109,187.2587738037109,187.2587738037109,187.4491500854492,187.4491500854492,187.6361923217773,187.6361923217773,187.8202819824219,187.8202819824219,188.048583984375,188.048583984375,188.2470550537109,188.2470550537109,188.4514694213867,188.4514694213867,188.6720962524414,188.6720962524414,188.8717193603516,188.8717193603516,189.0879058837891,189.0879058837891,189.2527160644531,189.2527160644531,189.2527160644531,189.4501571655273,189.501106262207,189.501106262207,187.1314086914062,187.1314086914062,187.3209075927734,187.4918212890625,187.4918212890625,187.6604080200195,187.8485641479492,187.8485641479492,188.0247573852539,188.0247573852539,188.2399215698242,188.2399215698242,188.4441452026367,188.4441452026367,188.6438903808594,188.8665237426758,188.8665237426758,188.8665237426758,189.0542144775391,189.2568206787109,189.2568206787109,189.4715423583984,189.4715423583984,189.5694808959961,189.5694808959961,189.5694808959961,189.5694808959961,187.2194747924805,187.2194747924805,187.2194747924805,187.3952713012695,187.3952713012695,187.5802917480469,187.5802917480469,187.7585067749023,187.9389190673828,187.9389190673828,188.1490097045898,188.3507385253906,188.3507385253906,188.5633087158203,188.7757797241211,188.7757797241211,188.977912902832,188.977912902832,189.2267379760742,189.2267379760742,189.2267379760742,189.4302215576172,189.6368179321289,189.6368179321289,189.6368179321289,189.6368179321289,189.6368179321289,189.6368179321289,187.4225387573242,187.4225387573242,187.4225387573242,187.6167602539062,187.7887268066406,187.7887268066406,187.9764862060547,187.9764862060547,188.1715087890625,188.357292175293,188.357292175293,188.5744018554688,188.7646179199219,188.9638900756836,189.1798553466797,189.3917465209961,189.3917465209961,189.6223373413086,189.6223373413086,189.703010559082,189.703010559082,189.703010559082,187.4627990722656,187.4627990722656,187.4627990722656,187.6746444702148,187.8663711547852,187.8663711547852,188.0698699951172,188.2878646850586,188.5196838378906,188.5196838378906,188.6892471313477,188.6892471313477,188.8743667602539,188.8743667602539,189.0519104003906,189.0519104003906,189.0519104003906,189.2728652954102,189.2728652954102,189.483512878418,189.7141723632812,189.7141723632812,189.7681350708008,189.7681350708008,187.5779876708984,187.5779876708984,187.7673034667969,187.7673034667969,187.9636306762695,187.9636306762695,188.1651306152344,188.384635925293,188.384635925293,188.6147766113281,188.8445434570312,188.8445434570312,189.0812225341797,189.0812225341797,189.3330993652344,189.5656051635742,189.7945938110352,189.7945938110352,189.8322601318359,189.8322601318359,187.6960830688477,187.8764877319336,187.8764877319336,188.0786209106445,188.0786209106445,188.2852172851562,188.2852172851562,188.5117340087891,188.5117340087891,188.7469024658203,188.7469024658203,188.9814453125,189.2120895385742,189.4424819946289,189.4424819946289,189.6739273071289,189.6739273071289,189.8953323364258,189.8953323364258,189.8953323364258,189.8953323364258,189.8953323364258,189.8953323364258,187.847770690918,187.847770690918,188.0407638549805,188.0407638549805,188.2249069213867,188.4391174316406,188.4391174316406,188.6710891723633,188.6710891723633,188.9088821411133,188.9088821411133,189.1457061767578,189.380241394043,189.6153106689453,189.6153106689453,189.8726272583008,189.9573440551758,189.9573440551758,189.9573440551758,187.8612747192383,187.8612747192383,188.0332565307617,188.0332565307617,188.2290725708008,188.4363784790039,188.4363784790039,188.6623458862305,188.6623458862305,188.6623458862305,188.898063659668,189.1320877075195,189.1320877075195,189.3666839599609,189.3666839599609,189.5988616943359,189.5988616943359,189.5988616943359,189.8310546875,189.8310546875,190.0184173583984,190.0184173583984,190.0184173583984,190.0184173583984,190.0184173583984,190.0184173583984,190.0184173583984,190.0184173583984,190.0184173583984,190.0184173583984,190.0184173583984,190.0184173583984,190.0184173583984,190.0184173583984,190.0184173583984,190.0184173583984,190.0184173583984,190.0184173583984,190.0184173583984,190.0184173583984,190.0184173583984,190.0184173583984,190.0184173583984,190.0184173583984,190.0184173583984,190.0184173583984,190.0184173583984,190.0184173583984,190.0184173583984,190.0184173583984,190.0184173583984,190.0184173583984,190.0184173583984,188.0392532348633,188.2070770263672,188.2070770263672,188.2070770263672,188.3853530883789,188.3853530883789,188.5760803222656,188.7764892578125,188.7764892578125,188.9951324462891,188.9951324462891,189.2257080078125,189.2257080078125,189.4592666625977,189.4592666625977,189.6914749145508,189.6914749145508,189.9253311157227,189.9253311157227,190.0781021118164,190.0781021118164,190.0781021118164,190.0781021118164,188.1572494506836,188.1572494506836,188.3020629882812,188.4396057128906,188.4396057128906,188.4396057128906,188.6256408691406,188.8348083496094,189.0103912353516,189.2204360961914,189.2204360961914,189.4515380859375,189.4515380859375,189.6826400756836,189.6826400756836,189.9129028320312,189.9129028320312,190.1371841430664,190.1371841430664,190.1371841430664,190.1371841430664,190.1371841430664,190.1371841430664,188.2080993652344,188.2080993652344,188.3907318115234,188.3907318115234,188.5864562988281,188.7953796386719,188.7953796386719,189.0286178588867,189.0286178588867,189.0286178588867,189.2623443603516,189.2623443603516,189.4980087280273,189.4980087280273,189.4980087280273,189.7299652099609,189.7299652099609,189.9596786499023,189.9596786499023,190.1939468383789,190.1939468383789,190.1939468383789,190.1953659057617,190.1953659057617,190.1953659057617,188.2550506591797,188.4270401000977,188.4270401000977,188.6249771118164,188.6249771118164,188.8341217041016,188.8341217041016,189.0617828369141,189.2987823486328,189.2987823486328,189.5578765869141,189.7903442382812,189.7903442382812,190.0236892700195,190.0236892700195,190.2525634765625,190.2525634765625,190.2525634765625,190.2525634765625,188.3732833862305,188.3732833862305,188.5443572998047,188.5443572998047,188.7331924438477,188.7331924438477,188.7331924438477,188.9376220703125,188.9376220703125,189.1624526977539,189.3982925415039,189.6370468139648,189.6370468139648,189.8730621337891,189.8730621337891,190.0542221069336,190.2852554321289,190.2852554321289,190.3088302612305,190.3088302612305,190.3088302612305,188.4566345214844,188.6389694213867,188.6389694213867,188.8284683227539,188.8284683227539,189.0329513549805,189.0329513549805,189.2549362182617,189.2549362182617,189.4875564575195,189.4875564575195,189.7245254516602,189.9592514038086,189.9592514038086,190.1954498291016,190.1954498291016,190.3642501831055,190.3642501831055,190.3642501831055,190.3642501831055,190.3642501831055,190.3642501831055,188.6295318603516,188.6295318603516,188.7985000610352,188.9929275512695,188.9929275512695,189.2016296386719,189.2016296386719,189.4265441894531,189.4265441894531,189.6620407104492,189.6620407104492,189.898796081543,189.898796081543,190.1343994140625,190.1343994140625,190.369255065918,190.4186859130859,190.4186859130859,190.4186859130859,188.5784454345703,188.5784454345703,188.7394256591797,188.7394256591797,188.8843460083008,188.8843460083008,189.081901550293,189.081901550293,189.2888412475586,189.5139083862305,189.5139083862305,189.7436676025391,189.7436676025391,189.9773635864258,189.9773635864258,190.2107925415039,190.4435958862305,190.4435958862305,190.4723052978516,190.4723052978516,188.7082290649414,188.7082290649414,188.8789443969727,188.8789443969727,188.8789443969727,189.0677795410156,189.0677795410156,189.2760467529297,189.2760467529297,189.5046844482422,189.5046844482422,189.7419891357422,189.9793319702148,189.9793319702148,190.2137680053711,190.2137680053711,190.4471740722656,190.4471740722656,190.4471740722656,190.5250778198242,190.5250778198242,190.5250778198242,188.7458343505859,188.7458343505859,188.9267578125,189.1128997802734,189.1128997802734,189.1128997802734,189.3159103393555,189.3159103393555,189.5370559692383,189.5370559692383,189.774284362793,189.774284362793,190.0118637084961,190.0118637084961,190.247688293457,190.247688293457,190.4821014404297,190.5769271850586,190.5769271850586,188.8172073364258,188.8172073364258,189.0000762939453,189.0000762939453,189.190673828125,189.398193359375,189.398193359375,189.6210479736328,189.6210479736328,189.8582916259766,190.1181259155273,190.3524551391602,190.3524551391602,190.5846099853516,190.5846099853516,190.6279983520508,190.6279983520508,188.9356307983398,188.9356307983398,189.1148147583008,189.1148147583008,189.3068161010742,189.5040512084961,189.5040512084961,189.6675491333008,189.6675491333008,189.6675491333008,189.8700637817383,189.8700637817383,190.090950012207,190.090950012207,190.2648620605469,190.2648620605469,190.470329284668,190.6454925537109,190.6454925537109,190.6454925537109,190.6782684326172,190.6782684326172,188.9917068481445,188.9917068481445,189.1713562011719,189.1713562011719,189.1713562011719,189.3436660766602,189.3436660766602,189.5266876220703,189.5266876220703,189.7062530517578,189.7062530517578,189.9167556762695,190.1135330200195,190.3221206665039,190.3221206665039,190.5504302978516,190.5504302978516,190.7276306152344,190.7276306152344,190.7276306152344,190.7276306152344,190.7276306152344,190.7276306152344,189.1306381225586,189.1306381225586,189.2972946166992,189.2972946166992,189.4739456176758,189.6406326293945,189.8382797241211,189.8382797241211,190.0065460205078,190.0065460205078,190.2100982666016,190.3469696044922,190.3469696044922,190.5299911499023,190.5299911499023,190.7316131591797,190.7762298583984,190.7762298583984,190.7762298583984,190.7762298583984,190.7762298583984,190.7762298583984,189.2517318725586,189.2517318725586,189.4071884155273,189.5937347412109,189.5937347412109,189.7665634155273,189.7665634155273,189.948356628418,189.948356628418,190.1563339233398,190.1563339233398,190.3484802246094,190.3484802246094,190.3484802246094,190.5845260620117,190.7892608642578,190.7892608642578,190.8241577148438,190.8241577148438,189.2075347900391,189.2075347900391,189.2075347900391,189.3707046508789,189.555549621582,189.555549621582,189.738166809082,189.738166809082,189.9234771728516,189.9234771728516,190.1292343139648,190.3267135620117,190.3267135620117,190.5388717651367,190.5388717651367,190.5388717651367,190.7429428100586,190.7429428100586,190.8712005615234,190.8712005615234,190.8712005615234,190.8712005615234,189.3591918945312,189.5317840576172,189.5317840576172,189.7095947265625,189.7095947265625,189.8994293212891,189.8994293212891,189.8994293212891,190.1023101806641,190.1023101806641,190.2888107299805,190.2888107299805,190.2888107299805,190.4880142211914,190.702018737793,190.9017105102539,190.9017105102539,190.9175186157227,190.9175186157227,190.9175186157227,189.3770523071289,189.543586730957,189.7195510864258,189.7195510864258,189.7195510864258,189.9023056030273,190.1113510131836,190.1113510131836,190.3309097290039,190.3309097290039,190.5589981079102,190.5589981079102,190.7870101928711,190.9631271362305,190.9631271362305,190.9631271362305,190.9631271362305,190.9631271362305,190.9631271362305,189.536376953125,189.7143783569336,189.9075241088867,189.9075241088867,190.1248168945312,190.1248168945312,190.3507614135742,190.5832824707031,190.5832824707031,190.8159866333008,190.8159866333008,191.0079345703125,191.0079345703125,191.0079345703125,191.0079345703125,191.0079345703125,191.0079345703125,189.5790023803711,189.5790023803711,189.5790023803711,189.7618408203125,189.7618408203125,189.9327926635742,189.9327926635742,190.1453018188477,190.1453018188477,190.3716430664062,190.3716430664062,190.6120758056641,190.85107421875,190.85107421875,191.0519943237305,191.0519943237305,191.0519943237305,191.0519943237305,189.6489410400391,189.6489410400391,189.8328170776367,190.0302963256836,190.0302963256836,190.2445220947266,190.2445220947266,190.4758071899414,190.4758071899414,190.712028503418,190.9735870361328,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,191.0954208374023,189.6018981933594,189.6018981933594,189.6018981933594,189.6018981933594,189.6018981933594,189.6018981933594,189.610969543457,189.7817306518555,189.7817306518555,189.7817306518555,189.964958190918,189.964958190918,190.1618270874023,190.1618270874023,190.1618270874023,190.362548828125,190.362548828125,190.5724029541016,190.5724029541016,190.8056106567383,190.8056106567383,191.0078277587891,191.0078277587891,191.2236557006836,191.2236557006836,191.4471740722656,191.4471740722656,191.4471740722656,191.6726379394531,191.8987197875977,191.8987197875977,192.1260681152344,192.1260681152344,192.351432800293,192.351432800293,192.5401992797852,192.5401992797852,192.7253799438477,192.7253799438477,192.9085159301758,192.9085159301758,193.0922546386719,193.0922546386719,193.275260925293,193.275260925293,193.4601058959961,193.6438293457031,193.8292388916016,193.8292388916016,194.0130157470703,194.0130157470703,194.1988677978516,194.3832550048828,194.3832550048828,194.4392623901367,194.4392623901367,194.4392623901367,194.4392623901367,190.0024337768555,190.0024337768555,190.2060546875,190.419548034668,190.6458435058594,190.8750839233398,191.1094055175781,191.3426818847656,191.3426818847656,191.3426818847656,191.5776901245117,191.5776901245117,191.8133087158203,191.8133087158203,192.0463943481445,192.2786026000977,192.5130996704102,192.5130996704102,192.7476959228516,192.7476959228516,192.9812774658203,192.9812774658203,193.2131271362305,193.4450531005859,193.4450531005859,193.6776733398438,193.9092178344727,193.9092178344727,194.1408157348633,194.1408157348633,194.3650054931641,194.5716094970703,194.5716094970703,194.5716094970703,194.5716094970703,194.5716094970703,194.5716094970703,190.0726318359375,190.2734832763672,190.2734832763672,190.4788055419922,190.4788055419922,190.7004547119141,190.7004547119141,190.7004547119141,190.9276885986328,190.9276885986328,190.9276885986328,191.1462020874023,191.3802490234375,191.3802490234375,191.6196517944336,191.8568420410156,191.8568420410156,192.0938720703125,192.3385391235352,192.3385391235352,192.5425720214844,192.5425720214844,192.7150115966797,192.9374618530273,193.1618576049805,193.1618576049805,193.1618576049805,193.3824310302734,193.3824310302734,193.3824310302734,193.6144409179688,193.8481674194336,193.8481674194336,194.0801315307617,194.0801315307617,194.3140258789062,194.3140258789062,194.3140258789062,194.5365676879883,194.7016983032227,194.7016983032227,194.7016983032227,194.7016983032227,190.2978744506836,190.2978744506836,190.4977493286133,190.4977493286133,190.4977493286133,190.7016983032227,190.9159317016602,190.9159317016602,191.1298370361328,191.1298370361328,191.3400726318359,191.3400726318359,191.5769195556641,191.5769195556641,191.8141479492188,191.8141479492188,192.0489349365234,192.0489349365234,192.2837905883789,192.5399322509766,192.5399322509766,192.7731399536133,192.7731399536133,193.0066986083984,193.0066986083984,193.239387512207,193.239387512207,193.239387512207,193.4717102050781,193.4717102050781,193.7038497924805,193.7038497924805,193.9365921020508,193.9365921020508,194.1697769165039,194.1697769165039,194.4047241210938,194.4047241210938,194.4047241210938,194.6313018798828,194.6313018798828,194.829833984375,194.829833984375,194.829833984375,194.829833984375,190.4660873413086,190.4660873413086,190.6607437133789,190.8596649169922,190.8596649169922,191.0636367797852,191.2659683227539,191.4717483520508,191.4717483520508,191.6979446411133,191.6979446411133,191.6979446411133,191.9339294433594,191.9339294433594,192.1691131591797,192.1691131591797,192.4046249389648,192.6374130249023,192.6374130249023,192.8705062866211,192.8705062866211,193.1033172607422,193.1033172607422,193.3359832763672,193.5673904418945,193.7997665405273,193.7997665405273,194.0561370849609,194.0561370849609,194.2895812988281,194.2895812988281,194.5246810913086,194.5246810913086,194.5246810913086,194.7514190673828,194.7514190673828,194.9558181762695,194.9558181762695,194.9558181762695,194.9558181762695,194.9558181762695,194.9558181762695,190.64599609375,190.8197860717773,190.8197860717773,191.0178298950195,191.0178298950195,191.2147369384766,191.2147369384766,191.4085006713867,191.4085006713867,191.6158905029297,191.6158905029297,191.840461730957,191.840461730957,192.0752487182617,192.0752487182617,192.3081436157227,192.3081436157227,192.3081436157227,192.5401458740234,192.5401458740234,192.7704849243164,192.7704849243164,192.9975662231445,192.9975662231445,193.2057342529297,193.4134979248047,193.5736541748047,193.5736541748047,193.7431488037109,193.7431488037109,193.9706344604492,194.1860733032227,194.1860733032227,194.1860733032227,194.4101333618164,194.4101333618164,194.6342391967773,194.6342391967773,194.8602294921875,194.8602294921875,195.0798110961914,195.0798110961914,195.0798110961914,195.0798110961914,195.0798110961914,195.0798110961914,190.8212203979492,191.0112533569336,191.0112533569336,191.2062149047852,191.3964309692383,191.5785293579102,191.5785293579102,191.5785293579102,191.7755661010742,191.9877395629883,191.9877395629883,191.9877395629883,192.2150115966797,192.2150115966797,192.4390869140625,192.4390869140625,192.6680526733398,192.6680526733398,192.9002304077148,192.9002304077148,193.1301040649414,193.1301040649414,193.3610687255859,193.5936965942383,193.5936965942383,193.8264236450195,194.0589294433594,194.2904891967773,194.2904891967773,194.5225372314453,194.5225372314453,194.754997253418,194.754997253418,195.0039901733398,195.0039901733398,195.2017822265625,195.2017822265625,195.2017822265625,195.2017822265625,195.2017822265625,195.2017822265625,191.031494140625,191.031494140625,191.2195053100586,191.4133911132812,191.4133911132812,191.5988235473633,191.5988235473633,191.783821105957,191.783821105957,191.9912261962891,191.9912261962891,192.2103576660156,192.2103576660156,192.4390106201172,192.4390106201172,192.6651763916016,192.8993301391602,193.1321182250977,193.1321182250977,193.3640975952148,193.3640975952148,193.5950622558594,193.5950622558594,193.8270263671875,193.8270263671875,194.0582962036133,194.0582962036133,194.2899780273438,194.5223159790039,194.7547454833984,194.7547454833984,194.9872741699219,194.9872741699219,195.2090911865234,195.2090911865234,195.32177734375,195.32177734375,195.32177734375,195.32177734375,191.291877746582,191.4945297241211,191.4945297241211,191.6831207275391,191.6831207275391,191.8561401367188,192.0435485839844,192.0435485839844,192.2394485473633,192.4424514770508,192.4424514770508,192.6545791625977,192.6545791625977,192.6545791625977,192.8751983642578,193.1037750244141,193.3328399658203,193.5614852905273,193.7705841064453,193.7705841064453,193.9878845214844,193.9878845214844,194.2078170776367,194.4160079956055,194.4160079956055,194.6293640136719,194.8482437133789,194.8482437133789,195.0531387329102,195.0531387329102,195.2668685913086,195.4398880004883,195.4398880004883,195.4398880004883,195.4398880004883,195.4398880004883,195.4398880004883,191.4200897216797,191.6083755493164,191.7991409301758,191.7991409301758,191.7991409301758,191.9807357788086,192.1834335327148,192.1834335327148,192.1834335327148,192.3991394042969,192.6263275146484,192.6263275146484,192.8595657348633,192.8595657348633,193.0909729003906,193.0909729003906,193.322265625,193.322265625,193.5531768798828,193.7848052978516,193.7848052978516,194.0175247192383,194.0175247192383,194.0175247192383,194.250358581543,194.250358581543,194.4820404052734,194.7150268554688,194.7150268554688,194.7150268554688,194.9486312866211,194.9486312866211,195.1814346313477,195.1814346313477,195.406379699707,195.406379699707,195.5559616088867,195.5559616088867,195.5559616088867,195.5559616088867,191.6231231689453,191.6231231689453,191.812629699707,191.812629699707,191.9988479614258,191.9988479614258,192.1983795166016,192.368522644043,192.368522644043,192.5622024536133,192.7631683349609,192.9350357055664,193.1311645507812,193.1311645507812,193.3012542724609,193.4905548095703,193.4905548095703,193.6922073364258,193.8834228515625,193.8834228515625,194.0856094360352,194.0856094360352,194.2789306640625,194.4751358032227,194.4751358032227,194.6784896850586,194.6784896850586,194.8741760253906,194.8741760253906,195.0812683105469,195.0812683105469,195.275764465332,195.4670791625977,195.6621017456055,195.6703033447266,195.6703033447266,195.6703033447266,195.6703033447266,195.6703033447266,195.6703033447266,191.877311706543,191.877311706543,192.0336151123047,192.0336151123047,192.2152481079102,192.2152481079102,192.3856887817383,192.5752029418945,192.7609634399414,192.7609634399414,192.9378433227539,192.9378433227539,193.1429748535156,193.3242416381836,193.3242416381836,193.5142364501953,193.7097625732422,193.7097625732422,193.8957824707031,193.8957824707031,194.1009140014648,194.1009140014648,194.2820587158203,194.487663269043,194.487663269043,194.6899871826172,194.6899871826172,194.8745727539062,195.0790023803711,195.262092590332,195.4490814208984,195.6360015869141,195.6360015869141,195.7827224731445,195.7827224731445,195.7827224731445,195.7827224731445,195.7827224731445,195.7827224731445,195.7827224731445,195.7827224731445,195.7827224731445,192.0831298828125,192.2612838745117,192.2612838745117,192.4069595336914,192.4069595336914,192.5961532592773,192.5961532592773,192.7945556640625,192.7945556640625,193.0160217285156,193.0160217285156,193.2272796630859,193.2272796630859,193.3866271972656,193.3866271972656,193.6035003662109,193.6035003662109,193.8214874267578,193.8214874267578,194.0420150756836,194.2673416137695,194.2673416137695,194.4887771606445,194.4887771606445,194.7143402099609,194.9384078979492,194.9384078979492,195.1680908203125,195.1680908203125,195.3956527709961,195.3956527709961,195.6242370605469,195.8441925048828,195.8441925048828,195.8933334350586,195.8933334350586,195.8933334350586,195.8933334350586,195.8933334350586,195.8933334350586,192.2238922119141,192.4059219360352,192.5913467407227,192.7881774902344,192.7881774902344,192.9973297119141,192.9973297119141,193.2175445556641,193.4670715332031,193.697998046875,193.697998046875,193.9287490844727,193.9287490844727,194.1599807739258,194.3899688720703,194.6206512451172,194.6206512451172,194.8517913818359,194.8517913818359,195.083381652832,195.083381652832,195.3138046264648,195.3138046264648,195.5450592041016,195.7718124389648,195.7718124389648,195.9915390014648,196.0021896362305,196.0021896362305,196.0021896362305,196.0021896362305,196.0021896362305,196.0021896362305,192.4120941162109,192.4120941162109,192.5914611816406,192.7810821533203,192.7810821533203,192.9814910888672,192.9814910888672,193.1936264038086,193.4173965454102,193.4173965454102,193.6475982666016,193.6475982666016,193.8806838989258,193.8806838989258,194.1117324829102,194.1117324829102,194.342643737793,194.5730819702148,194.5730819702148,194.8043594360352,194.8043594360352,195.0365142822266,195.0365142822266,195.2921676635742,195.2921676635742,195.2921676635742,195.5246505737305,195.5246505737305,195.7560043334961,195.9806060791016,196.1092224121094,196.1092224121094,196.1092224121094,196.1092224121094,196.1092224121094,196.1092224121094,192.4953994750977,192.4953994750977,192.6743240356445,192.6743240356445,192.8589935302734,193.0514373779297,193.0514373779297,193.2575225830078,193.4766006469727,193.4766006469727,193.7059478759766,193.7059478759766,193.9379272460938,193.9379272460938,194.1690444946289,194.1690444946289,194.4003219604492,194.4003219604492,194.6309509277344,194.8640899658203,195.0980682373047,195.3324584960938,195.3324584960938,195.5662612915039,195.7983245849609,196.0270156860352,196.0270156860352,196.2145767211914,196.2145767211914,196.2145767211914,196.2145767211914,196.2145767211914,196.2145767211914,192.6287078857422,192.8088912963867,192.8088912963867,192.8088912963867,192.9945068359375,193.1891098022461,193.1891098022461,193.3970489501953,193.3970489501953,193.6137847900391,193.6137847900391,193.6137847900391,193.8427810668945,193.8427810668945,194.0746307373047,194.3058624267578,194.3058624267578,194.3058624267578,194.5370101928711,194.7646636962891,194.9939498901367,195.2239456176758,195.2239456176758,195.4538040161133,195.4538040161133,195.6833877563477,195.6833877563477,195.9135665893555,195.9135665893555,196.1413879394531,196.3182220458984,196.3182220458984,196.3182220458984,196.3182220458984,196.3182220458984,196.3182220458984,192.7801361083984,192.7801361083984,192.9599838256836,192.9599838256836,193.1445846557617,193.3351898193359,193.3351898193359,193.5361404418945,193.7466583251953,193.7466583251953,193.9954681396484,193.9954681396484,194.2292251586914,194.2292251586914,194.462760925293,194.6954879760742,194.6954879760742,194.9281616210938,194.9281616210938,195.1613311767578,195.1613311767578,195.3950805664062,195.3950805664062,195.6094970703125,195.7914962768555,195.7914962768555,195.7914962768555,195.9535751342773,196.1659698486328,196.1659698486328,196.1659698486328,196.3635177612305,196.3635177612305,196.4202117919922,196.4202117919922,196.4202117919922,196.4202117919922,196.4202117919922,196.4202117919922,192.9658584594727,192.9658584594727,193.1169738769531,193.1169738769531,193.2954025268555,193.2954025268555,193.4712829589844,193.6386413574219,193.6386413574219,193.6386413574219,193.8286590576172,193.8286590576172,194.0192413330078,194.0192413330078,194.2184143066406,194.2184143066406,194.4251327514648,194.4251327514648,194.4251327514648,194.613655090332,194.8330001831055,195.0416107177734,195.0416107177734,195.2528228759766,195.2528228759766,195.475700378418,195.475700378418,195.6920394897461,195.6920394897461,195.9203643798828,195.9203643798828,195.9203643798828,196.1352462768555,196.3506011962891,196.3506011962891,196.5204849243164,196.5204849243164,196.5204849243164,196.5204849243164,196.5204849243164,196.5204849243164,193.0934143066406,193.2576675415039,193.4329605102539,193.4329605102539,193.6194229125977,193.6194229125977,193.7970657348633,193.7970657348633,193.9929122924805,194.1837921142578,194.1837921142578,194.1837921142578,194.3905258178711,194.3905258178711,194.6017379760742,194.6017379760742,194.8125305175781,194.8125305175781,195.0337753295898,195.0337753295898,195.2459487915039,195.2459487915039,195.46630859375,195.46630859375,195.6891632080078,195.9079818725586,196.134895324707,196.134895324707,196.3502502441406,196.5604019165039,196.5604019165039,196.6192092895508,196.6192092895508,196.6192092895508,196.6192092895508,196.6192092895508,196.6192092895508,193.3552551269531,193.3552551269531,193.5342025756836,193.5342025756836,193.7201843261719,193.7201843261719,193.9122161865234,193.9122161865234,194.1171798706055,194.1171798706055,194.337158203125,194.337158203125,194.5697326660156,194.7997131347656,194.7997131347656,195.0306396484375,195.0306396484375,195.2630386352539,195.49462890625,195.49462890625,195.7267761230469,195.7267761230469,195.9603118896484,196.1930160522461,196.1930160522461,196.1930160522461,196.426025390625,196.426025390625,196.6478576660156,196.6478576660156,196.6478576660156,196.7163009643555,196.7163009643555,196.7163009643555,196.7163009643555,196.7163009643555,196.7163009643555,196.7163009643555,196.7163009643555,196.7163009643555,196.7163009643555,196.7163009643555,196.7163009643555,196.7163009643555,196.7163009643555,196.7163009643555,196.7163009643555,196.7163009643555,196.7163009643555,196.7163009643555,196.7163009643555,196.7163009643555,196.7163009643555,196.7163009643555,196.7163009643555,196.7163009643555,196.7163009643555,196.7163009643555,196.7163009643555,196.7163009643555,196.7163009643555,196.7163009643555,196.7163009643555,196.7163009643555,196.7163009643555,196.7163009643555,196.7163009643555,196.7163009643555,196.7163009643555,196.7163009643555,196.7163009643555,196.7163009643555,196.7163009643555,196.7163009643555,196.7163009643555,196.7163009643555,196.7163009643555,196.7163009643555,196.7163009643555,193.467041015625,193.6111068725586,193.6111068725586,193.7820205688477,193.9606704711914,193.9606704711914,194.1482467651367,194.1482467651367,194.3461761474609,194.3461761474609,194.5822067260742,194.5822067260742,194.8115768432617,194.8115768432617,195.0426940917969,195.0426940917969,195.2765731811523,195.2765731811523,195.2765731811523,195.5097579956055,195.5097579956055,195.7423324584961,195.9765472412109,195.9765472412109,196.2109909057617,196.2109909057617,196.2109909057617,196.4443511962891,196.4443511962891,196.6709060668945,196.6709060668945,196.6709060668945,196.8118057250977,196.8118057250977,196.8118057250977,196.8118057250977,196.8118057250977,196.8118057250977,193.5703582763672,193.5703582763672,193.7466659545898,193.7466659545898,193.9308700561523,194.1202774047852,194.1202774047852,194.1202774047852,194.3119430541992,194.3119430541992,194.5049667358398,194.7134246826172,194.7134246826172,194.9325332641602,194.9325332641602,195.1508941650391,195.3324737548828,195.3324737548828,195.3324737548828,195.5337677001953,195.5337677001953,195.711311340332,195.711311340332,195.9264984130859,195.9264984130859,196.1224365234375,196.3054885864258,196.3054885864258,196.5357513427734,196.7108764648438,196.9057846069336,196.9057846069336,196.9057846069336,196.9057846069336,196.9057846069336,196.9057846069336,196.9057846069336,196.9057846069336,196.9057846069336,193.6733093261719,193.8112106323242,193.8112106323242,193.9917449951172,193.9917449951172,194.1740646362305,194.1740646362305,194.3535766601562,194.3535766601562,194.5420913696289,194.7219009399414,194.7219009399414,194.9266815185547,194.9266815185547,195.1180038452148,195.1180038452148,195.3011474609375,195.3011474609375,195.4920501708984,195.6759490966797,195.6759490966797,195.85986328125,195.85986328125,196.0676803588867,196.2868347167969,196.2868347167969,196.5201797485352,196.5201797485352,196.6960144042969,196.6960144042969,196.6960144042969,196.8977890014648,196.8977890014648,196.9983520507812,196.9983520507812,196.9983520507812,196.9983520507812,196.9983520507812,196.9983520507812,193.8304901123047,193.9552688598633,193.9552688598633,194.1377639770508,194.1377639770508,194.3222351074219,194.3222351074219,194.5243911743164,194.5243911743164,194.7235565185547,194.9194946289062,194.9194946289062,195.1331176757812,195.3603668212891,195.5912933349609,195.8237228393555,195.8237228393555,196.0545043945312,196.0545043945312,196.0545043945312,196.2859420776367,196.2859420776367,196.5166778564453,196.5166778564453,196.7496032714844,196.9751510620117,197.0893249511719,197.0893249511719,197.0893249511719,197.0893249511719,194.0214309692383,194.0214309692383,194.2004165649414,194.2004165649414,194.3830871582031,194.3830871582031,194.5779113769531,194.5779113769531,194.7868804931641,194.7868804931641,194.7868804931641,195.0084686279297,195.0084686279297,195.2434539794922,195.2434539794922,195.4773788452148,195.4773788452148,195.708869934082,195.9411392211914,195.9411392211914,196.1956329345703,196.1956329345703,196.4273834228516,196.4273834228516,196.6599426269531,196.8927307128906,196.8927307128906,197.111930847168,197.111930847168,197.1789474487305,197.1789474487305,197.1789474487305,197.1789474487305,197.1789474487305,197.1789474487305,194.2029113769531,194.2029113769531,194.3801116943359,194.3801116943359,194.5605087280273,194.5605087280273,194.5605087280273,194.7352676391602,194.7352676391602,194.7352676391602,194.8891983032227,194.8891983032227,195.0871200561523,195.0871200561523,195.2960891723633,195.2960891723633,195.2960891723633,195.5026016235352,195.5026016235352,195.6968841552734,195.6968841552734,195.6968841552734,195.9120025634766,195.9120025634766,196.1229858398438,196.3203430175781,196.3203430175781,196.3203430175781,196.5334167480469,196.7427597045898,196.7427597045898,196.960823059082,196.960823059082,197.1689987182617,197.2670288085938,197.2670288085938,197.2670288085938,197.2670288085938,197.2670288085938,197.2670288085938,194.2355194091797,194.2355194091797,194.4016876220703,194.4016876220703,194.530143737793,194.530143737793,194.6907043457031,194.8564605712891,194.8564605712891,195.0058441162109,195.0058441162109,195.2267150878906,195.2267150878906,195.3969650268555,195.3969650268555,195.6106719970703,195.6106719970703,195.827018737793,196.001091003418,196.2251281738281,196.3960876464844,196.3960876464844,196.6209182739258,196.6209182739258,196.8535537719727,197.0683364868164,197.0683364868164,197.2831878662109,197.2831878662109,197.3536987304688,197.3536987304688,197.3536987304688,197.3536987304688,197.3536987304688,197.3536987304688,194.4527053833008,194.4527053833008,194.6115036010742,194.6115036010742,194.7794418334961,194.7794418334961,194.946647644043,195.1112823486328,195.1112823486328,195.2948150634766,195.2948150634766,195.2948150634766,195.4655456542969,195.4655456542969,195.6749420166016,195.8999099731445,196.1197052001953,196.1197052001953,196.3514022827148,196.5791702270508,196.5791702270508,196.8081588745117,196.8081588745117,197.0388488769531,197.2694396972656,197.2694396972656,197.4389953613281,197.4389953613281,197.4389953613281,197.4389953613281,197.4389953613281,197.4389953613281,194.5172271728516,194.5172271728516,194.6865081787109,194.8660888671875,194.8660888671875,195.0368804931641,195.2338562011719,195.2338562011719,195.4556198120117,195.4556198120117,195.6861953735352,195.6861953735352,195.9464263916016,195.9464263916016,196.1759719848633,196.1759719848633,196.4065933227539,196.4065933227539,196.6381759643555,196.6381759643555,196.8704833984375,197.1041107177734,197.3350448608398,197.5229187011719,197.5229187011719,197.5229187011719,197.5229187011719,197.5229187011719,197.5229187011719,194.6394271850586,194.6394271850586,194.81396484375,194.9928207397461,195.1802597045898,195.1802597045898,195.3836059570312,195.3836059570312,195.6035003662109,195.6035003662109,195.8359832763672,195.8359832763672,196.068489074707,196.068489074707,196.2994384765625,196.2994384765625,196.5305938720703,196.7613220214844,196.7613220214844,196.9917068481445,196.9917068481445,197.2241897583008,197.2241897583008,197.4503784179688,197.4503784179688,197.6054840087891,197.6054840087891,197.6054840087891,197.6054840087891,197.6054840087891,197.6054840087891,194.8104400634766,194.8104400634766,194.9828643798828,194.9828643798828,195.1640243530273,195.3493041992188,195.3493041992188,195.5468597412109,195.5468597412109,195.7597122192383,195.7597122192383,195.9885177612305,196.2219161987305,196.2219161987305,196.4559860229492,196.4559860229492,196.6896209716797,196.9219436645508,197.1560287475586,197.3905868530273,197.3905868530273,197.6158828735352,197.6866607666016,197.6866607666016,197.6866607666016,197.6866607666016,197.6866607666016,197.6866607666016,194.9801330566406,195.1380462646484,195.1380462646484,195.3170471191406,195.5008926391602,195.5008926391602,195.6837921142578,195.89892578125,196.0778579711914,196.0778579711914,196.2723159790039,196.2723159790039,196.4646301269531,196.4646301269531,196.6636276245117,196.6636276245117,196.8812942504883,197.084602355957,197.084602355957,197.2958831787109,197.2958831787109,197.5171356201172,197.5171356201172,197.7214279174805,197.7666397094727,197.7666397094727,197.7666397094727,197.7666397094727,197.7666397094727,197.7666397094727,195.084358215332,195.2527465820312,195.4174118041992,195.4174118041992,195.603759765625,195.603759765625,195.7953414916992,195.7953414916992,195.7953414916992,195.9814987182617,195.9814987182617,196.1805038452148,196.1805038452148,196.3772506713867,196.3772506713867,196.592041015625,196.592041015625,196.7934951782227,196.7934951782227,197.0041961669922,197.0041961669922,197.0041961669922,197.2170944213867,197.4173126220703,197.6340484619141,197.8268203735352,197.8268203735352,197.8452453613281,197.8452453613281,197.8452453613281,197.8452453613281,197.8452453613281,197.8452453613281,195.2238235473633,195.2238235473633,195.3940505981445,195.3940505981445,195.5546264648438,195.5546264648438,195.5546264648438,195.7297439575195,195.7297439575195,195.7297439575195,195.9170150756836,195.9170150756836,196.1150970458984,196.1150970458984,196.3126525878906,196.50048828125,196.6902923583984,196.6902923583984,196.8962860107422,196.8962860107422,197.1066818237305,197.1066818237305,197.3292541503906,197.5587844848633,197.7870025634766,197.7870025634766,197.9225463867188,197.9225463867188,197.9225463867188,197.9225463867188,195.2859954833984,195.2859954833984,195.4518203735352,195.4518203735352,195.6248474121094,195.6248474121094,195.8078384399414,195.8078384399414,195.9975128173828,195.9975128173828,196.1926574707031,196.1926574707031,196.4027557373047,196.6266174316406,196.6266174316406,196.8572387695312,197.0874099731445,197.0874099731445,197.3427810668945,197.3427810668945,197.5734634399414,197.5734634399414,197.8063659667969,197.8063659667969,197.9986801147461,197.9986801147461,197.9986801147461,197.9986801147461,197.9986801147461,197.9986801147461,197.9986801147461,197.9986801147461,197.9986801147461,195.5274124145508,195.5274124145508,195.6995544433594,195.6995544433594,195.8835220336914,196.072265625,196.072265625,196.2757110595703,196.492073059082,196.7215576171875,196.7215576171875,196.9570617675781,196.9570617675781,197.1909942626953,197.1909942626953,197.4258880615234,197.6596450805664,197.6596450805664,197.893180847168,198.0735855102539,198.0735855102539,198.0735855102539,198.0735855102539,198.0735855102539,198.0735855102539,198.0735855102539,198.0735855102539,198.0735855102539,195.6546173095703,195.8471450805664,195.8471450805664,196.0325927734375,196.0325927734375,196.2224578857422,196.4235687255859,196.4235687255859,196.636360168457,196.8636474609375,196.8636474609375,197.0937118530273,197.0937118530273,197.3276290893555,197.3276290893555,197.5633087158203,197.5633087158203,197.797721862793,197.797721862793,198.0277786254883,198.0277786254883,198.1472091674805,198.1472091674805,198.1472091674805,198.1472091674805,195.636474609375,195.8001937866211,195.9745635986328,195.9745635986328,196.1540832519531,196.1540832519531,196.1540832519531,196.3444519042969,196.3444519042969,196.5448837280273,196.5448837280273,196.7582473754883,196.7582473754883,196.7582473754883,196.9809494018555,196.9809494018555,197.2088470458984,197.4400253295898,197.672981262207,197.672981262207,197.9051513671875,197.9051513671875,198.1512222290039,198.2196807861328,198.2196807861328,198.2196807861328,198.2196807861328,195.7864074707031,195.9520034790039,195.9520034790039,196.1246566772461,196.1246566772461,196.309326171875,196.4994277954102,196.6986618041992,196.6986618041992,196.6986618041992,196.9105072021484,197.1327667236328,197.1327667236328,197.3587951660156,197.3587951660156,197.5908126831055,197.5908126831055,197.8072967529297,197.8072967529297,198.0357818603516,198.0357818603516,198.2565307617188,198.2565307617188,198.2910842895508,198.2910842895508,198.2910842895508,198.2910842895508,198.2910842895508,198.2910842895508,195.8523864746094,195.9488983154297,195.9488983154297,196.0593643188477,196.1636810302734,196.1636810302734,196.2783203125,196.2783203125,196.4802703857422,196.4802703857422,196.4802703857422,196.6992492675781,196.6992492675781,196.9231643676758,196.9231643676758,197.1479644775391,197.1479644775391,197.1479644775391,197.3707809448242,197.3707809448242,197.5912551879883,197.8143997192383,197.8143997192383,198.0354843139648,198.0354843139648,198.2529144287109,198.2529144287109,198.3611831665039,198.3611831665039,198.3611831665039,198.3611831665039,198.3611831665039,198.3611831665039,198.3611831665039,198.3611831665039,198.3611831665039,196.0843200683594,196.0843200683594,196.2510147094727,196.2510147094727,196.4334945678711,196.6409301757812,196.6409301757812,196.6409301757812,196.8424224853516,197.0590133666992,197.2845764160156,197.2845764160156,197.5177993774414,197.5177993774414,197.5177993774414,197.7493896484375,197.7493896484375,197.9817199707031,198.2124938964844,198.2124938964844,198.4302520751953,198.4302520751953,198.4302520751953,198.4302520751953,198.4302520751953,198.4302520751953,198.4302520751953,198.4302520751953,198.4302520751953,198.4302520751953,198.4302520751953,198.4302520751953,198.4302520751953,198.4302520751953,198.4302520751953,198.4302520751953,198.4302520751953,198.4302520751953,198.4302520751953,198.4302520751953,198.4302520751953,198.4302520751953,198.4302520751953,198.4302520751953,198.4302520751953,198.4302520751953,198.4302520751953,198.4302520751953,198.4302520751953,198.4302520751953,198.4302520751953,198.4302520751953,198.4302520751953,198.4302520751953,198.4302520751953,198.4302520751953,198.4302520751953,198.4302520751953,198.4302520751953,198.4302520751953,198.4302520751953,198.4302520751953,196.054084777832,196.054084777832,196.054084777832,196.0576477050781,196.1921691894531,196.3522720336914,196.5268630981445,196.5268630981445,196.7135391235352,196.7135391235352,196.9054946899414,196.9054946899414,197.1090469360352,197.1090469360352,197.3284683227539,197.5540390014648,197.5540390014648,197.7761917114258,197.7761917114258,198.0001220703125,198.0001220703125,198.2269897460938,198.2269897460938,198.4545822143555,198.4979400634766,198.4979400634766,198.4979400634766,198.4979400634766,198.4979400634766,198.4979400634766,196.2697296142578,196.4382553100586,196.4382553100586,196.6214218139648,196.6214218139648,196.8089904785156,196.8089904785156,196.8089904785156,197.0123672485352,197.0123672485352,197.2308120727539,197.4594650268555,197.4594650268555,197.6934280395508,197.6934280395508,197.9241409301758,197.9241409301758,197.9241409301758,198.1571731567383,198.1571731567383,198.1571731567383,198.3880996704102,198.3880996704102,198.3880996704102,198.5647964477539,198.5647964477539,198.5647964477539,198.5647964477539,198.5647964477539,198.5647964477539,198.5647964477539,198.5647964477539,198.5647964477539,196.4289245605469,196.4289245605469,196.6034164428711,196.7879638671875,196.7879638671875,196.9800491333008,197.190315246582,197.190315246582,197.4118957519531,197.6448745727539,197.8761444091797,198.1305160522461,198.3616180419922,198.3616180419922,198.593620300293,198.593620300293,198.593620300293,198.6305160522461,198.6305160522461,198.6305160522461,198.6305160522461,196.4620895385742,196.4620895385742,196.4620895385742,196.6340255737305,196.8158187866211,197.0046997070312,197.0046997070312,197.1595764160156,197.3765335083008,197.6021957397461,197.8369140625,198.0696105957031,198.0696105957031,198.3029251098633,198.5360336303711,198.5360336303711,198.6952896118164,198.6952896118164,198.6952896118164,198.6952896118164,196.4746475219727,196.4746475219727,196.6341552734375,196.6341552734375,196.8106155395508,197.0151596069336,197.0151596069336,197.2118072509766,197.4253692626953,197.4253692626953,197.6566848754883,197.6566848754883,197.8921432495117,197.8921432495117,198.1258087158203,198.3602981567383,198.5922927856445,198.5922927856445,198.7589340209961,198.7589340209961,198.7589340209961,198.7589340209961,196.573616027832,196.573616027832,196.7416229248047,196.9192733764648,196.9192733764648,197.1063842773438,197.3058471679688,197.3058471679688,197.5238418579102,197.7530746459961,197.9889755249023,197.9889755249023,198.2238159179688,198.4575119018555,198.4575119018555,198.689826965332,198.689826965332,198.8216094970703,198.8216094970703,198.8216094970703,198.8216094970703,198.8216094970703,198.8216094970703,196.7086639404297,196.8809280395508,196.8809280395508,197.0625457763672,197.0625457763672,197.2515563964844,197.2515563964844,197.4571914672852,197.4571914672852,197.6448211669922,197.6448211669922,197.8734436035156,197.8734436035156,198.1101608276367,198.1101608276367,198.343505859375,198.343505859375,198.5769119262695,198.5769119262695,198.5769119262695,198.8099670410156,198.8099670410156,198.8832855224609,198.8832855224609,198.8832855224609,198.8832855224609,198.8832855224609,198.8832855224609,196.8351211547852,196.8351211547852,197.0066680908203,197.0066680908203,197.1911697387695,197.3807830810547,197.3807830810547,197.588264465332,197.588264465332,197.8112258911133,197.8112258911133,198.0455017089844,198.0455017089844,198.2840270996094,198.5169906616211,198.5169906616211,198.7758865356445,198.9439239501953,198.9439239501953,198.9439239501953,198.9439239501953,196.860710144043,196.860710144043,197.0307006835938,197.0307006835938,197.209228515625,197.209228515625,197.3960571289062,197.3960571289062,197.6013488769531,197.6013488769531,197.8218688964844,198.0558319091797,198.2915191650391,198.2915191650391,198.2915191650391,198.5257568359375,198.5257568359375,198.7588424682617,198.7588424682617,198.9888763427734,198.9888763427734,199.0035934448242,199.0035934448242,199.0035934448242,199.0035934448242,199.0035934448242,199.0035934448242,197.0602188110352,197.0602188110352,197.2333145141602,197.4174423217773,197.6115188598633,197.6115188598633,197.8233795166016,197.8233795166016,198.0498580932617,198.0498580932617,198.3078079223633,198.3078079223633,198.5384521484375,198.7693481445312,198.7693481445312,198.7693481445312,198.9990844726562,199.062255859375,199.062255859375,199.062255859375,199.062255859375,197.1176986694336,197.1176986694336,197.1176986694336,197.2893829345703,197.4721374511719,197.4721374511719,197.6627731323242,197.8705978393555,198.0919570922852,198.0919570922852,198.3261795043945,198.5603942871094,198.7924270629883,198.7924270629883,199.0260009765625,199.0260009765625,199.1200485229492,199.1200485229492,199.1200485229492,199.1200485229492,199.1200485229492,199.1200485229492,197.1890182495117,197.1890182495117,197.3607406616211,197.54345703125,197.54345703125,197.7353210449219,197.9678268432617,198.1935958862305,198.1935958862305,198.4313659667969,198.6663513183594,198.6663513183594,198.8990783691406,198.8990783691406,199.1317138671875,199.1317138671875,199.1317138671875,199.1768188476562,199.1768188476562,199.1768188476562,199.1768188476562,199.1768188476562,199.1768188476562,199.1768188476562,199.1768188476562,197.3061447143555,197.3061447143555,197.4782943725586,197.4782943725586,197.6623687744141,197.6623687744141,197.8561553955078,198.0684280395508,198.0684280395508,198.2963714599609,198.2963714599609,198.5329742431641,198.7678604125977,199.0017700195312,199.0017700195312,199.2327117919922,199.2327117919922,199.2327117919922,199.2327117919922,199.2327117919922,199.2327117919922,199.2327117919922,199.2327117919922,199.2327117919922,197.4351959228516,197.6114730834961,197.6114730834961,197.797607421875,197.797607421875,197.797607421875,197.9736557006836,197.9736557006836,198.1915435791016,198.1915435791016,198.4205932617188,198.6581420898438,198.6581420898438,198.8927536010742,198.8927536010742,198.8927536010742,199.1269912719727,199.2876739501953,199.2876739501953,199.2876739501953,199.2876739501953,197.4022521972656,197.4022521972656,197.5738220214844,197.5738220214844,197.5738220214844,197.7554168701172,197.7554168701172,197.9455261230469,198.1555633544922,198.1555633544922,198.3842163085938,198.6235656738281,198.8384552001953,198.8384552001953,199.0698623657227,199.3029403686523,199.3029403686523,199.3417587280273,199.3417587280273,199.3417587280273,199.3417587280273,199.3417587280273,199.3417587280273,199.3417587280273,199.3417587280273,199.3417587280273,199.3417587280273,199.3417587280273,199.3417587280273,199.3417587280273,199.3417587280273,199.3417587280273,199.3417587280273,199.3417587280273,199.3417587280273,199.3417587280273,199.3417587280273,199.3417587280273,197.5370712280273,197.6749420166016,197.8492431640625,197.8492431640625,198.0380706787109,198.0380706787109,198.239501953125,198.239501953125,198.4621810913086,198.4621810913086,198.695915222168,198.695915222168,198.935791015625,198.935791015625,199.173095703125,199.173095703125,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,199.3946838378906,197.5629806518555,197.5629806518555,197.5629806518555,197.5629806518555,197.5629806518555,197.5629806518555,197.5629806518555,197.5629806518555,197.5629806518555,197.6777877807617,197.8690032958984,197.8690032958984,198.0643157958984,198.0643157958984,198.0643157958984,198.2768630981445,198.5058670043945,198.739875793457,198.739875793457,198.9616775512695,198.9616775512695,199.1720886230469,199.1720886230469,199.3761749267578,199.3761749267578,199.600471496582,199.600471496582,199.8254928588867,200.0577239990234,200.0577239990234,200.2926635742188,200.2926635742188,200.5239639282227,200.5239639282227,200.7637023925781,200.7637023925781,200.9983215332031,200.9983215332031,201.2293701171875,201.2293701171875,201.4526290893555,201.6412200927734,201.6412200927734,201.6412200927734,201.8316268920898,201.8316268920898,202.0228805541992,202.0228805541992,202.0228805541992,202.210807800293,202.210807800293,202.4031143188477,202.4031143188477,202.5938568115234,202.5938568115234,202.7867202758789,202.7867202758789,202.9767684936523,202.9767684936523,202.9767684936523,203.1701202392578,203.1701202392578,203.3622817993164,203.3622817993164,203.5553588867188,203.7469100952148,203.9402923583984,203.9402923583984,204.1321487426758,204.3255233764648,204.5180206298828,204.708366394043,204.708366394043,204.9005584716797,205.0912551879883,205.0912551879883,205.1758193969727,205.1758193969727,205.1758193969727,205.1758193969727,205.1758193969727,205.1758193969727,205.1758193969727,205.1758193969727,205.1758193969727,198.0349655151367,198.0349655151367,198.2237167358398,198.4196319580078,198.4196319580078,198.6303558349609,198.6303558349609,198.8481216430664,198.8481216430664,199.0717926025391,199.2886199951172,199.2886199951172,199.4945755004883,199.4945755004883,199.7249603271484,199.7249603271484,199.9540252685547,200.1819000244141,200.1819000244141,200.4097366333008,200.4097366333008,200.6383819580078,200.866828918457,200.866828918457,201.0950927734375,201.0950927734375,201.3236236572266,201.5515060424805,201.5515060424805,201.7782211303711,201.7782211303711,202.0091323852539,202.240478515625,202.4716873168945,202.7019119262695,202.7019119262695,202.9314346313477,203.1603240966797,203.3884429931641,203.6414794921875,203.871826171875,203.871826171875,204.1021041870117,204.1021041870117,204.330696105957,204.330696105957,204.5598526000977,204.5598526000977,204.7904891967773,204.7904891967773,205.0090942382812,205.0090942382812,205.2240295410156,205.2240295410156,205.3839569091797,205.3839569091797,205.3839569091797,205.3839569091797,205.3839569091797,205.3839569091797,205.3839569091797,205.3839569091797,198.3847808837891,198.3847808837891,198.3847808837891,198.5764465332031,198.5764465332031,198.7204437255859,198.7204437255859,198.8620681762695,198.8620681762695,199.0707168579102,199.0707168579102,199.0707168579102,199.2565460205078,199.2565460205078,199.2565460205078,199.4430541992188,199.4430541992188,199.6224136352539,199.6224136352539,199.6224136352539,199.8031311035156,199.8031311035156,200.0005416870117,200.194091796875,200.3895721435547,200.5935134887695,200.5935134887695,200.5935134887695,200.7896575927734,200.7896575927734,200.9960174560547,200.9960174560547,201.2026214599609,201.4107208251953,201.4107208251953,201.6258010864258,201.6258010864258,201.8290100097656,201.8290100097656,202.0412979125977,202.2489852905273,202.4596633911133,202.6919937133789,202.6919937133789,202.8928070068359,203.0838775634766,203.0838775634766,203.2845993041992,203.2845993041992,203.2845993041992,203.483039855957,203.6946640014648,203.89208984375,203.89208984375,204.0956420898438,204.0956420898438,204.3061981201172,204.5034713745117,204.5034713745117,204.7156143188477,204.7156143188477,204.7156143188477,204.9077529907227,204.9077529907227,205.1181564331055,205.1181564331055,205.1181564331055,205.3288269042969,205.5482177734375,205.5482177734375,205.5888977050781,205.5888977050781,205.5888977050781,205.5888977050781,205.5888977050781,205.5888977050781,198.6397247314453,198.6397247314453,198.6397247314453,198.8183364868164,198.8183364868164,199.0085906982422,199.0085906982422,199.2042388916016,199.2042388916016,199.2042388916016,199.4054794311523,199.4054794311523,199.6099700927734,199.6099700927734,199.8092498779297,199.8092498779297,200.0209274291992,200.0209274291992,200.2395858764648,200.4724273681641,200.4724273681641,200.7005081176758,200.7005081176758,200.9315948486328,200.9315948486328,201.1598892211914,201.1598892211914,201.3908920288086,201.6238479614258,201.6238479614258,201.8570785522461,201.8570785522461,202.0878067016602,202.3183975219727,202.3183975219727,202.5491561889648,202.5491561889648,202.7805404663086,203.0124588012695,203.2685852050781,203.2685852050781,203.5005950927734,203.5005950927734,203.7325439453125,203.7325439453125,203.9652404785156,203.9652404785156,204.196044921875,204.196044921875,204.4253921508789,204.6560974121094,204.6560974121094,204.8874282836914,205.1188201904297,205.1188201904297,205.3437881469727,205.3437881469727,205.5655670166016,205.5655670166016,205.7875671386719,205.7875671386719,205.7875671386719,205.790397644043,205.790397644043,205.790397644043,205.790397644043,205.790397644043,205.790397644043,205.790397644043,205.790397644043,205.790397644043,198.9548263549805,198.9548263549805,199.1292343139648,199.1292343139648,199.1292343139648,199.3182907104492,199.5155258178711,199.7076034545898,199.7076034545898,199.8997955322266,200.0909957885742,200.3087615966797,200.3087615966797,200.5539703369141,200.7791061401367,201.0022811889648,201.0022811889648,201.0022811889648,201.2330169677734,201.2330169677734,201.2330169677734,201.4653244018555,201.4653244018555,201.6984329223633,201.9305267333984,201.9305267333984,202.1640701293945,202.1640701293945,202.3966445922852,202.3966445922852,202.6289520263672,202.6289520263672,202.8605499267578,202.8605499267578,203.0927047729492,203.0927047729492,203.3247299194336,203.3247299194336,203.55615234375,203.55615234375,203.55615234375,203.7884521484375,204.0202789306641,204.0202789306641,204.2529754638672,204.2529754638672,204.4249649047852,204.4249649047852,204.6530914306641,204.8798065185547,205.1105270385742,205.1105270385742,205.339485168457,205.5639572143555,205.5639572143555,205.7846984863281,205.7846984863281,205.7846984863281,205.9887619018555,205.9887619018555,205.9887619018555,205.9887619018555,205.9887619018555,205.9887619018555,205.9887619018555,205.9887619018555,205.9887619018555,205.9887619018555,205.9887619018555,205.9887619018555,199.3041763305664,199.3041763305664,199.4888305664062,199.4888305664062,199.6839599609375,199.6839599609375,199.8781585693359,199.8781585693359,200.0711822509766,200.2649459838867,200.2649459838867,200.4851989746094,200.7157745361328,200.7157745361328,200.948974609375,200.948974609375,201.1817779541016,201.1817779541016,201.4128875732422,201.4128875732422,201.6446762084961,201.8759536743164,202.1067733764648,202.3376693725586,202.3376693725586,202.568733215332,202.799201965332,202.799201965332,203.0295562744141,203.0295562744141,203.259651184082,203.4899978637695,203.4899978637695,203.7208633422852,203.95166015625,204.1824340820312,204.1824340820312,204.412727355957,204.6490783691406,204.879768371582,204.879768371582,205.1118621826172,205.3443069458008,205.5758666992188,205.5758666992188,205.7972030639648,205.7972030639648,206.0170135498047,206.1838607788086,206.1838607788086,206.1838607788086,206.1838607788086,206.1838607788086,206.1838607788086,206.1838607788086,206.1838607788086,199.5783767700195,199.5783767700195,199.757209777832,199.757209777832,199.9474029541016,200.1356887817383,200.1356887817383,200.3233413696289,200.5155944824219,200.7326736450195,200.7326736450195,200.9537963867188,200.9537963867188,200.9537963867188,201.1824035644531,201.1824035644531,201.433349609375,201.433349609375,201.6609954833984,201.8901138305664,201.8901138305664,202.1187438964844,202.3481140136719,202.3481140136719,202.5750503540039,202.8038177490234,202.8038177490234,203.030517578125,203.030517578125,203.2567749023438,203.2567749023438,203.4816970825195,203.4816970825195,203.4816970825195,203.7087554931641,203.7087554931641,203.937614440918,203.937614440918,204.1671524047852,204.3971405029297,204.3971405029297,204.6287689208984,204.6287689208984,204.8612594604492,204.8612594604492,205.0940093994141,205.3271484375,205.3271484375,205.559700012207,205.559700012207,205.7911834716797,206.0155410766602,206.0155410766602,206.2372055053711,206.2372055053711,206.3758087158203,206.3758087158203,206.3758087158203,206.3758087158203,206.3758087158203,206.3758087158203,206.3758087158203,206.3758087158203,206.3758087158203,206.3758087158203,206.3758087158203,206.3758087158203,206.3758087158203,206.3758087158203,206.3758087158203,206.3758087158203,206.3758087158203,206.3758087158203,206.3758087158203,206.3758087158203,206.3758087158203,206.3758087158203,206.3758087158203,206.3758087158203,206.3758087158203,206.3758087158203,206.3758087158203,206.3758087158203,206.3758087158203,206.3758087158203,199.7931365966797,199.9383773803711,200.1174697875977,200.3036499023438,200.489128112793,200.489128112793,200.6702575683594,200.6702575683594,200.8801574707031,201.1027221679688,201.3272933959961,201.5567398071289,201.5567398071289,201.7863388061523,202.0156631469727,202.2437286376953,202.2437286376953,202.4724273681641,202.7015838623047,202.7015838623047,202.930419921875,202.930419921875,203.1828918457031,203.1828918457031,203.1828918457031,203.4111938476562,203.4111938476562,203.4111938476562,203.6391143798828,203.6391143798828,203.8686676025391,203.8686676025391,204.0980072021484,204.0980072021484,204.3279113769531,204.5580673217773,204.5580673217773,204.7886428833008,204.7886428833008,205.0190658569336,205.0190658569336,205.2497940063477,205.2497940063477,205.4807205200195,205.4807205200195,205.7106094360352,205.7106094360352,205.9426498413086,206.1675338745117,206.1675338745117,206.3888092041016,206.3888092041016,206.5645217895508,206.5645217895508,206.5645217895508,206.5645217895508,206.5645217895508,206.5645217895508,206.5645217895508,206.5645217895508,206.5645217895508,206.5645217895508,206.5645217895508,206.5645217895508,200.1893539428711,200.1893539428711,200.3713531494141,200.3713531494141,200.5610122680664,200.5610122680664,200.7649688720703,200.9598083496094,201.1783294677734,201.1783294677734,201.4103012084961,201.4103012084961,201.6427001953125,201.6427001953125,201.8714904785156,201.8714904785156,202.1001663208008,202.3278198242188,202.5556335449219,202.5556335449219,202.7671508789062,202.993293762207,202.993293762207,203.2201080322266,203.4477691650391,203.4477691650391,203.6746444702148,203.6746444702148,203.9019546508789,203.9019546508789,204.1298294067383,204.1298294067383,204.3581619262695,204.3581619262695,204.5862655639648,204.5862655639648,204.8153076171875,205.0447769165039,205.0447769165039,205.2734069824219,205.5008392333984,205.5008392333984,205.7313003540039,205.9626770019531,205.9626770019531,206.1946563720703,206.1946563720703,206.4173583984375,206.4173583984375,206.6399078369141,206.7503967285156,206.7503967285156,206.7503967285156,206.7503967285156,206.7503967285156,206.7503967285156,206.7503967285156,206.7503967285156,206.7503967285156,200.4055099487305,200.5785293579102,200.7638549804688,200.7638549804688,200.7638549804688,200.9475784301758,200.9475784301758,201.1344528198242,201.1344528198242,201.3479919433594,201.3479919433594,201.5735321044922,201.5735321044922,201.8058090209961,201.8058090209961,202.0087280273438,202.2245712280273,202.3966522216797,202.3966522216797,202.5991668701172,202.5991668701172,202.8188781738281,202.8188781738281,203.012451171875,203.012451171875,203.2201614379883,203.2201614379883,203.4347534179688,203.6264114379883,203.6264114379883,203.8341751098633,203.8341751098633,203.8341751098633,204.0196380615234,204.0196380615234,204.0196380615234,204.2305374145508,204.2305374145508,204.4405822753906,204.6557388305664,204.6557388305664,204.6557388305664,204.8803939819336,205.102668762207,205.102668762207,205.3314971923828,205.3314971923828,205.3314971923828,205.5579071044922,205.7849044799805,206.0102386474609,206.0102386474609,206.0102386474609,206.2232437133789,206.2232437133789,206.4439926147461,206.4439926147461,206.6582489013672,206.6582489013672,206.8727111816406,206.8727111816406,206.9331665039062,206.9331665039062,206.9331665039062,206.9331665039062,206.9331665039062,206.9331665039062,200.7043609619141,200.8794021606445,201.0623550415039,201.0623550415039,201.2400894165039,201.2400894165039,201.4243621826172,201.4243621826172,201.6170654296875,201.6170654296875,201.8016738891602,201.8016738891602,202.0135879516602,202.0135879516602,202.2192459106445,202.2192459106445,202.432487487793,202.432487487793,202.432487487793,202.6523590087891,202.6523590087891,202.6523590087891,202.8652114868164,202.8652114868164,203.0905151367188,203.0905151367188,203.3049468994141,203.3049468994141,203.5258636474609,203.5258636474609,203.7484893798828,203.9728469848633,203.9728469848633,204.2021636962891,204.2021636962891,204.2021636962891,212.0353317260742,212.0353317260742,212.0353317260742,212.0353317260742,212.0353317260742,212.0353317260742,212.0353317260742,212.0353317260742,212.0353317260742,212.0353317260742,212.0353317260742,212.0353317260742,212.0353317260742,212.0353317260742,212.0353317260742,212.0353317260742,212.0353317260742,212.0353317260742,212.0353317260742,212.0353317260742,212.0353317260742,212.0353317260742,212.0353317260742,212.0353317260742,219.6647262573242,219.6647338867188,219.6647338867188,219.6647338867188,219.6647338867188,219.6647338867188,219.6647338867188,219.6647338867188,219.6647338867188,219.6647338867188,219.6647338867188,219.6647338867188,219.6647338867188,219.6647338867188,219.6647338867188,219.6647338867188,219.6647338867188,219.6647338867188,219.6647338867188,219.6647338867188,219.6647338867188,219.6647338867188,219.6647338867188,219.6647338867188,219.6647338867188,219.6647338867188,219.6647338867188,234.9235229492188,234.9235229492188,234.9235229492188,234.9235229492188,234.9235229492188,234.9235229492188,234.9235229492188,234.9235229492188,234.9235229492188,234.9235229492188,234.9235229492188,234.9235229492188,234.9235229492188,234.9235229492188,234.9235229492188,234.9235229492188,234.9235229492188,234.9235229492188,234.9235229492188,234.9235229492188,242.5529403686523,242.5529403686523,242.5529403686523,242.5529403686523,242.5529403686523,242.5529403686523,242.5529403686523,242.5529403686523,242.6679153442383,242.6679153442383,242.6679153442383,242.6679153442383,242.6679153442383,242.6679153442383,242.6679153442383,242.6679153442383,242.6679153442383,242.6679153442383,242.6679153442383,242.6679153442383,242.6679153442383,242.6679153442383,242.6679153442383,242.6679153442383,242.6679153442383,242.6679153442383,242.6679153442383,242.6679153442383,242.6679153442383,242.6679153442383,242.6679153442383,242.6679153442383,242.6679153442383,242.6679153442383,242.6679153442383,242.6679153442383,242.6679153442383,242.6679153442383,242.6679153442383,242.6679153442383,242.6679153442383,242.6679153442383,242.6679153442383,242.6679153442383,242.6679153442383,242.6679153442383,242.6679153442383,242.6679153442383,242.6679153442383,242.6679153442383,242.6679153442383,242.6679153442383,242.6679153442383,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766,257.9481353759766],"meminc":[0,0,0,0,0,0,15.28223419189453,0,0,0,0,0,0,0,30.46574401855469,0,0,0,0,0,0,0,0,0,0,0,4.57763671875e-05,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-0.00030517578125,0,0,0,15.41893005371094,0.1547164916992188,0,0.1724777221679688,0.1667404174804688,0,0.203338623046875,0,0.2145004272460938,0.212677001953125,0.21453857421875,0,0.2193603515625,0,0.227752685546875,0.2274169921875,0,0.2281570434570312,0,0.2293701171875,0,0.2257232666015625,0.20648193359375,0,0,0,-2.754127502441406,0,0,0.2286300659179688,0,0.2399368286132812,0,0.2431564331054688,0,0.243560791015625,0,0.2405624389648438,0.238189697265625,0.2343673706054688,0,0.2328948974609375,0,0.2347946166992188,0,0.2333831787109375,0,0.2338638305664062,0,0.2152023315429688,0,0,0,-2.664070129394531,0,0.2467193603515625,0.2405548095703125,0,0.2454452514648438,0,0.2430343627929688,0.2402496337890625,0,0.2361679077148438,0,0.233978271484375,0.232086181640625,0.2328567504882812,0.2330322265625,0,0.2306442260742188,0.1310882568359375,0,0,0,-2.672332763671875,0,0.2077255249023438,0,0.1902618408203125,0,0.2125091552734375,0.2329635620117188,0,0.238494873046875,0,0,0.2333831787109375,0,0,0.2305068969726562,0.253631591796875,0,0,0.230255126953125,0,0.2319488525390625,0,0,0.2319564819335938,0,0.2309646606445312,0,0.028228759765625,0,0,-2.646331787109375,0,0.2009658813476562,0,0.2096481323242188,0,0.2264938354492188,0.2303009033203125,0,0.2360153198242188,0,0,0.2343063354492188,0.2306747436523438,0,0.2325286865234375,0,0.2312545776367188,0,0.2313003540039062,0,0.2319564819335938,0,0.2300643920898438,0,0,0,0,0,-2.5806884765625,0,0.198974609375,0,0.2075881958007812,0.221099853515625,0,0.2335586547851562,0.2362594604492188,0.234893798828125,0,0.2562637329101562,0.2331390380859375,0,0.231475830078125,0,0,0.23138427734375,0.232574462890625,0,0.1414108276367188,0,-2.668266296386719,0,0,0.200897216796875,0.202392578125,0.2117538452148438,0,0,0.2232284545898438,0,0.2305526733398438,0,0,0.2361907958984375,0,0.2346038818359375,0,0.2335433959960938,0,0.2339096069335938,0.2300643920898438,0,0.2339553833007812,0,0.2337265014648438,0,0.04004669189453125,0,-2.536064147949219,0,0.2013931274414062,0,0.20306396484375,0,0.2151412963867188,0,0.2260284423828125,0,0.2277297973632812,0,0,0.2363815307617188,0,0.2358016967773438,0.2341079711914062,0,0,0.257049560546875,0,0.2327499389648438,0.2314071655273438,0,0.1107177734375,0,0,-2.565254211425781,0,0.17755126953125,0,0.2009735107421875,0.2092208862304688,0.2213973999023438,0,0.2289276123046875,0,0.2320480346679688,0,0.23284912109375,0,0.2305374145507812,0,0.2319564819335938,0.2301177978515625,0.2308731079101562,0,0.2129592895507812,0,0,0,-2.408660888671875,0,0.1998138427734375,0,0.2012710571289062,0,0.2125930786132812,0.2215347290039062,0,0.2238006591796875,0.233734130859375,0.2340164184570312,0,0.234466552734375,0,0,0.2340774536132812,0,0.2578201293945312,0.22857666015625,0,0,0,0,0,-2.374732971191406,0,0.2022018432617188,0.2147445678710938,0,0,0.2214889526367188,0.1847686767578125,0,0.20404052734375,0,0.2223129272460938,0,0.1990509033203125,0.2210769653320312,0,0.1805191040039062,0.1958999633789062,0.175933837890625,0,0.1851272583007812,0,0.03936767578125,0,0,-2.403656005859375,0,0,0.2130279541015625,0,0.1885986328125,0,0.1882858276367188,0,0.21234130859375,0,0.198638916015625,0,0.2131881713867188,0.2084808349609375,0,0.199737548828125,0,0.2236251831054688,0.1994247436523438,0,0.2138671875,0.2035903930664062,0,0,0.01155853271484375,0,0,-2.354095458984375,0,0,0.1812744140625,0,0,0.1903762817382812,0,0.187042236328125,0,0.1840896606445312,0,0.228302001953125,0,0.1984710693359375,0,0.2044143676757812,0,0.2206268310546875,0,0.1996231079101562,0,0.2161865234375,0,0.1648101806640625,0,0,0.1974411010742188,0.0509490966796875,0,-2.369697570800781,0,0.1894989013671875,0.1709136962890625,0,0.1685867309570312,0.1881561279296875,0,0.1761932373046875,0,0.2151641845703125,0,0.2042236328125,0,0.1997451782226562,0.2226333618164062,0,0,0.1876907348632812,0.202606201171875,0,0.2147216796875,0,0.09793853759765625,0,0,0,-2.350006103515625,0,0,0.1757965087890625,0,0.1850204467773438,0,0.1782150268554688,0.1804122924804688,0,0.2100906372070312,0.2017288208007812,0,0.2125701904296875,0.2124710083007812,0,0.2021331787109375,0,0.2488250732421875,0,0,0.2034835815429688,0.2065963745117188,0,0,0,0,0,-2.214279174804688,0,0,0.1942214965820312,0.171966552734375,0,0.1877593994140625,0,0.1950225830078125,0.1857833862304688,0,0.2171096801757812,0.190216064453125,0.1992721557617188,0.2159652709960938,0.2118911743164062,0,0.2305908203125,0,0.0806732177734375,0,0,-2.240211486816406,0,0,0.2118453979492188,0.1917266845703125,0,0.2034988403320312,0.2179946899414062,0.2318191528320312,0,0.1695632934570312,0,0.18511962890625,0,0.1775436401367188,0,0,0.2209548950195312,0,0.2106475830078125,0.2306594848632812,0,0.05396270751953125,0,-2.190147399902344,0,0.1893157958984375,0,0.1963272094726562,0,0.2014999389648438,0.2195053100585938,0,0.2301406860351562,0.229766845703125,0,0.2366790771484375,0,0.2518768310546875,0.2325057983398438,0.2289886474609375,0,0.03766632080078125,0,-2.136177062988281,0.1804046630859375,0,0.2021331787109375,0,0.2065963745117188,0,0.2265167236328125,0,0.23516845703125,0,0.2345428466796875,0.2306442260742188,0.2303924560546875,0,0.2314453125,0,0.221405029296875,0,0,0,0,0,-2.047561645507812,0,0.1929931640625,0,0.18414306640625,0.2142105102539062,0,0.2319717407226562,0,0.23779296875,0,0.2368240356445312,0.2345352172851562,0.2350692749023438,0,0.2573165893554688,0.084716796875,0,0,-2.0960693359375,0,0.1719818115234375,0,0.1958160400390625,0.207305908203125,0,0.2259674072265625,0,0,0.2357177734375,0.2340240478515625,0,0.2345962524414062,0,0.232177734375,0,0,0.2321929931640625,0,0.1873626708984375,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.979164123535156,0.1678237915039062,0,0,0.1782760620117188,0,0.1907272338867188,0.200408935546875,0,0.2186431884765625,0,0.2305755615234375,0,0.2335586547851562,0,0.232208251953125,0,0.233856201171875,0,0.15277099609375,0,0,0,-1.920852661132812,0,0.1448135375976562,0.137542724609375,0,0,0.18603515625,0.20916748046875,0.1755828857421875,0.2100448608398438,0,0.2311019897460938,0,0.2311019897460938,0,0.2302627563476562,0,0.2242813110351562,0,0,0,0,0,-1.929084777832031,0,0.1826324462890625,0,0.1957244873046875,0.20892333984375,0,0.2332382202148438,0,0,0.2337265014648438,0,0.2356643676757812,0,0,0.2319564819335938,0,0.2297134399414062,0,0.2342681884765625,0,0,0.0014190673828125,0,0,-1.940315246582031,0.1719894409179688,0,0.19793701171875,0,0.2091445922851562,0,0.2276611328125,0.23699951171875,0,0.25909423828125,0.2324676513671875,0,0.2333450317382812,0,0.2288742065429688,0,0,0,-1.879280090332031,0,0.1710739135742188,0,0.1888351440429688,0,0,0.2044296264648438,0,0.2248306274414062,0.23583984375,0.2387542724609375,0,0.2360153198242188,0,0.1811599731445312,0.2310333251953125,0,0.0235748291015625,0,0,-1.852195739746094,0.1823348999023438,0,0.1894989013671875,0,0.2044830322265625,0,0.22198486328125,0,0.2326202392578125,0,0.236968994140625,0.2347259521484375,0,0.2361984252929688,0,0.1688003540039062,0,0,0,0,0,-1.734718322753906,0,0.1689682006835938,0.194427490234375,0,0.2087020874023438,0,0.22491455078125,0,0.2354965209960938,0,0.23675537109375,0,0.2356033325195312,0,0.2348556518554688,0.04943084716796875,0,0,-1.840240478515625,0,0.160980224609375,0,0.1449203491210938,0,0.1975555419921875,0,0.206939697265625,0.225067138671875,0,0.2297592163085938,0,0.2336959838867188,0,0.233428955078125,0.2328033447265625,0,0.02870941162109375,0,-1.764076232910156,0,0.17071533203125,0,0,0.1888351440429688,0,0.2082672119140625,0,0.2286376953125,0,0.2373046875,0.2373428344726562,0,0.23443603515625,0,0.2334060668945312,0,0,0.07790374755859375,0,0,-1.779243469238281,0,0.1809234619140625,0.1861419677734375,0,0,0.2030105590820312,0,0.2211456298828125,0,0.2372283935546875,0,0.237579345703125,0,0.2358245849609375,0,0.2344131469726562,0.09482574462890625,0,-1.759719848632812,0,0.1828689575195312,0,0.1905975341796875,0.20751953125,0,0.2228546142578125,0,0.23724365234375,0.2598342895507812,0.2343292236328125,0,0.2321548461914062,0,0.04338836669921875,0,-1.692367553710938,0,0.1791839599609375,0,0.1920013427734375,0.197235107421875,0,0.1634979248046875,0,0,0.2025146484375,0,0.22088623046875,0,0.1739120483398438,0,0.2054672241210938,0.1751632690429688,0,0,0.03277587890625,0,-1.686561584472656,0,0.1796493530273438,0,0,0.1723098754882812,0,0.1830215454101562,0,0.1795654296875,0,0.2105026245117188,0.19677734375,0.208587646484375,0,0.2283096313476562,0,0.1772003173828125,0,0,0,0,0,-1.596992492675781,0,0.166656494140625,0,0.1766510009765625,0.16668701171875,0.1976470947265625,0,0.1682662963867188,0,0.20355224609375,0.136871337890625,0,0.1830215454101562,0,0.2016220092773438,0.04461669921875,0,0,0,0,0,-1.524497985839844,0,0.15545654296875,0.1865463256835938,0,0.1728286743164062,0,0.181793212890625,0,0.207977294921875,0,0.1921463012695312,0,0,0.2360458374023438,0.2047348022460938,0,0.0348968505859375,0,-1.616622924804688,0,0,0.1631698608398438,0.184844970703125,0,0.1826171875,0,0.1853103637695312,0,0.2057571411132812,0.197479248046875,0,0.212158203125,0,0,0.204071044921875,0,0.1282577514648438,0,0,0,-1.512008666992188,0.1725921630859375,0,0.1778106689453125,0,0.1898345947265625,0,0,0.202880859375,0,0.1865005493164062,0,0,0.1992034912109375,0.2140045166015625,0.1996917724609375,0,0.01580810546875,0,0,-1.54046630859375,0.166534423828125,0.17596435546875,0,0,0.1827545166015625,0.20904541015625,0,0.2195587158203125,0,0.22808837890625,0,0.2280120849609375,0.176116943359375,0,0,0,0,0,-1.426750183105469,0.1780014038085938,0.193145751953125,0,0.2172927856445312,0,0.2259445190429688,0.2325210571289062,0,0.2327041625976562,0,0.1919479370117188,0,0,0,0,0,-1.428932189941406,0,0,0.1828384399414062,0,0.1709518432617188,0,0.2125091552734375,0,0.2263412475585938,0,0.2404327392578125,0.2389984130859375,0,0.2009201049804688,0,0,0,-1.403053283691406,0,0.1838760375976562,0.197479248046875,0,0.2142257690429688,0,0.2312850952148438,0,0.2362213134765625,0.2615585327148438,0.1218338012695312,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.493522644042969,0,0,0,0,0,0.00907135009765625,0.1707611083984375,0,0,0.1832275390625,0,0.196868896484375,0,0,0.2007217407226562,0,0.2098541259765625,0,0.2332077026367188,0,0.2022171020507812,0,0.2158279418945312,0,0.2235183715820312,0,0,0.2254638671875,0.2260818481445312,0,0.2273483276367188,0,0.2253646850585938,0,0.1887664794921875,0,0.1851806640625,0,0.183135986328125,0,0.1837387084960938,0,0.1830062866210938,0,0.184844970703125,0.1837234497070312,0.1854095458984375,0,0.18377685546875,0,0.18585205078125,0.18438720703125,0,0.05600738525390625,0,0,0,-4.43682861328125,0,0.2036209106445312,0.2134933471679688,0.2262954711914062,0.2292404174804688,0.2343215942382812,0.2332763671875,0,0,0.2350082397460938,0,0.2356185913085938,0,0.2330856323242188,0.232208251953125,0.2344970703125,0,0.2345962524414062,0,0.23358154296875,0,0.2318496704101562,0.2319259643554688,0,0.2326202392578125,0.2315444946289062,0,0.231597900390625,0,0.2241897583007812,0.20660400390625,0,0,0,0,0,-4.498977661132812,0.2008514404296875,0,0.205322265625,0,0.221649169921875,0,0,0.22723388671875,0,0,0.2185134887695312,0.2340469360351562,0,0.2394027709960938,0.2371902465820312,0,0.237030029296875,0.2446670532226562,0,0.2040328979492188,0,0.1724395751953125,0.2224502563476562,0.224395751953125,0,0,0.2205734252929688,0,0,0.2320098876953125,0.2337265014648438,0,0.231964111328125,0,0.2338943481445312,0,0,0.2225418090820312,0.165130615234375,0,0,0,-4.403823852539062,0,0.1998748779296875,0,0,0.203948974609375,0.2142333984375,0,0.2139053344726562,0,0.210235595703125,0,0.236846923828125,0,0.2372283935546875,0,0.2347869873046875,0,0.2348556518554688,0.2561416625976562,0,0.2332077026367188,0,0.2335586547851562,0,0.2326889038085938,0,0,0.2323226928710938,0,0.2321395874023438,0,0.2327423095703125,0,0.233184814453125,0,0.2349472045898438,0,0,0.2265777587890625,0,0.1985321044921875,0,0,0,-4.363746643066406,0,0.1946563720703125,0.1989212036132812,0,0.2039718627929688,0.20233154296875,0.205780029296875,0,0.2261962890625,0,0,0.2359848022460938,0,0.2351837158203125,0,0.2355117797851562,0.2327880859375,0,0.23309326171875,0,0.2328109741210938,0,0.232666015625,0.2314071655273438,0.2323760986328125,0,0.2563705444335938,0,0.2334442138671875,0,0.2350997924804688,0,0,0.2267379760742188,0,0.2043991088867188,0,0,0,0,0,-4.309822082519531,0.1737899780273438,0,0.1980438232421875,0,0.1969070434570312,0,0.1937637329101562,0,0.2073898315429688,0,0.2245712280273438,0,0.2347869873046875,0,0.2328948974609375,0,0,0.2320022583007812,0,0.2303390502929688,0,0.227081298828125,0,0.2081680297851562,0.207763671875,0.16015625,0,0.16949462890625,0,0.2274856567382812,0.2154388427734375,0,0,0.22406005859375,0,0.2241058349609375,0,0.2259902954101562,0,0.2195816040039062,0,0,0,0,0,-4.258590698242188,0.190032958984375,0,0.1949615478515625,0.190216064453125,0.182098388671875,0,0,0.1970367431640625,0.2121734619140625,0,0,0.2272720336914062,0,0.2240753173828125,0,0.2289657592773438,0,0.232177734375,0,0.2298736572265625,0,0.2309646606445312,0.2326278686523438,0,0.23272705078125,0.2325057983398438,0.2315597534179688,0,0.2320480346679688,0,0.2324600219726562,0,0.248992919921875,0,0.1977920532226562,0,0,0,0,0,-4.1702880859375,0,0.1880111694335938,0.1938858032226562,0,0.1854324340820312,0,0.18499755859375,0,0.2074050903320312,0,0.2191314697265625,0,0.2286529541015625,0,0.226165771484375,0.2341537475585938,0.2327880859375,0,0.2319793701171875,0,0.2309646606445312,0,0.231964111328125,0,0.2312698364257812,0,0.2316818237304688,0.2323379516601562,0.2324295043945312,0,0.2325286865234375,0,0.2218170166015625,0,0.1126861572265625,0,0,0,-4.029899597167969,0.2026519775390625,0,0.1885910034179688,0,0.1730194091796875,0.187408447265625,0,0.1958999633789062,0.2030029296875,0,0.212127685546875,0,0,0.2206192016601562,0.22857666015625,0.22906494140625,0.2286453247070312,0.2090988159179688,0,0.2173004150390625,0,0.2199325561523438,0.20819091796875,0,0.2133560180664062,0.2188796997070312,0,0.20489501953125,0,0.2137298583984375,0.1730194091796875,0,0,0,0,0,-4.019798278808594,0.1882858276367188,0.190765380859375,0,0,0.1815948486328125,0.20269775390625,0,0,0.2157058715820312,0.2271881103515625,0,0.2332382202148438,0,0.2314071655273438,0,0.231292724609375,0,0.2309112548828125,0.23162841796875,0,0.2327194213867188,0,0,0.2328338623046875,0,0.2316818237304688,0.2329864501953125,0,0,0.2336044311523438,0,0.2328033447265625,0,0.224945068359375,0,0.1495819091796875,0,0,0,-3.932838439941406,0,0.1895065307617188,0,0.18621826171875,0,0.1995315551757812,0.1701431274414062,0,0.1936798095703125,0.2009658813476562,0.1718673706054688,0.1961288452148438,0,0.1700897216796875,0.189300537109375,0,0.2016525268554688,0.1912155151367188,0,0.2021865844726562,0,0.1933212280273438,0.1962051391601562,0,0.2033538818359375,0,0.1956863403320312,0,0.20709228515625,0,0.1944961547851562,0.191314697265625,0.1950225830078125,0.00820159912109375,0,0,0,0,0,-3.792991638183594,0,0.1563034057617188,0,0.1816329956054688,0,0.170440673828125,0.18951416015625,0.185760498046875,0,0.1768798828125,0,0.2051315307617188,0.1812667846679688,0,0.1899948120117188,0.195526123046875,0,0.1860198974609375,0,0.2051315307617188,0,0.1811447143554688,0.2056045532226562,0,0.2023239135742188,0,0.1845855712890625,0.2044296264648438,0.1830902099609375,0.1869888305664062,0.186920166015625,0,0.1467208862304688,0,0,0,0,0,0,0,0,-3.699592590332031,0.1781539916992188,0,0.1456756591796875,0,0.1891937255859375,0,0.1984024047851562,0,0.221466064453125,0,0.2112579345703125,0,0.1593475341796875,0,0.2168731689453125,0,0.217987060546875,0,0.2205276489257812,0.2253265380859375,0,0.221435546875,0,0.2255630493164062,0.2240676879882812,0,0.2296829223632812,0,0.2275619506835938,0,0.2285842895507812,0.2199554443359375,0,0.04914093017578125,0,0,0,0,0,-3.669441223144531,0.1820297241210938,0.1854248046875,0.1968307495117188,0,0.2091522216796875,0,0.22021484375,0.2495269775390625,0.230926513671875,0,0.2307510375976562,0,0.231231689453125,0.2299880981445312,0.230682373046875,0,0.23114013671875,0,0.2315902709960938,0,0.2304229736328125,0,0.2312545776367188,0.2267532348632812,0,0.2197265625,0.010650634765625,0,0,0,0,0,-3.590095520019531,0,0.1793670654296875,0.1896209716796875,0,0.200408935546875,0,0.2121353149414062,0.2237701416015625,0,0.2302017211914062,0,0.2330856323242188,0,0.231048583984375,0,0.2309112548828125,0.230438232421875,0,0.2312774658203125,0,0.2321548461914062,0,0.2556533813476562,0,0,0.23248291015625,0,0.231353759765625,0.2246017456054688,0.1286163330078125,0,0,0,0,0,-3.613822937011719,0,0.178924560546875,0,0.1846694946289062,0.19244384765625,0,0.206085205078125,0.2190780639648438,0,0.2293472290039062,0,0.2319793701171875,0,0.2311172485351562,0,0.2312774658203125,0,0.2306289672851562,0.2331390380859375,0.233978271484375,0.2343902587890625,0,0.2338027954101562,0.2320632934570312,0.2286911010742188,0,0.18756103515625,0,0,0,0,0,-3.585868835449219,0.1801834106445312,0,0,0.1856155395507812,0.1946029663085938,0,0.2079391479492188,0,0.21673583984375,0,0,0.2289962768554688,0,0.2318496704101562,0.231231689453125,0,0,0.2311477661132812,0.2276535034179688,0.2292861938476562,0.2299957275390625,0,0.2298583984375,0,0.229583740234375,0,0.2301788330078125,0,0.2278213500976562,0.1768341064453125,0,0,0,0,0,-3.5380859375,0,0.1798477172851562,0,0.184600830078125,0.1906051635742188,0,0.2009506225585938,0.2105178833007812,0,0.248809814453125,0,0.2337570190429688,0,0.2335357666015625,0.23272705078125,0,0.2326736450195312,0,0.2331695556640625,0,0.2337493896484375,0,0.21441650390625,0.1819992065429688,0,0,0.162078857421875,0.2123947143554688,0,0,0.1975479125976562,0,0.05669403076171875,0,0,0,0,0,-3.454353332519531,0,0.1511154174804688,0,0.1784286499023438,0,0.1758804321289062,0.1673583984375,0,0,0.1900177001953125,0,0.190582275390625,0,0.1991729736328125,0,0.2067184448242188,0,0,0.1885223388671875,0.2193450927734375,0.2086105346679688,0,0.211212158203125,0,0.2228775024414062,0,0.216339111328125,0,0.2283248901367188,0,0,0.2148818969726562,0.2153549194335938,0,0.1698837280273438,0,0,0,0,0,-3.427070617675781,0.1642532348632812,0.17529296875,0,0.18646240234375,0,0.177642822265625,0,0.1958465576171875,0.1908798217773438,0,0,0.2067337036132812,0,0.211212158203125,0,0.2107925415039062,0,0.2212448120117188,0,0.2121734619140625,0,0.2203598022460938,0,0.2228546142578125,0.2188186645507812,0.2269134521484375,0,0.2153549194335938,0.2101516723632812,0,0.058807373046875,0,0,0,0,0,-3.263954162597656,0,0.1789474487304688,0,0.1859817504882812,0,0.1920318603515625,0,0.2049636840820312,0,0.2199783325195312,0,0.232574462890625,0.22998046875,0,0.230926513671875,0,0.2323989868164062,0.2315902709960938,0,0.232147216796875,0,0.2335357666015625,0.2327041625976562,0,0,0.2330093383789062,0,0.221832275390625,0,0,0.06844329833984375,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-3.249259948730469,0.1440658569335938,0,0.1709136962890625,0.17864990234375,0,0.1875762939453125,0,0.1979293823242188,0,0.2360305786132812,0,0.2293701171875,0,0.2311172485351562,0,0.2338790893554688,0,0,0.233184814453125,0,0.232574462890625,0.2342147827148438,0,0.2344436645507812,0,0,0.2333602905273438,0,0.2265548706054688,0,0,0.140899658203125,0,0,0,0,0,-3.241447448730469,0,0.1763076782226562,0,0.1842041015625,0.1894073486328125,0,0,0.1916656494140625,0,0.193023681640625,0.2084579467773438,0,0.2191085815429688,0,0.2183609008789062,0.18157958984375,0,0,0.2012939453125,0,0.1775436401367188,0,0.2151870727539062,0,0.1959381103515625,0.1830520629882812,0,0.2302627563476562,0.1751251220703125,0.1949081420898438,0,0,0,0,0,0,0,0,-3.232475280761719,0.1379013061523438,0,0.1805343627929688,0,0.1823196411132812,0,0.1795120239257812,0,0.1885147094726562,0.1798095703125,0,0.2047805786132812,0,0.1913223266601562,0,0.1831436157226562,0,0.1909027099609375,0.18389892578125,0,0.1839141845703125,0,0.2078170776367188,0.2191543579101562,0,0.2333450317382812,0,0.1758346557617188,0,0,0.2017745971679688,0,0.1005630493164062,0,0,0,0,0,-3.167861938476562,0.1247787475585938,0,0.1824951171875,0,0.1844711303710938,0,0.2021560668945312,0,0.1991653442382812,0.1959381103515625,0,0.213623046875,0.2272491455078125,0.230926513671875,0.2324295043945312,0,0.2307815551757812,0,0,0.2314376831054688,0,0.2307357788085938,0,0.2329254150390625,0.2255477905273438,0.1141738891601562,0,0,0,-3.067893981933594,0,0.178985595703125,0,0.1826705932617188,0,0.19482421875,0,0.2089691162109375,0,0,0.221588134765625,0,0.2349853515625,0,0.2339248657226562,0,0.2314910888671875,0.232269287109375,0,0.2544937133789062,0,0.23175048828125,0,0.2325592041015625,0.2327880859375,0,0.2192001342773438,0,0.0670166015625,0,0,0,0,0,-2.976036071777344,0,0.1772003173828125,0,0.1803970336914062,0,0,0.1747589111328125,0,0,0.1539306640625,0,0.1979217529296875,0,0.2089691162109375,0,0,0.206512451171875,0,0.1942825317382812,0,0,0.215118408203125,0,0.2109832763671875,0.197357177734375,0,0,0.21307373046875,0.2093429565429688,0,0.2180633544921875,0,0.2081756591796875,0.09803009033203125,0,0,0,0,0,-3.031509399414062,0,0.166168212890625,0,0.1284561157226562,0,0.1605606079101562,0.1657562255859375,0,0.149383544921875,0,0.2208709716796875,0,0.1702499389648438,0,0.2137069702148438,0,0.2163467407226562,0.174072265625,0.2240371704101562,0.17095947265625,0,0.2248306274414062,0,0.232635498046875,0.21478271484375,0,0.2148513793945312,0,0.0705108642578125,0,0,0,0,0,-2.900993347167969,0,0.1587982177734375,0,0.167938232421875,0,0.167205810546875,0.1646347045898438,0,0.18353271484375,0,0,0.1707305908203125,0,0.2093963623046875,0.2249679565429688,0.2197952270507812,0,0.2316970825195312,0.2277679443359375,0,0.2289886474609375,0,0.2306900024414062,0.2305908203125,0,0.1695556640625,0,0,0,0,0,-2.921768188476562,0,0.169281005859375,0.1795806884765625,0,0.1707916259765625,0.1969757080078125,0,0.2217636108398438,0,0.2305755615234375,0,0.2602310180664062,0,0.2295455932617188,0,0.230621337890625,0,0.2315826416015625,0,0.2323074340820312,0.2336273193359375,0.2309341430664062,0.1878738403320312,0,0,0,0,0,-2.883491516113281,0,0.1745376586914062,0.1788558959960938,0.18743896484375,0,0.2033462524414062,0,0.2198944091796875,0,0.23248291015625,0,0.2325057983398438,0,0.2309494018554688,0,0.2311553955078125,0.2307281494140625,0,0.2303848266601562,0,0.23248291015625,0,0.2261886596679688,0,0.1551055908203125,0,0,0,0,0,-2.7950439453125,0,0.17242431640625,0,0.1811599731445312,0.1852798461914062,0,0.1975555419921875,0,0.2128524780273438,0,0.2288055419921875,0.2333984375,0,0.23406982421875,0,0.2336349487304688,0.2323226928710938,0.2340850830078125,0.23455810546875,0,0.2252960205078125,0.07077789306640625,0,0,0,0,0,-2.706527709960938,0.1579132080078125,0,0.1790008544921875,0.1838455200195312,0,0.1828994750976562,0.2151336669921875,0.1789321899414062,0,0.1944580078125,0,0.1923141479492188,0,0.1989974975585938,0,0.2176666259765625,0.20330810546875,0,0.2112808227539062,0,0.22125244140625,0,0.2042922973632812,0.0452117919921875,0,0,0,0,0,-2.682281494140625,0.1683883666992188,0.1646652221679688,0,0.1863479614257812,0,0.1915817260742188,0,0,0.1861572265625,0,0.199005126953125,0,0.196746826171875,0,0.2147903442382812,0,0.2014541625976562,0,0.2107009887695312,0,0,0.2128982543945312,0.2002182006835938,0.21673583984375,0.1927719116210938,0,0.01842498779296875,0,0,0,0,0,-2.621421813964844,0,0.17022705078125,0,0.1605758666992188,0,0,0.1751174926757812,0,0,0.1872711181640625,0,0.1980819702148438,0,0.1975555419921875,0.187835693359375,0.1898040771484375,0,0.20599365234375,0,0.2103958129882812,0,0.2225723266601562,0.2295303344726562,0.2282180786132812,0,0.1355438232421875,0,0,0,-2.636550903320312,0,0.1658248901367188,0,0.1730270385742188,0,0.1829910278320312,0,0.1896743774414062,0,0.1951446533203125,0,0.2100982666015625,0.2238616943359375,0,0.230621337890625,0.2301712036132812,0,0.25537109375,0,0.230682373046875,0,0.2329025268554688,0,0.1923141479492188,0,0,0,0,0,0,0,0,-2.471267700195312,0,0.1721420288085938,0,0.1839675903320312,0.1887435913085938,0,0.2034454345703125,0.2163619995117188,0.2294845581054688,0,0.235504150390625,0,0.2339324951171875,0,0.234893798828125,0.2337570190429688,0,0.2335357666015625,0.1804046630859375,0,0,0,0,0,0,0,0,-2.418968200683594,0.1925277709960938,0,0.1854476928710938,0,0.1898651123046875,0.20111083984375,0,0.2127914428710938,0.2272872924804688,0,0.2300643920898438,0,0.233917236328125,0,0.2356796264648438,0,0.2344131469726562,0,0.2300567626953125,0,0.1194305419921875,0,0,0,-2.510734558105469,0.1637191772460938,0.1743698120117188,0,0.1795196533203125,0,0,0.19036865234375,0,0.2004318237304688,0,0.2133636474609375,0,0,0.2227020263671875,0,0.2278976440429688,0.2311782836914062,0.2329559326171875,0,0.2321701049804688,0,0.2460708618164062,0.06845855712890625,0,0,0,-2.433273315429688,0.1655960083007812,0,0.1726531982421875,0,0.1846694946289062,0.1901016235351562,0.1992340087890625,0,0,0.2118453979492188,0.222259521484375,0,0.2260284423828125,0,0.2320175170898438,0,0.2164840698242188,0,0.228485107421875,0,0.2207489013671875,0,0.03455352783203125,0,0,0,0,0,-2.438697814941406,0.0965118408203125,0,0.1104660034179688,0.1043167114257812,0,0.1146392822265625,0,0.2019500732421875,0,0,0.2189788818359375,0,0.2239151000976562,0,0.2248001098632812,0,0,0.2228164672851562,0,0.2204742431640625,0.22314453125,0,0.2210845947265625,0,0.2174301147460938,0,0.1082687377929688,0,0,0,0,0,0,0,0,-2.276863098144531,0,0.1666946411132812,0,0.1824798583984375,0.2074356079101562,0,0,0.2014923095703125,0.2165908813476562,0.2255630493164062,0,0.2332229614257812,0,0,0.2315902709960938,0,0.232330322265625,0.23077392578125,0,0.2177581787109375,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2.376167297363281,0,0,0.00356292724609375,0.134521484375,0.1601028442382812,0.174591064453125,0,0.186676025390625,0,0.19195556640625,0,0.20355224609375,0,0.21942138671875,0.2255706787109375,0,0.2221527099609375,0,0.2239303588867188,0,0.22686767578125,0,0.2275924682617188,0.04335784912109375,0,0,0,0,0,-2.22821044921875,0.1685256958007812,0,0.18316650390625,0,0.1875686645507812,0,0,0.2033767700195312,0,0.21844482421875,0.2286529541015625,0,0.2339630126953125,0,0.230712890625,0,0,0.2330322265625,0,0,0.230926513671875,0,0,0.17669677734375,0,0,0,0,0,0,0,0,-2.135871887207031,0,0.1744918823242188,0.1845474243164062,0,0.1920852661132812,0.21026611328125,0,0.2215805053710938,0.2329788208007812,0.2312698364257812,0.2543716430664062,0.2311019897460938,0,0.2320022583007812,0,0,0.036895751953125,0,0,0,-2.168426513671875,0,0,0.17193603515625,0.181793212890625,0.1888809204101562,0,0.154876708984375,0.2169570922851562,0.2256622314453125,0.2347183227539062,0.232696533203125,0,0.2333145141601562,0.2331085205078125,0,0.1592559814453125,0,0,0,-2.22064208984375,0,0.1595077514648438,0,0.1764602661132812,0.2045440673828125,0,0.1966476440429688,0.21356201171875,0,0.2313156127929688,0,0.2354583740234375,0,0.2336654663085938,0.2344894409179688,0.23199462890625,0,0.1666412353515625,0,0,0,-2.185317993164062,0,0.1680068969726562,0.1776504516601562,0,0.1871109008789062,0.199462890625,0,0.2179946899414062,0.2292327880859375,0.23590087890625,0,0.2348403930664062,0.2336959838867188,0,0.2323150634765625,0,0.1317825317382812,0,0,0,0,0,-2.112945556640625,0.1722640991210938,0,0.1816177368164062,0,0.1890106201171875,0,0.2056350708007812,0,0.1876296997070312,0,0.2286224365234375,0,0.2367172241210938,0,0.2333450317382812,0,0.2334060668945312,0,0,0.2330551147460938,0,0.0733184814453125,0,0,0,0,0,-2.048164367675781,0,0.1715469360351562,0,0.1845016479492188,0.1896133422851562,0,0.2074813842773438,0,0.22296142578125,0,0.2342758178710938,0,0.238525390625,0.2329635620117188,0,0.2588958740234375,0.1680374145507812,0,0,0,-2.083213806152344,0,0.1699905395507812,0,0.17852783203125,0,0.18682861328125,0,0.205291748046875,0,0.22052001953125,0.2339630126953125,0.235687255859375,0,0,0.2342376708984375,0,0.2330856323242188,0,0.2300338745117188,0,0.01471710205078125,0,0,0,0,0,-1.943374633789062,0,0.173095703125,0.1841278076171875,0.1940765380859375,0,0.2118606567382812,0,0.2264785766601562,0,0.2579498291015625,0,0.2306442260742188,0.23089599609375,0,0,0.229736328125,0.06317138671875,0,0,0,-1.944557189941406,0,0,0.1716842651367188,0.1827545166015625,0,0.1906356811523438,0.20782470703125,0.2213592529296875,0,0.234222412109375,0.2342147827148438,0.2320327758789062,0,0.2335739135742188,0,0.09404754638671875,0,0,0,0,0,-1.9310302734375,0,0.171722412109375,0.1827163696289062,0,0.191864013671875,0.2325057983398438,0.22576904296875,0,0.2377700805664062,0.2349853515625,0,0.23272705078125,0,0.232635498046875,0,0,0.04510498046875,0,0,0,0,0,0,0,-1.870674133300781,0,0.172149658203125,0,0.1840744018554688,0,0.19378662109375,0.2122726440429688,0,0.2279434204101562,0,0.236602783203125,0.2348861694335938,0.2339096069335938,0,0.2309417724609375,0,0,0,0,0,0,0,0,-1.797515869140625,0.1762771606445312,0,0.1861343383789062,0,0,0.1760482788085938,0,0.2178878784179688,0,0.2290496826171875,0.237548828125,0,0.2346115112304688,0,0,0.2342376708984375,0.1606826782226562,0,0,0,-1.885421752929688,0,0.17156982421875,0,0,0.1815948486328125,0,0.1901092529296875,0.2100372314453125,0,0.2286529541015625,0.239349365234375,0.2148895263671875,0,0.2314071655273438,0.2330780029296875,0,0.038818359375,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.8046875,0.1378707885742188,0.1743011474609375,0,0.1888275146484375,0,0.2014312744140625,0,0.2226791381835938,0,0.233734130859375,0,0.2398757934570312,0,0.2373046875,0,0.221588134765625,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.831703186035156,0,0,0,0,0,0,0,0,0.11480712890625,0.1912155151367188,0,0.1953125,0,0,0.2125473022460938,0.22900390625,0.2340087890625,0,0.2218017578125,0,0.2104110717773438,0,0.2040863037109375,0,0.2242965698242188,0,0.2250213623046875,0.2322311401367188,0,0.2349395751953125,0,0.2313003540039062,0,0.2397384643554688,0,0.234619140625,0,0.231048583984375,0,0.2232589721679688,0.1885910034179688,0,0,0.1904067993164062,0,0.191253662109375,0,0,0.18792724609375,0,0.1923065185546875,0,0.1907424926757812,0,0.1928634643554688,0,0.1900482177734375,0,0,0.1933517456054688,0,0.1921615600585938,0,0.1930770874023438,0.1915512084960938,0.1933822631835938,0,0.1918563842773438,0.1933746337890625,0.1924972534179688,0.1903457641601562,0,0.1921920776367188,0.1906967163085938,0,0.084564208984375,0,0,0,0,0,0,0,0,-7.140853881835938,0,0.188751220703125,0.1959152221679688,0,0.210723876953125,0,0.2177658081054688,0,0.2236709594726562,0.216827392578125,0,0.2059555053710938,0,0.2303848266601562,0,0.22906494140625,0.227874755859375,0,0.2278366088867188,0,0.2286453247070312,0.2284469604492188,0,0.2282638549804688,0,0.2285308837890625,0.2278823852539062,0,0.226715087890625,0,0.2309112548828125,0.2313461303710938,0.2312088012695312,0.230224609375,0,0.229522705078125,0.2288894653320312,0.228118896484375,0.2530364990234375,0.2303466796875,0,0.2302780151367188,0,0.2285919189453125,0,0.229156494140625,0,0.2306365966796875,0,0.2186050415039062,0,0.214935302734375,0,0.1599273681640625,0,0,0,0,0,0,0,-6.999176025390625,0,0,0.1916656494140625,0,0.1439971923828125,0,0.1416244506835938,0,0.208648681640625,0,0,0.1858291625976562,0,0,0.1865081787109375,0,0.1793594360351562,0,0,0.1807174682617188,0,0.1974105834960938,0.1935501098632812,0.1954803466796875,0.2039413452148438,0,0,0.1961441040039062,0,0.20635986328125,0,0.20660400390625,0.208099365234375,0,0.2150802612304688,0,0.2032089233398438,0,0.2122879028320312,0.2076873779296875,0.2106781005859375,0.232330322265625,0,0.2008132934570312,0.191070556640625,0,0.2007217407226562,0,0,0.1984405517578125,0.2116241455078125,0.1974258422851562,0,0.20355224609375,0,0.2105560302734375,0.1972732543945312,0,0.2121429443359375,0,0,0.192138671875,0,0.2104034423828125,0,0,0.2106704711914062,0.219390869140625,0,0.040679931640625,0,0,0,0,0,-6.949172973632812,0,0,0.1786117553710938,0,0.1902542114257812,0,0.195648193359375,0,0,0.2012405395507812,0,0.2044906616210938,0,0.19927978515625,0,0.2116775512695312,0,0.218658447265625,0.2328414916992188,0,0.2280807495117188,0,0.2310867309570312,0,0.2282943725585938,0,0.2310028076171875,0.2329559326171875,0,0.2332305908203125,0,0.2307281494140625,0.2305908203125,0,0.2307586669921875,0,0.23138427734375,0.2319183349609375,0.2561264038085938,0,0.2320098876953125,0,0.2319488525390625,0,0.232696533203125,0,0.230804443359375,0,0.2293472290039062,0.2307052612304688,0,0.2313308715820312,0.2313919067382812,0,0.2249679565429688,0,0.2217788696289062,0,0.2220001220703125,0,0,0.00283050537109375,0,0,0,0,0,0,0,0,-6.8355712890625,0,0.174407958984375,0,0,0.189056396484375,0.197235107421875,0.19207763671875,0,0.1921920776367188,0.1912002563476562,0.2177658081054688,0,0.245208740234375,0.2251358032226562,0.223175048828125,0,0,0.2307357788085938,0,0,0.2323074340820312,0,0.2331085205078125,0.2320938110351562,0,0.2335433959960938,0,0.232574462890625,0,0.2323074340820312,0,0.231597900390625,0,0.2321548461914062,0,0.232025146484375,0,0.2314224243164062,0,0,0.2322998046875,0.2318267822265625,0,0.232696533203125,0,0.1719894409179688,0,0.2281265258789062,0.226715087890625,0.2307205200195312,0,0.2289581298828125,0.2244720458984375,0,0.2207412719726562,0,0,0.2040634155273438,0,0,0,0,0,0,0,0,0,0,0,-6.684585571289062,0,0.1846542358398438,0,0.19512939453125,0,0.1941986083984375,0,0.193023681640625,0.1937637329101562,0,0.2202529907226562,0.2305755615234375,0,0.2332000732421875,0,0.2328033447265625,0,0.231109619140625,0,0.2317886352539062,0.2312774658203125,0.2308197021484375,0.23089599609375,0,0.2310638427734375,0.23046875,0,0.2303543090820312,0,0.2300949096679688,0.2303466796875,0,0.230865478515625,0.2307968139648438,0.23077392578125,0,0.2302932739257812,0.2363510131835938,0.2306900024414062,0,0.2320938110351562,0.2324447631835938,0.2315597534179688,0,0.2213363647460938,0,0.2198104858398438,0.1668472290039062,0,0,0,0,0,0,0,-6.605484008789062,0,0.1788330078125,0,0.1901931762695312,0.1882858276367188,0,0.187652587890625,0.1922531127929688,0.2170791625976562,0,0.2211227416992188,0,0,0.228607177734375,0,0.250946044921875,0,0.2276458740234375,0.2291183471679688,0,0.2286300659179688,0.2293701171875,0,0.2269363403320312,0.2287673950195312,0,0.2266998291015625,0,0.22625732421875,0,0.2249221801757812,0,0,0.2270584106445312,0,0.2288589477539062,0,0.2295379638671875,0.2299880981445312,0,0.23162841796875,0,0.2324905395507812,0,0.2327499389648438,0.2331390380859375,0,0.2325515747070312,0,0.2314834594726562,0.2243576049804688,0,0.2216644287109375,0,0.1386032104492188,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-6.582672119140625,0.1452407836914062,0.1790924072265625,0.1861801147460938,0.1854782104492188,0,0.1811294555664062,0,0.20989990234375,0.222564697265625,0.2245712280273438,0.2294464111328125,0,0.2295989990234375,0.2293243408203125,0.2280654907226562,0,0.22869873046875,0.229156494140625,0,0.2288360595703125,0,0.252471923828125,0,0,0.228302001953125,0,0,0.2279205322265625,0,0.22955322265625,0,0.229339599609375,0,0.2299041748046875,0.2301559448242188,0,0.2305755615234375,0,0.2304229736328125,0,0.2307281494140625,0,0.230926513671875,0,0.229888916015625,0,0.2320404052734375,0.224884033203125,0,0.2212753295898438,0,0.1757125854492188,0,0,0,0,0,0,0,0,0,0,0,-6.375167846679688,0,0.1819992065429688,0,0.1896591186523438,0,0.2039566040039062,0.1948394775390625,0.2185211181640625,0,0.2319717407226562,0,0.2323989868164062,0,0.228790283203125,0,0.2286758422851562,0.2276535034179688,0.227813720703125,0,0.211517333984375,0.2261428833007812,0,0.2268142700195312,0.2276611328125,0,0.2268753051757812,0,0.2273101806640625,0,0.227874755859375,0,0.22833251953125,0,0.2281036376953125,0,0.2290420532226562,0.2294692993164062,0,0.2286300659179688,0.2274322509765625,0,0.2304611206054688,0.2313766479492188,0,0.2319793701171875,0,0.2227020263671875,0,0.2225494384765625,0.1104888916015625,0,0,0,0,0,0,0,0,-6.344886779785156,0.1730194091796875,0.1853256225585938,0,0,0.1837234497070312,0,0.1868743896484375,0,0.2135391235351562,0,0.2255401611328125,0,0.2322769165039062,0,0.2029190063476562,0.2158432006835938,0.1720809936523438,0,0.2025146484375,0,0.2197113037109375,0,0.193572998046875,0,0.2077102661132812,0,0.2145919799804688,0.1916580200195312,0,0.207763671875,0,0,0.1854629516601562,0,0,0.2108993530273438,0,0.2100448608398438,0.2151565551757812,0,0,0.2246551513671875,0.2222747802734375,0,0.2288284301757812,0,0,0.226409912109375,0.2269973754882812,0.2253341674804688,0,0,0.2130050659179688,0,0.2207489013671875,0,0.2142562866210938,0,0.2144622802734375,0,0.060455322265625,0,0,0,0,0,-6.228805541992188,0.1750411987304688,0.182952880859375,0,0.177734375,0,0.1842727661132812,0,0.1927032470703125,0,0.1846084594726562,0,0.2119140625,0,0.205657958984375,0,0.2132415771484375,0,0,0.2198715209960938,0,0,0.2128524780273438,0,0.2253036499023438,0,0.2144317626953125,0,0.220916748046875,0,0.222625732421875,0.2243576049804688,0,0.2293167114257812,0,0,7.833168029785156,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7.62939453125,7.62939453125e-06,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,15.2587890625,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7.629417419433594,0,0,0,0,0,0,0,0.1149749755859375,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,15.28022003173828,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"filename":["<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,null,null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>","<expr>","<expr>",null,null,null,null,null,null,null,null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,null,null,null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,null,null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,null,null,null,null,null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,null,null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,"<expr>","<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null]},"interval":10,"files":[{"filename":"<expr>","content":"## Generate Large Random Dataset\nn <- 2e6\nx <- runif(n)\ny <- runif(n)\nz <- runif(n)\nXYZ <- cbind(x,y,z)\n\n## Inspect 4 equivalent `row mean` calculations \nprofvis::profvis({\n    m <- rowSums(XYZ)/ncol(XYZ)\n    m <- rowMeans(XYZ)\n    m <- apply(XYZ, 1, mean)\n    m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }\n})\n## rowSums(), colSums(), rowMeans(), and colMeans() are vectorised and fast.\n## for loop is not the slowest, but the ugliest.","normpath":"<expr>"}],"prof_output":"/tmp/RtmpEaQLXc/file32dc4d001fe1.prof","highlight":{"output":["^output\\$"],"gc":["^<GC>$"],"stacktrace":["^\\.\\.stacktraceo(n|ff)\\.\\.$"]},"split":"h"}},"evals":[],"jsHooks":[]}</script>
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
##  mean1(x, 0.5) 33.87672 34.02311 35.56879 34.07123 37.28101 42.53914   100  a 
##  mean2(x, 0.5) 32.33560 32.64641 33.95854 32.69281 35.84514 41.11650   100   b
##  mean3(x, 0.5) 33.29995 33.98965 35.08249 34.02877 36.98335 42.94890   100  a
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
##  ma1(y) 274.07062 281.11096 291.05473 282.90383 294.86264 519.0745   100  a 
##  ma2(y)  26.51874  28.45913  35.54766  31.73592  35.33874 221.4850   100   b
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
##   0.120   0.000   0.043
```

```r
system.time({ lm(Y~X, data=DAT) })
```

```
##    user  system elapsed 
##   0.526   0.030   0.227
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
##   0.037   0.003   0.040
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
##   1.421   0.282   0.970
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

