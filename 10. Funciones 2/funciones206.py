import area

print('Selecciona una opción')
print('a) Superficie de un cuadrado')
print('b) Superficie de un rectángulo')
print('c) Superficie de un trapecio')
print('d) Superficie de un triángulo')
print('e) Superficie de un círculo')
print('f) Superficie de un romboide')
respuesta = input('?:')
while respuesta != 'a' and respuesta != 'b' and respuesta != 'c' and respuesta != 'd' and respuesta != 'e' and respuesta != 'f':
    respuesta = input('Opción incorrecta. Vuelve a intentarlo?:')
if respuesta == 'a':
    l = float(input('¿Longitud del lado?:'))
    superficie = area.cuadrado(l)
elif respuesta == 'b':
    b = float(input('¿Longitud de la base?:'))
    a = float(input('¿Longitud de la altura?:'))
    superficie = area.rectangulo(b, a)
elif respuesta == 'c':
    bMay = float(input('¿Longitud de la base mayor?:'))
    bMen = float(input('¿Longitud de la base menor?:'))
    a = float(input('¿Longitud de la altura?:'))
    superficie = area.trapecio(bMay, bMen, a)
elif respuesta == 'd':
    b = float(input('¿Longitud de la base?:'))
    a = float(input('¿Longitud de la altura?:'))
    superficie = area.triangulo(b, a)
elif respuesta == 'e':
    b = float(input('¿Longitud del radio?:'))
    superficie = area.circulo(b)
else:
    dMay = float(input('¿Longitud de la diagonal mayor?:'))
    dMen = float(input('¿Longitud de la diagonal menor?:'))
    superficie = area.romboide(dMay, dMen)
print('Superficie:', superficie)
