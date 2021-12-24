import cv2

destinationFile = 'inp.tif'
inpuDataset = cv2.imread('inp.tif', cv2.IMREAD_LOAD_GDAL)

format = 'JPEG'

inpuDataset = None
outputDataset = None

nycImage = cv2.imread(destinationFile, cv2.IMREAD_LOAD_GDAL & cv2.IMREAD_GRAYSCALE)

th, processedPic = cv2.threshold(nycImage, 65, 255, cv2.THRESH_BINARY)

cv2.imwrite(destinationFile, processedPic)
cv2.imshow('thresholded', processedPic)

cv2.waitKey(0)
cv2.destroyAllWindows()