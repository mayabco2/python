n = input("Ingrese una palabra: ")
cadena = str(n)
cadena_inversa = cadena[::-1]
print(cadena_inversa)
if cadena == cadena_inversa:
    print("Es un palindromo")
else:
    print("No es un palindromo")
