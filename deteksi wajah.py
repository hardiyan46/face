"""
https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
"""
import cv2

cam = cv2.VideoCapture(0)
cam.set(3, 640)  # merubah lebar
cam.set(4, 480)  # merubah tinggi
facedetektor = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')  #baca algoritma face detektor
eyedetektor = cv2.CascadeClassifier('haarcascade_eye.xml')   #baca algoritma eye detektor
while True:
    retV, frame = cam.read()
    abu = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # merubah dari color ke abu abu
    face = facedetektor.detectMultiScale(abu, 1.3, 5)  # frame, scalefactor,
    for (x, y, w, h) in face:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
        roiabu = abu[y:y + h, x:x + w]
        roiwarna = frame[y:y + h, x:x + w]
        eye = eyedetektor.detectMultiScale(roiabu)
        for (xe, ye, we, he) in eye:
            cv2.rectangle(roiwarna, (xe, ye), (xe + we, ye + he), (0, 0, 255), 1)

    cv2.imshow('my face', frame)  # menampilkan windows dengan nama frame
    # cv2.imshow('my face2', abu)   #tampilkan frame abu abu
    k = cv2.waitKey(1) & 0xFF
    if k == 27 or k == ord('q'):  # key close dengan Q dan ESC
        break
cam.release()
cv2.destroyAllWindows()
