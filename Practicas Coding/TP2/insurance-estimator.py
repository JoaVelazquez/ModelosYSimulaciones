from data_analysis import *
from data_preparation import *
import statsmodels.api as sm
import operator
import numpy as np


def forward_stepwise_selection(dataframe, target):
    """
    Given a dataframe and a target variable
    implement the forward stepwise selection algorithm and return
    and array with all the r2 values
    """
    pass


def backward_stepwise_selection(dataframe, target):
    """
    Given a dataframe and a target variable
    implement the forward stepwise selection algorithm and return
    and array with all the r2 values
    """
    pass


def backward_stepwise_selection_pvalues(dataframe, target):
    """
    Given a dataframe and a target variable
    implement the forward stepwise selection algorithm with p values
    and return and array with all the r2 values
    """
    pass


def r2_variation(vars_size, r2_adj, title, x_label, y_label):
    """
    Plot the scatter and the curve that shows how R2 value vary over
    every iteration. A title and labels for the graph must be included.
    Also, highlight the point where there is a maximum R2 value. Add information
    about that point. The amount of independent variables is given.
    """
    pass


def create_model(r2_adj, var_model, dataframe, target, mode):
    """
    Creates a linear regression model with the variable/s that has
    the highest r2 value given by a selection stepwise algorithm
    """
    pass


def main():
    pass


if __name__ == '__main__':
    main()