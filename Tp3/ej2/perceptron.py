import numpy as np
import matplotlib.pyplot as plt
import random
import math
from abc import ABC, abstractmethod


class SimplePerceptron(ABC):
    def __init__(self, learning_rate:float, weights, bias:float, input_data_dim:int):
        if(weights is None or len(weights) == 0):
            if(input_data_dim is None):
                raise Exception("No input_data_dim provided")
            self.weights = np.random.rand(input_data_dim + 1) # Tiene en cuenta w_0
        else:
            self.weights = weights
        
        self.learning_rate = learning_rate
        self.bias = bias


    @abstractmethod
    def activation_function(self, x:float) -> float:
        pass

    @abstractmethod
    def activation_derivative(self, x:float) -> float:
        pass

    def compute_error(self, input_data:list[list[float]], expected:list[float]):

        outputs:list[float] = self.current_outputs(input_data)

        total_error:float = 0
        for mu in range(len(expected)):
            total_error += (expected[mu] - outputs[mu])**2
        return total_error/2
    

    def current_outputs(self, input_data:list[list[float]]) -> list[float]:
        return [self.activation_function(np.dot([1] + x, self.weights) + self.bias) for x in input_data]

    def delta_weights(self, excitement:float, activation:float, expected:float, x_mu:float):
        return self.learning_rate * (expected - activation) * self.activation_derivative(excitement) * x_mu

    def train(self, operation, input_data:list[list[float]], expected:list[float], limit:int):
        current_steps = 0
        error_min = math.inf
        input_len = len(input_data)

        while abs(error_min) > 0 and current_steps < limit:
            mu = random.randrange(0, input_len)
            x_mu = np.array([1] + input_data[mu])
            excitement = np.dot(x_mu, self.weights) + self.bias
            activation = self.activation_function(excitement)

            self.weights += self.delta_weights(activation, excitement, expected[mu], x_mu)

            new_error = self.compute_error(input_data, expected)
            
            if new_error < error_min:
                error_min = new_error

            current_steps += 1


    def run(self, input:list[int]):
        x_mu =  np.array([1] + input)
        excitement = np.dot(x_mu, self.weights) + self.bias
        return self.activation_function(excitement)

    
    # def plot(self, operation, input_data, expected):
    #     # Puntos
    #     x_values = [point[0] for point in input_data]
    #     y_values = [point[1] for point in input_data]
    #     colors = ['red' if point == -1 else 'green' for point in expected]
    #     plt.scatter(x_values, y_values, marker='o', c=colors, zorder=2)

    #     # Recta
    #     m = -self.weights[1]/self.weights[2]
    #     b = -self.weights[0]/self.weights[2]
    #     x = np.linspace(-20, 20, 100)
    #     plt.plot(x, m*x + b, color='blue')

    #     plt.xlim(-1.5, 1.5)
    #     plt.xlabel('x')

    #     plt.ylim(-1.5, 1.5)
    #     plt.ylabel('y')

    #     title = f'Perceptron Simple Step for {operation} operation'
    #     plt.title(title)

    #     plt.grid(True, linestyle='--', alpha=0.7, zorder=1)

    #     plt.show()


class SimpleLinealPerceptron(SimplePerceptron):

    def activation_function(self, x:float) -> float:
        return x
    
    def activation_derivative(self, x:float) -> float:
        return 1


class SimpleHiperbolicPerceptron(SimplePerceptron):

    # Imagen: (-1, 1)
    def activation_function(self, x:float) -> float:
        return math.tanh(self.beta * x)
    
    def activation_derivative(self, x:float) -> float:
        return self.beta * (1 - self.activation_function(x)**2)

class SimpleLogisticPerceptrion(SimplePerceptron):
    
    def activation_function(self, x:float) -> float:
        return 1 / (1 + math.exp(-self.beta * x))
    
    def activation_derivative(self, x:float) -> float:
        return 2 * self.beta * self.activation_function(x) * (1 - self.activation_function(x))