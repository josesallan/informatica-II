# Función que muestra los componentes de cualquiera de los diccionarios utilizados
# La función recibirá como parámetro el nombre del diccionario a mostrar
def mostrar_diccionario(diccionario):
    print(' Nº - Pos -  Nombre')
    print(' =============================')

    # Ejecutamos un bucle for que recorre todos los posibles índices (del 1 al 99)
    for numero_camiseta in range(1, 99, 1):
        # Si no existe el índice termino la iteración actual
        if diccionario.get(numero_camiseta, 'no') == 'no':
            continue
        # Si existe el índice lo muestro
        else:
            # Asigno a la variable datos_jugador el valor asociado en titulares al índice numero_camiseta
            datos_jugador = diccionario[numero_camiseta]
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
    print()


# Creamos el diccionario de los jugadores en el campo y añadimos los elementos
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

# (6)Creamos la biblioteca suplentes
suplentes = {}

suplentes[4] = {'posicion': 'DEF', 'nombre': 'Carlos Marchena'}
suplentes[9] = {'posicion': 'DEL', 'nombre': 'Fernando Torres'}
suplentes[10] = {'posicion': 'MED', 'nombre': 'Cesc Fàbregas'}
suplentes[12] = {'posicion': 'POR', 'nombre': 'Víctor Valdés'}
suplentes[13] = {'posicion': 'DEL', 'nombre': 'Juan Mata'}
suplentes[17] = {'posicion': 'DEF', 'nombre': 'Álvaro Arbeloa'}
suplentes[19] = {'posicion': 'DEL', 'nombre': 'Fernando Llorente'}
suplentes[20] = {'posicion': 'MED', 'nombre': 'Javi Martínez'}
suplentes[21] = {'posicion': 'MED', 'nombre': 'David Silva'}
suplentes[22] = {'posicion': 'DEL', 'nombre': 'Jesús Navas'}
suplentes[23] = {'posicion': 'POR', 'nombre': 'Pepe Reina'}

# Mostramos los dos listados por pantalla.
# Montamos una línea de cabecera para la tabla
print(' Jugadores en el terrano de juego')
mostrar_diccionario(titulares)


print()
# Montamos una línea de cabecera para la tabla
print(' Jugadores en el terrano de suplentes')
mostrar_diccionario(suplentes)


# ----------- Sección que gestiona los cambios -------------- #

# Inicializo una variable que indica el número del cambio que se está gestioando
cambio = 1

# Con un bucle while controlamos el número de cambios (podemos hacer hasta tres cambios)
while cambio <= 3:
    # Preguntamos por el nombre del jugador a sustituir
    sale = int(input(' - Introduce el número del jugador que quieres sustituir:'))
    # Debemos leer el nombre del jugador sustituido
    # Si el número no existe no lo podemos sustituir
    nombresale = titulares.get(sale, 'No')
    if nombresale == 'No':
        # Si el número del jugador es incorrecto terminamos la iteración
        print(' * Número incorrecto - Cambio cancelado')
        continue
    else:
        print(' - Jugador a susituir:', nombresale['nombre'], '\tnúmero:', sale)
    # Preguntamos por el nombre del jugador que va a entrar al campo
    entra = int(input(' - Introduce el número del jugador que va a entrar:'))
    # Debemos leer el nombre del jugador a introducir
    # Si el número no existe no lo podemos sustituir
    nombreentra = suplentes.get(entra, 'No')
    if nombreentra == 'No':
        # Si el número del jugador es incorrecto terminamos la iteración
        print(' * Número incorrecto - Cambio cancelado')
        continue
    else:
        print(' - Jugador a susituir:', nombresale['nombre'], '\tnúmero:', sale)
        print(' - Jugador que entra en su lugar:', nombreentra['nombre'], '\tnúmero:', entra)
        # Es en este momento cuando puedo realizar la sustitución
        ###########################################################################
        # Elimino al jugador sustituido del diccionario titulares
        titulares.pop(sale)

        # Elimino al jugador que entra del diccionario suplentes
        suplentes.pop(entra)

        # Añado el jugador que entra al diccionario titulares
        titulares.setdefault(entra, nombreentra)

        # Añado el jugador que sale al diccionario suplentes
        suplentes.setdefault(sale, nombresale)
        # Muestro los resultados actualizados
        # Mostramos los resultados
        print()
        # Mostramos los dos listados por pantalla.
    # Montamos una línea de cabecera para la tabla
    print(' Jugadores en el terrano de juego')

    mostrar_diccionario(titulares)
    print()
    # Montamos una línea de cabecera para la tabla
    print(' Jugadores en el terrano de suplentes')
    mostrar_diccionario(suplentes)

    # Incrementamos el resultado de la variable cambio
    cambio = cambio + 1
print('Ya has realizado las tres sustituciones')
