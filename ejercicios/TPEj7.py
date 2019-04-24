#/usr/bin/env/ python
# -*- coding: utf-8 -*-

import math 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors
from matplotlib.pyplot import plot
from mpl_toolkits.mplot3d import axes3d


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

x=[]
y=[]
z=[]
k=0

for i in (0,len(secuencia)-3):
	x.append(secuencia[i+k])
	k+1
	y.append(secuencia[i+k])
	k+1
	z.append(secuencia[i+k])
	k+1

#grafico 3d
fig=plt.figure()
ax=fig.gca(projection='3d')
ax.plot(x,y,z,linewidth=0.5)
plt.show()	

#grafico 2d
fig=plt.figure()
plt.xlim(1,10000000)
plt.ylim(1,10000000)
plot(x,y,linewidth=0.5, markersize=12)
plt.show()	

