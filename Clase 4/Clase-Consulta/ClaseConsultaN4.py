
#* ========= Control de bucle por centinela =========
x = input("Ingrese un digito: ")
while x > 0:
    print(x)
    x = int(input("Ingrese un digito"))
    
print("Fin ejecucion centinela")


#* ==============  Control por contador ==============
x = 0
while x < 100:
    print(x)
    x = x + 1
    
print("Fin ejecución contador")