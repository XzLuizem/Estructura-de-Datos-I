import flet as ft
from model_flet import CounterModel
from view_flet import CounterView
from controller_flet import CounterController

def main(page: ft.Page):
    """
    Función principal que inicializa y corre la aplicación Flet con la arquitectura MVC.
    """
    # Configuración de la página
    page.title = "Contador con Flet (MVC)"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_width = 300
    page.window_height = 400

    # 1. Inicializar el Modelo y el Controlador
    model = CounterModel()
    controller = CounterController(model)
    
    # 2. Inicializar la Vista, pasándole el método del controlador
    view = CounterView(on_increment=controller.handle_increment)
    
    # 3. Darle al controlador una referencia a la vista
    controller.set_view(view)

    # 4. Añadir el control principal de la vista a la página
    page.add(view.column)
    page.update()

# Iniciar la aplicación Flet
if __name__ == "__main__":
    ft.app(target=main)
