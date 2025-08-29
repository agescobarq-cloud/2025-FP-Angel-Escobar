# Definir una matriz bidimensional 3x3
matriz = [
    [9, 2, 7],
    [4, 8, 1],
    [6, 3, 5]
]

# Función para ordenar una fila específica usando Bubble Sort
def ordenar_fila(matriz, fila_idx):
    n = len(matriz[fila_idx])
    # Bubble Sort
    for i in range(n):
        for j in range(0, n - i - 1):
            if matriz[fila_idx][j] > matriz[fila_idx][j + 1]:
                # Intercambiar elementos
                matriz[fila_idx][j], matriz[fila_idx][j + 1] = matriz[fila_idx][j + 1], matriz[fila_idx][j]

# Mostrar matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Ordenar la fila 1 (índice 1)
fila_a_ordenar = 1
ordenar_fila(matriz, fila_a_ordenar)

# Mostrar matriz con la fila ordenada
print(f"\nMatriz con la fila {fila_a_ordenar} ordenada:")
for fila in matriz:
    print(fila)