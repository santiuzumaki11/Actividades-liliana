#rellenar una matriz identidad de 4x 4

def matriz4x4(): #se crea la funcion

    matriz = [] #se crea un array matriz
    for i in range(4): #se genera el ciclo con un rango de 4
        fila = [] #se crea un array fila
        for j in range(4): #se genera un segundo ciclo con un rango de 4
            valor = int(input(f"Ingrese el valor para la posición ({i+1}, {j+1}): "))
            fila.append(valor) #se usa la palabra reservada append para agregar a fila
        matriz.append(fila) #se usa la palabra reservada append para agregar fila a matriz
    
    return matriz

# ejm de uso
mi_matriz = matriz4x4()
for fila in mi_matriz:
    print(fila) #se imprime fila
