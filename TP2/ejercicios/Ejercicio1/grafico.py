import pandas as pd
import matplotlib.pyplot as plt
alt1 = pd.read_csv("alternativa_1.csv", names=["minuto", "cantidad_procesada"])
alt2 = pd.read_csv("alternativa_2.csv", names=["minuto", "cantidad_procesada"])

# gca stands for 'get current axis'
ax = plt.gca()
alt1.plot(x = 'minuto', y = 'cantidad_procesada', label = 'alternativa 1', color = 'red', ax = ax)
alt2.plot(x = 'minuto', y = 'cantidad_procesada', label = 'alternativa 2', color = 'green', ax = ax)

ax.set_xlabel('Minutos de procesamiento')
ax.set_ylabel('Cantidad de instrucciones procesadas')
plt.show()