#.dado el nombre de una serie de estudiantes y las calificaciones obtenidas en
#un examen, calcular e imprimir la calificación media así como cada calificación
#y la diferencia con la media.

opcion = 1
while opcion ==1:
    nombre = input("Ingrese el nombre del estudiante")
    calificaciones = int(input("Ingrese el numero de calificaciones"))
    lista = []
    for i in range(calificaciones):
        c = float(input("Ingrese calificacion"))
        lista.append(c)

    suma = sum(lista)/calificaciones
    print(nombre)
    print("Calificaiones: ", lista)
    print("Media: ", suma)
    opcion = int(input("Ingese 1 para agregar estudiante o 2 para salir"))

#ejercicio elaborado con ayuda
