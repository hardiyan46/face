import cv2
cam = cv2.VideoCapture(0)

while True:
    retV, frame = cam.read()
    abu = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  #merubah dari color ke abu abu
    cv2.imshow('my face', frame)   #menampilkan windows dengan nama frame
    cv2.imshow('my face2', abu)
    k = cv2.waitKey(1) & 0xFF
    if  k == 27 or k == ord('q'): #key close dengan Q dan ESC
        break
cam.release()
cv2.destroyAllWindows()