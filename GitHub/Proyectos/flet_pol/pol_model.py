# -*- coding: utf-8 -*-
"""
Este módulo contiene la implementación del modelo para la aplicación de polinomios.

Incluye:
- DynamicPolynomial: Un ADT para un polinomio de grado dinámico.
- PolynomialModel: El modelo de la aplicación que maneja la lógica de negocio.
"""

import collections
import re


class DynamicPolynomial:
    """Implementación dinámica de un polinomio."""

    def __init__(self):
        """Inicializa un polinomio dinámico vacío."""
        self._coefficients = collections.defaultdict(float)

    def set_coefficient(self, degree, coefficient):
        """Establece el coeficiente para un grado específico."""
        degree = int(degree)
        coefficient = float(coefficient)
        if coefficient != 0:
            self._coefficients[degree] = coefficient
        elif degree in self._coefficients:
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
        all_degrees = set(self._coefficients.keys()) | set(
            other._coefficients.keys())
        for degree in all_degrees:
            coeff1 = self.get_coefficient(degree)
            coeff2 = other.get_coefficient(degree)
            result.set_coefficient(degree, coeff1 + coeff2)
        return result

    def __sub__(self, other):
        """Resta dos polinomios dinámicos."""
        result = DynamicPolynomial()
        all_degrees = set(self._coefficients.keys()) | set(
            other._coefficients.keys())
        for degree in all_degrees:
            coeff1 = self.get_coefficient(degree)
            coeff2 = other.get_coefficient(degree)
            result.set_coefficient(degree, coeff1 - coeff2)
        return result

    def __str__(self):
        """Representación en cadena del polinomio."""
        if not self._coefficients:
            return "0"

        terms = []
        sorted_degrees = sorted(self._coefficients.keys(), reverse=True)

        for i, degree in enumerate(sorted_degrees):
            coeff = self._coefficients[degree]
            
            # Formato del coeficiente
            if coeff.is_integer():
                coeff_val = int(coeff)
            else:
                coeff_val = round(coeff, 2)

            # Signo
            sign = ""
            if i == 0:
                if coeff_val < 0:
                    sign = "-"
            else:
                sign = " - " if coeff_val < 0 else " + "
            
            coeff_abs = abs(coeff_val)

            # Término
            if degree == 0:
                terms.append(f"{sign}{coeff_abs}")
            else:
                coeff_str = ""
                if coeff_abs != 1:
                    coeff_str = str(coeff_abs)
                
                if degree == 1:
                    terms.append(f"{sign}{coeff_str}x")
                else:
                    terms.append(f"{sign}{coeff_str}x^{degree}")
        
        return "".join(terms).lstrip(" +")


class PolynomialModel:
    """
    Modelo de datos para la aplicación de polinomios.
    Maneja el estado y la lógica de negocio de los polinomios.
    """

    def __init__(self):
        """Inicializa el modelo con polinomios vacíos."""
        self.poly1 = DynamicPolynomial()
        self.poly2 = DynamicPolynomial()
        self.result = DynamicPolynomial()

    def _parse_poly(self, poly_str: str) -> DynamicPolynomial:
        """Analiza una cadena y la convierte en un objeto DynamicPolynomial."""
        poly = DynamicPolynomial()
        poly_str = poly_str.strip().replace(" ", "")
        if not poly_str:
            return poly

        # Asegura que la cadena comience con un signo para facilitar el análisis
        if poly_str[0] not in ['+', '-']:
            poly_str = '+' + poly_str

        # Regex para encontrar todos los términos (ej: +3x^2, -x, +5)
        term_pattern = re.compile(r'([+-](?:(?:\d*\.?\d*)?x(?:\^\d+)?|\d+\.?\d*))')
        terms = term_pattern.findall(poly_str)

        for term in terms:
            if 'x' in term:
                parts = term.split('x')
                coeff_part = parts[0]
                
                if coeff_part == '+':
                    coeff = 1.0
                elif coeff_part == '-':
                    coeff = -1.0
                else:
                    coeff = float(coeff_part)

                if '^' in parts[1]:
                    degree = int(parts[1][1:])
                else:
                    degree = 1
            else:
                coeff = float(term)
                degree = 0
            
            # Suma al coeficiente existente para manejar términos como '2x + 3x'
            existing_coeff = poly.get_coefficient(degree)
            poly.set_coefficient(degree, existing_coeff + coeff)
            
        return poly

    def set_polynomials(self, poly1_str: str, poly2_str: str):
        """Establece los dos polinomios a partir de sus representaciones en cadena."""
        self.poly1 = self._parse_poly(poly1_str)
        self.poly2 = self._parse_poly(poly2_str)

    def add(self):
        """Suma los dos polinomios y almacena el resultado."""
        self.result = self.poly1 + self.poly2

    def subtract(self):
        """Resta el segundo polinomio del primero y almacena el resultado."""
        self.result = self.poly1 - self.poly2

    def get_result_str(self) -> str:
        """Devuelve la representación en cadena del polinomio resultante."""
        return str(self.result)