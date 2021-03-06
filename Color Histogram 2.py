from PIL import Image
import matplotlib.pyplot as plt

def getRed(redVal):
    return '#%02x%02x%02x' % (redVal, 0, 0)

def getGreen(greenVal):
    return '#%02x%02x%02x' % (0, greenVal, 0)

def getBlue(blueVal):
    return '#%02x%02x%02x' % (0, 0, blueVal)

# Create an Image with specific RGB value
image = Image.open("E:/Github/Color-Histogram-by-Python/storage/Apples/sum/01.jpg")

# Modify the color of two pixels
image.putpixel((0,1), (1,1,5))
image.putpixel((0,2), (2,1,5))

# Get the color histogram of the image
histogram = image.histogram()

# Take only the Red counts
l1 = histogram[0:256]

# Take only the Blue counts
l2 = histogram[256:512]

# Take only the Green counts
l3 = histogram[512:768]

plt.subplot(3, 1, 1)

# R histogram
for i in range(0, 256):
    plt.bar(i, l1[i], color = getRed(i), edgecolor=getRed(i), alpha=0.3)

# G histogram
plt.subplot(3, 1, 2)
for i in range(0, 256):
    plt.bar(i, l2[i], color = getGreen(i), edgecolor=getGreen(i),alpha=0.3)

# B histogram
plt.subplot(3, 1, 3)
for i in range(0, 256):
    plt.bar(i, l3[i], color = getBlue(i), edgecolor=getBlue(i),alpha=0.3)
plt.show()