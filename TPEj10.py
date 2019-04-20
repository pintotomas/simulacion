#Distribucion generada en el ejercicio 3 

#/usr/bin/env/ python
# -*- coding: utf-8 -*-

from numpy import random, sqrt, log, sin, cos, pi
import matplotlib.pyplot as plt

#Distribución uniforme
u1 = random.uniform(0,1, 100000)
u2 = random.uniform(0,1, 100000)

#Box muller transformation
z1 = sqrt(-2*log(u1))*cos(2*pi*u2)
z2 = sqrt(-2*log(u1))*sin(2*pi*u2)

#Ejercicio 10:

#Aplico el test a las dos distribuciones generadas

import scipy.stats

test1 = scipy.stats.kstest(z1, 'norm')
test2 = scipy.stats.kstest(z2, 'norm')

#Hipotesis nula (de igualdad): Si no la rechazamos podemos decir que es igual a una normal
#Hipotesis alternativa (de diferencias): Si rechazamos la hipotesis nula decimos que hay diferencias con la distribucion normal
#Con un nivel de significancia del 0,05%

if test1.pvalue >= 0.05: 
	print('La variable z1 pasa el test de kolmogorov-smirnov para un nivel de significancia del 0.05%, por lo tanto no podemos rechazar la hipotesis nula y la distribucion de esta variable es igual a la distribucion normal')
else:
	print('La variable z1 no pasa el test de kolmogorov-smirnov y afirmamos que tiene diferencias con la distribucion normal')
if test2.pvalue >= 0.05: 
	print('La variable z2 pasa el test de kolmogorov-smirnov para un nivel de significancia del 0.05%, por lo tanto no podemos rechazar la hipotesis nula y la distribucion de esta variable es igual a la distribucion normal')
else:
	print('La variable z2 no pasa el test de kolmogorov-smirnov y afirmamos que tiene diferencias con la distribucion normal')