'''
Created on 2018年6月4日

@author: user
'''
from cv2 import waitKey

if __name__ == '__main__':
    pass

import cv2
import numpy as np

img = cv2.imread('img.jpg')
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create()
kp = sift.detect(img,None)

kpimg = cv2.drawKeypoints(gray, kp, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('yo',kpimg)


waitKey(0)