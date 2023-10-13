import json
from utils import get_config_params

if __name__ == "__main__":
    with open('./kohonen_config.json', 'r') as f:
        config = json.load(f)

    radio = get_config_params(config)
