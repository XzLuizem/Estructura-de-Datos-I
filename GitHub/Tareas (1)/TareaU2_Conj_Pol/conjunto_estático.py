# -*- coding: utf-8 -*-
"""
Este módulo contiene implementaciones básicas de ADT para conjuntos.

Incluye: Conjunto (Estático)
Cada ADT incluye métodos para getters, setters,
y operaciones de conjuntos, siguiendo PEP 8.
"""

import collections
# Implementación Estática de Conjunto


class StaticSet:
    """Implementación estática de un conjunto."""

    def __init__(self, capacity):
        """Inicializa un conjunto estático con una capacidad dada."""
        self._elements = [None] * capacity
        self._size = 0
        self._capacity = capacity

    def add(self, element):
        """Agrega un elemento al conjunto si no está presente y hay espacio."""
        if self._size < self._capacity and element not in self._elements:
            self._elements[self._size] = element
            self._size += 1
            return True
        return False

    def remove(self, element):
        """Elimina un elemento del conjunto si está presente."""
        if element in self._elements:
            index = self._elements.index(element)
            self._elements[index] = self._elements[self._size - 1]
            self._elements[self._size - 1] = None
            self._size -= 1
            return True
        return False

    def contains(self, element):
        """Verifica si un elemento está en el conjunto."""
        return element in self._elements[:self._size]

    def get_elements(self):
        """Retorna los elementos del conjunto."""
        return self._elements[:self._size]

    def get_size(self):
        """Retorna el tamaño actual del conjunto."""
        return self._size

    def get_capacity(self):
        """Retorna la capacidad del conjunto."""
        return self._capacity

    def set_capacity(self, capacity):
        """Establece la capacidad del conjunto. Nota: Esto no cambia el tamaño
        del array subyacente en esta implementación estática simple."""
        self._capacity = capacity

    def __str__(self):
        """Representación en cadena del conjunto."""
        return "{" + ", ".join(map(str, self.get_elements())) + "}"

# Ejemplos de uso:


# Conjunto Estático
print("--- Conjunto Estático ---")
static_set = StaticSet(5)
static_set.add(1)
static_set.add(2)
static_set.add(3)
print(f"Conjunto estático: {static_set}")
print(f"Tamaño: {static_set.get_size()}")
print(f"Contiene 2: {static_set.contains(2)}")
static_set.remove(2)
print(f"Conjunto estático después de eliminar 2: {static_set}")
print(f"Tamaño: {static_set.get_size()}")
