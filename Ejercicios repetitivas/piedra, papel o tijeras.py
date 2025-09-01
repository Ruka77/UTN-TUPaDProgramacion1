import random
print("Bienvenido al juego de piedra papel o tijeras")

while True:
    print("Ingrese uno \n[1]Piedra [2]Papel [3]Tijeras [4]Salir")
    opcion_usuario = int(input(">> "))
    opcion_maquina = random.randint(1, 3)

    if opcion_maquina == 1:
        opcion_maquina_escrito = "piedra"
    elif opcion_maquina == 2:
        opcion_maquina_escrito = "papel"
    else:
        opcion_maquina_escrito = "tijeras"

    if opcion_usuario == 1 or opcion_usuario == 2 or opcion_usuario == 3:
        if opcion_maquina == opcion_usuario:
            print(f"Haz empatado con la maquina!!! Ambos sacaron {opcion_maquina_escrito}")
        elif opcion_maquina == 1 and opcion_usuario == 2:
            print(f"La maquina saca {opcion_maquina_escrito}, le haz ganado!!!")
        elif opcion_maquina == 1 and opcion_usuario == 3:
            print(f"La maquina saca {opcion_maquina_escrito}, te ha ganado, prueba de nuevo")
        elif opcion_maquina == 2 and opcion_usuario == 1:
            print(f"La maquina saca {opcion_maquina_escrito}, te ha ganado, prueba de nuevo")
        elif opcion_maquina == 2 and opcion_usuario == 3:
            print(f"La maquina saca {opcion_maquina_escrito}, le haz ganado!!!")
        elif opcion_maquina == 3 and opcion_usuario == 1:
            print(f"La maquina saca {opcion_maquina_escrito}, le haz ganado!!!")
        elif opcion_maquina == 3 and opcion_usuario == 2:
            print(f"La maquina saca {opcion_maquina_escrito}, te ha ganado, prueba de nuevo")
    elif opcion_usuario == 4:
        print("Hasta la proxima!!")
        exit()
    else:
        print("opcion invalida")