# Rbooks

This book is a collection of primers on using R for econometrics.

* The book is found at https://jadamso.github.io/Rbooks/
* The source materials are found at https://github.com/Jadamso/Rbooks
  * *index.Rmd* is the makefile
  * *ToDo.md* hints at what's next

To compile this book, navigate to the "book" directory, then compile via

    quarto preview
    
To publish online, 

    quarto render
    git add docs
    git commit -m "Publish site to docs/"
    git push
