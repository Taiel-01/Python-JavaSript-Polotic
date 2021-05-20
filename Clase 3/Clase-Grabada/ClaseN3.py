
#* ===================  Lista  =====================
nombres = ["Harry", "Ron", "Hermione"]

nombres.append("Draco")     #? agregar
nombres.sort()              #? ordenar

print(nombres)
print(nombres[0])           #? ubicacion [0]


#* ====================  Set  =======================
conjunto = set()

conjunto.add("Harry")
conjunto.add("Ron")
conjunto.add("Hermione")
conjunto.remove("Ron")

print(len(conjunto))


#* ====================  Diccionario  ====================
casas = {"Harry" : "Gryffindor", "Draco" : "Slytherin"}
casas["Hermione"] = "Gryffindor"

print(casas)

covidData = {123 : True, 456 : False}
covidData[789] = True

print(covidData);


#* ==================  if / elif / else  ==================
miVariable = int(input("Ingrese un digito numerico: "))

if miVariable < 0:
    print("La variable es menor que cero")
elif miVariable > 0:
    print("mi variable es mayor que cero")
else:
    print("mi variable es 0")