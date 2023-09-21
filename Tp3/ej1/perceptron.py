import numpy as np
import random
import math

class Perceptron:

    def __init__(self, learning_rate:float, weights):
        self._weights = weights
        self.learning_rate = learning_rate

class SimpleStepPerceptron(Perceptron):

    def __init__(self, learning_rate:float):
        weights = np.random.rand(3)
        super().__init__(learning_rate, weights)

    def activation_function(self, x:float) -> int:
        return 1 if x >= 0 else -1

    def compute_error(self, expected:list[float], outputs:list[float]):
        total_error = 0
        for mu in range(len(expected)):
            total_error += abs(expected[mu] - outputs[mu])
        return total_error

    def train(self, input:list[list[int]], expected:list[float], limit:int):
        current_steps = 0
        error = 0
        error_min = math.inf

        while abs(error_min) > 0 and current_steps < limit:
            index = random.randrange(0, len(input))
            x_mu = np.array([1] + input[index])
            excitement = np.dot(x_mu, self._weights)
            activation = self.activation_function(excitement)

            self._weights += self.learning_rate * (expected[index] - activation) * x_mu

            new_error = self.compute_error(expected, [self.activation_function(np.dot([1] + x, self._weights)) for x in input])
            if new_error < error_min:
                error_min = new_error
            current_steps += 1
            print(f'Weights: {self._weights}')
            print(f'Current step: {current_steps}, with new_error: {new_error}')

    def run(self, input:list[int]):
        x_mu =  np.array([1] + input)
        return self.activation_function(np.dot(x_mu, self._weights))
