"""
Este módulo define el controlador de la aplicación.
Conecta la vista (`PoView`) con el modelo (`PoModel`) y maneja la lógica de la aplicación.
"""

import flet as ft

from po_view import PoView
from po_model import PoModel


class PoController:
    """Clase controladora para manejar la lógica de la aplicación y las interacciones."""

    def __init__(self, model: PoModel, page: ft.Page):
        """Inicializa el controlador con un modelo y una página Flet."""
        self.model = model
        self.page = page
        self.view = PoView(
            on_next=self.handle_next,
            on_prev=self.handle_prev,
        )
        self.update_view()

    def handle_next(self, e):
        """Maneja el evento del botón 'Siguiente'."""
        self.model.next_shape()
        self.update_view()

    def handle_prev(self, e):
        """Maneja el evento del botón 'Anterior'."""
        self.model.prev_shape()
        self.update_view()

    def update_view(self):
        """Actualiza la vista con los datos actuales del modelo."""
        current_node = self.model.current_node
        self.view.update_view(current_node)
        self.page.update()
