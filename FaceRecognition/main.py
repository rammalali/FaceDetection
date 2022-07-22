import cv2
import time
from matplotlib import pyplot as plt
import numpy as np


face_xml = r'ProfileFace.xml'
face_detector = cv2.CascadeClassifier(face_xml)

def detect_object(image):
    face_list = face_detector.detectMultiScale(image, scaleFactor=1.06, minNeighbors=1, minSize=(70, 80))
    # print(face_list)

    for obj in face_list:
        (x, y, w, h) = obj
        start = (x, y)
        end = (x+w, y+h)
        # print(obj)
        image = cv2.rectangle(image, start, end, (0, 255, 0), 2)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # plt.imshow(image)
    # plt.show()
    print(face_list)
    if face_list is ():
        print('None')
        return None

    return face_list

cap = cv2.VideoCapture(0)
count = 0

prev_frame_time = 0

new_frame_time = 0

while True:
    ret, frame = cap.read()
    new_frame_time = time.time()
    fps = 1/(new_frame_time - prev_frame_time)
    prev_frame_time = new_frame_time
    try:
        if detect_object(frame) is not None:
            print('found')
            print(detect_object(frame)[0])
            (x, y, w, h) = detect_object(frame)[0]
            start = (x, y)
            end = (x + w, y + h)
            frame = cv2.rectangle(frame, start, end, (0, 255, 0), 2)
            cv2.putText(frame, str(fps), (20, 20), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)
            cv2.putText(frame, 'found', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow('frame', frame)
            # face = cv2.resize(detect_object(frame), (400, 400))
            # cv2.putText(face, ' ', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
        else:
            print('not f')
            cv2.putText(frame, str(fps), (20, 20), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)
            cv2.putText(frame, 'notfound', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
            cv2.imshow('frame', frame)
            pass
        if cv2.waitKey(1) == 0:
            break
    except:
        pass
cap.release()
cv2.destroAllWindows()
image_path =r'Messi_face.jpg'
image = cv2.imread(image_path)
detect_object(image)