class Usuario:
    """Representa a un usuario de SerieMatch y sus preferencias."""

    def __init__(self, nombre: str, edad: int):
        self._nombre = nombre
        self._edad = edad
        self._generos_favoritos = []
        self._series_vistas = []

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def edad(self) -> int:
        return self._edad

    @property
    def generos_favoritos(self) -> list:
        return self._generos_favoritos

    @property
    def series_vistas(self) -> list:
        return self._series_vistas

    def agregar_serie_vista(self, serie) -> None:
        """Registra una serie como vista por el usuario."""
        if serie not in self._series_vistas:
            self._series_vistas.append(serie)

    def agregar_genero_favorito(self, genero: str) -> None:
        """Agrega un género a la lista de favoritos del usuario."""
        if genero not in self._generos_favoritos:
            self._generos_favoritos.append(genero)

    def __repr__(self) -> str:
        return f"Usuario: {self._nombre} ({self._edad} años) · {len(self._series_vistas)} series vistas"
