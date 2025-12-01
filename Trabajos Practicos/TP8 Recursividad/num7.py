def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)


def main():
    nivel = int(input("Ingrese el número de bloques en el nivel inferior: "))
    print("Total de bloques en la pirámide:", contar_bloques(nivel))


if __name__ == "__main__":
    main()