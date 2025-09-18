# -*- coding: utf-8 -*-
"""
Este módulo contiene la implementación de la vista para la aplicación de polinomios.
"""

import flet as ft

class PolynomialView:
    """
    Vista de la aplicación de polinomios.
    Construye y contiene los elementos de la interfaz de usuario (UI).
    """

    def __init__(self, on_add, on_subtract):
        """
        Inicializa la vista y sus componentes.
        
        Args:
            on_add (function): La función a llamar cuando se presiona el botón de sumar.
            on_subtract (function): La función a llamar cuando se presiona el botón de restar.
        """
        self.on_add = on_add
        self.on_subtract = on_subtract

        self.title = ft.Text(
            "Calculadora de Polinomios", 
            size=30, 
            weight=ft.FontWeight.BOLD,
            text_align=ft.TextAlign.CENTER
        )

        self.poly1_input = ft.TextField(
            label="Polinomio 1",
            hint_text="Ej: 3x^2 + 2x - 5",
            width=400,
            border_radius=10
        )

        self.poly2_input = ft.TextField(
            label="Polinomio 2",
            hint_text="Ej: x^2 - 1",
            width=400,
            border_radius=10
        )

        self.add_button = ft.ElevatedButton(
            text="Sumar",
            on_click=self.on_add,
            icon=ft.Icons.ADD,
            width=180,
            height=40
        )

        self.subtract_button = ft.ElevatedButton(
            text="Restar",
            on_click=self.on_subtract,
            icon=ft.Icons.REMOVE,
            width=180,
            height=40
        )

        self.result_title = ft.Text(
            "Resultado:",
            size=20,
            weight=ft.FontWeight.W_500
        )
        
        self.result_value = ft.Text(
            "",
            size=24,
            weight=ft.FontWeight.BOLD,
            selectable=True
        )

        # Contenedor principal de la vista
        self.column = ft.Column(
            controls=[
                self.title,
                self.poly1_input,
                self.poly2_input,
                ft.Row(
                    controls=[self.add_button, self.subtract_button],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=20
                ),
                ft.Divider(),
                self.result_title,
                self.result_value
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=25,
            width=500
        )

    def get_poly1_str(self) -> str:
        """Retorna el texto del campo de entrada del primer polinomio."""
        return self.poly1_input.value or ""

    def get_poly2_str(self) -> str:
        """Retorna el texto del campo de entrada del segundo polinomio."""
        return self.poly2_input.value or ""

    def update_result(self, result_str: str):
        """
        Actualiza el texto del resultado en la vista.
        
        Args:
            result_str (str): La cadena de texto del resultado a mostrar.
        """
        self.result_value.value = result_str
        # Es necesario llamar a update() en el control para que Flet redibuje
        self.result_value.update()
