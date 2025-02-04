# (PART) Reproducible Research in R {-} 


``` r
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

``` r
# Packages for Rmarkdown
install.packages("knitr")
install.packages("rmarkdown")
install.packages("bookdown")

# Other packages used in this primer
install.packages("plotly")
install.packages("sf")
```

To get started with R Markdown, you can first read and work through https://jadamso.github.io/Rbooks/small-scale-projects.html, and then recreate https://jadamso.github.io/Rbooks/small-scale-projects.html#a-homework-example yourself.


# Small Projects
***


## Code Chunks

Save the following code as `CodeChunk.R`

``` r
# Define New Function
sum_squared <- function(x1, x2) {
	y <- (x1 + x2)^2
	return(y)
} 

# Test New Function
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

``` r
source('MyFirstCode.R')
```
Note that you may first need to `setwd()` so your computer knows where you saved your code.^[You can also use *GUI: point-click* click 'Source > Source as a local job' on top right]


After you get this working
* add a the line `print(sum_squared(y, y))` to the bottom of `MyFirstCode.R`. 
* apply the function to a vectors specified outside of that script

``` r
# Pass Objects/Functions *to* Script
y <- c(3,1,NA)
source('MyFirstCode.R')

# Pass Objects/Functions *from* Script
z <- sqrt(y)/2
sum_squared(z,z)
```

**CLI Alternatives** *(Skippable)* There are also alternative ways to replicate via the command line interface (CLI) after opening a terminal.
 

``` bash
# Method 1
Rscript -e "source('CodeChunk.R')"
# Method 2
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

``` r
rmarkdown::render('DataScientism.Rmd')
```


**Example 2: Homework Assignment**
Below is a template of what homework questions (and answers) look like. Create an .Rmd from scratch that produces a similar looking .html file.

*Question 1:*
Simulate 100 random observations of the form $y=x\beta+\epsilon$ and plot the relationship. Plot and explore the data interactively via plotly, https://plotly.com/r/line-and-scatter/. Then play around with different styles, https://www.r-graph-gallery.com/13-scatter-plot.html, to best express your point.

*Answer*
I simulate $400$ observations for $\epsilon \sim 2\times N(0,1)$ and $\beta=4$, as seen in this single chunk. Notice an upward trend.

``` r
n <- 100
E <- rnorm(n)
X <- seq(n)
Y <- 4*X + 2*E

library(plotly)
plot_ly( data=data.frame(X=X,Y=Y), x=~X, y=~Y)
```

```{=html}
<div class="plotly html-widget html-fill-item" id="htmlwidget-e1caddc08930944e9298" style="width:672px;height:480px;"></div>
<script type="application/json" data-for="htmlwidget-e1caddc08930944e9298">{"x":{"visdat":{"ce1a4a8032ba":["function () ","plotlyVisDat"]},"cur_data":"ce1a4a8032ba","attrs":{"ce1a4a8032ba":{"x":{},"y":{},"alpha_stroke":1,"sizes":[10,100],"spans":[1,20]}},"layout":{"margin":{"b":40,"l":60,"t":25,"r":10},"xaxis":{"domain":[0,1],"automargin":true,"title":"X"},"yaxis":{"domain":[0,1],"automargin":true,"title":"Y"},"hovermode":"closest","showlegend":false},"source":"A","config":{"modeBarButtonsToAdd":["hoverclosest","hovercompare"],"showSendToCloud":false},"data":[{"x":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100],"y":[6.2763517001922988,6.4571774840008231,13.480347440051023,18.027240129515118,20.075378384245155,23.685728754701579,27.636863178582445,31.640882242720242,38.90520383734021,44.396081454257136,41.599112090324688,49.663007964603182,52.979935927728405,58.476532521488281,60.822746690205427,63.216513177319364,69.07405801660191,71.279974719550225,77.200110206939812,77.576504720822555,83.886923026150143,83.836024823674975,91.116394392569106,96.387743420851407,97.408630820136679,105.13575443873452,107.10861793003268,113.54366329466967,116.08525334164129,124.16319005009686,120.95575651260567,128.18206135098541,128.79833143300425,135.6264924151258,137.56751137042406,142.3385803145637,148.54194922636538,151.35547763895352,156.13885349335723,161.39163580993213,164.04121856299173,166.71404110847763,171.6939135493129,174.51287943368689,180.23580351897257,187.55008537062707,188.29718687153525,192.36312863189605,194.46679360055646,200.1170454255809,201.66659392728116,208.27904041012738,211.31204010984402,219.29049610658546,221.69993109768825,223.86148336437248,225.73401946705746,233.70776295735453,234.7622522073342,239.89979179710411,242.51979091314033,245.61795218961385,252.64852536587432,255.18136634331984,259.27244278227499,267.42156748128508,265.18584056393661,273.37260891445356,281.20569765352508,279.44557491705871,284.15893988936182,286.44424385829819,290.65619209578239,297.378845796495,299.75196352376275,302.26427706522912,309.19679645931029,312.06604838290667,318.04376214119458,319.43167151602728,325.5200550793333,328.0526392793235,332.83785846648112,337.74763493921751,340.77972085315122,340.83804224010458,346.98261014388635,356.57358558185831,351.3965728543759,362.83484202924404,362.90887336059882,366.78064570211484,372.13371972844197,379.43238496159472,378.46676946660131,383.58219739084501,389.34747525487722,389.7462016576082,397.22121033432592,402.2462828815132],"type":"scatter","mode":"markers","marker":{"color":"rgba(31,119,180,1)","line":{"color":"rgba(31,119,180,1)"}},"error_y":{"color":"rgba(31,119,180,1)"},"error_x":{"color":"rgba(31,119,180,1)"},"line":{"color":"rgba(31,119,180,1)"},"xaxis":"x","yaxis":"y","frame":null}],"highlight":{"on":"plotly_click","persistent":false,"dynamic":false,"selectize":false,"opacityDim":0.20000000000000001,"selected":{"opacity":1},"debounce":0},"shinyEvents":["plotly_hover","plotly_click","plotly_selected","plotly_relayout","plotly_brushed","plotly_brushing","plotly_clickannotation","plotly_doubleclick","plotly_deselect","plotly_afterplot","plotly_sunburstclick"],"base_url":"https://plot.ly"},"evals":[],"jsHooks":[]}</script>
```

*Question 2:*
Verify the definition of a line segment for points $A=(0,3), B=(1,5)$ using a $101 \times 101$ grid. Recall a line segment is all points $s$ that have $d(s, A) + d(s, B) = d(A, B)$.

*Answer* 

``` r
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

``` r
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

``` r
# Project Structure
home_dir    <- path.expand("~/Desktop/Project/")
data_dir_r  <- paste0(data_dir, "Data/Raw/")
data_dir_c  <- paste0(data_dir, "Data/Clean/")
out_dir     <- paste0(hdir, "Output/")
code_dir    <- paste0(hdir, "Code/")

# Execute Codes
# libraries are loaded within each RBLOCK
setwd( code_dir )
source( "RBLOCK_001_DataClean.R" )
source( "RBLOCK_002_Figures.R" )
source( "RBLOCK_003_ModelsTests.R" )
source( "RBLOCK_004_Robust.R" )

# Report all information relevant for replication
sessionInfo()
```

Notice there is a lot of documentation `# like this`, which is crucial for large projects. Also notice that anyone should be able to replicate the entire project by downloading a zip file and simply changing `home_dir`.


If some folders or files need to be created, you can do this within R

``` r
# list the files and directories
list.files(recursive=TRUE, include.dirs=TRUE)
# create directory called 'Data'
dir.create('Data')
```

## Logging/Sinking

When executing the makefile, you can also log the output in three different ways: 

1. Inserting some code into the makefile that "sinks" the output 

``` r
# Project Structure
home_dir    <- path.expand("~/Desktop/Project/")
data_dir_r  <- paste0(data_dir, "Data/Raw/")
data_dir_c  <- paste0(data_dir, "Data/Clean/")
out_dir     <- paste0(hdir, "Output/")
code_dir    <- paste0(hdir, "Code/")

# Log Output
set.wd( code_dir )
sink("MAKEFILE.Rout", append=TRUE, split=TRUE)

# Execute Codes
source( "RBLOCK_001_DataClean.R" )
source( "RBLOCK_002_Figures.R" )
source( "RBLOCK_003_ModelsTests.R" )
source( "RBLOCK_004_Robust.R" )
sessionInfo()

# Stop Logging Output
sink()
```

2. Starting a session that "sinks" the makefile

``` r
sink("MAKEFILE.Rout", append=TRUE, split=TRUE)
source("MAKEFILE.R")
sink()
```

3. Execute the makefile via the commandline 

``` bash
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

``` r
library(microbenchmark)
library(compiler)
library(profvis)
library(parallel)
library(Rcpp)
```

Problems print to the console

``` r
message("This is what a message looks like")

warning("This is what a warning looks like")

stop("This is what an error looks like")
```

```
## Error: This is what an error looks like
```

Nonproblems also print to the console

``` r
cat('cat\n')
```

```
## cat
```

``` r
print('print')
```

```
## [1] "print"
```

**Tracing**

Consider this example of an error process (originally taken from https://adv-r.hadley.nz/ ).

``` r
# Let i() check if its argument is numeric
i <- function(i0) {
  if ( !is.numeric(i0) ) {
    stop("`d` must be numeric", call.=FALSE)
  }
  i0 + 10
}

# Let f() call g() call h() call i()
h <- function(i0) i(i0)
g <- function(h0) h(h0)
f <- function(g0) g(g0)

# Observe Error
f("a")
```

```
## Error: `d` must be numeric
```

First try simple print debugging

``` r
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

``` r
traceback()
```

```
## No traceback available
```

And if that fails, try an Interactive approach

``` r
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
## debug: h(h0)
```

```
## Error: `d` must be numeric
```


**Isolating**

To inspect objects

``` r
is.object(f)
is.object(c(1,1))

class(f)
class(c(1,1))

# Storage Mode Type 
typeof(f)
typeof(c(1,1))

storage.mode(f)
storage.mode(c(1,1))
```

To check for valid inputs/outputs

``` r
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
# Many others
```

To check for values

``` r
all( x > -2 )
any( x > -2 )
# Check Matrix Rows
rowAny <- function(x) rowSums(x) > 0
rowAll <- function(x) rowSums(x) == ncol(x)
```

**Handling**

Simplest example

``` r
x <- 'A'
tryCatch(
  expr = log(x),
  error = function(e) {
        message('Caught an error but did not break')
        print(e)
        return(NA)
})
```

Another example

``` r
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

<!--# Ignore warnings/messages
    Supressing errors is possible but a bad idea
    
    ``` r
    try(1+2, silent=T)
    ```
    
    ```
    ## [1] 3
    ```
    
    ``` r
    try(warning('warning'), silent=T)
    try(error('error'), silent=T)
    
    try(1+2, silent=F)
    ```
    
    ```
    ## [1] 3
    ```
    
    ``` r
    try(warning('warning'), silent=F)
    try(error('error'), silent=F)
    ```
    
    ```
    ## Error in error("error") : could not find function "error"
    ```
    
    ``` r
    #suppressMessages()    
    ```
-->

Safe Functions

``` r
# Define
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

# Test 
log_safe( 1)
```

```
## [1] 0
```

``` r
log_safe(-1)
```

```
## Warning Caught: 
## 	<simpleWarning in log(x): NaNs produced>
```

```
## [1] NA
```

``` r
log_safe(' ')
```

```
## Error Caught: 
## 	<simpleError in log(x): non-numeric argument to mathematical function>
```

```
## [1] NA
```

``` r
# Further Tests
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

``` r
s
```

```
## [1]   NA  Inf   NA   NA  NaN -Inf   NA    0
```



## Optimizing 

In General, clean code is faster and less error prone. 

By optimizing repetitive tasks, you end up with code that

* is cleaner, faster, and more general
* can be easily parallelized

So, after identifying a bottleneck, try 

1. **vectorize your code**
2. use a dedicated package 
3. use parallel computations
4. compile your code in C++


But remember

* Don't waste time optimizing code that is not holding you back.
* Look at what has already done.


**Benchmarking**

For identifying bottlenecks, the simplest approach is to time how long a code-chunk runs

``` r
system.time({
    x0 <- runif(1e5)
    x1 <- sqrt(x0)
    x2 <- paste0('J-', x1)
})
```

```
##    user  system elapsed 
##   0.229   0.000   0.230
```

You can *visually* identify bottlenecks in larger blocks

``` r
# Generate Large Random Dataset
n <- 2e6
x <- runif(n)
y <- runif(n)
z <- runif(n)
XYZ <- cbind(x,y,z)

# Inspect 4 equivalent `row mean` calculations 
profvis::profvis({
    m <- rowSums(XYZ)/ncol(XYZ)
    m <- rowMeans(XYZ)
    m <- apply(XYZ, 1, mean)
    m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }
})
```

