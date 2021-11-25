from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import plot_tree
from sklearn.metrics import mean_squared_error
import pandas as pd
import numpy as np

def main():
    dataset = pd.read_csv('Life_Expectancy.csv', delimiter=',')
    dataset = dataset.drop(['Columna_A_Borrar'], axis=1)
    dataset = dataset.dropna()

    print("\nDataset original: \n\n", dataset.head())

    X = dataset.drop('Life expectancy', axis=1)
    y = dataset[['Life expectancy']]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)

    '''modelo = DecisionTreeRegressor(random_state = 123) #Por default --> max_depthi: int, default=None. If None, then nodes are expanded until all leaves are.. 
                                                       #..pure or until all leaves contain less than min_samples_split samples.
    modelo.fit(X_train, y_train)

    fig, ax = plt.subplots(figsize=(12, 5))

    print("Profundidad del árbol: ", modelo.get_depth())
    print("Número de nodos terminales: ", modelo.get_n_leaves())

    plot = plot_tree(
                decision_tree = modelo,
                feature_names = dataset.drop(columns = "Life expectancy").columns,
                class_names   = 'Life expectancy',
                filled        = True,
                impurity      = False,
                fontsize      = 10,
                precision     = 2,
                ax            = ax
    )

    plt.show()'''

    # Seccion de Prueba para max-depth

    i = 1

    while (i <= 10):
        print("\n --------------- VUELTA N°", i, " ----------------\n")

        modelo = DecisionTreeRegressor(max_depth=i, random_state=123)
        modelo.fit(X_train, y_train)

        scoreEntrenamiento = modelo.score(X_train, y_train)
        scoreTest = modelo.score(X_test, y_test)

        print("\n> Score Entrenamiento = ", scoreEntrenamiento, "\n")
        print("> Score Test = ", scoreTest, "\n")

        i += 1

if __name__ == '__main__':
    main()