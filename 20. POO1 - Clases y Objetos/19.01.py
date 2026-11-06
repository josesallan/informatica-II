# Definimos la clase Libro:
class Libro():
    # Propiedades y valores iniciales
    propietario = "José Antonio Sallán Arasanz"
    read = False


# ------------------ Programa principal --------------------#
# Creamos una instancia de la clase Libro, objeto al que llamaremos miLibro
miLibro = Libro()

# Mostramos por pantalla el valor de la propiedad propietario y el estado read.
print(miLibro.propietario)
print(miLibro.read)
