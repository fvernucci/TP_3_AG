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


# Punto 1: Identificar y diseñar un individuo

# Función para generar un individuo aleatorio
def generar_individuo_aleatorio():
    individuo = random.sample(colores, len(colores))  # Permutación aleatoria de colores
    individuo.extend(random.sample(profesiones, len(profesiones)))  # Permutación aleatoria de profesiones
    individuo.extend(random.sample(lenguajes, len(lenguajes)))  # Permutación aleatoria de lenguajes
    individuo.extend(random.sample(bases_de_datos, len(bases_de_datos)))  # Permutación aleatoria de bases de datos
    individuo.extend(random.sample(editores, len(editores)))  # Permutación aleatoria de editores
    return individuo

individuo = generar_individuo_aleatorio()
print ("Punto 1:", individuo)


# Punto 2: Proponga un método para la generación de individuos. Poblar el universo de individuos iniciales

tamaño_de_la_poblacion = 50

poblacion_inicial = [generar_individuo_aleatorio() for _ in range(tamaño_de_la_poblacion)]
print ("Punto 2:", poblacion_inicial)

# Punto 3: A partir del código/estructura provista
# a. Implementar el operador Selección
# b. Implementar el operador Cruzamiento
# c. Implementar el operador Mutación

