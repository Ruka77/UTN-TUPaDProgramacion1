#Crear una función llamada calcular_imc(peso, altura) que reciba el
#peso en kilogramos y la altura en metros, y devuelva el índice de
#masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def main():
    peso = float(input("Dame tu peso en kilos\n"">> "))
    altura = float(input("Dime tu altura en metros\n"">> "))
    imc = calcular_imc(peso, altura)
    print(f"Tu indice de masa corporal es de {imc:.2f} puntos")

if __name__ == "__main__":
    main()