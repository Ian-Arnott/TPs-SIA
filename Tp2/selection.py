import math
import random

def elite(population, n, k):
    population.sort(key=lambda x: x.get_performance(), reverse=True)

    if k <= n:
        new_population = population[:k]
    else:    
        new_population = []
        for i in range(k):
            repetitions = math.ceil((k - i) / n)
            # print(f"i {i} | n(i) = {repetitions}")
            for _ in range(repetitions):
                if len(new_population) == k:
                    return new_population
                new_population.append(population[i])
            
    return new_population

def deterministic_tournament(population, k, m):
    new_population = []

    for _ in range(k):
        selected_characters = random.sample(population, m)
        selected_characters.sort(key=lambda x: x.get_performance(), reverse=True)
        new_population.append(selected_characters[0])

    return new_population