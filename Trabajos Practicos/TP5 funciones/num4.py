from math import pi

def calcular_area_circulo(radio):
    area = pi * radio ** 2
    return area

def calcular_perimetro_circulo(radio):
    perimetro = 2 * pi * radio
    return perimetro

def main():
    radio = int(input("Ingrese el radio del circulo\n"">> "))
    area = calcular_area_circulo(radio)
    perimetro = calcular_perimetro_circulo(radio)
    print(f"El area del circulo es {area:.2f} y el perimetro es {perimetro:.2f}")

if __name__ == "__main__":
    main()