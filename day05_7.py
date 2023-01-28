# import 가 안되는 이유 : 설치가 안된 라이브러리 (모듈) 또는 오타
# 외부 모듈 설치 : pip install 모듈명

# pip install opencv-python       아나콘다
# pip install python-opencv        일반
import cv2

# 이미지 = cv2.imread('img 1.png')           #이미지 보여줘
# cv2.imshow('title',이미지)             #보여줘

# cv2.waitKey(0)                  #무한대기


# 이미지 = cv2.imread('img2.webp')           #이미지 보여줘
# cv2.imshow('title',이미지)             #보여줘

# cv2.waitKey(0)

def cv_img(path):
    이미지 = cv2.imread(path)          
    cv2.imshow('title',이미지)             
    cv2.waitKey(0)

cv_img('../tree.png')