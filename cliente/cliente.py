#
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Hello" to server, expects "World" back
#

import zmq
import hashlib
import os

size_parts = 20*1024*1024
SERVER_TCP = "tcp://localhost:5555"


def npartes(nombreArchivo):
    size = os.stat(nombreArchivo).st_size
    partes = size/size_parts
    return partes


def nombrehash(FILE):
	extension = os.path.splitext(FILE)[1]
	with open(FILE, 'rb') as f:
		data = f.read()
		objetohash = hashlib.sha1(data)
		cadena = objetohash.hexdigest()
		f.close()	
	return (cadena + extension)


def descargar(nombreArchivo):
	context = zmq.Context()
#  Socket to talk to server
	print("Connecting to hello world server...")
	socket = context.socket(zmq.REQ)
	socket.connect(SERVER_TCP)

	socket.send_multipart([b'descarga',nombreArchivo.encode('utf8'),b'0',b'0',b'0',b'descargando'])
	
	opcion, message, part, NPart, NSend, estado = socket.recv_multipart()
	copia = open(message,'w+b')
	while (int(NPart.decode()) >= int(NSend.decode())):
		copia.write(part)
		socket.send_multipart([opcion,message,part,NPart,NSend,b'descargando'])
		opcion, message, part, NPart, NSend, estado = socket.recv_multipart()
		if(estado==b'complete'):
			break
	copia.close()	
    		
    				
def upload(nombreArchivo):
	context = zmq.Context()
	print("Connecting to hello world server...")
	socket = context.socket(zmq.REQ)
	socket.connect(SERVER_TCP)

	file = open(nombreArchivo,'r+b')
	nombreCompleto = nombrehash(nombreArchivo)
	NParte = int(npartes(nombreArchivo))
	print(NParte)
	for x in range(0,NParte+1):
		part = file.read(size_parts)
		socket.send_multipart([b'upload',nombreCompleto.encode(),part,str(NParte).encode(),str(x).encode(),b'upload'])
		opcion, message, part, NPar, NSend, estado = socket.recv_multipart()
	socket.send_multipart([b'upload',nombreCompleto.encode(),b'0',b'0',b'0',b'complete'])
	file.close()

def compartir(nombreArchivo):
	context = zmq.Context()
	print("Connecting to hello world server...")
	socket = context.socket(zmq.REQ)
	socket.connect(SERVER_TCP)
	socket.send_multipart([b'compartir',nombreArchivo.encode(),b'0',b'0',b'0',b'compartir'])
	opcion, message, part, NPart, NSend, estado = socket.recv_multipart()
    

def compartidos():
	context = zmq.Context()
	print("Connecting to hello world server...")
	socket = context.socket(zmq.REQ)
	socket.connect(SERVER_TCP)
	socket.send_multipart([b'compartidos',b'0',b'0',b'0',b'0',b'compartidos'])
	opcion, message, part, NPart, NSend, estado = socket.recv_multipart()
	print(part)
	print('holaprueba')


#compartir('holamundo.com')
#compartir('prueba.txt')
#compartidos()

#descargar('prueba.png')
#upload('pruebaupload.png')



