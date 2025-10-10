def imprimir_hola_mundo():
    print("Hola Mundo")

def main():
    imprimir_hola_mundo()

if __name__ == "__main__":
    main()

#-------------------------------------------------------#
def saludar_usuario(nombre):
    print(f"¡Hola {nombre}")

def main():
    saludar_usuario(input("Ingrese su nombre\n"">> ").capitalize())

if __name__ == "__main__":
    main()
#-------------------------------------------------------#
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia} ")

def main():
    nombre = input("Ingrese su nombre\n"">> ").capitalize()
    apellido = input("Ingrese su apellido\n"">> ").capitalize()
    edad = int(input("Ingrese su edad\n"">> "))
    residencia = input("Ingrese su dirección\n"">> ").lower()
    informacion_personal(nombre, apellido, edad, residencia)

if __name__ == "__main__":
    main()
#-------------------------------------------------------#
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
#-------------------------------------------------------#
def segundos_a_hora(segundos):
    return ((segundos / 60) / 60)

def main():
    segundos = int(input("Ingrese los segundos a calcular\n"">> "))
    hora = segundos_a_hora(segundos)
    print(f"{segundos} segundos son iguales a {hora:.2f} horas")

if __name__ == "__main__":
    main()
#-------------------------------------------------------#
def tabla_multiplicar(num):
    for i in range(11):
        print(num ," x ", i ," = ", num * i)

def main():
    numero = int(input("Ingrese el numero a mostrar su tabla\n"">> "))
    tabla_multiplicar(numero)

if __name__ == "__main__":
    main()
#-------------------------------------------------------#
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
#-------------------------------------------------------#
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
#-------------------------------------------------------#
def celsius_a_fahrenheit(celsius):
    f = (celsius * 9/5) + 32
    return f

def main():
    celsius = float(input("Ingrese la temperatura en celsius\n"">> "))
    fahrenheit = celsius_a_fahrenheit(celsius)
    print(f"La temperatura ingresada en fahrenheit es: {fahrenheit:.1f}°")

if __name__ == "__main__":
    main()
#-------------------------------------------------------#
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
