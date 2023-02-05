# opencv 모듈추가
# mediapipe 모듈 추가
import cv2
import mediapipe as mp








# 이미지   #이르,ㅁ
def ShowImage(img_path):
    img = cv2.imread('img2.jpg')
    cv2.putText(img,f'hello',(550,400),cv2.FONT_ITALIC,2,(255,0,255),2)
    cv2.imshow('title',img)
    cv2.waitKey(0)
ShowImage('img2.jpg')
















# 동영상
def ShowVideo(video_path):
    vc = cv2.VideoCapture(video_path)
    while True:
        success,img = vc.read()
        if success:
            cv2.imshow('title',img)
            cv2.waitKey(20)
ShowVideo('video2.mp4')