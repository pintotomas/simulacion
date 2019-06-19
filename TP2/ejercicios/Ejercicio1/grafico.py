import pandas as pd
import matplotlib as plt
alt1 = pd.read_csv("alternativa_1.csv", names=["minuto", "cantidad_procesada"])
alt2 = pd.read_csv("alternativa_2.csv", names=["minuto", "cantidad_procesada"])
alt1.plot()