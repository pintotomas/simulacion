import queue
import time


def procesar(cola_instrucciones):
  while True:
    if not (cola_instrucciones.empty()):
      print("*********PROCESANDO*********")
      time.sleep(cola_instrucciones.get().costo())
      print ("PROCESADA!!")