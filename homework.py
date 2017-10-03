#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 02:20:04 2017

@author: adafactor
"""

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

mask = cv.imread('line2.jpg', 0)
img = cv.imread('sj.jpg',0)

mask = cv.resize(mask, (300, 300), interpolation = cv.INTER_CUBIC)

fmask = np.fft.fft2(mask)
fimg = np.fft.fft2(img)
fsImg = np.fft.fftshift(fimg)
fsMask = np.fft.fftshift(fmask)
res = fsMask+fsImg


mag = np.log(np.abs(res))
inv = np.fft.ifftshift(res)
inv  = np.abs(np.fft.ifft2(inv))
plt.subplot(131),plt.imshow(img, cmap='gray')
plt.title('Input'), plt.xticks([]), plt.yticks([])

plt.subplot(132),plt.imshow(mag, cmap='gray')
plt.title('Magnitude'), plt.xticks([]), plt.yticks([])

plt.subplot(133),plt.imshow(inv, cmap='gray')
plt.title('Reconstruct'), plt.xticks([]), plt.yticks([])

plt.show()