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
<div class="plotly html-widget html-fill-item" id="htmlwidget-118caa4a402ddbb8dccd" style="width:672px;height:480px;"></div>
<script type="application/json" data-for="htmlwidget-118caa4a402ddbb8dccd">{"x":{"visdat":{"446b348d4fa0":["function () ","plotlyVisDat"]},"cur_data":"446b348d4fa0","attrs":{"446b348d4fa0":{"x":{},"y":{},"alpha_stroke":1,"sizes":[10,100],"spans":[1,20]}},"layout":{"margin":{"b":40,"l":60,"t":25,"r":10},"xaxis":{"domain":[0,1],"automargin":true,"title":"X"},"yaxis":{"domain":[0,1],"automargin":true,"title":"Y"},"hovermode":"closest","showlegend":false},"source":"A","config":{"modeBarButtonsToAdd":["hoverclosest","hovercompare"],"showSendToCloud":false},"data":[{"x":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100],"y":[1.2583930998990014,8.8010793299408974,9.6382426952997573,18.313018747754093,20.372908489827054,26.637330576212729,31.325582846522416,32.573118436477181,32.670014294413754,43.340109951816459,41.35116700021576,47.311932297705233,50.57926526310775,54.748979322129443,58.363560662928386,62.134446527089899,68.091882069534563,72.020353723054171,78.591756909518168,81.152587214575604,86.16188716520594,89.318185020548981,91.18463037450455,98.051488987653713,97.279701249946328,106.70068574454473,108.83409145664089,111.85310379868979,114.67911865818867,116.32994003683966,125.16904056518059,127.62392594870475,132.19861447168316,132.30863853901926,139.77844393191444,142.42416956001216,148.09167206559565,152.2575066674957,157.17709429256999,160.87671792742381,162.49599454196124,169.25509479491794,169.18967504033975,175.32261014148006,178.12958898116287,183.25185442982968,191.71573385583912,190.48845146438364,199.39945335761749,200.18449617323361,203.48951393926072,205.10234257578944,210.48755774506964,213.98780173161293,221.75980324176558,223.9547549027198,225.23089205903923,231.16528219428724,236.86371655220628,239.80882541990442,245.76428413044999,246.33196298079739,253.00382608519402,256.41092938049718,257.41036979781569,264.20469609595489,267.68908201828287,268.46810565428876,273.20247171512096,277.57855779388257,283.04331114157628,287.60940324101381,292.49496272543922,291.81772165789624,299.74074277451172,305.01992838614689,309.38208878971727,310.41227833489506,315.53719081601514,318.8290836201333,327.08356527613029,331.06324489099785,331.43716183870862,335.86512763947832,339.20729050186907,343.85267746165886,349.02840084898497,347.51565892805615,359.68429123741356,359.11645887857509,361.05627227237596,371.12909000776222,372.99332178905809,377.39785339115275,382.1500320620915,390.08198744443655,385.51072771864972,390.00056425516556,395.90258485216862,398.9498394289559],"type":"scatter","mode":"markers","marker":{"color":"rgba(31,119,180,1)","line":{"color":"rgba(31,119,180,1)"}},"error_y":{"color":"rgba(31,119,180,1)"},"error_x":{"color":"rgba(31,119,180,1)"},"line":{"color":"rgba(31,119,180,1)"},"xaxis":"x","yaxis":"y","frame":null}],"highlight":{"on":"plotly_click","persistent":false,"dynamic":false,"selectize":false,"opacityDim":0.20000000000000001,"selected":{"opacity":1},"debounce":0},"shinyEvents":["plotly_hover","plotly_click","plotly_selected","plotly_relayout","plotly_brushed","plotly_brushing","plotly_clickannotation","plotly_doubleclick","plotly_deselect","plotly_afterplot","plotly_sunburstclick"],"base_url":"https://plot.ly"},"evals":[],"jsHooks":[]}</script>
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
##   0.005   0.000   0.004
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
<div class="profvis html-widget html-fill-item" id="htmlwidget-432c6416ba99029146af" style="width:100%;height:600px;"></div>
<script type="application/json" data-for="htmlwidget-432c6416ba99029146af">{"x":{"message":{"prof":{"time":[1,2,3,4,5,6,7,8,9,9,9,10,10,11,11,12,12,13,13,14,14,15,15,16,16,17,17,18,18,19,19,20,20,21,21,22,22,23,24,24,25,25,26,26,27,27,28,28,28,29,30,30,31,31,31,32,32,33,33,33,34,35,35,36,36,37,38,38,39,40,41,41,42,43,44,44,45,45,46,47,48,49,49,50,51,52,53,54,54,55,56,56,57,57,58,58,59,59,59,60,60,61,61,62,63,64,65,65,66,66,66,67,68,68,69,69,70,71,71,72,72,73,73,74,74,75,75,76,76,76,77,78,78,79,79,80,80,81,81,82,82,83,84,85,85,86,86,87,87,88,88,89,89,90,91,91,92,92,92,93,94,95,95,96,96,97,97,98,98,99,99,100,101,101,102,103,104,104,104,105,105,106,106,107,107,108,108,109,110,110,111,112,113,113,114,114,115,115,116,116,117,117,118,118,118,119,120,121,122,122,122,123,124,125,125,125,126,126,127,127,127,128,129,130,130,130,131,131,132,132,133,134,134,134,135,135,135,136,136,137,137,138,138,139,139,140,140,141,141,142,142,143,143,144,144,145,145,146,147,147,148,149,149,150,150,151,152,153,153,154,154,155,155,155,155,156,157,157,158,158,159,160,160,161,161,162,163,163,163,164,164,165,166,166,167,167,168,168,169,169,170,170,171,171,172,172,172,173,174,174,175,175,176,176,177,177,178,179,180,180,181,182,182,183,183,184,184,185,185,185,186,186,187,187,188,188,189,189,190,190,191,192,192,193,193,194,195,196,196,197,198,198,199,199,200,201,201,202,203,203,204,204,205,205,205,206,207,207,207,208,208,209,210,211,211,211,212,212,213,214,214,215,215,216,216,216,217,217,217,218,218,218,219,219,219,220,220,220,221,221,221,222,222,222,223,223,223,224,224,225,225,226,226,227,228,229,229,230,230,231,231,232,232,233,233,234,234,235,235,235,236,236,237,238,238,239,239,240,240,241,242,242,243,244,245,245,246,247,247,247,248,248,249,250,251,251,252,252,253,253,254,254,255,255,256,256,257,257,258,258,259,260,260,261,262,263,263,263,264,265,265,266,266,267,267,268,269,269,270,270,271,271,272,273,273,274,275,275,276,276,277,277,277,278,278,279,279,280,281,282,282,283,283,284,285,285,285,286,286,287,287,288,288,289,289,290,291,291,292,292,293,293,294,295,295,296,296,297,297,298,299,299,299,299,300,300,301,301,302,302,303,303,304,305,306,306,306,307,308,308,309,309,310,311,311,312,312,313,313,314,315,316,316,317,317,318,318,319,319,319,320,320,320,321,321,322,323,323,324,325,325,326,327,327,328,329,329,330,330,330,331,331,331,332,333,333,334,334,335,335,335,336,336,337,337,338,338,339,339,340,340,340,341,341,342,342,343,343,343,344,344,345,346,346,347,347,348,348,349,349,350,350,351,351,352,352,353,353,353,354,354,355,355,356,357,358,359,359,359,360,360,360,361,361,362,362,363,363,364,365,365,366,366,366,367,367,368,368,368,369,370,370,371,371,372,372,373,373,374,374,375,375,376,376,377,377,378,378,379,379,380,380,381,381,382,382,383,383,384,384,385,385,386,386,387,387,388,388,389,389,390,390,391,391,392,392,393,393,394,394,395,395,396,396,397,397,398,399,399,400,400,401,402,402,403,404,404,405,406,407,407,408,409,409,410,410,411,411,411,412,412,413,413,414,415,415,416,416,417,417,418,418,419,419,420,421,421,422,423,423,424,424,425,425,426,426,426,427,427,427,428,429,429,430,430,431,432,433,433,434,434,435,436,437,437,438,439,440,440,441,441,442,442,443,443,444,444,445,445,446,446,447,448,448,449,449,450,451,451,452,452,453,453,454,454,455,456,456,457,458,459,459,460,460,461,462,463,463,464,464,465,465,466,467,467,467,468,468,468,469,469,470,470,470,471,471,471,472,472,473,474,474,475,475,476,477,477,478,479,479,480,480,481,482,482,483,483,484,484,484,485,486,487,487,488,489,489,490,491,491,492,492,493,494,495,495,496,497,497,498,498,498,499,499,499,500,500,501,501,502,502,503,504,505,505,505,506,507,507,507,508,508,508,509,509,510,511,511,512,512,513,514,514,514,515,516,516,517,517,518,519,519,520,520,521,521,521,522,523,523,523,524,524,525,525,526,526,526,527,527,528,529,529,530,531,532,533,534,534,535,535,536,536,537,537,537,538,539,539,540,540,541,541,542,543,543,544,545,545,546,546,547,547,547,548,548,549,550,550,550,551,551,552,553,553,553,554,554,554,555,555,556,556,557,558,558,559,559,559,560,561,561,562,562,562,563,563,564,565,566,567,568,568,568,569,569,570,571,571,572,572,573,573,574,574,575,576,576,577,577,577,578,578,579,579,580,581,581,581,582,582,582,583,583,584,585,585,585,586,587,588,589,589,590,591,591,592,592,593,593,594,594,595,596,597,597,598,599,599,600,600,601,601,602,602,603,603,604,605,605,606,607,607,607,608,608,609,610,610,611,611,612,613,613,614,615,615,616,617,618,619,619,620,620,621,621,622,623,624,625,625,625,626,626,627,627,628,628,629,630,630,630,631,632,632,633,633,633,634,634,635,635,636,636,637,637,638,639,639,640,641,642,643,643,644,645,645,645,646,646,646,647,647,648,648,649,649,650,651,651,652,652,653,654,655,655,655,656,656,656,657,657,658,658,658,659,659,659,660,660,661,661,661,662,662,663,664,664,664,665,665,666,666,667,668,668,669,670,670,671,671,671,672,672,673,673,674,674,675,676,676,676,677,677,678,679,679,680,680,681,681,682,683,683,683,684,684,684,685,685,685,686,686,686,687,687,687,688,688,688,689,689,689,690,690,690,691,691,691,692,692,692,693,693,693,694,694,694,695,696,697,697,698,698,699,699,700,700,701,702,702,703,703,703,704,705,705,706,707,707,708,708,709,709,710,711,711,712,712,713,713,714,714,715,716,717,717,718,718,719,719,719,720,721,722,722,723,723,724,724,725,726,726,727,727,728,728,729,729,730,730,731,731,731,732,733,733,733,734,734,735,735,736,737,737,738,739,739,740,740,741,741,742,742,743,743,744,744,744,745,746,746,747,748,748,749,749,749,750,750,751,751,751,752,753,754,754,754,755,755,755,756,756,757,758,759,760,760,761,761,761,762,763,764,764,765,765,765,766,766,766,767,767,768,768,769,769,770,771,771,771,772,772,773,774,775,776,776,777,777,777,778,778,779,779,780,780,781,782,782,783,783,784,785,785,786,787,788,788,788,789,789,789,790,790,791,791,792,792,793,793,793,794,794,795,795,796,796,797,797,797,798,798,798,799,799,800,800,801,801,802,802,803,804,804,805,805,806,806,807,807,808,809,809,810,810,811,811,812,812,813,813,814,815,816,816,817,817,818,818,819,819,819,820,820,821,822,822,822,823,823,824,825,826,826,827,828,829,829,830,830,830,831,832,832,832,833,833,833,834,834,835,835,836,836,837,837,838,838,839,839,840,840,841,842,842,842,843,843,843,844,844,844,845,845,846,846,847,848,849,849,850,850,851,852,852,853,854,854,854,855,855,855,856,857,857,858,859,859,860,860,861,861,862,862,863,864,864,864,865,865,865,866,866,867,867,868,868,869,870,870,871,871,872,873,873,874,874,875,875,875,876,877,877,878,879,880,880,881,882,882,883,883,884,884,885,885,886,886,886,887,887,888,888,889,889,890,890,891,891,892,892,893,893,894,895,895,896,896,897,898,899,899,900,901,902,903,904,904,905,905,905,906,906,906,907,907,908,908,909,909,910,911,912,912,913,913,914,914,915,915,915,916,916,916,917,918,919,919,920,921,921,922,923,924,924,924,925,925,925,926,926,926,927,927,927,928,928,928,929,929,929,930,930,930,931,931,931,932,932,932,933,933,933,934,934,934,935,935,935,936,936,937,937,938,938,938,939,940,940,941,941,942,942,943,944,944,945,945,945,946,946,946,947,947,948,948,949,949,950,950,951,951,952,953,953,954,955,955,955,956,956,956,957,957,958,959,959,960,960,961,961,962,962,962,963,963,964,964,965,965,966,966,967,967,968,968,969,969,970,971,971,972,972,973,973,974,974,975,975,976,977,977,978,978,979,979,980,980,981,981,982,982,983,983,984,984,985,985,986,986,987,987,988,988,989,989,990,990,991,991,991,992,992,993,993,993,994,994,994,995,995,996,996,997,997,998,999,1000,1001,1001,1002,1002,1002,1003,1003,1003,1004,1004,1005,1005,1006,1006,1007,1008,1009,1010,1010,1011,1011,1011,1012,1012,1012,1013,1013,1014,1014,1015,1015,1016,1016,1017,1018,1018,1018,1019,1020,1020,1020,1021,1021,1021,1022,1022,1022,1023,1023,1024,1024,1025,1025,1026,1027,1027,1028,1028,1029,1029,1030,1030,1031,1032,1032,1033,1034,1034,1034,1035,1035,1036,1037,1037,1038,1038,1038,1039,1040,1040,1041,1041,1042,1042,1043,1044,1045,1045,1045,1046,1046,1046,1047,1047,1047,1048,1048,1049,1049,1050,1050,1051,1051,1051,1052,1053,1053,1054,1054,1055,1055,1055,1056,1056,1056,1057,1058,1059,1060,1060,1061,1062,1062,1063,1063,1064,1064,1065,1066,1066,1067,1067,1068,1068,1069,1070,1070,1071,1071,1072,1072,1073,1073,1074,1074,1075,1075,1076,1076,1077,1077,1078,1079,1080,1080,1081,1081,1081,1082,1082,1083,1083,1084,1085,1085,1085,1086,1086,1086,1087,1087,1087,1088,1088,1088,1089,1089,1089,1090,1090,1090,1091,1091,1091,1092,1092,1092,1093,1093,1093,1094,1094,1094,1095,1095,1095,1096,1096,1096,1097,1097,1097,1098,1098,1098,1099,1099,1099,1100,1100,1100,1101,1101,1101,1102,1102,1102,1103,1103,1103,1104,1104,1104,1105,1105,1105,1106,1106,1106,1107,1107,1107,1108,1108,1108,1109,1109,1109,1110,1110,1110,1111,1111,1111,1112,1112,1112,1113,1113,1113,1114,1114,1114,1115,1115,1115,1116,1116,1116,1117,1117,1117,1118,1118,1118,1119,1119,1119,1120,1120,1120,1121,1121,1121,1122,1122,1122,1123,1123,1123,1124,1124,1124,1125,1125,1125,1126,1126,1126,1127,1127,1127,1128,1128,1128,1129,1129,1129,1130,1130,1130,1131,1131,1131,1132,1132,1132,1133,1133,1133,1134,1134,1134,1135,1135,1135,1136,1136,1137,1137,1138,1138,1139,1139,1140,1141,1141,1142,1142,1143,1144,1145,1146,1147,1147,1148,1148,1149,1149,1150,1150,1150,1151,1152,1152,1152,1153,1154,1154,1155,1155,1156,1156,1157,1157,1158,1159,1159,1159,1160,1160,1160,1161,1162,1162,1163,1163,1164,1164,1165,1165,1165,1166,1166,1167,1168,1168,1169,1169,1170,1170,1171,1171,1172,1172,1173,1174,1174,1175,1175,1176,1176,1177,1177,1178,1179,1179,1179,1180,1180,1181,1182,1182,1182,1183,1183,1183,1184,1184,1184,1185,1186,1187,1187,1188,1188,1189,1190,1190,1191,1191,1192,1192,1193,1194,1194,1195,1195,1196,1196,1197,1198,1199,1199,1200,1201,1201,1202,1202,1203,1203,1204,1204,1205,1205,1205,1206,1206,1206,1207,1208,1208,1209,1209,1210,1210,1210,1211,1212,1213,1213,1214,1214,1214,1215,1215,1216,1216,1217,1217,1218,1219,1219,1220,1221,1221,1222,1222,1223,1223,1224,1225,1226,1226,1227,1227,1227,1228,1228,1228,1229,1229,1230,1230,1231,1231,1232,1232,1233,1233,1234,1235,1236,1236,1237,1238,1238,1239,1239,1240,1240,1241,1242,1242,1242,1243,1244,1244,1245,1245,1246,1246,1247,1247,1248,1248,1249,1249,1250,1250,1250,1251,1251,1251,1252,1252,1252,1253,1253,1254,1254,1255,1255,1256,1256,1257,1257,1258,1258,1259,1260,1261,1262,1262,1263,1263,1264,1265,1265,1266,1266,1267,1267,1268,1268,1269,1270,1270,1271,1272,1272,1272,1273,1273,1273,1274,1275,1276,1276,1277,1277,1278,1279,1280,1280,1281,1281,1282,1282,1283,1283,1284,1284,1285,1286,1286,1286,1287,1287,1287,1288,1288,1289,1289,1289,1290,1291,1291,1292,1292,1293,1293,1294,1294,1295,1295,1296,1296,1297,1297,1298,1298,1299,1299,1300,1300,1301,1301,1302,1302,1302,1303,1304,1305,1306,1306,1307,1307,1308,1308,1309,1309,1310,1311,1311,1312,1313,1314,1314,1315,1316,1316,1317,1318,1318,1319,1320,1320,1321,1321,1322,1322,1322,1323,1323,1323,1324,1324,1324,1325,1325,1326,1326,1327,1327,1328,1328,1328,1329,1329,1330,1330,1331,1331,1332,1332,1333,1333,1334,1334,1335,1335,1336,1337,1338,1338,1339,1339,1340,1340,1341,1342,1342,1342,1343,1344,1344,1344,1345,1345,1345,1346,1347,1347,1348,1348,1349,1350,1350,1351,1351,1352,1352,1353,1353,1354,1354,1355,1356,1356,1357,1358,1359,1359,1359,1360,1360,1361,1361,1362,1362,1363,1364,1365,1366,1366,1366,1367,1367,1367,1368,1369,1370,1370,1371,1372,1373,1374,1374,1375,1375,1376,1377,1377,1378,1379,1379,1380,1380,1381,1381,1382,1382,1383,1383,1384,1384,1385,1385,1386,1386,1387,1387,1388,1388,1389,1390,1390,1391,1391,1392,1392,1393,1393,1394,1394,1395,1395,1396,1396,1397,1397,1398,1398,1399,1399,1400,1400,1401,1401,1402,1402,1403,1403,1404,1404,1405,1405,1406,1406,1407,1407,1408,1408,1409,1409,1409,1409,1409,1409,1409,1409,1410,1410,1410,1410,1410,1410,1410,1410,1411,1411,1411,1411,1411,1411,1411,1411,1412,1412,1412,1412,1412,1412,1412,1412,1413,1413,1413,1413,1413,1413,1413,1413,1414,1414,1414,1414,1414,1414,1414,1414,1415,1415,1415,1415,1415,1415,1415,1415,1416,1416,1416,1416,1416,1416,1416,1416,1417,1417,1417,1417,1417,1417,1417,1417,1418,1418,1418,1418,1418,1418,1418,1418,1419,1419,1419,1419,1419,1419,1419,1419,1420,1420,1420,1420,1420,1420,1420,1420,1421,1421,1421,1421,1421,1421,1421,1421,1422,1422,1422,1422,1422,1422,1422,1422,1423,1423,1423,1423,1423,1423,1423,1423,1424,1424,1424,1424,1424,1424,1424,1424,1425,1425,1425,1425,1425,1425,1425,1425,1426,1426,1426,1426,1426,1426,1426,1426,1427,1427,1427,1427,1427,1427,1427,1427],"depth":[1,1,1,1,1,1,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,3,2,1,2,1,3,2,1,1,2,1,2,1,1,2,1,1,1,2,1,1,1,2,1,2,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,1,1,2,1,3,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,1,1,3,2,1,1,1,3,2,1,2,1,3,2,1,1,1,3,2,1,2,1,2,1,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,1,1,2,1,2,1,4,3,2,1,1,2,1,2,1,1,2,1,2,1,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,2,1,1,1,2,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,1,2,1,1,2,1,2,1,1,2,1,1,2,1,2,1,3,2,1,1,3,2,1,2,1,1,1,3,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,2,1,1,2,1,1,1,2,1,1,3,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,1,3,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,3,2,1,2,1,2,1,1,1,2,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,4,3,2,1,2,1,2,1,2,1,2,1,1,1,3,2,1,1,2,1,2,1,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,1,2,1,1,2,1,1,2,1,1,2,1,3,2,1,3,2,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,1,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,3,2,1,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,1,2,1,1,1,2,1,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,1,2,1,2,1,1,1,2,1,2,1,1,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,1,1,2,1,2,1,1,1,2,1,2,1,2,1,1,3,2,1,3,2,1,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,1,2,1,1,2,1,2,1,1,2,1,2,1,3,2,1,1,1,2,1,1,2,1,1,2,1,2,1,1,1,2,1,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,1,3,2,1,1,3,2,1,3,2,1,2,1,1,2,1,2,1,1,3,2,1,1,2,1,2,1,1,2,1,2,1,3,2,1,1,3,2,1,2,1,2,1,3,2,1,2,1,1,2,1,1,1,1,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,3,2,1,2,1,1,3,2,1,2,1,1,3,2,1,3,2,1,2,1,2,1,1,2,1,3,2,1,1,2,1,3,2,1,2,1,1,1,1,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,2,1,2,1,1,3,2,1,3,2,1,2,1,1,3,2,1,1,1,1,2,1,1,2,1,2,1,2,1,2,1,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,3,2,1,2,1,1,2,1,2,1,1,2,1,1,2,1,1,1,1,2,1,2,1,2,1,1,1,1,3,2,1,2,1,2,1,2,1,1,3,2,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,1,1,1,2,1,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,1,1,3,2,1,3,2,1,2,1,3,2,1,3,2,1,2,1,3,2,1,2,1,1,3,2,1,2,1,2,1,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,1,3,2,1,2,1,1,2,1,2,1,2,1,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,1,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,3,2,1,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,3,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,1,2,1,3,2,1,2,1,3,2,1,1,1,3,2,1,3,2,1,2,1,1,1,1,2,1,3,2,1,1,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,3,2,1,2,1,1,1,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,1,1,3,2,1,3,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,3,2,1,2,1,1,3,2,1,2,1,1,1,2,1,1,1,2,1,3,2,1,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,3,2,1,2,1,2,1,1,1,2,1,2,1,1,2,1,1,3,2,1,3,2,1,1,2,1,1,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,3,2,1,1,2,1,1,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,1,2,1,1,1,1,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,3,2,1,3,2,1,1,1,2,1,1,2,1,1,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,3,2,1,3,2,1,2,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,1,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,1,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,1,3,2,1,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,1,3,2,1,2,1,1,2,1,3,2,1,1,2,1,2,1,2,1,1,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,3,2,1,3,2,1,1,1,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,3,2,1,2,1,2,1,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,1,1,1,2,1,2,1,2,1,3,2,1,1,3,2,1,1,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,1,3,2,1,3,2,1,3,2,1,1,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,1,2,1,2,1,3,2,1,1,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,1,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,1,2,1,2,1,2,1,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,1,3,2,1,3,2,1,1,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,1,1,2,1,2,1,2,1,2,1,1,2,1,1,1,2,1,1,2,1,1,2,1,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,1,3,2,1,1,3,2,1,3,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,1,3,2,1,2,1,2,1,2,1,1,1,1,3,2,1,3,2,1,1,1,2,1,1,1,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1],"label":["rowSums","rowSums","rowSums","rowSums","rowMeans","rowMeans","rowMeans","rowMeans","<GC>","aperm.default","apply","aperm.default","apply","aperm.default","apply","aperm.default","apply","aperm.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","mean.default","apply","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","length","local","isTRUE","mean.default","apply","<GC>","apply","isTRUE","mean.default","apply","apply","mean.default","apply","FUN","apply","apply","FUN","apply","apply","apply","<GC>","apply","apply","apply","mean.default","apply","mean.default","apply","apply","apply","apply","FUN","apply","apply","apply","apply","apply","<GC>","apply","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","apply","apply","apply","mean.default","apply","<GC>","FUN","apply","apply","FUN","apply","mean.default","apply","apply","FUN","apply","FUN","apply","length","local","FUN","apply","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","length","local","length","local","apply","apply","<GC>","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","<GC>","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","apply","FUN","apply","apply","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","is.na","local","FUN","apply","apply","FUN","apply","apply","apply","FUN","apply","<GC>","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","apply","<GC>","FUN","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","<GC>","mean.default","apply","mean.default","apply","is.na","local","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","apply","<GC>","apply","apply","length","local","FUN","apply","apply","apply","mean.default","apply","FUN","apply","<GC>","isTRUE","mean.default","apply","apply","length","local","FUN","apply","apply","FUN","apply","length","local","apply","<GC>","FUN","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","<GC>","FUN","apply","apply","FUN","apply","length","local","mean.default","apply","FUN","apply","apply","apply","<GC>","apply","apply","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","length","local","<GC>","apply","<GC>","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","apply","apply","mean.default","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","apply","<GC>","is.na","local","is.na","local","apply","apply","isTRUE","mean.default","apply","mean.default","apply","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","apply","apply","FUN","apply","FUN","apply","mean.default","apply","<GC>","apply","length","local","is.numeric","local","isTRUE","mean.default","apply","is.na","local","apply","FUN","apply","<GC>","apply","FUN","apply","apply","mean.default","apply","apply","apply","FUN","apply","apply","<GC>","FUN","apply","length","local","apply","apply","is.numeric","local","FUN","apply","FUN","apply","<GC>","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","apply","<GC>","mean.default","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","<GC>","apply","FUN","apply","apply","is.numeric","local","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","apply","is.na","local","apply","apply","FUN","apply","FUN","apply","apply","<GC>","is.numeric","local","length","local","FUN","apply","FUN","apply","mean.default","apply","apply","FUN","apply","<GC>","apply","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","apply","<GC>","isTRUE","mean.default","apply","length","local","is.na","local","mean.default","apply","mean.default","apply","apply","apply","<GC>","FUN","apply","apply","mean.default","apply","FUN","apply","apply","FUN","apply","mean.default","apply","<GC>","apply","apply","apply","mean.default","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","length","local","apply","is.na","local","apply","is.numeric","local","apply","<GC>","apply","apply","mean.default","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","<GC>","apply","isTRUE","mean.default","apply","length","local","mean.default","apply","FUN","apply","FUN","apply","<GC>","length","local","is.na","local","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","apply","mean.default","apply","<GC>","apply","FUN","apply","FUN","apply","is.numeric","local","is.numeric","local","mean.default","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","apply","apply","apply","isTRUE","mean.default","apply","<GC>","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","apply","FUN","apply","<GC>","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","apply","mean.default","apply","FUN","apply","apply","FUN","apply","apply","mean.default","apply","apply","apply","FUN","apply","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","apply","mean.default","apply","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","FUN","apply","FUN","apply","apply","apply","is.numeric","local","FUN","apply","apply","apply","length","local","apply","apply","length","local","<GC>","apply","mean.default","apply","FUN","apply","is.numeric","local","mean.default","apply","mean.default","apply","apply","is.numeric","local","FUN","apply","apply","mean.default","apply","mean.default","apply","length","local","FUN","apply","apply","<GC>","apply","apply","apply","mean.default","apply","FUN","apply","apply","apply","FUN","apply","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","is.na","local","apply","FUN","apply","length","local","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","mean.default","apply","FUN","apply","<GC>","mean.default","apply","apply","apply","FUN","apply","apply","FUN","apply","apply","mean.default","apply","FUN","apply","apply","apply","FUN","apply","apply","length","local","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","length","local","FUN","apply","apply","apply","isTRUE","mean.default","apply","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","mean.default","apply","<GC>","apply","apply","isTRUE","mean.default","apply","apply","FUN","apply","mean.default","apply","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","<GC>","FUN","apply","FUN","apply","apply","FUN","apply","apply","apply","apply","apply","FUN","apply","length","local","mean.default","apply","isTRUE","mean.default","apply","apply","<GC>","apply","<GC>","apply","mean.default","apply","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","apply","isTRUE","mean.default","apply","length","local","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","mean.default","apply","apply","length","local","isTRUE","mean.default","apply","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","apply","apply","<GC>","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","is.numeric","local","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","apply","apply","mean.default","apply","apply","FUN","apply","FUN","apply","mean.default","apply","<GC>","apply","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","<GC>","mean.default","apply","is.numeric","local","apply","FUN","apply","FUN","apply","apply","mean.default","apply","apply","mean.default","apply","apply","apply","apply","<GC>","apply","<GC>","apply","FUN","apply","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","isTRUE","mean.default","apply","apply","length","local","<GC>","mean.default","apply","is.na","local","mean.default","apply","FUN","apply","FUN","apply","apply","mean.default","apply","apply","apply","apply","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","length","local","FUN","apply","is.na","local","apply","FUN","apply","mean.default","apply","apply","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","length","local","isTRUE","mean.default","apply","mean.default","apply","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","apply","length","local","apply","FUN","apply","<GC>","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","apply","mean.default","apply","FUN","apply","FUN","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","apply","FUN","apply","isTRUE","mean.default","apply","apply","mean.default","apply","apply","<GC>","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","apply","apply","mean.default","apply","FUN","apply","<GC>","FUN","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","is.numeric","local","FUN","apply","<GC>","FUN","apply","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","apply","<GC>","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","is.numeric","local","isTRUE","mean.default","apply","is.numeric","local","isTRUE","mean.default","apply","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","isTRUE","mean.default","apply","mean.default","apply","apply","apply","apply","mean.default","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","length","local","apply","mean.default","apply","FUN","apply","apply","is.numeric","local","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","is.numeric","local","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","length","local","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","apply","FUN","apply","mean.default","apply","apply","FUN","apply","length","local","FUN","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","<GC>","apply","FUN","apply","is.numeric","local","apply","apply","FUN","apply","FUN","apply","length","local","isTRUE","mean.default","apply","is.numeric","local","apply","<GC>","length","local","FUN","apply","apply","apply","mean.default","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","is.numeric","local","FUN","apply","is.na","local","FUN","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","<GC>","length","local","<GC>","length","local","FUN","apply","FUN","apply","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","apply","length","local","mean.default","apply","apply","mean.default","apply","length","local","<GC>","FUN","apply","apply","length","local","apply","apply","mean.default","apply","apply","FUN","apply","is.na","local","mean.default","apply","<GC>","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","apply","<GC>","apply","<GC>","apply","apply","apply","mean.default","apply","apply","apply","apply","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","apply","mean.default","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","isTRUE","mean.default","apply","apply","apply","mean.default","apply","apply","FUN","apply","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","mean.default","apply","FUN","apply","FUN","apply","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","mean.default","apply","length","local","FUN","apply","FUN","apply","apply","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","FUN","apply","apply","is.numeric","local","mean.default","apply","FUN","apply","FUN","apply","<GC>","apply","apply","mean.default","apply","mean.default","apply","mean.default","apply","is.na","local","mean.default","apply","length","local","FUN","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","length","local","FUN","apply","FUN","apply","apply","apply","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","apply","apply","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","length","local","FUN","apply","mean.default","apply","apply","isTRUE","mean.default","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","is.na","local","FUN","apply","<GC>","apply","<GC>","apply","apply","FUN","apply","apply","isTRUE","mean.default","apply","mean.default","apply","apply","length","local","<GC>","FUN","apply","apply","is.na","local","mean.default","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","mean.default","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","apply","apply","FUN","apply","apply","length","local","<GC>","apply","<GC>","apply","apply","is.numeric","local","mean.default","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","FUN","apply","FUN","apply","apply","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","isTRUE","mean.default","apply","apply","FUN","apply","is.numeric","local","mean.default","apply","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","mean.default","apply","FUN","apply","is.na","local","FUN","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","is.numeric","local","mean.default","apply","FUN","apply","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","is.na","local","apply","FUN","apply","apply","FUN","apply","FUN","apply","mean.default","apply","apply","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","mean.default","apply","apply","FUN","apply","length","local","is.numeric","local","apply","isTRUE","mean.default","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","length","local","<GC>","is.numeric","local","<GC>","is.numeric","local","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","apply","apply","mean.default","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","apply","FUN","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","apply","FUN","apply","mean.default","apply","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","isTRUE","mean.default","apply","apply","apply","apply","is.na","local","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","apply","FUN","apply","apply","length","local","apply","FUN","apply","apply","mean.default","apply","FUN","apply","<GC>","length","local","<GC>","length","local","<GC>","length","local","mean.default","apply","length","local","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","is.numeric","local","mean.default","apply","mean.default","apply","apply","apply","FUN","apply","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","is.numeric","local","mean.default","apply","mean.default","apply","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","is.na","local","FUN","apply","FUN","apply","apply","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","apply","FUN","apply","apply","apply","apply","FUN","apply","mean.default","apply","apply","FUN","apply","apply","mean.default","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","findLocals1","FUN","lapply","findLocalsList1","findLocalsList","findLocals","compile","compiler:::tryCompile","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis"],"filenum":[1,1,1,1,1,1,1,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,null,1,1,null,null,null,null,1,null,1,null,null,1,1,null,1,null,1,1,null,1,1,1,null,1,1,1,null,1,null,1,1,1,1,null,1,1,1,1,1,null,1,1,null,1,null,1,null,1,null,null,1,null,1,null,1,1,1,1,null,1,null,null,1,1,null,1,null,1,1,null,1,null,1,null,null,null,1,null,1,null,null,1,1,null,1,null,1,null,1,null,null,null,null,1,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,null,1,1,1,null,1,null,1,null,1,null,1,null,1,1,null,1,1,1,null,null,1,null,1,null,1,null,null,null,1,1,null,1,1,1,null,1,null,1,null,1,null,1,null,1,null,null,1,1,1,1,null,null,1,1,1,null,null,1,null,1,null,null,1,1,1,null,null,1,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,1,null,null,null,1,1,1,null,1,null,1,null,null,null,1,1,null,null,null,1,1,null,1,null,null,1,null,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,1,null,1,null,null,null,1,null,1,1,1,null,1,1,null,1,null,1,null,1,null,null,1,null,1,null,null,null,1,null,1,null,1,1,null,1,null,1,1,1,null,1,1,null,1,null,1,1,null,1,1,null,1,null,1,null,null,1,1,null,null,null,null,null,1,1,null,null,1,null,1,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,1,1,1,null,1,null,1,null,1,null,1,null,null,null,null,null,null,1,null,null,1,null,1,null,1,null,1,1,null,1,1,1,null,1,1,null,null,1,null,null,1,1,null,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,1,1,null,null,1,1,null,1,null,1,null,1,1,null,1,null,1,null,1,1,null,null,1,null,1,null,1,null,null,1,null,1,null,null,1,1,null,1,null,1,1,null,null,null,null,null,null,1,null,1,null,1,1,null,1,null,1,null,1,1,null,1,null,1,null,1,1,null,null,null,1,null,null,null,null,null,1,null,1,1,1,null,null,1,1,null,1,null,1,1,null,1,null,1,null,1,1,1,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,1,null,1,null,null,1,null,null,1,1,null,1,null,1,null,null,1,null,null,null,1,null,1,null,1,null,null,null,null,null,null,1,null,null,1,null,1,1,null,1,null,1,null,1,null,1,null,null,null,null,null,1,null,null,1,null,1,null,1,1,1,1,null,null,1,null,null,1,null,1,null,1,null,1,1,null,1,null,null,1,null,1,null,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,1,null,1,1,null,1,1,1,null,1,1,null,1,null,1,null,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,1,null,1,1,null,1,null,1,null,1,null,null,1,null,null,1,1,null,1,null,1,1,1,null,null,null,1,1,1,null,null,1,1,null,null,null,1,null,1,null,1,null,null,null,1,null,1,1,null,null,null,1,1,null,1,null,1,null,null,null,1,1,null,1,1,1,null,1,null,1,1,1,null,1,null,1,null,1,1,null,null,1,null,null,1,null,1,null,null,1,null,null,1,null,null,1,null,1,null,null,1,null,1,1,null,1,null,1,1,null,1,null,1,null,null,1,1,1,null,1,1,null,1,1,null,1,null,1,1,1,null,1,1,null,null,null,null,1,null,null,1,null,1,null,null,null,1,1,1,null,null,1,1,null,null,1,null,null,1,null,1,1,null,1,null,1,1,null,null,1,1,null,1,null,1,1,null,1,null,1,null,null,1,1,null,null,1,null,1,null,1,null,null,1,null,1,1,null,1,1,1,1,1,null,1,null,null,null,1,null,null,1,1,null,1,null,1,null,1,1,null,1,1,null,1,null,1,null,null,1,null,1,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,1,null,null,null,null,1,1,null,1,null,null,1,null,1,1,1,1,1,null,null,1,null,1,1,null,1,null,1,null,1,null,null,1,null,1,null,null,1,null,1,null,1,1,null,null,1,null,null,1,null,1,1,null,null,1,1,1,1,null,1,1,null,1,null,1,null,1,null,1,1,1,null,1,1,null,1,null,1,null,1,null,1,null,1,1,null,1,1,null,null,1,null,null,1,null,1,null,1,1,null,1,1,null,1,1,1,1,null,1,null,1,null,1,1,1,1,null,null,1,null,1,null,1,null,1,1,null,null,1,1,null,null,null,null,1,null,null,null,1,null,1,null,1,1,null,1,1,1,1,null,1,1,null,null,1,null,null,1,null,null,null,1,null,null,1,null,1,null,1,1,1,null,null,1,null,null,1,null,1,null,null,1,null,null,1,null,null,null,null,1,null,1,1,null,null,1,null,1,null,1,1,null,null,1,null,1,null,null,1,null,1,null,1,null,1,1,null,null,1,null,1,1,null,1,null,1,null,1,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,1,1,null,1,null,1,null,1,null,1,1,null,1,null,null,1,1,null,1,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,1,1,null,1,null,1,null,null,1,1,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,null,null,1,null,null,1,1,null,null,1,null,1,null,1,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,null,1,1,null,1,1,null,null,null,null,1,null,null,null,null,1,1,1,null,null,1,null,null,1,null,1,1,1,1,null,1,null,null,1,1,1,null,1,null,null,1,null,null,1,null,1,null,1,null,1,1,null,null,1,null,1,1,1,1,null,1,null,null,1,null,1,null,1,null,null,1,null,1,null,1,1,null,null,1,1,null,null,1,null,null,1,null,null,null,1,null,1,null,null,1,null,1,null,null,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,1,null,1,null,null,null,1,null,1,1,null,1,null,1,null,1,null,1,null,null,1,1,null,1,null,1,null,null,null,null,1,null,null,1,null,null,null,null,1,1,1,null,1,1,1,null,1,null,null,1,1,null,null,1,null,null,1,null,1,null,null,null,1,null,null,null,1,null,1,null,1,1,null,null,1,null,null,null,null,null,null,null,1,null,1,1,1,null,1,null,1,1,null,1,1,null,null,1,null,null,1,1,null,1,1,null,1,null,1,null,1,null,1,1,null,null,1,null,null,1,null,1,null,1,null,1,1,null,null,null,1,1,null,1,null,null,null,null,1,1,null,null,1,1,null,1,1,null,1,null,null,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,1,1,null,1,1,1,1,1,null,1,null,null,1,null,null,1,null,1,null,1,null,1,1,1,null,1,null,1,null,1,null,null,1,null,null,1,1,1,null,1,1,null,1,1,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,null,1,1,null,1,null,1,null,1,1,null,1,null,null,1,null,null,1,null,1,null,1,null,null,null,1,null,1,1,null,1,1,null,null,1,null,null,1,null,1,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,null,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,null,null,1,null,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,null,1,null,null,1,null,null,null,1,null,1,1,1,1,null,1,null,null,1,null,null,1,null,1,null,1,null,1,1,1,1,null,1,null,null,1,null,null,1,null,1,null,null,null,1,null,1,1,null,null,1,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,1,1,null,null,null,1,null,1,null,1,1,null,1,1,null,null,1,null,1,1,null,null,null,null,1,1,null,null,null,1,null,1,1,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,null,1,1,null,1,null,1,null,null,1,null,null,1,1,1,1,null,1,1,null,null,null,1,null,1,1,null,null,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,1,null,1,null,null,1,null,1,null,1,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,1,1,1,1,null,1,null,1,null,1,null,null,1,1,null,null,1,1,null,1,null,null,null,1,null,1,1,null,null,1,null,null,1,1,null,1,null,1,null,1,null,null,1,null,1,1,null,1,null,1,null,1,null,null,null,1,1,null,1,null,1,null,1,null,1,1,null,null,1,null,1,1,null,null,1,null,null,1,null,null,1,1,1,null,1,null,1,1,null,1,null,1,null,1,1,null,null,null,1,null,1,1,1,null,1,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,1,null,1,null,1,null,null,1,1,1,null,1,null,null,1,null,1,null,1,null,null,1,null,1,1,null,1,null,1,null,1,1,1,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,1,1,null,1,1,null,1,null,null,null,null,1,null,null,1,1,null,1,null,1,null,1,null,1,null,1,null,null,null,null,null,null,null,null,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,1,1,null,1,null,1,1,null,1,null,1,null,1,null,1,1,null,1,1,null,null,1,null,null,1,1,1,null,1,null,1,1,1,null,1,null,1,null,1,null,1,null,1,1,null,null,1,null,null,1,null,1,null,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,1,1,1,null,null,null,1,null,1,null,1,1,null,1,1,1,null,1,1,null,null,1,null,1,1,null,1,null,1,null,null,null,null,null,null,null,null,null,null,1,null,null,null,1,null,null,1,null,1,null,1,null,1,null,1,null,null,null,1,null,1,1,1,null,1,null,1,null,1,1,null,null,1,1,null,null,1,null,null,1,1,null,1,null,1,1,null,1,null,1,null,null,null,1,null,1,1,null,1,1,1,null,null,1,null,null,null,1,null,1,1,1,1,null,null,1,null,null,1,1,1,null,1,1,1,1,null,1,null,1,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,null,null,null,null,null,1,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null],"linenum":[10,10,10,10,11,11,11,11,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,null,12,12,null,null,null,null,12,null,12,null,null,12,12,null,12,null,12,12,null,12,12,12,null,12,12,12,null,12,null,12,12,12,12,null,12,12,12,12,12,null,12,12,null,12,null,12,null,12,null,null,12,null,12,null,12,12,12,12,null,12,null,null,12,12,null,12,null,12,12,null,12,null,12,null,null,null,12,null,12,null,null,12,12,null,12,null,12,null,12,null,null,null,null,12,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,null,12,12,12,null,12,null,12,null,12,null,12,null,12,12,null,12,12,12,null,null,12,null,12,null,12,null,null,null,12,12,null,12,12,12,null,12,null,12,null,12,null,12,null,12,null,null,12,12,12,12,null,null,12,12,12,null,null,12,null,12,null,null,12,12,12,null,null,12,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,12,null,null,null,12,12,12,null,12,null,12,null,null,null,12,12,null,null,null,12,12,null,12,null,null,12,null,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,12,null,12,null,null,null,12,null,12,12,12,null,12,12,null,12,null,12,null,12,null,null,12,null,12,null,null,null,12,null,12,null,12,12,null,12,null,12,12,12,null,12,12,null,12,null,12,12,null,12,12,null,12,null,12,null,null,12,12,null,null,null,null,null,12,12,null,null,12,null,12,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,12,12,12,null,12,null,12,null,12,null,12,null,null,null,null,null,null,12,null,null,12,null,12,null,12,null,12,12,null,12,12,12,null,12,12,null,null,12,null,null,12,12,null,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,12,12,null,null,12,12,null,12,null,12,null,12,12,null,12,null,12,null,12,12,null,null,12,null,12,null,12,null,null,12,null,12,null,null,12,12,null,12,null,12,12,null,null,null,null,null,null,12,null,12,null,12,12,null,12,null,12,null,12,12,null,12,null,12,null,12,12,null,null,null,12,null,null,null,null,null,12,null,12,12,12,null,null,12,12,null,12,null,12,12,null,12,null,12,null,12,12,12,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,12,null,12,null,null,12,null,null,12,12,null,12,null,12,null,null,12,null,null,null,12,null,12,null,12,null,null,null,null,null,null,12,null,null,12,null,12,12,null,12,null,12,null,12,null,12,null,null,null,null,null,12,null,null,12,null,12,null,12,12,12,12,null,null,12,null,null,12,null,12,null,12,null,12,12,null,12,null,null,12,null,12,null,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,12,null,12,12,null,12,12,12,null,12,12,null,12,null,12,null,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,12,null,12,12,null,12,null,12,null,12,null,null,12,null,null,12,12,null,12,null,12,12,12,null,null,null,12,12,12,null,null,12,12,null,null,null,12,null,12,null,12,null,null,null,12,null,12,12,null,null,null,12,12,null,12,null,12,null,null,null,12,12,null,12,12,12,null,12,null,12,12,12,null,12,null,12,null,12,12,null,null,12,null,null,12,null,12,null,null,12,null,null,12,null,null,12,null,12,null,null,12,null,12,12,null,12,null,12,12,null,12,null,12,null,null,12,12,12,null,12,12,null,12,12,null,12,null,12,12,12,null,12,12,null,null,null,null,12,null,null,12,null,12,null,null,null,12,12,12,null,null,12,12,null,null,12,null,null,12,null,12,12,null,12,null,12,12,null,null,12,12,null,12,null,12,12,null,12,null,12,null,null,12,12,null,null,12,null,12,null,12,null,null,12,null,12,12,null,12,12,12,12,12,null,12,null,null,null,12,null,null,12,12,null,12,null,12,null,12,12,null,12,12,null,12,null,12,null,null,12,null,12,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,12,null,null,null,null,12,12,null,12,null,null,12,null,12,12,12,12,12,null,null,12,null,12,12,null,12,null,12,null,12,null,null,12,null,12,null,null,12,null,12,null,12,12,null,null,12,null,null,12,null,12,12,null,null,12,12,12,12,null,12,12,null,12,null,12,null,12,null,12,12,12,null,12,12,null,12,null,12,null,12,null,12,null,12,12,null,12,12,null,null,12,null,null,12,null,12,null,12,12,null,12,12,null,12,12,12,12,null,12,null,12,null,12,12,12,12,null,null,12,null,12,null,12,null,12,12,null,null,12,12,null,null,null,null,12,null,null,null,12,null,12,null,12,12,null,12,12,12,12,null,12,12,null,null,12,null,null,12,null,null,null,12,null,null,12,null,12,null,12,12,12,null,null,12,null,null,12,null,12,null,null,12,null,null,12,null,null,null,null,12,null,12,12,null,null,12,null,12,null,12,12,null,null,12,null,12,null,null,12,null,12,null,12,null,12,12,null,null,12,null,12,12,null,12,null,12,null,12,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,12,12,null,12,null,12,null,12,null,12,12,null,12,null,null,12,12,null,12,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,12,12,null,12,null,12,null,null,12,12,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,null,null,12,null,null,12,12,null,null,12,null,12,null,12,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,null,12,12,null,12,12,null,null,null,null,12,null,null,null,null,12,12,12,null,null,12,null,null,12,null,12,12,12,12,null,12,null,null,12,12,12,null,12,null,null,12,null,null,12,null,12,null,12,null,12,12,null,null,12,null,12,12,12,12,null,12,null,null,12,null,12,null,12,null,null,12,null,12,null,12,12,null,null,12,12,null,null,12,null,null,12,null,null,null,12,null,12,null,null,12,null,12,null,null,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,12,null,12,null,null,null,12,null,12,12,null,12,null,12,null,12,null,12,null,null,12,12,null,12,null,12,null,null,null,null,12,null,null,12,null,null,null,null,12,12,12,null,12,12,12,null,12,null,null,12,12,null,null,12,null,null,12,null,12,null,null,null,12,null,null,null,12,null,12,null,12,12,null,null,12,null,null,null,null,null,null,null,12,null,12,12,12,null,12,null,12,12,null,12,12,null,null,12,null,null,12,12,null,12,12,null,12,null,12,null,12,null,12,12,null,null,12,null,null,12,null,12,null,12,null,12,12,null,null,null,12,12,null,12,null,null,null,null,12,12,null,null,12,12,null,12,12,null,12,null,null,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,12,12,null,12,12,12,12,12,null,12,null,null,12,null,null,12,null,12,null,12,null,12,12,12,null,12,null,12,null,12,null,null,12,null,null,12,12,12,null,12,12,null,12,12,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,null,12,12,null,12,null,12,null,12,12,null,12,null,null,12,null,null,12,null,12,null,12,null,null,null,12,null,12,12,null,12,12,null,null,12,null,null,12,null,12,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,null,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,null,null,12,null,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,null,12,null,null,12,null,null,null,12,null,12,12,12,12,null,12,null,null,12,null,null,12,null,12,null,12,null,12,12,12,12,null,12,null,null,12,null,null,12,null,12,null,null,null,12,null,12,12,null,null,12,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,12,12,null,null,null,12,null,12,null,12,12,null,12,12,null,null,12,null,12,12,null,null,null,null,12,12,null,null,null,12,null,12,12,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,null,12,12,null,12,null,12,null,null,12,null,null,12,12,12,12,null,12,12,null,null,null,12,null,12,12,null,null,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,12,null,12,null,null,12,null,12,null,12,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,12,12,12,12,null,12,null,12,null,12,null,null,12,12,null,null,12,12,null,12,null,null,null,12,null,12,12,null,null,12,null,null,12,12,null,12,null,12,null,12,null,null,12,null,12,12,null,12,null,12,null,12,null,null,null,12,12,null,12,null,12,null,12,null,12,12,null,null,12,null,12,12,null,null,12,null,null,12,null,null,12,12,12,null,12,null,12,12,null,12,null,12,null,12,12,null,null,null,12,null,12,12,12,null,12,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,12,null,12,null,12,null,null,12,12,12,null,12,null,null,12,null,12,null,12,null,null,12,null,12,12,null,12,null,12,null,12,12,12,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,12,12,null,12,12,null,12,null,null,null,null,12,null,null,12,12,null,12,null,12,null,12,null,12,null,12,null,null,null,null,null,null,null,null,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,12,12,null,12,null,12,12,null,12,null,12,null,12,null,12,12,null,12,12,null,null,12,null,null,12,12,12,null,12,null,12,12,12,null,12,null,12,null,12,null,12,null,12,12,null,null,12,null,null,12,null,12,null,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,12,12,12,null,null,null,12,null,12,null,12,12,null,12,12,12,null,12,12,null,null,12,null,12,12,null,12,null,12,null,null,null,null,null,null,null,null,null,null,12,null,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,null,null,12,null,12,12,12,null,12,null,12,null,12,12,null,null,12,12,null,null,12,null,null,12,12,null,12,null,12,12,null,12,null,12,null,null,null,12,null,12,12,null,12,12,12,null,null,12,null,null,null,12,null,12,12,12,12,null,null,12,null,null,12,12,12,null,12,12,12,12,null,12,null,12,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,null,null,null,null,null,13,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null],"memalloc":[124.5359268188477,124.5359268188477,124.5359268188477,124.5359268188477,139.8181610107422,139.8181610107422,139.8181610107422,139.8181610107422,124.5295867919922,124.5295867919922,124.5295867919922,170.2839050292969,170.2839050292969,170.2839050292969,170.2839050292969,170.2839050292969,170.2839050292969,170.2839050292969,170.2839050292969,170.2839508056641,170.2839508056641,170.2839508056641,170.2839508056641,170.2839508056641,170.2839508056641,170.2839508056641,170.2839508056641,170.2839508056641,170.2839508056641,170.2839508056641,170.2839508056641,170.2839508056641,170.2839508056641,170.2836456298828,170.2836456298828,185.6562423706055,185.6562423706055,185.9052505493164,186.1787490844727,186.1787490844727,186.475830078125,186.475830078125,186.7658996582031,186.7658996582031,187.0463180541992,187.0463180541992,187.3728866577148,187.3728866577148,187.3728866577148,187.7332077026367,188.1088714599609,188.1088714599609,188.475227355957,188.475227355957,188.475227355957,188.605827331543,188.605827331543,185.9433059692383,185.9433059692383,185.9433059692383,186.30517578125,186.6694564819336,186.6694564819336,187.0754470825195,187.0754470825195,187.4354248046875,187.8173599243164,187.8173599243164,188.0544281005859,188.3893661499023,188.6702423095703,188.6702423095703,185.9557418823242,186.2109756469727,186.5478439331055,186.5478439331055,186.7912292480469,186.7912292480469,186.9941101074219,187.2257308959961,187.4747314453125,187.7822875976562,187.7822875976562,188.0031967163086,188.2635040283203,188.4705657958984,188.708854675293,188.7520294189453,188.7520294189453,186.0400543212891,186.2135314941406,186.2135314941406,186.4316482543945,186.4316482543945,186.6950531005859,186.6950531005859,186.888786315918,186.888786315918,186.888786315918,187.1327438354492,187.1327438354492,187.4915237426758,187.4915237426758,187.8119430541992,188.1118316650391,188.4463653564453,188.7569046020508,188.7569046020508,188.8325271606445,188.8325271606445,188.8325271606445,186.2738265991211,186.5528335571289,186.5528335571289,186.8661804199219,186.8661804199219,187.1657028198242,187.4892807006836,187.4892807006836,187.8146286010742,187.8146286010742,188.1352310180664,188.1352310180664,188.4705581665039,188.4705581665039,188.8072967529297,188.8072967529297,188.9117050170898,188.9117050170898,188.9117050170898,186.3802261352539,186.7137145996094,186.7137145996094,187.0378723144531,187.0378723144531,187.3791351318359,187.3791351318359,187.7204818725586,187.7204818725586,188.0654296875,188.0654296875,188.3992919921875,188.7393264770508,188.9896392822266,188.9896392822266,186.4033126831055,186.4033126831055,186.7188034057617,186.7188034057617,187.0483474731445,187.0483474731445,187.3945617675781,187.3945617675781,187.7320709228516,188.0636672973633,188.0636672973633,188.4092025756836,188.4092025756836,188.4092025756836,188.7350921630859,189.0601806640625,189.0662384033203,189.0662384033203,186.6508712768555,186.6508712768555,186.9568786621094,186.9568786621094,187.2420654296875,187.2420654296875,187.5650939941406,187.5650939941406,187.9033966064453,188.2532958984375,188.2532958984375,188.5953750610352,188.9122085571289,189.1417465209961,189.1417465209961,189.1417465209961,186.6384582519531,186.6384582519531,186.9402084350586,186.9402084350586,187.2692565917969,187.2692565917969,187.5673599243164,187.5673599243164,187.8884811401367,188.2248687744141,188.2248687744141,188.5450057983398,188.889289855957,189.2104110717773,189.2104110717773,189.2159042358398,189.2159042358398,186.9637145996094,186.9637145996094,187.2798156738281,187.2798156738281,187.624397277832,187.624397277832,187.9767608642578,187.9767608642578,187.9767608642578,188.3323822021484,188.6943283081055,189.0642318725586,189.288948059082,189.288948059082,189.288948059082,186.9056701660156,187.2287292480469,187.5673446655273,187.5673446655273,187.5673446655273,187.9202041625977,187.9202041625977,188.2822494506836,188.2822494506836,188.2822494506836,188.6890335083008,189.062873840332,189.3607482910156,189.3607482910156,189.3607482910156,186.9590454101562,186.9590454101562,187.2768020629883,187.2768020629883,187.6070175170898,187.9551849365234,187.9551849365234,187.9551849365234,188.310173034668,188.310173034668,188.310173034668,188.6760330200195,188.6760330200195,189.0391311645508,189.0391311645508,189.4172439575195,189.4172439575195,187.0019454956055,187.0019454956055,187.3051071166992,187.3051071166992,187.630485534668,187.630485534668,187.9743728637695,187.9743728637695,188.3265686035156,188.3265686035156,188.6891326904297,188.6891326904297,189.0539169311523,189.0539169311523,189.4235305786133,189.5009689331055,189.5009689331055,187.3496170043945,187.6682357788086,187.6682357788086,188.0019683837891,188.0019683837891,188.3543930053711,188.7079086303711,189.0643157958984,189.0643157958984,189.4310455322266,189.4310455322266,189.5693435668945,189.5693435668945,189.5693435668945,189.5693435668945,187.3909912109375,187.7069854736328,187.7069854736328,187.9984359741211,187.9984359741211,188.3421783447266,188.6929550170898,188.6929550170898,189.0514755249023,189.0514755249023,189.4151077270508,189.6366806030273,189.6366806030273,189.6366806030273,187.4583587646484,187.4583587646484,187.7544403076172,188.0684814453125,188.0684814453125,188.328727722168,188.328727722168,188.5764923095703,188.5764923095703,188.9216842651367,188.9216842651367,189.2687759399414,189.2687759399414,189.6302642822266,189.6302642822266,189.7028732299805,189.7028732299805,189.7028732299805,187.6462631225586,187.9424057006836,187.9424057006836,188.2594985961914,188.2594985961914,188.6025543212891,188.6025543212891,188.9550628662109,188.9550628662109,189.3150329589844,189.6882019042969,189.7679977416992,189.7679977416992,187.710090637207,187.908088684082,187.908088684082,188.185173034668,188.185173034668,188.5458984375,188.5458984375,188.8805389404297,188.8805389404297,188.8805389404297,189.2206115722656,189.2206115722656,189.5424575805664,189.5424575805664,189.8321228027344,189.8321228027344,189.8321228027344,189.8321228027344,187.8529968261719,187.8529968261719,188.1203155517578,188.3998260498047,188.3998260498047,188.7249984741211,188.7249984741211,189.0389938354492,189.3312835693359,189.6191787719727,189.6191787719727,189.8776397705078,187.7279281616211,187.7279281616211,187.9188461303711,187.9188461303711,188.1618804931641,188.4368515014648,188.4368515014648,188.6646881103516,188.9997787475586,188.9997787475586,189.2686538696289,189.2686538696289,189.557991027832,189.557991027832,189.557991027832,189.8774032592773,189.9572067260742,189.9572067260742,189.9572067260742,187.9603118896484,187.9603118896484,188.1680450439453,188.4204559326172,188.7234497070312,188.7234497070312,188.7234497070312,188.9803848266602,188.9803848266602,189.3306503295898,189.6729965209961,189.6729965209961,190.0145950317383,190.0145950317383,190.0182800292969,190.0182800292969,190.0182800292969,190.0182800292969,190.0182800292969,190.0182800292969,190.0182800292969,190.0182800292969,190.0182800292969,190.0182800292969,190.0182800292969,190.0182800292969,190.0182800292969,190.0182800292969,190.0182800292969,190.0182800292969,190.0182800292969,190.0182800292969,190.0182800292969,190.0182800292969,190.0182800292969,190.0182800292969,190.0182800292969,190.0182800292969,187.9895172119141,187.9895172119141,188.2069396972656,188.2069396972656,188.4347457885742,188.4347457885742,188.6921844482422,188.9865112304688,189.3076782226562,189.3076782226562,189.6407318115234,189.6407318115234,189.9829635620117,189.9829635620117,190.0779724121094,190.0779724121094,188.159065246582,188.159065246582,188.4266586303711,188.4266586303711,188.7300415039062,188.7300415039062,188.7300415039062,189.0638122558594,189.0638122558594,189.4111099243164,189.7695541381836,189.7695541381836,190.1370544433594,190.1370544433594,188.1158981323242,188.1158981323242,188.3830413818359,188.6621932983398,188.6621932983398,188.9837036132812,189.3310699462891,189.6806335449219,189.6806335449219,190.0432205200195,190.1952972412109,190.1952972412109,190.1952972412109,188.328239440918,188.328239440918,188.6011581420898,188.9075317382812,189.2452697753906,189.2452697753906,189.5846405029297,189.5846405029297,189.9341735839844,189.9341735839844,190.2524871826172,190.2524871826172,188.2921295166016,188.2921295166016,188.5520095825195,188.5520095825195,188.7610015869141,188.7610015869141,188.9347076416016,188.9347076416016,189.1155166625977,189.364990234375,189.364990234375,189.7161712646484,190.0921020507812,190.3087463378906,190.3087463378906,190.3087463378906,188.469123840332,188.7877883911133,188.7877883911133,189.1049194335938,189.1049194335938,189.4489974975586,189.4489974975586,189.7954406738281,190.1486206054688,190.1486206054688,190.3641586303711,190.3641586303711,188.526237487793,188.526237487793,188.7875213623047,189.077278137207,189.077278137207,189.4012908935547,189.7386245727539,189.7386245727539,190.0635833740234,190.0635833740234,190.3947372436523,190.3947372436523,190.3947372436523,190.4186401367188,190.4186401367188,188.7253494262695,188.7253494262695,188.9798278808594,189.2731094360352,189.5998916625977,189.5998916625977,189.9417190551758,189.9417190551758,190.2917098999023,190.4722213745117,190.4722213745117,190.4722213745117,188.7248916625977,188.7248916625977,188.9826202392578,188.9826202392578,189.2728729248047,189.2728729248047,189.6015396118164,189.6015396118164,189.9453506469727,190.2966003417969,190.2966003417969,190.5249481201172,190.5249481201172,188.7732543945312,188.7732543945312,189.0277633666992,189.3112640380859,189.3112640380859,189.6660766601562,189.6660766601562,190.009147644043,190.009147644043,190.359977722168,190.5768203735352,190.5768203735352,190.5768203735352,190.5768203735352,188.8652420043945,188.8652420043945,189.1240844726562,189.1240844726562,189.4139938354492,189.4139938354492,189.7413864135742,189.7413864135742,190.0636749267578,190.4022827148438,190.6278915405273,190.6278915405273,190.6278915405273,188.9016189575195,189.1443176269531,189.1443176269531,189.4122543334961,189.4122543334961,189.7201080322266,190.0601119995117,190.0601119995117,190.4145889282227,190.4145889282227,190.6780319213867,190.6780319213867,188.9782409667969,189.2261199951172,189.5016326904297,189.5016326904297,189.8164596557617,189.8164596557617,190.156005859375,190.156005859375,190.5030822753906,190.5030822753906,190.5030822753906,190.7275085449219,190.7275085449219,190.7275085449219,189.0777053833008,189.0777053833008,189.3244781494141,189.6313400268555,189.6313400268555,189.9540786743164,190.3014907836914,190.3014907836914,190.6547622680664,190.7761154174805,190.7761154174805,189.2259826660156,189.4858016967773,189.4858016967773,189.7778015136719,189.7778015136719,189.7778015136719,190.1066513061523,190.1066513061523,190.1066513061523,190.456413269043,190.8072967529297,190.8072967529297,190.8238830566406,190.8238830566406,189.3713760375977,189.3713760375977,189.3713760375977,189.6361846923828,189.6361846923828,189.942008972168,189.942008972168,190.2790832519531,190.2790832519531,190.6300506591797,190.6300506591797,190.8709869384766,190.8709869384766,190.8709869384766,189.2920989990234,189.2920989990234,189.5447998046875,189.5447998046875,189.8257064819336,189.8257064819336,189.8257064819336,190.1487579345703,190.1487579345703,190.482795715332,190.8308715820312,190.8308715820312,190.9173202514648,190.9173202514648,189.4372100830078,189.4372100830078,189.7004089355469,189.7004089355469,189.9918899536133,189.9918899536133,190.3140716552734,190.3140716552734,190.6529388427734,190.6529388427734,190.9627990722656,190.9627990722656,190.9627990722656,189.3984603881836,189.3984603881836,189.6448287963867,189.6448287963867,189.9254913330078,190.24267578125,190.58740234375,190.9449615478516,190.9449615478516,190.9449615478516,191.0076293945312,191.0076293945312,191.0076293945312,189.6252899169922,189.6252899169922,189.8980255126953,189.8980255126953,190.2082061767578,190.2082061767578,190.5499267578125,190.9034423828125,190.9034423828125,191.0517349243164,191.0517349243164,191.0517349243164,189.6339721679688,189.6339721679688,189.8926620483398,189.8926620483398,189.8926620483398,190.1888275146484,190.521598815918,190.521598815918,190.8718490600586,190.8718490600586,191.0950622558594,191.0950622558594,191.0950622558594,191.0950622558594,191.0950622558594,191.0950622558594,191.0950622558594,191.0950622558594,191.0950622558594,191.0950622558594,191.0950622558594,191.0950622558594,191.0950622558594,191.0950622558594,191.0950622558594,191.0950622558594,191.0950622558594,191.0950622558594,191.0950622558594,191.0950622558594,191.0950622558594,191.0950622558594,191.0950622558594,191.0950622558594,191.0950622558594,191.0950622558594,191.0950622558594,191.0950622558594,191.0950622558594,191.0950622558594,191.0950622558594,191.0950622558594,191.0950622558594,191.0950622558594,191.0950622558594,191.0950622558594,191.0950622558594,191.0950622558594,191.0950622558594,191.0950622558594,191.0950622558594,191.0950622558594,191.0950622558594,191.0950622558594,191.0950622558594,191.0950622558594,189.6017684936523,189.6017684936523,189.6017684936523,189.6017684936523,189.7937316894531,189.7937316894531,190.0445938110352,190.3288803100586,190.3288803100586,190.6415786743164,190.6415786743164,190.9438095092773,191.2582550048828,191.2582550048828,191.6032409667969,191.9853820800781,191.9853820800781,192.3763885498047,192.7498779296875,193.0759429931641,193.0759429931641,193.4004669189453,193.7275390625,193.7275390625,194.0519561767578,194.0519561767578,194.3774719238281,194.3774719238281,194.3774719238281,194.4390411376953,194.4390411376953,189.9825744628906,189.9825744628906,190.3016357421875,190.6440963745117,190.6440963745117,190.9689025878906,190.9689025878906,191.2950057983398,191.2950057983398,191.6541519165039,191.6541519165039,192.0216445922852,192.0216445922852,192.400505065918,192.7887649536133,192.7887649536133,193.1826095581055,193.5719299316406,193.5719299316406,193.9353256225586,193.9353256225586,194.3092803955078,194.3092803955078,194.5712738037109,194.5712738037109,194.5712738037109,194.5712738037109,194.5712738037109,194.5712738037109,190.2782135009766,190.5778732299805,190.5778732299805,190.8970489501953,190.8970489501953,191.1941299438477,191.5413970947266,191.8937911987305,191.8937911987305,192.2545318603516,192.2545318603516,192.6259155273438,193.0102005004883,193.3936004638672,193.3936004638672,193.7836990356445,194.17529296875,194.559814453125,194.559814453125,194.7014923095703,194.7014923095703,190.3206176757812,190.3206176757812,190.6090774536133,190.6090774536133,190.9198837280273,190.9198837280273,191.2222137451172,191.2222137451172,191.5488052368164,191.5488052368164,191.8822326660156,192.2364654541016,192.2364654541016,192.5975875854492,192.5975875854492,192.9646682739258,193.3382720947266,193.3382720947266,193.7045211791992,193.7045211791992,194.0714569091797,194.0714569091797,194.4535827636719,194.4535827636719,194.8242568969727,194.8295288085938,194.8295288085938,190.5575408935547,190.8512878417969,191.1551818847656,191.1551818847656,191.4532775878906,191.4532775878906,191.7963333129883,192.1450042724609,192.5038528442383,192.5038528442383,192.8704833984375,192.8704833984375,193.2410278320312,193.2410278320312,193.6223373413086,194.0059661865234,194.0059661865234,194.0059661865234,194.3984909057617,194.3984909057617,194.3984909057617,194.7886123657227,194.7886123657227,194.9556198120117,194.9556198120117,194.9556198120117,190.6631164550781,190.6631164550781,190.6631164550781,190.9409027099609,190.9409027099609,191.2359771728516,191.525749206543,191.525749206543,191.8691711425781,191.8691711425781,192.2508010864258,192.6078948974609,192.6078948974609,192.9741134643555,193.3484039306641,193.3484039306641,193.7328720092773,193.7328720092773,194.1173400878906,194.505859375,194.505859375,194.8940124511719,194.8940124511719,195.0795288085938,195.0795288085938,195.0795288085938,190.8412933349609,191.1176681518555,191.4054489135742,191.4054489135742,191.695686340332,192.0383224487305,192.0383224487305,192.3841323852539,192.7390594482422,192.7390594482422,193.1001281738281,193.1001281738281,193.4703826904297,193.8401794433594,194.2107315063477,194.2107315063477,194.5980606079102,194.9742584228516,194.9742584228516,195.2015075683594,195.2015075683594,195.2015075683594,195.2015075683594,195.2015075683594,195.2015075683594,191.253547668457,191.253547668457,191.5320434570312,191.5320434570312,191.8182067871094,191.8182067871094,192.1559829711914,192.5007934570312,192.8451156616211,192.8451156616211,192.8451156616211,193.1990814208984,193.5642013549805,193.5642013549805,193.5642013549805,193.9348068237305,193.9348068237305,193.9348068237305,194.320671081543,194.320671081543,194.7053680419922,195.0932922363281,195.0932922363281,195.3214874267578,195.3214874267578,191.2111892700195,191.4819030761719,191.4819030761719,191.4819030761719,191.7531127929688,192.0497207641602,192.0497207641602,192.3910369873047,192.3910369873047,192.7359008789062,193.0810012817383,193.0810012817383,193.4319458007812,193.4319458007812,193.7980117797852,193.7980117797852,193.7980117797852,194.1746292114258,194.5587005615234,194.5587005615234,194.5587005615234,194.9473724365234,194.9473724365234,195.3274765014648,195.3274765014648,195.439582824707,195.439582824707,195.439582824707,191.4420700073242,191.4420700073242,191.7087936401367,191.9722518920898,191.9722518920898,192.2895660400391,192.6299896240234,192.9757995605469,193.3257598876953,193.6836013793945,193.6836013793945,194.0566864013672,194.0566864013672,194.4364547729492,194.4364547729492,194.8222885131836,194.8222885131836,194.8222885131836,195.2080307006836,195.5556716918945,195.5556716918945,195.5556716918945,195.5556716918945,191.7237548828125,191.7237548828125,191.9865646362305,192.2625885009766,192.2625885009766,192.5512008666992,192.8771209716797,192.8771209716797,193.2112350463867,193.2112350463867,193.5455169677734,193.5455169677734,193.5455169677734,193.888916015625,193.888916015625,194.2800369262695,194.638557434082,194.638557434082,194.638557434082,194.975471496582,194.975471496582,195.3274536132812,195.6699981689453,195.6699981689453,195.6699981689453,195.6699981689453,195.6699981689453,195.6699981689453,191.8531265258789,191.8531265258789,192.1066818237305,192.1066818237305,192.3776702880859,192.697021484375,192.697021484375,193.0295181274414,193.0295181274414,193.0295181274414,193.3704452514648,193.619987487793,193.619987487793,193.9402542114258,193.9402542114258,193.9402542114258,194.2941665649414,194.2941665649414,194.6600189208984,195.0326766967773,195.404914855957,195.7780456542969,195.7823867797852,195.7823867797852,195.7823867797852,192.0370941162109,192.0370941162109,192.2874984741211,192.5629959106445,192.5629959106445,192.877799987793,192.877799987793,193.2124328613281,193.2124328613281,193.5481643676758,193.5481643676758,193.8915252685547,194.2891693115234,194.2891693115234,194.6560974121094,194.6560974121094,194.6560974121094,195.0361709594727,195.0361709594727,195.4099197387695,195.4099197387695,195.7874908447266,195.8930206298828,195.8930206298828,195.8930206298828,192.1405487060547,192.1405487060547,192.1405487060547,192.3895263671875,192.3895263671875,192.6560287475586,192.9638824462891,192.9638824462891,192.9638824462891,193.2943496704102,193.6347045898438,193.9858322143555,194.3473281860352,194.3473281860352,194.7229537963867,195.1036148071289,195.1036148071289,195.4900283813477,195.4900283813477,195.8720779418945,195.8720779418945,196.0018768310547,196.0018768310547,192.3033447265625,192.5577850341797,192.8326873779297,192.8326873779297,193.1443328857422,193.4738922119141,193.4738922119141,193.8155288696289,193.8155288696289,194.1668930053711,194.1668930053711,194.5294342041016,194.5294342041016,194.9033050537109,194.9033050537109,195.2834548950195,195.6706619262695,195.6706619262695,196.0488128662109,196.10888671875,196.10888671875,196.10888671875,192.5360565185547,192.5360565185547,192.7815322875977,193.0652770996094,193.0652770996094,193.3730621337891,193.3730621337891,193.7022552490234,194.0435791015625,194.0435791015625,194.3973846435547,194.7605743408203,194.7605743408203,195.1371917724609,195.5173797607422,195.9033279418945,196.2142715454102,196.2142715454102,196.2142715454102,196.2142715454102,192.7474899291992,192.7474899291992,192.9953155517578,193.2735061645508,193.5771942138672,193.9045867919922,193.9045867919922,193.9045867919922,194.2443008422852,194.2443008422852,194.5898132324219,194.5898132324219,194.9493637084961,194.9493637084961,195.3210067749023,195.6518173217773,195.6518173217773,195.6518173217773,195.9119644165039,196.2782516479492,196.2782516479492,196.3179321289062,196.3179321289062,196.3179321289062,192.8292007446289,192.8292007446289,193.0730972290039,193.0730972290039,193.3461303710938,193.3461303710938,193.6405639648438,193.6405639648438,193.9624557495117,194.3338928222656,194.3338928222656,194.6769256591797,195.0402297973633,195.4093627929688,195.7906875610352,195.7906875610352,196.1560821533203,196.4199447631836,196.4199447631836,196.4199447631836,196.4199447631836,196.4199447631836,196.4199447631836,193.0849761962891,193.0849761962891,193.3388519287109,193.3388519287109,193.6101531982422,193.6101531982422,193.8966751098633,194.2197265625,194.2197265625,194.547004699707,194.547004699707,194.8857269287109,195.2315216064453,195.5946197509766,195.5946197509766,195.5946197509766,195.9597702026367,195.9597702026367,195.9597702026367,196.3270416259766,196.3270416259766,196.5202331542969,196.5202331542969,196.5202331542969,196.5202331542969,196.5202331542969,196.5202331542969,193.2740478515625,193.2740478515625,193.5319976806641,193.5319976806641,193.5319976806641,193.8066177368164,193.8066177368164,194.0918121337891,194.4116592407227,194.4116592407227,194.4116592407227,194.7396621704102,194.7396621704102,195.1089935302734,195.1089935302734,195.4487686157227,195.8093566894531,195.8093566894531,196.1834945678711,196.5570220947266,196.5570220947266,196.6189651489258,196.6189651489258,196.6189651489258,193.2782974243164,193.2782974243164,193.5141830444336,193.5141830444336,193.7715530395508,193.7715530395508,194.0543518066406,194.3657379150391,194.3657379150391,194.3657379150391,194.7024536132812,194.7024536132812,195.0431060791016,195.3989181518555,195.3989181518555,195.772331237793,195.772331237793,196.1515197753906,196.1515197753906,196.5357055664062,196.7160491943359,196.7160491943359,196.7160491943359,196.7160491943359,196.7160491943359,196.7160491943359,196.7160491943359,196.7160491943359,196.7160491943359,196.7160491943359,196.7160491943359,196.7160491943359,196.7160491943359,196.7160491943359,196.7160491943359,196.7160491943359,196.7160491943359,196.7160491943359,196.7160491943359,196.7160491943359,196.7160491943359,196.7160491943359,196.7160491943359,196.7160491943359,196.7160491943359,196.7160491943359,196.7160491943359,196.7160491943359,196.7160491943359,196.7160491943359,196.7160491943359,196.7160491943359,196.7160491943359,196.7160491943359,196.7160491943359,196.7160491943359,193.4593276977539,193.6506652832031,193.8684234619141,193.8684234619141,194.0980758666992,194.0980758666992,194.3514556884766,194.3514556884766,194.6429290771484,194.6429290771484,194.9584197998047,195.2885589599609,195.2885589599609,195.6312255859375,195.6312255859375,195.6312255859375,195.983268737793,196.3555755615234,196.3555755615234,196.7313232421875,196.8114166259766,196.8114166259766,193.5768432617188,193.5768432617188,193.8144836425781,193.8144836425781,194.0685806274414,194.3494644165039,194.3494644165039,194.6630859375,194.6630859375,195.0015182495117,195.0015182495117,195.3427124023438,195.3427124023438,195.6952514648438,196.0642013549805,196.4425659179688,196.4425659179688,196.8175354003906,196.8175354003906,196.9054489135742,196.9054489135742,196.9054489135742,193.7171859741211,193.9519729614258,194.2044143676758,194.2044143676758,194.5134963989258,194.5134963989258,194.8289489746094,194.8289489746094,195.1660232543945,195.5041809082031,195.5041809082031,195.8567657470703,195.8567657470703,196.2276763916016,196.2276763916016,196.6081008911133,196.6081008911133,196.9832611083984,196.9832611083984,196.9980087280273,196.9980087280273,196.9980087280273,193.8941268920898,194.1314544677734,194.1314544677734,194.1314544677734,194.3827209472656,194.3827209472656,194.6666412353516,194.6666412353516,194.9837799072266,195.3241348266602,195.3241348266602,195.6695404052734,196.026985168457,196.026985168457,196.3994522094727,196.3994522094727,196.7802352905273,196.7802352905273,197.0890274047852,197.0890274047852,197.0890274047852,197.0890274047852,194.0854644775391,194.0854644775391,194.0854644775391,194.324089050293,194.5820541381836,194.5820541381836,194.8713989257812,195.1967468261719,195.1967468261719,195.5375289916992,195.5375289916992,195.5375289916992,195.8800506591797,195.8800506591797,196.2311859130859,196.2311859130859,196.2311859130859,196.5990295410156,196.9790420532227,197.178581237793,197.178581237793,197.178581237793,197.178581237793,197.178581237793,197.178581237793,194.3206481933594,194.3206481933594,194.5625839233398,194.8332824707031,195.138542175293,195.4705581665039,195.4705581665039,195.8106384277344,195.8106384277344,195.8106384277344,196.1653823852539,196.5326995849609,196.9133758544922,196.9133758544922,197.266731262207,197.266731262207,197.266731262207,197.266731262207,197.266731262207,197.266731262207,194.3404541015625,194.3404541015625,194.5838394165039,194.5838394165039,194.8400344848633,194.8400344848633,195.1304321289062,195.4503555297852,195.4503555297852,195.4503555297852,195.7914733886719,195.7914733886719,196.1365051269531,196.4975662231445,196.8720321655273,197.2481307983398,197.2481307983398,197.353385925293,197.353385925293,197.353385925293,194.390625,194.390625,194.6187438964844,194.6187438964844,194.8604202270508,194.8604202270508,195.1299743652344,195.434196472168,195.434196472168,195.739860534668,195.739860534668,196.0750198364258,196.415641784668,196.415641784668,196.7663955688477,197.1661987304688,197.4386672973633,197.4386672973633,197.4386672973633,197.4386672973633,197.4386672973633,197.4386672973633,194.6378402709961,194.6378402709961,194.8721237182617,194.8721237182617,195.1233749389648,195.1233749389648,195.4051742553711,195.4051742553711,195.4051742553711,195.7208786010742,195.7208786010742,196.057975769043,196.057975769043,196.3974838256836,196.3974838256836,196.7454605102539,196.7454605102539,196.7454605102539,197.1125717163086,197.1125717163086,197.1125717163086,197.4836654663086,197.4836654663086,197.5226211547852,197.5226211547852,194.6968536376953,194.6968536376953,194.9229049682617,194.9229049682617,195.1683120727539,195.4461364746094,195.4461364746094,195.7562484741211,195.7562484741211,196.0829544067383,196.0829544067383,196.4198760986328,196.4198760986328,196.7634353637695,197.1243896484375,197.1243896484375,197.4961090087891,197.4961090087891,197.6050872802734,197.6050872802734,194.7832489013672,194.7832489013672,195.0313873291016,195.0313873291016,195.2759017944336,195.5514831542969,195.8629531860352,195.8629531860352,196.1991653442383,196.1991653442383,196.5406951904297,196.5406951904297,196.8928451538086,196.8928451538086,196.8928451538086,197.2636260986328,197.2636260986328,197.6395416259766,197.6863784790039,197.6863784790039,197.6863784790039,194.9447784423828,194.9447784423828,195.172966003418,195.4195098876953,195.6979598999023,195.6979598999023,196.013671875,196.3509368896484,196.6972732543945,196.6972732543945,197.0496368408203,197.0496368408203,197.0496368408203,197.4184112548828,197.7662811279297,197.7662811279297,197.7662811279297,197.7662811279297,197.7662811279297,197.7662811279297,195.1109466552734,195.1109466552734,195.3448715209961,195.3448715209961,195.6006774902344,195.6006774902344,195.8884887695312,195.8884887695312,196.2127380371094,196.2127380371094,196.5566711425781,196.5566711425781,196.9007949829102,196.9007949829102,197.265739440918,197.6407852172852,197.6407852172852,197.6407852172852,197.8448638916016,197.8448638916016,197.8448638916016,197.8448638916016,197.8448638916016,197.8448638916016,195.3353958129883,195.3353958129883,195.5724487304688,195.5724487304688,195.8385391235352,196.1445693969727,196.4800109863281,196.4800109863281,196.7969360351562,196.7969360351562,197.1400451660156,197.5014572143555,197.5014572143555,197.8701324462891,197.922248840332,197.922248840332,197.922248840332,195.2853698730469,195.2853698730469,195.2853698730469,195.5089721679688,195.7519378662109,195.7519378662109,196.0210113525391,196.3347549438477,196.3347549438477,196.6664047241211,196.6664047241211,197.0074691772461,197.0074691772461,197.3642501831055,197.3642501831055,197.7233581542969,197.9982681274414,197.9982681274414,197.9982681274414,197.9982681274414,197.9982681274414,197.9982681274414,195.4991607666016,195.4991607666016,195.7257308959961,195.7257308959961,195.9761199951172,195.9761199951172,196.2633361816406,196.5846786499023,196.5846786499023,196.9645614624023,196.9645614624023,197.3145065307617,197.679313659668,197.679313659668,198.0493850708008,198.0493850708008,198.0732116699219,198.0732116699219,198.0732116699219,195.5587997436523,195.7844848632812,195.7844848632812,196.0303726196289,196.3100814819336,196.6276473999023,196.6276473999023,196.9665374755859,197.3123321533203,197.3123321533203,197.6761245727539,197.6761245727539,198.0481491088867,198.0481491088867,198.1468124389648,198.1468124389648,195.6206207275391,195.6206207275391,195.6206207275391,195.8445663452148,195.8445663452148,196.0828170776367,196.0828170776367,196.3563690185547,196.3563690185547,196.6664505004883,196.6664505004883,197.003173828125,197.003173828125,197.3484039306641,197.3484039306641,197.7096786499023,197.7096786499023,198.0762786865234,198.2192916870117,198.2192916870117,198.2192916870117,198.2192916870117,195.9162750244141,196.1972808837891,196.4895935058594,196.4895935058594,196.8193435668945,197.166145324707,197.4940719604492,197.841423034668,198.1969375610352,198.1969375610352,198.290641784668,198.290641784668,198.290641784668,198.290641784668,198.290641784668,198.290641784668,196.0497360229492,196.0497360229492,196.2883377075195,196.2883377075195,196.5562896728516,196.5562896728516,196.8637771606445,197.1971817016602,197.5426788330078,197.5426788330078,197.9014892578125,197.9014892578125,198.2715530395508,198.2715530395508,198.3607177734375,198.3607177734375,198.3607177734375,195.952751159668,195.952751159668,195.952751159668,196.1773376464844,196.4138793945312,196.6831207275391,196.6831207275391,196.9932479858398,197.3307571411133,197.3307571411133,197.6780776977539,198.0351715087891,198.4297637939453,198.4297637939453,198.4297637939453,198.4297637939453,198.4297637939453,198.4297637939453,198.4297637939453,198.4297637939453,198.4297637939453,198.4297637939453,198.4297637939453,198.4297637939453,198.4297637939453,198.4297637939453,198.4297637939453,198.4297637939453,198.4297637939453,198.4297637939453,198.4297637939453,198.4297637939453,198.4297637939453,198.4297637939453,198.4297637939453,198.4297637939453,198.4297637939453,198.4297637939453,198.4297637939453,198.4297637939453,198.4297637939453,198.4297637939453,198.4297637939453,198.4297637939453,198.4297637939453,196.0741119384766,196.0741119384766,196.0741119384766,196.2692337036133,196.2692337036133,196.4875030517578,196.4875030517578,196.7226791381836,196.7226791381836,196.7226791381836,196.9913635253906,197.2952651977539,197.2952651977539,197.6187973022461,197.6187973022461,197.9482345581055,197.9482345581055,198.245719909668,198.4765396118164,198.4765396118164,198.497428894043,198.497428894043,198.497428894043,198.497428894043,198.497428894043,198.497428894043,196.1746139526367,196.1746139526367,196.3501129150391,196.3501129150391,196.6463165283203,196.6463165283203,196.9121398925781,196.9121398925781,197.1876525878906,197.1876525878906,197.5204696655273,197.8583221435547,197.8583221435547,198.2118911743164,198.5642623901367,198.5642623901367,198.5642623901367,198.5642623901367,198.5642623901367,198.5642623901367,196.3197708129883,196.3197708129883,196.5432205200195,196.7868881225586,196.7868881225586,197.0595779418945,197.0595779418945,197.3759765625,197.3759765625,197.7476425170898,197.7476425170898,197.7476425170898,198.0906753540039,198.0906753540039,198.4218139648438,198.4218139648438,198.6299819946289,198.6299819946289,198.6299819946289,198.6299819946289,196.5124053955078,196.5124053955078,196.7393112182617,196.7393112182617,196.9913482666016,196.9913482666016,197.2848052978516,197.6128540039062,197.6128540039062,197.9590911865234,197.9590911865234,198.3082275390625,198.3082275390625,198.676025390625,198.676025390625,198.694694519043,198.694694519043,196.5066375732422,196.732780456543,196.732780456543,196.9745788574219,196.9745788574219,197.2555541992188,197.2555541992188,197.5734939575195,197.5734939575195,197.917610168457,197.917610168457,198.2669906616211,198.2669906616211,198.6347427368164,198.6347427368164,198.7583465576172,198.7583465576172,198.7583465576172,198.7583465576172,196.7966995239258,196.7966995239258,197.0372619628906,197.0372619628906,197.3138275146484,197.3138275146484,197.6272506713867,197.6272506713867,197.9675140380859,197.9675140380859,198.3147506713867,198.3147506713867,198.3147506713867,198.6727142333984,198.6727142333984,198.8209915161133,198.8209915161133,198.8209915161133,198.8209915161133,198.8209915161133,198.8209915161133,196.8439025878906,196.8439025878906,197.0790100097656,197.0790100097656,197.3481903076172,197.3481903076172,197.659309387207,197.999626159668,198.347526550293,198.7062149047852,198.7062149047852,198.882568359375,198.882568359375,198.882568359375,198.882568359375,198.882568359375,198.882568359375,196.9296112060547,196.9296112060547,197.158447265625,197.158447265625,197.4207916259766,197.4207916259766,197.7261657714844,198.0615005493164,198.4093017578125,198.765266418457,198.765266418457,198.9432144165039,198.9432144165039,198.9432144165039,198.9432144165039,198.9432144165039,198.9432144165039,197.0415573120117,197.0415573120117,197.2768783569336,197.2768783569336,197.5430450439453,197.5430450439453,197.8499526977539,197.8499526977539,198.1864547729492,198.5325698852539,198.5325698852539,198.5325698852539,198.8882293701172,199.0028305053711,199.0028305053711,199.0028305053711,199.0028305053711,199.0028305053711,199.0028305053711,197.1526336669922,197.1526336669922,197.1526336669922,197.3830108642578,197.3830108642578,197.6309661865234,197.6309661865234,197.919792175293,197.919792175293,198.2442321777344,198.5841598510742,198.5841598510742,198.9291305541992,198.9291305541992,199.0614929199219,199.0614929199219,199.0614929199219,199.0614929199219,197.219108581543,197.4515609741211,197.4515609741211,197.717658996582,198.0251998901367,198.0251998901367,198.0251998901367,198.3951034545898,198.3951034545898,198.7434692382812,199.1026458740234,199.1026458740234,199.1192855834961,199.1192855834961,199.1192855834961,197.162712097168,197.3870468139648,197.3870468139648,197.6304244995117,197.6304244995117,197.9122848510742,197.9122848510742,198.2267379760742,198.564811706543,198.9113998413086,198.9113998413086,198.9113998413086,199.1760177612305,199.1760177612305,199.1760177612305,199.1760177612305,199.1760177612305,199.1760177612305,197.3192367553711,197.3192367553711,197.5440063476562,197.5440063476562,197.7919540405273,197.7919540405273,198.0787048339844,198.0787048339844,198.0787048339844,198.4006805419922,198.7439270019531,198.7439270019531,199.076286315918,199.076286315918,199.2319259643555,199.2319259643555,199.2319259643555,199.2319259643555,199.2319259643555,199.2319259643555,197.4788208007812,197.7110977172852,197.9765396118164,198.2795181274414,198.2795181274414,198.6138687133789,198.9572601318359,198.9572601318359,199.2869262695312,199.2869262695312,199.2869262695312,199.2869262695312,197.4342193603516,197.6552886962891,197.6552886962891,197.8932342529297,197.8932342529297,198.1685562133789,198.1685562133789,198.4826202392578,198.82275390625,198.82275390625,199.1692581176758,199.1692581176758,199.3409423828125,199.3409423828125,199.3409423828125,199.3409423828125,199.3409423828125,199.3409423828125,199.3409423828125,199.3409423828125,199.3409423828125,199.3409423828125,199.3409423828125,199.3409423828125,197.5863418579102,197.7943496704102,198.0234603881836,198.0234603881836,198.2795104980469,198.2795104980469,198.2795104980469,198.5742721557617,198.5742721557617,198.8973617553711,198.8973617553711,199.2711563110352,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,199.3941421508789,197.5625228881836,197.5625228881836,197.5625228881836,197.5625228881836,197.5625228881836,197.5625228881836,197.8032455444336,197.8032455444336,198.0594635009766,198.0594635009766,198.349853515625,198.349853515625,198.6722106933594,198.6722106933594,198.9971694946289,199.2881088256836,199.2881088256836,199.6204605102539,199.6204605102539,199.945915222168,200.3180541992188,200.7073593139648,201.095458984375,201.4689254760742,201.4689254760742,201.7955017089844,201.7955017089844,202.121711730957,202.121711730957,202.4482803344727,202.4482803344727,202.4482803344727,202.7760009765625,203.1043853759766,203.1043853759766,203.1043853759766,203.4299392700195,203.754150390625,203.754150390625,204.0791702270508,204.0791702270508,204.4048767089844,204.4048767089844,204.7326202392578,204.7326202392578,205.0578308105469,205.1751556396484,205.1751556396484,205.1751556396484,205.1751556396484,205.1751556396484,205.1751556396484,198.0103454589844,198.2691116333008,198.2691116333008,198.5639190673828,198.5639190673828,198.8902969360352,198.8902969360352,199.2121429443359,199.2121429443359,199.2121429443359,199.5121688842773,199.5121688842773,199.8948822021484,200.2535552978516,200.2535552978516,200.6301422119141,200.6301422119141,201.011962890625,201.011962890625,201.4036560058594,201.4036560058594,201.7963562011719,201.7963562011719,202.1935119628906,202.5916213989258,202.5916213989258,202.9878463745117,202.9878463745117,203.384765625,203.384765625,203.7829208374023,203.7829208374023,204.1806030273438,204.5755615234375,204.5755615234375,204.5755615234375,204.9640350341797,204.9640350341797,205.3465423583984,205.3832931518555,205.3832931518555,205.3832931518555,205.3832931518555,205.3832931518555,205.3832931518555,198.3794937133789,198.3794937133789,198.3794937133789,198.6400527954102,198.9313430786133,199.2480926513672,199.2480926513672,199.551139831543,199.551139831543,199.8699645996094,200.2188110351562,200.2188110351562,200.5745544433594,200.5745544433594,200.9491577148438,200.9491577148438,201.3263092041016,201.71142578125,201.71142578125,202.0967712402344,202.0967712402344,202.4873657226562,202.4873657226562,202.8812026977539,203.2739181518555,203.6670913696289,203.6670913696289,204.0600509643555,204.4900894165039,204.4900894165039,204.8858413696289,204.8858413696289,205.2107696533203,205.2107696533203,205.5066680908203,205.5066680908203,205.5882186889648,205.5882186889648,205.5882186889648,205.5882186889648,205.5882186889648,205.5882186889648,198.6798706054688,198.9384460449219,198.9384460449219,199.225700378418,199.225700378418,199.5317535400391,199.5317535400391,199.5317535400391,199.8239669799805,200.1575469970703,200.5061721801758,200.5061721801758,200.8604736328125,200.8604736328125,200.8604736328125,201.232795715332,201.232795715332,201.6137542724609,201.6137542724609,202.0054473876953,202.0054473876953,202.3939895629883,202.7833709716797,202.7833709716797,203.1800079345703,203.5789108276367,203.5789108276367,203.9767303466797,203.9767303466797,204.3731536865234,204.3731536865234,204.7718658447266,205.1713562011719,205.5561752319336,205.5561752319336,205.7897491455078,205.7897491455078,205.7897491455078,205.7897491455078,205.7897491455078,205.7897491455078,198.8652420043945,198.8652420043945,199.0883407592773,199.0883407592773,199.3528900146484,199.3528900146484,199.6387405395508,199.6387405395508,199.9545974731445,199.9545974731445,200.2702789306641,200.6132278442383,200.9631118774414,200.9631118774414,201.3182907104492,201.6926879882812,201.6926879882812,202.0734939575195,202.0734939575195,202.4614639282227,202.4614639282227,202.8459854125977,203.2261962890625,203.2261962890625,203.2261962890625,203.6145706176758,203.9983139038086,203.9983139038086,204.3838043212891,204.3838043212891,204.7710800170898,204.7710800170898,205.1587600708008,205.1587600708008,205.5507049560547,205.5507049560547,205.9248428344727,205.9248428344727,205.9880065917969,205.9880065917969,205.9880065917969,205.9880065917969,205.9880065917969,205.9880065917969,199.2791900634766,199.2791900634766,199.2791900634766,199.5229110717773,199.5229110717773,199.7824249267578,199.7824249267578,200.0531845092773,200.0531845092773,200.3351898193359,200.3351898193359,200.6670150756836,200.6670150756836,201.0051574707031,201.0051574707031,201.346923828125,201.7090454101562,202.0801773071289,202.4579238891602,202.4579238891602,202.8429565429688,202.8429565429688,203.2242813110352,203.6066207885742,203.6066207885742,203.9889526367188,203.9889526367188,204.4110107421875,204.4110107421875,204.8015670776367,204.8015670776367,205.1976852416992,205.5936660766602,205.5936660766602,205.9745941162109,206.1831130981445,206.1831130981445,206.1831130981445,206.1831130981445,206.1831130981445,206.1831130981445,199.4789657592773,199.6969299316406,199.9535598754883,199.9535598754883,200.2194290161133,200.2194290161133,200.4874267578125,200.8128662109375,201.1508712768555,201.1508712768555,201.4916305541992,201.4916305541992,201.8418579101562,201.8418579101562,202.2077255249023,202.2077255249023,202.5824279785156,202.5824279785156,202.9580612182617,203.3397445678711,203.3397445678711,203.3397445678711,203.7217712402344,203.7217712402344,203.7217712402344,204.1036224365234,204.1036224365234,204.4878845214844,204.4878845214844,204.4878845214844,204.8727569580078,205.262077331543,205.262077331543,205.6461944580078,205.6461944580078,206.02099609375,206.02099609375,206.3750534057617,206.3750534057617,206.3750534057617,206.3750534057617,206.3750534057617,206.3750534057617,206.3750534057617,206.3750534057617,206.3750534057617,206.3750534057617,206.3750534057617,206.3750534057617,206.3750534057617,206.3750534057617,206.3750534057617,206.3750534057617,199.8623809814453,199.8623809814453,199.8623809814453,200.0888519287109,200.3253326416016,200.5608215332031,200.8266296386719,200.8266296386719,201.1391220092773,201.1391220092773,201.4658584594727,201.4658584594727,201.8019104003906,201.8019104003906,202.1451950073242,202.5064315795898,202.5064315795898,202.8758087158203,203.2480621337891,203.6233367919922,203.6233367919922,203.9966430664062,204.3768615722656,204.3768615722656,204.7624206542969,205.1485748291016,205.1485748291016,205.5383071899414,205.9345855712891,205.9345855712891,206.3167190551758,206.3167190551758,206.5638122558594,206.5638122558594,206.5638122558594,206.5638122558594,206.5638122558594,206.5638122558594,206.5638122558594,206.5638122558594,206.5638122558594,200.2785568237305,200.2785568237305,200.5215759277344,200.5215759277344,200.7696914672852,200.7696914672852,201.0439453125,201.0439453125,201.0439453125,201.3617248535156,201.3617248535156,201.7282943725586,201.7282943725586,202.0702972412109,202.0702972412109,202.416389465332,202.416389465332,202.7739868164062,202.7739868164062,203.1410598754883,203.1410598754883,203.5135955810547,203.5135955810547,203.8886337280273,204.2702941894531,204.6543426513672,204.6543426513672,205.0381469726562,205.0381469726562,205.4276657104492,205.4276657104492,205.8216781616211,206.2180328369141,206.2180328369141,206.2180328369141,206.5975189208984,206.7497024536133,206.7497024536133,206.7497024536133,206.7497024536133,206.7497024536133,206.7497024536133,200.3904571533203,200.630126953125,200.630126953125,200.8698501586914,200.8698501586914,201.1115112304688,201.4081497192383,201.4081497192383,201.7335205078125,201.7335205078125,202.0681610107422,202.0681610107422,202.4041976928711,202.4041976928711,202.7388229370117,202.7388229370117,203.0905685424805,203.4489364624023,203.4489364624023,203.8152847290039,204.1894454956055,204.5707778930664,204.5707778930664,204.5707778930664,204.9549102783203,204.9549102783203,205.3400573730469,205.3400573730469,205.7304916381836,205.7304916381836,206.1258239746094,206.5187149047852,206.8983383178711,206.932487487793,206.932487487793,206.932487487793,206.932487487793,206.932487487793,206.932487487793,200.7667465209961,201.0055694580078,201.2408905029297,201.2408905029297,201.5127639770508,201.8214263916016,202.1526565551758,202.488883972168,202.488883972168,202.8254470825195,202.8254470825195,203.1744079589844,203.5359344482422,203.5359344482422,203.9051055908203,204.2776947021484,204.2776947021484,212.0443725585938,212.0443725585938,212.0443725585938,212.0443725585938,212.0443725585938,212.0443725585938,212.0443725585938,212.0443725585938,212.0443725585938,212.0443725585938,212.0443725585938,212.0443725585938,212.0443725585938,212.0443725585938,212.0443725585938,212.0443725585938,212.0443725585938,212.0443725585938,219.6737670898438,219.6737747192383,219.6737747192383,219.6737747192383,219.6737747192383,219.6737747192383,219.6737747192383,219.6737747192383,219.6737747192383,219.6737747192383,219.6737747192383,219.6737747192383,219.6737747192383,219.6737747192383,219.6737747192383,219.6737747192383,219.6737747192383,219.6737747192383,219.6737747192383,219.6737747192383,219.6737747192383,219.6737747192383,219.6737747192383,234.9325637817383,234.9325637817383,234.9325637817383,234.9325637817383,234.9325637817383,234.9325637817383,234.9325637817383,234.9325637817383,234.9325637817383,234.9325637817383,234.9325637817383,234.9325637817383,234.9325637817383,234.9325637817383,234.9325637817383,234.9325637817383,242.5963287353516,242.5963287353516,242.5963287353516,242.5963287353516,242.5963287353516,242.5963287353516,242.5963287353516,242.5963287353516,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961,257.9571762084961],"meminc":[0,0,0,0,15.28223419189453,0,0,0,-15.28857421875,0,0,45.75431823730469,0,0,0,0,0,0,0,4.57763671875e-05,0,0,0,0,0,0,0,0,0,0,0,0,0,-0.00030517578125,0,15.37259674072266,0,0.2490081787109375,0.27349853515625,0,0.2970809936523438,0,0.290069580078125,0,0.2804183959960938,0,0.326568603515625,0,0,0.360321044921875,0.3756637573242188,0,0.3663558959960938,0,0,0.1305999755859375,0,-2.662521362304688,0,0,0.3618698120117188,0.3642807006835938,0,0.4059906005859375,0,0.3599777221679688,0.3819351196289062,0,0.2370681762695312,0.3349380493164062,0.2808761596679688,0,-2.714500427246094,0.2552337646484375,0.3368682861328125,0,0.2433853149414062,0,0.202880859375,0.2316207885742188,0.2490005493164062,0.30755615234375,0,0.2209091186523438,0.2603073120117188,0.207061767578125,0.2382888793945312,0.04317474365234375,0,-2.71197509765625,0.1734771728515625,0,0.2181167602539062,0,0.2634048461914062,0,0.1937332153320312,0,0,0.24395751953125,0,0.3587799072265625,0,0.3204193115234375,0.2998886108398438,0.33453369140625,0.3105392456054688,0,0.07562255859375,0,0,-2.558700561523438,0.2790069580078125,0,0.3133468627929688,0,0.2995223999023438,0.323577880859375,0,0.325347900390625,0,0.3206024169921875,0,0.3353271484375,0,0.3367385864257812,0,0.1044082641601562,0,0,-2.531478881835938,0.3334884643554688,0,0.32415771484375,0,0.3412628173828125,0,0.3413467407226562,0,0.3449478149414062,0,0.3338623046875,0.3400344848632812,0.2503128051757812,0,-2.586326599121094,0,0.31549072265625,0,0.3295440673828125,0,0.3462142944335938,0,0.3375091552734375,0.3315963745117188,0,0.3455352783203125,0,0,0.3258895874023438,0.3250885009765625,0.0060577392578125,0,-2.415367126464844,0,0.3060073852539062,0,0.285186767578125,0,0.323028564453125,0,0.3383026123046875,0.3498992919921875,0,0.3420791625976562,0.31683349609375,0.2295379638671875,0,0,-2.503288269042969,0,0.3017501831054688,0,0.3290481567382812,0,0.2981033325195312,0,0.3211212158203125,0.3363876342773438,0,0.3201370239257812,0.3442840576171875,0.3211212158203125,0,0.0054931640625,0,-2.252189636230469,0,0.31610107421875,0,0.3445816040039062,0,0.3523635864257812,0,0,0.355621337890625,0.3619461059570312,0.369903564453125,0.2247161865234375,0,0,-2.383277893066406,0.32305908203125,0.3386154174804688,0,0,0.3528594970703125,0,0.3620452880859375,0,0,0.4067840576171875,0.37384033203125,0.2978744506835938,0,0,-2.401702880859375,0,0.3177566528320312,0,0.3302154541015625,0.3481674194335938,0,0,0.3549880981445312,0,0,0.3658599853515625,0,0.36309814453125,0,0.37811279296875,0,-2.415298461914062,0,0.30316162109375,0,0.32537841796875,0,0.3438873291015625,0,0.3521957397460938,0,0.3625640869140625,0,0.3647842407226562,0,0.3696136474609375,0.0774383544921875,0,-2.151351928710938,0.3186187744140625,0,0.3337326049804688,0,0.3524246215820312,0.353515625,0.3564071655273438,0,0.366729736328125,0,0.1382980346679688,0,0,0,-2.178352355957031,0.3159942626953125,0,0.2914505004882812,0,0.3437423706054688,0.3507766723632812,0,0.3585205078125,0,0.3636322021484375,0.2215728759765625,0,0,-2.178321838378906,0,0.29608154296875,0.3140411376953125,0,0.2602462768554688,0,0.2477645874023438,0,0.3451919555664062,0,0.3470916748046875,0,0.3614883422851562,0,0.07260894775390625,0,0,-2.056610107421875,0.296142578125,0,0.3170928955078125,0,0.3430557250976562,0,0.352508544921875,0,0.3599700927734375,0.3731689453125,0.07979583740234375,0,-2.057907104492188,0.197998046875,0,0.2770843505859375,0,0.3607254028320312,0,0.3346405029296875,0,0,0.3400726318359375,0,0.3218460083007812,0,0.2896652221679688,0,0,0,-1.9791259765625,0,0.2673187255859375,0.279510498046875,0,0.3251724243164062,0,0.313995361328125,0.2922897338867188,0.2878952026367188,0,0.2584609985351562,-2.149711608886719,0,0.19091796875,0,0.2430343627929688,0.2749710083007812,0,0.2278366088867188,0.3350906372070312,0,0.2688751220703125,0,0.289337158203125,0,0,0.3194122314453125,0.079803466796875,0,0,-1.996894836425781,0,0.207733154296875,0.252410888671875,0.3029937744140625,0,0,0.2569351196289062,0,0.3502655029296875,0.34234619140625,0,0.3415985107421875,0,0.00368499755859375,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2.028762817382812,0,0.2174224853515625,0,0.2278060913085938,0,0.2574386596679688,0.2943267822265625,0.3211669921875,0,0.3330535888671875,0,0.3422317504882812,0,0.09500885009765625,0,-1.918907165527344,0,0.2675933837890625,0,0.3033828735351562,0,0,0.333770751953125,0,0.3472976684570312,0.3584442138671875,0,0.3675003051757812,0,-2.021156311035156,0,0.2671432495117188,0.2791519165039062,0,0.3215103149414062,0.3473663330078125,0.3495635986328125,0,0.3625869750976562,0.1520767211914062,0,0,-1.867057800292969,0,0.272918701171875,0.3063735961914062,0.337738037109375,0,0.3393707275390625,0,0.3495330810546875,0,0.3183135986328125,0,-1.960357666015625,0,0.2598800659179688,0,0.2089920043945312,0,0.1737060546875,0,0.1808090209960938,0.2494735717773438,0,0.3511810302734375,0.3759307861328125,0.216644287109375,0,0,-1.839622497558594,0.31866455078125,0,0.3171310424804688,0,0.3440780639648438,0,0.3464431762695312,0.353179931640625,0,0.2155380249023438,0,-1.837921142578125,0,0.2612838745117188,0.2897567749023438,0,0.3240127563476562,0.3373336791992188,0,0.3249588012695312,0,0.3311538696289062,0,0,0.02390289306640625,0,-1.693290710449219,0,0.2544784545898438,0.2932815551757812,0.3267822265625,0,0.341827392578125,0,0.3499908447265625,0.180511474609375,0,0,-1.747329711914062,0,0.2577285766601562,0,0.290252685546875,0,0.3286666870117188,0,0.34381103515625,0.3512496948242188,0,0.2283477783203125,0,-1.751693725585938,0,0.2545089721679688,0.2835006713867188,0,0.3548126220703125,0,0.3430709838867188,0,0.350830078125,0.2168426513671875,0,0,0,-1.711578369140625,0,0.2588424682617188,0,0.2899093627929688,0,0.327392578125,0,0.3222885131835938,0.3386077880859375,0.2256088256835938,0,0,-1.726272583007812,0.2426986694335938,0,0.2679367065429688,0,0.3078536987304688,0.3400039672851562,0,0.3544769287109375,0,0.2634429931640625,0,-1.699790954589844,0.2478790283203125,0.2755126953125,0,0.3148269653320312,0,0.3395462036132812,0,0.347076416015625,0,0,0.22442626953125,0,0,-1.649803161621094,0,0.2467727661132812,0.3068618774414062,0,0.3227386474609375,0.347412109375,0,0.353271484375,0.1213531494140625,0,-1.550132751464844,0.2598190307617188,0,0.2919998168945312,0,0,0.3288497924804688,0,0,0.349761962890625,0.3508834838867188,0,0.0165863037109375,0,-1.452507019042969,0,0,0.2648086547851562,0,0.3058242797851562,0,0.3370742797851562,0,0.3509674072265625,0,0.240936279296875,0,0,-1.578887939453125,0,0.2527008056640625,0,0.2809066772460938,0,0,0.3230514526367188,0,0.3340377807617188,0.3480758666992188,0,0.08644866943359375,0,-1.480110168457031,0,0.2631988525390625,0,0.2914810180664062,0,0.3221817016601562,0,0.3388671875,0,0.3098602294921875,0,0,-1.564338684082031,0,0.246368408203125,0,0.2806625366210938,0.3171844482421875,0.3447265625,0.3575592041015625,0,0,0.0626678466796875,0,0,-1.382339477539062,0,0.272735595703125,0,0.3101806640625,0,0.3417205810546875,0.353515625,0,0.1482925415039062,0,0,-1.417762756347656,0,0.2586898803710938,0,0,0.2961654663085938,0.3327713012695312,0,0.350250244140625,0,0.2232131958007812,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.493293762207031,0,0,0,0.1919631958007812,0,0.2508621215820312,0.2842864990234375,0,0.3126983642578125,0,0.3022308349609375,0.3144454956054688,0,0.3449859619140625,0.38214111328125,0,0.3910064697265625,0.3734893798828125,0.3260650634765625,0,0.32452392578125,0.3270721435546875,0,0.3244171142578125,0,0.3255157470703125,0,0,0.0615692138671875,0,-4.456466674804688,0,0.319061279296875,0.3424606323242188,0,0.3248062133789062,0,0.3261032104492188,0,0.3591461181640625,0,0.36749267578125,0,0.3788604736328125,0.3882598876953125,0,0.3938446044921875,0.3893203735351562,0,0.3633956909179688,0,0.3739547729492188,0,0.261993408203125,0,0,0,0,0,-4.293060302734375,0.2996597290039062,0,0.3191757202148438,0,0.2970809936523438,0.3472671508789062,0.3523941040039062,0,0.3607406616210938,0,0.3713836669921875,0.3842849731445312,0.3833999633789062,0,0.3900985717773438,0.3915939331054688,0.384521484375,0,0.1416778564453125,0,-4.380874633789062,0,0.2884597778320312,0,0.3108062744140625,0,0.3023300170898438,0,0.3265914916992188,0,0.3334274291992188,0.3542327880859375,0,0.3611221313476562,0,0.3670806884765625,0.3736038208007812,0,0.3662490844726562,0,0.3669357299804688,0,0.3821258544921875,0,0.3706741333007812,0.00527191162109375,0,-4.271987915039062,0.2937469482421875,0.30389404296875,0,0.298095703125,0,0.3430557250976562,0.3486709594726562,0.3588485717773438,0,0.3666305541992188,0,0.37054443359375,0,0.3813095092773438,0.3836288452148438,0,0,0.3925247192382812,0,0,0.3901214599609375,0,0.1670074462890625,0,0,-4.292503356933594,0,0,0.2777862548828125,0,0.295074462890625,0.2897720336914062,0,0.3434219360351562,0,0.3816299438476562,0.3570938110351562,0,0.3662185668945312,0.3742904663085938,0,0.3844680786132812,0,0.3844680786132812,0.388519287109375,0,0.388153076171875,0,0.185516357421875,0,0,-4.238235473632812,0.2763748168945312,0.28778076171875,0,0.2902374267578125,0.3426361083984375,0,0.3458099365234375,0.3549270629882812,0,0.3610687255859375,0,0.3702545166015625,0.3697967529296875,0.3705520629882812,0,0.3873291015625,0.3761978149414062,0,0.2272491455078125,0,0,0,0,0,-3.947959899902344,0,0.2784957885742188,0,0.286163330078125,0,0.3377761840820312,0.3448104858398438,0.3443222045898438,0,0,0.3539657592773438,0.3651199340820312,0,0,0.37060546875,0,0,0.3858642578125,0,0.3846969604492188,0.3879241943359375,0,0.2281951904296875,0,-4.110298156738281,0.2707138061523438,0,0,0.271209716796875,0.2966079711914062,0,0.3413162231445312,0,0.3448638916015625,0.3451004028320312,0,0.3509445190429688,0,0.3660659790039062,0,0,0.376617431640625,0.3840713500976562,0,0,0.388671875,0,0.3801040649414062,0,0.1121063232421875,0,0,-3.997512817382812,0,0.2667236328125,0.263458251953125,0,0.3173141479492188,0.340423583984375,0.3458099365234375,0.3499603271484375,0.3578414916992188,0,0.3730850219726562,0,0.3797683715820312,0,0.385833740234375,0,0,0.3857421875,0.3476409912109375,0,0,0,-3.831916809082031,0,0.2628097534179688,0.2760238647460938,0,0.2886123657226562,0.3259201049804688,0,0.3341140747070312,0,0.3342819213867188,0,0,0.3433990478515625,0,0.3911209106445312,0.3585205078125,0,0,0.3369140625,0,0.3519821166992188,0.3425445556640625,0,0,0,0,0,-3.816871643066406,0,0.2535552978515625,0,0.2709884643554688,0.3193511962890625,0,0.3324966430664062,0,0,0.3409271240234375,0.249542236328125,0,0.3202667236328125,0,0,0.353912353515625,0,0.3658523559570312,0.3726577758789062,0.3722381591796875,0.3731307983398438,0.00434112548828125,0,0,-3.745292663574219,0,0.2504043579101562,0.2754974365234375,0,0.3148040771484375,0,0.3346328735351562,0,0.3357315063476562,0,0.3433609008789062,0.39764404296875,0,0.3669281005859375,0,0,0.3800735473632812,0,0.373748779296875,0,0.3775711059570312,0.10552978515625,0,0,-3.752471923828125,0,0,0.2489776611328125,0,0.2665023803710938,0.3078536987304688,0,0,0.3304672241210938,0.3403549194335938,0.3511276245117188,0.3614959716796875,0,0.3756256103515625,0.3806610107421875,0,0.38641357421875,0,0.382049560546875,0,0.1297988891601562,0,-3.698532104492188,0.2544403076171875,0.27490234375,0,0.3116455078125,0.329559326171875,0,0.3416366577148438,0,0.3513641357421875,0,0.3625411987304688,0,0.373870849609375,0,0.3801498413085938,0.38720703125,0,0.3781509399414062,0.0600738525390625,0,0,-3.572830200195312,0,0.2454757690429688,0.2837448120117188,0,0.3077850341796875,0,0.329193115234375,0.3413238525390625,0,0.3538055419921875,0.363189697265625,0,0.376617431640625,0.38018798828125,0.3859481811523438,0.310943603515625,0,0,0,-3.466781616210938,0,0.2478256225585938,0.2781906127929688,0.3036880493164062,0.327392578125,0,0,0.3397140502929688,0,0.3455123901367188,0,0.3595504760742188,0,0.37164306640625,0.330810546875,0,0,0.2601470947265625,0.3662872314453125,0,0.03968048095703125,0,0,-3.488731384277344,0,0.243896484375,0,0.2730331420898438,0,0.29443359375,0,0.3218917846679688,0.3714370727539062,0,0.3430328369140625,0.3633041381835938,0.3691329956054688,0.3813247680664062,0,0.3653945922851562,0.2638626098632812,0,0,0,0,0,-3.334968566894531,0,0.253875732421875,0,0.27130126953125,0,0.2865219116210938,0.3230514526367188,0,0.3272781372070312,0,0.3387222290039062,0.345794677734375,0.36309814453125,0,0,0.3651504516601562,0,0,0.3672714233398438,0,0.1931915283203125,0,0,0,0,0,-3.246185302734375,0,0.2579498291015625,0,0,0.2746200561523438,0,0.2851943969726562,0.3198471069335938,0,0,0.3280029296875,0,0.3693313598632812,0,0.3397750854492188,0.3605880737304688,0,0.3741378784179688,0.3735275268554688,0,0.06194305419921875,0,0,-3.340667724609375,0,0.2358856201171875,0,0.2573699951171875,0,0.2827987670898438,0.3113861083984375,0,0,0.3367156982421875,0,0.3406524658203125,0.3558120727539062,0,0.3734130859375,0,0.3791885375976562,0,0.384185791015625,0.1803436279296875,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-3.256721496582031,0.1913375854492188,0.2177581787109375,0,0.2296524047851562,0,0.2533798217773438,0,0.291473388671875,0,0.31549072265625,0.33013916015625,0,0.3426666259765625,0,0,0.3520431518554688,0.3723068237304688,0,0.3757476806640625,0.0800933837890625,0,-3.234573364257812,0,0.237640380859375,0,0.2540969848632812,0.2808837890625,0,0.3136215209960938,0,0.3384323120117188,0,0.3411941528320312,0,0.3525390625,0.3689498901367188,0.3783645629882812,0,0.374969482421875,0,0.08791351318359375,0,0,-3.188262939453125,0.2347869873046875,0.25244140625,0,0.30908203125,0,0.3154525756835938,0,0.3370742797851562,0.3381576538085938,0,0.3525848388671875,0,0.37091064453125,0,0.3804244995117188,0,0.3751602172851562,0,0.01474761962890625,0,0,-3.1038818359375,0.2373275756835938,0,0,0.2512664794921875,0,0.2839202880859375,0,0.317138671875,0.3403549194335938,0,0.3454055786132812,0.3574447631835938,0,0.372467041015625,0,0.3807830810546875,0,0.3087921142578125,0,0,0,-3.003562927246094,0,0,0.2386245727539062,0.257965087890625,0,0.2893447875976562,0.325347900390625,0,0.3407821655273438,0,0,0.3425216674804688,0,0.35113525390625,0,0,0.3678436279296875,0.3800125122070312,0.1995391845703125,0,0,0,0,0,-2.857933044433594,0,0.2419357299804688,0.2706985473632812,0.3052597045898438,0.3320159912109375,0,0.3400802612304688,0,0,0.3547439575195312,0.3673171997070312,0.38067626953125,0,0.3533554077148438,0,0,0,0,0,-2.926277160644531,0,0.2433853149414062,0,0.256195068359375,0,0.2903976440429688,0.3199234008789062,0,0,0.3411178588867188,0,0.34503173828125,0.3610610961914062,0.3744659423828125,0.3760986328125,0,0.105255126953125,0,0,-2.962760925292969,0,0.228118896484375,0,0.2416763305664062,0,0.2695541381835938,0.3042221069335938,0,0.3056640625,0,0.3351593017578125,0.3406219482421875,0,0.3507537841796875,0.3998031616210938,0.2724685668945312,0,0,0,0,0,-2.800827026367188,0,0.234283447265625,0,0.251251220703125,0,0.28179931640625,0,0,0.315704345703125,0,0.33709716796875,0,0.339508056640625,0,0.3479766845703125,0,0,0.3671112060546875,0,0,0.37109375,0,0.0389556884765625,0,-2.825767517089844,0,0.2260513305664062,0,0.2454071044921875,0.2778244018554688,0,0.3101119995117188,0,0.3267059326171875,0,0.3369216918945312,0,0.3435592651367188,0.3609542846679688,0,0.3717193603515625,0,0.108978271484375,0,-2.82183837890625,0,0.248138427734375,0,0.2445144653320312,0.2755813598632812,0.3114700317382812,0,0.336212158203125,0,0.3415298461914062,0,0.3521499633789062,0,0,0.3707809448242188,0,0.37591552734375,0.04683685302734375,0,0,-2.741600036621094,0,0.2281875610351562,0.2465438842773438,0.2784500122070312,0,0.3157119750976562,0.3372650146484375,0.3463363647460938,0,0.3523635864257812,0,0,0.3687744140625,0.347869873046875,0,0,0,0,0,-2.65533447265625,0,0.2339248657226562,0,0.2558059692382812,0,0.287811279296875,0,0.324249267578125,0,0.34393310546875,0,0.3441238403320312,0,0.3649444580078125,0.3750457763671875,0,0,0.2040786743164062,0,0,0,0,0,-2.509468078613281,0,0.2370529174804688,0,0.2660903930664062,0.3060302734375,0.3354415893554688,0,0.316925048828125,0,0.343109130859375,0.3614120483398438,0,0.3686752319335938,0.05211639404296875,0,0,-2.636878967285156,0,0,0.223602294921875,0.2429656982421875,0,0.269073486328125,0.3137435913085938,0,0.3316497802734375,0,0.341064453125,0,0.356781005859375,0,0.3591079711914062,0.2749099731445312,0,0,0,0,0,-2.499107360839844,0,0.2265701293945312,0,0.2503890991210938,0,0.2872161865234375,0.3213424682617188,0,0.3798828125,0,0.349945068359375,0.36480712890625,0,0.3700714111328125,0,0.02382659912109375,0,0,-2.514411926269531,0.2256851196289062,0,0.2458877563476562,0.2797088623046875,0.31756591796875,0,0.3388900756835938,0.345794677734375,0,0.3637924194335938,0,0.3720245361328125,0,0.098663330078125,0,-2.526191711425781,0,0,0.2239456176757812,0,0.238250732421875,0,0.2735519409179688,0,0.3100814819335938,0,0.3367233276367188,0,0.3452301025390625,0,0.3612747192382812,0,0.3666000366210938,0.1430130004882812,0,0,0,-2.303016662597656,0.281005859375,0.2923126220703125,0,0.3297500610351562,0.3468017578125,0.3279266357421875,0.34735107421875,0.3555145263671875,0,0.0937042236328125,0,0,0,0,0,-2.24090576171875,0,0.2386016845703125,0,0.2679519653320312,0,0.3074874877929688,0.333404541015625,0.3454971313476562,0,0.3588104248046875,0,0.3700637817382812,0,0.08916473388671875,0,0,-2.407966613769531,0,0,0.2245864868164062,0.236541748046875,0.2692413330078125,0,0.3101272583007812,0.3375091552734375,0,0.347320556640625,0.3570938110351562,0.39459228515625,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2.35565185546875,0,0,0.1951217651367188,0,0.2182693481445312,0,0.2351760864257812,0,0,0.2686843872070312,0.3039016723632812,0,0.3235321044921875,0,0.329437255859375,0,0.2974853515625,0.2308197021484375,0,0.0208892822265625,0,0,0,0,0,-2.32281494140625,0,0.1754989624023438,0,0.29620361328125,0,0.2658233642578125,0,0.2755126953125,0,0.3328170776367188,0.3378524780273438,0,0.3535690307617188,0.3523712158203125,0,0,0,0,0,-2.244491577148438,0,0.22344970703125,0.2436676025390625,0,0.2726898193359375,0,0.3163986206054688,0,0.3716659545898438,0,0,0.3430328369140625,0,0.3311386108398438,0,0.2081680297851562,0,0,0,-2.117576599121094,0,0.2269058227539062,0,0.2520370483398438,0,0.29345703125,0.3280487060546875,0,0.3462371826171875,0,0.3491363525390625,0,0.3677978515625,0,0.01866912841796875,0,-2.188056945800781,0.2261428833007812,0,0.2417984008789062,0,0.280975341796875,0,0.3179397583007812,0,0.3441162109375,0,0.3493804931640625,0,0.3677520751953125,0,0.1236038208007812,0,0,0,-1.961647033691406,0,0.2405624389648438,0,0.2765655517578125,0,0.3134231567382812,0,0.3402633666992188,0,0.3472366333007812,0,0,0.3579635620117188,0,0.1482772827148438,0,0,0,0,0,-1.977088928222656,0,0.235107421875,0,0.2691802978515625,0,0.3111190795898438,0.3403167724609375,0.347900390625,0.3586883544921875,0,0.1763534545898438,0,0,0,0,0,-1.952957153320312,0,0.2288360595703125,0,0.2623443603515625,0,0.3053741455078125,0.3353347778320312,0.3478012084960938,0.3559646606445312,0,0.177947998046875,0,0,0,0,0,-1.901657104492188,0,0.235321044921875,0,0.2661666870117188,0,0.3069076538085938,0,0.3365020751953125,0.3461151123046875,0,0,0.3556594848632812,0.1146011352539062,0,0,0,0,0,-1.850196838378906,0,0,0.230377197265625,0,0.247955322265625,0,0.2888259887695312,0,0.3244400024414062,0.3399276733398438,0,0.344970703125,0,0.1323623657226562,0,0,0,-1.842384338378906,0.232452392578125,0,0.2660980224609375,0.3075408935546875,0,0,0.369903564453125,0,0.3483657836914062,0.3591766357421875,0,0.01663970947265625,0,0,-1.956573486328125,0.224334716796875,0,0.243377685546875,0,0.2818603515625,0,0.314453125,0.33807373046875,0.346588134765625,0,0,0.264617919921875,0,0,0,0,0,-1.856781005859375,0,0.2247695922851562,0,0.2479476928710938,0,0.2867507934570312,0,0,0.3219757080078125,0.3432464599609375,0,0.3323593139648438,0,0.1556396484375,0,0,0,0,0,-1.753105163574219,0.2322769165039062,0.26544189453125,0.302978515625,0,0.3343505859375,0.3433914184570312,0,0.3296661376953125,0,0,0,-1.852706909179688,0.2210693359375,0,0.237945556640625,0,0.2753219604492188,0,0.3140640258789062,0.3401336669921875,0,0.3465042114257812,0,0.1716842651367188,0,0,0,0,0,0,0,0,0,0,0,-1.754600524902344,0.2080078125,0.2291107177734375,0,0.2560501098632812,0,0,0.2947616577148438,0,0.323089599609375,0,0.3737945556640625,0.12298583984375,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.831619262695312,0,0,0,0,0,0.24072265625,0,0.2562179565429688,0,0.2903900146484375,0,0.322357177734375,0,0.3249588012695312,0.2909393310546875,0,0.3323516845703125,0,0.3254547119140625,0.3721389770507812,0.3893051147460938,0.3880996704101562,0.3734664916992188,0,0.3265762329101562,0,0.3262100219726562,0,0.326568603515625,0,0,0.3277206420898438,0.3283843994140625,0,0,0.3255538940429688,0.3242111206054688,0,0.3250198364257812,0,0.3257064819335938,0,0.3277435302734375,0,0.3252105712890625,0.1173248291015625,0,0,0,0,0,-7.164810180664062,0.2587661743164062,0,0.2948074340820312,0,0.3263778686523438,0,0.3218460083007812,0,0,0.3000259399414062,0,0.3827133178710938,0.358673095703125,0,0.3765869140625,0,0.3818206787109375,0,0.391693115234375,0,0.3927001953125,0,0.39715576171875,0.3981094360351562,0,0.3962249755859375,0,0.3969192504882812,0,0.3981552124023438,0,0.3976821899414062,0.39495849609375,0,0,0.3884735107421875,0,0.38250732421875,0.03675079345703125,0,0,0,0,0,-7.003799438476562,0,0,0.26055908203125,0.291290283203125,0.3167495727539062,0,0.3030471801757812,0,0.3188247680664062,0.348846435546875,0,0.355743408203125,0,0.374603271484375,0,0.3771514892578125,0.3851165771484375,0,0.385345458984375,0,0.390594482421875,0,0.3938369750976562,0.3927154541015625,0.3931732177734375,0,0.3929595947265625,0.4300384521484375,0,0.395751953125,0,0.3249282836914062,0,0.2958984375,0,0.08155059814453125,0,0,0,0,0,-6.908348083496094,0.258575439453125,0,0.2872543334960938,0,0.3060531616210938,0,0,0.2922134399414062,0.3335800170898438,0.3486251831054688,0,0.3543014526367188,0,0,0.3723220825195312,0,0.3809585571289062,0,0.391693115234375,0,0.3885421752929688,0.3893814086914062,0,0.396636962890625,0.3989028930664062,0,0.3978195190429688,0,0.39642333984375,0,0.398712158203125,0.3994903564453125,0.3848190307617188,0,0.2335739135742188,0,0,0,0,0,-6.924507141113281,0,0.2230987548828125,0,0.2645492553710938,0,0.2858505249023438,0,0.31585693359375,0,0.3156814575195312,0.3429489135742188,0.349884033203125,0,0.3551788330078125,0.3743972778320312,0,0.3808059692382812,0,0.387969970703125,0,0.384521484375,0.3802108764648438,0,0,0.3883743286132812,0.3837432861328125,0,0.3854904174804688,0,0.3872756958007812,0,0.3876800537109375,0,0.3919448852539062,0,0.3741378784179688,0,0.06316375732421875,0,0,0,0,0,-6.708816528320312,0,0,0.2437210083007812,0,0.2595138549804688,0,0.2707595825195312,0,0.2820053100585938,0,0.3318252563476562,0,0.3381423950195312,0,0.341766357421875,0.36212158203125,0.3711318969726562,0.37774658203125,0,0.3850326538085938,0,0.3813247680664062,0.3823394775390625,0,0.3823318481445312,0,0.42205810546875,0,0.3905563354492188,0,0.3961181640625,0.3959808349609375,0,0.3809280395507812,0.2085189819335938,0,0,0,0,0,-6.704147338867188,0.2179641723632812,0.2566299438476562,0,0.265869140625,0,0.2679977416992188,0.325439453125,0.3380050659179688,0,0.34075927734375,0,0.3502273559570312,0,0.3658676147460938,0,0.3747024536132812,0,0.3756332397460938,0.381683349609375,0,0,0.3820266723632812,0,0,0.3818511962890625,0,0.3842620849609375,0,0,0.3848724365234375,0.3893203735351562,0,0.3841171264648438,0,0.3748016357421875,0,0.3540573120117188,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-6.512672424316406,0,0,0.226470947265625,0.236480712890625,0.2354888916015625,0.26580810546875,0,0.3124923706054688,0,0.3267364501953125,0,0.3360519409179688,0,0.3432846069335938,0.361236572265625,0,0.3693771362304688,0.37225341796875,0.375274658203125,0,0.3733062744140625,0.380218505859375,0,0.38555908203125,0.3861541748046875,0,0.3897323608398438,0.3962783813476562,0,0.3821334838867188,0,0.2470932006835938,0,0,0,0,0,0,0,0,-6.285255432128906,0,0.2430191040039062,0,0.2481155395507812,0,0.2742538452148438,0,0,0.317779541015625,0,0.3665695190429688,0,0.3420028686523438,0,0.3460922241210938,0,0.3575973510742188,0,0.3670730590820312,0,0.3725357055664062,0,0.3750381469726562,0.3816604614257812,0.3840484619140625,0,0.3838043212890625,0,0.3895187377929688,0,0.394012451171875,0.3963546752929688,0,0,0.379486083984375,0.1521835327148438,0,0,0,0,0,-6.359245300292969,0.2396697998046875,0,0.2397232055664062,0,0.2416610717773438,0.2966384887695312,0,0.3253707885742188,0,0.3346405029296875,0,0.3360366821289062,0,0.334625244140625,0,0.35174560546875,0.358367919921875,0,0.3663482666015625,0.3741607666015625,0.3813323974609375,0,0,0.3841323852539062,0,0.3851470947265625,0,0.3904342651367188,0,0.3953323364257812,0.3928909301757812,0.3796234130859375,0.034149169921875,0,0,0,0,0,-6.165740966796875,0.2388229370117188,0.235321044921875,0,0.2718734741210938,0.3086624145507812,0.3312301635742188,0.3362274169921875,0,0.3365631103515625,0,0.3489608764648438,0.3615264892578125,0,0.369171142578125,0.372589111328125,0,7.766677856445312,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7.62939453125,7.62939453125e-06,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,15.2587890625,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7.663764953613281,0,0,0,0,0,0,0,15.36084747314453,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"filename":["<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,null,null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,null,null,null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,null,"<expr>","<expr>","<expr>",null,null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>","<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,null,null,"<expr>",null,null,null,null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,null,"<expr>",null,null,null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,null,null,null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,null,null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,null,null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,null,null,null,null,null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,null,null,"<expr>","<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null]},"interval":10,"files":[{"filename":"<expr>","content":"## Generate Large Random Dataset\nn <- 2e6\nx <- runif(n)\ny <- runif(n)\nz <- runif(n)\nXYZ <- cbind(x,y,z)\n\n## Inspect 4 equivalent `row mean` calculations \nprofvis::profvis({\n    m <- rowSums(XYZ)/ncol(XYZ)\n    m <- rowMeans(XYZ)\n    m <- apply(XYZ, 1, mean)\n    m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }\n})\n## rowSums(), colSums(), rowMeans(), and colMeans() are vectorised and fast.\n## for loop is not the slowest, but the ugliest.","normpath":"<expr>"}],"prof_output":"/tmp/Rtmpr0YqlL/file446bd925ff2.prof","highlight":{"output":["^output\\$"],"gc":["^<GC>$"],"stacktrace":["^\\.\\.stacktraceo(n|ff)\\.\\.$"]},"split":"h"}},"evals":[],"jsHooks":[]}</script>
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
##  mean1(x, 0.5) 20.18414 20.27268 20.60300 20.31455 20.38010 27.38109   100  a 
##  mean2(x, 0.5) 19.16268 19.31872 19.48517 19.35983 19.39755 22.06399   100   b
##  mean3(x, 0.5) 20.18493 20.25795 20.45853 20.28347 20.33923 23.28834   100  a
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
##  ma1(y) 169.29284 173.06891 177.60068 176.88931 179.26024 213.9525   100  a 
##  ma2(y)  18.79067  21.28152  26.43793  23.07705  24.94602 178.0120   100   b
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
##   0.104   0.000   0.035
```

```r
system.time({ lm(Y~X, data=DAT) })
```

```
##    user  system elapsed 
##   0.427   0.022   0.172
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
##   0.024   0.003   0.027
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
##   0.916   0.186   0.629
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

