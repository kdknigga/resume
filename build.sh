#!/bin/bash -e

poetry run python -m generator resume.yaml

# Run twice so the page counter can work
xelatex resume-full.tex
xelatex resume-full.tex

# Run twice so the page counter can work
xelatex resume-condensed.tex
xelatex resume-condensed.tex

./resume2html.sh

cp resume-condensed.pdf "Kristoffer David Knigga - Resume.pdf"
cp resume-condensed.pdf kdkresume.pdf

rm resume-full.tex resume-condensed.tex
rm resume-full.log resume-condensed.log
rm resume-full.aux resume-full.out resume-condensed.aux resume-condensed.out

