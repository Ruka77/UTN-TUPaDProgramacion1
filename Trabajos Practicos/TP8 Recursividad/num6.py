def suma_digitos(n):
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)


def main():
    numero = int(input("Ingrese un número para sumar sus dígitos: "))
    print("Suma de dígitos:", suma_digitos(numero))


if __name__ == "__main__":
    main()