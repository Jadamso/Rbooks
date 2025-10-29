# Rbooks

* The book is found at <https://jadamso.github.io/Rbooks/>
* The source materials are found at <https://github.com/Jadamso/Rbooks>
* Things to fix/add are found at <https://github.com/Jadamso/Rbooks/blob/main/ToDo.md>

To compile this book, navigate to the root directory, then 

    quarto preview book

To publish online, 

    quarto render book
    cp -r ./Templates/Figures_Manual ./docs/Figures_Manual
    git add .
    git commit -m " "
    git push
    
To publish a tagged release, 

    gh release create v0.0.2 --title "v0.0.2, for ECON 2320"

