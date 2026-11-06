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
        # Este es el método original de la superclase
        print("--- Propiedades ---")
        print(f"Vida: {self.vida}")
        print(f"Fuerza: {self.fuerza}")


class Perro(Animal):
    """Subclase que hereda de Animal"""
    size = 3

    # NOVEDAD: Sobrescritura de métodos y la función super()
    # Al crear un método con el mismo nombre, Python ejecutará ESTE en lugar del original.
    def propiedades(self):
        print("\n>>> Datos del Perro <<<")

        # ¡LA MAGIA DE super()!
        # En lugar de repetir los print() de vida y fuerza, llamamos al método
        # propiedades() de la superclase (Animal). Él hará ese trabajo por nosotros.
        super().propiedades()

        # Una vez que el padre ha terminado, simplemente añadimos la información exclusiva de esta subclase:
        print(f"Tamaño: {self.size}")
        print("-------------------")


class Gato(Animal):
    hambre = 2

class Raton(Animal):
    color = "blanco"


# =============================================================================
# PROGRAMA PRINCIPAL
# =============================================================================

print("Iniciando el programa...\n")

fuerza_usuario = float(input("Introduce el valor de 'fuerza' del objeto a crear: "))

perro1 = Perro(fuerza_usuario)

# Al llamar a propiedades(), Python buscará primero dentro de la clase Perro.
# Como lo hemos sobrescrito, ejecutará el nuevo método, el cual a su vez llamará al del padre.
perro1.propiedades()