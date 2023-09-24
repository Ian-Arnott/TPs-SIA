import json
import matplotlib.pyplot as plt
import numpy as np
from utils import get_config_params, get_data, PERCEPTRON_TYPES
from perceptron import SimpleLinealPerceptron, SimpleHiperbolicPerceptron, SimpleLogisticPerceptrion



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

def calculate_accuracy(predictions, expected, epsilon):
    correct_predictions = sum(1 for p, gt in zip(predictions, expected) if abs(p - gt) <= epsilon)
    accuracy = (correct_predictions / len(predictions)) * 100
    return accuracy

if __name__ == "__main__":
    with open('./config.json', 'r') as f:
        config = json.load(f)

    perceptron_type, learning_rate, training_amount, max_epochs, bias, beta, epsilon = get_config_params(config)

    input_data, expected_data = get_data()

    training_set = input_data[:training_amount].tolist()
    testing_set = input_data[training_amount:].tolist()

    perceptron = initialize_perceptron(perceptron_type, beta, learning_rate, bias, len(training_set[0]),epsilon)

    perceptron.train(training_set, expected_data[:training_amount], max_epochs)

    correct_predictions = 0 

    if(perceptron_type == PERCEPTRON_TYPES[0]): # LINEAR
        result = perceptron.predict(testing_set)
    else:
        # Escalo los resultados para que se ajusten al intervalo de entrenamiento
        # TODO: Habria que hacerlo para [entrenamiento + testeo]?
        result = perceptron.predict(testing_set, should_scale=True, scale_interval=min_max_interval(expected_data))

    for i in range(len(result)):
        print(f'Result: {result[i]} - Expected: {expected_data[i+training_amount]} - Delta: {abs(result[i] - expected_data[i+training_amount])}')

    #     plt.scatter(i, result[i], color='blue', label='Result')
    #     plt.scatter(i, expected_data[i+training_amount], color='red', label='Expected')

    # plt.xlabel('Sample')
    # plt.ylabel('Value')
    # plt.show()


    accuracy = calculate_accuracy(result, expected_data[training_amount:],epsilon)
    print(f'Accuracy: {accuracy}%')
