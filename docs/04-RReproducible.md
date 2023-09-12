# (PART) Reproducible Research in R {-} 

You want your work to be reproducible, and we will cover some of the basics of how to do this in R. Note the distintion

* Replicable: someone collecting new data comes to the same results.
* Reproducibile: someone reusing your data comes to the same results.

Will we cover some of both below. Note that you can read more about the distinction in many places, including

* https://www.annualreviews.org/doi/10.1146/annurev-psych-020821-114157
* https://nceas.github.io/sasap-training/materials/reproducible_research_in_r_fairbanks/

# Why be reproducible 
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

R is good for complex stats, concise figures, and coherent organization.

* Built and developed by applied statisticians for statistics.
* Used by many in academia and industry.


R Markdown is good for reproducible research 

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

Both are good for getting a job

* As a student, think about labour demand. R skills, unlike other purely academic software, is something future employers use and want. Do more of your own research on this to understand how much to invest.





https://kbroman.org/steps2rr/pages/organize.html


## Types of Projects

Homework reports are the smallest and probably first document you create. We will create little homework reports using R markdown that are almost entirely self-contained (showing both code and output). To do this, you will need to install [Pandoc](http://pandoc.org) on your computer.

Posters and presentations are another important type of scientific document. R markdown is good at creating both of these, and actually *very* good with some additional packages. So we will also use [flexdashboard](https://pkgs.rstudio.com/flexdashboard/) for posters and [beamer]( https://bookdown.org/yihui/rmarkdown/beamer-presentation.html) for presentions. Since beamer is a pdf output, you will need to install [TinyTex](https://yihui.org/tinytex/), which can be done within R

```r
install.packages('tinytex')
tinytex::install_tinytex()  # install TinyTeX
```

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


# Small Scale Projects
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
<div class="plotly html-widget html-fill-item-overflow-hidden html-fill-item" id="htmlwidget-5f938847c3457b437b4a" style="width:672px;height:480px;"></div>
<script type="application/json" data-for="htmlwidget-5f938847c3457b437b4a">{"x":{"visdat":{"25195ffaaf60":["function () ","plotlyVisDat"]},"cur_data":"25195ffaaf60","attrs":{"25195ffaaf60":{"x":{},"y":{},"alpha_stroke":1,"sizes":[10,100],"spans":[1,20]}},"layout":{"margin":{"b":40,"l":60,"t":25,"r":10},"xaxis":{"domain":[0,1],"automargin":true,"title":"X"},"yaxis":{"domain":[0,1],"automargin":true,"title":"Y"},"hovermode":"closest","showlegend":false},"source":"A","config":{"modeBarButtonsToAdd":["hoverclosest","hovercompare"],"showSendToCloud":false},"data":[{"x":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100],"y":[1.5200519262928855,8.5223815889974546,13.273016434475567,17.378392869419681,19.273383137053614,23.858723093564944,30.540699571117095,31.800345958158836,34.774029685882311,39.928425206131486,51.32154533218894,46.346763028165931,52.31096671980054,53.446374713743566,58.114181851126766,66.895314337475867,63.489792232018338,71.0667573536644,74.799237724784163,79.344588037737083,81.60371382529685,90.137393589317284,89.911911604271026,97.168359409057814,96.994479496732822,101.10857230497822,111.11490518303147,112.68855914445837,118.48509008389618,118.93120448678832,123.99017451312896,125.3621678219037,137.2183473032527,137.2624392684576,141.25846071694596,146.17385351906637,147.84619554624041,146.55587065570302,157.79287493922249,158.44474923303352,165.75078557121415,168.08157738301759,170.14592492987455,176.93158056348324,180.89980494586027,183.46536187228031,186.07474841588416,193.35743403366021,192.03919277508126,201.45459148851268,203.94817658174878,207.7496059163783,213.84193069420613,217.35284989142727,219.8228600991068,223.13591315868931,224.51385731393884,231.01438523766919,236.18495798533417,241.25191749502031,247.4093188143292,249.27014668599574,251.89956132104189,256.27378324010971,260.20553786105603,262.88211847002975,266.70189172570389,273.27391200783558,274.14862721523548,278.93073196627637,286.50649738002051,287.00472564697708,291.87930631917783,294.07983341608491,298.73689313532373,302.22393626176461,306.96924542075215,312.06161432743124,315.5557381367891,318.2761097335968,325.83687087569979,325.27792871374902,330.62345119757657,334.20229524551212,339.820088306917,341.13801876658874,348.65038659396748,351.74846965360177,354.28780167161295,358.17707424169998,364.22650345596736,368.12804579528733,369.83684372099543,378.16787542218702,383.64042314096736,387.9782682331944,387.96885608623694,390.51660047154803,396.81691484018546,398.10793106135111],"type":"scatter","mode":"markers","marker":{"color":"rgba(31,119,180,1)","line":{"color":"rgba(31,119,180,1)"}},"error_y":{"color":"rgba(31,119,180,1)"},"error_x":{"color":"rgba(31,119,180,1)"},"line":{"color":"rgba(31,119,180,1)"},"xaxis":"x","yaxis":"y","frame":null}],"highlight":{"on":"plotly_click","persistent":false,"dynamic":false,"selectize":false,"opacityDim":0.20000000000000001,"selected":{"opacity":1},"debounce":0},"shinyEvents":["plotly_hover","plotly_click","plotly_selected","plotly_relayout","plotly_brushed","plotly_brushing","plotly_clickannotation","plotly_doubleclick","plotly_deselect","plotly_afterplot","plotly_sunburstclick"],"base_url":"https://plot.ly"},"evals":[],"jsHooks":[]}</script>
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




# Medium Scale Projects
***

As you scale up to a medium sized project, however, you will have to be more organized.

Medium sized projects should have their own `Project` folder on your computer with files, subdirectories with files, and subsubdirectories with files. It should look like this
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




## Final Step

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


# Large Scale Projects


For larger scale projects, use scripts 

* https://kbroman.org/steps2rr/pages/scripts.html
* https://kbroman.org/steps2rr/pages/automate.html

## Debugging 

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
## Ncells 1209382 64.6    2357240 125.9  2357240 125.9
## Vcells 2293671 17.5    8388608  64.0  3530121  27.0
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
<div class="profvis html-widget html-fill-item-overflow-hidden html-fill-item" id="htmlwidget-96de579a237c96ad2315" style="width:100%;height:600px;"></div>
<script type="application/json" data-for="htmlwidget-96de579a237c96ad2315">{"x":{"message":{"prof":{"time":[1,2,3,4,5,6,7,8,9,9,9,10,10,11,11,12,12,13,13,14,14,15,15,16,16,17,17,18,18,19,19,20,20,21,21,22,23,23,24,25,26,27,28,28,29,29,30,30,30,31,32,32,33,33,34,34,35,35,35,36,37,37,38,38,38,39,39,39,39,40,40,41,41,42,42,43,43,44,44,45,45,46,47,47,48,49,49,50,51,51,52,53,54,54,55,56,56,56,57,58,59,60,60,61,61,62,62,63,63,64,65,65,65,66,66,67,67,67,68,68,69,70,70,71,71,71,72,73,73,74,74,74,75,76,77,77,78,79,80,80,81,81,82,82,83,84,84,85,86,86,87,88,88,89,89,90,90,90,91,91,91,92,92,93,93,94,94,95,95,96,96,97,97,98,98,98,99,100,100,100,101,101,101,102,102,103,103,104,104,105,105,106,107,107,108,109,109,110,111,111,112,113,113,114,115,115,116,116,117,117,118,118,119,120,121,122,122,123,123,123,124,124,125,125,126,126,127,128,129,130,131,131,132,133,134,134,135,135,136,136,137,137,137,138,139,139,140,140,141,142,142,143,143,144,144,145,146,146,147,147,147,148,148,149,149,150,150,151,152,152,153,153,154,154,155,155,156,156,157,157,158,158,159,159,160,160,160,161,161,161,162,163,163,163,164,164,165,166,167,167,168,169,169,170,170,171,171,171,172,172,173,173,174,174,175,175,176,176,177,177,178,179,179,179,180,180,180,181,181,181,182,182,183,183,184,185,185,186,186,186,187,188,189,190,191,191,191,192,192,193,194,194,194,195,195,195,196,196,196,197,197,197,198,198,198,199,199,199,200,200,200,201,201,201,202,202,202,203,203,203,204,204,205,205,206,207,207,208,208,208,209,210,210,211,211,211,212,212,213,213,214,214,215,215,216,217,217,218,218,219,219,220,220,221,221,222,222,223,223,224,224,225,226,226,227,227,228,229,229,230,230,231,232,232,232,233,233,233,234,234,235,235,236,236,237,237,238,238,239,239,240,240,241,241,241,242,243,244,244,245,245,246,246,246,247,248,248,249,249,250,250,251,252,252,253,253,254,254,255,255,255,256,256,257,258,258,259,259,260,261,262,262,262,263,264,264,265,265,266,267,268,268,269,269,270,270,270,271,271,272,272,273,274,274,275,275,276,276,276,277,277,278,278,279,279,280,280,281,282,282,283,283,283,284,284,285,286,286,287,287,288,289,290,290,290,291,292,293,293,294,294,295,296,296,297,297,298,298,299,300,300,301,301,302,302,303,303,303,304,305,305,306,306,307,307,308,308,308,309,309,310,310,310,311,311,312,312,313,313,314,314,315,315,315,316,316,316,317,317,318,318,319,319,320,321,321,322,323,323,323,324,324,325,326,326,327,327,328,328,329,329,329,330,330,331,331,332,332,333,333,334,334,335,335,335,336,336,337,337,338,339,339,340,340,340,341,341,342,342,343,343,344,344,345,345,346,346,347,347,347,348,348,348,349,349,349,350,350,350,351,351,351,352,352,352,353,353,353,354,354,354,355,355,355,356,356,356,357,357,357,358,358,358,359,359,359,360,360,360,361,361,361,362,362,362,363,363,363,364,364,364,365,365,365,366,366,366,367,367,367,368,368,368,369,369,369,370,370,370,371,371,371,372,372,372,373,373,374,374,375,376,376,377,377,377,378,379,380,381,381,382,383,383,383,384,384,385,386,386,386,387,387,387,388,388,388,389,389,390,390,391,392,393,394,395,395,396,396,397,398,398,399,399,400,400,401,401,401,402,402,403,404,404,405,405,406,407,408,409,409,410,410,411,412,412,413,414,414,415,415,415,416,416,417,417,418,419,419,420,420,421,421,422,422,423,423,424,425,426,427,428,428,428,429,429,430,430,431,431,431,432,433,433,433,434,435,436,436,436,437,438,438,439,440,440,440,441,441,441,442,442,442,443,443,444,444,445,445,446,446,447,447,448,448,449,449,450,450,451,451,451,452,452,453,453,454,454,454,455,455,456,456,457,457,458,458,459,460,460,461,462,462,463,463,464,464,465,465,466,466,467,467,468,468,468,469,470,471,471,472,472,473,474,475,476,476,477,477,478,478,479,479,480,481,481,481,482,482,482,483,483,484,485,485,486,486,487,488,488,489,489,490,490,491,492,492,493,493,494,494,494,495,495,495,496,497,497,498,498,499,500,501,501,501,502,502,503,503,504,504,505,506,506,507,507,508,508,509,509,510,510,511,512,512,513,513,514,515,515,516,516,517,518,518,519,519,520,520,521,521,522,522,522,523,523,524,525,525,525,526,526,527,527,528,528,529,530,530,531,531,532,533,533,533,534,535,535,536,536,537,538,538,539,539,540,540,541,542,542,543,543,544,544,545,545,545,546,546,546,547,547,548,548,549,549,550,550,551,551,552,552,553,554,554,554,555,555,556,557,557,558,558,558,559,559,560,560,561,561,562,562,563,563,564,565,566,566,567,567,568,568,569,569,570,570,570,571,571,572,572,573,574,574,575,575,576,576,577,577,578,578,579,579,580,580,581,582,582,582,583,583,583,584,584,585,586,586,587,588,589,589,589,590,590,591,591,592,592,592,593,593,594,594,594,595,596,596,597,598,599,599,600,600,601,602,603,604,604,605,605,606,606,606,606,607,608,608,609,610,610,611,611,612,612,613,613,614,614,615,615,616,617,617,618,618,618,619,620,620,620,621,621,622,622,623,623,624,624,625,625,626,626,627,627,628,628,629,629,629,630,630,630,631,631,632,632,633,633,634,635,635,636,636,637,637,638,639,639,640,641,641,642,642,643,643,644,644,645,645,646,646,647,647,648,648,649,649,650,650,651,651,652,652,653,653,654,654,655,655,656,656,657,658,658,659,659,660,660,661,661,661,662,662,662,663,663,664,665,665,665,665,666,666,666,666,667,668,668,669,669,670,670,671,671,672,672,673,674,674,675,675,675,676,677,677,677,678,678,679,679,680,680,681,682,682,683,684,684,685,686,686,687,687,688,688,688,689,689,689,690,690,690,691,691,692,692,693,694,695,696,696,697,698,698,699,699,699,700,700,700,701,702,702,703,703,704,704,705,705,706,706,707,707,707,708,708,708,709,709,710,710,710,711,711,711,712,712,712,713,713,714,714,715,716,716,717,717,718,718,719,719,720,720,721,721,722,722,723,724,725,725,726,727,728,728,729,730,730,731,731,732,732,733,733,734,734,735,736,737,737,738,738,739,740,740,740,741,741,742,743,743,744,745,746,746,747,747,747,748,748,749,749,750,750,751,751,752,752,753,753,753,754,754,754,755,755,756,756,757,758,758,759,760,761,761,762,763,763,764,764,764,765,765,766,766,767,767,768,768,769,769,770,770,771,771,772,772,773,774,774,774,774,775,775,775,775,776,776,777,777,778,778,779,779,780,781,782,782,783,784,784,784,784,785,785,785,785,786,786,787,787,788,789,790,790,791,791,792,792,793,793,794,794,795,795,795,795,796,796,796,797,797,797,798,798,799,799,800,800,801,802,802,803,804,804,805,805,806,807,807,808,809,809,809,810,810,811,812,813,813,814,814,815,815,815,815,816,816,817,817,818,819,819,820,821,821,822,822,822,823,823,824,824,824,825,825,826,826,827,827,828,828,829,829,830,830,831,831,832,833,833,834,834,835,835,835,836,836,837,838,839,839,840,841,841,842,842,843,844,844,845,845,846,846,847,847,848,848,849,850,850,850,851,851,852,852,853,854,854,854,854,855,855,855,855,856,857,857,858,858,859,859,859,860,861,861,862,863,864,864,865,865,866,866,866,867,867,868,868,869,869,870,871,871,872,872,873,873,874,874,875,875,876,876,877,877,878,878,879,879,880,880,881,881,882,882,883,883,884,884,885,885,886,886,887,888,888,889,890,890,891,892,892,892,893,893,893,894,894,895,896,896,897,898,898,899,899,900,901,901,901,902,902,902,903,904,904,905,906,907,907,908,908,909,909,909,910,910,910,911,911,911,912,912,913,913,914,914,914,915,915,916,916,917,917,918,919,919,920,920,920,921,921,922,922,923,923,924,924,925,925,926,926,927,927,928,928,929,929,930,930,931,931,932,932,933,933,933,934,934,935,935,936,936,936,937,937,938,938,939,939,940,941,941,942,942,942,943,944,944,945,946,946,946,947,947,947,948,948,949,950,950,951,951,952,952,953,954,955,955,955,956,956,956,957,958,958,959,959,960,960,961,961,962,962,963,963,964,964,965,965,966,966,967,967,968,968,969,970,970,971,971,972,972,972,973,973,973,974,975,976,976,977,977,978,978,979,980,980,981,981,982,983,983,984,984,985,986,986,987,987,987,988,989,989,990,990,991,991,991,992,993,993,994,994,995,995,996,996,996,997,997,998,998,999,999,1000,1000,1001,1001,1002,1002,1003,1004,1004,1005,1005,1006,1006,1007,1007,1008,1008,1009,1009,1010,1010,1010,1011,1012,1013,1014,1014,1015,1015,1016,1016,1017,1017,1018,1018,1019,1019,1020,1020,1020,1021,1021,1022,1022,1023,1024,1024,1024,1025,1026,1026,1027,1027,1027,1027,1028,1028,1028,1028,1029,1029,1029,1029,1030,1030,1030,1030,1031,1031,1031,1031,1032,1032,1032,1032,1033,1033,1033,1033,1034,1034,1034,1034,1035,1035,1035,1035,1036,1036,1036,1036,1037,1037,1037,1037,1038,1038,1038,1038,1039,1039,1039,1039,1040,1040,1040,1040,1041,1041,1041,1041,1042,1042,1042,1042,1043,1043,1043,1043,1044,1044,1044,1044,1045,1045,1045,1045,1046,1046,1046,1046,1047,1047,1047,1047,1048,1048,1048,1048,1049,1049,1049,1049,1050,1050,1050,1050,1051,1051,1051,1051,1052,1052,1052,1052,1053,1053,1053,1053,1054,1054,1054,1054,1055,1055,1055,1055,1056,1056,1056,1056,1057,1057,1057,1057,1058,1058,1058,1058,1059,1059,1059,1059,1060,1060,1060,1060,1061,1061,1061,1061,1062,1062,1062,1062,1063,1063,1063,1063,1064,1064,1064,1064,1065,1065,1065,1065,1066,1066,1066,1066,1067,1067,1067,1067,1068,1068,1068,1068,1069,1069,1069,1069,1070,1070,1070,1070,1071,1071,1071,1071,1072,1072,1072,1072,1073,1073,1073,1073,1074,1074,1074,1074,1075,1075,1075,1075,1076,1076,1076,1076,1077,1077,1077,1077,1078,1078,1078,1078,1079,1079,1080,1080,1081,1081,1082,1082,1083,1083,1084,1084,1085,1085,1086,1086,1087,1087,1087,1088,1088,1089,1089,1089,1090,1091,1091,1092,1092,1093,1094,1094,1095,1095,1096,1096,1097,1097,1098,1098,1099,1100,1100,1101,1102,1102,1102,1103,1103,1103,1104,1104,1105,1106,1106,1107,1107,1108,1108,1109,1110,1110,1111,1111,1112,1113,1113,1113,1114,1115,1116,1117,1117,1118,1119,1119,1120,1120,1121,1121,1122,1122,1123,1124,1124,1125,1125,1126,1126,1127,1128,1128,1128,1129,1130,1130,1131,1131,1132,1133,1134,1134,1135,1135,1136,1137,1138,1139,1139,1140,1140,1140,1141,1141,1142,1142,1142,1143,1143,1144,1145,1146,1147,1147,1148,1148,1149,1149,1149,1150,1150,1151,1151,1152,1152,1153,1153,1154,1155,1156,1156,1157,1157,1158,1158,1158,1159,1159,1160,1160,1161,1161,1162,1163,1163,1164,1164,1165,1165,1165,1166,1166,1167,1167,1168,1168,1169,1169,1169,1170,1170,1170,1171,1172,1172,1173,1174,1174,1174,1175,1175,1176,1176,1177,1177,1178,1178,1179,1179,1180,1180,1181,1181,1182,1183,1184,1185,1185,1186,1186,1187,1188,1188,1189,1190,1190,1191,1191,1191,1192,1192,1192,1193,1193,1194,1195,1195,1196,1197,1198,1198,1199,1200,1201,1201,1201,1202,1202,1203,1203,1204,1204,1205,1205,1206,1206,1207,1207,1208,1209,1209,1210,1210,1211,1211,1212,1212,1212,1213,1213,1213,1214,1214,1214,1215,1216,1216,1217,1218,1218,1219,1219,1220,1220,1221,1221,1222,1222,1223,1223,1224,1224,1225,1225,1225,1226,1226,1226,1227,1228,1228,1229,1229,1230,1231,1232,1232,1233,1234,1234,1235,1235,1236,1236,1237,1237,1238,1238,1239,1239,1240,1240,1241,1241,1242,1242,1243,1243,1244,1244,1245,1245,1245,1246,1246,1246,1247,1247,1248,1248,1249,1250,1250,1251,1251,1252,1253,1253,1254,1254,1255,1255,1256,1256,1257,1257,1257,1258,1258,1259,1259,1260,1261,1261,1262,1262,1262,1262,1263,1263,1263,1263,1264,1264,1264,1264,1265,1266,1266,1267,1267,1267,1268,1268,1269,1270,1270,1270,1271,1272,1272,1273,1273,1273,1274,1274,1275,1275,1276,1276,1277,1277,1278,1278,1279,1280,1281,1281,1281,1282,1282,1283,1283,1283,1284,1284,1284,1285,1285,1285,1286,1286,1287,1287,1288,1288,1289,1289,1290,1290,1291,1292,1293,1293,1294,1294,1294,1295,1295,1296,1297,1298,1298,1299,1299,1300,1300,1301,1301,1302,1302,1303,1303,1304,1304,1305,1305,1306,1306,1307,1308,1308,1309,1309,1310,1310,1311,1311,1312,1312,1313,1313,1314,1314,1315,1315,1316,1316,1317,1317,1318,1318,1319,1319,1320,1320,1321,1321,1322,1322,1323,1323,1324,1324,1325,1325,1326,1326,1327,1327,1327,1327,1327,1327,1327,1327,1328,1328,1328,1328,1328,1328,1328,1328,1329,1329,1329,1329,1329,1329,1329,1329,1330,1330,1330,1330,1330,1330,1330,1330,1331,1331,1331,1331,1331,1331,1331,1331,1332,1332,1332,1332,1332,1332,1332,1332,1333,1333,1333,1333,1333,1333,1333,1333,1334,1334,1334,1334,1334,1334,1334,1334,1335,1335,1335,1335,1335,1335,1335,1335,1336,1336,1336,1336,1336,1336,1336,1336,1337,1337,1337,1337,1337,1337,1337,1337,1338,1338,1338,1338,1338,1338,1338,1338,1339,1339,1339,1339,1339,1339,1339,1339,1340,1340,1340,1340,1340,1340,1340,1340,1341,1341,1341,1341,1341,1341,1341,1341,1342,1342,1342,1342,1342,1342,1342,1342,1343,1343,1343,1343,1343,1343,1343,1343,1344,1344,1344,1344,1344,1344,1344,1344,1345,1345,1345,1345,1345,1345,1345,1345,1346,1346,1346,1346,1346,1346,1346,1346],"depth":[1,1,1,1,1,1,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,1,1,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,3,2,1,1,2,1,3,2,1,4,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,1,2,1,1,1,2,1,1,3,2,1,1,1,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,3,2,1,2,1,1,2,1,3,2,1,1,2,1,3,2,1,1,1,2,1,1,1,2,1,2,1,2,1,1,2,1,1,2,1,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,1,1,1,2,1,3,2,1,2,1,2,1,2,1,1,1,1,1,2,1,1,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,1,3,2,1,2,1,1,1,2,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,3,2,1,1,1,1,1,3,2,1,2,1,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,3,2,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,1,1,3,2,1,1,2,1,2,1,1,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,2,1,1,2,1,2,1,1,1,3,2,1,1,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,3,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,1,3,2,1,2,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,3,2,1,1,1,1,2,1,1,3,2,1,2,1,1,3,2,1,3,2,1,3,2,1,2,1,2,1,1,1,1,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,1,1,1,2,1,2,1,1,2,1,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,1,1,1,3,2,1,2,1,2,1,3,2,1,1,3,2,1,1,1,3,2,1,1,2,1,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,1,2,1,2,1,1,1,1,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,1,2,1,2,1,1,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,1,3,2,1,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,2,1,1,2,1,1,1,3,2,1,2,1,2,1,3,2,1,2,1,3,2,1,1,2,1,1,1,2,1,2,1,1,1,1,2,1,2,1,4,3,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,1,4,3,2,1,4,3,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,1,3,2,1,2,1,2,1,2,1,1,2,1,1,2,1,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,1,1,1,2,1,1,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,1,3,2,1,2,1,1,2,1,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,1,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,4,3,2,1,4,3,2,1,2,1,2,1,2,1,2,1,1,1,2,1,1,4,3,2,1,4,3,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,4,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,1,2,1,1,3,2,1,2,1,1,1,2,1,2,1,4,3,2,1,2,1,2,1,1,2,1,1,2,1,3,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,1,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,1,4,3,2,1,4,3,2,1,1,2,1,2,1,3,2,1,1,2,1,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,1,3,2,1,3,2,1,2,1,1,2,1,1,2,1,2,1,1,3,2,1,3,2,1,1,2,1,1,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,3,2,1,1,2,1,1,3,2,1,3,2,1,2,1,1,2,1,2,1,2,1,1,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,1,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,1,2,1,3,2,1,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,3,2,1,1,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,3,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,3,2,1,3,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,1,3,2,1,1,1,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,3,2,1,1,2,1,2,1,1,1,2,1,2,1,1,1,1,2,1,3,2,1,2,1,3,2,1,2,1,1,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,3,2,1,3,2,1,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,1,2,1,2,1,1,2,1,1,2,1,3,2,1,3,2,1,2,1,1,2,1,1,1,2,1,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,1,2,1,2,1,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,4,3,2,1,4,3,2,1,4,3,2,1,1,2,1,3,2,1,2,1,1,3,2,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,1,3,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,3,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1],"label":["rowSums","rowSums","rowSums","rowSums","rowMeans","rowMeans","rowMeans","rowMeans","<GC>","aperm.default","apply","aperm.default","apply","aperm.default","apply","aperm.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","mean.default","apply","apply","mean.default","apply","apply","apply","apply","apply","FUN","apply","mean.default","apply","<GC>","FUN","apply","apply","FUN","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","mean.default","apply","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","mean.default","apply","length","local","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","apply","mean.default","apply","apply","mean.default","apply","apply","FUN","apply","apply","apply","FUN","apply","apply","<GC>","is.numeric","local","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","<GC>","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","apply","<GC>","apply","isTRUE","mean.default","apply","apply","apply","mean.default","apply","apply","apply","mean.default","apply","FUN","apply","<GC>","apply","apply","mean.default","apply","apply","FUN","apply","apply","FUN","apply","mean.default","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","length","local","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","is.numeric","local","FUN","apply","FUN","apply","FUN","apply","apply","<GC>","apply","apply","mean.default","apply","apply","FUN","apply","apply","FUN","apply","apply","<GC>","apply","mean.default","apply","FUN","apply","FUN","apply","apply","apply","apply","mean.default","apply","<GC>","FUN","apply","length","local","FUN","apply","FUN","apply","apply","apply","apply","apply","<GC>","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","<GC>","apply","mean.default","apply","apply","FUN","apply","is.na","local","FUN","apply","apply","FUN","apply","<GC>","mean.default","apply","FUN","apply","mean.default","apply","is.na","local","apply","FUN","apply","length","local","FUN","apply","<GC>","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","<GC>","FUN","apply","FUN","apply","apply","apply","mean.default","apply","apply","mean.default","apply","mean.default","apply","<GC>","is.numeric","local","mean.default","apply","FUN","apply","length","local","mean.default","apply","FUN","apply","FUN","apply","apply","<GC>","length","local","isTRUE","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","is.na","local","apply","FUN","apply","<GC>","mean.default","apply","apply","apply","apply","apply","isTRUE","mean.default","apply","mean.default","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","length","local","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","apply","mean.default","apply","<GC>","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","<GC>","apply","is.na","local","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","is.numeric","local","FUN","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","<GC>","is.na","local","apply","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","<GC>","apply","FUN","apply","length","local","apply","FUN","apply","FUN","apply","length","local","<GC>","mean.default","apply","length","local","apply","mean.default","apply","mean.default","apply","apply","apply","<GC>","FUN","apply","apply","mean.default","apply","FUN","apply","apply","apply","FUN","apply","<GC>","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","apply","mean.default","apply","mean.default","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","apply","FUN","apply","<GC>","mean.default","apply","length","local","apply","FUN","apply","mean.default","apply","apply","apply","<GC>","FUN","apply","apply","apply","FUN","apply","is.na","local","apply","<GC>","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","<GC>","mean.default","apply","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","FUN","apply","is.numeric","local","FUN","apply","mean.default","apply","is.numeric","local","isTRUE","mean.default","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","apply","FUN","apply","apply","<GC>","mean.default","apply","is.numeric","local","apply","mean.default","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","<GC>","length","local","length","local","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","apply","length","local","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","apply","mean.default","apply","isTRUE","mean.default","apply","apply","apply","apply","FUN","apply","apply","isTRUE","mean.default","apply","mean.default","apply","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","FUN","apply","apply","apply","apply","apply","FUN","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","apply","apply","mean.default","apply","mean.default","apply","apply","is.numeric","local","apply","FUN","apply","<GC>","FUN","apply","mean.default","apply","is.na","local","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","is.numeric","local","apply","apply","apply","apply","<GC>","FUN","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","isTRUE","mean.default","apply","apply","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","length","local","is.numeric","local","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","apply","FUN","apply","mean.default","apply","FUN","apply","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","<GC>","mean.default","apply","apply","apply","FUN","apply","mean.default","apply","apply","apply","apply","is.numeric","local","FUN","apply","FUN","apply","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","FUN","apply","is.numeric","local","apply","length","local","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","FUN","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","<GC>","apply","<GC>","apply","is.numeric","local","FUN","apply","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","<GC>","apply","FUN","apply","isTRUE","mean.default","apply","is.numeric","local","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","mean.default","apply","apply","<GC>","mean.default","apply","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","FUN","apply","is.numeric","local","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","apply","mean.default","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","<GC>","FUN","apply","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","apply","<GC>","length","local","<GC>","length","local","mean.default","apply","apply","mean.default","apply","apply","apply","isTRUE","mean.default","apply","is.na","local","FUN","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","mean.default","apply","apply","mean.default","apply","apply","apply","mean.default","apply","FUN","apply","apply","apply","apply","FUN","apply","FUN","apply","<GC>","isTRUE","mean.default","apply","apply","FUN","apply","apply","mean.default","apply","FUN","apply","length","local","FUN","apply","FUN","apply","FUN","apply","apply","is.numeric","local","<GC>","is.na","local","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","length","local","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","FUN","apply","FUN","apply","apply","is.numeric","local","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","mean.default","apply","FUN","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","isTRUE","mean.default","apply","apply","<GC>","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","FUN","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","apply","apply","apply","FUN","apply","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","length","local","is.na","local","FUN","apply","<GC>","apply","<GC>","apply","apply","apply","is.na","local","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","<GC>","apply","<GC>","apply","mean.default","apply","apply","apply","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","apply","<GC>","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","apply","mean.default","apply","apply","apply","FUN","apply","apply","FUN","apply","<GC>","is.numeric","local","is.na","local","length","local","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","length","local","FUN","apply","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","mean.default","apply","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","apply","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","<GC>","isTRUE","mean.default","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","length","local","apply","FUN","apply","apply","mean.default","apply","<GC>","apply","apply","is.numeric","local","apply","isTRUE","mean.default","apply","length","local","apply","apply","mean.default","apply","FUN","apply","<GC>","isTRUE","mean.default","apply","FUN","apply","is.na","local","apply","mean.default","apply","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","<GC>","apply","is.na","local","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","mean.default","apply","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","is.na","local","FUN","apply","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","mean.default","apply","apply","apply","<GC>","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","apply","FUN","apply","apply","mean.default","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","apply","FUN","apply","apply","mean.default","apply","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","apply","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","FUN","apply","length","local","length","local","FUN","apply","mean.default","apply","FUN","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","apply","<GC>","apply","mean.default","apply","apply","mean.default","apply","isTRUE","mean.default","apply","apply","mean.default","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","length","local","apply","FUN","apply","mean.default","apply","is.numeric","local","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","mean.default","apply","length","local","apply","mean.default","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","<GC>","apply","<GC>","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","apply","<GC>","apply","<GC>","apply","isTRUE","mean.default","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","length","local","length","local","apply","FUN","apply","<GC>","apply","<GC>","apply","mean.default","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","apply","apply","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","isTRUE","mean.default","apply","length","local","mean.default","apply","apply","isTRUE","mean.default","apply","apply","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","is.na","local","is.numeric","local","FUN","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","apply","<GC>","is.numeric","local","<GC>","is.numeric","local","mean.default","apply","apply","FUN","apply","FUN","apply","length","local","apply","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","apply","apply","FUN","apply","apply","is.numeric","local","mean.default","apply","FUN","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","<GC>","apply","apply","isTRUE","mean.default","apply","apply","is.numeric","local","mean.default","apply","apply","apply","mean.default","apply","FUN","apply","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","length","local","apply","apply","apply","<GC>","apply","<GC>","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","length","local","length","local","isTRUE","mean.default","apply","FUN","apply","length","local","mean.default","apply","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","mean.default","apply","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","is.numeric","local","apply","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","FUN","apply","apply","apply","mean.default","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","FUN","apply","length","local","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","FUN","apply","is.na","local","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","mean.default","apply","FUN","apply","apply","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","apply","FUN","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","apply","length","local","isTRUE","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","apply","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis"],"filenum":[1,1,1,1,1,1,1,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,1,1,1,1,null,1,null,1,null,null,1,1,null,1,null,1,null,1,null,null,1,1,null,1,null,null,1,null,null,null,1,null,1,null,null,null,1,null,1,null,1,null,1,1,null,1,1,null,1,1,null,1,1,1,null,1,1,null,null,null,1,1,1,null,1,null,1,null,1,null,1,1,null,null,1,null,1,null,null,1,null,1,1,null,1,null,null,1,1,null,1,null,null,1,1,1,null,1,1,1,null,1,null,1,null,1,1,null,1,1,null,1,1,null,1,null,1,null,null,1,null,null,1,null,null,null,1,null,1,null,1,null,1,null,1,null,null,1,1,null,null,1,null,null,1,null,null,null,1,null,1,null,1,1,null,1,1,null,1,1,null,1,1,null,1,1,null,1,null,1,null,1,null,1,1,1,1,null,1,null,null,1,null,null,null,1,null,1,1,1,1,1,null,1,1,1,null,1,null,1,null,1,null,null,1,1,null,1,null,1,1,null,1,null,null,null,1,1,null,1,null,null,1,null,1,null,1,null,null,1,null,1,null,null,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,1,null,null,1,null,1,1,1,null,1,1,null,1,null,1,null,null,null,null,1,null,1,null,null,null,1,null,1,null,1,1,null,null,null,null,null,1,null,null,1,null,1,null,null,1,null,1,null,null,1,1,1,1,1,null,null,1,null,1,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,null,1,1,null,1,null,null,1,1,null,1,null,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,null,1,null,1,null,1,1,null,null,1,null,null,1,null,1,null,null,null,1,null,1,null,1,null,1,null,1,null,null,null,1,1,null,1,null,1,null,null,1,1,null,1,null,1,null,null,1,null,1,null,1,null,null,null,null,1,null,null,1,null,1,null,1,1,1,null,null,1,1,null,1,null,1,1,1,null,1,null,1,null,null,1,null,1,null,1,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,1,null,1,null,null,1,null,null,1,null,1,null,1,1,1,null,null,1,1,1,null,1,null,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,null,1,1,null,1,null,1,null,1,null,null,1,null,1,null,null,1,null,null,null,1,null,1,null,null,null,null,1,null,null,1,null,1,null,1,null,1,1,null,1,1,null,null,1,null,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,null,null,null,null,null,1,1,null,1,null,null,1,null,1,null,null,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,1,null,1,null,null,1,1,1,1,null,1,1,null,null,1,null,1,1,null,null,1,null,null,1,null,null,1,null,1,null,1,1,1,1,1,null,1,null,1,1,null,1,null,1,null,1,null,null,1,null,1,1,null,1,null,1,1,1,1,null,1,null,1,1,null,null,1,null,1,null,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,null,1,1,1,1,null,null,1,null,1,null,1,null,null,1,1,null,null,1,1,1,null,null,1,1,null,1,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,null,null,null,null,1,null,1,null,1,null,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,1,1,null,1,null,1,1,1,1,null,null,null,1,null,1,null,1,1,null,null,1,null,null,1,null,1,1,null,1,null,1,1,null,1,null,1,null,null,1,null,null,null,1,null,null,1,null,null,1,1,null,1,null,1,1,1,null,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,null,null,1,1,null,1,null,1,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,1,1,null,1,null,1,1,null,null,1,1,null,1,null,1,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,null,1,null,1,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,1,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,null,null,null,null,null,null,1,1,null,1,1,1,null,null,1,null,null,null,1,null,null,1,null,1,null,null,1,1,null,1,1,1,null,1,null,1,1,1,1,null,1,null,1,null,null,null,1,1,null,1,1,null,1,null,1,null,null,null,1,null,1,null,1,1,null,null,null,null,null,1,null,null,1,null,1,null,1,null,null,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,null,1,null,null,1,null,1,1,null,null,null,1,null,null,null,1,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,null,1,1,null,null,1,null,1,null,1,null,1,1,null,1,1,null,1,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,1,1,1,null,1,1,null,1,null,null,1,null,null,1,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,1,null,1,null,1,null,null,null,null,null,1,null,1,null,1,1,1,null,null,1,1,null,1,1,null,1,null,1,null,1,null,1,null,1,1,1,null,1,null,1,1,null,null,1,null,1,1,null,1,1,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,1,null,1,1,null,1,1,1,null,1,1,null,1,null,null,null,null,null,null,null,null,1,null,1,null,1,null,1,null,null,null,1,1,null,null,null,1,null,null,null,1,null,1,null,1,null,1,null,1,1,1,null,1,1,null,null,null,1,null,null,null,1,null,1,null,1,1,1,null,1,null,1,null,1,null,1,null,1,null,null,null,1,null,null,1,null,null,1,null,1,null,1,null,null,1,null,1,1,null,1,null,1,1,null,null,1,null,null,1,null,null,1,1,null,1,null,1,null,null,null,1,null,1,null,null,1,null,1,1,null,1,null,null,1,null,1,null,null,1,null,1,null,null,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,null,1,null,1,1,1,null,1,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,1,null,null,1,null,null,null,1,1,null,null,null,1,null,null,null,1,1,null,1,null,1,null,null,1,1,null,1,1,1,null,1,null,1,null,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,1,null,1,1,null,null,1,null,null,1,null,1,1,null,1,1,null,1,null,1,1,null,null,1,null,null,1,1,null,1,1,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,1,null,1,null,null,1,null,1,null,1,null,null,null,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,1,null,1,null,null,1,1,null,1,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,null,1,1,null,null,1,null,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,null,1,null,null,1,1,1,null,1,null,1,null,1,1,null,1,null,1,1,null,1,null,1,1,null,1,null,null,1,1,null,1,null,1,null,null,1,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,null,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,null,1,1,null,null,1,1,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,1,null,1,null,1,null,1,null,1,null,null,null,null,null,1,null,1,null,null,1,null,1,null,null,1,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,1,null,1,1,null,null,null,null,null,null,null,1,1,null,1,null,1,null,null,1,null,1,null,1,1,null,null,1,1,1,1,null,1,1,null,null,null,1,null,1,null,1,1,null,1,null,1,null,1,1,null,null,1,1,null,null,null,1,1,1,null,1,null,1,1,1,1,null,1,null,null,1,null,1,null,null,1,null,null,1,1,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,1,1,null,null,null,null,null,null,1,null,1,null,null,null,1,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,null,1,null,null,1,1,null,1,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,1,1,null,1,null,1,1,null,1,1,null,1,null,null,1,null,null,1,null,1,1,null,1,1,1,null,1,1,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,null,null,null,1,null,null,1,null,null,1,1,null,1,1,null,1,null,1,null,1,null,null,null,1,null,1,null,1,null,null,1,null,null,1,1,null,1,null,1,1,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,1,null,1,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,1,null,1,null,null,null,1,null,null,null,1,null,null,null,1,1,null,null,null,null,1,null,1,1,null,null,1,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,1,1,null,null,1,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,1,1,null,1,null,null,1,null,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null],"linenum":[10,10,10,10,11,11,11,11,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,12,12,12,12,null,12,null,12,null,null,12,12,null,12,null,12,null,12,null,null,12,12,null,12,null,null,12,null,null,null,12,null,12,null,null,null,12,null,12,null,12,null,12,12,null,12,12,null,12,12,null,12,12,12,null,12,12,null,null,null,12,12,12,null,12,null,12,null,12,null,12,12,null,null,12,null,12,null,null,12,null,12,12,null,12,null,null,12,12,null,12,null,null,12,12,12,null,12,12,12,null,12,null,12,null,12,12,null,12,12,null,12,12,null,12,null,12,null,null,12,null,null,12,null,null,null,12,null,12,null,12,null,12,null,12,null,null,12,12,null,null,12,null,null,12,null,null,null,12,null,12,null,12,12,null,12,12,null,12,12,null,12,12,null,12,12,null,12,null,12,null,12,null,12,12,12,12,null,12,null,null,12,null,null,null,12,null,12,12,12,12,12,null,12,12,12,null,12,null,12,null,12,null,null,12,12,null,12,null,12,12,null,12,null,null,null,12,12,null,12,null,null,12,null,12,null,12,null,null,12,null,12,null,null,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,12,null,null,12,null,12,12,12,null,12,12,null,12,null,12,null,null,null,null,12,null,12,null,null,null,12,null,12,null,12,12,null,null,null,null,null,12,null,null,12,null,12,null,null,12,null,12,null,null,12,12,12,12,12,null,null,12,null,12,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,null,12,12,null,12,null,null,12,12,null,12,null,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,null,12,null,12,null,12,12,null,null,12,null,null,12,null,12,null,null,null,12,null,12,null,12,null,12,null,12,null,null,null,12,12,null,12,null,12,null,null,12,12,null,12,null,12,null,null,12,null,12,null,12,null,null,null,null,12,null,null,12,null,12,null,12,12,12,null,null,12,12,null,12,null,12,12,12,null,12,null,12,null,null,12,null,12,null,12,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,12,null,12,null,null,12,null,null,12,null,12,null,12,12,12,null,null,12,12,12,null,12,null,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,null,12,12,null,12,null,12,null,12,null,null,12,null,12,null,null,12,null,null,null,12,null,12,null,null,null,null,12,null,null,12,null,12,null,12,null,12,12,null,12,12,null,null,12,null,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,null,null,null,null,null,12,12,null,12,null,null,12,null,12,null,null,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,12,null,12,null,null,12,12,12,12,null,12,12,null,null,12,null,12,12,null,null,12,null,null,12,null,null,12,null,12,null,12,12,12,12,12,null,12,null,12,12,null,12,null,12,null,12,null,null,12,null,12,12,null,12,null,12,12,12,12,null,12,null,12,12,null,null,12,null,12,null,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,null,12,12,12,12,null,null,12,null,12,null,12,null,null,12,12,null,null,12,12,12,null,null,12,12,null,12,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,null,null,null,null,12,null,12,null,12,null,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,12,12,null,12,null,12,12,12,12,null,null,null,12,null,12,null,12,12,null,null,12,null,null,12,null,12,12,null,12,null,12,12,null,12,null,12,null,null,12,null,null,null,12,null,null,12,null,null,12,12,null,12,null,12,12,12,null,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,null,null,12,12,null,12,null,12,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,12,12,null,12,null,12,12,null,null,12,12,null,12,null,12,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,null,12,null,12,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,12,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,null,null,null,null,null,null,12,12,null,12,12,12,null,null,12,null,null,null,12,null,null,12,null,12,null,null,12,12,null,12,12,12,null,12,null,12,12,12,12,null,12,null,12,null,null,null,12,12,null,12,12,null,12,null,12,null,null,null,12,null,12,null,12,12,null,null,null,null,null,12,null,null,12,null,12,null,12,null,null,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,null,12,null,null,12,null,12,12,null,null,null,12,null,null,null,12,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,null,12,12,null,null,12,null,12,null,12,null,12,12,null,12,12,null,12,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,12,12,12,null,12,12,null,12,null,null,12,null,null,12,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,12,null,12,null,12,null,null,null,null,null,12,null,12,null,12,12,12,null,null,12,12,null,12,12,null,12,null,12,null,12,null,12,null,12,12,12,null,12,null,12,12,null,null,12,null,12,12,null,12,12,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,12,null,12,12,null,12,12,12,null,12,12,null,12,null,null,null,null,null,null,null,null,12,null,12,null,12,null,12,null,null,null,12,12,null,null,null,12,null,null,null,12,null,12,null,12,null,12,null,12,12,12,null,12,12,null,null,null,12,null,null,null,12,null,12,null,12,12,12,null,12,null,12,null,12,null,12,null,12,null,null,null,12,null,null,12,null,null,12,null,12,null,12,null,null,12,null,12,12,null,12,null,12,12,null,null,12,null,null,12,null,null,12,12,null,12,null,12,null,null,null,12,null,12,null,null,12,null,12,12,null,12,null,null,12,null,12,null,null,12,null,12,null,null,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,null,12,null,12,12,12,null,12,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,12,null,null,12,null,null,null,12,12,null,null,null,12,null,null,null,12,12,null,12,null,12,null,null,12,12,null,12,12,12,null,12,null,12,null,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,12,null,12,12,null,null,12,null,null,12,null,12,12,null,12,12,null,12,null,12,12,null,null,12,null,null,12,12,null,12,12,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,12,null,12,null,null,12,null,12,null,12,null,null,null,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,12,null,12,null,null,12,12,null,12,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,null,12,12,null,null,12,null,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,null,12,null,null,12,12,12,null,12,null,12,null,12,12,null,12,null,12,12,null,12,null,12,12,null,12,null,null,12,12,null,12,null,12,null,null,12,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,null,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,12,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,null,12,12,null,null,12,12,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,null,null,12,null,12,null,12,null,12,null,12,null,null,null,null,null,12,null,12,null,null,12,null,12,null,null,12,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,12,null,12,12,null,null,null,null,null,null,null,12,12,null,12,null,12,null,null,12,null,12,null,12,12,null,null,12,12,12,12,null,12,12,null,null,null,12,null,12,null,12,12,null,12,null,12,null,12,12,null,null,12,12,null,null,null,12,12,12,null,12,null,12,12,12,12,null,12,null,null,12,null,12,null,null,12,null,null,12,12,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,12,12,null,null,null,null,null,null,12,null,12,null,null,null,12,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,null,12,null,null,12,12,null,12,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,12,12,null,12,null,12,12,null,12,12,null,12,null,null,12,null,null,12,null,12,12,null,12,12,12,null,12,12,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,null,null,null,12,null,null,12,null,null,12,12,null,12,12,null,12,null,12,null,12,null,null,null,12,null,12,null,12,null,null,12,null,null,12,12,null,12,null,12,12,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,12,null,12,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,12,null,12,null,null,null,12,null,null,null,12,null,null,null,12,12,null,null,null,null,12,null,12,12,null,null,12,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,12,12,null,null,12,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,12,12,null,12,null,null,12,null,12,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null],"memalloc":[124.4599304199219,124.4599304199219,124.4599304199219,124.4599304199219,139.7421646118164,139.7421646118164,139.7421646118164,139.7421646118164,124.4535903930664,124.4535903930664,124.4535903930664,170.2079086303711,170.2079086303711,170.2079086303711,170.2079086303711,170.2079086303711,170.2079086303711,170.2079544067383,170.2079544067383,170.2079544067383,170.2079544067383,170.2079544067383,170.2079544067383,170.2079544067383,170.2079544067383,170.2079544067383,170.2079544067383,170.2079544067383,170.2079544067383,170.2079544067383,170.2079544067383,170.207649230957,170.207649230957,185.5920028686523,185.5920028686523,185.8430023193359,186.1131210327148,186.1131210327148,186.4232406616211,186.7598037719727,187.1128616333008,187.4855728149414,187.8942031860352,187.8942031860352,188.3072814941406,188.3072814941406,188.7229766845703,188.7229766845703,188.7229766845703,185.723388671875,186.1000671386719,186.1000671386719,186.5154418945312,186.5154418945312,186.9409637451172,186.9409637451172,187.3515853881836,187.3515853881836,187.3515853881836,187.7589111328125,188.1647415161133,188.1647415161133,188.5718612670898,188.5718612670898,188.5718612670898,188.792610168457,188.792610168457,188.792610168457,188.792610168457,185.9996185302734,185.9996185302734,186.365852355957,186.365852355957,186.7569580078125,186.7569580078125,187.1742782592773,187.1742782592773,187.5840377807617,187.5840377807617,187.9876098632812,187.9876098632812,188.3910675048828,188.7976303100586,188.7976303100586,185.8866958618164,186.2492218017578,186.2492218017578,186.6207122802734,187.0200271606445,187.0200271606445,187.4352035522461,187.8437805175781,188.2483749389648,188.2483749389648,188.6576385498047,188.965217590332,188.965217590332,188.965217590332,186.1771850585938,186.5236892700195,186.8922958374023,187.2876586914062,187.2876586914062,187.6925354003906,187.6925354003906,188.0937805175781,188.0937805175781,188.4961471557617,188.4961471557617,188.8982925415039,189.0494842529297,189.0494842529297,189.0494842529297,186.4304504394531,186.4304504394531,186.7856216430664,186.7856216430664,186.7856216430664,187.1620025634766,187.1620025634766,187.5618438720703,187.9684906005859,187.9684906005859,188.3734970092773,188.3734970092773,188.3734970092773,188.7798309326172,189.1323089599609,189.1323089599609,186.3766555786133,186.3766555786133,186.3766555786133,186.748176574707,187.1079025268555,187.4776000976562,187.4776000976562,187.8744888305664,188.2797317504883,188.6836471557617,188.6836471557617,189.0922927856445,189.0922927856445,189.2138977050781,189.2138977050781,186.6882019042969,187.0360336303711,187.0360336303711,187.4013366699219,187.791259765625,187.791259765625,188.1942596435547,188.5995025634766,188.5995025634766,189.0069808959961,189.0069808959961,189.2940368652344,189.2940368652344,189.2940368652344,186.670524597168,186.670524597168,186.670524597168,187.0142822265625,187.0142822265625,187.3766174316406,187.3766174316406,187.7542572021484,187.7542572021484,188.1488876342773,188.1488876342773,188.5532531738281,188.5532531738281,188.9629364013672,188.9629364013672,189.3730239868164,189.3730239868164,189.3730239868164,186.6963119506836,187.0265121459961,187.0265121459961,187.0265121459961,187.383430480957,187.383430480957,187.383430480957,187.7487716674805,187.7487716674805,188.1328659057617,188.1328659057617,188.5312118530273,188.5312118530273,188.9391937255859,188.9391937255859,189.3509750366211,189.4505844116211,189.4505844116211,187.052978515625,187.3956298828125,187.3956298828125,187.7529525756836,188.1277694702148,188.1277694702148,188.5234680175781,188.9268188476562,188.9268188476562,189.3379592895508,189.5270156860352,189.5270156860352,187.0951766967773,187.0951766967773,187.4371566772461,187.4371566772461,187.8233871459961,187.8233871459961,188.1931076049805,188.5857925415039,188.9834518432617,189.3909301757812,189.3909301757812,189.6021957397461,189.6021957397461,189.6021957397461,187.1958312988281,187.1958312988281,187.527961730957,187.527961730957,187.8750610351562,187.8750610351562,188.2394104003906,188.6254653930664,189.0234375,189.4286117553711,189.6760559082031,189.6760559082031,187.2834548950195,187.6113128662109,187.9566497802734,187.9566497802734,188.3196411132812,188.3196411132812,188.7048110961914,188.7048110961914,189.101936340332,189.101936340332,189.101936340332,189.5068588256836,189.748893737793,189.748893737793,187.3886489868164,187.3886489868164,187.7073593139648,188.0472030639648,188.0472030639648,188.40185546875,188.40185546875,188.778923034668,188.778923034668,189.1606521606445,189.5554046630859,189.5554046630859,189.8203964233398,189.8203964233398,189.8203964233398,187.4793853759766,187.4793853759766,187.7938690185547,187.7938690185547,188.1267318725586,188.1267318725586,188.4784317016602,188.85546875,188.85546875,189.2466430664062,189.2466430664062,189.6461639404297,189.6461639404297,189.8908309936523,189.8908309936523,187.5991058349609,187.5991058349609,187.9109115600586,187.9109115600586,188.2745132446289,188.2745132446289,188.6286239624023,188.6286239624023,189.0095901489258,189.0095901489258,189.0095901489258,189.4019546508789,189.4019546508789,189.4019546508789,189.8012161254883,189.9601364135742,189.9601364135742,189.9601364135742,187.7656402587891,187.7656402587891,188.0761871337891,188.407600402832,188.7620468139648,188.7620468139648,189.1369857788086,189.52783203125,189.52783203125,189.9273452758789,189.9273452758789,190.0282440185547,190.0282440185547,190.0282440185547,187.9140853881836,187.9140853881836,188.2188873291016,188.2188873291016,188.5491714477539,188.5491714477539,188.9039459228516,188.9039459228516,189.2761154174805,189.2761154174805,189.6665496826172,189.6665496826172,190.065299987793,190.0952835083008,190.0952835083008,190.0952835083008,188.0676193237305,188.0676193237305,188.0676193237305,188.3796081542969,188.3796081542969,188.3796081542969,188.7186050415039,188.7186050415039,189.0774917602539,189.0774917602539,189.4597320556641,189.852897644043,189.852897644043,190.1612548828125,190.1612548828125,190.1612548828125,187.9664916992188,188.2561798095703,188.5715103149414,188.9157257080078,189.2777557373047,189.2777557373047,189.2777557373047,189.6610336303711,189.6610336303711,190.0524139404297,190.2261962890625,190.2261962890625,190.2261962890625,190.2261962890625,190.2261962890625,190.2261962890625,190.2261962890625,190.2261962890625,190.2261962890625,190.2261962890625,190.2261962890625,190.2261962890625,190.2261962890625,190.2261962890625,190.2261962890625,190.2261962890625,190.2261962890625,190.2261962890625,190.2261962890625,190.2261962890625,190.2261962890625,190.2261962890625,190.2261962890625,190.2261962890625,190.2261962890625,190.2261962890625,190.2261962890625,188.0789642333984,188.0789642333984,188.0789642333984,188.2990341186523,188.2990341186523,188.5334091186523,188.5334091186523,188.7952194213867,189.0908966064453,189.0908966064453,189.4136199951172,189.4136199951172,189.4136199951172,189.7470016479492,190.0995712280273,190.0995712280273,190.2897644042969,190.2897644042969,190.2897644042969,188.234016418457,188.234016418457,188.5211181640625,188.5211181640625,188.843635559082,188.843635559082,189.1905517578125,189.1905517578125,189.5534896850586,189.9470291137695,189.9470291137695,190.3523635864258,190.3523635864258,188.1939010620117,188.1939010620117,188.4769668579102,188.4769668579102,188.7808685302734,188.7808685302734,189.1211318969727,189.1211318969727,189.4751129150391,189.4751129150391,189.8442687988281,189.8442687988281,190.2290725708008,190.4145202636719,190.4145202636719,188.4557571411133,188.4557571411133,188.7417526245117,189.0634002685547,189.0634002685547,189.4134750366211,189.4134750366211,189.7767105102539,190.1652374267578,190.1652374267578,190.1652374267578,190.4753189086914,190.4753189086914,190.4753189086914,188.4351577758789,188.4351577758789,188.7116928100586,188.7116928100586,189.0189056396484,189.0189056396484,189.3633651733398,189.3633651733398,189.7215805053711,189.7215805053711,190.1001892089844,190.1001892089844,190.5003128051758,190.5003128051758,190.5352249145508,190.5352249145508,190.5352249145508,188.720832824707,189.0168609619141,189.3477783203125,189.3477783203125,189.7022018432617,189.7022018432617,190.0719604492188,190.0719604492188,190.0719604492188,190.4678802490234,190.5941467285156,190.5941467285156,188.7471694946289,188.7471694946289,189.0311050415039,189.0311050415039,189.3519134521484,189.7015686035156,189.7015686035156,190.0653305053711,190.0653305053711,190.4535369873047,190.4535369873047,190.6520080566406,190.6520080566406,190.6520080566406,188.7878189086914,188.7878189086914,189.0686645507812,189.3884735107422,189.3884735107422,189.7378234863281,189.7378234863281,190.105598449707,190.4950485229492,190.7090759277344,190.7090759277344,190.7090759277344,188.8947219848633,189.1699523925781,189.1699523925781,189.4838409423828,189.4838409423828,189.8252105712891,190.1810760498047,190.5633850097656,190.5633850097656,190.7651672363281,190.7651672363281,188.9536209106445,188.9536209106445,188.9536209106445,189.2324447631836,189.2324447631836,189.5491790771484,189.5491790771484,189.893798828125,190.2549896240234,190.2549896240234,190.6197662353516,190.6197662353516,190.8203277587891,190.8203277587891,190.8203277587891,189.0253982543945,189.0253982543945,189.2973861694336,189.2973861694336,189.6072845458984,189.6072845458984,189.9536514282227,189.9536514282227,190.3124160766602,190.6997756958008,190.6997756958008,190.8746032714844,190.8746032714844,190.8746032714844,189.1459579467773,189.1459579467773,189.4216766357422,189.7395706176758,189.7395706176758,190.0889663696289,190.0889663696289,190.4506683349609,190.8407516479492,190.9280776977539,190.9280776977539,190.9280776977539,189.2822875976562,189.5689468383789,189.8962249755859,189.8962249755859,190.2385940551758,190.2385940551758,190.6004638671875,190.9805450439453,190.9805450439453,189.1834259033203,189.1834259033203,189.4450607299805,189.4450607299805,189.7402725219727,190.0774841308594,190.0774841308594,190.4349212646484,190.4349212646484,190.8070907592773,190.8070907592773,191.0322875976562,191.0322875976562,191.0322875976562,189.3460159301758,189.6161727905273,189.6161727905273,189.9300994873047,189.9300994873047,190.2759628295898,190.2759628295898,190.6373062133789,190.6373062133789,190.6373062133789,191.0252456665039,191.0252456665039,191.0831680297852,191.0831680297852,191.0831680297852,189.5433883666992,189.5433883666992,189.8286819458008,189.8286819458008,190.1575317382812,190.1575317382812,190.5120162963867,190.5120162963867,190.8817367553711,190.8817367553711,190.8817367553711,191.1331787109375,191.1331787109375,191.1331787109375,189.4855117797852,189.4855117797852,189.7513580322266,189.7513580322266,190.057975769043,190.057975769043,190.3989868164062,190.7597122192383,190.7597122192383,191.1401443481445,191.1823883056641,191.1823883056641,191.1823883056641,189.6957778930664,189.6957778930664,189.9835357666016,190.3130950927734,190.3130950927734,190.6691207885742,190.6691207885742,191.0425338745117,191.0425338745117,191.2308349609375,191.2308349609375,191.2308349609375,189.7033843994141,189.7033843994141,189.9832763671875,189.9832763671875,190.3057479858398,190.3057479858398,190.6565704345703,190.6565704345703,191.0243682861328,191.0243682861328,191.2784423828125,191.2784423828125,191.2784423828125,189.7080764770508,189.7080764770508,189.9744262695312,189.9744262695312,190.2826309204102,190.6263275146484,190.6263275146484,190.9920272827148,190.9920272827148,190.9920272827148,191.3253631591797,191.3253631591797,189.7269821166992,189.7269821166992,189.9864807128906,189.9864807128906,190.2838973999023,190.2838973999023,190.6184234619141,190.6184234619141,190.9775695800781,190.9775695800781,191.3550415039062,191.3550415039062,191.3550415039062,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,191.3714981079102,189.783203125,189.783203125,189.783203125,189.783203125,189.783203125,189.783203125,189.9839477539062,189.9839477539062,190.2338256835938,190.2338256835938,190.5088653564453,190.8133163452148,190.8133163452148,191.1286010742188,191.1286010742188,191.1286010742188,191.4541549682617,191.8268737792969,192.2292938232422,192.6250381469727,192.6250381469727,192.9620208740234,193.296257019043,193.296257019043,193.296257019043,193.6649475097656,193.6649475097656,194.0006713867188,194.3370056152344,194.3370056152344,194.3370056152344,194.6224975585938,194.6224975585938,194.6224975585938,194.6224975585938,194.6224975585938,194.6224975585938,190.2759094238281,190.2759094238281,190.6192474365234,190.6192474365234,190.9771118164062,191.3185882568359,191.7085189819336,192.1310424804688,192.5424652099609,192.5424652099609,192.9518508911133,192.9518508911133,193.3593063354492,193.7647171020508,193.7647171020508,194.1701965332031,194.1701965332031,194.5690536499023,194.5690536499023,194.7548828125,194.7548828125,194.7548828125,190.2736053466797,190.2736053466797,190.581901550293,190.9246215820312,190.9246215820312,191.2671508789062,191.2671508789062,191.6086120605469,192.0130310058594,192.43359375,192.843635559082,192.843635559082,193.2527084350586,193.2527084350586,193.6598815917969,194.0672302246094,194.0672302246094,194.4746627807617,194.868782043457,194.868782043457,194.8851165771484,194.8851165771484,194.8851165771484,190.5868606567383,190.5868606567383,190.8971099853516,190.8971099853516,191.2297821044922,191.5507278442383,191.5507278442383,191.9274749755859,191.9274749755859,192.3333511352539,192.3333511352539,192.7899398803711,192.7899398803711,193.1958618164062,193.1958618164062,193.6009902954102,194.0036010742188,194.4087753295898,194.8090362548828,195.0132369995117,195.0132369995117,195.0132369995117,190.6494293212891,190.6494293212891,190.9399642944336,190.9399642944336,191.2591781616211,191.2591781616211,191.2591781616211,191.5761337280273,191.929328918457,191.929328918457,191.929328918457,192.3126068115234,192.7246246337891,193.1320495605469,193.1320495605469,193.1320495605469,193.5371856689453,193.9393768310547,193.9393768310547,194.3443450927734,194.7504653930664,194.7504653930664,194.7504653930664,195.1392974853516,195.1392974853516,195.1392974853516,195.1392974853516,195.1392974853516,195.1392974853516,190.995246887207,190.995246887207,191.2981414794922,191.2981414794922,191.6071166992188,191.6071166992188,191.9372482299805,191.9372482299805,192.3092193603516,192.3092193603516,192.7049102783203,192.7049102783203,193.1072616577148,193.1072616577148,193.5046081542969,193.5046081542969,193.9053497314453,193.9053497314453,193.9053497314453,194.3066635131836,194.3066635131836,194.7104110717773,194.7104110717773,195.1068420410156,195.1068420410156,195.1068420410156,195.2633361816406,195.2633361816406,191.0631103515625,191.0631103515625,191.3533706665039,191.3533706665039,191.6590270996094,191.6590270996094,192.0090713500977,192.3704071044922,192.3704071044922,192.7549438476562,193.1633987426758,193.1633987426758,193.5654525756836,193.5654525756836,193.9647827148438,193.9647827148438,194.3648834228516,194.3648834228516,194.7664031982422,194.7664031982422,195.1639862060547,195.1639862060547,195.3853073120117,195.3853073120117,195.3853073120117,191.1976547241211,191.4758605957031,191.7714614868164,191.7714614868164,192.0748825073242,192.0748825073242,192.4244842529297,192.7924499511719,193.1815872192383,193.5818939208984,193.5818939208984,193.9824600219727,193.9824600219727,194.3858947753906,194.3858947753906,194.7892990112305,194.7892990112305,195.1937713623047,195.5054321289062,195.5054321289062,195.5054321289062,195.5054321289062,195.5054321289062,195.5054321289062,191.5985565185547,191.5985565185547,191.8869247436523,192.1920623779297,192.1920623779297,192.5400238037109,192.5400238037109,192.9109344482422,193.3026657104492,193.3026657104492,193.7112808227539,193.7112808227539,194.1140213012695,194.1140213012695,194.5173721313477,194.9189529418945,194.9189529418945,195.3206176757812,195.3206176757812,195.6234893798828,195.6234893798828,195.6234893798828,195.6234893798828,195.6234893798828,195.6234893798828,191.8039321899414,192.0881271362305,192.0881271362305,192.3995971679688,192.3995971679688,192.7497406005859,193.1199264526367,193.5081024169922,193.5081024169922,193.5081024169922,193.9169540405273,193.9169540405273,194.320182800293,194.320182800293,194.7230911254883,194.7230911254883,195.1254425048828,195.5211410522461,195.5211410522461,195.7397003173828,195.7397003173828,195.7397003173828,195.7397003173828,192.0052490234375,192.0052490234375,192.2824783325195,192.2824783325195,192.5991592407227,192.9452743530273,192.9452743530273,193.3104858398438,193.3104858398438,193.6989898681641,194.1008224487305,194.1008224487305,194.4987564086914,194.4987564086914,194.8973159790039,195.2912063598633,195.2912063598633,195.6845016479492,195.6845016479492,195.8540115356445,195.8540115356445,191.9525985717773,191.9525985717773,192.2147903442383,192.2147903442383,192.2147903442383,192.4864196777344,192.4864196777344,192.8020782470703,193.1430511474609,193.1430511474609,193.1430511474609,193.5017013549805,193.5017013549805,193.8875732421875,193.8875732421875,194.2908325195312,194.2908325195312,194.6493835449219,195.0469589233398,195.0469589233398,195.446174621582,195.446174621582,195.8789520263672,195.9664993286133,195.9664993286133,195.9664993286133,192.1813659667969,192.4420928955078,192.4420928955078,192.7279281616211,192.7279281616211,193.0525131225586,193.4001312255859,193.4001312255859,193.763557434082,193.763557434082,194.1583862304688,194.1583862304688,194.5627517700195,194.9650421142578,194.9650421142578,195.3666915893555,195.3666915893555,195.7660751342773,195.7660751342773,196.0772094726562,196.0772094726562,196.0772094726562,196.0772094726562,196.0772094726562,196.0772094726562,192.4678421020508,192.4678421020508,192.7334060668945,192.7334060668945,193.0441055297852,193.0441055297852,193.3786315917969,193.3786315917969,193.7316207885742,193.7316207885742,194.1073303222656,194.1073303222656,194.5115661621094,194.9118957519531,194.9118957519531,194.9118957519531,195.3119659423828,195.3119659423828,195.7146759033203,196.1071014404297,196.1071014404297,196.1860275268555,196.1860275268555,196.1860275268555,192.535041809082,192.535041809082,192.7906951904297,192.7906951904297,193.0839385986328,193.0839385986328,193.4087219238281,193.4087219238281,193.7890167236328,193.7890167236328,194.1607284545898,194.5564651489258,194.959228515625,194.959228515625,195.3607635498047,195.3607635498047,195.7638473510742,195.7638473510742,196.1591339111328,196.1591339111328,196.293212890625,196.293212890625,196.293212890625,192.6525268554688,192.6525268554688,192.9032363891602,192.9032363891602,193.184928894043,193.499153137207,193.499153137207,193.8341369628906,193.8341369628906,194.1942443847656,194.1942443847656,194.5784912109375,194.5784912109375,194.983154296875,194.983154296875,195.3821716308594,195.3821716308594,195.7838516235352,195.7838516235352,196.1820602416992,196.398551940918,196.398551940918,196.398551940918,196.398551940918,196.398551940918,196.398551940918,193.0092239379883,193.0092239379883,193.2761840820312,193.5796508789062,193.5796508789062,193.9088287353516,194.2649459838867,194.6460266113281,194.6460266113281,194.6460266113281,195.0420837402344,195.0420837402344,195.4449462890625,195.4449462890625,195.8510360717773,195.8510360717773,195.8510360717773,196.2551193237305,196.2551193237305,196.5022506713867,196.5022506713867,196.5022506713867,192.9357147216797,193.1878967285156,193.1878967285156,193.4616165161133,193.7633285522461,194.090576171875,194.090576171875,194.4425430297852,194.4425430297852,194.8167114257812,195.214973449707,195.6146621704102,196.0186614990234,196.0186614990234,196.4161071777344,196.4161071777344,196.6042556762695,196.6042556762695,196.6042556762695,196.6042556762695,193.0962524414062,193.3429718017578,193.3429718017578,193.6185455322266,193.9210586547852,193.9210586547852,194.2465133666992,194.2465133666992,194.6010131835938,194.6010131835938,194.9784088134766,194.9784088134766,195.380615234375,195.380615234375,195.7815628051758,195.7815628051758,196.1859283447266,196.5822830200195,196.5822830200195,196.7045974731445,196.7045974731445,196.7045974731445,193.3038482666016,193.549186706543,193.549186706543,193.549186706543,193.8240203857422,193.8240203857422,194.1217575073242,194.1217575073242,194.4504547119141,194.4504547119141,194.8044128417969,194.8044128417969,195.1809310913086,195.1809310913086,195.5850601196289,195.5850601196289,195.9804458618164,195.9804458618164,196.3799591064453,196.3799591064453,196.8033752441406,196.8033752441406,196.8033752441406,196.8033752441406,196.8033752441406,196.8033752441406,193.530876159668,193.530876159668,193.7826843261719,193.7826843261719,194.0615158081055,194.0615158081055,194.3668899536133,194.7046813964844,194.7046813964844,195.0683746337891,195.0683746337891,195.4595108032227,195.4595108032227,195.8637008666992,196.2677917480469,196.2677917480469,196.6715240478516,196.9004898071289,196.9004898071289,196.9004898071289,196.9004898071289,196.9004898071289,196.9004898071289,196.9004898071289,196.9004898071289,196.9004898071289,196.9004898071289,196.9004898071289,196.9004898071289,196.9004898071289,196.9004898071289,196.9004898071289,196.9004898071289,196.9004898071289,196.9004898071289,196.9004898071289,196.9004898071289,196.9004898071289,196.9004898071289,196.9004898071289,196.9004898071289,193.5562973022461,193.5562973022461,193.6327285766602,193.6327285766602,193.8329391479492,193.8329391479492,194.0598373413086,194.0598373413086,194.2976150512695,194.5667343139648,194.5667343139648,194.8713684082031,194.8713684082031,195.1926956176758,195.1926956176758,195.5292282104492,195.5292282104492,195.5292282104492,195.8966903686523,195.8966903686523,195.8966903686523,196.2961044311523,196.2961044311523,196.7003326416016,196.9958724975586,196.9958724975586,196.9958724975586,196.9958724975586,196.9958724975586,196.9958724975586,196.9958724975586,196.9958724975586,193.8870162963867,194.1457366943359,194.1457366943359,194.4297637939453,194.4297637939453,194.7429885864258,194.7429885864258,195.0823822021484,195.0823822021484,195.4310531616211,195.4310531616211,195.7951431274414,196.1787338256836,196.1787338256836,196.5802612304688,196.5802612304688,196.5802612304688,196.9867553710938,197.0900039672852,197.0900039672852,197.0900039672852,193.9047698974609,193.9047698974609,194.1472625732422,194.1472625732422,194.4147262573242,194.4147262573242,194.7121200561523,195.0318374633789,195.0318374633789,195.3784027099609,195.7370910644531,195.7370910644531,196.1220703125,196.5649719238281,196.5649719238281,196.974250793457,196.974250793457,197.1825332641602,197.1825332641602,197.1825332641602,197.1825332641602,197.1825332641602,197.1825332641602,194.2236557006836,194.2236557006836,194.2236557006836,194.4842224121094,194.4842224121094,194.7718811035156,194.7718811035156,195.0930099487305,195.4416122436523,195.8053283691406,196.1835403442383,196.1835403442383,196.5856094360352,196.9898986816406,196.9898986816406,197.2736053466797,197.2736053466797,197.2736053466797,197.2736053466797,197.2736053466797,197.2736053466797,194.3190383911133,194.5741119384766,194.5741119384766,194.8585739135742,194.8585739135742,195.1760559082031,195.1760559082031,195.5215530395508,195.5215530395508,195.8805313110352,195.8805313110352,196.251350402832,196.251350402832,196.251350402832,196.6456451416016,196.6456451416016,196.6456451416016,197.0479888916016,197.0479888916016,197.3631744384766,197.3631744384766,197.3631744384766,197.3631744384766,197.3631744384766,197.3631744384766,194.435661315918,194.435661315918,194.435661315918,194.6871109008789,194.6871109008789,194.9648742675781,194.9648742675781,195.2772903442383,195.6195983886719,195.6195983886719,195.9779205322266,195.9779205322266,196.3506317138672,196.3506317138672,196.7868804931641,196.7868804931641,197.1921920776367,197.1921920776367,197.4513702392578,197.4513702392578,197.4513702392578,197.4513702392578,194.6036834716797,194.8561935424805,195.1377944946289,195.1377944946289,195.4533386230469,195.7976303100586,196.1572952270508,196.1572952270508,196.5354995727539,196.9322509765625,196.9322509765625,197.3377075195312,197.3377075195312,197.5380020141602,197.5380020141602,197.5380020141602,197.5380020141602,194.7693710327148,194.7693710327148,195.0250930786133,195.3114929199219,195.6318817138672,195.6318817138672,195.9806671142578,195.9806671142578,196.3428497314453,196.7236709594727,196.7236709594727,196.7236709594727,197.1272430419922,197.1272430419922,197.5331726074219,197.6233749389648,197.6233749389648,194.7340774536133,194.9685134887695,195.2292175292969,195.2292175292969,195.5275421142578,195.5275421142578,195.5275421142578,195.8602294921875,195.8602294921875,196.2145004272461,196.2145004272461,196.5824890136719,196.5824890136719,197.01416015625,197.01416015625,197.4180908203125,197.4180908203125,197.7073287963867,197.7073287963867,197.7073287963867,197.7073287963867,197.7073287963867,197.7073287963867,194.9835205078125,194.9835205078125,195.2309265136719,195.2309265136719,195.5080718994141,195.8193435668945,195.8193435668945,196.1613693237305,196.5167846679688,196.8956680297852,196.8956680297852,197.2957534790039,197.6990127563477,197.6990127563477,197.789909362793,197.789909362793,197.789909362793,194.9943771362305,194.9943771362305,195.2261734008789,195.2261734008789,195.4842910766602,195.4842910766602,195.778564453125,195.778564453125,196.1054611206055,196.1054611206055,196.4569549560547,196.4569549560547,196.8205718994141,196.8205718994141,197.2111511230469,197.2111511230469,197.6138534545898,197.8711395263672,197.8711395263672,197.8711395263672,197.8711395263672,197.8711395263672,197.8711395263672,197.8711395263672,197.8711395263672,195.2494812011719,195.2494812011719,195.4975357055664,195.4975357055664,195.7773132324219,195.7773132324219,196.0889053344727,196.0889053344727,196.4311370849609,196.7860565185547,197.1966934204102,197.1966934204102,197.5955963134766,197.9510650634766,197.9510650634766,197.9510650634766,197.9510650634766,197.9510650634766,197.9510650634766,197.9510650634766,197.9510650634766,195.3161468505859,195.3161468505859,195.55615234375,195.55615234375,195.8229446411133,196.1266937255859,196.4625244140625,196.4625244140625,196.8146667480469,196.8146667480469,197.1810607910156,197.1810607910156,197.566650390625,197.566650390625,197.9698486328125,197.9698486328125,198.0297012329102,198.0297012329102,198.0297012329102,198.0297012329102,195.3772583007812,195.3772583007812,195.3772583007812,195.6064300537109,195.6064300537109,195.6064300537109,195.8631820678711,195.8631820678711,196.1538925170898,196.1538925170898,196.4753952026367,196.4753952026367,196.8202438354492,197.1753540039062,197.1753540039062,197.5561904907227,197.9539642333984,197.9539642333984,198.1071166992188,198.1071166992188,195.4448394775391,195.6708908081055,195.6708908081055,195.9237899780273,196.2106552124023,196.2106552124023,196.2106552124023,196.5317611694336,196.5317611694336,196.8776702880859,197.2362747192383,197.659912109375,197.659912109375,198.0601501464844,198.0601501464844,198.1831665039062,198.1831665039062,198.1831665039062,198.1831665039062,195.5778198242188,195.5778198242188,195.8054428100586,195.8054428100586,196.0576400756836,196.3448486328125,196.3448486328125,196.6639099121094,197.0074691772461,197.0074691772461,197.3592910766602,197.3592910766602,197.3592910766602,197.7267379760742,197.7267379760742,198.1176986694336,198.1176986694336,198.1176986694336,198.2581100463867,198.2581100463867,195.6865310668945,195.6865310668945,195.9121627807617,195.9121627807617,196.1588821411133,196.1588821411133,196.4440307617188,196.4440307617188,196.7620620727539,196.7620620727539,197.1046981811523,197.1046981811523,197.4550170898438,197.8308715820312,197.8308715820312,198.2277450561523,198.2277450561523,198.3318176269531,198.3318176269531,198.3318176269531,195.8213577270508,195.8213577270508,196.0494766235352,196.3038101196289,196.5933151245117,196.5933151245117,196.9148178100586,197.2602615356445,197.2602615356445,197.6200561523438,197.6200561523438,198.0415573120117,198.4042587280273,198.4042587280273,198.4042587280273,198.4042587280273,196.0106887817383,196.0106887817383,196.2458267211914,196.2458267211914,196.5107955932617,196.5107955932617,196.8106231689453,197.1419906616211,197.1419906616211,197.1419906616211,197.4922561645508,197.4922561645508,197.8603668212891,197.8603668212891,198.2525100708008,198.4756240844727,198.4756240844727,198.4756240844727,198.4756240844727,198.4756240844727,198.4756240844727,198.4756240844727,198.4756240844727,196.2009811401367,196.4438552856445,196.4438552856445,196.7207565307617,196.7207565307617,197.0329360961914,197.0329360961914,197.0329360961914,197.3737564086914,197.7306671142578,197.7306671142578,198.1102905273438,198.5080337524414,198.545768737793,198.545768737793,196.1864700317383,196.1864700317383,196.4141006469727,196.4141006469727,196.4141006469727,196.6696243286133,196.6696243286133,196.9608535766602,196.9608535766602,197.2861785888672,197.2861785888672,197.6350936889648,197.9849624633789,197.9849624633789,198.362922668457,198.362922668457,198.6148834228516,198.6148834228516,198.6148834228516,198.6148834228516,198.6148834228516,198.6148834228516,198.6148834228516,198.6148834228516,198.6148834228516,198.6148834228516,198.6148834228516,198.6148834228516,198.6148834228516,198.6148834228516,198.6148834228516,198.6148834228516,198.6148834228516,198.6148834228516,198.6148834228516,198.6148834228516,196.2970352172852,196.2970352172852,196.4794921875,196.4794921875,196.6953125,196.6953125,196.933479309082,196.933479309082,197.1962966918945,197.4976043701172,197.4976043701172,197.8250961303711,198.1688003540039,198.1688003540039,198.5303573608398,198.6826400756836,198.6826400756836,198.6826400756836,198.6826400756836,198.6826400756836,198.6826400756836,196.5408782958984,196.5408782958984,196.7829284667969,197.0781860351562,197.0781860351562,197.3867416381836,197.7285537719727,197.7285537719727,198.0819091796875,198.0819091796875,198.4593048095703,198.7496109008789,198.7496109008789,198.7496109008789,198.7496109008789,198.7496109008789,198.7496109008789,196.5854721069336,196.8209075927734,196.8209075927734,197.089973449707,197.3958206176758,197.734245300293,197.734245300293,198.0882034301758,198.0882034301758,198.4647903442383,198.4647903442383,198.4647903442383,198.8153686523438,198.8153686523438,198.8153686523438,198.8153686523438,198.8153686523438,198.8153686523438,196.6510162353516,196.6510162353516,196.8857879638672,196.8857879638672,197.1481475830078,197.1481475830078,197.1481475830078,197.4420471191406,197.4420471191406,197.7697143554688,197.7697143554688,198.1206512451172,198.1206512451172,198.4815216064453,198.8696136474609,198.8696136474609,198.8800964355469,198.8800964355469,198.8800964355469,196.716911315918,196.716911315918,196.9711303710938,196.9711303710938,197.2322845458984,197.2322845458984,197.5326843261719,197.5326843261719,197.8634262084961,197.8634262084961,198.2149276733398,198.2149276733398,198.5776290893555,198.5776290893555,198.9438323974609,198.9438323974609,198.9438323974609,198.9438323974609,196.8320236206055,196.8320236206055,197.0606689453125,197.0606689453125,197.317626953125,197.317626953125,197.6139678955078,197.6139678955078,197.6139678955078,197.9419784545898,197.9419784545898,198.2904052734375,198.2904052734375,198.6487655639648,198.6487655639648,198.6487655639648,199.0064163208008,199.0064163208008,199.0064163208008,199.0064163208008,196.9231109619141,196.9231109619141,197.1333160400391,197.3940887451172,197.3940887451172,197.6918869018555,197.6918869018555,197.6918869018555,198.0211181640625,198.3713226318359,198.3713226318359,198.7337265014648,199.0681381225586,199.0681381225586,199.0681381225586,199.0681381225586,199.0681381225586,199.0681381225586,197.0384521484375,197.0384521484375,197.3021621704102,197.5783615112305,197.5783615112305,197.8935775756836,197.8935775756836,198.2381973266602,198.2381973266602,198.5952453613281,198.9776840209961,199.1287536621094,199.1287536621094,199.1287536621094,199.1287536621094,199.1287536621094,199.1287536621094,197.2409515380859,197.4867401123047,197.4867401123047,197.7712097167969,197.7712097167969,198.0931854248047,198.0931854248047,198.4448776245117,198.4448776245117,198.8116302490234,198.8116302490234,199.1884460449219,199.1884460449219,199.1884460449219,199.1884460449219,197.2044067382812,197.2044067382812,197.4351577758789,197.4351577758789,197.6951599121094,197.6951599121094,197.9942169189453,197.9942169189453,198.3262481689453,198.6797561645508,198.6797561645508,199.0475769042969,199.0475769042969,199.2471160888672,199.2471160888672,199.2471160888672,199.2471160888672,199.2471160888672,199.2471160888672,197.3702697753906,197.6073989868164,197.9159469604492,197.9159469604492,198.2367172241211,198.2367172241211,198.5859603881836,198.5859603881836,198.9510650634766,199.3049011230469,199.3049011230469,199.3049011230469,199.3049011230469,197.3851318359375,197.5903854370117,197.5903854370117,197.8500900268555,197.8500900268555,198.150032043457,198.4840698242188,198.4840698242188,198.8408508300781,198.8408508300781,198.8408508300781,199.2152252197266,199.3617706298828,199.3617706298828,199.3617706298828,199.3617706298828,197.5964508056641,197.5964508056641,197.5964508056641,197.8381271362305,198.115852355957,198.115852355957,198.4292755126953,198.4292755126953,198.7705383300781,198.7705383300781,199.1266174316406,199.1266174316406,199.1266174316406,199.4176940917969,199.4176940917969,199.4176940917969,199.4176940917969,197.5916519165039,197.5916519165039,197.8211898803711,197.8211898803711,198.0831832885742,198.0831832885742,198.4165954589844,198.4165954589844,198.7537231445312,199.1081161499023,199.1081161499023,199.4727554321289,199.4727554321289,199.4727554321289,199.4727554321289,197.6357116699219,197.6357116699219,197.8636322021484,197.8636322021484,198.121955871582,198.121955871582,198.4198913574219,198.4198913574219,198.4198913574219,198.7507553100586,199.1052093505859,199.4682693481445,199.5269012451172,199.5269012451172,199.5269012451172,199.5269012451172,199.5269012451172,199.5269012451172,199.5269012451172,199.5269012451172,199.5269012451172,199.5269012451172,197.6640243530273,197.6640243530273,197.7604141235352,197.7604141235352,197.7604141235352,197.9759292602539,197.9759292602539,198.213134765625,198.213134765625,198.4850006103516,198.7904586791992,198.7904586791992,198.7904586791992,199.1254196166992,199.4692001342773,199.4692001342773,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,199.5797653198242,197.7473220825195,197.7473220825195,197.7473220825195,197.7473220825195,197.7473220825195,197.7473220825195,197.7473220825195,197.7473220825195,197.843635559082,197.843635559082,198.0958404541016,198.0958404541016,198.3788223266602,198.3788223266602,198.6968536376953,198.6968536376953,199.0226821899414,199.0226821899414,199.3332748413086,199.3332748413086,199.6499710083008,199.6499710083008,199.9925079345703,199.9925079345703,200.3685684204102,200.3685684204102,200.3685684204102,200.7723693847656,200.7723693847656,201.1204833984375,201.1204833984375,201.1204833984375,201.4556884765625,201.8227691650391,201.8227691650391,202.1562957763672,202.1562957763672,202.4889144897461,202.8227996826172,202.8227996826172,203.1572113037109,203.1572113037109,203.4913787841797,203.4913787841797,203.8258209228516,203.8258209228516,204.1606063842773,204.1606063842773,204.4943389892578,204.8294982910156,204.8294982910156,205.1653594970703,205.3934936523438,205.3934936523438,205.3934936523438,205.3934936523438,205.3934936523438,205.3934936523438,198.1253051757812,198.1253051757812,198.3847045898438,198.6755752563477,198.6755752563477,199.002311706543,199.002311706543,199.3413543701172,199.3413543701172,199.6598205566406,200.0336074829102,200.0336074829102,200.4230346679688,200.4230346679688,200.8232955932617,201.2280807495117,201.2280807495117,201.2280807495117,201.6340026855469,202.0343627929688,202.4342727661133,202.8357620239258,202.8357620239258,203.2378463745117,203.6391372680664,203.6391372680664,204.0393753051758,204.0393753051758,204.4764633178711,204.4764633178711,204.8737411499023,204.8737411499023,205.2598571777344,205.6026153564453,205.6026153564453,205.6026153564453,205.6026153564453,205.6026153564453,205.6026153564453,198.6191864013672,198.8866424560547,198.8866424560547,198.8866424560547,199.1882553100586,199.5137786865234,199.5137786865234,199.8257751464844,199.8257751464844,200.182746887207,200.560546875,200.9579696655273,200.9579696655273,201.3550338745117,201.3550338745117,201.7560729980469,202.155647277832,202.5561218261719,202.9568481445312,202.9568481445312,203.3567123413086,203.3567123413086,203.3567123413086,203.7555999755859,203.7555999755859,204.1533813476562,204.1533813476562,204.1533813476562,204.5483779907227,204.5483779907227,204.9449234008789,205.3400497436523,205.7253952026367,205.8083343505859,205.8083343505859,205.8083343505859,205.8083343505859,198.8516082763672,198.8516082763672,198.8516082763672,199.1079483032227,199.1079483032227,199.3938140869141,199.3938140869141,199.7315902709961,199.7315902709961,200.0334243774414,200.0334243774414,200.3851318359375,200.7518081665039,201.1371994018555,201.1371994018555,201.529899597168,201.529899597168,201.9299926757812,201.9299926757812,201.9299926757812,202.3293380737305,202.3293380737305,202.7286071777344,202.7286071777344,203.125358581543,203.125358581543,203.5226440429688,203.9217834472656,203.9217834472656,204.3201675415039,204.3201675415039,204.7184753417969,204.7184753417969,204.7184753417969,205.120475769043,205.120475769043,205.518684387207,205.518684387207,205.9026184082031,205.9026184082031,206.0108413696289,206.0108413696289,206.0108413696289,206.0108413696289,206.0108413696289,206.0108413696289,199.1397857666016,199.3924255371094,199.3924255371094,199.6679000854492,199.9648361206055,199.9648361206055,199.9648361206055,200.2657470703125,200.2657470703125,200.6159973144531,200.6159973144531,200.9836349487305,200.9836349487305,201.3646469116211,201.3646469116211,201.76220703125,201.76220703125,202.1588516235352,202.1588516235352,202.5576782226562,202.5576782226562,202.9568481445312,203.3578796386719,203.7512969970703,204.1494522094727,204.1494522094727,204.5491180419922,204.5491180419922,204.9510269165039,205.3533401489258,205.3533401489258,205.750846862793,206.1362991333008,206.1362991333008,206.2099990844727,206.2099990844727,206.2099990844727,206.2099990844727,206.2099990844727,206.2099990844727,199.4795532226562,199.4795532226562,199.7311859130859,200.0038757324219,200.0038757324219,200.2913055419922,200.6047744750977,200.9572525024414,200.9572525024414,201.3253860473633,201.7044830322266,202.0978546142578,202.0978546142578,202.0978546142578,202.4917907714844,202.4917907714844,202.8908233642578,202.8908233642578,203.28955078125,203.28955078125,203.6869583129883,203.6869583129883,204.0824813842773,204.0824813842773,204.4830932617188,204.4830932617188,204.8828811645508,205.2844772338867,205.2844772338867,205.6870193481445,205.6870193481445,206.0809860229492,206.0809860229492,206.4059448242188,206.4059448242188,206.4059448242188,206.4059448242188,206.4059448242188,206.4059448242188,206.4059448242188,206.4059448242188,206.4059448242188,199.8494415283203,200.1028671264648,200.1028671264648,200.3720092773438,200.6494369506836,200.6494369506836,200.9816741943359,200.9816741943359,201.3350372314453,201.3350372314453,201.7024993896484,201.7024993896484,202.0820388793945,202.0820388793945,202.5138702392578,202.5138702392578,202.9043045043945,202.9043045043945,203.3024826049805,203.3024826049805,203.3024826049805,203.7010040283203,203.7010040283203,203.7010040283203,204.0998229980469,204.5004806518555,204.5004806518555,204.9017486572266,204.9017486572266,205.3042907714844,205.7079620361328,206.1100921630859,206.1100921630859,206.4980545043945,206.5987777709961,206.5987777709961,206.5987777709961,206.5987777709961,206.5987777709961,206.5987777709961,206.5987777709961,206.5987777709961,206.5987777709961,206.5987777709961,206.5987777709961,206.5987777709961,206.5987777709961,206.5987777709961,199.9647369384766,199.9647369384766,199.9647369384766,199.9647369384766,200.0414199829102,200.0414199829102,200.2812957763672,200.2812957763672,200.53173828125,200.53173828125,200.53173828125,200.790901184082,200.790901184082,200.790901184082,201.0858535766602,201.0858535766602,201.4152221679688,201.4152221679688,201.7460632324219,202.0992431640625,202.0992431640625,202.4872512817383,202.4872512817383,202.8838500976562,203.279655456543,203.279655456543,203.674674987793,203.674674987793,204.1105346679688,204.1105346679688,204.5087051391602,204.5087051391602,204.9079284667969,204.9079284667969,204.9079284667969,205.3074798583984,205.3074798583984,205.7088317871094,205.7088317871094,206.1109619140625,206.5149078369141,206.5149078369141,206.7883224487305,206.7883224487305,206.7883224487305,206.7883224487305,206.7883224487305,206.7883224487305,206.7883224487305,206.7883224487305,206.7883224487305,206.7883224487305,206.7883224487305,206.7883224487305,200.4856262207031,200.7395172119141,200.7395172119141,201.0060501098633,201.0060501098633,201.0060501098633,201.3087158203125,201.3087158203125,201.6465759277344,201.9927444458008,201.9927444458008,201.9927444458008,202.3441696166992,202.709716796875,202.709716796875,203.0894775390625,203.0894775390625,203.0894775390625,203.4767379760742,203.4767379760742,203.8647689819336,203.8647689819336,204.2605743408203,204.2605743408203,204.6560974121094,204.6560974121094,205.0521469116211,205.0521469116211,205.4507217407227,205.8518600463867,206.252082824707,206.252082824707,206.252082824707,206.6535491943359,206.6535491943359,206.9750289916992,206.9750289916992,206.9750289916992,206.9750289916992,206.9750289916992,206.9750289916992,206.9750289916992,206.9750289916992,206.9750289916992,200.7345504760742,200.7345504760742,200.9786605834961,200.9786605834961,201.2552032470703,201.2552032470703,201.5491714477539,201.5491714477539,201.8762130737305,201.8762130737305,202.2193222045898,202.5717849731445,202.9373016357422,202.9373016357422,203.3186492919922,203.3186492919922,203.3186492919922,203.7016906738281,203.7016906738281,204.0870895385742,204.4824371337891,212.2497711181641,212.2497711181641,212.2497711181641,212.2497711181641,212.2497711181641,212.2497711181641,212.2497711181641,212.2497711181641,212.2497711181641,212.2497711181641,212.2497711181641,212.2497711181641,212.2497711181641,212.2497711181641,212.2497711181641,212.2497711181641,212.2497711181641,212.2497711181641,219.8791656494141,219.8791732788086,219.8791732788086,219.8791732788086,219.8791732788086,219.8791732788086,219.8791732788086,219.8791732788086,219.8791732788086,219.8791732788086,219.8791732788086,219.8791732788086,219.8791732788086,219.8791732788086,219.8791732788086,219.8791732788086,219.8791732788086,219.8791732788086,219.8791732788086,219.8791732788086,219.8791732788086,219.8791732788086,219.8791732788086,235.1379623413086,235.1379623413086,235.1379623413086,235.1379623413086,235.1379623413086,235.1379623413086,235.1379623413086,235.1379623413086,235.1379623413086,235.1379623413086,235.1379623413086,235.1379623413086,235.1379623413086,235.1379623413086,235.1379623413086,235.1379623413086,242.7673797607422,242.7673797607422,242.7673797607422,242.7673797607422,242.7673797607422,242.7673797607422,242.7673797607422,242.7673797607422,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664,258.1625747680664],"meminc":[0,0,0,0,15.28223419189453,0,0,0,-15.28857421875,0,0,45.75431823730469,0,0,0,0,0,4.57763671875e-05,0,0,0,0,0,0,0,0,0,0,0,0,0,-0.00030517578125,0,15.38435363769531,0,0.2509994506835938,0.2701187133789062,0,0.31011962890625,0.3365631103515625,0.353057861328125,0.372711181640625,0.40863037109375,0,0.4130783081054688,0,0.4156951904296875,0,0,-2.999588012695312,0.376678466796875,0,0.415374755859375,0,0.4255218505859375,0,0.4106216430664062,0,0,0.4073257446289062,0.4058303833007812,0,0.4071197509765625,0,0,0.2207489013671875,0,0,0,-2.792991638183594,0,0.3662338256835938,0,0.3911056518554688,0,0.4173202514648438,0,0.409759521484375,0,0.4035720825195312,0,0.4034576416015625,0.4065628051757812,0,-2.910934448242188,0.3625259399414062,0,0.371490478515625,0.3993148803710938,0,0.4151763916015625,0.4085769653320312,0.4045944213867188,0,0.4092636108398438,0.3075790405273438,0,0,-2.788032531738281,0.3465042114257812,0.3686065673828125,0.3953628540039062,0,0.404876708984375,0,0.4012451171875,0,0.4023666381835938,0,0.4021453857421875,0.1511917114257812,0,0,-2.619033813476562,0,0.3551712036132812,0,0,0.3763809204101562,0,0.39984130859375,0.406646728515625,0,0.4050064086914062,0,0,0.4063339233398438,0.35247802734375,0,-2.755653381347656,0,0,0.37152099609375,0.3597259521484375,0.3696975708007812,0,0.3968887329101562,0.405242919921875,0.4039154052734375,0,0.4086456298828125,0,0.1216049194335938,0,-2.52569580078125,0.3478317260742188,0,0.3653030395507812,0.389923095703125,0,0.4029998779296875,0.405242919921875,0,0.4074783325195312,0,0.2870559692382812,0,0,-2.623512268066406,0,0,0.3437576293945312,0,0.362335205078125,0,0.3776397705078125,0,0.3946304321289062,0,0.4043655395507812,0,0.4096832275390625,0,0.4100875854492188,0,0,-2.676712036132812,0.3302001953125,0,0,0.3569183349609375,0,0,0.3653411865234375,0,0.38409423828125,0,0.398345947265625,0,0.4079818725585938,0,0.4117813110351562,0.099609375,0,-2.397605895996094,0.3426513671875,0,0.3573226928710938,0.37481689453125,0,0.3956985473632812,0.403350830078125,0,0.4111404418945312,0.189056396484375,0,-2.431838989257812,0,0.34197998046875,0,0.38623046875,0,0.369720458984375,0.3926849365234375,0.3976593017578125,0.4074783325195312,0,0.2112655639648438,0,0,-2.406364440917969,0,0.3321304321289062,0,0.3470993041992188,0,0.364349365234375,0.3860549926757812,0.3979721069335938,0.4051742553710938,0.2474441528320312,0,-2.392601013183594,0.3278579711914062,0.3453369140625,0,0.3629913330078125,0,0.3851699829101562,0,0.397125244140625,0,0,0.4049224853515625,0.242034912109375,0,-2.360244750976562,0,0.3187103271484375,0.33984375,0,0.3546524047851562,0,0.3770675659179688,0,0.3817291259765625,0.3947525024414062,0,0.2649917602539062,0,0,-2.341011047363281,0,0.314483642578125,0,0.3328628540039062,0,0.3516998291015625,0.3770370483398438,0,0.39117431640625,0,0.3995208740234375,0,0.2446670532226562,0,-2.291725158691406,0,0.3118057250976562,0,0.3636016845703125,0,0.3541107177734375,0,0.3809661865234375,0,0,0.392364501953125,0,0,0.399261474609375,0.1589202880859375,0,0,-2.194496154785156,0,0.310546875,0.3314132690429688,0.3544464111328125,0,0.37493896484375,0.3908462524414062,0,0.3995132446289062,0,0.1008987426757812,0,0,-2.114158630371094,0,0.3048019409179688,0,0.3302841186523438,0,0.3547744750976562,0,0.3721694946289062,0,0.3904342651367188,0,0.3987503051757812,0.0299835205078125,0,0,-2.027664184570312,0,0,0.3119888305664062,0,0,0.3389968872070312,0,0.35888671875,0,0.3822402954101562,0.3931655883789062,0,0.3083572387695312,0,0,-2.19476318359375,0.2896881103515625,0.3153305053710938,0.3442153930664062,0.362030029296875,0,0,0.3832778930664062,0,0.3913803100585938,0.1737823486328125,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2.147232055664062,0,0,0.2200698852539062,0,0.234375,0,0.261810302734375,0.2956771850585938,0,0.322723388671875,0,0,0.3333816528320312,0.352569580078125,0,0.1901931762695312,0,0,-2.055747985839844,0,0.2871017456054688,0,0.3225173950195312,0,0.3469161987304688,0,0.3629379272460938,0.3935394287109375,0,0.40533447265625,0,-2.158462524414062,0,0.2830657958984375,0,0.3039016723632812,0,0.3402633666992188,0,0.3539810180664062,0,0.3691558837890625,0,0.3848037719726562,0.1854476928710938,0,-1.958763122558594,0,0.2859954833984375,0.3216476440429688,0,0.3500747680664062,0,0.3632354736328125,0.3885269165039062,0,0,0.3100814819335938,0,0,-2.0401611328125,0,0.2765350341796875,0,0.3072128295898438,0,0.3444595336914062,0,0.35821533203125,0,0.3786087036132812,0,0.4001235961914062,0,0.034912109375,0,0,-1.81439208984375,0.2960281372070312,0.3309173583984375,0,0.3544235229492188,0,0.3697586059570312,0,0,0.3959197998046875,0.1262664794921875,0,-1.846977233886719,0,0.283935546875,0,0.3208084106445312,0.3496551513671875,0,0.3637619018554688,0,0.3882064819335938,0,0.1984710693359375,0,0,-1.864189147949219,0,0.2808456420898438,0.3198089599609375,0,0.3493499755859375,0,0.3677749633789062,0.3894500732421875,0.2140274047851562,0,0,-1.814353942871094,0.2752304077148438,0,0.3138885498046875,0,0.34136962890625,0.355865478515625,0.3823089599609375,0,0.2017822265625,0,-1.811546325683594,0,0,0.2788238525390625,0,0.3167343139648438,0,0.3446197509765625,0.3611907958984375,0,0.364776611328125,0,0.2005615234375,0,0,-1.794929504394531,0,0.2719879150390625,0,0.3098983764648438,0,0.3463668823242188,0,0.3587646484375,0.387359619140625,0,0.1748275756835938,0,0,-1.728645324707031,0,0.2757186889648438,0.3178939819335938,0,0.349395751953125,0,0.3617019653320312,0.3900833129882812,0.0873260498046875,0,0,-1.645790100097656,0.2866592407226562,0.3272781372070312,0,0.3423690795898438,0,0.3618698120117188,0.3800811767578125,0,-1.797119140625,0,0.2616348266601562,0,0.2952117919921875,0.3372116088867188,0,0.3574371337890625,0,0.3721694946289062,0,0.2251968383789062,0,0,-1.686271667480469,0.2701568603515625,0,0.3139266967773438,0,0.3458633422851562,0,0.3613433837890625,0,0,0.387939453125,0,0.05792236328125,0,0,-1.539779663085938,0,0.2852935791015625,0,0.3288497924804688,0,0.3544845581054688,0,0.369720458984375,0,0,0.2514419555664062,0,0,-1.647666931152344,0,0.2658462524414062,0,0.3066177368164062,0,0.3410110473632812,0.3607254028320312,0,0.38043212890625,0.04224395751953125,0,0,-1.486610412597656,0,0.2877578735351562,0.329559326171875,0,0.3560256958007812,0,0.3734130859375,0,0.1883010864257812,0,0,-1.527450561523438,0,0.2798919677734375,0,0.3224716186523438,0,0.3508224487304688,0,0.3677978515625,0,0.2540740966796875,0,0,-1.570365905761719,0,0.2663497924804688,0,0.3082046508789062,0.3436965942382812,0,0.3656997680664062,0,0,0.3333358764648438,0,-1.598381042480469,0,0.2594985961914062,0,0.2974166870117188,0,0.3345260620117188,0,0.3591461181640625,0,0.377471923828125,0,0,0.01645660400390625,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.588294982910156,0,0,0,0,0,0.20074462890625,0,0.2498779296875,0,0.2750396728515625,0.3044509887695312,0,0.3152847290039062,0,0,0.3255538940429688,0.3727188110351562,0.4024200439453125,0.3957443237304688,0,0.3369827270507812,0.3342361450195312,0,0,0.3686904907226562,0,0.335723876953125,0.336334228515625,0,0,0.285491943359375,0,0,0,0,0,-4.346588134765625,0,0.3433380126953125,0,0.3578643798828125,0.3414764404296875,0.3899307250976562,0.4225234985351562,0.4114227294921875,0,0.4093856811523438,0,0.4074554443359375,0.4054107666015625,0,0.4054794311523438,0,0.3988571166992188,0,0.1858291625976562,0,0,-4.481277465820312,0,0.3082962036132812,0.3427200317382812,0,0.342529296875,0,0.341461181640625,0.4044189453125,0.420562744140625,0.4100418090820312,0,0.4090728759765625,0,0.4071731567382812,0.4073486328125,0,0.4074325561523438,0.3941192626953125,0,0.01633453369140625,0,0,-4.298255920410156,0,0.3102493286132812,0,0.332672119140625,0.3209457397460938,0,0.3767471313476562,0,0.4058761596679688,0,0.4565887451171875,0,0.4059219360351562,0,0.4051284790039062,0.4026107788085938,0.4051742553710938,0.4002609252929688,0.2042007446289062,0,0,-4.363807678222656,0,0.2905349731445312,0,0.3192138671875,0,0,0.31695556640625,0.3531951904296875,0,0,0.3832778930664062,0.412017822265625,0.4074249267578125,0,0,0.4051361083984375,0.402191162109375,0,0.40496826171875,0.4061203002929688,0,0,0.3888320922851562,0,0,0,0,0,-4.144050598144531,0,0.3028945922851562,0,0.3089752197265625,0,0.3301315307617188,0,0.3719711303710938,0,0.39569091796875,0,0.4023513793945312,0,0.3973464965820312,0,0.4007415771484375,0,0,0.4013137817382812,0,0.40374755859375,0,0.3964309692382812,0,0,0.156494140625,0,-4.200225830078125,0,0.2902603149414062,0,0.3056564331054688,0,0.3500442504882812,0.3613357543945312,0,0.3845367431640625,0.4084548950195312,0,0.4020538330078125,0,0.3993301391601562,0,0.4001007080078125,0,0.401519775390625,0,0.3975830078125,0,0.2213211059570312,0,0,-4.187652587890625,0.2782058715820312,0.2956008911132812,0,0.3034210205078125,0,0.3496017456054688,0.3679656982421875,0.3891372680664062,0.4003067016601562,0,0.4005661010742188,0,0.4034347534179688,0,0.4034042358398438,0,0.4044723510742188,0.3116607666015625,0,0,0,0,0,-3.906875610351562,0,0.2883682250976562,0.3051376342773438,0,0.34796142578125,0,0.37091064453125,0.3917312622070312,0,0.4086151123046875,0,0.402740478515625,0,0.403350830078125,0.401580810546875,0,0.4016647338867188,0,0.3028717041015625,0,0,0,0,0,-3.819557189941406,0.2841949462890625,0,0.3114700317382812,0,0.3501434326171875,0.3701858520507812,0.3881759643554688,0,0,0.4088516235351562,0,0.403228759765625,0,0.4029083251953125,0,0.4023513793945312,0.3956985473632812,0,0.2185592651367188,0,0,0,-3.734451293945312,0,0.2772293090820312,0,0.316680908203125,0.3461151123046875,0,0.3652114868164062,0,0.3885040283203125,0.4018325805664062,0,0.3979339599609375,0,0.3985595703125,0.393890380859375,0,0.3932952880859375,0,0.1695098876953125,0,-3.901412963867188,0,0.2621917724609375,0,0,0.2716293334960938,0,0.3156585693359375,0.340972900390625,0,0,0.3586502075195312,0,0.3858718872070312,0,0.40325927734375,0,0.358551025390625,0.3975753784179688,0,0.3992156982421875,0,0.4327774047851562,0.08754730224609375,0,0,-3.785133361816406,0.2607269287109375,0,0.2858352661132812,0,0.3245849609375,0.3476181030273438,0,0.3634262084960938,0,0.3948287963867188,0,0.4043655395507812,0.4022903442382812,0,0.4016494750976562,0,0.399383544921875,0,0.3111343383789062,0,0,0,0,0,-3.609367370605469,0,0.26556396484375,0,0.310699462890625,0,0.3345260620117188,0,0.3529891967773438,0,0.3757095336914062,0,0.40423583984375,0.40032958984375,0,0,0.4000701904296875,0,0.4027099609375,0.392425537109375,0,0.07892608642578125,0,0,-3.650985717773438,0,0.2556533813476562,0,0.293243408203125,0,0.3247833251953125,0,0.3802947998046875,0,0.3717117309570312,0.3957366943359375,0.4027633666992188,0,0.4015350341796875,0,0.4030838012695312,0,0.3952865600585938,0,0.1340789794921875,0,0,-3.64068603515625,0,0.2507095336914062,0,0.2816925048828125,0.3142242431640625,0,0.3349838256835938,0,0.360107421875,0,0.384246826171875,0,0.4046630859375,0,0.399017333984375,0,0.4016799926757812,0,0.3982086181640625,0.21649169921875,0,0,0,0,0,-3.389328002929688,0,0.2669601440429688,0.303466796875,0,0.3291778564453125,0.3561172485351562,0.3810806274414062,0,0,0.39605712890625,0,0.402862548828125,0,0.4060897827148438,0,0,0.404083251953125,0,0.24713134765625,0,0,-3.566535949707031,0.2521820068359375,0,0.2737197875976562,0.3017120361328125,0.3272476196289062,0,0.3519668579101562,0,0.3741683959960938,0.3982620239257812,0.399688720703125,0.4039993286132812,0,0.3974456787109375,0,0.1881484985351562,0,0,0,-3.508003234863281,0.2467193603515625,0,0.27557373046875,0.3025131225585938,0,0.3254547119140625,0,0.3544998168945312,0,0.3773956298828125,0,0.4022064208984375,0,0.4009475708007812,0,0.4043655395507812,0.3963546752929688,0,0.122314453125,0,0,-3.400749206542969,0.2453384399414062,0,0,0.2748336791992188,0,0.2977371215820312,0,0.3286972045898438,0,0.3539581298828125,0,0.3765182495117188,0,0.4041290283203125,0,0.3953857421875,0,0.3995132446289062,0,0.4234161376953125,0,0,0,0,0,-3.272499084472656,0,0.2518081665039062,0,0.2788314819335938,0,0.3053741455078125,0.3377914428710938,0,0.3636932373046875,0,0.3911361694335938,0,0.4041900634765625,0.4040908813476562,0,0.4037322998046875,0.2289657592773438,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-3.344192504882812,0,0.0764312744140625,0,0.2002105712890625,0,0.226898193359375,0,0.2377777099609375,0.2691192626953125,0,0.3046340942382812,0,0.3213272094726562,0,0.3365325927734375,0,0,0.367462158203125,0,0,0.3994140625,0,0.4042282104492188,0.2955398559570312,0,0,0,0,0,0,0,-3.108856201171875,0.2587203979492188,0,0.284027099609375,0,0.3132247924804688,0,0.3393936157226562,0,0.3486709594726562,0,0.3640899658203125,0.3835906982421875,0,0.4015274047851562,0,0,0.406494140625,0.1032485961914062,0,0,-3.185234069824219,0,0.24249267578125,0,0.2674636840820312,0,0.297393798828125,0.3197174072265625,0,0.3465652465820312,0.3586883544921875,0,0.384979248046875,0.442901611328125,0,0.4092788696289062,0,0.208282470703125,0,0,0,0,0,-2.958877563476562,0,0,0.2605667114257812,0,0.28765869140625,0,0.3211288452148438,0.348602294921875,0.3637161254882812,0.3782119750976562,0,0.402069091796875,0.4042892456054688,0,0.2837066650390625,0,0,0,0,0,-2.954566955566406,0.2550735473632812,0,0.2844619750976562,0,0.3174819946289062,0,0.3454971313476562,0,0.358978271484375,0,0.370819091796875,0,0,0.3942947387695312,0,0,0.40234375,0,0.315185546875,0,0,0,0,0,-2.927513122558594,0,0,0.2514495849609375,0,0.2777633666992188,0,0.3124160766601562,0.3423080444335938,0,0.3583221435546875,0,0.372711181640625,0,0.436248779296875,0,0.4053115844726562,0,0.2591781616210938,0,0,0,-2.847686767578125,0.2525100708007812,0.2816009521484375,0,0.3155441284179688,0.3442916870117188,0.3596649169921875,0,0.378204345703125,0.3967514038085938,0,0.40545654296875,0,0.2002944946289062,0,0,0,-2.768630981445312,0,0.2557220458984375,0.2863998413085938,0.3203887939453125,0,0.348785400390625,0,0.3621826171875,0.3808212280273438,0,0,0.4035720825195312,0,0.4059295654296875,0.09020233154296875,0,-2.889297485351562,0.23443603515625,0.2607040405273438,0,0.2983245849609375,0,0,0.3326873779296875,0,0.3542709350585938,0,0.3679885864257812,0,0.431671142578125,0,0.4039306640625,0,0.2892379760742188,0,0,0,0,0,-2.723808288574219,0,0.247406005859375,0,0.2771453857421875,0.3112716674804688,0,0.3420257568359375,0.3554153442382812,0.3788833618164062,0,0.40008544921875,0.40325927734375,0,0.0908966064453125,0,0,-2.7955322265625,0,0.2317962646484375,0,0.25811767578125,0,0.2942733764648438,0,0.3268966674804688,0,0.3514938354492188,0,0.363616943359375,0,0.3905792236328125,0,0.4027023315429688,0.2572860717773438,0,0,0,0,0,0,0,-2.621658325195312,0,0.2480545043945312,0,0.2797775268554688,0,0.3115921020507812,0,0.3422317504882812,0.35491943359375,0.4106369018554688,0,0.3989028930664062,0.35546875,0,0,0,0,0,0,0,-2.634918212890625,0,0.2400054931640625,0,0.2667922973632812,0.3037490844726562,0.3358306884765625,0,0.352142333984375,0,0.36639404296875,0,0.385589599609375,0,0.4031982421875,0,0.05985260009765625,0,0,0,-2.652442932128906,0,0,0.2291717529296875,0,0,0.2567520141601562,0,0.29071044921875,0,0.321502685546875,0,0.3448486328125,0.3551101684570312,0,0.3808364868164062,0.3977737426757812,0,0.1531524658203125,0,-2.662277221679688,0.2260513305664062,0,0.252899169921875,0.286865234375,0,0,0.32110595703125,0,0.3459091186523438,0.3586044311523438,0.4236373901367188,0,0.400238037109375,0,0.123016357421875,0,0,0,-2.6053466796875,0,0.2276229858398438,0,0.252197265625,0.2872085571289062,0,0.319061279296875,0.3435592651367188,0,0.3518218994140625,0,0,0.3674468994140625,0,0.390960693359375,0,0,0.140411376953125,0,-2.571578979492188,0,0.2256317138671875,0,0.2467193603515625,0,0.2851486206054688,0,0.3180313110351562,0,0.3426361083984375,0,0.3503189086914062,0.3758544921875,0,0.3968734741210938,0,0.1040725708007812,0,0,-2.510459899902344,0,0.228118896484375,0.25433349609375,0.2895050048828125,0,0.321502685546875,0.3454437255859375,0,0.3597946166992188,0,0.4215011596679688,0.362701416015625,0,0,0,-2.393569946289062,0,0.235137939453125,0,0.2649688720703125,0,0.2998275756835938,0.3313674926757812,0,0,0.3502655029296875,0,0.3681106567382812,0,0.3921432495117188,0.223114013671875,0,0,0,0,0,0,0,-2.274642944335938,0.2428741455078125,0,0.2769012451171875,0,0.3121795654296875,0,0,0.3408203125,0.3569107055664062,0,0.3796234130859375,0.3977432250976562,0.0377349853515625,0,-2.359298706054688,0,0.227630615234375,0,0,0.255523681640625,0,0.291229248046875,0,0.3253250122070312,0,0.3489151000976562,0.3498687744140625,0,0.377960205078125,0,0.2519607543945312,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2.317848205566406,0,0.1824569702148438,0,0.2158203125,0,0.2381668090820312,0,0.2628173828125,0.3013076782226562,0,0.3274917602539062,0.3437042236328125,0,0.3615570068359375,0.15228271484375,0,0,0,0,0,-2.141761779785156,0,0.2420501708984375,0.295257568359375,0,0.3085556030273438,0.3418121337890625,0,0.3533554077148438,0,0.3773956298828125,0.2903060913085938,0,0,0,0,0,-2.164138793945312,0.2354354858398438,0,0.2690658569335938,0.30584716796875,0.3384246826171875,0,0.3539581298828125,0,0.3765869140625,0,0,0.3505783081054688,0,0,0,0,0,-2.164352416992188,0,0.234771728515625,0,0.262359619140625,0,0,0.2938995361328125,0,0.327667236328125,0,0.3509368896484375,0,0.360870361328125,0.388092041015625,0,0.0104827880859375,0,0,-2.163185119628906,0,0.2542190551757812,0,0.2611541748046875,0,0.3003997802734375,0,0.3307418823242188,0,0.35150146484375,0,0.362701416015625,0,0.3662033081054688,0,0,0,-2.111808776855469,0,0.2286453247070312,0,0.2569580078125,0,0.2963409423828125,0,0,0.3280105590820312,0,0.3484268188476562,0,0.3583602905273438,0,0,0.3576507568359375,0,0,0,-2.083305358886719,0,0.210205078125,0.260772705078125,0,0.2977981567382812,0,0,0.3292312622070312,0.3502044677734375,0,0.3624038696289062,0.33441162109375,0,0,0,0,0,-2.029685974121094,0,0.2637100219726562,0.2761993408203125,0,0.315216064453125,0,0.3446197509765625,0,0.3570480346679688,0.3824386596679688,0.1510696411132812,0,0,0,0,0,-1.887802124023438,0.24578857421875,0,0.2844696044921875,0,0.3219757080078125,0,0.3516921997070312,0,0.3667526245117188,0,0.3768157958984375,0,0,0,-1.984039306640625,0,0.2307510375976562,0,0.2600021362304688,0,0.2990570068359375,0,0.33203125,0.3535079956054688,0,0.3678207397460938,0,0.1995391845703125,0,0,0,0,0,-1.876846313476562,0.2371292114257812,0.3085479736328125,0,0.320770263671875,0,0.3492431640625,0,0.3651046752929688,0.3538360595703125,0,0,0,-1.919769287109375,0.2052536010742188,0,0.25970458984375,0,0.2999420166015625,0.3340377807617188,0,0.356781005859375,0,0,0.3743743896484375,0.14654541015625,0,0,0,-1.76531982421875,0,0,0.2416763305664062,0.2777252197265625,0,0.3134231567382812,0,0.3412628173828125,0,0.3560791015625,0,0,0.29107666015625,0,0,0,-1.826042175292969,0,0.2295379638671875,0,0.261993408203125,0,0.3334121704101562,0,0.337127685546875,0.3543930053710938,0,0.3646392822265625,0,0,0,-1.837043762207031,0,0.2279205322265625,0,0.2583236694335938,0,0.2979354858398438,0,0,0.3308639526367188,0.3544540405273438,0.3630599975585938,0.05863189697265625,0,0,0,0,0,0,0,0,0,-1.862876892089844,0,0.0963897705078125,0,0,0.21551513671875,0,0.2372055053710938,0,0.2718658447265625,0.3054580688476562,0,0,0.3349609375,0.343780517578125,0,0.110565185546875,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.832443237304688,0,0,0,0,0,0,0,0.0963134765625,0,0.2522048950195312,0,0.2829818725585938,0,0.3180313110351562,0,0.3258285522460938,0,0.3105926513671875,0,0.3166961669921875,0,0.3425369262695312,0,0.3760604858398438,0,0,0.4038009643554688,0,0.348114013671875,0,0,0.335205078125,0.3670806884765625,0,0.333526611328125,0,0.3326187133789062,0.3338851928710938,0,0.33441162109375,0,0.33416748046875,0,0.334442138671875,0,0.3347854614257812,0,0.3337326049804688,0.3351593017578125,0,0.3358612060546875,0.2281341552734375,0,0,0,0,0,-7.2681884765625,0,0.2593994140625,0.2908706665039062,0,0.3267364501953125,0,0.3390426635742188,0,0.3184661865234375,0.3737869262695312,0,0.3894271850585938,0,0.4002609252929688,0.40478515625,0,0,0.4059219360351562,0.400360107421875,0.3999099731445312,0.4014892578125,0,0.4020843505859375,0.4012908935546875,0,0.400238037109375,0,0.4370880126953125,0,0.39727783203125,0,0.3861160278320312,0.3427581787109375,0,0,0,0,0,-6.983428955078125,0.2674560546875,0,0,0.3016128540039062,0.3255233764648438,0,0.3119964599609375,0,0.3569717407226562,0.3777999877929688,0.3974227905273438,0,0.397064208984375,0,0.4010391235351562,0.3995742797851562,0.4004745483398438,0.400726318359375,0,0.3998641967773438,0,0,0.3988876342773438,0,0.3977813720703125,0,0,0.3949966430664062,0,0.39654541015625,0.3951263427734375,0.385345458984375,0.08293914794921875,0,0,0,-6.95672607421875,0,0,0.2563400268554688,0,0.2858657836914062,0,0.3377761840820312,0,0.3018341064453125,0,0.3517074584960938,0.3666763305664062,0.3853912353515625,0,0.3927001953125,0,0.4000930786132812,0,0,0.3993453979492188,0,0.3992691040039062,0,0.3967514038085938,0,0.3972854614257812,0.399139404296875,0,0.3983840942382812,0,0.3983078002929688,0,0,0.4020004272460938,0,0.3982086181640625,0,0.3839340209960938,0,0.1082229614257812,0,0,0,0,0,-6.871055603027344,0.2526397705078125,0,0.2754745483398438,0.29693603515625,0,0,0.3009109497070312,0,0.350250244140625,0,0.3676376342773438,0,0.381011962890625,0,0.3975601196289062,0,0.3966445922851562,0,0.3988265991210938,0,0.399169921875,0.401031494140625,0.3934173583984375,0.3981552124023438,0,0.3996658325195312,0,0.4019088745117188,0.402313232421875,0,0.3975067138671875,0.3854522705078125,0,0.073699951171875,0,0,0,0,0,-6.730445861816406,0,0.2516326904296875,0.2726898193359375,0,0.2874298095703125,0.3134689331054688,0.35247802734375,0,0.368133544921875,0.3790969848632812,0.39337158203125,0,0,0.3939361572265625,0,0.3990325927734375,0,0.3987274169921875,0,0.3974075317382812,0,0.3955230712890625,0,0.4006118774414062,0,0.3997879028320312,0.4015960693359375,0,0.4025421142578125,0,0.3939666748046875,0,0.3249588012695312,0,0,0,0,0,0,0,0,-6.556503295898438,0.2534255981445312,0,0.2691421508789062,0.2774276733398438,0,0.3322372436523438,0,0.353363037109375,0,0.367462158203125,0,0.3795394897460938,0,0.4318313598632812,0,0.3904342651367188,0,0.3981781005859375,0,0,0.3985214233398438,0,0,0.3988189697265625,0.4006576538085938,0,0.4012680053710938,0,0.4025421142578125,0.4036712646484375,0.402130126953125,0,0.3879623413085938,0.1007232666015625,0,0,0,0,0,0,0,0,0,0,0,0,0,-6.634040832519531,0,0,0,0.07668304443359375,0,0.2398757934570312,0,0.2504425048828125,0,0,0.2591629028320312,0,0,0.294952392578125,0,0.3293685913085938,0,0.330841064453125,0.353179931640625,0,0.3880081176757812,0,0.3965988159179688,0.3958053588867188,0,0.39501953125,0,0.4358596801757812,0,0.3981704711914062,0,0.3992233276367188,0,0,0.3995513916015625,0,0.4013519287109375,0,0.402130126953125,0.4039459228515625,0,0.2734146118164062,0,0,0,0,0,0,0,0,0,0,0,-6.302696228027344,0.2538909912109375,0,0.2665328979492188,0,0,0.3026657104492188,0,0.337860107421875,0.3461685180664062,0,0,0.3514251708984375,0.3655471801757812,0,0.3797607421875,0,0,0.3872604370117188,0,0.388031005859375,0,0.3958053588867188,0,0.3955230712890625,0,0.3960494995117188,0,0.3985748291015625,0.4011383056640625,0.4002227783203125,0,0,0.4014663696289062,0,0.3214797973632812,0,0,0,0,0,0,0,0,-6.240478515625,0,0.244110107421875,0,0.2765426635742188,0,0.2939682006835938,0,0.3270416259765625,0,0.343109130859375,0.3524627685546875,0.3655166625976562,0,0.38134765625,0,0,0.3830413818359375,0,0.3853988647460938,0.3953475952148438,7.767333984375,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7.62939453125,7.62939453125e-06,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,15.2587890625,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7.629417419433594,0,0,0,0,0,0,0,15.39519500732422,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"filename":["<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>","<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,null,null,null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,null,null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,null,"<expr>","<expr>",null,null,null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,null,null,null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,null,null,null,null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>","<expr>",null,null,null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null]},"interval":10,"files":[{"filename":"<expr>","content":"## Generate Large Random Dataset\nn <- 2e6\nx <- runif(n)\ny <- runif(n)\nz <- runif(n)\nXYZ <- cbind(x,y,z)\n\n## Inspect 4 equivalent `row mean` calculations \nprofvis::profvis({\n    m <- rowSums(XYZ)/ncol(XYZ)\n    m <- rowMeans(XYZ)\n    m <- apply(XYZ, 1, mean)\n    m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }\n})\n## rowSums(), colSums(), rowMeans(), and colMeans() are vectorised and fast.\n## for loop is not the slowest, but the ugliest.","normpath":"<expr>"}],"prof_output":"/tmp/RtmpNaQU1E/file251951737e2b.prof","highlight":{"output":["^output\\$"],"gc":["^<GC>$"],"stacktrace":["^\\.\\.stacktraceo(n|ff)\\.\\.$"]},"split":"h"}},"evals":[],"jsHooks":[]}</script>
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
## 1 mean1(x, 0.5)     20ms   21.8ms      46.0    7.63MB     2.09
## 2 mean2(x, 0.5)   19.1ms   20.9ms      48.2    7.63MB     0   
## 3 mean3(x, 0.5)     20ms   21.8ms      46.5    7.63MB     2.11
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
##   0.103   0.000   0.032
```

```r
system.time({ lm(Y~X, data=DAT) })
```

```
##    user  system elapsed 
##   0.404   0.000   0.137
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
## 1 ma1(y)      163.3ms  164.3ms      6.08    15.3MB     2.03
## 2 ma2(y)       21.2ms   21.3ms     47.0     91.6MB   400.
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
##   0.026   0.002   0.028
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
##   0.765   0.225   0.559
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


##  Further Programming Guidance

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





