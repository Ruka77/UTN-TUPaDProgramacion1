titulos = ["los vengadores", "El señor de los anillos", "Senna", "mazze runner", "spiderman", "deadpool"]
copias = [7, 2, 0, 9, 0, 5]
suma_copias = 0

while True:
    print("""
[1] Ingresar lista de titulos
[2] Ingresar lista de ejemplares disponibles por titulo
[3] Mostrar catalogo en stock y sus copias
[4] Consultar disponibilidad de un titulo específico
[5] Mostrar titulos agotados
[6] Ingresar nuevo titulo y copias de este
[7] Actualizar numero de copias (préstamos/devolución)
[8] Ver catalogo disponibles
[9] Salir del programa
""")

    try:
        opcion = int(input(">> "))
    except ValueError:
        print("Ingrese una opción correcta en numeros")

    if opcion == 1:
        titulos = []
        while True:
            opcion_1 = int(input("[1] Ingresar otro titulo\n[0] Salir\n"">> "))
            if opcion_1 == 1:
                titulo_nuevo = input("Ingrese un titulo\n"">> ")
                titulos.append(titulo_nuevo)
                print(f"El titulo -{titulo_nuevo}- a sido agregado correctamente")
            elif opcion_1 == 0:
                break
            else:
                print("Opción ingresada incorrecta")
        print("La nueva lista es:")
        for i in titulos:
            print(i)

    elif opcion == 2:
        copias = []
        while True:
            nuevas_copias_completadas = True
            for i in titulos:
                try:
                    nuevas_copias = int(input(f"Ingrese la cantidad de ejemplares pare el titulo -{i}-\n"">> "))
                    copias.append(nuevas_copias)
                except ValueError:
                    print("Solo se pueden ingresar numeros de copias")
                    nuevas_copias_completadas = False
                    break
            if nuevas_copias_completadas == True:
                print("Cantidad de ejemplares ingresado correctamente")
                break

    elif opcion == 3:
        for i in range(len(copias)):
            suma_copias += copias[i]
        if not copias or suma_copias == 0:
            print("No se encuentran titulos con ejemplares existentes")
        else:
            for i in titulos:
                print(f"El titulo -{i}- tiene {copias[titulos.index(i)]} ejemplares")

    elif opcion == 4:
        titulo_a_buscar = input("Ingrese el titulo a consultar disponibilidad\n"">> ")
        if titulo_a_buscar in titulos:
            print(f"El titulo {titulo_a_buscar} tiene {copias[titulos.index(titulo_a_buscar)]}")
        else:
            print("No se a encontrado el titulo ingresado")

    elif opcion == 5:
        for i in range(len(titulos)):
            if copias[i] == 0:
                print(f"El titulo {titulos[i]} no está disponible")

    elif opcion == 6:
        nuevo_titulo = input("Ingrese el nombre del nuevo titulo\n"">> ")
        try:
            cantidad_de_copias = int(input("Ingrese la cantidad de copias del nuevo titulo\n"">> "))
        except ValueError:
            print("Solo puedes ingresar numeros en la cantidad de copias")
        titulos.append(nuevo_titulo)
        copias.append(cantidad_de_copias)
        print(f"Se a ingresado el nuevo titulo -{nuevo_titulo}-, el mismo contiene {cantidad_de_copias} de copias")

    elif opcion == 7:
        try:
            opcion_usuario = input("ingrese: \n[1] para devolución \n[2] para prestamo\n"">> ")
        except ValueError:
            print("Solo puedes ingresar numeros")
        titulo_devuelto_prestado = input("Ingrese el titulo devuelto\n"">> ")
        if titulo_devuelto_prestado in titulos:
            if opcion_usuario == 1:
                cantidad_devueltos = int(input("Ingrese la cantidad de copias devueltas de ese titulo\n"">> "))
                copias[titulos.index(titulo_devuelto_prestado)] = copias[titulos.index(titulo_devuelto_prestado)] + cantidad_devueltos
            elif opcion_usuario == 2:
                cantidad_prestados = int(input("Ingrese la cantidad de libros prestados"))
                if copias[titulos.index(titulo_devuelto_prestado)] - cantidad_prestados > 0:
                    copias[titulos.index(titulo_devuelto_prestado)] = copias[titulos.index(titulo_devuelto_prestado)] - cantidad_prestados
                else:
                    print("No se pueden prestar más libros de los que hay en existencia")
            else:
                print("Solo puedes ingresar 1 o 2")

    elif opcion == 8:
        print("Titulos en existencias:")
        for i in range(len(copias)):
            if copias[i] != 0:
                print(titulos[i])

    elif opcion == 9:
        print("Gracias por usar nuestro sistema de biblioteca")
        break
    else:
        print("Solo puedes ingresar las opciones del 1 al 9")