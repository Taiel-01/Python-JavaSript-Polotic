#* Tarea 4
#* lista (lista1 = [12, 15, 32, 42, 55, 75, 122, 132, 140, 190, 200]),
#* iterarla y mostrar numeros divisibles por cinco, y si se encuentra
#* un numero mayor que 150, detenga la iteracion

lista1 = [12, 15, 32, 42, 55, 75, 122, 132, 140, 190, 200]

for i in range(len(lista1)) :
    if lista1[i] > 150:
        break
    elif lista1[i] % 5 == 0:
        print(lista1[i])
        