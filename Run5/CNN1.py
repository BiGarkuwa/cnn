
stepSize = 15


import cv2

import cv2
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
            list_labels.append('symbol')

symbol1 = cv2.imread('/Users/b.i.garkuwa/Desktop/MSc Project/Datasets/Judy2_anon_symbols.jpg', 0)
print(symbol1.shape)

ret, symbol1 = cv2.threshold(symbol1, 180, 255, cv2.THRESH_BINARY)

for x in range(0, symbol1.shape[0] - w_width, stepSize):
    for y in range(0, symbol1.shape[1] - w_height, stepSize):
        prov_window = symbol1[x:x + w_width, y:y + w_height]
        if prov_window[int(w_width / 2), int(w_height / 2)] == 0:
            list_window.append(prov_window.flatten())
            list_labels.append('symbol')

symbol2 = cv2.imread('/Users/b.i.garkuwa/Desktop/MSc Project/Datasets/Judy3_anon_symbols.jpg', 0)
print(symbol2.shape)

ret, symbol2 = cv2.threshold(symbol2, 180, 255, cv2.THRESH_BINARY)

for x in range(0, symbol2.shape[0] - w_width, stepSize):
    for y in range(0, symbol2.shape[1] - w_height, stepSize):
        prov_window = symbol2[x:x + w_width, y:y + w_height]
        if prov_window[int(w_width / 2), int(w_height / 2)] == 0:
            list_window.append(prov_window.flatten())
            list_labels.append('symbol')

symbol3 = cv2.imread('/Users/b.i.garkuwa/Desktop/MSc Project/Datasets/Judy4_anon_symbols.jpg', 0)
print(symbol3.shape)

ret, symbol3 = cv2.threshold(symbol2, 180, 255, cv2.THRESH_BINARY)

for x in range(0, symbol3.shape[0] - w_width, stepSize):
    for y in range(0, symbol3.shape[1] - w_height, stepSize):
        prov_window = symbol3[x:x + w_width, y:y + w_height]
        if prov_window[int(w_width / 2), int(w_height / 2)] == 0:
            list_window.append(prov_window.flatten())
            list_labels.append('symbol')

symbol4 = cv2.imread('/Users/b.i.garkuwa/Desktop/MSc Project/Datasets/Judy5_anon_symbols.jpg', 0)
print(symbol4.shape)

ret, symbol4 = cv2.threshold(symbol4, 180, 255, cv2.THRESH_BINARY)

for x in range(0, symbol4.shape[0] - w_width, stepSize):
    for y in range(0, symbol4.shape[1] - w_height, stepSize):
        prov_window = symbol4[x:x + w_width, y:y + w_height]
        if prov_window[int(w_width / 2), int(w_height / 2)] == 0:
            list_window.append(prov_window.flatten())
            list_labels.append('symbol')

symbol5 = cv2.imread('/Users/b.i.garkuwa/Desktop/MSc Project/Datasets/Judy6_anon_symbols.jpg', 0)
print(symbol5.shape)

ret, symbol5 = cv2.threshold(symbol5, 180, 255, cv2.THRESH_BINARY)

for x in range(0, symbol5.shape[0] - w_width, stepSize):
    for y in range(0, symbol5.shape[1] - w_height, stepSize):
        prov_window = symbol5[x:x + w_width, y:y + w_height]
        if prov_window[int(w_width / 2), int(w_height / 2)] == 0:
            list_window.append(prov_window.flatten())
            list_labels.append('symbol')

symbol6 = cv2.imread('/Users/b.i.garkuwa/Desktop/MSc Project/Datasets/Judy7_anon_symbols.jpg', 0)
print(symbol6.shape)

ret, symbol6 = cv2.threshold(symbol6, 180, 255, cv2.THRESH_BINARY)

for x in range(0, symbol6.shape[0] - w_width, stepSize):
    for y in range(0, symbol6.shape[1] - w_height, stepSize):
        prov_window = symbol6[x:x + w_width, y:y + w_height]
        if prov_window[int(w_width / 2), int(w_height / 2)] == 0:
            list_window.append(prov_window.flatten())
            list_labels.append('symbol')

