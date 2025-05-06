"""
primeira do trabalho 1 

Este script será utilizado para analisar os dados de qualidade do ar disponibi-
lizados pela plataforma do Instituto Energia e Meio Ambiente. 


     Abrir corretamente o dado
     Inserir coluna datetime 
     Criar coluna com estação do ano
     Filtrar dataframe
     Extrair estatísticas básicas
     Estatísticas por agrupamento
     Exportar estatísticas agrupadas
     Criar uma função para realizar as tarefas acima
     Criar função para gerar figuras 
     Loop para qualquer arquivo dentro da pasta
     Estatística univariada e bivariada – função exclusiva
     Análise de dados usando o statsmodel
"""
import pandas as pd
import numpy as np
import os

"uf = unidade federal"
def FlowMaxAnalysis(uf,repoPath):
       uf = 'GO'
       repoPath = r"C:\Users\Usuario\Documents\GitHub\ENS5132\trabalho01"
       dataDir = repoPath+'/'+'inputs'+'/'+uf
       dataList = os.listdir(dataDir)
       print(dataList)       
       
       # faz com que a operação de leitura de arquivo seja relativa a pasta dataDir.
       os.chdir(dataDir)
       # Criando lista vazia
       allFiles  =[]
       
       # Abrir os dados de vazão, objeto de estudo, em um dataframe
       # Função par apular linhas == skiprows=15 
      
       aqPath = r"C:\Users\Usuario\Documents\GitHub\ENS5132\trabalho01\inputs\GO\60665000_Vazoes.csv"
       
       aqData = pd.read_csv(aqPath, encoding='latin1', sep=';', engine='python', quotechar='"', skiprows=15)
      
       allFiles.append(aqData)
       
       # ignorando colunas desnecessárias, de horas (pq é = nam), coigo a bacia estatísticas
       
       # Lista com colunas por posição
       cols_position = list(aqData.columns[0:2]) + list(aqData.columns[3:16])

       # Lista com colunas por nome
       cols_name = list(aqData.loc[:, 'Vazao01Status':'Vazao31Status'].columns)

       # Junta tudo que eu quero excluir
       cols_drop = cols_position + cols_name

       # Remove coluna hora do DataFrame
       aqData.drop(columns = cols_drop, inplace=True)
        
       #A função pd.to_datetime transforma a strins de data em objetos datetime do pandas, permitindo que façamos operações com base na data e hora, como filtar, ordemar ou extrair partes específicas como ano, mes, dia 
       #quando esta escrito %d/%m/%Y  esta indicando para o pd como é o formado da data no arquivo, para ele conseguir converter corretamente
       datetimeDf = pd.to_datetime(aqData.Data, format='%d/%m/%Y')
       
       aqData['datetime'] = datetimeDf
       aqData= aqData.set_index(aqData['datetime'])
       
       #  Inserir indice datetime De Data---------------------------------------------------- 

       #criando outra variavel para preencher com os dados arrumados
       # Derrete as colunas de vazões diárias .A função melt trasforma linhas em colunas
       meltedDf = aqData.melt(id_vars=['datetime'], 
                       value_vars=[col for col in aqData.columns if 'Vazao' in col], 
                       var_name='day', 
                       value_name='flow')

       
       # Transformando a coluna de datetime em index, usando essa função vc passa a trabalhar com o indice sendo data/hora, o que facilita a filtragem por período
       #meltedDf= meltedDf.set_index(meltedDf['datetime'])

       # Extrai o número do dia (ex: 'Vazao01' → 1)
       meltedDf['day'] = meltedDf['day'].str.extract('(\d+)').astype(int)

       # Cria coluna com ano e mês da linha original
       meltedDf['year'] = meltedDf['datetime'].dt.year
       meltedDf['month'] = meltedDf['datetime'].dt.month

       # Cria coluna com a data completa
       meltedDf['Date'] = pd.to_datetime({'year': meltedDf['year'],
                                                  'month': meltedDf['month'],
                                                  'day': meltedDf['day']}, errors='coerce')

       # Remove datas inválidas (ex: 31 de fevereiro)
       meltedDf.dropna(subset=['Date'], inplace=True)

       # Organiza o resultado final
       #meltedDf = meltedDf[['Date', 'flow']]
       
       
       # Cria as colunas separadas
       meltedDf['year'] = meltedDf['Date'].dt.year
       meltedDf['month'] = meltedDf['Date'].dt.month
       meltedDf['day'] = meltedDf['Date'].dt.day

       # Ordena cronologicamente
       meltedDf.sort_values(by='Date', inplace=True)

       # Reorganiza as colunas (se quiser deixar bonitinho)
       meltedDf = meltedDf[['Date', 'year', 'month', 'day', 'flow']]
       
       #salvando aos editados 
       # criando pasta chamada outputs para salvar os dado, caso a pasta já exista o parâmetro exist_ok=true faz o codigo não gerar outra pasta 
       os.makedirs(repoPath+'/'+'outputs/'+uf,exist_ok=True)
     
       #Salvando em csv 
       meltedDf.to_csv(repoPath+'/'+'outputs/'+uf+'/'+'flowBica.csv')

      return  meltedDf
   
   

       
       
     
       
       