##Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

def operaciones_basicas(a, b):
    sum = a + b
    rest = a - b
    mult = a * b
    divis = a / b
    resultados = (sum, rest, mult, divis)
    return resultados

def main():
    a = int(input("Ingrese el primer numero\n"">> "))
    b = int(input("Ingrese el segundo numero\n"">> "))
    resultado = operaciones_basicas(a, b)
    print(resultado)

if __name__ == "__main__":
    main()