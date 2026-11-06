def subrutina():
    a = b
    print(a)
    return


a = 4
b = 3
subrutina()
print(a)

# En este caso la subrutina utiliza dos variables a y b que no se han definido como globales o no candidate_locales
# Dentro del bucle no se asigna ningún valor a la variable b.  Es por tanto una variable libre y el programa busca
# su valor en un nivel superior.  b toma dentro de la función el valor 4.
# a toma el valor 3 ya que se asigna ese valor mediante la orden a = b
# Escribimos el valor de a dentro de la función que es 3.
# Al terminar la función volvemos a escribir a y ahora toma el valor 4 ya que a no es una variable global
# y aunque su valor haya cambiado en la función, ese cambio no afecta a su valor fuera de ella.