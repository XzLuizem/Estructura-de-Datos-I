# -*- coding: utf-8 -*-
"""
Este módulo contiene implementaciones básicas de ADT para polinomios.

Incluye: Polinomio (Dinámico)
Cada ADT incluye métodos para getters, setters,
y operaciones de polinomios, siguiendo PEP 8.
"""

import collections
# Implementación Dinámica de Polinomio


class DynamicPolynomial:
    """Implementación dinámica de un polinomio."""

    def __init__(self):
        """Inicializa un polinomio dinámico vacío."""
        # Usamos un diccionario para almacenar coeficientes, donde la clave es
        # el grado y el valor es el coeficiente.
        self._coefficients = collections.defaultdict(int)

    def set_coefficient(self, degree, coefficient):
        """Establece el coeficiente para un grado específico."""
        self._coefficients[degree] = coefficient
        # Limpiamos los coeficientes cero para mantener el diccionario limpio
        if self._coefficients[degree] == 0:
            del self._coefficients[degree]

    def get_coefficient(self, degree):
        """Retorna el coeficiente para un grado específico."""
        return self._coefficients.get(degree, 0)

    def get_degree(self):
        """Retorna el grado del polinomio."""
        return max(self._coefficients.keys()) if self._coefficients else 0

    def __add__(self, other):
        """Suma dos polinomios dinámicos."""
        result = DynamicPolynomial()
        # Suma coeficientes del primer polinomio
        for degree, coeff in self._coefficients.items():
            result.set_coefficient(degree, coeff)
        # Suma coeficientes del segundo polinomio
        for degree, coeff in other._coefficients.items():
            result.set_coefficient(
                degree, result.get_coefficient(degree) + coeff)
        return result

    def __sub__(self, other):
        """Resta dos polinomios dinámicos."""
        result = DynamicPolynomial()
        # Suma coeficientes del primer polinomio
        for degree, coeff in self._coefficients.items():
            result.set_coefficient(degree, coeff)
        # Resta coeficientes del segundo polinomio
        for degree, coeff in other._coefficients.items():
            result.set_coefficient(
                degree, result.get_coefficient(degree) - coeff)
        return result

    def __str__(self):
        """Representación en cadena del polinomio."""
        terms = []
        # Ordenamos los grados en orden descendente
        for degree in sorted(self._coefficients, reverse=True):
            coeff = self._coefficients[degree]
            if coeff != 0:
                if degree == 0:
                    terms.append(str(coeff))
                elif degree == 1:
                    terms.append(f"{coeff}x")
                else:
                    terms.append(f"{coeff}x^{degree}")
        return " + ".join(terms) if terms else "0"

# Ejemplos de uso:


# Polinomio Dinámico
print("\n--- Polinomio Dinámico ---")
poly1_dynamic = DynamicPolynomial()
poly1_dynamic.set_coefficient(2, 3)
poly1_dynamic.set_coefficient(0, 5)
print(f"Polinomio 1 dinámico: {poly1_dynamic}")

poly2_dynamic = DynamicPolynomial()
poly2_dynamic.set_coefficient(3, 2)
poly2_dynamic.set_coefficient(1, -1)
print(f"Polinomio 2 dinámico: {poly2_dynamic}")

poly_sum_dynamic = poly1_dynamic + poly2_dynamic
print(f"Suma de polinomios dinámicos: {poly_sum_dynamic}")

poly_sub_dynamic = poly1_dynamic - poly2_dynamic
print(f"Resta de polinomios dinámicos: {poly_sub_dynamic}")
