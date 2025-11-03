stock = {"manzana": 2, "choclo": 10, "naranja": 5}

def consultar_stock():
    producto = input("Ingresa el producto a consultar\n"">> ").strip().lower()
    if producto in stock:
        print(f"El stock de {producto} es de {stock[producto]} unidades")
    else:
        print("El producto ingresado no se ha encontrado")

def agregar_stock():
    producto = input("Ingrese el producto a agregar unidades\n"">> ").strip().lower()
    if producto in stock:
        unidades = int(input(f"Ingrese la cantidad de unidades a agregar a {producto}\n"">> "))
        stock[producto] += unidades
        print(f"Stock actualizado de {producto}: {stock[producto]}")
    else:
        print("El producto no fue encontrado")

def agregar_producto():
    producto = input("Ingrese el producto a agregar\n"">> ").strip().lower()
    if producto not in stock:
        stock[producto] = int(input(f"Ingrese la cantidad de unidades para {producto}\n"">> "))
        print(f"{producto} ha sido agregado con exito con {stock[producto]} unidades")
    else:
        print(f"El producto {producto} ya existe en la lista")
    

def main():
    print(f"El stock actual: \n{stock}")
    while True:
        opcion = input("Ingrese [1] para consultar el stock de un producto -- [2] Para agregar unidades -- [3] Agregar un nuevo producto -- [4] Salir\n"">> ")
        match opcion:
            case "1":
                consultar_stock()
            case "2":
                agregar_stock()
            case "3":
                agregar_producto()
            case "4":
                print("Saliendo del programa")
                break
            case __:
                print("Opción ingresada incorrecta")
                continue

if __name__ == "__main__":
    main()