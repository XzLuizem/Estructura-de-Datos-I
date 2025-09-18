class CounterController:
    """
    Controlador para la aplicación de contador.
    Maneja la interacción entre el modelo y la vista.
    """
    def __init__(self, model):
        self.model = model
        self.view = None

    def set_view(self, view):
        """Establece una referencia a la vista."""
        self.view = view

    def handle_increment(self, e):
        """
        Maneja el evento de clic del botón de incremento.
        Actualiza el modelo, la vista y la página.
        El objeto 'e' (evento) contiene una referencia a la página (e.page).
        """
        self.model.increment()
        new_count = self.model.get_count()
        if self.view:
            self.view.update_view(new_count)
        e.page.update() # Actualiza la UI