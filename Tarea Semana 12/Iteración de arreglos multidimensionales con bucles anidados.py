# Definimos la matriz 3D: [ciudades][semanas][días]
# Supongamos 3 ciudades, 2 semanas, 7 días por semana
temperaturas = [
    [  # Ciudad 1: México
        [  # Semana 1
            22, 23, 21, 24, 25, 22, 23  # Lunes a Domingo
        ],
        [  # Semana 2
            23, 24, 22, 25, 26, 23, 24
        ]
    ],
    [  # Ciudad 2: Bogotá
        [  # Semana 1
            18, 17, 19, 18, 20, 19, 17
        ],
        [  # Semana 2
            19, 18, 20, 19, 21, 20, 18
        ]
    ],
    [  # Ciudad 3: Lima
        [  # Semana 1
            20, 21, 20, 22, 21, 20, 21
        ],
        [  # Semana 2
            21, 22, 21, 23, 22, 21, 22
        ]
    ]
]

# Nombres de las ciudades para mostrar resultados
ciudades = ["México", "Bogotá", "Lima"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Calcular y mostrar promedios usando bucles anidados
for i in range(len(temperaturas)):  # Iterar sobre ciudades
    print(f"\nCiudad: {ciudades[i]}")
    for j in range(len(temperaturas[i])):  # Iterar sobre semanas
        suma_temperaturas = 0
        for k in range(len(temperaturas[i][j])):  # Iterar sobre días
            suma_temperaturas += temperaturas[i][j][k]
        # Calcular promedio
        promedio = suma_temperaturas / len(temperaturas[i][j])
        print(f"  Semana {j+1}: Promedio de temperatura = {promedio:.1f}°C")