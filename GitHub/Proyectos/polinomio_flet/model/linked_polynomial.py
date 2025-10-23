from .term_node import TermNode


class LinkedPolynomial:
    def __init__(self):
        self.head = None

    def insert_term(self, coef, exp):
        if coef == 0:
            return
        if not self.head or self.head.exp < exp:
            self.head = TermNode(coef, exp, self.head)
        else:
            curr = self.head
            while curr.next and curr.next.exp > exp:
                curr = curr.next
            if curr.exp == exp:
                curr.coef += coef
                if curr.coef == 0:
                    # Eliminar nodo
                    if self.head == curr:
                        self.head = curr.next
                    else:
                        prev = self.head
                        while prev.next != curr:
                            prev = prev.next
                        prev.next = curr.next
            else:
                curr.next = TermNode(coef, exp, curr.next)

    def from_string(self, s):
        """Parsea '3x^2 - x + 5' → lista enlazada."""
        import re
        s = s.replace(" ", "")
        if not s:
            return
        if s[0] not in "+-":
            s = "+" + s
        tokens = re.findall(
            r"[+-](?:\d*\.?\d*)?x\^\d+|[+-](?:\d*\.?\d*)?x|[+-]\d+\.?\d*", s)
        for token in tokens:
            sign = -1 if token[0] == "-" else 1
            body = token[1:]
            if "x^" in body:
                coef_str, exp_str = body.split("x^")
                coef = float(coef_str) if coef_str and coef_str != "" else 1.0
                exp = int(exp_str)
            elif "x" in body:
                coef = float(body.replace("x", "")) if body.replace(
                    "x", "") else 1.0
                exp = 1
            else:
                coef = float(body) if body else 0.0
                exp = 0
            self.insert_term(sign * coef, exp)

    def evaluate(self, x):
        total = 0
        curr = self.head
        while curr:
            total += curr.coef * (x ** curr.exp)
            curr = curr.next
        return total

    @staticmethod
    def add(p1, p2):
        res = LinkedPolynomial()
        a, b = p1.head, p2.head
        while a and b:
            if a.exp > b.exp:
                res.insert_term(a.coef, a.exp)
                a = a.next
            elif b.exp > a.exp:
                res.insert_term(b.coef, b.exp)
                b = b.next
            else:
                res.insert_term(a.coef + b.coef, a.exp)
                a = a.next
                b = b.next
        while a:
            res.insert_term(a.coef, a.exp)
            a = a.next
        while b:
            res.insert_term(b.coef, b.exp)
            b = b.next
        return res

    def to_string(self):
        if not self.head:
            return "0"
        parts = []
        curr = self.head
        while curr:
            c, e = curr.coef, curr.exp
            if c.is_integer():
                c = int(c)
            sign = " + " if c >= 0 and parts else "" if c >= 0 else " - "
            c_abs = abs(c)
            if e == 0:
                term = f"{c_abs}"
            elif e == 1:
                term = f"{c_abs}x" if c_abs != 1 else "x"
            else:
                term = f"{c_abs}x^{e}" if c_abs != 1 else f"x^{e}"
            parts.append(sign + term)
            curr = curr.next
        return "".join(parts).lstrip(" +")
