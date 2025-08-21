altura = int(input("Dime tu altura en cm \n >> "))
peso = int(input("Dime tu peso en kilos\n >> "))
altura_en_metros = altura / 100
imc = peso / (altura_en_metros * altura_en_metros)

print(f"\nTu IMC es de {imc} puntos")

if imc < 18.5:
    print("\nTe encuentras por debajo de tu peso recomendado por tu estatura")
elif imc >= 18.5 and imc <= 24.9:
    print("\nTe encuentras en tu peso recomendado para tu estatura")
elif imc >= 25 and imc <= 29.9:
    print("\nTe encuentras por encima de tu peso recomendado para tu estatura")
elif imc >= 30:
    print("\nTe encuentras muy por encima de tu peso recomendado para tu estatura")

print("\nIMC: \n" \
"Menos a 18.5 == Peso inferior al normla \n" \
"18.5 - 24.9 == Peso normal\n" \
"25 - 29.9 == Peso superior al normal\n" \
"Más de 30 == Peso muy superior al normal")