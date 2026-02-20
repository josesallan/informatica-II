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
# Solicitamos por pantalla las propiedades del primer vector
tipo = input("Tipo de vector(p, v, a): ")
x = float(input("Coordenada x: "))
y = float(input("Coordeanda y: "))

# Construimos un primer objeto de la clase Vector
miVector1 = Vector(tipo, x, y)

# Solicitamos por pantalla las propiedades del segundo vector
tipo = input("Tipo de vector(p, v, a): ")
x = float(input("Coordenada x: "))
y = float(input("Coordeanda y: "))

# Construimos un segundo objeto de la clase Vector
miVector2 = Vector(tipo, x, y)

# Calculamos las dos componentes del vector suma
x_suma = miVector1.x + miVector2.x
y_suma = miVector1.y + miVector2.y

# Creamos el vector suma
miVector3 = Vector('a', x_suma, y_suma)

# Mostramos las propiedades y el módulo del vector suma
miVector3.propiedades()
print(f'Módulo del vector suma: {miVector3.modulo():.2f} unidades2')
