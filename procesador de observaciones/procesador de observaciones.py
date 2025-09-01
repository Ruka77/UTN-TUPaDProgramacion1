dd = ""
mm = ""
dia = ""
anio_biciesto = False

print("Bienvenido al procesador de observaciones de clases. Porfavor ingrese el día")
fecha_completa = input("Ingresa la fecha con el siguiente formato: dia, DD/MM""\n"">> ")

dia, fecha_num = fecha_completa.split(", ")
dd, mm = fecha_num.split("/")
dd = int(dd)
mm = int(mm)
dia = dia.lower()

if dia != "lunes" and dia != "martes" and dia != "miercoles" and dia != "jueves" and dia != "viernes":
    print("Hubo un error, el día tipado no es correcto.")
    exit()

if mm < 1 or mm > 12:
    print("Hubo un error, el mes ingresado no es valido.")
    exit()

if mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm == 12:
    if dd < 1 or dd > 31:
        print("Día ingresado fuera de rango del mes ingresado")
        exit()
elif mm == 4 or mm == 6 or mm == 9 or mm == 11:
    if dd < 1 or dd > 30:
        print("Día ingresado fuera de rango del mes ingresado")
        exit()
else:
    anio = int(input("Ingrese el año \n"">> "))
    if anio % 4 == 0:
        anio_biciesto = True
    if anio % 100 == 0 and anio % 400 != 0:
        anio_biciesto = False
    if anio_biciesto:
        if dd < 1 or dd > 29:
            print("Día ingresado fuera de rango del mes ingresado")
            exit()
    else:
        if dd < 1 or dd > 28:
            print("Día ingresado fuera de rango del mes ingresado")
            exit()

print("Fecha ingresada correcta.")

if dia == "lunes" or dia == "martes" or dia == "miercoles":
    examenes = input("¿Se tomaron los examenes? responder con si o no \n"">> ").lower()
    if examenes == "si":
        cantidad_de_no_aprobados = int(input("Ingrese la cantidad de alumnos que reprobaron \n"">> "))
        cantidad_de_aprobados = int(input("Ingrese la cantidad de aprobados \n"">> "))
        cantidad_de_alumnos = cantidad_de_aprobados + cantidad_de_no_aprobados
        por_de_aprobados = round((cantidad_de_aprobados * 100) / cantidad_de_alumnos, 2)
        print(f"El porcentaje de aprobados es del {por_de_aprobados}%")

if dia == "jueves":
    por_de_asistencia = int(input("Ingrese el porcentaje de asistencia. (sin el simbolo de porcentaje) \n"">> "))
    if por_de_asistencia > 50:
        print("Asistieron la mayoría")
    elif por_de_asistencia < 50:
        print("No asistieron la mayoría")
    else:
        print("Asistió la mitad")

if dia == "viernes":
    if (mm == 1 or mm == 7) and dd == 1:
        print("Comienzo de nuevo ciclo")
        cantidad_de_alumnos_nuevo_ciclo = int(input("Dime la cantidad de alumnos del nuevo ciclo \n"">> "))
        arancel = int(input("Ingrese en pesos el arancel por cada alumno \n"">> "))
        total_de_ingresos = cantidad_de_alumnos_nuevo_ciclo * arancel
        print(f"La cantidad de ingresos totales es igual a ${total_de_ingresos}")