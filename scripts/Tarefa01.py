import numpy as np

#Crie uma matriz com números aleatórios com duas dimensões (2D) com 100 linhas e 100 colunas.
A = np.random.rand(100,100)*1000
A = A.astype(int)

#Determine o valor da última linha e coluna
print(A[99,99])

#Recorte a primeira linha e liste os valores
B = A[0,:]
print(B)

