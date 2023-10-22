import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import BoundaryNorm

def plot_heatmap(network, input_data, countries):
    k = network.k

    activation_matrix = np.zeros((k, k))
    countries_matrix = [["" for _ in range(k)] for _ in range(k)]

    for i in range(len(input_data)):
        x, y = network.predict(input_data[i])
        activation_matrix[x][y] += 1
        countries_matrix[x][y] += f"{countries[i]}\n"

    # Configurar un mapa de colores (puedes cambiar el mapa de colores según tus preferencias)
    cmap = plt.get_cmap('magma')  # Ejemplo de un mapa de colores

    # Configurar el tamaño de la figura
    plt.figure(figsize=(8, 8))

    

    # Establecer etiquetas para el eje x
    plt.xticks(range(k), range(k))

    # Establecer etiquetas para el eje y
    plt.yticks(range(k), range(k))
    
    # Crear una norma de límites enteros
    min_val = min(min(row) for row in activation_matrix)
    max_val = max(max(row) for row in activation_matrix)
    norm = BoundaryNorm(np.arange(min_val, max_val + 1), cmap.N)

    plt.imshow(activation_matrix, cmap=cmap, norm=norm)

    # Agregar valores numéricos a cada celda del heatmap
    for i in range(k):
        for j in range(k):
            cell_color = cmap(norm(activation_matrix[i][j]))
            brightness = np.linalg.norm(cell_color[:3])  # Calcula la luminancia (brillo)
            text_color = 'k' if brightness >= 0.5 else 'w'  # Determina el color del texto
            annotation = str(int(activation_matrix[i][j])) + "\n" + countries_matrix[i][j]
            plt.text(j, i, annotation, ha='center', va='center', color=text_color)


    # Agregar una barra de colores (leyenda)
    cbar = plt.colorbar()
    cbar.set_label('Group Count')  # Etiqueta de la barra de colores

    plt.show()

def plot_unified_distance_heatmap(ud_matrix, k):
    # Configurar un mapa de colores en escala de grises ("gray")
    cmap = plt.get_cmap('gray')

    # Crear el heatmap en blanco y negro
    plt.imshow(ud_matrix, cmap=cmap)

    # Agregar valores numéricos a cada celda del heatmap
    
    # Corregimos el color del texto
    min_val = min(min(row) for row in ud_matrix)
    max_val = max(max(row) for row in ud_matrix)
    color_thr = min_val + 0.8 * (max_val - min_val)


    print(color_thr)
    for i in range(k):
        for j in range(k):
            color = 'w' if ud_matrix[i][j] < color_thr else 'k'
            plt.text(j, i, str(f"{ud_matrix[i][j]:.2f}"), ha='center', va='center', color=color)
            

    # Agregar una barra de colores (leyenda)
    cbar = plt.colorbar()
    cbar.set_label('Valor')  # Etiqueta de la barra de colores

    plt.show()

def plot_one_variable_heatmap(network, input_data, labels, variable):
    k = network.k

    activation_matrix = np.zeros((k, k))

    for i in range(len(input_data)):
        x, y = network.predict(input_data[i])
        activation_matrix[x][y] += input_data[i][variable]

    cmap = plt.get_cmap('Purples')

    

    plt.xticks(range(k), range(k))
    plt.yticks(range(k), range(k))

    # Crear una norma de límites enteros
    min_val = min(min(row) for row in activation_matrix)
    max_val = max(max(row) for row in activation_matrix)
    norm = BoundaryNorm(np.arange(min_val, max_val + 1), cmap.N)

    plt.imshow(activation_matrix, cmap=cmap)

    for i in range(k):
        for j in range(k):
            cell_color = cmap(norm(activation_matrix[i][j]))
            brightness = np.linalg.norm(cell_color[:3])  # Calcula la luminancia (brillo)
            text_color = 'k' if brightness >= 0.5 else 'w'  # Determina el color del texto
            annotation = f"{activation_matrix[i, j]:.2f}"
            plt.text(j, i, annotation, ha='center', va='center', color=text_color)
            

    plt.title(f"\"{labels[variable]}\" para cada neurona")
    plt.colorbar()
    plt.show()