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
<div class="plotly html-widget html-fill-item" id="htmlwidget-94e7ebb5682db4dbe373" style="width:672px;height:480px;"></div>
<script type="application/json" data-for="htmlwidget-94e7ebb5682db4dbe373">{"x":{"visdat":{"39425929105f":["function () ","plotlyVisDat"]},"cur_data":"39425929105f","attrs":{"39425929105f":{"x":{},"y":{},"alpha_stroke":1,"sizes":[10,100],"spans":[1,20]}},"layout":{"margin":{"b":40,"l":60,"t":25,"r":10},"xaxis":{"domain":[0,1],"automargin":true,"title":"X"},"yaxis":{"domain":[0,1],"automargin":true,"title":"Y"},"hovermode":"closest","showlegend":false},"source":"A","config":{"modeBarButtonsToAdd":["hoverclosest","hovercompare"],"showSendToCloud":false},"data":[{"x":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100],"y":[4.4221910266116371,8.7498083875473789,17.098626284778252,13.365047679609864,19.735181361164074,24.104836696653329,24.380496608697051,29.778991873890948,37.028553255023645,39.882205636616334,42.237114796724647,47.412872548443751,51.629808187059645,54.19214286342428,63.601244592358796,64.049208809921737,67.317389716344294,70.633970557231819,76.453309309061268,82.002133850759975,87.377240542401196,88.142031427983824,90.935678032320638,97.455441077756191,97.626975893848126,108.90129884375831,108.85767268430696,113.4896768015297,114.97135566637793,123.61642639454809,121.09696903402099,127.74444587183862,133.44918390491827,136.14013755819715,144.03813029972312,139.41332366865498,149.20734832183419,153.71890356326722,153.92108238708607,160.12037320252526,161.96213380439471,168.20027772949499,169.96959801121966,173.16887887708572,179.00541126032263,183.95243540012729,187.5217290608455,192.2262610913109,191.51341591111355,198.42897975045335,205.06151018102724,205.96894117539034,214.62029099881852,213.52502238866865,218.98205189212379,223.96203736526283,225.97318981363898,235.1162054146148,237.9589132151784,239.61752459768812,244.96973171606425,247.10381456262834,250.2302209974392,256.63816617475436,259.85479799979328,264.59254569345245,270.48295034284189,270.06985536128445,274.99860146563532,280.46656423634118,283.5802753654861,285.28345993559674,289.20974609310758,296.95620828957288,299.58321499138833,301.97736438505484,304.33895994061646,309.93048276591401,318.25464837546934,316.99098079720744,323.85220694629623,330.19804070512504,332.06623970446827,335.83783770139979,345.19027328148439,340.98995419414678,348.71603491340198,352.70908325185309,356.69001020378016,359.75508833790019,363.94286960083252,365.93138369136796,375.09025658437929,377.30288725717827,380.23876668753525,385.65699576854081,387.96281835650558,388.85031810123826,396.17060062873475,399.04167624760311],"type":"scatter","mode":"markers","marker":{"color":"rgba(31,119,180,1)","line":{"color":"rgba(31,119,180,1)"}},"error_y":{"color":"rgba(31,119,180,1)"},"error_x":{"color":"rgba(31,119,180,1)"},"line":{"color":"rgba(31,119,180,1)"},"xaxis":"x","yaxis":"y","frame":null}],"highlight":{"on":"plotly_click","persistent":false,"dynamic":false,"selectize":false,"opacityDim":0.20000000000000001,"selected":{"opacity":1},"debounce":0},"shinyEvents":["plotly_hover","plotly_click","plotly_selected","plotly_relayout","plotly_brushed","plotly_brushing","plotly_clickannotation","plotly_doubleclick","plotly_deselect","plotly_afterplot","plotly_sunburstclick"],"base_url":"https://plot.ly"},"evals":[],"jsHooks":[]}</script>
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
<div class="profvis html-widget html-fill-item" id="htmlwidget-365d326ec1d90669c191" style="width:100%;height:600px;"></div>
<script type="application/json" data-for="htmlwidget-365d326ec1d90669c191">{"x":{"message":{"prof":{"time":[1,2,3,4,5,6,7,8,9,9,10,10,11,11,12,12,13,13,14,14,15,15,16,16,17,17,18,18,19,19,20,20,21,21,22,22,22,23,23,23,24,25,25,25,26,27,27,28,28,29,29,30,30,31,32,32,32,33,33,34,35,36,36,37,37,38,38,39,39,40,41,41,42,43,44,44,44,45,45,45,46,46,47,47,48,48,48,49,50,50,51,52,52,53,53,54,55,55,55,56,56,56,57,57,58,59,59,60,60,60,61,61,61,62,62,63,63,63,64,64,65,65,66,67,67,68,68,68,69,69,70,71,71,72,72,72,73,74,75,75,76,76,77,77,78,78,79,79,80,80,81,81,81,82,82,82,83,83,84,84,85,86,86,87,87,87,88,89,89,90,90,91,92,92,92,93,93,94,94,95,95,96,96,97,97,98,98,99,99,99,100,100,101,101,102,103,104,104,105,105,106,106,107,107,108,109,110,110,111,111,111,112,113,113,114,114,115,115,116,117,117,118,118,119,119,119,120,120,121,121,122,122,123,124,124,125,125,126,127,127,128,128,129,130,130,131,131,132,133,133,134,134,135,135,136,136,137,137,138,138,139,139,140,140,140,141,142,142,142,143,143,143,144,144,145,145,146,147,147,147,148,148,149,149,150,150,150,151,151,152,153,153,154,154,155,156,156,156,157,157,158,158,159,159,160,160,161,161,162,162,163,164,165,165,166,166,167,167,168,168,169,169,170,170,170,171,172,172,173,173,174,174,175,175,176,177,178,178,179,179,180,180,180,181,182,182,183,183,184,184,185,185,186,186,187,187,187,188,188,188,189,189,189,190,190,190,191,191,191,192,192,192,193,193,193,194,194,194,195,196,196,197,197,198,199,200,200,201,201,202,202,203,204,204,205,205,206,206,207,207,208,209,209,210,210,210,211,212,212,212,213,213,214,215,215,216,216,216,217,217,217,218,218,219,219,220,220,220,221,221,222,223,223,223,224,224,224,225,225,226,226,227,227,228,229,230,230,230,230,231,231,232,232,233,233,234,234,235,235,236,237,237,238,238,239,239,240,241,241,242,242,243,243,244,244,244,245,245,246,246,247,247,248,249,249,250,251,251,251,252,252,253,254,254,255,255,255,256,257,257,257,258,258,259,260,261,262,262,262,263,263,264,264,265,265,266,267,268,268,269,269,270,270,271,272,272,273,273,274,274,274,275,276,276,277,277,278,278,279,280,280,281,281,282,283,283,284,284,285,286,286,287,287,288,288,289,289,289,290,290,290,291,291,292,292,293,293,294,295,295,296,296,297,297,298,298,299,299,300,300,300,301,301,302,302,303,304,305,305,306,307,307,307,308,308,308,309,309,310,310,311,311,312,313,314,314,314,315,316,317,318,318,319,319,319,320,321,322,322,323,323,324,325,325,326,326,327,327,328,328,329,329,330,331,331,331,331,332,332,332,332,333,333,333,333,334,334,334,334,335,335,335,335,336,336,336,336,337,337,337,337,338,338,338,338,339,339,339,339,340,340,340,340,341,341,341,341,342,342,342,342,343,343,343,343,344,344,344,344,345,345,345,345,346,346,346,346,347,347,347,347,348,348,348,348,349,349,349,349,350,350,350,350,351,351,351,351,352,352,352,352,353,353,353,353,354,354,354,354,355,355,356,356,357,358,358,358,359,359,360,360,361,362,362,363,363,363,364,364,364,365,366,367,367,368,368,369,369,370,370,371,371,372,372,372,373,374,374,375,376,376,377,377,378,378,379,380,380,381,382,382,383,383,383,384,384,384,385,385,386,386,387,387,388,389,389,390,391,391,392,392,393,393,393,394,394,395,395,396,396,397,397,398,398,399,400,400,401,401,402,402,403,404,404,405,405,406,406,407,407,408,409,410,411,411,411,412,412,413,413,413,414,414,415,415,416,416,417,417,418,418,419,419,420,421,421,422,422,423,423,424,424,424,424,425,425,426,426,427,427,428,428,429,429,430,430,431,431,432,432,433,434,434,435,436,437,437,437,438,439,439,440,441,442,442,443,443,444,444,445,445,446,447,448,448,449,450,450,450,451,451,451,452,452,453,454,454,455,455,456,456,457,457,457,458,458,459,459,460,460,461,462,462,463,463,463,464,464,464,465,466,466,467,467,468,469,469,470,470,471,472,472,472,473,474,474,475,475,476,476,476,477,477,477,478,478,479,479,480,481,481,482,482,483,483,484,485,486,486,486,487,487,488,488,488,489,489,489,490,490,490,491,491,492,493,493,494,494,495,495,495,496,496,497,498,499,499,499,500,501,501,502,502,503,503,503,504,504,505,505,506,507,507,508,509,510,511,511,512,512,513,514,514,515,515,515,516,516,517,517,518,518,519,519,520,520,520,521,521,522,523,524,525,525,526,527,527,528,529,529,530,530,531,532,532,533,533,534,534,535,535,536,536,537,538,539,539,539,539,540,540,540,540,541,541,542,543,543,544,544,545,545,546,546,547,548,548,549,550,550,551,552,552,552,553,553,554,554,555,556,557,557,558,559,559,560,561,562,562,563,564,564,564,565,566,566,567,568,568,569,570,570,571,572,572,573,573,574,574,575,575,576,576,576,577,578,578,579,580,581,581,581,582,582,583,584,584,585,585,586,586,587,587,588,588,588,589,589,590,590,591,591,592,592,593,593,594,594,594,595,595,596,596,597,597,598,598,599,599,599,600,600,600,601,602,602,603,603,604,604,605,606,606,607,608,609,609,610,610,611,611,611,612,612,612,613,613,614,614,615,616,617,617,618,619,619,620,621,621,622,623,623,624,624,625,625,626,626,627,627,628,628,629,629,630,630,631,631,632,632,633,633,634,634,635,635,636,636,637,638,638,639,640,641,641,642,643,644,645,645,646,646,646,647,647,647,648,648,649,650,651,651,652,652,653,653,654,654,655,655,656,657,657,657,658,658,659,659,660,660,661,661,662,662,663,663,664,664,664,665,665,665,666,666,667,668,668,669,669,670,671,671,672,672,673,673,674,674,675,675,676,676,677,677,678,678,679,679,680,680,680,681,681,682,682,683,683,684,684,685,685,686,686,687,688,688,689,690,691,691,692,692,693,693,694,694,695,695,696,696,697,697,698,699,699,700,700,701,701,702,702,702,703,703,703,704,704,705,705,706,706,707,707,708,708,709,710,710,710,711,712,712,713,713,713,714,714,715,715,716,716,717,718,718,719,719,720,721,722,723,723,724,724,725,726,726,727,728,729,729,730,730,731,731,732,732,733,733,734,734,734,735,735,736,736,737,737,738,738,739,740,740,741,742,742,743,743,744,744,744,745,745,745,746,746,747,748,748,749,749,750,751,751,752,752,753,753,754,754,755,755,755,756,756,757,757,758,758,759,759,760,761,761,762,762,763,764,765,765,765,766,766,766,767,767,768,768,769,770,771,771,772,772,773,773,774,775,775,775,776,776,776,777,777,778,778,779,779,780,780,781,782,783,783,784,784,785,785,785,786,786,786,787,788,789,790,790,790,791,791,792,792,793,793,793,794,794,795,795,795,796,796,796,797,797,798,798,799,799,800,800,801,801,802,803,804,804,805,805,805,806,806,806,807,807,808,808,809,810,810,811,812,812,813,814,814,815,815,816,816,817,817,818,818,819,819,820,820,820,821,821,821,822,822,823,824,824,825,825,826,826,827,827,828,829,830,830,831,831,832,832,833,834,834,835,836,836,837,837,838,838,839,840,840,841,842,843,843,843,844,844,844,845,846,847,847,848,848,849,850,850,851,852,852,852,853,853,853,854,854,854,855,855,855,856,856,856,857,857,857,858,858,858,859,859,859,860,860,860,861,861,861,862,862,862,863,863,864,864,865,865,866,867,867,867,868,868,869,869,870,870,870,871,871,871,872,872,872,873,873,874,874,875,876,876,877,877,878,878,879,879,880,880,881,881,882,882,883,883,884,884,884,885,886,887,888,889,889,890,890,891,891,892,892,893,893,894,894,895,895,896,897,897,898,898,898,899,899,899,900,900,901,901,902,903,904,905,905,906,907,907,907,908,908,908,909,909,910,911,912,913,914,915,915,916,916,916,917,917,918,919,919,920,920,921,922,922,923,923,924,924,924,925,925,925,926,926,927,928,928,929,930,930,931,931,932,932,932,933,933,934,935,935,936,937,937,938,938,939,939,940,940,940,941,941,942,942,943,944,944,945,945,945,946,947,947,948,948,949,949,949,950,950,950,951,951,952,953,953,954,955,955,956,956,957,957,958,958,958,959,960,961,962,962,963,963,964,964,965,965,966,966,966,967,967,967,968,968,969,970,971,971,971,972,972,973,973,973,974,974,974,975,975,975,976,977,978,978,979,980,981,981,982,982,983,983,984,984,985,985,985,986,987,987,987,988,989,990,990,990,991,991,991,992,992,992,993,993,993,994,994,994,995,995,995,996,997,997,998,998,999,999,1000,1001,1001,1002,1003,1003,1003,1004,1004,1004,1005,1005,1005,1006,1006,1006,1007,1007,1007,1008,1008,1008,1009,1009,1009,1010,1010,1010,1011,1011,1011,1012,1012,1012,1013,1013,1013,1014,1014,1014,1015,1015,1015,1016,1016,1016,1017,1017,1017,1018,1018,1018,1019,1019,1019,1020,1020,1020,1021,1021,1021,1022,1022,1022,1023,1023,1023,1024,1024,1024,1025,1025,1025,1026,1026,1026,1027,1027,1027,1028,1028,1028,1029,1029,1029,1030,1030,1030,1031,1031,1031,1032,1032,1032,1033,1033,1033,1034,1034,1034,1035,1035,1035,1036,1036,1036,1037,1037,1037,1038,1038,1038,1039,1039,1039,1040,1040,1040,1041,1041,1041,1042,1042,1042,1043,1043,1043,1044,1044,1044,1045,1045,1045,1046,1046,1046,1047,1047,1047,1048,1048,1048,1049,1049,1049,1050,1050,1050,1051,1051,1051,1052,1052,1052,1053,1054,1055,1055,1056,1056,1057,1057,1058,1059,1059,1060,1060,1061,1061,1062,1062,1063,1063,1064,1064,1065,1065,1065,1066,1067,1068,1068,1069,1069,1070,1071,1071,1072,1073,1073,1073,1074,1074,1075,1075,1076,1076,1077,1078,1079,1079,1080,1080,1081,1081,1082,1083,1084,1084,1085,1085,1086,1086,1087,1088,1088,1089,1090,1090,1091,1091,1092,1092,1093,1094,1094,1095,1095,1096,1097,1097,1097,1098,1098,1098,1099,1099,1100,1101,1101,1101,1102,1102,1103,1103,1103,1104,1104,1105,1105,1106,1106,1107,1107,1108,1109,1109,1110,1110,1111,1112,1112,1113,1113,1114,1115,1115,1115,1116,1117,1118,1118,1119,1119,1119,1120,1120,1120,1121,1121,1122,1123,1123,1124,1125,1125,1126,1126,1127,1128,1128,1129,1129,1130,1131,1132,1132,1132,1133,1134,1134,1135,1135,1136,1136,1137,1137,1138,1138,1139,1140,1141,1141,1141,1142,1142,1142,1143,1144,1144,1145,1145,1146,1146,1147,1148,1149,1149,1150,1150,1151,1151,1152,1152,1153,1154,1155,1155,1156,1156,1157,1157,1158,1158,1158,1159,1159,1160,1160,1161,1161,1162,1162,1162,1163,1163,1163,1164,1164,1164,1165,1165,1166,1166,1167,1168,1169,1170,1170,1171,1171,1172,1173,1173,1173,1174,1175,1176,1177,1178,1178,1178,1179,1179,1180,1180,1181,1181,1182,1183,1183,1184,1184,1184,1185,1185,1185,1186,1187,1187,1187,1188,1188,1189,1189,1190,1190,1191,1191,1192,1193,1193,1193,1194,1194,1195,1196,1196,1197,1197,1198,1198,1199,1199,1200,1201,1202,1202,1203,1203,1204,1204,1205,1205,1205,1206,1206,1206,1207,1207,1207,1208,1208,1208,1209,1209,1209,1210,1210,1210,1211,1211,1211,1212,1212,1212,1213,1213,1214,1215,1216,1216,1217,1218,1219,1219,1220,1221,1222,1223,1223,1224,1224,1224,1225,1226,1226,1226,1227,1228,1228,1229,1229,1230,1230,1230,1231,1231,1232,1232,1233,1233,1234,1234,1235,1235,1236,1237,1238,1238,1239,1240,1241,1242,1242,1243,1243,1244,1244,1245,1246,1246,1246,1247,1248,1248,1249,1249,1249,1250,1250,1251,1251,1252,1252,1253,1253,1253,1253,1254,1254,1254,1254,1255,1255,1256,1256,1257,1258,1258,1259,1260,1261,1262,1263,1263,1264,1264,1264,1265,1265,1266,1266,1267,1267,1267,1268,1268,1268,1269,1269,1270,1270,1271,1272,1272,1273,1273,1274,1274,1274,1275,1275,1275,1276,1277,1278,1278,1279,1279,1279,1280,1280,1281,1281,1282,1282,1283,1283,1284,1284,1285,1285,1286,1286,1287,1287,1288,1288,1289,1289,1290,1290,1291,1291,1292,1292,1293,1293,1294,1294,1295,1295,1296,1297,1297,1298,1298,1299,1299,1300,1300,1301,1301,1302,1302,1303,1303,1304,1304,1305,1305,1306,1306,1307,1307,1308,1308,1309,1309,1310,1310,1311,1311,1312,1312,1313,1313,1314,1314,1315,1315,1316,1316,1316,1316,1316,1316,1316,1316,1316,1316,1316,1316,1316,1316,1316,1316,1316,1316,1316,1316,1316,1317,1317,1317,1317,1317,1317,1317,1317,1318,1318,1318,1318,1318,1318,1318,1318,1319,1319,1319,1319,1319,1319,1319,1319,1320,1320,1320,1320,1320,1320,1320,1320,1321,1321,1321,1321,1321,1321,1321,1321,1322,1322,1322,1322,1322,1322,1322,1322,1323,1323,1323,1323,1323,1323,1323,1323,1324,1324,1324,1324,1324,1324,1324,1324,1325,1325,1325,1325,1325,1325,1325,1325,1326,1326,1326,1326,1326,1326,1326,1326,1327,1327,1327,1327,1327,1327,1327,1327,1328,1328,1328,1328,1328,1328,1328,1328,1329,1329,1329,1329,1329,1329,1329,1329,1330,1330,1330,1330,1330,1330,1330,1330,1331,1331,1331,1331,1331,1331,1331,1331,1332,1332,1332,1332,1332,1332,1332,1332,1333,1333,1333,1333,1333,1333,1333,1333],"depth":[1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,1,3,2,1,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,1,1,2,1,2,1,2,1,2,1,1,2,1,1,1,3,2,1,3,2,1,2,1,2,1,3,2,1,1,2,1,1,2,1,2,1,1,3,2,1,3,2,1,2,1,1,2,1,3,2,1,3,2,1,2,1,3,2,1,2,1,2,1,1,2,1,3,2,1,2,1,1,2,1,3,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,3,2,1,1,2,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,1,1,2,1,3,2,1,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,3,2,1,3,2,1,2,1,2,1,1,3,2,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,1,2,1,2,1,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,1,3,2,1,2,1,1,2,1,3,2,1,3,2,1,2,1,2,1,3,2,1,2,1,1,3,2,1,3,2,1,2,1,2,1,2,1,1,1,4,3,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,1,3,2,1,2,1,1,2,1,3,2,1,1,3,2,1,2,1,1,1,1,3,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,1,2,1,1,3,2,1,3,2,1,2,1,2,1,2,1,1,1,3,2,1,1,1,1,2,1,3,2,1,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,2,1,2,1,1,3,2,1,2,1,2,1,1,2,1,3,2,1,3,2,1,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,1,2,1,2,1,2,1,1,2,1,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,1,1,3,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,4,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,1,3,2,1,1,2,1,1,1,2,1,2,1,2,1,2,1,1,1,2,1,1,3,2,1,3,2,1,2,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,3,2,1,3,2,1,1,2,1,2,1,1,2,1,2,1,1,3,2,1,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,1,1,3,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,3,2,1,2,1,1,1,3,2,1,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,1,1,1,2,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,1,1,2,1,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,1,4,3,2,1,4,3,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,1,3,2,1,2,1,2,1,1,1,2,1,1,2,1,1,1,2,1,1,3,2,1,1,2,1,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,1,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,1,2,1,1,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,1,1,2,1,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,1,2,1,1,1,1,2,1,3,2,1,3,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,1,1,1,2,1,2,1,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,1,3,2,1,3,2,1,2,1,2,1,1,1,2,1,2,1,2,1,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,3,2,1,3,2,1,1,1,1,3,2,1,2,1,2,1,3,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,1,2,1,1,1,3,2,1,3,2,1,1,1,2,1,2,1,1,2,1,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,3,2,1,2,1,2,1,1,1,1,2,1,1,3,2,1,3,2,1,2,1,1,1,1,1,1,2,1,3,2,1,2,1,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,2,1,1,2,1,1,2,1,2,1,3,2,1,2,1,1,2,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,3,2,1,1,2,1,2,1,3,2,1,3,2,1,2,1,1,2,1,1,2,1,2,1,2,1,3,2,1,1,1,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,1,1,3,2,1,2,1,3,2,1,3,2,1,3,2,1,1,1,2,1,1,1,2,1,2,1,2,1,2,1,3,2,1,1,3,2,1,1,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,1,2,1,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,1,2,1,2,1,1,2,1,1,3,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,1,3,2,1,3,2,1,2,1,1,3,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,1,3,2,1,1,1,2,1,3,2,1,3,2,1,2,1,1,2,1,1,2,1,2,1,1,2,1,2,1,1,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,1,1,3,2,1,3,2,1,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,1,1,1,2,1,2,1,1,3,2,1,1,1,1,1,3,2,1,2,1,2,1,2,1,1,2,1,3,2,1,3,2,1,1,3,2,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,1,1,2,1,1,1,2,1,1,1,1,2,1,3,2,1,1,3,2,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,1,1,1,2,1,2,1,2,1,1,3,2,1,1,2,1,3,2,1,2,1,2,1,2,1,4,3,2,1,4,3,2,1,2,1,2,1,1,2,1,1,1,1,1,2,1,3,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1],"label":["rowSums","rowSums","rowSums","rowSums","rowMeans","rowMeans","rowMeans","rowMeans","aperm.default","apply","aperm.default","apply","aperm.default","apply","aperm.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","apply","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","FUN","apply","FUN","apply","<GC>","apply","FUN","apply","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","FUN","apply","mean.default","apply","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","<GC>","apply","isTRUE","mean.default","apply","apply","apply","length","local","FUN","apply","FUN","apply","mean.default","apply","<GC>","apply","mean.default","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","<GC>","FUN","apply","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","<GC>","apply","is.na","local","FUN","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","apply","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","apply","mean.default","apply","<GC>","length","local","apply","FUN","apply","is.na","local","FUN","apply","apply","mean.default","apply","length","local","<GC>","FUN","apply","FUN","apply","is.numeric","local","FUN","apply","apply","FUN","apply","mean.default","apply","apply","<GC>","apply","FUN","apply","apply","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","<GC>","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","is.na","local","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","<GC>","FUN","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","apply","isTRUE","mean.default","apply","<GC>","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","apply","<GC>","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","apply","<GC>","apply","mean.default","apply","FUN","apply","FUN","apply","apply","apply","length","local","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","mean.default","apply","is.na","local","mean.default","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","is.numeric","local","FUN","apply","apply","apply","FUN","apply","FUN","apply","<GC>","apply","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","<GC>","FUN","apply","apply","isTRUE","mean.default","apply","mean.default","apply","apply","mean.default","apply","isTRUE","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","apply","<GC>","isTRUE","mean.default","apply","length","local","FUN","apply","is.na","local","FUN","apply","FUN","apply","apply","<GC>","apply","FUN","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","FUN","apply","<GC>","FUN","apply","mean.default","apply","is.numeric","local","FUN","apply","apply","FUN","apply","apply","<GC>","FUN","apply","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","apply","<GC>","mean.default","apply","is.numeric","local","apply","apply","apply","isTRUE","mean.default","apply","mean.default","apply","<GC>","apply","FUN","apply","apply","apply","FUN","apply","mean.default","apply","<GC>","apply","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","<GC>","apply","FUN","apply","apply","mean.default","apply","FUN","apply","apply","<GC>","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","<GC>","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","<GC>","apply","length","local","apply","apply","FUN","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","length","local","apply","apply","<GC>","mean.default","apply","apply","apply","apply","FUN","apply","<GC>","mean.default","apply","apply","apply","mean.default","apply","FUN","apply","apply","<GC>","apply","length","local","FUN","apply","FUN","apply","FUN","apply","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","is.numeric","local","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","apply","length","local","mean.default","apply","FUN","apply","<GC>","apply","mean.default","apply","isTRUE","mean.default","apply","apply","length","local","apply","is.numeric","local","mean.default","apply","FUN","apply","apply","mean.default","apply","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","apply","FUN","apply","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","is.na","local","mean.default","apply","mean.default","apply","<GC>","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","length","local","mean.default","apply","mean.default","apply","length","local","apply","apply","apply","<GC>","FUN","apply","is.numeric","local","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","FUN","apply","length","local","FUN","apply","<GC>","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","is.na","local","is.na","local","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","mean.default","apply","apply","apply","<GC>","mean.default","apply","apply","mean.default","apply","apply","apply","mean.default","apply","mean.default","apply","mean.default","apply","is.na","local","apply","apply","FUN","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","is.numeric","local","FUN","apply","apply","FUN","apply","<GC>","is.numeric","local","<GC>","is.numeric","local","apply","FUN","apply","FUN","apply","apply","mean.default","apply","is.numeric","local","apply","isTRUE","mean.default","apply","apply","mean.default","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","apply","apply","isTRUE","mean.default","apply","apply","FUN","apply","<GC>","apply","isTRUE","mean.default","apply","length","local","FUN","apply","apply","FUN","apply","apply","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","apply","is.na","local","apply","<GC>","apply","apply","FUN","apply","FUN","apply","apply","mean.default","apply","is.numeric","local","FUN","apply","mean.default","apply","mean.default","apply","apply","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","apply","mean.default","apply","apply","length","local","apply","<GC>","length","local","FUN","apply","mean.default","apply","apply","apply","mean.default","apply","apply","FUN","apply","apply","apply","FUN","apply","apply","<GC>","FUN","apply","apply","mean.default","apply","apply","FUN","apply","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","mean.default","apply","is.numeric","local","<GC>","FUN","apply","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","<GC>","FUN","apply","is.numeric","local","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","is.numeric","local","<GC>","length","local","<GC>","length","local","apply","mean.default","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","apply","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","is.na","local","apply","apply","mean.default","apply","apply","FUN","apply","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","apply","apply","mean.default","apply","apply","apply","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","<GC>","apply","FUN","apply","FUN","apply","FUN","apply","length","local","mean.default","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","is.na","local","apply","mean.default","apply","<GC>","apply","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","length","local","is.na","local","length","local","<GC>","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","apply","FUN","apply","apply","apply","<GC>","apply","<GC>","apply","FUN","apply","length","local","mean.default","apply","is.na","local","mean.default","apply","apply","FUN","apply","FUN","apply","mean.default","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","length","local","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","apply","mean.default","apply","mean.default","apply","apply","apply","apply","<GC>","apply","<GC>","apply","apply","FUN","apply","apply","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","<GC>","FUN","apply","mean.default","apply","is.na","local","length","local","length","local","apply","FUN","apply","apply","FUN","apply","length","local","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","<GC>","mean.default","apply","is.numeric","local","FUN","apply","FUN","apply","length","local","apply","FUN","apply","mean.default","apply","apply","apply","<GC>","is.numeric","local","<GC>","is.numeric","local","FUN","apply","FUN","apply","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","apply","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","is.numeric","local","FUN","apply","is.numeric","local","FUN","apply","FUN","apply","apply","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","is.na","local","FUN","apply","apply","mean.default","apply","apply","mean.default","apply","apply","FUN","apply","<GC>","apply","mean.default","apply","mean.default","apply","is.numeric","local","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","is.numeric","local","mean.default","apply","apply","apply","mean.default","apply","FUN","apply","length","local","apply","<GC>","apply","apply","mean.default","apply","length","local","mean.default","apply","apply","FUN","apply","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","is.numeric","local","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","<GC>","apply","<GC>","apply","mean.default","apply","length","local","isTRUE","mean.default","apply","apply","apply","apply","apply","<GC>","apply","<GC>","apply","mean.default","apply","FUN","apply","FUN","apply","is.na","local","mean.default","apply","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","is.numeric","local","FUN","apply","apply","apply","apply","mean.default","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","apply","apply","apply","apply","apply","FUN","apply","<GC>","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","mean.default","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","length","local","apply","mean.default","apply","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","<GC>","apply","apply","mean.default","apply","apply","is.numeric","local","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","<GC>","apply","<GC>","apply","apply","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","apply","FUN","apply","apply","is.numeric","local","mean.default","apply","FUN","apply","<GC>","length","local","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","apply","FUN","apply","apply","apply","mean.default","apply","<GC>","apply","<GC>","apply","FUN","apply","isTRUE","mean.default","apply","apply","isTRUE","mean.default","apply","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","mean.default","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","apply","mean.default","apply","FUN","apply","FUN","apply","apply","mean.default","apply","FUN","apply","is.na","local","is.na","local","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","is.numeric","local","FUN","apply","apply","mean.default","apply","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","apply","<GC>","apply","apply","apply","FUN","apply","is.na","local","FUN","apply","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","apply","mean.default","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","FUN","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","is.numeric","local","apply","FUN","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","mean.default","apply","apply","apply","isTRUE","mean.default","apply","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","is.na","local","apply","apply","apply","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","apply","apply","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","apply","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","apply","apply","FUN","apply","apply","apply","mean.default","apply","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","apply","isTRUE","mean.default","apply","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","is.numeric","local","<GC>","apply","<GC>","apply","<GC>","apply","is.na","local","apply","apply","FUN","apply","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","FUN","apply","FUN","apply","apply","is.na","local","apply","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","apply","mean.default","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","is.numeric","local","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","%in%","checkSkipLoopCntxt","checkSkipLoopCntxtList","checkSkipLoopCntxt","checkSkipLoopCntxtList","checkSkipLoopCntxt","checkSkipLoopCntxtList","checkSkipLoopCntxt","checkSkipLoopCntxtList","checkSkipLoopCntxt","checkSkipLoopCntxtList","checkSkipLoopCntxt","checkSkipLoopCntxtList","checkSkipLoopCntxt","h","tryInline","cmpCall","cmp","genCode","compile","compiler:::tryCompile","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis"],"filenum":[1,1,1,1,1,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,1,null,null,1,1,null,1,null,1,null,1,null,1,1,null,null,1,null,1,1,1,null,1,null,1,null,1,null,1,1,null,1,1,1,null,null,1,null,null,1,null,1,null,1,null,null,1,1,null,1,1,null,1,null,1,1,null,null,1,null,null,1,null,1,1,null,1,null,null,1,null,null,1,null,1,null,null,1,null,1,null,1,1,null,1,null,null,1,null,1,1,null,1,null,null,1,1,1,null,null,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,1,null,1,1,null,1,null,null,1,1,null,1,null,1,1,null,null,1,null,1,null,1,null,1,null,null,null,1,null,1,null,null,1,null,1,null,1,1,1,null,1,null,1,null,1,null,1,1,1,null,1,null,null,null,1,null,1,null,null,null,1,1,null,1,null,null,null,null,1,null,1,null,null,null,1,1,null,1,null,1,1,null,1,null,1,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,1,null,null,1,null,null,1,null,1,null,null,1,null,null,1,null,1,null,1,null,null,1,null,1,1,null,1,null,1,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,1,null,1,null,1,null,1,null,1,null,1,null,null,1,1,null,1,null,1,null,1,null,1,1,1,null,null,null,1,null,null,1,1,null,1,null,1,null,null,null,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,1,null,null,null,1,1,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,1,null,1,null,null,1,1,null,null,1,null,1,1,null,1,null,null,1,null,null,1,null,1,null,1,null,null,1,null,1,1,null,null,1,null,null,1,null,1,null,1,null,1,1,1,null,null,null,1,null,null,null,1,null,null,null,1,null,1,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,null,1,null,1,null,null,null,1,1,null,1,1,null,null,1,null,1,1,null,1,null,null,1,1,null,null,1,null,null,1,1,1,null,null,1,null,1,null,1,null,1,1,1,null,1,null,1,null,1,1,null,1,null,1,null,null,1,1,null,1,null,1,null,1,1,null,1,null,1,1,null,1,null,1,1,null,1,null,1,null,1,null,null,1,null,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,null,1,1,null,1,1,null,null,1,null,null,1,null,1,null,1,null,null,1,1,null,null,1,1,1,1,null,1,null,null,1,1,1,null,1,null,1,1,null,1,null,null,null,1,null,1,null,1,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,1,null,1,1,null,null,1,null,null,null,1,1,null,1,null,null,1,null,null,1,1,1,null,null,null,1,null,1,null,1,null,1,null,null,1,1,null,null,1,null,null,null,1,null,1,1,null,1,1,null,1,null,null,1,null,null,1,null,1,null,1,null,1,1,null,1,1,null,1,null,1,null,null,1,null,null,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,1,null,null,null,1,null,1,null,null,1,1,1,null,null,1,null,null,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,null,null,1,null,null,null,1,null,1,null,1,null,null,null,null,null,1,null,1,null,1,null,1,1,null,1,1,1,null,null,1,1,null,1,1,1,null,1,null,1,null,1,null,null,1,1,null,1,1,null,null,1,null,null,1,null,1,1,null,1,null,1,null,1,null,null,1,null,1,null,null,null,1,1,null,1,null,null,null,null,null,null,1,null,1,null,1,1,null,1,null,null,1,null,null,1,1,null,1,null,1,null,null,1,null,null,1,null,1,null,1,1,null,1,null,1,null,1,1,1,null,null,1,null,1,null,null,1,null,null,1,null,null,1,null,1,1,null,1,null,1,null,null,1,null,1,1,1,null,null,1,1,null,1,null,1,null,null,1,null,null,null,1,1,null,1,1,1,1,null,1,null,1,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,1,1,1,null,null,1,null,1,1,null,1,null,1,1,null,1,null,null,null,1,null,1,null,1,1,1,null,null,null,1,null,null,null,1,null,1,1,null,1,null,1,null,1,null,1,1,null,1,1,null,null,1,null,null,null,null,1,null,1,1,1,null,1,1,null,1,1,1,null,1,1,null,null,1,1,null,1,1,null,1,1,null,1,1,null,1,null,1,null,1,null,null,null,null,1,1,null,1,1,1,null,null,1,null,1,1,null,1,null,1,null,1,null,1,null,null,1,null,null,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,null,null,null,null,null,null,null,1,null,1,null,1,null,1,1,null,1,1,1,null,1,null,1,null,null,1,null,null,1,null,1,null,null,1,1,null,1,1,null,1,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,1,1,null,1,1,1,1,null,1,null,null,1,null,null,1,null,1,1,1,null,1,null,1,null,1,null,1,null,1,1,null,null,1,null,1,null,1,null,1,null,1,null,null,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,null,null,null,null,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,1,1,null,1,null,1,null,1,null,null,null,1,null,null,null,1,1,null,1,null,1,null,1,null,null,1,null,null,1,null,null,null,1,null,1,null,1,null,1,1,null,null,1,1,null,1,null,null,1,null,1,null,1,null,1,1,null,1,null,1,1,1,1,null,1,null,1,1,null,1,1,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,null,null,null,null,null,1,null,1,1,null,1,null,null,null,null,1,null,null,1,null,1,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,null,1,null,null,null,1,null,1,null,null,1,null,1,null,1,1,1,null,null,null,null,null,null,null,1,null,1,1,1,null,1,null,1,null,1,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,1,1,null,1,null,1,null,null,1,null,null,1,1,1,1,null,null,1,null,1,null,1,null,null,1,null,1,null,null,1,null,null,1,null,null,null,1,null,null,null,1,null,1,1,1,null,1,null,null,1,null,null,1,null,null,null,1,1,null,1,1,null,1,1,null,1,null,1,null,1,null,1,null,null,null,1,null,null,1,null,null,1,null,1,1,null,1,null,1,null,null,null,1,1,1,null,1,null,1,null,null,1,null,1,1,null,1,null,null,null,1,1,null,1,1,1,null,null,1,null,null,1,1,1,null,1,null,1,1,null,1,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,1,1,null,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,null,null,1,1,1,1,1,null,1,null,1,null,1,null,1,null,1,null,null,null,1,1,null,1,null,null,1,null,null,1,null,null,null,1,1,1,1,null,1,1,null,null,1,null,null,1,null,1,1,1,1,1,1,null,1,null,null,1,null,1,1,null,1,null,1,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,1,1,null,1,null,1,null,null,1,null,1,1,null,1,1,null,null,null,1,null,1,null,null,1,null,1,null,1,1,null,1,null,null,1,1,null,1,null,1,null,null,1,null,null,1,null,1,1,null,1,1,null,null,null,1,null,1,null,null,null,1,1,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,1,1,1,null,null,1,null,1,null,null,1,null,null,1,null,null,1,1,1,null,1,1,1,null,1,null,1,null,1,null,1,null,null,1,1,null,null,1,1,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,1,null,1,null,1,null,1,1,null,1,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,1,1,null,1,null,1,null,1,1,null,1,null,1,null,null,null,null,null,1,null,1,null,null,1,1,1,null,null,null,1,1,null,1,1,null,null,1,null,1,null,1,null,1,1,1,null,1,null,null,null,1,1,1,null,1,null,1,null,1,1,null,1,1,null,1,null,1,null,1,1,null,1,null,1,1,null,null,1,null,null,1,null,1,1,null,null,1,null,1,null,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,1,null,1,null,1,1,null,null,1,1,1,null,1,null,null,1,null,null,1,null,1,1,null,1,1,null,1,null,1,1,null,1,null,1,1,1,null,null,1,1,null,1,null,1,null,1,null,1,null,1,1,1,null,null,1,null,null,1,1,null,1,null,1,null,1,1,1,null,1,null,1,null,1,null,1,1,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,1,null,null,1,1,1,null,1,null,1,1,null,null,1,1,1,1,1,null,null,1,null,1,null,1,null,1,1,null,1,null,null,1,null,null,1,1,null,null,1,null,1,null,1,null,1,null,1,1,null,null,1,null,1,1,null,1,null,1,null,1,null,1,1,1,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,1,1,null,1,1,1,null,1,1,1,1,null,1,null,null,1,1,null,null,1,1,null,1,null,1,null,null,1,null,null,null,1,null,1,null,1,null,null,1,1,null,1,1,1,1,null,1,null,1,null,1,1,null,null,1,1,null,1,null,null,1,null,1,null,1,null,1,null,null,null,1,null,null,null,1,null,1,null,1,1,null,null,1,1,1,1,null,1,null,null,1,null,1,null,1,null,null,1,null,null,1,null,1,null,1,1,null,1,null,1,null,null,1,null,null,1,1,1,null,1,null,null,1,null,1,null,1,null,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,1,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null],"linenum":[10,10,10,10,11,11,11,11,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,12,null,null,12,12,null,12,null,12,null,12,null,12,12,null,null,12,null,12,12,12,null,12,null,12,null,12,null,12,12,null,12,12,12,null,null,12,null,null,12,null,12,null,12,null,null,12,12,null,12,12,null,12,null,12,12,null,null,12,null,null,12,null,12,12,null,12,null,null,12,null,null,12,null,12,null,null,12,null,12,null,12,12,null,12,null,null,12,null,12,12,null,12,null,null,12,12,12,null,null,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,12,null,12,12,null,12,null,null,12,12,null,12,null,12,12,null,null,12,null,12,null,12,null,12,null,null,null,12,null,12,null,null,12,null,12,null,12,12,12,null,12,null,12,null,12,null,12,12,12,null,12,null,null,null,12,null,12,null,null,null,12,12,null,12,null,null,null,null,12,null,12,null,null,null,12,12,null,12,null,12,12,null,12,null,12,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,12,null,null,12,null,null,12,null,12,null,null,12,null,null,12,null,12,null,12,null,null,12,null,12,12,null,12,null,12,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,12,null,12,null,12,null,12,null,12,null,12,null,null,12,12,null,12,null,12,null,12,null,12,12,12,null,null,null,12,null,null,12,12,null,12,null,12,null,null,null,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,12,null,null,null,12,12,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,12,null,12,null,null,12,12,null,null,12,null,12,12,null,12,null,null,12,null,null,12,null,12,null,12,null,null,12,null,12,12,null,null,12,null,null,12,null,12,null,12,null,12,12,12,null,null,null,12,null,null,null,12,null,null,null,12,null,12,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,null,12,null,12,null,null,null,12,12,null,12,12,null,null,12,null,12,12,null,12,null,null,12,12,null,null,12,null,null,12,12,12,null,null,12,null,12,null,12,null,12,12,12,null,12,null,12,null,12,12,null,12,null,12,null,null,12,12,null,12,null,12,null,12,12,null,12,null,12,12,null,12,null,12,12,null,12,null,12,null,12,null,null,12,null,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,null,12,12,null,12,12,null,null,12,null,null,12,null,12,null,12,null,null,12,12,null,null,12,12,12,12,null,12,null,null,12,12,12,null,12,null,12,12,null,12,null,null,null,12,null,12,null,12,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,12,null,12,12,null,null,12,null,null,null,12,12,null,12,null,null,12,null,null,12,12,12,null,null,null,12,null,12,null,12,null,12,null,null,12,12,null,null,12,null,null,null,12,null,12,12,null,12,12,null,12,null,null,12,null,null,12,null,12,null,12,null,12,12,null,12,12,null,12,null,12,null,null,12,null,null,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,12,null,null,null,12,null,12,null,null,12,12,12,null,null,12,null,null,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,null,null,12,null,null,null,12,null,12,null,12,null,null,null,null,null,12,null,12,null,12,null,12,12,null,12,12,12,null,null,12,12,null,12,12,12,null,12,null,12,null,12,null,null,12,12,null,12,12,null,null,12,null,null,12,null,12,12,null,12,null,12,null,12,null,null,12,null,12,null,null,null,12,12,null,12,null,null,null,null,null,null,12,null,12,null,12,12,null,12,null,null,12,null,null,12,12,null,12,null,12,null,null,12,null,null,12,null,12,null,12,12,null,12,null,12,null,12,12,12,null,null,12,null,12,null,null,12,null,null,12,null,null,12,null,12,12,null,12,null,12,null,null,12,null,12,12,12,null,null,12,12,null,12,null,12,null,null,12,null,null,null,12,12,null,12,12,12,12,null,12,null,12,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,12,12,12,null,null,12,null,12,12,null,12,null,12,12,null,12,null,null,null,12,null,12,null,12,12,12,null,null,null,12,null,null,null,12,null,12,12,null,12,null,12,null,12,null,12,12,null,12,12,null,null,12,null,null,null,null,12,null,12,12,12,null,12,12,null,12,12,12,null,12,12,null,null,12,12,null,12,12,null,12,12,null,12,12,null,12,null,12,null,12,null,null,null,null,12,12,null,12,12,12,null,null,12,null,12,12,null,12,null,12,null,12,null,12,null,null,12,null,null,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,null,null,null,null,null,null,null,12,null,12,null,12,null,12,12,null,12,12,12,null,12,null,12,null,null,12,null,null,12,null,12,null,null,12,12,null,12,12,null,12,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,12,12,null,12,12,12,12,null,12,null,null,12,null,null,12,null,12,12,12,null,12,null,12,null,12,null,12,null,12,12,null,null,12,null,12,null,12,null,12,null,12,null,null,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,null,null,null,null,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,12,12,null,12,null,12,null,12,null,null,null,12,null,null,null,12,12,null,12,null,12,null,12,null,null,12,null,null,12,null,null,null,12,null,12,null,12,null,12,12,null,null,12,12,null,12,null,null,12,null,12,null,12,null,12,12,null,12,null,12,12,12,12,null,12,null,12,12,null,12,12,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,null,null,null,null,null,12,null,12,12,null,12,null,null,null,null,12,null,null,12,null,12,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,null,12,null,null,null,12,null,12,null,null,12,null,12,null,12,12,12,null,null,null,null,null,null,null,12,null,12,12,12,null,12,null,12,null,12,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,12,12,null,12,null,12,null,null,12,null,null,12,12,12,12,null,null,12,null,12,null,12,null,null,12,null,12,null,null,12,null,null,12,null,null,null,12,null,null,null,12,null,12,12,12,null,12,null,null,12,null,null,12,null,null,null,12,12,null,12,12,null,12,12,null,12,null,12,null,12,null,12,null,null,null,12,null,null,12,null,null,12,null,12,12,null,12,null,12,null,null,null,12,12,12,null,12,null,12,null,null,12,null,12,12,null,12,null,null,null,12,12,null,12,12,12,null,null,12,null,null,12,12,12,null,12,null,12,12,null,12,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,12,12,null,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,null,null,12,12,12,12,12,null,12,null,12,null,12,null,12,null,12,null,null,null,12,12,null,12,null,null,12,null,null,12,null,null,null,12,12,12,12,null,12,12,null,null,12,null,null,12,null,12,12,12,12,12,12,null,12,null,null,12,null,12,12,null,12,null,12,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,12,12,null,12,null,12,null,null,12,null,12,12,null,12,12,null,null,null,12,null,12,null,null,12,null,12,null,12,12,null,12,null,null,12,12,null,12,null,12,null,null,12,null,null,12,null,12,12,null,12,12,null,null,null,12,null,12,null,null,null,12,12,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,12,12,12,null,null,12,null,12,null,null,12,null,null,12,null,null,12,12,12,null,12,12,12,null,12,null,12,null,12,null,12,null,null,12,12,null,null,12,12,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,12,null,12,null,12,null,12,12,null,12,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,12,12,null,12,null,12,null,12,12,null,12,null,12,null,null,null,null,null,12,null,12,null,null,12,12,12,null,null,null,12,12,null,12,12,null,null,12,null,12,null,12,null,12,12,12,null,12,null,null,null,12,12,12,null,12,null,12,null,12,12,null,12,12,null,12,null,12,null,12,12,null,12,null,12,12,null,null,12,null,null,12,null,12,12,null,null,12,null,12,null,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,12,null,12,null,12,12,null,null,12,12,12,null,12,null,null,12,null,null,12,null,12,12,null,12,12,null,12,null,12,12,null,12,null,12,12,12,null,null,12,12,null,12,null,12,null,12,null,12,null,12,12,12,null,null,12,null,null,12,12,null,12,null,12,null,12,12,12,null,12,null,12,null,12,null,12,12,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,12,null,null,12,12,12,null,12,null,12,12,null,null,12,12,12,12,12,null,null,12,null,12,null,12,null,12,12,null,12,null,null,12,null,null,12,12,null,null,12,null,12,null,12,null,12,null,12,12,null,null,12,null,12,12,null,12,null,12,null,12,null,12,12,12,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,12,12,null,12,12,12,null,12,12,12,12,null,12,null,null,12,12,null,null,12,12,null,12,null,12,null,null,12,null,null,null,12,null,12,null,12,null,null,12,12,null,12,12,12,12,null,12,null,12,null,12,12,null,null,12,12,null,12,null,null,12,null,12,null,12,null,12,null,null,null,12,null,null,null,12,null,12,null,12,12,null,null,12,12,12,12,null,12,null,null,12,null,12,null,12,null,null,12,null,null,12,null,12,null,12,12,null,12,null,12,null,null,12,null,null,12,12,12,null,12,null,null,12,null,12,null,12,null,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,13,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null],"memalloc":[124.5360641479492,124.5360641479492,124.5360641479492,124.5360641479492,139.8182983398438,139.8182983398438,139.8182983398438,139.8182983398438,170.2840423583984,170.2840423583984,170.2840423583984,170.2840423583984,170.2840423583984,170.2840423583984,170.2840423583984,170.2840423583984,170.2840881347656,170.2840881347656,170.2840881347656,170.2840881347656,170.2840881347656,170.2840881347656,170.2840881347656,170.2840881347656,170.2840881347656,170.2840881347656,170.2840881347656,170.2840881347656,170.2840881347656,170.2840881347656,170.2837829589844,170.2837829589844,185.6540374755859,185.6540374755859,185.9037628173828,185.9037628173828,185.9037628173828,186.1636581420898,186.1636581420898,186.1636581420898,186.4589462280273,186.7892150878906,186.7892150878906,186.7892150878906,187.1415481567383,187.4975891113281,187.4975891113281,187.8990936279297,187.8990936279297,188.3484878540039,188.3484878540039,188.6059722900391,188.6059722900391,185.8974380493164,186.2608871459961,186.2608871459961,186.2608871459961,186.6630401611328,186.6630401611328,187.0851287841797,187.5015411376953,187.9119186401367,187.9119186401367,188.3235702514648,188.3235702514648,188.6703872680664,188.6703872680664,185.9580230712891,185.9580230712891,186.3208084106445,186.7006912231445,186.7006912231445,187.1023559570312,187.5057067871094,187.9007263183594,187.9007263183594,187.9007263183594,188.2948455810547,188.2948455810547,188.2948455810547,188.6852951049805,188.6852951049805,185.9621047973633,185.9621047973633,186.3213195800781,186.3213195800781,186.3213195800781,186.6856384277344,187.0705642700195,187.0705642700195,187.4732284545898,187.8672256469727,187.8672256469727,188.256103515625,188.256103515625,188.6474609375,188.8327102661133,188.8327102661133,188.8327102661133,186.3174819946289,186.3174819946289,186.3174819946289,186.6673583984375,186.6673583984375,187.0349807739258,187.424201965332,187.424201965332,187.8244705200195,187.8244705200195,187.8244705200195,188.2279052734375,188.2279052734375,188.2279052734375,188.6337890625,188.6337890625,188.9118881225586,188.9118881225586,188.9118881225586,186.3718948364258,186.3718948364258,186.7209167480469,186.7209167480469,187.089485168457,187.4787979125977,187.4787979125977,187.8790969848633,187.8790969848633,187.8790969848633,188.285285949707,188.285285949707,188.6877212524414,188.9897766113281,188.9897766113281,186.4819564819336,186.4819564819336,186.4819564819336,186.8266296386719,187.1870651245117,187.5601043701172,187.5601043701172,187.9494476318359,187.9494476318359,188.3429183959961,188.3429183959961,188.7428131103516,188.7428131103516,189.0664138793945,189.0664138793945,186.5661544799805,186.5661544799805,186.9139251708984,186.9139251708984,186.9139251708984,187.2745132446289,187.2745132446289,187.2745132446289,187.6389923095703,187.6389923095703,188.0171203613281,188.0171203613281,188.4083099365234,188.797119140625,188.797119140625,189.1419219970703,189.1419219970703,189.1419219970703,186.631721496582,186.9649505615234,186.9649505615234,187.3206405639648,187.3206405639648,187.6827239990234,188.0620651245117,188.0620651245117,188.0620651245117,188.4574432373047,188.4574432373047,188.8427810668945,188.8427810668945,189.2160873413086,189.2160873413086,186.7094802856445,186.7094802856445,187.0319747924805,187.0319747924805,187.3769607543945,187.3769607543945,187.7335510253906,187.7335510253906,187.7335510253906,188.1029205322266,188.1029205322266,188.4894790649414,188.4894790649414,188.8852462768555,189.2791213989258,186.8103256225586,186.8103256225586,187.1358489990234,187.1358489990234,187.4810104370117,187.4810104370117,187.8391571044922,187.8391571044922,188.2128601074219,188.5962142944336,188.9911651611328,188.9911651611328,189.3609237670898,189.3609237670898,189.3609237670898,186.9471282958984,187.2988891601562,187.2988891601562,187.6421508789062,187.6421508789062,187.9993896484375,187.9993896484375,188.3751602172852,188.7655410766602,188.7655410766602,189.1591339111328,189.1591339111328,189.431640625,189.431640625,189.431640625,187.1284713745117,187.1284713745117,187.4600677490234,187.4600677490234,187.8083877563477,187.8083877563477,188.1685180664062,188.5545120239258,188.5545120239258,188.9470596313477,188.9470596313477,189.3422775268555,189.5011444091797,189.5011444091797,187.3239288330078,187.3239288330078,187.6539535522461,188.0046615600586,188.0046615600586,188.3697662353516,188.3697662353516,188.7509765625,189.1462478637695,189.1462478637695,189.5435409545898,189.5435409545898,187.226318359375,187.226318359375,187.5445251464844,187.5445251464844,187.8787536621094,187.8787536621094,188.231330871582,188.231330871582,188.6045227050781,188.6045227050781,188.9916305541992,188.9916305541992,188.9916305541992,189.3884353637695,189.6368560791016,189.6368560791016,189.6368560791016,187.4567794799805,187.4567794799805,187.4567794799805,187.7726287841797,187.7726287841797,188.1062240600586,188.1062240600586,188.4619522094727,188.8355102539062,188.8355102539062,188.8355102539062,189.2239761352539,189.2239761352539,189.6177978515625,189.6177978515625,189.7030410766602,189.7030410766602,189.7030410766602,187.6809539794922,187.6809539794922,187.9983673095703,188.3651123046875,188.3651123046875,188.71923828125,188.71923828125,189.0830612182617,189.4634399414062,189.4634399414062,189.4634399414062,189.7681732177734,189.7681732177734,187.6095428466797,187.6095428466797,187.9082641601562,187.9082641601562,188.2349395751953,188.2349395751953,188.5856018066406,188.5856018066406,188.9502410888672,188.9502410888672,189.3355941772461,189.7127532958984,189.8322982788086,189.8322982788086,187.8241424560547,187.8241424560547,188.1218948364258,188.1218948364258,188.4506988525391,188.4506988525391,188.8027420043945,188.8027420043945,189.172119140625,189.172119140625,189.172119140625,189.5614624023438,189.895393371582,189.895393371582,187.7955703735352,187.7955703735352,188.088264465332,188.088264465332,188.4048080444336,188.4048080444336,188.7537841796875,189.1173095703125,189.498420715332,189.498420715332,189.8938980102539,189.8938980102539,189.9574356079102,189.9574356079102,189.9574356079102,188.0853729248047,188.3913421630859,188.3913421630859,188.7312622070312,188.7312622070312,189.0901031494141,189.0901031494141,189.4691162109375,189.4691162109375,189.8632354736328,189.8632354736328,190.0185317993164,190.0185317993164,190.0185317993164,190.0185317993164,190.0185317993164,190.0185317993164,190.0185317993164,190.0185317993164,190.0185317993164,190.0185317993164,190.0185317993164,190.0185317993164,190.0185317993164,190.0185317993164,190.0185317993164,190.0185317993164,190.0185317993164,190.0185317993164,190.0185317993164,190.0185317993164,190.0185317993164,190.0185317993164,190.0185317993164,190.0185317993164,188.0588455200195,188.283073425293,188.283073425293,188.5203475952148,188.5203475952148,188.7888870239258,189.0928115844727,189.4238739013672,189.4238739013672,189.7695083618164,189.7695083618164,190.0781555175781,190.0781555175781,188.0309143066406,188.3081665039062,188.3081665039062,188.6106872558594,188.6106872558594,188.9505310058594,188.9505310058594,189.304801940918,189.304801940918,189.6767654418945,190.0676345825195,190.0676345825195,190.1372680664062,190.1372680664062,190.1372680664062,188.346809387207,188.6476821899414,188.6476821899414,188.6476821899414,188.9847717285156,188.9847717285156,189.3420181274414,189.7166976928711,189.7166976928711,190.1067657470703,190.1067657470703,190.1067657470703,190.1954040527344,190.1954040527344,190.1954040527344,188.4251251220703,188.4251251220703,188.7228622436523,188.7228622436523,189.0571670532227,189.0571670532227,189.0571670532227,189.4142227172852,189.4142227172852,189.788932800293,190.2175750732422,190.2175750732422,190.2175750732422,190.2526626586914,190.2526626586914,190.2526626586914,188.5436096191406,188.5436096191406,188.8486328125,188.8486328125,189.1907501220703,189.1907501220703,189.5530014038086,189.9374008178711,190.3089141845703,190.3089141845703,190.3089141845703,190.3089141845703,188.3955383300781,188.3955383300781,188.6760711669922,188.6760711669922,188.9888000488281,188.9888000488281,189.3379669189453,189.3379669189453,189.7047119140625,189.7047119140625,190.0945129394531,190.3643264770508,190.3643264770508,188.5503311157227,188.5503311157227,188.8310852050781,188.8310852050781,189.1516876220703,189.5039749145508,189.5039749145508,189.8688125610352,189.8688125610352,190.2583465576172,190.2583465576172,190.4187469482422,190.4187469482422,190.4187469482422,188.7062606811523,188.7062606811523,188.9952850341797,188.9952850341797,189.3276138305664,189.3276138305664,189.686164855957,190.0600357055664,190.0600357055664,190.4528198242188,190.4724044799805,190.4724044799805,190.4724044799805,188.8899841308594,188.8899841308594,189.1877670288086,189.5255584716797,189.5255584716797,189.8847961425781,189.8847961425781,189.8847961425781,190.2587661743164,190.5250930786133,190.5250930786133,190.5250930786133,188.7902221679688,188.7902221679688,189.0957565307617,189.4169845581055,189.7695846557617,190.1354064941406,190.1354064941406,190.1354064941406,190.5172348022461,190.5172348022461,190.5770568847656,190.5770568847656,189.0065689086914,189.0065689086914,189.2964401245117,189.6282653808594,189.9855346679688,189.9855346679688,190.3604125976562,190.3604125976562,190.6280212402344,190.6280212402344,188.9494323730469,189.2272109985352,189.2272109985352,189.544319152832,189.544319152832,189.8952713012695,189.8952713012695,189.8952713012695,190.2611846923828,190.6430206298828,190.6430206298828,190.6782913208008,190.6782913208008,189.1913986206055,189.1913986206055,189.4922714233398,189.8339767456055,189.8339767456055,190.1941757202148,190.1941757202148,190.5782928466797,190.7276916503906,190.7276916503906,189.1863327026367,189.1863327026367,189.4741668701172,189.8057632446289,189.8057632446289,190.1623382568359,190.1623382568359,190.5396041870117,190.5396041870117,190.7763214111328,190.7763214111328,190.7763214111328,189.1977386474609,189.1977386474609,189.1977386474609,189.474967956543,189.474967956543,189.8254089355469,189.8254089355469,190.1800308227539,190.1800308227539,190.5478286743164,190.8240966796875,190.8240966796875,189.2421035766602,189.2421035766602,189.5158462524414,189.5158462524414,189.8302993774414,189.8302993774414,190.179557800293,190.179557800293,190.5436401367188,190.5436401367188,190.5436401367188,190.871223449707,190.871223449707,189.2726974487305,189.2726974487305,189.5359344482422,189.8380355834961,190.1788101196289,190.1788101196289,190.5368499755859,190.9174346923828,190.9174346923828,190.9174346923828,190.9174346923828,190.9174346923828,190.9174346923828,189.5756530761719,189.5756530761719,189.8723831176758,189.8723831176758,190.2121276855469,190.2121276855469,190.5673980712891,190.9454879760742,190.9630279541016,190.9630279541016,190.9630279541016,189.6398239135742,189.9421691894531,190.2841033935547,190.6475143432617,190.6475143432617,191.0078277587891,191.0078277587891,191.0078277587891,189.4736175537109,189.7416229248047,190.0491485595703,190.0491485595703,190.3877792358398,190.3877792358398,190.7470474243164,191.0519561767578,191.0519561767578,189.5849533081055,189.5849533081055,189.8521728515625,189.8521728515625,190.16064453125,190.16064453125,190.5053482055664,190.5053482055664,190.8646087646484,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,191.0952529907227,189.6019134521484,189.6019134521484,189.6019134521484,189.6019134521484,189.6019134521484,189.6019134521484,189.6019134521484,189.6019134521484,189.7136764526367,189.7136764526367,189.9658966064453,189.9658966064453,190.241569519043,190.5540542602539,190.5540542602539,190.5540542602539,190.8746643066406,190.8746643066406,191.2030029296875,191.2030029296875,191.5592803955078,191.9532699584961,191.9532699584961,192.3554916381836,192.3554916381836,192.3554916381836,192.6892547607422,192.6892547607422,192.6892547607422,193.0205154418945,193.3504867553711,193.6808776855469,193.6808776855469,194.0104293823242,194.0104293823242,194.3429183959961,194.3429183959961,194.4393081665039,194.4393081665039,189.9869613647461,189.9869613647461,190.3294982910156,190.3294982910156,190.3294982910156,190.6897277832031,191.0347671508789,191.0347671508789,191.4071502685547,191.8050918579102,191.8050918579102,192.2128829956055,192.2128829956055,192.6215591430664,192.6215591430664,193.026985168457,193.4333190917969,193.4333190917969,193.8396530151367,194.2417831420898,194.2417831420898,194.5716247558594,194.5716247558594,194.5716247558594,194.5716247558594,194.5716247558594,194.5716247558594,190.3110504150391,190.3110504150391,190.6456985473633,190.6456985473633,190.9855804443359,190.9855804443359,191.3219223022461,191.6983795166016,191.6983795166016,192.0925521850586,192.494010925293,192.494010925293,192.9007339477539,192.9007339477539,193.3038177490234,193.3038177490234,193.3038177490234,193.7074203491211,193.7074203491211,194.109245300293,194.109245300293,194.5072326660156,194.5072326660156,194.7018127441406,194.7018127441406,190.2996063232422,190.2996063232422,190.6106033325195,190.9487457275391,190.9487457275391,191.2726287841797,191.2726287841797,191.6357192993164,191.6357192993164,192.0196762084961,192.4165954589844,192.4165954589844,192.8196640014648,192.8196640014648,193.2255020141602,193.2255020141602,193.6233444213867,193.6233444213867,194.0241470336914,194.4301910400391,194.8223114013672,194.8298721313477,194.8298721313477,194.8298721313477,190.6354522705078,190.6354522705078,190.9562225341797,190.9562225341797,190.9562225341797,191.2806549072266,191.2806549072266,191.6224975585938,191.6224975585938,191.9952621459961,191.9952621459961,192.3849487304688,192.3849487304688,192.7790603637695,192.7790603637695,193.1817779541016,193.1817779541016,193.5801620483398,193.9817581176758,193.9817581176758,194.3846969604492,194.3846969604492,194.781120300293,194.781120300293,194.9558639526367,194.9558639526367,194.9558639526367,194.9558639526367,190.719970703125,190.719970703125,191.0236587524414,191.0236587524414,191.3404235839844,191.3404235839844,191.6692733764648,191.6692733764648,192.0323638916016,192.0323638916016,192.4081802368164,192.4081802368164,192.8003540039062,192.8003540039062,193.1954193115234,193.1954193115234,193.5963134765625,193.999267578125,193.999267578125,194.4012222290039,194.8036575317383,195.0798492431641,195.0798492431641,195.0798492431641,190.8147888183594,191.1120376586914,191.1120376586914,191.4246292114258,191.7452239990234,192.1058959960938,192.1058959960938,192.4728469848633,192.4728469848633,192.8537979125977,192.8537979125977,193.2426452636719,193.2426452636719,193.6401290893555,194.0449600219727,194.451286315918,194.451286315918,194.8594436645508,195.2018203735352,195.2018203735352,195.2018203735352,195.2018203735352,195.2018203735352,195.2018203735352,191.2184677124023,191.2184677124023,191.5138473510742,191.8184051513672,191.8184051513672,192.1690063476562,192.1690063476562,192.5305099487305,192.5305099487305,192.907958984375,192.907958984375,192.907958984375,193.2940444946289,193.2940444946289,193.6874465942383,193.6874465942383,194.0897674560547,194.0897674560547,194.4937133789062,194.8992538452148,194.8992538452148,195.3218002319336,195.3218002319336,195.3218002319336,195.3218002319336,195.3218002319336,195.3218002319336,191.3871612548828,191.6833038330078,191.6833038330078,191.9933624267578,191.9933624267578,192.3457870483398,192.7100448608398,192.7100448608398,193.0886993408203,193.0886993408203,193.4770812988281,193.8720321655273,193.8720321655273,193.8720321655273,194.2761993408203,194.6796112060547,194.6796112060547,195.0852508544922,195.0852508544922,195.4398880004883,195.4398880004883,195.4398880004883,195.4398880004883,195.4398880004883,195.4398880004883,191.5874404907227,191.5874404907227,191.8750457763672,191.8750457763672,192.1866912841797,192.5366592407227,192.5366592407227,192.8940353393555,192.8940353393555,193.2672729492188,193.2672729492188,193.6495361328125,194.0415420532227,194.443000793457,194.443000793457,194.443000793457,194.8451538085938,194.8451538085938,195.247200012207,195.247200012207,195.247200012207,195.556022644043,195.556022644043,195.556022644043,195.556022644043,195.556022644043,195.556022644043,191.7937545776367,191.7937545776367,192.072395324707,192.3917846679688,192.3917846679688,192.7413101196289,192.7413101196289,193.0980834960938,193.0980834960938,193.0980834960938,193.46923828125,193.46923828125,193.8522491455078,194.2435607910156,194.6419219970703,194.6419219970703,194.6419219970703,195.0429992675781,195.4806671142578,195.4806671142578,195.6703567504883,195.6703567504883,191.7655639648438,191.7655639648438,191.7655639648438,192.0400238037109,192.0400238037109,192.3254776000977,192.3254776000977,192.6571273803711,193.0114288330078,193.0114288330078,193.3676986694336,193.7488327026367,194.1368713378906,194.5336685180664,194.5336685180664,194.9355239868164,194.9355239868164,195.3405075073242,195.7344665527344,195.7344665527344,195.7827529907227,195.7827529907227,195.7827529907227,192.0570526123047,192.0570526123047,192.3295669555664,192.3295669555664,192.6388244628906,192.6388244628906,192.9797058105469,192.9797058105469,193.3308563232422,193.3308563232422,193.3308563232422,193.6937866210938,193.6937866210938,194.0713424682617,194.4603729248047,194.858772277832,195.261100769043,195.261100769043,195.6615829467773,195.8934860229492,195.8934860229492,192.1001052856445,192.3695068359375,192.3695068359375,192.6521987915039,192.6521987915039,192.9809341430664,193.3297348022461,193.3297348022461,193.6840362548828,193.6840362548828,194.0618133544922,194.0618133544922,194.449462890625,194.449462890625,194.8454971313477,194.8454971313477,195.2467346191406,195.6928482055664,196.0022430419922,196.0022430419922,196.0022430419922,196.0022430419922,196.0022430419922,196.0022430419922,196.0022430419922,196.0022430419922,192.4743728637695,192.4743728637695,192.7493667602539,193.0665512084961,193.0665512084961,193.4069900512695,193.4069900512695,193.7607727050781,193.7607727050781,194.1296234130859,194.1296234130859,194.5134811401367,194.9074935913086,194.9074935913086,195.3089599609375,195.7138290405273,195.7138290405273,196.1046981811523,196.1093521118164,196.1093521118164,196.1093521118164,192.5816650390625,192.5816650390625,192.8516082763672,192.8516082763672,193.1623153686523,193.4966659545898,193.8461608886719,193.8461608886719,194.2111358642578,194.5936889648438,194.5936889648438,194.9856872558594,195.3877029418945,195.7883148193359,195.7883148193359,196.174186706543,196.2147369384766,196.2147369384766,196.2147369384766,192.6997604370117,192.9499816894531,192.9499816894531,193.23583984375,193.554084777832,193.554084777832,193.8952865600586,194.2461624145508,194.2461624145508,194.6164855957031,195.000602722168,195.000602722168,195.3960800170898,195.3960800170898,195.8356475830078,195.8356475830078,196.2322463989258,196.2322463989258,196.3183746337891,196.3183746337891,196.3183746337891,192.8512496948242,193.1092987060547,193.1092987060547,193.4004135131836,193.7163391113281,194.0588226318359,194.0588226318359,194.0588226318359,194.4104537963867,194.4104537963867,194.7802505493164,195.1630706787109,195.1630706787109,195.5589599609375,195.5589599609375,195.9615097045898,195.9615097045898,196.3565521240234,196.3565521240234,196.4203567504883,196.4203567504883,196.4203567504883,193.0097274780273,193.0097274780273,193.2679901123047,193.2679901123047,193.5574188232422,193.5574188232422,193.869873046875,193.869873046875,194.2143936157227,194.2143936157227,194.5733795166016,194.5733795166016,194.5733795166016,194.9430999755859,194.9430999755859,195.329833984375,195.329833984375,195.7262496948242,195.7262496948242,196.1284637451172,196.1284637451172,196.5206680297852,196.5206680297852,196.5206680297852,196.5206680297852,196.5206680297852,196.5206680297852,193.2091827392578,193.4642868041992,193.4642868041992,193.7511596679688,193.7511596679688,194.0660018920898,194.0660018920898,194.4094161987305,194.7608413696289,194.7608413696289,195.1351852416992,195.5601196289062,195.9582901000977,195.9582901000977,196.3638153076172,196.3638153076172,196.6194686889648,196.6194686889648,196.6194686889648,196.6194686889648,196.6194686889648,196.6194686889648,193.438346862793,193.438346862793,193.7087860107422,193.7087860107422,194.0047836303711,194.3327484130859,194.6841049194336,194.6841049194336,195.0490417480469,195.4296646118164,195.4296646118164,195.8206787109375,196.2212371826172,196.2212371826172,196.6137619018555,196.7165374755859,196.7165374755859,196.7165374755859,196.7165374755859,196.7165374755859,196.7165374755859,196.7165374755859,196.7165374755859,196.7165374755859,196.7165374755859,196.7165374755859,196.7165374755859,196.7165374755859,196.7165374755859,196.7165374755859,196.7165374755859,196.7165374755859,196.7165374755859,196.7165374755859,196.7165374755859,196.7165374755859,196.7165374755859,196.7165374755859,196.7165374755859,193.4786834716797,193.4786834716797,193.6955947875977,193.6955947875977,193.9222030639648,194.162223815918,194.162223815918,194.4322891235352,194.73779296875,195.0667953491211,195.0667953491211,195.4120254516602,195.7719802856445,196.1528930664062,196.549690246582,196.549690246582,196.8118591308594,196.8118591308594,196.8118591308594,196.8118591308594,196.8118591308594,196.8118591308594,193.7229919433594,193.7229919433594,193.9827575683594,194.2680740356445,194.5878982543945,194.5878982543945,194.9295654296875,194.9295654296875,195.2850646972656,195.2850646972656,195.6543273925781,195.6543273925781,196.0373992919922,196.0373992919922,196.4299392700195,196.8219223022461,196.8219223022461,196.8219223022461,196.9059371948242,196.9059371948242,193.7474899291992,193.7474899291992,193.9957733154297,193.9957733154297,194.2682876586914,194.2682876586914,194.573486328125,194.573486328125,194.9084625244141,194.9084625244141,195.2629241943359,195.2629241943359,195.2629241943359,195.6338653564453,195.6338653564453,195.6338653564453,196.0195693969727,196.0195693969727,196.4139556884766,196.8106002807617,196.8106002807617,196.998420715332,196.998420715332,193.8541030883789,194.0998764038086,194.0998764038086,194.373161315918,194.373161315918,194.6753234863281,194.6753234863281,195.0071334838867,195.0071334838867,195.3594589233398,195.3594589233398,195.7265396118164,195.7265396118164,196.1103515625,196.1103515625,196.5021743774414,196.5021743774414,196.9000091552734,196.9000091552734,197.0895233154297,197.0895233154297,197.0895233154297,193.9663543701172,193.9663543701172,194.2062301635742,194.2062301635742,194.4700241088867,194.4700241088867,194.7608947753906,194.7608947753906,195.0848922729492,195.0848922729492,195.4324951171875,195.4324951171875,195.7901382446289,196.1648788452148,196.1648788452148,196.5498733520508,196.9442901611328,197.1791305541992,197.1791305541992,197.1791305541992,197.1791305541992,194.3197479248047,194.3197479248047,194.5836868286133,194.5836868286133,194.8769073486328,194.8769073486328,195.2050628662109,195.2050628662109,195.5565643310547,195.5565643310547,195.9222640991211,196.3019256591797,196.3019256591797,196.6934280395508,196.6934280395508,197.09228515625,197.09228515625,197.267219543457,197.267219543457,197.267219543457,194.2749786376953,194.2749786376953,194.2749786376953,194.513801574707,194.513801574707,194.7789688110352,194.7789688110352,195.0746612548828,195.0746612548828,195.4069900512695,195.4069900512695,195.7604293823242,195.7604293823242,196.1274032592773,196.5105438232422,196.5105438232422,196.5105438232422,196.9035415649414,197.2959747314453,197.2959747314453,197.3539047241211,197.3539047241211,197.3539047241211,194.4534530639648,194.4534530639648,194.6957397460938,194.6957397460938,194.9640884399414,194.9640884399414,195.2669677734375,195.6024322509766,195.6024322509766,195.9575881958008,195.9575881958008,196.3285980224609,196.7153472900391,197.1092910766602,197.4392929077148,197.4392929077148,197.4392929077148,197.4392929077148,194.6550598144531,194.9075164794922,194.9075164794922,195.1865768432617,195.5031356811523,195.8473663330078,195.8473663330078,196.2055511474609,196.2055511474609,196.5801391601562,196.5801391601562,196.9712982177734,196.9712982177734,197.3643569946289,197.3643569946289,197.5231628417969,197.5231628417969,197.5231628417969,194.6564865112305,194.6564865112305,194.9254837036133,194.9254837036133,195.1966094970703,195.1966094970703,195.5065002441406,195.5065002441406,195.8478240966797,196.2057266235352,196.2057266235352,196.5792083740234,196.9622039794922,196.9622039794922,197.3549423217773,197.3549423217773,197.6057357788086,197.6057357788086,197.6057357788086,197.6057357788086,197.6057357788086,197.6057357788086,194.940803527832,194.940803527832,195.1881561279297,195.4647064208984,195.4647064208984,195.7786483764648,195.7786483764648,196.1223907470703,196.4717864990234,196.4717864990234,196.8271026611328,196.8271026611328,197.2024688720703,197.2024688720703,197.5869293212891,197.5869293212891,197.6869735717773,197.6869735717773,197.6869735717773,194.9301528930664,194.9301528930664,195.1656188964844,195.1656188964844,195.4283065795898,195.4283065795898,195.7254104614258,195.7254104614258,196.0565872192383,196.4108657836914,196.4108657836914,196.7705383300781,196.7705383300781,197.1388473510742,197.5240173339844,197.7668914794922,197.7668914794922,197.7668914794922,197.7668914794922,197.7668914794922,197.7668914794922,195.2103576660156,195.2103576660156,195.4579391479492,195.4579391479492,195.736946105957,196.05322265625,196.4016723632812,196.4016723632812,196.7603607177734,196.7603607177734,197.1384735107422,197.1384735107422,197.5352935791016,197.8454895019531,197.8454895019531,197.8454895019531,197.8454895019531,197.8454895019531,197.8454895019531,195.290283203125,195.290283203125,195.5383529663086,195.5383529663086,195.8159866333008,195.8159866333008,196.1346054077148,196.1346054077148,196.4765090942383,196.835807800293,197.2126235961914,197.2126235961914,197.6049346923828,197.6049346923828,197.9228820800781,197.9228820800781,197.9228820800781,197.9228820800781,197.9228820800781,197.9228820800781,195.4105834960938,195.660285949707,195.9399948120117,196.2576370239258,196.2576370239258,196.2576370239258,196.6026611328125,196.6026611328125,196.9629135131836,196.9629135131836,197.3352279663086,197.3352279663086,197.3352279663086,197.7258148193359,197.7258148193359,197.9989166259766,197.9989166259766,197.9989166259766,197.9989166259766,197.9989166259766,197.9989166259766,195.5789642333984,195.5789642333984,195.8339233398438,195.8339233398438,196.1210021972656,196.1210021972656,196.4464950561523,196.4464950561523,196.7955322265625,196.7955322265625,197.1484680175781,197.5234603881836,197.9117202758789,197.9117202758789,198.0738754272461,198.0738754272461,198.0738754272461,198.0738754272461,198.0738754272461,198.0738754272461,195.7214813232422,195.7214813232422,195.974494934082,195.974494934082,196.2626800537109,196.5890197753906,196.5890197753906,196.9381942749023,197.2993698120117,197.2993698120117,197.6796493530273,198.0696792602539,198.0696792602539,198.1474761962891,198.1474761962891,195.6618804931641,195.6618804931641,195.8978576660156,195.8978576660156,196.1640777587891,196.1640777587891,196.4660491943359,196.4660491943359,196.8031616210938,196.8031616210938,196.8031616210938,197.1577987670898,197.1577987670898,197.1577987670898,197.5278396606445,197.5278396606445,197.9151916503906,198.2199859619141,198.2199859619141,198.2199859619141,198.2199859619141,195.8687438964844,195.8687438964844,196.142692565918,196.142692565918,196.4253387451172,196.7468795776367,197.0937881469727,197.0937881469727,197.4543304443359,197.4543304443359,197.8351669311523,197.8351669311523,198.2264938354492,198.2913513183594,198.2913513183594,195.892822265625,196.1283264160156,196.1283264160156,196.3938293457031,196.3938293457031,196.6982803344727,196.6982803344727,197.0405578613281,197.4001617431641,197.4001617431641,197.7747573852539,198.1674728393555,198.3614349365234,198.3614349365234,198.3614349365234,198.3614349365234,198.3614349365234,198.3614349365234,196.1570281982422,196.4120635986328,196.7038116455078,196.7038116455078,197.0340957641602,197.0340957641602,197.3853149414062,197.738639831543,197.738639831543,198.1163482666016,198.4305114746094,198.4305114746094,198.4305114746094,198.4305114746094,198.4305114746094,198.4305114746094,198.4305114746094,198.4305114746094,198.4305114746094,198.4305114746094,198.4305114746094,198.4305114746094,198.4305114746094,198.4305114746094,198.4305114746094,198.4305114746094,198.4305114746094,198.4305114746094,198.4305114746094,198.4305114746094,198.4305114746094,198.4305114746094,198.4305114746094,198.4305114746094,198.4305114746094,198.4305114746094,198.4305114746094,198.4305114746094,198.4305114746094,198.4305114746094,196.0542526245117,196.0542526245117,196.0542526245117,196.1279373168945,196.1279373168945,196.3353652954102,196.3353652954102,196.5645217895508,196.5645217895508,196.8167495727539,197.1062393188477,197.1062393188477,197.1062393188477,197.4296264648438,197.4296264648438,197.7633895874023,197.7633895874023,198.1217269897461,198.1217269897461,198.1217269897461,198.4980926513672,198.4980926513672,198.4980926513672,198.4980926513672,198.4980926513672,198.4980926513672,196.2628784179688,196.2628784179688,196.5057525634766,196.5057525634766,196.7793731689453,197.0947036743164,197.0947036743164,197.438591003418,197.438591003418,197.7972640991211,197.7972640991211,198.1747589111328,198.1747589111328,198.5649490356445,198.5649490356445,198.5649490356445,198.5649490356445,196.357551574707,196.357551574707,196.6244659423828,196.6244659423828,196.9010009765625,196.9010009765625,196.9010009765625,197.2165374755859,197.5626831054688,197.9217758178711,198.2992324829102,198.6306991577148,198.6306991577148,198.6306991577148,198.6306991577148,196.4933090209961,196.4933090209961,196.7343902587891,196.7343902587891,197.0092010498047,197.0092010498047,197.3229675292969,197.3229675292969,197.6667175292969,197.6667175292969,198.0244903564453,198.4009475708008,198.4009475708008,198.6955108642578,198.6955108642578,198.6955108642578,198.6955108642578,198.6955108642578,198.6955108642578,196.6204452514648,196.6204452514648,196.8611602783203,196.8611602783203,197.1377792358398,197.4532165527344,197.7970428466797,198.1574249267578,198.1574249267578,198.5357971191406,198.7591247558594,198.7591247558594,198.7591247558594,198.7591247558594,198.7591247558594,198.7591247558594,196.7602310180664,196.7602310180664,197.0126724243164,197.3022613525391,197.6328125,198.0237121582031,198.3969573974609,198.789421081543,198.789421081543,198.8217620849609,198.8217620849609,198.8217620849609,196.7297744750977,196.7297744750977,196.962158203125,197.2260055541992,197.2260055541992,197.5278396606445,197.5278396606445,197.8646392822266,198.2227478027344,198.2227478027344,198.5961303710938,198.5961303710938,198.8833999633789,198.8833999633789,198.8833999633789,198.8833999633789,198.8833999633789,198.8833999633789,196.9094619750977,196.9094619750977,197.1569061279297,197.4411468505859,197.4411468505859,197.7672119140625,198.1202392578125,198.1202392578125,198.488410949707,198.488410949707,198.8719635009766,198.8719635009766,198.8719635009766,198.9440612792969,198.9440612792969,196.8989868164062,197.1333465576172,197.1333465576172,197.3986511230469,197.7018966674805,197.7018966674805,198.0424880981445,198.0424880981445,198.4032745361328,198.4032745361328,198.7817764282227,198.7817764282227,198.7817764282227,199.0036315917969,199.0036315917969,199.0036315917969,199.0036315917969,197.1552963256836,197.4087371826172,197.4087371826172,197.7008743286133,197.7008743286133,197.7008743286133,198.0314483642578,198.3867874145508,198.3867874145508,198.7553482055664,198.7553482055664,199.0623931884766,199.0623931884766,199.0623931884766,199.0623931884766,199.0623931884766,199.0623931884766,197.1646270751953,197.1646270751953,197.4056701660156,197.681884765625,197.681884765625,198.0000076293945,198.3474655151367,198.3474655151367,198.7091217041016,198.7091217041016,199.0909576416016,199.0909576416016,199.1200942993164,199.1200942993164,199.1200942993164,197.1957473754883,197.4308319091797,197.6990661621094,197.9994964599609,197.9994964599609,198.3355178833008,198.3355178833008,198.6906814575195,198.6906814575195,199.0609359741211,199.0609359741211,199.1769409179688,199.1769409179688,199.1769409179688,199.1769409179688,199.1769409179688,199.1769409179688,197.4623031616211,197.4623031616211,197.7173385620117,198.0113677978516,198.3442764282227,198.3442764282227,198.3442764282227,198.6989212036133,198.6989212036133,199.0686416625977,199.0686416625977,199.0686416625977,199.2327423095703,199.2327423095703,199.2327423095703,199.2327423095703,199.2327423095703,199.2327423095703,197.5091018676758,197.7574996948242,198.0442276000977,198.0442276000977,198.3724899291992,198.7245483398438,199.0904541015625,199.0904541015625,199.2878265380859,199.2878265380859,199.2878265380859,199.2878265380859,197.572868347168,197.572868347168,197.8171463012695,197.8171463012695,197.8171463012695,198.1000518798828,198.4237670898438,198.4237670898438,198.4237670898438,198.7752838134766,199.1412582397461,199.3418502807617,199.3418502807617,199.3418502807617,199.3418502807617,199.3418502807617,199.3418502807617,199.3418502807617,199.3418502807617,199.3418502807617,199.3418502807617,199.3418502807617,199.3418502807617,199.3418502807617,199.3418502807617,199.3418502807617,199.3418502807617,199.3418502807617,199.3418502807617,197.6310119628906,197.8562545776367,197.8562545776367,198.1014099121094,198.1014099121094,198.3813400268555,198.3813400268555,198.6969146728516,199.0389785766602,199.0389785766602,199.3819122314453,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,199.3948440551758,197.5631332397461,197.5631332397461,197.5631332397461,197.5631332397461,197.5631332397461,197.5631332397461,197.7317047119141,197.9848556518555,198.265739440918,198.265739440918,198.5868606567383,198.5868606567383,198.9225311279297,198.9225311279297,199.2372283935547,199.5795669555664,199.5795669555664,199.9718933105469,199.9718933105469,200.4153366088867,200.4153366088867,200.8185882568359,200.8185882568359,201.2207565307617,201.2207565307617,201.5832748413086,201.5832748413086,201.912841796875,201.912841796875,201.912841796875,202.2438354492188,202.575309753418,202.9077911376953,202.9077911376953,203.2390670776367,203.2390670776367,203.5707168579102,203.9020309448242,203.9020309448242,204.234016418457,204.564826965332,204.564826965332,204.564826965332,204.8980331420898,204.8980331420898,205.1759414672852,205.1759414672852,205.1759414672852,205.1759414672852,197.9130783081055,198.1575393676758,198.4559326171875,198.4559326171875,198.7913055419922,198.7913055419922,199.1401824951172,199.1401824951172,199.4640426635742,199.8305053710938,200.2189636230469,200.2189636230469,200.6174468994141,200.6174468994141,201.0226821899414,201.0226821899414,201.4341812133789,201.842155456543,201.842155456543,202.2515563964844,202.6607360839844,202.6607360839844,203.0696105957031,203.0696105957031,203.4793395996094,203.4793395996094,203.8899002075195,204.2994766235352,204.2994766235352,204.7092666625977,204.7092666625977,205.1019821166992,205.3841400146484,205.3841400146484,205.3841400146484,205.3841400146484,205.3841400146484,205.3841400146484,198.2744979858398,198.2744979858398,198.5113220214844,198.8049697875977,198.8049697875977,198.8049697875977,199.1303405761719,199.1303405761719,199.4610748291016,199.4610748291016,199.4610748291016,199.7932510375977,199.7932510375977,200.1613998413086,200.1613998413086,200.5453186035156,200.5453186035156,200.9412384033203,200.9412384033203,201.3468933105469,201.7562789916992,201.7562789916992,202.1623764038086,202.1623764038086,202.5690841674805,202.9765396118164,202.9765396118164,203.3847579956055,203.3847579956055,203.7931060791016,204.2017364501953,204.2017364501953,204.2017364501953,204.6100463867188,205.018684387207,205.4093551635742,205.4093551635742,205.5890502929688,205.5890502929688,205.5890502929688,205.5890502929688,205.5890502929688,205.5890502929688,198.6243667602539,198.6243667602539,198.8844299316406,199.1742858886719,199.1742858886719,199.4896469116211,199.8026428222656,199.8026428222656,200.1506576538086,200.1506576538086,200.5180435180664,200.8985137939453,200.8985137939453,201.2917709350586,201.2917709350586,201.6908798217773,202.0986480712891,202.5027008056641,202.5027008056641,202.5027008056641,202.9075775146484,203.3112716674805,203.3112716674805,203.7157821655273,203.7157821655273,204.1205825805664,204.1205825805664,204.5677185058594,204.5677185058594,204.9755020141602,204.9755020141602,205.3760986328125,205.7671890258789,205.7905883789062,205.7905883789062,205.7905883789062,205.7905883789062,205.7905883789062,205.7905883789062,199.0185852050781,199.2802352905273,199.2802352905273,199.5681915283203,199.5681915283203,199.8691787719727,199.8691787719727,200.1855010986328,200.5385589599609,200.8953170776367,200.8953170776367,201.2565002441406,201.2565002441406,201.6423034667969,201.6423034667969,202.0392456054688,202.0392456054688,202.4400863647461,202.8429794311523,203.2473983764648,203.2473983764648,203.6529235839844,203.6529235839844,204.0586471557617,204.0586471557617,204.465576171875,204.465576171875,204.465576171875,204.8730545043945,204.8730545043945,205.2809906005859,205.2809906005859,205.6698303222656,205.6698303222656,205.9888610839844,205.9888610839844,205.9888610839844,205.9888610839844,205.9888610839844,205.9888610839844,205.9888610839844,205.9888610839844,205.9888610839844,199.34619140625,199.34619140625,199.6041564941406,199.6041564941406,199.8882217407227,200.1808166503906,200.5109405517578,200.8984832763672,200.8984832763672,201.263671875,201.263671875,201.6404190063477,202.0288848876953,202.0288848876953,202.0288848876953,202.4239196777344,202.8235549926758,203.2246246337891,203.6241989135742,204.0245666503906,204.0245666503906,204.0245666503906,204.4274749755859,204.4274749755859,204.8280639648438,204.8280639648438,205.23095703125,205.23095703125,205.6316757202148,206.0177764892578,206.0177764892578,206.183967590332,206.183967590332,206.183967590332,206.183967590332,206.183967590332,206.183967590332,199.5407333374023,199.7924957275391,199.7924957275391,199.7924957275391,200.0592193603516,200.0592193603516,200.3408737182617,200.3408737182617,200.6534194946289,200.6534194946289,201.0008239746094,201.0008239746094,201.3569107055664,201.7267761230469,201.7267761230469,201.7267761230469,202.1091232299805,202.1091232299805,202.4961013793945,202.8868179321289,202.8868179321289,203.2811126708984,203.2811126708984,203.6786041259766,203.6786041259766,204.0795440673828,204.0795440673828,204.4779357910156,204.879524230957,205.2825927734375,205.2825927734375,205.6865539550781,205.6865539550781,206.0796051025391,206.0796051025391,206.3758697509766,206.3758697509766,206.3758697509766,206.3758697509766,206.3758697509766,206.3758697509766,206.3758697509766,206.3758697509766,206.3758697509766,206.3758697509766,206.3758697509766,206.3758697509766,206.3758697509766,206.3758697509766,206.3758697509766,206.3758697509766,206.3758697509766,206.3758697509766,206.3758697509766,206.3758697509766,206.3758697509766,206.3758697509766,206.3758697509766,206.3758697509766,199.9194564819336,199.9194564819336,200.1529998779297,200.3947219848633,200.640998840332,200.640998840332,200.9365005493164,201.2628860473633,201.6053009033203,201.6053009033203,201.9566116333008,202.3249359130859,202.7071990966797,203.095100402832,203.095100402832,203.4854965209961,203.4854965209961,203.4854965209961,203.8764266967773,204.2758331298828,204.2758331298828,204.2758331298828,204.6764907836914,205.0782775878906,205.0782775878906,205.4838104248047,205.4838104248047,205.8896865844727,205.8896865844727,205.8896865844727,206.2818908691406,206.2818908691406,206.5646896362305,206.5646896362305,206.5646896362305,206.5646896362305,206.5646896362305,206.5646896362305,200.3008422851562,200.3008422851562,200.5536651611328,200.8443222045898,201.154914855957,201.154914855957,201.4936904907227,201.8433685302734,202.20654296875,202.5827102661133,202.5827102661133,202.9678649902344,202.9678649902344,203.3597030639648,203.3597030639648,203.7551193237305,204.1560363769531,204.1560363769531,204.1560363769531,204.5571517944336,204.9609603881836,204.9609603881836,205.365592956543,205.365592956543,205.365592956543,205.7712707519531,205.7712707519531,206.1780395507812,206.1780395507812,206.5688552856445,206.5688552856445,206.7504653930664,206.7504653930664,206.7504653930664,206.7504653930664,206.7504653930664,206.7504653930664,206.7504653930664,206.7504653930664,200.4026565551758,200.4026565551758,200.6474456787109,200.6474456787109,200.8958358764648,201.1630249023438,201.1630249023438,201.4801483154297,201.8193435668945,202.1722259521484,202.5385055541992,202.916877746582,202.916877746582,203.3001403808594,203.3001403808594,203.3001403808594,203.6905670166016,203.6905670166016,204.0857238769531,204.0857238769531,204.4837417602539,204.4837417602539,204.4837417602539,204.8850555419922,204.8850555419922,204.8850555419922,205.2870330810547,205.2870330810547,205.6913452148438,205.6913452148438,206.0948181152344,206.4980163574219,206.4980163574219,206.8879013061523,206.8879013061523,206.9333648681641,206.9333648681641,206.9333648681641,206.9333648681641,206.9333648681641,206.9333648681641,200.7968597412109,201.041877746582,201.2909393310547,201.2909393310547,201.5869750976562,201.5869750976562,201.5869750976562,201.9191513061523,201.9191513061523,202.2665710449219,202.2665710449219,202.6242294311523,202.6242294311523,202.9925308227539,202.9925308227539,203.3703384399414,203.3703384399414,203.7570648193359,203.7570648193359,204.151008605957,204.151008605957,212.0326461791992,212.0326461791992,212.0326461791992,212.0326461791992,212.0326461791992,212.0326461791992,212.0326461791992,212.0326461791992,212.0326461791992,212.0326461791992,212.0326461791992,212.0326461791992,212.0326461791992,212.0326461791992,212.0326461791992,212.0326461791992,212.0326461791992,212.0326461791992,219.6620407104492,219.6620483398438,219.6620483398438,219.6620483398438,219.6620483398438,219.6620483398438,219.6620483398438,219.6620483398438,219.6620483398438,219.6620483398438,219.6620483398438,219.6620483398438,219.6620483398438,219.6620483398438,219.6620483398438,219.6620483398438,219.6620483398438,219.6620483398438,219.6620483398438,219.6620483398438,219.6620483398438,219.6620483398438,219.6620483398438,234.9208374023438,234.9208374023438,234.9208374023438,234.9208374023438,234.9208374023438,234.9208374023438,234.9208374023438,234.9208374023438,234.9208374023438,234.9208374023438,234.9208374023438,234.9208374023438,234.9208374023438,234.9208374023438,234.9208374023438,234.9208374023438,242.6113357543945,242.6113357543945,242.6113357543945,242.6113357543945,242.6113357543945,242.6113357543945,242.6113357543945,242.6113357543945,242.6113357543945,242.6113357543945,242.6113357543945,242.6113357543945,242.6113357543945,242.6113357543945,242.6113357543945,242.6113357543945,242.6113357543945,242.6113357543945,242.6113357543945,242.6113357543945,242.6113357543945,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016,257.9454498291016],"meminc":[0,0,0,0,15.28223419189453,0,0,0,30.46574401855469,0,0,0,0,0,0,0,4.57763671875e-05,0,0,0,0,0,0,0,0,0,0,0,0,0,-0.00030517578125,0,15.37025451660156,0,0.249725341796875,0,0,0.2598953247070312,0,0,0.2952880859375,0.3302688598632812,0,0,0.3523330688476562,0.3560409545898438,0,0.4015045166015625,0,0.4493942260742188,0,0.2574844360351562,0,-2.708534240722656,0.3634490966796875,0,0,0.4021530151367188,0,0.422088623046875,0.416412353515625,0.4103775024414062,0,0.411651611328125,0,0.3468170166015625,0,-2.712364196777344,0,0.3627853393554688,0.3798828125,0,0.4016647338867188,0.403350830078125,0.39501953125,0,0,0.3941192626953125,0,0,0.3904495239257812,0,-2.723190307617188,0,0.3592147827148438,0,0,0.36431884765625,0.3849258422851562,0,0.4026641845703125,0.3939971923828125,0,0.3888778686523438,0,0.391357421875,0.1852493286132812,0,0,-2.515228271484375,0,0,0.3498764038085938,0,0.3676223754882812,0.38922119140625,0,0.4002685546875,0,0,0.4034347534179688,0,0,0.4058837890625,0,0.2780990600585938,0,0,-2.539993286132812,0,0.3490219116210938,0,0.3685684204101562,0.389312744140625,0,0.400299072265625,0,0,0.40618896484375,0,0.402435302734375,0.3020553588867188,0,-2.507820129394531,0,0,0.3446731567382812,0.3604354858398438,0.3730392456054688,0,0.38934326171875,0,0.3934707641601562,0,0.3998947143554688,0,0.3236007690429688,0,-2.500259399414062,0,0.3477706909179688,0,0,0.3605880737304688,0,0,0.3644790649414062,0,0.3781280517578125,0,0.3911895751953125,0.3888092041015625,0,0.3448028564453125,0,0,-2.510200500488281,0.3332290649414062,0,0.3556900024414062,0,0.3620834350585938,0.3793411254882812,0,0,0.3953781127929688,0,0.3853378295898438,0,0.3733062744140625,0,-2.506607055664062,0,0.3224945068359375,0,0.3449859619140625,0,0.3565902709960938,0,0,0.3693695068359375,0,0.3865585327148438,0,0.3957672119140625,0.3938751220703125,-2.468795776367188,0,0.3255233764648438,0,0.3451614379882812,0,0.3581466674804688,0,0.3737030029296875,0.3833541870117188,0.3949508666992188,0,0.3697586059570312,0,0,-2.413795471191406,0.3517608642578125,0,0.34326171875,0,0.35723876953125,0,0.3757705688476562,0.390380859375,0,0.3935928344726562,0,0.2725067138671875,0,0,-2.303169250488281,0,0.3315963745117188,0,0.3483200073242188,0,0.3601303100585938,0.3859939575195312,0,0.392547607421875,0,0.3952178955078125,0.1588668823242188,0,-2.177215576171875,0,0.3300247192382812,0.3507080078125,0,0.3651046752929688,0,0.3812103271484375,0.3952713012695312,0,0.3972930908203125,0,-2.317222595214844,0,0.318206787109375,0,0.334228515625,0,0.3525772094726562,0,0.3731918334960938,0,0.3871078491210938,0,0,0.3968048095703125,0.2484207153320312,0,0,-2.180076599121094,0,0,0.3158493041992188,0,0.3335952758789062,0,0.3557281494140625,0.3735580444335938,0,0,0.3884658813476562,0,0.3938217163085938,0,0.08524322509765625,0,0,-2.022087097167969,0,0.317413330078125,0.3667449951171875,0,0.3541259765625,0,0.3638229370117188,0.3803787231445312,0,0,0.3047332763671875,0,-2.15863037109375,0,0.2987213134765625,0,0.3266754150390625,0,0.3506622314453125,0,0.3646392822265625,0,0.3853530883789062,0.3771591186523438,0.1195449829101562,0,-2.008155822753906,0,0.2977523803710938,0,0.3288040161132812,0,0.3520431518554688,0,0.3693771362304688,0,0,0.38934326171875,0.3339309692382812,0,-2.099822998046875,0,0.292694091796875,0,0.3165435791015625,0,0.3489761352539062,0.363525390625,0.3811111450195312,0,0.395477294921875,0,0.06353759765625,0,0,-1.872062683105469,0.30596923828125,0,0.3399200439453125,0,0.3588409423828125,0,0.3790130615234375,0,0.3941192626953125,0,0.1552963256835938,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.959686279296875,0.2242279052734375,0,0.237274169921875,0,0.2685394287109375,0.303924560546875,0.3310623168945312,0,0.3456344604492188,0,0.3086471557617188,0,-2.0472412109375,0.277252197265625,0,0.302520751953125,0,0.33984375,0,0.3542709350585938,0,0.3719635009765625,0.390869140625,0,0.06963348388671875,0,0,-1.790458679199219,0.300872802734375,0,0,0.3370895385742188,0,0.3572463989257812,0.3746795654296875,0,0.3900680541992188,0,0,0.0886383056640625,0,0,-1.770278930664062,0,0.2977371215820312,0,0.3343048095703125,0,0,0.3570556640625,0,0.3747100830078125,0.4286422729492188,0,0,0.03508758544921875,0,0,-1.709053039550781,0,0.305023193359375,0,0.3421173095703125,0,0.3622512817382812,0.3843994140625,0.3715133666992188,0,0,0,-1.913375854492188,0,0.2805328369140625,0,0.3127288818359375,0,0.3491668701171875,0,0.3667449951171875,0,0.389801025390625,0.2698135375976562,0,-1.813995361328125,0,0.2807540893554688,0,0.3206024169921875,0.3522872924804688,0,0.364837646484375,0,0.3895339965820312,0,0.160400390625,0,0,-1.712486267089844,0,0.2890243530273438,0,0.3323287963867188,0,0.358551025390625,0.373870849609375,0,0.3927841186523438,0.01958465576171875,0,0,-1.582420349121094,0,0.2977828979492188,0.3377914428710938,0,0.3592376708984375,0,0,0.3739700317382812,0.266326904296875,0,0,-1.734870910644531,0,0.3055343627929688,0.32122802734375,0.35260009765625,0.3658218383789062,0,0,0.3818283081054688,0,0.05982208251953125,0,-1.570487976074219,0,0.2898712158203125,0.3318252563476562,0.357269287109375,0,0.3748779296875,0,0.267608642578125,0,-1.6785888671875,0.2777786254882812,0,0.317108154296875,0,0.3509521484375,0,0,0.3659133911132812,0.3818359375,0,0.03527069091796875,0,-1.486892700195312,0,0.300872802734375,0.341705322265625,0,0.360198974609375,0,0.3841171264648438,0.1493988037109375,0,-1.541358947753906,0,0.2878341674804688,0.3315963745117188,0,0.3565750122070312,0,0.3772659301757812,0,0.2367172241210938,0,0,-1.578582763671875,0,0,0.2772293090820312,0,0.3504409790039062,0,0.3546218872070312,0,0.3677978515625,0.2762680053710938,0,-1.581993103027344,0,0.27374267578125,0,0.314453125,0,0.3492584228515625,0,0.3640823364257812,0,0,0.3275833129882812,0,-1.598526000976562,0,0.2632369995117188,0.3021011352539062,0.3407745361328125,0,0.3580398559570312,0.380584716796875,0,0,0,0,0,-1.341781616210938,0,0.2967300415039062,0,0.3397445678710938,0,0.3552703857421875,0.3780899047851562,0.01753997802734375,0,0,-1.323204040527344,0.3023452758789062,0.3419342041015625,0.3634109497070312,0,0.3603134155273438,0,0,-1.534210205078125,0.26800537109375,0.307525634765625,0,0.3386306762695312,0,0.3592681884765625,0.3049087524414062,0,-1.467002868652344,0,0.2672195434570312,0,0.3084716796875,0,0.3447036743164062,0,0.3592605590820312,0.2306442260742188,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.493339538574219,0,0,0,0,0,0,0,0.1117630004882812,0,0.2522201538085938,0,0.2756729125976562,0.3124847412109375,0,0,0.3206100463867188,0,0.328338623046875,0,0.3562774658203125,0.3939895629882812,0,0.4022216796875,0,0,0.3337631225585938,0,0,0.3312606811523438,0.3299713134765625,0.3303909301757812,0,0.3295516967773438,0,0.332489013671875,0,0.0963897705078125,0,-4.452346801757812,0,0.3425369262695312,0,0,0.3602294921875,0.3450393676757812,0,0.3723831176757812,0.3979415893554688,0,0.4077911376953125,0,0.4086761474609375,0,0.405426025390625,0.4063339233398438,0,0.4063339233398438,0.402130126953125,0,0.3298416137695312,0,0,0,0,0,-4.260574340820312,0,0.3346481323242188,0,0.3398818969726562,0,0.3363418579101562,0.3764572143554688,0,0.3941726684570312,0.401458740234375,0,0.4067230224609375,0,0.4030838012695312,0,0,0.4036026000976562,0,0.401824951171875,0,0.3979873657226562,0,0.194580078125,0,-4.402206420898438,0,0.3109970092773438,0.3381423950195312,0,0.323883056640625,0,0.3630905151367188,0,0.3839569091796875,0.3969192504882812,0,0.4030685424804688,0,0.4058380126953125,0,0.3978424072265625,0,0.4008026123046875,0.4060440063476562,0.392120361328125,0.00756072998046875,0,0,-4.194419860839844,0,0.320770263671875,0,0,0.324432373046875,0,0.3418426513671875,0,0.3727645874023438,0,0.3896865844726562,0,0.3941116333007812,0,0.4027175903320312,0,0.3983840942382812,0.4015960693359375,0,0.4029388427734375,0,0.39642333984375,0,0.17474365234375,0,0,0,-4.235893249511719,0,0.3036880493164062,0,0.3167648315429688,0,0.3288497924804688,0,0.3630905151367188,0,0.3758163452148438,0,0.3921737670898438,0,0.3950653076171875,0,0.4008941650390625,0.4029541015625,0,0.4019546508789062,0.402435302734375,0.2761917114257812,0,0,-4.265060424804688,0.2972488403320312,0,0.312591552734375,0.3205947875976562,0.3606719970703125,0,0.3669509887695312,0,0.380950927734375,0,0.3888473510742188,0,0.3974838256835938,0.4048309326171875,0.4063262939453125,0,0.4081573486328125,0.342376708984375,0,0,0,0,0,-3.983352661132812,0,0.295379638671875,0.3045578002929688,0,0.3506011962890625,0,0.3615036010742188,0,0.3774490356445312,0,0,0.3860855102539062,0,0.393402099609375,0,0.4023208618164062,0,0.4039459228515625,0.4055404663085938,0,0.42254638671875,0,0,0,0,0,-3.934638977050781,0.296142578125,0,0.31005859375,0,0.3524246215820312,0.3642578125,0,0.3786544799804688,0,0.3883819580078125,0.3949508666992188,0,0,0.4041671752929688,0.403411865234375,0,0.4056396484375,0,0.3546371459960938,0,0,0,0,0,-3.852447509765625,0,0.2876052856445312,0,0.3116455078125,0.3499679565429688,0,0.3573760986328125,0,0.3732376098632812,0,0.38226318359375,0.3920059204101562,0.401458740234375,0,0,0.4021530151367188,0,0.4020462036132812,0,0,0.3088226318359375,0,0,0,0,0,-3.76226806640625,0,0.2786407470703125,0.3193893432617188,0,0.3495254516601562,0,0.3567733764648438,0,0,0.37115478515625,0,0.3830108642578125,0.3913116455078125,0.3983612060546875,0,0,0.4010772705078125,0.4376678466796875,0,0.1896896362304688,0,-3.904792785644531,0,0,0.2744598388671875,0,0.2854537963867188,0,0.3316497802734375,0.3543014526367188,0,0.3562698364257812,0.381134033203125,0.3880386352539062,0.3967971801757812,0,0.40185546875,0,0.4049835205078125,0.3939590454101562,0,0.04828643798828125,0,0,-3.725700378417969,0,0.2725143432617188,0,0.3092575073242188,0,0.34088134765625,0,0.3511505126953125,0,0,0.3629302978515625,0,0.3775558471679688,0.3890304565429688,0.3983993530273438,0.4023284912109375,0,0.400482177734375,0.231903076171875,0,-3.793380737304688,0.2694015502929688,0,0.2826919555664062,0,0.3287353515625,0.3488006591796875,0,0.3543014526367188,0,0.377777099609375,0,0.3876495361328125,0,0.3960342407226562,0,0.4012374877929688,0.4461135864257812,0.3093948364257812,0,0,0,0,0,0,0,-3.527870178222656,0,0.274993896484375,0.3171844482421875,0,0.3404388427734375,0,0.3537826538085938,0,0.3688507080078125,0,0.3838577270507812,0.394012451171875,0,0.4014663696289062,0.4048690795898438,0,0.390869140625,0.0046539306640625,0,0,-3.527687072753906,0,0.2699432373046875,0,0.3107070922851562,0.3343505859375,0.3494949340820312,0,0.3649749755859375,0.3825531005859375,0,0.391998291015625,0.4020156860351562,0.4006118774414062,0,0.3858718872070312,0.04055023193359375,0,0,-3.514976501464844,0.2502212524414062,0,0.285858154296875,0.3182449340820312,0,0.3412017822265625,0.3508758544921875,0,0.3703231811523438,0.3841171264648438,0,0.395477294921875,0,0.4395675659179688,0,0.3965988159179688,0,0.08612823486328125,0,0,-3.467124938964844,0.2580490112304688,0,0.2911148071289062,0.3159255981445312,0.3424835205078125,0,0,0.3516311645507812,0,0.3697967529296875,0.3828201293945312,0,0.3958892822265625,0,0.4025497436523438,0,0.3950424194335938,0,0.06380462646484375,0,0,-3.410629272460938,0,0.2582626342773438,0,0.2894287109375,0,0.3124542236328125,0,0.3445205688476562,0,0.3589859008789062,0,0,0.369720458984375,0,0.3867340087890625,0,0.3964157104492188,0,0.4022140502929688,0,0.3922042846679688,0,0,0,0,0,-3.311485290527344,0.2551040649414062,0,0.2868728637695312,0,0.3148422241210938,0,0.343414306640625,0.3514251708984375,0,0.3743438720703125,0.4249343872070312,0.3981704711914062,0,0.4055252075195312,0,0.2556533813476562,0,0,0,0,0,-3.181121826171875,0,0.2704391479492188,0,0.2959976196289062,0.3279647827148438,0.3513565063476562,0,0.3649368286132812,0.3806228637695312,0,0.3910140991210938,0.4005584716796875,0,0.3925247192382812,0.1027755737304688,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-3.23785400390625,0,0.2169113159179688,0,0.2266082763671875,0.240020751953125,0,0.2700653076171875,0.3055038452148438,0.3290023803710938,0,0.3452301025390625,0.359954833984375,0.3809127807617188,0.3967971801757812,0,0.2621688842773438,0,0,0,0,0,-3.0888671875,0,0.259765625,0.2853164672851562,0.31982421875,0,0.3416671752929688,0,0.355499267578125,0,0.3692626953125,0,0.3830718994140625,0,0.3925399780273438,0.3919830322265625,0,0,0.084014892578125,0,-3.158447265625,0,0.2482833862304688,0,0.2725143432617188,0,0.3051986694335938,0,0.3349761962890625,0,0.354461669921875,0,0,0.370941162109375,0,0,0.3857040405273438,0,0.3943862915039062,0.3966445922851562,0,0.1878204345703125,0,-3.144317626953125,0.2457733154296875,0,0.273284912109375,0,0.3021621704101562,0,0.3318099975585938,0,0.352325439453125,0,0.3670806884765625,0,0.3838119506835938,0,0.3918228149414062,0,0.3978347778320312,0,0.18951416015625,0,0,-3.1231689453125,0,0.2398757934570312,0,0.2637939453125,0,0.2908706665039062,0,0.3239974975585938,0,0.3476028442382812,0,0.3576431274414062,0.3747406005859375,0,0.3849945068359375,0.3944168090820312,0.2348403930664062,0,0,0,-2.859382629394531,0,0.2639389038085938,0,0.2932205200195312,0,0.328155517578125,0,0.35150146484375,0,0.3656997680664062,0.3796615600585938,0,0.3915023803710938,0,0.3988571166992188,0,0.1749343872070312,0,0,-2.992240905761719,0,0,0.2388229370117188,0,0.265167236328125,0,0.2956924438476562,0,0.3323287963867188,0,0.3534393310546875,0,0.366973876953125,0.3831405639648438,0,0,0.3929977416992188,0.3924331665039062,0,0.05792999267578125,0,0,-2.90045166015625,0,0.2422866821289062,0,0.2683486938476562,0,0.3028793334960938,0.3354644775390625,0,0.3551559448242188,0,0.3710098266601562,0.386749267578125,0.3939437866210938,0.3300018310546875,0,0,0,-2.784233093261719,0.2524566650390625,0,0.2790603637695312,0.316558837890625,0.3442306518554688,0,0.358184814453125,0,0.3745880126953125,0,0.3911590576171875,0,0.3930587768554688,0,0.1588058471679688,0,0,-2.866676330566406,0,0.2689971923828125,0,0.2711257934570312,0,0.3098907470703125,0,0.3413238525390625,0.3579025268554688,0,0.3734817504882812,0.38299560546875,0,0.3927383422851562,0,0.25079345703125,0,0,0,0,0,-2.664932250976562,0,0.2473526000976562,0.27655029296875,0,0.3139419555664062,0,0.3437423706054688,0.349395751953125,0,0.355316162109375,0,0.3753662109375,0,0.38446044921875,0,0.1000442504882812,0,0,-2.756820678710938,0,0.2354660034179688,0,0.2626876831054688,0,0.2971038818359375,0,0.3311767578125,0.354278564453125,0,0.3596725463867188,0,0.3683090209960938,0.3851699829101562,0.2428741455078125,0,0,0,0,0,-2.556533813476562,0,0.2475814819335938,0,0.2790069580078125,0.3162765502929688,0.34844970703125,0,0.3586883544921875,0,0.37811279296875,0,0.396820068359375,0.3101959228515625,0,0,0,0,0,-2.555206298828125,0,0.2480697631835938,0,0.2776336669921875,0,0.3186187744140625,0,0.3419036865234375,0.3592987060546875,0.3768157958984375,0,0.3923110961914062,0,0.3179473876953125,0,0,0,0,0,-2.512298583984375,0.2497024536132812,0.2797088623046875,0.3176422119140625,0,0,0.3450241088867188,0,0.3602523803710938,0,0.372314453125,0,0,0.3905868530273438,0,0.273101806640625,0,0,0,0,0,-2.419952392578125,0,0.2549591064453125,0,0.287078857421875,0,0.3254928588867188,0,0.3490371704101562,0,0.352935791015625,0.3749923706054688,0.3882598876953125,0,0.1621551513671875,0,0,0,0,0,-2.352394104003906,0,0.2530136108398438,0,0.2881851196289062,0.3263397216796875,0,0.3491744995117188,0.361175537109375,0,0.380279541015625,0.3900299072265625,0,0.07779693603515625,0,-2.485595703125,0,0.2359771728515625,0,0.2662200927734375,0,0.301971435546875,0,0.3371124267578125,0,0,0.3546371459960938,0,0,0.3700408935546875,0,0.3873519897460938,0.3047943115234375,0,0,0,-2.351242065429688,0,0.2739486694335938,0,0.2826461791992188,0.3215408325195312,0.3469085693359375,0,0.3605422973632812,0,0.3808364868164062,0,0.391326904296875,0.06485748291015625,0,-2.398529052734375,0.235504150390625,0,0.2655029296875,0,0.3044509887695312,0,0.3422775268554688,0.3596038818359375,0,0.3745956420898438,0.3927154541015625,0.1939620971679688,0,0,0,0,0,-2.20440673828125,0.255035400390625,0.291748046875,0,0.3302841186523438,0,0.3512191772460938,0.3533248901367188,0,0.3777084350585938,0.3141632080078125,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2.376258850097656,0,0,0.0736846923828125,0,0.207427978515625,0,0.229156494140625,0,0.252227783203125,0.28948974609375,0,0,0.3233871459960938,0,0.3337631225585938,0,0.35833740234375,0,0,0.3763656616210938,0,0,0,0,0,-2.235214233398438,0,0.2428741455078125,0,0.27362060546875,0.3153305053710938,0,0.3438873291015625,0,0.358673095703125,0,0.3774948120117188,0,0.3901901245117188,0,0,0,-2.2073974609375,0,0.2669143676757812,0,0.2765350341796875,0,0,0.3155364990234375,0.3461456298828125,0.3590927124023438,0.3774566650390625,0.3314666748046875,0,0,0,-2.13739013671875,0,0.2410812377929688,0,0.274810791015625,0,0.3137664794921875,0,0.34375,0,0.3577728271484375,0.3764572143554688,0,0.2945632934570312,0,0,0,0,0,-2.075065612792969,0,0.2407150268554688,0,0.2766189575195312,0.3154373168945312,0.3438262939453125,0.360382080078125,0,0.3783721923828125,0.22332763671875,0,0,0,0,0,-1.998893737792969,0,0.25244140625,0.2895889282226562,0.3305511474609375,0.390899658203125,0.3732452392578125,0.3924636840820312,0,0.03234100341796875,0,0,-2.091987609863281,0,0.2323837280273438,0.2638473510742188,0,0.3018341064453125,0,0.3367996215820312,0.3581085205078125,0,0.373382568359375,0,0.2872695922851562,0,0,0,0,0,-1.97393798828125,0,0.2474441528320312,0.28424072265625,0,0.3260650634765625,0.35302734375,0,0.3681716918945312,0,0.3835525512695312,0,0,0.0720977783203125,0,-2.045074462890625,0.2343597412109375,0,0.2653045654296875,0.3032455444335938,0,0.3405914306640625,0,0.3607864379882812,0,0.3785018920898438,0,0,0.2218551635742188,0,0,0,-1.848335266113281,0.2534408569335938,0,0.2921371459960938,0,0,0.3305740356445312,0.3553390502929688,0,0.368560791015625,0,0.3070449829101562,0,0,0,0,0,-1.89776611328125,0,0.2410430908203125,0.276214599609375,0,0.3181228637695312,0.3474578857421875,0,0.3616561889648438,0,0.3818359375,0,0.02913665771484375,0,0,-1.924346923828125,0.2350845336914062,0.2682342529296875,0.3004302978515625,0,0.3360214233398438,0,0.35516357421875,0,0.3702545166015625,0,0.1160049438476562,0,0,0,0,0,-1.714637756347656,0,0.255035400390625,0.2940292358398438,0.3329086303710938,0,0,0.354644775390625,0,0.369720458984375,0,0,0.1641006469726562,0,0,0,0,0,-1.723640441894531,0.2483978271484375,0.2867279052734375,0,0.3282623291015625,0.3520584106445312,0.36590576171875,0,0.1973724365234375,0,0,0,-1.714958190917969,0,0.2442779541015625,0,0,0.2829055786132812,0.3237152099609375,0,0,0.3515167236328125,0.3659744262695312,0.200592041015625,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.710838317871094,0.2252426147460938,0,0.2451553344726562,0,0.2799301147460938,0,0.3155746459960938,0.3420639038085938,0,0.3429336547851562,0.01293182373046875,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.831710815429688,0,0,0,0,0,0.1685714721679688,0.2531509399414062,0.2808837890625,0,0.3211212158203125,0,0.3356704711914062,0,0.314697265625,0.3423385620117188,0,0.3923263549804688,0,0.4434432983398438,0,0.4032516479492188,0,0.4021682739257812,0,0.362518310546875,0,0.3295669555664062,0,0,0.33099365234375,0.3314743041992188,0.3324813842773438,0,0.3312759399414062,0,0.3316497802734375,0.3313140869140625,0,0.3319854736328125,0.330810546875,0,0,0.3332061767578125,0,0.2779083251953125,0,0,0,-7.262863159179688,0.2444610595703125,0.2983932495117188,0,0.3353729248046875,0,0.348876953125,0,0.3238601684570312,0.3664627075195312,0.388458251953125,0,0.3984832763671875,0,0.4052352905273438,0,0.4114990234375,0.4079742431640625,0,0.4094009399414062,0.4091796875,0,0.40887451171875,0,0.40972900390625,0,0.4105606079101562,0.409576416015625,0,0.4097900390625,0,0.3927154541015625,0.2821578979492188,0,0,0,0,0,-7.109642028808594,0,0.2368240356445312,0.2936477661132812,0,0,0.3253707885742188,0,0.3307342529296875,0,0,0.3321762084960938,0,0.3681488037109375,0,0.3839187622070312,0,0.3959197998046875,0,0.4056549072265625,0.4093856811523438,0,0.406097412109375,0,0.406707763671875,0.4074554443359375,0,0.4082183837890625,0,0.4083480834960938,0.40863037109375,0,0,0.4083099365234375,0.4086380004882812,0.3906707763671875,0,0.1796951293945312,0,0,0,0,0,-6.964683532714844,0,0.2600631713867188,0.28985595703125,0,0.3153610229492188,0.3129959106445312,0,0.3480148315429688,0,0.3673858642578125,0.3804702758789062,0,0.3932571411132812,0,0.39910888671875,0.4077682495117188,0.404052734375,0,0,0.404876708984375,0.4036941528320312,0,0.404510498046875,0,0.4048004150390625,0,0.4471359252929688,0,0.4077835083007812,0,0.4005966186523438,0.3910903930664062,0.02339935302734375,0,0,0,0,0,-6.772003173828125,0.2616500854492188,0,0.2879562377929688,0,0.3009872436523438,0,0.3163223266601562,0.353057861328125,0.3567581176757812,0,0.3611831665039062,0,0.38580322265625,0,0.396942138671875,0,0.4008407592773438,0.40289306640625,0.4044189453125,0,0.4055252075195312,0,0.4057235717773438,0,0.4069290161132812,0,0,0.4074783325195312,0,0.4079360961914062,0,0.3888397216796875,0,0.31903076171875,0,0,0,0,0,0,0,0,-6.642669677734375,0,0.257965087890625,0,0.2840652465820312,0.2925949096679688,0.3301239013671875,0.387542724609375,0,0.3651885986328125,0,0.3767471313476562,0.3884658813476562,0,0,0.3950347900390625,0.3996353149414062,0.4010696411132812,0.3995742797851562,0.4003677368164062,0,0,0.4029083251953125,0,0.4005889892578125,0,0.40289306640625,0,0.4007186889648438,0.3861007690429688,0,0.1661911010742188,0,0,0,0,0,-6.643234252929688,0.2517623901367188,0,0,0.2667236328125,0,0.2816543579101562,0,0.3125457763671875,0,0.3474044799804688,0,0.3560867309570312,0.3698654174804688,0,0,0.3823471069335938,0,0.3869781494140625,0.390716552734375,0,0.3942947387695312,0,0.397491455078125,0,0.40093994140625,0,0.3983917236328125,0.4015884399414062,0.4030685424804688,0,0.403961181640625,0,0.3930511474609375,0,0.2962646484375,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-6.456413269042969,0,0.2335433959960938,0.2417221069335938,0.24627685546875,0,0.295501708984375,0.326385498046875,0.3424148559570312,0,0.3513107299804688,0.3683242797851562,0.38226318359375,0.3879013061523438,0,0.3903961181640625,0,0,0.39093017578125,0.3994064331054688,0,0,0.4006576538085938,0.4017868041992188,0,0.4055328369140625,0,0.4058761596679688,0,0,0.3922042846679688,0,0.2827987670898438,0,0,0,0,0,-6.263847351074219,0,0.2528228759765625,0.2906570434570312,0.3105926513671875,0,0.338775634765625,0.3496780395507812,0.3631744384765625,0.3761672973632812,0,0.3851547241210938,0,0.3918380737304688,0,0.395416259765625,0.4009170532226562,0,0,0.4011154174804688,0.40380859375,0,0.404632568359375,0,0,0.4056777954101562,0,0.406768798828125,0,0.3908157348632812,0,0.181610107421875,0,0,0,0,0,0,0,-6.347808837890625,0,0.2447891235351562,0,0.2483901977539062,0.2671890258789062,0,0.3171234130859375,0.3391952514648438,0.3528823852539062,0.3662796020507812,0.3783721923828125,0,0.3832626342773438,0,0,0.3904266357421875,0,0.3951568603515625,0,0.3980178833007812,0,0,0.4013137817382812,0,0,0.4019775390625,0,0.4043121337890625,0,0.403472900390625,0.4031982421875,0,0.3898849487304688,0,0.04546356201171875,0,0,0,0,0,-6.136505126953125,0.2450180053710938,0.2490615844726562,0,0.2960357666015625,0,0,0.3321762084960938,0,0.3474197387695312,0,0.3576583862304688,0,0.3683013916015625,0,0.3778076171875,0,0.3867263793945312,0,0.3939437866210938,0,7.881637573242188,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7.62939453125,7.62939453125e-06,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,15.2587890625,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7.690498352050781,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,15.33411407470703,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"filename":["<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,null,null,null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,null,null,null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,null,null,null,null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,"<expr>","<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null]},"interval":10,"files":[{"filename":"<expr>","content":"## Generate Large Random Dataset\nn <- 2e6\nx <- runif(n)\ny <- runif(n)\nz <- runif(n)\nXYZ <- cbind(x,y,z)\n\n## Inspect 4 equivalent `row mean` calculations \nprofvis::profvis({\n    m <- rowSums(XYZ)/ncol(XYZ)\n    m <- rowMeans(XYZ)\n    m <- apply(XYZ, 1, mean)\n    m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }\n})\n## rowSums(), colSums(), rowMeans(), and colMeans() are vectorised and fast.\n## for loop is not the slowest, but the ugliest.","normpath":"<expr>"}],"prof_output":"/tmp/RtmpZx787i/file39426353348b.prof","highlight":{"output":["^output\\$"],"gc":["^<GC>$"],"stacktrace":["^\\.\\.stacktraceo(n|ff)\\.\\.$"]},"split":"h"}},"evals":[],"jsHooks":[]}</script>
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
##  mean1(x, 0.5) 19.58516 19.99251 20.21857 20.00112 20.02307 26.83424   100  a 
##  mean2(x, 0.5) 18.72616 19.14071 19.35622 19.14777 19.16579 21.90131   100   b
##  mean3(x, 0.5) 19.57174 19.98562 20.08648 19.99394 20.01733 22.65533   100  a
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
##  ma1(y) 169.70454 186.56621 187.71599 187.58405 190.09272 200.9890   100  a 
##  ma2(y)  19.01817  20.33762  26.39736  22.94111  24.96651 177.2961   100   b
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
##   0.102   0.000   0.033
```

```r
system.time({ lm(Y~X, data=DAT) })
```

```
##    user  system elapsed 
##   0.404   0.019   0.157
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
##   0.024   0.004   0.028
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
##   0.893   0.156   0.598
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

