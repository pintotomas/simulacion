#/usr/bin/env/ python
import math 
import numpy as np
import matplotlib.pyplot as plt
import random

# generador de números aleatorios que provee PYTHON
def aleatorio():
	return random.uniform(-1,1)

listaDeValores1=[]
listaDeValores2=[]

# genero 1000 valores por ejemplo
for i in range(0,10000):
	x = aleatorio()
	y = aleatorio()
	if ( x**2 + y**2) < 1:
		listaDeValores1.append(x)
		listaDeValores2.append(y)

#grafico
plt.plot(listaDeValores1,listaDeValores2,'o',markersize=1)
plt.show()



