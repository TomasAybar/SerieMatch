# TP7 - Implementación de Grafos
## 1. Introducción

En esta etapa del proyecto SerieMatch se implementó una estructura de datos de tipo grafo para relacionar las series del catálogo según los géneros que comparten.

El objetivo es permitir que los usuarios puedan descubrir otras series relacionadas con una serie determinada.

## 2. Representación del grafo

Se implementó un grafo **no dirigido y no ponderado**, utilizando una lista de adyacencia mediante un diccionario de Python.

- **Vértices:** representan las series del catálogo. Cada serie se identifica mediante su ID único, lo que permite diferenciar registros aunque tengan el mismo título.
- **Aristas:** representan las relaciones entre dos series que comparten al menos un género.
- **Adyacencia:** cada vértice almacena un conjunto de los IDs de las series con las que está conectado.

Se eligió un grafo no dirigido porque la relación entre dos series es recíproca: si una serie comparte géneros con otra, la relación existe en ambos sentidos.

Se eligió un grafo no ponderado porque las conexiones solamente indican si dos series comparten al menos un género. No se asigna un peso numérico a las aristas.

### Justificación de la representación

Se eligió una lista de adyacencia porque permite almacenar únicamente las conexiones existentes entre las series, sin reservar espacio para todas las posibles combinaciones de vértices, como sucedería con una matriz de adyacencia.

Además, resulta adecuada para las operaciones que necesita SerieMatch, como consultar los vecinos de una serie y realizar recorridos BFS y DFS.

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

**7. Buscar series relacionadas por género.**

Esta opción permite ingresar el título de una serie y consultar las demás series que comparten al menos un género.

La utilización de IDs permite conservar registros diferentes aunque tengan títulos iguales.

## 6. Ordenamiento de recomendaciones

Las series relacionadas se ordenan según la cantidad de géneros compartidos.

Las que tienen más coincidencias aparecen primero. Cuando dos series tienen la misma cantidad de géneros compartidos, se utiliza el orden alfabético como criterio secundario.

Esto permite presentar recomendaciones más relevantes para el usuario.

## 7. Ejemplos de consultas y pruebas realizadas

Se realizaron pruebas utilizando el catálogo real de SerieMatch, que cargó correctamente 46 registros.

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

También se probó la búsqueda de **Breaking Bad**, verificando el funcionamiento de las recomendaciones para un título con un único registro.

Se comprobó que los títulos duplicados se conservan como vértices independientes mediante sus IDs y que no se recomienda la misma serie que se está buscando.

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