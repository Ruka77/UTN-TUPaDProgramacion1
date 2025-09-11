texto = input("Ingrese una palabra o frase\n"">> ")
vocales = "aeiouAEIOU"

if len(texto) > 0 and texto[-1] in vocales:
    texto += "!"

print("Resultado:", texto)
