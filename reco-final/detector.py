import cv2
import numpy as np
import os.path


font = cv2.FONT_HERSHEY_SIMPLEX

class Usuario():
	"""Esta clase recibe un id y un nombre como parametros para poder centrar la informacion de los usuarios en un solo objeto"""
	def __init__(self, id, nombre, photos):
		self.id = id
		self.nombre = nombre
		self.photos = photos


def load_all_users():

	list_usuarios = []

	archivo = "dataSet/usrs/usuarios.dat"
	linea = open(archivo, "r")
	cont = 0
	for line in linea:
		num_id, nom, _ = line.split('=')
		pers = Usuario(num_id, nom, _)
		list_usuarios.append(pers)
		cont += 1
	linea.close()

	return list_usuarios



"""def predict(test_img):
	#hace una copia de la imagen original para no modificarla
	#img = test_img.copy()
	#se detecta la cara
	face, rect = detect_face(test_img)

	#se predice el sujeto que aparece en la imagen
	label = face_recognizer.predict(face)
	#get name of respective label returned by face recognizer
	#Obtiene el nombre de la etiqueta devuelto por el metodo anterior
	label_text = subjects[label]
	
	#se dibuja el rectangulo
	draw_rectangle(img, rect)
	#draw name of predicted person
	#se escribe el nombre de la persona detectada
	draw_text(img, label_text, rect[0], rect[1]-5)
	
	#Se devuelve la imagen
	return img

def load_trainners():
	list_trainners = os.listdir(file_trainner)
	numero_arch = len(list_trainners)
	return numero_arch
"""



def __init__():

	face_cascade = cv2.CascadeClassifier('haarcascades/face.xml')
	camera = cv2.VideoCapture(0)
	identificador = cv2.face.LBPHFaceRecognizer_create()

	identificador.read('dataSet/usrs/trainners/trainData.yml')

	array_usuarios = load_all_users()

	alguien = Usuario(None, None, None)

	print('Presiona "s" para cerrar la ventana')
	while True:

		_, img = camera.read()
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		faces = face_cascade.detectMultiScale(gray, 1.2, 5)

		for (x, y, w, h) in faces:
			cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
			id_user, conf = identificador.predict(gray[y:y+h, x:x+w])
			
			for usuario in array_usuarios:
				if str(id_user) in usuario.id:
					cv2.putText(img, "Soy: " + str(usuario.nombre), (x, h+y), font, 1, (200, 255, 255))


			"""if alguien.id == None:
				for search_user in array_usuarios:
					if str(id_user) in search_user.id:
						alguien = search_user
			elif str(alguien.id) not in str(id_user):
				for search_user in array_usuarios:
					if str(id_user) in str(search_user.id):
						alguien = search_user
			else:
				cv2.putText(img, "Soy: " + str(alguien.nombre), (x, h+y), font, 1, (200, 255, 255))
			"""

		cv2.imshow('Cara', img)
		if (cv2.waitKey(1) == ord("s")):
			break

		#(> <)

	camera.release()
	cv2.destroyAllWindows()

