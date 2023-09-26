import numpy as np
import random
import math
from abc import ABC, abstractmethod


class SimplePerceptron(ABC):
    def __init__(self, learning_rate:float, weights, bias:float, input_data_dim:int, epsilon:float):
        if(weights is None or len(weights) == 0):
            if(input_data_dim is None):
                raise Exception("No input_data_dim provided")
            self.weights = np.random.rand(input_data_dim + 1) # Tiene en cuenta w_0
        else:
            self.weights = weights
        
        self.learning_rate = learning_rate
        self.bias = bias
        self.epsilon = epsilon

 
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
            scaled_expected = self.activation_function(expected[mu])
            total_error += (scaled_expected - outputs[mu])**2
        return total_error/len(expected)
    
    def theta(self, x:list[float]) -> float:
        # Agrega un 1 al principio de x_mu para tener en cuenta el w_0
        extended_x = np.array([1] + x)
        return np.dot(extended_x, self.weights) + self.bias


    def current_outputs(self, input_data:list[list[float]]) -> list[float]:
        return [self.activation_function(self.theta(x_mu)) for x_mu in input_data]

    def delta_weights(self, excitement:float, activation:float, expected:float, x_mu:list[float]):
        extended_x_mu = np.array([1] + x_mu)
        scaled_expected = self.activation_function(expected)
        return self.learning_rate * (scaled_expected - activation) * self.activation_derivative(excitement) * extended_x_mu

    def train(self, input_data:list[list[float]], expected:list[float], limit:int, should_scale:bool = False):
        epoch = 0
        error_min = math.inf
        input_len = len(input_data)
        
        if (should_scale):
            expected = [self.scale_result(value, min(expected), max(expected)) for value in expected]

        mse = []
        
        while error_min > self.epsilon and epoch < limit:
            mu = random.randrange(0, input_len)
            x_mu = input_data[mu]
            excitement = self.theta(x_mu)
            activation = self.activation_function(excitement)

            self.weights += self.delta_weights(excitement, activation, expected[mu], x_mu)

            new_error = self.compute_error(input_data, expected)

            mse.append(new_error)
            
            if new_error < error_min:
                error_min = new_error

            epoch += 1
        
        return epoch, mse
    


    def scale_result(self, value,  new_min, new_max):
        scaled = ((value - new_min) / (new_max - new_min)) * (self.activation_max - self.activation_min) + self.activation_min
        return scaled

    def _predict_one(self, x:list[int], should_scale:bool, scale_interval:tuple[float]) -> float:
        excitement = self.theta(x)
        activation = self.activation_function(excitement)
        return activation

    def predict(self, input_data:list[list[float]], should_scale:bool = False, scale_interval:tuple[float] = ()) -> list[float]:
        if should_scale:
            if scale_interval is None or len(scale_interval) != 2:
                raise Exception("Wrong scale_interval: size must be 2")
            if scale_interval[0] > scale_interval[1]:
                raise Exception("Wrong scale_interval: min > max")

        return [self._predict_one(x, should_scale=should_scale, scale_interval=scale_interval) for x in input_data]




class SimpleLinealPerceptron(SimplePerceptron):

    def activation_function(self, x:float) -> float:
        return x
    
    def activation_derivative(self, x:float) -> float:
        return 1


class SimpleHiperbolicPerceptron(SimplePerceptron):

    def __init__(self,  beta:float, learning_rate:float, weights, bias:float, input_data_dim:int, epsilon:float):
        self.beta = beta
        self.activation_min = -1.0
        self.activation_max = 1.0
        super().__init__(learning_rate, weights, bias, input_data_dim, epsilon)

    # Imagen: (-1, 1)
    def activation_function(self, x:float) -> float:
        return math.tanh(self.beta * x)
    
    def activation_derivative(self, x:float) -> float:
        return self.beta * (1 - self.activation_function(x)**2)


class SimpleLogisticPerceptrion(SimplePerceptron):

    def __init__(self,  beta:float, learning_rate:float, weights, bias:float, input_data_dim:int, epsilon:float):
        self.beta = beta
        self.activation_min = 0.0
        self.activation_max = 1.0
        super().__init__(learning_rate, weights, bias, input_data_dim, epsilon)
    
    # Imagen: (0, 1)
    def activation_function(self, x:float) -> float:
        return 1 / (1 + math.exp(-self.beta * x))
    
    def activation_derivative(self, x:float) -> float:
        return 2 * self.beta * self.activation_function(x) * (1 - self.activation_function(x))