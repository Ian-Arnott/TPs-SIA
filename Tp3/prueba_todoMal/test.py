from perceptron_test import SimpleStepPerceptron


# FUNCION AND &&
inputs = [[1,1],[1,-1],[-1,1],[-1,-1]]

# results = [1,-1,-1,1]   # AND  0.75 success
# results = [1,1,1,-1]  # OR    1 success
results = [-1,1,1,-1]  # X OR   0.75 success

test = SimpleStepPerceptron(0.1)

print(test._weights)

# [a,b] x [u,w] --> a*u + b*w 

            #  W1
# entrada      W2        salida      1,1 ->   kasmdkmasd  ->   1
             # W3

            # train -->
            #  1(bias), 1, -1 @ 0.025, 0.33, 0.457 --> -0.0482

test.train(inputs,results,1000)

print(test._weights)

real_results = []
accuracy = 1
j = 0
for i in inputs:
    real_results.append(test.run(i))
    print(('OK' if (real_results[j]==results[j]) else 'FAIL') + ' \tentrada: ' + str(i) + ' \tresultado: ' + str(real_results[j]) + '\t esperado: ' + str(results[j]) )
    j+=1
j = 0
correct = 0
for r in real_results:
    if (r == results[j]):
        correct+=1
    j+=1
accuracy = correct / len(real_results)
print('accuracy: ' + str(accuracy))