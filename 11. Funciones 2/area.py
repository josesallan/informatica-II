"""
Módulo area.py
Contiene funciones para calcular la superficie de distintas figuras geométricas.
"""

import math  # Importamos la librería math para usar math.pi con precisión


def cuadrado(lado):
    """Calcula el área de un cuadrado."""
    return lado**2


def rectangulo(base, altura):
    """Calcula el área de un rectángulo."""
    return base * altura


def trapecio(base_mayor, base_menor, altura):
    """Calcula el área de un trapecio."""
    return ((base_mayor + base_menor) * altura) / 2


def triangulo(base, altura):
    """Calcula el área de un triángulo."""
    return (base * altura) / 2


def circulo(radio):
    """Calcula el área de un círculo."""
    return math.pi * (radio**2)


def romboide(base, altura):
    """Calcula el área de un romboide."""
    return base * altura
