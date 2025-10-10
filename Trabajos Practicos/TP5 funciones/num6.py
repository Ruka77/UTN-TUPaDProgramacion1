def tabla_multiplicar(num):
    for i in range(11):
        print(num ," x ", i ," = ", num * i)

def main():
    numero = int(input("Ingrese el numero a mostrar su tabla\n"">> "))
    tabla_multiplicar(numero)

if __name__ == "__main__":
    main()