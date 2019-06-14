#/usr/bin/env/ python
# -*- coding: utf-8 -*-
import math 
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats as sp

## datos y GCL del ejercicio 1
modulo = 2**32
multiplicador = 1013904223
incremento = 1664525
semilla = int(92702 * 0.15 + 93584 * 0.25 + 98757 * 0.26)
secuencia = [ semilla ]

def GCL( valor ): 
	return ( multiplicador * valor + incremento ) % modulo 

def funcionInversa( valoresFuncion, secuencia ):
	for nro in secuencia:
		if (nro >= 0) and (nro < 0.4):
			valoresFuncion.append(1)
		if (nro>=0.4) and (nro < 0.7):
			valoresFuncion.append(2)
		if (nro >= 0.7 and nro < 0.82):
			valoresFuncion.append(3)
		if (nro >= 0.82 and nro < 0.92):
			valoresFuncion.append(4)
		else:			
			valoresFuncion.append(5)
	
	return valoresFuncion

def modularSecuencia(secuencia):
	for i in range(1,100000):
		secuencia[i] = secuencia[i]/modulo
	return secuencia

def generarGCL(secuencia):
	for i in range(1,100000):
		secuencia.append( GCL( secuencia[ i-1 ] ) )
	return secuencia

def crearHistograma(valores):
	plt.title('Histograma')
	plt.xlabel('Valores de la funcion')
	plt.ylabel('Frecuencia')
	plt.hist(valores, alpha=0.5, ec='black')
	plt.grid(True)
	plt.show()

def correrEjercicio():
	## genero 100000 valores utilizando GCL
	secuenciaGCL = generarGCL(secuencia)
	## divido por su modulo para tener valores (0,1)
	secuenciaModulada = modularSecuencia(secuenciaGCL)
	valoresFuncion = []
	#La función inversa de la Función de distribución Empírica es: 
	valores = funcionInversa( valoresFuncion, secuenciaModulada )
	#histograma
	#crearHistograma(valores)
	valoresEsperados=[40000,30000,12000,10000,8000]
	histo ,bin_edges = np.histogram(valores)
	observado = [i for i in histo if i!=0]
	estadistica, pvalue = sp.chisquare(observado,valoresEsperados)
	print(estadistica)
	print(pvalue)

correrEjercicio()

