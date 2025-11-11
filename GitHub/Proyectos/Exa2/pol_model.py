# -*- coding: utf-8 -*-
"""
Este módulo contiene la implementación del modelo para la aplicación de conversión de infijo a prefijo.
"""

from data_structures import Stack

class InfixToPrefixModel:
    """
    Clase que representa el modelo de la aplicación.
    Contiene la lógica de negocio para la conversión de expresiones infijas a prefijas.
    """

    def __init__(self):
        """Inicializa el modelo."""
        self.terms_stack = Stack()
        self.operators_stack = Stack()
        self.operator_history = []
        self.result = ""

    def _precedence(self, op):
        """Devuelve la precedencia de un operador."""
        if op == '+' or op == '-':
            return 1
        if op == '*' or op == '/':
            return 2
        if op == '^':
            return 3
        return 0

    def _tokenize(self, expression):
        """Divide la expresión en tokens (números, operadores, paréntesis)."""
        self.operator_history = []
        tokens = []
        i = 0
        while i < len(expression):
            if expression[i].isspace():
                i += 1
                continue
            elif expression[i].isdigit() or (expression[i] == '-' and (i == 0 or expression[i-1] in '(+-*/^')):
                num = expression[i]
                i += 1
                while i < len(expression) and expression[i].isdigit():
                    num += expression[i]
                    i += 1
                tokens.append(num)
            elif expression[i].isalpha():
                var = expression[i]
                i += 1
                while i < len(expression) and expression[i].isalnum():
                    var += expression[i]
                    i += 1
                tokens.append(var)
            else:
                tokens.append(expression[i])
                if expression[i] in "+-*/^":
                    self.operator_history.append(expression[i])
                i += 1
        return tokens

    def infix_to_prefix(self, expression):
        """
        Convierte una expresión infija a prefija.

        Args:
            expression (str): La expresión infija a convertir.

        Returns:
            str: La expresión prefija resultante.
        """
        self.terms_stack = Stack()
        self.operators_stack = Stack()

        tokens = self._tokenize(expression)
        reversed_tokens = tokens[::-1]

        processed_tokens = []
        for token in reversed_tokens:
            if token == '(':
                processed_tokens.append(')')
            elif token == ')':
                processed_tokens.append('(')
            else:
                processed_tokens.append(token)

        prefix = []
        for token in processed_tokens:
            if token.isalnum() or (token.startswith('-') and token[1:].isdigit()):
                prefix.append(token)
                self.terms_stack.push(token)
            elif token == '(':
                self.operators_stack.push(token)
            elif token == ')':
                while not self.operators_stack.is_empty() and self.operators_stack.peek() != '(':
                    prefix.append(self.operators_stack.pop())
                if not self.operators_stack.is_empty():
                    self.operators_stack.pop()
            else:
                while not self.operators_stack.is_empty() and self._precedence(self.operators_stack.peek()) > self._precedence(token):
                    prefix.append(self.operators_stack.pop())
                self.operators_stack.push(token)

        while not self.operators_stack.is_empty():
            prefix.append(self.operators_stack.pop())

        self.result = " ".join(prefix[::-1])
        evaluation_result = self.evaluate_prefix(self.result)
        return self.result, evaluation_result

    def infix_to_postfix(self, expression):
        """
        Convierte una expresión infija a postfija.

        Args:
            expression (str): La expresión infija a convertir.

        Returns:
            str: La expresión postfija resultante.
        """
        self.terms_stack = Stack()
        self.operators_stack = Stack()
        tokens = self._tokenize(expression)
        
        postfix = []
        for token in tokens:
            if token.isalnum() or (token.startswith('-') and token[1:].isdigit()):
                postfix.append(token)
                self.terms_stack.push(token)
            elif token == '(':
                self.operators_stack.push(token)
            elif token == ')':
                while not self.operators_stack.is_empty() and self.operators_stack.peek() != '(':
                    postfix.append(self.operators_stack.pop())
                if not self.operators_stack.is_empty():
                    self.operators_stack.pop()
            else:
                while not self.operators_stack.is_empty() and self._precedence(self.operators_stack.peek()) >= self._precedence(token):
                    postfix.append(self.operators_stack.pop())
                self.operators_stack.push(token)

        while not self.operators_stack.is_empty():
            postfix.append(self.operators_stack.pop())
            
        self.result = " ".join(postfix)
        evaluation_result = self.evaluate_postfix(self.result)
        return self.result, evaluation_result

    def evaluate_prefix(self, expression):
        """Evalúa una expresión prefija."""
        stack = Stack()
        tokens = expression.split()
        for token in reversed(tokens):
            if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
                stack.push(int(token))
            else:
                if stack.size() < 2:
                    return "Error: Expresión inválida"
                operand1 = stack.pop()
                operand2 = stack.pop()
                if token == '+':
                    stack.push(operand1 + operand2)
                elif token == '-':
                    stack.push(operand1 - operand2)
                elif token == '*':
                    stack.push(operand1 * operand2)
                elif token == '/':
                    if operand2 == 0:
                        return "Error: División por cero"
                    stack.push(operand1 / operand2)
        if stack.size() == 1:
            return stack.pop()
        return "Error: Expresión inválida"

    def evaluate_postfix(self, expression):
        """Evalúa una expresión postfija."""
        stack = Stack()
        tokens = expression.split()
        for token in tokens:
            if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
                stack.push(int(token))
            else:
                if stack.size() < 2:
                    return "Error: Expresión inválida"
                operand2 = stack.pop()
                operand1 = stack.pop()
                if token == '+':
                    stack.push(operand1 + operand2)
                elif token == '-':
                    stack.push(operand1 - operand2)
                elif token == '*':
                    stack.push(operand1 * operand2)
                elif token == '/':
                    if operand2 == 0:
                        return "Error: División por cero"
                    stack.push(operand1 / operand2)
        if stack.size() == 1:
            return stack.pop()
        return "Error: Expresión inválida"

    def get_terms_stack_as_list(self) -> list[str]:
        """Devuelve la pila de términos como una lista de cadenas."""
        items = []
        current = self.terms_stack.head
        while current:
            items.append(str(current.value))
            current = current.next
        return items

    def get_operators_stack_as_list(self) -> list[str]:
        """Devuelve el historial de operadores como una lista de cadenas."""
        return self.operator_history
