import json
from kohonen import KohonenNetwork
from utils import get_config_params, get_data, standarize_data
import numpy as np
import matplotlib.pyplot as plt

def plot_heatmap(network, input_data, countries):

    activation_matrix = np.zeros((network.k, network.k))
    countries_matrix = [["" for _ in range(network.k)] for _ in range(network.k)]

    for i in range(len(input_data)):
        x, y = network.predict(input_data[i])
        activation_matrix[x][y] += 1
        countries_matrix[x][y] += f"{countries[i]}\n"

    # countries_array = np.array(countries_matrix)

    # Configurar un mapa de colores (puedes cambiar el mapa de colores según tus preferencias)
    cmap = plt.get_cmap('inferno')  # Ejemplo de un mapa de colores

    # Configurar el tamaño de la figura
    plt.figure(figsize=(8, 8))

    plt.imshow(activation_matrix, cmap=cmap)

    # Establecer etiquetas para el eje x
    plt.xticks(range(k), range(k))

    # Establecer etiquetas para el eje y
    plt.yticks(range(k), range(k))

    # Agregar valores numéricos a cada celda del heatmap
    for i in range(k):
        for j in range(k):
            color = 'w' if activation_matrix[i, j] < 6 else 'k'
            annotation = str(int(activation_matrix[i, j])) + "\n" + countries_matrix[i][j]
            plt.text(j, i, annotation, ha='center', va='center', color=color)


    # Agregar una barra de colores (leyenda)
    cbar = plt.colorbar()
    cbar.set_label('Group Count')  # Etiqueta de la barra de colores

    plt.show()

def plot_unified_distance_heatmap(ud_matrix):
    # Configurar un mapa de colores en escala de grises ("gray")
    cmap = plt.get_cmap('gray')

    # Crear el heatmap en blanco y negro
    plt.imshow(ud_matrix, cmap=cmap)

    # Agregar valores numéricos a cada celda del heatmap
    color_thr = max(max(row) for row in ud_matrix)/2.0
    for i in range(k):
        for j in range(k):
            color = 'w' if ud_matrix[i, j] < color_thr else 'k'
            plt.text(j, i, str(f"{ud_matrix[i, j]:.2f}"), ha='center', va='center', color=color)


    # Agregar una barra de colores (leyenda)
    cbar = plt.colorbar()
    cbar.set_label('Valor')  # Etiqueta de la barra de colores

    plt.show()


if __name__ == "__main__":
    with open('./config.json', 'r') as f:
        config = json.load(f)

    k, learning_rate, initial_radius, max_epochs, likeness_type = get_config_params(config)

    countries, labels, data = get_data()

    standarized_data = standarize_data(data)

    # Inicializa la red con kxk neuronas
    network = KohonenNetwork(standarized_data, len(standarized_data), k, learning_rate, initial_radius)

    n = len(standarized_data[0])

    # Entrena la red
    network.train(max_epochs)

    # for i in range(network.k):
    #     for j in range(network.k):
    #         print(network.neuron_matrix[i][j].weights)

    plot_heatmap(network, standarized_data, countries)
    plot_unified_distance_heatmap(network.get_unified_distance_matrix())

    

    


