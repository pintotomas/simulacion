import queue
import time
import csv
import numpy
def procesar(cola_instrucciones, modo):
  cantidad_procesada = 0
  minutos_procesamiento = 0
  start_time = time.time()
  while True:
    if not (cola_instrucciones.empty()):
      time.sleep(numpy.random.exponential(cola_instrucciones.get().costo()))
      cantidad_procesada += 1
      print("\r" + modo + " Cantidad procesada: "+str(cantidad_procesada), end="")

    # cada 60 segundos registro la cantidad de instrucciones que fueron procesadas
    actual_time = time.time()
    if actual_time - start_time >= 60:
      minutos_procesamiento += 1
      start_time = actual_time
      with open(modo+'.csv', mode='a') as registro_procesamiento:
        writer = csv.writer(registro_procesamiento, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([str(minutos_procesamiento), str(cantidad_procesada)])
   



      
