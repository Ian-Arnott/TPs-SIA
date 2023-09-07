import random

def use_all(parents, children, k, n):
    new_generation = parents + children
    return random.sample(new_generation, n)


def new_over_actual(parents, children, k, n):
    new_generation = []
    if(k > n):
        new_generation = children[:n]
    else:
        new_generation = children + parents[:(n-k)]
    return new_generation