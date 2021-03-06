import keras
import tensorflow
import matplotlib as plt
import cv2
import numpy as np

(symbol, text, connector) = (0, 1, 2)
stepSize = 20
(w_width, w_height) = (25, 25)  # window size

list_labels = list()
list_window = list()
test_window = list()

symbol = cv2.imread('/Users/b.i.garkuwa/Desktop/MSc Project/Datasets/Judy1_anon_symbols.jpg', 0)
print(symbol.shape)

ret, symbol = cv2.threshold(symbol, 180, 255, cv2.THRESH_BINARY)

for x in range(0, symbol.shape[0] - w_width, stepSize):
    for y in range(0, symbol.shape[1] - w_height, stepSize):
        prov_window = symbol[x:x + w_width, y:y + w_height]
        if prov_window[int(w_width / 2), int(w_height / 2)] == 0:
            list_window.append(prov_window.flatten())
            list_labels.append(0)

symbol1 = cv2.imread('/Users/b.i.garkuwa/Desktop/MSc Project/Datasets/Judy2_anon_symbols.jpg', 0)
print(symbol1.shape)

ret, symbol1 = cv2.threshold(symbol1, 180, 255, cv2.THRESH_BINARY)

for x in range(0, symbol1.shape[0] - w_width, stepSize):
    for y in range(0, symbol1.shape[1] - w_height, stepSize):
        prov_window = symbol1[x:x + w_width, y:y + w_height]
        if prov_window[int(w_width / 2), int(w_height / 2)] == 0:
            list_window.append(prov_window.flatten())
            list_labels.append(0)

symbol2 = cv2.imread('/Users/b.i.garkuwa/Desktop/MSc Project/Datasets/Judy3_anon_symbols.jpg', 0)
print(symbol2.shape)

ret, symbol2 = cv2.threshold(symbol2, 180, 255, cv2.THRESH_BINARY)

for x in range(0, symbol2.shape[0] - w_width, stepSize):
    for y in range(0, symbol2.shape[1] - w_height, stepSize):
        prov_window = symbol2[x:x + w_width, y:y + w_height]
        if prov_window[int(w_width / 2), int(w_height / 2)] == 0:
            list_window.append(prov_window.flatten())
            list_labels.append(0)

symbol3 = cv2.imread('/Users/b.i.garkuwa/Desktop/MSc Project/Datasets/Judy4_anon_symbols.jpg', 0)
print(symbol3.shape)

ret, symbol3 = cv2.threshold(symbol2, 180, 255, cv2.THRESH_BINARY)

for x in range(0, symbol3.shape[0] - w_width, stepSize):
    for y in range(0, symbol3.shape[1] - w_height, stepSize):
        prov_window = symbol3[x:x + w_width, y:y + w_height]
        if prov_window[int(w_width / 2), int(w_height / 2)] == 0:
            list_window.append(prov_window.flatten())
            list_labels.append(0)

symbol4 = cv2.imread('/Users/b.i.garkuwa/Desktop/MSc Project/Datasets/Judy5_anon_symbols.jpg', 0)
print(symbol4.shape)

ret, symbol4 = cv2.threshold(symbol4, 180, 255, cv2.THRESH_BINARY)

for x in range(0, symbol4.shape[0] - w_width, stepSize):
    for y in range(0, symbol4.shape[1] - w_height, stepSize):
        prov_window = symbol4[x:x + w_width, y:y + w_height]
        if prov_window[int(w_width / 2), int(w_height / 2)] == 0:
            list_window.append(prov_window.flatten())
            list_labels.append(0)

symbol5 = cv2.imread('/Users/b.i.garkuwa/Desktop/MSc Project/Datasets/Judy6_anon_symbols.jpg', 0)
print(symbol5.shape)

ret, symbol5 = cv2.threshold(symbol5, 180, 255, cv2.THRESH_BINARY)

for x in range(0, symbol5.shape[0] - w_width, stepSize):
    for y in range(0, symbol5.shape[1] - w_height, stepSize):
        prov_window = symbol5[x:x + w_width, y:y + w_height]
        if prov_window[int(w_width / 2), int(w_height / 2)] == 0:
            list_window.append(prov_window.flatten())
            list_labels.append(0)

symbol6 = cv2.imread('/Users/b.i.garkuwa/Desktop/MSc Project/Datasets/Judy7_anon_symbols.jpg', 0)
print(symbol6.shape)

