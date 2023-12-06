#calcular la suma de los elementos de la diagonal principal de una matriz de 4x4
def sumadiagonal(matriz): # se crea la funcion

    if len(matriz) != 4 or len(matriz[0]) != 4: #se hace el condicional
        raise ValueError("La matriz debe ser de tamaño 4x4.")
    
    suma = 0 #se genera el contador
    for i in range(4): #se crea el ciclo
        suma += matriz[i][i]
    
    return suma

# ejm de uso
mi_matriz = [ #se crea la matriz 
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

resultado = sumadiagonal(mi_matriz)
print(f"La suma de la diagonal principal es: {resultado}")
