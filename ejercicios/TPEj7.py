#/usr/bin/env/ python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

modulo = 2**32
multiplicador = 1013904223
incremento = 1664525
semilla = int(92702 * 0.15 + 93584 * 0.25 + 98757 * 0.26)
secuencia = [ semilla ]

def GCL( valor ): 
	return ( multiplicador * valor + incremento ) % modulo 

def cargarSecuencia(secuencia,inicio, fin):
	for i in range(inicio,fin):
		secuencia.append( GCL( secuencia[ i-1 ] ) )


#Cargo la lista de secuencias
cargarSecuencia(secuencia,1, 100000)

#Gráfico en dos dimensiones
plt.specgram(secuencia, NFFT=256, Fs=2, Fc=0,noverlap=128)

#Gráfico en tres dimensiones

plt.show()
