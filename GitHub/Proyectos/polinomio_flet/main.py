import flet as ft
from view.polynomial_view import PolynomialView
from controller.polynomial_controller import PolynomialController


def main(page: ft.Page):
    page.title = "Polinomio con Lista Enlazada"
    page.window_width = 600
    page.window_height = 600
    page.scroll = ft.ScrollMode.ADAPTIVE

    view = PolynomialView(on_add=lambda e: controller.handle_add(e),
                          on_eval=lambda e: controller.handle_eval(e))
    controller = PolynomialController(view)

    page.add(view.col)


if __name__ == "__main__":
    ft.app(target=main)
