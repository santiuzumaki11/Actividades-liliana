#Escribir una función Salario que calcula los salarios de un trabajados para un
#numero dado de horas trabajadas y un salario hora. Las horas que superan las
#40 horas semanales se pagaran como extras con un salario hora 1,5 veces el
#salario ordinario.

def Salario():
    HoraExtra = float(input("Ingresa el numero de horas extra trabajadas ")) #Se pide las horas extra
    HoraSemanal = 40 #Horas de trabajo comun
    SalarioHora = 5 #Salario normal
    salarioComun = HoraSemanal * SalarioHora #se hace el calculo
    SalarioExtra = HoraExtra + (SalarioHora * 1.5) 

    SalarioTotal = SalarioExtra + salarioComun #se suman las horas extra a las horas trabajadas
    print(f"Su salario total es de: {SalarioTotal}")  #se imprime el resultado
Salario()