import cv2
import numpy as np
#from matplotlib import pyplot as plt

img = cv2.imread('test.png',0)
edges = cv2.Canny(img,500,525)
cv2.imshow('edge-detect-sample',edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
