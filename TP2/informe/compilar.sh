#!/bin/bash

pdflatex informeSimulacionTP2.tex && pdflatex informeSimulacionTP2.tex

rm *.aux
rm *.log
rm *.toc
rm *.out
