numero = input("Introduzca un número entero: ")
numero = int(numero)

if numero % 2 == 0:
    print(f"El numero {numero} es par")
else:
    print(f"El numero {numero} es impar")

numero = int(input("Número: "))
if (numero % 2 == 0) and (numero > 10):
    print("El número es par y mayor que 10")
elif (numero % 2 == 0) and (numero < 10):
    print("El número es par y menor que 10")
else:
    print("El número es impar")