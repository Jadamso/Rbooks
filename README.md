# Rbooks

* The book is found at <https://jadamso.github.io/Rbooks/>
* The source materials are found at <https://github.com/Jadamso/Rbooks>
* Things to fix/add are found at <https://github.com/Jadamso/Rbooks/blob/main/ToDo.md>

To preview locally,

    quarto preview book

To publish online,

    git add <files> && git commit -m "message"
    git push
    quarto publish gh-pages book --no-browser

To sync files,

    cd book && for d in _freeze/*/; do stem=$(basename "$d"); [ ! -f "${stem}.qmd" ] && rm -rf "$d"; done
    cp -r ./Templates/Figures_Manual/* ./book/_book/Figures_Manual
    
To publish a tagged release, 

    gh release create v0.0.2 --title "v0.0.2, for ECON 2320"


<!-- ## CONVERT IMAGES
    for pdfile in *.pdf ; do 
    convert -verbose -density 500  "${pdfile}" "${pdfile%.*}".png;
    done
-->
