# TP_3_AG
Este repositorio contiene una implementación de un algoritmo genético para resolver el enigma de "¿Quién usa Vim?", que involucra a cinco personas, cada una con una profesión, un lenguaje de programación, una base de datos y un editor de código diferente, viviendo en casas de diferentes colores. A continuación, se proporciona una descripción detallada del enigma y la solución propuesta.

Problema:
Se presentan las siguientes restricciones en el enigma:

Hay 5 casas
El Matemático vive en la casa roja
El hacker programa en Python
El Brackets es utilizado en la casa verde
El analista usa Atom
La casa verde está a la derecha de la casa blanca
La persona que usa Redis programa en Java
Cassandra es utilizado en la casa amarilla
Notepad++ es usado en la casa del medio
El Desarrollador vive en la primera casa
La persona que usa HBase vive al lado de la que programa en JavaScript
La persona que usa Cassandra es vecina de la que programa en C#
La persona que usa Neo4J usa Sublime Text
El Ingeniero usa MongoDB
El Desarrollador vive en la casa azul
El objetivo del enigma es determinar quién es la persona que usa Vim

Solución:
Para abordar este problema, se ha implementado un algoritmo genético en Python. A continuación, se describen los componentes clave de la solución:

Generación de Individuos Iniciales: se generan individuos iniciales de manera aleatoria. Cada individuo representa una asignación de profesiones, lenguajes, bases de datos, editores y colores de casas.

Evaluación de Aptitud: se define una función de aptitud que evalúa cuántas restricciones cumple cada individuo. Cuantas más restricciones cumpla, mayor será su aptitud.

Selección por Aptitud: se implementa el operador de selección para elegir a los individuos más aptos de la población actual.

Cruzamiento Simple: se aplica el operador de cruzamiento, que combina a dos individuos para crear descendencia. El cruzamiento es simple y se basa en seleccionar aleatoriamente atributos de ambos padres.

Mutación Aleatoria: se implementa un operador de mutación que elige aleatoriamente un atributo de un individuo y lo modifica de forma aleatoria.

Condiciones de Corte: se establecen tres condiciones de corte para limitar la ejecución del algoritmo. Estas condiciones están relacionadas con el número de iteraciones, el tiempo transcurrido y la aptitud alcanzada.

Algoritmo Genético: el algoritmo genético se ejecuta en un bucle que evalúa la aptitud de la población, selecciona padres, aplica el cruzamiento y la mutación para crear una nueva generación. El proceso continúa hasta que se cumpla alguna de las condiciones de corte.

Resultado: una vez que se encuentra una solución o se alcanzan las condiciones de corte, se muestra el resultado. Se identifica al usuario que usa Vim en función de la solución encontrada.

Ejecución:
Para ejecutar el algoritmo y resolver el enigma, se deben establecer los siguientes parámetros:

max_iteraciones: número máximo de iteraciones permitidas
max_tiempo: tiempo máximo de ejecución en segundos
umbral_aptitud: umbral de aptitud que determina cuántas restricciones deben cumplirse para considerar una solución válida

Para poder ver en funcionamiento del código, correr el “tp3.py".
