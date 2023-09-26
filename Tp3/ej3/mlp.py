from mlp_utils import Dense
from activation_functions import Tanh

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