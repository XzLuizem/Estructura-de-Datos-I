# -*- coding: utf-8 -*-

# --- Nodos y Lista para Polinomios ---

class PolyNode:
    """Nodo para un término de un polinomio."""
    def __init__(self, coefficient, degree, next_node=None):
        self.coefficient = coefficient
        self.degree = degree
        self.next = next_node

class LinkedList:
    """Lista enlazada para almacenar los términos de un polinomio."""
    def __init__(self):
        self.head = None

    def append(self, coefficient, degree):
        # Este método es simple y solo añade al final, 
        # la lógica de inserción ordenada está en Polynomial.add_term
        new_node = PolyNode(coefficient, degree)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

# --- Estructuras Genéricas (Pila y Cola) ---

class Node:
    """Nodo genérico para usar en Pila y Cola."""
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

class Stack:
    """Implementación de una Pila (Stack) para valores genéricos."""
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, value):
        self.head = Node(value, self.head)

    def pop(self):
        if self.is_empty():
            return None
        popped_value = self.head.value
        self.head = self.head.next
        return popped_value

    def peek(self):
        if self.is_empty():
            return None
        return self.head.value

class Queue:
    """Implementación de una Cola (Queue) para valores genéricos."""
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def enqueue(self, value):
        new_node = Node(value)
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node
        if self.head is None:
            self.head = self.tail

    def dequeue(self):
        if self.is_empty():
            return None
        dequeued_value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return dequeued_value

    def peek(self):
        if self.is_empty():
            return None
        return self.head.value
