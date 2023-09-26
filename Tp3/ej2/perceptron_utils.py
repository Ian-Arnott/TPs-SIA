import matplotlib.pyplot as plt
import numpy as np
from perceptron import SimpleLinealPerceptron, SimpleHiperbolicPerceptron, SimpleLogisticPerceptrion
from utils import PERCEPTRON_TYPES


def initialize_perceptron(perceptron_type, beta, learning_rate, bias, input_size, epsilon):
    if perceptron_type == PERCEPTRON_TYPES[0]:
        return SimpleLinealPerceptron(learning_rate, None, bias, input_size, epsilon)
    elif perceptron_type == PERCEPTRON_TYPES[1]:
        return SimpleHiperbolicPerceptron(beta, learning_rate, None, bias, input_size, epsilon)
    elif perceptron_type == PERCEPTRON_TYPES[2]:
        return SimpleLogisticPerceptrion(beta, learning_rate, None, bias, input_size, epsilon)


def min_max_interval(values:list[float]) -> tuple[float]:
    min_value = min(values)
    max_value = max(values)
    return (min_value, max_value)


def calculate_accuracy(predictions, expected, epsilon):
    correct_predictions = sum(1 for p, gt in zip(predictions, expected) if abs(p - gt) <= epsilon)
    accuracy = (correct_predictions / len(predictions)) * 100
    return accuracy