"""Este script se encarga de crear la conexion con la base de datos online para conectar la raspberry con la app android"""
#import _mysql as mydb
import time
import MySQLdb as mydb


#sql11.freemysqlhosting.net
#sql11205354
#QdSPxkUF24


cnx = None
cursor = None

class Dato():

	def __init__(self, id, nombre, apellidos, hora):
		self.id = id
		self.nombre = nombre
		self.apellidos = apellidos
		self.hora = hora

def crear_conex(dato):
	
	try:

		cnx = mydb.connect(host="sql11.freemysqlhosting.net",user="sql11205354",passwd="QdSPxkUF24",db="sql11205354")
		insert_data(cnx, dato)
		print("***Conectado correctamente!")

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

def insert_data(cnx, dato):
	cursor = cnx.cursor()
	 
	sql = "insert into prueba VALUES("+dato.id+", '"+dato.nombre+"', '"+dato.apellidos+"', '"+dato.hora+"')"
	try: 
		cursor.execute(sql)
		cnx.commit()
	except mydb.Error as err:
		print("Error al realizar el insert")
		print(err)

	print("Cerrando conexion")
	cnx.close()


print("\Conectando con la base de datos...")

id = raw_input('\nIntroduce una ID: ')
nombre = raw_input('Introduce solo el nombre: ')
apellidos = raw_input('Ahora los apellidos: ')
hora = time.strftime("%H:%M:%S")

dato = Dato(id, nombre, apellidos, hora)

print("\nInsertando datos...")
cnx = crear_conex(dato)
