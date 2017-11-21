import cv2
import os
import sys
import os.path

directorio = 'dataSet/images/todo'
users_archivo = "dataSet/usrs/usuarios.dat"
face_cascade_default = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
face_cascade_alt = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_alt.xml')

#Iniciamos la camara
offset=50

class Person():
	"""Esta clase recibe un id y un nombre como parametros para poder centrar la informacion de los usuarios en un solo objeto"""
	def __init__(self, id, nombre, apellidos, edad, email, photos):
		self.id = id
		self.nombre = nombre
		self.apellidos = apellidos
		self.edad = edad
		self.email = email
		self.photos = photos


def exist_dir(directorio, tipo):
	"""Rrecibe la ruta de un directorio y lo crea en caso de no existir"""

	if not os.path.exists(directorio) and tipo == 'a':
		arch = open(directorio, 'a')
		arch.write('0=test=test=0=test=0\n')
		arch.close()
	elif not os.path.exists(directorio) and tipo == 'c':
		os.mkdir(directorio)
	else:
		pass


def load_id_users(nuevo_user):

	list_usuarios = []

	archivo = "dataSet/usrs/usuarios.dat"

	exist_dir(archivo, 'a')

	yo = None
	encontrado = False

	linea = open(users_archivo, "r")
	for line in linea:
		
		num_id, nom, apellidos, edad, email, photos = line.split('=')

		#Si el nombre nuevo       NO esta en   nombre archivo  y apellidos nuevo        NO esta en apellidos archivo
		if str(nuevo_user.nombre) not in str(nom).lower() and str(nuevo_user.apellidos) not in str(apellidos).lower():
			#pers = Person(num_id, nom, apellidos, edad, email, photos)
			#list_usuarios.append(pers)
			yo = nuevo_user
			encontrado = False

		else:
			yo = Person(num_id, nom, apellidos, edad, email, photos)
			print("Persona encontrada: \nId - " + yo.id + ", Nombre - " + yo.nombre + ", Fotos - " + yo.photos)
			encontrado = True
			break

	linea.close()

	return yo, encontrado

def new_user(yo):
	try:

		f = open(users_archivo, "a")
		print("Abierto")
		f.write(str(yo.id) + "=" + str(yo.nombre) + "=" + str(yo.apellidos) + "=" + str(yo.edad) + "=" + str(yo.email) + "=" + str(yo.photos) + "\n")
		print("Escrito")
		f.close()
		print("Archivo actualizado")

	except OSError as err:
	    print("OS error: " + err)
	except:
	    print("Unexpected error:", sys.exc_info()[0])
	    raise

def update_data(yo):

	#Cargamos todo el texto para trabajar con el
	f = open(users_archivo, "r")
	lineas = f.readlines()
	f.close()


	f = open(users_archivo, "w")
	#Recorremos las lineas hasta encontrar el usuario a actualizar
	for usuario in lineas:
		#Si encuentra la linea con el usuario lo sobreescribe
		if str(yo.id) in usuario:
			f.write(usuario.replace(str(usuario), str(yo.id) + "=" + str(yo.nombre) + "=" + str(yo.apellidos) + "=" + str(yo.edad) + "=" + str(yo.email) + "=" + str(yo.photos) + "\n"))
		#Si es otro usuario lo mantiene
		else:
			f.write(usuario)
	#Cerramos
	f.close()
	print("\nRegistro actualizado")

def last_id():
	"""Devuelve cual ha sido el ultimo id creado en el archivo"""
	f = open(users_archivo, "r")
	texto = f.readlines()
	
	if not texto:
		num = 0
	else:
		last = texto[len(texto)-1]
		num, _, _, _, _, _ = last.split("=")
	
	f.close()
	return num


def last_photo(id):
	"""Recibe el Id del usuario y devuelve el numero de archivos en el directorio"""
	
	directorio = 'dataSet/images/p' + str(id)
	lista = os.listdir(directorio)
	numero_arch = len(lista)
	return numero_arch


def train_more_photos(yo, registro):
	"""Pregunta al usuario si desea anadir mas imagenes a su coleccion"""
	resp = raw_input("Deseas guardar mas fotos? [s/n]: ")

	#while resp is not "s" and resp is not "n":
	if resp == "s" or resp == "si" or resp == "yes" or resp == "y":
		take_photos_id(yo, registro)
		#break
	elif resp == "n":
		print("Saliendo...")
		#break
	else:
		print("Respuesta incorrecta")



#Abrimos el archivo donde se almacenan los usuarios registrados
# usuario_alejandro.1, usuario_alejandro.2, usuario_alejandro.3, usuario_alejandro.4 ...


#######################################################################

