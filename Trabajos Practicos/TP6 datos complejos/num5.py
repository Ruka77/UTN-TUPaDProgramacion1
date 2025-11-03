contador_palabras = {}

def contador(palabras):
    for palabra in palabras:
        if palabra in contador_palabras:
            contador_palabras[palabra] += 1
        else:
            contador_palabras[palabra] = 1

def main():
    frase = input("Ingrese una frase\n"">> ").strip()
    palabras = frase.split()
    palabras_unicas = set(frase)
    contador(palabras)
    print(palabras)
    print(contador_palabras)

if __name__ == "__main__":
    main()