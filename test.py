import tensorflowpredict
import cv2

im=cv2.imread("C:\group14\datasets\Med clg\\3\\10.jpeg")


print(tensorflowpredict.loadeverything(im))