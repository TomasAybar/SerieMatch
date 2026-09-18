import json
import os
import random

CARPETA_SALIDA = "datos/generados"

GENEROS = ["Ciencia Ficción", "Acción", "Comedia", "Drama", "Fantasía"]
PLATAFORMAS = ["Netflix", "HBO Max", "Disney+", "Prime Video", "Apple TV+"]

def generar(n: int) -> None:
    series = [
        {
            "id": i,
            "titulo": f"Serie {i}",
            "generos": [random.choice(GENEROS)],
            "duracion_min": random.randint(20, 60),
            "puntuacion": round(random.uniform(1.0, 10.0), 1),
            "plataforma": random.choice(PLATAFORMAS),
            "sinopsis": "Sinopsis de prueba generada automáticamente.",
        }
        for i in range(n)
    ]
    os.makedirs(CARPETA_SALIDA, exist_ok=True)
    ruta = f"{CARPETA_SALIDA}/series_{n}.json"
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(series, archivo, ensure_ascii=False, indent=2)
    print(ruta)

if __name__ == "__main__":
    for n in (100, 1_000, 10_000, 100_000):
        generar(n)
