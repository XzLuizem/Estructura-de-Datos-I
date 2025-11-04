"""
Este módulo es el punto de entrada principal para la aplicación de polinomios.
Configura la aplicación Flet, inicializa el modelo, la vista y el controlador (MVC),
y lanza la interfaz de usuario.
"""

import flet as ft

from po_model import PoModel
from po_controller import PoController


def main(page: ft.Page):
    """Función principal para inicializar la aplicación Flet."""
    page.title = "Ciclo de figuras en Flet"
    # Establece el título de la aplicación

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    # Establece la alineación vertical para el contenido de la página

    page.window.width = 750
    # Establece el ancho de la ventana para la aplicación

    page.window.height = 600
    # Establece la altura de la ventana para la aplicación

    # Inicializa el modelo del polinomio
    model = PoModel()

    # Inicializa el controlador de la aplicación
    controller = PoController(model, page)

    # Agrega el contenedor de la vista a la página
    page.add(controller.view.container)


if __name__ == "__main__":
    # Inicia la aplicación Flet llamando a la función main
    ft.app(target=main)