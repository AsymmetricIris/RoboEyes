import cv2
import numpy as np

cap = cv2.VideoCapture(0)
 
while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    zoomCoefficient = (int)(2)
    grayShape = gray.shape
    graySizeY = (int)(gray.shape[0])
    graySizeX = (int)(gray.shape[1])
    grayCentreY = (int)(graySizeY/2)
    grayCentreX = (int)(graySizeX/2)
    zoomedImg = gray[(grayCentreY - (int)((graySizeY/2)/zoomCoefficient)) : (grayCentreY + (int)((graySizeY/2)/zoomCoefficient)), (grayCentreX - (int)((graySizeX/2)/zoomCoefficient)) : (grayCentreX + (int)((graySizeX/2)/zoomCoefficient))]
 
    cv2.imshow('frame',zoomedImg)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()