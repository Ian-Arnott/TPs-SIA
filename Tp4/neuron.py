import numpy as np

class Neuron:

    def __init__(self, weights: np.array[float], learning_rate: float = 0.1):
        #TODO: Los pesos se deberian inicializar con muestras del conjunto
        self.weights = weights
        self.activation = 0.0
        self.groupCount = 0
        self.learning_rate = learning_rate

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

class KohonenNetwork:

    def __init__(self, input_data:list[list[float]], input_size: int, k:int, learning_rate: float = 0.1):
        self.input_size = input_size
        self.k = k
        self.learning_rate = learning_rate
        
        # Inicializa la red con k neuronas
        self.neuron_matrix = [[Neuron(self.get_sample(input_data), learning_rate) for _ in range(k)] for _ in range(k)]

    @staticmethod
    def get_sample(input_data: list[list[float]]) -> np.array[float]:
        return np.array(input_data[np.random.randint(len(input_data))])