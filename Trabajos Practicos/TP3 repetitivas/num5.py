import random

print("Bienvenido al juego de azar, ingresa un numero entre el 0 y el 9")
num_generado = random.randint(0, 9)
num_usuario = 10
contador = 0

while num_usuario != num_generado:
    num_usuario = int(input(">> "))
    contador += 1

print(f"Haz acertado el numero en {contador} intentos!!!\n"f"El numero era {num_generado}")