#Esta funcion recibe el numero id del ultimo usuario y le suma 1 y el nombre del nuevo usuario	
def take_photos_id(yo, registro):
	"""Recibe un id y un nombre para tomar fotografias y guardarlas en un directorio personalizado"""
	camera = cv2.VideoCapture(0)

	#directorio = 'dataSet/images/p' + str(numero_id)
	exist_dir(directorio, 'c')
	cont = 0
	
	if registro == "e":
		cont = int(yo.photos) + 1
		inicio = int(yo.photos)
	else:
		cont = 1


	while True:

		try:
			_, img = camera.read()
			cv2.imshow('Cuando estes listo pulsa "s"', img)
		
			if (cv2.waitKey(1) == ord("s")):
				camera.release()
				cv2.destroyAllWindows()
				safe_photos(yo, cont, registro)
				break
		except:
			print("Unexpected error: ", sys.exc_info()[0])
	    


def safe_photos(yo, cont, registro):

	camera = cv2.VideoCapture(0)

	while True:

		if (cv2.waitKey(1) == ord("s")):
			break

		_, img = camera.read()
		
		if camera.isOpened():
			gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
			faces_filter_1 = face_cascade_default.detectMultiScale(gray, 1.3, 5)
			
			for (x, y, w, h) in faces_filter_1:
					#(x, y, w, h) Creamos una nueva carpeta para el nuevo usuario con su id (u1, u2, u3)
					#Dentro se encuentran las fotos con el formato user_nombre_numfoto.jpg (user_alejandro_1)
					cv2.imwrite(str(directorio) + '/user_' + str(yo.id) + '_' + str(cont) + '.jpg', gray[y-offset:y+h+offset,x-offset:x+w+offset])
					print("\tFOTO: " + str(cont))
					cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
					cv2.waitKey(10)
					cont += 1

					cv2.imshow('Cara', img)
					cv2.waitKey(15)
			

			"""for filter_test in faces_filter_1:

				faces_filter_2 = face_cascade_default.detectMultiScale(filter_test)

				for (x, y, w, h) in faces_filter_2:
					#(x, y, w, h) Creamos una nueva carpeta para el nuevo usuario con su id (u1, u2, u3)
					#Dentro se encuentran las fotos con el formato user_nombre_numfoto.jpg (user_alejandro_1)
					cv2.imwrite(str(directorio) + '/user_' + str(yo.id) + '_' + str(cont) + '.jpg', gray[y-offset:y+h+offset,x-offset:x+w+offset])
					print("FOTO: " + str(cont))
					cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
					cv2.waitKey(100)
					cont += 1

					cv2.imshow('Cara', img)
					cv2.waitKey(1)
					"""


			#Actualizamos el numero de fotos del usuario
			#yo.photos = cont

			print("1 - Contador: " + str(cont))
			print("1 - Photos: " + str(yo.photos))
			yo.photos = int(cont)-1
			print("2 - Contador: " + str(cont))
			print("2 - Photos: " + str(yo.photos))

			#(> <)
			if registro == "e":
				if cont > int(yo.photos) + 10:
					yo.photos = int(cont)
					update_data(yo)
					print("Datos actualizados, cerrando")
					break
			else:
				if cont > 10:
					yo.photos = int(cont)-1
					print("Escribiendo nuevo usuario: \n \t - " + str(yo.id) + "=" + str(yo.nombre) + "=" + str(yo.apellidos) + "=" + str(yo.edad) + "=" + str(yo.email) + "=" + str(yo.photos) + "\n")
					new_user(yo)
					break

		else:
			print("\t - Error al abrir la camara.")

	print("\tImagenes guardadas")
	camera.release()
	cv2.destroyAllWindows()

######################################################################


def init_user(yo):
	#Pedimos al usuario el nombre para realizar la comprobacion
	
	if yo == None:
		print("Creacion de usuario")
		yo = user_data()

	#Leemos todos los usuarios linea por linea
	search_user, guardado = load_id_users(yo)

	if guardado == True:
		registro = "e"
		train_more_photos(search_user, registro)

	else:
		print("\n - Nuevo usuario:")
		var = last_id()
		registro = "n"
		yo.id = int(var)+1
		yo.photos = 0
		print("Sacando fotos")
		take_photos_id(yo, registro)

	print("Cerrando registro")


def user_data():

	yo = None

	print("\nIntroduce tus datos personales: ")
	print("*Nombre y Apellidos obligatorios*")
	nombre = raw_input("Nombre: ")
	apellidos = raw_input("Apellidos: ")
	edad = raw_input("Edad: ")
	email = raw_input("Email: ")

	if nombre == "" or apellidos == "":
		print("Por favor rellene los datos.")
		user_data()

	else:
		
		if edad == "":
			edad = "Null"
		if email == "":
			email = "Null"

		yo = Person(None, nombre, apellidos, edad, email, None)
	
	print("Retorno")
	return yo

