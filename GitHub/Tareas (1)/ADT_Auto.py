class AutomovilEstatico:
    """
    Representa un Automóvil como un ADT estático utilizando una tupla.
    """

    mi_auto = ("Nissan", "Versa", 2018, "Gris")

    def get_marca(self):
        """Obtiene la marca del automóvil desde la tupla."""
        return self.mi_auto[0]

    def get_modelo(self):
        """Obtiene el modelo del automóvil desde la tupla."""
        return self.mi_auto[1]

    def get_año(self):
        """Obtiene el año del automóvil desde la tupla."""
        return self.mi_auto[2]

    def get_color(self):
        """Obtiene el color del automóvil desde la tupla."""
        return self.mi_auto[3]


coche1 = AutomovilEstatico()
print(f"Marca: {coche1.get_marca()}")
print(f"Modelo: {coche1.get_modelo()}")
print(f"Año: {coche1.get_año()}")
print(f"Color: {coche1.get_color()}")

# Generar error al modificar la tupla
# coche1.mi_auto[0] = "Toyota"
# print(f"Marca actualizada: {coche1.get_marca()}")
