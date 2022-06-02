import os

# Para crear archivo y recibe como parametro el nombre del archivo
def crear_archivo(nombre, contenido):
    archivo = open(nombre, "wt")
    archivo.write(contenido) 
    archivo.close()

# Para eliminar recibe como parametro el nombre del archivo
def eliminar_archivo(nombre):
    os.remove(nombre)

# Para agregar contenido a un archivo plano, debe existir un archivo
def agregar_contenido_archivo(nombre, contenido):
    archivo = open(nombre, "at")
    archivo.write("\n" + contenido) 
    archivo.close()

# Para leer el contenido de un archivo plano, debe existir un archivo
def leer_archivo(nombre):
    archivo = open(nombre, "rt", encoding="uft8")
    contenido = archivo.read()
    return contenido
