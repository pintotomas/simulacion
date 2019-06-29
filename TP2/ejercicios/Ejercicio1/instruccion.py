import random
import numpy

PROBA_ACCEDER_MEMORIA = 0.65
PROBA_SER_SIMPLE = 0.6
PROBA_ACCEDER_CACHE = 0.6
TASA_ACCESO_CACHE = 500
TASA_ACCESO_MEMORIA_CON_CACHE = 1500
TASA_ACCESO_MEMORIA_SIN_CACHE = 2000
TASA_EJECUCION_INSTRUCCION_SIMPLE = 60
TASA_EJECUCION_INSTRUCCION_COMPLEJA = 10 

class InstruccionFactory(object):
  
  @staticmethod
  def nueva_instruccion():
    tipo = random.uniform(0,1)
    memoria = random.uniform(0,1)
    lee_memoria = False
    if (memoria <= PROBA_ACCEDER_MEMORIA):
      lee_memoria = True
    if (tipo <= PROBA_SER_SIMPLE):
      return InstruccionSimple(lee_memoria)
    else:
      return InstruccionCompleja(lee_memoria)

class Instruccion(object):

  def __init__(self, lee_memoria, tasa):
    self.lee_memoria = lee_memoria
    self.tasa_tiempo_ejecucion = tasa

  def costo(self, modo):
    costo = numpy.random.exponential((1/self.tasa_tiempo_ejecucion))
    if self.lee_memoria and modo == "CACHE":
      u = random.uniform(0,1)
      if u <= PROBA_ACCEDER_CACHE:
        costo += numpy.random.exponential((1/TASA_ACCESO_CACHE))
      else:
        costo += numpy.random.exponential((1/TASA_ACCESO_MEMORIA_CON_CACHE))
    elif self.lee_memoria: #Alt 1
      costo += numpy.random.exponential((1/TASA_ACCESO_MEMORIA_SIN_CACHE))
    return costo

class InstruccionCompleja(Instruccion):

  def __init__(self, lee_memoria):
    super().__init__(lee_memoria, TASA_EJECUCION_INSTRUCCION_COMPLEJA)

class InstruccionSimple(Instruccion):

  def __init__(self, lee_memoria):
    super().__init__(lee_memoria, TASA_EJECUCION_INSTRUCCION_SIMPLE)

    