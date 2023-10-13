import numpy as np
from scipy.spatial import distance

class Neuron:

    def __init__(self, weights, learning_rate: float = 0.1):
        #TODO: Los pesos se deberian inicializar con muestras del conjunto
        self.weights = weights
        self.activation = 0.0
        self.groupCount = 0
        self.learning_rate = learning_rate

    def calculate_similitude(self, input) -> float:
        self.activation = self.euclidean(input)
        return self.activation

    # Distancia Euclidea
    def euclidean(self, input) -> float:
        return np.linalg.norm(self.weights - input)
    
    # Distancia Exponencial
    def exponential(self, input) -> float:
        return np.exp(-(self.euclidean(input)**2))
    
    # Actualiza los pesos de esta neurona
    def update_weight(self, input):
        self.weights = self.weights + self.learning_rate * (input - self.weights)

class KohonenNetwork:

    def __init__(self, input_data:list[list[float]], input_size: int, k:int, learning_rate: float = 0.1):
        self.input_size = input_size
        self.k = k
        self.learning_rate = learning_rate
        
        # Inicializa la red con k neuronas
        self.neuron_matrix = [[Neuron(self.get_sample(input_data), learning_rate) for _ in range(k)] for _ in range(k)]


    @staticmethod
    def get_sample(input_data: list[list[float]]):
        return np.array(input_data[np.random.randint(len(input_data))])
    

    def process_input(self, input_data, current_radius):
        # Calcula la similitud de cada neurona con la entrada
        for i in range(self.k):
            for j in range(self.k):
                self.neuron_matrix[i][j].calculate_similitude(input_data)
        
        # Obtiene la neurona con menor similitud
        winner_neuron, winner_neuron_index = self._get_winner_neuron()
        winner_neuron.groupCount += 1

        # Actualiza los pesos a partir de la neurona ganadora
        self.update_weights(winner_neuron_index, input_data, current_radius)


    def _get_winner_neuron(self) -> (Neuron, (int, int)):
        winner_neuron = self.neuron_matrix[0][0]
        winner_neuron_index = (0, 0)
        for i in range(self.k):
            for j in range(self.k):
                if self.neuron_matrix[i][j].activation < winner_neuron.activation:
                    winner_neuron = self.neuron_matrix[i][j]
                    winner_neuron_index = (i, j)
        return winner_neuron, winner_neuron_index

    @staticmethod
    def m_distance(x, y):
        return distance.cityblock(x, y)

    def update_weights(self, winner_neuron_index:(int, int), input_data, current_radius):
        for i in range(self.k):
            for j in range(self.k):
                if self.m_distance((i, j), winner_neuron_index) <= current_radius:
                    self.neuron_matrix[i][j].update_weight(input_data)