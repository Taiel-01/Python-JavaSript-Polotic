#* Tarea 3
#* Escriba un programa que acepte 5 numeros enteros del usuario
#* y los guarde en una lista

while True:
    numerosE = input("Escriba 5 numeros enteros separados por espacios: ")
    numerosE = numerosE.split()
    LargoE = len(numerosE)
    if LargoE == 5:
        break
    
for i in range(LargoE):
    numerosE[i] = int(numerosE[i])
    print(numerosE[i])
    