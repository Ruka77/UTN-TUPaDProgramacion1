tarjetas = [1111222233334444, 6666777788889999]
saldos = [0, 10]

while True:
    print("""
------- Bienvenido al dispositivo de calculo de sube -------

[1] Ingresar números de tarjeta
[2] Ingresar saldos correspondientes
[3] Mostrar todas las tarjetas y saldos
[4] Consultar saldo por número
[5] Listar saldos en negativo o cero
[6] Agregar tarjeta
[7] Cargar/debitar saldo
[8] Ver todas
[9] Salir
""")

    opcion = input(">> ")
    match opcion:
        case "1":
            tarjeta = input("Ingrese el numero de tarjeta\n"">> ").strip( )
            if not tarjeta.isdigit():
                print("La tarjeta solo puede contener numeros")
                continue
            tarjeta = int(tarjeta)
            if len(tarjeta) != 16:
                print("La tarjeta debe contener 16 digitos")
                continue
            tarjetas.append(tarjeta)
            saldos.append(0)

        case "2":
            numero_correcto = False
            if tarjetas:
                for i in range(len(tarjetas)):
                    saldo = input(f"Ingrese el saldo de la tarjetan numero {i + 1}\n"">> ").strip( )
                    if saldo.count(".") == 1:
                        parte_entera, parte_decimal = saldo.split(".")
                        if parte_entera.isdigit() and (parte_decimal.isdigit() or parte_decimal == " " or parte_decimal == ""):
                            saldo = float(saldo)
                            saldos[i] = saldo
                            numero_correcto = True
                        else:
                            print("El saldo ingresado solo debe contener numeros")
                            break
                    elif saldo.isdigit():
                        saldo = float(saldo)
                        saldos[i] = saldo
                        numero_correcto = True
                    else:
                        print("Los numeros decimales deben ir separados por un punto")
                        break
                if numero_correcto:
                    print(f"El nuevo saldo de las tarjetas es: {tarjetas} ; {saldos}")
            else:
                print("No existen tarjetas en el sistema")
        case "3":
            if tarjetas:
                for i in range(len(tarjetas)):
                    print(f"Tarjeta numero: {tarjetas[i]} ; saldo: ${saldos[i]}")
            else:
                print("No hay tarjetas registradas en el sistema")
        case "4":
            if tarjetas:
                tarjeta_a_consultar = input("Ingrese el numero de tarjeta que deseas consultar su saldo\n"">> ").strip( )
                if not tarjeta_a_consultar.isdigit():
                    print("Solo puedes ingresar numeros")
                    continue
                if len(tarjeta_a_consultar) != 16:
                    print("La tarjeta debe contar con 16 digitos")
                    continue
                tarjeta_a_consultar = int(tarjeta_a_consultar)
                if tarjeta_a_consultar in tarjetas:
                    print(f"El saldo de la tarjeta es: ${saldos[tarjetas.index(tarjeta_a_consultar)]}")
        case "5":
            if not tarjetas:
                print("No se encontraron tarjetas en el sistema")
                continue
            print("Tarjetas con saldo igual o menor a cero: ")
            for i in range(len(tarjetas)):
                if saldos[i] <= 0:
                    print(tarjetas[i])
        case "6":
            nueva_tarjeta = input("Ingrese el numero de la nueva tarjeta\n"">> ").strip( )
            if not nueva_tarjeta.isdigit():
                print("La tarjeta debe contener solo numeros")
                continue
            nuevo_saldo = input("Ingrese el saldo de la nueva tarjeta\n"">> ")
            if nuevo_saldo.count(".") == 1:
                        parte_entera, parte_decimal = nuevo_saldo.split(".")
                        if parte_entera.isdigit() and (parte_decimal.isdigit() or parte_decimal == " " or parte_decimal == ""):
                            nuevo_saldo = float(nuevo_saldo)
                        else:
                            print("El saldo ingresado solo debe contener numeros")
                            continue
            elif not nuevo_saldo.isdigit():
                print("El saldo de la nueva tarjeta debe ser un numero")
                continue
            nueva_tarjeta = int(nueva_tarjeta)
            nuevo_saldo = float(nuevo_saldo)
            tarjetas.append(nueva_tarjeta)
            saldos.append(nuevo_saldo)
            print("Nueva trajeta añadida con exito\n"f"Numero: {nueva_tarjeta} - saldo: ${nuevo_saldo}")
        case "7":
            if not tarjetas:
                print("No se encuentran tarjetas en el sistema")
                continue
            operacion = input("Ingrese que operación desea realizar: [Cargar / Debitar]\n"">> ").strip().lower()
            if operacion == "cargar":
                tarjeta_a_cargar = input("Ingrese el numero de tarjeta al que desea cargar\n"">> ")
                if not tarjeta_a_cargar.isdigit():
                    print("El numero de tarjeta solo puede contener digitos")
                    continue
                tarjeta_a_cargar = int(tarjeta_a_cargar)
                credito_a_cargar = input("Ingrese la cantidad de credito que deseas cargar\n"">> ").strip()
                if credito_a_cargar.count(".") == 1:
                    parte_entera, parte_decimal = credito_a_cargar.split(".")
                    if parte_entera.isdigit() and parte_decimal.isdigit() or parte_decimal == "":
                        credito_a_cargar = float(credito_a_cargar)
                    else:
                        print("Solo pudese ingresar numeros")
                        continue
                elif credito_a_cargar.isdigit():
                    credito_a_cargar = float(credito_a_cargar)
                else:
                    print("El saldo debe ir separado con una coma")
                    continue
                if tarjeta_a_cargar in tarjetas:
                    saldos[tarjetas.index(tarjeta_a_cargar)] = saldos[tarjetas.index(tarjeta_a_cargar)] + credito_a_cargar
                else:
                    print("Tarjeta ingresada no encontrada")
                    continue
                print(f"Saldo final de la tarjeta {tarjeta_a_cargar} ; ${saldos[tarjetas.index(tarjeta_a_cargar)]}")
            elif operacion == "debitar":
                tarjeta_a_debitar = input("Ingrese el numero de tarjeta al que desea cargar\n"">> ")
                if not tarjeta_a_debitar.isdigit():
                    print("El numero de tarjeta solo puede contener digitos")
                    continue
                tarjeta_a_debitar = int(tarjeta_a_debitar)
                credito_a_debitar = input("Ingrese la cantidad de credito que deseas debitar\n"">> ").strip()
                if credito_a_debitar.count(".") == 1:
                    parte_entera, parte_decimal = credito_a_debitar.split(".")
                    if parte_entera.isdigit() and parte_decimal.isdigit() or parte_decimal == "":
                        credito_a_debitar = float(credito_a_debitar)
                    else:
                        print("Solo pudese ingresar numeros")
                        continue
                elif credito_a_debitar.isdigit():
                    credito_a_debitar = float(credito_a_debitar)
                else:
                    print("Solo puedes ingresar numeros")
                    continue
                if tarjeta_a_debitar in tarjetas:
                    saldos[tarjetas.index(tarjeta_a_debitar)] = saldos[tarjetas.index(tarjeta_a_debitar)] - credito_a_debitar
                else:
                    print("El saldo debe ir separado con una coma")
                    continue
                print(f"Saldo final de la tarjeta {tarjeta_a_debitar} ; ${saldos[tarjetas.index(tarjeta_a_debitar)]}")
            else:
                print("Operación invalida")
                continue
        case "8":
            print("Hasta luego!!")
            break