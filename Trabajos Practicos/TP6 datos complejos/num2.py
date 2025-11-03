precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}

def main():
    precios_frutas.update({'naranja': 1200, "manzana": 1500, "pera": 2300})
    precios_frutas["Banana"] = 1330
    precios_frutas["manzana"] = 1700
    precios_frutas["Melón"] = 2800
    print(precios_frutas)

if __name__ == "__main__":
    main()