#/usr/bin/env/ python
# -*- coding: utf-8 -*-
import scipy.stats as stats
from numpy import random
from TPEj5 import correrEjercicio

#Tomamos los resultados del ejercicio 5
valoresObservados = correrEjercicio()
nMUestras = 100000

esperados = []
cant_valores = 100000
dispersionCuadrado = 0
uniforme = random.uniform(0,1,100000)

#Generamos la muestra esperada n*p_i
for i in range(cant_valores):
    esperado = nMUestras * float(uniforme[i])
    esperados.append(float(esperado))

#Medimos la dispersion de las ocurrencias obervadas(N_i) respectos de las esperadas n*p_i
for i in range(1,cant_valores):
    dispersionCuadrado += ((valoresObservados [i] - esperados[i]) ** 2) / esperados[i]

#Calculamos los grados de libertad de la distribucion Chi-2 

if (dispersionCuadrado < t):
	print(' Se acepta la hipotesis con la distribucion empirica con un error del 1% ')
else:
	print('Se rechaza la hipotesis con la distribucion empirica con un error del 1% ')

