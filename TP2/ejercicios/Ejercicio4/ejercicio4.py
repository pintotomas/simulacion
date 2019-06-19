
import simpy 
import random as rnd
import numpy
import instruccion
generador_instrucciones = instruccion.InstruccionFactory()

tiempos = []
SECOND_TO_MICROSECOND = 1000000

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
				tiempo_ejecucion += numpy.random.exponential(2000/float(SECOND_TO_MICROSECOND))


			elif cache:

				en_cache = (rnd.uniform(0,1) <= 0.6)

				if not en_cache:
					tiempo_ejecucion += numpy.random.exponential(1500/float(SECOND_TO_MICROSECOND)) #busqueda en memoria
				else:
					tiempo_ejecucion += numpy.random.exponential(500/float(SECOND_TO_MICROSECOND)) #busqueda en cache


		tiempo_ejecucion += numpy.random.exponential(self.instruc.costo())

		return tiempo_ejecucion



def procesar_instrucciones(environment, cantidad, cache):
	procesador = simpy.Resource(env, capacity = 1)
	for i in range(cantidad):
		instruc = generador_instrucciones.nueva_instruccion()
		proc = Procesamiento(env, tiempos,instruc, cache)
		environment.process(proc.ejecutar(procesador))
		tiempo_prox_instruc = numpy.random.exponential(250/float(SECOND_TO_MICROSECOND))
		yield environment.timeout(tiempo_prox_instruc)



cantidad = 200000

env = simpy.Environment()
env.process(procesar_instrucciones(env, cantidad, False))
env.run() 
print(sum(tiempos))
print("Tiempo total de ejecucion alternativa 1 (microsegundos) 200000 instrucciones: ", round(sum(tiempos)))


tiempos = []
env = simpy.Environment()
env.process(procesar_instrucciones(env, cantidad, True))
env.run() 
print("Tiempo total de ejecucion alternativa 2 (microsegundos) 200000 instrucciones: ", round(sum(tiempos)))