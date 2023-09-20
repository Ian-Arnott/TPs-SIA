from numpy import random, array
import sys
import math

class Perceptron:

    def __init__(self, learning_rate:float, weights):
        self._weights = weights
        self.learning_rate = learning_rate

# TODO: Extraer comportamientos comunes 
class SimpleStepPerceptron(Perceptron):

    def __init__(self, learning_rate:float):
        # Inicializo wi con 3 valores aleatorios
        weights = random.rand(1, 3)
        super().__init__(learning_rate, weights)

    def activation_function(self, x:float) -> int:
        return 1 if x >= 0 else -1

        # run(1,1) --> -1

    #TODO: Como se calcula el error?
    def compute_error(self, expected:list[float], outputs:list[float]):
        return ((array(expected) - array(outputs)) ** 2).mean()

    # La lista input son pares de 1 y -1: [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    # la lista expected son los valores esperados para cada par: [1, -1, -1, -1]
    def train(self, input:list[list[int]], expected:list[float], limit:int):
        i:int = 0
        error = 0
        min_error = math.inf
        w_min = None

        while min_error > 0 and i < limit:
            # Elijo un indice al azar
            #TODO: Como evito repetir?

            outputs = []
            for mu in range(len(input)):
                x_mu = array([1] + input[mu])
                excitement = self._weights @ x_mu
                activation = self.activation_function(excitement)
                outputs.append(activation)

                delta_w = self.learning_rate * (expected[mu] - activation) * x_mu
                self._weights += delta_w

            # Actualizamos el error usando la nueva función compute_error
            error = self.compute_error(expected, outputs)
            if(error < min_error):
                min_error = error
                w_min = self._weights
            
            i += 1
        print(i)

    def run(self, input:list[int]):
        # TODO: hay bias? Sin bias las dimensiones de las matrices no coinciden
        x_mu =  array([1]+input)
        return self.activation_function(self._weights @ x_mu)
    
class SimpleLinearPerceptron(Perceptron):

    def __init__(self, learning_rate: float, epsilon:float):
        # weights = random.rand(3,1)
        weights = array([[random.normal(29,27)], [random.normal(29,27)], [random.normal(29,27)]])
        self.epsilon = epsilon
        super().__init__(learning_rate, weights)

    def activation_function(self,x:float):
        return x

    def compute_error(self, expected:float, output:float):
        return ((expected - output)**2)/2

    def compute_error(self, expected:list[float], outputs:list[float]):
        return ((array(expected) - array(outputs))**2).mean()/2


    def train(self,  inp1:list[float], inp2:list[float],inp3:list[float], expected:list[float], limit:int):
        i:int = 0
        error = 0
        min_error = math.inf
        w_min = None

        while min_error > self.epsilon and i < limit:
            outputs = []
            for mu in range(len(inp1)):
                x_mu = array([[inp1[mu], inp2[mu], inp3[mu]]])

                # excitement = self._weights @ x_mu
                excitement = x_mu @ (self._weights)
                activation = self.activation_function(excitement)
                outputs.append(activation)


                delta_w = (self.learning_rate * (expected[mu] - excitement)) * x_mu.T

                # a
                # b
                # c  += a b c
                self._weights += delta_w

            # Actualizamos el error usando la nueva función compute_error
            error = self.compute_error(expected, outputs)
            if(error < min_error):
                min_error = error
                w_min = self._weights
            
            i += 1
        print(i)
        
    def run(self, inp1:float, inp2:float,inp3:float):
        # TODO: hay bias? Sin bias las dimensiones de las matrices no coinciden
        x_mu = [inp1,inp2,inp3]
        excitement = x_mu @ self._weights
        return self.activation_function(excitement)
