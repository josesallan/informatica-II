def subrutina():
    global a
    print(a)
    a += 10
    return


a = 33
subrutina()
print(a)

# Inicialmente la variable a toma el valor 33
# Se llama a la función subrutina()
# La función considera a como una variable global y la lee del código principal
# a vale 33 dentro de la función
# La función escribe su valor
# En la función se incrementa el valor de a en 10, pasa a ser 43
# Al terminar la rutina la orden print escribe otra vez 43 ya que a ha sido
# considerada como variable global en la rutina y se ha modificado su valor.
