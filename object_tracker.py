# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 03:31:17 2019

@author: mankup
"""

import cv2

def select_tracker():
    print("WELCOME!, Please choose the tracker")
    print("0 BOOSTING")
    print("1  MIL")
    print("2 KCF")
    print("3 TLD")
    print("4 MEDIANFLOW")
    choice = input("Please select your tracker")
    
    if choice == '0':
        tracker = cv2.TrackerBoosting_create()
    if choice == '1':
        tracker = cv2.TrackerMIL_create()
    if choice == '2':
        tracker = cv2.TrackerKCF_create()
    if choice == '3':
        tracker = cv2.TrackerTLD_create()
    if choice == '4':
        tracker = cv2.TrackerMedianFlow_create()
    
    return tracker

tracker = select_tracker()
tracker_name = str(tracker).split()[0][1:]

cap = cv2.VideoCapture(0)
ret,frame = cap.read()

roi = cv2.selectROI(frame, False)

ret = tracker.init(frame, roi)

while True:
    ret, frame = cap.read()
    
    #ROI = region of Interest
    success, roi = tracker.update(frame)
    
    (x,y,w,h) = tuple(map(int, roi))
    
    if success:
        p1= (x,y)
        p2 = (x+w, y+h)
        cv2.rectangle(frame, p1,p2, (0,255,0), 3)
        
    else:
        cv2.putText(frame, "Failure to Detect", (20,400), cv2.FONT_HERSHEY_SIMPLE,1,(0,255,0),3)
    cv2.putText(frame,tracker_name, (20,400), cv2.FONT_HERSHEY_SIMPLE, 1, (0,255,0),1)
    cv2.imshow(tracker_name,frame)
    
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
    
