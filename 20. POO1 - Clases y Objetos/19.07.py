# Definimos la clase Triangulo:
class Triangulo():
    # Propiedades
    tipo = "Triángulo"
    lados = 3
    base = 0.0
    altura = 0.0

    # Procedimientos

    # Calculo de la superficie
    def superficie(self):
        area = self.base * self.altura / 2
        return area


# ------------------ Programa principal --------------------#

# Creamos un objeto de la clase Triangulo
miTriangulo = Triangulo()

# Creamos un segundo objeto de la clase Triangulo
miTriangulo2 = Triangulo()

# Modificamos las propiedades del primer triangulo
miTriangulo.base = 5
miTriangulo.altura = 4

# Preguntamos por las propiedades del segundo triángulo y asignamos esos valores al objeto
print("---- Datos segundo triángulo -----")
base = float(input("Introduce la longitud de la base: "))
altura = float(input("Introduce la longitud de la altura:"))
miTriangulo2.base = base
miTriangulo2.altura = altura

# Mostramos las propiedades de los dos triángulos
print("Propiedades del primer triángulo")
print("--------------------------------")
print("Tipo:", miTriangulo.tipo)
print("Número de lados:", miTriangulo.lados)
print("Longitud de la base:", miTriangulo.base)
print("Longitud de la altura:", miTriangulo.altura)
print("Superficie triángulo:", miTriangulo.superficie())  # Llamamos al procedimiento
print()
print("Propiedades del segundo triángulo")
print("--------------------------------")
print("Tipo:", miTriangulo2.tipo)
print("Número de lados:", miTriangulo2.lados)
print("Longitud de la base:", miTriangulo2.base)
print("Longitud de la altura:", miTriangulo2.altura)
print("Superficie triángulo:", miTriangulo2.superficie()) # Llamamos al procedimiento
