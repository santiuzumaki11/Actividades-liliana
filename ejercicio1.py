#Diseñar una funcion que calcule la media de 3 numeros del teclado y poner un ejemplo de su aplicacion.


#Se crea la funcion (MediadeTres)
def MediadeTres(): #No hay parametros porque se ingresan los numeros desde teclado
    print("se calculara la media de 3 numeros, ingresa los numeros que gustes!\n")
    #se realizan los inputs respectivos 
    n1 = float(input("Ingresa el numero 1: "))
    n2 = float(input("Ingresa el numero 2: "))
    n3 = float(input("Ingresa el numero 3: "))

    "variable para calcular la media de los 3"
    media = (n1 + n2 + n3) / 3

    print("La media de los numeros ingresados es: ", media)
MediadeTres()