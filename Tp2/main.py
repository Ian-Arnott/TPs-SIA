import json
from utils import get_config_params
import genetic
from character import Character

if __name__ == "__main__":
    with open('./config.json', 'r') as f:
        config = json.load(f)
    
    N, K, character_type, crossing_method, selection_method, mutation_method, A, B = get_config_params(config)

    start_population = genetic.generate_start_population(N, character_type)

    # count = 0
    # for character in start_population:
    #     print(f"{character_type} {count}")
    #     print(character.get_performance())
    #     print(character)
    #     count += 1
    
    
    print(start_population[0].get_genotype());
    print(start_population[1].get_genotype());

    gen1, gen2 = genetic.anular_crossover(start_population[0], start_population[1]);

    print(gen1);
    print(gen2);

    print(Character.from_genotype(gen1));
    print(Character.from_genotype(gen2));

