# importing google_images_download module
from google_images_download import google_images_download
import os

# creating object
response = google_images_download.googleimagesdownload()

search_queries =["apple fruits jpg"]


def downloadimages(query):
    # keywords is the search query
    # format is the image file format
    # limit is the number of images to be downloaded
    # print urs is to print the image file url
    # size is the image size which can
    # be specified manually ("large, medium, icon")
    # aspect ratio denotes the height width ratio
    # of images to download. ("tall, square, wide, panoramic")
    arguments = {"keywords": query,
                 "limit": 100,
                 "print_urls": True,
                 "image_directory": "apples",
                 "chromedriver": "C:/Program Files/Google/Chrome/Application/chromedriver.exe"}
    try:
        response.download(arguments)

    # Handling File NotFound Error
    except FileNotFoundError:
        arguments = {"keywords": query,
                     "limit": 100,
                     "print_urls": True,
                     "image_directory": "apples",
                     "chromedriver": "C:/Program Files/Google/Chrome/Application/chromedriver.exe"}

        # Providing arguments for the searched query
        try:
            # Downloading the photos based
            # on the given arguments
            response.download(arguments)
        except:
            pass

# Driver Code
for query in search_queries:
    downloadimages(query)
# Change name
def main():
    paths = "E:/Github/Color-Histogram-by-Python/downloads/apples/"
    for count, filename in enumerate(os.listdir(paths)):
        dst = "apple " + str(count+1) +".jpg"
        src = paths+filename
        dst = paths+dst
        os.rename(src, dst)
if __name__ == '__main__':
    main()