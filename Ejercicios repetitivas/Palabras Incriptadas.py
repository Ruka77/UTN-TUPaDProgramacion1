letras = "abcdefghijklmnñopqrstuvwxyz"
corrimiento = int(input("Ingrese la cantidad de letras a correr\n"">> "))

for contador in range(0, 6):
    mensaje = input(f"Ingrese el mensaje numero {contador + 1} \n"">> ").lower()
    mensaje_cifrado = ""
    for caracter in mensaje:
        if caracter in letras:
            indice = letras.index(caracter)
            nueva_letra = letras[(indice + corrimiento) % 27]
            mensaje_cifrado += nueva_letra
        else:
            mensaje_cifrado += caracter
    print(f"el mensaje cifrado es: {mensaje_cifrado}")
    print("-----")