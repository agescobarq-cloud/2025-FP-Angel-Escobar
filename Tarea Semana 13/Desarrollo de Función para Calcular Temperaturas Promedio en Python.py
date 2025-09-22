# Definimos la matriz 3D: [ciudades][semanas][días]
# Supongamos 3 ciudades, 4 semanas, 7 días por semana
temperaturas = [
    [  # Ciudad 1: México
        [22, 23, 21, 24, 25, 22, 23],  # Semana 1
        [23, 24, 22, 25, 26, 23, 24],  # Semana 2
        [21, 22, 20, 23, 24, 21, 22],  # Semana 3
        [24, 25, 23, 26, 27, 24, 25]  # Semana 4
    ],
    [  # Ciudad 2: Bogotá
        [18, 17, 19, 18, 20, 19, 17],  # Semana 1
        [19, 18, 20, 19, 21, 20, 18],  # Semana 2
        [17, 16, 18, 17, 19, 18, 16],  # Semana 3
        [20, 19, 21, 20, 22, 21, 19]  # Semana 4
    ],
    [  # Ciudad 3: Lima
        [20, 21, 20, 22, 21, 20, 21],  # Semana 1
        [21, 22, 21, 23, 22, 21, 22],  # Semana 2
        [19, 20, 19, 21, 20, 19, 20],  # Semana 3
        [22, 23, 22, 24, 23, 22, 23]  # Semana 4
    ]
]

# Nombres de las ciudades para mostrar resultados
ciudades = ["México", "Bogotá", "Lima"]


# Función para calcular la temperatura promedio de cada ciudad
def calcular_promedio_ciudad(temperaturas, ciudades):
    """
    Calcula la temperatura promedio de cada ciudad durante todas las semanas.

    Args:
        temperaturas (list): Lista 3D con datos [ciudades][semanas][días]
        ciudades (list): Lista con nombres de las ciudades

    Returns:
        dict: Diccionario con nombres de ciudades y sus promedios
    """
    promedios = {}  # Diccionario para almacenar los promedios por ciudad

    for i in range(len(temperaturas)):  # Iterar sobre cada ciudad
        suma_total = 0  # Acumulador para la suma de temperaturas
        dias_totales = 0  # Contador para el total de días

        for j in range(len(temperaturas[i])):  # Iterar sobre cada semana de la ciudad
            for k in range(len(temperaturas[i][j])):  # Iterar sobre cada día de la semana
                suma_total += temperaturas[i][j][k]  # Sumar la temperatura del día
                dias_totales += 1  # Incrementar el contador de días

        # Calcular promedio para la ciudad (suma total dividida por número de días)
        promedio = suma_total / dias_totales if dias_totales > 0 else 0
        promedios[ciudades[i]] = round(promedio, 1)  # Almacenar promedio redondeado

    return promedios  # Devolver diccionario con promedios


# Calcular y mostrar promedios
resultados = calcular_promedio_ciudad(temperaturas, ciudades)  # Llamar a la función
for ciudad, promedio in resultados.items():  # Iterar sobre el diccionario de resultados
    print(f"Ciudad: {ciudad}, Promedio de temperatura = {promedio}°C")  # Mostrar promedio por ciudad