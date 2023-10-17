import numpy as np
import pandas as pd


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
    data = pd.read_csv('../data/europe.csv')
    countries = data["Country"].tolist()
    labels = data.columns[1:].tolist()
    country_data = data.iloc[:, 1:].values
    return countries, labels, country_data


def standarize_data(input_data):
    data_standarized = np.copy(input_data)  # Copia los datos para no modificar el original
    means = np.mean(data_standarized, axis=0)
    stdevs = np.std(data_standarized, axis=0)
    data_standarized = (data_standarized - means) / stdevs 
    return data_standarized


def get_config_params(config):
  
    learning_rate = config["learning_rate"]
    validate_percentage(learning_rate, "Learning rate")

    max_epochs = config["max_epochs"]
    validate_positive_int(max_epochs, "Max epochs")

    return learning_rate, max_epochs