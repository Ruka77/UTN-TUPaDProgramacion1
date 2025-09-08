import random

carton_lleno = False
numeros = random.sample(range(1, 51), 25)
carton = [[0 for _ in range(5)] for _ in range(5)]

for m in range(5):
    for n in range(5):
        carton[m][n] = numeros.pop()

print("Tu cartón de bingo es:")
for fila in carton:
    print(fila)

bolas = list(random.sample(range(1, 51), 48))
random.shuffle(bolas)

while not carton_lleno and bolas:
    bola = bolas.pop()
    print(f"Número sacado: {bola}")
    for m in range(5):
        for n in range(5):
            if carton[m][n] == bola:
                carton[m][n] = 0
                print("¡Has acertado un número!")
                for fila in carton:
                    print(fila)
                if all(carton[i][j] == 0 for i in range(5) for j in range(5)):
                    carton_lleno = True
                    break
    if carton_lleno:
        print("¡Bingo! Has completado el cartón.")
        break
    elif not bolas:
        print("No quedan más bolas. Fin del juego.")
        break