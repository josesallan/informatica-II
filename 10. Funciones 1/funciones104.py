def funcion():
    global a
    a = 10
    print(a)
    return


a = 33
funcion()
print(a)

# Los dos print muestran el valor 10 para a ya que aunque a inicialmente toma el valor
# 33. Al llamar a la función se le asigna el valor a antes del print()
# Ese valor se mantiene fuera de la función ya que a se ha definido como global
