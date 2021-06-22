import numpy as np
import matplotlib.pyplot as plt
import matlab
import neuralnetwork_copy as nn



with np.load('weightss_biases.npz', allow_pickle=True) as traineddata:
    weights = traineddata['weights']
    biases = traineddata['biases']

image = matlab.imread('testfile.jpg')
image = (765 - np.sum(image, axis=2))/765
image = image.reshape(784,1)

net = nn.NeuralNet((784, 20, 10), weights, biases)
predictions = net.predict(image)
print(np.argmax(predictions))

# plt.imshow(image.reshape(28,28), cmap='gray')
# plt.show()
