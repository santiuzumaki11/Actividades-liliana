#Escribir una función booleana Digito que determine si un carácter es uno de los
#dígitos 0 al 9.

def es_digito(caracter):
    # Comprueba si el carácter es un dígito utilizando el método isdigit()
    if caracter.isdigit(): #palabra reservada
        return True
    else:
        return False

#Ejm de su uso:
caracter = '5'
if es_digito(caracter):
    print(f"{caracter} es un dígito.")
else:
    print(f"{caracter} no es un dígito.")

caracter = 'A'
if es_digito(caracter):
    print(f"{caracter} es un dígito.")
else:
    print(f"{caracter} no es un dígito.")
