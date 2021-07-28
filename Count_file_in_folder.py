import os
import tqdm as t

lists = ["Apple Braeburn", "Apple Crimson Snow", "Apple Golden 1", "Apple Golden 2",
         "Apple Golden 3", "Apple Granny Smith", "Apple Pink Lady", "Apple Red 1", "Apple Red 2",
         "Apple Red 3", "Apple Granny Smith", "Apple Red Delicious", "Apple Red Yellow 1",
         "Apple Red Yellow 2", "Banana", "Banana Lady Finger", "Banana Red", "Orange"]
totalFiles = 0
# totalDir = 0

for name in lists:
    APP_FOLDER = 'E:/Github/Color-Histogram-by-Python/fruits-360/Training/' + name + '/'
    for bases, dirs, files in t.tqdm(os.walk(APP_FOLDER)):
        # print('Searching in : ',base)
        # for directories in dirs:
        #     totalDir += 1
        for Files in files:
            totalFiles += 1
    print('Total number of files',totalFiles)
    # print('Total Number of directories',totalDir)
    # print('Total:',(totalDir + totalFiles))