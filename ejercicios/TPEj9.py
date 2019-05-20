
#Generador Ej1

import math
import numpy 
import scipy.stats
import matplotlib.pyplot as plt

modulo = 2**32
multiplicador = 1013904223
incremento = 1664525
semilla = int(92702 * 0.15 + 93584 * 0.25 + 98757 * 0.26)
secuencia = [ semilla ]

def GCL( valor ): 
	return ( multiplicador * valor + incremento ) % modulo 

for i in range(1,5):
	secuencia.append( GCL( secuencia[ i-1 ] ) )

secuenciaRango01 = [0.9]

for i in range(1,100000):
	secuenciaRango01.append( GCL( secuenciaRango01[i-1]) )

for i in range(0,100000):
	secuenciaRango01[i]= secuenciaRango01[i]/modulo

#Gap test ej 9
from collections import Counter 

# Intervalo (enunciado)
a = 0.2
b = 0.5

# Cuento cada cuantos numeros aparece un numero de este intervalo y lo registro en un array
# Repito hasta recorrer todos los numeros generados

gaps = []

actual_gap = 0

for i in range(0, len(secuenciaRango01)):
  numero_generado = secuenciaRango01[i]
  if a <= numero_generado <= b:
    gaps.append(actual_gap)
    actual_gap = 0
  else:
    actual_gap += 1

frecuencias_gaps = Counter(gaps)
total = 0
for gap in frecuencias_gaps:
  frec = frecuencias_gaps[gap]
  total += frec

def proba_ideal(gap):

  # Intervalo (enunciado)
  a = 0.2
  b = 0.5

  p = b - a
  gap_prob = p * (1 - p)**gap
  return gap_prob


frecuencias_ideales = []
frecuencias_obtenidas = []
gaps = []
for gap in frecuencias_gaps:
  gaps.append(gap)
  frecuencias_ideales.append(proba_ideal(gap) * total)
  frecuencias_obtenidas.append(frecuencias_gaps[gap])

#esto es para mostrar mejor el grafico
gaps_corridos = []
for gap in gaps:
  gaps_corridos.append(gap + 0.15)

plt.bar(gaps, frecuencias_ideales, label='frecuencias ideales')
plt.bar(gaps_corridos , frecuencias_obtenidas, label='frecuencias obtenidas')
plt.legend()
plt.show()
result = scipy.stats.chisquare(frecuencias_obtenidas, frecuencias_ideales)
if result.pvalue < 0.05:
  print('Pasa el gap test')
