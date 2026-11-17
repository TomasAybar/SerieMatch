class GestorFavoritos:
    """Lista de series favoritas que se guarda en un archivo de texto"""

    def __init__(self, ruta_archivo):
        self.ruta_archivo = ruta_archivo
        self.ids = []

    def cargar(self):
        """Lee los IDs guardados en el .txt"""
        self.ids = []
        try:
            with open(self.ruta_archivo, "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    # Se ignoran líneas vacías o que no sean un número.
                    if linea.isdigit() and int(linea) not in self.ids:
                        self.ids.append(int(linea))
        except FileNotFoundError:
            pass
        return self.ids

    def es_favorito(self, id_serie):
        return id_serie in self.ids

    def agregar(self, id_serie):
        """Agrega un ID al final del .txt"""
        if self.es_favorito(id_serie):
            return False

        with open(self.ruta_archivo, "a", encoding="utf-8") as archivo:
            archivo.write(f"{id_serie}\n")

        self.ids.append(id_serie)
        return True
