titulos = ["los vengadores", "El señor de los anillos", "Senna", "mazze runner", "spiderman", "deadpool"]
copias = [7, 2, 0, 9, 0, 5]

while True:
    print("""
[1] Ingresar lista de títulos
[2] Ingresar lista de ejemplares disponibles por título
[3] Mostrar catalogo en stock y sus copias
[4] Consultar disponibilidad de un título específico
[5] Mostrar títulos agotados
[6] Ingresar nuevo título y copias de este
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
        copias = []
        while True:
            opcion_1 = int(input("[1] Ingresar otro título\n[0] Salir\n"">> "))
            if opcion_1 == 1:
                titulo_nuevo = input("Ingrese un título\n"">> ")
                if titulo_nuevo:
                    titulos.append(titulo_nuevo)
                    print(f"El título -{titulo_nuevo}- ha sido agregado correctamente")
                else:
                    print("No puedes ingresar un titulo vacío")
            elif opcion_1 == 0:
                break
            else:
                print("Opción ingresada incorrecta")
        print("La nueva lista es:")
        for i in titulos:
            print(i)

    elif opcion == 2:
        copias = []
        if titulos:
            while True:
                nuevas_copias_completadas = True
                for i in titulos:
                    try:
                        nuevas_copias = int(input(f"Ingrese la cantidad de ejemplares pare el título -{i}-\n"">> "))
                        copias.append(nuevas_copias)
                    except ValueError:
                        print("Solo se pueden ingresar numeros de copias")
                        nuevas_copias_completadas = False
                        break
                if nuevas_copias_completadas == True:
                    print("Cantidad de ejemplares ingresado correctamente")
                    break
        else:
            print("No hay títulos disponibles")

    elif opcion == 3:
        if not copias or sum(copias) == 0:
            print("No se encuentran títulos con ejemplares existentes")
        else:
            for i in titulos:
                print(f"El título -{i}- tiene {copias[titulos.index(i)]} ejemplares")

    elif opcion == 4:
        titulo_a_buscar = input("Ingrese el título a consultar disponibilidad\n"">> ")
        if titulo_a_buscar in titulos:
            if copias:
                print(f"El título {titulo_a_buscar} tiene {copias[titulos.index(titulo_a_buscar)]}")
            else:
                print("No se han ingresado copias de ningún titulo")
        else:
            print("No se a encontrado el título ingresado")

    elif opcion == 5:
        if copias:
            for i in range(len(titulos)):
                if copias[i] == 0:
                    print(f"El título {titulos[i]} no está disponible")
        else:
            print("No se han ingresado copias de ningún titulo")

    elif opcion == 6:
        if copias and titulos or not copias and not titulos:
            cantidad_de_copias = None
            nuevo_titulo = input("Ingrese el nombre del nuevo título\n"">> ")
            try:
                cantidad_de_copias = int(input("Ingrese la cantidad de copias del nuevo título\n"">> "))
            except ValueError:
                print("Solo puedes ingresar numeros en la cantidad de copias")
            if cantidad_de_copias != None:
                if cantidad_de_copias >= 0:
                    titulos.append(nuevo_titulo)
                    copias.append(cantidad_de_copias)
                    print(f"Se ha ingresado el nuevo título -{nuevo_titulo}-, el mismo contiene {cantidad_de_copias} de copias")
                else:
                    print("No puedes ingresar copias negativas")
        elif not copias and titulos:
            print("Ingresa titulos y copias de los otros titulos primero")

    elif opcion == 7:
        if copias and titulos:
            try:
                opcion_usuario = int(input("ingrese: \n[1] para devolución \n[2] para prestamo\n"">> "))
            except ValueError:
                print("Solo puedes ingresar numeros")
            titulo_devuelto_prestado = input("Ingrese el título devuelto\n"">> ")
            if titulo_devuelto_prestado in titulos:
                cantidad_devueltos = None
                cantidad_prestados = None
                if opcion_usuario == 1:
                    try:
                        cantidad_devueltos = int(input("Ingrese la cantidad de copias devueltas de ese título\n"">> "))
                    except ValueError:
                        print("Solo puedes ingresar numeros")
                    if cantidad_devueltos != None:
                        copias[titulos.index(titulo_devuelto_prestado)] = copias[titulos.index(titulo_devuelto_prestado)] + cantidad_devueltos
                elif opcion_usuario == 2:
                    try:
                        cantidad_prestados = int(input("Ingrese la cantidad de libros prestados"))
                    except ValueError:
                        print("Solo puedes ingresar numeros")
                    if cantidad_prestados != None:
                        if copias[titulos.index(titulo_devuelto_prestado)] - cantidad_prestados >= 0:
                            copias[titulos.index(titulo_devuelto_prestado)] = copias[titulos.index(titulo_devuelto_prestado)] - cantidad_prestados
                        else:
                            print("No se pueden prestar más libros de los que hay en existencia")
                else:
                    print("Solo puedes ingresar 1 o 2")
            else:
                print("No se han ingresado copias o titulos")

    elif opcion == 8:
        print("Títulos en existencias:")
        if titulos and copias:
            for i in range(len(copias)):
                if copias[i] != 0:
                    print(titulos[i])
        else:
            print("Titulos o copias no encontrados")

    elif opcion == 9:
        print("Gracias por usar nuestro sistema de biblioteca")
        break
    else:
        print("Solo puedes ingresar las opciones del 1 al 9")