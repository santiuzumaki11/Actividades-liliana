#Diseñar el algoritmo para calcular el máximo común divisor de cuatro números
#basado en una su algoritmo función mcd(el máximo común divisor de dos
#números).


# Definir una función para calcular el MCD de dos números
def mcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Definir una función para calcular el MCD de cuatro números
def mcd_cuatro_numeros(a, b, c, d):
    # Calcula el MCD de los dos primeros números
    mcd_ab = mcd(a, b)
    
    # Calcula el MCD de los dos últimos números
    mcd_cd = mcd(c, d)
    
    # Calcula el MCD de los dos resultados anteriores
    mcd_final = mcd(mcd_ab, mcd_cd)
    
    return mcd_final

# Ejemplo de uso
num1 = 24
num2 = 36
num3 = 48
num4 = 60

resultado = mcd_cuatro_numeros(num1, num2, num3, num4)
print(f"El MCD de {num1}, {num2}, {num3} y {num4} es {resultado}")
