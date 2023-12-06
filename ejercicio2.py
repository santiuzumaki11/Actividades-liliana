#Diseñar la función FACTORIAL que calcule la factorial de un número 
#entero entre el rango 100 a 1.000.000.

import math #importamos math para acceder a la funcion factorial

def calcular_factorial():
    try: #el try se usa por la posibilidad de errores en la ejecucion
        num = int(input("Ingresa un número entre 100 y 1,000,000: "))
        if 100 <= num <= 1000000:
            resultado = math.factorial(num)
            print(f"El factorial de {num} es: {resultado}")
        else:
            print("El número debe estar en el rango de 100 a 1,000,000.")
    except ValueError: #el except se combina con el try
        print("Debes ingresar un número válido.")
    except OverflowError:
        print("El cálculo del factorial ha excedido los límites de la memoria.")

calcular_factorial()
