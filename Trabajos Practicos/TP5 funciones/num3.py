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