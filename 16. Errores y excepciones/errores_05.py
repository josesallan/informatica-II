'''5. Partiremos de la siguiente lista:
elementos = [1, ‘pie’, -2]

Realiza una función llamada agregar_una_vez(lista, elemento) que reciba como
parámetros una lista y un elemento. La función debe añadir el elemento al final
de la lista con la condición de no repetir ningún elemento. Además, si este
elemento ya se encuentra en la lista se debe invocar un error de tipo ValueError
que debes capturar y mostrar este mensaje en su lugar: Error: Imposible
añadir elementos duplicados => [elemento].

Cuando tengas la función crea un programa que permita añadir elementos a la
lista de forma indefinida. Intenta añadir los siguientes valores a la lista: 10,
“pie”, "Hola" y luego muestra su contenido.

Sugerencia: Puedes utilizar la sintaxis "elemento in lista", si el elemento está en
la lista genera un valor True, si no lo está genera un valor False'''


# Definimos la función:
def agregar_una_vez(lista, elemento):
    # Gestionamos la situación en la cual el elemento que queremos añadir a la lista ya está en ella
    # Ten en cuenta que esto en sí, no es un error.  En una lista puede haber un valor más de una vez.
    # Por lo tanto cuando se intente añadir el elemento repetido, tenemos que detectar la situación.
    # Generar una execpción y actúar en consecuencia.
    try:
        if elemento in lista:
            # Si el valor ya está en la lista, lanzamos un error, por ejemplo del tipo ValueError
            raise ValueError
        else:
            # Si el valor todavía no está en la lista lo añadimos.
            lista.append(elemento)
    except ValueError:
        # Gestionamos la excepción.
        print("Error: Imposible añadir elementos duplicados => [" + str(elemento) + "]")


# Lista inicial
elementos = [1, 'pie', -2]

# Bucle infinito (salida al introducir la expresión "terminar")
while True:
    valor = input("Valor que quieres añadir a la lista (terminar para finalizar): ")
    if valor == "terminar":
        break
    agregar_una_vez(elementos, valor)
    print(elementos)
