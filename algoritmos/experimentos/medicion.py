import os
import timeit

import matplotlib.pyplot as plt

from estructuras.arbol_binario import ArbolBST
from modelos.catalogo import Catalogo


def medir_arbol(arbol, lista, titulo):
    """Mide la búsqueda en árbol sobre la lista dada."""
    for serie in lista:
        arbol.insertar(serie, clave=lambda s: s.titulo.lower())

    t_arbol = (
        min(
            timeit.repeat(
                lambda: arbol.buscar(titulo.lower(), clave=lambda s: s.titulo.lower()),
                number=20,
                repeat=5,
            )
        )
        / 20
        * 1000
    )

    return t_arbol


def main() -> None:
    arbol = ArbolBST()

    tamanios = (100, 1_000, 10_000, 100_000)
    tiempos_sec = []
    tiempos_arbol = []

    for n in tamanios:
        catalogo = Catalogo(arbol=arbol)
        catalogo.cargar_desde_json(f"datos/generados/series_{n}.json")

        titulo_probe = f"Serie {n - 1}"

        t_sec = (
            min(
                timeit.repeat(
                    lambda: catalogo.buscar(titulo_probe), number=20, repeat=5
                )
            )
            / 20
            * 1000
        )
        t_arbol = medir_arbol(arbol, catalogo.series, titulo_probe)

        tiempos_sec.append(t_sec)
        tiempos_arbol.append(t_arbol)
        print(f"{n}\t{t_sec:.4f}\t\t{t_arbol:.4f}")

    plt.plot(tamanios, tiempos_sec, label="secuencial", marker="o")
    plt.plot(tamanios, tiempos_arbol, label="árbol BST", marker="o")
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("N elementos")
    plt.ylabel("tiempo (ms)")
    plt.legend()
    os.makedirs("docs/capturas", exist_ok=True)
    plt.savefig("docs/capturas/experimento-tp3.png")


if __name__ == "__main__":
    main()
