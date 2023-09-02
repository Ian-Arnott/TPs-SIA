CROSSING_METHODS = ["one_point", "double_point", "uniform", "anular"]
SELECTION_METHODS = ["elite", "roulette", "universal", "boltzmann", "deterministic_tournament", "probabilistic_tournament", "ranking"]
MUTATION_METHODS = ["one_gen", "multigen"]

CHARACTER_TYPES = ["warrior", "archer", "defender", "infiltrator"]

def validate_positive_int(value, str):
    try:
        value = int(value)
        if value <= 0:
            raise ValueError
    except ValueError:
        print(f"{str} must be a positive integer")
        exit(1)    

def validate_method(value, methods, str):
    if value not in methods:
        print(f"Invalid {str} method")
        exit(1)
    

def get_config_params(config):
    N = config["N"]
    validate_positive_int(N, "N")

    K = config["K"]
    validate_positive_int(K, "K")

    character_type = config["character_type"]
    validate_method(character_type, CHARACTER_TYPES, "character_type")

    crossing_method = config["crossing_method"]
    validate_method(crossing_method, CROSSING_METHODS, "crossing")

    selection_method = config["selection_method"]
    validate_method(selection_method, SELECTION_METHODS, "selection")

    mutation_method = config["mutation_method"]
    validate_method(mutation_method, MUTATION_METHODS, "mutation")

    A = config["A"]

    if A > K:
        return -1

    B = config["B"]
    
    if B > K:
        return -1

    return N, K, character_type, crossing_method, selection_method, mutation_method, A, B