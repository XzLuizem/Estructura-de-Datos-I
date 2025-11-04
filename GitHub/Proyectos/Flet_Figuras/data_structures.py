"""
Este módulo define las estructuras de datos utilizadas en la aplicación.
"""


class Node:
    """
    Representa un nodo en una lista enlazada.
    """

    def __init__(self, data, next_node=None, prev_node=None):
        """
        Inicializa un nuevo nodo.
        """
        self.data = data
        self.next = next_node
        self.prev = prev_node


class CircularLinkedList:
    """
    Implementa una lista circular doblemente enlazada.
    """

    def __init__(self):
        """
        Inicializa una lista circular vacía.
        """
        self.head = None

    def is_empty(self):
        """
        Verifica si la lista está vacía.
        """
        return self.head is None

    def insert(self, data):
        """
        Inserta un nuevo nodo en la lista.
        """
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head
        else:
            last = self.head.prev
            last.next = new_node
            new_node.prev = last
            new_node.next = self.head
            self.head.prev = new_node

    def get_nodes(self):
        """
        Retorna una lista con todos los nodos de la lista.
        """
        if self.is_empty():
            return []
        nodes = []
        current = self.head
        while True:
            nodes.append(current)
            current = current.next
            if current == self.head:
                break
        return nodes
