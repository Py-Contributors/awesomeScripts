import cv2
import winsound
cam = cv2.VideoCapture(0)
while cam.isOpened():
    ret,frame_1 = cam.read()
    ret,frame_2 = cam.read()
    diff = cv2.absdiff(frame_1,frame_2)
    gray = cv2.cvtColor(diff,cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5) , 0 )
    _,thresh = cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh,None,iterations=3)
    contours,_= cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE )
    # cv2.drawContours(frame_1,contours, -1,(0,254,0),2)
    for c in contours:
        if cv2.contourArea(c)<5000:
            continue
        x,y,w,h= cv2.boundingRect(c)
        cv2.rectangle(frame_1,(x,y),(x+w,y+h),(195, 212, 255),2)
        winsound.PlaySound("nuclear-alarm-6997.mp3",winsound.SND_ASYNC)
        # winsound.Beep(2000,100)
    if cv2.waitKey(10) == ord('q'):
        break
    cv2.imshow('cam',frame_1)