symbol7 = cv2.imread('/Users/b.i.garkuwa/Desktop/MSc Project/Datasets/Judy8_anon_symbols.jpg', 0)
print(symbol7.shape)

ret, symbol7 = cv2.threshold(symbol7, 180, 255, cv2.THRESH_BINARY)

for x in range(0, symbol7.shape[0] - w_width, stepSize):
    for y in range(0, symbol7.shape[1] - w_height, stepSize):
        prov_window = symbol7[x:x + w_width, y:y + w_height]
        if prov_window[int(w_width / 2), int(w_height / 2)] == 0:
            list_window.append(prov_window.flatten())
            list_labels.append('symbol')

text = cv2.imread('/Users/b.i.garkuwa/Desktop/MSc Project/Datasets/Judy1_anon_text.jpg', 0)
print(text.shape)

ret, text = cv2.threshold(text, 180, 255, cv2.THRESH_BINARY)
for x in range(0, text.shape[0] - w_width, stepSize):
    for y in range(0, text.shape[1] - w_height, stepSize):
        prov_window = text[x:x + w_width, y:y + w_height]
        if prov_window[int(w_width / 2), int(w_height / 2)] == 0:
            list_window.append(prov_window.flatten())
            list_labels.append('text')

text1 = cv2.imread('/Users/b.i.garkuwa/Desktop/MSc Project/Datasets/Judy2_anon_text.jpg', 0)
print(text1.shape)

ret, text1 = cv2.threshold(text1, 180, 255, cv2.THRESH_BINARY)
for x in range(0, text1.shape[0] - w_width, stepSize):
    for y in range(0, text1.shape[1] - w_height, stepSize):
        prov_window = text1[x:x + w_width, y:y + w_height]
        if prov_window[int(w_width / 2), int(w_height / 2)] == 0:
            list_window.append(prov_window.flatten())
            list_labels.append('text')

text2 = cv2.imread('/Users/b.i.garkuwa/Desktop/MSc Project/Datasets/Judy3_anon_text.jpg', 0)
print(text2.shape)

ret, text2 = cv2.threshold(text2, 180, 255, cv2.THRESH_BINARY)
for x in range(0, text2.shape[0] - w_width, stepSize):
    for y in range(0, text2.shape[1] - w_height, stepSize):
        prov_window = text2[x:x + w_width, y:y + w_height]
        if prov_window[int(w_width / 2), int(w_height / 2)] == 0:
            list_window.append(prov_window.flatten())
            list_labels.append('text')

text3 = cv2.imread('/Users/b.i.garkuwa/Desktop/MSc Project/Datasets/Judy4_anon_text.jpg', 0)
print(text3.shape)

ret, text3 = cv2.threshold(text3, 180, 255, cv2.THRESH_BINARY)
for x in range(0, text3.shape[0] - w_width, stepSize):
    for y in range(0, text3.shape[1] - w_height, stepSize):
        prov_window = text3[x:x + w_width, y:y + w_height]
        if prov_window[int(w_width / 2), int(w_height / 2)] == 0:
            list_window.append(prov_window.flatten())
            list_labels.append('text')

text4 = cv2.imread('/Users/b.i.garkuwa/Desktop/MSc Project/Datasets/Judy5_anon_text.jpg', 0)
print(text4.shape)

ret, text4 = cv2.threshold(text4, 180, 255, cv2.THRESH_BINARY)
for x in range(0, text4.shape[0] - w_width, stepSize):
    for y in range(0, text4.shape[1] - w_height, stepSize):
        prov_window = text4[x:x + w_width, y:y + w_height]
        if prov_window[int(w_width / 2), int(w_height / 2)] == 0:
            list_window.append(prov_window.flatten())
            list_labels.append('text')

text5 = cv2.imread('/Users/b.i.garkuwa/Desktop/MSc Project/Datasets/Judy6_anon_text.jpg', 0)
print(text5.shape)

