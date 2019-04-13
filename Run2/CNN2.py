from keras import models
from keras import layers
network = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(25, 25, 1)))
network.add(layers.Dense(512, activation='relu', input_shape=(25 * 225,)))
network.add(layers.Dense(3, activation='softmax'))

network.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])


train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255
#test_images = test_images.reshape((10000, 28 * 28))
#test_images = test_images.astype('float32') / 255


from keras.utils import to_categorical
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)


network.fit(train_images, train_labels, epochs=5, batch_size=128)

















image2 = cv2.imread('/Users/b.i.garkuwa/Desktop/MSc Project/Datasets/Judy3_anon.jpg', 0)
print(image1.shape)

ret, image2 = cv2.threshold(image2, 180, 255, cv2.THRESH_BINARY)
for x in range(0, image2.shape[0] - w_width, stepSize):
    for y in range(0, image2.shape[1] - w_height, stepSize):
        prov_window = image2[x:x + w_width, y:y + w_height]
        if prov_window[int(w_width / 2), int(w_height / 2)] == 0:
            test_window.append(prov_window.flatten())

image3 = cv2.imread('/Users/b.i.garkuwa/Desktop/MSc Project/Datasets/Judy4_anon.jpg', 0)
print(image1.shape)

ret, image3 = cv2.threshold(image3, 180, 255, cv2.THRESH_BINARY)
for x in range(0, image3.shape[0] - w_width, stepSize):
    for y in range(0, image3.shape[1] - w_height, stepSize):
        prov_window = image3[x:x + w_width, y:y + w_height]
        if prov_window[int(w_width / 2), int(w_height / 2)] == 0:
            test_window.append(prov_window.flatten())

image4 = cv2.imread('/Users/b.i.garkuwa/Desktop/MSc Project/Datasets/Judy5_anon.jpg', 0)
print(image4.shape)

ret, image1 = cv2.threshold(image4, 180, 255, cv2.THRESH_BINARY)
for x in range(0, image4.shape[0] - w_width, stepSize):
    for y in range(0, image4.shape[1] - w_height, stepSize):
        prov_window = image4[x:x + w_width, y:y + w_height]
        if prov_window[int(w_width / 2), int(w_height / 2)] == 0:
            test_window.append(prov_window.flatten())

image5 = cv2.imread('/Users/b.i.garkuwa/Desktop/MSc Project/Datasets/Judy6_anon.jpg', 0)
print(image5.shape)

ret, image5 = cv2.threshold(image5, 180, 255, cv2.THRESH_BINARY)
for x in range(0, image5.shape[0] - w_width, stepSize):
    for y in range(0, image5.shape[1] - w_height, stepSize):
        prov_window = image5[x:x + w_width, y:y + w_height]
        if prov_window[int(w_width / 2), int(w_height / 2)] == 0:
            test_window.append(prov_window.flatten())

image6 = cv2.imread('/Users/b.i.garkuwa/Desktop/MSc Project/Datasets/Judy7_anon.jpg', 0)
print(image6.shape)

ret, image6 = cv2.threshold(image6, 180, 255, cv2.THRESH_BINARY)
for x in range(0, image6.shape[0] - w_width, stepSize):
    for y in range(0, image6.shape[1] - w_height, stepSize):
        prov_window = image6[x:x + w_width, y:y + w_height]
        if prov_window[int(w_width / 2), int(w_height / 2)] == 0:
            test_window.append(prov_window.flatten())

image7 = cv2.imread('/Users/b.i.garkuwa/Desktop/MSc Project/Datasets/Judy8_anon.jpg', 0)
print(image7.shape)

ret, image7 = cv2.threshold(image7, 180, 255, cv2.THRESH_BINARY)
for x in range(0, image7.shape[0] - w_width, stepSize):
    for y in range(0, image7.shape[1] - w_height, stepSize):
        prov_window = image7[x:x + w_width, y:y + w_height]
        if prov_window[int(w_width / 2), int(w_height / 2)] == 0:
            test_window.append(prov_window.flatten())





