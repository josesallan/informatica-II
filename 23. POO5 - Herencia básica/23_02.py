# =============================================================================
# DEFINICIÓN DE CLASES
# =============================================================================

class Animal():
    """
    Clase base que representa a un animal genérico en el videojuego.
    """

    def __init__(self, pfuerza):
        # NOVEDAD: Validación de datos dentro del constructor.
        # Condicionamos la creación de las propiedades a que el valor sea válido (<= 5).
        # Si el usuario introduce un número mayor (ej. 6), el 'if' no se ejecuta,
        # las variables no se crean, y Python lanzará un error (AttributeError)
        # al intentar usarlas después.
        if pfuerza <= 5:
            self.vida = 10
            self.fuerza = pfuerza

    def propiedades(self):
        """Muestra por pantalla los valores actuales de vida y fuerza del objeto."""
        print("--- Propiedades del Animal ---")
        print(f"Vida: {self.vida}")
        print(f"Fuerza: {self.fuerza}")
        print("------------------------------")


# =============================================================================
# PROGRAMA PRINCIPAL
# =============================================================================

print("Iniciando el programa...\n")

# NOVEDAD: Interacción con el usuario.
# Pedimos el dato por teclado y lo convertimos a número decimal (float)
# para poder realizar la comprobación matemática (<= 5) en el constructor.
fuerza_usuario = float(input("Introduce el valor de 'fuerza' del objeto a crear: "))

# Creamos el objeto pasándole la variable que acabamos de pedir al usuario.
animal1 = Animal(fuerza_usuario)

# Intentamos mostrar las propiedades del animal.
# ¡Ojo! Si el usuario introdujo una fuerza no permitida, el programa "romperá" aquí.
animal1.propiedades()