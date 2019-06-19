#!/usr/bin/env/ python

import matplotlib.pyplot as plt

Pt = [8]

def calculo(valor_pt):
	return ((0.909*valor_pt) - 1)

def fully_price(Pt):
	for i in range(1,100):
		Pt.append(calculo(Pt[i-1]))
	return Pt

prices = fully_price(Pt)
#Graficamos el precio en funcion del tiempo
x = range(0,100)
plt.xlabel('Periodo(t)')
plt.ylabel('Precio')
plt.plot(x, [prices[i]for i in x ])
plt.show()
