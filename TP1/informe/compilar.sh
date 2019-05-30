#!/bin/bash

pdflatex informeSimulacionTP1.tex && pdflatex informeSimulacionTP1.tex

rm *.aux
rm *.log
rm *.toc
rm *.out