import cv2
import mediapipe as mp
import pyautogui
camera = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w,screen_h= pyautogui.size()
while True:
    _,frame = camera.read()
    frame = cv2.flip(frame,1 )
    rgb_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    output  = face_mesh.process(rgb_frame)
    land_markpoint = output.multi_face_landmarks
    frame_h,frame_w, _ =frame.shape
    if land_markpoint:
        landmarks=land_markpoint[0].landmark
        for id, landmark in enumerate(landmarks[474:478]):
            x=int(landmark.x *frame_w)
            y=int(landmark.y * frame_h)
            cv2.circle(frame,(x,y),4,(0,255,0))
            if id==1:
                screen_x=int(landmark.x* screen_w)
                screen_y=int(landmark.y*screen_h)
                pyautogui.moveTo(screen_x,screen_y)
        right=[landmarks[44],landmarks[46]]
        left = [landmarks[145],landmarks[159]]
        for landmark in left:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 4, (0, 255, 255))
    if(left[0].y-left[1].y)<0.004:
        pyautogui.click()
        pyautogui.sleep(0)
        # for landmark in right:
        #     x = int(landmark.x * frame_w)
        #     y = int(landmark.y * frame_h)
        #     cv2.circle(frame, (x, y), 4, (0, 255, 255))
        # print(right[0].y - right[1].y)
        #     pyautogui.click()
        #     pyautogui.sleep(0.5)
    cv2.imshow('eye controlled mouse',frame)
    cv2.waitKey(1)
