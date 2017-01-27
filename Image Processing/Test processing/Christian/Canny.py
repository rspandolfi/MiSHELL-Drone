import cv2
import numpy as np

highthresh = 850
lowthresh = 300
edges = cv2.Canny(img,lowthresh,highthresh)
cv2.imshow('image',edges)