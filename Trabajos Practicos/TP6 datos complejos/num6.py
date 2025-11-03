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