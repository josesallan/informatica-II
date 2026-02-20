# Definimos la clase Vector y sus características
class Vector():
    def __init__(self, ptipo, px, py):
        self.__tipo = ptipo
        self.x = px
        self.y = py

    def propiedades(self):
        print("Tipo de vector:", self.__tipo)
        print("Coordenada x:", self.x)
        print("Coordenada y:", self.y)

    def nuevo_tipo(self, ptipo):
        self.__tipo = ptipo

    # Método que calcula el módulo del vector y lo devuelve al código principal
    def modulo(self):
        longitud = (self.x ** 2 + self.y ** 2) ** (1 / 2)
        return longitud

    # Creamos un método que informa del tipo actual del vector
    def tipo_actual(self):
        return self.__tipo


# ------------------ Programa principal --------------------#
# Solicitamos por pantalla las propiedades del primer vector
print(' - Introduce los datos del primer vector:')
while True:
    tipo = input("  - Tipo de vector(p, v, a): ")
    if tipo in ['p', 'v', 'a']:
        break
    else:
        print(' Tipo incorrecto, vuelve a intentarlo')
x = float(input("  - Coordenada x: "))
y = float(input("  - Coordeanda y: "))

# Construimos un primer objeto de la clase Vector
miVector1 = Vector(tipo, x, y)

# Solicitamos por pantalla las propiedades del segundo vector
print(' - Introduce los datos del segundo vector:')
while True:
    tipo = input("  - Tipo de vector(p, v, a): ")
    if tipo in ['p', 'v', 'a']:
        break
    else:
        print(' Tipo incorrecto, vuelve a intentarlo')
x = float(input("  - Coordenada x: "))
y = float(input("  - Coordeanda y: "))

# Construimos un segundo objeto de la clase Vector
miVector2 = Vector(tipo, x, y)

# Comprobaremos si el tipo de los dos vectores es el mismo
#  - En caso de no serlo se ofrecerá la posibilidad de realizar el cambio
#       - Si se hace el cambio se realizará la suma
#       - Si no se hace el cambio el programa terminará

respuesta = 'S'  # Establezco por defecto el valor respuesta a 'S'
if miVector1.tipo_actual() != miVector2.tipo_actual():
    print(f' El primer vector es del tipo {miVector1.tipo_actual()} mientras que el segundo vector es del tipo {miVector2.tipo_actual()}.')
    print(' No es posible sumar dos vectores de dos tipos diferentes ')
    respuesta = input(f' ¿Quieres modificar el tipo del primer vector a tipo {miVector2.tipo_actual()}? (S/N)')

if respuesta == 'S':
    # Calculamos las dos componentes del vector suma
    x_suma = miVector1.x + miVector2.x
    y_suma = miVector1.y + miVector2.y

    # Creamos el vector suma
    miVector3 = Vector(miVector1.tipo_actual(), x_suma, y_suma)

    # Mostramos las propiedades y el módulo del vector suma
    miVector3.propiedades()
    print(f'Módulo del vector suma: {miVector3.modulo():.2f} unidades2')
else:
    print("No ha sido posible realizar la suma.  Programa terminado")
