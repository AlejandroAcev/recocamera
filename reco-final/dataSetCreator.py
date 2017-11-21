
import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

camera = cv2.VideoCapture(0)

id = raw_input('Enter user Id: ')
cont = 0

while True:
	_, img = camera.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)

	for (x, y, w, h) in faces:
		cont += 1
		cv2.imwrite('dataSet/user.' + str(id) + '.' + str(cont) + '.jpg', gray[y:y+h, x:x+w])
		cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
		cv2.waitKey(100)

	cv2.imshow('Cara', img)
	cv2.waitKey(1)


	#(> <)
	if(cont > 15):
		break

camera.release()
cv2.destroyAllWindows()