ret, symbol6 = cv2.threshold(symbol6, 180, 255, cv2.THRESH_BINARY)

for x in range(0, symbol6.shape[0] - w_width, stepSize):
    for y in range(0, symbol6.shape[1] - w_height, stepSize):
        prov_window = symbol6[x:x + w_width, y:y + w_height]
        if prov_window[int(w_width / 2), int(w_height / 2)] == 0:
            list_window.append(prov_window.flatten())
            list_labels.append(0)

symbol7 = cv2.imread('/Users/b.i.garkuwa/Desktop/MSc Project/Datasets/Judy8_anon_symbols.jpg', 0)
print(symbol7.shape)

ret, symbol7 = cv2.threshold(symbol7, 180, 255, cv2.THRESH_BINARY)

for x in range(0, symbol7.shape[0] - w_width, stepSize):
    for y in range(0, symbol7.shape[1] - w_height, stepSize):
        prov_window = symbol7[x:x + w_width, y:y + w_height]
        if prov_window[int(w_width / 2), int(w_height / 2)] == 0:
            list_window.append(prov_window.flatten())
            list_labels.append(0)

text = cv2.imread('/Users/b.i.garkuwa/Desktop/MSc Project/Datasets/Judy1_anon_text.jpg', 0)
print(text.shape)

ret, text = cv2.threshold(text, 180, 255, cv2.THRESH_BINARY)
for x in range(0, text.shape[0] - w_width, stepSize):
    for y in range(0, text.shape[1] - w_height, stepSize):
        prov_window = text[x:x + w_width, y:y + w_height]
        if prov_window[int(w_width / 2), int(w_height / 2)] == 0:
            list_window.append(prov_window.flatten())
            list_labels.append(1)

text1 = cv2.imread('/Users/b.i.garkuwa/Desktop/MSc Project/Datasets/Judy2_anon_text.jpg', 0)
print(text1.shape)

ret, text1 = cv2.threshold(text1, 180, 255, cv2.THRESH_BINARY)
for x in range(0, text1.shape[0] - w_width, stepSize):
    for y in range(0, text1.shape[1] - w_height, stepSize):
        prov_window = text1[x:x + w_width, y:y + w_height]
        if prov_window[int(w_width / 2), int(w_height / 2)] == 0:
            list_window.append(prov_window.flatten())
            list_labels.append(1)

text2 = cv2.imread('/Users/b.i.garkuwa/Desktop/MSc Project/Datasets/Judy3_anon_text.jpg', 0)
print(text2.shape)

ret, text2 = cv2.threshold(text2, 180, 255, cv2.THRESH_BINARY)
for x in range(0, text2.shape[0] - w_width, stepSize):
    for y in range(0, text2.shape[1] - w_height, stepSize):
        prov_window = text2[x:x + w_width, y:y + w_height]
        if prov_window[int(w_width / 2), int(w_height / 2)] == 0:
            list_window.append(prov_window.flatten())
            list_labels.append(1)

text3 = cv2.imread('/Users/b.i.garkuwa/Desktop/MSc Project/Datasets/Judy4_anon_text.jpg', 0)
print(text3.shape)

ret, text3 = cv2.threshold(text3, 180, 255, cv2.THRESH_BINARY)
for x in range(0, text3.shape[0] - w_width, stepSize):
    for y in range(0, text3.shape[1] - w_height, stepSize):
        prov_window = text3[x:x + w_width, y:y + w_height]
        if prov_window[int(w_width / 2), int(w_height / 2)] == 0:
            list_window.append(prov_window.flatten())
            list_labels.append(1)

text4 = cv2.imread('/Users/b.i.garkuwa/Desktop/MSc Project/Datasets/Judy5_anon_text.jpg', 0)
print(text4.shape)

ret, text4 = cv2.threshold(text4, 180, 255, cv2.THRESH_BINARY)
for x in range(0, text4.shape[0] - w_width, stepSize):
    for y in range(0, text4.shape[1] - w_height, stepSize):
        prov_window = text4[x:x + w_width, y:y + w_height]
        if prov_window[int(w_width / 2), int(w_height / 2)] == 0:
            list_window.append(prov_window.flatten())
            list_labels.append(1)

text5 = cv2.imread('/Users/b.i.garkuwa/Desktop/MSc Project/Datasets/Judy6_anon_text.jpg', 0)
print(text5.shape)

