from xml.sax.handler import feature_namespaces
import cv2
import numpy
import os

img = cv2.imread('./cv/bird/000024.jpg')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

custom_cascade = cv2.CascadeClassifier('./cv/cascade/cascade.xml')

write_rect_img =  custom_cascade.detectMultiScale(gray)

for x,y,w,h in write_rect_img:
  cv2.rectangle(img,(x,y),(x+w,y+h),color=(0,255,0),thickness=2)

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
