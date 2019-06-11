import random
SECOND_TO_MICROSECOND = 1000000
class InstruccionFactory(object):
  
  @staticmethod
  def nueva_instruccion():
    # Tiro un random entre 0 y 1, si es menor o igual a 0.6 entonces
    # es una instruccion simple 
    # idem memoria
    tipo = random.uniform(0,1)
    memoria = random.uniform(0,1)
    lee_memoria = False
    if (memoria < 0.65):
      lee_memoria = True
    if (tipo <= 0.6):
      return InstruccionSimple(lee_memoria)
    else:
      return InstruccionCompleja(lee_memoria)

class InstruccionCompleja(object):

  def __init__(self, lee_memoria):
    self.lee_memoria = lee_memoria

  def costo(self):
    return 10/float(SECOND_TO_MICROSECOND)

class InstruccionSimple(object):

  def __init__(self, lee_memoria):
    self.lee_memoria = lee_memoria

  def costo(self):
    return 60/float(SECOND_TO_MICROSECOND)
    