ret, text5 = cv2.threshold(text5, 180, 255, cv2.THRESH_BINARY)
for x in range(0, text5.shape[0] - w_width, stepSize):
    for y in range(0, text5.shape[1] - w_height, stepSize):
        prov_window = text5[x:x + w_width, y:y + w_height]
        if prov_window[int(w_width / 2), int(w_height / 2)] == 0:
            list_window.append(prov_window.flatten())
            list_labels.append(1)

text6 = cv2.imread('/Users/b.i.garkuwa/Desktop/MSc Project/Datasets/Judy7_anon_text.jpg', 0)
print(text.shape)

ret, text6 = cv2.threshold(text6, 180, 255, cv2.THRESH_BINARY)
for x in range(0, text6.shape[0] - w_width, stepSize):
    for y in range(0, text6.shape[1] - w_height, stepSize):
        prov_window = text6[x:x + w_width, y:y + w_height]
        if prov_window[int(w_width / 2), int(w_height / 2)] == 0:
            list_window.append(prov_window.flatten())
            list_labels.append(1)

text7 = cv2.imread('/Users/b.i.garkuwa/Desktop/MSc Project/Datasets/Judy8_anon_text.jpg', 0)
print(text7.shape)

ret, text7 = cv2.threshold(text7, 180, 255, cv2.THRESH_BINARY)
for x in range(0, text7.shape[0] - w_width, stepSize):
    for y in range(0, text7.shape[1] - w_height, stepSize):
        prov_window = text7[x:x + w_width, y:y + w_height]
        if prov_window[int(w_width / 2), int(w_height / 2)] == 0:
            list_window.append(prov_window.flatten())
            list_labels.append(1)

connector = cv2.imread('/Users/b.i.garkuwa/Desktop/MSc Project/Datasets/Judy1_anon_connectors.jpg', 0)
print(connector.shape)

ret, connector = cv2.threshold(connector, 180, 255, cv2.THRESH_BINARY)
for x in range(0, connector.shape[0] - w_width, stepSize):
    for y in range(0, connector.shape[1] - w_height, stepSize):
        prov_window = connector[x:x + w_width, y:y + w_height]
        if prov_window[int(w_width / 2), int(w_height / 2)] == 0:
            list_window.append(prov_window.flatten())
            list_labels.append(2)

connector1 = cv2.imread('/Users/b.i.garkuwa/Desktop/MSc Project/Datasets/Judy2_anon_connectors.jpg', 0)
print(connector1.shape)

ret, connector1 = cv2.threshold(connector1, 180, 255, cv2.THRESH_BINARY)
for x in range(0, connector1.shape[0] - w_width, stepSize):
    for y in range(0, connector1.shape[1] - w_height, stepSize):
        prov_window = connector1[x:x + w_width, y:y + w_height]
        if prov_window[int(w_width / 2), int(w_height / 2)] == 0:
            list_window.append(prov_window.flatten())
            list_labels.append(2)

connector2 = cv2.imread('/Users/b.i.garkuwa/Desktop/MSc Project/Datasets/Judy3_anon_connectors.jpg', 0)
print(connector2.shape)

ret, connector2 = cv2.threshold(connector2, 180, 255, cv2.THRESH_BINARY)
for x in range(0, connector2.shape[0] - w_width, stepSize):
    for y in range(0, connector2.shape[1] - w_height, stepSize):
        prov_window = connector2[x:x + w_width, y:y + w_height]
        if prov_window[int(w_width / 2), int(w_height / 2)] == 0:
            list_window.append(prov_window.flatten())
            list_labels.append(2)

connector3 = cv2.imread('/Users/b.i.garkuwa/Desktop/MSc Project/Datasets/Judy4_anon_connectors.jpg', 0)
print(connector3.shape)

ret, connector3 = cv2.threshold(connector3, 180, 255, cv2.THRESH_BINARY)
for x in range(0, connector3.shape[0] - w_width, stepSize):
    for y in range(0, connector3.shape[1] - w_height, stepSize):
        prov_window = connector3[x:x + w_width, y:y + w_height]
        if prov_window[int(w_width / 2), int(w_height / 2)] == 0:
            list_window.append(prov_window.flatten())
            list_labels.append(2)

