import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

num_mode = mode(numeros_aleatorios)
num_median = median(numeros_aleatorios)
num_mean = mean(numeros_aleatorios)

print(f"La moda es: {num_mode}")
print(f"La mediana es: {num_median}")
print(f"La media es: {num_mean}")

if num_mean > num_median and num_median > num_mode:
    print("Se encuentra un sesgo positivo o a la derecha")
elif num_mean < num_median and num_median < num_mode:
    print("Se encuentra un sesgo negativo")
else:
    print("Sin sesgo")