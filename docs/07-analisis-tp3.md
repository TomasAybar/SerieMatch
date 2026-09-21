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

| N elementos | Secuencial (ms) | Árbol BST (ms) |
|---|---:|---:|
| 100 | 0.0064 | 0.0042 |
| 1.000 | 0.0633 | 0.0062 |
| 10.000 | 0.6464 | 0.0083 |
| 100.000 | 7.0750  | 0.0104 |