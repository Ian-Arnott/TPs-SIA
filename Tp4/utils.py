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
    return data


def get_config_params(config):
    radio = config["radio"]
    validate_positive_int(radio, "Radio")

    return radio
