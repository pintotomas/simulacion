import instruccion
import procesador
import queue
import threading
import time

generador_instrucciones = instruccion.InstruccionFactory()
#cola_instrucciones_a_procesar = queue.Queue()
cola_instrucciones_a_buscar_dato_memoria = queue.Queue()

contador_instrucciones_generadas = 0

cola_instrucciones = queue.Queue()
threading.Thread(target=procesador.procesar, args=(cola_instrucciones,)).start()

while True:

  contador_instrucciones_generadas += 1
  instruccion = generador_instrucciones.nueva_instruccion()
  if instruccion.lee_memoria:
    #print ("Añadiendo nueva instruccion al procesador")
    cola_instrucciones.put(instruccion)
  else: 
    cola_instrucciones_a_buscar_dato_memoria.put(instruccion)	
  #print("\rcantidad total: "+str(contador_instrucciones_generadas))
  print("Cantidad a procesar: "+str(cola_instrucciones.qsize()))
  #time.sleep(4)
  # print("Cantidad a buscar en memoria: "+str(cola_instrucciones_a_buscar_dato_memoria.qsize()))