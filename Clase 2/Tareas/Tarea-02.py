#* Tarea 2
#* Escribe un programa que acepte un numero entero (n) y calcule el valor de n + nn + nnn

numero = int(input("Introduzca un numero entero: "))
calculo = numero + numero ** 2 + numero ** 3

print(f"El resultado es {calculo}")