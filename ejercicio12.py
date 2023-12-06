#.Escribir una función que permita deducir si una fecha leída del teclado es
#válida
def fecha_valida(dia, mes, anio):
    # Verificar el año
    if anio <= 0:
        return False

    # Verificar si el mes (del 1 al 12)
    if mes < 1 or mes > 12:
        return False

    # Lista de días por mes 
    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Verificar el dia que se encuentre dentro del rango mensual
    if dia < 1 or dia > dias_por_mes[mes - 1]:
        return False

    # Verificar febrero en un año bisiesto (febrero tiene 29 días)
    if mes == 2 and anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
        if dia > 29:
            return False

    return True

# Leer la fecha desde el teclado
dia = int(input("Día: "))
mes = int(input("Mes: "))
anio = int(input("Año: "))

if fecha_valida(dia, mes, anio):
    print("La fecha es válida.")
else:
    print("La fecha no es válida.")
