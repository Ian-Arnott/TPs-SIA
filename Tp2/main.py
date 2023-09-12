import json
import math
from utils import get_config_params
from character import Character
from genetic import generate_start_population, select, check_end_condition

if __name__ == "__main__":
    with open('./config.json', 'r') as f:
        config = json.load(f)

    n, k, m, threshold, character_type, crossover_method, selection_method_1, selection_method_2, \
        selection_method_3, selection_method_4, mutation_method, new_generation_method, gene, \
            A, B, p_m, max_generations, max_generations_without_change, delta, optimal_fitness, optimal_fitness_error = get_config_params(config)

    # 1. Generate start population
    start_population = generate_start_population(n, character_type)
    end = False
    end_condition = None
    generation = 0
    generations_without_change = 0 
    previous_population = start_population
    while not end:
        print("Generation " + str(generation))

        # 2. Generate new population
        method1_count = math.ceil(A * k)
        method2_count = k - method1_count

        method1_selection = select(selection_method_1, previous_population, n, method1_count, m, threshold, generation)
        method2_selection = select(selection_method_2, previous_population, n, method2_count, m, threshold, generation)
        selected_population = method1_selection + method2_selection

        # 3. Crossover
        children = []
        for j in range(0, k, 2):
            child_1_genotype, child_2_genotype = crossover_method(selected_population[j], selected_population[j+1])
            children.append(Character.from_genotype(child_1_genotype))
            children.append(Character.from_genotype(child_2_genotype))

        # 4. Mutation
        mutation_method(children, p_m, gene)

        # 5. Replacement
        method3_count = math.ceil(B * n)
        method4_count = n - method3_count
        parents_and_children = previous_population + children


        method3_selection = select(selection_method_3, parents_and_children, n + k, method3_count, m, threshold, generation)
        method4_selection = select(selection_method_4, parents_and_children, n + k, method4_count, m, threshold, generation)
        # El array final deberia tener nuevamente n individuos despues del reemplazo

        previous_population = method3_selection + method4_selection

        new_population = new_generation_method(previous_population, children, k, n)

        end, end_condition, generations_without_change = check_end_condition(previous_population, new_population, generation, generations_without_change, max_generations, max_generations_without_change, delta, optimal_fitness, optimal_fitness_error)

        previous_population = new_population

        generation += 1

    
    print("Finished algorithm by end condition: " + end_condition)
    max = {"p":0, "class":"","items":None}
    for p in previous_population:
        if p.get_performance() > max["p"]:
            max["p"] = p.get_performance()
            max["class"] = p._class
            max["items"] = p._items
    print(max)



def run_main(config):

    n, k, m, threshold, character_type, crossover_method, selection_method_1, selection_method_2, \
        selection_method_3, selection_method_4, mutation_method, new_generation_method, gene, \
            A, B, p_m, max_generations, max_generations_without_change, delta, optimal_fitness, optimal_fitness_error = get_config_params(config)

    # 1. Generate start population
    start_population = generate_start_population(n, character_type)
    end = False
    end_condition = None
    generation = 0
    generations_without_change = 0 
    previous_population = start_population
    while not end:

        # 2. Generate new population
        method1_count = math.ceil(A * k)
        method2_count = k - method1_count

        method1_selection = select(selection_method_1, previous_population, n, method1_count, m, threshold, generation)
        method2_selection = select(selection_method_2, previous_population, n, method2_count, m, threshold, generation)
        selected_population = method1_selection + method2_selection

        # 3. Crossover
        children = []
        for j in range(0, k, 2):
            child_1_genotype, child_2_genotype = crossover_method(selected_population[j], selected_population[j+1])
            children.append(Character.from_genotype(child_1_genotype))
            children.append(Character.from_genotype(child_2_genotype))

        # 4. Mutation
        mutation_method(children, p_m, gene)

        # 5. Replacement
        method3_count = math.ceil(B * n)
        method4_count = n - method3_count
        parents_and_children = previous_population + children


        method3_selection = select(selection_method_3, parents_and_children, n + k, method3_count, m, threshold, generation)
        method4_selection = select(selection_method_4, parents_and_children, n + k, method4_count, m, threshold, generation)
        # El array final deberia tener nuevamente n individuos despues del reemplazo

        previous_population = method3_selection + method4_selection

        new_population = new_generation_method(previous_population, children, k, n)

        end, end_condition, generations_without_change = check_end_condition(previous_population, new_population, generation, generations_without_change, max_generations, max_generations_without_change,delta, optimal_fitness, optimal_fitness_error)

        previous_population = new_population

        generation += 1

    max = {"p":None, "perf":0}
    for p in previous_population:
        if p.get_performance() > max["perf"]:
            max["perf"] = p.get_performance()
            max["p"] = p
    return max["p"], generation