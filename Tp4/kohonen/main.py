import json
from kohonen import KohonenNetwork
from utils import get_config_params, get_data, standarize_data
from plots import plot_heatmap, plot_unified_distance_heatmap, plot_one_variable_heatmap

if __name__ == "__main__":
    with open('./config.json', 'r') as f:
        config = json.load(f)

    k, learning_rate, initial_radius, max_epochs, likeness_type = get_config_params(config)

    countries, labels, data = get_data()

    standarized_data = standarize_data(data)

    # Inicializa la red con kxk neuronas
    network = KohonenNetwork(standarized_data, len(standarized_data), k, learning_rate, initial_radius, likeness_type)

    n = len(standarized_data[0])

    # Entrena la red
    network.train(max_epochs)

    plot_heatmap(network, standarized_data, countries)
    plot_unified_distance_heatmap(network.get_unified_distance_matrix(), k)

    # for i in range(len(standarized_data[0])):
    #     plot_one_variable_heatmap(network, standarized_data, labels, i)

    


