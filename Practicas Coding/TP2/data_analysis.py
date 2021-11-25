import pandas as pd
import matplotlib.pyplot as plt


def create_dataframe(filename):
    """
    Given a filename in csv format
    create a panda dataframe and return it
    """
    df = pd.read_csv(filename)
    return df


def plot_scatter(x, y, x_label, y_label):
    """
    Plot a scatter of (x, y) points
    given as a parameter
    """
    plt.scatter(x, y)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

def plot_line(x, y):
    """
    Plot a line from (x, y) points
    given as a parameter
    """
    plt.plot(x, y)
    plt.show()

def main():
    #For testing purposes, to analyze the data
    df = create_dataframe('insurance.csv')
    print(df.head())


if __name__ == '__main__':
    main()
