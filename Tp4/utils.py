import numpy as np
import pandas as pd

PERCEPTRON_TYPES = ["LINEAR", "HIPERBOLIC", "LOGISTIC"]

def validate_perceptron_type(value, types, str):
    if value not in types:
        print(f"Invalid {str}")
        exit(1)


def validate_percentage(value, str):
    try:
        value = float(value)
        if value <= 0 or value > 1:
            raise ValueError
    except ValueError:
        print(f"{str} must be a positive float between 0 and 1")
        exit(1)


def validate_positive_int(value, str):
    try:
        value = int(value)
        if value <= 0:
            raise ValueError
    except ValueError:
        print(f"{str} must be a positive integer")
        exit(1)


def get_data():
    data = pd.read_csv('data/europe.csv')
    countries = data["Country"].tolist()
    labels = data.columns[1:].tolist()
    country_data = data.iloc[:, 1:].values
    return countries, labels, country_data

# Unit Length Scaling => X / ||X||
def standarize_data(data):
    norms = np.linalg.norm(data, axis=1) # Calcula la norma Euclidiana de cada fila (la longitud)
    return data / norms[:, np.newaxis]


def get_config_params(config):
    radius = config["radius"]
    validate_positive_int(radius, "Radius")

    max_epochs = config["max_epochs"]
    validate_positive_int(max_epochs, "Max epochs")

    return radius, max_epochs
