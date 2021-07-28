import os
import numpy as np
import matplotlib.image as mpimg

def calc_distance(hist1, hist2):
    chi_squared = 0.5 * np.sum(np.divide(np.square((hist2 - hist1)), hist2 + hist1))
    return chi_squared


def is_duplicate(image1, image2, threshold=0.03):
    hist1_1, bins = np.histogram(image1[:64][:64], bins=255, density=True)
    hist1_2, bins = np.histogram(image1[64:][64:], bins=255, density=True)
    hist1_3, bins = np.histogram(image1[64:][:64], bins=255, density=True)
    hist1_4, bins = np.histogram(image1[:64][64:], bins=255, density=True)

    hist2_1, bins = np.histogram(image2[:64][:64], bins=255, density=True)
    hist2_2, bins = np.histogram(image2[64:][64:], bins=255, density=True)
    hist2_3, bins = np.histogram(image2[64:][:64], bins=255, density=True)
    hist2_4, bins = np.histogram(image2[:64][64:], bins=255, density=True)

    dist1 = calc_distance(hist1_1, hist2_1)
    dist2 = calc_distance(hist1_2, hist2_2)
    dist3 = calc_distance(hist1_3, hist2_3)
    dist4 = calc_distance(hist1_4, hist2_4)

    print(dist1, dist2, dist3, dist4, sep="\n")
    return dist1 < threshold and dist2 < threshold and dist3 < threshold and dist4 < threshold

try:
    for i in range(1, 5):
        for j in range(i, 5):
            print("-------------------------------------------------------------------------------")
            print("Apple " + str(i) + ".jpg", "Apple " + str(j) + ".jpg")

            pic_1 = mpimg.imread("Apple " + str(i) + ".jpg")
            pic_2 = mpimg.imread("Apple " + str(j) + ".jpg")
            hist1, bins = np.histogram(pic_1, bins=255)
            hist2, bins = np.histogram(pic_2, bins=255)
            if is_duplicate(hist1, hist2):
                os.remove("Apple " + str(j) + ".jpg")

except Exception as error:
    print(error)