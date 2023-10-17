import numpy as np

class OjaNetwork:
    def __init__(self, learning_rate, input_size):
        self.weights = np.random.rand(input_size)
        self.learning_rate = learning_rate

    def train(self, input_data, max_epoch):
        epoch = 0

        while epoch < max_epoch:
            for x in input_data:
                O = np.dot(x, self.weights)
                self.weights += self.learning_rate * (O * x - O*O * self.weights)
            epoch += 1

        return self.weights