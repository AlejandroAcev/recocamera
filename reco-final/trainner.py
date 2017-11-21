import os
import cv2
import numpy as np
from PIL import Image

#Creamos nuestro propio reconocedor al que entrenaremos
recognizer = cv2.face.LBPHFaceRecognizer_create()
#Obtenemos la carpeta con los datos
path = "dataSet/images/"
face_cascade = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_alt.xml")
#face_cascade.load("recognizer/haarcascades/haarcascade_frontalface_default.xml")  getClass().getResource("recognizer/haarcascades/haarcascade_frontalface_alt.xml").getPath()
#Creamos una funcion que obtendra los ID de los usuarios
def getImageID(path):

	carpetas_imagenes = [os.path.join(path, persona) for persona in os.listdir(path)]

	for persona in os.listdir(path):

		carpeta = str(path) + str(persona)

		#Creamos un array vacio en el que guardaremos todas las caras y los id
		faces = []
		IDs = []

		#Abrimos la carpeta y cargamos todas las imagenes en un array
		for imagePath in os.listdir(carpeta):

			if imagePath in str("Thumbs.db"):
				continue

			else:
				#array_imagePaths = [os.path.join(carpeta, f) for f in os.listdir(persona)]
				#ruta_img = os.path.join(carpeta, imagePath)
				#print("Imagen: " + str(imagePath) + " --- Ruta_img: " + str(carpeta) + str(imagePath))
				
				try:
					#cargamos la imagen y la convertimos a gris para aumentar la velocidad de trabajo
					face_img = Image.open(os.path.join(carpeta, imagePath)).convert('L')

				except IOError:
					print("Pass")
					continue

				#la convertimos a formato numpy
				face_np = np.array(face_img, 'uint8')
				#Obtenemos el Id del usuario de la foto
				#ID = int(persona.replace('p', ''))
				ID = int(imagePath.replace("user_", "")[0])

				print(ID)

				img_faces = face_cascade.detectMultiScale(face_np, 1.3, 5)

				for (x, y, w, h) in img_faces:
					#Anadimos el Id al array de caras
					faces.append(face_np[y:y+h, x:x+w])
					IDs.append(ID)
					#Mostramos por pantalla la imagen
					cv2.imshow('Entrenamiento', face_np)
					cv2.waitKey(10)


				#Intentamos encontrar nuevamente la cara, en caso de ser un falso positivo se descarta
				"""try:
					img_faces = face_cascade.detectMultiScale(face_np, 1.1, 5)

					for (x, y, w, h) in img_faces:
						#Anadimos el Id al array de caras
						faces.append(face_np[y:y+h, x:x+w])
						IDs.append(ID)
						#Mostramos por pantalla la imagen
						cv2.imshow('Entrenamiento', face_np)
						cv2.waitKey(10)

				except:
					pass

				"""
				
	print("Fin de lectura")
	#Devolvemos los valores
	return IDs, faces


def __init__():

	#Invocamos la funcion
	array_Ids, array_faces = getImageID(path)
	#cv2.imshow('test', array_Ids[0])
	cv2.waitKey(1)

	#Entrenamos el reconocedor con las imagenes de las caras y los ID
	recognizer.train(array_faces, np.array(array_Ids))
	#Guardamos los datos en un archivo yml
	recognizer.write('dataSet/usrs/trainners/trainData.yml')
	cv2.destroyAllWindows()
	print("Entrenamiento finalizado")
	time.sleep(3)
	


