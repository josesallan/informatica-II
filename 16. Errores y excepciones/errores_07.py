'''7. Mejora el programa anterior consiguiendo que en caso de excepción la función
solicite un nuevo valor hasta que este tenga el formato correcto.'''

''' El código es igual al de ejercicio anterior con la diferencia de que el bloque try está dentro
de un while True, del cual solamente se puede salir a través del break que se ejecuta una vez
que hemos devuelto al valor al código principal'''


def entero_positivo(valor):
    while True:
        try:
            # En primer lugar detectamos si no se ha introducido ningún valor
            if valor == "":
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
            return valor
            break
        except AssertionError:
            return "No has introducido ningún tipo de valor."
        except ValueError:
            return "El valor introducido es un texto"
        except BufferError:
            return "El valor introducido es menor que cero."
        except TabError:
            return "El número introducido es decimal."
        # En caso de que se haya producido una excepción, tras gestionarla, solicitamos un valor correcto.
        valor = input("Introduce un número entero positivo: ")


# Código principal
posibleValor = input("Introduce un número entero positivo: ")
entero_positivo(posibleValor)