```{=html}
<div class="profvis html-widget html-fill-item" id="htmlwidget-8bf6ac7325a0fabae07e" style="width:100%;height:600px;"></div>
<script type="application/json" data-for="htmlwidget-8bf6ac7325a0fabae07e">{"x":{"message":{"prof":{"time":[1,1,1,1,1,1,1,1,1,1,1,1,2,3,4,5,6,7,9,10,11,12,13,14,14,14,15,15,16,16,17,17,18,18,19,19,20,20,21,21,22,22,23,23,24,24,25,25,26,26,27,27,28,28,29,29,30,30,31,31,32,32,33,33,34,35,36,36,37,38,38,39,39,40,41,41,42,43,43,44,45,45,46,47,47,48,48,49,49,50,50,51,51,52,52,53,53,54,54,55,55,56,56,57,57,58,58,59,59,60,60,61,61,62,62,63,64,64,65,66,66,67,68,69,69,70,70,71,71,72,72,73,73,74,74,75,75,76,76,77,77,78,78,79,80,80,81,81,81,82,83,84,84,85,86,86,86,87,87,87,88,88,89,89,90,90,91,91,92,92,93,94,94,95,95,96,96,97,97,98,98,99,99,99,99,100,100,100,100,101,101,102,103,103,104,104,105,106,106,107,107,108,108,109,109,110,110,111,112,112,113,113,114,115,116,116,116,117,118,118,119,120,121,121,121,122,122,122,123,123,124,124,124,125,125,125,126,126,127,128,128,129,129,130,130,131,132,133,133,134,135,136,136,136,137,137,138,139,140,141,141,142,142,143,143,144,145,146,147,147,147,148,149,149,149,150,150,150,151,151,152,152,153,153,154,155,156,156,157,157,158,158,159,160,160,161,161,161,162,162,162,163,164,164,165,165,166,166,167,167,168,169,169,170,170,171,171,171,172,173,173,174,174,174,175,175,176,176,177,177,177,178,178,179,180,180,180,181,181,182,182,183,184,184,185,186,186,186,187,187,188,188,189,189,190,191,192,193,193,194,194,195,195,196,196,197,197,198,198,199,199,200,200,201,202,202,203,204,204,205,205,206,206,207,207,208,209,209,210,210,211,212,213,213,214,214,215,215,216,216,217,217,218,219,220,220,220,221,221,221,222,223,223,224,225,225,226,226,227,228,228,229,229,230,231,231,232,232,232,233,233,234,234,235,235,236,236,236,237,237,238,239,239,240,240,241,241,242,242,243,243,243,244,244,244,245,246,247,247,248,249,249,249,250,250,251,251,251,252,252,253,253,254,254,255,255,256,256,257,257,258,258,259,259,260,260,261,261,262,262,263,263,264,264,265,265,265,266,266,266,267,267,268,269,270,271,271,272,273,274,274,275,276,276,276,277,277,277,278,278,278,279,279,279,280,280,280,281,281,281,282,282,282,283,283,283,284,284,284,285,285,286,286,287,287,288,289,289,290,291,292,292,293,293,294,294,294,295,295,295,296,296,297,298,299,299,300,300,301,301,301,302,303,304,304,305,305,305,306,306,306,307,308,308,309,309,310,310,311,312,313,314,314,315,315,315,316,316,316,317,317,318,318,319,320,320,321,322,323,323,324,325,325,326,326,326,327,327,327,328,328,329,329,329,330,330,331,331,332,332,333,334,335,335,336,336,337,337,338,338,339,339,340,340,341,341,342,342,343,343,344,344,345,345,346,346,346,347,347,347,348,349,349,350,350,351,351,352,352,353,353,353,354,355,355,356,356,357,357,358,359,360,361,361,361,362,362,363,364,364,365,366,366,366,367,367,367,368,369,369,370,371,371,372,372,373,373,374,374,375,376,376,376,376,377,377,377,377,378,378,379,379,380,380,381,382,382,383,383,384,384,385,385,386,386,387,387,388,388,389,389,390,390,391,392,392,392,393,394,395,395,396,396,397,397,398,399,399,399,400,400,400,401,402,402,402,403,403,404,404,405,405,405,406,406,406,407,407,408,408,408,409,409,410,411,412,412,413,413,414,414,414,415,415,415,416,417,417,418,418,418,419,419,420,420,421,421,422,422,423,423,423,424,424,424,425,426,426,427,427,427,428,428,429,430,430,431,432,432,433,433,434,434,435,435,436,436,437,437,438,438,438,439,439,440,440,441,441,442,442,443,443,444,444,445,445,446,447,447,448,448,449,449,450,450,450,451,451,451,452,452,452,453,453,454,455,456,456,457,457,458,459,459,460,460,461,461,461,462,462,463,463,464,464,465,466,466,466,467,467,468,468,468,469,469,469,470,470,471,472,473,473,474,474,475,475,476,476,477,477,478,479,479,480,480,481,481,481,482,482,482,483,484,484,485,485,486,486,487,487,488,488,489,489,490,490,491,491,492,492,493,493,494,494,495,495,496,496,497,497,498,498,499,499,500,500,501,501,502,502,503,503,504,504,505,505,506,506,507,507,508,508,509,509,510,510,511,511,512,512,513,513,514,514,515,515,516,516,517,517,518,518,519,520,521,521,522,522,523,523,524,525,525,526,526,527,528,529,529,529,530,530,531,531,532,532,533,534,534,535,536,536,537,538,538,538,539,539,539,540,540,541,542,542,543,544,545,545,546,547,547,548,548,549,549,549,550,551,551,552,552,553,553,554,554,555,556,556,557,557,558,559,559,560,561,561,562,562,563,563,563,564,565,566,567,567,568,568,569,570,570,571,571,572,573,574,575,575,576,576,577,578,579,579,580,580,581,582,582,583,583,583,584,584,584,585,586,586,587,587,588,588,589,589,590,591,592,592,593,594,594,595,596,596,597,598,598,599,600,601,601,602,602,603,603,604,605,605,606,606,607,607,608,608,609,609,610,610,611,611,612,613,613,614,614,615,615,616,616,616,617,617,618,619,619,620,621,621,622,622,623,623,624,624,625,625,626,626,627,628,628,628,629,629,629,630,630,631,631,632,632,633,633,634,634,634,635,635,636,636,637,637,638,638,639,639,640,640,641,641,642,642,643,643,644,644,645,645,646,647,647,647,648,648,649,650,650,651,651,652,652,653,653,653,654,654,654,655,655,656,657,657,658,659,660,660,661,661,661,662,663,663,664,665,665,666,666,667,667,668,668,669,669,670,671,671,671,672,672,672,673,673,673,674,674,675,675,675,676,676,677,678,679,680,680,681,682,682,683,684,684,685,685,686,686,687,688,689,689,689,690,691,692,692,693,693,694,694,695,695,696,697,698,698,699,699,700,701,701,702,703,703,704,705,706,706,707,707,708,708,709,709,710,711,712,712,713,713,714,714,714,715,715,715,716,716,717,717,717,718,718,719,720,720,721,721,722,722,723,723,724,724,725,725,726,726,727,727,728,728,729,729,730,731,732,732,733,734,734,735,735,735,736,736,736,737,738,738,739,739,740,740,741,742,742,743,744,745,745,745,746,747,747,748,748,749,750,750,751,751,752,753,754,755,756,756,756,757,757,757,758,758,759,759,760,761,761,762,763,764,765,765,766,766,767,768,768,769,769,770,771,772,772,773,773,774,774,775,775,776,776,777,777,778,778,779,779,780,780,781,782,783,784,784,784,785,785,786,786,787,787,788,788,789,789,790,791,791,792,792,793,793,794,794,795,795,796,796,797,797,798,798,799,800,800,801,802,802,803,803,804,804,804,805,805,806,806,807,808,808,809,809,810,810,811,811,812,812,812,813,814,814,815,815,816,816,816,817,817,817,818,818,818,819,820,821,821,822,822,823,823,824,824,825,825,826,826,827,827,828,829,829,830,831,831,832,833,833,834,834,835,835,836,836,836,837,837,837,838,838,838,839,840,840,841,841,842,842,843,843,844,844,845,845,846,846,846,847,848,849,849,850,850,851,851,852,852,853,854,854,855,855,856,856,857,857,858,859,859,860,860,861,861,862,862,863,864,864,865,865,866,866,866,867,867,868,868,868,869,869,870,870,871,871,872,872,873,874,874,875,875,875,876,876,876,877,877,877,878,879,879,880,880,881,881,882,882,883,883,884,884,885,885,886,886,887,887,888,888,888,889,890,891,891,892,893,893,894,895,895,895,896,896,896,897,897,898,899,899,900,900,901,901,902,902,903,904,904,905,906,906,907,907,908,908,909,909,910,911,911,911,912,912,913,913,913,914,914,914,915,915,915,916,916,917,918,918,919,920,921,921,922,922,923,923,923,924,924,925,926,926,927,927,927,928,928,929,929,930,930,931,931,932,932,933,933,934,934,935,935,936,936,937,937,938,939,939,940,940,941,941,942,942,943,944,945,946,946,947,948,949,949,950,951,951,951,952,952,952,953,953,953,954,954,954,955,955,955,956,956,956,957,957,957,958,958,958,959,959,959,960,960,960,961,961,961,962,962,962,963,963,963,964,964,964,965,965,965,966,966,966,967,967,968,968,968,969,969,970,971,971,972,973,973,974,975,975,976,977,977,977,978,979,980,980,981,982,982,983,984,984,984,985,985,985,986,987,987,988,988,989,990,990,991,991,992,992,993,993,994,994,995,995,996,996,996,997,998,998,999,999,1000,1000,1001,1001,1002,1002,1002,1003,1003,1003,1004,1004,1004,1005,1005,1006,1006,1007,1007,1008,1008,1009,1010,1010,1011,1012,1013,1013,1014,1014,1015,1015,1015,1016,1016,1017,1018,1018,1019,1019,1019,1020,1020,1021,1021,1022,1022,1023,1023,1024,1024,1025,1026,1026,1027,1027,1028,1028,1029,1030,1030,1031,1031,1031,1032,1033,1033,1034,1034,1035,1035,1036,1037,1037,1037,1038,1038,1038,1039,1039,1039,1040,1040,1041,1042,1043,1044,1044,1045,1045,1046,1047,1048,1048,1049,1049,1050,1050,1050,1051,1051,1052,1052,1053,1053,1054,1055,1055,1056,1056,1057,1057,1058,1058,1059,1059,1060,1061,1061,1062,1063,1063,1064,1064,1065,1066,1066,1067,1068,1069,1069,1070,1070,1071,1071,1072,1072,1072,1073,1073,1073,1074,1074,1075,1075,1076,1076,1077,1077,1078,1078,1079,1079,1080,1081,1082,1083,1083,1083,1084,1084,1085,1086,1086,1087,1087,1088,1088,1089,1089,1089,1090,1090,1090,1091,1092,1092,1092,1093,1094,1094,1095,1095,1096,1096,1097,1097,1098,1098,1099,1100,1101,1102,1102,1103,1103,1104,1104,1105,1105,1105,1106,1106,1106,1107,1107,1107,1108,1108,1109,1109,1110,1110,1111,1111,1112,1112,1113,1114,1115,1115,1116,1116,1117,1117,1118,1118,1119,1119,1120,1120,1121,1122,1122,1122,1123,1123,1123,1124,1124,1125,1125,1125,1126,1127,1127,1128,1128,1129,1130,1130,1131,1132,1132,1133,1133,1134,1134,1135,1135,1136,1137,1138,1138,1139,1139,1140,1141,1141,1142,1142,1143,1144,1144,1144,1145,1145,1146,1146,1146,1147,1148,1148,1149,1150,1151,1152,1152,1153,1153,1154,1154,1155,1155,1156,1156,1157,1157,1158,1158,1159,1159,1160,1161,1162,1163,1164,1164,1165,1165,1166,1166,1167,1167,1168,1168,1169,1169,1170,1170,1170,1171,1171,1171,1172,1173,1173,1174,1174,1175,1175,1176,1176,1177,1177,1178,1178,1179,1179,1180,1180,1181,1182,1183,1183,1184,1184,1185,1185,1186,1186,1187,1187,1188,1188,1189,1189,1190,1190,1191,1192,1193,1193,1194,1195,1195,1196,1196,1197,1197,1198,1198,1198,1199,1199,1200,1200,1201,1201,1201,1202,1202,1202,1203,1203,1203,1204,1204,1205,1205,1205,1206,1207,1208,1209,1209,1210,1210,1211,1211,1211,1212,1213,1214,1214,1215,1216,1216,1216,1217,1217,1217,1218,1218,1218,1219,1220,1220,1221,1222,1222,1223,1224,1225,1225,1226,1227,1227,1227,1228,1228,1229,1230,1230,1231,1231,1231,1232,1232,1232,1233,1233,1233,1234,1234,1235,1235,1236,1237,1237,1238,1238,1239,1240,1240,1241,1242,1243,1243,1244,1245,1245,1246,1246,1247,1247,1247,1248,1248,1248,1249,1249,1250,1251,1251,1252,1252,1253,1253,1254,1255,1255,1256,1257,1257,1258,1258,1259,1259,1260,1260,1261,1261,1262,1262,1263,1263,1264,1264,1265,1265,1265,1266,1267,1268,1269,1270,1271,1271,1272,1273,1274,1274,1274,1275,1275,1276,1276,1276,1277,1277,1277,1278,1279,1279,1280,1281,1281,1282,1282,1283,1283,1284,1284,1285,1285,1286,1286,1287,1288,1289,1289,1290,1290,1291,1291,1292,1292,1293,1294,1294,1295,1295,1296,1296,1297,1297,1298,1299,1299,1300,1301,1301,1302,1302,1303,1303,1304,1304,1304,1305,1305,1305,1306,1306,1306,1307,1307,1307,1308,1308,1308,1309,1309,1309,1310,1310,1310,1311,1311,1311,1312,1312,1312,1313,1313,1313,1314,1314,1314,1315,1315,1315,1316,1316,1316,1317,1317,1317,1318,1318,1318,1319,1320,1320,1321,1321,1322,1322,1322,1323,1323,1324,1325,1326,1327,1327,1328,1328,1329,1330,1331,1331,1332,1332,1333,1333,1334,1334,1335,1335,1336,1336,1337,1338,1338,1339,1340,1341,1342,1342,1343,1343,1344,1344,1345,1345,1345,1346,1346,1346,1347,1347,1347,1348,1349,1349,1349,1350,1350,1350,1351,1351,1352,1352,1353,1354,1354,1355,1355,1356,1356,1357,1357,1358,1358,1359,1359,1359,1360,1360,1360,1361,1361,1361,1362,1363,1363,1364,1364,1365,1366,1366,1366,1367,1367,1367,1368,1369,1370,1371,1371,1372,1372,1372,1373,1373,1373,1374,1374,1374,1375,1375,1376,1377,1378,1378,1379,1379,1380,1380,1380,1381,1381,1382,1382,1383,1383,1384,1384,1384,1385,1385,1385,1386,1386,1386,1387,1387,1387,1388,1388,1389,1389,1390,1390,1391,1392,1392,1393,1393,1393,1394,1395,1395,1395,1396,1396,1397,1397,1398,1399,1399,1399,1400,1400,1400,1401,1401,1402,1403,1403,1404,1404,1405,1406,1406,1407,1408,1408,1409,1410,1410,1411,1411,1412,1412,1412,1413,1413,1413,1414,1415,1415,1416,1416,1417,1418,1419,1419,1420,1420,1421,1421,1422,1422,1423,1423,1424,1424,1425,1425,1425,1426,1426,1426,1427,1427,1427,1428,1428,1429,1429,1430,1430,1431,1431,1432,1432,1433,1433,1434,1435,1435,1436,1436,1437,1437,1438,1438,1438,1439,1439,1439,1440,1441,1442,1443,1443,1444,1444,1445,1445,1446,1447,1447,1448,1449,1450,1450,1450,1451,1451,1451,1452,1452,1452,1453,1454,1454,1455,1456,1456,1457,1458,1459,1460,1460,1461,1462,1463,1463,1463,1464,1464,1464,1465,1465,1465,1466,1466,1467,1468,1469,1469,1470,1470,1470,1471,1471,1472,1473,1473,1474,1474,1475,1475,1475,1476,1476,1476,1477,1477,1477,1478,1478,1479,1479,1480,1480,1481,1481,1482,1483,1484,1485,1486,1487,1487,1488,1488,1489,1489,1490,1490,1491,1491,1491,1492,1493,1494,1494,1495,1495,1496,1496,1497,1498,1498,1499,1500,1500,1501,1501,1502,1503,1503,1504,1504,1505,1505,1506,1506,1507,1508,1509,1509,1509,1510,1511,1511,1511,1512,1512,1512,1513,1513,1513,1514,1515,1516,1516,1517,1518,1518,1519,1519,1520,1520,1521,1521,1522,1523,1523,1524,1524,1525,1525,1526,1526,1527,1527,1528,1528,1529,1529,1530,1530,1531,1531,1531,1532,1533,1533,1534,1534,1535,1535,1536,1537,1538,1539,1539,1539,1540,1541,1541,1542,1542,1543,1543,1544,1544,1545,1545,1546,1546,1547,1547,1548,1548,1549,1549,1550,1550,1551,1551,1552,1552,1553,1553,1554,1554,1555,1555,1556,1556,1557,1557,1558,1558,1559,1559,1560,1560,1561,1561,1562,1562,1563,1563,1564,1564,1565,1565,1566,1566,1567,1567,1568,1568,1569,1569,1570,1570,1571,1571,1572,1572,1573,1573,1574,1574,1575,1575,1576,1576,1577,1577,1578,1578,1579,1579,1580,1580,1581,1581,1582,1582,1583,1583,1584,1584,1585,1585,1586,1586,1587,1587,1588,1588,1589,1589,1590,1590,1591,1591,1592,1592,1593,1593,1594,1594,1595,1595,1596,1596,1597,1597,1598,1598,1599,1599,1600,1600,1601,1601,1602,1602,1603,1603,1604,1604,1605,1605,1606,1606,1607,1608,1608,1609,1609,1610,1610,1611,1612,1613,1613,1614,1614,1614,1615,1616,1616,1617,1617,1618,1618,1618,1619,1619,1620,1620,1621,1621,1622,1622,1623,1624,1624,1625,1625,1626,1626,1627,1628,1628,1628,1629,1630,1630,1630,1631,1631,1632,1632,1632,1633,1634,1635,1635,1636,1636,1637,1637,1637,1638,1639,1639,1640,1640,1641,1641,1642,1643,1643,1644,1644,1644,1645,1645,1645,1646,1646,1646,1647,1647,1648,1649,1650,1650,1651,1652,1652,1653,1654,1654,1654,1655,1655,1656,1657,1657,1658,1658,1658,1659,1660,1661,1662,1662,1663,1663,1664,1664,1665,1666,1666,1667,1667,1668,1668,1668,1669,1669,1670,1671,1672,1673,1673,1674,1674,1675,1675,1675,1676,1677,1677,1678,1679,1680,1680,1681,1681,1682,1682,1683,1683,1684,1684,1685,1685,1686,1686,1687,1687,1688,1688,1689,1689,1690,1690,1691,1691,1691,1692,1692,1693,1693,1694,1695,1696,1696,1696,1697,1697,1698,1699,1699,1700,1700,1701,1702,1702,1703,1703,1704,1704,1705,1706,1706,1707,1707,1708,1708,1708,1709,1710,1710,1711,1711,1712,1712,1713,1713,1713,1714,1714,1715,1715,1716,1716,1717,1717,1718,1718,1719,1720,1720,1721,1721,1722,1723,1723,1723,1724,1724,1725,1725,1726,1727,1728,1728,1729,1729,1730,1730,1730,1731,1732,1733,1733,1734,1734,1734,1735,1735,1735,1736,1736,1737,1738,1739,1739,1740,1740,1741,1741,1742,1742,1743,1743,1744,1744,1745,1745,1746,1747,1747,1748,1749,1750,1750,1751,1751,1752,1752,1753,1753,1754,1755,1755,1756,1757,1757,1758,1758,1759,1760,1760,1761,1761,1762,1763,1763,1764,1765,1765,1765,1766,1766,1767,1767,1768,1768,1768,1769,1769,1770,1770,1771,1771,1771,1772,1772,1773,1773,1773,1774,1775,1776,1776,1777,1777,1778,1778,1779,1779,1779,1780,1780,1781,1781,1782,1783,1783,1784,1784,1785,1785,1785,1786,1786,1786,1787,1787,1787,1788,1788,1789,1790,1791,1791,1792,1792,1793,1793,1793,1794,1795,1795,1796,1797,1797,1798,1798,1799,1799,1800,1801,1801,1802,1803,1803,1804,1804,1805,1806,1806,1807,1808,1809,1809,1810,1811,1811,1811,1812,1812,1812,1813,1814,1814,1815,1815,1815,1816,1817,1817,1818,1819,1819,1820,1820,1820,1821,1821,1821,1822,1822,1822,1823,1823,1823,1824,1824,1824,1825,1825,1825,1826,1826,1826,1827,1827,1827,1828,1828,1828,1829,1829,1830,1830,1831,1831,1832,1832,1833,1834,1834,1835,1835,1835,1836,1836,1837,1837,1838,1838,1839,1839,1840,1840,1841,1841,1842,1843,1843,1844,1844,1845,1845,1846,1847,1848,1849,1849,1850,1850,1851,1851,1852,1852,1853,1853,1854,1854,1855,1855,1856,1856,1857,1857,1858,1858,1859,1859,1860,1860,1861,1861,1862,1862,1863,1863,1864,1865,1865,1866,1866,1866,1867,1867,1868,1868,1869,1869,1870,1870,1871,1871,1872,1873,1873,1874,1875,1875,1876,1877,1878,1878,1879,1879,1880,1881,1882,1882,1883,1884,1884,1885,1885,1886,1887,1887,1888,1888,1889,1889,1890,1890,1891,1892,1892,1893,1893,1893,1894,1894,1894,1895,1895,1895,1896,1896,1896,1897,1898,1898,1899,1899,1900,1900,1901,1901,1902,1902,1903,1903,1904,1904,1904,1905,1905,1906,1906,1907,1907,1907,1908,1908,1909,1910,1911,1912,1913,1914,1915,1915,1916,1917,1917,1918,1918,1919,1919,1919,1920,1920,1921,1922,1922,1923,1924,1924,1925,1925,1926,1926,1926,1927,1927,1927,1928,1928,1928,1929,1929,1929,1930,1930,1931,1931,1932,1932,1933,1933,1933,1934,1934,1935,1936,1936,1937,1938,1938,1939,1939,1940,1940,1941,1941,1942,1943,1943,1944,1944,1945,1946,1946,1947,1947,1948,1948,1949,1949,1950,1950,1951,1951,1952,1952,1953,1953,1954,1954,1955,1955,1956,1956,1957,1957,1958,1959,1960,1960,1961,1961,1962,1962,1963,1963,1964,1964,1965,1965,1966,1966,1967,1967,1968,1968,1969,1969,1970,1970,1971,1971,1972,1972,1973,1973,1974,1974,1975,1975,1976,1976,1977,1977,1978,1978,1979,1979,1980,1980,1981,1981,1982,1982,1983,1983,1984,1984],"depth":[12,11,10,9,8,7,6,5,4,3,2,1,1,1,1,1,1,1,1,1,1,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,1,2,1,2,1,1,2,1,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,1,1,2,1,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,4,3,2,1,4,3,2,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,1,3,2,1,1,2,1,1,1,3,2,1,3,2,1,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,2,1,1,1,2,1,1,1,3,2,1,2,1,1,1,1,2,1,2,1,2,1,1,1,1,3,2,1,1,3,2,1,3,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,1,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,1,2,1,3,2,1,2,1,2,1,3,2,1,2,1,1,3,2,1,2,1,2,1,1,2,1,1,3,2,1,2,1,2,1,2,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,1,1,3,2,1,3,2,1,1,2,1,1,2,1,2,1,1,2,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,1,1,2,1,1,3,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,1,1,1,2,1,1,1,2,1,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,1,1,2,1,2,1,3,2,1,3,2,1,2,1,1,1,2,1,2,1,3,2,1,1,1,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,1,1,1,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,1,1,2,1,1,2,1,3,2,1,3,2,1,2,1,3,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,1,1,1,3,2,1,2,1,1,2,1,1,3,2,1,3,2,1,1,2,1,1,2,1,2,1,2,1,2,1,1,4,3,2,1,4,3,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,1,1,2,1,2,1,2,1,1,3,2,1,3,2,1,1,3,2,1,2,1,2,1,3,2,1,3,2,1,2,1,3,2,1,2,1,1,1,2,1,2,1,3,2,1,3,2,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,1,2,1,3,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,1,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,3,2,1,2,1,3,2,1,3,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,1,2,1,2,1,1,1,3,2,1,2,1,2,1,2,1,1,2,1,1,2,1,1,3,2,1,3,2,1,2,1,1,2,1,1,1,2,1,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,1,2,1,2,1,3,2,1,1,1,1,2,1,2,1,1,2,1,2,1,1,1,1,2,1,2,1,1,1,2,1,2,1,1,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,1,1,2,1,1,2,1,1,2,1,1,2,1,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,1,2,1,1,1,2,1,3,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,3,2,1,2,1,3,2,1,2,1,1,1,1,2,1,1,2,1,1,2,1,2,1,2,1,1,1,3,2,1,1,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,1,2,1,1,2,1,1,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,3,2,1,3,2,1,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,1,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,1,2,1,1,1,3,2,1,1,2,1,2,1,1,2,1,2,1,1,1,1,1,3,2,1,3,2,1,2,1,2,1,1,2,1,1,1,1,2,1,2,1,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,3,2,1,3,2,1,3,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,1,2,1,1,2,1,1,3,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,1,2,1,1,1,2,1,2,1,3,2,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,1,1,2,1,1,1,2,1,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,3,2,1,2,1,1,2,1,1,2,1,1,2,1,1,3,2,1,1,1,2,1,1,2,1,1,3,2,1,3,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,1,1,2,1,2,1,3,2,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,3,2,1,1,2,1,2,1,2,1,1,3,2,1,3,2,1,3,2,1,2,1,1,1,1,2,1,2,1,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,1,2,1,1,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,1,3,2,1,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,1,1,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,2,1,3,2,1,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,1,2,1,2,1,1,3,2,1,2,1,3,2,1,1,2,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,3,2,1,1,1,1,2,1,2,1,3,2,1,1,1,2,1,1,3,2,1,3,2,1,3,2,1,1,2,1,1,2,1,1,1,2,1,1,3,2,1,2,1,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,2,1,1,2,1,1,1,2,1,1,2,1,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,1,1,1,1,2,1,1,1,3,2,1,2,1,3,2,1,3,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,1,2,1,2,1,3,2,1,2,1,1,1,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,1,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,1,3,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,1,2,1,2,1,1,3,2,1,3,2,1,1,1,1,2,1,3,2,1,3,2,1,3,2,1,2,1,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,3,2,1,1,3,2,1,2,1,2,1,1,3,2,1,3,2,1,2,1,1,2,1,2,1,1,2,1,1,2,1,1,2,1,2,1,3,2,1,3,2,1,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,1,1,1,2,1,2,1,2,1,1,2,1,1,1,3,2,1,3,2,1,3,2,1,1,2,1,1,2,1,1,1,1,2,1,1,1,3,2,1,3,2,1,3,2,1,2,1,1,1,2,1,3,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,1,1,1,1,1,2,1,2,1,2,1,2,1,3,2,1,1,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,1,3,2,1,1,3,2,1,3,2,1,3,2,1,1,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,1,1,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,1,2,1,3,2,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,3,2,1,1,3,2,1,2,1,3,2,1,1,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,1,2,1,3,2,1,3,2,1,3,2,1,2,1,1,1,2,1,1,2,1,1,3,2,1,2,1,1,2,1,3,2,1,1,1,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,1,1,1,2,1,2,1,3,2,1,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,1,3,2,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,3,2,1,2,1,2,1,1,1,2,1,2,1,3,2,1,1,1,2,1,3,2,1,3,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,1,2,1,2,1,1,2,1,1,3,2,1,2,1,2,1,3,2,1,2,1,2,1,3,2,1,2,1,3,2,1,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,1,1,2,1,2,1,3,2,1,1,2,1,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,1,2,1,1,1,2,1,1,3,2,1,3,2,1,1,2,1,3,2,1,1,2,1,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,1,1,2,1,2,1,1,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,3,2,1,2,1,1,1,1,1,1,1,2,1,1,2,1,2,1,3,2,1,2,1,1,2,1,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1],"label":["cb$putcode","h","tryInline","cmpCall","cmp","genCode","cmpfun","compiler:::tryCmpfun","eval","eval","eval.parent","local","rowSums","rowSums","rowSums","rowSums","rowSums","rowSums","rowMeans","rowMeans","rowMeans","rowMeans","rowMeans","<GC>","aperm.default","apply","aperm.default","apply","aperm.default","apply","aperm.default","apply","aperm.default","apply","aperm.default","apply","aperm.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","apply","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","apply","FUN","apply","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","is.numeric","local","<GC>","apply","<GC>","apply","mean.default","apply","apply","FUN","apply","apply","FUN","apply","apply","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","<GC>","apply","<GC>","apply","mean.default","apply","length","local","FUN","apply","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","mean.default","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","mean.default","apply","length","local","FUN","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","is.numeric","local","apply","FUN","apply","mean.default","apply","apply","FUN","apply","is.numeric","local","FUN","apply","mean.default","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","apply","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","<GC>","apply","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","apply","isTRUE","mean.default","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","apply","apply","mean.default","apply","is.na","local","FUN","apply","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","FUN","apply","is.na","local","length","local","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","<GC>","is.numeric","local","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","apply","isTRUE","mean.default","apply","mean.default","apply","is.numeric","local","apply","length","local","apply","<GC>","mean.default","apply","is.na","local","is.na","local","FUN","apply","apply","apply","apply","FUN","apply","length","local","mean.default","apply","FUN","apply","<GC>","apply","<GC>","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","apply","mean.default","apply","mean.default","apply","mean.default","apply","length","local","apply","<GC>","apply","mean.default","apply","apply","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","apply","apply","<GC>","is.na","local","<GC>","is.na","local","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","mean.default","apply","apply","FUN","apply","<GC>","FUN","apply","mean.default","apply","is.numeric","local","is.numeric","local","isTRUE","mean.default","apply","is.na","local","apply","mean.default","apply","length","local","FUN","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","apply","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","length","local","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","apply","apply","apply","FUN","apply","apply","apply","mean.default","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","apply","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","length","local","apply","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","length","local","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","mean.default","apply","FUN","apply","FUN","apply","apply","apply","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","is.na","local","mean.default","apply","apply","FUN","apply","apply","apply","FUN","apply","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","mean.default","apply","<GC>","apply","<GC>","apply","is.na","local","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","length","local","mean.default","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","mean.default","apply","<GC>","apply","<GC>","apply","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","apply","mean.default","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","length","local","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","apply","FUN","apply","length","local","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","apply","<GC>","apply","<GC>","apply","FUN","apply","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","apply","apply","length","local","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","length","local","FUN","apply","mean.default","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","apply","mean.default","apply","apply","<GC>","apply","<GC>","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","FUN","apply","mean.default","apply","apply","<GC>","apply","<GC>","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","is.numeric","local","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","apply","apply","FUN","apply","FUN","apply","mean.default","apply","<GC>","apply","<GC>","apply","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","mean.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","mean.default","apply","apply","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","apply","FUN","apply","apply","apply","mean.default","apply","apply","length","local","length","local","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","apply","FUN","apply","mean.default","apply","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","isTRUE","mean.default","apply","apply","apply","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","FUN","apply","apply","apply","apply","mean.default","apply","FUN","apply","apply","apply","FUN","apply","is.numeric","local","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","length","local","apply","mean.default","apply","apply","FUN","apply","apply","mean.default","apply","apply","apply","FUN","apply","FUN","apply","mean.default","apply","apply","FUN","apply","<GC>","apply","<GC>","apply","mean.default","apply","FUN","apply","FUN","apply","is.numeric","local","apply","FUN","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","length","local","apply","FUN","apply","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","<GC>","is.na","local","<GC>","is.na","local","mean.default","apply","length","local","FUN","apply","FUN","apply","isTRUE","mean.default","apply","length","local","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","is.numeric","local","apply","isTRUE","mean.default","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","apply","mean.default","apply","apply","apply","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","apply","<GC>","is.na","local","<GC>","is.na","local","<GC>","is.na","local","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","apply","FUN","apply","apply","FUN","apply","apply","mean.default","apply","is.numeric","local","FUN","apply","apply","apply","isTRUE","mean.default","apply","apply","apply","mean.default","apply","<GC>","apply","<GC>","apply","FUN","apply","apply","apply","FUN","apply","mean.default","apply","apply","FUN","apply","apply","FUN","apply","apply","apply","FUN","apply","FUN","apply","length","local","FUN","apply","apply","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","length","local","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","is.numeric","local","FUN","apply","apply","apply","length","local","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","length","local","FUN","apply","mean.default","apply","apply","is.na","local","apply","apply","isTRUE","mean.default","apply","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","apply","apply","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","mean.default","apply","apply","FUN","apply","apply","apply","apply","FUN","apply","mean.default","apply","apply","FUN","apply","FUN","apply","apply","apply","mean.default","apply","mean.default","apply","length","local","mean.default","apply","<GC>","apply","<GC>","apply","FUN","apply","is.na","local","FUN","apply","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","FUN","apply","is.numeric","local","FUN","apply","FUN","apply","mean.default","apply","<GC>","apply","<GC>","apply","apply","is.numeric","local","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","is.na","local","mean.default","apply","FUN","apply","apply","FUN","apply","apply","FUN","apply","apply","FUN","apply","mean.default","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","apply","FUN","apply","mean.default","apply","<GC>","apply","<GC>","apply","apply","mean.default","apply","mean.default","apply","is.numeric","local","FUN","apply","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","is.na","local","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","is.numeric","local","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","apply","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","apply","FUN","apply","apply","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","length","local","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","mean.default","apply","is.numeric","local","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","apply","apply","apply","mean.default","apply","apply","apply","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","is.numeric","local","apply","FUN","apply","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","apply","mean.default","apply","apply","FUN","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","length","local","apply","FUN","apply","apply","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","apply","length","local","isTRUE","mean.default","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","isTRUE","mean.default","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","apply","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","is.numeric","local","FUN","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","FUN","apply","is.numeric","local","is.numeric","local","apply","is.na","local","apply","FUN","apply","FUN","apply","apply","is.na","local","apply","apply","mean.default","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","is.na","local","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","isTRUE","mean.default","apply","apply","mean.default","apply","is.na","local","FUN","apply","FUN","apply","is.numeric","local","apply","apply","apply","FUN","apply","FUN","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","is.numeric","local","is.na","local","mean.default","apply","FUN","apply","apply","apply","is.numeric","local","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","apply","apply","<GC>","apply","<GC>","apply","apply","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","apply","apply","mean.default","apply","FUN","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","is.na","local","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","FUN","apply","mean.default","apply","FUN","apply","length","local","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","apply","FUN","apply","is.na","local","FUN","apply","<GC>","apply","<GC>","apply","is.numeric","local","length","local","FUN","apply","apply","apply","FUN","apply","apply","FUN","apply","length","local","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","length","local","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","FUN","apply","apply","mean.default","apply","apply","apply","mean.default","apply","apply","isTRUE","mean.default","apply","mean.default","apply","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","FUN","apply","apply","is.numeric","local","apply","apply","FUN","apply","apply","FUN","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","apply","<GC>","apply","<GC>","apply","mean.default","apply","isTRUE","mean.default","apply","apply","apply","apply","apply","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","<GC>","apply","<GC>","apply","<GC>","apply","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","FUN","apply","apply","is.numeric","local","FUN","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","apply","mean.default","apply","mean.default","apply","apply","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","mean.default","apply","apply","FUN","apply","apply","apply","apply","mean.default","apply","mean.default","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","apply","FUN","apply","length","local","mean.default","apply","FUN","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","length","local","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","apply","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","apply","is.na","local","isTRUE","mean.default","apply","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","apply","<GC>","length","local","<GC>","length","local","length","local","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","mean.default","apply","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","length","local","FUN","apply","FUN","apply","FUN","apply","length","local","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","apply","apply","mean.default","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","mean.default","apply","apply","FUN","apply","apply","apply","apply","FUN","apply","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","is.numeric","local","apply","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","apply","apply","apply","apply","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","length","local","FUN","apply","length","local","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","isTRUE","mean.default","apply","apply","mean.default","apply","FUN","apply","length","local","apply","apply","apply","isTRUE","mean.default","apply","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","apply","FUN","apply","mean.default","apply","FUN","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","mean.default","apply","apply","isTRUE","mean.default","apply","apply","isTRUE","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","apply","mean.default","apply","FUN","apply","FUN","apply","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","apply","apply","FUN","apply","apply","mean.default","apply","apply","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","apply","length","local","FUN","apply","length","local","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","apply","mean.default","apply","length","local","isTRUE","mean.default","apply","apply","mean.default","apply","apply","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","apply","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","length","local","FUN","apply","apply","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","mean.default","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","apply","apply","is.numeric","local","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","apply","is.numeric","local","apply","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","apply","FUN","apply","apply","length","local","mean.default","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","apply","FUN","apply","is.na","local","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","is.na","local","apply","FUN","apply","apply","FUN","apply","mean.default","apply","apply","FUN","apply","apply","apply","FUN","apply","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","mean.default","apply","isTRUE","mean.default","apply","apply","mean.default","apply","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","is.na","local","FUN","apply","FUN","apply","FUN","apply","is.na","local","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","apply","mean.default","apply","is.numeric","local","is.numeric","local","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","is.numeric","local","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","mean.default","apply","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","apply","length","local","apply","mean.default","apply","apply","apply","FUN","apply","FUN","apply","apply","apply","mean.default","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","is.numeric","local","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","length","local","mean.default","apply","FUN","apply","length","local","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","apply","apply","apply","apply","FUN","apply","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","mean.default","apply","apply","FUN","apply","is.na","local","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","mean.default","apply","length","local","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","apply","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply"],"filenum":[null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null],"linenum":[null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null],"memalloc":[115.3899307250977,115.3899307250977,115.3899307250977,115.3899307250977,115.3899307250977,115.3899307250977,115.3899307250977,115.3899307250977,115.3899307250977,115.3899307250977,115.3899307250977,115.3899307250977,130.743278503418,130.743278503418,130.743278503418,130.743278503418,130.743278503418,130.743278503418,146.0022201538086,146.0022201538086,146.0022201538086,146.0022201538086,146.0022201538086,146.0025863647461,146.0025863647461,146.0025863647461,176.2883529663086,176.2883529663086,176.2883529663086,176.2883529663086,176.2883529663086,176.2883529663086,176.2883529663086,176.2883529663086,176.2883529663086,176.2883529663086,176.2883529663086,176.2883529663086,176.2883987426758,176.2883987426758,176.2882461547852,176.2882461547852,176.2882461547852,176.2882461547852,176.2882461547852,176.2882461547852,176.2882461547852,176.2882461547852,176.2882461547852,176.2882461547852,176.2882461547852,176.2882461547852,176.2882461547852,176.2882461547852,176.2882461547852,176.2882461547852,176.2882461547852,176.2882461547852,176.2882461547852,176.2882461547852,176.2882461547852,176.2882461547852,176.2880630493164,176.2880630493164,191.5468521118164,191.746223449707,191.9420700073242,191.9420700073242,192.1501693725586,192.3649749755859,192.3649749755859,192.5965805053711,192.5965805053711,192.8389129638672,193.0882873535156,193.0882873535156,193.3230514526367,193.557487487793,193.557487487793,193.7919921875,194.0289916992188,194.0289916992188,194.2615661621094,194.3811187744141,194.3811187744141,194.3811187744141,194.3811187744141,191.8145446777344,191.8145446777344,192.0393295288086,192.0393295288086,192.2805023193359,192.2805023193359,192.5350646972656,192.5350646972656,192.7863464355469,192.7863464355469,193.0370864868164,193.0370864868164,193.280876159668,193.280876159668,193.5242233276367,193.5242233276367,193.7644500732422,193.7644500732422,194.0034332275391,194.0034332275391,194.244384765625,194.244384765625,194.4393157958984,194.4393157958984,194.4393157958984,194.4393157958984,191.9161071777344,191.9161071777344,192.1314239501953,192.3663177490234,192.3663177490234,192.6136322021484,192.8634414672852,192.8634414672852,193.1111068725586,193.3536148071289,193.591682434082,193.591682434082,193.8303146362305,193.8303146362305,194.0691909790039,194.0691909790039,194.3092575073242,194.3092575073242,194.5149154663086,194.5149154663086,194.5149154663086,194.5149154663086,192.0032501220703,192.0032501220703,192.2031021118164,192.2031021118164,192.4347076416016,192.4347076416016,192.6816177368164,192.6816177368164,192.9312057495117,193.1764602661133,193.1764602661133,193.4193267822266,193.4193267822266,193.4193267822266,193.659309387207,193.8981781005859,194.1356201171875,194.1356201171875,194.3768768310547,194.5894012451172,194.5894012451172,194.5894012451172,194.5894012451172,194.5894012451172,194.5894012451172,192.1150054931641,192.1150054931641,192.3236236572266,192.3236236572266,192.5487823486328,192.5487823486328,192.7896881103516,192.7896881103516,193.0393905639648,193.0393905639648,193.2842483520508,193.5289840698242,193.5289840698242,193.7681579589844,193.7681579589844,194.0078659057617,194.0078659057617,194.2482681274414,194.2482681274414,194.4886627197266,194.4886627197266,194.6625823974609,194.6625823974609,194.6625823974609,194.6625823974609,194.6625823974609,194.6625823974609,194.6625823974609,194.6625823974609,192.2487030029297,192.2487030029297,192.4508361816406,192.6840438842773,192.6840438842773,192.929557800293,192.929557800293,193.1764984130859,193.4184112548828,193.4184112548828,193.6593551635742,193.6593551635742,193.8974685668945,193.8974685668945,194.1365127563477,194.1365127563477,194.3759841918945,194.3759841918945,194.6162872314453,194.7346572875977,194.7346572875977,194.7346572875977,194.7346572875977,192.4179534912109,192.634391784668,192.8698272705078,192.8698272705078,192.8698272705078,193.1186981201172,193.3641357421875,193.3641357421875,193.6089096069336,193.850959777832,194.092903137207,194.092903137207,194.092903137207,194.3332977294922,194.3332977294922,194.3332977294922,194.57421875,194.57421875,194.8054962158203,194.8054962158203,194.8054962158203,194.8054962158203,194.8054962158203,194.8054962158203,192.4363784790039,192.4363784790039,192.6433334350586,192.8691024780273,192.8691024780273,193.1111526489258,193.1111526489258,193.3532409667969,193.3532409667969,193.5956420898438,193.8376235961914,194.0789031982422,194.0789031982422,194.3209915161133,194.5604095458984,194.8012924194336,194.8012924194336,194.8012924194336,194.8752136230469,194.8752136230469,192.4763031005859,192.6551208496094,192.8791275024414,193.1197052001953,193.1197052001953,193.3648452758789,193.3648452758789,193.608772277832,193.608772277832,193.850212097168,194.0922622680664,194.3317184448242,194.5710906982422,194.5710906982422,194.5710906982422,194.8114700317383,194.9438400268555,194.9438400268555,194.9438400268555,194.9438400268555,194.9438400268555,194.9438400268555,192.7125854492188,192.7125854492188,192.9203643798828,192.9203643798828,193.1525726318359,193.1525726318359,193.3927307128906,193.6340789794922,193.8728561401367,193.8728561401367,194.114143371582,194.114143371582,194.3540573120117,194.3540573120117,194.5936889648438,194.8326873779297,194.8326873779297,195.0113372802734,195.0113372802734,195.0113372802734,195.0113372802734,195.0113372802734,195.0113372802734,192.7853469848633,192.9856719970703,192.9856719970703,193.2155609130859,193.2155609130859,193.4558029174805,193.4558029174805,193.6728820800781,193.6728820800781,193.8828811645508,194.0942230224609,194.0942230224609,194.3107147216797,194.3107147216797,194.5502395629883,194.5502395629883,194.5502395629883,194.7888641357422,195.0283889770508,195.0283889770508,195.0777130126953,195.0777130126953,195.0777130126953,192.8069534301758,192.8069534301758,193.0121002197266,193.0121002197266,193.2317581176758,193.2317581176758,193.2317581176758,193.4618301391602,193.4618301391602,193.7022552490234,193.9436721801758,193.9436721801758,193.9436721801758,194.1861724853516,194.1861724853516,194.426399230957,194.426399230957,194.6662216186523,194.9042434692383,194.9042434692383,195.1427993774414,195.1430358886719,195.1430358886719,195.1430358886719,192.942008972168,192.942008972168,193.1299362182617,193.1299362182617,193.3527603149414,193.3527603149414,193.5865631103516,193.8266906738281,194.0700225830078,194.3131408691406,194.3131408691406,194.5561981201172,194.5561981201172,194.8002853393555,194.8002853393555,195.0420684814453,195.0420684814453,195.2072677612305,195.2072677612305,195.2072677612305,195.2072677612305,193.0982360839844,193.0982360839844,193.3047943115234,193.3047943115234,193.5301513671875,193.7652359008789,193.7652359008789,194.0061492919922,194.2502746582031,194.2502746582031,194.4936447143555,194.4936447143555,194.7363204956055,194.7363204956055,194.9799118041992,194.9799118041992,195.2216720581055,195.2705230712891,195.2705230712891,193.1033325195312,193.1033325195312,193.2790145874023,193.4976425170898,193.7239303588867,193.7239303588867,193.9643325805664,193.9643325805664,194.2082595825195,194.2082595825195,194.4525527954102,194.4525527954102,194.6943359375,194.6943359375,194.9360198974609,195.1770477294922,195.3327255249023,195.3327255249023,195.3327255249023,195.3327255249023,195.3327255249023,195.3327255249023,193.2977981567383,193.4960098266602,193.4960098266602,193.7144775390625,193.9455871582031,193.9455871582031,194.1869277954102,194.1869277954102,194.4291915893555,194.6715240478516,194.6715240478516,194.9139099121094,194.9139099121094,195.1532745361328,195.3900985717773,195.3900985717773,195.3939590454102,195.3939590454102,195.3939590454102,193.308479309082,193.308479309082,193.5106048583984,193.5106048583984,193.7152404785156,193.7152404785156,193.9328079223633,193.9328079223633,193.9328079223633,194.1672592163086,194.1672592163086,194.4107818603516,194.653678894043,194.653678894043,194.8947982788086,194.8947982788086,195.1361999511719,195.1361999511719,195.3741683959961,195.3741683959961,195.4541625976562,195.4541625976562,195.4541625976562,195.4541625976562,195.4541625976562,195.4541625976562,193.5374526977539,193.7453918457031,193.9603652954102,193.9603652954102,194.1945037841797,194.4373321533203,194.4373321533203,194.4373321533203,194.6806793212891,194.6806793212891,194.9246139526367,194.9246139526367,194.9246139526367,195.1661071777344,195.1661071777344,195.4063415527344,195.4063415527344,195.5133819580078,195.5133819580078,195.5133819580078,195.5133819580078,193.6065292358398,193.6065292358398,193.8032531738281,193.8032531738281,194.0185623168945,194.0185623168945,194.25,194.25,194.4934234619141,194.4934234619141,194.7379989624023,194.7379989624023,194.9813995361328,194.9813995361328,195.2258834838867,195.2258834838867,195.4680023193359,195.4680023193359,195.5717239379883,195.5717239379883,195.5717239379883,195.5717239379883,195.5717239379883,195.5717239379883,193.7175216674805,193.7175216674805,193.9168701171875,194.1305236816406,194.3618698120117,194.6056060791016,194.6056060791016,194.8507461547852,195.0959396362305,195.3394165039062,195.3394165039062,195.5796737670898,195.6291046142578,195.6291046142578,195.6291046142578,195.6291046142578,195.6291046142578,195.6291046142578,195.6291046142578,195.6291046142578,195.6291046142578,195.6291046142578,195.6291046142578,195.6291046142578,195.6291046142578,195.6291046142578,195.6291046142578,195.6291046142578,195.6291046142578,195.6291046142578,195.6291046142578,195.6291046142578,195.6291046142578,195.6291046142578,195.6291046142578,195.6291046142578,195.6291046142578,195.6291046142578,195.6291046142578,193.7453994750977,193.7453994750977,193.9252853393555,193.9252853393555,194.1121292114258,194.1121292114258,194.3124160766602,194.5305252075195,194.5305252075195,194.7598876953125,195.0049514770508,195.2437744140625,195.2437744140625,195.4861755371094,195.4861755371094,195.6852951049805,195.6852951049805,195.6852951049805,195.6852951049805,195.6852951049805,195.6852951049805,193.8051910400391,193.8051910400391,193.9857788085938,194.1928405761719,194.4158630371094,194.4158630371094,194.6546249389648,194.6546249389648,194.8976821899414,194.8976821899414,194.8976821899414,195.1437454223633,195.3867111206055,195.6297912597656,195.6297912597656,195.7408447265625,195.7408447265625,195.7408447265625,195.7408447265625,195.7408447265625,195.7408447265625,193.9514694213867,194.1412963867188,194.1412963867188,194.3542861938477,194.3542861938477,194.5843353271484,194.5843353271484,194.8276138305664,195.0728149414062,195.3196487426758,195.5637359619141,195.5637359619141,195.7954864501953,195.7954864501953,195.7954864501953,195.7954864501953,195.7954864501953,195.7954864501953,193.955192565918,193.955192565918,194.130485534668,194.130485534668,194.3357162475586,194.5591583251953,194.5591583251953,194.8008499145508,195.0459899902344,195.2921829223633,195.2921829223633,195.5355682373047,195.7817153930664,195.7817153930664,195.8492660522461,195.8492660522461,195.8492660522461,195.8492660522461,195.8492660522461,195.8492660522461,194.1495132446289,194.1495132446289,194.3437881469727,194.3437881469727,194.3437881469727,194.5625839233398,194.5625839233398,194.7991256713867,194.7991256713867,195.0441055297852,195.0441055297852,195.2907028198242,195.5367202758789,195.781982421875,195.781982421875,195.9021224975586,195.9021224975586,195.9021224975586,195.9021224975586,194.1939468383789,194.1939468383789,194.3807983398438,194.3807983398438,194.5934906005859,194.5934906005859,194.8232116699219,194.8232116699219,195.0637512207031,195.0637512207031,195.3082046508789,195.3082046508789,195.5542755126953,195.5542755126953,195.7958602905273,195.7958602905273,195.9541702270508,195.9541702270508,195.9541702270508,195.9541702270508,195.9541702270508,195.9541702270508,194.2471923828125,194.435905456543,194.435905456543,194.645263671875,194.645263671875,194.8726577758789,194.8726577758789,195.1151275634766,195.1151275634766,195.3597640991211,195.3597640991211,195.3597640991211,195.6061782836914,195.8488082885742,195.8488082885742,196.0053939819336,196.0053939819336,196.0053939819336,196.0053939819336,194.3227081298828,194.5014190673828,194.7110366821289,194.9386520385742,194.9386520385742,194.9386520385742,195.1828918457031,195.1828918457031,195.4270477294922,195.6760025024414,195.6760025024414,195.9201354980469,196.0557708740234,196.0557708740234,196.0557708740234,196.0557708740234,196.0557708740234,196.0557708740234,194.4271621704102,194.6161956787109,194.6161956787109,194.8261337280273,195.0535507202148,195.0535507202148,195.297233581543,195.297233581543,195.5420074462891,195.5420074462891,195.78857421875,195.78857421875,196.0300750732422,196.1053085327148,196.1053085327148,196.1053085327148,196.1053085327148,196.1053085327148,196.1053085327148,196.1053085327148,196.1053085327148,194.5312118530273,194.5312118530273,194.7173385620117,194.7173385620117,194.9287719726562,194.9287719726562,195.1607513427734,195.4043579101562,195.4043579101562,195.6494674682617,195.6494674682617,195.8961715698242,195.8961715698242,196.1322021484375,196.1322021484375,196.1540679931641,196.1540679931641,194.4778366088867,194.4778366088867,194.6421051025391,194.6421051025391,194.8366851806641,194.8366851806641,195.0535736083984,195.0535736083984,195.2894897460938,195.5344085693359,195.5344085693359,195.5344085693359,195.7814025878906,196.0284118652344,196.2020645141602,196.2020645141602,196.2020645141602,196.2020645141602,194.6138229370117,194.6138229370117,194.788932800293,194.995491027832,194.995491027832,194.995491027832,195.2229080200195,195.2229080200195,195.2229080200195,195.4667434692383,195.7135467529297,195.7135467529297,195.7135467529297,195.9598846435547,195.9598846435547,196.1992797851562,196.1992797851562,196.2492599487305,196.2492599487305,196.2492599487305,196.2492599487305,196.2492599487305,196.2492599487305,194.7792663574219,194.7792663574219,194.976188659668,194.976188659668,194.976188659668,195.1973037719727,195.1973037719727,195.4349136352539,195.6805114746094,195.928337097168,195.928337097168,196.1744766235352,196.1744766235352,196.2957458496094,196.2957458496094,196.2957458496094,196.2957458496094,196.2957458496094,196.2957458496094,194.810188293457,194.9961929321289,194.9961929321289,195.2061004638672,195.2061004638672,195.2061004638672,195.4372177124023,195.4372177124023,195.683708190918,195.683708190918,195.9310150146484,195.9310150146484,196.1768112182617,196.1768112182617,196.3414077758789,196.3414077758789,196.3414077758789,196.3414077758789,196.3414077758789,196.3414077758789,194.8411178588867,195.0156021118164,195.0156021118164,195.221794128418,195.221794128418,195.221794128418,195.4477996826172,195.4477996826172,195.6882629394531,195.9321517944336,195.9321517944336,196.1765060424805,196.3863525390625,196.3863525390625,196.3863525390625,196.3863525390625,194.8682556152344,194.8682556152344,195.0554504394531,195.0554504394531,195.2512817382812,195.2512817382812,195.4722061157227,195.4722061157227,195.7107009887695,195.7107009887695,195.7107009887695,195.9558181762695,195.9558181762695,196.2037658691406,196.2037658691406,196.430549621582,196.430549621582,196.430549621582,196.430549621582,194.9397201538086,194.9397201538086,195.1274948120117,195.1274948120117,195.3294982910156,195.3294982910156,195.5536041259766,195.7961120605469,195.7961120605469,196.0443954467773,196.0443954467773,196.2931823730469,196.2931823730469,196.4741058349609,196.4741058349609,196.4741058349609,196.4741058349609,196.4741058349609,196.4741058349609,195.0331726074219,195.0331726074219,195.0331726074219,195.2073822021484,195.2073822021484,195.413818359375,195.6426315307617,195.8882293701172,195.8882293701172,196.1361923217773,196.1361923217773,196.3845443725586,196.5168533325195,196.5168533325195,196.5168533325195,196.5168533325195,195.1454925537109,195.1454925537109,195.1454925537109,195.3395385742188,195.3395385742188,195.553092956543,195.553092956543,195.7881011962891,195.7881011962891,196.0321426391602,196.2776565551758,196.2776565551758,196.2776565551758,196.5203170776367,196.5203170776367,196.558967590332,196.558967590332,196.558967590332,196.558967590332,196.558967590332,196.558967590332,195.2649993896484,195.2649993896484,195.4586563110352,195.6784286499023,195.9191207885742,195.9191207885742,196.1661758422852,196.1661758422852,196.4134902954102,196.4134902954102,196.6003723144531,196.6003723144531,196.6003723144531,196.6003723144531,195.2221984863281,195.3835830688477,195.3835830688477,195.5557098388672,195.5557098388672,195.7605133056641,195.7605133056641,195.7605133056641,195.9854736328125,195.9854736328125,195.9854736328125,196.2311859130859,196.4825973510742,196.4825973510742,196.6411056518555,196.6411056518555,196.6411056518555,196.6411056518555,196.6411056518555,196.6411056518555,196.6411056518555,196.6411056518555,196.6411056518555,196.6411056518555,196.6411056518555,196.6411056518555,196.6411056518555,196.6411056518555,196.6411056518555,196.6411056518555,196.6411056518555,196.6411056518555,196.6411056518555,196.6411056518555,196.6411056518555,196.6411056518555,196.6411056518555,196.6411056518555,196.6411056518555,196.6411056518555,196.6411056518555,196.6411056518555,196.6411056518555,196.6411056518555,196.6411056518555,196.6411056518555,196.6411056518555,196.6411056518555,196.6411056518555,196.6411056518555,196.6411056518555,196.6411056518555,196.6411056518555,196.6411056518555,196.6411056518555,196.6411056518555,196.6411056518555,196.6411056518555,196.6411056518555,196.6411056518555,196.6411056518555,196.6411056518555,196.6411056518555,196.6411056518555,196.6411056518555,196.6411056518555,196.6411056518555,196.6411056518555,195.2375793457031,195.2375793457031,195.2375793457031,195.2375793457031,195.2815475463867,195.2815475463867,195.482307434082,195.482307434082,195.6909332275391,195.6909332275391,195.9159469604492,195.9159469604492,196.1562957763672,196.1562957763672,196.3811569213867,196.602180480957,196.844352722168,196.844352722168,197.0822982788086,197.0822982788086,197.3188400268555,197.3188400268555,197.5643844604492,197.8019180297852,197.8019180297852,198.0001983642578,198.0001983642578,198.1997146606445,198.3979034423828,198.5985946655273,198.5985946655273,198.5985946655273,198.7963485717773,198.7963485717773,198.9965515136719,198.9965515136719,199.1967697143555,199.1967697143555,199.39453125,199.5948104858398,199.5948104858398,199.791633605957,199.9909744262695,199.9909744262695,200.1893310546875,200.3196563720703,200.3196563720703,200.3196563720703,200.3196563720703,200.3196563720703,200.3196563720703,195.5019989013672,195.5019989013672,195.7055892944336,195.9418792724609,195.9418792724609,196.1914749145508,196.4304046630859,196.6518707275391,196.6518707275391,196.8961868286133,197.1392059326172,197.1392059326172,197.3815383911133,197.3815383911133,197.6301574707031,197.6301574707031,197.6301574707031,197.8825378417969,198.1367340087891,198.1367340087891,198.3908233642578,198.3908233642578,198.6437454223633,198.6437454223633,198.8976135253906,198.8976135253906,199.1501770019531,199.4033203125,199.4033203125,199.6562042236328,199.6562042236328,199.9078826904297,200.1540222167969,200.1540222167969,200.3929061889648,200.4586334228516,200.4586334228516,200.4586334228516,200.4586334228516,195.7910690307617,195.7910690307617,195.7910690307617,195.9958114624023,196.2315444946289,196.4748611450195,196.7023162841797,196.7023162841797,196.9390106201172,196.9390106201172,197.1864166259766,197.4298248291016,197.4298248291016,197.6728363037109,197.6728363037109,197.9145431518555,198.1650466918945,198.4174499511719,198.6704330444336,198.6704330444336,198.9222259521484,198.9222259521484,199.1744613647461,199.4273147583008,199.6795806884766,199.6795806884766,199.9326324462891,199.9326324462891,200.1851959228516,200.4264526367188,200.4264526367188,200.5954055786133,200.5954055786133,200.5954055786133,200.5954055786133,200.5954055786133,200.5954055786133,195.9145050048828,196.0961151123047,196.0961151123047,196.3176803588867,196.3176803588867,196.5519409179688,196.5519409179688,196.7774276733398,196.7774276733398,197.0062484741211,197.2495269775391,197.4884796142578,197.4884796142578,197.7265777587891,197.9624404907227,197.9624404907227,198.2030868530273,198.4460296630859,198.4460296630859,198.6963272094727,198.9452743530273,198.9452743530273,199.1961898803711,199.4475402832031,199.6989288330078,199.6989288330078,199.9507522583008,199.9507522583008,200.2037963867188,200.2037963867188,200.4516143798828,200.6884536743164,200.6884536743164,200.7299270629883,200.7299270629883,200.7299270629883,200.7299270629883,196.2155609130859,196.2155609130859,196.4164581298828,196.4164581298828,196.6458053588867,196.6458053588867,196.8735961914062,196.8735961914062,197.1025695800781,197.3484115600586,197.3484115600586,197.5941314697266,197.5941314697266,197.8353576660156,197.8353576660156,198.0763168334961,198.0763168334961,198.0763168334961,198.3181457519531,198.3181457519531,198.5606002807617,198.8054046630859,198.8054046630859,199.0568466186523,199.308349609375,199.308349609375,199.5597763061523,199.5597763061523,199.811408996582,199.811408996582,200.0639190673828,200.0639190673828,200.316764831543,200.316764831543,200.5649032592773,200.5649032592773,200.8038864135742,200.8623504638672,200.8623504638672,200.8623504638672,200.8623504638672,200.8623504638672,200.8623504638672,196.4081726074219,196.4081726074219,196.6077194213867,196.6077194213867,196.8328170776367,196.8328170776367,197.0516204833984,197.0516204833984,197.2830963134766,197.2830963134766,197.2830963134766,197.5251083374023,197.5251083374023,197.7679138183594,197.7679138183594,198.007453918457,198.007453918457,198.2466125488281,198.2466125488281,198.4836807250977,198.4836807250977,198.7219772338867,198.7219772338867,198.9592361450195,198.9592361450195,199.1996383666992,199.1996383666992,199.4386596679688,199.4386596679688,199.6853561401367,199.6853561401367,199.9352569580078,199.9352569580078,200.1860427856445,200.4367599487305,200.4367599487305,200.4367599487305,200.6860809326172,200.6860809326172,200.9256057739258,200.9926071166992,200.9926071166992,200.9926071166992,200.9926071166992,196.5986633300781,196.5986633300781,196.7936325073242,196.7936325073242,196.7936325073242,197.0113906860352,197.0113906860352,197.0113906860352,197.2270889282227,197.2270889282227,197.464714050293,197.7091217041016,197.7091217041016,197.9534149169922,198.1929931640625,198.4327621459961,198.4327621459961,198.6703567504883,198.6703567504883,198.6703567504883,198.9113235473633,199.1518249511719,199.1518249511719,199.3908996582031,199.6382598876953,199.6382598876953,199.8874359130859,199.8874359130859,200.136962890625,200.136962890625,200.3894729614258,200.3894729614258,200.6412658691406,200.6412658691406,200.8857727050781,201.1206970214844,201.1206970214844,201.1206970214844,201.1206970214844,201.1206970214844,201.1206970214844,201.1206970214844,201.1206970214844,201.1206970214844,196.8794860839844,196.8794860839844,197.0919952392578,197.0919952392578,197.0919952392578,197.3023681640625,197.3023681640625,197.522590637207,197.7548217773438,197.9970321655273,198.2330932617188,198.2330932617188,198.4695816040039,198.704948425293,198.704948425293,198.9411392211914,199.1777038574219,199.1777038574219,199.4189987182617,199.4189987182617,199.6611862182617,199.6611862182617,199.9001846313477,200.1422729492188,200.3895492553711,200.3895492553711,200.3895492553711,200.6413955688477,200.8925018310547,201.1285018920898,201.1285018920898,201.2467956542969,201.2467956542969,201.2467956542969,201.2467956542969,196.9588623046875,196.9588623046875,197.1634674072266,197.371826171875,197.5823440551758,197.5823440551758,197.8210144042969,197.8210144042969,198.0652389526367,198.306884765625,198.306884765625,198.5450668334961,198.7829513549805,198.7829513549805,199.0183181762695,199.2562637329102,199.4945602416992,199.4945602416992,199.7343673706055,199.7343673706055,199.9767456054688,199.9767456054688,200.2281723022461,200.2281723022461,200.4807357788086,200.7330703735352,200.9863891601562,200.9863891601562,201.2277374267578,201.2277374267578,201.3708724975586,201.3708724975586,201.3708724975586,201.3708724975586,201.3708724975586,201.3708724975586,197.1267013549805,197.1267013549805,197.3302612304688,197.3302612304688,197.3302612304688,197.5313491821289,197.5313491821289,197.7372436523438,197.9723052978516,197.9723052978516,198.2139587402344,198.2139587402344,198.4555816650391,198.4555816650391,198.6919937133789,198.6919937133789,198.9283142089844,198.9283142089844,199.1625747680664,199.1625747680664,199.3978729248047,199.3978729248047,199.6395645141602,199.6395645141602,199.8811492919922,199.8811492919922,200.1236419677734,200.1236419677734,200.3672714233398,200.6187286376953,200.8708419799805,200.8708419799805,201.1235046386719,201.3655548095703,201.3655548095703,201.4928970336914,201.4928970336914,201.4928970336914,201.4928970336914,201.4928970336914,201.4928970336914,197.3316650390625,197.5320816040039,197.5320816040039,197.7296600341797,197.7296600341797,197.938835144043,197.938835144043,198.1750717163086,198.4171981811523,198.4171981811523,198.6593856811523,198.8979644775391,199.1355972290039,199.1355972290039,199.1355972290039,199.3709411621094,199.6082916259766,199.6082916259766,199.8494491577148,199.8494491577148,200.0893402099609,200.3355026245117,200.3355026245117,200.5842895507812,200.5842895507812,200.8351211547852,201.0874481201172,201.3336410522461,201.5731658935547,201.6129455566406,201.6129455566406,201.6129455566406,201.6129455566406,201.6129455566406,201.6129455566406,197.588134765625,197.588134765625,197.7836761474609,197.7836761474609,197.9811477661133,198.2078094482422,198.2078094482422,198.4463424682617,198.6867904663086,198.9270172119141,199.1642761230469,199.1642761230469,199.4006729125977,199.4006729125977,199.6374130249023,199.8772201538086,199.8772201538086,200.1174621582031,200.1174621582031,200.358024597168,200.5994338989258,200.8495483398438,200.8495483398438,201.102783203125,201.102783203125,201.3568572998047,201.3568572998047,201.5992050170898,201.5992050170898,201.7311248779297,201.7311248779297,201.7311248779297,201.7311248779297,197.6989517211914,197.6989517211914,197.8951721191406,197.8951721191406,198.0876998901367,198.0876998901367,198.3043441772461,198.5322875976562,198.7425765991211,198.9509963989258,198.9509963989258,198.9509963989258,199.1783905029297,199.1783905029297,199.4121780395508,199.4121780395508,199.6457061767578,199.6457061767578,199.877685546875,199.877685546875,200.1122894287109,200.1122894287109,200.3501129150391,200.5857086181641,200.5857086181641,200.82470703125,200.82470703125,201.0730438232422,201.0730438232422,201.3227767944336,201.3227767944336,201.5710067749023,201.5710067749023,201.8087921142578,201.8087921142578,201.847282409668,201.847282409668,201.847282409668,201.847282409668,197.9538192749023,198.144775390625,198.144775390625,198.3447341918945,198.5681762695312,198.5681762695312,198.8061065673828,198.8061065673828,199.0454940795898,199.0454940795898,199.0454940795898,199.2842788696289,199.2842788696289,199.5203170776367,199.5203170776367,199.7573623657227,199.9937286376953,199.9937286376953,200.2313232421875,200.2313232421875,200.4710235595703,200.4710235595703,200.718635559082,200.718635559082,200.9704666137695,200.9704666137695,200.9704666137695,201.2232894897461,201.4759902954102,201.4759902954102,201.7240982055664,201.7240982055664,201.9617080688477,201.9617080688477,201.9617080688477,201.9617080688477,201.9617080688477,201.9617080688477,201.9617080688477,201.9617080688477,201.9617080688477,198.1478958129883,198.3366088867188,198.5413360595703,198.5413360595703,198.7587280273438,198.7587280273438,198.987548828125,198.987548828125,199.2219848632812,199.2219848632812,199.4582061767578,199.4582061767578,199.6908721923828,199.6908721923828,199.9267120361328,199.9267120361328,200.1621551513672,200.3980255126953,200.3980255126953,200.6347427368164,200.8738098144531,200.8738098144531,201.1131591796875,201.3582458496094,201.3582458496094,201.608154296875,201.608154296875,201.8537750244141,201.8537750244141,202.0741882324219,202.0741882324219,202.0741882324219,202.0741882324219,202.0741882324219,202.0741882324219,202.0741882324219,202.0741882324219,202.0741882324219,198.3282775878906,198.5143508911133,198.5143508911133,198.7186050415039,198.7186050415039,198.9395065307617,198.9395065307617,199.1723480224609,199.1723480224609,199.409065246582,199.409065246582,199.6503448486328,199.6503448486328,199.8892059326172,199.8892059326172,199.8892059326172,200.1274642944336,200.3641815185547,200.6028442382812,200.6028442382812,200.8430938720703,200.8430938720703,201.0845108032227,201.0845108032227,201.3314056396484,201.3314056396484,201.582160949707,201.8341445922852,201.8341445922852,202.0752639770508,202.0752639770508,202.1848373413086,202.1848373413086,202.1848373413086,202.1848373413086,198.4069519042969,198.5934982299805,198.5934982299805,198.786003112793,198.786003112793,199.0002517700195,199.0002517700195,199.2250213623047,199.2250213623047,199.4608154296875,199.6982803344727,199.6982803344727,199.9358901977539,199.9358901977539,200.1719207763672,200.1719207763672,200.1719207763672,200.4075546264648,200.4075546264648,200.64306640625,200.64306640625,200.64306640625,200.8799514770508,200.8799514770508,201.118408203125,201.118408203125,201.3607559204102,201.3607559204102,201.6129302978516,201.6129302978516,201.865478515625,202.1119537353516,202.1119537353516,202.2937622070312,202.2937622070312,202.2937622070312,202.2937622070312,202.2937622070312,202.2937622070312,202.2937622070312,202.2937622070312,202.2937622070312,198.7123565673828,198.9003372192383,198.9003372192383,199.1073532104492,199.1073532104492,199.3262100219727,199.3262100219727,199.55517578125,199.55517578125,199.7919311523438,199.7919311523438,200.0296783447266,200.0296783447266,200.2635879516602,200.2635879516602,200.4999465942383,200.4999465942383,200.7350692749023,200.7350692749023,200.9719848632812,200.9719848632812,200.9719848632812,201.2100830078125,201.4406585693359,201.6759719848633,201.6759719848633,201.9132843017578,202.1505279541016,202.1505279541016,202.379280090332,202.40087890625,202.40087890625,202.40087890625,202.40087890625,202.40087890625,202.40087890625,198.8101577758789,198.8101577758789,198.9943084716797,199.1918182373047,199.1918182373047,199.4034576416016,199.4034576416016,199.6269989013672,199.6269989013672,199.8635635375977,199.8635635375977,200.1037673950195,200.3420867919922,200.3420867919922,200.5814819335938,200.8190078735352,200.8190078735352,201.0580215454102,201.0580215454102,201.2980575561523,201.2980575561523,201.5381088256836,201.5381088256836,201.7891082763672,202.0420989990234,202.0420989990234,202.0420989990234,202.290901184082,202.290901184082,202.5062561035156,202.5062561035156,202.5062561035156,202.5062561035156,202.5062561035156,202.5062561035156,202.5062561035156,202.5062561035156,202.5062561035156,199.0043640136719,199.0043640136719,199.1917724609375,199.3916549682617,199.3916549682617,199.6004028320312,199.8223495483398,200.0586471557617,200.0586471557617,200.2983474731445,200.2983474731445,200.5299758911133,200.5299758911133,200.5299758911133,200.7649307250977,200.7649307250977,200.9985427856445,201.2325973510742,201.2325973510742,201.4661407470703,201.4661407470703,201.4661407470703,201.7059936523438,201.7059936523438,201.9456939697266,201.9456939697266,202.1859436035156,202.1859436035156,202.4272537231445,202.4272537231445,202.6099624633789,202.6099624633789,202.6099624633789,202.6099624633789,202.6099624633789,202.6099624633789,199.1837463378906,199.1837463378906,199.3694076538086,199.3694076538086,199.5627975463867,199.5627975463867,199.7665557861328,199.984489440918,199.984489440918,200.2127227783203,200.2127227783203,200.4466552734375,200.4466552734375,200.6816101074219,200.6816101074219,200.9172592163086,201.1516952514648,201.3898162841797,201.6281280517578,201.6281280517578,201.8676376342773,202.1125030517578,202.3660583496094,202.3660583496094,202.6086730957031,202.712043762207,202.712043762207,202.712043762207,202.712043762207,202.712043762207,202.712043762207,202.712043762207,202.712043762207,202.712043762207,202.712043762207,202.712043762207,202.712043762207,202.712043762207,202.712043762207,202.712043762207,202.712043762207,202.712043762207,202.712043762207,202.712043762207,202.712043762207,202.712043762207,202.712043762207,202.712043762207,202.712043762207,202.712043762207,202.712043762207,202.712043762207,202.712043762207,202.712043762207,202.712043762207,202.712043762207,202.712043762207,202.712043762207,202.712043762207,202.712043762207,202.712043762207,202.712043762207,202.712043762207,202.712043762207,202.712043762207,202.712043762207,202.712043762207,202.712043762207,202.712043762207,202.712043762207,202.712043762207,202.712043762207,202.712043762207,199.2416915893555,199.2416915893555,199.3894424438477,199.3894424438477,199.3894424438477,199.5657730102539,199.5657730102539,199.7514266967773,199.9395751953125,199.9395751953125,200.1437911987305,200.3613815307617,200.3613815307617,200.5888671875,200.824462890625,200.824462890625,201.0573883056641,201.2917785644531,201.2917785644531,201.2917785644531,201.5282974243164,201.7668380737305,202.0087738037109,202.0087738037109,202.2593307495117,202.5097351074219,202.5097351074219,202.7459259033203,202.8121032714844,202.8121032714844,202.8121032714844,202.8121032714844,202.8121032714844,202.8121032714844,199.3909683227539,199.563591003418,199.563591003418,199.752555847168,199.752555847168,199.9101333618164,200.0732040405273,200.0732040405273,200.2907562255859,200.2907562255859,200.5227203369141,200.5227203369141,200.763298034668,200.763298034668,201.0017700195312,201.0017700195312,201.2422180175781,201.2422180175781,201.4803161621094,201.4803161621094,201.4803161621094,201.7222747802734,201.9635543823242,201.9635543823242,202.2055358886719,202.2055358886719,202.4591598510742,202.4591598510742,202.7105712890625,202.7105712890625,202.9109649658203,202.9109649658203,202.9109649658203,202.9109649658203,202.9109649658203,202.9109649658203,202.9109649658203,202.9109649658203,202.9109649658203,199.6386947631836,199.6386947631836,199.826789855957,199.826789855957,200.0224609375,200.0224609375,200.2332153320312,200.2332153320312,200.458122253418,200.6982192993164,200.6982192993164,200.9416580200195,201.1818161010742,201.4229431152344,201.4229431152344,201.6626663208008,201.6626663208008,201.903938293457,201.903938293457,201.903938293457,202.1469955444336,202.1469955444336,202.3933715820312,202.6490325927734,202.6490325927734,202.8943099975586,202.8943099975586,202.8943099975586,203.0081253051758,203.0081253051758,203.0081253051758,203.0081253051758,199.6800918579102,199.6800918579102,199.8553924560547,199.8553924560547,200.0413970947266,200.0413970947266,200.236946105957,200.4343032836914,200.4343032836914,200.6565093994141,200.6565093994141,200.8940811157227,200.8940811157227,201.1334533691406,201.3715667724609,201.3715667724609,201.6108779907227,201.6108779907227,201.6108779907227,201.8496780395508,202.0911483764648,202.0911483764648,202.3389587402344,202.3389587402344,202.5925369262695,202.5925369262695,202.8469772338867,203.0882263183594,203.0882263183594,203.0882263183594,203.1038208007812,203.1038208007812,203.1038208007812,203.1038208007812,203.1038208007812,203.1038208007812,199.8851547241211,199.8851547241211,200.0677185058594,200.2584609985352,200.4653472900391,200.6886596679688,200.6886596679688,200.9287109375,200.9287109375,201.1713943481445,201.4117965698242,201.6504592895508,201.6504592895508,201.8873748779297,201.8873748779297,202.1272354125977,202.1272354125977,202.1272354125977,202.375373840332,202.375373840332,202.6289138793945,202.6289138793945,202.8828125,202.8828125,203.1277313232422,203.1979370117188,203.1979370117188,203.1979370117188,203.1979370117188,199.9996109008789,199.9996109008789,200.1786422729492,200.1786422729492,200.3658676147461,200.3658676147461,200.5671005249023,200.7838516235352,200.7838516235352,201.0159683227539,201.2549667358398,201.2549667358398,201.4946670532227,201.4946670532227,201.7319869995117,201.97216796875,201.97216796875,202.2122573852539,202.4534683227539,202.6967163085938,202.6967163085938,202.9481353759766,202.9481353759766,203.1946792602539,203.1946792602539,203.2905044555664,203.2905044555664,203.2905044555664,203.2905044555664,203.2905044555664,203.2905044555664,200.1307601928711,200.1307601928711,200.3131332397461,200.3131332397461,200.5008392333984,200.5008392333984,200.7016448974609,200.7016448974609,200.9172439575195,200.9172439575195,201.1513671875,201.1513671875,201.3947830200195,201.6376953125,201.878044128418,202.1194534301758,202.1194534301758,202.1194534301758,202.3645706176758,202.3645706176758,202.6167984008789,202.8715362548828,202.8715362548828,203.1263198852539,203.1263198852539,203.3642730712891,203.3642730712891,203.3816452026367,203.3816452026367,203.3816452026367,203.3816452026367,203.3816452026367,203.3816452026367,200.3200836181641,200.5005416870117,200.5005416870117,200.5005416870117,200.691162109375,200.897819519043,200.897819519043,201.1191101074219,201.1191101074219,201.3577270507812,201.3577270507812,201.5997161865234,201.5997161865234,201.841194152832,201.841194152832,202.080924987793,202.3208541870117,202.5620880126953,202.8047103881836,202.8047103881836,203.0538711547852,203.0538711547852,203.3030624389648,203.3030624389648,203.4711990356445,203.4711990356445,203.4711990356445,203.4711990356445,203.4711990356445,203.4711990356445,203.4711990356445,203.4711990356445,203.4711990356445,200.5268173217773,200.5268173217773,200.7116317749023,200.7116317749023,200.9053573608398,200.9053573608398,201.1150283813477,201.1150283813477,201.3371658325195,201.3371658325195,201.5775146484375,201.8195495605469,202.0596160888672,202.0596160888672,202.3010559082031,202.3010559082031,202.5405807495117,202.5405807495117,202.7834396362305,202.7834396362305,203.0261459350586,203.0261459350586,203.2707366943359,203.2707366943359,203.5155944824219,203.5594100952148,203.5594100952148,203.5594100952148,203.5594100952148,203.5594100952148,203.5594100952148,200.5702362060547,200.5702362060547,200.7425765991211,200.7425765991211,200.7425765991211,200.9289627075195,201.129638671875,201.129638671875,201.3467025756836,201.3467025756836,201.5833740234375,201.8247146606445,201.8247146606445,202.0658798217773,202.3044509887695,202.3044509887695,202.5425720214844,202.5425720214844,202.7831726074219,202.7831726074219,203.0247802734375,203.0247802734375,203.269645690918,203.5179977416992,203.6461410522461,203.6461410522461,203.6461410522461,203.6461410522461,200.6620788574219,200.8403854370117,200.8403854370117,201.0258483886719,201.0258483886719,201.224479675293,201.4417419433594,201.4417419433594,201.4417419433594,201.6754531860352,201.6754531860352,201.9169311523438,201.9169311523438,201.9169311523438,202.1519622802734,202.3620910644531,202.3620910644531,202.5925598144531,202.8446502685547,203.0974273681641,203.3512725830078,203.3512725830078,203.6007919311523,203.6007919311523,203.7314071655273,203.7314071655273,203.7314071655273,203.7314071655273,203.7314071655273,203.7314071655273,200.9495468139648,200.9495468139648,201.1357116699219,201.1357116699219,201.3322448730469,201.3322448730469,201.5477981567383,201.7813568115234,202.0253753662109,202.2713470458984,202.5147933959961,202.5147933959961,202.7580032348633,202.7580032348633,202.9991073608398,202.9991073608398,203.2435455322266,203.2435455322266,203.4887084960938,203.4887084960938,203.7354583740234,203.7354583740234,203.8154296875,203.8154296875,203.8154296875,203.8154296875,203.8154296875,203.8154296875,200.9508972167969,201.1311645507812,201.1311645507812,201.3187713623047,201.3187713623047,201.5169296264648,201.5169296264648,201.7339859008789,201.7339859008789,201.9684066772461,201.9684066772461,202.2110977172852,202.2110977172852,202.4542770385742,202.4542770385742,202.692741394043,202.692741394043,202.9304122924805,203.1704406738281,203.4111251831055,203.4111251831055,203.6540145874023,203.6540145874023,203.8931732177734,203.8931732177734,203.8980712890625,203.8980712890625,203.8980712890625,203.8980712890625,201.1341705322266,201.1341705322266,201.313346862793,201.313346862793,201.5003509521484,201.5003509521484,201.7045593261719,201.9261856079102,202.1661071777344,202.1661071777344,202.4076309204102,202.6469116210938,202.6469116210938,202.8863143920898,202.8863143920898,203.1247711181641,203.1247711181641,203.3655090332031,203.3655090332031,203.3655090332031,203.6099395751953,203.6099395751953,203.8589324951172,203.8589324951172,203.9793167114258,203.9793167114258,203.9793167114258,203.9793167114258,203.9793167114258,203.9793167114258,203.9793167114258,203.9793167114258,203.9793167114258,201.3600845336914,201.3600845336914,201.5471649169922,201.5471649169922,201.5471649169922,201.744026184082,201.9583587646484,202.1913833618164,202.4362945556641,202.4362945556641,202.6822967529297,202.6822967529297,202.9251861572266,202.9251861572266,202.9251861572266,203.1669616699219,203.4085922241211,203.6565933227539,203.6565933227539,203.8977203369141,204.0592727661133,204.0592727661133,204.0592727661133,204.0592727661133,204.0592727661133,204.0592727661133,204.0592727661133,204.0592727661133,204.0592727661133,201.430061340332,201.6152496337891,201.6152496337891,201.8081588745117,202.0107955932617,202.0107955932617,202.2315063476562,202.467414855957,202.708122253418,202.708122253418,202.9464645385742,203.1843643188477,203.1843643188477,203.1843643188477,203.4219589233398,203.4219589233398,203.6617126464844,203.9039688110352,203.9039688110352,204.137939453125,204.137939453125,204.137939453125,204.137939453125,204.137939453125,204.137939453125,204.137939453125,204.137939453125,204.137939453125,201.4984588623047,201.4984588623047,201.6767730712891,201.6767730712891,201.8608474731445,202.0604705810547,202.0604705810547,202.2794647216797,202.2794647216797,202.5162506103516,202.7616882324219,202.7616882324219,203.0059356689453,203.2477111816406,203.4884948730469,203.4884948730469,203.7297744750977,203.9738616943359,203.9738616943359,204.2111663818359,204.2111663818359,204.2153396606445,204.2153396606445,204.2153396606445,204.2153396606445,204.2153396606445,204.2153396606445,201.6288757324219,201.6288757324219,201.8102111816406,201.9991455078125,201.9991455078125,202.2016525268555,202.2016525268555,202.4252014160156,202.4252014160156,202.6622085571289,202.906867980957,202.906867980957,203.1464691162109,203.3873596191406,203.3873596191406,203.627197265625,203.627197265625,203.8700561523438,203.8700561523438,204.1120452880859,204.1120452880859,204.2914428710938,204.2914428710938,204.2914428710938,204.2914428710938,204.2914428710938,204.2914428710938,201.7981185913086,201.7981185913086,201.9850006103516,201.9850006103516,201.9850006103516,202.1781463623047,202.3890991210938,202.6121978759766,202.8561096191406,203.100830078125,203.3421249389648,203.3421249389648,203.5830383300781,203.8237915039062,204.0659713745117,204.0659713745117,204.0659713745117,204.3103866577148,204.3103866577148,204.3663787841797,204.3663787841797,204.3663787841797,204.3663787841797,204.3663787841797,204.3663787841797,201.8060073852539,201.9847106933594,201.9847106933594,202.1728973388672,202.3626937866211,202.3626937866211,202.5716857910156,202.5716857910156,202.8006744384766,202.8006744384766,203.04443359375,203.04443359375,203.28955078125,203.28955078125,203.5311737060547,203.5311737060547,203.7719192504883,204.015022277832,204.2585296630859,204.2585296630859,204.4400253295898,204.4400253295898,204.4400253295898,204.4400253295898,204.4400253295898,204.4400253295898,202.0043411254883,202.1817474365234,202.1817474365234,202.3715972900391,202.3715972900391,202.5821304321289,202.5821304321289,202.809196472168,202.809196472168,203.0531616210938,203.300163269043,203.300163269043,203.5421447753906,203.7844924926758,203.7844924926758,204.0271606445312,204.0271606445312,204.2782821655273,204.2782821655273,204.5125503540039,204.5125503540039,204.5125503540039,204.5125503540039,204.5125503540039,204.5125503540039,204.5125503540039,204.5125503540039,204.5125503540039,204.5125503540039,204.5125503540039,204.5125503540039,204.5125503540039,204.5125503540039,204.5125503540039,204.5125503540039,204.5125503540039,204.5125503540039,204.5125503540039,204.5125503540039,204.5125503540039,204.5125503540039,204.5125503540039,204.5125503540039,204.5125503540039,204.5125503540039,204.5125503540039,204.5125503540039,204.5125503540039,204.5125503540039,204.5125503540039,204.5125503540039,204.5125503540039,204.5125503540039,204.5125503540039,204.5125503540039,204.5125503540039,204.5125503540039,204.5125503540039,204.5125503540039,204.5125503540039,204.5125503540039,202.0162124633789,202.0162124633789,202.0162124633789,202.0533065795898,202.2171096801758,202.2171096801758,202.3978500366211,202.3978500366211,202.5901947021484,202.5901947021484,202.5901947021484,202.788459777832,202.788459777832,203.0057678222656,203.2404861450195,203.4849243164062,203.7146377563477,203.7146377563477,203.9507064819336,203.9507064819336,204.1895294189453,204.4360733032227,204.5835800170898,204.5835800170898,204.5835800170898,204.5835800170898,204.5835800170898,204.5835800170898,202.2523193359375,202.2523193359375,202.4369354248047,202.4369354248047,202.6294403076172,202.6294403076172,202.8420944213867,203.0742645263672,203.0742645263672,203.3180541992188,203.562141418457,203.8020172119141,204.0427474975586,204.0427474975586,204.2819366455078,204.2819366455078,204.5235443115234,204.5235443115234,204.6537322998047,204.6537322998047,204.6537322998047,204.6537322998047,204.6537322998047,204.6537322998047,204.6537322998047,204.6537322998047,204.6537322998047,202.3910446166992,202.5780563354492,202.5780563354492,202.5780563354492,202.7744140625,202.7744140625,202.7744140625,202.9872436523438,202.9872436523438,203.2193984985352,203.2193984985352,203.4619750976562,203.7070465087891,203.7070465087891,203.9494400024414,203.9494400024414,204.1928100585938,204.1928100585938,204.4338836669922,204.4338836669922,204.6757354736328,204.6757354736328,204.7228927612305,204.7228927612305,204.7228927612305,204.7228927612305,204.7228927612305,204.7228927612305,202.3773574829102,202.3773574829102,202.3773574829102,202.5422821044922,202.7311019897461,202.7311019897461,202.9322204589844,202.9322204589844,203.1509017944336,203.3880996704102,203.3880996704102,203.3880996704102,203.6314849853516,203.6314849853516,203.6314849853516,203.8754425048828,204.116828918457,204.3584594726562,204.5993881225586,204.5993881225586,204.7908477783203,204.7908477783203,204.7908477783203,204.7908477783203,204.7908477783203,204.7908477783203,204.7908477783203,204.7908477783203,204.7908477783203,202.5635604858398,202.5635604858398,202.7471084594727,202.9403839111328,203.1545867919922,203.1545867919922,203.3849639892578,203.3849639892578,203.6285552978516,203.6285552978516,203.6285552978516,203.8757858276367,203.8757858276367,204.1179504394531,204.1179504394531,204.3625411987305,204.3625411987305,204.6061248779297,204.6061248779297,204.6061248779297,204.8481216430664,204.8481216430664,204.8481216430664,204.8577499389648,204.8577499389648,204.8577499389648,204.8577499389648,204.8577499389648,204.8577499389648,202.6178817749023,202.6178817749023,202.796516418457,202.796516418457,202.9853363037109,202.9853363037109,203.1888656616211,203.4133377075195,203.4133377075195,203.6528472900391,203.6528472900391,203.6528472900391,203.8969116210938,204.139274597168,204.139274597168,204.139274597168,204.3811111450195,204.3811111450195,204.6205749511719,204.6205749511719,204.8620986938477,204.9234924316406,204.9234924316406,204.9234924316406,204.9234924316406,204.9234924316406,204.9234924316406,202.6838302612305,202.6838302612305,202.8604888916016,203.0487976074219,203.0487976074219,203.2484817504883,203.2484817504883,203.4676361083984,203.7048950195312,203.7048950195312,203.9490356445312,204.1941452026367,204.1941452026367,204.4353866577148,204.6772079467773,204.6772079467773,204.9248580932617,204.9248580932617,204.9883117675781,204.9883117675781,204.9883117675781,204.9883117675781,204.9883117675781,204.9883117675781,202.7821502685547,202.9432525634766,202.9432525634766,203.1264572143555,203.1264572143555,203.31689453125,203.5292205810547,203.7587127685547,203.7587127685547,203.9987945556641,203.9987945556641,204.2440414428711,204.2440414428711,204.4851608276367,204.4851608276367,204.7285842895508,204.7285842895508,204.9670257568359,204.9670257568359,205.0519485473633,205.0519485473633,205.0519485473633,205.0519485473633,205.0519485473633,205.0519485473633,205.0519485473633,205.0519485473633,205.0519485473633,203.0260696411133,203.0260696411133,203.2091293334961,203.2091293334961,203.4029769897461,203.4029769897461,203.6163558959961,203.6163558959961,203.8439483642578,203.8439483642578,204.0841979980469,204.0841979980469,204.3274536132812,204.5672607421875,204.5672607421875,204.8058013916016,204.8058013916016,205.0442199707031,205.0442199707031,205.1146087646484,205.1146087646484,205.1146087646484,205.1146087646484,205.1146087646484,205.1146087646484,202.9711761474609,203.1290130615234,203.3171997070312,203.5163345336914,203.5163345336914,203.7378082275391,203.7378082275391,203.9772644042969,203.9772644042969,204.2187881469727,204.4628219604492,204.4628219604492,204.7048568725586,204.9484252929688,205.1763076782227,205.1763076782227,205.1763076782227,205.1763076782227,205.1763076782227,205.1763076782227,205.1763076782227,205.1763076782227,205.1763076782227,203.1229476928711,203.3029479980469,203.3029479980469,203.4949569702148,203.6977462768555,203.6977462768555,203.9124069213867,204.1557922363281,204.4032363891602,204.6498794555664,204.6498794555664,204.8944778442383,205.1392211914062,205.2368927001953,205.2368927001953,205.2368927001953,205.2368927001953,205.2368927001953,205.2368927001953,205.2368927001953,205.2368927001953,205.2368927001953,203.3239593505859,203.3239593505859,203.5101776123047,203.7089157104492,203.9284973144531,203.9284973144531,204.1676483154297,204.1676483154297,204.1676483154297,204.4139938354492,204.4139938354492,204.6611175537109,204.9057083129883,204.9057083129883,205.1503219604492,205.1503219604492,205.2966384887695,205.2966384887695,205.2966384887695,205.2966384887695,205.2966384887695,205.2966384887695,205.2966384887695,205.2966384887695,205.2966384887695,203.3761291503906,203.3761291503906,203.5595703125,203.5595703125,203.7481384277344,203.7481384277344,203.9470138549805,203.9470138549805,204.1639175415039,204.403434753418,204.6493835449219,204.8911895751953,205.1328201293945,205.3553237915039,205.3553237915039,205.3553237915039,205.3553237915039,205.3553237915039,205.3553237915039,203.4013366699219,203.4013366699219,203.5677108764648,203.5677108764648,203.5677108764648,203.7591323852539,203.9645080566406,204.1920852661133,204.1920852661133,204.4341888427734,204.4341888427734,204.6821823120117,204.6821823120117,204.9271011352539,205.169677734375,205.169677734375,205.4107818603516,205.4130630493164,205.4130630493164,205.4130630493164,205.4130630493164,203.4796676635742,203.6442642211914,203.6442642211914,203.8353729248047,203.8353729248047,204.0404891967773,204.0404891967773,204.2668685913086,204.2668685913086,204.5095367431641,204.7572784423828,205.0030136108398,205.0030136108398,205.0030136108398,205.2478332519531,205.4699401855469,205.4699401855469,205.4699401855469,205.4699401855469,205.4699401855469,205.4699401855469,205.4699401855469,205.4699401855469,205.4699401855469,203.5819931030273,203.7616806030273,203.9533157348633,203.9533157348633,204.1628875732422,204.392936706543,204.392936706543,204.6374816894531,204.6374816894531,204.8856201171875,204.8856201171875,205.1300582885742,205.1300582885742,205.3729705810547,205.5258102416992,205.5258102416992,205.5258102416992,205.5258102416992,205.5258102416992,205.5258102416992,205.5258102416992,205.5258102416992,205.5258102416992,205.5258102416992,205.5258102416992,205.5258102416992,205.5258102416992,205.5258102416992,205.5258102416992,205.5258102416992,203.6218490600586,203.6218490600586,203.6218490600586,203.7794799804688,203.9607086181641,203.9607086181641,204.1538696289062,204.1538696289062,204.3602523803711,204.3602523803711,204.5867233276367,204.8101501464844,205.0245819091797,205.242561340332,205.242561340332,205.242561340332,205.4874877929688,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,205.5806121826172,203.6872940063477,203.6872940063477,203.6872940063477,203.6872940063477,203.7217559814453,203.7217559814453,203.9147186279297,204.1211242675781,204.1211242675781,204.3443756103516,204.3443756103516,204.5819931030273,204.5819931030273,204.8285980224609,205.0664901733398,205.2863540649414,205.2863540649414,205.4924926757812,205.4924926757812,205.4924926757812,205.7238159179688,205.963996887207,205.963996887207,206.2063064575195,206.2063064575195,206.4418182373047,206.4418182373047,206.4418182373047,206.6806335449219,206.6806335449219,206.9217376708984,206.9217376708984,207.1637649536133,207.1637649536133,207.4062118530273,207.4062118530273,207.6461639404297,207.846305847168,207.846305847168,208.0437850952148,208.0437850952148,208.242546081543,208.242546081543,208.4400100708008,208.6391296386719,208.6391296386719,208.6391296386719,208.8358154296875,209.0339508056641,209.0339508056641,209.0339508056641,209.2310028076172,209.2310028076172,209.4305267333984,209.4305267333984,209.4305267333984,209.6300201416016,209.8272552490234,210.0264663696289,210.0264663696289,210.2231903076172,210.2231903076172,210.4228515625,210.4228515625,210.4228515625,210.6205825805664,210.8206634521484,210.8206634521484,211.0178604125977,211.0178604125977,211.2173767089844,211.2173767089844,211.4137344360352,211.6122207641602,211.6122207641602,211.7099609375,211.7099609375,211.7099609375,211.7099609375,211.7099609375,211.7099609375,211.7099609375,211.7099609375,211.7099609375,204.0933990478516,204.0933990478516,204.2910614013672,204.5005722045898,204.7294998168945,204.7294998168945,204.9734802246094,205.2152404785156,205.2152404785156,205.4438629150391,205.6579666137695,205.6579666137695,205.6579666137695,205.8960647583008,205.8960647583008,206.1356658935547,206.3770446777344,206.3770446777344,206.622917175293,206.622917175293,206.622917175293,206.8749389648438,207.1255187988281,207.3777389526367,207.6314086914062,207.6314086914062,207.8836822509766,207.8836822509766,208.1349868774414,208.1349868774414,208.3885269165039,208.64208984375,208.64208984375,208.8953170776367,208.8953170776367,209.1499481201172,209.1499481201172,209.1499481201172,209.4020767211914,209.4020767211914,209.6527252197266,209.9027786254883,210.1545181274414,210.4073944091797,210.4073944091797,210.6590576171875,210.6590576171875,210.8978729248047,210.8978729248047,210.8978729248047,211.1291809082031,211.3656768798828,211.3656768798828,211.5841903686523,211.8134384155273,211.9294586181641,211.9294586181641,211.9294586181641,211.9294586181641,211.9294586181641,211.9294586181641,204.4096527099609,204.4096527099609,204.6067581176758,204.6067581176758,204.8155288696289,204.8155288696289,205.0363006591797,205.0363006591797,205.2733612060547,205.2733612060547,205.5095520019531,205.5095520019531,205.7342071533203,205.7342071533203,205.9579467773438,205.9579467773438,206.2011184692383,206.2011184692383,206.2011184692383,206.443603515625,206.443603515625,206.6859893798828,206.6859893798828,206.9283294677734,207.1712951660156,207.4231414794922,207.4231414794922,207.4231414794922,207.6730499267578,207.6730499267578,207.9253845214844,208.1772994995117,208.1772994995117,208.4296493530273,208.4296493530273,208.6830902099609,208.9360733032227,208.9360733032227,209.188232421875,209.188232421875,209.4413223266602,209.4413223266602,209.6938552856445,209.9480438232422,209.9480438232422,210.2023086547852,210.2023086547852,210.4534225463867,210.4534225463867,210.4534225463867,210.7059097290039,210.9591369628906,210.9591369628906,211.2142791748047,211.2142791748047,211.4695816040039,211.4695816040039,211.7110595703125,211.7110595703125,211.7110595703125,211.9502105712891,211.9502105712891,212.1453094482422,212.1453094482422,212.1453094482422,212.1453094482422,212.1453094482422,212.1453094482422,212.1453094482422,212.1453094482422,204.8525161743164,205.0545501708984,205.0545501708984,205.2661285400391,205.2661285400391,205.4912185668945,205.722900390625,205.722900390625,205.722900390625,205.9471588134766,205.9471588134766,206.1749725341797,206.1749725341797,206.4173278808594,206.6578826904297,206.8971862792969,206.8971862792969,207.1365280151367,207.1365280151367,207.3758850097656,207.3758850097656,207.3758850097656,207.6149291992188,207.8573150634766,208.1044769287109,208.1044769287109,208.3569793701172,208.3569793701172,208.3569793701172,208.6082611083984,208.6082611083984,208.6082611083984,208.8609619140625,208.8609619140625,209.1126174926758,209.3653030395508,209.6179580688477,209.6179580688477,209.8704452514648,209.8704452514648,210.1233062744141,210.1233062744141,210.3745727539062,210.3745727539062,210.6256866455078,210.6256866455078,210.8774871826172,210.8774871826172,211.1295166015625,211.1295166015625,211.3815231323242,211.6336288452148,211.6336288452148,211.8805084228516,212.1222686767578,212.3577041625977,212.3577041625977,212.3577041625977,212.3577041625977,212.3577041625977,212.3577041625977,212.3577041625977,212.3577041625977,205.15576171875,205.3575057983398,205.3575057983398,205.5676040649414,205.7916641235352,205.7916641235352,206.0215148925781,206.0215148925781,206.2440643310547,206.4847640991211,206.4847640991211,206.7270812988281,206.7270812988281,206.9687805175781,207.209114074707,207.209114074707,207.4522171020508,207.6946792602539,207.6946792602539,207.6946792602539,207.9385681152344,207.9385681152344,208.1865158081055,208.1865158081055,208.4379959106445,208.4379959106445,208.4379959106445,208.690673828125,208.690673828125,208.9426574707031,208.9426574707031,209.1960525512695,209.1960525512695,209.1960525512695,209.4499664306641,209.4499664306641,209.7033538818359,209.7033538818359,209.7033538818359,209.9554901123047,210.2080688476562,210.4568405151367,210.4568405151367,210.7063522338867,210.7063522338867,210.9550628662109,210.9550628662109,211.2045516967773,211.2045516967773,211.2045516967773,211.4561614990234,211.4561614990234,211.7085189819336,211.7085189819336,211.9594268798828,212.2024765014648,212.2024765014648,212.4429016113281,212.4429016113281,212.566764831543,212.566764831543,212.566764831543,212.566764831543,212.566764831543,212.566764831543,212.566764831543,212.566764831543,212.566764831543,205.3785247802734,205.3785247802734,205.5690231323242,205.7704696655273,205.9813919067383,205.9813919067383,206.1988677978516,206.1988677978516,206.4146728515625,206.4146728515625,206.4146728515625,206.6491470336914,206.8938674926758,206.8938674926758,207.1261978149414,207.3659133911133,207.3659133911133,207.6014022827148,207.6014022827148,207.8414764404297,207.8414764404297,208.0788116455078,208.3102035522461,208.3102035522461,208.5472717285156,208.7844467163086,208.7844467163086,209.0234985351562,209.0234985351562,209.2623977661133,209.5037231445312,209.5037231445312,209.7538452148438,210.0054779052734,210.2547760009766,210.2547760009766,210.5050582885742,210.7555923461914,210.7555923461914,210.7555923461914,211.0075912475586,211.0075912475586,211.0075912475586,211.2589569091797,211.5097885131836,211.5097885131836,211.7621383666992,211.7621383666992,211.7621383666992,212.0074844360352,212.2576675415039,212.2576675415039,212.4932250976562,212.7328491210938,212.7328491210938,212.7723388671875,212.7723388671875,212.7723388671875,212.7723388671875,212.7723388671875,212.7723388671875,212.7723388671875,212.7723388671875,212.7723388671875,212.7723388671875,212.7723388671875,212.7723388671875,212.7723388671875,212.7723388671875,212.7723388671875,212.7723388671875,212.7723388671875,212.7723388671875,212.7723388671875,212.7723388671875,212.7723388671875,212.7723388671875,212.7723388671875,212.7723388671875,212.7723388671875,212.7723388671875,212.7723388671875,205.767936706543,205.767936706543,205.950080871582,205.950080871582,206.1488800048828,206.1488800048828,206.348762512207,206.348762512207,206.5536499023438,206.7637634277344,206.7637634277344,207.0048751831055,207.0048751831055,207.0048751831055,207.2500152587891,207.2500152587891,207.491828918457,207.491828918457,207.7325668334961,207.7325668334961,207.9722518920898,207.9722518920898,208.2135314941406,208.2135314941406,208.455192565918,208.455192565918,208.7073211669922,208.9586715698242,208.9586715698242,209.209602355957,209.209602355957,209.4590606689453,209.4590606689453,209.7065505981445,209.9578323364258,210.210693359375,210.462646484375,210.462646484375,210.7151565551758,210.7151565551758,210.9692230224609,210.9692230224609,211.2245864868164,211.2245864868164,211.4790267944336,211.4790267944336,211.7336349487305,211.7336349487305,211.9892883300781,211.9892883300781,212.2451095581055,212.2451095581055,212.4970779418945,212.4970779418945,212.7401275634766,212.7401275634766,212.9744415283203,212.9744415283203,212.9744415283203,212.9744415283203,212.9744415283203,212.9744415283203,212.9744415283203,212.9744415283203,206.1051712036133,206.1051712036133,206.3003463745117,206.5022659301758,206.5022659301758,206.7075805664062,206.7075805664062,206.7075805664062,206.9135665893555,206.9135665893555,207.1464233398438,207.1464233398438,207.3878784179688,207.3878784179688,207.6256484985352,207.6256484985352,207.8627624511719,207.8627624511719,208.0984497070312,208.334098815918,208.334098815918,208.5715942382812,208.8104858398438,208.8104858398438,209.0502319335938,209.2876586914062,209.5288619995117,209.5288619995117,209.768913269043,209.768913269043,210.0132446289062,210.2558135986328,210.5026321411133,210.5026321411133,210.755615234375,211.0084915161133,211.0084915161133,211.262580871582,211.262580871582,211.515495300293,211.7698822021484,211.7698822021484,212.0241470336914,212.0241470336914,212.2792739868164,212.2792739868164,212.5351181030273,212.5351181030273,212.7822570800781,213.0242156982422,213.0242156982422,213.1735153198242,213.1735153198242,213.1735153198242,213.1735153198242,213.1735153198242,213.1735153198242,213.1735153198242,213.1735153198242,213.1735153198242,213.1735153198242,213.1735153198242,213.1735153198242,206.464469909668,206.6606521606445,206.6606521606445,206.8609237670898,206.8609237670898,207.0602340698242,207.0602340698242,207.2737655639648,207.2737655639648,207.5152435302734,207.5152435302734,207.7610626220703,207.7610626220703,208.0020141601562,208.0020141601562,208.0020141601562,208.2429656982422,208.2429656982422,208.4820938110352,208.4820938110352,208.72216796875,208.72216796875,208.72216796875,208.9593887329102,208.9593887329102,209.1995086669922,209.4432525634766,209.6940612792969,209.9414291381836,210.1897277832031,210.4391784667969,210.6890716552734,210.6890716552734,210.927848815918,211.1682815551758,211.1682815551758,211.4111633300781,211.4111633300781,211.6638488769531,211.6638488769531,211.6638488769531,211.9173889160156,211.9173889160156,212.1707763671875,212.4244003295898,212.4244003295898,212.6763229370117,212.9233932495117,212.9233932495117,213.1647109985352,213.1647109985352,213.3692932128906,213.3692932128906,213.3692932128906,213.3692932128906,213.3692932128906,213.3692932128906,213.3692932128906,213.3692932128906,213.3692932128906,213.3692932128906,213.3692932128906,213.3692932128906,206.7137985229492,206.7137985229492,206.9061660766602,206.9061660766602,207.1030349731445,207.1030349731445,207.2986679077148,207.2986679077148,207.2986679077148,207.5100936889648,207.5100936889648,207.7493362426758,207.9944076538086,207.9944076538086,208.2346343994141,208.4732971191406,208.4732971191406,208.7117691040039,208.7117691040039,208.950927734375,208.950927734375,209.1966171264648,209.1966171264648,209.4441909790039,209.692024230957,209.692024230957,209.9402694702148,209.9402694702148,210.1892623901367,210.4377746582031,210.4377746582031,210.687126159668,210.687126159668,218.3793869018555,218.3793869018555,218.3793869018555,218.3793869018555,218.3793869018555,218.3793869018555,218.3793869018555,218.3793869018555,218.3793869018555,218.3793869018555,218.3793869018555,218.3793869018555,218.3793869018555,218.3793869018555,218.3793869018555,218.3793869018555,218.3793869018555,218.3793869018555,218.3793869018555,218.3793869018555,226.0087814331055,226.0087814331055,226.0087890625,226.0087890625,226.0087890625,226.0087890625,226.0087890625,226.0087890625,226.0087890625,226.0087890625,226.0087890625,226.0087890625,226.0087890625,226.0087890625,226.0087890625,226.0087890625,226.0087890625,226.0087890625,226.0087890625,226.0087890625,226.0087890625,226.0087890625,226.0087890625,226.0087890625,226.0087890625,226.0087890625,241.267578125,241.267578125,241.267578125,241.267578125,241.267578125,241.267578125,241.267578125,241.267578125,241.267578125,241.267578125,241.267578125,241.267578125,241.267578125,241.267578125,241.267578125,241.267578125,241.267578125,241.267578125,241.267578125,241.267578125,241.267578125,241.267578125,241.267578125,241.267578125,241.267578125,241.267578125],"meminc":[0,0,0,0,0,0,0,0,0,0,0,0,15.35334777832031,0,0,0,0,0,15.25894165039062,0,0,0,0,0.0003662109375,0,0,30.2857666015625,0,0,0,0,0,0,0,0,0,0,0,4.57763671875e-05,0,-0.000152587890625,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-0.00018310546875,0,15.2587890625,0.199371337890625,0.1958465576171875,0,0.208099365234375,0.2148056030273438,0,0.2316055297851562,0,0.2423324584960938,0.2493743896484375,0,0.2347640991210938,0.23443603515625,0,0.2345046997070312,0.23699951171875,0,0.232574462890625,0.1195526123046875,0,0,0,-2.566574096679688,0,0.2247848510742188,0,0.2411727905273438,0,0.2545623779296875,0,0.25128173828125,0,0.2507400512695312,0,0.2437896728515625,0,0.24334716796875,0,0.2402267456054688,0,0.238983154296875,0,0.2409515380859375,0,0.1949310302734375,0,0,0,-2.523208618164062,0,0.2153167724609375,0.234893798828125,0,0.247314453125,0.2498092651367188,0,0.2476654052734375,0.2425079345703125,0.238067626953125,0,0.2386322021484375,0,0.2388763427734375,0,0.2400665283203125,0,0.205657958984375,0,0,0,-2.511665344238281,0,0.1998519897460938,0,0.2316055297851562,0,0.2469100952148438,0,0.2495880126953125,0.2452545166015625,0,0.2428665161132812,0,0,0.2399826049804688,0.2388687133789062,0.2374420166015625,0,0.2412567138671875,0.2125244140625,0,0,0,0,0,-2.474395751953125,0,0.2086181640625,0,0.22515869140625,0,0.24090576171875,0,0.2497024536132812,0,0.2448577880859375,0.2447357177734375,0,0.2391738891601562,0,0.2397079467773438,0,0.2404022216796875,0,0.2403945922851562,0,0.173919677734375,0,0,0,0,0,0,0,-2.41387939453125,0,0.2021331787109375,0.2332077026367188,0,0.245513916015625,0,0.2469406127929688,0.241912841796875,0,0.2409439086914062,0,0.2381134033203125,0,0.239044189453125,0,0.239471435546875,0,0.2403030395507812,0.1183700561523438,0,0,0,-2.316703796386719,0.2164382934570312,0.2354354858398438,0,0,0.248870849609375,0.2454376220703125,0,0.2447738647460938,0.2420501708984375,0.241943359375,0,0,0.2403945922851562,0,0,0.2409210205078125,0,0.2312774658203125,0,0,0,0,0,-2.369117736816406,0,0.2069549560546875,0.22576904296875,0,0.2420501708984375,0,0.2420883178710938,0,0.242401123046875,0.2419815063476562,0.2412796020507812,0,0.2420883178710938,0.2394180297851562,0.2408828735351562,0,0,0.07392120361328125,0,-2.398910522460938,0.1788177490234375,0.2240066528320312,0.2405776977539062,0,0.2451400756835938,0,0.243927001953125,0,0.2414398193359375,0.2420501708984375,0.2394561767578125,0.2393722534179688,0,0,0.2403793334960938,0.1323699951171875,0,0,0,0,0,-2.231254577636719,0,0.2077789306640625,0,0.232208251953125,0,0.2401580810546875,0.2413482666015625,0.2387771606445312,0,0.2412872314453125,0,0.2399139404296875,0,0.2396316528320312,0.2389984130859375,0,0.17864990234375,0,0,0,0,0,-2.225990295410156,0.2003250122070312,0,0.229888916015625,0,0.2402420043945312,0,0.2170791625976562,0,0.2099990844726562,0.2113418579101562,0,0.21649169921875,0,0.2395248413085938,0,0,0.2386245727539062,0.2395248413085938,0,0.04932403564453125,0,0,-2.270759582519531,0,0.2051467895507812,0,0.2196578979492188,0,0,0.230072021484375,0,0.2404251098632812,0.2414169311523438,0,0,0.2425003051757812,0,0.2402267456054688,0,0.2398223876953125,0.2380218505859375,0,0.238555908203125,0.00023651123046875,0,0,-2.201026916503906,0,0.18792724609375,0,0.2228240966796875,0,0.2338027954101562,0.2401275634765625,0.2433319091796875,0.2431182861328125,0,0.2430572509765625,0,0.2440872192382812,0,0.2417831420898438,0,0.1651992797851562,0,0,0,-2.109031677246094,0,0.2065582275390625,0,0.2253570556640625,0.2350845336914062,0,0.2409133911132812,0.2441253662109375,0,0.2433700561523438,0,0.24267578125,0,0.24359130859375,0,0.24176025390625,0.04885101318359375,0,-2.167190551757812,0,0.1756820678710938,0.2186279296875,0.226287841796875,0,0.2404022216796875,0,0.243927001953125,0,0.244293212890625,0,0.2417831420898438,0,0.2416839599609375,0.24102783203125,0.1556777954101562,0,0,0,0,0,-2.034927368164062,0.198211669921875,0,0.2184677124023438,0.231109619140625,0,0.2413406372070312,0,0.2422637939453125,0.2423324584960938,0,0.2423858642578125,0,0.2393646240234375,0.2368240356445312,0,0.0038604736328125,0,0,-2.085479736328125,0,0.2021255493164062,0,0.2046356201171875,0,0.2175674438476562,0,0,0.2344512939453125,0,0.2435226440429688,0.2428970336914062,0,0.241119384765625,0,0.2414016723632812,0,0.2379684448242188,0,0.07999420166015625,0,0,0,0,0,-1.916709899902344,0.2079391479492188,0.2149734497070312,0,0.2341384887695312,0.242828369140625,0,0,0.24334716796875,0,0.2439346313476562,0,0,0.2414932250976562,0,0.240234375,0,0.1070404052734375,0,0,0,-1.906852722167969,0,0.1967239379882812,0,0.2153091430664062,0,0.2314376831054688,0,0.2434234619140625,0,0.2445755004882812,0,0.2434005737304688,0,0.2444839477539062,0,0.2421188354492188,0,0.1037216186523438,0,0,0,0,0,-1.854202270507812,0,0.1993484497070312,0.213653564453125,0.2313461303710938,0.2437362670898438,0,0.2451400756835938,0.2451934814453125,0.2434768676757812,0,0.2402572631835938,0.04943084716796875,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.883705139160156,0,0.1798858642578125,0,0.1868438720703125,0,0.200286865234375,0.218109130859375,0,0.2293624877929688,0.2450637817382812,0.2388229370117188,0,0.242401123046875,0,0.1991195678710938,0,0,0,0,0,-1.880104064941406,0,0.1805877685546875,0.207061767578125,0.2230224609375,0,0.2387619018554688,0,0.2430572509765625,0,0,0.246063232421875,0.2429656982421875,0.2430801391601562,0,0.111053466796875,0,0,0,0,0,-1.789375305175781,0.1898269653320312,0,0.2129898071289062,0,0.2300491333007812,0,0.2432785034179688,0.2452011108398438,0.2468338012695312,0.2440872192382812,0,0.23175048828125,0,0,0,0,0,-1.840293884277344,0,0.17529296875,0,0.205230712890625,0.2234420776367188,0,0.2416915893554688,0.2451400756835938,0.2461929321289062,0,0.2433853149414062,0.2461471557617188,0,0.0675506591796875,0,0,0,0,0,-1.699752807617188,0,0.19427490234375,0,0,0.2187957763671875,0,0.236541748046875,0,0.2449798583984375,0,0.2465972900390625,0.2460174560546875,0.2452621459960938,0,0.1201400756835938,0,0,0,-1.708175659179688,0,0.1868515014648438,0,0.2126922607421875,0,0.2297210693359375,0,0.24053955078125,0,0.2444534301757812,0,0.2460708618164062,0,0.2415847778320312,0,0.1583099365234375,0,0,0,0,0,-1.706977844238281,0.1887130737304688,0,0.2093582153320312,0,0.2273941040039062,0,0.2424697875976562,0,0.2446365356445312,0,0,0.2464141845703125,0.2426300048828125,0,0.156585693359375,0,0,0,-1.682685852050781,0.1787109375,0.2096176147460938,0.2276153564453125,0,0,0.2442398071289062,0,0.2441558837890625,0.2489547729492188,0,0.2441329956054688,0.1356353759765625,0,0,0,0,0,-1.628608703613281,0.1890335083007812,0,0.2099380493164062,0.2274169921875,0,0.243682861328125,0,0.2447738647460938,0,0.2465667724609375,0,0.2415008544921875,0.07523345947265625,0,0,0,0,0,0,0,-1.5740966796875,0,0.186126708984375,0,0.2114334106445312,0,0.2319793701171875,0.2436065673828125,0,0.2451095581054688,0,0.2467041015625,0,0.2360305786132812,0,0.0218658447265625,0,-1.676231384277344,0,0.1642684936523438,0,0.194580078125,0,0.216888427734375,0,0.2359161376953125,0.2449188232421875,0,0,0.2469940185546875,0.24700927734375,0.1736526489257812,0,0,0,-1.588241577148438,0,0.17510986328125,0.2065582275390625,0,0,0.2274169921875,0,0,0.24383544921875,0.2468032836914062,0,0,0.246337890625,0,0.2393951416015625,0,0.04998016357421875,0,0,0,0,0,-1.469993591308594,0,0.1969223022460938,0,0,0.2211151123046875,0,0.23760986328125,0.2455978393554688,0.2478256225585938,0,0.2461395263671875,0,0.1212692260742188,0,0,0,0,0,-1.485557556152344,0.186004638671875,0,0.2099075317382812,0,0,0.2311172485351562,0,0.246490478515625,0,0.2473068237304688,0,0.2457962036132812,0,0.1645965576171875,0,0,0,0,0,-1.500289916992188,0.1744842529296875,0,0.2061920166015625,0,0,0.2260055541992188,0,0.2404632568359375,0.2438888549804688,0,0.244354248046875,0.2098464965820312,0,0,0,-1.518096923828125,0,0.18719482421875,0,0.195831298828125,0,0.2209243774414062,0,0.238494873046875,0,0,0.2451171875,0,0.2479476928710938,0,0.2267837524414062,0,0,0,-1.490829467773438,0,0.187774658203125,0,0.2020034790039062,0,0.2241058349609375,0.2425079345703125,0,0.2482833862304688,0,0.2487869262695312,0,0.1809234619140625,0,0,0,0,0,-1.440933227539062,0,0,0.1742095947265625,0,0.2064361572265625,0.2288131713867188,0.2455978393554688,0,0.2479629516601562,0,0.24835205078125,0.1323089599609375,0,0,0,-1.371360778808594,0,0,0.1940460205078125,0,0.2135543823242188,0,0.2350082397460938,0,0.2440414428710938,0.245513916015625,0,0,0.2426605224609375,0,0.0386505126953125,0,0,0,0,0,-1.293968200683594,0,0.1936569213867188,0.2197723388671875,0.240692138671875,0,0.2470550537109375,0,0.247314453125,0,0.1868820190429688,0,0,0,-1.378173828125,0.1613845825195312,0,0.1721267700195312,0,0.204803466796875,0,0,0.2249603271484375,0,0,0.2457122802734375,0.2514114379882812,0,0.15850830078125,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.403526306152344,0,0,0,0.04396820068359375,0,0.2007598876953125,0,0.2086257934570312,0,0.2250137329101562,0,0.2403488159179688,0,0.2248611450195312,0.2210235595703125,0.2421722412109375,0,0.237945556640625,0,0.236541748046875,0,0.24554443359375,0.2375335693359375,0,0.1982803344726562,0,0.1995162963867188,0.1981887817382812,0.2006912231445312,0,0,0.19775390625,0,0.2002029418945312,0,0.2002182006835938,0,0.1977615356445312,0.2002792358398438,0,0.1968231201171875,0.1993408203125,0,0.1983566284179688,0.1303253173828125,0,0,0,0,0,-4.817657470703125,0,0.2035903930664062,0.2362899780273438,0,0.2495956420898438,0.2389297485351562,0.221466064453125,0,0.2443161010742188,0.2430191040039062,0,0.2423324584960938,0,0.2486190795898438,0,0,0.25238037109375,0.2541961669921875,0,0.25408935546875,0,0.2529220581054688,0,0.2538681030273438,0,0.2525634765625,0.253143310546875,0,0.2528839111328125,0,0.251678466796875,0.2461395263671875,0,0.2388839721679688,0.06572723388671875,0,0,0,-4.667564392089844,0,0,0.204742431640625,0.2357330322265625,0.243316650390625,0.2274551391601562,0,0.2366943359375,0,0.247406005859375,0.243408203125,0,0.243011474609375,0,0.2417068481445312,0.2505035400390625,0.2524032592773438,0.2529830932617188,0,0.2517929077148438,0,0.2522354125976562,0.2528533935546875,0.2522659301757812,0,0.2530517578125,0,0.2525634765625,0.2412567138671875,0,0.1689529418945312,0,0,0,0,0,-4.680900573730469,0.181610107421875,0,0.2215652465820312,0,0.2342605590820312,0,0.2254867553710938,0,0.22882080078125,0.2432785034179688,0.23895263671875,0,0.23809814453125,0.2358627319335938,0,0.2406463623046875,0.2429428100585938,0,0.2502975463867188,0.2489471435546875,0,0.25091552734375,0.2513504028320312,0.2513885498046875,0,0.2518234252929688,0,0.2530441284179688,0,0.2478179931640625,0.2368392944335938,0,0.041473388671875,0,0,0,-4.514366149902344,0,0.200897216796875,0,0.2293472290039062,0,0.2277908325195312,0,0.228973388671875,0.2458419799804688,0,0.2457199096679688,0,0.2412261962890625,0,0.2409591674804688,0,0,0.2418289184570312,0,0.2424545288085938,0.2448043823242188,0,0.2514419555664062,0.2515029907226562,0,0.2514266967773438,0,0.2516326904296875,0,0.2525100708007812,0,0.2528457641601562,0,0.248138427734375,0,0.238983154296875,0.05846405029296875,0,0,0,0,0,-4.454177856445312,0,0.1995468139648438,0,0.22509765625,0,0.2188034057617188,0,0.231475830078125,0,0,0.2420120239257812,0,0.2428054809570312,0,0.2395401000976562,0,0.2391586303710938,0,0.2370681762695312,0,0.2382965087890625,0,0.2372589111328125,0,0.2404022216796875,0,0.2390213012695312,0,0.2466964721679688,0,0.2499008178710938,0,0.2507858276367188,0.2507171630859375,0,0,0.2493209838867188,0,0.2395248413085938,0.0670013427734375,0,0,0,-4.393943786621094,0,0.1949691772460938,0,0,0.2177581787109375,0,0,0.2156982421875,0,0.2376251220703125,0.2444076538085938,0,0.244293212890625,0.2395782470703125,0.2397689819335938,0,0.2375946044921875,0,0,0.240966796875,0.2405014038085938,0,0.23907470703125,0.2473602294921875,0,0.249176025390625,0,0.2495269775390625,0,0.2525100708007812,0,0.2517929077148438,0,0.2445068359375,0.23492431640625,0,0,0,0,0,0,0,0,-4.2412109375,0,0.2125091552734375,0,0,0.2103729248046875,0,0.2202224731445312,0.2322311401367188,0.2422103881835938,0.2360610961914062,0,0.2364883422851562,0.2353668212890625,0,0.2361907958984375,0.2365646362304688,0,0.2412948608398438,0,0.2421875,0,0.2389984130859375,0.2420883178710938,0.2472763061523438,0,0,0.2518463134765625,0.2511062622070312,0.2360000610351562,0,0.1182937622070312,0,0,0,-4.287933349609375,0,0.2046051025390625,0.2083587646484375,0.2105178833007812,0,0.2386703491210938,0,0.2442245483398438,0.2416458129882812,0,0.2381820678710938,0.237884521484375,0,0.2353668212890625,0.237945556640625,0.2382965087890625,0,0.23980712890625,0,0.2423782348632812,0,0.2514266967773438,0,0.2525634765625,0.2523345947265625,0.2533187866210938,0,0.2413482666015625,0,0.1431350708007812,0,0,0,0,0,-4.244171142578125,0,0.2035598754882812,0,0,0.2010879516601562,0,0.2058944702148438,0.2350616455078125,0,0.2416534423828125,0,0.2416229248046875,0,0.2364120483398438,0,0.2363204956054688,0,0.2342605590820312,0,0.2352981567382812,0,0.2416915893554688,0,0.2415847778320312,0,0.24249267578125,0,0.2436294555664062,0.2514572143554688,0.2521133422851562,0,0.2526626586914062,0.2420501708984375,0,0.1273422241210938,0,0,0,0,0,-4.161231994628906,0.2004165649414062,0,0.1975784301757812,0,0.2091751098632812,0,0.236236572265625,0.24212646484375,0,0.2421875,0.2385787963867188,0.2376327514648438,0,0,0.2353439331054688,0.2373504638671875,0,0.2411575317382812,0,0.2398910522460938,0.2461624145507812,0,0.2487869262695312,0,0.2508316040039062,0.2523269653320312,0.2461929321289062,0.2395248413085938,0.0397796630859375,0,0,0,0,0,-4.024810791015625,0,0.1955413818359375,0,0.1974716186523438,0.2266616821289062,0,0.2385330200195312,0.240447998046875,0.2402267456054688,0.2372589111328125,0,0.2363967895507812,0,0.2367401123046875,0.23980712890625,0,0.2402420043945312,0,0.2405624389648438,0.2414093017578125,0.2501144409179688,0,0.25323486328125,0,0.2540740966796875,0,0.2423477172851562,0,0.1319198608398438,0,0,0,-4.032173156738281,0,0.1962203979492188,0,0.1925277709960938,0,0.216644287109375,0.2279434204101562,0.2102890014648438,0.2084197998046875,0,0,0.2273941040039062,0,0.2337875366210938,0,0.2335281372070312,0,0.2319793701171875,0,0.2346038818359375,0,0.237823486328125,0.235595703125,0,0.2389984130859375,0,0.2483367919921875,0,0.2497329711914062,0,0.24822998046875,0,0.2377853393554688,0,0.03849029541015625,0,0,0,-3.893463134765625,0.1909561157226562,0,0.1999588012695312,0.2234420776367188,0,0.2379302978515625,0,0.2393875122070312,0,0,0.2387847900390625,0,0.2360382080078125,0,0.2370452880859375,0.2363662719726562,0,0.2375946044921875,0,0.2397003173828125,0,0.2476119995117188,0,0.2518310546875,0,0,0.2528228759765625,0.2527008056640625,0,0.24810791015625,0,0.23760986328125,0,0,0,0,0,0,0,0,-3.813812255859375,0.1887130737304688,0.2047271728515625,0,0.2173919677734375,0,0.22882080078125,0,0.23443603515625,0,0.2362213134765625,0,0.232666015625,0,0.23583984375,0,0.235443115234375,0.235870361328125,0,0.2367172241210938,0.2390670776367188,0,0.239349365234375,0.245086669921875,0,0.249908447265625,0,0.2456207275390625,0,0.2204132080078125,0,0,0,0,0,0,0,0,-3.74591064453125,0.1860733032226562,0,0.204254150390625,0,0.2209014892578125,0,0.2328414916992188,0,0.2367172241210938,0,0.2412796020507812,0,0.238861083984375,0,0,0.2382583618164062,0.2367172241210938,0.2386627197265625,0,0.2402496337890625,0,0.2414169311523438,0,0.2468948364257812,0,0.2507553100585938,0.251983642578125,0,0.241119384765625,0,0.1095733642578125,0,0,0,-3.777885437011719,0.1865463256835938,0,0.1925048828125,0,0.2142486572265625,0,0.2247695922851562,0,0.2357940673828125,0.2374649047851562,0,0.23760986328125,0,0.2360305786132812,0,0,0.2356338500976562,0,0.2355117797851562,0,0,0.2368850708007812,0,0.2384567260742188,0,0.2423477172851562,0,0.2521743774414062,0,0.2525482177734375,0.2464752197265625,0,0.1818084716796875,0,0,0,0,0,0,0,0,-3.581405639648438,0.1879806518554688,0,0.2070159912109375,0,0.2188568115234375,0,0.2289657592773438,0,0.23675537109375,0,0.2377471923828125,0,0.2339096069335938,0,0.236358642578125,0,0.2351226806640625,0,0.2369155883789062,0,0,0.23809814453125,0.2305755615234375,0.2353134155273438,0,0.2373123168945312,0.23724365234375,0,0.2287521362304688,0.02159881591796875,0,0,0,0,0,-3.590721130371094,0,0.1841506958007812,0.197509765625,0,0.211639404296875,0,0.223541259765625,0,0.2365646362304688,0,0.240203857421875,0.2383193969726562,0,0.2393951416015625,0.2375259399414062,0,0.239013671875,0,0.2400360107421875,0,0.24005126953125,0,0.2509994506835938,0.25299072265625,0,0,0.2488021850585938,0,0.2153549194335938,0,0,0,0,0,0,0,0,-3.50189208984375,0,0.187408447265625,0.1998825073242188,0,0.2087478637695312,0.2219467163085938,0.236297607421875,0,0.2397003173828125,0,0.23162841796875,0,0,0.234954833984375,0,0.233612060546875,0.2340545654296875,0,0.2335433959960938,0,0,0.2398529052734375,0,0.2397003173828125,0,0.2402496337890625,0,0.2413101196289062,0,0.182708740234375,0,0,0,0,0,-3.426216125488281,0,0.1856613159179688,0,0.193389892578125,0,0.2037582397460938,0.2179336547851562,0,0.2282333374023438,0,0.2339324951171875,0,0.234954833984375,0,0.2356491088867188,0.23443603515625,0.2381210327148438,0.238311767578125,0,0.2395095825195312,0.2448654174804688,0.2535552978515625,0,0.24261474609375,0.1033706665039062,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-3.470352172851562,0,0.1477508544921875,0,0,0.17633056640625,0,0.1856536865234375,0.1881484985351562,0,0.2042160034179688,0.21759033203125,0,0.2274856567382812,0.235595703125,0,0.2329254150390625,0.2343902587890625,0,0,0.2365188598632812,0.2385406494140625,0.2419357299804688,0,0.2505569458007812,0.2504043579101562,0,0.2361907958984375,0.0661773681640625,0,0,0,0,0,-3.421134948730469,0.1726226806640625,0,0.18896484375,0,0.1575775146484375,0.1630706787109375,0,0.2175521850585938,0,0.231964111328125,0,0.2405776977539062,0,0.2384719848632812,0,0.240447998046875,0,0.23809814453125,0,0,0.2419586181640625,0.2412796020507812,0,0.2419815063476562,0,0.2536239624023438,0,0.2514114379882812,0,0.2003936767578125,0,0,0,0,0,0,0,0,-3.272270202636719,0,0.1880950927734375,0,0.1956710815429688,0,0.21075439453125,0,0.2249069213867188,0.2400970458984375,0,0.243438720703125,0.2401580810546875,0.2411270141601562,0,0.2397232055664062,0,0.24127197265625,0,0,0.2430572509765625,0,0.2463760375976562,0.2556610107421875,0,0.2452774047851562,0,0,0.1138153076171875,0,0,0,-3.328033447265625,0,0.1753005981445312,0,0.186004638671875,0,0.1955490112304688,0.197357177734375,0,0.2222061157226562,0,0.2375717163085938,0,0.2393722534179688,0.2381134033203125,0,0.2393112182617188,0,0,0.238800048828125,0.2414703369140625,0,0.2478103637695312,0,0.2535781860351562,0,0.2544403076171875,0.2412490844726562,0,0,0.015594482421875,0,0,0,0,0,-3.218666076660156,0,0.1825637817382812,0.1907424926757812,0.2068862915039062,0.2233123779296875,0,0.24005126953125,0,0.2426834106445312,0.2404022216796875,0.2386627197265625,0,0.2369155883789062,0,0.2398605346679688,0,0,0.248138427734375,0,0.2535400390625,0,0.2538986206054688,0,0.2449188232421875,0.0702056884765625,0,0,0,-3.198326110839844,0,0.1790313720703125,0,0.187225341796875,0,0.20123291015625,0.2167510986328125,0,0.23211669921875,0.2389984130859375,0,0.2397003173828125,0,0.2373199462890625,0.2401809692382812,0,0.2400894165039062,0.2412109375,0.2432479858398438,0,0.2514190673828125,0,0.2465438842773438,0,0.0958251953125,0,0,0,0,0,-3.159744262695312,0,0.182373046875,0,0.1877059936523438,0,0.2008056640625,0,0.2155990600585938,0,0.2341232299804688,0,0.2434158325195312,0.2429122924804688,0.2403488159179688,0.2414093017578125,0,0,0.2451171875,0,0.252227783203125,0.2547378540039062,0,0.2547836303710938,0,0.2379531860351562,0,0.01737213134765625,0,0,0,0,0,-3.061561584472656,0.1804580688476562,0,0,0.1906204223632812,0.2066574096679688,0,0.2212905883789062,0,0.238616943359375,0,0.2419891357421875,0,0.2414779663085938,0,0.2397308349609375,0.23992919921875,0.2412338256835938,0.2426223754882812,0,0.2491607666015625,0,0.2491912841796875,0,0.1681365966796875,0,0,0,0,0,0,0,0,-2.944381713867188,0,0.184814453125,0,0.1937255859375,0,0.2096710205078125,0,0.222137451171875,0,0.2403488159179688,0.242034912109375,0.2400665283203125,0,0.2414398193359375,0,0.2395248413085938,0,0.24285888671875,0,0.242706298828125,0,0.2445907592773438,0,0.2448577880859375,0.04381561279296875,0,0,0,0,0,-2.989173889160156,0,0.1723403930664062,0,0,0.1863861083984375,0.2006759643554688,0,0.2170639038085938,0,0.2366714477539062,0.2413406372070312,0,0.2411651611328125,0.2385711669921875,0,0.2381210327148438,0,0.2406005859375,0,0.241607666015625,0,0.2448654174804688,0.24835205078125,0.128143310546875,0,0,0,-2.984062194824219,0.1783065795898438,0,0.1854629516601562,0,0.1986312866210938,0.2172622680664062,0,0,0.2337112426757812,0,0.2414779663085938,0,0,0.2350311279296875,0.2101287841796875,0,0.23046875,0.2520904541015625,0.252777099609375,0.25384521484375,0,0.2495193481445312,0,0.130615234375,0,0,0,0,0,-2.7818603515625,0,0.1861648559570312,0,0.196533203125,0,0.2155532836914062,0.2335586547851562,0.2440185546875,0.2459716796875,0.2434463500976562,0,0.2432098388671875,0,0.2411041259765625,0,0.2444381713867188,0,0.2451629638671875,0,0.2467498779296875,0,0.0799713134765625,0,0,0,0,0,-2.864532470703125,0.180267333984375,0,0.1876068115234375,0,0.1981582641601562,0,0.2170562744140625,0,0.2344207763671875,0,0.2426910400390625,0,0.2431793212890625,0,0.23846435546875,0,0.2376708984375,0.2400283813476562,0.2406845092773438,0,0.242889404296875,0,0.2391586303710938,0,0.0048980712890625,0,0,0,-2.763900756835938,0,0.1791763305664062,0,0.1870040893554688,0,0.2042083740234375,0.2216262817382812,0.2399215698242188,0,0.2415237426757812,0.2392807006835938,0,0.2394027709960938,0,0.2384567260742188,0,0.2407379150390625,0,0,0.2444305419921875,0,0.248992919921875,0,0.1203842163085938,0,0,0,0,0,0,0,0,-2.619232177734375,0,0.1870803833007812,0,0,0.1968612670898438,0.2143325805664062,0.2330245971679688,0.2449111938476562,0,0.246002197265625,0,0.242889404296875,0,0,0.2417755126953125,0.2416305541992188,0.2480010986328125,0,0.2411270141601562,0.1615524291992188,0,0,0,0,0,0,0,0,-2.62921142578125,0.1851882934570312,0,0.1929092407226562,0.20263671875,0,0.2207107543945312,0.2359085083007812,0.2407073974609375,0,0.23834228515625,0.2378997802734375,0,0,0.2375946044921875,0,0.2397537231445312,0.2422561645507812,0,0.2339706420898438,0,0,0,0,0,0,0,0,-2.639480590820312,0,0.178314208984375,0,0.1840744018554688,0.1996231079101562,0,0.218994140625,0,0.236785888671875,0.2454376220703125,0,0.2442474365234375,0.2417755126953125,0.24078369140625,0,0.2412796020507812,0.2440872192382812,0,0.2373046875,0,0.00417327880859375,0,0,0,0,0,-2.586463928222656,0,0.18133544921875,0.188934326171875,0,0.2025070190429688,0,0.2235488891601562,0,0.2370071411132812,0.244659423828125,0,0.2396011352539062,0.2408905029296875,0,0.239837646484375,0,0.24285888671875,0,0.2419891357421875,0,0.1793975830078125,0,0,0,0,0,-2.493324279785156,0,0.1868820190429688,0,0,0.193145751953125,0.2109527587890625,0.2230987548828125,0.2439117431640625,0.244720458984375,0.2412948608398438,0,0.2409133911132812,0.240753173828125,0.2421798706054688,0,0,0.244415283203125,0,0.05599212646484375,0,0,0,0,0,-2.560371398925781,0.1787033081054688,0,0.1881866455078125,0.1897964477539062,0,0.2089920043945312,0,0.2289886474609375,0,0.2437591552734375,0,0.2451171875,0,0.2416229248046875,0,0.2407455444335938,0.24310302734375,0.2435073852539062,0,0.1814956665039062,0,0,0,0,0,-2.435684204101562,0.1774063110351562,0,0.189849853515625,0,0.2105331420898438,0,0.2270660400390625,0,0.2439651489257812,0.2470016479492188,0,0.2419815063476562,0.2423477172851562,0,0.2426681518554688,0,0.2511215209960938,0,0.2342681884765625,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2.496337890625,0,0,0.0370941162109375,0.1638031005859375,0,0.1807403564453125,0,0.1923446655273438,0,0,0.1982650756835938,0,0.2173080444335938,0.2347183227539062,0.2444381713867188,0.2297134399414062,0,0.2360687255859375,0,0.2388229370117188,0.2465438842773438,0.1475067138671875,0,0,0,0,0,-2.331260681152344,0,0.1846160888671875,0,0.1925048828125,0,0.2126541137695312,0.2321701049804688,0,0.2437896728515625,0.2440872192382812,0.2398757934570312,0.2407302856445312,0,0.2391891479492188,0,0.241607666015625,0,0.13018798828125,0,0,0,0,0,0,0,0,-2.262687683105469,0.18701171875,0,0,0.1963577270507812,0,0,0.21282958984375,0,0.2321548461914062,0,0.2425765991210938,0.2450714111328125,0,0.2423934936523438,0,0.2433700561523438,0,0.2410736083984375,0,0.241851806640625,0,0.04715728759765625,0,0,0,0,0,-2.345535278320312,0,0,0.1649246215820312,0.1888198852539062,0,0.2011184692382812,0,0.2186813354492188,0.2371978759765625,0,0,0.2433853149414062,0,0,0.24395751953125,0.2413864135742188,0.2416305541992188,0.2409286499023438,0,0.1914596557617188,0,0,0,0,0,0,0,0,-2.227287292480469,0,0.1835479736328125,0.1932754516601562,0.214202880859375,0,0.230377197265625,0,0.24359130859375,0,0,0.2472305297851562,0,0.2421646118164062,0,0.2445907592773438,0,0.2435836791992188,0,0,0.2419967651367188,0,0,0.0096282958984375,0,0,0,0,0,-2.2398681640625,0,0.1786346435546875,0,0.1888198852539062,0,0.2035293579101562,0.2244720458984375,0,0.2395095825195312,0,0,0.2440643310546875,0.2423629760742188,0,0,0.2418365478515625,0,0.2394638061523438,0,0.2415237426757812,0.06139373779296875,0,0,0,0,0,-2.239662170410156,0,0.1766586303710938,0.1883087158203125,0,0.1996841430664062,0,0.2191543579101562,0.2372589111328125,0,0.244140625,0.2451095581054688,0,0.241241455078125,0.2418212890625,0,0.247650146484375,0,0.06345367431640625,0,0,0,0,0,-2.206161499023438,0.161102294921875,0,0.1832046508789062,0,0.1904373168945312,0.2123260498046875,0.2294921875,0,0.240081787109375,0,0.2452468872070312,0,0.241119384765625,0,0.2434234619140625,0,0.2384414672851562,0,0.08492279052734375,0,0,0,0,0,0,0,0,-2.02587890625,0,0.1830596923828125,0,0.19384765625,0,0.21337890625,0,0.2275924682617188,0,0.2402496337890625,0,0.243255615234375,0.23980712890625,0,0.2385406494140625,0,0.2384185791015625,0,0.0703887939453125,0,0,0,0,0,-2.1434326171875,0.1578369140625,0.1881866455078125,0.1991348266601562,0,0.2214736938476562,0,0.2394561767578125,0,0.2415237426757812,0.2440338134765625,0,0.242034912109375,0.2435684204101562,0.2278823852539062,0,0,0,0,0,0,0,0,-2.053359985351562,0.1800003051757812,0,0.1920089721679688,0.202789306640625,0,0.21466064453125,0.2433853149414062,0.2474441528320312,0.24664306640625,0,0.244598388671875,0.2447433471679688,0.0976715087890625,0,0,0,0,0,0,0,0,-1.912933349609375,0,0.18621826171875,0.1987380981445312,0.2195816040039062,0,0.2391510009765625,0,0,0.2463455200195312,0,0.2471237182617188,0.2445907592773438,0,0.2446136474609375,0,0.1463165283203125,0,0,0,0,0,0,0,0,-1.920509338378906,0,0.183441162109375,0,0.188568115234375,0,0.1988754272460938,0,0.2169036865234375,0.2395172119140625,0.2459487915039062,0.2418060302734375,0.2416305541992188,0.222503662109375,0,0,0,0,0,-1.953987121582031,0,0.1663742065429688,0,0,0.1914215087890625,0.2053756713867188,0.2275772094726562,0,0.2421035766601562,0,0.2479934692382812,0,0.2449188232421875,0.2425765991210938,0,0.2411041259765625,0.00228118896484375,0,0,0,-1.933395385742188,0.1645965576171875,0,0.1911087036132812,0,0.2051162719726562,0,0.22637939453125,0,0.2426681518554688,0.24774169921875,0.2457351684570312,0,0,0.2448196411132812,0.22210693359375,0,0,0,0,0,0,0,0,-1.887947082519531,0.1796875,0.1916351318359375,0,0.2095718383789062,0.2300491333007812,0,0.2445449829101562,0,0.248138427734375,0,0.2444381713867188,0,0.2429122924804688,0.1528396606445312,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.903961181640625,0,0,0.1576309204101562,0.1812286376953125,0,0.1931610107421875,0,0.2063827514648438,0,0.226470947265625,0.2234268188476562,0.2144317626953125,0.2179794311523438,0,0,0.2449264526367188,0.0931243896484375,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.893318176269531,0,0,0,0.03446197509765625,0,0.192962646484375,0.2064056396484375,0,0.2232513427734375,0,0.2376174926757812,0,0.2466049194335938,0.2378921508789062,0.2198638916015625,0,0.2061386108398438,0,0,0.2313232421875,0.2401809692382812,0,0.2423095703125,0,0.2355117797851562,0,0,0.2388153076171875,0,0.2411041259765625,0,0.2420272827148438,0,0.2424468994140625,0,0.2399520874023438,0.2001419067382812,0,0.197479248046875,0,0.198760986328125,0,0.1974639892578125,0.1991195678710938,0,0,0.196685791015625,0.1981353759765625,0,0,0.197052001953125,0,0.19952392578125,0,0,0.199493408203125,0.197235107421875,0.1992111206054688,0,0.1967239379882812,0,0.1996612548828125,0,0,0.1977310180664062,0.2000808715820312,0,0.1971969604492188,0,0.1995162963867188,0,0.1963577270507812,0.198486328125,0,0.09774017333984375,0,0,0,0,0,0,0,0,-7.616561889648438,0,0.197662353515625,0.2095108032226562,0.2289276123046875,0,0.2439804077148438,0.24176025390625,0,0.2286224365234375,0.2141036987304688,0,0,0.23809814453125,0,0.2396011352539062,0.2413787841796875,0,0.2458724975585938,0,0,0.2520217895507812,0.250579833984375,0.2522201538085938,0.2536697387695312,0,0.2522735595703125,0,0.2513046264648438,0,0.2535400390625,0.2535629272460938,0,0.2532272338867188,0,0.2546310424804688,0,0,0.2521286010742188,0,0.2506484985351562,0.2500534057617188,0.251739501953125,0.2528762817382812,0,0.2516632080078125,0,0.2388153076171875,0,0,0.2313079833984375,0.2364959716796875,0,0.2185134887695312,0.229248046875,0.1160202026367188,0,0,0,0,0,-7.519805908203125,0,0.1971054077148438,0,0.208770751953125,0,0.2207717895507812,0,0.237060546875,0,0.2361907958984375,0,0.2246551513671875,0,0.2237396240234375,0,0.2431716918945312,0,0,0.2424850463867188,0,0.2423858642578125,0,0.242340087890625,0.2429656982421875,0.2518463134765625,0,0,0.249908447265625,0,0.2523345947265625,0.2519149780273438,0,0.252349853515625,0,0.2534408569335938,0.2529830932617188,0,0.2521591186523438,0,0.2530899047851562,0,0.252532958984375,0.2541885375976562,0,0.2542648315429688,0,0.2511138916015625,0,0,0.2524871826171875,0.2532272338867188,0,0.2551422119140625,0,0.2553024291992188,0,0.2414779663085938,0,0,0.2391510009765625,0,0.195098876953125,0,0,0,0,0,0,0,-7.292793273925781,0.2020339965820312,0,0.211578369140625,0,0.2250900268554688,0.2316818237304688,0,0,0.2242584228515625,0,0.227813720703125,0,0.2423553466796875,0.2405548095703125,0.2393035888671875,0,0.2393417358398438,0,0.2393569946289062,0,0,0.239044189453125,0.2423858642578125,0.247161865234375,0,0.25250244140625,0,0,0.25128173828125,0,0,0.2527008056640625,0,0.2516555786132812,0.252685546875,0.252655029296875,0,0.2524871826171875,0,0.2528610229492188,0,0.2512664794921875,0,0.2511138916015625,0,0.251800537109375,0,0.2520294189453125,0,0.2520065307617188,0.252105712890625,0,0.2468795776367188,0.24176025390625,0.2354354858398438,0,0,0,0,0,0,0,-7.201942443847656,0.2017440795898438,0,0.2100982666015625,0.22406005859375,0,0.2298507690429688,0,0.2225494384765625,0.2406997680664062,0,0.2423171997070312,0,0.24169921875,0.2403335571289062,0,0.24310302734375,0.242462158203125,0,0,0.2438888549804688,0,0.2479476928710938,0,0.2514801025390625,0,0,0.2526779174804688,0,0.251983642578125,0,0.2533950805664062,0,0,0.2539138793945312,0,0.253387451171875,0,0,0.25213623046875,0.2525787353515625,0.2487716674804688,0,0.24951171875,0,0.2487106323242188,0,0.2494888305664062,0,0,0.2516098022460938,0,0.2523574829101562,0,0.2509078979492188,0.2430496215820312,0,0.2404251098632812,0,0.1238632202148438,0,0,0,0,0,0,0,0,-7.188240051269531,0,0.1904983520507812,0.201446533203125,0.2109222412109375,0,0.2174758911132812,0,0.2158050537109375,0,0,0.2344741821289062,0.244720458984375,0,0.232330322265625,0.239715576171875,0,0.2354888916015625,0,0.2400741577148438,0,0.237335205078125,0.2313919067382812,0,0.2370681762695312,0.2371749877929688,0,0.2390518188476562,0,0.2388992309570312,0.2413253784179688,0,0.2501220703125,0.2516326904296875,0.249298095703125,0,0.2502822875976562,0.2505340576171875,0,0,0.2519989013671875,0,0,0.2513656616210938,0.2508316040039062,0,0.252349853515625,0,0,0.2453460693359375,0.25018310546875,0,0.2355575561523438,0.2396240234375,0,0.03948974609375,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-7.004402160644531,0,0.1821441650390625,0,0.1987991333007812,0,0.1998825073242188,0,0.2048873901367188,0.210113525390625,0,0.2411117553710938,0,0,0.2451400756835938,0,0.2418136596679688,0,0.2407379150390625,0,0.23968505859375,0,0.2412796020507812,0,0.2416610717773438,0,0.2521286010742188,0.2513504028320312,0,0.2509307861328125,0,0.2494583129882812,0,0.2474899291992188,0.25128173828125,0.2528610229492188,0.251953125,0,0.2525100708007812,0,0.2540664672851562,0,0.2553634643554688,0,0.2544403076171875,0,0.254608154296875,0,0.2556533813476562,0,0.2558212280273438,0,0.2519683837890625,0,0.2430496215820312,0,0.23431396484375,0,0,0,0,0,0,0,-6.869270324707031,0,0.1951751708984375,0.2019195556640625,0,0.2053146362304688,0,0,0.2059860229492188,0,0.2328567504882812,0,0.241455078125,0,0.2377700805664062,0,0.2371139526367188,0,0.235687255859375,0.2356491088867188,0,0.2374954223632812,0.2388916015625,0,0.23974609375,0.2374267578125,0.2412033081054688,0,0.24005126953125,0,0.2443313598632812,0.2425689697265625,0.2468185424804688,0,0.2529830932617188,0.2528762817382812,0,0.25408935546875,0,0.2529144287109375,0.2543869018554688,0,0.2542648315429688,0,0.255126953125,0,0.2558441162109375,0,0.2471389770507812,0.2419586181640625,0,0.1492996215820312,0,0,0,0,0,0,0,0,0,0,0,-6.70904541015625,0.1961822509765625,0,0.2002716064453125,0,0.199310302734375,0,0.213531494140625,0,0.2414779663085938,0,0.245819091796875,0,0.2409515380859375,0,0,0.2409515380859375,0,0.2391281127929688,0,0.2400741577148438,0,0,0.2372207641601562,0,0.2401199340820312,0.243743896484375,0.2508087158203125,0.2473678588867188,0.2482986450195312,0.24945068359375,0.2498931884765625,0,0.2387771606445312,0.2404327392578125,0,0.2428817749023438,0,0.252685546875,0,0,0.2535400390625,0,0.253387451171875,0.2536239624023438,0,0.251922607421875,0.2470703125,0,0.2413177490234375,0,0.2045822143554688,0,0,0,0,0,0,0,0,0,0,0,-6.655494689941406,0,0.1923675537109375,0,0.196868896484375,0,0.1956329345703125,0,0,0.21142578125,0,0.2392425537109375,0.2450714111328125,0,0.2402267456054688,0.2386627197265625,0,0.2384719848632812,0,0.2391586303710938,0,0.2456893920898438,0,0.2475738525390625,0.247833251953125,0,0.2482452392578125,0,0.248992919921875,0.2485122680664062,0,0.2493515014648438,0,7.6922607421875,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7.62939453125,0,7.62939453125e-06,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,15.2587890625,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"filename":[null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null]},"interval":10,"files":[],"prof_output":"/tmp/RtmpBiwznD/filece1a4a40b0e.prof","highlight":{"output":["^output\\$"],"gc":["^<GC>$"],"stacktrace":["^\\.\\.stacktraceo(n|ff)\\.\\.$"]},"split":"h"}},"evals":[],"jsHooks":[]}</script>
```

