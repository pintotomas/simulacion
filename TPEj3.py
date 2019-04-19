#/usr/bin/env/ python
# -*- coding: utf-8 -*-

from numpy import random, sqrt, log, sin, cos, pi
import matplotlib.pyplot as plt

#Distribución normal
u1 = random.normal(0,1, 100000)
u2 = random.normal(0,1, 100000)

#Box muller
z1 = sqrt(-2*log(u1))*cos(2*pi*u2)
z2 = sqrt(-2*log(u1))*sin(2*pi*u2)

#Histograma
plt.hist(z1, bins =60, alpha=0.5, ec='black')
plt.hist(z2, bins =60, alpha=0.5, ec='green')
plt.grid(True)
plt.show()
