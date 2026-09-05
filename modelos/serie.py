class Serie:
    """Representa un elemento del catalogo"""
    def __init__(self, titulo: str, generos: list, duracion_min: int, puntuacion: float, plataforma: str, sinopsis: str):
        self._titulo = titulo
        self._generos = generos
        self._duracion_min = duracion_min
        self._puntuacion = puntuacion
        self._plataforma = plataforma
        self._sinopsis = sinopsis

    @property
    def titulo(self) -> str:
        return self._titulo

    @property
    def generos(self) -> list:
        return self._generos

    @property
    def duracion_min(self) -> int:
        return self._duracion_min

    @property
    def puntuacion(self) -> float:
        return self._puntuacion

    @property
    def plataforma(self) -> str:
        return self._plataforma

    @property
    def sinopsis(self) -> str:
        return self._sinopsis

    def __repr__(self) -> str:
        return f'Serie: {self.titulo} Plataforma: {self.plataforma} ⭐Puntuacion: {self.puntuacion}'