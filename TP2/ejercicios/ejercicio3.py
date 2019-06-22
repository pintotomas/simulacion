#!/usr/bin/env/ python

import matplotlib.pyplot as plt
from matplotlib.pyplot import plot
import matplotlib.colors
from mpl_toolkits.mplot3d import Axes3D

Pt = [8]

def calculo(valor_pt):
	return ((0.909*valor_pt) - 1)

def fully_price(Pt):
	for i in range(1,100):
		Pt.append(calculo(Pt[i-1]))
	return Pt

prices = fully_price(Pt)
#Graficamos el precio en funcion del tiempo
t = range(0,100)
plt.xlabel('Periodo(t)')
plt.ylabel('Precio')
plt.plot(t, [ prices[i] for i in t ])
#plt.show()

#Hacemos el diagrama de fases del sistema
x= t
y= [9 - (1.1*prices[i]) for i in range(0,100) ]
z= prices

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(x,y,z,marker='o')
plt.title("Espacio de fases del sistema")
ax.set_xlabel('Periodo(t)')
ax.set_ylabel('Precio')
ax.set_zlabel('Cantidad')
plt.show()
