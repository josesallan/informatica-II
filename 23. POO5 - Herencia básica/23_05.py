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
        # Método común para todos los animales
        print(f"Vida: {self.vida}")
        print(f"Fuerza: {self.fuerza}")


class Perro(Animal):
    size = 3

    # NOVEDAD (Consolidación): Sobrescritura usando super()
    def propiedades(self):
        print("\n>>> Datos del Perro <<<")
        # Llamamos al padre para que imprima vida y fuerza
        super().propiedades()
        # Imprimimos lo exclusivo del perro
        print(f"Tamaño: {self.size}")
        print("-----------------------")


class Gato(Animal):
    hambre = 2

    # Aplicamos la misma técnica para el gato
    def propiedades(self):
        print("\n>>> Datos del Gato <<<")
        # super() nos ahorra volver a escribir los print de vida y fuerza
        super().propiedades()
        print(f"Hambre: {self.hambre}")
        print("----------------------")


class Raton(Animal):
    color = "blanco"

    # Y la misma técnica para el ratón
    def propiedades(self):
        print("\n>>> Datos del Ratón <<<")
        super().propiedades()
        print(f"Color: {self.color}")
        print("-----------------------")


# =============================================================================
# PROGRAMA PRINCIPAL
# =============================================================================

print("Iniciando el creador de personajes...\n")

# Creación e impresión del Perro
fuerza_perro = float(input("Introduce el valor de 'fuerza' del perro a crear: "))
perro1 = Perro(fuerza_perro)
perro1.propiedades()

# Creación e impresión del Gato
fuerza_gato = float(input("\nIntroduce el valor de 'fuerza' del gato a crear: "))
gato1 = Gato(fuerza_gato)
gato1.propiedades()

# Creación e impresión del Ratón
fuerza_raton = float(input("\nIntroduce el valor de 'fuerza' del ratón a crear: "))
raton1 = Raton(fuerza_raton)
raton1.propiedades()