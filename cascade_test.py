from xml.sax.handler import feature_namespaces
import cv2
import numpy
import os

# 画像を読み込む(検出したい画像を指定する)
img = cv2.imread('./cv/newbird/img02.jpg')
# 画像を指定したサイズにリザイス
resize_img = cv2.resize(img,(640,360))
# 画像をグレー化
gray = cv2.cvtColor(resize_img,cv2.COLOR_BGR2GRAY)

# 作成したカスケードファイルを読み込む
custom_cascade = cv2.CascadeClassifier('./cv/birdcascade/cascade.xml')

# 画像から該当する箇所を検出する
write_rect_img = custom_cascade.detectMultiScale(gray, scaleFactor=1.11, minNeighbors=10,minSize=(200,200))

# 検出した箇所を囲む
for x,y,w,h in write_rect_img:
  cv2.rectangle(resize_img,(x,y),(x+w,y+h),color=(0,255,0),thickness=2)

# 画像を表示する
cv2.imshow('image', resize_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
