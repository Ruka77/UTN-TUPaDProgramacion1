import csv
import os

def crear_archivo():
    ruta = "lista_de_productos.csv"
    if os.path.getsize(ruta) == 0:
        with open("lista_de_productos.csv", "w", newline="") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(["Producto", "Precio"])

def mostrar_productos():
    with open("lista_de_productos.csv", "r") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            print(fila)

def agregar_productos():
    producto = input("Ingrese el nombre del producto\n"">> ")
    while True:
        try:
            precio = int(input("Ingrese el valor del producto\n"">> "))
        except ValueError:
            print("El precio debe ser un valor numerico sin simbolos")
            continue
        break
    lista_producto = [{"producto": producto, "precio": precio}]
    with open("lista_de_productos.csv", "a", newline="") as archivo:
        campos = ["producto", "precio"]
        escribir = csv.DictWriter(archivo, fieldnames=campos)
        escribir.writerows(lista_producto)

def eliminar_productos():
    pass

def main():
    crear_archivo()
    while True:
        opcion = input("Ingrese la opción a realizar [1]Mostrar productos [2]Agregar producto [3]Eliminar producto [4]Salir\n"">> ")
        match opcion:
            case "1":
                mostrar_productos()
            case "2":
                agregar_productos()
            case "3":
                eliminar_productos()
            case "4":
                break
            case _:
                print("Ingrese una opción valida")

if __name__ == "__main__":
    main()