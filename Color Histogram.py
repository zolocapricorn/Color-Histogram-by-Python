import cv2
import numpy as np
import sklearn.neighbors as sn
import matplotlib.pyplot as plt

featureTr = [];
labelTr = [];
path = 'banana20.png'
image = cv2.imread(path)
RGB = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
red = RGB[0, :, :].reshape(1, -1);
green = RGB[:, 0, :].reshape(1, -1);
blue = RGB[:, :, 0].reshape(1, -1);
histr, binsr = np.histogram(red, bins = np.arange(-1, 256, 1))
histg, binsg = np.histogram(green, bins = np.arange(-1, 256, 1))
histb, binsb = np.histogram(blue, bins = np.arange(-1, 256, 1))
plt.hist(histr, binsr, label = "red", color = "red")
plt.hist(histg, binsg, label = "green", color = "green")
plt.hist(histb, binsb, label = "blue", color = "blue")
plt.show()