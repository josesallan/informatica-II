# Defino la clase Usuario
class Usuario():
    # A través de un constructor defino dos propiedades nombre y contraseña
    def __init__(self, pnombre, ppassword):
        self.nombre = pnombre
        self.password = ppassword


# ------------------ Programa principal --------------------#

# Solicito los datos del usuario a crear
nombre = input("Introduce el nombre del usuario: ")
password = input("Introduce la contraseña del usuario: ")
# Creo un usuario
usuario1 = Usuario(pnombre=nombre, ppassword=password)
# Muestro sus propiedades por pantalla
# Muestro sus propiedades por pantalla
print(f"- Las propiedades del objeto {usuario1.nombre} son:")
print(f'  * Nombre del usuario: {usuario1.nombre}')
print(f'  * Contraseña del usuario: {usuario1.password}')
