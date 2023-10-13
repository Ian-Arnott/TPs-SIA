import json
from utils import get_config_params, get_data, standarize_data

if __name__ == "__main__":
    with open('./kohonen_config.json', 'r') as f:
        config = json.load(f)

    radius, max_epochs = get_config_params(config)

    countries, labels, data = get_data()

    standarize_data = standarize_data(data)

    # print("Countries: ", countries)
    # print("Labels: ", labels)
    # print("Data: ", data)
    # print("Standarized Data:", standarize_data(data))

