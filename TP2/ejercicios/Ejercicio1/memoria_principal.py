import queue
import time
import numpy

SECOND_TO_MICROSECOND = 1000000
TASA_ALT1 = 2000

def buscar(cola_acceso_memoria, cola_procesador):
  while True:
    if not (cola_acceso_memoria.empty()):
      instruccion = cola_acceso_memoria.get()
      #Busco el dato
      tiempo_de_espera_busqueda_dato = numpy.random.exponential(TASA_ALT1)
      time.sleep(tiempo_de_espera_busqueda_dato/float(SECOND_TO_MICROSECOND))
      #Mando la instruccion a procesar
      cola_procesador.put(instruccion)
