from model.linked_polynomial import LinkedPolynomial


class PolynomialController:
    def __init__(self, view):
        self.view = view

    def handle_add(self, e):
        p1_str, p2_str, _ = self.view.get_inputs()
        p1 = LinkedPolynomial()
        p2 = LinkedPolynomial()
        p1.from_string(p1_str)
        p2.from_string(p2_str)
        p_sum = LinkedPolynomial.add(p1, p2)
        self.view.set_result(f"Suma: {p_sum.to_string()}")

    def handle_eval(self, e):
        p1_str, _, x_str = self.view.get_inputs()
        try:
            x = float(x_str)
            p1 = LinkedPolynomial()
            p1.from_string(p1_str)
            val = p1.evaluate(x)
            self.view.set_result(f"P1({x}) = {val}")
        except Exception as ex:
            self.view.set_result(f"Error: {ex}")
