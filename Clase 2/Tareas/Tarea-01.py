#* Tarea 1
#* Escribe un programa que acepte el radio de un circulo del usuario y calcule el area

import math

radio = float(input("El radio del circulo es: "))


if radio < 0: 
    print("Vuelva a intentarlo")
else:
    area = math.pi * radio ** 2;
    print(f"El area del circulo es: {round(area, 2)}")





