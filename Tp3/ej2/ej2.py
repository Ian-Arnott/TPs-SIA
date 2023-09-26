import json
import numpy as np
from activation_functions import Tanh, Linear
from mse import mse, mse_derivative
from mlp import Dense, train, predict
from utils import get_config_params, get_data, get_training_amount, PERCEPTRON_TYPES
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from perceptron_utils import initialize_perceptron, calculate_accuracy, min_max_interval

if __name__ == "__main__":
    with open('./config.json', 'r') as f:
        config = json.load(f)

    perceptron_type, learning_rate, training_percentage, max_epochs, bias, beta, epsilon = get_config_params(config)

    input_data, expected_data = get_data()
    training_amount = get_training_amount(len(input_data), training_percentage)


    training_set = input_data[:training_amount]
    perceptron = initialize_perceptron(perceptron_type, beta, learning_rate, bias, len(training_set[0]),epsilon)
    expected_data = [perceptron.scale_result(value,min(expected_data),max(expected_data)) for value in expected_data]
    print(expected_data)
    training_expected = expected_data[:training_amount]
    testing_set =  np.reshape(input_data[training_amount:], (len(input_data)-training_amount, 3, 1))
    testing_expected = expected_data[training_amount:]

    X = np.reshape(training_set, (training_amount, 3, 1))
    Y = np.reshape(training_expected, (training_amount, 1, 1))
    print(X)
    print(Y)

    network = [
        Dense(3, 1),
        Tanh()
    ]

        # train
    train(network, mse, mse_derivative, X, Y, epochs=10000, learning_rate=0.1)

    points = []
    for i in range(len(testing_set)):
        z = predict(network, testing_set[i])
        points.append([testing_set[i], testing_expected[i], z[0,0]])
    for point in points:
        print(f"Input: {point[0]} Expected:{point[1]} Result:{(point[2])}")
