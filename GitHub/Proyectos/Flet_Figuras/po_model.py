from data_structures import CircularLinkedList
from dataclasses import dataclass

@dataclass
class Figure:
    shape: str
    color: str

class ColorManager:
    """Maneja el mapeo cíclico de colores."""
    def __init__(self, colors):
        self.colors = colors
        self.num_colors = len(colors)

    def get_color(self, index, loop_count):
        """Devuelve el color para una figura dada la posición y el número de ciclos."""
        return self.colors[(index + loop_count) % self.num_colors]

class PoModel:
    """Clase que representa el modelo en la arquitectura MVC."""
    def __init__(self):
        self.figures = CircularLinkedList()
        self.colors = ["red", "green", "blue"]
        self.color_manager = ColorManager(self.colors)
        self.shapes = ["circle", "triangle", "square"]
        self.loop_count = 0
        self._initialize_figures()
        self.current_node = self.figures.head

    def _initialize_figures(self):
        """Inicializa las figuras con sus formas y colores iniciales."""
        for i in range(len(self.shapes)):
            figure = Figure(shape=self.shapes[i], color=self.colors[i])
            self.figures.insert(figure)

    def _update_colors(self):
        """Actualiza los colores de las figuras en función del contador de bucles."""
        nodes = self.figures.get_nodes()
        if not nodes:
            return

        for i, node in enumerate(nodes):
            color = self.color_manager.get_color(i, self.loop_count)
            figure = node.data
            figure.color = color

    def next_shape(self):
        """Avanza a la siguiente figura y actualiza los colores si se completa un ciclo."""
        if self.current_node:
            self.current_node = self.current_node.next
            if self.current_node == self.figures.head:
                self.loop_count += 1
                self._update_colors()

    def prev_shape(self):
        """Retrocede a la figura anterior y actualiza los colores si se completa un ciclo inversamente."""
        if self.current_node:
            if self.current_node == self.figures.head:
                self.loop_count -= 1
            self.current_node = self.current_node.prev
            self._update_colors()