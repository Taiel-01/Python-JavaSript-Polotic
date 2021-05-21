class Perro:

    especie = "Canis Lupus familiaris"

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def descripcion(self):
        return f"{self.nombre} tiene {self.edad}"

    def ladrar(self, sonido):
        return f"{self.nombre} hace este sonido: {sonido}"

    def str(self):
        return f"{self.nombre} tiene {self.edad} años"


class DogoArgentino(Perro):
    raza = "Dogo Argentino"


class BullDogFrances(Perro):
    raza = "Dogo Frances"
