# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 16:27:33 2019

@author: mankup
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

def display(img,cmap='gray'):
    fig = plt.figure(figsize = (12,10))
    ax = fig.add_subplot(111)
    ax.imshow(img,cmap='gray')
    

img1 = cv2.imread('C:/Users/mankup/Desktop/Spyder/Image Processing/a.jpg')
img2 = cv2.imread('C:/Users/mankup/Desktop/Spyder/Image Processing/alpha.jpg')

#Brute force detection with ORB descriptors

def ORB(img1,img2):
    orb = cv2.ORB_create()
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)
    
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)
    matches1 = bf.match(des1,des2)#see where it is matching
    matches1 = sorted(matches1, key = lambda x: x.distance)
    
    matches2 = cv2.drawMatches(img1,kp1,img2,kp2,matches1[:105],None,flags = 2)
    display(matches2)

#MUCH BETTER MATCHER
def SIFT(img1,img2):
    sift = cv2.xfeatures2d.SIFT_create()
    kp1, des1 = sift.detectAndCompute(img1,None)
    kp2, des2 = sift.detectAndCompute(img2,None)
    
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1,des2,k=2)
    
    good = []
    #RATIO TEST
    #LESS DISTANCE THE BETTER THE MATCH
    for match1,match2 in matches:
        if match1.distance < 0.75* match2.distance:
            good.append([match1])
    sift_matches = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good, None, flags = 2)
            
            
    display(sift_matches)

def FLANN(img1,img2):
    sift = cv2.xfeatures2d.SIFT_create()
    kp1, des1 = sift.detectAndCompute(img1,None)
    kp2, des2 = sift.detectAndCompute(img2,None)
    
    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithms = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks = 50)
    flann = cv2.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(des1,des2,k=2)
    good=[]
    for match1,match2 in matches:
        if match1.distance < 0.75* match2.distance:
            good.append([match1])
    flann_matches = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good, None, flag = 2)
    display(flann_matches)
    
FLANN(img1,img2)
    
    

#ORB(img1,img2)
#SIFT(img1,img2)