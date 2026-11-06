# Definimos la clase Videojuego:
class Videojuego():
    # Propiedades
    titulo = 'Sin título'
    nivel = 1
    puntuacion = 0
    completado = False
    favorito = False

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
        print('Video juego favorito:', self.favorito)

    def sumar_puntos(self, puntos):
        self.puntuacion = self.puntuacion + puntos

    def cambiar_titulo(self, nuevo_titulo):
        self.titulo = nuevo_titulo

    def marcar_favorito(self, favorito):
        self.favorito = favorito

    def comparar_puntuacion(self, otro_videojuego):
        # comparar self.puntuacion con otro_videojuego.puntuacion
        if self.puntuacion > otro_videojuego.puntuacion:
            print(self.titulo, 'tiene una puntuación mayor que', otro_videojuego.titulo)
        elif self.puntuacion < otro_videojuego.puntuacion:
            print(otro_videojuego.titulo, 'tiene una puntuación mayor que', self.titulo)
        else:
            print(self.titulo, 'y', otro_videojuego.titulo, 'tienen  la misma puntuación')


# ------------------ Programa principal --------------------#

# Creamos un objeto de la clase Videojuego
videojuego1 = Videojuego()

# Mostramos los valores de las propiedades iniciales
videojuego1.propiedades()

# Modificio el valor de las propiedades
videojuego1.sumar_puntos(150)
videojuego1.subir_nivel()
videojuego1.cambiar_titulo('Aventura Espacial')

# Mostramos los valores de las propiedades tras los cambios
videojuego1.propiedades()

# Creamos un  segundo objeto de la clase Videojuego
videojuego2 = Videojuego()

# Mostramos los valores de las propiedades iniciales
videojuego2.propiedades()

# Modificio el valor de las propiedades
videojuego2.sumar_puntos(100)
videojuego2.subir_nivel()
videojuego2.cambiar_titulo('Python - The Game')
videojuego2.marcar_favorito(True)

# Mostramos los valores de las propiedades tras los cambios
videojuego2.propiedades()

# Indicaremos cual de los dos juegos tiene una mayor puntuación
videojuego1.comparar_puntuacion(videojuego2)

