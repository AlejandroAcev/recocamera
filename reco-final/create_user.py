"""Este script se encarga de crear la conexion con la base de datos online para conectar la raspberry con la app android"""
#import _mysql as mydb
import time
import MySQLdb as mydb


#sql11.freemysqlhosting.net
#sql11205354
#QdSPxkUF24


#cnx = None
#cursor = None


class Dato():

	def __init__(self, id, nombre, apellidos, email, contrasena):
		self.id = id
		self.nombre = nombre
		self.apellidos = apellidos
		self.email = email
		self.contrasena = contrasena



def crear_conex():
	
	cnx = None

	try:

		cnx = mydb.connect(host="sql11.freemysqlhosting.net",user="sql11205354",passwd="QdSPxkUF24",db="sql11205354")

	except mydb.Error as err:
		if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
			print("Something is wrong with your user name or password")
		elif err.errno == errorcode.ER_BAD_DB_ERROR:
			print("Database does not exist")
		else:
			print(err)
	

	return cnx


def cerrar_conex(cnx):
	cnx.close()


def insert_user(dato):

	cnx = crear_conex()
	cursor = cnx.cursor()

	complete = False

	 
	#sql = "insert into users VALUES('"+dato.nombre+"', '"+dato.apellidos+"', '"+dato.email+"', '"+dato.contrasena+"')"
	sql = "insert into users VALUES(NULL, '"+dato.nombre+"', '"+dato.apellidos+"', '"+dato.email+"', '"+dato.contrasena+"')"

	try: 

		print("\nIntroduciendo en la base de datos...")
		cursor.execute(sql)
		cnx.commit()
		complete = True
		print("\nDatos guardados con exito")

	except mydb.Error as err:

		print("\n - Error al realizar el insert")
		print(err)
		cnx.close()


	cnx.close()

	print(complete)
	return complete


def consult_user(email):

	personas = []

	#Abrimos la conexion con la base de datos
	cnx = crear_conex()

	cursor = cnx.cursor()

	sql = "select * from users where email='"+email+"'"

	try: 

		cursor.execute(sql)
		
		for fila in cursor:
			personas.append(fila)
			print("Encontrados: "+str(fila))

	except mydb.Error as err:

		print("Error al realizar la consulta")
		print(err)
		cnx.close()

	cnx.close()

	return personas

def set_pass():
	contrasena = raw_input('Password: ')

	if contrasena.len() < 6:
		print("La contrasena debe tener al menos 6 caracteres. Intentelo de nuevo")

	return contrasena

def create_user():

	personas = []
	data_ok = True
	complete = False
	dato = Dato(None, None, None, None, None)

	nombre = raw_input('Introduce solo el nombre: ')
	apellidos = raw_input('Ahora los apellidos: ')
	email = raw_input('Finalmente indicanos tu email: ')

	personas = consult_user(email)

	for i in personas:
		if email in i:
			print("Ya existe un usuario con el mismo correo. Por favor utilice otro.\n")
			data_ok = False
			break


	if data_ok:
		contrasena = raw_input('Password: ')

		if nombre == "" or apellidos == "" or email == "" or contrasena == "":
			print("\n - Por favor, rellene todos los campos")
			time.sleep(3)
			complete = False
		else:
			dato = Dato(None, nombre, apellidos, email, contrasena)

			complete = insert_user(dato)

	else:
		create_user()

	print("Boolean: " + str(complete) + " - Dato: " + str(dato.id) + "-" + str(dato.nombre))
	return complete, dato


