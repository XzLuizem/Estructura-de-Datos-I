# -*- coding: utf-8 -*-
"""
Este módulo contiene la implementación de la vista para la aplicación de conversión de infijo a prefijo.
"""

import flet as ft


class InfixToPrefixView:
    """
    Clase que define la Vista en el patrón Modelo-Vista-Controlador (MVC).
    Es responsable de construir y gestionar todos los elementos de la interfaz de usuario (UI)
    utilizando la biblioteca Flet.
    """

    def __init__(self, on_convert, on_convert_postfix):
        """
        Inicializa la vista y todos sus componentes de UI.

        Args:
            on_convert (function): El manejador de eventos del controlador para el botón de conversión a prefijo.
            on_convert_postfix (function): El manejador de eventos del controlador para el botón de conversión a postfijo.
        """
        self.on_convert = on_convert
        self.on_convert_postfix = on_convert_postfix

        # --- Definición de todos los Controles de la UI ---

        self.title = ft.Text("Conversor de Infijo", size=28,
                             weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER)

        self.expression_input = ft.TextField(
            label="Expresión Infija", hint_text="Ej: (A + B) * C", border_radius=10)

        self.convert_button = ft.ElevatedButton(
            text="Convertir a Prefijo", on_click=self.on_convert, icon=ft.Icons.SWAP_HORIZ, width=180, height=40)
        self.convert_to_postfix_button = ft.ElevatedButton(
            text="Convertir a Postfijo", on_click=self.on_convert_postfix, icon=ft.Icons.SWAP_HORIZ, width=180, height=40)

        self.result_title = ft.Text(
            "Resultado:", size=20, weight=ft.FontWeight.W_500)
        self.result_value = ft.Text(
            "", size=24, weight=ft.FontWeight.BOLD, selectable=True)
        self.user_message = ft.Text("", size=16, color=ft.Colors.GREEN_500)

        # --- Paneles para las Pilas (Izquierda y Derecha) ---
        self.terms_view = ft.ListView(
            expand=True, spacing=5, auto_scroll=True)
        self.operators_view = ft.ListView(
            expand=True, spacing=5, auto_scroll=True)

        terms_panel = ft.Column(
            controls=[
                ft.Text("Pila de Términos", size=20,
                        weight=ft.FontWeight.BOLD),
                ft.Divider(),
                self.terms_view,
            ],
            width=350,
            spacing=10
        )

        operators_panel = ft.Column(
            controls=[
                ft.Text("Pila de Operandos", size=20,
                        weight=ft.FontWeight.BOLD),
                ft.Divider(),
                self.operators_view,
            ],
            width=350,
            spacing=10
        )

        # --- Columna Principal de Controles (Centro) ---
        main_controls_column = ft.Column(
            controls=[
                self.title,
                self.expression_input,
                ft.Row(
                    controls=[
                        self.convert_button,
                        self.convert_to_postfix_button,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=10
                ),
                ft.Divider(),
                self.result_title,
                self.result_value,
                self.user_message,
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=15,
            width=400,
            scroll=ft.ScrollMode.AUTO
        )

        # --- Contenedor Principal (Fila) ---
        self.container = ft.Row(
            controls=[
                terms_panel,
                ft.VerticalDivider(),
                main_controls_column,
                ft.VerticalDivider(),
                operators_panel
            ],
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.START,
        )

    # --- Métodos para obtener datos de la UI ---

    def get_expression_str(self) -> str:
        return self.expression_input.value or ""

    # --- Métodos para actualizar la UI ---

    def update_result_title(self, title: str):
        """Actualiza el título del resultado."""
        self.result_title.value = title
        self.result_title.update()

    def update_result(self, result_str: str):
        """Actualiza el campo de texto del resultado."""
        self.result_value.value = result_str
        self.result_value.update()

    def update_message(self, message_str: str, color=ft.Colors.GREEN_500):
        """Muestra un mensaje informativo al usuario."""
        self.user_message.value = message_str
        self.user_message.color = color
        self.user_message.update()

    def update_stacks(self, terms: list[str], operators: list[str]):
        """Actualiza las vistas de las pilas de términos y operandos."""
        self.terms_view.controls.clear()
        for item in reversed(terms):
            self.terms_view.controls.append(ft.Text(item, selectable=True))

        self.operators_view.controls.clear()
        for item in reversed(operators):
            self.operators_view.controls.append(ft.Text(item, selectable=True))

        self.terms_view.update()
        self.operators_view.update()
