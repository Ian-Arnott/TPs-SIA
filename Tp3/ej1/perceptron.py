import numpy as np
import matplotlib.pyplot as plt
import random
import math

class Perceptron:

    def __init__(self, learning_rate:float, weights, bias:float):
        self.weights = weights
        self.learning_rate = learning_rate
        self.bias = bias

class SimpleStepPerceptron(Perceptron):

    def __init__(self, learning_rate:float, bias:float):
        weights = np.random.rand(3)
        super().__init__(learning_rate, weights, bias)


    def activation_function(self, x:float) -> int:
        return 1 if x >= 0 else -1


    def compute_error(self, expected:list[float], outputs:list[float]):
        total_error = 0
        for mu in range(len(expected)):
            total_error += abs(expected[mu] - outputs[mu])
        return total_error


    def train(self, operation, input_data:list[list[int]], expected:list[float], limit:int):
        current_steps = 0
        error_min = math.inf
        input_len = len(input_data)

        while abs(error_min) > 0 and current_steps < limit:
            index = random.randrange(0, input_len)
            x_mu = np.array([1] + input_data[index])
            excitement = np.dot(x_mu, self.weights) + self.bias
            activation = self.activation_function(excitement)

            self.weights += self.learning_rate * (expected[index] - activation) * x_mu

            new_error = self.compute_error(expected, [self.activation_function(np.dot([1] + x, self.weights) + self.bias) for x in input_data])
            
            if new_error < error_min:
                error_min = new_error

            current_steps += 1


    def run(self, input:list[int]):
        x_mu =  np.array([1] + input)
        excitement = np.dot(x_mu, self.weights) + self.bias
        return self.activation_function(excitement)

    
    def plot(self, operation, input_data, expected):
        # Puntos
        x_values = [point[0] for point in input_data]
        y_values = [point[1] for point in input_data]
        colors = ['red' if point == -1 else 'green' for point in expected]
        plt.scatter(x_values, y_values, marker='o', c=colors, zorder=2)

        # Recta
        m = -self.weights[1]/self.weights[2]
        b = -self.weights[0]/self.weights[2]
        x = np.linspace(-20, 20, 100)
        plt.plot(x, m*x + b, color='blue')

        plt.xlim(-1.5, 1.5)
        plt.xlabel('x')

        plt.ylim(-1.5, 1.5)
        plt.ylabel('y')

        title = f'Perceptron Simple Step for {operation} operation'
        plt.title(title)

        plt.grid(True, linestyle='--', alpha=0.7, zorder=1)

        plt.show()
