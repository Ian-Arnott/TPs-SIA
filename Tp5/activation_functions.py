import numpy as np
from mlp import Activation

class Tanh(Activation):
    def __init__(self):
        tanh = lambda x: np.tanh(x)
        tanh_derivative = lambda x: 1 - np.tanh(x) ** 2
        super().__init__(tanh, tanh_derivative)

class Mish(Activation):
    def __init__(self):
        mish = lambda x: x * np.tanh(x)
        mish_derivative = lambda x: np.tanh(x) + x * (1 / np.cosh(x))**2
        super().__init__(mish, mish_derivative)

class Sigmoid(Activation):
    def __init__(self):
        def sigmoid(x):
            return 1 / (1 + np.exp(-x))

        def sigmoid_derivative(x):
            s = sigmoid(x)
            return s * (1 - s)

        super().__init__(sigmoid, sigmoid_derivative)

class Linear(Activation):
    def __init__(self):
        def linear(x):
            return x

        def linear_derivative(x):
            return 1

        super().__init__(linear, linear_derivative)