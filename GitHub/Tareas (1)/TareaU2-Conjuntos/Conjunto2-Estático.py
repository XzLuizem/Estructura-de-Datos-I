# Realizar el ADT conjunto empleando un modelo estático en memoria
# Implementación usando getters y setters para las listas de colores

class StaticSet:
    """
    Implementación de un Conjunto ADT estático.
    Utiliza un arreglo (lista de tamaño fijo) como modelo en memoria.
    Incluye getters y setters para las listas de validación de colores.
    """

    def __init__(self, max_capacity):
        """
        Inicializa un conjunto estático con una capacidad máxima dada.

        Args:
            max_capacity: La capacidad máxima del conjunto.
        """
        self.max_capacity = max_capacity
        self._elements = [None] * max_capacity
        self._size = 0
        # Atributos para almacenar los colores primarios y secundarios para validación
        self._primary_colors = []
        self._secondary_colors = []

    @property
    def primary_colors(self):
        """Getter para primary_colors."""
        return self._primary_colors

    @primary_colors.setter
    def primary_colors(self, colors):
        """Setter para primary_colors con validación."""
        if isinstance(colors, list):
            self._primary_colors = colors
            print("Listas de colores primarios establecidas.")
        else:
            print("Error: primary_colors debe ser una lista.")

    @property
    def secondary_colors(self):
        """Getter para secondary_colors."""
        return self._secondary_colors

    @secondary_colors.setter
    def secondary_colors(self, colors):
        """Setter para secondary_colors con validación."""
        if isinstance(colors, list):
            self._secondary_colors = colors
            print("Listas de colores secundarios establecidas.")
        else:
            print("Error: secondary_colors debe ser una lista.")

    def add(self, element):
        """
        Agrega un elemento al conjunto si existe espacio, no está ya en el conjunto,
        y *es* un color primario o secundario definido externamente.

        Args:
            element: El elemento a agregar.

        Returns:
            True si el elemento fue agregado, False en caso contrario.
        """
        # Verificar si el elemento es un color primario o secundario definido externamente
        if element not in self._primary_colors and element not in self._secondary_colors:
            print(
                f"'{element}' no es un color primario o secundario definido externamente. No se agregará.")
            return False

        # Ahora proceder con la lógica original si el elemento es un color válido
        if self._size < self.max_capacity:
            if not self.contains(element):
                self._elements[self._size] = element
                self._size += 1
                return True  # Elemento agregado exitosamente
            else:
                print(f"'{element}' ya existe en el conjunto. No se agregará.")
                return False  # Elemento ya existe en el conjunto
        else:
            print(f"El conjunto está lleno. No se pudo agregar '{element}'.")
            return False  # Conjunto lleno

    def remove(self, element):
        """
        Elimina un elemento del conjunto si existe.

        Args:
            element: El elemento a eliminar.

        Returns:
            True si el elemento fue eliminado, False en caso contrario.
        """
        try:
            # Buscar el índice del elemento en la parte ocupada del arreglo
            index = self._elements[:self._size].index(element)
            # Mover el último elemento a la posición del elemento eliminado
            self._elements[index] = self._elements[self._size - 1]
            # Opcional: limpiar la última posición
            self._elements[self._size - 1] = None
            self._size -= 1
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
        return element in self._elements[:self._size]

    def is_empty(self):
        """
        Verifica si el conjunto está vacío.

        Returns:
            True si el conjunto está vacío, False en caso contrario.
        """
        return self._size == 0

    def is_full(self):
        """
        Verifica si el conjunto está lleno.

        Returns:
            True si el conjunto está lleno, False en caso contrario.
        """
        return self._size == self.max_capacity

    def get_size(self):
        """
        Obtiene el número actual de elementos en el conjunto.

        Returns:
            El tamaño actual del conjunto.
        """
        return self._size

    def __str__(self):
        """
        Representación en cadena del conjunto.
        """
        return "{" + ", ".join(str(e) for e in self._elements[:self._size]) + "}"


# Ejemplo de uso con colores primarios y secundarios usando setters
print("--- Ejemplo con Colores ---")
primary_colors_list = ["rojo", "azul", "amarillo"]
secondary_colors_list = ["verde", "naranja", "violeta"]

