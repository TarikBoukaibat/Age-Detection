import cv2


def Detect_face(face, frame):
   frameHeight = frame.shape[0]
   frameWidth = frame.shape[1]
   blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300), [104, 117, 123], swapRB=False)
   face.setInput(blob)
   detection = face.forward()







capture = cv2.VideoCapture(0)
while True:
   ret,frame=capture.read()
   cv2.imshow("frame",frame)
   key=cv2.waitKey(1)
   if key==ord('q'):
      break

capture.release()
cv2.destroyAllWindows()














