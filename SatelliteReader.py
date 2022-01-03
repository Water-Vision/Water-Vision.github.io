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

    def filteringComparison(filepath):
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

        cv2.imshow('Original', img)
        cv2.imwrite('Original.tif', img)

        cv2.imshow('Global Thresholding V=127', th1)
        cv2.imwrite('GlobalThresholding.tif', th1)

        cv2.imshow('AdaptiveMeanThresholding', th2)
        cv2.imwrite('AdapMeanThresh.tif', th2)

        cv2.imshow('AdaptiveGaussianThresholding', th3)
        cv2.imwrite('AdapGaussThresh.tif', th3)

        plt.show()

    def filteringComparison2(filepath):
        img = cv2.imread(filepath, 0)

        # global thresholding
        ret1, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

        # Otsu's thresholding
        ret2, th2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        # Otsu's thresholding after Gaussian filtering
        blur = cv2.GaussianBlur(img, (5, 5), 0)
        ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        cv2.imwrite('Otsu.tif', th3)
        cv2.imshow('otsu', th3)

        cv2.imwrite('GaussianFiltered.tif', th3)
        cv2.imshow('GaussianFiltered', th3)

        # plot all the images and their histograms
        images = [img, 0, th1,
                  img, 0, th2,
                  blur, 0, th3]
        titles = ['Original Noisy Image', 'Histogram', 'Global Thresholding (v=127)',
                  'Original Noisy Image', 'Histogram', "Otsu's Thresholding",
                  'Gaussian filtered Image', 'Histogram', "Otsu's Thresholding"]
        for i in range(3):
            plt.subplot(3, 3, i * 3 + 1), plt.imshow(images[i * 3], 'gray')
            plt.title(titles[i * 3]), plt.xticks([]), plt.yticks([])
            plt.subplot(3, 3, i * 3 + 2), plt.hist(images[i * 3].ravel(), 256)
            plt.title(titles[i * 3 + 1]), plt.xticks([]), plt.yticks([])
            plt.subplot(3, 3, i * 3 + 3), plt.imshow(images[i * 3 + 2], 'gray')
            plt.title(titles[i * 3 + 2]), plt.xticks([]), plt.yticks([])
        plt.show()