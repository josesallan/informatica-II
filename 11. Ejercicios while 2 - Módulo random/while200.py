# importamos el módulo random de la librería estándar
import random

# Creamos variables y listas que luego utilizaremos en los ejemplos
mensaje = 'Mensajedetextosinsentido'
lista = ['Juan', 'Carlos', 'Luis', 'Pedro', 'Susana', 'Luisa']
numero = 100
# Con números
print(random.randint(1, 10))
# Con variables enteras
print(random.randint(1, numero))
# Con cadenas de texto
print(random.choice(mensaje))
# Con listas
print(random.choice(lista))
# Barajeando listas
(random.shuffle(lista))
print(lista)
# Tomando muestras de cadenas de texto
print(random.sample(mensaje, 4))
# Tomando muestras de listas
print(random.sample(lista, 2))
