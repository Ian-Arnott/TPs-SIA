import json
from utils import get_config_params, get_data, get_training_amount, PERCEPTRON_TYPES
from perceptron_utils import initialize_perceptron, calculate_accuracy, min_max_interval


if __name__ == "__main__":
    with open('./config.json', 'r') as f:
        config = json.load(f)

    perceptron_type, learning_rate, training_percentage, max_epochs, bias, beta, epsilon = get_config_params(config)

    input_data, expected_data = get_data()

    training_amount = get_training_amount(len(input_data), training_percentage)

    training_set = input_data[:training_amount].tolist()
    testing_set = input_data[training_amount:].tolist()

    perceptron = initialize_perceptron(perceptron_type, beta, learning_rate, bias, len(training_set[0]),epsilon)

    perceptron.train(training_set, expected_data[:training_amount], max_epochs)

    correct_predictions = 0 

    if(perceptron_type == PERCEPTRON_TYPES[0]): # LINEAR
        result = perceptron.predict(testing_set)
    else:
        # Escalo los resultados para que se ajusten al intervalo de entrenamiento
        # TODO: Habria que hacerlo para [entrenamiento + testeo]?
        result = perceptron.predict(testing_set, should_scale=True, scale_interval=min_max_interval(expected_data))

    for i in range(len(result)):
        print(f'Result: {result[i]} - Expected: {expected_data[i+training_amount]} - Delta: {abs(result[i] - expected_data[i+training_amount])}')

    #     plt.scatter(i, result[i], color='blue', label='Result')
    #     plt.scatter(i, expected_data[i+training_amount], color='red', label='Expected')

    # plt.xlabel('Sample')
    # plt.ylabel('Value')
    # plt.show()

    accuracy = calculate_accuracy(result, expected_data[training_amount:], epsilon)
    print(f'Accuracy: {accuracy}%')


def run_main(config):
    perceptron_type, learning_rate, training_percentage, max_epochs, bias, beta, epsilon = get_config_params(config)

    input_data, expected_data = get_data()

    training_amount = get_training_amount(len(input_data), training_percentage)

    training_set = input_data[:training_amount].tolist()
    testing_set = input_data[training_amount:].tolist()

    perceptron = initialize_perceptron(perceptron_type, beta, learning_rate, bias, len(training_set[0]),epsilon)

    epochs = perceptron.train(training_set, expected_data[:training_amount], max_epochs)

    if(perceptron_type == PERCEPTRON_TYPES[0]): # LINEAR
        result = perceptron.predict(testing_set)
    else:
        result = perceptron.predict(testing_set, should_scale=True, scale_interval=min_max_interval(expected_data))


    error = 0 # Mean Squared Error

    for i in range(len(result)):
        print(f'Result: {result[i]} - Expected: {expected_data[i+training_amount]} - Delta: {abs(result[i] - expected_data[i+training_amount])}')
        error += (perceptron.scale_result(result[i]) - perceptron.scale_result(expected_data[i+training_amount]))**2

    error = error / len(result) 

    return error, epochs