# -*- coding: utf-8 -*-
"""
Este módulo contiene la implementación del modelo para la aplicación de polinomios.
"""

import re
from data_structures import LinkedList, Node, Stack, Queue, PolyNode # Import PolyNode

class Polynomial:
    """
    Clase que representa un polinomio.
    Utiliza una lista enlazada para almacenar los términos del polinomio.
    Cada nodo de la lista (PolyNode) contiene un coeficiente y un grado.
    """

    def __init__(self):
        """Inicializa un polinomio vacío."""
        self.terms = LinkedList()

    def add_term(self, coefficient, degree):
        """
        Añade un término al polinomio.
        Si ya existe un término con el mismo grado, suma los coeficientes.
        Si el coeficiente resultante es cero, elimina el término.
        Los términos se mantienen ordenados por grado de mayor a menor.

        Args:
            coefficient (float): El coeficiente del término.
            degree (int): El grado del término.
        """
        coefficient = float(coefficient)
        degree = int(degree)
        if coefficient == 0: return

        # Si la lista está vacía o el nuevo término tiene un grado mayor que el de la cabeza,
        # se inserta al principio.
        if self.terms.head is None or degree > self.terms.head.degree:
            self.terms.head = PolyNode(coefficient, degree, self.terms.head)
            return

        current = self.terms.head
        prev = None
        # Recorre la lista para encontrar la posición correcta para el nuevo término.
        while current and degree < current.degree:
            prev = current
            current = current.next
        
        # Si se encuentra un término con el mismo grado, se suman los coeficientes.
        if current and degree == current.degree:
            current.coefficient += coefficient
            # Si el coeficiente se vuelve cero, se elimina el nodo.
            if current.coefficient == 0:
                if prev:
                    prev.next = current.next
                else:
                    self.terms.head = current.next
        else:
            # Si no se encuentra un término con el mismo grado, se inserta un nuevo nodo.
            new_node = PolyNode(coefficient, degree, current)
            if prev:
                prev.next = new_node
            else:
                self.terms.head = new_node

    def __add__(self, other):
        """
        Suma dos polinomios.

        Args:
            other (Polynomial): El otro polinomio a sumar.

        Returns:
            Polynomial: Un nuevo polinomio que es la suma de los dos.
        """
        result = Polynomial()
        p1_curr = self.terms.head
        p2_curr = other.terms.head
        
        new_head = None
        new_tail = None

        # Itera sobre los términos de ambos polinomios.
        while p1_curr or p2_curr:
            coeff = 0
            deg = 0

            # Compara los grados de los términos actuales de cada polinomio.
            if p1_curr and (not p2_curr or p1_curr.degree > p2_curr.degree):
                coeff = p1_curr.coefficient
                deg = p1_curr.degree
                p1_curr = p1_curr.next
            elif p2_curr and (not p1_curr or p2_curr.degree > p1_curr.degree):
                coeff = p2_curr.coefficient
                deg = p2_curr.degree
                p2_curr = p2_curr.next
            elif p1_curr and p2_curr: # Si los grados son iguales
                coeff = p1_curr.coefficient + p2_curr.coefficient
                deg = p1_curr.degree
                p1_curr = p1_curr.next
                p2_curr = p2_curr.next
            
            # Añade el nuevo término al polinomio resultado si el coeficiente no es cero.
            if coeff != 0:
                new_node = PolyNode(coeff, deg)
                if new_head is None:
                    new_head = new_node
                    new_tail = new_node
                else:
                    new_tail.next = new_node
                    new_tail = new_node
        
        result.terms.head = new_head
        return result

    def __sub__(self, other):
        """
        Resta un polinomio de otro.
        Se implementa negando el segundo polinomio y sumándolo.

        Args:
            other (Polynomial): El polinomio a restar.

        Returns:
            Polynomial: Un nuevo polinomio que es la resta de los dos.
        """
        neg_other = Polynomial()
        current = other.terms.head
        while current:
            neg_other.add_term(-current.coefficient, current.degree)
            current = current.next
        return self + neg_other

    def __str__(self):
        """
        Devuelve una representación en cadena del polinomio.
        Formatea el polinomio de una manera legible, por ejemplo, "3x^2 + 2x - 5".

        Returns:
            str: La representación en cadena del polinomio.
        """
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
            
            # Determina el signo del término.
            sign = '' if is_first else (' + ' if coeff > 0 else ' - ')
            if is_first and coeff < 0: sign = '-'
            
            coeff_abs = abs(coeff)
            # Formatea el coeficiente.
            coeff_str = '' if coeff_abs == 1 and degree != 0 else str(round(coeff_abs, 2) if not float(coeff_abs).is_integer() else int(coeff_abs))
            
            # Formatea el término según el grado.
            if degree == 0: term_str = f"{coeff_str}"
            elif degree == 1: term_str = f"{coeff_str}x"
            else: term_str = f"{coeff_str}x^{degree}"
            
            terms_list.append(f"{sign}{term_str}")
            is_first = False
            current = current.next
        return "".join(terms_list).lstrip(" +")
    
    def delete_term(self, degree) -> bool:
        """
        Elimina un término del polinomio dado su grado.

        Args:
            degree (int): El grado del término a eliminar.

        Returns:
            bool: True si el término fue eliminado, False en caso contrario.
        """
        degree = int(degree)
        current = self.terms.head
        prev = None
        deleted = False
        # Busca el término con el grado especificado.
        while current and current.degree != degree:
            prev = current
            current = current.next
        # Si se encuentra, se elimina.
        if current:
            if prev:
                prev.next = current.next
            else:
                self.terms.head = current.next
            deleted = True
        return deleted

    def search_term(self, degree):
        """
        Busca un término en el polinomio por su grado.

        Args:
            degree (int): El grado del término a buscar.

        Returns:
            float or None: El coeficiente del término si se encuentra, de lo contrario None.
        """
        degree = int(degree)
        current = self.terms.head
        while current:
            if current.degree == degree:
                return current.coefficient
            current = current.next
        return None

    def sort_terms(self, ascending=True):
        """
        Ordena los términos del polinomio por grado.

        Args:
            ascending (bool): True para orden ascendente, False para descendente.
        """
        if not self.terms.head: return
        nodes = []
        current = self.terms.head
        # Extrae todos los nodos a una lista.
        while current:
            nodes.append(current)
            current = current.next
        # Ordena la lista de nodos.
        nodes.sort(key=lambda node: node.degree, reverse=not ascending)
        # Reconstruye la lista enlazada a partir de la lista ordenada.
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
    """
    Clase que representa el modelo de la aplicación.
    Contiene la lógica de negocio y el estado de la calculadora de polinomios.
    """
    def __init__(self):
        """Inicializa el modelo."""
        self.poly1 = Polynomial()  # Primer polinomio operando
        self.poly2 = Polynomial()  # Segundo polinomio operando
        self.result = Polynomial() # Polinomio resultado
        self.history = Stack()     # Pila para almacenar el historial de resultados (para la función de deshacer)
        self.operations_queue = Queue() # Cola para las operaciones en espera
        self._initialize_queue()
        # Se añade un polinomio vacío al historial como estado inicial.
        self.history.push(Polynomial())

    def _initialize_queue(self):
        """Inicializa la cola con operaciones predefinidas si es necesario."""
        pass # Actualmente no se encolan operaciones iniciales.

    def _parse_poly(self, poly_str: str) -> Polynomial:
        """
        Analiza una cadena de texto y la convierte en un objeto Polynomial.
        Utiliza expresiones regulares para identificar los términos.

        Args:
            poly_str (str): La cadena que representa el polinomio.

        Returns:
            Polynomial: El objeto Polynomial correspondiente.
        """
        poly = Polynomial()
        poly_str = poly_str.strip().replace(" ", "")
        if not poly_str:
            return poly

        # Añade un signo de más al principio si no hay signo, para facilitar el análisis.
        if poly_str[0] not in ['+', '-']:
            poly_str = '+' + poly_str

        # Expresión regular para encontrar todos los términos en la cadena.
        term_pattern = re.compile(r'([+-][^+-]+)')
        terms = term_pattern.findall(poly_str)

        for term in terms:
            if not term:
                continue

            # Valores por defecto para coeficiente y grado.
            coeff = 1.0
            degree = 0

            if 'x' in term:
                parts = term.split('x')
                coeff_part = parts[0]

                # Extrae el coeficiente.
                if coeff_part == '+':
                    coeff = 1.0
                elif coeff_part == '-':
                    coeff = -1.0
                elif coeff_part:
                    coeff = float(coeff_part)

                # Extrae el grado.
                if len(parts) > 1 and parts[1]:
                    if '^' in parts[1]:
                        degree = int(parts[1][1:])
                    else:
                        degree = 1
                else: # Caso para 'x' sin exponente explícito.
                    degree = 1
            else: # Término constante.
                coeff = float(term)
                degree = 0

            if coeff != 0:
                poly.add_term(coeff, degree)
        return poly

    def set_polynomials(self, poly1_str: str, poly2_str: str = None):
        """
        Establece los polinomios operandos a partir de sus representaciones en cadena.

        Args:
            poly1_str (str): Cadena del primer polinomio.
            poly2_str (str, optional): Cadena del segundo polinomio. Defaults to None.
        """
        self.poly1 = self._parse_poly(poly1_str)
        if poly2_str is not None:
            self.poly2 = self._parse_poly(poly2_str)

    def add_term_to_poly1(self, coeff, degree):
        """Añade un término al primer polinomio."""
        self.poly1.add_term(coeff, degree)

    def add(self):
        """Suma los dos polinomios operandos y guarda el resultado."""
        self.result = self.poly1 + self.poly2

    def subtract(self):
        """Resta el segundo polinomio del primero y guarda el resultado."""
        self.result = self.poly1 - self.poly2

    def undo(self):
        """
        Deshace la última operación.
        Restaura el polinomio de resultado al estado anterior guardado en el historial.
        """
        if not self.history.is_empty():
            self.history.pop() # Elimina el estado actual.
            if not self.history.is_empty():
                # Restaura al estado anterior (la cima de la pila).
                self.result = self.history.peek().clone()
            else:
                # Si la pila queda vacía, el resultado es un polinomio cero.
                self.result = Polynomial()

    def clear_history(self):
        """Limpia el historial de operaciones."""
        print("clear_history in model called.")
        self.history = Stack()

    def get_result_str(self) -> str:
        """Devuelve la representación en cadena del polinomio resultado."""
        return str(self.result)

    def get_history_list(self) -> list[str]:
        """
        Devuelve el historial de resultados como una lista de cadenas.

        Returns:
            list[str]: Una lista con la representación en cadena de cada polinomio en el historial.
        """
        items = []
        current = self.history.head
        while current:
            items.append(str(current.value))
            current = current.next
        return items

    def enqueue_operation(self, operation_type: str, *args):
        """
        Encola una operación para su procesamiento posterior.

        Args:
            operation_type (str): El tipo de operación (ej. 'add', 'subtract').
            *args: Los argumentos para la operación.
        """
        self.operations_queue.enqueue((operation_type, args))

    def get_queue_list(self) -> list[str]:
        """
        Devuelve la cola de operaciones como una lista de cadenas para visualización.

        Returns:
            list[str]: Lista de operaciones encoladas.
        """
        items = []
        current = self.operations_queue.head
        while current:
            op_type, op_args = current.value
            items.append(f"{op_type.capitalize()} {op_args}")
            current = current.next
        return items

    def process_queue(self) -> bool:
        """
        Procesa la siguiente operación en la cola.

        Returns:
            bool: True si una operación fue procesada, False si la cola estaba vacía.
        """
        if self.operations_queue.is_empty():
            return False

        operation_data = self.operations_queue.dequeue()
        if not operation_data:
            return False

        operation_type, args = operation_data
        
        # El controlador es responsable de establecer poly1 y poly2 desde la vista
        # antes de llamar a process_queue.

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
