
import sys
import os
import time
import trainner as tr
import detector as dt
import createData as cd
import create_user as cu


#En primer lugar creamos los metodos que importaran los archivos con los scripts listos para ejecutarse
def create_acount():

	complete, dato = cu.create_user()
	
	if complete == True:
		cd.init_user(dato)
	else:
		print("No se ha podido guardar los datos")

def add_person():
	dato = None
	cd.init_user(dato)

def train():
	print("\Entrenamiento")
	tr.__init__()

def detect():
	dt.__init__()

def consult_user():
	user = raw_input("Email a buscar: ")
	cu.consult_user(user)

def salir():
	sys.exit()

def show_menu():	
	#Creamos el menu
	print("Que desea hacer?")
	print("1 - Crear una cuenta de usuario")
	print("2 - Anadir un usuario")
	print("3 - Realizar entrenamiento")
	print("4 - Detectar")
	print("5 - Consulta usuario")
	print("0 - Salir")
 

print("\nBienvenido")
opc = None

#Guardamos los metodos en una lista para su ejecucion
opciones = {'1':create_acount, '2':add_person, '3':train, '4':detect, '5':consult_user}
primera = True
while opc != "0":
	
	show_menu()
	print("\n****************************************************")

	opc = raw_input('Introduce una opcion: ')

	try:
		#Se ejecuta la opcion seleccionada por el usuario
		opciones[opc]()
		
	except:

		if opc != "0":
			#os.system('cls')
			print("\nOpcion seleccionada no valida")

			


