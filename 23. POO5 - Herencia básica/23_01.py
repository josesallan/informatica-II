# =============================================================================
# DEFINICIÓN DE CLASES
# =============================================================================

class Animal():
    """
    Clase base que representa a un animal genérico en el videojuego.
    Más adelante, otras clases (como Perros o Gatos) heredarán de ella.
    """

    # El método __init__ es el CONSTRUCTOR.
    # Se ejecuta de forma automática cada vez que creamos un nuevo animal.
    def __init__(self, pfuerza):
        # 'self' es obligatorio y hace referencia al propio objeto que se está creando.

        # Propiedad fija: Todos los animales nacen con 10 puntos de vida por defecto.
        self.vida = 10

        # Propiedad dinámica: La fuerza se asigna a través del parámetro 'pfuerza'
        # que recibimos al momento de crear el objeto.
        self.fuerza = pfuerza

    # Este método define un "comportamiento" del objeto: mostrar sus datos.
    def propiedades(self):
        """Muestra por pantalla los valores actuales de vida y fuerza del objeto."""

        print("--- Propiedades del Animal ---")

        # Utilizamos f-strings (f"...") en lugar de .format().
        # Es una forma más moderna y legible de incrustar variables en un texto.
        print(f"Vida: {self.vida}")
        print(f"Fuerza: {self.fuerza}")
        print("------------------------------")


# =============================================================================
# PROGRAMA PRINCIPAL
# =============================================================================

print("Iniciando el programa...\n")

# 1. CREACIÓN DEL OBJETO (Instanciación)
# Creamos un nuevo objeto a partir del "molde" de la clase Animal.
# Al escribir Animal(5), el número '5' viaja automáticamente al parámetro 'pfuerza' del constructor.
animal1 = Animal(5)

# 2. USO DE MÉTODOS
# Le pedimos a nuestro nuevo objeto 'animal1' que ejecute su método 'propiedades()'
# para que nos muestre por pantalla cómo han quedado establecidas los valores de sus propiedades.
animal1.propiedades()
