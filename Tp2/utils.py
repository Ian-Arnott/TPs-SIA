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

def validate_selection_params(x, k, str):
    if x > k:
        print(f"{str} must be greater than k={k}")
        exit(1)

def validate_threshold(thr, str):
    if thr < 0.5 or thr > 1:
        print(f"{str} must be between 0.5 and 1")
        exit(1)
    

def get_config_params(config):
    N = config["N"]
    validate_positive_int(N, "N")

    K = config["K"]
    validate_positive_int(K, "K")

    M = config["M"]
    validate_positive_int(M, "M")

    threshold = config["threshold"]
    validate_threshold(threshold, "threshold")

    character_type = config["character_type"]
    validate_method(character_type, CHARACTER_TYPES, "character_type")

    crossing_method = config["crossing_method"]
    validate_method(crossing_method, CROSSING_METHODS, "crossing")

    selection_method = config["selection_method"]
    validate_method(selection_method, SELECTION_METHODS, "selection")

    mutation_method = config["mutation_method"]
    validate_method(mutation_method, MUTATION_METHODS, "mutation")

    A = config["A"]
    validate_selection_params(A, K, "A")

    B = config["B"]
    validate_selection_params(B, K, "B")

    return N, K, M, threshold,character_type, crossing_method, selection_method, mutation_method, A, B