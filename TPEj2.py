#/usr/bin/env/ python
import math 
import numpy as np
import matplotlib.pyplot as plt

## datos del ejercicio anterior
modulo = 2**32
multiplicador = 1013904223
incremento = 1664525
semilla = 0.9 # hipotesis

secuencia = [semilla]
## Generador del ejercicio anterior, para este en un rango[0,1] se debe dividir por modulo
def GCL( valor ): 
	return ( multiplicador * valor + incremento ) % modulo 

for i in range(1,100000):
	secuencia.append( GCL( secuencia[ i-1 ] ) )

#divido los valores de la lista de secuencias por su modulo
for i in range(0,100000):
	secuencia[i]= secuencia[i]/modulo

# transformada inversa
def transformadaInversa(u):
	return -(1/20) * math.log(1-u)

for i in range(0,100000):
	secuencia[i]= transformadaInversa(secuencia[i])


#histograma
plt.title('Histograma')
plt.xlabel('SecuenciaDeValores')
plt.ylabel('Frecuencia')
plt.hist(secuencia, bins =60, alpha=0.5, ec='black')
plt.grid(True)
#plt.show()
plt.clf()

##calculo de media
media = sum(secuencia)/len(secuencia)

print(media)
print(1/20)

#calculo de varianza
diferenciaDeCuadrados = [(x-media)**2 for x in secuencia]
varianza = sum(diferenciaDeCuadrados)/len(secuencia)

print(varianza)
print(1/(20)**2)




