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

``` r
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

``` r
source('MyFirstCode.R')
```
Note that you may first need to `setwd()` so your computer knows where you saved your code.^[You can also use *GUI: point-click* click 'Source > Source as a local job' on top right]


After you get this working
* add a the line `print(sum_squared(y, y))` to the bottom of `MyFirstCode.R`. 
* apply the function to a vectors specified outside of that script

``` r
## Pass Objects/Functions *to* Script
y <- c(3,1,NA)
source('MyFirstCode.R')

## Pass Objects/Functions *from* Script
z <- sqrt(y)/2
sum_squared(z,z)
```

**CLI Alternatives** *(Skippable)* There are also alternative ways to replicate via the command line interface (CLI) after opening a terminal.
 

``` bash
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
<div class="plotly html-widget html-fill-item" id="htmlwidget-03620ff1e9bd43937878" style="width:672px;height:480px;"></div>
<script type="application/json" data-for="htmlwidget-03620ff1e9bd43937878">{"x":{"visdat":{"9562b03e3e6":["function () ","plotlyVisDat"]},"cur_data":"9562b03e3e6","attrs":{"9562b03e3e6":{"x":{},"y":{},"alpha_stroke":1,"sizes":[10,100],"spans":[1,20]}},"layout":{"margin":{"b":40,"l":60,"t":25,"r":10},"xaxis":{"domain":[0,1],"automargin":true,"title":"X"},"yaxis":{"domain":[0,1],"automargin":true,"title":"Y"},"hovermode":"closest","showlegend":false},"source":"A","config":{"modeBarButtonsToAdd":["hoverclosest","hovercompare"],"showSendToCloud":false},"data":[{"x":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100],"y":[2.6793978239772205,4.4176789748525422,12.865093582005221,20.122113005956074,19.040193296350033,22.62892399465677,29.829807917085176,30.024482140528178,36.010759400533743,41.217278121620446,46.311959113385264,48.358516881544908,52.692626040373526,53.682663101964927,56.547146691532966,65.41197810286782,68.551515673563998,69.829692458754238,76.155931248506505,82.536141136099431,82.848062629584803,84.803619030589346,90.748220853752585,93.759147296112261,99.337591591218555,104.27342286262081,108.16396772340293,112.0661834872362,115.55353431942979,120.68040424906907,125.35857110755556,131.82128007705523,128.26089645232585,137.74985912273854,140.3455803122512,145.83251976596492,150.95582210716256,153.12063792986979,155.72611144641161,155.4459458558365,164.27680275644627,168.96913706332643,168.97950159215017,172.36030107129903,178.16257279401802,186.17449347566634,187.83735609043373,190.94126296986306,197.36284849917394,198.08450917653502,204.46663754960252,209.58841438016805,210.25059419214082,216.41049620119594,220.70977412882081,222.71807276724351,226.71049744874128,234.69940420848238,238.10885256470928,239.26202582375004,247.00860262557461,247.4698525654355,253.52614035007571,258.07118008955354,260.2498482927088,263.67910036992691,266.99249876116949,272.77020973790508,275.00533641084809,282.12771648493322,284.86788770343207,289.45808028462147,293.94203058007787,294.86876677244641,299.76075255496471,302.78726086307671,310.17629846687464,310.58474323068327,316.90632835730344,321.85621580933645,324.34257774819139,330.58071252456079,331.17806580446768,335.77906483043574,344.77417076061136,342.70876904617279,347.22789684593232,348.61292109843924,357.50479719838114,358.40640864456265,369.07610273025426,367.31474730681754,368.3940611281659,378.45755600438952,378.57444011062387,383.61958831882754,389.81153965888916,393.41660919553874,396.81946231890112,401.95074270247056],"type":"scatter","mode":"markers","marker":{"color":"rgba(31,119,180,1)","line":{"color":"rgba(31,119,180,1)"}},"error_y":{"color":"rgba(31,119,180,1)"},"error_x":{"color":"rgba(31,119,180,1)"},"line":{"color":"rgba(31,119,180,1)"},"xaxis":"x","yaxis":"y","frame":null}],"highlight":{"on":"plotly_click","persistent":false,"dynamic":false,"selectize":false,"opacityDim":0.20000000000000001,"selected":{"opacity":1},"debounce":0},"shinyEvents":["plotly_hover","plotly_click","plotly_selected","plotly_relayout","plotly_brushed","plotly_brushing","plotly_clickannotation","plotly_doubleclick","plotly_deselect","plotly_afterplot","plotly_sunburstclick"],"base_url":"https://plot.ly"},"evals":[],"jsHooks":[]}</script>
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

``` r
# list the files and directories
list.files(recursive=TRUE, include.dirs=TRUE)
# create directory called 'Data'
dir.create('Data')
```

## Logging/Sinking

When executing the makefile, you can also log the output. Either by 

1. Inserting some code into the makefile that logs/sinks the output 

``` r
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
## Error in eval(expr, envir, enclos): This is what an error looks like
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

###  Tracing 

Consider this example of an error process (originally taken from https://adv-r.hadley.nz/ ).

``` r
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
## debug at <text>#3: h(h0)
```

```
## Error: `d` must be numeric
```



###  Isolating

To inspect objects

``` r
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
## Many others
```

To check for values

``` r
all( x > -2 )
any( x > -2 )
## Check Matrix Rows
rowAny <- function(x) rowSums(x) > 0
rowAll <- function(x) rowSums(x) == ncol(x)
```

### Handling

Simplest Example

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

Simple Example

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

<!--## Ignore warnings/messages
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

``` r
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

