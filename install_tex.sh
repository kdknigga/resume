#!/bin/bash

sudo dnf -y install texlive texlive-changepage texlive-lastpage texlive-xetex latex2html

mkdir -p ~/texmf/dist ~/texmf/tex/latex

pushd ~/texmf/dist
# packages
for pkg in tabto moresize
do
    wget "http://mirrors.ctan.org/macros/latex/contrib/$pkg.zip"
    unzip -o "$pkg.zip" -d "../tex/latex/$pkg"
    rm "$pkg.zip"
    pushd "../tex/latex/$pkg"
    find . -type f -name "*.ins" | while read insfile
    do
        tex "$insfile"
    done
    popd
done

wget "https://mirrors.ctan.org/graphics/pstricks/contrib/pst-graphicx.zip"
unzip -o "pst-graphicx.zip" -d "../tex/latex/pst-graphicx"
rm "pst-graphicx.zip"

wget "http://mirrors.ctan.org/fonts/raleway.zip"
unzip -o "raleway.zip" -d "../tex/latex/raleway"
rm "$font.zip"

wget "https://mirrors.ctan.org/fonts/psfonts/ly1.zip"
unzip -o "ly1.zip" -d "../tex/latex/ly1"
rm "ly1.zip"

popd
