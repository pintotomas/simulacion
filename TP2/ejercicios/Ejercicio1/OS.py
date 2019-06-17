import instruccion
import procesador
import queue
import threading
import time
import numpy
import memoria_principal
import cache

generador_instrucciones = instruccion.InstruccionFactory()
cola_acceder_memoria = queue.Queue()

contador_instrucciones_generadas = 0

cola_instrucciones = queue.Queue()

threading.Thread(target=procesador.procesar, args=(cola_instrucciones,)).start()
threading.Thread(target=cache.buscar, args=(cola_acceder_memoria,
 cola_instrucciones,)).start()

SECOND_TO_MICROSECOND = 1000000
TASA_ARRIBO_INSTRUC = 250

while True:
  tiempo_de_espera_arribo_instruc = numpy.random.exponential(TASA_ARRIBO_INSTRUC)
  time.sleep(tiempo_de_espera_arribo_instruc/float(SECOND_TO_MICROSECOND))
  contador_instrucciones_generadas += 1
  instruccion = generador_instrucciones.nueva_instruccion()
  if not(instruccion.lee_memoria):
    cola_instrucciones.put(instruccion)
  else: 
    cola_acceder_memoria.put(instruccion)	
  
