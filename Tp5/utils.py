import json
import matplotlib.pyplot as plt
import pandas as pd

#TODO: Conviene convertir la lista a np.array?
def fonts_to_bitmap(fonts:dict):
    bitmaps = {}
    for (character, hexaList) in fonts.items():
        bitmap = []
        for byte in hexaList:
            binary = format(byte, '08b')  
            row = [int(bit) for bit in binary[-5:]]  # Los caracteres tienen 3 bits de padding
            bitmap.extend(row)
        bitmaps[character] = bitmap
    return bitmaps


# Imprime un bitmap de 7x5
def print_bitmap(bitmap:list):
    for i in range(7):
        for j in range(5):
            print(bitmap[i*5 + j], end='')
        print()


# Devuelve una matriz de 7x5
def bitmap_as_matrix(bitmap:list): 
    return [[bitmap[i*5 + j] for j in range(5)] for i in range(7)]


# Imprime dos matrices de 7x5, una con el caracter original y otra con el caracter predicho
def plot_bitmap_matrix(original, predicted, character):
    # Crear un heatmap con imshow de matplotlib
    fig, axs = plt.subplots(1, 2, figsize=(3, 2)) # 1 fila, 2 columnas

    # Caso borde
    if(character == "DEL"):
        colors1 = ['black']
        custom_cmap1 = plt.matplotlib.colors.ListedColormap(colors1)
        colors2 = ['gray', 'black']
        custom_cmap2 = plt.matplotlib.colors.ListedColormap(colors2)

        axs[0].imshow(original, cmap=custom_cmap1, interpolation='none')
        axs[1].imshow(predicted, cmap=custom_cmap2, interpolation='none')
    else:
        axs[0].imshow(original, cmap='binary', interpolation='none')
        axs[1].imshow(predicted, cmap='binary', interpolation='none')

    # Crear heatmaps para cada par de matrices

    axs[0].set_title('Original ' + character)
    axs[0].set_xticks([])
    axs[0].set_yticks([])

    axs[1].set_title('Predicted ' + character)
    axs[1].set_xticks([])
    axs[1].set_yticks([])


def plot_latent_spaces(latent_space, characters):
    # Convertir la lista de tuplas y etiquetas a un DataFrame de Pandas
    df = pd.DataFrame({'x': [p[0] for p in latent_space], 'y': [p[1] for p in latent_space], 'etiqueta': characters})

    # Graficar los puntos usando Pandas
    ax = df.plot.scatter(x='x', y='y', color='blue', marker='o', s=50)

    # Anotar cada punto con su respectiva etiqueta
    for i, row in df.iterrows():
        ax.annotate(row['etiqueta'], (row['x'], row['y']), textcoords="offset points", xytext=(0,5), ha='center')

    # Configurar etiquetas y título
    ax.set_xlabel('Dimension 1')
    ax.set_ylabel('Dimension 2')
    ax.set_title('Gráfico del Espacio Latente para cada Caracter')

    # Mostrar el gráfico
    plt.show()


def get_config_params(config_file: str):
    with open(config_file, 'r') as f:
        config = json.load(f)

    learning_rate = config["learning_rate"]

    max_epochs = config["max_epochs"]

    bias = config["bias"]

    beta1 = config["beta1"]

    beta2 = config["beta2"]

    epsilon = config["epsilon"]

    optimizer = config["optimizer"]

    activation = config["activation"]

    hidden_layers = config["hidden_layers"]

    latent_space = config["latent_space"]

    return learning_rate, max_epochs, bias, beta1, beta2, epsilon, optimizer, activation, hidden_layers, latent_space
