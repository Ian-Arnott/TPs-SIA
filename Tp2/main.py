import json
from utils import get_config_params

if __name__ == "__main__":
    with open('./config.json', 'r') as f:
        config = json.load(f)
    
    N, K, crossing_method, selection_method, mutation_method = get_config_params(config)

    print(N, K, crossing_method, selection_method, mutation_method)