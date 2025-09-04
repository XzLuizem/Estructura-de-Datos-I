# Realizar el ADT conjunto empleando un modelo dinámico en memoria

class Conjunto_Dinamico:
    """
    Implementación de un Conjunto ADT dinámico.
    Utiliza una lista de Python como modelo en memoria, permitiendo un tamaño variable.
    """

    def __init__(self):
        """
        Inicializa un conjunto dinámico vacío.
        """
        self.elementos = []  # Usamos una lista de Python que es dinámica
        self.tamaño = 0

    def agregar(self, elemento):
        """
        Agrega un elemento al conjunto si no está ya presente.

        Args:
            elemento: El elemento a agregar.

        Returns:
            True si el elemento fue agregado, False en caso contrario.
        """
        if not self.contiene(elemento):
            self.elementos.append(elemento)
            self.tamaño += 1
            return True  # Elemento agregado exitosamente
        else:
            return False  # Elemento ya existe

    def eliminar(self, elemento):
        """
        Elimina un elemento del conjunto si existe.

        Args:
            elemento: El elemento a eliminar.

        Returns:
            True si el elemento fue eliminado, False en caso contrario.
        """
        try:
            self.elementos.remove(elemento)
            self.tamaño -= 1
            return True  # Elemento eliminado exitosamente
        except ValueError:
            return False  # Elemento no encontrado

    def contiene(self, elemento):
        """
        Verifica si un elemento está presente en el conjunto.

        Args:
            elemento: El elemento a buscar.

        Returns:
            True si el elemento está en el conjunto, False en caso contrario.
        """
        return elemento in self.elementos

    def es_vacio(self):
        """
        Verifica si el conjunto está vacío.

        Returns:
            True si el conjunto está vacío, False en caso contrario.
        """
        return self.tamaño == 0

    # En un conjunto dinámico, no existe un estado "lleno" con una capacidad máxima fija.
    # Si se necesitara una capacidad máxima, se podría agregar una verificación aquí,
    # pero por defecto, un conjunto dinámico no tiene límite.

    def obtener_tamaño(self):
        """
        Obtiene el número actual de elementos en el conjunto.

        Returns:
            El tamaño actual del conjunto.
        """
        return self.tamaño

    def __str__(self):
        """
        Representación en cadena del conjunto.
        """
        return "{" + ", ".join(str(e) for e in self.elementos) + "}"


# Ejemplo de uso
conjunto = Conjunto_Dinamico()
print(f"Conjunto inicial: {conjunto}")
print(f"¿Está vacío? {conjunto.es_vacio()}")
print(f"Tamaño: {conjunto.obtener_tamaño()}")

print("\nAgregando elementos:")
print(f"Agregar 10: {conjunto.agregar(10)}")
print(f"Agregar 20: {conjunto.agregar(20)}")
print(f"Agregar 10: {conjunto.agregar(10)}")  # Intentar agregar duplicado
print(f"Agregar 30: {conjunto.agregar(30)}")
print(f"Conjunto actual: {conjunto}")
print(f"Tamaño: {conjunto.obtener_tamaño()}")

print("\nVerificando si contiene elementos:")
print(f"Contiene 20? {conjunto.contiene(20)}")
print(f"Contiene 50? {conjunto.contiene(50)}")

print("\nEliminando elementos:")
print(f"Eliminar 20: {conjunto.eliminar(20)}")
# Intentar eliminar elemento no existente
print(f"Eliminar 50: {conjunto.eliminar(50)}")
print(f"Conjunto actual: {conjunto}")
print(f"Tamaño: {conjunto.obtener_tamaño()}")

print("\nAgregando más elementos:")
print(f"Agregar 40: {conjunto.agregar(40)}")
print(f"Agregar 50: {conjunto.agregar(50)}")
print(f"Agregar 60: {conjunto.agregar(60)}")
print(f"Conjunto actual: {conjunto}")
print(f"Tamaño: {conjunto.obtener_tamaño()}")
