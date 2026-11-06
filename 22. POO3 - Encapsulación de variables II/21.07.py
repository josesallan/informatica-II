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

# Solicitamos por pantalla las nuevas propiedades del vector
tipo2 = input("Nuevo tipo para el vector(p, v, a): ")
x2 = float(input("Nuevo valor de la coordenada x: "))
y2 = float(input("Nuevo valor de la coordeanda y: "))

# Intenamos modificar las propiedades del objeto vector
miVector1.__tipo = tipo2
miVector1.x = x2
miVector1.y = y2

# Llamamos al método propiedades para mostrar dichos valores por pantalla
miVector1.propiedades()

# El valor de la propiedad tipo,  no se ha modificado en el objeto por estar encapsulada
