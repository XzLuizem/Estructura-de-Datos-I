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
    Maneja la interacción entre el modelo y la vista.
    """

    def __init__(self, model: PolynomialModel, page: ft.Page):
        self.model = model
        self.page = page # Store page object
        self.dont_show_clear_history_confirmation = self.page.client_storage.get("dont_show_clear_history_confirmation") or False
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
            on_confirm_clear_history=self._confirm_clear_history,
            on_cancel_clear_history=self._cancel_clear_history,
        )

    def update_data_views(self):
        """Actualiza las vistas de historial y cola."""
        self.view.update_history(self.model.get_history_list())
        self.view.update_queue(self.model.get_queue_list())

    def _get_result_poly(self):
        """Obtiene el polinomio del campo de resultado y lo establece en el modelo."""
        result_str = self.view.result_value.value or "0"
        self.model.result = self.model._parse_poly(result_str)

    def _update_views_with_new_result(self, e):
        """Actualiza la UI después de que el polinomio de resultado ha sido modificado y guarda el estado."""
        self.view.update_message("") # Clear any previous messages
        new_result_str = str(self.model.result)
        self.view.update_result(new_result_str)
        self.update_data_views()
        e.page.update()

    def handle_add(self, e):
        """Realiza la operación de suma directamente."""
        poly1_str = self.view.get_poly1_str()
        poly2_str = self.view.get_poly2_str()
        self.model.set_polynomials(poly1_str, poly2_str)
        self.model.add()
        self.model.history.push(self.model.result.clone())
        self._update_views_with_new_result(e)

    def handle_subtract(self, e):
        """Realiza la operación de resta directamente."""
        poly1_str = self.view.get_poly1_str()
        poly2_str = self.view.get_poly2_str()
        self.model.set_polynomials(poly1_str, poly2_str)
        self.model.subtract()
        self.model.history.push(self.model.result.clone())
        self._update_views_with_new_result(e)

    def handle_add_term(self, e):
        """Añade un término al polinomio de resultado."""
        coeff_str = self.view.get_coeff_str()
        degree_str = self.view.get_degree_term_str()
        if not coeff_str or not degree_str: return

        self._get_result_poly()
        self.model.result.add_term(coeff_str, degree_str)
        self.model.history.push(self.model.result.clone())
        self._update_views_with_new_result(e)

    def handle_delete(self, e):
        """Elimina un término del polinomio de resultado."""
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
        """Busca un término en el polinomio de resultado."""
        degree_str = self.view.get_degree_str()
        if not degree_str: return

        self._get_result_poly()
        coefficient = self.model.result.search_term(degree_str)

        if coefficient is not None:
            result_msg = f"Coeficiente del grado {degree_str}: {coefficient}"
            log_msg = f"Búsqueda: grado {degree_str} -> Coef: {coefficient}"
        else:
            result_msg = f"No se encontró el término con grado {degree_str}"
            log_msg = f"Búsqueda fallida: grado {degree_str}"
        
        # La búsqueda no actualiza el resultado, solo muestra un mensaje
        self.view.update_message(result_msg)
        self.update_data_views()
        e.page.update()

    def handle_sort_asc(self, e):
        """Ordena el polinomio de resultado ascendentemente."""
        self._get_result_poly()
        self.model.result.sort_terms(ascending=True)
        self.model.history.push(self.model.result.clone())
        self._update_views_with_new_result(e)

    def handle_sort_desc(self, e):
        """Ordena el polinomio de resultado descendentemente."""
        self._get_result_poly()
        self.model.result.sort_terms(ascending=False)
        self.model.history.push(self.model.result.clone())
        self._update_views_with_new_result(e)

    def handle_clear_history(self, e):
        """Maneja el evento de limpiar el historial directamente para depuración."""
        print(f"handle_clear_history called. (Direct clear for debugging)")
        self.view.update_message("") # Clear any previous messages
        self.model.clear_history()
        self.update_data_views()
        self.view.container.update() # Force update the main container
        e.page.update()

    def handle_undo(self, e):
        """Maneja la acción de deshacer la última operación."""
        self.model.undo()
        self._update_views_with_new_result(e)

    def handle_enqueue_add(self, e):
        """Encola la operación de suma."""
        poly1_str = self.view.get_poly1_str()
        poly2_str = self.view.get_poly2_str()
        self.model.enqueue_operation("add", poly1_str, poly2_str)
        self.update_data_views()
        e.page.update()

    def handle_enqueue_subtract(self, e):
        """Encola la operación de resta."""
        poly1_str = self.view.get_poly1_str()
        poly2_str = self.view.get_poly2_str()
        self.model.enqueue_operation("subtract", poly1_str, poly2_str)
        self.update_data_views()
        e.page.update()

    def handle_enqueue_add_term(self, e):
        """Encola la operación de añadir un término."""
        coeff_str = self.view.get_coeff_str()
        degree_str = self.view.get_degree_term_str()
        if not coeff_str or not degree_str: return
        self.model.enqueue_operation("add_term", coeff_str, degree_str)
        self.update_data_views()
        e.page.update()

    def handle_enqueue_delete_term(self, e):
        """Encola la operación de eliminar un término."""
        degree_str = self.view.get_degree_str()
        if not degree_str: return
        self.model.enqueue_operation("delete_term", degree_str)
        self.update_data_views()
        e.page.update()

    def handle_enqueue_sort_asc(self, e):
        """Encola la operación de ordenar ascendentemente."""
        self.model.enqueue_operation("sort_asc")
        self.update_data_views()
        e.page.update()

    def handle_enqueue_sort_desc(self, e):
        """Encola la operación de ordenar descendentemente."""
        self.model.enqueue_operation("sort_desc")
        self.update_data_views()
        e.page.update()

    def handle_process_queue(self, e):
        """Procesa la siguiente operación en la cola y actualiza la UI."""
        # Before processing, ensure the model has the latest poly1 and poly2 from the view
        poly1_str = self.view.get_poly1_str()
        poly2_str = self.view.get_poly2_str()
        self.model.set_polynomials(poly1_str, poly2_str)

        was_processed = self.model.process_queue()
        if was_processed:
            self.model.history.push(self.model.result.clone())
            self._update_views_with_new_result(e)

    def _confirm_clear_history(self, e):
        """Confirma y limpia el historial, guardando la preferencia de 'no volver a preguntar'."""
        e.page.dialog.open = False
        if self.view.dont_show_again_checkbox.value:
            e.page.client_storage.set("dont_show_clear_history_confirmation", True)
            self.dont_show_clear_history_confirmation = True # Update controller's internal state
        
        self.view.update_message("") # Clear any previous messages
        self.model.clear_history()
        self.update_data_views()
        self.view.container.update() # Force update the main container
        e.page.update()

    def _cancel_clear_history(self, e):
        """Cancela la operación de limpiar historial y cierra el diálogo."""
        e.page.dialog.open = False
        e.page.update()
