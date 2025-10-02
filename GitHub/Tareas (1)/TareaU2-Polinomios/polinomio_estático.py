# -*- coding: utf-8 -*-
"""
Este módulo contiene implementaciones básicas de ADT para polinomios.

Incluye: Polinomio (Estático)
Cada ADT incluye métodos para getters, setters,
y operaciones de polinomios, siguiendo PEP 8.
"""

import collections
# Implementación Estática de Polinomio


class StaticPolynomial:
    """Implementación estática de un polinomio."""

    def __init__(self, degree):
        """Inicializa un polinomio estático con un grado dado."""
        self._coefficients = [0] * (degree + 1)
        self._degree = degree

    def set_coefficient(self, degree, coefficient):
        """Establece el coeficiente para un grado específico."""
        if 0 <= degree <= self._degree:
            self._coefficients[degree] = coefficient
        else:
            raise ValueError("Grado fuera de rango")

    def get_coefficient(self, degree):
        """Retorna el coeficiente para un grado específico."""
        if 0 <= degree <= self._degree:
            return self._coefficients[degree]
        else:
            return 0

    def get_degree(self):
        """Retorna el grado del polinomio."""
        return self._degree

    def __add__(self, other):
        """Suma dos polinomios estáticos."""
        new_degree = max(self._degree, other.get_degree())
        result = StaticPolynomial(new_degree)
        for i in range(new_degree + 1):
            coeff1 = self.get_coefficient(i)
            coeff2 = other.get_coefficient(i)
            result.set_coefficient(i, coeff1 + coeff2)
        return result

    def __sub__(self, other):
        """Resta dos polinomios estáticos."""
        new_degree = max(self._degree, other.get_degree())
        result = StaticPolynomial(new_degree)
        for i in range(new_degree + 1):
            coeff1 = self.get_coefficient(i)
            coeff2 = other.get_coefficient(i)
            result.set_coefficient(i, coeff1 - coeff2)
        return result

    def __str__(self):
        """Representación en cadena del polinomio."""
        terms = []
        for i in range(self._degree, -1, -1):
            coeff = self._coefficients[i]
            if coeff != 0:
                if i == 0:
                    terms.append(str(coeff))
                elif i == 1:
                    terms.append(f"{coeff}x")
                else:
                    terms.append(f"{coeff}x^{i}")
        return " + ".join(terms) if terms else "0"

# Ejemplos de uso:


# Polinomio Estático
print("\n--- Polinomio Estático ---")
poly1_static = StaticPolynomial(2)
poly1_static.set_coefficient(2, 3)
poly1_static.set_coefficient(0, 5)
print(f"Polinomio 1 estático: {poly1_static}")

poly2_static = StaticPolynomial(3)
poly2_static.set_coefficient(3, 2)
poly2_static.set_coefficient(1, -1)
print(f"Polinomio 2 estático: {poly2_static}")

poly_sum_static = poly1_static + poly2_static
print(f"Suma de polinomios estáticos: {poly_sum_static}")

poly_sub_static = poly1_static - poly2_static
print(f"Resta de polinomios estáticos: {poly_sub_static}")
