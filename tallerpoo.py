#Santiago Andres Gonzalez Londoño
#Ficha: 2697890
class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def obtener_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}")



class Automovil(Vehiculo):
    def __init__(self, marca, modelo, año, numero_puertas):
        super().__init__(marca, modelo, año)
        self.numero_puertas = numero_puertas

    def obtener_info(self):
        super().obtener_info()
        print(f"Número de puertas: {self.numero_puertas}")



class Camioneta(Vehiculo):
    def __init__(self, marca, modelo, año, capacidad_carga):
        super().__init__(marca, modelo, año)
        self.capacidad_carga = capacidad_carga

    def obtener_info(self):
        super().obtener_info()
        print(f"Capacidad de carga: {self.capacidad_carga} kg")


class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hacer_ruido(self):
        print("Ruido genérico")


class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza

    def hacer_ruido(self):
        print("¡Guau! (ladrido)")


class Gato(Animal):
    def __init__(self, nombre, edad, pelaje):
        super().__init__(nombre, edad)
        self.pelaje = pelaje

    def hacer_ruido(self):
        print("¡Miau! (maullido)")


class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def obtener_nombre_completo(self):
        return f"{self.nombre} {self.apellido}"


class Estudiante(Persona):
    def __init__(self, nombre, apellido, edad, carrera):
        super().__init__(nombre, apellido, edad)
        self.carrera = carrera

    def obtener_nombre_completo(self):
        return f"{super().obtener_nombre_completo()}, Carrera: {self.carrera}"


class Profesor(Persona):
    def __init__(self, nombre, apellido, edad, materia):
        super().__init__(nombre, apellido, edad)
        self.materia = materia

    def obtener_nombre_completo(self):
        return f"{super().obtener_nombre_completo()}, Materia: {self.materia}"


class Forma:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def calcular_area(self):
        return self.ancho * self.alto


class Rectangulo(Forma):
    def calcular_perimetro(self):
        return 2 * (self.ancho + self.alto)


import math

class Circulo(Forma):
    def calcular_circunferencia(self):
        return 2 * math.pi * (self.ancho / 2)


class Empleado:
    def __init__(self, nombre, apellido, sueldo):
        self.nombre = nombre
        self.apellido = apellido
        self.sueldo = sueldo

    def calcular_salario_neto(self):
        # Lógica genérica para calcular el salario neto
        return self.sueldo - 0.1 * self.sueldo  # Por ejemplo, restamos el 10% por impuestos y otros descuentos
    
class Gerente(Empleado):
    def __init__(self, nombre, apellido, sueldo, departamento):
        super().__init__(nombre, apellido, sueldo)
        self.departamento = departamento

    def calcular_salario_neto(self):
        # Lógica específica para calcular el salario neto de un gerente
        salario_neto_base = super().calcular_salario_neto()
        return salario_neto_base + 0.05 * salario_neto_base  # Por ejemplo, agregamos un bono del 5% por ser gerente



class Programador(Empleado):
    def __init__(self, nombre, apellido, sueldo, lenguaje):
        super().__init__(nombre, apellido, sueldo)
        self.lenguaje = lenguaje

    def calcular_salario_neto(self):
        # Lógica específica para calcular el salario neto de un programador
        salario_neto_base = super().calcular_salario_neto()
        return salario_neto_base + 0.03 * salario_neto_base  # Por ejemplo, agregamos un bono del 3% por ser experto en un lenguaje
