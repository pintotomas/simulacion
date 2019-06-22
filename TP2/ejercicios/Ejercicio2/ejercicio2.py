import os
import numpy
import random
import matplotlib.pyplot as plt

cant=51
p = 0.7

def factorial(n):
	if (n==0):
		return 1
	else:
		return n* factorial(n-1)
		
def combinatoria(n,r):	
	return factorial(n)/(factorial(r) * factorial(n-r))


def jMayorIgualAi(i,j):
	return combinatoria(cant,j-i) * p**(j-i) * (1-p) **(cant-(j-i))

def jMenorAi(i,j):
	sumatoria =0
	for k in range(i,cant):
		 sumatoria = sumatoria + jMayorIgualAi(i,k)
	return (1-sumatoria)/i

def funcionProbabilidad(i,j):
	if (i<=j):
		probabilidad = jMayorIgualAi(i,j)
	else:
		probabilidad = jMenorAi(i,j)
	return round(probabilidad,4)

def generarMatriz():
	archivo = open("matrizDeTransicion.txt","w")	
	cadena = ''
	matriz=[]
	for m in range (0,cant):
		fila=[]
		for n in range (0,cant):
			valor=funcionProbabilidad(m,n) 				
			fila.append(valor)
			cadena = cadena + str(valor) + ','
		archivo.write(cadena + os.linesep)
		matriz.append(fila)
		cadena=''
	archivo.close()	
	return matriz	

#a) genero la matriz de transición	
matrizDeTransicion = generarMatriz()
	
# La matriz de transición de estados se obtiene de la siguiente manera, dado que el ejercicio impone por simplicidad que la cantidad máxima
# de clientes que se permite en simultaneo en el Homebanking es 50, entonces la matriz de transición es de 51 x 51 (Tambien se incluye la 
# cantidad de 0 clientes).
# Cada elemento de la matriz es el cambio de estado al siguiente, es decir el paso del estado i al j, por ejemplo si el elemento de la
# matriz es el (1,2) entonces es la probabilidad de la cantidad de clientes conectados sea 2 sabiendo que en el minuto anterior estaba 
# conectado solo 1.   

#b) 

def generarOtroEstado(Lista):
	aleatorio = random.random()
	sumaTotal = Lista[0]
	i=0
	while(aleatorio > sumaTotal ):
		if(i<50):	
			sumaTotal = sumaTotal + Lista[i]
			i=i+1
		sumaTotal = sumaTotal + Lista[i]
	return i

estados = []
estadoActual = 0
estados.append(estadoActual)
observaciones = 100

#simulo los valores de los estados en cada momento
for i in range(observaciones):  
	estadoActual = generarOtroEstado(matrizDeTransicion[estadoActual])
	estados.append(estadoActual)

#grafico de como se modifican los clientes a lo largo de las observaciones.
plt.plot(estados)
plt.title("Evolución del sistema")
plt.xlabel('Observaciones')
plt.ylabel('Conectados')
plt.show()		

#c)
estados = []
estadoActual = 0
estados.append(estadoActual)
observaciones = 100000

#simulo los valores de los estados en cada momento
for i in range(0,observaciones):
	estadoActual = generarOtroEstado(matrizDeTransicion[estadoActual])	
	estados.append(estadoActual)

#Histograma
plt.title('Histograma')
plt.xlabel('Estados')
plt.ylabel('Cantidades')
plt.hist(estados, bins =50, alpha=0.6, ec='black')
plt.grid(True)
plt.show()


#d)






#e)
#P(i-->j >=40) <= 0.1

probabilidad=0
for i in range(0,51):
	for j in range(40,51):
		probabilidad = probabilidad + funcionProbabilidad(i,j)

if (probabilidad < 0.1):
	print("Es recomendable hacer la migración a otro servidor")
else:
	print("No es recomendable hacer la migración a otro servidor")	 
				


