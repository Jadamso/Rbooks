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

**It does not take much time to update or replicate your results**.

* Your computer runs for 2 hours and reproduces the figures and tables.
* You also rewrote your big calculations to use multiple cores, this took two hours to do but saved 6 hours *each time* you rerun your code.
* You add some more data. It adds almost no time to see whether much has changed.

**Your results are transparent and easier to build on**.

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

**Example 1: Data Scientism**.
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
* change the name to your own, and make any other edits you like
* use the console to run

``` r
rmarkdown::render('DataScientism.Rmd')
```


**Example 2: Homework Assignment**.
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
<div class="plotly html-widget html-fill-item" id="htmlwidget-c6ba478b53eb65ee1f27" style="width:672px;height:480px;"></div>
<script type="application/json" data-for="htmlwidget-c6ba478b53eb65ee1f27">{"x":{"visdat":{"2769323196f2":["function () ","plotlyVisDat"]},"cur_data":"2769323196f2","attrs":{"2769323196f2":{"x":{},"y":{},"alpha_stroke":1,"sizes":[10,100],"spans":[1,20]}},"layout":{"margin":{"b":40,"l":60,"t":25,"r":10},"xaxis":{"domain":[0,1],"automargin":true,"title":"X"},"yaxis":{"domain":[0,1],"automargin":true,"title":"Y"},"hovermode":"closest","showlegend":false},"source":"A","config":{"modeBarButtonsToAdd":["hoverclosest","hovercompare"],"showSendToCloud":false},"data":[{"x":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100],"y":[1.7341713858859293,9.4387569559039299,12.190321681068905,15.784736233761938,20.641057161622459,25.998276602339569,26.014124568904688,30.548006647731967,34.458476946559827,41.211145542276668,46.633669622708467,46.974839208063976,52.668410156037538,55.521867493462032,58.561543806066695,58.901449944881087,68.982700249180752,70.048598792226855,77.878930845092995,81.089625850705815,83.041404091387733,88.86942474801296,89.425185371186018,94.162201862348653,100.36949163525064,102.80701697373765,106.79767457546133,111.28795221399675,114.23997323203204,119.43445748622456,122.41543649634603,124.38394708488626,130.04902490743106,132.90001447605749,138.62919303394617,143.79279163292483,149.81051490188429,150.89845534765473,157.7530790267314,159.0831869122693,162.02512152814987,167.80980235304793,170.16285272003347,174.58265942842283,181.83293707550618,182.04508077668595,184.99642127879167,191.85283051269371,196.7099880234681,201.18110543955984,205.68022133565725,210.54888167666164,210.1273247165951,216.82520052905076,221.12984000236875,226.03865294716218,225.82406760729046,235.56566876011854,237.17316413122632,236.37855241706168,245.32260997451553,245.31636245415626,248.87533887006001,258.29740119802989,262.21542395847746,260.89219435279222,264.16816654952083,267.29942932947301,275.88465194832071,280.02943003235794,284.88593024585583,286.2513602230045,293.17838047339734,295.9632826630687,300.79181393736383,306.36520123180509,308.60541142842135,308.70813968858579,316.03745380293321,316.57506279665506,322.69392438837286,327.1805504797278,332.98681585188223,340.23843333586757,335.56373933360271,341.19612173605003,345.99273784874913,355.29659471194373,356.96053036185759,359.44917759010616,365.74124296670783,369.81616409721317,371.36915167670679,377.67038486089336,379.07909885098201,386.82800089905368,389.19251245711877,391.05252708274014,397.26121738477269,398.67682222394399],"type":"scatter","mode":"markers","marker":{"color":"rgba(31,119,180,1)","line":{"color":"rgba(31,119,180,1)"}},"error_y":{"color":"rgba(31,119,180,1)"},"error_x":{"color":"rgba(31,119,180,1)"},"line":{"color":"rgba(31,119,180,1)"},"xaxis":"x","yaxis":"y","frame":null}],"highlight":{"on":"plotly_click","persistent":false,"dynamic":false,"selectize":false,"opacityDim":0.20000000000000001,"selected":{"opacity":1},"debounce":0},"shinyEvents":["plotly_hover","plotly_click","plotly_selected","plotly_relayout","plotly_brushed","plotly_brushing","plotly_clickannotation","plotly_doubleclick","plotly_deselect","plotly_afterplot","plotly_sunburstclick"],"base_url":"https://plot.ly"},"evals":[],"jsHooks":[]}</script>
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

**Poster**.

