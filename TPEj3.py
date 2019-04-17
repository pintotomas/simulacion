#/usr/bin/env/ python
import numpy as np
import matplotlib.pyplot as plt

# distribucion normal
u1 = np.random.normal(0,1, 100000)
u2 = np.random.normal(0,1, 100000)

###Box muller
z1 = np.sqrt(-2 * np.log(u1)) * np.cos(u2)
z2 = np.sqrt(-2 * np.log(u1)) * np.sen(u2)

#Histograma
plt.hist(u1, bins =60, alpha=0.5, ec='black')
plt.hist(u2, bins =60, alpha=0.5, ec='green')
plt.grid(True)
plt.show()



