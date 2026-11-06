class Persona():
    def __init__(self, nombre, edad, lugar_residencia):
        self.nombre = nombre
        self.edad = edad
        self.lugar_residencia = lugar_residencia

    def descripcion(self):
        print("Nombre:", self.nombre, "Edad:", self.edad, "Resiencia:", self.lugar_residencia)


class Empleado(Persona):
    def __init__(self, nombre, edad, lugar_residencia, salario, antiguedad):
        Persona.__init__(self,nombre, edad, lugar_residencia)
        self.salario = salario
        self.antiguedad = antiguedad


manolo = Empleado("Manolo", 19, "Zaragoza", 1000, 3)
manolo.descripcion()