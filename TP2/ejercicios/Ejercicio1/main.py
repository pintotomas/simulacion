
TASA_ARRIBO_INSTRUC = 250
n = 100000 #cantidad de instrucciones que genero

iteraciones = 20

def run(modo):
  import instruccion
  import numpy
  if modo is not "CACHE" and modo is not "RAM":
    print("MODO INCORRECTO")
    return 

  generador_instrucciones = instruccion.InstruccionFactory()
  tiempo_proceso = float(0)
  for x in range(n):
    tiempo_de_espera_arribo_instruc = numpy.random.exponential((1/TASA_ARRIBO_INSTRUC))
    instruccion = generador_instrucciones.nueva_instruccion()
    tiempo_proceso += tiempo_de_espera_arribo_instruc + instruccion.costo(modo)
  return tiempo_proceso

print("Corriendo alternativa 1 20 veces")
tiempo_total_alt1 = 0
for x in range(iteraciones):
  tiempo = run("RAM")
  tiempo_total_alt1 += tiempo
print("Tiempo promedio alternativa 1:" + str(round(tiempo_total_alt1/iteraciones, 2)))

print("Corriendo alternativa 2 20 veces")
tiempo_total_alt2 = 0
for x in range(iteraciones):
  tiempo = run("CACHE")
  tiempo_total_alt2 += tiempo
print("Tiempo promedio alternativa 2:" + str(round(tiempo_total_alt2/iteraciones, 2)))