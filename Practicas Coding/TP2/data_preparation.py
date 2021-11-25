import pandas as pd
from data_analysis import *


def set_dummy_variable(dataframe, column):
    """
    Given a dataframe create dummy variables for a specific column
    Replace the old column and add the new ones
    """
    dummy = pd.get_dummies(dataframe[column],prefix = column)

    pos = dataframe.columns.get_loc(column)
    listNomCol = list(dummy.columns)
    for i in range(len(dummy.columns)):
        df = dataframe.insert(pos + i, dummy.columns[i], dummy[dummy.columns[i]], True)
    del dataframe[column]
    print(dataframe.head())
    return df


def add_dummies(dataframe, columns):
    """
    Add dummy variables for every column given
    return the dataframe
    """
    pass


def main():
    # Program steps
    df = create_dataframe('insurance.csv')
    #df = add_dummies(df, ['sex', 'smoker', 'region'])
    #df.to_csv('insurance-ready.csv', index=False)
    set_dummy_variable(df, 'sex')
    """"
    set_dummy_variable(df, 'smoker')
    set_dummy_variable(df, 'region')
    """
    # visualize data
    # plot_scatter(df[['bmi']], df[['charges']], 'bmi', 'charges')
    # plt.show()


if __name__ == '__main__':
    main()
