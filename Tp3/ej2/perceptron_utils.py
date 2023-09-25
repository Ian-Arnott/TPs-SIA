import matplotlib.pyplot as plt
import numpy as np
from perceptron import SimpleLinealPerceptron, SimpleHiperbolicPerceptron, SimpleLogisticPerceptrion
from utils import PERCEPTRON_TYPES


def initialize_perceptron(perceptron_type, beta, learning_rate, bias, input_size, epsilon):
    if perceptron_type == PERCEPTRON_TYPES[0]:
        return SimpleLinealPerceptron(learning_rate, None, bias, input_size, epsilon)
    elif perceptron_type == PERCEPTRON_TYPES[1]:
        return SimpleHiperbolicPerceptron(beta, learning_rate, None, bias, input_size, epsilon)
    elif perceptron_type == PERCEPTRON_TYPES[2]:
        return SimpleLogisticPerceptrion(beta, learning_rate, None, bias, input_size, epsilon)


def min_max_interval(values:list[float]) -> tuple[float]:
    min_value = min(values)
    max_value = max(values)
    return (min_value, max_value)


def calculate_accuracy(predictions, expected, epsilon):
    correct_predictions = sum(1 for p, gt in zip(predictions, expected) if abs(p - gt) <= epsilon)
    accuracy = (correct_predictions / len(predictions)) * 100
    return accuracy


def plot_3d_separation_plane(testing_set, result, perceptron):
    x1_values = [item[0] for item in testing_set]
    x2_values = [item[1] for item in testing_set]
    x3_values = [item[2] for item in testing_set]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(x1_values, x2_values, x3_values, c=result, cmap='viridis')

    w1, w2, w3 = perceptron.weights[1], perceptron.weights[2], perceptron.weights[3]
    w0 = perceptron.weights[0]
    xx, yy = np.meshgrid(np.linspace(min(x1_values), max(x1_values), 100), np.linspace(min(x2_values), max(x2_values), 100))
    zz = -(w1*xx + w2*yy + w0) / w3
    ax.plot_surface(xx, yy, zz, color='red', alpha=0.5)

    ax.set_xlabel('x1')
    ax.set_ylabel('x2')
    ax.set_zlabel('x3')

    plt.show()