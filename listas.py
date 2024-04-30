impares = [1,3,5,7,9,11,13,15,17,19]
print(type(impares))

print(impares[4])
print(impares[-6])
print(impares[:4]) #del inicio hasta el 4
print(impares[4:]) #desde el 4 hasta el final
print(impares[4:6])
print(impares[-4:-1])

lista_alfanumerica = ['a', 1, 'b', 2, 'c', 3, 'd']
print(lista_alfanumerica)
print(len(lista_alfanumerica)) #para ver cuantos elementos hay se usa el len = longitud
medio = len(lista_alfanumerica) // 2
print(lista_alfanumerica[medio]) #para ver el elemento del medio

impares = [1,3,5,7,9,11,13,15,17,19]
#len() devuelve un valor
tamaño = len(impares)
print(tamaño)
#reverse no devuelve un valor
revertido = impares.reverse()
print(impares)
print(revertido) #como reverse no devuelve un valor aca no sale nada

desordenado = [5,2,6,9,1,3,7]
desordenado.sort()
print(desordenado)

matriz = [
    [1,2,3,4,5],        #posicion 0
    [6,7,8,9,10],       #posicion 1
    [11,12,13,14,15]    #posicion 2
]

print(matriz[1][2])