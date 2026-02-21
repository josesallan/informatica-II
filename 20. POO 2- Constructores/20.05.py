# Definimos la clase Persona
class Persona():
    # Método constructor, recibe como parametros los valores de las propiedades name y age.
    def __init__(self, name, age):
        self.nombre = name
        self.edad = age

    def mostrar(self):
        print(self.nombre)
        print(self.edad)

    # Modificamos el método mayor para que en lugar de escribir un texto por pantalla
    # devuelva un valor lógico en función del caso en el que estemos.
    def mayor(self):
        if self.edad >= 18:
            return True
        else:
            return False


# ------------------ Programa principal --------------------#

# Solicitamos los datos por pantalla
nombre = input("Nombre de la persona: ")
edad = int(input("Edad de " + nombre + ": "))

# Creamos un objeto de la clase Persona y le asignamos el nombre persona1
persona1 = Persona(nombre, edad)

# Iniciamos el proceso de control de acceso al juego
respuesta = input("¿Quieres jugar una partida de 'Python: The Game' (S/N)? ")

# La primera condición para poder jugar es que la respuesta sea 'S'
if respuesta.upper() == "S":
    # En este caso debemos comprobar si el posible jugador es mayor de edad o si no lo es.
    if persona1.mayor() is True:
        print(" Bienvenido a 'Python: The Game'")
    else:
        print("No tienes edad suficiente para jugar a 'Python: The Game'.")
