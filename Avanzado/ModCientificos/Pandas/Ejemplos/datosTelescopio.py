####################
# Obteniendo y gráficando con Pandas y matplotlib
######################

#Le ponemos un alias a pandas

import pandas as pd
import matplotlib.pyplot as plt

from pandas import DataFrame

lista_de_listas=[[1,2,3,4],
				[5,6,7,8],
				[9,10,11,12],
				[13,14,15,16]]

dataframe=DataFrame(lista_de_listas,index=['jorge','Luis','Julio','Gali'],columns=['uno','dos','tres','cuatro'])

dataframe.to_csv('sTelescopio.csv')
