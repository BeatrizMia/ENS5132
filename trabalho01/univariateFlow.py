# -*- coding: utf-8 -*-
"""
Created on Sat May  3 10:19:29 2025

@author: Usuario
"""
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import os
from scipy import stats
from FlowMaxFigures import normalityCheck
#Esta função testa a hipótese nula de que uma amostra provém de uma distribuição normal
uf= 'GO'
repoPath = r"C:\Users\Usuario\Documents\GitHub\ENS5132\trabalho01"
dataDir = repoPath+'/'+'outputs'+'/'+uf
dataList = os.listdir(dataDir)
print(dataList)

#os.chdir(dataDir)

aqPath = r"C:\Users\Usuario\Documents\GitHub\ENS5132\trabalho01\outputs\GO\flow.csv"

aqData = pd.read_csv(aqPath)

# chama a função que cria a figura no scrip airQualityFigures para gerar
# Histogramas com transformações
# normalityCheck(aqTableAlvo,repoPath,uf,stationAlvo,pol)

# Teste de normalidade- Gaussianidade
 #  flow.normaltest(np.log(aqData['flow'].dropna()))
  #testBox = flow.normaltest(stats.boxcox(aqData['flow'].dropna())[0])

  # Gerar o histograma e as transformações
testLog = normalityCheck(aqData, repoPath, uf, stationAlvo, pol)