``` r
# rowSums(), colSums(), rowMeans(), and colMeans() are vectorised and fast.
# for loop is not the slowest, but the ugliest.
```


For systematic speed comparisons, try the `microbenchmark` package

``` r
# 3 Equivalent calculations of the mean of a vector
mean1 <- function(x,p=1) mean(x^p)
mean2 <- function(x,p=1) sum(x^p) / length(x)
mean3 <- function(x,p=1) mean.default(x^p)

# Time them
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
##  mean1(x, 0.5) 19.07073 19.51188 24.24301 21.51683 27.24342 45.48891   100   a
##  mean2(x, 0.5) 18.22886 18.65846 22.41235 19.73016 20.80544 65.74797   100   a
##  mean3(x, 0.5) 19.05757 19.52983 23.07903 21.41777 22.78251 51.66424   100   a
```

**Vectorize**

Computers are really good at math, so exploit this.

* First try vectors
* Then try `apply` functions
* See https://uscbiostats.github.io/software-dev-site/handbook-slow-patterns.html


Vector operations are generally faster and easier to read than loops

``` r
x <- runif(1e6)

# Compare 2 moving averages

# First Try
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

``` r
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

``` r
microbenchmark::microbenchmark(
  ma1(y),
  ma2(y)
)
```

```
## Unit: milliseconds
##    expr       min        lq     mean    median        uq      max neval cld
##  ma1(y) 134.72036 137.40204 139.9307 139.62180 141.41910 151.1462   100  a 
##  ma2(y)  18.16531  20.16352  27.0050  25.65907  28.54137 186.7108   100   b
```
Likewise, matrix operations are often faster than vector operations.


