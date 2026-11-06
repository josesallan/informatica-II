# Definimos la clase Videojuego:
class Videojuego():
    # Propiedades
    titulo = 'Sin título'
    nivel = 1
    puntuacion = 0
    completado = False

    # Métodos
    def subir_nivel(self):
        # Incrementa nivel en 1
        self.nivel = self.nivel + 1

    def completar_juego(self):
        # Cambia del valor de la propiedad completado a True
        self.completado = True

    def propiedades(self):
        print('Título del videojuego : ', self.titulo)
        print('Nivel: ', self.nivel)
        print('Puntuación: ', self.puntuacion)
        print('Videojuego completado: ', self.completado)


# ------------------ Programa principal --------------------#

# Creamos un objeto de la clase Videojuego
videojuego1 = Videojuego()

# Mostramos los valores de las propiedades iniciales
videojuego1.propiedades()

# Modificio el valor de las propiedades
videojuego1.subir_nivel()
videojuego1.completar_juego()

# Mostramos los valores de las propiedades tras los cambios
videojuego1.propiedades()

