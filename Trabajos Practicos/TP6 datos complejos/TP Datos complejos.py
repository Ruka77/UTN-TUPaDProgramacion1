precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}

def main():
    precios_frutas.update({'naranja': 1200, "manzana": 1500, "pera": 2300})
    print(precios_frutas)

if __name__ == "__main__":
    main()

#____________________________________________________________________________

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}

def main():
    precios_frutas.update({'naranja': 1200, "manzana": 1500, "pera": 2300})
    precios_frutas["Banana"] = 1330
    precios_frutas["manzana"] = 1700
    precios_frutas["Melón"] = 2800
    print(precios_frutas)

if __name__ == "__main__":
    main()

#____________________________________________________________________________

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}

def fruta(precio_frutas):
    frutas = list(precios_frutas.keys())
    return frutas

def main():
    precios_frutas.update({'naranja': 1200, "manzana": 1500, "pera": 2300})
    precios_frutas["Banana"] = 1330
    precios_frutas["manzana"] = 1700
    precios_frutas["Melón"] = 2800
    print(precios_frutas)
    frutas = fruta(precios_frutas)
    print(frutas)

if __name__ == "__main__":
    main()

#____________________________________________________________________________

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

#____________________________________________________________________________

contador_palabras = {}

def contador(palabras):
    for palabra in palabras:
        if palabra in contador_palabras:
            contador_palabras[palabra] += 1
        else:
            contador_palabras[palabra] = 1

def main():
    frase = input("Ingrese una frase\n"">> ").strip()
    palabras = frase.split()
    palabras_unicas = set(frase)
    contador(palabras)
    print(palabras)
    print(contador_palabras)

if __name__ == "__main__":
    main()

#____________________________________________________________________________

notas_de_alumnos = {}

def creador_de_dict(alumn1, alumn2, alumn3, notas1, notas2, notas3):
    notas_de_alumnos[alumn1] = notas1
    notas_de_alumnos[alumn2] = notas2
    notas_de_alumnos[alumn3] = notas3

def calcular_notas(alumno):
    notas = []
    print(f"Notas del alumno -{alumno}-")
    for i in range(3):
        nota = int(input(f"Ingrese la nota numero {i + 1}\n"">> "))
        notas.append(nota)
    notas_tupla = tuple(notas)
    return notas_tupla

def promedio(alumn, notas):
    promedios = notas[0] + notas[1] + notas[2]
    promedios = promedios / 3
    print(f"Promedio del alumno -{alumn}-: {promedios:.2f}")

def main():
    alumn1 = input("Ingrese el nombre del primer alumno\n"">> ")
    alumn2 = input("Ingrese el nombre del segundo alumno\n"">> ")
    alumn3 = input("Ingrese el nombre del tercer alumno\n"">> ")
    notas1 = calcular_notas(alumn1)
    notas2 = calcular_notas(alumn2)
    notas3 = calcular_notas(alumn3)
    creador_de_dict(alumn1, alumn2, alumn3, notas1, notas2, notas3)
    print(notas_de_alumnos)
    promedio(alumn1, notas1)
    promedio(alumn2, notas2)
    promedio(alumn3, notas3)

if __name__ == "__main__":
    main()

#____________________________________________________________________________

def main():
    parcial1 = {1, 2, 3, 4, 5}
    parcial2 = {4, 5, 6, 7, 8}
    ambos = parcial1 & parcial2
    print(f"Aprobaron ambos parciales: {ambos}")
    solo_uno = parcial1 ^ parcial2
    print(f"Aprobaron solo uno de los dos: {solo_uno}")
    al_menos_uno = parcial1 | parcial2
    print(f"Aprobaron al menos uno de los dos: {al_menos_uno}")

if __name__ == "__main__":
    main()

#____________________________________________________________________________

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

#____________________________________________________________________________

def crear_agenda():
    agenda = {
        ("lunes", "10:00"): "Reunión",
        ("martes", "15:00"): "Clase de inglés",
        ("miércoles", "18:30"): "Gimnasio",
        ("viernes", "09:00"): "Consulta médica"
    }
    return agenda


def consultar_agenda(agenda, dia, hora):
    clave = (dia.lower(), hora)
    if clave in agenda:
        return f"Actividad: {agenda[clave]}"
    else:
        return "No hay ninguna actividad registrada en ese día y hora."


def main():
    agenda = crear_agenda()

    print("=== CONSULTA DE AGENDA ===")
    dia = input("Ingresá el día: ").strip().lower()
    hora = input("Ingresá la hora (formato HH:MM): ").strip()

    resultado = consultar_agenda(agenda, dia, hora)
    print(resultado)


if __name__ == "__main__":
    main()

#____________________________________________________________________________


def invertir_diccionario(diccionario_original):
    diccionario_invertido = {capital: pais for pais, capital in diccionario_original.items()}
    return diccionario_invertido

def main():
    original = {
        "Argentina": "Buenos Aires",
        "Chile": "Santiago",
        "Uruguay": "Montevideo",
        "Paraguay": "Asunción"
    }

    print("Diccionario original:")
    print(original)

    invertido = invertir_diccionario(original)

    print("Diccionario invertido:")
    print(invertido)


if __name__ == "__main__":
    main()
