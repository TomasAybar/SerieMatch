from modelos.catalogo import Catalogo
from ui.consola import ConsolaUI


def main():

    mi_catalogo = Catalogo()
    mi_catalogo.cargar_datos(ruta_archivo="datos/series.json")

    app = ConsolaUI(catalogo=mi_catalogo)

    # Inicio app
    app.iniciar_aplicacion()


if __name__ == "__main__":
    main()
