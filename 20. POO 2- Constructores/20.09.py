# Definimos la clase Persona
class Persona():
    # Método constructor, recibe como parametros los valores de las propiedades name y age.
    def __init__(self, name, age=18):
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
print("Introduce los datos de la primera persona a crear:")
nombre = input("Nombre de la persona: ")
edad = int(input("Edad de " + nombre + ": "))
# Creamos el objeto enviando los dos valores como parámetros
p1 = Persona(nombre, edad)


print("Introduce los datos de la segunda persona a crear:")
nombre = input("Nombre de la persona: ")
#Creamos el objeto enviando únicamente el valor del nombre como parámetro
p2 = Persona(nombre)

# Mostramos las propiedades de cada uno  de los objetos
p1.mostrar()
# Iniciamos el proceso de control de acceso al juego

# comprobamos si la persona1 es mayor de edad.
if p1.mayor() is True:
    print(" Eres mayor de edad")
else:
    print(" Todavía no eres mayor de edad")

p2.mostrar()
# comprobamos si la persona2 es mayor de edad.
if p2.mayor() is True:
    print(" Eres mayor de edad")
else:
    print(" Todavía no eres mayor de edad")

