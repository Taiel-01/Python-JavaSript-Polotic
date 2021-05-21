try:
    f = open("miarchivo.txt", "r")
    f.write("Linea de prueba que estoy escribiendo en el curso")
except FileNotFoundError:
    print("El archivo no se ha encontrado")
finally:
    print("El try y exept finalizó")
