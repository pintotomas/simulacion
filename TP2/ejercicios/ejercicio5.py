import random
from random import randint
import simpy
import numpy
from numpy import mean


client_count = 10000 
arrival_rate = 45
tiempo_esperas = []

class Client(object):

    def process_duration(self):
        if (self.type == 'A'):
            return (75 + randint(-10, 10))
        if (self.type == 'B'):
            return (60 + randint(-15, 15))
        return (90 + randint(-20, 20))


    def __init__(self, env):
        self.tiempo_entrada = env.now
        self.env = env
        self.type = numpy.random.choice(['A', 'B', 'C'], p=[0.6, 0.25, 0.15])

    def process(self, cashier):
        global tiempo_esperas
        with cashier.request() as req:
            process_duration = self.get_process_duration()
            yield req
            yield self.env.timeout(process_duration)
            
        # print("%.2f Client type %s attended" % (self.env.now, self.type))
        tiempo_esperas.append(env.now - self.tiempo_entrada)

    def get_process_duration(self):
        return self.process_duration()

class Balanceador(object):   

    def __init__(self, round_robin):
        self.resources = []
        self.round_robin = round_robin
        self.last_assigned = 0

        for i in range(6):
            self.resources.append(simpy.Resource(env, capacity = 1))
            self.cantidad_colas = 6            


    def get_resource(self):
	#If we use Round Robin politic
        if self.round_robin:
            self.last_assigned = (self.last_assigned + 1) % 6
            return self.resources[self.last_assigned]
        else:
            # If we assign randomly
            random_value = randint(0,5)
	    return_value = self.resources[random_value]
            return return_value


def generate_clients(environment, count, interval):
    #Select one the options in the exercise
    balanceador_round_robin = Balanceador(False)
    balanceador_2 = Balanceador(True)

    balanceador = balanceador_2

    for i in range(count):
        client = Client(env)
        environment.process(client.process(balanceador.get_resource()))
        t = random.expovariate(1.0 / interval)
        yield environment.timeout(t)


env = simpy.Environment(
env.process(generate_clients(env, client_count, arrival_rate))
env.run()

print("Tiempo espera: %s" % mean(tiempo_esperas))
print("Tiempo max: %s" % max(tiempo_esperas))
print("Tiempo min: %s" % min(tiempo_esperas))
print("Tiempo total: %s" % env.now)
