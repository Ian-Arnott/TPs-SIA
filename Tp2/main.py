import json
from utils import get_config_params
from character import Character
from genetic import generate_start_population
from crossover import anular_crossover
from selection import elite, deterministic_tournament, probabilistic_tournament, roulette, universal
from mutation import uniform_multigen, limited_multigen, complete_mutation

if __name__ == "__main__":
    with open('./config.json', 'r') as f:
        config = json.load(f)

    n, k, m, threshold, character_type, crossing_method, selection_method, mutation_method, A, B, p_m = get_config_params(
        config)

    start_population = generate_start_population(n, character_type)
    print("Start population:")
    for i in range(n):
        print(start_population[i].get_performance())
    # ======================== CROSSOVER ========================
    # print(start_population[0].get_genotype());
    # print(start_population[1].get_genotype());

    # gen1, gen2 = anular_crossover(start_population[0], start_population[1]);

    # print(gen1);
    # print(gen2);

    # print(Character.from_genotype(gen1));
    # print(Character.from_genotype(gen2));

    # ======================== MUTATION  ========================
    # uniform_multigen(start_population, p_m)
    # complete_mutation(start_population, p_m)
    limited_multigen(start_population,p_m)
    
    # ======================== SELECTION ========================
    # print("\nElite:")
    # new_population = elite(start_population, n, k)

    # print("\nTournament Deterministic:")
    # new_population = deterministic_tournament(start_population, k, m)

    # print("\nTournament Probabilistic:")
    # new_population = probabilistic_tournament(start_population, k, threshold)

    print("\nRoulette:")
    new_population = roulette(start_population, n, k)

    # print("\nUniversal:")
    # new_population = universal(start_population, n, k)

    for i in range(k):
        print(new_population[i].get_performance())
