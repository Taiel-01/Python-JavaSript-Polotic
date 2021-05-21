import sys

try:
    numero1 = int(input("Ingrese numero 1: "))
    numero2 = int(input("Ingrese numero 2: "))
except ValueError:
    print("Error, valor no valido.")
    sys.exit(1)


try:
    resultado = numero1 / numero2
except ZeroDivisionError:
    print("Error, No se puede dividir por cero.")
    sys.exit(1)
else:
    print("La division salió como se esperaba.")
    print(
        f'El resultado de dividir {numero1} por {numero2} es: {round(resultado, 2)}')
