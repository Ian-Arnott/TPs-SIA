import selection

CROSSING_METHODS = ["one_point", "double_point", "uniform", "anular"]
SELECTION_METHODS = ["elite", "roulette", "universal", "boltzmann", "deterministic_tournament", "probabilistic_tournament", "ranking"]
MUTATION_METHODS = ["one_gen", "multigen"]
CHARACTER_TYPES = ["warrior", "archer", "defender", "infiltrator"]

SELECTION_METHODS_MAP = {
    "elite": selection.elite,
    "roulette": selection.roulette,
    "universal": selection.universal,
    "boltzmann": selection.boltzmann,
    "deterministic_tournament": selection.deterministic_tournament,
    "probabilistic_tournament": selection.probabilistic_tournament,
    # "ranking"
}

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

    # selection_method_1 = config["selection_method_1"]
    # validate_method(selection_method_1, SELECTION_METHODS, "selection")

    # selection_method_2 = config["selection_method_2"]
    # validate_method(selection_method_2, SELECTION_METHODS, "selection")

    # selection_method_3 = config["selection_method_3"]
    # validate_method(selection_method_3, SELECTION_METHODS, "selection")

    # selection_method_4 = config["selection_method_4"]
    # validate_method(selection_method_4, SELECTION_METHODS, "selection")
    selection_methods = [config["selection_method_1"], config["selection_method_2"], config["selection_method_3"], config["selection_method_4"]]
    for method in selection_methods:
        validate_method(method, SELECTION_METHODS, "selection")


    mutation_method = config["mutation_method"]
    validate_method(mutation_method, MUTATION_METHODS, "mutation")

    A = config["A"]
    validate_selection_params(A, K, "A")

    B = config["B"]
    validate_selection_params(B, K, "B")

    p_m = config["p_m"]


    return N, K, M, threshold,character_type, crossing_method, selection_methods[0], selection_methods[1], \
    selection_methods[2], selection_methods[3], mutation_method, A, B, p_m