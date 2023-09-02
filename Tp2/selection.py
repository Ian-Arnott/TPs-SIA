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


def roulette(population, n, k):
    sum_fitness = sum([character.get_performance() for character in population])

    if k <= n:
        new_population = population[:k]

    else:
        new_population = []
        for i in range(k):
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
