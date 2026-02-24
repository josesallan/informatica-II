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
    def __init__(self, pfuerza, psize):
        super().__init__(pfuerza)
        self.size = psize

    def propiedades(self):
        print("\n>>> Datos del Perro <<<")
        super().propiedades()
        print(f"Tamaño: {self.size}")
        print("-----------------------")

    # NOVEDAD: El método mágico __str__ (Ejercicios 8 y 9)
    # Los métodos que van entre dobles guiones bajos son "mágicos" porque Python
    # los llama automáticamente en ciertas situaciones.
    # __str__ se ejecuta automáticamente cuando intentamos imprimir el objeto con un print().
    def __str__(self):
        # MUY IMPORTANTE: Este método NO debe usar print(), sino que debe
        # DEVOLVER (return) una cadena de texto (string).
        return f"Este perro tiene {self.fuerza} puntos de fuerza, {self.vida} puntos de vida y un tamaño de {self.size}."


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

# NOVEDAD: Imprimir el objeto directamente
# Al hacer print(perro1), Python busca si la clase Perro tiene un método __str__.
# Como ahora sí lo tiene, en lugar de mostrar su posición en la memoria RAM,
# mostrará la frase bonita que hemos diseñado con el 'return'.
print("\nProbando el método __str__:")
print(perro1)

print("\n" + "=" * 40 + "\n")

fuerza_gato = float(input("Introduce el valor de 'fuerza' del gato a crear: "))
gato1 = Gato(fuerza_gato)
gato1.propiedades()

fuerza_raton = float(input("\nIntroduce el valor de 'fuerza' del ratón a crear: "))
raton1 = Raton(fuerza_raton)
raton1.propiedades()