#Distribucion generada en el ejercicio 3 

#/usr/bin/env/ python
# -*- coding: utf-8 -*-
import numpy as np
from numpy import random, sqrt, log, sin, cos, pi
import matplotlib.pyplot as plt
import scipy.stats
import statsmodels.api as sm # recommended import according to the docs

#Distribución uniforme
u1 = random.uniform(0,1, 100000)
u2 = random.uniform(0,1, 100000)

#Box muller transformation
z1 = sqrt(-2*log(u1))*cos(2*pi*u2)
z2 = sqrt(-2*log(u1))*sin(2*pi*u2)

#Ejercicio 10:

#Aplico el test a las dos distribuciones generadas


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


#Grafico de la empirica de z1
sample = z1
ecdf = sm.distributions.ECDF(sample)
x = np.linspace(min(sample), max(sample))
y = ecdf(x)
plt.step(x, y, label = 'empirical cdf (z1)')

#Grafico de la empirica de z2
sample = z2
ecdf = sm.distributions.ECDF(sample)
x = np.linspace(min(sample), max(sample))
y = ecdf(x)
plt.step(x, y, label = 'empirical cdf (z2)')

#Grafico la acumulada de la normal
x = np.linspace(-5, 5, 5000)
mu = 0
sigma = 1
y_cdf = scipy.stats.norm.cdf(x, mu, sigma) # the normal cdf
plt.plot(x, y_cdf, label='normal cdf')


plt.legend()
plt.show()