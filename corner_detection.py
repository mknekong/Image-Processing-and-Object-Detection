# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 15:59:29 2019

@author: mankup
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt


img1 = cv2.imread('C:/Users/mankup/Desktop/Spyder/Image Processing/a.jpg')
img2 = cv2.imread('C:/Users/mankup/Desktop/Spyder/Image Processing/a4.jpg')


def Haris(img1):
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    gray_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    
    #img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
    #gray_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    
    gray = np.float32(gray_img1)
    dst = cv2.cornerHarris(src = gray, blockSize = 2, ksize = 3, k = 0.04)
    dst = cv2.dilate(dst, None)
    img1[dst>0.01*dst.max()] = [255,0,0]
    
    
    plt.imshow(img1,cmap='gray')
    #plt.imshow(gray_img2,cmap='gray')
    

#Haris(img1)
    
#Shi Thomasi
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
gray_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
gray_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
def ShiThomasi(img):
    #detect 5 corners (img,5,)
    corners = cv2.goodFeaturesToTrack(img, 5, 0.01,10)
    corners = np.int0(corners)
    for i in corners:
        x,y = i.ravel()
        cv2.circle(img,(x,y),3,(255,0,0),-1)
    plt.imshow(img)
        
ShiThomasi(gray_img1)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    