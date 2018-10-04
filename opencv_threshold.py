'''
Created on 2018年5月8日

@author: user
'''
from openpyxl.chart import picture

if __name__ == '__main__':
    pass

import cv2
 
# Read image
src = cv2.imread("picture.jpg", cv2.IMREAD_GRAYSCALE)
 
# Set threshold and maxValue
thresh = 250

maxValue = 255
 
# Basic threshold example
th, dst = cv2.threshold(src, thresh, maxValue, cv2.THRESH_BINARY);

cv2.imshow('ww', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
