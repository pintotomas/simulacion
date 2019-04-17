#/usr/bin/env/ python
import math 
import numpy as np
import matplotlib.pyplot as plt



###Box muller

def z1(u1,u2):
	return math.sqrt(-2 * math.log(u1)) * math.cos(u2)

def z2(u1,u2):
	return math.sqrt(-2 * math.log(u1)) * math.sen(u2)

# distribucion normal
u1 = np.random.normal(0,1, 100000)
u2 = np.random.normal(0,1, 100000)


plt.hist(u1, bins =60, alpha=0.5, ec='black')
plt.grid(True)
plt.show()



