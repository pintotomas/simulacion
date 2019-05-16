#/usr/bin/env/ python
# -*- coding: utf-8 -*-

import math 
import matplotlib.pyplot as plt
import numpy as np

#Datos del ejercicio anterior
modulo = 2**32
multiplicador = 1013904223
incremento = 1664525
semilla = int(92702 * 0.15 + 93584 * 0.25 + 98757 * 0.26)

secuencia = [semilla]
#Generador del ejercicio anterior, para este en un rango[0,1] se debe dividir por modulo
def GCL( valor ): 
	return ( multiplicador * valor + incremento ) % modulo 

#Transformada inversa
def transformadaInversa(u):
	return -(float(20)) * math.log(1-u) ##modificado

#Creamos la secuencia utilizando el generador GCL
for i in range(1,100000):
	secuencia.append( GCL( secuencia[ i-1 ] ) )

#Divido los valores de la lista de secuencias por su modulo
for i in range(0,100000):
	secuencia[i]= float(secuencia[i])/float(modulo)

#Aplicamos transformada inversa a la secuencia
for i in range(0,100000):
	secuencia[i]= transformadaInversa(secuencia[i])

#Histograma
plt.title('Histograma Metodo de la transformada inversa')
plt.xlabel('SecuenciaDeValores')
plt.ylabel('Frecuencia')
plt.hist(secuencia, bins =60, alpha=0.5, ec='black')
plt.grid(True)
plt.show()

#Calculo de media
media = np.mean(secuencia)
#Valor simulado de la media
print("El valor simulado de la media es {}".format(media))
#Valor teorico de la media
print("El valor teórico de la media es {}".format(float(20)))

#Calculo de varianza
varianza = np.var(secuencia)
print("El valor simulado de la varianza es {}".format(varianza))
lamdaCuadrado = float(1)/float(20**2)
print("El valor teórico de la varianza es {}".format(float(1)/lamdaCuadrado))
