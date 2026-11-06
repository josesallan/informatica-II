# =============================================================================
# DEFINICIÓN DE CLASES
# =============================================================================

class Animal():
    """Clase Padre o Superclase"""
    def __init__(self, pfuerza):
        if pfuerza <= 5:
            self.vida = 10
            self.fuerza = pfuerza

    def propiedades(self):
        print(f"Vida: {self.vida}")
        print(f"Fuerza: {self.fuerza}")


class Perro(Animal):
    size = 3

    def propiedades(self):
        print("\n>>> Datos del Perro <<<")
        super().propiedades()
        print(f"Tamaño: {self.size}")
        print("-----------------------")

    # NOVEDAD: Método exclusivo de la subclase
    # Este método SOLO existe dentro de la clase Perro.
    # Ni la clase Animal, ni la clase Gato, ni la clase Raton saben qué es "ladrar".
    def ladrar(self):
        print("¡Guau, guau!")


class Gato(Animal):
    hambre = 2

    def propiedades(self):
        print("\n>>> Datos del Gato <<<")
        super().propiedades()
        print(f"Hambre: {self.hambre}")
        print("----------------------")


class Raton(Animal):
    color = "blanco"

    def propiedades(self):
        print("\n>>> Datos del Ratón <<<")
        super().propiedades()
        print(f"Color: {self.color}")
        print("-----------------------")


# =============================================================================
# PROGRAMA PRINCIPAL
# =============================================================================

print("Iniciando el programa...\n")

# Creamos un perro y un gato
fuerza_perro = float(input("Introduce la fuerza del perro: "))
perro1 = Perro(fuerza_perro)

fuerza_gato = float(input("Introduce la fuerza del gato: "))
gato1 = Gato(fuerza_gato)


# 1. EL PERRO LADRA
print("\nTurno del perro:")
perro1.propiedades()
# Como perro1 es un objeto de la clase Perro, puede usar el método ladrar()
perro1.ladrar()


# 2. EL GATO INTENTA LADRAR (Comprobación de error)
print("\nTurno del gato:")
gato1.propiedades()

# PRUEBA DIDÁCTICA:
# Quita la almohadilla (#) de la siguiente línea para comprobar qué ocurre
# si un gato intenta usar un método que pertenece exclusivamente a la clase Perro.
# gato1.ladrar()