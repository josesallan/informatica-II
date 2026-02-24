# =============================================================================
# EJERCICIO 1: LA ORQUESTA SINFÓNICA (Polimorfismo Básico)
# =============================================================================

# 1. LA SUPERCLASE (Nuestro contrato o molde)
class Instrumento():
    def tocar(self):
        # Usamos 'pass' porque un "instrumento genérico" no tiene un sonido concreto.
        # Esto sirve para avisar de que todas las clases hijas DEBEN tener este método.
        pass


# 2. LAS SUBCLASES (Nuestros instrumentos concretos)
class Guitarra(Instrumento):
    # Sobrescribimos el método tocar() con el sonido específico de la guitarra
    def tocar(self):
        print("Guitarra: ¡Plin, plin, plin!")


class Tambor(Instrumento):
    # Sobrescribimos el método tocar() con el sonido específico del tambor
    def tocar(self):
        print("Tambor: ¡Pom, pom, pom!")


class Piano(Instrumento):
    # Sobrescribimos el método tocar() con el sonido específico del piano
    def tocar(self):
        print("Piano: ¡Do, re, mi, fa, sol!")


# =============================================================================
# PROGRAMA PRINCIPAL
# =============================================================================

print("Afinando los instrumentos...\n")

# Creamos un objeto de cada clase
mi_guitarra = Guitarra()
mi_tambor = Tambor()
mi_piano = Piano()

# Metemos todos los objetos (que son de clases diferentes) en una misma lista
orquesta = [mi_guitarra, mi_tambor, mi_piano]

print("¡Que comience el concierto!\n")

# 3. LA MAGIA DEL POLIMORFISMO
# Recorremos la lista. En cada vuelta, la variable 'instrumento' será uno distinto.
for instrumento in orquesta:

    # Le damos a todos EXACTAMENTE la misma orden.
    # Python evalúa dinámicamente qué instrumento es en este milisegundo
    # y hace sonar la versión correcta del método tocar().
    # ¡Todo esto sin escribir ni un solo 'if'!
    instrumento.tocar()

print("\n¡Bravo! (Aplausos del público)")