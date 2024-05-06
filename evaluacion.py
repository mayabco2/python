'''Escribir un programa que almacena en una lista los siguientes precios
8, 22, 46, 50, 65, 75, 80
y muestre por pantalla el menor y el mayor de los precios'''
precios = [8, 22, 46, 50, 65, 75, 80]
precio_minimo = precios[0]
precio_maximo = precios[-1]
for precio in precios:
    if precio < precio_minimo:
        precio_minimo = precio
    elif precio > precio_maximo:
        precio_maximo = precio
print(f"El mínimo es: {precio_minimo}")
print(f"El máximo es: {precio_maximo}")


