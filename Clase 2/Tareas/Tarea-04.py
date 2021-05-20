#* Tarea 4
#* Escribe un programa que muestre la hora actual con la suma de dos horas adicionales

from datetime import datetime

tiempoActual = datetime.now()
horaActual = tiempoActual.hour
minutosActual = tiempoActual.minute

if horaActual >= 22 and horaActual <= 24:
    horaActual -= 24;
    print(f"dentro de dos horas seran las {horaActual + 2}:{minutosActual}")
else:
    print(f"dentro de dos horas seran las {horaActual + 2}:{minutosActual}")
    
