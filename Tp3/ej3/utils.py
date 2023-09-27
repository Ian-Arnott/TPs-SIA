import numpy as np
import pandas as pd


OPTIMIZER_TYPES = ["ADAM"]

def validate_optimizer_type(value, types, str):
    if value not in types:
        print(f"Invalid {str} optimizer type")
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


def get_data(ej):
    with open('../data/ej3-digitos.txt', 'r') as file:
        lines = file.readlines()

    input_data = []
    expected_data = []
    if (ej == 2):
        for i in range(10):
            aux = []
            for j in range(7):
                binary_digits = list(map(int, lines[7*i+j].strip().split()))
                aux.append(binary_digits)
            input_data.append(aux)
            expected_data.append(i % 2)
    if (ej == 3):
        for i in range(10):
            aux = []
            for j in range(7):
                binary_digits = list(map(int, lines[7*i+j].strip().split()))
                aux.append(binary_digits)
            input_data.append(aux)
            expected_data.append(i)
    return input_data, expected_data


def get_training_amount(total, percentage):
    return int(total * percentage)


def get_config_params(config):
    ej = config["ej"]

    learning_rate = config["learning_rate"]
    validate_percentage(learning_rate, "learning_rate")

    training_percentage = config["training_percentage"]
    validate_percentage(training_percentage, "training_percentage")

    max_epochs = config["max_epochs"]
    validate_positive_int(max_epochs, "max_epochs")

    bias = config["bias"]
    validate_positive_int(bias, "bias")

    beta = config["beta"]
    validate_positive_int(beta, "beta")

    epsilon = config["epsilon"]

    optimizer = config["optimizer"]
    validate_optimizer_type(optimizer, OPTIMIZER_TYPES, "optimizer")

    return ej, learning_rate, training_percentage, max_epochs, bias, beta, epsilon, optimizer

