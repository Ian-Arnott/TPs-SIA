import json
from kohonen import KohonenNetwork
from utils import get_config_params, get_data, standarize_data
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    with open('./kohonen_config.json', 'r') as f:
        config = json.load(f)

    k, learning_rate, radius, max_epochs, likeness_type = get_config_params(config)

    countries, labels, data = get_data()

    standarize_data = standarize_data(data)

    # Inicializa la red con kxk neuronas
    network = KohonenNetwork(standarize_data, len(standarize_data), k, learning_rate)

    n = len(standarize_data[0])

    # Entrena la red
    for epoch in range(max_epochs):
        for input_data in range(n):
            network.process_input(input_data, radius)

    neuron_matrix = network.neuron_matrix

    # Obtener los valores de groupCount como una matriz NumPy
    group_counts = np.array([[neuron.groupCount for neuron in row] for row in neuron_matrix])

    # Configurar un mapa de colores (puedes cambiar el mapa de colores según tus preferencias)
    cmap = plt.get_cmap('inferno')  # Ejemplo de un mapa de colores

    plt.imshow(group_counts, cmap=cmap)

    # Establecer etiquetas para el eje x
    plt.xticks(range(k), range(k))

    # Establecer etiquetas para el eje y
    plt.yticks(range(k), range(k))

    # Agregar una barra de colores (leyenda)
    cbar = plt.colorbar()
    
    cbar.set_label('Group Count')  # Etiqueta de la barra de colores

    plt.show()


