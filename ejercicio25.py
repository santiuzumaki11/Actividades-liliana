 import os
archivo = open("mi_archivo.txt", 'w')
while True:
    texto = input("digite lo que desea en este archivo(o escriba 'salir' para finalizar)")
    if texto.lower() == 'salir':
        break
    archivo.write(texto+ "\n")

archivo.close
archivo = open("mi_archivo.txt", 'r')
print(archivo.read())
archivo.close()