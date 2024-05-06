n = int(input("Introduce un número entero: "))
if n >= 0:
    for i in range(n, 0, -1):
        print(i, end=", ")