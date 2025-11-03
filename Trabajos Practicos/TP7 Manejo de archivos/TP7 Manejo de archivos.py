import os

def crear_archivo_inicial(ruta="productos.txt"):
    """Crea productos.txt con 3 productos si no existe."""
    if not os.path.exists(ruta):
        inicial = [
            "Lapicera,120.5,30\n",
            "Cuaderno,250,50\n",
            "Goma,50,100\n"
        ]
        with open(ruta, "w", encoding="utf-8") as f:
            f.writelines(inicial)


def leer_productos(ruta="productos.txt"):
    """
    Lee el archivo y devuelve:
    - lista_de_lineas: lista de strings (líneas limpias)
    - productos: lista de diccionarios con claves 'nombre','precio','cantidad'
    """
    productos = []
    lineas = []
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if not linea:
                    continue
                lineas.append(linea)
                partes = [p.strip() for p in linea.split(",")]
                if len(partes) != 3:
                    # línea inválida, la ignoramos o la podemos manejar.
                    continue
                nombre = partes[0]
                # intentamos convertir precio y cantidad
                try:
                    precio = float(partes[1])
                except ValueError:
                    precio = 0.0
                try:
                    cantidad = int(float(partes[2]))
                except ValueError:
                    cantidad = 0
                productos.append({
                    "nombre": nombre,
                    "precio": precio,
                    "cantidad": cantidad
                })
    except FileNotFoundError:
        # devolvemos listas vacías si no existe
        return [], []
    return lineas, productos


def mostrar_productos(productos):
    """Muestra por consola la lista de productos con el formato pedido."""
    if not productos:
        print("No hay productos para mostrar.")
        return
    for p in productos:
        print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")


def agregar_producto_a_archivo(ruta="productos.txt"):
    """
    Pide al usuario un producto (nombre, precio, cantidad) y lo agrega al archivo
    sin borrar el contenido existente (modo 'a').
    Permite agregar múltiples productos hasta que el usuario ingrese una línea vacía para nombre.
    """
    print("\n-- Agregar productos (dejar nombre vacío para terminar) --")
    with open(ruta, "a", encoding="utf-8") as f:
        while True:
            nombre = input("Nombre del producto (enter para terminar): ").strip()
            if nombre == "":
                break
            precio_in = input("Precio: ").strip()
            cantidad_in = input("Cantidad: ").strip()
            # validaciones básicas
            try:
                precio = float(precio_in)
            except ValueError:
                print("Precio inválido. Se asignará 0.0")
                precio = 0.0
            try:
                cantidad = int(float(cantidad_in))
            except ValueError:
                print("Cantidad inválida. Se asignará 0")
                cantidad = 0
            linea = f"{nombre},{precio},{cantidad}\n"
            f.write(linea)
            print(f"Producto '{nombre}' agregado al archivo.")


def buscar_producto(productos, nombre_buscar):
    """
    Busca un producto por nombre (case-insensitive).
    Devuelve el diccionario del producto o None si no existe.
    """
    nombre_buscar = nombre_buscar.strip().lower()
    for p in productos:
        if p["nombre"].strip().lower() == nombre_buscar:
            return p
    return None


def guardar_productos(productos, ruta="productos.txt"):
    """
    Sobrescribe el archivo escribiendo todos los productos de la lista.
    Cada línea: nombre,precio,cantidad
    """
    with open(ruta, "w", encoding="utf-8") as f:
        for p in productos:
            linea = f"{p['nombre']},{p['precio']},{p['cantidad']}\n"
            f.write(linea)
    print(f"\nArchivo '{ruta}' actualizado con {len(productos)} productos.")

def main():
    ruta = "productos.txt"
    crear_archivo_inicial(ruta)

    # 1) Leer y mostrar productos (y cargar en lista de dicts)
    _, productos = leer_productos(ruta)
    print("=== Productos cargados desde el archivo ===")
    mostrar_productos(productos)

    # 2) Agregar productos desde teclado (se agrega al archivo sin borrar)
    agregar = input("\n¿Querés agregar productos al archivo ahora? (s/n): ").strip().lower()
    if agregar == "s":
        agregar_producto_a_archivo(ruta)
        # recargamos la lista después de agregar
        _, productos = leer_productos(ruta)

    # 3) Buscar producto por nombre
    buscar = input("\n¿Querés buscar un producto por nombre? (s/n): ").strip().lower()
    if buscar == "s":
        nombre = input("Ingresá el nombre del producto a buscar: ").strip()
        encontrado = buscar_producto(productos, nombre)
        if encontrado:
            print("\nProducto encontrado:")
            print(f"Nombre: {encontrado['nombre']}")
            print(f"Precio: ${encontrado['precio']}")
            print(f"Cantidad: {encontrado['cantidad']}")
        else:
            print("No existe un producto con ese nombre.")

    # 4) Guardar los productos actualizados (sobrescribe con la lista actual)
    guardar = input("\n¿Querés sobrescribir el archivo productos.txt con los datos cargados en memoria? (s/n): ").strip().lower()
    if guardar == "s":
        guardar_productos(productos, ruta)

    print("\nPrograma finalizado. ¡Hasta luego!")

if __name__ == "__main__":
    main()

