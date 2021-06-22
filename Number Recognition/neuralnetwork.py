import numpy as np
from numpy.core.fromnumeric import argmax


class NeuralNet:
    def __init__(self, layer_sizes, weights=0, biases=0):
        weight_shapes = [(a,b) for a,b in zip(layer_sizes[1:],layer_sizes[:-1])]
        if weights == biases == 0:
            self.weights = [np.random.standard_normal(s)/s[1]**0.5 for s in weight_shapes]
            self.biases = [np.zeros((s,1)) for s in layer_sizes[1:]]
        else:
            self.weights = weights
            self.biases = biases

        self.hiddenlayer1 = None
        self.prediction = None
    
    def predict(self, a):
        if(len(self.weights)==2):
            w1, w2 = self.weights
            b1, b2 = self.biases
            inputlayer = a
            self.hiddenlayer1 = self.activation(np.matmul(w1, inputlayer) + b1)
            self.prediction = self.activation(np.matmul(w2, self.hiddenlayer1) + b2)
            return self.prediction
        else:
            print('Dont use more than 1 hidden layer.. Please')

    def print_accuracy(self, images, labels):
        self.predict(images)
        num_correct = sum([np.argmax(a) == np.argmax(b) for a,b in zip(self.prediction, labels)])
        print(f'{num_correct}/{len(images)} accuracy: {num_correct/len(images)*100}')

    def backpropagation(self, images, labels):
        learning_rate = -0.000044
        w1, w2 = self.weights
        
        b1, b2 = self.biases
        error_output = self.prediction-labels

        for i in range(len(images)):
            w2 += learning_rate * np.matmul(error_output[i], np.transpose(self.hiddenlayer1[i]), out=None)
            b2 += learning_rate * error_output[i]

            #now calibrating the hidden initial weights.
            error_hidden = np.matmul(np.transpose(w2), error_output[i]) * (self.hiddenlayer1[i] *(1-self.hiddenlayer1[i]))
            w1 += learning_rate * np.matmul(error_hidden, np.transpose(images[i]))
            b1 += learning_rate * error_hidden
            
            
        self.weights = w1,w2
        self.biases = b1, b2
            
        self.print_accuracy(images, labels)
        


    @staticmethod
    def activation(x):
        return 1/(1+np.exp(-x))

    def save_data(self):
        with open('weightss_biases.npz', 'bw') as npfile:
            np.savez_compressed(npfile, weights=self.weights, biases=self.biases)

    