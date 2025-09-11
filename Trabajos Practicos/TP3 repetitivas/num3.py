valor1 = int(input("Dime el primer numero\n"">> "))
valor2 = int(input("Dime el segundo numero\n"">> "))
suma = 0

for i in range(valor1 + 1, valor2):
    suma += i

print(f"La suma de todos los numeros comprendidos entre {valor1} y {valor2} [Sin incluirlos] es: {suma}")
