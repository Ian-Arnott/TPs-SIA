from character_class import Archer, Warrior, Defender, Infiltrator
from character import Character
import math
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



def standard_deviation(dataset):
    mean = sum(dataset) / len(dataset)
    variance = sum([(x - mean) ** 2 for x in dataset]) / len(dataset)
    return math.sqrt(variance)


# We define 'diversity' as the mean of the standard deviations of the stats and height of the population
def calculate_diversity(population):
    population_stats = [[], [], [], [], [], []]
    
    for character in population:
        stats = character.get_stats()
        population_stats[0].append(stats["strength"])
        population_stats[1].append(stats["agility"])
        population_stats[2].append(stats["expertise"])
        population_stats[3].append(stats["endurance"])
        population_stats[4].append(stats["health"])
        population_stats[5].append(character.get_height())
    
    standard_deviations = [standard_deviation(stat) for stat in population_stats]
    return sum(standard_deviations) / len(standard_deviations)


# def check_structural_end_condition(population, previous_population, delta):
#     avg_stats = sum([sum(character.get_stats().values()) for character in population]) / len(population)
#     avg_previous_stats = sum([sum(character.get_stats().values()) for character in previous_population]) / len(previous_population)
#     return abs(avg_stats - avg_previous_stats) < delta

def check_structural_end_condition(population, previous_population, delta):
    population_diversity = calculate_diversity(population)
    previous_population_diversity = calculate_diversity(previous_population)
    return abs(population_diversity - previous_population_diversity) < delta


def avg_performance(population):
    return sum([character.get_performance() for character in population]) / len(population)

def check_content_end_condition(population, previous_population, delta):
    pop_avg_performance = avg_performance(population)
    previous_pop_avg_performance = avg_performance(previous_population)
    return abs(pop_avg_performance - previous_pop_avg_performance) < delta

def check_optimal_fitness_end_condition(population, optimal_fitness, optimal_fitness_error):
    best_character = max(population, key=lambda character: character.get_performance())
    best_character_performance =  best_character.get_performance()
    return (optimal_fitness - optimal_fitness_error) <= best_character_performance <= (optimal_fitness + optimal_fitness_error)


def check_end_condition(population, previous_population, generation, generations_without_change, max_generations, max_generations_without_change, delta, optimal_fitness, optimal_fitness_error):

    if (generation >= max_generations):
        return True, "max_generations", generations_without_change
    
    if check_structural_end_condition(population, previous_population, delta):
        if generations_without_change >= max_generations_without_change:
            return True, "structural", generations_without_change
        else:
            return False, None, generations_without_change + 1
        
    if check_content_end_condition(population, previous_population, delta):
        if generations_without_change >= max_generations_without_change:
            return True, "content", generations_without_change
        else:
            return False, None, generations_without_change + 1
    
    if check_optimal_fitness_end_condition(population, optimal_fitness, optimal_fitness_error):
        return True, "optimal_fitness", generations_without_change    
    
    return False, None, generations_without_change