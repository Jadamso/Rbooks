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
<div class="plotly html-widget html-fill-item" id="htmlwidget-df91e9381b6bc3f455ac" style="width:672px;height:480px;"></div>
<script type="application/json" data-for="htmlwidget-df91e9381b6bc3f455ac">{"x":{"visdat":{"35f9dc4891e":["function () ","plotlyVisDat"]},"cur_data":"35f9dc4891e","attrs":{"35f9dc4891e":{"x":{},"y":{},"alpha_stroke":1,"sizes":[10,100],"spans":[1,20]}},"layout":{"margin":{"b":40,"l":60,"t":25,"r":10},"xaxis":{"domain":[0,1],"automargin":true,"title":"X"},"yaxis":{"domain":[0,1],"automargin":true,"title":"Y"},"hovermode":"closest","showlegend":false},"source":"A","config":{"modeBarButtonsToAdd":["hoverclosest","hovercompare"],"showSendToCloud":false},"data":[{"x":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100],"y":[5.7807055124744968,9.5881722613343481,8.8007417284031728,14.47611624380362,23.942463680331105,24.338927393380633,27.701341301048558,29.610584187908838,34.239779196898965,43.783441309273144,47.50855419183597,49.652310541202148,53.654985212001662,56.16137798931959,61.660667121783888,62.115438231645605,74.537039163239115,71.469259277865731,78.119564219218063,81.493473683874285,85.784805514638677,86.419820118467669,93.479173854445364,99.921023751168946,102.27422920854814,100.4341569407343,107.21070364566873,116.51542014791026,116.23652300474181,119.71100524665249,124.53533031052599,125.30911196153623,132.36934593407051,134.52324667076121,139.5753583813291,145.31791435715962,148.60638105850862,148.36120142876689,157.98079463574535,160.21885907622922,162.34618415294622,167.12774227406459,175.86969283871179,177.41554468714526,180.3448340426047,183.63157909010653,185.89176178130896,194.20842959413051,194.17751150080932,200.08131478818612,203.57178938859445,203.36989560016255,211.07124181771925,212.44316127297085,218.70074024438622,222.08552685310025,227.8249292567798,231.0577170770955,235.16670630986354,240.1698184416064,245.60033662634018,247.29087860840573,250.75560789392654,255.75721924144281,259.82027784217752,265.99281702871946,264.04956679721397,270.55275278846148,279.41638987396936,280.61543759957033,284.94835413058183,289.66506415915671,288.01870269041672,293.44881461737396,302.86079681910292,304.34464087461618,304.97265049175752,310.18885259190677,316.52758533590048,321.37270568383713,322.04778152920181,327.36476193127498,336.90964083067871,337.7817376970383,342.16110040814453,342.26632648027788,349.38593629135454,351.84600949295327,356.84942528842129,358.41981471920428,366.57936265007874,362.12996780048047,372.32616249036442,373.46161303078378,378.9501852556885,384.1724416636747,388.33113002843163,389.00461037995865,395.95729906843553,399.95312221963229],"type":"scatter","mode":"markers","marker":{"color":"rgba(31,119,180,1)","line":{"color":"rgba(31,119,180,1)"}},"error_y":{"color":"rgba(31,119,180,1)"},"error_x":{"color":"rgba(31,119,180,1)"},"line":{"color":"rgba(31,119,180,1)"},"xaxis":"x","yaxis":"y","frame":null}],"highlight":{"on":"plotly_click","persistent":false,"dynamic":false,"selectize":false,"opacityDim":0.20000000000000001,"selected":{"opacity":1},"debounce":0},"shinyEvents":["plotly_hover","plotly_click","plotly_selected","plotly_relayout","plotly_brushed","plotly_brushing","plotly_clickannotation","plotly_doubleclick","plotly_deselect","plotly_afterplot","plotly_sunburstclick"],"base_url":"https://plot.ly"},"evals":[],"jsHooks":[]}</script>
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
##   0.004   0.001   0.005
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
<div class="profvis html-widget html-fill-item" id="htmlwidget-f568b9df046d87774b80" style="width:100%;height:600px;"></div>
<script type="application/json" data-for="htmlwidget-f568b9df046d87774b80">{"x":{"message":{"prof":{"time":[1,2,3,4,5,6,7,8,9,9,9,10,10,11,11,12,12,13,13,14,14,15,15,16,16,17,17,18,18,19,19,20,20,21,21,22,22,22,23,23,24,25,25,26,27,28,29,30,31,31,32,33,33,34,34,35,36,36,37,37,38,38,39,39,40,40,41,42,42,43,43,44,44,44,45,46,47,47,48,49,50,50,51,51,52,53,53,54,54,55,55,55,56,57,57,58,58,59,59,60,60,61,61,62,62,63,63,64,64,65,65,65,66,66,67,67,68,69,69,70,71,71,72,72,73,74,74,74,75,75,76,76,77,77,78,78,79,79,80,80,81,81,82,82,83,84,84,85,85,86,86,87,88,88,88,89,89,90,91,91,92,92,93,94,94,95,96,96,97,97,98,99,99,100,100,101,101,102,103,103,104,104,104,105,105,106,107,107,108,108,109,109,110,110,111,112,112,112,113,114,115,116,117,117,118,118,119,119,119,120,120,121,121,122,122,123,123,124,125,125,126,126,127,127,128,128,129,129,130,131,131,132,132,133,133,134,134,135,135,135,135,136,136,136,137,137,138,138,139,140,140,141,142,142,143,143,143,144,144,145,145,146,146,147,147,148,148,149,149,150,150,150,151,152,152,153,154,155,155,156,157,157,158,158,159,159,160,160,161,162,162,163,163,163,164,164,165,165,166,166,167,167,168,168,169,169,170,170,171,171,171,172,173,173,173,174,175,175,176,176,177,178,179,179,180,180,180,181,181,182,183,183,184,185,185,186,186,187,187,187,188,188,188,189,189,189,190,190,190,191,191,191,192,192,192,193,193,193,194,194,194,195,195,195,196,197,198,199,199,200,200,201,202,202,203,203,204,204,205,205,206,206,206,207,207,208,209,209,209,210,210,211,211,212,213,213,214,215,215,215,216,216,216,217,218,218,218,219,220,220,221,221,221,222,222,223,223,223,224,225,225,226,226,227,227,228,229,229,230,231,231,232,232,232,233,234,234,234,235,235,236,237,237,238,239,239,239,240,241,241,241,242,242,243,243,244,244,245,245,246,246,247,247,248,248,248,249,249,249,250,250,251,252,252,252,253,254,254,255,255,256,257,257,257,258,258,259,259,260,260,260,261,261,262,262,263,263,264,264,265,265,265,266,266,266,267,268,269,269,270,271,272,272,272,273,273,274,274,275,276,276,277,277,278,279,279,279,280,280,281,281,282,282,283,283,284,285,285,285,286,287,287,288,288,289,289,290,290,291,291,292,292,292,293,293,294,295,295,296,296,297,297,298,298,299,300,300,301,302,303,303,304,304,304,305,305,306,306,307,307,308,308,309,309,310,310,310,311,311,312,313,313,314,315,315,316,316,316,317,317,317,318,318,319,320,320,321,321,322,322,322,322,323,323,323,323,324,324,325,325,326,327,327,328,328,329,329,330,330,331,331,331,332,333,334,334,334,335,335,335,336,336,336,337,337,337,338,338,338,339,339,339,340,340,340,341,341,341,342,342,342,343,343,343,344,344,344,345,345,345,346,346,346,347,347,347,348,348,348,349,349,349,350,350,350,351,351,351,352,352,352,353,353,353,354,354,354,355,355,355,356,356,356,357,357,357,358,358,358,359,359,360,361,361,362,362,363,364,365,366,366,367,368,368,369,370,370,371,371,372,372,373,373,374,374,374,375,375,376,376,377,377,377,378,378,379,379,380,380,381,382,383,383,384,384,385,385,386,387,387,388,388,389,389,390,390,391,391,392,392,393,393,394,394,395,396,396,397,397,398,399,400,401,401,402,402,403,404,404,405,405,405,406,407,408,409,409,409,410,410,411,412,412,413,413,413,414,414,415,415,415,416,417,418,418,419,419,420,421,421,422,423,424,424,425,425,426,426,427,427,427,428,428,429,429,430,430,431,431,432,432,433,433,434,435,436,436,437,438,438,439,439,440,440,441,441,442,442,442,443,443,443,444,445,446,446,447,447,448,449,450,450,451,451,452,452,453,453,454,454,455,455,455,456,456,457,457,457,458,459,459,460,461,461,462,463,463,464,465,466,467,467,467,468,468,469,469,470,471,471,472,473,474,475,475,476,476,476,477,478,478,479,479,480,481,481,482,482,483,483,484,484,485,485,486,486,487,487,488,488,489,490,491,491,492,492,493,493,494,495,495,495,496,496,496,497,498,498,499,500,500,501,501,502,502,503,504,505,506,507,507,508,508,508,509,509,509,510,510,511,511,512,512,513,514,514,515,515,516,517,518,518,519,519,520,521,521,522,522,523,524,524,525,526,526,527,528,529,529,530,530,531,531,532,532,533,533,533,534,534,534,535,535,535,536,536,537,538,539,539,540,540,541,541,542,543,543,544,544,545,546,546,547,547,547,548,548,549,550,551,551,551,552,553,553,553,554,554,555,555,555,556,556,557,557,558,558,559,559,559,560,560,560,561,561,562,562,563,563,564,565,565,565,566,566,567,568,569,569,570,571,571,571,572,572,572,573,574,574,575,575,576,577,577,578,579,580,580,581,581,582,582,583,584,584,584,585,586,586,587,588,588,589,589,590,590,590,591,591,592,592,592,593,594,595,595,596,596,596,597,597,597,598,599,600,600,601,602,603,604,605,605,606,607,608,608,608,609,609,609,610,610,611,611,611,612,613,613,614,615,616,616,616,617,618,619,619,619,620,620,620,621,621,621,622,622,623,624,625,626,626,627,628,628,629,629,630,630,631,631,632,632,633,633,634,634,635,635,636,636,637,637,638,638,639,639,640,640,641,641,642,642,643,643,644,644,645,645,646,647,648,649,649,650,650,651,651,651,652,652,653,653,654,654,654,655,655,656,656,656,657,657,657,658,658,658,659,659,660,661,662,662,663,664,665,665,665,666,666,667,668,668,668,669,669,670,670,671,671,672,673,674,674,675,676,677,677,678,679,679,679,680,680,680,681,681,682,682,683,683,684,685,686,686,687,687,688,688,689,689,690,690,691,691,691,692,692,693,694,694,695,695,696,696,697,697,698,698,699,699,700,700,700,701,701,702,702,702,702,703,703,703,703,704,705,706,706,707,708,708,709,709,710,710,711,711,712,712,713,713,713,714,714,714,715,715,716,716,717,717,718,718,719,719,719,720,721,721,722,722,723,724,724,725,725,726,726,727,728,728,729,729,730,731,731,732,732,733,733,734,735,735,735,736,736,736,737,737,738,738,739,739,740,741,741,742,742,743,743,744,744,745,746,746,747,747,748,748,749,750,751,751,752,752,753,753,754,755,755,756,757,757,757,758,758,758,759,759,760,761,761,761,762,762,763,763,763,764,765,765,766,767,767,767,768,768,768,769,769,769,770,771,771,772,772,772,773,773,774,774,775,775,776,777,777,777,778,778,779,779,780,781,781,782,782,783,783,784,784,785,785,786,787,787,788,788,789,789,789,790,790,790,791,791,792,793,793,794,794,795,795,796,796,797,797,798,798,799,799,799,800,800,800,801,801,802,802,803,804,804,805,805,806,807,808,808,809,810,810,810,811,812,812,813,813,814,815,815,816,816,817,818,819,819,820,820,821,822,822,823,824,824,825,825,826,826,827,828,828,829,830,830,830,830,831,831,832,832,833,833,833,834,835,835,836,836,837,837,838,839,839,840,840,841,841,842,843,843,844,845,846,846,847,847,848,848,849,849,850,850,851,851,852,853,854,854,855,856,856,857,858,858,858,859,859,860,860,861,861,862,862,863,863,864,864,865,866,866,867,868,868,869,869,870,870,871,871,872,872,873,873,874,874,875,875,876,876,877,877,878,878,879,879,880,880,881,881,882,883,883,884,884,885,885,886,887,887,887,888,888,889,889,890,890,891,891,892,893,893,894,894,895,895,895,896,896,897,898,898,898,899,899,899,900,900,901,901,902,902,903,903,903,904,904,905,905,906,906,907,907,907,908,908,908,909,909,910,910,910,911,912,913,914,915,915,916,916,917,917,917,918,918,918,919,919,920,920,921,921,922,923,923,924,924,925,925,926,926,926,927,927,927,928,928,929,929,930,930,931,931,932,932,932,933,933,934,934,935,935,935,936,936,936,937,937,938,938,939,940,940,941,941,942,942,943,943,944,944,945,945,946,946,947,947,948,948,949,949,950,950,951,952,953,953,953,954,954,954,955,956,956,957,958,958,959,959,960,960,960,961,961,962,962,962,962,963,963,963,963,964,964,965,965,965,966,966,967,968,969,969,970,970,971,971,971,972,972,972,973,973,974,975,975,975,976,977,978,978,979,979,980,980,980,981,981,981,982,983,983,984,984,985,985,985,986,987,988,988,988,989,989,989,990,991,991,992,992,993,993,994,995,995,996,996,997,997,997,998,998,998,999,999,1000,1000,1001,1002,1002,1003,1003,1003,1004,1005,1005,1005,1006,1006,1006,1007,1007,1008,1008,1009,1009,1009,1010,1011,1012,1012,1013,1014,1014,1015,1015,1016,1016,1017,1017,1018,1018,1019,1019,1020,1020,1021,1022,1022,1023,1023,1024,1024,1025,1025,1026,1026,1027,1027,1028,1028,1029,1029,1030,1030,1031,1031,1032,1032,1033,1033,1034,1034,1035,1035,1036,1036,1037,1037,1038,1038,1039,1039,1040,1040,1041,1041,1042,1042,1043,1043,1044,1044,1045,1045,1046,1046,1047,1047,1048,1048,1049,1049,1050,1050,1051,1051,1052,1052,1053,1053,1054,1054,1055,1055,1056,1056,1057,1057,1058,1058,1059,1059,1060,1060,1061,1061,1062,1062,1063,1063,1064,1064,1065,1065,1066,1066,1067,1067,1068,1068,1069,1069,1070,1070,1071,1071,1072,1072,1073,1073,1074,1074,1075,1075,1076,1076,1077,1077,1078,1078,1079,1079,1080,1081,1082,1082,1083,1084,1085,1085,1086,1086,1087,1087,1088,1088,1089,1090,1091,1092,1093,1094,1094,1095,1095,1096,1097,1097,1097,1098,1098,1099,1100,1101,1101,1101,1102,1102,1102,1103,1103,1103,1104,1104,1105,1105,1105,1106,1106,1107,1107,1108,1109,1110,1111,1112,1112,1113,1113,1113,1114,1114,1115,1116,1116,1117,1117,1118,1118,1119,1119,1120,1120,1120,1121,1121,1122,1123,1123,1124,1124,1125,1125,1125,1126,1126,1126,1127,1128,1128,1129,1129,1130,1130,1131,1131,1132,1132,1133,1133,1134,1134,1134,1135,1135,1135,1136,1136,1137,1137,1138,1138,1139,1139,1140,1140,1141,1142,1142,1142,1143,1143,1143,1144,1145,1146,1146,1146,1147,1147,1147,1147,1148,1148,1148,1148,1149,1149,1150,1150,1151,1151,1152,1152,1153,1154,1154,1155,1155,1155,1156,1156,1157,1157,1158,1158,1158,1159,1159,1160,1160,1161,1162,1163,1164,1164,1165,1166,1166,1167,1167,1168,1168,1169,1169,1170,1170,1171,1171,1172,1173,1173,1174,1174,1175,1175,1176,1176,1177,1178,1178,1179,1180,1180,1181,1181,1182,1183,1184,1185,1185,1186,1186,1187,1187,1187,1188,1188,1189,1189,1189,1190,1190,1191,1191,1191,1192,1192,1192,1193,1193,1193,1194,1194,1194,1195,1196,1196,1197,1197,1198,1198,1199,1200,1200,1201,1201,1202,1202,1203,1204,1204,1205,1205,1206,1206,1207,1207,1208,1208,1209,1209,1210,1210,1211,1211,1212,1213,1213,1213,1214,1214,1214,1215,1215,1215,1216,1217,1217,1218,1218,1219,1220,1221,1221,1222,1222,1223,1223,1223,1224,1224,1225,1226,1226,1227,1227,1228,1228,1228,1229,1229,1230,1231,1232,1232,1233,1233,1234,1234,1234,1235,1235,1235,1236,1236,1236,1237,1237,1237,1238,1238,1238,1239,1239,1239,1240,1240,1240,1241,1241,1241,1242,1242,1242,1243,1243,1244,1244,1245,1245,1246,1246,1247,1247,1248,1248,1249,1250,1251,1251,1252,1252,1252,1253,1254,1255,1255,1256,1256,1257,1257,1258,1259,1259,1260,1260,1261,1261,1262,1262,1262,1263,1263,1263,1264,1264,1264,1265,1266,1266,1267,1268,1269,1269,1270,1271,1271,1272,1272,1273,1274,1275,1276,1276,1277,1277,1278,1278,1279,1280,1280,1281,1281,1282,1282,1283,1283,1284,1284,1285,1285,1286,1286,1287,1287,1288,1288,1289,1289,1290,1290,1291,1291,1292,1292,1293,1294,1294,1295,1296,1297,1297,1297,1298,1298,1299,1300,1300,1301,1301,1302,1302,1302,1303,1303,1304,1304,1304,1305,1305,1305,1306,1306,1306,1307,1307,1308,1308,1309,1310,1311,1311,1312,1313,1313,1314,1314,1315,1315,1316,1317,1317,1318,1318,1319,1319,1320,1320,1321,1321,1322,1322,1323,1323,1324,1324,1325,1325,1326,1326,1327,1327,1328,1329,1329,1330,1330,1331,1331,1332,1332,1333,1333,1334,1334,1335,1335,1336,1336,1337,1337,1338,1338,1339,1339,1340,1340,1341,1341,1342,1342,1343,1343,1344,1344,1345,1345,1346,1346,1347,1347,1348,1348,1349,1349,1349,1349,1349,1349,1349,1349,1350,1350,1350,1350,1350,1350,1350,1350,1350,1350,1350,1350,1350,1350,1350,1350,1350,1350,1350,1350,1350,1350,1350,1350,1350,1350,1350,1350,1350,1350,1350,1350,1350,1350,1350,1350,1351,1351,1351,1351,1351,1351,1351,1351,1352,1352,1352,1352,1352,1352,1352,1352,1353,1353,1353,1353,1353,1353,1353,1353,1354,1354,1354,1354,1354,1354,1354,1354,1355,1355,1355,1355,1355,1355,1355,1355,1356,1356,1356,1356,1356,1356,1356,1356,1357,1357,1357,1357,1357,1357,1357,1357,1358,1358,1358,1358,1358,1358,1358,1358,1359,1359,1359,1359,1359,1359,1359,1359,1360,1360,1360,1360,1360,1360,1360,1360,1361,1361,1361,1361,1361,1361,1361,1361,1362,1362,1362,1362,1362,1362,1362,1362,1363,1363,1363,1363,1363,1363,1363,1363,1364,1364,1364,1364,1364,1364,1364,1364,1365,1365,1365,1365,1365,1365,1365,1365,1366,1366,1366,1366,1366,1366,1366,1366,1367,1367,1367,1367,1367,1367,1367,1367,1368,1368,1368,1368,1368,1368,1368,1368],"depth":[1,1,1,1,1,1,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,1,1,1,1,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,1,1,2,1,1,1,2,1,2,1,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,1,2,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,3,2,1,2,1,1,2,1,2,1,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,1,3,2,1,1,1,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,4,3,2,1,3,2,1,2,1,2,1,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,1,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,3,2,1,1,2,1,2,1,1,1,2,1,3,2,1,2,1,1,2,1,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,1,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,3,2,1,2,1,2,1,1,2,1,1,3,2,1,3,2,1,1,3,2,1,1,2,1,3,2,1,2,1,3,2,1,1,2,1,2,1,2,1,1,2,1,1,2,1,3,2,1,1,3,2,1,2,1,1,2,1,1,3,2,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,1,3,2,1,1,2,1,2,1,1,3,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,1,1,2,1,1,1,3,2,1,2,1,2,1,1,2,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,1,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,4,3,2,1,4,3,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,1,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,1,1,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,1,1,2,1,2,1,1,2,1,3,2,1,1,1,1,3,2,1,2,1,1,2,1,3,2,1,2,1,3,2,1,1,1,2,1,2,1,1,2,1,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,1,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,3,2,1,1,2,1,1,2,1,1,2,1,1,1,1,3,2,1,2,1,2,1,1,2,1,1,1,1,2,1,3,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,1,3,2,1,3,2,1,1,2,1,1,2,1,2,1,2,1,1,1,1,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,1,1,2,1,2,1,1,2,1,2,1,1,2,1,1,2,1,1,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,1,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,3,2,1,2,1,1,1,3,2,1,1,3,2,1,2,1,3,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,3,2,1,2,1,1,1,2,1,1,3,2,1,3,2,1,1,2,1,2,1,1,2,1,1,1,2,1,2,1,2,1,1,3,2,1,1,2,1,1,2,1,2,1,3,2,1,2,1,3,2,1,1,1,2,1,3,2,1,3,2,1,1,1,2,1,1,1,1,1,2,1,1,1,3,2,1,3,2,1,2,1,3,2,1,1,2,1,1,1,3,2,1,1,1,3,2,1,3,2,1,3,2,1,2,1,1,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,1,2,1,2,1,3,2,1,2,1,2,1,3,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,1,1,2,1,1,1,3,2,1,2,1,1,3,2,1,2,1,2,1,2,1,1,1,2,1,1,1,2,1,1,3,2,1,3,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,4,3,2,1,4,3,2,1,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,1,2,1,1,3,2,1,3,2,1,2,1,1,3,2,1,2,1,3,2,1,1,2,1,1,3,2,1,3,2,1,3,2,1,1,2,1,3,2,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,2,1,1,1,2,1,1,3,2,1,1,2,1,2,1,1,2,1,2,1,1,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,1,2,1,1,4,3,2,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,1,3,2,1,3,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,3,2,1,1,1,1,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,3,2,1,3,2,1,1,2,1,1,2,1,2,1,3,2,1,2,1,4,3,2,1,4,3,2,1,2,1,3,2,1,2,1,1,1,2,1,2,1,3,2,1,3,2,1,2,1,1,3,2,1,1,1,2,1,2,1,3,2,1,3,2,1,1,2,1,2,1,3,2,1,1,1,3,2,1,3,2,1,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,3,2,1,1,3,2,1,3,2,1,2,1,2,1,3,2,1,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,1,1,2,1,2,1,2,1,2,1,1,1,1,1,1,2,1,2,1,1,3,2,1,2,1,1,1,3,2,1,3,2,1,3,2,1,2,1,3,2,1,2,1,2,1,1,1,1,1,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,1,1,3,2,1,4,3,2,1,4,3,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,2,1,2,1,3,2,1,2,1,2,1,1,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,1,1,1,2,1,2,1,3,2,1,2,1,3,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,3,2,1,1,2,1,2,1,1,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,3,2,1,2,1,1,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,3,2,1,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,1,2,1,1,1,2,1,1,2,1,2,1,1,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,1,3,2,1,2,1,1,2,1,2,1,3,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,1,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,8,7,6,5,4,3,2,1,36,35,34,33,32,31,30,29,28,27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1],"label":["rowSums","rowSums","rowSums","rowSums","rowMeans","rowMeans","rowMeans","rowMeans","<GC>","aperm.default","apply","aperm.default","apply","aperm.default","apply","aperm.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","apply","apply","apply","apply","apply","<GC>","apply","apply","FUN","apply","is.numeric","local","apply","mean.default","apply","FUN","apply","FUN","apply","<GC>","apply","FUN","apply","apply","FUN","apply","length","local","isTRUE","mean.default","apply","apply","apply","<GC>","apply","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","is.numeric","local","<GC>","FUN","apply","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","length","local","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","apply","length","local","apply","FUN","apply","length","local","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","<GC>","apply","is.na","local","FUN","apply","apply","mean.default","apply","FUN","apply","FUN","apply","apply","<GC>","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","length","local","apply","<GC>","apply","length","local","apply","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","<GC>","FUN","apply","is.na","local","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","<GC>","mean.default","apply","apply","apply","apply","apply","FUN","apply","is.na","local","<GC>","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","mean.default","apply","<GC>","apply","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","<GC>","isTRUE","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","apply","mean.default","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","<GC>","FUN","apply","apply","FUN","apply","apply","apply","FUN","apply","apply","is.numeric","local","<GC>","apply","mean.default","apply","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","apply","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","<GC>","FUN","apply","apply","is.numeric","local","FUN","apply","apply","apply","FUN","apply","<GC>","is.na","local","mean.default","apply","apply","FUN","apply","apply","is.numeric","local","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","apply","apply","FUN","apply","mean.default","apply","apply","FUN","apply","<GC>","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","apply","apply","FUN","apply","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","<GC>","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","length","local","isTRUE","mean.default","apply","apply","<GC>","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","apply","mean.default","apply","<GC>","mean.default","apply","apply","isTRUE","mean.default","apply","is.numeric","local","apply","FUN","apply","apply","<GC>","mean.default","apply","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","<GC>","apply","<GC>","apply","mean.default","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","length","local","apply","<GC>","FUN","apply","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","length","local","<GC>","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","apply","FUN","apply","apply","apply","<GC>","is.na","local","mean.default","apply","is.numeric","local","apply","mean.default","apply","FUN","apply","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","<GC>","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","<GC>","FUN","apply","FUN","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","<GC>","apply","apply","mean.default","apply","apply","apply","FUN","apply","<GC>","mean.default","apply","length","local","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","is.numeric","local","apply","FUN","apply","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","is.na","local","FUN","apply","apply","mean.default","apply","<GC>","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","apply","apply","<GC>","is.na","local","<GC>","is.na","local","<GC>","is.na","local","<GC>","is.na","local","<GC>","is.na","local","<GC>","is.na","local","<GC>","is.na","local","<GC>","is.na","local","<GC>","is.na","local","<GC>","is.na","local","<GC>","is.na","local","<GC>","is.na","local","<GC>","is.na","local","<GC>","is.na","local","<GC>","is.na","local","<GC>","is.na","local","<GC>","is.na","local","<GC>","is.na","local","<GC>","is.na","local","<GC>","is.na","local","<GC>","is.na","local","<GC>","is.na","local","<GC>","is.na","local","<GC>","is.na","local","<GC>","is.na","local","FUN","apply","apply","FUN","apply","FUN","apply","apply","apply","apply","mean.default","apply","apply","FUN","apply","apply","length","local","FUN","apply","mean.default","apply","length","local","<GC>","FUN","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","is.numeric","local","mean.default","apply","apply","apply","FUN","apply","mean.default","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","length","local","FUN","apply","apply","is.numeric","local","length","local","apply","apply","apply","<GC>","apply","<GC>","apply","apply","mean.default","apply","isTRUE","mean.default","apply","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","<GC>","is.numeric","local","apply","apply","mean.default","apply","mean.default","apply","apply","is.numeric","local","apply","apply","FUN","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","<GC>","apply","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","length","local","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","FUN","apply","apply","FUN","apply","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","apply","apply","mean.default","apply","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","apply","length","local","mean.default","apply","apply","mean.default","apply","<GC>","apply","<GC>","apply","mean.default","apply","length","local","is.na","local","mean.default","apply","mean.default","apply","apply","apply","FUN","apply","mean.default","apply","FUN","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","FUN","apply","apply","length","local","is.numeric","local","mean.default","apply","apply","apply","apply","apply","length","local","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","is.numeric","local","length","local","apply","FUN","apply","FUN","apply","apply","apply","mean.default","apply","length","local","apply","<GC>","apply","<GC>","apply","apply","FUN","apply","apply","mean.default","apply","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","apply","apply","FUN","apply","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","mean.default","apply","<GC>","FUN","apply","mean.default","apply","apply","apply","isTRUE","mean.default","apply","apply","isTRUE","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","is.na","local","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","FUN","apply","is.na","local","apply","isTRUE","mean.default","apply","length","local","apply","apply","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","is.numeric","local","FUN","apply","apply","FUN","apply","apply","apply","is.na","local","FUN","apply","mean.default","apply","apply","<GC>","FUN","apply","apply","FUN","apply","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","apply","FUN","apply","apply","apply","apply","apply","FUN","apply","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","apply","is.numeric","local","apply","apply","isTRUE","mean.default","apply","apply","apply","isTRUE","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","apply","apply","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","is.na","local","mean.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","is.numeric","local","apply","apply","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","isTRUE","mean.default","apply","is.na","local","apply","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","apply","<GC>","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","apply","mean.default","apply","apply","apply","mean.default","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","is.numeric","local","FUN","apply","apply","apply","FUN","apply","is.na","local","mean.default","apply","mean.default","apply","is.numeric","local","<GC>","length","local","FUN","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","length","local","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","apply","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","length","local","FUN","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","mean.default","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","mean.default","apply","apply","mean.default","apply","mean.default","apply","apply","mean.default","apply","is.numeric","local","is.numeric","local","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","is.numeric","local","mean.default","apply","FUN","apply","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","<GC>","apply","<GC>","apply","FUN","apply","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","apply","isTRUE","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","apply","mean.default","apply","apply","isTRUE","mean.default","apply","<GC>","length","local","<GC>","length","local","apply","is.na","local","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","<GC>","apply","<GC>","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","length","local","length","local","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","apply","is.numeric","local","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","apply","mean.default","apply","apply","<GC>","is.na","local","apply","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","<GC>","apply","apply","mean.default","apply","apply","mean.default","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","apply","<GC>","isTRUE","mean.default","apply","is.na","local","FUN","apply","isTRUE","mean.default","apply","apply","mean.default","apply","is.numeric","local","mean.default","apply","apply","FUN","apply","<GC>","apply","<GC>","apply","apply","FUN","apply","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","<GC>","apply","FUN","apply","apply","apply","FUN","apply","apply","FUN","apply","apply","isTRUE","mean.default","apply","<GC>","apply","<GC>","apply","mean.default","apply","is.na","local","FUN","apply","FUN","apply","apply","mean.default","apply","apply","FUN","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","is.numeric","local","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","apply","apply","FUN","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","mean.default","apply","is.na","local","FUN","apply","isTRUE","mean.default","apply","FUN","apply","is.na","local","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","length","local","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","<GC>","apply","<GC>","apply","length","local","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","apply","apply","<GC>","is.numeric","local","<GC>","is.numeric","local","apply","FUN","apply","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","mean.default","apply","mean.default","apply","<GC>","length","local","<GC>","length","local","FUN","apply","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","apply","apply","<GC>","length","local","<GC>","length","local","apply","FUN","apply","FUN","apply","mean.default","apply","apply","is.numeric","local","FUN","apply","<GC>","length","local","<GC>","length","local","FUN","apply","mean.default","apply","apply","is.na","local","isTRUE","mean.default","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","is.na","local","isTRUE","mean.default","apply","apply","apply","mean.default","apply","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","apply","FUN","apply","FUN","apply","length","local","FUN","apply","mean.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","apply","apply","FUN","apply","apply","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","apply","apply","apply","apply","apply","mean.default","apply","mean.default","apply","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","length","local","isTRUE","mean.default","apply","FUN","apply","FUN","apply","apply","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","is.numeric","local","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","apply","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","apply","is.numeric","local","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","apply","apply","apply","is.na","local","apply","mean.default","apply","FUN","apply","is.na","local","<GC>","apply","<GC>","apply","<GC>","apply","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","mean.default","apply","apply","mean.default","apply","is.na","local","apply","apply","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","length","local","is.numeric","local","apply","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","is.na","local","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","mean.default","apply","length","local","isTRUE","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","length","local","mean.default","apply","FUN","apply","FUN","apply","apply","apply","length","local","isTRUE","mean.default","apply","apply","apply","FUN","apply","FUN","apply","mean.default","apply","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","apply","apply","mean.default","apply","apply","FUN","apply","FUN","apply","apply","apply","apply","FUN","apply","mean.default","apply","length","local","apply","mean.default","apply","is.numeric","local","FUN","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","<GC>","length","local","<GC>","length","local","<GC>","length","local","FUN","apply","FUN","apply","apply","apply","mean.default","apply","apply","mean.default","apply","length","local","mean.default","apply","apply","FUN","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","findCenvVar","getInlineInfo","tryInline","cmpCall","cmp","cmpPrim2","h","tryInline","cmpCall","cmp","h","tryInline","cmpCall","cmp","cmpPrim2","h","tryInline","cmpCall","cmp","cmpComplexAssign","h","tryInline","cmpCall","cmp","h","tryInline","cmpCall","cmp","cmpForBody","h","tryInline","cmpCall","cmp","genCode","compile","compiler:::tryCompile","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis"],"filenum":[1,1,1,1,1,1,1,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,1,null,1,1,1,1,1,1,null,1,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,null,null,null,1,1,1,null,1,1,1,null,1,null,1,1,null,1,null,null,null,null,1,1,null,1,null,1,null,1,null,1,null,1,null,null,null,1,null,1,null,null,1,null,1,null,1,1,null,null,1,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,null,1,1,null,1,null,1,null,1,1,null,null,1,null,1,1,null,1,null,1,1,null,null,1,null,1,null,null,1,null,1,null,1,null,1,1,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,1,null,null,1,1,1,1,1,null,1,null,null,null,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,null,null,1,null,null,1,null,1,null,1,1,null,1,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,1,null,1,1,1,null,1,1,null,null,null,1,null,1,null,1,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,1,null,null,1,1,null,null,null,1,1,1,null,1,null,null,null,null,1,1,null,1,1,null,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,1,1,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,null,1,null,1,1,null,null,1,null,1,null,1,1,null,1,1,null,null,1,null,null,1,1,null,null,1,1,null,1,null,null,1,null,null,null,null,1,1,null,1,null,1,null,1,1,null,1,1,null,1,null,null,1,1,null,null,1,null,null,1,null,1,1,null,null,1,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,1,null,1,null,1,1,null,null,1,null,null,null,1,null,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,1,1,null,1,1,1,null,null,null,null,1,null,null,1,null,1,null,1,1,null,null,1,null,1,null,1,null,1,null,1,1,null,null,1,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,1,null,1,null,1,null,1,null,1,1,null,1,1,1,null,1,null,null,1,null,null,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,1,1,null,1,null,null,1,null,null,1,null,1,1,null,1,null,1,null,null,null,1,null,null,null,1,null,null,null,1,1,null,1,null,1,null,1,null,1,null,null,1,1,1,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,1,1,null,1,null,1,1,1,1,null,1,1,null,1,1,null,null,null,1,null,1,null,null,null,null,1,null,1,null,1,null,null,1,null,1,null,null,null,1,1,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,null,1,1,null,null,null,null,1,1,1,null,1,null,1,1,null,1,null,null,1,1,1,1,null,null,1,null,1,1,null,1,null,null,1,null,1,null,null,null,1,1,null,1,null,1,1,null,null,1,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,1,null,1,1,null,1,null,1,null,1,null,null,null,null,1,null,null,1,1,1,null,1,null,1,1,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,null,1,1,null,1,1,null,1,1,null,1,1,1,1,null,null,1,null,1,null,1,1,null,1,1,1,1,null,1,null,null,1,1,null,null,null,1,1,null,1,null,1,null,1,null,1,null,null,null,null,null,1,null,1,1,1,null,1,null,1,null,1,1,null,null,1,null,null,1,1,null,1,1,null,null,null,null,null,1,1,1,1,1,null,null,null,null,1,null,null,1,null,1,null,null,null,null,1,null,1,null,1,1,1,null,1,null,null,1,null,1,null,1,1,null,1,1,null,1,1,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,1,1,1,null,1,null,1,null,1,1,null,1,null,1,1,null,1,null,null,1,null,1,1,1,null,null,1,1,null,null,1,null,1,null,null,1,null,1,null,null,null,1,null,null,1,null,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,1,null,1,1,null,null,1,null,null,1,1,null,null,null,1,1,null,1,1,1,null,null,null,1,null,1,1,null,null,1,1,null,1,1,null,1,null,1,null,null,1,null,1,null,null,1,1,1,null,1,null,null,1,null,null,1,1,1,null,1,1,1,1,1,null,1,1,1,null,null,1,null,null,1,null,1,null,null,1,1,null,null,1,1,null,null,1,1,1,null,null,1,null,null,1,null,null,1,null,1,1,1,1,null,1,1,null,1,null,1,null,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,1,1,null,1,null,1,null,null,1,null,1,null,1,null,null,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,1,null,1,1,1,null,null,1,null,1,1,null,null,1,null,1,null,1,null,1,1,1,null,1,1,1,null,1,1,null,null,1,null,null,1,null,1,null,null,null,1,1,1,null,1,null,null,null,1,null,1,null,null,null,null,null,null,1,1,null,1,null,1,null,1,null,null,null,1,null,1,null,null,1,null,1,null,null,null,1,null,null,null,1,1,1,null,1,1,null,1,null,1,null,null,null,1,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,null,null,1,1,null,1,null,1,1,null,1,null,1,null,1,1,null,1,null,1,1,null,1,null,null,null,null,1,null,null,1,null,null,1,null,null,null,1,null,1,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,1,1,null,1,null,1,null,1,1,null,1,1,null,null,1,null,null,1,null,1,1,null,null,1,null,1,null,null,1,1,null,1,1,null,null,1,null,null,null,null,null,null,1,null,null,null,null,1,null,1,null,1,null,1,1,null,null,1,null,1,null,1,1,null,1,null,1,null,1,null,null,null,null,1,null,1,null,1,null,null,1,null,null,1,null,1,1,null,null,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,1,null,1,1,null,1,null,1,1,1,null,1,1,null,null,null,1,null,1,null,1,1,null,1,null,1,1,1,null,1,null,1,1,null,1,1,null,1,null,1,null,1,1,null,1,1,null,null,null,1,null,null,null,1,null,null,1,1,null,1,null,null,null,1,1,null,1,null,1,null,1,1,null,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,1,1,null,1,1,null,1,1,null,null,1,null,1,null,1,null,1,null,null,null,1,null,1,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,null,1,1,null,1,null,1,null,1,1,null,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,null,1,null,1,1,null,null,1,null,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,1,null,null,1,1,1,1,1,null,1,null,1,null,null,1,null,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,null,1,null,null,1,null,1,null,1,null,null,null,1,null,null,1,null,1,null,null,null,null,1,null,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,null,1,null,1,null,1,null,1,1,1,null,null,null,null,null,null,1,null,1,1,null,1,null,1,null,null,1,null,1,null,null,null,1,null,null,null,1,null,1,null,null,1,null,1,1,1,null,1,null,1,null,null,null,null,null,null,null,1,1,null,null,1,1,1,null,1,null,1,null,null,1,null,null,1,1,null,1,null,1,null,null,1,1,1,null,null,null,null,null,null,1,null,1,null,1,null,1,1,null,null,null,1,null,null,null,null,null,null,null,1,null,1,1,null,null,null,null,1,1,null,null,1,null,null,1,null,1,null,null,null,null,1,1,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,1,null,1,1,1,null,1,null,1,null,1,null,1,1,1,1,1,1,null,1,null,1,1,null,null,1,null,1,1,1,null,null,1,null,null,1,null,null,1,null,null,null,null,1,null,1,null,1,1,1,1,1,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,1,null,1,null,1,null,null,1,null,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,1,null,null,1,null,null,1,1,1,null,null,1,null,null,null,1,null,null,null,1,null,1,null,1,null,1,null,1,1,null,null,null,null,1,null,1,null,1,null,null,1,null,1,null,1,1,1,1,null,null,1,null,1,null,1,null,null,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,1,null,1,1,null,1,null,null,1,1,1,null,1,null,1,null,null,1,null,1,null,null,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,1,null,1,null,1,null,1,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,null,1,null,null,1,null,null,1,1,null,null,null,null,1,1,null,1,null,1,null,null,1,null,null,1,null,1,null,1,null,null,1,null,1,1,1,null,1,null,null,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,null,null,1,null,1,null,1,1,1,null,null,null,null,1,1,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,1,null,1,1,1,null,1,1,null,1,null,1,1,1,1,null,1,null,1,null,null,1,null,1,null,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,1,1,null,null,1,null,1,1,null,1,null,1,null,null,1,null,1,null,null,null,null,null,null,null,null,null,null,1,null,1,1,1,null,1,1,null,1,null,null,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,1,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null],"linenum":[10,10,10,10,11,11,11,11,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,12,null,12,12,12,12,12,12,null,12,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,null,null,null,12,12,12,null,12,12,12,null,12,null,12,12,null,12,null,null,null,null,12,12,null,12,null,12,null,12,null,12,null,12,null,null,null,12,null,12,null,null,12,null,12,null,12,12,null,null,12,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,null,12,12,null,12,null,12,null,12,12,null,null,12,null,12,12,null,12,null,12,12,null,null,12,null,12,null,null,12,null,12,null,12,null,12,12,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,12,null,null,12,12,12,12,12,null,12,null,null,null,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,null,null,12,null,null,12,null,12,null,12,12,null,12,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,12,null,12,12,12,null,12,12,null,null,null,12,null,12,null,12,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,12,null,null,12,12,null,null,null,12,12,12,null,12,null,null,null,null,12,12,null,12,12,null,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,12,12,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,null,12,null,12,12,null,null,12,null,12,null,12,12,null,12,12,null,null,12,null,null,12,12,null,null,12,12,null,12,null,null,12,null,null,null,null,12,12,null,12,null,12,null,12,12,null,12,12,null,12,null,null,12,12,null,null,12,null,null,12,null,12,12,null,null,12,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,12,null,12,null,12,12,null,null,12,null,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,12,12,null,12,12,12,null,null,null,null,12,null,null,12,null,12,null,12,12,null,null,12,null,12,null,12,null,12,null,12,12,null,null,12,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,12,null,12,null,12,null,12,null,12,12,null,12,12,12,null,12,null,null,12,null,null,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,12,12,null,12,null,null,12,null,null,12,null,12,12,null,12,null,12,null,null,null,12,null,null,null,12,null,null,null,12,12,null,12,null,12,null,12,null,12,null,null,12,12,12,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,12,12,null,12,null,12,12,12,12,null,12,12,null,12,12,null,null,null,12,null,12,null,null,null,null,12,null,12,null,12,null,null,12,null,12,null,null,null,12,12,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,null,12,12,null,null,null,null,12,12,12,null,12,null,12,12,null,12,null,null,12,12,12,12,null,null,12,null,12,12,null,12,null,null,12,null,12,null,null,null,12,12,null,12,null,12,12,null,null,12,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,12,null,12,12,null,12,null,12,null,12,null,null,null,null,12,null,null,12,12,12,null,12,null,12,12,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,null,12,12,null,12,12,null,12,12,null,12,12,12,12,null,null,12,null,12,null,12,12,null,12,12,12,12,null,12,null,null,12,12,null,null,null,12,12,null,12,null,12,null,12,null,12,null,null,null,null,null,12,null,12,12,12,null,12,null,12,null,12,12,null,null,12,null,null,12,12,null,12,12,null,null,null,null,null,12,12,12,12,12,null,null,null,null,12,null,null,12,null,12,null,null,null,null,12,null,12,null,12,12,12,null,12,null,null,12,null,12,null,12,12,null,12,12,null,12,12,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,12,12,12,null,12,null,12,null,12,12,null,12,null,12,12,null,12,null,null,12,null,12,12,12,null,null,12,12,null,null,12,null,12,null,null,12,null,12,null,null,null,12,null,null,12,null,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,12,null,12,12,null,null,12,null,null,12,12,null,null,null,12,12,null,12,12,12,null,null,null,12,null,12,12,null,null,12,12,null,12,12,null,12,null,12,null,null,12,null,12,null,null,12,12,12,null,12,null,null,12,null,null,12,12,12,null,12,12,12,12,12,null,12,12,12,null,null,12,null,null,12,null,12,null,null,12,12,null,null,12,12,null,null,12,12,12,null,null,12,null,null,12,null,null,12,null,12,12,12,12,null,12,12,null,12,null,12,null,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,12,12,null,12,null,12,null,null,12,null,12,null,12,null,null,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,12,null,12,12,12,null,null,12,null,12,12,null,null,12,null,12,null,12,null,12,12,12,null,12,12,12,null,12,12,null,null,12,null,null,12,null,12,null,null,null,12,12,12,null,12,null,null,null,12,null,12,null,null,null,null,null,null,12,12,null,12,null,12,null,12,null,null,null,12,null,12,null,null,12,null,12,null,null,null,12,null,null,null,12,12,12,null,12,12,null,12,null,12,null,null,null,12,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,null,12,12,null,12,null,12,12,null,12,null,12,null,12,12,null,12,null,12,12,null,12,null,null,null,null,12,null,null,12,null,null,12,null,null,null,12,null,12,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,12,12,null,12,null,12,null,12,12,null,12,12,null,null,12,null,null,12,null,12,12,null,null,12,null,12,null,null,12,12,null,12,12,null,null,12,null,null,null,null,null,null,12,null,null,null,null,12,null,12,null,12,null,12,12,null,null,12,null,12,null,12,12,null,12,null,12,null,12,null,null,null,null,12,null,12,null,12,null,null,12,null,null,12,null,12,12,null,null,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,12,null,12,12,null,12,null,12,12,12,null,12,12,null,null,null,12,null,12,null,12,12,null,12,null,12,12,12,null,12,null,12,12,null,12,12,null,12,null,12,null,12,12,null,12,12,null,null,null,12,null,null,null,12,null,null,12,12,null,12,null,null,null,12,12,null,12,null,12,null,12,12,null,12,12,12,null,12,null,12,null,12,null,12,null,12,null,12,12,12,null,12,12,null,12,12,null,null,12,null,12,null,12,null,12,null,null,null,12,null,12,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,null,12,12,null,12,null,12,null,12,12,null,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,null,12,null,12,12,null,null,12,null,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,12,null,null,12,12,12,12,12,null,12,null,12,null,null,12,null,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,null,12,null,null,12,null,12,null,12,null,null,null,12,null,null,12,null,12,null,null,null,null,12,null,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,null,12,null,12,null,12,null,12,12,12,null,null,null,null,null,null,12,null,12,12,null,12,null,12,null,null,12,null,12,null,null,null,12,null,null,null,12,null,12,null,null,12,null,12,12,12,null,12,null,12,null,null,null,null,null,null,null,12,12,null,null,12,12,12,null,12,null,12,null,null,12,null,null,12,12,null,12,null,12,null,null,12,12,12,null,null,null,null,null,null,12,null,12,null,12,null,12,12,null,null,null,12,null,null,null,null,null,null,null,12,null,12,12,null,null,null,null,12,12,null,null,12,null,null,12,null,12,null,null,null,null,12,12,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,12,null,12,12,12,null,12,null,12,null,12,null,12,12,12,12,12,12,null,12,null,12,12,null,null,12,null,12,12,12,null,null,12,null,null,12,null,null,12,null,null,null,null,12,null,12,null,12,12,12,12,12,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,12,null,12,null,12,null,null,12,null,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,12,null,null,12,null,null,12,12,12,null,null,12,null,null,null,12,null,null,null,12,null,12,null,12,null,12,null,12,12,null,null,null,null,12,null,12,null,12,null,null,12,null,12,null,12,12,12,12,null,null,12,null,12,null,12,null,null,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,12,null,12,12,null,12,null,null,12,12,12,null,12,null,12,null,null,12,null,12,null,null,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,12,null,12,null,12,null,12,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,null,12,null,null,12,null,null,12,12,null,null,null,null,12,12,null,12,null,12,null,null,12,null,null,12,null,12,null,12,null,null,12,null,12,12,12,null,12,null,null,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,null,null,12,null,12,null,12,12,12,null,null,null,null,12,12,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,12,null,12,12,12,null,12,12,null,12,null,12,12,12,12,null,12,null,12,null,null,12,null,12,null,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,12,12,null,null,12,null,12,12,null,12,null,12,null,null,12,null,12,null,null,null,null,null,null,null,null,null,null,12,null,12,12,12,null,12,12,null,12,null,null,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,13,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,13,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null],"memalloc":[124.5359573364258,124.5359573364258,124.5359573364258,124.5359573364258,139.8181915283203,139.8181915283203,139.8181915283203,139.8181915283203,139.8185577392578,139.8185577392578,139.8185577392578,170.283935546875,170.283935546875,170.283935546875,170.283935546875,170.283935546875,170.283935546875,170.2839813232422,170.2839813232422,170.2839813232422,170.2839813232422,170.2839813232422,170.2839813232422,170.2839813232422,170.2839813232422,170.2839813232422,170.2839813232422,170.2839813232422,170.2839813232422,170.2839813232422,170.2839813232422,170.2839813232422,170.2839813232422,170.2836761474609,170.2836761474609,185.7102966308594,185.7102966308594,185.7102966308594,185.9617156982422,185.9617156982422,186.2321243286133,186.5474700927734,186.5474700927734,186.8955993652344,187.251708984375,187.6382827758789,188.0453186035156,188.4926071166992,188.6058578491211,188.6058578491211,186.0269546508789,186.4135971069336,186.4135971069336,186.8344192504883,186.8344192504883,187.2534790039062,187.659309387207,187.659309387207,188.0607757568359,188.0607757568359,188.4603500366211,188.4603500366211,188.670280456543,188.670280456543,186.0601959228516,186.0601959228516,186.4215545654297,186.8020935058594,186.8020935058594,187.2148590087891,187.2148590087891,187.6229934692383,187.6229934692383,187.6229934692383,188.0263900756836,188.4305801391602,188.7520751953125,188.7520751953125,186.0934524536133,186.446044921875,186.8200302124023,186.8200302124023,187.2222213745117,187.2222213745117,187.6273498535156,188.0299377441406,188.0299377441406,188.4340744018555,188.4340744018555,188.8325805664062,188.8325805664062,188.8325805664062,186.1468963623047,186.4965057373047,186.4965057373047,186.859375,186.859375,187.2470626831055,187.2470626831055,187.6520004272461,187.6520004272461,188.0542144775391,188.0542144775391,188.4542999267578,188.4542999267578,188.8573455810547,188.8573455810547,186.2128372192383,186.2128372192383,186.5691986083984,186.5691986083984,186.5691986083984,186.9327621459961,186.9327621459961,187.3170623779297,187.3170623779297,187.7218780517578,188.11376953125,188.11376953125,188.5133514404297,188.9150085449219,188.9150085449219,186.3093566894531,186.3093566894531,186.6587524414062,187.0138702392578,187.0138702392578,187.0138702392578,187.4258728027344,187.4258728027344,187.8264694213867,187.8264694213867,188.2174758911133,188.2174758911133,188.6068267822266,188.6068267822266,189.004264831543,189.004264831543,189.0662841796875,189.0662841796875,186.7502593994141,186.7502593994141,187.0997772216797,187.0997772216797,187.4640655517578,187.8548736572266,187.8548736572266,188.2489700317383,188.2489700317383,188.6366119384766,188.6366119384766,189.0324249267578,189.1418075561523,189.1418075561523,189.1418075561523,186.8420028686523,186.8420028686523,187.190673828125,187.5539245605469,187.5539245605469,187.9403076171875,187.9403076171875,188.3310470581055,188.7224578857422,188.7224578857422,189.1134872436523,189.2159652709961,189.2159652709961,186.9387054443359,186.9387054443359,187.2776031494141,187.6310043334961,187.6310043334961,187.9961166381836,187.9961166381836,188.3746032714844,188.3746032714844,188.7567901611328,189.1505584716797,189.1505584716797,189.2890090942383,189.2890090942383,189.2890090942383,187.0062408447266,187.0062408447266,187.3409118652344,187.6935577392578,187.6935577392578,188.0569763183594,188.0569763183594,188.4426574707031,188.4426574707031,188.8373184204102,188.8373184204102,189.2354583740234,189.3608093261719,189.3608093261719,189.3608093261719,187.1433715820312,187.4855422973633,187.8408126831055,188.2167510986328,188.6483535766602,188.6483535766602,189.0477676391602,189.0477676391602,189.4315185546875,189.4315185546875,189.4315185546875,187.0335540771484,187.0335540771484,187.3499145507812,187.3499145507812,187.6891250610352,187.6891250610352,188.0409545898438,188.0409545898438,188.4173355102539,188.8088226318359,188.8088226318359,189.2059631347656,189.2059631347656,189.5010299682617,189.5010299682617,187.2085418701172,187.2085418701172,187.5293121337891,187.5293121337891,187.8686676025391,188.221549987793,188.221549987793,188.598014831543,188.598014831543,188.992431640625,188.992431640625,189.3879547119141,189.3879547119141,189.5694046020508,189.5694046020508,189.5694046020508,189.5694046020508,187.3982009887695,187.3982009887695,187.3982009887695,187.7219467163086,187.7219467163086,188.0634078979492,188.0634078979492,188.4221572875977,188.8006286621094,188.8006286621094,189.1974029541016,189.5850219726562,189.5850219726562,189.6367416381836,189.6367416381836,189.6367416381836,187.5898513793945,187.5898513793945,187.9150085449219,187.9150085449219,188.2598037719727,188.2598037719727,188.6236343383789,188.6236343383789,189.0117416381836,189.0117416381836,189.4081573486328,189.4081573486328,189.7029342651367,189.7029342651367,189.7029342651367,187.5232391357422,187.8329696655273,187.8329696655273,188.1620407104492,188.5134506225586,188.8863372802734,188.8863372802734,189.2787017822266,189.7109375,189.7109375,189.7680587768555,189.7680587768555,187.7828521728516,187.7828521728516,188.0948638916016,188.0948638916016,188.4364471435547,188.7974014282227,188.7974014282227,189.1811904907227,189.1811904907227,189.1811904907227,189.5779190063477,189.5779190063477,189.8321838378906,189.8321838378906,187.7414932250977,187.7414932250977,188.0399856567383,188.0399856567383,188.3660125732422,188.3660125732422,188.720100402832,188.720100402832,189.0917434692383,189.0917434692383,189.4809722900391,189.4809722900391,189.4809722900391,189.8779983520508,189.8952560424805,189.8952560424805,189.8952560424805,188.0081176757812,188.3139190673828,188.3139190673828,188.6529388427734,188.6529388427734,189.0106201171875,189.3902282714844,189.7842864990234,189.7842864990234,189.9572677612305,189.9572677612305,189.9572677612305,187.9863586425781,187.9863586425781,188.2788314819336,188.6027755737305,188.6027755737305,188.9516067504883,189.3199462890625,189.3199462890625,189.7100601196289,189.7100601196289,190.0183410644531,190.0183410644531,190.0183410644531,190.0183410644531,190.0183410644531,190.0183410644531,190.0183410644531,190.0183410644531,190.0183410644531,190.0183410644531,190.0183410644531,190.0183410644531,190.0183410644531,190.0183410644531,190.0183410644531,190.0183410644531,190.0183410644531,190.0183410644531,190.0183410644531,190.0183410644531,190.0183410644531,190.0183410644531,190.0183410644531,190.0183410644531,190.0183410644531,190.0183410644531,190.0183410644531,188.0669860839844,188.2886734008789,188.5256805419922,188.7924041748047,188.7924041748047,189.0954055786133,189.0954055786133,189.4296646118164,189.7778091430664,189.7778091430664,190.0780487060547,190.0780487060547,188.0290222167969,188.0290222167969,188.2964477539062,188.2964477539062,188.5893402099609,188.5893402099609,188.5893402099609,188.9255981445312,188.9255981445312,189.2828674316406,189.6632690429688,189.6632690429688,189.6632690429688,190.0659484863281,190.0659484863281,190.1370849609375,190.1370849609375,188.3286819458008,188.6234283447266,188.6234283447266,188.9551849365234,189.3102493286133,189.3102493286133,189.3102493286133,189.691032409668,189.691032409668,189.691032409668,190.0864486694336,190.1953430175781,190.1953430175781,190.1953430175781,188.370964050293,188.6583938598633,188.6583938598633,188.9822769165039,188.9822769165039,188.9822769165039,189.3390197753906,189.3390197753906,189.7080459594727,189.7080459594727,189.7080459594727,190.0977554321289,190.2525253295898,190.2525253295898,188.4722213745117,188.4722213745117,188.7605056762695,188.7605056762695,189.0914535522461,189.4471664428711,189.4471664428711,189.8202056884766,190.2177200317383,190.2177200317383,190.3087692260742,190.3087692260742,190.3087692260742,188.5769271850586,188.8663101196289,188.8663101196289,188.8663101196289,189.1930389404297,189.1930389404297,189.5461502075195,189.9174041748047,189.9174041748047,190.3104553222656,190.3641891479492,190.3641891479492,190.3641891479492,188.6784210205078,188.96826171875,188.96826171875,188.96826171875,189.3007965087891,189.3007965087891,189.6578521728516,189.6578521728516,190.0317916870117,190.0317916870117,190.4187164306641,190.4187164306641,190.4187164306641,190.4187164306641,188.8017883300781,188.8017883300781,189.0984878540039,189.0984878540039,189.0984878540039,189.4360961914062,189.4360961914062,189.4360961914062,189.7926864624023,189.7926864624023,190.1706848144531,190.4722747802734,190.4722747802734,190.4722747802734,188.6809005737305,188.9526519775391,188.9526519775391,189.2609710693359,189.2609710693359,189.6063613891602,189.9697265625,189.9697265625,189.9697265625,190.3505401611328,190.3505401611328,190.5250015258789,190.5250015258789,188.8704833984375,188.8704833984375,188.8704833984375,189.1508712768555,189.1508712768555,189.4735717773438,189.4735717773438,189.8268051147461,189.8268051147461,190.2004318237305,190.2004318237305,190.5769653320312,190.5769653320312,190.5769653320312,190.5769653320312,190.5769653320312,190.5769653320312,189.0554580688477,189.3520812988281,189.6871719360352,189.6871719360352,190.0459365844727,190.4270477294922,190.6279296875,190.6279296875,190.6279296875,188.9853591918945,188.9853591918945,189.2596130371094,189.2596130371094,189.5759506225586,189.9239883422852,189.9239883422852,190.2868041992188,190.2868041992188,190.667236328125,190.6781768798828,190.6781768798828,190.6781768798828,189.1656646728516,189.1656646728516,189.4488830566406,189.4488830566406,189.7754669189453,189.7754669189453,190.131721496582,190.131721496582,190.5023574829102,190.7275924682617,190.7275924682617,190.7275924682617,189.1132736206055,189.3789443969727,189.3789443969727,189.6884307861328,189.6884307861328,190.0323486328125,190.0323486328125,190.3963012695312,190.3963012695312,190.7739486694336,190.7739486694336,190.7762069702148,190.7762069702148,190.7762069702148,189.3252944946289,189.3252944946289,189.6450119018555,189.9822769165039,189.9822769165039,190.3399353027344,190.3399353027344,190.714599609375,190.714599609375,190.8240356445312,190.8240356445312,189.3388137817383,189.6158447265625,189.6158447265625,189.9382400512695,190.2935791015625,190.6581649780273,190.6581649780273,190.8710479736328,190.8710479736328,190.8710479736328,189.3316955566406,189.3316955566406,189.5980758666992,189.5980758666992,189.9042892456055,189.9042892456055,190.2497482299805,190.2497482299805,190.613037109375,190.613037109375,190.9174346923828,190.9174346923828,190.9174346923828,189.3525695800781,189.3525695800781,189.6146087646484,189.9146728515625,189.9146728515625,190.2567825317383,190.6185073852539,190.6185073852539,190.9629135131836,190.9629135131836,190.9629135131836,190.9629135131836,190.9629135131836,190.9629135131836,189.6533737182617,189.6533737182617,189.9492950439453,190.2877197265625,190.2877197265625,190.6492004394531,190.6492004394531,191.0077285766602,191.0077285766602,191.0077285766602,191.0077285766602,191.0077285766602,191.0077285766602,191.0077285766602,191.0077285766602,189.7114334106445,189.7114334106445,190.0060348510742,190.0060348510742,190.3414840698242,190.7354965209961,190.7354965209961,191.0518569946289,191.0518569946289,189.5397033691406,189.5397033691406,189.7922515869141,189.7922515869141,190.0856475830078,190.0856475830078,190.0856475830078,190.4222412109375,190.7803192138672,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,191.0951538085938,189.6017761230469,189.6017761230469,189.6017761230469,189.6017761230469,189.6017761230469,189.6017761230469,189.7087860107422,189.7087860107422,189.9593658447266,190.2365112304688,190.2365112304688,190.5484390258789,190.5484390258789,190.8701553344727,191.1942672729492,191.5567245483398,191.9580993652344,191.9580993652344,192.3654937744141,192.6989135742188,192.6989135742188,193.0339508056641,193.3664398193359,193.3664398193359,193.6998138427734,193.6998138427734,194.0323944091797,194.0323944091797,194.3659820556641,194.3659820556641,194.4391098022461,194.4391098022461,194.4391098022461,189.9759063720703,189.9759063720703,190.3029861450195,190.3029861450195,190.6572875976562,190.6572875976562,190.6572875976562,190.9945449829102,190.9945449829102,191.350227355957,191.350227355957,191.7426300048828,191.7426300048828,192.14501953125,192.5497665405273,192.9582901000977,192.9582901000977,193.3662948608398,193.3662948608398,193.7746047973633,193.7746047973633,194.222526550293,194.5713729858398,194.5713729858398,194.5713729858398,194.5713729858398,190.2453994750977,190.2453994750977,190.5663604736328,190.5663604736328,190.9048385620117,190.9048385620117,191.2214126586914,191.2214126586914,191.5806503295898,191.5806503295898,191.9589233398438,191.9589233398438,192.3510131835938,192.7519378662109,192.7519378662109,193.1581802368164,193.1581802368164,193.5630187988281,193.9709320068359,194.3767547607422,194.7015838623047,194.7015838623047,194.7015838623047,194.7015838623047,190.4540481567383,190.771125793457,190.771125793457,191.1006317138672,191.1006317138672,191.1006317138672,191.4305038452148,191.7939834594727,192.1764526367188,192.5742874145508,192.5742874145508,192.5742874145508,192.9769744873047,192.9769744873047,193.3837966918945,193.7892532348633,193.7892532348633,194.1956787109375,194.1956787109375,194.1956787109375,194.5984344482422,194.5984344482422,194.8296661376953,194.8296661376953,194.8296661376953,190.4296264648438,190.7147750854492,191.0281448364258,191.0281448364258,191.3419189453125,191.3419189453125,191.6907730102539,192.0529327392578,192.0529327392578,192.4376068115234,192.872184753418,193.2752685546875,193.2752685546875,193.6816558837891,193.6816558837891,194.0895080566406,194.0895080566406,194.499397277832,194.499397277832,194.499397277832,194.8945693969727,194.8945693969727,194.9556884765625,194.9556884765625,190.7350387573242,190.7350387573242,191.0245742797852,191.0245742797852,191.329704284668,191.329704284668,191.6538467407227,191.6538467407227,192.0114288330078,192.3771209716797,192.7661514282227,192.7661514282227,193.1623764038086,193.5635528564453,193.5635528564453,193.9710083007812,193.9710083007812,194.378791809082,194.378791809082,194.8157577514648,194.8157577514648,195.0796737670898,195.0796737670898,195.0796737670898,195.0796737670898,195.0796737670898,195.0796737670898,191.0654449462891,191.3573684692383,191.6539306640625,191.6539306640625,192.0013732910156,192.0013732910156,192.3581771850586,192.7346801757812,193.1238861083984,193.1238861083984,193.5129776000977,193.5129776000977,193.9158248901367,193.9158248901367,194.3197555541992,194.3197555541992,194.7258148193359,194.7258148193359,195.1199645996094,195.1199645996094,195.1199645996094,195.2016677856445,195.2016677856445,191.0896224975586,191.0896224975586,191.0896224975586,191.3748016357422,191.664794921875,191.664794921875,192.0252914428711,192.379524230957,192.379524230957,192.7469100952148,193.1305465698242,193.1305465698242,193.5222091674805,193.9175567626953,194.319465637207,194.7219619750977,194.7219619750977,194.7219619750977,195.1179885864258,195.1179885864258,195.3216094970703,195.3216094970703,191.2020874023438,191.4786758422852,191.4786758422852,191.7616806030273,192.0758514404297,192.4269790649414,192.7912063598633,192.7912063598633,193.1748199462891,193.1748199462891,193.1748199462891,193.515739440918,193.8860168457031,193.8860168457031,194.2659378051758,194.2659378051758,194.6606216430664,195.0671463012695,195.0671463012695,195.4397354125977,195.4397354125977,195.4397354125977,195.4397354125977,191.4975204467773,191.4975204467773,191.7770690917969,191.7770690917969,192.0728988647461,192.0728988647461,192.4158172607422,192.4158172607422,192.7727127075195,192.7727127075195,193.1407089233398,193.5253524780273,193.9216995239258,193.9216995239258,194.3237457275391,194.3237457275391,194.7694091796875,194.7694091796875,195.1767807006836,195.555908203125,195.555908203125,195.555908203125,195.555908203125,195.555908203125,195.555908203125,191.6970977783203,191.9679641723633,191.9679641723633,192.2601318359375,192.5985107421875,192.5985107421875,192.9518814086914,192.9518814086914,193.3123397827148,193.3123397827148,193.6852416992188,194.0759582519531,194.468391418457,194.8735656738281,195.2792205810547,195.2792205810547,195.6701736450195,195.6701736450195,195.6701736450195,195.6701736450195,195.6701736450195,195.6701736450195,191.8774261474609,191.8774261474609,192.1413650512695,192.1413650512695,192.4300308227539,192.4300308227539,192.7634735107422,193.1147079467773,193.1147079467773,193.4735717773438,193.4735717773438,193.852653503418,194.2343139648438,194.6266326904297,194.6266326904297,195.0225372314453,195.0225372314453,195.4261474609375,195.7826461791992,195.7826461791992,195.7826461791992,195.7826461791992,192.0522308349609,192.3102874755859,192.3102874755859,192.6016464233398,192.9327239990234,192.9327239990234,193.2833709716797,193.6740875244141,194.0540542602539,194.0540542602539,194.4457244873047,194.4457244873047,194.8433227539062,194.8433227539062,195.2512664794922,195.2512664794922,195.6541976928711,195.6541976928711,195.6541976928711,195.8932189941406,195.8932189941406,195.8932189941406,195.8932189941406,195.8932189941406,195.8932189941406,192.3110046386719,192.3110046386719,192.5769195556641,192.8904266357422,193.2301483154297,193.2301483154297,193.5839691162109,193.5839691162109,193.9494400024414,193.9494400024414,194.3345947265625,194.7329940795898,194.7329940795898,195.1338882446289,195.1338882446289,195.5401840209961,195.9356994628906,195.9356994628906,196.0021591186523,196.0021591186523,196.0021591186523,192.326774597168,192.326774597168,192.5768814086914,192.8575744628906,193.1760864257812,193.1760864257812,193.1760864257812,193.519889831543,193.8739700317383,193.8739700317383,193.8739700317383,194.2458038330078,194.2458038330078,194.633430480957,194.633430480957,194.633430480957,195.0330123901367,195.0330123901367,195.4369277954102,195.4369277954102,195.8421325683594,195.8421325683594,196.1091690063477,196.1091690063477,196.1091690063477,196.1091690063477,196.1091690063477,196.1091690063477,192.6143493652344,192.6143493652344,192.8775405883789,192.8775405883789,193.2104568481445,193.2104568481445,193.5410919189453,193.889533996582,193.889533996582,193.889533996582,194.2542114257812,194.2542114257812,194.6386871337891,195.0388793945312,195.444580078125,195.444580078125,195.8529891967773,196.2145843505859,196.2145843505859,196.2145843505859,196.2145843505859,196.2145843505859,196.2145843505859,192.7142562866211,192.9643325805664,192.9643325805664,193.2533340454102,193.2533340454102,193.5677719116211,193.8990859985352,193.8990859985352,194.2475204467773,194.6099243164062,194.9914398193359,194.9914398193359,195.3865966796875,195.3865966796875,195.7890014648438,195.7890014648438,196.1869964599609,196.3181991577148,196.3181991577148,196.3181991577148,192.7709350585938,193.0101699829102,193.0101699829102,193.2771224975586,193.5718688964844,193.5718688964844,193.894905090332,193.894905090332,194.2351760864258,194.2351760864258,194.2351760864258,194.5812072753906,194.5812072753906,194.9398956298828,194.9398956298828,194.9398956298828,195.318717956543,195.7093276977539,196.1102905273438,196.1102905273438,196.4201965332031,196.4201965332031,196.4201965332031,196.4201965332031,196.4201965332031,196.4201965332031,193.0697708129883,193.3216857910156,193.6051483154297,193.6051483154297,193.9176025390625,194.2574005126953,194.6076431274414,194.9745635986328,195.3614196777344,195.3614196777344,195.7604522705078,196.1668090820312,196.5204849243164,196.5204849243164,196.5204849243164,196.5204849243164,196.5204849243164,196.5204849243164,193.1819458007812,193.1819458007812,193.428840637207,193.428840637207,193.428840637207,193.7042083740234,194.0086288452148,194.0086288452148,194.3462753295898,194.6974029541016,195.0648193359375,195.0648193359375,195.0648193359375,195.4510040283203,195.8486022949219,196.2550659179688,196.2550659179688,196.2550659179688,196.6192092895508,196.6192092895508,196.6192092895508,196.6192092895508,196.6192092895508,196.6192092895508,193.3325805664062,193.3325805664062,193.5791244506836,193.8540267944336,194.1581268310547,194.4954299926758,194.4954299926758,194.8461685180664,195.2089233398438,195.2089233398438,195.5943984985352,195.5943984985352,195.9922409057617,195.9922409057617,196.3965377807617,196.3965377807617,196.7163391113281,196.7163391113281,196.7163391113281,196.7163391113281,196.7163391113281,196.7163391113281,196.7163391113281,196.7163391113281,196.7163391113281,196.7163391113281,196.7163391113281,196.7163391113281,196.7163391113281,196.7163391113281,196.7163391113281,196.7163391113281,196.7163391113281,196.7163391113281,196.7163391113281,196.7163391113281,196.7163391113281,196.7163391113281,196.7163391113281,196.7163391113281,196.7163391113281,196.7163391113281,193.4866104125977,193.4866104125977,193.6780319213867,193.9044647216797,194.1433944702148,194.4143524169922,194.4143524169922,194.7203750610352,194.7203750610352,195.0509796142578,195.0509796142578,195.0509796142578,195.3933334350586,195.3933334350586,195.7530899047852,195.7530899047852,196.1362991333008,196.1362991333008,196.1362991333008,196.5386581420898,196.5386581420898,196.8115463256836,196.8115463256836,196.8115463256836,196.8115463256836,196.8115463256836,196.8115463256836,193.6971817016602,193.6971817016602,193.6971817016602,193.9486465454102,193.9486465454102,194.2244644165039,194.5347747802734,194.8740768432617,194.8740768432617,195.2277297973633,195.6004638671875,195.9936370849609,195.9936370849609,195.9936370849609,196.3947677612305,196.3947677612305,196.7950820922852,196.9056243896484,196.9056243896484,196.9056243896484,193.6830368041992,193.6830368041992,193.9145050048828,193.9145050048828,194.1694717407227,194.1694717407227,194.4531021118164,194.7718200683594,195.1179275512695,195.1179275512695,195.4720840454102,195.849006652832,196.245002746582,196.245002746582,196.6462554931641,196.9981460571289,196.9981460571289,196.9981460571289,196.9981460571289,196.9981460571289,196.9981460571289,193.9133224487305,193.9133224487305,194.1504058837891,194.1504058837891,194.4144973754883,194.4144973754883,194.7102279663086,195.041877746582,195.3908386230469,195.3908386230469,195.7490158081055,195.7490158081055,196.1370010375977,196.1370010375977,196.5374145507812,196.5374145507812,196.938720703125,196.938720703125,197.0891418457031,197.0891418457031,197.0891418457031,193.9767608642578,193.9767608642578,194.2109756469727,194.46728515625,194.46728515625,194.7530899047852,194.7530899047852,195.0759582519531,195.0759582519531,195.419548034668,195.419548034668,195.7708435058594,195.7708435058594,196.1465454101562,196.1465454101562,196.5378570556641,196.5378570556641,196.5378570556641,196.9377593994141,196.9377593994141,197.1786956787109,197.1786956787109,197.1786956787109,197.1786956787109,197.1786956787109,197.1786956787109,197.1786956787109,197.1786956787109,194.2555160522461,194.4993743896484,194.7704086303711,194.7704086303711,195.0752105712891,195.417236328125,195.417236328125,195.7702865600586,195.7702865600586,196.1407241821289,196.1407241821289,196.5282211303711,196.5282211303711,196.9301681518555,196.9301681518555,197.2667846679688,197.2667846679688,197.2667846679688,197.2667846679688,197.2667846679688,197.2667846679688,194.3367919921875,194.3367919921875,194.5713577270508,194.5713577270508,194.8342056274414,194.8342056274414,195.1295471191406,195.1295471191406,195.4654159545898,195.4654159545898,195.4654159545898,195.8181762695312,196.1817092895508,196.1817092895508,196.5700149536133,196.5700149536133,196.9720306396484,197.353515625,197.353515625,197.353515625,197.353515625,194.4682540893555,194.4682540893555,194.7018432617188,194.9632949829102,194.9632949829102,195.2600173950195,195.2600173950195,195.5952987670898,195.9464492797852,195.9464492797852,196.3105850219727,196.3105850219727,196.6957321166992,196.6957321166992,197.0955123901367,197.438720703125,197.438720703125,197.438720703125,197.438720703125,197.438720703125,197.438720703125,194.5974349975586,194.5974349975586,194.8319091796875,194.8319091796875,195.0926132202148,195.0926132202148,195.3788833618164,195.7048645019531,195.7048645019531,196.0526657104492,196.0526657104492,196.4067535400391,196.4067535400391,196.7840881347656,196.7840881347656,197.1829528808594,197.5226745605469,197.5226745605469,197.5226745605469,197.5226745605469,194.7260131835938,194.7260131835938,194.9580459594727,195.2172317504883,195.5104293823242,195.5104293823242,195.8436660766602,195.8436660766602,196.1940460205078,196.1940460205078,196.5547637939453,196.9368362426758,196.9368362426758,197.370246887207,197.6052322387695,197.6052322387695,197.6052322387695,197.6052322387695,197.6052322387695,197.6052322387695,194.8965072631836,194.8965072631836,195.1297454833984,195.3918762207031,195.3918762207031,195.3918762207031,195.6885833740234,195.6885833740234,196.0263977050781,196.0263977050781,196.0263977050781,196.3786087036133,196.7499160766602,196.7499160766602,197.1418075561523,197.540397644043,197.540397644043,197.540397644043,197.6864166259766,197.6864166259766,197.6864166259766,197.6864166259766,197.6864166259766,197.6864166259766,195.0900497436523,195.3310089111328,195.3310089111328,195.6056213378906,195.6056213378906,195.6056213378906,195.9174652099609,195.9174652099609,196.2629470825195,196.2629470825195,196.6204452514648,196.6204452514648,196.9975433349609,197.3953018188477,197.3953018188477,197.3953018188477,197.7663040161133,197.7663040161133,197.7663040161133,197.7663040161133,195.079963684082,195.3083801269531,195.3083801269531,195.5618133544922,195.5618133544922,195.8486938476562,195.8486938476562,196.1756286621094,196.1756286621094,196.5274505615234,196.5274505615234,196.9249954223633,197.3124923706055,197.3124923706055,197.7099456787109,197.7099456787109,197.8449325561523,197.8449325561523,197.8449325561523,197.8449325561523,197.8449325561523,197.8449325561523,195.320198059082,195.320198059082,195.5571441650391,195.8296051025391,195.8296051025391,196.1408843994141,196.1408843994141,196.4829330444336,196.4829330444336,196.8384017944336,196.8384017944336,197.2098846435547,197.2098846435547,197.6040573120117,197.6040573120117,197.9223175048828,197.9223175048828,197.9223175048828,197.9223175048828,197.9223175048828,197.9223175048828,195.3569488525391,195.3569488525391,195.5857162475586,195.5857162475586,195.8417892456055,196.1339569091797,196.1339569091797,196.4664154052734,196.4664154052734,196.8184204101562,197.1785659790039,197.5680770874023,197.5680770874023,197.9622421264648,197.9983520507812,197.9983520507812,197.9983520507812,195.4094390869141,195.6345748901367,195.6345748901367,195.8852233886719,195.8852233886719,196.1684417724609,196.5268783569336,196.5268783569336,196.8790664672852,196.8790664672852,197.2414093017578,197.6282272338867,198.0242080688477,198.0242080688477,198.0732345581055,198.0732345581055,195.5226364135742,195.7474594116211,195.7474594116211,195.9963150024414,196.2798767089844,196.2798767089844,196.6023788452148,196.6023788452148,196.9496231079102,196.9496231079102,197.3074035644531,197.688362121582,197.688362121582,198.081672668457,198.1469039916992,198.1469039916992,198.1469039916992,198.1469039916992,195.6178359985352,195.6178359985352,195.8401336669922,195.8401336669922,196.0842437744141,196.0842437744141,196.0842437744141,196.3611907958984,196.6812515258789,196.6812515258789,197.0277709960938,197.0277709960938,197.3855895996094,197.3855895996094,197.7493133544922,198.1302871704102,198.1302871704102,198.2194137573242,198.2194137573242,198.2194137573242,198.2194137573242,195.9190902709961,196.1532592773438,196.1532592773438,196.4528732299805,196.7678680419922,197.1129531860352,197.1129531860352,197.4686508178711,197.4686508178711,197.8457641601562,197.8457641601562,198.2347564697266,198.2347564697266,198.2906265258789,198.2906265258789,195.8523483276367,195.8523483276367,196.0754318237305,196.3193435668945,196.600212097168,196.600212097168,196.9198226928711,197.2650909423828,197.2650909423828,197.6240081787109,198.0072174072266,198.0072174072266,198.0072174072266,198.3608322143555,198.3608322143555,198.3608322143555,198.3608322143555,196.0089111328125,196.0089111328125,196.2359924316406,196.2359924316406,196.4895248413086,196.4895248413086,196.7794799804688,196.7794799804688,197.1082077026367,197.4599456787109,197.4599456787109,197.8210372924805,198.205680847168,198.205680847168,198.4298324584961,198.4298324584961,198.4298324584961,198.4298324584961,198.4298324584961,198.4298324584961,198.4298324584961,198.4298324584961,198.4298324584961,198.4298324584961,198.4298324584961,198.4298324584961,198.4298324584961,198.4298324584961,198.4298324584961,198.4298324584961,198.4298324584961,198.4298324584961,198.4298324584961,198.4298324584961,196.0537796020508,196.0537796020508,196.1230621337891,196.1230621337891,196.3257141113281,196.3257141113281,196.5526580810547,196.8019409179688,196.8019409179688,197.0897369384766,197.0897369384766,197.4143676757812,197.4143676757812,197.7511596679688,198.1033096313477,198.1033096313477,198.1033096313477,198.4976425170898,198.4976425170898,198.4976425170898,198.4976425170898,196.1848831176758,196.1848831176758,196.408088684082,196.408088684082,196.6598510742188,196.9483795166016,196.9483795166016,197.2756423950195,197.2756423950195,197.6317138671875,197.6317138671875,197.6317138671875,197.9964981079102,197.9964981079102,198.3801651000977,198.5645294189453,198.5645294189453,198.5645294189453,198.5645294189453,198.5645294189453,198.5645294189453,196.4417877197266,196.4417877197266,196.6773834228516,196.6773834228516,196.9462814331055,196.9462814331055,197.255615234375,197.255615234375,197.255615234375,197.5972290039062,197.5972290039062,197.9518661499023,197.9518661499023,198.3207168579102,198.3207168579102,198.6302719116211,198.6302719116211,198.6302719116211,198.6302719116211,198.6302719116211,198.6302719116211,196.4281387329102,196.4281387329102,196.6478729248047,196.6478729248047,196.6478729248047,196.8991851806641,197.1892471313477,197.5183715820312,197.8723754882812,198.234489440918,198.234489440918,198.619499206543,198.619499206543,198.6949615478516,198.6949615478516,198.6949615478516,198.6949615478516,198.6949615478516,198.6949615478516,196.6592636108398,196.6592636108398,196.8975830078125,196.8975830078125,197.1720733642578,197.1720733642578,197.48828125,197.8339004516602,197.8339004516602,198.1876831054688,198.1876831054688,198.5616607666016,198.5616607666016,198.758674621582,198.758674621582,198.758674621582,198.758674621582,198.758674621582,198.758674621582,196.7238159179688,196.7238159179688,196.9581298828125,196.9581298828125,197.2250061035156,197.2250061035156,197.5345153808594,197.5345153808594,197.8765563964844,197.8765563964844,197.8765563964844,198.228874206543,198.228874206543,198.5952987670898,198.5952987670898,198.8212966918945,198.8212966918945,198.8212966918945,198.8212966918945,198.8212966918945,198.8212966918945,196.7639389038086,196.7639389038086,196.9945678710938,196.9945678710938,197.2558670043945,197.5564041137695,197.5564041137695,197.89453125,197.89453125,198.2469253540039,198.2469253540039,198.6108932495117,198.6108932495117,198.8828811645508,198.8828811645508,198.8828811645508,198.8828811645508,196.8492431640625,196.8492431640625,197.0790863037109,197.0790863037109,197.3363342285156,197.3363342285156,197.6299057006836,197.6299057006836,197.9638214111328,197.9638214111328,198.3185272216797,198.6806411743164,198.9435424804688,198.9435424804688,198.9435424804688,198.9435424804688,198.9435424804688,198.9435424804688,196.9553451538086,197.185920715332,197.185920715332,197.4450988769531,197.7458648681641,197.7458648681641,198.0828018188477,198.0828018188477,198.4372634887695,198.4372634887695,198.4372634887695,198.8020706176758,198.8020706176758,199.003173828125,199.003173828125,199.003173828125,199.003173828125,199.003173828125,199.003173828125,199.003173828125,199.003173828125,197.0597915649414,197.0597915649414,197.2900238037109,197.2900238037109,197.2900238037109,197.5495300292969,197.5495300292969,197.8503723144531,198.1862258911133,198.5388793945312,198.5388793945312,198.905647277832,198.905647277832,199.0618286132812,199.0618286132812,199.0618286132812,199.0618286132812,199.0618286132812,199.0618286132812,197.1900329589844,197.1900329589844,197.42236328125,197.6863021850586,197.6863021850586,197.6863021850586,197.9907989501953,198.3309783935547,198.6863174438477,198.6863174438477,199.057861328125,199.057861328125,199.1195831298828,199.1195831298828,199.1195831298828,199.1195831298828,199.1195831298828,199.1195831298828,197.3613967895508,197.6015548706055,197.6015548706055,197.8802337646484,197.8802337646484,198.1994247436523,198.1994247436523,198.1994247436523,198.5439376831055,198.9007339477539,199.1763229370117,199.1763229370117,199.1763229370117,199.1763229370117,199.1763229370117,199.1763229370117,197.2798843383789,197.5017929077148,197.5017929077148,197.7499160766602,197.7499160766602,198.0386352539062,198.0386352539062,198.3667907714844,198.7164840698242,198.7164840698242,199.0798492431641,199.0798492431641,199.2322158813477,199.2322158813477,199.2322158813477,199.2322158813477,199.2322158813477,199.2322158813477,197.4515228271484,197.4515228271484,197.6821441650391,197.6821441650391,197.9411544799805,198.2415313720703,198.2415313720703,198.5765075683594,198.5765075683594,198.5765075683594,198.9307174682617,199.2871856689453,199.2871856689453,199.2871856689453,199.2871856689453,199.2871856689453,199.2871856689453,197.4354705810547,197.4354705810547,197.6574783325195,197.6574783325195,197.8996276855469,197.8996276855469,197.8996276855469,198.1845779418945,198.5072326660156,198.8581237792969,198.8581237792969,199.2173461914062,199.3412704467773,199.3412704467773,199.3412704467773,199.3412704467773,199.3412704467773,199.3412704467773,199.3412704467773,199.3412704467773,199.3412704467773,199.3412704467773,199.3412704467773,199.3412704467773,197.5681228637695,197.5681228637695,197.7750701904297,198.0080261230469,198.0080261230469,198.2691345214844,198.2691345214844,198.5669631958008,198.5669631958008,198.9003372192383,198.9003372192383,199.2504501342773,199.2504501342773,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,199.3944625854492,197.5627059936523,197.5627059936523,197.5627059936523,197.5627059936523,197.800651550293,198.0611267089844,198.3541030883789,198.3541030883789,198.6825942993164,199.015998840332,199.3239593505859,199.3239593505859,199.6885986328125,199.6885986328125,200.0918579101562,200.0918579101562,200.4945602416992,200.4945602416992,200.8993377685547,201.3017196655273,201.6475067138672,201.9766998291016,202.3053741455078,202.6341781616211,202.6341781616211,202.9668884277344,202.9668884277344,203.2969131469727,203.6264801025391,203.6264801025391,203.6264801025391,203.9561767578125,203.9561767578125,204.2847366333008,204.6155166625977,204.9453582763672,204.9453582763672,204.9453582763672,205.1752243041992,205.1752243041992,205.1752243041992,205.1752243041992,205.1752243041992,205.1752243041992,197.9076385498047,197.9076385498047,198.154899597168,198.154899597168,198.154899597168,198.4282531738281,198.4282531738281,198.7367553710938,198.7367553710938,199.0693359375,199.3872985839844,199.7238616943359,200.0924682617188,200.4866027832031,200.4866027832031,200.8933639526367,200.8933639526367,200.8933639526367,201.2994384765625,201.2994384765625,201.7040405273438,202.1109924316406,202.1109924316406,202.5174255371094,202.5174255371094,202.9230728149414,202.9230728149414,203.3285980224609,203.3285980224609,203.735725402832,203.735725402832,203.735725402832,204.1424789428711,204.1424789428711,204.5487518310547,204.9482574462891,204.9482574462891,205.3345260620117,205.3345260620117,205.3834381103516,205.3834381103516,205.3834381103516,205.3834381103516,205.3834381103516,205.3834381103516,198.3272857666016,198.5795745849609,198.5795745849609,198.8603134155273,198.8603134155273,199.1744384765625,199.1744384765625,199.4929580688477,199.4929580688477,199.8157806396484,199.8157806396484,200.1685409545898,200.1685409545898,200.5438690185547,200.5438690185547,200.5438690185547,200.9376220703125,200.9376220703125,200.9376220703125,201.3412094116211,201.3412094116211,201.7469635009766,201.7469635009766,202.1920776367188,202.1920776367188,202.599006652832,202.599006652832,203.0054626464844,203.0054626464844,203.4111785888672,203.8168411254883,203.8168411254883,203.8168411254883,204.2242965698242,204.2242965698242,204.2242965698242,204.6309127807617,205.0372467041016,205.4252624511719,205.4252624511719,205.4252624511719,205.5882797241211,205.5882797241211,205.5882797241211,205.5882797241211,205.5882797241211,205.5882797241211,205.5882797241211,205.5882797241211,198.5610198974609,198.5610198974609,198.8084030151367,198.8084030151367,199.0755233764648,199.0755233764648,199.3748397827148,199.3748397827148,199.6849746704102,200.0069427490234,200.0069427490234,200.3557739257812,200.3557739257812,200.3557739257812,200.7202682495117,200.7202682495117,201.1120529174805,201.1120529174805,201.5133895874023,201.5133895874023,201.5133895874023,201.917854309082,201.917854309082,202.3225326538086,202.3225326538086,202.7273788452148,203.1310806274414,203.5343933105469,203.9384765625,203.9384765625,204.3428115844727,204.747428894043,204.747428894043,205.1541442871094,205.1541442871094,205.54443359375,205.54443359375,205.7898406982422,205.7898406982422,205.7898406982422,205.7898406982422,205.7898406982422,205.7898406982422,199.0511856079102,199.3295974731445,199.3295974731445,199.6112365722656,199.6112365722656,199.9029388427734,199.9029388427734,200.2176971435547,200.2176971435547,200.5636138916016,200.9217376708984,200.9217376708984,201.2997360229492,201.7018966674805,201.7018966674805,202.1047821044922,202.1047821044922,202.5122756958008,202.9175567626953,203.324089050293,203.7309036254883,203.7309036254883,204.1360626220703,204.1360626220703,204.5439071655273,204.5439071655273,204.5439071655273,204.9515151977539,204.9515151977539,205.3500442504883,205.3500442504883,205.3500442504883,205.7355651855469,205.7355651855469,205.9880981445312,205.9880981445312,205.9880981445312,205.9880981445312,205.9880981445312,205.9880981445312,205.9880981445312,205.9880981445312,205.9880981445312,199.3356475830078,199.3356475830078,199.3356475830078,199.5857696533203,199.8556289672852,199.8556289672852,200.1380767822266,200.1380767822266,200.4507751464844,200.4507751464844,200.7953033447266,201.1465911865234,201.1465911865234,201.5165023803711,201.5165023803711,201.9081192016602,201.9081192016602,202.3073120117188,202.7132110595703,202.7132110595703,203.1178359985352,203.1178359985352,203.5246047973633,203.5246047973633,203.9310531616211,203.9310531616211,204.3395233154297,204.3395233154297,204.7480697631836,204.7480697631836,205.158447265625,205.158447265625,205.6102981567383,205.6102981567383,206.0029067993164,206.1832427978516,206.1832427978516,206.1832427978516,206.1832427978516,206.1832427978516,206.1832427978516,206.1832427978516,206.1832427978516,206.1832427978516,199.6930618286133,199.9478302001953,199.9478302001953,200.2166290283203,200.2166290283203,200.4991302490234,200.8344650268555,201.1852569580078,201.1852569580078,201.5452041625977,201.5452041625977,201.9220886230469,201.9220886230469,201.9220886230469,202.3184967041016,202.3184967041016,202.7140579223633,203.1191787719727,203.1191787719727,203.5211944580078,203.5211944580078,203.9249801635742,203.9249801635742,203.9249801635742,204.3313522338867,204.3313522338867,204.7389831542969,205.1469650268555,205.5560455322266,205.5560455322266,205.95947265625,205.95947265625,206.3486633300781,206.3486633300781,206.3486633300781,206.3751449584961,206.3751449584961,206.3751449584961,206.3751449584961,206.3751449584961,206.3751449584961,206.3751449584961,206.3751449584961,206.3751449584961,206.3751449584961,206.3751449584961,206.3751449584961,206.3751449584961,206.3751449584961,206.3751449584961,206.3751449584961,206.3751449584961,206.3751449584961,206.3751449584961,206.3751449584961,206.3751449584961,206.3751449584961,206.3751449584961,206.3751449584961,199.9675903320312,199.9675903320312,200.2049026489258,200.2049026489258,200.4463348388672,200.4463348388672,200.7002487182617,200.7002487182617,201.0065841674805,201.0065841674805,201.3413925170898,201.3413925170898,201.6859741210938,202.0388031005859,202.4146270751953,202.4146270751953,202.8059387207031,202.8059387207031,202.8059387207031,203.2033233642578,203.6000137329102,204.0028381347656,204.0028381347656,204.4064331054688,204.4064331054688,204.8103942871094,204.8103942871094,205.2161483764648,205.6214447021484,205.6214447021484,206.0266036987305,206.0266036987305,206.412841796875,206.412841796875,206.5639114379883,206.5639114379883,206.5639114379883,206.5639114379883,206.5639114379883,206.5639114379883,206.5639114379883,206.5639114379883,206.5639114379883,200.2917861938477,200.5348663330078,200.5348663330078,200.7892074584961,201.0776824951172,201.4091415405273,201.4091415405273,201.751708984375,202.1041641235352,202.1041641235352,202.4733657836914,202.4733657836914,202.8632125854492,203.2523651123047,203.6505126953125,204.0489654541016,204.0489654541016,204.4906463623047,204.4906463623047,204.8944473266602,204.8944473266602,205.2992858886719,205.7039337158203,205.7039337158203,206.1083602905273,206.1083602905273,206.4998245239258,206.4998245239258,206.7497024536133,206.7497024536133,206.7497024536133,206.7497024536133,206.7497024536133,206.7497024536133,200.4937133789062,200.4937133789062,200.7343597412109,200.7343597412109,200.9789199829102,200.9789199829102,201.2546157836914,201.2546157836914,201.5727157592773,201.5727157592773,201.9145584106445,201.9145584106445,202.2581481933594,202.2581481933594,202.6144104003906,202.9967193603516,202.9967193603516,203.3891372680664,203.7824401855469,204.1852416992188,204.1852416992188,204.1852416992188,204.5909042358398,204.5909042358398,204.9981307983398,205.4057083129883,205.4057083129883,205.8138198852539,205.8138198852539,206.2226791381836,206.2226791381836,206.2226791381836,206.6220626831055,206.6220626831055,206.9324798583984,206.9324798583984,206.9324798583984,206.9324798583984,206.9324798583984,206.9324798583984,206.9324798583984,206.9324798583984,206.9324798583984,200.755485534668,200.755485534668,200.9927139282227,200.9927139282227,201.256103515625,201.5375671386719,201.8585357666016,201.8585357666016,202.2006912231445,202.5483703613281,202.5483703613281,202.9094924926758,202.9094924926758,203.2941207885742,203.2941207885742,203.6866912841797,204.0835494995117,204.0835494995117,212.0416946411133,212.0416946411133,212.0416946411133,212.0416946411133,212.0416946411133,212.0416946411133,212.0416946411133,212.0416946411133,212.0416946411133,212.0416946411133,212.0416946411133,212.0416946411133,212.0416946411133,212.0416946411133,212.0416946411133,212.0416946411133,212.0416946411133,212.0416946411133,212.0416946411133,212.0416946411133,219.6710891723633,219.6710968017578,219.6710968017578,219.6710968017578,219.6710968017578,219.6710968017578,219.6710968017578,219.6710968017578,219.6710968017578,219.6710968017578,219.6710968017578,219.6710968017578,219.6710968017578,219.6710968017578,219.6710968017578,219.6710968017578,219.6710968017578,219.6710968017578,219.6710968017578,219.6710968017578,219.6710968017578,219.6710968017578,219.6710968017578,219.6710968017578,219.6710968017578,234.9298858642578,234.9298858642578,234.9298858642578,234.9298858642578,234.9298858642578,234.9298858642578,234.9298858642578,234.9298858642578,234.9298858642578,234.9298858642578,234.9298858642578,234.9298858642578,234.9298858642578,234.9298858642578,234.9298858642578,234.9298858642578,242.5593032836914,242.5593032836914,242.5593032836914,242.5593032836914,242.5593032836914,242.5593032836914,242.5593032836914,242.5593032836914,242.6582870483398,242.6582870483398,242.6582870483398,242.6582870483398,242.6582870483398,242.6582870483398,242.6582870483398,242.6582870483398,242.6582870483398,242.6582870483398,242.6582870483398,242.6582870483398,242.6582870483398,242.6582870483398,242.6582870483398,242.6582870483398,242.6582870483398,242.6582870483398,242.6582870483398,242.6582870483398,242.6582870483398,242.6582870483398,242.6582870483398,242.6582870483398,242.6582870483398,242.6582870483398,242.6582870483398,242.6582870483398,242.6582870483398,242.6582870483398,242.6582870483398,242.6582870483398,242.6582870483398,242.6582870483398,242.6582870483398,242.6582870483398,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156,257.9544982910156],"meminc":[0,0,0,0,15.28223419189453,0,0,0,0.0003662109375,0,0,30.46537780761719,0,0,0,0,0,4.57763671875e-05,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-0.00030517578125,0,15.42662048339844,0,0,0.2514190673828125,0,0.2704086303710938,0.3153457641601562,0,0.3481292724609375,0.356109619140625,0.3865737915039062,0.4070358276367188,0.4472885131835938,0.113250732421875,0,-2.578903198242188,0.3866424560546875,0,0.4208221435546875,0,0.4190597534179688,0.4058303833007812,0,0.4014663696289062,0,0.3995742797851562,0,0.209930419921875,0,-2.610084533691406,0,0.361358642578125,0.3805389404296875,0,0.4127655029296875,0,0.4081344604492188,0,0,0.4033966064453125,0.4041900634765625,0.3214950561523438,0,-2.658622741699219,0.3525924682617188,0.3739852905273438,0,0.402191162109375,0,0.4051284790039062,0.402587890625,0,0.4041366577148438,0,0.3985061645507812,0,0,-2.685684204101562,0.349609375,0,0.3628692626953125,0,0.3876876831054688,0,0.404937744140625,0,0.4022140502929688,0,0.40008544921875,0,0.403045654296875,0,-2.644508361816406,0,0.3563613891601562,0,0,0.3635635375976562,0,0.3843002319335938,0,0.404815673828125,0.3918914794921875,0,0.3995819091796875,0.4016571044921875,0,-2.60565185546875,0,0.349395751953125,0.3551177978515625,0,0,0.4120025634765625,0,0.4005966186523438,0,0.3910064697265625,0,0.3893508911132812,0,0.3974380493164062,0,0.06201934814453125,0,-2.316024780273438,0,0.349517822265625,0,0.364288330078125,0.39080810546875,0,0.3940963745117188,0,0.3876419067382812,0,0.39581298828125,0.1093826293945312,0,0,-2.2998046875,0,0.3486709594726562,0.363250732421875,0,0.386383056640625,0,0.3907394409179688,0.3914108276367188,0,0.3910293579101562,0.10247802734375,0,-2.277259826660156,0,0.338897705078125,0.3534011840820312,0,0.3651123046875,0,0.3784866333007812,0,0.3821868896484375,0.393768310546875,0,0.1384506225585938,0,0,-2.282768249511719,0,0.3346710205078125,0.3526458740234375,0,0.3634185791015625,0,0.38568115234375,0,0.3946609497070312,0,0.3981399536132812,0.1253509521484375,0,0,-2.217437744140625,0.3421707153320312,0.3552703857421875,0.3759384155273438,0.4316024780273438,0,0.3994140625,0,0.3837509155273438,0,0,-2.397964477539062,0,0.3163604736328125,0,0.3392105102539062,0,0.3518295288085938,0,0.3763809204101562,0.3914871215820312,0,0.3971405029296875,0,0.2950668334960938,0,-2.292488098144531,0,0.320770263671875,0,0.33935546875,0.3528823852539062,0,0.37646484375,0,0.3944168090820312,0,0.3955230712890625,0,0.1814498901367188,0,0,0,-2.17120361328125,0,0,0.3237457275390625,0,0.341461181640625,0,0.3587493896484375,0.3784713745117188,0,0.3967742919921875,0.3876190185546875,0,0.05171966552734375,0,0,-2.046890258789062,0,0.3251571655273438,0,0.3447952270507812,0,0.36383056640625,0,0.3881072998046875,0,0.3964157104492188,0,0.2947769165039062,0,0,-2.179695129394531,0.3097305297851562,0,0.329071044921875,0.351409912109375,0.3728866577148438,0,0.392364501953125,0.4322357177734375,0,0.05712127685546875,0,-1.985206604003906,0,0.31201171875,0,0.341583251953125,0.3609542846679688,0,0.3837890625,0,0,0.396728515625,0,0.2542648315429688,0,-2.090690612792969,0,0.298492431640625,0,0.3260269165039062,0,0.3540878295898438,0,0.37164306640625,0,0.3892288208007812,0,0,0.3970260620117188,0.0172576904296875,0,0,-1.887138366699219,0.3058013916015625,0,0.339019775390625,0,0.3576812744140625,0.379608154296875,0.3940582275390625,0,0.1729812622070312,0,0,-1.970909118652344,0,0.2924728393554688,0.323944091796875,0,0.3488311767578125,0.3683395385742188,0,0.3901138305664062,0,0.3082809448242188,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.95135498046875,0.2216873168945312,0.2370071411132812,0.2667236328125,0,0.3030014038085938,0,0.334259033203125,0.34814453125,0,0.3002395629882812,0,-2.049026489257812,0,0.267425537109375,0,0.2928924560546875,0,0,0.3362579345703125,0,0.357269287109375,0.380401611328125,0,0,0.402679443359375,0,0.071136474609375,0,-1.808403015136719,0.2947463989257812,0,0.331756591796875,0.3550643920898438,0,0,0.3807830810546875,0,0,0.395416259765625,0.1088943481445312,0,0,-1.824378967285156,0.2874298095703125,0,0.323883056640625,0,0,0.3567428588867188,0,0.3690261840820312,0,0,0.38970947265625,0.1547698974609375,0,-1.780303955078125,0,0.2882843017578125,0,0.3309478759765625,0.355712890625,0,0.3730392456054688,0.3975143432617188,0,0.0910491943359375,0,0,-1.731842041015625,0.2893829345703125,0,0,0.3267288208007812,0,0.3531112670898438,0.3712539672851562,0,0.3930511474609375,0.05373382568359375,0,0,-1.685768127441406,0.2898406982421875,0,0,0.3325347900390625,0,0.3570556640625,0,0.3739395141601562,0,0.3869247436523438,0,0,0,-1.616928100585938,0,0.2966995239257812,0,0,0.3376083374023438,0,0,0.3565902709960938,0,0.3779983520507812,0.3015899658203125,0,0,-1.791374206542969,0.2717514038085938,0,0.308319091796875,0,0.3453903198242188,0.3633651733398438,0,0,0.3808135986328125,0,0.1744613647460938,0,-1.654518127441406,0,0,0.2803878784179688,0,0.3227005004882812,0,0.3532333374023438,0,0.373626708984375,0,0.3765335083007812,0,0,0,0,0,-1.521507263183594,0.2966232299804688,0.3350906372070312,0,0.3587646484375,0.3811111450195312,0.2008819580078125,0,0,-1.642570495605469,0,0.2742538452148438,0,0.3163375854492188,0.3480377197265625,0,0.3628158569335938,0,0.38043212890625,0.0109405517578125,0,0,-1.51251220703125,0,0.2832183837890625,0,0.3265838623046875,0,0.3562545776367188,0,0.370635986328125,0.2252349853515625,0,0,-1.61431884765625,0.2656707763671875,0,0.3094863891601562,0,0.3439178466796875,0,0.36395263671875,0,0.3776473999023438,0,0.00225830078125,0,0,-1.450912475585938,0,0.3197174072265625,0.3372650146484375,0,0.3576583862304688,0,0.374664306640625,0,0.10943603515625,0,-1.485221862792969,0.2770309448242188,0,0.3223953247070312,0.3553390502929688,0.3645858764648438,0,0.2128829956054688,0,0,-1.539352416992188,0,0.2663803100585938,0,0.30621337890625,0,0.345458984375,0,0.3632888793945312,0,0.3043975830078125,0,0,-1.564865112304688,0,0.2620391845703125,0.3000640869140625,0,0.3421096801757812,0.361724853515625,0,0.3444061279296875,0,0,0,0,0,-1.309539794921875,0,0.2959213256835938,0.3384246826171875,0,0.361480712890625,0,0.3585281372070312,0,0,0,0,0,0,0,-1.296295166015625,0,0.2946014404296875,0,0.33544921875,0.394012451171875,0,0.3163604736328125,0,-1.512153625488281,0,0.2525482177734375,0,0.29339599609375,0,0,0.3365936279296875,0.3580780029296875,0.3148345947265625,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.493377685546875,0,0,0,0,0,0.1070098876953125,0,0.250579833984375,0.2771453857421875,0,0.3119277954101562,0,0.32171630859375,0.3241119384765625,0.362457275390625,0.4013748168945312,0,0.4073944091796875,0.3334197998046875,0,0.3350372314453125,0.332489013671875,0,0.3333740234375,0,0.33258056640625,0,0.333587646484375,0,0.07312774658203125,0,0,-4.463203430175781,0,0.3270797729492188,0,0.3543014526367188,0,0,0.3372573852539062,0,0.355682373046875,0,0.3924026489257812,0,0.4023895263671875,0.4047470092773438,0.4085235595703125,0,0.4080047607421875,0,0.4083099365234375,0,0.4479217529296875,0.348846435546875,0,0,0,-4.325973510742188,0,0.3209609985351562,0,0.3384780883789062,0,0.3165740966796875,0,0.3592376708984375,0,0.3782730102539062,0,0.39208984375,0.4009246826171875,0,0.4062423706054688,0,0.4048385620117188,0.4079132080078125,0.40582275390625,0.3248291015625,0,0,0,-4.247535705566406,0.31707763671875,0,0.3295059204101562,0,0,0.3298721313476562,0.3634796142578125,0.3824691772460938,0.3978347778320312,0,0,0.4026870727539062,0,0.4068222045898438,0.40545654296875,0,0.4064254760742188,0,0,0.4027557373046875,0,0.231231689453125,0,0,-4.400039672851562,0.2851486206054688,0.3133697509765625,0,0.3137741088867188,0,0.3488540649414062,0.3621597290039062,0,0.384674072265625,0.4345779418945312,0.4030838012695312,0,0.4063873291015625,0,0.4078521728515625,0,0.4098892211914062,0,0,0.395172119140625,0,0.06111907958984375,0,-4.220649719238281,0,0.2895355224609375,0,0.3051300048828125,0,0.3241424560546875,0,0.3575820922851562,0.365692138671875,0.3890304565429688,0,0.3962249755859375,0.4011764526367188,0,0.4074554443359375,0,0.4077835083007812,0,0.4369659423828125,0,0.263916015625,0,0,0,0,0,-4.014228820800781,0.2919235229492188,0.2965621948242188,0,0.347442626953125,0,0.3568038940429688,0.3765029907226562,0.3892059326171875,0,0.3890914916992188,0,0.4028472900390625,0,0.4039306640625,0,0.4060592651367188,0,0.3941497802734375,0,0,0.08170318603515625,0,-4.112045288085938,0,0,0.2851791381835938,0.2899932861328125,0,0.3604965209960938,0.3542327880859375,0,0.3673858642578125,0.383636474609375,0,0.39166259765625,0.3953475952148438,0.4019088745117188,0.402496337890625,0,0,0.396026611328125,0,0.2036209106445312,0,-4.119522094726562,0.2765884399414062,0,0.2830047607421875,0.3141708374023438,0.3511276245117188,0.364227294921875,0,0.3836135864257812,0,0,0.3409194946289062,0.3702774047851562,0,0.3799209594726562,0,0.394683837890625,0.406524658203125,0,0.372589111328125,0,0,0,-3.942214965820312,0,0.2795486450195312,0,0.2958297729492188,0,0.3429183959960938,0,0.3568954467773438,0,0.3679962158203125,0.3846435546875,0.3963470458984375,0,0.4020462036132812,0,0.4456634521484375,0,0.4073715209960938,0.3791275024414062,0,0,0,0,0,-3.858810424804688,0.2708663940429688,0,0.2921676635742188,0.33837890625,0,0.3533706665039062,0,0.3604583740234375,0,0.3729019165039062,0.390716552734375,0.3924331665039062,0.4051742553710938,0.4056549072265625,0,0.3909530639648438,0,0,0,0,0,-3.792747497558594,0,0.2639389038085938,0,0.288665771484375,0,0.3334426879882812,0.3512344360351562,0,0.3588638305664062,0,0.3790817260742188,0.3816604614257812,0.3923187255859375,0,0.395904541015625,0,0.4036102294921875,0.3564987182617188,0,0,0,-3.730415344238281,0.258056640625,0,0.2913589477539062,0.3310775756835938,0,0.35064697265625,0.390716552734375,0.3799667358398438,0,0.3916702270507812,0,0.3975982666015625,0,0.4079437255859375,0,0.4029312133789062,0,0,0.2390213012695312,0,0,0,0,0,-3.58221435546875,0,0.2659149169921875,0.313507080078125,0.3397216796875,0,0.35382080078125,0,0.3654708862304688,0,0.3851547241210938,0.3983993530273438,0,0.4008941650390625,0,0.4062957763671875,0.3955154418945312,0,0.06645965576171875,0,0,-3.675384521484375,0,0.2501068115234375,0.2806930541992188,0.318511962890625,0,0,0.3438034057617188,0.3540802001953125,0,0,0.3718338012695312,0,0.3876266479492188,0,0,0.3995819091796875,0,0.4039154052734375,0,0.4052047729492188,0,0.2670364379882812,0,0,0,0,0,-3.494819641113281,0,0.2631912231445312,0,0.332916259765625,0,0.3306350708007812,0.3484420776367188,0,0,0.3646774291992188,0,0.3844757080078125,0.4001922607421875,0.40570068359375,0,0.4084091186523438,0.3615951538085938,0,0,0,0,0,-3.500328063964844,0.2500762939453125,0,0.28900146484375,0,0.3144378662109375,0.3313140869140625,0,0.3484344482421875,0.3624038696289062,0.3815155029296875,0,0.3951568603515625,0,0.40240478515625,0,0.3979949951171875,0.1312026977539062,0,0,-3.547264099121094,0.2392349243164062,0,0.2669525146484375,0.2947463989257812,0,0.3230361938476562,0,0.34027099609375,0,0,0.3460311889648438,0,0.3586883544921875,0,0,0.3788223266601562,0.3906097412109375,0.4009628295898438,0,0.309906005859375,0,0,0,0,0,-3.350425720214844,0.2519149780273438,0.2834625244140625,0,0.3124542236328125,0.3397979736328125,0.3502426147460938,0.3669204711914062,0.3868560791015625,0,0.3990325927734375,0.4063568115234375,0.3536758422851562,0,0,0,0,0,-3.338539123535156,0,0.2468948364257812,0,0,0.2753677368164062,0.3044204711914062,0,0.337646484375,0.3511276245117188,0.3674163818359375,0,0,0.3861846923828125,0.3975982666015625,0.406463623046875,0,0,0.3641433715820312,0,0,0,0,0,-3.286628723144531,0,0.2465438842773438,0.27490234375,0.3041000366210938,0.3373031616210938,0,0.350738525390625,0.3627548217773438,0,0.3854751586914062,0,0.3978424072265625,0,0.404296875,0,0.3198013305664062,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-3.229728698730469,0,0.1914215087890625,0.2264328002929688,0.2389297485351562,0.2709579467773438,0,0.3060226440429688,0,0.3306045532226562,0,0,0.3423538208007812,0,0.3597564697265625,0,0.383209228515625,0,0,0.4023590087890625,0,0.27288818359375,0,0,0,0,0,-3.114364624023438,0,0,0.25146484375,0,0.27581787109375,0.3103103637695312,0.3393020629882812,0,0.3536529541015625,0.3727340698242188,0.3931732177734375,0,0,0.4011306762695312,0,0.4003143310546875,0.1105422973632812,0,0,-3.222587585449219,0,0.2314682006835938,0,0.2549667358398438,0,0.28363037109375,0.3187179565429688,0.3461074829101562,0,0.354156494140625,0.376922607421875,0.39599609375,0,0.4012527465820312,0.3518905639648438,0,0,0,0,0,-3.084823608398438,0,0.2370834350585938,0,0.2640914916992188,0,0.2957305908203125,0.3316497802734375,0.3489608764648438,0,0.3581771850585938,0,0.3879852294921875,0,0.4004135131835938,0,0.40130615234375,0,0.150421142578125,0,0,-3.112380981445312,0,0.2342147827148438,0.2563095092773438,0,0.2858047485351562,0,0.3228683471679688,0,0.3435897827148438,0,0.3512954711914062,0,0.375701904296875,0,0.3913116455078125,0,0,0.39990234375,0,0.240936279296875,0,0,0,0,0,0,0,-2.923179626464844,0.2438583374023438,0.2710342407226562,0,0.3048019409179688,0.3420257568359375,0,0.3530502319335938,0,0.3704376220703125,0,0.3874969482421875,0,0.401947021484375,0,0.3366165161132812,0,0,0,0,0,-2.92999267578125,0,0.2345657348632812,0,0.262847900390625,0,0.2953414916992188,0,0.3358688354492188,0,0,0.3527603149414062,0.3635330200195312,0,0.3883056640625,0,0.4020156860351562,0.3814849853515625,0,0,0,-2.885261535644531,0,0.2335891723632812,0.2614517211914062,0,0.296722412109375,0,0.3352813720703125,0.3511505126953125,0,0.3641357421875,0,0.3851470947265625,0,0.3997802734375,0.3432083129882812,0,0,0,0,0,-2.841285705566406,0,0.2344741821289062,0,0.2607040405273438,0,0.2862701416015625,0.3259811401367188,0,0.3478012084960938,0,0.3540878295898438,0,0.3773345947265625,0,0.39886474609375,0.3397216796875,0,0,0,-2.796661376953125,0,0.2320327758789062,0.259185791015625,0.2931976318359375,0,0.3332366943359375,0,0.3503799438476562,0,0.3607177734375,0.3820724487304688,0,0.43341064453125,0.2349853515625,0,0,0,0,0,-2.708724975585938,0,0.2332382202148438,0.2621307373046875,0,0,0.2967071533203125,0,0.3378143310546875,0,0,0.3522109985351562,0.371307373046875,0,0.3918914794921875,0.398590087890625,0,0,0.1460189819335938,0,0,0,0,0,-2.596366882324219,0.2409591674804688,0,0.2746124267578125,0,0,0.3118438720703125,0,0.3454818725585938,0,0.3574981689453125,0,0.3770980834960938,0.3977584838867188,0,0,0.371002197265625,0,0,0,-2.68634033203125,0.2284164428710938,0,0.2534332275390625,0,0.2868804931640625,0,0.326934814453125,0,0.3518218994140625,0,0.3975448608398438,0.3874969482421875,0,0.3974533081054688,0,0.1349868774414062,0,0,0,0,0,-2.524734497070312,0,0.2369461059570312,0.2724609375,0,0.311279296875,0,0.3420486450195312,0,0.35546875,0,0.3714828491210938,0,0.3941726684570312,0,0.3182601928710938,0,0,0,0,0,-2.56536865234375,0,0.2287673950195312,0,0.256072998046875,0.2921676635742188,0,0.33245849609375,0,0.3520050048828125,0.3601455688476562,0.3895111083984375,0,0.3941650390625,0.03610992431640625,0,0,-2.588912963867188,0.2251358032226562,0,0.2506484985351562,0,0.2832183837890625,0.3584365844726562,0,0.3521881103515625,0,0.3623428344726562,0.3868179321289062,0.3959808349609375,0,0.0490264892578125,0,-2.55059814453125,0.224822998046875,0,0.2488555908203125,0.2835617065429688,0,0.3225021362304688,0,0.3472442626953125,0,0.3577804565429688,0.3809585571289062,0,0.393310546875,0.0652313232421875,0,0,0,-2.529067993164062,0,0.2222976684570312,0,0.244110107421875,0,0,0.276947021484375,0.3200607299804688,0,0.3465194702148438,0,0.357818603515625,0,0.3637237548828125,0.3809738159179688,0,0.0891265869140625,0,0,0,-2.300323486328125,0.2341690063476562,0,0.2996139526367188,0.3149948120117188,0.3450851440429688,0,0.3556976318359375,0,0.3771133422851562,0,0.3889923095703125,0,0.05587005615234375,0,-2.438278198242188,0,0.22308349609375,0.2439117431640625,0.2808685302734375,0,0.319610595703125,0.3452682495117188,0,0.358917236328125,0.383209228515625,0,0,0.3536148071289062,0,0,0,-2.351921081542969,0,0.227081298828125,0,0.2535324096679688,0,0.2899551391601562,0,0.3287277221679688,0.3517379760742188,0,0.3610916137695312,0.3846435546875,0,0.224151611328125,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2.376052856445312,0,0.06928253173828125,0,0.2026519775390625,0,0.2269439697265625,0.2492828369140625,0,0.2877960205078125,0,0.3246307373046875,0,0.3367919921875,0.3521499633789062,0,0,0.3943328857421875,0,0,0,-2.312759399414062,0,0.22320556640625,0,0.2517623901367188,0.2885284423828125,0,0.3272628784179688,0,0.3560714721679688,0,0,0.3647842407226562,0,0.3836669921875,0.1843643188476562,0,0,0,0,0,-2.12274169921875,0,0.235595703125,0,0.2688980102539062,0,0.3093338012695312,0,0,0.34161376953125,0,0.3546371459960938,0,0.3688507080078125,0,0.3095550537109375,0,0,0,0,0,-2.202133178710938,0,0.2197341918945312,0,0,0.251312255859375,0.2900619506835938,0.3291244506835938,0.35400390625,0.3621139526367188,0,0.385009765625,0,0.07546234130859375,0,0,0,0,0,-2.035697937011719,0,0.2383193969726562,0,0.2744903564453125,0,0.3162078857421875,0.3456192016601562,0,0.3537826538085938,0,0.3739776611328125,0,0.1970138549804688,0,0,0,0,0,-2.034858703613281,0,0.23431396484375,0,0.266876220703125,0,0.30950927734375,0,0.342041015625,0,0,0.3523178100585938,0,0.366424560546875,0,0.2259979248046875,0,0,0,0,0,-2.057357788085938,0,0.2306289672851562,0,0.2612991333007812,0.300537109375,0,0.3381271362304688,0,0.3523941040039062,0,0.3639678955078125,0,0.2719879150390625,0,0,0,-2.033638000488281,0,0.2298431396484375,0,0.2572479248046875,0,0.2935714721679688,0,0.3339157104492188,0,0.354705810546875,0.3621139526367188,0.2629013061523438,0,0,0,0,0,-1.988197326660156,0.2305755615234375,0,0.2591781616210938,0.3007659912109375,0,0.3369369506835938,0,0.354461669921875,0,0,0.36480712890625,0,0.2011032104492188,0,0,0,0,0,0,0,-1.943382263183594,0,0.2302322387695312,0,0,0.2595062255859375,0,0.30084228515625,0.3358535766601562,0.3526535034179688,0,0.3667678833007812,0,0.1561813354492188,0,0,0,0,0,-1.871795654296875,0,0.232330322265625,0.2639389038085938,0,0,0.3044967651367188,0.340179443359375,0.3553390502929688,0,0.3715438842773438,0,0.0617218017578125,0,0,0,0,0,-1.758186340332031,0.2401580810546875,0,0.2786788940429688,0,0.3191909790039062,0,0,0.344512939453125,0.3567962646484375,0.2755889892578125,0,0,0,0,0,-1.896438598632812,0.2219085693359375,0,0.2481231689453125,0,0.2887191772460938,0,0.328155517578125,0.3496932983398438,0,0.3633651733398438,0,0.1523666381835938,0,0,0,0,0,-1.780693054199219,0,0.230621337890625,0,0.2590103149414062,0.3003768920898438,0,0.3349761962890625,0,0,0.3542098999023438,0.3564682006835938,0,0,0,0,0,-1.851715087890625,0,0.2220077514648438,0,0.2421493530273438,0,0,0.2849502563476562,0.3226547241210938,0.35089111328125,0,0.359222412109375,0.1239242553710938,0,0,0,0,0,0,0,0,0,0,0,-1.773147583007812,0,0.2069473266601562,0.2329559326171875,0,0.2611083984375,0,0.2978286743164062,0,0.3333740234375,0,0.3501129150390625,0,0.144012451171875,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.831756591796875,0,0,0,0.237945556640625,0.2604751586914062,0.2929763793945312,0,0.3284912109375,0.333404541015625,0.3079605102539062,0,0.3646392822265625,0,0.40325927734375,0,0.4027023315429688,0,0.4047775268554688,0.4023818969726562,0.3457870483398438,0.329193115234375,0.32867431640625,0.3288040161132812,0,0.3327102661132812,0,0.3300247192382812,0.3295669555664062,0,0,0.3296966552734375,0,0.3285598754882812,0.330780029296875,0.3298416137695312,0,0,0.2298660278320312,0,0,0,0,0,-7.267585754394531,0,0.2472610473632812,0,0,0.2733535766601562,0,0.308502197265625,0,0.33258056640625,0.317962646484375,0.3365631103515625,0.3686065673828125,0.394134521484375,0,0.4067611694335938,0,0,0.4060745239257812,0,0.40460205078125,0.406951904296875,0,0.40643310546875,0,0.4056472778320312,0,0.4055252075195312,0,0.4071273803710938,0,0,0.4067535400390625,0,0.4062728881835938,0.399505615234375,0,0.3862686157226562,0,0.04891204833984375,0,0,0,0,0,-7.05615234375,0.252288818359375,0,0.2807388305664062,0,0.3141250610351562,0,0.3185195922851562,0,0.3228225708007812,0,0.3527603149414062,0,0.3753280639648438,0,0,0.3937530517578125,0,0,0.4035873413085938,0,0.4057540893554688,0,0.4451141357421875,0,0.4069290161132812,0,0.4064559936523438,0,0.4057159423828125,0.4056625366210938,0,0,0.4074554443359375,0,0,0.4066162109375,0.4063339233398438,0.3880157470703125,0,0,0.1630172729492188,0,0,0,0,0,0,0,-7.027259826660156,0,0.2473831176757812,0,0.267120361328125,0,0.29931640625,0,0.3101348876953125,0.3219680786132812,0,0.3488311767578125,0,0,0.3644943237304688,0,0.39178466796875,0,0.401336669921875,0,0,0.4044647216796875,0,0.4046783447265625,0,0.40484619140625,0.4037017822265625,0.4033126831054688,0.404083251953125,0,0.4043350219726562,0.4046173095703125,0,0.4067153930664062,0,0.390289306640625,0,0.2454071044921875,0,0,0,0,0,-6.738655090332031,0.278411865234375,0,0.2816390991210938,0,0.2917022705078125,0,0.31475830078125,0,0.345916748046875,0.358123779296875,0,0.3779983520507812,0.40216064453125,0,0.4028854370117188,0,0.4074935913085938,0.4052810668945312,0.4065322875976562,0.4068145751953125,0,0.4051589965820312,0,0.4078445434570312,0,0,0.4076080322265625,0,0.398529052734375,0,0,0.3855209350585938,0,0.252532958984375,0,0,0,0,0,0,0,0,-6.652450561523438,0,0,0.2501220703125,0.2698593139648438,0,0.2824478149414062,0,0.3126983642578125,0,0.3445281982421875,0.351287841796875,0,0.3699111938476562,0,0.3916168212890625,0,0.3991928100585938,0.4058990478515625,0,0.4046249389648438,0,0.406768798828125,0,0.4064483642578125,0,0.4084701538085938,0,0.4085464477539062,0,0.4103775024414062,0,0.4518508911132812,0,0.392608642578125,0.1803359985351562,0,0,0,0,0,0,0,0,-6.490180969238281,0.2547683715820312,0,0.268798828125,0,0.282501220703125,0.3353347778320312,0.3507919311523438,0,0.3599472045898438,0,0.3768844604492188,0,0,0.3964080810546875,0,0.3955612182617188,0.405120849609375,0,0.4020156860351562,0,0.4037857055664062,0,0,0.4063720703125,0,0.4076309204101562,0.4079818725585938,0.4090805053710938,0,0.4034271240234375,0,0.389190673828125,0,0,0.02648162841796875,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-6.407554626464844,0,0.2373123168945312,0,0.2414321899414062,0,0.2539138793945312,0,0.30633544921875,0,0.334808349609375,0,0.3445816040039062,0.3528289794921875,0.375823974609375,0,0.3913116455078125,0,0,0.3973846435546875,0.3966903686523438,0.4028244018554688,0,0.403594970703125,0,0.403961181640625,0,0.4057540893554688,0.4052963256835938,0,0.4051589965820312,0,0.3862380981445312,0,0.1510696411132812,0,0,0,0,0,0,0,0,-6.272125244140625,0.2430801391601562,0,0.2543411254882812,0.2884750366210938,0.3314590454101562,0,0.3425674438476562,0.3524551391601562,0,0.36920166015625,0,0.3898468017578125,0.3891525268554688,0.3981475830078125,0.3984527587890625,0,0.441680908203125,0,0.4038009643554688,0,0.4048385620117188,0.4046478271484375,0,0.4044265747070312,0,0.3914642333984375,0,0.2498779296875,0,0,0,0,0,-6.255989074707031,0,0.2406463623046875,0,0.2445602416992188,0,0.27569580078125,0,0.3180999755859375,0,0.3418426513671875,0,0.3435897827148438,0,0.35626220703125,0.3823089599609375,0,0.3924179077148438,0.3933029174804688,0.402801513671875,0,0,0.4056625366210938,0,0.4072265625,0.4075775146484375,0,0.408111572265625,0,0.4088592529296875,0,0,0.399383544921875,0,0.3104171752929688,0,0,0,0,0,0,0,0,-6.176994323730469,0,0.2372283935546875,0,0.2633895874023438,0.281463623046875,0.3209686279296875,0,0.3421554565429688,0.3476791381835938,0,0.3611221313476562,0,0.3846282958984375,0,0.3925704956054688,0.3968582153320312,0,7.958145141601562,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7.62939453125,7.62939453125e-06,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,15.2587890625,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7.629417419433594,0,0,0,0,0,0,0,0.0989837646484375,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,15.29621124267578,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"filename":["<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,null,null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,null,null,null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,null,null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,null,null,null,null,"<expr>",null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,null,null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,null,null,"<expr>","<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,null,null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,"<expr>","<expr>",null,null,null,null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,null,null,null,null,null,null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,"<expr>","<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null]},"interval":10,"files":[{"filename":"<expr>","content":"## Generate Large Random Dataset\nn <- 2e6\nx <- runif(n)\ny <- runif(n)\nz <- runif(n)\nXYZ <- cbind(x,y,z)\n\n## Inspect 4 equivalent `row mean` calculations \nprofvis::profvis({\n    m <- rowSums(XYZ)/ncol(XYZ)\n    m <- rowMeans(XYZ)\n    m <- apply(XYZ, 1, mean)\n    m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }\n})\n## rowSums(), colSums(), rowMeans(), and colMeans() are vectorised and fast.\n## for loop is not the slowest, but the ugliest.","normpath":"<expr>"}],"prof_output":"/tmp/RtmpltiHnT/file35f9cd1fc1e.prof","highlight":{"output":["^output\\$"],"gc":["^<GC>$"],"stacktrace":["^\\.\\.stacktraceo(n|ff)\\.\\.$"]},"split":"h"}},"evals":[],"jsHooks":[]}</script>
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
##  mean1(x, 0.5) 19.77924 19.98140 20.23970 19.98764 20.00315 22.82520   100  a 
##  mean2(x, 0.5) 19.08468 19.13639 19.22427 19.14497 19.16051 21.74424   100   b
##  mean3(x, 0.5) 19.59929 19.97322 20.11096 19.97904 19.98987 26.98316   100  a
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
##  ma1(y) 167.49151 186.59471 185.56249 186.93254 187.60397 194.0983   100  a 
##  ma2(y)  18.37438  20.23806  26.74673  22.62764  24.63953 180.3698   100   b
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
##   0.103   0.000   0.033
```

```r
system.time({ lm(Y~X, data=DAT) })
```

```
##    user  system elapsed 
##   0.405   0.020   0.158
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
##   0.026   0.002   0.029
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
##   0.884   0.188   0.607
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

