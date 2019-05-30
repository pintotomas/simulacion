#/usr/bin/env/ python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

modulo = 2**32
multiplicador = 1013904223
incremento = 1664525
semilla = int(92702 * 0.15 + 93584 * 0.25 + 98757 * 0.6)
secuencia = [ semilla ]

def GCL( valor ): 
	return ( multiplicador * valor + incremento ) % modulo 

def cargarSecuencia(secuencia,inicio, fin):
	for i in range(inicio,fin):
		secuencia.append( GCL( secuencia[ i-1 ] ) )

cargarSecuencia(secuencia,1, 5)
print("Primeros 5 numeros de la secuencia: {}".format(secuencia))

#Para que de números entre 0 y 1, divido por su módulo
#Hipótesis: utilizo como semilla el valor: 0.9
secuenciaRango01 = [0.9]

#Cargo la lista de secuencias
cargarSecuencia(secuenciaRango01,1, 100000)

#divido los valores de la lista de secuencias por su modulo
for i in range(0,100000):
	secuenciaRango01[i]= secuenciaRango01[i]/modulo

#histograma
plt.title('Histograma')
plt.xlabel('SecuenciaDeValores')
plt.ylabel('Frecuencia')
plt.hist(secuenciaRango01, bins =60, alpha=0.5, ec='black')
plt.grid(True)
plt.show()
plt.clf()



