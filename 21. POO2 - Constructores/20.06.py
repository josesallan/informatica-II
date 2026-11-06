# Definimos la clase Triangulo
class Triangulo():
    # Utilizaremos un constructor para definir las propiedades de los objetos de la clase
    def __init__(self, side1, side2, side3):
        self.__lados = 3
        self.lado1 = side1
        self.lado2 = side2
        self.lado3 = side3

	# Este método mostará las propiedades de los objetos por pantalla
    def propiedades(self):
        # La propiedad lados va a estar encapsulada para evitar que se pueda modificar desde fuera
        # del código de la clase.
        print("Número de lados:", self.__lados)
        print("Lado 1: ", self.lado1)
        print("Lado 2: ", self.lado2)
        print("Lado 3: ", self.lado3)

    # Este método devuelve la longitud del lado más largo del objeto Triangulo
    def largo(self):
        if self.lado1 >= self.lado2:
            if self.lado1 >= self.lado3:
                largo = self.lado1
            else:
                largo = self.lado3
        else:
            if self.lado2 >= self.lado3:
                largo = self.lado2
            else:
                largo = self.lado3
        return largo

    # Método que devuelve el tipo de triángulo al que pertenece el objeto
    # comparando la longitud de los tres lados
    def tipo(self):
        if self.lado1 == self.lado2 == self.lado3:
            return "triángulo equilátero."
        elif (self.lado1 == self.lado2) or (self.lado1 == self.lado3) or (self.lado2 == self.lado2):
            return "triángulo isósceles."
        else:
            return "triángulo escaleno."


# ------------------ Programa principal --------------------#

# Solicitamos por teclado la longitud de los tres lados del triángulo (valores decimales)
lado1 = float(input("Longitud del primer lado: "))
lado2 = float(input("Longitud del segundo lado: "))
lado3 = float(input("Longitud del tercer lado: "))

# Creamos un objeto de la clase Triangulo
triangulo1 = Triangulo(lado1, lado2, lado3)

# Mostramos sus propiedades por pantalla
triangulo1.propiedades()
print('El lado más largo del triángulo tiene una longitud de', triangulo1.largo())
print('Es un', triangulo1.tipo())
