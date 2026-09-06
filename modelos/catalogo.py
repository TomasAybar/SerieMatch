# class Catalogo {
#             -series: list
#             +__init__()
#             +cargar_datos(ruta_archivo)
#             +buscar_por_titulo(titulo) Serie
#             +obtener_ranking() list
#             +filtrar_series(criterios) list
#         }


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

    # +buscar_por_titulo(titulo) Serie
    def buscar_por_titulo(self, titulo):
        print(f'bucando serie con el titulo... "{titulo}"')
        # agregar logica de recorrer self series y devolver series que coincidan con el titulo recibido

    # +obtener_ranking() list
    def obtener_ranking(self):
        print("Obteniendo ranking de series..")
        return []
        # agregar logica de ordernar series por puntuacion y retornar lista

    # +filtrar_series(criterios) list
    def filtrar_series(self):
        print("Filtrando seriess..")
        return []
        # agregar logica de aplicar filtros sobre series y devolver resultados
