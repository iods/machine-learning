from random import random

def dot_product(inputs, weights):
    return sum(float(x * y) for x, y in zip(inputs, weights))

def sign(n):
    return 1 if n > 0 else -1

class Perceptron:
    """ Simple perceptron for linear classification """
    def __init__(self, n, learning_constant = 0.2):
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

    def update_weights(self, error, inputs):
        for index, value in enumerate(inputs):
            self.weights[index] += self.constant * error * value

    def train(self, inputs, expected):
        guess = self.feed_forward(inputs)
        error = expected - guess
        self.update_weights(error, inputs)
        return error

# ==================

class SimplePerceptron():

    def __init__(self):
        self.threshold = 0.5
        self.learning_rate

threshold = 0.5
learning_rate = 0.1
weights = [0, 0, 0]
training_set = [((1, 0, 0), 1), ((1, 0, 1), 1), ((1, 1, 0), 1), ((1, 1, 1), 0)]

iterations = 0
while True:
  print('-' * 60)
  iterations += 1
  error_count = 0
  for input_vector, desired_output in training_set:
    result = dot_product(input_vector, weights) > threshold
    print(result)
    error = desired_output - result
    print(error)
    if error != 0:
      error_count += 1
      for index, value in enumerate(input_vector):
        weights[index] += learning_rate * error * value
  if error_count == 0:
    print("DONE")
    break
