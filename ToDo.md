# To Do

Add title page

## R OLS
Add /DataScientism/* templates
- edit
- post in ./docs 
- link. eg [RandRstudio](https://jadamso.github.io/Rbooks/01-RandRstudio.md)

## Intro R
The & and | operators
    always evaluate left and right
    vectorised
The && and || operators
    they evaluate the right side only if needed (i.e. conditionally)
    they accept only scalars on both sides!
x <- 1:3
if(length(x) >= 5 & x[5] > 12) print("ok")
if(length(x) >= 5& & x[5] > 12) print("ok")
https://meek-parfait-60672c.netlify.app/docs/m1_r-intro_01#103

Data clean/merge
 * by, with, subset, split, aggregate, stack, switch, do.call, reduce

Strings. https://meek-parfait-60672c.netlify.app/docs/M1_R-intro_03_text.html, https://raw.githubusercontent.com/rstudio/cheatsheets/main/regex.pdf
kingText = "The king infringes the law on playing curling."
gsub(pattern = "ing", replacement = "", x = kingText)
gsub("[aeiouy]", "_", kingText)
gsub("([[:alpha:]]{3,})ing\\b", "\\1", kingText) 

For and while loops
## Intermediate R

Add Fortran Code, https://masuday.github.io/fortran_tutorial/r.html

showDot = function(...){
  dots = list(...)
  print(dots)
}
showDot(arg1 = 1:5, "test stuff", 
        b = "another", list(test_still = 2))
        
## RReproducible

Add 
 - Screenshot of Rmarkdown
 - How to execute
 
Add Tikz Pictures
https://community.rstudio.com/t/tikz-in-r-markdown-with-html-output/54260/2

```{r}
#install.packages("magick")
#install.packages("pdftools")
```

```{tikz, fig.cap = "Funky tikz", fig.ext = 'png'}
\usetikzlibrary{positioning}
\usetikzlibrary{arrows}
\usetikzlibrary{shapes}

\begin{tikzpicture}[box/.style={draw,rounded corners,text width=2.5cm,align=center}]
\node[box] (a) {Data Folder};
\node[left=of a.170,font=\bfseries] (aux1) {Data Source 1};
\node[left=of a.190,font=\bfseries] (aux2) {Data Source 2};
\node[below=0cm of aux2]{ $\vdots$};
\node[ellipse, below=of a, fill=lightgray, x radius=3.75cm, align=center,  y radius=2cm] (b) { Data Work \\ \{Clean, Analyze, ...\}} ;
\node[box, below=of b, text width=4cm] (c) {Output Folder \\ \{Figures, Tables, ...\} };
\node[right=of c,font=\bfseries] (d) {Final Document};
\draw[->] (aux1) -- (a.170);
\draw[->] (aux2) -- (a.190);
\draw[->] (a) -- (b);
\draw[->] (b) -- (c);
\draw[->] (c) -- (d);
\end{tikzpicture}
```

