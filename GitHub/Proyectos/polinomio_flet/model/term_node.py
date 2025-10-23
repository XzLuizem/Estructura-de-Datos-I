class TermNode:
    __slots__ = ('coef', 'exp', 'next')

    def __init__(self, coef, exp, next_node=None):
        self.coef = coef
        self.exp = exp
        self.next = next_node
