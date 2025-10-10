""" Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
una temperatura en grados Celsius y devuelva su equivalente en
Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
resultado usando la función. """

def celsius_a_fahrenheit(celsius):
    f = (celsius * 9/5) + 32
    return f

def main():
    celsius = float(input("Ingrese la temperatura en celsius\n"">> "))
    fahrenheit = celsius_a_fahrenheit(celsius)
    print(f"La temperatura ingresada en fahrenheit es: {fahrenheit:.1f}°")

if __name__ == "__main__":
    main()
