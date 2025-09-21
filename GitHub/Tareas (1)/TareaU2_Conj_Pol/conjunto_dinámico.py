# -*- coding: utf-8 -*-
"""
Este módulo contiene implementaciones básicas de ADT para conjuntos.

Incluye: Conjunto (Dinámico)
Cada ADT incluye métodos para getters, setters,
y operaciones de conjuntos, siguiendo PEP 8.
"""

import collections
# Implementación Dinámica de Conjunto


class DynamicSet:
    """Implementación dinámica de un conjunto."""

    def __init__(self):
        """Inicializa un conjunto dinámico vacío."""
        self._elements = []

    def add(self, element):
        """Agrega un elemento al conjunto si no está presente."""
        if element not in self._elements:
            self._elements.append(element)
            return True
        return False

    def remove(self, element):
        """Elimina un elemento del conjunto si está presente."""
        if element in self._elements:
            self._elements.remove(element)
            return True
        return False

    def contains(self, element):
        """Verifica si un elemento está en el conjunto."""
        return element in self._elements

    def get_elements(self):
        """Retorna los elementos del conjunto."""
        return self._elements

    def get_size(self):
        """Retorna el tamaño actual del conjunto."""
        return len(self._elements)

    def __str__(self):
        """Representación en cadena del conjunto."""
        return "{" + ", ".join(map(str, self.get_elements())) + "}"

# Ejemplos de uso:


# Conjunto Dinámico
print("\n--- Conjunto Dinámico ---")
dynamic_set = DynamicSet()
dynamic_set.add("a")
dynamic_set.add("b")
dynamic_set.add("c")
print(f"Conjunto dinámico: {dynamic_set}")
print(f"Tamaño: {dynamic_set.get_size()}")
print(f"Contiene 'b': {dynamic_set.contains('b')}")
dynamic_set.remove("b")
print(f"Conjunto dinámico después de eliminar 'b': {dynamic_set}")
print(f"Tamaño: {dynamic_set.get_size()}")
