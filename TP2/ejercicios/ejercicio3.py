#!/usr/bin/env/ python

import matplotlib.pyplot as plt
from matplotlib.pyplot import plot
import matplotlib.colors
from mpl_toolkits.mplot3d import Axes3D

Pt = [8]
Qt = [1/5]

def calculoPt(valor_pt):
	return ((-0.909*valor_pt) + (94/11))

def fully_price(Pt):
	for i in range(1,100):
		Pt.append(calculoPt(Pt[i-1]))
	return Pt

#Calculamos los valores de Qt
def calculoQt(valor_pt):
	return (9 - (1.1*valor_pt))

def cantidadQt(Pt):
	for i in range(1,100):
		Qt.append(calculoQt(Pt[i]))
	return Qt

prices = fully_price(Pt)
#Graficamos el precio en funcion del tiempo
t = range(0,100)
plt.xlabel('Periodo(t)')
plt.ylabel('Precio')
plt.plot(t, [ prices[i] for i in t ])
plt.show()

#Hacemos el diagrama de fases del sistema
cantidad = cantidadQt(prices)
plt.xlabel('Cantidad')
plt.ylabel('Precio')
plt.plot(cantidad,prices)
plt.show()
