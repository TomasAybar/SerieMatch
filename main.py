from estructuras.arbol_binario import ArbolBST
from modelos.catalogo import Catalogo
from ui.consola import ConsolaUI
from estructuras.grafo import GrafoSeries


def main():

    
    mi_catalogo = Catalogo()

    mi_catalogo.cargar_datos(ruta_archivo="datos/series.json")
    grafo = GrafoSeries()
    grafo.construir_desde_catalogo(mi_catalogo.series)
    
    arbol = ArbolBST()
    app = ConsolaUI(catalogo=mi_catalogo, arbol=arbol, grafo=grafo)

    for serie in mi_catalogo.series:
        arbol.insertar(serie, clave=lambda s: s.titulo.lower())

    app.iniciar_aplicacion()


if __name__ == "__main__":
    main()
