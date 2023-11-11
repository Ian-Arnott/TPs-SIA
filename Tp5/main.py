from mlp import train, predict, Dense, Activation
from activation_functions import Tanh
from mse import mse, mse_derivative
import utils
from data.font import fontDict
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    bitmapDict = utils.fonts_to_bitmap(fontDict)

    # Prepare data
    bitmapList = list(bitmapDict.values())  
    X = np.reshape(bitmapList,(len(bitmapList), 35, 1))
    # Define Autoencoder Architecture
    autoencoder = [
        Dense(35, 10, optimizer_type="ADAM", learning_rate=0.001),
        Tanh(),
        Dense(10, 2, optimizer_type="ADAM", learning_rate=0.001),
        Tanh(),
        Dense(2, 10, optimizer_type="ADAM", learning_rate=0.001),
        Tanh(),
        Dense(10, 35, optimizer_type="ADAM", learning_rate=0.001),
        Tanh(),
    ]

    # Train Autoencoder
    train(autoencoder, mse, mse_derivative, X, X, epochs=1000, verbose=False)

    # Evaluate the network by predicting on the training data
    reconstructed_data = [predict(autoencoder, x) for x in X]

