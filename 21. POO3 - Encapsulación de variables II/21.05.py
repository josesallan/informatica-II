# Definimos la clase Rectangulo y sus características
class Rectangulo():
    # El constructor recibe como parámetro el valor de la longituda de la base y la altura
    def __init__(self, pbase, paltura):
        # Encapsulamos la propiedad lados para que no se pueda modifcar desde fuera del código de la clase.
        self.__lados = 4
        self.base = pbase
        self.altura = paltura

    # Este método muestra las propiedades de los objetos de la clase
    def propiedades(self):
        print("Número de lados:", self.__lados)
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

# Incluimos las ordenes que solicitan el valor de las dimensiones del rectángulo dentro de sendos
# bucles infinitos.  Estos bucles continuarán pidiendo el valor hasta que el valor intorducido sea mayor
# que cero
while True:
    try:
        base = float(input("Introduce el valor de la longitud de la base: "))
        if base < 0:
            raise ValueError
            # generamos ese tipo de error en concreto ya que es el mismo que se produciré
            # si introducimos una cadena de texto.  Con ello conseguimos gestionar las dos
            # situaciones con la misma expcepción.
        break
    except ValueError:
        print("La longitud ha de ser un valor numérico mayor que cero")

while True:
    try:
        altura = float(input("Introduce el valor de la longitud de la altura: "))
        if altura < 0:
            raise ValueError
        break
    except ValueError:
        print("La longitud ha de ser un valor numérico mayor que cero")

# Creamos el objeto, enviando como parámetros sus medidas
miRectangulo1 = Rectangulo(base, altura)

while True:
    try:
        lados = int(input("Introduce el número de lados del rectángulo: "))
        if lados < 0:
            raise ValueError
        break
    except ValueError:
        print("El número de lados ha de ser superior a cero")

# Modificamos el valor de la propiedad lados
miRectangulo1.__lados = lados

miRectangulo1.propiedades()

# Observa que si imprimimos la variable mirectangulo1.__lados, si que toma el valor con el número
# nuevo de lados... pero es una variable nueva, no la propiedad de nuestro objeto.
print(miRectangulo1.__lados)
