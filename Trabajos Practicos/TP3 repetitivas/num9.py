cantidad_de_numeros = 100
suma = 0

print("Ingrese todos los numeros a calcular")

for i in range(1, cantidad_de_numeros + 1):
    num_usuario = int(input(">> "))
    suma += num_usuario

print(f"La media de los {cantidad_de_numeros} numeros ingresados es de {suma / cantidad_de_numeros}")
