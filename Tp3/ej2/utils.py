import numpy as np
import pandas as pd

PERCEPTRON_TYPES = ["LINEAR", "HIPERBOLIC", "LOGISTIC"]

def validate_perceptron_type(value, types, str):
    if value not in types:
        print(f"Invalid {str} perceptron type")
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
    data = pd.read_csv('../data/ej2-conjunto.csv')
    input_data = np.array(data[['x1', 'x2', 'x3']])
    expected_data = np.array(data['y'])
    return input_data, expected_data


def get_training_amount(total, percentage):
    return int(total * percentage)


def get_config_params(config):
    perceptron_type = config["perceptron_type"]
    validate_perceptron_type(perceptron_type, PERCEPTRON_TYPES, "perceptron_type")

    learning_rate = config["learning_rate"]
    validate_percentage(learning_rate, "learning_rate")

    training_percentage = config["training_percentage"]
    validate_percentage(training_percentage, "training_percentage")

    max_epochs = config["max_epochs"]
    validate_positive_int(max_epochs, "max_epochs")

    bias = config["bias"]
    validate_positive_int(bias, "bias")

    beta = config["beta"]

    epsilon = config["epsilon"]

    return perceptron_type, learning_rate, training_percentage, max_epochs, bias, beta, epsilon

