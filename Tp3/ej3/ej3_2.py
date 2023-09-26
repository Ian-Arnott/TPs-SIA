import json
import numpy as np
from activation_functions import Tanh
from mse import mse, mse_derivative
from mlp import Dense, train, predict
from utils import get_config_params, get_data, get_training_amount, PERCEPTRON_TYPES
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

if __name__ == "__main__":
    with open('./config.json', 'r') as f:
        config = json.load(f)

    perceptron_type, learning_rate, training_percentage, max_epochs, bias, beta, epsilon = get_config_params(config)

    input_data, expected_data = get_data()
    training_amount = get_training_amount(len(input_data), training_percentage)

    training_set = input_data[:training_amount]
    training_expected = expected_data[:training_amount]
    testing_set =  np.reshape(input_data[training_amount:], (len(input_data)-training_amount, 5, 1))
    testing_expected = expected_data[training_amount:]
    X = np.reshape(training_set, (training_amount, 5, 1))
    Y = np.reshape(training_expected, (training_amount, 1, 1))
    print(X)
    print(Y)

    network = [
        Dense(5, 3),
        Tanh(),
        Dense(3, 1),
        Tanh()
    ]

        # train
    train(network, mse, mse_derivative, X, Y, epochs=10000, learning_rate=0.1)

    points = []
    for x in testing_set:
        for y in testing_expected:
            z = predict(network, [x])
            points.append([x, y, z[0,0]])
    for point in points:
        print(f"Input: {point[0]} Expected:{point[1]} Result:{point[2]}")
