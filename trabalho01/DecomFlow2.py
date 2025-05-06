# -*- coding: utf-8 -*-
"""
Created on Sat May  3 19:36:49 2025

@author: Usuario
"""

"""
Created on Thu May  1 15:02:43 2025

@author: Carlos - SC
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
from datetime import datetime
import statsmodels.api as sm

uf= 'GO'
repoPath = r"C:\Users\Usuario\Documents\GitHub\ENS5132\trabalho01"
aqPath = r"C:\Users\Usuario\Documents\GitHub\ENS5132\trabalho01\outputs\GO\flow.csv"

#lendo o arquivo 
aqData = pd.read_csv(aqPath)

# Substituir vírgulas por pontos na coluna 'flow'
aqData['flow'] = aqData['flow'].str.replace(',', '.', regex=False)

aqData['flow'] = aqData['flow'].str.replace(' ', '')  # Remover espaços, se houver

# Garantir que a coluna 'flow' tenha apenas valores numéricos
aqData['flow'] = pd.to_numeric(aqData['flow'], errors='coerce')

# Calcular a média dos valores de 'flow', ignorando os NaN
mean_flow = aqData['flow'].mean()
print(mean_flow)
# Substituir os NaN pela média calculada
aqData['flow'] = aqData['flow'].fillna(mean_flow)


# Função para decomposição da série temporal
def timeSeriesDecompose(aqData, uf, repoPath):
    # Decomposição da série temporal
    
    # Seleciona apenas a coluna dos poluentes (vazão no caso)
    dataDecompose = aqData[['datetime', 'flow']]
   
    # Garantir que a coluna 'datetime' está no formato datetime
    dataDecompose['datetime'] = pd.to_datetime(dataDecompose['datetime'])
    
    #transformando datetime em im index
    dataDecompose = dataDecompose.set_index('datetime')
    
    # Agrupa por mês e calcula a média mensal
    dataDecomposeMonthly = dataDecompose.groupby(pd.Grouper(freq="M")).mean()
    
    # Converte para a função de decomposição do statsmodel
    # Agora a variável 'dataDecomposeMonthly' é definida corretamente
    dataDecomposeMonthly = pd.Series(np.array(dataDecomposeMonthly['flow']), index=pd.to_datetime(dataDecomposeMonthly.index))
    
    # Gerando um índice periódico com os meses
    full_index = pd.date_range(start=dataDecomposeMonthly.index.min(), end=dataDecomposeMonthly.index.max(), freq='M')
    
    # Reindexando para preencher os dados faltantes com NaN
    complete_data = dataDecomposeMonthly.reindex(full_index)
    
    # Interpolando dados que possuem NaN
    complete_data = complete_data.interpolate().dropna()
    
    # Decompondo a série temporal utilizando a decomposição sazonal do statsmodel
    res = sm.tsa.seasonal_decompose(complete_data, period=12)
    
    # Gerando figura para a decomposição
    fig, axes = plt.subplots(ncols=1, nrows=4, sharex=True, figsize=(10, 8))
    
    res.observed.plot(ax=axes[0], legend=False, color='green')
    axes[0].set_ylabel('Original')
    axes[0].set_title('Decomposição da Série Temporal (Vazão)')
    
    res.trend.plot(ax=axes[1], legend=False, color='red')
    axes[1].set_ylabel('Tendência')
    
    res.seasonal.plot(ax=axes[2], legend=False, color='yellow')
    axes[2].set_ylabel('Sazonalidade')
    
    res.resid.plot(ax=axes[3], legend=False, color='gray')
    axes[3].set_ylabel('Ruído')
    
    fig.tight_layout()
    
    # Salvar figura
    fig.savefig(repoPath+'/figuras/'+uf+'/Decomposicao.png', bbox_inches='tight')
    
    return fig

# Chamada da função com os dados de vazão
uf = 'GO'  # Exemplo de Unidade Federativa
repoPath = r"C:\Users\Usuario\Documents\GitHub\ENS5132\trabalho01"
aqPath = r"C:\Users\Usuario\Documents\GitHub\ENS5132\trabalho01\outputs\GO\flow.csv"

# Lendo os dados de vazão
flow_data = pd.read_csv(aqPath)

# Certifique-se de que a coluna 'datetime' está no formato datetime
flow_data['datetime'] = pd.to_datetime(flow_data['datetime'])

# Chamar a função de decomposição
timeSeriesDecompose(flow_data, uf, repoPath)