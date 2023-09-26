import json
from mlp import train, predict
from utils import get_config_params, get_data, get_training_amount, PERCEPTRON_TYPES

if __name__ == "__main__":
    with open('./config.json', 'r') as f:
        config = json.load(f)

    perceptron_type, learning_rate, training_percentage, max_epochs, bias, beta, epsilon = get_config_params(config)

    input_data, expected_data = get_data()

    training_amount = get_training_amount(len(input_data), training_percentage)

    training_set = input_data[:training_amount].tolist()
    testing_set = input_data[training_amount:].tolist()