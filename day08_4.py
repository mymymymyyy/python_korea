import cv2
import mediapipe as mp
# 만약에 웹캠이면 VideoCapture에 0을 넣고 맨 밑 waitKey에 1을 넣는다
cap = cv2.VideoCapture('imggg.jpg')         # 0 으로 입력하면 웹캠
mp_fd = mp.solutions.face_detection
mp_draw = mp.solutions.drawing_utils
fd = mp_fd.FaceDetection(0.5)         # 정확도 조정

success,img = cap.read()
img = cv2.resize(img, (500,700))
from_bgr_to_rbg = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
result = fd.process(from_bgr_to_rbg)

if result.detections:
    for id, detection in enumerate(result.detections):
        mp_draw.draw_detection(img,detection)

cv2.imshow('title',img)
cv2.waitKey(0)