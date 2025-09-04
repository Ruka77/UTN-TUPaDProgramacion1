edad = int(input("Ingrese su edad\n"">> "))

if edad >= 18:
    print("Eres mayor de edad")

#////////////////////////////////////////////////////////////////

nota = int(input("Ingrese su nota\n"">> "))
if nota >= 6:
    print("Aprobaste")
else:
    print("Desaprobaste")

#////////////////////////////////////////////////////////////////

num_usuario = int(input("ingrese un numero par\n"">> "))
if num_usuario % 2 == 0:
    print("El numero es par")
else:
    print("Porfavor, ingrese un numero par")

#////////////////////////////////////////////////////////////////

edad = int(input("Ingrese su edad\n"">> "))

if edad < 12:
    print("Usted es un niño")
elif edad < 18:
    print("Usted es un adolescente")
elif edad < 30:
    print("Usted es un joven")
else:
    print("Usted es un adulto")

#////////////////////////////////////////////////////////////////

contraseña = str(input("Ingrese una contraseña\n"">> "))

if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Contraseña válida")
else:
    print("Contraseña inválida, porfavor ingrese una contraseña entre 8 y 14 caracteres")

#////////////////////////////////////////////////////////////////

import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

num_mode = mode(numeros_aleatorios)
num_median = median(numeros_aleatorios)
num_mean = mean(numeros_aleatorios)

print(f"La moda es: {num_mode}")
print(f"La mediana es: {num_median}")
print(f"La media es: {num_mean}")

if num_mean > num_median and num_median > num_mode:
    print("Se encuentra un sesgo positivo o a la derecha")
elif num_mean < num_median and num_median < num_mode:
    print("Se encuentra un sesgo negativo")
else:
    print("Sin sesgo")

#////////////////////////////////////////////////////////////////

texto = input("Ingrese una palabra o frase\n"">> ")
vocales = "aeiouAEIOU"

if len(texto) > 0 and texto[-1] in vocales:
    texto += "!"

print("Resultado:", texto)

#////////////////////////////////////////////////////////////////

nombre = input("Ingrese su nombre\n"">> ")

opcion = int(input("Ingrese \n[1]Para poner su nombre en mayusculas\n" \
"[2]Para poner su nombre en minusculas\n" \
"[3]Para poner la primera en mayusculas\n"))

if opcion == 1:
    nombre = nombre.upper()
elif opcion == 2:
    nombre = nombre.lower()
elif opcion == 3:
    nombre = nombre.title()

print(f"Tu nombre quedaría así: {nombre}")

#////////////////////////////////////////////////////////////////

terremeto = float(input("Ingrese la magnitud del terremoto\n"">> "))

if terremeto < 3:
    magnitud = "Muy leve, imperceptible"
elif terremeto < 4:
    magnitud = "Leve, ligeramente perceptible"
elif terremeto < 5:
    magnitud = "Moderado, sentido por personas, pero generalmente no causa daños"
elif terremeto < 6:
    magnitud = "Fuerte, puede causar daños en estructuras débiles"
elif terremeto < 7:
    magnitud = "Muy fuerte, puede causar daños significativos"
elif terremeto > 7:
    magnitud = "Extremo, puede causar graves daños a gran escala"
else:
    print("Numero fuera de rango permitido")

print(f"El terremoto fue {magnitud}")

#////////////////////////////////////////////////////////////////

hemisferio = input("Ingrese en qué hemisferio se encuentra, N o S\n"">> ").lower()
mes = input("Ingrese el mes en el que se encuentra\n"">> ").lower()
dia = int(input("Ingrese el día de la semana en el que se encuentra\n"">> "))

if hemisferio == "n":
    if mes == "diciembre" and dia >= 21:
        estacion = "invierno"
    elif mes == "enero" or mes == "febrero":
        estacion = "invierno"
    elif mes == "marzo" and dia <= 20:
        estacion = "invierno"
    elif mes == "marzo" and dia >= 21:
        estacion = "primavera"
    elif mes == "abril" or mes == "mayo":
        estacion = "primavera"
    elif mes == "junio" and dia <= 20:
        estacion = "primavera"
    elif mes == "junio" and dia >= 21:
        estacion = "verano"
    elif mes == "julio" or mes == "agosto":
        estacion = "verano"
    elif mes == "septiembre" and dia <= 20:
        estacion = "verano"
    elif mes == "septiembre" and dia >= 21:
        estacion = "otoño"
    elif mes == "octubre" or mes == "noviembre":
        estacion = "otoño"
    elif mes == "diciembre" and dia <= 20:
        estacion = "otoño"

elif hemisferio == "s":
    if mes == "diciembre" and dia >= 21:
        estacion = "verano"
    elif mes == "enero" or mes == "febrero":
        estacion = "verano"
    elif mes == "marzo" and dia <= 20:
        estacion = "verano"
    elif mes == "marzo" and dia >= 21:
        estacion = "otoño"
    elif mes == "abril" or mes == "mayo":
        estacion = "otoño"
    elif mes == "junio" and dia <= 20:
        estacion = "otoño"
    elif mes == "junio" and dia >= 21:
        estacion = "invierno"
    elif mes == "julio" or mes == "agosto":
        estacion = "invierno"
    elif mes == "septiembre" and dia <= 20:
        estacion = "invierno"
    elif mes == "septiembre" and dia >= 21:
        estacion = "primavera"
    elif mes == "octubre" or mes == "noviembre":
        estacion = "primavera"
    elif mes == "diciembre" and dia <= 20:
        estacion = "primavera"

print(f"La estación del año en la que te encuentras es {estacion}")

#////////////////////////////////////////////////////////////////