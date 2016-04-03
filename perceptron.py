class Perceptron():
    def __init__(self):
        pass

def dot_product(inputs, weights):
    return sum(i*w for i,w in zip(inputs, weights))

threshold = 0.5 # activation threshold
learning_rate = 0.1
weights = [0, 0, 0]
training_set = [([1, 0, 0], 1), ([1, 0, 1], 1), ([1, 1, 0], 1), ([1, 1, 1], 0)]
error_count = 0

def iteration():
    for input_vector, desired_output in training_set:
        print("Input %s" % input_vector)
        print("Weights %s" % weights)
        dp = dot_product(input_vector, weights)
        result = dp > threshold
        print(result)
        error = desired_output - result
        print(error)
        if error != 0:
            error_count += 1
            for index, value in enumerate(input_vector):
                weights[index] += learning_rate * error * value

def learn():
    while True:
        iteration()
        if error_count == 0:
            break
