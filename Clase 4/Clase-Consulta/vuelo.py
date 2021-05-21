class Vuelo():
    
    #? def defina los metodos de las clases
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.pasajeros = []
    
    def asignar_capacidad(self, capacidad):
        self.capacidad = capacidad
    
    def agregar_pasajero(self, nombre):
        #? si devuelve un valor mayor a cero va a ser true y sino va a ser false
        if not self.asientos_libres():
            return False
        self.pasajeros.append(nombre)
        return True
        
    def asientos_libres(self):
        return self.capacidad - len(self.pasajeros)
    
    def __str__(self):
        return f"Instancia de la clase Vuelo que tiene capacidad {self.capacidad}"


vuelo_a_madrid = Vuelo(2)
vuelo_a_madrid.agregar_pasajero("Juan Carlos")
print(vuelo_a_madrid)