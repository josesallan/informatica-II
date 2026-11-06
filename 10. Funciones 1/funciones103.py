def subrutina():
    global a
    print(a)
    a = 21
    return


subrutina()
a = 20
print(a)

# En este caso también se produce un error en la subrutina.
# Se debe a que aunque a se ha definido como global, cuando llegamos al print(a)
# todavía no se ha asignado un valor a la variable a.