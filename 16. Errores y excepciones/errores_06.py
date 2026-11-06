'''6. Escribe el código de una función que ha de ser capaz de aceptar números
enteros positivos. La función ha de chequear que el número introducido
cumple la condición dada. La función ha de ser capaz de gestionar los valores
que no sean enteros o que sean enteros negativos o si se introduce un texto o
si pulsamos “enter” sin haber introducido un valor, informando del error.'''


# La función comprobará si NO se cumplen las condiciones, desde la más extricta a la más suave:
def entero_positivo(valor):
    try:
        # En primer lugar detectamos si no se ha introducido ningún valor
        if valor == "":
            # En ese caso lanzamos un error cualquiera, en este caso AssertionError
            raise AssertionError
        else:
            # Comprobamos si el valor es un texto
            # Intentamos transformar el valor en un número decimal
            # Si el valor es un texto se generará un error tipo ValueError que detectaremos y procesaremos
            valorTratado = float(valor)
            # Si no se genera un error, ya sabremos que estamos tratando con un número.
            # Ahora detectaremos los casos en que sea negativo o decimal
            if valorTratado < 0:
                # Negativos
                raise BufferError
            if valorTratado != int(valorTratado):
                # Decimal
                raise TabError
        # Si hemos llegado hasta aquí, quiere decir que el número cumple las condiciones requeridas
        # por lo que lo devolvemos al código principal a través de un return
        return valor
    # En este bloque estamos gestionando cada una de las posible excepciones.
    except AssertionError:
        return "No has introducido ningún tipo de valor."
    except ValueError:
        return "El valor introducido es un texto"
    except BufferError:
        return "El valor introducido es menor que cero."
    except TabError:
        return "El número introducido es decimal."


posibleValor = input("Introduce un número entero positivo: ")
print(entero_positivo(posibleValor))
