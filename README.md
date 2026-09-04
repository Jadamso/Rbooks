# Rbooks

* The book is found at <https://jadamso.github.io/Rbooks/>
* The source materials are found at <https://github.com/Jadamso/Rbooks>
* Errors and issues can be reported at <https://github.com/Jadamso/Rbooks/issues>

To preview locally,

    quarto preview book
    quarto render book
    
To publish online,

    git add <files> && git commit -m "message"
    git push
    quarto publish gh-pages book --no-browser

To clear freeze entries for chapters that no longer exist,

    for d in book/_freeze/*/; do stem=$(basename "$d"); [ "$stem" = site_libs ] && continue; [ -f "book/${stem}.qmd" ] || rm -rf "$d"; done

To publish a tagged release, 

    gh release create v0.0.2 --title "v0.0.2, for ECON 2320"


<!-- ## CONVERT IMAGES
    for pdfile in *.pdf ; do 
    convert -verbose -density 500  "${pdfile}" "${pdfile%.*}".png;
    done
-->