# La capacidad máxima se establece explícitamente para este ejemplo
max_capacity_colors = 6  # 3 colores primarios + 3 colores secundarios
color_set_with_setters = StaticSet(max_capacity_colors)

# Establecer las listas de colores usando los setters
color_set_with_setters.primary_colors = primary_colors_list
color_set_with_setters.secondary_colors = secondary_colors_list

print(f"\nConjunto inicial de colores: {color_set_with_setters}")
print(f"¿Está vacío? {color_set_with_setters.is_empty()}")
print(f"Tamaño: {color_set_with_setters.get_size()}")

print("\nIntentando agregar colores primarios:")
for color in primary_colors_list:
    print(f"Agregar '{color}': {color_set_with_setters.add(color)}")
print(f"Conjunto actual: {color_set_with_setters}")
print(f"Tamaño: {color_set_with_setters.get_size()}")

print("\nIntentando agregar colores secundarios:")
for color in secondary_colors_list:
    print(f"Agregar '{color}': {color_set_with_setters.add(color)}")
print(f"Conjunto actual: {color_set_with_setters}")
print(f"Tamaño: {color_set_with_setters.get_size()}")
print(f"¿Está lleno? {color_set_with_setters.is_full()}")


print("\nVerificando si contiene colores:")
print(f"Contiene 'azul'? {color_set_with_setters.contains('azul')}")
print(f"Contiene 'blanco'? {color_set_with_setters.contains('blanco')}")
print(f"Contiene 'violeta'? {color_set_with_setters.contains('violeta')}")

print("\nEliminando colores:")
print(f"Eliminar 'azul': {color_set_with_setters.remove('azul')}")
# Intentar eliminar elemento no existente
print(f"Eliminar 'negro': {color_set_with_setters.remove('negro')}")
print(f"Conjunto actual: {color_set_with_setters}")
print(f"Tamaño: {color_set_with_setters.get_size()}")

print("\nIntentando agregar un color adicional que no es primario ni secundario:")
print(f"Agregar 'cian': {color_set_with_setters.add('cian')}")
print(f"Conjunto actual: {color_set_with_setters}")
print(f"Tamaño: {color_set_with_setters.get_size()}")
print(f"¿Está lleno? {color_set_with_setters.is_full()}")

print("\nIntentando agregar colores primarios o secundarios nuevamente (ya agregados):")
# Ya existe en el conjunto
print(f"Agregar 'rojo': {color_set_with_setters.add('rojo')}")
# Ya existe en el conjunto
print(f"Agregar 'verde': {color_set_with_setters.add('verde')}")

# --- Ejemplo con Colores ---
# Listas de colores primarios establecidas.
# Listas de colores secundarios establecidas.

# Conjunto inicial de colores: {}
# ¿Está vacío? True
# Tamaño: 0

# Intentando agregar colores primarios:
# Agregar 'rojo': True
# Agregar 'azul': True
# Agregar 'amarillo': True
# Conjunto actual: {rojo, azul, amarillo}
# Tamaño: 3

# Intentando agregar colores secundarios:
# Agregar 'verde': True
# Agregar 'naranja': True
# Agregar 'violeta': True
# Conjunto actual: {rojo, azul, amarillo, verde, naranja, violeta}
# Tamaño: 6
# ¿Está lleno? True

# Verificando si contiene colores:
# Contiene 'azul'? True
# Contiene 'blanco'? False
# Contiene 'violeta'? True

# Eliminando colores:
# Eliminar 'azul': True
# Eliminar 'negro': False
# Conjunto actual: {rojo, violeta, amarillo, verde, naranja}
# Tamaño: 5

# Intentando agregar un color adicional que no es primario ni secundario:
# 'cian' no es un color primario o secundario definido externamente. No se agregará.
# Agregar 'cian': False
# Conjunto actual: {rojo, violeta, amarillo, verde, naranja}
# Tamaño: 5
# ¿Está lleno? False

# Intentando agregar colores primarios o secundarios nuevamente (ya agregados):
# 'rojo' ya existe en el conjunto. No se agregará.
# Agregar 'rojo': False
# 'verde' ya existe en el conjunto. No se agregará.
# Agregar 'verde': False
