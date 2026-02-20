# Definimos la clase Vector y sus características
class Vector():
    def __init__(self, ptipo, px, py):
        self.__tipo = ptipo
        self.x = px
        self.y = py

    def propiedades(self):
        print("Tipo de vector:", self.__tipo)
        print("Coordenada x:", self.x)
        print("Coordenada y:", self.y)

    def nuevo_tipo(self, ptipo):
        self.__tipo = ptipo

    # Método que calcula el módulo del vector y lo devuelve al código principal
    def modulo(self):
        longitud = (self.x ** 2 + self.y ** 2) ** (1 / 2)
        return longitud



# ------------------ Programa principal --------------------#
# Solicitamos por pantalla las propiedades del vector
tipo = input("Tipo de vector(p, v, a): ")
x = float(input("Coordenada x: "))
y = float(input("Coordeanda y: "))

# Construimos un objeto de la clase Vector
miVector1 = Vector(tipo, x, y)

# Mostramos el módulo del vector
print(f'Módulo del vector: {miVector1.modulo():.2f} unidades2')
