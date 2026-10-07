class NodoAVL:
    """Nodo de un árbol AVL."""

    def __init__(self, dato):
        self.dato = dato
        self.izquierdo = None
        self.derecho = None
        self.altura = 1


class ArbolAVL:
    """Árbol AVL que se mantiene balanceado automáticamente."""

    def __init__(self):
        self.raiz = None

    # ---------- ALTURA ----------

    def _altura(self, nodo):
        if nodo is None:
            return 0
        return nodo.altura

    def _actualizar_altura(self, nodo):
        nodo.altura = 1 + max(
            self._altura(nodo.izquierdo),
            self._altura(nodo.derecho)
        )

    # ---------- FACTOR DE BALANCE ----------

    def _factor_balance(self, nodo):
        if nodo is None:
            return 0

        return (
            self._altura(nodo.izquierdo)
            - self._altura(nodo.derecho)
        )

    # ---------- ROTACIÓN DERECHA ----------

    def _rotacion_derecha(self, nodo):
        nuevo_raiz = nodo.izquierdo
        subarbol = nuevo_raiz.derecho

        nuevo_raiz.derecho = nodo
        nodo.izquierdo = subarbol

        self._actualizar_altura(nodo)
        self._actualizar_altura(nuevo_raiz)

        return nuevo_raiz

    # ---------- ROTACIÓN IZQUIERDA ----------

    def _rotacion_izquierda(self, nodo):
        nuevo_raiz = nodo.derecho
        subarbol = nuevo_raiz.izquierdo

        nuevo_raiz.izquierdo = nodo
        nodo.derecho = subarbol

        self._actualizar_altura(nodo)
        self._actualizar_altura(nuevo_raiz)

        return nuevo_raiz

    # ---------- INSERTAR ----------

    def insertar(self, dato, clave):
        """Inserta un elemento y balancea el árbol."""
        self.raiz = self._insertar_recursivo(
            self.raiz, dato, clave
        )

    def _insertar_recursivo(self, nodo, dato, clave):

        if nodo is None:
            return NodoAVL(dato)

        if clave(dato) < clave(nodo.dato):
            nodo.izquierdo = self._insertar_recursivo(
                nodo.izquierdo, dato, clave
            )
        else:
            nodo.derecho = self._insertar_recursivo(
                nodo.derecho, dato, clave
            )

        self._actualizar_altura(nodo)

        balance = self._factor_balance(nodo)

        # Caso izquierda-izquierda
        if balance > 1 and clave(dato) < clave(nodo.izquierdo.dato):
            return self._rotacion_derecha(nodo)

        # Caso derecha-derecha
        if balance < -1 and clave(dato) >= clave(nodo.derecho.dato):
            return self._rotacion_izquierda(nodo)

        # Caso izquierda-derecha
        if balance > 1 and clave(dato) >= clave(nodo.izquierdo.dato):
            nodo.izquierdo = self._rotacion_izquierda(
                nodo.izquierdo
            )
            return self._rotacion_derecha(nodo)

        # Caso derecha-izquierda
        if balance < -1 and clave(dato) < clave(nodo.derecho.dato):
            nodo.derecho = self._rotacion_derecha(
                nodo.derecho
            )
            return self._rotacion_izquierda(nodo)

        return nodo

    # ---------- BUSCAR ----------

    def buscar(self, valor, clave):
        """Busca un elemento por su clave."""
        return self._buscar_recursivo(
            self.raiz, valor, clave
        )

    def _buscar_recursivo(self, nodo, valor, clave):

        if nodo is None:
            return None

        if valor == clave(nodo.dato):
            return nodo.dato

        if valor < clave(nodo.dato):
            return self._buscar_recursivo(
                nodo.izquierdo, valor, clave
            )

        return self._buscar_recursivo(
            nodo.derecho, valor, clave
        )

    # ---------- RECORRIDO INORDER ----------

    def inorder(self):
        """Devuelve los elementos ordenados por clave."""
        resultado = []
        self._inorder_recursivo(self.raiz, resultado)
        return resultado

    def _inorder_recursivo(self, nodo, resultado):

        if nodo is not None:
            self._inorder_recursivo(
                nodo.izquierdo, resultado
            )

            resultado.append(nodo.dato)

            self._inorder_recursivo(
                nodo.derecho, resultado
            )

    # ---------- RECORRIDO PREORDER ----------

    def preorder(self):
        """Raíz → izquierda → derecha."""
        resultado = []
        self._preorder_recursivo(self.raiz, resultado)
        return resultado

    def _preorder_recursivo(self, nodo, resultado):
        if nodo is not None:
            resultado.append(nodo.dato)
            self._preorder_recursivo(nodo.izquierdo, resultado)
            self._preorder_recursivo(nodo.derecho, resultado)

    # ---------- RECORRIDO POSTORDER ----------

    def postorder(self):
        """Izquierda → derecha → raíz."""
        resultado = []
        self._postorder_recursivo(self.raiz, resultado)
        return resultado

    def _postorder_recursivo(self, nodo, resultado):
        if nodo is not None:
            self._postorder_recursivo(nodo.izquierdo, resultado)
            self._postorder_recursivo(nodo.derecho, resultado)
            resultado.append(nodo.dato)

    # ---------- ALTURA DEL ÁRBOL ----------

    def altura(self):
        """Devuelve la altura del árbol."""
        return self._altura(self.raiz)