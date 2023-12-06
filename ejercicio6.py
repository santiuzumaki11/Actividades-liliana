#Diseñar un procedimiento que acepte un numero de mes, un numero de día y
#un numero de año y los visualice en el formato dd/mm/aa Por ejemplo, los
#valores 19,09,1987 se visualizarían así: 19/9/87 y para los valores 3,9, y 1905
#así: 3/9/05.

print ("Realizaremos un formato fecha")

def fecha(): #No hay parametros porque los numeros se ingresan desde teclado
    dia = int(input("Ingresa el dia! "))
    mes = int(input("Ingresa el mes! "))
    year = int(input("Ingresa el año! "))

    formatofecha = (f"{dia}/{mes}/{year}")
    print(f"tu fecha es: {formatofecha}")
fecha() #Se cierra la funcion sin parametros para recibir