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
<div class="plotly html-widget html-fill-item" id="htmlwidget-fba9f5d61f232280a8cd" style="width:672px;height:480px;"></div>
<script type="application/json" data-for="htmlwidget-fba9f5d61f232280a8cd">{"x":{"visdat":{"20be44c59d45":["function () ","plotlyVisDat"]},"cur_data":"20be44c59d45","attrs":{"20be44c59d45":{"x":{},"y":{},"alpha_stroke":1,"sizes":[10,100],"spans":[1,20]}},"layout":{"margin":{"b":40,"l":60,"t":25,"r":10},"xaxis":{"domain":[0,1],"automargin":true,"title":"X"},"yaxis":{"domain":[0,1],"automargin":true,"title":"Y"},"hovermode":"closest","showlegend":false},"source":"A","config":{"modeBarButtonsToAdd":["hoverclosest","hovercompare"],"showSendToCloud":false},"data":[{"x":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100],"y":[4.0806380521789292,8.9119582708467355,12.266595226299486,17.355916954614035,17.574901878195284,19.543187474605944,26.752778015906113,34.762798225065865,36.295800263599503,40.903646991841882,44.056838343363751,46.531391812136349,52.079367025060307,55.810916730984296,60.179197880774502,65.409743669028728,68.537394451972517,71.202039093658186,72.234895658958109,77.819423813461242,82.406812201315859,91.586467801348519,94.796372411932012,97.299031667037156,101.88937554928745,101.01609327008705,108.65072081506786,109.8157171280865,114.16415719088697,119.15549337840642,125.58981216150094,128.26946250733764,131.39182695792096,137.49043901066074,140.33471536401885,144.09253233583237,146.48039591152741,153.01783856270728,155.15679568785214,160.68352292968802,161.01932967033343,168.75457767665299,170.71652571862896,174.20245476974551,177.72968491749828,186.37720469306714,186.91086799105838,192.27582502954235,193.81234900258156,198.24535354761974,205.18104367234056,205.58001671585077,210.36846466451468,214.89745515045041,221.41881771351822,225.14585209029912,226.41811585983714,233.18501649058732,236.78069348429213,243.3146340851759,247.08759092031764,249.73259276442849,250.67962234100474,255.8500145903574,258.2826687679472,263.93886951959377,267.36775295580247,269.87600881651059,276.58238990141263,281.00590240397582,285.39323883177292,284.26238315062164,290.53163991144612,297.0692053955367,302.6385869798147,309.31640889870135,307.12781441869038,311.6513588351412,312.56921560373053,320.8471285926733,326.04384204895865,328.9477067445377,332.83909397731651,335.18281672550694,341.39485745410047,347.09012394014553,348.57196516657893,353.39287539568176,355.4430732087601,358.43189902465195,368.09798759736333,370.90592854256488,371.23999631378172,373.23923027520141,378.80969953563272,383.89492113889145,388.15128514240445,392.75172845976158,392.9009069888582,400.67007418939284],"type":"scatter","mode":"markers","marker":{"color":"rgba(31,119,180,1)","line":{"color":"rgba(31,119,180,1)"}},"error_y":{"color":"rgba(31,119,180,1)"},"error_x":{"color":"rgba(31,119,180,1)"},"line":{"color":"rgba(31,119,180,1)"},"xaxis":"x","yaxis":"y","frame":null}],"highlight":{"on":"plotly_click","persistent":false,"dynamic":false,"selectize":false,"opacityDim":0.20000000000000001,"selected":{"opacity":1},"debounce":0},"shinyEvents":["plotly_hover","plotly_click","plotly_selected","plotly_relayout","plotly_brushed","plotly_brushing","plotly_clickannotation","plotly_doubleclick","plotly_deselect","plotly_afterplot","plotly_sunburstclick"],"base_url":"https://plot.ly"},"evals":[],"jsHooks":[]}</script>
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
##   0.004   0.000   0.005
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
<div class="profvis html-widget html-fill-item" id="htmlwidget-b747b5c402737f3a9d06" style="width:100%;height:600px;"></div>
<script type="application/json" data-for="htmlwidget-b747b5c402737f3a9d06">{"x":{"message":{"prof":{"time":[1,2,3,4,5,6,7,8,9,9,9,10,10,11,11,12,12,13,13,14,14,15,15,16,16,17,17,18,18,19,19,20,20,21,21,22,23,23,24,24,25,26,27,27,28,28,29,29,30,31,31,31,32,32,33,33,34,34,35,35,36,36,37,38,38,39,40,40,40,41,41,42,42,43,43,44,44,45,46,46,47,47,47,48,48,48,49,49,50,51,51,52,52,52,53,54,54,55,55,56,56,57,57,58,58,59,59,59,60,61,62,62,63,63,63,64,64,65,65,66,66,67,67,68,69,69,70,70,71,71,72,72,72,73,73,74,74,75,75,76,77,77,78,79,79,80,80,81,81,81,82,82,82,83,83,83,84,84,85,85,86,86,87,88,89,89,90,90,91,91,92,92,93,93,94,94,95,95,96,96,97,97,98,99,99,99,100,100,101,101,102,103,104,104,105,105,105,106,107,107,108,108,109,109,110,111,111,111,112,112,113,113,114,114,115,116,117,118,118,119,120,120,121,121,122,123,123,124,124,125,125,126,126,127,127,128,129,129,129,130,130,131,132,133,134,135,135,136,136,136,137,137,138,138,139,139,140,141,142,143,144,144,145,145,146,146,147,148,148,148,149,149,149,150,150,151,151,152,152,153,154,155,155,156,156,157,157,158,158,159,159,160,160,161,162,162,163,164,164,165,165,166,166,167,167,168,168,168,169,169,170,170,171,171,172,172,173,173,174,174,175,176,176,177,177,178,179,179,180,180,181,181,181,182,182,182,183,183,184,184,185,185,185,186,186,187,187,188,188,189,190,190,191,191,192,192,193,193,194,194,195,195,196,196,197,197,198,198,199,199,200,200,201,201,202,202,203,204,205,205,206,206,207,207,208,208,209,209,210,210,211,211,212,212,213,213,214,214,214,215,216,216,217,217,218,218,219,219,220,220,221,221,221,222,222,223,223,224,225,226,227,227,228,228,229,230,230,231,231,232,233,233,234,234,235,235,235,236,236,236,237,237,238,239,239,240,240,241,242,243,243,243,244,244,245,245,245,246,246,247,248,248,249,249,249,250,250,251,251,252,252,253,253,254,254,255,255,256,256,257,257,257,258,259,259,260,261,261,262,262,262,263,263,263,264,264,264,265,266,267,267,268,268,269,270,270,271,271,271,272,272,272,273,274,275,276,276,276,277,277,277,278,278,279,280,280,281,281,281,282,282,283,283,284,284,285,285,285,286,287,288,289,289,290,291,291,292,293,293,294,295,295,296,296,297,297,297,298,298,298,299,299,300,300,301,301,302,302,303,303,304,304,304,305,306,306,307,308,308,309,310,310,311,311,312,312,313,313,314,314,315,316,316,316,317,317,317,318,318,318,319,319,319,320,320,321,321,322,322,322,323,324,324,325,325,326,327,327,328,329,329,330,331,331,331,332,332,333,334,335,335,336,336,337,337,337,338,338,339,340,340,340,341,342,342,343,343,343,344,344,345,345,346,347,348,348,348,349,349,350,350,351,351,352,352,353,353,354,354,355,355,356,356,357,357,358,358,359,359,360,360,361,361,362,362,363,363,364,364,365,365,366,366,367,367,368,368,369,369,370,370,371,371,372,372,373,373,374,374,375,376,376,377,377,378,379,379,380,380,381,381,382,382,382,383,383,384,385,385,386,387,387,388,388,389,390,390,391,391,391,392,393,393,394,394,395,395,395,396,396,396,397,397,398,399,400,401,401,402,402,403,403,404,404,405,405,405,406,406,407,407,408,408,409,409,410,411,412,412,413,413,414,415,415,416,416,416,417,418,419,419,420,420,421,421,422,422,423,423,424,424,425,425,426,427,428,428,429,429,429,430,430,430,431,432,432,433,433,434,434,435,435,435,436,437,437,438,438,439,440,440,441,442,443,443,443,444,444,444,445,446,446,447,447,448,448,448,449,449,450,451,451,452,452,453,454,455,456,457,457,457,458,458,458,459,459,460,461,461,462,463,463,464,464,465,465,465,466,467,468,468,468,469,470,471,471,472,472,473,474,475,475,476,477,477,478,479,479,480,481,481,482,482,483,484,484,485,485,485,486,486,486,487,487,488,488,489,489,490,490,491,491,492,492,493,493,494,495,495,496,496,497,498,498,499,499,500,500,500,501,502,502,503,503,504,504,505,506,506,507,507,508,508,509,510,510,511,512,512,513,513,514,515,515,516,516,517,517,518,519,520,520,521,521,521,522,522,523,523,524,524,525,525,525,526,526,526,527,527,528,528,529,529,530,531,531,531,532,532,533,533,534,534,535,536,536,537,538,538,538,539,540,540,540,541,542,542,543,543,543,544,545,546,546,547,547,548,549,550,550,551,552,552,553,553,553,554,554,554,555,555,555,556,556,557,558,558,559,559,560,560,561,562,563,564,565,565,566,566,567,567,568,568,569,569,570,570,571,572,573,573,574,574,574,575,575,576,576,577,578,579,580,581,581,582,582,583,583,584,584,585,586,586,587,587,588,588,589,590,591,592,593,593,594,594,595,595,596,597,597,598,599,599,600,600,601,601,602,603,604,604,604,605,606,606,606,607,608,608,609,610,610,610,611,611,612,613,613,614,614,615,615,616,616,617,618,618,619,619,620,621,621,622,622,623,623,624,625,625,626,626,627,627,628,628,629,629,630,630,631,631,631,632,632,633,633,634,634,635,635,636,636,637,637,637,638,638,639,639,640,641,641,642,642,643,643,644,644,645,646,646,647,647,648,648,649,649,650,651,652,652,653,653,654,655,655,655,656,656,656,657,657,657,658,658,658,659,659,660,660,661,662,663,663,664,664,665,665,666,667,668,668,668,669,669,669,670,670,670,671,671,671,672,672,672,673,673,673,674,674,674,675,675,675,676,676,676,677,677,677,678,678,678,679,679,679,680,680,680,681,681,682,682,683,684,685,686,686,687,688,689,690,690,690,691,691,692,692,692,693,693,693,694,694,695,695,696,696,697,697,698,699,700,700,701,701,701,702,703,703,704,704,705,706,706,707,707,708,708,709,709,710,710,711,711,712,712,713,713,714,714,715,715,716,716,716,717,717,718,719,719,720,721,721,721,722,722,723,724,724,725,726,727,727,727,728,728,728,729,729,730,730,731,731,732,732,733,734,735,736,736,737,737,738,738,738,739,739,739,740,740,741,742,742,743,743,744,744,745,745,746,746,747,748,749,749,750,750,750,751,751,752,752,753,753,754,754,755,756,757,757,758,758,758,759,760,760,761,761,762,762,763,763,764,764,765,766,766,767,767,767,768,768,769,769,770,770,771,771,771,772,772,773,773,774,775,775,775,776,776,777,778,778,779,779,780,780,781,782,782,783,783,783,783,784,784,785,785,786,786,787,788,789,790,790,791,791,792,793,793,793,794,794,794,795,795,796,797,797,798,799,799,800,800,800,801,802,802,803,804,804,804,805,806,806,807,807,808,808,809,810,810,811,812,813,813,814,814,815,815,816,816,817,817,818,818,818,819,820,820,821,821,822,823,823,824,825,825,826,826,826,827,828,828,828,829,829,830,830,831,832,832,833,834,834,835,835,836,836,837,837,838,838,839,840,840,841,842,842,843,843,844,845,845,846,846,847,848,848,849,849,850,851,851,852,853,854,854,855,855,855,856,856,856,857,858,859,859,859,860,860,861,862,862,863,863,864,865,865,865,866,866,866,867,867,868,868,869,869,869,870,870,871,871,872,873,873,874,874,875,875,876,876,877,877,878,878,879,880,880,881,881,882,883,883,884,884,885,885,885,886,886,886,887,888,888,889,889,890,890,890,891,891,892,892,893,893,894,895,895,895,896,896,896,897,898,898,899,899,900,901,901,902,902,902,903,903,904,904,905,905,905,906,906,906,907,907,907,908,908,908,909,909,909,910,910,910,911,911,911,912,912,912,913,913,913,914,914,914,915,915,915,916,917,917,918,918,919,919,920,920,921,921,922,922,923,924,924,924,925,925,925,926,926,927,927,928,928,929,930,930,931,931,932,932,933,933,934,934,934,935,935,935,936,936,937,937,938,938,939,940,941,941,942,942,943,943,944,944,945,945,946,947,948,948,949,949,950,950,951,951,952,952,952,953,953,953,954,954,955,955,956,957,958,958,959,960,960,961,961,961,962,962,962,963,964,965,966,967,968,968,968,969,969,970,970,971,971,972,972,973,974,975,975,976,976,977,977,978,978,979,979,979,980,980,980,981,981,982,982,983,983,983,984,984,984,985,985,986,986,987,988,988,988,989,989,989,990,990,990,991,991,992,993,993,994,994,995,995,996,997,997,998,998,999,999,1000,1001,1001,1002,1002,1003,1003,1004,1004,1005,1006,1006,1007,1007,1008,1008,1009,1009,1010,1011,1012,1012,1012,1013,1014,1014,1015,1015,1016,1016,1017,1018,1019,1019,1019,1020,1020,1021,1021,1022,1022,1023,1023,1024,1024,1025,1026,1027,1028,1028,1029,1029,1030,1030,1031,1031,1032,1032,1033,1033,1034,1035,1036,1036,1037,1037,1038,1038,1039,1039,1040,1040,1040,1041,1041,1041,1042,1042,1043,1044,1045,1045,1046,1046,1047,1047,1047,1048,1048,1049,1049,1049,1050,1050,1050,1051,1051,1051,1052,1052,1052,1053,1053,1053,1054,1054,1054,1055,1055,1056,1057,1057,1058,1059,1059,1059,1060,1060,1061,1061,1062,1062,1063,1063,1064,1064,1065,1065,1066,1066,1067,1067,1068,1068,1069,1069,1070,1070,1071,1071,1072,1072,1073,1073,1074,1074,1075,1075,1076,1076,1077,1077,1078,1078,1079,1079,1080,1080,1081,1081,1082,1082,1083,1083,1084,1084,1085,1085,1086,1086,1087,1087,1088,1088,1089,1089,1090,1090,1091,1091,1092,1092,1093,1093,1094,1094,1095,1095,1096,1096,1097,1097,1098,1098,1099,1099,1100,1100,1101,1101,1102,1102,1103,1103,1104,1104,1105,1105,1106,1106,1107,1107,1108,1108,1109,1109,1110,1110,1111,1111,1112,1112,1113,1113,1114,1114,1115,1115,1115,1116,1116,1117,1117,1118,1118,1119,1119,1120,1120,1121,1121,1122,1123,1123,1124,1124,1125,1126,1126,1127,1128,1128,1129,1129,1130,1131,1132,1133,1133,1134,1135,1135,1136,1136,1137,1137,1137,1138,1138,1138,1139,1139,1140,1140,1141,1141,1142,1142,1143,1143,1144,1144,1145,1146,1146,1147,1147,1147,1148,1148,1149,1150,1150,1151,1151,1152,1153,1153,1154,1155,1155,1156,1156,1157,1157,1158,1158,1159,1159,1159,1160,1160,1160,1161,1161,1161,1162,1162,1163,1163,1164,1164,1165,1166,1166,1167,1167,1168,1168,1169,1170,1170,1171,1171,1172,1173,1173,1173,1174,1174,1175,1175,1176,1176,1177,1177,1178,1178,1179,1179,1180,1181,1181,1182,1182,1183,1183,1184,1184,1185,1185,1186,1186,1187,1188,1188,1188,1189,1189,1190,1191,1191,1192,1193,1193,1194,1194,1195,1195,1196,1196,1196,1197,1198,1199,1199,1200,1201,1201,1202,1203,1203,1204,1204,1204,1205,1205,1205,1206,1206,1206,1207,1207,1208,1209,1210,1210,1211,1211,1212,1212,1212,1213,1213,1214,1214,1215,1215,1216,1216,1217,1218,1219,1220,1220,1221,1221,1222,1222,1223,1223,1224,1224,1225,1226,1226,1227,1227,1228,1228,1229,1230,1231,1231,1232,1232,1233,1233,1233,1234,1234,1235,1236,1236,1237,1237,1238,1239,1240,1241,1242,1242,1243,1243,1244,1244,1245,1246,1246,1247,1248,1248,1248,1249,1249,1249,1250,1250,1250,1251,1251,1252,1252,1253,1254,1254,1255,1256,1256,1257,1258,1258,1259,1260,1261,1262,1263,1263,1264,1264,1265,1265,1266,1266,1267,1267,1268,1269,1269,1270,1270,1270,1271,1271,1271,1272,1272,1272,1273,1273,1273,1274,1274,1274,1275,1275,1275,1276,1276,1276,1277,1277,1277,1278,1279,1279,1280,1280,1281,1281,1282,1283,1283,1284,1285,1285,1286,1286,1287,1288,1288,1289,1290,1290,1291,1291,1291,1292,1293,1294,1295,1295,1296,1296,1297,1297,1298,1298,1299,1299,1300,1301,1301,1302,1303,1303,1304,1304,1305,1306,1306,1307,1308,1308,1309,1309,1310,1311,1311,1312,1312,1313,1313,1314,1315,1315,1316,1316,1317,1318,1318,1319,1319,1319,1320,1320,1320,1321,1321,1321,1322,1323,1323,1324,1325,1325,1326,1326,1327,1327,1328,1328,1329,1329,1330,1331,1332,1332,1333,1334,1334,1335,1335,1336,1336,1337,1338,1338,1339,1339,1340,1340,1340,1341,1341,1341,1342,1342,1343,1344,1345,1345,1346,1347,1347,1348,1348,1349,1349,1350,1350,1351,1351,1352,1353,1353,1354,1354,1355,1355,1356,1356,1357,1357,1358,1358,1359,1359,1360,1360,1361,1361,1362,1362,1363,1363,1364,1365,1365,1366,1366,1367,1367,1368,1368,1369,1369,1370,1370,1371,1371,1372,1372,1373,1373,1374,1374,1375,1375,1376,1376,1377,1377,1378,1378,1379,1379,1380,1380,1381,1381,1382,1382,1383,1383,1384,1384,1385,1385,1385,1385,1385,1385,1385,1385,1385,1385,1385,1385,1385,1385,1385,1385,1385,1385,1385,1386,1386,1386,1386,1386,1386,1386,1386,1387,1387,1387,1387,1387,1387,1387,1387,1388,1388,1388,1388,1388,1388,1388,1388,1389,1389,1389,1389,1389,1389,1389,1389,1390,1390,1390,1390,1390,1390,1390,1390,1391,1391,1391,1391,1391,1391,1391,1391,1392,1392,1392,1392,1392,1392,1392,1392,1393,1393,1393,1393,1393,1393,1393,1393,1394,1394,1394,1394,1394,1394,1394,1394,1395,1395,1395,1395,1395,1395,1395,1395,1396,1396,1396,1396,1396,1396,1396,1396,1397,1397,1397,1397,1397,1397,1397,1397,1398,1398,1398,1398,1398,1398,1398,1398,1399,1399,1399,1399,1399,1399,1399,1399,1400,1400,1400,1400,1400,1400,1400,1400,1401,1401,1401,1401,1401,1401,1401,1401,1402,1402,1402,1402,1402,1402,1402,1402,1403,1403,1403,1403,1403,1403,1403,1403],"depth":[1,1,1,1,1,1,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,3,2,1,2,1,1,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,1,1,2,1,3,2,1,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,2,1,1,1,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,1,1,1,1,2,1,3,2,1,2,1,2,1,2,1,1,1,1,1,2,1,2,1,2,1,1,3,2,1,3,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,1,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,1,1,3,2,1,2,1,3,2,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,1,2,1,3,2,1,3,2,1,3,2,1,1,1,2,1,2,1,1,2,1,3,2,1,3,2,1,1,1,1,3,2,1,3,2,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,3,2,1,1,1,1,2,1,1,2,1,1,2,1,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,3,2,1,1,2,1,2,1,1,2,1,1,2,1,1,3,2,1,2,1,1,1,2,1,2,1,3,2,1,2,1,1,3,2,1,1,2,1,3,2,1,2,1,2,1,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,1,2,1,2,1,1,2,1,3,2,1,1,2,1,2,1,3,2,1,3,2,1,2,1,1,1,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,1,2,1,3,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,1,2,1,1,1,3,2,1,3,2,1,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,1,1,1,1,3,2,1,3,2,1,2,1,1,2,1,1,2,1,2,1,3,2,1,1,1,3,2,1,1,1,2,1,2,1,1,1,2,1,1,2,1,1,2,1,1,2,1,2,1,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,3,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,1,1,2,1,3,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,3,2,1,2,1,2,1,2,1,1,2,1,1,3,2,1,1,3,2,1,1,2,1,3,2,1,1,1,2,1,2,1,1,1,2,1,1,2,1,3,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,2,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,3,2,1,2,1,2,1,1,1,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,1,1,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,1,1,3,2,1,1,3,2,1,1,2,1,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,1,1,2,1,2,1,2,1,1,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,1,1,1,2,1,1,1,1,3,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,1,1,2,1,3,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,1,2,1,1,3,2,1,2,1,1,2,1,1,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,1,1,1,2,1,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,1,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,1,3,2,1,2,1,1,2,1,2,1,2,1,1,2,1,4,3,2,1,2,1,2,1,2,1,1,1,1,2,1,2,1,1,3,2,1,3,2,1,2,1,1,2,1,1,2,1,3,2,1,1,2,1,1,3,2,1,1,2,1,2,1,2,1,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,3,2,1,1,2,1,2,1,1,2,1,1,2,1,3,2,1,1,3,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,1,2,1,1,1,2,1,3,2,1,3,2,1,1,1,3,2,1,2,1,1,2,1,2,1,1,3,2,1,3,2,1,2,1,2,1,3,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,1,2,1,2,1,1,2,1,3,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,1,1,2,1,1,2,1,3,2,1,3,2,1,1,1,1,1,1,3,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,1,3,2,1,3,2,1,3,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,1,3,2,1,1,2,1,2,1,2,1,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,2,1,1,1,2,1,2,1,3,2,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,2,1,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,1,2,1,2,1,1,1,1,2,1,1,2,1,2,1,3,2,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,2,1,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,3,2,1,3,2,1,3,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,1,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,3,2,1,2,1,1,2,1,1,2,1,2,1,2,1,3,2,1,1,1,2,1,1,2,1,1,2,1,3,2,1,3,2,1,3,2,1,2,1,1,1,2,1,2,1,3,2,1,2,1,2,1,2,1,2,1,1,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,1,1,2,1,2,1,3,2,1,2,1,1,2,1,2,1,1,1,1,1,2,1,2,1,2,1,1,2,1,1,3,2,1,3,2,1,3,2,1,2,1,2,1,1,2,1,1,2,1,1,2,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,1,2,1,1,2,1,3,2,1,1,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,3,2,1,3,2,1,3,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,1,2,1,2,1,2,1,1,2,1,2,1,3,2,1,3,2,1,2,1,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1,8,7,6,5,4,3,2,1],"label":["rowSums","rowSums","rowSums","rowSums","rowMeans","rowMeans","rowMeans","rowMeans","<GC>","aperm.default","apply","aperm.default","apply","aperm.default","apply","aperm.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","apply","FUN","apply","FUN","apply","apply","apply","mean.default","apply","FUN","apply","FUN","apply","apply","<GC>","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","length","local","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","is.numeric","local","FUN","apply","apply","mean.default","apply","isTRUE","mean.default","apply","apply","FUN","apply","mean.default","apply","<GC>","apply","mean.default","apply","mean.default","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","apply","FUN","apply","is.numeric","local","mean.default","apply","apply","mean.default","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","is.numeric","local","FUN","apply","apply","apply","<GC>","apply","mean.default","apply","FUN","apply","length","local","mean.default","apply","FUN","apply","is.na","local","FUN","apply","<GC>","apply","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","apply","apply","mean.default","apply","<GC>","mean.default","apply","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","apply","FUN","apply","apply","apply","apply","mean.default","apply","apply","FUN","apply","<GC>","apply","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","<GC>","FUN","apply","FUN","apply","apply","apply","apply","apply","FUN","apply","<GC>","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","apply","apply","apply","apply","<GC>","apply","FUN","apply","mean.default","apply","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","<GC>","apply","apply","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","apply","length","local","apply","is.na","local","is.numeric","local","is.na","local","is.na","local","<GC>","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","is.na","local","apply","FUN","apply","<GC>","apply","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","<GC>","mean.default","apply","length","local","mean.default","apply","FUN","apply","apply","mean.default","apply","FUN","apply","FUN","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","mean.default","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","<GC>","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","<GC>","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","apply","apply","apply","<GC>","apply","<GC>","apply","apply","mean.default","apply","FUN","apply","apply","is.na","local","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","mean.default","apply","FUN","apply","apply","apply","<GC>","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","apply","is.numeric","local","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","<GC>","FUN","apply","apply","is.na","local","apply","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","<GC>","mean.default","apply","isTRUE","mean.default","apply","apply","apply","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","<GC>","apply","isTRUE","mean.default","apply","apply","apply","apply","FUN","apply","apply","<GC>","apply","apply","FUN","apply","apply","mean.default","apply","FUN","apply","<GC>","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","is.numeric","local","FUN","apply","FUN","apply","<GC>","FUN","apply","apply","is.numeric","local","apply","FUN","apply","apply","FUN","apply","<GC>","apply","<GC>","apply","length","local","FUN","apply","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","<GC>","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","<GC>","apply","apply","FUN","apply","apply","FUN","apply","apply","<GC>","FUN","apply","FUN","apply","apply","apply","FUN","apply","FUN","apply","<GC>","is.na","local","FUN","apply","apply","isTRUE","mean.default","apply","apply","mean.default","apply","<GC>","FUN","apply","FUN","apply","mean.default","apply","apply","apply","isTRUE","mean.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","apply","mean.default","apply","FUN","apply","apply","FUN","apply","is.numeric","local","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","apply","FUN","apply","<GC>","mean.default","apply","apply","mean.default","apply","length","local","isTRUE","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","is.numeric","local","FUN","apply","apply","apply","FUN","apply","length","local","apply","mean.default","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","is.na","local","FUN","apply","mean.default","apply","apply","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","mean.default","apply","length","local","mean.default","apply","isTRUE","mean.default","apply","apply","mean.default","apply","FUN","apply","apply","FUN","apply","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","mean.default","apply","FUN","apply","apply","apply","apply","apply","<GC>","length","local","<GC>","length","local","FUN","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","isTRUE","mean.default","apply","apply","apply","mean.default","apply","<GC>","apply","apply","apply","mean.default","apply","apply","mean.default","apply","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","length","local","apply","FUN","apply","FUN","apply","apply","FUN","apply","<GC>","apply","isTRUE","mean.default","apply","apply","FUN","apply","FUN","apply","is.numeric","local","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","apply","mean.default","apply","FUN","apply","is.na","local","apply","apply","FUN","apply","isTRUE","mean.default","apply","is.numeric","local","FUN","apply","FUN","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","mean.default","apply","mean.default","apply","mean.default","apply","apply","isTRUE","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","isTRUE","mean.default","apply","apply","<GC>","FUN","apply","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","FUN","apply","is.na","local","apply","apply","FUN","apply","apply","mean.default","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","is.na","local","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","apply","apply","apply","mean.default","apply","FUN","apply","FUN","apply","<GC>","apply","FUN","apply","FUN","apply","apply","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","apply","apply","apply","apply","<GC>","apply","FUN","apply","FUN","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","FUN","apply","apply","apply","apply","apply","FUN","apply","<GC>","apply","FUN","apply","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","apply","<GC>","mean.default","apply","apply","length","local","apply","isTRUE","mean.default","apply","FUN","apply","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","apply","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","apply","mean.default","apply","FUN","apply","<GC>","apply","<GC>","apply","apply","mean.default","apply","FUN","apply","is.na","local","FUN","apply","apply","apply","length","local","FUN","apply","apply","isTRUE","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","isTRUE","mean.default","apply","FUN","apply","length","local","apply","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","FUN","apply","apply","apply","apply","FUN","apply","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","is.numeric","local","FUN","apply","mean.default","apply","is.numeric","local","apply","apply","FUN","apply","isTRUE","mean.default","apply","apply","FUN","apply","<GC>","apply","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","<GC>","FUN","apply","mean.default","apply","apply","FUN","apply","apply","isTRUE","mean.default","apply","FUN","apply","apply","mean.default","apply","apply","apply","<GC>","is.numeric","local","<GC>","is.numeric","local","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","apply","apply","apply","is.numeric","local","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","mean.default","apply","FUN","apply","is.numeric","local","FUN","apply","FUN","apply","apply","apply","length","local","<GC>","length","local","FUN","apply","mean.default","apply","length","local","mean.default","apply","apply","apply","mean.default","apply","isTRUE","mean.default","apply","apply","mean.default","apply","<GC>","apply","FUN","apply","FUN","apply","FUN","apply","apply","mean.default","apply","isTRUE","mean.default","apply","mean.default","apply","length","local","FUN","apply","isTRUE","mean.default","apply","<GC>","apply","length","local","apply","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","apply","mean.default","apply","<GC>","isTRUE","mean.default","apply","FUN","apply","mean.default","apply","length","local","apply","apply","apply","FUN","apply","FUN","apply","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","FUN","apply","apply","mean.default","apply","isTRUE","mean.default","apply","apply","mean.default","apply","apply","<GC>","mean.default","apply","apply","FUN","apply","mean.default","apply","FUN","apply","apply","FUN","apply","apply","apply","mean.default","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","apply","is.numeric","local","FUN","apply","apply","mean.default","apply","apply","<GC>","apply","isTRUE","mean.default","apply","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","apply","FUN","apply","apply","length","local","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","apply","FUN","apply","is.na","local","apply","FUN","apply","apply","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","apply","isTRUE","mean.default","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","mean.default","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","apply","length","local","FUN","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","FUN","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","FUN","apply","mean.default","apply","apply","FUN","apply","isTRUE","mean.default","apply","is.numeric","local","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","length","local","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","apply","<GC>","length","local","<GC>","length","local","FUN","apply","mean.default","apply","is.na","local","apply","FUN","apply","length","local","FUN","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","is.numeric","local","FUN","apply","apply","apply","is.numeric","local","FUN","apply","<GC>","apply","<GC>","apply","FUN","apply","apply","apply","FUN","apply","mean.default","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","mean.default","apply","apply","apply","FUN","apply","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","apply","apply","apply","apply","apply","isTRUE","mean.default","apply","mean.default","apply","<GC>","apply","<GC>","apply","FUN","apply","apply","apply","is.na","local","FUN","apply","FUN","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","FUN","apply","isTRUE","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","is.na","local","apply","mean.default","apply","length","local","mean.default","apply","FUN","apply","apply","<GC>","apply","<GC>","apply","FUN","apply","FUN","apply","apply","apply","isTRUE","mean.default","apply","apply","FUN","apply","<GC>","apply","<GC>","apply","apply","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","<GC>","apply","<GC>","apply","apply","apply","apply","length","local","is.na","local","FUN","apply","FUN","apply","<GC>","apply","<GC>","apply","apply","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","apply","mean.default","apply","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","<GC>","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","FUN","apply","FUN","apply","FUN","apply","length","local","FUN","apply","apply","FUN","apply","mean.default","apply","apply","FUN","apply","apply","FUN","apply","mean.default","apply","apply","apply","apply","mean.default","apply","apply","FUN","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","FUN","apply","is.numeric","local","mean.default","apply","FUN","apply","FUN","apply","mean.default","apply","apply","FUN","apply","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","is.na","local","apply","FUN","apply","FUN","apply","FUN","apply","mean.default","apply","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","apply","isTRUE","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","<GC>","apply","<GC>","apply","<GC>","apply","FUN","apply","mean.default","apply","mean.default","apply","apply","isTRUE","mean.default","apply","FUN","apply","apply","FUN","apply","apply","FUN","apply","length","local","is.numeric","local","isTRUE","mean.default","apply","apply","apply","FUN","apply","apply","FUN","apply","apply","length","local","<GC>","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","mean.default","apply","apply","apply","FUN","apply","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","length","local","mean.default","apply","FUN","apply","apply","apply","apply","FUN","apply","mean.default","apply","FUN","apply","length","local","FUN","apply","apply","<GC>","apply","<GC>","apply","<GC>","apply","apply","apply","length","local","mean.default","apply","isTRUE","mean.default","apply","FUN","apply","apply","mean.default","apply","FUN","apply","apply","apply","apply","apply","FUN","apply","FUN","apply","mean.default","apply","apply","FUN","apply","apply","<GC>","is.na","local","<GC>","is.na","local","<GC>","is.na","local","mean.default","apply","FUN","apply","apply","mean.default","apply","apply","mean.default","apply","apply","FUN","apply","apply","apply","apply","apply","FUN","apply","FUN","apply","mean.default","apply","FUN","apply","mean.default","apply","apply","FUN","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","FUN","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","apply","FUN","apply","isTRUE","mean.default","apply","apply","apply","apply","mean.default","apply","FUN","apply","<GC>","apply","<GC>","apply","<GC>","apply","apply","FUN","apply","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","apply","mean.default","apply","FUN","apply","apply","mean.default","apply","FUN","apply","FUN","apply","apply","FUN","apply","mean.default","apply","apply","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","<GC>","mean.default","apply","apply","is.numeric","local","apply","FUN","apply","FUN","apply","mean.default","apply","length","local","FUN","apply","apply","apply","FUN","apply","apply","mean.default","apply","FUN","apply","FUN","apply","apply","FUN","apply","FUN","apply","<GC>","FUN","apply","<GC>","FUN","apply","FUN","apply","apply","apply","FUN","apply","apply","mean.default","apply","mean.default","apply","mean.default","apply","FUN","apply","FUN","apply","apply","is.numeric","local","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","lengths","apply","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","unlist","apply","exists","findCenvVar","getInlineInfo","isBaseVar","isLoopTopFun","checkSkipLoopCntxt","checkSkipLoopCntxtList","checkSkipLoopCntxt","checkSkipLoopCntxtList","checkSkipLoopCntxt","checkSkipLoopCntxtList","checkSkipLoopCntxt","h","tryInline","cmpCall","cmp","genCode","compile","compiler:::tryCompile","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis","m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }","doTryCatch","tryCatchOne","tryCatchList","tryCatchList","tryCatch","with_profvis_handlers","profvis::profvis"],"filenum":[1,1,1,1,1,1,1,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,1,1,null,1,null,1,null,1,1,null,null,1,null,1,null,1,null,1,null,1,null,1,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,1,null,1,null,null,1,null,null,null,null,1,1,null,1,null,null,1,1,null,1,null,1,null,1,null,1,null,1,null,null,1,1,1,null,1,null,null,1,null,1,null,1,null,null,null,1,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,1,null,1,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,1,null,null,null,1,1,1,null,1,null,1,null,1,null,null,null,1,null,1,null,null,null,1,null,1,1,null,null,1,null,1,null,1,1,1,null,1,null,null,1,1,null,1,null,1,null,1,1,null,null,1,null,1,null,1,null,1,1,1,1,null,1,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,1,null,null,1,null,1,1,1,1,1,null,1,null,null,1,null,1,null,1,null,1,1,1,1,1,null,1,null,1,null,1,1,null,null,1,null,null,1,null,1,null,1,null,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,null,1,null,null,null,null,null,null,null,null,null,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,1,null,1,null,1,null,null,1,null,null,1,null,1,null,1,null,null,1,null,null,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,1,1,1,null,1,null,1,1,null,1,null,1,1,null,null,null,1,null,null,1,null,null,1,null,1,1,null,1,null,1,1,1,null,null,1,null,1,null,null,1,null,1,1,null,1,null,null,1,null,1,null,null,null,1,null,1,null,1,null,1,null,1,null,null,1,1,null,null,1,null,1,null,null,1,null,null,1,null,null,1,1,1,null,1,null,1,1,null,1,null,null,1,null,null,1,1,1,1,null,null,1,null,null,1,null,1,1,null,1,null,null,1,null,1,null,1,null,1,null,null,1,1,1,1,null,1,1,null,1,1,null,1,1,null,1,null,1,null,null,1,null,null,1,null,1,null,1,null,null,null,1,null,1,null,null,1,1,null,null,1,null,1,1,null,1,null,1,null,1,null,null,null,1,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,null,1,1,null,1,null,1,1,null,1,1,null,1,1,null,null,1,null,1,1,1,null,1,null,1,null,null,null,null,1,1,null,null,1,1,null,1,null,null,1,null,1,null,1,1,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,1,null,1,null,null,null,1,null,null,1,null,1,1,null,1,1,null,1,null,1,1,null,1,null,null,1,1,null,1,null,null,null,null,1,null,null,1,null,1,1,1,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,null,null,1,1,1,null,1,null,null,1,null,1,null,null,1,1,1,null,1,null,1,null,1,null,1,null,null,null,1,null,1,1,1,null,1,null,null,1,null,null,1,1,null,1,null,null,null,1,null,null,1,1,null,1,null,1,1,null,1,1,1,null,null,1,null,null,1,1,null,1,null,1,null,null,1,null,1,1,null,1,null,1,1,1,1,1,null,null,null,null,null,null,null,1,1,null,1,1,null,1,null,1,null,null,1,1,1,null,null,1,1,1,null,1,null,1,1,1,null,1,1,null,1,1,null,1,1,null,1,null,1,1,null,1,null,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,1,null,1,null,1,null,null,1,1,null,1,null,1,null,null,1,null,1,null,1,null,1,1,null,1,1,null,1,null,1,1,null,1,null,1,null,null,1,1,null,1,null,null,1,null,null,null,1,null,1,null,null,1,null,null,1,null,1,null,1,null,1,1,null,null,1,null,1,null,1,null,1,1,null,1,1,null,null,1,1,null,null,1,1,null,1,null,null,1,1,1,null,1,null,null,1,1,null,1,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,1,1,1,1,1,null,1,null,1,null,1,null,1,null,1,null,1,1,1,null,1,null,null,1,null,1,null,1,1,1,1,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,1,1,1,1,null,1,null,1,null,1,1,null,1,1,null,1,null,1,null,1,1,1,null,null,1,1,null,null,1,1,null,null,1,null,null,1,null,1,1,null,1,null,1,null,1,null,1,1,null,1,null,1,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,null,null,1,1,1,null,null,null,1,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,null,null,1,1,null,1,null,1,null,1,1,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,1,1,1,null,1,1,1,1,null,null,1,null,1,null,null,1,null,null,1,null,null,null,1,null,1,null,null,1,1,null,1,null,null,1,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,1,null,1,1,null,null,1,null,1,1,null,1,1,1,null,null,null,null,null,null,null,1,null,1,null,1,null,1,1,1,1,null,null,null,1,null,null,1,null,null,1,null,1,1,null,1,null,1,null,null,null,1,null,1,1,1,null,null,null,null,null,null,1,null,1,null,null,null,1,1,1,null,1,null,null,1,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,null,1,null,1,null,null,null,1,null,null,1,null,1,null,null,1,null,null,1,null,1,1,null,1,null,1,null,1,1,null,1,null,null,null,1,null,1,null,1,null,null,1,1,1,null,1,null,1,1,null,null,1,null,null,1,null,1,1,null,1,1,null,1,null,null,1,1,null,1,1,null,null,1,1,null,1,null,1,null,1,1,null,1,1,1,null,1,null,1,null,1,null,1,null,1,null,null,1,1,null,null,null,1,1,null,1,1,null,1,null,null,1,1,null,null,1,null,1,null,1,1,null,1,1,null,null,null,1,null,1,null,1,null,1,1,null,1,1,null,1,null,1,1,null,1,null,1,1,null,1,null,null,1,null,1,1,1,null,1,null,null,1,null,null,1,1,1,null,null,1,null,1,1,null,1,null,1,1,null,null,1,null,null,1,null,1,null,1,null,null,1,null,1,null,1,1,null,null,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,1,null,1,null,1,null,null,1,null,null,1,1,null,1,null,1,null,null,1,null,1,null,1,null,1,1,null,null,1,null,null,1,1,null,1,null,1,1,null,1,null,null,1,null,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,1,null,null,null,1,null,1,null,1,null,1,null,1,1,null,null,null,null,null,null,null,1,null,1,null,null,1,null,1,null,null,null,1,null,1,null,null,1,null,null,1,null,1,null,null,null,1,1,1,null,null,null,1,null,1,null,1,null,1,1,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,1,null,1,1,1,null,1,1,null,1,null,null,1,null,null,1,1,1,1,1,1,null,null,1,null,1,null,1,null,1,null,1,1,1,null,null,null,1,null,1,null,1,null,null,1,null,null,1,null,1,null,1,null,null,1,null,null,1,null,1,null,1,1,null,null,1,null,null,1,null,null,1,null,1,1,null,1,null,1,null,1,1,null,1,null,1,null,null,1,null,1,null,null,null,1,null,1,1,null,1,null,1,null,1,null,1,1,1,null,null,1,1,null,1,null,1,null,1,1,1,null,null,1,null,1,null,1,null,1,null,1,null,1,1,1,1,null,null,null,null,null,1,null,1,null,1,null,1,1,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,1,1,1,null,1,null,1,null,null,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,1,1,null,1,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,1,null,1,null,1,null,1,null,1,null,null,null,1,1,null,1,null,1,1,null,1,1,null,1,null,1,1,1,1,null,1,1,null,1,null,1,null,null,1,null,null,1,null,1,null,null,null,1,null,1,null,1,null,1,1,null,1,null,null,1,null,1,1,null,1,null,1,1,null,null,1,null,1,null,1,null,1,null,1,null,null,1,null,null,1,null,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,1,null,1,null,1,1,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,null,1,null,1,1,null,1,1,null,1,null,null,null,null,null,null,1,1,1,null,1,1,null,1,1,null,null,null,null,1,null,null,1,null,null,1,null,1,1,1,null,1,null,1,null,null,1,null,1,null,null,null,1,null,1,1,1,1,null,1,null,1,null,1,null,null,null,1,1,null,1,null,1,null,1,1,1,null,null,null,1,null,null,1,null,1,1,null,1,null,1,1,1,1,1,null,1,null,1,null,1,1,null,1,1,null,null,null,null,null,null,null,null,null,null,1,null,1,1,null,1,1,null,1,1,null,1,1,1,1,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,null,null,1,1,null,1,null,1,null,1,1,null,1,1,null,1,null,1,1,null,1,1,null,1,null,null,1,1,1,1,null,1,null,1,null,1,null,1,null,1,1,null,1,1,null,1,null,1,1,null,1,1,null,1,null,1,1,null,1,null,1,null,1,1,null,1,null,1,1,null,1,null,null,1,null,null,1,null,null,1,1,null,null,1,null,1,null,1,null,1,null,null,null,1,1,1,null,1,1,null,1,null,1,null,1,1,null,1,null,1,null,null,1,null,null,1,null,1,1,1,null,1,1,null,1,null,1,null,1,null,1,null,1,1,null,null,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,1,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null],"linenum":[10,10,10,10,11,11,11,11,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,12,12,null,12,null,12,null,12,12,null,null,12,null,12,null,12,null,12,null,12,null,12,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,12,null,12,null,null,12,null,null,null,null,12,12,null,12,null,null,12,12,null,12,null,12,null,12,null,12,null,12,null,null,12,12,12,null,12,null,null,12,null,12,null,12,null,null,null,12,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,12,null,12,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,12,null,null,null,12,12,12,null,12,null,12,null,12,null,null,null,12,null,12,null,null,null,12,null,12,12,null,null,12,null,12,null,12,12,12,null,12,null,null,12,12,null,12,null,12,null,12,12,null,null,12,null,12,null,12,null,12,12,12,12,null,12,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,12,null,null,12,null,12,12,12,12,12,null,12,null,null,12,null,12,null,12,null,12,12,12,12,12,null,12,null,12,null,12,12,null,null,12,null,null,12,null,12,null,12,null,12,12,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,null,12,null,null,null,null,null,null,null,null,null,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,12,null,12,null,12,null,null,12,null,null,12,null,12,null,12,null,null,12,null,null,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,12,12,12,null,12,null,12,12,null,12,null,12,12,null,null,null,12,null,null,12,null,null,12,null,12,12,null,12,null,12,12,12,null,null,12,null,12,null,null,12,null,12,12,null,12,null,null,12,null,12,null,null,null,12,null,12,null,12,null,12,null,12,null,null,12,12,null,null,12,null,12,null,null,12,null,null,12,null,null,12,12,12,null,12,null,12,12,null,12,null,null,12,null,null,12,12,12,12,null,null,12,null,null,12,null,12,12,null,12,null,null,12,null,12,null,12,null,12,null,null,12,12,12,12,null,12,12,null,12,12,null,12,12,null,12,null,12,null,null,12,null,null,12,null,12,null,12,null,null,null,12,null,12,null,null,12,12,null,null,12,null,12,12,null,12,null,12,null,12,null,null,null,12,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,null,12,12,null,12,null,12,12,null,12,12,null,12,12,null,null,12,null,12,12,12,null,12,null,12,null,null,null,null,12,12,null,null,12,12,null,12,null,null,12,null,12,null,12,12,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,12,null,12,null,null,null,12,null,null,12,null,12,12,null,12,12,null,12,null,12,12,null,12,null,null,12,12,null,12,null,null,null,null,12,null,null,12,null,12,12,12,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,null,null,12,12,12,null,12,null,null,12,null,12,null,null,12,12,12,null,12,null,12,null,12,null,12,null,null,null,12,null,12,12,12,null,12,null,null,12,null,null,12,12,null,12,null,null,null,12,null,null,12,12,null,12,null,12,12,null,12,12,12,null,null,12,null,null,12,12,null,12,null,12,null,null,12,null,12,12,null,12,null,12,12,12,12,12,null,null,null,null,null,null,null,12,12,null,12,12,null,12,null,12,null,null,12,12,12,null,null,12,12,12,null,12,null,12,12,12,null,12,12,null,12,12,null,12,12,null,12,null,12,12,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,12,null,12,null,12,null,null,12,12,null,12,null,12,null,null,12,null,12,null,12,null,12,12,null,12,12,null,12,null,12,12,null,12,null,12,null,null,12,12,null,12,null,null,12,null,null,null,12,null,12,null,null,12,null,null,12,null,12,null,12,null,12,12,null,null,12,null,12,null,12,null,12,12,null,12,12,null,null,12,12,null,null,12,12,null,12,null,null,12,12,12,null,12,null,null,12,12,null,12,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,12,12,12,12,12,null,12,null,12,null,12,null,12,null,12,null,12,12,12,null,12,null,null,12,null,12,null,12,12,12,12,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,12,12,12,12,null,12,null,12,null,12,12,null,12,12,null,12,null,12,null,12,12,12,null,null,12,12,null,null,12,12,null,null,12,null,null,12,null,12,12,null,12,null,12,null,12,null,12,12,null,12,null,12,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,null,null,12,12,12,null,null,null,12,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,null,null,12,12,null,12,null,12,null,12,12,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,12,12,12,null,12,12,12,12,null,null,12,null,12,null,null,12,null,null,12,null,null,null,12,null,12,null,null,12,12,null,12,null,null,12,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,12,null,12,12,null,null,12,null,12,12,null,12,12,12,null,null,null,null,null,null,null,12,null,12,null,12,null,12,12,12,12,null,null,null,12,null,null,12,null,null,12,null,12,12,null,12,null,12,null,null,null,12,null,12,12,12,null,null,null,null,null,null,12,null,12,null,null,null,12,12,12,null,12,null,null,12,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,null,12,null,12,null,null,null,12,null,null,12,null,12,null,null,12,null,null,12,null,12,12,null,12,null,12,null,12,12,null,12,null,null,null,12,null,12,null,12,null,null,12,12,12,null,12,null,12,12,null,null,12,null,null,12,null,12,12,null,12,12,null,12,null,null,12,12,null,12,12,null,null,12,12,null,12,null,12,null,12,12,null,12,12,12,null,12,null,12,null,12,null,12,null,12,null,null,12,12,null,null,null,12,12,null,12,12,null,12,null,null,12,12,null,null,12,null,12,null,12,12,null,12,12,null,null,null,12,null,12,null,12,null,12,12,null,12,12,null,12,null,12,12,null,12,null,12,12,null,12,null,null,12,null,12,12,12,null,12,null,null,12,null,null,12,12,12,null,null,12,null,12,12,null,12,null,12,12,null,null,12,null,null,12,null,12,null,12,null,null,12,null,12,null,12,12,null,null,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,12,null,12,null,12,null,null,12,null,null,12,12,null,12,null,12,null,null,12,null,12,null,12,null,12,12,null,null,12,null,null,12,12,null,12,null,12,12,null,12,null,null,12,null,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,12,null,null,null,12,null,12,null,12,null,12,null,12,12,null,null,null,null,null,null,null,12,null,12,null,null,12,null,12,null,null,null,12,null,12,null,null,12,null,null,12,null,12,null,null,null,12,12,12,null,null,null,12,null,12,null,12,null,12,12,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,12,null,12,12,12,null,12,12,null,12,null,null,12,null,null,12,12,12,12,12,12,null,null,12,null,12,null,12,null,12,null,12,12,12,null,null,null,12,null,12,null,12,null,null,12,null,null,12,null,12,null,12,null,null,12,null,null,12,null,12,null,12,12,null,null,12,null,null,12,null,null,12,null,12,12,null,12,null,12,null,12,12,null,12,null,12,null,null,12,null,12,null,null,null,12,null,12,12,null,12,null,12,null,12,null,12,12,12,null,null,12,12,null,12,null,12,null,12,12,12,null,null,12,null,12,null,12,null,12,null,12,null,12,12,12,12,null,null,null,null,null,12,null,12,null,12,null,12,12,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,12,12,12,null,12,null,12,null,null,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,12,12,null,12,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,12,null,12,null,12,null,12,null,12,null,null,null,12,12,null,12,null,12,12,null,12,12,null,12,null,12,12,12,12,null,12,12,null,12,null,12,null,null,12,null,null,12,null,12,null,null,null,12,null,12,null,12,null,12,12,null,12,null,null,12,null,12,12,null,12,null,12,12,null,null,12,null,12,null,12,null,12,null,12,null,null,12,null,null,12,null,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,12,null,12,null,12,12,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,null,12,null,12,12,null,12,12,null,12,null,null,null,null,null,null,12,12,12,null,12,12,null,12,12,null,null,null,null,12,null,null,12,null,null,12,null,12,12,12,null,12,null,12,null,null,12,null,12,null,null,null,12,null,12,12,12,12,null,12,null,12,null,12,null,null,null,12,12,null,12,null,12,null,12,12,12,null,null,null,12,null,null,12,null,12,12,null,12,null,12,12,12,12,12,null,12,null,12,null,12,12,null,12,12,null,null,null,null,null,null,null,null,null,null,12,null,12,12,null,12,12,null,12,12,null,12,12,12,12,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,null,null,12,12,null,12,null,12,null,12,12,null,12,12,null,12,null,12,12,null,12,12,null,12,null,null,12,12,12,12,null,12,null,12,null,12,null,12,null,12,12,null,12,12,null,12,null,12,12,null,12,12,null,12,null,12,12,null,12,null,12,null,12,12,null,12,null,12,12,null,12,null,null,12,null,null,12,null,null,12,12,null,null,12,null,12,null,12,null,12,null,null,null,12,12,12,null,12,12,null,12,null,12,null,12,12,null,12,null,12,null,null,12,null,null,12,null,12,12,12,null,12,12,null,12,null,12,null,12,null,12,null,12,12,null,null,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,12,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,13,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null,13,null,null,null,null,null,null,null],"memalloc":[124.5360641479492,124.5360641479492,124.5360641479492,124.5360641479492,139.8182983398438,139.8182983398438,139.8182983398438,139.8182983398438,139.8186645507812,139.8186645507812,139.8186645507812,170.2840423583984,170.2840423583984,170.2840423583984,170.2840423583984,170.2840423583984,170.2840423583984,170.2840881347656,170.2840881347656,170.2840881347656,170.2840881347656,170.2840881347656,170.2840881347656,170.2840881347656,170.2840881347656,170.2840881347656,170.2840881347656,170.2840881347656,170.2840881347656,170.2840881347656,170.2840881347656,170.2840881347656,170.2840881347656,170.2837829589844,170.2837829589844,185.6169052124023,185.8574829101562,185.8574829101562,186.1115188598633,186.1115188598633,186.3889312744141,186.7094268798828,187.0938568115234,187.0938568115234,187.4449615478516,187.4449615478516,187.8408203125,187.8408203125,188.2470474243164,188.6059417724609,188.6059417724609,188.6059417724609,185.7996215820312,185.7996215820312,186.1635971069336,186.1635971069336,186.5434799194336,186.5434799194336,186.959587097168,186.959587097168,187.3708343505859,187.3708343505859,187.779167175293,188.1854400634766,188.1854400634766,188.5924453735352,185.8308410644531,185.8308410644531,185.8308410644531,186.1907272338867,186.1907272338867,186.557975769043,186.557975769043,186.9447937011719,186.9447937011719,187.3513031005859,187.3513031005859,187.7558517456055,188.1620025634766,188.1620025634766,188.5691299438477,188.5691299438477,188.5691299438477,188.7521438598633,188.7521438598633,188.7521438598633,186.2167510986328,186.2167510986328,186.579704284668,186.9614944458008,186.9614944458008,187.3701782226562,187.3701782226562,187.3701782226562,187.7787399291992,188.1836776733398,188.1836776733398,188.5897369384766,188.5897369384766,188.8326416015625,188.8326416015625,186.2795944213867,186.2795944213867,186.6294937133789,186.6294937133789,186.9999237060547,186.9999237060547,186.9999237060547,187.3905792236328,187.7941055297852,188.2008590698242,188.2008590698242,188.6064071655273,188.6064071655273,188.6064071655273,188.9118881225586,188.9118881225586,186.3386154174805,186.3386154174805,186.6769561767578,186.6769561767578,187.0373992919922,187.0373992919922,187.4076156616211,187.7975845336914,187.7975845336914,188.1923446655273,188.1923446655273,188.589973449707,188.589973449707,188.9897232055664,188.9897232055664,188.9897232055664,186.3935546875,186.3935546875,186.7237319946289,186.7237319946289,187.0845260620117,187.0845260620117,187.4585800170898,187.8533401489258,187.8533401489258,188.2493896484375,188.6566162109375,188.6566162109375,189.0624771118164,189.0624771118164,186.4704513549805,186.4704513549805,186.4704513549805,186.790168762207,186.790168762207,186.790168762207,187.1349716186523,187.1349716186523,187.1349716186523,187.49560546875,187.49560546875,187.868293762207,187.868293762207,188.2612152099609,188.2612152099609,188.6613006591797,189.0648956298828,189.1418609619141,189.1418609619141,186.8525924682617,186.8525924682617,187.1949081420898,187.1949081420898,187.5532913208008,187.5532913208008,187.9268569946289,187.9268569946289,188.3125305175781,188.3125305175781,188.6989517211914,188.6989517211914,189.0974197387695,189.0974197387695,189.2160110473633,189.2160110473633,186.9278717041016,187.2680740356445,187.2680740356445,187.2680740356445,187.6256713867188,187.6256713867188,188.0013809204102,188.0013809204102,188.3918762207031,188.7910766601562,189.1918563842773,189.1918563842773,189.2890319824219,189.2890319824219,189.2890319824219,187.0558853149414,187.4003601074219,187.4003601074219,187.7455062866211,187.7455062866211,188.109992980957,188.109992980957,188.4778900146484,188.8564682006836,188.8564682006836,188.8564682006836,189.2335433959961,189.2335433959961,189.3609390258789,189.3609390258789,187.1458435058594,187.1458435058594,187.4758987426758,187.8227081298828,188.1886367797852,188.5695266723633,188.5695266723633,188.9589233398438,189.3550720214844,189.3550720214844,189.4315795898438,189.4315795898438,187.2726669311523,187.601203918457,187.601203918457,187.9528579711914,187.9528579711914,188.3204879760742,188.3204879760742,188.7014923095703,188.7014923095703,189.0776824951172,189.0776824951172,189.4604415893555,189.5010986328125,189.5010986328125,189.5010986328125,187.3952484130859,187.3952484130859,187.7229690551758,188.0683059692383,188.4341735839844,188.8095169067383,189.2011947631836,189.2011947631836,189.5695190429688,189.5695190429688,189.5695190429688,187.255500793457,187.255500793457,187.5533065795898,187.5533065795898,187.8798446655273,187.8798446655273,188.2229766845703,188.585563659668,188.9596252441406,189.3508605957031,189.6367797851562,189.6367797851562,187.4206924438477,187.4206924438477,187.7212982177734,187.7212982177734,188.0461578369141,188.3977661132812,188.3977661132812,188.3977661132812,188.7624053955078,188.7624053955078,188.7624053955078,189.181770324707,189.181770324707,189.5790481567383,189.5790481567383,189.7030029296875,189.7030029296875,187.6349105834961,187.9410552978516,188.2714080810547,188.2714080810547,188.6271133422852,188.6271133422852,188.9931411743164,188.9931411743164,189.3669052124023,189.3669052124023,189.7560043334961,189.7560043334961,187.5294647216797,187.5294647216797,187.8012847900391,188.0613174438477,188.0613174438477,188.3615798950195,188.6830139160156,188.6830139160156,189.0144729614258,189.0144729614258,189.328239440918,189.328239440918,189.663932800293,189.663932800293,189.8321990966797,189.8321990966797,189.8321990966797,187.6534881591797,187.6534881591797,187.8919067382812,187.8919067382812,188.164421081543,188.164421081543,188.4632568359375,188.4632568359375,188.82421875,188.82421875,189.0920257568359,189.0920257568359,189.3929290771484,189.712890625,189.712890625,189.8952102661133,189.8952102661133,187.8075180053711,188.0717239379883,188.0717239379883,188.3540496826172,188.3540496826172,188.6760787963867,188.6760787963867,188.6760787963867,189.0207061767578,189.0207061767578,189.0207061767578,189.3739776611328,189.3739776611328,189.7213592529297,189.7213592529297,189.9572448730469,189.9572448730469,189.9572448730469,187.8949356079102,187.8949356079102,188.1514663696289,188.1514663696289,188.4381942749023,188.4381942749023,188.7569122314453,189.1094131469727,189.1094131469727,189.4691162109375,189.4691162109375,189.856201171875,189.856201171875,190.0182418823242,190.0182418823242,190.0182418823242,190.0182418823242,190.0182418823242,190.0182418823242,190.0182418823242,190.0182418823242,190.0182418823242,190.0182418823242,190.0182418823242,190.0182418823242,190.0182418823242,190.0182418823242,190.0182418823242,190.0182418823242,190.0182418823242,190.0182418823242,188.0447463989258,188.0447463989258,188.2602767944336,188.4630584716797,188.6546783447266,188.6546783447266,188.9035186767578,188.9035186767578,189.1400451660156,189.1400451660156,189.3939743041992,189.3939743041992,189.6389236450195,189.6389236450195,189.9162368774414,189.9162368774414,190.0780334472656,190.0780334472656,188.0586853027344,188.0586853027344,188.2875137329102,188.2875137329102,188.5489730834961,188.5489730834961,188.5489730834961,188.8369750976562,189.1608810424805,189.1608810424805,189.4681091308594,189.4681091308594,189.7892150878906,189.7892150878906,190.1282501220703,190.1282501220703,190.1371841430664,190.1371841430664,188.2983093261719,188.2983093261719,188.2983093261719,188.5550003051758,188.5550003051758,188.8427810668945,188.8427810668945,189.1679382324219,189.4984283447266,189.8418350219727,190.1952438354492,190.1952438354492,190.1952438354492,190.1952438354492,188.4002685546875,188.6478576660156,188.6478576660156,188.9339981079102,188.9339981079102,189.2522048950195,189.5804901123047,189.5804901123047,189.9244003295898,189.9244003295898,190.2525405883789,190.2525405883789,190.2525405883789,190.2525405883789,190.2525405883789,190.2525405883789,188.4919052124023,188.4919052124023,188.7488021850586,189.0559463500977,189.0559463500977,189.3784255981445,189.3784255981445,189.7192535400391,190.0805587768555,190.3087997436523,190.3087997436523,190.3087997436523,188.4450912475586,188.4450912475586,188.7088317871094,188.7088317871094,188.7088317871094,189.0059585571289,189.0059585571289,189.3388366699219,189.7275161743164,189.7275161743164,190.0907135009766,190.0907135009766,190.0907135009766,190.364143371582,190.364143371582,188.5158386230469,188.5158386230469,188.7874755859375,188.7874755859375,189.0912094116211,189.0912094116211,189.4141082763672,189.4141082763672,189.7722778320312,189.7722778320312,190.1489791870117,190.1489791870117,190.4186935424805,190.4186935424805,190.4186935424805,188.6128082275391,188.874755859375,188.874755859375,189.1684722900391,189.5027694702148,189.5027694702148,189.8560256958008,189.8560256958008,189.8560256958008,190.2243423461914,190.2243423461914,190.2243423461914,190.4722747802734,190.4722747802734,190.4722747802734,188.7110977172852,188.983268737793,189.2922058105469,189.2922058105469,189.6361389160156,189.6361389160156,189.9989166259766,190.3827896118164,190.3827896118164,190.5249862670898,190.5249862670898,190.5249862670898,188.8714752197266,188.8714752197266,188.8714752197266,189.1523895263672,189.4755630493164,189.8326034545898,190.2070236206055,190.2070236206055,190.2070236206055,190.5769195556641,190.5769195556641,190.5769195556641,188.7955093383789,188.7955093383789,189.0562515258789,189.3789672851562,189.3789672851562,189.7130813598633,189.7130813598633,189.7130813598633,190.0699920654297,190.0699920654297,190.4423370361328,190.4423370361328,190.6279907226562,190.6279907226562,188.9779052734375,188.9779052734375,188.9779052734375,189.2481842041016,189.5586013793945,189.9058685302734,190.2716827392578,190.2716827392578,190.6505889892578,190.6781387329102,190.6781387329102,189.1658477783203,189.4517669677734,189.4517669677734,189.7779083251953,190.1310272216797,190.1310272216797,190.5063095092773,190.5063095092773,190.7276077270508,190.7276077270508,190.7276077270508,189.1148223876953,189.1148223876953,189.1148223876953,189.3889007568359,189.3889007568359,189.7007217407227,189.7007217407227,190.0071105957031,190.0071105957031,190.3529510498047,190.3529510498047,190.7028503417969,190.7028503417969,190.7762145996094,190.7762145996094,190.7762145996094,189.2231903076172,189.4713363647461,189.4713363647461,189.7281036376953,189.9996871948242,189.9996871948242,190.3154830932617,190.6122589111328,190.6122589111328,190.8240585327148,190.8240585327148,190.8240585327148,190.8240585327148,189.3805923461914,189.3805923461914,189.6145172119141,189.6145172119141,189.8973846435547,190.2225036621094,190.2225036621094,190.2225036621094,190.568359375,190.568359375,190.568359375,190.8710556030273,190.8710556030273,190.8710556030273,189.2582015991211,189.2582015991211,189.2582015991211,189.514030456543,189.514030456543,189.8082885742188,189.8082885742188,190.1771621704102,190.1771621704102,190.1771621704102,190.5359878540039,190.9148406982422,190.9148406982422,190.9173736572266,190.9173736572266,189.5539779663086,189.8422241210938,189.8422241210938,190.167839050293,190.5232315063477,190.5232315063477,190.89892578125,190.9629745483398,190.9629745483398,190.9629745483398,189.5819396972656,189.5819396972656,189.8614730834961,190.1821365356445,190.5321426391602,190.5321426391602,190.8964462280273,190.8964462280273,191.0077133178711,191.0077133178711,191.0077133178711,189.6162643432617,189.6162643432617,189.8897857666016,190.2057189941406,190.2057189941406,190.2057189941406,190.5547103881836,190.9239349365234,190.9239349365234,191.0518493652344,191.0518493652344,191.0518493652344,189.6735458374023,189.6735458374023,189.941032409668,189.941032409668,190.2498779296875,190.5921173095703,190.9521026611328,190.9521026611328,190.9521026611328,191.0951690673828,191.0951690673828,191.0951690673828,191.0951690673828,191.0951690673828,191.0951690673828,191.0951690673828,191.0951690673828,191.0951690673828,191.0951690673828,191.0951690673828,191.0951690673828,191.0951690673828,191.0951690673828,191.0951690673828,191.0951690673828,191.0951690673828,191.0951690673828,191.0951690673828,191.0951690673828,191.0951690673828,191.0951690673828,191.0951690673828,191.0951690673828,191.0951690673828,191.0951690673828,191.0951690673828,191.0951690673828,191.0951690673828,191.0951690673828,191.0951690673828,191.0951690673828,191.0951690673828,191.0951690673828,191.0951690673828,191.0951690673828,191.0951690673828,191.0951690673828,191.0951690673828,191.0951690673828,191.0951690673828,191.0951690673828,191.0951690673828,191.0951690673828,191.0951690673828,191.0951690673828,191.0951690673828,191.0951690673828,191.0951690673828,191.0951690673828,189.6018905639648,189.6018905639648,189.6092376708984,189.8483581542969,189.8483581542969,190.1040115356445,190.1040115356445,190.3837890625,190.6941528320312,190.6941528320312,190.9870452880859,190.9870452880859,191.2844619750977,191.2844619750977,191.6201553344727,191.6201553344727,191.6201553344727,191.9800643920898,191.9800643920898,192.3760757446289,192.7163238525391,192.7163238525391,193.0420074462891,193.3709106445312,193.3709106445312,193.7014617919922,193.7014617919922,194.0297088623047,194.357551574707,194.357551574707,194.4392013549805,194.4392013549805,194.4392013549805,189.9726867675781,190.2986679077148,190.2986679077148,190.6470260620117,190.6470260620117,190.9835586547852,190.9835586547852,190.9835586547852,191.3257369995117,191.3257369995117,191.3257369995117,191.6989669799805,191.6989669799805,192.0939025878906,192.4960327148438,192.9064025878906,193.3576202392578,193.3576202392578,193.7648468017578,193.7648468017578,194.1738739013672,194.1738739013672,194.5488739013672,194.5488739013672,194.5715103149414,194.5715103149414,194.5715103149414,190.1094741821289,190.1094741821289,190.371467590332,190.371467590332,190.6690902709961,190.6690902709961,190.8807601928711,190.8807601928711,191.0142974853516,191.1489639282227,191.2973403930664,191.2973403930664,191.5214080810547,191.5214080810547,191.7936935424805,191.9839706420898,191.9839706420898,192.2339935302734,192.2339935302734,192.2339935302734,192.4765472412109,192.6259765625,192.7337188720703,192.7337188720703,192.8553237915039,192.8553237915039,193.0451889038086,193.0451889038086,193.2182083129883,193.2182083129883,193.4447784423828,193.4447784423828,193.7141036987305,193.7141036987305,193.9831771850586,193.9831771850586,194.2527084350586,194.4484710693359,194.6492309570312,194.6492309570312,194.7016830444336,194.7016830444336,194.7016830444336,194.7016830444336,194.7016830444336,194.7016830444336,190.4475555419922,190.7422256469727,190.7422256469727,191.0730056762695,191.0730056762695,191.4004516601562,191.4004516601562,191.757682800293,191.757682800293,191.757682800293,192.1192092895508,192.4975128173828,192.4975128173828,192.8910598754883,192.8910598754883,193.288932800293,193.6935119628906,193.6935119628906,194.1015701293945,194.5089492797852,194.8297348022461,194.8297348022461,194.8297348022461,194.8297348022461,194.8297348022461,194.8297348022461,190.6944198608398,191.0299453735352,191.0299453735352,191.3547592163086,191.3547592163086,191.7132720947266,191.7132720947266,191.7132720947266,192.091926574707,192.091926574707,192.4822463989258,192.8766937255859,192.8766937255859,193.271125793457,193.271125793457,193.6686325073242,194.0552673339844,194.4289016723633,194.7407989501953,194.9557266235352,194.9557266235352,194.9557266235352,194.9557266235352,194.9557266235352,194.9557266235352,190.7817001342773,190.7817001342773,191.0674896240234,191.3739166259766,191.3739166259766,191.6878433227539,191.9945755004883,191.9945755004883,192.3353500366211,192.3353500366211,192.6865005493164,192.6865005493164,192.6865005493164,193.0509414672852,193.4316177368164,193.826057434082,193.826057434082,193.826057434082,194.2688140869141,194.6780242919922,195.0673828125,195.0673828125,195.0796966552734,195.0796966552734,190.982292175293,191.2731552124023,191.5685424804688,191.5685424804688,191.9013595581055,192.2568969726562,192.2568969726562,192.625373840332,192.97509765625,192.97509765625,193.3631439208984,193.76123046875,193.76123046875,194.1582260131836,194.1582260131836,194.5644760131836,194.9672775268555,194.9672775268555,195.2017135620117,195.2017135620117,195.2017135620117,195.2017135620117,195.2017135620117,195.2017135620117,191.2610397338867,191.2610397338867,191.5584869384766,191.5584869384766,191.8662567138672,191.8662567138672,192.2165222167969,192.2165222167969,192.5811614990234,192.5811614990234,192.9459762573242,192.9459762573242,193.325569152832,193.325569152832,193.6980514526367,194.0706024169922,194.0706024169922,194.4999771118164,194.4999771118164,194.8971481323242,195.2629470825195,195.2629470825195,195.3216247558594,195.3216247558594,191.2610931396484,191.2610931396484,191.2610931396484,191.5077819824219,191.7815246582031,191.7815246582031,192.0891494750977,192.0891494750977,192.430305480957,192.430305480957,192.7839889526367,193.0913162231445,193.0913162231445,193.4655685424805,193.4655685424805,193.8533935546875,193.8533935546875,194.2276611328125,194.6349563598633,194.6349563598633,195.0453796386719,195.4397430419922,195.4397430419922,195.4397430419922,195.4397430419922,191.5045166015625,191.7753295898438,191.7753295898438,192.0579833984375,192.0579833984375,192.390007019043,192.390007019043,192.7376556396484,193.1012420654297,193.4760055541992,193.4760055541992,193.8729476928711,193.8729476928711,193.8729476928711,194.3170928955078,194.3170928955078,194.7220458984375,194.7220458984375,195.1330795288086,195.1330795288086,195.5275039672852,195.5275039672852,195.5275039672852,195.5559234619141,195.5559234619141,195.5559234619141,191.6959915161133,191.6959915161133,191.9565887451172,191.9565887451172,192.2392654418945,192.2392654418945,192.5665054321289,192.9164276123047,192.9164276123047,192.9164276123047,193.2712631225586,193.2712631225586,193.6407699584961,193.6407699584961,194.0269927978516,194.0269927978516,194.3777694702148,194.6308059692383,194.6308059692383,194.9831619262695,195.281494140625,195.281494140625,195.281494140625,195.5909652709961,195.670166015625,195.670166015625,195.670166015625,191.7414245605469,191.9779663085938,191.9779663085938,192.2078704833984,192.2078704833984,192.2078704833984,192.4707794189453,192.7792587280273,193.1187515258789,193.1187515258789,193.4476165771484,193.4476165771484,193.7788772583008,194.1200714111328,194.4862213134766,194.4862213134766,194.8429641723633,195.2346649169922,195.2346649169922,195.6082382202148,195.6082382202148,195.6082382202148,195.7826385498047,195.7826385498047,195.7826385498047,195.7826385498047,195.7826385498047,195.7826385498047,192.1111221313477,192.1111221313477,192.3505783081055,192.6271820068359,192.6271820068359,192.8982696533203,192.8982696533203,193.2283630371094,193.2283630371094,193.5570755004883,193.9090805053711,194.2533721923828,194.6165008544922,194.995231628418,194.995231628418,195.3782730102539,195.3782730102539,195.7574768066406,195.7574768066406,195.8931884765625,195.8931884765625,192.11767578125,192.11767578125,192.349723815918,192.349723815918,192.5927581787109,192.8750305175781,193.2004013061523,193.2004013061523,193.5408096313477,193.5408096313477,193.5408096313477,193.8919143676758,193.8919143676758,194.2571334838867,194.2571334838867,194.6398696899414,195.0358428955078,195.4357528686523,195.8327484130859,196.002082824707,196.002082824707,192.2858276367188,192.2858276367188,192.5300750732422,192.5300750732422,192.7947540283203,192.7947540283203,193.0940551757812,193.4251937866211,193.4251937866211,193.772819519043,193.772819519043,194.1265640258789,194.1265640258789,194.4964599609375,194.8855590820312,195.2858276367188,195.6908798217773,196.0848693847656,196.0848693847656,196.1091537475586,196.1091537475586,192.5361099243164,192.5361099243164,192.7801513671875,193.0624008178711,193.0624008178711,193.3742523193359,193.7423934936523,193.7423934936523,194.0870361328125,194.0870361328125,194.4482879638672,194.4482879638672,194.8317794799805,195.2288589477539,195.6296081542969,195.6296081542969,195.6296081542969,196.0305404663086,196.2145004272461,196.2145004272461,196.2145004272461,192.5969848632812,192.8375396728516,192.8375396728516,193.0757904052734,193.3674621582031,193.3674621582031,193.3674621582031,193.6882705688477,193.6882705688477,194.030029296875,194.3862991333008,194.3862991333008,194.7568664550781,194.7568664550781,195.1516723632812,195.1516723632812,195.5543899536133,195.5543899536133,195.9578094482422,196.3181304931641,196.3181304931641,196.3181304931641,196.3181304931641,192.8926315307617,193.1143646240234,193.1143646240234,193.38916015625,193.38916015625,193.6864166259766,193.6864166259766,194.016487121582,194.3625259399414,194.3625259399414,194.7238311767578,194.7238311767578,195.0986480712891,195.0986480712891,195.4964904785156,195.4964904785156,195.9058380126953,195.9058380126953,196.3059692382812,196.3059692382812,196.4201583862305,196.4201583862305,196.4201583862305,192.9853363037109,192.9853363037109,193.2236328125,193.2236328125,193.494743347168,193.494743347168,193.7858734130859,193.7858734130859,194.0938186645508,194.0938186645508,194.4267272949219,194.4267272949219,194.4267272949219,194.7588882446289,194.7588882446289,195.1059646606445,195.1059646606445,195.4724273681641,195.8631896972656,195.8631896972656,196.2588424682617,196.2588424682617,196.5204772949219,196.5204772949219,196.5204772949219,196.5204772949219,193.2479629516602,193.4931411743164,193.4931411743164,193.7647552490234,193.7647552490234,194.0662384033203,194.0662384033203,194.3978576660156,194.3978576660156,194.7485275268555,195.1117630004883,195.4912719726562,195.4912719726562,195.7202453613281,195.7202453613281,196.0988159179688,196.4907836914062,196.4907836914062,196.4907836914062,196.6192092895508,196.6192092895508,196.6192092895508,196.6192092895508,196.6192092895508,196.6192092895508,193.4371871948242,193.4371871948242,193.4371871948242,193.6921310424805,193.6921310424805,193.9715423583984,193.9715423583984,194.2815551757812,194.6231079101562,194.9773406982422,194.9773406982422,195.3465423583984,195.3465423583984,195.7324066162109,195.7324066162109,196.136604309082,196.5356140136719,196.7163238525391,196.7163238525391,196.7163238525391,196.7163238525391,196.7163238525391,196.7163238525391,196.7163238525391,196.7163238525391,196.7163238525391,196.7163238525391,196.7163238525391,196.7163238525391,196.7163238525391,196.7163238525391,196.7163238525391,196.7163238525391,196.7163238525391,196.7163238525391,196.7163238525391,196.7163238525391,196.7163238525391,196.7163238525391,196.7163238525391,196.7163238525391,196.7163238525391,196.7163238525391,196.7163238525391,196.7163238525391,196.7163238525391,196.7163238525391,196.7163238525391,196.7163238525391,196.7163238525391,196.7163238525391,196.7163238525391,196.7163238525391,196.7163238525391,196.7163238525391,196.7163238525391,193.5284118652344,193.5284118652344,193.7306900024414,193.7306900024414,193.955810546875,194.1932983398438,194.4654693603516,194.769157409668,194.769157409668,195.0942001342773,195.4377746582031,195.799186706543,196.179817199707,196.179817199707,196.179817199707,196.5770874023438,196.5770874023438,196.8117065429688,196.8117065429688,196.8117065429688,196.8117065429688,196.8117065429688,196.8117065429688,193.7060546875,193.7060546875,193.9537811279297,193.9537811279297,194.2281112670898,194.2281112670898,194.5305938720703,194.5305938720703,194.8687896728516,195.2205429077148,195.5895690917969,195.5895690917969,195.9756393432617,195.9756393432617,195.9756393432617,196.3785781860352,196.7800674438477,196.7800674438477,196.9057083129883,196.9057083129883,193.6749267578125,193.8707809448242,193.8707809448242,194.1337966918945,194.1337966918945,194.3622665405273,194.3622665405273,194.6718215942383,194.6718215942383,195.0115432739258,195.0115432739258,195.3673934936523,195.3673934936523,195.7343215942383,195.7343215942383,196.107795715332,196.107795715332,196.5054244995117,196.5054244995117,196.9075622558594,196.9075622558594,196.9982833862305,196.9982833862305,196.9982833862305,193.8524475097656,193.8524475097656,194.0837478637695,194.3367233276367,194.3367233276367,194.6197509765625,194.9368591308594,194.9368591308594,194.9368591308594,195.2785568237305,195.2785568237305,195.6350555419922,196.00537109375,196.00537109375,196.3989028930664,196.8045043945312,197.089241027832,197.089241027832,197.089241027832,197.089241027832,197.089241027832,197.089241027832,194.1190948486328,194.1190948486328,194.3628234863281,194.3628234863281,194.6325149536133,194.6325149536133,194.9348602294922,194.9348602294922,195.2706146240234,195.6205215454102,195.984733581543,196.4111862182617,196.4111862182617,196.8142242431641,196.8142242431641,197.1788635253906,197.1788635253906,197.1788635253906,197.1788635253906,197.1788635253906,197.1788635253906,194.2070999145508,194.2070999145508,194.4430084228516,194.704963684082,194.704963684082,195.0014953613281,195.0014953613281,195.332275390625,195.332275390625,195.6798858642578,195.6798858642578,196.0387344360352,196.0387344360352,196.4256439208984,196.8268508911133,197.2242889404297,197.2242889404297,197.2668991088867,197.2668991088867,197.2668991088867,194.3018035888672,194.3018035888672,194.5345458984375,194.5345458984375,194.7912673950195,194.7912673950195,195.0806274414062,195.0806274414062,195.3899307250977,195.7365646362305,196.0936431884766,196.0936431884766,196.4656219482422,196.4656219482422,196.4656219482422,196.8591918945312,197.2589416503906,197.2589416503906,197.3536834716797,197.3536834716797,194.3972854614258,194.3972854614258,194.6285781860352,194.6285781860352,194.8805618286133,194.8805618286133,195.1648178100586,195.485107421875,195.485107421875,195.8676223754883,195.8676223754883,195.8676223754883,196.2255859375,196.2255859375,196.6095657348633,196.6095657348633,197.0081939697266,197.0081939697266,197.4044418334961,197.4044418334961,197.4044418334961,197.4388809204102,197.4388809204102,194.549430847168,194.549430847168,194.7764434814453,195.0296783447266,195.0296783447266,195.0296783447266,195.3130493164062,195.3130493164062,195.632942199707,195.9770660400391,195.9770660400391,196.332405090332,196.332405090332,196.7109603881836,196.7109603881836,197.1043853759766,197.4975738525391,197.4975738525391,197.5228500366211,197.5228500366211,197.5228500366211,197.5228500366211,194.7003936767578,194.7003936767578,194.9317016601562,194.9317016601562,195.1873474121094,195.1873474121094,195.4728240966797,195.7989273071289,196.1472473144531,196.5041122436523,196.5041122436523,196.8875122070312,196.8875122070312,197.2845077514648,197.6054000854492,197.6054000854492,197.6054000854492,197.6054000854492,197.6054000854492,197.6054000854492,194.8898468017578,194.8898468017578,195.1253356933594,195.4188385009766,195.4188385009766,195.7227630615234,196.0602569580078,196.0602569580078,196.413459777832,196.413459777832,196.413459777832,196.7809524536133,197.1720428466797,197.1720428466797,197.5683135986328,197.6865768432617,197.6865768432617,197.6865768432617,194.9034576416016,195.1324844360352,195.1324844360352,195.3813629150391,195.3813629150391,195.638557434082,195.638557434082,195.9520874023438,196.3001022338867,196.3001022338867,196.6587753295898,197.0371704101562,197.4337005615234,197.4337005615234,197.7665557861328,197.7665557861328,197.7665557861328,197.7665557861328,195.1251068115234,195.1251068115234,195.3591918945312,195.3591918945312,195.6204986572266,195.6204986572266,195.6204986572266,195.9145278930664,196.248176574707,196.248176574707,196.6010360717773,196.6010360717773,196.9660949707031,197.3545532226562,197.3545532226562,197.7466125488281,197.8451614379883,197.8451614379883,195.1581802368164,195.1581802368164,195.1581802368164,195.3873825073242,195.6656494140625,195.6656494140625,195.6656494140625,195.9542770385742,195.9542770385742,196.2799758911133,196.2799758911133,196.6309127807617,196.9774780273438,196.9774780273438,197.3482131958008,197.7396011352539,197.7396011352539,197.922492980957,197.922492980957,197.922492980957,197.922492980957,195.4301300048828,195.4301300048828,195.6656188964844,195.6656188964844,195.9268569946289,196.2282333374023,196.2282333374023,196.5655822753906,196.9208145141602,196.9208145141602,197.2912979125977,197.2912979125977,197.6842956542969,197.998649597168,197.998649597168,197.998649597168,197.998649597168,195.4951248168945,195.7292251586914,195.7292251586914,195.9917602539062,195.9917602539062,196.2891082763672,196.6274719238281,196.6274719238281,196.9830551147461,197.3520889282227,197.7443771362305,197.7443771362305,198.0735855102539,198.0735855102539,198.0735855102539,198.0735855102539,198.0735855102539,198.0735855102539,195.623405456543,195.823371887207,196.0830307006836,196.0830307006836,196.0830307006836,196.3795852661133,196.3795852661133,196.7098846435547,197.0642700195312,197.0642700195312,197.4300231933594,197.4300231933594,197.8192367553711,198.1471786499023,198.1471786499023,198.1471786499023,198.1471786499023,198.1471786499023,198.1471786499023,195.6968231201172,195.6968231201172,195.9215621948242,195.9215621948242,196.1812896728516,196.1812896728516,196.1812896728516,196.4760665893555,196.4760665893555,196.8105087280273,196.8105087280273,197.1664428710938,197.5386123657227,197.5386123657227,197.9290618896484,197.9290618896484,198.2197113037109,198.2197113037109,198.2197113037109,198.2197113037109,195.8320236206055,195.8320236206055,196.0645294189453,196.0645294189453,196.3253784179688,196.6199111938477,196.6199111938477,196.9508590698242,196.9508590698242,197.3003005981445,197.6626052856445,197.6626052856445,198.0477752685547,198.0477752685547,198.2909927368164,198.2909927368164,198.2909927368164,198.2909927368164,198.2909927368164,198.2909927368164,195.9947128295898,196.2301330566406,196.2301330566406,196.4956970214844,196.4956970214844,196.7990570068359,196.7990570068359,196.7990570068359,197.1329727172852,197.1329727172852,197.4677810668945,197.4677810668945,197.8271408081055,197.8271408081055,198.2039642333984,198.3611755371094,198.3611755371094,198.3611755371094,198.3611755371094,198.3611755371094,198.3611755371094,196.1177444458008,196.3530731201172,196.3530731201172,196.6198425292969,196.6198425292969,196.9247131347656,197.261848449707,197.261848449707,197.6152954101562,197.6152954101562,197.6152954101562,197.9843063354492,197.9843063354492,198.3622589111328,198.3622589111328,198.4301910400391,198.4301910400391,198.4301910400391,198.4301910400391,198.4301910400391,198.4301910400391,198.4301910400391,198.4301910400391,198.4301910400391,198.4301910400391,198.4301910400391,198.4301910400391,198.4301910400391,198.4301910400391,198.4301910400391,198.4301910400391,198.4301910400391,198.4301910400391,198.4301910400391,198.4301910400391,198.4301910400391,198.4301910400391,198.4301910400391,198.4301910400391,198.4301910400391,198.4301910400391,198.4301910400391,198.4301910400391,198.4301910400391,198.4301910400391,196.0541305541992,196.0541305541992,196.0541305541992,196.146125793457,196.3531723022461,196.3531723022461,196.583366394043,196.583366394043,196.8335876464844,196.8335876464844,197.1211776733398,197.1211776733398,197.443000793457,197.443000793457,197.7758941650391,197.7758941650391,198.1317443847656,198.4978103637695,198.4978103637695,198.4978103637695,198.4978103637695,198.4978103637695,198.4978103637695,196.2278900146484,196.2278900146484,196.4563446044922,196.4563446044922,196.7090148925781,196.7090148925781,196.9992141723633,197.326545715332,197.326545715332,197.6778411865234,197.6778411865234,198.0434722900391,198.0434722900391,198.4305953979492,198.4305953979492,198.5646514892578,198.5646514892578,198.5646514892578,198.5646514892578,198.5646514892578,198.5646514892578,196.4772720336914,196.4772720336914,196.7192306518555,196.7192306518555,197.0238189697266,197.0238189697266,197.3462371826172,197.6940307617188,198.0574188232422,198.0574188232422,198.4369964599609,198.4369964599609,198.63037109375,198.63037109375,198.63037109375,198.63037109375,196.5394668579102,196.5394668579102,196.7779388427734,197.0482406616211,197.357536315918,197.357536315918,197.6995544433594,197.6995544433594,198.0564575195312,198.0564575195312,198.4302215576172,198.4302215576172,198.6950759887695,198.6950759887695,198.6950759887695,198.6950759887695,198.6950759887695,198.6950759887695,196.5652847290039,196.5652847290039,196.7837982177734,196.7837982177734,197.0386123657227,197.3365707397461,197.6706085205078,197.6706085205078,198.0266494750977,198.395149230957,198.395149230957,198.7587509155273,198.7587509155273,198.7587509155273,198.7587509155273,198.7587509155273,198.7587509155273,196.6132659912109,196.8403854370117,197.1200485229492,197.417350769043,197.7528076171875,198.1103820800781,198.1103820800781,198.1103820800781,198.48291015625,198.48291015625,198.8213882446289,198.8213882446289,198.8213882446289,198.8213882446289,196.7259902954102,196.7259902954102,196.9525299072266,197.2059860229492,197.4972381591797,197.4972381591797,197.8251876831055,197.8251876831055,198.18017578125,198.18017578125,198.5469207763672,198.5469207763672,198.8829650878906,198.8829650878906,198.8829650878906,198.8829650878906,198.8829650878906,198.8829650878906,196.8204879760742,196.8204879760742,197.0482482910156,197.0482482910156,197.3007736206055,197.3007736206055,197.3007736206055,197.5910110473633,197.5910110473633,197.5910110473633,197.9180755615234,197.9180755615234,198.2702560424805,198.2702560424805,198.6354217529297,198.9436187744141,198.9436187744141,198.9436187744141,198.9436187744141,198.9436187744141,198.9436187744141,196.9328918457031,196.9328918457031,196.9328918457031,197.1636199951172,197.1636199951172,197.4193572998047,197.7439880371094,197.7439880371094,198.0796203613281,198.0796203613281,198.4362411499023,198.4362411499023,198.8073806762695,199.0033111572266,199.0033111572266,199.0033111572266,199.0033111572266,197.0984191894531,197.0984191894531,197.3345794677734,197.599967956543,197.599967956543,197.9061584472656,197.9061584472656,198.2470703125,198.2470703125,198.6023941040039,198.6023941040039,198.9757614135742,199.0619659423828,199.0619659423828,199.0619659423828,199.0619659423828,197.2107467651367,197.2107467651367,197.4482345581055,197.4482345581055,197.720329284668,198.0302200317383,198.355224609375,198.355224609375,198.355224609375,198.7074508666992,199.0750045776367,199.0750045776367,199.1197052001953,199.1197052001953,199.1197052001953,199.1197052001953,197.3438415527344,197.6066360473633,197.8816299438477,197.8816299438477,197.8816299438477,198.1929168701172,198.1929168701172,198.532112121582,198.532112121582,198.8892059326172,198.8892059326172,199.176513671875,199.176513671875,199.176513671875,199.176513671875,197.2940139770508,197.5202484130859,197.7694931030273,198.0577774047852,198.0577774047852,198.3794097900391,198.3794097900391,198.728645324707,198.728645324707,199.0895462036133,199.0895462036133,199.2324447631836,199.2324447631836,199.2324447631836,199.2324447631836,197.4711151123047,197.7050933837891,197.9692916870117,197.9692916870117,198.2732315063477,198.2732315063477,198.6103210449219,198.6103210449219,198.9691543579102,198.9691543579102,199.287467956543,199.287467956543,199.287467956543,199.287467956543,199.287467956543,199.287467956543,197.4472274780273,197.4472274780273,197.6735916137695,197.9481658935547,198.2382888793945,198.2382888793945,198.5660858154297,198.5660858154297,198.9228286743164,198.9228286743164,198.9228286743164,199.2906188964844,199.2906188964844,199.3415069580078,199.3415069580078,199.3415069580078,199.3415069580078,199.3415069580078,199.3415069580078,199.3415069580078,199.3415069580078,199.3415069580078,199.3415069580078,199.3415069580078,199.3415069580078,199.3415069580078,199.3415069580078,199.3415069580078,199.3415069580078,199.3415069580078,199.3415069580078,197.6179428100586,197.6179428100586,197.8330307006836,198.0716934204102,198.0716934204102,198.3400497436523,198.6421890258789,198.6421890258789,198.6421890258789,198.9790802001953,198.9790802001953,199.3328857421875,199.3328857421875,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,199.3944931030273,197.5628128051758,197.5628128051758,197.5628128051758,197.5628128051758,197.7285766601562,197.7285766601562,197.9811019897461,197.9811019897461,197.9811019897461,198.2569198608398,198.2569198608398,198.5711975097656,198.5711975097656,198.9060211181641,198.9060211181641,199.2213516235352,199.2213516235352,199.5591735839844,199.5591735839844,199.9425582885742,199.9425582885742,200.3439254760742,200.7500991821289,200.7500991821289,201.1552963256836,201.1552963256836,201.5275115966797,201.8526153564453,201.8526153564453,202.1764831542969,202.5045013427734,202.5045013427734,202.8289642333984,202.8289642333984,203.1535797119141,203.4771118164062,203.7847671508789,204.114013671875,204.114013671875,204.437255859375,204.7616577148438,204.7616577148438,205.0869903564453,205.0869903564453,205.1754608154297,205.1754608154297,205.1754608154297,205.1754608154297,205.1754608154297,205.1754608154297,198.0322952270508,198.0322952270508,198.2929000854492,198.2929000854492,198.58544921875,198.58544921875,198.9100952148438,198.9100952148438,199.23974609375,199.23974609375,199.5604019165039,199.5604019165039,199.9175033569336,200.2998123168945,200.2998123168945,200.6953582763672,200.6953582763672,200.6953582763672,201.1029663085938,201.1029663085938,201.5103607177734,201.9159469604492,201.9159469604492,202.3219985961914,202.3219985961914,202.7300338745117,203.1376266479492,203.1376266479492,203.5424957275391,203.9509429931641,203.9509429931641,204.359260559082,204.359260559082,204.7351303100586,204.7351303100586,205.1250610351562,205.1250610351562,205.3837051391602,205.3837051391602,205.3837051391602,205.3837051391602,205.3837051391602,205.3837051391602,205.3837051391602,205.3837051391602,205.3837051391602,198.4363174438477,198.4363174438477,198.6972503662109,198.6972503662109,198.9928207397461,198.9928207397461,199.3108062744141,199.6227111816406,199.6227111816406,199.9694519042969,199.9694519042969,200.3323364257812,200.3323364257812,200.7210159301758,201.1240997314453,201.1240997314453,201.5787582397461,201.5787582397461,201.9914627075195,202.4035034179688,202.4035034179688,202.4035034179688,202.8146362304688,202.8146362304688,203.2275695800781,203.2275695800781,203.6398849487305,203.6398849487305,204.0496673583984,204.0496673583984,204.4579544067383,204.4579544067383,204.8710632324219,204.8710632324219,205.2663726806641,205.5885467529297,205.5885467529297,205.5885467529297,205.5885467529297,205.5885467529297,205.5885467529297,198.7264633178711,198.7264633178711,198.8918228149414,198.8918228149414,199.0571060180664,199.0571060180664,199.3635711669922,199.6798629760742,199.6798629760742,199.6798629760742,200.0058746337891,200.0058746337891,200.361328125,200.7326965332031,200.7326965332031,201.1027603149414,201.4984741210938,201.4984741210938,201.902099609375,201.902099609375,202.3053359985352,202.3053359985352,202.7104949951172,202.7104949951172,202.7104949951172,203.1176452636719,203.5280838012695,203.9360122680664,203.9360122680664,204.3432769775391,204.7552947998047,204.7552947998047,205.1671371459961,205.5609283447266,205.5609283447266,205.7900924682617,205.7900924682617,205.7900924682617,205.7900924682617,205.7900924682617,205.7900924682617,205.7900924682617,205.7900924682617,205.7900924682617,199.0052642822266,199.0052642822266,199.2567825317383,199.5336074829102,199.8247222900391,199.8247222900391,200.1260604858398,200.1260604858398,200.4691009521484,200.4691009521484,200.4691009521484,200.8230056762695,200.8230056762695,201.1945190429688,201.1945190429688,201.5828552246094,201.5828552246094,201.9797592163086,201.9797592163086,202.3864974975586,202.788932800293,203.1931610107422,203.5971069335938,203.5971069335938,204.001091003418,204.001091003418,204.4060516357422,204.4060516357422,204.8110733032227,204.8110733032227,205.2143096923828,205.2143096923828,205.6132202148438,205.9883880615234,205.9883880615234,205.9883880615234,205.9883880615234,205.9883880615234,205.9883880615234,199.2920608520508,199.540885925293,199.8051071166992,199.8051071166992,200.0839538574219,200.0839538574219,200.3822631835938,200.3822631835938,200.3822631835938,200.7205581665039,200.7205581665039,201.0668258666992,201.4731826782227,201.4731826782227,201.8630676269531,201.8630676269531,202.2607650756836,202.6669921875,203.0708694458008,203.4751663208008,203.8789520263672,203.8789520263672,204.2842864990234,204.2842864990234,204.6902236938477,204.6902236938477,205.0945358276367,205.5026321411133,205.5026321411133,205.8966293334961,206.1834945678711,206.1834945678711,206.1834945678711,206.1834945678711,206.1834945678711,206.1834945678711,206.1834945678711,206.1834945678711,206.1834945678711,199.6462554931641,199.6462554931641,199.8785934448242,199.8785934448242,200.1374206542969,200.4076232910156,200.4076232910156,200.7216033935547,201.0632247924805,201.0632247924805,201.4124298095703,201.7792816162109,201.7792816162109,202.1641006469727,202.5598678588867,202.9640960693359,203.365234375,203.7672653198242,203.7672653198242,204.172248840332,204.172248840332,204.5793991088867,204.5793991088867,204.988037109375,204.988037109375,205.3953552246094,205.3953552246094,205.8043518066406,206.1928558349609,206.1928558349609,206.3754119873047,206.3754119873047,206.3754119873047,206.3754119873047,206.3754119873047,206.3754119873047,206.3754119873047,206.3754119873047,206.3754119873047,206.3754119873047,206.3754119873047,206.3754119873047,206.3754119873047,206.3754119873047,206.3754119873047,206.3754119873047,206.3754119873047,206.3754119873047,206.3754119873047,206.3754119873047,206.3754119873047,206.3754119873047,206.3754119873047,206.3754119873047,199.9048385620117,200.1306076049805,200.1306076049805,200.3699569702148,200.3699569702148,200.6123123168945,200.6123123168945,200.8952484130859,201.2173843383789,201.2173843383789,201.5571212768555,201.9075393676758,201.9075393676758,202.275634765625,202.275634765625,202.660270690918,203.0551071166992,203.0551071166992,203.4574584960938,203.8594741821289,203.8594741821289,204.2651977539062,204.2651977539062,204.2651977539062,204.669189453125,205.0761184692383,205.4826965332031,205.8911743164062,205.8911743164062,206.2782363891602,206.2782363891602,206.5641555786133,206.5641555786133,206.5641555786133,206.5641555786133,206.5641555786133,206.5641555786133,200.2225036621094,200.4916229248047,200.4916229248047,200.7421875,200.9669876098633,200.9669876098633,201.2531890869141,201.2531890869141,201.5881271362305,201.9165115356445,201.9165115356445,202.2323989868164,202.6031494140625,202.6031494140625,202.9847717285156,202.9847717285156,203.3776168823242,203.7654876708984,203.7654876708984,204.1580047607422,204.1580047607422,204.560546875,204.560546875,204.9649124145508,205.370719909668,205.370719909668,205.7777099609375,205.7777099609375,206.1863327026367,206.5734710693359,206.5734710693359,206.7499847412109,206.7499847412109,206.7499847412109,206.7499847412109,206.7499847412109,206.7499847412109,206.7499847412109,206.7499847412109,206.7499847412109,200.5686340332031,200.8117141723633,200.8117141723633,201.0603866577148,201.3516082763672,201.3516082763672,201.6816787719727,201.6816787719727,202.0240936279297,202.0240936279297,202.3729248046875,202.3729248046875,202.7371673583984,202.7371673583984,203.1209335327148,203.5142440795898,203.9170837402344,203.9170837402344,204.3212585449219,204.7685317993164,204.7685317993164,205.1750717163086,205.1750717163086,205.583740234375,205.583740234375,205.9941787719727,206.4041061401367,206.4041061401367,206.794189453125,206.794189453125,206.9328155517578,206.9328155517578,206.9328155517578,206.9328155517578,206.9328155517578,206.9328155517578,200.6460189819336,200.6460189819336,200.8789291381836,201.1188049316406,201.3679122924805,201.3679122924805,201.6646423339844,201.9931564331055,201.9931564331055,202.3386688232422,202.3386688232422,202.6935043334961,202.6935043334961,203.0605545043945,203.0605545043945,203.4423904418945,203.4423904418945,203.8349990844727,204.2341613769531,204.2341613769531,212.0392684936523,212.0392684936523,212.0392684936523,212.0392684936523,212.0392684936523,212.0392684936523,212.0392684936523,212.0392684936523,212.0392684936523,212.0392684936523,212.0392684936523,212.0392684936523,212.0392684936523,212.0392684936523,212.0392684936523,212.0392684936523,212.0392684936523,212.0392684936523,212.0392684936523,212.0392684936523,219.6686630249023,219.6686706542969,219.6686706542969,219.6686706542969,219.6686706542969,219.6686706542969,219.6686706542969,219.6686706542969,219.6686706542969,219.6686706542969,219.6686706542969,219.6686706542969,219.6686706542969,219.6686706542969,219.6686706542969,219.6686706542969,219.6686706542969,219.6686706542969,219.6686706542969,219.6686706542969,219.6686706542969,219.6686706542969,219.6686706542969,234.9274597167969,234.9274597167969,234.9274597167969,234.9274597167969,234.9274597167969,234.9274597167969,234.9274597167969,234.9274597167969,234.9274597167969,234.9274597167969,234.9274597167969,234.9274597167969,234.9274597167969,234.9274597167969,234.9274597167969,234.9274597167969,234.9274597167969,234.9274597167969,242.6157150268555,242.6157150268555,242.6157150268555,242.6157150268555,242.6157150268555,242.6157150268555,242.6157150268555,242.6157150268555,242.6157150268555,242.6157150268555,242.6157150268555,242.6157150268555,242.6157150268555,242.6157150268555,242.6157150268555,242.6157150268555,242.6157150268555,242.6157150268555,242.6157150268555,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547,257.9520721435547],"meminc":[0,0,0,0,15.28223419189453,0,0,0,0.0003662109375,0,0,30.46537780761719,0,0,0,0,0,4.57763671875e-05,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-0.00030517578125,0,15.33312225341797,0.2405776977539062,0,0.2540359497070312,0,0.2774124145507812,0.32049560546875,0.384429931640625,0,0.351104736328125,0,0.3958587646484375,0,0.4062271118164062,0.3588943481445312,0,0,-2.806320190429688,0,0.3639755249023438,0,0.3798828125,0,0.416107177734375,0,0.4112472534179688,0,0.4083328247070312,0.4062728881835938,0,0.4070053100585938,-2.761604309082031,0,0,0.3598861694335938,0,0.36724853515625,0,0.3868179321289062,0,0.4065093994140625,0,0.4045486450195312,0.4061508178710938,0,0.4071273803710938,0,0,0.183013916015625,0,0,-2.535392761230469,0,0.3629531860351562,0.3817901611328125,0,0.4086837768554688,0,0,0.4085617065429688,0.404937744140625,0,0.4060592651367188,0,0.2429046630859375,0,-2.553047180175781,0,0.3498992919921875,0,0.3704299926757812,0,0,0.390655517578125,0.4035263061523438,0.4067535400390625,0,0.405548095703125,0,0,0.30548095703125,0,-2.573272705078125,0,0.3383407592773438,0,0.360443115234375,0,0.3702163696289062,0.3899688720703125,0,0.3947601318359375,0,0.3976287841796875,0,0.399749755859375,0,0,-2.596168518066406,0,0.3301773071289062,0,0.3607940673828125,0,0.374053955078125,0.3947601318359375,0,0.3960494995117188,0.4072265625,0,0.4058609008789062,0,-2.592025756835938,0,0,0.3197174072265625,0,0,0.3448028564453125,0,0,0.3606338500976562,0,0.3726882934570312,0,0.3929214477539062,0,0.40008544921875,0.403594970703125,0.07696533203125,0,-2.289268493652344,0,0.342315673828125,0,0.3583831787109375,0,0.373565673828125,0,0.3856735229492188,0,0.3864212036132812,0,0.398468017578125,0,0.11859130859375,0,-2.288139343261719,0.3402023315429688,0,0,0.3575973510742188,0,0.3757095336914062,0,0.3904953002929688,0.399200439453125,0.4007797241210938,0,0.09717559814453125,0,0,-2.233146667480469,0.3444747924804688,0,0.3451461791992188,0,0.3644866943359375,0,0.3678970336914062,0.3785781860351562,0,0,0.3770751953125,0,0.1273956298828125,0,-2.215095520019531,0,0.3300552368164062,0.3468093872070312,0.3659286499023438,0.380889892578125,0,0.3893966674804688,0.396148681640625,0,0.076507568359375,0,-2.158912658691406,0.3285369873046875,0,0.351654052734375,0,0.3676300048828125,0,0.3810043334960938,0,0.376190185546875,0,0.3827590942382812,0.04065704345703125,0,0,-2.105850219726562,0,0.3277206420898438,0.3453369140625,0.3658676147460938,0.3753433227539062,0.3916778564453125,0,0.3683242797851562,0,0,-2.314018249511719,0,0.2978057861328125,0,0.3265380859375,0,0.3431320190429688,0.3625869750976562,0.3740615844726562,0.3912353515625,0.285919189453125,0,-2.216087341308594,0,0.3006057739257812,0,0.324859619140625,0.3516082763671875,0,0,0.3646392822265625,0,0,0.4193649291992188,0,0.39727783203125,0,0.1239547729492188,0,-2.068092346191406,0.3061447143554688,0.330352783203125,0,0.3557052612304688,0,0.36602783203125,0,0.3737640380859375,0,0.38909912109375,0,-2.226539611816406,0,0.271820068359375,0.2600326538085938,0,0.300262451171875,0.3214340209960938,0,0.3314590454101562,0,0.3137664794921875,0,0.335693359375,0,0.1682662963867188,0,0,-2.1787109375,0,0.2384185791015625,0,0.2725143432617188,0,0.2988357543945312,0,0.3609619140625,0,0.2678070068359375,0,0.3009033203125,0.3199615478515625,0,0.1823196411132812,0,-2.087692260742188,0.2642059326171875,0,0.2823257446289062,0,0.3220291137695312,0,0,0.3446273803710938,0,0,0.353271484375,0,0.347381591796875,0,0.2358856201171875,0,0,-2.062309265136719,0,0.25653076171875,0,0.2867279052734375,0,0.3187179565429688,0.3525009155273438,0,0.3597030639648438,0,0.3870849609375,0,0.1620407104492188,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.973495483398438,0,0.2155303955078125,0.2027816772460938,0.191619873046875,0,0.24884033203125,0,0.2365264892578125,0,0.2539291381835938,0,0.2449493408203125,0,0.277313232421875,0,0.1617965698242188,0,-2.01934814453125,0,0.2288284301757812,0,0.2614593505859375,0,0,0.2880020141601562,0.3239059448242188,0,0.3072280883789062,0,0.32110595703125,0,0.3390350341796875,0,0.00893402099609375,0,-1.838874816894531,0,0,0.2566909790039062,0,0.28778076171875,0,0.3251571655273438,0.3304901123046875,0.3434066772460938,0.3534088134765625,0,0,0,-1.794975280761719,0.247589111328125,0,0.2861404418945312,0,0.318206787109375,0.3282852172851562,0,0.3439102172851562,0,0.3281402587890625,0,0,0,0,0,-1.760635375976562,0,0.25689697265625,0.3071441650390625,0,0.322479248046875,0,0.3408279418945312,0.3613052368164062,0.228240966796875,0,0,-1.86370849609375,0,0.2637405395507812,0,0,0.2971267700195312,0,0.3328781127929688,0.3886795043945312,0,0.3631973266601562,0,0,0.2734298706054688,0,-1.848304748535156,0,0.271636962890625,0,0.3037338256835938,0,0.3228988647460938,0,0.3581695556640625,0,0.3767013549804688,0,0.26971435546875,0,0,-1.805885314941406,0.2619476318359375,0,0.2937164306640625,0.3342971801757812,0,0.3532562255859375,0,0,0.368316650390625,0,0,0.2479324340820312,0,0,-1.761177062988281,0.2721710205078125,0.3089370727539062,0,0.34393310546875,0,0.3627777099609375,0.3838729858398438,0,0.1421966552734375,0,0,-1.653511047363281,0,0,0.280914306640625,0.3231735229492188,0.3570404052734375,0.374420166015625,0,0,0.3698959350585938,0,0,-1.781410217285156,0,0.2607421875,0.3227157592773438,0,0.3341140747070312,0,0,0.3569107055664062,0,0.372344970703125,0,0.1856536865234375,0,-1.65008544921875,0,0,0.2702789306640625,0.3104171752929688,0.3472671508789062,0.365814208984375,0,0.37890625,0.02754974365234375,0,-1.512290954589844,0.285919189453125,0,0.326141357421875,0.353118896484375,0,0.3752822875976562,0,0.2212982177734375,0,0,-1.612785339355469,0,0,0.274078369140625,0,0.3118209838867188,0,0.3063888549804688,0,0.3458404541015625,0,0.3498992919921875,0,0.0733642578125,0,0,-1.553024291992188,0.2481460571289062,0,0.2567672729492188,0.2715835571289062,0,0.3157958984375,0.2967758178710938,0,0.2117996215820312,0,0,0,-1.443466186523438,0,0.2339248657226562,0,0.282867431640625,0.3251190185546875,0,0,0.345855712890625,0,0,0.3026962280273438,0,0,-1.61285400390625,0,0,0.255828857421875,0,0.2942581176757812,0,0.3688735961914062,0,0,0.35882568359375,0.3788528442382812,0,0.002532958984375,0,-1.363395690917969,0.2882461547851562,0,0.3256149291992188,0.3553924560546875,0,0.3756942749023438,0.06404876708984375,0,0,-1.381034851074219,0,0.2795333862304688,0.3206634521484375,0.350006103515625,0,0.3643035888671875,0,0.11126708984375,0,0,-1.391448974609375,0,0.2735214233398438,0.3159332275390625,0,0,0.3489913940429688,0.3692245483398438,0,0.1279144287109375,0,0,-1.378303527832031,0,0.267486572265625,0,0.3088455200195312,0.3422393798828125,0.3599853515625,0,0,0.14306640625,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.493278503417969,0,0.00734710693359375,0.2391204833984375,0,0.2556533813476562,0,0.2797775268554688,0.31036376953125,0,0.2928924560546875,0,0.2974166870117188,0,0.335693359375,0,0,0.3599090576171875,0,0.3960113525390625,0.3402481079101562,0,0.32568359375,0.3289031982421875,0,0.3305511474609375,0,0.3282470703125,0.3278427124023438,0,0.0816497802734375,0,0,-4.466514587402344,0.3259811401367188,0,0.348358154296875,0,0.3365325927734375,0,0,0.3421783447265625,0,0,0.37322998046875,0,0.3949356079101562,0.402130126953125,0.410369873046875,0.4512176513671875,0,0.4072265625,0,0.409027099609375,0,0.375,0,0.02263641357421875,0,0,-4.4620361328125,0,0.261993408203125,0,0.2976226806640625,0,0.211669921875,0,0.1335372924804688,0.1346664428710938,0.14837646484375,0,0.2240676879882812,0,0.2722854614257812,0.190277099609375,0,0.2500228881835938,0,0,0.2425537109375,0.1494293212890625,0.1077423095703125,0,0.1216049194335938,0,0.1898651123046875,0,0.1730194091796875,0,0.2265701293945312,0,0.2693252563476562,0,0.269073486328125,0,0.26953125,0.1957626342773438,0.2007598876953125,0,0.05245208740234375,0,0,0,0,0,-4.254127502441406,0.2946701049804688,0,0.330780029296875,0,0.3274459838867188,0,0.3572311401367188,0,0,0.3615264892578125,0.3783035278320312,0,0.3935470581054688,0,0.3978729248046875,0.4045791625976562,0,0.4080581665039062,0.407379150390625,0.3207855224609375,0,0,0,0,0,-4.13531494140625,0.3355255126953125,0,0.3248138427734375,0,0.3585128784179688,0,0,0.3786544799804688,0,0.39031982421875,0.3944473266601562,0,0.3944320678710938,0,0.3975067138671875,0.3866348266601562,0.3736343383789062,0.3118972778320312,0.2149276733398438,0,0,0,0,0,-4.174026489257812,0,0.2857894897460938,0.306427001953125,0,0.3139266967773438,0.306732177734375,0,0.3407745361328125,0,0.3511505126953125,0,0,0.36444091796875,0.38067626953125,0.394439697265625,0,0,0.4427566528320312,0.409210205078125,0.3893585205078125,0,0.0123138427734375,0,-4.097404479980469,0.290863037109375,0.2953872680664062,0,0.3328170776367188,0.3555374145507812,0,0.3684768676757812,0.3497238159179688,0,0.3880462646484375,0.3980865478515625,0,0.3969955444335938,0,0.40625,0.402801513671875,0,0.23443603515625,0,0,0,0,0,-3.940673828125,0,0.2974472045898438,0,0.307769775390625,0,0.3502655029296875,0,0.3646392822265625,0,0.3648147583007812,0,0.3795928955078125,0,0.3724822998046875,0.3725509643554688,0,0.4293746948242188,0,0.3971710205078125,0.3657989501953125,0,0.05867767333984375,0,-4.060531616210938,0,0,0.2466888427734375,0.27374267578125,0,0.3076248168945312,0,0.341156005859375,0,0.3536834716796875,0.3073272705078125,0,0.3742523193359375,0,0.3878250122070312,0,0.374267578125,0.4072952270507812,0,0.4104232788085938,0.3943634033203125,0,0,0,-3.935226440429688,0.27081298828125,0,0.28265380859375,0,0.3320236206054688,0,0.3476486206054688,0.36358642578125,0.3747634887695312,0,0.396942138671875,0,0,0.4441452026367188,0,0.4049530029296875,0,0.4110336303710938,0,0.3944244384765625,0,0,0.02841949462890625,0,0,-3.859931945800781,0,0.2605972290039062,0,0.2826766967773438,0,0.327239990234375,0.3499221801757812,0,0,0.3548355102539062,0,0.3695068359375,0,0.3862228393554688,0,0.3507766723632812,0.2530364990234375,0,0.35235595703125,0.2983322143554688,0,0,0.3094711303710938,0.07920074462890625,0,0,-3.928741455078125,0.236541748046875,0,0.2299041748046875,0,0,0.262908935546875,0.3084793090820312,0.3394927978515625,0,0.3288650512695312,0,0.3312606811523438,0.3411941528320312,0.36614990234375,0,0.3567428588867188,0.3917007446289062,0,0.3735733032226562,0,0,0.1744003295898438,0,0,0,0,0,-3.671516418457031,0,0.2394561767578125,0.2766036987304688,0,0.271087646484375,0,0.3300933837890625,0,0.3287124633789062,0.3520050048828125,0.3442916870117188,0.363128662109375,0.3787307739257812,0,0.3830413818359375,0,0.3792037963867188,0,0.135711669921875,0,-3.7755126953125,0,0.2320480346679688,0,0.2430343627929688,0.2822723388671875,0.3253707885742188,0,0.3404083251953125,0,0,0.351104736328125,0,0.3652191162109375,0,0.3827362060546875,0.3959732055664062,0.3999099731445312,0.3969955444335938,0.1693344116210938,0,-3.716255187988281,0,0.2442474365234375,0,0.264678955078125,0,0.2993011474609375,0.3311386108398438,0,0.347625732421875,0,0.3537445068359375,0,0.3698959350585938,0.38909912109375,0.4002685546875,0.4050521850585938,0.3939895629882812,0,0.02428436279296875,0,-3.573043823242188,0,0.2440414428710938,0.2822494506835938,0,0.3118515014648438,0.3681411743164062,0,0.3446426391601562,0,0.3612518310546875,0,0.3834915161132812,0.3970794677734375,0.4007492065429688,0,0,0.4009323120117188,0.1839599609375,0,0,-3.617515563964844,0.2405548095703125,0,0.238250732421875,0.2916717529296875,0,0,0.3208084106445312,0,0.3417587280273438,0.3562698364257812,0,0.3705673217773438,0,0.394805908203125,0,0.4027175903320312,0,0.4034194946289062,0.360321044921875,0,0,0,-3.425498962402344,0.2217330932617188,0,0.2747955322265625,0,0.2972564697265625,0,0.3300704956054688,0.346038818359375,0,0.3613052368164062,0,0.37481689453125,0,0.3978424072265625,0,0.4093475341796875,0,0.4001312255859375,0,0.1141891479492188,0,0,-3.434822082519531,0,0.2382965087890625,0,0.2711105346679688,0,0.2911300659179688,0,0.3079452514648438,0,0.3329086303710938,0,0,0.3321609497070312,0,0.347076416015625,0,0.3664627075195312,0.3907623291015625,0,0.3956527709960938,0,0.2616348266601562,0,0,0,-3.272514343261719,0.24517822265625,0,0.2716140747070312,0,0.301483154296875,0,0.3316192626953125,0,0.3506698608398438,0.3632354736328125,0.3795089721679688,0,0.228973388671875,0,0.378570556640625,0.3919677734375,0,0,0.1284255981445312,0,0,0,0,0,-3.182022094726562,0,0,0.25494384765625,0,0.2794113159179688,0,0.3100128173828125,0.341552734375,0.3542327880859375,0,0.36920166015625,0,0.3858642578125,0,0.4041976928710938,0.3990097045898438,0.1807098388671875,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-3.187911987304688,0,0.2022781372070312,0,0.2251205444335938,0.23748779296875,0.2721710205078125,0.3036880493164062,0,0.325042724609375,0.3435745239257812,0.3614120483398438,0.3806304931640625,0,0,0.3972702026367188,0,0.234619140625,0,0,0,0,0,-3.10565185546875,0,0.2477264404296875,0,0.2743301391601562,0,0.3024826049804688,0,0.33819580078125,0.3517532348632812,0.3690261840820312,0,0.3860702514648438,0,0,0.4029388427734375,0.4014892578125,0,0.125640869140625,0,-3.230781555175781,0.1958541870117188,0,0.2630157470703125,0,0.2284698486328125,0,0.3095550537109375,0,0.3397216796875,0,0.3558502197265625,0,0.3669281005859375,0,0.37347412109375,0,0.3976287841796875,0,0.4021377563476562,0,0.09072113037109375,0,0,-3.145835876464844,0,0.2313003540039062,0.2529754638671875,0,0.2830276489257812,0.317108154296875,0,0,0.3416976928710938,0,0.3564987182617188,0.3703155517578125,0,0.3935317993164062,0.4056015014648438,0.2847366333007812,0,0,0,0,0,-2.970146179199219,0,0.2437286376953125,0,0.2696914672851562,0,0.3023452758789062,0,0.33575439453125,0.3499069213867188,0.3642120361328125,0.42645263671875,0,0.4030380249023438,0,0.3646392822265625,0,0,0,0,0,-2.971763610839844,0,0.2359085083007812,0.2619552612304688,0,0.2965316772460938,0,0.330780029296875,0,0.3476104736328125,0,0.3588485717773438,0,0.3869094848632812,0.4012069702148438,0.3974380493164062,0,0.04261016845703125,0,0,-2.965095520019531,0,0.2327423095703125,0,0.2567214965820312,0,0.2893600463867188,0,0.3093032836914062,0.3466339111328125,0.3570785522460938,0,0.371978759765625,0,0,0.3935699462890625,0.399749755859375,0,0.0947418212890625,0,-2.956398010253906,0,0.231292724609375,0,0.251983642578125,0,0.2842559814453125,0.3202896118164062,0,0.3825149536132812,0,0,0.3579635620117188,0,0.3839797973632812,0,0.3986282348632812,0,0.3962478637695312,0,0,0.0344390869140625,0,-2.889450073242188,0,0.2270126342773438,0.25323486328125,0,0,0.2833709716796875,0,0.3198928833007812,0.3441238403320312,0,0.3553390502929688,0,0.3785552978515625,0,0.3934249877929688,0.3931884765625,0,0.02527618408203125,0,0,0,-2.822456359863281,0,0.2313079833984375,0,0.255645751953125,0,0.2854766845703125,0.3261032104492188,0.3483200073242188,0.3568649291992188,0,0.3833999633789062,0,0.3969955444335938,0.320892333984375,0,0,0,0,0,-2.715553283691406,0,0.2354888916015625,0.2935028076171875,0,0.303924560546875,0.337493896484375,0,0.3532028198242188,0,0,0.36749267578125,0.3910903930664062,0,0.396270751953125,0.1182632446289062,0,0,-2.783119201660156,0.2290267944335938,0,0.2488784790039062,0,0.2571945190429688,0,0.3135299682617188,0.3480148315429688,0,0.358673095703125,0.3783950805664062,0.3965301513671875,0,0.332855224609375,0,0,0,-2.641448974609375,0,0.2340850830078125,0,0.2613067626953125,0,0,0.2940292358398438,0.333648681640625,0,0.3528594970703125,0,0.3650588989257812,0.388458251953125,0,0.392059326171875,0.09854888916015625,0,-2.686981201171875,0,0,0.2292022705078125,0.2782669067382812,0,0,0.2886276245117188,0,0.3256988525390625,0,0.3509368896484375,0.3465652465820312,0,0.3707351684570312,0.391387939453125,0,0.182891845703125,0,0,0,-2.492362976074219,0,0.2354888916015625,0,0.2612380981445312,0.3013763427734375,0,0.3373489379882812,0.3552322387695312,0,0.3704833984375,0,0.3929977416992188,0.3143539428710938,0,0,0,-2.503524780273438,0.234100341796875,0,0.2625350952148438,0,0.2973480224609375,0.3383636474609375,0,0.3555831909179688,0.3690338134765625,0.3922882080078125,0,0.3292083740234375,0,0,0,0,0,-2.450180053710938,0.1999664306640625,0.2596588134765625,0,0,0.2965545654296875,0,0.3302993774414062,0.3543853759765625,0,0.365753173828125,0,0.3892135620117188,0.32794189453125,0,0,0,0,0,-2.450355529785156,0,0.2247390747070312,0,0.2597274780273438,0,0,0.2947769165039062,0,0.334442138671875,0,0.3559341430664062,0.3721694946289062,0,0.3904495239257812,0,0.2906494140625,0,0,0,-2.387687683105469,0,0.2325057983398438,0,0.2608489990234375,0.2945327758789062,0,0.3309478759765625,0,0.3494415283203125,0.3623046875,0,0.3851699829101562,0,0.2432174682617188,0,0,0,0,0,-2.296279907226562,0.2354202270507812,0,0.26556396484375,0,0.3033599853515625,0,0,0.3339157104492188,0,0.334808349609375,0,0.3593597412109375,0,0.3768234252929688,0.1572113037109375,0,0,0,0,0,-2.243431091308594,0.2353286743164062,0,0.2667694091796875,0,0.30487060546875,0.3371353149414062,0,0.3534469604492188,0,0,0.3690109252929688,0,0.3779525756835938,0,0.06793212890625,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2.376060485839844,0,0,0.0919952392578125,0.2070465087890625,0,0.230194091796875,0,0.2502212524414062,0,0.2875900268554688,0,0.3218231201171875,0,0.3328933715820312,0,0.3558502197265625,0.3660659790039062,0,0,0,0,0,-2.269920349121094,0,0.22845458984375,0,0.2526702880859375,0,0.2901992797851562,0.32733154296875,0,0.3512954711914062,0,0.365631103515625,0,0.3871231079101562,0,0.1340560913085938,0,0,0,0,0,-2.087379455566406,0,0.2419586181640625,0,0.3045883178710938,0,0.322418212890625,0.3477935791015625,0.3633880615234375,0,0.37957763671875,0,0.1933746337890625,0,0,0,-2.090904235839844,0,0.2384719848632812,0.2703018188476562,0.309295654296875,0,0.3420181274414062,0,0.356903076171875,0,0.3737640380859375,0,0.2648544311523438,0,0,0,0,0,-2.129791259765625,0,0.2185134887695312,0,0.2548141479492188,0.2979583740234375,0.3340377807617188,0,0.3560409545898438,0.368499755859375,0,0.3636016845703125,0,0,0,0,0,-2.145484924316406,0.2271194458007812,0.2796630859375,0.29730224609375,0.3354568481445312,0.357574462890625,0,0,0.372528076171875,0,0.3384780883789062,0,0,0,-2.09539794921875,0,0.2265396118164062,0.2534561157226562,0.2912521362304688,0,0.3279495239257812,0,0.3549880981445312,0,0.3667449951171875,0,0.3360443115234375,0,0,0,0,0,-2.062477111816406,0,0.2277603149414062,0,0.2525253295898438,0,0,0.2902374267578125,0,0,0.3270645141601562,0,0.3521804809570312,0,0.3651657104492188,0.308197021484375,0,0,0,0,0,-2.010726928710938,0,0,0.2307281494140625,0,0.2557373046875,0.3246307373046875,0,0.33563232421875,0,0.3566207885742188,0,0.3711395263671875,0.1959304809570312,0,0,0,-1.904891967773438,0,0.2361602783203125,0.2653884887695312,0,0.3061904907226562,0,0.340911865234375,0,0.3553237915039062,0,0.3733673095703125,0.08620452880859375,0,0,0,-1.851219177246094,0,0.23748779296875,0,0.2720947265625,0.3098907470703125,0.3250045776367188,0,0,0.3522262573242188,0.3675537109375,0,0.04470062255859375,0,0,0,-1.775863647460938,0.2627944946289062,0.274993896484375,0,0,0.3112869262695312,0,0.3391952514648438,0,0.3570938110351562,0,0.2873077392578125,0,0,0,-1.882499694824219,0.2262344360351562,0.2492446899414062,0.2882843017578125,0,0.3216323852539062,0,0.3492355346679688,0,0.36090087890625,0,0.1428985595703125,0,0,0,-1.761329650878906,0.233978271484375,0.2641983032226562,0,0.3039398193359375,0,0.3370895385742188,0,0.3588333129882812,0,0.3183135986328125,0,0,0,0,0,-1.840240478515625,0,0.2263641357421875,0.2745742797851562,0.2901229858398438,0,0.3277969360351562,0,0.3567428588867188,0,0,0.3677902221679688,0,0.0508880615234375,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.723564147949219,0,0.215087890625,0.2386627197265625,0,0.2683563232421875,0.3021392822265625,0,0,0.3368911743164062,0,0.3538055419921875,0,0.06160736083984375,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1.831680297851562,0,0,0,0.1657638549804688,0,0.2525253295898438,0,0,0.27581787109375,0,0.3142776489257812,0,0.3348236083984375,0,0.3153305053710938,0,0.3378219604492188,0,0.3833847045898438,0,0.4013671875,0.4061737060546875,0,0.4051971435546875,0,0.3722152709960938,0.325103759765625,0,0.3238677978515625,0.3280181884765625,0,0.324462890625,0,0.324615478515625,0.3235321044921875,0.3076553344726562,0.3292465209960938,0,0.3232421875,0.32440185546875,0,0.3253326416015625,0,0.088470458984375,0,0,0,0,0,-7.143165588378906,0,0.2606048583984375,0,0.2925491333007812,0,0.32464599609375,0,0.32965087890625,0,0.3206558227539062,0,0.3571014404296875,0.3823089599609375,0,0.3955459594726562,0,0,0.4076080322265625,0,0.4073944091796875,0.4055862426757812,0,0.4060516357421875,0,0.4080352783203125,0.4075927734375,0,0.4048690795898438,0.408447265625,0,0.4083175659179688,0,0.3758697509765625,0,0.3899307250976562,0,0.2586441040039062,0,0,0,0,0,0,0,0,-6.9473876953125,0,0.2609329223632812,0,0.2955703735351562,0,0.3179855346679688,0.3119049072265625,0,0.34674072265625,0,0.362884521484375,0,0.3886795043945312,0.4030838012695312,0,0.4546585083007812,0,0.4127044677734375,0.4120407104492188,0,0,0.4111328125,0,0.412933349609375,0,0.4123153686523438,0,0.4097824096679688,0,0.4082870483398438,0,0.4131088256835938,0,0.3953094482421875,0.322174072265625,0,0,0,0,0,-6.862083435058594,0,0.1653594970703125,0,0.165283203125,0,0.3064651489257812,0.3162918090820312,0,0,0.3260116577148438,0,0.3554534912109375,0.371368408203125,0,0.3700637817382812,0.3957138061523438,0,0.40362548828125,0,0.4032363891601562,0,0.4051589965820312,0,0,0.4071502685546875,0.4104385375976562,0.407928466796875,0,0.4072647094726562,0.412017822265625,0,0.4118423461914062,0.3937911987304688,0,0.2291641235351562,0,0,0,0,0,0,0,0,-6.784828186035156,0,0.2515182495117188,0.276824951171875,0.2911148071289062,0,0.3013381958007812,0,0.3430404663085938,0,0,0.3539047241210938,0,0.3715133666992188,0,0.388336181640625,0,0.3969039916992188,0,0.40673828125,0.402435302734375,0.4042282104492188,0.4039459228515625,0,0.4039840698242188,0,0.4049606323242188,0,0.4050216674804688,0,0.4032363891601562,0,0.3989105224609375,0.3751678466796875,0,0,0,0,0,-6.696327209472656,0.2488250732421875,0.26422119140625,0,0.2788467407226562,0,0.298309326171875,0,0,0.3382949829101562,0,0.3462677001953125,0.4063568115234375,0,0.3898849487304688,0,0.3976974487304688,0.4062271118164062,0.4038772583007812,0.404296875,0.4037857055664062,0,0.40533447265625,0,0.4059371948242188,0,0.4043121337890625,0.4080963134765625,0,0.3939971923828125,0.286865234375,0,0,0,0,0,0,0,0,-6.537239074707031,0,0.2323379516601562,0,0.2588272094726562,0.27020263671875,0,0.3139801025390625,0.3416213989257812,0,0.3492050170898438,0.366851806640625,0,0.3848190307617188,0.3957672119140625,0.4042282104492188,0.4011383056640625,0.4020309448242188,0,0.4049835205078125,0,0.4071502685546875,0,0.4086380004882812,0,0.407318115234375,0,0.40899658203125,0.3885040283203125,0,0.18255615234375,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-6.470573425292969,0.22576904296875,0,0.239349365234375,0,0.2423553466796875,0,0.2829360961914062,0.3221359252929688,0,0.3397369384765625,0.3504180908203125,0,0.3680953979492188,0,0.3846359252929688,0.39483642578125,0,0.4023513793945312,0.4020156860351562,0,0.4057235717773438,0,0,0.40399169921875,0.4069290161132812,0.4065780639648438,0.408477783203125,0,0.3870620727539062,0,0.285919189453125,0,0,0,0,0,-6.341651916503906,0.2691192626953125,0,0.2505645751953125,0.2248001098632812,0,0.2862014770507812,0,0.3349380493164062,0.3283843994140625,0,0.315887451171875,0.3707504272460938,0,0.381622314453125,0,0.3928451538085938,0.3878707885742188,0,0.39251708984375,0,0.4025421142578125,0,0.4043655395507812,0.4058074951171875,0,0.4069900512695312,0,0.4086227416992188,0.3871383666992188,0,0.176513671875,0,0,0,0,0,0,0,0,-6.181350708007812,0.2430801391601562,0,0.2486724853515625,0.2912216186523438,0,0.3300704956054688,0,0.3424148559570312,0,0.3488311767578125,0,0.3642425537109375,0,0.3837661743164062,0.393310546875,0.4028396606445312,0,0.4041748046875,0.4472732543945312,0,0.4065399169921875,0,0.4086685180664062,0,0.4104385375976562,0.4099273681640625,0,0.3900833129882812,0,0.1386260986328125,0,0,0,0,0,-6.286796569824219,0,0.23291015625,0.2398757934570312,0.2491073608398438,0,0.2967300415039062,0.3285140991210938,0,0.3455123901367188,0,0.3548355102539062,0,0.3670501708984375,0,0.3818359375,0,0.392608642578125,0.3991622924804688,0,7.805107116699219,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7.62939453125,7.62939453125e-06,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,15.2587890625,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7.688255310058594,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,15.33635711669922,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"filename":["<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,null,null,null,null,null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,null,null,null,null,null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>","<expr>",null,null,null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,null,null,null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,null,null,null,null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,null,null,null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,null,null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,null,null,null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,"<expr>",null,null,null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>",null,null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,null,null,null,null,null,null,null,null,null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>","<expr>","<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,null,"<expr>","<expr>",null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,null,"<expr>",null,null,"<expr>",null,"<expr>","<expr>","<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,null,null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>","<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,"<expr>",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,"<expr>","<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null,"<expr>",null,null,null,null,null,null,null]},"interval":10,"files":[{"filename":"<expr>","content":"## Generate Large Random Dataset\nn <- 2e6\nx <- runif(n)\ny <- runif(n)\nz <- runif(n)\nXYZ <- cbind(x,y,z)\n\n## Inspect 4 equivalent `row mean` calculations \nprofvis::profvis({\n    m <- rowSums(XYZ)/ncol(XYZ)\n    m <- rowMeans(XYZ)\n    m <- apply(XYZ, 1, mean)\n    m <- rep(NA, n);  for(i in 1:n){ m[i] <- (x[i] + y[i] + z[i]) / 3 }\n})\n## rowSums(), colSums(), rowMeans(), and colMeans() are vectorised and fast.\n## for loop is not the slowest, but the ugliest.","normpath":"<expr>"}],"prof_output":"/tmp/RtmpNetrKD/file20be1d1ad464.prof","highlight":{"output":["^output\\$"],"gc":["^<GC>$"],"stacktrace":["^\\.\\.stacktraceo(n|ff)\\.\\.$"]},"split":"h"}},"evals":[],"jsHooks":[]}</script>
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
##  mean1(x, 0.5) 19.58411 19.98042 20.16557 19.98826 19.99641 28.29909   100  a 
##  mean2(x, 0.5) 18.73101 19.13773 19.36589 19.14487 19.15865 22.03928   100   b
##  mean3(x, 0.5) 19.66264 20.02891 20.14341 20.03749 20.04691 23.01193   100  a
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
##    expr       min       lq      mean    median        uq      max neval cld
##  ma1(y) 169.47296 187.4299 192.00660 189.03709 191.55286 341.1323   100  a 
##  ma2(y)  18.65311  20.1438  24.30535  22.99911  25.92437  41.8285   100   b
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
##   0.104   0.000   0.033
```

```r
system.time({ lm(Y~X, data=DAT) })
```

```
##    user  system elapsed 
##   0.403   0.015   0.158
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
##   0.027   0.001   0.029
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
##   0.908   0.186   0.622
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

