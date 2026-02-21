# Definimos la clase Libro:
class Libro():
    # Propiedades y valores iniciales
    propietario = "José Antonio Sallán Arasanz"
    read = False

    # Definimos los métodos de la clase Libro.
    def leido(self):
        # Informa sobre si el libro ha sido leído o todavía no, comprobando propiedad self.read
        if self.read is True:
            print("Ya has leído este libro")
        else:
            print("Todavía no has leído este libro")

    def leer(self):
        # Asigna el valor True a la propiedad read
        self.read = True


# ------------------ Programa principal --------------------#
# Creamos una instancia de la clase Libro, objeto al que llamaremos miLibro
miLibro = Libro()

# Mostramos por pantalla el valor de la propiedad propietario y el estado read al iniciar el programa.
print("Propiedades iniciales")
print("---------------------")
print("Propietario:", miLibro.propietario)
print("Estado propiedad read:", miLibro.read)

# Ejecutamos el método read, para informar sobre la lectura o no lectura del libro.
miLibro.leido()

# Ejecutamos el metodo leer.
miLibro.leer()
print()

# Mostramos las propiedades y estados tras realizar la lectura del libro
print("Propiedades tras lectura")
print("------------------------")
print("Propietario:", miLibro.propietario)
print("Estado propiedad read:", miLibro.read)
# Ejecutamos el método read, para informar sobre la lectura o no lectura del libro.
miLibro.leido()
