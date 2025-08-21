import math
pi_value = math.pi

radio = int(input("Dime el radio del circulo que deseas calcular \n >> "))
area = pi_value * radio * radio
perimetro = 2 * pi_value * radio

print(f"El area del circulo es igual a: {area} y su perímetro es igual a: {perimetro}")