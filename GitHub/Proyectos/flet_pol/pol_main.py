# -*- coding: utf-8 -*-
"""
Este módulo es el punto de entrada principal para la aplicación de polinomios con Flet.
"""

import flet as ft
from pol_model import PolynomialModel
from pol_view import PolynomialView
from pol_controller import PolynomialController


def main(page: ft.Page):
    """
    Función principal que inicializa y corre la aplicación Flet con la arquitectura MVC.
    """
    # --- Configuración de la Página ---
    page.title = "Calculadora de Polinomios con Flet (MVC)"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_width = 550
    page.window_height = 600
    page.padding = ft.padding.all(30)
    page.theme_mode = ft.ThemeMode.LIGHT  # Opcional: LIGHT, DARK
    page.scroll = ft.ScrollMode.AUTO

    # --- Inicialización MVC ---

    # 1. Inicializar el Modelo
    # Contiene el estado y la lógica de negocio.
    model = PolynomialModel()

    # 2. Inicializar el Controlador
    # Maneja las interacciones y actualiza el modelo/vista.
    controller = PolynomialController(model)

    # 3. Inicializar la Vista
    # Construye la UI y le pasa los métodos del controlador como callbacks.
    view = PolynomialView(
        on_add=controller.handle_add,
        on_subtract=controller.handle_subtract
    )

    # 4. Conectar el Controlador con la Vista
    # El controlador necesita una referencia a la vista para poder actualizarla.
    controller.set_view(view)

    # --- Lanzamiento de la App ---

    # 5. Añadir el control principal de la vista a la página
    page.add(view.column)
    page.update()


# Iniciar la aplicación Flet
if __name__ == "__main__":
    ft.app(target=main)
