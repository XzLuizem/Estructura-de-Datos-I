# -*- coding: utf-8 -*-
"""
Este módulo contiene la implementación del controlador para la aplicación de polinomios.
"""

# Se importa el modelo y la vista para que el controlador pueda interactuar con ellos.
from pol_model import PolynomialModel
from pol_view import PolynomialView

class PolynomialController:
    """
    Controlador para la aplicación de polinomios.
    Maneja la interacción entre el modelo y la vista.
    """

    def __init__(self, model: PolynomialModel):
        """
        Inicializa el controlador con una referencia al modelo.
        
        Args:
            model (PolynomialModel): La instancia del modelo de datos.
        """
        self.model = model
        self.view: PolynomialView | None = None

    def set_view(self, view: PolynomialView):
        """Guarda una referencia a la vista para poder actualizarla."""
        self.view = view

    def _execute_operation(self, operation, e):
        """
        Lógica central para ejecutar una operación (suma o resta).
        
        Args:
            operation (function): La función del modelo a ejecutar (add o subtract).
            e: El objeto de evento de Flet que contiene la referencia a la página.
        """
        if not self.view:
            return

        # 1. Obtener datos de la Vista
        poly1_str = self.view.get_poly1_str()
        poly2_str = self.view.get_poly2_str()

        # 2. Actualizar el Modelo
        self.model.set_polynomials(poly1_str, poly2_str)
        operation()  # Llama a model.add() o model.subtract()
        result = self.model.get_result_str()

        # 3. Actualizar la Vista
        self.view.update_result(result)
        e.page.update()  # Redibuja la interfaz de usuario

    def handle_add(self, e):
        """
        Maneja el evento del botón de sumar.
        Invoca la lógica de negocio para la suma.
        """
        self._execute_operation(self.model.add, e)

    def handle_subtract(self, e):
        """
        Maneja el evento del botón de restar.
        Invoca la lógica de negocio para la resta.
        """
        self._execute_operation(self.model.subtract, e)
