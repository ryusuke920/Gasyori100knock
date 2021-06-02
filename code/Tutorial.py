import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import io

#img = io.imread('https://yoyoyo-yo.github.io/Gasyori100knock/dataset/images/imori_256x256.png')

#plt.imshow(img) 画像を出力
#print(img.shape) # 縦・横・３チャンネルを抽出
#print(img.dtype) # uint8 とは符号なしintで8ビットを意味するもの
#print(img[20, 30, 1]) # x=20, y=30のGの値を抽出
#print(img[20, 30:33]) # スライスで横方向にスライドしたデータを得られる

"""
subplot を使うには、3 つの引数を渡す必要があり、subplot(2, 2, 1) のように利用する（省略して subplot(221) としても可）。
最初の 2 つの引数は、分割数を表す。描画キャンパスを何行に分割するのかを 1 番目の引数で指定し、何列に分割するのかを 2 番目の引数で指定する。
3 番目の引数に、これからグラフを描くのに利用するサブ領域の番号を入れる。
例えば、描画キャンパスを 4 分割してあれば、サブ領域の番号は 1, 2, 3, 4 と決められている。
基本的に、上から下、左から右の順位で、領域の番号がつけられる。
"""

"""
img2 = img.copy()
img2[110:120, 370:420] = 0
fig, ax = plt.subplots(1, 2) # Figureオブジェクトとそれに属する一つのAxesオブジェクトを同時に作成
ax[0].imshow(img)
ax[1].imshow(img2)
plt.show()
"""

"""
# 260をuint8型に直すと260-256が起きて、４になってしまう
img = io.imread('https://yoyoyo-yo.github.io/Gasyori100knock/dataset/images/imori_256x256.png')
img[120:180, 120:180, 0] = 260
plt.imshow(img)
plt.show()
"""

"""
# intでしか計算できないので float -> 計算 -> int に変換する
img = io.imread('https://yoyoyo-yo.github.io/Gasyori100knock/dataset/images/imori_256x256.png')
img = img.astype(np.float32)
img[120:180, 120:180] *= 0.5
img = img.astype(np.uint8)
plt.imshow(img)
plt.show()
"""

img = io.imread('https://yoyoyo-yo.github.io/Gasyori100knock/dataset/images/imori_256x256.png')
h, w, c = img.shape # 縦、横、チャンネル
img[:h-1, :w-1] = img[:h-1, :w-1, ::-1]
plt.imshow(img)
plt.show()