import os
nombre = input("Ingrese el nombre del archivo con extension txt")
with open(nombre, 'w') as archivo:
    while True:
        texto = input("digite lo que desea en este archivo(o escriba 'salir' para finalizar)")
        if texto.lower() == 'salir':
            break
        archivo.write(texto+ "\n")
        print(f"*_{nombre}")