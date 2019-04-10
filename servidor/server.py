#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
#

import time
import zmq
import hashlib
import os


size_parts = 1024*1024*20

objetohash = hashlib.sha1(b'hola mundo')
cadena = objetohash.hexdigest()
extension = os.path.splitext('fuente.textClipping')[1]
print(cadena + extension)

a, b, c = ['1','2','3']
print(b)
def copiarArchivo(nombreArchivo):
    size = os.stat(nombreArchivo).st_size
    exten = os.path.splitext(nombreArchivo)[1]


    file = open(nombreArchivo,'r+b')
    hashname = hashlib.sha1(b'hola mundo')
    nombre = hashname.hexdigest()



    copia = open(nombre + exten,'w+b')
    for x in range(1,20):
        part = file.read(size_parts)
        copia.write(part)
        
    file.close()
    copia.close()
    sizecopia = os.stat(nombreArchivo).st_size
    

    print(size)
    print('copia')
    print(sizecopia)

def descargar(nombreArchivo):
    print('descargar')
    hola = message
    print(message)
    file = open(nombreArchivo,'r+b')
    part = file.read(size_parts)

    socket.send_multipart([message,part,b"hola"])
    pass
    
def upload(nombreArchivo):
    copia = open(nombreArchivo,'w+b')
    copia.write(part)
    copia.close()
    socket.send_multipart([b'0',b'0',b"0"])
    
    pass   


#copiarArchivo('prueba.png')

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
#  copiarArchivo('prueba.gif')
#     #  Wait for next request from client
    opcion, message, part = socket.recv_multipart()
    print("Received request: hola" )

    if (opcion==b'descarga'):
        descargar(message)
    if (opcion==b'upload'):
        upload(message)

#     #  Do some 'work'
#     time.sleep(1)

#     #  Send reply back to client
    
    



