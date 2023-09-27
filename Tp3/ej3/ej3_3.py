import json
import numpy as np
from activation_functions import Tanh
from mse import mse, mse_derivative
from mlp import Dense, train, predict
from utils import get_config_params, get_data, get_training_amount
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def addNoise(X, noise):
    for matrix in X:
        for i in range(len(matrix)):
            if np.random.rand() < noise:
                matrix[i] = 1 - matrix[i]

if __name__ == "__main__":
    with open('./config.json', 'r') as f:
        config = json.load(f)

    ej, learning_rate, training_percentage, max_epochs, bias, beta, epsilon, optimizer = get_config_params(config)

    input_data, expected_data = get_data(ej)
    flattened_input = []
    for i in range(len(input_data)):
        flattened_input.append([item for sublist in input_data[i] for item in sublist])
    max_expected = max(expected_data)
    scaled_expected = [(2 * x / max_expected) - 1 for x in expected_data]
    X = np.reshape(input_data, (10, 35, 1))
    Y = np.reshape(scaled_expected, (10, 1, 1))

    # print(X)
    # print(Y)

    network = [
        Dense(35, 36, optimizer_type=optimizer, learning_rate=learning_rate),
        Tanh(),
        Dense(36, 10, optimizer_type=optimizer, learning_rate=learning_rate),
        Tanh()
    ]

    # train
    train(network, mse, mse_derivative, X, Y, epochs=max_epochs, verbose=False)



# Funcion para agregar ruido
# Es muy caotica pero tiene sentido, las imagenes son de muy baja resolucion
# por lo tanto pequenos cambios las acercan a otros numero en gran medida
    # addNoise(X,0.01)

    points = []
    for i in range(len(X)):
        z = predict(network, X[i])
        scaled_z = [ [(x + 1) * 4.5 for x in row] for row in z ]
        points.append([X[i], expected_data[i], scaled_z[i]])
    for point in points:
        print(f"Expected:{point[1]} - Result:{round(point[2][0])}")
