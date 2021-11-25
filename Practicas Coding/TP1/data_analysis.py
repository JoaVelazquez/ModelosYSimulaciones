import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import mean_squared_error , r2_score
import numpy as np
from startup_prediction.py import create_dataframe, plot_scatter, plot_line

PARAMS = ['R&D Spend', 'Administration', 'Marketing Spend', 'State', 'Profit']
IND_VAR = ['R&D Spend']
DEP_VAR = ['Profit']

def train_model(dataframe):
    regr = linear_model.LinearRegression()
    ind_variable = dataframe[IND_VAR]
    dep_variable = dataframe[DEP_VAR]
    regr.fit(ind_variable, dep_variable)
    return regr

def betas(regr_model):
    beta_2 = regr_model.coef_[0][1]
    beta_1 = regr_model.coef_[0][0]
    beta_0 = regr_model.intercept_[0]
def mse(regr_model, dataframe):
    y_model = regr_model.predict(dataframe[IND_VAR])
    y_value = dataframe[DEP_VAR]
    y_values = np.transpose(y_value)
    mse = 0
    for i in range (0, y_values.size):
        mse += np.power(y_values[i] - y_model[i], 2)
    mse /= y_values.size
    return ms