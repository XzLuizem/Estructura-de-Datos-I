class CounterModel:
    """
    Modelo de datos para la aplicación de contador.
    Maneja el estado y la lógica de negocio del contador.
    """
    def __init__(self):
        self._count = 0

    def get_count(self):
        """Retorna el valor actual del contador."""
        return self._count

    def increment(self):
        """Incrementa el contador en uno."""
        self._count += 1
