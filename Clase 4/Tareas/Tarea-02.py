#* Tarea 02
#* Crea una clase Minibus que herede de la clase Vehiculo.
#* Debes poder tener un metodo capacidad() que defina por defecto la capacidad de 6 asientos
#* Luego crea una clase Pasajero que puedas ir agregando una instancia de Minibus.
#* Esta instancia no debera permitir mas de 50 pasajeros unicos(no se permiten pasajeros repetidos)

class Vehiculo():
    
    def __init__(self, asientos, ruedas, modelo):
        self.asientos = asientos
        self.ruedas = ruedas
        self.modelo = modelo
    
    def __str__(self):
        return f"El vehiculo tiene {self.ruedas} ruedas, {self.asientos} asientos y su modelo es {self.modelo}"


class Minibus (Vehiculo):

    def __init__ (self, asientos, ruedas, modelo):
        super().__init__(asientos, ruedas, modelo)
        self.setCapacidad()
        self.capacidad
        self.listaPasajeros = [] 
        self.limitePasajeros = 50
        
    def setCapacidad(self):
        self.capacidad = 6

    def AgregarPasajero(self, pasajero):
        if (len(self.listaPasajeros) >= self.limitePasajeros) and self.repetido(pasajero):
            self.listaPasajeros.append(pasajero)

    def repetido(self, pasajero):
        for i in self.listaPasajeros:
            if(i.nombre == pasajero.nombre):   
                return False
        return True
    
      
class Pasajero():
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        
    def __str__(self):
        return f"Nombre: {self.nombre} Apellido: {self.apellido}"



