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
<div class="plotly html-widget html-fill-item" id="htmlwidget-c5a3d67dd56214461da8" style="width:672px;height:480px;"></div>
<script type="application/json" data-for="htmlwidget-c5a3d67dd56214461da8">{"x":{"visdat":{"5d4d3989c8ce":["function () ","plotlyVisDat"]},"cur_data":"5d4d3989c8ce","attrs":{"5d4d3989c8ce":{"x":{},"y":{},"alpha_stroke":1,"sizes":[10,100],"spans":[1,20]}},"layout":{"margin":{"b":40,"l":60,"t":25,"r":10},"xaxis":{"domain":[0,1],"automargin":true,"title":"X"},"yaxis":{"domain":[0,1],"automargin":true,"title":"Y"},"hovermode":"closest","showlegend":false},"source":"A","config":{"modeBarButtonsToAdd":["hoverclosest","hovercompare"],"showSendToCloud":false},"data":[{"x":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100],"y":[4.0505718822189314,9.6439664842201314,8.8896128083356718,13.117946383274312,18.414302735171642,21.665262300825191,32.422706378784127,33.72607134335874,32.46644417809771,43.649052113285833,39.725533881497192,49.119551481607651,50.398934630070208,54.180786767581942,60.763515986139303,62.198615575900661,64.840727568040393,71.934614734219664,70.083436471439384,81.285685733744941,84.577332349099336,88.548586829879355,93.123668694108147,92.236454571312066,101.94602312849636,104.43781322641097,103.54448230477222,111.85415976493303,114.19686624651821,119.93958297808744,121.29698964911464,126.98794078960029,127.8712122036673,133.08745999052621,138.89830455076887,144.57065950830886,148.50872038076602,152.03066475024858,155.36928382332312,157.59994435196447,164.61708636275367,165.76576197375337,170.9958727474918,175.11403997441403,184.81580374064964,186.69301286440816,189.38082058803477,191.07156765316444,192.39820206843299,199.37401151636956,206.51051225190116,209.37528245280052,212.98124385444584,218.43493495293114,221.09576226888262,224.90194728430777,225.51636307051413,231.91602348860499,235.37333897970856,240.57324665844166,242.55493556720327,248.9677352768278,253.00833215873075,256.58802493641321,263.79647811484784,264.86357180366178,270.50475578265275,271.73799005214642,274.07731013489291,284.76098893126999,284.71178690787065,287.33239333479912,290.80304783697613,296.38940191792381,301.82768754405203,303.36519057732414,306.66389558960486,312.38728531426807,314.12178458129739,317.86393866771988,327.83579371674756,327.63986779396032,331.04712236204892,334.84346024963799,340.02509520941629,341.91855476991748,348.95768198988185,351.1119103729651,357.28390561432406,362.11292225496749,364.4245495750734,368.12659674404114,373.20910345423721,379.2239096186521,381.08684517425917,382.79077179759878,384.75126806565618,393.83738073480862,398.18095924141812,400.01867132517464],"type":"scatter","mode":"markers","marker":{"color":"rgba(31,119,180,1)","line":{"color":"rgba(31,119,180,1)"}},"error_y":{"color":"rgba(31,119,180,1)"},"error_x":{"color":"rgba(31,119,180,1)"},"line":{"color":"rgba(31,119,180,1)"},"xaxis":"x","yaxis":"y","frame":null}],"highlight":{"on":"plotly_click","persistent":false,"dynamic":false,"selectize":false,"opacityDim":0.20000000000000001,"selected":{"opacity":1},"debounce":0},"shinyEvents":["plotly_hover","plotly_click","plotly_selected","plotly_relayout","plotly_brushed","plotly_brushing","plotly_clickannotation","plotly_doubleclick","plotly_deselect","plotly_afterplot","plotly_sunburstclick"],"base_url":"https://plot.ly"},"evals":[],"jsHooks":[]}</script>
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
* then try `apply` functions

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
<div class="profvis html-widget html-fill-item" id="htmlwidget-8d39f69f72b9ab08dd11" style="width:100%;height:600px;"></div>
<script type="application/json" data-for="htmlwidget-8d39f69f72b9ab08dd11">{"x":{"message":{"prof":{"time":[1,2,3,4,5,6,7,8,9,9,9,10,10,11,11,12,12,13,13,14,14,15,15,16,16,17,17,18,18,19,19,20,20,21,21,22,22,23,24,24,25,25,26,27,28,29,29,30,30,31,31,32,32,33,33,34,35,36,36,37,38,38,39,39,39,40,40,41,42,43,44,45,45,45,46,46,46,47,47,48,48,49,49,50,51,52,52,53,54,55,55,55,56,57,58,59,60,61,62,62,62,63,63,63,64,64,65,65,66,66,67,67,68,68,69,69,70,71,71,72,73,73,74,74,75,76,76,77,77,78,78,79,79,80,80,80,81,82,82,83,84,85,86,87,87,88,89,89,90,90,91,91,91,92,93,93,94,94,94,95,95,95,96,97,98,99,99,100,100,100,101,102,103,103,104,104,104,105,105,105,106,106,107,107,108,109,109,110,111,111,112,112,113,113,114,114,115,115,116,117,118,118,119,119,120,121,122,122,123,124,125,126,127,127,127,128,128,129,129,130,130,131,132,132,133,133,134,134,134,135,135,135,136,136,137,137,138,138,139,139,139,140,141,141,142,142,143,143,144,144,145,145,146,146,147,147,148,148,149,150,150,150,151,151,152,152,153,153,154,155,156,156,157,157,158,158,159,159,159,160,161,162,162,163,164,164,164,165,165,166,167,167,168,169,170,171,171,172,172,172,173,173,174,174,175,176,176,177,177,178,178,179,179,179,180,180,180,181,181,181,182,182,182,183,183,183,184,184,184,185,185,185,186,186,187,187,188,188,189,189,189,190,190,191,192,192,193,194,194,194,195,195,196,196,197,198,199,199,200,201,201,201,202,203,204,205,205,206,206,207,208,209,209,209,210,210,211,212,212,213,213,213,214,215,216,216,217,217,218,218,219,220,220,221,221,222,222,222,223,223,224,225,225,226,226,227,227,228,228,228,229,229,229,230,230,231,231,232,232,232,233,233,234,234,235,235,236,236,237,237,238,238,239,239,240,241,241,242,242,243,243,244,244,245,246,246,247,247,248,249,250,250,250,251,251,252,252,253,254,254,255,255,256,256,256,257,257,258,259,259,260,260,260,261,261,262,262,263,263,263,264,265,265,266,267,267,268,268,269,269,269,270,270,271,272,272,273,274,274,275,275,276,276,276,277,277,278,278,279,279,280,280,281,281,282,282,282,283,283,284,284,285,285,286,286,287,288,288,288,289,289,290,290,290,291,292,292,293,293,293,294,294,294,295,295,296,297,297,298,298,299,300,300,300,301,301,302,302,303,303,304,304,305,305,306,306,306,307,308,308,309,309,310,310,311,311,312,312,313,313,313,314,314,314,315,315,316,316,317,317,318,319,319,319,320,321,321,322,322,323,324,324,325,325,325,326,326,326,327,327,327,328,328,328,329,329,329,330,330,330,331,331,331,332,332,332,333,333,333,334,334,334,335,335,335,336,336,336,337,337,337,338,338,338,339,339,339,340,340,340,341,341,341,342,342,342,343,343,343,344,344,344,345,345,345,346,346,346,347,347,347,348,348,348,349,349,350,350,351,351,352,353,353,353,354,355,355,356,356,357,358,358,359,360,360,361,361,362,362,363,363,364,365,365,366,367,368,368,368,369,369,370,370,371,372,373,374,374,375,375,376,376,376,377,377,378,378,379,379,380,381,381,381,382,383,384,384,385,385,386,386,387,387,388,388,389,389,389,390,390,390,391,391,392,393,393,394,394,395,396,396,397,397,397,398,399,399,400,401,401,402,403,403,404,404,405,405,406,406,407,408,408,409,409,410,410,411,411,412,412,413,413,414,414,415,415,416,416,416,417,417,418,418,419,419,420,420,421,422,423,424,424,425,426,426,427,427,428,428,429,429,430,430,431,431,432,432,433,434,434,434,435,435,435,436,436,437,438,438,439,440,440,441,442,442,442,443,443,444,444,445,445,445,446,446,447,448,448,449,449,449,450,450,451,452,453,453,454,454,455,455,456,456,457,457,458,459,459,459,460,460,461,462,462,463,463,464,465,465,465,466,466,467,467,467,468,468,468,469,470,470,471,471,472,472,473,473,474,474,474,475,475,476,477,477,478,479,480,480,481,482,482,483,484,484,485,486,486,487,488,488,489,489,490,490,491,491,492,492,492,493,493,493,494,494,495,495,496,497,497,497,498,498,499,500,501,501,502,502,503,504,504,505,505,505,506,506,507,508,508,509,510,510,511,511,512,512,513,514,515,515,516,516,517,517,518,519,520,520,521,521,522,522,523,523,524,524,525,525,526,526,527,527,528,528,529,529,529,530,530,530,531,531,531,532,532,533,533,534,534,535,535,536,536,537,537,538,539,540,540,541,541,542,542,543,544,545,545,546,547,547,547,548,548,549,549,550,550,551,552,552,553,553,554,554,555,555,556,556,557,557,557,558,558,559,559,560,561,561,562,562,563,563,564,564,565,565,566,566,566,567,567,568,568,568,569,570,570,571,572,572,573,574,574,575,576,576,576,577,577,577,578,578,579,579,580,581,581,582,583,583,584,585,586,586,587,588,588,588,589,589,589,590,590,591,592,593,594,594,595,595,595,596,596,597,597,598,599,599,600,600,600,601,602,602,603,604,605,605,606,607,607,608,608,608,609,609,610,610,611,611,611,612,612,612,613,613,613,614,614,614,615,615,615,616,616,616,617,617,617,618,618,618,619,619,619,620,620,620,621,621,621,622,622,622,623,623,623,624,625,625,625,626,626,627,627,628,629,629,630,630,631,632,632,633,633,634,634,634,635,635,635,635,636,636,637,637,638,638,638,639,639,640,640,641,641,642,642,643,643,644,644,645,645,646,646,647,647,648,648,649,650,650,650,651,652,652,653,654,654,655,655,656,657,657,658,658,659,660,660,661,661,662,662,663,663,663,664,664,665,665,666,666,666,667,667,668,668,668,669,669,669,670,670,671,671,672,672,673,673,674,675,675,676,676,677,677,677,678,678,679,679,680,680,681,681,682,682,683,684,685,686,686,687,687,688,688,689,689,690,690,690,691,691,691,692,692,693,694,694,695,695,696,697,697,698,698,699,700,700,700,701,701,701,702,702,702,703,703,704,704,705,706,706,707,707,708,709,709,710,711,712,712,712,712,713,713,714,714,715,715,716,716,717,717,717,718,719,720,720,721,722,722,722,723,723,723,724,724,725,725,726,726,727,727,728,729,729,730,731,731,732,732,733,733,734,734,735,735,736,736,737,737,737,738,738,739,739,740,740,741,741,742,742,742,743,743,744,745,745,746,746,747,748,749,750,751,751,752,752,753,753,753,754,754,754,755,756,756,757,758,758,759,759,760,761,762,762,763,763,764,764,765,765,766,766,767,767,768,769,769,770,770,770,771,772,772,773,773,773,774,774,774,775,776,776,777,778,778,779,779,780,781,781,782,782,783,783,784,785,785,786,786,787,788,789,789,790,791,792,792,792,793,793,793,794,794,795,795,796,797,797,798,799,800,800,801,801,802,802,802,802,803,803,803,803,804,804,805,806,807,807,808,808,809,809,810,811,811,812,812,813,814,814,815,815,815,816,817,817,818,818,819,820,820,821,821,821,822,822,822,823,824,824,825,826,826,827,827,828,829,829,830,830,831,831,832,832,833,833,834,834,835,835,836,837,838,838,839,839,839,840,840,840,841,841,841,842,842,842,843,843,843,844,844,844,845,845,845,846,846,846,847,847,847,848,848,848,849,849,849,850,850,851,852,853,853,854,854,855,856,857,857,858,858,858,859,859,859,860,860,860,861,862,863,863,864,865,866,866,867,867,867,868,868,868,869,869,870,870,871,872,872,872,873,874,875,875,876,876,877,877,878,878,879,880,880,881,882,883,883,884,884,885,885,885,886,886,886,887,887,888,888,889,890,890,891,892,892,893,893,893,894,894,895,895,896,897,897,898,898,898,899,899,899,900,901,901,901,902,902,903,903,904,904,905,905,905,906,906,907,908,909,909,910,910,911,911,911,912,912,913,913,914,914,915,915,916,917,917,917,918,919,919,920,920,920,921,921,921,922,922,923,924,925,926,926,927,928,929,929,929,930,930,931,932,932,933,933,934,934,935,936,936,937,937,937,938,938,938,939,939,940,940,941,942,943,943,944,945,945,945,946,946,946,947,947,948,948,949,950,950,951,951,952,953,953,953,954,954,954,955,955,955,956,956,957,957,958,958,959,960,961,961,962,962,963,963,964,964,965,965,966,966,967,967,968,969,969,970,970,970,971,971,971,972,972,973,974,974,974,975,975,976,976,977,977,978,978,978,979,979,979,980,980,980,981,981,981,982,982,982,983,983,983,984,985,985,986,986,987,987,987,988,989,989,990,990,991,991,991,992,992,992,993,993,993,994,994,994,995,995,995,996,996,996,997,997,997,998,998,998,999,999,999,1000,1000,1000,1001,1001,1001,1002,1002,1002,1003,1003,1003,1004,1004,1004,1005,1005,1005,1006,1006,1006,1007,1007,1007,1008,1008,1008,1009,1009,1009,1010,1010,1010,1011,1011,1011,1012,1012,1012,1013,1013,1013,1014,1014,1014,1015,1015,1015,1016,1016,1016,1017,1017,1017,1018,1018,1018,1019,1019,1019,1020,1020,1020,1021,1021,1021,1022,1022,1022,1023,1023,1023,1024,1024,1024,1025,1025,1025,1026,1026,1026,1027,1027,1027,1028,1028,1028,1029,1029,1029,1030,1030,1030,1031,1031,1031,1032,1032,1032,1033,1033,1033,1034,1034,1034,1035,1035,1035,1036,1036,1036,1037,1037,1037,1038,1038,1038,1039,1039,1039,1040,1040,1040,1041,1041,1042,1042,1043,1044,1044,1044,1045,1045,1045,1046,1047,1048,1048,1049,1049,1050,1050,1051,1051,1052,1052,1053,1053,1054,1055,1055,1056,1056,1057,1058,1058,1059,1059,1060,1061,1062,1063,1063,1063,1064,1064,1064,1065,1065,1066,1067,1067,1068,1068,1069,1069,1070,1071,1071,1072,1073,1073,1074,1075,1075,1076,1076,1077,1078,1078,1079,1080,1081,1081,1082,1082,1083,1083,1084,1084,1085,1085,1086,1086,1087,1087,1088,1088,1089,1089,1090,1090,1091,1092,1093,1094,1094,1094,1095,1096,1096,1097,1098,1098,1099,1100,1100,1101,1102,1102,1103,1103,1104,1105,1105,1106,1106,1107,1107,1108,1108,1109,1109,1110,1111,1111,1112,1112,1113,1113,1114,1114,1114,1115,1115,1116,1116,1117,1118,1118,1119,1119,1120,1121,1121,1122,1122,1123,1123,1124,1124,1125,1125,1126,1126,1127,1127,1127,1128,1128,1128,1129,1129,1129,1130,1131,1131,1131,1132,1132,1133,1134,1134,1135,1135,1136,1136,1137,1137,1137,1138,1139,1140,1140,1141,1141,1142,1142,1143,1144,1145,1145,1146,1146,1147,1147,1148,1148,1148,1149,1149,1149,1150,1150,1150,1151,1152,1152,1153,1154,1154,1155,1156,1157,1157,1158,1158,1159,1159,1160,1161,1161,1162,1162,1162,1163,1164,1165,1165,1166,1167,1167,1168,1168,1169,1169,1170,1170,1171,1171,1172,1172,1173,1173,1173,1174,1174,1175,1176,1176,1177,1178,1179,1180,1181,1181,1182,1183,1183,1184,1184,1185,1186,1186,1187,1188,1189,1189,1190,1190,1191,1191,1192,1192,1193,1193,1194,1194,1195,1195,1196,1196,1197,1197,1198,1198,1199,1199,1200,1201,1202,1202,1202,1203,1203,1204,1204,1205,1205,1206,1206,1207,1207,1208,1209,1209,1210,1210,1211,1212,1213,1213,1214,1214,1215,1215,1215,1216,1216,1217,1217,1218,1218,1219,1219,1220,1220,1221,1221,1222,1222,1222,1223,1223,1224,1225,1225,1226,1226,1227,1227,1228,1228,1229,1230,1230,1231,1232,1232,1233,1233,1234,1235,1235,1236,1236,1237,1237,1237,1238,1238,1238,1239,1239,1239,1240,1240,1241,1242,1243,1243,1244,1244,1245,1246,1247,1248,1248,1248,1249,1249,1250,1250,1251,1251,1252,1253,1253,1254,1254,1255,1256,1256,1257,1257,1257,1258,1258,1258,1259,1259,1259,1260,1260,1261,1261,1262,1263,1264,1265,1266,1266,1267,1268,1268,1268,1269,1270,1271,1271,1272,1272,1273,1273,1274,1275,1275,1276,1277,1277,1278,1278,1279,1279,1280,1281,1282,1282,1283,1284,1285,1285,1286,1287,1287,1288,1288,1289,1289,1290,1290,1291,1291,1292,1292,1293,1293,1294,1294,1295,1295,1296,1296,1297,1297,1298,1299,1299,1300,1300,1301,1301,1302,1302,1303,1303,1304,1304,1305,1305,1306,1306,1307,1307,1308,1308,1309,1309,1310,1310,1311,1311,1312,1312,1313,1313,1314,1314,1315,1315,1316,1316,1317,1317,1318,1318,1318,1318,1318,1318,1318,1318,1319,1319,1319,1319,1319,1319,1319,1319,1319,1319,1319,1319,1319,1319,1320,1320,1320,1320,1320,1320,1320,1320,1321,1321,1321,1321,1321,1321,1321,1321,1322,1322,1322,1322,1322,1322,1322,1322,1323,1323,1323,1323,1323,1323,1323,1323,1324,1324,1324,1324,1324,1324,1324,1324,1325,1325,1325,1325,1325,1325,1325,1325,1326,1326,1326,1326,1326,1326,1326,1326,1327,1327,1327,1327,1327,1327,1327,1327,1328,1328,1328,1328,1328,1328,1328,1328,1329,1329,1329,1329,1329,1329,1329,1329,1330,1330,1330,1330,1330,1330,1330,1330,1331,1331,1331,1331,1331,1331,1331,1331,1332,1332,1332,1332,1332,1332,1332,1332,1333,1333,1333,1333,1333,1333,1333,1333,1334,1334,1334,1334,1334,1334,1334,1334,1335,1335,1335,1335,1335,1335,1335,1335,1336,1336,1336,1336,1336,1336,1336,1336,1337,1337,1337,1337,1337,1337,1337,1337,1338,1338,1338,1338,1338,1338,1338,1338],"depth":[1,1,1,1,1,1,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,1,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,1,2,1,3,2,1,2,1,1,1,1,1,3,2,1,3,2,1,2,1,2,1,2,1,1,1,2,1,1,1,3,2,1,1,1,1,1,1,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,1,1,1,1,2,1,1,2,1,2,1,3,2,1,1,2,1,3,2,1,3,2,1,1,1,1,2,1,3,2,1,1,1,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,1,1,2,1,1,1,1,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,3,2,1,1,1,2,1,1,3,2,1,2,1,1,2,1,1,1,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,1,3,2,1,2,1,2,1,1,1,2,1,1,3,2,1,1,1,1,2,1,2,1,1,1,3,2,1,2,1,1,2,1,3,2,1,1,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,1,3,2,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,1,2,1,3,2,1,2,1,2,1,3,2,1,1,2,1,1,2,1,2,1,3,2,1,2,1,1,2,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,3,2,1,1,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,3,2,1,1,2,1,2,1,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,3,2,1,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,1,1,3,2,1,2,1,2,1,1,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,3,2,1,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,1,2,1,3,2,1,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,2,1,1,2,1,1,2,1,1,3,2,1,2,1,2,1,3,2,1,2,1,1,2,1,3,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,1,2,1,2,1,1,3,2,1,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,1,1,2,1,1,2,1,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,1,3,2,1,2,1,1,1,2,1,2,1,1,2,1,3,2,1,2,1,1,2,1,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,1,1,2,1,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,3,2,1,1,2,1,1,2,1,1,2,1,1,3,2,1,3,2,1,2,1,2,1,1,2,1,1,2,1,1,1,2,1,1,3,2,1,3,2,1,2,1,1,1,1,2,1,3,2,1,2,1,2,1,1,2,1,3,2,1,1,2,1,1,1,2,1,1,2,1,3,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,1,3,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,3,2,1,4,3,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,1,2,1,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,3,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,1,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,1,2,1,2,1,1,3,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,2,1,1,2,1,1,1,4,3,2,1,2,1,2,1,2,1,2,1,3,2,1,1,1,2,1,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,1,1,1,1,2,1,2,1,3,2,1,3,2,1,1,2,1,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,1,2,1,3,2,1,3,2,1,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,1,1,2,1,1,1,3,2,1,3,2,1,2,1,2,1,1,2,1,1,1,2,1,2,1,4,3,2,1,4,3,2,1,2,1,1,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,3,2,1,1,2,1,2,1,1,2,1,3,2,1,3,2,1,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,1,1,2,1,2,1,1,1,2,1,3,2,1,3,2,1,3,2,1,1,1,2,1,1,1,2,1,3,2,1,3,2,1,2,1,2,1,1,3,2,1,1,1,2,1,2,1,2,1,2,1,1,2,1,1,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,1,2,1,3,2,1,2,1,2,1,1,2,1,3,2,1,3,2,1,1,3,2,1,2,1,2,1,2,1,3,2,1,2,1,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,3,2,1,1,2,1,3,2,1,3,2,1,2,1,1,1,1,2,1,1,1,3,2,1,2,1,1,2,1,2,1,2,1,1,2,1,3,2,1,3,2,1,2,1,2,1,1,1,2,1,1,3,2,1,3,2,1,2,1,2,1,1,2,1,2,1,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,3,2,1,2,1,1,3,2,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,1,2,1,2,1,3,2,1,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,1,3,2,1,3,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,1,1,1,3,2,1,3,2,1,2,1,1,2,1,2,1,2,1,1,2,1,1,2,1,1,2,1,2,1,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,1,3,2,1,1,2,1,1,2,1,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,1,3,2,1,2,1,1,2,1,2,1,2,1,3,2,1,1,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,1,2,1,1,2,1,1,1,2,1,2,1,2,1,1,2,1,3,2,1,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,1,1,1,1,2,1,1,2,1,2,1,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,1,1,2,1,2,1,1,1,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,1,1,1,1,2,1,1,3,2,1,1,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,1,1,2,1,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,8,7,6,5,4,3,2,1,14,13,12,11,10,9,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1],"label":["rowSums","rowSums","rowSums","rowSums","rowMeans","rowMeans","rowMeans","rowMeans","<GC>","aperm.default","apply","aperm.default","apply","aperm.default","apply","aperm.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","apply","apply","length","local","FUN","apply","<GC>","apply","FUN","apply","FUN","apply","apply","apply","is.numeric","local","apply","FUN","apply","<GC>","mean.default","apply","FUN","apply","apply","apply","apply","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","mean.default","apply","apply","apply","mean.default","apply","apply","apply","<GC>","mean.default","apply","apply","apply","apply","apply","apply","apply","isTRUE","mean.default","apply","<GC>","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","apply","<GC>","apply","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","<GC>","apply","isTRUE","mean.default","apply","apply","mean.default","apply","apply","apply","apply","apply","<GC>","apply","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","mean.default","apply","apply","apply","apply","mean.default","apply","isTRUE","mean.default","apply","apply","apply","<GC>","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","apply","length","local","apply","<GC>","apply","FUN","apply","mean.default","apply","is.numeric","local","is.numeric","local","apply","apply","mean.default","apply","<GC>","apply","apply","apply","mean.default","apply","apply","apply","apply","apply","<GC>","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","length","local","mean.default","apply","<GC>","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","<GC>","apply","is.numeric","local","length","local","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","<GC>","mean.default","apply","mean.default","apply","length","local","FUN","apply","apply","apply","mean.default","apply","<GC>","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","apply","<GC>","FUN","apply","FUN","apply","apply","FUN","apply","apply","apply","apply","length","local","<GC>","FUN","apply","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","apply","apply","mean.default","apply","apply","<GC>","mean.default","apply","apply","apply","apply","mean.default","apply","FUN","apply","apply","apply","<GC>","FUN","apply","is.na","local","apply","is.na","local","isTRUE","mean.default","apply","apply","apply","<GC>","apply","FUN","apply","mean.default","apply","apply","is.numeric","local","mean.default","apply","<GC>","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","<GC>","apply","FUN","apply","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","<GC>","apply","length","local","apply","length","local","mean.default","apply","apply","apply","<GC>","FUN","apply","length","local","mean.default","apply","apply","mean.default","apply","FUN","apply","<GC>","mean.default","apply","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","apply","FUN","apply","apply","mean.default","apply","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","<GC>","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","<GC>","length","local","FUN","apply","is.na","local","FUN","apply","length","local","apply","<GC>","mean.default","apply","length","local","isTRUE","mean.default","apply","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","is.numeric","local","mean.default","apply","apply","mean.default","apply","mean.default","apply","apply","<GC>","FUN","apply","length","local","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","<GC>","FUN","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","<GC>","length","local","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","<GC>","length","local","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","isTRUE","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","FUN","apply","mean.default","apply","FUN","apply","<GC>","apply","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","length","local","FUN","apply","apply","apply","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","apply","is.numeric","local","FUN","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","length","local","FUN","apply","apply","is.na","local","isTRUE","mean.default","apply","apply","FUN","apply","apply","FUN","apply","apply","<GC>","apply","is.na","local","mean.default","apply","FUN","apply","apply","mean.default","apply","FUN","apply","length","local","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","mean.default","apply","is.na","local","FUN","apply","mean.default","apply","apply","apply","apply","mean.default","apply","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","apply","FUN","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","apply","mean.default","apply","apply","mean.default","apply","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","apply","apply","FUN","apply","<GC>","apply","<GC>","apply","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","mean.default","apply","apply","mean.default","apply","mean.default","apply","apply","isTRUE","mean.default","apply","length","local","<GC>","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","FUN","apply","is.na","local","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","apply","FUN","apply","apply","apply","<GC>","apply","apply","mean.default","apply","apply","FUN","apply","apply","mean.default","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","mean.default","apply","apply","apply","FUN","apply","is.na","local","<GC>","apply","apply","apply","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","is.numeric","local","<GC>","FUN","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","mean.default","apply","<GC>","apply","<GC>","apply","apply","apply","mean.default","apply","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","is.numeric","local","FUN","apply","apply","FUN","apply","is.na","local","mean.default","apply","mean.default","apply","<GC>","apply","isTRUE","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","FUN","apply","apply","mean.default","apply","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","FUN","apply","length","local","apply","mean.default","apply","apply","is.na","local","apply","apply","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","apply","mean.default","apply","<GC>","mean.default","apply","apply","FUN","apply","apply","apply","mean.default","apply","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","<GC>","length","local","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","<GC>","apply","<GC>","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","FUN","apply","is.numeric","local","apply","<GC>","apply","<GC>","apply","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","length","local","mean.default","apply","length","local","FUN","apply","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","apply","apply","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","apply","isTRUE","mean.default","apply","<GC>","is.numeric","local","<GC>","is.numeric","local","mean.default","apply","FUN","apply","apply","FUN","apply","mean.default","apply","apply","FUN","apply","apply","apply","<GC>","isTRUE","mean.default","apply","FUN","apply","is.numeric","local","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","apply","FUN","apply","apply","FUN","apply","<GC>","apply","<GC>","apply","length","local","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","apply","apply","mean.default","apply","is.numeric","local","apply","apply","apply","apply","mean.default","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","<GC>","apply","<GC>","apply","is.numeric","local","mean.default","apply","FUN","apply","apply","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","length","local","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","<GC>","apply","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","is.numeric","local","FUN","apply","apply","FUN","apply","apply","apply","mean.default","apply","FUN","apply","<GC>","isTRUE","mean.default","apply","<GC>","isTRUE","mean.default","apply","FUN","apply","apply","apply","FUN","apply","FUN","apply","mean.default","apply","apply","FUN","apply","<GC>","apply","apply","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","length","local","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","is.numeric","local","apply","apply","is.numeric","local","length","local","apply","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","apply","apply","mean.default","apply","apply","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","mean.default","apply","apply","isTRUE","mean.default","apply","apply","apply","is.numeric","local","<GC>","apply","<GC>","apply","FUN","apply","apply","length","local","apply","apply","FUN","apply","mean.default","apply","<GC>","is.numeric","local","<GC>","is.numeric","local","FUN","apply","FUN","apply","apply","is.na","local","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","apply","<GC>","apply","apply","is.numeric","local","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","apply","<GC>","apply","isTRUE","mean.default","apply","length","local","apply","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","<GC>","apply","is.numeric","local","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","is.numeric","local","apply","apply","apply","FUN","apply","apply","apply","<GC>","mean.default","apply","mean.default","apply","apply","FUN","apply","FUN","apply","FUN","apply","apply","length","local","<GC>","length","local","<GC>","length","local","FUN","apply","length","local","apply","apply","mean.default","apply","apply","<GC>","length","local","<GC>","length","local","is.numeric","local","mean.default","apply","apply","mean.default","apply","mean.default","apply","apply","isTRUE","mean.default","apply","<GC>","length","local","<GC>","length","local","FUN","apply","mean.default","apply","is.numeric","local","apply","apply","FUN","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","is.numeric","local","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","apply","mean.default","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","mean.default","apply","FUN","apply","is.na","local","mean.default","apply","FUN","apply","apply","FUN","apply","is.na","local","apply","FUN","apply","FUN","apply","apply","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","FUN","apply","mean.default","apply","length","local","apply","FUN","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","apply","length","local","FUN","apply","FUN","apply","<GC>","apply","<GC>","apply","<GC>","apply","mean.default","apply","is.numeric","local","FUN","apply","FUN","apply","apply","apply","apply","isTRUE","mean.default","apply","apply","FUN","apply","apply","FUN","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","<GC>","apply","<GC>","apply","mean.default","apply","length","local","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","length","local","is.na","local","isTRUE","mean.default","apply","apply","apply","is.na","local","FUN","apply","FUN","apply","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","apply","mean.default","apply","apply","apply","is.numeric","local","FUN","apply","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","is.numeric","local","apply","mean.default","apply","FUN","apply","<GC>","apply","<GC>","apply","<GC>","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","apply","apply","apply","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","apply","FUN","apply","apply","apply","FUN","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","mean.default","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","length","local","apply","FUN","apply","FUN","apply","apply","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","is.numeric","local","<GC>","apply","<GC>","apply","FUN","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","mean.default","apply","FUN","apply","is.na","local","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","mean.default","apply","length","local","<GC>","is.na","local","<GC>","is.na","local","<GC>","is.na","local","FUN","apply","apply","apply","mean.default","apply","mean.default","apply","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","length","local","length","local","apply","apply","apply","apply","mean.default","apply","apply","isTRUE","mean.default","apply","apply","apply","length","local","mean.default","apply","mean.default","apply","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","<GC>","apply","apply","apply","mean.default","apply","apply","apply","FUN","apply","apply","FUN","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","exists","findCenvVar","getInlineInfo","tryInline","cmpCall","cmp","cmpForBody","h","tryInline","cmpCall","cmp","genCode","compile","compiler:::tryCompile","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis"],"filenum":[1,1,1,1,1,1,1,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,1,1,1,null,null,null,1,null,1,null,1,null,1,1,1,null,null,1,null,1,null,null,1,null,1,1,1,1,1,null,null,1,null,null,1,null,1,null,1,null,1,1,1,null,1,1,1,null,null,1,1,1,1,1,1,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,null,1,1,null,1,1,1,1,1,null,1,1,null,1,null,1,null,null,1,1,null,1,null,null,1,null,null,1,1,1,1,null,1,null,null,1,1,1,null,1,null,null,1,null,null,1,null,1,null,1,1,null,null,1,null,1,null,1,null,1,null,null,null,null,1,1,null,1,null,1,1,1,null,1,1,1,1,1,null,null,1,null,1,null,1,null,1,1,null,null,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,null,1,1,null,1,null,1,null,null,null,null,null,1,null,1,null,1,null,1,1,null,null,1,null,1,null,null,null,1,1,1,null,1,null,1,null,1,null,null,1,1,1,null,1,1,null,null,1,null,1,1,null,1,1,1,1,null,null,null,null,1,null,1,null,1,1,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,null,1,null,1,1,null,1,1,null,null,1,null,1,null,1,1,1,null,1,1,null,null,1,1,1,1,null,1,null,1,1,1,null,null,1,null,null,1,null,null,null,null,1,1,1,null,1,null,1,null,1,1,null,null,null,1,null,null,1,null,1,1,null,1,null,1,null,1,null,null,1,null,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,null,1,null,null,null,1,1,1,null,null,1,null,null,null,1,1,null,1,null,1,null,null,1,null,1,1,null,1,null,null,1,null,1,null,1,null,null,1,1,null,1,1,null,1,null,1,null,null,1,null,1,1,null,1,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,null,null,null,1,null,null,null,1,null,null,1,null,null,1,null,null,null,null,1,1,null,1,null,null,1,null,null,null,null,1,1,null,1,null,1,1,null,null,1,null,null,null,1,null,1,null,1,null,1,null,null,1,1,null,1,null,1,null,1,null,1,null,1,null,null,null,null,null,1,null,1,null,1,null,1,1,null,null,null,1,null,1,null,1,1,null,1,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,1,null,1,null,1,null,1,1,null,null,1,1,null,1,null,1,1,null,1,1,null,1,null,1,null,1,null,1,1,null,1,1,1,null,null,1,null,null,null,1,1,1,1,null,1,null,1,null,null,1,null,1,null,1,null,1,1,null,null,1,1,1,null,null,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,1,1,null,null,null,1,1,null,null,null,null,1,1,null,1,1,null,1,1,null,1,null,null,null,1,null,1,1,null,1,null,1,null,null,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,null,null,1,null,1,1,1,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,null,1,null,null,1,null,1,1,null,1,1,null,1,1,null,null,1,null,1,null,1,null,null,1,null,1,1,null,1,null,null,1,null,1,1,1,null,1,null,1,null,1,null,1,null,1,1,null,null,1,null,1,1,null,1,null,1,1,null,null,1,null,null,null,null,1,null,null,1,1,null,1,null,1,null,null,null,1,null,null,1,null,1,1,null,1,1,1,null,1,1,null,1,1,null,1,1,null,1,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,1,null,1,1,null,null,1,null,1,1,1,null,1,null,1,1,null,1,null,null,1,null,1,1,null,1,1,null,1,null,1,null,1,1,1,null,1,null,null,null,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,null,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,1,null,1,null,1,null,1,1,1,null,1,1,null,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,null,1,1,null,1,null,null,null,1,null,1,null,1,null,null,1,null,1,null,null,1,1,null,1,1,null,1,1,null,1,1,null,null,1,null,null,1,null,1,null,null,1,null,1,1,null,null,1,1,null,1,1,null,null,1,null,null,1,null,1,1,1,1,null,1,null,null,1,null,1,null,1,1,null,1,null,null,1,1,null,1,1,1,null,1,1,null,1,null,null,1,null,1,null,1,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,1,null,null,1,null,1,null,1,1,null,1,null,1,1,null,1,null,1,null,null,1,null,null,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,null,1,1,null,1,1,null,1,null,null,1,null,1,null,1,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,null,1,null,1,null,null,1,null,null,1,null,null,null,1,null,null,null,1,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,1,1,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,1,1,null,1,null,1,1,null,1,null,1,1,null,null,1,null,null,null,null,null,null,null,1,null,1,1,null,1,null,1,1,null,1,1,1,null,null,null,1,null,1,null,null,null,1,null,1,null,null,1,1,1,null,1,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,1,null,1,1,null,1,null,1,null,1,null,null,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,1,null,1,null,null,1,1,1,1,null,1,null,1,null,null,1,null,null,1,1,null,1,1,null,1,null,1,1,1,null,1,null,1,null,1,null,null,null,1,null,1,1,null,1,null,null,1,1,null,1,null,null,1,null,null,1,1,null,null,1,null,1,null,1,1,null,1,null,1,null,1,1,null,1,null,1,1,1,null,1,1,1,null,null,1,null,null,1,null,null,null,1,1,null,1,1,1,null,1,null,1,null,null,null,1,null,null,null,1,null,1,1,1,null,1,null,1,null,1,1,null,1,null,1,1,null,1,null,null,1,1,null,1,null,1,1,null,1,null,null,1,null,null,1,1,null,1,1,null,1,null,1,1,null,null,null,1,null,1,null,1,null,1,null,1,null,1,1,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,1,null,null,null,null,1,1,null,1,null,null,1,null,null,1,null,null,1,1,1,null,1,1,1,null,1,null,null,1,null,null,1,null,1,null,1,1,null,null,1,1,1,null,null,null,1,null,1,null,1,1,null,null,1,1,null,1,null,1,null,null,null,null,null,null,null,1,null,1,1,null,null,1,null,1,null,null,1,null,1,null,1,1,null,null,null,null,1,null,null,1,1,null,null,1,null,1,null,1,null,1,null,null,1,null,null,1,1,null,1,null,1,null,null,1,null,1,null,null,null,1,null,1,1,null,null,1,1,null,1,null,null,1,null,null,1,null,null,1,1,1,null,1,1,1,null,null,1,null,1,1,null,1,null,1,null,1,1,null,null,null,null,null,null,null,null,null,1,null,null,1,1,null,1,1,null,null,null,null,null,null,null,null,null,1,1,null,1,null,1,1,null,null,1,null,null,null,null,null,null,null,1,null,1,null,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,null,null,null,1,null,null,1,null,1,1,null,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,1,null,1,null,1,null,null,1,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,1,null,null,1,null,null,1,1,1,null,1,null,1,null,1,null,null,null,1,null,1,1,null,1,null,null,1,null,1,null,1,1,1,1,null,null,1,null,null,1,null,1,1,null,1,null,1,null,null,1,null,1,1,null,1,1,null,1,null,1,1,null,1,1,1,null,null,null,1,null,1,null,1,null,1,null,1,null,1,null,null,null,1,null,1,1,1,1,null,null,1,1,null,1,1,null,1,1,null,1,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,1,null,null,1,null,1,1,null,1,null,null,null,null,null,null,1,1,1,null,null,null,1,null,1,1,1,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,1,null,1,1,null,1,1,1,null,null,null,1,null,1,1,null,1,null,null,1,1,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,1,null,1,1,1,1,1,null,1,1,null,1,null,1,1,null,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,1,null,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,1,1,null,1,null,1,null,null,1,null,null,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,1,null,1,null,1,null,1,null,null,1,null,1,1,null,1,null,1,1,null,1,null,null,null,null,null,null,null,null,null,null,null,null,1,1,1,null,1,null,1,1,1,1,null,null,1,null,1,null,1,null,1,1,null,1,null,1,1,null,1,null,null,1,null,null,1,null,null,1,null,null,null,null,1,1,1,1,null,1,1,null,null,1,1,1,null,null,null,1,null,1,1,null,1,1,null,1,null,1,null,1,1,1,null,1,1,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,1,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null],"linenum":[10,10,10,10,11,11,11,11,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,12,12,12,null,null,null,12,null,12,null,12,null,12,12,12,null,null,12,null,12,null,null,12,null,12,12,12,12,12,null,null,12,null,null,12,null,12,null,12,null,12,12,12,null,12,12,12,null,null,12,12,12,12,12,12,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,null,12,12,null,12,12,12,12,12,null,12,12,null,12,null,12,null,null,12,12,null,12,null,null,12,null,null,12,12,12,12,null,12,null,null,12,12,12,null,12,null,null,12,null,null,12,null,12,null,12,12,null,null,12,null,12,null,12,null,12,null,null,null,null,12,12,null,12,null,12,12,12,null,12,12,12,12,12,null,null,12,null,12,null,12,null,12,12,null,null,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,null,12,12,null,12,null,12,null,null,null,null,null,12,null,12,null,12,null,12,12,null,null,12,null,12,null,null,null,12,12,12,null,12,null,12,null,12,null,null,12,12,12,null,12,12,null,null,12,null,12,12,null,12,12,12,12,null,null,null,null,12,null,12,null,12,12,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,null,12,null,12,12,null,12,12,null,null,12,null,12,null,12,12,12,null,12,12,null,null,12,12,12,12,null,12,null,12,12,12,null,null,12,null,null,12,null,null,null,null,12,12,12,null,12,null,12,null,12,12,null,null,null,12,null,null,12,null,12,12,null,12,null,12,null,12,null,null,12,null,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,null,12,null,null,null,12,12,12,null,null,12,null,null,null,12,12,null,12,null,12,null,null,12,null,12,12,null,12,null,null,12,null,12,null,12,null,null,12,12,null,12,12,null,12,null,12,null,null,12,null,12,12,null,12,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,null,null,null,12,null,null,null,12,null,null,12,null,null,12,null,null,null,null,12,12,null,12,null,null,12,null,null,null,null,12,12,null,12,null,12,12,null,null,12,null,null,null,12,null,12,null,12,null,12,null,null,12,12,null,12,null,12,null,12,null,12,null,12,null,null,null,null,null,12,null,12,null,12,null,12,12,null,null,null,12,null,12,null,12,12,null,12,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,12,null,12,null,12,null,12,12,null,null,12,12,null,12,null,12,12,null,12,12,null,12,null,12,null,12,null,12,12,null,12,12,12,null,null,12,null,null,null,12,12,12,12,null,12,null,12,null,null,12,null,12,null,12,null,12,12,null,null,12,12,12,null,null,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,12,12,null,null,null,12,12,null,null,null,null,12,12,null,12,12,null,12,12,null,12,null,null,null,12,null,12,12,null,12,null,12,null,null,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,null,null,12,null,12,12,12,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,null,12,null,null,12,null,12,12,null,12,12,null,12,12,null,null,12,null,12,null,12,null,null,12,null,12,12,null,12,null,null,12,null,12,12,12,null,12,null,12,null,12,null,12,null,12,12,null,null,12,null,12,12,null,12,null,12,12,null,null,12,null,null,null,null,12,null,null,12,12,null,12,null,12,null,null,null,12,null,null,12,null,12,12,null,12,12,12,null,12,12,null,12,12,null,12,12,null,12,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,12,null,12,12,null,null,12,null,12,12,12,null,12,null,12,12,null,12,null,null,12,null,12,12,null,12,12,null,12,null,12,null,12,12,12,null,12,null,null,null,12,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,null,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,12,null,12,null,12,null,12,12,12,null,12,12,null,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,null,12,12,null,12,null,null,null,12,null,12,null,12,null,null,12,null,12,null,null,12,12,null,12,12,null,12,12,null,12,12,null,null,12,null,null,12,null,12,null,null,12,null,12,12,null,null,12,12,null,12,12,null,null,12,null,null,12,null,12,12,12,12,null,12,null,null,12,null,12,null,12,12,null,12,null,null,12,12,null,12,12,12,null,12,12,null,12,null,null,12,null,12,null,12,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,12,null,null,12,null,12,null,12,12,null,12,null,12,12,null,12,null,12,null,null,12,null,null,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,null,12,12,null,12,12,null,12,null,null,12,null,12,null,12,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,null,12,null,12,null,null,12,null,null,12,null,null,null,12,null,null,null,12,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,12,12,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,12,12,null,12,null,12,12,null,12,null,12,12,null,null,12,null,null,null,null,null,null,null,12,null,12,12,null,12,null,12,12,null,12,12,12,null,null,null,12,null,12,null,null,null,12,null,12,null,null,12,12,12,null,12,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,12,null,12,12,null,12,null,12,null,12,null,null,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,12,null,12,null,null,12,12,12,12,null,12,null,12,null,null,12,null,null,12,12,null,12,12,null,12,null,12,12,12,null,12,null,12,null,12,null,null,null,12,null,12,12,null,12,null,null,12,12,null,12,null,null,12,null,null,12,12,null,null,12,null,12,null,12,12,null,12,null,12,null,12,12,null,12,null,12,12,12,null,12,12,12,null,null,12,null,null,12,null,null,null,12,12,null,12,12,12,null,12,null,12,null,null,null,12,null,null,null,12,null,12,12,12,null,12,null,12,null,12,12,null,12,null,12,12,null,12,null,null,12,12,null,12,null,12,12,null,12,null,null,12,null,null,12,12,null,12,12,null,12,null,12,12,null,null,null,12,null,12,null,12,null,12,null,12,null,12,12,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,12,null,null,null,null,12,12,null,12,null,null,12,null,null,12,null,null,12,12,12,null,12,12,12,null,12,null,null,12,null,null,12,null,12,null,12,12,null,null,12,12,12,null,null,null,12,null,12,null,12,12,null,null,12,12,null,12,null,12,null,null,null,null,null,null,null,12,null,12,12,null,null,12,null,12,null,null,12,null,12,null,12,12,null,null,null,null,12,null,null,12,12,null,null,12,null,12,null,12,null,12,null,null,12,null,null,12,12,null,12,null,12,null,null,12,null,12,null,null,null,12,null,12,12,null,null,12,12,null,12,null,null,12,null,null,12,null,null,12,12,12,null,12,12,12,null,null,12,null,12,12,null,12,null,12,null,12,12,null,null,null,null,null,null,null,null,null,12,null,null,12,12,null,12,12,null,null,null,null,null,null,null,null,null,12,12,null,12,null,12,12,null,null,12,null,null,null,null,null,null,null,12,null,12,null,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,null,null,null,12,null,null,12,null,12,12,null,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,12,null,12,null,12,null,null,12,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,12,null,null,12,null,null,12,12,12,null,12,null,12,null,12,null,null,null,12,null,12,12,null,12,null,null,12,null,12,null,12,12,12,12,null,null,12,null,null,12,null,12,12,null,12,null,12,null,null,12,null,12,12,null,12,12,null,12,null,12,12,null,12,12,12,null,null,null,12,null,12,null,12,null,12,null,12,null,12,null,null,null,12,null,12,12,12,12,null,null,12,12,null,12,12,null,12,12,null,12,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,12,null,null,12,null,12,12,null,12,null,null,null,null,null,null,12,12,12,null,null,null,12,null,12,12,12,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,12,null,12,12,null,12,12,12,null,null,null,12,null,12,12,null,12,null,null,12,12,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,12,null,12,12,12,12,12,null,12,12,null,12,null,12,12,null,12,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,12,null,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,12,12,null,12,null,12,null,null,12,null,null,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,12,null,12,null,12,null,12,null,null,12,null,12,12,null,12,null,12,12,null,12,null,null,null,null,null,null,null,null,null,null,null,null,12,12,12,null,12,null,12,12,12,12,null,null,12,null,12,null,12,null,12,12,null,12,null,12,12,null,12,null,null,12,null,null,12,null,null,12,null,null,null,null,12,12,12,12,null,12,12,null,null,12,12,12,null,null,null,12,null,12,12,null,12,12,null,12,null,12,null,12,12,12,null,12,12,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,13,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,13,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null],"memalloc":[124.5185775756836,124.5185775756836,124.5185775756836,124.5185775756836,139.8008117675781,139.8008117675781,139.8008117675781,139.8008117675781,139.8011779785156,139.8011779785156,139.8011779785156,170.2665634155273,170.2665634155273,170.2665634155273,170.2665634155273,170.2665634155273,170.2665634155273,170.2666091918945,170.2666091918945,170.2664566040039,170.2664566040039,170.2664566040039,170.2664566040039,170.2664566040039,170.2664566040039,170.2664566040039,170.2664566040039,170.2664566040039,170.2664566040039,170.2664566040039,170.2664566040039,170.2664566040039,170.2664566040039,170.2662963867188,170.2662963867188,185.5651321411133,185.5651321411133,185.8097457885742,186.069450378418,186.069450378418,186.3531951904297,186.3531951904297,186.6746139526367,187.0277938842773,187.4234237670898,187.8207321166992,187.8207321166992,188.2381744384766,188.2381744384766,188.5720367431641,188.5720367431641,185.8539657592773,185.8539657592773,186.2279739379883,186.2279739379883,186.6287612915039,187.0575561523438,187.4787139892578,187.4787139892578,187.8948211669922,188.2913436889648,188.2913436889648,188.635986328125,188.635986328125,188.635986328125,185.9345474243164,185.9345474243164,186.2970809936523,186.6751251220703,187.0784759521484,187.4903869628906,187.8953399658203,187.8953399658203,187.8953399658203,188.3012161254883,188.3012161254883,188.3012161254883,188.7092132568359,188.7092132568359,185.9906997680664,185.9906997680664,186.3516311645508,186.3516311645508,186.7337341308594,187.1380767822266,187.5548477172852,187.5548477172852,187.968147277832,188.3821563720703,188.7974014282227,188.7974014282227,188.7974014282227,186.1246566772461,186.4852600097656,186.8615493774414,187.2544479370117,187.6654052734375,188.0752487182617,188.4864120483398,188.4864120483398,188.4864120483398,188.8761825561523,188.8761825561523,188.8761825561523,186.2564697265625,186.2564697265625,186.5895385742188,186.5895385742188,186.9606552124023,186.9606552124023,187.3437194824219,187.3437194824219,187.7482299804688,187.7482299804688,188.1502227783203,188.1502227783203,188.5556793212891,188.9537124633789,188.9537124633789,186.3507080078125,186.7246932983398,186.7246932983398,187.0937423706055,187.0937423706055,187.4733428955078,187.857795715332,187.857795715332,188.2571258544922,188.2571258544922,188.651481628418,188.651481628418,189.0299224853516,189.0299224853516,186.4614791870117,186.4614791870117,186.4614791870117,186.7914123535156,187.1498565673828,187.1498565673828,187.521842956543,187.9106979370117,188.3105621337891,188.7130432128906,189.1048889160156,189.1048889160156,186.5817184448242,186.9117279052734,186.9117279052734,187.2681350708008,187.2681350708008,187.6350555419922,187.6350555419922,187.6350555419922,188.0183486938477,188.4133377075195,188.4133377075195,188.782844543457,188.782844543457,188.782844543457,189.1787414550781,189.1787414550781,189.1787414550781,186.6791763305664,187.0019760131836,187.3537063598633,187.7190093994141,187.7190093994141,188.1062774658203,188.1062774658203,188.1062774658203,188.503776550293,188.9057159423828,189.2513580322266,189.2513580322266,186.8319549560547,186.8319549560547,186.8319549560547,187.1597518920898,187.1597518920898,187.1597518920898,187.5152816772461,187.5152816772461,187.8872985839844,187.8872985839844,188.2559814453125,188.656379699707,188.656379699707,189.0619430541992,189.3228073120117,189.3228073120117,186.9602432250977,186.9602432250977,187.277099609375,187.277099609375,187.6570358276367,187.6570358276367,188.0216674804688,188.0216674804688,188.4014282226562,188.7776489257812,189.1642074584961,189.1642074584961,189.3930435180664,189.3930435180664,187.1234741210938,187.4478073120117,187.7954864501953,187.7954864501953,188.1582565307617,188.5364608764648,188.934684753418,189.3365325927734,189.462287902832,189.462287902832,189.462287902832,187.3169097900391,187.3169097900391,187.6482086181641,187.6482086181641,188.0023040771484,188.0023040771484,188.3714752197266,188.7576065063477,188.7576065063477,189.1592712402344,189.1592712402344,189.5302352905273,189.5302352905273,189.5302352905273,187.2340087890625,187.2340087890625,187.2340087890625,187.531623840332,187.531623840332,187.8592147827148,187.8592147827148,188.2138366699219,188.2138366699219,188.582893371582,188.582893371582,188.582893371582,188.9675064086914,189.3647994995117,189.3647994995117,189.5971832275391,189.5971832275391,187.4374618530273,187.4374618530273,187.7149276733398,187.7149276733398,188.0519561767578,188.0519561767578,188.4135055541992,188.4135055541992,188.7898330688477,188.7898330688477,189.1801071166992,189.1801071166992,189.5802459716797,189.6630249023438,189.6630249023438,189.6630249023438,187.6790466308594,187.6790466308594,188.0012054443359,188.0012054443359,188.3496551513672,188.3496551513672,188.7213134765625,189.109245300293,189.5143508911133,189.5143508911133,189.7278442382812,189.7278442382812,187.653564453125,187.653564453125,187.9653930664062,187.9653930664062,187.9653930664062,188.3008804321289,188.6609268188477,189.0424423217773,189.0424423217773,189.4396743774414,189.7915649414062,189.7915649414062,189.7915649414062,187.6326293945312,187.6326293945312,187.9322738647461,188.2523574829102,188.2523574829102,188.6055755615234,188.9782333374023,189.3678436279297,189.7751541137695,189.7751541137695,189.8542785644531,189.8542785644531,189.8542785644531,187.9514923095703,187.9514923095703,188.2592468261719,188.2592468261719,188.6014862060547,188.9655456542969,188.9655456542969,189.3531723022461,189.3531723022461,189.7541198730469,189.7541198730469,189.9159698486328,189.9159698486328,189.9159698486328,189.9159698486328,189.9159698486328,189.9159698486328,189.9159698486328,189.9159698486328,189.9159698486328,189.9159698486328,189.9159698486328,189.9159698486328,189.9159698486328,189.9159698486328,189.9159698486328,189.9159698486328,189.9159698486328,189.9159698486328,189.9159698486328,189.9159698486328,189.9159698486328,187.8106307983398,187.8106307983398,188.01416015625,188.01416015625,188.2433471679688,188.2433471679688,188.4914779663086,188.4914779663086,188.4914779663086,188.7716903686523,188.7716903686523,189.0854415893555,189.427619934082,189.427619934082,189.783805847168,189.9763488769531,189.9763488769531,189.9763488769531,187.986946105957,187.986946105957,188.2491073608398,188.2491073608398,188.5543365478516,188.9012680053711,189.2681427001953,189.2681427001953,189.654670715332,190.0360412597656,190.0360412597656,190.0360412597656,187.9923934936523,188.2737884521484,188.5775375366211,188.9222106933594,188.9222106933594,189.2898101806641,189.2898101806641,189.6760177612305,190.0792617797852,190.0948791503906,190.0948791503906,190.0948791503906,188.3404312133789,188.3404312133789,188.6417541503906,188.9856567382812,188.9856567382812,189.3550186157227,189.3550186157227,189.3550186157227,189.744270324707,190.1467437744141,190.1526641845703,190.1526641845703,188.4275970458984,188.4275970458984,188.7282104492188,188.7282104492188,189.0717391967773,189.4394149780273,189.4394149780273,189.8272323608398,189.8272323608398,190.2095794677734,190.2095794677734,190.2095794677734,188.2890319824219,188.2890319824219,188.5637054443359,188.8666915893555,188.8666915893555,189.2122650146484,189.2122650146484,189.578483581543,189.578483581543,189.9646682739258,189.9646682739258,189.9646682739258,190.2655944824219,190.2655944824219,190.2655944824219,188.4006881713867,188.4006881713867,188.6726684570312,188.6726684570312,188.9759140014648,188.9759140014648,188.9759140014648,189.3068542480469,189.3068542480469,189.6725311279297,189.6725311279297,190.0617980957031,190.0617980957031,190.3206329345703,190.3206329345703,188.515022277832,188.515022277832,188.7905654907227,188.7905654907227,189.1037445068359,189.1037445068359,189.4566802978516,189.8259887695312,189.8259887695312,190.2180023193359,190.2180023193359,190.3748779296875,190.3748779296875,188.6446762084961,188.6446762084961,188.9207077026367,189.2379531860352,189.2379531860352,189.5913238525391,189.5913238525391,189.9645004272461,190.3533020019531,190.4281539916992,190.4281539916992,190.4281539916992,188.8051071166992,188.8051071166992,189.0964050292969,189.0964050292969,189.4302444458008,189.7919921875,189.7919921875,190.1748580932617,190.1748580932617,190.480583190918,190.480583190918,190.480583190918,188.7481384277344,188.7481384277344,189.0220565795898,189.3314895629883,189.3314895629883,189.6820449829102,189.6820449829102,189.6820449829102,190.0549087524414,190.0549087524414,190.442024230957,190.442024230957,190.5322265625,190.5322265625,190.5322265625,188.9343032836914,189.2178039550781,189.2178039550781,189.5430908203125,189.9029006958008,189.9029006958008,190.2838363647461,190.2838363647461,190.5830230712891,190.5830230712891,190.5830230712891,188.8810653686523,188.8810653686523,189.1483688354492,189.4522399902344,189.4522399902344,189.7988662719727,190.1671371459961,190.1671371459961,190.5558624267578,190.5558624267578,190.6328887939453,190.6328887939453,190.6328887939453,189.1196212768555,189.1196212768555,189.4085845947266,189.4085845947266,189.7434310913086,189.7434310913086,190.1057739257812,190.1057739257812,190.4909362792969,190.4909362792969,190.6820678710938,190.6820678710938,190.6820678710938,189.1143798828125,189.1143798828125,189.3949966430664,189.3949966430664,189.7201232910156,189.7201232910156,190.0786666870117,190.0786666870117,190.4571914672852,190.7304000854492,190.7304000854492,190.7304000854492,189.1323471069336,189.1323471069336,189.4011764526367,189.4011764526367,189.4011764526367,189.7094345092773,190.0941772460938,190.0941772460938,190.4657897949219,190.4657897949219,190.4657897949219,190.7779541015625,190.7779541015625,190.7779541015625,189.1833572387695,189.1833572387695,189.451789855957,189.7562637329102,189.7562637329102,190.1052856445312,190.1052856445312,190.4736557006836,190.8247299194336,190.8247299194336,190.8247299194336,189.2274856567383,189.2274856567383,189.4974899291992,189.4974899291992,189.8023147583008,189.8023147583008,190.1501007080078,190.1501007080078,190.5198287963867,190.5198287963867,190.8707809448242,190.8707809448242,190.8707809448242,189.2911682128906,189.5557098388672,189.5557098388672,189.8594589233398,189.8594589233398,190.2044677734375,190.2044677734375,190.5257720947266,190.5257720947266,190.9052963256836,190.9052963256836,190.9160079956055,190.9160079956055,190.9160079956055,189.5725631713867,189.5725631713867,189.5725631713867,189.8631362915039,189.8631362915039,190.1861953735352,190.1861953735352,190.5492553710938,190.5492553710938,190.927360534668,190.960578918457,190.960578918457,190.960578918457,189.6160430908203,189.8993682861328,189.8993682861328,190.2285842895508,190.2285842895508,190.5873107910156,190.9661254882812,190.9661254882812,191.0043869018555,191.0043869018555,191.0043869018555,191.0043869018555,191.0043869018555,191.0043869018555,191.0043869018555,191.0043869018555,191.0043869018555,191.0043869018555,191.0043869018555,191.0043869018555,191.0043869018555,191.0043869018555,191.0043869018555,191.0043869018555,191.0043869018555,191.0043869018555,191.0043869018555,191.0043869018555,191.0043869018555,191.0043869018555,191.0043869018555,191.0043869018555,191.0043869018555,191.0043869018555,191.0043869018555,191.0043869018555,191.0043869018555,191.0043869018555,191.0043869018555,191.0043869018555,191.0043869018555,191.0043869018555,191.0043869018555,191.0043869018555,191.0043869018555,191.0043869018555,191.0043869018555,191.0043869018555,191.0043869018555,191.0043869018555,191.0043869018555,191.0043869018555,191.0043869018555,191.0043869018555,191.0043869018555,191.0043869018555,191.0043869018555,191.0043869018555,191.0043869018555,191.0043869018555,191.0043869018555,191.0043869018555,191.0043869018555,191.0043869018555,191.0043869018555,191.0043869018555,191.0043869018555,191.0043869018555,191.0043869018555,191.0043869018555,191.0043869018555,191.0043869018555,191.0043869018555,191.0043869018555,189.4948272705078,189.4948272705078,189.4948272705078,189.5214767456055,189.5214767456055,189.5214767456055,189.775016784668,189.775016784668,190.044548034668,190.044548034668,190.3500671386719,190.3500671386719,190.6760864257812,190.9986343383789,190.9986343383789,190.9986343383789,191.3610916137695,191.7643890380859,191.7643890380859,192.1830749511719,192.1830749511719,192.5285873413086,192.8733978271484,192.8733978271484,193.2162780761719,193.5577697753906,193.5577697753906,193.9008712768555,193.9008712768555,194.2431793212891,194.2431793212891,194.2708892822266,194.2708892822266,189.9091796875,190.2524948120117,190.2524948120117,190.6196594238281,190.9629974365234,191.341178894043,191.341178894043,191.341178894043,191.7444229125977,191.7444229125977,192.1558990478516,192.1558990478516,192.5767440795898,192.9989395141602,193.4218444824219,193.844841003418,193.844841003418,194.2564010620117,194.2564010620117,194.4014663696289,194.4014663696289,194.4014663696289,189.981689453125,189.981689453125,190.2896347045898,190.2896347045898,190.633918762207,190.633918762207,190.9742584228516,191.3274307250977,191.3274307250977,191.3274307250977,191.7544021606445,192.1557159423828,192.5697937011719,192.5697937011719,192.9907531738281,192.9907531738281,193.4101257324219,193.4101257324219,193.8291625976562,193.8291625976562,194.2450408935547,194.2450408935547,194.530029296875,194.530029296875,194.530029296875,194.530029296875,194.530029296875,194.530029296875,190.4001922607422,190.4001922607422,190.7298431396484,191.0312118530273,191.0312118530273,191.3700332641602,191.3700332641602,191.7452697753906,192.1358489990234,192.1358489990234,192.5429382324219,192.5429382324219,192.5429382324219,192.9607238769531,193.3808135986328,193.3808135986328,193.8037796020508,194.2262649536133,194.2262649536133,194.6326599121094,194.6564254760742,194.6564254760742,190.4824600219727,190.4824600219727,190.7962188720703,190.7962188720703,191.1230850219727,191.1230850219727,191.4620056152344,191.8334274291992,191.8334274291992,192.2213897705078,192.2213897705078,192.6243438720703,192.6243438720703,193.0387725830078,193.0387725830078,193.45849609375,193.45849609375,193.8805313110352,193.8805313110352,194.3025512695312,194.3025512695312,194.7112350463867,194.7112350463867,194.7808990478516,194.7808990478516,194.7808990478516,190.6340408325195,190.6340408325195,190.9386444091797,190.9386444091797,191.2574615478516,191.2574615478516,191.596305847168,191.596305847168,191.9624099731445,192.3824234008789,192.7827529907227,193.1924438476562,193.1924438476562,193.6092529296875,194.0291061401367,194.0291061401367,194.4495315551758,194.4495315551758,194.8543548583984,194.8543548583984,194.9032669067383,194.9032669067383,190.8344955444336,190.8344955444336,191.1350708007812,191.1350708007812,191.4442596435547,191.4442596435547,191.7915267944336,192.1611099243164,192.1611099243164,192.1611099243164,192.5448837280273,192.5448837280273,192.5448837280273,192.9237365722656,192.9237365722656,193.3236846923828,193.7293701171875,193.7293701171875,194.1436080932617,194.5626678466797,194.5626678466797,194.9692916870117,195.023681640625,195.023681640625,195.023681640625,191.0115966796875,191.0115966796875,191.3060607910156,191.3060607910156,191.59912109375,191.59912109375,191.59912109375,191.9425201416016,191.9425201416016,192.3063278198242,192.6863403320312,192.6863403320312,193.0813598632812,193.0813598632812,193.0813598632812,193.4875793457031,193.4875793457031,193.9035110473633,194.3245010375977,194.7462692260742,194.7462692260742,195.1421966552734,195.1421966552734,195.1421966552734,195.1421966552734,191.2422027587891,191.2422027587891,191.5331726074219,191.5331726074219,191.8381500244141,192.229248046875,192.229248046875,192.229248046875,192.6019668579102,192.6019668579102,192.9831314086914,193.3815841674805,193.3815841674805,193.7901382446289,193.7901382446289,194.1907577514648,194.6076431274414,194.6076431274414,194.6076431274414,195.0228576660156,195.0228576660156,195.2588119506836,195.2588119506836,195.2588119506836,195.2588119506836,195.2588119506836,195.2588119506836,191.5248794555664,191.8094940185547,191.8094940185547,192.1370544433594,192.1370544433594,192.4952163696289,192.4952163696289,192.8624725341797,192.8624725341797,193.2495803833008,193.2495803833008,193.2495803833008,193.6473770141602,193.6473770141602,194.0548858642578,194.4698333740234,194.4698333740234,194.8885040283203,195.2958602905273,195.3734130859375,195.3734130859375,191.5300979614258,191.7983551025391,191.7983551025391,192.098991394043,192.4485397338867,192.4485397338867,192.8169708251953,193.1975936889648,193.1975936889648,193.5911254882812,193.9709396362305,193.9709396362305,194.378547668457,194.378547668457,194.7963562011719,194.7963562011719,195.2131118774414,195.2131118774414,195.486328125,195.486328125,195.486328125,195.486328125,195.486328125,195.486328125,191.8414001464844,191.8414001464844,192.1451644897461,192.1451644897461,192.4549407958984,192.8035659790039,192.8035659790039,192.8035659790039,193.1623840332031,193.1623840332031,193.5386047363281,193.9279403686523,194.3298416137695,194.3298416137695,194.7422027587891,194.7422027587891,195.1605987548828,195.5655288696289,195.5655288696289,195.5973052978516,195.5973052978516,195.5973052978516,191.9013977050781,191.9013977050781,192.1685485839844,192.4721145629883,192.4721145629883,192.8144683837891,193.1482238769531,193.1482238769531,193.4884033203125,193.4884033203125,193.8655166625977,193.8655166625977,194.2653045654297,194.6736450195312,195.0910263061523,195.0910263061523,195.5079879760742,195.5079879760742,195.7064895629883,195.7064895629883,191.9572982788086,192.2202682495117,192.5014419555664,192.5014419555664,192.8279647827148,192.8279647827148,193.1817169189453,193.1817169189453,193.544059753418,193.544059753418,193.9223861694336,193.9223861694336,194.3184356689453,194.3184356689453,194.7258911132812,194.7258911132812,195.1420059204102,195.1420059204102,195.5604782104492,195.5604782104492,195.8140335083008,195.8140335083008,195.8140335083008,195.8140335083008,195.8140335083008,195.8140335083008,192.3721694946289,192.3721694946289,192.3721694946289,192.6523818969727,192.6523818969727,192.9759750366211,192.9759750366211,193.3248062133789,193.3248062133789,193.689094543457,193.689094543457,194.0651550292969,194.0651550292969,194.4622421264648,194.4622421264648,194.8694152832031,195.2859954833984,195.7032318115234,195.7032318115234,195.9196929931641,195.9196929931641,195.9196929931641,195.9196929931641,192.4969100952148,192.7677383422852,193.0802307128906,193.0802307128906,193.4178085327148,193.7754516601562,193.7754516601562,193.7754516601562,194.1472625732422,194.1472625732422,194.5408935546875,194.5408935546875,194.9425430297852,194.9425430297852,195.3535614013672,195.7690124511719,195.7690124511719,196.0238037109375,196.0238037109375,196.0238037109375,196.0238037109375,192.6680908203125,192.6680908203125,192.9246520996094,192.9246520996094,193.2292861938477,193.2292861938477,193.2292861938477,193.5621643066406,193.5621643066406,193.9189529418945,193.9189529418945,194.28271484375,194.6678314208984,194.6678314208984,195.0689926147461,195.0689926147461,195.481689453125,195.481689453125,195.8965148925781,195.8965148925781,196.1261520385742,196.1261520385742,192.6122665405273,192.6122665405273,192.6122665405273,192.8614730834961,192.8614730834961,193.136604309082,193.136604309082,193.136604309082,193.4433670043945,193.7797546386719,193.7797546386719,194.1401824951172,194.50634765625,194.50634765625,194.8978881835938,195.3031921386719,195.3031921386719,195.7179946899414,196.1293334960938,196.1293334960938,196.1293334960938,196.2268905639648,196.2268905639648,196.2268905639648,192.8276748657227,192.8276748657227,193.0749740600586,193.0749740600586,193.3579635620117,193.6682662963867,193.6682662963867,194.0105133056641,194.3717193603516,194.3717193603516,194.7446441650391,195.1384735107422,195.5456237792969,195.5456237792969,195.9630813598633,196.3259811401367,196.3259811401367,196.3259811401367,196.3259811401367,196.3259811401367,196.3259811401367,193.0585098266602,193.0585098266602,193.3144683837891,193.5974502563477,193.9119033813477,194.2591171264648,194.2591171264648,194.6237640380859,194.6237640380859,194.6237640380859,195.0055770874023,195.0055770874023,195.403923034668,195.403923034668,195.8147735595703,196.2288436889648,196.2288436889648,196.4234390258789,196.4234390258789,196.4234390258789,193.0898208618164,193.332275390625,193.332275390625,193.6003875732422,193.894905090332,194.2244033813477,194.2244033813477,194.582878112793,194.9480667114258,194.9480667114258,195.3335952758789,195.3335952758789,195.3335952758789,195.7368545532227,195.7368545532227,196.1499328613281,196.1499328613281,196.5193099975586,196.5193099975586,196.5193099975586,196.5193099975586,196.5193099975586,196.5193099975586,196.5193099975586,196.5193099975586,196.5193099975586,196.5193099975586,196.5193099975586,196.5193099975586,196.5193099975586,196.5193099975586,196.5193099975586,196.5193099975586,196.5193099975586,196.5193099975586,196.5193099975586,196.5193099975586,196.5193099975586,196.5193099975586,196.5193099975586,196.5193099975586,196.5193099975586,196.5193099975586,196.5193099975586,196.5193099975586,196.5193099975586,196.5193099975586,196.5193099975586,196.5193099975586,196.5193099975586,196.5193099975586,196.5193099975586,196.5193099975586,196.5193099975586,196.5193099975586,196.5193099975586,193.3703384399414,193.5766677856445,193.5766677856445,193.5766677856445,193.8089828491211,193.8089828491211,194.0558547973633,194.0558547973633,194.3666229248047,194.6875839233398,194.6875839233398,195.0294647216797,195.0294647216797,195.3863830566406,195.7655334472656,195.7655334472656,196.165657043457,196.165657043457,196.5695724487305,196.5695724487305,196.5695724487305,196.6132736206055,196.6132736206055,196.6132736206055,196.6132736206055,193.4414749145508,193.4414749145508,193.6824493408203,193.6824493408203,193.9363403320312,193.9363403320312,193.9363403320312,194.2143249511719,194.2143249511719,194.5311813354492,194.5311813354492,194.8779754638672,194.8779754638672,195.2339859008789,195.2339859008789,195.6133880615234,195.6133880615234,196.0183715820312,196.0183715820312,196.4294662475586,196.4294662475586,196.7060852050781,196.7060852050781,196.7060852050781,196.7060852050781,193.6878967285156,193.6878967285156,193.9432754516602,194.2257385253906,194.2257385253906,194.2257385253906,194.5439224243164,194.8963851928711,194.8963851928711,195.2599716186523,195.6398773193359,195.6398773193359,196.0422897338867,196.0422897338867,196.4512329101562,196.797492980957,196.797492980957,196.797492980957,196.797492980957,193.7859573364258,194.0342559814453,194.0342559814453,194.3401794433594,194.3401794433594,194.652458190918,194.652458190918,195.0009765625,195.0009765625,195.0009765625,195.3608551025391,195.3608551025391,195.7367324829102,195.7367324829102,196.1347274780273,196.1347274780273,196.1347274780273,196.5433883666992,196.5433883666992,196.887321472168,196.887321472168,196.887321472168,196.887321472168,196.887321472168,196.887321472168,193.9243240356445,193.9243240356445,194.1705169677734,194.1705169677734,194.4439392089844,194.4439392089844,194.7523727416992,194.7523727416992,195.0960235595703,195.4576263427734,195.4576263427734,195.8338928222656,195.8338928222656,196.2318420410156,196.2318420410156,196.2318420410156,196.6415481567383,196.6415481567383,196.9757232666016,196.9757232666016,196.9757232666016,196.9757232666016,194.0674362182617,194.0674362182617,194.3138046264648,194.3138046264648,194.5889511108398,194.8993682861328,195.2466354370117,195.6088333129883,195.6088333129883,195.9859313964844,195.9859313964844,196.3844604492188,196.3844604492188,196.7939834594727,196.7939834594727,197.0628280639648,197.0628280639648,197.0628280639648,197.0628280639648,197.0628280639648,197.0628280639648,194.2341613769531,194.2341613769531,194.4784240722656,194.7797164916992,194.7797164916992,195.0920639038086,195.0920639038086,195.4386291503906,195.8003005981445,195.8003005981445,196.1761779785156,196.1761779785156,196.5776443481445,196.9824905395508,196.9824905395508,196.9824905395508,197.1483306884766,197.1483306884766,197.1483306884766,197.1483306884766,197.1483306884766,197.1483306884766,194.4267272949219,194.4267272949219,194.6818313598633,194.6818313598633,194.9705581665039,195.2988052368164,195.2988052368164,195.6559143066406,195.6559143066406,196.0250701904297,196.4088821411133,196.4088821411133,196.808952331543,197.2041931152344,197.2325744628906,197.2325744628906,197.2325744628906,197.2325744628906,194.4045944213867,194.4045944213867,194.6422348022461,194.6422348022461,194.9054183959961,194.9054183959961,195.20458984375,195.20458984375,195.540657043457,195.540657043457,195.540657043457,195.9021072387695,196.2752456665039,196.668586730957,196.668586730957,197.0764694213867,197.3154144287109,197.3154144287109,197.3154144287109,197.3154144287109,197.3154144287109,197.3154144287109,194.6465606689453,194.6465606689453,194.8962631225586,194.8962631225586,195.1759872436523,195.1759872436523,195.5300979614258,195.5300979614258,195.8834457397461,196.2476043701172,196.2476043701172,196.6287384033203,197.0341033935547,197.0341033935547,197.3968887329102,197.3968887329102,197.3968887329102,197.3968887329102,194.6963119506836,194.6963119506836,194.9376068115234,194.9376068115234,195.2070846557617,195.2070846557617,195.5138244628906,195.5138244628906,195.5138244628906,195.8605422973633,195.8605422973633,196.2266006469727,196.2266006469727,196.6042098999023,196.6042098999023,197.0042953491211,197.0042953491211,197.4081039428711,197.4081039428711,197.4081039428711,197.4770965576172,197.4770965576172,194.7590637207031,194.9926452636719,194.9926452636719,195.2509613037109,195.2509613037109,195.5458145141602,195.8800048828125,196.2388076782227,196.6075286865234,196.9967575073242,196.9967575073242,197.4042053222656,197.4042053222656,197.5559997558594,197.5559997558594,197.5559997558594,197.5559997558594,197.5559997558594,197.5559997558594,195.0685958862305,195.3212966918945,195.3212966918945,195.6063232421875,195.9336929321289,195.9336929321289,196.2878036499023,196.2878036499023,196.6906509399414,197.0748138427734,197.4822845458984,197.4822845458984,197.6335983276367,197.6335983276367,197.6335983276367,197.6335983276367,195.1835098266602,195.1835098266602,195.4384536743164,195.4384536743164,195.7274475097656,195.7274475097656,196.0591659545898,196.4176330566406,196.4176330566406,196.786994934082,196.786994934082,196.786994934082,197.1744232177734,197.5806655883789,197.5806655883789,197.7099914550781,197.7099914550781,197.7099914550781,197.7099914550781,197.7099914550781,197.7099914550781,195.3124694824219,195.5645294189453,195.5645294189453,195.8535919189453,196.1839370727539,196.1839370727539,196.5428314208984,196.5428314208984,196.9131698608398,197.3003540039062,197.3003540039062,197.7065582275391,197.7065582275391,197.78515625,197.78515625,195.2304306030273,195.4631118774414,195.4631118774414,195.7212371826172,195.7212371826172,196.0134811401367,196.348388671875,196.7097625732422,196.7097625732422,197.0822296142578,197.473014831543,197.8590698242188,197.8590698242188,197.8590698242188,197.8590698242188,197.8590698242188,197.8590698242188,195.4252700805664,195.4252700805664,195.6637954711914,195.6637954711914,195.932975769043,196.2427978515625,196.2427978515625,196.5909423828125,196.9560012817383,197.3350143432617,197.3350143432617,197.7354049682617,197.7354049682617,197.9317932128906,197.9317932128906,197.9317932128906,197.9317932128906,197.9317932128906,197.9317932128906,197.9317932128906,197.9317932128906,195.6236419677734,195.6236419677734,195.8700103759766,196.1506652832031,196.4757537841797,196.4757537841797,196.8300552368164,196.8300552368164,197.1959457397461,197.1959457397461,197.5805511474609,197.9750213623047,197.9750213623047,198.0034484863281,198.0034484863281,195.5958480834961,195.8304824829102,195.8304824829102,196.0907135009766,196.0907135009766,196.0907135009766,196.3915252685547,196.7329330444336,196.7329330444336,197.0952911376953,197.0952911376953,197.466552734375,197.8587875366211,197.8587875366211,198.0737838745117,198.0737838745117,198.0737838745117,198.0737838745117,198.0737838745117,198.0737838745117,195.8447647094727,196.0915298461914,196.0915298461914,196.3742752075195,196.7009429931641,196.7009429931641,197.0601425170898,197.0601425170898,197.4305725097656,197.8186111450195,197.8186111450195,198.1431274414062,198.1431274414062,198.1431274414062,198.1431274414062,195.8653564453125,195.8653564453125,196.1036682128906,196.1036682128906,196.3737106323242,196.3737106323242,196.6775283813477,196.6775283813477,197.017707824707,197.3772583007812,197.7462844848633,197.7462844848633,198.1377944946289,198.1377944946289,198.1377944946289,198.211296081543,198.211296081543,198.211296081543,198.211296081543,198.211296081543,198.211296081543,198.211296081543,198.211296081543,198.211296081543,198.211296081543,198.211296081543,198.211296081543,198.211296081543,198.211296081543,198.211296081543,198.211296081543,198.211296081543,198.211296081543,198.211296081543,198.211296081543,198.211296081543,198.211296081543,198.211296081543,198.211296081543,198.211296081543,198.211296081543,198.211296081543,195.8653182983398,195.8653182983398,195.8653182983398,195.9037628173828,195.9037628173828,196.1101760864258,196.3443222045898,196.5986709594727,196.5986709594727,196.8915557861328,196.8915557861328,197.22216796875,197.5611877441406,197.9213714599609,197.9213714599609,198.2781295776367,198.2781295776367,198.2781295776367,198.2781295776367,198.2781295776367,198.2781295776367,196.0629653930664,196.0629653930664,196.0629653930664,196.3013153076172,196.5670394897461,196.8749160766602,196.8749160766602,197.2191543579102,197.5826950073242,197.9605560302734,197.9605560302734,198.3441467285156,198.3441467285156,198.3441467285156,198.3441467285156,198.3441467285156,198.3441467285156,196.1386871337891,196.1386871337891,196.3740615844727,196.3740615844727,196.6338272094727,196.9373016357422,196.9373016357422,196.9373016357422,197.2784042358398,197.6440963745117,198.0212173461914,198.0212173461914,198.409065246582,198.409065246582,198.409065246582,198.409065246582,196.2580795288086,196.2580795288086,196.4942245483398,196.7569885253906,196.7569885253906,197.0636444091797,197.4065704345703,197.7696304321289,197.7696304321289,198.1462249755859,198.1462249755859,198.4729766845703,198.4729766845703,198.4729766845703,198.4729766845703,198.4729766845703,198.4729766845703,196.3596725463867,196.3596725463867,196.5962295532227,196.5962295532227,196.8598480224609,197.1656646728516,197.1656646728516,197.5104446411133,197.8749084472656,197.8749084472656,198.252555847168,198.252555847168,198.252555847168,198.5358200073242,198.5358200073242,198.5358200073242,198.5358200073242,196.4853973388672,196.7241592407227,196.7241592407227,196.9928359985352,196.9928359985352,196.9928359985352,197.304817199707,197.304817199707,197.304817199707,197.6547622680664,198.0209350585938,198.0209350585938,198.0209350585938,198.3999557495117,198.3999557495117,198.5977020263672,198.5977020263672,198.5977020263672,198.5977020263672,196.6492156982422,196.6492156982422,196.6492156982422,196.8973388671875,196.8973388671875,197.2095794677734,197.5414428710938,197.8989486694336,197.8989486694336,198.2576217651367,198.2576217651367,198.6377182006836,198.6377182006836,198.6377182006836,198.6584625244141,198.6584625244141,196.5923233032227,196.5923233032227,196.8246536254883,196.8246536254883,197.0792541503906,197.0792541503906,197.3740539550781,197.712043762207,197.712043762207,197.712043762207,198.0760345458984,198.4480285644531,198.4480285644531,198.718391418457,198.718391418457,198.718391418457,198.718391418457,198.718391418457,198.718391418457,196.7734756469727,196.7734756469727,197.012336730957,197.2829208374023,197.5977172851562,197.9484252929688,197.9484252929688,198.3159637451172,198.6988296508789,198.7772369384766,198.7772369384766,198.7772369384766,196.7524490356445,196.7524490356445,196.9814758300781,197.2334594726562,197.2334594726562,197.5232772827148,197.5232772827148,197.8559951782227,197.8559951782227,198.2163009643555,198.6272430419922,198.6272430419922,198.8351821899414,198.8351821899414,198.8351821899414,198.8351821899414,198.8351821899414,198.8351821899414,196.9803848266602,196.9803848266602,197.2210922241211,197.2210922241211,197.4923553466797,197.8093338012695,198.1560592651367,198.1560592651367,198.5224685668945,198.8921737670898,198.8921737670898,198.8921737670898,198.8921737670898,198.8921737670898,198.8921737670898,196.970947265625,196.970947265625,197.2029190063477,197.2029190063477,197.4602813720703,197.7598876953125,197.7598876953125,198.0977172851562,198.0977172851562,198.4623718261719,198.836784362793,198.836784362793,198.836784362793,198.9482421875,198.9482421875,198.9482421875,198.9482421875,198.9482421875,198.9482421875,197.2189102172852,197.2189102172852,197.4661712646484,197.4661712646484,197.752197265625,197.752197265625,198.0796966552734,198.4352645874023,198.8059158325195,198.8059158325195,199.0033950805664,199.0033950805664,199.0033950805664,199.0033950805664,197.271842956543,197.271842956543,197.5176849365234,197.5176849365234,197.8030471801758,197.8030471801758,198.1322402954102,198.1322402954102,198.4926986694336,198.8664321899414,198.8664321899414,199.0576858520508,199.0576858520508,199.0576858520508,199.0576858520508,199.0576858520508,199.0576858520508,197.3393096923828,197.3393096923828,197.5813598632812,197.8576889038086,197.8576889038086,197.8576889038086,198.1770935058594,198.1770935058594,198.5310287475586,198.5310287475586,198.8992919921875,198.8992919921875,199.1111068725586,199.1111068725586,199.1111068725586,199.1111068725586,199.1111068725586,199.1111068725586,199.1111068725586,199.1111068725586,199.1111068725586,199.1111068725586,199.1111068725586,199.1111068725586,199.1111068725586,199.1111068725586,199.1111068725586,199.1111068725586,199.1111068725586,199.1111068725586,197.3845367431641,197.605583190918,197.605583190918,197.8516387939453,197.8516387939453,198.1264038085938,198.1264038085938,198.1264038085938,198.4424896240234,198.7882995605469,198.7882995605469,199.1497573852539,199.1497573852539,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,199.1634674072266,197.3550720214844,197.3550720214844,197.3550720214844,197.3550720214844,197.3550720214844,197.3550720214844,197.3768768310547,197.3768768310547,197.6307220458984,197.6307220458984,197.9010238647461,198.2080612182617,198.2080612182617,198.2080612182617,198.5460433959961,198.5460433959961,198.5460433959961,198.8796539306641,199.204460144043,199.5865783691406,199.5865783691406,200.0037078857422,200.0037078857422,200.425422668457,200.425422668457,200.8461761474609,200.8461761474609,201.2429122924805,201.2429122924805,201.5843734741211,201.5843734741211,201.926025390625,202.2676773071289,202.2676773071289,202.610237121582,202.610237121582,202.9534072875977,203.2925262451172,203.2925262451172,203.6323699951172,203.6323699951172,203.9732208251953,204.3122177124023,204.6515960693359,204.8808822631836,204.8808822631836,204.8808822631836,204.8808822631836,204.8808822631836,204.8808822631836,197.7329025268555,197.7329025268555,197.9986267089844,198.2963562011719,198.2963562011719,198.6292343139648,198.6292343139648,198.9716262817383,198.9716262817383,199.3000640869141,199.6701431274414,199.6701431274414,200.0624008178711,200.4790878295898,200.4790878295898,200.9035339355469,201.3299865722656,201.3299865722656,201.7556762695312,201.7556762695312,202.1810989379883,202.6060333251953,202.6060333251953,203.0313873291016,203.4563903808594,203.880012512207,203.880012512207,204.3045349121094,204.3045349121094,204.7205276489258,204.7205276489258,205.0866317749023,205.0866317749023,205.0866317749023,205.0866317749023,205.0866317749023,205.0866317749023,198.2149963378906,198.2149963378906,198.4929504394531,198.4929504394531,198.8049240112305,198.8049240112305,199.1360626220703,199.1360626220703,199.4574127197266,199.8224029541016,200.2062225341797,200.6091995239258,200.6091995239258,200.6091995239258,201.0260543823242,201.4518051147461,201.4518051147461,201.8735656738281,202.2981414794922,202.2981414794922,202.7203903198242,203.1862106323242,203.1862106323242,203.6092834472656,204.032356262207,204.032356262207,204.456672668457,204.456672668457,204.8729629516602,205.2742004394531,205.2742004394531,205.2891845703125,205.2891845703125,205.2891845703125,205.2891845703125,198.4754409790039,198.4754409790039,198.7374420166016,198.7374420166016,199.0253448486328,199.3348999023438,199.3348999023438,199.6446151733398,199.6446151733398,199.9997634887695,199.9997634887695,200.3663558959961,200.3663558959961,200.3663558959961,200.7536544799805,200.7536544799805,201.1642608642578,201.1642608642578,201.5827026367188,202.0017700195312,202.0017700195312,202.3716735839844,202.3716735839844,202.6418609619141,203.0577850341797,203.0577850341797,203.4754180908203,203.4754180908203,203.8950042724609,203.8950042724609,204.3164749145508,204.3164749145508,204.7365798950195,204.7365798950195,205.1471939086914,205.1471939086914,205.4884796142578,205.4884796142578,205.4884796142578,205.4884796142578,205.4884796142578,205.4884796142578,205.4884796142578,205.4884796142578,205.4884796142578,198.8093414306641,199.0783004760742,199.0783004760742,199.0783004760742,199.3727951049805,199.3727951049805,199.709114074707,200.043571472168,200.043571472168,200.4044036865234,200.4044036865234,200.7813034057617,200.7813034057617,201.1827850341797,201.1827850341797,201.1827850341797,201.5983581542969,202.0182037353516,202.4335861206055,202.4335861206055,202.819953918457,202.819953918457,203.2335662841797,203.2335662841797,203.6505508422852,204.0689926147461,204.4873504638672,204.4873504638672,204.9056777954102,204.9056777954102,205.3168029785156,205.3168029785156,205.684440612793,205.684440612793,205.684440612793,205.684440612793,205.684440612793,205.684440612793,205.684440612793,205.684440612793,205.684440612793,199.1003952026367,199.3633575439453,199.3633575439453,199.644775390625,199.9349060058594,199.9349060058594,200.2631683349609,200.6208190917969,200.9860229492188,200.9860229492188,201.3739624023438,201.3739624023438,201.7841186523438,201.7841186523438,202.2039642333984,202.6173858642578,202.6173858642578,203.0027618408203,203.0027618408203,203.0027618408203,203.4158782958984,203.8291168212891,204.2419662475586,204.2419662475586,204.6573715209961,205.0737152099609,205.0737152099609,205.4841384887695,205.4841384887695,205.8773803710938,205.8773803710938,205.8773803710938,205.8773803710938,205.8773803710938,205.8773803710938,199.4026336669922,199.4026336669922,199.662483215332,199.662483215332,199.662483215332,199.9333953857422,199.9333953857422,200.2105407714844,200.5466995239258,200.5466995239258,200.9031448364258,201.2663803100586,201.651611328125,202.0549011230469,202.4648742675781,202.4648742675781,202.8777084350586,203.2882080078125,203.2882080078125,203.701057434082,203.701057434082,204.1172714233398,204.5340270996094,204.5340270996094,204.9510879516602,205.3691864013672,205.7757110595703,205.7757110595703,206.0670623779297,206.0670623779297,206.0670623779297,206.0670623779297,206.0670623779297,206.0670623779297,206.0670623779297,206.0670623779297,206.0670623779297,206.0670623779297,206.0670623779297,206.0670623779297,206.0670623779297,206.0670623779297,206.0670623779297,206.0670623779297,199.6343383789062,199.6343383789062,199.8650665283203,199.8650665283203,200.1109085083008,200.3587493896484,200.6768569946289,200.6768569946289,200.6768569946289,201.0078125,201.0078125,201.3559112548828,201.3559112548828,201.7141036987305,201.7141036987305,202.0987014770508,202.0987014770508,202.5003890991211,202.5003890991211,202.9150161743164,203.3251190185547,203.3251190185547,203.7368392944336,203.7368392944336,204.1521911621094,204.5663375854492,204.9819488525391,204.9819488525391,205.3991088867188,205.3991088867188,205.8125152587891,205.8125152587891,205.8125152587891,206.2122344970703,206.2122344970703,206.2537994384766,206.2537994384766,206.2537994384766,206.2537994384766,199.9210968017578,199.9210968017578,200.174690246582,200.174690246582,200.4315567016602,200.4315567016602,200.7056579589844,200.7056579589844,200.7056579589844,201.0321960449219,201.0321960449219,201.3830413818359,201.7425231933594,201.7425231933594,202.1182403564453,202.1182403564453,202.512336730957,202.512336730957,202.9217529296875,202.9217529296875,203.3356170654297,203.7470016479492,203.7470016479492,204.1602325439453,204.5761260986328,204.5761260986328,204.9940948486328,204.9940948486328,205.4124298095703,205.8325576782227,205.8325576782227,206.2356338500977,206.2356338500977,206.4374160766602,206.4374160766602,206.4374160766602,206.4374160766602,206.4374160766602,206.4374160766602,206.4374160766602,206.4374160766602,206.4374160766602,200.3821487426758,200.3821487426758,200.6324462890625,200.8946151733398,201.2081527709961,201.2081527709961,201.5520629882812,201.5520629882812,201.9064025878906,202.2741317749023,202.6655120849609,203.0739822387695,203.0739822387695,203.0739822387695,203.4902496337891,203.4902496337891,203.9029083251953,203.9029083251953,204.318603515625,204.318603515625,204.7360153198242,205.1549224853516,205.1549224853516,205.574836730957,205.574836730957,205.9940490722656,206.3987197875977,206.3987197875977,206.6182327270508,206.6182327270508,206.6182327270508,206.6182327270508,206.6182327270508,206.6182327270508,206.6182327270508,206.6182327270508,206.6182327270508,200.6159820556641,200.6159820556641,200.8605880737305,200.8605880737305,201.0908584594727,201.3953704833984,201.7294235229492,202.0797271728516,202.4398727416992,202.4398727416992,202.8200073242188,203.2182998657227,203.2182998657227,203.2182998657227,203.6321029663086,204.0429534912109,204.4543685913086,204.4543685913086,204.8688507080078,204.8688507080078,205.2847366333008,205.2847366333008,205.702018737793,206.1176528930664,206.1176528930664,206.5244750976562,206.7959976196289,206.7959976196289,206.7959976196289,206.7959976196289,206.7959976196289,206.7959976196289,200.880729675293,201.1216583251953,201.3795928955078,201.3795928955078,201.685173034668,202.023078918457,202.3739776611328,202.3739776611328,202.7300796508789,203.108154296875,203.108154296875,210.8632736206055,210.8632736206055,210.8632736206055,210.8632736206055,210.8632736206055,210.8632736206055,210.8632736206055,210.8632736206055,210.8632736206055,210.8632736206055,210.8632736206055,210.8632736206055,210.8632736206055,210.8632736206055,210.8632736206055,210.8632736206055,210.8632736206055,210.8632736206055,210.8632736206055,210.8632736206055,218.4926681518555,218.49267578125,218.49267578125,218.49267578125,218.49267578125,218.49267578125,218.49267578125,218.49267578125,218.49267578125,218.49267578125,218.49267578125,218.49267578125,218.49267578125,218.49267578125,218.49267578125,218.49267578125,218.49267578125,218.49267578125,218.49267578125,218.49267578125,218.49267578125,218.49267578125,218.49267578125,233.75146484375,233.75146484375,233.75146484375,233.75146484375,233.75146484375,233.75146484375,233.75146484375,233.75146484375,233.75146484375,233.75146484375,233.75146484375,233.75146484375,233.75146484375,233.75146484375,233.75146484375,233.75146484375,241.3808822631836,241.3808822631836,241.3808822631836,241.3808822631836,241.3808822631836,241.3808822631836,241.3808822631836,241.3808822631836,241.4455795288086,241.4455795288086,241.4455795288086,241.4455795288086,241.4455795288086,241.4455795288086,241.4455795288086,241.4455795288086,241.4455795288086,241.4455795288086,241.4455795288086,241.4455795288086,241.4455795288086,241.4455795288086,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078,256.7760772705078],"meminc":[0,0,0,0,15.28223419189453,0,0,0,0.0003662109375,0,0,30.46538543701172,0,0,0,0,0,4.57763671875e-05,0,-0.000152587890625,0,0,0,0,0,0,0,0,0,0,0,0,0,-0.00016021728515625,0,15.29883575439453,0,0.2446136474609375,0.25970458984375,0,0.2837448120117188,0,0.3214187622070312,0.353179931640625,0.3956298828125,0.397308349609375,0,0.4174423217773438,0,0.3338623046875,0,-2.718070983886719,0,0.3740081787109375,0,0.400787353515625,0.4287948608398438,0.4211578369140625,0,0.416107177734375,0.3965225219726562,0,0.3446426391601562,0,0,-2.701438903808594,0,0.3625335693359375,0.3780441284179688,0.403350830078125,0.4119110107421875,0.4049530029296875,0,0,0.4058761596679688,0,0,0.4079971313476562,0,-2.718513488769531,0,0.360931396484375,0,0.3821029663085938,0.4043426513671875,0.4167709350585938,0,0.413299560546875,0.4140090942382812,0.4152450561523438,0,0,-2.672744750976562,0.3606033325195312,0.3762893676757812,0.3928985595703125,0.4109573364257812,0.4098434448242188,0.411163330078125,0,0,0.3897705078125,0,0,-2.619712829589844,0,0.33306884765625,0,0.3711166381835938,0,0.3830642700195312,0,0.404510498046875,0,0.4019927978515625,0,0.40545654296875,0.3980331420898438,0,-2.603004455566406,0.3739852905273438,0,0.369049072265625,0,0.3796005249023438,0.3844528198242188,0,0.3993301391601562,0,0.3943557739257812,0,0.3784408569335938,0,-2.568443298339844,0,0,0.3299331665039062,0.3584442138671875,0,0.3719863891601562,0.38885498046875,0.3998641967773438,0.4024810791015625,0.391845703125,0,-2.523170471191406,0.3300094604492188,0,0.3564071655273438,0,0.3669204711914062,0,0,0.3832931518554688,0.394989013671875,0,0.3695068359375,0,0,0.3958969116210938,0,0,-2.499565124511719,0.3227996826171875,0.3517303466796875,0.3653030395507812,0,0.38726806640625,0,0,0.3974990844726562,0.4019393920898438,0.34564208984375,0,-2.419403076171875,0,0,0.3277969360351562,0,0,0.35552978515625,0,0.3720169067382812,0,0.368682861328125,0.4003982543945312,0,0.4055633544921875,0.2608642578125,0,-2.362564086914062,0,0.3168563842773438,0,0.3799362182617188,0,0.3646316528320312,0,0.3797607421875,0.376220703125,0.3865585327148438,0,0.2288360595703125,0,-2.269569396972656,0.3243331909179688,0.3476791381835938,0,0.3627700805664062,0.378204345703125,0.398223876953125,0.4018478393554688,0.1257553100585938,0,0,-2.145378112792969,0,0.331298828125,0,0.354095458984375,0,0.369171142578125,0.3861312866210938,0,0.4016647338867188,0,0.3709640502929688,0,0,-2.296226501464844,0,0,0.2976150512695312,0,0.3275909423828125,0,0.3546218872070312,0,0.3690567016601562,0,0,0.384613037109375,0.3972930908203125,0,0.2323837280273438,0,-2.159721374511719,0,0.2774658203125,0,0.3370285034179688,0,0.3615493774414062,0,0.3763275146484375,0,0.3902740478515625,0,0.4001388549804688,0.0827789306640625,0,0,-1.983978271484375,0,0.3221588134765625,0,0.34844970703125,0,0.3716583251953125,0.3879318237304688,0.4051055908203125,0,0.2134933471679688,0,-2.07427978515625,0,0.31182861328125,0,0,0.3354873657226562,0.36004638671875,0.3815155029296875,0,0.3972320556640625,0.3518905639648438,0,0,-2.158935546875,0,0.2996444702148438,0.3200836181640625,0,0.3532180786132812,0.3726577758789062,0.3896102905273438,0.4073104858398438,0,0.07912445068359375,0,0,-1.902786254882812,0,0.3077545166015625,0,0.3422393798828125,0.3640594482421875,0,0.3876266479492188,0,0.4009475708007812,0,0.1618499755859375,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2.105339050292969,0,0.2035293579101562,0,0.22918701171875,0,0.2481307983398438,0,0,0.28021240234375,0,0.313751220703125,0.3421783447265625,0,0.3561859130859375,0.1925430297851562,0,0,-1.989402770996094,0,0.2621612548828125,0,0.3052291870117188,0.3469314575195312,0.3668746948242188,0,0.3865280151367188,0.3813705444335938,0,0,-2.043647766113281,0.2813949584960938,0.3037490844726562,0.3446731567382812,0,0.3675994873046875,0,0.3862075805664062,0.4032440185546875,0.01561737060546875,0,0,-1.754447937011719,0,0.3013229370117188,0.343902587890625,0,0.3693618774414062,0,0,0.389251708984375,0.4024734497070312,0.00592041015625,0,-1.725067138671875,0,0.3006134033203125,0,0.3435287475585938,0.36767578125,0,0.3878173828125,0,0.3823471069335938,0,0,-1.920547485351562,0,0.2746734619140625,0.3029861450195312,0,0.3455734252929688,0,0.3662185668945312,0,0.3861846923828125,0,0,0.3009262084960938,0,0,-1.864906311035156,0,0.2719802856445312,0,0.3032455444335938,0,0,0.3309402465820312,0,0.3656768798828125,0,0.3892669677734375,0,0.2588348388671875,0,-1.805610656738281,0,0.275543212890625,0,0.3131790161132812,0,0.352935791015625,0.3693084716796875,0,0.3920135498046875,0,0.1568756103515625,0,-1.730201721191406,0,0.276031494140625,0.3172454833984375,0,0.3533706665039062,0,0.3731765747070312,0.3888015747070312,0.07485198974609375,0,0,-1.623046875,0,0.2912979125976562,0,0.3338394165039062,0.3617477416992188,0,0.3828659057617188,0,0.30572509765625,0,0,-1.732444763183594,0,0.2739181518554688,0.3094329833984375,0,0.350555419921875,0,0,0.37286376953125,0,0.387115478515625,0,0.09020233154296875,0,0,-1.597923278808594,0.2835006713867188,0,0.325286865234375,0.3598098754882812,0,0.3809356689453125,0,0.2991867065429688,0,0,-1.701957702636719,0,0.267303466796875,0.3038711547851562,0,0.3466262817382812,0.3682708740234375,0,0.3887252807617188,0,0.0770263671875,0,0,-1.513267517089844,0,0.2889633178710938,0,0.3348464965820312,0,0.3623428344726562,0,0.385162353515625,0,0.191131591796875,0,0,-1.56768798828125,0,0.2806167602539062,0,0.3251266479492188,0,0.3585433959960938,0,0.3785247802734375,0.2732086181640625,0,0,-1.598052978515625,0,0.268829345703125,0,0,0.308258056640625,0.3847427368164062,0,0.371612548828125,0,0,0.312164306640625,0,0,-1.594596862792969,0,0.2684326171875,0.304473876953125,0,0.3490219116210938,0,0.3683700561523438,0.35107421875,0,0,-1.597244262695312,0,0.2700042724609375,0,0.3048248291015625,0,0.3477859497070312,0,0.3697280883789062,0,0.3509521484375,0,0,-1.579612731933594,0.2645416259765625,0,0.3037490844726562,0,0.3450088500976562,0,0.3213043212890625,0,0.3795242309570312,0,0.010711669921875,0,0,-1.34344482421875,0,0,0.2905731201171875,0,0.32305908203125,0,0.3630599975585938,0,0.3781051635742188,0.0332183837890625,0,0,-1.344535827636719,0.2833251953125,0,0.3292160034179688,0,0.3587265014648438,0.378814697265625,0,0.03826141357421875,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.509559631347656,0,0,0.02664947509765625,0,0,0.2535400390625,0,0.26953125,0,0.3055191040039062,0,0.326019287109375,0.3225479125976562,0,0,0.362457275390625,0.4032974243164062,0,0.4186859130859375,0,0.3455123901367188,0.3448104858398438,0,0.3428802490234375,0.34149169921875,0,0.3431015014648438,0,0.3423080444335938,0,0.0277099609375,0,-4.361709594726562,0.3433151245117188,0,0.3671646118164062,0.3433380126953125,0.3781814575195312,0,0,0.4032440185546875,0,0.4114761352539062,0,0.4208450317382812,0.4221954345703125,0.4229049682617188,0.4229965209960938,0,0.41156005859375,0,0.1450653076171875,0,0,-4.419776916503906,0,0.3079452514648438,0,0.3442840576171875,0,0.3403396606445312,0.3531723022460938,0,0,0.426971435546875,0.4013137817382812,0.4140777587890625,0,0.42095947265625,0,0.41937255859375,0,0.419036865234375,0,0.4158782958984375,0,0.2849884033203125,0,0,0,0,0,-4.129837036132812,0,0.32965087890625,0.3013687133789062,0,0.3388214111328125,0,0.3752365112304688,0.3905792236328125,0,0.4070892333984375,0,0,0.41778564453125,0.4200897216796875,0,0.4229660034179688,0.4224853515625,0,0.4063949584960938,0.02376556396484375,0,-4.173965454101562,0,0.3137588500976562,0,0.3268661499023438,0,0.3389205932617188,0.3714218139648438,0,0.3879623413085938,0,0.4029541015625,0,0.4144287109375,0,0.4197235107421875,0,0.4220352172851562,0,0.4220199584960938,0,0.4086837768554688,0,0.06966400146484375,0,0,-4.146858215332031,0,0.3046035766601562,0,0.318817138671875,0,0.3388442993164062,0,0.3661041259765625,0.420013427734375,0.40032958984375,0.4096908569335938,0,0.41680908203125,0.4198532104492188,0,0.4204254150390625,0,0.4048233032226562,0,0.04891204833984375,0,-4.068771362304688,0,0.3005752563476562,0,0.3091888427734375,0,0.3472671508789062,0.3695831298828125,0,0,0.3837738037109375,0,0,0.3788528442382812,0,0.3999481201171875,0.4056854248046875,0,0.4142379760742188,0.4190597534179688,0,0.4066238403320312,0.05438995361328125,0,0,-4.0120849609375,0,0.294464111328125,0,0.293060302734375,0,0,0.3433990478515625,0,0.3638076782226562,0.3800125122070312,0,0.39501953125,0,0,0.406219482421875,0,0.4159317016601562,0.420989990234375,0.4217681884765625,0,0.3959274291992188,0,0,0,-3.899993896484375,0,0.2909698486328125,0,0.3049774169921875,0.3910980224609375,0,0,0.3727188110351562,0,0.38116455078125,0.3984527587890625,0,0.4085540771484375,0,0.4006195068359375,0.4168853759765625,0,0,0.4152145385742188,0,0.2359542846679688,0,0,0,0,0,-3.733932495117188,0.2846145629882812,0,0.3275604248046875,0,0.3581619262695312,0,0.3672561645507812,0,0.3871078491210938,0,0,0.397796630859375,0,0.4075088500976562,0.414947509765625,0,0.418670654296875,0.4073562622070312,0.07755279541015625,0,-3.843315124511719,0.2682571411132812,0,0.3006362915039062,0.34954833984375,0,0.3684310913085938,0.3806228637695312,0,0.3935317993164062,0.3798141479492188,0,0.4076080322265625,0,0.4178085327148438,0,0.4167556762695312,0,0.2732162475585938,0,0,0,0,0,-3.644927978515625,0,0.3037643432617188,0,0.3097763061523438,0.3486251831054688,0,0,0.3588180541992188,0,0.376220703125,0.3893356323242188,0.4019012451171875,0,0.4123611450195312,0,0.41839599609375,0.4049301147460938,0,0.03177642822265625,0,0,-3.695907592773438,0,0.26715087890625,0.3035659790039062,0,0.3423538208007812,0.3337554931640625,0,0.340179443359375,0,0.3771133422851562,0,0.3997879028320312,0.4083404541015625,0.4173812866210938,0,0.416961669921875,0,0.1985015869140625,0,-3.749191284179688,0.262969970703125,0.2811737060546875,0,0.3265228271484375,0,0.3537521362304688,0,0.3623428344726562,0,0.378326416015625,0,0.3960494995117188,0,0.4074554443359375,0,0.4161148071289062,0,0.4184722900390625,0,0.2535552978515625,0,0,0,0,0,-3.441864013671875,0,0,0.28021240234375,0,0.3235931396484375,0,0.3488311767578125,0,0.364288330078125,0,0.3760604858398438,0,0.3970870971679688,0,0.4071731567382812,0.4165802001953125,0.417236328125,0,0.216461181640625,0,0,0,-3.422782897949219,0.2708282470703125,0.3124923706054688,0,0.3375778198242188,0.3576431274414062,0,0,0.3718109130859375,0,0.3936309814453125,0,0.4016494750976562,0,0.4110183715820312,0.4154510498046875,0,0.254791259765625,0,0,0,-3.355712890625,0,0.256561279296875,0,0.3046340942382812,0,0,0.3328781127929688,0,0.3567886352539062,0,0.3637619018554688,0.3851165771484375,0,0.4011611938476562,0,0.4126968383789062,0,0.414825439453125,0,0.2296371459960938,0,-3.513885498046875,0,0,0.24920654296875,0,0.2751312255859375,0,0,0.3067626953125,0.3363876342773438,0,0.3604278564453125,0.3661651611328125,0,0.39154052734375,0.405303955078125,0,0.4148025512695312,0.4113388061523438,0,0,0.09755706787109375,0,0,-3.399215698242188,0,0.2472991943359375,0,0.282989501953125,0.310302734375,0,0.3422470092773438,0.3612060546875,0,0.3729248046875,0.393829345703125,0.4071502685546875,0,0.4174575805664062,0.3628997802734375,0,0,0,0,0,-3.267471313476562,0,0.2559585571289062,0.2829818725585938,0.314453125,0.3472137451171875,0,0.3646469116210938,0,0,0.3818130493164062,0,0.398345947265625,0,0.4108505249023438,0.4140701293945312,0,0.1945953369140625,0,0,-3.3336181640625,0.2424545288085938,0,0.2681121826171875,0.2945175170898438,0.329498291015625,0,0.3584747314453125,0.3651885986328125,0,0.385528564453125,0,0,0.40325927734375,0,0.4130783081054688,0,0.3693771362304688,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-3.148971557617188,0.206329345703125,0,0,0.2323150634765625,0,0.2468719482421875,0,0.3107681274414062,0.3209609985351562,0,0.3418807983398438,0,0.3569183349609375,0.379150390625,0,0.4001235961914062,0,0.4039154052734375,0,0,0.043701171875,0,0,0,-3.171798706054688,0,0.2409744262695312,0,0.2538909912109375,0,0,0.277984619140625,0,0.3168563842773438,0,0.3467941284179688,0,0.3560104370117188,0,0.3794021606445312,0,0.4049835205078125,0,0.4110946655273438,0,0.2766189575195312,0,0,0,-3.0181884765625,0,0.2553787231445312,0.2824630737304688,0,0,0.3181838989257812,0.3524627685546875,0,0.36358642578125,0.3799057006835938,0,0.4024124145507812,0,0.4089431762695312,0.3462600708007812,0,0,0,-3.01153564453125,0.2482986450195312,0,0.3059234619140625,0,0.3122787475585938,0,0.3485183715820312,0,0,0.3598785400390625,0,0.3758773803710938,0,0.3979949951171875,0,0,0.408660888671875,0,0.34393310546875,0,0,0,0,0,-2.962997436523438,0,0.2461929321289062,0,0.2734222412109375,0,0.3084335327148438,0,0.3436508178710938,0.361602783203125,0,0.3762664794921875,0,0.39794921875,0,0,0.4097061157226562,0,0.3341751098632812,0,0,0,-2.908287048339844,0,0.246368408203125,0,0.275146484375,0.3104171752929688,0.3472671508789062,0.3621978759765625,0,0.3770980834960938,0,0.398529052734375,0,0.4095230102539062,0,0.2688446044921875,0,0,0,0,0,-2.828666687011719,0,0.2442626953125,0.3012924194335938,0,0.312347412109375,0,0.3465652465820312,0.3616714477539062,0,0.3758773803710938,0,0.4014663696289062,0.40484619140625,0,0,0.1658401489257812,0,0,0,0,0,-2.721603393554688,0,0.2551040649414062,0,0.288726806640625,0.3282470703125,0,0.3571090698242188,0,0.3691558837890625,0.3838119506835938,0,0.4000701904296875,0.3952407836914062,0.02838134765625,0,0,0,-2.827980041503906,0,0.237640380859375,0,0.26318359375,0,0.2991714477539062,0,0.3360671997070312,0,0,0.3614501953125,0.373138427734375,0.393341064453125,0,0.4078826904296875,0.2389450073242188,0,0,0,0,0,-2.668853759765625,0,0.2497024536132812,0,0.27972412109375,0,0.3541107177734375,0,0.3533477783203125,0.3641586303710938,0,0.381134033203125,0.405364990234375,0,0.3627853393554688,0,0,0,-2.700576782226562,0,0.2412948608398438,0,0.2694778442382812,0,0.3067398071289062,0,0,0.3467178344726562,0,0.366058349609375,0,0.3776092529296875,0,0.40008544921875,0,0.40380859375,0,0,0.06899261474609375,0,-2.718032836914062,0.23358154296875,0,0.2583160400390625,0,0.2948532104492188,0.3341903686523438,0.3588027954101562,0.3687210083007812,0.3892288208007812,0,0.4074478149414062,0,0.15179443359375,0,0,0,0,0,-2.487403869628906,0.2527008056640625,0,0.2850265502929688,0.3273696899414062,0,0.3541107177734375,0,0.4028472900390625,0.3841629028320312,0.407470703125,0,0.1513137817382812,0,0,0,-2.450088500976562,0,0.25494384765625,0,0.2889938354492188,0,0.3317184448242188,0.3584671020507812,0,0.3693618774414062,0,0,0.3874282836914062,0.4062423706054688,0,0.1293258666992188,0,0,0,0,0,-2.39752197265625,0.2520599365234375,0,0.2890625,0.3303451538085938,0,0.3588943481445312,0,0.3703384399414062,0.3871841430664062,0,0.4062042236328125,0,0.0785980224609375,0,-2.554725646972656,0.2326812744140625,0,0.2581253051757812,0,0.2922439575195312,0.3349075317382812,0.3613739013671875,0,0.372467041015625,0.3907852172851562,0.3860549926757812,0,0,0,0,0,-2.433799743652344,0,0.238525390625,0,0.2691802978515625,0.3098220825195312,0,0.34814453125,0.3650588989257812,0.3790130615234375,0,0.400390625,0,0.1963882446289062,0,0,0,0,0,0,0,-2.308151245117188,0,0.246368408203125,0.2806549072265625,0.3250885009765625,0,0.3543014526367188,0,0.3658905029296875,0,0.3846054077148438,0.39447021484375,0,0.0284271240234375,0,-2.407600402832031,0.2346343994140625,0,0.2602310180664062,0,0,0.300811767578125,0.3414077758789062,0,0.3623580932617188,0,0.3712615966796875,0.3922348022460938,0,0.214996337890625,0,0,0,0,0,-2.229019165039062,0.24676513671875,0,0.282745361328125,0.3266677856445312,0,0.3591995239257812,0,0.3704299926757812,0.3880386352539062,0,0.3245162963867188,0,0,0,-2.27777099609375,0,0.238311767578125,0,0.2700424194335938,0,0.3038177490234375,0,0.340179443359375,0.3595504760742188,0.3690261840820312,0,0.391510009765625,0,0,0.0735015869140625,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2.345977783203125,0,0,0.03844451904296875,0,0.2064132690429688,0.2341461181640625,0.2543487548828125,0,0.2928848266601562,0,0.3306121826171875,0.339019775390625,0.3601837158203125,0,0.3567581176757812,0,0,0,0,0,-2.215164184570312,0,0,0.2383499145507812,0.2657241821289062,0.3078765869140625,0,0.34423828125,0.3635406494140625,0.3778610229492188,0,0.3835906982421875,0,0,0,0,0,-2.205459594726562,0,0.2353744506835938,0,0.259765625,0.3034744262695312,0,0,0.3411026000976562,0.365692138671875,0.3771209716796875,0,0.387847900390625,0,0,0,-2.150985717773438,0,0.23614501953125,0.2627639770507812,0,0.3066558837890625,0.342926025390625,0.3630599975585938,0,0.3765945434570312,0,0.326751708984375,0,0,0,0,0,-2.113304138183594,0,0.2365570068359375,0,0.2636184692382812,0.305816650390625,0,0.3447799682617188,0.3644638061523438,0,0.3776473999023438,0,0,0.28326416015625,0,0,0,-2.050422668457031,0.2387619018554688,0,0.2686767578125,0,0,0.311981201171875,0,0,0.349945068359375,0.3661727905273438,0,0,0.3790206909179688,0,0.1977462768554688,0,0,0,-1.948486328125,0,0,0.2481231689453125,0,0.3122406005859375,0.3318634033203125,0.3575057983398438,0,0.358673095703125,0,0.380096435546875,0,0,0.02074432373046875,0,-2.066139221191406,0,0.232330322265625,0,0.2546005249023438,0,0.2947998046875,0.3379898071289062,0,0,0.3639907836914062,0.3719940185546875,0,0.2703628540039062,0,0,0,0,0,-1.944915771484375,0,0.238861083984375,0.2705841064453125,0.3147964477539062,0.3507080078125,0,0.3675384521484375,0.3828659057617188,0.07840728759765625,0,0,-2.024787902832031,0,0.2290267944335938,0.251983642578125,0,0.2898178100585938,0,0.3327178955078125,0,0.3603057861328125,0.4109420776367188,0,0.2079391479492188,0,0,0,0,0,-1.85479736328125,0,0.2407073974609375,0,0.2712631225585938,0.3169784545898438,0.3467254638671875,0,0.3664093017578125,0.3697052001953125,0,0,0,0,0,-1.921226501464844,0,0.2319717407226562,0,0.2573623657226562,0.2996063232421875,0,0.33782958984375,0,0.364654541015625,0.3744125366210938,0,0,0.1114578247070312,0,0,0,0,0,-1.729331970214844,0,0.2472610473632812,0,0.2860260009765625,0,0.3274993896484375,0.3555679321289062,0.3706512451171875,0,0.197479248046875,0,0,0,-1.731552124023438,0,0.2458419799804688,0,0.2853622436523438,0,0.329193115234375,0,0.3604583740234375,0.3737335205078125,0,0.191253662109375,0,0,0,0,0,-1.718376159667969,0,0.2420501708984375,0.2763290405273438,0,0,0.3194046020507812,0,0.3539352416992188,0,0.3682632446289062,0,0.2118148803710938,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.726570129394531,0.2210464477539062,0,0.2460556030273438,0,0.2747650146484375,0,0,0.3160858154296875,0.3458099365234375,0,0.3614578247070312,0,0.01371002197265625,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.808395385742188,0,0,0,0,0,0.0218048095703125,0,0.25384521484375,0,0.2703018188476562,0.307037353515625,0,0,0.337982177734375,0,0,0.3336105346679688,0.3248062133789062,0.3821182250976562,0,0.4171295166015625,0,0.4217147827148438,0,0.4207534790039062,0,0.3967361450195312,0,0.341461181640625,0,0.3416519165039062,0.3416519165039062,0,0.342559814453125,0,0.343170166015625,0.3391189575195312,0,0.33984375,0,0.340850830078125,0.3389968872070312,0.3393783569335938,0.2292861938476562,0,0,0,0,0,-7.147979736328125,0,0.2657241821289062,0.2977294921875,0,0.3328781127929688,0,0.3423919677734375,0,0.3284378051757812,0.3700790405273438,0,0.3922576904296875,0.41668701171875,0,0.4244461059570312,0.42645263671875,0,0.425689697265625,0,0.4254226684570312,0.4249343872070312,0,0.42535400390625,0.4250030517578125,0.4236221313476562,0,0.4245223999023438,0,0.4159927368164062,0,0.3661041259765625,0,0,0,0,0,-6.871635437011719,0,0.2779541015625,0,0.3119735717773438,0,0.3311386108398438,0,0.32135009765625,0.364990234375,0.383819580078125,0.4029769897460938,0,0,0.4168548583984375,0.425750732421875,0,0.4217605590820312,0.4245758056640625,0,0.4222488403320312,0.4658203125,0,0.4230728149414062,0.4230728149414062,0,0.42431640625,0,0.416290283203125,0.4012374877929688,0,0.014984130859375,0,0,0,-6.813743591308594,0,0.2620010375976562,0,0.28790283203125,0.3095550537109375,0,0.3097152709960938,0,0.3551483154296875,0,0.3665924072265625,0,0,0.387298583984375,0,0.4106063842773438,0,0.4184417724609375,0.4190673828125,0,0.369903564453125,0,0.2701873779296875,0.415924072265625,0,0.417633056640625,0,0.419586181640625,0,0.4214706420898438,0,0.42010498046875,0,0.410614013671875,0,0.3412857055664062,0,0,0,0,0,0,0,0,-6.67913818359375,0.2689590454101562,0,0,0.29449462890625,0,0.3363189697265625,0.3344573974609375,0,0.3608322143554688,0,0.3768997192382812,0,0.4014816284179688,0,0,0.4155731201171875,0.4198455810546875,0.4153823852539062,0,0.3863677978515625,0,0.4136123657226562,0,0.4169845581054688,0.4184417724609375,0.4183578491210938,0,0.4183273315429688,0,0.4111251831054688,0,0.3676376342773438,0,0,0,0,0,0,0,0,-6.58404541015625,0.2629623413085938,0,0.2814178466796875,0.290130615234375,0,0.3282623291015625,0.3576507568359375,0.365203857421875,0,0.387939453125,0,0.41015625,0,0.4198455810546875,0.413421630859375,0,0.3853759765625,0,0,0.413116455078125,0.413238525390625,0.4128494262695312,0,0.4154052734375,0.4163436889648438,0,0.4104232788085938,0,0.3932418823242188,0,0,0,0,0,-6.474746704101562,0,0.2598495483398438,0,0,0.2709121704101562,0,0.2771453857421875,0.3361587524414062,0,0.3564453125,0.3632354736328125,0.3852310180664062,0.403289794921875,0.40997314453125,0,0.4128341674804688,0.4104995727539062,0,0.4128494262695312,0,0.4162139892578125,0.4167556762695312,0,0.4170608520507812,0.4180984497070312,0.406524658203125,0,0.291351318359375,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-6.432723999023438,0,0.2307281494140625,0,0.2458419799804688,0.2478408813476562,0.3181076049804688,0,0,0.3309555053710938,0,0.3480987548828125,0,0.3581924438476562,0,0.3845977783203125,0,0.4016876220703125,0,0.4146270751953125,0.4101028442382812,0,0.4117202758789062,0,0.4153518676757812,0.4141464233398438,0.4156112670898438,0,0.4171600341796875,0,0.4134063720703125,0,0,0.39971923828125,0,0.04156494140625,0,0,0,-6.33270263671875,0,0.2535934448242188,0,0.256866455078125,0,0.2741012573242188,0,0,0.3265380859375,0,0.3508453369140625,0.3594818115234375,0,0.3757171630859375,0,0.3940963745117188,0,0.4094161987304688,0,0.4138641357421875,0.4113845825195312,0,0.4132308959960938,0.4158935546875,0,0.41796875,0,0.4183349609375,0.4201278686523438,0,0.403076171875,0,0.2017822265625,0,0,0,0,0,0,0,0,-6.055267333984375,0,0.2502975463867188,0.2621688842773438,0.31353759765625,0,0.3439102172851562,0,0.354339599609375,0.3677291870117188,0.3913803100585938,0.4084701538085938,0,0,0.4162673950195312,0,0.41265869140625,0,0.4156951904296875,0,0.4174118041992188,0.4189071655273438,0,0.4199142456054688,0,0.4192123413085938,0.4046707153320312,0,0.219512939453125,0,0,0,0,0,0,0,0,-6.002250671386719,0,0.2446060180664062,0,0.2302703857421875,0.3045120239257812,0.3340530395507812,0.3503036499023438,0.3601455688476562,0,0.3801345825195312,0.3982925415039062,0,0,0.4138031005859375,0.4108505249023438,0.4114151000976562,0,0.4144821166992188,0,0.4158859252929688,0,0.4172821044921875,0.4156341552734375,0,0.4068222045898438,0.2715225219726562,0,0,0,0,0,-5.915267944335938,0.2409286499023438,0.2579345703125,0,0.3055801391601562,0.3379058837890625,0.3508987426757812,0,0.3561019897460938,0.3780746459960938,0,7.755119323730469,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7.62939453125,7.62939453125e-06,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,15.2587890625,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7.629417419433594,0,0,0,0,0,0,0,0.064697265625,0,0,0,0,0,0,0,0,0,0,0,0,0,15.33049774169922,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"filename":["<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>","<expr>",null,null,null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,null,null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,null,null,null,null,null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,null,null,null,null,null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,null,null,null,"<expr>","<expr>","<expr>",null,null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,null,null,null,null,null,null,null,null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,null,null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>","<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,"<expr>","<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null]},"interval":10,"files":[{"filename":"<expr>","content":"## Generate Large Random Dataset\nn <- 2e6\nx <- runif(n)\ny <- runif(n)\nz <- runif(n)\nXYZ <- cbind(x,y,z)\n\n## Inspect 4 equivalent `row mean` calculations \nprofvis::profvis({\n    m <- rowSums(XYZ)/ncol(XYZ)\n    m <- rowMeans(XYZ)\n    m <- apply(XYZ, 1, mean)\n    m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }\n})\n## rowSums(), colSums(), rowMeans(), and colMeans() are vectorised and fast.\n## for loop is not the slowest, but the ugliest.","normpath":"<expr>"}],"prof_output":"/tmp/RtmpI5RvR8/file5d4d162a0f40.prof","highlight":{"output":["^output\\$"],"gc":["^<GC>$"],"stacktrace":["^\\.\\.stacktraceo(n|ff)\\.\\.$"]},"split":"h"}},"evals":[],"jsHooks":[]}</script>
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
##  mean1(x, 0.5) 19.81019 19.98727 20.18328 19.99339 20.00638 24.38967   100  a 
##  mean2(x, 0.5) 18.76901 19.13709 19.31324 19.14557 19.15610 22.41564   100   b
##  mean3(x, 0.5) 19.96706 19.97821 20.18777 19.98235 19.99009 27.45483   100  a
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

Before creating your own program, check if there is a faster or more memory efficient version. E.g., [data.table](https://cran.r-project.org/web/packages/data.table/vignettes/datatable-intro.html) or [Rfast2](https://cran.r-project.org/web/packages/Rfast2/index.html) for basic data manipulation.

```r
X <- cbind(1, runif(1e6))
Y <- X %*% c(1,2) + rnorm(1e6)
DAT <- as.data.frame(cbind(Y,X))

system.time({.lm.fit(X, Y) })
```

```
##    user  system elapsed 
##   0.109   0.000   0.036
```

```r
system.time({ lm(Y~X, data=DAT) })
```

```
##    user  system elapsed 
##   0.401   0.028   0.168
```
Note that quicker codes tend to have fewer checks and return less information. So you must know exactly what you are putting in and getting out.


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
##    expr       min        lq     mean    median        uq     max neval cld
##  ma1(y) 162.58422 167.52014 178.1510 181.79322 185.02579 192.884   100  a 
##  ma2(y)  19.42104  23.48483  30.2364  24.54786  27.40122 176.096   100   b
```
Likewise, matrix operations are often faster than vector operations.


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
##   0.025   0.004   0.029
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
##   0.846   0.208   0.596
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

