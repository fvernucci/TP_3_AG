'''
Problema
1. Hay 5 casas.
2. El Matematico vive en la casa roja.
3. El hacker programa en Python.
4. El Brackets es utilizado en la casa verde.
5. El analista usa Atom.
6. La casa verde esta a la derecha de la casa blanca.
7. La persona que usa Redis programa en Java
8. Cassandra es utilizado en la casa amarilla
9. Notepad++ es usado en la casa del medio.
10. El Desarrollador vive en la primer casa.
11. La persona que usa HBase vive al lado de la que programa en JavaScript.
12. La persona que usa Cassandra es vecina de la que programa en C#.
13. La persona que usa Neo4J usa Sublime Text.
14. El Ingeniero usa MongoDB.
15. EL desarrollador vive en la casa azul.

¿Quien usa vim?
'''
import random
import time

# Variables globales
colores = ["Roja", "Verde", "Blanca", "Amarilla", "Azul"]
profesiones = ["Matemático", "Hacker", "Analista", "Desarrollador", "Ingeniero"]
lenguajes = ["Python", "Java", "JavaScript", "C#", "C++"]
bases_de_datos = ["Redis", "Cassandra", "HBase", "MongoDB", "Neo4J"]
editores = ["Brackets", "Atom", "Notepad++", "Sublime Text", "Vim"]

# Restricciones
RESTRICCIONES = [
    lambda h: h['Profesion'][h['Color'].index('Roja')] == 'Matemático',
    lambda h: h['Lenguaje'][h['Profesion'].index('Hacker')] == 'Python',
    lambda h: h['Editor'][h['Color'].index('Verde')] == 'Brackets',
    lambda h: h['Editor'][h['Profesion'].index('Analista')] == 'Atom',
    lambda h: h['Color'].index('Verde') == h['Color'].index('Blanca') + 1,
    lambda h: h['Lenguaje'][h['Bases_de_datos'].index('Redis')] == 'Java',
    lambda h: h['Bases_de_datos'][h['Color'].index('Amarilla')] == 'Cassandra',
    lambda h: h['Editor'][2] == 'Notepad++',
    lambda h: h['Profesion'].index('Desarrollador') == 0,
    lambda h: abs(h['Bases_de_datos'].index('HBase') - h['Lenguaje'].index('JavaScript')) == 1,
    lambda h: abs(h['Bases_de_datos'].index('Cassandra') - h['Lenguaje'].index('C#')) == 1,
    lambda h: h['Editor'][h['Bases_de_datos'].index('Neo4J')] == 'Sublime Text',
    lambda h: h['Profesion'][h['Color'].index('Azul')] == 'Desarrollador'
]

# Punto 1: Identificar y diseñar un individuo

def generar_individuo_aleatorio():
    individuo = {
        'Color': random.sample(colores, len(colores)),
        'Profesion': random.sample(profesiones, len(profesiones)),
        'Lenguaje': random.sample(lenguajes, len(lenguajes)),
        'Bases_de_datos': random.sample(bases_de_datos, len(bases_de_datos)),
        'Editor': random.sample(editores, len(editores))
    }
    return individuo

# Punto 2: Proponer un método para la generación de individuos. Poblar el universo de individuos iniciales
tamaño_poblacion = 2000
poblacion_inicial = [generar_individuo_aleatorio() for _ in range(tamaño_poblacion)]

# Función de evaluación de aptitud
def calcular_aptitud(individuo):
    return sum(1 for restriccion in RESTRICCIONES if restriccion(individuo))

# Punto 3: A partir del código/estructura provista

# a. Implementar el operador Selección (por aptitud)
def seleccion_por_aptitud(poblacion, n):
    poblacion_ordenada = sorted(poblacion, key=calcular_aptitud, reverse=True)
    seleccionados = poblacion_ordenada[:n]
    return seleccionados

# b. Implementar el operador Cruzamiento (cruzamiento simple)
def cruzamiento_simple(padre1, padre2):
    hijo = {}
    for atributo in padre1:
        hijo[atributo] = padre1[atributo] if random.random() < 0.5 else padre2[atributo]
    return hijo

# c. Implementar el operador Mutación
def mutacion_por_numero_aleatorio(individuo):
    atributo_aleatorio = random.choice(list(individuo.keys()))
    nuevo_valor = random.choice([valor for valor in individuo[atributo_aleatorio] if valor != individuo[atributo_aleatorio]])
    individuo[atributo_aleatorio] = nuevo_valor

# 4. Implementar condiciones de corte para el algoritmo genético
def condicion_corte(iteracion_actual, tiempo_inicial, max_iteraciones, max_tiempo, umbral_aptitud):
    tiempo_transcurrido = time.time() - tiempo_inicial
    if iteracion_actual >= max_iteraciones:
        return True, "Cantidad de iteraciones alcanzada"
    elif tiempo_transcurrido >= max_tiempo:
        return True, "Tiempo transcurrido alcanzado"
    elif calcular_aptitud(poblacion_inicial[0]) >= umbral_aptitud:
        return True, "Valor de 𝐹(𝑥) mayor o igual al umbral"
    return False, ""


# Algoritmo genético para encontrar al usuario de Vim
def algoritmo_genetico():
    maximo_generaciones = 1000
    poblacion_actual = poblacion_inicial.copy()  # Hacer una copia de la población inicial

    for generacion in range(maximo_generaciones):
        nueva_poblacion = []

        # Evaluar la aptitud de cada individuo en la población actual
        for individuo in poblacion_actual:
            individuo['aptitud'] = calcular_aptitud(individuo)

        # Comprobar si se ha encontrado al usuario de Vim
        usuario_vim = next((ind for ind in poblacion_actual if 'Vim' in ind['Editor']), None)
        if usuario_vim:
            return usuario_vim

        # Seleccionar padres, realizar cruce y mutación para crear la siguiente generación
        while len(nueva_poblacion) < tamaño_poblacion:
            padres = random.sample(poblacion_actual, 2)
            descendencia = cruzamiento_simple(padres[0], padres[1])
            mutacion_por_numero_aleatorio(descendencia)
            nueva_poblacion.append(descendencia)

        poblacion_actual = nueva_poblacion

        # Agregar condiciones de corte
        condicion, motivo = condicion_corte(generacion, tiempo_inicial, max_iteraciones, max_tiempo, umbral_aptitud)
        if condicion:
            print(f"Condición de corte: {motivo}")
            break

    return None

# Resolver el acertijo utilizando el algoritmo genético
max_iteraciones = 1000
max_tiempo = 60  # segundos
umbral_aptitud = len(RESTRICCIONES)
tiempo_inicial = time.time()

solucion = algoritmo_genetico()

if solucion:
    usuario_vim = solucion['Profesion'][solucion['Editor'].index('Vim')]
    print(f"El usuario de Vim es {usuario_vim}")
else:
    print("No se encontró una solución")
