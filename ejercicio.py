numero = int(input())

if numero < 0:
    print("El número es negativo")
elif numero == 0:
    print("El número es cero")
elif numero > 0 and numero >= 10 and numero <= 20:
    print("El número es positivo y esta entre 10 y 20")
elif numero > 0 and numero >= 20:
    print("El número es positivo y es mayor a 20")
elif numero > 0:
    print("El número es positivo")