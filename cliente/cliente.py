#
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Hello" to server, expects "World" back
#

import zmq
import hashlib
import os

objetohash = hashlib.sha1(b'hola mundo')
cadena = objetohash.hexdigest()
print(cadena)
size_parts = 1024*1024*20


def descargar(nombreArchivo):
	context = zmq.Context()
#  Socket to talk to server
	print("Connecting to hello world server...")
	socket = context.socket(zmq.REQ)
	socket.connect("tcp://localhost:5555")
	socket.send_multipart([b'descarga',nombreArchivo.encode('utf8'),b'false'])
	nombre, message, x = socket.recv_multipart()
	copia = open(nombre,'w+b')
	copia.write(message)
	copia.close()	
    		
    				
def upload(nombreArchivo):
	context = zmq.Context()
#  Socket to talk to server
	print("Connecting to hello world server...")
	socket = context.socket(zmq.REQ)
	socket.connect("tcp://localhost:5555")

	extension = os.path.splitext(nombreArchivo)[1]
	file = open(nombreArchivo,'r+b')
	part = file.read(size_parts)
	nombre = hashlib.sha1(part)
	nombreCompleto = nombre.hexdigest()+ extension
	socket.send_multipart([b'upload',nombreCompleto.encode('utf8'),part])


descargar('prueba.png')
upload('pruebaupload.png')



