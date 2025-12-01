def contar_digito(numero, digito):
    if numero == 0:
        return 0

    ultimo = numero % 10
    if ultimo == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)


def main():
    numero = int(input("Ingrese un número entero positivo: "))
    digito = int(input("Ingrese el dígito a contar (0-9): "))
    print(f"El dígito {digito} aparece:", contar_digito(numero, digito), "veces")


if __name__ == "__main__":
    main()