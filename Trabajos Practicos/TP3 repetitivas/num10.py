numero = int(input("Ingrese un número\n"">> "))
numero_invertido = 0

while numero > 0:
    digito = numero % 10
    numero_invertido = numero_invertido * 10 + digito
    numero = numero // 10

print(f"El número invertido es: {numero_invertido}")