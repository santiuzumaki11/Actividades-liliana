#Diseñar una función que calcule X´n para X, variable real y n variable entera.

def potencia(x, n):
    resultado = x ** n
    return resultado

# Ejemplo de uso
x = 2.5  # Variable real
n = 3    # Variable entera

resultado = potencia(x, n)
print(f"{x} elevado a la potencia {n} es igual a {resultado}")
