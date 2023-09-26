from multi_layer_perceptron import Dense
from activation_functions import Tanh
from mse import mse, mse_derivative
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def predict(network, input):
    output = input
    for layer in network:
        output = layer.forward(output)
    return output

def train(network, error_function, error_derivative, x_train, y_train, epochs = 1000, learning_rate = 0.01, verbose = True):
    for e in range(epochs):
        error = 0
        for x, y in zip(x_train, y_train):
            # forward
            output = predict(network, x)

            # error
            error += error_function(y, output)

            # backward
            grad = error_derivative(y, output)
            for layer in reversed(network):
                grad = layer.backward(grad, learning_rate)

        error /= len(x_train)
        if verbose:
            print(f"{e + 1}/{epochs}, error={error}")

if __name__ == "__main__":

    X = np.reshape([[0, 0], [0, 1], [1, 0], [1, 1]], (4, 2, 1))
    Y = np.reshape([[0], [1], [1], [0]], (4, 1, 1))

    print(X)
    print(Y)

    network = [
        Dense(2, 3),
        Tanh(),
        Dense(3, 1),
        Tanh()
    ]

    # train
    train(network, mse, mse_derivative, X, Y, epochs=10000, learning_rate=0.1)

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