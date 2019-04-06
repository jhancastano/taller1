#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
#

import time
import zmq
import hashlib
import os




objetohash = hashlib.sha1(b'hola mundo')
cadena = objetohash.hexdigest()
print(cadena)


def copiarArchivo(nombreArchivo):
    import os
    size = os.stat(nombreArchivo).st_size
    
    f = open(nombreArchivo,'r+b')
    copia = open('copia.zip','w+b')
    for x in range(1,20):
        part = f.read(int(1024*1024*1024))
        copia.write(part)
        
    f.close()
    copia.close()
    sizecopia = os.stat(nombreArchivo).st_size
    

    print(size)
    print('copia')
    print(sizecopia)


def descargar(nombreArchivo):
	pass


def subida():
	pass

copiarArchivo('prueba.zip')

# context = zmq.Context()
# socket = context.socket(zmq.REP)
# socket.bind("tcp://*:5555")

# while True:
#     copiarArchivo('prueba.gif')
#     #  Wait for next request from client
#     message = socket.recv()
#     print("Received request: %s" )

#     #  Do some 'work'
#     time.sleep(1)

#     #  Send reply back to client
#     socket.send(cadena.encode('utf8'))



