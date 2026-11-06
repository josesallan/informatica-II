'''Partimos de la siguiente lista:'''
lista = ['gato', 'perro', 'ratón', 'pato', 'elefante']

# Solicitamos el índice de uno de los elementos de la lista y lo almacenamos en una variable
indice = int(input("Introduce el índice del elemento de la lista que quieres mostrar por pantalla: "))

# Vamos a mostrar el elemento de la lista correspondiente al índice que hemos almacenado en la variable indice
# Este proceso puede generar un error del tipo IndexError si el valor de la variable indice no se corresponde
# con el índice de alugno de los elementos de la lista

# En previsión de que eso pueda suceder incluiremos la orden print dentro de un bloque try
try:
    print(lista[indice])
# En caso de que el valor de indice no sea válido capturaremos la excepción generada por el bloque try
except IndexError:
    # En caso de que se produzca un error de este tipo mostaremos los siguientes mensajes.
    print("El índice se encuentra fuera del rango.")
    print("Debes utilizar un número mayor o igual que cero y menor que la longitud de la lista.")
    print("En este caso el valor tendrá que estar incluido entre 0 y " + str(len(lista)  - 1) + ".")
