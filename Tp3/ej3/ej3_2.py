import json
import numpy as np
from activation_functions import Tanh
from mse import mse, mse_derivative
from mlp import Dense, train, predict
from utils import get_config_params, get_data, get_training_amount

if __name__ == "__main__":
    with open('./config.json', 'r') as f:
        config = json.load(f)

    ej, learning_rate, training_percentage, max_epochs, bias, beta, epsilon, optimizer = get_config_params(config)

    input_data, expected_data = get_data(ej)
    training_amount = get_training_amount(len(input_data), training_percentage)

    flattened_input = []

    for i in range(len(input_data)):
        flattened_input.append([item for sublist in input_data[i] for item in sublist])

    training_set = flattened_input[:training_amount]
    training_expected = expected_data[:training_amount]

    testing_set =  np.reshape(flattened_input[training_amount:], (len(input_data)-training_amount, 35, 1))
    testing_expected = expected_data[training_amount:]

    X = np.reshape(training_set, (training_amount, 35, 1))
    Y = np.reshape(training_expected, (training_amount, 1, 1))

    # print(X)
    # print(Y)

    network = [
        Dense(35, 32, learning_rate, optimizer),
        Tanh(),
        Dense(32, 2, learning_rate, optimizer),
        Tanh()
    ]

    # train
    train(network, mse, mse_derivative, X, Y, epochs=max_epochs, verbose=False)

    points = []
    for i in range(len(testing_set)):
        z = predict(network, testing_set[i])
        points.append([testing_set[i], testing_expected[i], z[0,0]])
    for point in points:
        print(f"Expected:{point[1]} Result:{round(point[2])}")
