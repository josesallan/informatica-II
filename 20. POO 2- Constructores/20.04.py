# Definimos la clase Persona
class Persona():
    # Método constructor, recibe como parametros los valores de las propiedades name y age.
    def __init__(self, name, age):
        self.nombre = name
        self.edad = age

    def mostrar(self):
        print(self.nombre)
        print(self.edad)

    def mayor(self):
        if self.edad >= 18:
            print(self.nombre, "es mayor de edad")
        else:
            print(self.nombre, "todavía no es mayor de edad")


# ------------------ Programa principal --------------------#

# Solicitamos los datos por pantalla
nombre = input("Nombre de la persona: ")
edad = int(input("Edad de " + nombre + ": "))

# Creamos un objeto de la clase persona, enviamos los valores a tomar por las propiedades
# nombre y edad
persona1 = Persona(nombre, edad)

# Mostramos los resultados por pantalla
persona1.mostrar()

# Indicamos si la persona es o no es mayor de edad.
persona1.mayor()
