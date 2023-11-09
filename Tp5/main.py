from mlp import train, predict, Dense
from activation_functions import Tanh, Sigmoid, Linear
from mse import mse, mse_derivative
import utils
from data.font import fontDict
import numpy as np

if __name__ == "__main__":

    bitmapDict = utils.fonts_to_bitmap(fontDict)
    for clave, valor in bitmapDict.items():
        print(f'{clave}: {valor}')

    learning_rate=0.001

    autoencoder = [
        Dense(35, 20, optimizer_type="ADAM", learning_rate=learning_rate),
        Tanh(),
        Dense(20, 10, optimizer_type="ADAM", learning_rate=learning_rate),
        Tanh(),
        Dense(10, 2, optimizer_type="ADAM", learning_rate=learning_rate),
        Tanh(),
        Dense(2, 10, optimizer_type="ADAM", learning_rate=learning_rate),
        Tanh(),
        Dense(10, 20, optimizer_type="ADAM", learning_rate=learning_rate),
        Tanh(),
        Dense(20, 35, optimizer_type="ADAM", learning_rate=learning_rate),
        Tanh(),
    ]

    # letras
    bitmapList = list(bitmapDict.values())

    # train
    train(autoencoder, mse, mse_derivative, bitmapList, bitmapList, epochs=1000, verbose=False)