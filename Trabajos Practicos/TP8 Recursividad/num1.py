def factorial(num):
    if num == 0:
        return 1
    num = num * factorial(num - 1)
    return num

def main():
    num = int(input("Indica el numero a calcular su factorial\n"">> "))
    print(factorial(num))

if __name__ == "__main__":
    main()