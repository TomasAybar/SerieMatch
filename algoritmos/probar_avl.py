from estructuras.arbol_binario import ArbolBST
from estructuras.avl import ArbolAVL
from estructuras.arbol_general import ArbolGeneral


def clave(numero):
    return numero


# ===================================================
# PRUEBA 1: Comparación BST vs AVL con datos ordenados
# ===================================================

print("=" * 50)
print("PRUEBA 1: BST vs AVL con 100 datos ordenados")
print("=" * 50)

numeros = list(range(1, 101))

bst = ArbolBST()
avl = ArbolAVL()

for numero in numeros:
    bst.insertar(numero, clave)
    avl.insertar(numero, clave)

print(f"Cantidad de datos: {len(numeros)}")
print(f"\n--- BST ---")
print(f"Altura: {bst.altura()}")
print(f"\n--- AVL ---")
print(f"Altura: {avl.altura()}")


# ===================================================
# PRUEBA 2: Recorridos del AVL (inorder, preorder, postorder)
# ===================================================

print("\n" + "=" * 50)
print("PRUEBA 2: Recorridos del AVL con 10 datos ordenados")
print("=" * 50)

avl_pequeño = ArbolAVL()
for n in range(1, 11):
    avl_pequeño.insertar(n, clave)

print("Inorder   (ordenado):", avl_pequeño.inorder())
print("Preorder  (raíz primero):", avl_pequeño.preorder())
print("Postorder (raíz al final):", avl_pequeño.postorder())
print("Altura del árbol:", avl_pequeño.altura())


# ===================================================
# PRUEBA 3: Las 4 rotaciones del AVL
# ===================================================

print("\n" + "=" * 50)
print("PRUEBA 3: Casos de rotación del AVL")
print("=" * 50)

# LL → rotación derecha
avl_ll = ArbolAVL()
for n in [30, 20, 10]:
    avl_ll.insertar(n, clave)
print(f"LL [30,20,10] → inorder: {avl_ll.inorder()}, altura: {avl_ll.altura()}")

# RR → rotación izquierda
avl_rr = ArbolAVL()
for n in [10, 20, 30]:
    avl_rr.insertar(n, clave)
print(f"RR [10,20,30] → inorder: {avl_rr.inorder()}, altura: {avl_rr.altura()}")

# LR → rotación doble izquierda-derecha
avl_lr = ArbolAVL()
for n in [30, 10, 20]:
    avl_lr.insertar(n, clave)
print(f"LR [30,10,20] → inorder: {avl_lr.inorder()}, altura: {avl_lr.altura()}")

# RL → rotación doble derecha-izquierda
avl_rl = ArbolAVL()
for n in [10, 30, 20]:
    avl_rl.insertar(n, clave)
print(f"RL [10,30,20] → inorder: {avl_rl.inorder()}, altura: {avl_rl.altura()}")


# ===================================================
# PRUEBA 4: Árbol General con jerarquía de dominio
# ===================================================

print("\n" + "=" * 50)
print("PRUEBA 4: Árbol General — jerarquía Catálogo → Género → Serie")
print("=" * 50)

arbol = ArbolGeneral()
arbol.insertar_raiz("Catálogo de Series")

drama = arbol.agregar_hijo(arbol.raiz, "Drama")
accion = arbol.agregar_hijo(arbol.raiz, "Ciencia Ficción")
comedia = arbol.agregar_hijo(arbol.raiz, "Thriller")

arbol.agregar_hijo(drama, "Breaking Bad")
arbol.agregar_hijo(drama, "Game of Thrones")
arbol.agregar_hijo(drama, "The Crown")

arbol.agregar_hijo(accion, "Black Mirror")
arbol.agregar_hijo(accion, "Westworld")

arbol.agregar_hijo(comedia, "Mindhunter")
arbol.agregar_hijo(comedia, "Ozark")

print(f"Raíz: {arbol.raiz.dato}")
print(f"Altura: {arbol.altura()}")
print(f"Total de nodos: {arbol.cantidad_nodos()}")

print("\n--- Recorrido en amplitud (BFS) ---")
print(arbol.amplitud())

print("\n--- Recorrido en profundidad preorder ---")
print(arbol.profundidad_preorder())

print("\n--- Recorrido en profundidad postorder ---")
print(arbol.profundidad_postorder())

print("\n--- Niveles del árbol ---")
for i, nivel in enumerate(arbol.obtener_niveles()):
    print(f"  Nivel {i}: {nivel}")

print("\n--- Búsqueda: nodo 'Drama' ---")
nodo = arbol.buscar("Drama")
print(f"  Encontrado: {nodo}")
print(f"  Hijos: {arbol.listar_hijos(nodo)}")

print("\n--- Búsqueda: nodo inexistente 'Comedia' ---")
nodo_inexistente = arbol.buscar("Comedia")
print(f"  Resultado: {nodo_inexistente}")
