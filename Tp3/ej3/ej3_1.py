from mlp import Dense, train, predict
from activation_functions import Tanh
from mse import mse, mse_derivative
from utils import get_config_params
import json
import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":

    with open('./config.json', 'r') as f:
        config = json.load(f)

    ej, learning_rate, training_percentage, max_epochs, bias, beta, epsilon, optimizer = get_config_params(config)


    X = np.reshape([[0, 0], [0, 1], [1, 0], [1, 1]], (4, 2, 1))
    Y = np.reshape([[0], [1], [1], [0]], (4, 1, 1))

    network = [
        Dense(2, 3, learning_rate, optimizer),
        Tanh(),
        Dense(3, 1, learning_rate, optimizer),
        Tanh()
    ]

    # train
    train(network, mse, mse_derivative, X, Y, max_epochs)

    # decision boundary plot
    points = []
    for x in np.linspace(0, 1, 20):
        for y in np.linspace(0, 1, 20):
            z = predict(network, [[x], [y]])
            points.append([x, y, z[0,0]])

    points = np.array(points)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.scatter(points[:, 0], points[:, 1], points[:, 2], c=points[:, 2], cmap="winter")
    plt.show()