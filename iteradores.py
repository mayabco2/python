numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    numero = numero ** 2
    print(numero)

animales = ['Perro', 'Gato', 'Tigre', 'Alcon']
for animal in animales:
    print(animal)

for i in range(len(animales)):
    print(f'{i}.- {animales[i]}') # el i es para indicar las posiciones e imprimir correctamente

for i in range(5, 10):
    print(i)

print("=================")

for i in range(2, 10, 2): #rango con saltos de 2
    print(i)

potencias = [x ** 2 for x in range(1,11)]  #el for en una sola linea
print(potencias) 

lista = [] #ampliando lo de arriba
for x in range(1, 11):
    lista.append(x**2) #append es para agregar un nuevo elemneto  la lista
print(lista)

# Dada una lista de edades mostrar las que son
# Menores de edad y las que son mayores de edad

edades = [3,45,17,33,12,34,22,10,28]

for edad in edades:
    if edad >= 18:
        print(f'{edad} es mayor de edad')
    elif edad >= 5 and edad < 18:
        print(f'{edad} es niña(o)')
    else:
        print(f'{edad} es infante')