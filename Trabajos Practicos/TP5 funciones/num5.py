def segundos_a_hora(segundos):
    return ((segundos / 60) / 60)

def main():
    segundos = int(input("Ingrese los segundos a calcular\n"">> "))
    hora = segundos_a_hora(segundos)
    print(f"{segundos} segundos son iguales a {hora:.2f} horas")

if __name__ == "__main__":
    main()