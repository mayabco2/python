'''Crear un programa que cree un programa de ajedrez 
de tamaño variable'''

n = int(input('Ingrese la dimensión: '))
for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0:
            print('#', end=' ')
        else:
            print(' ', end=' ')
    print(' ')

