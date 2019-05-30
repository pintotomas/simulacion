#/usr/bin/env/ python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import random

#Generador de números aleatorios que provee PYTHON
def aleatorio():
	return random.uniform(-1,1)

listaDeValores1=[]
listaDeValores2=[]

#Genero 1000 valores(por ejemplo)
for i in range(0,10000):
	x = aleatorio()
	y = aleatorio()
	if ( x**2 + y**2) < 1:
		listaDeValores1.append(x)
		listaDeValores2.append(y)

#Gráfico
plt.title('Grafico utilizando una distribucion uniforme')
plt.plot(listaDeValores1,listaDeValores2,'o',markersize=1)
plt.xlabel('Valores de X')
plt.ylabel('Valores de Y')
plt.show()



