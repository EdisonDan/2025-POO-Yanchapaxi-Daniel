def calcular_promedio_temperaturas(datos):

    promedios = {}

    for ciudad, semanas in datos.items():
        suma_temperaturas = sum(dia["temp"] for semana in semanas for dia in semana)
        total_dias = sum(len(semana) for semana in semanas)
        promedio = suma_temperaturas / total_dias
        promedios[ciudad] = f"{promedio:.2f}°C"
    print()
    return promedios


# Ejemplo de uso con datos
ciudades = ["Quito", "Guayaquil", "Cuenca"]
temperaturas = {
    "Quito": [
        [  # Semana 1
            {"day": "Lunes", "temp": 14},
            {"day": "Martes", "temp": 15},
            {"day": "Miércoles", "temp": 14},
            {"day": "Jueves", "temp": 16},
            {"day": "Viernes", "temp": 15},
            {"day": "Sábado", "temp": 14},
            {"day": "Domingo", "temp": 13}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 15},
            {"day": "Martes", "temp": 16},
            {"day": "Miércoles", "temp": 15},
            {"day": "Jueves", "temp": 17},
            {"day": "Viernes", "temp": 16},
            {"day": "Sábado", "temp": 14},
            {"day": "Domingo", "temp": 13}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 14},
            {"day": "Martes", "temp": 15},
            {"day": "Miércoles", "temp": 14},
            {"day": "Jueves", "temp": 15},
            {"day": "Viernes", "temp": 16},
            {"day": "Sábado", "temp": 15},
            {"day": "Domingo", "temp": 14}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 13},
            {"day": "Martes", "temp": 14},
            {"day": "Miércoles", "temp": 15},
            {"day": "Jueves", "temp": 16},
            {"day": "Viernes", "temp": 15},
            {"day": "Sábado", "temp": 14},
            {"day": "Domingo", "temp": 13}
        ],
    ],
    "Guayaquil": [
        [  # Semana 1
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 29},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 30},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 28}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 27},
            {"day": "Martes", "temp": 28},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 31},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 28}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 29},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 30},
            {"day": "Sábado", "temp": 28},
            {"day": "Domingo", "temp": 27}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 29},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 31},
            {"day": "Jueves", "temp": 32},
            {"day": "Viernes", "temp": 30},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 28}
        ],
    ],
    "Cuenca": [
        [  # Semana 1
            {"day": "Lunes", "temp": 18},
            {"day": "Martes", "temp": 19},
            {"day": "Miércoles", "temp": 18},
            {"day": "Jueves", "temp": 17},
            {"day": "Viernes", "temp": 18},
            {"day": "Sábado", "temp": 19},
            {"day": "Domingo", "temp": 18}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 19},
            {"day": "Martes", "temp": 18},
            {"day": "Miércoles", "temp": 17},
            {"day": "Jueves", "temp": 18},
            {"day": "Viernes", "temp": 19},
            {"day": "Sábado", "temp": 18},
            {"day": "Domingo", "temp": 17}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 17},
            {"day": "Martes", "temp": 18},
            {"day": "Miércoles", "temp": 17},
            {"day": "Jueves", "temp": 16},
            {"day": "Viernes", "temp": 17},
            {"day": "Sábado", "temp": 18},
            {"day": "Domingo", "temp": 17}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 18},
            {"day": "Martes", "temp": 19},
            {"day": "Miércoles", "temp": 18},
            {"day": "Jueves", "temp": 17},
            {"day": "Viernes", "temp": 18},
            {"day": "Sábado", "temp": 19},
            {"day": "Domingo", "temp": 18}
        ],
    ]
}
# Llamada a la función y muestra de resultados
resultado = calcular_promedio_temperaturas(temperaturas)
print(resultado)