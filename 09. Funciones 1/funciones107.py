def subrutina():
    def sub_subrutina():
        a = 5
        print(a)
        return

    a = 4
    sub_subrutina()
    print(a)
    return

a = 3
subrutina()
print(a)

# El resultado mostrado en cada caso por la variable a es 5 4 y 3
# Las variables son locales en las funciones por lo que al salir de ellas se mantiene el valor asignado en el exterior
# Inicialmente se asigna a la a el valor 3 en el código principal
# Sin embargo el primer print que se ejecuta muestra el 5 pues está incluido dento de la sub_subrutina dentro de la cual
# se ha modificado el valor de a.
# Por la misma razón se muestra a continuación el valor 4. 
