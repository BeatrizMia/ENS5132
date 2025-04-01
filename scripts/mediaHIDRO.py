
import numpy as np

import matplotlib.pyplot as plt

#%%
#dentro do espaco de tempo de 0 á 5 temos 10 amostras 
t = np.linspace(0, 5, 10)

y = np.cos(t)
print(y)

#usar o matplotlib para gerar um grafico
plt.plot(t, y)
#ele gerou o grafico mais ele não mostra, para mostrar tem que usar outra função
plt.show()
