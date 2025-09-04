contraseña = str(input("Ingrese una contraseña\n"">> "))

if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Contraseña válida")
else:
    print("Contraseña inválida, porfavor ingrese una contraseña entre 8 y 14 caracteres")