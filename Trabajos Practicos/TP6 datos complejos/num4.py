contactos = {}

def contacto():
    nombre = input("Ingrese el nombre del contacto\n"">> ")
    num = input("Ingrese el numero de telefono\n"">> ")
    contactos[nombre] = num
    print(f"El contacto con nombre -{nombre}- y numero -{num}- ha sido guardado")

def main():
    for i in range(5):
        contacto()
    print(contactos)

if __name__ == "__main__":
    main()