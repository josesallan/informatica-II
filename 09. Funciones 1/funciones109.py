def repite_hola(n, saludo):
    for i in range(0, n):
        print(saludo)
    return


veces = int(input('¿Cuántos saludos necesitas?'))
saludin = input('¿Qué saludo deseas mostrar?')
repite_hola(veces, saludin)
