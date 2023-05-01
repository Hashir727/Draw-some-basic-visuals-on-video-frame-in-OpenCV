import cv2
import numpy as np

cap = cv2.VideoCapture(1)

while True:
    _, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    img = cv2.line(frame, (0,0), (width, height), (0,255,0), 5)
    img = cv2.line(img, (0, height), (width, 0), (0,0,255), 5)
    img = cv2.rectangle(img, (150,150), (350,350), (128,128,128), 5)
    img = cv2.circle(img, (300,300), (90), (255,0,0), 5)
    img = cv2.putText(img, "Hello World", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255), 3, cv2.LINE_AA)

    cv2.imshow('img', img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
