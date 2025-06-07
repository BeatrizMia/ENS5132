import pandas as pd
import numpy as np
import xarray as xr
import netCDF as 
import os
import geopandas as gpd
from shapely.geometry import Point
import pandas as pd
import matplotlib.pyplot as plt
import folium
import contextily as cx
import rasterio as rio

# Diretório do arquivo
repoPath = r"C:\Users\Usuario\Documents\GitHub\ENS5132\trabalho02"
dataDir = repoPath+'/'+'inputs'+'/'+'FINN15_2020_MOZ_05272021.txt'    

# lendo o arquivo CSV com pandas
Ld = pd.read_csv(dataDir, sep=",", header=0, skipinitialspace=True)

# Ordenando o arquivo em ordem crescente dos dias
Ld = Ld.sort_values(by='DAY')

# Vendo o primeiro e ultimo dia
print("Primeiro DAY:", Ld['DAY'].iloc[0])
print("Último  DAY:", Ld['DAY'].iloc[-1]) 

# Recortando variaveis que serão avaliadas CO, CO2, CH4, N2O
Ld_poluentes = Ld[['DAY','TIME','LATI','LONGI','AREA','CO', 'CO2', 'CH4', 'NO2', 'BC']]

# Transformando para geopandas
gdff = gpd.GeoDataFrame(Ld_poluentes,
                       geometry=gpd.points_from_xy(
                                Ld_poluentes.LONGI, Ld_poluentes.LATI), 
                             crs="EPSG:4326" ) 

# Plotando na figura
fig, ax = plt.subplots()
geoMun.boundary.plot(ax=ax,color='gray', linewidth = 0.2)
gdf.plot(ax=ax)
