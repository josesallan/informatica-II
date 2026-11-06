# importamos la función pi del módulo math
from math import pi

# Definimos la clase Circulo y sus características
class Circulo():
    # El constructor recibe como parámetro el valor del radio
    # A modo de seguridad defino por defecto el valor del radio como 0.0
    def __init__(self, pradio=0.0):
        self.radio = pradio

    # Método que devuelve el valor de área del objeto de la clase Circulo
    def area(self):
        valor = pi * self.radio**2
        return valor

    # Método que devuelve el valor del perímetro del objeto de la clawse Circulo
    def perimetro(self):
        valor = 2 * pi * self.radio
        return valor


# ------------------ Programa principal --------------------#

# Creamos un objeto de la clase Circulo y mostramos su área y perímetro
radio = float(input("Radio del círculo: "))

miCirculo = Circulo(radio)

print(f"El círculo tiene una superficie de: {miCirculo.area():.2f}")
print(f'El círculo tiene un peímetro de: {miCirculo.perimetro():.2f}')