from estructuras.arbol_binario import ArbolBST
from modelos.catalogo import Catalogo
from ui.consola import ConsolaUI


def main():

    arbol = ArbolBST()

    mi_catalogo = Catalogo(arbol=arbol)
    mi_catalogo.cargar_datos(ruta_archivo="datos/series.json")

    app = ConsolaUI(catalogo=mi_catalogo)

    for serie in mi_catalogo.series:
        arbol.insertar(serie, clave=lambda s: s.titulo.lower())

    app.iniciar_aplicacion()


if __name__ == "__main__":
    main()
