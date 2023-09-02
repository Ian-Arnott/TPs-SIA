import math

def elite(population, k):
    n = population.size
    population = sorted(population)

    # CHECK: el segundo caso resuelve el primero??
    if k <= n:
        new_population = population[:k]
    else:     
        for i in range(n):
            repetitions = math.ceil((k - i) / n)
            new_population = population
            for _ in range(repetitions):
                if len(new_population) == k:
                    return new_population
                new_population.append(population[i])

    return new_population
