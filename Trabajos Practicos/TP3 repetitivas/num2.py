num_usuario = int(input("Ingrese un numero entero\n"">> "))
digitos = 0

while True:
    if num_usuario >= 1:
        num_usuario = num_usuario / 10
        digitos += 1
    elif num_usuario == 0:
        print("Haz ingresado 0")
        break
    else:
        break

print(f"La cantidad de digitos es de: {digitos}")