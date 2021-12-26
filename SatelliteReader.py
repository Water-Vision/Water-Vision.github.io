import cv2 as cv2
import numpy as np
from matplotlib import pyplot as plt
from ReaderAbstract import ReaderAbstract

class SatelliteReader(ReaderAbstract):
    def __init__(self):
        if not type(self) is SatelliteReader:
            raise Exception('Reader is NOT a SatelliteReader')
        # Any initialization code
        print('In the __init__  method of the SatelliteReader class')

    def extractHouseData(filepath):
        destinationFile = filepath

        nycImage = cv2.imread(destinationFile, cv2.IMREAD_GRAYSCALE)

        # refer https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html
        th, processedPic = cv2.threshold(nycImage, 100, 255, cv2.THRESH_TOZERO)

        cv2.imwrite('newHouse.tif', processedPic)
        cv2.imshow('thresholded', processedPic)

        #cv2.imshow('original', destinationFile)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def extractWaterData(filepath):
        img = cv2.imread(filepath, 0)
        img = cv2.medianBlur(img, 5)
        ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
        th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, \
                                   cv2.THRESH_BINARY, 11, 2)
        th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
                                   cv2.THRESH_BINARY, 11, 2)
        titles = ['Original Image', 'Global Thresholding (v = 127)',
                  'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
        images = [img, th1, th2, th3]
        for i in range(4):
            plt.subplot(2, 2, i + 1), plt.imshow(images[i], 'gray')
            plt.title(titles[i])
            plt.xticks([]), plt.yticks([])
        plt.show()