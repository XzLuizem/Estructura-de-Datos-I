# Realizar el ADT conjunto empleando un modelo dinámico en memoria
# Implementación usando una lista dinámica en memoria

class Conjunto_Dinamico:
    """
    Implementación de un Conjunto ADT dinámico.
    Utiliza una lista como modelo en memoria, permitiendo un tamaño variable.
    """

    def __init__(self):
        """
        Inicializa un conjunto dinámico vacío.
        """
        self._elementos = []  # Usamos una lista de Python que es dinámica
        self._tamaño = 0

    def add(self, element):
        """
        Agrega un elemento al conjunto si no está ya en el conjunto.

        Args:
            element: El elemento a agregar.

        Returns:
            True si el elemento fue agregado, False en caso contrario.
        """
        if not self.contains(element):
            self._elementos.append(element)
            self._tamaño += 1
            return True  # Elemento agregado exitosamente
        else:
            # print(f"'{element}' ya existe en el conjunto. No se agregará.")
            return False  # Elemento ya existe en el conjunto

    def remove(self, element):
        """
        Elimina un elemento del conjunto si existe.

        Args:
            element: El elemento a eliminar.

        Returns:
            True si el elemento fue eliminado, False en caso contrario.
        """
        try:
            self._elementos.remove(element)
            self._tamaño -= 1
            return True  # Elemento eliminado exitosamente
        except ValueError:
            return False  # Elemento no encontrado

    def contains(self, element):
        """
        Verifica si un elemento está presente en el conjunto.

        Args:
            element: El elemento a buscar.

        Returns:
            True si el elemento está en el conjunto, False en caso contrario.
        """
        return element in self._elementos

    def is_empty(self):
        """
        Verifica si el conjunto está vacío.

        Returns:
            True si el conjunto está vacío, False en caso contrario.
        """
        return self._tamaño == 0

    def is_full(self):
        """
        Verifica si el conjunto está lleno.
        En un conjunto dinámico sin límite fijo, siempre devuelve False.
        """
        return False  # Conjunto dinámico no tiene límite fijo

    def get_size(self):
        """
        Obtiene el número actual de elementos en el conjunto.

        Returns:
            El tamaño actual del conjunto.
        """
        return self._tamaño

    def __str__(self):
        """
        Representación en cadena del conjunto.
        """
        return "{" + ", ".join(str(e) for e in self._elementos) + "}"

# --- Ejemplo con tres conjuntos dinámicos: primarios, secundarios y otros colores ---


print("--- Ejemplo con tres conjuntos dinámicos ---")

# Listas de colores de referencia
primary_colors_list = ["rojo", "azul", "amarillo"]
secondary_colors_list = ["verde", "naranja", "violeta"]
all_colors_to_add = [
    "rojo", "azul", "verde", "cian", "magenta", "amarillo",
    "naranja", "marrón", "violeta", "negro", "blanco"
]

# Crear los tres conjuntos dinámicos
conjunto_primarios = Conjunto_Dinamico()
conjunto_secundarios = Conjunto_Dinamico()
conjunto_otros = Conjunto_Dinamico()

print(f"\nConjunto inicial primarios: {conjunto_primarios}")
print(f"Conjunto inicial secundarios: {conjunto_secundarios}")
print(f"Conjunto inicial otros: {conjunto_otros}")

print("\nAgregando colores a los conjuntos correspondientes:")

for color in all_colors_to_add:
    if color in primary_colors_list:
        if conjunto_primarios.add(color):
            print(f"Agregado '{color}' a primarios.")
    elif color in secondary_colors_list:
        if conjunto_secundarios.add(color):
            print(f"Agregado '{color}' a secundarios.")
    else:
        if conjunto_otros.add(color):
            print(f"Agregado '{color}' a otros.")

print("\nEstado final de los conjuntos:")
print(f"Conjunto primarios: {conjunto_primarios}")
print(f"Tamaño primarios: {conjunto_primarios.get_size()}")
print(f"Conjunto secundarios: {conjunto_secundarios}")
print(f"Tamaño secundarios: {conjunto_secundarios.get_size()}")
print(f"Conjunto otros: {conjunto_otros}")
print(f"Tamaño otros: {conjunto_otros.get_size()}")

print("\nVerificando elementos en los conjuntos:")
print(f"Primarios contiene 'rojo'? {conjunto_primarios.contains('rojo')}")
print(
    f"Secundarios contiene 'verde'? {conjunto_secundarios.contains('verde')}")
print(f"Otros contiene 'cian'? {conjunto_otros.contains('cian')}")
print(f"Primarios contiene 'cian'? {conjunto_primarios.contains('cian')}")

print("\nEliminando elementos:")
print(f"Eliminar 'azul' de primarios: {conjunto_primarios.remove('azul')}")
print(
    f"Eliminar 'naranja' de secundarios: {conjunto_secundarios.remove('naranja')}")
print(f"Eliminar 'negro' de otros: {conjunto_otros.remove('negro')}")
print(
    f"Eliminar 'rojo' de secundarios (no existe): {conjunto_secundarios.remove('rojo')}")

print("\nEstado final después de eliminaciones:")
print(f"Conjunto primarios: {conjunto_primarios}")
print(f"Tamaño primarios: {conjunto_primarios.get_size()}")
print(f"Conjunto secundarios: {conjunto_secundarios}")
print(f"Tamaño secundarios: {conjunto_secundarios.get_size()}")
print(f"Conjunto otros: {conjunto_otros}")
print(f"Tamaño otros: {conjunto_otros.get_size()}")
