# -*- coding: utf-8 -*-
"""
Data: 01/04/25

"""
#%% importar pacotes utilisados 
import numpy as np

import pandas as pd 

import matplotlib.pyplot as plt

import os
#%%   Revisão numpy e fazendo uma analise de dados 

#criando um vetor com arranjo de dados do modo np.arrange(menor valor,maior valor, variando de 0.15 cada numero de forma aleatória), número de dimenssões = Nemor valor *maior valor

x = np.arange(-10,20, 0.15)

print(x)

print('Esta é a quarta posição do meu vetor x:'+ str(x[3]))

print('Esse são os 3 primeiros valores' + str(x[0:3]))


# substituir um valor dentro do vetor 
x[9] = 9999999999999
x[11] = -9999999999

print('Novo valor da dimensão x[9] = '+ str(x[9]))
print('Novo valor da dimensão x[11] = '+ str(x[11]))

print(x)
# f9 complila apenas a linha 

# extraindo a média 

meanX = np.mean(x)
print('Média das dimenções dos vetores:'+ str(meanX))

# Operação Booleana (lógica true or false)

# and = &
# or = | 
# vamos usar  a lógica booleana para encontar os valores que estão fora do padrão -10<x<20
# Para isso criamos um vetor booleana, esse vetor preenche cada posição do vetor com true or false 
vecBool = (x>20) | (x<-10)

print("Verificando se os dados estão dentro do parámetro: ", vecBool)

#criando um vetor que seja preenchido com os valores que estão fora do padão, que são os True 
valErrado = x[vecBool]

# Vamos ver a seguir 3 formas de arrumar dados fora do padrão, 
#1° substituindo os valores errados por 0, Pode alterar a média bastante
#2° substituindo os valores errados por nan (Usa nanmean para ignorar NaNs) 
#3° substituindo os valores errados pela média (Mais preciso e suave)

# 1°) Agora para preencher os true com 0 devemos:
    
# criar uma cópia do vetor x (vetor com os dados) usando a função copy()

x2 = x.copy() 
# dessa copia vamos preencher os valores true com 0
x2[vecBool]=0

# A ideia é preencher os valores errados com a média de todos os outros valores
# Para descobrir a média sem dos valores discrepantes vamos
meanX2= np.mean(x2)

print("Média dos dados substituindo números discrepantes por 0 = ", meanX2)

# 2°) Agora para preencher os true com nan devemos:

# criar uma cópia do vetor x
x3 = x.copy()

# dessa cópia vamos preencher os valores true com nan, usando np.nan

x3[vecBool] = np.nan

# depois para calcular a media é importante usando np.nanmean(), 
meanX3= np.nanmean(x3)

print("Média dos dados ignorando os números discrepantes ",meanX3)

# 3°) Agora para preencher os true com a média 

# criar uma cópia do vetor x

x4= x.copy()

# dessa copia vamos usar o passoa anterior e substituir os nan pela media sem os dados discrepantes 
# usando para substituir os true np.nanmean(x3) 
# ou seja, onde tiver true vamos supstituir pela media de x3 ignorando os nan 

x4[vecBool] = np.nanmean(x3)

meanX4= np.mean(x4)

print("Média dos dados substituindo os valores discrepantes pela média dos valores ignorando o errado: ", meanX4)

#%%Usando o matplotlib para inspecionar os vetores 
# Os códigos a baixo vai gerar 4 graficos usando os dados de x, x2, x3, x4. 

fig, ax = plt.subplots(4)
#Essa função cria 4 gráficos empilhados verticalmente em uma unica coluna
ax[0].plot(x) #(Original)
ax[1].plot(x2) #(corrigido com 0 )
ax[2].plot(x3) #(corrigido com nan)
ax[3].plot(x4) #(corrigido com a media)

#%% loop and Range
# O loop começa do 0 e vai até o 9, a cada loop ele soma 1 
# Vai preenchendo o val com um valor que muda a cada loop
# val = 2^0, 2^1,..., 2^9
# como o valor de val muda a cada loop temos que colocar o print dentro do loop 
 
for ii in range(0, 10):
 val = 2**ii
 print(val)

    
# Loop utilizando Range e acumulando em um vetor 
# append é uma função para adicionar um elemento no final do vetor 
vetor = [] 
for ii in range(0,10):
   val = 2**ii
   vetor.append(val)
   print(vetor)

# agora queremos um loop que armazene os valores de cada loop, porem que dada valor seja  soma do seu anterior 
vetorAcumulado = []
soma = 0

for ii in range(0,10):
    soma = soma + 2**ii
    vetorAcumulado.append(soma)
    print(vetorAcumulado)
    
#%% Loop de strings 
    

alunas= ['Mariana', 'Bianca', 'AnaJulia', 'Mariah']
  
# esse for percorre a lista alunas, e a cada volta do loop, a variável aluna recebe um nome
# por exemplo, no primeiro loop aluna = mariana, segundo loop aluna = bianca etc 
  
for aluna in alunas:
    print('A nota da aluna'+aluna+' é : '+str(np.random.rand(1)*10))

# a função np.ramdom.rand(1)*10, gera números aleatórios de 0 à 1 e multiplica por 10

# Trabalhando com pandas 

# Criando um Datarame manualmente 
#DataFrame é uma estrutura de dados em forma de tabela, com linhas e colunas

# o dataframe pode ser estruturado de diferentes maneiras 
tabela = { 
    'Alunas': ['Mariana', 'Bianca', 'AnaJulia', 'Mariah'],
   ' Notas': [ 8, 7, 9, 10]
    }
df = pd.DataFrame(tabela)

print(df)

# outra forma de fazer 

df2 = pd.DataFrame({
    'Alunas':[ 'Mariana', 'Bianca', 'AnaJulia', 'Mariah'],
                  'Notas' :[ 8, 7, 9, 10]
                  })
df2['Média'] = [10, 9, 6, 10]
print(df2)

# outro exemplo, forma tabelas preenchendo por linha 

df3 = pd.DataFrame(columns=['date', 'NH3'],
               data=[
            ['2025/04/01',0.35],
                      ['2025/04/02',1.01]
                      ])
print(df3)

# da para colocar variaveis dentro do df como colunas
df3['NO3'] = np.nan #sem valor 
df3['O2'] = [2,10]
df['SO4'] = np.nan 


print(df3)
