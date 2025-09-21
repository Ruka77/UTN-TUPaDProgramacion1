lista = []

for i in range(1, 101):
    if i % 4 == 0:
        lista.append(i)

print(lista)

#------------------------------------------------------

lista = [1, 2, 3, 4, 5]

print(lista[3])

#------------------------------------------------------

lista = []

lista.append("Hola")
lista.append("Mundo")
lista.append("Nuevo")

print(lista)

#------------------------------------------------------

animales = ["perro", "gato", "conejo", "pez"]

animales[1] = "loro"
animales[3] = "oso"

print(animales)

#------------------------------------------------------

numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)
print("Lo que hace el programa es eliminar el numero más alto que encuentra en la lista llamada numeros.")

#------------------------------------------------------

lista = []

for i in range(10, 31, 5):
    lista.append(i)

print(lista[0:2])

#------------------------------------------------------

autos = ["sedan", "pollo", "suran", "gol"]

autos[1] = "ferrari"
autos[2] = "twingo"

print(autos)

#------------------------------------------------------

dobles = []

for i in range(5, 16, 5):
    dobles.append(i * 2)

print(dobles)

#------------------------------------------------------

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

compras[2].append("Jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")

print(compras)

#------------------------------------------------------

lista_anidada = [15, True, [25.5, 57.9, 30.6], False]

print(lista_anidada)