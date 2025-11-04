# -*- coding: utf-8 -*-
"""
Este módulo contiene la implementación de la vista para la aplicación de polinomios.
"""

import flet as ft


class PolynomialView:
    """
    Clase que define la Vista en el patrón Modelo-Vista-Controlador (MVC).
    Es responsable de construir y gestionar todos los elementos de la interfaz de usuario (UI)
    utilizando la biblioteca Flet.
    """

    def __init__(self, on_add, on_subtract, on_delete, on_search, on_sort_asc, on_sort_desc, on_add_term, on_clear_history, on_undo, on_enqueue_add, on_enqueue_subtract, on_enqueue_add_term, on_enqueue_delete_term, on_enqueue_sort_asc, on_enqueue_sort_desc, on_process_queue):
        """
        Inicializa la vista y todos sus componentes de UI.

        Args:
            Todos los parámetros 'on_*' son funciones (manejadores de eventos) del controlador
            que se asignan a los eventos 'on_click' de los botones correspondientes.
        """
        # Asignación de los manejadores de eventos del controlador a los atributos de la vista.
        self.on_add = on_add
        self.on_subtract = on_subtract
        self.on_delete = on_delete
        self.on_search = on_search
        self.on_sort_asc = on_sort_asc
        self.on_sort_desc = on_sort_desc
        self.on_add_term = on_add_term
        self.on_clear_history = on_clear_history
        self.on_undo = on_undo
        self.on_enqueue_add = on_enqueue_add
        self.on_enqueue_subtract = on_enqueue_subtract
        self.on_enqueue_add_term = on_enqueue_add_term
        self.on_enqueue_delete_term = on_enqueue_delete_term
        self.on_enqueue_sort_asc = on_enqueue_sort_asc
        self.on_enqueue_sort_desc = on_enqueue_sort_desc
        self.on_process_queue = on_process_queue

        # --- Definición de todos los Controles de la UI ---

        self.title = ft.Text("Calculadora de Polinomios", size=28,
                             weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER)

        # Campos de texto para la entrada de los dos polinomios.
        self.poly1_input = ft.TextField(
            label="Polinomio 1", hint_text="Ej: 3x^2 + 2x - 5", border_radius=10)
        self.poly2_input = ft.TextField(
            label="Polinomio 2", hint_text="Ej: x^2 - 1", border_radius=10)

        # Botones para operaciones directas.
        self.add_button = ft.ElevatedButton(
            text="Sumar", on_click=self.on_add, icon=ft.Icons.ADD, width=180, height=40)
        self.subtract_button = ft.ElevatedButton(
            text="Restar", on_click=self.on_subtract, icon=ft.Icons.REMOVE, width=180, height=40)
        self.undo_button = ft.ElevatedButton(
            text="Deshacer", on_click=self.on_undo, icon=ft.Icons.UNDO, width=180, height=40)

        # Botones para encolar operaciones básicas.
        self.enqueue_add_button = ft.ElevatedButton(
            text="Encolar Sumar", on_click=self.on_enqueue_add, icon=ft.Icons.PLAYLIST_ADD, width=180, height=40)
        self.enqueue_subtract_button = ft.ElevatedButton(
            text="Encolar Restar", on_click=self.on_enqueue_subtract, icon=ft.Icons.PLAYLIST_REMOVE, width=180, height=40)

        # Controles para añadir un término específico.
        self.coeff_input = ft.TextField(
            label="Coeficiente", width=120, border_radius=10)
        self.degree_input_term = ft.TextField(
            label="Grado", width=120, border_radius=10)
        self.add_term_button = ft.ElevatedButton(
            text="Añadir Término", on_click=self.on_add_term, icon=ft.Icons.PLUS_ONE, width=180, height=40)
        self.enqueue_add_term_button = ft.ElevatedButton(
            text="Encolar Añadir Término", on_click=self.on_enqueue_add_term, icon=ft.Icons.PLAYLIST_ADD, width=180, height=40)

        # Controles para buscar o eliminar un término por su grado.
        self.degree_input = ft.TextField(
            label="Grado", hint_text="Buscar/Eliminar", width=150, border_radius=10)
        self.delete_button = ft.ElevatedButton(
            text="Eliminar", on_click=self.on_delete, icon=ft.Icons.DELETE, width=150, height=40)
        self.enqueue_delete_term_button = ft.ElevatedButton(
            text="Encolar Eliminar", on_click=self.on_enqueue_delete_term, icon=ft.Icons.PLAYLIST_REMOVE, width=180, height=40)
        self.search_button = ft.ElevatedButton(
            text="Buscar", on_click=self.on_search, icon=ft.Icons.SEARCH, width=150, height=40)

        # Botones para ordenar el polinomio resultado.
        self.sort_asc_button = ft.ElevatedButton(
            text="Ordenar Asc", on_click=self.on_sort_asc, icon=ft.Icons.ARROW_UPWARD, width=180, height=40)
        self.sort_desc_button = ft.ElevatedButton(
            text="Ordenar Desc", on_click=self.on_sort_desc, icon=ft.Icons.ARROW_DOWNWARD, width=180, height=40)

        # Botones para encolar operaciones de ordenamiento.
        self.enqueue_sort_asc_button = ft.ElevatedButton(
            text="Encolar Ordenar Asc", on_click=self.on_enqueue_sort_asc, icon=ft.Icons.PLAYLIST_ADD, width=180, height=40)
        self.enqueue_sort_desc_button = ft.ElevatedButton(
            text="Encolar Ordenar Desc", on_click=self.on_enqueue_sort_desc, icon=ft.Icons.PLAYLIST_ADD, width=180, height=40)

        # Controles para mostrar el resultado y mensajes al usuario.
        self.result_title = ft.Text(
            "Resultado:", size=20, weight=ft.FontWeight.W_500)
        self.result_value = ft.Text(
            "", size=24, weight=ft.FontWeight.BOLD, selectable=True)
        self.user_message = ft.Text("", size=16, color=ft.Colors.GREEN_500)

        # Controles para la visualización y procesamiento de la cola de operaciones.
        self.queue_view = ft.ListView(height=80, spacing=10)
        self.process_queue_button = ft.ElevatedButton(
            text="Procesar Cola", on_click=self.on_process_queue, icon=ft.Icons.PLAY_ARROW, width=180, height=40)

        # --- Panel de Historial (Derecha) ---
        self.history_view = ft.ListView(
            expand=True, spacing=5, auto_scroll=True)
        self.clear_history_button = ft.IconButton(
            icon=ft.Icons.DELETE_FOREVER, on_click=self.on_clear_history, tooltip="Limpiar historial")

        # Estructura del panel de historial.
        history_panel = ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Text("Historial de Operaciones (Pila)", size=20,
                                weight=ft.FontWeight.BOLD, expand=True),
                        self.clear_history_button,
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Divider(),
                self.history_view,
            ],
            width=350,
            spacing=10
        )

        # --- Columna Principal de Controles (Izquierda) ---
        # Agrupa todos los controles principales en una columna vertical.
        main_controls_column = ft.Column(
            controls=[
                self.title,
                self.poly1_input,
                self.poly2_input,
                ft.Row([self.add_button, self.subtract_button, self.undo_button],
                       alignment=ft.MainAxisAlignment.CENTER, spacing=20),
                ft.Row([self.enqueue_add_button, self.enqueue_subtract_button],
                       alignment=ft.MainAxisAlignment.CENTER, spacing=20),
                ft.Divider(),
                ft.Row([self.coeff_input, self.degree_input_term],
                       alignment=ft.MainAxisAlignment.CENTER, spacing=10),
                ft.Row([self.add_term_button],
                       alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([self.enqueue_add_term_button],
                       alignment=ft.MainAxisAlignment.CENTER),
                ft.Divider(),
                ft.Row([self.degree_input, self.search_button, self.delete_button,
                       self.enqueue_delete_term_button], alignment=ft.MainAxisAlignment.CENTER, spacing=10),
                ft.Row([self.sort_asc_button, self.sort_desc_button],
                       alignment=ft.MainAxisAlignment.CENTER, spacing=20),
                ft.Row([self.enqueue_sort_asc_button, self.enqueue_sort_desc_button],
                       alignment=ft.MainAxisAlignment.CENTER, spacing=20),
                ft.Divider(),
                self.result_title,
                self.result_value,
                self.user_message,
                ft.Divider(),
                ft.Text("Cola de Operaciones:", size=16),
                self.queue_view,
                ft.Row([self.process_queue_button],
                       alignment=ft.MainAxisAlignment.CENTER),
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=15,
            width=750,
            scroll=ft.ScrollMode.AUTO
        )

        # --- Contenedor Principal (Fila) ---
        # Organiza la columna de controles y el panel de historial uno al lado del otro.
        self.container = ft.Row(
            controls=[
                main_controls_column,
                ft.VerticalDivider(),
                history_panel
            ],
            expand=True,
        )

    # --- Métodos para obtener datos de la UI ---

    def get_poly1_str(self) -> str: return self.poly1_input.value or ""
    def get_poly2_str(self) -> str: return self.poly2_input.value or ""
    def get_degree_str(self) -> str: return self.degree_input.value or ""
    def get_coeff_str(self) -> str: return self.coeff_input.value or ""

    def get_degree_term_str(
        self) -> str: return self.degree_input_term.value or ""

    # --- Métodos para actualizar la UI ---

    def update_result(self, result_str: str):
        """Actualiza el campo de texto del resultado."""
        self.result_value.value = result_str
        self.result_value.update()

    def update_message(self, message_str: str):
        """Muestra un mensaje informativo al usuario."""
        self.user_message.value = message_str
        self.user_message.update()

    def update_history(self, history_items: list[str]):
        """Actualiza la vista del historial con una lista de elementos."""
        self.history_view.controls.clear()
        # Muestra el historial en orden inverso (el más reciente arriba).
        for item in reversed(history_items):
            self.history_view.controls.append(ft.Text(item, selectable=True))
        self.history_view.update()

    def update_queue(self, queue_items: list[str]):
        """Actualiza la vista de la cola con una lista de operaciones."""
        self.queue_view.controls.clear()
        for item in queue_items:
            self.queue_view.controls.append(ft.Text(item))
        self.queue_view.update()