**Packages**

Before creating your own program, check if there is a faster or more memory efficient version. E.g., [data.table](https://cran.r-project.org/web/packages/data.table/vignettes/datatable-intro.html) or [Rfast2](https://cran.r-project.org/web/packages/Rfast2/index.html) for basic data manipulation.

Some functions are simply wrappers for the function you want, and calling it directly can speed things up. 

``` r
X <- cbind(1, runif(1e6))
Y <- X %*% c(1,2) + rnorm(1e6)
DAT <- as.data.frame(cbind(Y,X))

system.time({ lm(Y~X, data=DAT) })
```

```
##    user  system elapsed 
##   0.397   0.036   0.167
```

``` r
system.time({ .lm.fit(X, Y) })
```

```
##    user  system elapsed 
##   0.100   0.000   0.033
```

``` r
system.time({ solve(t(X)%*%X) %*% (t(X)%*%Y) })
```

```
##    user  system elapsed 
##   0.024   0.000   0.019
```
Note that such functions to have fewer checks and return less information, so you must know exactly what you are putting in and getting out.


**Parallel**

Sometimes there will still be a problematic bottleneck. 

Your next step should be parallelism:

* Write the function as a general vectorized function.
* Apply the same function to every element in a list *at the same time*


``` r
# lapply in parallel on {m}ultiple {c}ores
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


``` r
# vectorize and compile
e_power_e_fun <- compiler::cmpfun( function(vector){ vector^vector} )

# base R
x <- 0:1E6
s_vc <- system.time( e_power_e_vec <- e_power_e_fun(x) )
s_vc
```

```
##    user  system elapsed 
##   0.029   0.001   0.029
```

``` r
# brute power
x <- 0:1E6
s_bp <- system.time({
  e_power_e_mc <- unlist( parallel::mclapply(x, mc.cores=2, FUN=e_power_e_fun))
})
s_bp
```

```
##    user  system elapsed 
##   0.849   0.199   0.593
```

``` r
# Same results
all(e_power_e_vec==e_power_e_mc)
```

```
## [1] TRUE
```

Parallelism does not go great with a GUI.
For identifying bottlenecks on a cluster without a GUI, try `Rprof()`

``` r
Rprof( interval = 0.005)
    # Create Data
    x <- runif(2e6)
    y <- sqrt(x)
    # Loop Format Data
    z <- y*NA
    for(i in 2:length(y)){ z[i] <- (y[i]-y[i-1])/2 }
    # Regression
    X <- cbind(1,x)[-1,]
    Z <- z[-1]
    reg_fast <- .lm.fit(X, Z)
Rprof(NULL)
summaryRprof()
```

If you still are stuck, you can

* try [Amazon Web Server](https://aws.amazon.com/ec2/) for more brute-power 
* rewrite bottlenecks with a working C++ compiler or Fortran compiler.

Before doing that, however, look into <https://cran.r-project.org/web/views/HighPerformanceComputing.html>


**Compiled Code**

You can use C++ code within R to speed up a specific chunk.

To get C++ on your computer

* On Windows, install Rtools.
* On Mac, install Xcode from the app store.
* On Linux, sudo apt-get install r-base-dev or similar.

To call C++ from R use package `Rcpp`

``` r
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

``` r
.C
.Fortran
```
For a tutorial, see https://masuday.github.io/fortran_tutorial/r.html


**Memory Usage**

For finding problematic blocks or whole scripts: `utils::Rprof(memory.profiling = TRUE)` logs total memory usage of R at regular time intervals

For finding problematic functions: `utils::Rprofmem()` logs memory usage at each call

For memory leaks, first free up space and use the `bench` package for timing

``` r
gc() # garbage cleanup

bench::mark(
  mean1(x,.5),
  mean2(x,.5),
  mean3(x,.5))
```



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

``` r
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

Make sure R is up to date. The current version of R (and any packages) used to make this document are

``` r
sessionInfo()
```

```
## R version 4.4.1 (2024-06-14)
## Platform: x86_64-redhat-linux-gnu
## Running under: Fedora Linux 40 (Workstation Edition)
## 
## Matrix products: default
## BLAS/LAPACK: FlexiBLAS OPENBLAS-OPENMP;  LAPACK version 3.11.0
## 
## locale:
##  [1] LC_CTYPE=en_US.UTF-8       LC_NUMERIC=C              
##  [3] LC_TIME=en_US.UTF-8        LC_COLLATE=en_US.UTF-8    
##  [5] LC_MONETARY=en_US.UTF-8    LC_MESSAGES=en_US.UTF-8   
##  [7] LC_PAPER=en_US.UTF-8       LC_NAME=C                 
##  [9] LC_ADDRESS=C               LC_TELEPHONE=C            
## [11] LC_MEASUREMENT=en_US.UTF-8 LC_IDENTIFICATION=C       
## 
## time zone: Europe/Berlin
## tzcode source: system (glibc)
## 
## attached base packages:
## [1] parallel  stats     graphics  grDevices utils     datasets  compiler 
## [8] methods   base     
## 
## other attached packages:
## [1] Rcpp_1.0.13-1        profvis_0.4.0        microbenchmark_1.5.0
## [4] sf_1.0-19            plotly_4.10.4        ggplot2_3.5.1       
## [7] colorout_1.3-2      
## 
## loaded via a namespace (and not attached):
##  [1] sandwich_3.1-1     sass_0.4.9         utf8_1.2.4         generics_0.1.3    
##  [5] tidyr_1.3.1        class_7.3-22       KernSmooth_2.23-24 lattice_0.22-6    
##  [9] digest_0.6.37      magrittr_2.0.3     evaluate_1.0.1     grid_4.4.1        
## [13] bookdown_0.41      mvtnorm_1.3-2      fastmap_1.2.0      Matrix_1.7-1      
## [17] jsonlite_1.8.9     e1071_1.7-16       DBI_1.2.3          survival_3.7-0    
## [21] multcomp_1.4-26    httr_1.4.7         purrr_1.0.2        fansi_1.0.6       
## [25] crosstalk_1.2.1    viridisLite_0.4.2  scales_1.3.0       TH.data_1.1-2     
## [29] codetools_0.2-20   lazyeval_0.2.2     jquerylib_0.1.4    cli_3.6.3         
## [33] rlang_1.1.4        units_0.8-5        splines_4.4.1      munsell_0.5.1     
## [37] withr_3.0.2        cachem_1.1.0       yaml_2.3.10        tools_4.4.1       
## [41] dplyr_1.1.4        colorspace_2.1-1   vctrs_0.6.5        R6_2.5.1          
## [45] zoo_1.8-12         proxy_0.4-27       lifecycle_1.0.4    classInt_0.4-10   
## [49] htmlwidgets_1.6.4  MASS_7.3-61        pkgconfig_2.0.3    pillar_1.9.0      
## [53] bslib_0.8.0        gtable_0.3.6       data.table_1.16.2  glue_1.8.0        
## [57] xfun_0.49          tibble_3.2.1       tidyselect_1.2.1   highr_0.11        
## [61] knitr_1.48         htmltools_0.5.8.1  rmarkdown_2.29
```
With Rstudio, you can update both R and Rstudio.


Make sure your packages are up to date

``` r
update.packages()
```

After updating R, you can update *all* packages stored in *all* `.libPaths()` with the following command

``` r
update.packages(checkBuilt=T)
# install.packages(old.packages(checkBuilt=T)[,"Package"])
```

To find broken packages after an update

``` r
library(purrr)

set_names(.libPaths()) %>%
  map(function(lib) {
    .packages(all.available = TRUE, lib.loc = lib) %>%
        keep(function(pkg) {
            f <- system.file('Meta', 'package.rds', package = pkg, lib.loc = lib)
            tryCatch({readRDS(f); FALSE}, error = function(e) TRUE)
        })
  })
# https://stackoverflow.com/questions/31935516/installing-r-packages-error-in-readrdsfile-error-reading-from-connection/55997765
```

To remove packages duplicated in multiple libraries

``` r
# Libraries
i <- installed.packages()
libs <- .libPaths()
# Find Duplicated Packages
i1 <- i[ i[,'LibPath']==libs[1], ]
i2 <- i[ i[,'LibPath']==libs[2], ]
dups <- i2[,'Package'] %in% i1[,'Package']
all( dups )
# Remove
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

``` bash
rstudio
```

Alternatively, you are encouraged to try using R without a GUI. E.g., on Fedora, this document can be created directly via 

``` bash
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


**Knitr:** 
You can produce a pdf from an .Rnw file via `knitr`


``` bash
Rscript -e "knitr::Sweave2knitr('Sweave_file.Rnw')"
Rscript -e "knitr::knit2pdf('Sweave_file-knitr.Rnw')"
```

For background on knitr

* https://yihui.org/knitr/
* https://kbroman.org/knitr_knutshell/pages/latex.html
* https://sachsmc.github.io/knit-git-markr-guide/knitr/knit.html


**Sweave:** is an alternative to Rmarkdown for integrating latex and R. While Rmarkdown "writes R and latex within markdown", Sweave "write R in latex". Sweave files end in ".Rnw" and can be called within R


``` r
Sweave('Sweavefile.Rnw')
```

or directly from the command line


``` bash
R CMD Sweave Sweavefile.Rnw 
```

In both cases, a latex file `Sweavefile.tex` is produced, which can then be converted to `Sweavefile.pdf`.


For more on Sweave,

* https://rpubs.com/YaRrr/SweaveIntro
* https://support.rstudio.com/hc/en-us/articles/200552056-Using-Sweave-and-knitr
* https://www.statistik.lmu.de/~leisch/Sweave/Sweave-manual.pdf



## Stata

For those transitioning from Stata or replicating others' Stata work, you can work with Stata data and code within R.

Translations of common procedures is provided by https://stata2r.github.io/. See also the textbook "R for Stata Users" by Robert A. Muenchen and Joseph M. Hilbe.

Many packages allows you to read data created by different programs. As of right now, `haven` is a particularly useful for reading in Stata files

``` r
library(haven)
read_dta()
# See also foreign::read.dta
```

You can also execute stata commands directly in R via package `Rstata`. (Last time I checked, `Rstata` requires you to have purchased a non-student version of Stata.) Moreover, you can include stata in the markdown reports via package `Statamarkdown`:

``` r
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



