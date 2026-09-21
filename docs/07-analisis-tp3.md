## 1. ¿Qué resolvimos?

En este TP3 implementamos y analizamos un Árbol Binario de Búsqueda (BST) para mejorar la búsqueda de series dentro del catálogo de SerieMatch.

El árbol utiliza como criterio de ordenamiento el título de cada serie. Se implementaron operaciones de inserción, búsqueda y recorridos del árbol, incluyendo inorder, preorder y postorder.

Además, realizamos pruebas con diferentes cantidades de elementos y comparamos los tiempos de búsqueda utilizando tres métodos: búsqueda secuencial, búsqueda binaria y búsqueda mediante un árbol BST.

El objetivo fue analizar el funcionamiento de estas estructuras y comparar su comportamiento a medida que aumenta la cantidad de datos.

## 2. Clave de ordenamiento

La clave utilizada para ordenar las series dentro del Árbol Binario de Búsqueda es el atributo titulo.

Para realizar las comparaciones se utiliza el título convertido a minúsculas mediante lower(). De esta manera, la búsqueda no depende de si el usuario ingresa el título utilizando mayúsculas o minúsculas.

Por ejemplo, para la serie "Breaking Bad", la clave utilizada para realizar la comparación es:

breaking bad

Esto permite mantener un criterio de ordenamiento alfabético y realizar búsquedas por título.

## 3. Prueba del árbol
Salida de `python -m algoritmos.probar_bst`:

```
Altura del árbol: 4

--- inorder (ordenado alfabéticamente) ---
  Serie: Breaking Bad Plataforma: Netflix ⭐Puntuacion: 9.5
  Serie: Dark Plataforma: Netflix ⭐Puntuacion: 8.8
  Serie: Game of Thrones Plataforma: HBO Max ⭐Puntuacion: 9.2
  Serie: Stranger Things Plataforma: Netflix ⭐Puntuacion: 8.7
  Serie: The Office Plataforma: Prime Video ⭐Puntuacion: 8.9

--- preorder ---
  Stranger Things
  Breaking Bad
  Game of Thrones
  Dark
  The Office

--- postorder ---
  Dark
  Game of Thrones
  Breaking Bad
  The Office
  Stranger Things

--- búsquedas ---
Buscar 'breaking bad': Serie: Breaking Bad Plataforma: Netflix ⭐Puntuacion: 9.5
Buscar 'zzz': None

```

## Problemas al ejecutar ```python algoritmos/probar_bst.py```

en caso de que arroje algun error el comando de ejecucion:

```python -m algoritmos.probar_bst```

intente ejecutando:

```python -m algoritmos.probar_bst```


## 4. Comparación de tiempos 


| N elementos | Secuencial (ms) | Binaria (ms) | Árbol BST (ms) |
|-----------|-----------|-----------|-------------  |
|100          |0.0079           |0.0086          |0.0048  |
|1000         |0.0611           |0.0686          |0.0057 |
|10000        |0.6220           |0.6471          |0.0064|
|100000        |6.7825           |8.7617          |0.0062|


```
tamaño  secuencial_ms   binaria_ms      arbol_ms
¡Éxito! Se cargaron 100 series al catálogo.
100     0.0079          0.0086          0.0048
¡Éxito! Se cargaron 1000 series al catálogo.
1000    0.0611          0.0686          0.0057
¡Éxito! Se cargaron 10000 series al catálogo.
10000   0.6220          0.6471          0.0064
¡Éxito! Se cargaron 100000 series al catálogo.
100000  6.7825          8.7617          0.0062
```

![Resultados TP3](capturas/experimento-tp3.png)

## 5. Análisis de complejidad

La búsqueda secuencial tiene una complejidad temporal de O(n), ya que en el peor caso debe recorrer todos los elementos hasta encontrar la serie buscada.

La búsqueda binaria tiene una complejidad temporal de O(log n), siempre que los elementos se encuentren ordenados y se pueda acceder a ellos por posición.

