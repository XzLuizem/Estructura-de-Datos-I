class Conjunto_Estatico:
    def __init__(self, capacidad_maxima):
        self.capacidad_maxima = capacidad_maxima
        self.elementos = [None] * capacidad_maxima
        self.tamaño = 0

    def agregar(self, elemento):
        if self.tamaño < self.capacidad_maxima:
            if not self.contiene(elemento):
                self.elementos[self.tamaño] = elemento
                self.tamaño += 1
                return True  # Elemento agregado exitosamente
            else:
                return False  # Elemento ya existe
        else:
            return False  # Conjunto lleno

    def eliminar(self, elemento):
        try:
            indice = self.elementos[:self.tamaño].index(elemento)
            # Mover el último elemento a la posición del elemento eliminado
            self.elementos[indice] = self.elementos[self.tamaño - 1]
            # Opcional: limpiar la última posición
            self.elementos[self.tamaño - 1] = None
            self.tamaño -= 1
            return True  # Elemento eliminado exitosamente
        except ValueError:
            return False  # Elemento no encontrado

    def contiene(self, elemento):
        return elemento in self.elementos[:self.tamaño]

    def es_vacio(self):
        return self.tamaño == 0

    def es_lleno(self):
        return self.tamaño == self.capacidad_maxima

    def obtener_tamaño(self):
        return self.tamaño

    def __str__(self):
        return "{" + ", ".join(str(e) for e in self.elementos[:self.tamaño]) + "}"


# Ejemplo de uso
conjunto = Conjunto_Estatico(5)
print(f"Conjunto inicial: {conjunto}")
print(f"¿Está vacío? {conjunto.es_vacio()}")
print(f"¿Está lleno? {conjunto.es_lleno()}")
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

print("\nAgregando más elementos hasta llenar:")
print(f"Agregar 40: {conjunto.agregar(40)}")
print(f"Agregar 50: {conjunto.agregar(50)}")
# Intentar agregar a conjunto lleno
print(f"Agregar 60: {conjunto.agregar(60)}")
print(f"Conjunto actual: {conjunto}")
print(f"¿Está lleno? {conjunto.es_lleno()}")
print(f"Tamaño: {conjunto.obtener_tamaño()}")
