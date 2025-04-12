import numpy as np

import pandas as pd 

import matplotlib.pyplot as plt

import os

# Trabalhando com dado real
# Criando variável com o nome do estado
uf = 'SP'

# Definindo o caminho para a pasta de dados
dataDir = r"C:\Users\Usuario\Documents\GitHub\ENS5132\data" +'/'+ uf

# Lista de arquivos dentro da pasta dataDir
dataList = os.listdir(dataDir)

# Movendo para a pasta de dados/uf
os.chdir(dataDir)

allFiles =[]
# Loop na lista dataList 
for fileInList in dataList:
    print(fileInList)
    dfConc = pd.read_csv(fileInList,encoding='latin1')
    allFiles.append(dfConc)
    print(allFiles.append(dfConc))
    
# Concatenando meus DataFrames
allFiles = pd.concat(allFiles)

# Extraindo nomes das estações sem redundância
stations = pd.unique(allFiles['Estacao'])

print(stations)


# Cria uma pasta para os arquivos, se ainda não existir
os.makedirs('estacoes', exist_ok=True)

for estacao in stations:
    # Filtra os dados da estação atual
    df_estacao = allFiles[allFiles['Estacao'] == estacao]

    # Usa o nome da estação como nome de arquivo, com ajustes mínimos
    nome_arquivo = estacao.replace('/', '-') + '.csv'

    # Caminho completo do arquivo
    caminho_arquivo = os.path.join('estacoes', nome_arquivo)

    # Salva o arquivo CSV
    df_estacao.to_csv(caminho_arquivo, index=False, encoding='utf-8')
