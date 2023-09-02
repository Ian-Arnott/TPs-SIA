import random
import math

def one_point_crossover(parent1: list[float], parent2:list[float]) -> tuple[list[float], list[float]]:
    genes1 = parent1.get_genotype()
    genes2 = parent2.get_genotype()

    p = random.randint(0, len(genes1) - 1)
    print("Crossover point: ", str(p))

    child1 = genes1[:p] + genes2[p:]
    child2 = genes2[:p] + genes1[p:]

    return child1, child2

def two_point_crossover(parent1: list[float], parent2: list[float]) -> tuple[list[float], list[float]]:
    genes1 = parent1.get_genotype()
    genes2 = parent2.get_genotype()

    p1 = random.randint(0, len(genes1) - 1)
    p2 = random.randint(0, len(genes1) - 1)

    if p1 > p2:
        p1, p2 = p2, p1

    child1 = genes1[:p1] + genes2[p1:p2] + genes1[p2:]
    child2 = genes2[:p1] + genes1[p1:p2] + genes2[p2:]

    return child1, child2

def uniform_crossover(parent1: list[float], parent2: list[float]) -> tuple[list[float], list[float]]:
    genes1 = parent1.get_genotype()
    genes2 = parent2.get_genotype()

    child1 = []
    child2 = []

    for i in range(len(genes1)):
        if random.random() < 0.5:
            child1.append(genes1[i])
            child2.append(genes2[i])
        else:
            child1.append(genes2[i])
            child2.append(genes1[i])

    return child1, child2

def anular_crossover(parent1: list[float], parent2: list[float]) -> tuple[list[float], list[float]]:
    genes1 = parent1.get_genotype()
    genes2 = parent2.get_genotype()

    p = random.randint(0, len(genes1) - 1)
    length = random.randint(0, math.ceil(len(genes1)/2))
    length = min(length, len(genes1) - p)

    print("Crossover point: ", str(p))
    print("Length: ", str(length))

    child1 = genes1[:p] + genes2[p:p+length] + genes1[p+length:]
    child2 = genes2[:p] + genes1[p:p+length] + genes2[p+length:]
    
    return child1, child2