from modelos.catalogo import Catalogo
from ui.consola import ConsolaUI
from estructuras.arbol_binario import ArbolBST


def main():
    mi_catalogo = Catalogo()
    mi_catalogo.cargar_datos(ruta_archivo="datos/series.json")

    arbol = ArbolBST()
    for serie in mi_catalogo.series:
        arbol.insertar(serie, clave=lambda s: s.titulo.lower())

    app = ConsolaUI(catalogo=mi_catalogo, arbol=arbol)
    app.iniciar_aplicacion()


if __name__ == "__main__":
    main()  