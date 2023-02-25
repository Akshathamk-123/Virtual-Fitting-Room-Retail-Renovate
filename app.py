import cv2
#The above is to import the computer vision library 
import mediapipe as mp
#The above is to import the mediapipe library that is developed by Google
#It has two main steps 
#Hand_tracking and Palm_tracking
import time
#This is to check the frame rate 
 
cap = cv2.VideoCapture(0)
#VideoCapture function is for Capturing the video from camera that is required.
# 0 is the front camera of the Laptop 
#Either ways
'''
while True:
    success, img =cap.read()

    cv2.imshow("Image",img)
    cv2.waitKey(1)

'''

while cap.isOpened():
    success, image = cap.read()

    cv2.imshow("Image",image)
    cv2.waitKey(1)