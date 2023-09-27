import json
import numpy as np
from activation_functions import Tanh, Linear, Sigmoid
from mse import mse, mse_derivative
from mlp import Dense, train, predict
from utils import get_config_params, get_data, get_training_amount
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

if __name__ == "__main__":
    with open('./config.json', 'r') as f:
        config = json.load(f)

    ej, learning_rate, training_percentage, max_epochs, bias, beta, epsilon = get_config_params(config)

    input_data, expected_data = get_data(ej)
    flattened_input = []
    for i in range(len(input_data)):
        flattened_input.append([item for sublist in input_data[i] for item in sublist])
    max_expected = max(expected_data)
    scaled_expected = [(2 * x / max_expected) - 1 for x in expected_data]
    X = np.reshape(input_data, (10, 35, 1))
    Y = np.reshape(scaled_expected, (10, 1, 1))
    print(X)
    print(Y)

    network = [
        Dense(35, 36),
        Tanh(),
        Dense(36, 10),
        Tanh()
    ]

        # train
    train(network, mse, mse_derivative, X, Y, epochs=1000, learning_rate=0.01)

    points = []
    for i in range(len(X)):
        z = predict(network, X[i])
        points.append([X[i], Y[i], z[0,0]])
    for point in points:
        print(f"Input: {point[0]} Expected:{point[1]} Result:{(point[2])}")
