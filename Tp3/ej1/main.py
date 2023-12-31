import json
from perceptron import SimpleStepPerceptron
from utils import get_config_params, get_input_data, get_expected_outputs

if __name__ == "__main__":
    with open('./config.json', 'r') as f:
        config = json.load(f)

    operation, learning_rate, max_epochs, bias = get_config_params(config)

    perceptron = SimpleStepPerceptron(learning_rate, bias)

    correct_predictions = 0 
    input_data = get_input_data()
    expected_outputs = get_expected_outputs(operation)

    perceptron.train(input_data, expected_outputs, max_epochs)

    print("    Input     | Expected  | Output")
    for i in range(len(input_data)):
        result = perceptron.run(input_data[i])
        input_str = f'{input_data[i]}'.center(13)
        expected_str = f'{expected_outputs[i]}'.center(9)
        result_str = f'{result}'.rjust(3)
        print(f'{input_str} | {expected_str} | {result_str}')
        if result == expected_outputs[i]:
            correct_predictions += 1

    perceptron.plot_final(operation, input_data, expected_outputs)

    perceptron.plot_evolution(operation, input_data, expected_outputs)


    accuracy = (correct_predictions / len(input_data)) * 100
    print(f'\nAccuracy: {accuracy}%')


