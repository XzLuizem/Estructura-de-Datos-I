# -*- coding: utf-8 -*-
"""
Este módulo contiene la implementación del controlador para la aplicación de polinomios.
"""
import flet as ft

from pol_model import PolynomialModel
from pol_view import PolynomialView

class PolynomialController:
    """
    Controlador para la aplicación de polinomios.
    Maneja la lógica de la aplicación y la interacción entre el modelo (datos) y la vista (UI).
    """

    def __init__(self, model: PolynomialModel, page: ft.Page):
        """
        Inicializa el controlador.

        Args:
            model (PolynomialModel): La instancia del modelo de datos.
            page (ft.Page): La instancia de la página de Flet para la UI.
        """
        self.model = model
        self.page = page
        # Crea la instancia de la vista, pasando los manejadores de eventos (métodos de este controlador).
        self.view = PolynomialView(
            on_add=self.handle_add,
            on_subtract=self.handle_subtract,
            on_delete=self.handle_delete,
            on_search=self.handle_search,
            on_sort_asc=self.handle_sort_asc,
            on_sort_desc=self.handle_sort_desc,
            on_add_term=self.handle_add_term,
            on_clear_history=self.handle_clear_history,
            on_undo=self.handle_undo,
            on_enqueue_add=self.handle_enqueue_add,
            on_enqueue_subtract=self.handle_enqueue_subtract,
            on_enqueue_add_term=self.handle_enqueue_add_term,
            on_enqueue_delete_term=self.handle_enqueue_delete_term,
            on_enqueue_sort_asc=self.handle_enqueue_sort_asc,
            on_enqueue_sort_desc=self.handle_enqueue_sort_desc,
            on_process_queue=self.handle_process_queue,
        )

    def update_data_views(self):
        """Actualiza las vistas de datos (historial y cola) en la UI."""
        self.view.update_history(self.model.get_history_list())
        self.view.update_queue(self.model.get_queue_list())

    def _get_result_poly(self):
        """Obtiene el polinomio actual del campo de resultado de la vista y lo actualiza en el modelo."""
        result_str = self.view.result_value.value or "0"
        self.model.result = self.model._parse_poly(result_str)

    def _update_views_with_new_result(self, e):
        """Actualiza la UI con el nuevo resultado del modelo y guarda el estado en el historial."""
        self.view.update_message("") # Limpia mensajes anteriores.
        new_result_str = str(self.model.result)
        self.view.update_result(new_result_str)
        self.update_data_views()
        e.page.update() # Actualiza la página de Flet para reflejar los cambios.

    def handle_add(self, e):
        """Manejador para la operación de suma."""
        poly1_str = self.view.get_poly1_str()
        poly2_str = self.view.get_poly2_str()
        self.model.set_polynomials(poly1_str, poly2_str)
        self.model.add()
        self.model.history.push(self.model.result.clone()) # Guarda el resultado en el historial.
        self._update_views_with_new_result(e)

    def handle_subtract(self, e):
        """Manejador para la operación de resta."""
        poly1_str = self.view.get_poly1_str()
        poly2_str = self.view.get_poly2_str()
        self.model.set_polynomials(poly1_str, poly2_str)
        self.model.subtract()
        self.model.history.push(self.model.result.clone())
        self._update_views_with_new_result(e)

    def handle_add_term(self, e):
        """Manejador para añadir un término al polinomio de resultado."""
        coeff_str = self.view.get_coeff_str()
        degree_str = self.view.get_degree_term_str()
        if not coeff_str or not degree_str: return

        self._get_result_poly() # Obtiene el polinomio actual de la vista.
        self.model.result.add_term(coeff_str, degree_str)
        self.model.history.push(self.model.result.clone())
        self._update_views_with_new_result(e)

    def handle_delete(self, e):
        """Manejador para eliminar un término del polinomio de resultado."""
        degree_str = self.view.get_degree_str()
        if not degree_str: return

        self._get_result_poly()
        deleted = self.model.result.delete_term(degree_str)
        
        if deleted:
            self.model.history.push(self.model.result.clone())
            self._update_views_with_new_result(e)
        else:
            self.view.update_message(f"Término con grado {degree_str} no encontrado.")
            e.page.update()

    def handle_search(self, e):
        """Manejador para buscar un término en el polinomio de resultado."""
        degree_str = self.view.get_degree_str()
        if not degree_str: return

        self._get_result_poly()
        coefficient = self.model.result.search_term(degree_str)

        if coefficient is not None:
            result_msg = f"Coeficiente del grado {degree_str}: {coefficient}"
        else:
            result_msg = f"No se encontró el término con grado {degree_str}"
        
        # La búsqueda solo muestra un mensaje, no modifica el resultado.
        self.view.update_message(result_msg)
        self.update_data_views()
        e.page.update()

    def handle_sort_asc(self, e):
        """Manejador para ordenar el polinomio de resultado de forma ascendente."""
        self._get_result_poly()
        self.model.result.sort_terms(ascending=True)
        self.model.history.push(self.model.result.clone())
        self._update_views_with_new_result(e)

    def handle_sort_desc(self, e):
        """Manejador para ordenar el polinomio de resultado de forma descendente."""
        self._get_result_poly()
        self.model.result.sort_terms(ascending=False)
        self.model.history.push(self.model.result.clone())
        self._update_views_with_new_result(e)

    def handle_clear_history(self, e):
        """Manejador para limpiar el historial de operaciones."""
        self.view.update_message("")
        self.model.clear_history()
        self.update_data_views()
        self.view.container.update()
        e.page.update()

    def handle_undo(self, e):
        """Manejador para la acción de deshacer la última operación."""
        self.model.undo()
        self._update_views_with_new_result(e)

    # --- Manejadores para la Cola de Operaciones ---

    def handle_enqueue_add(self, e):
        """Encola una operación de suma."""
        poly1_str = self.view.get_poly1_str()
        poly2_str = self.view.get_poly2_str()
        self.model.enqueue_operation("add", poly1_str, poly2_str)
        self.update_data_views()
        e.page.update()

    def handle_enqueue_subtract(self, e):
        """Encola una operación de resta."""
        poly1_str = self.view.get_poly1_str()
        poly2_str = self.view.get_poly2_str()
        self.model.enqueue_operation("subtract", poly1_str, poly2_str)
        self.update_data_views()
        e.page.update()

    def handle_enqueue_add_term(self, e):
        """Encola una operación para añadir un término."""
        coeff_str = self.view.get_coeff_str()
        degree_str = self.view.get_degree_term_str()
        if not coeff_str or not degree_str: return
        self.model.enqueue_operation("add_term", coeff_str, degree_str)
        self.update_data_views()
        e.page.update()

    def handle_enqueue_delete_term(self, e):
        """Encola una operación para eliminar un término."""
        degree_str = self.view.get_degree_str()
        if not degree_str: return
        self.model.enqueue_operation("delete_term", degree_str)
        self.update_data_views()
        e.page.update()

    def handle_enqueue_sort_asc(self, e):
        """Encola una operación para ordenar ascendentemente."""
        self.model.enqueue_operation("sort_asc")
        self.update_data_views()
        e.page.update()

    def handle_enqueue_sort_desc(self, e):
        """Encola una operación para ordenar descendentemente."""
        self.model.enqueue_operation("sort_desc")
        self.update_data_views()
        e.page.update()

    def handle_process_queue(self, e):
        """Procesa la siguiente operación en la cola."""
        # Antes de procesar, se asegura que el modelo tenga los polinomios más recientes de la vista.
        poly1_str = self.view.get_poly1_str()
        poly2_str = self.view.get_poly2_str()
        self.model.set_polynomials(poly1_str, poly2_str)

        was_processed = self.model.process_queue()
        if was_processed:
            # Si se procesó una operación, se guarda el resultado y se actualiza la UI.
            self.model.history.push(self.model.result.clone())
            self._update_views_with_new_result(e)
