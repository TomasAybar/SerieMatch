# TP7 - Implementación de Grafos
## 1. Introducción

En esta etapa del proyecto SerieMatch se implementó una estructura de datos de tipo grafo para relacionar las series del catálogo según los géneros que comparten.

El objetivo es permitir que los usuarios puedan descubrir otras series relacionadas con una serie determinada.

### 1.1 ¿Por qué implementar un grafo en SerieMatch?

La consigna permitía no implementar el grafo si el proyecto no lo ameritaba, justificando la decisión. En SerieMatch se decidió implementarlo por los siguientes motivos:

- **La funcionalidad central del proyecto es recomendar.** La pregunta "dada esta serie, ¿cuáles se le parecen?" es una relación entre pares de series, y eso es exactamente lo que modela un grafo.
- **Ninguna de las estructuras anteriores resuelve esa pregunta.** El AVL busca una serie por título, el árbol general agrupa las series por género (cada serie aparece por separado bajo cada uno de sus géneros, sin saber con qué otras comparte varios géneros a la vez) y el heap las ordena por puntuación. Ninguna relaciona una serie con otra.
- **Las relaciones se calculan una sola vez.** Al construir el grafo quedan guardadas las conexiones de cada serie; después, consultar las relacionadas es leer su conjunto de vecinos.
- **Permite medir la afinidad.** Con los géneros compartidos de cada conexión se ordenan las recomendaciones de más a menos parecida (ver sección 6).

Reconocemos también sus límites en el estado actual del proyecto: con 45 series, comparar en cada consulta los géneros de la serie buscada contra todas las demás también respondería de forma instantánea. El grafo no se justifica por rendimiento con este volumen de datos, sino porque representa de forma directa la relación que el proyecto necesita y deja preparada la estructura para un catálogo más grande.

## 2. Representación del grafo

Se implementó un grafo **no dirigido y no ponderado**, utilizando una lista de adyacencia mediante un diccionario de Python.

- **Vértices:** representan las series del catálogo. Cada serie se identifica mediante su ID único, lo que permite diferenciar registros aunque tengan el mismo título.
- **Aristas:** representan las relaciones entre dos series que comparten al menos un género.
- **Adyacencia:** cada vértice almacena un conjunto de los IDs de las series con las que está conectado.

Se eligió un grafo no dirigido porque la relación entre dos series es recíproca: si una serie comparte géneros con otra, la relación existe en ambos sentidos.

Se eligió un grafo no ponderado porque las conexiones solamente indican si dos series comparten al menos un género. No se asigna un peso numérico a las aristas.

### Justificación de la representación

La elección entre lista y matriz de adyacencia depende de la densidad del grafo. Al construirlo con el catálogo real, el grafo resultó **denso**:

| Dato | Valor |
|---|---|
| Vértices (V) | 45 |
| Aristas (E) | 708 |
| Aristas posibles: V·(V−1)/2 | 990 |
| Densidad: E / aristas posibles | 71,5 % |

La densidad es alta porque hay géneros muy amplios: **Drama** aparece en 33 de las 45 series y, por sí solo, conecta a todas ellas entre sí. 33 de las 45 series están conectadas con al menos 32 de las otras 44.

Con esta densidad la diferencia de espacio entre ambas representaciones es chica: una matriz ocuparía 45 × 45 = 2.025 celdas, y la lista de adyacencia guarda 1.416 entradas (cada arista se guarda en los dos vértices). Por lo tanto, **el ahorro de espacio no es el motivo de la elección**.

Aun así se eligió la lista de adyacencia por las operaciones que necesita SerieMatch:

- **Consultar los vecinos de una serie** es la operación principal (recomendaciones, BFS y DFS). Con la lista se recorren solo los vecinos reales; con la matriz habría que recorrer la fila completa de V posiciones.
- **El catálogo es dinámico.** Agregar una serie en la lista es agregar una clave al diccionario; en una matriz hay que agregar una fila y una columna a toda la estructura.
- **Las series se identifican por su ID.** Con un diccionario el ID es directamente la clave. Una matriz necesita índices consecutivos desde 0, por lo que habría que mantener una tabla de traducción ID → índice y actualizarla al agregar o quitar series. Esto ya ocurre en el catálogo actual: al eliminar el registro duplicado de Stranger Things (ver sección 7) quedó libre el ID 18, y el diccionario no necesitó ningún ajuste.
- **Los conjuntos (`set`) evitan aristas duplicadas.** Dos series que comparten varios géneros quedan conectadas una sola vez.

