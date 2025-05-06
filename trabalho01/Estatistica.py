# -*- coding: utf-8 -*-
"""
Created on Sat May  3 15:36:05 2025

@author: Usuario
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


uf= 'GO'
repoPath = r"C:\Users\Usuario\Documents\GitHub\ENS5132\trabalho01"
aqPath = r"C:\Users\Usuario\Documents\GitHub\ENS5132\trabalho01\outputs\GO\flowBica.csv"

#lendo o arquivo 
aqData = pd.read_csv(aqPath)

# Substituir vírgulas por pontos na coluna 'flow'
aqData['flow'] = aqData['flow'].str.replace(',', '.', regex=False)

aqData['flow'] = aqData['flow'].str.replace(' ', '')  # Remover espaços, se houver


# Garantir que a coluna 'flow' tenha apenas valores numéricos
aqData['flow'] = pd.to_numeric(aqData['flow'], errors='coerce')

# Filtrar NaN antes de aplicar log
aqData['flow'] = aqData['flow'].dropna()

 # Criando uma coluna chamada Seanson e preenchendo todos os valores com NaN 
 aqData['Season'] = np.nan
 #Aqui a baixo vamos preencher com qual estação do cada mes de analise coresponde 
 # como data é um inidce podemos preencher a coluna da estaçao com base nos valores dos meses, usano a lógica boleeana 
 aqData['Season'][(aqData.month==1) | (aqData.month==12) | 
                   (aqData.month==2) ] = 'Verão'
 # Outono
 aqData['Season'][(aqData.month==3) | (aqData.month==5) | 
                   (aqData.month==4) ] = 'Outono'
 # Inverno
 aqData['Season'][(aqData.month==6) | (aqData.month==7) | 
                   (aqData.month==8) ] = 'Inverno'
 # Primavera
 aqData['Season'][(aqData.month==9) | (aqData.month==10) | 
                   (aqData.month==11) ] = 'Primavera'

# ----------------------------------------------------------------------------------------
# Calcular as estatísticas de vazão por estação
season_stats = aqData.groupby('Season')['flow'].describe().round(3)

# Calcular as estatísticas de vazão para todos os anos
flowData= aqData['flow'].describe().round(3)

# Adicionar uma linha para os dados de todos os anos na tabela de estações
flowData.name = 'Vazão'
eason_stats = pd.concat([season_stats, flowData.to_frame().T])

# Gerando a figura com a tabela
fig, ax = plt.subplots(figsize=(10, 6))  # Tamanho da figura
ax.axis('tight')  # Para ajustar o layout da tabela
ax.axis('off')  # Para desativar os eixos

# Gerando a tabela
ax.table(cellText=season_stats.values,
         colLabels=season_stats.columns,
         rowLabels=season_stats.index,
         cellLoc='center', loc='center')

 # Ajusta o layout para não sobrepor os gráficos
 fig.tight_layout()

plt.show()
# Salvar a tabela como uma figura
 fig.savefig(repoPath+'/figuras/'+uf+'/'+'EstatisticaBasicaBica_table.png', bbox_inches='tight')


return aqData, stations, aqTable


