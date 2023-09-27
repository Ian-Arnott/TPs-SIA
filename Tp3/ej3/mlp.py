import numpy as np

def predict(network, input):
    output = input
    for layer in network:
        output = layer.forward(output)
    return output

def train(network, error_function, error_derivative, x_train, y_train, epochs = 1000, learning_rate = 0.01, verbose = True, optimizer_type = None):
    if optimizer_type == "ADAM":
        optimizer = AdamOptimizer(learning_rate)
    else:
        optimizer = None
        
    for e in range(epochs):
        error = 0
        for x, y in zip(x_train, y_train):
            # forward
            output = predict(network, x)

            # error
            error += error_function(y, output)

            # backward
            grad = error_derivative(y, output)

            time_step = 0

            for layer in reversed(network):
                time_step += 1
                if isinstance(layer, Dense):
                    if optimizer is not None:
                        weights_gradient = np.dot(grad, layer.input.T)
                        layer.weights += optimizer.update(weights_gradient, time_step)

                grad = layer.backward(grad, learning_rate)

        error /= len(x_train)
        if verbose:
            print(f"{e + 1}/{epochs}, error={error}")

class Layer:
    def __init__(self):
        self.input = None
        self.output = None

    def fowards(self, input):
        pass

    def backwards(self, output_derivative, learing_rate):
        pass

class Dense(Layer):
    def __init__(self, input_size, output_size):
        self.weights = np.random.randn(output_size, input_size)
        self.bias =  np.random.randn(output_size, 1)

    def forward(self, input):
        self.input = input
        return np.dot(self.weights, self.input) + self.bias

    def backward(self, output_derivative, learning_rate):
        weights_gradient = np.dot(output_derivative, self.input.T)
        input_gradient = np.dot(self.weights.T, output_derivative)
        self.weights -= learning_rate * weights_gradient
        self.bias -= learning_rate * output_derivative
        return input_gradient

class Activation(Layer):
    def __init__(self, activation, activation_derivative):
        self.activation = activation
        self.activation_derivative = activation_derivative

    def forward(self, input):
        self.input = input
        return self.activation(self.input)

    def backward(self, output_gradient, learning_rate):
        return np.multiply(output_gradient, self.activation_derivative (self.input))

# Implementacion de optimizer

class Optimizer:
    def __init__(self, learning_rate):
        self.learningRate = learning_rate

    def update(self, gradient):
        return

class AdamOptimizer(Optimizer):
    def __init__(self, learning_rate, beta1=0.9, beta2=0.999, epsilon=1e-8, shape=None):
        super().__init__(learning_rate)
        self.beta1 = beta1
        self.beta2 = beta2
        self.epsilon = epsilon
        if shape is not None:
            self.m = np.zeros(shape)
            self.v = np.zeros(shape)
        else:
            self.m = None
            self.v = None

    def update(self, gradient, time_step):
        if self.m is None:
            self.m = np.zeros_like(gradient)
            self.v = np.zeros_like(gradient)
        
        self.m = self.beta1 * self.m + (1 - self.beta1) * gradient
        self.v = self.beta2 * self.v + (1 - self.beta2) * np.square(gradient)
        
        mHat = self.m / (1 - self.beta1**time_step)
        vHat = self.v / (1 - self.beta2**time_step)
        
        return (-self.learningRate * mHat) / (np.sqrt(vHat) + self.epsilon)
