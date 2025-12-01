def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])


def main():
    palabra = input("Ingrese una palabra sin espacios: ")
    print("¿Es palíndromo?:", es_palindromo(palabra))


if __name__ == "__main__":
    main()