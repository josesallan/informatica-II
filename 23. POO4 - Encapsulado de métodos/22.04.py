# Defino la clase Usuario
class Usuario():
    # A través de un constructor defino dos propiedades nombre y contraseña
    def __init__(self, pnombre, ppassword):
        self.nombre = pnombre
        self.__password = ppassword

    # Método que exporta el valor del la propiedad password
    def mostrar_password(self):
        return self.__password

    # Método que actualiza la contraseña con un valor recibido como parámetro
    def nuevo_password(self, pnpassword):
        self.__password = pnpassword


# ------------------ Programa principal --------------------#

# Solicito los datos del usuario a crear
nombre = input("Introduce el nombre del usuario: ")
password = input("Introduce la contraseña del usuario: ")
# Creo un usuario
usuario1 = Usuario(pnombre=nombre, ppassword=password)
# Muestro sus propiedades por pantalla
print(f"- Las propiedades del objeto {usuario1.nombre} son:")
print(f'  * Nombre del usuario: {usuario1.nombre}')
print(f'  * Contraseña del usuario: {usuario1.mostrar_password()}')

# Solicitamos una nueva contraseña
new_password = input(f'Introduce la nueva contraseña del objeto {usuario1.nombre}:')
usuario1.nuevo_password(pnpassword=new_password)

# Muestro las nuevas propiedades por pantalla
# Muestro sus propiedades por pantalla
print(f"- Las propiedades del objeto {usuario1.nombre} son:")
print(f'  * Nombre del usuario: {usuario1.nombre}')
print(f'  * Contraseña del usuario: {usuario1.mostrar_password()}')
