####################
# Data Frames
#####################

from pandas import DataFrame,Series

lista_de_listas=[[1,2,3,4],
				[5,6,7,8],
				[9,10,11,12],
				[13,14,15,16]]

dataframe = DataFrame(lista_de_listas,columns=['uno','dos','tres','cuatro'])
print(dataframe)

#Tambien podemos modificar los indices
dataframe=DataFrame(lista_de_listas,index=['jorge','Luis','Julio','Gali'],columns=['uno','dos','tres','cuatro'])

print(dataframe)

#Ahora pasaremos una serie a un dataframe

dicc_series={'Uno':Series([1,2,3],index=['a','b','c']),
			'Dos':Series([1,2,3,4],index=['a','b','c','d'])
			
}

dataframe = DataFrame(dicc_series)
print(dataframe)
