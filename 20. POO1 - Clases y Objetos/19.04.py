# Definimos la clase Triangulo:
class Triangulo():
    # Propiedades
    tipo = "Triángulo"
    lados = 3
    base = 0
    altura = 0


# ------------------ Programa principal --------------------#

# Creamos un objeto de la clase Triangulo
miTriangulo = Triangulo()

# Mostramos las propiedades del objeto miTriangulo
print("Propiedades objeto clase Triangulo")
print("----------------------------------")
print("Tipo:", miTriangulo.tipo)
print("Número de lados:", miTriangulo.lados)
print("Longitud de la base:", miTriangulo.base)
print("Longitud de la altura:", miTriangulo.altura)

# Creamos un segundo objeto de la clase Triangulo
miTriangulo2 = Triangulo()
print()
# Mostramos las propiedades del objeto miTriangulo2
print("Propiedades segundo objeto clase Triangulo")
print("------------------------------------------")
print("Tipo:", miTriangulo2.tipo)
print("Número de lados:", miTriangulo2.lados)
print("Longitud de la base:", miTriangulo2.base)
print("Longitud de la altura:", miTriangulo2.altura)
