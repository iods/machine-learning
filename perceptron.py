from random import random

def dot_product(inputs, weights):
    return sum(float(x * y) for x, y in zip(inputs, weights))

def sign(n):
    return 1 if n > 0 else -1

class Perceptron:
    """ Simple perceptron for linear classification """
    def __init__(self, n, learning_constant = 0.1):
        self.n = n
        self.weights = []
        # With a high learning constant the algo will converge more quickly but may
        # be less accurate than it would be using a smaller learning constant
        self.constant = learning_constant
        self.initialize_weights()

    def initialize_weights(self):
        """ Generate random weights (+ AND -) for the initial state """
        for i in range(self.n):
            self.weights.append((random() - 0.5))

    def feed_forward(self, inputs):
        """ Make a prediction about classification """
        # Take the dot product of the input and weights
        dot = dot_product(inputs, self.weights)
        return sign(dot)

    def calculate_new_weight(self, error ,value):
        return self.contant * error * value

    def train(self, inputs, goal):
        guess = self.feed_forward(inputs)
        print(guess)
        error = goal - guess
        print(error)
