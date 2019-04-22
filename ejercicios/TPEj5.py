#/usr/bin/env/ python
# -*- coding: utf-8 -*-
import math 
import numpy as np
import matplotlib.pyplot as plt

## datos y GCL del ejercicio 1
modulo = 2**32
multiplicador = 1013904223
incremento = 1664525
semilla = int(92702 * 0.15 + 93584 * 0.25 + 98757 * 0.26)
secuencia = [ semilla ]

def GCL( valor ): 
	return ( multiplicador * valor + incremento ) % modulo 

## genero 100000 valores
for i in range(1,100000):
	secuencia.append( GCL( secuencia[ i-1 ] ) )

## divido por su modulo para tener valores (0,1)
for i in range(1,100000):
	secuencia[i] = secuencia[i]/modulo

valoresFuncion = []
#La función inversa de la Función de distribución Empírica es: 
for nro in secuencia:
    if (nro >= 0 and nro < 0.4):
        valoresFuncion.append(1)
    elif (nro >= 0.4 and nro < 0.7):
        valoresFuncion.append(2)
    elif (nro >= 0.7 and nro < 0.82):
        valoresFuncion.append(3)
    elif (nro >= 0.82 and nro < 0.92):
        valoresFuncion.append(4)	
    else:
        valoresFuncion.append(5)

#histograma
plt.title('Histograma')
plt.xlabel('Valores de la funcion')
plt.ylabel('Frecuencia')
plt.hist(valoresFuncion, bins = 10, alpha=0.5, ec='black')
plt.grid(True)
plt.show()

