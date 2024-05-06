print("Iterador for")
for i in range(1, 11):
    print(i, end=" ")

print("")
print("Iterador while")
limite = 10
i = 1
while(i <= limite):
    print(i, end=" ")
    i += 1

print("")
animales = ["Perro", "Gato", "Alcon", "Caballo"]
indice = 0
while indice < len(animales):
    animal = animales[indice]
    print(f"{indice}.- {animal}")
    indice += 1

# Serie de fibonacci
a, b = 0, 1
limite = 8
while a < limite:
    print(a, end=", ")
    c = a
    a = b
    b = c + b
    # a, b = b, a + b   --> otra forma