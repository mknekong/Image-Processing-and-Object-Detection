# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 18:55:05 2019

@author: mankup
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread('C:/Users/mankup/Desktop/Spyder/Image Processing/a.jpg')
img2 = cv2.imread('C:/Users/mankup/Desktop/Spyder/Image Processing/alpha.jpg')

def display(img,cmap='gray'):
    fig = plt.figure(figsize = (12,10))
    ax = fig.add_subplot(111)
    ax.imshow(img,cmap='gray')

def Canny(img):
    
    med_value = np.median(img)
    #lower threshold
    lower= int(max(0,0.7*med_value))
    #upper threshold
    upper= int(min(255,1.3*med_value ))
    blurred_img = cv2.blur(img,ksize=(5,5))
    edges = cv2.Canny(image = blurred_img, threshold1 = lower, threshold2 = upper+50)
    display(edges)

Canny(img1)