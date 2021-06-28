import os
def main():
    paths = "E:/Github/Color-Histogram-by-Python/downloads/oranges/"
    for count, filename in enumerate(os.listdir(paths)):
        dst = "orange " + str(count) +".jpg"
        src = paths+filename
        dst = paths+dst
        print(filename)
        print(src)
        os.rename(src, dst)
if __name__ == '__main__':
    main()