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
    def ladrar(self, sonido="guau"):
        return super().ladrar(sonido)

class BulldogFrances(Perro):
    pass

perro1 = DogoArgentino("Firulais", 5)
perro1 = DogoArgentino("Firulais", 5)
print(perro1.raza)

print(type(perro1))

print(isinstance(perro1, DogoArgentino))

print(perro1.ladrar())