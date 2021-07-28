import cv2
import matplotlib.pyplot as plt

lists, count = [], 1
for i in range(1, 3):
    imagep = cv2.imread("E:/Github/Color-Histogram-by-Python/storage/Apples/sum/Apple "+str(i)+".jpg")
    for j in range(1, 3):
        imagew = cv2.imread("E:/Github/Color-Histogram-by-Python/storage/Apples/sum/Apple "+str(j)+".jpg")
        think1 = imagep - imagew
        summa = sum(sum(sum(think1)))
        if 0 <= summa <= 0.3 and i != j:
            lists.append(count)
        print(sum(sum(think1)))
        # print(summa)
        # print(count)
        count += 1
print(lists)
