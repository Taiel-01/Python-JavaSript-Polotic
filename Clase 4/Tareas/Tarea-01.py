#* Tarea 01
#* Escribe una clase llamada Rectangula que se define por 
#* una longitud, un ancho y un metodo que calculara el area de un rectangulo

class Rectangulo():

    def __init__(self, longitud, ancho):
        self.longitud = longitud
        self.ancho = ancho
        
        
    def area(self):
        return self.longitud * self.ancho
    
    def __str__(self):
        return f'El area del rectangulo es {self.area()}'
        

rectangulo1 = Rectangulo(2, 3)
print(rectangulo1)