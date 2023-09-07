import crossover
import mutation
import new_generation
import json

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

def validate_selection_params(x, str):
    if x < 0 or x > 1:
        print(f"{str} must be between 0 and 1")
        exit(1)

def validate_threshold(thr, str):
    if thr < 0.5 or thr > 1:
        print(f"{str} must be between 0.5 and 1")
        exit(1)

def get_boltzmann_params():
    with open('./config.json', 'r') as f:
        config = json.load(f)

    Tc = config["Tc"] # Critical Temperature

    T0 = config["T0"] # Initial Temperature
    validate_positive_int(T0, "T0")

    k = config["k"] # Decay constant
    validate_positive_int(k, "k")

    return Tc, T0, k
    

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

    new_generation_method = config["new_generation_method"]
    validate_method(new_generation_method, NEW_GENERATION_METHODS, "new_generation")

    # elegir el gen que se muta en la funcion gene_mutation
    gene = config["gene"]
    validate_method(gene, GENES, "gene")

    A = config["A"]
    validate_selection_params(A, "A")

    B = config["B"]
    validate_selection_params(B, "B")

    p_m = config["p_m"]

    max_generations = config["max_generations"]
    validate_positive_int(max_generations, "max_generations")

    max_generations_without_change = config["max_generations_without_change"]
    validate_positive_int(max_generations_without_change, "max_generations_without_change")

    delta = config["delta"]

    return N, K, M, threshold,character_type, CROSSOVER_METHODS_MAP[crossover_method], selection_methods[0], selection_methods[1], \
    selection_methods[2], selection_methods[3], MUTATION_METHODS_MAP[mutation_method], NEW_GENERATION_METHODS_MAP[new_generation_method], \
        gene, A, B, p_m, max_generations, max_generations_without_change, delta