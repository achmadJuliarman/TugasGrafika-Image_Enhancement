import cv2 as cv 
import numpy as np


img = cv.imread('saitama.png')
img = cv.resize(img, (700,400))
assert img is not None, "Citra Tidak Ditemukan"

# AVERAGING BLUR
averagingBlur = cv.blur(img, (12,12))

# GAUSSIAN BLUR
gaussianBlur = cv.GaussianBlur(img, (9,9),0)

# MEDIAN BLUR
medianBlur = cv.medianBlur(img, 7)   

# BILATERAL BLUR
bilateralBlur = cv.bilateralFilter(img,10,100,100)


cv.imshow('input citra', img)
cv.imshow('Averaging Blur', averagingBlur)
cv.imshow('Gaussian Blur', gaussianBlur)
cv.imshow('Median Blur', medianBlur)
cv.imshow('Bilateral Blur', bilateralBlur)
cv.waitKey()
cv.destroyAllWindows()
