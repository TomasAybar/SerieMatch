import os
import sys

# Permite ejecutar el script directamente (python algoritmos/probar_bst.py)
# agregando la raíz del proyecto al path de imports.
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from estructuras.arbol_binario import ArbolBST
from modelos.serie import Serie


def main():
    arbol = ArbolBST()

    # Lo construimos SIN orden, para que el árbol ordene solo
    datos = [
        Serie(id=1, titulo="Stranger Things", generos=["Sci-Fi", "Terror"], duracion_min=50,
              puntuacion=8.7, plataforma="Netflix", sinopsis="..."),
        Serie(id=2, titulo="Breaking Bad", generos=["Drama", "Crimen"], duracion_min=47,
              puntuacion=9.5, plataforma="Netflix", sinopsis="..."),
        Serie(id=3, titulo="The Office", generos=["Comedia"], duracion_min=22,
              puntuacion=8.9, plataforma="Prime Video", sinopsis="..."),
        Serie(id=4, titulo="Game of Thrones", generos=["Fantasía", "Drama"], duracion_min=57,
              puntuacion=9.2, plataforma="HBO Max", sinopsis="..."),
        Serie(id=5, titulo="Dark", generos=["Sci-Fi", "Misterio"], duracion_min=60,
              puntuacion=8.8, plataforma="Netflix", sinopsis="..."),
    ]

    for d in datos:
        arbol.insertar(d, clave=lambda e: e.titulo.lower())

    print("Altura del árbol:", arbol.altura())

    print("\n--- inorder (ordenado alfabéticamente) ---")
    for e in arbol.inorder():
        print(" ", e)

    print("\n--- preorder ---")
    for e in arbol.preorder():
        print(" ", e.titulo)

    print("\n--- postorder ---")
    for e in arbol.postorder():
        print(" ", e.titulo)

    print("\n--- búsquedas ---")
    encontrado = arbol.buscar("breaking bad", clave=lambda e: e.titulo.lower())
    print("Buscar 'breaking bad':", encontrado)

    no_encontrado = arbol.buscar("zzz", clave=lambda e: e.titulo.lower())
    print("Buscar 'zzz':", no_encontrado)


if __name__ == "__main__":
    main()