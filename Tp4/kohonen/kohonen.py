import numpy as np
import math
from scipy.spatial import distance

class Neuron:

    def __init__(self, weights, learning_rate: float = 0.1):
        #TODO: Los pesos se deberian inicializar con muestras del conjunto
        self.weights = weights
        self.activation = 0.0
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

    def __init__(self, input_data:list[list[float]], input_size: int, k:int, learning_rate: float = 0.1, radius: int = 1):
        self.input_size = input_size
        self.k = k
        self.learning_rate = learning_rate
        self.input_data = input_data
        self.initial_radius = radius
        
        # Inicializa la red con k neuronas
        self.neuron_matrix = [[Neuron(self.get_random_sample(), learning_rate) for _ in range(k)] for _ in range(k)]


    def get_random_sample(self):
        return np.array(self.input_data[np.random.randint(len(self.input_data))])
    

    def train(self, epochs):
        current_radius = self.initial_radius
        for epoch in range(epochs):
            current_input = self.get_random_sample()
            # Calcula la similitud de cada neurona con la entrada
            for i in range(self.k):
                for j in range(self.k):
                    self.neuron_matrix[i][j].calculate_similitude(current_input)
            
            # Obtiene la neurona con menor similitud
            winner_neuron_index = self.get_winner_neuron()

            # Actualiza los pesos a partir de la neurona ganadora
            if(current_radius > 1):
                current_radius = max(1, self.initial_radius / (epoch + 1))

            self.update_weights(winner_neuron_index, current_radius)

    def predict(self, input):
        # Calcula la similitud de cada neurona con la entrada
        for i in range(self.k):
            for j in range(self.k):
                self.neuron_matrix[i][j].calculate_similitude(input)

        # Obtiene la neurona con menor similitud
        winner_neuron_index = self.get_winner_neuron()
        return winner_neuron_index

    def get_winner_neuron(self) -> (int, int):
        winner_neuron = self.neuron_matrix[0][0]
        winner_neuron_index = (0, 0)
        for i in range(self.k):
            for j in range(self.k):
                if self.neuron_matrix[i][j].activation < winner_neuron.activation:
                    winner_neuron = self.neuron_matrix[i][j]
                    winner_neuron_index = (i, j)
        return winner_neuron_index


    def update_weights(self, winner_neuron_index:(int, int), radius: int = 1):
        neighbours = self.get_neighbours(winner_neuron_index, radius)
        for (i,j) in neighbours:
            self.neuron_matrix[i][j].update_weight(self.input_data)

    
    def get_neighbours(self, neuron_pos:(int, int), radius: int = 1):
        neighbours = []
        neuron_pos_array = np.array(neuron_pos)

        for i in range(self.k):
            for j in range(self.k):
                if np.linalg.norm(np.array([i, j]) - neuron_pos_array) <= radius:
                    neighbours.append((i, j))
        return neighbours
    
    # Se asume radio = 1
    def _get_neighbourhood_mean(self, neuron_pos):
        sum = 0
        count = 0
        x, y = neuron_pos
        neuron = self.neuron_matrix[x][y]


        # Up neighbour
        if(y - 1 >= 0):
            count += 1
            sum += neuron.euclidean(self.neuron_matrix[x][y - 1].weights)
        
        # Down neighbour
        if(y + 1 < self.k):
            count += 1
            sum += neuron.euclidean(self.neuron_matrix[x][y + 1].weights)

        # Left neighbour
        if(x - 1 >= 0):
            count += 1
            sum += neuron.euclidean(self.neuron_matrix[x - 1][y].weights)

        # Right neighbour
        if(x + 1 < self.k):
            count += 1
            sum += neuron.euclidean(self.neuron_matrix[x + 1][y].weights)

        return sum / count


    def get_unified_distance_matrix(self):
        unified_distance_matrix = np.zeros((self.k, self.k))
        for i in range(self.k):
            for j in range(self.k):
                unified_distance_matrix[i][j] = self._get_neighbourhood_mean((i, j))
        return unified_distance_matrix