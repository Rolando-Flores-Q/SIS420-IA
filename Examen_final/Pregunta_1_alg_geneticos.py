import random

# Parámetros del algoritmo genético
num_individuos = 50  # Número de individuos en cada generación
num_tareas = 10  # Número de tareas del proyecto
num_generaciones = 100  # Número de generaciones a evolucionar
prob_mutacion = 0.1  # Probabilidad de mutación

# Datos del problema (duraciones y requerimientos de recursos de las tareas)
duraciones = [3, 2, 4, 5, 3, 4, 2, 3, 4, 5]  # Duración estimada de cada tarea
recursos = [2, 1, 3, 2, 1, 2, 1, 2, 3, 2]  # Requerimientos de recursos de cada tarea

# Generar la población inicial
poblacion = []
for _ in range(num_individuos):
    individuo = [random.randint(0, 1) for _ in range(num_tareas)]  # Generar un individuo aleatorio
    poblacion.append(individuo)

# Función de aptitud (tiempo total de finalización del proyecto)
def aptitud(individuo):
    tiempo_total = max(sum(d * x for d, x in zip(duraciones, individuo)), max(duraciones))  # Calcular el tiempo total de finalización del proyecto
    return -tiempo_total  # Negativo para maximizar la aptitud (minimizar el tiempo total)

# Algoritmo genético
for generacion in range(num_generaciones):
    # Evaluar la aptitud de cada individuo en la población
    aptitudes = [aptitud(individuo) for individuo in poblacion]

    # Seleccionar individuos para reproducción (ruleta)
    padres = []
    total_aptitudes = sum(aptitudes)
    probabilidades = [aptitud / total_aptitudes for aptitud in aptitudes]
    for _ in range(num_individuos):
        padre = random.choices(poblacion, weights=probabilidades)[0]  # Selección de un individuo basado en la aptitud (ruleta)
        padres.append(padre)

    # Operador de recombinación (cruce)
    hijos = []
    for i in range(0, num_individuos, 2):
        padre1 = padres[i]
        padre2 = padres[i + 1]
        punto_cruce = random.randint(1, num_tareas - 1)  # Punto de cruce aleatorio
        hijo1 = padre1[:punto_cruce] + padre2[punto_cruce:]  # Recombinación de los genes de los padres
        hijo2 = padre2[:punto_cruce] + padre1[punto_cruce:]
        hijos.extend([hijo1, hijo2])  # Agregar los hijos a la nueva generación

    # Operador de mutación
    for individuo in hijos:
        for i in range(num_tareas):
            if random.random() < prob_mutacion:  # Aplicar la mutación con una probabilidad dada
                individuo[i] = 1 - individuo[i]  # Mutar un gen cambiándolo de 0 a 1 o viceversa

    # Reemplazar la población anterior con los hijos
    poblacion = hijos

# Encontrar el individuo con el menor tiempo total de finalización
mejor_individuo = max(poblacion, key=aptitud)
mejor_tiempo = -aptitud(mejor_individuo)

print("Mejor asignación de recursos encontrada: ", mejor_individuo)
print("Menor tiempo total de finalización encontrado: ", mejor_tiempo)
