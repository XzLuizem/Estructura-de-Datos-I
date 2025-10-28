import flet as ft
from pol_controller import PolynomialController
from pol_model import PolynomialModel
from pol_view import PolynomialView

def main(page: ft.Page):
    page.title = "Calculadora de Polinomios"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.window_width = 1000
    page.window_height = 800

    model = PolynomialModel()
    controller = PolynomialController(model, page)

    page.add(controller.view.container)

if __name__ == "__main__":
    ft.app(target=main)