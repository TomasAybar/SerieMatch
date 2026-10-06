from estructuras.arbol_binario import ArbolBST
from estructuras.avl import ArbolAVL


def clave(numero):
    return numero


# -----------------------------------
# PRUEBA CON 100 DATOS
# -----------------------------------

numeros = list(range(1, 101))

bst = ArbolBST()
avl = ArbolAVL()


# Insertamos los mismos datos en ambos árboles
for numero in numeros:
    bst.insertar(numero, clave)
    avl.insertar(numero, clave)


# -----------------------------------
# RESULTADOS
# -----------------------------------

print("Cantidad de datos:", len(numeros))

print("\n--- BST ---")
print("Altura:", bst.altura())

print("\n--- AVL ---")
print("Altura:", avl.altura())