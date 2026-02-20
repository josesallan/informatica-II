def subrutina_1():
    a = 20
    print(a)
    return


def subrutina_2():
    global a
    a = 30
    print(a)
    return


a = 10
subrutina_1()
print(a)
subrutina_2()
print(a)

# En la primera función la variable es local por lo tanto la asignación a=20 sólo afecta a la variable interior
# Por ello los dos primeros valores escritos son:
# 20    Valor de la variable en la función
# 10    Valor inicial de la variable
# En la segunda función la variable a pasa a ser global, la modificación de su valor se mantiene y por lo tanto 
# se muestra
# 30
# 30