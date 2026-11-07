
from collections import deque


class GrafoSeries:
    """Grafo no dirigido que conecta series por géneros compartidos."""

    def __init__(self):
        self.adyacencia = {}
        self.generos_por_serie = {}
        self.titulos_por_id = {}
        self.nombres_genero = {}

    def agregar_vertice(self, serie):
        """Agrega una serie utilizando su ID como identificador."""
        id_serie = serie.id

        if id_serie not in self.adyacencia:
            self.adyacencia[id_serie] = set()

        self.titulos_por_id[id_serie] = serie.titulo

    def agregar_arista(self, id1, id2):
        """Conecta dos series en ambas direcciones."""
        if id1 in self.adyacencia and id2 in self.adyacencia:
            if id1 != id2:
                self.adyacencia[id1].add(id2)
                self.adyacencia[id2].add(id1)

    def construir_desde_catalogo(self, series):
        """Construye el grafo conectando series por sus géneros."""
        self.adyacencia = {}
        self.generos_por_serie = {}
        self.titulos_por_id = {}
        self.nombres_genero = {}

        por_genero = {}

        for serie in series:
            self.agregar_vertice(serie)

            id_serie = serie.id

            generos = set()
            for genero in serie.generos:
                normalizado = genero.strip().lower()
                generos.add(normalizado)
                self.nombres_genero.setdefault(normalizado, genero.strip())

            self.generos_por_serie[id_serie] = generos

            for genero in generos:
                por_genero.setdefault(genero, []).append(id_serie)

        for ids in por_genero.values():
            for i in range(len(ids)):
                for j in range(i + 1, len(ids)):
                    self.agregar_arista(ids[i], ids[j])

    def _buscar_ids(self, titulo):
        """Busca series por ID o por título."""

        if isinstance(titulo, int):
            if titulo in self.titulos_por_id:
                return [titulo]
            return []
        
        return [
            id_serie
            for id_serie, nombre in self.titulos_por_id.items()
            if nombre.lower() == titulo.strip().lower()
        ]

    def existe_serie(self, titulo):
        """Indica si hay al menos una serie con ese título (o ID) en el grafo."""
        return bool(self._buscar_ids(titulo))

    def obtener_vecinos(self, titulo):
        """Devuelve las series relacionadas sin repetir títulos."""
        
        ids_origen = self._buscar_ids(titulo)
        ids_vecinos = set()

        for id_serie in ids_origen:
            ids_vecinos.update(self.adyacencia[id_serie])

        #Excluimos los registros que corresponden a la serie buscada.
        ids_vecinos.difference_update(ids_origen)

        #Evitamos mostrar títulos repetidos.
        titulos = {
            self.titulos_por_id[id_serie]
            for id_serie in ids_vecinos
        }

        return sorted(titulos, key=str.lower)

    def obtener_generos_compartidos(self, serie1, serie2):
        """Devuelve los géneros compartidos entre dos títulos."""
        ids1 = self._buscar_ids(serie1)
        ids2 = self._buscar_ids(serie2)

        compartidos = set()

        for id1 in ids1:
            for id2 in ids2:
                compartidos.update(
                    self.generos_por_serie[id1]
                    & self.generos_por_serie[id2]
                )

        return [self.nombres_genero[genero] for genero in sorted(compartidos)]

    def recorrido_bfs(self, origen):
        """Realiza un recorrido en amplitud."""
        ids_origen = self._buscar_ids(origen)

        if not ids_origen:
            return []

        visitados = set(ids_origen)
        cola = deque(ids_origen)
        resultado = []

        while cola:
            actual = cola.popleft()
            resultado.append(self.titulos_por_id[actual])

            vecinos = sorted(
                self.adyacencia[actual],
                key=lambda i: (self.titulos_por_id[i].lower(), i)
            )

            for vecino in vecinos:
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(vecino)

        return resultado

    def recorrido_dfs(self, origen):
        """Realiza un recorrido en profundidad."""
        ids_origen = self._buscar_ids(origen)

        if not ids_origen:
            return []

        visitados = set()
        resultado = []
        pila = list(reversed(ids_origen))

        while pila:
            actual = pila.pop()

            if actual not in visitados:
                visitados.add(actual)
                resultado.append(self.titulos_por_id[actual])

                vecinos = sorted(
                    self.adyacencia[actual],
                    key=lambda i: (self.titulos_por_id[i].lower(), i),
                    reverse=True
                )

                for vecino in vecinos:
                    if vecino not in visitados:
                        pila.append(vecino)

        return resultado
