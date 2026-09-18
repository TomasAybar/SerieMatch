import timeit
import matplotlib.pyplot as plt
from modelos.catalogo import Catalogo

def main() -> None:
    tamanios = (100, 1_000, 10_000, 100_000)
    tiempos_sec = []
    tiempos_bin = []

    for n in tamanios:
        catalogo = Catalogo()
        catalogo.cargar_desde_json(f"datos/series_{n}.json")
        catalogo.ordenar_por_titulo()

        titulo_probe = f"Serie {n - 1}"  # existe → no rompe el caso "no encontrado"

        t_sec = min(timeit.repeat(lambda: catalogo.buscar(titulo_probe), number=20, repeat=5)) / 20 * 1000
        t_bin = min(timeit.repeat(lambda: catalogo.buscar_binaria(titulo_probe), number=20, repeat=5)) / 20 * 1000

        tiempos_sec.append(t_sec)
        tiempos_bin.append(t_bin)
        print(f"{n}\t{t_sec:.4f}\t\t{t_bin:.4f}")

    # armar y guardar el gráfico
    plt.plot(tamanios, tiempos_sec, label="secuencial", marker="o")
    plt.plot(tamanios, tiempos_bin, label="binaria", marker="o")
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("N elementos")
    plt.ylabel("tiempo (ms)")
    plt.legend()
    plt.savefig("docs/capturas/experimento-tp2.png")

if __name__ == "__main__":
    main()