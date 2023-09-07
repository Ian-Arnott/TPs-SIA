from character_class import Archer, Warrior, Defender, Infiltrator
from character import Character
from selection import elite, deterministic_tournament, probabilistic_tournament, roulette, universal, ranking, boltzmann


def generate_start_population(N, character_type):
    character_classes = {
        "archer": Archer,
        "warrior": Warrior,
        "defender": Defender,
        "infiltrator": Infiltrator
    }

    if character_type not in character_classes:
        raise ValueError(f"Invalid character_type: {character_type}")

    population = [Character(character_classes[character_type]) for _ in range(N)]

    return population


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
    if method == "boltzmann":
        return boltzmann(population, n, k, generation)