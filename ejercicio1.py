nombre = [str(input("¿Cúal es su nombre? "))]
sexo = str(input("¿Cúal es su sexo? "))

if sexo == "mujer" and nombre[0].lower() < "m":
    print("Grupo A")
elif sexo == "hombre" and nombre[0].lower() > "n":
    print("Grupo A")
else:
    print("Grupo B")