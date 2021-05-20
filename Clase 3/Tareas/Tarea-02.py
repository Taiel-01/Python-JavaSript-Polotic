#* Tarea 2
#* Escriba un programa que acepte 5 numeros decimales del usuario


while True:
    numerosD = input("Escriba 5 numeros decimales separados por espacios: ")
    numerosD = numerosD.split()
    LargoD = len(numerosD)
    if LargoD == 5:
        break
    
for i in range(LargoD):
    numerosD[i] = float(numerosD[i])
    print(numerosD[i])
    
    