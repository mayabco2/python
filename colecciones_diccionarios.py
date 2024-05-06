# Diccionario
telefonos = {
    "Liz": 78787878,
    "Marco": 69686512,
    "Laura": 89895623,
    "Guido": 789554,
    "Mabel": 78562545,
    "Vero": 796454,
    "Claudia": 657932
}
print(type(telefonos))
print(telefonos["Liz"])  # Me muestra el telefono de liz que tenemos en el diccionario, es como una lista

print("Guido" in telefonos)
print("Pedro" not in telefonos)
print("lix" in telefonos)

# "Liz": 78787878
# clave   valor

for clave, valor in telefonos.items():
    print(f"Clave: {clave}   Valor: {valor}")