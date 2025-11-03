
def invertir_diccionario(diccionario_original):
    diccionario_invertido = {capital: pais for pais, capital in diccionario_original.items()}
    return diccionario_invertido

def main():
    original = {
        "Argentina": "Buenos Aires",
        "Chile": "Santiago",
        "Uruguay": "Montevideo",
        "Paraguay": "Asunción"
    }

    print("Diccionario original:")
    print(original)

    invertido = invertir_diccionario(original)

    print("Diccionario invertido:")
    print(invertido)


if __name__ == "__main__":
    main()
