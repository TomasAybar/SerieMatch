from estructuras.grafo import GrafoSeries
from modelos.catalogo import Catalogo


# Cargamos el catálogo real
catalogo = Catalogo()
catalogo.cargar_datos(ruta_archivo="datos/series.json")

# Construimos el grafo con las series del catálogo
grafo = GrafoSeries()
grafo.construir_desde_catalogo(catalogo.series)

# Mostramos la cantidad de series
print("=== GRAFO DE SERIEMATCH ===")
print("Cantidad de series:", len(grafo.adyacencia))

# Elegimos una serie para consultar
if grafo.adyacencia:
    origen = next(iter(grafo.adyacencia))

    print("\nSerie de origen:", origen)

    print("\n=== SERIES RELACIONADAS ===")
    print(grafo.obtener_vecinos(origen))

    print("\n=== RECORRIDO BFS ===")
    print(grafo.recorrido_bfs(origen))

    print("\n=== RECORRIDO DFS ===")
    print(grafo.recorrido_dfs(origen))