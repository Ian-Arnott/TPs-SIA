import json
from utils import get_config_params, get_data, get_training_amount, PERCEPTRON_TYPES
from perceptron_utils import initialize_perceptron, calculate_accuracy, min_max_interval


def run_main(config):
    perceptron_type, learning_rate, training_percentage, max_epochs, bias, beta, epsilon = get_config_params(config)

    input_data, expected_data = get_data()

    training_amount = get_training_amount(len(input_data), training_percentage)

    training_set = input_data[:training_amount].tolist()
    testing_set = input_data[training_amount:].tolist()

    perceptron = initialize_perceptron(perceptron_type, beta, learning_rate, bias, len(training_set[0]),epsilon)

    epoch = 0
    mse = []
    result = []

    if(perceptron_type == PERCEPTRON_TYPES[0]): # LINEAR
        epoch, mse = perceptron.train(training_set, expected_data[:training_amount], max_epochs)
        result, test_mse = perceptron.predict(testing_set)
    else:
        epoch, mse = perceptron.train(training_set, expected_data[:training_amount], max_epochs, should_scale=True)
        result, test_mse = perceptron.predict(testing_set, should_scale=True, scale_interval=min_max_interval(expected_data))

    return epoch, mse, test_mse



if __name__ == "__main__":
    with open('./config.json', 'r') as f:
        config = json.load(f)

    perceptron_type, learning_rate, training_percentage, max_epochs, bias, beta, epsilon = get_config_params(config)

    input_data, expected_data = get_data()

    training_amount = get_training_amount(len(input_data), training_percentage)

    training_set = input_data[:training_amount].tolist()
    testing_set = input_data[training_amount:].tolist()

    perceptron = initialize_perceptron(perceptron_type, beta, learning_rate, bias, len(training_set[0]),epsilon)

    correct_predictions = 0 

    if(perceptron_type == PERCEPTRON_TYPES[0]): # LINEAR
        epochs, mse = perceptron.train(training_set, expected_data[:training_amount], max_epochs)
        result, test_mse = perceptron.predict(testing_set)
    else:
        epochs, mse = perceptron.train(training_set, expected_data[:training_amount], max_epochs, should_scale=True)
        result, test_mse = perceptron.predict(testing_set, should_scale=True, scale_interval=min_max_interval(expected_data))

    correct_predictions = 0

    print("Expected         | Expected_Scaled    | Result            | Delta")
    print("------------------------------------------------------------------")
    for i in range(len(result)):
        expected_str = f'{expected_data[i+training_amount]}'.ljust(16)

        if(perceptron_type != PERCEPTRON_TYPES[0]): # LINEAR
            expected_scaled = perceptron.scale_result(expected_data[i+training_amount],min(expected_data),max(expected_data))
        else:
            expected_scaled = expected_data[i+training_amount]

        expected_scaled_str = f'{expected_scaled:.3f}'.ljust(18)
        result_str = f'{result[i]:.3f}'.ljust(17)
        delta_str = f'{abs(result[i] - expected_scaled):.3f}'.ljust(15)
        print(f'{expected_str} | {expected_scaled_str} | {result_str} | {delta_str}')
        
        if(abs(result[i] - expected_scaled) <= epsilon):
            correct_predictions += 1
    
    print(f'Correct predictions: {correct_predictions} out of {len(result)}')
    print(f'Training Error: {mse[len(mse)-1]}')
    print(f'Testing Error: {test_mse}')



