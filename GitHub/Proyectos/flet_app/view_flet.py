import flet as ft

class CounterView:
    """
    Vista de la aplicación de contador.
    Construye y contiene los elementos de la interfaz de usuario (UI).
    No hereda de UserControl para compatibilidad con versiones antiguas de Flet.
    """
    def __init__(self, on_increment):
        self.on_increment = on_increment

        self.txt_numero = ft.Text(
            value="0",
            text_align=ft.TextAlign.CENTER,
            size=50
        )

        self.btn_incrementar = ft.ElevatedButton(
            text="Incrementar",
            on_click=self.on_increment,
            width=150,
            height=50
        )
        
        # Este es el control principal que se añadirá a la página
        self.column = ft.Column(
            [self.txt_numero, self.btn_incrementar],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )

    def update_view(self, count):
        """Actualiza el texto del contador."""
        self.txt_numero.value = str(count)