ret, text5 = cv2.threshold(text5, 180, 255, cv2.THRESH_BINARY)
for x in range(0, text5.shape[0] - w_width, stepSize):
    for y in range(0, text5.shape[1] - w_height, stepSize):
        prov_window = text5[x:x + w_width, y:y + w_height]
        if prov_window[int(w_width / 2), int(w_height / 2)] == 0:
            list_window.append(prov_window.flatten())
            list_labels.append('text')

text6 = cv2.imread('/Users/b.i.garkuwa/Desktop/MSc Project/Datasets/Judy7_anon_text.jpg', 0)
print(text.shape)

ret, text6 = cv2.threshold(text6, 180, 255, cv2.THRESH_BINARY)
for x in range(0, text6.shape[0] - w_width, stepSize):
    for y in range(0, text6.shape[1] - w_height, stepSize):
        prov_window = text6[x:x + w_width, y:y + w_height]
        if prov_window[int(w_width / 2), int(w_height / 2)] == 0:
            list_window.append(prov_window.flatten())
            list_labels.append('text')

text7 = cv2.imread('/Users/b.i.garkuwa/Desktop/MSc Project/Datasets/Judy8_anon_text.jpg', 0)
print(text7.shape)

ret, text7 = cv2.threshold(text7, 180, 255, cv2.THRESH_BINARY)
for x in range(0, text7.shape[0] - w_width, stepSize):
    for y in range(0, text7.shape[1] - w_height, stepSize):
        prov_window = text7[x:x + w_width, y:y + w_height]
        if prov_window[int(w_width / 2), int(w_height / 2)] == 0:
            list_window.append(prov_window.flatten())
            list_labels.append('text')

connector = cv2.imread('/Users/b.i.garkuwa/Desktop/MSc Project/Datasets/Judy1_anon_connectors.jpg', 0)
print(connector.shape)

ret, connector = cv2.threshold(connector, 180, 255, cv2.THRESH_BINARY)
for x in range(0, connector.shape[0] - w_width, stepSize):
    for y in range(0, connector.shape[1] - w_height, stepSize):
        prov_window = connector[x:x + w_width, y:y + w_height]
        if prov_window[int(w_width / 2), int(w_height / 2)] == 0:
            list_window.append(prov_window.flatten())
            list_labels.append('connector')

plt.show()

connector1 = cv2.imread('/Users/b.i.garkuwa/Desktop/MSc Project/Datasets/Judy2_anon_connectors.jpg', 0)
print(connector1.shape)

ret, connector1 = cv2.threshold(connector1, 180, 255, cv2.THRESH_BINARY)
for x in range(0, connector1.shape[0] - w_width, stepSize):
    for y in range(0, connector1.shape[1] - w_height, stepSize):
        prov_window = connector1[x:x + w_width, y:y + w_height]
        if prov_window[int(w_width / 2), int(w_height / 2)] == 0:
            list_window.append(prov_window.flatten())
            list_labels.append('connector')

connector2 = cv2.imread('/Users/b.i.garkuwa/Desktop/MSc Project/Datasets/Judy3_anon_connectors.jpg', 0)
print(connector2.shape)

ret, connector2 = cv2.threshold(connector2, 180, 255, cv2.THRESH_BINARY)
for x in range(0, connector2.shape[0] - w_width, stepSize):
    for y in range(0, connector2.shape[1] - w_height, stepSize):
        prov_window = connector2[x:x + w_width, y:y + w_height]
        if prov_window[int(w_width / 2), int(w_height / 2)] == 0:
            list_window.append(prov_window.flatten())
            list_labels.append('connector')

connector3 = cv2.imread('/Users/b.i.garkuwa/Desktop/MSc Project/Datasets/Judy4_anon_connectors.jpg', 0)
print(connector3.shape)

