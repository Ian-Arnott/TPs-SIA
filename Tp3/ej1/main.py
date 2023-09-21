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

    perceptron.train(operation, input_data, expected_outputs, max_epochs)

    for i in range(len(input_data)):
        result = perceptron.run(input_data[i])
        print(f'Input: {input_data[i]}, Expected:{expected_outputs[i]}, Output: {result}')
        if result == expected_outputs[i]:
            correct_predictions += 1

    perceptron.plot(operation, input_data, expected_outputs)

    accuracy = (correct_predictions / len(input_data)) * 100
    print(f'Accuracy: {accuracy}%')


