# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 19:07:00 2019

@author: mankup
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread('C:/Users/mankup/Desktop/Spyder/Image Processing/a.jpg')
img2 = cv2.imread('C:/Users/mankup/Desktop/Spyder/Image Processing/alpha.jpg')

def contour(img):
    image,contours,hierarchy = cv2.findContours(img, cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)
    external_contours = np.zeros(image.shape)
    for i in range(len(contours)):
        #External Conti=our
        if hierarchy[0][i][3] == -1:
            cv2.drawContours(external_contours, contours, i , 255, -1)
            
    plt.imshow(external_contours, cmap='gray')
    
    
    internal_contours = np.zeros(image.shape)
    
    for i in range(len(contours)):
        #Internal contours
        if hierarchy[0][i][3] != -1"
        cv2.drawContours(external_contours, contours, i, 255,-1)

contour(img1)



plt.imshow(img1,cmap='gray')