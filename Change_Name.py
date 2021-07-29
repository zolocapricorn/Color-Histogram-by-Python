import os
def main():
    lists = [""]
    for name in lists:
        paths = "E:/Github/Color-Histogram-by-Python/storage/Oranges/sum/"
        for count, filename in enumerate(os.listdir(paths)):
            dst = "%02d.jpg" % (count+1)
            src = paths+filename
            dst = paths+dst
            os.rename(src, dst)
if __name__ == '__main__':
    main()