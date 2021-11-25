import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
#Convertimos a dummies las variables cualitativas _prop
#Comenzamos por barrio



def dummy_maker(data_frame,nombre):
    variable = pd.factorize(data_frame[nombre])
    print('\n> Conversion de variable "',nombre,'"', variable, '\n')
    index_variable = data_frame.columns.get_loc(nombre)
    data_frame = data_frame.drop(nombre, axis=1)
    data_frame.insert(index_variable, nombre, variable[0])
    return data_frame

def train_model(df_var_explicativa, df_var_objetivo):
    rlog = LogisticRegression().fit(X_train,y_train.values.ravel())
    return modelo

def main():
    data_frame = pd.read_csv('mark_banco.csv',delimiter=';')
    print(data_frame.head())

    lista_index = ['job','marital','education','default','housing','loan','contact',
                  'month','day_of_week','poutcome']

    #Creo las dummies
    for n in range(len(lista_index)):
        data_frame = dummy_maker(data_frame,lista_index[n])
    print(data_frame.head())

    #Entreno el modelo con todas las variables menos la obj ('y')
    """i = 0
    while(i != (len(lista_index)-1)):

        modelo_aux = train_model(data_frame[lista_index[i]],data_frame['y'])
        prediccion = modelo_aux.predict(data_frame)
        print('\n>Usando la variable ', lista_index[i], 'el modelo de regresion lineal'
                                                  ' simple predijo un "y" de : ', prediccion, '\n')
        i+=1
    """
    target_variable = 'y'
    y = data_frame[[target_variable]]
    X = data_frame.drop(target_variable, axis=1)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print(y)
    print(X)

if __name__ == '__main__':
    main()
