from perceptron_test import SimpleLinearPerceptron
import pandas as pd
from numpy import random

epsilon = 1.5


#    mu @ w   -> 1,3 x 3,1

test = SimpleLinearPerceptron(0.001,epsilon)

df = pd.read_csv('data/ej2-conjunto.csv', index_col=False)

x1 = df['x1'].array
x2 = df['x2'].array
x3 = df['x3'].array
results = df['y'].array


print(test._weights)

test.train(x1,x2,x3,results,10000)

print(test._weights)


real_results = []
accuracy = 1
j = 0
for i in range(len(x1)):
    real_results.append(test.run(x1[i],x2[i],x3[i]))
    print(('OK' if (real_results[i] < results[i]+ epsilon and real_results[i] > results[i] - epsilon) else 'FAIL') + ' \tentrada: ' + str(i) + ' \tresultado: ' + str(real_results[i]) + '\t esperado: ' + str(results[j]) )
    j+=1
j = 0
correct = 0
for r in real_results:
    if (r < results[j]+ epsilon and r > results[j] - epsilon):
        correct+=1
    j+=1
accuracy = correct / len(real_results)
print('accuracy: ' + str(accuracy))