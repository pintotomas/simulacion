#/usr/bin/env/ python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats 

modulo = 2**32
multiplicador = 1013904223
incremento = 1664525
semilla = int(92702 * 0.15 + 93584 * 0.25 + 98757 * 0.26)
secuencia = [ semilla ]
#Nivel de significación del 1%
alpha = 0.01

def GCL( valor ): 
	return ( multiplicador * valor + incremento ) % modulo 

def cargarSecuencia(secuencia,inicio, fin):
	for i in range(inicio,fin):
		secuencia.append( GCL( secuencia[ i-1 ] ) )

#Cargo la lista de secuencias
cargarSecuencia(secuencia,1, 100000)

#Aplicamos método de Chi-cuadrado
observado = secuencia
esperado = np.array([.25, .25, .25, .25]) 
stats.chisquare(observado, esperado)



