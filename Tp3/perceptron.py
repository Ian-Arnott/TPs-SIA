from numpy import random, array
import sys

class Perceptron:

    def __init__(self, learning_rate:float, weights):
        self._weights = weights
        self.learning_rate = learning_rate

# TODO: Extraer comportamientos comunes 
class SimpleStepPerceptron(Perceptron):

    def __init__(self, learning_rate:float):
        # Inicializo wi con 3 valores aleatorios
        weights = random.rand(3, 1)
        super().__init__(learning_rate, weights)

    def activation_function(self, x:float) -> int:
        return 1 if x >= 0 else -1

    #TODO: Como se calcula el error?
    def compute_error():
        return 1
        pass

    # La lista input son pares de 1 y -1: [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    # la lista expected son los valores esperados para cada par: [1, -1, -1, -1]
    def train(self, input:list[list[int]], expected:list[float], limit:int):
        i:int = 0
        error = 0
        min_error = sys.maxsize
        w_min = None

        while min_error > 0 and i < limit:
            # Elijo un indice al azar
            #TODO: Como evito repetir?
            mu = random.randint(0, len(input)-1)

            # Tomo el valor de entrada correspondiente, agregando el bias (1)
            x_mu = array([1] + input[mu])

            # Calculamos la excitacion (producto escalar)
            excitement = self._weights @ x_mu

            # Calculamos la activacion (theta)
            activation = self.activation_function(excitement)

            # Actualizamos los pesos
            delta_w = self.learning_rate * (expected[mu] - activation) * x_mu
            self._weights += delta_w

            # Actualizamos el error
            error = self.compute_error()
            if(error < min_error):
                min_error = error
                w_min = self._weights
            
            i += 1