En un Árbol Binario de Búsqueda, la búsqueda tiene una complejidad promedio de O(log n) cuando el árbol se encuentra razonablemente balanceado. Sin embargo, si el árbol queda desbalanceado, la complejidad puede llegar a O(n), ya que puede comportarse de forma similar a una lista.

En las pruebas realizadas se observó que el BST obtuvo tiempos de búsqueda muy bajos en comparación con los otros métodos. Sin embargo, estos resultados corresponden a la implementación y a los datos utilizados en el experimento, por lo que no significan que el BST siempre sea más rápido.

Los resultados permiten observar cómo las estructuras de datos pueden afectar el rendimiento de las búsquedas cuando aumenta la cantidad de elementos.

## 6. Conclusión

A partir de este TP pudimos implementar y poner en práctica un Árbol Binario de Búsqueda aplicado al catálogo de series de SerieMatch.

Las pruebas realizadas permitieron comprobar el funcionamiento de las diferentes operaciones del árbol y observar los resultados de sus recorridos y búsquedas.

También comparamos la búsqueda secuencial, la búsqueda binaria y la búsqueda mediante BST utilizando diferentes cantidades de elementos. Los resultados mostraron que el método de búsqueda y la estructura utilizada pueden influir considerablemente en el tiempo de ejecución.

Además, durante el desarrollo encontramos problemas relacionados con la construcción de árboles desbalanceados y con la recursividad, lo que nos permitió comprender mejor las limitaciones de una implementación de BST que no utiliza balanceo automático.

En conclusión, el TP nos permitió aplicar los conceptos de árboles binarios de búsqueda, complejidad algorítmica y medición de rendimiento a un caso concreto dentro del proyecto SerieMatch.

## 7. Errores o dudas que tuvimos

- problemas al ejecutar el comando `python algoritmos/probar_bst.py` la solucion fue ejecutar el script de la siguiente forma `python -m algoritmos.probar_bst`

- al ejecutar el script ocurria un error `RecursionError`, el problema era que el arbol estaba ordenado alfabeticamente por titulo, la solucion fue mezclar el orden utilizando random.shuffle antes de construirlo

```File "<frozen runpy>", line 203, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\frias\OneDrive\Desktop\SerieMatch\algoritmos\experimentos\medicion.py", line 77, in <module>
    main()
    ~~~~^^
  File "C:\Users\frias\OneDrive\Desktop\SerieMatch\algoritmos\experimentos\medicion.py", line 65, in main
    t_bst = medir_arbol(catalogo.series, titulo_probe)
  File "C:\Users\frias\OneDrive\Desktop\SerieMatch\algoritmos\experimentos\medicion.py", line 40, in medir_arbol
    arbol.insertar(e, clave=lambda e: e.titulo.lower())
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\frias\OneDrive\Desktop\SerieMatch\estructuras\arbol_binario.py", line 21, in insertar
    self._insertar_recursivo(self.raiz, dato, clave)
    ~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\frias\OneDrive\Desktop\SerieMatch\estructuras\arbol_binario.py", line 33, in _insertar_recursivo
    self._insertar_recursivo(nodo.derecho, dato, clave)
    ~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\frias\OneDrive\Desktop\SerieMatch\estructuras\arbol_binario.py", line 33, in _insertar_recursivo
    self._insertar_recursivo(nodo.derecho, dato, clave)
    ~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\frias\OneDrive\Desktop\SerieMatch\estructuras\arbol_binario.py", line 33, in _insertar_recursivo
    self._insertar_recursivo(nodo.derecho, dato, clave)
    ~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
  [Previous line repeated 990 more times]
  File "C:\Users\frias\OneDrive\Desktop\SerieMatch\estructuras\arbol_binario.py", line 24, in _insertar_recursivo
    if clave(dato) < clave(nodo.dato):
       ~~~~~^^^^^^
RecursionError: maximum recursion depth exceeded```
