
from estructuras.avl import ArbolAVL
from estructuras.arbol_general import ArbolGeneral
from estructuras.heap import MaxHeap
from estructuras.grafo import GrafoSeries
from modelos.catalogo import Catalogo
from ui.consola import ConsolaUI


def construir_arbol_categorias(catalogo):
    """Construye un árbol general con jerarquía: Catálogo → Género → Título."""
    arbol = ArbolGeneral()
    arbol.insertar_raiz("Catálogo de Series")

    for serie in catalogo.series:
        for genero in serie.generos:
            nodo_genero = arbol.buscar(genero)
            if nodo_genero is None:
                nodo_genero = arbol.agregar_hijo(arbol.raiz, genero)
            arbol.agregar_hijo(nodo_genero, serie.titulo)

    return arbol


def main():
    mi_catalogo = Catalogo()
    mi_catalogo.cargar_datos(ruta_archivo="datos/series.json")

    # Construcción del grafo
    grafo = GrafoSeries()
    grafo.construir_desde_catalogo(mi_catalogo.series)

    # Construcción del árbol AVL
    avl = ArbolAVL()
    for serie in mi_catalogo.series:
        avl.insertar(serie, clave=lambda s: s.titulo.lower())

    # Construcción del árbol general
    arbol_categorias = construir_arbol_categorias(mi_catalogo)

    # Construcción del Heap para el ranking
    heap_ranking = MaxHeap()
    for serie in mi_catalogo.series:
        heap_ranking.insert(serie)

    # Inicialización de la interfaz
    app = ConsolaUI(
        catalogo=mi_catalogo,
        avl=avl,
        arbol_categorias=arbol_categorias,
        heap_ranking=heap_ranking,
        grafo=grafo,
    )

    app.iniciar_aplicacion()


if __name__ == "__main__":
    main()
