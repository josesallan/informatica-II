# Definimos la clase CuentaBancaria
class CuentaBancaria():
    # Definimos el constructor
    # Por defecto el valor de saldo será 0 y el de activa True
    def __init__(self, titular, saldo=0.0, activa=True):
        self.titular = titular
        self.saldo = saldo
        self.__activa = activa

    # Método que muestra las propiedades por pantalla
    def datos(self):
        print(' - Titular de la cuenta: ', self.titular)
        print(' - Saldo actual en euros: ', self.saldo)
        print(' - Estado de la cuenta: ', end='')
        if self.__activa is True:
            print('Activa')
        else:
            print('Pendiente de activación')

    # Método para ingresar cantidad
    def ingresar(self, cantidad=0):
        self.saldo = self.saldo + cantidad

    # Método para retirar cantidad
    def retirar(self, cantidad=0):
        if cantidad <= self.saldo:
            self.saldo = self.saldo - cantidad
        else:
            pass

    # Método para descativar cuenta
    def desactivar(self):
        self.__activa = False


# ------------------ Programa principal --------------------#

# Objetos creado con parámetros prosicionales:
print("Creando el primer objeto")
titular = input(' - Introduce el nombre del titular: ')
saldo = float(input(' - Intorduce el saldo inicial de la cuenta de ' + titular + ' :'))
estado = input(' - Está la cuenta activada (S/N)')
if estado.upper() == "S":
    activa = True
else:
    activa = False

cliente1 = CuentaBancaria(titular, saldo, activa)
print(cliente1.datos())

# Objetos creado con parámetros por:
print("Creando el segundo objeto")
titular = input(' - Introduce el nombre del titular: ')
saldo = float(input(' - Intorduce el saldo inicial de la cuenta de ' + titular + ' :'))
estado = input(' - Está la cuenta activada (S/N)')
if estado.upper() == "S":
    activa = True
else:
    activa = False

cliente2 = CuentaBancaria(activa=activa, titular=titular, saldo=saldo)
print(cliente2.datos())

# Objetos creado con parámetros prosicionales y nombre:
print("Creando el tercer objeto")
titular = input(' - Introduce el nombre del titular: ')
saldo = float(input(' - Intorduce el saldo inicial de la cuenta de ' + titular + ' :'))
estado = input(' - Está la cuenta activada (S/N)')
if estado.upper() == "S":
    activa = True
else:
    activa = False

cliente3 = CuentaBancaria(titular, activa=activa, saldo=saldo)
print(cliente3.datos())

# ------------------ Operaciones con los objetos --------------------#

print("\n--- Operaciones con las cuentas ---\n")

# Cliente 1
print("Operaciones para cliente 1:")
cliente1.ingresar(200)        # Ingresamos 200 €
cliente1.retirar(50)          # Retiramos 50 €
cliente1.desactivar()          # Desactivamos la cuenta
print("Estado final de la cuenta del cliente 1:")
cliente1.datos()               # Mostramos las propiedades actualizadas
print("\n")

# Cliente 2
print("Operaciones para cliente 2:")
cliente2.ingresar(1000)       # Ingresamos 1000 €
cliente2.retirar(2000)        # Intentamos retirar más de lo que hay (no debería cambiar el saldo)
print("Estado final de la cuenta del cliente 2:")
cliente2.datos()               # Mostramos las propiedades actualizadas
print("\n")

# Cliente 3
print("Operaciones para cliente 3:")
cliente3.retirar(50)           # Retiramos 50 €
cliente3.ingresar(500)         # Ingresamos 500 €
print("Estado final de la cuenta del cliente 3:")
cliente3.datos()               # Mostramos las propiedades actualizadas