``` r
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

``` r
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
<div class="profvis html-widget html-fill-item" id="htmlwidget-b041468127c6c44cc66b" style="width:100%;height:600px;"></div>
<script type="application/json" data-for="htmlwidget-b041468127c6c44cc66b">{"x":{"message":{"prof":{"time":[1,2,3,4,5,6,7,8,9,9,9,10,10,11,11,12,12,13,13,14,14,15,15,16,16,17,17,18,18,19,19,20,20,21,21,22,22,23,23,24,24,25,26,27,27,28,28,29,29,30,31,31,32,32,32,32,33,33,33,34,34,35,36,36,37,37,38,38,39,40,41,41,42,42,43,43,44,44,45,46,47,47,48,48,49,49,50,50,50,51,51,52,52,53,53,54,54,55,56,56,57,57,58,58,58,59,60,60,60,61,61,62,63,64,64,65,65,66,66,67,67,67,68,68,69,69,70,70,71,72,73,73,74,74,75,75,75,76,77,77,77,78,78,79,79,80,80,81,81,81,82,82,83,83,84,84,85,85,86,87,88,88,88,89,89,90,90,91,92,92,92,93,93,93,94,95,95,96,96,97,97,98,99,100,100,100,101,101,102,102,103,103,104,104,105,106,106,107,107,108,108,108,109,110,110,111,111,112,112,113,113,113,114,114,115,116,116,117,117,117,118,119,119,120,121,121,122,123,123,124,124,125,125,125,126,126,127,128,128,129,130,130,131,131,132,133,133,133,134,135,136,136,136,137,137,138,139,140,141,141,142,142,142,143,143,144,144,145,145,146,146,147,148,148,149,149,150,150,150,151,151,152,153,153,154,154,155,156,157,158,158,159,159,159,160,161,161,162,162,162,163,163,164,165,166,166,167,167,168,168,168,169,170,170,171,171,171,172,173,173,174,174,174,175,175,176,176,177,177,177,178,179,179,180,180,180,181,182,182,183,183,184,184,184,185,186,186,187,188,188,189,190,190,191,192,192,193,193,193,194,195,195,196,196,197,197,198,198,199,199,200,201,201,202,202,203,203,203,204,204,204,205,205,205,206,206,206,207,207,207,208,208,208,209,209,209,210,210,210,211,212,212,212,213,213,214,214,215,216,216,217,217,218,218,219,219,219,220,220,221,222,222,223,223,224,224,225,225,226,226,226,227,227,228,228,229,229,230,230,231,231,232,233,234,234,234,235,236,236,237,237,238,238,238,239,240,240,240,241,241,241,242,242,243,243,244,244,245,245,246,246,247,247,247,248,248,248,249,250,251,252,252,253,254,255,255,255,256,256,257,257,257,258,258,259,260,260,261,261,262,262,262,263,264,264,265,266,266,267,267,268,268,269,269,269,270,270,271,271,272,273,273,274,274,275,275,276,276,276,277,278,278,279,280,280,281,282,283,283,283,284,284,285,285,286,286,287,288,289,290,290,291,292,292,293,293,293,294,294,295,295,296,296,297,297,297,298,299,299,300,300,301,301,302,302,303,303,304,304,305,306,306,307,307,307,308,308,309,310,310,310,311,311,312,312,313,313,314,314,314,315,315,316,316,317,317,317,318,319,319,319,320,320,321,322,323,323,323,324,324,325,325,326,326,327,327,328,328,329,329,330,330,330,331,332,333,333,334,334,335,335,336,336,337,337,338,339,339,340,340,341,341,342,342,342,343,343,343,344,345,345,346,346,347,348,349,349,350,350,351,351,352,352,353,353,354,354,355,355,355,356,356,356,357,357,357,358,358,358,359,359,359,360,360,360,361,361,361,362,362,362,363,363,363,364,364,364,365,365,365,366,366,366,367,367,367,368,368,368,369,369,369,370,370,370,371,371,371,372,372,372,373,373,373,374,374,374,375,375,375,376,376,376,377,377,377,378,378,378,379,379,379,380,380,380,381,382,382,383,383,384,384,385,386,386,387,387,388,388,389,389,389,390,390,391,392,392,393,393,393,394,394,394,395,395,396,396,396,397,397,398,398,399,400,400,401,401,402,403,403,404,405,405,406,407,407,408,409,410,410,410,411,411,412,412,413,413,414,414,414,415,416,416,416,417,417,418,419,420,420,421,422,422,423,424,424,424,424,425,425,425,426,426,427,428,428,429,429,430,430,431,431,432,432,433,433,434,434,434,435,435,436,436,437,437,437,438,438,438,439,439,439,440,440,441,441,442,442,442,443,444,445,445,446,447,447,448,448,449,449,450,450,451,451,452,452,453,453,454,454,454,455,456,456,457,457,458,459,459,460,460,461,461,461,462,462,463,464,464,465,465,466,467,467,467,468,468,469,469,470,470,471,471,472,472,473,474,474,475,476,476,477,477,478,478,479,479,480,481,481,481,482,483,483,484,484,485,485,486,486,486,487,487,488,489,489,490,491,491,492,492,493,493,494,494,494,495,496,497,497,498,498,499,499,500,500,500,501,502,503,503,504,504,505,505,506,506,507,508,508,508,508,509,509,510,510,511,512,513,513,514,514,515,515,516,516,517,517,518,518,519,520,521,521,522,523,524,524,524,525,525,525,526,526,527,527,528,528,529,530,531,531,532,533,533,534,534,535,535,536,536,537,538,538,539,539,540,541,541,542,542,543,544,544,544,545,545,545,546,546,546,547,547,548,548,549,549,550,550,551,551,552,553,553,553,554,554,554,555,556,556,557,558,558,559,559,560,561,561,562,563,563,564,565,565,565,566,566,567,567,567,568,568,569,569,570,570,571,572,572,573,573,574,574,575,575,576,577,577,578,578,579,579,580,580,580,581,581,581,582,583,583,584,584,585,585,586,586,587,587,588,589,589,590,590,591,591,592,592,593,593,594,594,595,595,596,596,597,598,599,600,601,602,602,603,603,604,604,605,605,606,606,606,607,607,607,608,608,609,609,609,610,611,611,612,612,613,613,614,615,615,615,616,617,618,618,618,619,619,620,620,621,621,622,622,622,623,623,624,625,625,626,626,627,627,628,629,629,630,630,631,631,632,632,632,632,633,633,634,635,635,636,636,637,638,639,640,641,641,641,642,642,643,643,644,644,644,644,645,645,645,645,646,646,647,647,648,648,649,649,650,650,651,651,652,652,652,653,654,654,655,656,656,656,657,657,658,658,659,660,660,661,662,663,663,663,664,664,665,665,666,666,667,667,668,668,668,669,669,669,670,670,670,671,671,671,672,672,672,673,673,673,674,674,674,675,675,675,676,676,676,677,677,677,678,678,678,679,679,679,680,680,680,681,682,683,683,684,684,684,685,685,686,687,687,688,689,689,690,690,691,692,693,693,694,694,694,695,696,696,697,698,698,699,700,701,701,702,703,703,704,705,705,706,706,706,707,707,707,708,708,709,709,710,710,711,711,712,712,713,713,714,714,714,715,715,716,716,717,717,717,718,718,719,719,720,720,720,721,721,721,722,723,723,724,724,725,725,726,726,727,727,728,729,729,730,731,732,733,733,733,734,734,735,735,736,737,738,738,739,740,740,741,741,742,743,743,744,744,744,745,745,745,746,747,747,748,748,749,749,750,750,751,751,752,752,753,753,754,754,755,755,756,756,756,757,757,758,759,759,760,761,761,762,762,763,763,764,764,765,765,766,766,767,767,768,768,769,769,770,770,771,772,772,773,774,774,775,776,777,777,778,778,779,779,779,780,780,780,781,781,782,782,783,783,784,784,784,785,786,786,787,787,787,788,789,789,790,790,791,791,792,792,793,793,794,794,795,796,796,796,797,798,798,799,799,800,800,801,801,802,802,802,803,803,803,804,804,804,805,805,806,806,807,807,808,808,809,809,810,810,811,812,812,813,813,814,814,814,814,815,815,815,815,816,817,817,818,818,819,820,820,821,821,822,822,823,823,824,824,825,825,825,826,826,826,827,827,828,828,829,829,830,830,831,832,833,833,834,834,835,836,836,836,837,837,837,838,839,840,840,841,841,842,843,843,844,844,845,845,846,846,847,847,847,848,848,848,849,849,850,851,851,852,852,852,853,854,854,855,856,856,857,857,858,858,859,859,860,860,861,861,862,862,863,863,864,865,866,867,868,868,868,869,869,869,870,871,871,872,873,873,874,875,875,876,876,877,877,878,878,879,879,879,880,880,880,881,881,882,882,882,883,883,884,885,885,886,886,887,887,888,888,889,889,890,890,891,892,893,893,894,894,895,896,897,897,898,898,899,899,900,900,901,902,902,903,903,904,904,905,905,906,907,908,909,909,910,910,911,911,912,912,912,913,914,915,916,916,917,917,918,919,919,920,920,921,921,922,922,923,923,924,924,925,925,926,926,927,927,928,928,929,929,930,930,931,931,932,932,933,933,934,934,935,935,936,937,938,938,939,939,939,940,940,941,941,942,943,943,944,945,945,945,946,947,947,948,948,949,949,950,950,950,951,951,952,953,953,954,955,956,957,958,958,959,959,959,960,960,960,961,962,962,963,964,964,965,965,966,967,967,968,968,969,969,969,970,970,970,971,972,972,973,974,974,975,975,976,976,977,978,978,979,979,980,981,981,982,983,984,985,985,986,986,987,987,988,988,989,989,990,990,990,991,991,992,992,993,994,994,995,995,996,996,996,997,997,997,998,998,999,1000,1001,1002,1002,1002,1003,1003,1003,1004,1004,1005,1006,1006,1007,1007,1008,1008,1008,1009,1009,1010,1010,1011,1011,1012,1013,1013,1014,1015,1015,1016,1016,1017,1017,1018,1018,1019,1019,1020,1020,1021,1021,1022,1022,1023,1023,1023,1024,1024,1024,1025,1025,1026,1027,1027,1027,1028,1028,1029,1029,1030,1030,1031,1031,1032,1032,1032,1033,1033,1033,1034,1034,1035,1036,1037,1038,1038,1039,1040,1040,1041,1041,1042,1042,1043,1043,1043,1044,1045,1045,1046,1046,1046,1047,1047,1048,1048,1049,1049,1050,1050,1050,1051,1051,1051,1052,1052,1053,1054,1054,1055,1056,1057,1058,1058,1059,1059,1059,1060,1060,1061,1061,1062,1063,1064,1064,1065,1065,1066,1066,1067,1067,1067,1068,1068,1068,1069,1069,1069,1070,1070,1070,1071,1071,1071,1072,1072,1072,1073,1073,1074,1074,1075,1076,1076,1077,1077,1078,1078,1079,1079,1080,1080,1081,1081,1082,1082,1083,1083,1084,1084,1085,1085,1086,1086,1087,1087,1088,1088,1089,1089,1090,1090,1091,1091,1092,1092,1093,1093,1094,1094,1095,1095,1096,1096,1097,1097,1098,1098,1099,1099,1100,1100,1101,1101,1102,1102,1103,1103,1104,1104,1105,1105,1106,1106,1107,1107,1108,1108,1109,1109,1110,1110,1111,1111,1112,1112,1113,1113,1114,1114,1115,1115,1116,1116,1117,1117,1118,1118,1119,1119,1120,1120,1121,1121,1122,1122,1123,1123,1124,1124,1125,1125,1126,1126,1127,1127,1128,1128,1129,1129,1130,1130,1131,1131,1132,1132,1133,1133,1134,1134,1135,1136,1136,1137,1138,1138,1139,1139,1140,1140,1141,1141,1142,1143,1144,1145,1146,1146,1147,1148,1149,1150,1150,1151,1151,1152,1152,1153,1154,1154,1155,1156,1156,1157,1157,1158,1158,1159,1159,1160,1160,1161,1161,1162,1163,1163,1164,1164,1165,1165,1166,1166,1167,1167,1168,1169,1169,1169,1170,1170,1171,1171,1172,1173,1174,1174,1175,1175,1175,1176,1177,1177,1178,1179,1180,1180,1181,1182,1182,1182,1183,1183,1183,1184,1184,1184,1185,1185,1186,1186,1187,1187,1188,1188,1189,1189,1190,1190,1191,1191,1192,1192,1192,1193,1194,1195,1195,1196,1196,1197,1197,1198,1198,1199,1199,1200,1201,1201,1201,1202,1202,1202,1203,1203,1204,1204,1205,1205,1205,1206,1206,1206,1207,1207,1207,1208,1209,1210,1210,1211,1211,1212,1212,1212,1213,1213,1214,1214,1215,1215,1216,1216,1217,1217,1218,1219,1219,1220,1220,1221,1221,1221,1222,1223,1223,1224,1225,1225,1226,1226,1226,1227,1227,1228,1228,1229,1229,1230,1230,1231,1232,1233,1234,1234,1235,1235,1236,1236,1236,1237,1238,1238,1239,1240,1241,1241,1242,1242,1243,1243,1244,1244,1245,1245,1246,1247,1248,1249,1249,1250,1250,1251,1251,1251,1252,1252,1252,1253,1253,1253,1254,1254,1254,1255,1255,1256,1256,1257,1258,1258,1259,1260,1260,1261,1262,1262,1263,1264,1264,1265,1265,1266,1267,1268,1269,1270,1270,1271,1271,1272,1272,1273,1274,1274,1275,1275,1276,1276,1277,1277,1278,1278,1279,1279,1280,1281,1281,1282,1282,1283,1284,1285,1286,1287,1287,1287,1288,1288,1289,1289,1290,1291,1292,1293,1294,1294,1295,1295,1296,1296,1297,1297,1298,1298,1299,1299,1300,1300,1301,1301,1302,1302,1303,1304,1304,1305,1305,1306,1306,1307,1307,1308,1308,1309,1309,1310,1310,1311,1311,1312,1313,1313,1313,1314,1315,1315,1316,1316,1317,1317,1318,1319,1319,1320,1321,1321,1322,1322,1323,1323,1324,1324,1325,1325,1326,1326,1327,1327,1328,1328,1329,1329,1330,1331,1331,1332,1332,1333,1334,1334,1335,1335,1335,1336,1336,1337,1337,1338,1338,1339,1339,1340,1340,1341,1341,1342,1343,1343,1343,1344,1344,1344,1345,1346,1346,1347,1347,1348,1348,1349,1350,1350,1351,1351,1352,1353,1353,1354,1355,1356,1357,1357,1358,1358,1359,1359,1360,1361,1361,1362,1362,1362,1363,1363,1363,1364,1365,1365,1365,1366,1366,1366,1367,1367,1367,1368,1368,1368,1369,1369,1369,1370,1370,1371,1371,1372,1372,1373,1374,1374,1375,1375,1376,1377,1378,1378,1379,1379,1379,1380,1380,1381,1381,1382,1382,1383,1383,1384,1384,1385,1385,1386,1386,1387,1387,1388,1388,1389,1390,1390,1391,1391,1392,1392,1393,1393,1394,1394,1395,1395,1396,1396,1397,1397,1398,1398,1399,1399,1400,1400,1401,1401,1402,1402,1403,1403,1404,1404,1405,1405,1406,1406,1407,1407,1408,1408,1409,1409,1409,1409,1409,1409,1409,1409,1410,1410,1410,1410,1410,1410,1410,1410,1410,1410,1410,1410,1410,1410,1410,1410,1410,1410,1410,1410,1410,1410,1410,1410,1410,1410,1410,1410,1410,1410,1410,1410,1410,1410,1410,1410,1410,1410,1410,1410,1410,1410,1410,1411,1411,1411,1411,1411,1411,1411,1411,1412,1412,1412,1412,1412,1412,1412,1412,1413,1413,1413,1413,1413,1413,1413,1413,1414,1414,1414,1414,1414,1414,1414,1414,1415,1415,1415,1415,1415,1415,1415,1415,1416,1416,1416,1416,1416,1416,1416,1416,1417,1417,1417,1417,1417,1417,1417,1417,1418,1418,1418,1418,1418,1418,1418,1418,1419,1419,1419,1419,1419,1419,1419,1419,1420,1420,1420,1420,1420,1420,1420,1420,1421,1421,1421,1421,1421,1421,1421,1421,1422,1422,1422,1422,1422,1422,1422,1422,1423,1423,1423,1423,1423,1423,1423,1423,1424,1424,1424,1424,1424,1424,1424,1424,1425,1425,1425,1425,1425,1425,1425,1425,1426,1426,1426,1426,1426,1426,1426,1426,1427,1427,1427,1427,1427,1427,1427,1427,1428,1428,1428,1428,1428,1428,1428,1428,1429,1429,1429,1429,1429,1429,1429,1429,1430,1430,1430,1430,1430,1430,1430,1430],"depth":[1,1,1,1,1,1,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,1,2,1,4,3,2,1,3,2,1,2,1,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,1,3,2,1,2,1,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,1,2,1,2,1,3,2,1,1,3,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,1,3,2,1,2,1,2,1,1,3,2,1,3,2,1,1,2,1,2,1,2,1,1,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,3,2,1,1,2,1,1,2,1,1,2,1,2,1,3,2,1,2,1,1,2,1,1,2,1,2,1,1,3,2,1,1,1,3,2,1,2,1,1,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,1,1,1,2,1,3,2,1,1,2,1,3,2,1,2,1,1,1,2,1,2,1,3,2,1,1,2,1,3,2,1,1,2,1,3,2,1,2,1,2,1,3,2,1,1,2,1,3,2,1,1,2,1,2,1,3,2,1,1,2,1,1,2,1,1,2,1,1,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,1,3,2,1,1,2,1,2,1,3,2,1,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,1,1,1,2,1,1,1,3,2,1,2,1,3,2,1,2,1,1,2,1,2,1,3,2,1,1,2,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,1,2,1,1,2,1,1,1,3,2,1,2,1,2,1,2,1,1,1,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,2,1,1,3,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,3,2,1,1,3,2,1,2,1,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,3,2,1,3,2,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,1,2,1,1,2,1,1,2,1,1,1,3,2,1,2,1,2,1,2,1,3,2,1,1,3,2,1,2,1,1,1,2,1,1,2,1,1,4,3,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,3,2,1,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,1,3,2,1,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,1,2,1,2,1,2,1,3,2,1,1,1,2,1,2,1,2,1,3,2,1,1,1,2,1,2,1,2,1,2,1,1,4,3,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,1,1,3,2,1,3,2,1,2,1,2,1,2,1,1,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,1,2,1,1,2,1,2,1,1,2,1,1,2,1,1,3,2,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,1,1,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,3,2,1,1,2,1,2,1,2,1,1,3,2,1,1,1,3,2,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,4,3,2,1,2,1,1,2,1,2,1,1,1,1,1,3,2,1,2,1,2,1,4,3,2,1,4,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,1,3,2,1,2,1,2,1,1,2,1,1,1,3,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,1,1,2,1,3,2,1,2,1,1,2,1,1,2,1,2,1,1,1,2,1,3,2,1,1,2,1,1,2,1,1,1,2,1,1,2,1,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,3,2,1,2,1,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,1,1,3,2,1,2,1,2,1,1,1,2,1,1,2,1,2,1,1,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,1,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,3,2,1,1,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,4,3,2,1,4,3,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,1,3,2,1,3,2,1,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,1,2,1,3,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,1,1,3,2,1,3,2,1,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,1,1,2,1,2,1,2,1,3,2,1,1,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,3,2,1,2,1,2,1,1,2,1,1,3,2,1,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,1,1,1,1,2,1,3,2,1,3,2,1,1,2,1,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,1,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,2,1,1,1,1,3,2,1,3,2,1,2,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,1,1,1,2,1,1,2,1,2,1,2,1,3,2,1,1,2,1,3,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,1,2,1,1,1,1,2,1,3,2,1,2,1,2,1,1,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,1,1,1,1,2,1,1,1,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,1,1,2,1,3,2,1,1,2,1,1,1,2,1,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,1,1,2,1,2,1,3,2,1,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,1,1,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,1,2,1,1,2,1,1,2,1,2,1,1,1,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,1,1,1,3,2,1,2,1,2,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,1,1,1,2,1,2,1,2,1,1,2,1,3,2,1,3,2,1,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,8,7,6,5,4,3,2,1,43,42,41,40,39,38,37,36,35,34,33,32,31,30,29,28,27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1],"label":["rowSums","rowSums","rowSums","rowSums","rowMeans","rowMeans","rowMeans","rowMeans","<GC>","aperm.default","apply","aperm.default","apply","aperm.default","apply","aperm.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","mean.default","apply","FUN","apply","apply","apply","is.numeric","local","mean.default","apply","FUN","apply","apply","FUN","apply","<GC>","isTRUE","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","<GC>","apply","FUN","apply","mean.default","apply","FUN","apply","apply","apply","mean.default","apply","mean.default","apply","length","local","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","<GC>","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","apply","apply","FUN","apply","mean.default","apply","<GC>","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","apply","FUN","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","length","local","mean.default","apply","apply","apply","<GC>","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","length","local","is.na","local","isTRUE","mean.default","apply","mean.default","apply","apply","mean.default","apply","<GC>","FUN","apply","apply","FUN","apply","apply","FUN","apply","apply","mean.default","apply","FUN","apply","<GC>","mean.default","apply","mean.default","apply","apply","length","local","apply","FUN","apply","mean.default","apply","apply","<GC>","mean.default","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","apply","mean.default","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","FUN","apply","apply","is.numeric","local","FUN","apply","apply","apply","apply","mean.default","apply","<GC>","mean.default","apply","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","apply","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","<GC>","apply","apply","length","local","apply","FUN","apply","apply","mean.default","apply","isTRUE","mean.default","apply","apply","<GC>","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","length","local","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","isTRUE","mean.default","apply","is.numeric","local","mean.default","apply","apply","mean.default","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","is.na","local","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","apply","apply","<GC>","FUN","apply","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","apply","isTRUE","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","length","local","mean.default","apply","isTRUE","mean.default","apply","<GC>","length","local","apply","apply","apply","FUN","apply","apply","apply","<GC>","mean.default","apply","length","local","isTRUE","mean.default","apply","FUN","apply","apply","mean.default","apply","FUN","apply","<GC>","FUN","apply","apply","length","local","apply","FUN","apply","mean.default","apply","FUN","apply","<GC>","FUN","apply","length","local","FUN","apply","apply","FUN","apply","FUN","apply","mean.default","apply","<GC>","mean.default","apply","apply","FUN","apply","apply","mean.default","apply","apply","apply","<GC>","FUN","apply","mean.default","apply","length","local","mean.default","apply","apply","apply","apply","<GC>","apply","apply","is.na","local","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","apply","is.numeric","local","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","<GC>","apply","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","apply","<GC>","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","<GC>","FUN","apply","mean.default","apply","length","local","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","<GC>","mean.default","apply","apply","apply","mean.default","apply","FUN","apply","FUN","apply","<GC>","apply","FUN","apply","apply","FUN","apply","FUN","apply","is.na","local","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","mean.default","apply","FUN","apply","apply","apply","<GC>","apply","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","is.numeric","local","FUN","apply","FUN","apply","apply","mean.default","apply","length","local","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","apply","mean.default","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","<GC>","FUN","apply","FUN","apply","length","local","apply","length","local","FUN","apply","apply","FUN","apply","apply","length","local","apply","FUN","apply","apply","apply","<GC>","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","length","local","apply","mean.default","apply","apply","<GC>","isTRUE","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","is.na","local","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","<GC>","apply","isTRUE","mean.default","apply","apply","mean.default","apply","mean.default","apply","apply","length","local","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","<GC>","FUN","apply","mean.default","apply","FUN","apply","is.numeric","local","FUN","apply","mean.default","apply","apply","mean.default","apply","apply","length","local","FUN","apply","FUN","apply","mean.default","apply","apply","<GC>","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","<GC>","mean.default","apply","apply","apply","mean.default","apply","length","local","FUN","apply","isTRUE","mean.default","apply","apply","apply","is.numeric","local","mean.default","apply","length","local","FUN","apply","apply","<GC>","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","apply","apply","FUN","apply","length","local","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","apply","apply","FUN","apply","apply","apply","<GC>","length","local","<GC>","length","local","is.numeric","local","mean.default","apply","mean.default","apply","apply","apply","mean.default","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","apply","mean.default","apply","mean.default","apply","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","apply","mean.default","apply","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","FUN","apply","is.na","local","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","FUN","apply","is.na","local","mean.default","apply","is.na","local","is.numeric","local","apply","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","<GC>","apply","mean.default","apply","FUN","apply","apply","apply","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","apply","isTRUE","mean.default","apply","mean.default","apply","<GC>","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","is.na","local","apply","is.numeric","local","is.na","local","FUN","apply","<GC>","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","length","local","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","<GC>","FUN","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","is.na","local","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","length","local","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","apply","apply","mean.default","apply","<GC>","length","local","apply","mean.default","apply","apply","FUN","apply","apply","apply","mean.default","apply","apply","mean.default","apply","apply","mean.default","apply","<GC>","is.numeric","local","<GC>","is.numeric","local","FUN","apply","is.numeric","local","is.numeric","local","FUN","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","mean.default","apply","length","local","FUN","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","apply","apply","apply","<GC>","is.numeric","local","length","local","FUN","apply","apply","apply","FUN","apply","apply","mean.default","apply","FUN","apply","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","length","local","FUN","apply","<GC>","mean.default","apply","mean.default","apply","apply","mean.default","apply","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","apply","<GC>","apply","mean.default","apply","FUN","apply","apply","is.numeric","local","apply","mean.default","apply","apply","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","is.numeric","local","isTRUE","mean.default","apply","apply","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","<GC>","apply","<GC>","apply","<GC>","apply","is.na","local","mean.default","apply","apply","isTRUE","mean.default","apply","apply","mean.default","apply","FUN","apply","is.numeric","local","FUN","apply","isTRUE","mean.default","apply","<GC>","is.numeric","local","<GC>","is.numeric","local","FUN","apply","length","local","length","local","FUN","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","apply","length","local","FUN","apply","apply","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","length","local","is.na","local","mean.default","apply","apply","apply","mean.default","apply","mean.default","apply","apply","<GC>","length","local","<GC>","length","local","apply","apply","FUN","apply","mean.default","apply","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","apply","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","is.numeric","local","mean.default","apply","apply","apply","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","mean.default","apply","apply","is.numeric","local","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","is.numeric","local","isTRUE","mean.default","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","is.na","local","mean.default","apply","<GC>","apply","<GC>","apply","apply","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","FUN","apply","<GC>","apply","<GC>","apply","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","apply","apply","apply","FUN","apply","<GC>","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","apply","FUN","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","mean.default","apply","length","local","FUN","apply","FUN","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","apply","<GC>","apply","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","mean.default","apply","mean.default","apply","mean.default","apply","<GC>","FUN","apply","FUN","apply","apply","FUN","apply","apply","apply","apply","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","mean.default","apply","apply","FUN","apply","is.numeric","local","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","apply","FUN","apply","apply","apply","apply","mean.default","apply","mean.default","apply","<GC>","apply","<GC>","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","<GC>","length","local","<GC>","length","local","FUN","apply","apply","apply","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","<GC>","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","apply","<GC>","apply","<GC>","apply","FUN","apply","mean.default","apply","mean.default","apply","is.numeric","local","is.numeric","local","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","is.na","local","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","apply","apply","apply","FUN","apply","apply","FUN","apply","<GC>","apply","<GC>","apply","isTRUE","mean.default","apply","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","length","local","apply","mean.default","apply","apply","apply","apply","FUN","apply","<GC>","FUN","apply","mean.default","apply","FUN","apply","apply","apply","length","local","FUN","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","is.numeric","local","mean.default","apply","apply","mean.default","apply","is.numeric","local","mean.default","apply","is.na","local","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","apply","length","local","FUN","apply","FUN","apply","mean.default","apply","apply","apply","apply","apply","mean.default","apply","apply","apply","apply","mean.default","apply","FUN","apply","FUN","apply","apply","mean.default","apply","apply","FUN","apply","FUN","apply","<GC>","apply","<GC>","apply","mean.default","apply","mean.default","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","apply","apply","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","apply","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","is.numeric","local","FUN","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","length","local","FUN","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","<GC>","length","local","<GC>","length","local","<GC>","length","local","apply","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","length","local","FUN","apply","FUN","apply","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","apply","mean.default","apply","apply","is.numeric","local","isTRUE","mean.default","apply","FUN","apply","<GC>","apply","<GC>","apply","FUN","apply","apply","apply","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","apply","mean.default","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","apply","FUN","apply","FUN","apply","<GC>","length","local","<GC>","length","local","<GC>","length","local","isTRUE","mean.default","apply","is.na","local","FUN","apply","apply","mean.default","apply","apply","mean.default","apply","apply","mean.default","apply","apply","FUN","apply","FUN","apply","apply","apply","apply","apply","FUN","apply","FUN","apply","mean.default","apply","apply","<GC>","apply","<GC>","apply","FUN","apply","mean.default","apply","length","local","mean.default","apply","apply","mean.default","apply","FUN","apply","apply","apply","apply","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","apply","apply","apply","apply","is.na","local","mean.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","is.numeric","local","mean.default","apply","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","length","local","FUN","apply","mean.default","apply","apply","FUN","apply","apply","FUN","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","mean.default","apply","FUN","apply","length","local","mean.default","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","is.numeric","local","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","apply","mean.default","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","<GC>","length","local","<GC>","length","local","<GC>","length","local","isTRUE","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","FUN","apply","mean.default","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","putconst","cb$putcode","cmpSubsetDispatch","h","tryInline","cmpCall","cmp","cmpPrim2","h","tryInline","cmpCall","cmp","cmpPrim2","h","tryInline","cmpCall","cmp","h","tryInline","cmpCall","cmp","cmpPrim2","h","tryInline","cmpCall","cmp","cmpComplexAssign","h","tryInline","cmpCall","cmp","h","tryInline","cmpCall","cmp","cmpForBody","h","tryInline","cmpCall","cmp","genCode","compile","compiler:::tryCompile","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis"],"filenum":[1,1,1,1,1,1,1,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,1,null,null,null,1,null,1,1,null,1,null,null,null,1,null,null,1,null,1,1,null,1,null,1,null,1,1,1,null,1,null,1,null,1,null,1,1,1,null,1,null,1,null,null,null,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,null,1,1,null,null,1,null,1,1,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,1,1,null,1,null,1,null,null,1,1,null,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,1,1,null,null,1,null,1,null,1,1,null,null,1,null,null,1,1,null,1,null,null,null,1,1,1,null,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,null,1,1,null,1,null,null,null,null,null,null,1,null,1,1,null,1,null,null,1,1,null,1,1,null,1,1,null,1,null,1,null,null,1,null,1,1,null,null,1,null,1,null,1,1,null,null,1,1,1,null,null,1,null,1,1,1,1,null,1,null,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,null,1,null,1,1,null,null,null,1,1,1,1,null,1,null,null,1,1,null,1,null,null,1,null,1,1,1,null,1,null,1,null,null,1,1,null,1,null,null,1,1,null,1,null,null,1,null,1,null,1,null,null,1,1,null,1,null,null,1,1,null,1,null,1,null,null,1,1,null,1,1,null,null,1,null,1,1,null,1,null,null,1,1,null,1,null,1,null,1,null,1,null,1,1,null,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,1,null,null,1,null,null,null,1,1,null,1,null,1,null,1,null,null,1,null,1,1,null,1,null,1,null,1,null,1,null,null,1,null,null,null,1,null,1,null,1,null,1,1,1,null,null,1,1,null,1,null,1,null,null,1,1,null,null,1,null,null,1,null,1,null,1,null,1,null,null,null,1,null,null,1,null,null,null,1,1,1,null,1,1,1,null,null,1,null,null,null,null,1,null,1,1,null,1,null,1,null,null,1,1,null,null,1,null,1,null,1,null,1,null,null,1,null,null,null,1,1,null,1,null,1,null,1,null,null,1,1,null,1,1,null,1,1,1,null,null,1,null,1,null,null,null,1,1,1,1,null,1,1,null,null,null,null,1,null,1,null,1,null,1,null,null,1,1,null,null,null,1,null,1,null,1,null,1,null,1,1,null,1,null,null,1,null,1,1,null,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,null,1,1,null,null,1,null,1,1,1,null,null,1,null,1,null,null,null,1,null,1,null,1,null,1,null,null,1,1,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,null,null,null,1,null,null,1,1,null,1,null,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,1,null,null,null,1,null,1,1,null,1,null,null,null,1,null,null,1,null,1,1,null,1,null,null,1,null,null,1,null,1,null,null,1,null,1,null,null,1,null,null,null,1,1,null,1,1,null,null,1,null,1,1,1,null,null,1,null,1,null,1,null,1,null,null,1,1,null,null,1,null,1,1,1,null,null,1,null,1,1,null,null,null,1,null,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,null,null,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,null,1,1,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,1,null,1,null,1,1,null,null,null,1,null,null,1,null,1,1,null,1,null,1,1,null,null,1,null,1,null,1,null,null,null,1,null,1,1,null,1,1,null,null,null,1,null,1,null,1,1,null,null,1,1,null,1,null,1,null,1,null,null,1,null,1,1,null,1,1,null,1,null,1,null,1,null,null,1,1,1,null,1,null,null,null,1,null,null,1,1,1,null,null,null,1,null,null,null,1,1,null,null,null,1,null,1,null,1,1,1,null,1,null,null,null,1,null,1,null,1,null,1,1,1,null,1,1,1,null,null,null,null,null,null,null,null,null,1,null,1,1,1,null,1,1,null,1,null,1,null,1,null,1,1,null,1,null,1,1,null,1,null,1,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,1,null,null,1,null,null,1,1,null,1,1,null,1,null,1,1,null,1,1,null,1,1,null,null,1,null,1,null,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,1,null,1,null,null,null,1,null,null,1,null,null,1,1,null,1,null,null,null,1,null,null,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,1,1,1,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,1,null,null,1,1,null,1,null,1,null,1,1,null,null,1,1,1,null,null,1,null,1,null,1,null,1,null,null,1,null,1,1,null,1,null,1,null,null,1,null,null,null,null,null,1,null,null,null,1,null,1,1,null,1,null,1,1,1,1,1,null,null,1,null,1,null,null,null,null,null,1,null,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,1,null,1,1,null,null,1,null,1,null,1,1,null,1,1,1,null,null,1,null,1,null,1,null,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,1,1,null,1,null,null,1,null,null,1,null,1,1,null,1,null,1,1,1,null,1,null,null,null,1,null,1,1,null,1,1,1,null,1,1,null,1,1,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,1,null,1,null,1,null,null,1,null,1,null,1,null,null,1,null,1,null,1,null,null,1,null,null,1,1,null,1,null,null,null,1,null,1,null,1,1,null,1,1,1,1,null,null,null,null,null,null,1,1,1,null,1,1,null,1,null,1,1,null,1,null,null,1,null,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,null,1,null,null,1,null,1,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,null,1,null,1,1,1,null,1,null,1,null,null,1,null,null,1,null,1,null,1,null,null,null,null,1,1,null,1,null,null,1,1,null,1,null,1,null,1,null,1,null,null,null,1,1,null,null,1,1,null,1,null,1,null,null,null,1,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,1,null,1,null,1,1,null,1,null,1,null,null,null,1,null,null,null,1,1,null,null,null,1,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,1,null,null,null,null,null,1,1,1,null,1,null,1,1,null,null,null,null,null,null,1,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,1,1,null,1,null,null,1,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,null,1,1,1,1,1,null,null,1,null,null,1,1,null,1,1,null,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,null,null,null,1,null,1,1,null,1,null,1,null,null,null,1,null,1,null,1,1,1,null,1,null,1,1,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,1,1,1,null,1,null,1,null,1,null,null,1,1,1,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,null,1,null,1,1,1,null,1,null,null,1,null,1,null,1,1,null,1,1,null,null,1,1,null,1,null,1,null,1,null,null,1,null,1,1,null,1,1,1,1,1,null,1,null,null,1,null,null,1,1,null,1,1,null,1,null,null,1,null,1,null,1,null,null,1,null,null,1,1,null,1,1,null,1,null,1,null,1,1,null,1,null,1,1,null,1,1,1,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,1,null,1,null,1,null,null,null,null,null,null,null,1,1,1,1,null,null,1,null,null,1,null,1,1,null,1,null,1,null,null,1,null,1,null,1,null,1,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,null,null,null,null,1,null,null,1,null,null,1,null,1,1,null,null,1,null,1,null,1,null,1,null,null,null,null,1,null,null,1,null,1,1,1,1,null,1,1,null,1,null,1,null,1,null,null,1,1,null,1,null,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,1,1,1,1,null,1,null,null,1,null,1,null,1,1,1,null,null,null,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,null,1,1,null,1,null,null,null,1,null,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,1,null,null,null,1,null,1,null,1,1,1,1,1,null,1,1,1,1,null,1,null,1,null,1,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,1,null,null,1,null,1,null,1,1,1,null,1,null,null,1,1,null,1,1,1,null,1,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,null,null,1,null,1,null,1,null,null,1,1,1,null,1,null,null,null,1,null,1,null,1,1,null,null,1,null,null,1,null,1,null,1,null,null,null,null,null,null,null,null,null,1,1,null,1,null,1,null,null,1,null,1,null,1,null,null,null,1,null,1,1,null,1,null,1,null,null,1,1,null,1,1,null,null,null,null,1,null,1,null,1,null,1,null,1,1,1,1,null,1,null,1,null,null,1,1,null,1,1,1,null,1,null,1,null,1,null,1,null,1,1,1,1,null,1,null,1,null,null,null,null,null,null,null,null,null,null,null,1,null,null,null,1,1,null,1,1,null,1,1,null,1,1,null,1,null,1,1,1,1,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,null,null,1,1,null,1,null,1,1,1,1,1,null,null,1,null,1,null,1,1,1,1,1,null,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,null,null,1,null,1,null,1,1,null,null,1,1,null,null,null,1,null,1,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,null,1,1,null,1,null,1,1,null,1,null,null,1,null,null,null,1,null,1,null,1,null,1,null,1,1,null,null,1,null,null,1,1,null,1,null,1,null,1,1,null,1,null,1,1,null,1,1,1,1,null,1,null,1,null,1,1,null,1,null,null,1,null,null,1,1,null,null,null,null,null,null,null,null,null,null,null,1,null,null,1,null,1,null,1,null,1,1,null,1,null,1,1,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,1,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null],"linenum":[10,10,10,10,11,11,11,11,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,12,null,null,null,12,null,12,12,null,12,null,null,null,12,null,null,12,null,12,12,null,12,null,12,null,12,12,12,null,12,null,12,null,12,null,12,12,12,null,12,null,12,null,null,null,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,null,12,12,null,null,12,null,12,12,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,12,12,null,12,null,12,null,null,12,12,null,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,12,12,null,null,12,null,12,null,12,12,null,null,12,null,null,12,12,null,12,null,null,null,12,12,12,null,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,null,12,12,null,12,null,null,null,null,null,null,12,null,12,12,null,12,null,null,12,12,null,12,12,null,12,12,null,12,null,12,null,null,12,null,12,12,null,null,12,null,12,null,12,12,null,null,12,12,12,null,null,12,null,12,12,12,12,null,12,null,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,null,12,null,12,12,null,null,null,12,12,12,12,null,12,null,null,12,12,null,12,null,null,12,null,12,12,12,null,12,null,12,null,null,12,12,null,12,null,null,12,12,null,12,null,null,12,null,12,null,12,null,null,12,12,null,12,null,null,12,12,null,12,null,12,null,null,12,12,null,12,12,null,null,12,null,12,12,null,12,null,null,12,12,null,12,null,12,null,12,null,12,null,12,12,null,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,12,null,null,12,null,null,null,12,12,null,12,null,12,null,12,null,null,12,null,12,12,null,12,null,12,null,12,null,12,null,null,12,null,null,null,12,null,12,null,12,null,12,12,12,null,null,12,12,null,12,null,12,null,null,12,12,null,null,12,null,null,12,null,12,null,12,null,12,null,null,null,12,null,null,12,null,null,null,12,12,12,null,12,12,12,null,null,12,null,null,null,null,12,null,12,12,null,12,null,12,null,null,12,12,null,null,12,null,12,null,12,null,12,null,null,12,null,null,null,12,12,null,12,null,12,null,12,null,null,12,12,null,12,12,null,12,12,12,null,null,12,null,12,null,null,null,12,12,12,12,null,12,12,null,null,null,null,12,null,12,null,12,null,12,null,null,12,12,null,null,null,12,null,12,null,12,null,12,null,12,12,null,12,null,null,12,null,12,12,null,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,null,12,12,null,null,12,null,12,12,12,null,null,12,null,12,null,null,null,12,null,12,null,12,null,12,null,null,12,12,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,null,null,null,12,null,null,12,12,null,12,null,12,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,12,null,null,null,12,null,12,12,null,12,null,null,null,12,null,null,12,null,12,12,null,12,null,null,12,null,null,12,null,12,null,null,12,null,12,null,null,12,null,null,null,12,12,null,12,12,null,null,12,null,12,12,12,null,null,12,null,12,null,12,null,12,null,null,12,12,null,null,12,null,12,12,12,null,null,12,null,12,12,null,null,null,12,null,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,null,null,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,null,12,12,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,12,null,12,null,12,12,null,null,null,12,null,null,12,null,12,12,null,12,null,12,12,null,null,12,null,12,null,12,null,null,null,12,null,12,12,null,12,12,null,null,null,12,null,12,null,12,12,null,null,12,12,null,12,null,12,null,12,null,null,12,null,12,12,null,12,12,null,12,null,12,null,12,null,null,12,12,12,null,12,null,null,null,12,null,null,12,12,12,null,null,null,12,null,null,null,12,12,null,null,null,12,null,12,null,12,12,12,null,12,null,null,null,12,null,12,null,12,null,12,12,12,null,12,12,12,null,null,null,null,null,null,null,null,null,12,null,12,12,12,null,12,12,null,12,null,12,null,12,null,12,12,null,12,null,12,12,null,12,null,12,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,12,null,null,12,null,null,12,12,null,12,12,null,12,null,12,12,null,12,12,null,12,12,null,null,12,null,12,null,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,12,null,12,null,null,null,12,null,null,12,null,null,12,12,null,12,null,null,null,12,null,null,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,12,12,12,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,12,null,null,12,12,null,12,null,12,null,12,12,null,null,12,12,12,null,null,12,null,12,null,12,null,12,null,null,12,null,12,12,null,12,null,12,null,null,12,null,null,null,null,null,12,null,null,null,12,null,12,12,null,12,null,12,12,12,12,12,null,null,12,null,12,null,null,null,null,null,12,null,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,12,null,12,12,null,null,12,null,12,null,12,12,null,12,12,12,null,null,12,null,12,null,12,null,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,12,12,null,12,null,null,12,null,null,12,null,12,12,null,12,null,12,12,12,null,12,null,null,null,12,null,12,12,null,12,12,12,null,12,12,null,12,12,null,12,null,null,null,null,null,null,null,12,null,null,null,null,null,12,null,12,null,12,null,null,12,null,12,null,12,null,null,12,null,12,null,12,null,null,12,null,null,12,12,null,12,null,null,null,12,null,12,null,12,12,null,12,12,12,12,null,null,null,null,null,null,12,12,12,null,12,12,null,12,null,12,12,null,12,null,null,12,null,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,null,12,null,null,12,null,12,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,null,12,null,12,12,12,null,12,null,12,null,null,12,null,null,12,null,12,null,12,null,null,null,null,12,12,null,12,null,null,12,12,null,12,null,12,null,12,null,12,null,null,null,12,12,null,null,12,12,null,12,null,12,null,null,null,12,null,null,12,null,null,null,null,null,null,null,12,null,null,null,null,null,12,null,12,null,12,12,null,12,null,12,null,null,null,12,null,null,null,12,12,null,null,null,12,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,12,null,null,null,null,null,12,12,12,null,12,null,12,12,null,null,null,null,null,null,12,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,12,12,null,12,null,null,12,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,null,12,12,12,12,12,null,null,12,null,null,12,12,null,12,12,null,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,null,null,null,12,null,12,12,null,12,null,12,null,null,null,12,null,12,null,12,12,12,null,12,null,12,12,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,12,12,12,null,12,null,12,null,12,null,null,12,12,12,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,null,12,null,12,12,12,null,12,null,null,12,null,12,null,12,12,null,12,12,null,null,12,12,null,12,null,12,null,12,null,null,12,null,12,12,null,12,12,12,12,12,null,12,null,null,12,null,null,12,12,null,12,12,null,12,null,null,12,null,12,null,12,null,null,12,null,null,12,12,null,12,12,null,12,null,12,null,12,12,null,12,null,12,12,null,12,12,12,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,12,null,12,null,12,null,null,null,null,null,null,null,12,12,12,12,null,null,12,null,null,12,null,12,12,null,12,null,12,null,null,12,null,12,null,12,null,12,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,null,null,null,null,12,null,null,12,null,null,12,null,12,12,null,null,12,null,12,null,12,null,12,null,null,null,null,12,null,null,12,null,12,12,12,12,null,12,12,null,12,null,12,null,12,null,null,12,12,null,12,null,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,12,12,12,12,null,12,null,null,12,null,12,null,12,12,12,null,null,null,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,null,12,12,null,12,null,null,null,12,null,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,12,null,null,null,12,null,12,null,12,12,12,12,12,null,12,12,12,12,null,12,null,12,null,12,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,12,null,null,12,null,12,null,12,12,12,null,12,null,null,12,12,null,12,12,12,null,12,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,null,null,12,null,12,null,12,null,null,12,12,12,null,12,null,null,null,12,null,12,null,12,12,null,null,12,null,null,12,null,12,null,12,null,null,null,null,null,null,null,null,null,12,12,null,12,null,12,null,null,12,null,12,null,12,null,null,null,12,null,12,12,null,12,null,12,null,null,12,12,null,12,12,null,null,null,null,12,null,12,null,12,null,12,null,12,12,12,12,null,12,null,12,null,null,12,12,null,12,12,12,null,12,null,12,null,12,null,12,null,12,12,12,12,null,12,null,12,null,null,null,null,null,null,null,null,null,null,null,12,null,null,null,12,12,null,12,12,null,12,12,null,12,12,null,12,null,12,12,12,12,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,null,null,12,12,null,12,null,12,12,12,12,12,null,null,12,null,12,null,12,12,12,12,12,null,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,null,null,12,null,12,null,12,12,null,null,12,12,null,null,null,12,null,12,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,null,12,12,null,12,null,12,12,null,12,null,null,12,null,null,null,12,null,12,null,12,null,12,null,12,12,null,null,12,null,null,12,12,null,12,null,12,null,12,12,null,12,null,12,12,null,12,12,12,12,null,12,null,12,null,12,12,null,12,null,null,12,null,null,12,12,null,null,null,null,null,null,null,null,null,null,null,12,null,null,12,null,12,null,12,null,12,12,null,12,null,12,12,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,13,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,13,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null],"memalloc":[124.5397033691406,124.5397033691406,124.5397033691406,124.5397033691406,139.8219375610352,139.8219375610352,139.8219375610352,139.8219375610352,139.8223037719727,139.8223037719727,139.8223037719727,170.2876815795898,170.2876815795898,170.2876815795898,170.2876815795898,170.2876815795898,170.2876815795898,170.287727355957,170.287727355957,170.287727355957,170.287727355957,170.287727355957,170.287727355957,170.287727355957,170.287727355957,170.287727355957,170.287727355957,170.287727355957,170.287727355957,170.287727355957,170.287727355957,170.287727355957,170.287727355957,170.2874221801758,170.2874221801758,185.6634826660156,185.6634826660156,185.9098739624023,185.9098739624023,186.1983337402344,186.1983337402344,186.4996109008789,186.8211517333984,187.1401443481445,187.1401443481445,187.4570693969727,187.4570693969727,187.7890090942383,187.7890090942383,188.0984420776367,188.4214248657227,188.4214248657227,188.6100997924805,188.6100997924805,188.6100997924805,188.6100997924805,185.7929840087891,185.7929840087891,185.7929840087891,186.1221542358398,186.1221542358398,186.4815139770508,186.867561340332,186.867561340332,187.2695770263672,187.2695770263672,187.6684494018555,187.6684494018555,188.0608749389648,188.4561462402344,188.6745071411133,188.6745071411133,186.0626525878906,186.0626525878906,186.4199447631836,186.4199447631836,186.7919464111328,186.7919464111328,187.1800842285156,187.5707702636719,187.9617004394531,187.9617004394531,188.3387756347656,188.3387756347656,188.726432800293,188.726432800293,185.9745864868164,185.9745864868164,185.9745864868164,186.3039245605469,186.3039245605469,186.660514831543,186.660514831543,187.0343246459961,187.0343246459961,187.4210205078125,187.4210205078125,187.8135452270508,188.1931686401367,188.1931686401367,188.5824966430664,188.5824966430664,188.8367919921875,188.8367919921875,188.8367919921875,186.206298828125,186.5376205444336,186.5376205444336,186.5376205444336,186.9336471557617,186.9336471557617,187.3016204833984,187.6759872436523,188.0550079345703,188.0550079345703,188.4217071533203,188.4217071533203,188.802864074707,188.802864074707,188.9160385131836,188.9160385131836,188.9160385131836,186.4502868652344,186.4502868652344,186.7889556884766,186.7889556884766,187.1546478271484,187.1546478271484,187.5347137451172,187.9205856323242,188.3138275146484,188.3138275146484,188.7132339477539,188.7132339477539,188.9939880371094,188.9939880371094,188.9939880371094,186.470703125,186.8126602172852,186.8126602172852,186.8126602172852,187.1757125854492,187.1757125854492,187.5540618896484,187.5540618896484,187.943244934082,187.943244934082,188.3310699462891,188.3310699462891,188.3310699462891,188.7163772583008,188.7163772583008,189.0705795288086,189.0705795288086,186.5039596557617,186.5039596557617,186.8361434936523,186.8361434936523,187.1931228637695,187.5635528564453,187.9497299194336,187.9497299194336,187.9497299194336,188.3368759155273,188.3368759155273,188.7246780395508,188.7246780395508,189.1224136352539,186.5735244750977,186.5735244750977,186.5735244750977,186.8951721191406,186.8951721191406,186.8951721191406,187.2370452880859,187.5962448120117,187.5962448120117,187.956657409668,187.956657409668,188.3292083740234,188.3292083740234,188.7017440795898,189.0891952514648,189.2202301025391,189.2202301025391,189.2202301025391,186.901237487793,186.901237487793,187.2104644775391,187.2104644775391,187.5348815917969,187.5348815917969,187.8714218139648,187.8714218139648,188.2212905883789,188.5832214355469,188.5832214355469,188.9481430053711,188.9481430053711,189.2933120727539,189.2933120727539,189.2933120727539,186.818489074707,187.1216430664062,187.1216430664062,187.4307022094727,187.4307022094727,187.7546157836914,187.7546157836914,188.0776596069336,188.0776596069336,188.0776596069336,188.4170761108398,188.4170761108398,188.761360168457,189.0803680419922,189.0803680419922,189.365119934082,189.365119934082,189.365119934082,186.9390258789062,187.2789688110352,187.2789688110352,187.6323776245117,187.9947357177734,187.9947357177734,188.3662872314453,188.7375717163086,188.7375717163086,189.1018142700195,189.1018142700195,189.4357681274414,189.4357681274414,189.4357681274414,187.0439224243164,187.0439224243164,187.3976974487305,187.7603912353516,187.7603912353516,188.1215591430664,188.4750671386719,188.4750671386719,188.8581771850586,188.8581771850586,189.2026443481445,189.5053100585938,189.5053100585938,189.5053100585938,187.1641387939453,187.5127410888672,187.8577499389648,187.8577499389648,187.8577499389648,188.2020111083984,188.2020111083984,188.5368194580078,188.8650283813477,189.1920471191406,189.5212936401367,189.5212936401367,189.5737228393555,189.5737228393555,189.5737228393555,187.4413604736328,187.4413604736328,187.7526702880859,187.7526702880859,188.076057434082,188.076057434082,188.4025115966797,188.4025115966797,188.7225799560547,189.0402984619141,189.0402984619141,189.3556289672852,189.3556289672852,189.6409759521484,189.6409759521484,189.6409759521484,187.3313674926758,187.3313674926758,187.5988616943359,187.9090728759766,187.9090728759766,188.2232055664062,188.2232055664062,188.5385360717773,188.8543930053711,189.1593017578125,189.4597320556641,189.4597320556641,189.7071838378906,189.7071838378906,189.7071838378906,187.4670867919922,187.8004913330078,187.8004913330078,188.0995254516602,188.0995254516602,188.0995254516602,188.4058990478516,188.4058990478516,188.7133178710938,189.0187225341797,189.3225860595703,189.3225860595703,189.6226348876953,189.6226348876953,189.772331237793,189.772331237793,189.772331237793,187.647331237793,187.9377899169922,187.9377899169922,188.2329177856445,188.2329177856445,188.2329177856445,188.5399780273438,188.8470611572266,188.8470611572266,189.1508483886719,189.1508483886719,189.1508483886719,189.4524688720703,189.4524688720703,189.7543411254883,189.7543411254883,189.8364105224609,189.8364105224609,189.8364105224609,187.7675323486328,188.0382232666016,188.0382232666016,188.3248062133789,188.3248062133789,188.3248062133789,188.6192932128906,188.9100494384766,188.9100494384766,189.1963653564453,189.1963653564453,189.4813690185547,189.4813690185547,189.4813690185547,189.7704925537109,189.8994522094727,189.8994522094727,187.8360977172852,188.095588684082,188.095588684082,188.3787536621094,188.6782913208008,188.6782913208008,188.9785308837891,189.2842712402344,189.2842712402344,189.5902633666992,189.5902633666992,189.5902633666992,189.8951187133789,189.9615020751953,189.9615020751953,188.0355987548828,188.0355987548828,188.3214340209961,188.3214340209961,188.6352005004883,188.6352005004883,188.9561920166016,188.9561920166016,189.2739944458008,189.5912017822266,189.5912017822266,189.9054718017578,189.9054718017578,190.0225524902344,190.0225524902344,190.0225524902344,190.0225524902344,190.0225524902344,190.0225524902344,190.0225524902344,190.0225524902344,190.0225524902344,190.0225524902344,190.0225524902344,190.0225524902344,190.0225524902344,190.0225524902344,190.0225524902344,190.0225524902344,190.0225524902344,190.0225524902344,190.0225524902344,190.0225524902344,190.0225524902344,190.0225524902344,190.0225524902344,190.0225524902344,187.9682846069336,188.1763534545898,188.1763534545898,188.1763534545898,188.4051666259766,188.4051666259766,188.6513595581055,188.6513595581055,188.9351577758789,189.2799224853516,189.2799224853516,189.6154098510742,189.6154098510742,189.9663619995117,189.9663619995117,190.0823745727539,190.0823745727539,190.0823745727539,188.1827163696289,188.1827163696289,188.4594802856445,188.7722854614258,188.7722854614258,189.1163864135742,189.1163864135742,189.4775695800781,189.4775695800781,189.8426666259766,189.8426666259766,190.1415176391602,190.1415176391602,190.1415176391602,188.1439666748047,188.1439666748047,188.4113616943359,188.4113616943359,188.7049560546875,188.7049560546875,189.0371475219727,189.0371475219727,189.3903656005859,189.3903656005859,189.7510147094727,190.1243133544922,190.1996459960938,190.1996459960938,190.1996459960938,188.4226760864258,188.7101669311523,188.7101669311523,189.0374298095703,189.0374298095703,189.3959503173828,189.3959503173828,189.3959503173828,189.7643051147461,190.1459350585938,190.1459350585938,190.1459350585938,190.2568435668945,190.2568435668945,190.2568435668945,188.4768524169922,188.4768524169922,188.7579650878906,188.7579650878906,189.0744857788086,189.0744857788086,189.4273681640625,189.4273681640625,189.7943344116211,189.7943344116211,190.1713943481445,190.1713943481445,190.1713943481445,190.3131713867188,190.3131713867188,190.3131713867188,188.5375518798828,188.8436508178711,189.1549453735352,189.498176574707,189.498176574707,189.8552017211914,190.2250595092773,190.3685302734375,190.3685302734375,190.3685302734375,188.6119766235352,188.6119766235352,188.8788604736328,188.8788604736328,188.8788604736328,189.1862716674805,189.1862716674805,189.5248260498047,189.8830947875977,189.8830947875977,190.2603454589844,190.2603454589844,190.4230270385742,190.4230270385742,190.4230270385742,188.6922378540039,188.9676971435547,188.9676971435547,189.2818374633789,189.6286849975586,189.6286849975586,189.9902267456055,189.9902267456055,190.3669128417969,190.3669128417969,190.4766006469727,190.4766006469727,190.4766006469727,188.80419921875,188.80419921875,189.0772094726562,189.0772094726562,189.3626480102539,189.6943435668945,189.6943435668945,190.0482788085938,190.0482788085938,190.4127655029297,190.4127655029297,190.5293197631836,190.5293197631836,190.5293197631836,188.8417434692383,189.0958480834961,189.0958480834961,189.3956146240234,189.7342376708984,189.7342376708984,190.0828857421875,190.4303283691406,190.5812530517578,190.5812530517578,190.5812530517578,188.8739013671875,188.8739013671875,189.134162902832,189.134162902832,189.4320907592773,189.4320907592773,189.7415008544922,190.0836791992188,190.4432373046875,190.6322250366211,190.6322250366211,188.9449691772461,189.2007522583008,189.2007522583008,189.4974746704102,189.4974746704102,189.4974746704102,189.8129577636719,189.8129577636719,190.1679458618164,190.1679458618164,190.5320739746094,190.5320739746094,190.682487487793,190.682487487793,190.682487487793,189.0662536621094,189.3406448364258,189.3406448364258,189.6522903442383,189.6522903442383,189.9821853637695,189.9821853637695,190.3310852050781,190.3310852050781,190.6914825439453,190.6914825439453,190.7318725585938,190.7318725585938,189.2029876708984,189.5114212036133,189.5114212036133,189.8190383911133,189.8190383911133,189.8190383911133,190.1659698486328,190.1659698486328,190.5295944213867,190.7804946899414,190.7804946899414,190.7804946899414,189.147087097168,189.147087097168,189.4154281616211,189.4154281616211,189.7197189331055,189.7197189331055,190.0380020141602,190.0380020141602,190.0380020141602,190.3940200805664,190.3940200805664,190.7579574584961,190.7579574584961,190.8283386230469,190.8283386230469,190.8283386230469,189.3402633666992,189.6184158325195,189.6184158325195,189.6184158325195,189.9358978271484,189.9358978271484,190.2773742675781,190.6349258422852,190.8753433227539,190.8753433227539,190.8753433227539,189.29150390625,189.29150390625,189.5399703979492,189.5399703979492,189.8265075683594,189.8265075683594,190.1512756347656,190.1512756347656,190.4968032836914,190.4968032836914,190.852653503418,190.852653503418,190.9216384887695,190.9216384887695,190.9216384887695,189.4771575927734,189.7659912109375,190.0716171264648,190.0716171264648,190.4087600708008,190.4087600708008,190.7621002197266,190.7621002197266,190.9672317504883,190.9672317504883,189.4700012207031,189.4700012207031,189.7181930541992,190.0083618164062,190.0083618164062,190.3396606445312,190.3396606445312,190.6925811767578,190.6925811767578,191.0119705200195,191.0119705200195,191.0119705200195,191.0119705200195,191.0119705200195,191.0119705200195,189.7081985473633,189.9884567260742,189.9884567260742,190.3094482421875,190.3094482421875,190.6517333984375,191.0048675537109,191.0560989379883,191.0560989379883,189.6999435424805,189.6999435424805,189.969123840332,189.969123840332,190.2769012451172,190.2769012451172,190.6206970214844,190.6206970214844,190.9786834716797,190.9786834716797,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,191.0995178222656,189.6059036254883,189.6059036254883,189.6059036254883,189.6059036254883,189.6059036254883,189.6059036254883,189.762321472168,190.0088424682617,190.0088424682617,190.2686767578125,190.2686767578125,190.5636672973633,190.5636672973633,190.869987487793,191.1820526123047,191.1820526123047,191.5216064453125,191.5216064453125,191.8899002075195,191.8899002075195,192.2898330688477,192.2898330688477,192.2898330688477,192.6483306884766,192.6483306884766,192.9759979248047,193.3069076538086,193.3069076538086,193.6362609863281,193.6362609863281,193.6362609863281,193.9659881591797,193.9659881591797,193.9659881591797,194.296257019043,194.296257019043,194.4439544677734,194.4439544677734,194.4439544677734,189.9166946411133,189.9166946411133,190.2268218994141,190.2268218994141,190.568489074707,190.9104690551758,190.9104690551758,191.2420806884766,191.2420806884766,191.6112670898438,191.9899444580078,191.9899444580078,192.3760681152344,192.7712173461914,192.7712173461914,193.1818466186523,193.6285552978516,193.6285552978516,194.0314331054688,194.4217681884766,194.576301574707,194.576301574707,194.576301574707,190.0981597900391,190.0981597900391,190.3811416625977,190.3811416625977,190.6995239257812,190.6995239257812,191.024284362793,191.024284362793,191.024284362793,191.3521194458008,191.7142562866211,191.7142562866211,191.7142562866211,192.0864181518555,192.0864181518555,192.4675521850586,192.8589324951172,193.2572250366211,193.2572250366211,193.6540374755859,194.0537033081055,194.0537033081055,194.4488525390625,194.7064743041992,194.7064743041992,194.7064743041992,194.7064743041992,190.2293395996094,190.2293395996094,190.2293395996094,190.5025939941406,190.5025939941406,190.8059310913086,191.1211318969727,191.1211318969727,191.4455413818359,191.4455413818359,191.8042678833008,191.8042678833008,192.1642913818359,192.1642913818359,192.5405120849609,192.5405120849609,192.9265975952148,192.9265975952148,193.3165054321289,193.3165054321289,193.3165054321289,193.7153472900391,193.7153472900391,194.1156463623047,194.1156463623047,194.5151672363281,194.5151672363281,194.5151672363281,194.8345718383789,194.8345718383789,194.8345718383789,194.8345718383789,194.8345718383789,194.8345718383789,190.647819519043,190.647819519043,190.9375228881836,190.9375228881836,191.2407684326172,191.2407684326172,191.2407684326172,191.592643737793,191.9505462646484,192.3097457885742,192.3097457885742,192.6853408813477,193.0610275268555,193.0610275268555,193.4473724365234,193.4473724365234,193.8365859985352,193.8365859985352,194.2296447753906,194.2296447753906,194.5972747802734,194.5972747802734,194.9459381103516,194.9459381103516,194.960578918457,194.960578918457,190.7292861938477,190.7292861938477,190.7292861938477,190.9943008422852,191.2883758544922,191.2883758544922,191.5856399536133,191.5856399536133,191.9310989379883,192.2854156494141,192.2854156494141,192.6539077758789,192.6539077758789,193.0301361083984,193.0301361083984,193.0301361083984,193.4138717651367,193.4138717651367,193.8048324584961,194.2010726928711,194.2010726928711,194.610107421875,194.610107421875,194.9960327148438,195.0845947265625,195.0845947265625,195.0845947265625,190.9084320068359,190.9084320068359,191.1836318969727,191.1836318969727,191.4711837768555,191.4711837768555,191.7735290527344,191.7735290527344,192.1176605224609,192.1176605224609,192.4705810546875,192.836784362793,192.836784362793,193.2082748413086,193.5886840820312,193.5886840820312,193.9778442382812,193.9778442382812,194.410758972168,194.410758972168,194.8196640014648,194.8196640014648,195.2005615234375,195.20654296875,195.20654296875,195.20654296875,191.1721801757812,191.4591979980469,191.4591979980469,191.7446823120117,191.7446823120117,192.0808944702148,192.0808944702148,192.4338150024414,192.4338150024414,192.4338150024414,192.797233581543,192.797233581543,193.1666412353516,193.5412292480469,193.5412292480469,193.9275054931641,194.3173522949219,194.3173522949219,194.7207794189453,194.7207794189453,195.1164703369141,195.1164703369141,195.3265380859375,195.3265380859375,195.3265380859375,191.2085571289062,191.4714660644531,191.7480392456055,191.7480392456055,192.0474243164062,192.0474243164062,192.383659362793,192.383659362793,192.7340393066406,192.7340393066406,192.7340393066406,193.0815277099609,193.4386215209961,193.8053359985352,193.8053359985352,194.1799545288086,194.1799545288086,194.5675964355469,194.5675964355469,194.9548568725586,194.9548568725586,195.3511352539062,195.4446258544922,195.4446258544922,195.4446258544922,195.4446258544922,191.4611206054688,191.4611206054688,191.7274703979492,191.7274703979492,191.9485702514648,192.0780715942383,192.2830429077148,192.2830429077148,192.4676742553711,192.4676742553711,192.7501449584961,192.7501449584961,192.9593124389648,192.9593124389648,193.2579879760742,193.2579879760742,193.578254699707,193.578254699707,193.8681716918945,194.1924743652344,194.5407104492188,194.5407104492188,194.8809509277344,195.2441024780273,195.5607681274414,195.5607681274414,195.5607681274414,195.5607681274414,195.5607681274414,195.5607681274414,191.72607421875,191.72607421875,192.0140686035156,192.0140686035156,192.2879867553711,192.2879867553711,192.5782318115234,192.9094619750977,193.2525405883789,193.2525405883789,193.5988082885742,193.9611358642578,193.9611358642578,194.327522277832,194.327522277832,194.6523056030273,194.6523056030273,194.9765853881836,194.9765853881836,195.3190994262695,195.6750335693359,195.6750335693359,195.6750335693359,195.6750335693359,191.7796478271484,192.0186920166016,192.0186920166016,192.2499465942383,192.2499465942383,192.5238418579102,192.8348159790039,192.8348159790039,192.8348159790039,193.1687393188477,193.1687393188477,193.1687393188477,193.474609375,193.474609375,193.474609375,193.8344879150391,193.8344879150391,194.1887588500977,194.1887588500977,194.5088272094727,194.5088272094727,194.8173217773438,194.8173217773438,195.1886215209961,195.1886215209961,195.5393981933594,195.7875366210938,195.7875366210938,195.7875366210938,195.7875366210938,195.7875366210938,195.7875366210938,191.9985961914062,192.2392196655273,192.2392196655273,192.5128555297852,192.8309783935547,192.8309783935547,193.1523971557617,193.1523971557617,193.4787292480469,193.8357162475586,193.8357162475586,194.1839370727539,194.5611419677734,194.5611419677734,194.9514465332031,195.3456954956055,195.3456954956055,195.3456954956055,195.7345428466797,195.7345428466797,195.8980941772461,195.8980941772461,195.8980941772461,192.121223449707,192.121223449707,192.3692169189453,192.3692169189453,192.5957107543945,192.5957107543945,192.8842468261719,193.1775970458984,193.1775970458984,193.5085678100586,193.5085678100586,193.8554763793945,193.8554763793945,194.1945266723633,194.1945266723633,194.5342483520508,194.8977661132812,194.8977661132812,195.2796325683594,195.2796325683594,195.6477661132812,195.6477661132812,196.006965637207,196.006965637207,196.006965637207,196.006965637207,196.006965637207,196.006965637207,192.3785705566406,192.6214294433594,192.6214294433594,192.900993347168,192.900993347168,193.2063369750977,193.2063369750977,193.5288543701172,193.5288543701172,193.8710098266602,193.8710098266602,194.2256317138672,194.5668182373047,194.5668182373047,194.9342651367188,194.9342651367188,195.3181610107422,195.3181610107422,195.6936798095703,195.6936798095703,196.0722274780273,196.0722274780273,196.1140594482422,196.1140594482422,192.5386962890625,192.5386962890625,192.7739486694336,192.7739486694336,193.0560073852539,193.3708114624023,193.6806335449219,194.0249862670898,194.3794479370117,194.7299957275391,194.7299957275391,195.100830078125,195.100830078125,195.4871597290039,195.4871597290039,195.8639068603516,195.8639068603516,196.2194366455078,196.2194366455078,196.2194366455078,196.2194366455078,196.2194366455078,196.2194366455078,192.7205276489258,192.7205276489258,192.9286422729492,192.9286422729492,192.9286422729492,193.1875228881836,193.4754028320312,193.4754028320312,193.7517852783203,193.7517852783203,194.0621948242188,194.0621948242188,194.3964614868164,194.744987487793,194.744987487793,194.744987487793,195.0963363647461,195.4727783203125,195.8655700683594,195.8655700683594,195.8655700683594,196.2542495727539,196.2542495727539,196.3230819702148,196.3230819702148,192.8559494018555,192.8559494018555,193.1008911132812,193.1008911132812,193.1008911132812,193.3758392333984,193.3758392333984,193.6816253662109,194.0138778686523,194.0138778686523,194.3635787963867,194.3635787963867,194.7275543212891,194.7275543212891,195.1054916381836,195.500358581543,195.500358581543,195.9037628173828,195.9037628173828,196.3012542724609,196.3012542724609,196.4251022338867,196.4251022338867,196.4251022338867,196.4251022338867,192.9556732177734,192.9556732177734,193.1975708007812,193.4690093994141,193.4690093994141,193.7652130126953,193.7652130126953,194.0890274047852,194.4393920898438,194.7992248535156,195.169548034668,195.5494079589844,195.5494079589844,195.5494079589844,195.9406967163086,195.9406967163086,196.3329391479492,196.3329391479492,196.5254058837891,196.5254058837891,196.5254058837891,196.5254058837891,196.5254058837891,196.5254058837891,196.5254058837891,196.5254058837891,193.3104782104492,193.3104782104492,193.5748977661133,193.5748977661133,193.860237121582,193.860237121582,194.1789245605469,194.1789245605469,194.5209045410156,194.5209045410156,194.8746490478516,194.8746490478516,195.2454681396484,195.2454681396484,195.2454681396484,195.667366027832,196.0675506591797,196.0675506591797,196.4640274047852,196.6241607666016,196.6241607666016,196.6241607666016,193.2431869506836,193.2431869506836,193.4804458618164,193.4804458618164,193.7408599853516,194.0220794677734,194.0220794677734,194.333854675293,194.6759719848633,195.0307464599609,195.0307464599609,195.0307464599609,195.3941268920898,195.3941268920898,195.76806640625,195.76806640625,196.154670715332,196.154670715332,196.543342590332,196.543342590332,196.7212677001953,196.7212677001953,196.7212677001953,196.7212677001953,196.7212677001953,196.7212677001953,196.7212677001953,196.7212677001953,196.7212677001953,196.7212677001953,196.7212677001953,196.7212677001953,196.7212677001953,196.7212677001953,196.7212677001953,196.7212677001953,196.7212677001953,196.7212677001953,196.7212677001953,196.7212677001953,196.7212677001953,196.7212677001953,196.7212677001953,196.7212677001953,196.7212677001953,196.7212677001953,196.7212677001953,196.7212677001953,196.7212677001953,196.7212677001953,196.7212677001953,196.7212677001953,196.7212677001953,196.7212677001953,196.7212677001953,196.7212677001953,196.7212677001953,196.7212677001953,196.7212677001953,193.4728240966797,193.6414566040039,193.8510818481445,193.8510818481445,194.0813293457031,194.0813293457031,194.0813293457031,194.3140335083008,194.3140335083008,194.5786743164062,194.8792114257812,194.8792114257812,195.2018127441406,195.4614715576172,195.4614715576172,195.7837753295898,195.7837753295898,196.1168975830078,196.4251403808594,196.764030456543,196.764030456543,196.8166732788086,196.8166732788086,196.8166732788086,193.5643005371094,193.7895812988281,193.7895812988281,194.0304718017578,194.3005294799805,194.3005294799805,194.5858535766602,194.9050445556641,195.2372817993164,195.2372817993164,195.5632553100586,195.908088684082,195.908088684082,196.2665634155273,196.6326217651367,196.6326217651367,196.910774230957,196.910774230957,196.910774230957,196.910774230957,196.910774230957,196.910774230957,193.8047714233398,193.8047714233398,194.0281753540039,194.0281753540039,194.2796478271484,194.2796478271484,194.5631942749023,194.5631942749023,194.8667678833008,194.8667678833008,195.2010803222656,195.2010803222656,195.545166015625,195.545166015625,195.545166015625,195.8901443481445,195.8901443481445,196.0221099853516,196.0221099853516,196.2532119750977,196.2532119750977,196.2532119750977,196.5591049194336,196.5591049194336,196.7775726318359,196.7775726318359,197.0033493041992,197.0033493041992,197.0033493041992,197.0033493041992,197.0033493041992,197.0033493041992,193.8450164794922,194.0545883178711,194.0545883178711,194.2858581542969,194.2858581542969,194.5372695922852,194.5372695922852,194.8264770507812,194.8264770507812,195.1495056152344,195.1495056152344,195.4890518188477,195.8430480957031,195.8430480957031,196.2092056274414,196.5942687988281,196.9845352172852,197.0943222045898,197.0943222045898,197.0943222045898,193.9990692138672,193.9990692138672,194.2273406982422,194.2273406982422,194.4983978271484,194.7797393798828,195.0941925048828,195.0941925048828,195.4318771362305,195.7807083129883,195.7807083129883,196.1449584960938,196.1449584960938,196.5219879150391,196.9081039428711,196.9081039428711,197.183952331543,197.183952331543,197.183952331543,197.183952331543,197.183952331543,197.183952331543,194.230354309082,194.4677276611328,194.4677276611328,194.7279968261719,194.7279968261719,195.0187149047852,195.0187149047852,195.3433532714844,195.3433532714844,195.6918258666992,195.6918258666992,196.050163269043,196.050163269043,196.4174194335938,196.4174194335938,196.8019104003906,196.8019104003906,197.1875839233398,197.1875839233398,197.2720260620117,197.2720260620117,197.2720260620117,194.2645034790039,194.2645034790039,194.4932327270508,194.7372131347656,194.7372131347656,195.0077743530273,195.3176803588867,195.3176803588867,195.6558227539062,195.6558227539062,196.006477355957,196.006477355957,196.3717498779297,196.3717498779297,196.7479705810547,196.7479705810547,197.1357727050781,197.1357727050781,197.3588027954102,197.3588027954102,197.3588027954102,197.3588027954102,194.5706100463867,194.5706100463867,194.7999649047852,194.7999649047852,195.0509033203125,195.3395004272461,195.3395004272461,195.6238250732422,195.9545669555664,195.9545669555664,196.2989883422852,196.6557998657227,197.0170364379883,197.0170364379883,197.3943099975586,197.3943099975586,197.4440231323242,197.4440231323242,197.4440231323242,194.5320358276367,194.5320358276367,194.5320358276367,194.7555847167969,194.7555847167969,194.9973907470703,194.9973907470703,195.2585220336914,195.2585220336914,195.5324249267578,195.5324249267578,195.5324249267578,195.8409576416016,196.1710205078125,196.1710205078125,196.5075454711914,196.5075454711914,196.5075454711914,196.8150482177734,197.197509765625,197.197509765625,197.5279846191406,197.5279846191406,197.5279846191406,197.5279846191406,197.5279846191406,197.5279846191406,194.8026123046875,194.8026123046875,195.0224761962891,195.0224761962891,195.2068786621094,195.4622192382812,195.4622192382812,195.4622192382812,195.757942199707,196.0532608032227,196.0532608032227,196.3690719604492,196.3690719604492,196.700927734375,196.700927734375,197.0246353149414,197.0246353149414,197.3517532348633,197.3517532348633,197.3517532348633,197.6105651855469,197.6105651855469,197.6105651855469,197.6105651855469,197.6105651855469,197.6105651855469,194.8442840576172,194.8442840576172,195.0887756347656,195.0887756347656,195.3917999267578,195.3917999267578,195.6897430419922,195.6897430419922,196.0173568725586,196.0173568725586,196.3595199584961,196.3595199584961,196.6973876953125,197.0368804931641,197.0368804931641,197.3836212158203,197.3836212158203,197.6917572021484,197.6917572021484,197.6917572021484,197.6917572021484,197.6917572021484,197.6917572021484,197.6917572021484,197.6917572021484,194.9462051391602,195.192024230957,195.192024230957,195.4527359008789,195.4527359008789,195.7506942749023,196.0713424682617,196.0713424682617,196.4089660644531,196.4089660644531,196.7477874755859,196.7477874755859,197.0997924804688,197.0997924804688,197.4648056030273,197.4648056030273,197.7716751098633,197.7716751098633,197.7716751098633,197.7716751098633,197.7716751098633,197.7716751098633,195.086669921875,195.086669921875,195.3072814941406,195.3072814941406,195.561882019043,195.561882019043,195.8356552124023,195.8356552124023,196.1252975463867,196.4537887573242,196.7975692749023,196.7975692749023,197.1499404907227,197.1499404907227,197.5154190063477,197.8502731323242,197.8502731323242,197.8502731323242,197.8502731323242,197.8502731323242,197.8502731323242,195.2234497070312,195.4495620727539,195.6876831054688,195.6876831054688,195.9582824707031,195.9582824707031,196.264778137207,196.5994720458984,196.5994720458984,196.9462661743164,196.9462661743164,197.2996444702148,197.2996444702148,197.6677551269531,197.6677551269531,197.9276504516602,197.9276504516602,197.9276504516602,197.9276504516602,197.9276504516602,197.9276504516602,195.3994216918945,195.3994216918945,195.6268157958984,195.8719940185547,195.8719940185547,196.1488876342773,196.1488876342773,196.1488876342773,196.4581146240234,196.7949752807617,196.7949752807617,197.1447525024414,197.5021438598633,197.5021438598633,197.8737869262695,197.8737869262695,198.0037078857422,198.0037078857422,198.0037078857422,198.0037078857422,195.5957794189453,195.5957794189453,195.8277435302734,195.8277435302734,196.0806274414062,196.0806274414062,196.3698120117188,196.3698120117188,196.690299987793,197.0353698730469,197.3907775878906,197.7560501098633,198.07861328125,198.07861328125,198.07861328125,198.07861328125,198.07861328125,198.07861328125,195.5924987792969,195.8177795410156,195.8177795410156,196.0556869506836,196.3227996826172,196.3227996826172,196.6291427612305,196.965202331543,196.965202331543,197.3171844482422,197.3171844482422,197.6760482788086,197.6760482788086,198.0410232543945,198.0410232543945,198.1522903442383,198.1522903442383,198.1522903442383,198.1522903442383,198.1522903442383,198.1522903442383,195.8325347900391,195.8325347900391,196.0659255981445,196.0659255981445,196.0659255981445,196.319465637207,196.319465637207,196.6118774414062,196.9399719238281,196.9399719238281,197.2863998413086,197.2863998413086,197.6731185913086,197.6731185913086,198.0332107543945,198.0332107543945,198.2247848510742,198.2247848510742,198.2247848510742,198.2247848510742,195.8730316162109,196.099983215332,196.3423767089844,196.3423767089844,196.6218948364258,196.6218948364258,196.9348373413086,197.2733383178711,197.6245651245117,197.6245651245117,197.9883270263672,197.9883270263672,198.2960662841797,198.2960662841797,198.2960662841797,198.2960662841797,195.9037704467773,196.1235733032227,196.1235733032227,196.3577194213867,196.3577194213867,196.6194686889648,196.6194686889648,196.9165496826172,196.9165496826172,197.2450408935547,197.5945892333984,197.9522094726562,198.3189544677734,198.3189544677734,198.3662796020508,198.3662796020508,195.9772644042969,195.9772644042969,196.1990280151367,196.1990280151367,196.1990280151367,196.4350128173828,196.7335662841797,197.0436859130859,197.3803176879883,197.3803176879883,197.7305679321289,197.7305679321289,198.0924530029297,198.4353332519531,198.4353332519531,198.4353332519531,198.4353332519531,198.4353332519531,198.4353332519531,198.4353332519531,198.4353332519531,198.4353332519531,198.4353332519531,198.4353332519531,198.4353332519531,198.4353332519531,198.4353332519531,198.4353332519531,198.4353332519531,198.4353332519531,198.4353332519531,198.4353332519531,198.4353332519531,198.4353332519531,198.4353332519531,196.0588302612305,196.0588302612305,196.1482543945312,196.1482543945312,196.3348007202148,196.3348007202148,196.5564575195312,196.5564575195312,196.7965316772461,196.7965316772461,197.0589752197266,197.0589752197266,197.3576354980469,197.6784820556641,198.0105819702148,198.0105819702148,198.4064865112305,198.4064865112305,198.4064865112305,198.503059387207,198.503059387207,198.503059387207,198.503059387207,196.3586502075195,196.5898742675781,196.5898742675781,196.8512649536133,197.1494750976562,197.1494750976562,197.1494750976562,197.4778594970703,197.8282165527344,197.8282165527344,198.1890335083008,198.1890335083008,198.5561065673828,198.5561065673828,198.5699462890625,198.5699462890625,198.5699462890625,196.3041534423828,196.3041534423828,196.5246047973633,196.7602005004883,196.7602005004883,197.0239410400391,197.326904296875,197.6608123779297,198.0104675292969,198.3724899291992,198.3724899291992,198.6357040405273,198.6357040405273,198.6357040405273,198.6357040405273,198.6357040405273,198.6357040405273,196.4859466552734,196.7124862670898,196.7124862670898,196.9562225341797,197.2378082275391,197.2378082275391,197.5580596923828,197.5580596923828,197.9371337890625,198.2913513183594,198.2913513183594,198.6603927612305,198.6603927612305,198.7004013061523,198.7004013061523,198.7004013061523,196.5071716308594,196.5071716308594,196.5071716308594,196.7262115478516,196.9630584716797,196.9630584716797,197.2347412109375,197.5431594848633,197.5431594848633,197.8827667236328,197.8827667236328,198.2310409545898,198.2310409545898,198.5951385498047,198.7641220092773,198.7641220092773,198.7641220092773,198.7641220092773,196.7088623046875,196.9386596679688,196.9386596679688,197.1919479370117,197.4842147827148,197.8113708496094,198.1608657836914,198.1608657836914,198.5165634155273,198.5165634155273,198.8267822265625,198.8267822265625,198.8267822265625,198.8267822265625,196.7472305297852,196.7472305297852,196.971305847168,196.971305847168,196.971305847168,197.2116928100586,197.2116928100586,197.5203628540039,197.5203628540039,197.8382034301758,198.1803283691406,198.1803283691406,198.5346603393555,198.5346603393555,198.8883972167969,198.8883972167969,198.8883972167969,198.8883972167969,198.8883972167969,198.8883972167969,196.8074645996094,196.8074645996094,197.025749206543,197.2624664306641,197.5323028564453,197.8405151367188,197.8405151367188,197.8405151367188,198.1767196655273,198.1767196655273,198.1767196655273,198.5278930664062,198.5278930664062,198.8853378295898,198.9491424560547,198.9491424560547,196.8633346557617,196.8633346557617,197.082633972168,197.082633972168,197.082633972168,197.3151321411133,197.3151321411133,197.581901550293,197.581901550293,197.8833084106445,197.8833084106445,198.2178955078125,198.5701370239258,198.5701370239258,198.9381637573242,199.0087051391602,199.0087051391602,199.0087051391602,199.0087051391602,197.1703948974609,197.1703948974609,197.4299850463867,197.4299850463867,197.7005233764648,197.7005233764648,198.0126953125,198.0126953125,198.349983215332,198.349983215332,198.703727722168,198.703727722168,199.0674819946289,199.0674819946289,199.0674819946289,199.0674819946289,199.0674819946289,199.0674819946289,197.0801849365234,197.0801849365234,197.2851943969727,197.5220413208008,197.5220413208008,197.5220413208008,197.7919692993164,197.7919692993164,198.1005859375,198.1005859375,198.4359130859375,198.4359130859375,198.7907409667969,198.7907409667969,199.1251831054688,199.1251831054688,199.1251831054688,199.1251831054688,199.1251831054688,199.1251831054688,197.1914596557617,197.1914596557617,197.4156951904297,197.6562728881836,197.9337692260742,198.2404327392578,198.2404327392578,198.5755920410156,198.9254913330078,198.9254913330078,199.1820373535156,199.1820373535156,199.1820373535156,199.1820373535156,197.2865295410156,197.2865295410156,197.2865295410156,197.5166244506836,197.7605056762695,197.7605056762695,198.042839050293,198.042839050293,198.042839050293,198.3591918945312,198.3591918945312,198.704719543457,198.704719543457,199.0637283325195,199.0637283325195,199.2378616333008,199.2378616333008,199.2378616333008,199.2378616333008,199.2378616333008,199.2378616333008,197.4589233398438,197.4589233398438,197.6873397827148,197.9419937133789,197.9419937133789,198.2336654663086,198.5598754882812,198.9106521606445,199.273307800293,199.273307800293,199.2929534912109,199.2929534912109,199.2929534912109,197.4149856567383,197.4149856567383,197.6194000244141,197.6194000244141,197.8578414916992,198.1304626464844,198.4420547485352,198.4420547485352,198.7826461791992,198.7826461791992,199.1404266357422,199.1404266357422,199.3469848632812,199.3469848632812,199.3469848632812,199.3469848632812,199.3469848632812,199.3469848632812,199.3469848632812,199.3469848632812,199.3469848632812,199.3469848632812,199.3469848632812,199.3469848632812,199.3469848632812,199.3469848632812,199.3469848632812,199.3469848632812,199.3469848632812,199.3469848632812,197.5505599975586,197.5505599975586,197.7483215332031,197.7483215332031,197.9778289794922,198.2277297973633,198.2277297973633,198.5123519897461,198.5123519897461,198.8307037353516,198.8307037353516,199.1677703857422,199.1677703857422,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,199.3999557495117,197.5679473876953,197.5679473876953,197.5679473876953,197.5679473876953,197.5882339477539,197.5882339477539,197.8265686035156,197.8265686035156,198.0732498168945,198.3331451416016,198.3331451416016,198.628173828125,198.9513549804688,198.9513549804688,199.2480773925781,199.2480773925781,199.5758666992188,199.5758666992188,199.9426345825195,199.9426345825195,200.3259048461914,200.6789627075195,201.0222015380859,201.33447265625,201.6437149047852,201.6437149047852,201.9427490234375,202.2400207519531,202.5431518554688,202.8563995361328,202.8563995361328,203.1797790527344,203.1797790527344,203.534782409668,203.534782409668,203.8536758422852,204.1681213378906,204.1681213378906,204.4783020019531,204.7832794189453,204.7832794189453,205.0980834960938,205.0980834960938,205.1819610595703,205.1819610595703,205.1819610595703,205.1819610595703,197.9478912353516,197.9478912353516,198.2216339111328,198.2216339111328,198.5242080688477,198.8588104248047,198.8588104248047,199.1927261352539,199.1927261352539,199.4975051879883,199.4975051879883,199.8460388183594,199.8460388183594,200.1918792724609,200.1918792724609,200.5390319824219,200.8944931030273,200.8944931030273,200.8944931030273,201.2522811889648,201.2522811889648,201.6007766723633,201.6007766723633,201.9547653198242,202.3016128540039,202.6503295898438,202.6503295898438,202.9266815185547,202.9266815185547,202.9266815185547,203.2153854370117,203.5755844116211,203.5755844116211,203.9338912963867,204.2944946289062,204.6800308227539,204.6800308227539,205.0343017578125,205.3901824951172,205.3901824951172,205.3901824951172,205.3901824951172,205.3901824951172,205.3901824951172,205.3901824951172,205.3901824951172,205.3901824951172,198.3775787353516,198.3775787353516,198.6295471191406,198.6295471191406,198.9015579223633,198.9015579223633,199.1998443603516,199.1998443603516,199.5019760131836,199.5019760131836,199.8095855712891,199.8095855712891,200.1444396972656,200.1444396972656,200.4953689575195,200.4953689575195,200.4953689575195,200.8612823486328,201.2461013793945,201.6364822387695,201.6364822387695,202.0325622558594,202.0325622558594,202.4333190917969,202.4333190917969,202.8408279418945,202.8408279418945,203.2454071044922,203.2454071044922,203.6527557373047,204.0578842163086,204.0578842163086,204.0578842163086,204.4535980224609,204.4535980224609,204.4535980224609,204.8479156494141,204.8479156494141,205.2317962646484,205.2317962646484,205.5950546264648,205.5950546264648,205.5950546264648,205.5950546264648,205.5950546264648,205.5950546264648,205.5950546264648,205.5950546264648,205.5950546264648,198.7175216674805,198.9664154052734,199.2327194213867,199.2327194213867,199.5191345214844,199.5191345214844,199.8112869262695,199.8112869262695,199.8112869262695,200.1362686157227,200.1362686157227,200.4877319335938,200.4877319335938,200.8502807617188,200.8502807617188,201.2341995239258,201.2341995239258,201.6284942626953,201.6284942626953,202.0286483764648,202.4300689697266,202.4300689697266,202.8347320556641,202.8347320556641,203.2127304077148,203.2127304077148,203.2127304077148,203.6086349487305,204.0046539306641,204.0046539306641,204.3991546630859,204.8035736083984,204.8035736083984,205.2117385864258,205.2117385864258,205.2117385864258,205.5988159179688,205.5988159179688,205.7966461181641,205.7966461181641,205.7966461181641,205.7966461181641,198.8716812133789,198.8716812133789,199.1114349365234,199.3641204833984,199.6329498291016,199.9152450561523,199.9152450561523,200.2258529663086,200.2258529663086,200.5710067749023,200.5710067749023,200.5710067749023,200.9308776855469,201.3451995849609,201.3451995849609,201.7360305786133,202.1227111816406,202.4926147460938,202.4926147460938,202.8553237915039,202.8553237915039,203.2180328369141,203.2180328369141,203.5797576904297,203.5797576904297,203.9411697387695,203.9411697387695,204.3073883056641,204.6768951416016,205.0457077026367,205.4087448120117,205.4087448120117,205.7541961669922,205.7541961669922,205.9949645996094,205.9949645996094,205.9949645996094,205.9949645996094,205.9949645996094,205.9949645996094,205.9949645996094,205.9949645996094,205.9949645996094,199.4613647460938,199.4613647460938,199.4613647460938,199.7940673828125,199.7940673828125,200.1227035522461,200.1227035522461,200.4680404663086,200.8484878540039,200.8484878540039,201.2250442504883,201.581672668457,201.581672668457,201.9369049072266,202.2900695800781,202.2900695800781,202.6500854492188,202.9919128417969,202.9919128417969,203.3351440429688,203.3351440429688,203.6835327148438,204.0409851074219,204.3959655761719,204.7469177246094,205.1002731323242,205.1002731323242,205.4931640625,205.4931640625,205.8358688354492,205.8358688354492,206.1768035888672,206.190055847168,206.190055847168,206.190055847168,206.190055847168,199.6564483642578,199.6564483642578,199.9790115356445,199.9790115356445,200.3043594360352,200.3043594360352,200.6409301757812,200.6409301757812,201.0132293701172,201.3949356079102,201.3949356079102,201.7660369873047,201.7660369873047,202.1231155395508,202.4789352416992,202.8312377929688,203.1863250732422,203.5327377319336,203.5327377319336,203.5327377319336,203.8805465698242,203.8805465698242,204.230598449707,204.230598449707,204.5856628417969,204.9480590820312,205.3006362915039,205.6535949707031,206.0078353881836,206.0078353881836,206.3466644287109,206.3466644287109,206.3820648193359,206.3820648193359,206.3820648193359,206.3820648193359,206.3820648193359,206.3820648193359,206.3820648193359,206.3820648193359,206.3820648193359,206.3820648193359,206.3820648193359,206.3820648193359,206.3820648193359,206.3820648193359,199.8943176269531,200.1665725708008,200.1665725708008,200.4592666625977,200.4592666625977,200.7677612304688,200.7677612304688,201.1236267089844,201.1236267089844,201.4898452758789,201.4898452758789,201.8736572265625,201.8736572265625,202.2628173828125,202.2628173828125,202.6434097290039,202.6434097290039,203.0107498168945,203.372184753418,203.372184753418,203.372184753418,203.7338943481445,204.0939407348633,204.0939407348633,204.4562530517578,204.4562530517578,204.8173980712891,204.8173980712891,205.1692810058594,205.5284118652344,205.5284118652344,205.8873291015625,206.2343521118164,206.2343521118164,206.570915222168,206.570915222168,206.570915222168,206.570915222168,206.570915222168,206.570915222168,200.2206420898438,200.2206420898438,200.5319976806641,200.5319976806641,200.8411407470703,200.8411407470703,201.1910552978516,201.1910552978516,201.5537567138672,201.5537567138672,201.9238815307617,202.2858200073242,202.2858200073242,202.6444931030273,202.6444931030273,203.057991027832,203.4566116333008,203.4566116333008,203.8447799682617,203.8447799682617,203.8447799682617,204.2295913696289,204.2295913696289,204.6205291748047,204.6205291748047,205.0164184570312,205.0164184570312,205.4156265258789,205.4156265258789,205.8202972412109,205.8202972412109,206.2279052734375,206.2279052734375,206.6129608154297,206.7567901611328,206.7567901611328,206.7567901611328,206.7567901611328,206.7567901611328,206.7567901611328,200.3768997192383,200.6201782226562,200.6201782226562,200.8668975830078,200.8668975830078,201.1137771606445,201.1137771606445,201.3971710205078,201.6951293945312,201.6951293945312,201.9833068847656,201.9833068847656,202.2819900512695,202.589729309082,202.589729309082,202.9213256835938,203.2679901123047,203.6301040649414,204.0517883300781,204.0517883300781,204.4406433105469,204.4406433105469,204.8254623413086,204.8254623413086,205.2122650146484,205.5922927856445,205.5922927856445,205.9723815917969,205.9723815917969,205.9723815917969,206.3510589599609,206.3510589599609,206.3510589599609,206.7051467895508,206.9396286010742,206.9396286010742,206.9396286010742,206.9396286010742,206.9396286010742,206.9396286010742,206.9396286010742,206.9396286010742,206.9396286010742,200.7642440795898,200.7642440795898,200.7642440795898,201.0051727294922,201.0051727294922,201.0051727294922,201.2567977905273,201.2567977905273,201.5451278686523,201.5451278686523,201.8727188110352,201.8727188110352,202.2152328491211,202.5698852539062,202.5698852539062,202.921012878418,202.921012878418,203.2751770019531,203.6219177246094,203.9685897827148,203.9685897827148,204.3136138916016,204.3136138916016,204.3136138916016,211.9981536865234,211.9981536865234,211.9981536865234,211.9981536865234,211.9981536865234,211.9981536865234,211.9981536865234,211.9981536865234,211.9981536865234,211.9981536865234,211.9981536865234,211.9981536865234,211.9981536865234,211.9981536865234,211.9981536865234,211.9981536865234,211.9981536865234,211.9981536865234,219.6275482177734,219.627555847168,219.627555847168,219.627555847168,219.627555847168,219.627555847168,219.627555847168,219.627555847168,219.627555847168,219.627555847168,219.627555847168,219.627555847168,219.627555847168,219.627555847168,219.627555847168,219.627555847168,219.627555847168,219.627555847168,219.627555847168,219.627555847168,219.627555847168,219.627555847168,219.627555847168,234.886344909668,234.886344909668,234.886344909668,234.886344909668,234.886344909668,234.886344909668,234.886344909668,234.886344909668,234.886344909668,234.886344909668,234.886344909668,234.886344909668,234.886344909668,234.886344909668,234.886344909668,234.886344909668,242.5157623291016,242.5157623291016,242.5157623291016,242.5157623291016,242.5157623291016,242.5157623291016,242.5157623291016,242.5157623291016,242.6303176879883,242.6303176879883,242.6303176879883,242.6303176879883,242.6303176879883,242.6303176879883,242.6303176879883,242.6303176879883,242.6303176879883,242.6303176879883,242.6303176879883,242.6303176879883,242.6303176879883,242.6303176879883,242.6303176879883,242.6303176879883,242.6303176879883,242.6303176879883,242.6303176879883,242.6303176879883,242.6303176879883,242.6303176879883,242.6303176879883,242.6303176879883,242.6303176879883,242.6303176879883,242.6303176879883,242.6303176879883,242.6303176879883,242.6303176879883,242.6303176879883,242.6303176879883,242.6303176879883,242.6303176879883,242.6303176879883,242.6303176879883,242.6303176879883,242.6303176879883,242.6303176879883,242.6303176879883,242.6303176879883,242.6303176879883,242.6303176879883,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258,257.9109573364258],"meminc":[0,0,0,0,15.28223419189453,0,0,0,0.0003662109375,0,0,30.46537780761719,0,0,0,0,0,4.57763671875e-05,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-0.00030517578125,0,15.37606048583984,0,0.2463912963867188,0,0.2884597778320312,0,0.3012771606445312,0.3215408325195312,0.3189926147460938,0,0.316925048828125,0,0.331939697265625,0,0.3094329833984375,0.3229827880859375,0,0.1886749267578125,0,0,0,-2.817115783691406,0,0,0.3291702270507812,0,0.3593597412109375,0.38604736328125,0,0.4020156860351562,0,0.3988723754882812,0,0.392425537109375,0.3952713012695312,0.2183609008789062,0,-2.611854553222656,0,0.3572921752929688,0,0.3720016479492188,0,0.3881378173828125,0.39068603515625,0.39093017578125,0,0.3770751953125,0,0.3876571655273438,0,-2.751846313476562,0,0,0.3293380737304688,0,0.3565902709960938,0,0.373809814453125,0,0.3866958618164062,0,0.3925247192382812,0.3796234130859375,0,0.3893280029296875,0,0.2542953491210938,0,0,-2.6304931640625,0.3313217163085938,0,0,0.396026611328125,0,0.3679733276367188,0.3743667602539062,0.3790206909179688,0,0.36669921875,0,0.3811569213867188,0,0.1131744384765625,0,0,-2.465751647949219,0,0.3386688232421875,0,0.365692138671875,0,0.38006591796875,0.3858718872070312,0.3932418823242188,0,0.3994064331054688,0,0.2807540893554688,0,0,-2.523284912109375,0.3419570922851562,0,0,0.3630523681640625,0,0.3783493041992188,0,0.3891830444335938,0,0.3878250122070312,0,0,0.3853073120117188,0,0.3542022705078125,0,-2.566619873046875,0,0.332183837890625,0,0.3569793701171875,0.3704299926757812,0.3861770629882812,0,0,0.38714599609375,0,0.3878021240234375,0,0.397735595703125,-2.54888916015625,0,0,0.3216476440429688,0,0,0.3418731689453125,0.3591995239257812,0,0.36041259765625,0,0.3725509643554688,0,0.3725357055664062,0.387451171875,0.1310348510742188,0,0,-2.318992614746094,0,0.3092269897460938,0,0.3244171142578125,0,0.3365402221679688,0,0.3498687744140625,0.3619308471679688,0,0.3649215698242188,0,0.3451690673828125,0,0,-2.474822998046875,0.3031539916992188,0,0.3090591430664062,0,0.32391357421875,0,0.3230438232421875,0,0,0.33941650390625,0,0.3442840576171875,0.3190078735351562,0,0.2847518920898438,0,0,-2.426094055175781,0.3399429321289062,0,0.3534088134765625,0.3623580932617188,0,0.371551513671875,0.3712844848632812,0,0.3642425537109375,0,0.333953857421875,0,0,-2.391845703125,0,0.3537750244140625,0.3626937866210938,0,0.3611679077148438,0.3535079956054688,0,0.3831100463867188,0,0.3444671630859375,0.3026657104492188,0,0,-2.341171264648438,0.348602294921875,0.3450088500976562,0,0,0.3442611694335938,0,0.334808349609375,0.3282089233398438,0.3270187377929688,0.3292465209960938,0,0.05242919921875,0,0,-2.132362365722656,0,0.311309814453125,0,0.3233871459960938,0,0.3264541625976562,0,0.320068359375,0.317718505859375,0,0.3153305053710938,0,0.2853469848632812,0,0,-2.309608459472656,0,0.2674942016601562,0.310211181640625,0,0.3141326904296875,0,0.3153305053710938,0.31585693359375,0.3049087524414062,0.3004302978515625,0,0.2474517822265625,0,0,-2.240097045898438,0.333404541015625,0,0.2990341186523438,0,0,0.3063735961914062,0,0.3074188232421875,0.3054046630859375,0.303863525390625,0,0.300048828125,0,0.1496963500976562,0,0,-2.125,0.2904586791992188,0,0.2951278686523438,0,0,0.3070602416992188,0.3070831298828125,0,0.3037872314453125,0,0,0.3016204833984375,0,0.3018722534179688,0,0.08206939697265625,0,0,-2.068878173828125,0.27069091796875,0,0.2865829467773438,0,0,0.2944869995117188,0.2907562255859375,0,0.28631591796875,0,0.285003662109375,0,0,0.28912353515625,0.1289596557617188,0,-2.0633544921875,0.259490966796875,0,0.2831649780273438,0.2995376586914062,0,0.3002395629882812,0.3057403564453125,0,0.3059921264648438,0,0,0.3048553466796875,0.06638336181640625,0,-1.9259033203125,0,0.2858352661132812,0,0.3137664794921875,0,0.3209915161132812,0,0.3178024291992188,0.3172073364257812,0,0.31427001953125,0,0.1170806884765625,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2.054267883300781,0.20806884765625,0,0,0.2288131713867188,0,0.2461929321289062,0,0.2837982177734375,0.3447647094726562,0,0.3354873657226562,0,0.3509521484375,0,0.1160125732421875,0,0,-1.899658203125,0,0.276763916015625,0.31280517578125,0,0.3441009521484375,0,0.3611831665039062,0,0.3650970458984375,0,0.2988510131835938,0,0,-1.997550964355469,0,0.26739501953125,0,0.2935943603515625,0,0.3321914672851562,0,0.3532180786132812,0,0.3606491088867188,0.3732986450195312,0.0753326416015625,0,0,-1.776969909667969,0.2874908447265625,0,0.3272628784179688,0,0.3585205078125,0,0,0.3683547973632812,0.3816299438476562,0,0,0.1109085083007812,0,0,-1.779991149902344,0,0.2811126708984375,0,0.3165206909179688,0,0.3528823852539062,0,0.3669662475585938,0,0.3770599365234375,0,0,0.1417770385742188,0,0,-1.775619506835938,0.3060989379882812,0.3112945556640625,0.343231201171875,0,0.357025146484375,0.3698577880859375,0.1434707641601562,0,0,-1.756553649902344,0,0.2668838500976562,0,0,0.3074111938476562,0,0.3385543823242188,0.3582687377929688,0,0.3772506713867188,0,0.1626815795898438,0,0,-1.730789184570312,0.2754592895507812,0,0.3141403198242188,0.3468475341796875,0,0.361541748046875,0,0.3766860961914062,0,0.1096878051757812,0,0,-1.672401428222656,0,0.27301025390625,0,0.2854385375976562,0.331695556640625,0,0.3539352416992188,0,0.3644866943359375,0,0.1165542602539062,0,0,-1.687576293945312,0.2541046142578125,0,0.2997665405273438,0.338623046875,0,0.3486480712890625,0.347442626953125,0.1509246826171875,0,0,-1.707351684570312,0,0.2602615356445312,0,0.2979278564453125,0,0.3094100952148438,0.3421783447265625,0.35955810546875,0.1889877319335938,0,-1.687255859375,0.2557830810546875,0,0.296722412109375,0,0,0.3154830932617188,0,0.3549880981445312,0,0.3641281127929688,0,0.1504135131835938,0,0,-1.616233825683594,0.2743911743164062,0,0.3116455078125,0,0.32989501953125,0,0.3488998413085938,0,0.3603973388671875,0,0.0403900146484375,0,-1.528884887695312,0.3084335327148438,0,0.3076171875,0,0,0.3469314575195312,0,0.3636245727539062,0.2509002685546875,0,0,-1.633407592773438,0,0.268341064453125,0,0.304290771484375,0,0.3182830810546875,0,0,0.35601806640625,0,0.3639373779296875,0,0.07038116455078125,0,0,-1.488075256347656,0.2781524658203125,0,0,0.3174819946289062,0,0.3414764404296875,0.3575515747070312,0.24041748046875,0,0,-1.583839416503906,0,0.2484664916992188,0,0.2865371704101562,0,0.32476806640625,0,0.3455276489257812,0,0.3558502197265625,0,0.0689849853515625,0,0,-1.444480895996094,0.2888336181640625,0.3056259155273438,0,0.3371429443359375,0,0.3533401489257812,0,0.2051315307617188,0,-1.497230529785156,0,0.2481918334960938,0.2901687622070312,0,0.331298828125,0,0.3529205322265625,0,0.3193893432617188,0,0,0,0,0,-1.30377197265625,0.2802581787109375,0,0.3209915161132812,0,0.34228515625,0.3531341552734375,0.05123138427734375,0,-1.356155395507812,0,0.2691802978515625,0,0.3077774047851562,0,0.3437957763671875,0,0.3579864501953125,0,0.1208343505859375,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.493614196777344,0,0,0,0,0,0.1564178466796875,0.24652099609375,0,0.2598342895507812,0,0.2949905395507812,0,0.3063201904296875,0.3120651245117188,0,0.3395538330078125,0,0.3682937622070312,0,0.399932861328125,0,0,0.3584976196289062,0,0.327667236328125,0.3309097290039062,0,0.3293533325195312,0,0,0.3297271728515625,0,0,0.3302688598632812,0,0.1476974487304688,0,0,-4.527259826660156,0,0.3101272583007812,0,0.3416671752929688,0.34197998046875,0,0.3316116333007812,0,0.3691864013671875,0.3786773681640625,0,0.3861236572265625,0.3951492309570312,0,0.4106292724609375,0.4467086791992188,0,0.4028778076171875,0.3903350830078125,0.1545333862304688,0,0,-4.478141784667969,0,0.2829818725585938,0,0.3183822631835938,0,0.3247604370117188,0,0,0.3278350830078125,0.3621368408203125,0,0,0.372161865234375,0,0.381134033203125,0.3913803100585938,0.3982925415039062,0,0.3968124389648438,0.3996658325195312,0,0.3951492309570312,0.2576217651367188,0,0,0,-4.477134704589844,0,0,0.27325439453125,0,0.3033370971679688,0.3152008056640625,0,0.3244094848632812,0,0.3587265014648438,0,0.3600234985351562,0,0.376220703125,0,0.3860855102539062,0,0.3899078369140625,0,0,0.3988418579101562,0,0.400299072265625,0,0.3995208740234375,0,0,0.3194046020507812,0,0,0,0,0,-4.186752319335938,0,0.289703369140625,0,0.3032455444335938,0,0,0.3518753051757812,0.3579025268554688,0.3591995239257812,0,0.3755950927734375,0.3756866455078125,0,0.3863449096679688,0,0.3892135620117188,0,0.3930587768554688,0,0.3676300048828125,0,0.348663330078125,0,0.01464080810546875,0,-4.231292724609375,0,0,0.2650146484375,0.2940750122070312,0,0.2972640991210938,0,0.345458984375,0.3543167114257812,0,0.3684921264648438,0,0.3762283325195312,0,0,0.3837356567382812,0,0.390960693359375,0.396240234375,0,0.4090347290039062,0,0.38592529296875,0.08856201171875,0,0,-4.176162719726562,0,0.2751998901367188,0,0.2875518798828125,0,0.3023452758789062,0,0.3441314697265625,0,0.3529205322265625,0.3662033081054688,0,0.371490478515625,0.3804092407226562,0,0.38916015625,0,0.4329147338867188,0,0.408905029296875,0,0.3808975219726562,0.0059814453125,0,0,-4.03436279296875,0.287017822265625,0,0.2854843139648438,0,0.336212158203125,0,0.3529205322265625,0,0,0.3634185791015625,0,0.3694076538085938,0.3745880126953125,0,0.3862762451171875,0.3898468017578125,0,0.4034271240234375,0,0.39569091796875,0,0.2100677490234375,0,0,-4.11798095703125,0.262908935546875,0.2765731811523438,0,0.2993850708007812,0,0.3362350463867188,0,0.3503799438476562,0,0,0.3474884033203125,0.3570938110351562,0.3667144775390625,0,0.3746185302734375,0,0.3876419067382812,0,0.3872604370117188,0,0.3962783813476562,0.0934906005859375,0,0,0,-3.983505249023438,0,0.2663497924804688,0,0.221099853515625,0.1295013427734375,0.2049713134765625,0,0.18463134765625,0,0.282470703125,0,0.20916748046875,0,0.298675537109375,0,0.3202667236328125,0,0.2899169921875,0.3243026733398438,0.348236083984375,0,0.340240478515625,0.3631515502929688,0.3166656494140625,0,0,0,0,0,-3.834693908691406,0,0.287994384765625,0,0.2739181518554688,0,0.2902450561523438,0.3312301635742188,0.34307861328125,0,0.3462677001953125,0.3623275756835938,0,0.3663864135742188,0,0.3247833251953125,0,0.32427978515625,0,0.3425140380859375,0.3559341430664062,0,0,0,-3.8953857421875,0.239044189453125,0,0.2312545776367188,0,0.273895263671875,0.31097412109375,0,0,0.33392333984375,0,0,0.3058700561523438,0,0,0.3598785400390625,0,0.3542709350585938,0,0.320068359375,0,0.3084945678710938,0,0.3712997436523438,0,0.3507766723632812,0.248138427734375,0,0,0,0,0,-3.7889404296875,0.2406234741210938,0,0.2736358642578125,0.3181228637695312,0,0.3214187622070312,0,0.3263320922851562,0.3569869995117188,0,0.3482208251953125,0.3772048950195312,0,0.3903045654296875,0.3942489624023438,0,0,0.3888473510742188,0,0.1635513305664062,0,0,-3.776870727539062,0,0.2479934692382812,0,0.2264938354492188,0,0.2885360717773438,0.2933502197265625,0,0.3309707641601562,0,0.3469085693359375,0,0.33905029296875,0,0.3397216796875,0.3635177612304688,0,0.381866455078125,0,0.368133544921875,0,0.3591995239257812,0,0,0,0,0,-3.628395080566406,0.24285888671875,0,0.2795639038085938,0,0.3053436279296875,0,0.3225173950195312,0,0.3421554565429688,0,0.3546218872070312,0.3411865234375,0,0.3674468994140625,0,0.3838958740234375,0,0.375518798828125,0,0.3785476684570312,0,0.04183197021484375,0,-3.575363159179688,0,0.2352523803710938,0,0.2820587158203125,0.3148040771484375,0.3098220825195312,0.3443527221679688,0.354461669921875,0.3505477905273438,0,0.3708343505859375,0,0.3863296508789062,0,0.3767471313476562,0,0.35552978515625,0,0,0,0,0,-3.498908996582031,0,0.2081146240234375,0,0,0.258880615234375,0.2878799438476562,0,0.2763824462890625,0,0.3104095458984375,0,0.3342666625976562,0.3485260009765625,0,0,0.351348876953125,0.3764419555664062,0.392791748046875,0,0,0.3886795043945312,0,0.0688323974609375,0,-3.467132568359375,0,0.2449417114257812,0,0,0.2749481201171875,0,0.3057861328125,0.3322525024414062,0,0.349700927734375,0,0.3639755249023438,0,0.3779373168945312,0.394866943359375,0,0.4034042358398438,0,0.397491455078125,0,0.1238479614257812,0,0,0,-3.469429016113281,0,0.2418975830078125,0.2714385986328125,0,0.29620361328125,0,0.3238143920898438,0.3503646850585938,0.359832763671875,0.3703231811523438,0.3798599243164062,0,0,0.3912887573242188,0,0.392242431640625,0,0.1924667358398438,0,0,0,0,0,0,0,-3.214927673339844,0,0.2644195556640625,0,0.28533935546875,0,0.3186874389648438,0,0.34197998046875,0,0.3537445068359375,0,0.370819091796875,0,0,0.4218978881835938,0.4001846313476562,0,0.3964767456054688,0.1601333618164062,0,0,-3.380973815917969,0,0.2372589111328125,0,0.2604141235351562,0.281219482421875,0,0.3117752075195312,0.3421173095703125,0.3547744750976562,0,0,0.3633804321289062,0,0.3739395141601562,0,0.3866043090820312,0,0.388671875,0,0.1779251098632812,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-3.248443603515625,0.1686325073242188,0.209625244140625,0,0.2302474975585938,0,0,0.2327041625976562,0,0.2646408081054688,0.300537109375,0,0.322601318359375,0.2596588134765625,0,0.3223037719726562,0,0.3331222534179688,0.3082427978515625,0.3388900756835938,0,0.052642822265625,0,0,-3.252372741699219,0.22528076171875,0,0.2408905029296875,0.2700576782226562,0,0.2853240966796875,0.3191909790039062,0.3322372436523438,0,0.3259735107421875,0.3448333740234375,0,0.3584747314453125,0.366058349609375,0,0.2781524658203125,0,0,0,0,0,-3.106002807617188,0,0.2234039306640625,0,0.2514724731445312,0,0.2835464477539062,0,0.3035736083984375,0,0.3343124389648438,0,0.344085693359375,0,0,0.3449783325195312,0,0.1319656372070312,0,0.2311019897460938,0,0,0.3058929443359375,0,0.2184677124023438,0,0.2257766723632812,0,0,0,0,0,-3.158332824707031,0.2095718383789062,0,0.2312698364257812,0,0.2514114379882812,0,0.2892074584960938,0,0.323028564453125,0,0.3395462036132812,0.3539962768554688,0,0.3661575317382812,0.3850631713867188,0.3902664184570312,0.1097869873046875,0,0,-3.095252990722656,0,0.228271484375,0,0.27105712890625,0.281341552734375,0.314453125,0,0.3376846313476562,0.3488311767578125,0,0.3642501831054688,0,0.3770294189453125,0.3861160278320312,0,0.275848388671875,0,0,0,0,0,-2.953598022460938,0.2373733520507812,0,0.2602691650390625,0,0.2907180786132812,0,0.3246383666992188,0,0.3484725952148438,0,0.35833740234375,0,0.3672561645507812,0,0.384490966796875,0,0.3856735229492188,0,0.084442138671875,0,0,-3.007522583007812,0,0.228729248046875,0.2439804077148438,0,0.2705612182617188,0.309906005859375,0,0.3381423950195312,0,0.3506546020507812,0,0.3652725219726562,0,0.376220703125,0,0.3878021240234375,0,0.2230300903320312,0,0,0,-2.788192749023438,0,0.2293548583984375,0,0.2509384155273438,0.2885971069335938,0,0.2843246459960938,0.3307418823242188,0,0.34442138671875,0.3568115234375,0.361236572265625,0,0.3772735595703125,0,0.049713134765625,0,0,-2.9119873046875,0,0,0.2235488891601562,0,0.2418060302734375,0,0.2611312866210938,0,0.2739028930664062,0,0,0.30853271484375,0.3300628662109375,0,0.3365249633789062,0,0,0.3075027465820312,0.3824615478515625,0,0.330474853515625,0,0,0,0,0,-2.725372314453125,0,0.2198638916015625,0,0.1844024658203125,0.255340576171875,0,0,0.2957229614257812,0.295318603515625,0,0.3158111572265625,0,0.3318557739257812,0,0.3237075805664062,0,0.327117919921875,0,0,0.2588119506835938,0,0,0,0,0,-2.766281127929688,0,0.2444915771484375,0,0.3030242919921875,0,0.297943115234375,0,0.3276138305664062,0,0.3421630859375,0,0.3378677368164062,0.3394927978515625,0,0.34674072265625,0,0.308135986328125,0,0,0,0,0,0,0,-2.745552062988281,0.245819091796875,0,0.260711669921875,0,0.2979583740234375,0.320648193359375,0,0.3376235961914062,0,0.3388214111328125,0,0.3520050048828125,0,0.3650131225585938,0,0.3068695068359375,0,0,0,0,0,-2.685005187988281,0,0.220611572265625,0,0.2546005249023438,0,0.273773193359375,0,0.289642333984375,0.3284912109375,0.343780517578125,0,0.3523712158203125,0,0.365478515625,0.3348541259765625,0,0,0,0,0,-2.626823425292969,0.2261123657226562,0.2381210327148438,0,0.270599365234375,0,0.3064956665039062,0.3346939086914062,0,0.3467941284179688,0,0.3533782958984375,0,0.3681106567382812,0,0.2598953247070312,0,0,0,0,0,-2.528228759765625,0,0.2273941040039062,0.24517822265625,0,0.2768936157226562,0,0,0.3092269897460938,0.3368606567382812,0,0.3497772216796875,0.357391357421875,0,0.37164306640625,0,0.1299209594726562,0,0,0,-2.407928466796875,0,0.231964111328125,0,0.2528839111328125,0,0.2891845703125,0,0.3204879760742188,0.3450698852539062,0.35540771484375,0.3652725219726562,0.3225631713867188,0,0,0,0,0,-2.486114501953125,0.22528076171875,0,0.2379074096679688,0.2671127319335938,0,0.3063430786132812,0.3360595703125,0,0.3519821166992188,0,0.3588638305664062,0,0.3649749755859375,0,0.11126708984375,0,0,0,0,0,-2.319755554199219,0,0.2333908081054688,0,0,0.2535400390625,0,0.2924118041992188,0.328094482421875,0,0.3464279174804688,0,0.38671875,0,0.3600921630859375,0,0.1915740966796875,0,0,0,-2.351753234863281,0.2269515991210938,0.2423934936523438,0,0.2795181274414062,0,0.3129425048828125,0.3385009765625,0.351226806640625,0,0.3637619018554688,0,0.3077392578125,0,0,0,-2.392295837402344,0.2198028564453125,0,0.2341461181640625,0,0.261749267578125,0,0.2970809936523438,0,0.3284912109375,0.34954833984375,0.3576202392578125,0.3667449951171875,0,0.04732513427734375,0,-2.389015197753906,0,0.2217636108398438,0,0,0.2359848022460938,0.298553466796875,0.31011962890625,0.3366317749023438,0,0.350250244140625,0,0.3618850708007812,0.3428802490234375,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2.376502990722656,0,0.08942413330078125,0,0.1865463256835938,0,0.2216567993164062,0,0.2400741577148438,0,0.2624435424804688,0,0.2986602783203125,0.3208465576171875,0.3320999145507812,0,0.395904541015625,0,0,0.0965728759765625,0,0,0,-2.1444091796875,0.2312240600585938,0,0.2613906860351562,0.2982101440429688,0,0,0.3283843994140625,0.3503570556640625,0,0.3608169555664062,0,0.3670730590820312,0,0.0138397216796875,0,0,-2.265792846679688,0,0.2204513549804688,0.235595703125,0,0.2637405395507812,0.3029632568359375,0.3339080810546875,0.3496551513671875,0.3620223999023438,0,0.263214111328125,0,0,0,0,0,-2.149757385253906,0.2265396118164062,0,0.2437362670898438,0.281585693359375,0,0.32025146484375,0,0.3790740966796875,0.354217529296875,0,0.3690414428710938,0,0.040008544921875,0,0,-2.193229675292969,0,0,0.2190399169921875,0.236846923828125,0,0.2716827392578125,0.3084182739257812,0,0.3396072387695312,0,0.3482742309570312,0,0.3640975952148438,0.1689834594726562,0,0,0,-2.055259704589844,0.22979736328125,0,0.2532882690429688,0.292266845703125,0.3271560668945312,0.3494949340820312,0,0.3556976318359375,0,0.3102188110351562,0,0,0,-2.079551696777344,0,0.2240753173828125,0,0,0.240386962890625,0,0.3086700439453125,0,0.317840576171875,0.3421249389648438,0,0.3543319702148438,0,0.3537368774414062,0,0,0,0,0,-2.0809326171875,0,0.2182846069335938,0.2367172241210938,0.26983642578125,0.3082122802734375,0,0,0.3362045288085938,0,0,0.3511734008789062,0,0.3574447631835938,0.06380462646484375,0,-2.085807800292969,0,0.21929931640625,0,0,0.2324981689453125,0,0.2667694091796875,0,0.3014068603515625,0,0.3345870971679688,0.3522415161132812,0,0.3680267333984375,0.0705413818359375,0,0,0,-1.838310241699219,0,0.2595901489257812,0,0.270538330078125,0,0.3121719360351562,0,0.3372879028320312,0,0.3537445068359375,0,0.3637542724609375,0,0,0,0,0,-1.987297058105469,0,0.2050094604492188,0.236846923828125,0,0,0.269927978515625,0,0.3086166381835938,0,0.3353271484375,0,0.354827880859375,0,0.334442138671875,0,0,0,0,0,-1.933723449707031,0,0.2242355346679688,0.2405776977539062,0.277496337890625,0.3066635131835938,0,0.3351593017578125,0.3498992919921875,0,0.2565460205078125,0,0,0,-1.8955078125,0,0,0.2300949096679688,0.2438812255859375,0,0.2823333740234375,0,0,0.3163528442382812,0,0.3455276489257812,0,0.3590087890625,0,0.17413330078125,0,0,0,0,0,-1.778938293457031,0,0.2284164428710938,0.2546539306640625,0,0.2916717529296875,0.3262100219726562,0.3507766723632812,0.3626556396484375,0,0.01964569091796875,0,0,-1.877967834472656,0,0.2044143676757812,0,0.2384414672851562,0.2726211547851562,0.3115921020507812,0,0.3405914306640625,0,0.3577804565429688,0,0.2065582275390625,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.796424865722656,0,0.1977615356445312,0,0.2295074462890625,0.2499008178710938,0,0.2846221923828125,0,0.3183517456054688,0,0.337066650390625,0,0.2321853637695312,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.832008361816406,0,0,0,0.02028656005859375,0,0.2383346557617188,0,0.2466812133789062,0.2598953247070312,0,0.2950286865234375,0.32318115234375,0,0.296722412109375,0,0.327789306640625,0,0.3667678833007812,0,0.383270263671875,0.353057861328125,0.3432388305664062,0.3122711181640625,0.3092422485351562,0,0.2990341186523438,0.297271728515625,0.303131103515625,0.3132476806640625,0,0.3233795166015625,0,0.3550033569335938,0,0.3188934326171875,0.3144454956054688,0,0.3101806640625,0.3049774169921875,0,0.3148040771484375,0,0.0838775634765625,0,0,0,-7.23406982421875,0,0.27374267578125,0,0.3025741577148438,0.3346023559570312,0,0.3339157104492188,0,0.304779052734375,0,0.3485336303710938,0,0.3458404541015625,0,0.3471527099609375,0.3554611206054688,0,0,0.3577880859375,0,0.3484954833984375,0,0.3539886474609375,0.3468475341796875,0.3487167358398438,0,0.2763519287109375,0,0,0.2887039184570312,0.360198974609375,0,0.358306884765625,0.3606033325195312,0.3855361938476562,0,0.3542709350585938,0.3558807373046875,0,0,0,0,0,0,0,0,-7.012603759765625,0,0.2519683837890625,0,0.2720108032226562,0,0.2982864379882812,0,0.3021316528320312,0,0.3076095581054688,0,0.3348541259765625,0,0.3509292602539062,0,0,0.3659133911132812,0.3848190307617188,0.390380859375,0,0.3960800170898438,0,0.4007568359375,0,0.4075088500976562,0,0.4045791625976562,0,0.4073486328125,0.4051284790039062,0,0,0.3957138061523438,0,0,0.394317626953125,0,0.383880615234375,0,0.3632583618164062,0,0,0,0,0,0,0,0,-6.877532958984375,0.2488937377929688,0.2663040161132812,0,0.2864151000976562,0,0.2921524047851562,0,0,0.324981689453125,0,0.3514633178710938,0,0.362548828125,0,0.3839187622070312,0,0.3942947387695312,0,0.4001541137695312,0.4014205932617188,0,0.4046630859375,0,0.3779983520507812,0,0,0.395904541015625,0.3960189819335938,0,0.394500732421875,0.4044189453125,0,0.4081649780273438,0,0,0.3870773315429688,0,0.1978302001953125,0,0,0,-6.924964904785156,0,0.2397537231445312,0.252685546875,0.268829345703125,0.2822952270507812,0,0.31060791015625,0,0.34515380859375,0,0,0.3598709106445312,0.4143218994140625,0,0.3908309936523438,0.3866806030273438,0.369903564453125,0,0.3627090454101562,0,0.3627090454101562,0,0.361724853515625,0,0.3614120483398438,0,0.3662185668945312,0.3695068359375,0.3688125610351562,0.363037109375,0,0.3454513549804688,0,0.2407684326171875,0,0,0,0,0,0,0,0,-6.533599853515625,0,0,0.33270263671875,0,0.3286361694335938,0,0.3453369140625,0.3804473876953125,0,0.376556396484375,0.35662841796875,0,0.3552322387695312,0.3531646728515625,0,0.360015869140625,0.341827392578125,0,0.343231201171875,0,0.348388671875,0.357452392578125,0.35498046875,0.3509521484375,0.3533554077148438,0,0.3928909301757812,0,0.3427047729492188,0,0.3409347534179688,0.01325225830078125,0,0,0,-6.533607482910156,0,0.3225631713867188,0,0.325347900390625,0,0.3365707397460938,0,0.3722991943359375,0.3817062377929688,0,0.3711013793945312,0,0.3570785522460938,0.3558197021484375,0.3523025512695312,0.3550872802734375,0.3464126586914062,0,0,0.347808837890625,0,0.3500518798828125,0,0.3550643920898438,0.362396240234375,0.3525772094726562,0.3529586791992188,0.3542404174804688,0,0.3388290405273438,0,0.035400390625,0,0,0,0,0,0,0,0,0,0,0,0,0,-6.487747192382812,0.2722549438476562,0,0.292694091796875,0,0.3084945678710938,0,0.355865478515625,0,0.3662185668945312,0,0.3838119506835938,0,0.38916015625,0,0.3805923461914062,0,0.367340087890625,0.3614349365234375,0,0,0.3617095947265625,0.36004638671875,0,0.3623123168945312,0,0.36114501953125,0,0.3518829345703125,0.359130859375,0,0.358917236328125,0.3470230102539062,0,0.3365631103515625,0,0,0,0,0,-6.350273132324219,0,0.3113555908203125,0,0.30914306640625,0,0.34991455078125,0,0.362701416015625,0,0.3701248168945312,0.3619384765625,0,0.358673095703125,0,0.4134979248046875,0.39862060546875,0,0.3881683349609375,0,0,0.3848114013671875,0,0.3909378051757812,0,0.3958892822265625,0,0.3992080688476562,0,0.4046707153320312,0,0.4076080322265625,0,0.3850555419921875,0.143829345703125,0,0,0,0,0,-6.379890441894531,0.2432785034179688,0,0.2467193603515625,0,0.2468795776367188,0,0.2833938598632812,0.2979583740234375,0,0.288177490234375,0,0.2986831665039062,0.3077392578125,0,0.3315963745117188,0.3466644287109375,0.3621139526367188,0.4216842651367188,0,0.38885498046875,0,0.3848190307617188,0,0.3868026733398438,0.3800277709960938,0,0.3800888061523438,0,0,0.3786773681640625,0,0,0.3540878295898438,0.2344818115234375,0,0,0,0,0,0,0,0,-6.175384521484375,0,0,0.2409286499023438,0,0,0.2516250610351562,0,0.288330078125,0,0.3275909423828125,0,0.3425140380859375,0.3546524047851562,0,0.3511276245117188,0,0.3541641235351562,0.34674072265625,0.3466720581054688,0,0.3450241088867188,0,0,7.684539794921875,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7.62939453125,7.62939453125e-06,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,15.2587890625,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7.629417419433594,0,0,0,0,0,0,0,0.1145553588867188,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,15.2806396484375,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"filename":["<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,null,null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,null,null,"<expr>",null,null,null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,null,null,null,null,null,null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,null,null,null,null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>","<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,null,null,"<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,null,null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,null,null,null,null,null,null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,null,null,null,null,null,null,null,null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,"<expr>","<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null]},"interval":10,"files":[{"filename":"<expr>","content":"## Generate Large Random Dataset\nn <- 2e6\nx <- runif(n)\ny <- runif(n)\nz <- runif(n)\nXYZ <- cbind(x,y,z)\n\n## Inspect 4 equivalent `row mean` calculations \nprofvis::profvis({\n    m <- rowSums(XYZ)/ncol(XYZ)\n    m <- rowMeans(XYZ)\n    m <- apply(XYZ, 1, mean)\n    m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }\n})\n## rowSums(), colSums(), rowMeans(), and colMeans() are vectorised and fast.\n## for loop is not the slowest, but the ugliest.","normpath":"<expr>"}],"prof_output":"/tmp/RtmpL3J5Hn/file956232d21d6f.prof","highlight":{"output":["^output\\$"],"gc":["^<GC>$"],"stacktrace":["^\\.\\.stacktraceo(n|ff)\\.\\.$"]},"split":"h"}},"evals":[],"jsHooks":[]}</script>
```

``` r
## rowSums(), colSums(), rowMeans(), and colMeans() are vectorised and fast.
## for loop is not the slowest, but the ugliest.
```

For more systematic speed comparisons, use the `microbenchmark` package

``` r
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
##  mean1(x, 0.5) 29.04080 30.31383 32.60656 33.48837 34.12850 36.09136   100  a 
##  mean2(x, 0.5) 27.86534 29.02359 31.42956 32.50656 32.78087 37.57611   100   b
##  mean3(x, 0.5) 28.94673 30.10793 32.60944 33.89489 34.14088 38.64793   100  a
```


For memory leaks, first free up space and use the `bench` package for timing

``` r
gc() ## garbage cleanup

bench::mark(
  mean1(x,.5),
  mean2(x,.5),
  mean3(x,.5))
```

### Speed-Ups


**vectorize**

Vector operations are generally faster and easier to read than loops

``` r
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
##    expr       min        lq      mean    median        uq      max neval cld
##  ma1(y) 246.48998 292.62278 296.22367 297.36998 306.91321 483.2286   100  a 
##  ma2(y)  23.96706  27.74139  34.27119  31.16914  35.27275 176.1122   100   b
```
Likewise, matrix operations are often faster than vector operations.




**Packages**
Before creating your own program, check if there is a faster or more memory efficient version. E.g., [data.table](https://cran.r-project.org/web/packages/data.table/vignettes/datatable-intro.html) or [Rfast2](https://cran.r-project.org/web/packages/Rfast2/index.html) for basic data manipulation.

``` r
X <- cbind(1, runif(1e6))
Y <- X %*% c(1,2) + rnorm(1e6)
DAT <- as.data.frame(cbind(Y,X))

system.time({.lm.fit(X, Y) })
```

```
##    user  system elapsed 
##   0.537   0.000   0.101
```

``` r
system.time({ lm(Y~X, data=DAT) })
```

```
##    user  system elapsed 
##   1.028   0.006   0.262
```
Note that quicker codes tend to have fewer checks and return less information. So you must know exactly what you are putting in and getting out.


###  Bottlenecks

Sometimes there will still be a problematic bottleneck. 

Your next step should be parallelism:

* Write the function as a general vectorized function.
* Apply the same function to every element in a list *at the same time*


``` r
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


``` r
## vectorize and compile
e_power_e_fun <- compiler::cmpfun( function(vector){ vector^vector} )

## base R
x <- 0:1E6
s_vc <- system.time( e_power_e_vec <- e_power_e_fun(x) )
s_vc
```

```
##    user  system elapsed 
##   0.033   0.001   0.034
```

``` r
## brute power
x <- 0:1E6
s_bp <- system.time({
  e_power_e_mc <- unlist( parallel::mclapply(x, mc.cores=2, FUN=e_power_e_fun))
})
s_bp
```

```
##    user  system elapsed 
##   1.397   0.257   0.937
```

``` r
## Same results
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

Make sure your packages are up to date

``` r
update.packages()
```

After reinstalling, you can update *all* packages stored in *all* `.libPaths()` with the following command

``` r
install.packages(old.packages(checkBuilt=T)[,"Package"])
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
## https://stackoverflow.com/questions/31935516/installing-r-packages-error-in-readrdsfile-error-reading-from-connection/55997765
```

To remove packages duplicated in multiple libraries

``` r
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


**Sweave:** is an alternative to Rmarkdown for integrating latex and R. While Rmarkdown "writes R and latex within markdown", Sweave "write R in latex". Sweave files end in ".Rnw" and can be called within R


``` r
Sweave('Sweave_file.Rnw')
```

or directly from the command line


``` bash
R CMD Sweave Sweave_file.Rnw 
```

In both cases, a latex file `Sweave_file.tex` is produced, which can then be converted to `Sweave_file.pdf`.



For more on Sweave,

* https://rpubs.com/YaRrr/SweaveIntro
* https://support.rstudio.com/hc/en-us/articles/200552056-Using-Sweave-and-knitr
* https://www.statistik.lmu.de/~leisch/Sweave/Sweave-manual.pdf


**Knitr:** 
You can also produce a pdf from an .Rnw file via `knitr`


``` bash
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

``` r
library(haven)
read_dta()
## See also foreign::read.dta
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

