from estructuras.arbol_binario import ArbolBST

class Elemento:
    def __init__(self, titulo, rating):
        self.titulo = titulo
        self.rating = rating
    def __repr__(self):
        return f"{self.titulo} (rating {self.rating})"

def main():
    arbol = ArbolBST()
    # Lo construimos SIN orden, para que el árbol ordene solo
    datos = [
        Elemento("Matrix", 9.0),
        Elemento("Inception", 8.8),
        Elemento("Titanic", 7.8),
        Elemento("Blade Runner", 8.5),
        Elemento("Arrival", 8.4),
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
    encontrado = arbol.buscar("matrix", clave=lambda e: e.titulo.lower())
    print("Buscar 'matrix':", encontrado)
    no_encontrado = arbol.buscar("zzz", clave=lambda e: e.titulo.lower())
    print("Buscar 'zzz':", no_encontrado)

if __name__ == "__main__":
    main()