ret, connector3 = cv2.threshold(connector3, 180, 255, cv2.THRESH_BINARY)
for x in range(0, connector3.shape[0] - w_width, stepSize):
    for y in range(0, connector3.shape[1] - w_height, stepSize):
        prov_window = connector3[x:x + w_width, y:y + w_height]
        if prov_window[int(w_width / 2), int(w_height / 2)] == 0:
            list_window.append(prov_window.flatten())
            list_labels.append('connector')

connector4 = cv2.imread('/Users/b.i.garkuwa/Desktop/MSc Project/Datasets/Judy5_anon_connectors.jpg', 0)
print(connector4.shape)

ret, connector4 = cv2.threshold(connector4, 180, 255, cv2.THRESH_BINARY)
for x in range(0, connector4.shape[0] - w_width, stepSize):
    for y in range(0, connector4.shape[1] - w_height, stepSize):
        prov_window = connector4[x:x + w_width, y:y + w_height]
        if prov_window[int(w_width / 2), int(w_height / 2)] == 0:
            list_window.append(prov_window.flatten())
            list_labels.append('connector')

connector5 = cv2.imread('/Users/b.i.garkuwa/Desktop/MSc Project/Datasets/Judy6_anon_connectors.jpg', 0)
print(connector.shape)

ret, connector5 = cv2.threshold(connector5, 180, 255, cv2.THRESH_BINARY)
for x in range(0, connector5.shape[0] - w_width, stepSize):
    for y in range(0, connector5.shape[1] - w_height, stepSize):
        prov_window = connector5[x:x + w_width, y:y + w_height]
        if prov_window[int(w_width / 2), int(w_height / 2)] == 0:
            list_window.append(prov_window.flatten())
            list_labels.append('connector')

connector6 = cv2.imread('/Users/b.i.garkuwa/Desktop/MSc Project/Datasets/Judy7_anon_connectors.jpg', 0)
print(connector6.shape)

ret, connector6 = cv2.threshold(connector6, 180, 255, cv2.THRESH_BINARY)
for x in range(0, connector6.shape[0] - w_width, stepSize):
    for y in range(0, connector6.shape[1] - w_height, stepSize):
        prov_window = connector6[x:x + w_width, y:y + w_height]
        if prov_window[int(w_width / 2), int(w_height / 2)] == 0:
            list_window.append(prov_window.flatten())
            list_labels.append('connector')

connector7 = cv2.imread('/Users/b.i.garkuwa/Desktop/MSc Project/Datasets/Judy8_anon_connectors.jpg', 0)
print(connector7.shape)

ret, connector7 = cv2.threshold(connector7, 180, 255, cv2.THRESH_BINARY)
for x in range(0, connector7.shape[0] - w_width, stepSize):
    for y in range(0, connector7.shape[1] - w_height, stepSize):
        prov_window = connector7[x:x + w_width, y:y + w_height]
        if prov_window[int(w_width / 2), int(w_height / 2)] == 0:
            list_window.append(prov_window.flatten())
            list_labels.append('connector')

image = cv2.imread('/Users/b.i.garkuwa/Desktop/MSc Project/Datasets/Judy1_anon.jpg', 0)
print(image.shape)

ret, image = cv2.threshold(image, 180, 255, cv2.THRESH_BINARY)
for x in range(0, image.shape[0] - w_width, stepSize):
    for y in range(0, image.shape[1] - w_height, stepSize):
        prov_window = image[x:x + w_width, y:y + w_height]
        if prov_window[int(w_width / 2), int(w_height / 2)] == 0:
            test_window.append(prov_window.flatten())

image1 = cv2.imread('/Users/b.i.garkuwa/Desktop/MSc Project/Datasets/Judy2_anon.jpg', 0)
print(image1.shape)

ret, image1 = cv2.threshold(image1, 180, 255, cv2.THRESH_BINARY)
for x in range(0, image1.shape[0] - w_width, stepSize):
    for y in range(0, image1.shape[1] - w_height, stepSize):
        prov_window = image1[x:x + w_width, y:y + w_height]
        if prov_window[int(w_width / 2), int(w_height / 2)] == 0:
            test_window.append(prov_window.flatten())

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





