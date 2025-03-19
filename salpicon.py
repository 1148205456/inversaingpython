# Lista para almacenar las frutas
frutas = []

# Ingreso de 10 frutas con su precio
for i in range(10):
    nombre = input(f"Ingrese el nombre de la fruta {i+1}: ")
    precio = float(input(f"Ingrese el precio de {nombre}: "))
    frutas.append({"nombre": nombre, "precio": precio})

# Ordenamiento para ordenar de mayor a menor precio
for i in range(len(frutas) - 1):
    for j in range(len(frutas) - 1 - i):
        if frutas[j]["precio"] < frutas[j + 1]["precio"]:
            frutas[j], frutas[j + 1] = frutas[j + 1], frutas[j]

# Mostrar frutas ordenadas
print("\nFrutas ordenadas de mayor a menor precio:")
for fruta in frutas:
    print(f"nombre: {fruta['nombre']}, precio: ${fruta['precio']:.2f}")