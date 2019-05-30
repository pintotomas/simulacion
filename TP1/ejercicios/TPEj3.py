#/usr/bin/env/ python
# -*- coding: utf-8 -*-

from numpy import random, sqrt, log, sin, cos, pi, mean, var
import matplotlib.pyplot as plt

#Distribución normal
u1 = random.uniform(0,1, 100000)
u2 = random.uniform(0,1, 100000)

#Box muller
z1 = sqrt(-2*log(u1))*cos(2*pi*u2)
z2 = sqrt(-2*log(u1))*sin(2*pi*u2)

#Histogramas
fig, ax = plt.subplots(1,2, figsize=(20, 10))
ax[0].hist(z1, bins =60, alpha=0.5, ec='black', label = "z1")
ax[0].hist(z2, bins =60, alpha=0.5, ec='green', label = "z2")
ax[1].hist(random.normal(0, 1, 100000), bins =60, alpha=0.5, ec='red')
ax[0].title.set_text('Histograma Box Muller')
ax[1].title.set_text('Histograma Normal estandar')
plt.show()

#Calculo de media
#Valor simulado de la media
print("El valor simulado de la media z1 es {}".format(mean(z1)))
print("El valor simulado de la media z2 es {}".format(mean(z2)))
#Valor teorico de la media
print("El valor teórico de la media es {}".format(0))

#Calculo de varianza
print("El valor simulado de la varianza z1 es {}".format(var(z1)))
print("El valor simulado de la varianza z2 es {}".format(var(z2)))
print("El valor teórico de la varianza es {}".format(1))