Si el catálogo creciera incorporando géneros más específicos, cada serie se conectaría con una proporción menor del total y la densidad bajaría, lo que haría más clara la ventaja de la lista de adyacencia.

## 3. Implementación

Se creó el archivo `estructuras/grafo.py`, que contiene la clase `GrafoSeries`.

Sus principales métodos son:

- `agregar_vertice()`: incorpora una serie al grafo.
- `agregar_arista()`: establece una conexión entre dos series.
- `construir_desde_catalogo()`: construye automáticamente el grafo utilizando las series y sus géneros.
- `obtener_vecinos()`: devuelve las series relacionadas con una serie determinada.
- `obtener_generos_compartidos()`: identifica los géneros que tienen en común dos series.
- `recorrido_bfs()`: realiza un recorrido en amplitud.
- `recorrido_dfs()`: realiza un recorrido en profundidad.

También se almacena la información de los géneros de cada serie para poder identificar las coincidencias.

## 4. Algoritmos de recorrido

### BFS (Breadth-First Search)

Es un recorrido en amplitud. Utiliza una cola para visitar primero los vértices más cercanos al punto de origen.

En SerieMatch permite recorrer las series relacionadas comenzando por una serie determinada.

### DFS (Depth-First Search)

Es un recorrido en profundidad. Utiliza una pila para explorar un camino hasta donde sea posible antes de regresar y continuar por otro camino.

Ambos algoritmos utilizan un conjunto de vértices visitados para evitar procesar repetidamente una misma serie.

## 5. Integración con el catálogo

El grafo se construye utilizando los datos del archivo `datos/series.json`, a través de la clase `Catalogo`.

Cada serie se identifica mediante su ID y se almacena su título como información descriptiva, junto con sus géneros.

La construcción del grafo se realiza desde `main.py` y se conecta con la interfaz de consola mediante la clase `ConsolaUI`.

Se incorporó una nueva opción en el menú:

**9. Buscar series relacionadas por género.**

Esta opción permite ingresar el título de una serie y consultar las demás series que comparten al menos un género.

La utilización de IDs permite diferenciar registros aunque tengan títulos iguales. En el catálogo actual no hay títulos repetidos, pero el grafo lo soporta: si se busca un título con varios registros, se combinan los vecinos de todos ellos.

## 6. Ordenamiento de recomendaciones

Las series relacionadas se ordenan según la cantidad de géneros compartidos.

Las que tienen más coincidencias aparecen primero. Cuando dos series tienen la misma cantidad de géneros compartidos, se utiliza el orden alfabético como criterio secundario.

Esto permite presentar recomendaciones más relevantes para el usuario.

## 7. Ejemplos de consultas y pruebas realizadas

Se realizaron pruebas utilizando el catálogo real de SerieMatch, que cargó correctamente 45 registros.

Se verificaron:

- La creación de vértices.
- La conexión entre series que comparten géneros.
- La consulta de series relacionadas.
- La identificación de géneros compartidos.
- El recorrido BFS.
- El recorrido DFS.
- El ordenamiento de las recomendaciones.
- La integración del grafo con el menú principal.

Como ejemplo, al buscar **Stranger Things**, el sistema devuelve series relacionadas como Dark, Lost, Severance y Silo, indicando los géneros que comparten.

También se probó la búsqueda de **Breaking Bad**, verificando el funcionamiento de las recomendaciones con otra serie del catálogo.

Se comprobó que no se recomienda la misma serie que se está buscando.

**Corrección del dataset:** durante las pruebas se detectó que *Stranger Things* figuraba dos veces en `datos/series.json` (IDs 3 y 18) con géneros distintos. Se unificó en un único registro: se conservó el ID 3 (puntuación 8.7, 51 min) y se le agregaron los géneros que solo tenía el duplicado (Fantasía y Misterio). El ID 18 quedó libre y no se renumeraron las demás series.

### Salida de consola

