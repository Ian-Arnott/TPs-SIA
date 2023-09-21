from perceptron_test import SimpleLinearPerceptron
import numpy as np
import pandas as pd

# Load the dataset
data = pd.read_csv('Tp3/data/ej2-conjunto.csv')
X = data[['x1', 'x2', 'x3']].values
y = data['y'].values

# Define epsilon
epsilon = 0.01  # Adjust this value as needed

# Define a training set and a testing set
split_ratio = 0.8
split_idx = int(split_ratio * len(X))
X_train, y_train = X[:split_idx], y[:split_idx]
X_test, y_test = X[split_idx:], y[split_idx:]

# Instantiate and train the linear perceptron
linear_perceptron = SimpleLinearPerceptron(epsilon, learning_rate=0.01)

# Train the linear perceptron
linear_perceptron.train(X_train, y_train, limit=1000)

# Define epsilon
epsilon = 0.01  # Adjust this value as needed

# Test the linear perceptron
correct_predictions = 0 

for i in range(len(X_test)):
    result = linear_perceptron.run(X_test[i])
    print(f'Input: {X_test[i]}, Expected: {y_test[i]}, Output: {result}')
    if abs(result - y_test[i]) < epsilon:
        correct_predictions += 1

accuracy = (correct_predictions / len(X_test)) * 100
print(f'Accuracy: {accuracy}%')
