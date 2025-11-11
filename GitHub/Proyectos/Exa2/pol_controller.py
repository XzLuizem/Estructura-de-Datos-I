# -*- coding: utf-8 -*-
"""
Este módulo contiene la implementación del controlador para la aplicación de conversión de infijo a prefijo.
"""
import flet as ft

from pol_model import InfixToPrefixModel
from pol_view import InfixToPrefixView

class InfixToPrefixController:
    """
    Controlador para la aplicación de conversión de infijo a prefijo.
    Maneja la lógica de la aplicación y la interacción entre el modelo (datos) y la vista (UI).
    """

    def __init__(self, model: InfixToPrefixModel, page: ft.Page):
        """
        Inicializa el controlador.

        Args:
            model (InfixToPrefixModel): La instancia del modelo de datos.
            page (ft.Page): La instancia de la página de Flet para la UI.
        """
        self.model = model
        self.page = page
        # Crea la instancia de la vista, pasando el manejador de eventos.
        self.view = InfixToPrefixView(
            on_convert=self.handle_convert,
            on_convert_postfix=self.handle_convert_postfix,
        )

    def handle_convert(self, e):
        """
        Manejador para la operación de conversión a prefijo.
        """
        expression = self.view.get_expression_str()
        if not expression:
            self.view.update_message("La expresión no puede estar vacía.", color=ft.Colors.RED)
            return

        try:
            prefix_expression, result = self.model.infix_to_prefix(expression)
            self.view.update_result_title("Prefijo =")
            self.view.update_result(f"{prefix_expression} = {result}")
            self.view.update_message("Conversión a prefijo exitosa.", color=ft.Colors.GREEN)
            
            terms = self.model.get_terms_stack_as_list()
            operators = self.model.get_operators_stack_as_list()
            self.view.update_stacks(terms, operators)

        except Exception as ex:
            self.view.update_message(f"Error: {ex}", color=ft.Colors.RED)

        self.page.update()

    def handle_convert_postfix(self, e):
        """
        Manejador para la operación de conversión a postfijo.
        """
        expression = self.view.get_expression_str()
        if not expression:
            self.view.update_message("La expresión no puede estar vacía.", color=ft.Colors.RED)
            return

        try:
            postfix_expression, result = self.model.infix_to_postfix(expression)
            self.view.update_result_title("Postfijo =")
            self.view.update_result(f"{postfix_expression} = {result}")
            self.view.update_message("Conversión a postfijo exitosa.", color=ft.Colors.GREEN)
            
            terms = self.model.get_terms_stack_as_list()
            operators = self.model.get_operators_stack_as_list()
            self.view.update_stacks(terms, operators)

        except Exception as ex:
            self.view.update_message(f"Error: {ex}", color=ft.Colors.RED)

        self.page.update()
