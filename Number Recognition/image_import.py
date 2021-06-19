import matlab
import numpy as np
import os


folders = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

training_images = []
training_labels = []
test_images = []
test_labels = []


location = 'D:\\Users\\Documents\\Code\\Interesting Projects\\Number Recognition\\archive'

for lab,i in enumerate(folders):
    images = os.listdir(location+'\\'+i)
    for j in images:
        # print(j)
        training_images.append(matlab.imread(location+'\\'+i+'\\'+j)/255)
        label = np.zeros(26)
        label[lab] = 1
        training_labels.append(label)

training_images = np.array(training_images)
training_labels = np.array(training_labels)


location = 'D:\\Users\\Documents\\Code\\Interesting Projects\\Number Recognition\\archive\\english_alphabets'

for lab,i in enumerate(folders):
    images = os.listdir(location+'\\'+i)
    for j in images:
        # print(j)
        test_images.append(matlab.imread(location+'\\'+i+'\\'+j)/255)
        label = np.zeros(26)
        label[lab] = 1
        test_labels.append(label)

test_images = np.array(test_images)
test_labels = np.array(test_labels)

# print(training_labels[-1])
with open('alphabet.npz', 'bw') as npfile:
    np.savez_compressed(npfile, training_images = training_images, training_labels = training_labels, test_images = test_images, test_labels = test_labels)


# image = matlab.imread('testfile.jpg')
# image = (765 - np.sum(image, axis=2))/765

# os.system('cd archive\\' + 'A')

# np.ndarray()
