#Diseñar una función que encuentro el mayor de dos números enteros

def encontrar_mayor(n1, n2): #Recibimos los parametros
    
    if n1 > n2: #hacemos la condicional
        return n1
    else:
        return n2

#variables con un numero preestablecido
n1 = 10
n2 = 15

mayor = encontrar_mayor(n1, n2) #variable que trae la funcion
print(f"El número mayor entre {n1} y {n2} es {mayor}")
