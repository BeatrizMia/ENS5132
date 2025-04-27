# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 13:48:12 2025


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



@author: Leonardo.Hoinaski
"""

# Importação dos pacotes
import pandas as pd
import numpy as np
import os

# pandas: principal biblioteca para trabalhar com tabelas (DataFrame)
# numpy: fornece arrays e funções numéricas (útil para valores NaN, operações vetoriais…)
# os: interface com o sistema operacional (pastas, arquivos, caminho)

"uf = unidade federal"
#def cria funções, a abixo estamos criano uma função para tratar os aos antes da analise, essa função pode ser usar várias vezes.
#o nome da função é airQualityAnalysisd, 

def airQualityAnalysis(uf,repoPath):
    # -------------------------- Abrir os dados -----------------------------------
    # Criando variável com o nome do estado
    uf = 'ES'
    #associando uma variavel ao caminho os dados 
    repoPath = r"C:\Users\Usuario\Documents\GitHub\ENS5132\projeto01"
    # Definindo o caminho para a pasta de dados, aqui invertemos a barra !! já que não tem r'
    dataDir = repoPath+'/'+'inputs/'+uf
    
    # Lista de arquivos dentro do caminho indicado pelo dataDir, local pasta dados 
    dataList = os.listdir(dataDir)

    # faz com que a operação de leitura de arquivo seja relativa a pasta dataDir.
    os.chdir(dataDir)
    
    #variavel vazia para ser preenchida no for
    
    allFiles =[]
    
    # Loop nos arquivos na lista dataList, varialvel que listou os arquivos presentes em dataDir
    for fileInList in dataList:
        print(fileInList) #print para tornar visivel os arquivos listados no dataList
        dfConc = pd.read_csv(fileInList,encoding='latin1') #df=DataFrame= é uma estrutura de dados bidimensional semelhante a uma planilha do Excel, principal estruura de dados da biblioteca Pandas, conc=concatenar=unir. Essa finção esta lendo o arquivo CSV na codificação em latin, essa informão esta sendo guardada na variavel dfConc  
        allFiles.append(dfConc) # depois de lidos dos arquivos listados em dataList são sendo adicionados na variavel allFiles
    

#une tudos os aquivos listados num só DataFrame

# Concatenando meus DataFrames
    aqData = pd.concat(allFiles)
    
    # Caminho para um dos arquivos
   #aqPath = repoPath + uf + '\2015ES1.csv'
    
    # Abrir dados de apenas uma das estações de monitoramento de ES
   #aqData = pd.read_csv(aqPath, encoding='latin1')
    
    
    # ----------------------- Inserir coluna datetime------------------------------
    # a função pd.to_datetime transforma strins de data em objetos datetime do pandas, permitindo que se faça operações de data e hora, como filtar, ordemar ou extrair partes específicas como ano, mes, dia 
    datetimeDf = pd.to_datetime(aqData.Data, format='%Y-%m-%d') #quando esta escrito %Y-%m-%d  esta indicando para o pd como é o formado da data no arquivo, para ele conseguir converter corretamente 
    
    # Criando coluna datetime dentro de aqData usando o objeto tempo dos arquivos 
    aqData['datetime'] = datetimeDf
    
    # Transformando a coluna de datetime em index, usando essa função vc passa a trabalhar com o indice sendo data/hora, o que facilita a filtragem por período
    aqData = aqData.set_index(aqData['datetime'])
    # como a data não é uma string mais podemos separa extaraindo o o ano , month e o dia  dos dados, pois eles são indices
    aqData['year'] = aqData.index.year
    aqData['month'] = aqData.index.month
    aqData['day'] = aqData.index.day
    
    # Extraindo a hora, aqui estamos criando uma variavel para extrair as horas do aqData, lembre que hora é uma string separada por :, logo o primeiro passo é criar uma nova lista que empilhe as a string horas tirando os : = aqData.Hora.str.split(':')
    horas  = aqData.Hora.str.split(':')
    #aqui vamos fazer a mesma coisa do anterior, loop das horas das varivel horas que são adicionadas á lista horaDf atraves da função append
   
    horaDf = []
    for hora in horas:
        #print(hora[0])
        horaDf.append(hora[0]) #perceba que quando colocamos hora[0]estamos pegando para ser adicionado á lista apenas a parte que fica antes dos dois pontos, as horas sem os min
    
    aqData['hour'] = horaDf # aqui estamos adicionando mais uma coluna chamada hour  e preenchendo essa coluna com os valoes de horaDf
    
    #juntando as colunas da data e formando um indice 
    # até o momento criamos 4 colunas diferentes, year, month, day, hour, mas o pd não endente que os dados de cada coluna na vdd correspondem a uma data completa, por isso vamos crior outra colona datetime e para preencher ela vamos usar o a função pd.to_datetime comolocando dentro a coluna do proprio aqData 'year, month, day, hour', assim essas partes separadas da data viram um indice de data e hora no formato '%Y%m%d %H
    aqData['datetime'] = pd.to_datetime(
        aqData[['year', 'month','day','hour']],format='%Y%m%d %H')
    
    # definindo datetime como um index da dataframe datetime
    aqData = aqData.set_index(aqData['datetime'])
    
    
    # ------------------------Estação do ano---------------------------------------
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
    
    
    # ---------------------Estatísticas básicas ----------------------------------
    # Extrair o nome dos poluentes presentes no dado, essa função pega todos os dados unicos da uma coluna, removendo as duplicações, e como estamos associando essa função a uma variavel, 
    # o que irá acontecer é que fazemos uma listas dos puluentes analisados nos dados
    pollutants = np.unique(aqData.Poluente)
    
    # a msm coisa esta acontecendo aqui estraindo os nomes das estacões atraves da função que remove duplicações e guardaremos em uma varialvel lista o nome as estação
    stations = np.unique(aqData.Estacao)
    
    # criando pasta para salvar os dado, caso a pasta já exista o parâmetro exist_ok=true faz o codigo não gerar outra pasta 
    os.makedirs(repoPath+'/'+'outputs/'+uf,exist_ok=True)
    
    # Esse Loop vai de estação em estação imprime a nome e cria uma variavel vazia para ser preenchida pelos dados  a cada loop
    for st in stations:
         print(st)
         statAll =[] #dentro de cada estaçao estamos criando um outro loop que vai de poluete em poluente, cria uma nova variavel associano o valor o poluente, com o poluente com a estação analisada & fazendo estatisticas descritivas (como média, desvio padrão, mínimo, máximo, etc.) das colunas numéricas de um DataFramo aqData. 
         for pol in pollutants:
             print(pol)
             basicStat = aqData['Valor'][(aqData.Poluente==pol) & 
                                        (aqData.Estacao==st)].describe()
             basicStat = pd.DataFrame(basicStat) # linha reunantes
             basicStat.columns =[pol] #renomeano a nome a coluna para o nome o poluente analisado
             statAll.append(basicStat)  # o resultado a correção é aicionado à variavel vazia StatAll     
        
    # Unindo as estatísticas por poluente
         dfmerge = pd.concat(statAll,axis=1)
        
    # Salva as estatísticas por estação    
    dfmerge.to_csv(r'C:\Users\Usuario\Documents\GitHub\ENS5132\projeto01\outputs'+'/'+uf+'/'+'basicStat.csv')
    
    # Salvando aqData
    aqData.to_csv(r'C:\Users\Usuario\Documents\GitHub\ENS5132\projeto01\outputs'+'/'+uf+'/'+'Data.csv')
   
    # Estatística básica usando groupby
    statGroup = aqData.groupby(['Estacao','Poluente']).describe()
    
    # Salvando em csv caa escação como Data 
    
    statGroup.to_csv(r'C:\Users\Usuario\Documents\GitHub\ENS5132\projeto01\outputs'+'/'+uf+'/'+'basicStat_ALL.csv')
    
    # Coloca o índice da matriz como a coluna datetime
    aqData = aqData.set_index(pd.DatetimeIndex(aqData['datetime']))
    
    # Criando uma tabela de dados com cada poluente em colunas diferentes.
    aqTable = aqData.reset_index(drop=True).pivot_table(
        columns='Poluente',
        index=['Estacao','datetime'],
        values='Valor')

    return aqData, stations, aqTable
    