Búsqueda de **Stranger Things** desde la opción 9 del menú. Las series aparecen ordenadas por cantidad de géneros compartidos y, ante empate, alfabéticamente:

```
==============================================================
        🎥   BIENVENIDO A SERIEMATCH (CLI Edition)  🎥
==============================================================
1. Registrar usuario
2. Agregar serie
3. Ver series
4. Buscar serie por titulo
5. Dejar reseña
6. Filtrar por género
7. Explorar categorías
8. Ranking de series
9. Buscar series relacionadas por género
0. Salir
Seleccione una opción: 9
Ingrese el titulo de una serie: Stranger Things

=== SERIES RELACIONADAS POR GÉNERO ===
- Dark | Géneros compartidos: Ciencia ficción, Drama, Misterio
- Lost | Géneros compartidos: Ciencia ficción, Drama, Misterio
- Severance | Géneros compartidos: Ciencia ficción, Drama, Misterio
- Silo | Géneros compartidos: Ciencia ficción, Drama, Misterio
- The Haunting of Hill House | Géneros compartidos: Drama, Misterio, Terror
- Wednesday | Géneros compartidos: Fantasía, Misterio, Terror
- Alice in Borderland | Géneros compartidos: Ciencia ficción, Misterio
- Arcane | Géneros compartidos: Ciencia ficción, Fantasía
- Black Mirror | Géneros compartidos: Ciencia ficción, Drama
- Chernobyl | Géneros compartidos: Drama, Misterio
- Game of Thrones | Géneros compartidos: Drama, Fantasía
- House | Géneros compartidos: Drama, Misterio
- House of the Dragon | Géneros compartidos: Drama, Fantasía
- Loki | Géneros compartidos: Ciencia ficción, Fantasía
- Sherlock | Géneros compartidos: Drama, Misterio
- Squid Game | Géneros compartidos: Drama, Misterio
- The Umbrella Academy | Géneros compartidos: Ciencia ficción, Fantasía
- The Walking Dead | Géneros compartidos: Drama, Terror
- The Witcher | Géneros compartidos: Drama, Fantasía
- Better Call Saul | Géneros compartidos: Drama
- Breaking Bad | Géneros compartidos: Drama
- Bridgerton | Géneros compartidos: Drama
- Cobra Kai | Géneros compartidos: Drama
- Euphoria | Géneros compartidos: Drama
- Money Heist | Géneros compartidos: Drama
- Mr. Robot | Géneros compartidos: Drama
- Ozark | Géneros compartidos: Drama
- Peaky Blinders | Géneros compartidos: Drama
- Succession | Géneros compartidos: Drama
- Suits | Géneros compartidos: Drama
- The Bear | Géneros compartidos: Drama
- The Boys | Géneros compartidos: Ciencia ficción
- The Crown | Géneros compartidos: Drama
- The Good Doctor | Géneros compartidos: Drama
- The Last of Us | Géneros compartidos: Drama
- The Mandalorian | Géneros compartidos: Ciencia ficción
- The Queen's Gambit | Géneros compartidos: Drama
- Vikings | Géneros compartidos: Drama
- You | Géneros compartidos: Drama
```

Si el título ingresado no existe en el catálogo, se informa sin mostrar recomendaciones:

```
Seleccione una opción: 9
Ingrese el titulo de una serie: No existe
No se encontró la serie en el catálogo.
```

## 8. Archivos involucrados

- `estructuras/grafo.py`: implementación de la estructura de grafo.
- `algoritmos/probar_grafo.py`: pruebas de funcionamiento del grafo.
- `ui/consola.py`: integración de la búsqueda de series relacionadas en el menú.
- `main.py`: creación del grafo y conexión con el catálogo.
- `modelos/serie.py`: definición de los atributos de las series utilizados por el grafo.

## 9. Conclusión

La implementación del grafo permitió incorporar nuevas relaciones entre las series del catálogo de SerieMatch.

A través de los algoritmos BFS y DFS se pueden realizar recorridos sobre las conexiones, mientras que la búsqueda por géneros compartidos permite generar recomendaciones y ordenarlas según su nivel de coincidencia.

De esta manera, el proyecto incorpora una nueva estructura de datos que amplía sus funcionalidades y permite descubrir relaciones entre los elementos del catálogo.