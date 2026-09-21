# class Catalogo {
#             -series: list
#             +__init__()
#             +cargar_datos(ruta_archivo)
#             +buscar_por_titulo(titulo) Serie
#             +obtener_ranking() list
#             +filtrar_series(criterios) list
#         }


import bisect
import json

from modelos.serie import Serie
from utils.adaptadores import normalizar_json_local


class Catalogo:
    def __init__(self):
        # -series: list
        self.series = []

    # metodos

    # +cargar_datos(ruta_archivo)
    def cargar_datos(self, ruta_archivo=None, url_api=None):
        try:
            if ruta_archivo:
                with open(ruta_archivo, "r", encoding="utf-8") as archivo:
                    datos_crudos = json.load(archivo)

                    for item in datos_crudos:
                        datos_limpios = normalizar_json_local(item)

                        nueva_serie = Serie(
                            id=datos_limpios["id"],
                            titulo=datos_limpios["titulo"],
                            generos=datos_limpios["generos"],
                            duracion_min=datos_limpios["duracion_min"],
                            puntuacion=datos_limpios["puntuacion"],
                            plataforma=datos_limpios["plataforma"],
                            sinopsis=datos_limpios["sinopsis"],
                        )

                        self.series.append(nueva_serie)

                print(f"¡Éxito! Se cargaron {len(self.series)} series al catálogo.")

            elif url_api:
                # agregar logica para api si se agrega
                pass

            else:
                print("Error por falta de ruta")

        except FileNotFoundError:
            print(f"[Error] No se encontró el dataset en la ruta: {ruta_archivo}")
        except json.JSONDecodeError:
            print("[Error] El archivo JSON está corrupto o mal formateado.")

    def cargar_desde_json(self, ruta_archivo):
        self.series = []
        self.cargar_datos(ruta_archivo=ruta_archivo)

    def buscar(self, titulo):
        titulo_normalizado = titulo.lower()
        for serie in self.series:
            if serie.titulo.lower() == titulo_normalizado:
                return serie
        return None

    """busqueda secuencial"""
    def buscar_serie_titulo(self):
        

        titulo = input("Ingrese el titulo a buscar: ")
        resultado = None

        for serie in self.series:
            if titulo.lower() in serie.titulo.lower():
                resultado = serie
                break
        if resultado:
            print(resultado)
        else:
            print("No se encontro")
        print("Fin de resultados")

    def filtrar_serie_genero(self):
        genero = input("Ingrese el género a filtrar: ")
        for serie in self.series:
            for g in serie.generos:
                if genero.lower() in g.lower():
                    print(serie)
        print("Fin de resultados")

    def listar_series(self):
        print("\n=== CATÁLOGO DE SERIES ===")

        if not self.series:
            print("No hay series cargadas en el sistema.")
            return

        for serie in self.series:
            print(
                f"[{serie.id}] {serie.titulo} - {serie.plataforma} - {serie.puntuacion}"
            )

    def ordenar_por_titulo(self):
        self.series.sort(key=lambda p: p.titulo.lower())

    """busqueda binaria"""
    def buscar_binaria(self, titulo: str):
        claves = [p.titulo.lower() for p in self.series]
        indice = bisect.bisect_left(claves, titulo.lower())
        if indice < len(claves) and claves[indice] == titulo.lower():
            return self.series[indice]
        return None