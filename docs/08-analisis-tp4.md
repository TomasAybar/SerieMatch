# Análisis TP4 — Árbol AVL

## 1. ¿Qué resolvimos?

En esta etapa implementamos un árbol AVL para complementar el árbol
binario de búsqueda (BST) realizado en la etapa anterior.

El objetivo principal fue evitar que el árbol pierda el balance cuando
los elementos se insertan en determinados órdenes.

El árbol AVL realiza rotaciones automáticamente cuando detecta que una
parte del árbol está demasiado cargada hacia un lado.

---

## 2. Implementación del árbol AVL

Se creó la clase `ArbolAVL` en:

`estructuras/avl.py`

El árbol cuenta con:

- Inserción de elementos.
- Búsqueda por clave.
- Recorrido inorder.
- Cálculo de altura.
- Cálculo del factor de balance.
- Rotación simple a la derecha.
- Rotación simple a la izquierda.
- Rotación doble izquierda-derecha.
- Rotación doble derecha-izquierda.

Cada nodo almacena también su altura para poder determinar si el árbol
necesita ser rebalanceado.

---

## 3. Factor de balance

Para determinar si un nodo está balanceado se utiliza el factor de
balance:

**Factor de balance = altura del subárbol izquierdo - altura del
subárbol derecho**

Un nodo está correctamente balanceado cuando su factor se encuentra
entre -1 y 1.

Cuando el valor supera esos límites, el AVL realiza una rotación para
volver a equilibrar el árbol.

---

## 4. Prueba de las rotaciones

Se probaron los cuatro casos posibles de desbalance.

### Caso LL

Datos insertados:

`[30, 20, 10]`

Se produce un desbalance hacia la izquierda y se realiza una rotación
simple a la derecha.

Resultado:

- Raíz: 20
- Inorder: `[10, 20, 30]`
- Altura: 2

### Caso RR

Datos insertados:

`[10, 20, 30]`

Se produce un desbalance hacia la derecha y se realiza una rotación
simple a la izquierda.

Resultado:

- Raíz: 20
- Inorder: `[10, 20, 30]`
- Altura: 2

### Caso LR

Datos insertados:

`[30, 10, 20]`

Se produce un desbalance izquierda-derecha y se realizan dos
rotaciones para corregirlo.

Resultado:

- Raíz: 20
- Inorder: `[10, 20, 30]`
- Altura: 2

### Caso RL

Datos insertados:

`[10, 30, 20]`

Se produce un desbalance derecha-izquierda y se realizan dos
rotaciones para corregirlo.

Resultado:

- Raíz: 20
- Inorder: `[10, 20, 30]`
- Altura: 2

Las cuatro pruebas finalizaron correctamente.

---

## 5. Comparación entre BST y AVL

Para comparar ambos árboles se utilizaron los mismos datos y el mismo
orden de inserción:

`[10, 20, 30, 40, 50]`

Resultados:

| Estructura | Altura |
|---|---:|
| BST | 5 |
| AVL | 3 |

Ambos árboles mantienen el mismo orden de los elementos al realizar el
recorrido inorder, pero el AVL consigue una estructura más equilibrada.

---

## 6. Prueba con 100 elementos

Para observar mejor la diferencia entre ambas estructuras se
insertaron 100 números en orden:

`[1, 2, 3, ..., 100]`

Los resultados fueron:

| Estructura | Cantidad de datos | Altura |
|---|---:|---:|
| BST | 100 | 100 |
| AVL | 100 | 7 |

En el BST, al insertar los números ordenados, cada nuevo elemento queda
a la derecha del anterior. Como consecuencia, el árbol termina
teniendo una estructura similar a una lista y su altura alcanza 100.

En cambio, el AVL realiza rotaciones durante las inserciones y mantiene
una estructura equilibrada, alcanzando una altura de solamente 7.

---

## 7. Conclusión

Las pruebas realizadas permiten comprobar la principal ventaja de un
árbol AVL frente a un BST sin balanceo.

Cuando los datos se insertan en un orden desfavorable, un BST puede
degradarse y alcanzar una altura muy grande. Esto puede afectar el
rendimiento de las operaciones de búsqueda e inserción.

El AVL evita esta situación mediante el cálculo del factor de balance y
la aplicación automática de rotaciones.

En la prueba con 100 elementos insertados en orden, el BST alcanzó una
altura de 100, mientras que el AVL mantuvo una altura de 7.

Por lo tanto, el AVL resulta más conveniente cuando se necesita
mantener una estructura de búsqueda equilibrada y evitar que el árbol
se degenere.