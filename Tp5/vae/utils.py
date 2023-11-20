import json
import matplotlib.pyplot as plt
import numpy as np


def plot_data(original, decoded, input_rows, input_cols):
    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.set_title('Original')
    ax2.set_title('Decoded')
    ax1.imshow(np.array(original).reshape((input_rows, input_cols)), cmap='gray')
    ax2.imshow(np.array(decoded).reshape((input_rows, input_cols)), cmap='gray')
    ax1.set_xticks([])
    ax1.set_yticks([])
    ax2.set_xticks([])
    ax2.set_yticks([])

    fig.show()