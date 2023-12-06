#escribir un algoritmo que convierta los números arábigos en números romanos
#y viceversa I=1, V=5, X=10, L=50,C=100, D=500 y M=1000.

numero = int(input("Ingrese un numero"))
numeros = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
romanos = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "I"]

resultado = ''
i = 0

while numero > 0 and numero < 3000:
    for _ in range(numero//numeros[i]):
        resultado += romanos[i]
        numero -= numeros[i]

    i += 1

print(resultado)

#ejercicio hecho con ayuda
