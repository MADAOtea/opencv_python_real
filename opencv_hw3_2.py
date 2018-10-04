'''
Created on 2018年6月26日

@author: user
'''

import numpy as np
import cv2
from matplotlib import pyplot as plt
from cv2 import imshow
from haha.HelloWorld import dst

if __name__ == '__main__':
    pass


bear = cv2.imread('bear.jpg')
bk = cv2.imread('bk_beach.jpg')



rows,cols,channels = bear.shape
roi = bk[0:rows,0:cols]
     
dst2=cv2.addWeighted(bear,0.5,roi,0.5,0)
bk[0:rows,0:cols] = dst2 

cv2.imshow('w', bk)

cv2.waitKey(0)
