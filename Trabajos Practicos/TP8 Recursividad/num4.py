def decimal_a_binario(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return decimal_a_binario(n // 2) + str(n % 2)


def main():
    n = int(input("Ingrese un número decimal para convertir a binario: "))
    print("Resultado binario:", decimal_a_binario(n))


if __name__ == "__main__":
    main()