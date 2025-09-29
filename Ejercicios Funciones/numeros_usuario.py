
def sum_digitos(num):
    suma = 0
    for digito in str(num):
        suma += int(digito)
    return suma

def main():
    sum = 0
    while True:
        num_usuario = input("Ingrese un numero [0] = Salir\n"">> ")
        if int(num_usuario) == 0:
            break
        sum += int(num_usuario)
        print(f"La suma de los digitos de tu numero es: {sum_digitos(num_usuario)}")
    print(f"La suma de todos los numeros ingresados es: {sum}")

if __name__ == "__main__":
    main()