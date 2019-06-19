#!/usr/bin/env/ python
# -*- coding: utf-8 -*-
from scipy import stats as sp
from numpy import random

#Tomamos los resultados del ejercicio 5
valoresObservados=[39440.,30081.,12106.,10317.,8093.]
#Tomamos los valores esperados por a distribución
valoresEsperados=[40000.0, 30000.0, 12000.0, 10000.0, 8000.0]

estadistica, pvalue = sp.chisquare(valoresObservados,valoresEsperados)
print(estadistica)
print(pvalue)
if (pvalue < 0.01):
	print(' Se acepta la hipotesis con la distribucion empirica con un error menor del 1% ')
else:
	print('Se rechaza la hipotesis con la distribucion empirica con un error mayor del 1% ')

