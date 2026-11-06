# =============================================================================
# EJERCICIO 2: EL ATAQUE DEL EQUIPO (Pythonator)
# =============================================================================

# 1. LA SUPERCLASE (Nuestro molde para cualquier personaje)
class Personaje():
    # Definimos el constructor. TODOS los personajes tendrán un nombre.
    def __init__(self, nombre):
        self.nombre = nombre

    # Definimos la acción genérica.
    # Usamos 'pass' porque un "personaje" sin clase aún no sabe cómo atacar.
    def atacar(self):
        pass


# 2. LAS SUBCLASES (Nuestras clases del videojuego)
# Al poner (Personaje), heredan automáticamente el __init__ con el nombre
class Guerrero(Personaje):
    def atacar(self):
        # Usamos self.nombre, que lo ha heredado de la clase padre
        print(f"🗡️ ¡{self.nombre} ataca con un espadazo brutal!")


class Mago(Personaje):
    def atacar(self):
        print(f"🔥 ¡{self.nombre} lanza una bola de fuego devastadora!")


class Arquero(Personaje):
    def atacar(self):
        print(f"🏹 ¡{self.nombre} dispara una flecha certera entre ceja y ceja!")


# =============================================================================
# PROGRAMA PRINCIPAL
# =============================================================================

print("Generando los personajes de la partida...\n")

# Creamos nuestros objetos.
# Fijémonos en que les pasamos el nombre entre paréntesis porque
# están usando el __init__ de la clase padre (Personaje).
arturo = Guerrero("Arturo")
merlin = Mago("Merlín")
legolas = Arquero("Legolas")

# Agrupamos a todos los objetos en una lista (nuestro equipo de batalla)
equipo = [arturo, merlin, legolas]

print("¡Aparece un dragón salvaje! El equipo entra en combate:\n")

# 3. EL SUPERPODER DEL POLIMORFISMO
# Le damos la misma orden de atacar a todo el equipo con un solo bucle.
for heroe in equipo:

    # Python descubre de qué clase es cada 'heroe' en el momento
    # y ejecuta su propio método atacar() personalizado.
    heroe.atacar()

print("\n¡El dragón ha sido derrotado! Fin del combate.")
