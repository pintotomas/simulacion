
#Generador Ej1

import math
import numpy 

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

#Gap test
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

#el maximo gap es 23, separo en bins de 3
bins = [(0,3) , (4,7), (8,11), (12,15), (16,19), (20,23)]
bins_ocurrencias = {(0,3) : 0, (4,7): 0, (8,11): 0, (12,15): 0, (16,19): 0, (20,23): 0}
# por cada gap en frecuencias_gap, le sumo su resultado al bin correspondiente
for gap in frecuencias_gaps:
  for interval in bins:
    start = interval[0]
    finish = interval[1]
    if start <= gap <= finish:
      bins_ocurrencias[interval] += frecuencias_gaps[gap]

#Testeo que este for ande
assert bins_ocurrencias[(0,3)] == frecuencias_gaps[0] + frecuencias_gaps[1] + frecuencias_gaps[2] + frecuencias_gaps[3]
assert bins_ocurrencias[(4,7)] == frecuencias_gaps[4] + frecuencias_gaps[5] + frecuencias_gaps[6] + frecuencias_gaps[7]

#Ahora calculo las frecuencias relativas de cada bin de gaps

total = sum(bins_ocurrencias.values())
#calculo las frecuencias relativas
bins_frecuencias_relativas = {k: v/total for k, v in bins_ocurrencias.items()}

#calculo las frecuencias relativas acumuladas
bins_frecuencias_relativas_acumuladas = {}
bins_frecuencias_relativas_acumuladas[(0,3)] = bins_frecuencias_relativas[(0,3)]
bins_frecuencias_relativas_acumuladas[(4,7)] = bins_frecuencias_relativas[(4,7)] + bins_frecuencias_relativas_acumuladas[(0,3)]
bins_frecuencias_relativas_acumuladas[(8,11)] = bins_frecuencias_relativas[(8,11)] + bins_frecuencias_relativas_acumuladas[(4,7)]
bins_frecuencias_relativas_acumuladas[(12,15)] = bins_frecuencias_relativas[(12,15)] + bins_frecuencias_relativas_acumuladas[(8,11)]
bins_frecuencias_relativas_acumuladas[(16,19)] = bins_frecuencias_relativas[(16,19)] + bins_frecuencias_relativas_acumuladas[(12,15)]
bins_frecuencias_relativas_acumuladas[(20,23)] = bins_frecuencias_relativas[(20,23)] + bins_frecuencias_relativas_acumuladas[(16,19)]

#testeo que esto este acumulando bien
assert bins_frecuencias_relativas_acumuladas[(20,23)] == 1

#Calculo FX de cada bin (1 - (0.9)**x+1) siendo x el segundo valor de la tupla (por ej para (0,3) es 1 - (0.9)**4)
FX_bins = {}
for interval in bins:
  finish = interval[1]
  FX_bins[interval] = 1 - ((0.9)**(finish + 1))

#Ahora resto los valores de bins_frecuencias_relativas_acumuladas a FX_bins
res = {}
for k in FX_bins.keys():
  res[k] = bins_frecuencias_relativas_acumuladas[k] - FX_bins[k]
#Falta seguir los ultimos pasos que hace este chabon: https://www.youtube.com/watch?v=xh-4iOv-Oyk

#Step 4
max_value = max(res.values())

#Step 5 asumo alpha 0.05

n = 100000

D = 1.36/math.sqrt(n)
if max_value > D:
  print('La muestra es rechazada por el GAP test')
else:
  print('La hipotesis no es rechazada')
