def subrutina():
    print(a)
    a += 10
    return


a = 33
subrutina()
print(a)

# En este caso la variable no se declara como global en la función por lo tanto es una variable local
# y solo tiene sentido dentro de la subrutina.
# Inicialmente a vale 33
# Se llama a la función subrutina().  En ella la primera orden da un error ya que el print no puede
# mostrar el valor de a ya que todavía no se ha definido en el ámbito de la función (no le llega el
# valor 33 que es externo)