"""
Este módulo define la vista de la aplicación de polígonos usando Flet.
Es responsable de construir y mostrar la interfaz de usuario.
"""

import flet as ft
import math
from flet.canvas import Canvas, Circle, Path, Rect

class PoView:
    """Clase que representa la vista en la arquitectura MVC para la aplicación de polígonos."""

    def __init__(self, on_next, on_prev):
        """Inicializa la vista con los manejadores de eventos para las operaciones de siguiente y anterior."""
        self.on_next = on_next
        self.on_prev = on_prev

        self.title = ft.Text(
            "Ciclo de Figuras geométricas", size=25, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER
        )

        self.next_button = ft.ElevatedButton(
            text="Siguiente", on_click=self.on_next, icon=ft.Icons.NAVIGATE_NEXT, width=120, height=50
        )

        self.prev_button = ft.ElevatedButton(
            text="Anterior", on_click=self.on_prev, icon=ft.Icons.NAVIGATE_BEFORE, width=120, height=50
        )

        self.canvas = Canvas(width=400, height=200)

        main_controls_column = ft.Column(
            controls=[
                self.title,
                ft.Row(
                    [self.prev_button, self.canvas, self.next_button],
                    alignment=ft.MainAxisAlignment.CENTER, 
                    spacing=20
                ),
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=15,
            width=700,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

        self.container = ft.Container(
            content=main_controls_column, 
            expand=True,
            alignment=ft.alignment.center
        )

    def update_view(self, current_node):
        """Actualiza el lienzo con la figura y el color actuales."""
        self.canvas.shapes.clear()
        if not current_node:
            return

        figure = current_node.data
        x_center = 200
        y_center = 100
        paint = ft.Paint(color=figure.color, style=ft.PaintingStyle.FILL)

        if figure.shape == "circle":
            self.canvas.shapes.append(Circle(x_center, y_center, 40, paint))
        elif figure.shape == "triangle":
            self.canvas.shapes.append(
                Path(
                    [
                        Path.MoveTo(x_center, y_center - 40),
                        Path.LineTo(x_center - 40, y_center + 40),
                        Path.LineTo(x_center + 40, y_center + 40),
                        Path.Close(),
                    ],
                    paint=paint,
                )
            )
        elif figure.shape == "square":
            self.canvas.shapes.append(Rect(x_center - 40, y_center - 40, 80, 80, 5, paint=paint))
        
        #self.canvas.update()
