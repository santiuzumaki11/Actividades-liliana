import os
archivo = open(“agenda.txt”, 'r')
contenido = archivo.read()
archivo.close()
print(contenido)