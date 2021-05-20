#* Tarea 3
#* Escribe un programa que acepte una cadena de Caracteres y cuente el tamaño de la cadena
#* y cuantas veces aparece la letra A 

myString = input("Introduzca un string: ")
myString = myString.lower();

largoString = len(myString)

stringA = int(myString.count('a')) + int(myString.count('á'))

print(f"tu string tiene un largo de {largoString} caracteres")
print(f"En tu string habian {stringA} letras 'a'")