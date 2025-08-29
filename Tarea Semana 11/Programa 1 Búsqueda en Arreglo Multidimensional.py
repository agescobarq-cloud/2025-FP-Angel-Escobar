# Definir una matriz bidimensional 3x3
matriz = [
    [4, 7, 1],
    [9, 3, 8],
    [2, 6, 5]
]

# Función para buscar un valor en la matriz
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return True, i, j  # Retorna True y la posición (i,j)
    return False, -1, -1  # Retorna False si no se encuentra

# Valor a buscar
valor_buscado = 6

# Realizar la búsqueda
encontrado, fila, columna = buscar_valor(matriz, valor_buscado)

# Mostrar la matriz
print("Matriz 3x3:")
for fila in matriz:
    print(fila)

# Mostrar resultado de la búsqueda
if encontrado:
    print(f"\nEl valor {valor_buscado} se encontró en la posición ({fila}, {columna})")
else:
    print(f"\nEl valor {valor_buscado} no se encontró en la matriz")