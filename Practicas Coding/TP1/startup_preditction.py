import pandas as pd
import matplotlib.pyplot as plt

def create_dataframe( filename ):
    """"
    tiene que tomar un arch .csv y devolver el dataframe
    """
    df = pd.read_csv(filename)
    return df
def plot_scatter( x, y, x_label, y_label ):
    plt.scatter(x,y)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
def plot_line( x, y ):
    plt.plot(x,y)
    plt.show()

def main():
