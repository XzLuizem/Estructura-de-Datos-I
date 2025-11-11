# -*- coding: utf-8 -*-

# --- Nodos y Lista para Polinomios ---

class PolyNode:
    """Representa un nodo en la lista enlazada de un polinomio.
    Cada nodo contiene un término del polinomio (coeficiente y grado).
    """
    def __init__(self, coefficient, signo, next_node=None):
        """Inicializa un nuevo nodo de polinomio.

        Args:
            coefficient (float): El coeficiente del término.
            signo (int): El grado del término.
            next_node (PolyNode, optional): El siguiente nodo en la lista. Defaults to None.
        """
        self.coefficient = coefficient
        self.signo = signo
        self.next = next_node

class LinkedList:
    """Implementación de una lista enlazada simple.
    Se utiliza como estructura base para la clase Polynomial.
    """
    def __init__(self):
        """Inicializa una lista enlazada vacía."""
        self.head = None

    def append(self, coefficient, signo):
        """Añade un nuevo término (nodo) al final de la lista.
        Nota: La lógica de inserción ordenada se maneja en Polynomial.add_term.
        """
        new_node = PolyNode(coefficient, signo)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

# --- Estructuras Genéricas (Pila y Cola) ---

class Node:
    """Nodo genérico para ser utilizado en la Pila (Stack) y la Cola (Queue)."""
    def __init__(self, value, next_node=None):
        """Inicializa un nuevo nodo genérico.

        Args:
            value: El valor a almacenar en el nodo.
            next_node (Node, optional): El siguiente nodo en la estructura. Defaults to None.
        """
        self.value = value
        self.next = next_node

class Stack:
    """Implementación de una Pila (Stack) utilizando una lista enlazada.
    LIFO (Last-In, First-Out).
    """
    def __init__(self):
        """Inicializa una pila vacía."""
        self.head = None

    def is_empty(self):
        """Comprueba si la pila está vacía."""
        return self.head is None

    def push(self, value):
        """Añade un elemento a la cima de la pila."""
        self.head = Node(value, self.head)

    def pop(self):
        """Elimina y devuelve el elemento en la cima de la pila."""
        if self.is_empty():
            return None
        popped_value = self.head.value
        self.head = self.head.next
        return popped_value

    def peek(self):
        """Devuelve el elemento en la cima de la pila sin eliminarlo."""
        if self.is_empty():
            return None
        return self.head.value

    def size(self):
        """Devuelve el número de elementos en la pila."""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
