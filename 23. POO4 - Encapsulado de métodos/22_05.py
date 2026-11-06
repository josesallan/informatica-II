import os


# Defino la clase Usuario
class Usuario():
    # A través de un constructor defino dos propiedades nombre y contraseña
    def __init__(self, pnombre, ppassword):
        self.nombre = pnombre
        self.__password = ppassword

    # Método para mostrar las propiedades del objeto
    def propiedades(self):
        print()
        texto = "Las propiedades del objeto " + str(self.nombre) + " son:"
        print(texto)
        print(len(texto) * "=")
        print("Nombre de usuario:", self.nombre)
        print("contraseña del usuario:", self.__password)

    # Método que exporta el valor del la propiedad password
    def mostrar_password(self):
        return self.__password

    # Método que actualiza la contraseña con un valor recibido como parámetro
    def nuevo_password(self, pnpassword):
        self.__password = pnpassword

    # Método que modifica el nombre del usuario
    def nuevo_nombre(self, pnnombre):
        self.nombre = pnnombre


# ------------------ Programa principal --------------------#

# Creo un usuario
nombre = input("Introduce el nombre del usuario: ")
password = input("Introduce la contraseña del usuario: ")
usuario1 = Usuario(nombre, password)
os.system("clear")
while True:
    print()
    print(" - Menú de configuración de usuario:")
    print("   =================================")
    print("a) Mostrar el nombre del usuario")
    print("b) Mostrar el nombre y la contraseña del usuario")
    print("c) Cambiar en nombre del usuario")
    print("d) Cambiar la contraseña del usuario")
    print("e) Salir del programa")
    opcion = input("Selecciona una opción:")
    os.system("clear")
    if opcion == "a":
        print("El nombre del usuario es:", usuario1.nombre)
    elif opcion == "b":
        usuario1.propiedades()
    elif opcion == "c":
        nuevoNombre = input("Introduce el nuevo nombre del objeto " + usuario1.nombre + ": ")
        usuario1.nuevo_nombre(nuevoNombre)
    elif opcion == "d":
        nuevoPassword = input("Introduce la nueva contraseña del objeto " + usuario1.nombre + ": ")
        usuario1.nuevo_password(nuevoPassword)
    else:
        print("Programa terminado")
        break
