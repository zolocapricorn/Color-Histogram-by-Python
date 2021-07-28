import cv2
import os
import tqdm as t

totalFiles = 0
lists = ["Apple Braeburn", "Apple Crimson Snow", "Apple Golden 1", "Apple Golden 2",
         "Apple Golden 3", "Apple Granny Smith", "Apple Pink Lady", "Apple Red 1", "Apple Red 2",
         "Apple Red 3", "Apple Granny Smith", "Apple Red Delicious", "Apple Red Yellow 1",
         "Apple Red Yellow 2", "Banana", "Banana Lady Finger", "Banana Red", "Orange"]

for name in lists:
    paths = 'E:/Github/Color-Histogram-by-Python/fruits-360/Training/'+name+'/'
    for bases, dirs, files in os.walk(paths):
        for Files in files:
            totalFiles += 1
    print(totalFiles)

    for count in t.tqdm(range(totalFiles)):
        path = "E:/Github/Color-Histogram-by-Python/fruits-360/Training/%s/%02d.jpg" % (name, count)
        image = cv2.imread(path)
        out = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    totalFiles = 0