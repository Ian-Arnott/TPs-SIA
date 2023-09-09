import math
import random
from utils import get_boltzmann_params


def elite(population, n, k):        
    population.sort(key=lambda x: x.get_performance(), reverse=True)

    if k >= n: #TODO: no seria k >= n ? 
        new_population = population[:k]
    else:
        new_population = []
        for i in range(k):
            repetitions = math.ceil((k - i) / n)
            for _ in range(repetitions):
                if len(new_population) == k:
                    return new_population
                new_population.append(population[i])

    return new_population


def roulette(population, n, k):
    # sum_fitness = sum([character.get_performance() for character in population])

    # if k >= n:
    #     new_population = population[:k]

    # else:
    #     new_population = []
    #     for _ in range(k):
    #         rnd = random.uniform(0, sum_fitness)
    #         sum_aux = 0

    #         for j in population:
    #             sum_aux += j.get_performance()
    #             if sum_aux >= rnd:
    #                 new_population.append(j)
    #                 break
    # Calculate relative fitness p_j
    total_fitness = sum(character.get_performance() for character in population)
    relative_fitness = [character.get_performance() / total_fitness for character in population]

    # Calculate cumulative relative fitness q_i
    cumulative_fitness = [sum(relative_fitness[:i+1]) for i in range(len(relative_fitness))]
    new_population = []
    for _ in range(k):
        r_j = random.uniform(0, 1)

        # Find the index i where q_i-1 < r_j <= q_i
        for i, q_i in enumerate(cumulative_fitness):
            if i == 0 and 0 <= r_j <= q_i:
                new_population.append(population[i])
                break
            elif cumulative_fitness[i-1] < r_j <= q_i:
                new_population.append(population[i])
                break

    return new_population


def universal(population, n, k):
    # if k >= n:
    #     new_population = population[:k]

    # else:
    #     new_population = []

    #     for i in range(k):
    #         rnd = random.uniform(0, 1)
    #         r = (rnd + i) / k
    #         p = roulette(population, n, r)
    #         new_population.extend(p)
    new_population = []
    for j in range(k):
        r_j = (random.uniform(0, 1) + j) / k

        # Calculate relative fitness p_j
        total_fitness = sum(character.get_performance() for character in population)
        relative_fitness = [character.get_performance() / total_fitness for character in population]

        # Calculate cumulative relative fitness q_i
        cumulative_fitness = [sum(relative_fitness[:i+1]) for i in range(len(relative_fitness))]

        # Find the index i where q_i-1 < r_j <= q_i
        for i, q_i in enumerate(cumulative_fitness):
            if i == 0 and 0 <= r_j <= q_i:
                new_population.append(population[i])
                break
            elif cumulative_fitness[i-1] < r_j <= q_i:
                new_population.append(population[i])
                break

    return new_population


def deterministic_tournament(population, k, m):
    new_population = []

    for _ in range(k):
        selected_characters = random.sample(population, m)
        selected_characters.sort(key=lambda x: x.get_performance(), reverse=True)
        new_population.append(selected_characters[0])

    return new_population


def probabilistic_tournament(population, k, thr):
    new_population = []

    for _ in range(k):
        selected_characters = random.sample(population, 2)
        r = random.uniform(0, 1)
        selected_characters.sort(key=lambda x: x.get_performance(), reverse=True)
        if r < thr:
            new_population.append(selected_characters[0])
        else:
            new_population.append(selected_characters[1])

    return new_population

def _calculate_temperature(i):
    Tc, T0, k = get_boltzmann_params()
    return Tc + (T0-Tc)*math.exp(-k*i)


def boltzmann(population, n, k, generation):
    temperature = _calculate_temperature(generation)
    new_population = []

    for _ in range(k):
        
        maxPerformance = max([individual.get_performance() for individual in population])
        scaledPerformances = [(individual.get_performance() - maxPerformance) for individual in population]
        probabilities = [math.exp(performance / temperature) for performance in scaledPerformances]
        # probabilities = [math.exp(individual.get_performance() / temperature) for individual in population] # e^(fitness(i)/temperature)	

        total_probability = sum(probabilities)
        expected_value = [p / total_probability for p in probabilities]
        
        selected_index = random.choices(range(n), weights=expected_value, k=1)[0]
        selected_individual = population[selected_index]

        new_population.append(selected_individual)

    return new_population


def ranking(population, n, k):
    new_population = []
    population.sort(key=lambda x: x.get_performance(), reverse=True)

    rankings = []
    total = 0

    for i in range(n):
        pseudo_fitness = (n - (i-1))/n
        rankings.append(pseudo_fitness)
        total += pseudo_fitness

    rankings = [r / total for r in rankings]
    
    new_population = random.choices(population, weights=rankings, k=k)

    return new_population