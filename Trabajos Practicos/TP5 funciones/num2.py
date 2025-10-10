def saludar_usuario(nombre):
    print(f"¡Hola {nombre}")

def main():
    saludar_usuario(input("Ingrese su nombre\n"">> ").capitalize())

if __name__ == "__main__":
    main()