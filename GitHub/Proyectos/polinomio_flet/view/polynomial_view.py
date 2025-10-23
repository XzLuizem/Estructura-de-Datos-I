import flet as ft


class PolynomialView:
    def __init__(self, on_add, on_eval):
        self.on_add = on_add
        self.on_eval = on_eval

        self.poly1 = ft.TextField(
            label="Polinomio 1", width=400, hint_text="Ej: 3x^2 - x + 5")
        self.poly2 = ft.TextField(
            label="Polinomio 2", width=400, hint_text="Ej: x^2 + 2")
        self.x_val = ft.TextField(label="Valor de x", width=150, value="2")
        self.result = ft.Text("", size=20, selectable=True)

        self.col = ft.Column(
            controls=[
                ft.Text("🧮 Polinomios con Lista Enlazada",
                        size=28, weight="bold"),
                self.poly1,
                self.poly2,
                ft.ElevatedButton("Sumar Polinomios",
                                  on_click=self.on_add, icon=ft.Icons.ADD),
                self.x_val,
                ft.ElevatedButton(
                    "Evaluar P1 en x", on_click=self.on_eval, icon=ft.Icons.CALCULATE),
                ft.Divider(),
                ft.Text("Resultado:", weight="bold"),
                self.result
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )

    def get_inputs(self):
        return self.poly1.value, self.poly2.value, self.x_val.value

    def set_result(self, text):
        self.result.value = text
        self.result.update()
