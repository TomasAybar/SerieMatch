import os
import random
import timeit

import matplotlib.pyplot as plt

from estructuras.heap import MaxHeap
from modelos.catalogo import Catalogo
from modelos.serie import Serie

ruta_cargar_series = "datos/generados/series_"
ruta_guardar_graficos = "docs/capturas"

TOP_N = 5


def construir_heap(series):
    heap = MaxHeap()
    for serie in series:
        heap.insert(serie)
    return heap


def top_n_heap(heap, n):
    """Extrae n veces el máximo y los reinserta para dejar el heap intacto."""
    extraidos = [heap.extract_max() for _ in range(min(n, len(heap.heap)))]
    for serie in extraidos:
        heap.insert(serie)
    return extraidos


def top_n_sorted(series, n):
    return sorted(series, key=lambda s: s.puntuacion, reverse=True)[:n]


def crear_grafico(tamaños, t_sorted, t_heap):
    plt.plot(tamaños, t_sorted, label="sorted (por consulta)", marker="o")
    plt.plot(tamaños, t_heap, label="heap (por consulta)", marker="o")

    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("N elementos")
    plt.ylabel("tiempo (ms)")
    plt.title(f"Top-{TOP_N}: heap vs sorted")
    plt.legend()

    os.makedirs(ruta_guardar_graficos, exist_ok=True)
    destino = f"{ruta_guardar_graficos}/experimento-heap.png"
    plt.savefig(destino, dpi=300)
    print(f"\nGráfico guardado en '{destino}'")
    plt.close()


def main() -> None:
    tamaños = (100, 1_000, 10_000, 100_000)
    tiempos_sorted = []
    tiempos_heap = []

    print(f"Top-{TOP_N} por puntuación\n")
    print("tamaño\tsorted_ms\tconstruir_heap_ms\theap_ms\tinsert_ms\tconsultas_equilibrio")

    for n in tamaños:
        catalogo = Catalogo()
        catalogo.cargar_desde_json(f"{ruta_cargar_series}{n}.json")
        series = catalogo.series

        # Ambos métodos deben devolver las mismas puntuaciones
        heap = construir_heap(series)
        assert [s.puntuacion for s in top_n_heap(heap, TOP_N)] == [
            s.puntuacion for s in top_n_sorted(series, TOP_N)
        ]

        t_construir = min(timeit.repeat(lambda: construir_heap(series), number=1, repeat=3)) * 1000
        t_sorted = min(timeit.repeat(lambda: top_n_sorted(series, TOP_N), number=5, repeat=5)) / 5 * 1000
        t_heap = min(timeit.repeat(lambda: top_n_heap(heap, TOP_N), number=20, repeat=5)) / 20 * 1000

        nueva = Serie(0, "Nueva", ["Drama"], 45, round(random.uniform(0, 10), 1), "X", "")
        t_insert = min(timeit.repeat(lambda: heap.insert(nueva), number=20, repeat=5)) / 20 * 1000

        # Consultas Q a partir de las cuales construir el heap + Q consultas
        # cuesta menos que hacer Q veces sorted
        if t_sorted > t_heap:
            equilibrio = f"{t_construir / (t_sorted - t_heap):.1f}"
        else:
            equilibrio = "nunca"

        tiempos_sorted.append(t_sorted)
        tiempos_heap.append(t_heap)

        print(f"{n}\t{t_sorted:.4f}\t\t{t_construir:.4f}\t\t{t_heap:.4f}\t{t_insert:.4f}\t\t{equilibrio}")

    crear_grafico(tamaños, tiempos_sorted, tiempos_heap)


if __name__ == "__main__":
    main()
