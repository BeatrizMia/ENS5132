# -*- coding: utf-8 -*-
"""
Created on Sat May  3 11:27:51 2025

@author: Usuario
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats


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

# Filtrar NaN antes de aplicar log
flow_data = aqData['flow'].dropna()

def normalityCheck(flow_data, repoPath, uf):
    # Criando a figura com 3 subplots
    fig, ax = plt.subplots(3, figsize=(12, 9))

    # Log transformando os dados de vazão (fluxo)
    ax[0].hist(np.log(aqData['flow'].dropna()), facecolor='red')
    ax[0].set_title('Log')
    ax[0].set_xlabel('Vazão (log)')
    ax[0].set_ylabel('Frequência')

    # Box-Cox transformação
    flow_data = aqData['flow'].dropna()
    if (flow_data > 0).all():
        transformed_data, _ = stats.boxcox(flow_data)
        ax[1].hist(transformed_data, facecolor='green')
        ax[1].set_title('BoxCox')
        ax[1].set_xlabel('Vazão (Box-Cox)')
        ax[1].set_ylabel('Frequência')
    else:
        ax[1].hist(flow_data, facecolor='green')
        ax[1].set_title('BoxCox (Dados não podem ser transformados)')
        ax[1].set_xlabel('Vazão')
        ax[1].set_ylabel('Frequência')

    # Dados originais
    ax[2].hist(flow_data, facecolor='blue')
    ax[2].set_title('Dado original')
    ax[2].set_xlabel('Vazão')
    ax[2].set_ylabel('Frequência')

    # Ajusta o layout para não sobrepor os gráficos
    fig.tight_layout()

    # Salva o histograma gerado como uma imagem
    fig.savefig(repoPath + '/figuras/' + uf + '/histogramDataNormalization_' + 'flow' + '.png')
    
    return fig





