print("Dame un numero y lo sumaré con el proximo que ingreses [Ingresa 0 para salir]")
num = int(input("Ingrese el primer numero\n"">> "))
suma = 0

while num:
    suma += num
    num = int(input(">> "))

print(f"El total acumulado es {suma}")