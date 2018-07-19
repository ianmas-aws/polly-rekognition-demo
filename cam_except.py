import cv2

vidcap = cv2.VideoCapture()

if vidcap.open(1):
    print('Camera active')
    retval, image = vidcap.retrieve()
    vidcap.release()
else:
    print('Camera not active')
