import numpy as np

def sigmoid(x):
    # activation function: f(x) = 1 / (1 + e^(-x)) 
    return 1/ (1+np.exp(-x))

class Neuron:
    def __init__(self,weights,bias):
        self.weights = weights
        self.bias = bias
        
    def feedforward(self,inputs):
        #calculate dot product of (weight x inputs) + bias
        tot = np.dot(self.weights,inputs) + self.bias
        print(tot)
        return sigmoid(tot)
        
        
# weights = np.array([0,1])
# bias = 0
# n = Neuron(weights,bias)

# x = np.array([0.9526,0.9526])
# print(n.feedforward(x))

class NeuralNetwork:
    '''
        this Neural network have,
        - 2 inputs
        - 1 hidden layer with 2 neurons (h1,h2)
        - an output layer with 1 neuron (o1)
        Each of neurons have same wights and bias
        w=[0,1]
        b=0 
    '''
    
    def __init__(self):
        weights = np.array([0,1])
        bias = 0
        
        self.h1 = Neuron(weights,bias)
        self.h2 = Neuron(weights,bias)
        self.o1 = Neuron(weights,bias)
        
    def feedforward(self,x):
        h1_out = self.h1.feedforward(x)
        h2_out = self.h2.feedforward(x)
        o1_x = np.array([h1_out,h2_out])
        o1_out = self.o1.feedforward(o1_x)
        
        return o1_out
    
network = NeuralNetwork()
x = np.array([2,3])

print(network.feedforward(x))