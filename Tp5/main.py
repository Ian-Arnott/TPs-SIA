from mlp import train, predict, Dense, Activation
from activation_functions import Tanh
from mse import mse, mse_derivative
import utils
from data.font import fontDict
import numpy as np
import matplotlib.pyplot as plt

def visualize_results(original_data, reconstructed_data, num_samples=5):
    fig, axes = plt.subplots(num_samples, 2, figsize=(8, 3 * num_samples))

    for i in range(num_samples):
        original_image = original_data[i].reshape((7, 5))
        reconstructed_image = reconstructed_data[i][0].reshape((7, 5))

        axes[i, 0].imshow(original_image, cmap='gray', aspect='auto')
        axes[i, 0].set_title(f'Original - Sample {i + 1}')
        axes[i, 0].axis('off')

        axes[i, 1].imshow(reconstructed_image, cmap='gray', aspect='auto')
        axes[i, 1].set_title(f'Reconstructed - Sample {i + 1}')
        axes[i, 1].axis('off')

    plt.suptitle('Autoencoder Results', fontsize=16)
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

def plot_latent_space(latent_space, labels):
    latent_values = [point[1] for point in latent_space]
    latent_values = np.array(latent_values)

    plt.scatter(latent_values[:, 0], latent_values[:, 1], c=labels, cmap='viridis')
    plt.title('Latent Space Visualization')
    plt.xlabel('Latent Dimension 1')
    plt.ylabel('Latent Dimension 2')
    plt.colorbar()
    plt.show()

if __name__ == "__main__":
    bitmapDict = utils.fonts_to_bitmap(fontDict)
    bitmapList = list(bitmapDict.values())  
    X = np.reshape(bitmapList,(len(bitmapList), 35, 1))

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

    train(autoencoder, mse, mse_derivative, X, X, epochs=1000, verbose=False)
    reconstructed_data = [predict(autoencoder, x) for x in X]