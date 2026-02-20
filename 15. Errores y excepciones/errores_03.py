# 3. (Necesario haber visto diccionarios). Partimos del siguiente diccionario:
colores = {'rojo': 'red', 'verde': 'green', 'negro': 'black'}

'''Crea un programa que solicite un término del diccionario para mostrar su valor
asociado por pantalla'''

# En primer lugar solicitamos la clave del elemento cuyo valor queremos mostrar
# En este caso es la palabra en español cuyo significado en inglés queremos mostar
valor = input("Introduce el nombre de un color en español: ")

# Gestionamos el posible error de que la clave introducida no esté en el diccionario.

# Intentamos mostrar el valor asociado a la clave
try:
    print(valor, "se dice", colores[valor], "en inglés")

# En caso de que la clave no esté se gestiona la excepción
except KeyError:
    print("Error: El término", valor, "no se encuentra en este diccionario, debes probar con otro que sí exista.")
