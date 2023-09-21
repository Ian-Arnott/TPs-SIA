from perceptron_test import SimpleStepPerceptron

input_data =  [[-1, 1], [1, -1], [-1, -1], [1, 1]]
expected_outputs = [-1, -1, -1, 1]

perceptron = SimpleStepPerceptron(0.01)

perceptron.train(input_data, expected_outputs, limit=500)

test_data =  [[-1, 1], [1, -1], [-1, -1], [1, 1]]
correct_predictions = 0 

for i in range(len(test_data)):
    result = perceptron.run(test_data[i])
    print(f'Input: {test_data[i]}, Expected:{expected_outputs[i]}, Output: {result}')
    if result == expected_outputs[i]:
        correct_predictions += 1

accuracy = (correct_predictions / len(test_data)) * 100
print(f'Accuracy: {accuracy}%')
