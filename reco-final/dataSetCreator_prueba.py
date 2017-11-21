import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

camera = cv2.VideoCapture(0)

nombre_id = raw_input('Introduce tu nombre: ')


#Abrimos el archivo donde se almacenan los usuarios registrados
# usuario_alejandro.1, usuario_alejandro.2, usuario_alejandro.3, usuario_alejandro.4 ...
with open('dataBase/usrs') as f:
	content = f.readline()
	while content:
		if id not in line:
			take_photos_id()
			break
		else:

	f.close()


#######################################################################
id = raw_input('Enter user Id: ')
cont = 0

while True:
	_, img = camera.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)

	for (x, y, w, h) in faces:
		cont += 1
		cv2.imwrite('dataSet/images/user_' + str(id) + '_' + str(cont) + '.jpg', gray[y:y+h, x:x+w])
		cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
		cv2.waitKey(100)

	cv2.imshow('Cara', img)
	cv2.waitKey(1)


	#(> <)
	if(cont > 15):
		break

camera.release()
cv2.destroyAllWindows()

#~#####################################################################




#Esta funcion saca fotos del usuario para almacenarlas en la base de datos junto a su id
def take_photos_id():

	for i in range(1, 11):

		_, img = camera.read()
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		faces = face_cascade.detectMultiScale(gray, 1.3, 5)

		for (x, y, w, h) in faces:
			img_num += 1
			cv2.imwrite('dataBase/img/usuario_' + str(nombre_id) + '.' + str(img_num) + '.jpg')
			pritn('dataBase/img/usuario_' + str(nombre_id) + '.' + str(img_num) + '.jpg')
			cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
			cv2.waitKey(100)

	cv2.imshow("Face", img)
	cv2.waitKey(1)




camera.release()
cv2.destroyAllWindows()



