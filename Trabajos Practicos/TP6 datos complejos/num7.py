
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