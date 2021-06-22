import neuralnetwork as nn
import numpy as np


with np.load('mnist.npz') as data:
    training_images = data['training_images']
    training_labels = data['training_labels']

with np.load('weightss_biases.npz', allow_pickle=True) as traineddata:
    weights = traineddata['weights']
    biases = traineddata['biases']


layer_sizes = (784,20,10)
x = np.ones((layer_sizes[0], 1))
# net = nn.NeuralNet(layer_sizes)
net = nn.NeuralNet(layer_sizes, weights, biases)
net.print_accuracy(training_images, training_labels)



for i in range(30):
    net.backpropagation(training_images, training_labels)

net.save_data()
