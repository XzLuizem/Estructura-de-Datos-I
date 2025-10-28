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

    def __init__(self, on_add, on_subtract, on_delete, on_search, on_sort_asc, on_sort_desc, on_add_term, on_clear_history, on_undo, on_enqueue_add, on_enqueue_subtract, on_enqueue_add_term, on_enqueue_delete_term, on_enqueue_sort_asc, on_enqueue_sort_desc, on_process_queue, on_confirm_clear_history, on_cancel_clear_history):
        """
        Inicializa la vista y sus componentes.
        """
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
        self.on_confirm_clear_history = on_confirm_clear_history
        self.on_cancel_clear_history = on_cancel_clear_history

        # --- Controles de la UI ---

        self.title = ft.Text("Calculadora de Polinomios", size=28, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER)

        self.poly1_input = ft.TextField(label="Polinomio 1", hint_text="Ej: 3x^2 + 2x - 5", border_radius=10)
        self.poly2_input = ft.TextField(label="Polinomio 2", hint_text="Ej: x^2 - 1", border_radius=10)

        self.add_button = ft.ElevatedButton(text="Sumar", on_click=self.on_add, icon=ft.Icons.ADD, width=180, height=40)
        self.subtract_button = ft.ElevatedButton(text="Restar", on_click=self.on_subtract, icon=ft.Icons.REMOVE, width=180, height=40)
        self.undo_button = ft.ElevatedButton(text="Deshacer", on_click=self.on_undo, icon=ft.Icons.UNDO, width=180, height=40)

        self.enqueue_add_button = ft.ElevatedButton(text="Encolar Sumar", on_click=self.on_enqueue_add, icon=ft.Icons.PLAYLIST_ADD, width=180, height=40)
        self.enqueue_subtract_button = ft.ElevatedButton(text="Encolar Restar", on_click=self.on_enqueue_subtract, icon=ft.Icons.PLAYLIST_REMOVE, width=180, height=40)

        self.coeff_input = ft.TextField(label="Coeficiente", width=120, border_radius=10)
        self.degree_input_term = ft.TextField(label="Grado", width=120, border_radius=10)
        self.add_term_button = ft.ElevatedButton(text="Añadir Término", on_click=self.on_add_term, icon=ft.Icons.PLUS_ONE, width=180, height=40)
        self.enqueue_add_term_button = ft.ElevatedButton(text="Encolar Añadir Término", on_click=self.on_enqueue_add_term, icon=ft.Icons.PLAYLIST_ADD, width=180, height=40)

        self.degree_input = ft.TextField(label="Grado", hint_text="Buscar/Eliminar", width=150, border_radius=10)
        self.delete_button = ft.ElevatedButton(text="Eliminar", on_click=self.on_delete, icon=ft.Icons.DELETE, width=150, height=40)
        self.enqueue_delete_term_button = ft.ElevatedButton(text="Encolar Eliminar", on_click=self.on_enqueue_delete_term, icon=ft.Icons.PLAYLIST_REMOVE, width=180, height=40)
        self.search_button = ft.ElevatedButton(text="Buscar", on_click=self.on_search, icon=ft.Icons.SEARCH, width=150, height=40)

        self.sort_asc_button = ft.ElevatedButton(text="Ordenar Asc", on_click=self.on_sort_asc, icon=ft.Icons.ARROW_UPWARD, width=180, height=40)
        self.sort_desc_button = ft.ElevatedButton(text="Ordenar Desc", on_click=self.on_sort_desc, icon=ft.Icons.ARROW_DOWNWARD, width=180, height=40)

        self.enqueue_sort_asc_button = ft.ElevatedButton(text="Encolar Ordenar Asc", on_click=self.on_enqueue_sort_asc, icon=ft.Icons.PLAYLIST_ADD, width=180, height=40)
        self.enqueue_sort_desc_button = ft.ElevatedButton(text="Encolar Ordenar Desc", on_click=self.on_enqueue_sort_desc, icon=ft.Icons.PLAYLIST_ADD, width=180, height=40)

        self.result_title = ft.Text("Resultado:", size=20, weight=ft.FontWeight.W_500)
        self.result_value = ft.Text("", size=24, weight=ft.FontWeight.BOLD, selectable=True)
        self.user_message = ft.Text("", size=16, color=ft.Colors.GREEN_500) # Control for user messages

        self.queue_view = ft.ListView(height=80, spacing=10)
        self.process_queue_button = ft.ElevatedButton(text="Procesar Cola", on_click=self.on_process_queue, icon=ft.Icons.PLAY_ARROW, width=180, height=40)

        # --- Confirmation Dialog for Clear History ---
        self.dont_show_again_checkbox = ft.Checkbox(label="No volver a preguntar", value=False)
        self.confirm_clear_history_dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("Confirmar Limpiar Historial"),
            content=ft.Column([
                ft.Text("¿Estás seguro de que quieres borrar todo el historial? Esta acción no se puede deshacer."),
                self.dont_show_again_checkbox
            ], tight=True),
            actions=[
                ft.TextButton("Sí", on_click=self.on_confirm_clear_history),
                ft.TextButton("No", on_click=self.on_cancel_clear_history),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        
        # --- Panel de Historial (Derecha) ---
        self.history_view = ft.ListView(expand=True, spacing=5, auto_scroll=True)
        self.clear_history_button = ft.IconButton(icon=ft.Icons.DELETE_FOREVER, on_click=self.on_clear_history, tooltip="Limpiar historial")

        history_panel = ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Text("Historial de Operaciones (Pila)", size=20, weight=ft.FontWeight.BOLD, expand=True),
                        self.clear_history_button,
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Divider(),
                self.history_view,
            ],
            width=350, # Set a fixed width for the history panel
            spacing=10
        )

        # --- Columna Principal de Controles (Izquierda) ---
        main_controls_column = ft.Column(
            controls=[
                self.title,
                self.poly1_input,
                self.poly2_input,
                ft.Row([self.add_button, self.subtract_button, self.undo_button], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
                ft.Row([self.enqueue_add_button, self.enqueue_subtract_button], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
                ft.Divider(),
                ft.Row([self.coeff_input, self.degree_input_term], alignment=ft.MainAxisAlignment.CENTER, spacing=10),
                ft.Row([self.add_term_button], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([self.enqueue_add_term_button], alignment=ft.MainAxisAlignment.CENTER),
                ft.Divider(),
                ft.Row([self.degree_input, self.search_button, self.delete_button, self.enqueue_delete_term_button], alignment=ft.MainAxisAlignment.CENTER, spacing=10),
                ft.Row([self.sort_asc_button, self.sort_desc_button], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
                ft.Row([self.enqueue_sort_asc_button, self.enqueue_sort_desc_button], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
                ft.Divider(),
                self.result_title,
                self.result_value,
                self.user_message, # Add the message control to the layout
                ft.Divider(),
                ft.Text("Cola de Operaciones:", size=16),
                self.queue_view,
                ft.Row([self.process_queue_button], alignment=ft.MainAxisAlignment.CENTER),
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=15,
            width=750,
            scroll=ft.ScrollMode.AUTO
        )

        # --- Contenedor Principal (Fila) ---
        self.container = ft.Row(
            controls=[
                main_controls_column,
                ft.VerticalDivider(),
                history_panel
            ],
            expand=True,
        )

    def get_poly1_str(self) -> str: return self.poly1_input.value or ""
    def get_poly2_str(self) -> str: return self.poly2_input.value or ""
    def get_degree_str(self) -> str: return self.degree_input.value or ""
    def get_coeff_str(self) -> str: return self.coeff_input.value or ""
    def get_degree_term_str(self) -> str: return self.degree_input_term.value or ""

    def update_result(self, result_str: str):
        self.result_value.value = result_str
        self.result_value.update()

    def update_message(self, message_str: str):
        """Muestra un mensaje al usuario."""
        self.user_message.value = message_str
        self.user_message.update()

    def update_history(self, history_items: list[str]):
        self.history_view.controls.clear()
        for item in reversed(history_items):
            self.history_view.controls.append(ft.Text(item, selectable=True))
        self.history_view.update()

    def update_queue(self, queue_items: list[str]):
        self.queue_view.controls.clear()
        for item in queue_items:
            self.queue_view.controls.append(ft.Text(item))
        self.queue_view.update()

    def show_clear_history_confirmation(self, page):
        print("show_clear_history_confirmation called.")
        page.dialog = self.confirm_clear_history_dialog
        self.confirm_clear_history_dialog.open = True
        page.update()
