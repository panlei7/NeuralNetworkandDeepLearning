import numpy as np

def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))


class Network():
    def __init__(self, sizes):
        self.layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(i, 1) for i in sizes[1:]]
        self.weights = [np.random.randn(i, j)
                        for i in size[1:] for j in size[:-1]]


    def feedforward(self, a):
        for b, w in zip(self.biases, self.weights):
            a = sigmoid(np.dot(w, a))
