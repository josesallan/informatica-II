titulares = {}

# Añadimos cada uno de los jugadores.
# La información de cada uno de los jugadores estará almacenada en un diccionario independiente
# No es necesaro que los diccionarios de todos los jugadores tengan los mismos campos.
# Para acceder a los diferentes campos del diccionario de un jugador necesitaré conocer el nombre de las claves.

titulares[1] = {'posicion': 'POR', 'nombre': 'Iker Casillas', 'capitan': 'X'}
titulares[15] = {'posicion': 'DEF', 'nombre': 'Sergio Ramos'}
titulares[3] = {'posicion': 'DEF', 'nombre': 'Gerard Piqué'}
titulares[5] = {'posicion': 'DEF', 'nombre': 'Carles Puyo'}
titulares[11] = {'posicion': 'DEF', 'nombre': 'Joan Capdevila'}
titulares[14] = {'posicion': 'MED', 'nombre': 'Xabi Alonso'}
titulares[16] = {'posicion': 'MED', 'nombre': 'Sergio Busquets'}
titulares[8] = {'posicion': 'MED', 'nombre': 'Sergio Busquets'}
titulares[18] = {'posicion': 'MED', 'nombre': 'Pedro Rodríguez'}
titulares[6] = {'posicion': 'MED', 'nombre': 'Andrés Iniesta'}
titulares[7] = {'posicion': 'DEL', 'nombre': 'David Villa'}

# (5)Creamos una copia de la biblioteca titulares y la llamamos final.
final = titulares.copy()
# Eliminamos los tres jugadores sustituidos
final.pop(14)  # Xabi Alonso
final.pop(18)  # Pedrito
final.pop(7)  # Villa
# Añadimos los tres jugadores sustituidos
final.setdefault(22, {'posicion': 'MED', 'nombre': 'Jesús Navas'})
final.setdefault(10, {'posicion': 'MED', 'nombre': 'Cesc Fàbregas'})
final.setdefault(9, {'posicion': 'DEL', 'nombre': 'Fernando Torres'})

# Mostramos los resultados
print()
print('Final partido 2010')
print('------------------')
# Ejecutamos un bucle for que recorre todos los posibles índices (del 1 al 99)
for numero_camiseta in range(1, 99, 1):
    # Si no existe el índice termino la iteración actual
    if final.get(numero_camiseta, 'no') == 'no':
        continue
    # Si existe el índice lo muestro
    else:
        # Asigno a la variable datos_jugador el valor asociado en titulares al índice numero_camiseta
        datos_jugador = final[numero_camiseta]
        # Muestro el número del jugador actual y sus datos.
        if len(str(numero_camiseta)) == 1:
            print('  ' + str(numero_camiseta) + ' - ', end="")
        else:
            print(' ' + str(numero_camiseta) + ' - ', end="")
        print(datos_jugador['posicion'], '-> ', end="")
        print(datos_jugador['nombre'], end="")
        if datos_jugador.get('capitan', "no") == 'no':
            print()
        else:
            print(' (C)')
print("-")
