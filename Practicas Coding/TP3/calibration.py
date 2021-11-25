from data_analysis import *
import statsmodels.api as sm
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
import numpy as np

"""
Reference:	Chwirut, D., NIST (1979). 
Ultrasonic Reference Block Study.
"""


def train_model(dep_variables, target, mode, degree=1):

    var_explicativas = dep_variables
    var_objetivo = target

    if mode == 'p':

        polynomial_features = PolynomialFeatures(degree=degree)
        xp = polynomial_features.fit_transform(var_explicativas)

        model = sm.OLS(var_objetivo, xp)
        regr = model.fit()

        pred = regr.predict(xp)
        plt.plot(var_explicativas,pred,color='red')
        plt.xlabel('Metal Distance')
        plt.ylabel('Ultrasonic Response')
        plt.show()
    elif mode == 'l':

        x_log = np.log10(var_explicativas)
        y_log = np.log10(var_objetivo)

        x_log = sm.add_constant(x_log)
        model = sm.OLS(y_log, x_log)
        regr = model.fit()

    return regr


def plot_solution(model, dataframe ):
    return True


def is_calibrated(x, y, regr, mode, degree=1):

    if mode=='p':
        ajuste = "polinomico"
        prediccion = regr.predict( PolynomialFeatures(degree=degree).fit_transform([[x]]) )

    elif mode=='l':

        ajuste = "logaritmico"
        beta_0 = regr.params[0]
        beta_1 = regr.params[1]

        a = np.power(10, beta_0)
        prediccion= a*np.power(x, beta_1)
        #prediccion = regr.predict(sm.add_constant(np.log10([[x]])))


    if ( (prediccion < (y * 1.05)) and (prediccion > (y * 0.95)) ):
        print("--Usando ajuste ",ajuste)
        print("\nEsta calibrado! Valor predecido: ", prediccion, " - Valor 'y': ", y)
        return True
    else:
        print("--Usando ajuste ", ajuste)
        print("\nNo esta calibrado! Valor predecido: ", prediccion, " - Valor 'y': ", y)
        return False

def main():
    # this should work
    df = create_dataframe('Chwirut1.csv')

    # polinomial of degree 2
    print(train_model(df[['metal_distance']], df[['ultrasonic_response']], 'p', 2).summary())
    modeloPolinomicoGrad2 = train_model(df[['metal_distance']], df[['ultrasonic_response']], 'p', 2)

    # polinomial of degree 3
    print(train_model(df[['metal_distance']], df[['ultrasonic_response']], 'p', 3).summary())
    modeloPolinomicoGrad3 = train_model(df[['metal_distance']], df[['ultrasonic_response']], 'p', 3)

    # logarithmic
    print(train_model(df[['metal_distance']], df[['ultrasonic_response']], 'l').summary())
    modeloLogaritmico = train_model(df[['metal_distance']], df[['ultrasonic_response']], 'l')

    # the program
    print('press 0 to stop, 1 to continue')
    i = 1
    while i:
        print('Metal distance')
        x = float(input())
        print('Ultrasonic Value')
        y = float(input())
        is_calibrated(x, y, modeloLogaritmico, 'l',1)
        print('Continue?')
        i = int(input())


if __name__ == '__main__':
    main()