import queue
import time

def procesar(cola_instrucciones):
  cantidad_procesada = 0
  while True:
    if not (cola_instrucciones.empty()):
      time.sleep(cola_instrucciones.get().costo())
      cantidad_procesada += 1
      print("\rCantidad procesada: "+str(cantidad_procesada), end="")
