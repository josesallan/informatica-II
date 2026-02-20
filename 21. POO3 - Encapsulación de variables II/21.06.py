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


# ------------------ Programa principal --------------------#

# Solicitamos por pantalla las propiedades del vector
tipo = input("Tipo de vector(p, v, a): ")
x = float(input("Coordenada x: "))
y = float(input("Coordeanda y: "))

# Construimos un objeto de la clase Vector
miVector1 = Vector(tipo, x, y)

# Mostramos sus propiedades por pantalla
miVector1.propiedades()
