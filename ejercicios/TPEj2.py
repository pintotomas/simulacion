#/usr/bin/env/ python
# -*- coding: utf-8 -*-

import math 
import matplotlib.pyplot as plt

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
	return -(1/20) * math.log(1-u)

#Creamos la secuencia utilizando el generador GCL
for i in range(1,100000):
	secuencia.append( GCL( secuencia[ i-1 ] ) )

#Divido los valores de la lista de secuencias por su modulo
for i in range(0,100000):
	secuencia[i]= secuencia[i]/modulo

#Aplicamos transformada inversa a la secuencia
for i in range(0,100000):
	secuencia[i]= transformadaInversa(secuencia[i])

#Histograma
plt.title('Histograma')
plt.xlabel('SecuenciaDeValores')
plt.ylabel('Frecuencia')
plt.hist(secuencia, bins =60, alpha=0.5, ec='black')
plt.grid(True)
#plt.show()
plt.clf()

#Calculo de media
media = sum(secuencia)/len(secuencia)
#Valor simulado de la media
print("El valor simulado de la media es {}".format(media))
#Valor teorico de la media
print("El valor teórico de la media es {}".format(1/20))

#Calculo de varianza
diferenciaDeCuadrados = [(x-media)**2 for x in secuencia]
varianza = sum(diferenciaDeCuadrados)/len(secuencia)
print("El valor simulado de la varianza es {}".format(varianza))
print("El valor simulado de la varianza es {}".format(1/(20)**2))
