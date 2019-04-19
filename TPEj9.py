
#Generador Ej1

import math

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

n = 100000
average_gap = math.ceil(sum(gaps)/len(gaps)) #Lo redondeo hacia arriba
min_gap = min(gaps)
max_gap = max(gaps)
prob_intervalo = round(b-a, 3)
prob_fuera_intervalo = 1 - prob_intervalo
prob_average_gap_teorica = (prob_fuera_intervalo**average_gap)*prob_intervalo

print('En promedio, cada '+str(average_gap)+' numeros generado por este GCL cae en el intervalo '+str(a)+','+str(b))
print('El gap maximo fue: '+str(max_gap)+', y el minimo: '+str(min_gap))
print('La probabilidad de que el numero caiga en el intervalo es '+str(prob_intervalo))
print('Teoricamente la probabilidad de que caiga '+str(average_gap)+' veces fuera del intervalo y vuelva a caer en el intervalo es: ' +str(round(prob_average_gap_teorica, 1)))
print('La probabilidad es relativamente baja, concluyo que si bien segun el histograma del ejercicio 1 los numeros estan')
print('bastante bien distribuidos, no se estan generando de manera muy aleatoria si no que secuencialmente (tiene sentido porque es GCL)')