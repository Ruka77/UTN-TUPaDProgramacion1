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
