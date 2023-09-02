import json
from utils import get_config_params
from genetic import generate_start_population

if __name__ == "__main__":
    with open('./config.json', 'r') as f:
        config = json.load(f)
    
    N, K, character_type, crossing_method, selection_method, mutation_method = get_config_params(config)

    start_population = generate_start_population(N, character_type)

    count = 0
    for character in start_population:
        print(f"{character_type} - {count}")
        print(character.get_performance())
        print()
        count += 1

    print(N, K, crossing_method, selection_method, mutation_method)