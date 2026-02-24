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
    # Constructor propio (Herencia Avanzada)
    def __init__(self, pfuerza, psize):
        super().__init__(pfuerza)
        self.size = psize

    def propiedades(self):
        print("\n>>> Datos del Perro <<<")
        super().propiedades()
        print(f"Tamaño: {self.size}")
        print("-----------------------")

    # ATENCIÓN: En este paso AÚN NO hemos programado el método __str__


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

print("Iniciando el creador de personajes...\n")

fuerza_perro = float(input("Introduce el valor de 'fuerza' del perro a crear: "))
size_perro = float(input("Introduce el valor del 'tamaño' del perro a crear: "))

perro1 = Perro(fuerza_perro, size_perro)
perro1.propiedades()

print("\n" + "=" * 40)
print("EJERCICIO 8: Intentando imprimir el objeto directamente")
print("=" * 40 + "\n")

# NOVEDAD Y PROBLEMA (Ejercicio 8):
# Le pedimos a Python que imprima directamente la variable 'perro1'.
# Como 'perro1' no es un texto, ni un número, sino un OBJETO COMPLEJO,
# Python no sabe qué partes de ese objeto queremos mostrar.
print(perro1)

# ¿QUÉ ES ESE RESULTADO RARO?
# Verás algo como esto: <__main__.Perro object at 0x000001C1A5407580>
# Como no le hemos enseñado a la clase Perro cómo debe "presentarse" en texto,
# Python hace lo único que puede: decirnos de qué clase es el objeto (__main__.Perro)
# y en qué "cajón" exacto de la memoria RAM del ordenador está guardado (el código 0x...).
# ¡Esto es útil para el ordenador, pero inútil para un jugador humano!