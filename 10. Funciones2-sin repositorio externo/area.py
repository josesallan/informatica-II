# Módulo con funciones para calcular superficies
pi = 3.1415927
# cuadrado S = l*l


def cuadrado(lado):
    sup = lado ** 2
    return sup


# Rectangulo S = b*a
def rectangulo(b, a):
    sup = b * a
    return sup


# trapecio S = (B+b)*h/2
def trapecio(B, b, h):
    sup = (B + b) * h / 2
    return sup


# triángulo S = B*h/2
def triangulo(b, h):
    sup = b * h / 2
    return sup


# círculo S = pi*r2
def circulo(r):
    sup = pi * r ** 2
    return sup


# romboide S = D*d/2
def romboide(D, d):
    sup = D * d / 2
    return sup
