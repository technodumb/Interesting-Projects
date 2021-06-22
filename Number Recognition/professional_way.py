import tensorflow as tf
import cv2 as cv
# import matplotlib.pyplot as plt
import numpy as np
# from tensorflow.python.ops.math_ops import argmax
# import matlab

folders = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# objects =

# (training_images, training_labels), (test_images, test_labels) = objects.load_data()
with np.load('alphabet.npz') as data:
    training_images = data['training_images']
    training_labels = data['training_labels']
    test_images = data['test_images']
    test_labels = data['test_labels']
temp = []
for i in training_images:
    temp.append(cv.resize(i, (28,28)))

training_images = np.array(temp)

temp=[]
for i in test_images:
    temp.append(cv.resize(i, (28,28)))

test_images = np.array(temp)
# for i in range(4, 14):
#     plt.imshow(training_images[i])
#     plt.show()

# print(training_images.shape)
# print(training_images[0])

from keras.utils import to_categorical

training_labels = to_categorical(training_labels)
training_labels = training_labels[:,:,1]
test_labels = to_categorical(test_labels)
test_labels = test_labels[:,:,1]

# training_images = training_images/255.0
# test_images = test_images/255.0

model = tf.keras.models.Sequential([tf.keras.layers.Flatten(input_shape=(28,28)),
                                    tf.keras.layers.Dense(128, activation='relu'),
                                    tf.keras.layers.Dense(26, activation=tf.nn.softmax)])

model.compile(optimizer='Adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])


print(training_images.shape, training_labels.shape)
model.fit(training_images, training_labels, epochs=10)



#
#
print(model.evaluate(test_images, test_labels))
# # predictions = model.predict(training_images)
# # for i in range(6000, 6100):
# #     print(np.argmax(predictions[i]) == np.argmax(training_labels[i]))
#
#
#
# # print(image.shape)
# plt.imshow(image, 'winter')
# plt.show()
# image = np.mean(matlab.imread('testfile.jpg')/255, axis=2);print(folders[np.argmax(model.predict(np.array([image])))])
# dlabel = np.zeros((26,1));dlabel[folders.index('W')]; model.fit(np.array([image]), np.array([dlabel]), epochs=2)

print(training_images[0].shape)