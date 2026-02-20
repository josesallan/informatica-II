# Definimos la clase Rectangulo y sus características
class Rectangulo():
    # El constructor recibe como parámetro el valor de la longituda de la base y la altura
    def __init__(self, pbase, paltura):
        self.lados = 4
        self.base = pbase
        self.altura = paltura

    # Este método muestra las propiedades de los objetos de la clase
    def propiedades(self):
        print("Número de lados:", self.lados)
        print("Longitud de la base:", self.base)
        print("Longitud de la altura:", self.altura)

    # Método que devuelve el valor de área del objeto de la clase Rectangulo
    def area(self):
        valor = self.base * self.altura
        return valor

    # Método que devuelve el valor del perímetro del objeto de la clawse Rectangulo
    def perimetro(self):
        valor = (self. base + self.altura) * 2
        return valor


# ------------------ Programa principal --------------------#
# Solicitamos por pantalla las longitudes de la base  y la altura del objeto a crear
base = float(input("Introduce el valor de la longitud de la base: "))
altura = float(input("Introduce el valor de longitud de la altura: "))

# Creamos el objeto, enviando como parámetros sus medidas
miRectangulo1 = Rectangulo(base, altura)

miRectangulo1.propiedades()
print(f'El rectángulo tiene una superficie de: {miRectangulo1.area():.2f}')
print(f'El rectángulo tiene un perímetro de: {miRectangulo1.perimetro():.2f}')

