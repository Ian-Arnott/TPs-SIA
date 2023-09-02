from character import Archer, Warrior, Defender, Infiltrator

def generate_start_population(N, character_type):
    character_classes = {
        "archer": Archer,
        "warrior": Warrior,
        "defender": Defender,
        "infiltrator": Infiltrator
    }

    if character_type not in character_classes:
        raise ValueError(f"Invalid character_type: {character_type}")

    population = [character_classes[character_type]() for _ in range(N)]
    
    return population