connector4 = cv2.imread('/Users/b.i.garkuwa/Desktop/MSc Project/Datasets/Judy5_anon_connectors.jpg', 0)
print(connector4.shape)

ret, connector4 = cv2.threshold(connector4, 180, 255, cv2.THRESH_BINARY)
for x in range(0, connector4.shape[0] - w_width, stepSize):
    for y in range(0, connector4.shape[1] - w_height, stepSize):
        prov_window = connector4[x:x + w_width, y:y + w_height]
        if prov_window[int(w_width / 2), int(w_height / 2)] == 0:
            list_window.append(prov_window.flatten())
            list_labels.append(2)

connector5 = cv2.imread('/Users/b.i.garkuwa/Desktop/MSc Project/Datasets/Judy6_anon_connectors.jpg', 0)
print(connector5.shape)

ret, connector5 = cv2.threshold(connector5, 180, 255, cv2.THRESH_BINARY)
for x in range(0, connector5.shape[0] - w_width, stepSize):
    for y in range(0, connector5.shape[1] - w_height, stepSize):
        prov_window = connector5[x:x + w_width, y:y + w_height]
        if prov_window[int(w_width / 2), int(w_height / 2)] == 0:
            list_window.append(prov_window.flatten())
            list_labels.append(2)

connector6 = cv2.imread('/Users/b.i.garkuwa/Desktop/MSc Project/Datasets/Judy7_anon_connectors.jpg', 0)
print(connector6.shape)

ret, connector6 = cv2.threshold(connector6, 180, 255, cv2.THRESH_BINARY)
for x in range(0, connector6.shape[0] - w_width, stepSize):
    for y in range(0, connector6.shape[1] - w_height, stepSize):
        prov_window = connector6[x:x + w_width, y:y + w_height]
        if prov_window[int(w_width / 2), int(w_height / 2)] == 0:
            list_window.append(prov_window.flatten())
            list_labels.append(2)

connector7 = cv2.imread('/Users/b.i.garkuwa/Desktop/MSc Project/Datasets/Judy8_anon_connectors.jpg', 0)
print(connector7.shape)

ret, connector7 = cv2.threshold(connector7, 180, 255, cv2.THRESH_BINARY)
for x in range(0, connector7.shape[0] - w_width, stepSize):
    for y in range(0, connector7.shape[1] - w_height, stepSize):
        prov_window = connector7[x:x + w_width, y:y + w_height]
        if prov_window[int(w_width / 2), int(w_height / 2)] == 0:
            list_window.append(prov_window.flatten())
            list_labels.append(2)


#Change the list of windows to an array of images 
list_window = np.asanyarray(list_window)
list_labels = np.asanyarray(list_labels)

list_window = list_window.reshape((43744, 25, 25, 1))
list_window = list_window.astype('float32') / 255

#print(list_window)

#Change labels ti categorical
from keras.utils import to_categorical

list_labels = to_categorical(list_labels)

#Build the convolutional neural networks
from keras import layers
from keras import models

model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(25, 25, 1)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))

model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(3, activation='softmax'))
model.summary()

#model = models.Sequential()
#model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(25, 25, 1)))
#model.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
#model.add(layers.Dense(3, activation='softmax'))

model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

model.fit(list_window, list_labels, epochs=5, batch_size=128)


#Test

image1 = cv2.imread('/Users/b.i.garkuwa/Desktop/MSc Project/Datasets/Judy2_anon.jpg', 0)
print(image1.shape)

ret, image1 = cv2.threshold(image1, 180, 255, cv2.THRESH_BINARY)
for x in range(0, image1.shape[0] - w_width, stepSize):
    for y in range(0, image1.shape[1] - w_height, stepSize):
        prov_window = image1[x:x + w_width, y:y + w_height]
        if prov_window[int(w_width / 2), int(w_height / 2)] == 0:
            test_window.append(prov_window.flatten())


image = cv2.imread('/Users/b.i.garkuwa/Desktop/MSc Project/Datasets/Judy1_anon.jpg', 0)
print(image.shape)

ret, image = cv2.threshold(image, 180, 255, cv2.THRESH_BINARY)
for x in range(0, image.shape[0] - w_width, stepSize):
    for y in range(0, image.shape[1] - w_height, stepSize):
        prov_window = image[x:x + w_width, y:y + w_height]
        if prov_window[int(w_width / 2), int(w_height / 2)] == 0:
            test_window.append(prov_window.flatten())