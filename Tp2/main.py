import json
import math
from utils import get_config_params
from character import Character
from genetic import generate_start_population
from crossover import anular_crossover
from selection import elite, deterministic_tournament, probabilistic_tournament, roulette, universal, ranking, boltzmann

def select(method, population, n, k, m, thr, generation):
    if method == "elite":
        return elite(population, n, k)
    if method == "roulette":
        return roulette(population, n, k)
    if method == "universal":
        return universal(population, n, k)
    if method == "ranking":
       return ranking(population, n, k)
    if method == "deterministic_tournament":
        return deterministic_tournament(population, k, m)
    if method == "probabilistic_tournament":
        return probabilistic_tournament(population, k, thr)
    if method == boltzmann:
        return boltzmann(population, n, k, generation)

if __name__ == "__main__":
    with open('./config.json', 'r') as f:
        config = json.load(f)

    n, k, m, threshold, character_type, crossover_method, selection_method_1, selection_method_2, selection_method_3, gene, selection_method_4, mutation_method, A, B, p_m = get_config_params(
        config)

    # 1. Generate start population
    start_population = generate_start_population(n, character_type)

    i:int = 0
    generation = 0 
    previous_population = start_population
    while i < 100:  #TODO: Cambiar a parámetros de corte
        # 2. Generate new population
        method1_count = math.ceil(A * k)
        method2_count = k - method1_count

        method1_selection = select(selection_method_1, previous_population, n, method1_count, m, threshold, generation)
        method2_selection = select(selection_method_2, previous_population, n, method2_count, m, threshold, generation)
        selected_population = method1_selection + method2_selection
        print("Selected population size: " + str(len(selected_population)))

        # 3. Crossover
        children = []
        for i in range(0, k, 2):
            #print(str(i) + ", " + str(i+1))
            child_1_genotype, child_2_genotype = anular_crossover(selected_population[i], selected_population[i+1])
            children.append(Character.from_genotype(child_1_genotype))
            children.append(Character.from_genotype(child_2_genotype))

        # 4. Mutation
        mutation_method(children, p_m, gene)

        # 5. #TODO: Replacement
        method3_count = math.ceil(B * n)
        method4_count = n - method3_count
        parents_and_children = previous_population + children

        print("\n\n\nParents and children size: " + str(len(parents_and_children)))
        i = 0
        for c in parents_and_children:
            print("i: "  + str(i))
            i += 1
            print(c)

        method3_selection = select(selection_method_3, parents_and_children, n + k, method3_count, m, threshold, generation)
        method4_selection = select(selection_method_4, parents_and_children, n + k, method4_count, m, threshold, generation)
        # El array final deberia tener nuevamente n individuos despues del reemplazo

        previous_population = method3_selection + method4_selection #TODO: Reemplazo

        generation += 1
        i += 1
    