See [DataScientism_Poster.html](https://jadamso.github.io/Rbooks/Templates/DataScientism_Poster.html) and recreate from the source file [DataScientism_Poster.Rmd](https://jadamso.github.io/Rbooks/Templates/DataScientism_Poster.Rmd). Simply change the name to your own, and knit the document.

**Slides**.

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

**MAKEFILE**.

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

**Tracing**.

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


**Isolating**.

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

**Handling**.

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


**Benchmarking**.

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
##   0.236   0.000   0.238
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
<div class="profvis html-widget html-fill-item" id="htmlwidget-f45ae73c09f6799a8bb5" style="width:100%;height:600px;"></div>
<script type="application/json" data-for="htmlwidget-f45ae73c09f6799a8bb5">{"x":{"message":{"prof":{"time":[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,16,16,17,17,18,18,19,19,20,20,21,21,22,22,23,23,24,24,25,25,26,26,27,27,28,28,29,29,30,30,31,31,32,32,33,33,34,34,35,35,36,37,38,38,39,40,40,41,41,42,42,43,43,44,44,45,45,45,46,47,47,48,49,49,50,50,51,51,52,52,53,53,54,55,55,56,56,57,57,58,58,59,60,61,62,63,63,63,64,64,64,65,65,66,66,67,68,68,69,69,70,70,71,72,72,73,74,75,76,76,77,77,78,78,79,79,80,80,81,81,82,82,83,83,84,84,85,86,87,87,88,88,89,90,90,91,92,92,93,93,94,94,95,96,96,97,97,98,98,99,100,101,102,103,104,105,105,105,106,106,107,107,107,108,108,109,109,110,110,111,111,112,112,113,113,114,115,116,116,117,117,118,118,119,119,119,120,120,121,121,122,122,123,123,123,124,124,125,125,126,127,127,128,128,129,130,130,131,131,132,133,134,135,135,136,136,137,137,138,138,139,140,140,141,142,143,143,143,144,144,145,145,146,146,147,148,148,149,149,150,150,151,151,152,153,153,154,155,156,156,157,157,158,158,159,159,159,160,160,160,161,162,162,163,163,163,164,164,165,165,166,166,167,167,168,169,169,169,170,170,170,171,171,172,173,173,174,174,174,175,176,176,177,178,179,180,181,181,181,182,182,182,183,184,185,185,186,186,187,188,188,189,190,190,191,191,192,192,193,193,193,194,194,194,195,196,197,197,198,198,199,199,200,201,201,201,202,202,203,204,204,205,205,205,206,206,206,207,207,207,208,208,209,210,211,211,212,212,213,213,214,214,215,215,215,216,216,217,217,217,218,218,219,219,220,221,221,222,222,223,223,224,224,225,225,226,226,227,227,228,229,229,229,230,230,230,231,231,231,232,232,233,234,234,235,235,236,237,237,238,239,240,241,241,241,242,242,242,243,243,244,244,245,246,247,247,248,249,250,251,251,252,253,253,253,254,254,254,255,255,256,256,257,258,259,260,260,261,262,262,263,263,264,264,265,265,266,266,267,268,268,269,269,270,270,271,272,272,273,273,274,274,275,276,276,276,277,277,277,278,278,279,279,280,281,281,282,283,283,284,285,286,286,287,287,287,288,288,288,289,289,289,290,290,290,291,291,291,292,292,292,293,293,293,294,294,294,295,295,295,296,296,297,297,298,299,299,300,300,301,301,302,302,303,303,304,305,305,306,306,307,307,308,309,310,310,310,311,311,312,313,314,314,315,316,316,316,317,317,317,318,318,319,319,320,321,322,322,323,323,324,324,325,325,326,326,327,327,327,328,328,328,329,330,330,331,331,332,333,334,334,335,335,336,336,337,337,337,338,338,338,339,339,340,341,342,343,343,344,345,345,346,346,346,347,347,347,348,348,348,349,350,350,351,351,352,353,354,354,355,356,357,358,358,358,359,359,360,361,361,362,362,363,363,364,364,365,365,366,366,367,367,368,368,368,369,369,369,370,370,371,371,372,372,373,374,375,375,376,376,377,377,378,378,378,379,379,379,380,380,380,381,381,381,382,383,384,384,385,386,386,387,387,388,388,389,389,389,390,390,390,391,392,392,393,393,394,395,395,396,397,398,399,399,400,400,400,401,401,401,402,403,403,403,404,404,405,406,406,407,407,408,409,410,410,410,411,411,411,412,412,413,413,413,414,414,415,415,416,416,417,417,418,418,418,419,420,420,421,421,422,422,423,423,423,424,425,425,426,426,427,428,428,429,429,429,430,430,430,431,431,432,432,432,433,433,433,434,434,435,435,435,436,436,437,437,438,439,439,440,440,440,441,441,441,442,442,443,443,444,444,445,445,446,446,447,447,448,448,449,449,450,450,450,451,451,451,452,453,454,454,455,455,456,456,457,457,458,458,459,459,460,460,460,461,461,461,462,462,463,463,463,464,464,465,465,466,467,468,468,469,470,470,470,471,471,471,472,472,473,474,475,476,477,477,478,478,479,479,480,480,481,482,482,483,484,484,485,485,486,486,487,487,488,488,488,489,489,489,490,490,491,492,492,493,494,495,495,496,497,497,497,498,498,498,499,500,500,501,501,502,502,503,503,504,504,505,505,506,506,507,507,508,508,509,509,510,510,511,511,512,512,513,513,514,514,515,515,516,516,517,517,518,518,519,519,520,520,521,521,522,522,523,523,524,524,525,525,526,526,527,527,528,528,529,529,530,530,531,531,532,532,533,533,534,534,535,535,536,536,537,537,538,538,539,539,540,540,541,541,542,542,542,543,543,543,544,544,544,545,546,547,547,548,548,549,550,551,552,553,553,554,555,556,556,557,557,558,558,559,559,560,560,561,561,562,562,563,563,564,564,565,565,566,567,567,567,568,568,568,569,569,570,570,571,571,572,572,573,573,574,574,574,575,575,575,576,576,576,577,578,578,579,579,580,580,581,581,582,582,583,584,584,584,585,585,586,586,587,587,588,589,590,590,591,591,591,592,592,592,593,593,593,594,595,595,596,596,597,597,598,598,599,599,599,600,600,601,601,602,602,603,603,604,604,605,605,606,606,607,608,608,609,609,610,611,612,613,613,614,614,615,615,616,616,616,617,617,617,618,619,619,620,620,621,622,623,624,624,625,625,626,626,627,627,628,628,629,629,630,630,631,632,632,633,633,633,634,635,635,636,637,637,638,638,639,639,639,640,640,641,641,642,642,643,643,644,644,645,645,645,646,646,647,647,648,648,649,650,651,651,652,652,653,654,654,655,655,655,656,656,657,657,658,658,659,659,660,660,661,661,662,662,663,663,664,664,665,665,666,666,667,667,668,669,670,670,670,671,671,671,672,672,673,673,674,674,675,675,676,677,678,678,679,679,680,681,682,682,683,684,684,685,685,686,686,687,687,688,689,689,690,690,690,691,692,692,693,694,694,695,696,697,698,698,698,699,699,699,700,700,701,701,702,702,703,703,704,704,705,706,706,707,707,708,708,709,709,710,710,711,712,712,713,713,714,714,715,716,717,717,718,718,719,719,720,720,721,721,721,722,722,722,723,723,724,725,726,727,727,728,728,729,730,730,731,731,732,732,733,733,734,734,735,736,737,737,738,738,739,740,741,742,742,743,744,744,745,745,746,746,747,748,748,748,749,750,750,751,752,753,753,754,755,755,756,756,757,757,758,759,759,759,760,761,762,762,762,763,764,765,765,766,766,767,767,768,768,769,769,769,770,770,771,771,772,773,773,774,774,774,775,775,775,776,776,776,777,777,777,778,778,779,779,780,780,781,781,782,783,783,784,785,785,786,786,787,787,788,788,789,789,789,790,790,791,791,792,793,793,794,795,795,796,797,797,798,799,800,801,801,802,802,802,803,803,803,804,804,805,806,806,807,807,807,808,808,809,809,810,811,811,812,812,813,813,813,814,815,815,816,817,817,818,819,819,820,821,822,822,823,823,823,824,824,824,825,825,825,826,826,827,827,828,829,829,829,830,830,831,831,832,833,833,834,834,835,835,836,837,837,838,838,839,840,840,841,841,842,842,843,843,844,845,845,846,846,847,847,848,849,849,850,850,850,851,851,851,852,852,853,854,854,855,855,856,856,857,857,858,858,859,859,859,860,861,861,861,862,862,863,863,864,865,865,866,866,867,867,868,869,869,870,870,871,871,872,873,873,874,874,874,875,875,876,876,877,878,878,879,880,880,881,881,882,883,883,884,885,885,886,886,887,888,889,889,890,890,891,891,892,892,893,893,894,894,895,896,896,897,897,898,898,899,899,900,900,901,901,902,903,903,904,904,904,905,906,907,907,908,908,909,909,909,910,911,911,912,912,913,913,914,914,915,915,916,916,917,917,918,918,919,919,920,920,921,921,922,923,924,924,925,925,926,926,927,927,928,929,930,930,931,932,932,933,933,934,934,935,935,936,936,937,937,938,938,939,940,940,940,941,941,941,942,942,943,943,943,944,944,945,945,946,947,948,948,949,950,950,950,951,951,951,952,952,952,953,953,953,954,954,954,955,955,956,957,957,958,958,959,959,960,961,961,962,962,962,963,963,964,964,965,966,966,967,967,968,968,969,970,970,971,971,972,972,972,973,973,973,974,974,974,975,976,976,977,977,978,979,979,980,980,981,982,983,984,984,985,985,986,986,987,987,988,988,989,990,990,991,991,991,992,993,993,994,994,995,995,995,996,996,997,997,998,999,999,999,1000,1001,1002,1002,1003,1003,1003,1004,1004,1005,1006,1006,1007,1007,1008,1008,1009,1009,1010,1011,1011,1012,1012,1013,1013,1014,1014,1015,1015,1016,1016,1017,1017,1018,1019,1019,1020,1020,1021,1022,1022,1023,1024,1024,1025,1025,1025,1026,1026,1027,1027,1028,1029,1029,1030,1030,1031,1032,1032,1032,1033,1034,1034,1035,1036,1037,1037,1038,1039,1039,1040,1040,1040,1041,1041,1041,1042,1042,1042,1043,1043,1043,1044,1044,1044,1045,1045,1045,1046,1046,1046,1047,1047,1047,1048,1048,1048,1049,1049,1049,1050,1050,1050,1051,1051,1051,1052,1052,1052,1053,1053,1053,1054,1054,1054,1055,1055,1055,1056,1056,1056,1057,1057,1057,1058,1058,1058,1059,1059,1060,1061,1062,1063,1064,1065,1065,1066,1066,1067,1067,1067,1068,1068,1069,1069,1070,1071,1072,1072,1073,1073,1074,1075,1075,1076,1076,1077,1077,1078,1078,1079,1079,1080,1080,1081,1082,1082,1083,1083,1084,1084,1085,1085,1086,1086,1086,1087,1088,1088,1089,1089,1090,1090,1091,1091,1092,1092,1092,1093,1093,1094,1094,1094,1094,1095,1095,1095,1095,1096,1096,1097,1097,1098,1098,1098,1099,1099,1100,1101,1101,1102,1102,1102,1103,1103,1104,1105,1105,1106,1107,1107,1108,1108,1109,1109,1110,1110,1111,1111,1112,1112,1113,1113,1114,1114,1115,1115,1116,1116,1117,1117,1118,1118,1119,1119,1120,1120,1121,1121,1122,1123,1123,1124,1124,1125,1125,1126,1126,1127,1127,1128,1129,1130,1131,1132,1133,1133,1134,1134,1135,1135,1136,1136,1137,1137,1138,1138,1139,1140,1141,1141,1142,1142,1142,1143,1143,1144,1144,1145,1145,1146,1146,1147,1148,1148,1149,1149,1150,1151,1151,1152,1152,1153,1153,1154,1155,1155,1156,1156,1156,1157,1157,1157,1158,1158,1158,1159,1159,1160,1160,1161,1162,1162,1163,1163,1163,1164,1164,1165,1165,1166,1166,1167,1167,1168,1169,1169,1170,1170,1171,1171,1172,1173,1173,1174,1175,1175,1175,1176,1176,1176,1177,1177,1177,1178,1178,1179,1179,1180,1180,1181,1181,1182,1182,1183,1183,1183,1184,1185,1185,1185,1186,1187,1188,1188,1189,1189,1190,1191,1191,1191,1192,1193,1193,1194,1194,1195,1195,1196,1196,1197,1197,1198,1198,1199,1200,1200,1201,1201,1202,1202,1203,1203,1204,1205,1206,1207,1207,1208,1208,1209,1209,1210,1210,1211,1211,1212,1212,1213,1213,1214,1214,1215,1215,1216,1216,1216,1217,1217,1217,1218,1218,1219,1219,1220,1220,1221,1222,1222,1223,1224,1224,1225,1225,1226,1226,1227,1227,1227,1228,1228,1228,1229,1229,1229,1230,1231,1231,1232,1232,1233,1233,1234,1235,1235,1235,1236,1237,1237,1237,1238,1239,1240,1240,1241,1241,1242,1242,1243,1244,1244,1245,1245,1246,1246,1247,1247,1247,1248,1248,1248,1249,1249,1249,1250,1250,1250,1251,1251,1252,1252,1253,1253,1254,1254,1255,1255,1255,1256,1257,1257,1258,1258,1258,1259,1259,1260,1260,1261,1261,1262,1263,1264,1265,1265,1266,1266,1266,1267,1267,1267,1268,1268,1269,1270,1270,1271,1272,1273,1273,1274,1274,1275,1275,1276,1276,1276,1277,1277,1278,1279,1279,1280,1280,1281,1281,1282,1282,1283,1283,1283,1284,1284,1284,1285,1285,1286,1286,1287,1287,1288,1289,1289,1290,1291,1292,1293,1293,1294,1295,1296,1296,1297,1297,1297,1298,1298,1299,1299,1300,1300,1301,1301,1302,1302,1303,1303,1304,1304,1305,1305,1306,1307,1307,1308,1308,1309,1309,1309,1310,1310,1310,1311,1311,1312,1312,1313,1314,1314,1315,1315,1316,1316,1317,1317,1318,1319,1319,1320,1321,1321,1322,1323,1323,1323,1324,1325,1325,1326,1326,1327,1327,1328,1328,1329,1330,1330,1330,1331,1331,1331,1332,1332,1332,1333,1333,1334,1335,1336,1336,1337,1337,1338,1338,1339,1340,1340,1340,1341,1342,1342,1343,1344,1344,1345,1345,1346,1346,1346,1347,1347,1347,1348,1348,1349,1349,1350,1351,1351,1352,1353,1353,1354,1354,1355,1355,1356,1356,1356,1357,1358,1359,1360,1360,1361,1361,1362,1362,1362,1363,1363,1363,1364,1364,1364,1365,1365,1365,1366,1367,1368,1368,1369,1369,1370,1371,1372,1373,1373,1374,1374,1374,1375,1375,1376,1377,1377,1378,1378,1379,1379,1380,1381,1381,1382,1382,1383,1383,1383,1384,1384,1384,1385,1385,1385,1386,1387,1388,1388,1389,1390,1391,1391,1392,1392,1393,1393,1394,1394,1395,1395,1396,1396,1397,1398,1398,1399,1399,1400,1400,1401,1401,1401,1402,1402,1402,1403,1404,1405,1406,1406,1407,1408,1408,1409,1409,1410,1410,1411,1412,1412,1413,1414,1414,1415,1415,1415,1416,1416,1416,1417,1417,1417,1418,1418,1419,1419,1420,1421,1422,1422,1423,1424,1424,1425,1425,1426,1427,1427,1428,1428,1429,1429,1430,1430,1431,1431,1432,1432,1433,1433,1434,1434,1435,1435,1436,1436,1437,1437,1438,1438,1439,1439,1440,1440,1441,1441,1442,1442,1443,1443,1444,1444,1445,1445,1446,1446,1447,1447,1448,1448,1449,1449,1450,1450,1451,1451,1452,1452,1453,1453,1454,1454,1455,1456,1457,1458,1458,1459,1460,1461,1461,1462,1462,1463,1463,1464,1464,1465,1466,1466,1466,1467,1467,1467,1468,1468,1468,1469,1470,1470,1471,1471,1472,1473,1473,1474,1474,1475,1475,1476,1476,1477,1477,1478,1478,1478,1479,1479,1480,1481,1481,1481,1482,1482,1482,1483,1483,1483,1484,1484,1484,1485,1485,1486,1487,1487,1488,1488,1489,1489,1490,1490,1491,1491,1492,1492,1493,1494,1494,1495,1496,1496,1496,1497,1497,1498,1499,1499,1500,1500,1500,1501,1501,1501,1502,1502,1502,1503,1503,1503,1504,1504,1504,1505,1505,1505,1506,1506,1507,1507,1508,1509,1509,1510,1510,1511,1511,1511,1512,1513,1513,1514,1515,1515,1516,1516,1516,1517,1517,1517,1518,1518,1518,1519,1519,1520,1520,1521,1521,1522,1523,1523,1524,1524,1525,1526,1526,1527,1528,1529,1530,1530,1531,1531,1532,1532,1533,1533,1534,1534,1535,1536,1536,1537,1537,1538,1539,1539,1540,1540,1541,1541,1542,1542,1543,1543,1544,1544,1545,1545,1546,1546,1547,1547,1548,1548,1548,1549,1549,1550,1550,1551,1551,1552,1552,1553,1553,1554,1555,1555,1556,1556,1557,1557,1558,1558,1559,1559,1560,1560,1561,1561,1561,1562,1562,1563,1564,1564,1565,1565,1566,1566,1567,1567,1568,1569,1569,1569,1570,1570,1570,1571,1571,1571,1572,1572,1573,1574,1575,1575,1576,1576,1577,1577,1578,1578,1579,1579,1580,1581,1581,1582,1582,1583,1583,1583,1584,1584,1584,1585,1585,1585,1586,1586,1587,1588,1588,1588,1589,1590,1591,1591,1592,1593,1593,1594,1595,1595,1596,1596,1596,1597,1597,1597,1598,1598,1598,1599,1599,1599,1600,1600,1601,1602,1602,1603,1604,1605,1605,1606,1607,1607,1608,1608,1609,1610,1610,1611,1611,1612,1612,1613,1613,1614,1614,1614,1615,1616,1616,1617,1618,1619,1619,1620,1620,1621,1621,1622,1623,1623,1623,1624,1624,1624,1625,1625,1625,1626,1627,1628,1628,1629,1629,1630,1631,1631,1632,1633,1634,1634,1634,1635,1636,1636,1636,1637,1637,1637,1638,1638,1638,1639,1640,1640,1641,1641,1642,1642,1643,1643,1644,1644,1645,1646,1647,1648,1648,1649,1650,1650,1651,1651,1652,1652,1653,1653,1654,1654,1655,1656,1656,1657,1657,1658,1658,1659,1659,1660,1660,1661,1661,1662,1662,1663,1663,1664,1664,1665,1665,1666,1666,1667,1667,1668,1668,1669,1669,1670,1670,1671,1671,1671,1672,1673,1674,1674,1675,1675,1676,1676,1677,1678,1678,1679,1680,1681,1682,1682,1682,1683,1683,1683,1684,1684,1684,1685,1685,1685,1686,1686,1686,1687,1687,1687,1688,1688,1688,1689,1689,1689,1690,1690,1690,1691,1691,1691,1692,1692,1692,1693,1693,1693,1694,1694,1694,1695,1695,1695,1696,1696,1696,1697,1697,1697,1698,1698,1698,1699,1699,1699,1700,1700,1700,1701,1701,1701,1702,1702,1702,1703,1703,1703,1704,1704,1704,1705,1705,1705,1706,1706,1706,1707,1707,1707,1708,1708,1708,1709,1709,1709,1710,1710,1710,1711,1711,1711,1712,1712,1712,1713,1713,1713,1714,1714,1714,1715,1715,1715,1716,1716,1716,1717,1717,1717,1718,1718,1718,1719,1719,1719,1720,1720,1720,1721,1721,1721,1722,1722,1722,1723,1723,1723,1724,1724,1724,1725,1725,1725,1726,1726,1726,1727,1727,1727,1728,1728,1728,1729,1729,1729,1730,1730,1730,1731,1731,1731,1732,1732,1732,1733,1733,1733,1734,1734,1734,1735,1735,1735,1736,1736,1736,1737,1737,1737,1738,1738,1738,1739,1739,1739,1740,1740,1740,1741,1741,1741,1742,1742,1742,1743,1743,1743,1744,1744,1744,1745,1745,1745,1746,1746,1746,1747,1747,1747,1748,1748,1748,1749,1749,1749,1750,1750,1750,1751,1751,1751,1752,1752,1752,1753,1753,1753,1754,1754,1754,1755,1755,1755,1756,1756,1756,1757,1757,1758,1758,1759,1759,1760,1761,1761,1761,1762,1763,1764,1764,1765,1765,1766,1766,1767,1767,1768,1768,1769,1769,1770,1770,1770,1771,1771,1772,1772,1773,1773,1774,1775,1775,1776,1776,1777,1777,1778,1778,1779,1780,1780,1781,1781,1782,1783,1784,1785,1785,1786,1786,1787,1787,1787,1788,1788,1789,1789,1790,1790,1791,1791,1791,1792,1792,1793,1793,1794,1795,1795,1795,1796,1796,1796,1797,1797,1797,1798,1799,1800,1800,1801,1801,1802,1802,1803,1803,1804,1804,1805,1805,1806,1807,1807,1808,1808,1809,1809,1810,1810,1811,1811,1812,1812,1813,1813,1814,1815,1815,1816,1816,1817,1817,1818,1818,1819,1819,1820,1820,1820,1821,1821,1822,1822,1823,1823,1824,1825,1825,1826,1826,1827,1827,1828,1828,1829,1829,1830,1830,1831,1832,1832,1833,1833,1833,1833,1834,1834,1834,1834,1835,1835,1835,1835,1836,1836,1836,1836,1837,1837,1838,1838,1839,1839,1840,1841,1841,1842,1843,1843,1844,1844,1845,1845,1846,1847,1847,1848,1849,1849,1850,1850,1851,1852,1852,1853,1853,1854,1855,1855,1856,1857,1857,1858,1858,1859,1859,1860,1861,1862,1862,1863,1864,1864,1865,1866,1866,1867,1867,1868,1869,1869,1870,1870,1871,1871,1872,1872,1873,1873,1874,1874,1875,1875,1876,1877,1878,1878,1879,1879,1880,1880,1881,1881,1882,1882,1883,1884,1885,1885,1886,1887,1887,1888,1889,1889,1890,1891,1891,1891,1892,1892,1893,1893,1894,1895,1896,1896,1897,1897,1898,1898,1899,1899,1900,1900,1901,1901,1902,1902,1903,1903,1904,1905,1905,1905,1906,1906,1906,1907,1907,1907,1908,1908,1908,1909,1909,1910,1910,1910,1911,1912,1912,1913,1913,1913,1914,1914,1915,1916,1916,1917,1917,1918,1918,1919,1919,1920,1920,1921,1922,1922,1923,1924,1925,1926,1926,1927,1927,1928,1929,1930,1931,1931,1932,1933,1933,1934,1935,1935,1936,1936,1936,1937,1938,1939,1939,1939,1940,1940,1940,1941,1941,1942,1942,1943,1943,1944,1944,1945,1945,1946,1946,1947,1947,1948,1949,1949,1950,1950,1951,1952,1953,1954,1955,1956,1956,1957,1957,1957,1958,1959,1959,1960,1961,1961,1962,1963,1964,1965,1966,1966,1966,1967,1968,1969,1969,1970,1970,1971,1972,1973,1973,1974,1974,1975,1976,1976,1976,1977,1977,1977,1978,1978,1978,1979,1979,1979,1980,1980,1981,1982,1983,1983,1984,1984,1985,1986,1987,1987,1988,1989,1990,1990,1991,1992,1992,1993,1994,1995,1995,1996,1997,1998,1999,1999,2000,2000,2000,2001,2001,2002,2002,2003,2004,2004,2005,2005,2006,2006,2006,2007,2007,2008,2009,2010,2010,2010,2011,2011,2011,2012,2012,2012,2013,2013,2013,2014,2014,2014,2015,2015,2015,2016,2016,2016,2017,2017,2017,2018,2018,2018,2019,2019,2019,2020,2020,2020,2021,2021,2021,2022,2022,2023,2024,2024,2025,2025,2026,2026,2027,2028,2029,2030,2030,2031,2031,2032,2033,2033,2033,2034,2035,2035,2036,2036,2036,2037,2038,2038,2039,2039,2040,2040,2041,2041,2042,2043,2043,2044,2045,2045,2046,2046,2047,2047,2048,2048,2049,2050,2051,2051,2052,2052,2053,2053,2054,2054,2055,2055,2056,2056,2056,2057,2057,2058,2058,2059,2059,2060,2060,2061,2061,2062,2063,2064,2065,2065,2066,2067,2067,2068,2069,2069,2070,2070,2071,2071,2072,2072,2073,2073,2073,2074,2074,2075,2076,2076,2077,2077,2078,2078,2079,2080,2080,2081,2081,2082,2083,2083,2083,2084,2085,2085,2086,2086,2087,2087,2088,2088,2089,2089,2090,2090,2091,2091,2092,2092,2093,2093,2094,2094,2095,2095,2096,2096,2097,2097,2097,2098,2098,2099,2100,2101,2101,2102,2103,2104,2104,2104,2105,2106,2106,2106,2107,2108,2109,2109,2110,2111,2111,2112,2112,2113,2113,2114,2114,2115,2116,2116,2117,2117,2118,2119,2119,2119,2120,2120,2120,2121,2121,2121,2122,2122,2122,2123,2123,2124,2124,2125,2125,2125,2126,2126,2127,2127,2128,2128,2129,2129,2130,2130,2131,2131,2132,2132,2133,2133,2134,2134,2135,2135,2136,2136,2137,2137,2138,2138,2139,2140,2140,2141,2141,2142,2142,2143,2143,2144,2144,2145,2145,2146,2146,2147,2147,2148,2148,2149,2149,2150,2150,2151,2151,2152,2152,2153,2153,2154,2154,2155,2155,2156,2156,2157,2157,2158,2158,2159,2159,2160,2160,2161,2161,2162,2162],"depth":[27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,1,1,1,3,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,1,1,1,1,1,3,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,1,1,1,2,1,2,1,2,1,2,1,1,2,1,1,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,1,1,2,1,2,1,2,1,3,2,1,3,2,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,2,1,1,2,1,3,2,1,1,2,1,1,1,1,1,3,2,1,3,2,1,1,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,1,1,2,1,2,1,2,1,1,3,2,1,2,1,1,2,1,3,2,1,3,2,1,3,2,1,2,1,1,1,2,1,2,1,2,1,2,1,3,2,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,1,2,1,1,1,1,3,2,1,3,2,1,2,1,2,1,1,1,2,1,1,1,1,2,1,1,3,2,1,3,2,1,2,1,2,1,1,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,3,2,1,3,2,1,2,1,2,1,1,2,1,1,2,1,1,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,1,3,2,1,2,1,1,1,2,1,1,3,2,1,3,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,1,2,1,2,1,1,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,1,1,1,2,1,1,2,1,3,2,1,3,2,1,3,2,1,1,2,1,2,1,1,1,2,1,1,1,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,1,1,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,1,2,1,2,1,1,2,1,1,1,1,2,1,3,2,1,3,2,1,1,3,2,1,2,1,1,2,1,2,1,1,1,3,2,1,3,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,1,2,1,3,2,1,3,2,1,2,1,3,2,1,3,2,1,2,1,3,2,1,2,1,2,1,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,3,2,1,2,1,2,1,1,1,2,1,1,3,2,1,3,2,1,2,1,1,1,1,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,1,2,1,1,1,2,1,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,1,1,2,1,2,1,1,1,1,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,2,1,1,1,2,1,3,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,1,1,2,1,2,1,2,1,3,2,1,3,2,1,1,2,1,2,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,1,2,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,1,2,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,1,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,1,2,1,1,2,1,1,1,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,1,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,1,1,1,2,1,1,2,1,2,1,2,1,1,3,2,1,1,2,1,1,1,2,1,1,2,1,2,1,2,1,1,3,2,1,1,1,3,2,1,1,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,1,2,1,1,2,1,1,1,1,2,1,3,2,1,3,2,1,2,1,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,3,2,1,1,2,1,1,2,1,1,2,1,1,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,3,2,1,2,1,2,1,1,2,1,1,2,1,2,1,1,2,1,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,1,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,2,1,3,2,1,2,1,2,1,1,1,2,1,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,2,1,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,3,2,1,1,2,1,2,1,1,2,1,2,1,1,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,1,2,1,2,1,3,2,1,2,1,2,1,1,3,2,1,1,1,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,1,3,2,1,1,2,1,1,1,2,1,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,1,1,1,1,1,2,1,2,1,3,2,1,2,1,2,1,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,2,1,3,2,1,2,1,4,3,2,1,4,3,2,1,2,1,2,1,3,2,1,2,1,1,2,1,3,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,3,2,1,1,1,2,1,2,1,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,1,3,2,1,1,3,2,1,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,3,2,1,2,1,2,1,2,1,1,1,1,2,1,3,2,1,3,2,1,2,1,1,2,1,1,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,1,1,1,2,1,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,1,3,2,1,1,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,3,2,1,2,1,1,1,2,1,2,1,2,1,1,3,2,1,1,2,1,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,3,2,1,1,1,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,1,1,2,1,2,1,1,1,1,2,1,3,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,3,2,1,1,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,1,1,1,2,1,1,2,1,2,1,2,1,1,2,1,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,1,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,1,2,1,1,1,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,3,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,3,2,1,2,1,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,2,1,3,2,1,1,2,1,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,1,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,3,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,1,3,2,1,1,1,2,1,1,2,1,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,1,2,1,1,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,1,1,2,1,2,1,2,1,1,3,2,1,3,2,1,3,2,1,1,1,2,1,2,1,1,2,1,1,1,3,2,1,1,3,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,1,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,1,2,1,2,1,2,1,1,2,1,1,1,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,3,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,3,2,1,3,2,1,3,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,1,1,2,1,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,1,2,1,1,2,1,1,3,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,3,2,1,1,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,1,1,2,1,2,1,1,1,1,2,1,1,2,1,1,2,1,3,2,1,1,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,1,1,1,1,2,1,3,2,1,1,2,1,1,2,1,1,1,1,1,3,2,1,1,1,2,1,2,1,1,1,2,1,2,1,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,1,1,2,1,2,1,1,1,2,1,1,1,2,1,1,2,1,1,1,2,1,1,1,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,1,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,2,1,1,1,1,2,1,2,1,1,3,2,1,1,2,1,3,2,1,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,1,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,1,2,1,1,1,3,2,1,1,3,2,1,1,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1],"label":["findCenvVar","findVar","cmpComplexAssign","h","tryInline","cmpCall","cmp","h","tryInline","cmpCall","cmp","cmpForBody","h","tryInline","cmpCall","cmp","h","tryInline","cmpCall","cmp","genCode","cmpfun","compiler:::tryCmpfun","eval","eval","eval.parent","local","rowSums","rowSums","rowSums","rowSums","rowSums","rowSums","rowSums","rowSums","rowMeans","rowMeans","rowMeans","rowMeans","rowMeans","rowMeans","<GC>","aperm.default","apply","aperm.default","apply","aperm.default","apply","aperm.default","apply","aperm.default","apply","aperm.default","apply","aperm.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","apply","apply","length","local","apply","FUN","apply","FUN","apply","is.na","local","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","mean.default","apply","apply","<GC>","apply","<GC>","apply","FUN","apply","length","local","mean.default","apply","apply","FUN","apply","FUN","apply","is.na","local","length","local","apply","apply","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","mean.default","apply","apply","FUN","apply","apply","apply","apply","FUN","apply","FUN","apply","<GC>","apply","<GC>","apply","length","local","FUN","apply","FUN","apply","length","local","FUN","apply","apply","apply","FUN","apply","is.numeric","local","apply","FUN","apply","apply","<GC>","apply","is.numeric","local","FUN","apply","apply","mean.default","apply","FUN","apply","FUN","apply","apply","apply","apply","apply","apply","apply","<GC>","length","local","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","length","local","apply","apply","mean.default","apply","<GC>","apply","<GC>","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","apply","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","apply","<GC>","mean.default","apply","FUN","apply","is.na","local","mean.default","apply","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","apply","apply","<GC>","apply","<GC>","apply","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","length","local","apply","<GC>","length","local","<GC>","length","local","mean.default","apply","apply","mean.default","apply","isTRUE","mean.default","apply","apply","mean.default","apply","apply","apply","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","isTRUE","mean.default","apply","is.numeric","local","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","is.numeric","local","<GC>","is.numeric","local","is.na","local","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","length","local","isTRUE","mean.default","apply","FUN","apply","<GC>","apply","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","is.numeric","local","FUN","apply","apply","FUN","apply","apply","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","is.numeric","local","apply","apply","FUN","apply","apply","apply","apply","FUN","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","is.na","local","apply","apply","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","mean.default","apply","<GC>","apply","<GC>","apply","apply","is.numeric","local","FUN","apply","is.na","local","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","apply","FUN","apply","apply","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","mean.default","apply","apply","FUN","apply","is.numeric","local","mean.default","apply","mean.default","apply","FUN","apply","apply","FUN","apply","<GC>","apply","<GC>","apply","apply","apply","isTRUE","mean.default","apply","mean.default","apply","apply","apply","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","apply","apply","length","local","FUN","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","is.numeric","local","mean.default","apply","apply","apply","mean.default","apply","mean.default","apply","mean.default","apply","<GC>","length","local","<GC>","length","local","FUN","apply","apply","apply","apply","mean.default","apply","apply","mean.default","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","apply","apply","apply","<GC>","FUN","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","is.na","local","length","local","<GC>","mean.default","apply","<GC>","mean.default","apply","length","local","FUN","apply","mean.default","apply","apply","apply","FUN","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","apply","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","apply","is.numeric","local","FUN","apply","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","length","local","is.na","local","FUN","apply","isTRUE","mean.default","apply","apply","<GC>","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","mean.default","apply","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","is.numeric","local","isTRUE","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","is.numeric","local","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","apply","apply","FUN","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","apply","apply","apply","apply","FUN","apply","mean.default","apply","<GC>","apply","<GC>","apply","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","apply","mean.default","apply","apply","apply","mean.default","apply","apply","<GC>","is.na","local","<GC>","is.na","local","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","apply","is.na","local","mean.default","apply","apply","apply","apply","apply","FUN","apply","apply","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","is.na","local","is.numeric","local","FUN","apply","FUN","apply","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","isTRUE","mean.default","apply","is.numeric","local","mean.default","apply","FUN","apply","apply","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","apply","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","FUN","apply","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","isTRUE","mean.default","apply","apply","mean.default","apply","apply","length","local","FUN","apply","isTRUE","mean.default","apply","<GC>","apply","<GC>","apply","length","local","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","apply","apply","is.numeric","local","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","is.na","local","is.na","local","<GC>","apply","<GC>","apply","<GC>","apply","length","local","mean.default","apply","apply","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","apply","FUN","apply","mean.default","apply","apply","apply","mean.default","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","apply","mean.default","apply","apply","FUN","apply","apply","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","is.numeric","local","FUN","apply","mean.default","apply","FUN","apply","is.na","local","apply","mean.default","apply","mean.default","apply","length","local","apply","apply","FUN","apply","length","local","FUN","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","apply","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","apply","apply","mean.default","apply","FUN","apply","apply","apply","apply","is.na","local","apply","<GC>","apply","<GC>","apply","<GC>","apply","apply","isTRUE","mean.default","apply","apply","is.numeric","local","apply","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","apply","isTRUE","mean.default","apply","apply","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","apply","is.na","local","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","FUN","apply","length","local","FUN","apply","FUN","apply","apply","mean.default","apply","apply","length","local","FUN","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","apply","FUN","apply","apply","FUN","apply","apply","mean.default","apply","apply","apply","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","apply","mean.default","apply","apply","length","local","apply","FUN","apply","apply","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","mean.default","apply","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","apply","FUN","apply","FUN","apply","FUN","apply","apply","is.na","local","mean.default","apply","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","<GC>","apply","apply","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","isTRUE","mean.default","apply","mean.default","apply","length","local","apply","FUN","apply","mean.default","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","apply","FUN","apply","apply","FUN","apply","mean.default","apply","apply","FUN","apply","apply","mean.default","apply","FUN","apply","apply","apply","mean.default","apply","mean.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","mean.default","apply","apply","FUN","apply","length","local","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","length","local","isTRUE","mean.default","apply","apply","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","apply","mean.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","is.na","local","apply","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","apply","apply","is.na","local","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","is.na","local","apply","mean.default","apply","mean.default","apply","is.numeric","local","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","is.numeric","local","apply","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","mean.default","apply","apply","is.numeric","local","mean.default","apply","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","mean.default","apply","isTRUE","mean.default","apply","apply","<GC>","apply","<GC>","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","mean.default","apply","FUN","apply","<GC>","apply","<GC>","apply","<GC>","apply","is.na","local","is.numeric","local","apply","mean.default","apply","mean.default","apply","apply","mean.default","apply","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","apply","FUN","apply","is.numeric","local","apply","isTRUE","mean.default","apply","apply","mean.default","apply","apply","apply","FUN","apply","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","apply","apply","apply","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","apply","apply","mean.default","apply","mean.default","apply","apply","<GC>","apply","<GC>","apply","<GC>","apply","mean.default","apply","mean.default","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","length","local","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","FUN","apply","length","local","isTRUE","mean.default","apply","FUN","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","apply","FUN","apply","apply","FUN","apply","mean.default","apply","FUN","apply","is.numeric","local","mean.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","apply","mean.default","apply","is.na","local","is.numeric","local","FUN","apply","mean.default","apply","apply","apply","apply","apply","apply","FUN","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","mean.default","apply","apply","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","apply","FUN","apply","is.numeric","local","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","is.na","local","FUN","apply","FUN","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","apply","<GC>","is.na","local","<GC>","is.na","local","<GC>","is.na","local","FUN","apply","mean.default","apply","is.numeric","local","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","isTRUE","mean.default","apply","apply","apply","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","<GC>","apply","<GC>","apply","FUN","apply","is.na","local","FUN","apply","is.na","local","apply","mean.default","apply","is.numeric","local","FUN","apply","FUN","apply","apply","apply","apply","FUN","apply","FUN","apply","mean.default","apply","<GC>","apply","<GC>","apply","length","local","FUN","apply","length","local","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","length","local","apply","FUN","apply","mean.default","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","FUN","apply","length","local","mean.default","apply","apply","isTRUE","mean.default","apply","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","is.numeric","local","FUN","apply","is.numeric","local","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","apply","apply","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","apply","FUN","apply","apply","apply","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","length","local","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","apply","FUN","apply","apply","apply","apply","mean.default","apply","apply","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","length","local","is.na","local","mean.default","apply","apply","is.numeric","local","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","apply","FUN","apply","<GC>","apply","<GC>","apply","<GC>","apply","apply","is.numeric","local","apply","mean.default","apply","apply","isTRUE","mean.default","apply","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","FUN","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","mean.default","apply","apply","FUN","apply","apply","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","apply","length","local","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","apply","mean.default","apply","mean.default","apply","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","is.na","local","FUN","apply","FUN","apply","apply","FUN","apply","is.na","local","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","apply","mean.default","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","is.na","local","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","apply","apply","FUN","apply","apply","FUN","apply","mean.default","apply","FUN","apply","apply","FUN","apply","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","is.numeric","local","apply","apply","mean.default","apply","apply","FUN","apply","is.na","local","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","apply","apply","apply","FUN","apply","apply","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","mean.default","apply","is.numeric","local","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","apply","length","local","FUN","apply","isTRUE","mean.default","apply","apply","mean.default","apply","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","apply","FUN","apply","apply","apply","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","mean.default","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","is.na","local","mean.default","apply","FUN","apply","<GC>","apply","<GC>","apply","<GC>","apply","is.na","local","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","apply","FUN","apply","length","local","is.numeric","local","mean.default","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","apply","is.na","local","apply","mean.default","apply","apply","is.na","local","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","apply","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","apply","<GC>","apply","<GC>","apply","<GC>","apply","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","apply","mean.default","apply","FUN","apply","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","apply","<GC>","length","local","<GC>","length","local","<GC>","length","local","apply","FUN","apply","mean.default","apply","length","local","FUN","apply","FUN","apply","apply","apply","apply","mean.default","apply","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","length","local","apply","FUN","apply","length","local","is.na","local","FUN","apply","FUN","apply","length","local","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","apply","mean.default","apply","apply","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","mean.default","apply","is.numeric","local","apply","isTRUE","mean.default","apply","apply","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","is.na","local","FUN","apply","mean.default","apply","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","apply","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","is.na","local","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","apply","<GC>","is.na","local","<GC>","is.na","local","<GC>","is.na","local","apply","apply","FUN","apply","is.na","local","FUN","apply","FUN","apply","FUN","apply","length","local","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","is.na","local","FUN","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","apply","is.na","local","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","length","local","apply","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","mean.default","apply","apply","apply","FUN","apply","apply","mean.default","apply","apply","FUN","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","is.numeric","local","mean.default","apply","FUN","apply","apply","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","length","local","apply","apply","mean.default","apply","apply","FUN","apply","apply","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","apply","apply","is.na","local","mean.default","apply","is.na","local","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","is.numeric","local","isTRUE","mean.default","apply","apply","length","local","isTRUE","mean.default","apply","FUN","apply","apply","mean.default","apply","is.na","local","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","apply","apply","mean.default","apply","mean.default","apply","apply","apply","apply","mean.default","apply","apply","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","apply","apply","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","FUN","apply","apply","apply","apply","apply","isTRUE","mean.default","apply","apply","apply","is.na","local","FUN","apply","apply","apply","is.numeric","local","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","apply","FUN","apply","length","local","apply","apply","length","local","apply","apply","mean.default","apply","apply","mean.default","apply","apply","apply","mean.default","apply","apply","apply","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","length","local","FUN","apply","mean.default","apply","apply","apply","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","FUN","apply","isTRUE","mean.default","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","is.na","local","apply","FUN","apply","apply","FUN","apply","mean.default","apply","length","local","FUN","apply","apply","apply","FUN","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","is.na","local","FUN","apply","mean.default","apply","apply","apply","apply","FUN","apply","apply","mean.default","apply","apply","FUN","apply","FUN","apply","FUN","apply","is.numeric","local","isTRUE","mean.default","apply","mean.default","apply","apply","FUN","apply","FUN","apply","mean.default","apply","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","is.numeric","local","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","apply","apply","mean.default","apply","apply","apply","isTRUE","mean.default","apply","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","length","local","mean.default","apply","apply","FUN","apply","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","length","local","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","apply","any","local","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply"],"filenum":[null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null],"linenum":[null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null],"memalloc":[115.400146484375,115.400146484375,115.400146484375,115.400146484375,115.400146484375,115.400146484375,115.400146484375,115.400146484375,115.400146484375,115.400146484375,115.400146484375,115.400146484375,115.400146484375,115.400146484375,115.400146484375,115.400146484375,115.400146484375,115.400146484375,115.400146484375,115.400146484375,115.400146484375,115.400146484375,115.400146484375,115.400146484375,115.400146484375,115.400146484375,115.400146484375,130.7246780395508,130.7246780395508,130.7246780395508,130.7246780395508,130.7246780395508,130.7246780395508,130.7246780395508,130.7246780395508,145.9836196899414,145.9836196899414,145.9836196899414,145.9836196899414,145.9836196899414,145.9836196899414,145.9839859008789,145.9839859008789,145.9839859008789,176.2697525024414,176.2697525024414,176.2697525024414,176.2697525024414,176.2697525024414,176.2697525024414,176.2697525024414,176.2697525024414,176.2697525024414,176.2697525024414,176.2697525024414,176.2697525024414,176.2697982788086,176.2697982788086,176.269645690918,176.269645690918,176.269645690918,176.269645690918,176.269645690918,176.269645690918,176.269645690918,176.269645690918,176.269645690918,176.269645690918,176.269645690918,176.269645690918,176.269645690918,176.269645690918,176.269645690918,176.269645690918,176.269645690918,176.269645690918,176.269645690918,176.269645690918,176.269645690918,176.269645690918,176.2694625854492,176.2694625854492,191.5282516479492,191.7243576049805,191.9240341186523,191.9240341186523,192.1322250366211,192.2993392944336,192.2993392944336,192.506103515625,192.506103515625,192.7294464111328,192.7294464111328,192.9701690673828,192.9701690673828,193.2112884521484,193.2112884521484,193.4468002319336,193.4468002319336,193.4468002319336,193.6824264526367,193.9185028076172,193.9185028076172,194.1531295776367,194.3501892089844,194.3501892089844,194.3501892089844,194.3501892089844,191.7405014038086,191.7405014038086,191.94970703125,191.94970703125,192.1781845092773,192.1781845092773,192.4233322143555,192.6761245727539,192.6761245727539,192.9274215698242,192.9274215698242,193.1755599975586,193.1755599975586,193.4158096313477,193.4158096313477,193.6299133300781,193.8530426025391,194.0654373168945,194.2648849487305,194.408073425293,194.408073425293,194.408073425293,194.408073425293,194.408073425293,194.408073425293,191.867057800293,191.867057800293,192.0668869018555,192.0668869018555,192.2678756713867,192.4771499633789,192.4771499633789,192.6708908081055,192.6708908081055,192.8823471069336,192.8823471069336,193.1064758300781,193.3110275268555,193.3110275268555,193.5382537841797,193.7560882568359,193.9766616821289,194.2036590576172,194.2036590576172,194.3833618164062,194.3833618164062,194.4833679199219,194.4833679199219,194.4833679199219,194.4833679199219,191.9820785522461,191.9820785522461,192.1826400756836,192.1826400756836,192.3908081054688,192.3908081054688,192.6048431396484,192.6048431396484,192.832763671875,192.832763671875,193.0699081420898,193.3183059692383,193.5627593994141,193.5627593994141,193.8058242797852,193.8058242797852,194.0487594604492,194.2922058105469,194.2922058105469,194.5365295410156,194.5574188232422,194.5574188232422,192.0429534912109,192.0429534912109,192.2445602416992,192.2445602416992,192.4516906738281,192.6669692993164,192.6669692993164,192.9013671875,192.9013671875,193.1426620483398,193.1426620483398,193.3892593383789,193.6333465576172,193.8783111572266,194.1214065551758,194.3670120239258,194.6119079589844,194.6303787231445,194.6303787231445,194.6303787231445,192.1590118408203,192.1590118408203,192.3520431518555,192.3520431518555,192.3520431518555,192.5587463378906,192.5587463378906,192.7800216674805,192.7800216674805,193.0172500610352,193.0172500610352,193.261360168457,193.261360168457,193.50634765625,193.50634765625,193.7476425170898,193.7476425170898,193.9904403686523,194.232421875,194.4765319824219,194.4765319824219,194.7020874023438,194.7020874023438,194.7020874023438,194.7020874023438,192.2941665649414,192.2941665649414,192.2941665649414,192.4950714111328,192.4950714111328,192.7030029296875,192.7030029296875,192.9272613525391,192.9272613525391,193.1690902709961,193.1690902709961,193.1690902709961,193.4147415161133,193.4147415161133,193.6605834960938,193.6605834960938,193.9054794311523,194.14892578125,194.14892578125,194.3905563354492,194.3905563354492,194.6336517333984,194.7726287841797,194.7726287841797,194.7726287841797,194.7726287841797,192.4741668701172,192.6818237304688,192.9049606323242,193.1430969238281,193.1430969238281,193.3877410888672,193.3877410888672,193.6340789794922,193.6340789794922,193.8760604858398,193.8760604858398,194.1204833984375,194.35107421875,194.35107421875,194.5936965942383,194.8214111328125,194.8420639038086,194.8420639038086,194.8420639038086,192.4537353515625,192.4537353515625,192.6495971679688,192.6495971679688,192.8526458740234,192.8526458740234,193.0425262451172,193.25390625,193.25390625,193.4486999511719,193.4486999511719,193.6657485961914,193.6657485961914,193.895133972168,193.895133972168,194.1063690185547,194.3392639160156,194.3392639160156,194.566291809082,194.784309387207,194.910400390625,194.910400390625,194.910400390625,194.910400390625,192.6662063598633,192.6662063598633,192.8700714111328,192.8700714111328,192.8700714111328,193.0618591308594,193.0618591308594,193.0618591308594,193.2728271484375,193.4917526245117,193.4917526245117,193.7199020385742,193.7199020385742,193.7199020385742,193.9327697753906,193.9327697753906,194.158561706543,194.158561706543,194.3972091674805,194.3972091674805,194.6148300170898,194.6148300170898,194.8594131469727,194.9775314331055,194.9775314331055,194.9775314331055,194.9775314331055,194.9775314331055,194.9775314331055,192.7865905761719,192.7865905761719,192.9937438964844,193.1972274780273,193.1972274780273,193.4100494384766,193.4100494384766,193.4100494384766,193.6295394897461,193.8608322143555,193.8608322143555,194.102165222168,194.3454818725586,194.5898132324219,194.8324279785156,195.0437164306641,195.0437164306641,195.0437164306641,195.0437164306641,195.0437164306641,195.0437164306641,192.8101959228516,193.0110092163086,193.2181777954102,193.2181777954102,193.4375381469727,193.4375381469727,193.6708221435547,193.9148330688477,193.9148330688477,194.1607284545898,194.4024658203125,194.4024658203125,194.6452178955078,194.6452178955078,194.8895874023438,194.8895874023438,195.108757019043,195.108757019043,195.108757019043,195.108757019043,195.108757019043,195.108757019043,192.9245300292969,193.1196670532227,193.3240203857422,193.3240203857422,193.5158538818359,193.5158538818359,193.7320404052734,193.7320404052734,193.9189529418945,194.1361465454102,194.1361465454102,194.1361465454102,194.3670654296875,194.3670654296875,194.584358215332,194.8203048706055,194.8203048706055,195.0203704833984,195.0203704833984,195.0203704833984,195.1726989746094,195.1726989746094,195.1726989746094,195.1726989746094,195.1726989746094,195.1726989746094,193.0519943237305,193.0519943237305,193.2497863769531,193.4231567382812,193.6238327026367,193.6238327026367,193.8318099975586,193.8318099975586,194.056266784668,194.056266784668,194.2920455932617,194.2920455932617,194.5273818969727,194.5273818969727,194.5273818969727,194.7677841186523,194.7677841186523,194.9908142089844,194.9908142089844,194.9908142089844,195.2231216430664,195.2231216430664,195.2357559204102,195.2357559204102,193.0956726074219,193.2870483398438,193.2870483398438,193.494987487793,193.494987487793,193.7108459472656,193.7108459472656,193.9465560913086,193.9465560913086,194.1927032470703,194.1927032470703,194.4396133422852,194.4396133422852,194.6841888427734,194.6841888427734,194.9279251098633,195.1680068969727,195.1680068969727,195.1680068969727,195.2976684570312,195.2976684570312,195.2976684570312,195.2976684570312,195.2976684570312,195.2976684570312,193.2989501953125,193.2989501953125,193.4991683959961,193.709342956543,193.709342956543,193.9372634887695,193.9372634887695,194.1792449951172,194.4238586425781,194.4238586425781,194.6495208740234,194.8947372436523,195.1398696899414,195.3586349487305,195.3586349487305,195.3586349487305,195.3586349487305,195.3586349487305,195.3586349487305,193.3107452392578,193.3107452392578,193.4941329956055,193.4941329956055,193.7010803222656,193.9197158813477,194.1581878662109,194.1581878662109,194.4042053222656,194.6512756347656,194.8965911865234,195.1418380737305,195.1418380737305,195.384765625,195.418586730957,195.418586730957,195.418586730957,195.418586730957,195.418586730957,195.418586730957,193.512336730957,193.512336730957,193.7031097412109,193.7031097412109,193.8913650512695,194.076286315918,194.2895965576172,194.5048294067383,194.5048294067383,194.7388153076172,194.971809387207,194.971809387207,195.1908264160156,195.1908264160156,195.4267959594727,195.4267959594727,195.4775619506836,195.4775619506836,195.4775619506836,195.4775619506836,193.5880508422852,193.7749710083008,193.7749710083008,193.9734115600586,193.9734115600586,194.1804885864258,194.1804885864258,194.4151382446289,194.6585159301758,194.6585159301758,194.9043121337891,194.9043121337891,195.1482315063477,195.1482315063477,195.3911895751953,195.5356597900391,195.5356597900391,195.5356597900391,195.5356597900391,195.5356597900391,195.5356597900391,193.6508941650391,193.6508941650391,193.8442459106445,193.8442459106445,194.04541015625,194.2669906616211,194.2669906616211,194.5070877075195,194.7549819946289,194.7549819946289,195.0046691894531,195.2519149780273,195.4965515136719,195.4965515136719,195.5927047729492,195.5927047729492,195.5927047729492,195.5927047729492,195.5927047729492,195.5927047729492,195.5927047729492,195.5927047729492,195.5927047729492,195.5927047729492,195.5927047729492,195.5927047729492,195.5927047729492,195.5927047729492,195.5927047729492,195.5927047729492,195.5927047729492,195.5927047729492,195.5927047729492,195.5927047729492,195.5927047729492,195.5927047729492,195.5927047729492,195.5927047729492,195.5927047729492,195.5927047729492,195.5927047729492,193.63671875,193.63671875,193.8066329956055,193.8066329956055,193.9893188476562,194.1838684082031,194.1838684082031,194.3897323608398,194.3897323608398,194.6123886108398,194.6123886108398,194.8517761230469,194.8517761230469,195.0993118286133,195.0993118286133,195.3442764282227,195.589241027832,195.589241027832,195.6486206054688,195.6486206054688,195.6486206054688,195.6486206054688,193.8705673217773,194.068229675293,194.2796325683594,194.2796325683594,194.2796325683594,194.5123062133789,194.5123062133789,194.7575988769531,195.0049133300781,195.2521057128906,195.2521057128906,195.4992828369141,195.7039566040039,195.7039566040039,195.7039566040039,195.7039566040039,195.7039566040039,195.7039566040039,193.8631210327148,193.8631210327148,194.0551605224609,194.0551605224609,194.2556610107422,194.4788208007812,194.7213973999023,194.7213973999023,194.9686279296875,194.9686279296875,195.2170944213867,195.2170944213867,195.4638137817383,195.4638137817383,195.7075500488281,195.7075500488281,195.7583160400391,195.7583160400391,195.7583160400391,195.7583160400391,195.7583160400391,195.7583160400391,194.0624771118164,194.2534332275391,194.2534332275391,194.4631271362305,194.4631271362305,194.6919784545898,194.9365921020508,195.1829452514648,195.1829452514648,195.4283981323242,195.4283981323242,195.6744232177734,195.6744232177734,195.8118438720703,195.8118438720703,195.8118438720703,195.8118438720703,195.8118438720703,195.8118438720703,194.0648498535156,194.0648498535156,194.24267578125,194.4441299438477,194.6673278808594,194.9092559814453,194.9092559814453,195.1562118530273,195.4037780761719,195.4037780761719,195.6502990722656,195.6502990722656,195.6502990722656,195.8645477294922,195.8645477294922,195.8645477294922,195.8645477294922,195.8645477294922,195.8645477294922,194.0964965820312,194.2849044799805,194.2849044799805,194.4809112548828,194.4809112548828,194.6946258544922,194.9305953979492,195.1752548217773,195.1752548217773,195.4217987060547,195.6663665771484,195.9024276733398,195.9163055419922,195.9163055419922,195.9163055419922,194.1417465209961,194.1417465209961,194.3105392456055,194.5028610229492,194.5028610229492,194.7134552001953,194.7134552001953,194.9456024169922,194.9456024169922,195.1923065185547,195.1923065185547,195.439567565918,195.439567565918,195.6826171875,195.6826171875,195.9234008789062,195.9234008789062,195.9672698974609,195.9672698974609,195.9672698974609,195.9672698974609,195.9672698974609,195.9672698974609,194.2889175415039,194.2889175415039,194.4580230712891,194.4580230712891,194.6233825683594,194.6233825683594,194.7970428466797,194.9949798583984,195.2131118774414,195.2131118774414,195.439811706543,195.439811706543,195.6725082397461,195.6725082397461,195.9097595214844,195.9097595214844,195.9097595214844,196.0174789428711,196.0174789428711,196.0174789428711,196.0174789428711,196.0174789428711,196.0174789428711,194.3976211547852,194.3976211547852,194.3976211547852,194.5799942016602,194.7548675537109,194.9633483886719,194.9633483886719,195.1679382324219,195.4099349975586,195.4099349975586,195.6271591186523,195.6271591186523,195.8475570678711,195.8475570678711,196.0667495727539,196.0667495727539,196.0667495727539,196.0667495727539,196.0667495727539,196.0667495727539,194.3713455200195,194.5480499267578,194.5480499267578,194.7276840209961,194.7276840209961,194.9262008666992,195.1284561157227,195.1284561157227,195.3570022583008,195.5925903320312,195.8262176513672,196.0658645629883,196.0658645629883,196.115348815918,196.115348815918,196.115348815918,196.115348815918,196.115348815918,196.115348815918,194.5836868286133,194.7654342651367,194.7654342651367,194.7654342651367,194.9538726806641,194.9538726806641,195.1673202514648,195.3878479003906,195.3878479003906,195.6227874755859,195.6227874755859,195.858528137207,196.0978012084961,196.1630935668945,196.1630935668945,196.1630935668945,196.1630935668945,196.1630935668945,196.1630935668945,194.6457824707031,194.6457824707031,194.8324890136719,194.8324890136719,194.8324890136719,195.0330810546875,195.0330810546875,195.2515411376953,195.2515411376953,195.4859619140625,195.4859619140625,195.7281494140625,195.7281494140625,195.9704360961914,195.9704360961914,195.9704360961914,196.2043914794922,196.2100601196289,196.2100601196289,194.5943984985352,194.5943984985352,194.7795791625977,194.7795791625977,194.9715194702148,194.9715194702148,194.9715194702148,195.1838226318359,195.4131698608398,195.4131698608398,195.6525726318359,195.6525726318359,195.8994827270508,196.1207046508789,196.1207046508789,196.2563323974609,196.2563323974609,196.2563323974609,196.2563323974609,196.2563323974609,196.2563323974609,194.6769485473633,194.6769485473633,194.8304824829102,194.8304824829102,194.8304824829102,195.0066528320312,195.0066528320312,195.0066528320312,195.1780624389648,195.1780624389648,195.3555068969727,195.3555068969727,195.3555068969727,195.5545120239258,195.5545120239258,195.7322769165039,195.7322769165039,195.9447174072266,196.1552886962891,196.1552886962891,196.3018264770508,196.3018264770508,196.3018264770508,196.3018264770508,196.3018264770508,196.3018264770508,194.7691879272461,194.7691879272461,194.9486999511719,194.9486999511719,195.1337814331055,195.1337814331055,195.3296279907227,195.3296279907227,195.5502471923828,195.5502471923828,195.7523498535156,195.7523498535156,195.9743118286133,195.9743118286133,196.2036590576172,196.2036590576172,196.3465576171875,196.3465576171875,196.3465576171875,196.3465576171875,196.3465576171875,196.3465576171875,194.8328323364258,194.9923400878906,195.1733245849609,195.1733245849609,195.3554229736328,195.3554229736328,195.5691909790039,195.5691909790039,195.7809906005859,195.7809906005859,195.9933090209961,195.9933090209961,196.2203216552734,196.2203216552734,196.3905944824219,196.3905944824219,196.3905944824219,196.3905944824219,196.3905944824219,196.3905944824219,194.8914184570312,194.8914184570312,195.0634002685547,195.0634002685547,195.0634002685547,195.2553863525391,195.2553863525391,195.4468231201172,195.4468231201172,195.6656723022461,195.8889846801758,196.1150131225586,196.1150131225586,196.3539962768555,196.4338912963867,196.4338912963867,196.4338912963867,196.4338912963867,196.4338912963867,196.4338912963867,195.0610046386719,195.0610046386719,195.2475891113281,195.4458084106445,195.6705093383789,195.9115219116211,196.1521682739258,196.1521682739258,196.3886642456055,196.3886642456055,196.4765243530273,196.4765243530273,196.4765243530273,196.4765243530273,195.1118850708008,195.3010101318359,195.3010101318359,195.5044250488281,195.7291488647461,195.7291488647461,195.9699325561523,195.9699325561523,196.2140350341797,196.2140350341797,196.4524612426758,196.4524612426758,196.518440246582,196.518440246582,196.518440246582,196.518440246582,196.518440246582,196.518440246582,195.1797409057617,195.1797409057617,195.3691101074219,195.5548934936523,195.5548934936523,195.7521743774414,195.957763671875,196.1650466918945,196.1650466918945,196.3722381591797,196.5596771240234,196.5596771240234,196.5596771240234,196.5596771240234,196.5596771240234,196.5596771240234,195.1544799804688,195.3297119140625,195.3297119140625,195.5143508911133,195.5143508911133,195.7136535644531,195.7136535644531,195.9221878051758,195.9221878051758,196.1447982788086,196.1447982788086,196.3630905151367,196.3630905151367,196.5820846557617,196.5820846557617,196.6002883911133,196.6002883911133,196.6002883911133,196.6002883911133,196.6002883911133,196.6002883911133,196.6002883911133,196.6002883911133,196.6002883911133,196.6002883911133,196.6002883911133,196.6002883911133,196.6002883911133,196.6002883911133,196.6002883911133,196.6002883911133,196.6002883911133,196.6002883911133,196.6002883911133,196.6002883911133,196.6002883911133,196.6002883911133,196.6002883911133,196.6002883911133,196.6002883911133,196.6002883911133,196.6002883911133,196.6002883911133,196.6002883911133,196.6002883911133,196.6002883911133,196.6002883911133,196.6002883911133,196.6002883911133,196.6002883911133,196.6002883911133,196.6002883911133,196.6002883911133,196.6002883911133,196.6002883911133,196.6002883911133,196.6002883911133,196.6002883911133,196.6002883911133,196.6002883911133,196.6002883911133,196.6002883911133,196.6002883911133,196.6002883911133,196.6002883911133,196.6002883911133,196.6002883911133,196.6002883911133,196.6002883911133,196.6002883911133,196.6002883911133,196.6002883911133,196.6002883911133,196.6002883911133,196.6002883911133,196.6002883911133,196.6002883911133,196.6002883911133,196.6002883911133,195.2029113769531,195.2029113769531,195.2029113769531,195.2029113769531,195.3561630249023,195.3561630249023,195.5460510253906,195.5460510253906,195.5460510253906,195.7529296875,195.7529296875,195.7529296875,195.9626312255859,195.9626312255859,195.9626312255859,196.184814453125,196.4098815917969,196.619255065918,196.619255065918,196.8533477783203,196.8533477783203,197.0842361450195,197.309440612793,197.5485000610352,197.7545547485352,197.9384536743164,197.9384536743164,198.1245346069336,198.3035125732422,198.4871826171875,198.4871826171875,198.6507263183594,198.6507263183594,198.8356628417969,198.8356628417969,198.9990463256836,198.9990463256836,199.1752471923828,199.1752471923828,199.3458099365234,199.3458099365234,199.5279312133789,199.5279312133789,199.7163925170898,199.7163925170898,199.880973815918,199.880973815918,200.0561141967773,200.0561141967773,200.2229309082031,200.2687911987305,200.2687911987305,200.2687911987305,200.2687911987305,200.2687911987305,200.2687911987305,195.4917602539062,195.4917602539062,195.6860198974609,195.6860198974609,195.8914489746094,195.8914489746094,196.1206741333008,196.1206741333008,196.3526382446289,196.3526382446289,196.5719528198242,196.5719528198242,196.5719528198242,196.80517578125,196.80517578125,196.80517578125,197.0503082275391,197.0503082275391,197.0503082275391,197.2893676757812,197.5076065063477,197.5076065063477,197.7402496337891,197.7402496337891,197.9769668579102,197.9769668579102,198.201789855957,198.201789855957,198.4102630615234,198.4102630615234,198.6375503540039,198.8685913085938,198.8685913085938,198.8685913085938,199.1002044677734,199.1002044677734,199.3334197998047,199.3334197998047,199.5722351074219,199.5722351074219,199.8119888305664,200.0189361572266,200.2277984619141,200.2277984619141,200.4073333740234,200.4073333740234,200.4073333740234,200.4073333740234,200.4073333740234,200.4073333740234,200.4073333740234,200.4073333740234,200.4073333740234,195.8055114746094,196.0134658813477,196.0134658813477,196.2349090576172,196.2349090576172,196.458869934082,196.458869934082,196.6720809936523,196.6720809936523,196.89892578125,196.89892578125,196.89892578125,197.1354904174805,197.1354904174805,197.3752136230469,197.3752136230469,197.5925827026367,197.5925827026367,197.8209075927734,197.8209075927734,198.0460052490234,198.0460052490234,198.2783584594727,198.2783584594727,198.5064849853516,198.5064849853516,198.7343826293945,198.9658584594727,198.9658584594727,199.2092361450195,199.2092361450195,199.4400405883789,199.6549301147461,199.8640975952148,200.0740280151367,200.0740280151367,200.275764465332,200.275764465332,200.4731979370117,200.4731979370117,200.5437164306641,200.5437164306641,200.5437164306641,200.5437164306641,200.5437164306641,200.5437164306641,195.9042892456055,196.0986480712891,196.0986480712891,196.3039703369141,196.3039703369141,196.5145950317383,196.7263259887695,196.9459228515625,197.1896514892578,197.1896514892578,197.4340209960938,197.4340209960938,197.675895690918,197.675895690918,197.9060668945312,197.9060668945312,198.1296691894531,198.1296691894531,198.3742370605469,198.3742370605469,198.617431640625,198.617431640625,198.8362197875977,199.0602111816406,199.0602111816406,199.3018188476562,199.3018188476562,199.3018188476562,199.515869140625,199.7413787841797,199.7413787841797,199.9814758300781,200.1848373413086,200.1848373413086,200.4187622070312,200.4187622070312,200.6119155883789,200.6119155883789,200.6119155883789,200.6777648925781,200.6777648925781,200.6777648925781,200.6777648925781,196.1123962402344,196.1123962402344,196.3141326904297,196.3141326904297,196.5112075805664,196.5112075805664,196.7084503173828,196.7084503173828,196.7084503173828,196.9098892211914,196.9098892211914,197.08642578125,197.08642578125,197.3117141723633,197.3117141723633,197.5336456298828,197.7646179199219,197.9854049682617,197.9854049682617,198.2094497680664,198.2094497680664,198.4527359008789,198.6943054199219,198.6943054199219,198.9334945678711,198.9334945678711,198.9334945678711,199.1738815307617,199.1738815307617,199.4144668579102,199.4144668579102,199.656623840332,199.656623840332,199.8982467651367,199.8982467651367,200.1430206298828,200.1430206298828,200.3866119384766,200.3866119384766,200.6185989379883,200.6185989379883,200.8098297119141,200.8098297119141,200.8098297119141,200.8098297119141,200.8098297119141,200.8098297119141,196.4421234130859,196.4421234130859,196.6502456665039,196.6502456665039,196.8116912841797,196.9599685668945,197.0650482177734,197.0650482177734,197.0650482177734,197.1434707641602,197.1434707641602,197.1434707641602,197.29541015625,197.29541015625,197.46142578125,197.46142578125,197.6588668823242,197.6588668823242,197.8520355224609,197.8520355224609,198.0535430908203,198.1973571777344,198.3575668334961,198.3575668334961,198.5534210205078,198.5534210205078,198.7167663574219,198.8586196899414,199.019172668457,199.019172668457,199.1191329956055,199.221321105957,199.221321105957,199.3169631958008,199.3169631958008,199.4148101806641,199.4148101806641,199.5253753662109,199.5253753662109,199.6107177734375,199.6985626220703,199.6985626220703,199.7954406738281,199.7954406738281,199.7954406738281,199.8814697265625,199.9814453125,199.9814453125,200.0847778320312,200.2499008178711,200.2499008178711,200.4428253173828,200.6472473144531,200.8531875610352,200.939582824707,200.939582824707,200.939582824707,200.939582824707,200.939582824707,200.939582824707,196.5005493164062,196.5005493164062,196.6974334716797,196.6974334716797,196.9023895263672,196.9023895263672,197.1085739135742,197.1085739135742,197.3268814086914,197.3268814086914,197.5598526000977,197.8024520874023,197.8024520874023,198.033576965332,198.033576965332,198.2453536987305,198.2453536987305,198.4578170776367,198.4578170776367,198.6891174316406,198.6891174316406,198.9264602661133,199.16552734375,199.16552734375,199.4036636352539,199.4036636352539,199.6428604125977,199.6428604125977,199.8824005126953,200.1219177246094,200.3533020019531,200.3533020019531,200.5844268798828,200.5844268798828,200.8179626464844,200.8179626464844,201.0434494018555,201.0434494018555,201.0673675537109,201.0673675537109,201.0673675537109,201.0673675537109,201.0673675537109,201.0673675537109,196.7841262817383,196.7841262817383,196.984504699707,197.1855545043945,197.389045715332,197.6137771606445,197.6137771606445,197.8448791503906,197.8448791503906,198.0818252563477,198.3204040527344,198.3204040527344,198.5578689575195,198.5578689575195,198.7871856689453,198.7871856689453,199.0144271850586,199.0144271850586,199.2452011108398,199.2452011108398,199.472053527832,199.5919723510742,199.717041015625,199.717041015625,199.9096908569336,199.9096908569336,200.1392822265625,200.3695831298828,200.609489440918,200.8420257568359,200.8420257568359,201.0665054321289,201.1930160522461,201.1930160522461,201.1930160522461,201.1930160522461,201.1930160522461,201.1930160522461,197.0515060424805,197.2538833618164,197.2538833618164,197.2538833618164,197.4546051025391,197.674690246582,197.674690246582,197.8642578125,197.9915618896484,198.1228332519531,198.1228332519531,198.3053817749023,198.4737930297852,198.4737930297852,198.6247482299805,198.6247482299805,198.7668151855469,198.7668151855469,198.8697891235352,198.987060546875,198.987060546875,198.987060546875,199.1332092285156,199.2834854125977,199.4347076416016,199.4347076416016,199.4347076416016,199.6060104370117,199.761833190918,199.9295806884766,199.9295806884766,200.1076431274414,200.1076431274414,200.2681884765625,200.2681884765625,200.3879241943359,200.3879241943359,200.5303726196289,200.5303726196289,200.5303726196289,200.7102127075195,200.7102127075195,200.9079895019531,200.9079895019531,201.0681838989258,201.2359771728516,201.2359771728516,201.3166732788086,201.3166732788086,201.3166732788086,201.3166732788086,201.3166732788086,201.3166732788086,201.3166732788086,201.3166732788086,201.3166732788086,197.106803894043,197.106803894043,197.106803894043,197.2527770996094,197.2527770996094,197.4082565307617,197.4082565307617,197.550910949707,197.550910949707,197.7211074829102,197.7211074829102,197.8906936645508,198.0901489257812,198.0901489257812,198.3009490966797,198.5014724731445,198.5014724731445,198.7009658813477,198.7009658813477,198.9054565429688,198.9054565429688,199.1086654663086,199.1086654663086,199.2869033813477,199.2869033813477,199.2869033813477,199.4380340576172,199.4380340576172,199.628059387207,199.628059387207,199.7460021972656,199.8989410400391,199.8989410400391,200.0087890625,200.1498870849609,200.1498870849609,200.3447265625,200.5282363891602,200.5282363891602,200.7288436889648,200.9464263916016,201.1753082275391,201.3981018066406,201.3981018066406,201.4382705688477,201.4382705688477,201.4382705688477,201.4382705688477,201.4382705688477,201.4382705688477,197.2835464477539,197.2835464477539,197.4720764160156,197.6599426269531,197.6599426269531,197.8466720581055,197.8466720581055,197.8466720581055,198.0412521362305,198.0412521362305,198.2580261230469,198.2580261230469,198.4818725585938,198.7026901245117,198.7026901245117,198.9263763427734,198.9263763427734,199.1644973754883,199.1644973754883,199.1644973754883,199.3981018066406,199.6383209228516,199.6383209228516,199.8805923461914,200.1242065429688,200.1242065429688,200.3663101196289,200.6091842651367,200.6091842651367,200.8542022705078,201.0981140136719,201.3347854614258,201.3347854614258,201.5579833984375,201.5579833984375,201.5579833984375,201.5579833984375,201.5579833984375,201.5579833984375,201.5579833984375,201.5579833984375,201.5579833984375,197.5391082763672,197.5391082763672,197.728157043457,197.728157043457,197.9118881225586,198.1122360229492,198.1122360229492,198.1122360229492,198.2693328857422,198.2693328857422,198.4776000976562,198.4776000976562,198.6604690551758,198.8838500976562,198.8838500976562,199.1191101074219,199.1191101074219,199.3521270751953,199.3521270751953,199.5876159667969,199.8245391845703,199.8245391845703,200.0593414306641,200.0593414306641,200.2964401245117,200.5283432006836,200.5283432006836,200.7603378295898,200.7603378295898,201.0012512207031,201.0012512207031,201.2376174926758,201.2376174926758,201.4696731567383,201.6756744384766,201.6756744384766,201.6756744384766,201.6756744384766,201.6756744384766,201.6756744384766,197.7318115234375,197.8948974609375,197.8948974609375,198.0754241943359,198.0754241943359,198.0754241943359,198.2742309570312,198.2742309570312,198.2742309570312,198.4731979370117,198.4731979370117,198.6892776489258,198.9093246459961,198.9093246459961,199.1379165649414,199.1379165649414,199.3385391235352,199.3385391235352,199.5092315673828,199.5092315673828,199.7220611572266,199.7220611572266,199.9130020141602,199.9130020141602,199.9130020141602,200.0937957763672,200.2800979614258,200.2800979614258,200.2800979614258,200.4943542480469,200.4943542480469,200.6974182128906,200.6974182128906,200.9293365478516,201.1372756958008,201.1372756958008,201.3359832763672,201.3359832763672,201.5612258911133,201.5612258911133,201.7490768432617,201.7915267944336,201.7915267944336,201.7915267944336,201.7915267944336,197.8373718261719,197.8373718261719,198.0244903564453,198.1860504150391,198.1860504150391,198.3840103149414,198.3840103149414,198.3840103149414,198.5643844604492,198.5643844604492,198.7477340698242,198.7477340698242,198.9632873535156,199.1636123657227,199.1636123657227,199.3854827880859,199.5986862182617,199.5986862182617,199.8069458007812,199.8069458007812,200.0410614013672,200.2504043579102,200.2504043579102,200.4776458740234,200.7003021240234,200.7003021240234,200.9104766845703,200.9104766845703,201.1523513793945,201.362678527832,201.5860748291016,201.5860748291016,201.8058166503906,201.8058166503906,201.9055023193359,201.9055023193359,201.9055023193359,201.9055023193359,201.9055023193359,201.9055023193359,198.1195526123047,198.1195526123047,198.3014984130859,198.4687271118164,198.4687271118164,198.6623382568359,198.6623382568359,198.8592300415039,198.8592300415039,199.0485153198242,199.0485153198242,199.2598190307617,199.2598190307617,199.4931564331055,199.4931564331055,199.7326812744141,199.9715270996094,199.9715270996094,200.2105255126953,200.2105255126953,200.2105255126953,200.4502716064453,200.6894454956055,200.9308319091797,200.9308319091797,201.1733627319336,201.1733627319336,201.4172744750977,201.4172744750977,201.4172744750977,201.6609878540039,201.8930130004883,201.8930130004883,202.0176315307617,202.0176315307617,202.0176315307617,202.0176315307617,202.0176315307617,202.0176315307617,198.3214492797852,198.3214492797852,198.5062103271484,198.5062103271484,198.7018890380859,198.7018890380859,198.9031372070312,198.9031372070312,199.1049957275391,199.1049957275391,199.3278045654297,199.3278045654297,199.5634536743164,199.5634536743164,199.7938537597656,200.0316925048828,200.2681884765625,200.2681884765625,200.5071792602539,200.5071792602539,200.7477874755859,200.7477874755859,200.9890594482422,200.9890594482422,201.2304229736328,201.4727020263672,201.712158203125,201.712158203125,201.9457168579102,202.1280364990234,202.1280364990234,202.1280364990234,202.1280364990234,202.1280364990234,202.1280364990234,198.4676895141602,198.4676895141602,198.649658203125,198.649658203125,198.847297668457,198.847297668457,199.0510101318359,199.0510101318359,199.2638244628906,199.4907455444336,199.4907455444336,199.4907455444336,199.7325439453125,199.7325439453125,199.7325439453125,199.9748764038086,199.9748764038086,200.1626358032227,200.1626358032227,200.1626358032227,200.3321380615234,200.3321380615234,200.5653305053711,200.5653305053711,200.807487487793,201.0500717163086,201.2918319702148,201.2918319702148,201.5342254638672,201.7780838012695,201.7780838012695,201.7780838012695,202.0158386230469,202.0158386230469,202.0158386230469,202.2365646362305,202.2365646362305,202.2365646362305,202.2365646362305,202.2365646362305,202.2365646362305,202.2365646362305,202.2365646362305,202.2365646362305,198.6054458618164,198.6054458618164,198.7881622314453,198.9835815429688,198.9835815429688,199.1875076293945,199.1875076293945,199.4058074951172,199.4058074951172,199.6322479248047,199.8732528686523,199.8732528686523,200.113655090332,200.113655090332,200.113655090332,200.3540802001953,200.3540802001953,200.5932464599609,200.5932464599609,200.8343811035156,201.0768356323242,201.0768356323242,201.3186264038086,201.3186264038086,201.5609741210938,201.5609741210938,201.7941665649414,201.9754333496094,201.9754333496094,202.1946029663086,202.1946029663086,202.3434066772461,202.3434066772461,202.3434066772461,202.3434066772461,202.3434066772461,202.3434066772461,202.3434066772461,202.3434066772461,202.3434066772461,198.764762878418,198.9139633178711,198.9139633178711,199.1031265258789,199.1031265258789,199.2918243408203,199.4709548950195,199.4709548950195,199.6758880615234,199.6758880615234,199.8835220336914,200.1090087890625,200.33642578125,200.5587005615234,200.5587005615234,200.7983856201172,200.7983856201172,201.0235290527344,201.0235290527344,201.2562484741211,201.2562484741211,201.4926071166992,201.4926071166992,201.7231140136719,201.9669189453125,201.9669189453125,202.2004623413086,202.2004623413086,202.2004623413086,202.4184494018555,202.4484558105469,202.4484558105469,202.4484558105469,202.4484558105469,198.8839874267578,198.8839874267578,198.8839874267578,199.0527725219727,199.0527725219727,199.2339172363281,199.2339172363281,199.4204635620117,199.6013336181641,199.6013336181641,199.6013336181641,199.8045120239258,200.0063095092773,200.2216186523438,200.2216186523438,200.4573059082031,200.4573059082031,200.4573059082031,200.6818923950195,200.6818923950195,200.9216613769531,201.1448211669922,201.1448211669922,201.3681793212891,201.3681793212891,201.6084060668945,201.6084060668945,201.8338928222656,201.8338928222656,202.0733108520508,202.2942276000977,202.2942276000977,202.5077209472656,202.5077209472656,202.5519409179688,202.5519409179688,202.5519409179688,202.5519409179688,202.5519409179688,202.5519409179688,199.0856552124023,199.0856552124023,199.2609405517578,199.2609405517578,199.3915481567383,199.5418701171875,199.5418701171875,199.7177429199219,199.7177429199219,199.8444442749023,200.0025024414062,200.0025024414062,200.1786117553711,200.3287506103516,200.3287506103516,200.5013809204102,200.5013809204102,200.5013809204102,200.6438446044922,200.6438446044922,200.7895278930664,200.7895278930664,200.9702987670898,201.0981597900391,201.0981597900391,201.2769775390625,201.2769775390625,201.3974075317383,201.5298461914062,201.5298461914062,201.5298461914062,201.6974716186523,201.8120269775391,201.8120269775391,201.9798126220703,202.140625,202.2963180541992,202.2963180541992,202.4797439575195,202.6262130737305,202.6262130737305,202.6535873413086,202.6535873413086,202.6535873413086,202.6535873413086,202.6535873413086,202.6535873413086,202.6535873413086,202.6535873413086,202.6535873413086,202.6535873413086,202.6535873413086,202.6535873413086,202.6535873413086,202.6535873413086,202.6535873413086,202.6535873413086,202.6535873413086,202.6535873413086,202.6535873413086,202.6535873413086,202.6535873413086,202.6535873413086,202.6535873413086,202.6535873413086,202.6535873413086,202.6535873413086,202.6535873413086,202.6535873413086,202.6535873413086,202.6535873413086,202.6535873413086,202.6535873413086,202.6535873413086,202.6535873413086,202.6535873413086,202.6535873413086,202.6535873413086,202.6535873413086,202.6535873413086,202.6535873413086,202.6535873413086,202.6535873413086,202.6535873413086,202.6535873413086,202.6535873413086,202.6535873413086,202.6535873413086,202.6535873413086,202.6535873413086,202.6535873413086,202.6535873413086,202.6535873413086,202.6535873413086,202.6535873413086,202.6535873413086,202.6535873413086,202.6535873413086,199.2647705078125,199.2647705078125,199.4244384765625,199.6021957397461,199.7889785766602,199.9823455810547,200.1890563964844,200.4144744873047,200.4144744873047,200.6531219482422,200.6531219482422,200.8919677734375,200.8919677734375,200.8919677734375,201.1278076171875,201.1278076171875,201.3629608154297,201.3629608154297,201.6017456054688,201.8420944213867,202.0830993652344,202.0830993652344,202.3237152099609,202.3237152099609,202.5594940185547,202.7533950805664,202.7533950805664,202.7533950805664,202.7533950805664,202.7533950805664,202.7533950805664,199.4181060791016,199.4181060791016,199.6011199951172,199.6011199951172,199.7876968383789,199.7876968383789,199.9831848144531,200.1949768066406,200.1949768066406,200.4172592163086,200.4172592163086,200.6555633544922,200.6555633544922,200.8945922851562,200.8945922851562,201.1335754394531,201.1335754394531,201.1335754394531,201.3700790405273,201.6073226928711,201.6073226928711,201.8464965820312,201.8464965820312,202.0849685668945,202.0849685668945,202.3245544433594,202.3245544433594,202.5665054321289,202.5665054321289,202.5665054321289,202.7974014282227,202.7974014282227,202.8518295288086,202.8518295288086,202.8518295288086,202.8518295288086,202.8518295288086,202.8518295288086,202.8518295288086,202.8518295288086,199.5065231323242,199.5065231323242,199.6862335205078,199.6862335205078,199.8726043701172,199.8726043701172,199.8726043701172,200.059814453125,200.059814453125,200.2576522827148,200.4695358276367,200.4695358276367,200.6962738037109,200.6962738037109,200.6962738037109,200.9217758178711,200.9217758178711,201.1273498535156,201.3597412109375,201.3597412109375,201.5972671508789,201.8380737304688,201.8380737304688,202.0786743164062,202.0786743164062,202.3208236694336,202.3208236694336,202.5638580322266,202.5638580322266,202.7984924316406,202.7984924316406,202.9487533569336,202.9487533569336,202.9487533569336,202.9487533569336,202.9487533569336,202.9487533569336,199.7448959350586,199.7448959350586,199.9180908203125,199.9180908203125,200.1039199829102,200.1039199829102,200.2925643920898,200.2925643920898,200.4662857055664,200.4662857055664,200.6507034301758,200.6507034301758,200.8545989990234,200.8545989990234,201.0804977416992,201.2500076293945,201.2500076293945,201.437385559082,201.437385559082,201.6053009033203,201.6053009033203,201.7873153686523,201.7873153686523,201.959228515625,201.959228515625,202.1234588623047,202.3067245483398,202.4516677856445,202.6271514892578,202.8020935058594,202.961181640625,202.961181640625,203.044075012207,203.044075012207,203.044075012207,203.044075012207,203.044075012207,203.044075012207,203.044075012207,203.044075012207,199.8513717651367,199.8513717651367,200.0001525878906,200.1479721069336,200.2928619384766,200.2928619384766,200.4599380493164,200.4599380493164,200.4599380493164,200.5959625244141,200.5959625244141,200.7624206542969,200.7624206542969,200.9340744018555,200.9340744018555,201.0935592651367,201.0935592651367,201.268669128418,201.4004669189453,201.4004669189453,201.5738372802734,201.5738372802734,201.7549819946289,201.9683456420898,201.9683456420898,202.1974792480469,202.1974792480469,202.4366836547852,202.4366836547852,202.6797409057617,202.9194412231445,202.9194412231445,203.1378631591797,203.1378631591797,203.1378631591797,203.1378631591797,203.1378631591797,203.1378631591797,203.1378631591797,203.1378631591797,203.1378631591797,199.9814987182617,199.9814987182617,200.14697265625,200.14697265625,200.3329620361328,200.5217742919922,200.5217742919922,200.7209701538086,200.7209701538086,200.7209701538086,200.9404983520508,200.9404983520508,201.1736679077148,201.1736679077148,201.4184646606445,201.4184646606445,201.6603088378906,201.6603088378906,201.9024887084961,202.1354675292969,202.1354675292969,202.3192367553711,202.3192367553711,202.5399322509766,202.5399322509766,202.7264556884766,202.8907241821289,202.8907241821289,203.1108169555664,203.2301025390625,203.2301025390625,203.2301025390625,203.2301025390625,203.2301025390625,203.2301025390625,203.2301025390625,203.2301025390625,203.2301025390625,200.1881637573242,200.1881637573242,200.3615951538086,200.3615951538086,200.5435180664062,200.5435180664062,200.7333908081055,200.7333908081055,200.9339370727539,200.9339370727539,201.1524276733398,201.1524276733398,201.1524276733398,201.3907699584961,201.62744140625,201.62744140625,201.62744140625,201.8691177368164,202.1030807495117,202.3395538330078,202.3395538330078,202.5775146484375,202.5775146484375,202.8207855224609,203.0661849975586,203.0661849975586,203.0661849975586,203.2964401245117,203.3209381103516,203.3209381103516,203.3209381103516,203.3209381103516,200.2509689331055,200.2509689331055,200.4164810180664,200.4164810180664,200.6040267944336,200.6040267944336,200.7944488525391,200.7944488525391,200.9911956787109,201.2057876586914,201.2057876586914,201.4338760375977,201.4338760375977,201.6735687255859,201.6735687255859,201.9181823730469,201.9181823730469,202.1636581420898,202.4065933227539,202.6510848999023,202.8962707519531,202.8962707519531,203.1419372558594,203.1419372558594,203.3738021850586,203.3738021850586,203.4102401733398,203.4102401733398,203.4102401733398,203.4102401733398,200.3742828369141,200.3742828369141,200.5484771728516,200.5484771728516,200.7273406982422,200.7273406982422,200.9168167114258,200.9168167114258,201.1098556518555,201.1098556518555,201.1098556518555,201.3165740966797,201.3165740966797,201.3165740966797,201.5390396118164,201.5390396118164,201.7740020751953,201.7740020751953,202.0158233642578,202.0158233642578,202.2565612792969,202.4940414428711,202.4940414428711,202.7364883422852,202.9798736572266,202.9798736572266,203.2238082885742,203.2238082885742,203.4556045532227,203.4556045532227,203.4981002807617,203.4981002807617,203.4981002807617,203.4981002807617,203.4981002807617,203.4981002807617,203.4981002807617,203.4981002807617,203.4981002807617,200.5300674438477,200.6900482177734,200.6900482177734,200.8360290527344,200.8360290527344,201.0092315673828,201.0092315673828,201.1901550292969,201.3738403320312,201.3738403320312,201.3738403320312,201.5639190673828,201.7402420043945,201.7402420043945,201.7402420043945,201.9314270019531,202.1191329956055,202.3094482421875,202.3094482421875,202.5068588256836,202.5068588256836,202.6851577758789,202.6851577758789,202.885009765625,203.0775680541992,203.0775680541992,203.2639236450195,203.2639236450195,203.4604187011719,203.4604187011719,203.5846481323242,203.5846481323242,203.5846481323242,203.5846481323242,203.5846481323242,203.5846481323242,203.5846481323242,203.5846481323242,203.5846481323242,203.5846481323242,203.5846481323242,203.5846481323242,200.7044296264648,200.7044296264648,200.8486480712891,200.8486480712891,201.0097732543945,201.0097732543945,201.1812362670898,201.1812362670898,201.3564987182617,201.3564987182617,201.3564987182617,201.5534286499023,201.7583160400391,201.7583160400391,201.9841766357422,201.9841766357422,201.9841766357422,202.2152786254883,202.2152786254883,202.456184387207,202.456184387207,202.6944961547852,202.6944961547852,202.9354782104492,203.1788635253906,203.4204254150391,203.6501312255859,203.6501312255859,203.6696472167969,203.6696472167969,203.6696472167969,203.6696472167969,203.6696472167969,203.6696472167969,200.7748641967773,200.7748641967773,200.9432067871094,201.1245727539062,201.1245727539062,201.3126525878906,201.5003356933594,201.6703186035156,201.6703186035156,201.8758010864258,201.8758010864258,202.0993576049805,202.0993576049805,202.3285446166992,202.3285446166992,202.3285446166992,202.5655975341797,202.5655975341797,202.8020935058594,203.042366027832,203.042366027832,203.2821044921875,203.2821044921875,203.5189437866211,203.5189437866211,203.7432479858398,203.7432479858398,203.7533950805664,203.7533950805664,203.7533950805664,203.7533950805664,203.7533950805664,203.7533950805664,200.9056701660156,200.9056701660156,201.0734939575195,201.0734939575195,201.2498168945312,201.2498168945312,201.4357299804688,201.6293334960938,201.6293334960938,201.8382797241211,202.0640563964844,202.3014068603516,202.5393676757812,202.5393676757812,202.7438507080078,202.9573364257812,203.1960525512695,203.1960525512695,203.4360733032227,203.4360733032227,203.4360733032227,203.6736907958984,203.6736907958984,203.8356628417969,203.8356628417969,203.8356628417969,203.8356628417969,203.8356628417969,203.8356628417969,201.1121215820312,201.1121215820312,201.2899017333984,201.2899017333984,201.4774932861328,201.4774932861328,201.6722869873047,201.6722869873047,201.8831634521484,202.1142807006836,202.1142807006836,202.3578948974609,202.3578948974609,202.5984268188477,202.5984268188477,202.5984268188477,202.8391799926758,202.8391799926758,202.8391799926758,203.0806579589844,203.0806579589844,203.3231887817383,203.3231887817383,203.5694580078125,203.8060455322266,203.8060455322266,203.9167556762695,203.9167556762695,203.9167556762695,203.9167556762695,203.9167556762695,203.9167556762695,201.2886047363281,201.4674606323242,201.4674606323242,201.6585083007812,201.8577270507812,201.8577270507812,202.0765609741211,202.3111267089844,202.3111267089844,202.3111267089844,202.5549850463867,202.7996444702148,202.7996444702148,203.0428771972656,203.0428771972656,203.2846603393555,203.2846603393555,203.5279083251953,203.5279083251953,203.7723617553711,203.9963912963867,203.9963912963867,203.9963912963867,203.9963912963867,203.9963912963867,203.9963912963867,203.9963912963867,203.9963912963867,203.9963912963867,201.3145370483398,201.3145370483398,201.4910507202148,201.6765975952148,201.8681869506836,201.8681869506836,202.0747375488281,202.0747375488281,202.3015747070312,202.3015747070312,202.5418701171875,202.7871398925781,202.7871398925781,202.7871398925781,203.0313339233398,203.2737274169922,203.2737274169922,203.5160446166992,203.7603759765625,203.7603759765625,203.9966888427734,203.9966888427734,204.0748138427734,204.0748138427734,204.0748138427734,204.0748138427734,204.0748138427734,204.0748138427734,201.3805160522461,201.3805160522461,201.5374145507812,201.5374145507812,201.6984786987305,201.8853759765625,201.8853759765625,202.0714340209961,202.2633895874023,202.2633895874023,202.4565353393555,202.4565353393555,202.6776504516602,202.6776504516602,202.9070053100586,202.9070053100586,202.9070053100586,203.0933380126953,203.3197784423828,203.5574722290039,203.7865142822266,203.7865142822266,204.0214462280273,204.0214462280273,204.1520004272461,204.1520004272461,204.1520004272461,204.1520004272461,204.1520004272461,204.1520004272461,204.1520004272461,204.1520004272461,204.1520004272461,204.1520004272461,204.1520004272461,204.1520004272461,201.5339965820312,201.6540832519531,201.7961044311523,201.7961044311523,201.9600219726562,201.9600219726562,202.0998382568359,202.2758407592773,202.4462280273438,202.6201400756836,202.6201400756836,202.8024673461914,202.8024673461914,202.8024673461914,202.9607238769531,202.9607238769531,203.1495056152344,203.3224105834961,203.3224105834961,203.502067565918,203.502067565918,203.6900177001953,203.6900177001953,203.8588104248047,204.0497283935547,204.0497283935547,204.2208480834961,204.2208480834961,204.2278594970703,204.2278594970703,204.2278594970703,204.2278594970703,204.2278594970703,204.2278594970703,204.2278594970703,204.2278594970703,204.2278594970703,201.6214752197266,201.7512283325195,201.892951965332,201.892951965332,202.063850402832,202.2161636352539,202.3861999511719,202.3861999511719,202.5671310424805,202.5671310424805,202.7345199584961,202.7345199584961,202.9300155639648,202.9300155639648,203.1103897094727,203.1103897094727,203.3154144287109,203.3154144287109,203.5442352294922,203.7817916870117,203.7817916870117,204.0270767211914,204.0270767211914,204.2606506347656,204.2606506347656,204.3025741577148,204.3025741577148,204.3025741577148,204.3025741577148,204.3025741577148,204.3025741577148,201.7381439208984,201.9049453735352,202.0866241455078,202.2763595581055,202.2763595581055,202.4748229980469,202.6977462768555,202.6977462768555,202.9351119995117,202.9351119995117,203.1804275512695,203.1804275512695,203.42333984375,203.6658477783203,203.6658477783203,203.9087066650391,204.1534271240234,204.1534271240234,204.3759841918945,204.3759841918945,204.3759841918945,204.3759841918945,204.3759841918945,204.3759841918945,204.3759841918945,204.3759841918945,204.3759841918945,201.9120559692383,201.9120559692383,202.0889511108398,202.0889511108398,202.2783432006836,202.4758148193359,202.6908798217773,202.6908798217773,202.9251480102539,203.1704025268555,203.1704025268555,203.3810043334961,203.3810043334961,203.52685546875,203.7432174682617,203.7432174682617,203.8866882324219,203.8866882324219,204.057975769043,204.057975769043,204.2176513671875,204.2176513671875,204.3703460693359,204.3703460693359,204.4482879638672,204.4482879638672,204.4482879638672,204.4482879638672,204.4482879638672,204.4482879638672,204.4482879638672,204.4482879638672,204.4482879638672,204.4482879638672,204.4482879638672,204.4482879638672,204.4482879638672,204.4482879638672,204.4482879638672,204.4482879638672,204.4482879638672,204.4482879638672,204.4482879638672,204.4482879638672,204.4482879638672,204.4482879638672,204.4482879638672,204.4482879638672,204.4482879638672,204.4482879638672,204.4482879638672,204.4482879638672,204.4482879638672,204.4482879638672,204.4482879638672,204.4482879638672,204.4482879638672,204.4482879638672,204.4482879638672,204.4482879638672,204.4482879638672,204.4482879638672,204.4482879638672,204.4482879638672,201.9599227905273,201.9599227905273,201.9599227905273,201.9599227905273,202.064079284668,202.064079284668,202.2240142822266,202.3997650146484,202.5874786376953,202.7842483520508,202.7842483520508,203.0015411376953,203.2359848022461,203.4805450439453,203.4805450439453,203.7054824829102,203.7054824829102,203.9371109008789,203.9371109008789,204.1719436645508,204.1719436645508,204.4165115356445,204.5191802978516,204.5191802978516,204.5191802978516,204.5191802978516,204.5191802978516,204.5191802978516,204.5191802978516,204.5191802978516,204.5191802978516,202.2214279174805,202.4024429321289,202.4024429321289,202.5933303833008,202.5933303833008,202.7959594726562,203.0209503173828,203.0209503173828,203.237663269043,203.237663269043,203.4308624267578,203.4308624267578,203.6658248901367,203.6658248901367,203.8476257324219,203.8476257324219,204.0708465576172,204.0708465576172,204.0708465576172,204.245964050293,204.245964050293,204.4441299438477,204.5891799926758,204.5891799926758,204.5891799926758,204.5891799926758,204.5891799926758,204.5891799926758,204.5891799926758,204.5891799926758,204.5891799926758,204.5891799926758,204.5891799926758,204.5891799926758,202.1943435668945,202.1943435668945,202.3239135742188,202.4654769897461,202.4654769897461,202.6272583007812,202.6272583007812,202.7771453857422,202.7771453857422,202.9447402954102,202.9447402954102,203.1240158081055,203.1240158081055,203.284065246582,203.284065246582,203.4714050292969,203.645881652832,203.645881652832,203.8356399536133,204.0363464355469,204.0363464355469,204.0363464355469,204.207649230957,204.207649230957,204.3950576782227,204.5583801269531,204.5583801269531,204.6580429077148,204.6580429077148,204.6580429077148,204.6580429077148,204.6580429077148,204.6580429077148,204.6580429077148,204.6580429077148,204.6580429077148,204.6580429077148,204.6580429077148,204.6580429077148,202.3098678588867,202.3098678588867,202.3098678588867,202.4583129882812,202.4583129882812,202.4583129882812,202.6314849853516,202.6314849853516,202.8145751953125,202.8145751953125,203.0063705444336,203.2151641845703,203.2151641845703,203.4402618408203,203.4402618408203,203.6817321777344,203.6817321777344,203.6817321777344,203.9211502075195,204.1593780517578,204.1593780517578,204.3978958129883,204.6321029663086,204.6321029663086,204.7258071899414,204.7258071899414,204.7258071899414,204.7258071899414,204.7258071899414,204.7258071899414,204.7258071899414,204.7258071899414,204.7258071899414,202.5297698974609,202.5297698974609,202.708122253418,202.708122253418,202.8965759277344,202.8965759277344,203.0973358154297,203.3207015991211,203.3207015991211,203.5567245483398,203.5567245483398,203.7997589111328,204.0406341552734,204.0406341552734,204.2835998535156,204.5259399414062,204.7694396972656,204.7924880981445,204.7924880981445,204.7924880981445,204.7924880981445,202.5310363769531,202.5310363769531,202.7057418823242,202.7057418823242,202.8940887451172,202.8940887451172,203.088005065918,203.302360534668,203.302360534668,203.5343551635742,203.5343551635742,203.778076171875,204.0233917236328,204.0233917236328,204.2671585083008,204.2671585083008,204.5121078491211,204.5121078491211,204.7551422119141,204.7551422119141,204.8581008911133,204.8581008911133,204.8581008911133,204.8581008911133,204.8581008911133,204.8581008911133,202.7410507202148,202.7410507202148,202.9196929931641,202.9196929931641,203.1127014160156,203.1127014160156,203.1127014160156,203.3136215209961,203.3136215209961,203.5241851806641,203.5241851806641,203.7591781616211,203.7591781616211,204.0043106079102,204.0043106079102,204.2471466064453,204.2471466064453,204.4910430908203,204.7344436645508,204.7344436645508,204.9226684570312,204.9226684570312,204.9226684570312,204.9226684570312,204.9226684570312,204.9226684570312,202.7727661132812,202.7727661132812,202.9480438232422,202.9480438232422,203.1345977783203,203.1345977783203,203.1345977783203,203.332145690918,203.332145690918,203.5429611206055,203.7724380493164,203.7724380493164,204.0114364624023,204.0114364624023,204.256965637207,204.256965637207,204.4991302490234,204.4991302490234,204.7445526123047,204.986198425293,204.986198425293,204.986198425293,204.986198425293,204.986198425293,204.986198425293,204.986198425293,204.986198425293,204.986198425293,202.8290710449219,202.8290710449219,203.0000534057617,203.1821975708008,203.3779754638672,203.3779754638672,203.5848693847656,203.5848693847656,203.80859375,203.80859375,204.0272369384766,204.0272369384766,204.2437744140625,204.2437744140625,204.4715957641602,204.7152633666992,204.7152633666992,204.9585113525391,204.9585113525391,205.0486907958984,205.0486907958984,205.0486907958984,205.0486907958984,205.0486907958984,205.0486907958984,205.0486907958984,205.0486907958984,205.0486907958984,203.0235214233398,203.0235214233398,203.1981887817383,203.3867797851562,203.3867797851562,203.3867797851562,203.581657409668,203.7949142456055,203.9897308349609,203.9897308349609,204.1804351806641,204.4119110107422,204.4119110107422,204.6560440063477,204.9013290405273,204.9013290405273,205.1101303100586,205.1101303100586,205.1101303100586,205.1101303100586,205.1101303100586,205.1101303100586,205.1101303100586,205.1101303100586,205.1101303100586,203.043571472168,203.043571472168,203.043571472168,203.2186889648438,203.2186889648438,203.403694152832,203.5998077392578,203.5998077392578,203.8112564086914,204.0111236572266,204.1664428710938,204.1664428710938,204.3868865966797,204.6062316894531,204.6062316894531,204.8402938842773,204.8402938842773,205.074462890625,205.1705627441406,205.1705627441406,205.1705627441406,205.1705627441406,205.1705627441406,205.1705627441406,203.1764984130859,203.1764984130859,203.3446197509766,203.3446197509766,203.3446197509766,203.5187301635742,203.7166137695312,203.7166137695312,203.9136581420898,204.123176574707,204.3500671386719,204.3500671386719,204.5745697021484,204.5745697021484,204.8167266845703,204.8167266845703,205.0520401000977,205.230094909668,205.230094909668,205.230094909668,205.230094909668,205.230094909668,205.230094909668,205.230094909668,205.230094909668,205.230094909668,203.2334899902344,203.3952789306641,203.5606307983398,203.5606307983398,203.7560577392578,203.7560577392578,203.9417114257812,204.1584396362305,204.1584396362305,204.3709945678711,204.5922012329102,204.8350982666016,204.8350982666016,204.8350982666016,205.0634231567383,205.2885360717773,205.2885360717773,205.2885360717773,205.2885360717773,205.2885360717773,205.2885360717773,205.2885360717773,205.2885360717773,205.2885360717773,203.2826614379883,203.4399948120117,203.4399948120117,203.6108016967773,203.6108016967773,203.7983627319336,203.7983627319336,203.9823913574219,203.9823913574219,204.2029647827148,204.2029647827148,204.4066925048828,204.6271591186523,204.8605422973633,205.0704116821289,205.0704116821289,205.3066101074219,205.34619140625,205.34619140625,205.34619140625,205.34619140625,205.34619140625,205.34619140625,203.5180435180664,203.5180435180664,203.6952972412109,203.6952972412109,203.8889541625977,204.0902709960938,204.0902709960938,204.3107299804688,204.3107299804688,204.5497055053711,204.5497055053711,204.7953338623047,204.7953338623047,205.0388946533203,205.0388946533203,205.2821655273438,205.2821655273438,205.4027862548828,205.4027862548828,205.4027862548828,205.4027862548828,205.4027862548828,205.4027862548828,205.4027862548828,205.4027862548828,205.4027862548828,205.4027862548828,205.4027862548828,205.4027862548828,205.4027862548828,205.4027862548828,205.4027862548828,205.4027862548828,205.4027862548828,205.4027862548828,203.5210494995117,203.5210494995117,203.5210494995117,203.6786804199219,203.8571929931641,204.0485229492188,204.0485229492188,204.2515335083008,204.2515335083008,204.4688415527344,204.4688415527344,204.6934509277344,204.8359069824219,204.8359069824219,205.043701171875,205.2254943847656,205.3865814208984,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,205.4582977294922,203.5401000976562,203.5401000976562,203.5401000976562,203.5401000976562,203.5401000976562,203.5401000976562,203.5485076904297,203.5485076904297,203.7401504516602,203.7401504516602,203.9426651000977,203.9426651000977,204.154670715332,204.3843231201172,204.3843231201172,204.3843231201172,204.6296157836914,204.8721923828125,205.1020431518555,205.1020431518555,205.3117065429688,205.3117065429688,205.5398101806641,205.5398101806641,205.7740707397461,205.7740707397461,206.0173187255859,206.0173187255859,206.263298034668,206.263298034668,206.5084609985352,206.5084609985352,206.5084609985352,206.7529067993164,206.7529067993164,206.9990844726562,206.9990844726562,207.2451248168945,207.2451248168945,207.491455078125,207.6872863769531,207.6872863769531,207.8808364868164,207.8808364868164,208.0729827880859,208.0729827880859,208.2668838500977,208.2668838500977,208.459098815918,208.6548614501953,208.6548614501953,208.8489532470703,208.8489532470703,209.0464172363281,209.2441787719727,209.4406433105469,209.6384048461914,209.6384048461914,209.83056640625,209.83056640625,210.0288772583008,210.0288772583008,210.0288772583008,210.2250671386719,210.2250671386719,210.4226226806641,210.4226226806641,210.6177749633789,210.6177749633789,210.8158874511719,210.8158874511719,210.8158874511719,211.0104522705078,211.0104522705078,211.2071762084961,211.2071762084961,211.4045257568359,211.4798812866211,211.4798812866211,211.4798812866211,211.4798812866211,211.4798812866211,211.4798812866211,211.4798812866211,211.4798812866211,211.4798812866211,203.9485321044922,204.1474151611328,204.3565292358398,204.3565292358398,204.5801010131836,204.5801010131836,204.8208236694336,204.8208236694336,205.0643844604492,205.0643844604492,205.2935562133789,205.2935562133789,205.4829483032227,205.4829483032227,205.6967468261719,205.9335403442383,205.9335403442383,206.1144943237305,206.1144943237305,206.2860488891602,206.2860488891602,206.4945297241211,206.4945297241211,206.6679229736328,206.6679229736328,206.8823318481445,206.8823318481445,207.1153717041016,207.1153717041016,207.3445205688477,207.578254699707,207.578254699707,207.819221496582,207.819221496582,208.0529174804688,208.0529174804688,208.2947235107422,208.2947235107422,208.5281066894531,208.5281066894531,208.7634429931641,208.7634429931641,208.7634429931641,209.0037002563477,209.0037002563477,209.2324905395508,209.2324905395508,209.4739227294922,209.4739227294922,209.7064971923828,209.9358139038086,209.9358139038086,210.1788711547852,210.1788711547852,210.4101028442383,210.4101028442383,210.650032043457,210.650032043457,210.8866806030273,210.8866806030273,211.1171340942383,211.1171340942383,211.3459701538086,211.5647506713867,211.5647506713867,211.6970520019531,211.6970520019531,211.6970520019531,211.6970520019531,211.6970520019531,211.6970520019531,211.6970520019531,211.6970520019531,211.6970520019531,211.6970520019531,211.6970520019531,211.6970520019531,211.6970520019531,211.6970520019531,211.6970520019531,211.6970520019531,204.3523712158203,204.3523712158203,204.5439300537109,204.5439300537109,204.7469863891602,204.7469863891602,204.9490585327148,205.1729049682617,205.1729049682617,205.3876876831055,205.5962600708008,205.5962600708008,205.8133239746094,205.8133239746094,206.0400390625,206.0400390625,206.2757797241211,206.5118942260742,206.5118942260742,206.7359771728516,206.9711303710938,206.9711303710938,207.212760925293,207.212760925293,207.4549026489258,207.6987075805664,207.6987075805664,207.9450073242188,207.9450073242188,208.1926803588867,208.4382705688477,208.4382705688477,208.683235168457,208.9327774047852,208.9327774047852,209.1854476928711,209.1854476928711,209.4399337768555,209.4399337768555,209.6951065063477,209.9501190185547,210.2060852050781,210.2060852050781,210.4589462280273,210.7080993652344,210.7080993652344,210.9522171020508,211.1954193115234,211.1954193115234,211.4382095336914,211.4382095336914,211.6789627075195,211.9106674194336,211.9106674194336,211.9106674194336,211.9106674194336,211.9106674194336,211.9106674194336,211.9106674194336,211.9106674194336,204.6659088134766,204.6659088134766,204.863166809082,204.863166809082,205.0719451904297,205.0719451904297,205.2951507568359,205.525146484375,205.7545928955078,205.7545928955078,205.9800491333008,205.9800491333008,206.2285232543945,206.2285232543945,206.4758224487305,206.4758224487305,206.7198638916016,206.7198638916016,206.9660339355469,207.2117691040039,207.4617767333984,207.4617767333984,207.7168502807617,207.9692306518555,207.9692306518555,208.1640090942383,208.406005859375,208.406005859375,208.6469192504883,208.8887481689453,208.8887481689453,208.8887481689453,209.1317749023438,209.1317749023438,209.3748626708984,209.3748626708984,209.6168441772461,209.8594589233398,210.1026992797852,210.1026992797852,210.3455429077148,210.3455429077148,210.5893020629883,210.5893020629883,210.8331909179688,210.8331909179688,211.0771026611328,211.0771026611328,211.3224029541016,211.3224029541016,211.5646286010742,211.5646286010742,211.7963638305664,211.7963638305664,212.0282897949219,212.1208801269531,212.1208801269531,212.1208801269531,212.1208801269531,212.1208801269531,212.1208801269531,212.1208801269531,212.1208801269531,212.1208801269531,212.1208801269531,212.1208801269531,212.1208801269531,205.0439224243164,205.0439224243164,205.2411727905273,205.2411727905273,205.2411727905273,205.44775390625,205.6516036987305,205.6516036987305,205.8460464477539,205.8460464477539,205.8460464477539,206.0272750854492,206.0272750854492,206.2158126831055,206.4223327636719,206.4223327636719,206.6425323486328,206.6425323486328,206.8778228759766,206.8778228759766,207.1176834106445,207.1176834106445,207.3526458740234,207.3526458740234,207.5941772460938,207.8374862670898,207.8374862670898,208.0789413452148,208.3233337402344,208.5672912597656,208.8095092773438,208.8095092773438,209.0530242919922,209.0530242919922,209.2961730957031,209.5403060913086,209.7835159301758,210.028190612793,210.028190612793,210.2732696533203,210.5180740356445,210.5180740356445,210.7643203735352,211.0106353759766,211.0106353759766,211.255615234375,211.255615234375,211.255615234375,211.5021286010742,211.7480392456055,211.9752349853516,211.9752349853516,211.9752349853516,212.2073974609375,212.2073974609375,212.2073974609375,212.3277435302734,212.3277435302734,212.3277435302734,212.3277435302734,212.3277435302734,212.3277435302734,212.3277435302734,212.3277435302734,205.3394775390625,205.3394775390625,205.53564453125,205.53564453125,205.7420425415039,205.7420425415039,205.9479064941406,206.1561965942383,206.1561965942383,206.3679656982422,206.3679656982422,206.6097030639648,206.8532943725586,207.0972747802734,207.3393630981445,207.5819473266602,207.8249206542969,207.8249206542969,208.0677871704102,208.0677871704102,208.0677871704102,208.3100967407227,208.5527801513672,208.5527801513672,208.796760559082,209.0399017333984,209.0399017333984,209.2819519042969,209.5232315063477,209.7655639648438,210.0072021484375,210.2503662109375,210.2503662109375,210.2503662109375,210.4937896728516,210.7375259399414,210.9828033447266,210.9828033447266,211.2275772094727,211.2275772094727,211.4727020263672,211.7187957763672,211.9651260375977,211.9651260375977,212.1963729858398,212.1963729858398,212.4250793457031,212.5311889648438,212.5311889648438,212.5311889648438,212.5311889648438,212.5311889648438,212.5311889648438,212.5311889648438,212.5311889648438,212.5311889648438,212.5311889648438,212.5311889648438,212.5311889648438,205.6658401489258,205.6658401489258,205.8607940673828,206.0644226074219,206.2649154663086,206.2649154663086,206.4688720703125,206.4688720703125,206.6838455200195,206.927864074707,207.1720123291016,207.1720123291016,207.4165649414062,207.6585464477539,207.9023208618164,207.9023208618164,208.1464996337891,208.3910217285156,208.3910217285156,208.6058349609375,208.8469390869141,209.0881652832031,209.0881652832031,209.3292541503906,209.5697250366211,209.8126068115234,210.0559387207031,210.0559387207031,210.2998352050781,210.2998352050781,210.2998352050781,210.544075012207,210.544075012207,210.7865982055664,210.7865982055664,211.0329513549805,211.2793197631836,211.2793197631836,211.5341491699219,211.5341491699219,211.7880477905273,211.7880477905273,211.7880477905273,212.0437088012695,212.0437088012695,212.2872085571289,212.5271987915039,212.7313995361328,212.7313995361328,212.7313995361328,212.7313995361328,212.7313995361328,212.7313995361328,212.7313995361328,212.7313995361328,212.7313995361328,212.7313995361328,212.7313995361328,212.7313995361328,212.7313995361328,212.7313995361328,212.7313995361328,212.7313995361328,212.7313995361328,212.7313995361328,212.7313995361328,212.7313995361328,212.7313995361328,212.7313995361328,212.7313995361328,212.7313995361328,212.7313995361328,212.7313995361328,212.7313995361328,212.7313995361328,212.7313995361328,212.7313995361328,212.7313995361328,212.7313995361328,212.7313995361328,212.7313995361328,212.7313995361328,212.7313995361328,205.9500503540039,205.9500503540039,206.1299819946289,206.3257675170898,206.3257675170898,206.5194854736328,206.5194854736328,206.7109375,206.7109375,206.9178695678711,207.1510772705078,207.395622253418,207.6376037597656,207.6376037597656,207.8776550292969,207.8776550292969,208.1185531616211,208.3609390258789,208.3609390258789,208.3609390258789,208.6024398803711,208.8448867797852,208.8448867797852,209.0816268920898,209.0816268920898,209.0816268920898,209.3215484619141,209.5634689331055,209.5634689331055,209.8040466308594,209.8040466308594,210.0466003417969,210.0466003417969,210.2936401367188,210.2936401367188,210.5486526489258,210.802490234375,210.802490234375,211.0571060180664,211.3127746582031,211.3127746582031,211.5674133300781,211.5674133300781,211.8215255737305,211.8215255737305,212.0773391723633,212.0773391723633,212.3330612182617,212.5766830444336,212.8182525634766,212.8182525634766,212.9282760620117,212.9282760620117,212.9282760620117,212.9282760620117,212.9282760620117,212.9282760620117,212.9282760620117,212.9282760620117,206.2921371459961,206.2921371459961,206.2921371459961,206.4882965087891,206.4882965087891,206.6869354248047,206.6869354248047,206.8850784301758,206.8850784301758,207.0989532470703,207.0989532470703,207.3339385986328,207.3339385986328,207.5806350708008,207.8240966796875,208.0630187988281,208.3029098510742,208.3029098510742,208.5443496704102,208.7851181030273,208.7851181030273,209.025749206543,209.2666091918945,209.2666091918945,209.5072555541992,209.5072555541992,209.7495269775391,209.7495269775391,209.9876556396484,209.9876556396484,210.2298355102539,210.2298355102539,210.2298355102539,210.4718017578125,210.4718017578125,210.7158660888672,210.9597778320312,210.9597778320312,211.2020034790039,211.2020034790039,211.4460754394531,211.4460754394531,211.6909866333008,211.9474258422852,211.9474258422852,212.2039184570312,212.2039184570312,212.4599914550781,212.7084197998047,212.7084197998047,212.7084197998047,212.9444122314453,213.1220703125,213.1220703125,213.1220703125,213.1220703125,213.1220703125,213.1220703125,213.1220703125,213.1220703125,206.531867980957,206.531867980957,206.7180480957031,206.7180480957031,206.9128646850586,206.9128646850586,207.1042709350586,207.1042709350586,207.3051910400391,207.3051910400391,207.5347290039062,207.5347290039062,207.7789916992188,207.7789916992188,208.0234146118164,208.0234146118164,208.2659530639648,208.2659530639648,208.2659530639648,208.5058364868164,208.5058364868164,208.7469024658203,208.9880752563477,209.2289505004883,209.2289505004883,209.4697570800781,209.7110366821289,209.9526214599609,209.9526214599609,209.9526214599609,210.1951065063477,210.4379959106445,210.4379959106445,210.4379959106445,210.6496658325195,210.8815155029297,211.125129699707,211.125129699707,211.3679351806641,211.611198425293,211.611198425293,211.8549346923828,211.8549346923828,212.0999221801758,212.0999221801758,212.3434982299805,212.3434982299805,212.5870895385742,212.8284759521484,212.8284759521484,213.0590515136719,213.0590515136719,213.2932052612305,213.3127899169922,213.3127899169922,213.3127899169922,213.3127899169922,213.3127899169922,213.3127899169922,213.3127899169922,213.3127899169922,213.3127899169922,213.3127899169922,213.3127899169922,213.3127899169922,206.9169387817383,206.9169387817383,207.1064376831055,207.1064376831055,207.2970275878906,207.2970275878906,207.2970275878906,207.4823303222656,207.4823303222656,215.2991943359375,215.2991943359375,215.2991943359375,215.2991943359375,215.2991943359375,215.2991943359375,215.2991943359375,215.2991943359375,215.2991943359375,215.2991943359375,215.2991943359375,215.2991943359375,215.2991943359375,215.2991943359375,215.2991943359375,215.2991943359375,215.2991943359375,215.2991943359375,215.2991943359375,215.2991943359375,215.2991943359375,215.2991943359375,215.2991943359375,215.2991943359375,222.9285888671875,222.9285888671875,222.9285888671875,222.928596496582,222.928596496582,222.928596496582,222.928596496582,222.928596496582,222.928596496582,222.928596496582,222.928596496582,222.928596496582,222.928596496582,222.928596496582,222.928596496582,222.928596496582,222.928596496582,222.928596496582,222.928596496582,222.928596496582,222.928596496582,222.928596496582,222.928596496582,222.928596496582,222.928596496582,222.928596496582,222.928596496582,238.187385559082,238.187385559082,238.187385559082,238.187385559082,238.187385559082,238.187385559082,238.187385559082,238.187385559082,238.187385559082,238.187385559082,238.187385559082,238.187385559082,238.187385559082,238.187385559082,238.187385559082,238.187385559082,238.187385559082,238.187385559082,238.187385559082,238.187385559082],"meminc":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,15.32453155517578,0,0,0,0,0,0,0,15.25894165039062,0,0,0,0,0,0.0003662109375,0,0,30.2857666015625,0,0,0,0,0,0,0,0,0,0,0,4.57763671875e-05,0,-0.000152587890625,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-0.00018310546875,0,15.2587890625,0.19610595703125,0.199676513671875,0,0.20819091796875,0.1671142578125,0,0.2067642211914062,0,0.2233428955078125,0,0.24072265625,0,0.241119384765625,0,0.2355117797851562,0,0,0.235626220703125,0.2360763549804688,0,0.2346267700195312,0.1970596313476562,0,0,0,-2.609687805175781,0,0.2092056274414062,0,0.2284774780273438,0,0.245147705078125,0.2527923583984375,0,0.2512969970703125,0,0.248138427734375,0,0.2402496337890625,0,0.2141036987304688,0.2231292724609375,0.2123947143554688,0.1994476318359375,0.1431884765625,0,0,0,0,0,-2.541015625,0,0.1998291015625,0,0.20098876953125,0.2092742919921875,0,0.1937408447265625,0,0.211456298828125,0,0.2241287231445312,0.2045516967773438,0,0.2272262573242188,0.21783447265625,0.2205734252929688,0.2269973754882812,0,0.1797027587890625,0,0.100006103515625,0,0,0,-2.501289367675781,0,0.2005615234375,0,0.2081680297851562,0,0.2140350341796875,0,0.2279205322265625,0,0.2371444702148438,0.2483978271484375,0.2444534301757812,0,0.2430648803710938,0,0.2429351806640625,0.2434463500976562,0,0.24432373046875,0.0208892822265625,0,-2.51446533203125,0,0.2016067504882812,0,0.2071304321289062,0.2152786254882812,0,0.2343978881835938,0,0.2412948608398438,0,0.2465972900390625,0.2440872192382812,0.244964599609375,0.2430953979492188,0.24560546875,0.2448959350585938,0.01847076416015625,0,0,-2.471366882324219,0,0.1930313110351562,0,0,0.2067031860351562,0,0.2212753295898438,0,0.2372283935546875,0,0.244110107421875,0,0.2449874877929688,0,0.2412948608398438,0,0.2427978515625,0.2419815063476562,0.244110107421875,0,0.225555419921875,0,0,0,-2.407920837402344,0,0,0.2009048461914062,0,0.2079315185546875,0,0.2242584228515625,0,0.2418289184570312,0,0,0.2456512451171875,0,0.2458419799804688,0,0.2448959350585938,0.2434463500976562,0,0.2416305541992188,0,0.2430953979492188,0.13897705078125,0,0,0,-2.2984619140625,0.2076568603515625,0.2231369018554688,0.2381362915039062,0,0.2446441650390625,0,0.246337890625,0,0.2419815063476562,0,0.2444229125976562,0.2305908203125,0,0.2426223754882812,0.2277145385742188,0.02065277099609375,0,0,-2.388328552246094,0,0.19586181640625,0,0.2030487060546875,0,0.18988037109375,0.2113800048828125,0,0.194793701171875,0,0.2170486450195312,0,0.2293853759765625,0,0.2112350463867188,0.2328948974609375,0,0.2270278930664062,0.218017578125,0.1260910034179688,0,0,0,-2.244194030761719,0,0.2038650512695312,0,0,0.1917877197265625,0,0,0.210968017578125,0.2189254760742188,0,0.2281494140625,0,0,0.2128677368164062,0,0.2257919311523438,0,0.2386474609375,0,0.217620849609375,0,0.2445831298828125,0.1181182861328125,0,0,0,0,0,-2.190940856933594,0,0.2071533203125,0.2034835815429688,0,0.2128219604492188,0,0,0.2194900512695312,0.231292724609375,0,0.2413330078125,0.243316650390625,0.2443313598632812,0.24261474609375,0.2112884521484375,0,0,0,0,0,-2.2335205078125,0.2008132934570312,0.2071685791015625,0,0.2193603515625,0,0.2332839965820312,0.2440109252929688,0,0.2458953857421875,0.2417373657226562,0,0.2427520751953125,0,0.2443695068359375,0,0.2191696166992188,0,0,0,0,0,-2.184226989746094,0.1951370239257812,0.2043533325195312,0,0.19183349609375,0,0.2161865234375,0,0.1869125366210938,0.217193603515625,0,0,0.2309188842773438,0,0.2172927856445312,0.2359466552734375,0,0.2000656127929688,0,0,0.1523284912109375,0,0,0,0,0,-2.120704650878906,0,0.1977920532226562,0.173370361328125,0.2006759643554688,0,0.207977294921875,0,0.224456787109375,0,0.23577880859375,0,0.2353363037109375,0,0,0.2404022216796875,0,0.2230300903320312,0,0,0.2323074340820312,0,0.01263427734375,0,-2.140083312988281,0.191375732421875,0,0.2079391479492188,0,0.2158584594726562,0,0.2357101440429688,0,0.2461471557617188,0,0.2469100952148438,0,0.2445755004882812,0,0.2437362670898438,0.240081787109375,0,0,0.1296615600585938,0,0,0,0,0,-1.99871826171875,0,0.2002182006835938,0.210174560546875,0,0.2279205322265625,0,0.2419815063476562,0.2446136474609375,0,0.2256622314453125,0.2452163696289062,0.2451324462890625,0.2187652587890625,0,0,0,0,0,-2.047889709472656,0,0.1833877563476562,0,0.2069473266601562,0.2186355590820312,0.2384719848632812,0,0.2460174560546875,0.2470703125,0.2453155517578125,0.2452468872070312,0,0.2429275512695312,0.03382110595703125,0,0,0,0,0,-1.90625,0,0.1907730102539062,0,0.1882553100585938,0.1849212646484375,0.2133102416992188,0.2152328491210938,0,0.2339859008789062,0.2329940795898438,0,0.2190170288085938,0,0.2359695434570312,0,0.0507659912109375,0,0,0,-1.889511108398438,0.186920166015625,0,0.1984405517578125,0,0.2070770263671875,0,0.234649658203125,0.243377685546875,0,0.2457962036132812,0,0.2439193725585938,0,0.2429580688476562,0.14447021484375,0,0,0,0,0,-1.884765625,0,0.1933517456054688,0,0.2011642456054688,0.2215805053710938,0,0.2400970458984375,0.247894287109375,0,0.2496871948242188,0.2472457885742188,0.2446365356445312,0,0.09615325927734375,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.955986022949219,0,0.1699142456054688,0,0.1826858520507812,0.194549560546875,0,0.2058639526367188,0,0.22265625,0,0.2393875122070312,0,0.2475357055664062,0,0.244964599609375,0.244964599609375,0,0.05937957763671875,0,0,0,-1.778053283691406,0.197662353515625,0.2114028930664062,0,0,0.2326736450195312,0,0.2452926635742188,0.247314453125,0.2471923828125,0,0.2471771240234375,0.2046737670898438,0,0,0,0,0,-1.840835571289062,0,0.1920394897460938,0,0.20050048828125,0.2231597900390625,0.2425765991210938,0,0.2472305297851562,0,0.2484664916992188,0,0.2467193603515625,0,0.2437362670898438,0,0.0507659912109375,0,0,0,0,0,-1.695838928222656,0.1909561157226562,0,0.2096939086914062,0,0.228851318359375,0.2446136474609375,0.2463531494140625,0,0.245452880859375,0,0.2460250854492188,0,0.137420654296875,0,0,0,0,0,-1.746994018554688,0,0.177825927734375,0.2014541625976562,0.2231979370117188,0.2419281005859375,0,0.2469558715820312,0.2475662231445312,0,0.24652099609375,0,0,0.2142486572265625,0,0,0,0,0,-1.768051147460938,0.1884078979492188,0,0.1960067749023438,0,0.213714599609375,0.2359695434570312,0.244659423828125,0,0.2465438842773438,0.24456787109375,0.2360610961914062,0.01387786865234375,0,0,-1.774559020996094,0,0.168792724609375,0.19232177734375,0,0.2105941772460938,0,0.232147216796875,0,0.2467041015625,0,0.2472610473632812,0,0.2430496215820312,0,0.24078369140625,0,0.0438690185546875,0,0,0,0,0,-1.678352355957031,0,0.1691055297851562,0,0.1653594970703125,0,0.1736602783203125,0.19793701171875,0.2181320190429688,0,0.2266998291015625,0,0.232696533203125,0,0.2372512817382812,0,0,0.1077194213867188,0,0,0,0,0,-1.619857788085938,0,0,0.182373046875,0.1748733520507812,0.2084808349609375,0,0.20458984375,0.2419967651367188,0,0.21722412109375,0,0.22039794921875,0,0.2191925048828125,0,0,0,0,0,-1.695404052734375,0.1767044067382812,0,0.1796340942382812,0,0.198516845703125,0.2022552490234375,0,0.228546142578125,0.2355880737304688,0.2336273193359375,0.2396469116210938,0,0.0494842529296875,0,0,0,0,0,-1.531661987304688,0.1817474365234375,0,0,0.1884384155273438,0,0.2134475708007812,0.2205276489257812,0,0.2349395751953125,0,0.2357406616210938,0.2392730712890625,0.0652923583984375,0,0,0,0,0,-1.517311096191406,0,0.18670654296875,0,0,0.200592041015625,0,0.2184600830078125,0,0.2344207763671875,0,0.2421875,0,0.2422866821289062,0,0,0.2339553833007812,0.00566864013671875,0,-1.61566162109375,0,0.1851806640625,0,0.1919403076171875,0,0,0.2123031616210938,0.2293472290039062,0,0.2394027709960938,0,0.2469100952148438,0.221221923828125,0,0.1356277465820312,0,0,0,0,0,-1.579383850097656,0,0.153533935546875,0,0,0.1761703491210938,0,0,0.1714096069335938,0,0.1774444580078125,0,0,0.199005126953125,0,0.177764892578125,0,0.2124404907226562,0.2105712890625,0,0.1465377807617188,0,0,0,0,0,-1.532638549804688,0,0.1795120239257812,0,0.1850814819335938,0,0.1958465576171875,0,0.2206192016601562,0,0.2021026611328125,0,0.2219619750976562,0,0.2293472290039062,0,0.1428985595703125,0,0,0,0,0,-1.513725280761719,0.1595077514648438,0.1809844970703125,0,0.182098388671875,0,0.2137680053710938,0,0.2117996215820312,0,0.2123184204101562,0,0.2270126342773438,0,0.1702728271484375,0,0,0,0,0,-1.499176025390625,0,0.1719818115234375,0,0,0.191986083984375,0,0.191436767578125,0,0.2188491821289062,0.2233123779296875,0.2260284423828125,0,0.238983154296875,0.07989501953125,0,0,0,0,0,-1.372886657714844,0,0.18658447265625,0.1982192993164062,0.224700927734375,0.2410125732421875,0.2406463623046875,0,0.2364959716796875,0,0.087860107421875,0,0,0,-1.364639282226562,0.1891250610351562,0,0.2034149169921875,0.2247238159179688,0,0.24078369140625,0,0.2441024780273438,0,0.2384262084960938,0,0.06597900390625,0,0,0,0,0,-1.338699340820312,0,0.1893692016601562,0.1857833862304688,0,0.1972808837890625,0.2055892944335938,0.2072830200195312,0,0.2071914672851562,0.18743896484375,0,0,0,0,0,-1.405197143554688,0.17523193359375,0,0.1846389770507812,0,0.1993026733398438,0,0.2085342407226562,0,0.2226104736328125,0,0.218292236328125,0,0.218994140625,0,0.0182037353515625,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.397377014160156,0,0,0,0.1532516479492188,0,0.1898880004882812,0,0,0.206878662109375,0,0,0.2097015380859375,0,0,0.2221832275390625,0.225067138671875,0.2093734741210938,0,0.2340927124023438,0,0.2308883666992188,0.2252044677734375,0.2390594482421875,0.2060546875,0.18389892578125,0,0.1860809326171875,0.1789779663085938,0.1836700439453125,0,0.163543701171875,0,0.1849365234375,0,0.1633834838867188,0,0.1762008666992188,0,0.170562744140625,0,0.1821212768554688,0,0.1884613037109375,0,0.164581298828125,0,0.175140380859375,0,0.1668167114257812,0.04586029052734375,0,0,0,0,0,-4.777030944824219,0,0.1942596435546875,0,0.2054290771484375,0,0.2292251586914062,0,0.231964111328125,0,0.2193145751953125,0,0,0.2332229614257812,0,0,0.2451324462890625,0,0,0.2390594482421875,0.2182388305664062,0,0.2326431274414062,0,0.2367172241210938,0,0.224822998046875,0,0.2084732055664062,0,0.2272872924804688,0.2310409545898438,0,0,0.2316131591796875,0,0.23321533203125,0,0.2388153076171875,0,0.2397537231445312,0.2069473266601562,0.2088623046875,0,0.179534912109375,0,0,0,0,0,0,0,0,-4.601821899414062,0.2079544067382812,0,0.2214431762695312,0,0.2239608764648438,0,0.2132110595703125,0,0.2268447875976562,0,0,0.2365646362304688,0,0.2397232055664062,0,0.2173690795898438,0,0.2283248901367188,0,0.22509765625,0,0.2323532104492188,0,0.2281265258789062,0,0.2278976440429688,0.231475830078125,0,0.243377685546875,0,0.230804443359375,0.2148895263671875,0.20916748046875,0.209930419921875,0,0.2017364501953125,0,0.1974334716796875,0,0.07051849365234375,0,0,0,0,0,-4.639427185058594,0.1943588256835938,0,0.205322265625,0,0.2106246948242188,0.21173095703125,0.2195968627929688,0.2437286376953125,0,0.2443695068359375,0,0.2418746948242188,0,0.2301712036132812,0,0.223602294921875,0,0.24456787109375,0,0.243194580078125,0,0.2187881469726562,0.2239913940429688,0,0.241607666015625,0,0,0.21405029296875,0.2255096435546875,0,0.2400970458984375,0.2033615112304688,0,0.2339248657226562,0,0.1931533813476562,0,0,0.06584930419921875,0,0,0,-4.56536865234375,0,0.2017364501953125,0,0.1970748901367188,0,0.1972427368164062,0,0,0.2014389038085938,0,0.1765365600585938,0,0.2252883911132812,0,0.2219314575195312,0.2309722900390625,0.2207870483398438,0,0.2240447998046875,0,0.2432861328125,0.2415695190429688,0,0.2391891479492188,0,0,0.240386962890625,0,0.2405853271484375,0,0.242156982421875,0,0.2416229248046875,0,0.2447738647460938,0,0.24359130859375,0,0.2319869995117188,0,0.1912307739257812,0,0,0,0,0,-4.367706298828125,0,0.2081222534179688,0,0.1614456176757812,0.1482772827148438,0.1050796508789062,0,0,0.07842254638671875,0,0,0.1519393920898438,0,0.166015625,0,0.1974411010742188,0,0.1931686401367188,0,0.201507568359375,0.1438140869140625,0.1602096557617188,0,0.1958541870117188,0,0.1633453369140625,0.1418533325195312,0.160552978515625,0,0.0999603271484375,0.1021881103515625,0,0.09564208984375,0,0.09784698486328125,0,0.110565185546875,0,0.0853424072265625,0.0878448486328125,0,0.0968780517578125,0,0,0.086029052734375,0.0999755859375,0,0.10333251953125,0.1651229858398438,0,0.1929244995117188,0.2044219970703125,0.2059402465820312,0.086395263671875,0,0,0,0,0,-4.439033508300781,0,0.1968841552734375,0,0.2049560546875,0,0.2061843872070312,0,0.2183074951171875,0,0.23297119140625,0.2425994873046875,0,0.2311248779296875,0,0.2117767333984375,0,0.21246337890625,0,0.2313003540039062,0,0.2373428344726562,0.2390670776367188,0,0.2381362915039062,0,0.23919677734375,0,0.2395401000976562,0.2395172119140625,0.23138427734375,0,0.2311248779296875,0,0.2335357666015625,0,0.2254867553710938,0,0.02391815185546875,0,0,0,0,0,-4.283241271972656,0,0.20037841796875,0.2010498046875,0.2034912109375,0.2247314453125,0,0.2311019897460938,0,0.2369461059570312,0.2385787963867188,0,0.2374649047851562,0,0.2293167114257812,0,0.2272415161132812,0,0.23077392578125,0,0.2268524169921875,0.1199188232421875,0.1250686645507812,0,0.1926498413085938,0,0.2295913696289062,0.2303009033203125,0.2399063110351562,0.2325363159179688,0,0.2244796752929688,0.1265106201171875,0,0,0,0,0,-4.141510009765625,0.2023773193359375,0,0,0.2007217407226562,0.2200851440429688,0,0.1895675659179688,0.1273040771484375,0.1312713623046875,0,0.1825485229492188,0.1684112548828125,0,0.1509552001953125,0,0.1420669555664062,0,0.1029739379882812,0.1172714233398438,0,0,0.146148681640625,0.1502761840820312,0.1512222290039062,0,0,0.1713027954101562,0.15582275390625,0.1677474975585938,0,0.1780624389648438,0,0.1605453491210938,0,0.1197357177734375,0,0.1424484252929688,0,0,0.179840087890625,0,0.1977767944335938,0,0.1601943969726562,0.1677932739257812,0,0.08069610595703125,0,0,0,0,0,0,0,0,-4.209869384765625,0,0,0.1459732055664062,0,0.1554794311523438,0,0.1426544189453125,0,0.170196533203125,0,0.169586181640625,0.1994552612304688,0,0.2108001708984375,0.2005233764648438,0,0.199493408203125,0,0.2044906616210938,0,0.2032089233398438,0,0.1782379150390625,0,0,0.1511306762695312,0,0.1900253295898438,0,0.1179428100585938,0.1529388427734375,0,0.1098480224609375,0.1410980224609375,0,0.1948394775390625,0.1835098266601562,0,0.2006072998046875,0.2175827026367188,0.2288818359375,0.2227935791015625,0,0.04016876220703125,0,0,0,0,0,-4.15472412109375,0,0.1885299682617188,0.1878662109375,0,0.1867294311523438,0,0,0.194580078125,0,0.2167739868164062,0,0.223846435546875,0.2208175659179688,0,0.2236862182617188,0,0.2381210327148438,0,0,0.2336044311523438,0.2402191162109375,0,0.2422714233398438,0.2436141967773438,0,0.2421035766601562,0.2428741455078125,0,0.2450180053710938,0.2439117431640625,0.2366714477539062,0,0.2231979370117188,0,0,0,0,0,0,0,0,-4.018875122070312,0,0.1890487670898438,0,0.1837310791015625,0.200347900390625,0,0,0.1570968627929688,0,0.2082672119140625,0,0.1828689575195312,0.2233810424804688,0,0.235260009765625,0,0.2330169677734375,0,0.2354888916015625,0.2369232177734375,0,0.23480224609375,0,0.2370986938476562,0.231903076171875,0,0.23199462890625,0,0.2409133911132812,0,0.2363662719726562,0,0.2320556640625,0.2060012817382812,0,0,0,0,0,-3.943862915039062,0.1630859375,0,0.1805267333984375,0,0,0.1988067626953125,0,0,0.1989669799804688,0,0.2160797119140625,0.2200469970703125,0,0.2285919189453125,0,0.20062255859375,0,0.1706924438476562,0,0.21282958984375,0,0.1909408569335938,0,0,0.1807937622070312,0.1863021850585938,0,0,0.2142562866210938,0,0.20306396484375,0,0.2319183349609375,0.2079391479492188,0,0.1987075805664062,0,0.2252426147460938,0,0.1878509521484375,0.042449951171875,0,0,0,-3.954154968261719,0,0.1871185302734375,0.16156005859375,0,0.1979598999023438,0,0,0.1803741455078125,0,0.183349609375,0,0.2155532836914062,0.2003250122070312,0,0.2218704223632812,0.2132034301757812,0,0.2082595825195312,0,0.2341156005859375,0.2093429565429688,0,0.2272415161132812,0.22265625,0,0.210174560546875,0,0.2418746948242188,0.2103271484375,0.2233963012695312,0,0.2197418212890625,0,0.0996856689453125,0,0,0,0,0,-3.78594970703125,0,0.18194580078125,0.1672286987304688,0,0.1936111450195312,0,0.1968917846679688,0,0.1892852783203125,0,0.2113037109375,0,0.23333740234375,0,0.2395248413085938,0.2388458251953125,0,0.2389984130859375,0,0,0.23974609375,0.2391738891601562,0.2413864135742188,0,0.2425308227539062,0,0.2439117431640625,0,0,0.24371337890625,0.232025146484375,0,0.1246185302734375,0,0,0,0,0,-3.696182250976562,0,0.1847610473632812,0,0.1956787109375,0,0.2012481689453125,0,0.2018585205078125,0,0.222808837890625,0,0.2356491088867188,0,0.2304000854492188,0.2378387451171875,0.2364959716796875,0,0.2389907836914062,0,0.2406082153320312,0,0.24127197265625,0,0.241363525390625,0.242279052734375,0.2394561767578125,0,0.2335586547851562,0.1823196411132812,0,0,0,0,0,-3.660346984863281,0,0.1819686889648438,0,0.1976394653320312,0,0.2037124633789062,0,0.2128143310546875,0.2269210815429688,0,0,0.2417984008789062,0,0,0.2423324584960938,0,0.1877593994140625,0,0,0.1695022583007812,0,0.2331924438476562,0,0.242156982421875,0.242584228515625,0.24176025390625,0,0.2423934936523438,0.2438583374023438,0,0,0.2377548217773438,0,0,0.2207260131835938,0,0,0,0,0,0,0,0,-3.631118774414062,0,0.1827163696289062,0.1954193115234375,0,0.2039260864257812,0,0.2182998657226562,0,0.2264404296875,0.2410049438476562,0,0.2404022216796875,0,0,0.2404251098632812,0,0.239166259765625,0,0.2411346435546875,0.2424545288085938,0,0.241790771484375,0,0.2423477172851562,0,0.2331924438476562,0.1812667846679688,0,0.2191696166992188,0,0.1488037109375,0,0,0,0,0,0,0,0,-3.578643798828125,0.149200439453125,0,0.1891632080078125,0,0.1886978149414062,0.1791305541992188,0,0.2049331665039062,0,0.2076339721679688,0.2254867553710938,0.2274169921875,0.2222747802734375,0,0.23968505859375,0,0.2251434326171875,0,0.2327194213867188,0,0.236358642578125,0,0.2305068969726562,0.243804931640625,0,0.2335433959960938,0,0,0.217987060546875,0.03000640869140625,0,0,0,-3.564468383789062,0,0,0.1687850952148438,0,0.1811447143554688,0,0.1865463256835938,0.1808700561523438,0,0,0.2031784057617188,0.2017974853515625,0.2153091430664062,0,0.235687255859375,0,0,0.2245864868164062,0,0.2397689819335938,0.2231597900390625,0,0.223358154296875,0,0.2402267456054688,0,0.2254867553710938,0,0.2394180297851562,0.220916748046875,0,0.2134933471679688,0,0.044219970703125,0,0,0,0,0,-3.466285705566406,0,0.1752853393554688,0,0.1306076049804688,0.1503219604492188,0,0.175872802734375,0,0.1267013549804688,0.1580581665039062,0,0.1761093139648438,0.1501388549804688,0,0.1726303100585938,0,0,0.1424636840820312,0,0.1456832885742188,0,0.1807708740234375,0.1278610229492188,0,0.1788177490234375,0,0.1204299926757812,0.1324386596679688,0,0,0.1676254272460938,0.1145553588867188,0,0.16778564453125,0.1608123779296875,0.1556930541992188,0,0.1834259033203125,0.1464691162109375,0,0.027374267578125,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-3.388816833496094,0,0.15966796875,0.1777572631835938,0.1867828369140625,0.1933670043945312,0.2067108154296875,0.2254180908203125,0,0.2386474609375,0,0.2388458251953125,0,0,0.23583984375,0,0.2351531982421875,0,0.2387847900390625,0.2403488159179688,0.2410049438476562,0,0.2406158447265625,0,0.23577880859375,0.1939010620117188,0,0,0,0,0,-3.335289001464844,0,0.183013916015625,0,0.1865768432617188,0,0.1954879760742188,0.2117919921875,0,0.2222824096679688,0,0.2383041381835938,0,0.2390289306640625,0,0.238983154296875,0,0,0.2365036010742188,0.23724365234375,0,0.2391738891601562,0,0.2384719848632812,0,0.2395858764648438,0,0.2419509887695312,0,0,0.23089599609375,0,0.0544281005859375,0,0,0,0,0,0,0,-3.345306396484375,0,0.1797103881835938,0,0.186370849609375,0,0,0.1872100830078125,0,0.1978378295898438,0.211883544921875,0,0.2267379760742188,0,0,0.2255020141601562,0,0.2055740356445312,0.232391357421875,0,0.2375259399414062,0.2408065795898438,0,0.2406005859375,0,0.2421493530273438,0,0.2430343627929688,0,0.2346343994140625,0,0.1502609252929688,0,0,0,0,0,-3.203857421875,0,0.1731948852539062,0,0.1858291625976562,0,0.1886444091796875,0,0.1737213134765625,0,0.184417724609375,0,0.2038955688476562,0,0.2258987426757812,0.1695098876953125,0,0.1873779296875,0,0.1679153442382812,0,0.1820144653320312,0,0.1719131469726562,0,0.1642303466796875,0.1832656860351562,0.1449432373046875,0.1754837036132812,0.1749420166015625,0.159088134765625,0,0.08289337158203125,0,0,0,0,0,0,0,-3.192703247070312,0,0.1487808227539062,0.1478195190429688,0.1448898315429688,0,0.1670761108398438,0,0,0.1360244750976562,0,0.1664581298828125,0,0.1716537475585938,0,0.15948486328125,0,0.17510986328125,0.1317977905273438,0,0.173370361328125,0,0.1811447143554688,0.2133636474609375,0,0.2291336059570312,0,0.2392044067382812,0,0.2430572509765625,0.2397003173828125,0,0.2184219360351562,0,0,0,0,0,0,0,0,-3.156364440917969,0,0.1654739379882812,0,0.1859893798828125,0.188812255859375,0,0.1991958618164062,0,0,0.2195281982421875,0,0.2331695556640625,0,0.2447967529296875,0,0.2418441772460938,0,0.2421798706054688,0.2329788208007812,0,0.1837692260742188,0,0.2206954956054688,0,0.1865234375,0.1642684936523438,0,0.2200927734375,0.1192855834960938,0,0,0,0,0,0,0,0,-3.041938781738281,0,0.173431396484375,0,0.1819229125976562,0,0.1898727416992188,0,0.2005462646484375,0,0.2184906005859375,0,0,0.23834228515625,0.2366714477539062,0,0,0.2416763305664062,0.2339630126953125,0.2364730834960938,0,0.2379608154296875,0,0.2432708740234375,0.2453994750976562,0,0,0.230255126953125,0.02449798583984375,0,0,0,-3.069969177246094,0,0.1655120849609375,0,0.1875457763671875,0,0.1904220581054688,0,0.196746826171875,0.2145919799804688,0,0.22808837890625,0,0.2396926879882812,0,0.2446136474609375,0,0.2454757690429688,0.2429351806640625,0.2444915771484375,0.2451858520507812,0,0.24566650390625,0,0.2318649291992188,0,0.03643798828125,0,0,0,-3.035957336425781,0,0.1741943359375,0,0.178863525390625,0,0.1894760131835938,0,0.1930389404296875,0,0,0.2067184448242188,0,0,0.2224655151367188,0,0.2349624633789062,0,0.2418212890625,0,0.2407379150390625,0.2374801635742188,0,0.2424468994140625,0.2433853149414062,0,0.2439346313476562,0,0.2317962646484375,0,0.0424957275390625,0,0,0,0,0,0,0,0,-2.968032836914062,0.1599807739257812,0,0.1459808349609375,0,0.1732025146484375,0,0.1809234619140625,0.183685302734375,0,0,0.1900787353515625,0.1763229370117188,0,0,0.1911849975585938,0.1877059936523438,0.1903152465820312,0,0.1974105834960938,0,0.1782989501953125,0,0.1998519897460938,0.1925582885742188,0,0.1863555908203125,0,0.1964950561523438,0,0.1242294311523438,0,0,0,0,0,0,0,0,0,0,0,-2.880218505859375,0,0.1442184448242188,0,0.1611251831054688,0,0.1714630126953125,0,0.175262451171875,0,0,0.196929931640625,0.2048873901367188,0,0.225860595703125,0,0,0.2311019897460938,0,0.24090576171875,0,0.238311767578125,0,0.2409820556640625,0.2433853149414062,0.2415618896484375,0.229705810546875,0,0.0195159912109375,0,0,0,0,0,-2.894783020019531,0,0.1683425903320312,0.181365966796875,0,0.188079833984375,0.18768310546875,0.16998291015625,0,0.2054824829101562,0,0.2235565185546875,0,0.22918701171875,0,0,0.2370529174804688,0,0.2364959716796875,0.2402725219726562,0,0.2397384643554688,0,0.2368392944335938,0,0.22430419921875,0,0.0101470947265625,0,0,0,0,0,-2.847724914550781,0,0.1678237915039062,0,0.1763229370117188,0,0.1859130859375,0.193603515625,0,0.2089462280273438,0.2257766723632812,0.2373504638671875,0.2379608154296875,0,0.2044830322265625,0.2134857177734375,0.2387161254882812,0,0.240020751953125,0,0,0.2376174926757812,0,0.1619720458984375,0,0,0,0,0,-2.723541259765625,0,0.1777801513671875,0,0.187591552734375,0,0.194793701171875,0,0.21087646484375,0.2311172485351562,0,0.2436141967773438,0,0.2405319213867188,0,0,0.240753173828125,0,0,0.2414779663085938,0,0.2425308227539062,0,0.2462692260742188,0.2365875244140625,0,0.1107101440429688,0,0,0,0,0,-2.628150939941406,0.1788558959960938,0,0.1910476684570312,0.19921875,0,0.2188339233398438,0.2345657348632812,0,0,0.2438583374023438,0.244659423828125,0,0.2432327270507812,0,0.2417831420898438,0,0.2432479858398438,0,0.2444534301757812,0.224029541015625,0,0,0,0,0,0,0,0,-2.681854248046875,0,0.176513671875,0.185546875,0.19158935546875,0,0.2065505981445312,0,0.226837158203125,0,0.24029541015625,0.245269775390625,0,0,0.2441940307617188,0.2423934936523438,0,0.2423171997070312,0.2443313598632812,0,0.2363128662109375,0,0.078125,0,0,0,0,0,-2.694297790527344,0,0.1568984985351562,0,0.1610641479492188,0.1868972778320312,0,0.1860580444335938,0.19195556640625,0,0.193145751953125,0,0.2211151123046875,0,0.2293548583984375,0,0,0.1863327026367188,0.2264404296875,0.2376937866210938,0.2290420532226562,0,0.2349319458007812,0,0.13055419921875,0,0,0,0,0,0,0,0,0,0,0,-2.618003845214844,0.120086669921875,0.1420211791992188,0,0.1639175415039062,0,0.1398162841796875,0.1760025024414062,0.1703872680664062,0.1739120483398438,0,0.1823272705078125,0,0,0.1582565307617188,0,0.18878173828125,0.1729049682617188,0,0.179656982421875,0,0.1879501342773438,0,0.168792724609375,0.19091796875,0,0.1711196899414062,0,0.00701141357421875,0,0,0,0,0,0,0,0,-2.60638427734375,0.1297531127929688,0.1417236328125,0,0.1708984375,0.152313232421875,0.1700363159179688,0,0.1809310913085938,0,0.167388916015625,0,0.19549560546875,0,0.1803741455078125,0,0.2050247192382812,0,0.22882080078125,0.2375564575195312,0,0.2452850341796875,0,0.2335739135742188,0,0.04192352294921875,0,0,0,0,0,-2.564430236816406,0.1668014526367188,0.1816787719726562,0.1897354125976562,0,0.1984634399414062,0.2229232788085938,0,0.23736572265625,0,0.2453155517578125,0,0.2429122924804688,0.2425079345703125,0,0.24285888671875,0.244720458984375,0,0.2225570678710938,0,0,0,0,0,0,0,0,-2.46392822265625,0,0.1768951416015625,0,0.18939208984375,0.1974716186523438,0.2150650024414062,0,0.2342681884765625,0.2452545166015625,0,0.210601806640625,0,0.1458511352539062,0.2163619995117188,0,0.1434707641601562,0,0.1712875366210938,0,0.1596755981445312,0,0.1526947021484375,0,0.07794189453125,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2.488365173339844,0,0,0,0.104156494140625,0,0.1599349975585938,0.175750732421875,0.187713623046875,0.1967697143554688,0,0.2172927856445312,0.2344436645507812,0.2445602416992188,0,0.2249374389648438,0,0.23162841796875,0,0.234832763671875,0,0.24456787109375,0.1026687622070312,0,0,0,0,0,0,0,0,-2.297752380371094,0.1810150146484375,0,0.190887451171875,0,0.2026290893554688,0.2249908447265625,0,0.2167129516601562,0,0.1931991577148438,0,0.2349624633789062,0,0.1818008422851562,0,0.2232208251953125,0,0,0.1751174926757812,0,0.1981658935546875,0.145050048828125,0,0,0,0,0,0,0,0,0,0,0,-2.39483642578125,0,0.1295700073242188,0.1415634155273438,0,0.1617813110351562,0,0.1498870849609375,0,0.1675949096679688,0,0.1792755126953125,0,0.1600494384765625,0,0.1873397827148438,0.1744766235351562,0,0.18975830078125,0.2007064819335938,0,0,0.1713027954101562,0,0.187408447265625,0.1633224487304688,0,0.09966278076171875,0,0,0,0,0,0,0,0,0,0,0,-2.348175048828125,0,0,0.1484451293945312,0,0,0.1731719970703125,0,0.1830902099609375,0,0.1917953491210938,0.2087936401367188,0,0.22509765625,0,0.2414703369140625,0,0,0.2394180297851562,0.2382278442382812,0,0.2385177612304688,0.2342071533203125,0,0.0937042236328125,0,0,0,0,0,0,0,0,-2.196037292480469,0,0.1783523559570312,0,0.1884536743164062,0,0.2007598876953125,0.2233657836914062,0,0.23602294921875,0,0.2430343627929688,0.240875244140625,0,0.2429656982421875,0.242340087890625,0.243499755859375,0.02304840087890625,0,0,0,-2.261451721191406,0,0.1747055053710938,0,0.1883468627929688,0,0.1939163208007812,0.21435546875,0,0.23199462890625,0,0.2437210083007812,0.2453155517578125,0,0.2437667846679688,0,0.2449493408203125,0,0.2430343627929688,0,0.1029586791992188,0,0,0,0,0,-2.117050170898438,0,0.1786422729492188,0,0.1930084228515625,0,0,0.2009201049804688,0,0.2105636596679688,0,0.2349929809570312,0,0.2451324462890625,0,0.2428359985351562,0,0.243896484375,0.2434005737304688,0,0.1882247924804688,0,0,0,0,0,-2.14990234375,0,0.1752777099609375,0,0.186553955078125,0,0,0.1975479125976562,0,0.2108154296875,0.2294769287109375,0,0.2389984130859375,0,0.2455291748046875,0,0.2421646118164062,0,0.24542236328125,0.2416458129882812,0,0,0,0,0,0,0,0,-2.157127380371094,0,0.1709823608398438,0.1821441650390625,0.1957778930664062,0,0.2068939208984375,0,0.223724365234375,0,0.2186431884765625,0,0.2165374755859375,0,0.2278213500976562,0.2436676025390625,0,0.2432479858398438,0,0.090179443359375,0,0,0,0,0,0,0,0,-2.025169372558594,0,0.1746673583984375,0.1885910034179688,0,0,0.1948776245117188,0.2132568359375,0.1948165893554688,0,0.190704345703125,0.231475830078125,0,0.2441329956054688,0.2452850341796875,0,0.20880126953125,0,0,0,0,0,0,0,0,-2.066558837890625,0,0,0.1751174926757812,0,0.1850051879882812,0.1961135864257812,0,0.2114486694335938,0.1998672485351562,0.1553192138671875,0,0.2204437255859375,0.2193450927734375,0,0.2340621948242188,0,0.2341690063476562,0.096099853515625,0,0,0,0,0,-1.994064331054688,0,0.168121337890625,0,0,0.1741104125976562,0.1978836059570312,0,0.1970443725585938,0.2095184326171875,0.2268905639648438,0,0.2245025634765625,0,0.242156982421875,0,0.2353134155273438,0.1780548095703125,0,0,0,0,0,0,0,0,-1.996604919433594,0.1617889404296875,0.1653518676757812,0,0.1954269409179688,0,0.1856536865234375,0.2167282104492188,0,0.212554931640625,0.2212066650390625,0.2428970336914062,0,0,0.2283248901367188,0.2251129150390625,0,0,0,0,0,0,0,0,-2.005874633789062,0.1573333740234375,0,0.170806884765625,0,0.18756103515625,0,0.1840286254882812,0,0.2205734252929688,0,0.2037277221679688,0.2204666137695312,0.2333831787109375,0.209869384765625,0,0.2361984252929688,0.039581298828125,0,0,0,0,0,-1.828147888183594,0,0.1772537231445312,0,0.1936569213867188,0.2013168334960938,0,0.220458984375,0,0.2389755249023438,0,0.2456283569335938,0,0.243560791015625,0,0.2432708740234375,0,0.1206207275390625,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.881736755371094,0,0,0.1576309204101562,0.1785125732421875,0.1913299560546875,0,0.2030105590820312,0,0.2173080444335938,0,0.224609375,0.1424560546875,0,0.207794189453125,0.181793212890625,0.1610870361328125,0.07171630859375,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.918197631835938,0,0,0,0,0,0.0084075927734375,0,0.1916427612304688,0,0.2025146484375,0,0.212005615234375,0.2296524047851562,0,0,0.2452926635742188,0.2425765991210938,0.2298507690429688,0,0.2096633911132812,0,0.2281036376953125,0,0.2342605590820312,0,0.2432479858398438,0,0.2459793090820312,0,0.2451629638671875,0,0,0.24444580078125,0,0.2461776733398438,0,0.2460403442382812,0,0.2463302612304688,0.195831298828125,0,0.1935501098632812,0,0.1921463012695312,0,0.1939010620117188,0,0.1922149658203125,0.1957626342773438,0,0.194091796875,0,0.1974639892578125,0.1977615356445312,0.1964645385742188,0.1977615356445312,0,0.1921615600585938,0,0.1983108520507812,0,0,0.1961898803710938,0,0.1975555419921875,0,0.1951522827148438,0,0.1981124877929688,0,0,0.1945648193359375,0,0.1967239379882812,0,0.1973495483398438,0.07535552978515625,0,0,0,0,0,0,0,0,-7.531349182128906,0.198883056640625,0.2091140747070312,0,0.22357177734375,0,0.24072265625,0,0.243560791015625,0,0.2291717529296875,0,0.18939208984375,0,0.2137985229492188,0.2367935180664062,0,0.1809539794921875,0,0.1715545654296875,0,0.2084808349609375,0,0.1733932495117188,0,0.2144088745117188,0,0.2330398559570312,0,0.2291488647460938,0.233734130859375,0,0.240966796875,0,0.2336959838867188,0,0.2418060302734375,0,0.2333831787109375,0,0.2353363037109375,0,0,0.2402572631835938,0,0.228790283203125,0,0.2414321899414062,0,0.232574462890625,0.2293167114257812,0,0.2430572509765625,0,0.231231689453125,0,0.23992919921875,0,0.2366485595703125,0,0.2304534912109375,0,0.2288360595703125,0.218780517578125,0,0.1323013305664062,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-7.344680786132812,0,0.191558837890625,0,0.2030563354492188,0,0.2020721435546875,0.223846435546875,0,0.21478271484375,0.2085723876953125,0,0.2170639038085938,0,0.226715087890625,0,0.2357406616210938,0.236114501953125,0,0.2240829467773438,0.2351531982421875,0,0.2416305541992188,0,0.2421417236328125,0.243804931640625,0,0.2462997436523438,0,0.2476730346679688,0.2455902099609375,0,0.244964599609375,0.249542236328125,0,0.2526702880859375,0,0.254486083984375,0,0.2551727294921875,0.2550125122070312,0.2559661865234375,0,0.2528610229492188,0.2491531372070312,0,0.2441177368164062,0.2432022094726562,0,0.2427902221679688,0,0.240753173828125,0.2317047119140625,0,0,0,0,0,0,0,-7.244758605957031,0,0.1972579956054688,0,0.2087783813476562,0,0.22320556640625,0.2299957275390625,0.2294464111328125,0,0.2254562377929688,0,0.24847412109375,0,0.2472991943359375,0,0.2440414428710938,0,0.2461700439453125,0.2457351684570312,0.2500076293945312,0,0.2550735473632812,0.25238037109375,0,0.1947784423828125,0.2419967651367188,0,0.2409133911132812,0.2418289184570312,0,0,0.2430267333984375,0,0.2430877685546875,0,0.2419815063476562,0.24261474609375,0.2432403564453125,0,0.2428436279296875,0,0.2437591552734375,0,0.2438888549804688,0,0.2439117431640625,0,0.24530029296875,0,0.2422256469726562,0,0.2317352294921875,0,0.2319259643554688,0.09259033203125,0,0,0,0,0,0,0,0,0,0,0,-7.076957702636719,0,0.1972503662109375,0,0,0.2065811157226562,0.2038497924804688,0,0.1944427490234375,0,0,0.1812286376953125,0,0.18853759765625,0.2065200805664062,0,0.2201995849609375,0,0.23529052734375,0,0.2398605346679688,0,0.2349624633789062,0,0.2415313720703125,0.2433090209960938,0,0.241455078125,0.2443923950195312,0.24395751953125,0.242218017578125,0,0.2435150146484375,0,0.2431488037109375,0.2441329956054688,0.2432098388671875,0.2446746826171875,0,0.2450790405273438,0.2448043823242188,0,0.246246337890625,0.2463150024414062,0,0.2449798583984375,0,0,0.2465133666992188,0.24591064453125,0.2271957397460938,0,0,0.2321624755859375,0,0,0.1203460693359375,0,0,0,0,0,0,0,-6.988265991210938,0,0.1961669921875,0,0.2063980102539062,0,0.2058639526367188,0.2082901000976562,0,0.2117691040039062,0,0.2417373657226562,0.24359130859375,0.2439804077148438,0.2420883178710938,0.242584228515625,0.2429733276367188,0,0.2428665161132812,0,0,0.2423095703125,0.2426834106445312,0,0.2439804077148438,0.2431411743164062,0,0.2420501708984375,0.2412796020507812,0.2423324584960938,0.24163818359375,0.2431640625,0,0,0.2434234619140625,0.2437362670898438,0.2452774047851562,0,0.2447738647460938,0,0.2451248168945312,0.24609375,0.2463302612304688,0,0.2312469482421875,0,0.2287063598632812,0.106109619140625,0,0,0,0,0,0,0,0,0,0,0,-6.865348815917969,0,0.1949539184570312,0.2036285400390625,0.2004928588867188,0,0.2039566040039062,0,0.2149734497070312,0.2440185546875,0.2441482543945312,0,0.2445526123046875,0.2419815063476562,0.2437744140625,0,0.2441787719726562,0.2445220947265625,0,0.214813232421875,0.2411041259765625,0.2412261962890625,0,0.2410888671875,0.2404708862304688,0.2428817749023438,0.2433319091796875,0,0.243896484375,0,0,0.2442398071289062,0,0.242523193359375,0,0.2463531494140625,0.246368408203125,0,0.2548294067382812,0,0.2538986206054688,0,0,0.2556610107421875,0,0.243499755859375,0.239990234375,0.2042007446289062,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-6.781349182128906,0,0.179931640625,0.1957855224609375,0,0.1937179565429688,0,0.1914520263671875,0,0.2069320678710938,0.2332077026367188,0.2445449829101562,0.2419815063476562,0,0.24005126953125,0,0.2408981323242188,0.2423858642578125,0,0,0.2415008544921875,0.2424468994140625,0,0.2367401123046875,0,0,0.2399215698242188,0.2419204711914062,0,0.2405776977539062,0,0.2425537109375,0,0.247039794921875,0,0.2550125122070312,0.2538375854492188,0,0.2546157836914062,0.2556686401367188,0,0.254638671875,0,0.2541122436523438,0,0.2558135986328125,0,0.2557220458984375,0.243621826171875,0.2415695190429688,0,0.1100234985351562,0,0,0,0,0,0,0,-6.636138916015625,0,0,0.1961593627929688,0,0.198638916015625,0,0.1981430053710938,0,0.2138748168945312,0,0.2349853515625,0,0.2466964721679688,0.2434616088867188,0.238922119140625,0.2398910522460938,0,0.2414398193359375,0.2407684326171875,0,0.240631103515625,0.2408599853515625,0,0.2406463623046875,0,0.2422714233398438,0,0.238128662109375,0,0.2421798706054688,0,0,0.2419662475585938,0,0.2440643310546875,0.2439117431640625,0,0.2422256469726562,0,0.2440719604492188,0,0.2449111938476562,0.256439208984375,0,0.2564926147460938,0,0.256072998046875,0.2484283447265625,0,0,0.235992431640625,0.1776580810546875,0,0,0,0,0,0,0,-6.590202331542969,0,0.1861801147460938,0,0.1948165893554688,0,0.19140625,0,0.2009201049804688,0,0.2295379638671875,0,0.2442626953125,0,0.2444229125976562,0,0.2425384521484375,0,0,0.2398834228515625,0,0.2410659790039062,0.2411727905273438,0.240875244140625,0,0.2408065795898438,0.2412796020507812,0.2415847778320312,0,0,0.2424850463867188,0.242889404296875,0,0,0.211669921875,0.2318496704101562,0.2436141967773438,0,0.2428054809570312,0.2432632446289062,0,0.2437362670898438,0,0.2449874877929688,0,0.2435760498046875,0,0.24359130859375,0.2413864135742188,0,0.2305755615234375,0,0.2341537475585938,0.01958465576171875,0,0,0,0,0,0,0,0,0,0,0,-6.395851135253906,0,0.1894989013671875,0,0.1905899047851562,0,0,0.185302734375,0,7.816864013671875,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7.62939453125,0,0,7.62939453125e-06,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,15.2587890625,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"filename":[null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null]},"interval":10,"files":[],"prof_output":"/tmp/Rtmpk0VTqr/file27697d689b25.prof","highlight":{"output":["^output\\$"],"gc":["^<GC>$"],"stacktrace":["^\\.\\.stacktraceo(n|ff)\\.\\.$"]},"split":"h"}},"evals":[],"jsHooks":[]}</script>
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
##  mean1(x, 0.5) 32.33647 33.09313 33.52699 33.12929 33.17716 43.16296   100  a 
##  mean2(x, 0.5) 30.39817 31.70594 32.44638 31.73242 31.76939 43.23818   100   b
##  mean3(x, 0.5) 32.35873 33.08039 33.41836 33.11147 33.16153 43.05426   100  a
```

**Vectorize**.

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
##    expr       min       lq      mean    median        uq      max neval cld
##  ma1(y) 230.93547 235.1598 239.58282 236.80274 240.88109 262.1204   100  a 
##  ma2(y)  25.82273  27.8113  36.86629  34.88936  38.63891 220.3427   100   b
```
Likewise, matrix operations are often faster than vector operations.


**Packages**.

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
##   0.606   0.053   0.264
```

``` r
system.time({ .lm.fit(X, Y) })
```

```
##    user  system elapsed 
##   0.112   0.000   0.040
```

``` r
system.time({ solve(t(X)%*%X) %*% (t(X)%*%Y) })
```

```
##    user  system elapsed 
##   0.028   0.000   0.024
```
Note that such functions to have fewer checks and return less information, so you must know exactly what you are putting in and getting out.


**Parallel**.

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
##   0.035   0.003   0.038
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
##   1.340   0.333   0.928
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


**Compiled Code**.

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


**Memory Usage**.

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


**Example: Histogram**.
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

The current version of R (and any packages) used to make this document are

``` r
sessionInfo()
```

```
## R version 4.4.2 (2024-10-31)
## Platform: x86_64-redhat-linux-gnu
## Running under: Fedora Linux 40 (Workstation Edition)
## 
## Matrix products: default
## BLAS/LAPACK: FlexiBLAS OPENBLAS-OPENMP;  LAPACK version 3.12.0
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
## [1] Rcpp_1.0.14          profvis_0.4.0        microbenchmark_1.5.0
## [4] sf_1.0-19            plotly_4.10.4        ggplot2_3.5.1       
## [7] colorout_1.3-2      
## 
## loaded via a namespace (and not attached):
##  [1] sandwich_3.1-1     sass_0.4.9         generics_0.1.3     tidyr_1.3.1       
##  [5] class_7.3-23       KernSmooth_2.23-26 lattice_0.22-6     digest_0.6.37     
##  [9] magrittr_2.0.3     evaluate_1.0.3     grid_4.4.2         bookdown_0.42     
## [13] mvtnorm_1.3-3      fastmap_1.2.0      Matrix_1.7-2       jsonlite_1.8.9    
## [17] e1071_1.7-16       DBI_1.2.3          survival_3.8-3     multcomp_1.4-28   
## [21] httr_1.4.7         purrr_1.0.4        crosstalk_1.2.1    viridisLite_0.4.2 
## [25] scales_1.3.0       TH.data_1.1-3      codetools_0.2-20   lazyeval_0.2.2    
## [29] jquerylib_0.1.4    cli_3.6.3          rlang_1.1.5        units_0.8-5       
## [33] splines_4.4.2      munsell_0.5.1      withr_3.0.2        cachem_1.1.0      
## [37] yaml_2.3.10        tools_4.4.2        dplyr_1.1.4        colorspace_2.1-1  
## [41] vctrs_0.6.5        R6_2.5.1           zoo_1.8-12         proxy_0.4-27      
## [45] lifecycle_1.0.4    classInt_0.4-11    htmlwidgets_1.6.4  MASS_7.3-64       
## [49] pkgconfig_2.0.3    pillar_1.10.1      bslib_0.9.0        gtable_0.3.6      
## [53] data.table_1.16.4  glue_1.8.0         xfun_0.50          tibble_3.2.1      
## [57] tidyselect_1.2.1   knitr_1.49         htmltools_0.5.8.1  rmarkdown_2.29
```
With Rstudio, you can update both R and Rstudio.

## Latest versions

Make sure R is up to date.

Make sure your R packages are up to date.

``` r
update.packages()
```

After updating R, you can update *all* packages stored in *all* `.libPaths()` with the following command

``` r
update.packages(checkBuilt=T, ask=F)
# install.packages(old.packages(checkBuilt=T)[,"Package"])
```

**Used Rarely:**

To find specific broken packages after an update

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



