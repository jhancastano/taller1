#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
#

import time
import zmq
import hashlib
import os


size_parts = 1024*1024

def npartes(nombreArchivo):
    size = os.stat(nombreArchivo).st_size
    partes = size/size_parts
    return partes


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

def descargar(nombreArchivo):
    print('descargando')
    file = open(nombreArchivo,'r+b')
    NParte = int(npartes(nombreArchivo))
    print(NParte)
    for x in range(0,NParte+1):
        part = file.read(size_parts)
        socket.send_multipart([b'descargando',nombreArchivo,part,str(NParte).encode(),str(x).encode(),b'descargando'])
        opcion, message, part, NPar, NSend, estado = socket.recv_multipart()
        if(estado == b'descargado'):
            socket.send_multipart([b'descargado',nombreArchivo,b'0',b'0',b'0',b'complete'])
            break
    socket.send_multipart([b'descargado',nombreArchivo,b'0',b'0',b'0',b'complete'])
    file.close()
    
    
def upload(nombreArchivo,part,NPart,NSend,estado):
    
    copia = open(nombreArchivo,'w+b')
    while (int(NPart.decode()) >= int(NSend.decode())):
        copia.write(part)
        socket.send_multipart([b'upload',nombreArchivo,part,NPart,NSend,b'upload'])
        opcion, message, part, NPart, NSend, estado = socket.recv_multipart()
        if (estado==b'complete'):
            break
    pass
    socket.send_multipart([b'upload',nombreArchivo,part,NPart,NSend,b'complete'])
    copia.close()

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    opcion, message, part, NPart, NSend, estado = socket.recv_multipart()
    print("go server" )

    if (opcion==b'descarga'):
        descargar(message)
    if (opcion==b'upload'):
        upload(message,part,NPart,NSend,estado)


    
    



