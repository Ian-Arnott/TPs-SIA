import json
from utils import get_config_params, get_data, PERCEPTRON_TYPES
from perceptron import SimpleLinealPerceptron, SimpleHiperbolicPerceptron, SimpleLogisticPerceptrion



def initialize_perceptron(perceptron_type, beta, learning_rate, bias, input_size):
    if perceptron_type == PERCEPTRON_TYPES[0]:
        return SimpleLinealPerceptron(learning_rate, None, bias, input_size)
    elif perceptron_type == PERCEPTRON_TYPES[1]:
        return SimpleHiperbolicPerceptron(beta, learning_rate, None, bias, input_size)
    elif perceptron_type == PERCEPTRON_TYPES[2]:
        return SimpleLogisticPerceptrion(beta, learning_rate, None, bias, input_size)


def min_max_interval(values:list[float]) -> tuple[float]:
    min_value = min(values)
    max_value = max(values)
    return (min_value, max_value)

if __name__ == "__main__":
    with open('./config.json', 'r') as f:
        config = json.load(f)

    perceptron_type, learning_rate, training_amount, max_epochs, bias, beta = get_config_params(config)

    input_data, expected_data = get_data()

    training_set = input_data[:training_amount].tolist()
    testing_set = input_data[training_amount:].tolist()

    perceptron = initialize_perceptron(perceptron_type, beta, learning_rate, bias, len(training_set[0]))

    perceptron.train(training_set, expected_data[:training_amount], max_epochs)

    correct_predictions = 0 

    if(perceptron_type == PERCEPTRON_TYPES[0]): # LINEAR
        result = perceptron.predict(testing_set)
    else:
        # Escalo los resultados para que se ajusten al intervalo de entrenamiento
        # TODO: Habria que hacerlo para [entrenamiento + testeo]?
        result = perceptron.predict(testing_set, should_scale=True, scale_interval=min_max_interval(expected_data[:training_amount]))

    for i in range(len(result)):
        print(f'Result: {result[i]} - Expected: {expected_data[i+training_amount]}')

    # accuracy = (correct_predictions / len(input_data)) * 100
    # print(f'\nAccuracy: {accuracy}%')
