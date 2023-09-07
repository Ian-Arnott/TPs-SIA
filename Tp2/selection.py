import math
import random


def elite(population, n, k):        
    # print("\n\n\n\nelite:\n")
    # for character in population:
    #     print(character)

    population.sort(key=lambda x: x.get_performance(), reverse=True)

    if k <= n:
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
    sum_fitness = sum([character.get_performance() for character in population])

    if k <= n:
        new_population = population[:k]

    else:
        new_population = []
        for _ in range(k):
            rnd = random.uniform(0, sum_fitness)
            sum_aux = 0

            for j in population:
                sum_aux += j.get_performance()
                if sum_aux >= rnd:
                    new_population.append(j)
                    break

    return new_population


def universal(population, n, k):
    if k <= n:
        new_population = population[:k]

    else:
        new_population = []

        for i in range(k):
            rnd = random.uniform(0, 1)
            r = (rnd + i) / k
            p = roulette(population, n, r)
            new_population.extend(p)

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
        r = random.uniform(0.5, 1)
        selected_characters.sort(key=lambda x: x.get_performance(), reverse=True)
        if r < thr:
            new_population.append(selected_characters[0])
        else:
            new_population.append(selected_characters[1])

    return new_population

def _calculate_temperature(i):
    #TODO: agregar a config
    Tc=0.01     # Critical temperature
    T0=10       # Initial temperature
    k=2         # Decreasing factor (constant)
    return Tc + (T0-Tc)*math.exp(-k*i)


def boltzmann(population, n, k, generation):
    temperature = _calculate_temperature(generation)
    new_population = []

    for _ in range(k):
        probabilities = [math.exp(individual.fitness / temperature) for individual in population] # e^(fitness(i)/temperature)	

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