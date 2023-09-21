import json
from utils import get_config_params

if __name__ == "__main__":
    with open('./config.json', 'r') as f:
        config = json.load(f)

    perceptron_type, learning_rate, max_epochs, bias = get_config_params(config)