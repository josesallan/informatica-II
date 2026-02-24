import os


# Definición de la clase Usuario
class Usuario():
    # A través de un constructor defino dos propiedades nombre y contraseña
    def __init__(self, pnombre, ppassword):
        self.nombre = pnombre
        self.__password = ppassword
        # Añadimos dos variables encapsuladas para gestionar el posible bloqueo de contraseña.
        self.__intentos = 3
        self.__bloqueada = False

    # Método de comprobación de contraseña
    def __passwordCandidate(self):
        # Inicalmente comprobamos que la cuenta no está bloqueada.  En caso de estarlo el programa finaliza
        if self.__bloqueada is True:
            print('Operación denegada. La cuenta está bloqueada')
        else:
            aComprobar = input("Introduce el valor de la contraseña actual:")
            if aComprobar == self.__password:
                print("Contraseña válida")
                return True
            else:
                print("Contraseña incorrecta")

                # Modificamos el número de intentos restantes (restamos uno)
                self.__intentos = self.__intentos - 1
                # Mostramos por pantalla el número de intentos restantes
                print(f'{self.__intentos} intentos restantes.')
                if self.__intentos == 0:
                    self.__bloquear_cuenta()
                return False

    # Método para mostrar las propiedades del objeto
    def propiedades(self):
        print()
        correcto = self.__passwordCandidate()
        if correcto:
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
        correcto = self.__passwordCandidate()
        if correcto:
            self.__password = pnpassword

    # Método que modifica el nombre del usuario
    def nuevo_nombre(self, pnnombre):
        correcto = self.__passwordCandidate()
        if correcto:
            self.nombre = pnnombre

    # Método encapsulado que bloquea la cuenta
    def __bloquear_cuenta(self):
        self.__bloqueada = True
        print('¡Cuenta bloqueada por seguridad!')

    # Añadimos un método __str__(self), este es el método que se genera al invocar el nombre del objeto
    # En este caso mostraremos el nombre del objeto e informaremos de si la cuenta esta activa o bloqueada
    def __str__(self):
        cadena = '- Nombre de usuarios: ' + self.nombre + '\n'
        if self.__bloqueada is True:
            cadena = cadena + '   - Cuenta bloqueada'
        else:
            cadena = cadena + '   - Cuenta operativa'
        return cadena


# ------------------ Programa principal --------------------#
# Creamos un usuario
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
    print("e) Ejecutar el módulo de control de contraseña")
    print("f) Salir del programa")
    opcion = input("Selecciona una opción:")
    os.system("clear")
    if opcion == "a":
        print(usuario1)
    elif opcion == "b":
        usuario1.propiedades()
    elif opcion == "c":
        nuevoNombre = input("Introduce el nuevo nombre del objeto " + usuario1.nombre + ": ")
        usuario1.nuevo_nombre(nuevoNombre)
    elif opcion == "d":
        nuevoPassword = input("Introduce la nueva contraseña del objeto " + usuario1.nombre + ": ")
        usuario1.nuevo_password(nuevoPassword)
    elif opcion == "e":
        usuario1.__passwordCandidate()
    else:
        print("Programa terminado")
        break
