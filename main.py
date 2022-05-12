from distutils.errors import DistutilsSetupError
import imghdr
from tkinter import image_names
import cv2
import numpy
import os

# ファイル名をすべて列挙
files = os.listdir("./cv/bird")

# read_test_img = cv2.imread('./cv/bird/000002.jpg')
# resize_img = cv2.resize(read_test_img,(640,360))
# cv2.imwrite('test3.jpg',resize_img)

for file in files:
    read_imgpath = './cv/bird/' + file
    read_img = cv2.imread(read_imgpath)
    resize_img = cv2.resize(read_img,(640,360))
    cv2.imwrite(f"{file}r.jpg",resize_img)

# # ## グレースケール画像に変換 ##
# gray = cv2.cvtColor(resize_img, cv2.COLOR_BGR2GRAY)

# # ## 画像の白黒2値化 ##
# ret, thresh = cv2.threshold(gray, 190, 255, cv2.THRESH_BINARY

# # th = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,31,40)

# # # ## 輪郭を抽出 ##
# contrours,hierarcy = cv2.findContours(
#     gaues_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
