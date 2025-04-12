# -*- coding: utf-8 -*-
"""
trabalhando com o pandas 

"""
import numpy as np
import pandas as pd 
import os
""""
crianod um dataframe manualmente 
data=date
dado=data
"""
df= pd.DataFrame(colums=['date','NH3'], 
                         data = [
                             ['2025/04/01',0.35],
                             ['2025/04/02',1.01]
                             ])

#criando mais coisas dentro do df
df['NO3']= np.nan
df['O2']=[2,10]
df['SO4'] = np.nan
df['SO4'][0] = 10
#%%    Trabalhando com dados reais 
uf = 'ES'

# definir o caminho para a pasta de dados 

dataDir = r"C:\Users\Usuario\Documents\GitHub\ENS5132\dataES\ES"+'/'+ uf

# lista de arquivos 
datalist = os.listdir(dataDir)

# mover para a pasta de dados/uf
os.chdir(dataDir)
allFiles =[]

# Loop na lista datalist 
for fileInList in datalist:
    print(fileInList)
    dfConc = pd.read_csv(fileInList,encoding='Latin1')
    allFiles.append(dfConc)
    
    #### buraco 
    allFiles = pd.concat(allFiles)
    # usando logica 
   # criando coluna datatime 
datetimeDF = pd.to_datetime(stationDF.Data, format='%Y-%m-%d')

# criar uma coluna dentro do da
stationDF['datetime']=datetimeDF
# transformando a coluna datetime em index 
stationDF = stationDF.set_index(stationDF['datatime'])

#extrair o ano e mes 
strationDF['year']=stationDf.index.year
strationDF['month']=stationDf.index.month
strationDF['day']=stationDf.index.day

#extraindo a hora 
hora = strationDF.Hora.str.split(':')

horasDf = []
for hora in horas:
    print(hora[0])
    horaDf.append(hora[0])
    stationDF['hour']=horaDf
    
    #corrigindo a coluna datelina 
stationDf['datetime']=pd.to_datetime(stationDf)
    
