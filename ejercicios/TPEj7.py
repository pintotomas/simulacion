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

x=[]
y=[]
z=[]

k=0
valor=semilla
for i in range(15000):
	valor=GCL(valor)
	#print(valor)	
	if(k==0):
		x.append(valor)
		k=1
	else:
		if(k==1):		
			y.append(valor)
			k=2
		else:
			z.append(valor)
			k=0

#grafico 3d
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x,y,z,marker='o')
plt.title("Grafico 3d")
ax.set_xlabel('Valores de X')
ax.set_ylabel('Valores de Y')
ax.set_zlabel('Valores de Z')
plt.show()

#grafico 2d
fig=plt.figure()
plt.xlim(1,1000000000)
plt.ylim(1,1000000000)
plot(x,y)
plt.title('Grafico 2d')
plt.xlabel('Valores de X')
plt.ylabel('valores de Y')
plt.grid(True)
plt.show()

