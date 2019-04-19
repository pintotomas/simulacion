#/usr/bin/env/ python
from numpy import random, sqrt, log, sin, cos, pi
import matplotlib.pyplot as plt
from scipy.stats import norm

#Distribución normal estandar x de T, la que queremos generar
x = random.normal(40,6, 100000)

#Distribución normal y de T. función conocida
y = random.normal(0,1, 100000)

valores= x/y
t=max(valores)
print(t)



#Histograma
#plt.hist(u1, bins =60, normed=1, alpha=0.5, ec='black')
#plt.hist(u2, bins =60, alpha=0.5, ec='green')
#plt.grid(True)
#plt.show()
