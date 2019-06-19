

SECOND_TO_MICROSECOND = 1000000
TASA_ARRIBO_INSTRUC = 250



def run(modo):
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
  cola_instrucciones = queue.Queue()

  threading.Thread(target=procesador.procesar, args=(cola_instrucciones, modo)).start()
  if modo == "alternativa_1":
    threading.Thread(target=memoria_principal.buscar, args=(cola_acceder_memoria, cola_instrucciones,)).start()
  elif modo == "alternativa_2":
    threading.Thread(target=cache.buscar, args=(cola_acceder_memoria, cola_instrucciones,)).start()
  while True:
    tiempo_de_espera_arribo_instruc = numpy.random.exponential(TASA_ARRIBO_INSTRUC)
    time.sleep(tiempo_de_espera_arribo_instruc/float(SECOND_TO_MICROSECOND))
    instruccion = generador_instrucciones.nueva_instruccion()
    if not(instruccion.lee_memoria):
      cola_instrucciones.put(instruccion)
    else: 
      cola_acceder_memoria.put(instruccion)	
