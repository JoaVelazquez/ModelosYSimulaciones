import pandas as pd
from sklearn import linear_model

def train_model( data_frame_var_explicativa, data_frame_var_objetivo):
    regr = linear_model.LinearRegression()
    modelo=regr.fit(data_frame_var_explicativa, data_frame_var_objetivo)
    return modelo

def main():

    data_frame = pd.read_csv('propiedades.csv') #Cargo el dataset

    print(data_frame.head()) #Muestro el dataset

    #Convertimos a dummies las variables cualitativas _prop
    #Comenzamos por barrio
    barrio = pd.factorize(data_frame['barrio'])
    print('\n> Conversion de variable barrio: ', barrio, '\n')
    index_barrio = data_frame.columns.get_loc('barrio')
    data_frame = data_frame.drop('barrio', axis=1)
    data_frame.insert(index_barrio, 'barrio', barrio[0])

    print('\n>Dataset modificado: \n')
    print(data_frame.head())

    #Seguimos con las tipo_prop
    tipo_prop = pd.factorize(data_frame['tipo_prop'])
    print('\n> Conversion de variable tipo_prop: ', tipo_prop, '\n')
    index_tipo_prop = data_frame.columns.get_loc('tipo_prop')
    data_frame = data_frame.drop('tipo_prop', axis=1)
    data_frame.insert(index_tipo_prop, 'tipo_prop',tipo_prop[0])

    print('\n>Dataset modificado: \n')
    print(data_frame.head())

    #Filtramos el dataset por los valores del enunciado
    # (50.000 < precio  800.000 )
    data_frame_filt = data_frame[(data_frame['precio'] > 50000) & (data_frame['precio'] < 800000)]
    print(data_frame_filt.head())

    #Creo un ciclo que entrene un modelo por cada variable
    list_variables = ['cant_amb','cant_banos', 'sup_total','sup_cub']
    for variable in list_variables:
        modelo_aux = train_model(data_frame_filt[variable],data_frame_filt['precio'])
        prediccion = modelo_aux.predict(data_frame_filt)
        print('\n>Usando la variable ',variable, 'el modelo de regresion lineal'
                                                 ' simple predijo un precio de : USD$',prediccion, '\n'

if __name__ == '__main__':
    main()
