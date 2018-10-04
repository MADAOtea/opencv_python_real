'''
Created on 2018年5月30日

@author: user
'''
#coding=utf-8 

if __name__ == '__main__':
    pass

import cv2 
import numpy as np

img = cv2.imread('test1.png',0)  
img2 = img.copy() 
kernel = np.ones((11,11), np.uint8)
i = 0 

for i in range(200):
  img2 = cv2.morphologyEx(img2, cv2.MORPH_CLOSE, kernel)    

cv2.imshow("closing", img2 );  
cv2.imshow("source", img);  
cv2.waitKey(0)  
cv2.destroyAllWindows() 