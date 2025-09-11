cantidad_de_numeros = 100

print(f"Ingrese {cantidad_de_numeros} numeros para saber cuantos son pares, cuantos impares, cuantos positivos y cuantos negativos")

contador_pares = 0
contador_impares = 0
contador_positivos = 0
contador_negativos = 0

for i in range(1, cantidad_de_numeros + 1):
    num_usuario = int(input(">> "))
    if num_usuario % 2 == 0:
        contador_pares += 1
    else:
        contador_impares += 1
    if num_usuario > 0:
        contador_positivos += 1
    elif num_usuario < 0:
        contador_negativos += 1

print(f"""La cantidad de numeros pares es de: {contador_pares}
La cantidad de numeros impares es de: {contador_impares}
La cantidad de numeros positivos es de: {contador_positivos}
La cantidad de numeros negativos es de: {contador_negativos}""")
