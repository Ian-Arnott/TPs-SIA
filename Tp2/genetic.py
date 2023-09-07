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


def check_structural_end_condition(population, previous_population, delta):
    #TODO: ver si esto sirve como corte por estructura o es mas por contenido
    avg_performance = sum([character.get_performance() for character in population]) / len(population)
    avg_previous_performance = sum([character.get_performance() for character in previous_population]) / len(previous_population)
    return abs(avg_performance - avg_previous_performance) < delta


def check_end_condition(population, previous_population, generation, generations_without_change, max_generations, max_generations_without_change, delta):

    if (generation >= max_generations):
        return True, "Max generations reached", generations_without_change
    
    if check_structural_end_condition(population, previous_population, delta):
        if generations_without_change >= max_generations_without_change:
            return True, "Structural end condition reached", generations_without_change
        else:
            return False, None, generations_without_change + 1

    return False, None, generations_without_change