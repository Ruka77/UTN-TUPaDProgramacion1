""" Crear una función llamada calcular_promedio(a, b, c) que reciba
tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta
función. """

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio

def main():
    primera_nota = float(input("Ingrese la primera nota\n"">> "))
    segunda_nota = float(input("Ingrese la segunda nota\n"">> "))
    tercera_nota = float(input("Ingrese la tercera nota\n"">> "))
    promedio = calcular_promedio(primera_nota, segunda_nota, tercera_nota)
    print(f"El promedio de las tres notas ingresadas es: {promedio:.2f}")

if __name__ == "__main__":
    main()