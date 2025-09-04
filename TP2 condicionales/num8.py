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