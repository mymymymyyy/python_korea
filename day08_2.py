import cv2

# pip install python-opencv
# pip install opencv-python
def 이미지띄우기(img_path):
    # 이미지 읽어줘
    img = cv2.imread('person.jpg')
    # 이미지 보여줘
    cv2.imshow('title',img)
    # 무한대기
    cv2.waitKey(0)


def ShowVideo(video_path):
    # 동영상 읽어줘
    vc = cv2.VideoCapture(video_path)
    # 무한반복
    while True:
        success,img = vc.read()
        # 동영상을 성공적으로 읽었으면
        if success:
            cv2.imshow('title',img)
            cv2.waitKey(20)


# ShowImage('person.jp g) 이거 키면 사진뜸
ShowVideo('video.mp4')
