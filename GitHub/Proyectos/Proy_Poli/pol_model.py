# -*- coding: utf-8 -*-
"""
Este módulo contiene la implementación del modelo para la aplicación de polinomios.
"""

import re
from data_structures import LinkedList, Node, Stack, Queue, PolyNode # Import PolyNode

class Polynomial:
    """Implementación de un polinomio usando una lista enlazada."""

    def __init__(self):
        self.terms = LinkedList()

    def add_term(self, coefficient, degree):
        coefficient = float(coefficient)
        degree = int(degree)
        if coefficient == 0: return

        if self.terms.head is None or degree > self.terms.head.degree:
            self.terms.head = PolyNode(coefficient, degree, self.terms.head)
            return

        current = self.terms.head
        prev = None # Keep track of the previous node for removal
        while current and degree < current.degree: # Iterate until degree is less than or equal to current.degree
            prev = current
            current = current.next
        
        if current and degree == current.degree:
            current.coefficient += coefficient
            if current.coefficient == 0:
                # Remove the node if coefficient becomes zero
                if prev:
                    prev.next = current.next
                else:
                    self.terms.head = current.next
        else:
            # Insert new node
            new_node = PolyNode(coefficient, degree, current)
            if prev:
                prev.next = new_node
            else:
                self.terms.head = new_node

    def __add__(self, other):
        result = Polynomial()
        p1_curr = self.terms.head
        p2_curr = other.terms.head
        
        # We will build the new list by appending at the tail, which is faster.
        # To do that, we need a tail pointer.
        new_head = None
        new_tail = None

        while p1_curr or p2_curr:
            coeff = 0
            deg = 0

            if p1_curr and (not p2_curr or p1_curr.degree > p2_curr.degree):
                coeff = p1_curr.coefficient
                deg = p1_curr.degree
                p1_curr = p1_curr.next
            elif p2_curr and (not p1_curr or p2_curr.degree > p1_curr.degree):
                coeff = p2_curr.coefficient
                deg = p2_curr.degree
                p2_curr = p2_curr.next
            elif p1_curr and p2_curr: # Degrees are equal
                coeff = p1_curr.coefficient + p2_curr.coefficient
                deg = p1_curr.degree
                p1_curr = p1_curr.next
                p2_curr = p2_curr.next
            
            if coeff != 0:
                new_node = PolyNode(coeff, deg) # Corrected
                if new_head is None:
                    new_head = new_node
                    new_tail = new_node
                else:
                    new_tail.next = new_node
                    new_tail = new_node
        
        result.terms.head = new_head
        return result

    def __sub__(self, other):
        neg_other = Polynomial()
        current = other.terms.head
        while current:
            neg_other.add_term(-current.coefficient, current.degree)
            current = current.next
        return self + neg_other

    def __str__(self):
        if not self.terms.head:
            return "0"
        terms_list = []
        current = self.terms.head
        is_first = True
        while current:
            coeff, degree = current.coefficient, current.degree
            if coeff == 0:
                current = current.next
                continue
            sign = '' if is_first else (' + ' if coeff > 0 else ' - ')
            if is_first and coeff < 0: sign = '-'
            coeff_abs = abs(coeff)
            coeff_str = '' if coeff_abs == 1 and degree != 0 else str(round(coeff_abs, 2) if not float(coeff_abs).is_integer() else int(coeff_abs))
            if degree == 0: term_str = f"{coeff_str}"
            elif degree == 1: term_str = f"{coeff_str}x"
            else: term_str = f"{coeff_str}x^{degree}"
            terms_list.append(f"{sign}{term_str}")
            is_first = False
            current = current.next
        return "".join(terms_list).lstrip(" +")
    
    # Other methods like delete, search, sort are omitted for brevity but assumed to be here
    def delete_term(self, degree) -> bool:
        degree = int(degree)
        current = self.terms.head
        prev = None
        deleted = False
        while current and current.degree != degree:
            prev = current
            current = current.next
        if current:
            if prev:
                prev.next = current.next
            else:
                self.terms.head = current.next
            deleted = True
        return deleted

    def search_term(self, degree):
        degree = int(degree)
        current = self.terms.head
        while current:
            if current.degree == degree:
                return current.coefficient
            current = current.next
        return None

    def sort_terms(self, ascending=True):
        if not self.terms.head: return
        nodes = []
        current = self.terms.head
        while current:
            nodes.append(current)
            current = current.next
        nodes.sort(key=lambda node: node.degree, reverse=not ascending)
        self.terms.head = nodes[0]
        current = self.terms.head
        for node in nodes[1:]:
            current.next = node
            current = current.next
        current.next = None

    def clone(self):
        """Crea y devuelve una copia profunda de este polinomio."""
        cloned_poly = Polynomial()
        current = self.terms.head
        while current:
            cloned_poly.add_term(current.coefficient, current.degree)
            current = current.next
        return cloned_poly

