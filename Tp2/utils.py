import crossover
import mutation
import new_generation

CROSSOVER_METHODS = ["one_point", "double_point", "uniform", "anular"]
CROSSOVER_METHODS_MAP = {
    "one_point": crossover.one_point_crossover,
    "double_point": crossover.two_point_crossover,
    "uniform": crossover.uniform_crossover,
    "anular": crossover.anular_crossover
}
SELECTION_METHODS = ["elite", "roulette", "universal", "boltzmann", "deterministic_tournament", "probabilistic_tournament", "ranking"]

MUTATION_METHODS = ["gene_mutation","uniform_multigen", "complete_mutation", "limited_multigen"]
MUTATION_METHODS_MAP = {
    "gene_mutation": mutation.gene_mutation,
    "uniform_multigen": mutation.uniform_multigen,
    "complete_mutation": mutation.complete_mutation,
    "limited_multigen": mutation.limited_multigen
}

GENES = ["items", "class", "height"]

NEW_GENERATION_METHODS = ["use_all", "new_over_actual"]
NEW_GENERATION_METHODS_MAP = {
    "use_all": new_generation.use_all,
    "new_over_actual": new_generation.new_over_actual,

}

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

    crossover_method = config["crossing_method"]
    validate_method(crossover_method, CROSSOVER_METHODS, "crossing")

    selection_methods = [config["selection_method_1"], config["selection_method_2"], config["selection_method_3"], config["selection_method_4"]]
    for method in selection_methods:
        validate_method(method, SELECTION_METHODS, "selection")

    mutation_method = config["mutation_method"]
    validate_method(mutation_method, MUTATION_METHODS, "mutation")

    # elegir el gen que se muta en la funcion gene_mutation
    gene = config["gene"]
    validate_method(gene, GENES, "gene")

    A = config["A"]
    validate_selection_params(A, 1, "A")

    B = config["B"]
    validate_selection_params(B, 1, "B")

    p_m = config["p_m"]

    return N, K, M, threshold,character_type, CROSSOVER_METHODS_MAP[crossover_method], selection_methods[0], selection_methods[1], \
    selection_methods[2], selection_methods[3], MUTATION_METHODS_MAP[mutation_method], gene, A, B, p_m