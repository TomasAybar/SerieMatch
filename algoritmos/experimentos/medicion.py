
import os
import random
import time
import timeit

import matplotlib.pyplot as plt

from estructuras.arbol_binario import ArbolBST
from modelos.catalogo import Catalogo

ruta_cargar_series = 'datos/generados/series_'

ruta_guardar_graficos = "docs/capturas"

def crear_grafico(tamaños, secuencial, binaria, arbol):
    
    plt.plot(tamaños, secuencial, label="secuencial", marker='o')
    plt.plot(tamaños, binaria, label="binaria", marker='o')
    plt.plot(tamaños, arbol, label="arbol", marker='o')
    
    plt.xscale("log")
    plt.yscale("log")

    plt.xlabel("N elementos")
    plt.ylabel("tiempo (ms)")

    plt.legend()
    
    os.makedirs(ruta_guardar_graficos, exist_ok=True)
    plt.savefig(f"{ruta_guardar_graficos}/experimento-tp3.png", dpi=300)
    print(f"\nGráfico guardado en '{ruta_guardar_graficos}/experimento-tp3.png'")
    plt.close()

def medir_arbol(lista, titulo):
    """Mide la búsqueda en árbol sobre la lista dada."""
    arbol = ArbolBST()
    lista_desordenada = list(lista)
    random.shuffle(lista_desordenada)
    for e in lista_desordenada:
        arbol.insertar(e, clave=lambda e: e.titulo.lower())
    inicio = time.time()
    resultado = arbol.buscar(titulo.lower(), clave=lambda e: e.titulo.lower())
    fin = time.time()
    return (fin - inicio) * 1000 # milisegundos

def main() -> None:

    tamaños = (100, 1_000, 10_000, 100_000)
    tiempos_sec = []
    tiempos_bin = []
    tiempos_arbol = []

    print("tamaño\tsecuencial_ms\tbinaria_ms\tarbol_ms")

    for n in tamaños:
        catalogo = Catalogo()

        catalogo.cargar_desde_json(f"{ruta_cargar_series}{n}.json")
        catalogo.ordenar_por_titulo()
        
        titulo_probe = f"Serie {n - 1}" # existe → no rompe el caso "no encontrado"

        t_sec = min(timeit.repeat(lambda: catalogo.buscar(titulo_probe), number=20, repeat=5)) / 20 * 1000
        t_bin = min(timeit.repeat(lambda: catalogo.buscar_binaria(titulo_probe), number=20, repeat=5)) / 20 * 1000
        t_bst = medir_arbol(catalogo.series, titulo_probe)

        tiempos_sec.append(t_sec)
        tiempos_bin.append(t_bin)
        tiempos_arbol.append(t_bst)

        print(f"{n}\t{t_sec:.4f}\t\t{t_bin:.4f}\t\t{t_bst:.4f}")

    crear_grafico(tamaños, tiempos_sec, tiempos_bin, tiempos_arbol)    

        
if __name__ == "__main__":
    main()