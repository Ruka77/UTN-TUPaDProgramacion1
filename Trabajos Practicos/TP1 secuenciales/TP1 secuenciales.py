#Leyenda: los comentarios donde salen las barras medias es para indicar y seperar cada ejercicio del trabajo practico y sea más simple
# y comodo leer el codigo

#-----------------------------------------------------------------------------------#

print("Hola Mundo!")

#-----------------------------------------------------------------------------------#

nombre = input("¿Cuál es tu nombre? Ingresalo!! " "\n"
">> ")

print(f"Hola {nombre}, mucho gusto!")

#-----------------------------------------------------------------------------------#

nombre = input("Ingresa tu nombre""\n"">> ")
apellido = input("ingresa tu apellido""\n"">> ")
edad = input("ingresa tu edad""\n"">> ")
residencia =  input("ingresa tu lugar de residencia""\n"">> ")

print(f"Hola! Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#-----------------------------------------------------------------------------------#

import math
pi_value = math.pi

radio = int(input("Dime el radio del circulo que deseas calcular \n >> "))
area = pi_value * radio * radio
perimetro = 2 * pi_value * radio

print(f"El area del circulo es igual a: {area} y su perímetro es igual a: {perimetro}")

#-----------------------------------------------------------------------------------#

segundos = int(input("dime la cantidad de segundos \n >> "))
horas = segundos / 3600

print(f"Los {segundos} segundos ingresados equivalen a {horas} hora/s")

#-----------------------------------------------------------------------------------#

num = int(input("Dime de cuál numero quieres ver su tabla de multiplicación" "\n" ">> "))
numero_por_0 = num * 0
numero_por_1 = num * 1
numero_por_2 = num * 2
numero_por_3 = num * 3
numero_por_4 = num * 4
numero_por_5 = num * 5
numero_por_6 = num * 6
numero_por_7 = num * 7
numero_por_8 = num * 8
numero_por_9 = num * 9
print(f"""
  {num} x 0 = {numero_por_0}
  {num} x 1 = {numero_por_1}
  {num} x 2 = {numero_por_2}
  {num} x 3 = {numero_por_3}
  {num} x 4 = {numero_por_4}
  {num} x 5 = {numero_por_5}
  {num} x 6 = {numero_por_6}
  {num} x 7 = {numero_por_7}
  {num} x 8 = {numero_por_8}
  {num} x 9 = {numero_por_9}
      """)

#-----------------------------------------------------------------------------------#

num_usuario1 = int(input("Dame dos numeros enteros" "\n" ">> "))
num_usuario2 = int(input(">> "))

suma = num_usuario1 + num_usuario2
division = num_usuario1 / num_usuario2
resta = num_usuario1 - num_usuario2
multiplicacion = num_usuario1 * num_usuario2

print(f"tu numero {num_usuario1} y {num_usuario2} dan como resultado: \n"
      f"suma: {suma} \n"
      f"resta: {resta}\n"
      f"division: {division}\n"
      f"multiplicacion: {multiplicacion}")

#-----------------------------------------------------------------------------------#

altura = int(input("Dime tu altura en cm \n >> "))
peso = int(input("Dime tu peso en kilos\n >> "))
altura_en_metros = altura / 100
imc = peso / (altura_en_metros * altura_en_metros)

print(f"\nTu IMC es de {imc} puntos")

if imc < 18.5:
    print("\nTe encuentras por debajo de tu peso recomendado por tu estatura")
elif imc >= 18.5 and imc <= 24.9:
    print("\nTe encuentras en tu peso recomendado para tu estatura")
elif imc >= 25 and imc <= 29.9:
    print("\nTe encuentras por encima de tu peso recomendado para tu estatura")
elif imc >= 30:
    print("\nTe encuentras muy por encima de tu peso recomendado para tu estatura")

print("\nIMC: \n" \
"Menos a 18.5 == Peso inferior al normla \n" \
"18.5 - 24.9 == Peso normal\n" \
"25 - 29.9 == Peso superior al normal\n" \
"Más de 30 == Peso muy superior al normal")

#-----------------------------------------------------------------------------------#

celsius = float(input("Dime una temperatura en grades celsius \n>> "))
fahrenheit = (9/5) * celsius + 32

print(f"La temperatura ingresadda en fahrenheit es de: {fahrenheit}°")

#-----------------------------------------------------------------------------------#

print("Dame a continuación 3 numeros para sacar su promedio")

num1 = int(input(">> "))
num2 = int(input(">> "))
num3 = int(input(">> "))

promedio = (num1 + num2 + num3) / 3

print(f"El promedio de los 3 numeros dados es: {promedio}")