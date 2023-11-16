import json

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
