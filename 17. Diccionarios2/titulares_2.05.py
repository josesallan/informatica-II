titulares = {
    1: {"posicion": "POR", "nombre": "Iker Casillas", "capitan": True},
    15: {"posicion": "DEF", "nombre": "Sergio Ramos"},
    3: {"posicion": "DEF", "nombre": "Gerard Piqué"},
    5: {"posicion": "DEF", "nombre": "Carles Puyol"},
    11: {"posicion": "DEF", "nombre": "Joan Capdevila"},
    14: {"posicion": "MED", "nombre": "Xabi Alonso"},
    16: {"posicion": "MED", "nombre": "Sergio Busquets"},
    8: {"posicion": "MED", "nombre": "Xavi Hernández"},
    18: {"posicion": "MED", "nombre": "Pedro Rodríguez"},
    6: {"posicion": "MED", "nombre": "Andrés Iniesta"},
    7: {"posicion": "DEL", "nombre": "David Villa"}
}

print("Nº -  Pos -      Nombre")
print("============================")
for posible_dorsal in range(100):
    resultado = titulares.get(posible_dorsal)
    if resultado is not None:
        len_dorsal = len(str(posible_dorsal))
        if len_dorsal == 1:
            print(" " + str(posible_dorsal), end="")
        else:
            print(posible_dorsal, end="")
        try:
            nada = resultado["capitan"]
            print(" - ",resultado["posicion"], "-> ", resultado["nombre"], "(C)")
        except KeyError:
            print(" - ",resultado["posicion"], "-> ", resultado["nombre"])

# (5)Creamos una copia de la biblioteca titulares y la llamamos plantilla.
plantilla = titulares.copy()
# Mostraremos ahora los elementos de la biblioteca con la misma forma que en el 2.
print()
print("Nº -  Pos -      Nombre")
print("============================")
for posible_dorsal in range(100):
    resultado = plantilla.get(posible_dorsal)
    if resultado is not None:
        len_dorsal = len(str(posible_dorsal))
        if len_dorsal == 1:
            print(" " + str(posible_dorsal), end="")
        else:
            print(posible_dorsal, end="")
        try:
            nada = resultado["capitan"]
            print(" - ",resultado["posicion"], "-> ", resultado["nombre"], "(C)")
        except KeyError:
            print(" - ",resultado["posicion"], "-> ", resultado["nombre"])