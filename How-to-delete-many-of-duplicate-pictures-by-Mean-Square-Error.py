# Concept
# นำภาพมาลบกัน โดยภาพที่นำมาลบกันจะต้อง resize ก่อน ซึ่งควรจะ resize เป็นภาพเล็กๆ
# เมื่อนำภาพมาลบกันเสร็จ เราจะได้ Error ให้นำ error ทั้งหมด มาคิด MSE --> MSE เอาไว้เทียบแค่ภาพ 2 ภาพ
# ถ้าห่างกันน้อยอาจจะมีความเป็นไปได้สูงที่เป็นภาพเดียวกัน (RMSE)
# ค่า RMSE ต้องมากเกิน 500 ถ้าน้อยกว่านับว่าเป็นภาพซ้ำ ให้ลบ เว้นเสียแต่ว่าภาพนั้นจะเป็นภาพเดียวกัน นั่นก็คือ มีตำแหน่งเดียวกันกับต้นฉบับ
# จากนั้นทำการลบภาพ

import os
import cv2
import tqdm as t
import numpy as np
import matplotlib.pyplot as plt

totalFiles = 0
data = []
point = []
result = []
check = []
count = 0

path_prototype = 'E:/Github/Color-Histogram-by-Python/storage/Oranges/sum/'
for bases, dirs, files in os.walk(path_prototype):
    for Files in files:
        totalFiles += 1

for prototype in t.tqdm(range(count+1, totalFiles+1)):
    path1 = 'E:/Github/Color-Histogram-by-Python/storage/Oranges/sum/%02d.jpg' % (prototype)
    for walk in t.tqdm(range(count+2, totalFiles+1)):
        path2 = 'E:/Github/Color-Histogram-by-Python/storage/Oranges/sum/%02d.jpg' % (walk)

        # Read pic and set colour
        image_1 = cv2.imread(path1)
        image_2 = cv2.imread(path2)

        # Resize
        size1 = cv2.resize(image_1, (256, 256))
        size2 = cv2.resize(image_2, (256, 256))

        # Change pic to hist
        hist1, bins1 = np.histogram(size1, bins=256)
        hist2, bins2 = np.histogram(size2, bins=256)

        # Find Root Mean Square Error (RMSE)
        rmse = np.sqrt(np.mean(pow(np.subtract(hist1, hist2), 2)))
        if rmse <= 100:
            point.append(walk)
            check.append((prototype, walk, rmse))
    count += 1
    data.append(point)
    point = []
    for number in data:
        for innumber in number:
            if innumber not in result:
                result.append(innumber)
print(sorted(result))
# Delete
if len(result) > 0:
    for delete in t.tqdm(sorted(result)):
        if os.path.exists("E:/Github/Color-Histogram-by-Python/storage/Oranges/sum/%02d.jpg" % (delete)):
            os.remove("E:/Github/Color-Histogram-by-Python/storage/Oranges/sum/%02d.jpg" % (delete))

# mse = 256
# Apple 336 --> 313
# Banana 412 --> 331
# Orange 194 --> 169

# mse = 100
# Apple 335 --> 334
# Banana 417 --> 416
# Orange 193 --> 189
