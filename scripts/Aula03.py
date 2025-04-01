# -*- coding: utf-8 -*-
"""
Nessa aula com: 
    Arrays numpy
    pandas dataframe
    matplotlib
    
    requisitos: pip install spyder numpy pands ma
"""
#%%
import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

#%% Criando uma lista de números inteiros, strings, float,

listA = [1, 2, 3]
listB = [1, 2, 3, 'Salve o corinthias']
listC = [1, 2, 3, 20.5]
print(listA)
print(listB)
print(listC)
#%%
#Trabalhando co Numpy

#criando um array no numpy

arr = np.array([0.7, 0.75, 1.85])
print(arr)

#criando um arranjo a partir de uma lista de números

arr2 = np.array(listA)
print(arr2)

#criando um array numpy a partir de uma lista com string
arr3 = np.array(listB)

#criando uma matriz de números float

precip = np.array([[1.07, 0.44, 1.50], [0.27, 1.33, 1.72]])
print(precip)

# acessando o valor da primeira linha e coluna 
print(precip[0,0])

#acessando todos os valores da primeira linha 
print(precip[0,:])

#acessando todos os valores da primeira colina
print(precip[:,0])

#extraindo os dois primeiros valores da primeira linha 
print(precip[0,0:2])

#extraindo os dois primeiros valores da primeira coluna 
print(precip[0:2,0])

#extrarir os dois últimos valores da ultima coluna. Pode ser usado quando vc não sabe a dimenção da matriz.
print(precip[-1, -1])

#%%
#criando matrizes com multiplas dimenções 
#criar um arranjo de dados com inicio (1), fim (16) e passo (passo)
x = np.arange(1,16,1)

#Mudando o shape/dimensão da matriz 
xreshape = x.reshape(3,5)
x = np.arange(1,16,1).reshape(3, 5) 

#transposta
print(xreshape.transpose())

#criando matriz da números aleatórios 3D
matrand = np.random.rand(10,100,100)

#recortando matriz
matrandslice = matrand[0,:,:]

#criando matriz com 4D sw números aleatórios (esse daqui não funcionou)
matrand4D = np.random.rand(3, 10, 100,100)
print(matrand4D)

#dimensão da matriz 
print(matrand4D.ndim)

#Shape da matriz 
print(matrand4D.shape)

#Número de elementos 
print(matrand4D.size)

#multiplicação escalar
print(matrand4D*3.5)

#Abrir arquivo texto 
teste1 = np.loadtxt(r"C:\Users\Usuario\Documents\GitHub\ENS5132\data\teste1.txt")
print(teste1)
#abrir arquivo separadp por virgula .csv
teste2 = np.loadtxt(r"C:\Users\Usuario\Documents\GitHub\ENS5132\data\teste2.csv",delimiter=',')

# operação media da matriz 4D, ele pega todos os valores empilha e faz a média 
print(matrand4D.mean())

#outra ex pegar todos os maximos da primerira dimensão e fazer a média 
maxMat4D = matrand4D.max(axis=0)

#%% Pandas DataFrame
#fazemos inverso primeiro abrimos um arquivo 

df = pd.read_csv("pegar o link da pasta como dados ", encoding= 'Latil')

df.describe()
df.info()
df.valor #valor é a coluna 
df.Valor.plot() #isso vai gerar um grafico com os valores 

# se vc quer que ele filtre os dados pode selecionar 
df

#%%