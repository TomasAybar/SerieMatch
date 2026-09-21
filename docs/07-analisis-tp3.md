## Resultado del algoritmo probar_bst.py

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

## Problemas al ejecutar ```python algoritmos/probar_bst.py```

en caso de que arroje algun error el comando de ejecucion:

```python -m algoritmos.probar_bst```

intente ejecutando:

```python -m algoritmos.probar_bst```

## 6. Resultados 

| N elementos | secuencial_ms | binaria_ms | arbol_ms |
|---|---:|---:|---:|
| 100 | 0.012 ms | 0.004 ms | base |
| 1.000 | 0.115 ms | 0.006 ms | ~10x |
| 10.000 | 1.140 ms | 0.009 ms | ~10x |
| 100.000 | 11.30 ms | 0.012 ms | ~10x |

| N elementos | Secuencial (ms) | Binaria (ms) | Árbol BST (ms) |
|-----------|-----------|-----------|-------------  |
|100          |0.0107           |0.0090          |0.037193  |
|1000         |0.0797           |0.0661          |0.028133 |
|10000        |0.6250           |0.6437          |0.077963|
|100000        |7.2725           |9.5880          |0.029325|
