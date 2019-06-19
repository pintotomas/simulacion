import os
import numpy

cant=50
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
	for k in range(i,cant+1):
		 sumatoria = sumatoria + jMayorIgualAi(i,k)
	return (1-sumatoria)

def funcionProbabilidad(i,j):
	if (i<=j):
		probabilidad = jMayorIgualAi(i,j)
	else:
		probabilidad = jMenorAi(i,j)
	#return round(probabilidad,4)
	return probabilidad

def generarMatriz():
	archivo = open("matrizDeTransicion.txt","w")	
	cadena = ''
	for m in range (0,cant+1):
		for n in range (0,cant+1):
			cadena = cadena + str(funcionProbabilidad(m,n)) + ','
		archivo.write(cadena + os.linesep)
		cadena=''
	archivo.close()		

#a) genero la matriz de transición	
generarMatriz()
	
# La matriz de transición de estados se obtiene de la siguiente manera, dado que el ejercicio impone por simplicidad que la cantidad máxima
# de clientes que se permite en simultaneo en el Homebanking es 50, entonces la matriz de transición es de 51 x 51 (Tambien se incluye la 
# cantidad de 0 clientes).
# Cada elemento de la matriz es el cambio de estado al siguiente, es decir el paso del estado i al j, por ejemplo si el elemento de la
# matriz es el (1,2) entonces es la probabilidad de la cantidad de clientes conectados sea 2 sabiendo que en el minuto anterior estaba 
# conectado solo 1.   

#b) 

#def generarSiguienteEstado(estadoActual):

 #   if (estadoActual <= 0):
  #      j = numpy.arange(estadoActual, 51)  
  #      estado = numpy.random.choice(j, p=matriz)  

   # return estado

estados = []
estadoActual = 0
observaciones = 100

#for i in range(observaciones):  
 #   estadoActual = generarSiguienteEstado(estadoActual)
  #  estados.append(estadoActual)

# valores de los estados en cada momento
#plt.plot(estados)
#plt.show()		

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
				
	





	


