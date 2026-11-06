# =============================================================================
# DEFINICIÓN DE CLASES
# =============================================================================

class Animal():
    """Clase Padre o Superclase"""

    # El constructor del padre solo espera recibir la fuerza
    def __init__(self, pfuerza):
        if pfuerza <= 5:
            self.vida = 10
            self.fuerza = pfuerza

    def propiedades(self):
        print(f"Vida: {self.vida}")
        print(f"Fuerza: {self.fuerza}")


class Perro(Animal):

    # NOVEDAD: Constructor propio en la subclase (Herencia Avanzada)
    # Como ahora el tamaño no es fijo, el perro necesita recibir DOS datos al nacer.
    def __init__(self, pfuerza, psize):
        # 1. Delegamos en el padre:
        # El perro no sabe cómo gestionar la vida y la fuerza, de eso se encarga el padre.
        # Usamos super().__init__() para "enviarle" el parámetro de la fuerza a la clase Animal.
        super().__init__(pfuerza)

        # 2. Gestionamos lo propio:
        # Una vez que el padre ha hecho su trabajo, el perro guarda su propiedad exclusiva.
        self.size = psize

    def propiedades(self):
        print("\n>>> Datos del Perro <<<")
        super().propiedades()
        print(f"Tamaño: {self.size}")
        print("-----------------------")


class Gato(Animal):
    hambre = 2

    def propiedades(self):
        print("\n>>> Datos del Gato <<<")
        super().propiedades()  # Mantenemos la buena práctica de usar super()
        print(f"Hambre: {self.hambre}")
        print("----------------------")


class Raton(Animal):
    color = "blanco"

    def propiedades(self):
        print("\n>>> Datos del Ratón <<<")
        super().propiedades()  # Mantenemos la buena práctica de usar super()
        print(f"Color: {self.color}")
        print("-----------------------")


# =============================================================================
# PROGRAMA PRINCIPAL
# =============================================================================

print("Iniciando el creador de personajes...\n")

# NOVEDAD: Petición de múltiples parámetros
fuerza_perro = float(input("Introduce el valor de 'fuerza' del perro a crear: "))
size_perro = float(input("Introduce el valor del 'tamaño' del perro a crear: "))

# Al instanciar el Perro, le pasamos los DOS argumentos que pide su nuevo __init__
perro1 = Perro(fuerza_perro, size_perro)
perro1.propiedades()

fuerza_gato = float(input("\nIntroduce el valor de 'fuerza' del gato a crear: "))
gato1 = Gato(fuerza_gato)
gato1.propiedades()

fuerza_raton = float(input("\nIntroduce el valor de 'fuerza' del ratón a crear: "))
raton1 = Raton(fuerza_raton)
raton1.propiedades()