print("Hola Mundo")

numero = 4
print(numero)
print(bin(numero))
print(hex(numero))

numeroComplejo = 4 + 1j
print(numeroComplejo.imag)
print(numeroComplejo.real)


#* En esta parte van las importaciones
import datetime

#* Declaramos variables, funciones o inicializamos
miFechaYHora = datetime.datetime.now()
print(miFechaYHora)

numero = 123
print(type(numero))

otronumero = 123.0
print(type(otronumero))


#* Implementamos la ejecucion de nuestro aplicativo
micadena = "Cadena"

print(type(micadena))
print(micadena.upper())
print(micadena.lower())
print(micadena.capitalize())

