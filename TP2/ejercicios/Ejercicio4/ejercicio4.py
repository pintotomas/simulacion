
import simpy 
import random as rnd
import numpy
import instruccion
generador_instrucciones = instruccion.InstruccionFactory()

tiempos = []

PROBA_ACCEDER_CACHE = 0.6
TASA_ACCESO_CACHE = 500
TASA_ACCESO_MEMORIA_CON_CACHE = 1500
TASA_ACCESO_MEMORIA_SIN_CACHE = 2000
TASA_ARRIBO_INSTRUC = 250

class Procesamiento:
	def __init__(self, env, tiempos_procesamientos ,instruc, cache ):

		self.env = env
		self.instruc = instruc
		self.tiempo_ejecucion = self.calcular_tiempo_ejecucion(cache)
		self.tiempo_procesamiento = None 
		self.registro_procesamientos= tiempos_procesamientos



	def ejecutar(self, procesador):
		with procesador.request() as req:
			self.tiempo_procesamiento = env.now
			yield req 
			yield self.env.timeout(self.tiempo_ejecucion)
			self.tiempo_procesamiento = env.now - self.tiempo_procesamiento 
			self.registro_procesamientos.append(self.tiempo_procesamiento)

	def calcular_tiempo_ejecucion(self,cache):
		tiempo_ejecucion = 0

		if self.instruc.lee_memoria:

			if not cache:
				tiempo_ejecucion += numpy.random.exponential(1/TASA_ACCESO_MEMORIA_SIN_CACHE)


			elif cache:

				en_cache = (rnd.uniform(0,1) <= PROBA_ACCEDER_CACHE)

				if not en_cache:
					tiempo_ejecucion += numpy.random.exponential(1/TASA_ACCESO_MEMORIA_CON_CACHE) #busqueda en memoria
				else:
					tiempo_ejecucion += numpy.random.exponential(1/TASA_ACCESO_CACHE) #busqueda en cache


		tiempo_ejecucion += numpy.random.exponential(1/self.instruc.costo())

		return tiempo_ejecucion



def procesar_instrucciones(environment, cantidad, cache):
	procesador = simpy.Resource(env, capacity = 1)
	for i in range(cantidad):
		instruc = generador_instrucciones.nueva_instruccion()
		proc = Procesamiento(env, tiempos,instruc, cache)
		environment.process(proc.ejecutar(procesador))
		tiempo_prox_instruc = numpy.random.exponential(1/TASA_ARRIBO_INSTRUC)
		yield environment.timeout(tiempo_prox_instruc)



cantidad = 40000

env = simpy.Environment()
env.process(procesar_instrucciones(env, cantidad, False))
env.run() 
print(sum(tiempos))
print("Tiempo total de ejecucion alternativa 1 40000 instrucciones: ", round(sum(tiempos)))


tiempos = []
env = simpy.Environment()
env.process(procesar_instrucciones(env, cantidad, True))
env.run() 
print("Tiempo total de ejecucion alternativa 2 40000 instrucciones: ", round(sum(tiempos)))
