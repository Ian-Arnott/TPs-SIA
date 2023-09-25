import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import random
import math
from PIL import Image
import os

class Perceptron:

    def __init__(self, learning_rate:float, weights, bias:float):
        self.weights = weights
        self.learning_rate = learning_rate
        self.bias = bias
        self.equations = []

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
    
    def add_equation(self):
        m = -self.weights[1]/self.weights[2]
        b = -self.weights[0]/self.weights[2]
        y = {'m': m, 'b': b}
        self.equations.append(y)

    def train(self, input_data:list[list[int]], expected:list[float], limit:int):
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
            
            self.add_equation()

            current_steps += 1


    def run(self, input:list[int]):
        x_mu =  np.array([1] + input)
        excitement = np.dot(x_mu, self.weights) + self.bias
        return self.activation_function(excitement)

    
    def plot_final(self, operation, input_data, expected):
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

        plt.xlim(-2, 2)
        plt.xlabel('x')

        plt.ylim(-2,2)
        plt.ylabel('y')

        title = f'Perceptron Simple Step for {operation} operation'
        plt.title(title)

        plt.grid(True, linestyle='--', alpha=0.7, zorder=1)
    
        legend_elements = [Line2D([0], [0], marker='o', color='w', label='-1', markerfacecolor='red', markersize=10),
                       Line2D([0], [0], marker='o', color='w', label='1', markerfacecolor='green', markersize=10)]
        plt.legend(handles=legend_elements, title='Output')

        plt.show()


    def plot_evolution(self, operation, input_data, expected):
        image_files = []
        x = np.linspace(-20, 20, 100)
        plt.figure()

        for i, equation in enumerate(self.equations):
            x_values = [point[0] for point in input_data]
            y_values = [point[1] for point in input_data]
            colors = ['red' if point == -1 else 'green' for point in expected]
            plt.scatter(x_values, y_values, marker='o', c=colors, zorder=2)

            m = equation['m']
            b = equation['b']
            y = m*x+b

            plt.plot(x, y, color='blue')
            plt.xlim(-2, 2)
            plt.xlabel('x')
            plt.ylim(-2, 2)
            plt.ylabel('y')
            title = f'Perceptron Simple Step {i+1} for {operation} operation'
            plt.title(title)
            plt.grid(True, linestyle='--', alpha=0.7, zorder=1)
            legend_elements = [Line2D([0], [0], marker='o', color='w', label='-1', markerfacecolor='red', markersize=10),
                       Line2D([0], [0], marker='o', color='w', label='1', markerfacecolor='green', markersize=10)]
            plt.legend(handles=legend_elements, title='Output')

            file_name = f'graph_{i}.png'
            plt.savefig(file_name)

            image_files.append(file_name)

            plt.close()

        images = [Image.open(file) for file in image_files]
        images[0].save('evolution.gif', save_all=True, append_images=images[1:], duration=500, loop=0)

        for file in image_files:
            os.remove(file)