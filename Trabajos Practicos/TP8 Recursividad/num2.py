def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def main():
    pos = int(input("Ingrese la posición hasta donde quiere mostrar la serie\n"">> "))
    print(f"Serie de Fibonacci hasta la posición {pos}:")
    for i in range(pos + 1):
        print(fibonacci(i))

if __name__ == "__main__":
    main()

