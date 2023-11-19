import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


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



# Imprime una lista de matrices de 7x5, una por cada caracter
def plot_bitmap_matrix_2(matrix_list, character_list, title):
    num_plots = len(matrix_list)
    num_rows = int(np.sqrt(num_plots))
    num_cols = int(np.ceil(num_plots / num_rows))

    fig, axes = plt.subplots(num_rows, num_cols, figsize=(8, 8))

    for i in range(num_rows):
        for j in range(num_cols):
            index = i * num_cols + j
            if index < num_plots:
                axes[i, j].imshow(matrix_list[index], cmap='binary', interpolation='none', vmin=0, vmax=1)
                axes[i, j].set_title(character_list[index])
                axes[i, j].set_xticks([])
                axes[i, j].set_yticks([])
            else:
                fig.delaxes(axes[i, j])  # Elimina los ejes si no hay más plots

    plt.suptitle(title)
    plt.tight_layout()
    plt.show()



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



# Imprime 3 matrices de 7x5, una con el caracter original, otra con ruido y otra con el caracter predicho
def plot_bitmap_matrix_with_noise(original, noisy, predicted, character):
    # Crear un heatmap con imshow de matplotlib
    fig, axs = plt.subplots(1, 3, figsize=(3, 2)) # 1 fila, 2 columnas

    # Caso borde
    if(character == "DEL"):
        colors1 = ['black']
        custom_cmap1 = plt.matplotlib.colors.ListedColormap(colors1)
        colors2 = ['gray', 'black']
        custom_cmap2 = plt.matplotlib.colors.ListedColormap(colors2)

        axs[0].imshow(original, cmap=custom_cmap1, interpolation='none')
        axs[1].imshow(noisy, cmap=custom_cmap2, interpolation='none')
        axs[2].imshow(predicted, cmap=custom_cmap2, interpolation='none')
    else:
        axs[0].imshow(original, cmap='binary', interpolation='none')
        axs[1].imshow(noisy, cmap='binary', interpolation='none')
        axs[2].imshow(predicted, cmap='binary', interpolation='none')

    # Crear heatmaps para cada par de matrices

    axs[0].set_title('Original ' + character)
    axs[0].set_xticks([])
    axs[0].set_yticks([])

    axs[1].set_title('Noisy ' + character)
    axs[1].set_xticks([])
    axs[1].set_yticks([])

    axs[2].set_title('Predicted ' + character)
    axs[2].set_xticks([])
    axs[2].set_yticks([])