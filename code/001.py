# Q.1 チャネル入れ替え
import numpy as np
import matplotlib.pyplot as plt
import cv2
from skimage import io

img_orig = io.imread('https://yoyoyo-yo.github.io/Gasyori100knock/dataset/images/imori_256x256.png')

def rgb2bgr(img):
    return img[..., ::-1]

img_bgr = rgb2bgr(img_orig)

plt.figure(figsize=(12, 3)) # figsizeは全体のサイズを指定する
plt.subplot(1, 2, 1)
plt.title('input')
plt.imshow(img_orig)
plt.subplot(1, 2, 2)
plt.title('answer')
plt.imshow(img_bgr)
plt.show()