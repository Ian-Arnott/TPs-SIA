import numpy as np

class Neuron:

    def __init__(self, weights: list[float], learning_rate: float = 0.1):
        #TODO: Los pesos se deberian inicializar con muestras del conjunto
        self.weights = np.array(weights)
        self.activation = 0.0
        self.groupCount = 0
        self.learning_rate = learning_rate

        self.up = None
        self.down = None
        self.right = None
        self.left = None
        self.upRight = None
        self.upLeft = None
        self.downRight = None
        self.downLeft = None

    def calculate_similitude(self, input: np.array[float]) -> float:
        self.activation = self.euclidean(input)
        return self.activation

    # Distancia Euclidea
    def euclidean(self, input: np.array[float]) -> float:
        return np.linalg.norm(self.weights - input)
    
    # Distancia Exponencial
    def exponential(self, input: np.array[float]) -> float:
        return np.exp(-(self.euclidean(input)**2))
    
    # Actualiza los pesos de esta neurona
    def update_weight(self, input: np.array[float]):
        self.weights = self.weights + self.learning_rate * (input - self.weights)