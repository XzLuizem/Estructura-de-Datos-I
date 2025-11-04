# -*- coding: utf-8 -*-
"""
Este es el módulo principal que inicia la aplicación de la Calculadora de Polinomios.
Configura la ventana de la aplicación y ensambla los componentes del patrón MVC (Modelo-Vista-Controlador).
"""

import flet as ft
from pol_controller import PolynomialController
from pol_model import PolynomialModel

def main(page: ft.Page):
    """
    Función principal que se ejecuta cuando la aplicación Flet se inicia.

    Args:
        page (ft.Page): El objeto de página principal de la aplicación Flet.
    """
    # --- Configuración de la Página/Ventana ---
    page.title = "Calculadora de Polinomios"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.window.width = 1200
    page.window.height = 800

    # --- Inicialización del Patrón MVC ---
    
    # 1. Crear la instancia del Modelo, que contiene los datos y la lógica de negocio.
    model = PolynomialModel()
    
    # 2. Crear la instancia del Controlador, que actúa como intermediario.
    #    Se le pasa el modelo para que pueda manipular los datos y la página para interactuar con la UI.
    controller = PolynomialController(model, page)
    
    # 3. La Vista se crea dentro del Controlador. Aquí, añadimos el contenedor principal de la vista a la página.
    page.add(controller.view.container)

# --- Punto de Entrada de la Aplicación ---
if __name__ == "__main__":
    # Inicia la aplicación Flet, especificando la función 'main' como el punto de entrada.
    ft.app(target=main)