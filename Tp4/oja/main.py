import json
from utils import get_config_params, get_data, standarize_data
from oja import OjaNetwork

if __name__ == "__main__":
    with open('./config.json', 'r') as f:
        config = json.load(f)

    learning_rate, max_epochs = get_config_params(config)

    countries, labels, data = get_data()

    standarized_data = standarize_data(data)

    oja = OjaNetwork(learning_rate, len(standarized_data[0]))

    weights = oja.train(standarized_data, max_epochs)

    print("Weights Oja:")
    print(weights)