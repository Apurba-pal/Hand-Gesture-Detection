# print("before importing")
from cvzone.HandTrackingModule import HandDetector
import cv2 as cv
# print("after importing")

capture = cv.VideoCapture(0)
detector = HandDetector(maxHands=1)

# this method takes an integer like 0,1,2 (if you have a webcam) or a video path 
# the capture variable is an instance of this video capture class

while True:
    # here we grab the video frame by frame by utilising the capture.read() method 
    success, frame = capture.read()
    # reads the video frame by frame and a boolean which says that whether it was successfully read or not
    cv.imshow('Video', frame)
    hands, frame = detector.findHands(frame)
    # display each frame by this cv.imshow('Video', frame) code
    # to break out of this loop 
    if cv.waitKey(20) & 0xFF==ord('q'): # this basically says that if q is presses then stop the loop 
        break

capture.release()
cv.destroyAllWindows()
