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
<div class="plotly html-widget html-fill-item" id="htmlwidget-0b421b607f3a46d8eb30" style="width:672px;height:480px;"></div>
<script type="application/json" data-for="htmlwidget-0b421b607f3a46d8eb30">{"x":{"visdat":{"15e37b01545a":["function () ","plotlyVisDat"]},"cur_data":"15e37b01545a","attrs":{"15e37b01545a":{"x":{},"y":{},"alpha_stroke":1,"sizes":[10,100],"spans":[1,20]}},"layout":{"margin":{"b":40,"l":60,"t":25,"r":10},"xaxis":{"domain":[0,1],"automargin":true,"title":"X"},"yaxis":{"domain":[0,1],"automargin":true,"title":"Y"},"hovermode":"closest","showlegend":false},"source":"A","config":{"modeBarButtonsToAdd":["hoverclosest","hovercompare"],"showSendToCloud":false},"data":[{"x":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100],"y":[3.2083574915003994,11.758082254989596,14.924828165559102,14.605756481359833,20.227297866090662,21.274543325472255,29.392217917996316,31.806101582230617,36.103243246322833,38.911421668820047,42.86460342377751,50.443102579247565,48.410425662795319,55.276916522876583,60.639921395227965,65.013906128111117,65.642462008758443,69.528201369053349,80.136784812865713,75.907851937380684,84.718250920122784,84.410150277055394,89.232283469481999,97.422174039581705,99.442164003100913,107.4572485584618,106.01869540150783,112.1472832095013,119.58249711085685,121.1216510842421,119.69780133948771,130.29417273500528,132.13036243104258,133.26390272956814,140.76169242202988,138.02422571578259,147.58528543747724,153.7923945771399,158.20876110705197,157.44169954894306,164.93398252092609,169.64978868106394,167.35173466463064,174.0204799644757,180.53441310883338,182.78566970218824,188.05716154365464,192.95109540762832,193.37996134675768,198.13319686979531,204.64867920435375,207.90759267503591,212.43867781352625,214.99975261489618,222.5009194350132,226.14936360962599,228.96326548304603,228.47814485135012,234.08747246212374,241.43475229864205,245.2887023664583,244.76425922590946,255.61084986834044,253.27306825901533,260.99816227161665,268.6157786733271,266.71504826772656,273.60948844089978,279.10313240010561,279.05590166202796,287.12032467108907,287.96903602622297,290.39101334542499,295.79067891199344,300.39208152833214,301.7336902002163,310.34323710220838,312.93153209510587,315.01497778042926,319.25444799532261,325.74113687699213,324.30040095361073,331.112707439514,335.68569598866355,338.80418114748409,341.39864602038693,346.05210762181503,351.90571136255818,355.67806804025861,359.09542705827874,363.40106580814722,367.38328831404715,372.00523749569544,378.15895995986898,381.82418287359945,384.76192889704782,388.60083395131119,394.51863929180575,394.82725935281485,399.9120118450922],"type":"scatter","mode":"markers","marker":{"color":"rgba(31,119,180,1)","line":{"color":"rgba(31,119,180,1)"}},"error_y":{"color":"rgba(31,119,180,1)"},"error_x":{"color":"rgba(31,119,180,1)"},"line":{"color":"rgba(31,119,180,1)"},"xaxis":"x","yaxis":"y","frame":null}],"highlight":{"on":"plotly_click","persistent":false,"dynamic":false,"selectize":false,"opacityDim":0.20000000000000001,"selected":{"opacity":1},"debounce":0},"shinyEvents":["plotly_hover","plotly_click","plotly_selected","plotly_relayout","plotly_brushed","plotly_brushing","plotly_clickannotation","plotly_doubleclick","plotly_deselect","plotly_afterplot","plotly_sunburstclick"],"base_url":"https://plot.ly"},"evals":[],"jsHooks":[]}</script>
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
## Caught a warning!
```

```
## <simpleWarning in log(x): NaNs produced>
```

```
## Returned log(x) if successfull or NA if Error or Warning
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
    ```
    
    ```
    ## Warning in doTryCatch(return(expr), name, parentenv, handler): warning
    ```
    
    ```r
    try(error('error'), silent=T)
    
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
<div class="profvis html-widget html-fill-item" id="htmlwidget-3e9a9ab3a461eff0ae63" style="width:100%;height:600px;"></div>
<script type="application/json" data-for="htmlwidget-3e9a9ab3a461eff0ae63">{"x":{"message":{"prof":{"time":[1,2,3,4,5,6,7,8,9,9,10,10,11,11,12,12,13,13,14,14,15,15,16,16,17,17,18,18,19,19,20,20,21,21,22,22,23,23,24,24,25,25,25,26,27,27,28,28,29,30,30,31,31,32,32,33,33,33,34,34,34,35,35,36,36,37,38,38,39,39,39,40,41,41,42,43,43,43,44,44,45,45,46,47,47,48,48,48,48,49,50,51,51,52,52,53,53,54,54,55,55,56,56,57,57,58,58,59,60,60,61,61,62,62,63,63,64,64,65,65,65,66,66,67,68,69,70,70,71,71,72,72,73,73,74,74,74,75,75,76,76,77,77,78,79,79,80,80,81,82,83,83,83,84,84,85,85,86,87,87,87,88,88,88,89,90,90,91,91,92,92,92,93,93,94,95,95,96,97,98,98,99,100,100,101,101,101,102,102,102,103,103,104,104,105,105,106,106,107,108,109,110,110,110,111,111,112,112,113,113,114,114,115,115,115,116,116,117,117,118,118,118,118,119,119,120,120,121,121,122,122,123,123,124,124,125,125,126,126,126,127,127,128,128,128,129,130,130,131,132,133,134,134,134,135,136,136,137,138,138,139,139,140,140,141,141,142,142,143,143,144,145,145,146,147,148,148,149,149,149,150,151,151,152,153,153,154,155,156,156,157,157,158,159,160,161,162,163,164,164,165,165,166,166,166,167,167,168,168,168,169,169,170,170,171,171,172,172,173,174,175,175,175,176,177,177,178,179,180,181,181,182,183,184,184,185,185,186,186,187,187,188,188,189,189,190,190,191,191,192,193,194,194,195,195,196,196,197,198,198,199,199,200,200,201,202,203,203,204,204,205,205,206,206,207,207,208,208,209,209,210,210,211,211,212,212,213,214,214,215,215,216,216,217,218,218,218,219,219,220,221,221,221,222,222,222,223,223,224,225,225,226,227,228,228,228,229,230,230,231,231,232,232,233,233,234,234,234,235,235,236,236,237,237,237,238,238,239,240,240,241,242,242,242,243,243,244,244,244,245,245,245,246,246,247,248,249,249,250,251,251,252,252,253,253,254,254,255,255,256,256,256,257,257,258,258,259,259,260,260,260,261,262,262,263,263,264,264,265,265,265,266,266,267,267,268,268,269,270,270,271,272,273,273,274,275,275,276,276,277,277,277,278,278,278,279,279,280,281,281,282,283,283,284,284,285,285,286,287,288,288,288,289,289,290,290,290,291,291,292,292,293,293,294,294,295,295,296,296,297,297,298,298,299,300,300,301,302,302,302,303,303,304,305,306,306,306,307,307,308,308,309,310,310,311,312,312,313,314,314,315,315,316,317,317,318,318,319,320,320,321,321,322,322,323,324,324,325,325,326,326,327,328,328,328,329,329,330,330,331,332,332,333,333,334,334,335,335,336,336,337,337,338,338,339,339,340,340,341,341,342,342,342,343,343,343,344,344,344,345,345,346,347,347,348,348,349,349,349,350,350,351,351,352,353,354,354,355,355,356,356,357,358,359,360,360,360,361,361,361,362,362,363,363,364,364,365,365,366,367,367,367,368,368,369,369,369,370,370,371,371,372,372,373,373,373,374,375,375,376,376,377,377,378,379,379,380,381,381,382,383,383,384,384,384,385,385,385,386,386,386,387,387,387,388,388,388,389,389,389,390,390,390,391,391,391,392,392,392,393,393,393,394,394,394,395,395,395,396,396,396,397,397,397,398,398,398,399,399,399,400,400,400,401,401,401,402,402,402,403,403,403,404,404,404,405,405,405,406,406,406,407,407,407,408,408,408,409,410,410,411,411,412,412,413,413,414,414,415,415,416,416,417,418,419,420,421,421,422,423,423,424,424,424,425,426,427,427,428,428,429,429,430,430,431,432,432,433,434,435,435,436,436,437,437,438,438,438,439,439,440,440,441,442,442,443,443,444,444,444,445,445,446,446,447,447,448,448,448,449,450,450,450,451,451,451,452,453,453,454,454,455,456,456,456,457,457,458,458,459,459,460,460,461,462,462,462,463,463,464,465,465,465,466,466,467,467,468,468,469,469,469,470,470,471,471,472,472,473,473,474,474,475,475,476,477,477,477,478,478,478,479,479,479,480,481,481,482,482,483,484,485,486,486,487,487,488,489,489,490,490,491,491,492,492,493,494,495,495,496,497,497,498,499,499,499,500,500,501,501,502,502,503,503,504,504,505,505,505,506,506,506,507,507,508,508,509,510,511,511,512,512,513,513,514,514,515,516,516,517,517,518,519,519,519,520,520,521,521,522,522,523,524,524,525,526,527,527,528,528,529,529,529,530,530,531,531,532,532,533,533,534,535,535,536,536,537,537,538,539,539,539,540,541,541,542,543,543,544,544,545,545,545,546,546,546,547,547,548,548,549,550,550,551,551,552,553,553,554,554,555,555,556,556,557,557,558,558,558,559,559,560,560,561,561,562,562,563,563,564,565,565,566,567,567,568,568,569,569,569,570,570,571,571,572,573,573,574,574,575,576,576,577,577,578,578,578,579,580,581,582,582,583,583,584,584,585,586,586,587,588,588,589,589,590,590,591,592,592,593,593,594,594,595,596,596,597,598,599,599,600,601,602,602,603,603,604,604,605,606,607,607,608,608,608,609,609,610,611,611,612,613,613,614,614,615,615,616,616,617,618,619,619,620,620,621,621,622,622,623,623,623,624,624,625,626,626,627,627,628,628,629,629,630,631,631,632,632,632,633,633,633,634,634,635,636,636,637,637,638,638,639,640,640,641,641,642,643,644,644,644,645,645,645,646,646,646,647,648,648,649,649,650,650,651,651,652,652,653,653,654,655,656,656,656,657,657,657,658,658,659,660,660,661,661,661,662,662,663,663,664,664,665,665,666,667,667,667,668,668,668,669,669,670,670,671,672,673,674,674,675,675,676,676,676,677,677,678,678,679,679,679,680,680,680,681,681,681,682,682,682,683,683,683,684,684,684,685,685,685,686,686,686,687,687,687,688,688,688,689,689,689,690,690,690,691,691,692,692,693,693,694,694,695,695,696,696,697,697,698,698,699,699,699,700,700,701,701,702,702,703,703,704,704,705,705,705,706,706,707,708,708,709,709,710,710,711,711,712,712,713,714,714,714,715,715,716,716,717,718,718,719,720,720,721,721,722,723,723,724,724,725,725,725,726,726,726,727,727,728,728,729,729,730,731,731,731,732,732,733,733,734,734,735,735,736,736,736,737,737,737,738,739,739,740,740,740,741,741,742,742,743,743,744,744,745,746,746,747,747,747,747,748,748,748,748,749,749,750,750,751,752,752,753,754,754,755,755,756,757,758,758,758,759,759,759,760,761,761,761,762,762,763,764,765,765,766,766,767,768,769,769,769,770,770,770,771,771,772,772,773,773,774,774,775,775,776,776,777,778,778,779,779,779,780,780,780,781,781,782,782,782,783,783,784,784,785,786,786,787,788,788,789,789,790,791,791,792,792,793,793,794,794,795,796,797,797,798,798,799,800,800,801,801,802,802,803,803,804,804,804,805,805,806,806,806,807,808,809,809,810,810,811,811,811,812,812,813,813,814,814,815,815,816,816,817,818,818,819,819,820,821,822,822,822,823,823,823,824,824,825,825,826,827,828,828,828,829,830,830,831,832,832,833,833,833,834,834,834,835,835,836,836,837,838,838,839,839,840,840,841,841,842,843,844,844,845,845,846,846,847,847,848,848,849,850,850,851,851,852,853,854,854,855,855,856,856,857,858,859,859,860,860,861,861,862,862,863,863,864,864,864,865,865,865,866,867,867,868,868,869,870,870,871,871,872,872,873,873,874,874,874,874,875,875,875,875,876,876,877,877,878,878,879,879,880,880,880,881,881,882,882,883,884,884,885,885,886,886,886,887,887,888,889,889,890,890,891,891,892,893,894,894,894,895,895,895,896,896,897,898,898,899,899,900,900,901,902,903,903,904,904,905,905,906,907,907,908,908,909,910,910,911,912,913,913,913,914,914,914,915,915,915,916,916,916,917,917,917,918,918,918,919,919,919,920,920,920,921,921,921,922,922,922,923,923,923,924,925,925,926,926,927,928,929,930,930,931,932,932,932,933,933,933,934,934,934,935,935,935,936,936,937,937,938,938,939,940,940,941,941,942,942,942,943,943,944,944,945,945,946,946,947,947,948,948,949,949,950,950,951,951,951,952,952,952,953,953,954,954,955,955,956,956,957,958,958,959,959,960,960,960,961,961,961,962,962,963,964,964,965,965,965,966,966,967,967,968,968,969,969,970,970,971,972,972,972,973,974,974,975,975,975,976,976,977,977,978,978,978,979,979,979,980,980,981,981,982,983,983,984,984,984,985,985,986,987,987,987,988,988,988,989,990,990,991,991,992,992,993,993,994,994,995,996,997,997,998,998,999,999,1000,1000,1001,1001,1001,1002,1003,1003,1004,1004,1005,1006,1006,1007,1007,1008,1008,1008,1009,1009,1009,1010,1010,1011,1012,1013,1013,1014,1014,1014,1015,1015,1016,1016,1017,1017,1018,1018,1019,1019,1020,1021,1021,1022,1023,1024,1024,1025,1025,1026,1026,1026,1027,1027,1028,1028,1029,1029,1030,1030,1031,1031,1032,1032,1033,1034,1034,1034,1034,1035,1035,1035,1035,1036,1036,1036,1037,1037,1037,1038,1039,1039,1040,1040,1041,1042,1042,1043,1043,1043,1044,1045,1045,1046,1046,1047,1047,1048,1048,1049,1049,1050,1050,1051,1051,1052,1052,1053,1054,1054,1055,1055,1056,1056,1057,1057,1058,1058,1058,1059,1059,1059,1060,1060,1060,1061,1061,1061,1062,1062,1062,1063,1063,1063,1064,1064,1064,1065,1065,1066,1067,1067,1068,1069,1070,1070,1071,1071,1072,1073,1073,1074,1074,1075,1075,1076,1076,1077,1077,1078,1078,1079,1079,1080,1080,1081,1081,1082,1082,1083,1083,1084,1084,1085,1085,1086,1086,1087,1087,1088,1088,1089,1089,1090,1090,1091,1091,1092,1092,1093,1093,1094,1094,1095,1095,1096,1096,1097,1097,1098,1098,1099,1099,1100,1100,1101,1101,1102,1102,1103,1103,1104,1104,1105,1105,1106,1106,1107,1107,1108,1108,1109,1109,1110,1110,1111,1111,1112,1112,1113,1113,1114,1114,1115,1115,1116,1116,1117,1117,1118,1118,1119,1119,1120,1120,1121,1121,1122,1122,1123,1123,1124,1124,1125,1125,1126,1126,1127,1127,1127,1128,1128,1129,1129,1130,1130,1131,1132,1133,1134,1134,1135,1135,1135,1136,1136,1137,1138,1139,1139,1140,1140,1140,1141,1141,1142,1143,1143,1144,1145,1146,1147,1147,1148,1148,1149,1150,1150,1150,1151,1151,1151,1152,1152,1153,1154,1154,1155,1155,1156,1156,1156,1157,1158,1158,1159,1159,1160,1161,1162,1162,1163,1164,1165,1165,1166,1166,1167,1168,1168,1169,1169,1170,1171,1172,1173,1173,1173,1174,1174,1174,1175,1175,1175,1176,1176,1177,1178,1179,1179,1180,1181,1181,1181,1182,1182,1183,1183,1184,1184,1185,1185,1186,1186,1187,1187,1188,1189,1189,1190,1190,1191,1191,1192,1192,1193,1194,1194,1195,1195,1196,1196,1196,1197,1197,1197,1198,1198,1198,1199,1199,1200,1201,1202,1202,1203,1203,1204,1204,1205,1206,1207,1207,1208,1208,1209,1210,1210,1211,1211,1212,1213,1214,1214,1214,1215,1216,1216,1217,1218,1219,1219,1219,1220,1220,1220,1221,1221,1221,1222,1222,1223,1223,1223,1224,1224,1224,1225,1225,1226,1226,1227,1227,1228,1228,1229,1229,1230,1231,1232,1233,1234,1234,1235,1235,1236,1236,1237,1237,1237,1238,1238,1238,1239,1240,1240,1241,1242,1242,1243,1243,1244,1245,1246,1246,1247,1247,1248,1248,1249,1249,1250,1251,1251,1252,1252,1253,1253,1253,1254,1255,1255,1256,1256,1256,1257,1257,1258,1258,1259,1259,1260,1260,1261,1262,1262,1263,1263,1264,1264,1264,1265,1265,1265,1266,1266,1266,1267,1267,1268,1268,1269,1269,1270,1270,1271,1272,1272,1273,1273,1274,1274,1275,1275,1276,1276,1277,1277,1277,1278,1279,1280,1280,1281,1282,1283,1283,1283,1284,1284,1285,1286,1286,1287,1287,1288,1288,1289,1289,1290,1290,1291,1291,1292,1292,1293,1294,1294,1295,1295,1296,1296,1297,1298,1298,1299,1300,1300,1301,1301,1302,1303,1304,1304,1305,1305,1306,1306,1307,1308,1309,1309,1310,1310,1311,1312,1312,1313,1313,1314,1314,1315,1315,1316,1316,1316,1317,1318,1318,1319,1319,1320,1321,1321,1321,1322,1323,1324,1324,1325,1326,1326,1327,1328,1328,1329,1329,1330,1330,1331,1332,1333,1334,1334,1334,1335,1335,1335,1336,1336,1337,1338,1338,1338,1339,1339,1340,1341,1342,1343,1343,1343,1344,1344,1345,1345,1345,1346,1347,1348,1348,1349,1349,1350,1351,1352,1352,1353,1354,1354,1355,1355,1355,1356,1356,1356,1357,1358,1358,1359,1360,1360,1361,1361,1361,1362,1362,1363,1363,1364,1364,1365,1366,1366,1367,1367,1368,1368,1369,1369,1370,1370,1371,1371,1372,1372,1373,1373,1374,1374,1375,1375,1376,1376,1377,1377,1378,1379,1379,1380,1380,1381,1381,1382,1382,1383,1383,1384,1384,1385,1385,1386,1386,1387,1387,1388,1388,1389,1389,1390,1390,1391,1391,1392,1392,1393,1393,1394,1394,1395,1395,1396,1396,1397,1397,1398,1398,1398,1398,1398,1398,1399,1399,1399,1399,1399,1399,1399,1399,1400,1400,1400,1400,1400,1400,1400,1400,1401,1401,1401,1401,1401,1401,1401,1401,1402,1402,1402,1402,1402,1402,1402,1402,1403,1403,1403,1403,1403,1403,1403,1403,1404,1404,1404,1404,1404,1404,1404,1404,1405,1405,1405,1405,1405,1405,1405,1405,1406,1406,1406,1406,1406,1406,1406,1406,1407,1407,1407,1407,1407,1407,1407,1407,1408,1408,1408,1408,1408,1408,1408,1408,1409,1409,1409,1409,1409,1409,1409,1409,1410,1410,1410,1410,1410,1410,1410,1410,1411,1411,1411,1411,1411,1411,1411,1411,1412,1412,1412,1412,1412,1412,1412,1412,1413,1413,1413,1413,1413,1413,1413,1413,1414,1414,1414,1414,1414,1414,1414,1414,1415,1415,1415,1415,1415,1415,1415,1415,1416,1416,1416,1416,1416,1416,1416,1416,1417,1417,1417,1417,1417,1417,1417,1417],"depth":[1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,3,2,1,1,2,1,1,3,2,1,2,1,2,1,1,2,1,4,3,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,1,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,1,1,3,2,1,2,1,2,1,1,3,2,1,3,2,1,1,2,1,2,1,3,2,1,2,1,1,2,1,1,1,2,1,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,1,1,1,3,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,4,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,3,2,1,1,2,1,1,1,1,3,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,1,2,1,3,2,1,1,2,1,1,2,1,1,1,2,1,2,1,1,1,1,1,1,1,2,1,2,1,3,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,1,3,2,1,1,2,1,1,1,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,3,2,1,2,1,1,3,2,1,3,2,1,2,1,1,2,1,1,1,3,2,1,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,3,2,1,2,1,1,2,1,1,3,2,1,2,1,3,2,1,3,2,1,2,1,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,1,1,2,1,1,2,1,2,1,3,2,1,3,2,1,2,1,1,2,1,1,2,1,2,1,2,1,1,1,3,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,3,2,1,2,1,1,1,3,2,1,2,1,2,1,1,2,1,1,2,1,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,3,2,1,2,1,2,1,1,1,2,1,2,1,2,1,1,1,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,3,2,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,1,2,1,1,2,1,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,1,1,2,1,1,2,1,3,2,1,1,1,2,1,2,1,2,1,2,1,1,2,1,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,3,2,1,1,3,2,1,3,2,1,1,2,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,1,3,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,3,2,1,1,2,1,2,1,1,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,1,2,1,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,3,2,1,2,1,2,1,2,1,1,2,1,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,3,2,1,1,2,1,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,3,2,1,1,1,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,1,1,2,1,1,1,2,1,2,1,2,1,1,1,2,1,3,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,1,1,3,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,3,2,1,3,2,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,2,1,2,1,1,1,1,2,1,2,1,3,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,1,2,1,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,4,3,2,1,4,3,2,1,2,1,2,1,1,2,1,1,2,1,2,1,1,1,3,2,1,3,2,1,1,3,2,1,2,1,1,1,2,1,2,1,1,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,3,2,1,2,1,3,2,1,2,1,2,1,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,2,1,3,2,1,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,1,3,2,1,3,2,1,2,1,2,1,1,1,3,2,1,1,2,1,1,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,4,3,2,1,4,3,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,2,1,1,1,3,2,1,3,2,1,2,1,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,1,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,1,2,1,2,1,1,1,1,2,1,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,1,2,1,3,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,3,2,1,2,1,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,2,1,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,4,3,2,1,4,3,2,1,3,2,1,3,2,1,1,2,1,2,1,1,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,1,2,1,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,1,1,2,1,3,2,1,2,1,1,1,2,1,3,2,1,2,1,1,2,1,1,1,1,2,1,2,1,1,3,2,1,3,2,1,2,1,1,2,1,2,1,3,2,1,1,2,1,2,1,1,1,2,1,1,1,2,1,2,1,1,2,1,2,1,1,1,1,3,2,1,3,2,1,3,2,1,2,1,1,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,1,1,2,1,2,1,2,1,1,1,2,1,2,1,1,2,1,2,1,1,1,3,2,1,1,2,1,1,1,3,2,1,3,2,1,3,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,1,1,1,2,1,2,1,2,1,3,2,1,3,2,1,1,2,1,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,1,2,1,1,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,1,1,2,1,2,1,2,1,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,1,3,2,1,1,1,2,1,1,2,1,1,2,1,2,1,2,1,1,1,1,3,2,1,3,2,1,2,1,1,3,2,1,2,1,1,1,1,3,2,1,2,1,3,2,1,1,1,2,1,2,1,1,1,2,1,1,2,1,3,2,1,3,2,1,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1],"label":["rowSums","rowSums","rowSums","rowSums","rowMeans","rowMeans","rowMeans","rowMeans","aperm.default","apply","aperm.default","apply","aperm.default","apply","aperm.default","apply","aperm.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","mean.default","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","apply","length","local","FUN","apply","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","apply","mean.default","apply","<GC>","FUN","apply","apply","FUN","apply","apply","isTRUE","mean.default","apply","is.numeric","local","FUN","apply","apply","mean.default","apply","<GC>","isTRUE","mean.default","apply","apply","apply","mean.default","apply","mean.default","apply","length","local","FUN","apply","FUN","apply","mean.default","apply","<GC>","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","<GC>","FUN","apply","FUN","apply","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","FUN","apply","is.na","local","mean.default","apply","apply","is.numeric","local","mean.default","apply","apply","apply","<GC>","mean.default","apply","mean.default","apply","mean.default","apply","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","mean.default","apply","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","FUN","apply","apply","apply","FUN","apply","apply","mean.default","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","apply","apply","<GC>","length","local","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","<GC>","isTRUE","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","apply","is.na","local","apply","apply","apply","isTRUE","mean.default","apply","apply","mean.default","apply","apply","is.numeric","local","FUN","apply","FUN","apply","<GC>","apply","FUN","apply","mean.default","apply","apply","FUN","apply","apply","apply","mean.default","apply","<GC>","is.numeric","local","apply","mean.default","apply","apply","is.numeric","local","apply","apply","FUN","apply","<GC>","apply","apply","apply","apply","apply","apply","apply","FUN","apply","mean.default","apply","<GC>","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","<GC>","FUN","apply","apply","mean.default","apply","apply","apply","apply","FUN","apply","apply","apply","<GC>","apply","<GC>","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","mean.default","apply","<GC>","apply","mean.default","apply","apply","is.numeric","local","FUN","apply","FUN","apply","apply","apply","mean.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","apply","FUN","apply","FUN","apply","mean.default","apply","apply","isTRUE","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","FUN","apply","apply","is.na","local","apply","apply","isTRUE","mean.default","apply","apply","FUN","apply","length","local","FUN","apply","mean.default","apply","<GC>","mean.default","apply","is.na","local","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","length","local","apply","isTRUE","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","length","local","apply","apply","FUN","apply","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","<GC>","FUN","apply","length","local","length","local","FUN","apply","isTRUE","mean.default","apply","apply","length","local","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","<GC>","apply","mean.default","apply","apply","FUN","apply","apply","apply","FUN","apply","apply","FUN","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","FUN","apply","apply","apply","<GC>","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","length","local","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","apply","is.numeric","local","apply","is.numeric","local","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","<GC>","FUN","apply","FUN","apply","mean.default","apply","apply","FUN","apply","apply","mean.default","apply","apply","<GC>","apply","is.numeric","local","apply","FUN","apply","length","local","apply","mean.default","apply","<GC>","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","mean.default","apply","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","apply","is.numeric","local","mean.default","apply","FUN","apply","length","local","mean.default","apply","mean.default","apply","<GC>","is.na","local","isTRUE","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","<GC>","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","apply","apply","<GC>","apply","mean.default","apply","length","local","apply","apply","apply","isTRUE","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","is.na","local","apply","<GC>","FUN","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","FUN","apply","mean.default","apply","apply","<GC>","apply","apply","FUN","apply","apply","is.na","local","isTRUE","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","mean.default","apply","FUN","apply","FUN","apply","is.numeric","local","mean.default","apply","mean.default","apply","mean.default","apply","apply","apply","apply","apply","FUN","apply","apply","FUN","apply","<GC>","FUN","apply","apply","apply","FUN","apply","is.numeric","local","FUN","apply","mean.default","apply","apply","FUN","apply","apply","apply","FUN","apply","length","local","mean.default","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","length","local","mean.default","apply","isTRUE","mean.default","apply","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","apply","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","apply","<GC>","mean.default","apply","FUN","apply","is.na","local","FUN","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","is.numeric","local","FUN","apply","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","is.na","local","apply","apply","apply","length","local","FUN","apply","apply","FUN","apply","FUN","apply","mean.default","apply","<GC>","apply","apply","apply","mean.default","apply","apply","mean.default","apply","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","<GC>","is.numeric","local","<GC>","is.numeric","local","FUN","apply","FUN","apply","apply","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","apply","FUN","apply","FUN","apply","apply","<GC>","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","FUN","apply","apply","apply","is.numeric","local","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","<GC>","apply","FUN","apply","apply","FUN","apply","mean.default","apply","is.numeric","local","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","is.numeric","local","FUN","apply","apply","mean.default","apply","FUN","apply","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","<GC>","FUN","apply","mean.default","apply","is.numeric","local","FUN","apply","FUN","apply","FUN","apply","apply","mean.default","apply","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","is.numeric","local","<GC>","apply","apply","FUN","apply","FUN","apply","apply","is.numeric","local","is.na","local","isTRUE","mean.default","apply","apply","apply","apply","is.numeric","local","<GC>","apply","<GC>","apply","apply","mean.default","apply","apply","mean.default","apply","mean.default","apply","mean.default","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","<GC>","apply","apply","apply","FUN","apply","apply","apply","FUN","apply","is.na","local","FUN","apply","apply","apply","FUN","apply","<GC>","FUN","apply","length","local","apply","FUN","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","apply","apply","FUN","apply","<GC>","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","apply","is.na","local","is.na","local","FUN","apply","apply","mean.default","apply","mean.default","apply","apply","apply","<GC>","mean.default","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","apply","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","apply","apply","apply","FUN","apply","is.numeric","local","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","<GC>","apply","mean.default","apply","isTRUE","mean.default","apply","length","local","apply","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","FUN","apply","length","local","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","length","local","length","local","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","length","local","mean.default","apply","apply","FUN","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","isTRUE","mean.default","apply","mean.default","apply","apply","apply","FUN","apply","FUN","apply","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","is.na","local","FUN","apply","FUN","apply","length","local","is.numeric","local","FUN","apply","apply","mean.default","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","apply","FUN","apply","mean.default","apply","apply","<GC>","apply","length","local","mean.default","apply","mean.default","apply","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","<GC>","apply","<GC>","apply","FUN","apply","isTRUE","mean.default","apply","is.numeric","local","isTRUE","mean.default","apply","apply","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","<GC>","apply","<GC>","apply","mean.default","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","FUN","apply","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","apply","mean.default","apply","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","mean.default","apply","apply","length","local","FUN","apply","FUN","apply","mean.default","apply","apply","apply","<GC>","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","mean.default","apply","apply","apply","<GC>","apply","<GC>","apply","FUN","apply","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","is.na","local","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","length","local","mean.default","apply","apply","mean.default","apply","is.na","local","FUN","apply","FUN","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","<GC>","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","<GC>","apply","<GC>","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","mean.default","apply","FUN","apply","apply","apply","apply","mean.default","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","is.na","local","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","length","local","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","length","local","FUN","apply","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","apply","length","local","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","<GC>","apply","<GC>","apply","apply","isTRUE","mean.default","apply","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","mean.default","apply","FUN","apply","is.numeric","local","mean.default","apply","FUN","apply","apply","apply","is.numeric","local","<GC>","apply","<GC>","apply","length","local","isTRUE","mean.default","apply","apply","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","<GC>","apply","<GC>","apply","FUN","apply","apply","FUN","apply","apply","apply","FUN","apply","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","is.na","local","mean.default","apply","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","is.numeric","local","FUN","apply","apply","mean.default","apply","<GC>","FUN","apply","apply","is.na","local","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","apply","<GC>","apply","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","<GC>","is.numeric","local","mean.default","apply","apply","FUN","apply","apply","apply","mean.default","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","apply","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","mean.default","apply","isTRUE","mean.default","apply","is.numeric","local","apply","mean.default","apply","apply","apply","apply","FUN","apply","FUN","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","apply","length","local","FUN","apply","apply","apply","mean.default","apply","apply","apply","mean.default","apply","mean.default","apply","apply","is.na","local","mean.default","apply","apply","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","apply","apply","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","is.numeric","local","FUN","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","apply","apply","length","local","FUN","apply","FUN","apply","apply","apply","mean.default","apply","mean.default","apply","apply","is.na","local","mean.default","apply","apply","apply","isTRUE","mean.default","apply","apply","mean.default","apply","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","apply","apply","apply","apply","FUN","apply","length","local","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","apply","apply","mean.default","apply","length","local","FUN","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","<GC>","length","local","<GC>","length","local","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","apply","length","local","length","local","mean.default","apply","length","local","FUN","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","length","local","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","apply","FUN","apply","FUN","apply","mean.default","apply","apply","is.na","local","apply","mean.default","apply","mean.default","apply","apply","apply","FUN","apply","mean.default","apply","FUN","apply","apply","apply","length","local","FUN","apply","apply","is.na","local","<GC>","apply","<GC>","apply","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","mean.default","apply","apply","isTRUE","mean.default","apply","apply","apply","is.numeric","local","apply","FUN","apply","apply","FUN","apply","FUN","apply","is.na","local","apply","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","apply","isTRUE","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","apply","apply","length","local","FUN","apply","apply","apply","mean.default","apply","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","is.na","local","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","FUN","apply","FUN","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","lapply","findLocalsList1","findLocalsList","findLocals","compile","compiler:::tryCompile","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis"],"filenum":[1,1,1,1,1,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,1,null,1,null,1,1,null,null,null,1,null,1,null,null,1,null,null,1,null,1,null,1,1,null,1,null,null,1,1,null,1,1,null,null,1,null,null,null,1,1,null,1,null,null,null,1,1,1,null,1,null,1,null,null,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,1,1,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,null,null,1,1,null,null,null,1,1,1,null,null,1,null,1,null,1,1,null,null,1,null,null,1,1,null,1,null,1,null,null,1,null,1,1,null,1,1,1,null,1,1,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,1,1,1,null,null,null,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,null,1,1,null,null,1,1,1,null,null,1,1,null,1,1,null,null,null,1,null,1,null,1,null,1,null,1,1,null,1,1,1,null,1,null,null,null,1,null,1,1,null,null,1,1,null,1,null,1,1,1,1,1,1,1,null,1,null,1,null,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,1,1,null,null,1,1,null,1,1,1,1,null,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,1,null,1,null,1,null,1,1,null,null,null,1,null,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,1,null,null,1,null,1,1,null,null,1,null,null,1,null,1,1,null,null,1,1,null,null,1,1,null,1,null,null,null,1,null,1,null,null,1,null,null,null,1,null,null,1,null,1,1,null,null,1,null,null,1,null,1,null,null,1,null,null,1,null,null,1,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,null,null,null,1,null,null,1,1,null,null,null,1,null,1,null,null,1,null,1,null,1,null,1,1,null,1,1,1,null,1,1,null,1,null,1,null,null,1,null,null,1,null,1,1,null,1,1,null,1,null,1,null,1,1,1,null,null,1,null,1,null,null,1,null,null,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,1,1,1,null,null,1,null,1,null,1,1,null,1,1,null,1,1,null,1,null,null,1,null,1,null,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,1,null,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,null,null,1,null,1,null,null,null,1,null,1,null,null,null,null,null,1,null,null,1,null,1,1,null,1,null,1,null,null,1,null,1,null,1,1,1,null,1,null,1,null,null,1,1,1,null,null,1,null,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,1,null,null,1,null,1,null,1,null,1,null,null,1,1,null,1,null,1,null,1,1,null,1,1,null,1,1,null,null,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,1,null,1,null,1,null,1,null,null,null,1,null,1,null,1,1,1,1,1,null,1,1,null,1,null,null,1,1,1,null,1,null,null,null,1,null,1,1,null,1,1,1,null,1,null,null,null,1,null,null,1,null,1,null,1,1,null,1,null,1,null,null,1,null,1,null,null,null,1,null,null,1,1,null,null,1,null,null,1,1,null,1,null,1,1,null,null,1,null,1,null,1,null,1,null,1,1,null,null,1,null,1,1,null,null,1,null,1,null,null,null,1,null,null,1,null,1,null,1,null,1,null,1,null,null,null,1,1,null,null,1,null,null,1,null,null,1,1,null,1,null,null,1,1,1,null,null,null,1,1,null,1,null,1,null,1,null,1,1,1,null,1,1,null,1,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,null,null,null,null,null,null,1,null,1,1,1,null,1,null,1,null,1,null,1,1,null,1,null,1,1,null,null,1,null,1,null,1,null,1,1,null,1,1,1,null,null,null,1,null,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,null,1,null,null,1,1,null,1,1,null,1,null,1,null,null,1,null,null,1,null,null,null,1,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,null,null,1,null,1,null,1,1,null,1,1,null,1,null,1,null,null,1,null,null,null,1,1,null,1,null,1,1,null,null,null,null,null,null,1,1,1,1,null,null,null,1,null,1,1,null,1,1,null,1,null,1,null,1,1,null,1,null,1,null,1,1,null,1,1,1,null,1,1,1,null,1,null,null,null,1,1,1,null,1,null,null,1,null,null,1,null,1,1,null,1,null,1,null,1,null,1,1,1,null,1,null,1,null,1,null,1,null,null,1,null,1,1,null,1,null,1,null,1,null,1,1,null,1,null,null,1,null,null,1,null,1,1,null,null,null,null,null,1,1,null,1,null,1,1,1,null,null,1,null,null,1,null,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,1,1,null,null,1,null,null,1,null,1,1,null,1,null,null,1,null,1,null,1,null,1,null,1,1,null,null,1,null,null,1,null,1,null,1,1,1,1,null,1,null,null,null,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,1,null,null,1,null,1,null,1,1,null,1,1,null,1,null,null,1,null,1,null,1,null,null,1,null,null,1,null,1,null,1,null,1,1,null,null,1,null,null,null,null,null,1,null,1,null,null,1,null,null,1,1,null,1,null,null,1,null,1,null,1,null,null,null,1,1,null,1,null,null,null,1,null,null,null,1,null,1,null,1,1,null,1,1,null,1,null,1,1,1,null,null,1,null,null,1,1,null,null,1,null,1,1,1,null,1,null,1,1,1,null,null,1,null,null,1,null,null,null,1,null,1,null,null,null,null,null,1,1,null,1,null,null,1,null,null,1,null,1,null,null,1,null,1,null,1,1,null,1,1,null,1,null,1,1,null,1,null,null,null,1,null,1,1,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,null,1,null,null,null,null,1,1,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,1,1,null,null,1,null,null,1,null,1,null,1,1,1,null,null,1,1,null,1,1,null,1,null,null,1,null,null,1,null,1,null,1,1,null,null,null,1,null,1,null,1,1,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,1,1,null,1,null,1,null,1,1,1,null,1,null,1,null,1,null,null,null,1,null,null,1,null,null,1,1,null,null,null,1,1,null,1,null,null,null,1,null,1,null,null,null,1,null,null,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,1,null,1,null,1,null,null,1,null,1,1,null,1,null,1,null,1,1,1,null,null,1,null,null,1,null,1,1,null,1,null,1,null,1,1,1,null,1,null,1,null,1,1,null,1,null,1,1,null,1,1,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,1,null,1,null,1,1,1,1,null,1,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,null,1,null,1,null,1,null,null,1,null,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,null,null,1,null,1,null,1,1,null,1,null,1,null,null,1,null,null,1,null,1,1,null,null,null,null,1,null,1,null,1,null,1,null,1,null,1,1,null,null,1,1,null,1,null,null,1,null,1,null,1,null,null,1,null,null,1,null,1,null,1,1,null,1,null,null,1,null,1,1,null,null,1,null,null,1,1,null,1,null,1,null,null,null,1,null,1,1,1,null,null,null,1,null,1,null,null,null,null,1,1,null,1,null,1,1,null,1,null,1,null,null,1,null,null,1,null,1,1,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,1,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,null,null,1,1,null,null,null,1,null,null,null,1,null,null,1,null,null,1,1,null,null,null,1,1,null,1,null,null,1,1,null,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,null,1,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,1,1,null,1,1,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,1,1,1,null,1,null,null,1,null,1,1,1,null,1,null,null,1,null,null,1,null,1,1,1,1,null,1,null,1,1,null,null,1,null,null,1,null,1,1,null,1,null,1,null,null,1,1,null,null,null,1,1,1,null,1,1,1,null,1,null,1,1,null,null,null,1,1,1,1,null,null,1,null,null,1,null,null,1,null,1,1,1,null,1,1,null,null,1,null,1,null,1,null,1,null,1,null,null,null,1,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,1,1,1,null,null,null,1,null,1,1,1,null,1,null,1,1,null,null,null,1,1,1,null,null,1,1,null,1,1,1,null,null,1,null,null,1,null,null,1,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,1,1,1,1,null,1,null,null,null,1,null,null,1,null,null,1,1,null,1,1,null,1,null,1,1,1,null,1,null,null,null,1,null,1,1,null,1,null,1,null,null,1,1,null,1,null,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,null,null,null,null,null,null,null,1,null,1,null,1,null,1,null,1,1,null,null,null,null,null,1,null,null,null,1,null,null,1,1,1,null,1,1,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,1,null,null,1,null,1,null,1,1,1,null,1,null,1,null,1,1,1,null,null,null,1,1,null,null,null,1,null,1,null,1,null,null,1,1,null,1,null,1,1,null,null,1,1,1,null,null,1,null,1,1,null,1,null,1,null,null,1,1,1,null,null,1,null,null,1,null,1,1,null,null,1,null,1,1,1,1,null,null,1,null,1,null,null,1,1,1,null,null,null,1,1,1,null,1,1,null,1,null,null,1,null,null,1,1,null,null,1,null,1,null,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,null,null,null,1,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null],"linenum":[10,10,10,10,11,11,11,11,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,12,null,12,null,12,12,null,null,null,12,null,12,null,null,12,null,null,12,null,12,null,12,12,null,12,null,null,12,12,null,12,12,null,null,12,null,null,null,12,12,null,12,null,null,null,12,12,12,null,12,null,12,null,null,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,12,12,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,null,null,12,12,null,null,null,12,12,12,null,null,12,null,12,null,12,12,null,null,12,null,null,12,12,null,12,null,12,null,null,12,null,12,12,null,12,12,12,null,12,12,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,12,12,12,null,null,null,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,null,12,12,null,null,12,12,12,null,null,12,12,null,12,12,null,null,null,12,null,12,null,12,null,12,null,12,12,null,12,12,12,null,12,null,null,null,12,null,12,12,null,null,12,12,null,12,null,12,12,12,12,12,12,12,null,12,null,12,null,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,12,12,null,null,12,12,null,12,12,12,12,null,12,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,12,null,12,null,12,null,12,12,null,null,null,12,null,12,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,12,null,null,12,null,12,12,null,null,12,null,null,12,null,12,12,null,null,12,12,null,null,12,12,null,12,null,null,null,12,null,12,null,null,12,null,null,null,12,null,null,12,null,12,12,null,null,12,null,null,12,null,12,null,null,12,null,null,12,null,null,12,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,null,null,null,12,null,null,12,12,null,null,null,12,null,12,null,null,12,null,12,null,12,null,12,12,null,12,12,12,null,12,12,null,12,null,12,null,null,12,null,null,12,null,12,12,null,12,12,null,12,null,12,null,12,12,12,null,null,12,null,12,null,null,12,null,null,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,12,12,12,null,null,12,null,12,null,12,12,null,12,12,null,12,12,null,12,null,null,12,null,12,null,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,12,null,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,null,null,12,null,12,null,null,null,12,null,12,null,null,null,null,null,12,null,null,12,null,12,12,null,12,null,12,null,null,12,null,12,null,12,12,12,null,12,null,12,null,null,12,12,12,null,null,12,null,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,12,null,null,12,null,12,null,12,null,12,null,null,12,12,null,12,null,12,null,12,12,null,12,12,null,12,12,null,null,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,12,null,12,null,12,null,12,null,null,null,12,null,12,null,12,12,12,12,12,null,12,12,null,12,null,null,12,12,12,null,12,null,null,null,12,null,12,12,null,12,12,12,null,12,null,null,null,12,null,null,12,null,12,null,12,12,null,12,null,12,null,null,12,null,12,null,null,null,12,null,null,12,12,null,null,12,null,null,12,12,null,12,null,12,12,null,null,12,null,12,null,12,null,12,null,12,12,null,null,12,null,12,12,null,null,12,null,12,null,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,null,null,12,12,null,null,12,null,null,12,null,null,12,12,null,12,null,null,12,12,12,null,null,null,12,12,null,12,null,12,null,12,null,12,12,12,null,12,12,null,12,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,null,null,null,null,null,null,12,null,12,12,12,null,12,null,12,null,12,null,12,12,null,12,null,12,12,null,null,12,null,12,null,12,null,12,12,null,12,12,12,null,null,null,12,null,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,null,12,null,null,12,12,null,12,12,null,12,null,12,null,null,12,null,null,12,null,null,null,12,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,null,null,12,null,12,null,12,12,null,12,12,null,12,null,12,null,null,12,null,null,null,12,12,null,12,null,12,12,null,null,null,null,null,null,12,12,12,12,null,null,null,12,null,12,12,null,12,12,null,12,null,12,null,12,12,null,12,null,12,null,12,12,null,12,12,12,null,12,12,12,null,12,null,null,null,12,12,12,null,12,null,null,12,null,null,12,null,12,12,null,12,null,12,null,12,null,12,12,12,null,12,null,12,null,12,null,12,null,null,12,null,12,12,null,12,null,12,null,12,null,12,12,null,12,null,null,12,null,null,12,null,12,12,null,null,null,null,null,12,12,null,12,null,12,12,12,null,null,12,null,null,12,null,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,12,12,null,null,12,null,null,12,null,12,12,null,12,null,null,12,null,12,null,12,null,12,null,12,12,null,null,12,null,null,12,null,12,null,12,12,12,12,null,12,null,null,null,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,12,null,null,12,null,12,null,12,12,null,12,12,null,12,null,null,12,null,12,null,12,null,null,12,null,null,12,null,12,null,12,null,12,12,null,null,12,null,null,null,null,null,12,null,12,null,null,12,null,null,12,12,null,12,null,null,12,null,12,null,12,null,null,null,12,12,null,12,null,null,null,12,null,null,null,12,null,12,null,12,12,null,12,12,null,12,null,12,12,12,null,null,12,null,null,12,12,null,null,12,null,12,12,12,null,12,null,12,12,12,null,null,12,null,null,12,null,null,null,12,null,12,null,null,null,null,null,12,12,null,12,null,null,12,null,null,12,null,12,null,null,12,null,12,null,12,12,null,12,12,null,12,null,12,12,null,12,null,null,null,12,null,12,12,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,null,12,null,null,null,null,12,12,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,12,12,null,null,12,null,null,12,null,12,null,12,12,12,null,null,12,12,null,12,12,null,12,null,null,12,null,null,12,null,12,null,12,12,null,null,null,12,null,12,null,12,12,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,12,12,null,12,null,12,null,12,12,12,null,12,null,12,null,12,null,null,null,12,null,null,12,null,null,12,12,null,null,null,12,12,null,12,null,null,null,12,null,12,null,null,null,12,null,null,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,12,null,12,null,12,null,null,12,null,12,12,null,12,null,12,null,12,12,12,null,null,12,null,null,12,null,12,12,null,12,null,12,null,12,12,12,null,12,null,12,null,12,12,null,12,null,12,12,null,12,12,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,12,null,12,null,12,12,12,12,null,12,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,null,12,null,12,null,12,null,null,12,null,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,null,null,12,null,12,null,12,12,null,12,null,12,null,null,12,null,null,12,null,12,12,null,null,null,null,12,null,12,null,12,null,12,null,12,null,12,12,null,null,12,12,null,12,null,null,12,null,12,null,12,null,null,12,null,null,12,null,12,null,12,12,null,12,null,null,12,null,12,12,null,null,12,null,null,12,12,null,12,null,12,null,null,null,12,null,12,12,12,null,null,null,12,null,12,null,null,null,null,12,12,null,12,null,12,12,null,12,null,12,null,null,12,null,null,12,null,12,12,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,12,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,null,null,12,12,null,null,null,12,null,null,null,12,null,null,12,null,null,12,12,null,null,null,12,12,null,12,null,null,12,12,null,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,null,12,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,12,12,null,12,12,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,12,12,12,null,12,null,null,12,null,12,12,12,null,12,null,null,12,null,null,12,null,12,12,12,12,null,12,null,12,12,null,null,12,null,null,12,null,12,12,null,12,null,12,null,null,12,12,null,null,null,12,12,12,null,12,12,12,null,12,null,12,12,null,null,null,12,12,12,12,null,null,12,null,null,12,null,null,12,null,12,12,12,null,12,12,null,null,12,null,12,null,12,null,12,null,12,null,null,null,12,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,12,12,12,null,null,null,12,null,12,12,12,null,12,null,12,12,null,null,null,12,12,12,null,null,12,12,null,12,12,12,null,null,12,null,null,12,null,null,12,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,12,12,12,12,null,12,null,null,null,12,null,null,12,null,null,12,12,null,12,12,null,12,null,12,12,12,null,12,null,null,null,12,null,12,12,null,12,null,12,null,null,12,12,null,12,null,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,null,null,null,null,null,null,null,12,null,12,null,12,null,12,null,12,12,null,null,null,null,null,12,null,null,null,12,null,null,12,12,12,null,12,12,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,12,null,null,12,null,12,null,12,12,12,null,12,null,12,null,12,12,12,null,null,null,12,12,null,null,null,12,null,12,null,12,null,null,12,12,null,12,null,12,12,null,null,12,12,12,null,null,12,null,12,12,null,12,null,12,null,null,12,12,12,null,null,12,null,null,12,null,12,12,null,null,12,null,12,12,12,12,null,null,12,null,12,null,null,12,12,12,null,null,null,12,12,12,null,12,12,null,12,null,null,12,null,null,12,12,null,null,12,null,12,null,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,null,null,null,13,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null],"memalloc":[124.5373001098633,124.5373001098633,124.5373001098633,124.5373001098633,139.8195343017578,139.8195343017578,139.8195343017578,139.8195343017578,170.2852783203125,170.2852783203125,170.2852783203125,170.2852783203125,170.2852783203125,170.2852783203125,170.2852783203125,170.2852783203125,170.2852783203125,170.2852783203125,170.2853240966797,170.2853240966797,170.2853240966797,170.2853240966797,170.2853240966797,170.2853240966797,170.2853240966797,170.2853240966797,170.2853240966797,170.2853240966797,170.2853240966797,170.2853240966797,170.2853240966797,170.2853240966797,170.2850189208984,170.2850189208984,185.7254867553711,185.7254867553711,185.9886932373047,185.9886932373047,186.2847061157227,186.2847061157227,186.620246887207,186.620246887207,186.620246887207,186.9838714599609,187.3512496948242,187.3512496948242,187.7436141967773,187.7436141967773,188.1526031494141,188.5659484863281,188.5659484863281,185.7220306396484,185.7220306396484,186.1029891967773,186.1029891967773,186.4122009277344,186.4122009277344,186.4122009277344,186.7168273925781,186.7168273925781,186.7168273925781,187.1178283691406,187.1178283691406,187.5142211914062,187.5142211914062,187.9254531860352,188.3392944335938,188.3392944335938,188.6709213256836,188.6709213256836,188.6709213256836,185.9792709350586,186.3478775024414,186.3478775024414,186.7232208251953,187.1135177612305,187.1135177612305,187.1135177612305,187.4820175170898,187.4820175170898,187.7652130126953,187.7652130126953,188.1631774902344,188.5660934448242,188.5660934448242,188.7526397705078,188.7526397705078,188.7526397705078,188.7526397705078,186.198860168457,186.4680404663086,186.746826171875,186.746826171875,187.126708984375,187.126708984375,187.5122299194336,187.5122299194336,187.8991317749023,187.8991317749023,188.2957229614258,188.2957229614258,188.6953048706055,188.6953048706055,188.833137512207,188.833137512207,186.3689880371094,186.3689880371094,186.7311553955078,187.1097106933594,187.1097106933594,187.477165222168,187.477165222168,187.8411102294922,187.8411102294922,188.1936340332031,188.1936340332031,188.5712585449219,188.5712585449219,188.9123229980469,188.9123229980469,188.9123229980469,186.2861099243164,186.2861099243164,186.6348495483398,187.0096664428711,187.3795013427734,187.7601089477539,187.7601089477539,188.1218338012695,188.1218338012695,188.492546081543,188.492546081543,188.9068603515625,188.9068603515625,188.9902114868164,188.9902114868164,188.9902114868164,186.494140625,186.494140625,186.8568801879883,186.8568801879883,187.2071151733398,187.2071151733398,187.5416259765625,187.8830795288086,187.8830795288086,188.2317657470703,188.2317657470703,188.5505447387695,188.9030227661133,189.0668411254883,189.0668411254883,189.0668411254883,186.5645904541016,186.5645904541016,186.8636169433594,186.8636169433594,187.2043991088867,187.5149536132812,187.5149536132812,187.5149536132812,187.8116836547852,187.8116836547852,187.8116836547852,188.1773452758789,188.5663986206055,188.5663986206055,188.9458236694336,188.9458236694336,189.1422882080078,189.1422882080078,189.1422882080078,186.6472930908203,186.6472930908203,186.9617462158203,187.3025360107422,187.3025360107422,187.6779327392578,187.9967727661133,188.2846755981445,188.2846755981445,188.5909957885742,188.9130783081055,188.9130783081055,189.216438293457,189.216438293457,189.216438293457,186.6724853515625,186.6724853515625,186.6724853515625,186.978515625,186.978515625,187.3101806640625,187.3101806640625,187.7183380126953,187.7183380126953,188.0836563110352,188.0836563110352,188.4420318603516,188.8044967651367,189.1810684204102,189.2893905639648,189.2893905639648,189.2893905639648,187.0082778930664,187.0082778930664,187.3456802368164,187.3456802368164,187.654167175293,187.654167175293,188.0075759887695,188.0075759887695,188.3752365112305,188.3752365112305,188.3752365112305,188.752685546875,188.752685546875,189.1331024169922,189.1331024169922,189.3612213134766,189.3612213134766,189.3612213134766,189.3612213134766,187.051513671875,187.051513671875,187.388427734375,187.388427734375,187.7443161010742,187.7443161010742,188.1113739013672,188.1113739013672,188.4976654052734,188.4976654052734,188.8852386474609,188.8852386474609,189.2809219360352,189.2809219360352,189.4318466186523,189.4318466186523,189.4318466186523,187.2382507324219,187.2382507324219,187.5844497680664,187.5844497680664,187.5844497680664,187.9430541992188,188.3104019165039,188.3104019165039,188.6915740966797,189.0795516967773,189.471321105957,187.1120452880859,187.1120452880859,187.1120452880859,187.4419784545898,187.8262557983398,187.8262557983398,188.1851806640625,188.5504150390625,188.5504150390625,188.9294357299805,188.9294357299805,189.3144302368164,189.3144302368164,189.5697326660156,189.5697326660156,187.3459320068359,187.3459320068359,187.6735610961914,187.6735610961914,188.018180847168,188.3786773681641,188.3786773681641,188.6862182617188,189.0146102905273,189.3722152709961,189.3722152709961,189.636962890625,189.636962890625,189.636962890625,187.4100341796875,187.7091598510742,187.7091598510742,188.0306167602539,188.3621063232422,188.3621063232422,188.6959915161133,189.0433578491211,189.4174728393555,189.4174728393555,189.7032012939453,189.7032012939453,187.505989074707,187.8068008422852,188.1322021484375,188.5260772705078,188.8139266967773,189.0515213012695,189.2657089233398,189.2657089233398,189.5600051879883,189.5600051879883,189.7682952880859,189.7682952880859,189.7682952880859,187.6058044433594,187.6058044433594,187.9127349853516,187.9127349853516,187.9127349853516,188.1102981567383,188.1102981567383,188.3198013305664,188.3198013305664,188.6444320678711,188.6444320678711,188.948356628418,188.948356628418,189.2624588012695,189.5098342895508,189.8324203491211,189.8324203491211,189.8324203491211,187.6441879272461,187.9708786010742,187.9708786010742,188.2988967895508,188.6260833740234,188.948860168457,189.2191925048828,189.2191925048828,189.507568359375,189.760009765625,189.8953704833984,189.8953704833984,189.8953704833984,189.8953704833984,187.8707275390625,187.8707275390625,188.0569305419922,188.0569305419922,188.2471618652344,188.2471618652344,188.4482345581055,188.4482345581055,188.7830276489258,188.7830276489258,189.1422424316406,189.1422424316406,189.3590316772461,189.6566162109375,189.936279296875,189.936279296875,189.9574584960938,189.9574584960938,187.9138870239258,187.9138870239258,188.2120513916016,188.4264297485352,188.4264297485352,188.6720809936523,188.6720809936523,188.9240798950195,188.9240798950195,189.2061309814453,189.5138397216797,189.7813262939453,189.7813262939453,190.0184097290039,190.0184097290039,190.0184097290039,190.0184097290039,190.0184097290039,190.0184097290039,190.0184097290039,190.0184097290039,190.0184097290039,190.0184097290039,190.0184097290039,190.0184097290039,190.0184097290039,190.0184097290039,190.0184097290039,190.0184097290039,190.0184097290039,190.0184097290039,188.0505065917969,188.3283309936523,188.3283309936523,188.5899658203125,188.5899658203125,188.8692092895508,188.8692092895508,189.1403350830078,189.4140243530273,189.4140243530273,189.4140243530273,189.6888122558594,189.6888122558594,189.8455657958984,190.0690765380859,190.0690765380859,190.0690765380859,190.0781936645508,190.0781936645508,190.0781936645508,188.0747909545898,188.0747909545898,188.3560791015625,188.5970458984375,188.5970458984375,188.7388610839844,188.9521713256836,189.2047119140625,189.2047119140625,189.2047119140625,189.4326248168945,189.5814437866211,189.5814437866211,189.7185287475586,189.7185287475586,189.8543090820312,189.8543090820312,190.0122375488281,190.0122375488281,190.1372222900391,190.1372222900391,190.1372222900391,188.15673828125,188.15673828125,188.3923721313477,188.3923721313477,188.62158203125,188.62158203125,188.62158203125,188.8486099243164,188.8486099243164,189.0752182006836,189.2829360961914,189.2829360961914,189.5141906738281,189.7119750976562,189.7119750976562,189.7119750976562,189.9046478271484,189.9046478271484,190.1111831665039,190.1111831665039,190.1111831665039,190.1954040527344,190.1954040527344,190.1954040527344,188.2262115478516,188.2262115478516,188.4816589355469,188.6980895996094,188.928596496582,188.928596496582,189.1561889648438,189.3848724365234,189.3848724365234,189.6080551147461,189.6080551147461,189.8207855224609,189.8207855224609,189.9786605834961,189.9786605834961,190.1501312255859,190.1501312255859,190.2525787353516,190.2525787353516,190.2525787353516,188.296257019043,188.296257019043,188.508056640625,188.508056640625,188.7254409790039,188.7254409790039,188.9540939331055,188.9540939331055,188.9540939331055,189.2049026489258,189.4459838867188,189.4459838867188,189.6497268676758,189.6497268676758,189.8485107421875,189.8485107421875,190.026969909668,190.026969909668,190.026969909668,190.2533493041992,190.2533493041992,190.3088150024414,190.3088150024414,188.3899841308594,188.3899841308594,188.5802307128906,188.7970504760742,188.7970504760742,189.0111999511719,189.2324752807617,189.4614181518555,189.4614181518555,189.710578918457,189.9406433105469,189.9406433105469,190.1640319824219,190.1640319824219,190.3642425537109,190.3642425537109,190.3642425537109,190.3642425537109,190.3642425537109,190.3642425537109,188.5905532836914,188.5905532836914,188.7887191772461,189.0092620849609,189.0092620849609,189.2461929321289,189.4826965332031,189.4826965332031,189.7077941894531,189.7077941894531,189.9299468994141,189.9299468994141,190.150520324707,190.363899230957,190.4186630249023,190.4186630249023,190.4186630249023,188.6084289550781,188.6084289550781,188.8076019287109,188.8076019287109,188.8076019287109,189.0452346801758,189.0452346801758,189.2952499389648,189.2952499389648,189.5403671264648,189.5403671264648,189.7890319824219,189.7890319824219,190.0436477661133,190.0436477661133,190.3007736206055,190.3007736206055,190.4722366333008,190.4722366333008,188.6613159179688,188.6613159179688,188.9023818969727,189.1763458251953,189.1763458251953,189.4321441650391,189.7038040161133,189.7038040161133,189.7038040161133,189.9472351074219,189.9472351074219,190.2147674560547,190.4817352294922,190.5250244140625,190.5250244140625,190.5250244140625,188.8483047485352,188.8483047485352,189.1057662963867,189.1057662963867,189.3734893798828,189.6563568115234,189.6563568115234,189.9409790039062,190.2256393432617,190.2256393432617,190.5083618164062,190.5768051147461,190.5768051147461,188.9548187255859,188.9548187255859,189.2177886962891,189.5047378540039,189.5047378540039,189.8378524780273,189.8378524780273,190.1365280151367,190.436393737793,190.436393737793,190.6279144287109,190.6279144287109,188.9375991821289,188.9375991821289,189.2012252807617,189.499870300293,189.499870300293,189.8125305175781,189.8125305175781,190.1283874511719,190.1283874511719,190.4418334960938,190.6781311035156,190.6781311035156,190.6781311035156,188.9863891601562,188.9863891601562,189.2511138916016,189.2511138916016,189.5509567260742,189.8772125244141,189.8772125244141,190.2042999267578,190.2042999267578,190.527702331543,190.527702331543,190.7275695800781,190.7275695800781,189.1098022460938,189.1098022460938,189.3795547485352,189.3795547485352,189.6899261474609,189.6899261474609,190.0271987915039,190.0271987915039,190.3679733276367,190.3679733276367,190.7031707763672,190.7031707763672,190.7761383056641,190.7761383056641,190.7761383056641,189.2967681884766,189.2967681884766,189.2967681884766,189.5799865722656,189.5799865722656,189.5799865722656,189.9085159301758,189.9085159301758,190.2555389404297,190.600700378418,190.600700378418,190.823974609375,190.823974609375,189.2788467407227,189.2788467407227,189.2788467407227,189.5496444702148,189.5496444702148,189.8605880737305,189.8605880737305,190.2084655761719,190.5628509521484,190.8710479736328,190.8710479736328,189.2541809082031,189.2541809082031,189.5051040649414,189.5051040649414,189.7975692749023,190.1353607177734,190.498664855957,190.8643112182617,190.8643112182617,190.8643112182617,190.9172973632812,190.9172973632812,190.9172973632812,189.5201110839844,189.5201110839844,189.8037338256836,189.8037338256836,190.1332702636719,190.1332702636719,190.4954299926758,190.4954299926758,190.8664169311523,190.9628753662109,190.9628753662109,190.9628753662109,189.5429534912109,189.5429534912109,189.8200531005859,189.8200531005859,189.8200531005859,190.1426239013672,190.1426239013672,190.4973831176758,190.4973831176758,190.8670959472656,190.8670959472656,191.0076675415039,191.0076675415039,191.0076675415039,189.5868377685547,189.8649139404297,189.8649139404297,190.1805801391602,190.1805801391602,190.5310668945312,190.5310668945312,190.8993301391602,191.0517120361328,191.0517120361328,189.6845169067383,189.9666061401367,189.9666061401367,190.2932205200195,190.6336059570312,190.6336059570312,190.9998245239258,190.9998245239258,190.9998245239258,191.095100402832,191.095100402832,191.095100402832,191.095100402832,191.095100402832,191.095100402832,191.095100402832,191.095100402832,191.095100402832,191.095100402832,191.095100402832,191.095100402832,191.095100402832,191.095100402832,191.095100402832,191.095100402832,191.095100402832,191.095100402832,191.095100402832,191.095100402832,191.095100402832,191.095100402832,191.095100402832,191.095100402832,191.095100402832,191.095100402832,191.095100402832,191.095100402832,191.095100402832,191.095100402832,191.095100402832,191.095100402832,191.095100402832,191.095100402832,191.095100402832,191.095100402832,191.095100402832,191.095100402832,191.095100402832,191.095100402832,191.095100402832,191.095100402832,191.095100402832,191.095100402832,191.095100402832,191.095100402832,191.095100402832,191.095100402832,191.095100402832,191.095100402832,191.095100402832,191.095100402832,191.095100402832,191.095100402832,191.095100402832,191.095100402832,191.095100402832,191.095100402832,191.095100402832,191.095100402832,191.095100402832,191.095100402832,191.095100402832,191.095100402832,191.095100402832,191.095100402832,191.095100402832,191.095100402832,191.095100402832,189.6020812988281,189.6020812988281,189.6020812988281,189.6168670654297,189.8659973144531,189.8659973144531,190.1309432983398,190.1309432983398,190.4253921508789,190.4253921508789,190.7477569580078,190.7477569580078,191.0639724731445,191.0639724731445,191.4126586914062,191.4126586914062,191.7876358032227,191.7876358032227,192.1981201171875,192.5666198730469,192.900749206543,193.235710144043,193.5722045898438,193.5722045898438,193.9070816040039,194.243049621582,194.243049621582,194.4392471313477,194.4392471313477,194.4392471313477,189.8911666870117,190.2294616699219,190.5856094360352,190.5856094360352,190.933952331543,190.933952331543,191.280143737793,191.280143737793,191.6992034912109,191.6992034912109,192.0922012329102,192.4993515014648,192.4993515014648,192.9110870361328,193.3257369995117,193.7399673461914,193.7399673461914,194.1587066650391,194.1587066650391,194.5582580566406,194.5582580566406,194.5715484619141,194.5715484619141,194.5715484619141,190.2431945800781,190.2431945800781,190.5751953125,190.5751953125,190.9546661376953,191.2893981933594,191.2893981933594,191.6607437133789,191.6607437133789,192.0466003417969,192.0466003417969,192.0466003417969,192.4431762695312,192.4431762695312,192.8437728881836,192.8437728881836,193.2558059692383,193.2558059692383,193.661491394043,193.661491394043,193.661491394043,194.0678253173828,194.4741287231445,194.4741287231445,194.4741287231445,194.7017059326172,194.7017059326172,194.7017059326172,190.2697830200195,190.5727081298828,190.5727081298828,190.8943176269531,190.8943176269531,191.2140960693359,191.5607833862305,191.5607833862305,191.5607833862305,191.9259262084961,191.9259262084961,192.3069229125977,192.3069229125977,192.6971588134766,192.6971588134766,193.0975952148438,193.0975952148438,193.5066146850586,193.9205932617188,193.9205932617188,193.9205932617188,194.335563659668,194.335563659668,194.7298583984375,194.8297653198242,194.8297653198242,194.8297653198242,190.5262680053711,190.5262680053711,190.8272476196289,190.8272476196289,191.1464004516602,191.1464004516602,191.4621124267578,191.4621124267578,191.4621124267578,191.8218765258789,191.8218765258789,192.1876983642578,192.1876983642578,192.5707550048828,192.5707550048828,192.9574890136719,192.9574890136719,193.3539276123047,193.3539276123047,193.7490615844727,193.7490615844727,194.2029724121094,194.6119155883789,194.6119155883789,194.6119155883789,194.9558258056641,194.9558258056641,194.9558258056641,194.9558258056641,194.9558258056641,194.9558258056641,190.85498046875,191.1671295166016,191.1671295166016,191.4771575927734,191.4771575927734,191.8304290771484,192.1972503662109,192.5797119140625,192.9731063842773,192.9731063842773,193.369987487793,193.369987487793,193.7718963623047,194.177001953125,194.177001953125,194.5904235839844,194.5904235839844,194.9889831542969,194.9889831542969,195.079719543457,195.079719543457,190.9167556762695,191.1889877319336,191.4735641479492,191.4735641479492,191.7782363891602,192.1301879882812,192.1301879882812,192.4861068725586,192.8519287109375,192.8519287109375,192.8519287109375,193.234130859375,193.234130859375,193.6185607910156,193.6185607910156,194.0136108398438,194.0136108398438,194.4131164550781,194.4131164550781,194.8298873901367,194.8298873901367,195.2017211914062,195.2017211914062,195.2017211914062,195.2017211914062,195.2017211914062,195.2017211914062,191.2101135253906,191.2101135253906,191.5079116821289,191.5079116821289,191.8049774169922,192.1860122680664,192.5442733764648,192.5442733764648,192.905632019043,192.905632019043,193.2798538208008,193.2798538208008,193.669807434082,193.669807434082,194.05517578125,194.4591217041016,194.4591217041016,194.8570327758789,194.8570327758789,195.2570114135742,195.3217086791992,195.3217086791992,195.3217086791992,191.3170166015625,191.3170166015625,191.6077728271484,191.6077728271484,191.8957595825195,191.8957595825195,192.2407455444336,192.5997009277344,192.5997009277344,192.9585494995117,193.3257141113281,193.7057647705078,193.7057647705078,194.0973892211914,194.0973892211914,194.4788970947266,194.4788970947266,194.4788970947266,194.8691329956055,194.8691329956055,195.2594604492188,195.2594604492188,195.4397811889648,195.4397811889648,191.4165878295898,191.4165878295898,191.6937408447266,191.974967956543,191.974967956543,192.3053970336914,192.3053970336914,192.6595001220703,192.6595001220703,193.0168228149414,193.3829956054688,193.3829956054688,193.3829956054688,193.7643585205078,194.1529769897461,194.1529769897461,194.5723495483398,194.9682312011719,194.9682312011719,195.3672714233398,195.3672714233398,195.555908203125,195.555908203125,195.555908203125,191.5878219604492,191.5878219604492,191.5878219604492,191.8650817871094,191.8650817871094,192.1475524902344,192.1475524902344,192.4790954589844,192.8296508789062,192.8296508789062,193.1862640380859,193.1862640380859,193.5583801269531,193.9403915405273,193.9403915405273,194.3340377807617,194.3340377807617,194.7233657836914,194.7233657836914,195.1178894042969,195.1178894042969,195.5220108032227,195.5220108032227,195.6702346801758,195.6702346801758,195.6702346801758,191.7920761108398,191.7920761108398,192.0617599487305,192.0617599487305,192.3467178344727,192.3467178344727,192.679084777832,192.679084777832,193.025634765625,193.025634765625,193.3777084350586,193.7331924438477,193.7331924438477,194.1090240478516,194.4996490478516,194.4996490478516,194.8909454345703,194.8909454345703,195.2933349609375,195.2933349609375,195.2933349609375,195.6895599365234,195.6895599365234,195.7826080322266,195.7826080322266,192.0123825073242,192.2999877929688,192.2999877929688,192.5937347412109,192.5937347412109,192.9267883300781,193.2802124023438,193.2802124023438,193.6366195678711,193.6366195678711,194.0082702636719,194.0082702636719,194.0082702636719,194.3915557861328,194.7860260009766,195.1855850219727,195.58740234375,195.58740234375,195.8932800292969,195.8932800292969,195.8932800292969,195.8932800292969,192.2989883422852,192.5712738037109,192.5712738037109,192.8895721435547,193.2321624755859,193.2321624755859,193.5872802734375,193.5872802734375,193.9526214599609,193.9526214599609,194.3313522338867,194.7208862304688,194.7208862304688,195.1255035400391,195.1255035400391,195.5303802490234,195.5303802490234,195.9329223632812,196.0021209716797,196.0021209716797,192.3795318603516,192.6425704956055,192.9446716308594,192.9446716308594,193.2799606323242,193.6271667480469,193.9864730834961,193.9864730834961,194.3583450317383,194.3583450317383,194.7450561523438,194.7450561523438,195.1119766235352,195.557861328125,195.9677734375,195.9677734375,196.1092224121094,196.1092224121094,196.1092224121094,192.4875183105469,192.4875183105469,192.7469253540039,193.042366027832,193.042366027832,193.370491027832,193.7130355834961,193.7130355834961,194.0690841674805,194.0690841674805,194.424446105957,194.424446105957,194.8041915893555,194.8041915893555,195.1944580078125,195.5971069335938,196.000244140625,196.000244140625,196.2146072387695,196.2146072387695,192.5965576171875,192.5965576171875,192.8530960083008,192.8530960083008,193.1326446533203,193.1326446533203,193.1326446533203,193.4464111328125,193.4464111328125,193.7820587158203,194.1393280029297,194.1393280029297,194.5060729980469,194.5060729980469,194.8865737915039,194.8865737915039,195.2801361083984,195.2801361083984,195.6800079345703,196.0846557617188,196.0846557617188,196.3182373046875,196.3182373046875,196.3182373046875,196.3182373046875,196.3182373046875,196.3182373046875,193.0050735473633,193.0050735473633,193.2852630615234,193.5955810546875,193.5955810546875,193.931266784668,193.931266784668,194.3232498168945,194.3232498168945,194.6883850097656,195.0681838989258,195.0681838989258,195.4656219482422,195.4656219482422,195.8676147460938,196.2696990966797,196.4202499389648,196.4202499389648,196.4202499389648,192.9510803222656,192.9510803222656,192.9510803222656,193.2027130126953,193.2027130126953,193.2027130126953,193.4857330322266,193.794921875,193.794921875,194.1325378417969,194.1325378417969,194.4857711791992,194.4857711791992,194.8521881103516,194.8521881103516,195.2315673828125,195.2315673828125,195.6297378540039,195.6297378540039,196.0355758666992,196.4346771240234,196.5206069946289,196.5206069946289,196.5206069946289,193.128303527832,193.128303527832,193.128303527832,193.4018936157227,193.4018936157227,193.7037353515625,194.0288848876953,194.0288848876953,194.3715515136719,194.3715515136719,194.3715515136719,194.7288665771484,194.7288665771484,195.0903472900391,195.0903472900391,195.46826171875,195.46826171875,195.8550643920898,195.8550643920898,196.2492523193359,196.6192626953125,196.6192626953125,196.6192626953125,196.6192626953125,196.6192626953125,196.6192626953125,193.3634262084961,193.3634262084961,193.6206665039062,193.6206665039062,193.9065170288086,194.2256546020508,194.5729751586914,194.9300689697266,194.9300689697266,195.3010406494141,195.3010406494141,195.6843032836914,195.6843032836914,195.6843032836914,196.0802001953125,196.0802001953125,196.4811172485352,196.4811172485352,196.7164306640625,196.7164306640625,196.7164306640625,196.7164306640625,196.7164306640625,196.7164306640625,196.7164306640625,196.7164306640625,196.7164306640625,196.7164306640625,196.7164306640625,196.7164306640625,196.7164306640625,196.7164306640625,196.7164306640625,196.7164306640625,196.7164306640625,196.7164306640625,196.7164306640625,196.7164306640625,196.7164306640625,196.7164306640625,196.7164306640625,196.7164306640625,196.7164306640625,196.7164306640625,196.7164306640625,196.7164306640625,196.7164306640625,196.7164306640625,196.7164306640625,196.7164306640625,196.7164306640625,196.7164306640625,196.7164306640625,196.7164306640625,193.3930740356445,193.3930740356445,193.5723876953125,193.5723876953125,193.790168762207,193.790168762207,194.0249786376953,194.0249786376953,194.2774505615234,194.2774505615234,194.5664749145508,194.5664749145508,194.9236221313477,194.9236221313477,195.2647323608398,195.2647323608398,195.6172332763672,195.6172332763672,195.6172332763672,195.9864730834961,195.9864730834961,196.3780975341797,196.3780975341797,196.7723693847656,196.7723693847656,196.8116455078125,196.8116455078125,193.627799987793,193.627799987793,193.8806457519531,193.8806457519531,193.8806457519531,194.1626358032227,194.1626358032227,194.474609375,194.8145217895508,194.8145217895508,195.1728668212891,195.1728668212891,195.5448608398438,195.5448608398438,195.928955078125,195.928955078125,196.327522277832,196.327522277832,196.7291946411133,196.9056777954102,196.9056777954102,196.9056777954102,193.6839981079102,193.6839981079102,193.929328918457,193.929328918457,194.197509765625,194.4673385620117,194.4673385620117,194.7958145141602,195.1508178710938,195.1508178710938,195.5161972045898,195.5161972045898,195.9028472900391,196.3000106811523,196.3000106811523,196.7076263427734,196.7076263427734,196.9982376098633,196.9982376098633,196.9982376098633,196.9982376098633,196.9982376098633,196.9982376098633,194.0012817382812,194.0012817382812,194.2901153564453,194.2901153564453,194.5799865722656,194.5799865722656,194.9040908813477,195.2589263916016,195.2589263916016,195.2589263916016,195.6106109619141,195.6106109619141,195.980339050293,195.980339050293,196.3661575317383,196.3661575317383,196.7644882202148,196.7644882202148,197.0892944335938,197.0892944335938,197.0892944335938,197.0892944335938,197.0892944335938,197.0892944335938,194.1241302490234,194.3780136108398,194.3780136108398,194.6598281860352,194.6598281860352,194.6598281860352,194.9796981811523,194.9796981811523,195.3298263549805,195.3298263549805,195.6875991821289,195.6875991821289,196.061164855957,196.061164855957,196.4508743286133,196.851676940918,196.851676940918,197.1787872314453,197.1787872314453,197.1787872314453,197.1787872314453,197.1787872314453,197.1787872314453,197.1787872314453,197.1787872314453,194.2505493164062,194.2505493164062,194.5014724731445,194.5014724731445,194.7790832519531,195.0954055786133,195.0954055786133,195.4437866210938,195.8017272949219,195.8017272949219,196.1681289672852,196.1681289672852,196.5506896972656,196.9482498168945,197.2669372558594,197.2669372558594,197.2669372558594,197.2669372558594,197.2669372558594,197.2669372558594,194.4263610839844,194.6832046508789,194.6832046508789,194.6832046508789,194.9678573608398,194.9678573608398,195.2914505004883,195.6385498046875,195.9928283691406,195.9928283691406,196.3631896972656,196.3631896972656,196.7473754882812,197.1416931152344,197.3535995483398,197.3535995483398,197.3535995483398,197.3535995483398,197.3535995483398,197.3535995483398,194.5777587890625,194.5777587890625,194.8324127197266,194.8324127197266,195.1190719604492,195.1190719604492,195.443229675293,195.443229675293,195.7936401367188,195.7936401367188,196.1538696289062,196.1538696289062,196.5236511230469,196.8793258666992,196.8793258666992,197.2571105957031,197.2571105957031,197.2571105957031,197.4388809204102,197.4388809204102,197.4388809204102,194.5053787231445,194.5053787231445,194.7315902709961,194.7315902709961,194.7315902709961,195.0156936645508,195.0156936645508,195.309944152832,195.309944152832,195.6312942504883,195.9882049560547,195.9882049560547,196.3402709960938,196.6954803466797,196.6954803466797,197.0715713500977,197.0715713500977,197.4570465087891,197.5227432250977,197.5227432250977,194.6851654052734,194.6851654052734,194.9224014282227,194.9224014282227,195.1823196411133,195.1823196411133,195.4723281860352,195.7994918823242,196.1469268798828,196.1469268798828,196.4987564086914,196.4987564086914,196.8640975952148,197.2490921020508,197.2490921020508,197.6053085327148,197.6053085327148,197.6053085327148,197.6053085327148,194.8523635864258,194.8523635864258,195.0866317749023,195.0866317749023,195.0866317749023,195.3512649536133,195.3512649536133,195.6500930786133,195.6500930786133,195.6500930786133,195.9841690063477,196.3344192504883,196.722412109375,196.722412109375,197.0988540649414,197.0988540649414,197.4794311523438,197.4794311523438,197.4794311523438,197.6865310668945,197.6865310668945,197.6865310668945,197.6865310668945,195.0861053466797,195.0861053466797,195.3380737304688,195.3380737304688,195.6225204467773,195.6225204467773,195.941162109375,196.2864990234375,196.2864990234375,196.6420135498047,196.6420135498047,197.0122680664062,197.3984909057617,197.766471862793,197.766471862793,197.766471862793,197.766471862793,197.766471862793,197.766471862793,195.1299667358398,195.1299667358398,195.3738555908203,195.3738555908203,195.6457977294922,195.9548416137695,196.2982788085938,196.2982788085938,196.2982788085938,196.6504287719727,197.0110931396484,197.0110931396484,197.3750381469727,197.6699447631836,197.6699447631836,197.8450698852539,197.8450698852539,197.8450698852539,197.8450698852539,197.8450698852539,197.8450698852539,195.2973556518555,195.2973556518555,195.5383071899414,195.5383071899414,195.8081665039062,196.1128158569336,196.1128158569336,196.4514617919922,196.4514617919922,196.7971649169922,196.7971649169922,197.155143737793,197.155143737793,197.5273742675781,197.9034271240234,197.9224319458008,197.9224319458008,195.3147430419922,195.3147430419922,195.5530395507812,195.5530395507812,195.8222045898438,195.8222045898438,196.1017532348633,196.1017532348633,196.4546890258789,196.7855682373047,196.7855682373047,197.1302261352539,197.1302261352539,197.4778900146484,197.8567657470703,197.99853515625,197.99853515625,197.99853515625,197.99853515625,195.6152801513672,195.6152801513672,195.9012069702148,196.2084579467773,196.5510940551758,196.5510940551758,196.9080276489258,196.9080276489258,197.2693710327148,197.2693710327148,197.553092956543,197.553092956543,197.8889236450195,197.8889236450195,198.0735244750977,198.0735244750977,198.0735244750977,198.0735244750977,198.0735244750977,198.0735244750977,195.6528701782227,195.9108657836914,195.9108657836914,196.1758270263672,196.1758270263672,196.4837493896484,196.8129577636719,196.8129577636719,197.1576156616211,197.1576156616211,197.5199356079102,197.5199356079102,197.8995590209961,197.8995590209961,198.1471176147461,198.1471176147461,198.1471176147461,198.1471176147461,198.1471176147461,198.1471176147461,198.1471176147461,198.1471176147461,195.7562561035156,195.7562561035156,195.9924545288086,195.9924545288086,196.2615814208984,196.2615814208984,196.5365829467773,196.5365829467773,196.8661041259766,196.8661041259766,196.8661041259766,197.212646484375,197.212646484375,197.5706176757812,197.5706176757812,197.9496459960938,198.2196044921875,198.2196044921875,198.2196044921875,198.2196044921875,195.8665542602539,195.8665542602539,195.8665542602539,196.1307907104492,196.1307907104492,196.4099731445312,196.7303924560547,196.7303924560547,197.0813598632812,197.0813598632812,197.4372100830078,197.4372100830078,197.8007507324219,198.1795425415039,198.2909240722656,198.2909240722656,198.2909240722656,195.854850769043,195.854850769043,195.854850769043,196.0793075561523,196.0793075561523,196.3316650390625,196.6214981079102,196.6214981079102,196.9506759643555,196.9506759643555,197.3058395385742,197.3058395385742,197.6595001220703,198.0344161987305,198.3610458374023,198.3610458374023,198.3610458374023,198.3610458374023,196.0436401367188,196.0436401367188,196.2852249145508,196.5574493408203,196.5574493408203,196.8650436401367,196.8650436401367,197.2083435058594,197.5578231811523,197.5578231811523,197.9143905639648,198.2889862060547,198.4301147460938,198.4301147460938,198.4301147460938,198.4301147460938,198.4301147460938,198.4301147460938,198.4301147460938,198.4301147460938,198.4301147460938,198.4301147460938,198.4301147460938,198.4301147460938,198.4301147460938,198.4301147460938,198.4301147460938,198.4301147460938,198.4301147460938,198.4301147460938,198.4301147460938,198.4301147460938,198.4301147460938,198.4301147460938,198.4301147460938,198.4301147460938,198.4301147460938,198.4301147460938,198.4301147460938,198.4301147460938,198.4301147460938,198.4301147460938,196.0540466308594,196.0540466308594,196.0540466308594,196.1395721435547,196.3529052734375,196.3529052734375,196.5883712768555,196.5883712768555,196.8469161987305,197.143669128418,197.4729461669922,197.8114929199219,197.8114929199219,198.1652755737305,198.4977416992188,198.4977416992188,198.4977416992188,198.4977416992188,198.4977416992188,198.4977416992188,196.2693557739258,196.2693557739258,196.2693557739258,196.5011596679688,196.5011596679688,196.5011596679688,196.7702026367188,196.7702026367188,197.0772247314453,197.0772247314453,197.4143524169922,197.4143524169922,197.7653350830078,198.1235885620117,198.1235885620117,198.4977188110352,198.4977188110352,198.564582824707,198.564582824707,198.564582824707,196.3057022094727,196.3057022094727,196.5305252075195,196.5305252075195,196.7819442749023,196.7819442749023,197.0727005004883,197.0727005004883,197.4010162353516,197.4010162353516,197.7528533935547,197.7528533935547,198.1138305664062,198.1138305664062,198.4850921630859,198.4850921630859,198.6303863525391,198.6303863525391,198.6303863525391,198.6303863525391,198.6303863525391,198.6303863525391,196.5660400390625,196.5660400390625,196.8162612915039,196.8162612915039,197.1037139892578,197.1037139892578,197.4295501708984,197.4295501708984,197.7746505737305,198.1284561157227,198.1284561157227,198.501708984375,198.501708984375,198.695068359375,198.695068359375,198.695068359375,198.695068359375,198.695068359375,198.695068359375,196.6624145507812,196.6624145507812,196.9117050170898,197.2005615234375,197.2005615234375,197.5320434570312,197.5320434570312,197.5320434570312,197.8868408203125,197.8868408203125,198.238883972168,198.238883972168,198.595458984375,198.595458984375,198.7587661743164,198.7587661743164,198.7587661743164,198.7587661743164,196.7393188476562,196.981559753418,196.981559753418,196.981559753418,197.2589492797852,197.5788421630859,197.5788421630859,197.931396484375,197.931396484375,197.931396484375,198.2923431396484,198.2923431396484,198.6655654907227,198.6655654907227,198.821403503418,198.821403503418,198.821403503418,198.821403503418,198.821403503418,198.821403503418,196.8665161132812,196.8665161132812,197.103759765625,197.103759765625,197.3728179931641,197.6814346313477,197.6814346313477,198.0058898925781,198.0058898925781,198.0058898925781,198.3492736816406,198.3492736816406,198.7034530639648,198.8830795288086,198.8830795288086,198.8830795288086,198.8830795288086,198.8830795288086,198.8830795288086,196.9007186889648,197.1026840209961,197.1026840209961,197.313720703125,197.313720703125,197.472541809082,197.472541809082,197.7566452026367,197.7566452026367,198.0037078857422,198.0037078857422,198.2890930175781,198.599609375,198.8651428222656,198.8651428222656,198.9436874389648,198.9436874389648,198.9436874389648,198.9436874389648,196.8959197998047,196.8959197998047,197.1196517944336,197.1196517944336,197.1196517944336,197.3629150390625,197.6220397949219,197.6220397949219,197.9164657592773,197.9164657592773,198.2306365966797,198.5573196411133,198.5573196411133,198.7866668701172,198.7866668701172,199.0033798217773,199.0033798217773,199.0033798217773,199.0033798217773,199.0033798217773,199.0033798217773,197.0246963500977,197.0246963500977,197.2565612792969,197.5228576660156,197.8139724731445,197.8139724731445,198.1526641845703,198.1526641845703,198.1526641845703,198.5357055664062,198.5357055664062,198.8747406005859,198.8747406005859,199.0620880126953,199.0620880126953,199.0620880126953,199.0620880126953,197.1688766479492,197.1688766479492,197.4257125854492,197.7150115966797,197.7150115966797,198.0318222045898,198.3682403564453,198.7146301269531,198.7146301269531,199.068603515625,199.068603515625,199.1198272705078,199.1198272705078,199.1198272705078,197.1486587524414,197.1486587524414,197.365234375,197.365234375,197.6115417480469,197.6115417480469,197.8991622924805,197.8991622924805,198.2246856689453,198.2246856689453,198.5815963745117,198.5815963745117,198.9441070556641,199.1766510009766,199.1766510009766,199.1766510009766,199.1766510009766,199.1766510009766,199.1766510009766,199.1766510009766,199.1766510009766,197.3456497192383,197.3456497192383,197.3456497192383,197.5755233764648,197.5755233764648,197.5755233764648,197.8605422973633,198.1489791870117,198.1489791870117,198.4722518920898,198.4722518920898,198.8232650756836,199.1839752197266,199.1839752197266,199.232536315918,199.232536315918,199.232536315918,197.335205078125,197.5649337768555,197.5649337768555,197.8177795410156,197.8177795410156,198.1147384643555,198.1147384643555,198.4221725463867,198.4221725463867,198.7700729370117,198.7700729370117,199.1331329345703,199.1331329345703,199.2874984741211,199.2874984741211,199.2874984741211,199.2874984741211,197.5765991210938,197.81982421875,197.81982421875,198.101448059082,198.101448059082,198.4257278442383,198.4257278442383,198.7802047729492,198.7802047729492,199.118537902832,199.118537902832,199.118537902832,199.3415756225586,199.3415756225586,199.3415756225586,199.3415756225586,199.3415756225586,199.3415756225586,199.3415756225586,199.3415756225586,199.3415756225586,199.3415756225586,199.3415756225586,199.3415756225586,199.3415756225586,199.3415756225586,199.3415756225586,199.3415756225586,199.3415756225586,199.3415756225586,197.4879989624023,197.4879989624023,197.6793212890625,197.8970794677734,197.8970794677734,198.1028442382812,198.3355941772461,198.6191558837891,198.6191558837891,198.9412689208984,198.9412689208984,199.2863311767578,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,199.394416809082,197.5627593994141,197.5627593994141,197.5627593994141,197.5627593994141,197.6260604858398,197.6260604858398,197.6260604858398,197.8722305297852,197.8722305297852,198.1284790039062,198.1284790039062,198.4197311401367,198.4197311401367,198.7419586181641,199.0630874633789,199.3610458374023,199.7409210205078,199.7409210205078,200.1202774047852,200.1202774047852,200.1202774047852,200.5140228271484,200.5140228271484,200.9183197021484,201.3231430053711,201.6655197143555,201.6655197143555,201.9954299926758,201.9954299926758,201.9954299926758,202.3242568969727,202.3242568969727,202.6468276977539,202.9814147949219,202.9814147949219,203.3087997436523,203.6415328979492,203.9713287353516,204.3048477172852,204.3048477172852,204.6386032104492,204.6386032104492,204.9697113037109,205.1748886108398,205.1748886108398,205.1748886108398,205.1748886108398,205.1748886108398,205.1748886108398,197.9609680175781,197.9609680175781,198.2227325439453,198.5160369873047,198.5160369873047,198.8450393676758,198.8450393676758,199.1817855834961,199.1817855834961,199.1817855834961,199.4955978393555,199.8514175415039,199.8514175415039,200.2081146240234,200.2081146240234,200.5785446166992,200.9692230224609,201.354377746582,201.354377746582,201.7034149169922,202.0856018066406,202.4522933959961,202.4522933959961,202.8243103027344,202.8243103027344,203.2098770141602,203.573600769043,203.573600769043,203.9500045776367,203.9500045776367,204.3362655639648,204.7028884887695,205.0584487915039,205.3830947875977,205.3830947875977,205.3830947875977,205.3830947875977,205.3830947875977,205.3830947875977,205.3830947875977,205.3830947875977,205.3830947875977,198.4083251953125,198.4083251953125,198.6698989868164,198.9537658691406,199.2621917724609,199.2621917724609,199.5677490234375,199.8846130371094,199.8846130371094,199.8846130371094,200.2239761352539,200.2239761352539,200.5726470947266,200.5726470947266,200.939567565918,200.939567565918,201.2973480224609,201.2973480224609,201.6830825805664,201.6830825805664,202.0733032226562,202.0733032226562,202.4634628295898,202.8570404052734,202.8570404052734,203.2591705322266,203.2591705322266,203.658576965332,203.658576965332,204.098876953125,204.098876953125,204.4994354248047,204.9037322998047,204.9037322998047,205.2899703979492,205.2899703979492,205.5879287719727,205.5879287719727,205.5879287719727,205.5879287719727,205.5879287719727,205.5879287719727,205.5879287719727,205.5879287719727,205.5879287719727,198.7591781616211,198.7591781616211,199.0150299072266,199.297721862793,199.5891418457031,199.5891418457031,199.8865661621094,199.8865661621094,200.2267990112305,200.2267990112305,200.5801086425781,200.945442199707,201.3237152099609,201.3237152099609,201.7118759155273,201.7118759155273,202.1030807495117,202.497314453125,202.497314453125,202.9033813476562,202.9033813476562,203.2872772216797,203.6790084838867,204.0729064941406,204.0729064941406,204.0729064941406,204.4514541625977,204.7348022460938,204.7348022460938,205.0997695922852,205.4679870605469,205.7894134521484,205.7894134521484,205.7894134521484,205.7894134521484,205.7894134521484,205.7894134521484,205.7894134521484,205.7894134521484,205.7894134521484,199.0215835571289,199.0215835571289,199.2584915161133,199.2584915161133,199.2584915161133,199.5127487182617,199.5127487182617,199.5127487182617,199.7866592407227,199.7866592407227,200.0647888183594,200.0647888183594,200.3908233642578,200.3908233642578,200.7323455810547,200.7323455810547,201.0823822021484,201.0823822021484,201.4454879760742,201.8240966796875,202.2148818969727,202.6052169799805,202.9997863769531,202.9997863769531,203.400276184082,203.400276184082,203.7990798950195,203.7990798950195,204.1997146606445,204.1997146606445,204.1997146606445,204.601203918457,204.601203918457,204.601203918457,205.0031127929688,205.4069671630859,205.4069671630859,205.7990570068359,205.9877471923828,205.9877471923828,205.9877471923828,205.9877471923828,199.2285308837891,199.4746475219727,199.7334976196289,199.7334976196289,200.006217956543,200.006217956543,200.2892227172852,200.2892227172852,200.6189422607422,200.6189422607422,200.9624099731445,201.3183746337891,201.3183746337891,201.6823272705078,201.6823272705078,202.068733215332,202.068733215332,202.068733215332,202.465705871582,202.8554077148438,202.8554077148438,203.2597045898438,203.2597045898438,203.2597045898438,203.6601181030273,203.6601181030273,204.0603637695312,204.0603637695312,204.4632568359375,204.4632568359375,204.8640594482422,204.8640594482422,205.2706909179688,205.6743927001953,205.6743927001953,206.0673522949219,206.0673522949219,206.1827926635742,206.1827926635742,206.1827926635742,206.1827926635742,206.1827926635742,206.1827926635742,199.5265808105469,199.5265808105469,199.5265808105469,199.7715225219727,199.7715225219727,200.0266876220703,200.0266876220703,200.2939147949219,200.2939147949219,200.6174926757812,200.6174926757812,200.9578704833984,201.3101196289062,201.3101196289062,201.6702270507812,201.6702270507812,202.0486907958984,202.0486907958984,202.4288024902344,202.4288024902344,202.8074493408203,202.8074493408203,203.1889419555664,203.1889419555664,203.1889419555664,203.5724029541016,203.9535446166992,204.3423385620117,204.3423385620117,204.7324752807617,205.1282806396484,205.5329513549805,205.5329513549805,205.5329513549805,205.9318389892578,205.9318389892578,206.3196563720703,206.374755859375,206.374755859375,206.374755859375,206.374755859375,206.374755859375,206.374755859375,206.374755859375,206.374755859375,206.374755859375,206.374755859375,206.374755859375,206.374755859375,206.374755859375,206.374755859375,199.7782974243164,199.9799194335938,199.9799194335938,200.2140045166016,200.2140045166016,200.4514846801758,200.4514846801758,200.701545715332,201.0029830932617,201.0029830932617,201.3295745849609,201.6703033447266,201.6703033447266,202.0223388671875,202.0223388671875,202.3933715820312,202.7759552001953,203.1656875610352,203.1656875610352,203.5568618774414,203.5568618774414,203.9509429931641,203.9509429931641,204.3507461547852,204.7633972167969,205.1635360717773,205.1635360717773,205.567268371582,205.567268371582,205.9698638916016,206.3593826293945,206.3593826293945,206.5634994506836,206.5634994506836,206.5634994506836,206.5634994506836,200.0869979858398,200.0869979858398,200.329345703125,200.329345703125,200.329345703125,200.5820846557617,200.8414306640625,200.8414306640625,201.1428909301758,201.1428909301758,201.4805145263672,201.8279113769531,201.8279113769531,201.8279113769531,202.1843566894531,202.5571670532227,202.9788513183594,202.9788513183594,203.3696212768555,203.7663879394531,203.7663879394531,204.1618957519531,204.5660171508789,204.5660171508789,204.9713745117188,204.9713745117188,205.3788528442383,205.3788528442383,205.7868957519531,206.1994781494141,206.5930099487305,206.7493057250977,206.7493057250977,206.7493057250977,206.7493057250977,206.7493057250977,206.7493057250977,200.4047546386719,200.4047546386719,200.648551940918,200.8941650390625,200.8941650390625,200.8941650390625,201.1533203125,201.1533203125,201.462158203125,201.799072265625,202.1478118896484,202.5018768310547,202.5018768310547,202.5018768310547,202.8707580566406,202.8707580566406,203.2523880004883,203.2523880004883,203.2523880004883,203.6377105712891,204.0336608886719,204.4302139282227,204.4302139282227,204.8367538452148,204.8367538452148,205.2458419799805,205.655158996582,206.0661849975586,206.0661849975586,206.4757614135742,206.8712310791016,206.8712310791016,206.9321060180664,206.9321060180664,206.9321060180664,206.9321060180664,206.9321060180664,206.9321060180664,200.7467727661133,201.0124053955078,201.0124053955078,201.2516174316406,201.5266952514648,201.5266952514648,201.8397674560547,201.8397674560547,201.8397674560547,202.176155090332,202.176155090332,202.5209655761719,202.5209655761719,202.8726119995117,202.8726119995117,203.2346038818359,203.6115951538086,203.6115951538086,203.9996795654297,203.9996795654297,204.3966064453125,204.3966064453125,212.073112487793,212.073112487793,212.073112487793,212.073112487793,212.073112487793,212.073112487793,212.073112487793,212.073112487793,212.073112487793,212.073112487793,212.073112487793,212.073112487793,212.073112487793,212.073112487793,212.073112487793,212.073112487793,212.073112487793,212.073112487793,219.702507019043,219.7025146484375,219.7025146484375,219.7025146484375,219.7025146484375,219.7025146484375,219.7025146484375,219.7025146484375,219.7025146484375,219.7025146484375,219.7025146484375,219.7025146484375,219.7025146484375,219.7025146484375,219.7025146484375,219.7025146484375,219.7025146484375,219.7025146484375,219.7025146484375,219.7025146484375,219.7025146484375,234.9613037109375,234.9613037109375,234.9613037109375,234.9613037109375,234.9613037109375,234.9613037109375,234.9613037109375,234.9613037109375,234.9613037109375,234.9613037109375,234.9613037109375,234.9613037109375,234.9613037109375,234.9613037109375,234.9613037109375,234.9613037109375,234.9613037109375,234.9613037109375,242.6285171508789,242.6285171508789,242.6285171508789,242.6285171508789,242.6285171508789,242.6285171508789,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953,257.9859161376953],"meminc":[0,0,0,0,15.28223419189453,0,0,0,30.46574401855469,0,0,0,0,0,0,0,0,0,4.57763671875e-05,0,0,0,0,0,0,0,0,0,0,0,0,0,-0.00030517578125,0,15.44046783447266,0,0.2632064819335938,0,0.2960128784179688,0,0.335540771484375,0,0,0.3636245727539062,0.3673782348632812,0,0.392364501953125,0,0.4089889526367188,0.4133453369140625,0,-2.843917846679688,0,0.3809585571289062,0,0.3092117309570312,0,0,0.30462646484375,0,0,0.4010009765625,0,0.396392822265625,0,0.4112319946289062,0.4138412475585938,0,0.3316268920898438,0,0,-2.691650390625,0.3686065673828125,0,0.3753433227539062,0.3902969360351562,0,0,0.368499755859375,0,0.2831954956054688,0,0.3979644775390625,0.4029159545898438,0,0.1865463256835938,0,0,0,-2.553779602050781,0.2691802978515625,0.2787857055664062,0,0.3798828125,0,0.3855209350585938,0,0.38690185546875,0,0.3965911865234375,0,0.3995819091796875,0,0.1378326416015625,0,-2.464149475097656,0,0.3621673583984375,0.3785552978515625,0,0.3674545288085938,0,0.3639450073242188,0,0.3525238037109375,0,0.37762451171875,0,0.341064453125,0,0,-2.626213073730469,0,0.3487396240234375,0.37481689453125,0.3698348999023438,0.3806076049804688,0,0.361724853515625,0,0.3707122802734375,0,0.4143142700195312,0,0.08335113525390625,0,0,-2.496070861816406,0,0.3627395629882812,0,0.3502349853515625,0,0.3345108032226562,0.3414535522460938,0,0.3486862182617188,0,0.3187789916992188,0.35247802734375,0.163818359375,0,0,-2.502250671386719,0,0.2990264892578125,0,0.3407821655273438,0.3105545043945312,0,0,0.2967300415039062,0,0,0.36566162109375,0.3890533447265625,0,0.379425048828125,0,0.1964645385742188,0,0,-2.4949951171875,0,0.314453125,0.340789794921875,0,0.375396728515625,0.3188400268554688,0.28790283203125,0,0.3063201904296875,0.32208251953125,0,0.3033599853515625,0,0,-2.543952941894531,0,0,0.3060302734375,0,0.3316650390625,0,0.4081573486328125,0,0.3653182983398438,0,0.3583755493164062,0.3624649047851562,0.3765716552734375,0.1083221435546875,0,0,-2.281112670898438,0,0.33740234375,0,0.3084869384765625,0,0.3534088134765625,0,0.3676605224609375,0,0,0.3774490356445312,0,0.3804168701171875,0,0.228118896484375,0,0,0,-2.309707641601562,0,0.3369140625,0,0.3558883666992188,0,0.3670578002929688,0,0.38629150390625,0,0.3875732421875,0,0.3956832885742188,0,0.1509246826171875,0,0,-2.193595886230469,0,0.3461990356445312,0,0,0.3586044311523438,0.3673477172851562,0,0.3811721801757812,0.3879776000976562,0.3917694091796875,-2.359275817871094,0,0,0.3299331665039062,0.38427734375,0,0.3589248657226562,0.365234375,0,0.3790206909179688,0,0.3849945068359375,0,0.2553024291992188,0,-2.223800659179688,0,0.3276290893554688,0,0.3446197509765625,0.3604965209960938,0,0.3075408935546875,0.3283920288085938,0.35760498046875,0,0.2647476196289062,0,0,-2.2269287109375,0.2991256713867188,0,0.3214569091796875,0.3314895629882812,0,0.3338851928710938,0.3473663330078125,0.374114990234375,0,0.2857284545898438,0,-2.197212219238281,0.300811767578125,0.3254013061523438,0.3938751220703125,0.2878494262695312,0.2375946044921875,0.2141876220703125,0,0.2942962646484375,0,0.2082901000976562,0,0,-2.162490844726562,0,0.3069305419921875,0,0,0.1975631713867188,0,0.209503173828125,0,0.3246307373046875,0,0.303924560546875,0,0.3141021728515625,0.24737548828125,0.3225860595703125,0,0,-2.188232421875,0.326690673828125,0,0.3280181884765625,0.3271865844726562,0.3227767944335938,0.2703323364257812,0,0.2883758544921875,0.25244140625,0.1353607177734375,0,0,0,-2.024642944335938,0,0.1862030029296875,0,0.1902313232421875,0,0.2010726928710938,0,0.3347930908203125,0,0.3592147827148438,0,0.2167892456054688,0.2975845336914062,0.2796630859375,0,0.02117919921875,0,-2.043571472167969,0,0.2981643676757812,0.2143783569335938,0,0.2456512451171875,0,0.2519989013671875,0,0.2820510864257812,0.307708740234375,0.267486572265625,0,0.2370834350585938,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.967903137207031,0.2778244018554688,0,0.2616348266601562,0,0.2792434692382812,0,0.2711257934570312,0.2736892700195312,0,0,0.2747879028320312,0,0.1567535400390625,0.2235107421875,0,0,0.00911712646484375,0,0,-2.003402709960938,0,0.2812881469726562,0.240966796875,0,0.141815185546875,0.2133102416992188,0.2525405883789062,0,0,0.2279129028320312,0.1488189697265625,0,0.1370849609375,0,0.1357803344726562,0,0.157928466796875,0,0.1249847412109375,0,0,-1.980484008789062,0,0.2356338500976562,0,0.2292098999023438,0,0,0.2270278930664062,0,0.2266082763671875,0.2077178955078125,0,0.2312545776367188,0.197784423828125,0,0,0.1926727294921875,0,0.2065353393554688,0,0,0.08422088623046875,0,0,-1.969192504882812,0,0.2554473876953125,0.2164306640625,0.2305068969726562,0,0.2275924682617188,0.2286834716796875,0,0.2231826782226562,0,0.2127304077148438,0,0.1578750610351562,0,0.1714706420898438,0,0.102447509765625,0,0,-1.956321716308594,0,0.2117996215820312,0,0.2173843383789062,0,0.2286529541015625,0,0,0.2508087158203125,0.2410812377929688,0,0.2037429809570312,0,0.1987838745117188,0,0.1784591674804688,0,0,0.22637939453125,0,0.0554656982421875,0,-1.918830871582031,0,0.19024658203125,0.2168197631835938,0,0.2141494750976562,0.2212753295898438,0.22894287109375,0,0.2491607666015625,0.2300643920898438,0,0.223388671875,0,0.2002105712890625,0,0,0,0,0,-1.773689270019531,0,0.1981658935546875,0.2205429077148438,0,0.2369308471679688,0.2365036010742188,0,0.22509765625,0,0.2221527099609375,0,0.2205734252929688,0.21337890625,0.0547637939453125,0,0,-1.810234069824219,0,0.1991729736328125,0,0,0.2376327514648438,0,0.2500152587890625,0,0.2451171875,0,0.2486648559570312,0,0.2546157836914062,0,0.2571258544921875,0,0.1714630126953125,0,-1.810920715332031,0,0.2410659790039062,0.2739639282226562,0,0.25579833984375,0.2716598510742188,0,0,0.2434310913085938,0,0.2675323486328125,0.2669677734375,0.0432891845703125,0,0,-1.676719665527344,0,0.2574615478515625,0,0.2677230834960938,0.282867431640625,0,0.2846221923828125,0.2846603393554688,0,0.2827224731445312,0.06844329833984375,0,-1.621986389160156,0,0.262969970703125,0.2869491577148438,0,0.3331146240234375,0,0.298675537109375,0.29986572265625,0,0.1915206909179688,0,-1.690315246582031,0,0.2636260986328125,0.29864501953125,0,0.3126602172851562,0,0.31585693359375,0,0.313446044921875,0.236297607421875,0,0,-1.691741943359375,0,0.2647247314453125,0,0.2998428344726562,0.3262557983398438,0,0.32708740234375,0,0.3234024047851562,0,0.1998672485351562,0,-1.617767333984375,0,0.2697525024414062,0,0.3103713989257812,0,0.3372726440429688,0,0.3407745361328125,0,0.3351974487304688,0,0.072967529296875,0,0,-1.4793701171875,0,0,0.2832183837890625,0,0,0.3285293579101562,0,0.3470230102539062,0.3451614379882812,0,0.2232742309570312,0,-1.545127868652344,0,0,0.2707977294921875,0,0.310943603515625,0,0.3478775024414062,0.3543853759765625,0.308197021484375,0,-1.616867065429688,0,0.2509231567382812,0,0.2924652099609375,0.3377914428710938,0.3633041381835938,0.3656463623046875,0,0,0.05298614501953125,0,0,-1.397186279296875,0,0.2836227416992188,0,0.3295364379882812,0,0.3621597290039062,0,0.3709869384765625,0.09645843505859375,0,0,-1.419921875,0,0.277099609375,0,0,0.32257080078125,0,0.3547592163085938,0,0.3697128295898438,0,0.1405715942382812,0,0,-1.420829772949219,0.278076171875,0,0.3156661987304688,0,0.3504867553710938,0,0.3682632446289062,0.1523818969726562,0,-1.367195129394531,0.2820892333984375,0,0.3266143798828125,0.3403854370117188,0,0.3662185668945312,0,0,0.09527587890625,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.493019104003906,0,0,0.0147857666015625,0.2491302490234375,0,0.2649459838867188,0,0.2944488525390625,0,0.3223648071289062,0,0.3162155151367188,0,0.3486862182617188,0,0.3749771118164062,0,0.4104843139648438,0.368499755859375,0.3341293334960938,0.3349609375,0.3364944458007812,0,0.3348770141601562,0.335968017578125,0,0.196197509765625,0,0,-4.548080444335938,0.3382949829101562,0.3561477661132812,0,0.3483428955078125,0,0.34619140625,0,0.4190597534179688,0,0.3929977416992188,0.4071502685546875,0,0.4117355346679688,0.4146499633789062,0.4142303466796875,0,0.4187393188476562,0,0.3995513916015625,0,0.0132904052734375,0,0,-4.328353881835938,0,0.332000732421875,0,0.3794708251953125,0.3347320556640625,0,0.3713455200195312,0,0.3858566284179688,0,0,0.396575927734375,0,0.4005966186523438,0,0.4120330810546875,0,0.4056854248046875,0,0,0.4063339233398438,0.4063034057617188,0,0,0.2275772094726562,0,0,-4.431922912597656,0.3029251098632812,0,0.3216094970703125,0,0.3197784423828125,0.3466873168945312,0,0,0.365142822265625,0,0.3809967041015625,0,0.3902359008789062,0,0.4004364013671875,0,0.4090194702148438,0.4139785766601562,0,0,0.4149703979492188,0,0.3942947387695312,0.09990692138671875,0,0,-4.303497314453125,0,0.3009796142578125,0,0.31915283203125,0,0.3157119750976562,0,0,0.3597640991210938,0,0.3658218383789062,0,0.383056640625,0,0.3867340087890625,0,0.3964385986328125,0,0.3951339721679688,0,0.4539108276367188,0.4089431762695312,0,0,0.3439102172851562,0,0,0,0,0,-4.100845336914062,0.3121490478515625,0,0.310028076171875,0,0.353271484375,0.3668212890625,0.3824615478515625,0.3933944702148438,0,0.396881103515625,0,0.4019088745117188,0.4051055908203125,0,0.413421630859375,0,0.3985595703125,0,0.09073638916015625,0,-4.1629638671875,0.2722320556640625,0.284576416015625,0,0.3046722412109375,0.3519515991210938,0,0.3559188842773438,0.3658218383789062,0,0,0.3822021484375,0,0.384429931640625,0,0.395050048828125,0,0.399505615234375,0,0.4167709350585938,0,0.3718338012695312,0,0,0,0,0,-3.991607666015625,0,0.2977981567382812,0,0.2970657348632812,0.3810348510742188,0.3582611083984375,0,0.361358642578125,0,0.3742218017578125,0,0.38995361328125,0,0.3853683471679688,0.4039459228515625,0,0.3979110717773438,0,0.3999786376953125,0.064697265625,0,0,-4.004692077636719,0,0.2907562255859375,0,0.2879867553710938,0,0.3449859619140625,0.3589553833007812,0,0.3588485717773438,0.3671646118164062,0.3800506591796875,0,0.3916244506835938,0,0.3815078735351562,0,0,0.3902359008789062,0,0.3903274536132812,0,0.1803207397460938,0,-4.023193359375,0,0.2771530151367188,0.2812271118164062,0,0.3304290771484375,0,0.3541030883789062,0,0.3573226928710938,0.3661727905273438,0,0,0.3813629150390625,0.3886184692382812,0,0.41937255859375,0.3958816528320312,0,0.3990402221679688,0,0.1886367797851562,0,0,-3.968086242675781,0,0,0.2772598266601562,0,0.282470703125,0,0.33154296875,0.350555419921875,0,0.3566131591796875,0,0.3721160888671875,0.3820114135742188,0,0.393646240234375,0,0.3893280029296875,0,0.3945236206054688,0,0.4041213989257812,0,0.148223876953125,0,0,-3.878158569335938,0,0.269683837890625,0,0.2849578857421875,0,0.332366943359375,0,0.3465499877929688,0,0.3520736694335938,0.3554840087890625,0,0.3758316040039062,0.390625,0,0.39129638671875,0,0.4023895263671875,0,0,0.3962249755859375,0,0.093048095703125,0,-3.770225524902344,0.2876052856445312,0,0.2937469482421875,0,0.3330535888671875,0.353424072265625,0,0.3564071655273438,0,0.3716506958007812,0,0,0.3832855224609375,0.39447021484375,0.3995590209960938,0.4018173217773438,0,0.305877685546875,0,0,0,-3.594291687011719,0.2722854614257812,0,0.31829833984375,0.34259033203125,0,0.3551177978515625,0,0.3653411865234375,0,0.3787307739257812,0.3895339965820312,0,0.4046173095703125,0,0.404876708984375,0,0.4025421142578125,0.0691986083984375,0,-3.622589111328125,0.2630386352539062,0.3021011352539062,0,0.3352890014648438,0.3472061157226562,0.3593063354492188,0,0.3718719482421875,0,0.3867111206054688,0,0.3669204711914062,0.4458847045898438,0.409912109375,0,0.141448974609375,0,0,-3.6217041015625,0,0.2594070434570312,0.295440673828125,0,0.328125,0.3425445556640625,0,0.356048583984375,0,0.3553619384765625,0,0.3797454833984375,0,0.3902664184570312,0.40264892578125,0.40313720703125,0,0.2143630981445312,0,-3.618049621582031,0,0.2565383911132812,0,0.2795486450195312,0,0,0.3137664794921875,0,0.3356475830078125,0.357269287109375,0,0.3667449951171875,0,0.3805007934570312,0,0.3935623168945312,0,0.399871826171875,0.4046478271484375,0,0.23358154296875,0,0,0,0,0,-3.313163757324219,0,0.2801895141601562,0.3103179931640625,0,0.3356857299804688,0,0.3919830322265625,0,0.3651351928710938,0.3797988891601562,0,0.3974380493164062,0,0.4019927978515625,0.4020843505859375,0.1505508422851562,0,0,-3.469169616699219,0,0,0.2516326904296875,0,0,0.28302001953125,0.3091888427734375,0,0.337615966796875,0,0.3532333374023438,0,0.3664169311523438,0,0.3793792724609375,0,0.3981704711914062,0,0.4058380126953125,0.3991012573242188,0.08592987060546875,0,0,-3.392303466796875,0,0,0.273590087890625,0,0.3018417358398438,0.3251495361328125,0,0.3426666259765625,0,0,0.3573150634765625,0,0.361480712890625,0,0.3779144287109375,0,0.3868026733398438,0,0.3941879272460938,0.3700103759765625,0,0,0,0,0,-3.255836486816406,0,0.2572402954101562,0,0.2858505249023438,0.3191375732421875,0.347320556640625,0.3570938110351562,0,0.3709716796875,0,0.3832626342773438,0,0,0.3958969116210938,0,0.4009170532226562,0,0.2353134155273438,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-3.323356628417969,0,0.1793136596679688,0,0.2177810668945312,0,0.2348098754882812,0,0.252471923828125,0,0.2890243530273438,0,0.357147216796875,0,0.3411102294921875,0,0.3525009155273438,0,0,0.3692398071289062,0,0.3916244506835938,0,0.3942718505859375,0,0.039276123046875,0,-3.183845520019531,0,0.2528457641601562,0,0,0.2819900512695312,0,0.3119735717773438,0.3399124145507812,0,0.3583450317382812,0,0.3719940185546875,0,0.38409423828125,0,0.3985671997070312,0,0.40167236328125,0.176483154296875,0,0,-3.2216796875,0,0.245330810546875,0,0.2681808471679688,0.2698287963867188,0,0.3284759521484375,0.3550033569335938,0,0.3653793334960938,0,0.3866500854492188,0.3971633911132812,0,0.4076156616210938,0,0.2906112670898438,0,0,0,0,0,-2.996955871582031,0,0.2888336181640625,0,0.2898712158203125,0,0.3241043090820312,0.3548355102539062,0,0,0.3516845703125,0,0.3697280883789062,0,0.3858184814453125,0,0.3983306884765625,0,0.3248062133789062,0,0,0,0,0,-2.965164184570312,0.2538833618164062,0,0.2818145751953125,0,0,0.3198699951171875,0,0.350128173828125,0,0.3577728271484375,0,0.373565673828125,0,0.38970947265625,0.4008026123046875,0,0.3271102905273438,0,0,0,0,0,0,0,-2.928237915039062,0,0.2509231567382812,0,0.2776107788085938,0.3163223266601562,0,0.3483810424804688,0.357940673828125,0,0.3664016723632812,0,0.3825607299804688,0.3975601196289062,0.3186874389648438,0,0,0,0,0,-2.840576171875,0.2568435668945312,0,0,0.2846527099609375,0,0.3235931396484375,0.3470993041992188,0.354278564453125,0,0.370361328125,0,0.384185791015625,0.394317626953125,0.2119064331054688,0,0,0,0,0,-2.775840759277344,0,0.2546539306640625,0,0.2866592407226562,0,0.32415771484375,0,0.3504104614257812,0,0.3602294921875,0,0.369781494140625,0.3556747436523438,0,0.3777847290039062,0,0,0.1817703247070312,0,0,-2.933502197265625,0,0.2262115478515625,0,0,0.2841033935546875,0,0.29425048828125,0,0.32135009765625,0.3569107055664062,0,0.3520660400390625,0.3552093505859375,0,0.3760910034179688,0,0.3854751586914062,0.06569671630859375,0,-2.837577819824219,0,0.2372360229492188,0,0.259918212890625,0,0.290008544921875,0.3271636962890625,0.3474349975585938,0,0.3518295288085938,0,0.3653411865234375,0.3849945068359375,0,0.3562164306640625,0,0,0,-2.752944946289062,0,0.2342681884765625,0,0,0.2646331787109375,0,0.298828125,0,0,0.334075927734375,0.350250244140625,0.3879928588867188,0,0.3764419555664062,0,0.3805770874023438,0,0,0.2070999145507812,0,0,0,-2.600425720214844,0,0.2519683837890625,0,0.2844467163085938,0,0.3186416625976562,0.3453369140625,0,0.3555145263671875,0,0.3702545166015625,0.3862228393554688,0.36798095703125,0,0,0,0,0,-2.636505126953125,0,0.2438888549804688,0,0.271942138671875,0.3090438842773438,0.3434371948242188,0,0,0.3521499633789062,0.3606643676757812,0,0.3639450073242188,0.2949066162109375,0,0.1751251220703125,0,0,0,0,0,-2.547714233398438,0,0.2409515380859375,0,0.2698593139648438,0.3046493530273438,0,0.3386459350585938,0,0.345703125,0,0.3579788208007812,0,0.3722305297851562,0.3760528564453125,0.01900482177734375,0,-2.607688903808594,0,0.2382965087890625,0,0.2691650390625,0,0.2795486450195312,0,0.352935791015625,0.3308792114257812,0,0.3446578979492188,0,0.3476638793945312,0.378875732421875,0.1417694091796875,0,0,0,-2.383255004882812,0,0.2859268188476562,0.3072509765625,0.3426361083984375,0,0.35693359375,0,0.3613433837890625,0,0.283721923828125,0,0.3358306884765625,0,0.184600830078125,0,0,0,0,0,-2.420654296875,0.25799560546875,0,0.2649612426757812,0,0.30792236328125,0.3292083740234375,0,0.3446578979492188,0,0.3623199462890625,0,0.3796234130859375,0,0.24755859375,0,0,0,0,0,0,0,-2.390861511230469,0,0.2361984252929688,0,0.2691268920898438,0,0.2750015258789062,0,0.3295211791992188,0,0,0.3465423583984375,0,0.35797119140625,0,0.3790283203125,0.26995849609375,0,0,0,-2.353050231933594,0,0,0.2642364501953125,0,0.2791824340820312,0.3204193115234375,0,0.3509674072265625,0,0.3558502197265625,0,0.3635406494140625,0.3787918090820312,0.1113815307617188,0,0,-2.436073303222656,0,0,0.224456787109375,0,0.2523574829101562,0.2898330688476562,0,0.3291778564453125,0,0.35516357421875,0,0.3536605834960938,0.3749160766601562,0.326629638671875,0,0,0,-2.317405700683594,0,0.2415847778320312,0.2722244262695312,0,0.3075942993164062,0,0.3432998657226562,0.3494796752929688,0,0.3565673828125,0.3745956420898438,0.1411285400390625,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2.376068115234375,0,0,0.0855255126953125,0.2133331298828125,0,0.2354660034179688,0,0.258544921875,0.2967529296875,0.3292770385742188,0.3385467529296875,0,0.3537826538085938,0.3324661254882812,0,0,0,0,0,-2.228385925292969,0,0,0.2318038940429688,0,0,0.26904296875,0,0.3070220947265625,0,0.337127685546875,0,0.350982666015625,0.3582534790039062,0,0.3741302490234375,0,0.066864013671875,0,0,-2.258880615234375,0,0.224822998046875,0,0.2514190673828125,0,0.2907562255859375,0,0.3283157348632812,0,0.351837158203125,0,0.3609771728515625,0,0.3712615966796875,0,0.145294189453125,0,0,0,0,0,-2.064346313476562,0,0.2502212524414062,0,0.2874526977539062,0,0.325836181640625,0,0.3451004028320312,0.3538055419921875,0,0.3732528686523438,0,0.193359375,0,0,0,0,0,-2.03265380859375,0,0.2492904663085938,0.2888565063476562,0,0.33148193359375,0,0,0.35479736328125,0,0.3520431518554688,0,0.3565750122070312,0,0.1633071899414062,0,0,0,-2.019447326660156,0.2422409057617188,0,0,0.2773895263671875,0.3198928833007812,0,0.3525543212890625,0,0,0.3609466552734375,0,0.3732223510742188,0,0.1558380126953125,0,0,0,0,0,-1.954887390136719,0,0.23724365234375,0,0.2690582275390625,0.3086166381835938,0,0.3244552612304688,0,0,0.3433837890625,0,0.3541793823242188,0.17962646484375,0,0,0,0,0,-1.98236083984375,0.20196533203125,0,0.2110366821289062,0,0.1588211059570312,0,0.2841033935546875,0,0.2470626831054688,0,0.2853851318359375,0.310516357421875,0.265533447265625,0,0.07854461669921875,0,0,0,-2.047767639160156,0,0.2237319946289062,0,0,0.2432632446289062,0.259124755859375,0,0.2944259643554688,0,0.3141708374023438,0.3266830444335938,0,0.2293472290039062,0,0.2167129516601562,0,0,0,0,0,-1.978683471679688,0,0.2318649291992188,0.26629638671875,0.2911148071289062,0,0.3386917114257812,0,0,0.3830413818359375,0,0.3390350341796875,0,0.187347412109375,0,0,0,-1.893211364746094,0,0.2568359375,0.2892990112304688,0,0.3168106079101562,0.3364181518554688,0.3463897705078125,0,0.353973388671875,0,0.0512237548828125,0,0,-1.971168518066406,0,0.2165756225585938,0,0.246307373046875,0,0.2876205444335938,0,0.3255233764648438,0,0.3569107055664062,0,0.3625106811523438,0.2325439453125,0,0,0,0,0,0,0,-1.831001281738281,0,0,0.2298736572265625,0,0,0.2850189208984375,0.2884368896484375,0,0.323272705078125,0,0.35101318359375,0.3607101440429688,0,0.04856109619140625,0,0,-1.897331237792969,0.2297286987304688,0,0.2528457641601562,0,0.2969589233398438,0,0.30743408203125,0,0.347900390625,0,0.3630599975585938,0,0.1543655395507812,0,0,0,-1.710899353027344,0.24322509765625,0,0.2816238403320312,0,0.32427978515625,0,0.3544769287109375,0,0.3383331298828125,0,0,0.2230377197265625,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.85357666015625,0,0.1913223266601562,0.2177581787109375,0,0.2057647705078125,0.2327499389648438,0.2835617065429688,0,0.322113037109375,0,0.345062255859375,0.1080856323242188,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.831657409667969,0,0,0,0.06330108642578125,0,0,0.2461700439453125,0,0.2562484741210938,0,0.2912521362304688,0,0.3222274780273438,0.3211288452148438,0.2979583740234375,0.3798751831054688,0,0.3793563842773438,0,0,0.3937454223632812,0,0.404296875,0.4048233032226562,0.342376708984375,0,0.3299102783203125,0,0,0.328826904296875,0,0.32257080078125,0.3345870971679688,0,0.3273849487304688,0.332733154296875,0.3297958374023438,0.3335189819335938,0,0.3337554931640625,0,0.3311080932617188,0.2051773071289062,0,0,0,0,0,-7.213920593261719,0,0.2617645263671875,0.293304443359375,0,0.3290023803710938,0,0.3367462158203125,0,0,0.313812255859375,0.3558197021484375,0,0.3566970825195312,0,0.3704299926757812,0.3906784057617188,0.3851547241210938,0,0.3490371704101562,0.3821868896484375,0.3666915893554688,0,0.3720169067382812,0,0.3855667114257812,0.3637237548828125,0,0.37640380859375,0,0.386260986328125,0.3666229248046875,0.355560302734375,0.32464599609375,0,0,0,0,0,0,0,0,-6.974769592285156,0,0.2615737915039062,0.2838668823242188,0.3084259033203125,0,0.3055572509765625,0.316864013671875,0,0,0.3393630981445312,0,0.3486709594726562,0,0.3669204711914062,0,0.3577804565429688,0,0.3857345581054688,0,0.3902206420898438,0,0.3901596069335938,0.3935775756835938,0,0.402130126953125,0,0.3994064331054688,0,0.4402999877929688,0,0.4005584716796875,0.404296875,0,0.3862380981445312,0,0.2979583740234375,0,0,0,0,0,0,0,0,-6.828750610351562,0,0.2558517456054688,0.2826919555664062,0.2914199829101562,0,0.29742431640625,0,0.3402328491210938,0,0.3533096313476562,0.3653335571289062,0.3782730102539062,0,0.3881607055664062,0,0.391204833984375,0.3942337036132812,0,0.40606689453125,0,0.3838958740234375,0.3917312622070312,0.3938980102539062,0,0,0.3785476684570312,0.2833480834960938,0,0.3649673461914062,0.3682174682617188,0.3214263916015625,0,0,0,0,0,0,0,0,-6.767829895019531,0,0.236907958984375,0,0,0.2542572021484375,0,0,0.2739105224609375,0,0.2781295776367188,0,0.3260345458984375,0,0.341522216796875,0,0.35003662109375,0,0.3631057739257812,0.3786087036132812,0.3907852172851562,0.3903350830078125,0.3945693969726562,0,0.4004898071289062,0,0.3988037109375,0,0.400634765625,0,0,0.4014892578125,0,0,0.4019088745117188,0.4038543701171875,0,0.39208984375,0.188690185546875,0,0,0,-6.75921630859375,0.2461166381835938,0.25885009765625,0,0.2727203369140625,0,0.2830047607421875,0,0.3297195434570312,0,0.3434677124023438,0.3559646606445312,0,0.36395263671875,0,0.3864059448242188,0,0,0.39697265625,0.3897018432617188,0,0.404296875,0,0,0.4004135131835938,0,0.4002456665039062,0,0.40289306640625,0,0.4008026123046875,0,0.4066314697265625,0.4037017822265625,0,0.3929595947265625,0,0.1154403686523438,0,0,0,0,0,-6.656211853027344,0,0,0.2449417114257812,0,0.2551651000976562,0,0.2672271728515625,0,0.323577880859375,0,0.3403778076171875,0.3522491455078125,0,0.360107421875,0,0.3784637451171875,0,0.3801116943359375,0,0.3786468505859375,0,0.3814926147460938,0,0,0.3834609985351562,0.3811416625976562,0.3887939453125,0,0.39013671875,0.3958053588867188,0.4046707153320312,0,0,0.3988876342773438,0,0.3878173828125,0.0550994873046875,0,0,0,0,0,0,0,0,0,0,0,0,0,-6.596458435058594,0.2016220092773438,0,0.2340850830078125,0,0.2374801635742188,0,0.25006103515625,0.3014373779296875,0,0.3265914916992188,0.340728759765625,0,0.3520355224609375,0,0.37103271484375,0.3825836181640625,0.3897323608398438,0,0.39117431640625,0,0.3940811157226562,0,0.3998031616210938,0.4126510620117188,0.4001388549804688,0,0.4037322998046875,0,0.4025955200195312,0.3895187377929688,0,0.2041168212890625,0,0,0,-6.47650146484375,0,0.2423477172851562,0,0,0.2527389526367188,0.2593460083007812,0,0.3014602661132812,0,0.3376235961914062,0.3473968505859375,0,0,0.3564453125,0.3728103637695312,0.4216842651367188,0,0.3907699584960938,0.3967666625976562,0,0.3955078125,0.4041213989257812,0,0.4053573608398438,0,0.4074783325195312,0,0.4080429077148438,0.4125823974609375,0.3935317993164062,0.1562957763671875,0,0,0,0,0,-6.344551086425781,0,0.2437973022460938,0.2456130981445312,0,0,0.2591552734375,0,0.308837890625,0.3369140625,0.3487396240234375,0.35406494140625,0,0,0.3688812255859375,0,0.3816299438476562,0,0,0.3853225708007812,0.3959503173828125,0.3965530395507812,0,0.4065399169921875,0,0.409088134765625,0.4093170166015625,0.4110260009765625,0,0.409576416015625,0.3954696655273438,0,0.06087493896484375,0,0,0,0,0,-6.185333251953125,0.2656326293945312,0,0.2392120361328125,0.2750778198242188,0,0.3130722045898438,0,0,0.3363876342773438,0,0.3448104858398438,0,0.3516464233398438,0,0.3619918823242188,0.3769912719726562,0,0.3880844116210938,0,0.3969268798828125,0,7.676506042480469,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7.62939453125,7.62939453125e-06,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,15.2587890625,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7.667213439941406,0,0,0,0,0,15.35739898681641,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"filename":["<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,null,null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>","<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,null,null,"<expr>",null,null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,null,null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,null,null,null,"<expr>","<expr>","<expr>","<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,null,null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,null,null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>","<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,null,null,"<expr>",null,null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,"<expr>","<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null]},"interval":10,"files":[{"filename":"<expr>","content":"## Generate Large Random Dataset\nn <- 2e6\nx <- runif(n)\ny <- runif(n)\nz <- runif(n)\nXYZ <- cbind(x,y,z)\n\n## Inspect 4 equivalent `row mean` calculations \nprofvis::profvis({\n    m <- rowSums(XYZ)/ncol(XYZ)\n    m <- rowMeans(XYZ)\n    m <- apply(XYZ, 1, mean)\n    m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }\n})\n## rowSums(), colSums(), rowMeans(), and colMeans() are vectorised and fast.\n## for loop is not the slowest, but the ugliest.","normpath":"<expr>"}],"prof_output":"/tmp/RtmpYgnWP3/file15e34ff27cc2.prof","highlight":{"output":["^output\\$"],"gc":["^<GC>$"],"stacktrace":["^\\.\\.stacktraceo(n|ff)\\.\\.$"]},"split":"h"}},"evals":[],"jsHooks":[]}</script>
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
##  mean1(x, 0.5) 19.86670 21.01193 25.23672 23.08634 26.53421 54.19951   100   a
##  mean2(x, 0.5) 18.93285 20.15900 24.98203 21.96553 27.34243 50.92795   100   a
##  mean3(x, 0.5) 19.84720 20.66372 24.37547 22.86381 25.45524 41.98796   100   a
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
##  ma1(y) 174.87259 187.94205 198.74114 192.49076 200.30609 340.8298   100  a 
##  ma2(y)  19.66996  21.73871  26.71302  24.20618  27.26824 186.1022   100   b
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
##   0.106   0.000   0.034
```

```r
system.time({ lm(Y~X, data=DAT) })
```

```
##    user  system elapsed 
##   0.403   0.019   0.155
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
##   0.903   0.159   0.605
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