class PolynomialModel:
    def __init__(self):
        self.poly1 = Polynomial()
        self.poly2 = Polynomial()
        self.result = Polynomial()
        self.history = Stack() # Stack will now store Polynomial objects
        self.operations_queue = Queue()
        self._initialize_queue()
        self.history.push(Polynomial()) # Push an empty polynomial as the initial state

    def _initialize_queue(self):
        pass # No initial enqueues

    def _parse_poly(self, poly_str: str) -> Polynomial:
        poly = Polynomial()
        poly_str = poly_str.strip().replace(" ", "")
        if not poly_str:
            return poly

        # Add a plus sign at the beginning if there is no sign
        if poly_str[0] not in ['+', '-']:
            poly_str = '+' + poly_str

        # Regex to find all terms
        term_pattern = re.compile(r'([+-][^+-]+)')
        terms = term_pattern.findall(poly_str)

        for term in terms:
            if not term:
                continue

            # Default values
            coeff = 1.0
            degree = 0

            if 'x' in term:
                parts = term.split('x')
                coeff_part = parts[0]

                if coeff_part == '+':
                    coeff = 1.0
                elif coeff_part == '-':
                    coeff = -1.0
                elif coeff_part:
                    coeff = float(coeff_part)

                if len(parts) > 1 and parts[1]:
                    if '^' in parts[1]:
                        degree = int(parts[1][1:])
                    else:
                        degree = 1
                else: # This case is for "x" with no exponent, so degree is 1
                    degree = 1
            else:
                coeff = float(term)
                degree = 0

            if coeff != 0:
                poly.add_term(coeff, degree)
        return poly

    def set_polynomials(self, poly1_str: str, poly2_str: str = None):
        self.poly1 = self._parse_poly(poly1_str)
        if poly2_str is not None:
            self.poly2 = self._parse_poly(poly2_str)

    def add_term_to_poly1(self, coeff, degree):
        self.poly1.add_term(coeff, degree)

    def add(self):
        self.result = self.poly1 + self.poly2

    def subtract(self):
        self.result = self.poly1 - self.poly2

    def undo(self):
        """Deshace la última operación restaurando el estado anterior del polinomio de resultado."""
        if not self.history.is_empty():
            self.history.pop() # Pop the current state
            if not self.history.is_empty():
                self.result = self.history.peek().clone() # Restore to the previous state
            else:
                self.result = Polynomial() # If stack is empty after pop, reset to empty polynomial

    def clear_history(self):
        print("clear_history in model called.")
        self.history = Stack()

    def get_result_str(self) -> str:
        return str(self.result)

    def get_history_list(self) -> list[str]:
        items = []
        current = self.history.head
        while current:
            # Assuming the stack stores Polynomial objects now
            items.append(str(current.value)) # Convert Polynomial object to string
            current = current.next
        return items

    def enqueue_operation(self, operation_type: str, *args):
        """Encola una operación para ser procesada posteriormente."""
        # Store operation type and its arguments
        self.operations_queue.enqueue((operation_type, args))

    def get_queue_list(self) -> list[str]:
        items = []
        current = self.operations_queue.head
        while current:
            op_type, op_args = current.value
            items.append(f"{op_type.capitalize()} {op_args}") # Display operation type and args
            current = current.next
        return items

    def process_queue(self) -> bool:
        """Procesa la siguiente operación en la cola y devuelve True si se procesó una."""
        if self.operations_queue.is_empty():
            return False

        operation_data = self.operations_queue.dequeue()
        if not operation_data:
            return False

        operation_type, args = operation_data
        
        # The controller is responsible for setting poly1 and poly2 before calling process_queue
        # So for 'add' and 'subtract', self.poly1 and self.poly2 are already updated from the view

        if operation_type == "add":
            self.add()
        elif operation_type == "subtract":
            self.subtract()
        elif operation_type == "add_term":
            coeff, degree = args
            self.result.add_term(coeff, degree)
        elif operation_type == "delete_term":
            degree = args[0]
            self.result.delete_term(degree)
        elif operation_type == "sort_asc":
            self.result.sort_terms(ascending=True)
        elif operation_type == "sort_desc":
            self.result.sort_terms(ascending=False)
        
        return True
