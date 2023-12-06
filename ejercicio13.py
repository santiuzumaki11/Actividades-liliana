#escribir el algoritmo que permita obtener el número de elementos positivos de
#una tabla

def contar_elementos_positivos(tabla): #se crea la funcion

    #ciclo para recorrer la lista
    contador = 0
    for elemento in tabla:
        if elemento > 0:
            contador += 1
    return contador

# ejm de uso
mi_tabla = [1, -2, 3, -4, 5, 0, 6]
elementos_positivos = contar_elementos_positivos(mi_tabla)
print(f"El número de elementos positivos en la tabla es: {elementos_positivos}")
