terremeto = float(input("Ingrese la magnitud del terremoto\n"">> "))

if terremeto < 3:
    magnitud = "Muy leve, imperceptible"
elif terremeto < 4:
    magnitud = "Leve, ligeramente perceptible"
elif terremeto < 5:
    magnitud = "Moderado, sentido por personas, pero generalmente no causa daños"
elif terremeto < 6:
    magnitud = "Fuerte, puede causar daños en estructuras débiles"
elif terremeto < 7:
    magnitud = "Muy fuerte, puede causar daños significativos"
elif terremeto > 7:
    magnitud = "Extremo, puede causar graves daños a gran escala"
else:
    print("Numero fuera de rango permitido")

print(f"El terremoto fue {magnitud}")