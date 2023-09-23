import json
import numpy as np
from utils import get_config_params, get_data, PERCEPTRON_TYPES
from perceptron import SimpleLinealPerceptron, SimpleHiperbolicPerceptron, SimpleLogisticPerceptrion

def initialize_perceptron(perceptron_type, learning_rate, bias, input_size):
    if perceptron_type == PERCEPTRON_TYPES[0]:
        return SimpleLinealPerceptron(learning_rate, None, bias, input_size)
    elif perceptron_type == PERCEPTRON_TYPES[1]:
        return SimpleHiperbolicPerceptron(learning_rate, None, bias, input_size)
    elif perceptron_type == PERCEPTRON_TYPES[2]:
        return SimpleLogisticPerceptrion(learning_rate, None, bias, input_size)


if __name__ == "__main__":
    with open('./config.json', 'r') as f:
        config = json.load(f)

    perceptron_type, learning_rate, training_amount, max_epochs, bias = get_config_params(config)

    input_data, expected_data = get_data()

    training_set = input_data[:training_amount].tolist()
    testing_set = input_data[training_amount:].tolist()

    perceptron = initialize_perceptron(perceptron_type, learning_rate, bias, len(training_set[0]))

    perceptron.train(training_set, expected_data[:training_amount], max_epochs)


