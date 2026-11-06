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
        print("--- Propiedades ---")
        # Utilizamos f-strings en lugar de .format()
        print(f"Vida: {self.vida}")
        print(f"Fuerza: {self.fuerza}")
        print("-------------------")


# NOVEDAD: Creación de Subclases (Herencia)
# Al escribir (Animal) entre los paréntesis, le indicamos a Python que la clase
# 'Perro' va a heredar TODOS los métodos y propiedades de la clase 'Animal'.
class Perro(Animal):
    """Subclase que hereda de Animal"""

    # NOVEDAD: Propiedad exclusiva de la subclase.
    # Además de lo que hereda de Animal, añadimos características propias.
    # Todos los objetos de la clase Perro nacerán con un tamaño de 3.
    size = 3


class Gato(Animal):
    """Subclase que hereda de Animal"""
    hambre = 2


class Raton(Animal):
    """Subclase que hereda de Animal"""
    color = "blanco"


# =============================================================================
# PROGRAMA PRINCIPAL
# =============================================================================

print("Iniciando el programa...\n")

fuerza_usuario = float(input("Introduce el valor de 'fuerza' del objeto a crear: "))

# NOVEDAD: Instanciando una subclase
# Fíjate bien: estamos creando un objeto de la clase 'Perro', no de 'Animal'.
# Aunque no hemos escrito un método __init__ dentro de la clase Perro,
# Python va a buscar inteligentemente el __init__ a su clase padre.
# Por eso sigue siendo necesario pasarle el parámetro de la fuerza.
perro1 = Perro(fuerza_usuario)

# NOVEDAD: Uso de un método heredado
# El objeto 'perro1' puede usar el método 'propiedades()' perfectamente,
# ¡sin que hayamos tenido que escribir ni una sola línea de ese método en Perro!
perro1.propiedades()
