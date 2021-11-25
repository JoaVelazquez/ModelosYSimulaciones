import pandas as pd

"""
Completar las funciones señaladas con la logica
correspondiente segun conceptos vistos en clase 0. 
No modificar la constante SRC. Todas las funciones
se resuelven en una o dos lineas de codigo
"""
SRC = {"Name":
           ["Geoffrey Hinton",
            "Michael I Jordan",
            "Andrew Ng",
            "Yann LeCun",
            "Yoshua Bengio"],
       "Age": [73, 65, 45, 61, 57],
       "Country":
           ["UK", "US", "UK", "FR", "FR"]}


def set_dataframe(source):
    """
    From the SRC constant, create a panda data frame
    and return it. This will be a useful helper function
    """
    data_frame = pd.DataFrame(source)
    return data_frame


def average_age(data_frame):
    """
    Given a data frame, get the average
    age of all of the names in list
    >>> average_age( set_dataframe(SRC) )
    60.2
    """
    column_age = data_frame["Age"]
    sum_ages = sum(column_age)
    avg_age = sum_ages/len(column_age)
    return avg_age


def people_from(a_country, data_frame):
    """
    Given a data frame, get all the people
    from a given country
    """
    people = data_frame.loc[data_frame["Country"] == a_country]
    return people

if __name__ == '__main__':
    data = set_dataframe(SRC)
    print(data)
    print("Average Age:", average_age(data))
